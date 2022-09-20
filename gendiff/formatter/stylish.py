# stylish formattef
import json
import re

from gendiff.formatter import TYPES


def get_type(type):
    return {
        'added': '+',
        'no changes': ' ',
        'removed': '-'
    }[type]


def make_tree(data):
    '''
    function rebuild dictionary representation
    '''
    result = {}
    if not isinstance(data, dict):
        return data
    for key, value in data.items():
        if not isinstance(value, dict):
            result[f'  {key}'] = value
        elif not data[key].get('type') in TYPES:
            result[f'  {key}'] = make_tree(value)
        else:
            type = data[key].get('type')
            if type == TYPES[2]:  # updated
                result[f'- {key}'] = make_tree(value['old_value'])
                result[f'+ {key}'] = make_tree(value['new_value'])
            else:
                result[f'{get_type(type)} {key}'] = make_tree(value['value'])
    return result


def stringify(data):
    '''
    function cuts \' and fixes indents
    '''
    result = json.dumps(data, indent=4)
    result = result.replace('"', '')
    result = result.replace(',', '')
    result = result.replace('  }', '    }')
    result = re.sub(r"\n\s\s", '\n', result)
    return result


def stylish_formatter(data):
    result = make_tree(data)
    return stringify(result)
