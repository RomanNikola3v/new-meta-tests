import pytest
from playwright.sync_api import Page
import datetime

pg = 'https://meta:meta@demo.metaratings.ru/'


def test_page_load_time(page:Page,domain):
    before = datetime.datetime.now()
    page.goto(domain.meta_stage)
    page.wait_for_load_state('domcontentloaded')
    after = datetime.datetime.now()
    result = after - before
    page.wait_for_load_state('networkidle')
    after = datetime.datetime.now()
    resultIdle = after - before
    assert [result,resultIdle] == True
