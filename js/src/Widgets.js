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
        type: undefined,
        border_color: undefined,
        closable: undefined,
        close_icon: undefined,
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
        location: undefined,
        position: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-alert";
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
    return "v-alert-title";
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
        full_height: undefined,
        overlaps: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-app";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        image: undefined,
        collapse: undefined,
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
    return "v-app-bar";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        value: undefined,
        size: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        block: undefined,
        stacked: undefined,
        ripple: undefined,
        disabled: undefined,
        selected_class: undefined,
        loading: undefined,
        href: undefined,
        replace: undefined,
        exact: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-app-bar-nav-icon";
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
    return "v-app-bar-title";
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
        type: undefined,
        model_value: undefined,
        error: undefined,
        density: undefined,
        reverse: undefined,
        rounded: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        id: undefined,
        items: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        loading: undefined,
        label: undefined,
        auto_select_first: undefined,
        search: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        custom_key_filter: undefined,
        filter_keys: undefined,
        chips: undefined,
        closable_chips: undefined,
        close_text: undefined,
        open_text: undefined,
        eager: undefined,
        hide_no_data: undefined,
        hide_selected: undefined,
        menu: undefined,
        menu_icon: undefined,
        transition: undefined,
        multiple: undefined,
        no_data_text: undefined,
        open_on_clear: undefined,
        item_color: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        return_object: undefined,
        value_comparator: undefined,
        autofocus: undefined,
        counter: undefined,
        prefix: undefined,
        placeholder: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        role: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        focused: undefined,
        hide_details: undefined,
        bg_color: undefined,
        clearable: undefined,
        clear_icon: undefined,
        base_color: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-autocomplete";
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

        end: undefined,
        start: undefined,
        icon: undefined,
        density: undefined,
        rounded: undefined,
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
    return "v-avatar";
  }
}

AvatarModel.serializers = {
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
        location: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        floating: undefined,
        label: undefined,
        transition: undefined,
        bordered: undefined,
        content: undefined,
        dot: undefined,
        inline: undefined,
        max: undefined,
        offset_x: undefined,
        offset_y: undefined,
        text_color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-badge";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        stacked: undefined,
        avatar: undefined,
        lines: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-banner";
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
    return "v-banner-actions";
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
    return "v-banner-text";
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
        model_value: undefined,
        density: undefined,
        height: undefined,
        elevation: undefined,
        absolute: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        order: undefined,
        active: undefined,
        disabled: undefined,
        selected_class: undefined,
        multiple: undefined,
        bg_color: undefined,
        mode: undefined,
        max: undefined,
        grow: undefined,
        mandatory: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-bottom-navigation";
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
        z_index: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        activator_props: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        scroll_strategy: undefined,
        transition: undefined,
        attach: undefined,
        inset: undefined,
        fullscreen: undefined,
        retain_focus: undefined,
        scrollable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-bottom-sheet";
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
        tag: undefined,
        color: undefined,
        items: undefined,
        disabled: undefined,
        bg_color: undefined,
        divider: undefined,
        active_class: undefined,
        active_color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-breadcrumbs";
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
    return "v-breadcrumbs-divider";
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
        tag: undefined,
        color: undefined,
        active: undefined,
        disabled: undefined,
        href: undefined,
        replace: undefined,
        exact: undefined,
        active_class: undefined,
        active_color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-breadcrumbs-item";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        value: undefined,
        size: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        block: undefined,
        stacked: undefined,
        ripple: undefined,
        disabled: undefined,
        selected_class: undefined,
        loading: undefined,
        href: undefined,
        replace: undefined,
        exact: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-btn";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        divided: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-btn-group";
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
        model_value: undefined,
        density: undefined,
        elevation: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        selected_class: undefined,
        multiple: undefined,
        max: undefined,
        mandatory: undefined,
        divided: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-btn-toggle";
  }
}

