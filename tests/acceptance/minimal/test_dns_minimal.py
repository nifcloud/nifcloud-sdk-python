import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("dns")


def test_list_hosted_zones(client):
    zones = client.list_hosted_zones()["HostedZones"]
    assert len(zones) == 1
