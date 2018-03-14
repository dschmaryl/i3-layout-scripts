#!/usr/bin/env python3

from os import listdir

from config import LAYOUTS_DIR


layouts = sorted([f for f in listdir(LAYOUTS_DIR) if '.json' not in f])

print('')
for layout in layouts:
    if layout == 'bin':
        # don't list bin dir as layout
        continue
    else:
        print(layout)
print('')
