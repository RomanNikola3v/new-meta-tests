import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Helpers'))


class Domain:

    def __init__(self):
        self.meta = 'https://metaratings.ru'
        self.mma = 'https://mma.metaratings.ru'
        self.cybersport = 'https://cybersport.metaratings.ru'
        self.kz = 'https://meta-ratings.kz'
        self.tj = 'https://metaratings.tj'
        self.by = 'https://metaratings.by'
        self.ta = 'https://www.telecomasia.net'
        self.meta_stage = self.meta.replace('https://','https://stage.')
        self.mma_stage = self.mma.replace('https://','https://stage.')
        self.cybersport_stage = self.cybersport.replace('https://','https://stage.')
        self.kz_stage = self.kz.replace('https://','https://stage.')
        self.tj_stage = self.tj.replace('https://','https://stage.')
        self.by_stage = self.by.replace('https://','https://stage.')


@pytest.fixture
def domain():
    result = Domain()
    return result

