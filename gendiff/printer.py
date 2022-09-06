import json


plain_data = {
    '- follow': False,
    '  host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
    '+ timeout': 20,
    '+ verbose': True,
}

nested_data = {
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
}


def show_diff(data):
    result = json.dumps(data, indent=2)
    result = result.replace('"', '')
    result = result.replace(',', '')
    return result


if __name__ == "__main__":
    show_diff(plain_data)
    show_diff(nested_data)
