import requests
import csv
from bs4 import BeautifulSoup

LINK = input('Enter link of topic from quotefancy.com --> ') or 'https://quotefancy.com/motivational-quotes'


def save_data(result):
    typefile = input('Enter filetype .txt/.csv --> ').lower() or '.txt'
    filename = input('Enter filename --> ') or 'result'
    with open(f'etc\\results\{filename + typefile}', 'w+') as f:
        if typefile == '.csv':
            writer = csv.writer(f, delimiter='\n')
            writer.writerow(result)
        else:
            for el in result:
                f.write(el + '\n')


def getImages(countPages):
    result = []
    for number in countPages:
        link = LINK + f'/page/{str(number)}'
        soup = BeautifulSoup(
            requests.get(link).text, 'lxml')
        for img in soup.find_all('div', {"class": "frame"}):
            try:
                print(link, img.find('img')['src'])
                result.append(img.find('img')['src'])
            except KeyError:
                print(link, img.find('img')['data-original'])
                result.append(img.find('img')['data-original'])
    check = input('Save result? Y/N --> ').lower() or 'y'
    if check == 'y':
        save_data(result)


def start():
    soup = BeautifulSoup(
        requests.get(LINK).text, 'lxml')
    countPages = [1] + [el.get_text() for el in soup.find_all("a", {"class": "page-number"})]
    getImages(countPages)


if __name__ == '__main__':
    start()
