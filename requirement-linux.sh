#!/bin/bash

# Install Python dependencies
python3.11 -m pip install -r requirements.txt --break-system-packages

# Copy lucek.py to /usr/local/bin
sudo chmod +x lucek.py
sudo cp lucek.py /usr/local/bin/lucek
