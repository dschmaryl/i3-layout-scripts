# i3 Layout Save/Open

These scripts can be used to save a layout or open a saved layout in i3. To save a workspace layout, use as follows:

$ python3 save.py WORKSPACE LAYOUT

I prefer to use an alias to shorten this to just 'save [args]'. To open a saved layout, use:

$ python3 open.py LAYOUT [WORKSPACE]

If a workspace number is not specified then the layout will open in the current workspace. To save typing, a shortcut to open a specific layout is created in a bin folder with the same name as the layout but only if nothing with that name already exists in your PATH. So, most of the time, I use by switching to the workspace I want, hitting mod+d to open dmenu, typing the name of the layout and hitting enter.
