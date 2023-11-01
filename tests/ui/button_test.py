import playwright.sync_api
from IPython.display import display


def test_button(ipywidgets_runner, page_session: playwright.sync_api.Page, assert_solara_snapshot):
    def kernel_code():
        import ipyvuetify as v

        button = v.Btn(
            children=[v.Icon(children=["mdi-check"]), "Click Me!"],
            class_="snapshot-button",
        )
        container = v.Container(
            children=[button],
            class_="ma-2 snapshot-container",
        )

        def change_description(*ignore):
            button.children = ["Tested event"]

        button.on_event("click", change_description)
        display(container)

    ipywidgets_runner(kernel_code)
    button_sel = page_session.locator("button >> text=Click Me!")
    button_sel.wait_for()
    assert_solara_snapshot(page_session.locator(".snapshot-button").screenshot())
    button_sel.click()
    page_session.locator("button >> text=Tested event").wait_for()
