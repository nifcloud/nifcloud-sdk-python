from datetime import datetime

import pytest

from nifcloud import session


@pytest.fixture(scope="function")
def client():
    return session.get_session().create_client("computing")


def test_describe_instances(client):
    reservation_set = client.describe_instances()["ReservationSet"]
    assert len(reservation_set) == 2

    # instance: sdktest001
    sdktest001 = reservation_set[0]
    assert sdktest001["ReservationId"] == ""
    assert sdktest001["OwnerId"] == ""
    group_set = sdktest001["GroupSet"]
    assert len(group_set) == 1
    assert group_set[0] == {"GroupId": "sdktestfw001"}
    assert len(sdktest001["InstancesSet"]) == 1
    instances_set = sdktest001["InstancesSet"][0]
    assert instances_set["InstanceId"] == "sdktest001"
    assert instances_set["InstanceUniqueId"] == "i-0nzgxtwf"
    assert instances_set["ImageId"] == "89"
    assert instances_set["InstanceState"]["Code"] == 16
    assert instances_set["InstanceState"]["Name"] == "running"
    assert type(instances_set["PrivateDnsName"]) is str
    assert instances_set.get("DnsName") is not None
    assert instances_set["KeyName"] == "sdktest001"
    assert instances_set["AmiLaunchIndex"] == ""
    assert len(instances_set["ProductCodes"]) == 1
    assert instances_set["ProductCodes"][0] == {"ProductCode": ""}
    assert instances_set["InstanceType"] == "e-mini"
    assert type(instances_set["LaunchTime"]) is datetime
    assert instances_set["Placement"]["AvailabilityZone"] == "east-11"
    assert instances_set["KernelId"] == ""
    assert instances_set["RamdiskId"] == ""
    assert instances_set["Platform"] == "ubuntu"
    assert instances_set["ImageName"] == "Ubuntu 16.04 64bit Plain"
    assert instances_set["Monitoring"]["State"] == "disabled"
    assert instances_set["SubnetId"] == ""
    assert instances_set["VpcId"] == ""
    assert type(instances_set["PrivateIpAddress"]) is str
    assert type(instances_set["IpAddress"]) is str
    assert type(instances_set["PrivateIpAddressV6"]) is str
    assert type(instances_set["IpAddressV6"]) is str
    assert not instances_set["StateReason"]["Code"]
    assert instances_set["StateReason"]["Message"] == ""
    assert instances_set["Architecture"] == "x86_64"
    assert instances_set["RootDeviceName"] == ""

    assert len(instances_set["BlockDeviceMapping"]) == 1
    block_device_mapping = instances_set["BlockDeviceMapping"][0]
    assert block_device_mapping["DeviceName"] == "SCSI (0:0)"
    assert block_device_mapping["Ebs"]["Status"] == "attached"
    assert block_device_mapping["Ebs"]["VolumeId"] == "sdktestdisk001"
    assert not block_device_mapping["Ebs"]["DeleteOnTermination"]
    assert type(block_device_mapping["Ebs"]["AttachTime"]) is datetime

    assert instances_set["InstanceLifecycle"] == ""
    assert instances_set["SpotInstanceRequestId"] == ""
    assert instances_set["AccountingType"] == "2"
    assert instances_set["NextMonthAccountingType"] == "2"

    assert len(instances_set["Loadbalancing"]) == 1
    loadbalancing = instances_set["Loadbalancing"][0]
    assert loadbalancing["LoadBalancerName"] == "sdktestlb001"
    assert loadbalancing["LoadBalancerPort"] == 80
    assert loadbalancing["InstancePort"] == 80
    assert loadbalancing["State"] == "OutOfService"

    assert instances_set["IpType"] == "static"
    assert instances_set["NiftyPrivateIpType"] == "static"
    assert instances_set["Description"] == ""
    assert instances_set["HotAdd"] == "2"

    assert instances_set["NiftyPrivateNetworkType"] == "STANDARD"
    assert instances_set["Tenancy"] == "default"

    assert len(instances_set["NetworkInterfaceSet"]) == 2
    network_interface_glo = instances_set["NetworkInterfaceSet"][0]
    assert network_interface_glo["SubnetId"] == ""
    assert network_interface_glo["VpcId"] == ""
    assert network_interface_glo["Description"] == ""
    assert network_interface_glo["OwnerId"] == ""
    assert network_interface_glo["NiftyNetworkId"] == "net-COMMON_GLOBAL"
    assert network_interface_glo["Status"] == "in-use"
    assert type(network_interface_glo["MacAddress"]) is str
    assert network_interface_glo["PrivateDnsName"] == ""
    assert network_interface_glo["SourceDestCheck"] == ""
    assert network_interface_glo["GroupSet"] == []
    assert network_interface_glo["Attachment"]["DeviceIndex"] == 0
    assert network_interface_glo["Attachment"]["Status"] == "attached"
    assert network_interface_glo["Attachment"]["DeleteOnTermination"]
    assert type(network_interface_glo["Association"]["PublicIp"]) is str
    assert type(network_interface_glo["Association"]["PublicIpV6"]) is str
    assert network_interface_glo["Association"]["PublicDnsName"] == ""
    assert network_interface_glo["Association"]["IpOwnerId"] == ""
    assert network_interface_glo["PrivateIpAddressesSet"] == []

    network_interface_pri = instances_set["NetworkInterfaceSet"][1]
    assert network_interface_pri["SubnetId"] == ""
    assert network_interface_pri["VpcId"] == ""
    assert network_interface_pri["Description"] == ""
    assert network_interface_pri["OwnerId"] == ""
    assert network_interface_pri["NiftyNetworkId"] == "net-COMMON_PRIVATE"
    assert network_interface_pri["Status"] == "in-use"
    assert type(network_interface_pri["MacAddress"]) is str
    assert type(network_interface_pri["PrivateIpAddress"]) is str
    assert type(network_interface_pri["PrivateIpAddressV6"]) is str
    assert network_interface_pri["PrivateDnsName"] == ""
    assert network_interface_pri["SourceDestCheck"] == ""
    assert network_interface_pri["GroupSet"] == []
    assert network_interface_pri["Attachment"]["DeviceIndex"] == 0
    assert network_interface_pri["Attachment"]["Status"] == "attached"
    assert network_interface_pri["Attachment"]["DeleteOnTermination"]
    assert network_interface_pri["PrivateIpAddressesSet"] == []

    assert len(instances_set["NiftyElasticLoadBalancing"]) == 1
    elastic_load_balancing = instances_set["NiftyElasticLoadBalancing"][0]
    assert type(elastic_load_balancing["ElasticLoadBalancerId"]) is str
    assert elastic_load_balancing["ElasticLoadBalancerName"] == "sdktestmlb001"
    assert elastic_load_balancing["ElasticLoadBalancerPort"] == 80
    assert elastic_load_balancing["InstancePort"] == 80
    assert elastic_load_balancing["Protocol"] == "TCP"

    # instance: sdktest002
    sdktest002 = reservation_set[1]
    assert sdktest002["ReservationId"] == ""
    assert sdktest002["OwnerId"] == ""
    group_set = sdktest002["GroupSet"]
    assert len(group_set) == 1
    assert group_set[0] == {"GroupId": "sdktestfw001"}
    assert len(sdktest002["InstancesSet"]) == 1
    instances_set = sdktest002["InstancesSet"][0]
    assert instances_set["InstanceId"] == "sdktest002"
    assert instances_set["InstanceUniqueId"] == "i-0nzgxdk7"
    assert instances_set["ImageId"] == "68"
    assert instances_set["InstanceState"]["Code"] == 16
    assert instances_set["InstanceState"]["Name"] == "running"
    assert type(instances_set["PrivateDnsName"]) is str
    assert instances_set.get("DnsName") is not None
    assert instances_set["KeyName"] == "sdktest001"
    assert instances_set["AmiLaunchIndex"] == ""
    assert len(instances_set["ProductCodes"]) == 1
    assert instances_set["ProductCodes"][0] == {"ProductCode": ""}
    assert instances_set["InstanceType"] == "e-mini"
    assert type(instances_set["LaunchTime"]) is datetime
    assert instances_set["Placement"]["AvailabilityZone"] == "east-11"
    assert instances_set["KernelId"] == ""
    assert instances_set["RamdiskId"] == ""
    assert instances_set["Platform"] == "centos"
    assert instances_set["ImageName"] == "CentOS 7.1 64bit Plain"
    assert instances_set["Monitoring"]["State"] == "disabled"
    assert instances_set["SubnetId"] == ""
    assert instances_set["VpcId"] == ""
    assert type(instances_set["PrivateIpAddress"]) is str
    assert type(instances_set["PrivateIpAddressV6"]) is str
    assert not instances_set["StateReason"]["Code"]
    assert instances_set["StateReason"]["Message"] == ""
    assert instances_set["Architecture"] == "x86_64"
    assert instances_set["RootDeviceName"] == ""

    assert len(instances_set["BlockDeviceMapping"]) == 0

    assert instances_set["InstanceLifecycle"] == ""
    assert instances_set["SpotInstanceRequestId"] == ""
    assert instances_set["AccountingType"] == "2"
    assert instances_set["NextMonthAccountingType"] == "2"

    assert len(instances_set["Loadbalancing"]) == 0

    assert instances_set["IpType"] == "none"
    assert instances_set["NiftyPrivateIpType"] == "static"
    assert instances_set["Description"] == ""
    assert instances_set["HotAdd"] == "0"

    assert instances_set["NiftyPrivateNetworkType"] == "PRIVATE_LAN"
    assert instances_set["Tenancy"] == "default"

    assert len(instances_set["NetworkInterfaceSet"]) == 1
    network_interface_pri = instances_set["NetworkInterfaceSet"][0]
    assert network_interface_pri["SubnetId"] == ""
    assert network_interface_pri["VpcId"] == ""
    assert network_interface_pri["Description"] == ""
    assert network_interface_pri["OwnerId"] == ""
    assert network_interface_pri["NiftyNetworkId"] == "net-0avs0v5m"
    assert network_interface_pri["NiftyNetworkName"] == "sdktestlan001"
    assert network_interface_pri["Status"] == "in-use"
    assert type(network_interface_pri["MacAddress"]) is str
    assert type(network_interface_pri["PrivateIpAddress"]) is str
    assert type(network_interface_pri["PrivateIpAddressV6"]) is str
    assert network_interface_pri["PrivateDnsName"] == ""
    assert network_interface_pri["SourceDestCheck"] == ""
    assert network_interface_pri["GroupSet"] == []
    assert network_interface_pri["Attachment"]["DeviceIndex"] == 0
    assert network_interface_pri["Attachment"]["Status"] == "attached"
    assert network_interface_pri["Attachment"]["DeleteOnTermination"]
    assert network_interface_pri["PrivateIpAddressesSet"] == []

    assert len(instances_set["NiftyElasticLoadBalancing"]) == 0


