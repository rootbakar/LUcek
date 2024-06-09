#!/bin/bash

# Install Python 3.8 if not installed
if ! command -v python3.8 &>/dev/null; then
    echo "Python 3.8 is not installed. Installing..."
    sudo apt update -y
    sudo apt install python3.8 -y
    wget https://bootstrap.pypa.io/get-pip.py
    python3.8 get-pip.py
fi

# Install Python dependencies
pip3.8 install -r requirements.txt

# Copy lucek.py to /usr/local/bin
sudo chmod +x lucek.py
sudo cp lucek.py /usr/local/bin/lucek
