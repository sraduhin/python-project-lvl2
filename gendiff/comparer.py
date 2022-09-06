from gendiff.parser.parser import parser


def generate_diff(data1, data2):
    result = {}
    union_keys = sorted(set(data1.keys() | data2.keys()))
    for key in union_keys:
        if data1.get(key) == data2.get(key):
            result[f'  {key}'] = data1[key]
        elif key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result[f'  {key}'] = generate_diff(data1[key], data2[key])
            else:
                result[f'- {key}'] = data1[key]
                result[f'+ {key}'] = data2[key]
        elif key in data1:
            result[f'- {key}'] = data1[key]
        else:
            result[f'+ {key}'] = data2[key]
    return result


def run_differ(filepath1, filepath2):
    data1 = parser(filepath1)
    data2 = parser(filepath2)
    return generate_diff(data1, data2)


if __name__ == '__main__':
    # {
    #   '- follow': False,
    #   '  host': 'hexlet.io',
    #   '- proxy': '123.234.53.22',
    #   '- timeout': 50,
    #   '+ timeout': 20,
    #   '+ verbose': True
    # }
    run_differ('tests/fixtures/plain/file1.json', 'tests/fixtures/plain/file2.json')
    # {
    #   '  common': {
    #       '+ follow': False,
    #       '  setting1': 'Value 1',
    #       '- setting2': 200,
    #       '- setting3': True,
    #       '+ setting3': None,
    #       '+ setting4': 'blah blah', '+ setting5': {'key5': 'value5'}, '  setting6': {'  doge': {'- wow': '', '+ wow': 'so much'}, '  key': 'value', '+ ops': 'vops'}}, '  group1': {'- baz': 'bas', '+ baz': 'bars', '  foo': 'bar', '- nest': {'key': 'value'}, '+ nest': 'str'}, '- group2': {'abc': 12345, 'deep': {'id': 45}}, '+ group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
    run_differ('tests/fixtures/nested/file1.json', 'tests/fixtures/nested/file2.json')
