# -*- coding: utf-8 -*-
import requests
from encryption_decryption_function import str_to_bs64

"""
目标：采集100页的全部数字，并计算所有数据加和！ 本题js加密为入门难度。当做新手训练。无限debugger难度较高，可以用于无限debugger训练

"""


def debugger_summation(page: int):
    global number
    headers = {
        'authority': 'www.python-spider.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1698653592,1698737339; no-alert=true; sessionid=lbg6f27etlfi4cz30ndqd5gdtiwqbmxx; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1698742166',
        'origin': 'https://www.python-spider.com',
        'pragma': 'no-cache',
        'referer': 'https://www.python-spider.com/challenge/54',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'page': str(page),
        'token': str_to_bs64(str(page))
    }
    response = requests.post('https://www.python-spider.com/api/challenge54', headers=headers, data=data)
    data_dict = response.json()
    for data in data_dict['data']:
        number += int(data['value'])


if __name__ == '__main__':
    number = 0
    for i in range(100):
        page = i + 1
        debugger_summation(page)
    print(number)
