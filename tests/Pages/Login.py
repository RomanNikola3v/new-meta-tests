from playwright.sync_api import Page


class Login:

    def __init__(self,page):
        self.login = 'roman.nikolaev@brl.ru'
        self.password = 'nDPxU76BkR'
        self.domain = 'https://meta:meta@stage.metaratings.ru'
        self.page = page



    def authorize_in_nova(self):
        self.page.goto(f'{self.domain}/nova')
        self.page.locator("input[name=\"email\"]").click()

        self.page.locator("input[name=\"email\"]").fill(self.login)
        self.page.locator("input[name=\"password\"]").click()
        self.page.locator("input[name=\"password\"]").fill(self.password)
        self.page.locator("text=Авторизоваться").click()
