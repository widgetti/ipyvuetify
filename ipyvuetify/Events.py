from ipywidgets.widgets.widget import CallbackDispatcher

import logging
logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("init")

class Events:
    def __init__(self):
        self._event_handlers_map = {}
        self.on_msg(self._handle_event)

    def on_event(self, event, callback, remove=False):
        self._event_handlers_map[event]=CallbackDispatcher()

        logging.info(f"{'un' if remove else ''}register {event}")
        self._event_handlers_map[event].register_callback(callback, remove=remove)

        if remove and not self._event_handlers_map[event].callbacks:
            del self._event_handlers_map[event]

        difference = set(self._event_handlers_map.keys()) ^ set(self._events)
        logging.info(f"difference: {difference} current: {self._event_handlers_map.keys()}")
        if len(difference) != 0:
            self._events = list(self._event_handlers_map.keys())

        logging.info(self._events)

    def fire_event(self, event, data):
        logging.info(f"fir: {self} {event} {data}")
        self._event_handlers_map[event](self, event, data)

    def _handle_event(self, _, content, buffers):
        event = content.get("event", "")
        data = content.get("data", {})
        logging.info(f"event: {event}, data: {data}")
        self.fire_event(event, data)

    def log(self, msg):
        logging.info(msg)
