from gendiff.formatter.json import json_formatter
from gendiff.formatter.plain import plain_formatter
from gendiff.formatter.stylish import stylish_formatter

FORMAT = {
    'stylish': stylish_formatter,
    'plain': plain_formatter,
    'json': json_formatter
}


def format_data(data, format_type):
    format_function = FORMAT.get(format_type)
    if format_function:
        return format_function(data)
    raise Exception('Unsupported format!')
