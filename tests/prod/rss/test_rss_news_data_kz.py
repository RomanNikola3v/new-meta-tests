import requests
from tests.Helpers.SoupPage import SoupPageXml
import pytest
from email.utils import parsedate

page = 'https://meta-ratings.kz/rss/news/'

soup = SoupPageXml(page).return_soup()


titles = soup.select('title')
links = soup.select('link')
amplinks = soup.select('amplink')
descriptions = soup.select('description')
pubDates = soup.select('pubDate')
authors = soup.select('author')
enclosures = soup.select('enclosure')
genres = soup.select('genre')
texts = soup.select('full-text')

print(titles)
p = list(range(0,20))


@pytest.mark.parametrize('params',p)
def test_rss_fields_kz(params):
    assert len(titles[params+1].text) >= 30
    res1 = requests.get(links[params+1].text)
    assert res1.status_code == 200
    res2 = requests.get(amplinks[params + 1].text)
    assert '/amp/' in amplinks[params].text
    assert res2.status_code == 200
    assert len(descriptions[params+1].text) >= 140
    assert len(authors[params].text) > 5
    assert genres[params].text == 'message' or genres[params].text == 'article'
    assert len(texts[params].text) > 100
    isset = parsedate(pubDates[params].text)
    print(type(isset))
    assert type(isset) is tuple