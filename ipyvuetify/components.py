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
        def get_ignore_props(self, cls):
            unavailable = [name for name, trait in cls.class_traits().items() if trait.__class__.__name__ == "TraitNotAvailable"]
            return [*super().get_ignore_props(cls), *unavailable]

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
    close_icon: Any = None,
    close_label: str = None,
    color: str = None,
    density: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    icon: Any = None,
    icon_size: typing.Union[str, float] = None,
    icon_sizes: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
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
    tag: Any = None,
    text: str = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Alert, Any]:
    """Widget for the Vuetify v-alert component, see https://vuetifyjs.com/en/api/v-alert/
    :param border: Adds a colored border to the component.
    :param border_color: Specifies the color of the border. Only used in combination with **border** prop. Accepts any color value.
    :param closable: Adds a close icon that can hide the alert.
    :param close_icon: Change the default icon used for **closable** alerts.
    :param close_label: Text used for *aria-label* on **closable** alerts. Can also be customized globally in [Internationalization](https://vuetifyjs.com/en/customization/internationalization).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param height: Sets the height for the component.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param icon_size: The specific size of the icon, can use named sizes.
    :param icon_sizes: An array of tuples that define the icon sizes for each named size.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: Controls whether the component is visible or hidden.
    :param position: Sets the position for the component.
    :param prominent: Displays a larger vertically centered icon to draw more attention.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes the component's border-radius.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param type: Create a specialized alert that uses a contextual color and has a pre-defined icon.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AlertTitle, Any]:
    """Widget for the Vuetify v-alert-title component, see https://vuetifyjs.com/en/api/v-alert-title/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    overlaps: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.App, Any]:
    """Widget for the Vuetify v-app component, see https://vuetifyjs.com/en/api/v-app/
    :param overlaps: **FOR INTERNAL USE ONLY**
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
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
    collapse_position: str = None,
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
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AppBar, Any]:
    """Widget for the Vuetify v-app-bar component, see https://vuetifyjs.com/en/api/v-app-bar/
    :param absolute: Applies position: absolute to the component.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param collapse: Morphs the component into a collapsed state, reducing its maximum width.
    :param collapse_position: Specifies side to attach the collapsed toolbar.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param extended: Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop. When false, will not show extension slot even if content is present.
    :param extension_height: Designate an explicit height for the `extension` slot.
    :param flat: Removes the component's **box-shadow**.
    :param floating: Applies **display: inline-flex** to the component.
    :param height: Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.
    :param image: Specifies a [v-img](https://vuetifyjs.com/en/components/images) as the component's background.
    :param location: Aligns the component towards the top or bottom.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Assign a specific name for layout registration.
    :param order: Adjust the order of the component in relation to its registration order.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param scroll_behavior: Specify an action to take when the scroll position of **scroll-target** reaches **scroll-threshold**. Accepts any combination of hide, inverted, collapse, elevate, and fade-image. Multiple values can be used, separated by a space.
    :param scroll_target: The element to target for scrolling events. Uses `window` by default.
    :param scroll_threshold: The amount of scroll distance down before **scroll-behavior** activates.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
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
    active_color: str = None,
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
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
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slim: bool = None,
    slot: str = None,
    stacked: bool = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: Any = None,
    text: typing.Union[str, float, bool] = None,
    theme: str = None,
    tile: bool = None,
    to: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AppBarNavIcon, Any]:
    """Widget for the Vuetify v-app-bar-nav-icon component, see https://vuetifyjs.com/en/api/v-app-bar-nav-icon/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param active_color: The applied color when the component is in an active state.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param block: Expands the button to 100% of available space.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param flat: Removes the button box shadow. This is different than using the 'flat' variant.
    :param height: Sets the height for the component.
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component. The button will become _round_.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param position: Sets the position for the component.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param slim: Reduces padding to 0 8px.
    :param stacked: Displays the button as a flex-column.
    :param symbol: The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    tag: Any = None,
    text: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AppBarTitle, Any]:
    """Widget for the Vuetify v-app-bar-title component, see https://vuetifyjs.com/en/api/v-app-bar-title/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
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
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    auto_select_first: typing.Union[bool, str] = None,
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: Any = None,
    clear_on_select: bool = None,
    clearable: bool = None,
    closable_chips: bool = None,
    close_text: str = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    custom_filter: Any = None,
    custom_key_filter: Any = None,
    density: str = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    item_children: str = None,
    item_color: str = None,
    item_props: str = None,
    item_title: str = None,
    item_type: str = None,
    item_value: str = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    list_props: Any = None,
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    menu: bool = None,
    menu_icon: Any = None,
    menu_props: Any = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_modifiers: Any = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    no_auto_scroll: bool = None,
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
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
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
    tile: bool = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    value_comparator: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Autocomplete, Any]:
    """Widget for the Vuetify v-autocomplete component, see https://vuetifyjs.com/en/api/v-autocomplete/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param auto_select_first: When searching, will always highlight the first option and select it on blur. `exact` will only highlight and select exact matches.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: Enables autofocus.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param chips: Changes display of selections to chips.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clear_on_select: Reset the search text when a selection is made while using the **multiple** prop.
    :param clearable: Allows for the component to be cleared.
    :param closable_chips: Enables the [closable](https://vuetifyjs.com/en/api/v-chip/#props-closable) prop on all [v-chip](https://vuetifyjs.com/en/components/chips/) components.
    :param close_text: Text set to the inputs `aria-label` and `title` when input menu is closed.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Function returns the counter display text.
    :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
    :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the input.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param filter_keys: Array of specific keys to filter on the item.
    :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :param hide_selected: Do not display in the select menu items that are already selected.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-autocomplete/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param item_children: This property currently has **no effect**.
    :param item_color: Sets color of selected items.
    :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
    :param item_title: Property on supplied `items` that contains its title.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: Can be an array of objects or strings. By default objects should have **title** and **value** properties, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props). Keys to use for these can be changed with the **item-title**, **item-value**, and **item-props** props.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param list_props: Pass props through to the `v-list` component. Accepts an object with anything from [v-list](https://vuetifyjs.com/en/api/v-list/#props) props, camelCase keys are recommended.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param menu: Renders with the menu open by default.
    :param menu_icon: Sets the the spin icon.
    :param menu_props: Pass props through to the `v-menu` component. Accepts an object with anything from [v-menu](https://vuetifyjs.com/en/api/v-menu/#props) props, camelCase keys are recommended.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes select to multiple. Accepts array for value.
    :param name: Sets the component's name attribute.
    :param no_data_text: Text shown when no items are provided to the component.
    :param no_filter: Do not apply filtering when searching. Useful when data is being filtered server side.
    :param open_on_clear: Open's the menu whenever the clear icon is clicked.
    :param open_text: Text set to the inputs **aria-label** and **title** when input menu is open.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-autocomplete/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param placeholder: Sets the input’s placeholder text.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param readonly: Puts input in readonly state.
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param reverse: Reverses the orientation.
    :param role: The role attribute applied to the input.
    :param rounded: Adds a border radius to the input.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param search: Text input used to filter items.
    :param single_line: Label does not move on focus/dirty.
    :param suffix: Displays suffix text.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param type: Sets input type.
    :param validate_on: Change what type of event triggers validation to run.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    end: bool = None,
    icon: Any = None,
    image: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rounded: typing.Union[str, float, bool] = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    start: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: str = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Avatar, Any]:
    """Widget for the Vuetify v-avatar component, see https://vuetifyjs.com/en/api/v-avatar/
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param end: Applies margin at the start of the component.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param image: Apply a specific image using [v-img](https://vuetifyjs.com/en/components/images/).
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param start: Applies margin at the end of the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
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


def _AvatarGroup(
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    gap: typing.Union[str, float] = None,
    hoverable: bool = None,
    item_props: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    limit: typing.Union[str, float] = None,
    overflow_text: str = None,
    reverse: bool = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.AvatarGroup, Any]:
    """Widget for the Vuetify v-avatar-group component, see https://vuetifyjs.com/en/api/v-avatar-group/
    :param border: Applies border styles to the child [v-avatar](https://vuetifyjs.com/en/components/avatars) components.
    :param gap: Sets the overlap gap between avatars. Negative values cause avatars to overlap.
    :param hoverable: Enables a hover animation on child avatars.
    :param items: An array of strings or objects used for automatically generating children components.
    :param limit: The total number of avatars to display, including the overflow indicator. E.g. a limit of `3` with 5 items renders 2 avatars and a `+3` overflow indicator.
    :param overflow_text: Custom text to display in the overflow avatar. Defaults to `+N` where N is the number of hidden items.
    :param reverse: Reverses the stacking order of the avatars.
    :param size: Sets the size of all child avatars.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tooltip: A tooltip caption.
    :param vertical: Stacks avatars vertically instead of horizontally.
    """
    ...


@implements(_AvatarGroup)
def AvatarGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.AvatarGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _AvatarGroup


def _Badge(
    attributes: dict = {},
    bordered: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    content: typing.Union[str, float] = None,
    dot: bool = None,
    floating: bool = None,
    height: typing.Union[str, float] = None,
    icon: Any = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    max: typing.Union[str, float] = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    offset_x: typing.Union[str, float] = None,
    offset_y: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text_color: str = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Badge, Any]:
    """Widget for the Vuetify v-badge component, see https://vuetifyjs.com/en/api/v-badge/
    :param bordered: Applies a **2px** by default and **1.5px** border around the badge when using the **dot** property.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param content: Text content to show in the badge.
    :param dot: Reduce the size of the badge and hide its contents.
    :param floating: Move the badge further away from the slotted content. Equivalent to an 8px offset.
    :param height: Sets the height for the component.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param inline: Display as an inline block instead of absolute position. **location**, **floating**, and **offset** will have no effect.
    :param label: The **aria-label** used for the badge.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max: Sets the maximum number allowed when using the **content** prop with a `number` like value. If the content number exceeds the maximum value, a `+` suffix is added.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: Controls whether the component is visible or hidden.
    :param offset_x: Offset the badge on the x-axis.
    :param offset_y: Offset the badge on the y-axis.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text_color: Applies a specified color to the control text - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param width: Sets the width for the component.
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
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: str = None,
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    stacked: bool = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: str = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Banner, Any]:
    """Widget for the Vuetify v-banner component, see https://vuetifyjs.com/en/api/v-banner/
    :param avatar: Designates a specific src image to pass to the thumbnail.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param height: Sets the height for the component.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param lines: The amount of visible lines of text before it truncates.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param mobile: Applies the mobile banner styles.
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param position: Sets the position for the component.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param stacked: Forces the banner actions onto a new line. This is not applicable when the banner has `lines="one"`.
    :param sticky: Applies `position: sticky` to the component with `top: 0`. You can find more information on the [MDN documentation for sticky position](https://developer.mozilla.org/en-US/docs/Web/CSS/position).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BannerActions, Any]:
    """Widget for the Vuetify v-banner-actions component, see https://vuetifyjs.com/en/api/v-banner-actions/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BannerText, Any]:
    """Widget for the Vuetify v-banner-text component, see https://vuetifyjs.com/en/api/v-banner-text/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    base_color: str = None,
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
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BottomNavigation, Any]:
    """Widget for the Vuetify v-bottom-navigation component, see https://vuetifyjs.com/en/api/v-bottom-navigation/
    :param absolute: Applies **position: absolute** to the component.
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param base_color: Sets the color of component when not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Puts all children components into a disabled state.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param grow: Force all [v-btn](https://vuetifyjs.com/en/components/buttons) children to take up all available horizontal space.
    :param height: Sets the height for the component.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param mode: Changes the orientation and active state styling of the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows one to select multiple items.
    :param name: Assign a specific name for layout registration.
    :param order: Adjust the order of the component in relation to its registration order.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
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
    activator_props: Any = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    capture_focus: bool = None,
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
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
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
    stick_to_target: bool = None,
    style_: str = None,
    tabbable: bool = None,
    target: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    viewport_margin: typing.Union[str, float] = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BottomSheet, Any]:
    """Widget for the Vuetify v-bottom-sheet component, see https://vuetifyjs.com/en/api/v-bottom-sheet/
    :param absolute: Applies **position: absolute** to the content element.
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Closes component when you click on its content.
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param fullscreen: Changes layout for fullscreen display.
    :param height: Sets the height for the component.
    :param inset: Reduces the sheet content maximum width to 70%.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :param open_on_click: Activate the component when the activator is clicked.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Activate the component when the activator is hovered.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :param retain_focus: Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.
    :param scrim: Accepts true/false to enable background, and string to define color.
    :param scroll_strategy: Strategy used when the component is activate and user scrolls.
    :param scrollable: When set to true, expects a `v-card` and a `v-card-text` component with a designated height. For more information, check out the [scrollable example](https://vuetifyjs.com/en/components/dialogs#scrollable).
    :param stick_to_target: Enables the overlay content to go off-screen when scrolling.
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param viewport_margin: Sets custom viewport margin for the overlay content
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
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
    icon: Any = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Breadcrumbs, Any]:
    """Widget for the Vuetify v-breadcrumbs component, see https://vuetifyjs.com/en/api/v-breadcrumbs/
    :param active_class: The class applied to the component when it is in an active state.
    :param active_color: The applied color when the component is in an active state.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param divider: Specifies the dividing character between items.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param items: An array of strings or objects used for automatically generating children components.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tile: Removes any applied **border-radius** from the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BreadcrumbsDivider, Any]:
    """Widget for the Vuetify v-breadcrumbs-divider component, see https://vuetifyjs.com/en/api/v-breadcrumbs-divider/
    :param divider: Specifies the dividing character between items.
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
    max_width: typing.Union[str, float] = None,
    replace: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    title: str = None,
    to: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BreadcrumbsItem, Any]:
    """Widget for the Vuetify v-breadcrumbs-item component, see https://vuetifyjs.com/en/api/v-breadcrumbs-item/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param active_class: The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.
    :param active_color: The applied color when the component is in an active state.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param max_width: Sets the maximum width for the component.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param title: Specify a title text for the component.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    active_color: str = None,
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
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
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slim: bool = None,
    slot: str = None,
    spaced: str = None,
    stacked: bool = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: Any = None,
    text: typing.Union[str, float, bool] = None,
    theme: str = None,
    tile: bool = None,
    to: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Btn, Any]:
    """Widget for the Vuetify v-btn component, see https://vuetifyjs.com/en/api/v-btn/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param active_color: The applied color when the component is in an active state.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param block: Expands the button to 100% of available space.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param flat: Removes the button box shadow. This is different than using the 'flat' variant.
    :param height: Sets the height for the component.
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component. The button will become _round_.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param position: Sets the position for the component.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param slim: Reduces padding to 0 8px.
    :param spaced: Extends content to the edges to move main content from prepend and append slots.
    :param stacked: Displays the button as a flex-column.
    :param symbol: The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    base_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    direction: str = None,
    divided: bool = None,
    elevation: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BtnGroup, Any]:
    """Widget for the Vuetify v-btn-group component, see https://vuetifyjs.com/en/api/v-btn-group/
    :param base_color: Sets the color of component when not focused.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param divided: Add dividers between children [v-btn](https://vuetifyjs.com/en/components/buttons) components.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
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
    base_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    direction: str = None,
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
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.BtnToggle, Any]:
    """Widget for the Vuetify v-btn-toggle component, see https://vuetifyjs.com/en/api/v-btn-toggle/
    :param base_color: Sets the color of component when not focused.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Puts all children components into a disabled state.
    :param divided: Add dividers between children [v-btn](https://vuetifyjs.com/en/components/buttons) components.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows one to select multiple items.
    :param rounded: Round edge buttons.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes the component's border-radius.
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
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
    categories: typing.Union[str, list] = None,
    category_days: typing.Union[str, float] = None,
    category_for_invalid: str = None,
    category_hide_dynamic: bool = None,
    category_show_all: bool = None,
    category_text: str = None,
    children: list = [],
    class_: str = None,
    day_format: Any = None,
    end: typing.Union[str, float] = None,
    event_category: str = None,
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
    event_timed: str = None,
    events: list = [],
    first_day_of_week: typing.Union[str, float] = None,
    first_day_of_year: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    locale: str = None,
    max_days: float = None,
    model_value: typing.Union[str, float] = None,
    now: str = None,
    slot: str = None,
    start: typing.Union[str, float] = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    weekday_format: Any = None,
    weekdays: typing.Union[str, list] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Calendar, Any]:
    """Widget for the Vuetify v-calendar component, see https://vuetifyjs.com/en/api/v-calendar/
    :param categories: Specifies what categories to display in the `category` view. This controls the order of the categories as well. If the calendar uses events any categories specified in those events not specified in this value are dynamically rendered in the view unless `category-hide-dynamic` is true.
    :param category_days: The number of days to render in the `category` view.
    :param category_for_invalid: The category to place events in that have invalid categories. A category is invalid when it is not a string. By default events without a category are not displayed until this value is specified.
    :param category_hide_dynamic: Sets whether categories specified in an event should be hidden if it's not defined in `categories`.
    :param category_show_all: Set whether the `category` view should show all defined `categories` even if there are no events for a category.
    :param category_text: If categories is a list of objects, you can use this to determine what property to print out as the category text on the calendar. You can provide a function to do some logic or just define the prop name. It's similar to item-text on v-select
    :param day_format: Formats day of the month string that appears in a day to a specified locale
    :param end: The ending date on the calendar (inclusive) in the format of `YYYY-MM-DD`. This may be ignored depending on the `type` of the calendar.
    :param event_category: Set property of *event*'s category. Instead of a property a function can be given which takes an event and returns the category.
    :param event_color: A background color for all events or a function which accepts an event object passed to the calendar to return a color.
    :param event_end: Set property of *event*'s end timestamp.
    :param event_height: The height of an event in pixels in the `month` view and at the top of the `day` views.
    :param event_margin_bottom: Margin bottom for event
    :param event_more: Whether the more 'button' is displayed on a calendar with too many events in a given day. It will say something like '5 more' and when clicked generates a `click:more` event.
    :param event_more_text: The text to display in the more 'button' given the number of hidden events.
    :param event_name: Set property of *event*'s displayed name, or a function which accepts an event object passed to the calendar as the first argument and a flag signalling whether the name is for a timed event (true) or an event over a day.
    :param event_overlap_mode: One of `stack`, `column`, or a custom render function
    :param event_overlap_threshold: A value in minutes that's used to determine whether two timed events should be placed in column beside each other or should be treated as slightly overlapping events.
    :param event_ripple: Applies the `v-ripple` directive.
    :param event_start: Set property of *event*'s start timestamp.
    :param event_text_color: A text color for all events or a function which accepts an event object passed to the calendar to return a color.
    :param event_timed: If Dates or milliseconds are used as the start or end timestamp of an event, this prop can be a string to a property on the event that is truthy if the event is a timed event or a function which takes the event and returns a truthy value if the event is a timed event.
    :param events: An array of event objects with a property for a start timestamp and optionally a name and end timestamp. If an end timestamp is not given, the value of start will be used. If no name is given, you must provide an implementation for the `event` slot.
    :param first_day_of_week: Sets the first day of the week, starting with 0 for Sunday. (Note: not guaranteed to work when using custom date adapters.)
    :param first_day_of_year: Sets the day that determines the first week of the year, starting with 0 for Sunday. For ISO 8601 this should be 4. (Note: not guaranteed to work when using custom date adapters.)
    :param locale: The locale of the calendar.
    :param max_days: The maximum number of days to display in the custom calendar if an `end` day is not set.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param now: Override the day & time which is considered now. This is in the format of `YYYY-MM-DD hh:mm:ss`. The calendar is styled according to now.
    :param start: The starting date on the calendar (inclusive) in the format of `YYYY-MM-DD`. This may be ignored depending on the `type` of the calendar.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param type: A string which is one of `month`, `week`, `day`, `4day`, `custom-weekly`, `custom-daily`, and `category`. The custom types look at the `start` and `end` dates passed to the component as opposed to the `value`.
    :param weekday_format: Formats day of the week string that appears in the header to specified locale
    :param weekdays: An array of weekdays to display. Does not affect the order.
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


def _Card(
    append_avatar: str = None,
    append_icon: Any = None,
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
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    prepend_avatar: str = None,
    prepend_icon: Any = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    subtitle: typing.Union[str, float, bool] = None,
    tabbable: bool = None,
    tag: Any = None,
    text: typing.Union[str, float, bool] = None,
    theme: str = None,
    tile: bool = None,
    title: typing.Union[str, float, bool] = None,
    to: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Card, Any]:
    """Widget for the Vuetify v-card component, see https://vuetifyjs.com/en/api/v-card/
    :param append_avatar: Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param flat: Removes the card's elevation.
    :param height: Sets the height for the component.
    :param hover: Applies **4dp** of elevation when hovered (default 2dp). You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param image: Apply a specific background image to the component.
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param position: Sets the position for the component.
    :param prepend_avatar: Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.
    :param prepend_icon: Prepends a [v-icon](https://vuetifyjs.com/en/components/icons/) component to the header.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardActions, Any]:
    """Widget for the Vuetify v-card-actions component, see https://vuetifyjs.com/en/api/v-card-actions/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    append_icon: Any = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    density: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    prepend_avatar: str = None,
    prepend_icon: Any = None,
    slot: str = None,
    style_: str = None,
    subtitle: typing.Union[str, float, bool] = None,
    tabbable: bool = None,
    tag: Any = None,
    title: typing.Union[str, float, bool] = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardItem, Any]:
    """Widget for the Vuetify v-card-item component, see https://vuetifyjs.com/en/api/v-card-item/
    :param append_avatar: Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param density: Adjusts the vertical height used by the component.
    :param prepend_avatar: Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param title: Specify a title text for the component.
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
    opacity: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardSubtitle, Any]:
    """Widget for the Vuetify v-card-subtitle component, see https://vuetifyjs.com/en/api/v-card-subtitle/
    :param opacity: Sets the component's opacity value
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    opacity: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardText, Any]:
    """Widget for the Vuetify v-card-text component, see https://vuetifyjs.com/en/api/v-card-text/
    :param opacity: Sets the component's opacity value
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CardTitle, Any]:
    """Widget for the Vuetify v-card-title component, see https://vuetifyjs.com/en/api/v-card-title/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    crossfade: bool = None,
    cycle: bool = None,
    delimiter_icon: Any = None,
    direction: str = None,
    disabled: bool = None,
    height: typing.Union[str, float] = None,
    hide_delimiter_background: bool = None,
    hide_delimiters: bool = None,
    interval: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    model_value: Any = None,
    next_icon: Any = None,
    prev_icon: Any = None,
    progress: typing.Union[str, bool] = None,
    reverse: bool = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    touch: bool = None,
    transition_duration: float = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    vertical_arrows: typing.Union[bool, str, str] = None,
    vertical_delimiters: typing.Union[bool, str, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Carousel, Any]:
    """Widget for the Vuetify v-carousel component, see https://vuetifyjs.com/en/api/v-carousel/
    :param color: Applies a color to the navigation dots - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param continuous: Determines whether carousel is continuous.
    :param crossfade: Enables crossfade transition.
    :param cycle: Determines if the carousel should cycle through images.
    :param delimiter_icon: Sets icon for carousel delimiter.
    :param direction: The transition direction when changing windows.
    :param disabled: Removes the ability to click or target the component.
    :param height: Sets the height for the component.
    :param hide_delimiter_background: Hides the bottom delimiter background.
    :param hide_delimiters: Hides the carousel's bottom delimiters.
    :param interval: The duration between image cycles. Requires the **cycle** prop.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param next_icon: The displayed icon for forcing pagination to the next item.
    :param prev_icon: The displayed icon for forcing pagination to the previous item.
    :param progress: Displays a carousel progress bar. Requires the **cycle** prop and **interval**.
    :param reverse: Reverse the normal transition direction.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param show_arrows: Displays arrows for next/previous navigation.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param touch: Provide a custom **left** and **right** function when swiped left or right.
    :param transition_duration: Overrides transition duration. Does not work in firefox, safari <18, or with `prefers-reduced-motion: reduce`.
    :param vertical_delimiters: Displays carousel delimiters vertically.
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
    absolute: bool = None,
    alt: str = None,
    aspect_ratio: typing.Union[str, float] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    content_class: Any = None,
    cover: bool = None,
    crossorigin: str = None,
    disabled: bool = None,
    draggable: typing.Union[bool, str, str] = None,
    eager: bool = None,
    gradient: str = None,
    height: typing.Union[str, float] = None,
    image_class: Any = None,
    inline: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lazy_src: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    options: Any = None,
    position: str = None,
    referrerpolicy: str = None,
    reverse_transition: typing.Union[str, bool] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    sizes: str = None,
    slot: str = None,
    src: typing.Union[str, dict] = None,
    srcset: str = None,
    style_: str = None,
    tabbable: bool = None,
    tile: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CarouselItem, Any]:
    """Widget for the Vuetify v-carousel-item component, see https://vuetifyjs.com/en/api/v-carousel-item/
    :param absolute: Applies position: absolute to the component.
    :param alt: Alternate text for screen readers. Leave empty for decorative images.
    :param aspect_ratio: Calculated as `width/height`, so for a 1920x1080px image this will be `1.7778`. Will be calculated automatically if omitted.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param content_class: Apply a custom class to the internal content element.
    :param cover: Resizes the background image to cover the entire container.
    :param crossorigin: Specify that images should be fetched with CORS enabled [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#crossorigin)
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.
    :param draggable: Controls the `draggable` behavior of the image. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable).
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param gradient: The gradient to apply to the image. Only supports [linear-gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient) syntax, anything else should be done with classes.
    :param height: Sets the height for the component.
    :param image_class: Applies CSS classes to the inner `<img>` element.
    :param inline: Display as an inline element instead of a block, also disables flex-grow.
    :param lazy_src: Something to show while waiting for the main image to load, typically a small base64-encoded thumbnail. Has a slight blur filter applied.
    NOTE: This prop has no effect unless either `height` or `aspect-ratio` are provided.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param options: Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) constructor.
    :param position: Applies [object-position](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position) styles to the image and placeholder elements.
    :param referrerpolicy: Define which referrer is sent when fetching the resource [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#referrerpolicy)
    :param reverse_transition: Sets the reverse transition.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param sizes: For use with `srcset`, see [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes).
    :param src: The image URL. This prop is mandatory.
    :param srcset: A set of alternate images to use based on device size. [Read more...](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset).
    :param tabbable: Is widget tabbable?
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param transition: The transition to use when switching from `lazy-src` to `src`. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param width: Sets the width for the component.
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
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    false_icon: Any = None,
    false_value: Any = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    indeterminate: bool = None,
    indeterminate_icon: Any = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: Any = None,
    true_value: Any = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    value: Any = None,
    value_comparator: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Checkbox, Any]:
    """Widget for the Vuetify v-checkbox component, see https://vuetifyjs.com/en/api/v-checkbox/
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param defaults_target: The target component to provide defaults values for.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param false_icon: The icon used when inactive.
    :param false_value: Sets value for falsy state.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the input is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-checkbox/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param indeterminate: Sets an indeterminate state for the checkbox.
    :param indeterminate_icon: The icon used when in an indeterminate state.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes expected model to an array.
    :param name: Sets the component's name attribute.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-checkbox/#props-hint) to always be visible.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param readonly: Puts input in readonly state.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param true_icon: The icon used when active.
    :param true_value: Sets value for truthy state.
    :param type: Provides the default type for children selection controls.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param width: Sets the width for the component.
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
    base_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    false_icon: Any = None,
    false_value: Any = None,
    id: str = None,
    indeterminate: bool = None,
    indeterminate_icon: Any = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: Any = None,
    true_value: Any = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    value_comparator: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CheckboxBtn, Any]:
    """Widget for the Vuetify v-checkbox-btn component, see https://vuetifyjs.com/en/api/v-checkbox-btn/
    :param base_color: Sets the color of the input when it is not focused.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param defaults_target: The target component to provide defaults values for.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param false_icon: The icon used when inactive.
    :param false_value: Sets value for falsy state.
    :param id: Sets the DOM id on the component.
    :param indeterminate: Puts the control in an indeterminate state. Used with the [indeterminate-icon](https://vuetifyjs.com/en/api/v-checkbox-btn/#props-indeterminate-icon) property.
    :param indeterminate_icon: Icon used when the component is in an indeterminate state.
    :param inline: Puts children inputs into a row.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes select to multiple. Accepts array for value.
    :param name: Sets the component's name attribute.
    :param readonly: Puts input in readonly state.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param true_icon: The icon used when active.
    :param true_value: Sets value for truthy state.
    :param type: Provides the default type for children selection controls.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
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
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    closable: bool = None,
    close_icon: Any = None,
    close_label: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    draggable: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    filter: bool = None,
    filter_icon: Any = None,
    href: str = None,
    label: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    link: bool = None,
    model_value: bool = None,
    pill: bool = None,
    prepend_avatar: str = None,
    prepend_icon: Any = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: typing.Union[str, float, bool] = None,
    theme: str = None,
    tile: bool = None,
    to: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Chip, Any]:
    """Widget for the Vuetify v-chip component, see https://vuetifyjs.com/en/api/v-chip/
    :param active_class: The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.
    :param append_avatar: Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param closable: Adds remove button and then a chip can be closed.
    :param close_icon: Change the default icon used for **close** chips.
    :param close_label: Text used for *aria-label* on the close button in **close** chips. Can also be customized globally in [Internationalization](https://vuetifyjs.com/en/customization/internationalization).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param draggable: Makes the chip draggable.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param filter: Displays a selection icon when selected.
    :param filter_icon: Change the default icon used for **filter** chips.
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param label: Applies a medium size border radius.
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param pill: Remove `v-avatar` padding.
    :param prepend_avatar: Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param size: Sets the height, padding and the font size of the component. Accepts only predefined options: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param value: The value used when a child of a [v-chip-group](https://vuetifyjs.com/en/components/chip-groups).
    :param variant: Applies a distinct style to the component.
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
    base_color: str = None,
    center_active: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    column: bool = None,
    content_class: Any = None,
    direction: str = None,
    disabled: bool = None,
    filter: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    model_value: Any = None,
    multiple: bool = None,
    next_icon: Any = None,
    prev_icon: Any = None,
    scroll_to_active: bool = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slot: str = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ChipGroup, Any]:
    """Widget for the Vuetify v-chip-group component, see https://vuetifyjs.com/en/api/v-chip-group/
    :param base_color: Sets the color of component when not focused. Recommended with `color` or `filter` to properly highlight selected items.
    :param center_active: Forces the selected chip to be centered.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param column: Remove horizontal pagination and wrap items as needed.
    :param content_class: Adds classes to the slide group item.
    :param direction: Switch between horizontal and vertical modes.
    :param disabled: Puts all children components into a disabled state.
    :param filter: Applies an checkmark icon in front of every chip for using it like a filter.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Sets the designated mobile breakpoint for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows one to select multiple items.
    :param next_icon: Specify the icon to use for the next icon.
    :param prev_icon: Specify the icon to use for the prev icon.
    :param scroll_to_active: Keeps the last active element visible when resizing the scrollable container.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param show_arrows: Force the display of the pagination arrows.
    :param symbol: The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param variant: Applies a distinct style to the component.
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
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ClassIcon, Any]:
    """Widget for the Vuetify v-class-icon component, see https://vuetifyjs.com/en/api/v-class-icon/
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Code, Any]:
    """Widget for the Vuetify v-code component, see https://vuetifyjs.com/en/api/v-code/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    xl: typing.Union[str, float, bool] = None,
    xxl: typing.Union[str, float, bool] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Col, Any]:
    """Widget for the Vuetify v-col component, see https://vuetifyjs.com/en/api/v-col/
    :param align_self: Applies the [align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) css property. Available options are: **start**, **center**, **end**, **auto**, **baseline** and **stretch**.
    :param cols: Sets the default number of columns the component extends. Available options are: **1 -> 12** and **auto**.
    :param lg: Changes the number of columns on large and greater breakpoints.
    :param md: Changes the number of columns on medium and greater breakpoints.
    :param offset: Sets the default offset for the column.
    :param offset_lg: Changes the offset of the component on large and greater breakpoints.
    :param offset_md: Changes the offset of the component on medium and greater breakpoints.
    :param offset_sm: Changes the offset of the component on small and greater breakpoints.
    :param offset_xl: Changes the offset of the component on extra large and greater breakpoints.
    :param offset_xxl: Changes the offset of the component on extra extra large and greater breakpoints.
    :param order: Sets the default [order](https://developer.mozilla.org/en-US/docs/Web/CSS/order) for the column.
    :param order_lg: Changes the order of the component on large and greater breakpoints.
    :param order_md: Changes the order of the component on medium and greater breakpoints.
    :param order_sm: Changes the order of the component on small and greater breakpoints.
    :param order_xl: Changes the order of the component on extra large and greater breakpoints.
    :param order_xxl: Changes the order of the component on extra extra large and greater breakpoints.
    :param sm: Changes the number of columns on small and greater breakpoints.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tooltip: A tooltip caption.
    :param xl: Changes the number of columns on extra large and greater breakpoints.
    :param xxl: Changes the number of columns on extra extra large and greater breakpoints.
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


def _ColorInput(
    active: bool = None,
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    cancel_text: str = None,
    canvas_height: typing.Union[str, float] = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    color: str = None,
    color_pip: bool = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    density: str = None,
    dirty: bool = None,
    disabled: bool = None,
    divided: bool = None,
    dot_size: typing.Union[str, float] = None,
    elevation: typing.Union[str, float] = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    eye_dropper_icon: Any = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_actions: bool = None,
    hide_canvas: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_eye_dropper: bool = None,
    hide_header: bool = None,
    hide_inputs: bool = None,
    hide_pip: bool = None,
    hide_sliders: bool = None,
    hide_spin_buttons: bool = None,
    hide_title: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    landscape: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    menu_props: Any = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    mode: str = None,
    model_modifiers: Any = None,
    model_value: typing.Union[str, dict] = None,
    modes: list = [],
    name: str = None,
    ok_text: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    picker_props: Any = None,
    pip_icon: str = None,
    pip_location: str = None,
    pip_variant: str = None,
    placeholder: str = None,
    position: str = None,
    prefix: str = None,
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
    readonly: bool = None,
    reverse: bool = None,
    role: str = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    show_swatches: bool = None,
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    suffix: str = None,
    swatches: list = [],
    swatches_max_height: typing.Union[str, float] = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ColorInput, Any]:
    """Widget for the Vuetify v-color-input component, see https://vuetifyjs.com/en/api/v-color-input/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: Enables autofocus.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param cancel_text: Text for the cancel button
    :param canvas_height: Height of canvas.
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param color_pip: Synchronize pip color with current value
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Function returns the counter display text.
    :param density: Adjusts the vertical height used by the component.
    :param dirty: Manually apply the dirty state styling.
    :param disabled: Removes the ability to click or target the input.
    :param divided: Adds a divider between the header and controls.
    :param dot_size: Changes the size of the selection dot on the canvas.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param eye_dropper_icon: Icon used to trigger EyeDropper API.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_actions: Prevent showing the default actions buttons. Does not affect `<component :is="actions" />`
    :param hide_canvas: Hides canvas.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_eye_dropper: Hides eyedropper icon.
    :param hide_header: Hide the picker header.
    :param hide_inputs: Hides inputs.
    :param hide_pip: Hide pip icon
    :param hide_sliders: Hides sliders.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hide_title: Hide the picker title.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-color-input/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param landscape: Puts the picker into landscape mode.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param mode: The current selected input type. Syncable with `v-model:mode`.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: Represents the committed v-model value
    :param modes: Sets available input types.
    :param name: Sets the component's name attribute.
    :param ok_text: Text for the ok button
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-color-input/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param picker_props: Pass props through to the picker component. Intended for props that conflict with `v-text-field` (`color`, `width`, `rounded`, etc.)
    :param pip_icon: The icon used for pip
    :param pip_location: Move pip icon to a different slot
    :param pip_variant: Variant of the pip control
    :param placeholder: Sets the input’s placeholder text.
    :param position: Sets the position for the component.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param readonly: Puts input in readonly state.
    :param reverse: Reverses the orientation.
    :param role: The role attribute applied to the input.
    :param rounded: Adds a border radius to the input.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param show_swatches: Displays color swatches.
    :param single_line: Label does not move on focus/dirty.
    :param suffix: Displays suffix text.
    :param swatches: Sets the available color swatches to select from. 2D array of rows and columns, accepts any color format the picker does.
    :param swatches_max_height: Sets the maximum height of the swatches section.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param type: Sets input type.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width of the color picker.
    """
    ...


@implements(_ColorInput)
def ColorInput(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ColorInput
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ColorInput


def _ColorPicker(
    attributes: dict = {},
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    canvas_height: typing.Union[str, float] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    divided: bool = None,
    dot_size: typing.Union[str, float] = None,
    elevation: typing.Union[str, float] = None,
    eye_dropper_icon: Any = None,
    height: typing.Union[str, float] = None,
    hide_canvas: bool = None,
    hide_eye_dropper: bool = None,
    hide_header: bool = None,
    hide_inputs: bool = None,
    hide_sliders: bool = None,
    hide_title: bool = None,
    landscape: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    mode: str = None,
    model_value: typing.Union[str, dict] = None,
    modes: list = [],
    position: str = None,
    readonly: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    show_swatches: bool = None,
    slot: str = None,
    style_: str = None,
    swatches: list = [],
    swatches_max_height: typing.Union[str, float] = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ColorPicker, Any]:
    """Widget for the Vuetify v-color-picker component, see https://vuetifyjs.com/en/api/v-color-picker/
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param canvas_height: Height of canvas.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param divided: Adds a divider between the header and controls.
    :param dot_size: Changes the size of the selection dot on the canvas.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param eye_dropper_icon: Icon used to trigger EyeDropper API.
    :param height: Sets the height for the component.
    :param hide_canvas: Hides canvas.
    :param hide_eye_dropper: Hides eyedropper icon.
    :param hide_header: Hide the picker header.
    :param hide_inputs: Hides inputs.
    :param hide_sliders: Hides sliders.
    :param hide_title: Hide the picker title.
    :param landscape: Puts the picker into landscape mode.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param mode: The current selected input type. Syncable with `v-model:mode`.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param modes: Sets available input types.
    :param position: Sets the position for the component.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param show_swatches: Displays color swatches.
    :param swatches: Sets the available color swatches to select from. 2D array of rows and columns, accepts any color format the picker does.
    :param swatches_max_height: Sets the maximum height of the swatches section.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param width: Sets the width of the color picker.
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
    always_filter: bool = None,
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    auto_select_first: typing.Union[bool, str] = None,
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: Any = None,
    clear_on_select: bool = None,
    clearable: bool = None,
    closable_chips: bool = None,
    close_text: str = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    custom_filter: Any = None,
    custom_key_filter: Any = None,
    delimiters: list = [],
    density: str = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    item_children: str = None,
    item_color: str = None,
    item_props: str = None,
    item_title: str = None,
    item_type: str = None,
    item_value: str = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    list_props: Any = None,
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    menu: bool = None,
    menu_icon: Any = None,
    menu_props: Any = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_modifiers: Any = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    no_auto_scroll: bool = None,
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
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
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
    tile: bool = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    value_comparator: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Combobox, Any]:
    """Widget for the Vuetify v-combobox component, see https://vuetifyjs.com/en/api/v-combobox/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param always_filter: When enabled, dropdown list will always show items matching non-empty value within the field. Recommended when the list is meant to show suggestions rather than options to choose from. For optimal UX, should be combined with `:menu-icon="false"` and `hide-selected`.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param auto_select_first: When searching, will always highlight the first option and select it on blur. `exact` will only highlight and select exact matches.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: Enables autofocus.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param chips: Changes display of selections to chips.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clear_on_select: Reset the search text when a selection is made while using the **multiple** prop.
    :param clearable: Allows for the component to be cleared.
    :param closable_chips: Enables the [closable](https://vuetifyjs.com/en/api/v-chip/#props-closable) prop on all [v-chip](https://vuetifyjs.com/en/components/chips/) components.
    :param close_text: Text set to the inputs `aria-label` and `title` when input menu is closed.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Function returns the counter display text.
    :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
    :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
    :param delimiters: Accepts an array of strings that will trigger a new tag when typing. Does not replace the normal Tab and Enter keys.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the input.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param filter_keys: Array of specific keys to filter on the item.
    :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :param hide_selected: Do not display in the select menu items that are already selected.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-combobox/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param item_children: This property currently has **no effect**.
    :param item_color: Sets color of selected items.
    :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
    :param item_title: Property on supplied `items` that contains its title.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: Can be an array of objects or strings. By default objects should have **title** and **value** properties, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props). Keys to use for these can be changed with the **item-title**, **item-value**, and **item-props** props.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param list_props: Pass props through to the `v-list` component. Accepts an object with anything from [v-list](https://vuetifyjs.com/en/api/v-list/#props) props, camelCase keys are recommended.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param menu: Renders with the menu open by default.
    :param menu_icon: Sets the the spin icon.
    :param menu_props: Pass props through to the `v-menu` component. Accepts an object with anything from [v-menu](https://vuetifyjs.com/en/api/v-menu/#props) props, camelCase keys are recommended.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes select to multiple. Accepts array for value.
    :param name: Sets the component's name attribute.
    :param no_data_text: Text shown when no items are provided to the component.
    :param no_filter: Disables all item filtering.
    :param open_on_clear: Open's the menu whenever the clear icon is clicked.
    :param open_text: Text set to the inputs **aria-label** and **title** when input menu is open.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-combobox/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param placeholder: Sets the input’s placeholder text.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param readonly: Puts input in readonly state.
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param reverse: Reverses the orientation.
    :param role: The role attribute applied to the input.
    :param rounded: Adds a border radius to the input.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param single_line: Label does not move on focus/dirty.
    :param suffix: Displays suffix text.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param type: Sets input type.
    :param validate_on: Change what type of event triggers validation to run.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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


def _CommandPalette(
    absolute: bool = None,
    activator: str = None,
    activator_props: Any = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    capture_focus: bool = None,
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    custom_filter: Any = None,
    custom_key_filter: Any = None,
    density: str = None,
    disabled: bool = None,
    eager: bool = None,
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    fullscreen: bool = None,
    height: typing.Union[str, float] = None,
    hotkey: str = None,
    input_icon: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    list_props: Any = None,
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    no_data_text: str = None,
    no_filter: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    placeholder: str = None,
    retain_focus: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    scrollable: bool = None,
    search: str = None,
    slot: str = None,
    stick_to_target: bool = None,
    style_: str = None,
    tabbable: bool = None,
    target: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    viewport_margin: typing.Union[str, float] = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CommandPalette, Any]:
    """Widget for the Vuetify v-command-palette component, see https://vuetifyjs.com/en/api/v-command-palette/
    :param absolute: Applies **position: absolute** to the content element.
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Closes component when you click on its content.
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
    :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param filter_keys: Array of specific keys to filter on the item.
    :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
    :param fullscreen: Changes layout for fullscreen display.
    :param height: Sets the height for the component.
    :param hotkey: Global keyboard shortcut to toggle the palette. Accepts hotkey strings like `'ctrl+shift+p'` or `'meta+j'`. The shortcut is automatically registered on mount and cleaned up on unmount.
    :param input_icon: Icon to display at the start of the search input field.
    :param items: Array of command palette items. Objects should have **title** and optionally **subtitle**, **prependIcon**, **appendIcon**, **prependAvatar**, **appendAvatar**, **hotkey**, **onClick**, **to**, **href**, and **value** properties. Use `type: 'subheader'` with a **title** for section headers, or `type: 'divider'` for visual separators between groups.
    :param list_props: Pass props through to the `v-list` component. Accepts an object with anything from [v-list](https://vuetifyjs.com/en/api/v-list/#props) props, camelCase keys are recommended.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: Controls the visibility of the command palette dialog. Use `v-model` for two-way binding.
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :param no_data_text: Text displayed when no items match the current search query.
    :param no_filter: Disables all item filtering.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :param open_on_click: Activate the component when the activator is clicked.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Activate the component when the activator is hovered.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :param placeholder: Placeholder text displayed in the search input.
    :param retain_focus: Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.
    :param scrim: Accepts true/false to enable background, and string to define color.
    :param scroll_strategy: Strategy used when the component is activate and user scrolls.
    :param scrollable: When set to true, expects a `v-card` and a `v-card-text` component with a designated height. For more information, check out the [scrollable example](https://vuetifyjs.com/en/components/dialogs#scrollable).
    :param search: The current search query. Use `v-model:search` to control or monitor the search input value.
    :param stick_to_target: Enables the overlay content to go off-screen when scrolling.
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param viewport_margin: Sets custom viewport margin for the overlay content
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
    """
    ...


@implements(_CommandPalette)
def CommandPalette(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CommandPalette
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CommandPalette


def _CommandPaletteItemComponent(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    index: float = None,
    item: dict = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.CommandPaletteItemComponent, Any]:
    """Widget for the Vuetify v-command-palette-item-component component, see https://vuetifyjs.com/en/api/v-command-palette-item-component/
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_CommandPaletteItemComponent)
def CommandPaletteItemComponent(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.CommandPaletteItemComponent
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _CommandPaletteItemComponent


def _ComponentIcon(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ComponentIcon, Any]:
    """Widget for the Vuetify v-component-icon component, see https://vuetifyjs.com/en/api/v-component-icon/
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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


def _ConfirmEdit(
    attributes: dict = {},
    cancel_text: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: typing.Union[bool, list] = None,
    hide_actions: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    ok_text: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ConfirmEdit, Any]:
    """Widget for the Vuetify v-confirm-edit component, see https://vuetifyjs.com/en/api/v-confirm-edit/
    :param cancel_text: Text for the cancel button
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Control the disabled state of action buttons. If not provided, internal logic will be used to determine the disabled state.
    :param hide_actions: Prevent showing the default actions buttons. Does not affect `<component :is="actions" />`
    :param model_value: Represents the committed v-model value
    :param ok_text: Text for the ok button
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ConfirmEdit)
def ConfirmEdit(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ConfirmEdit
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ConfirmEdit


def _Container(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    fluid: bool = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Container, Any]:
    """Widget for the Vuetify v-container component, see https://vuetifyjs.com/en/api/v-container/
    :param fluid: Removes viewport maximum-width size breakpoints.
    :param height: Sets the height for the component.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Counter, Any]:
    """Widget for the Vuetify v-counter component, see https://vuetifyjs.com/en/api/v-counter/
    :param active: Determines whether the counter is visible or not.
    :param disabled: Removes the ability to click or target the component.
    :param max: Sets the maximum allowed value.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param value: Sets the current counter value.
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
    custom_filter: Any = None,
    custom_key_filter: Any = None,
    custom_key_sort: Any = None,
    expand_on_click: bool = None,
    expanded: list = [],
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    group_by: list = [],
    initial_sort_order: str = None,
    item_selectable: str = None,
    item_value: str = None,
    items: list = [],
    items_length: typing.Union[str, float] = None,
    items_per_page: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: bool = None,
    model_value: list = [],
    multi_sort: typing.Union[bool, dict] = None,
    must_sort: bool = None,
    no_filter: bool = None,
    page: typing.Union[str, float] = None,
    page_by: str = None,
    return_object: bool = None,
    search: str = None,
    select_strategy: str = None,
    show_expand: bool = None,
    show_select: bool = None,
    slot: str = None,
    sort_by: list = [],
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    transition: typing.Union[str, bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataIterator, Any]:
    """Widget for the Vuetify v-data-iterator component, see https://vuetifyjs.com/en/api/v-data-iterator/
    :param custom_filter: Function to filter items.
    :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
    :param custom_key_sort: Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified.
    :param expand_on_click: Expands item when the row is clicked.
    :param expanded: Array of expanded items. Can be bound to external variable using **v-model:expanded**.
    :param filter_keys: Array of specific keys to filter on the item.
    :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
    :param group_by: Configures attributes (and sort order) to group items together.
    :param initial_sort_order: Specifies the initial sort order when an **toggleSort** is called for unsorted property.
    :param item_selectable: Property on supplied `items` that contains the boolean value indicating if the item is selectable.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: An array of strings or objects used for automatically generating children components.
    :param items_per_page: Changes how many items per page should be visible. Can be bound to external variable using **v-model:itemsPerPage**.. Setting this prop to `-1` will display all items on the page.
    :param loading: If `true` and no items are provided, then a loading text will be shown.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multi_sort: Let user sort by multiple properties/columns.

    - **key**: (optional) when set to `ctrl`, user is required to hold a keyboard key (Ctrl on PC and Command on Mac)
    - **mode**: when user selects a new column to sort by, it will be set first (`prepend`) or last (`append`) in the sort priority. Defaults to `append`
    - **modifier**: (optional) allows user to use both multi-sort modes (`append` and `prepend`) simultaneously

    **Note**: object notation requires at least **v3.11.0**
    :param must_sort: Forces sorting on the column(s).
    :param no_filter: Disables all item filtering.
    :param page: The current displayed page number (1-indexed).
    :param page_by: Controls how pagination counts items.
    - **item** paginates by individual items,
    - **auto** paginates by top-level groups and falls back to regular items if **group-by** is empty,
    - **any** paginates by both items and groups combined
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param search: Text input used to filter items.
    :param select_strategy: Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).
    :param show_expand: Shows the expand icon.
    :param show_select: Shows the column with checkboxes for selecting items in the list.
    :param sort_by: Array of column keys and sort orders that determines the sort order of the table.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
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
    cell_props: dict = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    custom_filter: Any = None,
    custom_key_filter: Any = None,
    custom_key_sort: Any = None,
    density: str = None,
    disable_sort: bool = None,
    expand_icon: Any = None,
    expand_on_click: bool = None,
    expanded: list = [],
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    first_icon: Any = None,
    first_page_label: str = None,
    fixed_footer: bool = None,
    fixed_header: bool = None,
    group_by: list = [],
    group_collapse_icon: Any = None,
    group_expand_icon: Any = None,
    header_props: Any = None,
    headers: str = None,
    height: typing.Union[str, float] = None,
    hide_default_body: bool = None,
    hide_default_footer: bool = None,
    hide_default_header: bool = None,
    hide_no_data: bool = None,
    hover: bool = None,
    initial_sort_order: str = None,
    item_selectable: str = None,
    item_value: str = None,
    items: list = [],
    items_per_page: typing.Union[str, float] = None,
    items_per_page_options: list = [],
    items_per_page_text: str = None,
    last_icon: Any = None,
    last_page_label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    loading_text: str = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    model_value: Any = None,
    multi_sort: typing.Union[bool, dict] = None,
    must_sort: bool = None,
    next_icon: Any = None,
    next_page_label: str = None,
    no_data_text: str = None,
    no_filter: bool = None,
    page: typing.Union[str, float] = None,
    page_by: str = None,
    page_text: str = None,
    prev_icon: Any = None,
    prev_page_label: str = None,
    return_object: bool = None,
    row_props: dict = None,
    search: str = None,
    select_strategy: str = None,
    show_current_page: bool = None,
    show_expand: bool = None,
    show_select: bool = None,
    slot: str = None,
    sort_asc_icon: Any = None,
    sort_by: list = [],
    sort_desc_icon: Any = None,
    sort_icon: Any = None,
    sticky: bool = None,
    striped: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTable, Any]:
    """Widget for the Vuetify v-data-table component, see https://vuetifyjs.com/en/api/v-data-table/
    :param cell_props: An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.
    :param collapse_icon: Icon to display when the expandable row is expanded.
    :param color: Applies a color to checkboxes, page size dropdown and sort badges in the table header.
    :param custom_filter: Function to filter items.
    :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
    :param custom_key_sort: Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified.
    :param density: Adjusts the vertical height of the table rows.
    :param disable_sort: Toggles rendering of sort button.
    :param expand_icon: Icon to display when the expandable row is collapsed.
    :param expand_on_click: Expands item when the row is clicked.
    :param expanded: Array of expanded items. Can be bound to external variable using **v-model:expanded**.
    :param filter_keys: Array of specific keys to filter on the item.
    :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
    :param first_icon: First icon.
    :param first_page_label: Label for first page.
    :param fixed_footer: Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.
    :param fixed_header: Fixed header to top of table.
    :param group_by: Configures attributes (and sort order) to group items together. Can be customized further with `group-header` and `group-summary` slots.
    :param group_collapse_icon: Icon to display when the row group is expanded.
    :param group_expand_icon: Icon to display when the row group is collapsed.
    :param header_props: Pass props to the default header. See [`v-data-table-headers` API](https://vuetifyjs.com/en/api/v-data-table-headers) for more information.
    :param headers: An array of objects that each describe a header column.
    :param height: Set an explicit height of table.
    :param hide_default_body: Hides the default body.
    :param hide_default_footer: Hides the default footer.
    :param hide_default_header: Hides the default header.
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :param hover: Adds a hover effects to a table rows.
    :param initial_sort_order: Specifies the initial sort order when an unsorted column is clicked.
    :param item_selectable: Property on supplied `items` that indicates whether the item is selectable.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: An array of strings or objects used for automatically generating children components.
    :param items_per_page: Changes how many items per page should be visible. Can be bound to external variable using **v-model:itemsPerPage**.. Setting this prop to `-1` will display all items on the page.
    :param items_per_page_options: Array of options to show in the items-per-page dropdown.
    :param items_per_page_text: Text for items-per-page dropdown.
    :param last_icon: Last icon.
    :param last_page_label: Label for last page.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param loading_text: Text shown when the data is loading.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multi_sort: Let user sort by multiple properties/columns.

    - **key**: (optional) when set to `ctrl`, user is required to hold a keyboard key (Ctrl on PC and Command on Mac)
    - **mode**: when user selects a new column to sort by, it will be set first (`prepend`) or last (`append`) in the sort priority. Defaults to `append`
    - **modifier**: (optional) allows user to use both multi-sort modes (`append` and `prepend`) simultaneously

    **Note**: object notation requires at least **v3.11.0**
    :param must_sort: Forces sorting on the column(s).
    :param next_icon: Next icon.
    :param next_page_label: Label for next page.
    :param no_data_text: Text shown when no items are provided to the component.
    :param no_filter: Disables all item filtering.
    :param page: The current displayed page number (1-indexed).
    :param page_by: Controls how pagination counts items.
    - **item** paginates by individual items,
    - **auto** paginates by top-level groups and falls back to regular items if **group-by** is empty,
    - **any** paginates by both items and groups combined
    :param page_text: Label for page number.
    :param prev_icon: Previous icon.
    :param prev_page_label: Label for previous page.
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param row_props: An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.
    :param search: Text input used to filter items.
    :param select_strategy: Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).
    :param show_current_page: Show current page number between prev/next icons.
    :param show_expand: Shows the expand toggle in default rows.
    :param show_select: Shows the select checkboxes in both the header and rows (if using default rows).
    :param sort_asc_icon: Icon used for ascending sort button.
    :param sort_by: Changes which item property (or properties) should be used for sort order. Can be bound to external variable using **v-model:sortBy**..
    :param sort_desc_icon: Icon used for descending sort button.
    :param sort_icon: Icon used for unsorted columns. By default it uses either **sortAscIcon** or **sortDescIcon** depending on **initialSortOrder**, but can be customized to show a neutral icon instead.
    :param sticky: Deprecated, use `fixed-header` instead.
    :param striped: Applies a background to either **even** or **odd** rows.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param width: Sets the width for the component.
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
    color: str = None,
    first_icon: Any = None,
    first_page_label: str = None,
    items_per_page_options: list = [],
    items_per_page_text: str = None,
    last_icon: Any = None,
    last_page_label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    next_icon: Any = None,
    next_page_label: str = None,
    page_text: str = None,
    prev_icon: Any = None,
    prev_page_label: str = None,
    show_current_page: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableFooter, Any]:
    """Widget for the Vuetify v-data-table-footer component, see https://vuetifyjs.com/en/api/v-data-table-footer/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param first_icon: First icon.
    :param first_page_label: Label for first page.
    :param items_per_page_options: Array of options to show in the items-per-page dropdown.
    :param items_per_page_text: Text for items-per-page dropdown.
    :param last_icon: Last icon.
    :param last_page_label: Label for last page.
    :param next_icon: Next icon.
    :param next_page_label: Label for next page.
    :param page_text: Label for page number.
    :param prev_icon: Previous icon.
    :param prev_page_label: Label for previous page.
    :param show_current_page: Show current page number between prev/next icons.
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


def _DataTableHeaders(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disable_sort: bool = None,
    fixed_header: bool = None,
    header_props: Any = None,
    initial_sort_order: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    multi_sort: bool = None,
    slot: str = None,
    sort_asc_icon: Any = None,
    sort_desc_icon: Any = None,
    sort_icon: Any = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableHeaders, Any]:
    """Widget for the Vuetify v-data-table-headers component, see https://vuetifyjs.com/en/api/v-data-table-headers/
    :param color: Applies a color to checkboxes, page size dropdown and sort badges in the table header.
    :param density: Adjusts the vertical height used by the component.
    :param fixed_header: Sticks the header to the top of the table.
    :param header_props: Additional props to be be passed to the default header
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param sort_asc_icon: Icon used for ascending sort button.
    :param sort_desc_icon: Icon used for descending sort button.
    :param sort_icon: Icon used for unsorted columns. By default it uses either **sortAscIcon** or **sortDescIcon** depending on **initialSortOrder**, but can be customized to show a neutral icon instead.
    :param sticky: Deprecated, use `fixed-header` instead.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_DataTableHeaders)
def DataTableHeaders(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DataTableHeaders
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DataTableHeaders


def _DataTableRow(
    attributes: dict = {},
    cell_props: dict = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    density: str = None,
    expand_icon: Any = None,
    index: float = None,
    item: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableRow, Any]:
    """Widget for the Vuetify v-data-table-row component, see https://vuetifyjs.com/en/api/v-data-table-row/
    :param cell_props: Props to be applied to the cell.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param index: Row index.
    :param item: Data (key, index and column values) of the displayed item.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
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
    cell_props: dict = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    density: str = None,
    expand_icon: Any = None,
    group_collapse_icon: Any = None,
    group_expand_icon: Any = None,
    hide_no_data: bool = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    loading_text: str = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    no_data_text: str = None,
    row_props: dict = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableRows, Any]:
    """Widget for the Vuetify v-data-table-rows component, see https://vuetifyjs.com/en/api/v-data-table-rows/
    :param cell_props: An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :param items: An array of strings or objects used for automatically generating children components.
    :param loading: Displays `loading` slot if set to `true`
    :param loading_text: Text shown when the data is loading.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param no_data_text: Text shown when no items are provided to the component.
    :param row_props: An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.
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
    cell_props: dict = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    custom_key_sort: Any = None,
    density: str = None,
    disable_sort: bool = None,
    expand_icon: Any = None,
    expand_on_click: bool = None,
    expanded: list = [],
    first_icon: Any = None,
    first_page_label: str = None,
    fixed_footer: bool = None,
    fixed_header: bool = None,
    group_by: list = [],
    group_collapse_icon: Any = None,
    group_expand_icon: Any = None,
    header_props: Any = None,
    headers: str = None,
    height: typing.Union[str, float] = None,
    hide_default_body: bool = None,
    hide_default_footer: bool = None,
    hide_default_header: bool = None,
    hide_no_data: bool = None,
    hover: bool = None,
    initial_sort_order: str = None,
    item_selectable: str = None,
    item_value: str = None,
    items: list = [],
    items_length: typing.Union[str, float] = None,
    items_per_page: typing.Union[str, float] = None,
    items_per_page_options: list = [],
    items_per_page_text: str = None,
    last_icon: Any = None,
    last_page_label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    loading_text: str = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    model_value: Any = None,
    multi_sort: typing.Union[bool, dict] = None,
    must_sort: bool = None,
    next_icon: Any = None,
    next_page_label: str = None,
    no_data_text: str = None,
    page: typing.Union[str, float] = None,
    page_by: str = None,
    page_text: str = None,
    prev_icon: Any = None,
    prev_page_label: str = None,
    return_object: bool = None,
    row_props: dict = None,
    search: str = None,
    select_strategy: str = None,
    show_current_page: bool = None,
    show_expand: bool = None,
    show_select: bool = None,
    slot: str = None,
    sort_asc_icon: Any = None,
    sort_by: list = [],
    sort_desc_icon: Any = None,
    sort_icon: Any = None,
    sticky: bool = None,
    striped: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableServer, Any]:
    """Widget for the Vuetify v-data-table-server component, see https://vuetifyjs.com/en/api/v-data-table-server/
    :param cell_props: An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.
    :param color: Applies a color to checkboxes, page size dropdown and sort badges in the table header.
    :param custom_key_sort: Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified.
    :param density: Adjusts the vertical height used by the component.
    :param disable_sort: Toggles rendering of sort button.
    :param expand_on_click: Expands item when the row is clicked.
    :param expanded: Array of expanded items. Can be bound to external variable using **v-model:expanded**.
    :param first_icon: First icon.
    :param first_page_label: Label for first page.
    :param fixed_footer: Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.
    :param fixed_header: Use the fixed-header prop together with the height prop to fix the header to the top of the table.
    :param group_by: Defines the grouping of the table items.
    :param header_props: Pass props to the default header. See [`v-data-table-server` API](https://vuetifyjs.com/en/api/v-data-table-server) for more information.
    :param headers: An array of objects that each describe a header column.
    :param height: Use the height prop to set the height of the table.
    :param hide_default_body: Hides the default body.
    :param hide_default_footer: Hides the default footer.
    :param hide_default_header: Hides the default header.
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :param hover: Will add a hover effect to a table's row when the mouse is over it.
    :param initial_sort_order: Specifies the initial sort order when an unsorted column is clicked.
    :param item_selectable: Property on supplied `items` that indicates whether the item is selectable.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: An array of strings or objects used for automatically generating children components.
    :param items_length: Number of all items.
    :param items_per_page: The number of items to display on each page.
    :param items_per_page_options: Array of options to show in the items-per-page dropdown.
    :param items_per_page_text: Text for items-per-page dropdown.
    :param last_icon: Last icon.
    :param last_page_label: Label for last page.
    :param loading: Displays `loading` slot if set to `true`
    :param loading_text: Text shown when the data is loading.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multi_sort: Let user sort by multiple properties/columns.

    - **key**: (optional) when set to `ctrl`, user is required to hold a keyboard key (Ctrl on PC and Command on Mac)
    - **mode**: when user selects a new column to sort by, it will be set first (`prepend`) or last (`append`) in the sort priority. Defaults to `append`
    - **modifier**: (optional) allows user to use both multi-sort modes (`append` and `prepend`) simultaneously

    **Note**: object notation requires at least **v3.11.0**
    :param must_sort: Forces sorting on the column(s).
    :param next_icon: Next icon.
    :param next_page_label: Label for next page.
    :param no_data_text: Text shown when no items are provided to the component.
    :param page: The current displayed page number (1-indexed).
    :param page_by: Controls how pagination counts items.
    - **item** paginates by individual items,
    - **auto** paginates by top-level groups and falls back to regular items if **group-by** is empty,
    - **any** paginates by both items and groups combined
    :param page_text: Label for page number.
    :param prev_icon: Previous icon.
    :param prev_page_label: Label for previous page.
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param row_props: An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.
    :param search: Text input used to filter items.
    :param select_strategy: Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).
    :param show_current_page: Show current page number between prev/next icons.
    :param show_expand: Shows the expand icon.
    :param show_select: Shows the column with checkboxes for selecting items in the list.
    :param sort_asc_icon: Icon used for ascending sort button.
    :param sort_by: Array of column keys and sort orders that determines the sort order of the table.
    :param sort_desc_icon: Icon used for descending sort button.
    :param sort_icon: Icon used for unsorted columns. By default it uses either **sortAscIcon** or **sortDescIcon** depending on **initialSortOrder**, but can be customized to show a neutral icon instead.
    :param sticky: Deprecated, use `fixed-header` instead.
    :param striped: Applies a background to either **even** or **odd** rows.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param width: Sets the width for the component.
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
    cell_props: dict = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    custom_filter: Any = None,
    custom_key_filter: Any = None,
    custom_key_sort: Any = None,
    density: str = None,
    disable_sort: bool = None,
    expand_icon: Any = None,
    expand_on_click: bool = None,
    expanded: list = [],
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    fixed_footer: bool = None,
    fixed_header: bool = None,
    group_by: list = [],
    group_collapse_icon: Any = None,
    group_expand_icon: Any = None,
    header_props: Any = None,
    headers: str = None,
    height: typing.Union[str, float] = None,
    hide_default_body: bool = None,
    hide_default_header: bool = None,
    hide_no_data: bool = None,
    hover: bool = None,
    initial_sort_order: str = None,
    item_height: typing.Union[str, float] = None,
    item_key: str = None,
    item_selectable: str = None,
    item_value: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    loading_text: str = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    model_value: Any = None,
    multi_sort: typing.Union[bool, dict] = None,
    must_sort: bool = None,
    no_data_text: str = None,
    no_filter: bool = None,
    return_object: bool = None,
    row_props: dict = None,
    search: str = None,
    select_strategy: str = None,
    show_expand: bool = None,
    show_select: bool = None,
    slot: str = None,
    sort_asc_icon: Any = None,
    sort_by: list = [],
    sort_desc_icon: Any = None,
    sort_icon: Any = None,
    sticky: bool = None,
    striped: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DataTableVirtual, Any]:
    """Widget for the Vuetify v-data-table-virtual component, see https://vuetifyjs.com/en/api/v-data-table-virtual/
    :param cell_props: An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.
    :param color: Applies a color to checkboxes, page size dropdown and sort badges in the table header.
    :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
    :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
    :param custom_key_sort: Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified.
    :param density: Adjusts the vertical height used by the component.
    :param disable_sort: Toggles rendering of sort button.
    :param expand_on_click: Expands item when the row is clicked.
    :param expanded: Array of expanded items. Can be bound to external variable using **v-model:expanded**.
    :param filter_keys: Array of specific keys to filter on the item.
    :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
    :param fixed_footer: Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.
    :param fixed_header: Sticks the header to the top of the table.
    :param group_by: Defines the grouping of the table items.
    :param header_props: Pass props to the default header.
    :param headers: An array of objects that each describe a header column.
    :param height: Use the height prop to set the height of the table.
    :param hide_default_body: Hides the default body.
    :param hide_default_header: Hides the default header.
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :param hover: Will add a hover effect to a table's row when the mouse is over it.
    :param initial_sort_order: Specifies the initial sort order when an unsorted column is clicked.
    :param item_height: Height in pixels of each item to display.
    :param item_key: The property on each item that is used as a unique key.
    :param item_selectable: Property on supplied `items` that indicates whether the item is selectable.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: An array of strings or objects used for automatically generating children components.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param loading_text: Text shown when the data is loading.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multi_sort: Let user sort by multiple properties/columns.

    - **key**: (optional) when set to `ctrl`, user is required to hold a keyboard key (Ctrl on PC and Command on Mac)
    - **mode**: when user selects a new column to sort by, it will be set first (`prepend`) or last (`append`) in the sort priority. Defaults to `append`
    - **modifier**: (optional) allows user to use both multi-sort modes (`append` and `prepend`) simultaneously

    **Note**: object notation requires at least **v3.11.0**
    :param must_sort: Forces sorting on the column(s).
    :param no_data_text: Text shown when no items are provided to the component.
    :param no_filter: Disables all item filtering.
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param row_props: An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.
    :param search: Text input used to filter items.
    :param select_strategy: Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).
    :param show_expand: Shows the expand icon.
    :param show_select: Shows the column with checkboxes for selecting items in the list.
    :param sort_asc_icon: Icon used for ascending sort button.
    :param sort_by: Array of column keys and sort orders that determines the sort order of the table.
    :param sort_desc_icon: Icon used for descending sort button.
    :param sort_icon: Icon used for unsorted columns. By default it uses either **sortAscIcon** or **sortDescIcon** depending on **initialSortOrder**, but can be customized to show a neutral icon instead.
    :param sticky: Deprecated, use `fixed-header` instead.
    :param striped: Applies a background to either **even** or **odd** rows.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param width: Sets the width for the component.
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


def _DateInput(
    active: bool = None,
    allowed_dates: list = [],
    allowed_months: list = [],
    allowed_years: list = [],
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    cancel_text: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    color: str = None,
    control_height: typing.Union[str, float] = None,
    control_variant: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    density: str = None,
    dirty: bool = None,
    disabled: bool = None,
    display_format: str = None,
    divided: bool = None,
    elevation: typing.Union[str, float] = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    event_color: typing.Union[typing.Union[str, bool, list], dict] = None,
    events: typing.Union[list, dict] = None,
    first_day_of_week: typing.Union[str, float] = None,
    first_day_of_year: typing.Union[str, float] = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    header: str = None,
    header_color: str = None,
    header_date_format: str = None,
    hide_actions: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_header: bool = None,
    hide_spin_buttons: bool = None,
    hide_title: bool = None,
    hide_weekdays: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    input_format: str = None,
    label: str = None,
    landscape: bool = None,
    landscape_header_width: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    location: Any = None,
    max: Any = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    menu: bool = None,
    menu_props: Any = None,
    messages: typing.Union[str, list] = None,
    min: Any = None,
    min_width: typing.Union[str, float] = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    mode_icon: Any = None,
    model_modifiers: Any = None,
    model_value: Any = None,
    month: typing.Union[str, float] = None,
    multiple: typing.Union[bool, float, str] = None,
    name: str = None,
    next_icon: Any = None,
    no_month_picker: bool = None,
    ok_text: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    picker_props: Any = None,
    placeholder: str = None,
    position: str = None,
    prefix: str = None,
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
    prev_icon: Any = None,
    readonly: bool = None,
    reverse: bool = None,
    reverse_transition: str = None,
    role: str = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    show_adjacent_months: bool = None,
    show_week: bool = None,
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    suffix: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: str = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    transition: str = None,
    type: str = None,
    update_on: list = [],
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
    view_mode: str = None,
    weekday_format: str = None,
    weekdays: list = [],
    weeks_in_month: str = None,
    width: typing.Union[str, float] = None,
    year: float = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DateInput, Any]:
    """Widget for the Vuetify v-date-input component, see https://vuetifyjs.com/en/api/v-date-input/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param allowed_dates: Restricts which dates can be selected.
    :param allowed_months: Restricts which months can be selected.
    :param allowed_years: Restricts which years can be selected.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: Enables autofocus.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param cancel_text: Text for the cancel button
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param control_height: Sets the height of the controls.
    :param control_variant: - **docked:** Separate control groups for month and year.
    - **modal:** Month and year are displayed together, clicking the text opens a month picker, clicking the dropdown arrow opens a year picker. There are also arrow buttons to scroll between months.
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Function returns the counter display text.
    :param density: Adjusts the vertical height used by the component.
    :param dirty: Manually apply the dirty state styling.
    :param disabled: Removes the ability to click or target the input.
    :param display_format: The format of the date that is displayed in the input. Can use any format [here](https://vuetifyjs.com/en/features/dates/#format-options) or a custom function.
    :param divided: Adds a divider between the header and controls.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param event_color: Sets the color for event dots. It can be string (all events will have the same color) or `object` where attribute is the event date and value is boolean/color/array of colors for specified date or `function` taking date as a parameter and returning boolean/color/array of colors for that date.
    :param events: Array of dates or object defining events or colors or function returning boolean/color/array of colors.
    :param first_day_of_week: Sets the first day of the week, starting with 0 for Sunday. (Note: not guaranteed to work when using custom date adapters.)
    :param first_day_of_year: Sets the day that determines the first week of the year, starting with 0 for Sunday. For ISO 8601 this should be 4. (Note: not guaranteed to work when using custom date adapters.)
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param header: Text shown when no **display-date** is set.
    :param header_color: Allows you to set a different color for the header when used in conjunction with the `color` prop.
    :param header_date_format: Allows you to customize the format of the date selection text that appears in the header of the calendar.
    :param hide_actions: Hide the Cancel and OK buttons, and automatically update the value when a date is selected.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_header: Hide the picker header.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hide_title: Hide the picker title.
    :param hide_weekdays: Hides the weekdays.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-date-input/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param input_format: Format for manual date input. Use yyyy, mm, dd with separators '.', '-', '/' (e.g. 'yyyy-mm-dd', 'dd/mm/yyyy').
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param landscape: Puts the picker into landscape mode.
    :param landscape_header_width: Sets header width when in landscape mode.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param location: Specifies the date picker's location. Can combine by using a space separated string.
    :param max: Maximum allowed date/month (ISO 8601 format).
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param menu: Renders with the menu open by default.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min: Minimum allowed date/month (ISO 8601 format).
    :param min_width: Sets the minimum width for the component.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param mode_icon: Icon displayed next to the current month and year, toggles year selection when clicked.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: Represents the committed v-model value
    :param month: Sets the month.
    :param multiple: Allow the selection of multiple dates. The **range** value selects all dates between two selections.
    :param name: Sets the component's name attribute.
    :param next_icon: Sets the icon for next month/year button.
    :param no_month_picker: Only applies to `controlVariant="modal"`, the month and year picker buttons are combined into one that only opens the year picker.
    :param ok_text: Text for the ok button
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-date-input/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param picker_props: Pass props through to the picker component. Intended for props that conflict with `v-text-field` (`color`, `width`, `rounded`, etc.)
    :param placeholder: Sets the input’s placeholder text.
    :param position: Sets the position for the component.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param prev_icon: Sets the icon for previous month/year button.
    :param readonly: Makes the picker readonly (doesn't allow to select new date).
    :param reverse: Reverses the orientation.
    :param reverse_transition: The transition used when changing months into the past
    :param role: The role attribute applied to the input.
    :param rounded: Adds a border radius to the input.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param show_adjacent_months: Toggles visibility of days from previous and next months.
    :param show_week: Toggles visibility of the week numbers in the body of the calendar.
    :param single_line: Label does not move on focus/dirty.
    :param suffix: Displays suffix text.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param transition: The transition used when changing months into the future
    :param type: Determines the type of the picker - `date` for date picker, `month` for month picker.
    :param update_on: Specifies when the text input should update the model value. If empty, the text field will go into read-only state.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param variant: Applies a distinct style to the component.
    :param view_mode: Determines which picker in the date or month picker is being displayed. Allowed values: `'month'`, `'months'`, `'year'`.
    :param weekday_format: Allows you to customize the format of the weekday string that appears in the body of the calendar. Uses `'narrow'` by default. (Note: not guaranteed to work when using custom date adapters.)
    :param weekdays: An array of weekdays to display. Does not affect the order.
    :param weeks_in_month: A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.
    :param width: Width of the picker.
    :param year: Sets the year.
    """
    ...


@implements(_DateInput)
def DateInput(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DateInput
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DateInput


def _DatePicker(
    allowed_dates: list = [],
    allowed_months: list = [],
    allowed_years: list = [],
    attributes: dict = {},
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    control_height: typing.Union[str, float] = None,
    control_variant: str = None,
    disabled: bool = None,
    divided: bool = None,
    elevation: typing.Union[str, float] = None,
    event_color: typing.Union[typing.Union[str, bool, list], dict] = None,
    events: typing.Union[list, dict] = None,
    first_day_of_week: typing.Union[str, float] = None,
    first_day_of_year: typing.Union[str, float] = None,
    header: str = None,
    header_color: str = None,
    header_date_format: str = None,
    height: typing.Union[str, float] = None,
    hide_header: bool = None,
    hide_title: bool = None,
    hide_weekdays: bool = None,
    landscape: bool = None,
    landscape_header_width: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    max: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min: Any = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    mode_icon: Any = None,
    model_value: Any = None,
    month: typing.Union[str, float] = None,
    multiple: typing.Union[bool, float, str] = None,
    next_icon: Any = None,
    no_month_picker: bool = None,
    position: str = None,
    prev_icon: Any = None,
    readonly: bool = None,
    reverse_transition: str = None,
    rounded: typing.Union[str, float, bool] = None,
    show_adjacent_months: bool = None,
    show_week: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: str = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    transition: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    view_mode: str = None,
    weekday_format: str = None,
    weekdays: list = [],
    weeks_in_month: str = None,
    width: typing.Union[str, float] = None,
    year: float = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePicker, Any]:
    """Widget for the Vuetify v-date-picker component, see https://vuetifyjs.com/en/api/v-date-picker/
    :param allowed_dates: Restricts which dates can be selected.
    :param allowed_months: Restricts which months can be selected.
    :param allowed_years: Restricts which years can be selected.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param control_height: Sets the height of the controls.
    :param control_variant: - **docked:** Separate control groups for month and year.
    - **modal:** Month and year are displayed together, clicking the text opens a month picker, clicking the dropdown arrow opens a year picker. There are also arrow buttons to scroll between months.
    :param disabled: Removes the ability to click or target the component.
    :param divided: Adds a divider between the header and controls.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param event_color: Sets the color for event dots. It can be string (all events will have the same color) or `object` where attribute is the event date and value is boolean/color/array of colors for specified date or `function` taking date as a parameter and returning boolean/color/array of colors for that date.
    :param events: Array of dates or object defining events or colors or function returning boolean/color/array of colors.
    :param first_day_of_week: Sets the first day of the week, starting with 0 for Sunday. (Note: not guaranteed to work when using custom date adapters.)
    :param first_day_of_year: Sets the day that determines the first week of the year, starting with 0 for Sunday. For ISO 8601 this should be 4. (Note: not guaranteed to work when using custom date adapters.)
    :param header: Text shown when no **display-date** is set.
    :param header_color: Allows you to set a different color for the header when used in conjunction with the `color` prop.
    :param header_date_format: Allows you to customize the format of the date selection text that appears in the header of the calendar.
    :param height: Sets the height for the component.
    :param hide_header: Hides the header.
    :param hide_title: Hide the picker title.
    :param hide_weekdays: Hides the weekdays.
    :param landscape: Changes the picker to landscape mode.
    :param landscape_header_width: Sets header width when in landscape mode.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max: Maximum allowed date/month (ISO 8601 format).
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min: Minimum allowed date/month (ISO 8601 format).
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param mode_icon: Icon displayed next to the current month and year, toggles year selection when clicked.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param month: Sets the month.
    :param multiple: Allow the selection of multiple dates. The **range** value selects all dates between two selections.
    :param next_icon: Sets the icon for next month/year button.
    :param no_month_picker: Only applies to `controlVariant="modal"`, the month and year picker buttons are combined into one that only opens the year picker.
    :param position: Sets the position for the component.
    :param prev_icon: Sets the icon for previous month/year button.
    :param readonly: Makes the picker readonly (doesn't allow to select new date).
    :param reverse_transition: The transition used when changing months into the past
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param show_adjacent_months: Toggles visibility of days from previous and next months.
    :param show_week: Toggles visibility of the week numbers in the body of the calendar.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param transition: The transition used when changing months into the future
    :param view_mode: Determines which picker in the date or month picker is being displayed. Allowed values: `'month'`, `'months'`, `'year'`.
    :param weekday_format: Allows you to customize the format of the weekday string that appears in the body of the calendar. Uses `'narrow'` by default. (Note: not guaranteed to work when using custom date adapters.)
    :param weekdays: An array of weekdays to display. Does not affect the order.
    :param weeks_in_month: A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.
    :param width: Width of the picker.
    :param year: Sets the year.
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
    active: typing.Union[str, list] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    control_height: typing.Union[str, float] = None,
    control_variant: str = None,
    disabled: typing.Union[str, bool, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mode_icon: Any = None,
    month_text: str = None,
    next_icon: Any = None,
    no_month_picker: bool = None,
    prev_icon: Any = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    text: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    view_mode: str = None,
    year_text: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerControls, Any]:
    """Widget for the Vuetify v-date-picker-controls component, see https://vuetifyjs.com/en/api/v-date-picker-controls/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param control_height: Sets the height of the controls.
    :param control_variant: - **docked:** Separate control groups for month and year.
    - **modal:** Month and year are displayed together, clicking the text opens a month picker, clicking the dropdown arrow opens a year picker. There are also arrow buttons to scroll between months.
    :param disabled: Removes the ability to click or target the component.
    :param mode_icon: Icon used for the mode button.
    :param next_icon: Icon used for the next button.
    :param no_month_picker: Only applies to `controlVariant="modal"`, the month and year picker buttons are combined into one that only opens the year picker.
    :param prev_icon: Icon used for the previous button.
    :param tabbable: Is widget tabbable?
    :param text: Specify content text for the component.
    :param tooltip: A tooltip caption.
    :param view_mode: Sets the view mode of the date picker.
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
    append_icon: Any = None,
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerHeader, Any]:
    """Widget for the Vuetify v-date-picker-header component, see https://vuetifyjs.com/en/api/v-date-picker-header/
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param header: Sets the header content.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param transition: Sets the transition when the header changes.
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
    disabled: bool = None,
    event_color: typing.Union[typing.Union[str, bool, list], dict] = None,
    events: typing.Union[list, dict] = None,
    first_day_of_week: typing.Union[str, float] = None,
    first_day_of_year: typing.Union[str, float] = None,
    hide_weekdays: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: Any = None,
    min: Any = None,
    model_value: Any = None,
    month: typing.Union[str, float] = None,
    multiple: typing.Union[bool, float, str] = None,
    readonly: bool = None,
    reverse_transition: str = None,
    show_adjacent_months: bool = None,
    show_week: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    transition: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    weekday_format: str = None,
    weekdays: list = [],
    weeks_in_month: str = None,
    year: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerMonth, Any]:
    """Widget for the Vuetify v-date-picker-month component, see https://vuetifyjs.com/en/api/v-date-picker-month/
    :param allowed_dates: Sets the allowed dates of the month.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param first_day_of_week: Sets the first day of the week, starting with 0 for Sunday. (Note: not guaranteed to work when using custom date adapters.)
    :param first_day_of_year: Sets the day that determines the first week of the year, starting with 0 for Sunday. For ISO 8601 this should be 4. (Note: not guaranteed to work when using custom date adapters.)
    :param hide_weekdays: Hide the days of the week letters.
    :param max: Sets the maximum date of the month.
    :param min: Sets the minimum date of the month.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param month: Sets the month.
    :param multiple: Sets the multiple of the month.
    :param reverse_transition: The transition used when changing months into the past
    :param show_adjacent_months: Show adjacent months.
    :param show_week: Show the week number.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param transition: The transition used when changing months into the future
    :param weekday_format: Allows you to customize the format of the weekday string that appears in the body of the calendar. Uses `'narrow'` by default. (Note: not guaranteed to work when using custom date adapters.)
    :param weekdays: An array of weekdays to display. Does not affect the order.
    :param weeks_in_month: A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.
    :param year: Sets the year.
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


def _DatePickerMonths(
    allowed_months: list = [],
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: Any = None,
    min: Any = None,
    model_value: float = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    year: float = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerMonths, Any]:
    """Widget for the Vuetify v-date-picker-months component, see https://vuetifyjs.com/en/api/v-date-picker-months/
    :param allowed_months: Restricts which months can be selected.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param height: Sets the height for the component.
    :param max: Sets the maximum selectable date. Months after this date will be disabled.
    :param min: Sets the minimum selectable date. Months before this date will be disabled.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param year: Sets the year for the given months.
    """
    ...


@implements(_DatePickerMonths)
def DatePickerMonths(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.DatePickerMonths
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _DatePickerMonths


def _DatePickerYears(
    allowed_years: list = [],
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: Any = None,
    min: Any = None,
    model_value: float = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DatePickerYears, Any]:
    """Widget for the Vuetify v-date-picker-years component, see https://vuetifyjs.com/en/api/v-date-picker-years/
    :param allowed_years: Restricts which years can be selected.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param height: Sets the height for the component.
    :param max: Sets the maximum date of the month.
    :param min: Sets the minimum date of the month.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DefaultsProvider, Any]:
    """Widget for the Vuetify v-defaults-provider component, see https://vuetifyjs.com/en/api/v-defaults-provider/
    :param defaults: Specify new default prop values for components. Keep in mind that this will be merged with previously defined values.
    :param disabled: Turns off all calculations of new default values for improved performance in situations where defaults propagation isn't necessary.
    :param reset: Reset the default values up the nested chain by {n} amount.
    :param root: Force current defaults to match the application root defaults.
    :param scoped: Prevents the ability for default values to be inherited from parent components.
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
    activator_props: Any = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    capture_focus: bool = None,
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
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
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
    stick_to_target: bool = None,
    style_: str = None,
    tabbable: bool = None,
    target: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    viewport_margin: typing.Union[str, float] = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Dialog, Any]:
    """Widget for the Vuetify v-dialog component, see https://vuetifyjs.com/en/api/v-dialog/
    :param absolute: Applies **position: absolute** to the content element.
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Closes component when you click on its content.
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param fullscreen: Changes layout for fullscreen display.
    :param height: Sets the height for the component.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param no_click_animation: Disables the bounce effect when clicking outside of a `v-dialog`'s content when using the **persistent** prop.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :param open_on_click: Activate the component when the activator is clicked.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Designates whether component should activate when its activator is hovered.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param persistent: Clicking outside of the element or pressing **esc** key will not deactivate it.
    :param retain_focus: Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.
    :param scrim: Accepts true/false to enable background, and string to define color.
    :param scroll_strategy: Strategy used when the component is activate and user scrolls.
    :param scrollable: When set to true, expects a `v-card` and a `v-card-text` component with a designated height. For more information, check out the [scrollable example](https://vuetifyjs.com/en/components/dialogs#scrollable).
    :param stick_to_target: Enables the overlay content to go off-screen when scrolling.
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param viewport_margin: Sets custom viewport margin for the overlay content
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DialogBottomTransition, Any]:
    """Widget for the Vuetify v-dialog-bottom-transition component, see https://vuetifyjs.com/en/api/v-dialog-bottom-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DialogTopTransition, Any]:
    """Widget for the Vuetify v-dialog-top-transition component, see https://vuetifyjs.com/en/api/v-dialog-top-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    target: list = [],
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.DialogTransition, Any]:
    """Widget for the Vuetify v-dialog-transition component, see https://vuetifyjs.com/en/api/v-dialog-transition/
    :param tabbable: Is widget tabbable?
    :param target: Sets the target element for the transition.
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
    content_offset: typing.Union[str, float, list] = None,
    gradient: bool = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: typing.Union[str, float] = None,
    opacity: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    thickness: typing.Union[str, float] = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    vertical: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Divider, Any]:
    """Widget for the Vuetify v-divider component, see https://vuetifyjs.com/en/api/v-divider/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param content_offset: Increases content spacing from the lines. When passed as an array, the second value shifts slot content down (or right in vertical mode).
    :param gradient: Adds fading effect for both sides.
    :param inset: Adds indentation (72px) for **normal** dividers, reduces max height for **vertical**.
    :param length: Sets the dividers length. Default unit is px.
    :param opacity: Sets the component's opacity value
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param thickness: Sets the dividers thickness. Default unit is px.
    :param tooltip: A tooltip caption.
    :param variant: Applies `border-style`.
    :param vertical: Displays dividers vertically.
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


