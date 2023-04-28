import pytest
import csv
from tests.Helpers.SoupPage import SoupPage
import requests

file = open('amp.csv','r')

data = list(csv.reader(file,delimiter=';'))
pages = []
for d in data:
    pages.append(d[0])

@pytest.mark.parametrize('params',pages)
def test_amp_tag_on_page(params):
    page = SoupPage(params)
    soup = page.return_soup()
    amp = soup.select('link[rel="amphtml"]')
    amp_href = amp[0].get('href')
    assert len(amp) == 1
    assert requests.get(amp_href,auth=('meta','meta')).status_code == 200
    assert amp_href.replace('/amp/','/') == params