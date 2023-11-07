# -*- coding: utf-8 -*-
import requests
from encryption_decryption_function import str_to_bs64

"""
目标：采集100页的全部数字，并计算所有数据加和！ 本题js加密为入门难度。当做新手训练。无限debugger难度较高，可以用于无限debugger训练

// arguments 类数组 特性，不是数组，只有一部分数组的特性，其余很多属性没有
_eval = eval;
eval= function(){
    // [xxxx].indexOf('xxxx') 判断[]数组中是否包含 'xxxx' 的值相等，相等返回0，不等返回-1
    if ([arguments[0]].indexOf('debugger'))
    return _eval(arguments[0])
}


// 此处要接触 原型链 知识， __proto__ 相当于父(上级)，prototype 相当于兄(同级)， a = new Date() 相当于 a继承Date(a是Date儿子), 
// 当 new Date() 函数变更，无需在new 一个对象, a 跟着变更，相当于浅拷贝
_appendChild = Node.prototype.appendChild
Node.prototype.appendChild = function(){
    if (arguments[0].innerHTML && arguments[0].innerHTML.indexOf('debugger') != -1){
         arguments[0].innerHTML = ''
    }
    return _appendChild.apply(this, arguments)
}

// 学过原型链的大家应该都清楚了
已知：
1. Function.constructor = Function
2. 所有的函数定义，实际上都是 new Function
3. 也就是说，函数实际上是 Function 的实例化对象
4. 那么函数的constructor，实际上就是 Function.prototype.constructor
5. 所以 Function.prototype.constructor = Function
6. 所以只要修改 Function.prototype.constructor，就可以实现 hook 自定义函数的constructor 目的

所以应该这样写：
_Function = Function
Function.prototype.constructor = function(){
    if (arguments[0].indexOf('debugger') != -1){
            return _Function('')
        }
    return _Function(arguments[0])
}
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
