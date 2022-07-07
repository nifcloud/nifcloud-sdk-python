import os

import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client(
        "storage",
        region_name="jp-east-1",
        nifcloud_access_key_id=os.getenv("NIFCLOUD_STORAGE_ACCESS_KEY_ID"),
        nifcloud_secret_access_key=os.getenv("NIFCLOUD_STORAGE_SECRET_ACCESS_KEY")
    )


def test_get_service(client):
    buckets = client.get_service()["Buckets"]
    assert len(buckets) == 0
