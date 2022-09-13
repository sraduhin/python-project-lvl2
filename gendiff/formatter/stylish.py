import json
import re


'''def get_action(action):
    return {None: ' ', 'add': '+', 'remove': '-'}[action]'''


def has_children(data):
    return isinstance(data, dict)


def make_tree(data):
    if not has_children(data):
        return data
    result = {}
    for key, value in data.keys():
        key, action, value = item
        if action == 'update':
            result[f'- {key}'] = make_tree(value['old_value'])
            result[f'+ {key}'] = make_tree(value['new_value'])
        else:
            result[f'{value["action"]} {key}'] = make_tree(value)
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
    SIMPLE_RESULT = [('follow', 'remove', False), ('host', None, 'hexlet.io'), ('proxy', 'remove', '123.234.53.22'), ('timeout', 'update', (50, 20)), ('verbose', 'add', True)]

    NESTED_RESULT = [('common', None, [('follow', 'add', False), ('setting1', None, 'Value 1'), ('setting2', 'remove', 200), ('setting3', 'update', (True, None)), ('setting4', 'add', 'blah blah'), ('setting5', 'add', [('key5', None, 'value5')]), ('setting6', None, [('doge', None, [('wow', 'update', ('', 'so much'))]), ('key', None, 'value'), ('ops', 'add', 'vops')])]), ('group1', None, [('baz', 'update', ('bas', 'bars')), ('foo', None, 'bar'), ('nest', 'update', ([('key', None, 'value')], 'str'))]), ('group2', 'remove', [('abc', None, 12345), ('deep', None, [('id', None, 45)])]), ('group3', 'add', [('deep', None, [('id', None, [('number', None, 45)])]), ('fee', None, 100500)])]
    print(main(SIMPLE_RESULT))
    print(main(NESTED_RESULT))
