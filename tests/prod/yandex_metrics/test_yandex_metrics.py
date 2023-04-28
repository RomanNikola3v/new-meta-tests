import pytest
from playwright.sync_api import Page

domainAndMetric = [
    {'domain':'https://metaratings.ru',
     'metricsYandex': 'PageView. Counter 49983739. URL: https://metaratings.ru/?_ym_debug=1. Referrer: ',
     },
    {'domain':'https://mma.metaratings.ru',
     'metricsYandex': 'PageView. Counter 71903464. URL: https://mma.metaratings.ru/?_ym_debug=1. Referrer: ',
     },
    {'domain':'https://cybersport.metaratings.ru',
     'metricsYandex': 'PageView. Counter 70899649. URL: https://cybersport.metaratings.ru/?_ym_debug=1. Referrer: ',
     },
    {'domain':'https://meta-ratings.kz',
     'metricsYandex': 'PageView. Counter 61683715. URL: https://meta-ratings.kz/?_ym_debug=1. Referrer: ',
     },
    {'domain':'https://metaratings.by',
     'metricsYandex': 'PageView. Counter 61645819. URL: https://metaratings.by/?_ym_debug=1. Referrer: ',
     },
    {'domain':'https://metaratings.tj',
     'metricsYandex': 'PageView. Counter 61682716. URL: https://metaratings.tj/?_ym_debug=1. Referrer: ',
     }
]

@pytest.mark.parametrize('params',domainAndMetric)
def test_metrics_presented(params,page:Page):
    messages = []
    page.on("console", lambda msg: messages.append(msg.text))
    page.goto(params['domain']+'/?_ym_debug=1')
    page.wait_for_timeout(3000)
    assert params['metricsYandex'] in messages
