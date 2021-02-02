from http.server import BaseHTTPRequestHandler, HTTPServer
from bs4 import BeautifulSoup
from utils import commit_errors
import urllib.request
import time
import sched
import random
from itertools import cycle

URL = "https://twitter.com/explore/tabs/trending/"
PROXY_URL = 'https://free-proxy-list.net/'
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
        self.header = HEADER
    def get_proxy(self):

        req = urllib.request.Request(PROXY_URL)
        req.add_header('User-Agent', self.header['User-Agent'])

        try:
            with urllib.request.urlopen(req) as response:
                soup = BeautifulSoup(response.read(), 'lxml')
                table = soup.find('table',id='proxylisttable')
                list_tr = table.find_all('tr')
                list_td = [elem.find_all('td') for elem in list_tr]
                list_td = list(filter(None, list_td))
                list_ip = [elem[0].text for elem in list_td]
                list_ports = [elem[1].text for elem in list_td]
                list_proxies = [':'.join(elem) for elem in list(zip(list_ip, list_ports))]
                print('o tipo do dado é', type(list_proxies))
                self.proxy_list = list_proxies
        except Exception as err:
            commit_errors(err, __file__)
        proxy_support = urllib.request.ProxyHandler(self.proxy_list)
        urllib.request.install_opener(proxy_support)


    def _get(self):
        try:
            proxy = cycle(self.get_proxy())
            req = urllib.request.Request(self.url)
            req.add_header('User-Agent',  self.header['User-Agent'])
            with urllib.request.urlopen(req) as response:
                self.raw = response.read()
        except Exception as err:
            commit_errors(err, __file__)

    def process(self):
        self._get()
        try:
            data = BeautifulSoup(self.raw, 'html.parser')  # .prettify()
            # print(data.select("div.css-1dbjc4n.r-bnwqim.r-16y2uox"))
            #
            # print('second -- ', data.select("span.css-901oao"))
            print(data)
        except Exception as err:
            commit_errors(err, __file__)

    def monitoring_daemon(self):
        s = sched.scheduler(time.time, time.sleep)
        while True:
            s.enter(3, 1, self.process)
            s.run()

    