BtnToggleModel.serializers = {
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        image: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        ripple: undefined,
        disabled: undefined,
        loading: undefined,
        href: undefined,
        replace: undefined,
        exact: undefined,
        link: undefined,
        subtitle: undefined,
        append_avatar: undefined,
        hover: undefined,
        prepend_avatar: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-card";
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
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-card-actions";
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
    return "v-card-item";
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
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-card-subtitle";
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
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-card-text";
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
    return "v-card-title";
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

        model_value: undefined,
        height: undefined,
        reverse: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        disabled: undefined,
        selected_class: undefined,
        direction: undefined,
        mandatory: undefined,
        cycle: undefined,
        delimiter_icon: undefined,
        hide_delimiters: undefined,
        hide_delimiter_background: undefined,
        interval: undefined,
        progress: undefined,
        continuous: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        touch: undefined,
        vertical_delimiters: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-carousel";
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
        value: undefined,
        disabled: undefined,
        selected_class: undefined,
        eager: undefined,
        content_class: undefined,
        transition: undefined,
        options: undefined,
        inline: undefined,
        alt: undefined,
        cover: undefined,
        gradient: undefined,
        lazy_src: undefined,
        sizes: undefined,
        src: undefined,
        srcset: undefined,
        aspect_ratio: undefined,
        reverse_transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-carousel-item";
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
        model_value: undefined,
        error: undefined,
        density: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        value: undefined,
        id: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        ripple: undefined,
        disabled: undefined,
        label: undefined,
        multiple: undefined,
        value_comparator: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        indeterminate: undefined,
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
    return "v-checkbox";
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
        model_value: undefined,
        error: undefined,
        density: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        value: undefined,
        id: undefined,
        ripple: undefined,
        disabled: undefined,
        label: undefined,
        multiple: undefined,
        value_comparator: undefined,
        readonly: undefined,
        inline: undefined,
        indeterminate: undefined,
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
    return "v-checkbox-btn";
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
        border: undefined,
        closable: undefined,
        close_icon: undefined,
        close_label: undefined,
        model_value: undefined,
        density: undefined,
        elevation: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        value: undefined,
        size: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        ripple: undefined,
        disabled: undefined,
        selected_class: undefined,
        href: undefined,
        replace: undefined,
        exact: undefined,
        label: undefined,
        link: undefined,
        active_class: undefined,
        append_avatar: undefined,
        prepend_avatar: undefined,
        draggable: undefined,
        filter_icon: undefined,
        pill: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-chip";
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

        filter: undefined,
        model_value: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        selected_class: undefined,
        multiple: undefined,
        value_comparator: undefined,
        max: undefined,
        mandatory: undefined,
        column: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-chip-group";
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
    return "v-class-icon";
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
    return "v-code";
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
        cols: undefined,
        sm: undefined,
        md: undefined,
        lg: undefined,
        xl: undefined,
        xxl: undefined,
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
    return "v-col";
  }
}

ColModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ColorPickerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ColorPickerModel",

        border: undefined,
        model_value: undefined,
        width: undefined,
        elevation: undefined,
        position: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        disabled: undefined,
        mode: undefined,
        canvas_height: undefined,
        dot_size: undefined,
        hide_canvas: undefined,
        hide_sliders: undefined,
        hide_inputs: undefined,
        modes: undefined,
        show_swatches: undefined,
        swatches_max_height: undefined,
        swatches: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-color-picker";
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
        density: undefined,
        reverse: undefined,
        rounded: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        id: undefined,
        items: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        loading: undefined,
        label: undefined,
        auto_select_first: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        custom_key_filter: undefined,
        filter_keys: undefined,
        chips: undefined,
        closable_chips: undefined,
        close_text: undefined,
        open_text: undefined,
        eager: undefined,
        hide_no_data: undefined,
        hide_selected: undefined,
        menu: undefined,
        menu_icon: undefined,
        transition: undefined,
        multiple: undefined,
        no_data_text: undefined,
        open_on_clear: undefined,
        item_color: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        return_object: undefined,
        value_comparator: undefined,
        autofocus: undefined,
        counter: undefined,
        prefix: undefined,
        placeholder: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        role: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        focused: undefined,
        hide_details: undefined,
        bg_color: undefined,
        clearable: undefined,
        clear_icon: undefined,
        base_color: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
        delimiters: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-combobox";
  }
}

