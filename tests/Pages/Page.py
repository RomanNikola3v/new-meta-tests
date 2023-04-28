
class AdminPage:

    def __init__(self, page):
        self.page = page

    def fill_name(self, text):
        self.page.locator("[placeholder=\"Название\"]").click()
        self.page.locator("[placeholder=\"Название\"]").fill(text)

    def fill_announce(self,text):
        self.page.locator("textarea[id=\"annonce\"]").click()
        self.page.locator("text=Анонс Кол-во символов: 0 >> textarea").fill(text)

    def fill_picture(self):
        self.page.locator("text=Выбрать файл").click()
        self.page.locator("input[name=\"name\"]").set_input_files("1.jpeg")

    def fill_region(self, index):
        # 0-ru 1-ua 2-by 3-kz 4-tj
        self.page.locator(
            "text=Metaratings Metaratings ru Metaratings ua Metaratings by Metaratings kz Metarati >> input[type=\"checkbox\"]").nth(
            index).check()

    def fill_tag(self):
        self.page.locator("span:has-text(\"Теги\")").click()
        self.page.locator("[placeholder=\"Теги\"]").fill("winline")
        self.page.wait_for_timeout(10)
        self.page.locator("text=Winline").first.click()

    def fill_text_block(self,text):
        self.page.locator(".ce-block__content").click()
        self.page.keyboard.type(text)


    def fill_author(self):
        self.page.locator(".search-input-trigger").first.click()
        self.page.locator("[placeholder=\"Search\"]").click()
        self.page.locator("[placeholder=\"Search\"]").fill("а")
        self.page.locator(".px-4 > .flex").first.click()

    def fill_category(self, text="Футбол"):
        self.page.locator('input[placeholder="Разделы"]')
        self.page.keyboard.type(text)
        self.page.keyboard.press("Enter")
