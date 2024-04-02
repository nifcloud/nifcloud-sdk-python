import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("devops-runner", region_name="jp-west-1")


def test_list_runners(client):
    runners = client.list_runners()["Runners"]
    assert len(runners) == 0
