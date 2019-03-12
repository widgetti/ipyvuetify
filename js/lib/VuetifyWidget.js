import {
  WidgetModel, DOMWidgetModel,
  WidgetView, DOMWidgetView,
  unpack_models
} from '@jupyter-widgets/base';





export
class VuetifyWidgetModel extends DOMWidgetModel {

  defaults() {
    return {...super.defaults(), ... {
      _view_name: "VuetifyView",
      _model_name: "VuetifyWidgetModel",
      _view_module: "jupyter-vuetify",
      _model_module: "jupyter-vuetify",
      _view_module_version: "0.1.0",
      _model_module_version: "0.1.0",
      children: undefined,
    }};
  }

  vueRenderChildren(createElement) {
    return this.get("children").map(c => c.vueRender(createElement));
  }
}

VuetifyWidgetModel.serializers = {
    ...DOMWidgetModel.serializers,
    children: { deserialize: unpack_models },
  };


