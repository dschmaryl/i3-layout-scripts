#!/usr/bin/env python3

from os import listdir

from config import LAYOUTS_DIR


def get_layouts():
    return sorted([f.split('.json')[0]
                   for f in listdir(LAYOUTS_DIR) if '.json' in f])


if __name__ == '__main__':
    print('')
    for layout in get_layouts():
        print(layout)
    print('')
