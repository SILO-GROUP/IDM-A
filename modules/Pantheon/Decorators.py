from typing import Union

from flask_restx import Api, Namespace


class NamespaceWrapper(Namespace):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def expect_header(self, name: str, desc: str):
        return self.doc(params={name: {"in": "header", "description": desc}})
