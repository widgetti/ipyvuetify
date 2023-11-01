import json
import re
import textwrap
from pathlib import Path


def dedent_with_offset(text, offset):
    # Remove common leading whitespace using dedent
    dedented_text = textwrap.dedent(text)

    # Add the desired offset (indentation) back to the string
    offset_spaces = " " * offset
    indented_text = "\n".join(
        offset_spaces + line for line in dedented_text.splitlines()
    )

    return indented_text


def property_to_snake_case(name):
    return re.sub("(?!^)([A-Z]+)", r"_\1", name).lower()


def get_component_files():
    component_files = []
    for file_path in Path("vuetify/packages/api-generator/dist/api").glob("V*.json"):
        component_files.append((file_path.stem, file_path))

    return sorted(component_files)


def get_sub(prop: dict):
    if prop["type"] == "string":
        return "Unicode()"
    if prop["type"] == "number":
        return "Float()"
    if prop["type"] == "boolean":
        return "Bool()"
    if prop["type"] == "array":
        return "TList(Any())"
    if prop["type"] == "object":
        return "Dict()"
    if prop["type"] in ["anyOf", "function", "record", "ref"]:
        return None
    raise Exception(f"Unknown sub type {prop['type']}")


def generate_traitlet(prop: dict):
    if (
        "string & {}" in prop["text"]
        or prop["type"] == "string"
        or prop["type"] == "ref"
        or prop["type"] == "function"
    ):
        return "Unicode(default_value=None, allow_none=True).tag(sync=True)\n"
    if prop["type"] == "anyOf":
        sub = [get_sub(e) for e in prop["items"] if get_sub(e) is not None]
        if len(set(sub)) == 1:
            if sub[0] == "TList(Any())":
                return (
                    "TList(Any(), default_value=None, allow_none=True).tag(sync=True)\n"
                )
            return sub[0].replace(
                "()", "(default_value=None, allow_none=True).tag(sync=True)\n"
            )
        return f"Union([{', '.join(sub)}], default_value=None, allow_none=True).tag(sync=True)\n"
    if prop["type"] == "boolean":
        return "Bool(default_value=None, allow_none=True).tag(sync=True)\n"
    if prop["type"] == "array":
        return "TList(Any(), default_value=None, allow_none=True).tag(sync=True)\n"
    if prop["type"] == "object":
        return "Dict(default_value=None, allow_none=True).tag(sync=True)\n"
    if prop["type"] == "number":
        return "Float(default_value=None, allow_none=True).tag(sync=True)\n"
    if prop["type"] == "any":
        return "Any().tag(sync=True)\n"
    raise Exception(f"Unknown type {prop['type']}")


def generate_python_class(name: str, path: Path):
    code = textwrap.dedent(
        f"""\
        class {name[1:]}(VuetifyWidget):
            _model_name = Unicode("{name[1:]}Model").tag(sync=True)
    """
    )
    with open(path) as f:
        data = json.load(f)
        props = data["props"]
        for prop_name, prop in sorted(props.items()):
            if prop["type"] in ["record", "unknown"]:
                continue

            code += dedent_with_offset(
                f"""
                {property_to_snake_case(prop_name)} = {generate_traitlet(prop)}
            """,
                4,
            )

    return code + "\n\n"


def generate_python():
    code = textwrap.dedent(
        """\
        from traitlets import Unicode, Union, Float, List as TList, Dict, Bool, Any

        from .vuetify_widget import VuetifyWidget


    """
    )
    components = get_component_files()
    for name, path in components:
        code += generate_python_class(name, path)

    code += textwrap.dedent(
        f"""\
        __all__ = ["{'", "'.join([name[1:] for name, _ in components])}"]
    """
    )

    return code


def generate_js_class(name, path):
    class_name = name[1:]
    code = textwrap.dedent(
        f"""\
        export class {class_name}Model extends VuetifyWidgetModel {{
            defaults() {{
                return {{
                    ...super.defaults(),
                    ...{{
                        _model_name: "{class_name}Model",
    """
    )

    with open(path) as f:
        data = json.load(f)
        props = data["props"]
        for prop_name, prop in props.items():
            if prop["type"] in ["record", "unknown"]:
                continue

            code += dedent_with_offset(
                f"""
                {property_to_snake_case(prop_name)}: undefined,
            """,
                16,
            )

        code += f"""
            }},
        }};
    }}

    getVueTag() {{ // eslint-disable-line class-methods-use-this
        return "{data["fileName"]}";
    }}
}}

{class_name}Model.serializers = {{
    ...VuetifyWidgetModel.serializers,
}};

"""
    return code


def generate_js():
    code = textwrap.dedent(
        """\
        import { VuetifyWidgetModel } from "./VuetifyWidget";

    """
    )

    components = get_component_files()
    for name, path in components:
        code += generate_js_class(name, path)

    return code


with open("../ipyvuetify/vuetify_widgets.py", "w") as f:
    f.write(generate_python())

with open("../js/src/Widgets.js", "w") as f:
    f.write(generate_js())
