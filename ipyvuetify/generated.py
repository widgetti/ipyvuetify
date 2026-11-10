from ipyvue import VueWidget
from traitlets import Any, Bool, Dict, Float, Unicode, Union
from traitlets import List as TList

from ._version import semver


class VuetifyWidget(VueWidget):

    _model_name = Unicode("VuetifyWidgetModel").tag(sync=True)

    _view_name = Unicode("VuetifyView").tag(sync=True)

    _view_module = Unicode("jupyter-vuetify").tag(sync=True)

    _model_module = Unicode("jupyter-vuetify").tag(sync=True)

    _view_module_version = Unicode(semver).tag(sync=True)

    _model_module_version = Unicode(semver).tag(sync=True)

    _metadata = Dict(default_value=None, allow_none=True).tag(sync=True)


class Alert(VuetifyWidget):
    """Widget for the Vuetify v-alert component, see https://vuetifyjs.com/en/api/v-alert/"""

    _model_name = Unicode("AlertModel").tag(sync=True)

    border = Union(
        [Bool(), Unicode(), Unicode(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Adds a colored border to the component.",
    ).tag(sync=True)

    border_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies the color of the border. Only used in combination with **border** prop. Accepts any color value.",
    ).tag(sync=True)

    closable = Bool(
        default_value=None, allow_none=True, help="Adds a close icon that can hide the alert."
    ).tag(sync=True)

    close_icon = Any(help="Change the default icon used for **closable** alerts.").tag(sync=True)

    close_label = Unicode(
        default_value=None,
        allow_none=True,
        help="Text used for *aria-label* on **closable** alerts. Can also be customized globally in [Internationalization](https://vuetifyjs.com/en/customization/internationalization).",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    icon_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The specific size of the icon, can use named sizes.",
    ).tag(sync=True)

    icon_sizes = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of tuples that define the icon sizes for each named size.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="Controls whether the component is visible or hidden.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prominent = Bool(
        default_value=None,
        allow_none=True,
        help="Displays a larger vertically centered icon to draw more attention.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None, allow_none=True, help="Removes the component's border-radius."
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Create a specialized alert that uses a contextual color and has a pre-defined icon.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class AlertTitle(VuetifyWidget):
    """Widget for the Vuetify v-alert-title component, see https://vuetifyjs.com/en/api/v-alert-title/"""

    _model_name = Unicode("AlertTitleModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class App(VuetifyWidget):
    """Widget for the Vuetify v-app component, see https://vuetifyjs.com/en/api/v-app/"""

    _model_name = Unicode("AppModel").tag(sync=True)

    overlaps = TList(
        Any(), default_value=None, allow_none=True, help="**FOR INTERNAL USE ONLY**"
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)


class AppBar(VuetifyWidget):
    """Widget for the Vuetify v-app-bar component, see https://vuetifyjs.com/en/api/v-app-bar/"""

    _model_name = Unicode("AppBarModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies position: absolute to the component."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    collapse = Bool(
        default_value=None,
        allow_none=True,
        help="Morphs the component into a collapsed state, reducing its maximum width.",
    ).tag(sync=True)

    collapse_position = Unicode(
        default_value=None, allow_none=True, help="Specifies side to attach the collapsed toolbar."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    extended = Bool(
        default_value=None,
        allow_none=True,
        help="Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop. When false, will not show extension slot even if content is present.",
    ).tag(sync=True)

    extension_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designate an explicit height for the `extension` slot.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None, allow_none=True, help="Removes the component's **box-shadow**."
    ).tag(sync=True)

    floating = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **display: inline-flex** to the component.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.",
    ).tag(sync=True)

    image = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies a [v-img](https://vuetifyjs.com/en/components/images) as the component's background.",
    ).tag(sync=True)

    location = Unicode(
        default_value=None, allow_none=True, help="Aligns the component towards the top or bottom."
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Assign a specific name for layout registration."
    ).tag(sync=True)

    order = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Adjust the order of the component in relation to its registration order.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    scroll_behavior = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify an action to take when the scroll position of **scroll-target** reaches **scroll-threshold**. Accepts any combination of hide, inverted, collapse, elevate, and fade-image. Multiple values can be used, separated by a space.",
    ).tag(sync=True)

    scroll_target = Unicode(
        default_value=None,
        allow_none=True,
        help="The element to target for scrolling events. Uses `window` by default.",
    ).tag(sync=True)

    scroll_threshold = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The amount of scroll distance down before **scroll-behavior** activates.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)


class AppBarNavIcon(VuetifyWidget):
    """Widget for the Vuetify v-app-bar-nav-icon component, see https://vuetifyjs.com/en/api/v-app-bar-nav-icon/"""

    _model_name = Unicode("AppBarNavIconModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    block = Bool(
        default_value=None, allow_none=True, help="Expands the button to 100% of available space."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the button box shadow. This is different than using the 'flat' variant.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component. The button will become _round_."
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    readonly = Bool(
        default_value=None,
        allow_none=True,
        help="Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.",
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    slim = Bool(default_value=None, allow_none=True, help="Reduces padding to 0 8px.").tag(
        sync=True
    )

    stacked = Bool(
        default_value=None, allow_none=True, help="Displays the button as a flex-column."
    ).tag(sync=True)

    symbol = Any(
        help="The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/)."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify content text for the component.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class AppBarTitle(VuetifyWidget):
    """Widget for the Vuetify v-app-bar-title component, see https://vuetifyjs.com/en/api/v-app-bar-title/"""

    _model_name = Unicode("AppBarTitleModel").tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)


class Autocomplete(VuetifyWidget):
    """Widget for the Vuetify v-autocomplete component, see https://vuetifyjs.com/en/api/v-autocomplete/"""

    _model_name = Unicode("AutocompleteModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    auto_select_first = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="When searching, will always highlight the first option and select it on blur. `exact` will only highlight and select exact matches.",
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True, help="Enables autofocus.").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    chips = Bool(
        default_value=None, allow_none=True, help="Changes display of selections to chips."
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clear_on_select = Bool(
        default_value=None,
        allow_none=True,
        help="Reset the search text when a selection is made while using the **multiple** prop.",
    ).tag(sync=True)

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    closable_chips = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the [closable](https://vuetifyjs.com/en/api/v-chip/#props-closable) prop on all [v-chip](https://vuetifyjs.com/en/components/chips/) components.",
    ).tag(sync=True)

    close_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text set to the inputs `aria-label` and `title` when input menu is closed.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Float(
        default_value=None, allow_none=True, help="Function returns the counter display text."
    ).tag(sync=True)

    custom_filter = Any(
        help="Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted."
    ).tag(sync=True)

    custom_key_filter = Any(
        help="Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    filter_keys = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Array of specific keys to filter on the item.",
    ).tag(sync=True)

    filter_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.\n\n- **some**: There is at least one match from either the custom filter or the custom key filter.\n- **every**: All columns match either the custom filter or the custom key filter.\n- **union**: There is at least one match from the custom filter, or all columns match the custom key filters.\n- **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_no_data = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.",
    ).tag(sync=True)

    hide_selected = Bool(
        default_value=None,
        allow_none=True,
        help="Do not display in the select menu items that are already selected.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-autocomplete/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    item_children = Unicode(
        default_value=None, allow_none=True, help="This property currently has **no effect**."
    ).tag(sync=True)

    item_color = Unicode(
        default_value=None, allow_none=True, help="Sets color of selected items."
    ).tag(sync=True)

    item_props = Unicode(
        default_value=None,
        allow_none=True,
        help="Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.",
    ).tag(sync=True)

    item_title = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its title.",
    ).tag(sync=True)

    item_type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Can be an array of objects or strings. By default objects should have **title** and **value** properties, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props). Keys to use for these can be changed with the **item-title**, **item-value**, and **item-props** props.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    list_props = Any(
        help="Pass props through to the `v-list` component. Accepts an object with anything from [v-list](https://vuetifyjs.com/en/api/v-list/#props) props, camelCase keys are recommended."
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    menu = Bool(
        default_value=None, allow_none=True, help="Renders with the menu open by default."
    ).tag(sync=True)

    menu_icon = Any(help="Sets the the spin icon.").tag(sync=True)

    menu_props = Any(
        help="Pass props through to the `v-menu` component. Accepts an object with anything from [v-menu](https://vuetifyjs.com/en/api/v-menu/#props) props, camelCase keys are recommended."
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None,
        allow_none=True,
        help="Changes select to multiple. Accepts array for value.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    no_auto_scroll = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when no items are provided to the component.",
    ).tag(sync=True)

    no_filter = Bool(
        default_value=None,
        allow_none=True,
        help="Do not apply filtering when searching. Useful when data is being filtered server side.",
    ).tag(sync=True)

    open_on_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Open's the menu whenever the clear icon is clicked.",
    ).tag(sync=True)

    open_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text set to the inputs **aria-label** and **title** when input menu is open.",
    ).tag(sync=True)

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-autocomplete/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    role = Unicode(
        default_value=None, allow_none=True, help="The role attribute applied to the input."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a border radius to the input.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    search = Unicode(
        default_value=None, allow_none=True, help="Text input used to filter items."
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True, help="Sets input type.").tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Avatar(VuetifyWidget):
    """Widget for the Vuetify v-avatar component, see https://vuetifyjs.com/en/api/v-avatar/"""

    _model_name = Unicode("AvatarModel").tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    end = Bool(
        default_value=None, allow_none=True, help="Applies margin at the start of the component."
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    image = Unicode(
        default_value=None,
        allow_none=True,
        help="Apply a specific image using [v-img](https://vuetifyjs.com/en/components/images/).",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    start = Bool(
        default_value=None, allow_none=True, help="Applies margin at the end of the component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class AvatarGroup(VuetifyWidget):
    """Widget for the Vuetify v-avatar-group component, see https://vuetifyjs.com/en/api/v-avatar-group/"""

    _model_name = Unicode("AvatarGroupModel").tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Applies border styles to the child [v-avatar](https://vuetifyjs.com/en/components/avatars) components.",
    ).tag(sync=True)

    gap = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the overlap gap between avatars. Negative values cause avatars to overlap.",
    ).tag(sync=True)

    hoverable = Bool(
        default_value=None, allow_none=True, help="Enables a hover animation on child avatars."
    ).tag(sync=True)

    item_props = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    limit = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The total number of avatars to display, including the overflow indicator. E.g. a limit of `3` with 5 items renders 2 avatars and a `+3` overflow indicator.",
    ).tag(sync=True)

    overflow_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Custom text to display in the overflow avatar. Defaults to `+N` where N is the number of hidden items.",
    ).tag(sync=True)

    reverse = Bool(
        default_value=None, allow_none=True, help="Reverses the stacking order of the avatars."
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the size of all child avatars.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    vertical = Bool(
        default_value=None,
        allow_none=True,
        help="Stacks avatars vertically instead of horizontally.",
    ).tag(sync=True)


class Badge(VuetifyWidget):
    """Widget for the Vuetify v-badge component, see https://vuetifyjs.com/en/api/v-badge/"""

    _model_name = Unicode("BadgeModel").tag(sync=True)

    bordered = Bool(
        default_value=None,
        allow_none=True,
        help="Applies a **2px** by default and **1.5px** border around the badge when using the **dot** property.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    content = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Text content to show in the badge.",
    ).tag(sync=True)

    dot = Bool(
        default_value=None,
        allow_none=True,
        help="Reduce the size of the badge and hide its contents.",
    ).tag(sync=True)

    floating = Bool(
        default_value=None,
        allow_none=True,
        help="Move the badge further away from the slotted content. Equivalent to an 8px offset.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    inline = Bool(
        default_value=None,
        allow_none=True,
        help="Display as an inline block instead of absolute position. **location**, **floating**, and **offset** will have no effect.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None, allow_none=True, help="The **aria-label** used for the badge."
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum number allowed when using the **content** prop with a `number` like value. If the content number exceeds the maximum value, a `+` suffix is added.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="Controls whether the component is visible or hidden.",
    ).tag(sync=True)

    offset_x = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Offset the badge on the x-axis.",
    ).tag(sync=True)

    offset_y = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Offset the badge on the y-axis.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a specified color to the control text - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Banner(VuetifyWidget):
    """Widget for the Vuetify v-banner component, see https://vuetifyjs.com/en/api/v-banner/"""

    _model_name = Unicode("BannerModel").tag(sync=True)

    avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates a specific src image to pass to the thumbnail.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    lines = Unicode(
        default_value=None,
        allow_none=True,
        help="The amount of visible lines of text before it truncates.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None, allow_none=True, help="Applies the mobile banner styles."
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    stacked = Bool(
        default_value=None,
        allow_none=True,
        help='Forces the banner actions onto a new line. This is not applicable when the banner has `lines="one"`.',
    ).tag(sync=True)

    sticky = Bool(
        default_value=None,
        allow_none=True,
        help="Applies `position: sticky` to the component with `top: 0`. You can find more information on the [MDN documentation for sticky position](https://developer.mozilla.org/en-US/docs/Web/CSS/position).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class BannerActions(VuetifyWidget):
    """Widget for the Vuetify v-banner-actions component, see https://vuetifyjs.com/en/api/v-banner-actions/"""

    _model_name = Unicode("BannerActionsModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)


class BannerText(VuetifyWidget):
    """Widget for the Vuetify v-banner-text component, see https://vuetifyjs.com/en/api/v-banner-text/"""

    _model_name = Unicode("BannerTextModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class BottomNavigation(VuetifyWidget):
    """Widget for the Vuetify v-bottom-navigation component, see https://vuetifyjs.com/en/api/v-bottom-navigation/"""

    _model_name = Unicode("BottomNavigationModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies **position: absolute** to the component."
    ).tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    grow = Bool(
        default_value=None,
        allow_none=True,
        help="Force all [v-btn](https://vuetifyjs.com/en/components/buttons) children to take up all available horizontal space.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the orientation and active state styling of the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Assign a specific name for layout registration."
    ).tag(sync=True)

    order = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Adjust the order of the component in relation to its registration order.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)


class BottomSheet(VuetifyWidget):
    """Widget for the Vuetify v-bottom-sheet component, see https://vuetifyjs.com/en/api/v-bottom-sheet/"""

    _model_name = Unicode("BottomSheetModel").tag(sync=True)

    absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **position: absolute** to the content element.",
    ).tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.",
    ).tag(sync=True)

    capture_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None, allow_none=True, help="Closes component when you click on its content."
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    fullscreen = Bool(
        default_value=None, allow_none=True, help="Changes layout for fullscreen display."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    inset = Bool(
        default_value=None, allow_none=True, help="Reduces the sheet content maximum width to 70%."
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    no_click_animation = Bool(
        default_value=None,
        allow_none=True,
        help="Disables the bounce effect when clicking outside of the content element when using the persistent prop.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is clicked.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is hovered.",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    persistent = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking outside of the element or pressing esc key will not deactivate it.",
    ).tag(sync=True)

    retain_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    scroll_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Strategy used when the component is activate and user scrolls.",
    ).tag(sync=True)

    scrollable = Bool(
        default_value=None,
        allow_none=True,
        help="When set to true, expects a `v-card` and a `v-card-text` component with a designated height. For more information, check out the [scrollable example](https://vuetifyjs.com/en/components/dialogs#scrollable).",
    ).tag(sync=True)

    stick_to_target = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the overlay content to go off-screen when scrolling.",
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    viewport_margin = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom viewport margin for the overlay content",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class Breadcrumbs(VuetifyWidget):
    """Widget for the Vuetify v-breadcrumbs component, see https://vuetifyjs.com/en/api/v-breadcrumbs/"""

    _model_name = Unicode("BreadcrumbsModel").tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it is in an active state.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    divider = Unicode(
        default_value=None, allow_none=True, help="Specifies the dividing character between items."
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)


class BreadcrumbsDivider(VuetifyWidget):
    """Widget for the Vuetify v-breadcrumbs-divider component, see https://vuetifyjs.com/en/api/v-breadcrumbs-divider/"""

    _model_name = Unicode("BreadcrumbsDividerModel").tag(sync=True)

    divider = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Specifies the dividing character between items.",
    ).tag(sync=True)


class BreadcrumbsItem(VuetifyWidget):
    """Widget for the Vuetify v-breadcrumbs-item component, see https://vuetifyjs.com/en/api/v-breadcrumbs-item/"""

    _model_name = Unicode("BreadcrumbsItemModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Btn(VuetifyWidget):
    """Widget for the Vuetify v-btn component, see https://vuetifyjs.com/en/api/v-btn/"""

    _model_name = Unicode("BtnModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    block = Bool(
        default_value=None, allow_none=True, help="Expands the button to 100% of available space."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the button box shadow. This is different than using the 'flat' variant.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component. The button will become _round_."
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    readonly = Bool(
        default_value=None,
        allow_none=True,
        help="Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.",
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    slim = Bool(default_value=None, allow_none=True, help="Reduces padding to 0 8px.").tag(
        sync=True
    )

    spaced = Unicode(
        default_value=None,
        allow_none=True,
        help="Extends content to the edges to move main content from prepend and append slots.",
    ).tag(sync=True)

    stacked = Bool(
        default_value=None, allow_none=True, help="Displays the button as a flex-column."
    ).tag(sync=True)

    symbol = Any(
        help="The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/)."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify content text for the component.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class BtnGroup(VuetifyWidget):
    """Widget for the Vuetify v-btn-group component, see https://vuetifyjs.com/en/api/v-btn-group/"""

    _model_name = Unicode("BtnGroupModel").tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    divided = Bool(
        default_value=None,
        allow_none=True,
        help="Add dividers between children [v-btn](https://vuetifyjs.com/en/components/buttons) components.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class BtnToggle(VuetifyWidget):
    """Widget for the Vuetify v-btn-toggle component, see https://vuetifyjs.com/en/api/v-btn-toggle/"""

    _model_name = Unicode("BtnToggleModel").tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    divided = Bool(
        default_value=None,
        allow_none=True,
        help="Add dividers between children [v-btn](https://vuetifyjs.com/en/components/buttons) components.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Round edge buttons.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None, allow_none=True, help="Removes the component's border-radius."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class Calendar(VuetifyWidget):
    """Widget for the Vuetify v-calendar component, see https://vuetifyjs.com/en/api/v-calendar/"""

    _model_name = Unicode("CalendarModel").tag(sync=True)

    categories = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Specifies what categories to display in the `category` view. This controls the order of the categories as well. If the calendar uses events any categories specified in those events not specified in this value are dynamically rendered in the view unless `category-hide-dynamic` is true.",
    ).tag(sync=True)

    category_days = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The number of days to render in the `category` view.",
    ).tag(sync=True)

    category_for_invalid = Unicode(
        default_value=None,
        allow_none=True,
        help="The category to place events in that have invalid categories. A category is invalid when it is not a string. By default events without a category are not displayed until this value is specified.",
    ).tag(sync=True)

    category_hide_dynamic = Bool(
        default_value=None,
        allow_none=True,
        help="Sets whether categories specified in an event should be hidden if it's not defined in `categories`.",
    ).tag(sync=True)

    category_show_all = Bool(
        default_value=None,
        allow_none=True,
        help="Set whether the `category` view should show all defined `categories` even if there are no events for a category.",
    ).tag(sync=True)

    category_text = Unicode(
        default_value=None,
        allow_none=True,
        help="If categories is a list of objects, you can use this to determine what property to print out as the category text on the calendar. You can provide a function to do some logic or just define the prop name. It's similar to item-text on v-select",
    ).tag(sync=True)

    day_format = Any(
        help="Formats day of the month string that appears in a day to a specified locale"
    ).tag(sync=True)

    end = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The ending date on the calendar (inclusive) in the format of `YYYY-MM-DD`. This may be ignored depending on the `type` of the calendar.",
    ).tag(sync=True)

    event_category = Unicode(
        default_value=None,
        allow_none=True,
        help="Set property of *event*'s category. Instead of a property a function can be given which takes an event and returns the category.",
    ).tag(sync=True)

    event_color = Unicode(
        default_value=None,
        allow_none=True,
        help="A background color for all events or a function which accepts an event object passed to the calendar to return a color.",
    ).tag(sync=True)

    event_end = Unicode(
        default_value=None, allow_none=True, help="Set property of *event*'s end timestamp."
    ).tag(sync=True)

    event_height = Float(
        default_value=None,
        allow_none=True,
        help="The height of an event in pixels in the `month` view and at the top of the `day` views.",
    ).tag(sync=True)

    event_margin_bottom = Float(
        default_value=None, allow_none=True, help="Margin bottom for event"
    ).tag(sync=True)

    event_more = Bool(
        default_value=None,
        allow_none=True,
        help="Whether the more 'button' is displayed on a calendar with too many events in a given day. It will say something like '5 more' and when clicked generates a `click:more` event.",
    ).tag(sync=True)

    event_more_text = Unicode(
        default_value=None,
        allow_none=True,
        help="The text to display in the more 'button' given the number of hidden events.",
    ).tag(sync=True)

    event_name = Unicode(
        default_value=None,
        allow_none=True,
        help="Set property of *event*'s displayed name, or a function which accepts an event object passed to the calendar as the first argument and a flag signalling whether the name is for a timed event (true) or an event over a day.",
    ).tag(sync=True)

    event_overlap_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="One of `stack`, `column`, or a custom render function",
    ).tag(sync=True)

    event_overlap_threshold = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="A value in minutes that's used to determine whether two timed events should be placed in column beside each other or should be treated as slightly overlapping events.",
    ).tag(sync=True)

    event_ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the `v-ripple` directive.",
    ).tag(sync=True)

    event_start = Unicode(
        default_value=None, allow_none=True, help="Set property of *event*'s start timestamp."
    ).tag(sync=True)

    event_text_color = Unicode(
        default_value=None,
        allow_none=True,
        help="A text color for all events or a function which accepts an event object passed to the calendar to return a color.",
    ).tag(sync=True)

    event_timed = Unicode(
        default_value=None,
        allow_none=True,
        help="If Dates or milliseconds are used as the start or end timestamp of an event, this prop can be a string to a property on the event that is truthy if the event is a timed event or a function which takes the event and returns a truthy value if the event is a timed event.",
    ).tag(sync=True)

    events = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of event objects with a property for a start timestamp and optionally a name and end timestamp. If an end timestamp is not given, the value of start will be used. If no name is given, you must provide an implementation for the `event` slot.",
    ).tag(sync=True)

    first_day_of_week = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the first day of the week, starting with 0 for Sunday. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    first_day_of_year = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the day that determines the first week of the year, starting with 0 for Sunday. For ISO 8601 this should be 4. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    locale = Unicode(default_value=None, allow_none=True, help="The locale of the calendar.").tag(
        sync=True
    )

    max_days = Float(
        default_value=None,
        allow_none=True,
        help="The maximum number of days to display in the custom calendar if an `end` day is not set.",
    ).tag(sync=True)

    model_value = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    now = Unicode(
        default_value=None,
        allow_none=True,
        help="Override the day & time which is considered now. This is in the format of `YYYY-MM-DD hh:mm:ss`. The calendar is styled according to now.",
    ).tag(sync=True)

    start = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The starting date on the calendar (inclusive) in the format of `YYYY-MM-DD`. This may be ignored depending on the `type` of the calendar.",
    ).tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="A string which is one of `month`, `week`, `day`, `4day`, `custom-weekly`, `custom-daily`, and `category`. The custom types look at the `start` and `end` dates passed to the component as opposed to the `value`.",
    ).tag(sync=True)

    weekday_format = Any(
        help="Formats day of the week string that appears in the header to specified locale"
    ).tag(sync=True)

    weekdays = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="An array of weekdays to display. Does not affect the order.",
    ).tag(sync=True)


class Card(VuetifyWidget):
    """Widget for the Vuetify v-card component, see https://vuetifyjs.com/en/api/v-card/"""

    _model_name = Unicode("CardModel").tag(sync=True)

    append_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True, help="Removes the card's elevation.").tag(
        sync=True
    )

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hover = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **4dp** of elevation when hovered (default 2dp). You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    image = Unicode(
        default_value=None,
        allow_none=True,
        help="Apply a specific background image to the component.",
    ).tag(sync=True)

    link = Bool(
        default_value=None,
        allow_none=True,
        help="Designates that the component is a link. This is automatic when using the href or to prop.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prepend_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends a [v-icon](https://vuetifyjs.com/en/components/icons/) component to the header."
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    subtitle = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify a subtitle text for the component.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify content text for the component.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify a title text for the component.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class CardActions(VuetifyWidget):
    """Widget for the Vuetify v-card-actions component, see https://vuetifyjs.com/en/api/v-card-actions/"""

    _model_name = Unicode("CardActionsModel").tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class CardItem(VuetifyWidget):
    """Widget for the Vuetify v-card-item component, see https://vuetifyjs.com/en/api/v-card-item/"""

    _model_name = Unicode("CardItemModel").tag(sync=True)

    append_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    prepend_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    subtitle = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify a subtitle text for the component.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    title = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify a title text for the component.",
    ).tag(sync=True)


class CardSubtitle(VuetifyWidget):
    """Widget for the Vuetify v-card-subtitle component, see https://vuetifyjs.com/en/api/v-card-subtitle/"""

    _model_name = Unicode("CardSubtitleModel").tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the component's opacity value",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class CardText(VuetifyWidget):
    """Widget for the Vuetify v-card-text component, see https://vuetifyjs.com/en/api/v-card-text/"""

    _model_name = Unicode("CardTextModel").tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the component's opacity value",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class CardTitle(VuetifyWidget):
    """Widget for the Vuetify v-card-title component, see https://vuetifyjs.com/en/api/v-card-title/"""

    _model_name = Unicode("CardTitleModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class Carousel(VuetifyWidget):
    """Widget for the Vuetify v-carousel component, see https://vuetifyjs.com/en/api/v-carousel/"""

    _model_name = Unicode("CarouselModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a color to the navigation dots - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    continuous = Bool(
        default_value=None, allow_none=True, help="Determines whether carousel is continuous."
    ).tag(sync=True)

    crossfade = Bool(default_value=None, allow_none=True, help="Enables crossfade transition.").tag(
        sync=True
    )

    cycle = Bool(
        default_value=None,
        allow_none=True,
        help="Determines if the carousel should cycle through images.",
    ).tag(sync=True)

    delimiter_icon = Any(help="Sets icon for carousel delimiter.").tag(sync=True)

    direction = Unicode(
        default_value=None, allow_none=True, help="The transition direction when changing windows."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_delimiter_background = Bool(
        default_value=None, allow_none=True, help="Hides the bottom delimiter background."
    ).tag(sync=True)

    hide_delimiters = Bool(
        default_value=None, allow_none=True, help="Hides the carousel's bottom delimiters."
    ).tag(sync=True)

    interval = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The duration between image cycles. Requires the **cycle** prop.",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    next_icon = Any(help="The displayed icon for forcing pagination to the next item.").tag(
        sync=True
    )

    prev_icon = Any(help="The displayed icon for forcing pagination to the previous item.").tag(
        sync=True
    )

    progress = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays a carousel progress bar. Requires the **cycle** prop and **interval**.",
    ).tag(sync=True)

    reverse = Bool(
        default_value=None, allow_none=True, help="Reverse the normal transition direction."
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    show_arrows = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays arrows for next/previous navigation.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    touch = Bool(
        default_value=None,
        allow_none=True,
        help="Provide a custom **left** and **right** function when swiped left or right.",
    ).tag(sync=True)

    transition_duration = Float(
        default_value=None,
        allow_none=True,
        help="Overrides transition duration. Does not work in firefox, safari <18, or with `prefers-reduced-motion: reduce`.",
    ).tag(sync=True)

    vertical_arrows = Union(
        [Bool(), Unicode(), Unicode()], default_value=None, allow_none=True
    ).tag(sync=True)

    vertical_delimiters = Union(
        [Bool(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Displays carousel delimiters vertically.",
    ).tag(sync=True)


class CarouselItem(VuetifyWidget):
    """Widget for the Vuetify v-carousel-item component, see https://vuetifyjs.com/en/api/v-carousel-item/"""

    _model_name = Unicode("CarouselItemModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies position: absolute to the component."
    ).tag(sync=True)

    alt = Unicode(
        default_value=None,
        allow_none=True,
        help="Alternate text for screen readers. Leave empty for decorative images.",
    ).tag(sync=True)

    aspect_ratio = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Calculated as `width/height`, so for a 1920x1080px image this will be `1.7778`. Will be calculated automatically if omitted.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    content_class = Any(help="Apply a custom class to the internal content element.").tag(sync=True)

    cover = Bool(
        default_value=None,
        allow_none=True,
        help="Resizes the background image to cover the entire container.",
    ).tag(sync=True)

    crossorigin = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify that images should be fetched with CORS enabled [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#crossorigin)",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help='Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.',
    ).tag(sync=True)

    draggable = Union(
        [Bool(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Controls the `draggable` behavior of the image. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable).",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    gradient = Unicode(
        default_value=None,
        allow_none=True,
        help="The gradient to apply to the image. Only supports [linear-gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient) syntax, anything else should be done with classes.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    image_class = Any(help="Applies CSS classes to the inner `<img>` element.").tag(sync=True)

    inline = Bool(
        default_value=None,
        allow_none=True,
        help="Display as an inline element instead of a block, also disables flex-grow.",
    ).tag(sync=True)

    lazy_src = Unicode(
        default_value=None,
        allow_none=True,
        help="Something to show while waiting for the main image to load, typically a small base64-encoded thumbnail. Has a slight blur filter applied.  \nNOTE: This prop has no effect unless either `height` or `aspect-ratio` are provided.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    options = Any(
        help="Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) constructor."
    ).tag(sync=True)

    position = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies [object-position](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position) styles to the image and placeholder elements.",
    ).tag(sync=True)

    referrerpolicy = Unicode(
        default_value=None,
        allow_none=True,
        help="Define which referrer is sent when fetching the resource [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#referrerpolicy)",
    ).tag(sync=True)

    reverse_transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the reverse transition.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    sizes = Unicode(
        default_value=None,
        allow_none=True,
        help="For use with `srcset`, see [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes).",
    ).tag(sync=True)

    src = Union(
        [Unicode(), Dict()],
        default_value=None,
        allow_none=True,
        help="The image URL. This prop is mandatory.",
    ).tag(sync=True)

    srcset = Unicode(
        default_value=None,
        allow_none=True,
        help="A set of alternate images to use based on device size. [Read more...](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset).",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="The transition to use when switching from `lazy-src` to `src`. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Checkbox(VuetifyWidget):
    """Widget for the Vuetify v-checkbox component, see https://vuetifyjs.com/en/api/v-checkbox/"""

    _model_name = Unicode("CheckboxModel").tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    defaults_target = Unicode(
        default_value=None,
        allow_none=True,
        help="The target component to provide defaults values for.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    false_icon = Any(help="The icon used when inactive.").tag(sync=True)

    false_value = Any(help="Sets value for falsy state.").tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the input is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-checkbox/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    indeterminate = Bool(
        default_value=None, allow_none=True, help="Sets an indeterminate state for the checkbox."
    ).tag(sync=True)

    indeterminate_icon = Any(help="The icon used when in an indeterminate state.").tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Changes expected model to an array."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-checkbox/#props-hint) to always be visible.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    true_icon = Any(help="The icon used when active.").tag(sync=True)

    true_value = Any(help="Sets value for truthy state.").tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Provides the default type for children selection controls.",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class CheckboxBtn(VuetifyWidget):
    """Widget for the Vuetify v-checkbox-btn component, see https://vuetifyjs.com/en/api/v-checkbox-btn/"""

    _model_name = Unicode("CheckboxBtnModel").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    defaults_target = Unicode(
        default_value=None,
        allow_none=True,
        help="The target component to provide defaults values for.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    false_icon = Any(help="The icon used when inactive.").tag(sync=True)

    false_value = Any(help="Sets value for falsy state.").tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    indeterminate = Bool(
        default_value=None,
        allow_none=True,
        help="Puts the control in an indeterminate state. Used with the [indeterminate-icon](https://vuetifyjs.com/en/api/v-checkbox-btn/#props-indeterminate-icon) property.",
    ).tag(sync=True)

    indeterminate_icon = Any(help="Icon used when the component is in an indeterminate state.").tag(
        sync=True
    )

    inline = Bool(default_value=None, allow_none=True, help="Puts children inputs into a row.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None,
        allow_none=True,
        help="Changes select to multiple. Accepts array for value.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    true_icon = Any(help="The icon used when active.").tag(sync=True)

    true_value = Any(help="Sets value for truthy state.").tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Provides the default type for children selection controls.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)


class Chip(VuetifyWidget):
    """Widget for the Vuetify v-chip component, see https://vuetifyjs.com/en/api/v-chip/"""

    _model_name = Unicode("ChipModel").tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.",
    ).tag(sync=True)

    append_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    closable = Bool(
        default_value=None,
        allow_none=True,
        help="Adds remove button and then a chip can be closed.",
    ).tag(sync=True)

    close_icon = Any(help="Change the default icon used for **close** chips.").tag(sync=True)

    close_label = Unicode(
        default_value=None,
        allow_none=True,
        help="Text used for *aria-label* on the close button in **close** chips. Can also be customized globally in [Internationalization](https://vuetifyjs.com/en/customization/internationalization).",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    draggable = Bool(default_value=None, allow_none=True, help="Makes the chip draggable.").tag(
        sync=True
    )

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    filter = Bool(
        default_value=None, allow_none=True, help="Displays a selection icon when selected."
    ).tag(sync=True)

    filter_icon = Any(help="Change the default icon used for **filter** chips.").tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    label = Bool(
        default_value=None, allow_none=True, help="Applies a medium size border radius."
    ).tag(sync=True)

    link = Bool(
        default_value=None,
        allow_none=True,
        help="Designates that the component is a link. This is automatic when using the href or to prop.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    pill = Bool(default_value=None, allow_none=True, help="Remove `v-avatar` padding.").tag(
        sync=True
    )

    prepend_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height, padding and the font size of the component. Accepts only predefined options: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify content text for the component.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    value = Any(
        help="The value used when a child of a [v-chip-group](https://vuetifyjs.com/en/components/chip-groups)."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class ChipGroup(VuetifyWidget):
    """Widget for the Vuetify v-chip-group component, see https://vuetifyjs.com/en/api/v-chip-group/"""

    _model_name = Unicode("ChipGroupModel").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of component when not focused. Recommended with `color` or `filter` to properly highlight selected items.",
    ).tag(sync=True)

    center_active = Bool(
        default_value=None, allow_none=True, help="Forces the selected chip to be centered."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    column = Bool(
        default_value=None,
        allow_none=True,
        help="Remove horizontal pagination and wrap items as needed.",
    ).tag(sync=True)

    content_class = Any(help="Adds classes to the slide group item.").tag(sync=True)

    direction = Unicode(
        default_value=None, allow_none=True, help="Switch between horizontal and vertical modes."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    filter = Bool(
        default_value=None,
        allow_none=True,
        help="Applies an checkmark icon in front of every chip for using it like a filter.",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Sets the designated mobile breakpoint for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    next_icon = Any(help="Specify the icon to use for the next icon.").tag(sync=True)

    prev_icon = Any(help="Specify the icon to use for the prev icon.").tag(sync=True)

    scroll_to_active = Bool(
        default_value=None,
        allow_none=True,
        help="Keeps the last active element visible when resizing the scrollable container.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    show_arrows = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Force the display of the pagination arrows.",
    ).tag(sync=True)

    symbol = Any(
        help="The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/)."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class ClassIcon(VuetifyWidget):
    """Widget for the Vuetify v-class-icon component, see https://vuetifyjs.com/en/api/v-class-icon/"""

    _model_name = Unicode("ClassIconModel").tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class Code(VuetifyWidget):
    """Widget for the Vuetify v-code component, see https://vuetifyjs.com/en/api/v-code/"""

    _model_name = Unicode("CodeModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class Col(VuetifyWidget):
    """Widget for the Vuetify v-col component, see https://vuetifyjs.com/en/api/v-col/"""

    _model_name = Unicode("ColModel").tag(sync=True)

    align_self = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies the [align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) css property. Available options are: **start**, **center**, **end**, **auto**, **baseline** and **stretch**.",
    ).tag(sync=True)

    cols = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the default number of columns the component extends. Available options are: **1 -> 12** and **auto**.",
    ).tag(sync=True)

    lg = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Changes the number of columns on large and greater breakpoints.",
    ).tag(sync=True)

    md = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Changes the number of columns on medium and greater breakpoints.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the default offset for the column.",
    ).tag(sync=True)

    offset_lg = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the offset of the component on large and greater breakpoints.",
    ).tag(sync=True)

    offset_md = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the offset of the component on medium and greater breakpoints.",
    ).tag(sync=True)

    offset_sm = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the offset of the component on small and greater breakpoints.",
    ).tag(sync=True)

    offset_xl = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the offset of the component on extra large and greater breakpoints.",
    ).tag(sync=True)

    offset_xxl = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the offset of the component on extra extra large and greater breakpoints.",
    ).tag(sync=True)

    order = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the default [order](https://developer.mozilla.org/en-US/docs/Web/CSS/order) for the column.",
    ).tag(sync=True)

    order_lg = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the order of the component on large and greater breakpoints.",
    ).tag(sync=True)

    order_md = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the order of the component on medium and greater breakpoints.",
    ).tag(sync=True)

    order_sm = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the order of the component on small and greater breakpoints.",
    ).tag(sync=True)

    order_xl = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the order of the component on extra large and greater breakpoints.",
    ).tag(sync=True)

    order_xxl = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the order of the component on extra extra large and greater breakpoints.",
    ).tag(sync=True)

    sm = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Changes the number of columns on small and greater breakpoints.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    xl = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Changes the number of columns on extra large and greater breakpoints.",
    ).tag(sync=True)

    xxl = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Changes the number of columns on extra extra large and greater breakpoints.",
    ).tag(sync=True)


