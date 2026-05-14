import "typeface-roboto";
import "material-design-icons-iconfont/dist/material-design-icons.css";
import "@mdi/font/css/materialdesignicons.css";
import "./ipyvuetify-styles.css";
import { addModule } from "jupyter-vue";
import * as Vue from "vue";
import * as Vuetify from "vuetify";

addModule("vuetify", Vuetify);

export { VuetifyView } from "./VuetifyView";
export * from "./Widgets";
export { HtmlModel } from "./Html";
export { VuetifyTemplateModel } from "./VuetifyTemplate";
export { ThemeModel, ThemeColorsModel } from "./Themes";
export { addApp } from "./VuetifyApp";

export { version } from "./version";
export { Vue, Vuetify };
