# -*- coding: utf-8 -*-
import requests
import re
import execjs

cookies = {
    'sessionid': 'ej59kzqq45net4nepy8noj9t39jgjkb8'
}
session = requests.session()

url = 'https://www.python-spider.com/challenge/11'
response = session.get(url, cookies=cookies)
js_code = re.match('<script>(.*?)</script>', response.text).group(1)
with open('第11题.js', 'r', encoding='utf-8') as f:
    # 进行替换的时候，可以讲 第11题.js 中 __jscode 以上的代码删除（除了补充的环境）---> 补充的环境+替换的代码直接输出即可/ 直接用扣下来的+补环境 直接运行也可以
    __jsl_clearance = execjs.compile(f.read().replace('__jscode', js_code)).call('decode')
cookies['__jsl_clearance'] = __jsl_clearance.split('=')[1].split(';')[0]
url = 'https://www.python-spider.com/challenge/11'
response = session.get(url, cookies=cookies)
print(response.text)
