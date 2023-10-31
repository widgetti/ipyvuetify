from ipyvue import VueWidget
from traitlets import Dict, Unicode

from ._version import semver


class VuetifyWidget(VueWidget):

    _model_name = Unicode("VuetifyWidgetModel").tag(sync=True)

    _view_name = Unicode("VuetifyView").tag(sync=True)

    _view_module = Unicode("jupyter-vuetify").tag(sync=True)

    _model_module = Unicode("jupyter-vuetify").tag(sync=True)

    _view_module_version = Unicode(semver).tag(sync=True)

    _model_module_version = Unicode(semver).tag(sync=True)

    _metadata = Dict(default_value=None, allow_none=True).tag(sync=True)


__all__ = ["VuetifyWidget"]
