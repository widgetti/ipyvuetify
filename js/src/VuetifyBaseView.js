import { DOMWidgetView } from '@jupyter-widgets/base';
import Vue from 'vue';
import { getContainer } from './jupyterEnvironment';

export class VuetifyBaseView extends DOMWidgetView {
    remove() {
        this.vueApp.$destroy();
        return super.remove();
    }

    createDivs(elem) {
        if (!elem) {
            elem = document.body;
        }

        /* Scope vuetify styles for overlays to this element */
        const vuetifyStyles = document.createElement('DIV');
        vuetifyStyles.classList.add('vuetify-styles');
        vuetifyStyles.setAttribute('id', 'vuetify-styles');
        elem.insertBefore(vuetifyStyles, elem.children[0]);

        /* Overlays wil be rendered here (e.g. v-menu, v-tooltip and dialog). */
        const overlay = document.createElement('DIV');
        overlay.setAttribute('vuetify-overlay', true);
        overlay.classList.add('application');
        overlay.classList.add('theme--light');
        vuetifyStyles.appendChild(overlay);

        /* Set the Vuetify data-app attribute. Needed for Slider and closing overlays
         * (click-outside mixin) */
        elem.setAttribute('data-app', true);
    }

    render() {
        super.render();
        this.displayed.then(() => {
            if (!document.getElementById('vuetify-styles')) {
                this.createDivs(getContainer());
            }

            const vueEl = document.createElement('div');
            this.el.appendChild(vueEl);

            this.vueApp = new Vue({
                el: vueEl,

                render: (createElement) => {
                    // TODO: Don't use v-app in embedded mode
                    /* Prevent re-rendering of toplevel component. This happens on button-click in
                     * v-menu */
                    if (!this.ipyvuetifyApp) {
                        this.ipyvuetifyApp = createElement('div', { class: 'vuetify-styles' }, [
                            createElement('v-app', [
                                this.vueRender(createElement)])]);
                    }
                    return this.ipyvuetifyApp;
                },
            });
        });
    }

    vueRender(createElement) {} // eslint-disable-line no-unused-vars
}
