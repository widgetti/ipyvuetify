import {
  WidgetModel, DOMWidgetModel,
  WidgetView, DOMWidgetView,
  unpack_models
} from '@jupyter-widgets/base';



import { VuetifyWidgetModel } from './VuetifyWidget';


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

  vueRender(createElement) {
    const model = this;
    return createElement({
        data() {
            return {
                    absolute: model.get("absolute"),
                    block: model.get("block"),
                    bottom: model.get("bottom"),
                    color: model.get("color"),
                    dark: model.get("dark"),
                    depressed: model.get("depressed"),
                    exact: model.get("exact"),
                    fab: model.get("fab"),
                    fixed: model.get("fixed"),
                    flat: model.get("flat"),
                    href: model.get("href"),
                    icon: model.get("icon"),
                    large: model.get("large"),
                    left: model.get("left"),
                    light: model.get("light"),
                    loading: model.get("loading"),
                    outline: model.get("outline"),
                    right: model.get("right"),
                    ripple: model.get("ripple"),
                    round: model.get("round"),
                    small: model.get("small"),
                    target: model.get("target"),
                    top: model.get("top"),
                    type: model.get("type"),
            };
        },
        created() {
            model.on("change:absolute", () => this.absolute = model.get("absolute"));
            model.on("change:block", () => this.block = model.get("block"));
            model.on("change:bottom", () => this.bottom = model.get("bottom"));
            model.on("change:color", () => this.color = model.get("color"));
            model.on("change:dark", () => this.dark = model.get("dark"));
            model.on("change:depressed", () => this.depressed = model.get("depressed"));
            model.on("change:exact", () => this.exact = model.get("exact"));
            model.on("change:fab", () => this.fab = model.get("fab"));
            model.on("change:fixed", () => this.fixed = model.get("fixed"));
            model.on("change:flat", () => this.flat = model.get("flat"));
            model.on("change:href", () => this.href = model.get("href"));
            model.on("change:icon", () => this.icon = model.get("icon"));
            model.on("change:large", () => this.large = model.get("large"));
            model.on("change:left", () => this.left = model.get("left"));
            model.on("change:light", () => this.light = model.get("light"));
            model.on("change:loading", () => this.loading = model.get("loading"));
            model.on("change:outline", () => this.outline = model.get("outline"));
            model.on("change:right", () => this.right = model.get("right"));
            model.on("change:ripple", () => this.ripple = model.get("ripple"));
            model.on("change:round", () => this.round = model.get("round"));
            model.on("change:small", () => this.small = model.get("small"));
            model.on("change:target", () => this.target = model.get("target"));
            model.on("change:top", () => this.top = model.get("top"));
            model.on("change:type", () => this.type = model.get("type"));
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

BtnModel.serializers = {
    ...VuetifyWidgetModel.serializers,
  };


