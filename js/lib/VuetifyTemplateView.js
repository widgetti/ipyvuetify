import {DOMWidgetView} from '@jupyter-widgets/base';

import Vue from 'vue';

export class VuetifyTemplateView extends DOMWidgetView {
    render() {
        super.render();
        this.displayed.then(() => {

            /* Set the Vuetify data-app attribute on a higher level element so overlays get renderd at the right
             * position (e.g. with v-menu and v-tooltip)
             */
            const elem = document.getElementById("site");
            if (!elem.hasAttribute("data-app")) {
                elem.setAttribute("data-app", true);
            }

            const model = this.model;
            this.vueApp = new Vue({
                el: this.el,

                render(createElement) {
                    // TODO: Don't use v-app in embedded mode
                    /* Prevent re-rendering of toplevel component. This happens on button-click in v-menu */
                    if (!this.ipyvuetify_app) {
                        this.ipyvuetify_app = createElement("v-app", [createElement(createComponentObject(model))]);
                    }
                    return this.ipyvuetify_app;
                }
            });
        });
    }
}

function createComponentObject(model) {
    return {
        data() {
            return createDataMapping(model);
        },
        created() {
            addModelListeners(model, this);
        },
        watch: createWatches(model),
        methods: createMethods(model),
        components: createComponents(model.get("components") || {}),
        template: model.get("template"),
    }
}

function createDataMapping(model) {
    return model.keys()
        .filter(prop => !prop.startsWith("_") && !["events", "template", "components"].includes(prop))
        .reduce((result, prop) => {
            result[prop] = model.get(prop);
            return result;
        }, {});
}

function addModelListeners(model, component) {
    model.keys()
        .filter(prop => !prop.startsWith("_") && !["v_model", "components"].includes(prop))
        .forEach(prop => model.on("change:" + prop, () => component[prop] = model.get(prop)));
}

function createWatches(model) {
    return model.keys()
        .filter(prop => !prop.startsWith("_") && !["events", "template", "components"].includes(prop))
        .reduce((result, prop) => {
            result[prop] = function (value) {
                model.set(prop, value === undefined ? null : value);
                model.save_changes();
            };
            return result;
        }, {});
}

function createMethods(model) {
    return model.get("events").reduce((result, event) => {
        result[event] = (value) => model.send({event, data: value});
        return result;
    }, {})
}

function createComponents(components) {
    return Object.entries(components)
        .reduce((result, [name, model]) => {
            result[name] = createComponentObject(model);
            return result;
        }, {});
}
