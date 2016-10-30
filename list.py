#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


LAYOUTS_DIR = os.path.expanduser('~') + '/.config/i3/layouts/'

layouts = sorted([f for f in os.listdir(LAYOUTS_DIR) if '.json' not in f])

print('')
for layout in layouts:
    print(layout)
print('')
