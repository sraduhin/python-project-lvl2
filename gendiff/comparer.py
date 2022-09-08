from gendiff.parser.parser import parser
from gendiff.printer import show_diff_stylish


'''def put(data):
    dict_data = {}
    if not isinstance(data, dict):
        return data
    for key in data.keys():
        dict_data[f'  {key}'] = put(data[key])
    return dict_data'''

'''def generate_diff(data1, data2):
    result = {}
    union_keys = sorted(set(data1.keys() | data2.keys()))  # перенести сортировку в конец программы
    for key in union_keys:
        if data1.get(key) == data2.get(key):
            result[f'  {key}'] = put(data1[key])
        elif key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result[f'  {key}'] = generate_diff(data1[key], data2[key])
            else:
                result[f'- {key}'] = put(data1[key])
                result[f'+ {key}'] = put(data2[key])
        elif key in data1:
            result[f'- {key}'] = put(data1[key])
        else:
            result[f'+ {key}'] = put(data2[key])
    return result'''


def generate_diff(data1, data2):
    result = {}
    union_keys = sorted(set(data1.keys() | data2.keys()))  # перенести сортировку в конец программы
    for key in union_keys:
        if data1.get(key) == data2.get(key):
            if isinstance(data1[key], dict):
                result[key]['children'] = data1[key]
            result[key]['value'] = data1[key]
        elif key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result[key] = generate_diff(data1[key], data2[key])
            else:
                result[key] = {'action': 'updated', 'From': data1[key],
                               'to': data2[key]}
        elif key in data1:
            result[key] = {'action': 'removed', 'value': data1[key]}
        else:
            result[key] = {'action': 'added', 'value': data2[key]}
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