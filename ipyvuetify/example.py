import ipywidgets as widgets
from traitlets import Unicode, Instance, CBool, CInt, CUnicode, HasTraits, Any, Dict
from ipywidgets.widgets.widget import widget_serialization
from ipywidgets.widgets.trait_types import TypedTuple
from enum import Enum



@widgets.register
class VuetifyWidget2(widgets.DOMWidget):
    _view_name = Unicode('VuetifyView').tag(sync=True)
    _model_name = Unicode('VuetifyModel').tag(sync=True)
    _view_module = Unicode('jupyter-vuetify').tag(sync=True)
    _model_module = Unicode('jupyter-vuetify').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    children = TypedTuple(trait=Instance('ipywidgets.widgets.domwidget.DOMWidget'), help="children", default=[], allow_none=True).tag(sync=True, **widget_serialization).tag(sync=True)
    # props =

@widgets.register
class Text2(VuetifyWidget2):
    _model_name = Unicode('TextModel').tag(sync=True)
    value = Unicode('').tag(sync=True)

    def __init__(self, value):
        super().__init__()
        self.dina = property(lambda: CBool(None, allow_none=True).tag(sync=True))
        print("Text1" + value)
        self.value = value

class Props(Enum):
    right = "right"
    xLarge = "xLarge"
    round = "round"

globals().update(Props.__members__)

@widgets.register
class Icon2(VuetifyWidget2):
    _model_name = Unicode('IconModel').tag(sync=True)
    color = CUnicode(None, allow_none=True).tag(sync=True)
    dark = CBool(None, allow_none=True).tag(sync=True)
    disabled = CBool(None, allow_none=True).tag(sync=True)
    large = CBool(None, allow_none=True).tag(sync=True)
    left = CBool(None, allow_none=True).tag(sync=True)
    light = CBool(None, allow_none=True).tag(sync=True)
    medium = CBool(None, allow_none=True).tag(sync=True)
    right = CBool(None, allow_none=True).tag(sync=True)
    small = CBool(None, allow_none=True).tag(sync=True)
    size = CInt(None, allow_none=True).tag(sync=True)
    value = Unicode('home').tag(sync=True)
    xLarge = CBool(None, allow_none=True).tag(sync=True)

    def __init__(self, value, *args, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        for arg in args:
            setattr(self, arg.name, True)
        self.value = value
        super().__init__()

    # _propTraitMap = {
    #     "color":
    # }
    #
    # def propTraits(self, name):
    #     if

@widgets.register
class Button2(VuetifyWidget2):
    _model_name = Unicode('ButtonModel').tag(sync=True)
    absolute = CBool(None, allow_none=True).tag(sync=True)
    #active-class
    block = CBool(None, allow_none=True).tag(sync=True)
    bottom = CBool(None, allow_none=True).tag(sync=True)
    color = CUnicode(None, allow_none=True).tag(sync=True)
    dark = CBool(None, allow_none=True).tag(sync=True)
    depressed = CBool(None, allow_none=True).tag(sync=True)
    exact = CBool(None, allow_none=True).tag(sync=True)
    #exact-active-class
    fab = CBool(None, allow_none=True).tag(sync=True)
    fixed = CBool(None, allow_none=True).tag(sync=True)
    flat = CBool(None, allow_none=True).tag(sync=True)
    href = CUnicode(None, allow_none=True).tag(sync=True)
    icon = CBool(None, allow_none=True).tag(sync=True)
    #input-value
    large = CBool(None, allow_none=True).tag(sync=True)
    left = CBool(None, allow_none=True).tag(sync=True)
    light = CBool(None, allow_none=True).tag(sync=True)
    loading = CBool(None, allow_none=True).tag(sync=True)
    #nuxt
    outline = CBool(None, allow_none=True).tag(sync=True)
    #replace
    right = CBool(None, allow_none=True).tag(sync=True)
    ripple = CBool(None, allow_none=True).tag(sync=True)
    round = CBool(None, allow_none=True).tag(sync=True)
    small = CBool(None, allow_none=True).tag(sync=True)
    #tag
    target = CUnicode(None, allow_none=True).tag(sync=True)
    #to
    top = CBool(None, allow_none=True).tag(sync=True)
    type = Unicode('button').tag(sync=True)
    #value

    def __init__(self, *args, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        for arg in args:
            setattr(self, arg.name, True)
        super().__init__()

@widgets.register
class Layout2(VuetifyWidget2):
    _model_name = Unicode('LayoutModel').tag(sync=True)
    alignBaseline = CBool(None, allow_none=True).tag(sync=True)
    alignCenter = CBool(None, allow_none=True).tag(sync=True)
    alignContentCenter = CBool(None, allow_none=True).tag(sync=True)
    alignContentEnd = CBool(None, allow_none=True).tag(sync=True)
    alignContentSpaceAround = CBool(None, allow_none=True).tag(sync=True)
    alignContentSpaceBetween = CBool(None, allow_none=True).tag(sync=True)
    alignContentStart = CBool(None, allow_none=True).tag(sync=True)
    # todo: meer