ComboboxModel.serializers = {
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
    return "v-component-icon";
  }
}

ComponentIconModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ContainerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ContainerModel",

        tag: undefined,
        fluid: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-container";
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

        value: undefined,
        active: undefined,
        transition: undefined,
        max: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-counter";
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

        model_value: undefined,
        tag: undefined,
        items: undefined,
        loading: undefined,
        search: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        custom_key_filter: undefined,
        filter_keys: undefined,
        item_value: undefined,
        return_object: undefined,
        value_comparator: undefined,
        item_selectable: undefined,
        show_select: undefined,
        select_strategy: undefined,
        page: undefined,
        sort_by: undefined,
        multi_sort: undefined,
        must_sort: undefined,
        items_per_page: undefined,
        expand_on_click: undefined,
        show_expand: undefined,
        expanded: undefined,
        group_by: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-data-iterator";
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

        model_value: undefined,
        density: undefined,
        height: undefined,
        width: undefined,
        sticky: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        items: undefined,
        loading: undefined,
        search: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        custom_key_filter: undefined,
        filter_keys: undefined,
        hide_no_data: undefined,
        no_data_text: undefined,
        item_value: undefined,
        return_object: undefined,
        value_comparator: undefined,
        hover: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        item_selectable: undefined,
        show_select: undefined,
        select_strategy: undefined,
        page: undefined,
        sort_by: undefined,
        multi_sort: undefined,
        must_sort: undefined,
        items_per_page: undefined,
        expand_on_click: undefined,
        show_expand: undefined,
        expanded: undefined,
        group_by: undefined,
        headers: undefined,
        loading_text: undefined,
        row_height: undefined,
        sort_asc_icon: undefined,
        sort_desc_icon: undefined,
        fixed_header: undefined,
        fixed_footer: undefined,
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
    return "v-data-table";
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
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-data-table-footer";
  }
}

DataTableFooterModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DataTableRowModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DataTableRowModel",

        item: undefined,
        index: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-data-table-row";
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

        items: undefined,
        loading: undefined,
        hide_no_data: undefined,
        no_data_text: undefined,
        loading_text: undefined,
        row_height: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-data-table-rows";
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

        model_value: undefined,
        density: undefined,
        height: undefined,
        width: undefined,
        sticky: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        items: undefined,
        loading: undefined,
        search: undefined,
        hide_no_data: undefined,
        no_data_text: undefined,
        item_value: undefined,
        return_object: undefined,
        value_comparator: undefined,
        hover: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        item_selectable: undefined,
        show_select: undefined,
        select_strategy: undefined,
        page: undefined,
        sort_by: undefined,
        multi_sort: undefined,
        must_sort: undefined,
        items_per_page: undefined,
        expand_on_click: undefined,
        show_expand: undefined,
        expanded: undefined,
        group_by: undefined,
        items_length: undefined,
        headers: undefined,
        loading_text: undefined,
        row_height: undefined,
        sort_asc_icon: undefined,
        sort_desc_icon: undefined,
        fixed_header: undefined,
        fixed_footer: undefined,
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
    return "v-data-table-server";
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

        model_value: undefined,
        density: undefined,
        height: undefined,
        width: undefined,
        sticky: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        items: undefined,
        loading: undefined,
        search: undefined,
        filter_mode: undefined,
        no_filter: undefined,
        custom_filter: undefined,
        custom_key_filter: undefined,
        filter_keys: undefined,
        hide_no_data: undefined,
        no_data_text: undefined,
        item_value: undefined,
        return_object: undefined,
        value_comparator: undefined,
        hover: undefined,
        item_selectable: undefined,
        show_select: undefined,
        select_strategy: undefined,
        sort_by: undefined,
        multi_sort: undefined,
        must_sort: undefined,
        expand_on_click: undefined,
        show_expand: undefined,
        expanded: undefined,
        group_by: undefined,
        headers: undefined,
        loading_text: undefined,
        row_height: undefined,
        sort_asc_icon: undefined,
        sort_desc_icon: undefined,
        fixed_header: undefined,
        fixed_footer: undefined,
        item_height: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-data-table-virtual";
  }
}

DataTableVirtualModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DateCardModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DateCardModel",

        model_value: undefined,
        height: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        transition: undefined,
        multiple: undefined,
        max: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        cancel_text: undefined,
        ok_text: undefined,
        input_mode: undefined,
        hide_actions: undefined,
        display_date: undefined,
        mode_icon: undefined,
        view_mode: undefined,
        allowed_dates: undefined,
        show_adjacent_months: undefined,
        hide_weekdays: undefined,
        show_week: undefined,
        hover_date: undefined,
        side: undefined,
        min: undefined,
        format: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-date-card";
  }
}

DateCardModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DatePickerModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DatePickerModel",

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
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        header: undefined,
        disabled: undefined,
        multiple: undefined,
        bg_color: undefined,
        max: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        cancel_text: undefined,
        ok_text: undefined,
        input_mode: undefined,
        hide_actions: undefined,
        display_date: undefined,
        mode_icon: undefined,
        view_mode: undefined,
        allowed_dates: undefined,
        show_adjacent_months: undefined,
        hide_weekdays: undefined,
        show_week: undefined,
        hover_date: undefined,
        side: undefined,
        min: undefined,
        format: undefined,
        calendar_icon: undefined,
        keyboard_icon: undefined,
        input_text: undefined,
        input_placeholder: undefined,
        landscape: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-date-picker";
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

        variant: undefined,
        disabled: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        display_date: undefined,
        mode_icon: undefined,
        view_mode: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-date-picker-controls";
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
    return "v-date-picker-header";
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

        model_value: undefined,
        color: undefined,
        multiple: undefined,
        max: undefined,
        display_date: undefined,
        allowed_dates: undefined,
        show_adjacent_months: undefined,
        hide_weekdays: undefined,
        show_week: undefined,
        hover_date: undefined,
        side: undefined,
        min: undefined,
        format: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-date-picker-month";
  }
}

DatePickerMonthModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class DatePickerYearsModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "DatePickerYearsModel",

        height: undefined,
        color: undefined,
        max: undefined,
        display_date: undefined,
        min: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-date-picker-years";
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
        root: undefined,
        reset: undefined,
        scoped: undefined,
        defaults: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-defaults-provider";
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
        z_index: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        activator_props: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        scroll_strategy: undefined,
        transition: undefined,
        attach: undefined,
        fullscreen: undefined,
        retain_focus: undefined,
        scrollable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-dialog";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-dialog-bottom-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-dialog-top-transition";
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
    return "v-dialog-transition";
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
        vertical: undefined,
        inset: undefined,
        thickness: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-divider";
  }
}

DividerModel.serializers = {
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
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-expand-transition";
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
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-expand-x-transition";
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
        elevation: undefined,
        rounded: undefined,
        tag: undefined,
        color: undefined,
        value: undefined,
        ripple: undefined,
        disabled: undefined,
        selected_class: undefined,
        eager: undefined,
        readonly: undefined,
        bg_color: undefined,
        hide_actions: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-expansion-panel";
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
    return "v-expansion-panel-text";
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

        color: undefined,
        ripple: undefined,
        readonly: undefined,
        hide_actions: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-expansion-panel-title";
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

        model_value: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        disabled: undefined,
        selected_class: undefined,
        multiple: undefined,
        readonly: undefined,
        max: undefined,
        mandatory: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-expansion-panels";
  }
}

ExpansionPanelsModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class FabTransitionModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "FabTransitionModel",

        disabled: undefined,
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-fab-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-fade-transition";
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
        theme: undefined,
        color: undefined,
        variant: undefined,
        id: undefined,
        active: undefined,
        disabled: undefined,
        loading: undefined,
        label: undefined,
        center_affix: undefined,
        focused: undefined,
        append_inner_icon: undefined,
        bg_color: undefined,
        clearable: undefined,
        clear_icon: undefined,
        base_color: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-field";
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
    return "v-field-label";
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
        density: undefined,
        reverse: undefined,
        rounded: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        id: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        loading: undefined,
        label: undefined,
        chips: undefined,
        multiple: undefined,
        counter: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        bg_color: undefined,
        clearable: undefined,
        clear_icon: undefined,
        base_color: undefined,
        dirty: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_size_string: undefined,
        counter_string: undefined,
        show_size: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-file-input";
  }
}

FileInputModel.serializers = {
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
    return "v-footer";
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
    return "v-form";
  }
}

FormModel.serializers = {
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
    return "v-hover";
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
        size: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-icon";
  }
}

IconModel.serializers = {
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
        eager: undefined,
        content_class: undefined,
        transition: undefined,
        options: undefined,
        inline: undefined,
        alt: undefined,
        cover: undefined,
        gradient: undefined,
        lazy_src: undefined,
        sizes: undefined,
        src: undefined,
        srcset: undefined,
        aspect_ratio: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-img";
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
        direction: undefined,
        mode: undefined,
        side: undefined,
        margin: undefined,
        load_more_text: undefined,
        empty_text: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-infinite-scroll";
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

        model_value: undefined,
        error: undefined,
        density: undefined,
        name: undefined,
        id: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        label: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
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
    return "v-input";
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

        value: undefined,
        disabled: undefined,
        selected_class: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-item";
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

        model_value: undefined,
        tag: undefined,
        theme: undefined,
        disabled: undefined,
        selected_class: undefined,
        multiple: undefined,
        max: undefined,
        mandatory: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-item-group";
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

        tag: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-kbd";
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
        clickable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-label";
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

        full_height: undefined,
        overlaps: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-layout";
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
    return "v-layout-item";
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
    return "v-lazy";
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
    return "v-ligature-icon";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        items: undefined,
        disabled: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        return_object: undefined,
        value_comparator: undefined,
        bg_color: undefined,
        base_color: undefined,
        lines: undefined,
        mandatory: undefined,
        active_class: undefined,
        active_color: undefined,
        selected: undefined,
        select_strategy: undefined,
        nav: undefined,
        open_strategy: undefined,
        opened: undefined,
        item_type: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-list";
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
        value: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        base_color: undefined,
        active_color: undefined,
        fluid: undefined,
        expand_icon: undefined,
        collapse_icon: undefined,
        subgroup: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-list-group";
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
    return "v-list-img";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        value: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        ripple: undefined,
        disabled: undefined,
        href: undefined,
        replace: undefined,
        exact: undefined,
        base_color: undefined,
        link: undefined,
        lines: undefined,
        active_class: undefined,
        active_color: undefined,
        subtitle: undefined,
        append_avatar: undefined,
        prepend_avatar: undefined,
        nav: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-list-item";
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
    return "v-list-item-action";
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
    return "v-list-item-media";
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
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-list-item-subtitle";
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
    return "v-list-item-title";
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
    return "v-list-subheader";
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
        fallback_locale: undefined,
        rtl: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-locale-provider";
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

        tag: undefined,
        scrollable: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-main";
  }
}

MainModel.serializers = {
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
        z_index: undefined,
        id: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        activator_props: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        scroll_strategy: undefined,
        transition: undefined,
        attach: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-menu";
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
    return "v-messages";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        image: undefined,
        floating: undefined,
        order: undefined,
        scrim: undefined,
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
    return "v-navigation-drawer";
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
    return "v-no-ssr";
  }
}

