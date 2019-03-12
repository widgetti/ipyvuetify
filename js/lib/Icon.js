import {
  WidgetModel, DOMWidgetModel,
  WidgetView, DOMWidgetView,
  unpack_models
} from '@jupyter-widgets/base';



import { VuetifyWidgetModel } from './VuetifyWidget';


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

  vueRender(createElement) {
    const model = this;
    return createElement({
        data() {
            return {
                    color: model.get("color"),
                    dark: model.get("dark"),
                    disabled: model.get("disabled"),
                    large: model.get("large"),
                    left: model.get("left"),
                    light: model.get("light"),
                    medium: model.get("medium"),
                    right: model.get("right"),
                    small: model.get("small"),
                    size: model.get("size"),
                    value: model.get("value"),
                    xLarge: model.get("xLarge"),
            };
        },
        created() {
            model.on("change:color", () => this.color = model.get("color"));
            model.on("change:dark", () => this.dark = model.get("dark"));
            model.on("change:disabled", () => this.disabled = model.get("disabled"));
            model.on("change:large", () => this.large = model.get("large"));
            model.on("change:left", () => this.left = model.get("left"));
            model.on("change:light", () => this.light = model.get("light"));
            model.on("change:medium", () => this.medium = model.get("medium"));
            model.on("change:right", () => this.right = model.get("right"));
            model.on("change:small", () => this.small = model.get("small"));
            model.on("change:size", () => this.size = model.get("size"));
            model.on("change:value", () => this.value = model.get("value"));
            model.on("change:xLarge", () => this.xLarge = model.get("xLarge"));
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

IconModel.serializers = {
    ...VuetifyWidgetModel.serializers,
  };


