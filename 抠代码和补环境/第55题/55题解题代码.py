import requests
import json
import base64
from Crypto.Cipher import AES


def get_response(page):
    headers = {
        'authority': 'www.python-spider.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1698391348,1698644393,1698812805,1699158090; sessionid=962dlukx2g7146qd07ts6z32owlgioh6; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1699159553',
        'origin': 'https://www.python-spider.com',
        'referer': 'https://www.python-spider.com/challenge/55',
        'sec-ch-ua': '^\\^Google',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'page': str(page)
    }
    response = requests.post('https://www.python-spider.com/api/challenge55', headers=headers, data=data)
    result = response.json()['result']
    return result


# 将原始的明文用空格填充到16字节
def pad(data):
    pad_data = data
    for i in range(0, 16 - len(data)):
        pad_data = pad_data + ' '
    return pad_data


def AES_de(key, data, iv=None):
    # 解密过程逆着加密过程写
    # 将密文字符串重新编码成二进制形式
    data = data.encode("utf-8")
    # 将base64的编码解开
    data = base64.b64decode(data)
    # 创建解密对象
    AES_de_obj = AES.new(key.encode("utf-8"), AES.MODE_ECB)
    # 完成解密
    AES_de_str = AES_de_obj.decrypt(data)
    # 去掉补上的空格
    AES_de_str = AES_de_str.strip()
    # # 对明文解码
    AES_de_str = AES_de_str.decode("utf-8")
    return AES_de_str


if __name__ == '__main__':
    num = 0
    key = 'aiding6666666666'
    for i in range(100):
        pages = i + 1
        print('pages:', pages)
        data = get_response(pages)
        res_str = AES_de(key, data)
        res_str = res_str.replace(res_str.split("}")[-1], '')
        res_dict = json.loads(res_str)
        for j in res_dict['data']:
            num += int(j['value'])
    print('num:', num)
