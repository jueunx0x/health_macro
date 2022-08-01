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

def check_exists_by_XPATH(xpath):
    try:
        driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        return False
    return True


url = "https://www.naver.com"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#driver = webdriver.Chrome(options=options)
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get(url)  # driver실행
time.sleep(3)

search_box=check_exists_by_XPATH('//*[@id="query"]')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "query")))

driver.find_element(By.XPATH,'//*[@id="query"]').click()
driver.find_element(By.XPATH,'//*[@id="query"]').send_keys('flowerforyou')
driver.find_element(By.XPATH,'//*[@id="query"]').send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loc-main-section-root")))
driver.find_element(By.XPATH,'//*[@id="loc-main-section-root"]/section/div/ul/li[2]/div[2]/a[1]/div/div/span[1]').click()
for i in range (50):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="web_1"]/div/div[2]/div[2]/a')))
    driver.find_element(By.XPATH,'//*[@id="web_1"]/div/div[2]/div[2]/a').click()

    driver.switch_to.window(driver.window_handles[1])
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
driver.quit()
