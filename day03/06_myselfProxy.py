"""
    使用独享代理去访问已经被封掉的西刺代理网站
"""
import requests
from fake_useragent import UserAgent

url = 'https://www.xicidaili.com/nn/1'
headers = {'User-Agent':UserAgent().random}
proxies = {
    'http' : 'http://309435365:szayclhp@115.220.1.49:16816',
    'https': 'https://309435365:szayclhp@115.220.1.49:16816'
}
html = requests.get(url=url, proxies=proxies, headers=headers).text
print(html)









