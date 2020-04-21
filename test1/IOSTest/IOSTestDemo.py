import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class IOSTestDemo(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'IOSTestDemo'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'ed7eedfd8422c94eb026882417defeca58f871c2'
        self.dc['platformName'] = 'ios'
        # self.dc['deviceName']='127.0.0.1:4723'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testIOSTestDemo(self):
        self.driver.find_element_by_xpath("xpath=//*[@text='逸车主']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text=' 工具箱']").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//*[@text='运输证查询' and ./parent::*[@text='运输证查询']]")))
        self.driver.find_element_by_xpath("xpath=//*[@text='运输证查询' and ./parent::*[@text='运输证查询']]").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text=' 我的']")))
        self.driver.find_element_by_xpath("xpath=//*[@text=' 我的']").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@text=' 工具箱']")))
        self.driver.find_element_by_xpath("xpath=//*[@text=' 工具箱']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='保单查询' and ./parent::*[@text='保单查询']]").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@accessibilityLabel='header-back']")))
        self.driver.find_element_by_xpath("xpath=//*[@accessibilityLabel='header-back']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text=' 首页']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
