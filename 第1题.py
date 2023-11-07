# -*- coding: utf-8 -*-
import base64
import hashlib
import time
import requests
from encryption_decryption_function import str_to_bs64, str_to_md5

"""
目标：采集100页的全部数字，并计算所有数据加和。就从这里开启你的逆向之旅吧！
"""


def summation(page: int):
    global number
    t = str(round(time.time()))
    headers = {
        'authority': 'www.python-spider.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.python-spider.com',
        'pragma': 'no-cache',
        'referer': 'https://www.python-spider.com/challenge/1',
        'safe': str_to_md5(str_to_bs64('9622' + t)),
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'timestamp': str(t),
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'page': str(page)
    }
    response = requests.post('https://www.python-spider.com/api/challenge1', headers=headers, data=data)
    data_dict = response.json()
    data_list = data_dict['data']
    for data in data_list:
        number += int(data['value'])


if __name__ == '__main__':
    number = 0
    for i in range(100):
        page = i + 1
        summation(page)
    print(number)
