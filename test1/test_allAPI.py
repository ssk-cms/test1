from test1.send_method import *

# 将所有的接口和对应的参数txt文件存入字典中，以后按需取
api_address={"api_mall/classification/":'./casefile/test_addClassification46.txt',
             "api_order/drawback/":"./casefile/test_adddrawback68.txt",
             "api_mall/goods/add/":"./casefile/test_addGoods44.txt",
             "api_mall/classification/":"./casefile/test_addGoodsBuriedPoint45.txt",
             "api_app/member/addMember/":"./casefile/test_addMember10.txt",
             "api_app/merchant/addMerchant/":"./casefile/test_addMerchant17.txt",
             "api_order/order/addDishOrder/":"./casefile/test_addMerchant62.txt",
             "api_app/merchantBankcard/":"./casefile/test_addMerchantBankcard22.txt",
             "api_order/order/":"./casefile/test_addOrder61.txt",
             "api_mall/shopBuriedPoint/":"./casefile/test_addShopBuriedPoint38.txt",
             "api_mall/shopBuriedPoint/count/":"./casefile/test_addShopBuriedPoint39.txt",
             "api_mall/shopCollection/":"./casefile/test_addShopCollection35.txt",
             "api_task/task/":"./casefile/test_addTask49.txt",
             "api_task/taskCheck/":"./casefile/test_addTaskCheck54.txt",
             "api_task/taskReceipt/":"./casefile/test_addTaskReceipt53.txt",
             "api_task/taskReward/":"./casefile/test_addTaskReward56.txt",
             "api_mall/vip/":"./casefile/test_addVip30.txt",
             "api_mall/vipTask/":"./casefile/test_addVipTask34.txt",
             "api_order/order/appraiseOrder/":"./casefile/test_appraiseOrder67.txt",
             "api_order/order/closeOrder/":"./casefile/test_closeOrder65.txt",
             "api_mall/shopCollection/":"./casefile/test_delShopCollection36.txt",
             "api_mall/vip/":"./casefile/test_delVip31.txt",
             "api_task/taskReward/advance/":"./casefile/test_getAdvanceChance57.txt",
             "api_app/advertisement/":"./casefile/test_getAdvertisementInfo5.txt",
             "api_mall/shop/browseRecord/":"./casefile/test_getBrowseRecord40.txt",
             "api_mall/classification/":"./casefile/test_getClassificationPage48.txt",
             "api_mall/shopCollection/":"./casefile/test_getCollectionShop37.txt",
             "api_app/commercialArea/":"./casefile/test_getCommercialAreaInfo6.txt",
             "api_business/dic/":"./casefile/test_getDicList2.txt",
             "api_order/drawback/":"./casefile/test_getDrawbackInfo70.txt",
             "api_order/drawback/":"./casefile/test_getDrawbackPage71.txt",
             "api_mall/goods/":"./casefile/test_getGoodsInfo41.txt",
             "api_mall/goods/select/":"./casefile/test_getGoodsPage43.txt",
             "api_app/memberBills/":"./casefile/test_getMemberBillsPage13.txt",
             "api_app/member/":"./casefile/test_getMemberInfo8.txt",
             "api_app/merchantBankcard/":"./casefile/test_getMerchantBankcardInfo21.txt"}

class DealApi():

    def resolvingFile(self,api,filePath):

        self.api = api
        self.filePath = filePath

        f = Openfile(filePath)
        t = f.openfile()
        self.L = []
        self.ok = 0

        for i in t:
            url = api + i[0] + ',' + i[1]  # 按需拼接参数
            run = Sendmethod()
            # print(i[-1].strip())
            r, res = run.send_get(url)  # 按需选择请求方式
            if res == 200:
                self.ok += 1
                self.L.append(r)
            else:
                self.L.append(res)

    def WriteFile(self):

        apiName = input("请输入接口名称：") #输入汉字
        with open('report.txt', 'a+', encoding="utf-8") as f:
            f.write(apiName+'%s次，成功与失败返回如下：%s ' % (self.ok, self.L))  # 按需更改汉字

        with open('report.txt', 'a+', encoding="utf-8") as f:
            f.write("========================"+"\n")  #结束符

if __name__ == "_main_"():

    dealApi = DealApi()
    for i in api_address:

        api = i.keys()
        filePath = i.values()
        dealApi.resolvingFile(api,filePath)
        dealApi.WriteFile()

    print("接口测试完毕，具体请看report.txt")
