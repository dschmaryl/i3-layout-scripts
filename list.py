#!/usr/bin/env python3

from os import listdir

from config import LAYOUTS_DIR

print('')
for file_name in sorted(listdir(LAYOUTS_DIR)):
    if '.json' in file_name:
        print(file_name.split('.json')[0])
print('')
