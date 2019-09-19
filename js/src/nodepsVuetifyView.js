import { DOMWidgetView } from '@jupyter-widgets/base';
import { vueRender } from 'jupyter-vue';

export class VuetifyView extends DOMWidgetView {
    vueRender(createElement) {
        return vueRender(createElement, this.model, this);
    }
}