class ColorInput(VuetifyWidget):
    """Widget for the Vuetify v-color-input component, see https://vuetifyjs.com/en/api/v-color-input/"""

    _model_name = Unicode("ColorInputModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True, help="Enables autofocus.").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    cancel_text = Unicode(
        default_value=None, allow_none=True, help="Text for the cancel button"
    ).tag(sync=True)

    canvas_height = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Height of canvas."
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    color_pip = Bool(
        default_value=None, allow_none=True, help="Synchronize pip color with current value"
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Float(
        default_value=None, allow_none=True, help="Function returns the counter display text."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    dirty = Bool(
        default_value=None, allow_none=True, help="Manually apply the dirty state styling."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    divided = Bool(
        default_value=None, allow_none=True, help="Adds a divider between the header and controls."
    ).tag(sync=True)

    dot_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the size of the selection dot on the canvas.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    eye_dropper_icon = Any(help="Icon used to trigger EyeDropper API.").tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None,
        allow_none=True,
        help='Prevent showing the default actions buttons. Does not affect `<component :is="actions" />`',
    ).tag(sync=True)

    hide_canvas = Bool(default_value=None, allow_none=True, help="Hides canvas.").tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_eye_dropper = Bool(default_value=None, allow_none=True, help="Hides eyedropper icon.").tag(
        sync=True
    )

    hide_header = Bool(default_value=None, allow_none=True, help="Hide the picker header.").tag(
        sync=True
    )

    hide_inputs = Bool(default_value=None, allow_none=True, help="Hides inputs.").tag(sync=True)

    hide_pip = Bool(default_value=None, allow_none=True, help="Hide pip icon").tag(sync=True)

    hide_sliders = Bool(default_value=None, allow_none=True, help="Hides sliders.").tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hide_title = Bool(default_value=None, allow_none=True, help="Hide the picker title.").tag(
        sync=True
    )

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-color-input/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    landscape = Bool(
        default_value=None, allow_none=True, help="Puts the picker into landscape mode."
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    menu_props = Any().tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="The current selected input type. Syncable with `v-model:mode`.",
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Union(
        [Unicode(), Dict()],
        default_value=None,
        allow_none=True,
        help="Represents the committed v-model value",
    ).tag(sync=True)

    modes = TList(
        Any(), default_value=None, allow_none=True, help="Sets available input types."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    ok_text = Unicode(default_value=None, allow_none=True, help="Text for the ok button").tag(
        sync=True
    )

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-color-input/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    picker_props = Any(
        help="Pass props through to the picker component. Intended for props that conflict with `v-text-field` (`color`, `width`, `rounded`, etc.)"
    ).tag(sync=True)

    pip_icon = Unicode(default_value=None, allow_none=True, help="The icon used for pip").tag(
        sync=True
    )

    pip_location = Unicode(
        default_value=None, allow_none=True, help="Move pip icon to a different slot"
    ).tag(sync=True)

    pip_variant = Unicode(
        default_value=None, allow_none=True, help="Variant of the pip control"
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    role = Unicode(
        default_value=None, allow_none=True, help="The role attribute applied to the input."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a border radius to the input.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    show_swatches = Bool(default_value=None, allow_none=True, help="Displays color swatches.").tag(
        sync=True
    )

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    swatches = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Sets the available color swatches to select from. 2D array of rows and columns, accepts any color format the picker does.",
    ).tag(sync=True)

    swatches_max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height of the swatches section.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True, help="Sets input type.").tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width of the color picker.",
    ).tag(sync=True)


class ColorPicker(VuetifyWidget):
    """Widget for the Vuetify v-color-picker component, see https://vuetifyjs.com/en/api/v-color-picker/"""

    _model_name = Unicode("ColorPickerModel").tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    canvas_height = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Height of canvas."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    divided = Bool(
        default_value=None, allow_none=True, help="Adds a divider between the header and controls."
    ).tag(sync=True)

    dot_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes the size of the selection dot on the canvas.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    eye_dropper_icon = Any(help="Icon used to trigger EyeDropper API.").tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_canvas = Bool(default_value=None, allow_none=True, help="Hides canvas.").tag(sync=True)

    hide_eye_dropper = Bool(default_value=None, allow_none=True, help="Hides eyedropper icon.").tag(
        sync=True
    )

    hide_header = Bool(default_value=None, allow_none=True, help="Hide the picker header.").tag(
        sync=True
    )

    hide_inputs = Bool(default_value=None, allow_none=True, help="Hides inputs.").tag(sync=True)

    hide_sliders = Bool(default_value=None, allow_none=True, help="Hides sliders.").tag(sync=True)

    hide_title = Bool(default_value=None, allow_none=True, help="Hide the picker title.").tag(
        sync=True
    )

    landscape = Bool(
        default_value=None, allow_none=True, help="Puts the picker into landscape mode."
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="The current selected input type. Syncable with `v-model:mode`.",
    ).tag(sync=True)

    model_value = Union(
        [Unicode(), Dict()],
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    modes = TList(
        Any(), default_value=None, allow_none=True, help="Sets available input types."
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    show_swatches = Bool(default_value=None, allow_none=True, help="Displays color swatches.").tag(
        sync=True
    )

    swatches = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Sets the available color swatches to select from. 2D array of rows and columns, accepts any color format the picker does.",
    ).tag(sync=True)

    swatches_max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height of the swatches section.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width of the color picker.",
    ).tag(sync=True)


class Combobox(VuetifyWidget):
    """Widget for the Vuetify v-combobox component, see https://vuetifyjs.com/en/api/v-combobox/"""

    _model_name = Unicode("ComboboxModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    always_filter = Bool(
        default_value=None,
        allow_none=True,
        help='When enabled, dropdown list will always show items matching non-empty value within the field. Recommended when the list is meant to show suggestions rather than options to choose from. For optimal UX, should be combined with `:menu-icon="false"` and `hide-selected`.',
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    auto_select_first = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="When searching, will always highlight the first option and select it on blur. `exact` will only highlight and select exact matches.",
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True, help="Enables autofocus.").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    chips = Bool(
        default_value=None, allow_none=True, help="Changes display of selections to chips."
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clear_on_select = Bool(
        default_value=None,
        allow_none=True,
        help="Reset the search text when a selection is made while using the **multiple** prop.",
    ).tag(sync=True)

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    closable_chips = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the [closable](https://vuetifyjs.com/en/api/v-chip/#props-closable) prop on all [v-chip](https://vuetifyjs.com/en/components/chips/) components.",
    ).tag(sync=True)

    close_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text set to the inputs `aria-label` and `title` when input menu is closed.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Float(
        default_value=None, allow_none=True, help="Function returns the counter display text."
    ).tag(sync=True)

    custom_filter = Any(
        help="Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted."
    ).tag(sync=True)

    custom_key_filter = Any(
        help="Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified."
    ).tag(sync=True)

    delimiters = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts an array of strings that will trigger a new tag when typing. Does not replace the normal Tab and Enter keys.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    filter_keys = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Array of specific keys to filter on the item.",
    ).tag(sync=True)

    filter_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.\n\n- **some**: There is at least one match from either the custom filter or the custom key filter.\n- **every**: All columns match either the custom filter or the custom key filter.\n- **union**: There is at least one match from the custom filter, or all columns match the custom key filters.\n- **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_no_data = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.",
    ).tag(sync=True)

    hide_selected = Bool(
        default_value=None,
        allow_none=True,
        help="Do not display in the select menu items that are already selected.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-combobox/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    item_children = Unicode(
        default_value=None, allow_none=True, help="This property currently has **no effect**."
    ).tag(sync=True)

    item_color = Unicode(
        default_value=None, allow_none=True, help="Sets color of selected items."
    ).tag(sync=True)

    item_props = Unicode(
        default_value=None,
        allow_none=True,
        help="Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.",
    ).tag(sync=True)

    item_title = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its title.",
    ).tag(sync=True)

    item_type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Can be an array of objects or strings. By default objects should have **title** and **value** properties, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props). Keys to use for these can be changed with the **item-title**, **item-value**, and **item-props** props.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    list_props = Any(
        help="Pass props through to the `v-list` component. Accepts an object with anything from [v-list](https://vuetifyjs.com/en/api/v-list/#props) props, camelCase keys are recommended."
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    menu = Bool(
        default_value=None, allow_none=True, help="Renders with the menu open by default."
    ).tag(sync=True)

    menu_icon = Any(help="Sets the the spin icon.").tag(sync=True)

    menu_props = Any(
        help="Pass props through to the `v-menu` component. Accepts an object with anything from [v-menu](https://vuetifyjs.com/en/api/v-menu/#props) props, camelCase keys are recommended."
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None,
        allow_none=True,
        help="Changes select to multiple. Accepts array for value.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    no_auto_scroll = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when no items are provided to the component.",
    ).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True, help="Disables all item filtering.").tag(
        sync=True
    )

    open_on_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Open's the menu whenever the clear icon is clicked.",
    ).tag(sync=True)

    open_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text set to the inputs **aria-label** and **title** when input menu is open.",
    ).tag(sync=True)

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-combobox/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    role = Unicode(
        default_value=None, allow_none=True, help="The role attribute applied to the input."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a border radius to the input.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True, help="Sets input type.").tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class CommandPalette(VuetifyWidget):
    """Widget for the Vuetify v-command-palette component, see https://vuetifyjs.com/en/api/v-command-palette/"""

    _model_name = Unicode("CommandPaletteModel").tag(sync=True)

    absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **position: absolute** to the content element.",
    ).tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.",
    ).tag(sync=True)

    capture_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None, allow_none=True, help="Closes component when you click on its content."
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    custom_filter = Any(
        help="Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted."
    ).tag(sync=True)

    custom_key_filter = Any(
        help="Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    filter_keys = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Array of specific keys to filter on the item.",
    ).tag(sync=True)

    filter_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.\n\n- **some**: There is at least one match from either the custom filter or the custom key filter.\n- **every**: All columns match either the custom filter or the custom key filter.\n- **union**: There is at least one match from the custom filter, or all columns match the custom key filters.\n- **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.",
    ).tag(sync=True)

    fullscreen = Bool(
        default_value=None, allow_none=True, help="Changes layout for fullscreen display."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hotkey = Unicode(
        default_value=None,
        allow_none=True,
        help="Global keyboard shortcut to toggle the palette. Accepts hotkey strings like `'ctrl+shift+p'` or `'meta+j'`. The shortcut is automatically registered on mount and cleaned up on unmount.",
    ).tag(sync=True)

    input_icon = Unicode(
        default_value=None,
        allow_none=True,
        help="Icon to display at the start of the search input field.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of command palette items. Objects should have **title** and optionally **subtitle**, **prependIcon**, **appendIcon**, **prependAvatar**, **appendAvatar**, **hotkey**, **onClick**, **to**, **href**, and **value** properties. Use `type: 'subheader'` with a **title** for section headers, or `type: 'divider'` for visual separators between groups.",
    ).tag(sync=True)

    list_props = Any(
        help="Pass props through to the `v-list` component. Accepts an object with anything from [v-list](https://vuetifyjs.com/en/api/v-list/#props) props, camelCase keys are recommended."
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the visibility of the command palette dialog. Use `v-model` for two-way binding.",
    ).tag(sync=True)

    no_click_animation = Bool(
        default_value=None,
        allow_none=True,
        help="Disables the bounce effect when clicking outside of the content element when using the persistent prop.",
    ).tag(sync=True)

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text displayed when no items match the current search query.",
    ).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True, help="Disables all item filtering.").tag(
        sync=True
    )

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is clicked.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is hovered.",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    persistent = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking outside of the element or pressing esc key will not deactivate it.",
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Placeholder text displayed in the search input."
    ).tag(sync=True)

    retain_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    scroll_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Strategy used when the component is activate and user scrolls.",
    ).tag(sync=True)

    scrollable = Bool(
        default_value=None,
        allow_none=True,
        help="When set to true, expects a `v-card` and a `v-card-text` component with a designated height. For more information, check out the [scrollable example](https://vuetifyjs.com/en/components/dialogs#scrollable).",
    ).tag(sync=True)

    search = Unicode(
        default_value=None,
        allow_none=True,
        help="The current search query. Use `v-model:search` to control or monitor the search input value.",
    ).tag(sync=True)

    stick_to_target = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the overlay content to go off-screen when scrolling.",
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    viewport_margin = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom viewport margin for the overlay content",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class CommandPaletteItemComponent(VuetifyWidget):
    """Widget for the Vuetify v-command-palette-item-component component, see https://vuetifyjs.com/en/api/v-command-palette-item-component/"""

    _model_name = Unicode("CommandPaletteItemComponentModel").tag(sync=True)

    index = Float(default_value=None, allow_none=True).tag(sync=True)

    item = Dict(default_value=None, allow_none=True).tag(sync=True)


class ComponentIcon(VuetifyWidget):
    """Widget for the Vuetify v-component-icon component, see https://vuetifyjs.com/en/api/v-component-icon/"""

    _model_name = Unicode("ComponentIconModel").tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class ConfirmEdit(VuetifyWidget):
    """Widget for the Vuetify v-confirm-edit component, see https://vuetifyjs.com/en/api/v-confirm-edit/"""

    _model_name = Unicode("ConfirmEditModel").tag(sync=True)

    cancel_text = Unicode(
        default_value=None, allow_none=True, help="Text for the cancel button"
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Union(
        [Bool(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Control the disabled state of action buttons. If not provided, internal logic will be used to determine the disabled state.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None,
        allow_none=True,
        help='Prevent showing the default actions buttons. Does not affect `<component :is="actions" />`',
    ).tag(sync=True)

    model_value = Any(help="Represents the committed v-model value").tag(sync=True)

    ok_text = Unicode(default_value=None, allow_none=True, help="Text for the ok button").tag(
        sync=True
    )


class Container(VuetifyWidget):
    """Widget for the Vuetify v-container component, see https://vuetifyjs.com/en/api/v-container/"""

    _model_name = Unicode("ContainerModel").tag(sync=True)

    fluid = Bool(
        default_value=None, allow_none=True, help="Removes viewport maximum-width size breakpoints."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Counter(VuetifyWidget):
    """Widget for the Vuetify v-counter component, see https://vuetifyjs.com/en/api/v-counter/"""

    _model_name = Unicode("CounterModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Determines whether the counter is visible or not.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    max = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum allowed value.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    value = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the current counter value.",
    ).tag(sync=True)


class DataIterator(VuetifyWidget):
    """Widget for the Vuetify v-data-iterator component, see https://vuetifyjs.com/en/api/v-data-iterator/"""

    _model_name = Unicode("DataIteratorModel").tag(sync=True)

    custom_filter = Any(help="Function to filter items.").tag(sync=True)

    custom_key_filter = Any(
        help="Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified."
    ).tag(sync=True)

    custom_key_sort = Any(
        help="Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified."
    ).tag(sync=True)

    expand_on_click = Bool(
        default_value=None, allow_none=True, help="Expands item when the row is clicked."
    ).tag(sync=True)

    expanded = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of expanded items. Can be bound to external variable using **v-model:expanded**.",
    ).tag(sync=True)

    filter_keys = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Array of specific keys to filter on the item.",
    ).tag(sync=True)

    filter_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.\n\n- **some**: There is at least one match from either the custom filter or the custom key filter.\n- **every**: All columns match either the custom filter or the custom key filter.\n- **union**: There is at least one match from the custom filter, or all columns match the custom key filters.\n- **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.",
    ).tag(sync=True)

    group_by = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Configures attributes (and sort order) to group items together.",
    ).tag(sync=True)

    initial_sort_order = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies the initial sort order when an **toggleSort** is called for unsorted property.",
    ).tag(sync=True)

    item_selectable = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains the boolean value indicating if the item is selectable.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    items_length = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    items_per_page = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes how many items per page should be visible. Can be bound to external variable using **v-model:itemsPerPage**.. Setting this prop to `-1` will display all items on the page.",
    ).tag(sync=True)

    loading = Bool(
        default_value=None,
        allow_none=True,
        help="If `true` and no items are provided, then a loading text will be shown.",
    ).tag(sync=True)

    model_value = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    multi_sort = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Let user sort by multiple properties/columns.\n\n- **key**: (optional) when set to `ctrl`, user is required to hold a keyboard key (Ctrl on PC and Command on Mac)\n- **mode**: when user selects a new column to sort by, it will be set first (`prepend`) or last (`append`) in the sort priority. Defaults to `append`\n- **modifier**: (optional) allows user to use both multi-sort modes (`append` and `prepend`) simultaneously\n\n**Note**: object notation requires at least **v3.11.0**",
    ).tag(sync=True)

    must_sort = Bool(
        default_value=None, allow_none=True, help="Forces sorting on the column(s)."
    ).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True, help="Disables all item filtering.").tag(
        sync=True
    )

    page = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The current displayed page number (1-indexed).",
    ).tag(sync=True)

    page_by = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how pagination counts items.\n- **item** paginates by individual items,\n- **auto** paginates by top-level groups and falls back to regular items if **group-by** is empty,\n- **any** paginates by both items and groups combined",
    ).tag(sync=True)

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    search = Unicode(
        default_value=None, allow_none=True, help="Text input used to filter items."
    ).tag(sync=True)

    select_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).",
    ).tag(sync=True)

    show_expand = Bool(default_value=None, allow_none=True, help="Shows the expand icon.").tag(
        sync=True
    )

    show_select = Bool(
        default_value=None,
        allow_none=True,
        help="Shows the column with checkboxes for selecting items in the list.",
    ).tag(sync=True)

    sort_by = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of column keys and sort orders that determines the sort order of the table.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)


class DataTable(VuetifyWidget):
    """Widget for the Vuetify v-data-table component, see https://vuetifyjs.com/en/api/v-data-table/"""

    _model_name = Unicode("DataTableModel").tag(sync=True)

    cell_props = Dict(
        default_value=None,
        allow_none=True,
        help="An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.",
    ).tag(sync=True)

    collapse_icon = Any(help="Icon to display when the expandable row is expanded.").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a color to checkboxes, page size dropdown and sort badges in the table header.",
    ).tag(sync=True)

    custom_filter = Any(help="Function to filter items.").tag(sync=True)

    custom_key_filter = Any(
        help="Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified."
    ).tag(sync=True)

    custom_key_sort = Any(
        help="Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified."
    ).tag(sync=True)

    density = Unicode(
        default_value=None, allow_none=True, help="Adjusts the vertical height of the table rows."
    ).tag(sync=True)

    disable_sort = Bool(
        default_value=None, allow_none=True, help="Toggles rendering of sort button."
    ).tag(sync=True)

    expand_icon = Any(help="Icon to display when the expandable row is collapsed.").tag(sync=True)

    expand_on_click = Bool(
        default_value=None, allow_none=True, help="Expands item when the row is clicked."
    ).tag(sync=True)

    expanded = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of expanded items. Can be bound to external variable using **v-model:expanded**.",
    ).tag(sync=True)

    filter_keys = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Array of specific keys to filter on the item.",
    ).tag(sync=True)

    filter_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.\n\n- **some**: There is at least one match from either the custom filter or the custom key filter.\n- **every**: All columns match either the custom filter or the custom key filter.\n- **union**: There is at least one match from the custom filter, or all columns match the custom key filters.\n- **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.",
    ).tag(sync=True)

    first_icon = Any(help="First icon.").tag(sync=True)

    first_page_label = Unicode(
        default_value=None, allow_none=True, help="Label for first page."
    ).tag(sync=True)

    fixed_footer = Bool(
        default_value=None,
        allow_none=True,
        help="Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.",
    ).tag(sync=True)

    fixed_header = Bool(
        default_value=None, allow_none=True, help="Fixed header to top of table."
    ).tag(sync=True)

    group_by = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Configures attributes (and sort order) to group items together. Can be customized further with `group-header` and `group-summary` slots.",
    ).tag(sync=True)

    group_collapse_icon = Any(help="Icon to display when the row group is expanded.").tag(sync=True)

    group_expand_icon = Any(help="Icon to display when the row group is collapsed.").tag(sync=True)

    header_props = Any(
        help="Pass props to the default header. See [`v-data-table-headers` API](https://vuetifyjs.com/en/api/v-data-table-headers) for more information."
    ).tag(sync=True)

    headers = Unicode(
        default_value=None,
        allow_none=True,
        help="An array of objects that each describe a header column.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Set an explicit height of table.",
    ).tag(sync=True)

    hide_default_body = Bool(
        default_value=None, allow_none=True, help="Hides the default body."
    ).tag(sync=True)

    hide_default_footer = Bool(
        default_value=None, allow_none=True, help="Hides the default footer."
    ).tag(sync=True)

    hide_default_header = Bool(
        default_value=None, allow_none=True, help="Hides the default header."
    ).tag(sync=True)

    hide_no_data = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.",
    ).tag(sync=True)

    hover = Bool(
        default_value=None, allow_none=True, help="Adds a hover effects to a table rows."
    ).tag(sync=True)

    initial_sort_order = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies the initial sort order when an unsorted column is clicked.",
    ).tag(sync=True)

    item_selectable = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that indicates whether the item is selectable.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    items_per_page = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Changes how many items per page should be visible. Can be bound to external variable using **v-model:itemsPerPage**.. Setting this prop to `-1` will display all items on the page.",
    ).tag(sync=True)

    items_per_page_options = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of options to show in the items-per-page dropdown.",
    ).tag(sync=True)

    items_per_page_text = Unicode(
        default_value=None, allow_none=True, help="Text for items-per-page dropdown."
    ).tag(sync=True)

    last_icon = Any(help="Last icon.").tag(sync=True)

    last_page_label = Unicode(default_value=None, allow_none=True, help="Label for last page.").tag(
        sync=True
    )

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    loading_text = Unicode(
        default_value=None, allow_none=True, help="Text shown when the data is loading."
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multi_sort = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Let user sort by multiple properties/columns.\n\n- **key**: (optional) when set to `ctrl`, user is required to hold a keyboard key (Ctrl on PC and Command on Mac)\n- **mode**: when user selects a new column to sort by, it will be set first (`prepend`) or last (`append`) in the sort priority. Defaults to `append`\n- **modifier**: (optional) allows user to use both multi-sort modes (`append` and `prepend`) simultaneously\n\n**Note**: object notation requires at least **v3.11.0**",
    ).tag(sync=True)

    must_sort = Bool(
        default_value=None, allow_none=True, help="Forces sorting on the column(s)."
    ).tag(sync=True)

    next_icon = Any(help="Next icon.").tag(sync=True)

    next_page_label = Unicode(default_value=None, allow_none=True, help="Label for next page.").tag(
        sync=True
    )

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when no items are provided to the component.",
    ).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True, help="Disables all item filtering.").tag(
        sync=True
    )

    page = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The current displayed page number (1-indexed).",
    ).tag(sync=True)

    page_by = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how pagination counts items.\n- **item** paginates by individual items,\n- **auto** paginates by top-level groups and falls back to regular items if **group-by** is empty,\n- **any** paginates by both items and groups combined",
    ).tag(sync=True)

    page_text = Unicode(default_value=None, allow_none=True, help="Label for page number.").tag(
        sync=True
    )

    prev_icon = Any(help="Previous icon.").tag(sync=True)

    prev_page_label = Unicode(
        default_value=None, allow_none=True, help="Label for previous page."
    ).tag(sync=True)

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    row_props = Dict(
        default_value=None,
        allow_none=True,
        help="An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.",
    ).tag(sync=True)

    search = Unicode(
        default_value=None, allow_none=True, help="Text input used to filter items."
    ).tag(sync=True)

    select_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).",
    ).tag(sync=True)

    show_current_page = Bool(
        default_value=None,
        allow_none=True,
        help="Show current page number between prev/next icons.",
    ).tag(sync=True)

    show_expand = Bool(
        default_value=None, allow_none=True, help="Shows the expand toggle in default rows."
    ).tag(sync=True)

    show_select = Bool(
        default_value=None,
        allow_none=True,
        help="Shows the select checkboxes in both the header and rows (if using default rows).",
    ).tag(sync=True)

    sort_asc_icon = Any(help="Icon used for ascending sort button.").tag(sync=True)

    sort_by = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Changes which item property (or properties) should be used for sort order. Can be bound to external variable using **v-model:sortBy**..",
    ).tag(sync=True)

    sort_desc_icon = Any(help="Icon used for descending sort button.").tag(sync=True)

    sort_icon = Any(
        help="Icon used for unsorted columns. By default it uses either **sortAscIcon** or **sortDescIcon** depending on **initialSortOrder**, but can be customized to show a neutral icon instead."
    ).tag(sync=True)

    sticky = Bool(
        default_value=None, allow_none=True, help="Deprecated, use `fixed-header` instead."
    ).tag(sync=True)

    striped = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a background to either **even** or **odd** rows.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class DataTableFooter(VuetifyWidget):
    """Widget for the Vuetify v-data-table-footer component, see https://vuetifyjs.com/en/api/v-data-table-footer/"""

    _model_name = Unicode("DataTableFooterModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    first_icon = Any(help="First icon.").tag(sync=True)

    first_page_label = Unicode(
        default_value=None, allow_none=True, help="Label for first page."
    ).tag(sync=True)

    items_per_page_options = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of options to show in the items-per-page dropdown.",
    ).tag(sync=True)

    items_per_page_text = Unicode(
        default_value=None, allow_none=True, help="Text for items-per-page dropdown."
    ).tag(sync=True)

    last_icon = Any(help="Last icon.").tag(sync=True)

    last_page_label = Unicode(default_value=None, allow_none=True, help="Label for last page.").tag(
        sync=True
    )

    next_icon = Any(help="Next icon.").tag(sync=True)

    next_page_label = Unicode(default_value=None, allow_none=True, help="Label for next page.").tag(
        sync=True
    )

    page_text = Unicode(default_value=None, allow_none=True, help="Label for page number.").tag(
        sync=True
    )

    prev_icon = Any(help="Previous icon.").tag(sync=True)

    prev_page_label = Unicode(
        default_value=None, allow_none=True, help="Label for previous page."
    ).tag(sync=True)

    show_current_page = Bool(
        default_value=None,
        allow_none=True,
        help="Show current page number between prev/next icons.",
    ).tag(sync=True)


class DataTableHeaders(VuetifyWidget):
    """Widget for the Vuetify v-data-table-headers component, see https://vuetifyjs.com/en/api/v-data-table-headers/"""

    _model_name = Unicode("DataTableHeadersModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a color to checkboxes, page size dropdown and sort badges in the table header.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disable_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    fixed_header = Bool(
        default_value=None, allow_none=True, help="Sticks the header to the top of the table."
    ).tag(sync=True)

    header_props = Any(help="Additional props to be be passed to the default header").tag(sync=True)

    initial_sort_order = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    multi_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    sort_asc_icon = Any(help="Icon used for ascending sort button.").tag(sync=True)

    sort_desc_icon = Any(help="Icon used for descending sort button.").tag(sync=True)

    sort_icon = Any(
        help="Icon used for unsorted columns. By default it uses either **sortAscIcon** or **sortDescIcon** depending on **initialSortOrder**, but can be customized to show a neutral icon instead."
    ).tag(sync=True)

    sticky = Bool(
        default_value=None, allow_none=True, help="Deprecated, use `fixed-header` instead."
    ).tag(sync=True)


