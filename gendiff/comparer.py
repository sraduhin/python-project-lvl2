from gendiff.parser.parser import parser
from gendiff.formatter.stylish import main as show_diff_stylish
from gendiff.formatter.plain import main as show_diff_plain


def has_children(data):
    return isinstance(data, dict)


def get_children_repr(data):
    childrens = {}
    if has_children(data):
        for key in data.keys():
            childrens[key] = get_children_repr(data.get(key))
            #  childrens.append((key, None, get_children_repr(data.get(key))))
        return childrens
    else:
        return data


def generate_diff(data1, data2):
    result = {}
    union_keys = sorted(set(data1.keys() | data2.keys()))  # перенести сортировку в конец программы
    for key in union_keys:
        if has_children(data1.get(key)) and has_children(data2.get(key)):
            result[key] = generate_diff(data1[key], data2[key])
            #  result.append((key, None, generate_diff(data1[key], data2[key])))
        elif data1.get(key) == data2.get(key):
            result[key] = {'value': get_children_repr(data1[key])}
            #  result.append((key, None, get_children_repr(data1[key])))
        elif key in data1 and key in data2:
            action = 'update'
            old_value = get_children_repr(data1[key])
            new_value = get_children_repr(data2[key])
            result[key] = {'action': action, 'old_value': old_value, 'new_value': new_value}
        elif key in data1:
            action = '-'
            value = get_children_repr(data1[key])
            result[key] = {'action': action, 'value': value}
        else:
            action = '+'
            value = get_children_repr(data2[key])
            result[key] = {'action': action, 'value': value}
    return result


def main(filepath1, filepath2, format='stylish'):
    data1 = parser(filepath1)
    data2 = parser(filepath2)
    result = generate_diff(data1, data2)
    if format == 'stylish' or format is None:
        return show_diff_stylish(result)
    elif format == 'plain':
        return show_diff_plain(result)
    raise ValueError(f"Unknown format: {format}")


if __name__ == '__main__':
    print(generate_diff(parser('tests/fixtures/simple/file1.json'), parser('tests/fixtures/simple/file2.json')))
    print(generate_diff(parser('tests/fixtures/nested/file1.json'), parser('tests/fixtures/nested/file2.json')))
    assert generate_diff(parser('tests/fixtures/nested/file1.json'), parser('tests/fixtures/nested/file2.json')) == [('common', None, [('follow', 'add', False), ('setting1', None, 'Value 1'), ('setting2', 'remove', 200), ('setting3', 'update', (True, None)), ('setting4', 'add', 'blah blah'), ('setting5', 'add', [('key5', None, 'value5')]), ('setting6', None, [('doge', None, [('wow', 'update', ('', 'so much'))]), ('key', None, 'value'), ('ops', 'add', 'vops')])]), ('group1', None, [('baz', 'update', ('bas', 'bars')), ('foo', None, 'bar'), ('nest', 'update', ([('key', None, 'value')], 'str'))]), ('group2', 'remove', [('abc', None, 12345), ('deep', None, [('id', None, 45)])]), ('group3', 'add', [('deep', None, [('id', None, [('number', None, 45)])]), ('fee', None, 100500)])]