#!/bin/bash

# Install Python 3.8 if not installed
if ! command -v python3.8 &>/dev/null; then
    echo "Python 3.8 is not installed. Installing..."
    brew install python@3.8 #if not installed
    brew reinstall python@3.8 #if installed
    brew cleanup python@3.8
    wget https://bootstrap.pypa.io/get-pip.py
    python3.8 get-pip.py
fi

# Install Python dependencies
pip3.8 install -r requirements.txt

# Copy lucek.py to /usr/local/bin
chmod +x lucek.py
cp lucek.py /usr/local/bin/lucek
