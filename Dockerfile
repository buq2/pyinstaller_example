FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# Binutils is needed by pyinstaller as it uses objdump
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv python3-dev binutils && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install -r requirements.txt && \
    pyinstaller --onefile entrypoint.py --name tool --add-data 'weird-external-file.txt:.'
