
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
time.sleep(3)
#driver.find_element(By.XPATH,'//*[@id="xwup_cert_table"]/table/tbody/tr[8]/td[2]/div').click()
#공인인증서
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
time.sleep(120)
table = driver.find_element(By.XPATH,'//*[@id="grdInfectionsReportList"]')
tbody = table.find_element(By.TAG_NAME,"tbody")
rows = tbody.find_element(By.TAG_NAME,"tr")
i=1
while True:
        try:


                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="{i}"]/td[14]').click()
                time.sleep(3)
                exists=check_exists_by_SELECTOR("#sbtnUpdate")


                if (exists == True):
                        driver.find_element(By.XPATH, '//*[@id="sbtnUpdate"]').click()

                        time.sleep(1)

                       # da = Alert(driver)
                        #da.accept()

                        try:
                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                                da = Alert(driver)
                                if (da.text == '현재 이 문서가 수정 중인 상태입니다. 잠시 후 다시 시도해주시기 바랍니다.'):
                                        da.accept()
                                        time.sleep(1)
                                        driver.find_element(By.ID, 'sbtnClose').click()
                                        i += 1

                        except:
                                time.sleep(2)
                                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()#보고함
                                try:
                                        element = WebDriverWait(driver, 2).until(EC.alert_is_present())

                                except:
                                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()

                                time.sleep(2)
                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                                da = Alert(driver)

                                reported = '일자에 이미 신고된 문서가 있습니다.'
                                if(da.text=='한글, 영문, 기본 특수문자만 입력 가능합니다.'):
                                        da.accept()

                                        input=driver.find_element(By.XPATH,'//*[@id="ptxtEidsSymptms"]')
                                        input.click()
                                        input.send_keys(Keys.ARROW_DOWN)

                                        input_2=driver.find_element(By.XPATH,'//*[@id="ptxtRmInfo"]')
                                        input_2.click()
                                        input_2.send_keys(Keys.ARROW_DOWN)

                                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()  # 보고함
                                        try:
                                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                                        except:
                                                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                        da.accept()
                                        time.sleep(3)


                                elif(da.text=='의료기관 정보가 등록되어 있지 않습니다. 콜센터(1522-6339)에 문의 바랍니다.'):
                                        da.accept()
                                        time.sleep(1)
                                        hospital_info=driver.find_element(By.XPATH, '//*[@id="ptxtSttemntMdlcnstNm"]')
                                        hospital_info=hospital_info.get_attribute('innerText')
                                        time.sleep(1)

                                        driver.find_element(By.XPATH,'//*[@id="pbtnSearchSttemntMdlcnst"]').click()
                                        driver.find_element(By.XPATH,'//*[@id="txtSearchinsttNm"]').click()
                                        time.sleep(1)
                                        driver.find_element(By.XPATH,'//*[@id="txtSearchinsttNm"]').send_keys(hospital_info)
                                        time.sleep(1)
                                        driver.find_element(By.XPATH,'//*[@id="ibtnPopSearch"]').click()
                                        time.sleep(2)
                                        driver.find_element(By.XPATH,'//*[@id="1"]/td[4]').click()
                                        time.sleep(1)
                                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                        try:
                                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                                        except:driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                        da.accept()
                                        time.sleep(3)
                                elif(da.text=='한글 및 영문만 입력 가능합니다.'):
                                        da.accept()
                                        driver.find_element(By.XPATH,'//*[@id="ptxtPrtctorNm"]').click()
                                        driver.find_element(By.XPATH, '//*[@id="ptxtPrtctorNm"]').send_keys(Keys.ARROW_RIGHT)

                                        driver.find_element(By.XPATH,'//*[@id="ptxtPatntRdnmadrDtl"]').send_keys(Keys.ARROW_LEFT)

                                        driver.find_element(By.XPATH,'//*[@id="ptxtSttemntDoctrNm"]').click()
                                        driver.find_element(By.XPATH, '//*[@id="ptxtSttemntDoctrNm"]').send_keys(Keys.ARROW_LEFT)

                                        driver.find_element(By.XPATH,'//*[@id="ptxtPatntNm"]').click()
                                        driver.find_element(By.XPATH, '//*[@id="ptxtPatntNm"]').send_keys(Keys.ARROW_RIGHT)

                                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()

                                        try:
                                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                                        except:
                                                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                        da.accept()
                                        time.sleep(3)
                                elif(da.text=='외국인인 경우, 국적 정보를 기재하여 주시기 바랍니다.'):
                                        da.accept()
                                        time.sleep(3)
                                        country=driver.find_element('//*[@id="ptxtPatntNlty"]')
                                        country.click()
                                        country.send_keys('미상')
                                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()

                                        try:
                                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                                        except:
                                                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                        da.accept()
                                        time.sleep(3)
                                elif(da.text=='코로나바이러스감염증-19의 경우 증상 및 징후를 기재하셔야 합니다.'):
                                        da.accept()
                                        symptoms=driver.find_element(By.XPATH,'//*[@id="ptxtEidsSymptms"]')
                                        symptoms.click()
                                        symptoms.send_keys('.')

                                        driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()

                                        try:
                                                element = WebDriverWait(driver, 2).until(EC.alert_is_present())
                                        except:
                                                driver.find_element(By.XPATH, '//*[@id="pbtnCreateReport"]').click()
                                        da.accept()
                                        time.sleep(3)

                                elif (reported in da.text):
                                        da.accept()
                                        driver.find_element(By.XPATH,'//*[@id="pbtnClose"]').click()
                                        time.sleep(3)
                                        i+=1

                                else:
                                        da.accept()
                                        time.sleep(3)


                else:
                        driver.find_element(By.ID,'sbtnClose').click() #없으면 닫기버튼 누름.
                        time.sleep(3)
                        i+=1




        except :
                driver.quit()