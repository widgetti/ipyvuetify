from ipywidgets.widgets.widget import CallbackDispatcher


class Events(object):
    def __init__(self, **kwargs):
        self._event_handlers_map = {}
        self.on_msg(self._handle_event)

    def on_event(self, event, callback, remove=False):
        self._event_handlers_map[event] = CallbackDispatcher()

        self._event_handlers_map[event].register_callback(callback, remove=remove)

        if remove and not self._event_handlers_map[event].callbacks:
            del self._event_handlers_map[event]

        difference = set(self._event_handlers_map.keys()) ^ set(self._events)
        if len(difference) != 0:
            self._events = list(self._event_handlers_map.keys())

    def fire_event(self, event, data):
        self._event_handlers_map[event](self, event, data)

    def _handle_event(self, _, content, buffers):
        event = content.get("event", "")
        data = content.get("data", {})
        self.fire_event(event, data)
