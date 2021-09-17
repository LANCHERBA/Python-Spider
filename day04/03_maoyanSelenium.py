"""
    使用selenium+Chrome来抓取猫眼电影top100数据
"""
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 1. 打开浏览器
driver = webdriver.Chrome(options=options)

# 2. 输入URL地址
driver.get('https://book.douban.com/top250?icn=index-book250-all')

def get_one_page():
    # 3. table_list: 匹配所有图书信息的table节点对象列表
    # table_list: [<element table at xxx>, <element table at xxx>, ...]
    table_list = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div/table')
    for table in table_list:
        item = {}
        info_list = table.text.split('\n')
        # 情况1: ['杀死一只知更鸟  ', 'To Kill a Mocking Bird', '[美] 哈珀·李 / 高红梅 / 译林出版社 / 2012-9 / 32.00元', '9.2 ( 76503人评价 )', '有一种东西不能遵循从众原则，那就是——人的良心']
        # 情况2: ['笑傲江湖（全四册）', '金庸 / 生活·读书·新知三联书店 / 1994-5 / 76.80元', '9.0 ( 88170人评价 )', '欲练此功，必先自宫']
        if len(info_list) == 5:
            item['name'] = info_list[0].strip()
            item['book_info'] = info_list[2].strip()
            item['score'] = info_list[3].split('(')[0].strip()
            item['commit'] = info_list[3].split('(')[1][1:-1].strip()
            item['comment'] = info_list[4].strip()
        elif len(info_list) == 4:
            item['name'] = info_list[0].strip()
            item['book_info'] = info_list[1].strip()
            item['score'] = info_list[2].split('(')[0].strip()
            item['commit'] = info_list[2].split('(')[1][1:-1].strip()
            item['comment'] = info_list[3].strip()
        print(item)

while True:
    get_one_page()
    # 1. 查找节点时,如果找不到会抛出异常
    try:
        driver.find_element_by_link_text('后页>').click()
        # 2. 点击之后需要给页面元素加载预留时间
        time.sleep(1)
    except:
        driver.quit()
        break






















