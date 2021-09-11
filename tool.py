#!/usr/bin/env python3
import argparse
import os

def find_external_file():
    fname = 'weird-external-file.txt'
    for dir in os.environ['PATH'].split(os.pathsep):
        fullname = os.path.join(dir, fname)
        if os.path.exists(fullname):
            return fullname

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--flag', action='store_true')

    args = parser.parse_args()
    if args.flag:
        print('Flag set')
    print('Internal tool')
    print('Trying to read txt file...')
    with open(find_external_file(), 'r') as f:
        print('Read txt file:')
        print(f.read())

if __name__ == '__main__':
    main()
