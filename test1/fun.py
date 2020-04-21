from test1.send_method import *
import os
import requests

# file_path1=os.path.abspath(os.path.dirname(__file__))+'/casefile/test_appraiseOrderbody66.json'
# openf=Openfile(file_path)
# t=openf.open_csv()
# api='http://10.168.17.181/rx_api/api_order/order/appraiseOrder/'
# openf1=Openfile(file_path1)
# t1=openf1.openjson()
# for i in t:
#     url = api + i[0] + ',' + i[1]
#     run = Sendmethod(url,t1)
#     print('订单类订单评价接口'+run.send_put())



url='https://www.baidu.com'
r=requests.get(url)
if r.status_code==200:
    print('ok')
    l=[1,'2',7,'hjg']
    # with open('./casefile/test_appraiseOrder66', 'a+') as f:
    #     f.write('a' +str(l)+ '\n')
    f=Openfile('./casefile/test_getDicList2.txt')
    L=f.openfile()
    s=str(L[0])
    print(s)
