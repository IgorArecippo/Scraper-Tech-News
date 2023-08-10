import requests
import time
from parsel import Selector
BASE_URL = "https://blog.betrybe.com"


# Requisito 1
def fetch(url):
    headers = {
        "user-agent": "Fake user-agent"
    }

    try:
        res = requests.get(url, header=headers, timeout=3)
        time.sleep(1)

        if res.status_code == 200:
            return res.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news = selector.css(".entry-title a::attr(href)").getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css("a.next::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    news = {
        'url': selector.css('link[rel=canonical]::attr(href)').get(),
        'title': selector.css('h1.entry-title::text').get().strip(),
        'timestamp': selector.css('li.meta-date::text').get().strip(),
        'writer': selector.css(
            'li.meta-author span.author a::text').get().strip(),
        'reading_time': int(selector.css(
            '.meta-reading-time::text').re_first(r'\d+')),
        'summary': "".join(selector.css(
            'div.entry-content > p:first-of-type *::text').getall()).strip(),
        'category': selector.css('span.label::text').get().strip()
    }

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
