import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("nas")


def test_describe_nas_instances(client):
    nas_instances = client.describe_nas_instances()["NASInstances"]
    assert len(nas_instances) == 1
    nas_instance = nas_instances[0]
    # assert nas_instance["AllocatedStorage"] == 100
    assert nas_instance["AllocatedStorage"] == "100"
    assert nas_instance["AvailabilityZone"] == "east-11"
    assert nas_instance["NASInstanceClass"] == "e-small"
    assert nas_instance["NASInstanceIdentifier"] == "sdktestnas001"
    assert nas_instance["NASInstanceDescription"] == ""
    assert nas_instance["NASInstanceStatus"] == "available"
    assert len(nas_instance["NASSecurityGroups"]) == 1
    assert nas_instance["NASSecurityGroups"] == [{
        "NASSecurityGroupName": "default.east-11",
        # "Status": "available"
    }]
    assert type(nas_instance["Endpoint"]["Address"]) is str
    assert type(nas_instance["Endpoint"]["PrivateAddress"]) is str
    assert nas_instance["Protocol"] == "nfs"
    # assert type(nas_instance["CreateTime"]) == datetime.datetime
    assert type(nas_instance["CreateTime"]) == str
    assert nas_instance["StorageType"] == 0
    assert nas_instance["AuthenticationType"] == 0
    assert nas_instance["NASInstanceType"] == 0
    # assert not nas_instance["NoRootSquash"]
    assert nas_instance["NoRootSquash"] == "false"


def test_describe_nas_security_groups(client):
    security_groups = client.describe_nas_security_groups()["NASSecurityGroups"]  # noqa: E501
    assert len(security_groups) == 2

    # default security group
    security_group = security_groups[0]
    assert security_group["NASSecurityGroupDescription"] == "default"
    assert security_group["NASSecurityGroupName"] == "default.east-11"
    assert security_group["IPRanges"] == []
    assert security_group["AvailabilityZone"] == "east-11"

    # custom security group
    security_group = security_groups[1]
    assert security_group["NASSecurityGroupDescription"] == "SDK TEST MEMO"
    assert security_group["NASSecurityGroupName"] == "sdktestnasfw001"
    assert len(security_group["SecurityGroups"]) == 1
    ec2_security_groups = security_group["SecurityGroups"][0]
    assert ec2_security_groups["SecurityGroupName"] == "sdktestfw001"
    assert type(ec2_security_groups["SecurityGroupOwnerId"]) is str
    assert ec2_security_groups["Status"] == "authorized"
    assert security_group["IPRanges"] == []
    assert security_group["AvailabilityZone"] == "east-11"
