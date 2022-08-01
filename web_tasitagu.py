import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
#driver = webdriver.Chrome(options=options)
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get(url)  # driver실행

# 로그인
time.sleep(5)
driver.switch_to.frame('base')

elements = driver.find_element(By.XPATH, '//*[@id="xwup_certselect_tek_input1"]')
elements.send_keys('wndms0421!')
elements.send_keys(Keys.RETURN)
# 웹보고-이전보고건
time.sleep(5)
driver.switch_to.frame('base')
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/ul/li/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/ul/li/ul/li[1]/a').click()
time.sleep(20)
driver.switch_to.frame('ifrm')
driver.find_element(By.XPATH,'//*[@id="mbtnSearch"]').click()# 조회버튼
time.sleep(5)
table = driver.find_element(By.XPATH,'//*[@id="grdInfectionsReportList"]')
tbody = table.find_element(By.TAG_NAME,"tbody")
rows = tbody.find_element(By.TAG_NAME,"tr")

while True:
        try:
                driver.find_element(By.XPATH, '//*[@id="1"]/td[14]').click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="subDetailForm"]/div/div/button[1]').click()
                time.sleep(2)

                da = Alert(driver)
                da.accept()
                time.sleep(3)

                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                time.sleep(2)
                da = Alert(driver)
                da.accept()
                time.sleep(3)

        except selenium.common.exceptions.NoSuchElementException:
                driver.quit()