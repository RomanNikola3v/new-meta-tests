import pytest, requests

from tests.Helpers.SoupPage import SoupPage, SoupPageXml

meta = 'https://metaratings.ru'
mma = 'https://mma.metaratings.ru'
cybersport = 'https://cybersport.metaratings.ru'
def get_news_url(domain):
    news = []
    for n in list(range(1, 5)):
        page = SoupPage(f'{domain}/news/?page={n}')
        soup = page.return_soup(auth=False)
        tags = soup.select('a[class^="NewsItem_newsItem"]')
        for a in tags:
            href = a.get('href')
            if 'mma.' not in href and 'cybersport.' not in href:
                news.append(href)
    return news

def get_rss_links_text(url):
    page = SoupPageXml(url)
    soupmeta = page.return_soup()
    links = soupmeta.select(f'link')
    only_url = []
    for link in links:
        only_url.append(link.text)
    return only_url

only_url_meta = get_rss_links_text('https://metaratings.ru/rss/news/')
only_url_mma = get_rss_links_text('https://mma.metaratings.ru/rss/news/')
only_url_cybersport = get_rss_links_text('https://cybersport.metaratings.ru/rss/news/')

@pytest.mark.parametrize('params', get_news_url(meta))
def test_news_in_rss(params):
    assert f'{meta}{params}' in only_url_meta

@pytest.mark.parametrize('params', get_news_url(mma))
def test_news_in_rss_mma(params):
    assert f'{mma}{params}' in only_url_mma

@pytest.mark.parametrize('params', get_news_url(cybersport))
def test_news_in_rss_cybersport(params):
    assert f'{cybersport}{params}' in only_url_cybersport

