#!/bin/bash

# Install Python 3.12 if not installed
if ! command -v python3.12 &>/dev/null; then
    echo "Python 3.12 is not installed. Installing..."
    sudo apt update -y
    sudo apt install python3.12 -y
    wget https://bootstrap.pypa.io/get-pip.py
    python3.12 get-pip.py
fi

# Install Python dependencies
python3.12 -m pip install -r requirements.txt --break-system-packages

# Copy lucek.py to /usr/local/bin
sudo chmod +x lucek.py
sudo cp lucek.py /usr/local/bin/lucek
