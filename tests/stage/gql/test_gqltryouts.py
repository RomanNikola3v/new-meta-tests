from tests.Helpers.GraphqlTypesRequest import GraphQlTypesRequest
from tests.Helpers.gql_valid_responses import GqlValid


enviroment = 'stage'
valid_responses = GqlValid()


def test_graphql_News_type_are_unchanged():
    res = GraphQlTypesRequest(enviroment,"News").get_types()
    expected_response = valid_responses.news
    print(type(res))
    assert res == expected_response


def test_graphql_Article_type_are_unchanged():
    res = GraphQlTypesRequest(enviroment,'Article').get_types()
    expected_response = valid_responses.article
    assert res == expected_response

def test_graphql_Bonus_type_are_unchanged():
    res = GraphQlTypesRequest(enviroment,'Bonus').get_types()
    expected_response = valid_responses.bonus
    assert res == expected_response


def test_graphql_Tips_type_are_unchanged():
    res = GraphQlTypesRequest(enviroment,'Tips').get_types()
    expected_response = valid_responses.tips
    assert res == expected_response
