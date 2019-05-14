from traitlets import Unicode
from .generated.VuetifyWidget import VuetifyWidget


class Html(VuetifyWidget):

    _model_name = Unicode('HtmlModel').tag(sync=True)

    tag = Unicode().tag(sync=True)


__all__ = ['Html']
