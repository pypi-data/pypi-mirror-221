# -*- coding: utf-8 -*-

import requests, json
import pickle

# url
base_url = 'https://investlife.cn/data/'

# token
g_token = None

# 设置token
def set_token(user_token):
    global g_token
    g_token = user_token

def get_stock_list(listed_state = None, fields = None):
    headers = {'Content-Type': 'application/json', 'token': g_token}
    url = base_url + 'get_stock_list'
    param = {'listed_state': listed_state, 'fields': fields}

    res = requests.post(url=url, headers=headers, data=json.dumps(param))

    if res.ok:
        return pickle.loads(res.content)

    raise Exception(res.text)
    

if __name__ == '__main__':
    set_token('abc')
    data = get_stock_list()
    print(data)