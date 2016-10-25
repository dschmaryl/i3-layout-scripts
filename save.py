#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

from subprocess import call, check_output, DEVNULL, STDOUT


LAYOUTS_DIR = '/home/daryl/.config/i3/layouts/'
BIN_DIR = LAYOUTS_DIR + 'bin/'


def get_layout(workspace):
    i3_save_tree = ['i3-save-tree', '--workspace', workspace]
    return check_output(i3_save_tree).decode('utf-8').split("\n")


def save_layout(layout, layout_name):
    executables_file = LAYOUTS_DIR + layout_name
    layout_file = executables_file + '.json'
    executables = []

    with open(layout_file, 'w') as f:
        # remove comments inserted by i3-save-tree
        for line in layout:
            if line.find("//") != -1:
                # only save class and instance lines, otherwise just
                # discard the line since it's unnecessary.
                if line.find('// "class":') != -1:
                    f.write(line.replace("// ", '') + "\n")
                if line.find('// "instance":') != -1:
                    f.write(line.replace("// ", '').rstrip(',') + "\n")
                    executables.extend(re.findall(r'\^(.+)\$', line))
            else:
                f.write(line + "\n")

    # create bash script to execute the programs listed in the layout
    with open(executables_file, 'w') as f:
        f.write("#!/bin/bash\n")
        for executable in executables:
            # fix certain program names that differ from their class names.
            # there is probably a better way to do this.
            if executable.find('google') != -1:
                f.write("google-chrome-stable &> /dev/null &\n")
            elif executable.find('Navigator') != -1:
                f.write("firefox &> /dev/null &\n")
            else:
                f.write(executable.lower() + " &> /dev/null &\n")
    call(['chmod', '+x', executables_file])


def save_shortcut(layout_name):
    # create a shortcut in ~/bin instead of having to type 'open layout'.
    # first check to make sure there isn't already a program with that name.
    if call(['which', layout_name], stdout=DEVNULL, stderr=STDOUT) == 1:
        with open(BIN_DIR + layout_name, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write("open " + layout_name + " $1\n")
        call(['chmod', '+x', BIN_DIR + layout_name])
    else:
        print(layout_name, 'already in path, skipping bin shortcut')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit("usage: save 'workspace' 'layout_name'")

    workspace = sys.argv[-2]
    if int(workspace) not in range(1, 11):
        exit(workspace + ' is not a valid workspace')

    layout_name = sys.argv[-1]

    layout = get_layout(workspace)
    save_layout(layout, layout_name)
    save_shortcut(layout_name)
