#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir

from config import LAYOUTS_DIR


layouts = sorted([f for f in listdir(LAYOUTS_DIR) if '.json' not in f])

print('')
for layout in layouts:
    print(layout)
print('')
