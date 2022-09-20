import os
import json
import yaml


JSON_EXTENSIONS = ['json']
YAML_EXTENSIONS = ['yml', 'yaml']


def load_file(filepath):
    '''
    read file

    input: path string

    output: file data

    raises: wrong path, wrong extension
    '''
    if os.path.isfile(filepath):
        extension = filepath.split('.')[1]
        if extension not in (JSON_EXTENSIONS + YAML_EXTENSIONS):
            file_name = filepath.split('/').pop()
            raise ValueError(f'enexpected extension of the file: {file_name}')
        with open(filepath, 'r') as f:
            f = f.read()
            return f, extension
    raise ValueError(f"{filepath} doesn't exists")


def parse_file(content, extension='undefined'):
    '''
    parse data to required type

    input: file data

    output: json or yaml kind of data, extension

    raises: wrong file data
    '''
    if extension == 'undefined':
        if content.startswith('---'):
            return yaml.safe_load(content)
        elif content.startswith('{'):
            return json.loads(content)
        raise ValueError('Wrong file data')
    if extension in JSON_EXTENSIONS:
        return json.loads(content)
    if extension in YAML_EXTENSIONS:
        return yaml.safe_load(content)
