import { VuetifyBaseView } from './VuetifyBaseView';
import { vueTemplateRender } from './VueTemplateRenderer';

export class VuetifyTemplateView extends VuetifyBaseView {
    vueRender(createElement) {
        return vueTemplateRender(createElement, this.model, this);
    }
}