class DataTableRow(VuetifyWidget):
    """Widget for the Vuetify v-data-table-row component, see https://vuetifyjs.com/en/api/v-data-table-row/"""

    _model_name = Unicode("DataTableRowModel").tag(sync=True)

    cell_props = Dict(
        default_value=None, allow_none=True, help="Props to be applied to the cell."
    ).tag(sync=True)

    collapse_icon = Any().tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    expand_icon = Any().tag(sync=True)

    index = Float(default_value=None, allow_none=True, help="Row index.").tag(sync=True)

    item = Any(help="Data (key, index and column values) of the displayed item.").tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)


class DataTableRows(VuetifyWidget):
    """Widget for the Vuetify v-data-table-rows component, see https://vuetifyjs.com/en/api/v-data-table-rows/"""

    _model_name = Unicode("DataTableRowsModel").tag(sync=True)

    cell_props = Dict(
        default_value=None,
        allow_none=True,
        help="An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.",
    ).tag(sync=True)

    collapse_icon = Any().tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    expand_icon = Any().tag(sync=True)

    group_collapse_icon = Any().tag(sync=True)

    group_expand_icon = Any().tag(sync=True)

    hide_no_data = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays `loading` slot if set to `true`",
    ).tag(sync=True)

    loading_text = Unicode(
        default_value=None, allow_none=True, help="Text shown when the data is loading."
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when no items are provided to the component.",
    ).tag(sync=True)

    row_props = Dict(
        default_value=None,
        allow_none=True,
        help="An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.",
    ).tag(sync=True)


