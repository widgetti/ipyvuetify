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
    border: typing.Union[bool, str, str, str, str] = None,
    border_color: str = None,
    children: list = [],
    class_: str = None,
    closable: bool = None,
    close_icon: typing.Union[str, list] = None,
    close_label: str = None,
    color: str = None,
    density: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    icon: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    position: str = None,
    prominent: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    theme: str = None,
    title: str = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    width: typing.Union[str, float] = None,
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


def _AlertTitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AlertTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_AlertTitle)
def AlertTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.AlertTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _AlertTitle


def _App(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    full_height: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    overlaps: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
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
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    collapse: bool = None,
    color: str = None,
    density: str = None,
    elevation: typing.Union[str, float] = None,
    extended: bool = None,
    extension_height: typing.Union[str, float] = None,
    flat: bool = None,
    floating: bool = None,
    height: typing.Union[str, float] = None,
    image: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    model_value: bool = None,
    name: str = None,
    order: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    scroll_behavior: str = None,
    scroll_target: str = None,
    scroll_threshold: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    active: bool = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    block: bool = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    flat: bool = None,
    height: typing.Union[str, float] = None,
    href: str = None,
    icon: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    location: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    prepend_icon: typing.Union[str, list] = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    stacked: bool = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
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


def _AppBarTitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AppBarTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_AppBarTitle)
def AppBarTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.AppBarTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _AppBarTitle


