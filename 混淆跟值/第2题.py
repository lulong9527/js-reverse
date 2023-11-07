import requests
import subprocess
result = subprocess.check_output(['node', '第2题.js'])
sign = result.decode().replace('\n', '')
print(type(sign), sign)
cookies = {
    'sessionid': 'cwcac9fjwh6ct9es91qvky7x4f374481',
    'sign': sign

}
response = requests.get('https://www.python-spider.com/challenge/2', cookies=cookies)
print(response.text)
