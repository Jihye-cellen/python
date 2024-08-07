from flask import Blueprint, render_template
import json

bp = Blueprint('scrap', __name__, url_prefix='/scrap')

@bp.route('/movie.json')
def scrap_movie():
    import requests
    from bs4 import BeautifulSoup
    
    url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    es = soup.find('div', attrs={'class': 'sect-movie-chart'}).find_all('li', limit=12)
    items=[]
    for e in es:
        rank= e.find('strong', attrs={'class': 'rank'}).get_text()
        title= e.find('strong', attrs={'class': 'title'}).get_text()
        img = e.find('img')['src']
        date = e.find('span', attrs={'class': 'txt-info'}).get_text().strip()[0:10]
        link = e.find('a', attrs={'class': 'link-reservation'})['href']
        link = "http://www.cgv.co.kr" + link
        percent = e.find('strong', attrs={'class': 'percent'}).get_text()

        data = {'rank': rank, 'title': title, 'image': img, 'date':date, 'link': link, 'percent':percent}
        items.append(data)

    with open('static/data/movie.json', 'w', encoding='utf-8') as file:
        json.dump(items, file, indent='\t', ensure_ascii=False)

    return items
    




@bp.route('/movie')
def movie():
    return render_template('index.html', title='무비차트', pageName='scrap/movie.html')


@bp.route('/finance')
def finance():
    return render_template('index.html', title='시가총액', pageName='scrap/finance.html')

@bp.route('/finance.json')
def scrap_finance():
    #csv => json 변환
    import csv
    import json
    data=[]
    with open('static/data/코스피거래시가총액.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    return json_data