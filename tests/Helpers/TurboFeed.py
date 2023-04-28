

class TurboFeed:
    def __init__(self,soup):
        self.items = soup.select('item[turbo="true"]')
        self.titles = soup.select('title')
        self.turbo_title = self.titles[0].text

        self.descriptions = soup.select('description')
        self.feed_description = self.descriptions[0].text

        self.topics = soup.select('topic')

        self.analytics = soup.select('analytics')
        self.yandex_analytics_id = self.analytics[1].get('id')
        self.yandex_analytics_type = self.analytics[1].get('type')
        self.google_analytics_id = self.analytics[0].get('id')
        self.google_analytics_type = self.analytics[0].get('type')

        self.pubDates = soup.select('pubDate')
        self.categories = soup.select('category')
        self.authors = soup.select('author')
        self.contents = soup.select('content')
        self.end_of_range = None

    def test_range(self):
        if len(self.items) < 10:
            self.end_of_range = len(self.items) - 1
        else:
            self.end_of_range = 10

class Sitemap:
    def __init__(self,soup):
        self.pages = soup.select('loc')