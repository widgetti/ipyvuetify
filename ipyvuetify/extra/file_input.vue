<template>
  <v-file-input
    ref="file-input"
    :class="class_ || []"
    :style="style_ || {}"
    v-bind="props"
    @change="setFiles"
    @click:clear="clear"
  >
    <template v-slot:progress>
      <v-progress-linear
        absolute
        :color="
          loading === null || loading === true || loading === ''
            ? color || 'primary'
            : loading
        "
        :height="loader_height || 4"
        :indeterminate="progress_indeterminate"
        :value="total_progress"
      />
    </template>
    <template v-for="slot in v_slots" v-slot:[slot.name]>
      <jupyter-widget :key="slot.name" :widget="slot.children" />
    </template>
  </v-file-input>
</template>

<script>
module.exports = {
  created() {
    this.chunk_size = 2 * 1024 * 1024;
  },
  mounted() {
    const fileInput = this.$refs["file-input"];
    const input = fileInput.$refs["input"];
    const inputSlot = fileInput.$refs["input-slot"];

    // Native drag & drop on input[type=file] seems to be supported in Chrome and Firefox since at least 2011:
    // - https://bugzilla.mozilla.org/show_bug.cgi?id=50660
    // - https://bugs.webkit.org/show_bug.cgi?id=58401

    input.classList.add("v-file-input-native-dropzone");

    input.addEventListener("click", (e) => {
      // Disable click propagation to label
      e.stopPropagation();
    });

    inputSlot.addEventListener("dragover", (e) => {
      // Enable custom drag-and-drop behaviour for any target except input
      if (e.target !== input) e.preventDefault();
      e.dataTransfer.dropEffect = "copy";
    });

    inputSlot.addEventListener("dragenter", (e) => {
      if (e.target !== input) e.preventDefault();
      if (!inputSlot.contains(e.relatedTarget)) {
        inputSlot.classList.add("v-file-input-custom-dropzone");
      }
    });

    inputSlot.addEventListener("dragleave", (e) => {
      if (e.target !== input) e.preventDefault();
      if (!inputSlot.contains(e.relatedTarget)) {
        inputSlot.classList.remove("v-file-input-custom-dropzone");
      }
    });

    // const supportsFileSystemAccessAPI =
    //   "getAsFileSystemHandle" in DataTransferItem.prototype;

    const supportsFileSystemAccessAPI = false;

    const dropHandler = async (e) => {
      if (e.target !== input) e.preventDefault();

      e.stopPropagation();

      inputSlot.classList.remove("v-file-input-custom-dropzone");

      let files;
      if (e.dataTransfer.items) {
        const fileDataTransferItems = [...e.dataTransfer.items].filter(
          (item) => item.kind === "file" // `file` misleadingly means actual file or directory
        );

        let getFiles;
        let hasDirectories;
        if (supportsFileSystemAccessAPI) {
          const fileSystemHandles = await Promise.all(
            fileDataTransferItems.map((item) => item.getAsFileSystemHandle())
          );

          hasDirectories = fileSystemHandles.some(
            (handle) => handle.kind === "directory"
          );

          getFiles = async () => this.getFileList([]); // FIXME: get FileList from FileSystemHandles
        } else {
          const fileSystemEntries = fileDataTransferItems.map((item) =>
            item.webkitGetAsEntry()
          );

          hasDirectories = fileSystemEntries.some((entry) => entry.isDirectory);

          getFiles = async () => this.getFileList(fileSystemEntries);
        }

        if (
          (!this.webkitdirectory && hasDirectories) ||
          (!this.multiple && hasDirectories) ||
          (!this.multiple && fileDataTransferItems.length > 1)
        ) {
          if (e.target === input) e.preventDefault(); // Skip native drag-and-drop handler
          return;
        }

        if (e.target === input) return; // Use native drag-and-drop handler

        if (
          !hasDirectories &&
          e.dataTransfer.files &&
          e.dataTransfer.files.length >= fileDataTransferItems.length
        ) {
          files = e.dataTransfer.files;
        } else {
          files = await getFiles();
        }
      } else {
        files = e.dataTransfer.files;
      }

      files = this.filterAcceptedFiles(files);

      input.files = files;
      input.dispatchEvent(new Event("change"));
    };

    input.addEventListener("drop", dropHandler);
    inputSlot.addEventListener("drop", dropHandler);
  },
  computed: {
    webkitdirectory: function () {
      return "webkitdirectory" in (this.attributes || {});
    },
    computedLoadingValue: function () {
      return (
        (!this.progress_indeterminate || this.total_progress > 0) &&
        this.total_progress < 100
      );
    },
    props: function () {
      const keys = [
        "append_icon",
        "append_outer_icon",
        "autofocus",
        "background_color",
        "chips",
        "clear_icon",
        "clearable",
        "color",
        "counter",
        "counter_size_string",
        "counter_string",
        "dark",
        "dense",
        "disabled",
        "error",
        "error_count",
        "error_messages",
        "filled",
        "flat",
        "full_width",
        "height",
        "hide_details",
        "hide_input",
        "hint",
        "id",
        "label",
        "light",
        "loader_height",
        "loading",
        "messages",
        "multiple",
        "outlined",
        "persistent_hint",
        "persistent_placeholder",
        "placeholder",
        "prefix",
        "prepend_icon",
        "prepend_inner_icon",
        "readonly",
        "reverse",
        "rounded",
        "rules",
        "shaped",
        "show_size",
        "single_line",
        "small_chips",
        "solo",
        "solo_inverted",
        "success",
        "success_messages",
        "suffix",
        "truncate_length",
        "type",
        "validate_on_blur",
        "value",
      ];

      const useAsAttr = (key) =>
        this.$data[key] !== null &&
        !key.startsWith("_") &&
        ![
          "attributes",
          "v_slots",
          "v_on",
          "layout",
          "children",
          "slot",
          "v_model",
          "style_",
          "class_",
        ].includes(key);

      const props = keys.filter(useAsAttr).reduce(
        (result, key) => {
          result[key.replace(/_$/g, "").replace(/_/g, "-")] = this.$data[key];
          return result;
        },
        { ...(this.attributes || {}) }
      );

      if (!("loading" in props)) {
        props["loading"] = this.computedLoadingValue;
      }

      return props;
    },
  },
  methods: {
    getFileList: async function (fileEntries) {
      async function readDirectoryEntry(directoryEntry) {
        const directoryReader = directoryEntry.createReader();
        const result = [];
        let entries;
        do {
          try {
            // readEntries will return only some of the entries in a directory
            // e.g. Chrome returns at most 100 entries at a time
            entries = await new Promise((resolve, reject) => {
              directoryReader.readEntries(resolve, reject);
            });
          } catch (error) {
            console.error(error);
            entries = [];
          }
          result.push(...entries);
        } while (entries.length > 0);
        return result;
      }

      const entries = [];

      const queue = [...fileEntries];

      while (queue.length > 0) {
        let entry = queue.shift();
        if (entry.isFile) {
          entries.push(entry);
        } else if (entry.isDirectory) {
          queue.push(...(await readDirectoryEntry(entry)));
        }
      }

      const files = await Promise.all(
        entries.map(
          (e) => new Promise((resolve, reject) => e.file(resolve, reject))
        )
      );

      const dt = new DataTransfer();
      files.forEach((file) => {
        dt.items.add(file);
      });

      return dt.files;
    },
    isAcceptedFile(file) {
      if (!this.accept) return true;
      for (const mime of this.accept.split(/\s*,\s*/)) {
        if (
          mime === file.type ||
          (/^\.[^/\\]+$/.test(mime) && file.name.endsWith(mime)) ||
          (/^[^/\\]+\/\*$/.test(mime) &&
            file.type.startsWith(mime.slice(0, -1)))
        )
          return true;
      }
      return false;
    },
    filterAcceptedFiles(files) {
      const acceptedFiles = [...files].filter(this.isAcceptedFile);
      if (acceptedFiles.length < files.length) {
        const dataTransfer = new DataTransfer();
        for (const file of acceptedFiles) {
          dataTransfer.items.add(file);
          if (!this.multiple) break;
        }
        return dataTransfer.files;
      }
      return files;
    },
    change(e) {
      if (!e.target) return;

      const files = e.target.files || [];

      this.setFiles(this.multiple ? [...files] : files[0]);
    },
    clear() {
      this.native_file_info = [];
      this.file_info = [];
    },
    setFiles(value) {
      if (!value) {
        this.clear();
        return;
      }
      this.native_file_info = value instanceof File ? [value] : value;
      this.file_info = this.native_file_info.map(
        ({ name, size, lastModified, type }) => ({
          name,
          size,
          lastModified,
          type,
        })
      );
    },
    jupyter_clear() {
      this.clear();
    },
    jupyter_read(chunk) {
      const { id, file_index, offset, length } = chunk;

      let to_do = length;
      let sub_offset = offset;

      (async () => {
        while (to_do > 0) {
          const sub_length = Math.min(to_do, this.chunk_size);

          const file = this.native_file_info[file_index];
          const blob = file.slice(sub_offset, sub_offset + sub_length);
          const buff = await blob.arrayBuffer();

          const msg = {
            id,
            file_index,
            offset: sub_offset,
            length: sub_length,
          };
          this.upload(msg, [buff]);

          to_do -= sub_length;
          sub_offset += sub_length;
        }
      })();
    },
  },
};
</script>

<style>
.v-file-input input[type="file"].v-file-input-native-dropzone {
  position: absolute;
  max-width: none;
  max-height: none;
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: 0;
  pointer-events: auto;
}

.v-file-input .v-file-input-custom-dropzone {
  outline-style: dashed;
}
</style>
