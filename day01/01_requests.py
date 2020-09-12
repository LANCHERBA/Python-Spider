"""
    向京东官网发起请求，并得到相应内容
"""

import requests

#1 get()获取到的为响应对象
resp = requests.get(
    url='https://www.jd.com'
)
# print(resp)

#2. text:获取响应内容 - 字符串
html = resp.text
# print(html)

#3. content:获取响应内容 - 字符串(图片，视频，音频)
html = resp.content
# print(html)

#4. status_code: 获取HTTP响应码
code = resp.status_code
# print(code)

#5. url:获取返回实际数据的url地址
url = resp.url
# print(url)