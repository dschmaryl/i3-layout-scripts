#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


LAYOUTS_DIR = os.path.expanduser('~') + '/.config/i3/layouts/'
BIN_DIR = LAYOUTS_DIR + 'bin/'


def get_layouts():
    return sorted([f for f in os.listdir(LAYOUTS_DIR) if '.json' not in f])


def remove(layout_name):
    os.remove(LAYOUTS_DIR + layout_name)
    os.remove(LAYOUTS_DIR + layout_name + '.json')
    os.remove(BIN_DIR + layout_name)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: remove LAYOUT_NAME")
    else:
        layout_name = sys.argv[-1]
        layouts = get_layouts()
        if layout_name in layouts:
            remove(layout_name)
            print("layout '" + layout_name + "' removed")
        else:
            print("no layout named '" + layout_name + "'")
