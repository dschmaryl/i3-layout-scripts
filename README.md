# i3 Layout Save/Open

These scripts can be used to save a layout or open a saved layout in i3. Note: the perl-anyevent-i3 package needs to be installed.

To save a workspace layout, use as follows:

    python3 save.py [WORKSPACE_NUMBER] LAYOUT_NAME

If a workspace_number is not specified, the current workspace is saved. I prefer to use a shell script to shorten this to 'save [args]'. An alias can be used, however it will not be available in dmenu since dmenu does not normally support shell aliases. My shortcut, which is named 'save' and sits in my home/bin folder, looks like:

    python3 /path/to/i3-layout-scripts/save.py $1 $2

To open a saved layout, use:

    python3 open.py LAYOUT_NAME [WORKSPACE_NUMBER]

When a layout is saved, and if nothing else with the same name as the layout exists in your PATH, then a shortcut to open that layout is created to save some typing. These shortcuts are put in '~/.i3-layouts/bin' by default, so this folder needs to be added to your PATH. The easiest way to open a layout is to switch to the workspace where you want the layout to open and then enter the layout name in dmenu or whatever launcher you prefer.
