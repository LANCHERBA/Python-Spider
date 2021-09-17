"""
    selenium切换句柄
"""
from selenium import webdriver
import time

class MzbSpider:
    def __init__(self):
        # 设置无界面
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url=self.url)

    def get_html(self):
        self.driver.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[2]/td[2]/a').click()
        time.sleep(1)
        # 获取并切换句柄
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[1])
        # 解析提取数据
        self.parse_html()

    def parse_html(self):
        """解析提取数据"""
        tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            item = {}
            info_list = tr.text.split()
            item['name'] = info_list[1].strip()
            item['code'] = info_list[0].strip()
            print(item)

    def run(self):
        self.get_html()
        # 关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()














