import { DOMWidgetView } from "@jupyter-widgets/base";
import { vueRender, createViewContext } from "jupyter-vue";

export class VuetifyView extends DOMWidgetView {
  vueRender(createElement) {
    return createElement({
      provide: {
        viewCtx: createViewContext(this),
      },
      render: () => {
        return vueRender(createElement, this.model, this);
      },
    });
  }
}
