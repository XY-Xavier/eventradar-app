#!/bin/bash
# Quick start script for EventRadar

cd "$(dirname "$0")"

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Run ./setup.sh first to set up the project."
    exit 1
fi

# Activate venv and run
echo "🎯 Starting EventRadar..."
source venv/bin/activate
python app.py
