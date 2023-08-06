# -*- coding: utf-8 -*-

import requests, json

# url
base_url = 'https://investlife.cn/data/'

# token
token = ''

# 设置token
def set_token(param):
    token = param

def get_stock_list(listed_state, fields):
    headers = {'Content-Type': 'application/json', 'token': token}
    url = base_url + 'get_stock_list'
    param = {'listed_state': listed_state, 'fields': fields}

    return requests.post(url=url, headers=headers, data=json.dumps(param))