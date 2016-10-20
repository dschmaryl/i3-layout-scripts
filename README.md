These scripts can be used to save a layout or open a saved layout in i3. I prefer to create shortcuts in my bin folder to point to everything, so I use as follows:

$ save WORKSPACE LAYOUT

$ open LAYOUT [WORKSPACE]

If a workspace number is not specified then the layout will open in the current workspace. To save myself typing, a shortcut to open a specific layout is created in my bin folder with the same name as the layout but only if nothing in my PATH exists with that name. So, most of the time, I use by hitting mod+d to open dmenu and type the name of the layout I want.
