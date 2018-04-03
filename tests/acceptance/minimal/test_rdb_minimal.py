import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("rdb")


def test_describe_db_instances(client):
    db_instances = client.describe_db_instances()["DBInstances"]
    assert len(db_instances) == 1
    db_instance = db_instances[0]
    # assert db_instance["AllocatedStorage"] == 50
    assert db_instance["AllocatedStorage"] == "50"
    assert not db_instance["AutoMinorVersionUpgrade"]
    assert db_instance["AvailabilityZone"] == "east-11"
    # assert db_instance["BackupRetentionPeriod"] == 0
    assert db_instance["BackupRetentionPeriod"] == "0"
    assert db_instance["DBInstanceClass"] == "db.mini"
    assert db_instance["DBInstanceIdentifier"] == "sdktestdb001"
    assert db_instance["DBInstanceStatus"] == "available"
    assert db_instance["DBName"] == "sdktest"
    assert len(db_instance["DBParameterGroups"]) == 1
    assert db_instance["DBParameterGroups"] == [{
        "DBParameterGroupName": "default.mysql5.7",
        # "ParameterApplyStatus": "in-sync"
    }]
    assert len(db_instance["DBSecurityGroups"]) == 1
    assert db_instance["DBSecurityGroups"] == [{
        "DBSecurityGroupName": "default.east-11",
        # "Status": "available"
    }]
    assert type(db_instance["Endpoint"]["Address"]) is str
    assert type(db_instance["Endpoint"]["NiftyPrivateAddress"]) is str
    # assert type(db_instance["Endpoint"]["Port"]) is int
    assert type(db_instance["Endpoint"]["Port"]) is str
    assert db_instance["Engine"] == "mysql"
    assert db_instance["EngineVersion"] == "5.7.15"
    # assert type(db_instance["InstanceCreateTime"]) is datetime.datetime
    assert type(db_instance["InstanceCreateTime"]) is str
    assert db_instance["LicenseModel"] == "general-public-license"
    assert db_instance["MasterUsername"] == "sdktestuser"
    # assert not db_instance["MultiAZ"]
    assert db_instance["MultiAZ"] == "false"
    assert len(db_instance["OptionGroupMemberships"]) == 1
    assert db_instance["OptionGroupMemberships"] == [{
        "OptionGroupName": "default:mysql-5-7",
        "Status": "in-sync"
    }]
    assert type(db_instance["PreferredBackupWindow"]) is str
    assert type(db_instance["PreferredMaintenanceWindow"]) is str
    assert db_instance["PubliclyAccessible"]
    assert db_instance["PendingModifiedValues"] == {}
    assert db_instance["NiftyStorageType"] == 0


def test_describe_db_security_groups(client):
    security_groups = client.describe_db_security_groups()["DBSecurityGroups"]
    assert len(security_groups) == 2

    # custom security group
    security_group = security_groups[0]
    assert security_group["DBSecurityGroupDescription"] == "SDK TEST MEMO"
    assert security_group["DBSecurityGroupName"] == "sdktestdbfw001"
    assert len(security_group["EC2SecurityGroups"]) == 1
    ec2_security_group = security_group["EC2SecurityGroups"][0]
    assert ec2_security_group["EC2SecurityGroupName"] == "sdktestfw001"
    assert type(ec2_security_group["EC2SecurityGroupOwnerId"]) is str
    assert ec2_security_group["Status"] == "authorized"
    assert security_group["IPRanges"] == []

    # default security group
    security_group = security_groups[1]
    assert security_group["DBSecurityGroupDescription"] == "default"
    assert security_group["DBSecurityGroupName"] == "default.east-11"
    assert security_group["EC2SecurityGroups"] == []
    assert security_group["IPRanges"] == []
