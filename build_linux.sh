#!/bin/bash
docker run -v "$(pwd -W):/src/" cdrx/pyinstaller-linux "mkdir build; cd build; pyinstaller --onefile ../entrypoint.py --name tool --add-data '../weird-external-file.txt:.'"
