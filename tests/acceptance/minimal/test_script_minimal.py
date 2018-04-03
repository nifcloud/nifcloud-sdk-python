import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("script")


def test_execute_script(client):
    script_indentifier = "sdktest001.js"
    method = "GET"
    query = '{"query_key":"query_value"}'
    header = '{"header_key":"header_value"}'
    body = '{"body_key":"body_value"}'
    execute_result = client.execute_script(
        ScriptIdentifier=script_indentifier,
        Method=method,
        Query=query,
        Header=header,
        Body=body
    )
    result = execute_result["Result"]
    assert result["ResponseStatus"] == 200
    assert result["ScriptIdentifier"] == script_indentifier
    assert result["RequestQuery"] == query
    assert result["RequestHeader"] == header
    assert result["RequestBody"] == body
    assert result["ResponseHeader"] == '{"Content-Type":"text/plain"}'
    assert result["ResponseData"] == "v6.11.1"
