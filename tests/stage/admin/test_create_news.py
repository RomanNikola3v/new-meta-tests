from tests.Pages.Login import Login
from tests.Pages.NewsPage import NewsPage
from playwright.sync_api import Page
import datetime

date = datetime.datetime.now()

def test_create_news_all_regions(page:Page):
    login = Login(page)
    login.domain = 'https://meta:meta@stage.metaratings.ru'
    login.authorize_in_nova()

    news = NewsPage(page)

    #open news creation page
    page.goto(f'{login.domain}{news.url}')

    #name of element
    name = f"ALL regions test news with any amount of charachters {date}"
    news.fill_name(name)
    #announce picture
    news.fill_picture()

    #cheсk all checkboxes
    news.fill_all_checkboxes()

    #fill an Author
    news.fill_author()

    #fill source
    # Click [data-testid="sources-search-input"] div >> nth=2
    news.fill_source()

    #fill announce
    # Click text=Анонс Кол-во символов: 0 >> textarea
    news.fill_announce(
        "ALL Character and word limits are quite common these days on the Internet. The one that most people are likely aware of is the 140 character limit for tweets ")


    #fill milimum text content
    news.fill_text_block('FILLED')

    #fill tag
    news.fill_tag()
    #fill category

    news.fill_category()

    #check_regions
    news.fill_region(0)
    news.fill_region(2)
    news.fill_region(3)
    news.fill_region(1)
    news.press_save_and_wait()


    #assert created

    page.goto(login.domain+'/news')
    page.locator(f'[text="{name}"]').is_visible()



def test_create_news_ru(page:Page):
    login = Login(page)
    login.domain = 'https://meta:meta@stage.metaratings.ru'
    login.authorize_in_nova()

    news = NewsPage(page)

    #open news creation page
    page.goto(f'{login.domain}{news.url}')

    #name of element
    name = f"RU test news with any amount of charachters {date}"
    news.fill_name(name)
    #announce picture
    news.fill_picture()

    #cheсk all checkboxes
    news.fill_all_checkboxes()

    #fill an Author
    news.fill_author()

    #fill source
    # Click [data-testid="sources-search-input"] div >> nth=2
    news.fill_source()

    #fill announce
    # Click text=Анонс Кол-во символов: 0 >> textarea
    news.fill_announce(
        "RU Character and word limits are quite common these days on the Internet. The one that most people are likely aware of is the 140 character limit for tweets ")


    #fill milimum text content
    news.fill_text_block('FILLED')

    #fill tag
    news.fill_tag()
    #fill category

    news.fill_category()

    #check_regions
    news.fill_region(0)

    news.press_save_and_wait()


    #assert created

    page.goto(login.domain+'/news')
    page.locator(f'[text="{name}"]').is_visible()

def test_create_news_kz(page:Page):
    login = Login(page)
    login.domain = 'https://meta:meta@stage.metaratings.ru'
    login.authorize_in_nova()

    news = NewsPage(page)

    #open news creation page
    page.goto(f'{login.domain}{news.url}')

    #name of element
    name = f"KZ test news with any amount of charachters {date}"
    news.fill_name(name)
    #announce picture
    news.fill_picture()

    #cheсk all checkboxes
    news.fill_all_checkboxes()

    #fill an Author
    news.fill_author()

    #fill source
    # Click [data-testid="sources-search-input"] div >> nth=2
    news.fill_source()

    #fill announce
    # Click text=Анонс Кол-во символов: 0 >> textarea
    news.fill_announce(
        "KZ Character and word limits are quite common these days on the Internet. The one that most people are likely aware of is the 140 character limit for tweets ")


    #fill milimum text content
    news.fill_text_block('FILLED')

    #fill tag
    news.fill_tag()
    #fill category

    news.fill_category()

    #check_regions
    news.fill_region(3)



    news.press_save_and_wait()


    #assert created

    page.goto(login.domain+'/news')
    page.locator(f'[text="{name}"]').is_visible()