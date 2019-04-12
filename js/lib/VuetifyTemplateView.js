import {DOMWidgetView} from '@jupyter-widgets/base';

import Vue from 'vue';

export class VuetifyTemplateView extends DOMWidgetView {
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
                        this.ipyvuetify_app = createElement("v-app", [createElement(this.createComponentObject(model))]);
                    }
                    return this.ipyvuetify_app;
                }
            });
        });
    }

    createComponentObject(model) {
        const widgetView = this;
        return {
            data() {
                return widgetView.createDataMapping(model);
            },
            created() {
                widgetView.addModelListeners(model, this);
            },
            watch: this.createWatches(model),
            methods: this.createMethods(model),
            components: this.createComponents(model.get("components") || {}),
            template: model.get("template"),
        }
    }

    createDataMapping(model) {
        return model.keys()
            .filter(prop => !prop.startsWith("_") && !["events", "template", "components"].includes(prop))
            .reduce((result, prop) => {
                result[prop] = model.get(prop);
                return result;
            }, {});
    }

    addModelListeners(model, vueModel) {
        model.keys()
            .filter(prop => !prop.startsWith("_") && !["v_model", "components"].includes(prop))
            .forEach(prop => model.on("change:" + prop, () => vueModel[prop] = model.get(prop)));
    }

    createWatches(model) {
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

    createMethods(model) {
        return model.get("events").reduce((result, event) => {
            result[event] = (value) => model.send({event, data: value});
            return result;
        }, {})
    }

    createComponents(components) {
        return Object.entries(components)
            .reduce((result, [name, model]) => {
                result[name] = this.createComponentObject(model);
                return result;
            }, {});
    }
}
