import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("nas", region_name="jp-west-1")


def test_describe_nas_instances(client):
    nas_instances = client.describe_nas_instances()["NASInstances"]
    assert len(nas_instances) == 0
