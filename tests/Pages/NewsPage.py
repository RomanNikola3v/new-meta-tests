from tests.Pages.Page import AdminPage

class NewsPage(AdminPage):

    def __init__(self, page):
        self.url = '/nova/resources/news/new'
        self.page = page

    def fill_all_checkboxes(self):
        self.page.locator("input[name=\"Выводить картинку на странице\"]").check()
        # Check input[name="Новость дня"]
        self.page.locator("input[name=\"Новость дня\"]").check()
        # Check input[name="Эксклюзив"]
        self.page.locator("input[name=\"Эксклюзив\"]").check()
        # Click input[name="Есть видео \(статус\)"]
        self.page.locator("input[name=\"Есть видео \\(статус\\)\"]").click()
        # Check input[name="Есть фото \(статус\)"]
        self.page.locator("input[name=\"Есть фото \\(статус\\)\"]").check()
        # Check input[name="Выгружать в Яндекс Дзен"]
        self.page.locator("input[name=\"Выгружать в Яндекс Дзен\"]").check()


    def fill_source(self):
        self.page.locator("[data-testid=\"sources-search-input\"] div").nth(2).click()
        self.page.locator(".search-input-trigger").click()
        self.page.locator("[placeholder=\"Search\"]").click()
        self.page.locator(".px-4 > .flex").first.click()






    def fill_mail_pulse(self):
        self.page.locator("input[name=\"Экспортировать в Mail\\.ru Pulse\"]").check()

    def press_save_and_wait(self):
        self.page.locator("button:has-text(\"Создать новость\")").click()
        self.page.wait_for_timeout(5000)