def _EmptyState(
    action_text: str = None,
    attributes: dict = {},
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    headline: str = None,
    height: typing.Union[str, float] = None,
    href: str = None,
    icon: Any = None,
    image: str = None,
    justify: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    text: str = None,
    text_width: typing.Union[str, float] = None,
    theme: str = None,
    title: str = None,
    to: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.EmptyState, Any]:
    """Widget for the Vuetify v-empty-state component, see https://vuetifyjs.com/en/api/v-empty-state/
    :param action_text: The text used for the action button.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param headline: A large headline often used for 404 pages.
    :param height: Sets the height for the component.
    :param href: The URL the action button links to.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param image: Apply a specific image using [v-img](https://vuetifyjs.com/en/components/images/).
    :param justify: Control the justification of the text.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param size: The size used to control the dimensions of the media element inside the component. Can be specified as a number or a string (e.g., '50%', '100px').
    :param tabbable: Is widget tabbable?
    :param text: Specify content text for the component.
    :param text_width: Sets the width of the text container.
    :param theme: Specify a theme for this component and all of its children.
    :param title: Specify a title text for the component.
    :param to: The URL the action button links to.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
    """
    ...


@implements(_EmptyState)
def EmptyState(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.EmptyState
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _EmptyState


def _ExpandBothTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpandBothTransition, Any]:
    """Widget for the Vuetify v-expand-both-transition component, see https://vuetifyjs.com/en/api/v-expand-both-transition/
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_ExpandBothTransition)
def ExpandBothTransition(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.ExpandBothTransition
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _ExpandBothTransition


def _ExpandTransition(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mode: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpandTransition, Any]:
    """Widget for the Vuetify v-expand-transition component, see https://vuetifyjs.com/en/api/v-expand-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
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
    group: bool = None,
    hide_on_leave: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mode: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpandXTransition, Any]:
    """Widget for the Vuetify v-expand-x-transition component, see https://vuetifyjs.com/en/api/v-expand-x-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
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
    collapse_icon: Any = None,
    color: str = None,
    disabled: bool = None,
    eager: bool = None,
    elevation: typing.Union[str, float] = None,
    expand_icon: Any = None,
    focusable: bool = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    slot: str = None,
    static: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanel, Any]:
    """Widget for the Vuetify v-expansion-panel component, see https://vuetifyjs.com/en/api/v-expansion-panel/
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Disables the expansion-panel content.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :param focusable: Makes the expansion panel content focusable.
    :param height: Sets the height for the component.
    :param hide_actions: Hide the expand icon in the content title.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param readonly: Makes the expansion panel content read only.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param static: Remove title size expansion when selected.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param value: Controls the opened/closed state of content.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanelText, Any]:
    """Widget for the Vuetify v-expansion-panel-text component, see https://vuetifyjs.com/en/api/v-expansion-panel-text/
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
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
    collapse_icon: Any = None,
    color: str = None,
    expand_icon: Any = None,
    focusable: bool = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    static: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanelTitle, Any]:
    """Widget for the Vuetify v-expansion-panel-title component, see https://vuetifyjs.com/en/api/v-expansion-panel-title/
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :param focusable: Makes the expansion panel headers focusable.
    :param height: Sets the height for the component.
    :param hide_actions: Hide the expand icon in the content title.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param readonly: Makes the expansion panel content read only.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param static: Remove title size expansion when selected.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    disabled: bool = None,
    eager: bool = None,
    elevation: typing.Union[str, float] = None,
    expand_icon: Any = None,
    flat: bool = None,
    focusable: bool = None,
    hide_actions: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    model_value: Any = None,
    multiple: bool = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    slot: str = None,
    static: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ExpansionPanels, Any]:
    """Widget for the Vuetify v-expansion-panels component, see https://vuetifyjs.com/en/api/v-expansion-panels/
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Puts all children components into a disabled state.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :param flat: Removes the expansion-panel's elevation and borders.
    :param focusable: Makes the expansion-panel headers focusable.
    :param hide_actions: Hide the expand icon in the content title.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param model_value: Controls expanded panel(s). Defaults to an empty array when using **multiple** prop. It is recommended to set unique `value` prop for the panels inside, otherwise index is used instead.
    :param multiple: Allows one to select multiple items.
    :param readonly: Makes the entire expansion panel read only.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param static: Remove title size expansion when selected.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes the border-radius.
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
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


def _Fab(
    absolute: bool = None,
    active: bool = None,
    active_color: str = None,
    app: bool = None,
    appear: bool = None,
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    block: bool = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    extended: bool = None,
    flat: bool = None,
    height: typing.Union[str, float] = None,
    href: str = None,
    icon: Any = None,
    layout: bool = None,
    loading: typing.Union[str, bool] = None,
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    name: str = None,
    offset: bool = None,
    order: typing.Union[str, float] = None,
    position: str = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slim: bool = None,
    slot: str = None,
    stacked: bool = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: Any = None,
    text: typing.Union[str, float, bool] = None,
    theme: str = None,
    tile: bool = None,
    to: Any = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Fab, Any]:
    """Widget for the Vuetify v-fab component, see https://vuetifyjs.com/en/api/v-fab/
    :param absolute: Applies **position: absolute** to the component.
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param active_color: The applied color when the component is in an active state.
    :param app: If true, attaches to the closest layout and positions according to the value of **location**.
    :param appear: Used to control the animation of the FAB.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param block: Expands the button to 100% of available space.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param extended: An alternate style for the FAB that expects text.
    :param flat: Removes the button box shadow. This is different than using the 'flat' variant.
    :param height: Sets the height for the component.
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component. The button will become _round_.
    :param layout: If true, will effect layout dimensions based on size and position.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param location: The location of the fab relative to the layout. Only works when using **app**.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Assign a specific name for layout registration.
    :param offset: Translates the Fab up or down, depending on if location is set to **top** or **bottom**.
    :param order: Adjust the order of the component in relation to its registration order.
    :param position: Sets the position for the component.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param slim: Reduces padding to 0 8px.
    :param stacked: Displays the button as a flex-column.
    :param symbol: The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
    """
    ...


@implements(_Fab)
def Fab(**kwargs):

    widget_cls = ipyvuetify.generated.Fab
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Fab


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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FabTransition, Any]:
    """Widget for the Vuetify v-fab-transition component, see https://vuetifyjs.com/en/api/v-fab-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FadeTransition, Any]:
    """Widget for the Vuetify v-fade-transition component, see https://vuetifyjs.com/en/api/v-fade-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    append_inner_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    color: str = None,
    details: bool = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    label_id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    model_value: Any = None,
    persistent_clear: bool = None,
    prepend_inner_icon: Any = None,
    reverse: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    single_line: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Field, Any]:
    """Widget for the Vuetify v-field component, see https://vuetifyjs.com/en/api/v-field/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param details: Controls whether the field generates an `aria-describedby` attribute for accessibility.
    :param dirty: Manually apply the dirty state styling.
    :param disabled: Removes the ability to click or target the input.
    :param error: Puts the input in a manual error state.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param reverse: Reverses the orientation.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param single_line: Label does not move on focus/dirty.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FieldLabel, Any]:
    """Widget for the Vuetify v-field-label component, see https://vuetifyjs.com/en/api/v-field-label/
    :param floating: Elevates the label above the slotted content.
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
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    color: str = None,
    counter: bool = None,
    counter_size_string: str = None,
    counter_string: str = None,
    density: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    filter_by_type: str = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_input: bool = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_value: list = [],
    multiple: bool = None,
    name: str = None,
    persistent_clear: bool = None,
    persistent_hint: bool = None,
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
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
    tile: bool = None,
    tooltip: str = None,
    truncate_length: typing.Union[str, float] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FileInput, Any]:
    """Widget for the Vuetify v-file-input component, see https://vuetifyjs.com/en/api/v-file-input/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param chips: Changes display of selections to chips.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param counter: Displays the number of selected files.
    :param counter_size_string: The text displayed when using the **counter** and **show-size** props. Can also be customized globally on the [internationalization page](https://vuetifyjs.com/en/customization/internationalization).
    :param counter_string: The text displayed when using the **counter** prop. Can also be customized globally on the [internationalization page](https://vuetifyjs.com/en/customization/internationalization).
    :param density: Adjusts the vertical height used by the component.
    :param dirty: Manually apply the dirty state styling.
    :param disabled: Removes the ability to click or target the input.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param filter_by_type: Make the input accept only files matched by one or more [unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#Unique_file_type_specifiers). Applies to drag & drop and selecting folders. Emits `rejected` event when some files do not pass through to make it possible to notify user and deliver better user experience.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_input: Display the icon only without the input (file names).
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-file-input/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Adds the **multiple** attribute to the input, allowing multiple file selections.
    :param name: Sets the component's name attribute.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-file-input/#props-hint) to always be visible.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param readonly: Puts input in readonly state.
    :param reverse: Reverses the orientation.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param show_size: Sets the displayed size of selected file(s). When using **true** will default to _1000_ displaying (**kB, MB, GB**) while _1024_ will display (**KiB, MiB, GiB**).
    :param single_line: Label does not move on focus/dirty.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param truncate_length: The length of a filename before it is truncated with ellipsis.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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


def _FileUpload(
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    browse_text: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clearable: bool = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    divider_text: str = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    filter_by_type: str = None,
    focused: bool = None,
    glow: bool = None,
    hide_browse: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon: Any = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    inset_file_list: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_value: list = [],
    multiple: bool = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    rules: list = [],
    scrim: typing.Union[str, bool] = None,
    show_size: bool = None,
    slot: str = None,
    style_: str = None,
    subtitle: str = None,
    tabbable: bool = None,
    theme: str = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FileUpload, Any]:
    """Widget for the Vuetify v-file-upload component, see https://vuetifyjs.com/en/api/v-file-upload/
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param browse_text: Text for the browse button.
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param divider_text: Text in the divider.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param filter_by_type: Make the input accept only files matched by one or more [unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#Unique_file_type_specifiers). Applies to drag & drop and selecting folders. Emits `rejected` event when some files do not pass through to make it possible to notify user and deliver better user experience.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the input is focused and apply color.
    :param hide_browse: Hides the browse button.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-file-upload/#props-persistent-hint) property.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param inset_file_list: Renders the file list inside the dropzone container instead of below it.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows multiple files to be uploaded.
    :param name: Sets the component's name attribute.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-file-upload/#props-hint) to always be visible.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param readonly: Puts input in readonly state.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param scrim: Determines whether an overlay is used when hovering over the component with files. Accepts true/false to enable background, and string to define color.
    :param show_size: Shows the size of the file.
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param width: Sets the width for the component.
    """
    ...


@implements(_FileUpload)
def FileUpload(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.FileUpload
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _FileUpload


def _FileUploadDropzone(
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    browse_text: str = None,
    children: list = [],
    class_: str = None,
    clearable: bool = None,
    close_delay: typing.Union[str, float] = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    divider_text: str = None,
    elevation: typing.Union[str, float] = None,
    error: bool = None,
    height: typing.Union[str, float] = None,
    hide_browse: bool = None,
    icon: Any = None,
    inset_file_list: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: typing.Union[str, float] = None,
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: list = [],
    multiple: bool = None,
    opacity: typing.Union[str, float] = None,
    open_delay: typing.Union[str, float] = None,
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    scrim: typing.Union[str, bool] = None,
    show_size: bool = None,
    slot: str = None,
    style_: str = None,
    subtitle: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    thickness: typing.Union[str, float] = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FileUploadDropzone, Any]:
    """Widget for the Vuetify v-file-upload-dropzone component, see https://vuetifyjs.com/en/api/v-file-upload-dropzone/
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param browse_text: Text for the browse button.
    :param clearable: Allows for the component to be cleared.
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param divider_text: Text in the divider.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param error: Puts the dropzone in an error state, changing the border color.
    :param height: Sets the height for the component.
    :param hide_browse: Hides the browse button.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param inset_file_list: Renders the file list inside the dropzone container instead of below it.
    :param length: Sets the dividers length. Default unit is px.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows multiple files to be uploaded.
    :param opacity: Sets the component's opacity value
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :param position: Sets the position for the component.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param scrim: Determines whether an overlay is used when hovering over the component with files. Accepts true/false to enable background, and string to define color.
    :param show_size: Shows the size of the file.
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param thickness: Sets the dividers thickness. Default unit is px.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
    """
    ...


@implements(_FileUploadDropzone)
def FileUploadDropzone(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.FileUploadDropzone
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _FileUploadDropzone


def _FileUploadItem(
    active: bool = None,
    active_class: str = None,
    active_color: str = None,
    append_avatar: str = None,
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    clearable: bool = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    exact: bool = None,
    file: Any = None,
    file_icon: str = None,
    height: typing.Union[str, float] = None,
    href: str = None,
    index: float = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: typing.Union[bool, str, str, str] = None,
    link: bool = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    nav: bool = None,
    prepend_avatar: str = None,
    prepend_gap: typing.Union[str, float] = None,
    prepend_icon: Any = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    show_size: bool = None,
    slim: bool = None,
    slot: str = None,
    style_: str = None,
    subtitle: typing.Union[str, float, bool] = None,
    tabbable: bool = None,
    tabindex: typing.Union[str, float] = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: typing.Union[str, float, bool] = None,
    to: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FileUploadItem, Any]:
    """Widget for the Vuetify v-file-upload-item component, see https://vuetifyjs.com/en/api/v-file-upload-item/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param active_class: The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.
    :param active_color: Deprecated, use `color` instead.
    :param append_avatar: Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control when in an **active** state or **input-value** is **true** - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors),
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param file: The file object uploaded
    :param file_icon: The icon prepending each uploaded file. This will be a preview image if the file is an image.
    :param height: Sets the height for the component.
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param index: The index of the file in the upload list.
    :param lines: The line declaration specifies the minimum height of the item and can also be controlled from v-list with the same prop.
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param nav: Reduces the width v-list-item takes up as well as adding a border radius.
    :param prepend_avatar: Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param show_size: Show the size of the file
    :param slim: Reduces horizontal spacing for badges, icons, tooltips, and avatars to create a more compact visual representation.
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param tabindex: Controls the tabindex of the list item. When set, overrides the default tabindex behavior. Automatically set to -1 by VList when using `navigationStrategy="track"` to prevent Tab key navigation into items.
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Generates a `v-list-item-title` component with the supplied value. Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title) attribute, that must be set with `v-bind:title.attr` instead.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param value: The value used for selection. Obtained from [`v-list`](https://vuetifyjs.com/en/api/v-list)'s `v-model:selected` when the item is selected.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
    """
    ...


@implements(_FileUploadItem)
def FileUploadItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.FileUploadItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _FileUploadItem


def _FileUploadList(
    activatable: bool = None,
    activated: Any = None,
    active_class: str = None,
    active_color: str = None,
    active_strategy: str = None,
    attributes: dict = {},
    base_color: str = None,
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    clearable: bool = None,
    collapse_icon: Any = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    expand_icon: Any = None,
    files: list = [],
    filterable: bool = None,
    height: typing.Union[str, float] = None,
    indent: typing.Union[str, float] = None,
    item_children: str = None,
    item_props: str = None,
    item_title: str = None,
    item_type: str = None,
    item_value: str = None,
    items: list = [],
    items_registration: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: typing.Union[bool, str, str, str] = None,
    mandatory: bool = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    nav: bool = None,
    navigation_index: float = None,
    navigation_strategy: str = None,
    open_strategy: str = None,
    opened: Any = None,
    prepend_gap: typing.Union[str, float] = None,
    return_object: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    select_strategy: str = None,
    selectable: bool = None,
    selected: Any = None,
    show_size: bool = None,
    slim: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.FileUploadList, Any]:
    """Widget for the Vuetify v-file-upload-list component, see https://vuetifyjs.com/en/api/v-file-upload-list/
    :param activatable: Designates whether the list items are activatable. Additionally, sets necessary accessibility attributes internally.
    :param activated: Array of ids of activated nodes.
    :param active_class: The class applied to the component when it is in an active state.
    :param active_color: Deprecated, use `color` instead.
    :param active_strategy: Affects how items with children behave when activated. If not specified, the **single-independent** strategy will be used.
    - **leaf:** Only leaf nodes (items without children) can be activated.
    - **single-leaf:** Similar as **leaf**, but only a single item can be activated at a time.
    - **independent:** All nodes can be activated whether they have children or not.
    - **single-independent:** Similar as **independent**, but only a single item can be activated at a time.
    :param base_color: Sets the color of component when not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param clearable: Allows for the component to be cleared.
    :param collapse_icon: Icon to display when the list item is expanded.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Puts all children inputs into a disabled state.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param expand_icon: Icon to display when the list item is collapsed.
    :param files: An array of File objects to display in the list. When used inside a VFileUpload, this is provided automatically via injection.
    :param filterable: **FOR INTERNAL USE ONLY** Prevents list item selection using [space] key and pass it back to the text input. Used internally for VAutocomplete and VCombobox.
    :param height: Sets the height for the component.
    :param indent: Overrides the indent size for nested groups.
    :param item_children: Property on supplied `items` that contains its children.
    :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
    :param item_title: Property on supplied `items` that contains its title.
    :param item_type: Designates the key on the supplied items that is used for determining the nodes type.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: Can be an array of objects or strings. By default objects should have a **title** property, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props), a **value** property to allow selection, and a **children** property containing more item objects. Keys to use for these can be changed with the **item-title**, **item-value**, **item-props**, and **item-children** props.
    :param items_registration: When set to 'props', skips rendering collapsed items/nodes (for significant performance gains).
    :param lines: Designates a **minimum-height** for all children `v-list-item` components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp) and is not supported in all browsers.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param nav: An alternative styling that reduces `v-list-item` width and rounds the corners. Typically used with **[v-navigation-drawer](https://vuetifyjs.com/en/components/navigation-drawers)**.
    :param navigation_index: Specifies the currently selected navigation index when using `navigationStrategy="track"`. Can be used with `v-model:navigationIndex` for two-way binding. Items at this index receive visual keyboard focus styling and automatic scrolling. Note: Only works with the `items` prop, not with slotted items.
    :param navigation_strategy: Determines keyboard navigation behavior. **focus** (default) moves DOM focus to items, suitable for traditional lists. **track** provides visual keyboard focus without moving DOM focus, ideal for command palettes and autocomplete where an external element retains focus. When track mode is active, items automatically receive `tabindex="-1"`, proper `aria-activedescendant` is set on the list container, and keyboard-focused items display focus-visible styling with auto-scrolling.
    :param open_strategy: Affects how items with children behave when expanded.
    - **multiple:** Any number of groups can be open at once.
    - **single:** Only one group at each level can be open, opening a group will cause others to close.
    - **list:** Multiple, but all other groups will close when an item is selected.
    :param opened: An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`.
    :param prepend_gap: Sets the horizontal spacing between prepend slot and the main content within list item. Also affects indent to ensure expected alignment of group children.
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param select_strategy: Affects how items with children behave when selected.
    - **leaf:** Only leaf nodes (items without children) can be selected.
    - **independent:** All nodes can be selected whether they have children or not.
    - **classic:** Selecting a parent node will cause all children to be selected, parent nodes will be displayed as selected if all their descendants are selected. Only leaf nodes will be added to the model.
    - **trunk**: Same as classic but if all of a node's children are selected then only that node will be added to the model.
    - **branch**: Same as classic but if any of a node's children are selected then that node will also be added to the model.
    :param selectable: Designates whether the list items are selectable. Additionally, sets necessary accessibility attributes internally.
    :param selected: An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`.
    :param show_size: Shows the size of each file.
    :param slim: Reduces horizontal spacing for badges, icons, tooltips, and avatars within slim list items to create a more compact visual representation.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
    """
    ...


@implements(_FileUploadList)
def FileUploadList(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.FileUploadList
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _FileUploadList


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
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Footer, Any]:
    """Widget for the Vuetify v-footer component, see https://vuetifyjs.com/en/api/v-footer/
    :param absolute: Applies **position: absolute** to the component.
    :param app: Determines the position of the footer. If true, the footer would be given a fixed position at the bottom of the viewport. If false, the footer is set to the bottom of the page.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param height: Sets the height for the component.
    :param name: Assign a specific name for layout registration.
    :param order: Adjust the order of the component in relation to its registration order.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Form, Any]:
    """Widget for the Vuetify v-form component, see https://vuetifyjs.com/en/api/v-form/
    :param disabled: Puts all children inputs into a disabled state.
    :param fast_fail: Stop validation as soon as any rules fail.
    :param model_value: The value representing the validity of the form. If the value is `null` then no validation has taken place yet, or the form has been reset. Otherwise the value will be a `boolean` that indicates if validation has passed or not.
    :param readonly: Puts all children inputs into a readonly state.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param validate_on: Changes the events in which validation occurs.
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


def _Hotkey(
    attributes: dict = {},
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    display_mode: str = None,
    elevation: typing.Union[str, float] = None,
    inline: bool = None,
    key_map: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    platform: str = None,
    prefix: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    suffix: str = None,
    tabbable: bool = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Hotkey, Any]:
    """Widget for the Vuetify v-hotkey component, see https://vuetifyjs.com/en/api/v-hotkey/
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Applies a disabled visual state to the component.
    :param display_mode: Controls how keyboard keys are visually represented. Affects the entire component's appearance:
    - **icon:** Uses SVG icons for keys when appropriate (default)
    - **symbol:** Uses Unicode symbols (⌘, ⌃, ⇧, ⌥) - Allows you to manage presentation of modifier keys with fonts
    - **text:** Uses full text labels (Command, Control, Shift, Alt) - most accessible and descriptive
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param inline: Optimizes the component for seamless integration within text content and documentation. Applies compact styling with baseline alignment, constrained height (1lh), and responsive typography that inherits from parent text. Ideal for help documentation, tooltips, and instructional content. When using multiple inline hotkeys in the same paragraph, increase line-height to prevent visual overlap on text wrapping.
    :param key_map: Custom key mapping object that defines how individual keys should be displayed. Users can import and modify the exported `hotkeyMap` to create custom configurations. Each key maps to a `PlatformKeyConfig` object with:

    ```typescript
    {
      mac?: { symbol?: string, icon?: string, text: string },
      default: { symbol?: string, icon?: string, text: string }
    }
    ```

    **Usage Example:**
    ```typescript
    import { hotkeyMap } from 'vuetify/labs/VHotkey'

    const customKeyMap = {
      ...hotkeyMap,
      'custom-key': {
        default: { text: 'Custom', icon: 'custom-icon' },
        mac: { text: 'Custom', symbol: '⚡' }
      }
    }
    ```

    This enables:
    - **Custom key definitions:** Add support for application-specific keys
    - **Localization:** Override text representations for different languages
    - **Brand customization:** Change how modifier keys appear
    - **Platform-specific styling:** Different representations for Mac vs other platforms

    Recommended to set at the application level via component defaults rather than per-instance for consistency.
    :param platform: Controls platform-specific rendering behavior for keyboard shortcuts. Accepts three values:
    - **`'auto'` (default):** Automatically detects the user's platform based on user agent and renders appropriately
    - **`'mac'`:** Forces Mac-style rendering (Command symbols, icons, Option key, etc.)
    - **`'pc'`:** Forces PC-style rendering (Ctrl text, Alt key, etc.)

    This is particularly useful for:
    - **Cross-platform testing:** Verify how shortcuts appear on different platforms
    - **Design consistency:** Ensure specific platform rendering in demos and prototypes
    - **Development workflow:** Test platform-specific behaviors without switching devices
    - **Documentation:** Show platform-specific examples in help content
    :param prefix: Text to display before the hotkey.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param suffix: Text to display after the hotkey.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param variant: Controls the visual style and presentation of the hotkey component. Supports standard Vuetify variants plus a special contained variant:

    **Standard Variants** (apply styling to individual key elements):
    - **elevated (default):** Raised appearance with shadow, good for standalone hotkey displays
    - **flat:** Solid background without shadow, clean and minimal
    - **tonal:** Subtle tinted background without border, balances visibility with restraint
    - **outlined:** Border-only styling without elevation, lightweight and unobtrusive
    - **text:** Minimal styling with text color emphasis only, blends with content
    - **plain:** No background or border, most subtle option

    **Special Variant** (different visual structure):
    - **contained:** Follows MDN's nested `<kbd>` pattern - wraps all keys in a single styled container with unstyled nested elements. Creates a cohesive visual unit that clearly groups related keys together. Cannot be combined with standard variants. Ideal for complex key combinations where you want to show the entire sequence as one unit.
    """
    ...


@implements(_Hotkey)
def Hotkey(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Hotkey
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Hotkey


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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Hover, Any]:
    """Widget for the Vuetify v-hover component, see https://vuetifyjs.com/en/api/v-hover/
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param disabled: Removes hover functionality.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
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
    v_bind: str = None,
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
    disabled: bool = None,
    end: bool = None,
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    opacity: typing.Union[str, float] = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    start: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Icon, Any]:
    """Widget for the Vuetify v-icon component, see https://vuetifyjs.com/en/api/v-icon/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param end: Applies margin at the start of the component.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param opacity: Sets the component's opacity value
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param start: Applies margin at the end of the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
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


def _IconBtn(
    active: bool = None,
    active_color: str = None,
    active_icon: Any = None,
    active_variant: str = None,
    attributes: dict = {},
    base_variant: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    hide_overlay: bool = None,
    icon: Any = None,
    icon_color: str = None,
    icon_size: typing.Union[str, float] = None,
    icon_sizes: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: bool = None,
    opacity: typing.Union[str, float] = None,
    readonly: bool = None,
    rotate: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    size: typing.Union[str, float] = None,
    sizes: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: typing.Union[str, float, bool] = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.IconBtn, Any]:
    """Widget for the Vuetify v-icon-btn component, see https://vuetifyjs.com/en/api/v-icon-btn/
    :param active: When undefined (default), the component utilizes its default variant, otherwise it will use the activeVariant if active is true, or the baseVariant if active is false.
    :param active_color: The applied color when the component is in an active state.
    :param active_icon: When active is a boolean, this icon is used when active is true.
    :param active_variant: When active is a boolean, this variant is used when active is true.
    :param base_variant: When active is a boolean, this variant is used when active is false.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param height: Sets the height for the component.
    :param hide_overlay: Hides overlay from being displayed when active or focused.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param icon_color: Explicit color applied to the icon.
    :param icon_size: The specific size of the icon, can use named sizes.
    :param icon_sizes: An array of tuples that define the icon sizes for each named size.
    :param loading: Displays circular progress bar in place of the icon.
    :param opacity: Sets the component's opacity value
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :param rotate: The rotation of the icon in degrees.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param size: Sets the height and width of the component.
    :param sizes: An array of tuples that define the button sizes for each named size.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
    """
    ...


@implements(_IconBtn)
def IconBtn(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.IconBtn
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _IconBtn


def _Img(
    absolute: bool = None,
    alt: str = None,
    aspect_ratio: typing.Union[str, float] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    content_class: Any = None,
    cover: bool = None,
    crossorigin: str = None,
    draggable: typing.Union[bool, str, str] = None,
    eager: bool = None,
    gradient: str = None,
    height: typing.Union[str, float] = None,
    image_class: Any = None,
    inline: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lazy_src: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    options: Any = None,
    position: str = None,
    referrerpolicy: str = None,
    rounded: typing.Union[str, float, bool] = None,
    sizes: str = None,
    slot: str = None,
    src: typing.Union[str, dict] = None,
    srcset: str = None,
    style_: str = None,
    tabbable: bool = None,
    tile: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Img, Any]:
    """Widget for the Vuetify v-img component, see https://vuetifyjs.com/en/api/v-img/
    :param absolute: Applies position: absolute to the component.
    :param alt: Alternate text for screen readers. Leave empty for decorative images.
    :param aspect_ratio: Calculated as `width/height`, so for a 1920x1080px image this will be `1.7778`. Will be calculated automatically if omitted.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param content_class: Apply a custom class to the internal content element.
    :param cover: Resizes the background image to cover the entire container.
    :param crossorigin: Specify that images should be fetched with CORS enabled [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#crossorigin)
    :param draggable: Controls the `draggable` behavior of the image. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable).
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param gradient: The gradient to apply to the image. Only supports [linear-gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient) syntax, anything else should be done with classes.
    :param height: Sets the height for the component.
    :param image_class: Applies CSS classes to the inner `<img>` element.
    :param inline: Display as an inline element instead of a block, also disables flex-grow.
    :param lazy_src: Something to show while waiting for the main image to load, typically a small base64-encoded thumbnail. Has a slight blur filter applied.
    NOTE: This prop has no effect unless either `height` or `aspect-ratio` are provided.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param options: Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) constructor.
    :param position: Applies [object-position](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position) styles to the image and placeholder elements.
    :param referrerpolicy: Define which referrer is sent when fetching the resource [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#referrerpolicy)
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param sizes: For use with `srcset`, see [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes).
    :param src: The image URL. This prop is mandatory.
    :param srcset: A set of alternate images to use based on device size. [Read more...](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset).
    :param tabbable: Is widget tabbable?
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param transition: The transition to use when switching from `lazy-src` to `src`. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param width: Sets the width for the component.
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
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.InfiniteScroll, Any]:
    """Widget for the Vuetify v-infinite-scroll component, see https://vuetifyjs.com/en/api/v-infinite-scroll/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param direction: Specifies if scroller is **vertical** or **horizontal**.
    :param empty_text: Text shown when there is no more content to load.
    :param height: Sets the height for the component.
    :param load_more_text: Text shown in default load more button, when in manual mode.
    :param margin: Value sent to the intersection observer. Will make the observer trigger earlier, by the margin (px) value supplied.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param mode: Specifies if content should load automatically when scrolling (**intersect**) or manually (**manual**).
    :param side: Specifies the side where new content should appear. Either the **start**, **end**, or **both** sides.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_value: Any = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Input, Any]:
    """Widget for the Vuetify v-input component, see https://vuetifyjs.com/en/api/v-input/
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param direction: Changes the direction of the input.
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the input is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-input/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-input/#props-hint) to always be visible.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param readonly: Puts input in readonly state.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Item, Any]:
    """Widget for the Vuetify v-item component, see https://vuetifyjs.com/en/api/v-item/
    :param disabled: Removes the ability to click or target the component.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
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
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ItemGroup, Any]:
    """Widget for the Vuetify v-item-group component, see https://vuetifyjs.com/en/api/v-item-group/
    :param disabled: Puts all children components into a disabled state.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows one to select multiple items.
    :param selected_class: Configure the selected CSS class. This class will be available in `v-item` default scoped slot.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
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
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    elevation: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Kbd, Any]:
    """Widget for the Vuetify v-kbd component, see https://vuetifyjs.com/en/api/v-kbd/
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
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
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Label, Any]:
    """Widget for the Vuetify v-label component, see https://vuetifyjs.com/en/api/v-label/
    :param tabbable: Is widget tabbable?
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
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
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    overlaps: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Layout, Any]:
    """Widget for the Vuetify v-layout component, see https://vuetifyjs.com/en/api/v-layout/
    :param full_height: Sets the component height to 100%.
    :param height: Sets the height for the component.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param overlaps: **FOR INTERNAL USE ONLY**
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.LayoutItem, Any]:
    """Widget for the Vuetify v-layout-item component, see https://vuetifyjs.com/en/api/v-layout-item/
    :param absolute: Applies **position: absolute** to the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Assign a specific name for layout registration.
    :param order: Adjust the order of the component in relation to its registration order.
    :param position: The position of the item.
    :param size: Sets the height and width of the component.
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
    options: Any = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Lazy, Any]:
    """Widget for the Vuetify v-lazy component, see https://vuetifyjs.com/en/api/v-lazy/
    :param height: Sets the height for the component.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param options: Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) constructor.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param width: Sets the width for the component.
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
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.LigatureIcon, Any]:
    """Widget for the Vuetify v-ligature-icon component, see https://vuetifyjs.com/en/api/v-ligature-icon/
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    activatable: bool = None,
    activated: Any = None,
    active_class: str = None,
    active_color: str = None,
    active_strategy: str = None,
    attributes: dict = {},
    base_color: str = None,
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    expand_icon: Any = None,
    filterable: bool = None,
    height: typing.Union[str, float] = None,
    indent: typing.Union[str, float] = None,
    item_children: str = None,
    item_props: str = None,
    item_title: str = None,
    item_type: str = None,
    item_value: str = None,
    items: list = [],
    items_registration: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: typing.Union[bool, str, str, str] = None,
    mandatory: bool = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    nav: bool = None,
    navigation_index: float = None,
    navigation_strategy: str = None,
    open_strategy: str = None,
    opened: Any = None,
    prepend_gap: typing.Union[str, float] = None,
    return_object: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    select_strategy: str = None,
    selectable: bool = None,
    selected: Any = None,
    slim: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.List, Any]:
    """Widget for the Vuetify v-list component, see https://vuetifyjs.com/en/api/v-list/
    :param activatable: Designates whether the list items are activatable. Additionally, sets necessary accessibility attributes internally.
    :param activated: Array of ids of activated nodes.
    :param active_class: The class applied to the component when it is in an active state.
    :param active_color: Deprecated, use `color` instead.
    :param active_strategy: Affects how items with children behave when activated. If not specified, the **single-independent** strategy will be used.
    - **leaf:** Only leaf nodes (items without children) can be activated.
    - **single-leaf:** Similar as **leaf**, but only a single item can be activated at a time.
    - **independent:** All nodes can be activated whether they have children or not.
    - **single-independent:** Similar as **independent**, but only a single item can be activated at a time.
    :param base_color: Sets the color of component when not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param collapse_icon: Icon to display when the list item is expanded.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Puts all children inputs into a disabled state.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param expand_icon: Icon to display when the list item is collapsed.
    :param filterable: **FOR INTERNAL USE ONLY** Prevents list item selection using [space] key and pass it back to the text input. Used internally for VAutocomplete and VCombobox.
    :param height: Sets the height for the component.
    :param indent: Overrides the indent size for nested groups.
    :param item_children: Property on supplied `items` that contains its children.
    :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
    :param item_title: Property on supplied `items` that contains its title.
    :param item_type: Designates the key on the supplied items that is used for determining the nodes type.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: Can be an array of objects or strings. By default objects should have a **title** property, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props), a **value** property to allow selection, and a **children** property containing more item objects. Keys to use for these can be changed with the **item-title**, **item-value**, **item-props**, and **item-children** props.
    :param items_registration: When set to 'props', skips rendering collapsed items/nodes (for significant performance gains).
    :param lines: Designates a **minimum-height** for all children `v-list-item` components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp) and is not supported in all browsers.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param nav: An alternative styling that reduces `v-list-item` width and rounds the corners. Typically used with **[v-navigation-drawer](https://vuetifyjs.com/en/components/navigation-drawers)**.
    :param navigation_index: Specifies the currently selected navigation index when using `navigationStrategy="track"`. Can be used with `v-model:navigationIndex` for two-way binding. Items at this index receive visual keyboard focus styling and automatic scrolling. Note: Only works with the `items` prop, not with slotted items.
    :param navigation_strategy: Determines keyboard navigation behavior. **focus** (default) moves DOM focus to items, suitable for traditional lists. **track** provides visual keyboard focus without moving DOM focus, ideal for command palettes and autocomplete where an external element retains focus. When track mode is active, items automatically receive `tabindex="-1"`, proper `aria-activedescendant` is set on the list container, and keyboard-focused items display focus-visible styling with auto-scrolling.
    :param open_strategy: Affects how items with children behave when expanded.
    - **multiple:** Any number of groups can be open at once.
    - **single:** Only one group at each level can be open, opening a group will cause others to close.
    - **list:** Multiple, but all other groups will close when an item is selected.
    :param opened: An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`.
    :param prepend_gap: Sets the horizontal spacing between prepend slot and the main content within list item. Also affects indent to ensure expected alignment of group children.
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param select_strategy: Affects how items with children behave when selected.
    - **leaf:** Only leaf nodes (items without children) can be selected.
    - **independent:** All nodes can be selected whether they have children or not.
    - **classic:** Selecting a parent node will cause all children to be selected, parent nodes will be displayed as selected if all their descendants are selected. Only leaf nodes will be added to the model.
    - **trunk**: Same as classic but if all of a node's children are selected then only that node will be added to the model.
    - **branch**: Same as classic but if any of a node's children are selected then that node will also be added to the model.
    :param selectable: Designates whether the list items are selectable. Additionally, sets necessary accessibility attributes internally.
    :param selected: An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`.
    :param slim: Reduces horizontal spacing for badges, icons, tooltips, and avatars within slim list items to create a more compact visual representation.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    disabled: bool = None,
    expand_icon: Any = None,
    fluid: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    prepend_icon: Any = None,
    raw_id: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    subgroup: bool = None,
    tabbable: bool = None,
    tag: Any = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListGroup, Any]:
    """Widget for the Vuetify v-list-group component, see https://vuetifyjs.com/en/api/v-list-group/
    :param active_color: Deprecated, use `color` instead.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param collapse_icon: Icon to display when the list item is expanded.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Puts all children inputs into a disabled state.
    :param expand_icon: Icon to display when the list item is collapsed.
    :param fluid: Removes the left padding assigned for action icons from group items.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param raw_id: Defines the root element's id attribute in the component. If it is provided, the id attribute will be dynamically generated in the format: "v-list-group--id-[rawId]".
    :param subgroup: Designate the component as nested list group.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param value: Expands / Collapse the list-group.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListImg, Any]:
    """Widget for the Vuetify v-list-img component, see https://vuetifyjs.com/en/api/v-list-img/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    append_icon: Any = None,
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
    index: float = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: typing.Union[bool, str, str, str] = None,
    link: bool = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    nav: bool = None,
    prepend_avatar: str = None,
    prepend_gap: typing.Union[str, float] = None,
    prepend_icon: Any = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    slim: bool = None,
    slot: str = None,
    style_: str = None,
    subtitle: typing.Union[str, float, bool] = None,
    tabbable: bool = None,
    tabindex: typing.Union[str, float] = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: typing.Union[str, float, bool] = None,
    to: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItem, Any]:
    """Widget for the Vuetify v-list-item component, see https://vuetifyjs.com/en/api/v-list-item/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param active_class: The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.
    :param active_color: Deprecated, use `color` instead.
    :param append_avatar: Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control when in an **active** state or **input-value** is **true** - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors),
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param height: Sets the height for the component.
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param lines: The line declaration specifies the minimum height of the item and can also be controlled from v-list with the same prop.
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param nav: Reduces the width v-list-item takes up as well as adding a border radius.
    :param prepend_avatar: Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param slim: Reduces horizontal spacing for badges, icons, tooltips, and avatars to create a more compact visual representation.
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param tabindex: Controls the tabindex of the list item. When set, overrides the default tabindex behavior. Automatically set to -1 by VList when using `navigationStrategy="track"` to prevent Tab key navigation into items.
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Generates a `v-list-item-title` component with the supplied value. Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title) attribute, that must be set with `v-bind:title.attr` instead.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param value: The value used for selection. Obtained from [`v-list`](https://vuetifyjs.com/en/api/v-list)'s `v-model:selected` when the item is selected.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemAction, Any]:
    """Widget for the Vuetify v-list-item-action component, see https://vuetifyjs.com/en/api/v-list-item-action/
    :param end: Applies margin at the start of the component.
    :param start: Applies margin at the end of the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemMedia, Any]:
    """Widget for the Vuetify v-list-item-media component, see https://vuetifyjs.com/en/api/v-list-item-media/
    :param end: Applies margin at the start of the component.
    :param start: Applies margin at the end of the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    opacity: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemSubtitle, Any]:
    """Widget for the Vuetify v-list-item-subtitle component, see https://vuetifyjs.com/en/api/v-list-item-subtitle/
    :param opacity: Sets the component's opacity value
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListItemTitle, Any]:
    """Widget for the Vuetify v-list-item-title component, see https://vuetifyjs.com/en/api/v-list-item-title/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    tag: Any = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ListSubheader, Any]:
    """Widget for the Vuetify v-list-subheader component, see https://vuetifyjs.com/en/api/v-list-subheader/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param inset: Insets the subheader without additional spacing, aligning it flush with the surrounding content.
    :param sticky: Sticks the header to the top of the table.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param title: Specify a title text for the component.
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
    messages: Any = None,
    rtl: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.LocaleProvider, Any]:
    """Widget for the Vuetify v-locale-provider component, see https://vuetifyjs.com/en/api/v-locale-provider/
    :param fallback_locale: Specify a fallback locale to use when a locale is not found.
    :param locale: Specify a locale to use.
    :param messages: Displays a list of messages or a single message if using a string.
    :param rtl: Specify a RTL mode.
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
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Main, Any]:
    """Widget for the Vuetify v-main component, see https://vuetifyjs.com/en/api/v-main/
    :param height: Sets the height for the component.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param scrollable: Specify a custom scrollable function.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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


