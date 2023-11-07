import requests
import requests

cookies = {
    'HMACCOUNT_BFESS': '187D04FA3E11E62A',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.python-spider.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = (
    ('hca', '187D04FA3E11E62A'),
    ('cc', '1'),
    ('ck', '1'),
    ('cl', '30-bit'),
    ('ds', '1512x982'),
    ('vl', '324'),
    ('ep', '142424,72616'),
    ('et', '3'),
    ('ja', '0'),
    ('ln', 'zh-cn'),
    ('lo', '0'),
    ('lt', '1699339272'),
    ('rnd', '635042415'),
    ('si', '337e99a01a907a08d00bed4a1a52e35d'),
    ('su', 'https://www.python-spider.com/challenge/3'),
    ('v', '1.3.0'),
    ('lv', '2'),
    ('sn', '22090'),
    ('r', '0'),
    ('ww', '1512'),
    ('u', 'https://www.python-spider.com/challenge/3'),
)

response = requests.get('https://hm.baidu.com/hm.gif', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://hm.baidu.com/hm.gif?hca=187D04FA3E11E62A&cc=1&ck=1&cl=30-bit&ds=1512x982&vl=324&ep=142424%2C72616&et=3&ja=0&ln=zh-cn&lo=0&lt=1699339272&rnd=635042415&si=337e99a01a907a08d00bed4a1a52e35d&su=https%3A%2F%2Fwww.python-spider.com%2Fchallenge%2F3&v=1.3.0&lv=2&sn=22090&r=0&ww=1512&u=https%3A%2F%2Fwww.python-spider.com%2Fchallenge%2F3', headers=headers, cookies=cookies)

print(response.text)



import requests

cookies = {
    'sessionid': 'gxoucw0suytmmfsyuf1daahvmkys1d9g',
    'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d': '1699339272',
    'Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d': '1699343681',
    'm': 'ae705844192feff466d9dbdbc6009fb5|1699343922000',
}

headers = {
    'Host': 'www.python-spider.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.python-spider.com/challenge/3',
    'accept-language': 'zh-CN,zh;q=0.9',
}

response = requests.get('https://www.python-spider.com/challenge/3', headers=headers, cookies=cookies)

print(2222, response.text)