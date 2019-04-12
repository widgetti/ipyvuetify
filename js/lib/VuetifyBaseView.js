import {DOMWidgetView} from '@jupyter-widgets/base';
import Vue from 'vue';

export class VuetifyBaseView extends DOMWidgetView {
    render() {
        super.render();
        this.displayed.then(() => {

            /* Set the Vuetify data-app attribute on a higher level element so overlays get rendered at the right
             * position (e.g. with v-menu and v-tooltip)
             */
            const elem = document.getElementById("site");
            if (!elem.hasAttribute("data-app")) {
                elem.setAttribute("data-app", true);
            }

            const model = this.model;
            this.vueApp = new Vue({
                el: this.el,

                render: createElement => {
                    // TODO: Don't use v-app in embedded mode
                    /* Prevent re-rendering of toplevel component. This happens on button-click in v-menu */
                    if (!this.ipyvuetify_app) {
                        this.ipyvuetify_app = createElement("v-app", [this.vueRender(createElement)]);
                    }
                    return this.ipyvuetify_app;
                }
            });
        });
    }

    vueRender(createElement) {}

    eventToObject(event) {
        let props = undefined;
        switch (event.constructor) {
            case MouseEvent:
                props = ["altKey", "ctrlKey", "metaKey", "shiftKey", "offsetX", "offsetY", "clientX", "clientY", "pageX", "pageY", "screenX", "screenY", "shiftKey", "x", "y"];
                break;
            case WheelEvent:
                props = ["altKey", "ctrlKey", "metaKey", "shiftKey", "offsetX", "offsetY", "clientX", "clientY", "pageX", "pageY", "screenX", "screenY", "shiftKey", "x", "y", "wheelDelta", "wheelDeltaX", "wheelDeltaY"]
            // TODO: More events
        }

        if (!props) {
            return event;
        }

        return props.reduce(
            (result, key) => {
                result[key] = event[key];
                return result},
            {});
    }
}