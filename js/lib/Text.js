import {
  WidgetModel, DOMWidgetModel,
  WidgetView, DOMWidgetView,
  unpack_models
} from '@jupyter-widgets/base';



import { VuetifyWidgetModel } from './VuetifyWidget';


export
class TextModel extends VuetifyWidgetModel {

  defaults() {
    return {...super.defaults(), ... {
      _model_name: "TextModel",
      value: "",
    }};
  }

  vueRender(createElement) {
    const model = this;
    return createElement({
        data() {
            return {
                    value: model.get("value"),
            };
        },
        created() {
            model.on("change:value", () => this.value = model.get("value"));
        },
        render(createElement) {
            return this._v(this.value);
        }
    })
  }
}

TextModel.serializers = {
    ...VuetifyWidgetModel.serializers,
  };


