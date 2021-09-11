Example how to "cross compile" self contained tool packages with PyInstaller / cdrx/pyinstaller-linux image.

`tool.py` is the tool for which we want to create a self contained executable.
`entrypoint.py` is a wrapper script which setups environment variables suitably for the `tool.py`.

Both build scripts `build_linux.sh` and `build_windows.sh` can be executed in Linux and Windows (for example through git bash) 
to create the executables for Linux or Windows.
