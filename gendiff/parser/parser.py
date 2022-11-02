import json
import yaml

JSON_FORMATS = ['json']
YAML_FORMATS = ['yml', 'yaml']


def get_format(filepath):
    '''
    extract .format

    input: path string

    output: str or None
    '''
    chain = filepath.split('.')
    return chain[-1] if len(chain) > 1 else None


def parse_file(content, format='undefined'):
    '''
    parse data to required type

    input: file data

    output: json or yaml kind of data, extension

    raises: wrong file data
    '''
    if format == 'undefined':
        if content.startswith('---'):
            return yaml.safe_load(content)
        elif content.startswith('{'):
            return json.loads(content)
        raise ValueError('Wrong file data')
    if format in JSON_FORMATS:
        return json.loads(content)
    if format in YAML_FORMATS:
        return yaml.safe_load(content)
    raise ValueError(f'enexpected format: {format}')
