from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #detach를 지정시에는 time.sleep을 실행하지 않아도 계속 창이 떠있음

browser = webdriver.Chrome(options=options)
browser.maximize_window() #창이 뜰시 화면 가득 차는 옵션 minimize는 작게 하는 옵션

browser.get("https://www.naver.com/") #브라우저 실행
e = browser.find_element(By.ID, 'query') #브라우저 검색창의 아이디 지정
e.send_keys('나도코딩') #keys로 입력가능/ 조정도 가능
time.sleep(2)
e.send_keys(Keys.ENTER)
time.sleep(5)

browser.quit() #broser꺼짐

#time.sleep(60*60) 한시간동안 켜져있음


