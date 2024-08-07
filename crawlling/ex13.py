from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless') #브라우저 실행 안해도 데이터를 크롤링 할 수 있음
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36') 
#로봇이 한다고 착각할 수 있어서 headless를 줘야하는 경우에는 사용해야함 
options.add_experimental_option('detach', True)
browser= webdriver.Chrome(options=options)
browser.maximize_window()

query ='춘식이'
url='https://www.google.com/search?sca_esv=0938baf10882972d&sca_upv=1&hl=ko&sxsrf=ADLYWIKfKKN3cQ4idR4iA_9gTzzdQshcvQ:1722991634806&q={}&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ9zKNKSjpwusJM2dYWg4btGKvTs8msUkFt41RLL2EsYFXj1HJ-6Tz3zY-OaA8p5OIwKXtepe1nwMbiobd8aopYI3Djq-_wHNSyqi1J5rXtrZ-dEOjuJfkJpxXj8pUC3HmGzP_4yQ_xdzK9qDO3vbGQ9OKpWceCh1Pu2_RMxyWEg0WL5jtkA&sa=X&ved=2ahUKEwiXy9-C1OGHAxVlha8BHRMoFpUQtKgLegQIHBAB&biw=1920&bih=953&dpr=1'.format(query)
browser.get(url)

#prev_height = browser.execute_script('return document.body.scrollHeight') #body에 있는 정보들의 높이를 스크롤 해서 갯수세기
#browser.execute_script('alert("{}")'.format(prev_height)) #자바스크립트로도 구현 가능

prev_height = browser.execute_script('return document.body.scrollHeight')#이전 스크롤
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') #스크롤을 조작
    time.sleep(2) #2초마다 내려가기
    curr_height = browser.execute_script('return document.body.scrollHeight') #현재 스크롤
    if prev_height == curr_height:
        print('스크롤 완료!')
        break
    prev_height = curr_height

    
import re #같이 사용가능
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

with open('data/image.html', 'w', encoding='utf-8') as file: 
    file.write(soup.prettify()) #prettify() 이쁘게 출력

es = soup.find_all('div', attrs={'class': re.compile('^eA0Zlc')})
print(len(es))
for index, e in enumerate(es):
    title = e.find('div', attrs={'class': 'toI8Rb OSrXXb'})
    image = e.find('img')['src']
    print(index+1, title.get_text())
    print(image)
    print('-' *80)





