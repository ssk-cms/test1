'''
读取excel表格中图片地址，生成指定文件夹将图片下载并保存
'''
import time
import urllib.request

from utils import CreateDictionaryUtils
from utils.OpenExcelUtils import OpenExcelUtils
from utils.ShowPerformProcessUtils import ShowProcess


class GenerateImages():
    path = "F:\\peoplePhotos\\"
    '''
    下载图片并保存
    '''

    def download(self, path, idCardFaceAddress, idCardBackAddress, mainPageAddress, attachPageAddress, idcard):
        # 下载身份证正面照片
        if idCardFaceAddress is None:
            fileName = '身份证正面照片下载失败集合.txt'
            content = "身份证号为" + idcard + "身份证正面照片下载失败" + "===============" + "\n"
            self.writeFile(fileName, content)
            return
        else:
            urllib.request.urlretrieve(idCardFaceAddress, path + '\\idCardFace.jpg')
        # 下载身份证背面照片
        if idCardBackAddress is None:
            fileName = '身份证背面照片下载失败集合.txt'
            content = "身份证号为" + idcard + "身份证背面照片下载失败" + "===============" + "\n"
            self.writeFile(fileName, content)
            return
        else:
            urllib.request.urlretrieve(idCardBackAddress, path + '\\idCardBack.jpg')
        # 下载驾驶证主页照片
        if mainPageAddress is None:
            fileName = '驾驶证主页照片下载失败集合.txt'
            content = "身份证号为" + idcard + "驾驶证主页照片下载失败" + "===============" + "\n"
            self.writeFile(fileName, content)
            return
        else:
            urllib.request.urlretrieve(mainPageAddress, path + '\\mainPage.jpg')
        # 下载驾驶证副页照片
        if attachPageAddress is None:
            fileName = '驾驶证副页照片下载失败集合.txt'
            content = "身份证号为" + idcard + "驾驶证副页照片下载失败" + "===============" + "\n"
            self.writeFile(fileName, content)
            return
        else:
            urllib.request.urlretrieve(attachPageAddress, path + '\\attachPage.jpg')

    '''
    读写文件
    '''

    def writeFile(self, filename, content):
        with open(filename, "a+", encoding="utf-8") as f:
            f.write(content)

    '''
    读取表格内容
    '''

    def gainContent(self):
        sheet = OpenExcelUtils.open_excel(self, tableName="司机图片.xlsx", sheetName="司机图片")
        for i in range(sheet.nrows):
            i = i + 1
            # 司机姓名
            driverName = sheet.cell(i, 0).value
            # 身份证号
            idCard = sheet.cell(i, 1).value
            # 手机号
            phone = sheet.cell(i, 2).value
            # 车牌号
            vichelNumber = sheet.cell(i, 3).value
            # 身份证正面照
            idCardFace = sheet.cell(i, 4).value
            # 身份证背面照
            idCardBack = sheet.cell(i, 5).value
            # 驾驶证正面
            mainPage = sheet.cell(i, 6).value
            # 驾驶证背面
            attachPage = sheet.cell(i, 7).value
            # 居住证
            residencePermit = sheet.cell(i, 8).value
            # 创建目录（人证文件夹用司机手机号命名，如果没有手机号则用司机姓名+无手机号命名）
            if phone is None:
                path = self.path + idCard + "无手机号"
            else:
                path = self.path + phone

            if CreateDictionaryUtils.CreateDictionary.createDictionary(self, self.path + phone):
                self.download(path, idCardFace, idCardBack, mainPage, attachPage, idCard)
            else:
                self.writeFile('创建文件夹失败集合.txt', "身份证号为" + idCard + "创建文件夹失败" + "===============" + "\n")
                continue
            # 显示任务执行进度
            process_bar = ShowProcess(sheet.nrows, 'OK')
            process_bar.show_process(i)
            time.sleep(0.01)
            if i > sheet.nrows:
                break




if __name__ == "__main__":
    gainContent = GenerateImages()
    gainContent.gainContent()
