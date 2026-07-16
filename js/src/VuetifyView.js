import { VueView, createViewContext, vueRender } from "jupyter-vue";
import "vuetify/styles";
import colors from "vuetify/lib/util/colors.mjs";
import { createVuetify, useTheme } from "vuetify";
import * as components from "vuetify/components";
import * as labComponents from "vuetify/labs/components";
import * as directives from "vuetify/directives";
import { ThemeColorsModel, ThemeModel } from "./Themes";
import { addApp } from "./VuetifyApp";

// Every widget view gets its own Vue app, but all views for one widget manager
// should share a single Vuetify plugin and theme state.
const managerStateByWidgetManager = new WeakMap();

function getManagerState(widgetManager) {
  let managerState = managerStateByWidgetManager.get(widgetManager);
  if (!managerState) {
    managerState = {
      initializedThemes: new WeakSet(),
      vuetify: createVuetify({
        components: {
          ...components,
          ...labComponents,
        },
        directives,
      }),
    };
    managerStateByWidgetManager.set(widgetManager, managerState);
  }
  return managerState;
}

const observer = new MutationObserver((mutationList) => {
  for (const mutation of mutationList) {
    if (mutation.type === "childList") {
      const overlay = document.querySelector(".v-overlay-container");
      if (overlay) {
        overlay.classList.add("vuetify-styles");
        overlay.addEventListener("keydown", (event) => {
          event.stopPropagation();
        });
      }
    }
  }
});
observer.observe(document.body, { childList: true });

export class VuetifyView extends VueView {
  addPlugins(vueApp) {
    super.addPlugins(vueApp);
    const { vuetify } = getManagerState(this.model.widget_manager);
    this.el.classList.add("vuetify-styles");
    document.querySelector("html").style.fontSize = "16px";
    vueApp.use(vuetify);
    addApp(vueApp);
  }

  async beforeViewRender() {
    await super.beforeViewRender();
    const models = await Promise.all(
      Object.values(this.model.widget_manager._models)
    );
    this.themeModel = models.find((m) => m instanceof ThemeModel);
    models
      .filter((m) => m instanceof ThemeColorsModel)
      .forEach((m) => {
        if (m.get("_theme_name") === "light") {
          this.themeLightModel = m;
        } else if (m.get("_theme_name") === "dark") {
          this.themeDarkModel = m;
        }
      });
  }

  onSetup() {
    super.onSetup();
    this.setupTheme(useTheme());
  }

  /** @override */
  vueComponent() {
    const view = this;
    return {
      provide: {
        viewCtx: createViewContext(view),
      },
      setup: () => {
        view.onSetup();
        return () => vueRender(view.model, view);
      },
    };
  }

  setupTheme(theme) {
    if (!this.themeModel) {
      return;
    }
    const managerState = getManagerState(this.model.widget_manager);
    if (!managerState.initializedThemes.has(theme)) {
      initializeTheme(
        theme,
        this.themeModel,
        this.themeLightModel,
        this.themeDarkModel
      );
      managerState.initializedThemes.add(theme);
    }
  }
}

function initializeTheme(theme, themeModel, themeLightModel, themeDarkModel) {
  if (ThemeModel.themeManager) {
    const setAutoTheme = () => {
      if (themeModel.get("dark") === null) {
        const isDark = document.body.dataset.jpThemeLight === "false";
        theme.global.name.value = isDark ? "dark" : "light";
        themeModel.set("dark_jlab", isDark);
        themeModel.save_changes();
      }
    };
    ThemeModel.themeManager.themeChanged.connect(() => {
      setAutoTheme();
    });
    setAutoTheme();
  }

  const onDark = () => {
    theme.global.name.value = themeModel.get("dark") ? "dark" : "light";
  };

  const onColorsLight = () => {
    mergeThemeColors(theme, "light", getColors(themeLightModel));
  };
  onColorsLight();

  const onColorsDark = () => {
    mergeThemeColors(theme, "dark", getColors(themeDarkModel));
  };
  onColorsDark();

  if (themeModel.get("dark") !== null) {
    onDark();
  } else if (document.body.dataset.jpThemeLight) {
    const isDark = document.body.dataset.jpThemeLight === "false";
    theme.global.name.value = isDark ? "dark" : "light";
    themeModel.set("dark_jlab", isDark);
    themeModel.save_changes();
  } else if (document.body.classList.contains("theme-dark")) {
    theme.global.name.value = "dark";
    themeModel.set("dark", true);
    themeModel.save_changes();
  } else if (document.body.classList.contains("theme-light")) {
    themeModel.set("dark", false);
    themeModel.save_changes();
  }

  themeModel.on("change:dark", onDark);
  themeLightModel.on("change", onColorsLight);
  themeDarkModel.on("change", onColorsDark);
}

function mergeThemeColors(theme, themeName, colors) {
  const themeConfig = theme.themes.value[themeName];
  themeConfig.colors = {
    ...(themeConfig.colors || {}),
    ...colors,
  };
}

function parseColor(colorStr) {
  const parts = colorStr.split(".").slice(1);
  let result = colors;

  parts.forEach((part) => {
    result = result[part];
  });

  return typeof result === "string" ? result : result.base;
}

function getColors(colorModel) {
  const colors = Object.fromEntries(
    Object.entries(colorModel.attributes)
      .filter(
        ([key]) =>
          !key.startsWith("_") &&
          !["accent", "anchor", "custom_theme_colors"].includes(key)
      )
      .map(([key, value]) => [
        key.replace(/_/g, "-"),
        value.startsWith("colors.") ? parseColor(value) : value,
      ])
  );
  return {
    ...colors,
    ...(colorModel.get("custom_theme_colors") || {}),
  };
}
