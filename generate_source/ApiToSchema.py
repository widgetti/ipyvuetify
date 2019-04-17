import json
import re


sizes = ['xs', 'sm', 'md', 'lg', 'xl']
display_values = ['inline',
                  'block',
                  'contents',
                  'flex',
                  'grid',
                  'inline_block',
                  'inline_flex',
                  'inline_grid',
                  'inline_table',
                  'list_item',
                  'run_in',
                  'table',
                  'table_caption',
                  'table_column_group',
                  'table_header_group',
                  'table_footer_group',
                  'table_row_group',
                  'table_cell',
                  'table_column',
                  'table_row',
                  'none',
                  'initial',
                  'inherit']

spacing_types = ['m', 'p']
spacing_directions = ['t', 'b', 'l', 'r', 'x', 'y', 'a']
spacing_sizes = ['auto'] + [str(s) for s in range(0, 6)]

keywords = ['for']


def identity(x):
    return x


def kebab_to_camel(name):
    return ''.join(
        map(
            lambda x: x.capitalize(),
            name.split('-')[1:]))


def property_to_snake_case(name):
    return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()


def make_boolean_prop(): return {
    'type': 'boolean',
    'allowNull': True,
    'default': None}


def make_d_type_props():
    return [(f'd_{d}', make_boolean_prop())
            for d in display_values]


def make_grid_list_props():
    return [(f'grid_list_{s}', make_boolean_prop())
            for s in sizes]


def make_grit_props(prefix, start, end):
    return [(f'{prefix}{s}{n}', make_boolean_prop())
            for s in sizes
            for n in range(start, end)]


def make_spacing_props():
    return [(f'{t}{d}_{s}', make_boolean_prop())
            for t in spacing_types
            for d in spacing_directions
            for s in spacing_sizes]


def api_type_to_schema_type(api_type):
    # Vuetify api schema contains casing errors
    if type(api_type) is str:
        api_type = api_type.casefold()

    if api_type in ['boolean', 'string', 'object', 'array']:
        return api_type
    if api_type == 'number':
        return 'float'
    if type(api_type) is list:
        return 'union'
    if api_type == 'function':
        # Not supported
        return None

    print(f'Unknown type: {api_type}')
    return None


def make_property(data):
    if 'type' not in data.keys():
        return None

    api_name = data['name']
    schema_name = property_to_snake_case(api_name)

    if schema_name in keywords:
        schema_name += '_'

    if data['type'] == 'any':
        return schema_name, None

    schema_type = api_type_to_schema_type(data['type'])

    if schema_type is None:
        return None

    # compressed properties like: (size)(1-12) and d-{type} are handled on a higher level
    if '(' in api_name or '{' in api_name:
        return None

    property_dict = {
        'type': schema_type,
        'allowNull': True,
        'default': None
    }

    if schema_type == 'union':
        union_types = [api_type_to_schema_type(t)
                       for t in data['type']]
        property_dict['oneOf'] = [{'type': t}
                                  for t in union_types
                                  if t]

    return schema_name, property_dict


def make_widget(data):
    name, attributes = data
    widget_name = kebab_to_camel(name)

    if 'props' not in attributes.keys():
        # Widgets without props are directives, internationalization or $vuetify
        return None

    properties = list(filter(identity, map(make_property, attributes['props'])))

    # compressed properties like: (size)(1-12) and d-{type}
    if widget_name == 'Container':
        properties += make_d_type_props() + make_grid_list_props()
    elif widget_name == 'Flex':
        properties += make_grit_props('', 1, 13) + make_grit_props('offset_', 0, 13) + make_grit_props('order_', 1, 13)
    elif widget_name == 'Layout':
        properties += make_d_type_props()

    if widget_name in ['Container', 'Content', 'Flex', 'Layout']:
        properties += make_spacing_props()

    return (widget_name, {
        'inherits': ['VuetifyWidget'],
        'properties': dict(properties)})


def generate_schema(vuetify_api_file_name, base_schema_file_name, schema_output_file_name):
    api_data = json.loads(open(vuetify_api_file_name).read())
    base = json.loads(open(base_schema_file_name).read())

    schema_tuples = filter(identity, map(make_widget, api_data.items()))

    base['widgets'] = {**base['widgets'], **dict(schema_tuples)}

    with open(schema_output_file_name, 'w') as outfile:
        json.dump(base, outfile)
