import pytest
from tests.Helpers.SoupPage import SoupPage
from playwright.sync_api import Page

meta = 'https://metaratings.ru'
cybersport = 'https://cybersport.metaratings.ru'
kz = 'https://meta-ratings.kz'
def get_news_url(domain):
    news = []
    for n in list(range(3, 10)):
        page = SoupPage(f'{domain}/news/?page={n}')
        soup = page.return_soup(auth=False)
        tags = soup.select('a[class^="NewsItem_newsItem"]')
        for a in tags:
            href = a.get('href')
            if 'mma.' not in href and 'cybersport.' not in href:
                news.append(href)
    return news

@pytest.mark.parametrize('params',get_news_url(meta))
def test_news_dzen_card_meta(params, page:Page):
    page.goto("https://dzen.ru/news/search?issue_tld=ru&text="+ meta + params)
    assert page.get_by_text('Новостей по вашему запросу не найдено').count() == 0

@pytest.mark.parametrize('params',get_news_url(cybersport))
def test_news_dzen_card_cyber(params, page:Page):
    page.goto("https://dzen.ru/news/search?issue_tld=ru&text="+ cybersport + params)
    assert page.get_by_text('Новостей по вашему запросу не найдено').count() == 0




