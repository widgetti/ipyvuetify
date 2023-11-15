from ipywidgets import Widget
from traitlets import Bool, Unicode

from ._version import semver


class Themes:
    def __init__(self):
        self.light = ThemeColors(
            _theme_name="light",
            background="#FFFFFF",
            surface="#FFFFFF",
            surface_bright="#FFFFFF",
            surface_variant="#424242",
            on_surface_variant="#EEEEEE",
            primary="#6200EE",
            primary_darken_1="#3700B3",
            secondary="#03DAC6",
            secondary_darken_1="#018786",
            error="#B00020",
            info="#2196F3",
            success="#4CAF50",
            warning="#FB8C00",
        )

        self.dark = ThemeColors(
            _theme_name="dark",
            background="#121212",
            surface="#212121",
            surface_bright="#ccbfd6",
            surface_variant="#a3a3a3",
            on_surface_variant="#424242",
            primary="#BB86FC",
            primary_darken_1="#3700B3",
            secondary="#03DAC5",
            secondary_darken_1="#03DAC5",
            error="#CF6679",
            info="#2196F3",
            success="#4CAF50",
            warning="#FB8C00",
        )


class Theme(Widget):
    _model_name = Unicode("ThemeModel").tag(sync=True)

    _model_module = Unicode("jupyter-vuetify").tag(sync=True)

    _view_module_version = Unicode(semver).tag(sync=True)

    _model_module_version = Unicode(semver).tag(sync=True)

    dark = Bool(None, allow_none=True).tag(sync=True)

    dark_jlab = Bool(None, allow_none=True).tag(sync=True)

    def __init__(self):
        super().__init__()

        self.themes = Themes()


class ColorNotAvailable(Unicode):
    def get(self, *ignored):
        raise AttributeError(f"The theme color '{self.name}' is no longer available in Vuetify 3")

    def set(self, *ignored):
        raise AttributeError(f"The theme color '{self.name}' is no longer available in Vuetify 3")


class ThemeColors(Widget):

    _model_name = Unicode("ThemeColorsModel").tag(sync=True)

    _model_module = Unicode("jupyter-vuetify").tag(sync=True)

    _view_module_version = Unicode(semver).tag(sync=True)

    _model_module_version = Unicode(semver).tag(sync=True)

    _theme_name = Unicode().tag(sync=True)

    accent = ColorNotAvailable()
    anchor = ColorNotAvailable()
    background = Unicode().tag(sync=True)
    surface = Unicode().tag(sync=True)
    surface_bright = Unicode().tag(sync=True)
    surface_variant = Unicode().tag(sync=True)
    on_surface_variant = Unicode().tag(sync=True)
    primary = Unicode().tag(sync=True)
    primary_darken_1 = Unicode().tag(sync=True)
    secondary = Unicode().tag(sync=True)
    secondary_darken_1 = Unicode().tag(sync=True)
    error = Unicode().tag(sync=True)
    info = Unicode().tag(sync=True)
    success = Unicode().tag(sync=True)
    warning = Unicode().tag(sync=True)


theme = Theme()

__all__ = ["theme"]
