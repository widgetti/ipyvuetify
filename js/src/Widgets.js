import { VuetifyWidgetModel } from "./VuetifyWidget";

export class AlertModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AlertModel",

        title: undefined,
        text: undefined,
        border: undefined,
        border_color: undefined,
        closable: undefined,
        close_icon: undefined,
        type: undefined,
        close_label: undefined,
        icon: undefined,
        model_value: undefined,
        prominent: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        icon_sizes: undefined,
        icon_size: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VAlert";
  }
}

AlertModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class AlertTitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AlertTitleModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VAlertTitle";
  }
}

AlertTitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class AppModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AppModel",

        theme: undefined,
        overlaps: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VApp";
  }
}

AppModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class AppBarModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AppBarModel",

        title: undefined,
        flat: undefined,
        border: undefined,
        model_value: undefined,
        density: undefined,
        height: undefined,
        elevation: undefined,
        location: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        image: undefined,
        collapse: undefined,
        collapse_position: undefined,
        extended: undefined,
        extension_height: undefined,
        floating: undefined,
        order: undefined,
        scroll_target: undefined,
        scroll_threshold: undefined,
        scroll_behavior: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VAppBar";
  }
}

AppBarModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class AppBarNavIconModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AppBarNavIconModel",

        symbol: undefined,
        text: undefined,
        flat: undefined,
        replace: undefined,
        border: undefined,
        icon: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        size: undefined,
        value: undefined,
        active: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        block: undefined,
        readonly: undefined,
        slim: undefined,
        stacked: undefined,
        ripple: undefined,
        selected_class: undefined,
        loading: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VAppBarNavIcon";
  }
}

AppBarNavIconModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class AppBarTitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AppBarTitleModel",

        text: undefined,
        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VAppBarTitle";
  }
}

AppBarTitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class AutocompleteModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AutocompleteModel",

        flat: undefined,
        search: undefined,
        type: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        autocomplete: undefined,
        disabled: undefined,
        multiple: undefined,
        placeholder: undefined,
        id: undefined,
        prefix: undefined,
        role: undefined,
        autofocus: undefined,
        label: undefined,
        menu: undefined,
        items: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        auto_select_first: undefined,
        clear_on_select: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        filter_keys: undefined,
        chips: undefined,
        closable_chips: undefined,
        eager: undefined,
        hide_no_data: undefined,
        hide_selected: undefined,
        bg_color: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        item_type: undefined,
        return_object: undefined,
        value_comparator: undefined,
        menu_icon: undefined,
        no_data_text: undefined,
        open_on_clear: undefined,
        item_color: undefined,
        no_auto_scroll: undefined,
        close_text: undefined,
        open_text: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VAutocomplete";
  }
}

AutocompleteModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class AvatarModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AvatarModel",

        text: undefined,
        border: undefined,
        end: undefined,
        start: undefined,
        icon: undefined,
        density: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        size: undefined,
        image: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VAvatar";
  }
}

AvatarModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class AvatarGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "AvatarGroupModel",

        border: undefined,
        reverse: undefined,
        tag: undefined,
        size: undefined,
        items: undefined,
        item_props: undefined,
        vertical: undefined,
        gap: undefined,
        hoverable: undefined,
        limit: undefined,
        overflow_text: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VAvatarGroup";
  }
}

AvatarGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BadgeModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BadgeModel",

        icon: undefined,
        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        max: undefined,
        label: undefined,
        floating: undefined,
        transition: undefined,
        bordered: undefined,
        content: undefined,
        dot: undefined,
        inline: undefined,
        offset_x: undefined,
        offset_y: undefined,
        text_color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBadge";
  }
}

BadgeModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BannerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BannerModel",

        text: undefined,
        border: undefined,
        icon: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        sticky: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        stacked: undefined,
        bg_color: undefined,
        lines: undefined,
        mobile: undefined,
        avatar: undefined,
        mobile_breakpoint: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBanner";
  }
}

BannerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BannerActionsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BannerActionsModel",

        density: undefined,
        color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBannerActions";
  }
}

BannerActionsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BannerTextModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BannerTextModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBannerText";
  }
}

BannerTextModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BottomNavigationModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BottomNavigationModel",

        border: undefined,
        density: undefined,
        height: undefined,
        elevation: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        mode: undefined,
        order: undefined,
        active: undefined,
        base_color: undefined,
        selected_class: undefined,
        bg_color: undefined,
        mandatory: undefined,
        grow: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBottomNavigation";
  }
}

BottomNavigationModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BottomSheetModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BottomSheetModel",

        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        absolute: undefined,
        theme: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        stick_to_target: undefined,
        viewport_margin: undefined,
        scroll_strategy: undefined,
        retain_focus: undefined,
        capture_focus: undefined,
        transition: undefined,
        attach: undefined,
        inset: undefined,
        fullscreen: undefined,
        scrollable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBottomSheet";
  }
}

BottomSheetModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BreadcrumbsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BreadcrumbsModel",

        icon: undefined,
        density: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        color: undefined,
        disabled: undefined,
        items: undefined,
        active_color: undefined,
        divider: undefined,
        active_class: undefined,
        bg_color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBreadcrumbs";
  }
}

BreadcrumbsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BreadcrumbsDividerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BreadcrumbsDividerModel",

        divider: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBreadcrumbsDivider";
  }
}

BreadcrumbsDividerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BreadcrumbsItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BreadcrumbsItemModel",

        title: undefined,
        replace: undefined,
        max_width: undefined,
        width: undefined,
        tag: undefined,
        color: undefined,
        disabled: undefined,
        active: undefined,
        active_color: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        active_class: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBreadcrumbsItem";
  }
}

BreadcrumbsItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BtnModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BtnModel",

        symbol: undefined,
        text: undefined,
        flat: undefined,
        replace: undefined,
        border: undefined,
        icon: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        size: undefined,
        value: undefined,
        active: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        block: undefined,
        readonly: undefined,
        slim: undefined,
        stacked: undefined,
        ripple: undefined,
        selected_class: undefined,
        loading: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        spaced: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBtn";
  }
}

BtnModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BtnGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BtnGroupModel",

        border: undefined,
        density: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        base_color: undefined,
        direction: undefined,
        divided: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBtnGroup";
  }
}

BtnGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class BtnToggleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "BtnToggleModel",

        border: undefined,
        density: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        base_color: undefined,
        selected_class: undefined,
        mandatory: undefined,
        direction: undefined,
        divided: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VBtnToggle";
  }
}

BtnToggleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CalendarModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CalendarModel",

        end: undefined,
        start: undefined,
        type: undefined,
        model_value: undefined,
        category_days: undefined,
        categories: undefined,
        category_text: undefined,
        max_days: undefined,
        category_hide_dynamic: undefined,
        category_show_all: undefined,
        category_for_invalid: undefined,
        weekdays: undefined,
        first_day_of_week: undefined,
        first_day_of_year: undefined,
        weekday_format: undefined,
        day_format: undefined,
        locale: undefined,
        now: undefined,
        events: undefined,
        event_start: undefined,
        event_end: undefined,
        event_timed: undefined,
        event_category: undefined,
        event_height: undefined,
        event_color: undefined,
        event_text_color: undefined,
        event_name: undefined,
        event_overlap_threshold: undefined,
        event_overlap_mode: undefined,
        event_more: undefined,
        event_more_text: undefined,
        event_ripple: undefined,
        event_margin_bottom: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCalendar";
  }
}

CalendarModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CardModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CardModel",

        title: undefined,
        text: undefined,
        flat: undefined,
        replace: undefined,
        link: undefined,
        border: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        image: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        ripple: undefined,
        loading: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        subtitle: undefined,
        append_avatar: undefined,
        hover: undefined,
        prepend_avatar: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCard";
  }
}

CardModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CardActionsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CardActionsModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCardActions";
  }
}

CardActionsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CardItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CardItemModel",

        title: undefined,
        density: undefined,
        tag: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        subtitle: undefined,
        append_avatar: undefined,
        prepend_avatar: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCardItem";
  }
}

CardItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CardSubtitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CardSubtitleModel",

        tag: undefined,
        opacity: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCardSubtitle";
  }
}

CardSubtitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CardTextModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CardTextModel",

        tag: undefined,
        opacity: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCardText";
  }
}

CardTextModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CardTitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CardTitleModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCardTitle";
  }
}

CardTitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CarouselModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CarouselModel",

        reverse: undefined,
        height: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        disabled: undefined,
        progress: undefined,
        cycle: undefined,
        selected_class: undefined,
        mandatory: undefined,
        direction: undefined,
        interval: undefined,
        delimiter_icon: undefined,
        hide_delimiters: undefined,
        hide_delimiter_background: undefined,
        continuous: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        touch: undefined,
        crossfade: undefined,
        transition_duration: undefined,
        vertical_arrows: undefined,
        vertical_delimiters: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCarousel";
  }
}

CarouselModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CarouselItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CarouselItemModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        position: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        color: undefined,
        alt: undefined,
        disabled: undefined,
        src: undefined,
        value: undefined,
        draggable: undefined,
        selected_class: undefined,
        eager: undefined,
        content_class: undefined,
        transition: undefined,
        options: undefined,
        inline: undefined,
        cover: undefined,
        gradient: undefined,
        image_class: undefined,
        lazy_src: undefined,
        sizes: undefined,
        srcset: undefined,
        aspect_ratio: undefined,
        crossorigin: undefined,
        referrerpolicy: undefined,
        reverse_transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCarouselItem";
  }
}

CarouselItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CheckboxModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CheckboxModel",

        type: undefined,
        error: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        indeterminate: undefined,
        multiple: undefined,
        value: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        ripple: undefined,
        value_comparator: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        indeterminate_icon: undefined,
        true_value: undefined,
        false_value: undefined,
        defaults_target: undefined,
        false_icon: undefined,
        true_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCheckbox";
  }
}

CheckboxModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CheckboxBtnModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CheckboxBtnModel",

        type: undefined,
        error: undefined,
        density: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        indeterminate: undefined,
        multiple: undefined,
        value: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        readonly: undefined,
        ripple: undefined,
        value_comparator: undefined,
        inline: undefined,
        indeterminate_icon: undefined,
        true_value: undefined,
        false_value: undefined,
        defaults_target: undefined,
        false_icon: undefined,
        true_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCheckboxBtn";
  }
}

CheckboxBtnModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ChipModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ChipModel",

        text: undefined,
        filter: undefined,
        replace: undefined,
        link: undefined,
        border: undefined,
        closable: undefined,
        close_icon: undefined,
        close_label: undefined,
        model_value: undefined,
        density: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        size: undefined,
        value: undefined,
        draggable: undefined,
        label: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        ripple: undefined,
        selected_class: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        active_class: undefined,
        append_avatar: undefined,
        prepend_avatar: undefined,
        filter_icon: undefined,
        pill: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VChip";
  }
}

ChipModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ChipGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ChipGroupModel",

        symbol: undefined,
        filter: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        base_color: undefined,
        selected_class: undefined,
        mandatory: undefined,
        value_comparator: undefined,
        scroll_to_active: undefined,
        content_class: undefined,
        direction: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        column: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        center_active: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VChipGroup";
  }
}

ChipGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ClassIconModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ClassIconModel",

        icon: undefined,
        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VClassIcon";
  }
}

ClassIconModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CodeModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CodeModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCode";
  }
}

CodeModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ColModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ColModel",

        tag: undefined,
        order: undefined,
        offset: undefined,
        sm: undefined,
        md: undefined,
        lg: undefined,
        xl: undefined,
        xxl: undefined,
        cols: undefined,
        offset_sm: undefined,
        offset_md: undefined,
        offset_lg: undefined,
        offset_xl: undefined,
        offset_xxl: undefined,
        order_sm: undefined,
        order_md: undefined,
        order_lg: undefined,
        order_xl: undefined,
        order_xxl: undefined,
        align_self: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCol";
  }
}

ColModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ColorInputModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ColorInputModel",

        title: undefined,
        flat: undefined,
        border: undefined,
        type: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        autocomplete: undefined,
        disabled: undefined,
        placeholder: undefined,
        id: undefined,
        prefix: undefined,
        role: undefined,
        autofocus: undefined,
        mode: undefined,
        label: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        bg_color: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
        divided: undefined,
        hide_header: undefined,
        hide_pip: undefined,
        color_pip: undefined,
        pip_icon: undefined,
        pip_location: undefined,
        pip_variant: undefined,
        canvas_height: undefined,
        dot_size: undefined,
        hide_canvas: undefined,
        hide_sliders: undefined,
        hide_inputs: undefined,
        modes: undefined,
        show_swatches: undefined,
        swatches_max_height: undefined,
        landscape: undefined,
        hide_title: undefined,
        hide_eye_dropper: undefined,
        eye_dropper_icon: undefined,
        swatches: undefined,
        cancel_text: undefined,
        ok_text: undefined,
        hide_actions: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VColorInput";
  }
}

ColorInputModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ColorPickerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ColorPickerModel",

        title: undefined,
        border: undefined,
        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        disabled: undefined,
        mode: undefined,
        readonly: undefined,
        bg_color: undefined,
        divided: undefined,
        hide_header: undefined,
        canvas_height: undefined,
        dot_size: undefined,
        hide_canvas: undefined,
        hide_sliders: undefined,
        hide_inputs: undefined,
        modes: undefined,
        show_swatches: undefined,
        swatches_max_height: undefined,
        landscape: undefined,
        hide_title: undefined,
        hide_eye_dropper: undefined,
        eye_dropper_icon: undefined,
        swatches: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VColorPicker";
  }
}

ColorPickerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ComboboxModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ComboboxModel",

        flat: undefined,
        type: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        delimiters: undefined,
        autocomplete: undefined,
        disabled: undefined,
        multiple: undefined,
        placeholder: undefined,
        id: undefined,
        prefix: undefined,
        role: undefined,
        autofocus: undefined,
        label: undefined,
        menu: undefined,
        items: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        auto_select_first: undefined,
        clear_on_select: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        filter_keys: undefined,
        chips: undefined,
        closable_chips: undefined,
        eager: undefined,
        hide_no_data: undefined,
        hide_selected: undefined,
        bg_color: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        item_type: undefined,
        return_object: undefined,
        value_comparator: undefined,
        menu_icon: undefined,
        no_data_text: undefined,
        open_on_clear: undefined,
        item_color: undefined,
        no_auto_scroll: undefined,
        close_text: undefined,
        open_text: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
        always_filter: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCombobox";
  }
}

ComboboxModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CommandPaletteModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CommandPaletteModel",

        search: undefined,
        model_value: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        absolute: undefined,
        theme: undefined,
        disabled: undefined,
        placeholder: undefined,
        items: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        filter_keys: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        stick_to_target: undefined,
        viewport_margin: undefined,
        scroll_strategy: undefined,
        retain_focus: undefined,
        capture_focus: undefined,
        transition: undefined,
        attach: undefined,
        no_data_text: undefined,
        fullscreen: undefined,
        scrollable: undefined,
        input_icon: undefined,
        hotkey: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCommandPalette";
  }
}

CommandPaletteModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CommandPaletteItemComponentModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CommandPaletteItemComponentModel",

        item: undefined,
        index: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCommandPaletteItemComponent";
  }
}

CommandPaletteItemComponentModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ComponentIconModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ComponentIconModel",

        icon: undefined,
        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VComponentIcon";
  }
}

ComponentIconModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ConfirmEditModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ConfirmEditModel",

        color: undefined,
        disabled: undefined,
        cancel_text: undefined,
        ok_text: undefined,
        hide_actions: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VConfirmEdit";
  }
}

ConfirmEditModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ContainerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ContainerModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        tag: undefined,
        fluid: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VContainer";
  }
}

ContainerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class CounterModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "CounterModel",

        disabled: undefined,
        max: undefined,
        value: undefined,
        active: undefined,
        transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VCounter";
  }
}

CounterModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataIteratorModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataIteratorModel",

        search: undefined,
        model_value: undefined,
        tag: undefined,
        items: undefined,
        loading: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        filter_keys: undefined,
        select_strategy: undefined,
        item_value: undefined,
        return_object: undefined,
        value_comparator: undefined,
        transition: undefined,
        items_length: undefined,
        item_selectable: undefined,
        show_select: undefined,
        page: undefined,
        initial_sort_order: undefined,
        sort_by: undefined,
        multi_sort: undefined,
        must_sort: undefined,
        items_per_page: undefined,
        page_by: undefined,
        expand_on_click: undefined,
        show_expand: undefined,
        expanded: undefined,
        group_by: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDataIterator";
  }
}

DataIteratorModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataTableModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataTableModel",

        search: undefined,
        density: undefined,
        height: undefined,
        width: undefined,
        sticky: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        items: undefined,
        loading: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        filter_keys: undefined,
        hide_no_data: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        select_strategy: undefined,
        item_value: undefined,
        return_object: undefined,
        value_comparator: undefined,
        no_data_text: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        hover: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        item_selectable: undefined,
        show_select: undefined,
        page: undefined,
        initial_sort_order: undefined,
        sort_by: undefined,
        multi_sort: undefined,
        must_sort: undefined,
        items_per_page: undefined,
        page_by: undefined,
        expand_on_click: undefined,
        show_expand: undefined,
        expanded: undefined,
        group_by: undefined,
        cell_props: undefined,
        disable_sort: undefined,
        headers: undefined,
        loading_text: undefined,
        group_collapse_icon: undefined,
        group_expand_icon: undefined,
        row_props: undefined,
        hide_default_body: undefined,
        hide_default_footer: undefined,
        hide_default_header: undefined,
        fixed_header: undefined,
        sort_icon: undefined,
        sort_asc_icon: undefined,
        sort_desc_icon: undefined,
        fixed_footer: undefined,
        striped: undefined,
        first_icon: undefined,
        last_icon: undefined,
        items_per_page_text: undefined,
        page_text: undefined,
        first_page_label: undefined,
        prev_page_label: undefined,
        next_page_label: undefined,
        last_page_label: undefined,
        items_per_page_options: undefined,
        show_current_page: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDataTable";
  }
}

DataTableModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataTableFooterModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataTableFooterModel",

        color: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        first_icon: undefined,
        last_icon: undefined,
        items_per_page_text: undefined,
        page_text: undefined,
        first_page_label: undefined,
        prev_page_label: undefined,
        next_page_label: undefined,
        last_page_label: undefined,
        items_per_page_options: undefined,
        show_current_page: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDataTableFooter";
  }
}

DataTableFooterModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataTableHeadersModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataTableHeadersModel",

        density: undefined,
        sticky: undefined,
        color: undefined,
        loading: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        initial_sort_order: undefined,
        multi_sort: undefined,
        disable_sort: undefined,
        fixed_header: undefined,
        sort_icon: undefined,
        sort_asc_icon: undefined,
        sort_desc_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDataTableHeaders";
  }
}

DataTableHeadersModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataTableRowModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataTableRowModel",

        density: undefined,
        color: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        index: undefined,
        cell_props: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDataTableRow";
  }
}

DataTableRowModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataTableRowsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataTableRowsModel",

        density: undefined,
        color: undefined,
        items: undefined,
        loading: undefined,
        hide_no_data: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        no_data_text: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        cell_props: undefined,
        loading_text: undefined,
        group_collapse_icon: undefined,
        group_expand_icon: undefined,
        row_props: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDataTableRows";
  }
}

DataTableRowsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataTableServerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataTableServerModel",

        search: undefined,
        density: undefined,
        height: undefined,
        width: undefined,
        sticky: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        items: undefined,
        loading: undefined,
        hide_no_data: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        select_strategy: undefined,
        item_value: undefined,
        return_object: undefined,
        value_comparator: undefined,
        no_data_text: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        hover: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        items_length: undefined,
        item_selectable: undefined,
        show_select: undefined,
        page: undefined,
        initial_sort_order: undefined,
        sort_by: undefined,
        multi_sort: undefined,
        must_sort: undefined,
        items_per_page: undefined,
        page_by: undefined,
        expand_on_click: undefined,
        show_expand: undefined,
        expanded: undefined,
        group_by: undefined,
        cell_props: undefined,
        disable_sort: undefined,
        headers: undefined,
        loading_text: undefined,
        group_collapse_icon: undefined,
        group_expand_icon: undefined,
        row_props: undefined,
        hide_default_body: undefined,
        hide_default_footer: undefined,
        hide_default_header: undefined,
        fixed_header: undefined,
        sort_icon: undefined,
        sort_asc_icon: undefined,
        sort_desc_icon: undefined,
        fixed_footer: undefined,
        striped: undefined,
        first_icon: undefined,
        last_icon: undefined,
        items_per_page_text: undefined,
        page_text: undefined,
        first_page_label: undefined,
        prev_page_label: undefined,
        next_page_label: undefined,
        last_page_label: undefined,
        items_per_page_options: undefined,
        show_current_page: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDataTableServer";
  }
}

DataTableServerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataTableVirtualModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataTableVirtualModel",

        search: undefined,
        density: undefined,
        height: undefined,
        width: undefined,
        sticky: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        items: undefined,
        loading: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        filter_keys: undefined,
        hide_no_data: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        select_strategy: undefined,
        item_value: undefined,
        return_object: undefined,
        value_comparator: undefined,
        no_data_text: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        hover: undefined,
        item_selectable: undefined,
        show_select: undefined,
        initial_sort_order: undefined,
        sort_by: undefined,
        multi_sort: undefined,
        must_sort: undefined,
        expand_on_click: undefined,
        show_expand: undefined,
        expanded: undefined,
        group_by: undefined,
        cell_props: undefined,
        disable_sort: undefined,
        headers: undefined,
        loading_text: undefined,
        group_collapse_icon: undefined,
        group_expand_icon: undefined,
        row_props: undefined,
        hide_default_body: undefined,
        hide_default_header: undefined,
        fixed_header: undefined,
        sort_icon: undefined,
        sort_asc_icon: undefined,
        sort_desc_icon: undefined,
        fixed_footer: undefined,
        striped: undefined,
        item_height: undefined,
        item_key: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDataTableVirtual";
  }
}

DataTableVirtualModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DateInputModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DateInputModel",

        title: undefined,
        text: undefined,
        flat: undefined,
        border: undefined,
        type: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        autocomplete: undefined,
        disabled: undefined,
        multiple: undefined,
        placeholder: undefined,
        id: undefined,
        prefix: undefined,
        role: undefined,
        autofocus: undefined,
        header: undefined,
        label: undefined,
        menu: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        bg_color: undefined,
        transition: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        divided: undefined,
        weekdays: undefined,
        first_day_of_week: undefined,
        first_day_of_year: undefined,
        weekday_format: undefined,
        month: undefined,
        events: undefined,
        event_color: undefined,
        year: undefined,
        show_week: undefined,
        hide_header: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        reverse_transition: undefined,
        landscape: undefined,
        hide_title: undefined,
        cancel_text: undefined,
        ok_text: undefined,
        hide_actions: undefined,
        display_format: undefined,
        update_on: undefined,
        header_color: undefined,
        header_date_format: undefined,
        landscape_header_width: undefined,
        control_height: undefined,
        control_variant: undefined,
        no_month_picker: undefined,
        mode_icon: undefined,
        view_mode: undefined,
        hide_weekdays: undefined,
        show_adjacent_months: undefined,
        weeks_in_month: undefined,
        allowed_dates: undefined,
        allowed_months: undefined,
        allowed_years: undefined,
        input_format: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDateInput";
  }
}

DateInputModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DatePickerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DatePickerModel",

        title: undefined,
        text: undefined,
        border: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        disabled: undefined,
        multiple: undefined,
        header: undefined,
        readonly: undefined,
        bg_color: undefined,
        transition: undefined,
        divided: undefined,
        weekdays: undefined,
        first_day_of_week: undefined,
        first_day_of_year: undefined,
        weekday_format: undefined,
        month: undefined,
        events: undefined,
        event_color: undefined,
        year: undefined,
        show_week: undefined,
        hide_header: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        reverse_transition: undefined,
        landscape: undefined,
        hide_title: undefined,
        header_color: undefined,
        header_date_format: undefined,
        landscape_header_width: undefined,
        control_height: undefined,
        control_variant: undefined,
        no_month_picker: undefined,
        mode_icon: undefined,
        view_mode: undefined,
        hide_weekdays: undefined,
        show_adjacent_months: undefined,
        weeks_in_month: undefined,
        allowed_dates: undefined,
        allowed_months: undefined,
        allowed_years: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "IpyvuetifyDatePicker";
  }
}

DatePickerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DatePickerControlsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DatePickerControlsModel",

        text: undefined,
        disabled: undefined,
        active: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        control_height: undefined,
        control_variant: undefined,
        no_month_picker: undefined,
        mode_icon: undefined,
        month_text: undefined,
        year_text: undefined,
        view_mode: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDatePickerControls";
  }
}

DatePickerControlsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DatePickerHeaderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DatePickerHeaderModel",

        color: undefined,
        header: undefined,
        append_icon: undefined,
        transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDatePickerHeader";
  }
}

DatePickerHeaderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DatePickerMonthModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DatePickerMonthModel",

        color: undefined,
        disabled: undefined,
        multiple: undefined,
        readonly: undefined,
        transition: undefined,
        weekdays: undefined,
        first_day_of_week: undefined,
        first_day_of_year: undefined,
        weekday_format: undefined,
        month: undefined,
        events: undefined,
        event_color: undefined,
        year: undefined,
        show_week: undefined,
        reverse_transition: undefined,
        hide_weekdays: undefined,
        show_adjacent_months: undefined,
        weeks_in_month: undefined,
        allowed_dates: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDatePickerMonth";
  }
}

DatePickerMonthModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DatePickerMonthsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DatePickerMonthsModel",

        model_value: undefined,
        height: undefined,
        color: undefined,
        year: undefined,
        allowed_months: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDatePickerMonths";
  }
}

DatePickerMonthsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DatePickerYearsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DatePickerYearsModel",

        model_value: undefined,
        height: undefined,
        color: undefined,
        allowed_years: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDatePickerYears";
  }
}

DatePickerYearsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DefaultsProviderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DefaultsProviderModel",

        disabled: undefined,
        reset: undefined,
        root: undefined,
        scoped: undefined,
        defaults: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDefaultsProvider";
  }
}

DefaultsProviderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DialogModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DialogModel",

        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        absolute: undefined,
        theme: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        stick_to_target: undefined,
        viewport_margin: undefined,
        scroll_strategy: undefined,
        retain_focus: undefined,
        capture_focus: undefined,
        transition: undefined,
        attach: undefined,
        fullscreen: undefined,
        scrollable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDialog";
  }
}

DialogModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DialogBottomTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DialogBottomTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDialogBottomTransition";
  }
}

DialogBottomTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DialogTopTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DialogTopTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDialogTopTransition";
  }
}

DialogTopTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DialogTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DialogTransitionModel",

        target: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDialogTransition";
  }
}

DialogTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DividerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DividerModel",

        length: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        opacity: undefined,
        vertical: undefined,
        inset: undefined,
        gradient: undefined,
        thickness: undefined,
        content_offset: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VDivider";
  }
}

DividerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class EmptyStateModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "EmptyStateModel",

        title: undefined,
        text: undefined,
        icon: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        theme: undefined,
        color: undefined,
        size: undefined,
        image: undefined,
        href: undefined,
        to: undefined,
        bg_color: undefined,
        headline: undefined,
        action_text: undefined,
        justify: undefined,
        text_width: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VEmptyState";
  }
}

EmptyStateModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ExpandBothTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ExpandBothTransitionModel",
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VExpandBothTransition";
  }
}

ExpandBothTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ExpandTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ExpandTransitionModel",

        disabled: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VExpandTransition";
  }
}

ExpandTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ExpandXTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ExpandXTransitionModel",

        disabled: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VExpandXTransition";
  }
}

ExpandXTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ExpansionPanelModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ExpansionPanelModel",

        title: undefined,
        text: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        static: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        color: undefined,
        disabled: undefined,
        value: undefined,
        readonly: undefined,
        ripple: undefined,
        selected_class: undefined,
        eager: undefined,
        bg_color: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        hide_actions: undefined,
        focusable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VExpansionPanel";
  }
}

ExpansionPanelModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ExpansionPanelTextModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ExpansionPanelTextModel",

        eager: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VExpansionPanelText";
  }
}

ExpansionPanelTextModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ExpansionPanelTitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ExpansionPanelTitleModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        static: undefined,
        color: undefined,
        readonly: undefined,
        ripple: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        hide_actions: undefined,
        focusable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VExpansionPanelTitle";
  }
}

ExpansionPanelTitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ExpansionPanelsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ExpansionPanelsModel",

        flat: undefined,
        elevation: undefined,
        static: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        readonly: undefined,
        ripple: undefined,
        selected_class: undefined,
        eager: undefined,
        bg_color: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        mandatory: undefined,
        hide_actions: undefined,
        focusable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VExpansionPanels";
  }
}

ExpansionPanelsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FabModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FabModel",

        symbol: undefined,
        text: undefined,
        flat: undefined,
        replace: undefined,
        border: undefined,
        icon: undefined,
        model_value: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        disabled: undefined,
        size: undefined,
        value: undefined,
        layout: undefined,
        extended: undefined,
        order: undefined,
        active: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        block: undefined,
        readonly: undefined,
        slim: undefined,
        stacked: undefined,
        ripple: undefined,
        selected_class: undefined,
        loading: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        offset: undefined,
        transition: undefined,
        app: undefined,
        appear: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFab";
  }
}

FabModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FabTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FabTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFabTransition";
  }
}

FabTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FadeTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FadeTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFadeTransition";
  }
}

FadeTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FieldModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FieldModel",

        flat: undefined,
        error: undefined,
        reverse: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        id: undefined,
        details: undefined,
        label: undefined,
        active: undefined,
        base_color: undefined,
        loading: undefined,
        bg_color: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        focused: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        label_id: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VField";
  }
}

FieldModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FieldLabelModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FieldLabelModel",

        floating: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFieldLabel";
  }
}

FieldLabelModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FileInputModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FileInputModel",

        flat: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        disabled: undefined,
        multiple: undefined,
        id: undefined,
        label: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        chips: undefined,
        bg_color: undefined,
        counter: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_size_string: undefined,
        counter_string: undefined,
        hide_input: undefined,
        show_size: undefined,
        truncate_length: undefined,
        filter_by_type: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFileInput";
  }
}

FileInputModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FileUploadModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FileUploadModel",

        title: undefined,
        icon: undefined,
        model_value: undefined,
        error: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        multiple: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        subtitle: undefined,
        scrim: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        clearable: undefined,
        show_size: undefined,
        filter_by_type: undefined,
        browse_text: undefined,
        divider_text: undefined,
        inset_file_list: undefined,
        hide_browse: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFileUpload";
  }
}

FileUploadModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FileUploadDropzoneModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FileUploadDropzoneModel",

        title: undefined,
        length: undefined,
        border: undefined,
        icon: undefined,
        model_value: undefined,
        error: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        disabled: undefined,
        multiple: undefined,
        subtitle: undefined,
        opacity: undefined,
        scrim: undefined,
        close_delay: undefined,
        open_delay: undefined,
        clearable: undefined,
        thickness: undefined,
        show_size: undefined,
        browse_text: undefined,
        divider_text: undefined,
        inset_file_list: undefined,
        hide_browse: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFileUploadDropzone";
  }
}

FileUploadDropzoneModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FileUploadItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FileUploadItemModel",

        title: undefined,
        replace: undefined,
        link: undefined,
        border: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        value: undefined,
        nav: undefined,
        active: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        slim: undefined,
        ripple: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        subtitle: undefined,
        active_class: undefined,
        lines: undefined,
        prepend_gap: undefined,
        clearable: undefined,
        append_avatar: undefined,
        prepend_avatar: undefined,
        index: undefined,
        show_size: undefined,
        file: undefined,
        file_icon: undefined,
        tabindex: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFileUploadItem";
  }
}

FileUploadItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FileUploadListModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FileUploadListModel",

        border: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        activated: undefined,
        disabled: undefined,
        files: undefined,
        nav: undefined,
        items: undefined,
        active_color: undefined,
        base_color: undefined,
        slim: undefined,
        active_class: undefined,
        bg_color: undefined,
        filterable: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        lines: undefined,
        prepend_gap: undefined,
        indent: undefined,
        navigation_strategy: undefined,
        navigation_index: undefined,
        activatable: undefined,
        selectable: undefined,
        opened: undefined,
        selected: undefined,
        mandatory: undefined,
        items_registration: undefined,
        active_strategy: undefined,
        select_strategy: undefined,
        open_strategy: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        item_type: undefined,
        return_object: undefined,
        value_comparator: undefined,
        clearable: undefined,
        show_size: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFileUploadList";
  }
}

FileUploadListModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FooterModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FooterModel",

        border: undefined,
        height: undefined,
        elevation: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        order: undefined,
        app: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VFooter";
  }
}

FooterModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FormModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FormModel",

        model_value: undefined,
        disabled: undefined,
        readonly: undefined,
        validate_on: undefined,
        fast_fail: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VForm";
  }
}

FormModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class HotkeyModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "HotkeyModel",

        keys: undefined,
        border: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        prefix: undefined,
        suffix: undefined,
        inline: undefined,
        display_mode: undefined,
        platform: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VHotkey";
  }
}

HotkeyModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class HoverModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "HoverModel",

        model_value: undefined,
        disabled: undefined,
        close_delay: undefined,
        open_delay: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VHover";
  }
}

HoverModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class IconModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "IconModel",

        end: undefined,
        start: undefined,
        icon: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        disabled: undefined,
        size: undefined,
        opacity: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VIcon";
  }
}

IconModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class IconBtnModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "IconBtnModel",

        text: undefined,
        border: undefined,
        icon: undefined,
        height: undefined,
        width: undefined,
        elevation: undefined,
        icon_sizes: undefined,
        icon_size: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        size: undefined,
        active: undefined,
        active_color: undefined,
        readonly: undefined,
        loading: undefined,
        opacity: undefined,
        icon_color: undefined,
        sizes: undefined,
        base_variant: undefined,
        hide_overlay: undefined,
        rotate: undefined,
        active_icon: undefined,
        active_variant: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VIconBtn";
  }
}

IconBtnModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ImgModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ImgModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        position: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        color: undefined,
        alt: undefined,
        src: undefined,
        draggable: undefined,
        eager: undefined,
        content_class: undefined,
        transition: undefined,
        options: undefined,
        inline: undefined,
        cover: undefined,
        gradient: undefined,
        image_class: undefined,
        lazy_src: undefined,
        sizes: undefined,
        srcset: undefined,
        aspect_ratio: undefined,
        crossorigin: undefined,
        referrerpolicy: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VImg";
  }
}

ImgModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class InfiniteScrollModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "InfiniteScrollModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        tag: undefined,
        color: undefined,
        mode: undefined,
        direction: undefined,
        side: undefined,
        margin: undefined,
        load_more_text: undefined,
        empty_text: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VInfiniteScroll";
  }
}

InfiniteScrollModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class InputModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "InputModel",

        error: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VInput";
  }
}

InputModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ItemModel",

        disabled: undefined,
        value: undefined,
        selected_class: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VItem";
  }
}

ItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ItemGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ItemGroupModel",

        tag: undefined,
        theme: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        selected_class: undefined,
        mandatory: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VItemGroup";
  }
}

ItemGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class KbdModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "KbdModel",

        border: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VKbd";
  }
}

KbdModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class LabelModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "LabelModel",

        text: undefined,
        theme: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VLabel";
  }
}

LabelModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class LayoutModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "LayoutModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        full_height: undefined,
        overlaps: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VLayout";
  }
}

LayoutModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class LayoutItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "LayoutItemModel",

        model_value: undefined,
        position: undefined,
        absolute: undefined,
        name: undefined,
        size: undefined,
        order: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VLayoutItem";
  }
}

LayoutItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class LazyModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "LazyModel",

        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        tag: undefined,
        transition: undefined,
        options: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VLazy";
  }
}

LazyModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class LigatureIconModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "LigatureIconModel",

        icon: undefined,
        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VLigatureIcon";
  }
}

LigatureIconModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListModel",

        border: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        nav: undefined,
        items: undefined,
        active_color: undefined,
        base_color: undefined,
        slim: undefined,
        active_class: undefined,
        bg_color: undefined,
        filterable: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        lines: undefined,
        prepend_gap: undefined,
        indent: undefined,
        navigation_strategy: undefined,
        navigation_index: undefined,
        activatable: undefined,
        selectable: undefined,
        mandatory: undefined,
        items_registration: undefined,
        active_strategy: undefined,
        select_strategy: undefined,
        open_strategy: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        item_type: undefined,
        return_object: undefined,
        value_comparator: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VList";
  }
}

ListModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListGroupModel",

        title: undefined,
        tag: undefined,
        color: undefined,
        disabled: undefined,
        value: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        fluid: undefined,
        raw_id: undefined,
        subgroup: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VListGroup";
  }
}

ListGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListImgModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListImgModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VListImg";
  }
}

ListImgModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListItemModel",

        title: undefined,
        replace: undefined,
        link: undefined,
        border: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        value: undefined,
        nav: undefined,
        active: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        slim: undefined,
        ripple: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        subtitle: undefined,
        active_class: undefined,
        lines: undefined,
        prepend_gap: undefined,
        append_avatar: undefined,
        prepend_avatar: undefined,
        index: undefined,
        tabindex: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VListItem";
  }
}

ListItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListItemActionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListItemActionModel",

        end: undefined,
        start: undefined,
        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VListItemAction";
  }
}

ListItemActionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListItemMediaModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListItemMediaModel",

        end: undefined,
        start: undefined,
        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VListItemMedia";
  }
}

ListItemMediaModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListItemSubtitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListItemSubtitleModel",

        tag: undefined,
        opacity: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VListItemSubtitle";
  }
}

ListItemSubtitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListItemTitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListItemTitleModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VListItemTitle";
  }
}

ListItemTitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ListSubheaderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ListSubheaderModel",

        title: undefined,
        sticky: undefined,
        tag: undefined,
        color: undefined,
        inset: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VListSubheader";
  }
}

ListSubheaderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class LocaleProviderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "LocaleProviderModel",

        locale: undefined,
        rtl: undefined,
        fallback_locale: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VLocaleProvider";
  }
}

LocaleProviderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class MainModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "MainModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        tag: undefined,
        scrollable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VMain";
  }
}

MainModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class MaskInputModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "MaskInputModel",

        flat: undefined,
        type: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        autocomplete: undefined,
        disabled: undefined,
        placeholder: undefined,
        id: undefined,
        prefix: undefined,
        role: undefined,
        autofocus: undefined,
        label: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        bg_color: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
        mask: undefined,
        return_masked_value: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VMaskInput";
  }
}

MaskInputModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class MenuModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "MenuModel",

        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        theme: undefined,
        disabled: undefined,
        id: undefined,
        eager: undefined,
        activator: undefined,
        submenu: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        stick_to_target: undefined,
        viewport_margin: undefined,
        scroll_strategy: undefined,
        retain_focus: undefined,
        capture_focus: undefined,
        disable_initial_focus: undefined,
        transition: undefined,
        attach: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VMenu";
  }
}

MenuModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class MessagesModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "MessagesModel",

        color: undefined,
        active: undefined,
        transition: undefined,
        messages: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VMessages";
  }
}

MessagesModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class NavigationDrawerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "NavigationDrawerModel",

        border: undefined,
        model_value: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        absolute: undefined,
        sticky: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        image: undefined,
        floating: undefined,
        order: undefined,
        persistent: undefined,
        scrim: undefined,
        close_delay: undefined,
        open_delay: undefined,
        retain_focus: undefined,
        capture_focus: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        disable_resize_watcher: undefined,
        disable_route_watcher: undefined,
        expand_on_hover: undefined,
        permanent: undefined,
        rail: undefined,
        rail_width: undefined,
        temporary: undefined,
        touchless: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VNavigationDrawer";
  }
}

NavigationDrawerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class NoSsrModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "NoSsrModel",
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VNoSsr";
  }
}

NoSsrModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class NumberInputModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "NumberInputModel",

        flat: undefined,
        type: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        autocomplete: undefined,
        disabled: undefined,
        max: undefined,
        min: undefined,
        placeholder: undefined,
        step: undefined,
        id: undefined,
        prefix: undefined,
        role: undefined,
        autofocus: undefined,
        label: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        bg_color: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
        inset: undefined,
        decimal_separator: undefined,
        control_variant: undefined,
        hide_input: undefined,
        precision: undefined,
        min_fraction_digits: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VNumberInput";
  }
}

NumberInputModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class OtpInputModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "OtpInputModel",

        length: undefined,
        type: undefined,
        model_value: undefined,
        error: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        placeholder: undefined,
        autofocus: undefined,
        label: undefined,
        base_color: undefined,
        loading: undefined,
        divider: undefined,
        bg_color: undefined,
        focused: undefined,
        focus_all: undefined,
        masked: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VOtpInput";
  }
}

OtpInputModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class OverlayModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "OverlayModel",

        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        absolute: undefined,
        theme: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        stick_to_target: undefined,
        viewport_margin: undefined,
        scroll_strategy: undefined,
        retain_focus: undefined,
        capture_focus: undefined,
        transition: undefined,
        attach: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VOverlay";
  }
}

OverlayModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class PaginationModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "PaginationModel",

        length: undefined,
        border: undefined,
        start: undefined,
        model_value: undefined,
        density: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        size: undefined,
        aria_label: undefined,
        active_color: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        first_icon: undefined,
        last_icon: undefined,
        total_visible: undefined,
        page_aria_label: undefined,
        current_page_aria_label: undefined,
        first_aria_label: undefined,
        previous_aria_label: undefined,
        next_aria_label: undefined,
        last_aria_label: undefined,
        ellipsis: undefined,
        show_first_last_page: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VPagination";
  }
}

PaginationModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ParallaxModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ParallaxModel",

        scale: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VParallax";
  }
}

ParallaxModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class PickerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "PickerModel",

        title: undefined,
        border: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        bg_color: undefined,
        divided: undefined,
        hide_header: undefined,
        landscape: undefined,
        hide_title: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VPicker";
  }
}

PickerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class PickerTitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "PickerTitleModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VPickerTitle";
  }
}

PickerTitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class PieModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "PieModel",

        title: undefined,
        density: undefined,
        rounded: undefined,
        size: undefined,
        legend: undefined,
        items: undefined,
        bg_color: undefined,
        item_title: undefined,
        item_value: undefined,
        gap: undefined,
        item_key: undefined,
        rotate: undefined,
        tooltip: undefined,
        palette: undefined,
        gauge_cut: undefined,
        inner_cut: undefined,
        hover_scale: undefined,
        animation: undefined,
        hide_slice: undefined,
        reveal: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VPie";
  }
}

PieModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class PieSegmentModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "PieSegmentModel",

        rounded: undefined,
        color: undefined,
        pattern: undefined,
        value: undefined,
        active: undefined,
        gap: undefined,
        rotate: undefined,
        inner_cut: undefined,
        hover_scale: undefined,
        animation: undefined,
        hide_slice: undefined,
        reveal: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VPieSegment";
  }
}

PieSegmentModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class PieTooltipModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "PieTooltipModel",

        model_value: undefined,
        item: undefined,
        target: undefined,
        offset: undefined,
        transition: undefined,
        title_format: undefined,
        subtitle_format: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VPieTooltip";
  }
}

PieTooltipModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ProgressCircularModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ProgressCircularModel",

        model_value: undefined,
        width: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        indeterminate: undefined,
        size: undefined,
        bg_color: undefined,
        rotate: undefined,
        reveal: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VProgressCircular";
  }
}

ProgressCircularModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ProgressLinearModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ProgressLinearModel",

        model_value: undefined,
        reverse: undefined,
        height: undefined,
        location: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        indeterminate: undefined,
        max: undefined,
        active: undefined,
        bg_color: undefined,
        opacity: undefined,
        striped: undefined,
        stream: undefined,
        bg_opacity: undefined,
        buffer_value: undefined,
        buffer_color: undefined,
        buffer_opacity: undefined,
        clickable: undefined,
        rounded_bar: undefined,
        chunk_count: undefined,
        chunk_width: undefined,
        chunk_gap: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VProgressLinear";
  }
}

ProgressLinearModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class PullToRefreshModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "PullToRefreshModel",

        disabled: undefined,
        pull_down_threshold: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VPullToRefresh";
  }
}

PullToRefreshModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class RadioModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "RadioModel",

        type: undefined,
        model_value: undefined,
        error: undefined,
        density: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        multiple: undefined,
        value: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        readonly: undefined,
        ripple: undefined,
        value_comparator: undefined,
        inline: undefined,
        true_value: undefined,
        false_value: undefined,
        defaults_target: undefined,
        false_icon: undefined,
        true_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VRadio";
  }
}

RadioModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class RadioGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "RadioGroupModel",

        type: undefined,
        error: undefined,
        density: undefined,
        height: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        ripple: undefined,
        value_comparator: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        inline: undefined,
        defaults_target: undefined,
        false_icon: undefined,
        true_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VRadioGroup";
  }
}

RadioGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class RangeSliderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "RangeSliderModel",

        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        max: undefined,
        min: undefined,
        step: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        ripple: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        thumb_color: undefined,
        thumb_label: undefined,
        thumb_size: undefined,
        show_ticks: undefined,
        ticks: undefined,
        tick_size: undefined,
        track_color: undefined,
        track_fill_color: undefined,
        track_size: undefined,
        no_keyboard: undefined,
        strict: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VRangeSlider";
  }
}

RangeSliderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class RatingModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "RatingModel",

        length: undefined,
        model_value: undefined,
        density: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        size: undefined,
        active_color: undefined,
        readonly: undefined,
        ripple: undefined,
        clearable: undefined,
        hover: undefined,
        item_aria_label: undefined,
        empty_icon: undefined,
        full_icon: undefined,
        half_increments: undefined,
        item_label_position: undefined,
        item_labels: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VRating";
  }
}

RatingModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ResponsiveModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ResponsiveModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        content_class: undefined,
        inline: undefined,
        aspect_ratio: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VResponsive";
  }
}

ResponsiveModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class RowModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "RowModel",

        tag: undefined,
        align: undefined,
        justify: undefined,
        dense: undefined,
        no_gutters: undefined,
        align_sm: undefined,
        align_md: undefined,
        align_lg: undefined,
        align_xl: undefined,
        align_xxl: undefined,
        justify_sm: undefined,
        justify_md: undefined,
        justify_lg: undefined,
        justify_xl: undefined,
        justify_xxl: undefined,
        align_content_sm: undefined,
        align_content_md: undefined,
        align_content_lg: undefined,
        align_content_xl: undefined,
        align_content_xxl: undefined,
        align_content: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VRow";
  }
}

RowModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ScaleTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ScaleTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VScaleTransition";
  }
}

ScaleTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ScrollXReverseTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ScrollXReverseTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VScrollXReverseTransition";
  }
}

ScrollXReverseTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ScrollXTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ScrollXTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VScrollXTransition";
  }
}

ScrollXTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ScrollYReverseTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ScrollYReverseTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VScrollYReverseTransition";
  }
}

ScrollYReverseTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ScrollYTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ScrollYTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VScrollYTransition";
  }
}

ScrollYTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SelectModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SelectModel",

        flat: undefined,
        search: undefined,
        type: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        autocomplete: undefined,
        disabled: undefined,
        multiple: undefined,
        placeholder: undefined,
        id: undefined,
        prefix: undefined,
        role: undefined,
        autofocus: undefined,
        label: undefined,
        menu: undefined,
        items: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        filter_keys: undefined,
        chips: undefined,
        closable_chips: undefined,
        eager: undefined,
        hide_no_data: undefined,
        hide_selected: undefined,
        bg_color: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        item_type: undefined,
        return_object: undefined,
        value_comparator: undefined,
        menu_icon: undefined,
        transition: undefined,
        no_data_text: undefined,
        open_on_clear: undefined,
        item_color: undefined,
        no_auto_scroll: undefined,
        close_text: undefined,
        open_text: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSelect";
  }
}

SelectModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SelectionControlModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SelectionControlModel",

        type: undefined,
        error: undefined,
        density: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        multiple: undefined,
        value: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        readonly: undefined,
        ripple: undefined,
        value_comparator: undefined,
        inline: undefined,
        true_value: undefined,
        false_value: undefined,
        defaults_target: undefined,
        false_icon: undefined,
        true_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSelectionControl";
  }
}

SelectionControlModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SelectionControlGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SelectionControlGroupModel",

        type: undefined,
        error: undefined,
        density: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        multiple: undefined,
        id: undefined,
        readonly: undefined,
        ripple: undefined,
        value_comparator: undefined,
        inline: undefined,
        defaults_target: undefined,
        false_icon: undefined,
        true_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSelectionControlGroup";
  }
}

SelectionControlGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SheetModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SheetModel",

        border: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSheet";
  }
}

SheetModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SkeletonLoaderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SkeletonLoaderModel",

        type: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        theme: undefined,
        color: undefined,
        loading: undefined,
        loading_text: undefined,
        boilerplate: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSkeletonLoader";
  }
}

SkeletonLoaderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SlideGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SlideGroupModel",

        symbol: undefined,
        tag: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        selected_class: undefined,
        mandatory: undefined,
        scroll_to_active: undefined,
        content_class: undefined,
        direction: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        center_active: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSlideGroup";
  }
}

SlideGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SlideGroupItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SlideGroupItemModel",

        disabled: undefined,
        value: undefined,
        selected_class: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSlideGroupItem";
  }
}

SlideGroupItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SlideXReverseTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SlideXReverseTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSlideXReverseTransition";
  }
}

SlideXReverseTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SlideXTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SlideXTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSlideXTransition";
  }
}

SlideXTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SlideYReverseTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SlideYReverseTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSlideYReverseTransition";
  }
}

SlideYReverseTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SlideYTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SlideYTransitionModel",

        disabled: undefined,
        mode: undefined,
        origin: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSlideYTransition";
  }
}

SlideYTransitionModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SliderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SliderModel",

        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        max: undefined,
        min: undefined,
        step: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        ripple: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        thumb_color: undefined,
        thumb_label: undefined,
        thumb_size: undefined,
        show_ticks: undefined,
        ticks: undefined,
        tick_size: undefined,
        track_color: undefined,
        track_fill_color: undefined,
        track_size: undefined,
        no_keyboard: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSlider";
  }
}

SliderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SnackbarModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SnackbarModel",

        text: undefined,
        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        position: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        transition: undefined,
        attach: undefined,
        vertical: undefined,
        multi_line: undefined,
        timer: undefined,
        timeout: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSnackbar";
  }
}

SnackbarModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SnackbarQueueModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SnackbarQueueModel",

        text: undefined,
        closable: undefined,
        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        position: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        transition: undefined,
        attach: undefined,
        close_text: undefined,
        vertical: undefined,
        multi_line: undefined,
        timer: undefined,
        timeout: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSnackbarQueue";
  }
}

SnackbarQueueModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SpacerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SpacerModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSpacer";
  }
}

SpacerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SparklineModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SparklineModel",

        type: undefined,
        model_value: undefined,
        fill: undefined,
        height: undefined,
        width: undefined,
        color: undefined,
        labels: undefined,
        max: undefined,
        min: undefined,
        id: undefined,
        item_value: undefined,
        gradient: undefined,
        auto_line_width: undefined,
        auto_draw: undefined,
        auto_draw_duration: undefined,
        auto_draw_easing: undefined,
        gradient_direction: undefined,
        label_size: undefined,
        line_width: undefined,
        padding: undefined,
        show_labels: undefined,
        smooth: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSparkline";
  }
}

SparklineModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SpeedDialModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SpeedDialModel",

        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        theme: undefined,
        disabled: undefined,
        id: undefined,
        eager: undefined,
        activator: undefined,
        submenu: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        stick_to_target: undefined,
        viewport_margin: undefined,
        scroll_strategy: undefined,
        retain_focus: undefined,
        capture_focus: undefined,
        disable_initial_focus: undefined,
        transition: undefined,
        attach: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSpeedDial";
  }
}

SpeedDialModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperModel",

        flat: undefined,
        border: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        items: undefined,
        selected_class: undefined,
        bg_color: undefined,
        mandatory: undefined,
        item_title: undefined,
        item_value: undefined,
        item_props: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        hide_actions: undefined,
        alt_labels: undefined,
        complete_icon: undefined,
        edit_icon: undefined,
        editable: undefined,
        error_icon: undefined,
        non_linear: undefined,
        prev_text: undefined,
        next_text: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepper";
  }
}

StepperModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperActionsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperActionsModel",

        color: undefined,
        disabled: undefined,
        prev_text: undefined,
        next_text: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepperActions";
  }
}

StepperActionsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperHeaderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperHeaderModel",

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepperHeader";
  }
}

StepperHeaderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperItemModel",

        title: undefined,
        icon: undefined,
        error: undefined,
        color: undefined,
        disabled: undefined,
        value: undefined,
        ripple: undefined,
        selected_class: undefined,
        subtitle: undefined,
        rules: undefined,
        complete_icon: undefined,
        edit_icon: undefined,
        editable: undefined,
        error_icon: undefined,
        complete: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepperItem";
  }
}

StepperItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperVerticalModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperVerticalModel",

        flat: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        items: undefined,
        readonly: undefined,
        ripple: undefined,
        selected_class: undefined,
        eager: undefined,
        bg_color: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        mandatory: undefined,
        item_title: undefined,
        item_value: undefined,
        item_props: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        hide_actions: undefined,
        focusable: undefined,
        alt_labels: undefined,
        complete_icon: undefined,
        edit_icon: undefined,
        editable: undefined,
        error_icon: undefined,
        non_linear: undefined,
        prev_text: undefined,
        next_text: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepperVertical";
  }
}

StepperVerticalModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperVerticalActionsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperVerticalActionsModel",

        color: undefined,
        disabled: undefined,
        prev_text: undefined,
        next_text: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepperVerticalActions";
  }
}

StepperVerticalActionsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperVerticalItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperVerticalItemModel",

        title: undefined,
        text: undefined,
        icon: undefined,
        error: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        static: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        color: undefined,
        disabled: undefined,
        value: undefined,
        readonly: undefined,
        ripple: undefined,
        selected_class: undefined,
        eager: undefined,
        subtitle: undefined,
        bg_color: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        rules: undefined,
        hide_actions: undefined,
        focusable: undefined,
        complete_icon: undefined,
        edit_icon: undefined,
        editable: undefined,
        error_icon: undefined,
        complete: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepperVerticalItem";
  }
}

StepperVerticalItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperWindowModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperWindowModel",

        reverse: undefined,
        tag: undefined,
        theme: undefined,
        disabled: undefined,
        selected_class: undefined,
        direction: undefined,
        crossfade: undefined,
        transition_duration: undefined,
        vertical_arrows: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepperWindow";
  }
}

StepperWindowModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperWindowItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperWindowItemModel",

        disabled: undefined,
        value: undefined,
        selected_class: undefined,
        eager: undefined,
        transition: undefined,
        reverse_transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VStepperWindowItem";
  }
}

StepperWindowItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SvgIconModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SvgIconModel",

        icon: undefined,
        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSvgIcon";
  }
}

SvgIconModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SwitchModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SwitchModel",

        flat: undefined,
        type: undefined,
        error: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        disabled: undefined,
        indeterminate: undefined,
        multiple: undefined,
        value: undefined,
        id: undefined,
        label: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        ripple: undefined,
        loading: undefined,
        value_comparator: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        inline: undefined,
        inset: undefined,
        true_value: undefined,
        false_value: undefined,
        defaults_target: undefined,
        false_icon: undefined,
        true_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSwitch";
  }
}

SwitchModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class SystemBarModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "SystemBarModel",

        height: undefined,
        elevation: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        order: undefined,
        window: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VSystemBar";
  }
}

SystemBarModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TabModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TabModel",

        text: undefined,
        replace: undefined,
        fixed: undefined,
        border: undefined,
        icon: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        size: undefined,
        value: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        slim: undefined,
        stacked: undefined,
        ripple: undefined,
        selected_class: undefined,
        loading: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        spaced: undefined,
        direction: undefined,
        inset: undefined,
        slider_color: undefined,
        slider_transition_duration: undefined,
        hide_slider: undefined,
        slider_transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTab";
  }
}

TabModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TableModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TableModel",

        density: undefined,
        height: undefined,
        tag: undefined,
        theme: undefined,
        hover: undefined,
        fixed_header: undefined,
        fixed_footer: undefined,
        striped: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTable";
  }
}

TableModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TabsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TabsModel",

        symbol: undefined,
        density: undefined,
        height: undefined,
        tag: undefined,
        color: undefined,
        disabled: undefined,
        max: undefined,
        multiple: undefined,
        items: undefined,
        stacked: undefined,
        selected_class: undefined,
        spaced: undefined,
        bg_color: undefined,
        mandatory: undefined,
        scroll_to_active: undefined,
        content_class: undefined,
        direction: undefined,
        mobile: undefined,
        mobile_breakpoint: undefined,
        grow: undefined,
        inset: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        center_active: undefined,
        slider_color: undefined,
        slider_transition_duration: undefined,
        hide_slider: undefined,
        slider_transition: undefined,
        align_tabs: undefined,
        fixed_tabs: undefined,
        inset_padding: undefined,
        inset_radius: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTabs";
  }
}

TabsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TabsWindowModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TabsWindowModel",

        reverse: undefined,
        tag: undefined,
        theme: undefined,
        disabled: undefined,
        selected_class: undefined,
        direction: undefined,
        crossfade: undefined,
        transition_duration: undefined,
        vertical_arrows: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTabsWindow";
  }
}

TabsWindowModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TabsWindowItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TabsWindowItemModel",

        disabled: undefined,
        value: undefined,
        selected_class: undefined,
        eager: undefined,
        transition: undefined,
        reverse_transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTabsWindowItem";
  }
}

TabsWindowItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TextFieldModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TextFieldModel",

        flat: undefined,
        type: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        autocomplete: undefined,
        disabled: undefined,
        placeholder: undefined,
        id: undefined,
        prefix: undefined,
        role: undefined,
        autofocus: undefined,
        label: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        bg_color: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTextField";
  }
}

TextFieldModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TextareaModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TextareaModel",

        flat: undefined,
        model_value: undefined,
        error: undefined,
        reverse: undefined,
        density: undefined,
        max_height: undefined,
        max_width: undefined,
        min_width: undefined,
        width: undefined,
        rounded: undefined,
        tile: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        autocomplete: undefined,
        disabled: undefined,
        placeholder: undefined,
        id: undefined,
        prefix: undefined,
        autofocus: undefined,
        label: undefined,
        active: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        readonly: undefined,
        loading: undefined,
        bg_color: undefined,
        counter: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        glow: undefined,
        icon_color: undefined,
        hide_spin_buttons: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        clearable: undefined,
        clear_icon: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
        auto_grow: undefined,
        no_resize: undefined,
        rows: undefined,
        max_rows: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTextarea";
  }
}

TextareaModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ThemeProviderModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ThemeProviderModel",

        tag: undefined,
        theme: undefined,
        with_background: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VThemeProvider";
  }
}

ThemeProviderModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TimePickerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TimePickerModel",

        title: undefined,
        border: undefined,
        model_value: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        location: undefined,
        position: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        max: undefined,
        min: undefined,
        readonly: undefined,
        bg_color: undefined,
        scrollable: undefined,
        divided: undefined,
        hide_header: undefined,
        hide_title: undefined,
        view_mode: undefined,
        format: undefined,
        period: undefined,
        use_seconds: undefined,
        allowed_hours: undefined,
        allowed_minutes: undefined,
        allowed_seconds: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTimePicker";
  }
}

TimePickerModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TimePickerClockModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TimePickerClockModel",

        model_value: undefined,
        color: undefined,
        disabled: undefined,
        max: undefined,
        min: undefined,
        step: undefined,
        readonly: undefined,
        scrollable: undefined,
        double: undefined,
        rotate: undefined,
        format: undefined,
        ampm: undefined,
        displayed_value: undefined,
        allowed_values: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTimePickerClock";
  }
}

TimePickerClockModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TimePickerControlsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TimePickerControlsModel",

        color: undefined,
        disabled: undefined,
        max: undefined,
        min: undefined,
        value: undefined,
        readonly: undefined,
        hour: undefined,
        minute: undefined,
        view_mode: undefined,
        ampm: undefined,
        second: undefined,
        period: undefined,
        use_seconds: undefined,
        allowed_hours: undefined,
        allowed_minutes: undefined,
        allowed_seconds: undefined,
        input_hints: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTimePickerControls";
  }
}

TimePickerControlsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TimelineModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TimelineModel",

        density: undefined,
        tag: undefined,
        theme: undefined,
        align: undefined,
        size: undefined,
        icon_color: undefined,
        direction: undefined,
        justify: undefined,
        side: undefined,
        line_thickness: undefined,
        line_color: undefined,
        dot_color: undefined,
        fill_dot: undefined,
        hide_opposite: undefined,
        line_inset: undefined,
        truncate_line: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTimeline";
  }
}

TimelineModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TimelineItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TimelineItemModel",

        icon: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        size: undefined,
        icon_color: undefined,
        side: undefined,
        dot_color: undefined,
        fill_dot: undefined,
        hide_dot: undefined,
        hide_opposite: undefined,
        line_inset: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTimelineItem";
  }
}

TimelineItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ToolbarModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ToolbarModel",

        title: undefined,
        flat: undefined,
        border: undefined,
        density: undefined,
        height: undefined,
        elevation: undefined,
        location: undefined,
        absolute: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        image: undefined,
        collapse: undefined,
        collapse_position: undefined,
        extended: undefined,
        extension_height: undefined,
        floating: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VToolbar";
  }
}

ToolbarModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ToolbarItemsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ToolbarItemsModel",

        color: undefined,
        variant: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VToolbarItems";
  }
}

ToolbarItemsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ToolbarTitleModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ToolbarTitleModel",

        text: undefined,
        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VToolbarTitle";
  }
}

ToolbarTitleModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TooltipModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TooltipModel",

        text: undefined,
        model_value: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        location: undefined,
        theme: undefined,
        disabled: undefined,
        id: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        opacity: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        z_index: undefined,
        target: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        stick_to_target: undefined,
        viewport_margin: undefined,
        scroll_strategy: undefined,
        transition: undefined,
        attach: undefined,
        interactive: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTooltip";
  }
}

TooltipModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TreeviewModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TreeviewModel",

        search: undefined,
        border: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        items: undefined,
        active_color: undefined,
        base_color: undefined,
        slim: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        filter_keys: undefined,
        hide_no_data: undefined,
        active_class: undefined,
        bg_color: undefined,
        filterable: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        lines: undefined,
        prepend_gap: undefined,
        indent: undefined,
        navigation_strategy: undefined,
        navigation_index: undefined,
        activatable: undefined,
        selectable: undefined,
        mandatory: undefined,
        items_registration: undefined,
        active_strategy: undefined,
        select_strategy: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        item_type: undefined,
        return_object: undefined,
        value_comparator: undefined,
        open_on_click: undefined,
        no_data_text: undefined,
        indeterminate_icon: undefined,
        false_icon: undefined,
        true_icon: undefined,
        hide_actions: undefined,
        fluid: undefined,
        open_all: undefined,
        indent_lines_color: undefined,
        indent_lines_opacity: undefined,
        loading_icon: undefined,
        selected_color: undefined,
        separate_roots: undefined,
        indent_lines: undefined,
        load_children: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTreeview";
  }
}

TreeviewModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TreeviewGroupModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TreeviewGroupModel",

        title: undefined,
        tag: undefined,
        color: undefined,
        disabled: undefined,
        value: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        fluid: undefined,
        raw_id: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTreeviewGroup";
  }
}

TreeviewGroupModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class TreeviewItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "TreeviewItemModel",

        title: undefined,
        replace: undefined,
        link: undefined,
        border: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        tile: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        value: undefined,
        nav: undefined,
        active: undefined,
        active_color: undefined,
        base_color: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        slim: undefined,
        ripple: undefined,
        loading: undefined,
        href: undefined,
        exact: undefined,
        to: undefined,
        subtitle: undefined,
        active_class: undefined,
        lines: undefined,
        prepend_gap: undefined,
        append_avatar: undefined,
        prepend_avatar: undefined,
        hide_actions: undefined,
        index: undefined,
        tabindex: undefined,
        has_custom_prepend: undefined,
        toggle_icon: undefined,
        indent_lines: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VTreeviewItem";
  }
}

TreeviewItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ValidationModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ValidationModel",

        error: undefined,
        name: undefined,
        disabled: undefined,
        label: undefined,
        readonly: undefined,
        error_messages: undefined,
        max_errors: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VValidation";
  }
}

ValidationModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class VideoModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "VideoModel",

        type: undefined,
        density: undefined,
        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        elevation: undefined,
        rounded: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        src: undefined,
        playing: undefined,
        progress: undefined,
        image: undefined,
        floating: undefined,
        eager: undefined,
        aspect_ratio: undefined,
        hide_overlay: undefined,
        track_color: undefined,
        autoplay: undefined,
        muted: undefined,
        no_fullscreen: undefined,
        start_at: undefined,
        controls_transition: undefined,
        controls_variant: undefined,
        background_color: undefined,
        hide_play: undefined,
        hide_volume: undefined,
        hide_fullscreen: undefined,
        split_time: undefined,
        pills: undefined,
        detached: undefined,
        duration: undefined,
        volume: undefined,
        volume_props: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VVideo";
  }
}

VideoModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class VideoControlsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "VideoControlsModel",

        density: undefined,
        elevation: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        playing: undefined,
        progress: undefined,
        floating: undefined,
        fullscreen: undefined,
        track_color: undefined,
        background_color: undefined,
        hide_play: undefined,
        hide_volume: undefined,
        hide_fullscreen: undefined,
        split_time: undefined,
        pills: undefined,
        detached: undefined,
        duration: undefined,
        volume: undefined,
        volume_props: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VVideoControls";
  }
}

VideoControlsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class VideoVolumeModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "VideoVolumeModel",

        model_value: undefined,
        label: undefined,
        direction: undefined,
        inline: undefined,
        slider_props: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VVideoVolume";
  }
}

VideoVolumeModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class VirtualScrollModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "VirtualScrollModel",

        height: undefined,
        max_height: undefined,
        max_width: undefined,
        min_height: undefined,
        min_width: undefined,
        width: undefined,
        items: undefined,
        item_height: undefined,
        item_key: undefined,
        renderless: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VVirtualScroll";
  }
}

VirtualScrollModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class WindowModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "WindowModel",

        reverse: undefined,
        tag: undefined,
        theme: undefined,
        disabled: undefined,
        selected_class: undefined,
        mandatory: undefined,
        direction: undefined,
        continuous: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        touch: undefined,
        crossfade: undefined,
        transition_duration: undefined,
        vertical_arrows: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VWindow";
  }
}

WindowModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class WindowItemModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "WindowItemModel",

        disabled: undefined,
        value: undefined,
        selected_class: undefined,
        eager: undefined,
        transition: undefined,
        reverse_transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "VWindowItem";
  }
}

WindowItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};
