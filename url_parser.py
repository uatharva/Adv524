import requests
from bs4 import BeautifulSoup

tag_student_progs = ' Student Programs'
tag_careers = ' Careers'
url = 'https://www.google.com/search?q='


def parser_requester(company_name):
    try:
        url_string = BeautifulSoup(requests.get(url + company_name + tag_student_progs).content, "html.parser").find('div', {'class': 'kCrYT'}).find_all('a')[0]['href']
        return url_string[7: url_string.index('&')]
    except:
        url_string = BeautifulSoup(requests.get(url + company_name + tag_careers).content, "html.parser").find('div', {
            'class': 'kCrYT'}).find_all('a')[0]['href']
        return url_string[7: url_string.index('&')]
