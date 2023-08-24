from ._version import __version__ as __version__
from .generated import *  # noqa: F403
from .Html import Html as Html
from .Themes import theme as theme
from .VuetifyTemplate import VuetifyTemplate as VuetifyTemplate


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
