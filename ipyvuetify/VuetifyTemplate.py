from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization

import logging
logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("init")


class Events:
    def __init__(self):
        self.on_msg(self._handle_event)
        self.events = [item[4:] for item in dir(self) if item.startswith("vue_")]

    def _handle_event(self, _, content, buffers):
        event = content.get("event", "")
        data = content.get("data", {})
        logging.info(f"event: {event}, data: {data}")
        getattr(self, f'vue_{event}')(data)

    def log(self, msg):
        logging.info(msg)


class VuetifyTemplate(DOMWidget, Events):

    _model_name = Unicode('VuetifyTemplateModel').tag(sync=True)

    _view_name = Unicode('VuetifyTemplateView').tag(sync=True)

    _view_module = Unicode('jupyter-vuetify').tag(sync=True)

    _model_module = Unicode('jupyter-vuetify').tag(sync=True)

    _view_module_version = Unicode('0.1.0').tag(sync=True)

    _model_module_version = Unicode('0.1.0').tag(sync=True)

    template = Unicode(None, allow_none=True).tag(sync=True)

    events = List(Unicode(), default_value=None, allow_none=True).tag(sync=True)

    components = Dict(default_value=None, allow_none=True).tag(sync=True, **widget_serialization)

__all__ = ['AnyVue']

