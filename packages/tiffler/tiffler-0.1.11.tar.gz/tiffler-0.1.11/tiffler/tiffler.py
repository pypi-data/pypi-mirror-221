import re
from collections import OrderedDict
from functools import lru_cache
from typing import *

SUPPORTED_TYPES = {
    "float": "[-+]?\d*\.\d+|\d+",
    "int": "[-+]?\d+",
    "bool": "true|True|false|False|0|1",
    "str": ".+",
}

SUPPORTED_CONVERTERS = {
    "int": lambda val: int(float(val)),
    "bool": lambda val: {
        "true": True,
        "false": False,
        "0": False,
        "1": True,
    }.get(val.lower(), bool(val)),
}

__all__ = ["Tiffler", "compile", "scan", "search"]


class Tiffler:
    def __init__(
        self,
        template: str,
        case_sensitive: bool = True,
        types: Dict[str, str] = None,
        converters: Dict[str, Callable] = None,
        **kwargs,
    ):
        self.case_sensitive = case_sensitive

        if types is None:
            types = SUPPORTED_TYPES
        self.types = types

        if converters is None:
            converters = SUPPORTED_CONVERTERS
        self.converters = converters

        self.build(template)

    def build(self, template: str):
        self.vars = OrderedDict()
        expr = (
            r"((?<=[^\\]\{)(\?|([a-zA-Z_]\w*.*?))(?=\}))"
            "|(?<=^\{)(\?|([a-zA-Z_]\w*.*?))(?=\})"
        )

        self.template = ""
        curr_idx = 0
        for match in re.finditer(expr, template):
            var_name, var_type, var_expr, *_ = match.group().split(":") + [None, None]
            if var_name.isidentifier():
                assert var_name not in self.vars, f"Duplicate var name {var_name} found"

                if var_type is None:
                    var_type = "str"

                if var_expr is None:
                    var_expr = self.types.get(var_type, ".+")

                if var_type in self.converters:
                    var_type = self.converters[var_type]
                else:
                    assert var_type in self.types, f"Type {var_type} is not supported"
                    var_type = eval(var_type)

                self.template += (
                    template[curr_idx : match.start() - 1] + rf"({var_expr})"
                )
                curr_idx = match.end() + 1
                self.vars[var_name] = var_type

        self.template += template[curr_idx:]
        if self.case_sensitive:
            self.expr = re.compile(self.template)
        else:
            self.expr = re.compile(self.template, re.IGNORECASE)

    def scan(self, text: str, **kwargs) -> Dict[str, Any]:
        match = self.expr.match(text)
        result = {}

        if match:
            for val, (key, dtype) in zip(match.groups(), self.vars.items()):
                result[key] = dtype(val)

        return result

    def search(self, text: str, **kwargs) -> Iterator[Dict[str, Any]]:
        for match in self.expr.finditer(text):
            result = {}
            for val, (key, dtype) in zip(match.groups(), self.vars.items()):
                result[key] = dtype(val)

            yield result


@lru_cache(typed=True)
def compile(template: str, case_sensitive: bool = False, **kwargs) -> Tiffler:
    return Tiffler(template, case_sensitive=case_sensitive, **kwargs)


def scan(
    template: str, text: str, case_sensitive: bool = False, **kwargs
) -> Dict[str, Any]:
    tiffler = compile(template, case_sensitive=case_sensitive)
    return tiffler.scan(text, **kwargs)


def search(
    template: str, text: str, case_sensitive: bool = False, **kwargs
) -> Iterator[Dict[str, Any]]:
    tiffler = compile(template, case_sensitive=case_sensitive)
    return tiffler.search(text, **kwargs)
