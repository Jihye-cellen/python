import requests
from bs4 import BeautifulSoup
import re #정규식 어떤 이름으로 지정된 것을 가져오겠다.

#쿠팡 노트북 검색 후 1페이지 데이터
#전체 반복도 가능 (page 안에 중괄호를 넣어놓고, .format(i) 변수를 지정해준다. ) /index는 아예 페이지가 넘어갈 때 새로 된다. 
for i in range(1,6):    
    url ='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor='.format(i)

#보통 데이터 무단수집 방지를 위해 user-agent string을 이용해야 하며, 한글을 설정해줘야한다. 
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    }
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'lxml')

    es= soup.find_all('li', attrs={'class': re.compile('^search-product')})
    for index, e in enumerate(es):
        title = e.find('div', attrs={'class': 'name'}).get_text().strip()
        price = e.find('strong', attrs={'class': 'price-value'}).get_text()
        #print(index+1, title, price)

    #애플제외, 리뷰100개이상, 평점 5.0 이상 제품만 출력
    index = 0
    for e in es:
        title = e.find('div', attrs={'class': 'name'}).get_text().strip()
        price = e.find('strong', attrs={'class': 'price-value'}).get_text()
        if 'Apple' in title:
            continue #continue를 하면 값을 넘겨버림
        count = e.find('span', attrs={'class': 'rating-total-count'})
        if count:
            count = count.get_text().strip()    #count가 0이면 콘솔에서 오류가 나므로 if문으로 해결
        else:
            continue   #continue를 사용하면 출력 자체가 안되고, count=0으로 쓰면 전부 출력됨
        count = int(count[1:-1]) #괄호제거(slice)    
        if count < 200:  #평점 수 200개 이상만 출력
            continue

        rating = e.find('em', attrs={'class': 'rating'})
        if rating:
            rating = rating.get_text()
        else:
            continue

        rating = float(rating) #실수변환
        if rating < 5.0: #5.0이상만 출력
            continue

        index += 1
        print(index, title)
        print("가격: ", price)
        print('평점수: ', count)
        print("평점: ", rating)
        print("-" * 80)

