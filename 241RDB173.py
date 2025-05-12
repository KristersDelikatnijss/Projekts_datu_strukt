import requests
from bs4 import BeautifulSoup

class News:
    def __init__(self, title, link, source):
        self.title = title 
        self.link = link   
        self.source = source 

    def __str__(self):
        return f"{self.title}\nLink: {self.link}\n"

def bbc_news():
    adrese = "http://feeds.bbci.co.uk/news/rss.xml"
    response = requests.get(adrese)
    soup = BeautifulSoup(response.content, "xml")

    items = soup.find_all("item")
    news = []

    for item in items[:15]:
        title = item.title.text
        link = item.link.text
        news.append(News(title, link, "BBC ziņas"))

    return news

def f1_news():
    adrese = "https://www.bbc.com/sport/formula1"
    response = requests.get(adrese)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all('a', class_='ssrcss-mnw9yn-PromoLink')
    news = []
    count = 0 
    for article in articles:
        if count >= 15:
            break
        headline_tag = article.find('p', class_='ssrcss-1b1mki6-PromoHeadline')
        if headline_tag:
            title = headline_tag.get_text(strip=True)
            link = "https://www.bbc.com" + article['href']
            news.append(News(title, link, "BBC F1"))
            count += 1
    
    return news

def print_news():
    bbc = bbc_news()
    f1 = f1_news()
    summary = "Ziņas:\n\n"

    summary += "BBC ziņas:\n"
    for article in bbc:
        summary += str(article) + "\n"

    summary += "F1 ziņas:\n"
    if f1:
        for article in f1:
            summary += str(article) + "\n"
    else:
        summary += "Nevarēja iegūt ziņas par F1.\n"
    print(summary)

if __name__ == "__main__":
    print_news()
