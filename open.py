#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys


LAYOUTS_DIR = os.path.expanduser('~') + '/.config/i3/layouts/'


def open_layout(workspace_name, workspace_number=None):
    executables_file = LAYOUTS_DIR + workspace_name
    layout_file = executables_file + '.json'

    if not os.path.isfile(layout_file):
        print('layout not found: ' + workspace_name)
        return
    if not os.path.isfile(executables_file):
        print('executable not found: ' + workspace_name)
        return

    if workspace_number:
        subprocess.check_output(['i3-msg', 'workspace', workspace_number])

    subprocess.check_output(['i3-msg', 'append_layout', layout_file])
    subprocess.check_output([executables_file])


if __name__ == '__main__':
    if len(sys.argv) == 3:
        workspace_name = sys.argv[-2]
        workspace_number = sys.argv[-1]
        if int(workspace_number) not in range(1, 11):
            exit(workspace_number + ' is not a valid workspace')
        open_layout(workspace_name, workspace_number)

    elif len(sys.argv) == 2:
        workspace_name = sys.argv[-1]
        open_layout(workspace_name)

    else:
        exit("usage: open LAYOUT_NAME WORKSPACE_NUMBER")
