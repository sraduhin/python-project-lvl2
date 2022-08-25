import json


def generate_diff(filepath1, filepath2):
    with open(filepath1, 'r') as file1:
        f1 = json.load(file1)
        with open(filepath2, 'r') as file2:
            f2 = json.load(file2)
            union_keys = sorted(set(f1.keys() | f2.keys()))
            result = ''
            result += '{'
            for key in union_keys:
                if f1.get(key) == f2.get(key):
                    result += f'\n  + {key}: {f1[key]}'
                elif key in f1 and key in f2:
                    result += f'\n  - {key}: {f1[key]}'
                    result += f'\n  + {key}: {f2[key]}'
                elif key in f1:
                    result += f'\n  - {key}: {f1[key]}'
                else:
                    result += f'\n  + {key}: {f2[key]}'
            result += '\n}'
    return result


if __name__ == '__main__':
    generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')
