from traitlets import Unicode, List, Dict
from ipywidgets import DOMWidget
from ipywidgets.widgets.widget import widget_serialization


class Events(object):
    def __init__(self, **kwargs):
        self.on_msg(self._handle_event)
        self.events = [item[4:] for item in dir(self) if item.startswith("vue_")]

    def _handle_event(self, _, content, buffers):
        event = content.get("event", "")
        data = content.get("data", {})
        getattr(self, 'vue_' + event)(data)


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


__all__ = ['VuetifyTemplate']
