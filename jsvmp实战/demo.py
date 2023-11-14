# -*- coding: utf-8 -*-
import requests

headers = {
    'authority': 'www.python-spider.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'text/plain;charset=UTF-8',
    'cookie': 'yrx-13=A6d5nyu2jxPLaG8rrKM41Nz0MNB0LHsO1QD_gnkUwzZdaMmOgfwLXuXQj9OK; Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1699605433,1699845034,1699864141,1699943589; sessionid=6i4hy81316n89pcged3hrgcz266n38z1; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1699943601',
    'origin': 'https://www.python-spider.com',
    'pragma': 'no-cache',
    'referer': 'https://www.python-spider.com/challenge/new/jss?nm=15',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'yrx-15-jsvmp': '861871127.96b2fdce53be66bfc1bb0675520557b868c8f59cb5df9c9581ef6f7fb8633a04.1699943854648',
}

params = (
    ('yrx15', '8ebba084e45a1638b24f9fa21294a96d'),
)

data = '\u4F60\u662F\u5149\uFF0C\u4F60\u662F\u7535\uFF0C\u4F60\u662F\u552F\u4E00\u7684\u795E\u8BDD'.encode('utf-8')
response = requests.post('https://www.python-spider.com/challenge/api/user', headers=headers, params=params, data=data)

print(response.text)



