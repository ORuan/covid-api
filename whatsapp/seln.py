from selenium import webdriver
import os
import sys
import time
import io
import json
import chromedriver_autoinstaller as installator
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutomationWhatsApp():

    def __init__(self, leads, number):
        self.url = 'https://web.whatsapp.com/send?phone='
        self.leads = leads
        self.number = number

    def config(self):
        try:
            path_install = installator.install()
            options = webdriver.ChromeOptions()
            prefs = {'profile.managed_default_content_settings.images': 2,
                     "profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
            options.add_experimental_option("prefs", prefs)
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
            print(err)

    def send_status(self):

        try:
            if self.driver:
                pass
        except Exception as err:
            self.config()

        try:
            for lead in range(len(self.leads)):
                time.sleep(2)
                try:
                    with open(f'./messages/{self.leads[lead]}.txt', 'r') as file:
                        content = file.readlines()
                        self.content = content
                except Exception as err:
                    print(err)

                self.driver.get(self.url+self.number[lead])

                wait = WebDriverWait(self.driver, 60)

                inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
                input_box = wait.until(
                    EC.presence_of_element_located((By.XPATH, inp_xpath)))

                for msg in self.content:
                    input_box.send_keys(msg + Keys.ENTER)

        except Exception as err:
            print(err)
            self.driver.quit()

    def scan_qr_code(self):
        self.config()
        try:
            self.driver.get(url)
        except NoSuchElementException:
            time.sleep(3)
            self.driver.get(url)
        except Exception as err:
            print(err)