def test_describe_key_pairs(client):
    key_pairs = client.describe_key_pairs()
    key_set = key_pairs["KeySet"]
    assert len(key_set) == 2

    # sdktest001
    assert key_set[0]["KeyName"] == "sdktest001"
    assert key_set[0]["Description"] == "SDK TEST MEMO"
    assert len(key_set[0]["InstancesSet"]) == 2
    assert key_set[0]["InstancesSet"][0]["InstanceId"] == "sdktest001"
    assert key_set[0]["InstancesSet"][1]["InstanceId"] == "sdktest002"

    # sdktest002
    assert key_set[1]["KeyName"] == "sdktest002"
    assert key_set[1]["Description"] == "SDK TEST MEMO 2"
    assert len(key_set[1]["InstancesSet"]) == 0


def test_describe_regions(client):
    regions = client.describe_regions()
    actual_regions = regions["RegionInfo"]
    expected_regions = [
        {
            "RegionName": "east-1",
            "RegionEndpoint": "east-1.cp.cloud.nifty.com"
        },
        {
            "RegionName": "east-2",
            "RegionEndpoint": "east-2.cp.cloud.nifty.com"
        },
        {
            "RegionName": "east-3",
            "RegionEndpoint": "east-3.cp.cloud.nifty.com"
        },
        {
            "RegionName": "jp-east-4",
            "RegionEndpoint": "jp-east-4.cp.cloud.nifty.com"
        },
        {
            "RegionName": "west-1",
            "RegionEndpoint": "west-1.cp.cloud.nifty.com"
        }
    ]
    for actual, expected in zip(actual_regions, expected_regions):
        assert actual["RegionName"] == expected["RegionName"]
        assert actual["RegionEndpoint"] == expected["RegionEndpoint"]


