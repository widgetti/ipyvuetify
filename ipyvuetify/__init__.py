from ._generated import *  # noqa: F403
from ._Html import Html as Html
from ._version import __version__ as __version__
from ._VuetifyTemplate import VuetifyTemplate as VuetifyTemplate
from .Themes import theme as theme


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
