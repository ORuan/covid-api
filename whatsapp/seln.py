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
import logging
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from core.settings import DEBUG, DOMAIN, BASE_DIR
from selenium.common.exceptions import WebDriverException
class AutomationWhatsApp():

    def __init__(self, citys, number):
        self.url = 'https://web.whatsapp.com/send?phone='
        self.citys = citys
        self.number = number

    def config(self):
        try:
            path_install = installator.install()
            options = webdriver.ChromeOptions()
            prefs = {'profile.managed_default_content_settings.images': 2,
                     "profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
            options.add_experimental_option("prefs", prefs)
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
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
            logging.error(err)
            print(err)

    def send_status(self):

        try:
            if self.driver:
                pass
        except Exception as err:
            logging.info('Installing webdriver')
            self.config()

        for _number_u in range(len(self.number)):
            time.sleep(1)
            try:
                with open(f'./messages/{self.citys[_number_u]}.txt', 'r') as file:
                    content = file.readlines()
                    self.content = content
                self.driver.get(self.url+self.number[_number_u])
                wait = WebDriverWait(self.driver, 10)
                inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
                input_box = wait.until(
                    EC.presence_of_element_located((By.XPATH, inp_xpath)))
                for msg in self.content:
                    input_box.send_keys(msg + Keys.ENTER)
                self.driver.quit()
            except UnexpectedAlertPresentException:
                print('err')
                logging.error(err)
                continue
            except WebDriverException as err:
                os.system(f'rm {BASE_DIR}/static/qr_code.png')
                time.sleep(5)
                self.driver.save_screenshot(f'{BASE_DIR}/static/qr_code.png')     
                if DEBUG == True:
                    print('http://localhost:8000/8ade7b25-d7c9-400c-8ea6-e1c8413d01af/')
                else:
                    print('http://'+DOMAIN+'/8ade7b25-d7c9-400c-8ea6-e1c8413d01af/')
                #Develoment
                # Handle render qr_code_View     
                time.sleep(5)     
                self.driver.quit()
                print(err.screen, file=sys.stderr)
            except Exception as err:
                self.driver.quit()
                logging.error(err)