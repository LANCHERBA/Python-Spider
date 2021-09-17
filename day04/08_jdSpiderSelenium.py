"""
    使用selenium抓取京东商城 爬虫书 商品的数据
    所抓数据:
        1. 产品名称
        2. 产品价格
        3. 评价数量
        4. 产品商家
    知识点:
        1. 浏览器对象driver执行JS脚本,execute_script('')
"""
from selenium import webdriver
import time
import pymongo

class JdSpider:
    def __init__(self):
        # 设置无界面
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.url = 'https://www.jd.com/'
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.get(url=self.url)
        # 创建mongodb相关变量
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['jddb']
        self.myset = self.db['jdset']

    def get_html(self):
        """找到搜索框,发送搜索关键字,点击搜索,进入到商品页"""
        self.driver.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
        self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        # 点击搜索之后预留加载时间
        time.sleep(1)

    def parse_html(self):
        """解析提取1页的完整数据"""
        # 执行JS脚本,让所有商品数据完全加载出来之后再抓取
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        # 给页面加载预留时间
        time.sleep(3)
        li_list = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            item = {}
            try:
                item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text
                item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]/strong').text
                item['commit'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text
                item['shop'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]/a').text
                print(item)
                # 存入mongodb数据库
                self.myset.insert_one(item)
            except:
                pass

    def run(self):
        self.get_html()
        while True:
            self.parse_html()
            # 没有找到,返回 -1 ,没有找到说明不是最后一页
            if self.driver.page_source.find('pn-next disabled') == -1:
                self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
                time.sleep(1)
            else:
                self.driver.quit()
                break

if __name__ == '__main__':
    spider = JdSpider()
    spider.run()




















