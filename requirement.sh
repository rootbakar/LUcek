#!/bin/bash

# Install Python 3.8 if not installed
if ! command -v python3.8 &>/dev/null; then
    echo "Python 3.8 is not installed. Installing..."
    sudo apt install python3.8 -y
fi

# Install Python dependencies
pip install -r requirements.txt
