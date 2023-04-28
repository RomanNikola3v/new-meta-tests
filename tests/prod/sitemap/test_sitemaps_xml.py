from tests.Helpers.SoupPage import SoupPageXml
import pytest

meta = ['https://metaratings.ru/sitemap-files.xml', 'https://metaratings.ru/sitemap-news.xml', 'https://metaratings.ru/sitemap-article-bookmakers.xml', 'https://metaratings.ru/sitemap-tips.xml', 'https://metaratings.ru/sitemap-bookmakers.xml', 'https://metaratings.ru/sitemap-bonuses.xml', 'https://metaratings.ru/sitemap-authors.xml', 'https://metaratings.ru/sitemap-bonus-properties.xml', 'https://metaratings.ru/sitemap-bookmaker-ratings.xml', 'https://metaratings.ru/sitemap-bonus-seo-filters.xml', 'https://metaratings.ru/sitemap-article-blogs.xml', 'https://metaratings.ru/sitemap-article-sports-histories.xml', 'https://metaratings.ru/sitemap-article-sports-terms.xml', 'https://metaratings.ru/sitemap-article-healths.xml', 'https://metaratings.ru/sitemap-article-lottery-articles.xml', 'https://metaratings.ru/sitemap-article-bets.xml', 'https://metaratings.ru/sitemap-article-articles-bets.xml', 'https://metaratings.ru/sitemap-article-sport-events.xml', 'https://metaratings.ru/sitemap-article-ranges.xml', 'https://metaratings.ru/sitemap-article-bets-strategies.xml', 'https://metaratings.ru/sitemap-article-content-pages.xml', 'https://metaratings.ru/sitemap-article-betting-schools.xml', 'https://metaratings.ru/sitemap-article-bookmakers-worlds.xml', 'https://metaratings.ru/sitemap-article-cappers-ratings.xml', 'https://metaratings.ru/sitemap-article-lottery-news.xml', 'https://metaratings.ru/sitemap-article-lottery-ratings.xml', 'https://metaratings.ru/sitemap-category-blogs.xml', 'https://metaratings.ru/sitemap-category-tips.xml', 'https://metaratings.ru/sitemap-category-news.xml', 'https://metaratings.ru/sitemap-category-sports-histories.xml', 'https://metaratings.ru/sitemap-category-page-totals.xml', 'https://metaratings.ru/sitemap-category-lottery-ratings.xml', 'https://metaratings.ru/sitemap-category-bookmakers-worlds.xml']
mma = ['https://mma.metaratings.ru/sitemap-files.xml', 'https://mma.metaratings.ru/sitemap-tips.xml', 'https://mma.metaratings.ru/sitemap-news.xml', 'https://mma.metaratings.ru/sitemap-authors.xml', 'https://mma.metaratings.ru/sitemap-category-sports-ratings.xml', 'https://mma.metaratings.ru/sitemap-article-blogs.xml', 'https://mma.metaratings.ru/sitemap-article-videos.xml']
cybersport = ['https://cybersport.metaratings.ru/sitemap-files.xml', 'https://cybersport.metaratings.ru/sitemap-tips.xml', 'https://cybersport.metaratings.ru/sitemap-news.xml', 'https://cybersport.metaratings.ru/sitemap-authors.xml', 'https://cybersport.metaratings.ru/sitemap-people.xml', 'https://cybersport.metaratings.ru/sitemap-article-blogs.xml', 'https://cybersport.metaratings.ru/sitemap-article-sports-ratings.xml', 'https://cybersport.metaratings.ru/sitemap-article-wikis.xml', 'https://cybersport.metaratings.ru/sitemap-article-schools.xml', 'https://cybersport.metaratings.ru/sitemap-article-guides.xml', 'https://cybersport.metaratings.ru/sitemap-article-events.xml', 'https://cybersport.metaratings.ru/sitemap-article-cosplays.xml', 'https://cybersport.metaratings.ru/sitemap-article-games.xml', 'https://cybersport.metaratings.ru/sitemap-article-teams.xml', 'https://cybersport.metaratings.ru/sitemap-article-cheats.xml', 'https://cybersport.metaratings.ru/sitemap-article-mems.xml', 'https://cybersport.metaratings.ru/sitemap-article-videos.xml', 'https://cybersport.metaratings.ru/sitemap-article-lives.xml']
kz = ['https://meta-ratings.kz/sitemap-files.xml', 'https://meta-ratings.kz/sitemap-news.xml', 'https://meta-ratings.kz/sitemap-article-bookmakers.xml', 'https://meta-ratings.kz/sitemap-tips.xml', 'https://meta-ratings.kz/sitemap-bookmakers.xml', 'https://meta-ratings.kz/sitemap-bonuses.xml', 'https://meta-ratings.kz/sitemap-authors.xml', 'https://meta-ratings.kz/sitemap-bonus-properties.xml', 'https://meta-ratings.kz/sitemap-bookmaker-ratings.xml', 'https://meta-ratings.kz/sitemap-bonus-seo-filters.xml', 'https://meta-ratings.kz/sitemap-article-blogs.xml', 'https://meta-ratings.kz/sitemap-article-sports-histories.xml', 'https://meta-ratings.kz/sitemap-article-sports-terms.xml', 'https://meta-ratings.kz/sitemap-article-lottery-articles.xml', 'https://meta-ratings.kz/sitemap-article-bets.xml', 'https://meta-ratings.kz/sitemap-article-articles-bets.xml', 'https://meta-ratings.kz/sitemap-article-sport-events.xml', 'https://meta-ratings.kz/sitemap-article-ranges.xml', 'https://meta-ratings.kz/sitemap-article-bets-strategies.xml', 'https://meta-ratings.kz/sitemap-article-content-pages.xml', 'https://meta-ratings.kz/sitemap-article-betting-schools.xml', 'https://meta-ratings.kz/sitemap-article-cappers-ratings.xml', 'https://meta-ratings.kz/sitemap-article-lottery-ratings.xml', 'https://meta-ratings.kz/sitemap-category-blogs.xml', 'https://meta-ratings.kz/sitemap-category-tips.xml', 'https://meta-ratings.kz/sitemap-category-news.xml', 'https://meta-ratings.kz/sitemap-category-sports-histories.xml', 'https://meta-ratings.kz/sitemap-category-page-totals.xml', 'https://meta-ratings.kz/sitemap-category-lottery-ratings.xml']
by = ['https://metaratings.by/sitemap-files.xml', 'https://metaratings.by/sitemap-news.xml', 'https://metaratings.by/sitemap-article-bookmakers.xml', 'https://metaratings.by/sitemap-tips.xml', 'https://metaratings.by/sitemap-bookmakers.xml', 'https://metaratings.by/sitemap-bonuses.xml', 'https://metaratings.by/sitemap-authors.xml', 'https://metaratings.by/sitemap-bonus-properties.xml', 'https://metaratings.by/sitemap-bookmaker-ratings.xml', 'https://metaratings.by/sitemap-bonus-seo-filters.xml', 'https://metaratings.by/sitemap-article-blogs.xml', 'https://metaratings.by/sitemap-article-sports-histories.xml', 'https://metaratings.by/sitemap-article-sports-terms.xml', 'https://metaratings.by/sitemap-article-lottery-articles.xml', 'https://metaratings.by/sitemap-article-bets.xml', 'https://metaratings.by/sitemap-article-articles-bets.xml', 'https://metaratings.by/sitemap-article-sport-events.xml', 'https://metaratings.by/sitemap-article-ranges.xml', 'https://metaratings.by/sitemap-article-bets-strategies.xml', 'https://metaratings.by/sitemap-article-content-pages.xml', 'https://metaratings.by/sitemap-article-betting-schools.xml', 'https://metaratings.by/sitemap-article-cappers-ratings.xml', 'https://metaratings.by/sitemap-article-lottery-news.xml', 'https://metaratings.by/sitemap-article-lottery-ratings.xml', 'https://metaratings.by/sitemap-category-blogs.xml', 'https://metaratings.by/sitemap-category-tips.xml', 'https://metaratings.by/sitemap-category-news.xml', 'https://metaratings.by/sitemap-category-sports-histories.xml', 'https://metaratings.by/sitemap-category-page-totals.xml', 'https://metaratings.by/sitemap-category-lottery-ratings.xml']
tj = ['https://metaratings.tj/sitemap-files.xml', 'https://metaratings.tj/sitemap-news.xml', 'https://metaratings.tj/sitemap-article-bookmakers.xml', 'https://metaratings.tj/sitemap-tips.xml', 'https://metaratings.tj/sitemap-bookmakers.xml', 'https://metaratings.tj/sitemap-bonuses.xml', 'https://metaratings.tj/sitemap-authors.xml', 'https://metaratings.tj/sitemap-bonus-properties.xml', 'https://metaratings.tj/sitemap-bookmaker-ratings.xml', 'https://metaratings.tj/sitemap-bonus-seo-filters.xml', 'https://metaratings.tj/sitemap-article-blogs.xml', 'https://metaratings.tj/sitemap-article-sports-histories.xml', 'https://metaratings.tj/sitemap-article-sports-terms.xml', 'https://metaratings.tj/sitemap-article-lottery-articles.xml', 'https://metaratings.tj/sitemap-article-bets.xml', 'https://metaratings.tj/sitemap-article-articles-bets.xml', 'https://metaratings.tj/sitemap-article-sport-events.xml', 'https://metaratings.tj/sitemap-article-ranges.xml', 'https://metaratings.tj/sitemap-article-bets-strategies.xml', 'https://metaratings.tj/sitemap-article-content-pages.xml', 'https://metaratings.tj/sitemap-article-betting-schools.xml', 'https://metaratings.tj/sitemap-article-cappers-ratings.xml', 'https://metaratings.tj/sitemap-article-lottery-news.xml', 'https://metaratings.tj/sitemap-article-lottery-ratings.xml', 'https://metaratings.tj/sitemap-category-blogs.xml', 'https://metaratings.tj/sitemap-category-tips.xml', 'https://metaratings.tj/sitemap-category-news.xml', 'https://metaratings.tj/sitemap-category-sports-histories.xml', 'https://metaratings.tj/sitemap-category-page-totals.xml', 'https://metaratings.tj/sitemap-category-lottery-ratings.xml']
ta = ['https://www.telecomasia.net/sitemap-files.xml','https://www.telecomasia.net/122.xml', 'https://www.telecomasia.net/123.xml','https://www.telecomasia.net/123.part1.xml','https://www.telecomasia.net/126.xml','https://www.telecomasia.net/128.xml','https://www.telecomasia.net/129.xml','https://www.telecomasia.net/131.xml','https://www.telecomasia.net/135.xml','https://www.telecomasia.net/136.xml','https://www.telecomasia.net/141.xml','https://www.telecomasia.net/142.xml','https://www.telecomasia.net/157.xml','https://www.telecomasia.net/198.xml']


def get_loc_text(url):
    page = SoupPageXml(url + '/sitemap.xml')
    soup = page.return_soup()
    links = []
    locs = soup.select('loc')
    for loc in locs:
        links.append(loc.text)
    return links

def test_meta_sitemap(domain):
    assert get_loc_text(domain.meta) == meta

def test_meta_sitemap_mma(domain):
    assert get_loc_text(domain.mma) == mma

def test_meta_sitemap_cybersport(domain):
    assert get_loc_text(domain.cybersport) == cybersport

def test_meta_sitemap_kz(domain):
    assert get_loc_text(domain.kz) == kz

def test_meta_sitemap_by(domain):
    assert get_loc_text(domain.by) == by

def test_meta_sitemap_tj(domain):
    assert get_loc_text(domain.tj) == tj

def test_ta_sitemap_en(domain):
    assert get_loc_text(domain.ta) == ta