def _MaskInput(
    active: bool = None,
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    density: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    mask: typing.Union[str, dict] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_modifiers: Any = None,
    model_value: Any = None,
    name: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
    readonly: bool = None,
    return_masked_value: bool = None,
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
    tile: bool = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.MaskInput, Any]:
    """Widget for the Vuetify v-mask-input component, see https://vuetifyjs.com/en/api/v-mask-input/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: Enables autofocus.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Function returns the counter display text.
    :param density: Adjusts the vertical height used by the component.
    :param dirty: Manually apply the dirty state styling.
    :param disabled: Removes the ability to click or target the input.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-mask-input/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param mask: Apply a mask to the input. See [guide](https://vuetifyjs.com/en/components/mask-inputs/#guide) for more information.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-mask-input/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param placeholder: Sets the input’s placeholder text.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param readonly: Puts input in readonly state.
    :param return_masked_value: Returns the unmodified masked string.
    :param reverse: Reverses the orientation.
    :param role: The role attribute applied to the input.
    :param rounded: Adds a border radius to the input.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param single_line: Label does not move on focus/dirty.
    :param suffix: Displays suffix text.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param type: Sets input type.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
    """
    ...


@implements(_MaskInput)
def MaskInput(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.MaskInput
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _MaskInput


def _Menu(
    activator: str = None,
    activator_props: Any = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    capture_focus: bool = None,
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disable_initial_focus: bool = None,
    disabled: bool = None,
    eager: bool = None,
    height: typing.Union[str, float] = None,
    id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    retain_focus: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    slot: str = None,
    stick_to_target: bool = None,
    style_: str = None,
    submenu: bool = None,
    tabbable: bool = None,
    target: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    viewport_margin: typing.Union[str, float] = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Menu, Any]:
    """Widget for the Vuetify v-menu component, see https://vuetifyjs.com/en/api/v-menu/
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default. Generally not recommended except as a last resort: the default positioning algorithm should handle most scenarios better than is possible without teleporting, and you may have unexpected behavior if the menu ends up as child of its activator.
    :param close_delay: Milliseconds to wait before closing component. Only works with the **open-on-hover** prop.
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Designates if menu should close when its content is clicked.
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param disable_initial_focus: Deprecated, use `capture-focus` instead. Prevents automatic redirect of first `focusin` event. Intended to use on permanently open menus or VSpeedDial.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param height: Sets the height for the component.
    :param id: The unique identifier of the component.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component. Use `auto` to use the activator width.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Milliseconds to wait before opening component. Only works with the **open-on-hover** prop.
    :param open_on_click: Designates whether menu should open on activator click.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Designates whether menu should open on activator hover.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :param retain_focus: Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.
    :param scrim: Accepts true/false to enable background, and string to define color.
    :param scroll_strategy: Strategy used when the component is activate and user scrolls.
    :param stick_to_target: Enables the overlay content to go off-screen when scrolling.
    :param submenu: Opens with right arrow and closes on left instead of up/down. Implies `location="end"`. Directions are reversed for RTL.
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param viewport_margin: Sets custom viewport margin for the overlay content
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
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
    transition: typing.Union[str, bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Messages, Any]:
    """Widget for the Vuetify v-messages component, see https://vuetifyjs.com/en/api/v-messages/
    :param active: Determines whether the messages are visible or not.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param messages: Displays a list of messages or a single message if using a string.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
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
    capture_focus: bool = None,
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    color: str = None,
    disable_resize_watcher: bool = None,
    disable_route_watcher: bool = None,
    elevation: typing.Union[str, float] = None,
    expand_on_hover: bool = None,
    floating: bool = None,
    image: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: str = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    model_value: bool = None,
    name: str = None,
    open_delay: typing.Union[str, float] = None,
    order: typing.Union[str, float] = None,
    permanent: bool = None,
    persistent: bool = None,
    rail: bool = None,
    rail_width: typing.Union[str, float] = None,
    retain_focus: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    scrim: typing.Union[str, bool] = None,
    slot: str = None,
    sticky: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    temporary: bool = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    touchless: bool = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.NavigationDrawer, Any]:
    """Widget for the Vuetify v-navigation-drawer component, see https://vuetifyjs.com/en/api/v-navigation-drawer/
    :param absolute: Applies **position: absolute** to the component.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disable_resize_watcher: Prevents the automatic opening or closing of the drawer when resized, based on whether the device is mobile or desktop.
    :param disable_route_watcher: Disables opening of navigation drawer when route changes.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param expand_on_hover: Collapses the drawer to a **rail-variant** until hovering with the mouse.
    :param floating: A floating drawer has no visible container (no border-right).
    :param image: Apply a specific background image to the component.
    :param location: Controls the edge of the screen the drawer is attached to.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Sets the designated mobile breakpoint for the component. This will apply alternate styles for mobile devices such as the `temporary` prop, or activate the `bottom` prop when the breakpoint value is met. Setting the value to `0` will disable this functionality.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Assign a specific name for layout registration.
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :param order: Adjust the order of the component in relation to its registration order.
    :param permanent: The drawer remains visible regardless of screen size.
    :param persistent: Clicking outside or pressing **esc** key will not dismiss the dialog.
    :param rail: Sets the component width to the **rail-width** value.
    :param rail_width: Sets the width for the component when `rail` is enabled.
    :param retain_focus: Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param scrim: Determines whether an overlay is used when a **temporary** drawer is open. Accepts true/false to enable background, and string to define color.
    :param sticky: When true, the drawer will remain visible when scrolling past the top of the page.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param temporary: A temporary drawer sits above its application and uses a scrim (overlay) to darken the background.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param touchless: Disable mobile touch functionality.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.NoSsr, Any]:
    """Widget for the Vuetify v-no-ssr component, see https://vuetifyjs.com/en/api/v-no-ssr/
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


