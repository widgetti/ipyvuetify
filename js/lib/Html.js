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
                attributes: null,
            }};
    }

    vueRender(createElement) {
        const model = this;
        let elem = createElement(
            model.get("tag"), {
                ...model.get("attributes"),
                ...model.get("slot") && {slot: model.get("slot")}
            },
            model.vueRenderChildren(createElement));
        return elem;
     }
}

HtmlModel.serializers = {
    ...VuetifyWidgetModel.serializers,
};
