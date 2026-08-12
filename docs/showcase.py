import ipyvuetify as v

lorum_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

items = [v.ListItem(children=[v.ListItemTitle(children=[f"Click me {i}"])]) for i in range(1, 5)]

menu = v.Menu(
    location="bottom",
    v_slots=[
        {
            "name": "activator",
            "variable": "menuData",
            "children": v.Btn(
                v_on="menuData.props",
                color="primary",
                children=["menu", v.Icon(children=["mdi-menu-down"])],
            ),
        }
    ],
    children=[v.List(children=items)],
)

dialog = v.Dialog(
    width="500",
    v_slots=[
        {
            "name": "activator",
            "variable": "x",
            "children": v.Btn(v_on="x.props", color="success", children=["Open dialog"]),
        }
    ],
    children=[
        v.Card(
            children=[
                v.CardTitle(
                    class_="text-h5 bg-grey-lighten-2",
                    children=["Lorem ipsum"],
                ),
                v.CardText(
                    children=[
                        lorum_ipsum,
                        v.TextField(label="Label", placeholder="Placeholder"),
                    ]
                ),
            ]
        )
    ],
)

dialog.on_event("keydown.stop", lambda *args: None)

v.Container(
    children=[
        v.Row(
            children=[
                v.Btn(class_="ma-2", color="primary", children=["button"]),
                v.Btn(class_="ma-2", color="primary", variant="outlined", children=["button"]),
                v.Btn(class_="ma-2", color="primary", rounded=True, children=["button"]),
                v.Btn(
                    class_="ma-2",
                    color="primary",
                    icon=True,
                    size="large",
                    children=[
                        v.Icon(children=["mdi-pencil"]),
                    ],
                ),
                v.Btn(
                    class_="ma-2",
                    color="primary",
                    icon=True,
                    children=[
                        v.Icon(children=["mdi-pencil"]),
                    ],
                ),
                v.Btn(class_="ma-2", color="primary", variant="text", children=["button"]),
            ]
        ),
        v.Row(
            children=[
                v.Btn(class_="ma-2", color="primary", size="x-small", children=["button"]),
                v.Btn(
                    class_="ma-2",
                    color="primary",
                    size="x-small",
                    variant="outlined",
                    children=["button"],
                ),
                v.Btn(
                    class_="ma-2",
                    color="primary",
                    size="x-small",
                    rounded=True,
                    children=["button"],
                ),
                v.Btn(
                    class_="ma-2",
                    color="primary",
                    size="x-small",
                    icon=True,
                    children=[
                        v.Icon(children=["mdi-pencil"]),
                    ],
                ),
                v.Btn(
                    class_="ma-2",
                    color="primary",
                    size="x-small",
                    icon=True,
                    children=[
                        v.Icon(children=["mdi-pencil"]),
                    ],
                ),
                v.Btn(
                    class_="ma-2",
                    color="primary",
                    size="x-small",
                    variant="text",
                    children=["button"],
                ),
            ]
        ),
        v.Row(
            children=[
                v.Col(
                    cols=4,
                    children=[
                        v.Select(
                            label="Fruits",
                            items=["Apple", "Pear", "Cherry"],
                            v_model="Pear",
                        )
                    ],
                ),
                v.Col(
                    cols=4,
                    children=[
                        v.Select(
                            label="Fruits",
                            items=["Apple", "Pear", "Cherry"],
                            chips=True,
                            multiple=True,
                            v_model=["Pear", "Cherry"],
                        )
                    ],
                ),
                v.Col(
                    cols=4,
                    children=[
                        v.Select(
                            label="Fruits",
                            items=["Apple", "Pear", "Cherry"],
                            variant="outlined",
                        )
                    ],
                ),
            ]
        ),
        v.Row(
            children=[
                v.Col(cols=4, children=[v.Slider()]),
                v.Col(cols=4, children=[v.Slider(thumb_label="always")]),
                v.Col(cols=4, children=[v.RangeSlider(v_model=[20, 80])]),
            ]
        ),
        v.Row(
            children=[
                v.Col(cols=4, children=[v.Switch(label="switch")]),
                v.Col(cols=4, children=[menu]),
                v.Col(cols=4, children=[dialog]),
            ]
        ),
    ]
)
