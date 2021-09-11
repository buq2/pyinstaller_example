# PyInstaller Example

Example how to "cross compile" self contained tool packages with PyInstaller / cdrx/pyinstaller-linux image.

`tool.py` is the tool for which we want to create a self contained executable.
`entrypoint.py` is a wrapper script which setups environment variables suitably for the `tool.py`.

Both build scripts `build_linux.sh` and `build_windows.sh` can be executed in Linux and Windows (for example through git bash) 
to create the executables for Linux or Windows.


# To build Linux binaries in a Docker without cdrx/* images
```
docker build -t pyinstaller_example .

# Start named container
docker run --name pyinst_ex pyinstaller_example

# Copy executable from the image to workspace
docker cp pyinst_ex:dist/tool .

# Kill the container
docker rm pyinst_ex
```
