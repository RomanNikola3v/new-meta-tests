from bs4 import BeautifulSoup
import requests


class SoupPage:
    def __init__(self, url):
        self.soup = None
        self.url = url
        self.response = None


    def return_soup(self,auth=True):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36',
            'X-Meta-QA': 'qa-2023'


        }
        if auth == True:
            self.response = requests.get(self.url, auth=('meta','meta'), headers=headers)
        else:
            self.response = requests.get(self.url, headers=headers)

        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        return self.soup


class SoupPageXml:
    def __init__(self,url):
        self.soup = None
        self.url = url

    def return_soup(self):
        res = requests.get(self.url)
        self.soup = BeautifulSoup(res.content,features='lxml-xml')
        return self.soup


