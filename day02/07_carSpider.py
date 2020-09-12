"""
汽车之家二级页面数据抓取案例
思路：
    1. 一级页面提取数据：汽车详情页链接
    2. 二级页面提取数据：具体汽车的数据

"""

import requests
import re
import time
import random


class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
        }
        self.one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)"'
        self.two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b>'

    def get_html(self, url):
        """功能函数1 - 获取html"""
        #加入程序抛出异常：网站会加入没办法解析的数据来反爬。
        html = requests.get(url=url, headers=self.headers).content.decode('gb2312','ignore')
        return html

    def re_html(self, regex, html):
        """功能函数2 - 正则解析解析"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        return r_list

    def parse_html(self, one_url):
        """程序逻辑函数"""
        one_html = self.get_html(one_url)
        # href_list : ['/declear/xxx','','','',...]
        href_list = self.re_html(regex=self.one_regex, html=one_html)
        for href in href_list:
            two_url = 'https://www.che168.com' + href
            # 提取一辆汽车的具体信息
            self.get_carinfo(two_url)
            # 控制抓取频率，没抓取一辆汽车随机休眠0-1秒钟
            time.sleep(random.uniform(0, 1))

    def get_carinfo(self, two_url):
        """提取一辆汽车的具体信息"""
        two_html = self.get_html(url=two_url)
        # car_info_list : [('奔驰'，'2万公里','2000年','自动/1.6','20.52'),]
        car_info_list = self.re_html(self.two_regex, two_html)
        item = {}
        item['name'] = car_info_list[0][0].strip()
        item['km'] = car_info_list[0][1].strip()
        item['time'] = car_info_list[0][2].strip()
        item['type'] = car_info_list[0][3].split('/')[0].strip()
        item['displacement'] = car_info_list[0][3].split('/')[1].strip()
        item['price'] = car_info_list[0][4].strip()
        print(item)

    def run(self):
        for o in range(1, 3):
            page_url = self.url.format(o)
            self.parse_html(page_url)

if __name__ == '__main__':
    spider = CarSpider()
    spider.run()



# 一级页面正则表达式
"""
<li class="cards-li list-photo-li".*?<a href="(.*?)"         
"""

# 二级页面正则表达式
"""
<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b>
"""
