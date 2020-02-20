import os, time, sys, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Do an action on the app's landing page
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.get(os.environ["APP_URL"]); # Open a browser to the app's landing page
time.sleep(3)
# Verify the expected content is present
title_text = driver.find_element_by_css_selector('h1.title').text
print("The title text is: {}".format(title_text))
if title_text == "Congratulations!":
    print("Experience Test Successful")
else:
    sys.exit("Experience Test Failed")

subtitle_text = driver.find_element_by_css_selector('h2.subtitle').text
print("The subtitle text is: {}".format(subtitle_text))
if subtitle_text == "You are currently running a Django server.":
    print("Experience Test Successful")
else:
    sys.exit("Experience Test Failed")
