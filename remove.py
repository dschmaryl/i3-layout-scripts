#!/usr/bin/env python3

from os import listdir, remove
from sys import argv

from config import CREATE_BIN_SHORTCUTS, BIN_DIR, LAYOUTS_DIR


def get_layouts():
    return sorted([f for f in listdir(LAYOUTS_DIR) if '.json' not in f])


def remove_layout(layout_name):
    remove(LAYOUTS_DIR + layout_name)
    remove(LAYOUTS_DIR + layout_name + '.json')
    if CREATE_BIN_SHORTCUTS:
        remove(BIN_DIR + layout_name)


if __name__ == '__main__':
    if len(argv) != 2:
        print("usage: remove LAYOUT_NAME")
    else:
        layout_name = argv[-1]
        layouts = get_layouts()
        if layout_name in layouts:
            remove_layout(layout_name)
            print("layout '" + layout_name + "' removed")
        else:
            print("no layout named '" + layout_name + "'")
