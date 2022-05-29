from typing import Union

from flask_restx import Api, Namespace


def expect_header(api: Union[Api, Namespace], name: str, desc: str):
    return api.doc(params={name: {"in": "header", "description": desc}})
