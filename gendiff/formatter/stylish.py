# stylish formatter
from gendiff.constrants import ADDED, REMOVED, UPDATED, CHILDREN
import json

REPLACER = ' '
SPACE_COUNT = 4


def stylish_formatter(data):
    '''
    function rebuild dictionary representation
    '''
    def inner(data, depth, replacer=REPLACER, space_count=SPACE_COUNT):
        result = '{\n'
        indent = (replacer * space_count) * depth
        depth += 1
        for key, value in data.items():
            type = value.get('type')
            if type == CHILDREN:
                extra_indent = indent + replacer * space_count
                result += f"{extra_indent}{key}: {inner(value['value'], depth)}"
                result += '\n'
            elif type == UPDATED:
                old_value = normalize(value['old_value'], depth)
                new_value = normalize(value['new_value'], depth)
                result += f"{indent}  - {key}: {old_value}\n"
                result += f"{indent}  + {key}: {new_value}\n"
            elif type == ADDED:
                changed_value = normalize(value['value'], depth)
                result += f"{indent}  + {key}: {changed_value}\n"
            elif type == REMOVED:
                changed_value = normalize(value['value'], depth)
                result += f"{indent}  - {key}: {changed_value}\n"
            else:
                changed_value = normalize(value['value'], depth)
                extra_indent = indent + replacer * space_count
                result += f"{extra_indent}{key}: {changed_value}\n"
        return result + indent + '}'
    return inner(data, 0)


def normalize(value, depth):
    """Normalize simple data and rebuild inner tree"""

    def inner(value, depth, replacer, space_count):
        if not isinstance(value, dict):
            return json.dumps(value).strip('"')
        result = ''
        indent = ' ' * 4 * depth
        for inner_key, inner_value in value.items():
            inner_value = normalize(inner_value, depth + 1)
            extra_indent = indent + replacer * space_count
            result += f'{extra_indent}{inner_key}: {inner_value}\n'
        return '{\n' + result + indent + '}'
    return inner(value, depth, REPLACER, SPACE_COUNT)
