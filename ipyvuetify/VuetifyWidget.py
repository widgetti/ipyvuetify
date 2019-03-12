from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization



class VuetifyWidget(DOMWidget):

    _view_name = Unicode('VuetifyView').tag(sync=True)

    _model_name = Unicode('VuetifyWidgetModel').tag(sync=True)

    _view_module = Unicode('jupyter-vuetify').tag(sync=True)

    _model_module = Unicode('jupyter-vuetify').tag(sync=True)

    _view_module_version = Unicode('0.1.0').tag(sync=True)

    _model_module_version = Unicode('0.1.0').tag(sync=True)

    children = List(Instance(DOMWidget)).tag(sync=True, **widget_serialization)



__all__ = ['VuetifyWidget']
