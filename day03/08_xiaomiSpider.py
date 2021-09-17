"""
    Ajax动态加载数据抓取 - 小米应用商店聊天社交分类下的应用信息
    1、右键 - 查看网页源代码 - 确认为动态加载
    2、F12抓包,页面执行点击行为
    3、XHR中查找返回实际数据的网络数据包 - Preview
    4、多次点击下一页,分析查询参数的变化 - QueryString Paramters
"""
import requests
import json
import time
import random
from fake_useragent import UserAgent

class XiaomiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'

    def get_html(self, url):
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        # json.loads() : 把json格式的字符串转为python数据类型
        html = json.loads(html)
        # 开始数据解析提取
        self.parse_html(html)

    def parse_html(self, html):
        """数据解析提取"""
        for one_app_dict in html['data']:
            item = {}
            item['name'] = one_app_dict['displayName']
            item['type'] = one_app_dict['level1CategoryName']
            item['link'] = one_app_dict['packageName']
            print(item)

    def run(self):
        # 获取总页数
        total = self.get_total()
        for i in range(total):
            page_url = self.url.format(i)
            self.get_html(url=page_url)
            # 控制数据抓取的频率
            time.sleep(random.randint(1,3))

    def get_total(self):
        total_url = 'http://app.mi.com/categotyAllListApi?page=0&categoryId=2&pageSize=30'
        html = requests.get(url=total_url, headers={'User-Agent':UserAgent().random}).json()
        count = html['count']
        total = count // 30 if count % 30 == 0 else count // 30 + 1

        return total

if __name__ == '__main__':
    spider = XiaomiSpider()
    spider.run()













