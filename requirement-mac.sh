#!/bin/bash

# Install Python 3 if not installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Installing..."
    brew install python@3 #if not installed
    brew reinstall python@3 #if installed
    brew cleanup python@3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
fi

# Install Python dependencies
python3 -m pip install -r requirements.txt
python3 -m pip install -r requirements.txt --break-system-packages

# Copy lucek.py to /usr/local/bin
chmod +x lucek.py
cp lucek.py /usr/local/bin/lucek
