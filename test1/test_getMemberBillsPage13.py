from test1.send_method import *


api='api_app/memberBills/'#按需更改
file_path='./casefile/test_getMemberBillsPage13.txt'#txt文件统一建在casefile下

f=Openfile(file_path)
t=f.openfile()
L=[]
ok=0
print(t)
for i in t:
    url = api + i[0] + ',' + i[1]+ ',' + i[2]+ ',' + i[3]#按需拼接参数
    run = Sendmethod()
    t=i[-1].strip()
    data = eval(t.strip())
    print(type(data))


    r, res = run.send_post(url, data)  # 按需选择请求方式

    if res==200:
        ok+=1
        L.append(r)
    else:
        L.append(res)
# L=','.join(L)
with open('report.txt', 'a+',encoding="utf-8") as f:
    f.write('用户类用户账单列表接口共成功执行%s次，成功与失败返回如下：%s '%(ok,L))#按需更改汉字