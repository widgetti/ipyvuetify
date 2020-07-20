import { DOMWidgetView } from '@jupyter-widgets/base';
import Vue from 'vue'; // eslint-disable-line import/no-extraneous-dependencies
import { vueRender, createViewContext } from 'jupyter-vue';
import { getContainer } from './jupyterEnvironment';
import vuetify from './plugins/vuetify';

export class VuetifyView extends DOMWidgetView {
    remove() {
        this.vueApp.$destroy();
        return super.remove();
    }

    createDivs(elem) {
        /* Scope vuetify styles for overlays to this element */
        const vuetifyStyles = document.createElement('DIV');
        vuetifyStyles.classList.add('vuetify-styles');
        vuetifyStyles.setAttribute('id', 'vuetify-styles');
        elem.insertBefore(vuetifyStyles, elem.children[0]);

        /* Overlays wil be rendered here (e.g. v-menu, v-tooltip and dialog). */
        const overlay = document.createElement('DIV');
        overlay.setAttribute('vuetify-overlay', true);
        overlay.classList.add('v-application');
        overlay.classList.add('v-application--is-ltr');
        overlay.classList.add('theme--light');

        /* Prevent the notebook from capturing keyboard events in overlay components (e.g. Menu and
         * Dialog). The captured events were executed as commands, messing up the notebook and
         * prevented the events from reaching the designated component within the overlay. */

        overlay.addEventListener("keydown", (event) => {
            event.stopPropagation();
        });

        vuetifyStyles.appendChild(overlay);

        /* Set the Vuetify data-app attribute. Needed for Slider and closing overlays
         * (click-outside mixin) */
        elem.setAttribute('data-app', true);
    }

    render() {
        super.render();
        this.displayed.then(() => {
            if (!document.getElementById('vuetify-styles')) {
                this.createDivs(getContainer() || document.body);
            }

            const vueEl = document.createElement('div');
            this.el.appendChild(vueEl);

            this.vueApp = new Vue({
                vuetify,
                el: vueEl,
                provide: {
                    viewCtx: createViewContext(this),
                },
                render: (createElement) => {
                    // TODO: Don't use v-app in embedded mode
                    /* Prevent re-rendering of toplevel component. This happens on button-click in
                     * v-menu */
                    if (!this.ipyvuetifyApp) {
                        this.ipyvuetifyApp = createElement('div', { class: 'vuetify-styles' }, [
                            createElement('v-app', [vueRender(createElement, this.model, this)]),
                        ]);
                    }
                    return this.ipyvuetifyApp;
                },
            });
        });
    }

    vueRender(createElement) {
        return createElement({
            provide: {
                viewCtx: createViewContext(this),
            },
            render: () => {
                return vueRender(createElement, this.model, this)
            },
        });
    }
}
