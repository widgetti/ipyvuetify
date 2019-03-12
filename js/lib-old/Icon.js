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
class IconModel extends VuetifyWidgetModel {

  defaults() {
    return {...super.defaults(), ... {
      _model_name: "IconModel",
      color: null,
      dark: null,
      disabled: null,
      large: null,
      left: null,
      light: null,
      medium: null,
      right: null,
      small: null,
      size: null,
      value: undefined,
      xLarge: null,
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
                    color: null,
                    dark: null,
                    disabled: null,
                    large: null,
                    left: null,
                    light: null,
                    medium: null,
                    right: null,
                    small: null,
                    size: null,
                    value: null,
                    xLarge: null,
            };
        },
        created() {
            // model.on("change:color", () => this.value = model.get("color"));
            // model.on("change:dark", () => this.value = model.get("dark"));
            // model.on("change:disabled", () => this.value = model.get("disabled"));
            // model.on("change:large", () => this.value = model.get("large"));
            // model.on("change:left", () => this.value = model.get("left"));
            // model.on("change:light", () => this.value = model.get("light"));
            // model.on("change:medium", () => this.value = model.get("medium"));
            // model.on("change:right", () => this.value = model.get("right"));
            // model.on("change:small", () => this.value = model.get("small"));
            // model.on("change:size", () => this.value = model.get("size"));
            model.on("change:value", () => this.value = model.get("value"));
            // model.on("change:xLarge", () => this.value = model.get("xLarge"));
        },
        render(createElement) {
            return createElement('v-icon', {
                    attrs: {
                        color: this.color,
                        dark: this.dark,
                        disabled: this.disabled,
                        large: this.large,
                        left: this.left,
                        light: this.light,
                        medium: this.medium,
                        right: this.right,
                        small: this.small,
                        size: this.size,
                        value: this.value,
                        xLarge: this.xLarge,
                    }
            },
            this.value);
        }
    })
  }
}

