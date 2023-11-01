import * as Vue from "vue"; // eslint-disable-line import/no-extraneous-dependencies
import { VueView } from "jupyter-vue";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { VDataTable } from "vuetify/labs/VDataTable";

const observer = new MutationObserver((mutationList, observer) => {
  for (const mutation of mutationList) {
    if (mutation.type === "childList") {
      console.log("A child node has been added or removed.", mutation);
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
    console.log(
      Vue.compile(
        `<v-btn v-model="xx" :color="'primary'" :key="cc">test</v-btn>`
      )
    );
    super.addPlugins(vueApp);
    const vuetify = createVuetify({
      components: { ...components, VDataTable },
      directives,
    });
    this.el.classList.add("vuetify-styles");
    document.querySelector("html").style.fontSize = "16px";
    vueApp.use(vuetify);
  }
}
