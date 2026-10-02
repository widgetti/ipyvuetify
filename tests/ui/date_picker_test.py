import playwright.sync_api
from IPython.display import display


def test_date_picker(ipywidgets_runner, page_session: playwright.sync_api.Page):
    # DatePicker renders the VDatePicker of the app it is mounted in (the host's
    # Vuetify in nodeps.js), and maps v_model between "YYYY-MM-DD" and Date
    def kernel_code():
        import ipyvuetify as v

        picker = v.DatePicker(v_model="2024-01-15", class_="date-picker-test")
        label = v.Html(tag="div", children=["picked 2024-01-15"], class_="date-picker-label")

        def on_change(*ignore):
            label.children = [f"picked {picker.v_model}"]

        picker.observe(on_change, "v_model")
        display(v.Container(children=[picker, label]))

    ipywidgets_runner(kernel_code)
    page_session.locator(".date-picker-test").wait_for()
    page_session.locator(".date-picker-test button >> text=/^20$/").click()
    page_session.locator("text=picked 2024-01-20").wait_for()
