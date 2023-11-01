from ._version import __version__
from .generated import *  # noqa: F403
from .Html import Html
from .Themes import theme
from .VuetifyTemplate import VuetifyTemplate


def _prefix():
    import sys
    from pathlib import Path

    prefix = sys.prefix
    here = Path(__file__).parent
    # for when in dev mode
    if (here.parent / "prefix").exists():
        prefix = str(here.parent)
    return prefix


def _jupyter_labextension_paths():
    return [
        {
            "src": f"{_prefix()}/prefix/share/jupyter/labextensions/jupyter-vuetify/",
            "dest": "jupyter-vuetify",
        }
    ]


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": f"{_prefix()}/prefix/share/jupyter/nbextensions/jupyter-vuetify/",
            "dest": "jupyter-vuetify",
            "require": "jupyter-vuetify/extension",
        }
    ]
