/* Jupyter (notebook, lab, voila): ipyvuetify brings its own Vuetify, with styles scoped
 * to .vuetify-styles. nodeps.js (Solara) replaces this module with
 * nodepsVuetifyPlugin.js, see webpack.config.js.
 */
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as labComponents from "vuetify/labs/components";
import * as directives from "vuetify/directives";

export function createVuetifyPlugin() {
  return createVuetify({
    components: {
      ...components,
      ...labComponents,
    },
    directives,
  });
}
