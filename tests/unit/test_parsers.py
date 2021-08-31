from datetime import datetime

import pytest
from dateutil import tz

from nifcloud import parsers


def test_parse_timestamp_is_none():
    cqp = parsers.ComputingQueryParser()
    assert cqp.parse_timestamp("") is None


@pytest.mark.parametrize('val, expected', [
    # computing https://pfs.nifcloud.com/api/rest/DescribeInstances.htm
    ("2010-05-17T11:22:33.456+09:00", datetime(2010, 5, 17, 11, 22, 33, 456000, tz.gettz('Asia/Tokyo'))),
    # rdb https://pfs.nifcloud.com/api/rdb/DescribeDBInstances.htm
    ("2014-12-16T06:57:32.000Z", datetime(2014, 12, 16, 6, 57, 32, 0, tz.gettz('UTC'))),
    # nas https://pfs.nifcloud.com/api/nas/DescribeNASInstances.htm
    ("2016-02-02T09:07:40.000+09:00", datetime(2016, 2, 2, 9, 7, 40, 0, tz.gettz('Asia/Tokyo'))),
    # hatoba https://pfs.nifcloud.com/api/kubernetes-service-hatoba/ListClusters.htm
    ("2019-07-24T00:00:00Z", datetime(2019, 7, 24, 0, 0, 0, 0, tz.gettz('UTC')))
])
def test_parse_timestamp_service_format(val, expected):
    cqp = parsers.ComputingQueryParser()
    assert cqp.parse_timestamp(val) == expected
