"""
    猫眼电影top100数据抓取 - 存入MYSQL数据库

数据原格式：
<div class="movie-item-info">
        <p class="name"><a href="/films/2049" title="十二怒汉" data-act="boarditem-click" data-val="{movieId:2049}">十二怒汉</a></p>
        <p class="star">
                主演：亨利·方达,李·科布,马丁·鲍尔萨姆
        </p>
<p class="releasetime">上映时间：1957-04-13(美国)</p>    </div>
"""

import requests
import re
import time
import random
import pymysql


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
        self.regex_top100 = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        # 数据库连接对象 + 游标对象
        self.db = pymysql.connect('localhost', 'root', '123456', 'mydb', charset='utf8')
        self.cur = self.db.cursor()

    def get_html(self, url):
        """获取响应内容"""
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据函数"""
        pattern = re.compile(self.regex_top100, re.S)
        r_list = pattern.findall(html)
        # r_list: [(),(),...,()]
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """具体数据处理的函数"""
        # r_list:[().(),..,()]
        ins = 'insert into mytab values(%s,%s,%s)'
        for r in r_list:
            li = [
                r[0].strip(),
                r[1].strip(),
                r[2].strip()
            ]
            self.cur.execute(ins, li)
        # 千万别忘提交到数据库实行
        self.db.commit()

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(page_url)
            # 控制数据抓取的频率 uniform 生成指定范围内的浮点数
            time.sleep(random.uniform(0, 2))

        # 关闭mysql连接对象和游标对象
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    new_MaoyanSpider = MaoyanSpider()
    new_MaoyanSpider.run()
