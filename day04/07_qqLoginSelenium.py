"""
    使用selenium模拟登录QQ邮箱
"""
from selenium import webdriver

# 1. 打开浏览器并进入登录页
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

# 2. 切换到iframe子页面: 因为selenium默认支持id 或者 name 两个属性值的切换
driver.switch_to.frame('login_frame')

# 3. 用户名 + 密码 + 登录按钮
driver.find_element_by_id('u').send_keys('2621470058')
driver.find_element_by_id('p').send_keys('zhanshen001')
driver.find_element_by_id('login_button').click()







