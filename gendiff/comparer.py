from gendiff.parser.parser import parse_file, get_format
from gendiff.parser.loader import load_file
from gendiff.formatter.format import format_data, DEFAULT_FORMAT
from gendiff.constrants import CHILDREN, UNCHANGED, UPDATED, REMOVED, ADDED


def compare(data1, data2):
    '''
    function build dictionary representation diff files
    '''
    result = {}
    union_keys = set(data1.keys() | data2.keys())
    for key in union_keys:
        if isinstance(data1.get(key), dict) & isinstance(data2.get(key), dict):
            result[key] = {
                'type': CHILDREN,
                'value': compare(data1[key], data2[key])
            }
        elif data1.get(key) == data2.get(key):
            result[key] = {
                'type': UNCHANGED,
                'value': data1.get(key)
            }
        elif key in data1 and key in data2:
            result[key] = {
                'type': UPDATED,
                'old_value': data1[key],
                'new_value': data2[key]
            }
        elif key in data1:
            result[key] = {
                'type': REMOVED,
                'value': data1[key]
            }
        else:
            result[key] = {
                'type': ADDED,
                'value': data2[key]
            }
    return result


def generate_diff(filepath1, filepath2, format=DEFAULT_FORMAT):
    '''
    run comparer and show result in format type: "stylish", "plain", "json"

    default format "stylish"

    raises: unknown format
    '''
    content1 = load_file(filepath1)
    extension1 = get_format(filepath1)
    content2 = load_file(filepath2)
    extension2 = get_format(filepath2)
    data1 = parse_file(content1, extension1)
    data2 = parse_file(content2, extension2)
    result = compare(data1, data2)
    return format_data(result, format)
