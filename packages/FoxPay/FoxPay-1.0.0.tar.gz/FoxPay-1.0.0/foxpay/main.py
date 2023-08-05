# -*- coding:utf-8 -*-

import hashlib
from OpenSSL.crypto import load_privatekey, FILETYPE_PEM, sign
import base64
import requests
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

#参数字典排序
def sort_dict_by_first_letter(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[0]))
    return sorted_dict

def base64_safe_decode(encoded_string):
    try:
        # 尝试对 Base64 编码的字符串进行解码
        decoded_bytes = base64.b64decode(encoded_string)
        # 将解码后的字节串转换为字符串
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except Exception as e:
        print("解码失败：", e)
        return None

#私钥加密sha1，并base64
def sign_message(message, private_key_string):
    # 将私钥字符串加载为私钥对象
    private_key = load_privatekey(FILETYPE_PEM, private_key_string)

    # 对消息进行哈希
    hash_value = hashlib.sha1(message.encode()).digest()

    # 使用私钥进行签名
    signature = sign(private_key, hash_value, "sha1")
    print(signature)
    encoded_signature = base64.b64encode(signature)

    return encoded_signature

def sign_with_private_key(data_to_sign, private_key_path):
    # 读取私钥 .pem 文件
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # 将字符串转换为字节串
    data_to_sign_bytes = data_to_sign.encode('utf-8')

    # 使用私钥进行 SHA1withRSA 签名
    signature = private_key.sign(
        data_to_sign_bytes,
        padding.PKCS1v15(),
        hashes.SHA1()
    )

    # 将签名结果进行 Base64 编码
    signature_base64 = base64.b64encode(signature).decode('utf-8')

    return signature_base64

def query_order(url_pre,data,appid,sign):
    url=url_pre+'/sdk/application/createApplicationOrder'
    print(sign)
    # input()
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'app_id': appid,
        'sign': sign
    }

    print(url)
    print(headers)
    print(data)
    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.status_code)
    print(response.json())

if __name__ == '__main__':
    my_dict = {
        'subject': '测试订单标题',
        'order_no': 20230628,
        'amount': 3.11,
        'notify_url': 'http://test.com/callback',
        'time_out': 5,
        'locale': 'zh-CN',
        'remark': '测试订单备注'
    }

    publick_key='MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCn4Q6mbmlSvH6kbeWJERz4rAQeTB/cEShKzgtkrWyaIZqHLgWh5iNdXyME0uaRUutFae1uc+J1yMyVU3cS+K36JUlqThmBHZ6/93KHsRvQ8FAcmBzKB2yVhW4qF0fA71yaWJzgNe93JI/4u3VSfu7tpy3ilPvmZlh6j9z9I+KKkQIDAQAB'
    private_key='MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAK7w5mS8/G7v7xjTAC5S+qx3E0OBFX6kt0kN3l9OHW7qA6cxFEP4DP04qRD3DCR4VvoHcNO0JwFv0Z3hc0afQt6qFGPcWMk9hFMTtB6gQwjOxLSRxDO2u1EVcfp13KzCLagx8/bfPM8+EMHkSXMPncIXmWXoy64r3aJmHOrCAgQnAgMBAAECgYAZjsMyC3Qbpvz41PatTd0mbh0H2ydvQZQvXZHTvZ9KMXEIL4Dk7yvCoND+VAFXoKcgTw76NtMOAC6RELtdIW5Mx+M4p8OZD+DeNqXUrXUpKd1odyagROSsqm03kwqDC+ZKIpU2f2SRST0HCi3ttXXMWqaKz3aeca6IaUPamoDGeQJBAPZHQRXlo1pbf0PJyjTgWkRB2FbZNCps9qoxhFMOOWf98rH/MvZ/Zi6YJMHqJssW+mK0lkMtgeHS5lwTgkGIqo8CQQC12MCRbBSdjL5hqUuFf8hUMQ+UC6yAEziiGAwkD5FhjpY07ylcywdJMH6srH4cFeYHTVfZPKLqk1yT46GheLjpAkAxSq+nL1ATnK6LJc836BOJB9jCATUkrKxuAf0nFni87KHvqFFN7s/H0aHBwhjDmzTAHr7YcTpGtYxvr2Pps+3XAkA7vhFN9X80X5fwh+ka2+dZ2aBvmAI9NZNmlZXvhvnRXkH09BnXtZAYOIl1e1oXKg6fmYZiBWzUukMxBxkD7qB5AkEAlP4x8e2red7uDNKk0iauppUFuZrX/dd3snm2ulAcC/qjacoXhCSF+KTApD9ScgZ7RJ4ZO2zr1lCfW5WbWaVi4Q=='
    appid='7IJNKYVX'

    # decoded_string = base64_safe_decode(private_key)
    # print(decoded_string)
    # input()

    url='http://139.159.184.46:7600'

    sorted_dict = sort_dict_by_first_letter(my_dict)

    signkey=''
    for key, value in sorted_dict.items():
        signkey=signkey+str(key)+'='+str(value)+'&'
    signkey=signkey[:-1]
    print(signkey)

    # 私钥字符串
    # 私钥内容
    private_key_string = f"-----BEGIN RSA PRIVATE KEY-----\n{private_key}\n-----END RSA PRIVATE KEY-----\n"

    print(private_key_string)
    # input()
    # 进行签名
    # signature = sign_message(signkey, private_key_string)
    private_key_path = "private.pem"
    signature=sign_with_private_key(signkey, private_key_path)

    # 打印签名结果
    print(signature)

    query_order(url,my_dict,appid,signature)