def _NumberInput(
    active: bool = None,
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    color: str = None,
    control_variant: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    decimal_separator: str = None,
    density: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_input: bool = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    inset: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max: float = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min: float = None,
    min_fraction_digits: float = None,
    min_width: typing.Union[str, float] = None,
    model_modifiers: Any = None,
    model_value: float = None,
    name: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    precision: float = None,
    prefix: str = None,
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
    readonly: bool = None,
    reverse: bool = None,
    role: str = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    single_line: bool = None,
    slot: str = None,
    step: float = None,
    style_: str = None,
    suffix: str = None,
    tabbable: bool = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.NumberInput, Any]:
    """Widget for the Vuetify v-number-input component, see https://vuetifyjs.com/en/api/v-number-input/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: Enables autofocus.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param control_variant: Controls layout of the stepper buttons.
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Function returns the counter display text.
    :param decimal_separator: Expects single character to be used as decimal separator.
    :param density: Adjusts the vertical height used by the component.
    :param dirty: Manually apply the dirty state styling.
    :param disabled: Removes the ability to click or target the input.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_input: Hide the input field.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-number-input/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param inset: Applies an indentation to the dividers used in the stepper buttons.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max: Specifies the maximum allowable value for the input.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min: Specifies the minimum allowable value for the input.
    :param min_fraction_digits: Specifies the minimum fraction digits to be displayed (capped to `precision`). Defaults to `precision` when not explicitly set.
    :param min_width: Sets the minimum width for the component.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-number-input/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param placeholder: Sets the input’s placeholder text.
    :param precision: Enforces strict precision. It is expected to be an integer value in range between `0` and `15`, or null for unrestricted.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param readonly: Puts input in readonly state.
    :param reverse: Reverses the orientation.
    :param role: The role attribute applied to the input.
    :param rounded: Adds a border radius to the input.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param single_line: Label does not move on focus/dirty.
    :param step: Defines the interval between allowed values when the user increments or decrements the input
    :param suffix: Displays suffix text.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param type: **IGNORED** underlying input is always of type 'text'
    :param validate_on: Change what type of event triggers validation to run.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
    """
    ...


