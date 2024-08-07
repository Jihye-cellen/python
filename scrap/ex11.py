import requests
from bs4 import BeautifulSoup
import re

query="춘식이"
url = "https://www.google.com/search?sca_esv=0938baf10882972d&sca_upv=1&hl=ko&sxsrf=ADLYWIKfKKN3cQ4idR4iA_9gTzzdQshcvQ:1722991634806&q={}&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ9zKNKSjpwusJM2dYWg4btGKvTs8msUkFt41RLL2EsYFXj1HJ-6Tz3zY-OaA8p5OIwKXtepe1nwMbiobd8aopYI3Djq-_wHNSyqi1J5rXtrZ-dEOjuJfkJpxXj8pUC3HmGzP_4yQ_xdzK9qDO3vbGQ9OKpWceCh1Pu2_RMxyWEg0WL5jtkA&sa=X&ved=2ahUKEwiXy9-C1OGHAxVlha8BHRMoFpUQtKgLegQIHBAB&biw=1920&bih=953&dpr=1".format(query)

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
}

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

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
    