class DataTableServer(VuetifyWidget):
    """Widget for the Vuetify v-data-table-server component, see https://vuetifyjs.com/en/api/v-data-table-server/"""

    _model_name = Unicode("DataTableServerModel").tag(sync=True)

    cell_props = Dict(
        default_value=None,
        allow_none=True,
        help="An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.",
    ).tag(sync=True)

    collapse_icon = Any().tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a color to checkboxes, page size dropdown and sort badges in the table header.",
    ).tag(sync=True)

    custom_key_sort = Any(
        help="Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disable_sort = Bool(
        default_value=None, allow_none=True, help="Toggles rendering of sort button."
    ).tag(sync=True)

    expand_icon = Any().tag(sync=True)

    expand_on_click = Bool(
        default_value=None, allow_none=True, help="Expands item when the row is clicked."
    ).tag(sync=True)

    expanded = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of expanded items. Can be bound to external variable using **v-model:expanded**.",
    ).tag(sync=True)

    first_icon = Any(help="First icon.").tag(sync=True)

    first_page_label = Unicode(
        default_value=None, allow_none=True, help="Label for first page."
    ).tag(sync=True)

    fixed_footer = Bool(
        default_value=None,
        allow_none=True,
        help="Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.",
    ).tag(sync=True)

    fixed_header = Bool(
        default_value=None,
        allow_none=True,
        help="Use the fixed-header prop together with the height prop to fix the header to the top of the table.",
    ).tag(sync=True)

    group_by = TList(
        Any(), default_value=None, allow_none=True, help="Defines the grouping of the table items."
    ).tag(sync=True)

    group_collapse_icon = Any().tag(sync=True)

    group_expand_icon = Any().tag(sync=True)

    header_props = Any(
        help="Pass props to the default header. See [`v-data-table-server` API](https://vuetifyjs.com/en/api/v-data-table-server) for more information."
    ).tag(sync=True)

    headers = Unicode(
        default_value=None,
        allow_none=True,
        help="An array of objects that each describe a header column.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Use the height prop to set the height of the table.",
    ).tag(sync=True)

    hide_default_body = Bool(
        default_value=None, allow_none=True, help="Hides the default body."
    ).tag(sync=True)

    hide_default_footer = Bool(
        default_value=None, allow_none=True, help="Hides the default footer."
    ).tag(sync=True)

    hide_default_header = Bool(
        default_value=None, allow_none=True, help="Hides the default header."
    ).tag(sync=True)

    hide_no_data = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.",
    ).tag(sync=True)

    hover = Bool(
        default_value=None,
        allow_none=True,
        help="Will add a hover effect to a table's row when the mouse is over it.",
    ).tag(sync=True)

    initial_sort_order = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies the initial sort order when an unsorted column is clicked.",
    ).tag(sync=True)

    item_selectable = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that indicates whether the item is selectable.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    items_length = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Number of all items."
    ).tag(sync=True)

    items_per_page = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The number of items to display on each page.",
    ).tag(sync=True)

    items_per_page_options = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of options to show in the items-per-page dropdown.",
    ).tag(sync=True)

    items_per_page_text = Unicode(
        default_value=None, allow_none=True, help="Text for items-per-page dropdown."
    ).tag(sync=True)

    last_icon = Any(help="Last icon.").tag(sync=True)

    last_page_label = Unicode(default_value=None, allow_none=True, help="Label for last page.").tag(
        sync=True
    )

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays `loading` slot if set to `true`",
    ).tag(sync=True)

    loading_text = Unicode(
        default_value=None, allow_none=True, help="Text shown when the data is loading."
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multi_sort = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Let user sort by multiple properties/columns.\n\n- **key**: (optional) when set to `ctrl`, user is required to hold a keyboard key (Ctrl on PC and Command on Mac)\n- **mode**: when user selects a new column to sort by, it will be set first (`prepend`) or last (`append`) in the sort priority. Defaults to `append`\n- **modifier**: (optional) allows user to use both multi-sort modes (`append` and `prepend`) simultaneously\n\n**Note**: object notation requires at least **v3.11.0**",
    ).tag(sync=True)

    must_sort = Bool(
        default_value=None, allow_none=True, help="Forces sorting on the column(s)."
    ).tag(sync=True)

    next_icon = Any(help="Next icon.").tag(sync=True)

    next_page_label = Unicode(default_value=None, allow_none=True, help="Label for next page.").tag(
        sync=True
    )

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when no items are provided to the component.",
    ).tag(sync=True)

    page = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The current displayed page number (1-indexed).",
    ).tag(sync=True)

    page_by = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how pagination counts items.\n- **item** paginates by individual items,\n- **auto** paginates by top-level groups and falls back to regular items if **group-by** is empty,\n- **any** paginates by both items and groups combined",
    ).tag(sync=True)

    page_text = Unicode(default_value=None, allow_none=True, help="Label for page number.").tag(
        sync=True
    )

    prev_icon = Any(help="Previous icon.").tag(sync=True)

    prev_page_label = Unicode(
        default_value=None, allow_none=True, help="Label for previous page."
    ).tag(sync=True)

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    row_props = Dict(
        default_value=None,
        allow_none=True,
        help="An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.",
    ).tag(sync=True)

    search = Unicode(
        default_value=None, allow_none=True, help="Text input used to filter items."
    ).tag(sync=True)

    select_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).",
    ).tag(sync=True)

    show_current_page = Bool(
        default_value=None,
        allow_none=True,
        help="Show current page number between prev/next icons.",
    ).tag(sync=True)

    show_expand = Bool(default_value=None, allow_none=True, help="Shows the expand icon.").tag(
        sync=True
    )

    show_select = Bool(
        default_value=None,
        allow_none=True,
        help="Shows the column with checkboxes for selecting items in the list.",
    ).tag(sync=True)

    sort_asc_icon = Any(help="Icon used for ascending sort button.").tag(sync=True)

    sort_by = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of column keys and sort orders that determines the sort order of the table.",
    ).tag(sync=True)

    sort_desc_icon = Any(help="Icon used for descending sort button.").tag(sync=True)

    sort_icon = Any(
        help="Icon used for unsorted columns. By default it uses either **sortAscIcon** or **sortDescIcon** depending on **initialSortOrder**, but can be customized to show a neutral icon instead."
    ).tag(sync=True)

    sticky = Bool(
        default_value=None, allow_none=True, help="Deprecated, use `fixed-header` instead."
    ).tag(sync=True)

    striped = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a background to either **even** or **odd** rows.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class DataTableVirtual(VuetifyWidget):
    """Widget for the Vuetify v-data-table-virtual component, see https://vuetifyjs.com/en/api/v-data-table-virtual/"""

    _model_name = Unicode("DataTableVirtualModel").tag(sync=True)

    cell_props = Dict(
        default_value=None,
        allow_none=True,
        help="An object of additional props to be passed to each `<td>` in the table body. Also accepts a function that will be called for each cell. If the same prop is defined both here and in `cellProps` in a headers object, the value from the headers object will be used.",
    ).tag(sync=True)

    collapse_icon = Any().tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a color to checkboxes, page size dropdown and sort badges in the table header.",
    ).tag(sync=True)

    custom_filter = Any(
        help="Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted."
    ).tag(sync=True)

    custom_key_filter = Any(
        help="Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified."
    ).tag(sync=True)

    custom_key_sort = Any(
        help="Function used on specific keys within the item object. `customSort` is skipped for columns with `customKeySort` specified."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disable_sort = Bool(
        default_value=None, allow_none=True, help="Toggles rendering of sort button."
    ).tag(sync=True)

    expand_icon = Any().tag(sync=True)

    expand_on_click = Bool(
        default_value=None, allow_none=True, help="Expands item when the row is clicked."
    ).tag(sync=True)

    expanded = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of expanded items. Can be bound to external variable using **v-model:expanded**.",
    ).tag(sync=True)

    filter_keys = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Array of specific keys to filter on the item.",
    ).tag(sync=True)

    filter_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.\n\n- **some**: There is at least one match from either the custom filter or the custom key filter.\n- **every**: All columns match either the custom filter or the custom key filter.\n- **union**: There is at least one match from the custom filter, or all columns match the custom key filters.\n- **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.",
    ).tag(sync=True)

    fixed_footer = Bool(
        default_value=None,
        allow_none=True,
        help="Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.",
    ).tag(sync=True)

    fixed_header = Bool(
        default_value=None, allow_none=True, help="Sticks the header to the top of the table."
    ).tag(sync=True)

    group_by = TList(
        Any(), default_value=None, allow_none=True, help="Defines the grouping of the table items."
    ).tag(sync=True)

    group_collapse_icon = Any().tag(sync=True)

    group_expand_icon = Any().tag(sync=True)

    header_props = Any(help="Pass props to the default header.").tag(sync=True)

    headers = Unicode(
        default_value=None,
        allow_none=True,
        help="An array of objects that each describe a header column.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Use the height prop to set the height of the table.",
    ).tag(sync=True)

    hide_default_body = Bool(
        default_value=None, allow_none=True, help="Hides the default body."
    ).tag(sync=True)

    hide_default_header = Bool(
        default_value=None, allow_none=True, help="Hides the default header."
    ).tag(sync=True)

    hide_no_data = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.",
    ).tag(sync=True)

    hover = Bool(
        default_value=None,
        allow_none=True,
        help="Will add a hover effect to a table's row when the mouse is over it.",
    ).tag(sync=True)

    initial_sort_order = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies the initial sort order when an unsorted column is clicked.",
    ).tag(sync=True)

    item_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Height in pixels of each item to display.",
    ).tag(sync=True)

    item_key = Unicode(
        default_value=None,
        allow_none=True,
        help="The property on each item that is used as a unique key.",
    ).tag(sync=True)

    item_selectable = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that indicates whether the item is selectable.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    loading_text = Unicode(
        default_value=None, allow_none=True, help="Text shown when the data is loading."
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multi_sort = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Let user sort by multiple properties/columns.\n\n- **key**: (optional) when set to `ctrl`, user is required to hold a keyboard key (Ctrl on PC and Command on Mac)\n- **mode**: when user selects a new column to sort by, it will be set first (`prepend`) or last (`append`) in the sort priority. Defaults to `append`\n- **modifier**: (optional) allows user to use both multi-sort modes (`append` and `prepend`) simultaneously\n\n**Note**: object notation requires at least **v3.11.0**",
    ).tag(sync=True)

    must_sort = Bool(
        default_value=None, allow_none=True, help="Forces sorting on the column(s)."
    ).tag(sync=True)

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when no items are provided to the component.",
    ).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True, help="Disables all item filtering.").tag(
        sync=True
    )

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    row_props = Dict(
        default_value=None,
        allow_none=True,
        help="An object of additional props to be passed to each `<tr>` in the table body. Also accepts a function that will be called for each row.",
    ).tag(sync=True)

    search = Unicode(
        default_value=None, allow_none=True, help="Text input used to filter items."
    ).tag(sync=True)

    select_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Defines the strategy of selecting items in the list. Possible values are: 'single' (only one item can be selected at a time), 'page' ('Select all' button will select only items on the current page), 'all' ('Select all' button will select all items in the list).",
    ).tag(sync=True)

    show_expand = Bool(default_value=None, allow_none=True, help="Shows the expand icon.").tag(
        sync=True
    )

    show_select = Bool(
        default_value=None,
        allow_none=True,
        help="Shows the column with checkboxes for selecting items in the list.",
    ).tag(sync=True)

    sort_asc_icon = Any(help="Icon used for ascending sort button.").tag(sync=True)

    sort_by = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of column keys and sort orders that determines the sort order of the table.",
    ).tag(sync=True)

    sort_desc_icon = Any(help="Icon used for descending sort button.").tag(sync=True)

    sort_icon = Any(
        help="Icon used for unsorted columns. By default it uses either **sortAscIcon** or **sortDescIcon** depending on **initialSortOrder**, but can be customized to show a neutral icon instead."
    ).tag(sync=True)

    sticky = Bool(
        default_value=None, allow_none=True, help="Deprecated, use `fixed-header` instead."
    ).tag(sync=True)

    striped = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a background to either **even** or **odd** rows.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class DateInput(VuetifyWidget):
    """Widget for the Vuetify v-date-input component, see https://vuetifyjs.com/en/api/v-date-input/"""

    _model_name = Unicode("DateInputModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    allowed_dates = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which dates can be selected."
    ).tag(sync=True)

    allowed_months = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which months can be selected."
    ).tag(sync=True)

    allowed_years = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which years can be selected."
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True, help="Enables autofocus.").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    cancel_text = Unicode(
        default_value=None, allow_none=True, help="Text for the cancel button"
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    control_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height of the controls.",
    ).tag(sync=True)

    control_variant = Unicode(
        default_value=None,
        allow_none=True,
        help="- **docked:** Separate control groups for month and year.\n- **modal:** Month and year are displayed together, clicking the text opens a month picker, clicking the dropdown arrow opens a year picker. There are also arrow buttons to scroll between months.",
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Float(
        default_value=None, allow_none=True, help="Function returns the counter display text."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    dirty = Bool(
        default_value=None, allow_none=True, help="Manually apply the dirty state styling."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    display_format = Unicode(
        default_value=None,
        allow_none=True,
        help="The format of the date that is displayed in the input. Can use any format [here](https://vuetifyjs.com/en/features/dates/#format-options) or a custom function.",
    ).tag(sync=True)

    divided = Bool(
        default_value=None, allow_none=True, help="Adds a divider between the header and controls."
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    event_color = Union(
        [Union([Unicode(), Bool(), TList(Any())]), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the color for event dots. It can be string (all events will have the same color) or `object` where attribute is the event date and value is boolean/color/array of colors for specified date or `function` taking date as a parameter and returning boolean/color/array of colors for that date.",
    ).tag(sync=True)

    events = Union(
        [TList(Any()), Dict()],
        default_value=None,
        allow_none=True,
        help="Array of dates or object defining events or colors or function returning boolean/color/array of colors.",
    ).tag(sync=True)

    first_day_of_week = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the first day of the week, starting with 0 for Sunday. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    first_day_of_year = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the day that determines the first week of the year, starting with 0 for Sunday. For ISO 8601 this should be 4. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    header = Unicode(
        default_value=None, allow_none=True, help="Text shown when no **display-date** is set."
    ).tag(sync=True)

    header_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Allows you to set a different color for the header when used in conjunction with the `color` prop.",
    ).tag(sync=True)

    header_date_format = Unicode(
        default_value=None,
        allow_none=True,
        help="Allows you to customize the format of the date selection text that appears in the header of the calendar.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None,
        allow_none=True,
        help="Hide the Cancel and OK buttons, and automatically update the value when a date is selected.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_header = Bool(default_value=None, allow_none=True, help="Hide the picker header.").tag(
        sync=True
    )

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hide_title = Bool(default_value=None, allow_none=True, help="Hide the picker title.").tag(
        sync=True
    )

    hide_weekdays = Bool(default_value=None, allow_none=True, help="Hides the weekdays.").tag(
        sync=True
    )

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-date-input/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    input_format = Unicode(
        default_value=None,
        allow_none=True,
        help="Format for manual date input. Use yyyy, mm, dd with separators '.', '-', '/' (e.g. 'yyyy-mm-dd', 'dd/mm/yyyy').",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    landscape = Bool(
        default_value=None, allow_none=True, help="Puts the picker into landscape mode."
    ).tag(sync=True)

    landscape_header_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets header width when in landscape mode.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the date picker's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max = Any(help="Maximum allowed date/month (ISO 8601 format).").tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    menu = Bool(
        default_value=None, allow_none=True, help="Renders with the menu open by default."
    ).tag(sync=True)

    menu_props = Any().tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min = Any(help="Minimum allowed date/month (ISO 8601 format).").tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    mode_icon = Any(
        help="Icon displayed next to the current month and year, toggles year selection when clicked."
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Any(help="Represents the committed v-model value").tag(sync=True)

    month = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Sets the month."
    ).tag(sync=True)

    multiple = Union(
        [Bool(), Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Allow the selection of multiple dates. The **range** value selects all dates between two selections.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    next_icon = Any(help="Sets the icon for next month/year button.").tag(sync=True)

    no_month_picker = Bool(
        default_value=None,
        allow_none=True,
        help='Only applies to `controlVariant="modal"`, the month and year picker buttons are combined into one that only opens the year picker.',
    ).tag(sync=True)

    ok_text = Unicode(default_value=None, allow_none=True, help="Text for the ok button").tag(
        sync=True
    )

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-date-input/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    picker_props = Any(
        help="Pass props through to the picker component. Intended for props that conflict with `v-text-field` (`color`, `width`, `rounded`, etc.)"
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    prev_icon = Any(help="Sets the icon for previous month/year button.").tag(sync=True)

    readonly = Bool(
        default_value=None,
        allow_none=True,
        help="Makes the picker readonly (doesn't allow to select new date).",
    ).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    reverse_transition = Unicode(
        default_value=None,
        allow_none=True,
        help="The transition used when changing months into the past",
    ).tag(sync=True)

    role = Unicode(
        default_value=None, allow_none=True, help="The role attribute applied to the input."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a border radius to the input.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    show_adjacent_months = Bool(
        default_value=None,
        allow_none=True,
        help="Toggles visibility of days from previous and next months.",
    ).tag(sync=True)

    show_week = Bool(
        default_value=None,
        allow_none=True,
        help="Toggles visibility of the week numbers in the body of the calendar.",
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    transition = Unicode(
        default_value=None,
        allow_none=True,
        help="The transition used when changing months into the future",
    ).tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Determines the type of the picker - `date` for date picker, `month` for month picker.",
    ).tag(sync=True)

    update_on = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Specifies when the text input should update the model value. If empty, the text field will go into read-only state.",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    view_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Determines which picker in the date or month picker is being displayed. Allowed values: `'month'`, `'months'`, `'year'`.",
    ).tag(sync=True)

    weekday_format = Unicode(
        default_value=None,
        allow_none=True,
        help="Allows you to customize the format of the weekday string that appears in the body of the calendar. Uses `'narrow'` by default. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    weekdays = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of weekdays to display. Does not affect the order.",
    ).tag(sync=True)

    weeks_in_month = Unicode(
        default_value=None,
        allow_none=True,
        help="A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Width of the picker."
    ).tag(sync=True)

    year = Float(default_value=None, allow_none=True, help="Sets the year.").tag(sync=True)


class DatePicker(VuetifyWidget):
    """Widget for the Vuetify v-date-picker component, see https://vuetifyjs.com/en/api/v-date-picker/"""

    _model_name = Unicode("DatePickerModel").tag(sync=True)

    allowed_dates = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which dates can be selected."
    ).tag(sync=True)

    allowed_months = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which months can be selected."
    ).tag(sync=True)

    allowed_years = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which years can be selected."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    control_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height of the controls.",
    ).tag(sync=True)

    control_variant = Unicode(
        default_value=None,
        allow_none=True,
        help="- **docked:** Separate control groups for month and year.\n- **modal:** Month and year are displayed together, clicking the text opens a month picker, clicking the dropdown arrow opens a year picker. There are also arrow buttons to scroll between months.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    divided = Bool(
        default_value=None, allow_none=True, help="Adds a divider between the header and controls."
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    event_color = Union(
        [Union([Unicode(), Bool(), TList(Any())]), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the color for event dots. It can be string (all events will have the same color) or `object` where attribute is the event date and value is boolean/color/array of colors for specified date or `function` taking date as a parameter and returning boolean/color/array of colors for that date.",
    ).tag(sync=True)

    events = Union(
        [TList(Any()), Dict()],
        default_value=None,
        allow_none=True,
        help="Array of dates or object defining events or colors or function returning boolean/color/array of colors.",
    ).tag(sync=True)

    first_day_of_week = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the first day of the week, starting with 0 for Sunday. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    first_day_of_year = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the day that determines the first week of the year, starting with 0 for Sunday. For ISO 8601 this should be 4. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    header = Unicode(
        default_value=None, allow_none=True, help="Text shown when no **display-date** is set."
    ).tag(sync=True)

    header_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Allows you to set a different color for the header when used in conjunction with the `color` prop.",
    ).tag(sync=True)

    header_date_format = Unicode(
        default_value=None,
        allow_none=True,
        help="Allows you to customize the format of the date selection text that appears in the header of the calendar.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_header = Bool(default_value=None, allow_none=True, help="Hides the header.").tag(sync=True)

    hide_title = Bool(default_value=None, allow_none=True, help="Hide the picker title.").tag(
        sync=True
    )

    hide_weekdays = Bool(default_value=None, allow_none=True, help="Hides the weekdays.").tag(
        sync=True
    )

    landscape = Bool(
        default_value=None, allow_none=True, help="Changes the picker to landscape mode."
    ).tag(sync=True)

    landscape_header_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets header width when in landscape mode.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max = Any(help="Maximum allowed date/month (ISO 8601 format).").tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min = Any(help="Minimum allowed date/month (ISO 8601 format).").tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    mode_icon = Any(
        help="Icon displayed next to the current month and year, toggles year selection when clicked."
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    month = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Sets the month."
    ).tag(sync=True)

    multiple = Union(
        [Bool(), Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Allow the selection of multiple dates. The **range** value selects all dates between two selections.",
    ).tag(sync=True)

    next_icon = Any(help="Sets the icon for next month/year button.").tag(sync=True)

    no_month_picker = Bool(
        default_value=None,
        allow_none=True,
        help='Only applies to `controlVariant="modal"`, the month and year picker buttons are combined into one that only opens the year picker.',
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prev_icon = Any(help="Sets the icon for previous month/year button.").tag(sync=True)

    readonly = Bool(
        default_value=None,
        allow_none=True,
        help="Makes the picker readonly (doesn't allow to select new date).",
    ).tag(sync=True)

    reverse_transition = Unicode(
        default_value=None,
        allow_none=True,
        help="The transition used when changing months into the past",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    show_adjacent_months = Bool(
        default_value=None,
        allow_none=True,
        help="Toggles visibility of days from previous and next months.",
    ).tag(sync=True)

    show_week = Bool(
        default_value=None,
        allow_none=True,
        help="Toggles visibility of the week numbers in the body of the calendar.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    transition = Unicode(
        default_value=None,
        allow_none=True,
        help="The transition used when changing months into the future",
    ).tag(sync=True)

    view_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Determines which picker in the date or month picker is being displayed. Allowed values: `'month'`, `'months'`, `'year'`.",
    ).tag(sync=True)

    weekday_format = Unicode(
        default_value=None,
        allow_none=True,
        help="Allows you to customize the format of the weekday string that appears in the body of the calendar. Uses `'narrow'` by default. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    weekdays = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of weekdays to display. Does not affect the order.",
    ).tag(sync=True)

    weeks_in_month = Unicode(
        default_value=None,
        allow_none=True,
        help="A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Width of the picker."
    ).tag(sync=True)

    year = Float(default_value=None, allow_none=True, help="Sets the year.").tag(sync=True)


class DatePickerControls(VuetifyWidget):
    """Widget for the Vuetify v-date-picker-controls component, see https://vuetifyjs.com/en/api/v-date-picker-controls/"""

    _model_name = Unicode("DatePickerControlsModel").tag(sync=True)

    active = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    control_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height of the controls.",
    ).tag(sync=True)

    control_variant = Unicode(
        default_value=None,
        allow_none=True,
        help="- **docked:** Separate control groups for month and year.\n- **modal:** Month and year are displayed together, clicking the text opens a month picker, clicking the dropdown arrow opens a year picker. There are also arrow buttons to scroll between months.",
    ).tag(sync=True)

    disabled = Union(
        [Unicode(), Bool(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    mode_icon = Any(help="Icon used for the mode button.").tag(sync=True)

    month_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Any(help="Icon used for the next button.").tag(sync=True)

    no_month_picker = Bool(
        default_value=None,
        allow_none=True,
        help='Only applies to `controlVariant="modal"`, the month and year picker buttons are combined into one that only opens the year picker.',
    ).tag(sync=True)

    prev_icon = Any(help="Icon used for the previous button.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    view_mode = Unicode(
        default_value=None, allow_none=True, help="Sets the view mode of the date picker."
    ).tag(sync=True)

    year_text = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DatePickerHeader(VuetifyWidget):
    """Widget for the Vuetify v-date-picker-header component, see https://vuetifyjs.com/en/api/v-date-picker-header/"""

    _model_name = Unicode("DatePickerHeaderModel").tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    header = Unicode(default_value=None, allow_none=True, help="Sets the header content.").tag(
        sync=True
    )

    transition = Unicode(
        default_value=None, allow_none=True, help="Sets the transition when the header changes."
    ).tag(sync=True)


class DatePickerMonth(VuetifyWidget):
    """Widget for the Vuetify v-date-picker-month component, see https://vuetifyjs.com/en/api/v-date-picker-month/"""

    _model_name = Unicode("DatePickerMonthModel").tag(sync=True)

    allowed_dates = TList(
        Any(), default_value=None, allow_none=True, help="Sets the allowed dates of the month."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    event_color = Union(
        [Union([Unicode(), Bool(), TList(Any())]), Dict()], default_value=None, allow_none=True
    ).tag(sync=True)

    events = Union([TList(Any()), Dict()], default_value=None, allow_none=True).tag(sync=True)

    first_day_of_week = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the first day of the week, starting with 0 for Sunday. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    first_day_of_year = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the day that determines the first week of the year, starting with 0 for Sunday. For ISO 8601 this should be 4. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    hide_weekdays = Bool(
        default_value=None, allow_none=True, help="Hide the days of the week letters."
    ).tag(sync=True)

    max = Any(help="Sets the maximum date of the month.").tag(sync=True)

    min = Any(help="Sets the minimum date of the month.").tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    month = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Sets the month."
    ).tag(sync=True)

    multiple = Union(
        [Bool(), Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Sets the multiple of the month.",
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse_transition = Unicode(
        default_value=None,
        allow_none=True,
        help="The transition used when changing months into the past",
    ).tag(sync=True)

    show_adjacent_months = Bool(
        default_value=None, allow_none=True, help="Show adjacent months."
    ).tag(sync=True)

    show_week = Bool(default_value=None, allow_none=True, help="Show the week number.").tag(
        sync=True
    )

    transition = Unicode(
        default_value=None,
        allow_none=True,
        help="The transition used when changing months into the future",
    ).tag(sync=True)

    weekday_format = Unicode(
        default_value=None,
        allow_none=True,
        help="Allows you to customize the format of the weekday string that appears in the body of the calendar. Uses `'narrow'` by default. (Note: not guaranteed to work when using custom date adapters.)",
    ).tag(sync=True)

    weekdays = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of weekdays to display. Does not affect the order.",
    ).tag(sync=True)

    weeks_in_month = Unicode(
        default_value=None,
        allow_none=True,
        help="A dynamic number of weeks in a month will grow and shrink depending on how many days are in the month. A static number always shows 7 weeks.",
    ).tag(sync=True)

    year = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Sets the year."
    ).tag(sync=True)


class DatePickerMonths(VuetifyWidget):
    """Widget for the Vuetify v-date-picker-months component, see https://vuetifyjs.com/en/api/v-date-picker-months/"""

    _model_name = Unicode("DatePickerMonthsModel").tag(sync=True)

    allowed_months = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which months can be selected."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    max = Any(
        help="Sets the maximum selectable date. Months after this date will be disabled."
    ).tag(sync=True)

    min = Any(
        help="Sets the minimum selectable date. Months before this date will be disabled."
    ).tag(sync=True)

    model_value = Float(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    year = Float(
        default_value=None, allow_none=True, help="Sets the year for the given months."
    ).tag(sync=True)


class DatePickerYears(VuetifyWidget):
    """Widget for the Vuetify v-date-picker-years component, see https://vuetifyjs.com/en/api/v-date-picker-years/"""

    _model_name = Unicode("DatePickerYearsModel").tag(sync=True)

    allowed_years = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which years can be selected."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    max = Any(help="Sets the maximum date of the month.").tag(sync=True)

    min = Any(help="Sets the minimum date of the month.").tag(sync=True)

    model_value = Float(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)


class DefaultsProvider(VuetifyWidget):
    """Widget for the Vuetify v-defaults-provider component, see https://vuetifyjs.com/en/api/v-defaults-provider/"""

    _model_name = Unicode("DefaultsProviderModel").tag(sync=True)

    defaults = Dict(
        default_value=None,
        allow_none=True,
        help="Specify new default prop values for components. Keep in mind that this will be merged with previously defined values.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Turns off all calculations of new default values for improved performance in situations where defaults propagation isn't necessary.",
    ).tag(sync=True)

    reset = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Reset the default values up the nested chain by {n} amount.",
    ).tag(sync=True)

    root = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Force current defaults to match the application root defaults.",
    ).tag(sync=True)

    scoped = Bool(
        default_value=None,
        allow_none=True,
        help="Prevents the ability for default values to be inherited from parent components.",
    ).tag(sync=True)


class Dialog(VuetifyWidget):
    """Widget for the Vuetify v-dialog component, see https://vuetifyjs.com/en/api/v-dialog/"""

    _model_name = Unicode("DialogModel").tag(sync=True)

    absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **position: absolute** to the content element.",
    ).tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.",
    ).tag(sync=True)

    capture_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None, allow_none=True, help="Closes component when you click on its content."
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    fullscreen = Bool(
        default_value=None, allow_none=True, help="Changes layout for fullscreen display."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    no_click_animation = Bool(
        default_value=None,
        allow_none=True,
        help="Disables the bounce effect when clicking outside of a `v-dialog`'s content when using the **persistent** prop.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is clicked.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether component should activate when its activator is hovered.",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    persistent = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking outside of the element or pressing **esc** key will not deactivate it.",
    ).tag(sync=True)

    retain_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    scroll_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Strategy used when the component is activate and user scrolls.",
    ).tag(sync=True)

    scrollable = Bool(
        default_value=None,
        allow_none=True,
        help="When set to true, expects a `v-card` and a `v-card-text` component with a designated height. For more information, check out the [scrollable example](https://vuetifyjs.com/en/components/dialogs#scrollable).",
    ).tag(sync=True)

    stick_to_target = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the overlay content to go off-screen when scrolling.",
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    viewport_margin = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom viewport margin for the overlay content",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class DialogBottomTransition(VuetifyWidget):
    """Widget for the Vuetify v-dialog-bottom-transition component, see https://vuetifyjs.com/en/api/v-dialog-bottom-transition/"""

    _model_name = Unicode("DialogBottomTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class DialogTopTransition(VuetifyWidget):
    """Widget for the Vuetify v-dialog-top-transition component, see https://vuetifyjs.com/en/api/v-dialog-top-transition/"""

    _model_name = Unicode("DialogTopTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class DialogTransition(VuetifyWidget):
    """Widget for the Vuetify v-dialog-transition component, see https://vuetifyjs.com/en/api/v-dialog-transition/"""

    _model_name = Unicode("DialogTransitionModel").tag(sync=True)

    target = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Sets the target element for the transition.",
    ).tag(sync=True)


class Divider(VuetifyWidget):
    """Widget for the Vuetify v-divider component, see https://vuetifyjs.com/en/api/v-divider/"""

    _model_name = Unicode("DividerModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    content_offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases content spacing from the lines. When passed as an array, the second value shifts slot content down (or right in vertical mode).",
    ).tag(sync=True)

    gradient = Bool(
        default_value=None, allow_none=True, help="Adds fading effect for both sides."
    ).tag(sync=True)

    inset = Bool(
        default_value=None,
        allow_none=True,
        help="Adds indentation (72px) for **normal** dividers, reduces max height for **vertical**.",
    ).tag(sync=True)

    length = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the dividers length. Default unit is px.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the component's opacity value",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    thickness = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the dividers thickness. Default unit is px.",
    ).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True, help="Applies `border-style`.").tag(
        sync=True
    )

    vertical = Bool(default_value=None, allow_none=True, help="Displays dividers vertically.").tag(
        sync=True
    )


class EmptyState(VuetifyWidget):
    """Widget for the Vuetify v-empty-state component, see https://vuetifyjs.com/en/api/v-empty-state/"""

    _model_name = Unicode("EmptyStateModel").tag(sync=True)

    action_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the action button."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    headline = Unicode(
        default_value=None, allow_none=True, help="A large headline often used for 404 pages."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    href = Unicode(
        default_value=None, allow_none=True, help="The URL the action button links to."
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    image = Unicode(
        default_value=None,
        allow_none=True,
        help="Apply a specific image using [v-img](https://vuetifyjs.com/en/components/images/).",
    ).tag(sync=True)

    justify = Unicode(
        default_value=None, allow_none=True, help="Control the justification of the text."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The size used to control the dimensions of the media element inside the component. Can be specified as a number or a string (e.g., '50%', '100px').",
    ).tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    text_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width of the text container.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    to = Unicode(
        default_value=None, allow_none=True, help="The URL the action button links to."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class ExpandBothTransition(VuetifyWidget):
    """Widget for the Vuetify v-expand-both-transition component, see https://vuetifyjs.com/en/api/v-expand-both-transition/"""

    _model_name = Unicode("ExpandBothTransitionModel").tag(sync=True)


class ExpandTransition(VuetifyWidget):
    """Widget for the Vuetify v-expand-transition component, see https://vuetifyjs.com/en/api/v-expand-transition/"""

    _model_name = Unicode("ExpandTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)


class ExpandXTransition(VuetifyWidget):
    """Widget for the Vuetify v-expand-x-transition component, see https://vuetifyjs.com/en/api/v-expand-x-transition/"""

    _model_name = Unicode("ExpandXTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)


class ExpansionPanel(VuetifyWidget):
    """Widget for the Vuetify v-expansion-panel component, see https://vuetifyjs.com/en/api/v-expansion-panel/"""

    _model_name = Unicode("ExpansionPanelModel").tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    collapse_icon = Any(help="Icon used when the expansion panel is in a collapsable state.").tag(
        sync=True
    )

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None, allow_none=True, help="Disables the expansion-panel content."
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    expand_icon = Any(help="Icon used when the expansion panel is in a expandable state.").tag(
        sync=True
    )

    focusable = Bool(
        default_value=None, allow_none=True, help="Makes the expansion panel content focusable."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None, allow_none=True, help="Hide the expand icon in the content title."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    readonly = Bool(
        default_value=None, allow_none=True, help="Makes the expansion panel content read only."
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    static = Bool(
        default_value=None, allow_none=True, help="Remove title size expansion when selected."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    value = Any(help="Controls the opened/closed state of content.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class ExpansionPanelText(VuetifyWidget):
    """Widget for the Vuetify v-expansion-panel-text component, see https://vuetifyjs.com/en/api/v-expansion-panel-text/"""

    _model_name = Unicode("ExpansionPanelTextModel").tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)


class ExpansionPanelTitle(VuetifyWidget):
    """Widget for the Vuetify v-expansion-panel-title component, see https://vuetifyjs.com/en/api/v-expansion-panel-title/"""

    _model_name = Unicode("ExpansionPanelTitleModel").tag(sync=True)

    collapse_icon = Any(help="Icon used when the expansion panel is in a collapsable state.").tag(
        sync=True
    )

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    expand_icon = Any(help="Icon used when the expansion panel is in a expandable state.").tag(
        sync=True
    )

    focusable = Bool(
        default_value=None, allow_none=True, help="Makes the expansion panel headers focusable."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None, allow_none=True, help="Hide the expand icon in the content title."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    readonly = Bool(
        default_value=None, allow_none=True, help="Makes the expansion panel content read only."
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    static = Bool(
        default_value=None, allow_none=True, help="Remove title size expansion when selected."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class ExpansionPanels(VuetifyWidget):
    """Widget for the Vuetify v-expansion-panels component, see https://vuetifyjs.com/en/api/v-expansion-panels/"""

    _model_name = Unicode("ExpansionPanelsModel").tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    collapse_icon = Any(help="Icon used when the expansion panel is in a collapsable state.").tag(
        sync=True
    )

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    expand_icon = Any(help="Icon used when the expansion panel is in a expandable state.").tag(
        sync=True
    )

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the expansion-panel's elevation and borders.",
    ).tag(sync=True)

    focusable = Bool(
        default_value=None, allow_none=True, help="Makes the expansion-panel headers focusable."
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None, allow_none=True, help="Hide the expand icon in the content title."
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    model_value = Any(
        help="Controls expanded panel(s). Defaults to an empty array when using **multiple** prop. It is recommended to set unique `value` prop for the panels inside, otherwise index is used instead."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    readonly = Bool(
        default_value=None, allow_none=True, help="Makes the entire expansion panel read only."
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    static = Bool(
        default_value=None, allow_none=True, help="Remove title size expansion when selected."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(default_value=None, allow_none=True, help="Removes the border-radius.").tag(
        sync=True
    )

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class Fab(VuetifyWidget):
    """Widget for the Vuetify v-fab component, see https://vuetifyjs.com/en/api/v-fab/"""

    _model_name = Unicode("FabModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies **position: absolute** to the component."
    ).tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    app = Bool(
        default_value=None,
        allow_none=True,
        help="If true, attaches to the closest layout and positions according to the value of **location**.",
    ).tag(sync=True)

    appear = Bool(
        default_value=None, allow_none=True, help="Used to control the animation of the FAB."
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    block = Bool(
        default_value=None, allow_none=True, help="Expands the button to 100% of available space."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    extended = Bool(
        default_value=None,
        allow_none=True,
        help="An alternate style for the FAB that expects text.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the button box shadow. This is different than using the 'flat' variant.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component. The button will become _round_."
    ).tag(sync=True)

    layout = Bool(
        default_value=None,
        allow_none=True,
        help="If true, will effect layout dimensions based on size and position.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    location = Any(
        help="The location of the fab relative to the layout. Only works when using **app**."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Assign a specific name for layout registration."
    ).tag(sync=True)

    offset = Bool(
        default_value=None,
        allow_none=True,
        help="Translates the Fab up or down, depending on if location is set to **top** or **bottom**.",
    ).tag(sync=True)

    order = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Adjust the order of the component in relation to its registration order.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    readonly = Bool(
        default_value=None,
        allow_none=True,
        help="Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.",
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    slim = Bool(default_value=None, allow_none=True, help="Reduces padding to 0 8px.").tag(
        sync=True
    )

    stacked = Bool(
        default_value=None, allow_none=True, help="Displays the button as a flex-column."
    ).tag(sync=True)

    symbol = Any(
        help="The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/)."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify content text for the component.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class FabTransition(VuetifyWidget):
    """Widget for the Vuetify v-fab-transition component, see https://vuetifyjs.com/en/api/v-fab-transition/"""

    _model_name = Unicode("FabTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class FadeTransition(VuetifyWidget):
    """Widget for the Vuetify v-fade-transition component, see https://vuetifyjs.com/en/api/v-fade-transition/"""

    _model_name = Unicode("FadeTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class Field(VuetifyWidget):
    """Widget for the Vuetify v-field component, see https://vuetifyjs.com/en/api/v-field/"""

    _model_name = Unicode("FieldModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    details = Bool(
        default_value=None,
        allow_none=True,
        help="Controls whether the field generates an `aria-describedby` attribute for accessibility.",
    ).tag(sync=True)

    dirty = Bool(
        default_value=None, allow_none=True, help="Manually apply the dirty state styling."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    label_id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class FieldLabel(VuetifyWidget):
    """Widget for the Vuetify v-field-label component, see https://vuetifyjs.com/en/api/v-field-label/"""

    _model_name = Unicode("FieldLabelModel").tag(sync=True)

    floating = Bool(
        default_value=None, allow_none=True, help="Elevates the label above the slotted content."
    ).tag(sync=True)


class FileInput(VuetifyWidget):
    """Widget for the Vuetify v-file-input component, see https://vuetifyjs.com/en/api/v-file-input/"""

    _model_name = Unicode("FileInputModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    chips = Bool(
        default_value=None, allow_none=True, help="Changes display of selections to chips."
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    counter = Bool(
        default_value=None, allow_none=True, help="Displays the number of selected files."
    ).tag(sync=True)

    counter_size_string = Unicode(
        default_value=None,
        allow_none=True,
        help="The text displayed when using the **counter** and **show-size** props. Can also be customized globally on the [internationalization page](https://vuetifyjs.com/en/customization/internationalization).",
    ).tag(sync=True)

    counter_string = Unicode(
        default_value=None,
        allow_none=True,
        help="The text displayed when using the **counter** prop. Can also be customized globally on the [internationalization page](https://vuetifyjs.com/en/customization/internationalization).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    dirty = Bool(
        default_value=None, allow_none=True, help="Manually apply the dirty state styling."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    filter_by_type = Unicode(
        default_value=None,
        allow_none=True,
        help="Make the input accept only files matched by one or more [unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#Unique_file_type_specifiers). Applies to drag & drop and selecting folders. Emits `rejected` event when some files do not pass through to make it possible to notify user and deliver better user experience.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_input = Bool(
        default_value=None,
        allow_none=True,
        help="Display the icon only without the input (file names).",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-file-input/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    multiple = Bool(
        default_value=None,
        allow_none=True,
        help="Adds the **multiple** attribute to the input, allowing multiple file selections.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-file-input/#props-hint) to always be visible.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    show_size = Union(
        [Bool(), Float(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the displayed size of selected file(s). When using **true** will default to _1000_ displaying (**kB, MB, GB**) while _1024_ will display (**KiB, MiB, GiB**).",
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    truncate_length = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The length of a filename before it is truncated with ellipsis.",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class FileUpload(VuetifyWidget):
    """Widget for the Vuetify v-file-upload component, see https://vuetifyjs.com/en/api/v-file-upload/"""

    _model_name = Unicode("FileUploadModel").tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    browse_text = Unicode(
        default_value=None, allow_none=True, help="Text for the browse button."
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    divider_text = Unicode(default_value=None, allow_none=True, help="Text in the divider.").tag(
        sync=True
    )

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    filter_by_type = Unicode(
        default_value=None,
        allow_none=True,
        help="Make the input accept only files matched by one or more [unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#Unique_file_type_specifiers). Applies to drag & drop and selecting folders. Emits `rejected` event when some files do not pass through to make it possible to notify user and deliver better user experience.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the input is focused and apply color.",
    ).tag(sync=True)

    hide_browse = Bool(default_value=None, allow_none=True, help="Hides the browse button.").tag(
        sync=True
    )

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-file-upload/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    inset_file_list = Bool(
        default_value=None,
        allow_none=True,
        help="Renders the file list inside the dropzone container instead of below it.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows multiple files to be uploaded."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-file-upload/#props-hint) to always be visible.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Determines whether an overlay is used when hovering over the component with files. Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    show_size = Bool(default_value=None, allow_none=True, help="Shows the size of the file.").tag(
        sync=True
    )

    subtitle = Unicode(
        default_value=None, allow_none=True, help="Specify a subtitle text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class FileUploadDropzone(VuetifyWidget):
    """Widget for the Vuetify v-file-upload-dropzone component, see https://vuetifyjs.com/en/api/v-file-upload-dropzone/"""

    _model_name = Unicode("FileUploadDropzoneModel").tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    browse_text = Unicode(
        default_value=None, allow_none=True, help="Text for the browse button."
    ).tag(sync=True)

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    divider_text = Unicode(default_value=None, allow_none=True, help="Text in the divider.").tag(
        sync=True
    )

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    error = Bool(
        default_value=None,
        allow_none=True,
        help="Puts the dropzone in an error state, changing the border color.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_browse = Bool(default_value=None, allow_none=True, help="Hides the browse button.").tag(
        sync=True
    )

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    inset_file_list = Bool(
        default_value=None,
        allow_none=True,
        help="Renders the file list inside the dropzone container instead of below it.",
    ).tag(sync=True)

    length = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the dividers length. Default unit is px.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows multiple files to be uploaded."
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the component's opacity value",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Determines whether an overlay is used when hovering over the component with files. Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    show_size = Bool(default_value=None, allow_none=True, help="Shows the size of the file.").tag(
        sync=True
    )

    subtitle = Unicode(
        default_value=None, allow_none=True, help="Specify a subtitle text for the component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    thickness = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the dividers thickness. Default unit is px.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class FileUploadItem(VuetifyWidget):
    """Widget for the Vuetify v-file-upload-item component, see https://vuetifyjs.com/en/api/v-file-upload-item/"""

    _model_name = Unicode("FileUploadItemModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None, allow_none=True, help="Deprecated, use `color` instead."
    ).tag(sync=True)

    append_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control when in an **active** state or **input-value** is **true** - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors),",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    file = Any(help="The file object uploaded").tag(sync=True)

    file_icon = Unicode(
        default_value=None,
        allow_none=True,
        help="The icon prepending each uploaded file. This will be a preview image if the file is an image.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    index = Float(
        default_value=None, allow_none=True, help="The index of the file in the upload list."
    ).tag(sync=True)

    lines = Union(
        [Bool(), Unicode(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="The line declaration specifies the minimum height of the item and can also be controlled from v-list with the same prop.",
    ).tag(sync=True)

    link = Bool(
        default_value=None,
        allow_none=True,
        help="Designates that the component is a link. This is automatic when using the href or to prop.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    nav = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces the width v-list-item takes up as well as adding a border radius.",
    ).tag(sync=True)

    prepend_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.",
    ).tag(sync=True)

    prepend_gap = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    show_size = Bool(default_value=None, allow_none=True, help="Show the size of the file").tag(
        sync=True
    )

    slim = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces horizontal spacing for badges, icons, tooltips, and avatars to create a more compact visual representation.",
    ).tag(sync=True)

    subtitle = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify a subtitle text for the component.",
    ).tag(sync=True)

    tabindex = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help='Controls the tabindex of the list item. When set, overrides the default tabindex behavior. Automatically set to -1 by VList when using `navigationStrategy="track"` to prevent Tab key navigation into items.',
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Generates a `v-list-item-title` component with the supplied value. Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title) attribute, that must be set with `v-bind:title.attr` instead.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    value = Any(
        help="The value used for selection. Obtained from [`v-list`](https://vuetifyjs.com/en/api/v-list)'s `v-model:selected` when the item is selected."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class FileUploadList(VuetifyWidget):
    """Widget for the Vuetify v-file-upload-list component, see https://vuetifyjs.com/en/api/v-file-upload-list/"""

    _model_name = Unicode("FileUploadListModel").tag(sync=True)

    activatable = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether the list items are activatable. Additionally, sets necessary accessibility attributes internally.",
    ).tag(sync=True)

    activated = Any(help="Array of ids of activated nodes.").tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it is in an active state.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None, allow_none=True, help="Deprecated, use `color` instead."
    ).tag(sync=True)

    active_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Affects how items with children behave when activated. If not specified, the **single-independent** strategy will be used.\n- **leaf:** Only leaf nodes (items without children) can be activated.\n- **single-leaf:** Similar as **leaf**, but only a single item can be activated at a time.\n- **independent:** All nodes can be activated whether they have children or not.\n- **single-independent:** Similar as **independent**, but only a single item can be activated at a time.",
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    collapse_icon = Any(help="Icon to display when the list item is expanded.").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None, allow_none=True, help="Puts all children inputs into a disabled state."
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    expand_icon = Any(help="Icon to display when the list item is collapsed.").tag(sync=True)

    files = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of File objects to display in the list. When used inside a VFileUpload, this is provided automatically via injection.",
    ).tag(sync=True)

    filterable = Bool(
        default_value=None,
        allow_none=True,
        help="**FOR INTERNAL USE ONLY** Prevents list item selection using [space] key and pass it back to the text input. Used internally for VAutocomplete and VCombobox.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    indent = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Overrides the indent size for nested groups.",
    ).tag(sync=True)

    item_children = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its children.",
    ).tag(sync=True)

    item_props = Unicode(
        default_value=None,
        allow_none=True,
        help="Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.",
    ).tag(sync=True)

    item_title = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its title.",
    ).tag(sync=True)

    item_type = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the key on the supplied items that is used for determining the nodes type.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Can be an array of objects or strings. By default objects should have a **title** property, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props), a **value** property to allow selection, and a **children** property containing more item objects. Keys to use for these can be changed with the **item-title**, **item-value**, **item-props**, and **item-children** props.",
    ).tag(sync=True)

    items_registration = Unicode(
        default_value=None,
        allow_none=True,
        help="When set to 'props', skips rendering collapsed items/nodes (for significant performance gains).",
    ).tag(sync=True)

    lines = Union(
        [Bool(), Unicode(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Designates a **minimum-height** for all children `v-list-item` components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp) and is not supported in all browsers.",
    ).tag(sync=True)

    mandatory = Bool(
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    nav = Bool(
        default_value=None,
        allow_none=True,
        help="An alternative styling that reduces `v-list-item` width and rounds the corners. Typically used with **[v-navigation-drawer](https://vuetifyjs.com/en/components/navigation-drawers)**.",
    ).tag(sync=True)

    navigation_index = Float(
        default_value=None,
        allow_none=True,
        help='Specifies the currently selected navigation index when using `navigationStrategy="track"`. Can be used with `v-model:navigationIndex` for two-way binding. Items at this index receive visual keyboard focus styling and automatic scrolling. Note: Only works with the `items` prop, not with slotted items.',
    ).tag(sync=True)

    navigation_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help='Determines keyboard navigation behavior. **focus** (default) moves DOM focus to items, suitable for traditional lists. **track** provides visual keyboard focus without moving DOM focus, ideal for command palettes and autocomplete where an external element retains focus. When track mode is active, items automatically receive `tabindex="-1"`, proper `aria-activedescendant` is set on the list container, and keyboard-focused items display focus-visible styling with auto-scrolling.',
    ).tag(sync=True)

    open_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Affects how items with children behave when expanded.\n- **multiple:** Any number of groups can be open at once.\n- **single:** Only one group at each level can be open, opening a group will cause others to close.\n- **list:** Multiple, but all other groups will close when an item is selected.",
    ).tag(sync=True)

    opened = Any(
        help="An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`."
    ).tag(sync=True)

    prepend_gap = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the horizontal spacing between prepend slot and the main content within list item. Also affects indent to ensure expected alignment of group children.",
    ).tag(sync=True)

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    select_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Affects how items with children behave when selected.\n- **leaf:** Only leaf nodes (items without children) can be selected.\n- **independent:** All nodes can be selected whether they have children or not.\n- **classic:** Selecting a parent node will cause all children to be selected, parent nodes will be displayed as selected if all their descendants are selected. Only leaf nodes will be added to the model.\n- **trunk**: Same as classic but if all of a node's children are selected then only that node will be added to the model.\n- **branch**: Same as classic but if any of a node's children are selected then that node will also be added to the model.",
    ).tag(sync=True)

    selectable = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether the list items are selectable. Additionally, sets necessary accessibility attributes internally.",
    ).tag(sync=True)

    selected = Any(
        help="An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`."
    ).tag(sync=True)

    show_size = Bool(default_value=None, allow_none=True, help="Shows the size of each file.").tag(
        sync=True
    )

    slim = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces horizontal spacing for badges, icons, tooltips, and avatars within slim list items to create a more compact visual representation.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Footer(VuetifyWidget):
    """Widget for the Vuetify v-footer component, see https://vuetifyjs.com/en/api/v-footer/"""

    _model_name = Unicode("FooterModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies **position: absolute** to the component."
    ).tag(sync=True)

    app = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the position of the footer. If true, the footer would be given a fixed position at the bottom of the viewport. If false, the footer is set to the bottom of the page.",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Assign a specific name for layout registration."
    ).tag(sync=True)

    order = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Adjust the order of the component in relation to its registration order.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)


class Form(VuetifyWidget):
    """Widget for the Vuetify v-form component, see https://vuetifyjs.com/en/api/v-form/"""

    _model_name = Unicode("FormModel").tag(sync=True)

    disabled = Bool(
        default_value=None, allow_none=True, help="Puts all children inputs into a disabled state."
    ).tag(sync=True)

    fast_fail = Bool(
        default_value=None, allow_none=True, help="Stop validation as soon as any rules fail."
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The value representing the validity of the form. If the value is `null` then no validation has taken place yet, or the form has been reset. Otherwise the value will be a `boolean` that indicates if validation has passed or not.",
    ).tag(sync=True)

    readonly = Bool(
        default_value=None, allow_none=True, help="Puts all children inputs into a readonly state."
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None, allow_none=True, help="Changes the events in which validation occurs."
    ).tag(sync=True)


class Hotkey(VuetifyWidget):
    """Widget for the Vuetify v-hotkey component, see https://vuetifyjs.com/en/api/v-hotkey/"""

    _model_name = Unicode("HotkeyModel").tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Applies a disabled visual state to the component.",
    ).tag(sync=True)

    display_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how keyboard keys are visually represented. Affects the entire component's appearance:\n- **icon:** Uses SVG icons for keys when appropriate (default)\n- **symbol:** Uses Unicode symbols (⌘, ⌃, ⇧, ⌥) - Allows you to manage presentation of modifier keys with fonts\n- **text:** Uses full text labels (Command, Control, Shift, Alt) - most accessible and descriptive",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    inline = Bool(
        default_value=None,
        allow_none=True,
        help="Optimizes the component for seamless integration within text content and documentation. Applies compact styling with baseline alignment, constrained height (1lh), and responsive typography that inherits from parent text. Ideal for help documentation, tooltips, and instructional content. When using multiple inline hotkeys in the same paragraph, increase line-height to prevent visual overlap on text wrapping.",
    ).tag(sync=True)

    key_map = Any(
        help="Custom key mapping object that defines how individual keys should be displayed. Users can import and modify the exported `hotkeyMap` to create custom configurations. Each key maps to a `PlatformKeyConfig` object with:\n\n```typescript\n{\n  mac?: { symbol?: string, icon?: string, text: string },\n  default: { symbol?: string, icon?: string, text: string }\n}\n```\n\n**Usage Example:**\n```typescript\nimport { hotkeyMap } from 'vuetify/labs/VHotkey'\n\nconst customKeyMap = {\n  ...hotkeyMap,\n  'custom-key': {\n    default: { text: 'Custom', icon: 'custom-icon' },\n    mac: { text: 'Custom', symbol: '⚡' }\n  }\n}\n```\n\nThis enables:\n- **Custom key definitions:** Add support for application-specific keys\n- **Localization:** Override text representations for different languages\n- **Brand customization:** Change how modifier keys appear\n- **Platform-specific styling:** Different representations for Mac vs other platforms\n\nRecommended to set at the application level via component defaults rather than per-instance for consistency."
    ).tag(sync=True)

    keys = Unicode(
        default_value=None,
        allow_none=True,
        help='String representing keyboard shortcuts to display. Supports multiple formats:\n- **Single keys:** `"k"`, `"enter"`, `"escape"`\n- **Key combinations:** `"ctrl+k"`, `"meta+shift+p"`, `"alt+arrowup"`\n- **Sequential actions:** `"ctrl+k-then-p"` (use dash for \'then\' relationships)\n- **Multiple shortcuts:** `"ctrl+k meta+p"` (space-separated for alternative shortcuts)\n\nSupports platform-aware key names like `meta` (becomes Cmd on Mac, Ctrl on PC) and `alt` (becomes Option on Mac).',
    ).tag(sync=True)

    platform = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls platform-specific rendering behavior for keyboard shortcuts. Accepts three values:\n- **`'auto'` (default):** Automatically detects the user's platform based on user agent and renders appropriately\n- **`'mac'`:** Forces Mac-style rendering (Command symbols, icons, Option key, etc.)\n- **`'pc'`:** Forces PC-style rendering (Ctrl text, Alt key, etc.)\n\nThis is particularly useful for:\n- **Cross-platform testing:** Verify how shortcuts appear on different platforms\n- **Design consistency:** Ensure specific platform rendering in demos and prototypes\n- **Development workflow:** Test platform-specific behaviors without switching devices\n- **Documentation:** Show platform-specific examples in help content",
    ).tag(sync=True)

    prefix = Unicode(
        default_value=None, allow_none=True, help="Text to display before the hotkey."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    suffix = Unicode(
        default_value=None, allow_none=True, help="Text to display after the hotkey."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls the visual style and presentation of the hotkey component. Supports standard Vuetify variants plus a special contained variant:\n\n**Standard Variants** (apply styling to individual key elements):\n- **elevated (default):** Raised appearance with shadow, good for standalone hotkey displays\n- **flat:** Solid background without shadow, clean and minimal\n- **tonal:** Subtle tinted background without border, balances visibility with restraint\n- **outlined:** Border-only styling without elevation, lightweight and unobtrusive\n- **text:** Minimal styling with text color emphasis only, blends with content\n- **plain:** No background or border, most subtle option\n\n**Special Variant** (different visual structure):\n- **contained:** Follows MDN's nested `<kbd>` pattern - wraps all keys in a single styled container with unstyled nested elements. Creates a cohesive visual unit that clearly groups related keys together. Cannot be combined with standard variants. Ideal for complex key combinations where you want to show the entire sequence as one unit.",
    ).tag(sync=True)


class Hover(VuetifyWidget):
    """Widget for the Vuetify v-hover component, see https://vuetifyjs.com/en/api/v-hover/"""

    _model_name = Unicode("HoverModel").tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True, help="Removes hover functionality.").tag(
        sync=True
    )

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)


class Icon(VuetifyWidget):
    """Widget for the Vuetify v-icon component, see https://vuetifyjs.com/en/api/v-icon/"""

    _model_name = Unicode("IconModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    end = Bool(
        default_value=None, allow_none=True, help="Applies margin at the start of the component."
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the component's opacity value",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    start = Bool(
        default_value=None, allow_none=True, help="Applies margin at the end of the component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)


class IconBtn(VuetifyWidget):
    """Widget for the Vuetify v-icon-btn component, see https://vuetifyjs.com/en/api/v-icon-btn/"""

    _model_name = Unicode("IconBtnModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="When undefined (default), the component utilizes its default variant, otherwise it will use the activeVariant if active is true, or the baseVariant if active is false.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    active_icon = Any(help="When active is a boolean, this icon is used when active is true.").tag(
        sync=True
    )

    active_variant = Unicode(
        default_value=None,
        allow_none=True,
        help="When active is a boolean, this variant is used when active is true.",
    ).tag(sync=True)

    base_variant = Unicode(
        default_value=None,
        allow_none=True,
        help="When active is a boolean, this variant is used when active is false.",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_overlay = Bool(
        default_value=None,
        allow_none=True,
        help="Hides overlay from being displayed when active or focused.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    icon_color = Unicode(
        default_value=None, allow_none=True, help="Explicit color applied to the icon."
    ).tag(sync=True)

    icon_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The specific size of the icon, can use named sizes.",
    ).tag(sync=True)

    icon_sizes = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of tuples that define the icon sizes for each named size.",
    ).tag(sync=True)

    loading = Bool(
        default_value=None,
        allow_none=True,
        help="Displays circular progress bar in place of the icon.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the component's opacity value",
    ).tag(sync=True)

    readonly = Bool(
        default_value=None,
        allow_none=True,
        help="Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.",
    ).tag(sync=True)

    rotate = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The rotation of the icon in degrees.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component.",
    ).tag(sync=True)

    sizes = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of tuples that define the button sizes for each named size.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify content text for the component.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Img(VuetifyWidget):
    """Widget for the Vuetify v-img component, see https://vuetifyjs.com/en/api/v-img/"""

    _model_name = Unicode("ImgModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies position: absolute to the component."
    ).tag(sync=True)

    alt = Unicode(
        default_value=None,
        allow_none=True,
        help="Alternate text for screen readers. Leave empty for decorative images.",
    ).tag(sync=True)

    aspect_ratio = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Calculated as `width/height`, so for a 1920x1080px image this will be `1.7778`. Will be calculated automatically if omitted.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    content_class = Any(help="Apply a custom class to the internal content element.").tag(sync=True)

    cover = Bool(
        default_value=None,
        allow_none=True,
        help="Resizes the background image to cover the entire container.",
    ).tag(sync=True)

    crossorigin = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify that images should be fetched with CORS enabled [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#crossorigin)",
    ).tag(sync=True)

    draggable = Union(
        [Bool(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Controls the `draggable` behavior of the image. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/draggable).",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    gradient = Unicode(
        default_value=None,
        allow_none=True,
        help="The gradient to apply to the image. Only supports [linear-gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient) syntax, anything else should be done with classes.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    image_class = Any(help="Applies CSS classes to the inner `<img>` element.").tag(sync=True)

    inline = Bool(
        default_value=None,
        allow_none=True,
        help="Display as an inline element instead of a block, also disables flex-grow.",
    ).tag(sync=True)

    lazy_src = Unicode(
        default_value=None,
        allow_none=True,
        help="Something to show while waiting for the main image to load, typically a small base64-encoded thumbnail. Has a slight blur filter applied.  \nNOTE: This prop has no effect unless either `height` or `aspect-ratio` are provided.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    options = Any(
        help="Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) constructor."
    ).tag(sync=True)

    position = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies [object-position](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position) styles to the image and placeholder elements.",
    ).tag(sync=True)

    referrerpolicy = Unicode(
        default_value=None,
        allow_none=True,
        help="Define which referrer is sent when fetching the resource [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#referrerpolicy)",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    sizes = Unicode(
        default_value=None,
        allow_none=True,
        help="For use with `srcset`, see [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes).",
    ).tag(sync=True)

    src = Union(
        [Unicode(), Dict()],
        default_value=None,
        allow_none=True,
        help="The image URL. This prop is mandatory.",
    ).tag(sync=True)

    srcset = Unicode(
        default_value=None,
        allow_none=True,
        help="A set of alternate images to use based on device size. [Read more...](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset).",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="The transition to use when switching from `lazy-src` to `src`. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class InfiniteScroll(VuetifyWidget):
    """Widget for the Vuetify v-infinite-scroll component, see https://vuetifyjs.com/en/api/v-infinite-scroll/"""

    _model_name = Unicode("InfiniteScrollModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    direction = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies if scroller is **vertical** or **horizontal**.",
    ).tag(sync=True)

    empty_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when there is no more content to load.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    load_more_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown in default load more button, when in manual mode.",
    ).tag(sync=True)

    margin = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Value sent to the intersection observer. Will make the observer trigger earlier, by the margin (px) value supplied.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies if content should load automatically when scrolling (**intersect**) or manually (**manual**).",
    ).tag(sync=True)

    side = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies the side where new content should appear. Either the **start**, **end**, or **both** sides.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Input(VuetifyWidget):
    """Widget for the Vuetify v-input component, see https://vuetifyjs.com/en/api/v-input/"""

    _model_name = Unicode("InputModel").tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(
        default_value=None, allow_none=True, help="Changes the direction of the input."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the input is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-input/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-input/#props-hint) to always be visible.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Item(VuetifyWidget):
    """Widget for the Vuetify v-item component, see https://vuetifyjs.com/en/api/v-item/"""

    _model_name = Unicode("ItemModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)


class ItemGroup(VuetifyWidget):
    """Widget for the Vuetify v-item-group component, see https://vuetifyjs.com/en/api/v-item-group/"""

    _model_name = Unicode("ItemGroupModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the selected CSS class. This class will be available in `v-item` default scoped slot.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)


class Kbd(VuetifyWidget):
    """Widget for the Vuetify v-kbd component, see https://vuetifyjs.com/en/api/v-kbd/"""

    _model_name = Unicode("KbdModel").tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)


class Label(VuetifyWidget):
    """Widget for the Vuetify v-label component, see https://vuetifyjs.com/en/api/v-label/"""

    _model_name = Unicode("LabelModel").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)


class Layout(VuetifyWidget):
    """Widget for the Vuetify v-layout component, see https://vuetifyjs.com/en/api/v-layout/"""

    _model_name = Unicode("LayoutModel").tag(sync=True)

    full_height = Bool(
        default_value=None, allow_none=True, help="Sets the component height to 100%."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    overlaps = TList(
        Any(), default_value=None, allow_none=True, help="**FOR INTERNAL USE ONLY**"
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class LayoutItem(VuetifyWidget):
    """Widget for the Vuetify v-layout-item component, see https://vuetifyjs.com/en/api/v-layout-item/"""

    _model_name = Unicode("LayoutItemModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies **position: absolute** to the component."
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Assign a specific name for layout registration."
    ).tag(sync=True)

    order = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Adjust the order of the component in relation to its registration order.",
    ).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True, help="The position of the item.").tag(
        sync=True
    )

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component.",
    ).tag(sync=True)


class Lazy(VuetifyWidget):
    """Widget for the Vuetify v-lazy component, see https://vuetifyjs.com/en/api/v-lazy/"""

    _model_name = Unicode("LazyModel").tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    options = Any(
        help="Options that are passed to the [Intersection observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) constructor."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class LigatureIcon(VuetifyWidget):
    """Widget for the Vuetify v-ligature-icon component, see https://vuetifyjs.com/en/api/v-ligature-icon/"""

    _model_name = Unicode("LigatureIconModel").tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class List(VuetifyWidget):
    """Widget for the Vuetify v-list component, see https://vuetifyjs.com/en/api/v-list/"""

    _model_name = Unicode("ListModel").tag(sync=True)

    activatable = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether the list items are activatable. Additionally, sets necessary accessibility attributes internally.",
    ).tag(sync=True)

    activated = Any(help="Array of ids of activated nodes.").tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it is in an active state.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None, allow_none=True, help="Deprecated, use `color` instead."
    ).tag(sync=True)

    active_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Affects how items with children behave when activated. If not specified, the **single-independent** strategy will be used.\n- **leaf:** Only leaf nodes (items without children) can be activated.\n- **single-leaf:** Similar as **leaf**, but only a single item can be activated at a time.\n- **independent:** All nodes can be activated whether they have children or not.\n- **single-independent:** Similar as **independent**, but only a single item can be activated at a time.",
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    collapse_icon = Any(help="Icon to display when the list item is expanded.").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None, allow_none=True, help="Puts all children inputs into a disabled state."
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    expand_icon = Any(help="Icon to display when the list item is collapsed.").tag(sync=True)

    filterable = Bool(
        default_value=None,
        allow_none=True,
        help="**FOR INTERNAL USE ONLY** Prevents list item selection using [space] key and pass it back to the text input. Used internally for VAutocomplete and VCombobox.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    indent = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Overrides the indent size for nested groups.",
    ).tag(sync=True)

    item_children = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its children.",
    ).tag(sync=True)

    item_props = Unicode(
        default_value=None,
        allow_none=True,
        help="Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.",
    ).tag(sync=True)

    item_title = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its title.",
    ).tag(sync=True)

    item_type = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the key on the supplied items that is used for determining the nodes type.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Can be an array of objects or strings. By default objects should have a **title** property, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props), a **value** property to allow selection, and a **children** property containing more item objects. Keys to use for these can be changed with the **item-title**, **item-value**, **item-props**, and **item-children** props.",
    ).tag(sync=True)

    items_registration = Unicode(
        default_value=None,
        allow_none=True,
        help="When set to 'props', skips rendering collapsed items/nodes (for significant performance gains).",
    ).tag(sync=True)

    lines = Union(
        [Bool(), Unicode(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Designates a **minimum-height** for all children `v-list-item` components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp) and is not supported in all browsers.",
    ).tag(sync=True)

    mandatory = Bool(
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    nav = Bool(
        default_value=None,
        allow_none=True,
        help="An alternative styling that reduces `v-list-item` width and rounds the corners. Typically used with **[v-navigation-drawer](https://vuetifyjs.com/en/components/navigation-drawers)**.",
    ).tag(sync=True)

    navigation_index = Float(
        default_value=None,
        allow_none=True,
        help='Specifies the currently selected navigation index when using `navigationStrategy="track"`. Can be used with `v-model:navigationIndex` for two-way binding. Items at this index receive visual keyboard focus styling and automatic scrolling. Note: Only works with the `items` prop, not with slotted items.',
    ).tag(sync=True)

    navigation_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help='Determines keyboard navigation behavior. **focus** (default) moves DOM focus to items, suitable for traditional lists. **track** provides visual keyboard focus without moving DOM focus, ideal for command palettes and autocomplete where an external element retains focus. When track mode is active, items automatically receive `tabindex="-1"`, proper `aria-activedescendant` is set on the list container, and keyboard-focused items display focus-visible styling with auto-scrolling.',
    ).tag(sync=True)

    open_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Affects how items with children behave when expanded.\n- **multiple:** Any number of groups can be open at once.\n- **single:** Only one group at each level can be open, opening a group will cause others to close.\n- **list:** Multiple, but all other groups will close when an item is selected.",
    ).tag(sync=True)

    opened = Any(
        help="An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`."
    ).tag(sync=True)

    prepend_gap = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the horizontal spacing between prepend slot and the main content within list item. Also affects indent to ensure expected alignment of group children.",
    ).tag(sync=True)

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    select_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Affects how items with children behave when selected.\n- **leaf:** Only leaf nodes (items without children) can be selected.\n- **independent:** All nodes can be selected whether they have children or not.\n- **classic:** Selecting a parent node will cause all children to be selected, parent nodes will be displayed as selected if all their descendants are selected. Only leaf nodes will be added to the model.\n- **trunk**: Same as classic but if all of a node's children are selected then only that node will be added to the model.\n- **branch**: Same as classic but if any of a node's children are selected then that node will also be added to the model.",
    ).tag(sync=True)

    selectable = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether the list items are selectable. Additionally, sets necessary accessibility attributes internally.",
    ).tag(sync=True)

    selected = Any(
        help="An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`."
    ).tag(sync=True)

    slim = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces horizontal spacing for badges, icons, tooltips, and avatars within slim list items to create a more compact visual representation.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class ListGroup(VuetifyWidget):
    """Widget for the Vuetify v-list-group component, see https://vuetifyjs.com/en/api/v-list-group/"""

    _model_name = Unicode("ListGroupModel").tag(sync=True)

    active_color = Unicode(
        default_value=None, allow_none=True, help="Deprecated, use `color` instead."
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    collapse_icon = Any(help="Icon to display when the list item is expanded.").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None, allow_none=True, help="Puts all children inputs into a disabled state."
    ).tag(sync=True)

    expand_icon = Any(help="Icon to display when the list item is collapsed.").tag(sync=True)

    fluid = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the left padding assigned for action icons from group items.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    raw_id = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help='Defines the root element\'s id attribute in the component. If it is provided, the id attribute will be dynamically generated in the format: "v-list-group--id-[rawId]".',
    ).tag(sync=True)

    subgroup = Bool(
        default_value=None, allow_none=True, help="Designate the component as nested list group."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    value = Any(help="Expands / Collapse the list-group.").tag(sync=True)


class ListImg(VuetifyWidget):
    """Widget for the Vuetify v-list-img component, see https://vuetifyjs.com/en/api/v-list-img/"""

    _model_name = Unicode("ListImgModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class ListItem(VuetifyWidget):
    """Widget for the Vuetify v-list-item component, see https://vuetifyjs.com/en/api/v-list-item/"""

    _model_name = Unicode("ListItemModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None, allow_none=True, help="Deprecated, use `color` instead."
    ).tag(sync=True)

    append_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control when in an **active** state or **input-value** is **true** - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors),",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    index = Float(default_value=None, allow_none=True).tag(sync=True)

    lines = Union(
        [Bool(), Unicode(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="The line declaration specifies the minimum height of the item and can also be controlled from v-list with the same prop.",
    ).tag(sync=True)

    link = Bool(
        default_value=None,
        allow_none=True,
        help="Designates that the component is a link. This is automatic when using the href or to prop.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    nav = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces the width v-list-item takes up as well as adding a border radius.",
    ).tag(sync=True)

    prepend_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.",
    ).tag(sync=True)

    prepend_gap = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    slim = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces horizontal spacing for badges, icons, tooltips, and avatars to create a more compact visual representation.",
    ).tag(sync=True)

    subtitle = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify a subtitle text for the component.",
    ).tag(sync=True)

    tabindex = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help='Controls the tabindex of the list item. When set, overrides the default tabindex behavior. Automatically set to -1 by VList when using `navigationStrategy="track"` to prevent Tab key navigation into items.',
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Generates a `v-list-item-title` component with the supplied value. Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title) attribute, that must be set with `v-bind:title.attr` instead.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    value = Any(
        help="The value used for selection. Obtained from [`v-list`](https://vuetifyjs.com/en/api/v-list)'s `v-model:selected` when the item is selected."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class ListItemAction(VuetifyWidget):
    """Widget for the Vuetify v-list-item-action component, see https://vuetifyjs.com/en/api/v-list-item-action/"""

    _model_name = Unicode("ListItemActionModel").tag(sync=True)

    end = Bool(
        default_value=None, allow_none=True, help="Applies margin at the start of the component."
    ).tag(sync=True)

    start = Bool(
        default_value=None, allow_none=True, help="Applies margin at the end of the component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class ListItemMedia(VuetifyWidget):
    """Widget for the Vuetify v-list-item-media component, see https://vuetifyjs.com/en/api/v-list-item-media/"""

    _model_name = Unicode("ListItemMediaModel").tag(sync=True)

    end = Bool(
        default_value=None, allow_none=True, help="Applies margin at the start of the component."
    ).tag(sync=True)

    start = Bool(
        default_value=None, allow_none=True, help="Applies margin at the end of the component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class ListItemSubtitle(VuetifyWidget):
    """Widget for the Vuetify v-list-item-subtitle component, see https://vuetifyjs.com/en/api/v-list-item-subtitle/"""

    _model_name = Unicode("ListItemSubtitleModel").tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the component's opacity value",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class ListItemTitle(VuetifyWidget):
    """Widget for the Vuetify v-list-item-title component, see https://vuetifyjs.com/en/api/v-list-item-title/"""

    _model_name = Unicode("ListItemTitleModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class ListSubheader(VuetifyWidget):
    """Widget for the Vuetify v-list-subheader component, see https://vuetifyjs.com/en/api/v-list-subheader/"""

    _model_name = Unicode("ListSubheaderModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    inset = Bool(
        default_value=None,
        allow_none=True,
        help="Insets the subheader without additional spacing, aligning it flush with the surrounding content.",
    ).tag(sync=True)

    sticky = Bool(
        default_value=None, allow_none=True, help="Sticks the header to the top of the table."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)


class LocaleProvider(VuetifyWidget):
    """Widget for the Vuetify v-locale-provider component, see https://vuetifyjs.com/en/api/v-locale-provider/"""

    _model_name = Unicode("LocaleProviderModel").tag(sync=True)

    fallback_locale = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a fallback locale to use when a locale is not found.",
    ).tag(sync=True)

    locale = Unicode(default_value=None, allow_none=True, help="Specify a locale to use.").tag(
        sync=True
    )

    messages = Any(help="Displays a list of messages or a single message if using a string.").tag(
        sync=True
    )

    rtl = Bool(default_value=None, allow_none=True, help="Specify a RTL mode.").tag(sync=True)


class Main(VuetifyWidget):
    """Widget for the Vuetify v-main component, see https://vuetifyjs.com/en/api/v-main/"""

    _model_name = Unicode("MainModel").tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    scrollable = Bool(
        default_value=None, allow_none=True, help="Specify a custom scrollable function."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class MaskInput(VuetifyWidget):
    """Widget for the Vuetify v-mask-input component, see https://vuetifyjs.com/en/api/v-mask-input/"""

    _model_name = Unicode("MaskInputModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True, help="Enables autofocus.").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Float(
        default_value=None, allow_none=True, help="Function returns the counter display text."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    dirty = Bool(
        default_value=None, allow_none=True, help="Manually apply the dirty state styling."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-mask-input/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    mask = Union(
        [Unicode(), Dict()],
        default_value=None,
        allow_none=True,
        help="Apply a mask to the input. See [guide](https://vuetifyjs.com/en/components/mask-inputs/#guide) for more information.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-mask-input/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    return_masked_value = Bool(
        default_value=None, allow_none=True, help="Returns the unmodified masked string."
    ).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    role = Unicode(
        default_value=None, allow_none=True, help="The role attribute applied to the input."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a border radius to the input.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True, help="Sets input type.").tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Menu(VuetifyWidget):
    """Widget for the Vuetify v-menu component, see https://vuetifyjs.com/en/api/v-menu/"""

    _model_name = Unicode("MenuModel").tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default. Generally not recommended except as a last resort: the default positioning algorithm should handle most scenarios better than is possible without teleporting, and you may have unexpected behavior if the menu ends up as child of its activator.",
    ).tag(sync=True)

    capture_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only works with the **open-on-hover** prop.",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None,
        allow_none=True,
        help="Designates if menu should close when its content is clicked.",
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    disable_initial_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Deprecated, use `capture-focus` instead. Prevents automatic redirect of first `focusin` event. Intended to use on permanently open menus or VSpeedDial.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    id = Unicode(
        default_value=None, allow_none=True, help="The unique identifier of the component."
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component. Use `auto` to use the activator width.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    no_click_animation = Bool(
        default_value=None,
        allow_none=True,
        help="Disables the bounce effect when clicking outside of the content element when using the persistent prop.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only works with the **open-on-hover** prop.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether menu should open on activator click.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether menu should open on activator hover.",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    persistent = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking outside of the element or pressing esc key will not deactivate it.",
    ).tag(sync=True)

    retain_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    scroll_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Strategy used when the component is activate and user scrolls.",
    ).tag(sync=True)

    stick_to_target = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the overlay content to go off-screen when scrolling.",
    ).tag(sync=True)

    submenu = Bool(
        default_value=None,
        allow_none=True,
        help='Opens with right arrow and closes on left instead of up/down. Implies `location="end"`. Directions are reversed for RTL.',
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    viewport_margin = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom viewport margin for the overlay content",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class Messages(VuetifyWidget):
    """Widget for the Vuetify v-messages component, see https://vuetifyjs.com/en/api/v-messages/"""

    _model_name = Unicode("MessagesModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Determines whether the messages are visible or not.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)


class NavigationDrawer(VuetifyWidget):
    """Widget for the Vuetify v-navigation-drawer component, see https://vuetifyjs.com/en/api/v-navigation-drawer/"""

    _model_name = Unicode("NavigationDrawerModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies **position: absolute** to the component."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    capture_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disable_resize_watcher = Bool(
        default_value=None,
        allow_none=True,
        help="Prevents the automatic opening or closing of the drawer when resized, based on whether the device is mobile or desktop.",
    ).tag(sync=True)

    disable_route_watcher = Bool(
        default_value=None,
        allow_none=True,
        help="Disables opening of navigation drawer when route changes.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    expand_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Collapses the drawer to a **rail-variant** until hovering with the mouse.",
    ).tag(sync=True)

    floating = Bool(
        default_value=None,
        allow_none=True,
        help="A floating drawer has no visible container (no border-right).",
    ).tag(sync=True)

    image = Unicode(
        default_value=None,
        allow_none=True,
        help="Apply a specific background image to the component.",
    ).tag(sync=True)

    location = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls the edge of the screen the drawer is attached to.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Sets the designated mobile breakpoint for the component. This will apply alternate styles for mobile devices such as the `temporary` prop, or activate the `bottom` prop when the breakpoint value is met. Setting the value to `0` will disable this functionality.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Assign a specific name for layout registration."
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)

    order = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Adjust the order of the component in relation to its registration order.",
    ).tag(sync=True)

    permanent = Bool(
        default_value=None,
        allow_none=True,
        help="The drawer remains visible regardless of screen size.",
    ).tag(sync=True)

    persistent = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking outside or pressing **esc** key will not dismiss the dialog.",
    ).tag(sync=True)

    rail = Bool(
        default_value=None,
        allow_none=True,
        help="Sets the component width to the **rail-width** value.",
    ).tag(sync=True)

    rail_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component when `rail` is enabled.",
    ).tag(sync=True)

    retain_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Determines whether an overlay is used when a **temporary** drawer is open. Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    sticky = Bool(
        default_value=None,
        allow_none=True,
        help="When true, the drawer will remain visible when scrolling past the top of the page.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    temporary = Bool(
        default_value=None,
        allow_none=True,
        help="A temporary drawer sits above its application and uses a scrim (overlay) to darken the background.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    touchless = Bool(
        default_value=None, allow_none=True, help="Disable mobile touch functionality."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class NoSsr(VuetifyWidget):
    """Widget for the Vuetify v-no-ssr component, see https://vuetifyjs.com/en/api/v-no-ssr/"""

    _model_name = Unicode("NoSsrModel").tag(sync=True)


class NumberInput(VuetifyWidget):
    """Widget for the Vuetify v-number-input component, see https://vuetifyjs.com/en/api/v-number-input/"""

    _model_name = Unicode("NumberInputModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True, help="Enables autofocus.").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    control_variant = Unicode(
        default_value=None, allow_none=True, help="Controls layout of the stepper buttons."
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Float(
        default_value=None, allow_none=True, help="Function returns the counter display text."
    ).tag(sync=True)

    decimal_separator = Unicode(
        default_value=None,
        allow_none=True,
        help="Expects single character to be used as decimal separator.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    dirty = Bool(
        default_value=None, allow_none=True, help="Manually apply the dirty state styling."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_input = Bool(default_value=None, allow_none=True, help="Hide the input field.").tag(
        sync=True
    )

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-number-input/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    inset = Bool(
        default_value=None,
        allow_none=True,
        help="Applies an indentation to the dividers used in the stepper buttons.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Specifies the maximum allowable value for the input.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min = Float(
        default_value=None,
        allow_none=True,
        help="Specifies the minimum allowable value for the input.",
    ).tag(sync=True)

    min_fraction_digits = Float(
        default_value=None,
        allow_none=True,
        help="Specifies the minimum fraction digits to be displayed (capped to `precision`). Defaults to `precision` when not explicitly set.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Float(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-number-input/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    precision = Float(
        default_value=None,
        allow_none=True,
        help="Enforces strict precision. It is expected to be an integer value in range between `0` and `15`, or null for unrestricted.",
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    role = Unicode(
        default_value=None, allow_none=True, help="The role attribute applied to the input."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a border radius to the input.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    step = Float(
        default_value=None,
        allow_none=True,
        help="Defines the interval between allowed values when the user increments or decrements the input",
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="**IGNORED** underlying input is always of type 'text'",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class OtpInput(VuetifyWidget):
    """Widget for the Vuetify v-otp-input component, see https://vuetifyjs.com/en/api/v-otp-input/"""

    _model_name = Unicode("OtpInputModel").tag(sync=True)

    autofocus = Bool(
        default_value=None,
        allow_none=True,
        help="Automatically focuses the first input on page load",
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    divider = Unicode(
        default_value=None, allow_none=True, help="Specifies the dividing character between items."
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    focus_all = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all inputs into a focus state when any are focused",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    length = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="The OTP field's length."
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    masked = Bool(
        default_value=None,
        allow_none=True,
        help='Hides the entered characters with bullets, similar to a password input, but makes it possible to also restrict characters to digits with `type="number"`.',
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    type = Unicode(
        default_value=None, allow_none=True, help="Supported types: `text`, `password`, `number`."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Overlay(VuetifyWidget):
    """Widget for the Vuetify v-overlay component, see https://vuetifyjs.com/en/api/v-overlay/"""

    _model_name = Unicode("OverlayModel").tag(sync=True)

    absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **position: absolute** to the content element.",
    ).tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.",
    ).tag(sync=True)

    capture_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None, allow_none=True, help="Closes component when you click on its content."
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    no_click_animation = Bool(
        default_value=None,
        allow_none=True,
        help="Disables the bounce effect when clicking outside of the content element when using the persistent prop.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is clicked.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is hovered.",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    persistent = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking outside of the element or pressing esc key will not deactivate it.",
    ).tag(sync=True)

    retain_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    scroll_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Strategy used when the component is activate and user scrolls.",
    ).tag(sync=True)

    stick_to_target = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the overlay content to go off-screen when scrolling.",
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    viewport_margin = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom viewport margin for the overlay content",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class Pagination(VuetifyWidget):
    """Widget for the Vuetify v-pagination component, see https://vuetifyjs.com/en/api/v-pagination/"""

    _model_name = Unicode("PaginationModel").tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    aria_label = Unicode(
        default_value=None, allow_none=True, help="Label for the root element."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the selected page button - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    current_page_aria_label = Unicode(
        default_value=None, allow_none=True, help="Label for the currently selected page."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    ellipsis = Unicode(
        default_value=None,
        allow_none=True,
        help="Text to show between page buttons when truncating the list.",
    ).tag(sync=True)

    first_aria_label = Unicode(
        default_value=None, allow_none=True, help="Label for the go to first button."
    ).tag(sync=True)

    first_icon = Any(help="The icon to use for the first button.").tag(sync=True)

    last_aria_label = Unicode(
        default_value=None, allow_none=True, help="Label for the go to last button."
    ).tag(sync=True)

    last_icon = Any(help="The icon to use for the last button.").tag(sync=True)

    length = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="The number of pages."
    ).tag(sync=True)

    model_value = Float(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    next_aria_label = Unicode(
        default_value=None, allow_none=True, help="Label for the next button."
    ).tag(sync=True)

    next_icon = Any(help="The icon to use for the next button.").tag(sync=True)

    page_aria_label = Unicode(
        default_value=None, allow_none=True, help="Label for each page button."
    ).tag(sync=True)

    prev_icon = Any(help="The icon to use for the prev button.").tag(sync=True)

    previous_aria_label = Unicode(
        default_value=None, allow_none=True, help="Label for the previous button."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    show_first_last_page = Bool(
        default_value=None, allow_none=True, help="Show buttons for going to first and last page."
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    start = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Specify the starting page."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    total_visible = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Specify the total visible pagination numbers.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class Parallax(VuetifyWidget):
    """Widget for the Vuetify v-parallax component, see https://vuetifyjs.com/en/api/v-parallax/"""

    _model_name = Unicode("ParallaxModel").tag(sync=True)

    scale = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The scale of the parallax image.",
    ).tag(sync=True)


class Picker(VuetifyWidget):
    """Widget for the Vuetify v-picker component, see https://vuetifyjs.com/en/api/v-picker/"""

    _model_name = Unicode("PickerModel").tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    divided = Bool(
        default_value=None, allow_none=True, help="Adds a divider between the header and controls."
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_header = Bool(default_value=None, allow_none=True, help="Hide the picker header.").tag(
        sync=True
    )

    hide_title = Bool(default_value=None, allow_none=True, help="Hide the picker title.").tag(
        sync=True
    )

    landscape = Bool(
        default_value=None, allow_none=True, help="Puts the picker into landscape mode."
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class PickerTitle(VuetifyWidget):
    """Widget for the Vuetify v-picker-title component, see https://vuetifyjs.com/en/api/v-picker-title/"""

    _model_name = Unicode("PickerTitleModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class Pie(VuetifyWidget):
    """Widget for the Vuetify v-pie component, see https://vuetifyjs.com/en/api/v-pie/"""

    _model_name = Unicode("PieModel").tag(sync=True)

    animation = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Controls duration and easing of the expand/collapse and hover effect. Defaults to `easeInOutCubic` over 400ms.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    gap = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Reduces segment size by a specified angle. Recommended to in range (0-10).",
    ).tag(sync=True)

    gauge_cut = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Allows removing bottom part of the chart to make it into a gauge. Expects angle (0-180).",
    ).tag(sync=True)

    hide_slice = Bool(
        default_value=None,
        allow_none=True,
        help="Makes inner slice invisible instead of semi-transparent.",
    ).tag(sync=True)

    hover_scale = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Enables interactive behavior by reducing segment size until it gets hovered. Expects fraction value (0-0.25).",
    ).tag(sync=True)

    inner_cut = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Specifies inner radius for a donut-style chart as a percent (0-100). Without `hide-slice`, inner slice is visible with translucent color matching the item.",
    ).tag(sync=True)

    item_key = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = Union(
        [Dict(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Data items expected to contain `key`, `title` and `value`.",
    ).tag(sync=True)

    legend = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Controls legend visibility, position and text format.",
    ).tag(sync=True)

    palette = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Defines colors and patterns to be applied based on the data items order. Data items can also define their colors.",
    ).tag(sync=True)

    reveal = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Enables and controls duration for initial reveal animation. Easing function is shared with `animation` prop.",
    ).tag(sync=True)

    rotate = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Rotates the chart segments clockwise.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Number passed as corner radius relative to 100x100 SVG viewport",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the chart (excluding title and legend).",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    tooltip = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Controls tooltip visibility, transition, offset from the cursor and formats of title and subtitle.",
    ).tag(sync=True)


class PieSegment(VuetifyWidget):
    """Widget for the Vuetify v-pie-segment component, see https://vuetifyjs.com/en/api/v-pie-segment/"""

    _model_name = Unicode("PieSegmentModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    animation = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Controls duration and easing of the expand/collapse and hover effect. Defaults to `easeInOutCubic` over 400ms.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets segment color to be passed straight to CSS style attribute.",
    ).tag(sync=True)

    gap = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Reduces segment size by a specified angle. Recommended to in range (0-10).",
    ).tag(sync=True)

    hide_slice = Bool(
        default_value=None,
        allow_none=True,
        help="Makes inner slice invisible instead of semi-transparent.",
    ).tag(sync=True)

    hover_scale = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Reduces outer radius until segment is hovered. Expects fraction value (0-0.25)",
    ).tag(sync=True)

    inner_cut = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets inner slice size in percent (0-100).",
    ).tag(sync=True)

    pattern = Unicode(
        default_value=None, allow_none=True, help="Decal pattern to put on top of the outer slice."
    ).tag(sync=True)

    reveal = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Enables and controls duration for initial reveal animation. Easing function is shared with `animation` prop.",
    ).tag(sync=True)

    rotate = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Sets segment offset angle."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Number passed as corner radius relative to 100x100 SVG viewport",
    ).tag(sync=True)

    value = Float(
        default_value=None,
        allow_none=True,
        help="The value used for calculate segment/arc angle size.",
    ).tag(sync=True)


class PieTooltip(VuetifyWidget):
    """Widget for the Vuetify v-pie-tooltip component, see https://vuetifyjs.com/en/api/v-pie-tooltip/"""

    _model_name = Unicode("PieTooltipModel").tag(sync=True)

    item = Dict(
        default_value=None, allow_none=True, help="Data item related to hovered segment"
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    subtitle_format = Unicode(
        default_value=None,
        allow_none=True,
        help="Formatter definition or function. When passed as String macros for `[title]` and `[value]` get replaced dynamically.",
    ).tag(sync=True)

    target = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    title_format = Unicode(
        default_value=None,
        allow_none=True,
        help="Formatter definition or function. When passed as String macros for `[title]` and `[value]` get replaced dynamically.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="The transition used when hovering between chart segments",
    ).tag(sync=True)


class ProgressCircular(VuetifyWidget):
    """Widget for the Vuetify v-progress-circular component, see https://vuetifyjs.com/en/api/v-progress-circular/"""

    _model_name = Unicode("ProgressCircularModel").tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    indeterminate = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Constantly animates, use when loading progress is unknown. If set to the string `'disable-shrink'` it will use a simpler animation that does not run on the main thread.",
    ).tag(sync=True)

    model_value = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The percentage value for current progress.",
    ).tag(sync=True)

    reveal = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Animates the progress circle from 0 to its model value when the component mounts.",
    ).tag(sync=True)

    rotate = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Rotates the circle start point in degrees.",
    ).tag(sync=True)

    rounded = Bool(
        default_value=None,
        allow_none=True,
        help="Rounds the ends of the progress arc for a softer appearance. When enabled, the progress stroke will have rounded caps instead of square ends.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the diameter of the circle in pixels.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the stroke of the circle in pixels.",
    ).tag(sync=True)


class ProgressLinear(VuetifyWidget):
    """Widget for the Vuetify v-progress-linear component, see https://vuetifyjs.com/en/api/v-progress-linear/"""

    _model_name = Unicode("ProgressLinearModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies position: absolute to the component."
    ).tag(sync=True)

    active = Bool(
        default_value=None, allow_none=True, help="Reduce the height to 0, hiding component."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    bg_opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Background opacity, if null it defaults to 0.3 if background color is not specified or 1 otherwise.",
    ).tag(sync=True)

    buffer_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of the buffer bar."
    ).tag(sync=True)

    buffer_opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Set the opacity of the buffer bar.",
    ).tag(sync=True)

    buffer_value = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The percentage value for the buffer.",
    ).tag(sync=True)

    chunk_count = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Specifies amount of chunks to divide the bar into.",
    ).tag(sync=True)

    chunk_gap = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Defines size of the gap between chunks.",
    ).tag(sync=True)

    chunk_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Defines chunk absolute size. Useful when chunk is narrow.",
    ).tag(sync=True)

    clickable = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking on the progress track will automatically set the value.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    indeterminate = Bool(
        default_value=None,
        allow_none=True,
        help="Constantly animates, use when loading progress is unknown.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum value the progress can reach.",
    ).tag(sync=True)

    model_value = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Set the opacity of the progress bar.",
    ).tag(sync=True)

    reverse = Bool(
        default_value=None,
        allow_none=True,
        help="Displays reversed progress (right to left in LTR mode and left to right in RTL).",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    rounded_bar = Bool(
        default_value=None, allow_none=True, help="Applies a border radius to the progress bar."
    ).tag(sync=True)

    stream = Bool(
        default_value=None,
        allow_none=True,
        help="An alternative style for portraying loading that works in tandem with **buffer-value**.",
    ).tag(sync=True)

    striped = Bool(
        default_value=None,
        allow_none=True,
        help="Adds a stripe background to the filled portion of the progress component.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)


class PullToRefresh(VuetifyWidget):
    """Widget for the Vuetify v-pull-to-refresh component, see https://vuetifyjs.com/en/api/v-pull-to-refresh/"""

    _model_name = Unicode("PullToRefreshModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    pull_down_threshold = Float(
        default_value=None,
        allow_none=True,
        help="The distance the user must pull down to trigger a refresh.",
    ).tag(sync=True)


class Radio(VuetifyWidget):
    """Widget for the Vuetify v-radio component, see https://vuetifyjs.com/en/api/v-radio/"""

    _model_name = Unicode("RadioModel").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    defaults_target = Unicode(
        default_value=None,
        allow_none=True,
        help="The target component to provide defaults values for.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    false_icon = Any(help="The icon used when inactive.").tag(sync=True)

    false_value = Any(help="Sets value for falsy state.").tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    inline = Bool(default_value=None, allow_none=True, help="Puts children inputs into a row.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None,
        allow_none=True,
        help="Changes select to multiple. Accepts array for value.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    true_icon = Any(help="The icon used when active.").tag(sync=True)

    true_value = Any(help="Sets value for truthy state.").tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Provides the default type for children selection controls.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)


class RadioGroup(VuetifyWidget):
    """Widget for the Vuetify v-radio-group component, see https://vuetifyjs.com/en/api/v-radio-group/"""

    _model_name = Unicode("RadioGroupModel").tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    defaults_target = Unicode(
        default_value=None,
        allow_none=True,
        help="The target component to provide defaults values for.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    false_icon = Any(help="The icon used when inactive.").tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the input is focused and apply color.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height of the input.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-radio-group/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    inline = Bool(default_value=None, allow_none=True, help="Displays radio buttons in row.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-radio-group/#props-hint) to always be visible.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    true_icon = Any(help="The icon used when active.").tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Provides the default type for children selection controls.",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class RangeSlider(VuetifyWidget):
    """Widget for the Vuetify v-range-slider component, see https://vuetifyjs.com/en/api/v-range-slider/"""

    _model_name = Unicode("RangeSliderModel").tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(
        default_value=None, allow_none=True, help="Changes the direction of the input."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the input is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-range-slider/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    max = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum allowed value.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum allowed value.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    no_keyboard = Bool(
        default_value=None,
        allow_none=True,
        help="**FOR INTERNAL USE ONLY** Ignore keyboard events.",
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-range-slider/#props-hint) to always be visible.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the slider direction.").tag(
        sync=True
    )

    ripple = Bool(
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    show_ticks = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.",
    ).tag(sync=True)

    step = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="If greater than 0, sets step interval for ticks.",
    ).tag(sync=True)

    strict = Bool(
        default_value=None,
        allow_none=True,
        help="Disallows dragging the ending thumb past the starting thumb and vice versa.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    thumb_color = Unicode(
        default_value=None, allow_none=True, help="Sets the thumb and thumb label color."
    ).tag(sync=True)

    thumb_label = Union(
        [Bool(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Show thumb label. If `true` it shows label when using slider. If set to `'always'` it always shows label. (since [v3.12.0](https://vuetifyjs.com/en/getting-started/release-notes/?version=v3.12.0) it supports `'hover'` to show label when hovering over the thumb.",
    ).tag(sync=True)

    thumb_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Controls the size of the thumb label.",
    ).tag(sync=True)

    tick_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Controls the size of **ticks**",
    ).tag(sync=True)

    ticks = Union(
        [TList(Any()), Dict()],
        default_value=None,
        allow_none=True,
        help="Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    track_color = Unicode(default_value=None, allow_none=True, help="Sets the track's color").tag(
        sync=True
    )

    track_fill_color = Unicode(
        default_value=None, allow_none=True, help="Sets the track's fill color"
    ).tag(sync=True)

    track_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the track's size (height).",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Rating(VuetifyWidget):
    """Widget for the Vuetify v-rating component, see https://vuetifyjs.com/en/api/v-rating/"""

    _model_name = Unicode("RatingModel").tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    clearable = Bool(
        default_value=None,
        allow_none=True,
        help="Allows for the component to be cleared by clicking on the current value.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    empty_icon = Any(help="The icon displayed when empty.").tag(sync=True)

    full_icon = Any(help="The icon displayed when full.").tag(sync=True)

    half_increments = Bool(
        default_value=None, allow_none=True, help="Allows the selection of half increments."
    ).tag(sync=True)

    hover = Bool(
        default_value=None,
        allow_none=True,
        help="Provides visual feedback when hovering over icons.",
    ).tag(sync=True)

    item_aria_label = Unicode(
        default_value=None, allow_none=True, help="The **aria-label** used for each item."
    ).tag(sync=True)

    item_label_position = Unicode(
        default_value=None,
        allow_none=True,
        help="Position of item labels. Accepts 'top' and 'bottom'.",
    ).tag(sync=True)

    item_labels = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of labels to display next to each item..",
    ).tag(sync=True)

    length = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The amount of items to show.",
    ).tag(sync=True)

    model_value = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    readonly = Bool(
        default_value=None, allow_none=True, help="Removes all hover effects and pointer events."
    ).tag(sync=True)

    ripple = Bool(
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)


class Responsive(VuetifyWidget):
    """Widget for the Vuetify v-responsive component, see https://vuetifyjs.com/en/api/v-responsive/"""

    _model_name = Unicode("ResponsiveModel").tag(sync=True)

    aspect_ratio = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets a base aspect ratio, calculated as width/height. This will only set a **minimum** height, the component can still grow if it has a lot of content.",
    ).tag(sync=True)

    content_class = Any(help="Apply a custom class to the internal content element.").tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    inline = Bool(
        default_value=None,
        allow_none=True,
        help="Display as an inline element instead of a block, also disables flex-grow.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Row(VuetifyWidget):
    """Widget for the Vuetify v-row component, see https://vuetifyjs.com/en/api/v-row/"""

    _model_name = Unicode("RowModel").tag(sync=True)

    align = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies the [align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) css property. Available options are: **start**, **center**, **end**, **baseline** and **stretch**.",
    ).tag(sync=True)

    align_content = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies the [align-content](https://developer.mozilla.org/en-US/docs/Web/CSS/align-content) css property. Available options are: **start**, **center**, **end**, **space-between**, **space-around** and **stretch**.",
    ).tag(sync=True)

    align_content_lg = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-content** property on large and greater breakpoints.",
    ).tag(sync=True)

    align_content_md = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-content** property on medium and greater breakpoints.",
    ).tag(sync=True)

    align_content_sm = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-content** property on small and greater breakpoints.",
    ).tag(sync=True)

    align_content_xl = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-content** property on extra large and greater breakpoints.",
    ).tag(sync=True)

    align_content_xxl = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-content** property on extra extra large and greater breakpoints.",
    ).tag(sync=True)

    align_lg = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-items** property on large and greater breakpoints.",
    ).tag(sync=True)

    align_md = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-items** property on medium and greater breakpoints.",
    ).tag(sync=True)

    align_sm = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-items** property on small and greater breakpoints.",
    ).tag(sync=True)

    align_xl = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-items** property on extra large and greater breakpoints.",
    ).tag(sync=True)

    align_xxl = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **align-items** property on extra extra large and greater breakpoints.",
    ).tag(sync=True)

    dense = Bool(
        default_value=None, allow_none=True, help="Reduces the gutter between `v-col`s."
    ).tag(sync=True)

    justify = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies the [justify-content](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content) css property. Available options are: **start**, **center**, **end**, **space-between** and **space-around**.",
    ).tag(sync=True)

    justify_lg = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **justify-content** property on large and greater breakpoints.",
    ).tag(sync=True)

    justify_md = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **justify-content** property on medium and greater breakpoints.",
    ).tag(sync=True)

    justify_sm = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **justify-content** property on small and greater breakpoints.",
    ).tag(sync=True)

    justify_xl = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **justify-content** property on extra large and greater breakpoints.",
    ).tag(sync=True)

    justify_xxl = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the **justify-content** property on extra extra large and greater breakpoints.",
    ).tag(sync=True)

    no_gutters = Bool(
        default_value=None, allow_none=True, help="Removes the gutter between `v-col`s."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class ScaleTransition(VuetifyWidget):
    """Widget for the Vuetify v-scale-transition component, see https://vuetifyjs.com/en/api/v-scale-transition/"""

    _model_name = Unicode("ScaleTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class ScrollXReverseTransition(VuetifyWidget):
    """Widget for the Vuetify v-scroll-x-reverse-transition component, see https://vuetifyjs.com/en/api/v-scroll-x-reverse-transition/"""

    _model_name = Unicode("ScrollXReverseTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class ScrollXTransition(VuetifyWidget):
    """Widget for the Vuetify v-scroll-x-transition component, see https://vuetifyjs.com/en/api/v-scroll-x-transition/"""

    _model_name = Unicode("ScrollXTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class ScrollYReverseTransition(VuetifyWidget):
    """Widget for the Vuetify v-scroll-y-reverse-transition component, see https://vuetifyjs.com/en/api/v-scroll-y-reverse-transition/"""

    _model_name = Unicode("ScrollYReverseTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class ScrollYTransition(VuetifyWidget):
    """Widget for the Vuetify v-scroll-y-transition component, see https://vuetifyjs.com/en/api/v-scroll-y-transition/"""

    _model_name = Unicode("ScrollYTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class Select(VuetifyWidget):
    """Widget for the Vuetify v-select component, see https://vuetifyjs.com/en/api/v-select/"""

    _model_name = Unicode("SelectModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True, help="Enables autofocus.").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    chips = Bool(
        default_value=None, allow_none=True, help="Changes display of selections to chips."
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    closable_chips = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the [closable](https://vuetifyjs.com/en/api/v-chip/#props-closable) prop on all [v-chip](https://vuetifyjs.com/en/components/chips/) components.",
    ).tag(sync=True)

    close_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text set to the inputs `aria-label` and `title` when input menu is closed.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Float(
        default_value=None, allow_none=True, help="Function returns the counter display text."
    ).tag(sync=True)

    custom_filter = Any(
        help="Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted."
    ).tag(sync=True)

    custom_key_filter = Any(
        help="Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    filter_keys = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Array of specific keys to filter on the item.",
    ).tag(sync=True)

    filter_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.\n\n- **some**: There is at least one match from either the custom filter or the custom key filter.\n- **every**: All columns match either the custom filter or the custom key filter.\n- **union**: There is at least one match from the custom filter, or all columns match the custom key filters.\n- **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_no_data = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.",
    ).tag(sync=True)

    hide_selected = Bool(
        default_value=None,
        allow_none=True,
        help="Do not display in the select menu items that are already selected.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-select/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    item_children = Unicode(
        default_value=None, allow_none=True, help="This property currently has **no effect**."
    ).tag(sync=True)

    item_color = Unicode(
        default_value=None, allow_none=True, help="Sets color of selected items."
    ).tag(sync=True)

    item_props = Unicode(
        default_value=None,
        allow_none=True,
        help="Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.",
    ).tag(sync=True)

    item_title = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its title.",
    ).tag(sync=True)

    item_type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Set property of **items**'s value - **must be primitive**. Dot notation is supported. **Note:** This is currently not supported with `v-combobox` [GitHub Issue](https://github.com/vuetifyjs/vuetify/issues/5479).",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Can be an array of objects or strings. By default objects should have **title** and **value** properties, and can optionally have a **props** property containing any [VListItem props](https://vuetifyjs.com/en/api/v-list-item/#props). Keys to use for these can be changed with the **item-title**, **item-value**, and **item-props** props.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    list_props = Any(
        help="Pass props through to the `v-list` component. Accepts an object with anything from [v-list](https://vuetifyjs.com/en/api/v-list/#props) props, camelCase keys are recommended."
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    menu = Bool(
        default_value=None, allow_none=True, help="Renders with the menu open by default."
    ).tag(sync=True)

    menu_icon = Any(help="Sets the the spin icon.").tag(sync=True)

    menu_props = Any(
        help="Pass props through to the `v-menu` component. Accepts an object with anything from [v-menu](https://vuetifyjs.com/en/api/v-menu/#props) props, camelCase keys are recommended."
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width of the select's `v-menu` content.",
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None,
        allow_none=True,
        help="Changes select to multiple. Accepts array for value.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    no_auto_scroll = Bool(
        default_value=None,
        allow_none=True,
        help="Prevents the select menu to scroll to the selected item automatically.",
    ).tag(sync=True)

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when no items are provided to the component.",
    ).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True, help="Disables all item filtering.").tag(
        sync=True
    )

    open_on_clear = Bool(
        default_value=None,
        allow_none=True,
        help="When using the **clearable** prop, once cleared, the select menu will either open or stay open, depending on the current state.",
    ).tag(sync=True)

    open_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text set to the inputs **aria-label** and **title** when input menu is open.",
    ).tag(sync=True)

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-select/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the selection behavior to return the object directly rather than the value specified with **item-value**.",
    ).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    role = Unicode(
        default_value=None, allow_none=True, help="The role attribute applied to the input."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a border radius to the input.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    search = Unicode(
        default_value=None, allow_none=True, help="Text input used to filter items."
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True, help="Sets input type.").tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class SelectionControl(VuetifyWidget):
    """Widget for the Vuetify v-selection-control component, see https://vuetifyjs.com/en/api/v-selection-control/"""

    _model_name = Unicode("SelectionControlModel").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    defaults_target = Unicode(
        default_value=None,
        allow_none=True,
        help="The target component to provide defaults values for.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    false_icon = Any(help="The icon used when inactive.").tag(sync=True)

    false_value = Any(help="Sets value for falsy state.").tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    inline = Bool(default_value=None, allow_none=True, help="Puts children inputs into a row.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None,
        allow_none=True,
        help="Changes select to multiple. Accepts array for value.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    true_icon = Any(help="The icon used when active.").tag(sync=True)

    true_value = Any(help="Sets value for truthy state.").tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Provides the default type for children selection controls.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)


class SelectionControlGroup(VuetifyWidget):
    """Widget for the Vuetify v-selection-control-group component, see https://vuetifyjs.com/en/api/v-selection-control-group/"""

    _model_name = Unicode("SelectionControlGroupModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    defaults_target = Unicode(
        default_value=None,
        allow_none=True,
        help="The target component to provide defaults values for.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    false_icon = Any(help="The icon used when inactive.").tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    inline = Bool(default_value=None, allow_none=True, help="Puts children inputs into a row.").tag(
        sync=True
    )

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None,
        allow_none=True,
        help="Changes select to multiple. Accepts array for value.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    true_icon = Any(help="The icon used when active.").tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Provides the default type for children selection controls.",
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)


class Sheet(VuetifyWidget):
    """Widget for the Vuetify v-sheet component, see https://vuetifyjs.com/en/api/v-sheet/"""

    _model_name = Unicode("SheetModel").tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class SkeletonLoader(VuetifyWidget):
    """Widget for the Vuetify v-skeleton-loader component, see https://vuetifyjs.com/en/api/v-skeleton-loader/"""

    _model_name = Unicode("SkeletonLoaderModel").tag(sync=True)

    boilerplate = Bool(
        default_value=None, allow_none=True, help="Remove the loading animation from the skeleton."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    loading = Bool(
        default_value=None,
        allow_none=True,
        help="Applies a loading animation with a on-hover loading cursor. A value of **false** will only work when there is content in the `default` slot.",
    ).tag(sync=True)

    loading_text = Unicode(
        default_value=None, allow_none=True, help="aria-label for the element in a loading state."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help='A string delimited list of skeleton components to create such as `type="text@3"` or `type="card, list-item"`. Will recursively generate a corresponding skeleton from the provided string. Also supports short-hand for multiple elements such as **article@3** and **paragraph@2** which will generate 3 _article_ skeletons and 2 _paragraph_ skeletons. Please see below for a list of available pre-defined options.',
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class SlideGroup(VuetifyWidget):
    """Widget for the Vuetify v-slide-group component, see https://vuetifyjs.com/en/api/v-slide-group/"""

    _model_name = Unicode("SlideGroupModel").tag(sync=True)

    center_active = Bool(
        default_value=None, allow_none=True, help="Forces the selected component to be centered."
    ).tag(sync=True)

    content_class = Any(help="Adds classes to the slide group item.").tag(sync=True)

    direction = Unicode(
        default_value=None, allow_none=True, help="Switch between horizontal and vertical modes."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Sets the designated mobile breakpoint for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    next_icon = Any(help="The appended slot when arrows are shown.").tag(sync=True)

    prev_icon = Any(help="The prepended slot when arrows are shown.").tag(sync=True)

    scroll_to_active = Bool(
        default_value=None,
        allow_none=True,
        help="Keeps the last active element visible when resizing the scrollable container.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    show_arrows = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Change when the overflow arrow indicators are shown. By **default**, arrows *always* display on Desktop when the container is overflowing. When the container overflows on mobile, arrows are not shown by default. A **show-arrows** value of `true` allows these arrows to show on Mobile if the container overflowing. A value of `desktop` *always* displays arrows on Desktop while a value of `mobile` always displays arrows on Mobile. A value of `always` always displays arrows on Desktop *and* Mobile. Use **never** to turn arrows off. Find more information on how to customize breakpoint thresholds on the [breakpoints page](https://vuetifyjs.com/en/customizing/breakpoints).",
    ).tag(sync=True)

    symbol = Any(
        help="The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/)."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class SlideGroupItem(VuetifyWidget):
    """Widget for the Vuetify v-slide-group-item component, see https://vuetifyjs.com/en/api/v-slide-group-item/"""

    _model_name = Unicode("SlideGroupItemModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)


class SlideXReverseTransition(VuetifyWidget):
    """Widget for the Vuetify v-slide-x-reverse-transition component, see https://vuetifyjs.com/en/api/v-slide-x-reverse-transition/"""

    _model_name = Unicode("SlideXReverseTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class SlideXTransition(VuetifyWidget):
    """Widget for the Vuetify v-slide-x-transition component, see https://vuetifyjs.com/en/api/v-slide-x-transition/"""

    _model_name = Unicode("SlideXTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class SlideYReverseTransition(VuetifyWidget):
    """Widget for the Vuetify v-slide-y-reverse-transition component, see https://vuetifyjs.com/en/api/v-slide-y-reverse-transition/"""

    _model_name = Unicode("SlideYReverseTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class SlideYTransition(VuetifyWidget):
    """Widget for the Vuetify v-slide-y-transition component, see https://vuetifyjs.com/en/api/v-slide-y-transition/"""

    _model_name = Unicode("SlideYTransitionModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    group = Bool(
        default_value=None,
        allow_none=True,
        help="Creates a `transition-group` component. You can find more information in the [vue docs](https://vuejs.org/api/built-in-components.html#transitiongroup).",
    ).tag(sync=True)

    hide_on_leave = Bool(
        default_value=None, allow_none=True, help="Hides the leaving element (no exit animation)."
    ).tag(sync=True)

    leave_absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Absolutely positions the leaving element (useful for [FLIP](https://aerotwist.com/blog/flip-your-animations/)).",
    ).tag(sync=True)

    mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition mode (does not apply to transition-group). You can find more information on the Vue documentation [for transition modes](https://vuejs.org/api/built-in-components.html#transition).",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)


class Slider(VuetifyWidget):
    """Widget for the Vuetify v-slider component, see https://vuetifyjs.com/en/api/v-slider/"""

    _model_name = Unicode("SliderModel").tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(
        default_value=None, allow_none=True, help="Changes the direction of the input."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the input is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-slider/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    max = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum allowed value.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum allowed value.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    no_keyboard = Bool(
        default_value=None,
        allow_none=True,
        help="**FOR INTERNAL USE ONLY** Ignore keyboard events.",
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-slider/#props-hint) to always be visible.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the slider direction.").tag(
        sync=True
    )

    ripple = Bool(
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    show_ticks = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.",
    ).tag(sync=True)

    step = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="If greater than 0, sets step interval for ticks.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    thumb_color = Unicode(
        default_value=None, allow_none=True, help="Sets the thumb and thumb label color."
    ).tag(sync=True)

    thumb_label = Union(
        [Bool(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Show thumb label. If `true` it shows label when using slider. If set to `'always'` it always shows label. (since [v3.12.0](https://vuetifyjs.com/en/getting-started/release-notes/?version=v3.12.0) it supports `'hover'` to show label when hovering over the thumb.",
    ).tag(sync=True)

    thumb_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Controls the size of the thumb label.",
    ).tag(sync=True)

    tick_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Controls the size of **ticks**",
    ).tag(sync=True)

    ticks = Union(
        [TList(Any()), Dict()],
        default_value=None,
        allow_none=True,
        help="Show track ticks. If `true` it shows ticks when using slider. If set to `'always'` it always shows ticks.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    track_color = Unicode(default_value=None, allow_none=True, help="Sets the track's color").tag(
        sync=True
    )

    track_fill_color = Unicode(
        default_value=None, allow_none=True, help="Sets the track's fill color"
    ).tag(sync=True)

    track_size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the track's size (height).",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Snackbar(VuetifyWidget):
    """Widget for the Vuetify v-snackbar component, see https://vuetifyjs.com/en/api/v-snackbar/"""

    _model_name = Unicode("SnackbarModel").tag(sync=True)

    absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **position: absolute** to the content element.",
    ).tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.",
    ).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None, allow_none=True, help="Closes component when you click on its content."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    multi_line = Bool(
        default_value=None,
        allow_none=True,
        help="Deprecated, use `min-height` instead. Increases minimum height.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is clicked.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is hovered.",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    timeout = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Time (in milliseconds) to wait until snackbar is automatically hidden.  Use `-1` to keep open indefinitely (`0` in version < 2.3 ). It is recommended for this number to be between `4000` and `10000`. Changes to this property will reset the timeout.",
    ).tag(sync=True)

    timer = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Display a progress bar that counts down until the snackbar closes. Pass a string to set a custom color, otherwise uses `info`.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    vertical = Bool(
        default_value=None,
        allow_none=True,
        help="Stacks snackbar content on top of the actions (button).",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class SnackbarQueue(VuetifyWidget):
    """Widget for the Vuetify v-snackbar-queue component, see https://vuetifyjs.com/en/api/v-snackbar-queue/"""

    _model_name = Unicode("SnackbarQueueModel").tag(sync=True)

    absolute = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **position: absolute** to the content element.",
    ).tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.",
    ).tag(sync=True)

    closable = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a dismiss button that closes the active snackbar.",
    ).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only applies to hover and focus events.",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None, allow_none=True, help="Closes component when you click on its content."
    ).tag(sync=True)

    close_text = Unicode(
        default_value=None,
        allow_none=True,
        help="The text used in the close button when using the **closable** prop.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    multi_line = Bool(
        default_value=None,
        allow_none=True,
        help="Deprecated, use `min-height` instead. Increases minimum height.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only applies to hover and focus events.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is clicked.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is hovered.",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    timeout = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Time (in milliseconds) to wait until snackbar is automatically hidden.  Use `-1` to keep open indefinitely (`0` in version < 2.3 ). It is recommended for this number to be between `4000` and `10000`. Changes to this property will reset the timeout.",
    ).tag(sync=True)

    timer = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Display a progress bar that counts down until the snackbar closes. Pass a string to set a custom color, otherwise uses `info`.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    vertical = Bool(
        default_value=None,
        allow_none=True,
        help="Stacks snackbar content on top of the actions (button).",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class Spacer(VuetifyWidget):
    """Widget for the Vuetify v-spacer component, see https://vuetifyjs.com/en/api/v-spacer/"""

    _model_name = Unicode("SpacerModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class Sparkline(VuetifyWidget):
    """Widget for the Vuetify v-sparkline component, see https://vuetifyjs.com/en/api/v-sparkline/"""

    _model_name = Unicode("SparklineModel").tag(sync=True)

    auto_draw = Bool(
        default_value=None,
        allow_none=True,
        help="Trace the length of the line when first rendered.",
    ).tag(sync=True)

    auto_draw_duration = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Amount of time (in ms) to run the trace animation.",
    ).tag(sync=True)

    auto_draw_easing = Unicode(
        default_value=None,
        allow_none=True,
        help="The easing function to use for the trace animation.",
    ).tag(sync=True)

    auto_line_width = Bool(
        default_value=None,
        allow_none=True,
        help="Automatically expand bars to use space efficiently.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    fill = Bool(
        default_value=None,
        allow_none=True,
        help="Using the **fill** property allows you to better customize the look and feel of your sparkline.",
    ).tag(sync=True)

    gradient = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of colors to use as a linear-gradient.",
    ).tag(sync=True)

    gradient_direction = Unicode(
        default_value=None, allow_none=True, help="The direction the gradient should run."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Height of the SVG trendline or bars.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="The id of the component.").tag(
        sync=True
    )

    item_value = Unicode(default_value=None, allow_none=True, help="The value of the item.").tag(
        sync=True
    )

    label_size = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="The label font size."
    ).tag(sync=True)

    labels = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of string labels that correspond to the same index as its data counterpart.",
    ).tag(sync=True)

    line_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The thickness of the line, in px.",
    ).tag(sync=True)

    max = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The maximum value of the sparkline.",
    ).tag(sync=True)

    min = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The minimum value of the sparkline.",
    ).tag(sync=True)

    model_value = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    padding = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Low `smooth` or high `line-width` values may result in cropping, increase padding to compensate.",
    ).tag(sync=True)

    show_labels = Bool(
        default_value=None, allow_none=True, help="Show labels below each data point."
    ).tag(sync=True)

    smooth = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Number of px to use as a corner radius. `true` defaults to 8, `false` is 0.",
    ).tag(sync=True)

    type = Unicode(
        default_value=None, allow_none=True, help="Choose between a trendline or bars."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Width of the SVG trendline or bars.",
    ).tag(sync=True)


class SpeedDial(VuetifyWidget):
    """Widget for the Vuetify v-speed-dial component, see https://vuetifyjs.com/en/api/v-speed-dial/"""

    _model_name = Unicode("SpeedDialModel").tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.",
    ).tag(sync=True)

    capture_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before closing component. Only works with the **open-on-hover** prop.",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None, allow_none=True, help="Closes component when you click on its content."
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    disable_initial_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Deprecated, use `capture-focus` instead. Prevents automatic redirect of first `focusin` event. Intended to use on permanently open menus or VSpeedDial.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    id = Unicode(
        default_value=None, allow_none=True, help="The unique identifier of the component."
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    no_click_animation = Bool(
        default_value=None,
        allow_none=True,
        help="Disables the bounce effect when clicking outside of the content element when using the persistent prop.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Milliseconds to wait before opening component. Only works with the **open-on-hover** prop.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is clicked.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None, allow_none=True, help="Opens speed-dial on hover."
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    persistent = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking outside of the element or pressing esc key will not deactivate it.",
    ).tag(sync=True)

    retain_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Captures and keeps focus within the content element when using **Tab** and **Shift**+**Tab**. Recommended to be `false` when using external tools that require focus such as TinyMCE or vue-clipboard.",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    scroll_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Strategy used when the component is activate and user scrolls.",
    ).tag(sync=True)

    stick_to_target = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the overlay content to go off-screen when scrolling.",
    ).tag(sync=True)

    submenu = Bool(
        default_value=None,
        allow_none=True,
        help='Opens with right arrow and closes on left instead of up/down. Implies `location="end"`. Directions are reversed for RTL.',
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    viewport_margin = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom viewport margin for the overlay content",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class Stepper(VuetifyWidget):
    """Widget for the Vuetify v-stepper component, see https://vuetifyjs.com/en/api/v-stepper/"""

    _model_name = Unicode("StepperModel").tag(sync=True)

    alt_labels = Bool(
        default_value=None, allow_none=True, help="Places the labels beneath the step."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    complete_icon = Any(help="Icon to display when step is marked as completed.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    edit_icon = Any(help="Icon to display when step is editable.").tag(sync=True)

    editable = Bool(default_value=None, allow_none=True, help="Marks step as editable.").tag(
        sync=True
    )

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    error_icon = Any(help="Icon to display when step has an error.").tag(sync=True)

    flat = Bool(default_value=None, allow_none=True, help="Removes the stepper's elevation.").tag(
        sync=True
    )

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None, allow_none=True, help="Hide actions bar (prev and next buttons)."
    ).tag(sync=True)

    item_props = Unicode(
        default_value=None,
        allow_none=True,
        help="Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.",
    ).tag(sync=True)

    item_title = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its title.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the stepper into a mobile state, removing labels from stepper items.",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    next_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the Next button."
    ).tag(sync=True)

    non_linear = Bool(
        default_value=None, allow_none=True, help="Allow user to jump to any step."
    ).tag(sync=True)

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    prev_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the Prev button."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class StepperActions(VuetifyWidget):
    """Widget for the Vuetify v-stepper-actions component, see https://vuetifyjs.com/en/api/v-stepper-actions/"""

    _model_name = Unicode("StepperActionsModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Union(
        [Bool(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    next_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the Next button."
    ).tag(sync=True)

    prev_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the Prev button."
    ).tag(sync=True)


class StepperHeader(VuetifyWidget):
    """Widget for the Vuetify v-stepper-header component, see https://vuetifyjs.com/en/api/v-stepper-header/"""

    _model_name = Unicode("StepperHeaderModel").tag(sync=True)

    tag = Unicode(
        default_value=None, allow_none=True, help="Specify a custom tag used on the root element."
    ).tag(sync=True)


class StepperItem(VuetifyWidget):
    """Widget for the Vuetify v-stepper-item component, see https://vuetifyjs.com/en/api/v-stepper-item/"""

    _model_name = Unicode("StepperItemModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    complete = Bool(default_value=None, allow_none=True, help="Marks step as complete.").tag(
        sync=True
    )

    complete_icon = Any(help="Icon to display when step is marked as completed.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    edit_icon = Any(help="Icon to display when step is editable.").tag(sync=True)

    editable = Bool(default_value=None, allow_none=True, help="Marks step as editable.").tag(
        sync=True
    )

    error = Bool(
        default_value=None, allow_none=True, help="Puts the stepper item in a manual error state."
    ).tag(sync=True)

    error_icon = Any(help="Icon to display when step has an error.").tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    subtitle = Unicode(
        default_value=None, allow_none=True, help="Specify a subtitle text for the component."
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)


class StepperVertical(VuetifyWidget):
    """Widget for the Vuetify v-stepper-vertical component, see https://vuetifyjs.com/en/api/v-stepper-vertical/"""

    _model_name = Unicode("StepperVerticalModel").tag(sync=True)

    alt_labels = Bool(
        default_value=None, allow_none=True, help="Places the labels beneath the step."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    collapse_icon = Any(help="Icon used when the expansion panel is in a collapsable state.").tag(
        sync=True
    )

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    complete_icon = Any(help="Icon to display when step is marked as completed.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    edit_icon = Any(help="Icon to display when step is editable.").tag(sync=True)

    editable = Bool(default_value=None, allow_none=True, help="Marks step as editable.").tag(
        sync=True
    )

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    error_icon = Any(help="Icon to display when step has an error.").tag(sync=True)

    expand_icon = Any(help="Icon used when the expansion panel is in a expandable state.").tag(
        sync=True
    )

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the expansion-panel's elevation and borders.",
    ).tag(sync=True)

    focusable = Bool(
        default_value=None, allow_none=True, help="Makes the expansion-panel headers focusable."
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None, allow_none=True, help="Hide the expand icon in the content title."
    ).tag(sync=True)

    item_props = Unicode(
        default_value=None,
        allow_none=True,
        help="Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.",
    ).tag(sync=True)

    item_title = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its title.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of strings or objects used for automatically generating children components.",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Overrides the display configuration default screen size that the component should be considered in mobile.",
    ).tag(sync=True)

    model_value = Any(
        help="Controls expanded panel(s). Defaults to an empty array when using **multiple** prop. It is recommended to set unique `value` prop for the panels inside, otherwise index is used instead."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    next_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the Next button."
    ).tag(sync=True)

    non_linear = Bool(
        default_value=None, allow_none=True, help="Allow user to jump to any step."
    ).tag(sync=True)

    prev_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the Prev button."
    ).tag(sync=True)

    readonly = Bool(
        default_value=None, allow_none=True, help="Makes the entire expansion panel read only."
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(default_value=None, allow_none=True, help="Removes the border-radius.").tag(
        sync=True
    )

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class StepperVerticalActions(VuetifyWidget):
    """Widget for the Vuetify v-stepper-vertical-actions component, see https://vuetifyjs.com/en/api/v-stepper-vertical-actions/"""

    _model_name = Unicode("StepperVerticalActionsModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Union(
        [Bool(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    next_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the Next button."
    ).tag(sync=True)

    prev_text = Unicode(
        default_value=None, allow_none=True, help="The text used for the Prev button."
    ).tag(sync=True)


class StepperVerticalItem(VuetifyWidget):
    """Widget for the Vuetify v-stepper-vertical-item component, see https://vuetifyjs.com/en/api/v-stepper-vertical-item/"""

    _model_name = Unicode("StepperVerticalItemModel").tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    collapse_icon = Any(help="Icon used when the expansion panel is in a collapsable state.").tag(
        sync=True
    )

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    complete = Bool(default_value=None, allow_none=True, help="Marks step as complete.").tag(
        sync=True
    )

    complete_icon = Any(help="Icon to display when step is marked as completed.").tag(sync=True)

    disabled = Bool(
        default_value=None, allow_none=True, help="Disables the expansion-panel content."
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    edit_icon = Any(help="Icon to display when step is editable.").tag(sync=True)

    editable = Bool(default_value=None, allow_none=True, help="Marks step as editable.").tag(
        sync=True
    )

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the stepper item in a manual error state."
    ).tag(sync=True)

    error_icon = Any(help="Icon to display when step has an error.").tag(sync=True)

    expand_icon = Any(help="Icon used when the expansion panel is in a expandable state.").tag(
        sync=True
    )

    focusable = Bool(
        default_value=None, allow_none=True, help="Makes the expansion panel content focusable."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None, allow_none=True, help="Hide the expand icon in the content title."
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    readonly = Bool(
        default_value=None, allow_none=True, help="Makes the expansion panel content read only."
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    static = Bool(
        default_value=None, allow_none=True, help="Remove title size expansion when selected."
    ).tag(sync=True)

    subtitle = Unicode(
        default_value=None, allow_none=True, help="Specify a subtitle text for the component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    value = Any(help="Controls the opened/closed state of content.").tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class StepperWindow(VuetifyWidget):
    """Widget for the Vuetify v-stepper-window component, see https://vuetifyjs.com/en/api/v-stepper-window/"""

    _model_name = Unicode("StepperWindowModel").tag(sync=True)

    crossfade = Bool(default_value=None, allow_none=True, help="Enables crossfade transition.").tag(
        sync=True
    )

    direction = Unicode(
        default_value=None, allow_none=True, help="The transition direction when changing windows."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    reverse = Bool(
        default_value=None, allow_none=True, help="Reverse the normal transition direction."
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition_duration = Float(
        default_value=None,
        allow_none=True,
        help="Overrides transition duration. Does not work in firefox, safari <18, or with `prefers-reduced-motion: reduce`.",
    ).tag(sync=True)

    vertical_arrows = Union(
        [Bool(), Unicode(), Unicode()], default_value=None, allow_none=True
    ).tag(sync=True)


class StepperWindowItem(VuetifyWidget):
    """Widget for the Vuetify v-stepper-window-item component, see https://vuetifyjs.com/en/api/v-stepper-window-item/"""

    _model_name = Unicode("StepperWindowItemModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help='Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.',
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    reverse_transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the reverse transition.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="The transition used when the component progressing through items. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)


class SvgIcon(VuetifyWidget):
    """Widget for the Vuetify v-svg-icon component, see https://vuetifyjs.com/en/api/v-svg-icon/"""

    _model_name = Unicode("SvgIconModel").tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class Switch(VuetifyWidget):
    """Widget for the Vuetify v-switch component, see https://vuetifyjs.com/en/api/v-switch/"""

    _model_name = Unicode("SwitchModel").tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    defaults_target = Unicode(
        default_value=None,
        allow_none=True,
        help="The target component to provide defaults values for.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(
        default_value=None, allow_none=True, help="Changes the direction of the input."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    false_icon = Any(help="The icon used when inactive.").tag(sync=True)

    false_value = Any(help="Sets value for falsy state.").tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Display component without elevation. Default elevation for thumb is 4dp, `flat` resets it.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the input is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-switch/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    indeterminate = Bool(
        default_value=None, allow_none=True, help="Sets an indeterminate state for the switch."
    ).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True, help="Puts children inputs into a row.").tag(
        sync=True
    )

    inset = Bool(
        default_value=None,
        allow_none=True,
        help="Enlarge the `v-switch` track to encompass the thumb.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays circular progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - primary, secondary, success, info, warning, error) or a Boolean which uses the component color (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Changes expected model to an array."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-switch/#props-hint) to always be visible.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    true_icon = Any(help="The icon used when active.").tag(sync=True)

    true_value = Any(help="Sets value for truthy state.").tag(sync=True)

    type = Unicode(
        default_value=None,
        allow_none=True,
        help="Provides the default type for children selection controls.",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class SystemBar(VuetifyWidget):
    """Widget for the Vuetify v-system-bar component, see https://vuetifyjs.com/en/api/v-system-bar/"""

    _model_name = Unicode("SystemBarModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies **position: absolute** to the component."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Assign a specific name for layout registration."
    ).tag(sync=True)

    order = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Adjust the order of the component in relation to its registration order.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    window = Bool(
        default_value=None,
        allow_none=True,
        help="Increases the system bar height to 32px (24px default).",
    ).tag(sync=True)


class Tab(VuetifyWidget):
    """Widget for the Vuetify v-tab component, see https://vuetifyjs.com/en/api/v-tab/"""

    _model_name = Unicode("TabModel").tag(sync=True)

    active_color = Unicode(
        default_value=None,
        allow_none=True,
        help="The applied color when the component is in an active state.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the direction of the tabs. Can be either `horizontal` or `vertical`.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    fixed = Bool(
        default_value=None,
        allow_none=True,
        help="Forces component to take up all available space up to their maximum width (300px), and centers it.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_slider = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the active tab slider component (no exit or enter animation).",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon using the [v-icon](https://vuetifyjs.com/en/components/icons/) component. The button will become _round_."
    ).tag(sync=True)

    inset = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the slider to take full height. Automatically propagated from VTabs.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    readonly = Bool(
        default_value=None,
        allow_none=True,
        help="Puts the button in a readonly state. Cannot be clicked or navigated to by keyboard.",
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    slider_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the slider when active on that component - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    slider_transition = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes slider transition to one of the predefined animation presets.",
    ).tag(sync=True)

    slider_transition_duration = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Applies custom slider transition duration. Default duration depends on transition type (fade: 400, grow: 350, shift: 225).",
    ).tag(sync=True)

    slim = Bool(default_value=None, allow_none=True, help="Reduces padding to 0 8px.").tag(
        sync=True
    )

    spaced = Unicode(
        default_value=None,
        allow_none=True,
        help="Extends content to the edges to move main content from prepend and append slots.",
    ).tag(sync=True)

    stacked = Bool(
        default_value=None, allow_none=True, help="Displays the tab as a flex-column."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify content text for the component.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Table(VuetifyWidget):
    """Widget for the Vuetify v-table component, see https://vuetifyjs.com/en/api/v-table/"""

    _model_name = Unicode("TableModel").tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    fixed_footer = Bool(
        default_value=None,
        allow_none=True,
        help="Use the fixed-footer prop together with the height prop to fix the footer to the bottom of the table.",
    ).tag(sync=True)

    fixed_header = Bool(
        default_value=None,
        allow_none=True,
        help="Use the fixed-header prop together with the height prop to fix the header to the top of the table.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Use the height prop to set the height of the table.",
    ).tag(sync=True)

    hover = Bool(
        default_value=None,
        allow_none=True,
        help="Will add a hover effect to a table's row when the mouse is over it.",
    ).tag(sync=True)

    striped = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies a background to either **even** or **odd** rows.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)


class Tabs(VuetifyWidget):
    """Widget for the Vuetify v-tabs component, see https://vuetifyjs.com/en/api/v-tabs/"""

    _model_name = Unicode("TabsModel").tag(sync=True)

    align_tabs = Unicode(
        default_value=None,
        allow_none=True,
        help="Aligns the tabs to the `start`, `center`, or `end` of container. Also accepts `title` to align with the `v-toolbar-title` component.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_active = Bool(
        default_value=None, allow_none=True, help="Forces the selected tab to be centered."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the selected tab - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    content_class = Any(help="Adds classes to the slide group item.").tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the direction of the tabs. Can be either `horizontal` or `vertical`.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Puts all children components into a disabled state.",
    ).tag(sync=True)

    fixed_tabs = Bool(
        default_value=None,
        allow_none=True,
        help="Tabs will be centered and each tab item will grow up to 300px width.",
    ).tag(sync=True)

    grow = Bool(
        default_value=None, allow_none=True, help="Forces tabs to take up all available space."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height of the tabs bar.",
    ).tag(sync=True)

    hide_slider = Bool(
        default_value=None, allow_none=True, help="Hide's the generated `v-tabs-slider`."
    ).tag(sync=True)

    inset = Bool(
        default_value=None,
        allow_none=True,
        help="Changes the slider to take full height. Tabs will also get some spacing and customizable rounding.",
    ).tag(sync=True)

    inset_padding = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom spacing between tabs for `inset` mode.",
    ).tag(sync=True)

    inset_radius = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom border radius for the tabs container `inset` mode. Rounding for individual tabs is calculated by subtracting the padding.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="The items to display in the component. This can be an array of strings or objects with a property `text`.",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Sets a maximum number of selections that can be made.",
    ).tag(sync=True)

    mobile = Bool(
        default_value=None,
        allow_none=True,
        help="Determines the display mode of the component. If true, the component will be displayed in mobile mode. If false, the component will be displayed in desktop mode. If null, will be based on the current mobile-breakpoint",
    ).tag(sync=True)

    mobile_breakpoint = Union(
        [Float(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Sets the designated mobile breakpoint for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    multiple = Bool(
        default_value=None, allow_none=True, help="Allows one to select multiple items."
    ).tag(sync=True)

    next_icon = Any(help="Right pagination icon.").tag(sync=True)

    prev_icon = Any(help="Left pagination icon.").tag(sync=True)

    scroll_to_active = Bool(
        default_value=None,
        allow_none=True,
        help="Keeps the last active element visible when resizing the scrollable container.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    show_arrows = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Show pagination arrows if the tab items overflow their container. For mobile devices, arrows will only display when using this prop.",
    ).tag(sync=True)

    slider_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes the background color of an auto-generated `v-tabs-slider`.",
    ).tag(sync=True)

    slider_transition = Unicode(
        default_value=None,
        allow_none=True,
        help="Changes slider transition to one of the predefined animation presets.",
    ).tag(sync=True)

    slider_transition_duration = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Applies custom slider transition duration. Default duration depends on transition type (fade: 400, grow: 350, shift: 225).",
    ).tag(sync=True)

    spaced = Unicode(
        default_value=None,
        allow_none=True,
        help="Extends content to the edges to move main content from prepend and append slots.",
    ).tag(sync=True)

    stacked = Bool(
        default_value=None,
        allow_none=True,
        help="Apply the stacked prop to all children v-tab components.",
    ).tag(sync=True)

    symbol = Any(
        help="The [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) used to hook into group functionality for components like [v-btn-toggle](https://vuetifyjs.com/en/components/btn-toggle) and [v-bottom-navigation](https://vuetifyjs.com/en/components/bottom-navigations/)."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)


class TabsWindow(VuetifyWidget):
    """Widget for the Vuetify v-tabs-window component, see https://vuetifyjs.com/en/api/v-tabs-window/"""

    _model_name = Unicode("TabsWindowModel").tag(sync=True)

    crossfade = Bool(default_value=None, allow_none=True, help="Enables crossfade transition.").tag(
        sync=True
    )

    direction = Unicode(
        default_value=None, allow_none=True, help="The transition direction when changing windows."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    reverse = Bool(
        default_value=None, allow_none=True, help="Reverse the normal transition direction."
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition_duration = Float(
        default_value=None,
        allow_none=True,
        help="Overrides transition duration. Does not work in firefox, safari <18, or with `prefers-reduced-motion: reduce`.",
    ).tag(sync=True)

    vertical_arrows = Union(
        [Bool(), Unicode(), Unicode()], default_value=None, allow_none=True
    ).tag(sync=True)


class TabsWindowItem(VuetifyWidget):
    """Widget for the Vuetify v-tabs-window-item component, see https://vuetifyjs.com/en/api/v-tabs-window-item/"""

    _model_name = Unicode("TabsWindowItemModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help='Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.',
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    reverse_transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the reverse transition.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="The transition used when the component progressing through items. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)


class TextField(VuetifyWidget):
    """Widget for the Vuetify v-text-field component, see https://vuetifyjs.com/en/api/v-text-field/"""

    _model_name = Unicode("TextFieldModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True, help="Enables autofocus.").tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    clear_icon = Any(help="Applied when using **clearable** and the input is dirty.").tag(sync=True)

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Float(
        default_value=None, allow_none=True, help="Function returns the counter display text."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    dirty = Bool(
        default_value=None, allow_none=True, help="Manually apply the dirty state styling."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes elevation (shadow) added to element when using the **solo** or **solo-inverted** props.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-text-field/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-text-field/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input’s placeholder text."
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the outside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Prepends an icon inside the component's input, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the input orientation.").tag(
        sync=True
    )

    role = Unicode(
        default_value=None, allow_none=True, help="The role attribute applied to the input."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Adds a border radius to the input.",
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True, help="Sets input type.").tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Textarea(VuetifyWidget):
    """Widget for the Vuetify v-textarea component, see https://vuetifyjs.com/en/api/v-textarea/"""

    _model_name = Unicode("TextareaModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    append_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **append-inner** slot."
    ).tag(sync=True)

    auto_grow = Bool(
        default_value=None,
        allow_none=True,
        help="Automatically grow the textarea depending on amount of text.",
    ).tag(sync=True)

    autocomplete = Unicode(
        default_value=None,
        allow_none=True,
        help="Helps influence browser's suggestions. Special value **suppress** manipulates fields `name` attribute while **off** relies on browser's good will to stop suggesting values. Any other value is passed to the native `autocomplete` on the underlying element.",
    ).tag(sync=True)

    autofocus = Bool(
        default_value=None,
        allow_none=True,
        help="The element should be focused as soon as the page loads.",
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the color of the input when it is not focused.",
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    center_affix = Bool(
        default_value=None,
        allow_none=True,
        help="Vertically align **appendInner**, **prependInner**, **clearIcon** and **label** in the center.",
    ).tag(sync=True)

    clear_icon = Any(help="The icon used when the **clearable** prop is set to true.").tag(
        sync=True
    )

    clearable = Bool(
        default_value=None, allow_none=True, help="Allows for the component to be cleared."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    counter = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Creates counter for input length; if no number is specified, it defaults to 25. Does not apply any validation.",
    ).tag(sync=True)

    counter_value = Any(help="Display the input length but do not provide any validation.").tag(
        sync=True
    )

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    dirty = Bool(
        default_value=None, allow_none=True, help="Manually apply the dirty state styling."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the input.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    flat = Bool(
        default_value=None,
        allow_none=True,
        help="Removes box shadow when using a variant with elevation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    glow = Bool(
        default_value=None,
        allow_none=True,
        help="Makes prepend/append icons full opacity when the field is focused and apply color.",
    ).tag(sync=True)

    hide_details = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Hides hint and validation errors. When set to `auto` messages will be rendered only if there's a message (hint, error message, counter value etc) to display.",
    ).tag(sync=True)

    hide_spin_buttons = Bool(
        default_value=None,
        allow_none=True,
        help="Hides spin buttons on the input when type is set to `number`.",
    ).tag(sync=True)

    hint = Unicode(
        default_value=None,
        allow_none=True,
        help="Displays hint text below the input when focused. Force this always open with the [persistent-hint](https://vuetifyjs.com/en/api/v-textarea/#props-persistent-hint) property.",
    ).tag(sync=True)

    icon_color = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the color of the prepend/append icons.",
    ).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True, help="Sets the DOM id on the component.").tag(
        sync=True
    )

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    loading = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Displays linear progress bar. Can either be a String which specifies which color is applied to the progress bar (any material color or theme color - **primary**, **secondary**, **success**, **info**, **warning**, **error**) or a Boolean which uses the component **color** (set by color prop - if it's supported by the component) or the primary color.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Alternative for **max-rows**. Specifies the maximum height in pixels (including the field padding) for **auto-grow**.",
    ).tag(sync=True)

    max_rows = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Specifies the maximum number of rows for **auto-grow**.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Displays a list of messages or a single message if using a string.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_modifiers = Any(help="**FOR INTERNAL USE ONLY**").tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    no_resize = Bool(default_value=None, allow_none=True, help="Remove resize handle.").tag(
        sync=True
    )

    persistent_clear = Bool(
        default_value=None,
        allow_none=True,
        help="Always show the clearable icon when the input is dirty (By default it only shows on hover).",
    ).tag(sync=True)

    persistent_counter = Bool(
        default_value=None, allow_none=True, help="Forces counter to always be visible."
    ).tag(sync=True)

    persistent_hint = Bool(
        default_value=None,
        allow_none=True,
        help="Forces [hint](https://vuetifyjs.com/en/api/v-textarea/#props-hint) to always be visible.",
    ).tag(sync=True)

    persistent_placeholder = Bool(
        default_value=None, allow_none=True, help="Forces placeholder to always be visible."
    ).tag(sync=True)

    placeholder = Unicode(
        default_value=None, allow_none=True, help="Sets the input's placeholder text."
    ).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True, help="Displays prefix text.").tag(
        sync=True
    )

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    prepend_inner_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend-inner** slot."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    reverse = Bool(default_value=None, allow_none=True, help="Reverses the orientation.").tag(
        sync=True
    )

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    rows = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Default row count."
    ).tag(sync=True)

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    single_line = Bool(
        default_value=None, allow_none=True, help="Label does not move on focus/dirty."
    ).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True, help="Displays suffix text.").tag(
        sync=True
    )

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class ThemeProvider(VuetifyWidget):
    """Widget for the Vuetify v-theme-provider component, see https://vuetifyjs.com/en/api/v-theme-provider/"""

    _model_name = Unicode("ThemeProviderModel").tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    with_background = Bool(
        default_value=None,
        allow_none=True,
        help="Wraps its children in an element and applies the current theme's background color to it.",
    ).tag(sync=True)


class TimePicker(VuetifyWidget):
    """Widget for the Vuetify v-time-picker component, see https://vuetifyjs.com/en/api/v-time-picker/"""

    _model_name = Unicode("TimePickerModel").tag(sync=True)

    allowed_hours = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which hours can be selected."
    ).tag(sync=True)

    allowed_minutes = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which minutes can be selected."
    ).tag(sync=True)

    allowed_seconds = TList(
        Any(), default_value=None, allow_none=True, help="Restricts which seconds can be selected."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    divided = Bool(
        default_value=None, allow_none=True, help="Adds a divider between the header and controls."
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    format = Unicode(
        default_value=None,
        allow_none=True,
        help="Defines the format of a time displayed in picker. Available options are `ampm` and `24hr`.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_header = Bool(default_value=None, allow_none=True, help="Hide the picker header.").tag(
        sync=True
    )

    hide_title = Bool(default_value=None, allow_none=True, help="Hide the picker title.").tag(
        sync=True
    )

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string."
    ).tag(sync=True)

    max = Unicode(default_value=None, allow_none=True, help="Maximum allowed time.").tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min = Unicode(default_value=None, allow_none=True, help="Minimum allowed time.").tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    period = Unicode(default_value=None, allow_none=True, help="Sets period for 12hr format.").tag(
        sync=True
    )

    position = Unicode(
        default_value=None, allow_none=True, help="Sets the position for the component."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts picker in readonly state.").tag(
        sync=True
    )

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    scrollable = Bool(
        default_value=None, allow_none=True, help="Allows changing hour/minute with mouse scroll."
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    use_seconds = Bool(
        default_value=None, allow_none=True, help="Toggles the use of seconds in picker."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    view_mode = Unicode(
        default_value=None, allow_none=True, help="The current view mode of the picker."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Width of the picker."
    ).tag(sync=True)


class TimePickerClock(VuetifyWidget):
    """Widget for the Vuetify v-time-picker-clock component, see https://vuetifyjs.com/en/api/v-time-picker-clock/"""

    _model_name = Unicode("TimePickerClockModel").tag(sync=True)

    allowed_values = Any(help="Restricts which hours can be selected.").tag(sync=True)

    ampm = Bool(default_value=None, allow_none=True, help="Displays time in a 12-hour format.").tag(
        sync=True
    )

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    displayed_value = Any(help="Used to display a custom value on the clock.").tag(sync=True)

    double = Bool(
        default_value=None,
        allow_none=True,
        help="If set, this probably indicates a double rotation or a mode where more than one set of values (like hours and minutes) is displayed on the clock at the same time.",
    ).tag(sync=True)

    format = Any(
        help="Specifies the format of the displayed time, either 12-hour or 24-hour, depending on the component's setup."
    ).tag(sync=True)

    max = Float(
        default_value=None,
        allow_none=True,
        help="Defines the maximum time value that can be selected.",
    ).tag(sync=True)

    min = Float(
        default_value=None,
        allow_none=True,
        help="Defines the minimum time value that can be selected.",
    ).tag(sync=True)

    model_value = Float(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    readonly = Bool(
        default_value=None,
        allow_none=True,
        help="When true, the picker is in a read-only state, and users cannot modify the selected time.",
    ).tag(sync=True)

    rotate = Float(
        default_value=None,
        allow_none=True,
        help="Controls rotation, specifying the degree of rotation for the clock hands.",
    ).tag(sync=True)

    scrollable = Bool(
        default_value=None,
        allow_none=True,
        help="Allows the time selection to be scrollable, enhancing user experience for devices with scroll inputs.",
    ).tag(sync=True)

    step = Float(
        default_value=None,
        allow_none=True,
        help="Defines the increments between selectable times, such as a step of 1 for every minute or a larger step for every 5 or 15 minutes.",
    ).tag(sync=True)


class TimePickerControls(VuetifyWidget):
    """Widget for the Vuetify v-time-picker-controls component, see https://vuetifyjs.com/en/api/v-time-picker-controls/"""

    _model_name = Unicode("TimePickerControlsModel").tag(sync=True)

    allowed_hours = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    allowed_minutes = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    allowed_seconds = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    ampm = Bool(default_value=None, allow_none=True, help="Enables AM/PM mode.").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    hour = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="The current hour value."
    ).tag(sync=True)

    input_hints = Bool(default_value=None, allow_none=True).tag(sync=True)

    max = Unicode(default_value=None, allow_none=True).tag(sync=True)

    min = Unicode(default_value=None, allow_none=True).tag(sync=True)

    minute = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="The current minute value."
    ).tag(sync=True)

    period = Unicode(
        default_value=None, allow_none=True, help="The current period value. either `am` or `pm`."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Makes the timepicker readonly.").tag(
        sync=True
    )

    second = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="The current second value."
    ).tag(sync=True)

    use_seconds = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the display and selection of seconds in the timepicker.",
    ).tag(sync=True)

    value = Float(
        default_value=None, allow_none=True, help="The current value of the timepicker."
    ).tag(sync=True)

    view_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="The current view mode of the timepicker. Can be either `hour`, `minute`, or `second`.",
    ).tag(sync=True)


class Timeline(VuetifyWidget):
    """Widget for the Vuetify v-timeline component, see https://vuetifyjs.com/en/api/v-timeline/"""

    _model_name = Unicode("TimelineModel").tag(sync=True)

    align = Unicode(
        default_value=None,
        allow_none=True,
        help="Places the timeline dot at the top or center of the timeline item.",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    direction = Unicode(
        default_value=None,
        allow_none=True,
        help="Display timeline in a **vertical** or **horizontal** direction.",
    ).tag(sync=True)

    dot_color = Unicode(default_value=None, allow_none=True, help="Color of the item dot.").tag(
        sync=True
    )

    fill_dot = Bool(
        default_value=None,
        allow_none=True,
        help="Remove outer border of item dot, making the color fill the entire dot.",
    ).tag(sync=True)

    hide_opposite = Bool(
        default_value=None, allow_none=True, help="Hide opposite content if it exists."
    ).tag(sync=True)

    icon_color = Unicode(default_value=None, allow_none=True, help="Color of the icon.").tag(
        sync=True
    )

    justify = Unicode(
        default_value=None,
        allow_none=True,
        help="Places timeline line at the center or automatically on the left or right side.",
    ).tag(sync=True)

    line_color = Unicode(
        default_value=None, allow_none=True, help="Color of the timeline line."
    ).tag(sync=True)

    line_inset = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Specifies the distance between the line and the dot of timeline items.",
    ).tag(sync=True)

    line_thickness = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Thickness of the timeline line.",
    ).tag(sync=True)

    side = Unicode(
        default_value=None,
        allow_none=True,
        help="Display all timeline items on one side of the timeline, either **start** or **end**.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height and width of the component. Default unit is px. Can also use the following predefined sizes: **x-small**, **small**, **default**, **large**, and **x-large**.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    truncate_line = Unicode(
        default_value=None,
        allow_none=True,
        help="Truncate timeline directly at the **start** or **end** of the line, or on **both** ends.",
    ).tag(sync=True)


class TimelineItem(VuetifyWidget):
    """Widget for the Vuetify v-timeline-item component, see https://vuetifyjs.com/en/api/v-timeline-item/"""

    _model_name = Unicode("TimelineItemModel").tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    dot_color = Unicode(default_value=None, allow_none=True, help="Color of the item dot.").tag(
        sync=True
    )

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    fill_dot = Bool(
        default_value=None,
        allow_none=True,
        help="Remove outer border of item dot, making the color fill the entire dot.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_dot = Bool(default_value=None, allow_none=True, help="Hide the timeline item dot.").tag(
        sync=True
    )

    hide_opposite = Bool(
        default_value=None, allow_none=True, help="Hide opposite content if it exists."
    ).tag(sync=True)

    icon = Any(
        help="Apply a specific icon to the inside dot using the [v-icon](https://vuetifyjs.com/en/components/icons/) component."
    ).tag(sync=True)

    icon_color = Unicode(default_value=None, allow_none=True, help="Color of the icon.").tag(
        sync=True
    )

    line_inset = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Specifies the distance between the line and the dot of the item.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    side = Unicode(
        default_value=None,
        allow_none=True,
        help="Show the item either **before** or **after** the timeline. This will override the implicit ordering of items, but will in turn be overridden by the `v-timeline` **single-side** prop.",
    ).tag(sync=True)

    size = Union(
        [Unicode(), Float()], default_value=None, allow_none=True, help="Size of the item dot"
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Toolbar(VuetifyWidget):
    """Widget for the Vuetify v-toolbar component, see https://vuetifyjs.com/en/api/v-toolbar/"""

    _model_name = Unicode("ToolbarModel").tag(sync=True)

    absolute = Bool(
        default_value=None, allow_none=True, help="Applies position: absolute to the component."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    collapse = Bool(
        default_value=None,
        allow_none=True,
        help="Puts the toolbar into a collapsed state reducing its maximum width.",
    ).tag(sync=True)

    collapse_position = Unicode(
        default_value=None, allow_none=True, help="Specifies side to attach the collapsed toolbar."
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    extended = Bool(
        default_value=None,
        allow_none=True,
        help="Use this prop to increase the height of the toolbar _without_ using the `extension` slot for adding content. May be used in conjunction with the **extension-height** prop. When false, will not show extension slot even if content is present.",
    ).tag(sync=True)

    extension_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Specify an explicit height for the `extension` slot.",
    ).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True, help="Removes the toolbar's box-shadow.").tag(
        sync=True
    )

    floating = Bool(
        default_value=None,
        allow_none=True,
        help="Applies **display: inline-flex** to the component.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates a specific height for the toolbar. Overrides the heights imposed by other props, e.g. **prominent**, **dense**, **extended**, etc.",
    ).tag(sync=True)

    image = Unicode(
        default_value=None,
        allow_none=True,
        help="Specifies a [v-img](https://vuetifyjs.com/en/components/images) as the component's background.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the component's location. Can combine by using a space separated string. Requires the **absolute** prop."
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)


class ToolbarItems(VuetifyWidget):
    """Widget for the Vuetify v-toolbar-items component, see https://vuetifyjs.com/en/api/v-toolbar-items/"""

    _model_name = Unicode("ToolbarItemsModel").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)


class ToolbarTitle(VuetifyWidget):
    """Widget for the Vuetify v-toolbar-title component, see https://vuetifyjs.com/en/api/v-toolbar-title/"""

    _model_name = Unicode("ToolbarTitleModel").tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)


class Tooltip(VuetifyWidget):
    """Widget for the Vuetify v-tooltip component, see https://vuetifyjs.com/en/api/v-tooltip/"""

    _model_name = Unicode("TooltipModel").tag(sync=True)

    activator = Unicode(
        default_value=None, allow_none=True, help="Explicitly sets the overlay's activator."
    ).tag(sync=True)

    activator_props = Any(help="Apply custom properties to the activator.").tag(sync=True)

    attach = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specifies which DOM element the overlay content should teleport to. Can be a direct element reference, querySelector string, or `true` to disable teleporting. Uses `body` by default.",
    ).tag(sync=True)

    close_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Delay (in ms) after which menu closes (when open-on-hover prop is set to true).",
    ).tag(sync=True)

    close_on_back = Bool(
        default_value=None,
        allow_none=True,
        help="Closes the overlay content when the browser's back button is pressed or `$router.back()` is called, cancelling the original navigation. `persistent` overlays will cancel navigation and animate as if they were clicked outside instead of closing.",
    ).tag(sync=True)

    close_on_content_click = Bool(
        default_value=None, allow_none=True, help="Closes component when you click on its content."
    ).tag(sync=True)

    contained = Bool(
        default_value=None,
        allow_none=True,
        help="Limits the size of the component and scrim to its offset parent. Implies `absolute` and `attach`. (Note: The parent element must have position: relative.).",
    ).tag(sync=True)

    content_class = Any(
        help="Applies a custom class to the detached element. This is useful because the content is moved to the beginning of the `v-app` component (unless the **attach** prop is provided) and is not targetable by classes passed directly on the component."
    ).tag(sync=True)

    content_props = Any(help="Apply custom properties to the content.").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    id = Unicode(
        default_value=None,
        allow_none=True,
        help="HTML id attribute of the tooltip overlay. If not set, a globally unique id will be used.",
    ).tag(sync=True)

    interactive = Bool(
        default_value=None,
        allow_none=True,
        help="When true, the tooltip will respond to pointer events, allowing you to copy text from it.",
    ).tag(sync=True)

    location = Any(
        help="Specifies the anchor point for positioning the component, using directional cues to align it either horizontally, vertically, or both.."
    ).tag(sync=True)

    location_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="A function used to specifies how the component should position relative to its activator.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Bool(
        default_value=None,
        allow_none=True,
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array.",
    ).tag(sync=True)

    no_click_animation = Bool(
        default_value=None,
        allow_none=True,
        help="Disables the bounce effect when clicking outside of the content element when using the persistent prop.",
    ).tag(sync=True)

    offset = Union(
        [Unicode(), Float(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Increases distance from the target. When passed as a pair of numbers, the second value shifts anchor along the side and away from the target.",
    ).tag(sync=True)

    opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the opacity of the scrim element. Only applies if `scrim` is enabled.",
    ).tag(sync=True)

    open_delay = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Delay (in ms) after which tooltip opens (when `open-on-hover` prop is set to **true**).",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether the tooltip should open on activator click.",
    ).tag(sync=True)

    open_on_focus = Bool(
        default_value=None,
        allow_none=True,
        help="Activate the component when the activator is focused.",
    ).tag(sync=True)

    open_on_hover = Bool(
        default_value=None,
        allow_none=True,
        help="Designates whether the tooltip should open on activator hover.",
    ).tag(sync=True)

    origin = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the transition origin on the element. You can find more information on the MDN documentation [for transition origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin).",
    ).tag(sync=True)

    persistent = Bool(
        default_value=None,
        allow_none=True,
        help="Clicking outside of the element or pressing esc key will not deactivate it.",
    ).tag(sync=True)

    scrim = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Accepts true/false to enable background, and string to define color.",
    ).tag(sync=True)

    scroll_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Strategy used when the component is activate and user scrolls.",
    ).tag(sync=True)

    stick_to_target = Bool(
        default_value=None,
        allow_none=True,
        help="Enables the overlay content to go off-screen when scrolling.",
    ).tag(sync=True)

    target = Unicode(
        default_value=None,
        allow_none=True,
        help='For locationStrategy="connected", specify an element or array of x,y coordinates that the overlay should position itself relative to. This will be the activator element by default.',
    ).tag(sync=True)

    text = Unicode(
        default_value=None, allow_none=True, help="Specify content text for the component."
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the component transition. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    viewport_margin = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets custom viewport margin for the overlay content",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)

    z_index = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="The z-index used for the component.",
    ).tag(sync=True)


class Treeview(VuetifyWidget):
    """Widget for the Vuetify v-treeview component, see https://vuetifyjs.com/en/api/v-treeview/"""

    _model_name = Unicode("TreeviewModel").tag(sync=True)

    activatable = Bool(
        default_value=None,
        allow_none=True,
        help="Allows user to mark a node as active by clicking on it.",
    ).tag(sync=True)

    activated = Any(help="Array of ids of activated nodes.").tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it is in an active state.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None, allow_none=True, help="Deprecated, use `color` instead."
    ).tag(sync=True)

    active_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Affects how items with children behave when activated. If not specified, the **single-independent** strategy will be used.\n- **leaf:** Only leaf nodes (items without children) can be activated.\n- **single-leaf:** Similar as **leaf**, but only a single item can be activated at a time.\n- **independent:** All nodes can be activated whether they have children or not.\n- **single-independent:** Similar as **independent**, but only a single item can be activated at a time.",
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    bg_color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control's background. Used on components that also support the **color** prop. - supports utility colors with or without `bg-` prefix (for example `success`, `purple` or `bg-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    collapse_icon = Any(help="Icon to display when the list item is expanded.").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the active node - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    custom_filter = Any(
        help="Function used to filter items, called for each filterable key on each item in the list. The first argument is the filterable value from the item, the second is the search term, and the third is the internal item object. The function should return true if the item should be included in the filtered list, or the index of the match in the value if it should be included with the result highlighted."
    ).tag(sync=True)

    custom_key_filter = Any(
        help="Function used on specific keys within the item object. `customFilter` is skipped for columns with `customKeyFilter` specified."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None, allow_none=True, help="Disables selection for all nodes."
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    expand_icon = Any(help="Icon used to indicate that a node can be expanded.").tag(sync=True)

    false_icon = Any(help="The icon used when inactive.").tag(sync=True)

    filter_keys = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Array of specific keys to filter on the item.",
    ).tag(sync=True)

    filter_mode = Unicode(
        default_value=None,
        allow_none=True,
        help="Controls how the results of `customFilter` and `customKeyFilter` are combined. All modes only apply `customFilter` to columns not specified in `customKeyFilter`.\n\n- **some**: There is at least one match from either the custom filter or the custom key filter.\n- **every**: All columns match either the custom filter or the custom key filter.\n- **union**: There is at least one match from the custom filter, or all columns match the custom key filters.\n- **intersection**: There is at least one match from the custom filter, and all columns match the custom key filters.",
    ).tag(sync=True)

    filterable = Bool(
        default_value=None,
        allow_none=True,
        help="**FOR INTERNAL USE ONLY** Prevents list item selection using [space] key and pass it back to the text input. Used internally for VAutocomplete and VCombobox.",
    ).tag(sync=True)

    fluid = Bool(
        default_value=None, allow_none=True, help="Removes indentation from nested items."
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None,
        allow_none=True,
        help="Hide the expand icon and loading indicator next to each item title.",
    ).tag(sync=True)

    hide_no_data = Bool(
        default_value=None,
        allow_none=True,
        help="Hides the menu when there are no options to show.  Useful for preventing the menu from opening before results are fetched asynchronously.  Also has the effect of opening the menu when the `items` array changes if not already open.",
    ).tag(sync=True)

    indent = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Overrides the indent size for nested groups.",
    ).tag(sync=True)

    indent_lines = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Controls visibility and variant of the indent lines.",
    ).tag(sync=True)

    indent_lines_color = Unicode(
        default_value=None, allow_none=True, help="Sets color of indent lines"
    ).tag(sync=True)

    indent_lines_opacity = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets opacity of indent lines",
    ).tag(sync=True)

    indeterminate_icon = Any(
        help="Icon used when node is in an indeterminate state. Only visible when `selectable` is `true`."
    ).tag(sync=True)

    item_children = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its children.",
    ).tag(sync=True)

    item_props = Unicode(
        default_value=None,
        allow_none=True,
        help="Props object that will be applied to each item component. `true` will treat the original object as raw props and pass it directly to the component.",
    ).tag(sync=True)

    item_title = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its title.",
    ).tag(sync=True)

    item_type = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the key on the supplied items that is used for determining the nodes type.",
    ).tag(sync=True)

    item_value = Unicode(
        default_value=None,
        allow_none=True,
        help="Property on supplied `items` that contains its value.",
    ).tag(sync=True)

    items = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="An array of items used to build the treeview.",
    ).tag(sync=True)

    items_registration = Unicode(
        default_value=None,
        allow_none=True,
        help="When set to 'props', skips rendering collapsed items/nodes (for significant performance gains).",
    ).tag(sync=True)

    lines = Union(
        [Bool(), Unicode(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Designates a **minimum-height** for all children `v-list-item` components. This prop uses [line-clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-line-clamp) and is not supported in all browsers.",
    ).tag(sync=True)

    load_children = Any(
        help="A function used when dynamically loading children. If this prop is set, then the supplied function will be run if expanding an item that has a `item-children` property that is an empty array. Supports returning a Promise."
    ).tag(sync=True)

    loading_icon = Unicode(
        default_value=None, allow_none=True, help="Icon used when node is in a loading state."
    ).tag(sync=True)

    mandatory = Bool(
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    model_value = Any(
        help="Allows one to control which nodes are selected. The array contains the values of currently selected items. It is equivalent to the `v-model:selected`"
    ).tag(sync=True)

    navigation_index = Float(
        default_value=None,
        allow_none=True,
        help='Specifies the currently selected navigation index when using `navigationStrategy="track"`. Can be used with `v-model:navigationIndex` for two-way binding. Items at this index receive visual keyboard focus styling and automatic scrolling. Note: Only works with the `items` prop, not with slotted items.',
    ).tag(sync=True)

    navigation_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help='Determines keyboard navigation behavior. **focus** (default) moves DOM focus to items, suitable for traditional lists. **track** provides visual keyboard focus without moving DOM focus, ideal for command palettes and autocomplete where an external element retains focus. When track mode is active, items automatically receive `tabindex="-1"`, proper `aria-activedescendant` is set on the list container, and keyboard-focused items display focus-visible styling with auto-scrolling.',
    ).tag(sync=True)

    no_data_text = Unicode(
        default_value=None,
        allow_none=True,
        help="Text shown when no items are provided to the component.",
    ).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True, help="Disables all item filtering.").tag(
        sync=True
    )

    open_all = Bool(
        default_value=None,
        allow_none=True,
        help="When `true` will cause all branch nodes to be opened when component is mounted.",
    ).tag(sync=True)

    open_on_click = Bool(
        default_value=None,
        allow_none=True,
        help="When `true` will cause nodes to be opened by clicking anywhere on it, instead of only opening by clicking on expand icon. When using this prop with `activatable` you will be unable to mark nodes with children as active.",
    ).tag(sync=True)

    opened = Any(
        help="An array containing the values of currently opened groups. Can be two-way bound with `v-model:opened`."
    ).tag(sync=True)

    prepend_gap = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the horizontal spacing between prepend slot and the main content within list item. Also affects indent to ensure expected alignment of group children.",
    ).tag(sync=True)

    return_object = Bool(
        default_value=None,
        allow_none=True,
        help="When `true` will make `v-model`, `v-model:selected`, `v-model:activated` and `v-model:opened` return the complete object instead of just the key.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Provides an alternative active style for `v-treeview` node. Only visible when `activatable` is `true` and should not be used in conjunction with the `shaped` prop.",
    ).tag(sync=True)

    search = Unicode(
        default_value=None, allow_none=True, help="The search model for filtering results."
    ).tag(sync=True)

    select_strategy = Unicode(
        default_value=None,
        allow_none=True,
        help="Affects how items with children behave when selected.\n- **leaf:** Only leaf nodes (items without children) can be selected.\n- **independent:** All nodes can be selected whether they have children or not.\n- **classic:** Selecting a parent node will cause all children to be selected, parent nodes will be displayed as selected if all their descendants are selected. Only leaf nodes will be added to the model.\n- **trunk**: Same as classic but if all of a node's children are selected then only that node will be added to the model.\n- **branch**: Same as classic but if any of a node's children are selected then that node will also be added to the model.",
    ).tag(sync=True)

    selectable = Bool(
        default_value=None,
        allow_none=True,
        help="Will render a checkbox next to each node allowing them to be selected. Additionally, the **[openOnClick](https://vuetifyjs.com/en/api/v-treeview/#props-open-on-click)** property will be applied internally.",
    ).tag(sync=True)

    selected = Any(
        help="An array containing the values of currently selected items. Can be two-way bound with `v-model:selected`."
    ).tag(sync=True)

    selected_color = Unicode(
        default_value=None, allow_none=True, help="The color of the selection checkbox."
    ).tag(sync=True)

    separate_roots = Bool(
        default_value=None,
        allow_none=True,
        help="Applies to `default` variant of `indent-lines`. Prevents showing lines between root-level nodes.",
    ).tag(sync=True)

    slim = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces horizontal spacing for badges, icons, tooltips, and avatars within slim list items to create a more compact visual representation.",
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    true_icon = Any(help="The icon used when active.").tag(sync=True)

    value_comparator = Any(
        help="Apply a custom comparison algorithm to compare **model-value** and values contains in the **items** prop."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class TreeviewGroup(VuetifyWidget):
    """Widget for the Vuetify v-treeview-group component, see https://vuetifyjs.com/en/api/v-treeview-group/"""

    _model_name = Unicode("TreeviewGroupModel").tag(sync=True)

    active_color = Unicode(
        default_value=None, allow_none=True, help="Deprecated, use `color` instead."
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    collapse_icon = Any(help="Icon to display when the list item is expanded.").tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control - supports utility colors with or without `text-` prefix (for example `success`, `purple` or `text-purple`) or CSS color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors).",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None, allow_none=True, help="Puts all children inputs into a disabled state."
    ).tag(sync=True)

    expand_icon = Any(help="Icon to display when the list item is collapsed.").tag(sync=True)

    fluid = Bool(
        default_value=None, allow_none=True, help="Removes indentation from nested items."
    ).tag(sync=True)

    prepend_icon = Any(
        help="Prepends an icon to the component, uses the same syntax as `v-icon`."
    ).tag(sync=True)

    raw_id = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help='Defines the root element\'s id attribute in the component. If it is provided, the id attribute will be dynamically generated in the format: "v-list-group--id-[rawId]".',
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    title = Unicode(
        default_value=None, allow_none=True, help="Specify a title text for the component."
    ).tag(sync=True)

    value = Any(help="Expands / Collapse the list-group.").tag(sync=True)


