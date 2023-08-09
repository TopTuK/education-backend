import pytest

from django.core.cache import cache

from amocrm.cache.lead_b2b_pipeline_statuses_ids import get_b2b_pipeline_status_id
from amocrm.exceptions import AmoCRMCacheException
from amocrm.types import AmoCRMPipeline
from amocrm.types import AmoCRMPipelineStatus

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.single_thread,
]


@pytest.fixture
def first_contact_status():
    return AmoCRMPipelineStatus(id=5, name="Первичный контакт")


@pytest.fixture
def b2b_pipeline(first_contact_status):
    return AmoCRMPipeline(id=333, name="b2b", statuses=[first_contact_status])


@pytest.fixture
def pipelines(b2b_pipeline):
    return [b2b_pipeline, AmoCRMPipeline(id=111, name="individual", statuses=[AmoCRMPipelineStatus(id=10, name="hm status")])]


@pytest.fixture(autouse=True)
def mock_get_pipelines(mocker, pipelines):
    return mocker.patch("amocrm.client.AmoCRMClient.get_pipelines", return_value=pipelines)


def test_return_pipeline_status_if_in_cache(first_contact_status, mock_get_pipelines):
    cache.set("amocrm_b2b_first_contact_status_id", first_contact_status.id)

    got = get_b2b_pipeline_status_id(status_name="first_contact")

    assert got == first_contact_status.id
    mock_get_pipelines.assert_not_called()


def test_return_pipeline_from_response_if_not_in_cache(first_contact_status, mock_get_pipelines):
    cache.clear()

    got = get_b2b_pipeline_status_id(status_name="first_contact")
    assert got == first_contact_status.id
    assert cache.get("amocrm_b2b_first_contact_status_id") == first_contact_status.id
    mock_get_pipelines.assert_called_once()


def test_fail_if_not_in_cache_and_pipeline_not_in_response(mock_get_pipelines):
    cache.clear()
    mock_get_pipelines.return_value = [AmoCRMPipeline(id=111, name="individual", statuses=[AmoCRMPipelineStatus(id=10, name="hm status")])]

    with pytest.raises(AmoCRMCacheException, match="Cannot retrieve b2b pipeline"):
        get_b2b_pipeline_status_id(status_name="first_contact")


def test_fail_if_not_in_cache_and_status_not_in_response(mock_get_pipelines):
    cache.clear()
    mock_get_pipelines.return_value = [AmoCRMPipeline(id=333, name="b2b", statuses=[AmoCRMPipelineStatus(id=7, name="Переговоры")])]

    with pytest.raises(AmoCRMCacheException, match="Cannot retrieve first_contact"):
        get_b2b_pipeline_status_id(status_name="first_contact")
