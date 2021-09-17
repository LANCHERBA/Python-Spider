"""
    开放代理 代理IP池的建立
"""
import requests
from fake_useragent import UserAgent

class OpenProxyPool:
    def __init__(self):
        self.api_url = 'http://dev.kdlapi.com/api/getproxy/?orderid=959296725299041&num=20&protocol=2&method=2&an_ha=1&sep=1'
        self.test_url = 'http://httpbin.org/get'

    def get_html(self):
        headers = { 'User-Agent':UserAgent().random }
        html = requests.get(url=self.api_url, headers=headers).text
        # proxy_list: ['ip:port','ip:port',...]
        proxy_list = html.split('\r\n')
        for proxy in proxy_list:
            # 依次对每个代理IP进行测试
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        """对每个代理IP进行测试"""
        proxies = {
            'http' : 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy),
        }
        try:
            resp = requests.get(url=self.test_url, proxies=proxies, timeout=2)
            if resp.status_code == 200:
                print(proxy, '\033[31m可用\033[0m')
            else:
                print(proxy, '不可用')
        except:
            print(proxy, '不可用')

    def run(self):
        self.get_html()

if __name__ == '__main__':
    spider = OpenProxyPool()
    spider.run()












