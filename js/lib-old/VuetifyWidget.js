import {
  WidgetModel, DOMWidgetModel,
  WidgetView, DOMWidgetView,
  unpack_models
} from '@jupyter-widgets/base';

import Vue from 'vue';
import * as widgets from "@jupyter-widgets/base";
import {VuetifyModel2} from "./example";

// import {
//   data_union_serialization, array_serialization
// } from 'jupyter-dataserializers';

// import { VuetifyWidgetModel } from './VuetifyWidget';

export
class VuetifyWidgetModel extends DOMWidgetModel {

  defaults() {
    return {...super.defaults(), ... {
      _view_name: "VuetifyView",
      _model_name: "VuetifyModel",
      _view_module: "vuetify",
      _view_module_version: "0.1.0",
      _model_module_version: '0.1.0',
      children: null,
    }};
  }

  // serializers = {
  //   ...DOMWidgetModel.serializers,
  //   children: { deserialize: unpack_models },
  // };

  vueRenderChildren(createElement) {
    console.log("hier");
    return this.get("children").map(c => {
      console.log("c:", c, typeof c);
      c.vueRender(createElement)
    });
  }
}

VuetifyWidgetModel.serializers = {
  ...DOMWidgetModel.serializers,
  children: {deserialize: unpack_models},
  // child: { deserialize: widgets.unpack_models },
  // icon: {deserialize: widgets.unpack_models},
  // value: { deserialize: widgets.unpack_models },
  // control: { deserialize: widgets.unpack_models },
};

