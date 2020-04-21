from test1.send_method import *


api='api_mall/shop/browseRecord/'#按需更改
file_path='./casefile/test_getBrowseRecord40.txt'#txt文件统一建在casefile下

f=Openfile(file_path)
t=f.openfile()
L=[]
ok=0
print(t)
for i in t:
    url = api + i[0] + ',' + i[1]#按需拼接参数
    run = Sendmethod()
    # print(i[-1].strip())
    r,res=run.send_get(url)#按需选择请求方式
    if res==200:
        ok+=1
        L.append(r)
    else:
        L.append(res)
with open('report.txt', 'a+',encoding="utf-8") as f:
    f.write('店铺类店铺浏览记录接口共成功执行%s次，成功与失败返回如下：%s '%(ok,L))#按需更改汉字