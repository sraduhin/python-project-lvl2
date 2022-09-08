import json
import re

def get_action(action):
    return {
        None: ' ',
        'add': '+',
        'remove': '-',
    }[action]


def has_inner_tree(data):
    return isinstance(data, list)


def make_diff_stylish_tree(data):
    if not has_inner_tree(data):
        return data
    result = {}
    for item in data:
        key, action, value = item
        if action == 'update':
            result[f'- {key}'] = make_diff_stylish_tree(value[0])
            result[f'+ {key}'] = make_diff_stylish_tree(value[1])
        else:
            action = get_action(action)
            result[f'{action} {key}'] = make_diff_stylish_tree(value)
    return result


def stringify(data):
    result = json.dumps(data, indent=4)
    result = result.replace('"', '')
    result = result.replace(',', '')
    result = result.replace('  }', '    }')
    result = re.sub(r"\n\s\s", '\n', result)
    return result


def show_diff_stylish(data):
    result = make_diff_stylish_tree(data)
    return stringify(result)


def make_cosmetics(data):
    if isinstance(data, bool):
        return f'{data}'.lower()
    if data == None:
        return 'null'
    return '[complex value]' if has_inner_tree(data) else data


def get_property(prefix, key):
    return key if prefix == '' else prefix + '.' + key


def show_diff_plain(data):
    actions = ['add', 'remove', 'update']
    def make_diff_by_action(data, prefix=''):
        result = ''
        for item in data:
            key, action, value = item
            if action not in actions:
                if has_inner_tree(value):
                    prefix = get_property(prefix, key)
                    result += make_diff_by_action(value, prefix)
                continue
            result += f"Property '{get_property(prefix, key)}' was "
            if action == 'add':
                result += f"added with value: {make_cosmetics(value)}\n"
            elif action == 'remove':
                result += f"removed\n"
            elif action == 'update':
                result += f"updated. From {make_cosmetics(value[0])} to {make_cosmetics(value[1])}\n"
        return result
    return make_diff_by_action(data)


if __name__ == "__main__":
    SIMPLE_RESULT = [('follow', 'remove', False), ('host', None, 'hexlet.io'), ('proxy', 'remove', '123.234.53.22'), ('timeout', 'update', (50, 20)), ('verbose', 'add', True)]

    NESTED_RESULT = [('common', None, [('follow', 'add', False), ('setting1', None, 'Value 1'), ('setting2', 'remove', 200), ('setting3', 'update', (True, None)), ('setting4', 'add', 'blah blah'), ('setting5', 'add', [('key5', None, 'value5')]), ('setting6', None, [('doge', None, [('wow', 'update', ('', 'so much'))]), ('key', None, 'value'), ('ops', 'add', 'vops')])]), ('group1', None, [('baz', 'update', ('bas', 'bars')), ('foo', None, 'bar'), ('nest', 'update', ([('key', None, 'value')], 'str'))]), ('group2', 'remove', [('abc', None, 12345), ('deep', None, [('id', None, 45)])]), ('group3', 'add', [('deep', None, [('id', None, [('number', None, 45)])]), ('fee', None, 100500)])]
    print(show_diff_plain(SIMPLE_RESULT))
    print(show_diff_plain(NESTED_RESULT))
