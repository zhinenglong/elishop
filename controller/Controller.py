import json
from . CView import CView
from . import render_template, render_template_string, make_response, stream_template, stream_template_string


class Controller(CView):

    @classmethod
    def render(cls, file=None, **data):
        if file is None:
            return "file is None"
        return render_template(file, **data)

    @classmethod
    def render_text(cls, strs: str, **data):
        return render_template_string(strs, **data)

    @classmethod
    def render_stream(cls, tpl, **data):
        return stream_template(tpl, **data)

    @classmethod
    def render_stream_str(cls, strs: str, **data):
        return stream_template_string(strs, **data)

    @classmethod
    def render_json(cls, data):
        return json.JSONEncoder().encode(data)
