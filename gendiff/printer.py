import json
import re


'''plain_data = {
    '- follow': False,
    '  host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
    '+ timeout': 20,
    '+ verbose': True,
}'''

'''nested_data = {
    '  common': {
        '+ follow': False,
        '  setting1': 'Value 1',
        '- setting2': 200,
        '- setting3': True,
        '+ setting3': None,
        '+ setting4': 'blah blah',
        '+ setting5': {
            'key5': 'value5',
        },
        '  setting6': {
            '  doge': {
                '- wow': '',
                '+ wow': 'so much',
            },
            '  key': 'value',
            '+ ops': 'vops',
        },
    },
    '  group1': {
        '- baz': 'bas',
        '+ baz': 'bars',
        '  foo': 'bar',
        '- nest': {
            'key': 'value',
        },
        '+ nest': 'str',
    },
    '- group2': {
        'abc': 12345,
        'deep': {
            'id': 45,
        },
    },
    '+ group3': {
        'deep': {
            'id': {
                'number': 45,
            },
        },
        'fee': 100500,
    },
}'''


plain_data = {'follow': {'value': False, 'operator': '-'}, 'host': {'value': 'hexlet.io'}, 'proxy': {'value': '123.234.53.22', 'operator': '-'}, 'timeout': {'value': 20, 'operator': '+'}, 'verbose': {'value': True, 'operator': '+'}}

nested_data = {'common': {'value': {'follow': {'value': False, 'operator': '+'}, 'setting1': {'value': 'Value 1'}, 'setting2': {'value': 200, 'operator': '-'}, 'setting3': {'value': None, 'operator': '+'}, 'setting4': {'value': 'blah blah', 'operator': '+'}, 'setting5': {'value': {'key5': {'value': 'value5'}}, 'operator': '+'}, 'setting6': {'value': {'doge': {'value': {'wow': {'value': 'so much', 'operator': '+'}}}, 'key': {'value': 'value'}, 'ops': {'value': 'vops', 'operator': '+'}}}}}, 'group1': {'value': {'baz': {'value': 'bars', 'operator': '+'}, 'foo': {'value': 'bar'}, 'nest': {'value': 'str', 'operator': '+'}}}, 'group2': {'value': {'abc': {'value': 12345}, 'deep': {'value': {'id': {'value': 45}}}}, 'operator': '-'}, 'group3': {'value': {'deep': {'value': {'id': {'value': {'number': {'value': 45}}}}}, 'fee': {'value': 100500}}, 'operator': '+'}}
def join_key_and_operator(dict_):
    result_dict = {}
    for key in dict_.keys():
        operator = dict_[key].get('operator') or ' '
        if not isinstance(dict_[key]['value'], dict):
            result_dict[f'{operator} {key}'] = dict_[key]['value']
        else:
            result_dict[f'{operator} {key}'] = join_key_and_operator(dict_[key]['value'])
    return result_dict


def show_diff(data):
    joined_data = join_key_and_operator(data)
    result = json.dumps(joined_data, indent=4)
    result = result.replace('"', '')
    result = result.replace(',', '')
    result = result.replace('  }', '    }')
    result = re.sub(r"\n\s\s", '\n', result)
    return result


if __name__ == "__main__":
    #print(join_key_and_operator(plain_data))
    #print(join_key_and_operator(nested_data))
    print(show_diff(plain_data))
    print(show_diff(nested_data))
