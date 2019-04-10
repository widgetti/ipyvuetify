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
                render(createElement) {
                    // TODO: Don't use v-app in embedded mode
                    if (!this.ipyvuetify_app) {
                        this.ipyvuetify_app = createElement("v-app", [vueRender(createElement, model)]);
                    }
                    return this.ipyvuetify_app;
                }
            });
        });
    }
}

function vueRender(createElement, model) {
    const tag = model.getVuetifyTag();
    const elem = createElement({
        data() {
            return {
                v_model: model.get("v_model")
            };
        },
        created() {
            addListeners(model, this);
        },
        render(createElement) {
            return createElement(
                tag,
                createContent(model, this),
                renderChildren(this, model, createElement));
        }
    }, {...model.get("slot") && {slot: model.get("slot")}});

    /* Impersonate the wrapped component (e.g. v-tabs uses this name to detect v-tab en v-tab-item) */
    elem.componentOptions.Ctor.options.name = tag;
    return elem;
}

function eventToObject(event) {
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

function registerChangedEvents(model, component) {

    const previous = model.previous("_events") || [];
    const current = model.get("_events");

    const removed = previous.filter(e => !current.includes(e));
    const added = current.filter(e => !previous.includes(e));

    removed.forEach(e => component.$children[0].$off(e));
    added.forEach(name => {
        component.$children[0].$on(name, (e) => {
            model.send({event: name, data: eventToObject(e)});
        });
    });
}

function registerAllEvents(model, component) {
    (model.get("_events") || []).forEach(name => {
        component.$children[0].$on(name, (e) => {
            model.send({event: name, data: eventToObject(e)});
        });
    });
}

function addListeners(model, component) {
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

function createAttrsMapping(model) {
    const useAsAttr = (key) =>
        model.get(key) !== null && !key.startsWith("_") && !["layout", "children", "slot", "_events", "v_model", "vstyle", "vclass"].includes(key);

    return model.keys()
        .filter(useAsAttr)
        .reduce((result, key) => {
            result[key.replace(/_/g, "-")] = model.get(key);
            return result;
        }, {})
}

function createEventMapping(model) {
    const mapping = (model.get("_events") || [])
        .reduce((result, event) => {
            result[event] = (e) => {
                model.send({event: event, data: eventToObject(e)});
                model.save_changes();
            };
            return result;
    }, {});
    return mapping;
}

function createContent(model, vm) {
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
    const childViewModels = model.get("children").map(child => {
        if (typeof (child) === "string") {
            return child;
        } else {
            if (component.childCache[child.cid]) {
                return component.childCache[child.cid];
            } else {
                const vm = vueRender(createElement, child);
                component.childCache[child.cid] = vm;
                return vm;
            }
        }
    });

    /* Remove unused components */
    const childIds = model.get("children").map(child => child.cid);
    Object.keys(component.childCache)
        .filter(key => !childIds.includes(key))
        .forEach(key => delete component.childCache[key]);
    return childViewModels
}
