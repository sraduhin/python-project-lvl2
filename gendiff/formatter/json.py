import json


def get_action(action):
    return {None: ' ', 'add': '+', 'remove': '-'}[action]


def has_inner_tree(data):
    return isinstance(data, list)


def make_diff(data):
    if not has_inner_tree(data):
        return data
    result = {}
    for item in data:
        key, action, value = item
        if action == 'update':
            result[f'- {key}'] = make_diff(value[0])
            result[f'+ {key}'] = make_diff(value[1])
        else:
            action = get_action(action)
            result[f'{action} {key}'] = make_diff(value)
    return result


def main(data):
    result = make_diff(data)
    return json.dumps(result)


if __name__ == "__main__":
    SIMPLE_RESULT = [('follow', 'remove', False), ('host', None, 'hexlet.io'), ('proxy', 'remove', '123.234.53.22'), ('timeout', 'update', (50, 20)), ('verbose', 'add', True)]

    NESTED_RESULT = [('common', None, [('follow', 'add', False), ('setting1', None, 'Value 1'), ('setting2', 'remove', 200), ('setting3', 'update', (True, None)), ('setting4', 'add', 'blah blah'), ('setting5', 'add', [('key5', None, 'value5')]), ('setting6', None, [('doge', None, [('wow', 'update', ('', 'so much'))]), ('key', None, 'value'), ('ops', 'add', 'vops')])]), ('group1', None, [('baz', 'update', ('bas', 'bars')), ('foo', None, 'bar'), ('nest', 'update', ([('key', None, 'value')], 'str'))]), ('group2', 'remove', [('abc', None, 12345), ('deep', None, [('id', None, 45)])]), ('group3', 'add', [('deep', None, [('id', None, [('number', None, 45)])]), ('fee', None, 100500)])]
    print(main(SIMPLE_RESULT))
    print(main(NESTED_RESULT))
