#!/bin/bash

# Check if venv folder already exists
if [ ! -d "venv" ]; then
    # For Linux and MacOS
    python3 -m venv venv
    source venv/bin/activate
else
    # For Windows
    python -m venv venv
    venv\Scripts\activate
fi

# Install requirements
pip install -r requirements.txt

# Run the script
cd scripts
python3 007-TheBond.py
