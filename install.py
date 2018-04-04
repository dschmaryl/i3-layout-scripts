#!/usr/bin/env python3

from os import environ
from pathlib import Path
from subprocess import call, DEVNULL, STDOUT

from config import CREATE_BIN_SHORTCUTS, BIN_DIR, LAYOUTS_DIR


def check_commands():
    print("Checking 'i3-save-tree'")
    try:
        i3_save_tree_command = "i3-save-tree --version".split(' ')
        call(i3_save_tree_command, stdout=DEVNULL, stderr=STDOUT)
    except FileNotFoundError:
        print("ERROR: 'i3-save-tree' command not found. Is i3 installed?")
        return 1

    if CREATE_BIN_SHORTCUTS:
        print("Checking 'which'")
        try:
            which_command = 'which ls'.split(' ')
            call(which_command, stdout=DEVNULL, stderr=STDOUT)
        except FileNotFoundError:
            print("ERROR: 'which' command not found. Please install 'which'",
                  "to create bin shortcuts, or set CREATE_BIN_SHORTCUTS to",
                  "False in 'config.py'")
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

    if CREATE_BIN_SHORTCUTS:
        bin_dir = Path(BIN_DIR)
        if bin_dir.exists():
            print('Bin dir already exists')
        else:
            bin_dir.mkdir()
            print("Created bin dir at '%s'" % bin_dir)

        if environ['PATH'].find(BIN_DIR[:-1]) == -1:
            print('Bin dir not currently in your PATH. Please add it')


if __name__ == '__main__':
    # check to make sure 'i3-save-tree' and 'which' are installed
    if check_commands() == 1:
        exit(1)

    # create directories used to save layouts and shortcuts
    answer = input("Create directories according to 'config.py'? [y]/n: ")
    if answer in ['', 'y', 'yes', 'Y']:
        create_layouts_dirs()