@implements(_NumberInput)
def NumberInput(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.NumberInput
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _NumberInput


def _OtpInput(
    attributes: dict = {},
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
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
    masked: bool = None,
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.OtpInput, Any]:
    """Widget for the Vuetify v-otp-input component, see https://vuetifyjs.com/en/api/v-otp-input/
    :param autofocus: Automatically focuses the first input on page load
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the input.
    :param divider: Specifies the dividing character between items.
    :param error: Puts the input in a manual error state.
    :param focus_all: Puts all inputs into a focus state when any are focused
    :param focused: Forces a focused state styling on the component.
    :param height: Sets the height for the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param length: The OTP field's length.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param masked: Hides the entered characters with bullets, similar to a password input, but makes it possible to also restrict characters to digits with `type="number"`.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param placeholder: Sets the input’s placeholder text.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param type: Supported types: `text`, `password`, `number`.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    activator_props: Any = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    capture_focus: bool = None,
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
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    retain_focus: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    slot: str = None,
    stick_to_target: bool = None,
    style_: str = None,
    tabbable: bool = None,
    target: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    viewport_margin: typing.Union[str, float] = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Overlay, Any]:
    """Widget for the Vuetify v-overlay component, see https://vuetifyjs.com/en/api/v-overlay/
    :param absolute: Applies **position: absolute** to the content element.
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Closes component when you click on its content.
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param height: Sets the height for the component.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :param open_on_click: Activate the component when the activator is clicked.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Activate the component when the activator is hovered.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :param retain_focus: Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.
    :param scrim: Accepts true/false to enable background, and string to define color.
    :param scroll_strategy: Strategy used when the component is activate and user scrolls.
    :param stick_to_target: Enables the overlay content to go off-screen when scrolling.
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param viewport_margin: Sets custom viewport margin for the overlay content
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
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
    first_icon: Any = None,
    last_aria_label: str = None,
    last_icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    length: typing.Union[str, float] = None,
    model_value: float = None,
    next_aria_label: str = None,
    next_icon: Any = None,
    page_aria_label: str = None,
    prev_icon: Any = None,
    previous_aria_label: str = None,
    rounded: typing.Union[str, float, bool] = None,
    show_first_last_page: bool = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    start: typing.Union[str, float] = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    total_visible: typing.Union[str, float] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Pagination, Any]:
    """Widget for the Vuetify v-pagination component, see https://vuetifyjs.com/en/api/v-pagination/
    :param active_color: The applied color when the component is in an active state.
    :param aria_label: Label for the root element.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the selected page button - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param current_page_aria_label: Label for the currently selected page.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param ellipsis: Text to show between page buttons when truncating the list.
    :param first_aria_label: Label for the go to first button.
    :param first_icon: The icon to use for the first button.
    :param last_aria_label: Label for the go to last button.
    :param last_icon: The icon to use for the last button.
    :param length: The number of pages.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param next_aria_label: Label for the next button.
    :param next_icon: The icon to use for the next button.
    :param page_aria_label: Label for each page button.
    :param prev_icon: The icon to use for the prev button.
    :param previous_aria_label: Label for the previous button.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param show_first_last_page: Show buttons for going to first and last page.
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param start: Specify the starting page.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param total_visible: Specify the total visible pagination numbers.
    :param variant: Applies a distinct style to the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Parallax, Any]:
    """Widget for the Vuetify v-parallax component, see https://vuetifyjs.com/en/api/v-parallax/
    :param scale: The scale of the parallax image.
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
    divided: bool = None,
    elevation: typing.Union[str, float] = None,
    height: typing.Union[str, float] = None,
    hide_header: bool = None,
    hide_title: bool = None,
    landscape: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Picker, Any]:
    """Widget for the Vuetify v-picker component, see https://vuetifyjs.com/en/api/v-picker/
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param divided: Adds a divider between the header and controls.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param height: Sets the height for the component.
    :param hide_header: Hide the picker header.
    :param hide_title: Hide the picker title.
    :param landscape: Puts the picker into landscape mode.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param position: Sets the position for the component.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.PickerTitle, Any]:
    """Widget for the Vuetify v-picker-title component, see https://vuetifyjs.com/en/api/v-picker-title/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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


