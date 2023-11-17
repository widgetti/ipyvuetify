import * as Vue from "vue"; // eslint-disable-line import/no-extraneous-dependencies
import { VueView, createViewContext, vueRender } from "jupyter-vue";
import "vuetify/styles";
import colors from "vuetify/lib/util/colors.mjs";
import { createVuetify, useTheme } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { VDataTable } from "vuetify/labs/VDataTable";
import { ThemeColorsModel, ThemeModel } from "./Themes";

const observer = new MutationObserver((mutationList, observer) => {
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
    const vuetify = createVuetify({
      components: { ...components, VDataTable },
      directives,
    });
    this.el.classList.add("vuetify-styles");
    document.querySelector("html").style.fontSize = "16px";
    vueApp.use(vuetify);
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
    this.setupTheme();
  }

  /* used in pages using nodeps */
  vueRender() {
    return Vue.h({
      provide: {
        viewCtx: createViewContext(this),
      },
      render: () => {
        return vueRender(this.model, this);
      },
    });
  }

  setupTheme() {
    if (!this.themeModel) {
      return;
    }
    this.theme = useTheme();

    if (ThemeModel.themeManager) {
      const setAutoTheme = () => {
        if (this.themeModel.get("dark") === null) {
          const isDark = document.body.dataset.jpThemeLight === "false";
          this.theme.global.name.value = isDark ? "dark" : "light";
          this.themeModel.set("dark_jlab", isDark);
          this.themeModel.save_changes();
        }
      };
      ThemeModel.themeManager.themeChanged.connect(() => {
        setAutoTheme();
      }, this);
      setAutoTheme();
    }

    const onDark = () => {
      this.theme.global.name.value = this.themeModel.get("dark")
        ? "dark"
        : "light";
    };

    const onColorsLight = () => {
      this.theme.themes.value.light.colors = getColors(this.themeLightModel);
    };
    onColorsLight();

    const onColorsDark = () => {
      this.theme.themes.value.dark.colors = getColors(this.themeDarkModel);
    };
    onColorsDark();

    if (this.themeModel.get("dark") !== null) {
      onDark();
    } else if (document.body.dataset.jpThemeLight) {
      const isDark = document.body.dataset.jpThemeLight === "false";
      this.theme.global.name.value = isDark ? "dark" : "light";
      this.themeModel.set("dark_jlab", isDark);
      this.themeModel.save_changes();
    } else if (document.body.classList.contains("theme-dark")) {
      this.theme.global.name.value = "dark";
      this.themeModel.set("dark", true);
      this.themeModel.save_changes();
    } else if (document.body.classList.contains("theme-light")) {
      this.themeModel.set("dark", false);
      this.themeModel.save_changes();
    }

    Vue.onMounted(() => {
      this.themeModel.on("change:dark", onDark);
      this.themeLightModel.on("change", onColorsLight);
      this.themeDarkModel.on("change", onColorsDark);
    });

    Vue.onUnmounted(() => {
      this.themeModel.off("change:dark", onDark);
      this.themeLightModel.off("change", onColorsLight);
      this.themeDarkModel.off("change", onColorsDark);
    });
  }
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
  return _.mapKeys(
    _.mapValues(
      _.pickBy(
        { ...colorModel.attributes },
        (v, k) => !k.startsWith("_") && k !== "accent" && k !== "anchor"
      ),
      (v) => (v.startsWith("colors.") ? parseColor(v) : v)
    ),
    (v, k) => k.replace(/_/g, "-")
  );
}
