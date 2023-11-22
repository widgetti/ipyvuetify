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
    _model_name = Unicode("AlertModel").tag(sync=True)

    border = Union(
        [Bool(), Unicode(), Unicode(), Unicode(), Unicode()],
        default_value=None,
        allow_none=True,
    ).tag(sync=True)

    border_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    closable = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    close_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    icon = Bool(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prominent = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class AlertTitle(VuetifyWidget):
    _model_name = Unicode("AlertTitleModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class App(VuetifyWidget):
    _model_name = Unicode("AppModel").tag(sync=True)

    full_height = Bool(default_value=None, allow_none=True).tag(sync=True)

    overlaps = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class AppBar(VuetifyWidget):
    _model_name = Unicode("AppBarModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    collapse = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    extended = Bool(default_value=None, allow_none=True).tag(sync=True)

    extension_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(
        sync=True
    )

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    floating = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    image = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    order = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    scroll_behavior = Unicode(default_value=None, allow_none=True).tag(sync=True)

    scroll_target = Unicode(default_value=None, allow_none=True).tag(sync=True)

    scroll_threshold = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)


class AppBarNavIcon(VuetifyWidget):
    _model_name = Unicode("AppBarNavIconModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    block = Bool(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    exact = Bool(default_value=None, allow_none=True).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    href = Unicode(default_value=None, allow_none=True).tag(sync=True)

    icon = Bool(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    replace = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    stacked = Bool(default_value=None, allow_none=True).tag(sync=True)

    symbol = Any().tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class AppBarTitle(VuetifyWidget):
    _model_name = Unicode("AppBarTitleModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Autocomplete(VuetifyWidget):
    _model_name = Unicode("AutocompleteModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    auto_select_first = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(
        sync=True
    )

    autofocus = Bool(default_value=None, allow_none=True).tag(sync=True)

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    chips = Bool(default_value=None, allow_none=True).tag(sync=True)

    clear_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    clearable = Bool(default_value=None, allow_none=True).tag(sync=True)

    closable_chips = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    counter = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    counter_value = Float(default_value=None, allow_none=True).tag(sync=True)

    custom_filter = Unicode(default_value=None, allow_none=True).tag(sync=True)

    custom_key_filter = Dict(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    filter_keys = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    filter_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hide_no_data = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_selected = Bool(default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_children = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_props = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    menu = Bool(default_value=None, allow_none=True).tag(sync=True)

    menu_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_counter = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_placeholder = Bool(default_value=None, allow_none=True).tag(sync=True)

    placeholder = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    prepend_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    return_object = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    role = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    search = Unicode(default_value=None, allow_none=True).tag(sync=True)

    single_line = Bool(default_value=None, allow_none=True).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Avatar(VuetifyWidget):
    _model_name = Unicode("AvatarModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    end = Bool(default_value=None, allow_none=True).tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    image = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    start = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Badge(VuetifyWidget):
    _model_name = Unicode("BadgeModel").tag(sync=True)

    bordered = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    content = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    dot = Bool(default_value=None, allow_none=True).tag(sync=True)

    floating = Bool(default_value=None, allow_none=True).tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    offset_x = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    offset_y = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Banner(VuetifyWidget):
    _model_name = Unicode("BannerModel").tag(sync=True)

    avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    lines = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    stacked = Bool(default_value=None, allow_none=True).tag(sync=True)

    sticky = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class BannerActions(VuetifyWidget):
    _model_name = Unicode("BannerActionsModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)


class BannerText(VuetifyWidget):
    _model_name = Unicode("BannerTextModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class BottomNavigation(VuetifyWidget):
    _model_name = Unicode("BottomNavigationModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    grow = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    max = Float(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    order = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class BottomSheet(VuetifyWidget):
    _model_name = Unicode("BottomSheetModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    activator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    activator_props = Dict(default_value=None, allow_none=True).tag(sync=True)

    attach = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    close_on_back = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_on_content_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    contained = Bool(default_value=None, allow_none=True).tag(sync=True)

    content_class = Any().tag(sync=True)

    content_props = Any().tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    fullscreen = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    inset = Bool(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_click_animation = Bool(default_value=None, allow_none=True).tag(sync=True)

    offset = Union([Unicode(), Float(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    open_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    open_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent = Bool(default_value=None, allow_none=True).tag(sync=True)

    retain_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    scrim = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    scroll_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    scrollable = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    z_index = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Breadcrumbs(VuetifyWidget):
    _model_name = Unicode("BreadcrumbsModel").tag(sync=True)

    active_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    active_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    divider = Unicode(default_value=None, allow_none=True).tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class BreadcrumbsDivider(VuetifyWidget):
    _model_name = Unicode("BreadcrumbsDividerModel").tag(sync=True)

    divider = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class BreadcrumbsItem(VuetifyWidget):
    _model_name = Unicode("BreadcrumbsItemModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    active_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    active_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    exact = Bool(default_value=None, allow_none=True).tag(sync=True)

    href = Unicode(default_value=None, allow_none=True).tag(sync=True)

    replace = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Btn(VuetifyWidget):
    _model_name = Unicode("BtnModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    block = Bool(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    exact = Bool(default_value=None, allow_none=True).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    href = Unicode(default_value=None, allow_none=True).tag(sync=True)

    icon = Bool(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    replace = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    stacked = Bool(default_value=None, allow_none=True).tag(sync=True)

    symbol = Any().tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class BtnGroup(VuetifyWidget):
    _model_name = Unicode("BtnGroupModel").tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    divided = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class BtnToggle(VuetifyWidget):
    _model_name = Unicode("BtnToggleModel").tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    divided = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    max = Float(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Card(VuetifyWidget):
    _model_name = Unicode("CardModel").tag(sync=True)

    append_avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    exact = Bool(default_value=None, allow_none=True).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    href = Unicode(default_value=None, allow_none=True).tag(sync=True)

    image = Unicode(default_value=None, allow_none=True).tag(sync=True)

    link = Bool(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    replace = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    subtitle = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class CardActions(VuetifyWidget):
    _model_name = Unicode("CardActionsModel").tag(sync=True)


class CardItem(VuetifyWidget):
    _model_name = Unicode("CardItemModel").tag(sync=True)

    append_avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    subtitle = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)


class CardSubtitle(VuetifyWidget):
    _model_name = Unicode("CardSubtitleModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class CardText(VuetifyWidget):
    _model_name = Unicode("CardTextModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class CardTitle(VuetifyWidget):
    _model_name = Unicode("CardTitleModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Carousel(VuetifyWidget):
    _model_name = Unicode("CarouselModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    continuous = Bool(default_value=None, allow_none=True).tag(sync=True)

    cycle = Bool(default_value=None, allow_none=True).tag(sync=True)

    delimiter_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_delimiter_background = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_delimiters = Bool(default_value=None, allow_none=True).tag(sync=True)

    interval = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    next_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    progress = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_arrows = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    touch = Any().tag(sync=True)

    vertical_delimiters = Union(
        [Bool(), Unicode(), Unicode()], default_value=None, allow_none=True
    ).tag(sync=True)


class CarouselItem(VuetifyWidget):
    _model_name = Unicode("CarouselItemModel").tag(sync=True)

    alt = Unicode(default_value=None, allow_none=True).tag(sync=True)

    aspect_ratio = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    content_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    cover = Bool(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    gradient = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    lazy_src = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    options = Dict(default_value=None, allow_none=True).tag(sync=True)

    reverse_transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    sizes = Unicode(default_value=None, allow_none=True).tag(sync=True)

    src = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    srcset = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Checkbox(VuetifyWidget):
    _model_name = Unicode("CheckboxModel").tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    defaults_target = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    false_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    false_value = Any().tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    indeterminate = Bool(default_value=None, allow_none=True).tag(sync=True)

    indeterminate_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Bool(default_value=None, allow_none=True).tag(sync=True)

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    true_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    true_value = Any().tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)

    value = Any().tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)


class CheckboxBtn(VuetifyWidget):
    _model_name = Unicode("CheckboxBtnModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    defaults_target = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    false_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    false_value = Any().tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    indeterminate = Bool(default_value=None, allow_none=True).tag(sync=True)

    indeterminate_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    true_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    true_value = Any().tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Chip(VuetifyWidget):
    _model_name = Unicode("ChipModel").tag(sync=True)

    active_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    append_avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    closable = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    close_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    draggable = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    exact = Bool(default_value=None, allow_none=True).tag(sync=True)

    filter = Bool(default_value=None, allow_none=True).tag(sync=True)

    filter_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    href = Unicode(default_value=None, allow_none=True).tag(sync=True)

    label = Bool(default_value=None, allow_none=True).tag(sync=True)

    link = Bool(default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    pill = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    replace = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ChipGroup(VuetifyWidget):
    _model_name = Unicode("ChipGroupModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    column = Bool(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    filter = Bool(default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    max = Float(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ClassIcon(VuetifyWidget):
    _model_name = Unicode("ClassIconModel").tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Code(VuetifyWidget):
    _model_name = Unicode("CodeModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Col(VuetifyWidget):
    _model_name = Unicode("ColModel").tag(sync=True)

    align_self = Unicode(default_value=None, allow_none=True).tag(sync=True)

    cols = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    lg = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    md = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    offset = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    offset_lg = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    offset_md = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    offset_sm = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    offset_xl = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    offset_xxl = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    order = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    order_lg = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    order_md = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    order_sm = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    order_xl = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    order_xxl = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    sm = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    xl = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    xxl = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)


class ColorPicker(VuetifyWidget):
    _model_name = Unicode("ColorPickerModel").tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    canvas_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    dot_size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_canvas = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_inputs = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_sliders = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    modes = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    show_swatches = Bool(default_value=None, allow_none=True).tag(sync=True)

    swatches = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    swatches_max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Combobox(VuetifyWidget):
    _model_name = Unicode("ComboboxModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    auto_select_first = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(
        sync=True
    )

    autofocus = Bool(default_value=None, allow_none=True).tag(sync=True)

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    chips = Bool(default_value=None, allow_none=True).tag(sync=True)

    clear_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    clearable = Bool(default_value=None, allow_none=True).tag(sync=True)

    closable_chips = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    counter = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    counter_value = Float(default_value=None, allow_none=True).tag(sync=True)

    custom_filter = Unicode(default_value=None, allow_none=True).tag(sync=True)

    custom_key_filter = Dict(default_value=None, allow_none=True).tag(sync=True)

    delimiters = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    filter_keys = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    filter_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hide_no_data = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_selected = Bool(default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_children = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_props = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    menu = Bool(default_value=None, allow_none=True).tag(sync=True)

    menu_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_counter = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_placeholder = Bool(default_value=None, allow_none=True).tag(sync=True)

    placeholder = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    prepend_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    return_object = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    role = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    single_line = Bool(default_value=None, allow_none=True).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ComponentIcon(VuetifyWidget):
    _model_name = Unicode("ComponentIconModel").tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Container(VuetifyWidget):
    _model_name = Unicode("ContainerModel").tag(sync=True)

    fluid = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Counter(VuetifyWidget):
    _model_name = Unicode("CounterModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    value = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class DataIterator(VuetifyWidget):
    _model_name = Unicode("DataIteratorModel").tag(sync=True)

    custom_filter = Unicode(default_value=None, allow_none=True).tag(sync=True)

    custom_key_filter = Dict(default_value=None, allow_none=True).tag(sync=True)

    expand_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    expanded = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    filter_keys = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    filter_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    group_by = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    item_selectable = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    items_per_page = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    loading = Bool(default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    multi_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    must_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True).tag(sync=True)

    page = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    return_object = Bool(default_value=None, allow_none=True).tag(sync=True)

    search = Unicode(default_value=None, allow_none=True).tag(sync=True)

    select_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_expand = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_select = Bool(default_value=None, allow_none=True).tag(sync=True)

    sort_by = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DataTable(VuetifyWidget):
    _model_name = Unicode("DataTableModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    custom_filter = Unicode(default_value=None, allow_none=True).tag(sync=True)

    custom_key_filter = Dict(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    expand_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    expanded = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    filter_keys = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    filter_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    first_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    first_page_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    fixed_footer = Bool(default_value=None, allow_none=True).tag(sync=True)

    fixed_header = Bool(default_value=None, allow_none=True).tag(sync=True)

    group_by = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    headers = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_no_data = Bool(default_value=None, allow_none=True).tag(sync=True)

    hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    item_selectable = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    items_per_page = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    items_per_page_options = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    items_per_page_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    last_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    last_page_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    loading_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    multi_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    must_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    next_page_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True).tag(sync=True)

    page = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    page_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_page_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    return_object = Bool(default_value=None, allow_none=True).tag(sync=True)

    row_height = Float(default_value=None, allow_none=True).tag(sync=True)

    search = Unicode(default_value=None, allow_none=True).tag(sync=True)

    select_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_current_page = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_expand = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_select = Bool(default_value=None, allow_none=True).tag(sync=True)

    sort_asc_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    sort_by = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    sort_desc_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    sticky = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class DataTableFooter(VuetifyWidget):
    _model_name = Unicode("DataTableFooterModel").tag(sync=True)


class DataTableRow(VuetifyWidget):
    _model_name = Unicode("DataTableRowModel").tag(sync=True)

    index = Float(default_value=None, allow_none=True).tag(sync=True)

    item = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DataTableRows(VuetifyWidget):
    _model_name = Unicode("DataTableRowsModel").tag(sync=True)

    hide_no_data = Bool(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    loading_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    row_height = Float(default_value=None, allow_none=True).tag(sync=True)


class DataTableServer(VuetifyWidget):
    _model_name = Unicode("DataTableServerModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    expand_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    expanded = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    first_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    first_page_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    fixed_footer = Bool(default_value=None, allow_none=True).tag(sync=True)

    fixed_header = Bool(default_value=None, allow_none=True).tag(sync=True)

    group_by = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    headers = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_no_data = Bool(default_value=None, allow_none=True).tag(sync=True)

    hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    item_selectable = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    items_length = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    items_per_page = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    items_per_page_options = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    items_per_page_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    last_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    last_page_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    loading_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    multi_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    must_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    next_page_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    page = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    page_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_page_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    return_object = Bool(default_value=None, allow_none=True).tag(sync=True)

    row_height = Float(default_value=None, allow_none=True).tag(sync=True)

    search = Unicode(default_value=None, allow_none=True).tag(sync=True)

    select_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_current_page = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_expand = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_select = Bool(default_value=None, allow_none=True).tag(sync=True)

    sort_asc_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    sort_by = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    sort_desc_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    sticky = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class DataTableVirtual(VuetifyWidget):
    _model_name = Unicode("DataTableVirtualModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    custom_filter = Unicode(default_value=None, allow_none=True).tag(sync=True)

    custom_key_filter = Dict(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    expand_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    expanded = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    filter_keys = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    filter_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    fixed_footer = Bool(default_value=None, allow_none=True).tag(sync=True)

    fixed_header = Bool(default_value=None, allow_none=True).tag(sync=True)

    group_by = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    headers = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_no_data = Bool(default_value=None, allow_none=True).tag(sync=True)

    hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    item_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    item_selectable = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    loading_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    multi_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    must_sort = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_filter = Bool(default_value=None, allow_none=True).tag(sync=True)

    return_object = Bool(default_value=None, allow_none=True).tag(sync=True)

    row_height = Float(default_value=None, allow_none=True).tag(sync=True)

    search = Unicode(default_value=None, allow_none=True).tag(sync=True)

    select_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_expand = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_select = Bool(default_value=None, allow_none=True).tag(sync=True)

    sort_asc_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    sort_by = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    sort_desc_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    sticky = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class DateCard(VuetifyWidget):
    _model_name = Unicode("DateCardModel").tag(sync=True)

    allowed_dates = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    cancel_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Union([Unicode(), Bool(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    display_date = Any().tag(sync=True)

    format = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_actions = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_weekdays = Bool(default_value=None, allow_none=True).tag(sync=True)

    hover_date = Any().tag(sync=True)

    input_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    mode_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    ok_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_adjacent_months = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_week = Bool(default_value=None, allow_none=True).tag(sync=True)

    side = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    view_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DatePicker(VuetifyWidget):
    _model_name = Unicode("DatePickerModel").tag(sync=True)

    allowed_dates = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    calendar_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    cancel_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Union([Unicode(), Bool(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    display_date = Any().tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    format = Unicode(default_value=None, allow_none=True).tag(sync=True)

    header = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_actions = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_weekdays = Bool(default_value=None, allow_none=True).tag(sync=True)

    hover_date = Any().tag(sync=True)

    input_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    input_placeholder = Unicode(default_value=None, allow_none=True).tag(sync=True)

    input_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    keyboard_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    landscape = Bool(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    mode_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    ok_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    show_adjacent_months = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_week = Bool(default_value=None, allow_none=True).tag(sync=True)

    side = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    view_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class DatePickerControls(VuetifyWidget):
    _model_name = Unicode("DatePickerControlsModel").tag(sync=True)

    disabled = Union([Unicode(), Bool(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    display_date = Unicode(default_value=None, allow_none=True).tag(sync=True)

    mode_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    view_mode = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DatePickerHeader(VuetifyWidget):
    _model_name = Unicode("DatePickerHeaderModel").tag(sync=True)

    append_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    header = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DatePickerMonth(VuetifyWidget):
    _model_name = Unicode("DatePickerMonthModel").tag(sync=True)

    allowed_dates = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    display_date = Any().tag(sync=True)

    format = Unicode(default_value=None, allow_none=True).tag(sync=True)

    hide_weekdays = Bool(default_value=None, allow_none=True).tag(sync=True)

    hover_date = Any().tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_adjacent_months = Bool(default_value=None, allow_none=True).tag(sync=True)

    show_week = Bool(default_value=None, allow_none=True).tag(sync=True)

    side = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DatePickerYears(VuetifyWidget):
    _model_name = Unicode("DatePickerYearsModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    display_date = Any().tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class DefaultsProvider(VuetifyWidget):
    _model_name = Unicode("DefaultsProviderModel").tag(sync=True)

    defaults = Dict(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    reset = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    root = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    scoped = Bool(default_value=None, allow_none=True).tag(sync=True)


class Dialog(VuetifyWidget):
    _model_name = Unicode("DialogModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    activator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    activator_props = Dict(default_value=None, allow_none=True).tag(sync=True)

    attach = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    close_on_back = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_on_content_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    contained = Bool(default_value=None, allow_none=True).tag(sync=True)

    content_class = Any().tag(sync=True)

    content_props = Any().tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    fullscreen = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_click_animation = Bool(default_value=None, allow_none=True).tag(sync=True)

    offset = Union([Unicode(), Float(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    open_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    open_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent = Bool(default_value=None, allow_none=True).tag(sync=True)

    retain_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    scrim = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    scroll_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    scrollable = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    z_index = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class DialogBottomTransition(VuetifyWidget):
    _model_name = Unicode("DialogBottomTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DialogTopTransition(VuetifyWidget):
    _model_name = Unicode("DialogTopTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class DialogTransition(VuetifyWidget):
    _model_name = Unicode("DialogTransitionModel").tag(sync=True)

    target = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Divider(VuetifyWidget):
    _model_name = Unicode("DividerModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    inset = Bool(default_value=None, allow_none=True).tag(sync=True)

    length = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    thickness = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    vertical = Bool(default_value=None, allow_none=True).tag(sync=True)


class ExpandTransition(VuetifyWidget):
    _model_name = Unicode("ExpandTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ExpandXTransition(VuetifyWidget):
    _model_name = Unicode("ExpandXTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ExpansionPanel(VuetifyWidget):
    _model_name = Unicode("ExpansionPanelModel").tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    collapse_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    expand_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    hide_actions = Bool(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)


class ExpansionPanelText(VuetifyWidget):
    _model_name = Unicode("ExpansionPanelTextModel").tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)


class ExpansionPanelTitle(VuetifyWidget):
    _model_name = Unicode("ExpansionPanelTitleModel").tag(sync=True)

    collapse_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    expand_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    hide_actions = Bool(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)


class ExpansionPanels(VuetifyWidget):
    _model_name = Unicode("ExpansionPanelsModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    max = Float(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class FabTransition(VuetifyWidget):
    _model_name = Unicode("FabTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class FadeTransition(VuetifyWidget):
    _model_name = Unicode("FadeTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Field(VuetifyWidget):
    _model_name = Unicode("FieldModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    clear_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    clearable = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    dirty = Bool(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    persistent_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    single_line = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class FieldLabel(VuetifyWidget):
    _model_name = Unicode("FieldLabelModel").tag(sync=True)

    floating = Bool(default_value=None, allow_none=True).tag(sync=True)


class FileInput(VuetifyWidget):
    _model_name = Unicode("FileInputModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    append_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    chips = Bool(default_value=None, allow_none=True).tag(sync=True)

    clear_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    clearable = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    counter = Bool(default_value=None, allow_none=True).tag(sync=True)

    counter_size_string = Unicode(default_value=None, allow_none=True).tag(sync=True)

    counter_string = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    dirty = Bool(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    prepend_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    show_size = Union([Bool(), Float(), Float()], default_value=None, allow_none=True).tag(
        sync=True
    )

    single_line = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Footer(VuetifyWidget):
    _model_name = Unicode("FooterModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    app = Bool(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    order = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Form(VuetifyWidget):
    _model_name = Unicode("FormModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    fast_fail = Bool(default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Hover(VuetifyWidget):
    _model_name = Unicode("HoverModel").tag(sync=True)

    close_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Icon(VuetifyWidget):
    _model_name = Unicode("IconModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    end = Bool(default_value=None, allow_none=True).tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    start = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Img(VuetifyWidget):
    _model_name = Unicode("ImgModel").tag(sync=True)

    alt = Unicode(default_value=None, allow_none=True).tag(sync=True)

    aspect_ratio = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    content_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    cover = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    gradient = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    lazy_src = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    options = Dict(default_value=None, allow_none=True).tag(sync=True)

    sizes = Unicode(default_value=None, allow_none=True).tag(sync=True)

    src = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    srcset = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class InfiniteScroll(VuetifyWidget):
    _model_name = Unicode("InfiniteScrollModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    empty_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    load_more_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    margin = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    side = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Input(VuetifyWidget):
    _model_name = Unicode("InputModel").tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)


class Item(VuetifyWidget):
    _model_name = Unicode("ItemModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)


class ItemGroup(VuetifyWidget):
    _model_name = Unicode("ItemGroupModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    max = Float(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Kbd(VuetifyWidget):
    _model_name = Unicode("KbdModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Label(VuetifyWidget):
    _model_name = Unicode("LabelModel").tag(sync=True)

    clickable = Bool(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Layout(VuetifyWidget):
    _model_name = Unicode("LayoutModel").tag(sync=True)

    full_height = Bool(default_value=None, allow_none=True).tag(sync=True)

    overlaps = TList(Any(), default_value=None, allow_none=True).tag(sync=True)


class LayoutItem(VuetifyWidget):
    _model_name = Unicode("LayoutItemModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    order = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Lazy(VuetifyWidget):
    _model_name = Unicode("LazyModel").tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    options = Dict(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class LigatureIcon(VuetifyWidget):
    _model_name = Unicode("LigatureIconModel").tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class List(VuetifyWidget):
    _model_name = Unicode("ListModel").tag(sync=True)

    active_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    active_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    item_children = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_props = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    lines = Union(
        [Bool(), Unicode(), Unicode(), Unicode()], default_value=None, allow_none=True
    ).tag(sync=True)

    mandatory = Bool(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    nav = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_strategy = Union(
        [Unicode(), Unicode(), Unicode(), Dict()], default_value=None, allow_none=True
    ).tag(sync=True)

    opened = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    return_object = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    select_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    selected = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class ListGroup(VuetifyWidget):
    _model_name = Unicode("ListGroupModel").tag(sync=True)

    active_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    collapse_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    expand_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    fluid = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    subgroup = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)


class ListImg(VuetifyWidget):
    _model_name = Unicode("ListImgModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ListItem(VuetifyWidget):
    _model_name = Unicode("ListItemModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    active_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    active_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    append_avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    exact = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    href = Unicode(default_value=None, allow_none=True).tag(sync=True)

    lines = Unicode(default_value=None, allow_none=True).tag(sync=True)

    link = Bool(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    nav = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_avatar = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    replace = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    subtitle = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class ListItemAction(VuetifyWidget):
    _model_name = Unicode("ListItemActionModel").tag(sync=True)

    end = Bool(default_value=None, allow_none=True).tag(sync=True)

    start = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ListItemMedia(VuetifyWidget):
    _model_name = Unicode("ListItemMediaModel").tag(sync=True)

    end = Bool(default_value=None, allow_none=True).tag(sync=True)

    start = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ListItemSubtitle(VuetifyWidget):
    _model_name = Unicode("ListItemSubtitleModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ListItemTitle(VuetifyWidget):
    _model_name = Unicode("ListItemTitleModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ListSubheader(VuetifyWidget):
    _model_name = Unicode("ListSubheaderModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    inset = Bool(default_value=None, allow_none=True).tag(sync=True)

    sticky = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)


class LocaleProvider(VuetifyWidget):
    _model_name = Unicode("LocaleProviderModel").tag(sync=True)

    fallback_locale = Unicode(default_value=None, allow_none=True).tag(sync=True)

    locale = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rtl = Bool(default_value=None, allow_none=True).tag(sync=True)


class Main(VuetifyWidget):
    _model_name = Unicode("MainModel").tag(sync=True)

    scrollable = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Menu(VuetifyWidget):
    _model_name = Unicode("MenuModel").tag(sync=True)

    activator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    activator_props = Dict(default_value=None, allow_none=True).tag(sync=True)

    attach = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    close_on_back = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_on_content_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    contained = Bool(default_value=None, allow_none=True).tag(sync=True)

    content_class = Any().tag(sync=True)

    content_props = Any().tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_click_animation = Bool(default_value=None, allow_none=True).tag(sync=True)

    offset = Union([Unicode(), Float(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    open_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    open_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent = Bool(default_value=None, allow_none=True).tag(sync=True)

    scrim = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    scroll_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    z_index = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Messages(VuetifyWidget):
    _model_name = Unicode("MessagesModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)


class NavigationDrawer(VuetifyWidget):
    _model_name = Unicode("NavigationDrawerModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disable_resize_watcher = Bool(default_value=None, allow_none=True).tag(sync=True)

    disable_route_watcher = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    expand_on_hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    floating = Bool(default_value=None, allow_none=True).tag(sync=True)

    image = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    order = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    permanent = Bool(default_value=None, allow_none=True).tag(sync=True)

    rail = Bool(default_value=None, allow_none=True).tag(sync=True)

    rail_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    scrim = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    sticky = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    temporary = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    touchless = Bool(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class NoSsr(VuetifyWidget):
    _model_name = Unicode("NoSsrModel").tag(sync=True)


class OtpInput(VuetifyWidget):
    _model_name = Unicode("OtpInputModel").tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True).tag(sync=True)

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    divider = Unicode(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    focus_all = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    length = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    placeholder = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Overlay(VuetifyWidget):
    _model_name = Unicode("OverlayModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    activator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    activator_props = Dict(default_value=None, allow_none=True).tag(sync=True)

    attach = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    close_on_back = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_on_content_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    contained = Bool(default_value=None, allow_none=True).tag(sync=True)

    content_class = Any().tag(sync=True)

    content_props = Any().tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_click_animation = Bool(default_value=None, allow_none=True).tag(sync=True)

    offset = Union([Unicode(), Float(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    open_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    open_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent = Bool(default_value=None, allow_none=True).tag(sync=True)

    scrim = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    scroll_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    z_index = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Pagination(VuetifyWidget):
    _model_name = Unicode("PaginationModel").tag(sync=True)

    active_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    aria_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    current_page_aria_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    ellipsis = Unicode(default_value=None, allow_none=True).tag(sync=True)

    first_aria_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    first_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    last_aria_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    last_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    length = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Float(default_value=None, allow_none=True).tag(sync=True)

    next_aria_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    page_aria_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    previous_aria_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    show_first_last_page = Bool(default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    start = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    total_visible = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Parallax(VuetifyWidget):
    _model_name = Unicode("ParallaxModel").tag(sync=True)

    scale = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Picker(VuetifyWidget):
    _model_name = Unicode("PickerModel").tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    landscape = Bool(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class PickerTitle(VuetifyWidget):
    _model_name = Unicode("PickerTitleModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ProgressCircular(VuetifyWidget):
    _model_name = Unicode("ProgressCircularModel").tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    indeterminate = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rotate = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class ProgressLinear(VuetifyWidget):
    _model_name = Unicode("ProgressLinearModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_opacity = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    buffer_value = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    clickable = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    indeterminate = Bool(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rounded_bar = Bool(default_value=None, allow_none=True).tag(sync=True)

    stream = Bool(default_value=None, allow_none=True).tag(sync=True)

    striped = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Radio(VuetifyWidget):
    _model_name = Unicode("RadioModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    defaults_target = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    false_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    false_value = Any().tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    true_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    true_value = Any().tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)


class RadioGroup(VuetifyWidget):
    _model_name = Unicode("RadioGroupModel").tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    defaults_target = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    false_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Bool(default_value=None, allow_none=True).tag(sync=True)

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    true_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)


class RangeSlider(VuetifyWidget):
    _model_name = Unicode("RangeSliderModel").tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    min = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    show_ticks = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    step = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    strict = Bool(default_value=None, allow_none=True).tag(sync=True)

    thumb_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    thumb_label = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    thumb_size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    tick_size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    ticks = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    track_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    track_fill_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    track_size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)


class Rating(VuetifyWidget):
    _model_name = Unicode("RatingModel").tag(sync=True)

    active_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    clearable = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    empty_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    full_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    half_increments = Bool(default_value=None, allow_none=True).tag(sync=True)

    hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    item_aria_label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_label_position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_labels = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    length = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Bool(default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Responsive(VuetifyWidget):
    _model_name = Unicode("ResponsiveModel").tag(sync=True)

    aspect_ratio = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    content_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Row(VuetifyWidget):
    _model_name = Unicode("RowModel").tag(sync=True)

    align = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_content = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_content_lg = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_content_md = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_content_sm = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_content_xl = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_content_xxl = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_lg = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_md = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_sm = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_xl = Unicode(default_value=None, allow_none=True).tag(sync=True)

    align_xxl = Unicode(default_value=None, allow_none=True).tag(sync=True)

    dense = Bool(default_value=None, allow_none=True).tag(sync=True)

    justify = Unicode(default_value=None, allow_none=True).tag(sync=True)

    justify_lg = Unicode(default_value=None, allow_none=True).tag(sync=True)

    justify_md = Unicode(default_value=None, allow_none=True).tag(sync=True)

    justify_sm = Unicode(default_value=None, allow_none=True).tag(sync=True)

    justify_xl = Unicode(default_value=None, allow_none=True).tag(sync=True)

    justify_xxl = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_gutters = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ScaleTransition(VuetifyWidget):
    _model_name = Unicode("ScaleTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ScrollXReverseTransition(VuetifyWidget):
    _model_name = Unicode("ScrollXReverseTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ScrollXTransition(VuetifyWidget):
    _model_name = Unicode("ScrollXTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ScrollYReverseTransition(VuetifyWidget):
    _model_name = Unicode("ScrollYReverseTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ScrollYTransition(VuetifyWidget):
    _model_name = Unicode("ScrollYTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Select(VuetifyWidget):
    _model_name = Unicode("SelectModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    autofocus = Bool(default_value=None, allow_none=True).tag(sync=True)

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    chips = Bool(default_value=None, allow_none=True).tag(sync=True)

    clear_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    clearable = Bool(default_value=None, allow_none=True).tag(sync=True)

    closable_chips = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    counter = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    counter_value = Float(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hide_no_data = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_selected = Bool(default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_children = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_props = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    menu = Bool(default_value=None, allow_none=True).tag(sync=True)

    menu_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_data_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    open_on_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_counter = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_placeholder = Bool(default_value=None, allow_none=True).tag(sync=True)

    placeholder = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    prepend_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    return_object = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    role = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    single_line = Bool(default_value=None, allow_none=True).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class SelectionControl(VuetifyWidget):
    _model_name = Unicode("SelectionControlModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    defaults_target = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    false_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    false_value = Any().tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    true_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    true_value = Any().tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)


class SelectionControlGroup(VuetifyWidget):
    _model_name = Unicode("SelectionControlGroupModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    defaults_target = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    false_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Bool(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    true_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Sheet(VuetifyWidget):
    _model_name = Unicode("SheetModel").tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class SkeletonLoader(VuetifyWidget):
    _model_name = Unicode("SkeletonLoaderModel").tag(sync=True)

    boilerplate = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    loading = Bool(default_value=None, allow_none=True).tag(sync=True)

    loading_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class SlideGroup(VuetifyWidget):
    _model_name = Unicode("SlideGroupModel").tag(sync=True)

    center_active = Bool(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    max = Float(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_arrows = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    symbol = Any().tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class SlideGroupItem(VuetifyWidget):
    _model_name = Unicode("SlideGroupItemModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)


class SlideXReverseTransition(VuetifyWidget):
    _model_name = Unicode("SlideXReverseTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class SlideXTransition(VuetifyWidget):
    _model_name = Unicode("SlideXTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class SlideYReverseTransition(VuetifyWidget):
    _model_name = Unicode("SlideYReverseTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class SlideYTransition(VuetifyWidget):
    _model_name = Unicode("SlideYTransitionModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    group = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_on_leave = Bool(default_value=None, allow_none=True).tag(sync=True)

    leave_absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    mode = Unicode(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Slider(VuetifyWidget):
    _model_name = Unicode("SliderModel").tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    min = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    show_ticks = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    step = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    thumb_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    thumb_label = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    thumb_size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    tick_size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    ticks = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    track_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    track_fill_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    track_size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)


class Snackbar(VuetifyWidget):
    _model_name = Unicode("SnackbarModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    activator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    activator_props = Dict(default_value=None, allow_none=True).tag(sync=True)

    attach = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    close_on_back = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_on_content_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    contained = Bool(default_value=None, allow_none=True).tag(sync=True)

    content_class = Any().tag(sync=True)

    content_props = Any().tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    multi_line = Bool(default_value=None, allow_none=True).tag(sync=True)

    offset = Union([Unicode(), Float(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    open_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    open_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    timeout = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    transition = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    vertical = Bool(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    z_index = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Spacer(VuetifyWidget):
    _model_name = Unicode("SpacerModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Stepper(VuetifyWidget):
    _model_name = Unicode("StepperModel").tag(sync=True)

    alt_labels = Bool(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    editable = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_actions = Bool(default_value=None, allow_none=True).tag(sync=True)

    item_title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    item_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    max = Float(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    mobile = Bool(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    next_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    non_linear = Bool(default_value=None, allow_none=True).tag(sync=True)

    position = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class StepperActions(VuetifyWidget):
    _model_name = Unicode("StepperActionsModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Union([Bool(), Unicode(), Unicode()], default_value=None, allow_none=True).tag(
        sync=True
    )

    next_text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prev_text = Unicode(default_value=None, allow_none=True).tag(sync=True)


class StepperHeader(VuetifyWidget):
    _model_name = Unicode("StepperHeaderModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class StepperItem(VuetifyWidget):
    _model_name = Unicode("StepperItemModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    complete = Bool(default_value=None, allow_none=True).tag(sync=True)

    complete_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    edit_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    editable = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    icon = Unicode(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    subtitle = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)


class StepperWindow(VuetifyWidget):
    _model_name = Unicode("StepperWindowModel").tag(sync=True)

    continuous = Bool(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    next_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_arrows = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    touch = Any().tag(sync=True)


class StepperWindowItem(VuetifyWidget):
    _model_name = Unicode("StepperWindowItemModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse_transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)


class SvgIcon(VuetifyWidget):
    _model_name = Unicode("SvgIconModel").tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Switch(VuetifyWidget):
    _model_name = Unicode("SwitchModel").tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    defaults_target = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    false_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    false_value = Any().tag(sync=True)

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    indeterminate = Bool(default_value=None, allow_none=True).tag(sync=True)

    inline = Bool(default_value=None, allow_none=True).tag(sync=True)

    inset = Bool(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Bool(default_value=None, allow_none=True).tag(sync=True)

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    true_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    true_value = Any().tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)

    value = Any().tag(sync=True)

    value_comparator = Unicode(default_value=None, allow_none=True).tag(sync=True)


class SystemBar(VuetifyWidget):
    _model_name = Unicode("SystemBarModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    order = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    window = Bool(default_value=None, allow_none=True).tag(sync=True)


class Tab(VuetifyWidget):
    _model_name = Unicode("TabModel").tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    exact = Bool(default_value=None, allow_none=True).tag(sync=True)

    fixed = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_slider = Bool(default_value=None, allow_none=True).tag(sync=True)

    href = Unicode(default_value=None, allow_none=True).tag(sync=True)

    icon = Bool(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    replace = Bool(default_value=None, allow_none=True).tag(sync=True)

    ripple = Union([Bool(), Dict()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    slider_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    stacked = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Table(VuetifyWidget):
    _model_name = Unicode("TableModel").tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    fixed_footer = Bool(default_value=None, allow_none=True).tag(sync=True)

    fixed_header = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Tabs(VuetifyWidget):
    _model_name = Unicode("TabsModel").tag(sync=True)

    align_tabs = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    center_active = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    fixed_tabs = Bool(default_value=None, allow_none=True).tag(sync=True)

    grow = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_slider = Bool(default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    max = Float(default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    multiple = Bool(default_value=None, allow_none=True).tag(sync=True)

    next_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_arrows = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    slider_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    stacked = Bool(default_value=None, allow_none=True).tag(sync=True)

    symbol = Any().tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)


class TextField(VuetifyWidget):
    _model_name = Unicode("TextFieldModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    append_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    autofocus = Bool(default_value=None, allow_none=True).tag(sync=True)

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    clear_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    clearable = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    counter = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    counter_value = Float(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    dirty = Bool(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    persistent_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_counter = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_placeholder = Bool(default_value=None, allow_none=True).tag(sync=True)

    placeholder = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    prepend_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    role = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    single_line = Bool(default_value=None, allow_none=True).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    type = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Textarea(VuetifyWidget):
    _model_name = Unicode("TextareaModel").tag(sync=True)

    active = Bool(default_value=None, allow_none=True).tag(sync=True)

    append_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    append_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    auto_grow = Bool(default_value=None, allow_none=True).tag(sync=True)

    autofocus = Bool(default_value=None, allow_none=True).tag(sync=True)

    base_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    bg_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    center_affix = Bool(default_value=None, allow_none=True).tag(sync=True)

    clear_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    clearable = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    counter = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    counter_value = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    dirty = Bool(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_details = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    hint = Unicode(default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    loading = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_rows = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    no_resize = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_clear = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_counter = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_hint = Bool(default_value=None, allow_none=True).tag(sync=True)

    persistent_placeholder = Bool(default_value=None, allow_none=True).tag(sync=True)

    placeholder = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prefix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    prepend_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    prepend_inner_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    rows = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    single_line = Bool(default_value=None, allow_none=True).tag(sync=True)

    suffix = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ThemeProvider(VuetifyWidget):
    _model_name = Unicode("ThemeProviderModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    with_background = Bool(default_value=None, allow_none=True).tag(sync=True)


class Timeline(VuetifyWidget):
    _model_name = Unicode("TimelineModel").tag(sync=True)

    align = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    justify = Unicode(default_value=None, allow_none=True).tag(sync=True)

    line_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    line_inset = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    line_thickness = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    side = Unicode(default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    truncate_line = Unicode(default_value=None, allow_none=True).tag(sync=True)


class TimelineItem(VuetifyWidget):
    _model_name = Unicode("TimelineItemModel").tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    dot_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    fill_dot = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    hide_dot = Bool(default_value=None, allow_none=True).tag(sync=True)

    hide_opposite = Bool(default_value=None, allow_none=True).tag(sync=True)

    icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    icon_color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    line_inset = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    size = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Toolbar(VuetifyWidget):
    _model_name = Unicode("ToolbarModel").tag(sync=True)

    absolute = Bool(default_value=None, allow_none=True).tag(sync=True)

    border = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    collapse = Bool(default_value=None, allow_none=True).tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    density = Unicode(default_value=None, allow_none=True).tag(sync=True)

    elevation = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    extended = Bool(default_value=None, allow_none=True).tag(sync=True)

    extension_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(
        sync=True
    )

    flat = Bool(default_value=None, allow_none=True).tag(sync=True)

    floating = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    image = Unicode(default_value=None, allow_none=True).tag(sync=True)

    rounded = Union([Unicode(), Float(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    title = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ToolbarItems(VuetifyWidget):
    _model_name = Unicode("ToolbarItemsModel").tag(sync=True)

    color = Unicode(default_value=None, allow_none=True).tag(sync=True)

    variant = Unicode(default_value=None, allow_none=True).tag(sync=True)


class ToolbarTitle(VuetifyWidget):
    _model_name = Unicode("ToolbarTitleModel").tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)


class Tooltip(VuetifyWidget):
    _model_name = Unicode("TooltipModel").tag(sync=True)

    activator = Unicode(default_value=None, allow_none=True).tag(sync=True)

    activator_props = Dict(default_value=None, allow_none=True).tag(sync=True)

    attach = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    close_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    close_on_back = Bool(default_value=None, allow_none=True).tag(sync=True)

    close_on_content_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    contained = Bool(default_value=None, allow_none=True).tag(sync=True)

    content_class = Any().tag(sync=True)

    content_props = Any().tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    id = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location = Unicode(default_value=None, allow_none=True).tag(sync=True)

    location_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Bool(default_value=None, allow_none=True).tag(sync=True)

    no_click_animation = Bool(default_value=None, allow_none=True).tag(sync=True)

    offset = Union([Unicode(), Float(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    open_delay = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    open_on_click = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_focus = Bool(default_value=None, allow_none=True).tag(sync=True)

    open_on_hover = Bool(default_value=None, allow_none=True).tag(sync=True)

    origin = Unicode(default_value=None, allow_none=True).tag(sync=True)

    scrim = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    scroll_strategy = Unicode(default_value=None, allow_none=True).tag(sync=True)

    text = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    z_index = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Validation(VuetifyWidget):
    _model_name = Unicode("ValidationModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    error = Bool(default_value=None, allow_none=True).tag(sync=True)

    error_messages = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(
        sync=True
    )

    focused = Bool(default_value=None, allow_none=True).tag(sync=True)

    label = Unicode(default_value=None, allow_none=True).tag(sync=True)

    max_errors = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    name = Unicode(default_value=None, allow_none=True).tag(sync=True)

    readonly = Bool(default_value=None, allow_none=True).tag(sync=True)

    rules = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    validate_on = Unicode(default_value=None, allow_none=True).tag(sync=True)

    validation_value = Any().tag(sync=True)


class VirtualScroll(VuetifyWidget):
    _model_name = Unicode("VirtualScrollModel").tag(sync=True)

    height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    item_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    items = TList(Any(), default_value=None, allow_none=True).tag(sync=True)

    max_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    max_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_height = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    min_width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)

    renderless = Bool(default_value=None, allow_none=True).tag(sync=True)

    width = Union([Unicode(), Float()], default_value=None, allow_none=True).tag(sync=True)


class Window(VuetifyWidget):
    _model_name = Unicode("WindowModel").tag(sync=True)

    continuous = Bool(default_value=None, allow_none=True).tag(sync=True)

    direction = Unicode(default_value=None, allow_none=True).tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    mandatory = Union([Bool(), Unicode()], default_value=None, allow_none=True).tag(sync=True)

    model_value = Any().tag(sync=True)

    next_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    prev_icon = Union([Unicode(), TList(Any())], default_value=None, allow_none=True).tag(sync=True)

    reverse = Bool(default_value=None, allow_none=True).tag(sync=True)

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    show_arrows = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    tag = Unicode(default_value=None, allow_none=True).tag(sync=True)

    theme = Unicode(default_value=None, allow_none=True).tag(sync=True)

    touch = Any().tag(sync=True)


class WindowItem(VuetifyWidget):
    _model_name = Unicode("WindowItemModel").tag(sync=True)

    disabled = Bool(default_value=None, allow_none=True).tag(sync=True)

    eager = Bool(default_value=None, allow_none=True).tag(sync=True)

    reverse_transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(
        sync=True
    )

    selected_class = Unicode(default_value=None, allow_none=True).tag(sync=True)

    transition = Union([Unicode(), Bool()], default_value=None, allow_none=True).tag(sync=True)

    value = Any().tag(sync=True)


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
    "ColorPicker",
    "Combobox",
    "ComponentIcon",
    "Container",
    "Counter",
    "DataIterator",
    "DataTable",
    "DataTableFooter",
    "DataTableRow",
    "DataTableRows",
    "DataTableServer",
    "DataTableVirtual",
    "DateCard",
    "DatePicker",
    "DatePickerControls",
    "DatePickerHeader",
    "DatePickerMonth",
    "DatePickerYears",
    "DefaultsProvider",
    "Dialog",
    "DialogBottomTransition",
    "DialogTopTransition",
    "DialogTransition",
    "Divider",
    "ExpandTransition",
    "ExpandXTransition",
    "ExpansionPanel",
    "ExpansionPanelText",
    "ExpansionPanelTitle",
    "ExpansionPanels",
    "FabTransition",
    "FadeTransition",
    "Field",
    "FieldLabel",
    "FileInput",
    "Footer",
    "Form",
    "Hover",
    "Icon",
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
    "Menu",
    "Messages",
    "NavigationDrawer",
    "NoSsr",
    "OtpInput",
    "Overlay",
    "Pagination",
    "Parallax",
    "Picker",
    "PickerTitle",
    "ProgressCircular",
    "ProgressLinear",
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
    "Spacer",
    "Stepper",
    "StepperActions",
    "StepperHeader",
    "StepperItem",
    "StepperWindow",
    "StepperWindowItem",
    "SvgIcon",
    "Switch",
    "SystemBar",
    "Tab",
    "Table",
    "Tabs",
    "TextField",
    "Textarea",
    "ThemeProvider",
    "Timeline",
    "TimelineItem",
    "Toolbar",
    "ToolbarItems",
    "ToolbarTitle",
    "Tooltip",
    "Validation",
    "VirtualScroll",
    "Window",
    "WindowItem",
]