def _Pie(
    animation: typing.Union[bool, dict] = None,
    attributes: dict = {},
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    density: str = None,
    gap: typing.Union[str, float] = None,
    gauge_cut: typing.Union[str, float] = None,
    hide_slice: bool = None,
    hover_scale: typing.Union[str, float] = None,
    inner_cut: typing.Union[str, float] = None,
    item_key: str = None,
    item_title: str = None,
    item_value: str = None,
    items: typing.Union[dict, list] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    legend: typing.Union[bool, dict] = None,
    palette: list = [],
    reveal: typing.Union[bool, dict] = None,
    rotate: typing.Union[str, float] = None,
    rounded: typing.Union[str, float] = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    title: str = None,
    tooltip: typing.Union[bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Pie, Any]:
    """Widget for the Vuetify v-pie component, see https://vuetifyjs.com/en/api/v-pie/
    :param animation: Controls duration and easing of the expand/collapse and hover effect. Defaults to `easeInOutCubic` over 400ms.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param gap: Reduces segment size by a specified angle. Recommended to in range (0-10).
    :param gauge_cut: Allows removing bottom part of the chart to make it into a gauge. Expects angle (0-180).
    :param hide_slice: Makes inner slice invisible instead of semi-transparent.
    :param hover_scale: Enables interactive behavior by reducing segment size until it gets hovered. Expects fraction value (0-0.25).
    :param inner_cut: Specifies inner radius for a donut-style chart as a percent (0-100). Without `hide-slice`, inner slice is visible with translucent color matching the item.
    :param items: Data items expected to contain `key`, `title` and `value`.
    :param legend: Controls legend visibility, position and text format.
    :param palette: Defines colors and patterns to be applied based on the data items order. Data items can also define their colors.
    :param reveal: Enables and controls duration for initial reveal animation. Easing function is shared with `animation` prop.
    :param rotate: Rotates the chart segments clockwise.
    :param rounded: Number passed as corner radius relative to 100x100 SVG viewport
    :param size: Sets the height and width of the chart (excluding title and legend).
    :param tabbable: Is widget tabbable?
    :param title: Specify a title text for the component.
    :param tooltip: Controls tooltip visibility, transition, offset from the cursor and formats of title and subtitle.
    """
    ...


@implements(_Pie)
def Pie(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Pie
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Pie


def _PieSegment(
    active: bool = None,
    animation: typing.Union[bool, dict] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    gap: typing.Union[str, float] = None,
    hide_slice: bool = None,
    hover_scale: typing.Union[str, float] = None,
    inner_cut: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    pattern: str = None,
    reveal: typing.Union[bool, dict] = None,
    rotate: typing.Union[str, float] = None,
    rounded: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: float = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.PieSegment, Any]:
    """Widget for the Vuetify v-pie-segment component, see https://vuetifyjs.com/en/api/v-pie-segment/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param animation: Controls duration and easing of the expand/collapse and hover effect. Defaults to `easeInOutCubic` over 400ms.
    :param color: Sets segment color to be passed straight to CSS style attribute.
    :param gap: Reduces segment size by a specified angle. Recommended to in range (0-10).
    :param hide_slice: Makes inner slice invisible instead of semi-transparent.
    :param hover_scale: Reduces outer radius until segment is hovered. Expects fraction value (0-0.25)
    :param inner_cut: Sets inner slice size in percent (0-100).
    :param pattern: Decal pattern to put on top of the outer slice.
    :param reveal: Enables and controls duration for initial reveal animation. Easing function is shared with `animation` prop.
    :param rotate: Sets segment offset angle.
    :param rounded: Number passed as corner radius relative to 100x100 SVG viewport
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param value: The value used for calculate segment/arc angle size.
    """
    ...


@implements(_PieSegment)
def PieSegment(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.PieSegment
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _PieSegment


def _PieTooltip(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    item: dict = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: bool = None,
    offset: typing.Union[str, float, list] = None,
    slot: str = None,
    style_: str = None,
    subtitle_format: str = None,
    tabbable: bool = None,
    target: list = [],
    title_format: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.PieTooltip, Any]:
    """Widget for the Vuetify v-pie-tooltip component, see https://vuetifyjs.com/en/api/v-pie-tooltip/
    :param item: Data item related to hovered segment
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param subtitle_format: Formatter definition or function. When passed as String macros for `[title]` and `[value]` get replaced dynamically.
    :param tabbable: Is widget tabbable?
    :param title_format: Formatter definition or function. When passed as String macros for `[title]` and `[value]` get replaced dynamically.
    :param tooltip: A tooltip caption.
    :param transition: The transition used when hovering between chart segments
    """
    ...


@implements(_PieTooltip)
def PieTooltip(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.PieTooltip
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _PieTooltip


def _ProgressCircular(
    attributes: dict = {},
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    indeterminate: typing.Union[bool, str] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: typing.Union[str, float] = None,
    reveal: typing.Union[bool, dict] = None,
    rotate: typing.Union[str, float] = None,
    rounded: bool = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ProgressCircular, Any]:
    """Widget for the Vuetify v-progress-circular component, see https://vuetifyjs.com/en/api/v-progress-circular/
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param indeterminate: Constantly animates, use when loading progress is unknown. If set to the string `'disable-shrink'` it will use a simpler animation that does not run on the main thread.
    :param model_value: The percentage value for current progress.
    :param reveal: Animates the progress circle from 0 to its model value when the component mounts.
    :param rotate: Rotates the circle start point in degrees.
    :param rounded: Rounds the ends of the progress arc for a softer appearance. When enabled, the progress stroke will have rounded caps instead of square ends.
    :param size: Sets the diameter of the circle in pixels.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param width: Sets the stroke of the circle in pixels.
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
    buffer_color: str = None,
    buffer_opacity: typing.Union[str, float] = None,
    buffer_value: typing.Union[str, float] = None,
    children: list = [],
    chunk_count: typing.Union[str, float] = None,
    chunk_gap: typing.Union[str, float] = None,
    chunk_width: typing.Union[str, float] = None,
    class_: str = None,
    clickable: bool = None,
    color: str = None,
    height: typing.Union[str, float] = None,
    indeterminate: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    max: typing.Union[str, float] = None,
    model_value: typing.Union[str, float] = None,
    opacity: typing.Union[str, float] = None,
    reverse: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    rounded_bar: bool = None,
    slot: str = None,
    stream: bool = None,
    striped: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ProgressLinear, Any]:
    """Widget for the Vuetify v-progress-linear component, see https://vuetifyjs.com/en/api/v-progress-linear/
    :param absolute: Applies position: absolute to the component.
    :param active: Reduce the height to 0, hiding component.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param bg_opacity: Background opacity, if null it defaults to 0.3 if background color is not specified or 1 otherwise.
    :param buffer_color: Sets the color of the buffer bar.
    :param buffer_opacity: Set the opacity of the buffer bar.
    :param buffer_value: The percentage value for the buffer.
    :param chunk_count: Specifies amount of chunks to divide the bar into.
    :param chunk_gap: Defines size of the gap between chunks.
    :param chunk_width: Defines chunk absolute size. Useful when chunk is narrow.
    :param clickable: Clicking on the progress track will automatically set the value.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param height: Sets the height for the component.
    :param indeterminate: Constantly animates, use when loading progress is unknown.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max: Sets the maximum value the progress can reach.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param opacity: Set the opacity of the progress bar.
    :param reverse: Displays reversed progress (right to left in LTR mode and left to right in RTL).
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param rounded_bar: Applies a border radius to the progress bar.
    :param stream: An alternative style for portraying loading that works in tandem with **buffer-value**.
    :param striped: Adds a stripe background to the filled portion of the progress component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
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


def _PullToRefresh(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    pull_down_threshold: float = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.PullToRefresh, Any]:
    """Widget for the Vuetify v-pull-to-refresh component, see https://vuetifyjs.com/en/api/v-pull-to-refresh/
    :param disabled: Removes the ability to click or target the component.
    :param pull_down_threshold: The distance the user must pull down to trigger a refresh.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_PullToRefresh)
def PullToRefresh(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.PullToRefresh
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _PullToRefresh


def _Radio(
    attributes: dict = {},
    base_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    false_icon: Any = None,
    false_value: Any = None,
    id: str = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: Any = None,
    true_value: Any = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    value_comparator: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Radio, Any]:
    """Widget for the Vuetify v-radio component, see https://vuetifyjs.com/en/api/v-radio/
    :param base_color: Sets the color of the input when it is not focused.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param defaults_target: The target component to provide defaults values for.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param false_icon: The icon used when inactive.
    :param false_value: Sets value for falsy state.
    :param id: Sets the DOM id on the component.
    :param inline: Puts children inputs into a row.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes select to multiple. Accepts array for value.
    :param name: Sets the component's name attribute.
    :param readonly: Puts input in readonly state.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param true_icon: The icon used when active.
    :param true_value: Sets value for truthy state.
    :param type: Provides the default type for children selection controls.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
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
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    false_icon: Any = None,
    focused: bool = None,
    glow: bool = None,
    height: typing.Union[str, float] = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_value: Any = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: Any = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    value_comparator: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.RadioGroup, Any]:
    """Widget for the Vuetify v-radio-group component, see https://vuetifyjs.com/en/api/v-radio-group/
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param defaults_target: The target component to provide defaults values for.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param false_icon: The icon used when inactive.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the input is focused and apply color.
    :param height: Sets the height of the input.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-radio-group/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param inline: Displays radio buttons in row.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-radio-group/#props-hint) to always be visible.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param readonly: Puts input in readonly state.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param true_icon: The icon used when active.
    :param type: Provides the default type for children selection controls.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param width: Sets the width for the component.
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
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
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
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: list = [],
    name: str = None,
    no_keyboard: bool = None,
    persistent_hint: bool = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    reverse: bool = None,
    ripple: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    show_ticks: typing.Union[bool, str] = None,
    slot: str = None,
    step: typing.Union[str, float] = None,
    strict: bool = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    thumb_color: str = None,
    thumb_label: typing.Union[bool, str, str] = None,
    thumb_size: typing.Union[str, float] = None,
    tick_size: typing.Union[str, float] = None,
    ticks: typing.Union[list, dict] = None,
    tile: bool = None,
    tooltip: str = None,
    track_color: str = None,
    track_fill_color: str = None,
    track_size: typing.Union[str, float] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.RangeSlider, Any]:
    """Widget for the Vuetify v-range-slider component, see https://vuetifyjs.com/en/api/v-range-slider/
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param direction: Changes the direction of the input.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the input is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-range-slider/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param max: Sets the maximum allowed value.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min: Sets the minimum allowed value.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param no_keyboard: **FOR INTERNAL USE ONLY** Ignore keyboard events.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-range-slider/#props-hint) to always be visible.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param readonly: Puts input in readonly state.
    :param reverse: Reverses the slider direction.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param show_ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
    :param step: If greater than 0, sets step interval for ticks.
    :param strict: Disallows dragging the ending thumb past the starting thumb and vice versa.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param thumb_color: Sets the thumb and thumb label color.
    :param thumb_label: Show thumb label. If `true` it shows label when using slider. If set to `'always'` it always shows label. (since [v3.12.0](https://vuetifyjs.com/en/getting-started/release-notes/?version=v3.12.0) it supports `'hover'` to show label when hovering over the thumb.
    :param thumb_size: Controls the size of the thumb label.
    :param tick_size: Controls the size of **ticks**
    :param ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param track_color: Sets the track's color
    :param track_fill_color: Sets the track's fill color
    :param track_size: Sets the track's size (height).
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param width: Sets the width for the component.
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
    empty_icon: Any = None,
    full_icon: Any = None,
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
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Rating, Any]:
    """Widget for the Vuetify v-rating component, see https://vuetifyjs.com/en/api/v-rating/
    :param active_color: The applied color when the component is in an active state.
    :param clearable: Allows for the component to be cleared by clicking on the current value.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param empty_icon: The icon displayed when empty.
    :param full_icon: The icon displayed when full.
    :param half_increments: Allows the selection of half increments.
    :param hover: Provides visual feedback when hovering over icons.
    :param item_aria_label: The **aria-label** used for each item.
    :param item_label_position: Position of item labels. Accepts 'top' and 'bottom'.
    :param item_labels: Array of labels to display next to each item..
    :param length: The amount of items to show.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param readonly: Removes all hover effects and pointer events.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
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
    content_class: Any = None,
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Responsive, Any]:
    """Widget for the Vuetify v-responsive component, see https://vuetifyjs.com/en/api/v-responsive/
    :param aspect_ratio: Sets a base aspect ratio, calculated as width/height. This will only set a **minimum** height, the component can still grow if it has a lot of content.
    :param content_class: Apply a custom class to the internal content element.
    :param height: Sets the height for the component.
    :param inline: Display as an inline element instead of a block, also disables flex-grow.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Row, Any]:
    """Widget for the Vuetify v-row component, see https://vuetifyjs.com/en/api/v-row/
    :param align: Applies the [align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) css property. Available options are: **start**, **center**, **end**, **baseline** and **stretch**.
    :param align_content: Applies the [align-content](https://developer.mozilla.org/en-US/docs/Web/CSS/align-content) css property. Available options are: **start**, **center**, **end**, **space-between**, **space-around** and **stretch**.
    :param align_content_lg: Changes the **align-content** property on large and greater breakpoints.
    :param align_content_md: Changes the **align-content** property on medium and greater breakpoints.
    :param align_content_sm: Changes the **align-content** property on small and greater breakpoints.
    :param align_content_xl: Changes the **align-content** property on extra large and greater breakpoints.
    :param align_content_xxl: Changes the **align-content** property on extra extra large and greater breakpoints.
    :param align_lg: Changes the **align-items** property on large and greater breakpoints.
    :param align_md: Changes the **align-items** property on medium and greater breakpoints.
    :param align_sm: Changes the **align-items** property on small and greater breakpoints.
    :param align_xl: Changes the **align-items** property on extra large and greater breakpoints.
    :param align_xxl: Changes the **align-items** property on extra extra large and greater breakpoints.
    :param dense: Reduces the gutter between `v-col`s.
    :param justify: Applies the [justify-content](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content) css property. Available options are: **start**, **center**, **end**, **space-between** and **space-around**.
    :param justify_lg: Changes the **justify-content** property on large and greater breakpoints.
    :param justify_md: Changes the **justify-content** property on medium and greater breakpoints.
    :param justify_sm: Changes the **justify-content** property on small and greater breakpoints.
    :param justify_xl: Changes the **justify-content** property on extra large and greater breakpoints.
    :param justify_xxl: Changes the **justify-content** property on extra extra large and greater breakpoints.
    :param no_gutters: Removes the gutter between `v-col`s.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScaleTransition, Any]:
    """Widget for the Vuetify v-scale-transition component, see https://vuetifyjs.com/en/api/v-scale-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScrollXReverseTransition, Any]:
    """Widget for the Vuetify v-scroll-x-reverse-transition component, see https://vuetifyjs.com/en/api/v-scroll-x-reverse-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScrollXTransition, Any]:
    """Widget for the Vuetify v-scroll-x-transition component, see https://vuetifyjs.com/en/api/v-scroll-x-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScrollYReverseTransition, Any]:
    """Widget for the Vuetify v-scroll-y-reverse-transition component, see https://vuetifyjs.com/en/api/v-scroll-y-reverse-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ScrollYTransition, Any]:
    """Widget for the Vuetify v-scroll-y-transition component, see https://vuetifyjs.com/en/api/v-scroll-y-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    chips: bool = None,
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    closable_chips: bool = None,
    close_text: str = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    custom_filter: Any = None,
    custom_key_filter: Any = None,
    density: str = None,
    disabled: bool = None,
    eager: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_no_data: bool = None,
    hide_selected: bool = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    item_children: str = None,
    item_color: str = None,
    item_props: str = None,
    item_title: str = None,
    item_type: str = None,
    item_value: str = None,
    items: list = [],
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    list_props: Any = None,
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    menu: bool = None,
    menu_icon: Any = None,
    menu_props: Any = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_modifiers: Any = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    no_auto_scroll: bool = None,
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
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
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
    tile: bool = None,
    tooltip: str = None,
    transition: typing.Union[str, bool, dict] = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    value_comparator: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Select, Any]:
    """Widget for the Vuetify v-select component, see https://vuetifyjs.com/en/api/v-select/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: Enables autofocus.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param chips: Changes display of selections to chips.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clearable: Allows for the component to be cleared.
    :param closable_chips: Enables the [closable](https://vuetifyjs.com/en/api/v-chip/#props-closable) prop on all [v-chip](https://vuetifyjs.com/en/components/chips/) components.
    :param close_text: Text set to the inputs `aria-label` and `title` when input menu is closed.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Function returns the counter display text.
    :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
    :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the input.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param filter_keys: Array of specific keys to filter on the item.
    :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :param hide_selected: Do not display in the select menu items that are already selected.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-select/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param item_children: This property currently has **no effect**.
    :param item_color: Sets color of selected items.
    :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
    :param item_title: Property on supplied `items` that contains its title.
    :param item_value: Set property of **items**'s value - **must be primitive**. Dot notation is supported. **Note:** This is currently not supported with `v-combobox` [GitHub Issue](https://github.com/vuetifyjs/vuetify/issues/5479).
    :param items: Can be an array of objects or strings. By default objects should have **title** and **value** properties, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props). Keys to use for these can be changed with the **item-title**, **item-value**, and **item-props** props.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param list_props: Pass props through to the `v-list` component. Accepts an object with anything from [v-list](https://vuetifyjs.com/en/api/v-list/#props) props, camelCase keys are recommended.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param menu: Renders with the menu open by default.
    :param menu_icon: Sets the the spin icon.
    :param menu_props: Pass props through to the `v-menu` component. Accepts an object with anything from [v-menu](https://vuetifyjs.com/en/api/v-menu/#props) props, camelCase keys are recommended.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width of the select's `v-menu` content.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes select to multiple. Accepts array for value.
    :param name: Sets the component's name attribute.
    :param no_auto_scroll: Prevents the select menu to scroll to the selected item automatically.
    :param no_data_text: Text shown when no items are provided to the component.
    :param no_filter: Disables all item filtering.
    :param open_on_clear: When using the **clearable** prop, once cleared, the select menu will either open or stay open, depending on the current state.
    :param open_text: Text set to the inputs **aria-label** and **title** when input menu is open.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-select/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param placeholder: Sets the input’s placeholder text.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param readonly: Puts input in readonly state.
    :param return_object: Changes the selection behavior to return the object directly rather than the value specified with **item-value**.
    :param reverse: Reverses the orientation.
    :param role: The role attribute applied to the input.
    :param rounded: Adds a border radius to the input.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param search: Text input used to filter items.
    :param single_line: Label does not move on focus/dirty.
    :param suffix: Displays suffix text.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param type: Sets input type.
    :param validate_on: Change what type of event triggers validation to run.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    base_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    defaults_target: str = None,
    density: str = None,
    disabled: bool = None,
    error: bool = None,
    false_icon: Any = None,
    false_value: Any = None,
    id: str = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: Any = None,
    true_value: Any = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    value_comparator: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SelectionControl, Any]:
    """Widget for the Vuetify v-selection-control component, see https://vuetifyjs.com/en/api/v-selection-control/
    :param base_color: Sets the color of the input when it is not focused.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param defaults_target: The target component to provide defaults values for.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param false_icon: The icon used when inactive.
    :param false_value: Sets value for falsy state.
    :param id: Sets the DOM id on the component.
    :param inline: Puts children inputs into a row.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes select to multiple. Accepts array for value.
    :param name: Sets the component's name attribute.
    :param readonly: Puts input in readonly state.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param true_icon: The icon used when active.
    :param true_value: Sets value for truthy state.
    :param type: Provides the default type for children selection controls.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
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
    false_icon: Any = None,
    id: str = None,
    inline: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: Any = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SelectionControlGroup, Any]:
    """Widget for the Vuetify v-selection-control-group component, see https://vuetifyjs.com/en/api/v-selection-control-group/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param defaults_target: The target component to provide defaults values for.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param false_icon: The icon used when inactive.
    :param id: Sets the DOM id on the component.
    :param inline: Puts children inputs into a row.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes select to multiple. Accepts array for value.
    :param name: Sets the component's name attribute.
    :param readonly: Puts input in readonly state.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param true_icon: The icon used when active.
    :param type: Provides the default type for children selection controls.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
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
    location: Any = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    position: str = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Sheet, Any]:
    """Widget for the Vuetify v-sheet component, see https://vuetifyjs.com/en/api/v-sheet/
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param height: Sets the height for the component.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param position: Sets the position for the component.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SkeletonLoader, Any]:
    """Widget for the Vuetify v-skeleton-loader component, see https://vuetifyjs.com/en/api/v-skeleton-loader/
    :param boilerplate: Remove the loading animation from the skeleton.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param height: Sets the height for the component.
    :param loading: Applies a loading animation with a on-hover loading cursor. A value of **false** will only work when there is content in the `default` slot.
    :param loading_text: aria-label for the element in a loading state.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param type: A string delimited list of skeleton components to create such as `type="text@3"` or `type="card, list-item"`. Will recursively generate a corresponding skeleton from the provided string. Also supports short-hand for multiple elements such as **article@3** and **paragraph@2** which will generate 3 _article_ skeletons and 2 _paragraph_ skeletons. Please see below for a list of available pre-defined options.
    :param width: Sets the width for the component.
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
    content_class: Any = None,
    direction: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    model_value: Any = None,
    multiple: bool = None,
    next_icon: Any = None,
    prev_icon: Any = None,
    scroll_to_active: bool = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slot: str = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideGroup, Any]:
    """Widget for the Vuetify v-slide-group component, see https://vuetifyjs.com/en/api/v-slide-group/
    :param center_active: Forces the selected component to be centered.
    :param content_class: Adds classes to the slide group item.
    :param direction: Switch between horizontal and vertical modes.
    :param disabled: Puts all children components into a disabled state.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Sets the designated mobile breakpoint for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows one to select multiple items.
    :param next_icon: The appended slot when arrows are shown.
    :param prev_icon: The prepended slot when arrows are shown.
    :param scroll_to_active: Keeps the last active element visible when resizing the scrollable container.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param show_arrows: Change when the overflow arrow indicators are shown. By **default**, arrows *always* display on Desktop when the container is overflowing. When the container overflows on mobile, arrows are not shown by default. A **show-arrows** value of `true` allows these arrows to show on Mobile if the container overflowing. A value of `desktop` *always* displays arrows on Desktop while a value of `mobile` always displays arrows on Mobile. A value of `always` always displays arrows on Desktop *and* Mobile. Use **never** to turn arrows off. Find more information on how to customize breakpoint thresholds on the [breakpoints page](https://vuetifyjs.com/en/customizing/breakpoints).
    :param symbol: The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideGroupItem, Any]:
    """Widget for the Vuetify v-slide-group-item component, see https://vuetifyjs.com/en/api/v-slide-group-item/
    :param disabled: Removes the ability to click or target the component.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideXReverseTransition, Any]:
    """Widget for the Vuetify v-slide-x-reverse-transition component, see https://vuetifyjs.com/en/api/v-slide-x-reverse-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideXTransition, Any]:
    """Widget for the Vuetify v-slide-x-transition component, see https://vuetifyjs.com/en/api/v-slide-x-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideYReverseTransition, Any]:
    """Widget for the Vuetify v-slide-y-reverse-transition component, see https://vuetifyjs.com/en/api/v-slide-y-reverse-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SlideYTransition, Any]:
    """Widget for the Vuetify v-slide-y-transition component, see https://vuetifyjs.com/en/api/v-slide-y-transition/
    :param disabled: Removes the ability to click or target the component.
    :param group: Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).
    :param hide_on_leave: Hides the leaving element (no exit animation).
    :param leave_absolute: Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).
    :param mode: Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
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
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
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
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: typing.Union[str, float] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: typing.Union[str, float] = None,
    name: str = None,
    no_keyboard: bool = None,
    persistent_hint: bool = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    reverse: bool = None,
    ripple: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    show_ticks: typing.Union[bool, str] = None,
    slot: str = None,
    step: typing.Union[str, float] = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    thumb_color: str = None,
    thumb_label: typing.Union[bool, str, str] = None,
    thumb_size: typing.Union[str, float] = None,
    tick_size: typing.Union[str, float] = None,
    ticks: typing.Union[list, dict] = None,
    tile: bool = None,
    tooltip: str = None,
    track_color: str = None,
    track_fill_color: str = None,
    track_size: typing.Union[str, float] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Slider, Any]:
    """Widget for the Vuetify v-slider component, see https://vuetifyjs.com/en/api/v-slider/
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param direction: Changes the direction of the input.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the input is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-slider/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param max: Sets the maximum allowed value.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min: Sets the minimum allowed value.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param no_keyboard: **FOR INTERNAL USE ONLY** Ignore keyboard events.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-slider/#props-hint) to always be visible.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param readonly: Puts input in readonly state.
    :param reverse: Reverses the slider direction.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param show_ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
    :param step: If greater than 0, sets step interval for ticks.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param thumb_color: Sets the thumb and thumb label color.
    :param thumb_label: Show thumb label. If `true` it shows label when using slider. If set to `'always'` it always shows label. (since [v3.12.0](https://vuetifyjs.com/en/getting-started/release-notes/?version=v3.12.0) it supports `'hover'` to show label when hovering over the thumb.
    :param thumb_size: Controls the size of the thumb label.
    :param tick_size: Controls the size of **ticks**
    :param ticks: Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param track_color: Sets the track's color
    :param track_fill_color: Sets the track's fill color
    :param track_size: Sets the track's size (height).
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param width: Sets the width for the component.
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
    activator_props: Any = None,
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
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    multi_line: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
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
    target: str = None,
    text: str = None,
    theme: str = None,
    tile: bool = None,
    timeout: typing.Union[str, float] = None,
    timer: typing.Union[str, bool] = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    vertical: bool = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Snackbar, Any]:
    """Widget for the Vuetify v-snackbar component, see https://vuetifyjs.com/en/api/v-snackbar/
    :param absolute: Applies **position: absolute** to the content element.
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Closes component when you click on its content.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param height: Sets the height for the component.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multi_line: Deprecated, use `min-height` instead. Increases minimum height.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :param open_on_click: Activate the component when the activator is clicked.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Activate the component when the activator is hovered.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param position: Sets the position for the component.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param timeout: Time (in milliseconds) to wait until snackbar is automatically hidden.  Use `-1` to keep open indefinitely (`0` in version < 2.3 ). It is recommended for this number to be between `4000` and `10000`. Changes to this property will reset the timeout.
    :param timer: Display a progress bar that counts down until the snackbar closes. Pass a string to set a custom color, otherwise uses `info`.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param variant: Applies a distinct style to the component.
    :param vertical: Stacks snackbar content on top of the actions (button).
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
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


def _SnackbarQueue(
    absolute: bool = None,
    activator: str = None,
    activator_props: Any = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    closable: typing.Union[str, bool] = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    close_text: str = None,
    color: str = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disabled: bool = None,
    eager: bool = None,
    height: typing.Union[str, float] = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: list = [],
    multi_line: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
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
    target: str = None,
    text: str = None,
    theme: str = None,
    tile: bool = None,
    timeout: typing.Union[str, float] = None,
    timer: typing.Union[str, bool] = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    vertical: bool = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SnackbarQueue, Any]:
    """Widget for the Vuetify v-snackbar-queue component, see https://vuetifyjs.com/en/api/v-snackbar-queue/
    :param absolute: Applies **position: absolute** to the content element.
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :param closable: Adds a dismiss button that closes the active snackbar.
    :param close_delay: Milliseconds to wait before closing component. Only applies to hover and focus events.
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Closes component when you click on its content.
    :param close_text: The text used in the close button when using the **closable** prop.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param height: Sets the height for the component.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multi_line: Deprecated, use `min-height` instead. Increases minimum height.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Milliseconds to wait before opening component. Only applies to hover and focus events.
    :param open_on_click: Activate the component when the activator is clicked.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Activate the component when the activator is hovered.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param position: Sets the position for the component.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param timeout: Time (in milliseconds) to wait until snackbar is automatically hidden.  Use `-1` to keep open indefinitely (`0` in version < 2.3 ). It is recommended for this number to be between `4000` and `10000`. Changes to this property will reset the timeout.
    :param timer: Display a progress bar that counts down until the snackbar closes. Pass a string to set a custom color, otherwise uses `info`.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param variant: Applies a distinct style to the component.
    :param vertical: Stacks snackbar content on top of the actions (button).
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
    """
    ...


@implements(_SnackbarQueue)
def SnackbarQueue(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.SnackbarQueue
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _SnackbarQueue


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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Spacer, Any]:
    """Widget for the Vuetify v-spacer component, see https://vuetifyjs.com/en/api/v-spacer/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    auto_draw_duration: typing.Union[str, float] = None,
    auto_draw_easing: str = None,
    auto_line_width: bool = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    fill: bool = None,
    gradient: list = [],
    gradient_direction: str = None,
    height: typing.Union[str, float] = None,
    id: str = None,
    item_value: str = None,
    label_size: typing.Union[str, float] = None,
    labels: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    line_width: typing.Union[str, float] = None,
    max: typing.Union[str, float] = None,
    min: typing.Union[str, float] = None,
    model_value: list = [],
    padding: typing.Union[str, float] = None,
    show_labels: bool = None,
    slot: str = None,
    smooth: typing.Union[str, float, bool] = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Sparkline, Any]:
    """Widget for the Vuetify v-sparkline component, see https://vuetifyjs.com/en/api/v-sparkline/
    :param auto_draw: Trace the length of the line when first rendered.
    :param auto_draw_duration: Amount of time (in ms) to run the trace animation.
    :param auto_draw_easing: The easing function to use for the trace animation.
    :param auto_line_width: Automatically expand bars to use space efficiently.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param fill: Using the **fill** property allows you to better customize the look and feel of your sparkline.
    :param gradient: An array of colors to use as a linear-gradient.
    :param gradient_direction: The direction the gradient should run.
    :param height: Height of the SVG trendline or bars.
    :param id: The id of the component.
    :param item_value: The value of the item.
    :param label_size: The label font size.
    :param labels: An array of string labels that correspond to the same index as its data counterpart.
    :param line_width: The thickness of the line, in px.
    :param max: The maximum value of the sparkline.
    :param min: The minimum value of the sparkline.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param padding: Low `smooth` or high `line-width` values may result in cropping, increase padding to compensate.
    :param show_labels: Show labels below each data point.
    :param smooth: Number of px to use as a corner radius. `true` defaults to 8, `false` is 0.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param type: Choose between a trendline or bars.
    :param width: Width of the SVG trendline or bars.
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
    activator: str = None,
    activator_props: Any = None,
    attach: typing.Union[str, bool] = None,
    attributes: dict = {},
    capture_focus: bool = None,
    children: list = [],
    class_: str = None,
    close_delay: typing.Union[str, float] = None,
    close_on_back: bool = None,
    close_on_content_click: bool = None,
    contained: bool = None,
    content_class: Any = None,
    content_props: Any = None,
    disable_initial_focus: bool = None,
    disabled: bool = None,
    eager: bool = None,
    height: typing.Union[str, float] = None,
    id: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    retain_focus: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    slot: str = None,
    stick_to_target: bool = None,
    style_: str = None,
    submenu: bool = None,
    tabbable: bool = None,
    target: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool, dict] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    viewport_margin: typing.Union[str, float] = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SpeedDial, Any]:
    """Widget for the Vuetify v-speed-dial component, see https://vuetifyjs.com/en/api/v-speed-dial/
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :param close_delay: Milliseconds to wait before closing component. Only works with the **open-on-hover** prop.
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Closes component when you click on its content.
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param disable_initial_focus: Deprecated, use `capture-focus` instead. Prevents automatic redirect of first `focusin` event. Intended to use on permanently open menus or VSpeedDial.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param height: Sets the height for the component.
    :param id: The unique identifier of the component.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Milliseconds to wait before opening component. Only works with the **open-on-hover** prop.
    :param open_on_click: Activate the component when the activator is clicked.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Opens speed-dial on hover.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :param retain_focus: Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.
    :param scrim: Accepts true/false to enable background, and string to define color.
    :param scroll_strategy: Strategy used when the component is activate and user scrolls.
    :param stick_to_target: Enables the overlay content to go off-screen when scrolling.
    :param submenu: Opens with right arrow and closes on left instead of up/down. Implies `location="end"`. Directions are reversed for RTL.
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param viewport_margin: Sets custom viewport margin for the overlay content
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
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
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    complete_icon: Any = None,
    disabled: bool = None,
    edit_icon: Any = None,
    editable: bool = None,
    elevation: typing.Union[str, float] = None,
    error_icon: Any = None,
    flat: bool = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    item_props: str = None,
    item_title: str = None,
    item_value: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
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
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Stepper, Any]:
    """Widget for the Vuetify v-stepper component, see https://vuetifyjs.com/en/api/v-stepper/
    :param alt_labels: Places the labels beneath the step.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param complete_icon: Icon to display when step is marked as completed.
    :param disabled: Puts all children components into a disabled state.
    :param edit_icon: Icon to display when step is editable.
    :param editable: Marks step as editable.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param error_icon: Icon to display when step has an error.
    :param flat: Removes the stepper's elevation.
    :param height: Sets the height for the component.
    :param hide_actions: Hide actions bar (prev and next buttons).
    :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
    :param item_title: Property on supplied `items` that contains its title.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: An array of strings or objects used for automatically generating children components.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param mobile: Forces the stepper into a mobile state, removing labels from stepper items.
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows one to select multiple items.
    :param next_text: The text used for the Next button.
    :param non_linear: Allow user to jump to any step.
    :param position: Sets the position for the component.
    :param prev_text: The text used for the Prev button.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperActions, Any]:
    """Widget for the Vuetify v-stepper-actions component, see https://vuetifyjs.com/en/api/v-stepper-actions/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param next_text: The text used for the Next button.
    :param prev_text: The text used for the Prev button.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperHeader, Any]:
    """Widget for the Vuetify v-stepper-header component, see https://vuetifyjs.com/en/api/v-stepper-header/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    complete_icon: Any = None,
    disabled: bool = None,
    edit_icon: Any = None,
    editable: bool = None,
    error: bool = None,
    error_icon: Any = None,
    icon: Any = None,
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperItem, Any]:
    """Widget for the Vuetify v-stepper-item component, see https://vuetifyjs.com/en/api/v-stepper-item/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param complete: Marks step as complete.
    :param complete_icon: Icon to display when step is marked as completed.
    :param disabled: Removes the ability to click or target the component.
    :param edit_icon: Icon to display when step is editable.
    :param editable: Marks step as editable.
    :param error: Puts the stepper item in a manual error state.
    :param error_icon: Icon to display when step has an error.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
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


