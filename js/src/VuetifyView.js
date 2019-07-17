import { VuetifyBaseView } from './VuetifyBaseView';
import { vueRender } from './VueRenderer';

export class VuetifyView extends VuetifyBaseView {
    vueRender(createElement) {
        return vueRender(createElement, this.model, this);
    }
}
