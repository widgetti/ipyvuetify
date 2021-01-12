from ._version import version_info, __version__  # noqa: F401
from .Html import Html  # noqa: F401
from .VuetifyTemplate import VuetifyTemplate  # noqa: F401
from .generated import *  # noqa: F401, F403
from .Themes import theme  # noqa: F401


def _jupyter_labextension_paths():
    return [{
        'src': 'labextension',
        'dest': 'jupyter-vuetify',
    }]


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'nbextension',
        'dest': 'jupyter-vuetify',
        'require': 'jupyter-vuetify/extension'
    }]
