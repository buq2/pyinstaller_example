#!/bin/bash
docker run -v "$(pwd -W):/src/" cdrx/pyinstaller-windows "mkdir build; cd build; wine /wine/drive_c/Python37/Scripts/pyinstaller.exe --onefile ../entrypoint.py --name tool --add-data '../weird-external-file.txt;.'"
