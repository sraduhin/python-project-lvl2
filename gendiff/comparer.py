from gendiff.parser.parser import parser
from gendiff.printer import show_diff_stylish


def has_children(data):
    return isinstance(data, dict)

def place_nested_data(data):
    place_data = []
    if has_children(data):
        for key in data.keys():
            place_data.append((key, None, place_nested_data(data.get(key))))
        return place_data
    else:
        return data


def generate_diff(data1, data2):
    result = []
    union_keys = sorted(set(data1.keys() | data2.keys()))  # перенести сортировку в конец программы
    for key in union_keys:
        if has_children(data1.get(key)) and has_children(data2.get(key)):
            result.append((key, None, generate_diff(data1[key], data2[key])))
        elif data1.get(key) == data2.get(key):
            result.append((key, None, place_nested_data(data1[key])))
        elif key in data1 and key in data2:
            result.append((key, 'update', (place_nested_data(data1[key]), place_nested_data(data2[key]))))
        elif key in data1:
            result.append((key, 'remove', place_nested_data(data1[key])))
        else:
            result.append((key, 'add', place_nested_data(data2[key])))
    return result


def run_diff(filepath1, filepath2):
    data1 = parser(filepath1)
    data2 = parser(filepath2)
    result = generate_diff(data1, data2)
    return show_diff_stylish(result)


if __name__ == '__main__':
    # run_diff('tests/fixtures/simple/file1.json', 'tests/fixtures/simple/file2.json')
    # run_diff('tests/fixtures/nested/file1.json', 'tests/fixtures/nested/file2.json')
    print(generate_diff(parser('tests/fixtures/simple/file1.json'), parser('tests/fixtures/simple/file2.json')))
    print(generate_diff(parser('tests/fixtures/nested/file1.json'), parser('tests/fixtures/nested/file2.json')))
    assert generate_diff(parser('tests/fixtures/nested/file1.json'), parser('tests/fixtures/nested/file2.json')) == [('common', None, [('follow', 'add', False), ('setting1', None, 'Value 1'), ('setting2', 'remove', 200), ('setting3', 'update', (True, None)), ('setting4', 'add', 'blah blah'), ('setting5', 'add', [('key5', None, 'value5')]), ('setting6', None, [('doge', None, [('wow', 'update', ('', 'so much'))]), ('key', None, 'value'), ('ops', 'add', 'vops')])]), ('group1', None, [('baz', 'update', ('bas', 'bars')), ('foo', None, 'bar'), ('nest', 'update', ([('key', None, 'value')], 'str'))]), ('group2', 'remove', [('abc', None, 12345), ('deep', None, [('id', None, 45)])]), ('group3', 'add', [('deep', None, [('id', None, [('number', None, 45)])]), ('fee', None, 100500)])]