import asyncio
import copy
import io
import os
import sys

import IPython

try:
    import nest_asyncio

    has_nest_asyncio = True
except ModuleNotFoundError:
    has_nest_asyncio = False

import traitlets

import ipyvuetify as v

chunk_listener_id = 0


def load_template(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


async def process_messages():
    ipython = IPython.get_ipython()
    original_parent_ident = ipython.kernel._parent_ident
    original_parent_header = ipython.kernel._parent_header
    original_set_parent = ipython.set_parent

    def set_parent_sink(*args):
        pass

    try:
        ipython.set_parent = set_parent_sink
        while not ipython.kernel.msg_queue.empty():
            await ipython.kernel.do_one_iteration()
    finally:
        # reset parent header to original execute request
        ipython.kernel.set_parent(
            original_parent_ident, original_parent_header
        )  # for execution count indicator
        sys.stdout.parent_header = original_parent_header  # for print statements
        sys.stderr.parent_header = original_parent_header  # for errors
        ipython.display_pub.parent_header = original_parent_header  # for display()
        ipython.set_parent = original_set_parent  # for displaying execution result


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
        self.size = widget.file_info[file_index]["size"]

        self.chunk_queue = []

        widget.chunk_listeners[self.id] = self

        chunk_listener_id += 1
        self.waits = 0

    def handle_chunk(self, content, buffer):
        content["buffer"] = buffer
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
            raise ValueError(f"whence {whence} invalid")

    def tell(self):
        return self.offset

    def readinto(self, buffer):
        if not self.valid:
            raise Exception("Invalid file state")
        mem = memoryview(buffer)

        remaining = max(0, self.size - self.offset)
        size = min(len(buffer), remaining)

        self.widget.send(
            {
                "method": "read",
                "args": [
                    {
                        "file_index": self.file_index,
                        "offset": self.offset,
                        "length": size,
                        "id": self.id,
                    }
                ],
            }
        )

        sleep_interval = 0.01
        max_iterations = self.timeout / sleep_interval

        async def read_all():
            bytes_read = 0
            while bytes_read < size:
                iterations = 0
                while not self.chunk_queue:
                    iterations += 1

                    if self.version != self.widget.version:
                        self.valid = False
                        raise Exception("File changed")
                    if iterations > max_iterations:
                        self.valid = False
                        raise Exception("Timeout")

                    await asyncio.sleep(sleep_interval)
                    await process_messages()

                self.waits += iterations

                chunk = self.chunk_queue[0]
                chunk_size = chunk["length"]

                mem[bytes_read : bytes_read + chunk_size] = chunk["buffer"]

                self.chunk_queue.pop(0)
                bytes_read += chunk_size
                self.offset += chunk_size

                self.widget.update_stats(self.file_index, chunk_size)
                await process_messages()

        def has_event_loop():
            try:
                asyncio.get_event_loop()
                return True
            except RuntimeError:
                return False

        if has_event_loop():
            # we already have an event loop in this thread, so to be able to call asyncio.run(...)
            # while also receiving messages from the frontend, we need to use nest_asyncio
            if not has_nest_asyncio:
                raise RuntimeError(
                    "nest_asyncio is required for FileInput when an event loop is already running in the current thread, "
                    "please run 'pip install nest_asyncio'."
                )
            else:
                nest_asyncio.apply()
        asyncio.run(read_all())
        return size

    def readall(self):
        return self.read(self.size - self.offset)


class FileInput(v.VuetifyTemplate):
    template = traitlets.Unicode(load_template("file_input.vue")).tag(sync=True)
    data = traitlets.Unicode("{myfiles: undefined}").tag(sync=True)

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

    @traitlets.observe("file_info")
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
            file["file_obj"] = ClientSideFile(self, index, timeout=timeout)
            files.append(file)
        return files

    def clear(self):
        self.reset_stats()
        self.send({"method": "clear", "args": []})

    def reset_stats(self):
        self.stats = [0 for _ in self.file_info]
        self.total_progress = 0
        self.total_progress_inner = 0
        self.total_size_inner = sum([f["size"] for f in self.file_info])

    def vue_upload(self, content, buffers):
        listener_id = content["id"]
        listener = self.chunk_listeners.get(listener_id)
        if listener:
            if listener.version != self.version:
                del self.chunk_listeners[listener_id]
            else:
                listener.handle_chunk(content, buffers[0])


__all__ = ["FileInput"]
