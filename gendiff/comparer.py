from gendiff.parser.parser import parser
from gendiff.formatter.stylish import main as show_diff_stylish
from gendiff.formatter.plain import main as show_diff_plain
from gendiff.formatter.json import main as show_diff_json


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
            result[key] = data1.get(key)
        elif key in data1 and key in data2:
            result[key] = {
                'action': 'update',
                'old_value': data1[key],
                'new_value': data2[key]
            }
        elif key in data1:
            result[key] = {'action': '-', 'value': data1[key]}
        else:
            result[key] = {'action': '+', 'value': data2[key]}
    return result


def generate_diff(filepath1, filepath2, format='stylish'):
    '''
    run comparer and show result in format type

    raises: unknown format
    '''
    data1 = parser(filepath1)
    data2 = parser(filepath2)
    result = compare(data1, data2)
    if format == 'stylish' or format is None:
        return show_diff_stylish(result)
    elif format == 'plain':
        return show_diff_plain(result)
    elif format == 'json':
        return show_diff_json(result)
    raise ValueError(f"Unknown format: {format}")
