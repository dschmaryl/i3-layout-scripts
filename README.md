# i3 Layout Save/Open

These scripts can be used to save a layout or open a saved layout in i3. To save a workspace layout, use as follows:

$ python3 save.py WORKSPACE LAYOUT

I prefer to use an alias to shorten this to just 'save [args]'. To open a saved layout, use:

$ python3 open.py LAYOUT [WORKSPACE]

If a workspace number is not specified then the layout will open in the current workspace.

To save typing, a shortcut to open a specific layout is created in a bin folder with the same name as the layout but only if nothing with that name already exists in your PATH. The easiest way to use this is to switch to a workspace, hit mod-d to open dmenu, type the name of the layout and hit enter.
