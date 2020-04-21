# 10.用户发起退款
# 接口方法： POST
# 接口地址：/api_order/drawback/{userId},{sign}
# 签名生成参数：adddrawback
from test1.send_method import *
api = 'api_order/drawback/'#按需更改
file_path = './casefile/test_adddrawback68.txt'#txt文件统一建在casefile下
f = Openfile(file_path)
t = f.openfile()
L = []
ok = 0
for i in t:
    url = api + i[0] + ',' + i[1]  #按需拼接参数
    run = Sendmethod() # get参数 不用传
    t = i[-1].strip()
    data = eval(t.strip())

    r, res = run.send_post(url, data)  # 按需选择请求方式
    if res == 200:
        ok += 1
        L.append(r)
    else:
        L.append(res)
with open('report.txt', 'a+', encoding="utf-8") as f:
    f.write('订单类 , 用户发起退款成功 %s次，成功与失败返回如下：%s ' % (ok, L))  # 按需更改汉字
print("====================")