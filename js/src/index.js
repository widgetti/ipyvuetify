import "typeface-roboto";
import "material-design-icons-iconfont/dist/material-design-icons.css";
import "@mdi/font/css/materialdesignicons.css";
import "./styles.css";

export { VuetifyView } from "./VuetifyView";
export * from "./generated";
export { HtmlModel } from "./Html";
export { VuetifyTemplateModel } from "./VuetifyTemplate";
export { ThemeModel, ThemeColorsModel } from "./Themes";
export { Vue, Vuetify } from "./plugins/vuetify";

export const { version } = require("../package.json"); // eslint-disable-line global-require
