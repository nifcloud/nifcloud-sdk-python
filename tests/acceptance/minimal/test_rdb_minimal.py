import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("rdb")


def test_describe_db_engine_versions(client):
    db_engine_versions = client.describe_db_engine_versions(
        Engine='mysql', EngineVersion='5.7.15')["DBEngineVersions"]
    assert len(db_engine_versions) == 1
    db_engine_version = db_engine_versions[0]

    assert db_engine_version["DBEngineDescription"] == "MySQL Community Edition"
    assert db_engine_version["DBEngineVersionDescription"] == "MySQL 5.7.15"
    assert db_engine_version["DBParameterGroupFamily"] == "mysql5.7"
    assert db_engine_version["Engine"] == "mysql"
    assert db_engine_version["EngineVersion"] == "5.7.15"
