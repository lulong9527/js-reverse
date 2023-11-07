# -*- coding: utf-8 -*-
import base64
import hashlib


# 将数据转换成 base64编码
def str_to_bs64(data: str):
    base64_string = base64.b64encode(data.encode()).decode()
    return base64_string


# 将数据 进行 md5 加密, 并转换成 十六进制字符串
def str_to_md5(data: str):
    # 将字符串编码并进行 MD5 加密
    hash_object = hashlib.md5(data.encode())
    # 获取加密后的十六进制字符串
    hash_hex = hash_object.hexdigest()
    return hash_hex


__all__ = ['str_to_bs64', 'str_to_md5']
