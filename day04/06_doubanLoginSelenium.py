"""
    使用selenium模拟登录豆瓣网站
"""
from selenium import webdriver

# 1. 打开浏览器,输入地址到登录页
driver = webdriver.Chrome()
driver.get('https://www.douban.com/')
driver.maximize_window()

# 2. 先切换iframe
frame_node = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_to.frame(frame_node)

# 3. 密码登录、用户名、密码、登录按钮
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element_by_name('username').send_keys('15110225726')
driver.find_element_by_name('password').send_keys('zhanshen001')
# 注意：查找节点时,如果属性值中包含空格,则必须使用 . 来代替,否则会无法找到该节点
driver.find_element_by_class_name('btn.btn-account').click()

















