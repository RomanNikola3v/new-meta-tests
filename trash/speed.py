from playwright.sync_api import sync_playwright
import datetime


ulist = ["https://demo.metaratings.ru", "https://demo.metaratings.ru/prognozy/basketbol/uniks-zenit-prognoz-na-match-edinoi-ligi-vtb-18-aprelya-2023-goda/", "https://demo.metaratings.ru/news/ulyanov-lokomotiv-ne-rassmatrivaet-sychevogo-na-zamenu-dzyube-244141/", "https://demo.metaratings.ru/news/", "https://demo.metaratings.ru/prognozy/", "https://demo.metaratings.ru/stavki/bitva-liderov-ostanetsya-za-zenitom-a-yuznoe-derbi-poraduet-golami-lucsie-stavki-na-23-i-tur-rpl/", "https://demo.metaratings.ru/blog/zhena-gilermo-abaskalya-alekhandra-de-agore-svadba-v-moskve-foto-biografiya/", "https://demo.metaratings.ru/bonuses/", "https://demo.metaratings.ru/bonuses/betboom-predlagaet-fribety-za-uchastie-v-kvize/", "https://demo.metaratings.ru/bookmakersrating/", "https://demo.metaratings.ru/mobilnye-bukmekerskie-kontory/", "https://demo.metaratings.ru/bookmakersrating/marathonbet-ru/"]
def measure_page_load_speed(pg):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        before = datetime.datetime.now()
        page.goto(pg.replace('demo','meta:meta@demo'))
        page.wait_for_load_state('domcontentloaded')
        after = datetime.datetime.now()
        result = after - before
        page.wait_for_load_state('networkidle')
        after = datetime.datetime.now()
        resultIdle = after - before
        print(str(resultIdle.total_seconds())[0:5])
        browser.close()

if __name__ == '__main__':
    for i in ulist:
        measure_page_load_speed(i)
