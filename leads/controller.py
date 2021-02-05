from http.server import BaseHTTPRequestHandler, HTTPServer
from bs4 import BeautifulSoup
import urllib.request as req
import time
import sched
import random
from lxml import html


HEADERS_LIST = [
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
            'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
            'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
            'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
        ]
HEADER = {'User-Agent': random.choice(HEADERS_LIST), 'X-Requested-With': 'XMLHttpRequest'}

class Monitor():
    def __init__(self, cities):
        self.header = HEADER['User-Agent']


    def process(self):
        data_message = list()
        try:
            for city in self.cities:
                print(city)
                _req = req.Request(f"http://www.{city}.ba.gov.br/coronavirus#conteudo")
                with req.urlopen(_req) as response:
                    self.data = response.read()

                _data = BeautifulSoup(self.data, 'lxml') 
                s3_text = _data.select('#container_noticias > div.bloco_covid > div.painel > ul > li > h3')
                s4_text = _data.select('#container_noticias > div.bloco_covid > div.painel > ul > li > h4')
            
                for i in range(len(s3_text)):
                    data_message.insert(i, f'{s4_text[i].text}: {s3_text[i].text}\n')
                
                with open(f'./messages/{city}.txt', 'w') as msg:
                    msg.writelines(data_message)        
            
        except Exception as err:
            print(err)


    def monitoring_daemon(self, cities):
        list_cities = list(cities)
        self.cities = list()
        
        for i in range(len(list_cities)):
            self.cities.append(list_cities[i][2]) 

        s = sched.scheduler(time.time, time.sleep)
        while True: 
            s.enter(5, 1, self.process)
            s.run()