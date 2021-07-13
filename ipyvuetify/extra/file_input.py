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


class ClientSideFile(io.RawIOBase):

    def __init__(self, widget, file_index, timeout=30):
        global chunk_listener_id
        self.id = chunk_listener_id
        self.widget = widget
        self.version = widget.version
        self.file_index = file_index
        self.timeout = timeout
        self.valid = True
        self.offset = 0
        self.size = widget.file_info[file_index]['size']

        self.chunk_queue = []

        widget.chunk_listeners[self.id] = self

        chunk_listener_id += 1
        self.waits = 0

    def handle_chunk(self, content, buffer):
        content['buffer'] = buffer
        self.chunk_queue.append(content)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset = self.offset + offset
        elif whence == io.SEEK_END:
            self.offset = self.size + offset
        else:
            raise ValueError(f'whence {whence} invalid')

    def tell(self):
        return self.offset

    def readinto(self, buffer):
        if not self.valid:
            raise Exception('Invalid file state')
        bytes_read = 0
        mem = memoryview(buffer)

        remaining = max(0, self.size - self.offset)
        size = min(len(buffer), remaining)

        ipython = IPython.get_ipython()
        self.widget.send({
            'method': 'read',
            'args': [{
                'file_index': self.file_index,
                'offset': self.offset,
                'length': size,
                'id': self.id
            }]
        })

        sleep_interval = 0.01
        max_iterations = self.timeout / sleep_interval
        while bytes_read < size:
            iterations = 0
            while not self.chunk_queue:
                iterations += 1

                if self.version != self.widget.version:
                    self.valid = False
                    raise Exception('File changed')
                if iterations > max_iterations:
                    self.valid = False
                    raise Exception('Timeout')

                time.sleep(sleep_interval)
                ipython.kernel.do_one_iteration()

            self.waits += iterations

            chunk = self.chunk_queue[0]
            chunk_size = chunk['length']

            mem[bytes_read:bytes_read + chunk_size] = chunk['buffer']

            self.chunk_queue.pop(0)
            bytes_read += chunk_size
            self.offset += chunk_size

            self.widget.update_stats(self.file_index, chunk_size)
            ipython.kernel.do_one_iteration()

        return size

class FileInput(v.VuetifyTemplate):
    template = traitlets.Unicode(load_template('file_input.vue')).tag(sync=True)
    data = traitlets.Unicode('{myfiles: undefined}').tag(sync=True)

    file_info = traitlets.List().tag(sync=True)
    version = traitlets.Int(0).tag(sync=True)
    multiple = traitlets.Bool(True).tag(sync=True)
    disabled = traitlets.Bool(False).tag(sync=True)
    directory = traitlets.Bool(False).tag(sync=True)
    accept = traitlets.Unicode().tag(sync=True)
    total_progress = traitlets.Int(0).tag(sync=True)
    show_progress = traitlets.Bool(True).tag(sync=True)
    progress_indeterminate = traitlets.Bool(False).tag(sync=True)

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
        self.stats[file_index] += bytes_read
        tot = sum(self.stats)
        percent = round((tot / self.total_size_inner) * 100)
        if percent != self.total_progress_inner:
            self.total_progress_inner = percent
            self.total_progress = percent

    def get_files(self, timeout=30):
        files = []
        for index, file in enumerate(self.file_info):
            file = copy.deepcopy(self.file_info[index])
            file['file_obj'] = ClientSideFile(self, index, timeout=timeout)
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
