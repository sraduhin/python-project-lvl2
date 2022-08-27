import os
import json
import yaml


JSON_EXTENSIONS = ['json']
YAML_EXTENSIONS = ['yml', 'yaml']


def parser(filepath):
    if os.path.isfile(filepath):
        if filepath.split('.')[1] not in (JSON_EXTENSIONS + YAML_EXTENSIONS):
            file_name = filepath.split('/').pop()
            raise ValueError(f'enexpected extension of the file: {file_name}')

        with open(filepath, 'r') as f:
            if filepath.split('.')[1] in JSON_EXTENSIONS:
                return json.load(f)
            if filepath.split('.')[1] in YAML_EXTENSIONS:
                return yaml.safe_load(f)
    raise ValueError(f"{filepath} doesn't exists")


if __name__ == '__main__':
    print(parser('gendiff/files/file1.json'))