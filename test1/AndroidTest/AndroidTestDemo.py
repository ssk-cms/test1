import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class AndroidTestDemo(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'AndroidTestDemo'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '9cf6e04e'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testAndroidTestDemo(self):
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='item_icon' and ./parent::*[@contentDescription='逸车主']]").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//*[@id='iv_tab_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='工具箱']]")))
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='iv_tab_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='工具箱']]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='ivApp' and (./preceding-sibling::* | ./following-sibling::*)[@text='保单查询']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='返回']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='ivApp' and (./preceding-sibling::* | ./following-sibling::*)[@text='运输证查询']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='返回']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='iv_tab_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='首页']]").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
