from traitlets import (
    Unicode, Dict
)
from ipywidgets import Widget, DOMWidget
from ipywidgets.widgets.widget import widget_serialization

from .generated.VuetifyWidget import VuetifyWidget


class Html(VuetifyWidget):

    _model_name = Unicode('HtmlModel').tag(sync=True)

    tag = Unicode().tag(sync=True)

__all__ = ['Html']