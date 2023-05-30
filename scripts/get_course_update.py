import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_course():

    ua = UserAgent()
    URL = 'https://www.alta.ru/currency/'
    response = requests.get(URL, headers={'User-agent': ua.random})

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('div', class_='module-tableSort')
    rows = table.findAll('tr')
    my_dict = {}

    for row in rows:
        if row.find('td', 't-left') and row.find('td', 't-right'):
            k_i = row.find('td', 't-left').text.index('\n')
            k = row.find('td', 't-left').text[:k_i]
            v = row.find('td', 't-right').text.strip('\n')
            my_dict[k.strip('\n')] = v
    return my_dict

if __name__ == '__main__':
    for item in get_course().items():
        print(item)