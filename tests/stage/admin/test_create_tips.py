from tests.Pages.Login import Login
from tests.Pages import TipsPage
from playwright.sync_api import Page
import datetime

date = datetime.datetime.now()




def test_create_tips(page:Page):
    login = Login(page)
    login.domain = 'https://meta:meta@stage.metaratings.ru'
    login.authorize_in_nova()
    tips = TipsPage(page)

    page.goto(login.domain+tips.url)



    tips.fill_name('test')
    tips.fill_author()
    tips.fill_picture()
    tips.fill_region(7)
    tips.fill_text_block('FILLEF TIPS')
    tips.fill_tag()
    tips.fill_prematch_block('dsa;dlksa')
    tips.fill_name_for_announce('dalsdl')
    tips.fill_teams()
    tips.fill_koef_fields('2','TEST','Винлайн')
    tips.fill_category()

    page.wait_for_timeout(10000)