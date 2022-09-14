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
                result[f'- {key}'] = value['old_value']
                result[f'+ {key}'] = value['new_value']
            else:
                result[f'{action} {key}'] = value['value']
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


if __name__ == "__main__":
    import
    SIMPLE_REPR = {'follow': {'action': '-', 'value': False}, 'host': 'hexlet.io', 'proxy': {'action': '-', 'value': '123.234.53.22'}, 'timeout': {'action': 'update', 'old_value': 50, 'new_value': 20}, 'verbose': {'action': '+', 'value': True}}

    NESTED_REPR = {'common': {'follow': {'action': '+', 'value': False}, 'setting1': 'Value 1', 'setting2': {'action': '-', 'value': 200}, 'setting3': {'action': 'update', 'old_value': True, 'new_value': None}, 'setting4': {'action': '+', 'value': 'blah blah'}, 'setting5': {'action': '+', 'value': {'key5': 'value5'}}, 'setting6': {'doge': {'wow': {'action': 'update', 'old_value': '', 'new_value': 'so much'}}, 'key': 'value', 'ops': {'action': '+', 'value': 'vops'}}}, 'group1': {'baz': {'action': 'update', 'old_value': 'bas', 'new_value': 'bars'}, 'foo': 'bar', 'nest': {'action': 'update', 'old_value': {'key': 'value'}, 'new_value': 'str'}}, 'group2': {'action': '-', 'value': {'abc': 12345, 'deep': {'id': 45}}}, 'group3': {'action': '+', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}
    print(main(SIMPLE_REPR))
    print(main(NESTED_REPR))
