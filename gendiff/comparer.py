#from gendiff.parser.parser import parser
#from gendiff.formatter.stylish import main as show_diff_stylish
#from gendiff.formatter.plain import main as show_diff_plain


def generate_diff(data1, data2):
    result = {}
    union_keys = sorted(set(data1.keys() | data2.keys()))  # перенести сортировку в конец программы
    for key in union_keys:
        if isinstance(data1.get(key)), dict) and isinstance(data2.get(key)):
            result[key] = generate_diff(data1[key], data2[key])
        elif data1.get(key) == data2.get(key):
            result[key] = data1.get(key)
        elif key in data1 and key in data2:
            result[key] = {'action': 'update', 'old_value': data1[key], 'new_value': data2[key]}
        elif key in data1:
            result[key] = {'action': '-', 'value': data1[key]}
        else:
            result[key] = {'action': '+', 'value': data2[key]}
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
    data1 = parser('tests/fixtures/nested/file1.json')
    data2 = parser('tests/fixtures/nested/file2.json')
    print(generate_diff(data1, data2))
    data1 = parser('tests/fixtures/simple/file1.json')
    data2 = parser('tests/fixtures/simple/file2.json')
    print(generate_diff(data1, data2))