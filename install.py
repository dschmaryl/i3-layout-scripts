#!/usr/bin/env python3

from os import environ
from pathlib import Path
from subprocess import call, DEVNULL, STDOUT

from config import LAYOUTS_DIR, BIN_DIR


def check_commands():
    print("Checking 'which i3-save-tree'...")
    try:
        which_command = 'which i3-save-tree'.split(' ')
        if call(which_command, stdout=DEVNULL, stderr=STDOUT) == 1:
            print("ERROR: 'i3-save-tree' command not found. Is i3 installed?")
            return 1
    except FileNotFoundError:
        print("ERROR: 'which' command not found. Please install.")
        return 1

    print('Success.')
    return 0


def create_layouts_dirs():
    layouts_dir = Path(LAYOUTS_DIR)
    if layouts_dir.exists():
        print('Layouts dir already exists')
    else:
        layouts_dir.mkdir()
        print("Created layouts dir at '%s'" % layouts_dir)

    bin_dir = Path(BIN_DIR)
    if bin_dir.exists():
        print('Bin dir already exists')
    else:
        bin_dir.mkdir()
        print("Created bin dir at '%s'" % bin_dir)

    if environ['PATH'].find(BIN_DIR[:-1]) == -1:
        print('Bin dir not currently in your PATH. Please add it')


if __name__ == '__main__':
    # check to make sure both 'which' and 'i3-save-tree' are installed
    if check_commands() == 1:
        exit(1)

    # create directories used to save layouts and shortcuts
    answer = input("Create directories according to 'config.py'? [y]/n: ")
    if answer in ['', 'y', 'yes', 'Y']:
        create_layouts_dirs()
