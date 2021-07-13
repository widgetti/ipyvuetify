<template>
    <div>
        <v-file-input v-model="myfiles" :disabled="disabled" :multiple="multiple" show-size show-counter clearable chips :counter="multiple" @change="setFiles"
                      :webkitdirectory="directory" :directory="directory" :accept="accept"/>
        <v-progress-linear
                v-if="(total_progress > 0 || progress_indeterminate) && show_progress"
                :indeterminate="progress_indeterminate"
                :value="progress_indeterminate ? 0 : total_progress"/>
    </div>
</template>

<script>
    modules.export = {
        created() {
            this.chunk_size = 2 * 1024 * 1024;
        },
        methods: {
            setFiles(e) {
                if (!e) {
                    this.native_file_info = [];
                    this.file_info = [];
                    return;
                }
                this.native_file_info = e instanceof File ? [e] : e;
                this.file_info = this.native_file_info.map(({name, size, lastModified, type}) => ({
                    name, size, lastModified, type
                }))
            },
            jupyter_clear() {
                this.myfiles = undefined;
                this.setFiles(false);
            },
            jupyter_read(chunk) {
                const {id, file_index, offset, length} = chunk;

                let to_do = length;
                let sub_offset = offset;

                (async () => {
                    while (to_do > 0) {
                        const sub_length = Math.min(to_do, this.chunk_size);

                        const file = this.native_file_info[file_index];
                        const blob = file.slice(sub_offset, sub_offset + sub_length);
                        const buff = await blob.arrayBuffer();

                        const msg = {id, file_index, offset: sub_offset, length: sub_length}
                        this.upload(msg, [buff]);

                        to_do -= sub_length
                        sub_offset += sub_length
                    }
                })();
            }
        },
    };
</script>
