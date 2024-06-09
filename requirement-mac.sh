#!/bin/bash

# Install Python 3.12 if not installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3.12 is not installed. Installing..."
    brew install python@3.12 #if not installed
    brew reinstall python@3.12 #if installed
    brew cleanup python@3.12
    wget https://bootstrap.pypa.io/get-pip.py
    python3.12 get-pip.py
fi

# Install Python dependencies
python3.12 -m pip install -r requirements.txt --break-system-packages

# Copy lucek.py to /usr/local/bin
chmod +x lucek.py
cp lucek.py /usr/local/bin/lucek
