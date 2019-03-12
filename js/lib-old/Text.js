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
class TextModel extends VuetifyWidgetModel {

  defaults() {
    return {...super.defaults(), ... {
      _model_name: "TextModel",
      value: "",
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
                    value: "",
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

