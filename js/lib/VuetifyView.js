import {VuetifyBaseView} from "./VuetifyBaseView";

export class VuetifyView extends VuetifyBaseView {

    vueRender(createElement) {
        return this._vueRender(createElement, this.model);
    }

    _vueRender(createElement, model) {
        const widgetView = this;
        if (model.get("_view_name") !== "VuetifyView") {
            return createElement(VuetifyBaseView.createObjectForNestedModel(model, widgetView));
        }
        let tag = model.getVuetifyTag();
        if (tag === "html") {
            if (model.get("tag").toLowerCase().includes("script")) {
                return;
            }
            return createElement(
                model.get("tag"), {
                    ...model.get("style_") && {style: model.get("style_")},
                    ...model.get("class_") && {class: model.get("class_")},
                    ...model.get("slot") && {slot: model.get("slot")}
                },
                model.get("children").map(child => (typeof child === "string") ? child : this._vueRender(createElement, child)));
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
            model.get(key) !== null && !key.startsWith("_") && !["layout", "children", "slot", "_events", "v_model", "style_", "class_"].includes(key);

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
            ...model.get("style_") && {style: model.get("style_")},
            ...model.get("class_") && {class: model.get("class_")},
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
                    const vm = this._vueRender(createElement, child);
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
