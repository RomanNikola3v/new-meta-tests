import requests


class GraphQlTypesRequest:

    def __init__(self, domain, query_type):
        self.domain = domain
        self.query_type = query_type
        self.GQL_URL = f'https://meta:meta@{domain}.metaratings.ru/graphql'
        self.query = """
  query IntrospectionQuery {
    __schema {
      types {
        name
        fields {
          name
          type {
            kind
            name
        }
        }
      }
    }
  }
"""

    def get_types(self):
        subject = None
        res = requests.post(self.GQL_URL, json={'query': self.query})
        try:

            result = res.json()
            for type in result['data']['__schema']['types']:
                if type['name'] == self.query_type:
                    subject = type
        except Exception as e:
            print(e)

        return subject
