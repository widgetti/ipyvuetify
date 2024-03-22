/* eslint camelcase: off */
import { WidgetModel } from "@jupyter-widgets/base";
import Vue from "vue";
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
        dark_effective: null,
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
          this.setTheme();
        }
      }, this);
    }
    this.setTheme();

    this.on("change:dark", () => {
      this.setTheme();
    });

    new Vue({
      vuetify,
      watch: {
        "$vuetify.theme.dark": (newValue) => {
          this.vuetifyThemeChange();
        },
      },
    });
  }

  setTheme() {
    if (this.get("dark") !== null) {
      vuetify.framework.theme.dark = this.get("dark");
    } else if (document.body.dataset.jpThemeLight) {
      vuetify.framework.theme.dark =
        document.body.dataset.jpThemeLight === "false";
    } else if (document.body.classList.contains("theme-dark")) {
      vuetify.framework.theme.dark = true;
    } else if (document.body.classList.contains("theme-light")) {
      vuetify.framework.theme.dark = false;
    } else if (window.Jupyter) {
      // Special case for Jupyter Notebook
      vuetify.framework.theme.dark = false;
    } else if (document.body.dataset.vscodeThemeKind === "vscode-dark") {
      // Special case for VS Code
      vuetify.framework.theme.dark = true;
    } else if (document.body.dataset.vscodeThemeKind === "vscode-light") {
      vuetify.framework.theme.dark = false;
    } else if (document.documentElement.matches("[theme=dark]")) {
      // Special case for Colab
      vuetify.framework.theme.dark = true;
    } else if (document.documentElement.matches("[theme=light]")) {
      vuetify.framework.theme.dark = false;
    }
    this.set("dark_effective", vuetify.framework.theme.dark);
    this.save_changes();
  }

  vuetifyThemeChange() {
    if (
      this.get("dark") !== null &&
      this.get("dark") !== vuetify.framework.theme.dark
    ) {
      this.set("dark", vuetify.framework.theme.dark);
    }
    this.set("dark_effective", vuetify.framework.theme.dark);
    this.save_changes();
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
