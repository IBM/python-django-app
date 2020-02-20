#!/usr/bin/env bash

# Run Chrome Headless
start-chrome-headless() {
    chromedriver --url-base=/wd/hub
}

# Start
nohup start-chrome-headless &>/dev/null &
