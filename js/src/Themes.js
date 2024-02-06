/* eslint camelcase: off */
import { WidgetModel } from "@jupyter-widgets/base";
import colors from "@mariobuikhuizen/vuetify/lib/util/colors";
import vuetify from "./plugins/vuetify";

export class ThemeModel extends WidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "ThemeModel",
        _model_module: "jupyter-vuetify",
        _view_module_version: "0.1.11",
        _model_module_version: "0.1.11",
        dark: null,
        dark_jlab: null,
      },
    };
  }

  constructor(...args) {
    super(...args);

    if (!vuetify) {
      return;
    }

    if (ThemeModel.themeManager) {
      ThemeModel.themeManager.themeChanged.connect(() => {
        if (this.get("dark") === null) {
          vuetify.framework.theme.dark =
            document.body.dataset.jpThemeLight === "false";
          this.set("dark_jlab", vuetify.framework.theme.dark);
          this.save_changes();
        }
      }, this);
    }
    
    if (this.get("dark") !== null) {
      vuetify.framework.theme.dark = this.get("dark");
    } else if (document.body.dataset.jpThemeLight) {
      vuetify.framework.theme.dark =
        document.body.dataset.jpThemeLight === "false";
      this.set("dark_jlab", vuetify.framework.theme.dark);
      this.save_changes();
    } else if (document.body.classList.contains("theme-dark")) {
      vuetify.framework.theme.dark = true;
      this.set("dark", true);
      this.save_changes();
    } else if (document.body.classList.contains("theme-light")) {
      this.set("dark", false);
      this.save_changes();
    } else if(window.Jupyter) {
      this.set("dark", false);
      this.save_changes();
    } else {
      // e.g. solara
      let osPrefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
      this.set("dark_jlab", osPrefersDark);
      this.save_changes();
    }
    this.on("change:dark", () => {
      vuetify.framework.theme.dark = this.get("dark");
      // TODO: call the same code as in the constructor
    });
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
        _view_module_version: "0.1.11",
        _model_module_version: "0.1.11",
        _theme_name: null,
        primary: null,
        secondary: null,
        accent: null,
        error: null,
        info: null,
        success: null,
        warning: null,
        anchor: null,
      },
    };
  }

  constructor(...args) {
    super(...args);

    if (!vuetify) {
      return;
    }

    const themeName = this.get("_theme_name");

    this.keys()
      .filter((prop) => !prop.startsWith("_"))
      .forEach((prop) => {
        vuetify.framework.theme.themes[themeName][prop] = convertColor(
          this.get(prop)
        );
        this.on(`change:${prop}`, () => {
          vuetify.framework.theme.themes[themeName][prop] = convertColor(
            this.get(prop)
          );
        });
      });
  }
}

ThemeColorsModel.serializers = {
  ...WidgetModel.serializers,
};

function convertColor(colorStr) {
  if (colorStr == null) {
    return null;
  }

  if (colorStr.startsWith("colors")) {
    const parts = colorStr.split(".").slice(1);
    let result = colors;

    parts.forEach((part) => {
      result = result[part];
    });

    return result;
  }

  return colorStr;
}