def _StepperVertical(
    alt_labels: bool = None,
    attributes: dict = {},
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    complete_icon: Any = None,
    disabled: bool = None,
    eager: bool = None,
    edit_icon: Any = None,
    editable: bool = None,
    elevation: typing.Union[str, float] = None,
    error_icon: Any = None,
    expand_icon: Any = None,
    flat: bool = None,
    focusable: bool = None,
    hide_actions: bool = None,
    item_props: str = None,
    item_title: str = None,
    item_value: str = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    model_value: Any = None,
    multiple: bool = None,
    next_text: str = None,
    non_linear: bool = None,
    prev_text: str = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperVertical, Any]:
    """Widget for the Vuetify v-stepper-vertical component, see https://vuetifyjs.com/en/api/v-stepper-vertical/
    :param alt_labels: Places the labels beneath the step.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param complete_icon: Icon to display when step is marked as completed.
    :param disabled: Puts all children components into a disabled state.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param edit_icon: Icon to display when step is editable.
    :param editable: Marks step as editable.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param error_icon: Icon to display when step has an error.
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :param flat: Removes the expansion-panel's elevation and borders.
    :param focusable: Makes the expansion-panel headers focusable.
    :param hide_actions: Hide the expand icon in the content title.
    :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
    :param item_title: Property on supplied `items` that contains its title.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: An array of strings or objects used for automatically generating children components.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Overrides the display configuration default screen size that the component should be considered in mobile.
    :param model_value: Controls expanded panel(s). Defaults to an empty array when using **multiple** prop. It is recommended to set unique `value` prop for the panels inside, otherwise index is used instead.
    :param multiple: Allows one to select multiple items.
    :param next_text: The text used for the Next button.
    :param non_linear: Allow user to jump to any step.
    :param prev_text: The text used for the Prev button.
    :param readonly: Makes the entire expansion panel read only.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes the border-radius.
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
    """
    ...


@implements(_StepperVertical)
def StepperVertical(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperVertical
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperVertical


def _StepperVerticalActions(
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperVerticalActions, Any]:
    """Widget for the Vuetify v-stepper-vertical-actions component, see https://vuetifyjs.com/en/api/v-stepper-vertical-actions/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param next_text: The text used for the Next button.
    :param prev_text: The text used for the Prev button.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_StepperVerticalActions)
def StepperVerticalActions(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperVerticalActions
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperVerticalActions


def _StepperVerticalItem(
    attributes: dict = {},
    bg_color: str = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    complete: bool = None,
    complete_icon: Any = None,
    disabled: bool = None,
    eager: bool = None,
    edit_icon: Any = None,
    editable: bool = None,
    elevation: typing.Union[str, float] = None,
    error: bool = None,
    error_icon: Any = None,
    expand_icon: Any = None,
    focusable: bool = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    rules: list = [],
    selected_class: str = None,
    slot: str = None,
    static: bool = None,
    style_: str = None,
    subtitle: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperVerticalItem, Any]:
    """Widget for the Vuetify v-stepper-vertical-item component, see https://vuetifyjs.com/en/api/v-stepper-vertical-item/
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param collapse_icon: Icon used when the expansion panel is in a collapsable state.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param complete: Marks step as complete.
    :param complete_icon: Icon to display when step is marked as completed.
    :param disabled: Disables the expansion-panel content.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param edit_icon: Icon to display when step is editable.
    :param editable: Marks step as editable.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param error: Puts the stepper item in a manual error state.
    :param error_icon: Icon to display when step has an error.
    :param expand_icon: Icon used when the expansion panel is in a expandable state.
    :param focusable: Makes the expansion panel content focusable.
    :param height: Sets the height for the component.
    :param hide_actions: Hide the expand icon in the content title.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param readonly: Makes the expansion panel content read only.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param static: Remove title size expansion when selected.
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param value: Controls the opened/closed state of content.
    :param width: Sets the width for the component.
    """
    ...


@implements(_StepperVerticalItem)
def StepperVerticalItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.StepperVerticalItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _StepperVerticalItem


def _StepperWindow(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    crossfade: bool = None,
    direction: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    reverse: bool = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    transition_duration: float = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    vertical_arrows: typing.Union[bool, str, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperWindow, Any]:
    """Widget for the Vuetify v-stepper-window component, see https://vuetifyjs.com/en/api/v-stepper-window/
    :param crossfade: Enables crossfade transition.
    :param direction: The transition direction when changing windows.
    :param disabled: Removes the ability to click or target the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param reverse: Reverse the normal transition direction.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition_duration: Overrides transition duration. Does not work in firefox, safari <18, or with `prefers-reduced-motion: reduce`.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.StepperWindowItem, Any]:
    """Widget for the Vuetify v-stepper-window-item component, see https://vuetifyjs.com/en/api/v-stepper-window-item/
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param reverse_transition: Sets the reverse transition.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param transition: The transition used when the component progressing through items. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
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
    icon: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SvgIcon, Any]:
    """Widget for the Vuetify v-svg-icon component, see https://vuetifyjs.com/en/api/v-svg-icon/
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
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
    false_icon: Any = None,
    false_value: Any = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    indeterminate: bool = None,
    inline: bool = None,
    inset: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_value: Any = None,
    multiple: bool = None,
    name: str = None,
    persistent_hint: bool = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rules: list = [],
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    true_icon: Any = None,
    true_value: Any = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    value: Any = None,
    value_comparator: Any = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Switch, Any]:
    """Widget for the Vuetify v-switch component, see https://vuetifyjs.com/en/api/v-switch/
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of the input when it is not focused.
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param defaults_target: The target component to provide defaults values for.
    :param density: Adjusts the vertical height used by the component.
    :param direction: Changes the direction of the input.
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param false_icon: The icon used when inactive.
    :param false_value: Sets value for falsy state.
    :param flat: Display component without elevation. Default elevation for thumb is 4dp, `flat` resets it.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the input is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-switch/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param indeterminate: Sets an indeterminate state for the switch.
    :param inline: Puts children inputs into a row.
    :param inset: Enlarge the `v-switch` track to encompass the thumb.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param loading: Displays circular progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - primary, secondary, success, info, warning, error) or a Boolean which uses the component color (set by color prop - if it's supported by the component) or the primary color.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Changes expected model to an array.
    :param name: Sets the component's name attribute.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-switch/#props-hint) to always be visible.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param readonly: Puts input in readonly state.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param true_icon: The icon used when active.
    :param true_value: Sets value for truthy state.
    :param type: Provides the default type for children selection controls.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param width: Sets the width for the component.
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
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    window: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.SystemBar, Any]:
    """Widget for the Vuetify v-system-bar component, see https://vuetifyjs.com/en/api/v-system-bar/
    :param absolute: Applies **position: absolute** to the component.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param height: Sets the height for the component.
    :param name: Assign a specific name for layout registration.
    :param order: Adjust the order of the component in relation to its registration order.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param window: Increases the system bar height to 32px (24px default).
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
    active_color: str = None,
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
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
    icon: Any = None,
    inset: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    prepend_icon: Any = None,
    readonly: bool = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    selected_class: str = None,
    size: typing.Union[str, float] = None,
    slider_color: str = None,
    slider_transition: str = None,
    slider_transition_duration: typing.Union[str, float] = None,
    slim: bool = None,
    slot: str = None,
    spaced: str = None,
    stacked: bool = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    text: typing.Union[str, float, bool] = None,
    theme: str = None,
    tile: bool = None,
    to: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Tab, Any]:
    """Widget for the Vuetify v-tab component, see https://vuetifyjs.com/en/api/v-tab/
    :param active_color: The applied color when the component is in an active state.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param direction: Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param fixed: Forces component to take up all available space up to their maximum width (300px), and centers it.
    :param height: Sets the height for the component.
    :param hide_slider: Hides the active tab slider component (no exit or enter animation).
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param icon: Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component. The button will become _round_.
    :param inset: Changes the slider to take full height. Automatically propagated from VTabs.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param readonly: Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param slider_color: Applies specified color to the slider when active on that component - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param slider_transition: Changes slider transition to one of the predefined animation presets.
    :param slider_transition_duration: Applies custom slider transition duration. Default duration depends on transition type (fade: 400, grow: 350, shift: 225).
    :param slim: Reduces padding to 0 8px.
    :param spaced: Extends content to the edges to move main content from prepend and append slots.
    :param stacked: Displays the tab as a flex-column.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param tooltip: A tooltip caption.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    striped: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Table, Any]:
    """Widget for the Vuetify v-table component, see https://vuetifyjs.com/en/api/v-table/
    :param density: Adjusts the vertical height used by the component.
    :param fixed_footer: Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.
    :param fixed_header: Use the fixed-header prop together with the height prop to fix the header to the top of the table.
    :param height: Use the height prop to set the height of the table.
    :param hover: Will add a hover effect to a table's row when the mouse is over it.
    :param striped: Applies a background to either **even** or **odd** rows.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
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
    content_class: Any = None,
    density: str = None,
    direction: str = None,
    disabled: bool = None,
    fixed_tabs: bool = None,
    grow: bool = None,
    height: typing.Union[str, float] = None,
    hide_slider: bool = None,
    inset: bool = None,
    inset_padding: typing.Union[str, float] = None,
    inset_radius: typing.Union[str, float] = None,
    items: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    max: float = None,
    mobile: bool = None,
    mobile_breakpoint: typing.Union[float, str] = None,
    model_value: Any = None,
    multiple: bool = None,
    next_icon: Any = None,
    prev_icon: Any = None,
    scroll_to_active: bool = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slider_color: str = None,
    slider_transition: str = None,
    slider_transition_duration: typing.Union[str, float] = None,
    slot: str = None,
    spaced: str = None,
    stacked: bool = None,
    style_: str = None,
    symbol: Any = None,
    tabbable: bool = None,
    tag: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Tabs, Any]:
    """Widget for the Vuetify v-tabs component, see https://vuetifyjs.com/en/api/v-tabs/
    :param align_tabs: Aligns the tabs to the `start`, `center`, or `end` of container. Also accepts `title` to align with the `v-toolbar-title` component.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_active: Forces the selected tab to be centered.
    :param color: Applies specified color to the selected tab - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param content_class: Adds classes to the slide group item.
    :param density: Adjusts the vertical height used by the component.
    :param direction: Changes the direction of the tabs. Can be either `horizontal` or `vertical`.
    :param disabled: Puts all children components into a disabled state.
    :param fixed_tabs: Tabs will be centered and each tab item will grow up to 300px width.
    :param grow: Forces tabs to take up all available space.
    :param height: Sets the height of the tabs bar.
    :param hide_slider: Hide's the generated `v-tabs-slider`.
    :param inset: Changes the slider to take full height. Tabs will also get some spacing and customizable rounding.
    :param inset_padding: Sets custom spacing between tabs for `inset` mode.
    :param inset_radius: Sets custom border radius for the tabs container `inset` mode. Rounding for individual tabs is calculated by subtracting the padding.
    :param items: The items to display in the component. This can be an array of strings or objects with a property `text`.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max: Sets a maximum number of selections that can be made.
    :param mobile: Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint
    :param mobile_breakpoint: Sets the designated mobile breakpoint for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param multiple: Allows one to select multiple items.
    :param next_icon: Right pagination icon.
    :param prev_icon: Left pagination icon.
    :param scroll_to_active: Keeps the last active element visible when resizing the scrollable container.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param show_arrows: Show pagination arrows if the tab items overflow their container. For mobile devices, arrows will only display when using this prop.
    :param slider_color: Changes the background color of an auto-generated `v-tabs-slider`.
    :param slider_transition: Changes slider transition to one of the predefined animation presets.
    :param slider_transition_duration: Applies custom slider transition duration. Default duration depends on transition type (fade: 400, grow: 350, shift: 225).
    :param spaced: Extends content to the edges to move main content from prepend and append slots.
    :param stacked: Apply the stacked prop to all children v-tab components.
    :param symbol: The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
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


def _TabsWindow(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    crossfade: bool = None,
    direction: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    model_value: Any = None,
    reverse: bool = None,
    selected_class: str = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    transition_duration: float = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    vertical_arrows: typing.Union[bool, str, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TabsWindow, Any]:
    """Widget for the Vuetify v-tabs-window component, see https://vuetifyjs.com/en/api/v-tabs-window/
    :param crossfade: Enables crossfade transition.
    :param direction: The transition direction when changing windows.
    :param disabled: Removes the ability to click or target the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param reverse: Reverse the normal transition direction.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition_duration: Overrides transition duration. Does not work in firefox, safari <18, or with `prefers-reduced-motion: reduce`.
    """
    ...


@implements(_TabsWindow)
def TabsWindow(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TabsWindow
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TabsWindow


def _TabsWindowItem(
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TabsWindowItem, Any]:
    """Widget for the Vuetify v-tabs-window-item component, see https://vuetifyjs.com/en/api/v-tabs-window-item/
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param reverse_transition: Sets the reverse transition.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param transition: The transition used when the component progressing through items. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
    """
    ...


@implements(_TabsWindowItem)
def TabsWindowItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TabsWindowItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TabsWindowItem


def _TextField(
    active: bool = None,
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: float = None,
    density: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_modifiers: Any = None,
    model_value: Any = None,
    name: str = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
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
    tile: bool = None,
    tooltip: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TextField, Any]:
    """Widget for the Vuetify v-text-field component, see https://vuetifyjs.com/en/api/v-text-field/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: Enables autofocus.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param clear_icon: Applied when using **clearable** and the input is dirty.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Function returns the counter display text.
    :param density: Adjusts the vertical height used by the component.
    :param dirty: Manually apply the dirty state styling.
    :param disabled: Removes the ability to click or target the input.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param flat: Removes elevation (shadow) added to element when using the **solo** or **solo-inverted** props.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-text-field/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-text-field/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param placeholder: Sets the input’s placeholder text.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Prepends an icon inside the component's input, uses the same syntax as `v-icon`.
    :param readonly: Puts input in readonly state.
    :param reverse: Reverses the input orientation.
    :param role: The role attribute applied to the input.
    :param rounded: Adds a border radius to the input.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param single_line: Label does not move on focus/dirty.
    :param suffix: Displays suffix text.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param type: Sets input type.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    append_icon: Any = None,
    append_inner_icon: Any = None,
    attributes: dict = {},
    auto_grow: bool = None,
    autocomplete: str = None,
    autofocus: bool = None,
    base_color: str = None,
    bg_color: str = None,
    center_affix: bool = None,
    children: list = [],
    class_: str = None,
    clear_icon: Any = None,
    clearable: bool = None,
    color: str = None,
    counter: typing.Union[str, float, bool] = None,
    counter_value: Any = None,
    density: str = None,
    dirty: bool = None,
    disabled: bool = None,
    error: bool = None,
    error_messages: typing.Union[str, list] = None,
    flat: bool = None,
    focused: bool = None,
    glow: bool = None,
    hide_details: typing.Union[bool, str] = None,
    hide_spin_buttons: bool = None,
    hint: str = None,
    icon_color: typing.Union[str, bool] = None,
    id: str = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    loading: typing.Union[str, bool] = None,
    max_errors: typing.Union[str, float] = None,
    max_height: typing.Union[str, float] = None,
    max_rows: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    messages: typing.Union[str, list] = None,
    min_width: typing.Union[str, float] = None,
    model_modifiers: Any = None,
    model_value: Any = None,
    name: str = None,
    no_resize: bool = None,
    persistent_clear: bool = None,
    persistent_counter: bool = None,
    persistent_hint: bool = None,
    persistent_placeholder: bool = None,
    placeholder: str = None,
    prefix: str = None,
    prepend_icon: Any = None,
    prepend_inner_icon: Any = None,
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
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Textarea, Any]:
    """Widget for the Vuetify v-textarea component, see https://vuetifyjs.com/en/api/v-textarea/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param append_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot.
    :param auto_grow: Automatically grow the textarea depending on amount of text.
    :param autocomplete: Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.
    :param autofocus: The element should be focused as soon as the page loads.
    :param base_color: Sets the color of the input when it is not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param center_affix: Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.
    :param clear_icon: The icon used when the **clearable** prop is set to true.
    :param clearable: Allows for the component to be cleared.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param counter: Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.
    :param counter_value: Display the input length but do not provide any validation.
    :param density: Adjusts the vertical height used by the component.
    :param dirty: Manually apply the dirty state styling.
    :param disabled: Removes the ability to click or target the input.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param flat: Removes box shadow when using a variant with elevation.
    :param focused: Forces a focused state styling on the component.
    :param glow: Makes prepend/append icons full opacity when the field is focused and apply color.
    :param hide_details: Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.
    :param hide_spin_buttons: Hides spin buttons on the input when type is set to `number`.
    :param hint: Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-textarea/#props-persistent-hint) property.
    :param icon_color: Sets the color of the prepend/append icons.
    :param id: Sets the DOM id on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param loading: Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param max_height: Alternative for **max-rows**. Specifies the maximum height in pixels (including the field padding) for **auto-grow**.
    :param max_rows: Specifies the maximum number of rows for **auto-grow**.
    :param max_width: Sets the maximum width for the component.
    :param messages: Displays a list of messages or a single message if using a string.
    :param min_width: Sets the minimum width for the component.
    :param model_modifiers: **FOR INTERNAL USE ONLY**
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param no_resize: Remove resize handle.
    :param persistent_clear: Always show the clearable icon when the input is dirty (By default it only shows on hover).
    :param persistent_counter: Forces counter to always be visible.
    :param persistent_hint: Forces [hint](https://vuetifyjs.com/en/api/v-textarea/#props-hint) to always be visible.
    :param persistent_placeholder: Forces placeholder to always be visible.
    :param placeholder: Sets the input's placeholder text.
    :param prefix: Displays prefix text.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param prepend_inner_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot.
    :param readonly: Puts input in readonly state.
    :param reverse: Reverses the orientation.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param rows: Default row count.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param single_line: Label does not move on focus/dirty.
    :param suffix: Displays suffix text.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    with_background: bool = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ThemeProvider, Any]:
    """Widget for the Vuetify v-theme-provider component, see https://vuetifyjs.com/en/api/v-theme-provider/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param with_background: Wraps its children in an element and applies the current theme's background color to it.
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
    allowed_hours: list = [],
    allowed_minutes: list = [],
    allowed_seconds: list = [],
    attributes: dict = {},
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    disabled: bool = None,
    divided: bool = None,
    elevation: typing.Union[str, float] = None,
    format: str = None,
    height: typing.Union[str, float] = None,
    hide_header: bool = None,
    hide_title: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    max: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min: str = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: Any = None,
    period: str = None,
    position: str = None,
    readonly: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    scrollable: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    use_seconds: bool = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    view_mode: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TimePicker, Any]:
    """Widget for the Vuetify v-time-picker component, see https://vuetifyjs.com/en/api/v-time-picker/
    :param allowed_hours: Restricts which hours can be selected.
    :param allowed_minutes: Restricts which minutes can be selected.
    :param allowed_seconds: Restricts which seconds can be selected.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param divided: Adds a divider between the header and controls.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param format: Defines the format of a time displayed in picker. Available options are `ampm` and `24hr`.
    :param height: Sets the height for the component.
    :param hide_header: Hide the picker header.
    :param hide_title: Hide the picker title.
    :param location: Specifies the component's location. Can combine by using a space separated string.
    :param max: Maximum allowed time.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min: Minimum allowed time.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param period: Sets period for 12hr format.
    :param position: Sets the position for the component.
    :param readonly: Puts picker in readonly state.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param scrollable: Allows changing hour/minute with mouse scroll.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param use_seconds: Toggles the use of seconds in picker.
    :param variant: Applies a distinct style to the component.
    :param view_mode: The current view mode of the picker.
    :param width: Width of the picker.
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
    allowed_values: Any = None,
    ampm: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    displayed_value: Any = None,
    double: bool = None,
    format: Any = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: float = None,
    min: float = None,
    model_value: float = None,
    readonly: bool = None,
    rotate: float = None,
    scrollable: bool = None,
    slot: str = None,
    step: float = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TimePickerClock, Any]:
    """Widget for the Vuetify v-time-picker-clock component, see https://vuetifyjs.com/en/api/v-time-picker-clock/
    :param allowed_values: Restricts which hours can be selected.
    :param ampm: Displays time in a 12-hour format.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param displayed_value: Used to display a custom value on the clock.
    :param double: If set, this probably indicates a double rotation or a mode where more than one set of values (like hours and minutes) is displayed on the clock at the same time.
    :param format: Specifies the format of the displayed time, either 12-hour or 24-hour, depending on the component's setup.
    :param max: Defines the maximum time value that can be selected.
    :param min: Defines the minimum time value that can be selected.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param readonly: When true, the picker is in a read-only state, and users cannot modify the selected time.
    :param rotate: Controls rotation, specifying the degree of rotation for the clock hands.
    :param scrollable: Allows the time selection to be scrollable, enhancing user experience for devices with scroll inputs.
    :param step: Defines the increments between selectable times, such as a step of 1 for every minute or a larger step for every 5 or 15 minutes.
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


def _TimePickerControls(
    allowed_hours: list = [],
    allowed_minutes: list = [],
    allowed_seconds: list = [],
    ampm: bool = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    color: str = None,
    disabled: bool = None,
    hour: typing.Union[str, float] = None,
    input_hints: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max: str = None,
    min: str = None,
    minute: typing.Union[str, float] = None,
    period: str = None,
    readonly: bool = None,
    second: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    use_seconds: bool = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: float = None,
    view_mode: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TimePickerControls, Any]:
    """Widget for the Vuetify v-time-picker-controls component, see https://vuetifyjs.com/en/api/v-time-picker-controls/
    :param ampm: Enables AM/PM mode.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Removes the ability to click or target the component.
    :param hour: The current hour value.
    :param minute: The current minute value.
    :param period: The current period value. either `am` or `pm`.
    :param readonly: Makes the timepicker readonly.
    :param second: The current second value.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param use_seconds: Enables the display and selection of seconds in the timepicker.
    :param value: The current value of the timepicker.
    :param view_mode: The current view mode of the timepicker. Can be either `hour`, `minute`, or `second`.
    """
    ...


