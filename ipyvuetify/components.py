import typing
from typing import Any, Dict, Union

import ipyvue
import ipywidgets
import reacton

try:
    # new place where this hook is defined
    from ipyvue.hooks import use_event  # noqa: F401
except ModuleNotFoundError:
    # old place where this hook is defined
    from reacton.ipyvue import use_event  # noqa: F401
from reacton import ipywidgets as w
from reacton.core import Element, ValueElement
from reacton.utils import implements

import ipyvuetify

if __name__ == "__main__":
    from reacton import generate

    class CodeGen(generate.CodeGen):
        def has_callback(self, cls, name):
            # in ipyvuetify we only sync v_model back
            return name == "v_model"

    CodeGen([ipyvuetify]).generate(__file__)


# generated code:


def _Alert(
    attributes: dict = {},
    border: str = None,
    children: list = [],
    class_: str = None,
    close_label: str = None,
    color: str = None,
    colored_border: bool = None,
    dark: bool = None,
    dense: bool = None,
    dismissible: bool = None,
    elevation: typing.Union[float, str] = None,
    height: typing.Union[float, str] = None,
    icon: typing.Union[bool, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    mode: str = None,
    origin: str = None,
    outlined: bool = None,
    prominent: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    text: bool = None,
    tile: bool = None,
    tooltip: str = None,
    transition: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: bool = None,
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Alert, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Alert)
def Alert(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Alert
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Alert


def _App(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.App, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_App)
def App(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.App
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _App


def _AppBar(
    absolute: bool = None,
    app: bool = None,
    attributes: dict = {},
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    clipped_left: bool = None,
    clipped_right: bool = None,
    collapse: bool = None,
    collapse_on_scroll: bool = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    elevate_on_scroll: bool = None,
    elevation: typing.Union[float, str] = None,
    extended: bool = None,
    extension_height: typing.Union[float, str] = None,
    fade_img_on_scroll: bool = None,
    fixed: bool = None,
    flat: bool = None,
    floating: bool = None,
    height: typing.Union[float, str] = None,
    hide_on_scroll: bool = None,
    inverted_scroll: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    prominent: bool = None,
    scroll_off_screen: bool = None,
    scroll_target: str = None,
    scroll_threshold: typing.Union[str, float] = None,
    short: bool = None,
    shrink_on_scroll: bool = None,
    slot: str = None,
    src: typing.Union[str, dict] = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: bool = None,
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AppBar, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_AppBar)
def AppBar(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.AppBar
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _AppBar


def _AppBarNavIcon(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AppBarNavIcon, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_AppBarNavIcon)
def AppBarNavIcon(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.AppBarNavIcon
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _AppBarNavIcon


def _Autocomplete(
    allow_overflow: bool = None,
    append_icon: str = None,
    append_outer_icon: str = None,
    attach: Any = None,
    attributes: dict = {},
    auto_select_first: bool = None,
    autofocus: bool = None,
    background_color: str = None,
    cache_items: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: str = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[bool, float, str] = None,
    dark: bool = None,
    deletable_chips: bool = None,
    dense: bool = None,
    disable_lookup: bool = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    filled: bool = None,
    flat: bool = None,
    full_width: bool = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hint: str = None,
    id: str = None,
    item_color: str = None,
    item_disabled: typing.Union[str, list] = None,
    item_text: typing.Union[str, list] = None,
    item_value: typing.Union[str, list] = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    menu_props: typing.Union[str, list, dict] = None,
    messages: typing.Union[str, list] = None,
    multiple: bool = None,
    no_data_text: str = None,
    no_filter: bool = None,
    open_on_clear: bool = None,
    outlined: bool = None,
    persistent_hint: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: str = None,
    prepend_inner_icon: str = None,
    readonly: bool = None,
    return_object: bool = None,
    reverse: bool = None,
    rounded: bool = None,
    rules: list = [],
    search_input: str = None,
    shaped: bool = None,
    single_line: bool = None,
    slot: str = None,
    small_chips: bool = None,
    solo: bool = None,
    solo_inverted: bool = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    suffix: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Autocomplete, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Autocomplete)
def Autocomplete(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Autocomplete
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Autocomplete


def _Avatar(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    right: bool = None,
    size: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Avatar, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Avatar)
def Avatar(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Avatar
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Avatar


def _Badge(
    attributes: dict = {},
    avatar: bool = None,
    bordered: bool = None,
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    content: Any = None,
    dark: bool = None,
    dot: bool = None,
    icon: str = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    light: bool = None,
    mode: str = None,
    offset_x: typing.Union[float, str] = None,
    offset_y: typing.Union[float, str] = None,
    origin: str = None,
    overlap: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tile: bool = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Badge, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Badge)
def Badge(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Badge
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Badge


def _Banner(
    app: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    elevation: typing.Union[float, str] = None,
    height: typing.Union[float, str] = None,
    icon: str = None,
    icon_color: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    mobile_break_point: typing.Union[float, str] = None,
    single_line: bool = None,
    slot: str = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: bool = None,
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Banner, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Banner)
def Banner(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Banner
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Banner


def _BottomNavigation(
    absolute: bool = None,
    active_class: str = None,
    app: bool = None,
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    fixed: bool = None,
    grow: bool = None,
    height: typing.Union[float, str] = None,
    hide_on_scroll: bool = None,
    horizontal: bool = None,
    input_value: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    scroll_target: str = None,
    scroll_threshold: typing.Union[str, float] = None,
    shift: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BottomNavigation, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_BottomNavigation)
def BottomNavigation(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.BottomNavigation
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _BottomNavigation


def _BottomSheet(
    activator: Any = None,
    attach: Any = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[float, str] = None,
    content_class: str = None,
    dark: bool = None,
    disabled: bool = None,
    eager: bool = None,
    fullscreen: bool = None,
    hide_overlay: bool = None,
    inset: bool = None,
    internal_activator: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_width: typing.Union[str, float] = None,
    no_click_animation: bool = None,
    open_delay: typing.Union[float, str] = None,
    open_on_hover: bool = None,
    origin: str = None,
    overlay_color: str = None,
    overlay_opacity: typing.Union[float, str] = None,
    persistent: bool = None,
    retain_focus: bool = None,
    return_value: Any = None,
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BottomSheet, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_BottomSheet)
def BottomSheet(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.BottomSheet
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _BottomSheet


def _Breadcrumbs(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    divider: str = None,
    items: list = [],
    large: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Breadcrumbs, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Breadcrumbs)
def Breadcrumbs(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Breadcrumbs
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Breadcrumbs


def _BreadcrumbsDivider(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BreadcrumbsDivider, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_BreadcrumbsDivider)
def BreadcrumbsDivider(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.BreadcrumbsDivider
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _BreadcrumbsDivider


def _BreadcrumbsItem(
    active_class: str = None,
    append: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    exact: bool = None,
    exact_active_class: str = None,
    href: typing.Union[str, dict] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    link: bool = None,
    nuxt: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    target: str = None,
    to: typing.Union[str, dict] = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BreadcrumbsItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_BreadcrumbsItem)
def BreadcrumbsItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.BreadcrumbsItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _BreadcrumbsItem


def _Btn(
    absolute: bool = None,
    active_class: str = None,
    append: bool = None,
    attributes: dict = {},
    block: bool = None,
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    depressed: bool = None,
    disabled: bool = None,
    elevation: typing.Union[float, str] = None,
    exact: bool = None,
    exact_active_class: str = None,
    fab: bool = None,
    fixed: bool = None,
    height: typing.Union[float, str] = None,
    href: typing.Union[str, dict] = None,
    icon: bool = None,
    input_value: Any = None,
    large: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    light: bool = None,
    link: bool = None,
    loading: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    nuxt: bool = None,
    outlined: bool = None,
    replace: bool = None,
    retain_focus_on_click: bool = None,
    right: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: bool = None,
    slot: str = None,
    small: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    target: str = None,
    text: bool = None,
    tile: bool = None,
    to: typing.Union[str, dict] = None,
    tooltip: str = None,
    top: bool = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[float, str] = None,
    x_large: bool = None,
    x_small: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Btn, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Btn)
def Btn(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Btn
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Btn


def _BtnToggle(
    active_class: str = None,
    attributes: dict = {},
    background_color: str = None,
    borderless: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    group: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    multiple: bool = None,
    rounded: bool = None,
    shaped: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BtnToggle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_BtnToggle)
def BtnToggle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.BtnToggle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _BtnToggle


def _Calendar(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    end: str = None,
    event_color: str = None,
    event_end: str = None,
    event_height: float = None,
    event_margin_bottom: float = None,
    event_more: bool = None,
    event_more_text: str = None,
    event_name: str = None,
    event_overlap_mode: str = None,
    event_overlap_threshold: typing.Union[str, float] = None,
    event_ripple: typing.Union[bool, dict] = None,
    event_start: str = None,
    event_text_color: str = None,
    events: list = [],
    first_interval: typing.Union[float, str] = None,
    hide_header: bool = None,
    interval_count: typing.Union[float, str] = None,
    interval_height: typing.Union[float, str] = None,
    interval_minutes: typing.Union[float, str] = None,
    interval_width: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    locale: str = None,
    max_days: float = None,
    min_weeks: Any = None,
    now: str = None,
    short_intervals: bool = None,
    short_months: bool = None,
    short_weekdays: bool = None,
    show_month_on_first: bool = None,
    slot: str = None,
    start: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: str = None,
    weekdays: typing.Union[list, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Calendar, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Calendar)
def Calendar(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Calendar
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Calendar


def _CalendarDaily(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    end: str = None,
    first_interval: typing.Union[float, str] = None,
    hide_header: bool = None,
    interval_count: typing.Union[float, str] = None,
    interval_height: typing.Union[float, str] = None,
    interval_minutes: typing.Union[float, str] = None,
    interval_width: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    locale: str = None,
    max_days: float = None,
    now: str = None,
    short_intervals: bool = None,
    short_weekdays: bool = None,
    slot: str = None,
    start: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    weekdays: typing.Union[list, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CalendarDaily, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CalendarDaily)
def CalendarDaily(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CalendarDaily
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CalendarDaily


def _CalendarMonthly(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    end: str = None,
    hide_header: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    locale: str = None,
    min_weeks: Any = None,
    now: str = None,
    short_months: bool = None,
    short_weekdays: bool = None,
    show_month_on_first: bool = None,
    slot: str = None,
    start: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    weekdays: typing.Union[list, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CalendarMonthly, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CalendarMonthly)
def CalendarMonthly(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CalendarMonthly
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CalendarMonthly


def _CalendarWeekly(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    end: str = None,
    hide_header: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    locale: str = None,
    min_weeks: Any = None,
    now: str = None,
    short_months: bool = None,
    short_weekdays: bool = None,
    show_month_on_first: bool = None,
    slot: str = None,
    start: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    weekdays: typing.Union[list, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CalendarWeekly, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CalendarWeekly)
def CalendarWeekly(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CalendarWeekly
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CalendarWeekly


def _Card(
    active_class: str = None,
    append: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    elevation: typing.Union[float, str] = None,
    exact: bool = None,
    exact_active_class: str = None,
    flat: bool = None,
    height: typing.Union[float, str] = None,
    hover: bool = None,
    href: typing.Union[str, dict] = None,
    img: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    link: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    nuxt: bool = None,
    outlined: bool = None,
    raised: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    shaped: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    target: str = None,
    tile: bool = None,
    to: typing.Union[str, dict] = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Card, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Card)
def Card(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Card
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Card


def _CardActions(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardActions, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CardActions)
def CardActions(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CardActions
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CardActions


def _CardSubtitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardSubtitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CardSubtitle)
def CardSubtitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CardSubtitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CardSubtitle


def _CardText(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardText, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CardText)
def CardText(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CardText
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CardText


def _CardTitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CardTitle)
def CardTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CardTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CardTitle


def _Carousel(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    continuous: bool = None,
    cycle: bool = None,
    dark: bool = None,
    delimiter_icon: str = None,
    height: typing.Union[float, str] = None,
    hide_delimiter_background: bool = None,
    hide_delimiters: bool = None,
    interval: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    multiple: bool = None,
    next_icon: typing.Union[bool, str] = None,
    prev_icon: typing.Union[bool, str] = None,
    progress: bool = None,
    progress_color: str = None,
    reverse: bool = None,
    show_arrows: bool = None,
    show_arrows_on_hover: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    touch: dict = None,
    touchless: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    vertical: bool = None,
    vertical_delimiters: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Carousel, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Carousel)
def Carousel(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Carousel
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Carousel


def _CarouselItem(
    active_class: str = None,
    append: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    eager: bool = None,
    exact: bool = None,
    exact_active_class: str = None,
    href: typing.Union[str, dict] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    link: bool = None,
    nuxt: bool = None,
    replace: bool = None,
    reverse_transition: typing.Union[bool, str] = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    target: str = None,
    to: typing.Union[str, dict] = None,
    tooltip: str = None,
    transition: typing.Union[bool, str] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CarouselItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CarouselItem)
def CarouselItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CarouselItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CarouselItem


def _CarouselReverseTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CarouselReverseTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CarouselReverseTransition)
def CarouselReverseTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CarouselReverseTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CarouselReverseTransition


def _CarouselTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CarouselTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CarouselTransition)
def CarouselTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CarouselTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CarouselTransition


def _Checkbox(
    append_icon: str = None,
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    false_value: Any = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    indeterminate: bool = None,
    indeterminate_icon: str = None,
    input_value: Any = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loading: bool = None,
    messages: typing.Union[str, list] = None,
    multiple: bool = None,
    off_icon: str = None,
    on_icon: str = None,
    persistent_hint: bool = None,
    prepend_icon: str = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    tabbable: bool = None,
    tooltip: str = None,
    true_value: Any = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Checkbox, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Checkbox)
def Checkbox(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Checkbox
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Checkbox


def _Chip(
    active: bool = None,
    active_class: str = None,
    append: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_: bool = None,
    close_icon: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    draggable: bool = None,
    exact: bool = None,
    exact_active_class: str = None,
    filter: bool = None,
    filter_icon: str = None,
    href: typing.Union[str, dict] = None,
    input_value: Any = None,
    label: bool = None,
    large: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    link: bool = None,
    nuxt: bool = None,
    outlined: bool = None,
    pill: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    small: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    target: str = None,
    text_color: str = None,
    to: typing.Union[str, dict] = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    x_large: bool = None,
    x_small: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Chip, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Chip)
def Chip(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Chip
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Chip


def _ChipGroup(
    active_class: str = None,
    attributes: dict = {},
    center_active: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    column: bool = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    mobile_break_point: typing.Union[float, str] = None,
    multiple: bool = None,
    next_icon: str = None,
    prev_icon: str = None,
    show_arrows: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ChipGroup, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ChipGroup)
def ChipGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ChipGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ChipGroup


def _Col(
    align_self: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    cols: typing.Union[bool, str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lg: typing.Union[bool, str, float] = None,
    md: typing.Union[bool, str, float] = None,
    offset: typing.Union[str, float] = None,
    offset_lg: typing.Union[str, float] = None,
    offset_md: typing.Union[str, float] = None,
    offset_sm: typing.Union[str, float] = None,
    offset_xl: typing.Union[str, float] = None,
    order: typing.Union[str, float] = None,
    order_lg: typing.Union[str, float] = None,
    order_md: typing.Union[str, float] = None,
    order_sm: typing.Union[str, float] = None,
    order_xl: typing.Union[str, float] = None,
    slot: str = None,
    sm: typing.Union[bool, str, float] = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    xl: typing.Union[bool, str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Col, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Col)
def Col(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Col
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Col


def _ColorPicker(
    attributes: dict = {},
    canvas_height: typing.Union[str, float] = None,
    children: list = [],
    class_: str = None,
    dark: bool = None,
    disabled: bool = None,
    dot_size: typing.Union[float, str] = None,
    flat: bool = None,
    hide_canvas: bool = None,
    hide_inputs: bool = None,
    hide_mode_switch: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mode: str = None,
    show_swatches: bool = None,
    slot: str = None,
    style_: str = None,
    swatches: list = [],
    swatches_max_height: typing.Union[float, str] = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[dict, str] = None,
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ColorPicker, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ColorPicker)
def ColorPicker(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ColorPicker
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ColorPicker


def _ColorPickerCanvas(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: dict = None,
    disabled: bool = None,
    dot_size: typing.Union[float, str] = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ColorPickerCanvas, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ColorPickerCanvas)
def ColorPickerCanvas(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ColorPickerCanvas
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ColorPickerCanvas


def _ColorPickerSwatches(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: dict = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    swatches: list = [],
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ColorPickerSwatches, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ColorPickerSwatches)
def ColorPickerSwatches(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ColorPickerSwatches
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ColorPickerSwatches


def _Combobox(
    allow_overflow: bool = None,
    append_icon: str = None,
    append_outer_icon: str = None,
    attach: Any = None,
    attributes: dict = {},
    auto_select_first: bool = None,
    autofocus: bool = None,
    background_color: str = None,
    cache_items: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: str = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[bool, float, str] = None,
    dark: bool = None,
    deletable_chips: bool = None,
    delimiters: list = [],
    dense: bool = None,
    disable_lookup: bool = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    filled: bool = None,
    flat: bool = None,
    full_width: bool = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hint: str = None,
    id: str = None,
    item_color: str = None,
    item_disabled: typing.Union[str, list] = None,
    item_text: typing.Union[str, list] = None,
    item_value: typing.Union[str, list] = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    menu_props: typing.Union[str, list, dict] = None,
    messages: typing.Union[str, list] = None,
    multiple: bool = None,
    no_data_text: str = None,
    no_filter: bool = None,
    open_on_clear: bool = None,
    outlined: bool = None,
    persistent_hint: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: str = None,
    prepend_inner_icon: str = None,
    readonly: bool = None,
    return_object: bool = None,
    reverse: bool = None,
    rounded: bool = None,
    rules: list = [],
    search_input: str = None,
    shaped: bool = None,
    single_line: bool = None,
    slot: str = None,
    small_chips: bool = None,
    solo: bool = None,
    solo_inverted: bool = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    suffix: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Combobox, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Combobox)
def Combobox(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Combobox
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Combobox


def _Container(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    fluid: bool = None,
    id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    ma_0: bool = None,
    ma_1: bool = None,
    ma_2: bool = None,
    ma_3: bool = None,
    ma_4: bool = None,
    ma_5: bool = None,
    ma_auto: bool = None,
    mb_0: bool = None,
    mb_1: bool = None,
    mb_2: bool = None,
    mb_3: bool = None,
    mb_4: bool = None,
    mb_5: bool = None,
    mb_auto: bool = None,
    ml_0: bool = None,
    ml_1: bool = None,
    ml_2: bool = None,
    ml_3: bool = None,
    ml_4: bool = None,
    ml_5: bool = None,
    ml_auto: bool = None,
    mr_0: bool = None,
    mr_1: bool = None,
    mr_2: bool = None,
    mr_3: bool = None,
    mr_4: bool = None,
    mr_5: bool = None,
    mr_auto: bool = None,
    mt_0: bool = None,
    mt_1: bool = None,
    mt_2: bool = None,
    mt_3: bool = None,
    mt_4: bool = None,
    mt_5: bool = None,
    mt_auto: bool = None,
    mx_0: bool = None,
    mx_1: bool = None,
    mx_2: bool = None,
    mx_3: bool = None,
    mx_4: bool = None,
    mx_5: bool = None,
    mx_auto: bool = None,
    my_0: bool = None,
    my_1: bool = None,
    my_2: bool = None,
    my_3: bool = None,
    my_4: bool = None,
    my_5: bool = None,
    my_auto: bool = None,
    pa_0: bool = None,
    pa_1: bool = None,
    pa_2: bool = None,
    pa_3: bool = None,
    pa_4: bool = None,
    pa_5: bool = None,
    pa_auto: bool = None,
    pb_0: bool = None,
    pb_1: bool = None,
    pb_2: bool = None,
    pb_3: bool = None,
    pb_4: bool = None,
    pb_5: bool = None,
    pb_auto: bool = None,
    pl_0: bool = None,
    pl_1: bool = None,
    pl_2: bool = None,
    pl_3: bool = None,
    pl_4: bool = None,
    pl_5: bool = None,
    pl_auto: bool = None,
    pr_0: bool = None,
    pr_1: bool = None,
    pr_2: bool = None,
    pr_3: bool = None,
    pr_4: bool = None,
    pr_5: bool = None,
    pr_auto: bool = None,
    pt_0: bool = None,
    pt_1: bool = None,
    pt_2: bool = None,
    pt_3: bool = None,
    pt_4: bool = None,
    pt_5: bool = None,
    pt_auto: bool = None,
    px_0: bool = None,
    px_1: bool = None,
    px_2: bool = None,
    px_3: bool = None,
    px_4: bool = None,
    px_5: bool = None,
    px_auto: bool = None,
    py_0: bool = None,
    py_1: bool = None,
    py_2: bool = None,
    py_3: bool = None,
    py_4: bool = None,
    py_5: bool = None,
    py_auto: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Container, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Container)
def Container(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Container
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Container


def _Content(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    ma_0: bool = None,
    ma_1: bool = None,
    ma_2: bool = None,
    ma_3: bool = None,
    ma_4: bool = None,
    ma_5: bool = None,
    ma_auto: bool = None,
    mb_0: bool = None,
    mb_1: bool = None,
    mb_2: bool = None,
    mb_3: bool = None,
    mb_4: bool = None,
    mb_5: bool = None,
    mb_auto: bool = None,
    ml_0: bool = None,
    ml_1: bool = None,
    ml_2: bool = None,
    ml_3: bool = None,
    ml_4: bool = None,
    ml_5: bool = None,
    ml_auto: bool = None,
    mr_0: bool = None,
    mr_1: bool = None,
    mr_2: bool = None,
    mr_3: bool = None,
    mr_4: bool = None,
    mr_5: bool = None,
    mr_auto: bool = None,
    mt_0: bool = None,
    mt_1: bool = None,
    mt_2: bool = None,
    mt_3: bool = None,
    mt_4: bool = None,
    mt_5: bool = None,
    mt_auto: bool = None,
    mx_0: bool = None,
    mx_1: bool = None,
    mx_2: bool = None,
    mx_3: bool = None,
    mx_4: bool = None,
    mx_5: bool = None,
    mx_auto: bool = None,
    my_0: bool = None,
    my_1: bool = None,
    my_2: bool = None,
    my_3: bool = None,
    my_4: bool = None,
    my_5: bool = None,
    my_auto: bool = None,
    pa_0: bool = None,
    pa_1: bool = None,
    pa_2: bool = None,
    pa_3: bool = None,
    pa_4: bool = None,
    pa_5: bool = None,
    pa_auto: bool = None,
    pb_0: bool = None,
    pb_1: bool = None,
    pb_2: bool = None,
    pb_3: bool = None,
    pb_4: bool = None,
    pb_5: bool = None,
    pb_auto: bool = None,
    pl_0: bool = None,
    pl_1: bool = None,
    pl_2: bool = None,
    pl_3: bool = None,
    pl_4: bool = None,
    pl_5: bool = None,
    pl_auto: bool = None,
    pr_0: bool = None,
    pr_1: bool = None,
    pr_2: bool = None,
    pr_3: bool = None,
    pr_4: bool = None,
    pr_5: bool = None,
    pr_auto: bool = None,
    pt_0: bool = None,
    pt_1: bool = None,
    pt_2: bool = None,
    pt_3: bool = None,
    pt_4: bool = None,
    pt_5: bool = None,
    pt_auto: bool = None,
    px_0: bool = None,
    px_1: bool = None,
    px_2: bool = None,
    px_3: bool = None,
    px_4: bool = None,
    px_5: bool = None,
    px_auto: bool = None,
    py_0: bool = None,
    py_1: bool = None,
    py_2: bool = None,
    py_3: bool = None,
    py_4: bool = None,
    py_5: bool = None,
    py_auto: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Content, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Content)
def Content(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Content
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Content


def _Counter(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Counter, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Counter)
def Counter(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Counter
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Counter


def _Data(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disable_filtering: bool = None,
    disable_pagination: bool = None,
    disable_sort: bool = None,
    group_by: typing.Union[str, list] = None,
    group_desc: typing.Union[bool, list] = None,
    items: list = [],
    items_per_page: float = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    locale: str = None,
    multi_sort: bool = None,
    must_sort: bool = None,
    options: dict = None,
    page: float = None,
    search: str = None,
    server_items_length: float = None,
    slot: str = None,
    sort_by: typing.Union[str, list] = None,
    sort_desc: typing.Union[bool, list] = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Data, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Data)
def Data(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Data
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Data


def _DataFooter(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disable_items_per_page: bool = None,
    disable_pagination: bool = None,
    first_icon: str = None,
    items_per_page_all_text: str = None,
    items_per_page_options: list = [],
    items_per_page_text: str = None,
    last_icon: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    next_icon: str = None,
    options: dict = None,
    page_text: str = None,
    pagination: dict = None,
    prev_icon: str = None,
    show_current_page: bool = None,
    show_first_last_page: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataFooter, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataFooter)
def DataFooter(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataFooter
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataFooter


def _DataIterator(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    disable_filtering: bool = None,
    disable_pagination: bool = None,
    disable_sort: bool = None,
    expanded: list = [],
    footer_props: dict = None,
    group_by: typing.Union[str, list] = None,
    group_desc: typing.Union[bool, list] = None,
    hide_default_footer: bool = None,
    item_key: str = None,
    items: list = [],
    items_per_page: float = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loading: typing.Union[bool, str] = None,
    loading_text: str = None,
    locale: str = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    multi_sort: bool = None,
    must_sort: bool = None,
    no_data_text: str = None,
    no_results_text: str = None,
    options: dict = None,
    page: float = None,
    search: str = None,
    selectable_key: str = None,
    server_items_length: float = None,
    single_expand: bool = None,
    single_select: bool = None,
    slot: str = None,
    sort_by: typing.Union[str, list] = None,
    sort_desc: typing.Union[bool, list] = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataIterator, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataIterator)
def DataIterator(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataIterator
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataIterator


def _DataTable(
    attributes: dict = {},
    calculate_widths: bool = None,
    caption: str = None,
    children: list = [],
    class_: str = None,
    dark: bool = None,
    dense: bool = None,
    disable_filtering: bool = None,
    disable_pagination: bool = None,
    disable_sort: bool = None,
    expand_icon: str = None,
    expanded: list = [],
    fixed_header: bool = None,
    footer_props: dict = None,
    group_by: typing.Union[str, list] = None,
    group_desc: typing.Union[bool, list] = None,
    header_props: dict = None,
    headers: list = [],
    headers_length: float = None,
    height: typing.Union[float, str] = None,
    hide_default_footer: bool = None,
    hide_default_header: bool = None,
    item_key: str = None,
    items: list = [],
    items_per_page: float = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loading: typing.Union[bool, str] = None,
    loading_text: str = None,
    locale: str = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    multi_sort: bool = None,
    must_sort: bool = None,
    no_data_text: str = None,
    no_results_text: str = None,
    options: dict = None,
    page: float = None,
    search: str = None,
    selectable_key: str = None,
    server_items_length: float = None,
    show_expand: bool = None,
    show_group_by: bool = None,
    show_select: bool = None,
    single_expand: bool = None,
    single_select: bool = None,
    slot: str = None,
    sort_by: typing.Union[str, list] = None,
    sort_desc: typing.Union[bool, list] = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTable, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataTable)
def DataTable(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataTable
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataTable


def _DataTableHeader(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mobile: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableHeader, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataTableHeader)
def DataTableHeader(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataTableHeader
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataTableHeader


def _DatePicker(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    event_color: typing.Union[list, dict, str] = None,
    events: typing.Union[list, dict] = None,
    first_day_of_week: typing.Union[str, float] = None,
    full_width: bool = None,
    header_color: str = None,
    landscape: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    locale: str = None,
    locale_first_day_of_year: typing.Union[str, float] = None,
    max: str = None,
    min: str = None,
    multiple: bool = None,
    next_icon: str = None,
    no_title: bool = None,
    picker_date: str = None,
    prev_icon: str = None,
    range: bool = None,
    reactive: bool = None,
    readonly: bool = None,
    scrollable: bool = None,
    selected_items_text: str = None,
    show_current: typing.Union[bool, str] = None,
    show_week: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[list, str] = None,
    width: typing.Union[float, str] = None,
    year_icon: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePicker, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DatePicker)
def DatePicker(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePicker
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePicker


def _DatePickerDateTable(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    current: str = None,
    dark: bool = None,
    disabled: bool = None,
    event_color: typing.Union[list, dict, str] = None,
    events: typing.Union[list, dict] = None,
    first_day_of_week: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    locale: str = None,
    locale_first_day_of_year: typing.Union[str, float] = None,
    max: str = None,
    min: str = None,
    range: bool = None,
    readonly: bool = None,
    scrollable: bool = None,
    show_week: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    table_date: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[str, list] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerDateTable, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DatePickerDateTable)
def DatePickerDateTable(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePickerDateTable
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePickerDateTable


def _DatePickerHeader(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    locale: str = None,
    max: str = None,
    min: str = None,
    next_icon: str = None,
    prev_icon: str = None,
    readonly: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerHeader, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DatePickerHeader)
def DatePickerHeader(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePickerHeader
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePickerHeader


def _DatePickerMonthTable(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    current: str = None,
    dark: bool = None,
    disabled: bool = None,
    event_color: typing.Union[list, dict, str] = None,
    events: typing.Union[list, dict] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    locale: str = None,
    max: str = None,
    min: str = None,
    range: bool = None,
    readonly: bool = None,
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    table_date: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[str, list] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerMonthTable, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DatePickerMonthTable)
def DatePickerMonthTable(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePickerMonthTable
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePickerMonthTable


def _DatePickerTitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    date: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    readonly: bool = None,
    selecting_year: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: str = None,
    year: typing.Union[float, str] = None,
    year_icon: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DatePickerTitle)
def DatePickerTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePickerTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePickerTitle


def _DatePickerYears(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    locale: str = None,
    max: typing.Union[float, str] = None,
    min: typing.Union[float, str] = None,
    readonly: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerYears, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DatePickerYears)
def DatePickerYears(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePickerYears
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePickerYears


def _Dialog(
    activator: Any = None,
    attach: Any = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[float, str] = None,
    content_class: str = None,
    dark: bool = None,
    disabled: bool = None,
    eager: bool = None,
    fullscreen: bool = None,
    hide_overlay: bool = None,
    internal_activator: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_width: typing.Union[str, float] = None,
    no_click_animation: bool = None,
    open_delay: typing.Union[float, str] = None,
    open_on_hover: bool = None,
    origin: str = None,
    overlay_color: str = None,
    overlay_opacity: typing.Union[float, str] = None,
    persistent: bool = None,
    retain_focus: bool = None,
    return_value: Any = None,
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Dialog, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Dialog)
def Dialog(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Dialog
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Dialog


def _DialogBottomTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DialogBottomTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DialogBottomTransition)
def DialogBottomTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DialogBottomTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DialogBottomTransition


def _DialogTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DialogTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DialogTransition)
def DialogTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DialogTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DialogTransition


def _Divider(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Divider, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Divider)
def Divider(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Divider
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Divider


def _EditDialog(
    attributes: dict = {},
    cancel_text: Any = None,
    children: list = [],
    class_: str = None,
    dark: bool = None,
    eager: bool = None,
    large: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    persistent: bool = None,
    return_value: Any = None,
    save_text: Any = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.EditDialog, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_EditDialog)
def EditDialog(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.EditDialog
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _EditDialog


def _ExpandTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mode: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpandTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpandTransition)
def ExpandTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpandTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpandTransition


def _ExpandXTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mode: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpandXTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpandXTransition)
def ExpandXTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpandXTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpandXTransition


def _ExpansionPanel(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    readonly: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanel, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpansionPanel)
def ExpansionPanel(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpansionPanel
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpansionPanel


def _ExpansionPanelContent(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    eager: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanelContent, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpansionPanelContent)
def ExpansionPanelContent(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpansionPanelContent
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpansionPanelContent


def _ExpansionPanelHeader(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    disable_icon_rotate: bool = None,
    expand_icon: str = None,
    hide_actions: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanelHeader, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpansionPanelHeader)
def ExpansionPanelHeader(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpansionPanelHeader
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpansionPanelHeader


def _ExpansionPanels(
    accordion: bool = None,
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    disabled: bool = None,
    flat: bool = None,
    focusable: bool = None,
    hover: bool = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    multiple: bool = None,
    popout: bool = None,
    readonly: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanels, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpansionPanels)
def ExpansionPanels(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpansionPanels
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpansionPanels


def _FabTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FabTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_FabTransition)
def FabTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.FabTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _FabTransition


def _FadeTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FadeTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_FadeTransition)
def FadeTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.FadeTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _FadeTransition


def _FileInput(
    append_icon: str = None,
    append_outer_icon: str = None,
    attributes: dict = {},
    autofocus: bool = None,
    background_color: str = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: str = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[bool, float, str] = None,
    counter_size_string: str = None,
    counter_string: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    filled: bool = None,
    flat: bool = None,
    full_width: bool = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    messages: typing.Union[str, list] = None,
    multiple: bool = None,
    outlined: bool = None,
    persistent_hint: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: str = None,
    prepend_inner_icon: str = None,
    readonly: bool = None,
    reverse: bool = None,
    rounded: bool = None,
    rules: list = [],
    shaped: bool = None,
    show_size: typing.Union[bool, float] = None,
    single_line: bool = None,
    slot: str = None,
    small_chips: bool = None,
    solo: bool = None,
    solo_inverted: bool = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    suffix: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    truncate_length: typing.Union[float, str] = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FileInput, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_FileInput)
def FileInput(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.FileInput
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _FileInput


def _Flex(
    align_self_baseline: bool = None,
    align_self_center: bool = None,
    align_self_end: bool = None,
    align_self_start: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    grow: bool = None,
    id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lg1: bool = None,
    lg10: bool = None,
    lg11: bool = None,
    lg12: bool = None,
    lg2: bool = None,
    lg3: bool = None,
    lg4: bool = None,
    lg5: bool = None,
    lg6: bool = None,
    lg7: bool = None,
    lg8: bool = None,
    lg9: bool = None,
    ma_0: bool = None,
    ma_1: bool = None,
    ma_2: bool = None,
    ma_3: bool = None,
    ma_4: bool = None,
    ma_5: bool = None,
    ma_auto: bool = None,
    mb_0: bool = None,
    mb_1: bool = None,
    mb_2: bool = None,
    mb_3: bool = None,
    mb_4: bool = None,
    mb_5: bool = None,
    mb_auto: bool = None,
    md1: bool = None,
    md10: bool = None,
    md11: bool = None,
    md12: bool = None,
    md2: bool = None,
    md3: bool = None,
    md4: bool = None,
    md5: bool = None,
    md6: bool = None,
    md7: bool = None,
    md8: bool = None,
    md9: bool = None,
    ml_0: bool = None,
    ml_1: bool = None,
    ml_2: bool = None,
    ml_3: bool = None,
    ml_4: bool = None,
    ml_5: bool = None,
    ml_auto: bool = None,
    mr_0: bool = None,
    mr_1: bool = None,
    mr_2: bool = None,
    mr_3: bool = None,
    mr_4: bool = None,
    mr_5: bool = None,
    mr_auto: bool = None,
    mt_0: bool = None,
    mt_1: bool = None,
    mt_2: bool = None,
    mt_3: bool = None,
    mt_4: bool = None,
    mt_5: bool = None,
    mt_auto: bool = None,
    mx_0: bool = None,
    mx_1: bool = None,
    mx_2: bool = None,
    mx_3: bool = None,
    mx_4: bool = None,
    mx_5: bool = None,
    mx_auto: bool = None,
    my_0: bool = None,
    my_1: bool = None,
    my_2: bool = None,
    my_3: bool = None,
    my_4: bool = None,
    my_5: bool = None,
    my_auto: bool = None,
    offset_lg0: bool = None,
    offset_lg1: bool = None,
    offset_lg10: bool = None,
    offset_lg11: bool = None,
    offset_lg12: bool = None,
    offset_lg2: bool = None,
    offset_lg3: bool = None,
    offset_lg4: bool = None,
    offset_lg5: bool = None,
    offset_lg6: bool = None,
    offset_lg7: bool = None,
    offset_lg8: bool = None,
    offset_lg9: bool = None,
    offset_md0: bool = None,
    offset_md1: bool = None,
    offset_md10: bool = None,
    offset_md11: bool = None,
    offset_md12: bool = None,
    offset_md2: bool = None,
    offset_md3: bool = None,
    offset_md4: bool = None,
    offset_md5: bool = None,
    offset_md6: bool = None,
    offset_md7: bool = None,
    offset_md8: bool = None,
    offset_md9: bool = None,
    offset_sm0: bool = None,
    offset_sm1: bool = None,
    offset_sm10: bool = None,
    offset_sm11: bool = None,
    offset_sm12: bool = None,
    offset_sm2: bool = None,
    offset_sm3: bool = None,
    offset_sm4: bool = None,
    offset_sm5: bool = None,
    offset_sm6: bool = None,
    offset_sm7: bool = None,
    offset_sm8: bool = None,
    offset_sm9: bool = None,
    offset_xl0: bool = None,
    offset_xl1: bool = None,
    offset_xl10: bool = None,
    offset_xl11: bool = None,
    offset_xl12: bool = None,
    offset_xl2: bool = None,
    offset_xl3: bool = None,
    offset_xl4: bool = None,
    offset_xl5: bool = None,
    offset_xl6: bool = None,
    offset_xl7: bool = None,
    offset_xl8: bool = None,
    offset_xl9: bool = None,
    offset_xs0: bool = None,
    offset_xs1: bool = None,
    offset_xs10: bool = None,
    offset_xs11: bool = None,
    offset_xs12: bool = None,
    offset_xs2: bool = None,
    offset_xs3: bool = None,
    offset_xs4: bool = None,
    offset_xs5: bool = None,
    offset_xs6: bool = None,
    offset_xs7: bool = None,
    offset_xs8: bool = None,
    offset_xs9: bool = None,
    order_lg1: bool = None,
    order_lg10: bool = None,
    order_lg11: bool = None,
    order_lg12: bool = None,
    order_lg2: bool = None,
    order_lg3: bool = None,
    order_lg4: bool = None,
    order_lg5: bool = None,
    order_lg6: bool = None,
    order_lg7: bool = None,
    order_lg8: bool = None,
    order_lg9: bool = None,
    order_md1: bool = None,
    order_md10: bool = None,
    order_md11: bool = None,
    order_md12: bool = None,
    order_md2: bool = None,
    order_md3: bool = None,
    order_md4: bool = None,
    order_md5: bool = None,
    order_md6: bool = None,
    order_md7: bool = None,
    order_md8: bool = None,
    order_md9: bool = None,
    order_sm1: bool = None,
    order_sm10: bool = None,
    order_sm11: bool = None,
    order_sm12: bool = None,
    order_sm2: bool = None,
    order_sm3: bool = None,
    order_sm4: bool = None,
    order_sm5: bool = None,
    order_sm6: bool = None,
    order_sm7: bool = None,
    order_sm8: bool = None,
    order_sm9: bool = None,
    order_xl1: bool = None,
    order_xl10: bool = None,
    order_xl11: bool = None,
    order_xl12: bool = None,
    order_xl2: bool = None,
    order_xl3: bool = None,
    order_xl4: bool = None,
    order_xl5: bool = None,
    order_xl6: bool = None,
    order_xl7: bool = None,
    order_xl8: bool = None,
    order_xl9: bool = None,
    order_xs1: bool = None,
    order_xs10: bool = None,
    order_xs11: bool = None,
    order_xs12: bool = None,
    order_xs2: bool = None,
    order_xs3: bool = None,
    order_xs4: bool = None,
    order_xs5: bool = None,
    order_xs6: bool = None,
    order_xs7: bool = None,
    order_xs8: bool = None,
    order_xs9: bool = None,
    pa_0: bool = None,
    pa_1: bool = None,
    pa_2: bool = None,
    pa_3: bool = None,
    pa_4: bool = None,
    pa_5: bool = None,
    pa_auto: bool = None,
    pb_0: bool = None,
    pb_1: bool = None,
    pb_2: bool = None,
    pb_3: bool = None,
    pb_4: bool = None,
    pb_5: bool = None,
    pb_auto: bool = None,
    pl_0: bool = None,
    pl_1: bool = None,
    pl_2: bool = None,
    pl_3: bool = None,
    pl_4: bool = None,
    pl_5: bool = None,
    pl_auto: bool = None,
    pr_0: bool = None,
    pr_1: bool = None,
    pr_2: bool = None,
    pr_3: bool = None,
    pr_4: bool = None,
    pr_5: bool = None,
    pr_auto: bool = None,
    pt_0: bool = None,
    pt_1: bool = None,
    pt_2: bool = None,
    pt_3: bool = None,
    pt_4: bool = None,
    pt_5: bool = None,
    pt_auto: bool = None,
    px_0: bool = None,
    px_1: bool = None,
    px_2: bool = None,
    px_3: bool = None,
    px_4: bool = None,
    px_5: bool = None,
    px_auto: bool = None,
    py_0: bool = None,
    py_1: bool = None,
    py_2: bool = None,
    py_3: bool = None,
    **kwargs,
) -> ValueElement[ipyvuetify.generated.Flex, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Flex)
def Flex(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Flex
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Flex


def _Footer(
    absolute: bool = None,
    app: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    elevation: typing.Union[float, str] = None,
    fixed: bool = None,
    height: typing.Union[float, str] = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    padless: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Footer, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Footer)
def Footer(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Footer
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Footer


def _Form(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lazy_validation: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Form, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Form)
def Form(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Form
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Form


def _Hover(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[float, str] = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    open_delay: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Hover, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Hover)
def Hover(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Hover
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Hover


def _Html(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = "",
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.Html, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Html)
def Html(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.Html
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Html


def _Icon(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    large: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    light: bool = None,
    right: bool = None,
    size: typing.Union[float, str] = None,
    slot: str = None,
    small: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    x_large: bool = None,
    x_small: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Icon, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Icon)
def Icon(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Icon
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Icon


def _Img(
    alt: str = None,
    aspect_ratio: typing.Union[str, float] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    contain: bool = None,
    eager: bool = None,
    gradient: str = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lazy_src: str = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    options: dict = None,
    position: str = None,
    sizes: str = None,
    slot: str = None,
    src: typing.Union[str, dict] = None,
    srcset: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[bool, str] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Img, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Img)
def Img(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Img
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Img


def _Input(
    append_icon: str = None,
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loading: bool = None,
    messages: typing.Union[str, list] = None,
    persistent_hint: bool = None,
    prepend_icon: str = None,
    readonly: bool = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Input, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Input)
def Input(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Input
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Input


def _Item(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Item, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Item)
def Item(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Item
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Item


def _ItemGroup(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    multiple: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ItemGroup, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ItemGroup)
def ItemGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ItemGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ItemGroup


def _Label(
    absolute: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    focused: bool = None,
    for_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: typing.Union[float, str] = None,
    light: bool = None,
    right: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Label, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Label)
def Label(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Label
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Label


def _Layout(
    align_baseline: bool = None,
    align_center: bool = None,
    align_content_center: bool = None,
    align_content_end: bool = None,
    align_content_space_around: bool = None,
    align_content_space_between: bool = None,
    align_content_start: bool = None,
    align_end: bool = None,
    align_start: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    column: bool = None,
    d_block: bool = None,
    d_contents: bool = None,
    d_flex: bool = None,
    d_grid: bool = None,
    d_inherit: bool = None,
    d_initial: bool = None,
    d_inline: bool = None,
    d_inline_block: bool = None,
    d_inline_flex: bool = None,
    d_inline_grid: bool = None,
    d_inline_table: bool = None,
    d_list_item: bool = None,
    d_none: bool = None,
    d_run_in: bool = None,
    d_table: bool = None,
    d_table_caption: bool = None,
    d_table_cell: bool = None,
    d_table_column: bool = None,
    d_table_column_group: bool = None,
    d_table_footer_group: bool = None,
    d_table_header_group: bool = None,
    d_table_row: bool = None,
    d_table_row_group: bool = None,
    fill_height: bool = None,
    id: str = None,
    justify_center: bool = None,
    justify_end: bool = None,
    justify_space_around: bool = None,
    justify_space_between: bool = None,
    justify_start: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    ma_0: bool = None,
    ma_1: bool = None,
    ma_2: bool = None,
    ma_3: bool = None,
    ma_4: bool = None,
    ma_5: bool = None,
    ma_auto: bool = None,
    mb_0: bool = None,
    mb_1: bool = None,
    mb_2: bool = None,
    mb_3: bool = None,
    mb_4: bool = None,
    mb_5: bool = None,
    mb_auto: bool = None,
    ml_0: bool = None,
    ml_1: bool = None,
    ml_2: bool = None,
    ml_3: bool = None,
    ml_4: bool = None,
    ml_5: bool = None,
    ml_auto: bool = None,
    mr_0: bool = None,
    mr_1: bool = None,
    mr_2: bool = None,
    mr_3: bool = None,
    mr_4: bool = None,
    mr_5: bool = None,
    mr_auto: bool = None,
    mt_0: bool = None,
    mt_1: bool = None,
    mt_2: bool = None,
    mt_3: bool = None,
    mt_4: bool = None,
    mt_5: bool = None,
    mt_auto: bool = None,
    mx_0: bool = None,
    mx_1: bool = None,
    mx_2: bool = None,
    mx_3: bool = None,
    mx_4: bool = None,
    mx_5: bool = None,
    mx_auto: bool = None,
    my_0: bool = None,
    my_1: bool = None,
    my_2: bool = None,
    my_3: bool = None,
    my_4: bool = None,
    my_5: bool = None,
    my_auto: bool = None,
    pa_0: bool = None,
    pa_1: bool = None,
    pa_2: bool = None,
    pa_3: bool = None,
    pa_4: bool = None,
    pa_5: bool = None,
    pa_auto: bool = None,
    pb_0: bool = None,
    pb_1: bool = None,
    pb_2: bool = None,
    pb_3: bool = None,
    pb_4: bool = None,
    pb_5: bool = None,
    pb_auto: bool = None,
    pl_0: bool = None,
    pl_1: bool = None,
    pl_2: bool = None,
    pl_3: bool = None,
    pl_4: bool = None,
    pl_5: bool = None,
    pl_auto: bool = None,
    pr_0: bool = None,
    pr_1: bool = None,
    pr_2: bool = None,
    pr_3: bool = None,
    pr_4: bool = None,
    pr_5: bool = None,
    pr_auto: bool = None,
    pt_0: bool = None,
    pt_1: bool = None,
    pt_2: bool = None,
    pt_3: bool = None,
    pt_4: bool = None,
    pt_5: bool = None,
    pt_auto: bool = None,
    px_0: bool = None,
    px_1: bool = None,
    px_2: bool = None,
    px_3: bool = None,
    px_4: bool = None,
    px_5: bool = None,
    px_auto: bool = None,
    py_0: bool = None,
    py_1: bool = None,
    py_2: bool = None,
    py_3: bool = None,
    py_4: bool = None,
    py_5: bool = None,
    py_auto: bool = None,
    reverse: bool = None,
    row: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    wrap: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Layout, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Layout)
def Layout(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Layout
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Layout


def _Lazy(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    min_height: typing.Union[float, str] = None,
    options: dict = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Lazy, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Lazy)
def Lazy(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Lazy
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Lazy


def _List(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    elevation: typing.Union[float, str] = None,
    expand: bool = None,
    flat: bool = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    nav: bool = None,
    rounded: bool = None,
    shaped: bool = None,
    slot: str = None,
    style_: str = None,
    subheader: bool = None,
    tabbable: bool = None,
    tag: str = None,
    three_line: bool = None,
    tile: bool = None,
    tooltip: str = None,
    two_line: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.List, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_List)
def List(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.List
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _List


def _ListGroup(
    active_class: str = None,
    append_icon: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    eager: bool = None,
    group: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    no_action: bool = None,
    prepend_icon: str = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    sub_group: bool = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListGroup, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListGroup)
def ListGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListGroup


def _ListItem(
    active_class: str = None,
    append: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    exact: bool = None,
    exact_active_class: str = None,
    href: typing.Union[str, dict] = None,
    inactive: bool = None,
    input_value: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    link: bool = None,
    nuxt: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    selectable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    target: str = None,
    three_line: bool = None,
    to: typing.Union[str, dict] = None,
    tooltip: str = None,
    two_line: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItem)
def ListItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItem


def _ListItemAction(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemAction, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemAction)
def ListItemAction(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemAction
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemAction


def _ListItemActionText(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemActionText, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemActionText)
def ListItemActionText(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemActionText
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemActionText


def _ListItemAvatar(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    height: typing.Union[float, str] = None,
    horizontal: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    right: bool = None,
    size: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemAvatar, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemAvatar)
def ListItemAvatar(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemAvatar
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemAvatar


def _ListItemContent(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemContent, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemContent)
def ListItemContent(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemContent
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemContent


def _ListItemGroup(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    multiple: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemGroup, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemGroup)
def ListItemGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemGroup


def _ListItemIcon(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemIcon, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemIcon)
def ListItemIcon(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemIcon
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemIcon


def _ListItemSubtitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemSubtitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemSubtitle)
def ListItemSubtitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemSubtitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemSubtitle


def _ListItemTitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemTitle)
def ListItemTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemTitle


def _Menu(
    absolute: bool = None,
    activator: Any = None,
    allow_overflow: bool = None,
    attach: Any = None,
    attributes: dict = {},
    auto: bool = None,
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[float, str] = None,
    close_on_click: bool = None,
    close_on_content_click: bool = None,
    content_class: str = None,
    dark: bool = None,
    disable_keys: bool = None,
    disabled: bool = None,
    eager: bool = None,
    fixed: bool = None,
    internal_activator: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    nudge_bottom: typing.Union[float, str] = None,
    nudge_left: typing.Union[float, str] = None,
    nudge_right: typing.Union[float, str] = None,
    nudge_top: typing.Union[float, str] = None,
    nudge_width: typing.Union[float, str] = None,
    offset_overflow: bool = None,
    offset_x: bool = None,
    offset_y: bool = None,
    open_delay: typing.Union[float, str] = None,
    open_on_click: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    position_x: float = None,
    position_y: float = None,
    return_value: Any = None,
    right: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    top: bool = None,
    transition: typing.Union[bool, str] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    z_index: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Menu, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Menu)
def Menu(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Menu
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Menu


def _MenuTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.MenuTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_MenuTransition)
def MenuTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.MenuTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _MenuTransition


def _Messages(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Messages, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Messages)
def Messages(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Messages
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Messages


def _NavigationDrawer(
    absolute: bool = None,
    app: bool = None,
    attributes: dict = {},
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    clipped: bool = None,
    color: str = None,
    dark: bool = None,
    disable_resize_watcher: bool = None,
    disable_route_watcher: bool = None,
    expand_on_hover: bool = None,
    fixed: bool = None,
    floating: bool = None,
    height: typing.Union[float, str] = None,
    hide_overlay: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mini_variant: bool = None,
    mini_variant_width: typing.Union[float, str] = None,
    mobile_break_point: typing.Union[float, str] = None,
    overlay_color: str = None,
    overlay_opacity: typing.Union[float, str] = None,
    permanent: bool = None,
    right: bool = None,
    slot: str = None,
    src: typing.Union[str, dict] = None,
    stateless: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    temporary: bool = None,
    tooltip: str = None,
    touchless: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.NavigationDrawer, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_NavigationDrawer)
def NavigationDrawer(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.NavigationDrawer
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _NavigationDrawer


def _OverflowBtn(
    allow_overflow: bool = None,
    append_icon: str = None,
    append_outer_icon: str = None,
    attach: Any = None,
    attributes: dict = {},
    auto_select_first: bool = None,
    autofocus: bool = None,
    background_color: str = None,
    cache_items: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: str = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[bool, float, str] = None,
    dark: bool = None,
    deletable_chips: bool = None,
    dense: bool = None,
    disable_lookup: bool = None,
    disabled: bool = None,
    eager: bool = None,
    editable: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    filled: bool = None,
    flat: bool = None,
    full_width: bool = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hint: str = None,
    id: str = None,
    item_color: str = None,
    item_disabled: typing.Union[str, list] = None,
    item_text: typing.Union[str, list] = None,
    item_value: typing.Union[str, list] = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    menu_props: typing.Union[str, list, dict] = None,
    messages: typing.Union[str, list] = None,
    multiple: bool = None,
    no_data_text: str = None,
    no_filter: bool = None,
    open_on_clear: bool = None,
    outlined: bool = None,
    persistent_hint: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: str = None,
    prepend_inner_icon: str = None,
    readonly: bool = None,
    return_object: bool = None,
    reverse: bool = None,
    rounded: bool = None,
    rules: list = [],
    search_input: str = None,
    segmented: bool = None,
    shaped: bool = None,
    single_line: bool = None,
    slot: str = None,
    small_chips: bool = None,
    solo: bool = None,
    solo_inverted: bool = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    suffix: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.OverflowBtn, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_OverflowBtn)
def OverflowBtn(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.OverflowBtn
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _OverflowBtn


def _Overlay(
    absolute: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    opacity: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    z_index: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Overlay, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Overlay)
def Overlay(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Overlay
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Overlay


def _Pagination(
    attributes: dict = {},
    children: list = [],
    circle: bool = None,
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: float = None,
    light: bool = None,
    next_icon: str = None,
    prev_icon: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    total_visible: typing.Union[float, str] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: float = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Pagination, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Pagination)
def Pagination(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Pagination
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Pagination


def _Parallax(
    alt: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    src: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Parallax, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Parallax)
def Parallax(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Parallax
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Parallax


def _Picker(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    full_width: bool = None,
    landscape: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    no_title: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Picker, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Picker)
def Picker(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Picker
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Picker


def _ProgressCircular(
    attributes: dict = {},
    button: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    indeterminate: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rotate: typing.Union[float, str] = None,
    size: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[float, str] = None,
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ProgressCircular, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ProgressCircular)
def ProgressCircular(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ProgressCircular
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ProgressCircular


def _ProgressLinear(
    absolute: bool = None,
    active: bool = None,
    attributes: dict = {},
    background_color: str = None,
    background_opacity: typing.Union[float, str] = None,
    bottom: bool = None,
    buffer_value: typing.Union[float, str] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    fixed: bool = None,
    height: typing.Union[float, str] = None,
    indeterminate: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    query: bool = None,
    rounded: bool = None,
    slot: str = None,
    stream: bool = None,
    striped: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    top: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ProgressLinear, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ProgressLinear)
def ProgressLinear(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ProgressLinear
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ProgressLinear


def _Radio(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    name: str = None,
    off_icon: str = None,
    on_icon: str = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Radio, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Radio)
def Radio(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Radio
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Radio


def _RadioGroup(
    active_class: str = None,
    append_icon: str = None,
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    column: bool = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loading: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    messages: typing.Union[str, list] = None,
    multiple: bool = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: str = None,
    readonly: bool = None,
    row: bool = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.RadioGroup, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_RadioGroup)
def RadioGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.RadioGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _RadioGroup


def _RangeSlider(
    append_icon: str = None,
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    inverse_label: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    max: typing.Union[float, str] = None,
    messages: typing.Union[str, list] = None,
    min: typing.Union[float, str] = None,
    persistent_hint: bool = None,
    prepend_icon: str = None,
    readonly: bool = None,
    rules: list = [],
    slot: str = None,
    step: typing.Union[float, str] = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    tabbable: bool = None,
    thumb_color: str = None,
    thumb_label: typing.Union[bool, str] = None,
    thumb_size: typing.Union[float, str] = None,
    tick_labels: list = [],
    tick_size: typing.Union[float, str] = None,
    ticks: typing.Union[bool, str] = None,
    tooltip: str = None,
    track_color: str = None,
    track_fill_color: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.RangeSlider, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_RangeSlider)
def RangeSlider(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.RangeSlider
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _RangeSlider


def _Rating(
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    clearable: bool = None,
    close_delay: typing.Union[float, str] = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    empty_icon: str = None,
    full_icon: str = None,
    half_icon: str = None,
    half_increments: bool = None,
    hover: bool = None,
    large: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: typing.Union[float, str] = None,
    light: bool = None,
    open_delay: typing.Union[float, str] = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    size: typing.Union[float, str] = None,
    slot: str = None,
    small: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: float = None,
    x_large: bool = None,
    x_small: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Rating, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Rating)
def Rating(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Rating
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Rating


def _Responsive(
    aspect_ratio: typing.Union[str, float] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Responsive, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Responsive)
def Responsive(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Responsive
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Responsive


def _Row(
    align: str = None,
    align_content: str = None,
    align_content_lg: str = None,
    align_content_md: str = None,
    align_content_sm: str = None,
    align_content_xl: str = None,
    align_lg: str = None,
    align_md: str = None,
    align_sm: str = None,
    align_xl: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dense: bool = None,
    justify: str = None,
    justify_lg: str = None,
    justify_md: str = None,
    justify_sm: str = None,
    justify_xl: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    no_gutters: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Row, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Row)
def Row(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Row
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Row


def _ScaleTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScaleTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ScaleTransition)
def ScaleTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ScaleTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ScaleTransition


def _ScrollXReverseTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScrollXReverseTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ScrollXReverseTransition)
def ScrollXReverseTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ScrollXReverseTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ScrollXReverseTransition


def _ScrollXTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScrollXTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ScrollXTransition)
def ScrollXTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ScrollXTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ScrollXTransition


def _ScrollYReverseTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScrollYReverseTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ScrollYReverseTransition)
def ScrollYReverseTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ScrollYReverseTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ScrollYReverseTransition


def _ScrollYTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScrollYTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ScrollYTransition)
def ScrollYTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ScrollYTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ScrollYTransition


def _Select(
    append_icon: str = None,
    append_outer_icon: str = None,
    attach: Any = None,
    attributes: dict = {},
    autofocus: bool = None,
    background_color: str = None,
    cache_items: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: str = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[bool, float, str] = None,
    dark: bool = None,
    deletable_chips: bool = None,
    dense: bool = None,
    disable_lookup: bool = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    filled: bool = None,
    flat: bool = None,
    full_width: bool = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hide_selected: bool = None,
    hint: str = None,
    id: str = None,
    item_color: str = None,
    item_disabled: typing.Union[str, list] = None,
    item_text: typing.Union[str, list] = None,
    item_value: typing.Union[str, list] = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    menu_props: typing.Union[str, list, dict] = None,
    messages: typing.Union[str, list] = None,
    multiple: bool = None,
    no_data_text: str = None,
    open_on_clear: bool = None,
    outlined: bool = None,
    persistent_hint: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: str = None,
    prepend_inner_icon: str = None,
    readonly: bool = None,
    return_object: bool = None,
    reverse: bool = None,
    rounded: bool = None,
    rules: list = [],
    shaped: bool = None,
    single_line: bool = None,
    slot: str = None,
    small_chips: bool = None,
    solo: bool = None,
    solo_inverted: bool = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    suffix: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Select, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Select)
def Select(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Select
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Select


def _Sheet(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    elevation: typing.Union[float, str] = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Sheet, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Sheet)
def Sheet(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Sheet
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Sheet


def _SimpleCheckbox(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    indeterminate: bool = None,
    indeterminate_icon: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    off_icon: str = None,
    on_icon: str = None,
    ripple: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SimpleCheckbox, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SimpleCheckbox)
def SimpleCheckbox(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SimpleCheckbox
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SimpleCheckbox


def _SimpleTable(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    dense: bool = None,
    fixed_header: bool = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SimpleTable, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SimpleTable)
def SimpleTable(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SimpleTable
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SimpleTable


def _SkeletonLoader(
    attributes: dict = {},
    boilerplate: bool = None,
    children: list = [],
    class_: str = None,
    dark: bool = None,
    elevation: typing.Union[float, str] = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loading: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tile: bool = None,
    tooltip: str = None,
    transition: str = None,
    type: str = None,
    types: dict = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SkeletonLoader, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SkeletonLoader)
def SkeletonLoader(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SkeletonLoader
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SkeletonLoader


def _SlideGroup(
    active_class: str = None,
    attributes: dict = {},
    center_active: bool = None,
    children: list = [],
    class_: str = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    mobile_break_point: typing.Union[float, str] = None,
    multiple: bool = None,
    next_icon: str = None,
    prev_icon: str = None,
    show_arrows: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideGroup, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SlideGroup)
def SlideGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SlideGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SlideGroup


def _SlideItem(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SlideItem)
def SlideItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SlideItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SlideItem


def _SlideXReverseTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideXReverseTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SlideXReverseTransition)
def SlideXReverseTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SlideXReverseTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SlideXReverseTransition


def _SlideXTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideXTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SlideXTransition)
def SlideXTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SlideXTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SlideXTransition


def _SlideYReverseTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideYReverseTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SlideYReverseTransition)
def SlideYReverseTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SlideYReverseTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SlideYReverseTransition


def _SlideYTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideYTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SlideYTransition)
def SlideYTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SlideYTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SlideYTransition


def _Slider(
    append_icon: str = None,
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    inverse_label: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    max: typing.Union[float, str] = None,
    messages: typing.Union[str, list] = None,
    min: typing.Union[float, str] = None,
    persistent_hint: bool = None,
    prepend_icon: str = None,
    readonly: bool = None,
    rules: list = [],
    slot: str = None,
    step: typing.Union[float, str] = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    tabbable: bool = None,
    thumb_color: str = None,
    thumb_label: typing.Union[bool, str] = None,
    thumb_size: typing.Union[float, str] = None,
    tick_labels: list = [],
    tick_size: typing.Union[float, str] = None,
    ticks: typing.Union[bool, str] = None,
    tooltip: str = None,
    track_color: str = None,
    track_fill_color: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Slider, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Slider)
def Slider(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Slider
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Slider


def _Snackbar(
    absolute: bool = None,
    attributes: dict = {},
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    multi_line: bool = None,
    right: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    timeout: float = None,
    tooltip: str = None,
    top: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Snackbar, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Snackbar)
def Snackbar(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Snackbar
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Snackbar


def _Spacer(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Spacer, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Spacer)
def Spacer(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Spacer
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Spacer


def _Sparkline(
    attributes: dict = {},
    auto_draw: bool = None,
    auto_draw_duration: float = None,
    auto_draw_easing: str = None,
    auto_line_width: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    fill: bool = None,
    gradient: list = [],
    gradient_direction: str = None,
    height: typing.Union[str, float] = None,
    label_size: typing.Union[float, str] = None,
    labels: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    line_width: typing.Union[str, float] = None,
    padding: typing.Union[str, float] = None,
    show_labels: bool = None,
    slot: str = None,
    smooth: typing.Union[bool, float, str] = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Sparkline, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Sparkline)
def Sparkline(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Sparkline
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Sparkline


def _SpeedDial(
    absolute: bool = None,
    attributes: dict = {},
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    direction: str = None,
    fixed: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    mode: str = None,
    open_on_hover: bool = None,
    origin: str = None,
    right: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    top: bool = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SpeedDial, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SpeedDial)
def SpeedDial(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SpeedDial
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SpeedDial


def _Stepper(
    alt_labels: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    non_linear: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Stepper, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Stepper)
def Stepper(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Stepper
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Stepper


def _StepperContent(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    step: typing.Union[float, str] = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperContent, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperContent)
def StepperContent(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperContent
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperContent


def _StepperHeader(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperHeader, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperHeader)
def StepperHeader(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperHeader
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperHeader


def _StepperItems(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperItems, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperItems)
def StepperItems(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperItems
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperItems


def _StepperStep(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    complete: bool = None,
    complete_icon: str = None,
    edit_icon: str = None,
    editable: bool = None,
    error_icon: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rules: list = [],
    slot: str = None,
    step: typing.Union[float, str] = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperStep, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperStep)
def StepperStep(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperStep
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperStep


def _Subheader(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Subheader, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Subheader)
def Subheader(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Subheader
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Subheader


def _Switch(
    append_icon: str = None,
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    false_value: Any = None,
    flat: bool = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    input_value: Any = None,
    inset: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loading: typing.Union[bool, str] = None,
    messages: typing.Union[str, list] = None,
    multiple: bool = None,
    persistent_hint: bool = None,
    prepend_icon: str = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    tabbable: bool = None,
    tooltip: str = None,
    true_value: Any = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Switch, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Switch)
def Switch(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Switch
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Switch


def _SystemBar(
    absolute: bool = None,
    app: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    fixed: bool = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    lights_out: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    window: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SystemBar, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SystemBar)
def SystemBar(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SystemBar
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SystemBar


def _Tab(
    active_class: str = None,
    append: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    disabled: bool = None,
    exact: bool = None,
    exact_active_class: str = None,
    href: typing.Union[str, dict] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    link: bool = None,
    nuxt: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    target: str = None,
    to: typing.Union[str, dict] = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Tab, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Tab)
def Tab(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Tab
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Tab


def _TabItem(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    eager: bool = None,
    id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    reverse_transition: typing.Union[bool, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[bool, str] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TabItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TabItem)
def TabItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TabItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TabItem


def _TabReverseTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TabReverseTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TabReverseTransition)
def TabReverseTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TabReverseTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TabReverseTransition


def _TabTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    leave_absolute: bool = None,
    mode: str = None,
    origin: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TabTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TabTransition)
def TabTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TabTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TabTransition


def _TableOverflow(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TableOverflow, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TableOverflow)
def TableOverflow(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TableOverflow
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TableOverflow


def _Tabs(
    active_class: str = None,
    align_with_title: bool = None,
    attributes: dict = {},
    background_color: str = None,
    center_active: bool = None,
    centered: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    fixed_tabs: bool = None,
    grow: bool = None,
    height: typing.Union[float, str] = None,
    hide_slider: bool = None,
    icons_and_text: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mobile_break_point: typing.Union[float, str] = None,
    next_icon: str = None,
    optional: bool = None,
    prev_icon: str = None,
    right: bool = None,
    show_arrows: bool = None,
    slider_color: str = None,
    slider_size: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Tabs, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Tabs)
def Tabs(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Tabs
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Tabs


def _TabsItems(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    continuous: bool = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    multiple: bool = None,
    next_icon: typing.Union[bool, str] = None,
    prev_icon: typing.Union[bool, str] = None,
    reverse: bool = None,
    show_arrows: bool = None,
    show_arrows_on_hover: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    touch: dict = None,
    touchless: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TabsItems, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TabsItems)
def TabsItems(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TabsItems
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TabsItems


def _TabsSlider(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TabsSlider, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TabsSlider)
def TabsSlider(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TabsSlider
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TabsSlider


def _Text(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: str = "",
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Text, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Text)
def Text(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Text
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Text


def _TextField(
    append_icon: str = None,
    append_outer_icon: str = None,
    attributes: dict = {},
    autofocus: bool = None,
    background_color: str = None,
    children: list = [],
    class_: str = None,
    clear_icon: str = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[bool, float, str] = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    filled: bool = None,
    flat: bool = None,
    full_width: bool = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    messages: typing.Union[str, list] = None,
    outlined: bool = None,
    persistent_hint: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: str = None,
    prepend_inner_icon: str = None,
    readonly: bool = None,
    reverse: bool = None,
    rounded: bool = None,
    rules: list = [],
    shaped: bool = None,
    single_line: bool = None,
    slot: str = None,
    solo: bool = None,
    solo_inverted: bool = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    suffix: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TextField, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TextField)
def TextField(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TextField
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TextField


def _Textarea(
    append_icon: str = None,
    append_outer_icon: str = None,
    attributes: dict = {},
    auto_grow: bool = None,
    autofocus: bool = None,
    background_color: str = None,
    children: list = [],
    class_: str = None,
    clear_icon: str = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[bool, float, str] = None,
    dark: bool = None,
    dense: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_count: typing.Union[float, str] = None,
    error_messages: typing.Union[str, list] = None,
    filled: bool = None,
    flat: bool = None,
    full_width: bool = None,
    height: typing.Union[float, str] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loader_height: typing.Union[float, str] = None,
    loading: typing.Union[bool, str] = None,
    messages: typing.Union[str, list] = None,
    no_resize: bool = None,
    outlined: bool = None,
    persistent_hint: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: str = None,
    prepend_inner_icon: str = None,
    readonly: bool = None,
    reverse: bool = None,
    rounded: bool = None,
    row_height: typing.Union[float, str] = None,
    rows: typing.Union[float, str] = None,
    rules: list = [],
    shaped: bool = None,
    single_line: bool = None,
    slot: str = None,
    solo: bool = None,
    solo_inverted: bool = None,
    style_: str = None,
    success: bool = None,
    success_messages: typing.Union[str, list] = None,
    suffix: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on_blur: bool = None,
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Textarea, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Textarea)
def Textarea(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Textarea
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Textarea


def _ThemeProvider(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    root: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ThemeProvider, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ThemeProvider)
def ThemeProvider(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ThemeProvider
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ThemeProvider


def _TimePicker(
    allowed_hours: list = None,
    allowed_minutes: list = None,
    allowed_seconds: list = None,
    ampm_in_title: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    format: str = None,
    full_width: bool = None,
    header_color: str = None,
    landscape: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max: str = None,
    min: str = None,
    no_title: bool = None,
    readonly: bool = None,
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    use_seconds: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TimePicker, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TimePicker)
def TimePicker(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TimePicker
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TimePicker


def _TimePickerClock(
    ampm: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    disabled: bool = None,
    double: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max: float = None,
    min: float = None,
    readonly: bool = None,
    rotate: float = None,
    scrollable: bool = None,
    slot: str = None,
    step: float = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: float = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TimePickerClock, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TimePickerClock)
def TimePickerClock(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TimePickerClock
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TimePickerClock


def _TimePickerTitle(
    ampm: bool = None,
    ampm_readonly: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    hour: float = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    minute: float = None,
    period: str = None,
    readonly: bool = None,
    second: float = None,
    selecting: float = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    use_seconds: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TimePickerTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TimePickerTitle)
def TimePickerTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TimePickerTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TimePickerTitle


def _Timeline(
    align_top: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dark: bool = None,
    dense: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    reverse: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Timeline, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Timeline)
def Timeline(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Timeline
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Timeline


def _TimelineItem(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    fill_dot: bool = None,
    hide_dot: bool = None,
    icon: str = None,
    icon_color: str = None,
    large: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    light: bool = None,
    right: bool = None,
    slot: str = None,
    small: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TimelineItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TimelineItem)
def TimelineItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TimelineItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TimelineItem


def _Toolbar(
    absolute: bool = None,
    attributes: dict = {},
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    collapse: bool = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    elevation: typing.Union[float, str] = None,
    extended: bool = None,
    extension_height: typing.Union[float, str] = None,
    flat: bool = None,
    floating: bool = None,
    height: typing.Union[float, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    max_height: typing.Union[float, str] = None,
    max_width: typing.Union[float, str] = None,
    min_height: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    prominent: bool = None,
    short: bool = None,
    slot: str = None,
    src: typing.Union[str, dict] = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[float, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Toolbar, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Toolbar)
def Toolbar(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Toolbar
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Toolbar


def _ToolbarItems(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ToolbarItems, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ToolbarItems)
def ToolbarItems(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ToolbarItems
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ToolbarItems


def _ToolbarTitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ToolbarTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ToolbarTitle)
def ToolbarTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ToolbarTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ToolbarTitle


def _Tooltip(
    absolute: bool = None,
    activator: Any = None,
    allow_overflow: bool = None,
    attach: Any = None,
    attributes: dict = {},
    bottom: bool = None,
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[float, str] = None,
    color: str = None,
    content_class: str = None,
    dark: bool = None,
    disabled: bool = None,
    eager: bool = None,
    fixed: bool = None,
    internal_activator: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    left: bool = None,
    light: bool = None,
    max_width: typing.Union[float, str] = None,
    min_width: typing.Union[float, str] = None,
    nudge_bottom: typing.Union[float, str] = None,
    nudge_left: typing.Union[float, str] = None,
    nudge_right: typing.Union[float, str] = None,
    nudge_top: typing.Union[float, str] = None,
    nudge_width: typing.Union[float, str] = None,
    offset_overflow: bool = None,
    open_delay: typing.Union[float, str] = None,
    open_on_click: bool = None,
    open_on_hover: bool = None,
    position_x: float = None,
    position_y: float = None,
    right: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    top: bool = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    z_index: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Tooltip, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Tooltip)
def Tooltip(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Tooltip
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Tooltip


def _Treeview(
    activatable: bool = None,
    active: list = [],
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    dark: bool = None,
    dense: bool = None,
    expand_icon: str = None,
    hoverable: bool = None,
    indeterminate_icon: str = None,
    item_children: str = None,
    item_disabled: str = None,
    item_key: str = None,
    item_text: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    loading_icon: str = None,
    multiple_active: bool = None,
    off_icon: str = None,
    on_icon: str = None,
    open_: list = [],
    open_all: bool = None,
    open_on_click: bool = None,
    return_object: bool = None,
    rounded: bool = None,
    search: str = None,
    selectable: bool = None,
    selected_color: str = None,
    selection_type: str = None,
    shaped: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Treeview, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Treeview)
def Treeview(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Treeview
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Treeview


def _TreeviewNode(
    activatable: bool = None,
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    expand_icon: str = None,
    indeterminate_icon: str = None,
    item: dict = None,
    item_children: str = None,
    item_disabled: str = None,
    item_key: str = None,
    item_text: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    level: float = None,
    loading_icon: str = None,
    off_icon: str = None,
    on_icon: str = None,
    open_on_click: bool = None,
    rounded: bool = None,
    selectable: bool = None,
    selected_color: str = None,
    shaped: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TreeviewNode, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_TreeviewNode)
def TreeviewNode(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TreeviewNode
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TreeviewNode


def _VirtualTable(
    attributes: dict = {},
    children: list = [],
    chunk_size: float = None,
    class_: str = None,
    dark: bool = None,
    dense: bool = None,
    fixed_header: bool = None,
    header_height: float = None,
    height: typing.Union[float, str] = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    row_height: float = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.VirtualTable, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_VirtualTable)
def VirtualTable(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.VirtualTable
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _VirtualTable


def _VuetifyTemplate(
    components: dict = None,
    css: str = None,
    data: str = None,
    events: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    methods: str = None,
    tabbable: bool = None,
    template: typing.Union[Element[ipyvue.Template], str] = None,
    tooltip: str = None,
) -> Element[ipyvuetify.VuetifyTemplate]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_VuetifyTemplate)
def VuetifyTemplate(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.VuetifyTemplate
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return Element(comp, kwargs=kwargs)


del _VuetifyTemplate


def _VuetifyWidget(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.VuetifyWidget, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_VuetifyWidget)
def VuetifyWidget(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.VuetifyWidget
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _VuetifyWidget


def _Window(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    continuous: bool = None,
    dark: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    light: bool = None,
    mandatory: bool = None,
    max: typing.Union[float, str] = None,
    multiple: bool = None,
    next_icon: typing.Union[bool, str] = None,
    prev_icon: typing.Union[bool, str] = None,
    reverse: bool = None,
    show_arrows: bool = None,
    show_arrows_on_hover: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    touch: dict = None,
    touchless: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Window, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Window)
def Window(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Window
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Window


def _WindowItem(
    active_class: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    eager: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    reverse_transition: typing.Union[bool, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[bool, str] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.WindowItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_WindowItem)
def WindowItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.WindowItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _WindowItem
