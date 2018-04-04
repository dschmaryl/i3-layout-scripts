#!/usr/bin/env python3

from os.path import expanduser


# Default location is '~/.i3-layouts'. Change according to preference.
# Note: must end with '/'
LAYOUTS_DIR = expanduser('~') + '/.i3-layouts/'

# If this is set to True, then a bash executable is created with the same name
# as the layout. This way, you can enter just the layout name in dmenu or
# command line to launch a layout.
CREATE_BIN_SHORTCUTS = True

# BIN_DIR is the folder in which shortcuts to open layouts are saved. Make
# sure this directory is in your PATH. Obviously, this doesn't apply if
# CREATE_BIN_SHORTCUTS is set to False.
# Note: must end with '/'
BIN_DIR = expanduser('~') + '/.i3-layouts/bin/'
