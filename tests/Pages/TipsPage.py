from tests.Pages.Page import AdminPage


class TipsPage(AdminPage):

    def __init__(self,page):
        self.page = page
        self.url = "/nova/resources/tips/new"

    def fill_name_for_announce(self,text):
        self.page.locator('input[placeholder="Название для анонса"]').click()
        self.page.locator('input[placeholder="Название для анонса"]').fill(text)

    def fill_prematch_block(self,text):
        self.page.locator('trix-editor[placeholder="Предматчевый блок"]').click()
        self.page.locator('trix-editor[placeholder="Предматчевый блок"]').fill(text)

    def fill_teams(self):
        self.page.locator('div[data-testid="teams-search-input"]').nth(0).click()
        self.page.keyboard.type('Россия')
        self.page.locator('div[dusk="teams-search-input-result-0"]').click()

        self.page.locator('div[data-testid="teams-search-input"]').nth(1).click()
        self.page.keyboard.type('Россия')
        self.page.locator('div[dusk="teams-search-input-result-0"]').click()

    def fill_koef_fields(self, kef, text, bookmaker):
        self.page.locator('input[type="number"][step="0.01"]').click()
        self.page.keyboard.type(kef)
        self.page.locator('input:near(:text("СТАВКА"))').nth(0).click()
        self.page.keyboard.type(text)
        self.page.locator('div[style="width: 250px;"]').click()
        self.page.keyboard.type(bookmaker)
        self.page.locator(f'div[dusk="undefined-result-0"]').click()