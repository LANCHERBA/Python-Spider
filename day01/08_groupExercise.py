"""
    正则表达式分组练习
"""

import re

html = """
<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>
    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>
<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>
    <p class="content">
        Small white rabbit white and white
    </p>
</div>
"""

regex = '<div class="animal">.*?<a title="(.*?)".*?<p class="content">(.*?)</p>'

pattern = re.compile(regex, re.S)
r_list = pattern.findall(html)
# 第一步实现
print(r_list)
# 第二步实现
for r in r_list:
    print('动物名称： ', r[0].strip())
    print('动物信息： ', r[1].strip())
    print('*'*50)
