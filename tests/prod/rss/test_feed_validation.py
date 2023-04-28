import pytest
import requests

pages = ['https://metaratings.ru/rss/news/','https://cybersport.metaratings.ru/rss/news/','https://mma.metaratings.ru/rss/news/', 'https://metaratings.by/rss/news/', 'https://meta-ratings.kz/rss/news',
         'https://metaratings.ru/upload/turbo/feed-1.xml',
         'https://metaratings.ru/upload/turbo/feed-2.xml',
         'https://metaratings.ru/upload/turbo/feed-3.xml',
         'https://metaratings.ru/upload/turbo/feed-4.xml',
         'https://metaratings.ru/upload/turbo/feed-27.xml',
         'https://metaratings.ru/upload/turbo/feed-33.xml',
         'https://metaratings.ru/upload/turbo/feed-39.xml',
         'https://metaratings.ru/upload/turbo/feed-45.xml',
         'https://metaratings.ru/upload/turbo/feed-51.xml',
         'https://metaratings.ru/upload/turbo/feed-57.xml',
         'https://metaratings.ru/upload/turbo/feed-63.xml',
         'https://metaratings.ru/upload/turbo/feed-69.xml',
         'https://metaratings.ru/upload/turbo/feed-81.xml',
         'https://cybersport.metaratings.ru//upload/turbo/feed-101.xml',
         'https://mma.metaratings.ru//upload/turbo/feed-100.xml',
         'https://meta-ratings.kz/upload/turbo/feed-9.xml',
'https://meta-ratings.kz/upload/turbo/feed-10.xml',
'https://meta-ratings.kz/upload/turbo/feed-11.xml',
'https://meta-ratings.kz/upload/turbo/feed-12.xml',
'https://meta-ratings.kz/upload/turbo/feed-26.xml',
'https://meta-ratings.kz/upload/turbo/feed-38.xml',
'https://meta-ratings.kz/upload/turbo/feed-44.xml',
'https://meta-ratings.kz/upload/turbo/feed-50.xml',
'https://meta-ratings.kz/upload/turbo/feed-56.xml',
'https://meta-ratings.kz/upload/turbo/feed-62.xml',
'https://meta-ratings.kz/upload/turbo/feed-80.xml',

         ]



@pytest.mark.parametrize('params', pages)
def test_validate_feeds(params):
    res = requests.get(params.replace('https://','https://meta:meta@'))
    assert 'parsererror' not in res.text
    assert res.status_code == 200