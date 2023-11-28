/* eslint camelcase: off */
import { VueTemplateModel } from "jupyter-vue";
import { version } from "./version";

export class VuetifyTemplateModel extends VueTemplateModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "VuetifyTemplateModel",
        _view_name: "VuetifyView",
        _view_module: "jupyter-vuetify",
        _model_module: "jupyter-vuetify",
        _view_module_version: version,
        _model_module_version: version,
      },
    };
  }
}

VuetifyTemplateModel.serializers = {
  ...VueTemplateModel.serializers,
};
