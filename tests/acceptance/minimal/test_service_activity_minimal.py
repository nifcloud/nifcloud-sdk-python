import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("service-activity")


def test_list_service_menu(client):
    result = client.describe_service_statuses()
    result_data = result["Data"]
    result_service_menu = result_data["ServiceMenu"]
    assert len(result_service_menu) != 0
