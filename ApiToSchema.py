import json
import pprint
from collections import ChainMap
import re

pp = pprint.PrettyPrinter(indent=4)

api_data = json.loads(open('vuetify_api_1.5.6.json').read())


def kebab_to_camel(name):
    return "".join(
        map(
            lambda x: x.capitalize(),
            name.split("-")[1:]))


# def kebab_to_camel_prop(name):
#     parts = name.split("-")
#
#     if len(parts) == 1:
#         return parts[0]
#
#     return "".join(
#         [parts[0]] + list(map(
#             lambda x: x.capitalize(),
#             parts[1:])))

# def component_to_snake_case(name):
#     return "_".join(name.split("-")[1:])

def property_to_snake_case(name):
    return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()


sizes = ['xs', 'sm', 'md', 'lg', 'xl']
display_values = ["inline",
                  "block",
                  "contents",
                  "flex",
                  "grid",
                  "inline_block",
                  "inline_flex",
                  "inline_grid",
                  "inline_table",
                  "list_item",
                  "run_in",
                  "table",
                  "table_caption",
                  "table_column_group",
                  "table_header_group",
                  "table_footer_group",
                  "table_row_group",
                  "table_cell",
                  "table_column",
                  "table_row",
                  "none",
                  "initial",
                  "inherit"]


def make_boolean_prop(): return {"type": "boolean", "allowNull": True, "default": None}


def make_d_type_props():
    return [(f"d_{d}", make_boolean_prop()) for d in display_values]


def make_grid_list_props():
    return [(f"grid_list_{s}", make_boolean_prop()) for s in sizes]


def make_grit_props(prefix, start, end):
    return [(f"{prefix}{s}{n}", make_boolean_prop()) for s in sizes for n in range(start, end)]


def make_widget(data):
    # if data[0] not in [""]:
    #     return None

    widgetName = kebab_to_camel(data[0])

    def api_default_to_schema(data):
        if "default" not in data.keys():
            print(f'{widgetName}.{data["name"]} has no default')
            return None

        if "type" not in data.keys():
            print(f'{widgetName}.{data["name"]} has no type')
            return None

        type = data["type"]
        default = data["default"]
        if default == "undefined":
            return None
        if type == "boolean":
            return None if default == "false" else True
        if type == "string":
            return default[1:-1]

        return default

    def make_prop(data):
        # TODO: handle keywords properly
        if data["name"] in ["for"]:
            return None

        # compressed properties like: (size)(1-12) and d-{type} are handled on a higher level
        if "(" in data["name"] or "{" in data["name"]:
            print("compressed: " + widgetName + "." + data["name"])
            return None

        if "type" not in data.keys():
            print(f'{widgetName}.{data["name"]} has no type (2)')
            return None

        # name = kebab_to_camel_prop(data["name"])
        name = property_to_snake_case(data["name"])

        def api_type_to_schema(type_):
            # Vuetify api schema contains casing errors
            if type(type_) is str:
                type_ = type_.casefold()

            if type_ in ["boolean", "string", "object"]:
                return type_
            elif type_ == "number":
                return 'float'
            elif type(type_) is list:
                return 'union'
            else:
                print(f'{widgetName}.{name} {type_} {data["source"]}')
                return None

        if data["type"] == "any":
            return (name, None)

        if data["type"] == "array":
            return (name, {
                "type": "array",
                "allowNull": True,
                "default": None
            })

        type_ = api_type_to_schema(data["type"])
        if type_ == None:
            return None

        prop_dict = {
            "type": type_,
            "allowNull": True,
            "default": None
        }

        if type_ == "union":
            prop_dict["oneOf"] = list(map(lambda x: {"type": x},
                                          filter(None.__ne__,
                                                 map(api_type_to_schema, data["type"]))))

        # default = api_default_to_schema(data)
        # if default == None:
        #     prop_dict["allowNull"] = True
        # prop_dict["default"] = default

        return (name, prop_dict)

    if "props" not in data[1].keys():
        print(f'{widgetName} has no properties')
        return None

    all_props = map(make_prop, data[1]["props"])

    # skipped_props = list(filter(lambda p: "skipped" in p.keys(), all_props))
    # pp.pprint(skipped_props)
    # print("skipped:" + )

    supported_props = list(filter(None.__ne__, all_props))

    # compressed: Container.d-{type}
    # compressed: Container.grid-list-{xs through xl}
    # compressed: Flex.(size)(1-12)
    # compressed: Flex.offset-(size)(0-12)
    # compressed: Flex.order-(size)(1-12)
    # compressed: Layout.d-{type}

    if widgetName == "Container":
        supported_props += make_d_type_props() + make_grid_list_props()
    elif widgetName == "Flex":
        supported_props += make_grit_props("", 1, 13) + make_grit_props("offset_", 0, 13) + make_grit_props("order_", 1,
                                                                                                            13)
    elif widgetName == "Layout":
        supported_props += make_d_type_props()

    # naar template: props = [("_model_name", widgetName + "Model")] + supported_props
    props = supported_props
    # if widgetName == "Icon":
    #     props = props + [("value", {"type": "string"})]

    return {
        widgetName: {
            "inherits": ["VuetifyWidget"],
            "properties": dict(props)
        }
    }


def make_schema(data):
    return list(filter(None.__ne__, map(make_widget, data)))


test_data = list(api_data.items())
# [:20]


# pp.pprint(make_schema(test_data))

base = json.loads(open('js/gen-source/base.json').read())
base["widgets"] = {**base["widgets"], **dict(ChainMap(*make_schema(test_data)))}

with open('js/gen-source/widget_gen_schema.json', 'w') as outfile:
    json.dump(base, outfile)
