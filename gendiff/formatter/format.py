from gendiff.formatter.json import json_formatter
from gendiff.formatter.plain import plain_formatter
from gendiff.formatter.stylish import stylish_formatter

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'

DEFAULT_FORMAT = FORMAT_STYLISH


def format_data(data, format_type=DEFAULT_FORMAT):
    formats = {
        FORMAT_STYLISH: stylish_formatter,
        FORMAT_PLAIN: plain_formatter,
        FORMAT_JSON: json_formatter
    }
    format_function = formats.get(format_type)
    if format_function:
        return format_function(data)
    raise Exception('Unsupported format!')
