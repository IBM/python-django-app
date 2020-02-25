#!/usr/bin/env bash

echo "Installing Chrome web driver..."
source <(curl -sSL "${DEVX_SKIT_ASSETS_GIT_URL_RAW:-https://raw.githubusercontent.com/IBM/devex-skit-assets/master}/scripts/install_chrome.sh")

echo "Starting Chrome web driver..."
source <(curl -sSL "${DEVX_SKIT_ASSETS_GIT_URL_RAW:-https://raw.githubusercontent.com/IBM/devex-skit-assets/master}/scripts/start_chrome.sh")

echo "Downloading and installing pip..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip -V

echo "Installing Selenium Python package..."
pip install selenium

echo "Running UI test using Selenium..."
python3 python_django.py
