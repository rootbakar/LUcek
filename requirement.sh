```bash
#!/bin/bash

# Install Python 3 if not installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Installing..."
    sudo apt install python3 -y
fi

# Install Python dependencies
pip install -r requirements.txt
