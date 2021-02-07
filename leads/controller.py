from http.server import BaseHTTPRequestHandler, HTTPServer
from bs4 import BeautifulSoup
import urllib.request as req
import time
import sched
import random
from lxml import html
from pymemcache.client import base
import urllib
import schedule
from whatsapp.seln import AutomationWhatsApp
from leads.models import Leads
import threading
import logging
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.ERROR)


HEADERS_LIST = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
]
HEADER = {
    'User-Agent': random.choice(HEADERS_LIST), 'X-Requested-With': 'XMLHttpRequest'}


class Monitor():
    def __init__(self):
        self.header = HEADER['User-Agent']
        self.cities = None

    def get_leads(self):
        _cities = list()
        _numbers = list()

        try:
            _leads = Leads.objects.all().order_by('city').values_list().distinct()
            for i in range(len(_leads)):
                _cities.append(_leads[i][2])
                _numbers.append(_leads[i][1])

            self.cities = sorted(set(_cities))
            return _numbers
        except Exception as err:
            logging.error(err)
            print(err)

    def process(self):
        _numbers = self.get_leads()
        try:
            for city in self.cities:
                data_message = list()
                _req = req.Request(
                    f"http://www.{city}.ba.gov.br/coronavirus#conteudo")
                with req.urlopen(_req) as response:
                    self.data = response.read()

                _data = BeautifulSoup(self.data, 'lxml')
                s3_text = _data.select(
                    '#container_noticias > div.bloco_covid > div.painel > ul > li > h3')
                s4_text = _data.select(
                    '#container_noticias > div.bloco_covid > div.painel > ul > li > h4')

                for i in range(len(s3_text)):
                    data_message.insert(
                        i, f'{s4_text[i].text}: {s3_text[i].text}\n')

                with open(f'./messages/{city}.txt', 'w') as msg:
                    msg.writelines('------\n')
                    msg.writelines(data_message)

            th_sender = AutomationWhatsApp(citys=self.cities, number=_numbers)
            threading.Thread(target=th_sender.send_status, daemon=True).start()
        except Exception as err:
            logging.error(err)
            print(err)

    def monitoring_daemon(self):
        schedule.every().day.at("09:10").do(self.process)
        while True:
            schedule.run_pending()
            time.sleep(0.1)
