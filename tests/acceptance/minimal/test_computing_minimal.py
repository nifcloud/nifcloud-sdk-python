import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("computing")


def test_describe_regions(client):
    regions = client.describe_regions()
    actual_regions = regions["RegionInfo"]
    expected_regions = [
        {
            "RegionName": "east-1",
            "RegionEndpoint": "jp-east-1.computing.api.nifcloud.com"
        },
        {
            "RegionName": "east-2",
            "RegionEndpoint": "jp-east-2.computing.api.nifcloud.com"
        },
        {
            "RegionName": "east-3",
            "RegionEndpoint": "jp-east-3.computing.api.nifcloud.com"
        },
        {
            "RegionName": "jp-east-4",
            "RegionEndpoint": "jp-east-4.computing.api.nifcloud.com"
        },
        {
            "RegionName": "west-1",
            "RegionEndpoint": "jp-west-1.computing.api.nifcloud.com"
        },
        {
            "RegionName": "jp-west-2",
            "RegionEndpoint": "jp-west-2.computing.api.nifcloud.com"
        },
        {
            "RegionName": "us-east-1",
            "RegionEndpoint": "us-east-1.computing.api.nifcloud.com"
        }
    ]
    for actual, expected in zip(actual_regions, expected_regions):
        assert actual["RegionName"] == expected["RegionName"]
        assert actual["RegionEndpoint"] == expected["RegionEndpoint"]
