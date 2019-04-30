import requests
from bs4 import BeautifulSoup
import datetime
import time

while True:
    now = datetime.datetime.now()
    time_now = now.hour, now.minute, now.second
    time.sleep(1)
    print(time_now)

    if time_now == (19, 0, 0):
        url = requests.get("https://www.upi.com/Odd_News/")
        print(url.status_code)
        src = url.content
        soup = BeautifulSoup(src, 'lxml')
        article = ""
        header = ""
        text_clean = []
        file = open("news.txt", "w")

        data = soup.find_all('div', attrs={'class': 'row story list'})

        for div in data:
            links = div.find('a')
            article = links.attrs['href']

        print(article)

        url = requests.get(article)
        art = url.content
        article_soup = BeautifulSoup(art, 'lxml')
        print(article_soup)

        header = article_soup.find('h1', {'class': 'headline montserrat bold'})
        header_clean = header.get_text()

        body = article_soup.find('article')
        text = body.findAll('p')
        for text in text:
            text_clean.append(text.get_text())

        file.writelines(header_clean + '\n' + '\n' + '\n')
        for p in text_clean:
            file.writelines(p + '\n' + '\n')
        file.write(article + '\n' + '\n' + '\n')
        file.close()
        time.sleep(5)

