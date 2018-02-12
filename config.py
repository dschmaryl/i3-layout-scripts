#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import expanduser


# Default location is '~/.i3-layouts'. Change according to preference.
# LAYOUTS_DIR must end with '/'
LAYOUTS_DIR = expanduser('~') + '/.i3-layouts/'

# BIN_DIR is the folder in which shortcuts to open layouts are saved. Make
# sure this directory is in your PATH. Must end with '/'
BIN_DIR = expanduser('~') + '/.i3-layouts/bin/'