NoSsrModel.serializers = {
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
        loading: undefined,
        label: undefined,
        autofocus: undefined,
        placeholder: undefined,
        focused: undefined,
        bg_color: undefined,
        base_color: undefined,
        divider: undefined,
        focus_all: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-otp-input";
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
        z_index: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        no_click_animation: undefined,
        persistent: undefined,
        scrim: undefined,
        activator_props: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        scroll_strategy: undefined,
        transition: undefined,
        attach: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-overlay";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        size: undefined,
        disabled: undefined,
        active_color: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        first_icon: undefined,
        last_icon: undefined,
        aria_label: undefined,
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
    return "v-pagination";
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
    return "v-parallax";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        bg_color: undefined,
        landscape: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-picker";
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
    return "v-picker-title";
  }
}

PickerTitleModel.serializers = {
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        size: undefined,
        bg_color: undefined,
        indeterminate: undefined,
        rotate: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-progress-circular";
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
        height: undefined,
        reverse: undefined,
        location: undefined,
        absolute: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        active: undefined,
        bg_color: undefined,
        max: undefined,
        indeterminate: undefined,
        clickable: undefined,
        bg_opacity: undefined,
        buffer_value: undefined,
        stream: undefined,
        striped: undefined,
        rounded_bar: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-progress-linear";
  }
}

ProgressLinearModel.serializers = {
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
        value: undefined,
        id: undefined,
        ripple: undefined,
        disabled: undefined,
        label: undefined,
        multiple: undefined,
        value_comparator: undefined,
        readonly: undefined,
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
    return "v-radio";
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
        model_value: undefined,
        error: undefined,
        density: undefined,
        height: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        id: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        ripple: undefined,
        disabled: undefined,
        label: undefined,
        value_comparator: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
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
    return "v-radio-group";
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
        density: undefined,
        reverse: undefined,
        elevation: undefined,
        rounded: undefined,
        color: undefined,
        name: undefined,
        id: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        label: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        max: undefined,
        min: undefined,
        step: undefined,
        thumb_color: undefined,
        thumb_label: undefined,
        thumb_size: undefined,
        show_ticks: undefined,
        ticks: undefined,
        tick_size: undefined,
        track_color: undefined,
        track_fill_color: undefined,
        track_size: undefined,
        strict: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-range-slider";
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
        size: undefined,
        ripple: undefined,
        disabled: undefined,
        readonly: undefined,
        clearable: undefined,
        active_color: undefined,
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
    return "v-rating";
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
    return "v-responsive";
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
        justify: undefined,
        align_content: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-row";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-scale-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-scroll-x-reverse-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-scroll-x-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-scroll-y-reverse-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-scroll-y-transition";
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
        type: undefined,
        model_value: undefined,
        error: undefined,
        density: undefined,
        reverse: undefined,
        rounded: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        id: undefined,
        items: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        loading: undefined,
        label: undefined,
        chips: undefined,
        closable_chips: undefined,
        close_text: undefined,
        open_text: undefined,
        eager: undefined,
        hide_no_data: undefined,
        hide_selected: undefined,
        menu: undefined,
        menu_icon: undefined,
        transition: undefined,
        multiple: undefined,
        no_data_text: undefined,
        open_on_clear: undefined,
        item_color: undefined,
        item_title: undefined,
        item_value: undefined,
        item_children: undefined,
        item_props: undefined,
        return_object: undefined,
        value_comparator: undefined,
        autofocus: undefined,
        counter: undefined,
        prefix: undefined,
        placeholder: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        role: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        focused: undefined,
        hide_details: undefined,
        bg_color: undefined,
        clearable: undefined,
        clear_icon: undefined,
        base_color: undefined,
        persistent_clear: undefined,
        prepend_inner_icon: undefined,
        single_line: undefined,
        counter_value: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-select";
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
        value: undefined,
        id: undefined,
        ripple: undefined,
        disabled: undefined,
        label: undefined,
        multiple: undefined,
        value_comparator: undefined,
        readonly: undefined,
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
    return "v-selection-control";
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
        model_value: undefined,
        error: undefined,
        density: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        id: undefined,
        ripple: undefined,
        disabled: undefined,
        multiple: undefined,
        value_comparator: undefined,
        readonly: undefined,
        inline: undefined,
        defaults_target: undefined,
        false_icon: undefined,
        true_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-selection-control-group";
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
        tag: undefined,
        theme: undefined,
        color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-sheet";
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
    return "v-skeleton-loader";
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
        model_value: undefined,
        tag: undefined,
        disabled: undefined,
        selected_class: undefined,
        multiple: undefined,
        direction: undefined,
        max: undefined,
        mandatory: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        center_active: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-slide-group";
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

        value: undefined,
        disabled: undefined,
        selected_class: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-slide-group-item";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-slide-x-reverse-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-slide-x-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-slide-y-reverse-transition";
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
        origin: undefined,
        mode: undefined,
        group: undefined,
        hide_on_leave: undefined,
        leave_absolute: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-slide-y-transition";
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
        density: undefined,
        reverse: undefined,
        elevation: undefined,
        rounded: undefined,
        color: undefined,
        name: undefined,
        id: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        label: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        max: undefined,
        min: undefined,
        step: undefined,
        thumb_color: undefined,
        thumb_label: undefined,
        thumb_size: undefined,
        show_ticks: undefined,
        ticks: undefined,
        tick_size: undefined,
        track_color: undefined,
        track_fill_color: undefined,
        track_size: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-slider";
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
        theme: undefined,
        color: undefined,
        variant: undefined,
        z_index: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        activator_props: undefined,
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
        timeout: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-snackbar";
  }
}

