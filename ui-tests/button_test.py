import playwright.sync_api
from IPython.display import display


def test_button(ipywidget_runner, page_session: playwright.sync_api.Page):
    def kernel_code():
        import ipyvuetify as v

        button = v.Btn(children=["Click Me!"])

        def change_description(*ignore):
            button.children = ["Tested event"]

        button.on_event("click", change_description)
        display(button)

    ipywidget_runner(kernel_code)
    button_sel = page_session.locator("button >> text=Click Me!")
    button_sel.wait_for()
    button_sel.click()
    page_session.locator("button >> text=Tested event").wait_for()
