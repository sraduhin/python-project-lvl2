from ast import operator
import json
import re


def show_diff(data):
    result = json.dumps(data, indent=4)
    result = result.replace('"', '')
    result = result.replace(',', '')
    result = result.replace('  }', '    }')
    result = re.sub(r"\n\s\s", '\n', result)
    return result


def show_diff_plain(data):
    result = ''
    for key in data.keys():
        action = key[:1]
        property = key[2:]
        result += f"Property '{property}' was {action} with {data[key]}\n"
    return result



if __name__ == "__main__":
    simple_data = {'- follow': False, '  host': 'hexlet.io', '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20, '+ verbose': True}
    nested_data = {'  common': {'+ follow': False, '  setting1': 'Value 1', '- setting2': 200, '- setting3': True, '+ setting3': None, '+ setting4': 'blah blah', '+ setting5': {'  key5': 'value5'}, '  setting6': {'  doge': {'- wow': '', '+ wow': 'so much'}, '  key': 'value', '+ ops': 'vops'}}, '  group1': {'- baz': 'bas', '+ baz': 'bars', '  foo': 'bar', '- nest': {'  key': 'value'}, '+ nest': 'str'}, '- group2': {'  abc': 12345, '  deep': {'  id': 45}}, '+ group3': {'  deep': {'  id': {'  number': 45}}, '  fee': 100500}}
    with open('tests/fixtures/nested/result_plain', 'r') as f:
        f = f.read()
        print(f)
    print('>>>')
    print(show_diff_plain(nested_data))
    print(show_diff(nested_data))
