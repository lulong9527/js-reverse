import time

import requests
import execjs


def get_sign(data):
    with open('compute_sign.js', 'r', encoding='utf-8') as f:
        demo_code = f.read()
    sign = execjs.compile(demo_code).call('get_sign', data)
    return sign


def post_data(data: str):
    cookies = {
        'PSTM': '1692418097',
        'BAIDUID': '9ACE297B2A06524DF8727B6DDB1B1CCB:FG=1',
        'BIDUPSID': '338BF1F7878D5A6E8C547387697B6334',
        'REALTIME_TRANS_SWITCH': '1',
        'FANYI_WORD_SWITCH': '1',
        'HISTORY_SWITCH': '1',
        'SOUND_SPD_SWITCH': '1',
        'SOUND_PREFER_SWITCH': '1',
        'H_WISE_SIDS': '216833_213361_214797_110085_244726_261718_236312_265615_265881_266358_267371_267074_268592_268706_266187_259642_269409_256151_269832_269905_269050_267066_256739_270460_270519_264424_270547_271171_263618_271321_271269_266028_270102_271812_271254_234296_234208_272282_267596_272466_272764_260335_273137_273231_273301_273400_273387_271157_273472_273520_271147_273318_264170_270186_272263_273164_274077_273931_274140_274177_273917_273043_273593_272857_274301_203520_274413_272562_179345_273071_274765_274762_274755_274778_274853_274857_274846_270158_275069_275097_267806_267548_272333_275167_274332_275199_275147_272317_275776_275782_270366_273491_275007_275823_275939_275970_274784_274079_276090_269610_276060_276120_275903_276202_276251_274283_274502_276196_276334_276244',
        'H_WISE_SIDS_BFESS': '216833_213361_214797_110085_244726_261718_236312_265615_265881_266358_267371_267074_268592_268706_266187_259642_269409_256151_269832_269905_269050_267066_256739_270460_270519_264424_270547_271171_263618_271321_271269_266028_270102_271812_271254_234296_234208_272282_267596_272466_272764_260335_273137_273231_273301_273400_273387_271157_273472_273520_271147_273318_264170_270186_272263_273164_274077_273931_274140_274177_273917_273043_273593_272857_274301_203520_274413_272562_179345_273071_274765_274762_274755_274778_274853_274857_274846_270158_275069_275097_267806_267548_272333_275167_274332_275199_275147_272317_275776_275782_270366_273491_275007_275823_275939_275970_274784_274079_276090_269610_276060_276120_275903_276202_276251_274283_274502_276196_276334_276244',
        'MCITY': '-179%3A',
        'BDUSS': 'VczVkFYYXByS01vekluaFBhSnFxRDlVMjVVcTYydHMyOEhMUkpFcW1KSTNzMkpsSVFBQUFBJCQAAAAAAAAAAAEAAAAKOehI0KHQocK9tPPLp7n4xbYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcmO2U3JjtlQ',
        'BDUSS_BFESS': 'VczVkFYYXByS01vekluaFBhSnFxRDlVMjVVcTYydHMyOEhMUkpFcW1KSTNzMkpsSVFBQUFBJCQAAAAAAAAAAAEAAAAKOehI0KHQocK9tPPLp7n4xbYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcmO2U3JjtlQ',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'BA_HECTOR': '0g2ka0ak802k2g21a0ak81am1ik4fjf1q',
        'BAIDUID_BFESS': '9ACE297B2A06524DF8727B6DDB1B1CCB:FG=1',
        'ZFY': ':AnBcgT4E0zKoc7EdhE1cD:BAzp3slHugmmxctOTNXV8U:C',
        'APPGUIDE_10_6_6': '1',
        'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1698840840',
        'BDRCVFR[feWj1Vr5u3D]': 'I67x6TjHwwYf0',
        'delPer': '0',
        'PSINO': '3',
        'H_PS_PSSID': '39531_39419_39592_39528_39497_26350_39561_22160',
        'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1698841550',
        'ab_sr': '1.0.1_NDc0ZTliOWEyNThmOWQ0Mjg2NDBkODg0YjJhOWYzMjQ2ZTI4MmYxOThmN2RjOWU1OGUzNDJiNmRmZmEyNTFkZTZlNGZhMGY0NTA3MDMxMjZjYzZiMzA1ZWZhODM2MDY1YWM2MjZhZWU5ZDM0NDE3NTMwYTE1ZDA5MDI1YzRmNzdiODhjZjgyZjgzYzZhOGZlOWY1OTMwMGZiNTg5OWZjYjdjYzBmNjQ5N2VkZjNmMjg5ZTU3MTA4YTZlYzY1NTFj',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Acs-Token': '1698841550259_1698841654391_rUmDAOVnVAwkizrnbmFxHFNs4aQ1Dtv24xGIHhqIzMXoAWuNDnnXS7kGCeCOBd90gCxRfAV20Rq++BUXApahx1n8Aut0tUl9+DbHAWTqauvZ+BlhWea7/WfD10qcmSoXT/8psFTjojmJT3d7UohxH8w3FrxIXffmQwqDI96EgZMxeNCgnq4kbOhQG6UuHIamiNAaw6lHRxunD1vvEExv6yoTEcOPWbrRXGqPC5Qrd0qfvnFvhcdqwpjvs7qntQQB3AkNBOSAS6JR/gvagEiuoMr/g2tTFYGeeBknnf9qqA9ZryxVlCfn4qAPFvWcMn3SypxPlDnTRoymg5NgqL8gCaDrXi9txejCPo3T8x2IPuIpmYhLVGHGeiwXpqJpxlvCKmB2o4Ppveg1uW6xlPXNxwmrMPewR8oSnd4+zkkuPKTQw9a7PAg/gy7t7OQ8ha/loMp6d41F0LhssO0miBLx34WN2U1vrugAk7+fTtmclzJIMsgfCAE5uJhP7AsssPgO506+PhtpWpn42OFhJgeZTA==',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://fanyi.baidu.com',
        'Pragma': 'no-cache',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    params = (
        ('from', 'zh'),
        ('to', 'en'),
    )
    data = {
        'from': 'zh',
        'to': 'en',
        'query': data,
        'transtype': 'enter',
        'simple_means_flag': '3',
        'sign': get_sign(data),
        'token': '24cae223b795d34ae95b9f486e8b9472',
        'domain': 'common',
        'ts': str(round(time.time()*1000))
    }
    response = requests.post('https://fanyi.baidu.com/v2transapi', headers=headers, params=params, cookies=cookies,
                             data=data)
    print(response.text)


if __name__ == '__main__':
    post_data('中国')
