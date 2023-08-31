# Inbuilt Python modules
import os
import time
import requests
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# Imports required for Selenium Chromedriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as poel

queries = [
    
]
# max times it will click more results
pages = 5
# can be out of "d", "w", "m", "y", ""
recency = "m" 
# Domains to avoid
avoid = [
    "amazon",
    "wikipedia",
    "imdb",
    "duckduckgo",
    "youtube",
    "google"
]

# beta
f_link = [

]
f_title = [
    "sustainable"
]



