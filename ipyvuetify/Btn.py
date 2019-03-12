from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization

from .VuetifyWidget import VuetifyWidget


class Btn(VuetifyWidget):

    _model_name = Unicode('BtnModel').tag(sync=True)

    absolute = Bool(None, allow_none=True).tag(sync=True)

    block = Bool(None, allow_none=True).tag(sync=True)

    bottom = Bool(None, allow_none=True).tag(sync=True)

    color = Unicode(None, allow_none=True).tag(sync=True)

    dark = Bool(None, allow_none=True).tag(sync=True)

    depressed = Bool(None, allow_none=True).tag(sync=True)

    exact = Bool(None, allow_none=True).tag(sync=True)

    fab = Bool(None, allow_none=True).tag(sync=True)

    fixed = Bool(None, allow_none=True).tag(sync=True)

    flat = Bool(None, allow_none=True).tag(sync=True)

    href = Bool(None, allow_none=True).tag(sync=True)

    icon = Bool(None, allow_none=True).tag(sync=True)

    large = Bool(None, allow_none=True).tag(sync=True)

    left = Bool(None, allow_none=True).tag(sync=True)

    light = Bool(None, allow_none=True).tag(sync=True)

    loading = Bool(None, allow_none=True).tag(sync=True)

    outline = Bool(None, allow_none=True).tag(sync=True)

    right = Bool(None, allow_none=True).tag(sync=True)

    ripple = Bool(None, allow_none=True).tag(sync=True)

    round = Bool(None, allow_none=True).tag(sync=True)

    small = Bool(None, allow_none=True).tag(sync=True)

    target = Bool(None, allow_none=True).tag(sync=True)

    top = Bool(None, allow_none=True).tag(sync=True)

    type = Unicode('button').tag(sync=True)



__all__ = ['Btn']
