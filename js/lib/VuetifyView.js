import { DOMWidgetView } from '@jupyter-widgets/base';
import Vue from 'vue';

// Custom View. Renders the widget model.
export class VuetifyView extends DOMWidgetView {
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
                        this.ipyvuetify_app = createElement("v-app", [this.vueRender(createElement, model)]);
                    }
                    return this.ipyvuetify_app;
                }
            });
        });
    }

    vueRender(createElement, model) {
        const widgetView = this;
        let tag = model.getVuetifyTag();
        if (tag === "html") {
            return createElement(
                model.get("tag"), {
                    ...model.get("vstyle") && {style: model.get("vstyle")},
                    ...model.get("vclass") && {class: model.get("vclass")},
                    ...model.get("attributes"),
                    ...model.get("slot") && {slot: model.get("slot")}
                },
                model.get("children").map(child => (typeof child === "string") ? child : this.vueRender(createElement, child)));
        }
        const elem = createElement({
            data() {
                return {
                    v_model: model.get("v_model")
                };
            },
            created() {
                widgetView.addListeners(model, this);
            },
            render(createElement) {
                return createElement(
                    tag,
                    widgetView.createContent(model, this),
                    widgetView.renderChildren(createElement, model, this));
            }
        }, {...model.get("slot") && {slot: model.get("slot")}});

        /* Impersonate the wrapped component (e.g. v-tabs uses this name to detect v-tab en v-tab-item) */
        elem.componentOptions.Ctor.options.name = tag;
        return elem;
    }

    eventToObject(event) {
        let props = undefined;
        switch (event.constructor) {
            case MouseEvent:
                props = ["altKey", "ctrlKey", "metaKey", "shiftKey", "offsetX", "offsetY", "clientX", "clientY", "pageX", "pageY", "screenX", "screenY", "shiftKey", "x", "y"];
                break;
            case WheelEvent:
                props = ["altKey", "ctrlKey", "metaKey", "shiftKey", "offsetX", "offsetY", "clientX", "clientY", "pageX", "pageY", "screenX", "screenY", "shiftKey", "x", "y", "wheelDelta", "wheelDeltaX", "wheelDeltaY"]
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

    registerChangedEvents(model, vueModel) {

        const previous = model.previous("_events") || [];
        const current = model.get("_events");

        const removed = previous.filter(e => !current.includes(e));
        const added = current.filter(e => !previous.includes(e));

        removed.forEach(e => vueModel.$children[0].$off(e));
        added.forEach(name => {
            vueModel.$children[0].$on(name, (e) => {
                model.send({event: name, data: this.eventToObject(e)});
            });
        });
    }

    registerAllEvents(model, vueModel) {
        (model.get("_events") || []).forEach(name => {
            vueModel.$children[0].$on(name, (e) => {
                model.send({event: name, data: this.eventToObject(e)});
            });
        });
    }

    addListeners(model, vueModel) {
        const listener = () => {
            vueModel.$forceUpdate();
        };
        const use = (key) =>
            !key.startsWith("_") && !["v_model"].includes(key);

        model.keys()
            .filter(use)
            .forEach(key => model.on("change:"+key, listener));

        model.on("change:v_model", () => {
            if (model.get("v_model") !== vueModel.v_model) {
                vueModel.v_model = model.get("v_model");
            }
        });
    }

    createAttrsMapping(model) {
        const useAsAttr = (key) =>
            model.get(key) !== null && !key.startsWith("_") && !["layout", "children", "slot", "_events", "v_model", "vstyle", "vclass"].includes(key);

        return model.keys()
            .filter(useAsAttr)
            .reduce((result, key) => {
                result[key.replace(/_/g, "-")] = model.get(key);
                return result;
            }, {})
    }

    createEventMapping(model) {
        return (model.get("_events") || [])
            .reduce((result, event) => {
                result[event] = (e) => {
                    model.send({event: event, data: this.eventToObject(e)});
                    model.save_changes();
                };
                return result;
            }, {});
    }

    createContent(model, vueModel) {
        return {
            on: this.createEventMapping(model),
            ...model.get("vstyle") && {style: model.get("vstyle")},
            ...model.get("vclass") && {class: model.get("vclass")},
            attrs: this.createAttrsMapping(model),
            ...model.get("v_model") !== "!!disabled!!" && {
                model: {
                    value: vueModel.v_model,
                    callback: (v) => {
                        model.set("v_model", v === undefined ? null : v);
                        model.save_changes();
                    },
                    expression: "v_model"
                }
            }
        }
    }

    renderChildren(createElement, model, vueModel) {
        if (!vueModel.childCache) {
            vueModel.childCache = {};
        }
        const childViewModels = model.get("children").map(child => {
            if (typeof (child) === "string") {
                return child;
            } else {
                if (vueModel.childCache[child.cid]) {
                    return vueModel.childCache[child.cid];
                } else {
                    const vm = this.vueRender(createElement, child);
                    vueModel.childCache[child.cid] = vm;
                    return vm;
                }
            }
        });

        /* Remove unused components */
        const childIds = model.get("children").map(child => child.cid);
        Object.keys(vueModel.childCache)
            .filter(key => !childIds.includes(key))
            .forEach(key => delete vueModel.childCache[key]);
        return childViewModels
    }
}
