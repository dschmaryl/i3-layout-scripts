#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from subprocess import call, DEVNULL, STDOUT

from config import LAYOUTS_DIR, BIN_DIR


def check_i3_save_tree_command():
    if call('i3-save-tree', stdout=DEVNULL, stderr=STDOUT) == 2:
        raise Exception


def create_layouts_dirs():
    layouts_dir = Path(LAYOUTS_DIR)
    if layouts_dir.exists():
        print('layouts dir already exists')
    else:
        layouts_dir.mkdir()
        print("created layouts dir at '%s'" % layouts_dir)

    bin_dir = Path(BIN_DIR)
    if bin_dir.exists():
        print('bin dir already exists')
    else:
        bin_dir.mkdir()
        print("created bin dir at '%s'" % bin_dir)


if __name__ == '__main__':
    try:
        print("Checking 'i3-save-tree' command...")
        check_i3_save_tree_command()
        print('Success.')
    except Exception:
        print("ERROR: 'i3-save-tree' command failed.")
        print("Most likely, the 'perl-anyevent-i3' package is missing.")
        exit(1)

    answer = input("create dirs according to 'config.py'? (y)/n: ")
    if answer in ['', 'y', 'yes', 'Y']:
        create_layouts_dirs()
