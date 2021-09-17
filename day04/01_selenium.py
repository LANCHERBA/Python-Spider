# 导入selenium的webdriver接口
from selenium import webdriver

# 1. 打开Chrome浏览器
driver = webdriver.Chrome()
# 2. 在浏览器地址栏输入百度的URL地址,并确认
driver.get('http://www.baidu.com/')
# 3. 浏览器窗口最大化
driver.maximize_window()
# 4. 获取屏幕快照
driver.save_screenshot('baidu.png')
# 5. find()方法 : 没有找到,返回 -1 ,经常用于判断是否为最后一页
print(driver.page_source.find('aaaaaaaaaaaaaaa'))
# 6. 关闭浏览器
driver.quit()










