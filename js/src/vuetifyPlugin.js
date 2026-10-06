// Jupyter: ipyvuetify brings its own Vuetify. nodeps.js (Solara) replaces this module with
// nodepsVuetifyPlugin.js, so it does not bundle a second copy (see webpack.config.js).
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as labComponents from "vuetify/labs/components";
import * as directives from "vuetify/directives";

export const createVuetifyPlugin = () =>
  createVuetify({
    components: { ...components, ...labComponents },
    directives,
  });
