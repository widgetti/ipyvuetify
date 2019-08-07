import { createObjectForNestedModel, eventToObject, vueRender } from './VueRenderer'; // eslint-disable-line import/no-cycle
import { VuetifyWidgetModel } from './generated';
import { VuetifyTemplateModel } from './VuetifyTemplate';

export function vueTemplateRender(createElement, model, parentView) {
    return createElement(createComponentObject(model, parentView));
}

function createComponentObject(model, parentView) {
    if (model instanceof VuetifyWidgetModel) {
        return {
            render(createElement) {
                return vueRender(createElement, model, parentView);
            },
        };
    }
    if (!(model instanceof VuetifyTemplateModel)) {
        return createObjectForNestedModel(model, parentView);
    }
    return {
        data() {
            return createDataMapping(model);
        },
        created() {
            addModelListeners(model, this);
        },
        watch: createWatches(model, parentView),
        methods: createMethods(model, parentView),
        components: createComponents(model.get('components') || {}, parentView),
        template: model.get('template'),
    };
}

function createDataMapping(model) {
    return model.keys()
        .filter(prop => !prop.startsWith('_') && !['events', 'template', 'components'].includes(prop))
        .reduce((result, prop) => {
            result[prop] = model.get(prop); // eslint-disable-line no-param-reassign
            return result;
        }, {});
}

function addModelListeners(model, vueModel) {
    model.keys()
        .filter(prop => !prop.startsWith('_') && !['v_model', 'components'].includes(prop))
        // eslint-disable-next-line no-param-reassign
        .forEach(prop => model.on(`change:${prop}`, () => { vueModel[prop] = model.get(prop); }));
}

function createWatches(model, parentView) {
    return model.keys()
        .filter(prop => !prop.startsWith('_') && !['events', 'template', 'components'].includes(prop))
        .reduce((result, prop) => {
            result[prop] = (value) => { // eslint-disable-line no-param-reassign
                model.set(prop, value === undefined ? null : value);
                model.save_changes(model.callbacks(parentView));
            };
            return result;
        }, {});
}

function createMethods(model, parentView) {
    return model.get('events').reduce((result, event) => {
        // eslint-disable-next-line no-param-reassign
        result[event] = value => model.send(
            { event, data: eventToObject(value) },
            model.callbacks(parentView),
        );
        return result;
    }, {});
}

function createComponents(components, parentView) {
    return Object.entries(components)
        .reduce((result, [name, model]) => {
            // eslint-disable-next-line no-param-reassign
            result[name] = createComponentObject(model, parentView);
            return result;
        }, {});
}
