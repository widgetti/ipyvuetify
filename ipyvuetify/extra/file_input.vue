<template>
  <v-file-input
    :class="class_ || []"
    :style="style_ || {}"
    v-bind="props"
    @change="setFiles"
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
    <template v-for="slot in v_slots" :key="slot.name" v-slot:[slot.name]>
      <jupyter-widget :widget="slot.children" />
    </template>
  </v-file-input>
</template>

<script>
module.exports = {
  created() {
    this.chunk_size = 2 * 1024 * 1024;
  },
  computed: {
    computedLoadingValue: function () {
      const total_progress = this.$data["total_progress"];
      const progress_indeterminate = this.$data["progress_indeterminate"];
      return (
        (!progress_indeterminate || total_progress > 0) && total_progress < 100
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

      const attributes = this.$data["attributes"] || {};

      const props = keys.filter(useAsAttr).reduce(
        (result, key) => {
          result[key.replace(/_$/g, "").replace(/_/g, "-")] = this.$data[key];
          return result;
        },
        { ...attributes }
      );

      if (!("loading" in props)) {
        props["loading"] = this.computedLoadingValue;
      }

      return props;
    },
  },
  methods: {
    setFiles(value) {
      if (!value) {
        this.native_file_info = [];
        this.file_info = [];
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
      this.native_file_info = [];
      this.file_info = [];
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
