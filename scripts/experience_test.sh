#!/usr/bin/env bash

echo "Installing Chrome web driver..."
./install_chrome.sh

echo "Starting Chrome web driver..."
./start_chrome.sh

echo "Downloading and installing pip..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip -V

echo "Installing Selenium Python package..."
pip install selenium

echo "Running UI test using Selenium..."
python3 python_django.py
