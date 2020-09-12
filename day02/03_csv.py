"""
    csv模块实例
"""

import csv

with open('test.csv', 'w') as f:
    # 初始化csv文件的写入对象
    writer = csv.writer(f)
    writer.writerow(['月光宝盒', '周星驰', '1993-01-01'])
