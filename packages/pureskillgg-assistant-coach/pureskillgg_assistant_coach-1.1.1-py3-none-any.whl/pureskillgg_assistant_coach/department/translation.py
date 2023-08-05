from typing import Union
from pybars import Compiler


class Translation:
    def __init__(
        self, translations: Union[dict, None], data=None, /, data_is_str=False
    ):
        self._translations = translations
        self._data = data if data_is_str else convert_data_to_str(data)
        self._compiler = Compiler()
        self._required_key = "en"
        self._passthrough_types = (str, bool)

    def get(self):
        if self._translations is None:
            return None
        if self._required_key in self._translations:
            return {k: self._render(v) for k, v in self._translations.items()}

        output = {}
        for key, value in self._translations.items():
            output[key] = self._output_translated_values(value)
        return output

    def _output_translated_values(self, value):
        if isinstance(value, self._passthrough_types):
            return value
        if isinstance(value, dict):
            return Translation(value, self._data, data_is_str=True).get()
        if isinstance(value, list):
            return self._handle_list(value)
        raise RuntimeError(f"Unhandled type {type(value)}")

    def _handle_list(self, my_list):
        return [self._output_translated_values(item) for item in my_list]

    def _render(self, source):
        template = self._compiler.compile(source)
        return template(self._data, helpers=helpers)


# pylint: disable=unused-argument
def _list(self, options, items, default=""):
    if items is None:
        return f"{default}"

    if len(items) == 0:
        return f"{default}"

    if len(items) == 1:
        return f"{items[0]}"

    if len(items) == 2:
        return f"{items[0]} & {items[1]}"

    if len(items) > 2:
        last = items.pop()
        return f'{", ".join(items)} & {last}'

    return f"{default}"


helpers = {"list": _list}


def to_string(val):
    if isinstance(val, list):
        return [str(i) for i in val]

    return str(val)


def convert_data_to_str(data):
    if data is None:
        return None

    return {k: to_string(v) for k, v in data.items()}
