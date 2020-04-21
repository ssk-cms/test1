import requests
import time
import datetime

import json
import base64

baseurl = "http://139.159.204.118:8765/open/service/wzQueryAndCalPrice"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"}

#终端输入
# key = input("请输入搜索内容:")
# pn = int(input("输入页数:"))
# pn = (pn-1) * 10

t = time.time()
nowTime = lambda:int(round(t * 1000))

s = requests.session()
s.keep_alive = False
result = ""
#wd = key&pn=10
params = {
        "json":json.dumps(base64.b64encode({"fdjh":"063723","hphm":"粤Y72Y28","hpzl":"02","vin":"185038"})),
        "timestamp":str(nowTime),
        "appKey":"ToBeNo.1",
        "accode":"888888"
        }

#无需拼接url地址 也不用url 编码
res = requests.post(baseurl,params=params,headers=headers)
print(res)
print(res.content)
print(base64.b64encode(res.text.encode("utf-8")))
html = res.text
print(json.loads(html,strict=False))