def _Autocomplete(
    active: bool = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    auto_select_first: typing.Union[bool, str] = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: typing.Union[str, list] = None,
    clearable: bool = None,
    closable_chips: bool = None,
    close_text: str = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    custom_filter: str = None,
    custom_key_filter: dict = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    flat: bool = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hint: str = None,
    id: str = None,
    item_children: str = None,
    item_color: str = None,
    item_props: str = None,
    item_title: str = None,
    item_value: str = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    menu: bool = None,
    menu_icon: typing.Union[str, list] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    no_data_text: str = None,
    no_filter: bool = None,
    open_on_clear: bool = None,
    open_text: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: typing.Union[str, list] = None,
    prepend_inner_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    return_object: bool = None,
    reverse: bool = None,
    role: str = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    search: str = None,
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    suffix: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    value_comparator: str = None,
    variant: str = None,
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
    density: str = None,
    end: bool = None,
    icon: typing.Union[str, list] = None,
    image: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rounded: typing.Union[str, float, bool] = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    start: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
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
    bordered: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    content: typing.Union[str, float] = None,
    dot: bool = None,
    floating: bool = None,
    icon: typing.Union[str, list] = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    max: typing.Union[str, float] = None,
    model_value: bool = None,
    offset_x: typing.Union[str, float] = None,
    offset_y: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    text_color: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    attributes: dict = {},
    avatar: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    icon: typing.Union[str, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: str = None,
    location: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    stacked: bool = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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


def _BannerActions(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BannerActions, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_BannerActions)
def BannerActions(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.BannerActions
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _BannerActions


def _BannerText(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BannerText, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_BannerText)
def BannerText(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.BannerText
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _BannerText


def _BottomNavigation(
    absolute: bool = None,
    active: bool = None,
    attributes: dict = {},
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    grow: bool = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    mode: str = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    order: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    absolute: bool = None,
    activator: str = None,
    activator_props: dict = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disabled: bool = None,
    eager: bool = None,
    fullscreen: bool = None,
    height: typing.Union[str, float] = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    retain_focus: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, dict] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
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
    active_class: str = None,
    active_color: str = None,
    attributes: dict = {},
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    divider: str = None,
    icon: typing.Union[str, list] = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
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
    divider: typing.Union[str, float] = None,
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
    active: bool = None,
    active_class: str = None,
    active_color: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    exact: bool = None,
    href: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    replace: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    title: str = None,
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
    active: bool = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    block: bool = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    flat: bool = None,
    height: typing.Union[str, float] = None,
    href: str = None,
    icon: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    location: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    prepend_icon: typing.Union[str, list] = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    stacked: bool = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
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


def _BtnGroup(
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    divided: bool = None,
    elevation: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BtnGroup, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_BtnGroup)
def BtnGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.BtnGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _BtnGroup


def _BtnToggle(
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    divided: bool = None,
    elevation: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    model_value: Any = None,
    multiple: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
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


def _Card(
    append_avatar: str = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    flat: bool = None,
    height: typing.Union[str, float] = None,
    hover: bool = None,
    href: str = None,
    image: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    link: bool = None,
    loading: typing.Union[str, bool] = None,
    location: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    prepend_avatar: str = None,
    prepend_icon: typing.Union[str, list] = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    subtitle: str = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    theme: str = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    width: typing.Union[str, float] = None,
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


def _CardItem(
    append_avatar: str = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    density: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    prepend_avatar: str = None,
    prepend_icon: typing.Union[str, list] = None,
    slot: str = None,
    style_: str = None,
    subtitle: str = None,
    tabbable: bool = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CardItem)
def CardItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CardItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CardItem


def _CardSubtitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
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
    tag: str = None,
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
    tag: str = None,
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    continuous: bool = None,
    cycle: bool = None,
    delimiter_icon: typing.Union[str, list] = None,
    direction: str = None,
    disabled: bool = None,
    height: typing.Union[str, float] = None,
    hide_delimiter_background: bool = None,
    hide_delimiters: bool = None,
    interval: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    model_value: Any = None,
    next_icon: typing.Union[str, list] = None,
    prev_icon: typing.Union[str, list] = None,
    progress: typing.Union[str, bool] = None,
    reverse: bool = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    touch: Any = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    vertical_delimiters: typing.Union[bool, str, str] = None,
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
    alt: str = None,
    aspect_ratio: typing.Union[str, float] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    content_class: str = None,
    cover: bool = None,
    disabled: bool = None,
    eager: bool = None,
    gradient: str = None,
    height: typing.Union[str, float] = None,
    inline: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lazy_src: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    options: dict = None,
    reverse_transition: typing.Union[str, bool] = None,
    selected_class: str = None,
    sizes: str = None,
    slot: str = None,
    src: typing.Union[str, dict] = None,
    srcset: str = None,
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


def _Checkbox(
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    false_icon: typing.Union[str, list] = None,
    false_value: Any = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    indeterminate: bool = None,
    indeterminate_icon: typing.Union[str, list] = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_errors: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    ripple: bool = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: typing.Union[str, list] = None,
    true_value: Any = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    value: Any = None,
    value_comparator: str = None,
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


def _CheckboxBtn(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    false_icon: typing.Union[str, list] = None,
    false_value: Any = None,
    id: str = None,
    indeterminate: bool = None,
    indeterminate_icon: typing.Union[str, list] = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    readonly: bool = None,
    ripple: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: typing.Union[str, list] = None,
    true_value: Any = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    value_comparator: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CheckboxBtn, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CheckboxBtn)
def CheckboxBtn(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CheckboxBtn
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CheckboxBtn


def _Chip(
    active_class: str = None,
    append_avatar: str = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    closable: bool = None,
    close_icon: typing.Union[str, list] = None,
    close_label: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    draggable: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    filter: bool = None,
    filter_icon: str = None,
    href: str = None,
    label: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    link: bool = None,
    model_value: bool = None,
    pill: bool = None,
    prepend_avatar: str = None,
    prepend_icon: typing.Union[str, list] = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    column: bool = None,
    disabled: bool = None,
    filter: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    model_value: Any = None,
    multiple: bool = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: str = None,
    variant: str = None,
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


def _ClassIcon(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    icon: typing.Union[str, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ClassIcon, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ClassIcon)
def ClassIcon(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ClassIcon
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ClassIcon


def _Code(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Code, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Code)
def Code(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Code
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Code


def _Col(
    align_self: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    cols: typing.Union[str, float, bool] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lg: typing.Union[str, float, bool] = None,
    md: typing.Union[str, float, bool] = None,
    offset: typing.Union[str, float] = None,
    offset_lg: typing.Union[str, float] = None,
    offset_md: typing.Union[str, float] = None,
    offset_sm: typing.Union[str, float] = None,
    offset_xl: typing.Union[str, float] = None,
    offset_xxl: typing.Union[str, float] = None,
    order: typing.Union[str, float] = None,
    order_lg: typing.Union[str, float] = None,
    order_md: typing.Union[str, float] = None,
    order_sm: typing.Union[str, float] = None,
    order_xl: typing.Union[str, float] = None,
    order_xxl: typing.Union[str, float] = None,
    slot: str = None,
    sm: typing.Union[str, float, bool] = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    xl: typing.Union[str, float, bool] = None,
    xxl: typing.Union[str, float, bool] = None,
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
    border: typing.Union[str, float, bool] = None,
    canvas_height: typing.Union[str, float] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    dot_size: typing.Union[str, float] = None,
    elevation: typing.Union[str, float] = None,
    hide_canvas: bool = None,
    hide_inputs: bool = None,
    hide_sliders: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mode: str = None,
    model_value: str = None,
    modes: list = [],
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    show_swatches: bool = None,
    slot: str = None,
    style_: str = None,
    swatches: list = [],
    swatches_max_height: typing.Union[str, float] = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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


def _Combobox(
    active: bool = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    auto_select_first: typing.Union[bool, str] = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: typing.Union[str, list] = None,
    clearable: bool = None,
    closable_chips: bool = None,
    close_text: str = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    custom_filter: str = None,
    custom_key_filter: dict = None,
    delimiters: list = [],
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    flat: bool = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hint: str = None,
    id: str = None,
    item_children: str = None,
    item_color: str = None,
    item_props: str = None,
    item_title: str = None,
    item_value: str = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    menu: bool = None,
    menu_icon: typing.Union[str, list] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    no_data_text: str = None,
    no_filter: bool = None,
    open_on_clear: bool = None,
    open_text: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: typing.Union[str, list] = None,
    prepend_inner_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    return_object: bool = None,
    reverse: bool = None,
    role: str = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    suffix: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    value_comparator: str = None,
    variant: str = None,
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


def _ComponentIcon(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    icon: typing.Union[str, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ComponentIcon, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ComponentIcon)
def ComponentIcon(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ComponentIcon
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ComponentIcon


def _Container(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    fluid: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
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


def _Counter(
    active: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, dict] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[str, float] = None,
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


def _DataIterator(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    custom_filter: str = None,
    custom_key_filter: dict = None,
    expand_on_click: bool = None,
    expanded: list = [],
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    group_by: list = [],
    item_selectable: str = None,
    item_value: str = None,
    items: list = [],
    items_per_page: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: bool = None,
    model_value: list = [],
    multi_sort: bool = None,
    must_sort: bool = None,
    no_filter: bool = None,
    page: typing.Union[str, float] = None,
    return_object: bool = None,
    search: str = None,
    select_strategy: str = None,
    show_expand: bool = None,
    show_select: bool = None,
    slot: str = None,
    sort_by: list = [],
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: str = None,
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
    children: list = [],
    class_: str = None,
    color: str = None,
    custom_filter: str = None,
    custom_key_filter: dict = None,
    density: str = None,
    expand_on_click: bool = None,
    expanded: list = [],
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    first_icon: str = None,
    first_page_label: str = None,
    fixed_footer: bool = None,
    fixed_header: bool = None,
    group_by: list = [],
    headers: str = None,
    height: typing.Union[str, float] = None,
    hide_no_data: bool = None,
    hover: bool = None,
    item_selectable: str = None,
    item_value: str = None,
    items: list = [],
    items_per_page: typing.Union[str, float] = None,
    items_per_page_options: list = [],
    items_per_page_text: str = None,
    last_icon: str = None,
    last_page_label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    loading_text: str = None,
    model_value: list = [],
    multi_sort: bool = None,
    must_sort: bool = None,
    next_icon: str = None,
    next_page_label: str = None,
    no_data_text: str = None,
    no_filter: bool = None,
    page: typing.Union[str, float] = None,
    page_text: str = None,
    prev_icon: str = None,
    prev_page_label: str = None,
    return_object: bool = None,
    row_height: float = None,
    search: str = None,
    select_strategy: str = None,
    show_current_page: bool = None,
    show_expand: bool = None,
    show_select: bool = None,
    slot: str = None,
    sort_asc_icon: typing.Union[str, list] = None,
    sort_by: list = [],
    sort_desc_icon: typing.Union[str, list] = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: str = None,
    width: typing.Union[str, float] = None,
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


def _DataTableFooter(
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
) -> ValueElement[ipyvuetify.generated.DataTableFooter, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataTableFooter)
def DataTableFooter(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataTableFooter
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataTableFooter


def _DataTableRow(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    index: float = None,
    item: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableRow, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataTableRow)
def DataTableRow(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataTableRow
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataTableRow


def _DataTableRows(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    hide_no_data: bool = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    loading_text: str = None,
    no_data_text: str = None,
    row_height: float = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableRows, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataTableRows)
def DataTableRows(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataTableRows
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataTableRows


def _DataTableServer(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    expand_on_click: bool = None,
    expanded: list = [],
    first_icon: str = None,
    first_page_label: str = None,
    fixed_footer: bool = None,
    fixed_header: bool = None,
    group_by: list = [],
    headers: str = None,
    height: typing.Union[str, float] = None,
    hide_no_data: bool = None,
    hover: bool = None,
    item_selectable: str = None,
    item_value: str = None,
    items: list = [],
    items_length: typing.Union[str, float] = None,
    items_per_page: typing.Union[str, float] = None,
    items_per_page_options: list = [],
    items_per_page_text: str = None,
    last_icon: str = None,
    last_page_label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    loading_text: str = None,
    model_value: list = [],
    multi_sort: bool = None,
    must_sort: bool = None,
    next_icon: str = None,
    next_page_label: str = None,
    no_data_text: str = None,
    page: typing.Union[str, float] = None,
    page_text: str = None,
    prev_icon: str = None,
    prev_page_label: str = None,
    return_object: bool = None,
    row_height: float = None,
    search: str = None,
    select_strategy: str = None,
    show_current_page: bool = None,
    show_expand: bool = None,
    show_select: bool = None,
    slot: str = None,
    sort_asc_icon: typing.Union[str, list] = None,
    sort_by: list = [],
    sort_desc_icon: typing.Union[str, list] = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableServer, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataTableServer)
def DataTableServer(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataTableServer
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataTableServer


def _DataTableVirtual(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    custom_filter: str = None,
    custom_key_filter: dict = None,
    density: str = None,
    expand_on_click: bool = None,
    expanded: list = [],
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    fixed_footer: bool = None,
    fixed_header: bool = None,
    group_by: list = [],
    headers: str = None,
    height: typing.Union[str, float] = None,
    hide_no_data: bool = None,
    hover: bool = None,
    item_height: typing.Union[str, float] = None,
    item_selectable: str = None,
    item_value: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    loading_text: str = None,
    model_value: list = [],
    multi_sort: bool = None,
    must_sort: bool = None,
    no_data_text: str = None,
    no_filter: bool = None,
    return_object: bool = None,
    row_height: float = None,
    search: str = None,
    select_strategy: str = None,
    show_expand: bool = None,
    show_select: bool = None,
    slot: str = None,
    sort_asc_icon: typing.Union[str, list] = None,
    sort_by: list = [],
    sort_desc_icon: typing.Union[str, list] = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableVirtual, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataTableVirtual)
def DataTableVirtual(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataTableVirtual
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataTableVirtual


def _DateCard(
    allowed_dates: list = [],
    attributes: dict = {},
    cancel_text: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: typing.Union[str, bool, list] = None,
    display_date: Any = None,
    format: str = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    hide_weekdays: bool = None,
    hover_date: Any = None,
    input_mode: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    min: typing.Union[str, float] = None,
    mode_icon: str = None,
    model_value: list = [],
    multiple: bool = None,
    next_icon: str = None,
    ok_text: str = None,
    prev_icon: str = None,
    show_adjacent_months: bool = None,
    show_week: bool = None,
    side: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, dict] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    view_mode: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DateCard, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DateCard)
def DateCard(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DateCard
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DateCard


def _DatePicker(
    allowed_dates: list = [],
    attributes: dict = {},
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    calendar_icon: str = None,
    cancel_text: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: typing.Union[str, bool, list] = None,
    display_date: Any = None,
    elevation: typing.Union[str, float] = None,
    format: str = None,
    header: str = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    hide_weekdays: bool = None,
    hover_date: Any = None,
    input_mode: str = None,
    input_placeholder: str = None,
    input_text: str = None,
    keyboard_icon: str = None,
    landscape: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    max: typing.Union[str, float] = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    mode_icon: str = None,
    model_value: list = [],
    multiple: bool = None,
    next_icon: str = None,
    ok_text: str = None,
    position: str = None,
    prev_icon: str = None,
    rounded: typing.Union[str, float, bool] = None,
    show_adjacent_months: bool = None,
    show_week: bool = None,
    side: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    view_mode: str = None,
    width: typing.Union[str, float] = None,
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


def _DatePickerControls(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: typing.Union[str, bool, list] = None,
    display_date: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mode_icon: str = None,
    next_icon: str = None,
    prev_icon: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    view_mode: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerControls, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DatePickerControls)
def DatePickerControls(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePickerControls
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePickerControls


def _DatePickerHeader(
    append_icon: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    header: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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


def _DatePickerMonth(
    allowed_dates: list = [],
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    display_date: Any = None,
    format: str = None,
    hide_weekdays: bool = None,
    hover_date: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    min: typing.Union[str, float] = None,
    model_value: list = [],
    multiple: bool = None,
    show_adjacent_months: bool = None,
    show_week: bool = None,
    side: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerMonth, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DatePickerMonth)
def DatePickerMonth(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePickerMonth
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePickerMonth


def _DatePickerYears(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    display_date: Any = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    min: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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


def _DefaultsProvider(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    defaults: dict = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    reset: typing.Union[str, float] = None,
    root: typing.Union[str, bool] = None,
    scoped: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DefaultsProvider, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DefaultsProvider)
def DefaultsProvider(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DefaultsProvider
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DefaultsProvider


def _Dialog(
    absolute: bool = None,
    activator: str = None,
    activator_props: dict = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disabled: bool = None,
    eager: bool = None,
    fullscreen: bool = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    retain_focus: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, dict] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
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
    disabled: bool = None,
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


def _DialogTopTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
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
) -> ValueElement[ipyvuetify.generated.DialogTopTransition, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DialogTopTransition)
def DialogTopTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DialogTopTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DialogTopTransition


def _DialogTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    target: str = None,
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
    color: str = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    thickness: typing.Union[str, float] = None,
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


def _ExpandTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
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
    disabled: bool = None,
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
    attributes: dict = {},
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    collapse_icon: typing.Union[str, list] = None,
    color: str = None,
    disabled: bool = None,
    eager: bool = None,
    elevation: typing.Union[str, float] = None,
    expand_icon: typing.Union[str, list] = None,
    hide_actions: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
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


def _ExpansionPanelText(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
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
) -> ValueElement[ipyvuetify.generated.ExpansionPanelText, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpansionPanelText)
def ExpansionPanelText(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpansionPanelText
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpansionPanelText


def _ExpansionPanelTitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    collapse_icon: typing.Union[str, list] = None,
    color: str = None,
    expand_icon: typing.Union[str, list] = None,
    hide_actions: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanelTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpansionPanelTitle)
def ExpansionPanelTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpansionPanelTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpansionPanelTitle


def _ExpansionPanels(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    model_value: Any = None,
    multiple: bool = None,
    readonly: bool = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
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
    disabled: bool = None,
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
    disabled: bool = None,
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


def _Field(
    active: bool = None,
    append_inner_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: typing.Union[str, list] = None,
    clearable: bool = None,
    color: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    flat: bool = None,
    focused: bool = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    persistent_clear: bool = None,
    prepend_inner_icon: typing.Union[str, list] = None,
    reverse: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Field, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Field)
def Field(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Field
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Field


def _FieldLabel(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    floating: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FieldLabel, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_FieldLabel)
def FieldLabel(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.FieldLabel
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _FieldLabel


def _FileInput(
    active: bool = None,
    append_icon: typing.Union[str, list] = None,
    append_inner_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: typing.Union[str, list] = None,
    clearable: bool = None,
    color: str = None,
    counter: bool = None,
    counter_size_string: str = None,
    counter_string: str = None,
    density: str = None,
    direction: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    flat: bool = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    model_value: list = [],
    multiple: bool = None,
    name: str = None,
    persistent_clear: bool = None,
    persistent_hint: bool = None,
    prepend_icon: typing.Union[str, list] = None,
    prepend_inner_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    reverse: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    show_size: typing.Union[bool, float, float] = None,
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
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


def _Footer(
    absolute: bool = None,
    app: bool = None,
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    name: str = None,
    order: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    disabled: bool = None,
    fast_fail: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: bool = None,
    readonly: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
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
    close_delay: typing.Union[str, float] = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: bool = None,
    open_delay: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    end: bool = None,
    icon: typing.Union[str, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    size: typing.Union[str, float] = None,
    slot: str = None,
    start: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    content_class: str = None,
    cover: bool = None,
    eager: bool = None,
    gradient: str = None,
    height: typing.Union[str, float] = None,
    inline: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lazy_src: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    options: dict = None,
    sizes: str = None,
    slot: str = None,
    src: typing.Union[str, dict] = None,
    srcset: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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


def _InfiniteScroll(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    direction: str = None,
    empty_text: str = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    load_more_text: str = None,
    margin: typing.Union[str, float] = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    mode: str = None,
    side: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.InfiniteScroll, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_InfiniteScroll)
def InfiniteScroll(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.InfiniteScroll
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _InfiniteScroll


def _Input(
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_errors: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    selected_class: str = None,
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    model_value: Any = None,
    multiple: bool = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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


def _Kbd(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Kbd, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Kbd)
def Kbd(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Kbd
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Kbd


def _Label(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    clickable: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    full_height: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    overlaps: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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


def _LayoutItem(
    absolute: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: bool = None,
    name: str = None,
    order: typing.Union[str, float] = None,
    position: str = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.LayoutItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_LayoutItem)
def LayoutItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.LayoutItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _LayoutItem


def _Lazy(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
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
    width: typing.Union[str, float] = None,
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


def _LigatureIcon(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    icon: typing.Union[str, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.LigatureIcon, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_LigatureIcon)
def LigatureIcon(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.LigatureIcon
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _LigatureIcon


def _List(
    active_class: str = None,
    active_color: str = None,
    attributes: dict = {},
    base_color: str = None,
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    item_children: str = None,
    item_props: str = None,
    item_title: str = None,
    item_type: str = None,
    item_value: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: typing.Union[bool, str, str, str] = None,
    mandatory: bool = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    nav: bool = None,
    open_strategy: typing.Union[str, str, str, dict] = None,
    opened: list = [],
    return_object: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    select_strategy: str = None,
    selected: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: str = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
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
    active_color: str = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    base_color: str = None,
    children: list = [],
    class_: str = None,
    collapse_icon: typing.Union[str, list] = None,
    color: str = None,
    expand_icon: typing.Union[str, list] = None,
    fluid: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    prepend_icon: typing.Union[str, list] = None,
    slot: str = None,
    style_: str = None,
    subgroup: bool = None,
    tabbable: bool = None,
    tag: str = None,
    title: str = None,
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


def _ListImg(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListImg, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListImg)
def ListImg(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListImg
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListImg


def _ListItem(
    active: bool = None,
    active_class: str = None,
    active_color: str = None,
    append_avatar: str = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    base_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    height: typing.Union[str, float] = None,
    href: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: str = None,
    link: bool = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    nav: bool = None,
    prepend_avatar: str = None,
    prepend_icon: typing.Union[str, list] = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    subtitle: typing.Union[str, float, bool] = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    title: typing.Union[str, float, bool] = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
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
    end: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    start: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
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


def _ListItemMedia(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    end: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    start: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemMedia, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListItemMedia)
def ListItemMedia(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListItemMedia
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListItemMedia


def _ListItemSubtitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
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
    tag: str = None,
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


def _ListSubheader(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListSubheader, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ListSubheader)
def ListSubheader(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ListSubheader
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ListSubheader


def _LocaleProvider(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    fallback_locale: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    locale: str = None,
    rtl: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.LocaleProvider, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_LocaleProvider)
def LocaleProvider(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.LocaleProvider
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _LocaleProvider


def _Main(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Main, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Main)
def Main(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Main
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Main


def _Menu(
    activator: str = None,
    activator_props: dict = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disabled: bool = None,
    eager: bool = None,
    height: typing.Union[str, float] = None,
    id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, dict] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
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


def _Messages(
    active: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    messages: typing.Union[str, list] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, dict] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disable_resize_watcher: bool = None,
    disable_route_watcher: bool = None,
    elevation: typing.Union[str, float] = None,
    expand_on_hover: bool = None,
    floating: bool = None,
    image: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    model_value: bool = None,
    name: str = None,
    order: typing.Union[str, float] = None,
    permanent: bool = None,
    rail: bool = None,
    rail_width: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    scrim: typing.Union[str, bool] = None,
    slot: str = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    temporary: bool = None,
    theme: str = None,
    tooltip: str = None,
    touchless: bool = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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


def _NoSsr(
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
) -> ValueElement[ipyvuetify.generated.NoSsr, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_NoSsr)
def NoSsr(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.NoSsr
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _NoSsr


def _OtpInput(
    attributes: dict = {},
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    divider: str = None,
    error: bool = None,
    focus_all: bool = None,
    focused: bool = None,
    height: typing.Union[str, float] = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: typing.Union[str, float] = None,
    loading: typing.Union[str, bool] = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: typing.Union[str, float] = None,
    placeholder: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.OtpInput, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_OtpInput)
def OtpInput(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.OtpInput
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _OtpInput


def _Overlay(
    absolute: bool = None,
    activator: str = None,
    activator_props: dict = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disabled: bool = None,
    eager: bool = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
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
    active_color: str = None,
    aria_label: str = None,
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    current_page_aria_label: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    ellipsis: str = None,
    first_aria_label: str = None,
    first_icon: typing.Union[str, list] = None,
    last_aria_label: str = None,
    last_icon: typing.Union[str, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: typing.Union[str, float] = None,
    model_value: float = None,
    next_aria_label: str = None,
    next_icon: typing.Union[str, list] = None,
    page_aria_label: str = None,
    prev_icon: typing.Union[str, list] = None,
    previous_aria_label: str = None,
    rounded: typing.Union[str, float, bool] = None,
    show_first_last_page: bool = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    start: typing.Union[str, float] = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    total_visible: typing.Union[str, float] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    scale: typing.Union[str, float] = None,
    slot: str = None,
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
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    landscape: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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


def _PickerTitle(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.PickerTitle, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_PickerTitle)
def PickerTitle(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.PickerTitle
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _PickerTitle


def _ProgressCircular(
    attributes: dict = {},
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    indeterminate: typing.Union[bool, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: typing.Union[str, float] = None,
    rotate: typing.Union[str, float] = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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
    bg_color: str = None,
    bg_opacity: typing.Union[str, float] = None,
    buffer_value: typing.Union[str, float] = None,
    children: list = [],
    class_: str = None,
    clickable: bool = None,
    color: str = None,
    height: typing.Union[str, float] = None,
    indeterminate: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    max: typing.Union[str, float] = None,
    model_value: typing.Union[str, float] = None,
    reverse: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    rounded_bar: bool = None,
    slot: str = None,
    stream: bool = None,
    striped: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    false_icon: typing.Union[str, list] = None,
    false_value: Any = None,
    id: str = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    readonly: bool = None,
    ripple: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: typing.Union[str, list] = None,
    true_value: Any = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    value_comparator: str = None,
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
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    false_icon: typing.Union[str, list] = None,
    focused: bool = None,
    height: typing.Union[str, float] = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_errors: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    ripple: bool = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: typing.Union[str, list] = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    value_comparator: str = None,
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
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    max_errors: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min: typing.Union[str, float] = None,
    model_value: list = [],
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    reverse: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    show_ticks: typing.Union[bool, str] = None,
    slot: str = None,
    step: typing.Union[str, float] = None,
    strict: bool = None,
    style_: str = None,
    tabbable: bool = None,
    thumb_color: str = None,
    thumb_label: typing.Union[bool, str] = None,
    thumb_size: typing.Union[str, float] = None,
    tick_size: typing.Union[str, float] = None,
    ticks: list = [],
    tooltip: str = None,
    track_color: str = None,
    track_fill_color: str = None,
    track_size: typing.Union[str, float] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
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
    active_color: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    clearable: bool = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    empty_icon: typing.Union[str, list] = None,
    full_icon: typing.Union[str, list] = None,
    half_increments: bool = None,
    hover: bool = None,
    item_aria_label: str = None,
    item_label_position: str = None,
    item_labels: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: typing.Union[str, float] = None,
    model_value: typing.Union[str, float] = None,
    name: str = None,
    readonly: bool = None,
    ripple: bool = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    content_class: str = None,
    height: typing.Union[str, float] = None,
    inline: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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
    align_content_xxl: str = None,
    align_lg: str = None,
    align_md: str = None,
    align_sm: str = None,
    align_xl: str = None,
    align_xxl: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    dense: bool = None,
    justify: str = None,
    justify_lg: str = None,
    justify_md: str = None,
    justify_sm: str = None,
    justify_xl: str = None,
    justify_xxl: str = None,
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
    disabled: bool = None,
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
    disabled: bool = None,
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
    disabled: bool = None,
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
    disabled: bool = None,
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
    disabled: bool = None,
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
    active: bool = None,
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: typing.Union[str, list] = None,
    clearable: bool = None,
    closable_chips: bool = None,
    close_text: str = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    flat: bool = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hint: str = None,
    id: str = None,
    item_children: str = None,
    item_color: str = None,
    item_props: str = None,
    item_title: str = None,
    item_value: str = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    menu: bool = None,
    menu_icon: typing.Union[str, list] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    no_data_text: str = None,
    open_on_clear: bool = None,
    open_text: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: typing.Union[str, list] = None,
    prepend_inner_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    return_object: bool = None,
    reverse: bool = None,
    role: str = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    suffix: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, dict] = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    value_comparator: str = None,
    variant: str = None,
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


def _SelectionControl(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    false_icon: typing.Union[str, list] = None,
    false_value: Any = None,
    id: str = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    multiple: bool = None,
    name: str = None,
    readonly: bool = None,
    ripple: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: typing.Union[str, list] = None,
    true_value: Any = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    value_comparator: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SelectionControl, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SelectionControl)
def SelectionControl(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SelectionControl
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SelectionControl


def _SelectionControlGroup(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    false_icon: typing.Union[str, list] = None,
    id: str = None,
    inline: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    readonly: bool = None,
    ripple: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: typing.Union[str, list] = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SelectionControlGroup, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SelectionControlGroup)
def SelectionControlGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SelectionControlGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SelectionControlGroup


def _Sheet(
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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


def _SkeletonLoader(
    attributes: dict = {},
    boilerplate: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: bool = None,
    loading_text: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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
    attributes: dict = {},
    center_active: bool = None,
    children: list = [],
    class_: str = None,
    direction: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    model_value: Any = None,
    multiple: bool = None,
    next_icon: typing.Union[str, list] = None,
    prev_icon: typing.Union[str, list] = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slot: str = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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


def _SlideGroupItem(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideGroupItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SlideGroupItem)
def SlideGroupItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SlideGroupItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SlideGroupItem


def _SlideXReverseTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
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
    disabled: bool = None,
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
    disabled: bool = None,
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
    disabled: bool = None,
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
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    max_errors: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min: typing.Union[str, float] = None,
    model_value: typing.Union[str, float] = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    reverse: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    show_ticks: typing.Union[bool, str] = None,
    slot: str = None,
    step: typing.Union[str, float] = None,
    style_: str = None,
    tabbable: bool = None,
    thumb_color: str = None,
    thumb_label: typing.Union[bool, str] = None,
    thumb_size: typing.Union[str, float] = None,
    tick_size: typing.Union[str, float] = None,
    ticks: list = [],
    tooltip: str = None,
    track_color: str = None,
    track_fill_color: str = None,
    track_size: typing.Union[str, float] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
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
    activator: str = None,
    activator_props: dict = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    color: str = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disabled: bool = None,
    eager: bool = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    multi_line: bool = None,
    offset: typing.Union[str, float, list] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    timeout: typing.Union[str, float] = None,
    tooltip: str = None,
    transition: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    vertical: bool = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
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
    tag: str = None,
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


def _Stepper(
    alt_labels: bool = None,
    attributes: dict = {},
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    editable: bool = None,
    elevation: typing.Union[str, float] = None,
    flat: bool = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    item_title: str = None,
    item_value: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    mobile: bool = None,
    model_value: Any = None,
    multiple: bool = None,
    next_text: str = None,
    non_linear: bool = None,
    position: str = None,
    prev_text: str = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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


def _StepperActions(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: typing.Union[bool, str, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    next_text: str = None,
    prev_text: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperActions, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperActions)
def StepperActions(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperActions
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperActions


def _StepperHeader(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
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


def _StepperItem(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    complete: bool = None,
    complete_icon: str = None,
    disabled: bool = None,
    edit_icon: str = None,
    editable: bool = None,
    error: bool = None,
    error_icon: str = None,
    icon: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    ripple: typing.Union[bool, dict] = None,
    rules: list = [],
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    subtitle: str = None,
    tabbable: bool = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperItem)
def StepperItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperItem


def _StepperWindow(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    continuous: bool = None,
    direction: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    model_value: Any = None,
    next_icon: typing.Union[str, list] = None,
    prev_icon: typing.Union[str, list] = None,
    reverse: bool = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    touch: Any = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperWindow, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperWindow)
def StepperWindow(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperWindow
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperWindow


def _StepperWindowItem(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    eager: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    reverse_transition: typing.Union[str, bool] = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperWindowItem, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperWindowItem)
def StepperWindowItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperWindowItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperWindowItem


def _SvgIcon(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    icon: typing.Union[str, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SvgIcon, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_SvgIcon)
def SvgIcon(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SvgIcon
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SvgIcon


def _Switch(
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    false_icon: typing.Union[str, list] = None,
    false_value: Any = None,
    flat: bool = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    indeterminate: bool = None,
    inline: bool = None,
    inset: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    ripple: bool = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: typing.Union[str, list] = None,
    true_value: Any = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    value: Any = None,
    value_comparator: str = None,
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    name: str = None,
    order: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
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
    append_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    fixed: bool = None,
    height: typing.Union[str, float] = None,
    hide_slider: bool = None,
    href: str = None,
    icon: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    prepend_icon: typing.Union[str, list] = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slider_color: str = None,
    slot: str = None,
    stacked: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
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


def _Table(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    density: str = None,
    fixed_footer: bool = None,
    fixed_header: bool = None,
    height: typing.Union[str, float] = None,
    hover: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Table, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Table)
def Table(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Table
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Table


def _Tabs(
    align_tabs: str = None,
    attributes: dict = {},
    bg_color: str = None,
    center_active: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    fixed_tabs: bool = None,
    grow: bool = None,
    height: typing.Union[str, float] = None,
    hide_slider: bool = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    model_value: Any = None,
    multiple: bool = None,
    next_icon: typing.Union[str, list] = None,
    prev_icon: typing.Union[str, list] = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slider_color: str = None,
    slot: str = None,
    stacked: bool = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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


def _TextField(
    active: bool = None,
    append_icon: typing.Union[str, list] = None,
    append_inner_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: typing.Union[str, list] = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    density: str = None,
    direction: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    flat: bool = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    name: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: typing.Union[str, list] = None,
    prepend_inner_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    reverse: bool = None,
    role: str = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    suffix: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    type: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
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
    active: bool = None,
    append_icon: typing.Union[str, list] = None,
    append_inner_icon: typing.Union[str, list] = None,
    attributes: dict = {},
    auto_grow: bool = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: typing.Union[str, list] = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: str = None,
    density: str = None,
    direction: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    flat: bool = None,
    focused: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hint: str = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_rows: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    model_value: Any = None,
    name: str = None,
    no_resize: bool = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: typing.Union[str, list] = None,
    prepend_inner_icon: typing.Union[str, list] = None,
    readonly: bool = None,
    reverse: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    rows: typing.Union[str, float] = None,
    rules: list = [],
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    suffix: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
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
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    with_background: bool = None,
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


def _Timeline(
    align: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    density: str = None,
    direction: str = None,
    justify: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    line_color: str = None,
    line_inset: typing.Union[str, float] = None,
    line_thickness: typing.Union[str, float] = None,
    side: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    truncate_line: str = None,
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
    density: str = None,
    dot_color: str = None,
    elevation: typing.Union[str, float] = None,
    fill_dot: bool = None,
    height: typing.Union[str, float] = None,
    hide_dot: bool = None,
    hide_opposite: bool = None,
    icon: typing.Union[str, list] = None,
    icon_color: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    line_inset: typing.Union[str, float] = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
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
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    collapse: bool = None,
    color: str = None,
    density: str = None,
    elevation: typing.Union[str, float] = None,
    extended: bool = None,
    extension_height: typing.Union[str, float] = None,
    flat: bool = None,
    floating: bool = None,
    height: typing.Union[str, float] = None,
    image: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    title: str = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    color: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
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
    tag: str = None,
    text: str = None,
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
    activator: str = None,
    activator_props: dict = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disabled: bool = None,
    eager: bool = None,
    height: typing.Union[str, float] = None,
    id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
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


def _Validation(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    focused: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_errors: typing.Union[str, float] = None,
    model_value: Any = None,
    name: str = None,
    readonly: bool = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Validation, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_Validation)
def Validation(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Validation
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Validation


def _VirtualScroll(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    height: typing.Union[str, float] = None,
    item_height: typing.Union[str, float] = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    renderless: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.VirtualScroll, Any]:
    """
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_VirtualScroll)
def VirtualScroll(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.VirtualScroll
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _VirtualScroll


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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    continuous: bool = None,
    direction: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    model_value: Any = None,
    next_icon: typing.Union[str, list] = None,
    prev_icon: typing.Union[str, list] = None,
    reverse: bool = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: str = None,
    theme: str = None,
    tooltip: str = None,
    touch: Any = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
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
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    eager: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    reverse_transition: typing.Union[str, bool] = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
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
