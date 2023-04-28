

class PageMeta:

    def __init__(self,soup):
        self.soup = soup
        self.h1 = None
        self.description = None
        self.hreflangs = None
        self.canonical = None
        self.title = None
        self.og_title = None
        self.og_description = None
        self.og_siteName = None
        self.og_image = None
        self.hreflangs_ta = None

    def filler(self,select, get):
            action = self.soup.select(select)
            if len(action)>0:
                return action[0].get(get).replace('//dev.','//').rstrip()
            else:
                return None



    def find_hreflangs(self):
        hreflangs = {'ru-RU': None, 'ru-BY': None, 'ru-KZ': None, 'ru-UA': None, 'ru-TJ': None}
        lang_zones = ['ru-RU', 'ru-BY', 'ru-KZ', 'ru-UA', 'ru-TJ']
        for language in lang_zones:
            l = self.soup.select(f'link[hreflang="{language}"]')
            if len(l) > 0:
                hreflangs[language] = l[0].get('href').replace('//dev.','//')
        self.hreflangs = hreflangs

    def find_meta(self):
        print( self.soup.find('title'))
        self.title = self.soup.find('title').text
        self.h1 = self.soup.find('h1').text
        self.description = self.filler('meta[name="description"]', 'content')
        print(self.description)
        self.canonical = self.filler('link[rel="canonical"]','href')
        self.og_title = self.filler('meta[property="og:title"]','content')
        self.og_description = self.filler('meta[property="og:description"]','content')
        self.og_siteName = self.filler('meta[property="og:site_name"]','content')
        self.og_image = self.filler('meta[property="og:image"]', 'content')


    def find_hreflangs_ta(self):
        hreflangs = {'en': None, 'es': None, 'en-ng': None, 'en-gh': None, 'en-za': None,'en-ke': None, 'en-in': None, 'uk-ua': None, 'en-us': None, 'en-bd': None,'en-zm': None}
        lang_zones = ['en', 'es', 'en-ng', 'en-gh', 'en-za', 'en-ke', 'en-in', 'uk-ua', 'en-us', 'en-bd', 'en-zm']
        for language in lang_zones:
            l = self.soup.select(f'link[hreflang="{language}"]')
            if len(l) > 0:
                hreflangs[language] = l[0].get('href').replace('//dev.','//')
        self.hreflangs = hreflangs