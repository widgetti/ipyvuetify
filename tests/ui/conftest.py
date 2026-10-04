import re

import pytest

# On the Solara runner, nodeps.js uses the Vuetify of the host page. These console messages
# mean that the host's Vuetify is older than the one ipyvuetify is built for, or that a
# component did not resolve.
CONSOLE_ERRORS = re.compile(r"built for Vuetify|Failed to resolve component")


def _uses_solara_runner(request) -> bool:
    callspec = getattr(request.node, "callspec", None)
    if callspec is not None and callspec.params.get("ipywidgets_runner") == "solara":
        return True
    return "solara_test" in request.fixturenames


@pytest.fixture(autouse=True)
def fail_on_console_errors(request):
    if not _uses_solara_runner(request):
        yield
        return
    page = request.getfixturevalue("page_session")
    errors = []

    def on_console(message):
        if CONSOLE_ERRORS.search(message.text):
            errors.append(f"console.{message.type}: {message.text}")

    def on_page_error(error):
        errors.append(f"pageerror: {error}")

    page.on("console", on_console)
    page.on("pageerror", on_page_error)
    try:
        yield
    finally:
        page.remove_listener("console", on_console)
        page.remove_listener("pageerror", on_page_error)
    assert not errors, "browser errors during the test:\n" + "\n".join(errors)
