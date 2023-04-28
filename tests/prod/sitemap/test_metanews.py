import select

from tests.Helpers.SoupPage import SoupPageXml
import pytest
import datetime


page = SoupPageXml('https://metaratings.ru/metanews.xml')
soup = page.return_soup()

date = datetime.datetime.now()
date_formated = f'{date.year}-{date.month:02d}-{date.day:02d}'

def test_metanews():
    pub_dates = soup.select('publication_date')
    pub_name = soup.select('name')
    pub_title = soup.select('title')
    pub_language = soup.select('language')
    for i in list(range(0,20)):
        assert pub_dates[i].text == date_formated
        assert pub_language[i].text == 'ru'
        assert len(pub_name[i].text) > 40
        assert len(pub_title[i].text) > 40
