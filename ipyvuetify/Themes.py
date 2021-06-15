from ipywidgets import Widget
from traitlets import Unicode, Bool
from ._version import semver


class Themes:
    def __init__(self):
        self.light = ThemeColors(
            _theme_name='light',
            primary='#1976D2',
            secondary='#424242',
            accent='#82B1FF',
            error='#FF5252',
            info='#2196F3',
            success='#4CAF50',
            warning='#FB8C00')

        self.dark = ThemeColors(
            _theme_name='dark',
            primary='#2196F3',
            secondary='#424242',
            accent='#FF4081',
            error='#FF5252',
            info='#2196F3',
            success='#4CAF50',
            warning='#FB8C00')


class Theme(Widget):
    _model_name = Unicode('ThemeModel').tag(sync=True)

    _model_module = Unicode('jupyter-vuetify').tag(sync=True)

    _view_module_version = Unicode(semver).tag(sync=True)

    _model_module_version = Unicode(semver).tag(sync=True)

    dark = Bool(None, allow_none=True).tag(sync=True)

    def __init__(self):
        super().__init__()

        self.themes = Themes()


class ThemeColors(Widget):

    _model_name = Unicode('ThemeColorsModel').tag(sync=True)

    _model_module = Unicode('jupyter-vuetify').tag(sync=True)

    _view_module_version = Unicode(semver).tag(sync=True)

    _model_module_version = Unicode(semver).tag(sync=True)

    _theme_name = Unicode().tag(sync=True)

    primary = Unicode().tag(sync=True)
    secondary = Unicode().tag(sync=True)
    accent = Unicode().tag(sync=True)
    error = Unicode().tag(sync=True)
    info = Unicode().tag(sync=True)
    success = Unicode().tag(sync=True)
    warning = Unicode().tag(sync=True)
    anchor = Unicode(None, allow_none=True).tag(sync=True)


theme = Theme()

__all__ = ['theme']
