from gendiff.parser.parser import parser


def generate_diff(filepath1, filepath2):
    data1 = parser(filepath1)
    data2 = parser(filepath2)
    result = ''
    union_keys = sorted(set(data1.keys() | data2.keys()))
    result += '{'
    for key in union_keys:
        if data1.get(key) == data2.get(key):
            result += f'\n  + {key}: {data1[key]}'
        elif key in data1 and key in data2:
            result += f'\n  - {key}: {data1[key]}'
            result += f'\n  + {key}: {data2[key]}'
        elif key in data1:
            result += f'\n  - {key}: {data1[key]}'
        else:
            result += f'\n  + {key}: {data2[key]}'
    result += '\n}'
    return result


if __name__ == '__main__':
    generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')
