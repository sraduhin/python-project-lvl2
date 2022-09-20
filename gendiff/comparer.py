from gendiff.parser.parser import parse_file, load_file
from gendiff.formatter.format import format_data

from gendiff.formatter import TYPES


def compare(data1, data2):
    '''
    function build dictionary representation diff files
    '''
    result = {}
    union_keys = sorted(set(data1.keys() | data2.keys()))
    for key in union_keys:
        if isinstance(data1.get(key), dict) & isinstance(data2.get(key), dict):
            result[key] = compare(data1[key], data2[key])
        elif data1.get(key) == data2.get(key):
            result[key] = {
                'type': 'no changes',
                'value': data1.get(key)
            }
        elif key in data1 and key in data2:
            result[key] = {
                'type': 'updated',
                'old_value': data1[key],
                'new_value': data2[key]
            }
        elif key in data1:
            result[key] = {
                'type': 'removed',
                'value': data1[key]
            }
        else:
            result[key] = {
                'type': 'added',
                'value': data2[key]
            }
    print('check result', result)
    return result


def generate_diff(filepath1, filepath2, format='stylish'):
    '''
    run comparer and show result in format type

    raises: unknown format
    '''
    content1, extension1 = load_file(filepath1)
    content2, extension2 = load_file(filepath2)
    data1 = parse_file(content1, extension1)
    data2 = parse_file(content2, extension2)
    result = compare(data1, data2)
    return format_data(result, format)