class TreeviewItem(VuetifyWidget):
    """Widget for the Vuetify v-treeview-item component, see https://vuetifyjs.com/en/api/v-treeview-item/"""

    _model_name = Unicode("TreeviewItemModel").tag(sync=True)

    active = Bool(
        default_value=None,
        allow_none=True,
        help="Controls the **active** state of the item. This is typically used to highlight the component.",
    ).tag(sync=True)

    active_class = Unicode(
        default_value=None,
        allow_none=True,
        help="The class applied to the component when it matches the current route. Find more information about the [active-class prop](https://router.vuejs.org/api/#active-class) on the [vue-router](https://router.vuejs.org/) documentation.",
    ).tag(sync=True)

    active_color = Unicode(
        default_value=None, allow_none=True, help="Deprecated, use `color` instead."
    ).tag(sync=True)

    append_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Appends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component after default content in the **append** slot.",
    ).tag(sync=True)

    append_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component after default content in the **append** slot."
    ).tag(sync=True)

    base_color = Unicode(
        default_value=None, allow_none=True, help="Sets the color of component when not focused."
    ).tag(sync=True)

    border = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help='Applies utility border classes to the component. To use it, you need to omit the `border-` prefix, (for example use `border-sm` as `border="sm"`).  Find a list of the built-in border classes on the [borders page](https://vuetifyjs.com/en/styles/borders).',
    ).tag(sync=True)

    color = Unicode(
        default_value=None,
        allow_none=True,
        help="Applies specified color to the control when in an **active** state or **input-value** is **true** - supports utility colors (for example `success` or `purple`) or css color (`#033` or `rgba(255, 0, 0, 0.5)`). Find a list of built-in classes on the [colors page](https://vuetifyjs.com/en/styles/colors#material-colors),",
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    exact = Bool(
        default_value=None,
        allow_none=True,
        help="Exactly match the link. Without this, '/' will match every route. You can find more information about the [**exact** prop](https://router.vuejs.org/api/#exact) on the vue-router documentation.",
    ).tag(sync=True)

    has_custom_prepend = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_actions = Bool(
        default_value=None,
        allow_none=True,
        help="Hide the expand icon and loading indicator next to each item title.",
    ).tag(sync=True)

    href = Unicode(
        default_value=None,
        allow_none=True,
        help="Designates the component as anchor and applies the **href** attribute.",
    ).tag(sync=True)

    indent_lines = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Array of indent lines to render next to the item.",
    ).tag(sync=True)

    index = Float(default_value=None, allow_none=True).tag(sync=True)

    lines = Union(
        [Bool(), Unicode(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
        help="The line declaration specifies the minimum height of the item and can also be controlled from v-list with the same prop.",
    ).tag(sync=True)

    link = Bool(
        default_value=None,
        allow_none=True,
        help="Designates that the component is a link. This is automatic when using the href or to prop.",
    ).tag(sync=True)

    loading = Bool(
        default_value=None, allow_none=True, help="Places the v-treeview-item into a loading state."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    nav = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces the width of v-list-item takes and adds a border radius.",
    ).tag(sync=True)

    prepend_avatar = Unicode(
        default_value=None,
        allow_none=True,
        help="Prepends a [v-avatar](https://vuetifyjs.com/en/components/avatars/) component in the **prepend** slot before default content.",
    ).tag(sync=True)

    prepend_gap = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Any(
        help="Creates a [v-icon](https://vuetifyjs.com/en/api/v-icon/) component in the **prepend** slot before default content."
    ).tag(sync=True)

    replace = Bool(
        default_value=None,
        allow_none=True,
        help="Setting **replace** prop will call `router.replace()` instead of `router.push()` when clicked, so the navigation will not leave a history record. You can find more information about the [replace](https://router.vuejs.org/api/#replace) prop on the vue-router documentation.",
    ).tag(sync=True)

    ripple = Union(
        [Bool(), Dict()],
        default_value=None,
        allow_none=True,
        help="Applies the [v-ripple](https://vuetifyjs.com/en/directives/ripple) directive.",
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Designates the **border-radius** applied to the component. This can be **0**, **xs**, **sm**, true, **lg**, **xl**, **pill**, **circle**, and **shaped**. Find more information on available border radius classes on the [Border Radius page](https://vuetifyjs.com/en/styles/border-radius).",
    ).tag(sync=True)

    slim = Bool(
        default_value=None,
        allow_none=True,
        help="Reduces the vertical padding or height of the v-treeview-item, making it more compact.",
    ).tag(sync=True)

    subtitle = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Specify a subtitle text for the component.",
    ).tag(sync=True)

    tabindex = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help='Controls the tabindex of the list item. When set, overrides the default tabindex behavior. Automatically set to -1 by VList when using `navigationStrategy="track"` to prevent Tab key navigation into items.',
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    tile = Bool(
        default_value=None,
        allow_none=True,
        help="Removes any applied **border-radius** from the component.",
    ).tag(sync=True)

    title = Union(
        [Unicode(), Float(), Bool()],
        default_value=None,
        allow_none=True,
        help="Generates a `v-list-item-title` component with the supplied value. Note that this overrides the native [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title) attribute, that must be set with `v-bind:title.attr` instead.",
    ).tag(sync=True)

    to = Any(
        help="Denotes the target route of the link. You can find more information about the [**to** prop](https://router.vuejs.org/api/#to) on the vue-router documentation."
    ).tag(sync=True)

    toggle_icon = Any(
        help="Allows customization of the icon used to toggle the expansion and collapse of treeview branches."
    ).tag(sync=True)

    value = Any(
        help="The value used for selection. Obtained from [`v-list`](https://vuetifyjs.com/en/api/v-list)'s `v-model:selected` when the item is selected."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Validation(VuetifyWidget):
    """Widget for the Vuetify v-validation component, see https://vuetifyjs.com/en/api/v-validation/"""

    _model_name = Unicode("ValidationModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    error = Bool(
        default_value=None, allow_none=True, help="Puts the input in a manual error state."
    ).tag(sync=True)

    error_messages = Union(
        [Unicode(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Puts the input in an error state and passes through custom error messages. Will be combined with any validations that occur from the **rules** prop. This field will not trigger validation.",
    ).tag(sync=True)

    focused = Bool(
        default_value=None, allow_none=True, help="Forces a focused state styling on the component."
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Sets the text of the [v-label](https://vuetifyjs.com/en/api/v-label/) or [v-field-label](https://vuetifyjs.com/en/api/v-field-label/) component.",
    ).tag(sync=True)

    max_errors = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Control the maximum number of shown errors from validation.",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    name = Unicode(
        default_value=None, allow_none=True, help="Sets the component's name attribute."
    ).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True, help="Puts input in readonly state.").tag(
        sync=True
    )

    rules = TList(
        Any(),
        default_value=None,
        allow_none=True,
        help="Accepts a mixed array of types `function`, `boolean` and `string`. Functions pass an input value as an argument and must return either `true` / `false` or a `string` containing an error message. The input field will enter an error state if a function returns (or any value in the array contains) `false` or is a `string`.",
    ).tag(sync=True)

    validate_on = Unicode(
        default_value=None,
        allow_none=True,
        help="Change what type of event triggers validation to run.",
    ).tag(sync=True)

    validation_value = Any(help="The value used when applying validation rules.").tag(sync=True)


class Video(VuetifyWidget):
    """Widget for the Vuetify v-video component, see https://vuetifyjs.com/en/api/v-video/"""

    _model_name = Unicode("VideoModel").tag(sync=True)

    aspect_ratio = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the aspect ratio for the playback, calculated as width/height.",
    ).tag(sync=True)

    autoplay = Bool(
        default_value=None,
        allow_none=True,
        help="Starts loading the media file without waiting for user to click. Playback begins once enough data is loaded.",
    ).tag(sync=True)

    background_color = Unicode(
        default_value=None, allow_none=True, help="Container background color."
    ).tag(sync=True)

    color = Unicode(
        default_value=None, allow_none=True, help="General color applied to icons and sliders."
    ).tag(sync=True)

    controls_props = Any(
        help="Pass props through to the `v-video-controls` component. Accepts an object with anything from [v-video-controls](https://vuetifyjs.com/en/api/v-video-controls/#props) props, camelCase keys are recommended."
    ).tag(sync=True)

    controls_transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="The reveal transition applied to the VVideoControls component once the media file is loaded.",
    ).tag(sync=True)

    controls_variant = Unicode(
        default_value=None, allow_none=True, help="Variant passed to the VVideoControls component."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    detached = Bool(
        default_value=None,
        allow_none=True,
        help="Moves the container below so it won't obstruct the video.",
    ).tag(sync=True)

    duration = Float(
        default_value=None,
        allow_none=True,
        help="Total duration of the video used to calculate displayed time.",
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Silently loades the media file without waiting for user to click.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    floating = Bool(
        default_value=None,
        allow_none=True,
        help="Introduces visual spacing from the video boundaries.",
    ).tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the height for the component.",
    ).tag(sync=True)

    hide_fullscreen = Bool(
        default_value=None, allow_none=True, help="Hides default fullscreen button."
    ).tag(sync=True)

    hide_overlay = Bool(default_value=None, allow_none=True, help="Hide center play icon.").tag(
        sync=True
    )

    hide_play = Bool(default_value=None, allow_none=True, help="Hides default play button.").tag(
        sync=True
    )

    hide_volume = Bool(
        default_value=None, allow_none=True, help="Hides default volume control."
    ).tag(sync=True)

    image = Unicode(
        default_value=None,
        allow_none=True,
        help="Apply a specific image as cover before the video is loaded.",
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    muted = Bool(
        default_value=None,
        allow_none=True,
        help="Hides volume control and disables the playback sound.",
    ).tag(sync=True)

    no_fullscreen = Bool(
        default_value=None,
        allow_none=True,
        help="Disable fullscreen and hide the default fullscreen button.",
    ).tag(sync=True)

    pills = Bool(
        default_value=None,
        allow_none=True,
        help="Makes the container transparent and shows inner actions in separated boxes.",
    ).tag(sync=True)

    playing = Bool(
        default_value=None, allow_none=True, help="Applies correct icon of the default play button."
    ).tag(sync=True)

    progress = Float(
        default_value=None, allow_none=True, help="Controls main slider value (0 ~ 100)"
    ).tag(sync=True)

    rounded = Union(
        [Unicode(), Float(), Bool(), TList(Any())],
        default_value=None,
        allow_none=True,
        help="Applies a border radius to the video container and the controls. Accepts array of two values to customize elements separately.",
    ).tag(sync=True)

    split_time = Bool(
        default_value=None,
        allow_none=True,
        help="Splits time into elapsed and remaining on each side of the main slider.",
    ).tag(sync=True)

    src = Unicode(default_value=None, allow_none=True, help="Media file URL").tag(sync=True)

    start_at = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Moves progress to the specified time (in seconds) once the media file is loaded.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    track_color = Unicode(
        default_value=None, allow_none=True, help="Passed to the main slider `color` prop."
    ).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True, help="Media file type (optional)").tag(
        sync=True
    )

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    volume = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Volume value passed to the underlying control and slots.",
    ).tag(sync=True)

    volume_props = Unicode(
        default_value=None, allow_none=True, help="Props passed down to the VVideoVolume component."
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class VideoControls(VuetifyWidget):
    """Widget for the Vuetify v-video-controls component, see https://vuetifyjs.com/en/api/v-video-controls/"""

    _model_name = Unicode("VideoControlsModel").tag(sync=True)

    background_color = Unicode(
        default_value=None, allow_none=True, help="Container background color."
    ).tag(sync=True)

    color = Unicode(
        default_value=None, allow_none=True, help="General color applied to icons and sliders."
    ).tag(sync=True)

    density = Unicode(
        default_value=None,
        allow_none=True,
        help="Adjusts the vertical height used by the component.",
    ).tag(sync=True)

    detached = Bool(
        default_value=None,
        allow_none=True,
        help="Moves the container below so it won't obstruct the video.",
    ).tag(sync=True)

    duration = Float(
        default_value=None,
        allow_none=True,
        help="Total duration of the video used to calculate displayed time.",
    ).tag(sync=True)

    elevation = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Designates an elevation applied to the component between 0 and 24. You can find more information on the [elevation page](https://vuetifyjs.com/en/styles/elevation).",
    ).tag(sync=True)

    floating = Bool(
        default_value=None,
        allow_none=True,
        help="Introduces visual spacing from the video boundaries.",
    ).tag(sync=True)

    fullscreen = Bool(
        default_value=None,
        allow_none=True,
        help="Applies correct icon on the default fullscreen button.",
    ).tag(sync=True)

    hide_fullscreen = Bool(
        default_value=None, allow_none=True, help="Hides default fullscreen button."
    ).tag(sync=True)

    hide_play = Bool(default_value=None, allow_none=True, help="Hides default play button.").tag(
        sync=True
    )

    hide_volume = Bool(
        default_value=None, allow_none=True, help="Hides default volume control."
    ).tag(sync=True)

    pills = Bool(
        default_value=None,
        allow_none=True,
        help="Makes the container transparent and shows inner actions in separated boxes.",
    ).tag(sync=True)

    playing = Bool(
        default_value=None, allow_none=True, help="Applies correct icon of the default play button."
    ).tag(sync=True)

    progress = Float(
        default_value=None, allow_none=True, help="Controls main slider value (0 ~ 100)"
    ).tag(sync=True)

    split_time = Bool(
        default_value=None,
        allow_none=True,
        help="Splits time into elapsed and remaining on each side of the main slider.",
    ).tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    track_color = Unicode(
        default_value=None, allow_none=True, help="Passed to the main slider `color` prop."
    ).tag(sync=True)

    variant = Unicode(
        default_value=None, allow_none=True, help="Applies a distinct style to the component."
    ).tag(sync=True)

    volume = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Volume value passed to the underlying control and slots.",
    ).tag(sync=True)

    volume_props = Unicode(
        default_value=None, allow_none=True, help="Props passed down to the VVideoVolume component."
    ).tag(sync=True)


class VideoVolume(VuetifyWidget):
    """Widget for the Vuetify v-video-volume component, see https://vuetifyjs.com/en/api/v-video-volume/"""

    _model_name = Unicode("VideoVolumeModel").tag(sync=True)

    direction = Unicode(
        default_value=None, allow_none=True, help="Switch between horizontal and vertical slider."
    ).tag(sync=True)

    inline = Bool(
        default_value=None,
        allow_none=True,
        help="Display slider next to the icon. VMenu won't be displayed on click. Recomended to pair with **sliderProps** to configure slider width.",
    ).tag(sync=True)

    label = Unicode(
        default_value=None,
        allow_none=True,
        help="Text to display in tooltip and passed to `aria-label`.",
    ).tag(sync=True)

    menu_props = Any(
        help="Props passed to VMenu containing volume slider. Useful to adjust **location** and control menu alignment"
    ).tag(sync=True)

    model_value = Float(default_value=None, allow_none=True, help="Volume value (0 ~ 100)").tag(
        sync=True
    )

    slider_props = Dict(
        default_value=None, allow_none=True, help="Selected props to customize volume slider."
    ).tag(sync=True)


class VirtualScroll(VuetifyWidget):
    """Widget for the Vuetify v-virtual-scroll component, see https://vuetifyjs.com/en/api/v-virtual-scroll/"""

    _model_name = Unicode("VirtualScrollModel").tag(sync=True)

    height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Height of the component as a css value/",
    ).tag(sync=True)

    item_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Height in pixels of each item to display.",
    ).tag(sync=True)

    item_key = Unicode(
        default_value=None,
        allow_none=True,
        help="Should point to a property with a unique value for each item, if not set then item index will be used as a key which may result in unnecessary re-renders.",
    ).tag(sync=True)

    items = TList(
        Any(), default_value=None, allow_none=True, help="The array of items to display."
    ).tag(sync=True)

    max_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum height for the component.",
    ).tag(sync=True)

    max_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the maximum width for the component.",
    ).tag(sync=True)

    min_height = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum height for the component.",
    ).tag(sync=True)

    min_width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the minimum width for the component.",
    ).tag(sync=True)

    renderless = Bool(
        default_value=None,
        allow_none=True,
        help="Disables default component rendering functionality. The parent node must be [a positioned element](https://developer.mozilla.org/en-US/docs/Web/CSS/position#types_of_positioning), e.g. using `position: relative;`",
    ).tag(sync=True)

    width = Union(
        [Unicode(), Float()],
        default_value=None,
        allow_none=True,
        help="Sets the width for the component.",
    ).tag(sync=True)