SnackbarModel.serializers = {
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
    return "v-spacer";
  }
}

SpacerModel.serializers = {
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
        tag: undefined,
        theme: undefined,
        color: undefined,
        items: undefined,
        disabled: undefined,
        selected_class: undefined,
        multiple: undefined,
        item_title: undefined,
        item_value: undefined,
        bg_color: undefined,
        max: undefined,
        mandatory: undefined,
        hide_actions: undefined,
        mobile: undefined,
        alt_labels: undefined,
        editable: undefined,
        non_linear: undefined,
        prev_text: undefined,
        next_text: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-stepper";
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
    return "v-stepper-actions";
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
    return "v-stepper-header";
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
        value: undefined,
        ripple: undefined,
        disabled: undefined,
        selected_class: undefined,
        rules: undefined,
        subtitle: undefined,
        editable: undefined,
        complete: undefined,
        complete_icon: undefined,
        edit_icon: undefined,
        error_icon: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-stepper-item";
  }
}

StepperItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class StepperWindowModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "StepperWindowModel",

        model_value: undefined,
        reverse: undefined,
        tag: undefined,
        theme: undefined,
        disabled: undefined,
        selected_class: undefined,
        direction: undefined,
        mandatory: undefined,
        continuous: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        touch: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-stepper-window";
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

        value: undefined,
        disabled: undefined,
        selected_class: undefined,
        eager: undefined,
        transition: undefined,
        reverse_transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-stepper-window-item";
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
    return "v-svg-icon";
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
        model_value: undefined,
        error: undefined,
        density: undefined,
        theme: undefined,
        color: undefined,
        name: undefined,
        value: undefined,
        id: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        ripple: undefined,
        disabled: undefined,
        loading: undefined,
        label: undefined,
        multiple: undefined,
        value_comparator: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        inline: undefined,
        inset: undefined,
        indeterminate: undefined,
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
    return "v-switch";
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
    return "v-system-bar";
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
        fixed: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        value: undefined,
        size: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        stacked: undefined,
        ripple: undefined,
        disabled: undefined,
        selected_class: undefined,
        loading: undefined,
        href: undefined,
        replace: undefined,
        exact: undefined,
        direction: undefined,
        slider_color: undefined,
        hide_slider: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-tab";
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
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-table";
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
        model_value: undefined,
        density: undefined,
        height: undefined,
        tag: undefined,
        color: undefined,
        items: undefined,
        stacked: undefined,
        disabled: undefined,
        selected_class: undefined,
        multiple: undefined,
        direction: undefined,
        bg_color: undefined,
        max: undefined,
        grow: undefined,
        mandatory: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        center_active: undefined,
        slider_color: undefined,
        hide_slider: undefined,
        align_tabs: undefined,
        fixed_tabs: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-tabs";
  }
}

