import requests
from bs4 import BeautifulSoup


def crawl_page(page, web_url):
    link = web_url.replace("$PAGE", str(page))
    code = requests.get(link)
    plain = code.text
    soup = BeautifulSoup(plain, "html.parser")
    return soup


def beautiful_soup(soup):
    return BeautifulSoup(soup, "html.parser")
