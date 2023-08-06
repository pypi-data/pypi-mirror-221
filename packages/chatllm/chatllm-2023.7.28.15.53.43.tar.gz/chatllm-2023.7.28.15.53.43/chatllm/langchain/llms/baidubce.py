#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : baidubce
# @Time         : 2023/7/26 17:16
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :
"""
# 接口设计
1. 重试逻辑
2. 多线程请求/异步请求
3. 转换为openai


"""

from meutils.pipe import *

api_key = 'APCEKzr4rU8ywqPxzDQn0rCn'
secret_key = '5ryzXEhNkk5DT9PeX3jLhZ1w3rsEUktn'


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
    return response.json().get("access_token")


import requests
import json

import requests
import json


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

    response = requests.request("POST", url)
    return response.json().get("access_token")


def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你好" * 1000
            }
        ]
    })

    response = requests.request("POST", url, data=payload)

    print(response.text)


if __name__ == '__main__':
    main()
