import ipyvuetify as v

lorum_ipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''

items = [v.ListItem(children=[
    v.ListItemTitle(children=[
        f'Click me {i}'])])
    for i in range(1, 5)]

menu = v.Menu(offset_y=True,
              v_slots=[{
                  'name': 'activator',
                  'variable': 'menuData',
                  'children': v.Btn(v_on='menuData.on', color='primary', children=[
                      'menu',
                      v.Icon(right=True, children=[
                          'mdi-menu-down'
                      ])
                  ]),
              }],
              children=[
                  v.List(children=items)
              ]
              )

dialog = v.Dialog(width='500',
                  v_slots=[{
                      'name': 'activator',
                      'variable': 'x',
                      'children':  v.Btn(v_on='x.on', color='success', dark=True, children=[
                          'Open dialog'
                      ]),
                  }],
                  children=[
                      v.Card(children=[
                          v.CardTitle(class_='headline gray lighten-2', primary_title=True, children=[
                              "Lorem ipsum"
                          ]),
                          v.CardText(children=[
                              lorum_ipsum,
                              v.TextField(label='Label', placeholder='Placeholder')
                          ]),
                      ])
                  ])

dialog.on_event('keydown.stop', lambda *args: None)

v.Container(children=[
    v.Row(children=[
        v.Btn(class_='ma-2', color='primary', children=['button']),
        v.Btn(class_='ma-2', color='primary', outlined=True, children=['button']),
        v.Btn(class_='ma-2', color='primary', rounded=True, children=['button']),
        v.Btn(class_='ma-2', color='primary', fab=True, children=[
            v.Icon(children=['mdi-pencil']),
        ]),
        v.Btn(class_='ma-2', color='primary', icon=True, children=[
            v.Icon(children=['mdi-pencil']),
        ]),
        v.Btn(class_='ma-2', color='primary', text=True, children=['button']),
    ]),
    v.Row(children=[
        v.Btn(class_='ma-2', color='primary', x_small=True, children=['button']),
        v.Btn(class_='ma-2', color='primary', x_small=True, outlined=True, children=['button']),
        v.Btn(class_='ma-2', color='primary', x_small=True, rounded=True, children=['button']),
        v.Btn(class_='ma-2', color='primary', x_small=True, fab=True, children=[
            v.Icon(children=['mdi-pencil']),
        ]),
        v.Btn(class_='ma-2', color='primary', x_small=True, icon=True, children=[
            v.Icon(children=['mdi-pencil']),
        ]),
        v.Btn(class_='ma-2', color='primary', x_small=True, text=True, children=['button']),
    ]),
    v.Row(children=[
        v.Col(cols=4, children=[
            v.Select(label='Fruits', items=['Apple', 'Pear', 'Cherry'], v_model='Pear')
        ]),
        v.Col(cols=4, children=[
            v.Select(label='Fruits', items=['Apple', 'Pear', 'Cherry'], chips=True, multiple=True, v_model=['Pear', 'Cherry'])
        ]),
        v.Col(cols=4, children=[
            v.Select(label='Fruits', items=['Apple', 'Pear', 'Cherry'], outlined=True)
        ]),
    ]),
    v.Row(children=[
        v.Col(cols=4, children=[v.Slider()]),
        v.Col(cols=4, children=[v.Slider(thumb_label='always')]),
        v.Col(cols=4, children=[v.RangeSlider(value=[20,80])]),
    ]),
    v.Row(children=[
        v.Col(cols=4, children=[v.Switch(label='switch', margin_top='0')]),
        v.Col(cols=4, children=[menu]),
        v.Col(cols=4, children=[dialog]),
    ]),
])