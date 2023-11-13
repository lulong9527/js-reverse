# -*- coding: utf-8 -*-
import requests

headers = {
    'authority': 'www.python-spider.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'yrx-13=AyH_CeGU4V0hqikdNkEGamb2MOY-zpXAv0I51IP2HSiH6k8Yyx6lkE-SSaUQ;; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1699583477,1699605433,1699845034; sessionid=jtu7jxrunsq4cq2vywx81y5mmgofa4vd; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1699845055',
    'origin': 'https://www.python-spider.com',
    'pragma': 'no-cache',
    'referer': 'https://www.python-spider.com/challenge/new/jss?nm=13',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = (
    ('nm', '13'),
)

data = {
  'as': 'Window'
}

response = requests.post('https://www.python-spider.com/challenge/new/check', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.python-spider.com/challenge/new/check?nm=13', headers=headers, data=data)

print(response.text)