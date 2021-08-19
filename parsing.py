import requests
from bs4 import BeautifulSoup

URL = 'https://rabota.by/catalog/informacionnye-tehnologii-internet-telekom'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

HOST = 'https://rabota.by'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='vacancy-serp-item vacancy-serp-item_premium', )
    

    vacancy = []
    for item in items:
        activity = item.find('div', class_='vacancy-serp-item-activity')
        if activity:

            vacancy.append({
                'title': item.find('span', class_='resume-search-item__name').get_text(strip=True),
                'link' : item.find('a', class_='bloko-link').get('href')
            })

    print(vacancy)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')



parse()
