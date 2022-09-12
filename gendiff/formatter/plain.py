def has_inner_tree(data):
    return isinstance(data, list)


def make_cosmetics(data):
    if isinstance(data, bool):
        return f'{data}'.lower()
    if isinstance(data, int):
        return data
    if data is None:
        return 'null'
    return '[complex value]' if has_inner_tree(data) else f"'{data}'"


def get_property(prefix, key):
    return key if prefix == '' else prefix + '.' + key


def main(data):
    actions = ['add', 'remove', 'update']

    def make_diff_by_action(data, depth=[]):
        result = ''
        for item in data:
            key, action, value = item
            if action not in actions:
                if has_inner_tree(value):
                    depth.append(key)
                    result += make_diff_by_action(value, depth)
                    depth.pop()
                continue
            depth.append(key)
            result += f"Property '{'.'.join(depth)}' was "
            if action == 'add':
                result += f"added with value: {make_cosmetics(value)}\n"
            elif action == 'remove':
                result += "removed\n"
            elif action == 'update':
                result += f"updated. From {make_cosmetics(value[0])} "
                result += f"to {make_cosmetics(value[1])}\n"
            depth.pop()
        return result
    return make_diff_by_action(data)[:-1]  # [:-1] cut last \n


if __name__ == "__main__":
    SIMPLE_RESULT = [('follow', 'remove', False), ('host', None, 'hexlet.io'), ('proxy', 'remove', '123.234.53.22'), ('timeout', 'update', (50, 20)), ('verbose', 'add', True)]

    NESTED_RESULT = [
        ('common', None, [
            ('follow', 'add', False),
            ('setting1', None, 'Value 1'),
            ('setting2', 'remove', 200),
            ('setting3', 'update', (True, None)), 
            ('setting4', 'add', 'blah blah'),
            ('setting5', 'add', [
                ('key5', None, 'value5')]),
            ('setting6', None, [
                ('doge', None, [
                    ('wow', 'update', ('', 'so much'))]),
                ('key', None, 'value'),
                ('ops', 'add', 'vops')])]),
        ('group1', None, [
            ('baz', 'update', ('bas', 'bars')),
            ('foo', None, 'bar'),
            ('nest', 'update', ([
                ('key', None, 'value')], 'str'))]), ('group2', 'remove', [('abc', None, 12345), ('deep', None, [('id', None, 45)])]), ('group3', 'add', [('deep', None, [('id', None, [('number', None, 45)])]), ('fee', None, 100500)])]
    print(main(SIMPLE_RESULT))
    print(main(NESTED_RESULT))
