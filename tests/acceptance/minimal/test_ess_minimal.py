import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("ess")


def test_list_identities(client):
    identities = client.list_identities()["Identities"]
    assert len(identities) == 0


def test_get_send_quota(client):
    send_quota = client.get_send_quota()

    assert send_quota["Max24HourSend"] == 2500000.0
    assert send_quota["MaxSendRate"] == 50.0
    assert send_quota["SentLast24Hours"] == 0.0


def test_get_send_statistics(client):
    send_statistics = client.get_send_statistics()["SendDataPoints"]
    assert len(send_statistics) == 0
