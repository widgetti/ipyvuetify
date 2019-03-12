from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization

from .VuetifyWidget import VuetifyWidget


class Icon(VuetifyWidget):

    _model_name = Unicode('IconModel').tag(sync=True)

    color = Unicode(None, allow_none=True).tag(sync=True)

    dark = Bool(None, allow_none=True).tag(sync=True)

    disabled = Bool(None, allow_none=True).tag(sync=True)

    large = Bool(None, allow_none=True).tag(sync=True)

    left = Bool(None, allow_none=True).tag(sync=True)

    light = Bool(None, allow_none=True).tag(sync=True)

    medium = Bool(None, allow_none=True).tag(sync=True)

    right = Bool(None, allow_none=True).tag(sync=True)

    small = Bool(None, allow_none=True).tag(sync=True)

    size = Int(None, allow_none=True).tag(sync=True)

    value = Unicode().tag(sync=True)

    xLarge = Bool(None, allow_none=True).tag(sync=True)



__all__ = ['Icon']
