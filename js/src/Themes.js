/* eslint camelcase: off */
import { WidgetModel } from "@jupyter-widgets/base";
import { version } from "./version";

export class ThemeModel extends WidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ThemeModel",
        _model_module: "jupyter-vuetify",
        _view_module_version: version,
        _model_module_version: version,
        dark: null,
        dark_jlab: null,
      },
    };
  }

  constructor(...args) {
    super(...args);
  }
}

ThemeModel.serializers = {
  ...WidgetModel.serializers,
};

export class ThemeColorsModel extends WidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ThemeColorsModel",
        _model_module: "jupyter-vuetify",
        _view_module_version: version,
        _model_module_version: version,
        _theme_name: null,
        background: null,
        surface: null,
        surface_bright: null,
        surface_variant: null,
        on_surface_variant: null,
        primary: null,
        primary_darken_1: null,
        secondary: null,
        secondary_darken_1: null,
        error: null,
        info: null,
        success: null,
        warning: null,
      },
    };
  }

  constructor(...args) {
    super(...args);
  }
}

ThemeColorsModel.serializers = {
  ...WidgetModel.serializers,
};