class Window(VuetifyWidget):
    """Widget for the Vuetify v-window component, see https://vuetifyjs.com/en/api/v-window/"""

    _model_name = Unicode("WindowModel").tag(sync=True)

    continuous = Bool(
        default_value=None,
        allow_none=True,
        help='If `true`, window will "wrap around" from the last item to the first, and from the first item to the last.',
    ).tag(sync=True)

    crossfade = Bool(default_value=None, allow_none=True, help="Enables crossfade transition.").tag(
        sync=True
    )

    direction = Unicode(
        default_value=None, allow_none=True, help="The transition direction when changing windows."
    ).tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help="Removes the ability to click or target the component.",
    ).tag(sync=True)

    mandatory = Union(
        [Bool(), Unicode()],
        default_value=None,
        allow_none=True,
        help="Forces at least one item to always be selected (if available).",
    ).tag(sync=True)

    model_value = Any(
        help="The v-model value of the component. If component supports the **multiple** prop, this defaults to an empty array."
    ).tag(sync=True)

    next_icon = Any(help='Icon used for the "next" button if `show-arrows` is `true`.').tag(
        sync=True
    )

    prev_icon = Any(help='Icon used for the "prev" button if `show-arrows` is `true`.').tag(
        sync=True
    )

    reverse = Bool(
        default_value=None, allow_none=True, help="Reverse the normal transition direction."
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    show_arrows = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help='Display the "next" and "prev" buttons.',
    ).tag(sync=True)

    tag = Any(help="Specify a custom tag used on the root element.").tag(sync=True)

    theme = Unicode(
        default_value=None,
        allow_none=True,
        help="Specify a theme for this component and all of its children.",
    ).tag(sync=True)

    touch = Bool(
        default_value=None,
        allow_none=True,
        help="Provide a custom **left** and **right** function when swiped left or right.",
    ).tag(sync=True)

    transition_duration = Float(
        default_value=None,
        allow_none=True,
        help="Overrides transition duration. Does not work in firefox, safari <18, or with `prefers-reduced-motion: reduce`.",
    ).tag(sync=True)

    vertical_arrows = Union(
        [Bool(), Unicode(), Unicode()], default_value=None, allow_none=True
    ).tag(sync=True)


