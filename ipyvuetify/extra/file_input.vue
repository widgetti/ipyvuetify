<template>
    <div>
        <v-file-input v-model="myfiles" :disabled="disabled" :multiple="multiple" show-size show-counter clearable chips :counter="multiple" @change="setFiles"/>
        <v-progress-linear v-if="total_progress > 0" :value="total_progress"/>
    </div>
</template>

<script>
    modules.export = {
        created() {
            this.messages = [];
            this.no_msg_counter = 1000;

            const handle_message = () => {
                (async () => {
                    if (this.messages.length > 0) {
                        this.no_msg_counter = 0;

                        while (this.messages.length > 0) {
                            const chunk = this.messages[0];
                            const {file_index, offset, length} = chunk;
                            const file = this.native_file_info[file_index];
                            const blob = file.slice(offset, offset + length);
                            const buff = await blob.arrayBuffer();
                            this.upload(chunk, [buff]);
                            this.messages.shift();
                        }
                    } else {
                        this.no_msg_counter += 1
                    }
                    setTimeout(handle_message, this.no_msg_counter >= 1000 ? 1000 : 10);
                })();
            }
            handle_message();
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
            jupyter_send_chunk(chunk, buffers) {
                this.messages.push(chunk);
            },
            jupyter_clear() {
                this.myfiles = undefined;
                this.setFiles(false);
            },
        },
    };
</script>
