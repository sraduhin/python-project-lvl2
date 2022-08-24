#!/usr/bin/env python3
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='first_file')
    parser.add_argument('second_file', help='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

def generate_diff(filepath1, filepath2):
    with open(filepath1, 'r') as file1:
        f1 = json.load(file1)
        with open(filepath2, 'r') as file2:
            f2 = json.load(file2)
            union_keys = sorted(set(f1.keys() | f2.keys()))
            print('{')
            for key in union_keys:
                if f1.get(key) == f2.get(key):
                    print('\t+ {}: {}'.format(key, f1[key]))
                elif key in f1 and key in f2:
                    print('\t- {}: {}'.format(key, f1[key]))
                    print('\t+ {}: {}'.format(key, f2[key]))
                elif key in f1:
                    print('\t- {}: {}'.format(key, f1[key]))
                else:
                    print('\t+ {}: {}'.format(key, f2[key]))
            print('}')


if __name__ == '__main__':
    generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')
