# NIFCLOUD SDK for Python

[![Test](https://github.com/nifcloud/nifcloud-sdk-python/workflows/Test/badge.svg)](https://github.com/nifcloud/nifcloud-sdk-python/actions?query=workflow%3ATest)
[![Documentation](https://readthedocs.org/projects/nifcloud-sdk-python/badge)](https://nifcloud-sdk-python.readthedocs.io/en/latest/)
[![PyPI](https://badge.fury.io/py/nifcloud.svg)](https://pypi.python.org/pypi/nifcloud)

The **NIFCLOUD SDK for Python** is data-driven SDK.
It works by feeding AWS-SDK-compatible model JSONs to botocore module.

## Features

* :heavy_check_mark: Full support for NIFCLOUD Computing / RDB / NAS / Script / Hatoba / ESS / DNS / ObjectStorageService / ServiceActivity APIs
* :heavy_check_mark: The nifcloud package is the foundation for the [NIFCLOUD CLI](https://github.com/nifcloud/nifcloud-cli).
* :heavy_check_mark: AWS-SDK-compatible data-driven architecture

## Requirements

- Python 3.7 or later

## How to Install

```
pip install nifcloud
```

## Usage

Write your python program:

```python
from nifcloud import session

client = session.get_session().create_client(
    "computing",
    region_name="jp-east-1",
    nifcloud_access_key_id="<Your NIFCLOUD Access Key ID>",
    nifcloud_secret_access_key="<Your NIFCLOUD Secret Access Key>"
)

print(client.describe_instances())
```

Execute the program:

```
$ python test.py
```

Credentials and region name can be also passed via environment variables.

```python
from nifcloud import session

client = session.get_session().create_client("computing")
print(client.describe_instances())
```

```
$ export NIFCLOUD_ACCESS_KEY_ID=<Your NIFCLOUD Access Key ID>
$ export NIFCLOUD_SECRET_ACCESS_KEY=<Your NIFCLOUD Secret Access Key>
$ export NIFCLOUD_DEFAULT_REGION=jp-east-1
$ python test.py
```

See [documentation](https://nifcloud-sdk-python.readthedocs.io/en/latest/) for detail.

## License

See [LICENSE.txt](LICENSE.txt).
