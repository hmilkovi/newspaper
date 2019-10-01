import time
from urllib.request import ProxyHandler, build_opener, install_opener, Request, urlopen

from stem import Signal
from stem.control import Controller


class TorHandler:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
        self.current_ip = None
        self.proxy = '127.0.0.1:8118'

    def open_url(self, url):
        # communicate with TOR via a local proxy (privoxy)
        def _set_url_proxy():
            proxy_support = ProxyHandler({'http': self.proxy})
            opener = build_opener(proxy_support)
            install_opener(opener)

        _set_url_proxy()
        request = Request(url, None, self.headers)
        return urlopen(request).read().decode('utf-8')

    @staticmethod
    def renew_connection():
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='btt')
            controller.signal(Signal.NEWNYM)
            controller.close()

    def new_ip(self):
        self.current_ip = self.open_url('http://icanhazip.com/')
        print('Current IP: {}'.format(self.current_ip))

        wait_time = 1
        seconds = 0
        self.renew_connection()
        new_ip = self.current_ip
        while self.current_ip == new_ip:
            time.sleep(wait_time)
            seconds += wait_time
            new_ip = self.open_url('http://icanhazip.com/')
            if self.current_ip == new_ip:
                print('{} seconds elapsed awaiting a different IP address.'.format(seconds))
        self.current_ip = new_ip
        print('New IP: {}'.format(self.current_ip))
                

if __name__ == '__main__':
    tor = TorHandler()
    while True:
        tor.new_ip()
        time.sleep(1)