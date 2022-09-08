import json
import re


def get_action(data):
    if not data.get('action'):
        return ' '
    return "+" if data.get('action') == 'added' else "-"


def put(data):
    dict_data = {}
    if not isinstance(data, dict):
        return data
    for key in data.keys():
        dict_data[f'  {key}'] = put(data[key])
    return dict_data


def show_diff_stylish(data):
    result = {}
    for key in data.keys():
        action = get_action(data[key])
        result[f'{action} {key}'] = put(data[key])
    result = json.dumps(result, indent=4)
    #result = result.replace('"', '')
    #result = result.replace(',', '')
    #result = result.replace('  }', '    }')
    #result = re.sub(r"\n\s\s", '\n', result)
    return result


def show_diff_plain(data):
    result = ''
    for key in data.keys():
        action = key[:1]
        property = key[2:]
        result += f"Property '{property}' was {action} with {data[key]}\n"
    return result



if __name__ == "__main__":
    SIMPLE_RESULT = {'follow': {'action': 'removed', 'value': False}, 'host': {'value': 'hexlet.io'}, 'proxy': {'action': 'removed', 'value': '123.234.53.22'}, 'timeout': {'action': 'updated', 'From': 50, 'to': 20}, 'verbose': {'action': 'added', 'value': True}}

    NESTED_RESULT = {'common': {'follow': {'action': 'added', 'value': False}, 'setting1': {'value': 'Value 1'}, 'setting2': {'action': 'removed', 'value': 200}, 'setting3': {'action': 'updated', 'From': True, 'to': None}, 'setting4': {'action': 'added', 'value': 'blah blah'}, 'setting5': {'action': 'added', 'value': {'key5': 'value5'}}, 'setting6': {'doge': {'wow': {'action': 'updated', 'From': '', 'to': 'so much'}}, 'key': {'value': 'value'}, 'ops': {'action': 'added', 'value': 'vops'}}}, 'group1': {'baz': {'action': 'updated', 'From': 'bas', 'to': 'bars'}, 'foo': {'value': 'bar'}, 'nest': {'action': 'updated', 'From': {'key': 'value'}, 'to': 'str'}}, 'group2': {'action': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}}, 'group3': {'action': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}
    '''with open('tests/fixtures/nested/result_plain', 'r') as f:
        f = f.read()
        print(f)
    print('>>>')
    print(show_diff_plain(nested_data))'''
    print(show_diff_stylish(NESTED_RESULT))
    print(show_diff_stylish(SIMPLE_RESULT))
