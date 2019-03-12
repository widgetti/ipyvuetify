import {
  WidgetModel, DOMWidgetModel,
  WidgetView, DOMWidgetView,
  unpack_models
} from '@jupyter-widgets/base';

// import {
//   data_union_serialization, array_serialization
// } from 'jupyter-dataserializers';

import { VuetifyWidgetModel } from './VuetifyWidget';
import Vue from 'vue';

export
class BtnModel extends VuetifyWidgetModel {

  defaults() {
    return {...super.defaults(), ... {
      _model_name: "BtnModel",
      absolute: null,
      block: null,
      bottom: null,
      color: null,
      dark: null,
      depressed: null,
      exact: null,
      fab: null,
      fixed: null,
      flat: null,
      href: null,
      icon: null,
      large: null,
      left: null,
      light: null,
      loading: null,
      outline: null,
      right: null,
      ripple: null,
      round: null,
      small: null,
      target: null,
      top: null,
      type: "button",
    }};
  }

  // serializers = {
  //   ...VuetifyWidgetModel.serializers,
  // };

  vueRender(createElement) {
    const model = this;
    return createElement({
        data() {
            return {
                    absolute: null,
                    block: null,
                    bottom: null,
                    color: null,
                    dark: null,
                    depressed: null,
                    exact: null,
                    fab: null,
                    fixed: null,
                    flat: null,
                    href: null,
                    icon: null,
                    large: null,
                    left: null,
                    light: null,
                    loading: null,
                    outline: null,
                    right: null,
                    ripple: null,
                    round: null,
                    small: null,
                    target: null,
                    top: null,
                    type: "button",
            };
        },
        created() {
            model.on("change:absolute", () => this.value = model.get("absolute"));
            model.on("change:block", () => this.value = model.get("block"));
            model.on("change:bottom", () => this.value = model.get("bottom"));
            model.on("change:color", () => this.value = model.get("color"));
            model.on("change:dark", () => this.value = model.get("dark"));
            model.on("change:depressed", () => this.value = model.get("depressed"));
            model.on("change:exact", () => this.value = model.get("exact"));
            model.on("change:fab", () => this.value = model.get("fab"));
            model.on("change:fixed", () => this.value = model.get("fixed"));
            model.on("change:flat", () => this.value = model.get("flat"));
            model.on("change:href", () => this.value = model.get("href"));
            model.on("change:icon", () => this.value = model.get("icon"));
            model.on("change:large", () => this.value = model.get("large"));
            model.on("change:left", () => this.value = model.get("left"));
            model.on("change:light", () => this.value = model.get("light"));
            model.on("change:loading", () => this.value = model.get("loading"));
            model.on("change:outline", () => this.value = model.get("outline"));
            model.on("change:right", () => this.value = model.get("right"));
            model.on("change:ripple", () => this.value = model.get("ripple"));
            model.on("change:round", () => this.value = model.get("round"));
            model.on("change:small", () => this.value = model.get("small"));
            model.on("change:target", () => this.value = model.get("target"));
            model.on("change:top", () => this.value = model.get("top"));
            model.on("change:type", () => this.value = model.get("type"));
        },
        render(createElement) {
            return createElement('v-btn', {
                    attrs: {
                        absolute: this.absolute,
                        block: this.block,
                        bottom: this.bottom,
                        color: this.color,
                        dark: this.dark,
                        depressed: this.depressed,
                        exact: this.exact,
                        fab: this.fab,
                        fixed: this.fixed,
                        flat: this.flat,
                        href: this.href,
                        icon: this.icon,
                        large: this.large,
                        left: this.left,
                        light: this.light,
                        loading: this.loading,
                        outline: this.outline,
                        right: this.right,
                        ripple: this.ripple,
                        round: this.round,
                        small: this.small,
                        target: this.target,
                        top: this.top,
                        type: this.type,
                    }
            },
            model.vueRenderChildren(createElement));
        }
    })
  }
}

