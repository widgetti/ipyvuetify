from ._version import version_info, __version__  # noqa: F401
from .Html import Html  # noqa: F401
from .VuetifyTemplate import VuetifyTemplate  # noqa: F401
from .generated import *  # noqa: F401, F403


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyter-vuetify',
        'require': 'jupyter-vuetify/extension'
    }]
