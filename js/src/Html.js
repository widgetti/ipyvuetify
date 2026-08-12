/* eslint camelcase: off */
import { HtmlModel as VueHtmlModel } from "jupyter-vue";
import { version } from "./version";

export class HtmlModel extends VueHtmlModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "HtmlModel",
        _view_name: "VuetifyView",
        _view_module: "jupyter-vuetify",
        _model_module: "jupyter-vuetify",
        _view_module_version: version,
        _model_module_version: version,
      },
    };
  }
}

HtmlModel.serializers = {
  ...VueHtmlModel.serializers,
};
