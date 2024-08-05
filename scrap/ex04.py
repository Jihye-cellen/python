import requests
from bs4 import BeautifulSoup

#cgv 스크래핑
url ='http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)
#print(res.text)

#with open('cgv.html', 'w', encoding='utf-8') as file:
    #file.write(res.text)

soup =BeautifulSoup(res.text , 'lxml')
title = soup.title
print(title.get_text())

movie = soup.find('div', attrs={'class': 'sect-movie-chart'})
movies = movie.find_all('li')
#print(len(movies))
for index, m in enumerate(movies):
    title = m.find('strong', attrs={'class': 'title'}).get_text()
    poster = m.find('img').attrs['src']
    link = m.find('a', attrs={'class': 'link-reservation'})['href']
    date = m.find('span', attrs={'class': 'txt-info'}).find('strong').get_text().lstrip()
    percent = m.find('strong', attrs={'class': 'percent'}).get_text()
    print(str(index+1), title)
    print(poster)
    print("개봉일 : " + date[0:10])
    print('http://www.cgv.co.kr' + link)
    print(percent)
    print('-' * 80)

