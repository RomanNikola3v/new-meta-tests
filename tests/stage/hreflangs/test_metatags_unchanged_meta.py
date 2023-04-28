from tests.Helpers.PageMeta import PageMeta
from tests.Helpers.SoupPage import SoupPage
import pytest



pg = ["https://stage.metaratings.ru/authors/aleksandr-atvesskiy/", "https://stage.metaratings.ru/authors/aleksandr-kotkin/", "https://stage.metaratings.ru/best-bookmakers/", "https://stage.metaratings.ru/best-bookmakers/1win-registratsiya/", "https://stage.metaratings.ru/best-loto/", "https://stage.metaratings.ru/best-loto/gde-kupit-loterejnyj-bilet/", "https://stage.metaratings.ru/bk-s-bezdepozitnym-bonusom-za-registraciyu/", "https://stage.metaratings.ru/blog/", "https://stage.metaratings.ru/blog/?page=2", "https://stage.metaratings.ru/blog/ak-bars-v-sezone-kkhl-2022-2023-proval-znarka-so-zvyozdami-vozvrashchenie-bilyaletdinova-kak-vyshli-v-final/", "https://stage.metaratings.ru/blog/girls/", "https://stage.metaratings.ru/blog/girls/?page=2", "https://stage.metaratings.ru/blog/gisele-bundchen-i-ee-muzh-tom-brady-razvodyatsya-foto-modeli-prichiny-rasstavaniya/", "https://stage.metaratings.ru/bonuses/1xbet/", "https://stage.metaratings.ru/bonuses/1xbet/promokody/", "https://stage.metaratings.ru/bonuses/abonenty-bilayn-megafon-i-mts-mogut-bez-komissii-popolnyat-igrovoy-schet-v-bk-leon/", "https://stage.metaratings.ru/bonuses/akcii/", "https://stage.metaratings.ru/bonuses/aktsiya-ot-leon-delay-stavki-s-mobilnogo-prilozheniya/", "https://stage.metaratings.ru/bonuses/betboom-razygraet-500-000-rubley-fribetov-na-vtoroy-trasse-vesenney-gonki/", "https://stage.metaratings.ru/bookmakersrating/", "https://stage.metaratings.ru/bookmakersrating/bet365/", "https://stage.metaratings.ru/bookmakersrating/lootbet/", "https://stage.metaratings.ru/bukmekerskie-kontory-yandex-dengi/", "https://stage.metaratings.ru/bukmekery-mira/", "https://stage.metaratings.ru/bukmekery-s-rublyami/", "https://stage.metaratings.ru/cappersrating/", "https://stage.metaratings.ru/news/", "https://stage.metaratings.ru/news/15-letnyaya-rossiiskaya-tennisistka-andreeva-oderzhala-pervuyu-pobedu-na-turnirakh-wta-246314/", "https://stage.metaratings.ru/news/?page=2", "https://stage.metaratings.ru/news/agent-chakyra-prokommentiroval-informaciyu-ob-interese-zenita-k-vrataryu-trabzonspora-246156/", "https://stage.metaratings.ru/news/biatlon/", "https://stage.metaratings.ru/news/drugie/", "https://stage.metaratings.ru/news/eks-marketolog-romy-obyasnil-preimushestvo-chm-2018-v-rossii-nad-mundialem-v-katare-218057/", "https://stage.metaratings.ru/news/eksklyuzivy/?page=2", "https://stage.metaratings.ru/prognozy/", "https://stage.metaratings.ru/prognozy/amerikanskiy-futbol/", "https://stage.metaratings.ru/prognozy/basketbol/", "https://stage.metaratings.ru/prognozy/basketbol/?page=3", "https://stage.metaratings.ru/prognozy/basketbol/bruklin-filadelfiya-prognoz-na-match-nba-22-aprelya-2023-goda/", "https://stage.metaratings.ru/prognozy/drugie/", "https://stage.metaratings.ru/prognozy/drugie/?page=2", "https://stage.metaratings.ru/prognozy/futbol/argentina-khorvatiya-prognoz-kf-1-85-i-stavki-13-dekabrya-na-match-chempionata-mira-po-futbolu-2022-/", "https://stage.metaratings.ru/prognozy/futbol/fnl/", "https://stage.metaratings.ru/prognozy/futbol/inter-barselona-prognoz-na-segodnya-stavki-po-statistike-koeffitsienty-na-match-tretego-tura-lch/", "https://stage.metaratings.ru/shkola-bettinga/", "https://stage.metaratings.ru/shkola-bettinga/analiz-futbolnykh-matchey/", "https://stage.metaratings.ru/sports-history/", "https://stage.metaratings.ru/sports-history/?page=2", "https://stage.metaratings.ru/sports-history/aleksandr-bolshunov-biografiya/", "https://stage.metaratings.ru/stavki-na-apl/", "https://stage.metaratings.ru/stavki/?page=5", "https://stage.metaratings.ru/stavki/akron-v-finale-puti-regionov-kubka-rossii-kak-uspexi-kluba-mozno-bylo-ispolzovat-v-stavkax/", "https://stage.metaratings.ru/shkola-bettinga/", "https://stage.metaratings.ru/shkola-bettinga/analiz-futbolnykh-matchey/", "https://stage.metaratings.ru/sports-history/", "https://stage.metaratings.ru/sports-history/?page=2", "https://stage.metaratings.ru/sports-history/aleksandr-bolshunov-biografiya/", "https://stage.metaratings.ru/stavki-na-apl/", "https://stage.metaratings.ru/stavki/?page=5", "https://stage.metaratings.ru/stavki/akron-v-finale-puti-regionov-kubka-rossii-kak-uspexi-kluba-mozno-bylo-ispolzovat-v-stavkax/", "https://stage.metaratings.ru/tags/ajax/", "https://stage.metaratings.ru/tags/inter/", "https://stage.metaratings.ru/tags/liverpool/", "https://stage.metaratings.ru/teams/toronto-meypl-lifs/", "https://stage.metaratings.ru/teams/zenit-sankt-peterburg/", "https://stage.metaratings.ru/tournaments/belarus-vysshaya-liga/", "https://stage.metaratings.ru/tournaments/europa-conference-league/", "https://stage.metaratings.ru/vacancies/", "https://stage.metaratings.ru/vilki/", "https://stage.metaratings.ru/zachem-nuzhen-metareyting/", "https://stage.metaratings.ru/zarubezhnye-bukmekerskie-kontory/", "https://stage.metaratings.ru/zerkala-bukmekerskih-kontor/"]

def cook_pages(target):
    page = SoupPage(target)
    soup = page.return_soup()
    assert page.response.status_code == 200
    result = PageMeta(soup)
    return result

@pytest.mark.parametrize('params',pg)
def test_meta_ta(params):

    meta_new = cook_pages(params)
    meta_old = cook_pages(params.replace('stage.',''))

    meta_old.find_hreflangs()
    meta_new.find_hreflangs()
    meta_old.find_meta()
    meta_new.find_meta()

    mn = {
        "h1":meta_new.h1,
        "des":meta_new.description,
        "title":meta_new.title,
        "canonical":meta_new.canonical.replace('stage.',''),
        "ogTitle":meta_new.og_title,
        "ogDes":meta_new.og_description,
        "ogSiteName":meta_new.og_siteName,
        'hreflangs':meta_new.hreflangs_ta

    }

    mo = {
        "h1":meta_old.h1,
        "des":meta_old.description,
        "title":meta_old.title,
        "canonical":meta_old.canonical,
        "ogTitle":meta_old.og_title,
        "ogDes":meta_old.og_description,
        "ogSiteName":meta_old.og_siteName,
        'hreflangs':meta_old.hreflangs_ta
    }

    assert mo == mn