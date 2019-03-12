import * as widgets from '@jupyter-widgets/base';
import Vue from 'vue';
import Vuetify from 'vuetify';

import 'vuetify/dist/vuetify.min.css';
// import 'https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900|Material+Icons';
import './styles.css';

Vue.use(Vuetify);

export class VuetifyModel2 extends widgets.DOMWidgetModel {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: 'VuetifyModel2',
            _view_name: 'VuetifyView2',
            _model_module: 'jupyter-vuetify',
            _view_module: 'jupyter-vuetify',
            _model_module_version: '0.1.0',
            _view_module_version: '0.1.0',
        };
    }

    vueRenderChildren(createElement) {
        return this.get("children").map(c => c.vueRender(createElement));
    }
}

VuetifyModel2.serializers = {
    ...widgets.DOMWidgetModel.serializers,
    children: {deserialize: widgets.unpack_models},
    // child: { deserialize: widgets.unpack_models },
    // icon: {deserialize: widgets.unpack_models},
    // value: { deserialize: widgets.unpack_models },
    // control: { deserialize: widgets.unpack_models },
};

// Custom View. Renders the widget model.
export class VuetifyView2 extends widgets.DOMWidgetView {
    render() {
        super.render();
        this.displayed.then(() => {
            this.vueApp = new Vue({
                el: this.el,
                render: createElement => {
                    return createElement("v-app", [
                        createElement("div", {}, [this.model.vueRender(createElement)])]);
                }
            });
        });
    }
}

export class TextModel2 extends VuetifyModel2 {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: 'TextModel',
        };
    }

    vueRender(createElement) {
        const model = this;
        console.log("TextModel-vueRender3");
        return createElement({
            data() {
                return {
                    value: model.get('value')
                }
            },
            created() {
                model.on('change:value', () => this.value = model.get("value"));
            },
            render(createElement) {
                return this._v(this.value);
            }
        })
    }
}

export class IconModel2 extends VuetifyModel2 {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: 'IconModel',
        };
    }

    vueRender(createElement) {
        const model = this;
        window.bla = model;
        const keys = ['color', 'dark', 'disabled', 'large', 'left', 'light', 'medium', 'right', 'small', 'size', 'xLarge'];
        return createElement({
            data() {
                return keys
                    .concat("value")
                    .filter(k => model.get(k))
                    .reduce(
                        (map, k) => (map[k] = model.get(k), map),
                        {});
            },
            created() {
                keys
                    .concat("value")
                    .forEach(k => model.on("change:" + k, () => this[k] = model.get(k)));
            },
            render(createElement) {
                return createElement('v-icon', {
                        attrs: keys.reduce((map, k) => (map[k] = this[k], map), {})
                    },
                    this.value);
            }
        })
    }
}

export class GenericModel2 extends VuetifyModel2 {
    // this.name = "";
    // keys = [];
    // element = "";

    defaults() {
        const model = this;
        return {
            ...super.defaults(),
            _model_name: model.name,
        };
    }

    vueRender(createElement) {
        const model = this;
        return createElement({
            data() {
                return keys
                    .filter(k => model.get(k))
                    .reduce(
                        (map, k) => (map[k] = model.get(k), map),
                        {});
            },
            created() {
                keys.forEach(k => model.on("change:" + k, () => this[k] = model.get(k)));
            },
            render(createElement) {
                return createElement(element, {
                        attrs: keys.reduce((map, k) => (map[k] = this[k], map), {})
                    },
                    model.vueRenderChildren(createElement)
                );
            }
        });
    }
}

function makeElem(createElement, model, element, keys) {
    return createElement({
        data() {
            return keys
                .filter(k => model.get(k))
                .reduce(
                    (map, k) => (map[k] = model.get(k), map),
                    {});
        },
        created() {
            keys.forEach(k => model.on("change:" + k, () => this[k] = model.get(k)));
        },
        render(createElement) {
            return createElement(element, {
                    attrs: keys.reduce((map, k) => (map[k] = this[k], map), {})
                },
                model.vueRenderChildren(createElement)
            );
        }
    });
}

export class ButtonModel2 extends VuetifyModel2 {
    defaults() {
        return {
            ...super.defaults(),
            _model_name: 'ButtonModel',
        };
    }

    vueRender(createElement) {
        return makeElem(
            createElement,
            this,
            "v-btn",
            ['absolute', 'block', 'bottom', 'color', 'dark', 'depressed', 'exact', 'fab',
                'fixed', 'flat', 'href', 'icon', 'large', 'left', 'light', 'loading', 'outline',
                'right', 'ripple', 'round', 'small', 'target', 'top', 'type']);
    }
}
