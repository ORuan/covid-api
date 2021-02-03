from selenium import webdriver
import os
import sys
import time
import io
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import chromedriver_autoinstaller
from selenium.common.exceptions import NoSuchElementException


url = 'https://web.whatsapp.com/'

class AutomationWhatsApp():

    def __init__(self):
        pass

    def config(self):
        try:
            path_install = chromedriver_autoinstaller.install()

            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-extensions')
            options.add_argument(r"user-data-dir=./driver/data/46445000/")
            options.add_argument('--start-maximized')
            options.add_argument('lang=pt-br')
            options.add_argument('--disable-software-rasterizer')
            options.add_argument('disable-infobars')

            self.driver = webdriver.Chrome(
                chrome_options=options,
                executable_path=path_install
            )   
        except Exception as err:
            #commit_errors(err)
            print(err)


    def monitoring_zp(self):
        self.driver.get(url)

    def scan_qr_code(self):
        self.config()
        try:
            self.driver.get(url)
        except NoSuchElementException:
            time.sleep(3)
            self.driver.get(url)
        except Exception as err:
            print(err)
            #commit_errors(err)