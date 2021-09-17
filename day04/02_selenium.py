from selenium import webdriver

# 1. 打开Chrome浏览器
driver = webdriver.Chrome()
# 2. 输入百度URL地址,进入百度首页
driver.get('http://www.baidu.com/')
# 3. 找到搜索框节点,并发送文本 - 赵丽颖
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')
# 4. 找到百度一下按钮,并进行模拟点击
driver.find_element_by_xpath('//*[@id="su"]').click()













