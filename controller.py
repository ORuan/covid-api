from http.server import BaseHTTPRequestHandler, HTTPServer
from bs4 import BeautifulSoup
from utils import commit_errors
import urllib.request as req
import time
import sched
import random
from lxml import html


city = "guanambi"
URL = f"http://www.{city}.ba.gov.br/coronavirus#conteudo"

HEADERS_LIST = [
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
            'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
            'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
            'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
        ]
HEADER = {'User-Agent': random.choice(HEADERS_LIST), 'X-Requested-With': 'XMLHttpRequest'}

class Monitor():
    def __init__(self):
        self.url = URL
        self.header = HEADER['User-Agent']

    def _get(self):
        try:
            _req = req.Request(self.url)
            _req.add_header('User-Agent',  self.header)
            with req.urlopen(_req) as response:
                self.raw = response.read()
        except Exception as err:
            commit_errors(err, __file__)

    def process(self):
        self._get()
        
        data_message = list()
        
        try:
            data = BeautifulSoup(self.raw, 'lxml') 

            s3_text = data.select('#container_noticias > div.bloco_covid > div.painel > ul > li > h3')
            s4_text = data.select('#container_noticias > div.bloco_covid > div.painel > ul > li > h4')
        except Exception as err:
            commit_errors(err, __file__)
        try:
            for i in range(len(s3_text)):
                data_message.insert(i, f'{s4_text[i].text}: {s3_text[i].text}\n')
            
            with open('./message.txt', 'w') as msg:
                msg.writelines(data_message)        
            
        except Exception as err:
            print(err)
                

    def monitoring_daemon(self):
        s = sched.scheduler(time.time, time.sleep)
        while True:
            s.enter(3, 1, self.process)
            s.run()

    