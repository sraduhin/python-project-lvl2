from gendiff.formatter.json import json_formatter
from gendiff.formatter.plain import plain_formatter
from gendiff.formatter.stylish import stylish_formatter

FORMAT = {
    'stylish': stylish_formatter,
    'plain': plain_formatter,
    'json': json_formatter
}


def format_data(data, format_type):
    try:
        format_function = FORMAT[format_type]
        return format_function(data)
    except TypeError:
        f"Unknown format: {format_type}"
