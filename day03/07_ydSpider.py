"""
    抓取有道翻译的翻译结果
    1、F12抓包,页面中翻译单词
    2、分析Form表单数据变化
    3、寻找加密的JS文件,并分析加密算法
    4、用Python实现对应的加密算法
    5、处理headers、data为字典，发请求进行数据抓取
"""
import requests
import time
import random
from hashlib import md5

class YdSpider:
    def __init__(self):
        # post_url: 一定要为F12抓包抓到的地址
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            # Cookie、Referer、User-Agent网站检查频率最高的三个字段
            '''Cookie''': '''OUTFOX_SEARCH_USER_ID_NCOO=1250534436.2162786; OUTFOX_SEARCH_USER_ID="895374202@10.108.160.18"; JSESSIONID=aaaLxQUeeSZhb_fCiCKlx; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1592971538802''',
            '''Referer''': '''http://fanyi.youdao.com/''',
            '''User-Agent''': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36''',
        }

    def get_ts_salt_sign(self, word):
        # ts salt
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        # sign
        string = "fanyideskweb" + word + salt + "mmbP%A-r6U3Nw(n]BjuEU"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    def attack_yd(self, word):
        # 获取 ts salt sign
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "07f15609aa4583527f9a1c22f48db662",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # 发送post请求
        # .json() ：把json格式的字符串转为Python数据类型
        html = requests.post(url=self.post_url, data=data, headers=self.headers).json()

        result = html['translateResult'][0][0]['tgt']

        return result

    def run(self):
        word = input('请输入要翻译的单词:')
        result = self.attack_yd(word)
        print(result)

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()



