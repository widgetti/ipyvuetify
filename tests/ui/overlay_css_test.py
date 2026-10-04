import ipywidgets as widgets
import playwright.sync_api
import pytest
import solara.server.settings
from IPython.display import display


@pytest.fixture
def app_css(tmp_path, monkeypatch):
    # Solara puts assets/custom.css in the page head, as it does for an app's own css
    (tmp_path / "custom.css").write_text(".v-btn { text-transform: none; }\n")
    monkeypatch.setattr(solara.server.settings.assets, "extra_locations", [str(tmp_path)])


def text_transform(locator: playwright.sync_api.Locator) -> str:
    return locator.evaluate("el => getComputedStyle(el).textTransform")


# must request app_css before solara_test, which loads the page
def test_app_css_wins_in_lumino_and_overlay(
    app_css, solara_test, page_session: playwright.sync_api.Page
):
    # nodeps.js (Solara) uses the host's Vuetify css. ipyvuetify 3.0.0 added a copy scoped to
    # .vuetify-styles (on Lumino-hosted views and the overlay container), and that copy won
    # over the app's css: these buttons were uppercase.
    import ipyvuetify as v

    menu = v.Menu(
        v_slots=[
            {
                "name": "activator",
                "variable": "menuData",
                "children": v.Btn(
                    v_on="menuData.props", children=["open menu"], class_="menu-activator"
                ),
            }
        ],
        children=[v.Card(children=[v.Btn(children=["in overlay"], class_="overlay-btn")])],
    )
    display(widgets.VBox(children=[v.Btn(children=["in lumino"], class_="lumino-btn"), menu]))

    lumino_button = page_session.locator(".lumino-btn")
    lumino_button.wait_for()
    assert text_transform(lumino_button) == "none"

    page_session.locator(".menu-activator").click()
    overlay_button = page_session.locator(".v-overlay-container .overlay-btn")
    overlay_button.wait_for()
    assert text_transform(overlay_button) == "none"
