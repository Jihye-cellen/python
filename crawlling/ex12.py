from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time


#네이버 항공권

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) 

browser = webdriver.Chrome(options=options)
browser.maximize_window()

def wait_until(xpath):
  WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
# xpath의 값을 찾을 때까지 기다리게 해주는 식 이 함수를 쓰게 되면 time.sleep()을 강제로 쓰지 않아도 됨 10초 이상은 기다리지 않게 함 (함수로 변형)


browser.get("https://flight.naver.com/")
#e = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]') copy에서 xpath를 복사
e = browser.find_element(By.XPATH, '//button[text()="가는 날"]') #//(전체문서에서 찾겠다). button(버튼에서) [조건에 맞는 것을]
e.click()

#가는 날(28) 클릭
xpath='//b[text()="28"]' 
wait_until(xpath)
es = browser.find_elements(By.XPATH, xpath)
es[0].click()

#오는 날(30) 클릭
xpath = '//b[text()="30"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH, xpath)
es[0].click()

#도착버튼클릭
xpath = '//b[text()="도착"]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#국내클릭
xpath = '//button[text()="국내"]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#제주국제공항클릭 contains 함수는 어떠한 단어를 포함하고 있을때 사용가능 
xpath = '//i[contains(text(),"제주국제공항")]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

xpath = '//span[contains(text(), "검색")]'
wait_until(xpath)

#항공권검색
xpath = '//span[contains(text(), "검색")]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

first = '//*[@id="container"]/div[5]/div/div[3]/div[1]/div'
wait_until(first)
e = browser.find_element(By.XPATH, first)
#print(e.text)

#검색목록
es = browser.find_elements(By.XPATH, '//*[contains(@class,"concurrent_ConcurrentItemContainer__NDJda")]')
es = es[:10]
for e in es:
  print(e.text)
  print('-' * 50)
print("전체검색수:", len(es))

browser.quit()