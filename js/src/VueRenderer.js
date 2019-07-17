/* eslint camelcase: ['error', {allow: ['v_model']}] */
import { JupyterPhosphorWidget } from '@jupyter-widgets/base';
import { vueTemplateRender } from './VueTemplateRenderer'; // eslint-disable-line import/no-cycle

export function createObjectForNestedModel(model, parentView) {
    const viewPromise = parentView.create_child_view(model);

    return {
        mounted() {
            viewPromise.then(view => JupyterPhosphorWidget.attach(view.pWidget, this.$el));
        },
        render(createElement) {
            return createElement('div', { style: { display: 'flex' } });
        },
    };
}

export function eventToObject(event) {
    if (event == null) {
        return event;
    }
    let props;
    switch (event.constructor) {
        case MouseEvent:
            props = ['altKey', 'ctrlKey', 'metaKey', 'shiftKey', 'offsetX', 'offsetY', 'clientX', 'clientY', 'pageX', 'pageY', 'screenX', 'screenY', 'shiftKey', 'x', 'y'];
            break;
        case WheelEvent:
            props = ['altKey', 'ctrlKey', 'metaKey', 'shiftKey', 'offsetX', 'offsetY', 'clientX', 'clientY', 'pageX', 'pageY', 'screenX', 'screenY', 'shiftKey', 'x', 'y', 'wheelDelta', 'wheelDeltaX', 'wheelDeltaY'];
            break;
        // TODO: More events
        default:
            return event;
    }

    return props.reduce(
        (result, key) => {
            result[key] = event[key]; // eslint-disable-line no-param-reassign
            return result;
        }, {},
    );
}

export function vueRender(createElement, model, parentView) {
    if (model.get('_view_name') === 'VuetifyTemplateView') {
        return vueTemplateRender(createElement, model, parentView);
    }
    if (model.get('_view_name') !== 'VuetifyView') {
        return createElement(createObjectForNestedModel(model, parentView));
    }
    const tag = model.getVuetifyTag();
    if (tag === 'html') {
        if (model.get('tag').toLowerCase().includes('script')) {
            return undefined;
        }
        return createElement(
            model.get('tag'), {
                ...model.get('style_') && { style: model.get('style_') },
                ...model.get('class_') && { class: model.get('class_') },
                ...model.get('slot') && { slot: model.get('slot') },
            },
            model.get('children').map(child => (typeof child === 'string'
                ? child
                : vueRender(createElement, child, parentView))),
        );
    }

    const elem = createElement({
        data() {
            return {
                v_model: model.get('v_model'),
            };
        },
        created() {
            addListeners(model, this);
        },
        render(createElement2) {
            return createElement2(
                tag,
                createContent(model, this, parentView),
                renderChildren(createElement2, model, this, parentView),
            );
        },
    }, { ...model.get('slot') && { slot: model.get('slot') } });

    /* Impersonate the wrapped component (e.g. v-tabs uses this name to detect v-tab and
     * v-tab-item) */
    elem.componentOptions.Ctor.options.name = tag;
    return elem;
}

function addListeners(model, vueModel) {
    const listener = () => {
        vueModel.$forceUpdate();
    };
    const use = key => key === '_events' || (!key.startsWith('_') && !['v_model'].includes(key));

    model.keys()
        .filter(use)
        .forEach(key => model.on(`change:${key}`, listener));

    model.on('change:v_model', () => {
        if (model.get('v_model') !== vueModel.v_model) {
            vueModel.v_model = model.get('v_model'); // eslint-disable-line no-param-reassign
        }
    });
}

function createAttrsMapping(model) {
    const useAsAttr = key => model.get(key) !== null
        && !key.startsWith('_')
        && !['layout', 'children', 'slot', 'v_model', 'style_', 'class_'].includes(key);

    return model.keys()
        .filter(useAsAttr)
        .reduce((result, key) => {
            result[key.replace(/_/g, '-')] = model.get(key); // eslint-disable-line no-param-reassign
            return result;
        }, {});
}

function createEventMapping(model, parentView) {
    return (model.get('_events') || [])
        .reduce((result, event) => {
            result[event] = (e) => { // eslint-disable-line no-param-reassign
                model.send({ event, data: eventToObject(e) }, model.callbacks(parentView));
            };
            return result;
        }, {});
}

function createContent(model, vueModel, parentView) {
    return {
        on: createEventMapping(model, parentView),
        ...model.get('style_') && { style: model.get('style_') },
        ...model.get('class_') && { class: model.get('class_') },
        attrs: createAttrsMapping(model),
        ...model.get('v_model') !== '!!disabled!!' && {
            model: {
                value: vueModel.v_model,
                callback: (v) => {
                    model.set('v_model', v === undefined ? null : v);
                    model.save_changes(model.callbacks(parentView));
                },
                expression: 'v_model',
            },
        },
    };
}

function renderChildren(createElement, model, vueModel, parentView) {
    if (!vueModel.childCache) {
        vueModel.childCache = {}; // eslint-disable-line no-param-reassign
    }
    const childViewModels = model.get('children').map((child) => {
        if (typeof (child) === 'string') {
            return child;
        }
        if (vueModel.childCache[child.cid]) {
            return vueModel.childCache[child.cid];
        }
        const vm = vueRender(createElement, child, parentView);
        vueModel.childCache[child.cid] = vm; // eslint-disable-line no-param-reassign
        return vm;
    });

    /* Remove unused components */
    const childIds = model.get('children').map(child => child.cid);
    Object.keys(vueModel.childCache)
        .filter(key => !childIds.includes(key))
        // eslint-disable-next-line no-param-reassign
        .forEach(key => delete vueModel.childCache[key]);
    return childViewModels;
}
