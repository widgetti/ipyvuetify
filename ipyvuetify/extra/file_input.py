import ipyvuetify as v
import traitlets
import time
import io
import os
import IPython
import copy

chunk_listener_id = 0


def load_template(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


class SeqClientSideFile(io.RawIOBase):

    def __init__(self, widget, file_index):
        global chunk_listener_id
        self.id = chunk_listener_id
        self.widget = widget
        self.version = widget.version
        self.widget = widget
        self.file_index = file_index
        self.valid = True
        self.offset = 0
        self.size = widget.file_info[file_index]['size']

        self.chunk_buffer_size = 7
        self.chunk_size = 2 * 1024 * 1024
        self.chunk_req_counter = 0
        self.chunk_resp_counter = 0

        self.chunk_queue = []

        widget.chunk_listeners[self.id] = self

        chunk_listener_id += 1
        self.waits = 0

    def handle_chunk(self, content, buffer):
        self.chunk_queue.append({
            'offset': content['offset'],
            'buffer': buffer
        })
        self.chunk_resp_counter += 1

    def readable(self):
        return True

    def seekable(self):
        return False

    def tell(self):
        return self.offset

    def _manage_chunks(self):
        while self.chunk_queue and self.chunk_queue[0]['offset'] + self.chunk_size <= self.offset:
            self.chunk_queue.pop(0)

        pending = self.chunk_req_counter - self.chunk_resp_counter
        offset = self.chunk_req_counter * self.chunk_size

        while self.chunk_buffer_size - len(self.chunk_queue) - pending > 0 and offset < self.size:
            remaining = self.size - offset
            length = min(remaining, self.chunk_size)
            self.widget.send({
                'method': 'send_chunk',
                'args': [{
                    'file_index': self.file_index,
                    'offset': offset,
                    'length': length,
                    'id': self.id
                }]
            })

            self.chunk_req_counter += 1
            pending = self.chunk_req_counter - self.chunk_resp_counter
            offset = self.chunk_req_counter * self.chunk_size

    def readinto(self, buffer):
        if not self.valid:
            raise Exception('Invalid file state')
        bytes_read = 0
        mem = memoryview(buffer)

        remaining = self.size - self.offset
        size = min(len(buffer), remaining)

        ipython = IPython.get_ipython()
        chunk_size = self.chunk_size

        while bytes_read < size:
            self._manage_chunks()

            ipython.kernel.do_one_iteration()
            iterations = 0
            while not self.chunk_queue:
                iterations += 1

                if self.version != self.widget.version:
                    self.valid = False
                    raise Exception('File changed')
                if iterations > 200:
                    self.valid = False
                    raise Exception('Timeout')

                time.sleep(0.01)
                ipython.kernel.do_one_iteration()

            self.waits += iterations

            chunk = self.chunk_queue[0]
            chunk_offset = self.offset - chunk['offset']

            bytes_remaining = size - bytes_read
            chunk_bytes_available = chunk_size - chunk_offset

            to_read = min(bytes_remaining, chunk_bytes_available)

            mem[bytes_read:bytes_read + to_read] = \
                chunk['buffer'][chunk_offset:chunk_offset + to_read]

            bytes_read += to_read
            self.offset += to_read

            self.widget.update_stats(self.file_index, self.offset)

        return size

    def read(self, size=-1):

        remaining = self.size - self.offset

        if remaining <= 0:
            return b''

        if size == -1:
            num_bytes = remaining
        else:
            num_bytes = min(remaining, size)

        buffer = bytearray(num_bytes)
        self.readinto(buffer)

        return buffer


class FileInput(v.VuetifyTemplate):
    template = traitlets.Unicode(load_template('file_input.vue')).tag(sync=True)
    data = traitlets.Unicode('{myfiles: undefined}').tag(sync=True)

    file_info = traitlets.List().tag(sync=True)
    version = traitlets.Int(0).tag(sync=True)
    multiple = traitlets.Bool(True).tag(sync=True)
    disabled = traitlets.Bool(False).tag(sync=True)
    total_progress = traitlets.Int(0).tag(sync=True)

    total_progress_inner = 0
    total_size_inner = 0

    def __init__(self, **kwargs):
        self.chunk_listeners = {}
        self.stats = []
        super().__init__(**kwargs)

    @traitlets.observe('file_info')
    def _file_info_changed(self, _):
        self.version += 1
        self.reset_stats()

    def update_stats(self, file_index, bytes_read):
        self.stats[file_index] = bytes_read
        tot = sum(self.stats)
        percent = round((tot / self.total_size_inner) * 100)
        if percent != self.total_progress_inner:
            self.total_progress_inner = percent
            self.total_progress = percent

    def get_files(self):
        files = []
        for index, file in enumerate(self.file_info):
            file = copy.deepcopy(self.file_info[index])
            file['file_obj'] = SeqClientSideFile(self, index)
            files.append(file)
        return files

    def clear(self):
        self.reset_stats()
        self.send({
            'method': 'clear',
            'args': []
        })

    def reset_stats(self):
        self.stats = [0 for _ in self.file_info]
        self.total_progress = 0
        self.total_progress_inner = 0
        self.total_size_inner = sum([f['size'] for f in self.file_info])

    def vue_upload(self, content, buffers):
        listener_id = content['id']
        listener = self.chunk_listeners.get(listener_id)
        if listener:
            if listener.version != self.version:
                del self.chunk_listeners[listener_id]
            else:
                listener.handle_chunk(content, buffers[0])


__all__ = ['FileInput']
