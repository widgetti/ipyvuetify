import {
    WidgetModel, DOMWidgetModel,
    WidgetView, DOMWidgetView,
    unpack_models
} from '@jupyter-widgets/base';

import { VuetifyWidgetModel } from './generated/VuetifyWidget';

export
class HtmlModel extends VuetifyWidgetModel {

    defaults() {
        return {...super.defaults(), ... {
                _model_name: "HtmlModel",
                tag: null,
            }};
    }

    getVuetifyTag() {
        return "html"
    }
}

HtmlModel.serializers = {
    ...VuetifyWidgetModel.serializers,
};
