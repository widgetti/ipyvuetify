import { DOMWidgetView } from '@jupyter-widgets/base';
import Vue from 'vue';

// Custom View. Renders the widget model.
export class VuetifyView extends DOMWidgetView {
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

                    if (!this.ipyvuetify_app) {
                        this.ipyvuetify_app = createElement("v-app", [model.vueRender(createElement)]);
                    }
                    return this.ipyvuetify_app;
                }
            });
        });
    }
}

export function eventToObject(event) {
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

export function registerChangedEvents(model, component) {

    const previous = model.previous("events") || [];
    const current = model.get("events");

    const removed = previous.filter(e => !current.includes(e));
    const added = current.filter(e => !previous.includes(e));

    removed.forEach(e => component.$children[0].$off(e));
    added.forEach(name => {
        component.$children[0].$on(name, (e) => {
            model.send({event: name, data: eventToObject(e)});
        });
    });
}

export function registerAllEvents(model, component) {
    (model.get("events") || []).forEach(name => {
        component.$children[0].$on(name, (e) => {
            model.send({event: name, data: eventToObject(e)});
        });
    });
}

export function addListeners(model, component) {
    const listener = () => {
        component.$forceUpdate();
    };
    const use = (key) =>
        !key.startsWith("_") && !["v_model"].includes(key);

    model.keys()
        .filter(use)
        .forEach(key => model.on("change:"+key, listener));

    model.on("change:v_model", () => {
        if (model.get("v_model") !== component.v_model) {
            component.v_model = model.get("v_model");
        }
    });
}

export function createAttrsMapping(model) {
    const useAsAttr = (key) =>
        model.get(key) !== null && !key.startsWith("_") && !["layout", "children", "slot", "events", "v_model", "vstyle", "vclass"].includes(key);

    return model.keys()
        .filter(useAsAttr)
        .reduce((result, key) => {
            result[key.replace(/_/g, "-")] = model.get(key);
            return result;
        }, {})
}

export function createEventMapping(model) {
    const mapping = (model.get("events") || [])
        .reduce((result, event) => {
            result[event] = (e) => {
                model.send({event: event, data: eventToObject(e)});
                model.save_changes();
            };
            return result;
    }, {});
    return mapping;
}

export function createContent(model, vm, name) {
    return {
        on: createEventMapping(model),
        ...model.get("vstyle") && {style: model.get("vstyle")},
        ...model.get("vclass") && {class: model.get("vclass")},
        attrs: createAttrsMapping(model),
        ...model.get("v_model") !== "!!disabled!!" && {
            model: {
                value: vm.v_model,
                callback: (v) => {
                    model.set("v_model", v === undefined ? null : v);
                    model.save_changes();
                },
                expression: "v_model"
            }
        }
    }
}

export function renderChildren(component, model, createElement) {
    if (!component.childCache) {
        component.childCache = {};
    }
    const childViewModels = model.get("children").map(c => {
        if (typeof (c) === "string") {
            return c;
        } else {
            if (component.childCache[c.cid]) {
                return component.childCache[c.cid];
            } else {
                const vm = c.vueRender(createElement);
                component.childCache[c.cid] = vm;
                return vm;
            }
        }
    });

    /* Remove unused components */
    const childIds = model.get("children").map(c => c.cid);
    Object.keys(component.childCache)
        .filter(key => !childIds.includes(key))
        .forEach(key => delete component.childCache[key]);
    return childViewModels
}
