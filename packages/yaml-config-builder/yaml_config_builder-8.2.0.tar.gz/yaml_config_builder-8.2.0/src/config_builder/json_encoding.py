import json
from collections import OrderedDict
from typing import Any


class TupleEncoder(json.JSONEncoder):
    """
    Customize the json encoding in order to have a tuple save conversion
    """

    def encode(self, obj: Any) -> str:
        """Return a JSON string representation of a Python data structure.

        >>> from json.encoder import JSONEncoder
        >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
        '{"foo": ["bar", "baz"]}'

        REMARK: The encoding will only work for top level tupels and not for nested tuples

        Args:
            obj: The object to encode

        Returns:
            The encoded object as json string
        """

        def tuple_save_encoding(value: Any) -> Any:
            if isinstance(value, tuple):
                return {"__is_tuple__": True, "content": value}
            if isinstance(value, list):
                return [tuple_save_encoding(e) for e in value]
            if isinstance(value, dict) or isinstance(value, OrderedDict):
                return {k: tuple_save_encoding(v) for k, v in value.items()}
            else:
                return value

        return str(json.JSONEncoder.encode(self, tuple_save_encoding(value=obj)))

    @staticmethod
    def tuple_save_loading_hook(obj: Any) -> Any:
        """
        Method that is designed to be used as object_hook in json.loads
        when decoding a json string, which has been encoded via TupleEncoder.encode

        Args:
            obj: The object to decode

        REMARK: The decoding will only work for top level tuples and not for nested tuples

        Returns:
            The correct representation of the object
        """
        if "content" in obj and "__is_tuple__" in obj:
            return tuple(obj["content"])
        return obj
