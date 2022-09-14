import json
import re


def has_children(data):
    return isinstance(data, dict)


def make_tree(data):
    result = {}
    if not has_children(data):
        return data
    for key, value in data.items():
        if not has_children(value):
            result[f'  {key}'] = value
        elif not data[key].get('action'):
            result[f'  {key}'] = make_tree(value)
        else:
            action = data[key].get('action')
            if action == 'update':
                result[f'- {key}'] = make_tree(value['old_value'])
                result[f'+ {key}'] = make_tree(value['new_value'])
            else:
                result[f'{action} {key}'] = make_tree(value['value'])
    return result


def stringify(data):
    result = json.dumps(data, indent=4)
    result = result.replace('"', '')
    result = result.replace(',', '')
    result = result.replace('  }', '    }')
    result = re.sub(r"\n\s\s", '\n', result)
    return result


def main(data):
    result = make_tree(data)
    return stringify(result)