TabsModel.serializers = {
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
        density: undefined,
        reverse: undefined,
        rounded: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        id: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        loading: undefined,
        label: undefined,
        autofocus: undefined,
        counter: undefined,
        prefix: undefined,
        placeholder: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        role: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        bg_color: undefined,
        clearable: undefined,
        clear_icon: undefined,
        base_color: undefined,
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
    return "v-text-field";
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
        density: undefined,
        reverse: undefined,
        rounded: undefined,
        theme: undefined,
        color: undefined,
        variant: undefined,
        name: undefined,
        id: undefined,
        active: undefined,
        prepend_icon: undefined,
        append_icon: undefined,
        disabled: undefined,
        loading: undefined,
        label: undefined,
        autofocus: undefined,
        counter: undefined,
        prefix: undefined,
        placeholder: undefined,
        persistent_placeholder: undefined,
        persistent_counter: undefined,
        suffix: undefined,
        center_affix: undefined,
        hint: undefined,
        persistent_hint: undefined,
        messages: undefined,
        direction: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
        hide_details: undefined,
        append_inner_icon: undefined,
        bg_color: undefined,
        clearable: undefined,
        clear_icon: undefined,
        base_color: undefined,
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
    return "v-textarea";
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
    return "v-theme-provider";
  }
}

ThemeProviderModel.serializers = {
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
        direction: undefined,
        align: undefined,
        side: undefined,
        justify: undefined,
        line_inset: undefined,
        line_thickness: undefined,
        line_color: undefined,
        truncate_line: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-timeline";
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
        tag: undefined,
        size: undefined,
        line_inset: undefined,
        dot_color: undefined,
        fill_dot: undefined,
        hide_dot: undefined,
        hide_opposite: undefined,
        icon_color: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-timeline-item";
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
        absolute: undefined,
        rounded: undefined,
        tag: undefined,
        theme: undefined,
        color: undefined,
        image: undefined,
        collapse: undefined,
        extended: undefined,
        extension_height: undefined,
        floating: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-toolbar";
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
    return "v-toolbar-items";
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
    return "v-toolbar-title";
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
        z_index: undefined,
        id: undefined,
        disabled: undefined,
        eager: undefined,
        activator: undefined,
        close_on_back: undefined,
        contained: undefined,
        content_class: undefined,
        content_props: undefined,
        no_click_animation: undefined,
        scrim: undefined,
        activator_props: undefined,
        open_on_click: undefined,
        open_on_hover: undefined,
        open_on_focus: undefined,
        close_on_content_click: undefined,
        close_delay: undefined,
        open_delay: undefined,
        location_strategy: undefined,
        origin: undefined,
        offset: undefined,
        scroll_strategy: undefined,
        transition: undefined,
        attach: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-tooltip";
  }
}

TooltipModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};

export class ValidationModel extends VuetifyWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ValidationModel",

        model_value: undefined,
        error: undefined,
        name: undefined,
        disabled: undefined,
        label: undefined,
        error_messages: undefined,
        max_errors: undefined,
        readonly: undefined,
        rules: undefined,
        validate_on: undefined,
        validation_value: undefined,
        focused: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-validation";
  }
}

ValidationModel.serializers = {
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
        renderless: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-virtual-scroll";
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

        model_value: undefined,
        reverse: undefined,
        tag: undefined,
        theme: undefined,
        disabled: undefined,
        selected_class: undefined,
        direction: undefined,
        mandatory: undefined,
        continuous: undefined,
        next_icon: undefined,
        prev_icon: undefined,
        show_arrows: undefined,
        touch: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-window";
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

        value: undefined,
        disabled: undefined,
        selected_class: undefined,
        eager: undefined,
        transition: undefined,
        reverse_transition: undefined,
      },
    };
  }

  getVueTag() {
    // eslint-disable-line class-methods-use-this
    return "v-window-item";
  }
}

WindowItemModel.serializers = {
  ...VuetifyWidgetModel.serializers,
};