class WindowItem(VuetifyWidget):
    """Widget for the Vuetify v-window-item component, see https://vuetifyjs.com/en/api/v-window-item/"""

    _model_name = Unicode("WindowItemModel").tag(sync=True)

    disabled = Bool(
        default_value=None,
        allow_none=True,
        help='Prevents the item from becoming active when using the "next" and "prev" buttons or the `toggle` method.',
    ).tag(sync=True)

    eager = Bool(
        default_value=None,
        allow_none=True,
        help="Forces the component's content to render when it mounts. This is useful if you have content that will not be rendered in the DOM that you want crawled for SEO.",
    ).tag(sync=True)

    reverse_transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="Sets the reverse transition.",
    ).tag(sync=True)

    selected_class = Unicode(
        default_value=None,
        allow_none=True,
        help="Configure the active CSS class applied when an item is selected.",
    ).tag(sync=True)

    transition = Union(
        [Unicode(), Bool()],
        default_value=None,
        allow_none=True,
        help="The transition used when the component progressing through items. Can be one of the [built in](https://vuetifyjs.com/en/styles/transitions/) or custom transition.",
    ).tag(sync=True)

    value = Any(
        help="The value used when the component is selected in a group. If not provided, a unique ID will be used."
    ).tag(sync=True)


__all__ = [
    "VuetifyWidget",
    "Alert",
    "AlertTitle",
    "App",
    "AppBar",
    "AppBarNavIcon",
    "AppBarTitle",
    "Autocomplete",
    "Avatar",
    "AvatarGroup",
    "Badge",
    "Banner",
    "BannerActions",
    "BannerText",
    "BottomNavigation",
    "BottomSheet",
    "Breadcrumbs",
    "BreadcrumbsDivider",
    "BreadcrumbsItem",
    "Btn",
    "BtnGroup",
    "BtnToggle",
    "Calendar",
    "Card",
    "CardActions",
    "CardItem",
    "CardSubtitle",
    "CardText",
    "CardTitle",
    "Carousel",
    "CarouselItem",
    "Checkbox",
    "CheckboxBtn",
    "Chip",
    "ChipGroup",
    "ClassIcon",
    "Code",
    "Col",
    "ColorInput",
    "ColorPicker",
    "Combobox",
    "CommandPalette",
    "CommandPaletteItemComponent",
    "ComponentIcon",
    "ConfirmEdit",
    "Container",
    "Counter",
    "DataIterator",
    "DataTable",
    "DataTableFooter",
    "DataTableHeaders",
    "DataTableRow",
    "DataTableRows",
    "DataTableServer",
    "DataTableVirtual",
    "DateInput",
    "DatePicker",
    "DatePickerControls",
    "DatePickerHeader",
    "DatePickerMonth",
    "DatePickerMonths",
    "DatePickerYears",
    "DefaultsProvider",
    "Dialog",
    "DialogBottomTransition",
    "DialogTopTransition",
    "DialogTransition",
    "Divider",
    "EmptyState",
    "ExpandBothTransition",
    "ExpandTransition",
    "ExpandXTransition",
    "ExpansionPanel",
    "ExpansionPanelText",
    "ExpansionPanelTitle",
    "ExpansionPanels",
    "Fab",
    "FabTransition",
    "FadeTransition",
    "Field",
    "FieldLabel",
    "FileInput",
    "FileUpload",
    "FileUploadDropzone",
    "FileUploadItem",
    "FileUploadList",
    "Footer",
    "Form",
    "Hotkey",
    "Hover",
    "Icon",
    "IconBtn",
    "Img",
    "InfiniteScroll",
    "Input",
    "Item",
    "ItemGroup",
    "Kbd",
    "Label",
    "Layout",
    "LayoutItem",
    "Lazy",
    "LigatureIcon",
    "List",
    "ListGroup",
    "ListImg",
    "ListItem",
    "ListItemAction",
    "ListItemMedia",
    "ListItemSubtitle",
    "ListItemTitle",
    "ListSubheader",
    "LocaleProvider",
    "Main",
    "MaskInput",
    "Menu",
    "Messages",
    "NavigationDrawer",
    "NoSsr",
    "NumberInput",
    "OtpInput",
    "Overlay",
    "Pagination",
    "Parallax",
    "Picker",
    "PickerTitle",
    "Pie",
    "PieSegment",
    "PieTooltip",
    "ProgressCircular",
    "ProgressLinear",
    "PullToRefresh",
    "Radio",
    "RadioGroup",
    "RangeSlider",
    "Rating",
    "Responsive",
    "Row",
    "ScaleTransition",
    "ScrollXReverseTransition",
    "ScrollXTransition",
    "ScrollYReverseTransition",
    "ScrollYTransition",
    "Select",
    "SelectionControl",
    "SelectionControlGroup",
    "Sheet",
    "SkeletonLoader",
    "SlideGroup",
    "SlideGroupItem",
    "SlideXReverseTransition",
    "SlideXTransition",
    "SlideYReverseTransition",
    "SlideYTransition",
    "Slider",
    "Snackbar",
    "SnackbarQueue",
    "Spacer",
    "Sparkline",
    "SpeedDial",
    "Stepper",
    "StepperActions",
    "StepperHeader",
    "StepperItem",
    "StepperVertical",
    "StepperVerticalActions",
    "StepperVerticalItem",
    "StepperWindow",
    "StepperWindowItem",
    "SvgIcon",
    "Switch",
    "SystemBar",
    "Tab",
    "Table",
    "Tabs",
    "TabsWindow",
    "TabsWindowItem",
    "TextField",
    "Textarea",
    "ThemeProvider",
    "TimePicker",
    "TimePickerClock",
    "TimePickerControls",
    "Timeline",
    "TimelineItem",
    "Toolbar",
    "ToolbarItems",
    "ToolbarTitle",
    "Tooltip",
    "Treeview",
    "TreeviewGroup",
    "TreeviewItem",
    "Validation",
    "Video",
    "VideoControls",
    "VideoVolume",
    "VirtualScroll",
    "Window",
    "WindowItem",
]
