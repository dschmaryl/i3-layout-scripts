# i3 Layout Save/Open

These scripts can be used to save layouts and open saved layouts in i3. For each layout, a bash script to launch the applications associated with layout is also created. Also included are 'list' and 'remove' scripts to manage saved layouts.

To install:

    git clone https://github.com/dschmaryl/i3-layout-scripts
    cd i3-layout-scripts

Edit 'config.py' if you would like to change the default directories in which layouts and program launchers will be saved. Then run:

    python3 install.py

To save a workspace layout, use as follows:

    python3 save.py [WORKSPACE_NUMBER] LAYOUT_NAME

If a workspace_number is not specified, the current workspace is saved. I prefer to use a shell script to shorten this to 'save [args]'. An alias can be used, however it will not be available in dmenu since dmenu does not normally support shell aliases. My shortcut, which is named 'save' and sits in my home/bin folder, looks like:

    python3 /path/to/i3-layout-scripts/save.py $1 $2

To open a saved layout, use:

    python3 open.py LAYOUT_NAME [WORKSPACE_NUMBER]

When a layout is saved, and if nothing else with the same name as the layout exists in your PATH, a shortcut to open that layout is created to save some typing. These shortcuts are put in '~/.i3-layouts/bin' by default, so this folder needs to be added to your PATH. The easiest way to open a saved layout is to switch to the workspace in which you want the layout to open and then enter the name of the layout in dmenu or whatever launcher you prefer.
