# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import selenium
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

url = ""#접속할 사이트

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get(url)  # driver실행

# 로그인
time.sleep(7)
driver.switch_to.frame('base')

#공인인증서
# 역학조사
time.sleep(5)
driver.switch_to.frame('base')
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[3]/a').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[3]/ul/li[2]/a').click()

time.sleep(30)
element = driver.switch_to.frame("ifrm")  # 프레임 변경
#driver.find_element(By.XPATH, '//*[@id="schReportDeStartCal"]').click()  # 날짜 선택(시작)
#driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[4]/a').click()  # (해당날짜 클릭)
#driver.find_element(By.XPATH, '//*[@id="schReportDeEndCal"]').click()  # 날짜 선택(끝)
#driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[4]/a').click()  # (해당날짜 클릭)

driver.find_element(By.XPATH, '//*[@id="contetnsWrap"]/tbody/tr/td/div[3]/div[2]/button[1]').click()  # 조회버튼 클릭
#임시저장을 저장으로
while True:
    try:
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="1"]/td[3]').click()
        driver.find_element(By.XPATH, '//*[@id="contetnsWrap"]/tbody/tr/td/div[3]/div[2]/button[4]').click()
        time.sleep(6)
        driver.find_element(By.XPATH,
                            '//*[@id="regist_pop"]/div/div[1]/div[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/img').click()
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]/a').click()
        if driver.find_element(By.XPATH, '// *[ @ id = "covidVacntnAt"]').is_selected() == True :
            driver.find_element(By.XPATH, '//*[@id="btn_modi"]').click()
            # 팝업창
            time.sleep(5)
            da = Alert(driver)
            da.accept()
            time.sleep(5)
            da.accept()
            time.sleep(6)
        else:
            driver.find_element(By.CSS_SELECTOR, '#covidVacntnAt').click()
            driver.find_element(By.XPATH, '//*[@id="btn_modi"]').click()
            # 팝업창
            time.sleep(5)
            da = Alert(driver)
            da.accept()
            time.sleep(5)
            da.accept()
            time.sleep(6)
    except selenium.common.exceptions.NoSuchElementException:
        driver.Dispose()