@implements(_TimePickerControls)
def TimePickerControls(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TimePickerControls
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TimePickerControls


def _Timeline(
    align: str = None,
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    density: str = None,
    direction: str = None,
    dot_color: str = None,
    fill_dot: bool = None,
    hide_opposite: bool = None,
    icon_color: str = None,
    justify: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    line_color: str = None,
    line_inset: typing.Union[str, float] = None,
    line_thickness: typing.Union[str, float] = None,
    side: str = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    truncate_line: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Timeline, Any]:
    """Widget for the Vuetify v-timeline component, see https://vuetifyjs.com/en/api/v-timeline/
    :param align: Places the timeline dot at the top or center of the timeline item.
    :param density: Adjusts the vertical height used by the component.
    :param direction: Display timeline in a **vertical** or **horizontal** direction.
    :param dot_color: Color of the item dot.
    :param fill_dot: Remove outer border of item dot, making the color fill the entire dot.
    :param hide_opposite: Hide opposite content if it exists.
    :param icon_color: Color of the icon.
    :param justify: Places timeline line at the center or automatically on the left or right side.
    :param line_color: Color of the timeline line.
    :param line_inset: Specifies the distance between the line and the dot of timeline items.
    :param line_thickness: Thickness of the timeline line.
    :param side: Display all timeline items on one side of the timeline, either **start** or **end**.
    :param size: Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param truncate_line: Truncate timeline directly at the **start** or **end** of the line, or on **both** ends.
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
    icon: Any = None,
    icon_color: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    line_inset: typing.Union[str, float] = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    rounded: typing.Union[str, float, bool] = None,
    side: str = None,
    size: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    tile: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TimelineItem, Any]:
    """Widget for the Vuetify v-timeline-item component, see https://vuetifyjs.com/en/api/v-timeline-item/
    :param density: Adjusts the vertical height used by the component.
    :param dot_color: Color of the item dot.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param fill_dot: Remove outer border of item dot, making the color fill the entire dot.
    :param height: Sets the height for the component.
    :param hide_dot: Hide the timeline item dot.
    :param hide_opposite: Hide opposite content if it exists.
    :param icon: Apply a specific icon to the inside dot using the [v-icon](https://vuetifyjs.com/en/components/icons/) component.
    :param icon_color: Color of the icon.
    :param line_inset: Specifies the distance between the line and the dot of the item.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param side: Show the item either **before** or **after** the timeline. This will override the implicit ordering of items, but will in turn be overridden by the `v-timeline` **single-side** prop.
    :param size: Size of the item dot
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    collapse_position: str = None,
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
    location: Any = None,
    rounded: typing.Union[str, float, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Toolbar, Any]:
    """Widget for the Vuetify v-toolbar component, see https://vuetifyjs.com/en/api/v-toolbar/
    :param absolute: Applies position: absolute to the component.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param collapse: Puts the toolbar into a collapsed state reducing its maximum width.
    :param collapse_position: Specifies side to attach the collapsed toolbar.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param density: Adjusts the vertical height used by the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param extended: Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop. When false, will not show extension slot even if content is present.
    :param extension_height: Specify an explicit height for the `extension` slot.
    :param flat: Removes the toolbar's box-shadow.
    :param floating: Applies **display: inline-flex** to the component.
    :param height: Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.
    :param image: Specifies a [v-img](https://vuetifyjs.com/en/components/images) as the component's background.
    :param location: Specifies the component's location. Can combine by using a space separated string. Requires the **absolute** prop.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Specify a title text for the component.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ToolbarItems, Any]:
    """Widget for the Vuetify v-toolbar-items component, see https://vuetifyjs.com/en/api/v-toolbar-items/
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param variant: Applies a distinct style to the component.
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
    tag: Any = None,
    text: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.ToolbarTitle, Any]:
    """Widget for the Vuetify v-toolbar-title component, see https://vuetifyjs.com/en/api/v-toolbar-title/
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param text: Specify content text for the component.
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
    activator_props: Any = None,
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
    interactive: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    location: Any = None,
    location_strategy: str = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: bool = None,
    no_click_animation: bool = None,
    offset: typing.Union[str, float, list] = None,
    opacity: typing.Union[str, float] = None,
    open_delay: typing.Union[str, float] = None,
    open_on_click: bool = None,
    open_on_focus: bool = None,
    open_on_hover: bool = None,
    origin: str = None,
    persistent: bool = None,
    scrim: typing.Union[str, bool] = None,
    scroll_strategy: str = None,
    slot: str = None,
    stick_to_target: bool = None,
    style_: str = None,
    tabbable: bool = None,
    target: str = None,
    text: str = None,
    theme: str = None,
    tooltip: str = None,
    transition: typing.Union[str, bool] = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    viewport_margin: typing.Union[str, float] = None,
    width: typing.Union[str, float] = None,
    z_index: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Tooltip, Any]:
    """Widget for the Vuetify v-tooltip component, see https://vuetifyjs.com/en/api/v-tooltip/
    :param activator: Explicitly sets the overlay's activator.
    :param activator_props: Apply custom properties to the activator.
    :param attach: Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.
    :param close_delay: Delay (in ms) after which menu closes (when open-on-hover prop is set to true).
    :param close_on_back: Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.
    :param close_on_content_click: Closes component when you click on its content.
    :param contained: Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).
    :param content_class: Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component.
    :param content_props: Apply custom properties to the content.
    :param disabled: Removes the ability to click or target the component.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param height: Sets the height for the component.
    :param id: HTML id attribute of the tooltip overlay. If not set, a globally unique id will be used.
    :param interactive: When true, the tooltip will respond to pointer events, allowing you to copy text from it.
    :param location: Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both..
    :param location_strategy: A function used to specifies how the component should position relative to its activator.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param no_click_animation: Disables the bounce effect when clicking outside of the content element when using the persistent prop.
    :param offset: Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.
    :param opacity: Sets the opacity of the scrim element. Only applies if `scrim` is enabled.
    :param open_delay: Delay (in ms) after which tooltip opens (when `open-on-hover` prop is set to **true**).
    :param open_on_click: Designates whether the tooltip should open on activator click.
    :param open_on_focus: Activate the component when the activator is focused.
    :param open_on_hover: Designates whether the tooltip should open on activator hover.
    :param origin: Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).
    :param persistent: Clicking outside of the element or pressing esc key will not deactivate it.
    :param scrim: Accepts true/false to enable background, and string to define color.
    :param scroll_strategy: Strategy used when the component is activate and user scrolls.
    :param stick_to_target: Enables the overlay content to go off-screen when scrolling.
    :param tabbable: Is widget tabbable?
    :param target: For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.
    :param text: Specify content text for the component.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param transition: Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param viewport_margin: Sets custom viewport margin for the overlay content
    :param width: Sets the width for the component.
    :param z_index: The z-index used for the component.
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
    activated: Any = None,
    active_class: str = None,
    active_color: str = None,
    active_strategy: str = None,
    attributes: dict = {},
    base_color: str = None,
    bg_color: str = None,
    border: typing.Union[str, float, bool] = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    custom_filter: Any = None,
    custom_key_filter: Any = None,
    density: str = None,
    disabled: bool = None,
    elevation: typing.Union[str, float] = None,
    expand_icon: Any = None,
    false_icon: Any = None,
    filter_keys: typing.Union[str, list] = None,
    filter_mode: str = None,
    filterable: bool = None,
    fluid: bool = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    hide_no_data: bool = None,
    indent: typing.Union[str, float] = None,
    indent_lines: typing.Union[bool, str] = None,
    indent_lines_color: str = None,
    indent_lines_opacity: typing.Union[str, float] = None,
    indeterminate_icon: Any = None,
    item_children: str = None,
    item_props: str = None,
    item_title: str = None,
    item_type: str = None,
    item_value: str = None,
    items: list = [],
    items_registration: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: typing.Union[bool, str, str, str] = None,
    load_children: Any = None,
    loading_icon: str = None,
    mandatory: bool = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    model_value: Any = None,
    navigation_index: float = None,
    navigation_strategy: str = None,
    no_data_text: str = None,
    no_filter: bool = None,
    open_all: bool = None,
    open_on_click: bool = None,
    opened: Any = None,
    prepend_gap: typing.Union[str, float] = None,
    return_object: bool = None,
    rounded: typing.Union[str, float, bool] = None,
    search: str = None,
    select_strategy: str = None,
    selectable: bool = None,
    selected: Any = None,
    selected_color: str = None,
    separate_roots: bool = None,
    slim: bool = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    tooltip: str = None,
    true_icon: Any = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value_comparator: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Treeview, Any]:
    """Widget for the Vuetify v-treeview component, see https://vuetifyjs.com/en/api/v-treeview/
    :param activatable: Allows user to mark a node as active by clicking on it.
    :param activated: Array of ids of activated nodes.
    :param active_class: The class applied to the component when it is in an active state.
    :param active_color: Deprecated, use `color` instead.
    :param active_strategy: Affects how items with children behave when activated. If not specified, the **single-independent** strategy will be used.
    - **leaf:** Only leaf nodes (items without children) can be activated.
    - **single-leaf:** Similar as **leaf**, but only a single item can be activated at a time.
    - **independent:** All nodes can be activated whether they have children or not.
    - **single-independent:** Similar as **independent**, but only a single item can be activated at a time.
    :param base_color: Sets the color of component when not focused.
    :param bg_color: Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param collapse_icon: Icon to display when the list item is expanded.
    :param color: Applies specified color to the active node - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param custom_filter: Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted.
    :param custom_key_filter: Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified.
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Disables selection for all nodes.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param expand_icon: Icon used to indicate that a node can be expanded.
    :param false_icon: The icon used when inactive.
    :param filter_keys: Array of specific keys to filter on the item.
    :param filter_mode: Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.

    - **some**: There is at least one match from either the custom filter or the custom key filter.
    - **every**: All columns match either the custom filter or the custom key filter.
    - **union**: There is at least one match from the custom filter, or all columns match the custom key filters.
    - **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.
    :param filterable: **FOR INTERNAL USE ONLY** Prevents list item selection using [space] key and pass it back to the text input. Used internally for VAutocomplete and VCombobox.
    :param fluid: Removes indentation from nested items.
    :param height: Sets the height for the component.
    :param hide_actions: Hide the expand icon and loading indicator next to each item title.
    :param hide_no_data: Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.
    :param indent: Overrides the indent size for nested groups.
    :param indent_lines: Controls visibility and variant of the indent lines.
    :param indent_lines_color: Sets color of indent lines
    :param indent_lines_opacity: Sets opacity of indent lines
    :param indeterminate_icon: Icon used when node is in an indeterminate state. Only visible when `selectable` is `true`.
    :param item_children: Property on supplied `items` that contains its children.
    :param item_props: Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.
    :param item_title: Property on supplied `items` that contains its title.
    :param item_type: Designates the key on the supplied items that is used for determining the nodes type.
    :param item_value: Property on supplied `items` that contains its value.
    :param items: An array of items used to build the treeview.
    :param items_registration: When set to 'props', skips rendering collapsed items/nodes (for significant performance gains).
    :param lines: Designates a **minimum-height** for all children `v-list-item` components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp) and is not supported in all browsers.
    :param load_children: A function used when dynamically loading children. If this prop is set, then the supplied function will be run if expanding an item that has a `item-children` property that is an empty array. Supports returning a Promise.
    :param loading_icon: Icon used when node is in a loading state.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param model_value: Allows one to control which nodes are selected. The array contains the values of currently selected items. It is equivalent to the `v-model:selected`
    :param navigation_index: Specifies the currently selected navigation index when using `navigationStrategy="track"`. Can be used with `v-model:navigationIndex` for two-way binding. Items at this index receive visual keyboard focus styling and automatic scrolling. Note: Only works with the `items` prop, not with slotted items.
    :param navigation_strategy: Determines keyboard navigation behavior. **focus** (default) moves DOM focus to items, suitable for traditional lists. **track** provides visual keyboard focus without moving DOM focus, ideal for command palettes and autocomplete where an external element retains focus. When track mode is active, items automatically receive `tabindex="-1"`, proper `aria-activedescendant` is set on the list container, and keyboard-focused items display focus-visible styling with auto-scrolling.
    :param no_data_text: Text shown when no items are provided to the component.
    :param no_filter: Disables all item filtering.
    :param open_all: When `true` will cause all branch nodes to be opened when component is mounted.
    :param open_on_click: When `true` will cause nodes to be opened by clicking anywhere on it, instead of only opening by clicking on expand icon. When using this prop with `activatable` you will be unable to mark nodes with children as active.
    :param opened: An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`.
    :param prepend_gap: Sets the horizontal spacing between prepend slot and the main content within list item. Also affects indent to ensure expected alignment of group children.
    :param return_object: When `true` will make `v-model`, `v-model:selected`, `v-model:activated` and `v-model:opened` return the complete object instead of just the key.
    :param rounded: Provides an alternative active style for `v-treeview` node. Only visible when `activatable` is `true` and should not be used in conjunction with the `shaped` prop.
    :param search: The search model for filtering results.
    :param select_strategy: Affects how items with children behave when selected.
    - **leaf:** Only leaf nodes (items without children) can be selected.
    - **independent:** All nodes can be selected whether they have children or not.
    - **classic:** Selecting a parent node will cause all children to be selected, parent nodes will be displayed as selected if all their descendants are selected. Only leaf nodes will be added to the model.
    - **trunk**: Same as classic but if all of a node's children are selected then only that node will be added to the model.
    - **branch**: Same as classic but if any of a node's children are selected then that node will also be added to the model.
    :param selectable: Will render a checkbox next to each node allowing them to be selected. Additionally, the **[openOnClick](https://vuetifyjs.com/en/api/v-treeview/#props-open-on-click)** property will be applied internally.
    :param selected: An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`.
    :param selected_color: The color of the selection checkbox.
    :param separate_roots: Applies to `default` variant of `indent-lines`. Prevents showing lines between root-level nodes.
    :param slim: Reduces horizontal spacing for badges, icons, tooltips, and avatars within slim list items to create a more compact visual representation.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param tooltip: A tooltip caption.
    :param true_icon: The icon used when active.
    :param value_comparator: Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
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


def _TreeviewGroup(
    active_color: str = None,
    append_icon: Any = None,
    attributes: dict = {},
    base_color: str = None,
    children: list = [],
    class_: str = None,
    collapse_icon: Any = None,
    color: str = None,
    disabled: bool = None,
    expand_icon: Any = None,
    fluid: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    prepend_icon: Any = None,
    raw_id: typing.Union[str, float] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    title: str = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TreeviewGroup, Any]:
    """Widget for the Vuetify v-treeview-group component, see https://vuetifyjs.com/en/api/v-treeview-group/
    :param active_color: Deprecated, use `color` instead.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param collapse_icon: Icon to display when the list item is expanded.
    :param color: Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).
    :param disabled: Puts all children inputs into a disabled state.
    :param expand_icon: Icon to display when the list item is collapsed.
    :param fluid: Removes indentation from nested items.
    :param prepend_icon: Prepends an icon to the component, uses the same syntax as `v-icon`.
    :param raw_id: Defines the root element's id attribute in the component. If it is provided, the id attribute will be dynamically generated in the format: "v-list-group--id-[rawId]".
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param title: Specify a title text for the component.
    :param tooltip: A tooltip caption.
    :param value: Expands / Collapse the list-group.
    """
    ...


@implements(_TreeviewGroup)
def TreeviewGroup(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TreeviewGroup
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TreeviewGroup


def _TreeviewItem(
    active: bool = None,
    active_class: str = None,
    active_color: str = None,
    append_avatar: str = None,
    append_icon: Any = None,
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
    has_custom_prepend: bool = None,
    height: typing.Union[str, float] = None,
    hide_actions: bool = None,
    href: str = None,
    indent_lines: list = [],
    index: float = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    lines: typing.Union[bool, str, str, str] = None,
    link: bool = None,
    loading: bool = None,
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    nav: bool = None,
    prepend_avatar: str = None,
    prepend_gap: typing.Union[str, float] = None,
    prepend_icon: Any = None,
    replace: bool = None,
    ripple: typing.Union[bool, dict] = None,
    rounded: typing.Union[str, float, bool] = None,
    slim: bool = None,
    slot: str = None,
    style_: str = None,
    subtitle: typing.Union[str, float, bool] = None,
    tabbable: bool = None,
    tabindex: typing.Union[str, float] = None,
    tag: Any = None,
    theme: str = None,
    tile: bool = None,
    title: typing.Union[str, float, bool] = None,
    to: Any = None,
    toggle_icon: Any = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    variant: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.TreeviewItem, Any]:
    """Widget for the Vuetify v-treeview-item component, see https://vuetifyjs.com/en/api/v-treeview-item/
    :param active: Controls the **active** state of the item. This is typically used to highlight the component.
    :param active_class: The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.
    :param active_color: Deprecated, use `color` instead.
    :param append_avatar: Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.
    :param append_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot.
    :param base_color: Sets the color of component when not focused.
    :param border: Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).
    :param color: Applies specified color to the control when in an **active** state or **input-value** is **true** - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors),
    :param density: Adjusts the vertical height used by the component.
    :param disabled: Removes the ability to click or target the component.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param exact: Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.
    :param height: Sets the height for the component.
    :param hide_actions: Hide the expand icon and loading indicator next to each item title.
    :param href: Designates the component as anchor and applies the **href** attribute.
    :param indent_lines: Array of indent lines to render next to the item.
    :param lines: The line declaration specifies the minimum height of the item and can also be controlled from v-list with the same prop.
    :param link: Designates that the component is a link. This is automatic when using the href or to prop.
    :param loading: Places the v-treeview-item into a loading state.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param nav: Reduces the width of v-list-item takes and adds a border radius.
    :param prepend_avatar: Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.
    :param prepend_icon: Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content.
    :param replace: Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.
    :param ripple: Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.
    :param rounded: Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).
    :param slim: Reduces the vertical padding or height of the v-treeview-item, making it more compact.
    :param subtitle: Specify a subtitle text for the component.
    :param tabbable: Is widget tabbable?
    :param tabindex: Controls the tabindex of the list item. When set, overrides the default tabindex behavior. Automatically set to -1 by VList when using `navigationStrategy="track"` to prevent Tab key navigation into items.
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tile: Removes any applied **border-radius** from the component.
    :param title: Generates a `v-list-item-title` component with the supplied value. Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title) attribute, that must be set with `v-bind:title.attr` instead.
    :param to: Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation.
    :param toggle_icon: Allows customization of the icon used to toggle the expansion and collapse of treeview branches.
    :param tooltip: A tooltip caption.
    :param value: The value used for selection. Obtained from [`v-list`](https://vuetifyjs.com/en/api/v-list)'s `v-model:selected` when the item is selected.
    :param variant: Applies a distinct style to the component.
    :param width: Sets the width for the component.
    """
    ...


@implements(_TreeviewItem)
def TreeviewItem(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.TreeviewItem
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _TreeviewItem


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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    validate_on: str = None,
    validation_value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Validation, Any]:
    """Widget for the Vuetify v-validation component, see https://vuetifyjs.com/en/api/v-validation/
    :param disabled: Removes the ability to click or target the component.
    :param error: Puts the input in a manual error state.
    :param error_messages: Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.
    :param focused: Forces a focused state styling on the component.
    :param label: Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.
    :param max_errors: Control the maximum number of shown errors from validation.
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param name: Sets the component's name attribute.
    :param readonly: Puts input in readonly state.
    :param rules: Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param validate_on: Change what type of event triggers validation to run.
    :param validation_value: The value used when applying validation rules.
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


def _Video(
    aspect_ratio: typing.Union[str, float] = None,
    attributes: dict = {},
    autoplay: bool = None,
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    controls_props: Any = None,
    controls_transition: typing.Union[str, bool] = None,
    controls_variant: str = None,
    density: str = None,
    detached: bool = None,
    duration: float = None,
    eager: bool = None,
    elevation: typing.Union[str, float] = None,
    floating: bool = None,
    height: typing.Union[str, float] = None,
    hide_fullscreen: bool = None,
    hide_overlay: bool = None,
    hide_play: bool = None,
    hide_volume: bool = None,
    image: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    max_height: typing.Union[str, float] = None,
    max_width: typing.Union[str, float] = None,
    min_height: typing.Union[str, float] = None,
    min_width: typing.Union[str, float] = None,
    muted: bool = None,
    no_fullscreen: bool = None,
    pills: bool = None,
    playing: bool = None,
    progress: float = None,
    rounded: typing.Union[str, float, bool, list] = None,
    slot: str = None,
    split_time: bool = None,
    src: str = None,
    start_at: typing.Union[str, float] = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    track_color: str = None,
    type: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    volume: typing.Union[str, float] = None,
    volume_props: str = None,
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Video, Any]:
    """Widget for the Vuetify v-video component, see https://vuetifyjs.com/en/api/v-video/
    :param aspect_ratio: Sets the aspect ratio for the playback, calculated as width/height.
    :param autoplay: Starts loading the media file without waiting for user to click. Playback begins once enough data is loaded.
    :param background_color: Container background color.
    :param color: General color applied to icons and sliders.
    :param controls_props: Pass props through to the `v-video-controls` component. Accepts an object with anything from [v-video-controls](https://vuetifyjs.com/en/api/v-video-controls/#props) props, camelCase keys are recommended.
    :param controls_transition: The reveal transition applied to the VVideoControls component once the media file is loaded.
    :param controls_variant: Variant passed to the VVideoControls component.
    :param density: Adjusts the vertical height used by the component.
    :param detached: Moves the container below so it won't obstruct the video.
    :param duration: Total duration of the video used to calculate displayed time.
    :param eager: Silently loades the media file without waiting for user to click.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param floating: Introduces visual spacing from the video boundaries.
    :param height: Sets the height for the component.
    :param hide_fullscreen: Hides default fullscreen button.
    :param hide_overlay: Hide center play icon.
    :param hide_play: Hides default play button.
    :param hide_volume: Hides default volume control.
    :param image: Apply a specific image as cover before the video is loaded.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param muted: Hides volume control and disables the playback sound.
    :param no_fullscreen: Disable fullscreen and hide the default fullscreen button.
    :param pills: Makes the container transparent and shows inner actions in separated boxes.
    :param playing: Applies correct icon of the default play button.
    :param progress: Controls main slider value (0 ~ 100)
    :param rounded: Applies a border radius to the video container and the controls. Accepts array of two values to customize elements separately.
    :param split_time: Splits time into elapsed and remaining on each side of the main slider.
    :param src: Media file URL
    :param start_at: Moves progress to the specified time (in seconds) once the media file is loaded.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param track_color: Passed to the main slider `color` prop.
    :param type: Media file type (optional)
    :param variant: Applies a distinct style to the component.
    :param volume: Volume value passed to the underlying control and slots.
    :param volume_props: Props passed down to the VVideoVolume component.
    :param width: Sets the width for the component.
    """
    ...


@implements(_Video)
def Video(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.Video
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _Video


def _VideoControls(
    attributes: dict = {},
    background_color: str = None,
    children: list = [],
    class_: str = None,
    color: str = None,
    density: str = None,
    detached: bool = None,
    duration: float = None,
    elevation: typing.Union[str, float] = None,
    floating: bool = None,
    fullscreen: bool = None,
    hide_fullscreen: bool = None,
    hide_play: bool = None,
    hide_volume: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    pills: bool = None,
    playing: bool = None,
    progress: float = None,
    slot: str = None,
    split_time: bool = None,
    style_: str = None,
    tabbable: bool = None,
    theme: str = None,
    tooltip: str = None,
    track_color: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    variant: str = None,
    volume: typing.Union[str, float] = None,
    volume_props: str = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.VideoControls, Any]:
    """Widget for the Vuetify v-video-controls component, see https://vuetifyjs.com/en/api/v-video-controls/
    :param background_color: Container background color.
    :param color: General color applied to icons and sliders.
    :param density: Adjusts the vertical height used by the component.
    :param detached: Moves the container below so it won't obstruct the video.
    :param duration: Total duration of the video used to calculate displayed time.
    :param elevation: Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).
    :param floating: Introduces visual spacing from the video boundaries.
    :param fullscreen: Applies correct icon on the default fullscreen button.
    :param hide_fullscreen: Hides default fullscreen button.
    :param hide_play: Hides default play button.
    :param hide_volume: Hides default volume control.
    :param pills: Makes the container transparent and shows inner actions in separated boxes.
    :param playing: Applies correct icon of the default play button.
    :param progress: Controls main slider value (0 ~ 100)
    :param split_time: Splits time into elapsed and remaining on each side of the main slider.
    :param tabbable: Is widget tabbable?
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param track_color: Passed to the main slider `color` prop.
    :param variant: Applies a distinct style to the component.
    :param volume: Volume value passed to the underlying control and slots.
    :param volume_props: Props passed down to the VVideoVolume component.
    """
    ...


@implements(_VideoControls)
def VideoControls(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.VideoControls
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _VideoControls


def _VideoVolume(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    direction: str = None,
    inline: bool = None,
    label: str = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    menu_props: Any = None,
    model_value: float = None,
    slider_props: dict = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tooltip: str = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.VideoVolume, Any]:
    """Widget for the Vuetify v-video-volume component, see https://vuetifyjs.com/en/api/v-video-volume/
    :param direction: Switch between horizontal and vertical slider.
    :param inline: Display slider next to the icon. VMenu won't be displayed on click. Recomended to pair with **sliderProps** to configure slider width.
    :param label: Text to display in tooltip and passed to `aria-label`.
    :param menu_props: Props passed to VMenu containing volume slider. Useful to adjust **location** and control menu alignment
    :param model_value: Volume value (0 ~ 100)
    :param slider_props: Selected props to customize volume slider.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    """
    ...


@implements(_VideoVolume)
def VideoVolume(**kwargs):
    if isinstance(kwargs.get("layout"), dict):
        kwargs["layout"] = w.Layout(**kwargs["layout"])
    widget_cls = ipyvuetify.generated.VideoVolume
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return ValueElement("v_model", comp, kwargs=kwargs)


del _VideoVolume


def _VirtualScroll(
    attributes: dict = {},
    children: list = [],
    class_: str = None,
    height: typing.Union[str, float] = None,
    item_height: typing.Union[str, float] = None,
    item_key: str = None,
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    width: typing.Union[str, float] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.VirtualScroll, Any]:
    """Widget for the Vuetify v-virtual-scroll component, see https://vuetifyjs.com/en/api/v-virtual-scroll/
    :param height: Height of the component as a css value/
    :param item_height: Height in pixels of each item to display.
    :param item_key: Should point to a property with a unique value for each item, if not set then item index will be used as a key which may result in unnecessary re-renders.
    :param items: The array of items to display.
    :param max_height: Sets the maximum height for the component.
    :param max_width: Sets the maximum width for the component.
    :param min_height: Sets the minimum height for the component.
    :param min_width: Sets the minimum width for the component.
    :param renderless: Disables default component rendering functionality. The parent node must be [a positioned element](https://developer.mozilla.org/en-US/docs/Web/CSS/position#types_of_positioning), e.g. using `position: relative;`
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param width: Sets the width for the component.
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
    events: list = [],
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
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
    v_bind: str = None,
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
    crossfade: bool = None,
    direction: str = None,
    disabled: bool = None,
    layout: Union[Dict[str, Any], Element[ipywidgets.widgets.widget_layout.Layout]] = {},
    mandatory: typing.Union[bool, str] = None,
    model_value: Any = None,
    next_icon: Any = None,
    prev_icon: Any = None,
    reverse: bool = None,
    selected_class: str = None,
    show_arrows: typing.Union[str, bool] = None,
    slot: str = None,
    style_: str = None,
    tabbable: bool = None,
    tag: Any = None,
    theme: str = None,
    tooltip: str = None,
    touch: bool = None,
    transition_duration: float = None,
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    vertical_arrows: typing.Union[bool, str, str] = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.Window, Any]:
    """Widget for the Vuetify v-window component, see https://vuetifyjs.com/en/api/v-window/
    :param continuous: If `true`, window will "wrap around" from the last item to the first, and from the first item to the last.
    :param crossfade: Enables crossfade transition.
    :param direction: The transition direction when changing windows.
    :param disabled: Removes the ability to click or target the component.
    :param mandatory: Forces at least one item to always be selected (if available).
    :param model_value: The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.
    :param next_icon: Icon used for the "next" button if `show-arrows` is `true`.
    :param prev_icon: Icon used for the "prev" button if `show-arrows` is `true`.
    :param reverse: Reverse the normal transition direction.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param show_arrows: Display the "next" and "prev" buttons.
    :param tabbable: Is widget tabbable?
    :param tag: Specify a custom tag used on the root element.
    :param theme: Specify a theme for this component and all of its children.
    :param tooltip: A tooltip caption.
    :param touch: Provide a custom **left** and **right** function when swiped left or right.
    :param transition_duration: Overrides transition duration. Does not work in firefox, safari <18, or with `prefers-reduced-motion: reduce`.
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
    v_bind: str = None,
    v_model: Any = "!!disabled!!",
    v_on: str = None,
    v_slots: list = [],
    value: Any = None,
    on_v_model: typing.Callable[[Any], Any] = None,
) -> ValueElement[ipyvuetify.generated.WindowItem, Any]:
    """Widget for the Vuetify v-window-item component, see https://vuetifyjs.com/en/api/v-window-item/
    :param disabled: Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.
    :param eager: Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.
    :param reverse_transition: Sets the reverse transition.
    :param selected_class: Configure the active CSS class applied when an item is selected.
    :param tabbable: Is widget tabbable?
    :param tooltip: A tooltip caption.
    :param transition: The transition used when the component progressing through items. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.
    :param value: The value used when the component is selected in a group. If not provided, a unique ID will be used.
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
