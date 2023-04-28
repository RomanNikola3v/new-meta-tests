import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36',
    'X-Meta-QA': 'qa-2023'


}


def test_robots_sport(domain):
    with open('robots_sport.txt') as robo:
        response_sport = requests.get(domain.meta + '/robots.txt',headers=headers)

        assert response_sport.text.replace('\r','') == robo.read()

def test_robots_mma(domain):
    with open('robots_mma.txt') as robo:
        response_mma = requests.get(domain.mma + '/robots.txt',headers=headers)
        assert response_mma.text.replace('\r','') == robo.read()

def test_robots_cyber(domain):
    with open('robots_cyber.txt') as robo:
        response_cyber = requests.get(domain.cybersport + '/robots.txt',headers=headers)
        assert response_cyber.text.replace('\r','') == robo.read()

def test_robots_telecom(domain):
    with open('robots_telecom.txt') as robo:
        response_telecom = requests.get(domain.ta + '/robots.txt',headers=headers)
        assert response_telecom.text.replace('\r','') == robo.read()

def test_robots_kz(domain):
    with open('robots_kz.txt') as robo:
        response_kz = requests.get(domain.kz + '/robots.txt',headers=headers)
        assert response_kz.text.replace('\r','') == robo.read()