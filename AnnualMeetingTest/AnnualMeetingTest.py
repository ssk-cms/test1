import requests
import xlrd


class Sendmethod():
    def __init__(self):
        self.urlstart = "http://47.99.154.25:8099/wx/activity/cj/do?token=eyJraWQiOiJpY21zIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiLotbXkvJ_kvJ8iLCJkcml2ZXJJZCI6MjA3MjcsImNvbXBhbnlJZCI6MywiZXhwIjoxNTY4MzU0NDg1LCJpYXQiOjE1NjU3NjI0ODUsImp0aSI6Ii0zanBiTmI2amkxSTZZd25DaWpJUUEifQ.dflY3uR9Llhjaozh6uK8OZ8Ylju7A47PlTUt0DPg_zrCAvTMq8VKjdyFwfW2Xyp89nlE-QVEoOGOSQ6jACipsHYi6yLqXmfb2CImzSDEoFguImtkPIOe_3A9prbSn1DQ76i3mUsBI535wzYyoZTqqP6nvZXNy-tdZtmZ8nEi82kGXn0MTdMi8nGV84E14k_Q_JW0MWrytlbRhVbs6ZDhLew0QjesSHvsgBhXegnGtkfa965ebEENp8FXtoaHqGVO-oD0YEQ8eAHYlE8Ej5hfFihAaerBhPAK3ztcxtWja79MS06YjzNNtBS5vKTbwO1fxFnJzLcMv6wLEETJgbcgEw"
        # self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    #post请求
    def send_post(self,json=None):
        url = self.urlstart

        response = requests.post(url=url,json=json)
        restext = response.text
        resatus = response.status_code
        return restext,resatus

    def open_excel(self):
        try:
            book = xlrd.open_workbook("ic_activity_cj.xls")
        except:
            print("open excel file failed!")
        try:
            sheet = book.sheet_by_name("ic_activity_cj")
            return sheet
        except:
            print("locate worksheet in excel failed!")

    def selectDataFromXls(self):
        sheet = self.open_excel()
        count = 1
        for i in range(sheet.nrows):
            dict = {}
            dict["carId"] = int(sheet.cell(i, 0).value)
            dict["driverId"] = int(sheet.cell(i,1).value)
            resText,restatus = self.send_post(dict)
            if "恭喜" in resText:
                with open('win.txt', "a+", encoding="utf-8") as f:
                    f.write('第'+str(count) + "次中奖" + "\n" +resText+ "===============" + "\n")

            else:
                with open('lose.txt', "a+", encoding="utf-8") as f:
                    f.write('第'+str(count) + "人[未]中奖" +resText +"\n" +"===============" + "\n")
            count += 1
if __name__ == "__main__":
    sendMethod = Sendmethod()
    sendMethod.selectDataFromXls()