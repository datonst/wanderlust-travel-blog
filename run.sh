#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Wanderlust Travel Blog - Setup Script"
echo "===================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Download images
echo "Downloading placeholder images..."
python download_images.py

# Run the application
echo "Starting the Flask application..."
echo "Access the website at http://localhost:5000"
python main.py 