"""
    向测试网站发请求，获取响应内容来确认User-Agent到底是什么
"""

import requests

# 常用变量定义
url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}
html = requests.get(
    url=url,
    headers=headers
).text
print(html)
