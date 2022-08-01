import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
def check_exists_by_SELECTOR(selector):
    try:
        driver.find_element(By.CSS_SELECTOR,selector)
    except NoSuchElementException:
        return False
    return True

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
#공인인증서
# 웹보고-이전보고건
time.sleep(5)
driver.switch_to.frame('base')
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/ul/li/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/ul/li/ul/li[1]/a').click()
time.sleep(22)
driver.switch_to.frame('ifrm')
driver.find_element(By.XPATH,'//*[@id="mbtnSearch"]').click()# 조회버튼
time.sleep(120)
table = driver.find_element(By.XPATH,'//*[@id="grdInfectionsReportList"]')
tbody = table.find_element(By.TAG_NAME,"tbody")
rows = tbody.find_element(By.TAG_NAME,"tr")

time.sleep(1)

time.sleep(3)

i=4
while True:
        try:
                time.sleep(3)

                driver.find_element(By.XPATH, f'//*[@id="{i}"]/td[14]').click()
                time.sleep(3)

#여기부터 시작
                modify=check_exists_by_SELECTOR("#sbtnUpdate")

                if(modify==True):
                        driver.find_element(By.XPATH,'//*[@id="sbtnUpdate"]').click()  # 이전보고건 수정 버튼
                        time.sleep(5)

                        #da = Alert(driver)
                        #da.accept()
                        #time.sleep(3)

                        driver.find_element(By.XPATH,'//*[@id="prdoDsndgnssInspctResultTyCd2" and @value="2"]').click()  # 음성체크
                        driver.find_element(By.XPATH, '//*[@id="prdoPatntClCd4"and @value="4"]').click()

                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                        try:
                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())

                        except:
                                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                        time.sleep(2)
                        element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                        da = Alert(driver)

                        time.sleep(3)
                        # alert의 텍스트 출력
                        if (da.text == '발병일은 진단일 보다 빨라야 합니다.'):

                                da.accept()

                                month = driver.find_element(By.XPATH, '//*[@id="ptxtDgnssDe2"]').get_attribute("value")
                                day = driver.find_element(By.XPATH, '//*[@id="ptxtDgnssDe3"]').get_attribute("value")
                                error_month = driver.find_element(By.XPATH, '//*[@id="ptxtAtfssDe2"]')
                                error_day = driver.find_element(By.XPATH, '//*[@id="ptxtAtfssDe3"]')
                                error_month.clear()
                                error_day.clear()

                                error_month.send_keys(month)
                                error_day.send_keys(day)
                                time.sleep(2)

                                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                try:
                                        element = WebDriverWait(driver, 2).until(EC.alert_is_present())

                                except:
                                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                time.sleep(1)
                                da = Alert(driver)
                                da.accept()
                                time.sleep(3)
                        elif (da.text == '외국인인 경우, 국적 정보를 기재하여 주시기 바랍니다.'):
                                da.accept()

                                driver.find_element(By.XPATH,'//*[@id="ptxtPatntNlty"]').click()
                                driver.find_element(By.XPATH,'//*[@id="ptxtPatntNlty"]').send_keys('미상')

                                try:
                                        element = WebDriverWait(driver, 2).until(EC.alert_is_present())

                                except:
                                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                time.sleep(2)
                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                                da = Alert(driver)
                                da.accept()

                                time.sleep(3)

                        else:
                                da.accept()
                                time.sleep(2)


                else:

                        driver.find_element(By.XPATH,'//*[@id="sbtnClose"]').click()
                        i+=1


        except:
                driver.quit()
'''
         #여기부터 원래 코드
                driver.find_element(By.XPATH, '//*[@id="subDetailForm"]/div/div/button[1]').click()#이전보고건 수정 버튼

                time.sleep(2)

                da = Alert(driver)
                da.accept()
                time.sleep(3)
                driver.find_element(By.XPATH,'//*[@id="prdoDsndgnssInspctResultTyCd2"and @value="2"]').click() #음성체크
                driver.find_element(By.XPATH,'//*[@id="prdoPatntClCd4"and @value="4"]').click()

                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                try:
                        element = WebDriverWait(driver, 2).until(EC.alert_is_present())

                except:
                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                time.sleep(2)
                alert = driver.switch_to.alert
                # alert의 텍스트 출력
                if alert.text == '발병일은 진단일 보다 빨라야 합니다.':
                        alert.accept()

                        month=driver.find_element(By.XPATH,'//*[@id="ptxtDgnssDe2"]').get_attribute("value")
                        day=driver.find_element(By.XPATH,'//*[@id="ptxtDgnssDe3"]').get_attribute("value")
                        error_month=driver.find_element(By.XPATH, '//*[@id="ptxtAtfssDe2"]')
                        error_day=driver.find_element(By.XPATH,'//*[@id="ptxtAtfssDe3"]')
                        error_month.clear()
                        error_day.clear()

                        error_month.send_keys(month)
                        error_day.send_keys(day)
                        time.sleep(2)

                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                        try:
                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())

                        except:
                                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                        time.sleep(1)
                        da = Alert(driver)
                        da.accept()
                        time.sleep(3)
                        
                else:
                        da.accept()
                        time.sleep(3)

        except selenium.common.exceptions.NoSuchElementException:
                driver.quit()
'''