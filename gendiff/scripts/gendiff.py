#!/usr/bin/env python3
import argparse

from gendiff import main as run_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='first_file')
    parser.add_argument('second_file', help='second_file')
    parser.add_argument('-f', '--format', action='store', help='set format of output')

    args = parser.parse_args()

    diff = run_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
