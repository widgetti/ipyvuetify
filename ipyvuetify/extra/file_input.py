import asyncio
import copy
import io
import os
import sys
import warnings

import IPython
import nest_asyncio
import traitlets
from ipywidgets import dlink, widget_serialization
from traitlets import Any, Bool, Dict, Float, Int, List, Unicode, Union

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
        self.size = widget.v_model[file_index]["size"]

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

        asyncio.run(read_all())
        return size

    def readall(self):
        return self.read(self.size - self.offset)


class FileInput(v.VuetifyTemplate):
    append_icon = Unicode(None, allow_none=True).tag(sync=True)

    append_outer_icon = Unicode(None, allow_none=True).tag(sync=True)

    autofocus = Bool(None, allow_none=True).tag(sync=True)

    background_color = Unicode(None, allow_none=True).tag(sync=True)

    chips = Bool(None, allow_none=True).tag(sync=True)

    clear_icon = Unicode(None, allow_none=True).tag(sync=True)

    clearable = Bool(None, allow_none=True).tag(sync=True)

    color = Unicode(None, allow_none=True).tag(sync=True)

    counter = Union([Bool(), Float(), Unicode()], default_value=None, allow_none=True).tag(
        sync=True
    )

    counter_size_string = Unicode(None, allow_none=True).tag(sync=True)

    counter_string = Unicode(None, allow_none=True).tag(sync=True)

    dark = Bool(None, allow_none=True).tag(sync=True)

    dense = Bool(None, allow_none=True).tag(sync=True)

    disabled = Bool(None, allow_none=True).tag(sync=True)

    error = Bool(None, allow_none=True).tag(sync=True)

    error_count = Union([Float(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), List(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    filled = Bool(None, allow_none=True).tag(sync=True)

    flat = Bool(None, allow_none=True).tag(sync=True)

    full_width = Bool(None, allow_none=True).tag(sync=True)

    height = Union([Float(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    # Missing Vuetify prop: hide-input

    hint = Unicode(None, allow_none=True).tag(sync=True)

    id = Unicode(None, allow_none=True).tag(sync=True)

    label = Unicode(None, allow_none=True).tag(sync=True)

    light = Bool(None, allow_none=True).tag(sync=True)

    loader_height = Union([Float(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), List(Any())], default_value=None, allow_none=True).tag(sync=True)

    multiple = Bool(None, allow_none=True).tag(sync=True)

    outlined = Bool(None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(None, allow_none=True).tag(sync=True)

    # Missing Vuetify prop: persistent-placeholder

    placeholder = Unicode(None, allow_none=True).tag(sync=True)

    prefix = Unicode(None, allow_none=True).tag(sync=True)

    prepend_icon = Unicode(None, allow_none=True).tag(sync=True)

    prepend_inner_icon = Unicode(None, allow_none=True).tag(sync=True)

    readonly = Bool(None, allow_none=True).tag(sync=True)

    reverse = Bool(None, allow_none=True).tag(sync=True)

    rounded = Bool(None, allow_none=True).tag(sync=True)

    rules = List(Any(), default_value=None, allow_none=True).tag(sync=True)

    shaped = Bool(None, allow_none=True).tag(sync=True)

    show_size = Union([Bool(), Float()], default_value=None, allow_none=True).tag(sync=True)

    single_line = Bool(None, allow_none=True).tag(sync=True)

    small_chips = Bool(None, allow_none=True).tag(sync=True)

    solo = Bool(None, allow_none=True).tag(sync=True)

    solo_inverted = Bool(None, allow_none=True).tag(sync=True)

    success = Bool(None, allow_none=True).tag(sync=True)

    success_messages = Union([Unicode(), List(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    suffix = Unicode(None, allow_none=True).tag(sync=True)

    truncate_length = Union([Float(), Unicode()], default_value=None, allow_none=True).tag(
        sync=True
    )

    type = Unicode(None, allow_none=True).tag(sync=True)

    validate_on_blur = Bool(None, allow_none=True).tag(sync=True)

    value = Any(None, allow_none=True).tag(sync=True)

    # VueWidget props

    v_model = List(Dict(), allow_none=True).tag(sync=True)

    style_ = Unicode(None, allow_none=True).tag(sync=True)

    class_ = Unicode(None, allow_none=True).tag(sync=True)

    attributes = Dict(None, allow_none=True).tag(sync=True)

    v_slots = List(Dict()).tag(sync=True, **widget_serialization)

    v_on = Unicode(None, allow_none=True).tag(sync=True)

    # Component-specific props

    template = Unicode(load_template("file_input.vue")).tag(sync=True)

    version = Int(0).tag(sync=True)

    total_progress = Int(0).tag(sync=True)

    progress_indeterminate = Bool(False).tag(sync=True)

    file_info = List(Dict(), allow_none=True)  # Deprecated, use v_model instead

    total_progress_inner = 0
    total_size_inner = 0

    def __init__(self, *args, **kwargs):
        self.chunk_listeners = {}
        self.stats = []

        # Keep default behaviour
        kwargs.setdefault("multiple", True)
        kwargs.setdefault("clearable", True)

        attributes = kwargs.setdefault("attributes", {})
        if "accept" in kwargs:
            warnings.warn(
                "accept argument is deprecated, use attributes dictionary instead",
                DeprecationWarning,
            )
            attributes["accept"] = kwargs["accept"]
            del kwargs["accept"]
        if "directory" in kwargs:
            warnings.warn(
                "directory argument is deprecated, use attributes dictionary instead",
                DeprecationWarning,
            )
            attributes["directory"] = kwargs["directory"]
            del kwargs["directory"]
        if "show_progress" in kwargs:
            warnings.warn(
                "show_progress argument is deprecated, use v_slots to change the progress slot",
                DeprecationWarning,
            )
            del kwargs["show_progress"]
        if "file_info" in kwargs:
            warnings.warn("file_info cannot be set on FileInput")
            del kwargs["file_info"]
        if "v_model" in kwargs:
            warnings.warn("v_model cannot be set on FileInput")
            del kwargs["v_model"]

        # Maintain backwards compatibility for the file_info
        dlink((self, "v_model"), (self, "file_info"))

        super().__init__(*args, **kwargs)

        if not hasattr(IPython.get_ipython(), "kernel"):
            return
        kernel = IPython.get_ipython().kernel
        if kernel.implementation == "ipython":
            nest_asyncio.apply()

    @property
    def accept(self):
        warnings.warn("accept is deprecated, use attributes dictionary instead", DeprecationWarning)
        if "accept" in self.attributes:
            return self.attributes["accept"]
        return ""

    @accept.setter
    def accept(self, value):
        warnings.warn("accept is deprecated, use attributes dictionary instead", DeprecationWarning)
        self.attributes = {**self.attributes, "accept": value}

    @property
    def directory(self):
        warnings.warn(
            "directory is deprecated, use attributes dictionary instead", DeprecationWarning
        )
        if "directory" in self.attributes:
            return self.attributes["directory"]
        return False

    @directory.setter
    def directory(self, value):
        warnings.warn(
            "directory is deprecated, use attributes dictionary instead", DeprecationWarning
        )
        self.attributes = {**self.attributes, "directory": value}

    @property
    def show_progress(self):
        warnings.warn(
            "show_progress is deprecated, use v_slots to change the progress slot",
            DeprecationWarning,
        )
        return True

    @show_progress.setter
    def show_progress(self, _):
        warnings.warn(
            "show_progress is deprecated, use v_slots to change the progress slot",
            DeprecationWarning,
        )

    @traitlets.observe("v_model")
    def _v_model_changed(self, _):
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
        for index, file in enumerate(self.v_model):
            file = copy.deepcopy(self.v_model[index])
            file["file_obj"] = ClientSideFile(self, index, timeout=timeout)
            files.append(file)
        return files

    def clear(self):
        self.reset_stats()
        self.send({"method": "clear", "args": []})

    def reset_stats(self):
        self.stats = [0 for _ in self.v_model]
        self.total_progress = 0
        self.total_progress_inner = 0
        self.total_size_inner = sum([f["size"] for f in self.v_model])

    def vue_upload(self, content, buffers):
        listener_id = content["id"]
        listener = self.chunk_listeners.get(listener_id)
        if listener:
            if listener.version != self.version:
                del self.chunk_listeners[listener_id]
            else:
                listener.handle_chunk(content, buffers[0])


__all__ = ["FileInput"]
