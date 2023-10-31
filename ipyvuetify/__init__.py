from ._version import __version__
from .Html import Html
from .Themes import theme
from .vuetify_widgets import *  # noqa: F403
from .VuetifyTemplate import VuetifyTemplate


def _jupyter_labextension_paths():
    return [
        {
            "src": "labextension",
            "dest": "jupyter-vuetify",
        }
    ]


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "nbextension",
            "dest": "jupyter-vuetify",
            "require": "jupyter-vuetify/extension",
        }
    ]
