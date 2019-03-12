import { DOMWidgetView } from '@jupyter-widgets/base';
import Vue from 'vue';

import Vuetify from 'vuetify';

import 'vuetify/dist/vuetify.min.css';

import './styles.css';

Vue.use(Vuetify);


// Custom View. Renders the widget model.
export class VuetifyView extends DOMWidgetView {
    render() {
        super.render();
        this.displayed.then(() => {
            this.vueApp = new Vue({
                el: this.el,
                render: createElement => {
                    // TODO: Don't use v-app in embedded mode
                    return createElement("v-app", [
                        createElement("div", {}, [this.model.vueRender(createElement)])]);
                }
            });
        });
    }
}
