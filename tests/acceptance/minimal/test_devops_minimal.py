import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("devops", region_name="jp-west-1")


def test_list_instances(client):
    instances = client.list_instances()["Instances"]
    assert len(instances) == 0
