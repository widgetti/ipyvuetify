# This subclass is needed to use VuetifyView instead of VueView so CSS workarounds for Vuetify are
# added in the frontend.

from traitlets import Unicode
from ipyvue import VueTemplate
from ._version import semver


class VuetifyTemplate(VueTemplate):

    _model_name = Unicode('VuetifyTemplateModel').tag(sync=True)

    _view_name = Unicode('VuetifyView').tag(sync=True)

    _view_module = Unicode('jupyter-vuetify').tag(sync=True)

    _model_module = Unicode('jupyter-vuetify').tag(sync=True)

    _view_module_version = Unicode(semver).tag(sync=True)

    _model_module_version = Unicode(semver).tag(sync=True)


__all__ = ['VuetifyTemplate']
