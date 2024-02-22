# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: test.py
@time: 2023/11/21 15:15
@desc:

"""
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

url = "https://movie.douban.com/j/chart/top_list"
params = {
    "type": "17",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "100"
}
response = requests.get(url, headers=headers, params=params)

# print(json.dumps(response.json(),indent=4,ensure_ascii=False))

data = response.json()
for args in data:
    title = args["title"]
    score = args["score"]
    rank = args["rank"]
    print(title, score, rank)
