from sports.entities import ResultInternalEntity
from sports.data_providers.api_football_data_provider import (
    transform_provider_results_data_to_entities,
    transform_provider_standings_data_to_entities,
)
from sports.tests.api_football_response_example import (
    STANDINGS_RESPONSE_EXAMPLE,
    FIXTURES_RESPONSE_EXAMPLE,
)
from sports.tests.test_data import (
    TEST_TEAM_STANDINGS_ENTITY_LIST,
    TEST_RESULT_ENTITY_LIST,
)


def test_transform_raw_standings_data_to_entities():
    assert (
        transform_provider_standings_data_to_entities(
            provider_data=STANDINGS_RESPONSE_EXAMPLE
        )
        == TEST_TEAM_STANDINGS_ENTITY_LIST
    )


def test_transform_provider_results_data_to_entities():
    assert (
        transform_provider_results_data_to_entities(
            provider_data=FIXTURES_RESPONSE_EXAMPLE
        )
        == TEST_RESULT_ENTITY_LIST
    )
