import os


def load_file(filepath):
    '''
    read file

    input: path string

    output: file data

    raises: file doesnt exists
    '''
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            f = f.read()
            return f
    raise ValueError(f"{filepath} doesn't exists")
