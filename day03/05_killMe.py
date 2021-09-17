"""
    让西刺代理封掉我!
"""
import requests
from fake_useragent import UserAgent

for pg in range(1, 101):
    url = 'https://www.xicidaili.com/nn/{}'.format(pg)
    headers = {'User-Agent':UserAgent().random}
    resp = requests.get(url=url, headers=headers)
    print(pg)






