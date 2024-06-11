#!/bin/bash

# Install Python 3 if not installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Installing..."
    sudo apt update -y
    sudo apt install python3 -y
    sudo apt install python3-pip
fi

# Install Python dependencies
python3 -m pip install -r requirements.txt --break-system-packages

# Copy lucek.py to /usr/local/bin
sudo chmod +x lucek.py
sudo cp lucek.py /usr/local/bin/lucek
