import requests
import xlrd


class Sendmethod():
    def __init__(self):
        self.urlstart = "http://192.168.6.100:8026/assistant/battery/replace?account=2019030612309589&token=eyJraWQiOiJpY21zIiwiYWxnIjoiUlMyNTYifQ.eyJ1c2VySWQiOjY4MiwiY29tcGFueUlkIjoxMSwib3JnSWQiOjE0LCJ1c2VyT3JnSWQiOjUzMywiZXhwIjoxNTc2ODQyMDA2LCJpYXQiOjE1NzQyNTAwMDYsImp0aSI6IlU0Sng0RkxfUmpLdDVwbE1sRmZ0cXcifQ.UL_F6qMIkgrANLhbWHQrY9uQaxYY3td-s_SkD233a6r1aL_b6JaTLHotFa623MlFOUZKTVMwT6BXiQIj68BrYIgQq77f2D9jzHCg5T91PKbN0CX_LAgUisnz4CLHxUtShONK0_u_uPne_aOPSu3k6wlYEXjw5cDKgzXjK0FkxBWTfLuUh3uLU_hhhc8Qm9ctra3oZ2CWC297qKb4O3V-IBTJr9ezzK0CTCHFVu1ThFQ_GB-q648pNa7hgobudiQhx8tH5pX_gn56GnvIC1b1CS7CrEECa8cfa2N630s3UIsliHPoa87Ih0F44Z9VAa2nfu5VUtMSKrMg0dDtZGNAOw"
        # self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    # get请求
    def send_get(self, url):
        url = url

        response = requests.get(url)
        restext = response.text
        resatus = response.status_code
        return restext, resatus

    def selectDataFromXls(self):
        count = 1
        for i in range(1000):
            resText,restatus = self.send_get(self.urlstart)
            if restatus == 200:
                with open('ok.txt', "a+", encoding="utf-8") as f:
                    f.write('第'+str(count) + "次访问成功" + "\n" +resText+ "===============" + "\n")
            else:
                with open('false.txt', "a+", encoding="utf-8") as f:
                    f.write('第'+str(count) + "次访问失败" + "\n" +resText+ "===============" + "\n")
            count += 1
if __name__ == "__main__":
    sendMethod = Sendmethod()
    sendMethod.selectDataFromXls()