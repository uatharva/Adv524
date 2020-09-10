import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import urllib
import re
from bs4.element import Comment
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from mechanize import Browser

browser = webdriver.Firefox()

mech = Browser()
url = "http://www.biggestuscities.com/top-1000"
page = mech.open(url)
html = page.read()
soup = BeautifulSoup(html)
all_locations = []
for row in soup.find("table").findAll('a', {'class': 'link'}):
    if '/city/' in row['href']:
        all_locations.append(row.text.strip())

locations = ' office locations '
tag_careers = ' locations '
URL = 'https://www.google.com/search?q='


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def location_parser(company_name):
    final_list = []
    try:
        url = BeautifulSoup(requests.get(URL + company_name + locations).content, "html.parser").find('div', {
            'class': 'kCrYT'}).find_all('a')[0]['href']
        url = url[7: url.index('&')]
        print(url)
        page = BeautifulSoup(requests.get(url, headers={'User-Agent': ua.chrome}).content, "html.parser").find_all(
            text=True)
        visible_texts = filter(tag_visible, page)
        visible_texts = u" ".join(t.strip() for t in visible_texts)
        print(visible_texts)
        for t in all_locations:
            if t in visible_texts:
                final_list.append(t)

        print(final_list)
    except:
        url = BeautifulSoup(requests.get(URL + company_name + tag_careers).content, "html.parser").find('div', {
            'class': 'kCrYT'}).find_all('a')[0]['href']
        url = url[7: url.index('&')]
        print(url)
        page = BeautifulSoup(requests.get(url).content, "html.parser").find_all(text=True)
        visible_texts = filter(tag_visible, page)
        visible_texts = u" ".join(t.strip() for t in visible_texts)
        print(visible_texts)
        for t in all_locations:
            if t in visible_texts:
                final_list.append(t)

        print(final_list)
