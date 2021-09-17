"""
    免费代理IP使用
"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0'}
proxies = {
    'http' : 'http://183.166.252.187:4216',
    'https': 'https://183.166.252.187:4216',
}
# 测试
html = requests.get(url=url, proxies=proxies, headers=headers).text
print(html)








