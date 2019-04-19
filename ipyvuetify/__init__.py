from ._version import version_info, __version__
from .Html import Html
from .VuetifyTemplate import VuetifyTemplate
from .generated import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyter-vuetify',
        'require': 'jupyter-vuetify/extension'
    }]