def test_describe_load_balancers(client):
    load_balancers = client.describe_load_balancers()["DescribeLoadBalancersResult"]  # noqa: E501
    describe_load_balancers_assertions(load_balancers)


def test_describe_load_balancers_with_parameters(client):
    load_balancers = client.describe_load_balancers(
        LoadBalancerNames=[{
            "LoadBalancerName": "sdktestlb001",
            "LoadBalancerPort": 80,
            "InstancePort": 80
        }]
    )["DescribeLoadBalancersResult"]
    describe_load_balancers_assertions(load_balancers)


def describe_load_balancers_assertions(result):
    assert len(result["LoadBalancerDescriptions"]) == 1
    load_balancer = result["LoadBalancerDescriptions"][0]
    assert load_balancer["LoadBalancerName"] == "sdktestlb001"
    assert type(load_balancer["DNSName"]) == str
    assert load_balancer["NetworkVolume"] == 10
    # assert load_balancer["PolicyType"] == "standard"
    assert len(load_balancer["ListenerDescriptions"]) == 1
    listener = load_balancer["ListenerDescriptions"][0]
    assert listener["Listener"] == {
        "Protocol": "HTTP",
        "LoadBalancerPort": 80,
        "InstancePort": 80,
        "BalancingType": 1
    }
    assert load_balancer["Policies"] == {
        'AppCookieStickinessPolicies': [
            {'CookieName': '', 'PolicyName': ''}
        ],
        'LBCookieStickinessPolicies': [
            {'CookieExpirationPeriod': '', 'PolicyName': ''}
        ]
    }
    assert load_balancer["AvailabilityZones"] == ["east-11"]
    assert len(load_balancer["Instances"]) == 1
    instance = load_balancer["Instances"][0]
    assert instance["InstanceId"] == "sdktest001"
    assert type(instance["InstanceUniqueId"]) == str
    health_check = load_balancer["HealthCheck"]
    assert health_check["HealthyThreshold"] == 1
    assert len(health_check["InstanceStates"]) == 1
    instance_states = health_check["InstanceStates"][0]
    assert instance_states["Description"] == ""
    assert instance_states["InstanceId"] == "sdktest001"
    assert type(instance_states["InstanceUniqueId"]) == str
    assert instance_states["ReasonCode"] == ""
    assert instance_states["State"] == "OutOfService"
    assert health_check["Interval"] == 30
    assert health_check["Target"] == "TCP:80"
    assert health_check["Timeout"] == 30
    assert health_check["UnhealthyThreshold"] == 1
    assert load_balancer["Filter"]["FilterType"] == "1"
    assert len(load_balancer["Filter"]["IPAddresses"]) == 1
    ip_address = load_balancer["Filter"]["IPAddresses"][0]
    assert type(ip_address["IPAddress"]) == str
    assert type(load_balancer["CreatedTime"]) == datetime
    assert load_balancer["AccountingType"] == "2"
    assert load_balancer["NextMonthAccountingType"] == "2"
