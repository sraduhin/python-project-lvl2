SIMPLE_REPR = [
    ('follow', 'remove', False),
    ('host', None, 'hexlet.io'),
    ('proxy', 'remove', '123.234.53.22'),
    ('timeout', 'update', (50, 20)),
    ('verbose', 'add', True)
]

NESTED_REPR = [
    ('common', None,[
        ('follow', 'add', False),
        ('setting1', None, 'Value 1'),
        ('setting2', 'remove', 200),
        ('setting3', 'update', (True, None)),
        ('setting4', 'add', 'blah blah'),
        ('setting5', 'add', [
            ('key5', None, 'value5')
            ]),
        ('setting6', None, [
            ('doge', None, [
                ('wow', 'update', ('', 'so much'))
            ]),
            ('key', None, 'value'),
            ('ops', 'add', 'vops')
        ])]),
    ('group1', None, [
        ('baz', 'update', ('bas', 'bars')),
        ('foo', None, 'bar'),
        ('nest', 'update', ([
            ('key', None, 'value')
        ], 'str'))
    ]),
    ('group2', 'remove', [
        ('abc', None, 12345),
        ('deep', None, [
            ('id', None, 45)
        ])]),
    ('group3', 'add', [
        ('deep', None, [
            ('id', None, [
                ('number', None, 45)
            ])
        ]),
        ('fee', None, 100500)
    ])
]

SIMPLE_PARSED_DATA = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False
}

NESTED_PARSED_DATA = {
    'common': {
        'setting1': 'Value 1',
        'setting2': 200,
        'setting3': True,
        'setting6': {
            'key': 'value',
            'doge': {
                'wow': ''
            }
        }
    },
    'group1': {
        'baz': 'bas',
        'foo': 'bar',
        'nest': {
            'key': 'value'
        }
    },
    'group2': {
        'abc': 12345,
        'deep': {
            'id': 45
        }
    }
}