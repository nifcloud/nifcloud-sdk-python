# NIFCLOUD SDK for Python (Developer Preview)

[![Test](https://github.com/nifcloud/nifcloud-sdk-python/workflows/Test/badge.svg)](https://github.com/nifcloud/nifcloud-sdk-python/actions?query=workflow%3ATest)
[![Documentation](https://readthedocs.org/projects/nifcloud-sdk-python/badge)](https://nifcloud-sdk-python.readthedocs.io/en/latest/)
[![PyPI](https://badge.fury.io/py/nifcloud.svg)](https://pypi.python.org/pypi/nifcloud)

The **NIFCLOUD SDK for Python (Develper Preview)** is data-driven SDK.
It works by feeding AWS-SDK-compatible model JSONs to botocore module.

## Features

* :heavy_check_mark: Full support for NIFCLOUD Computing / RDB / NAS / Script / Hatoba APIs
* :heavy_check_mark: Useful CLI tool for debugging
* :heavy_check_mark: AWS-SDK-compatible data-driven architecture

## Requirements

* Python 2.6 or later

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
    aws_access_key_id="<Your NIFCLOUD Access Key ID>",
    aws_secret_access_key="<Your NIFCLOUD Secret Access Key>"
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
$ export AWS_ACCESS_KEY_ID=<Your NIFCLOUD Access Key ID>
$ export AWS_SECRET_ACCESS_KEY=<Your NIFCLOUD Secret Access Key>
$ export AWS_DEFAULT_REGION=jp-east-1
$ python test.py
```

See [documentation](https://nifcloud-sdk-python.readthedocs.io/en/latest/) for detail.

## Debug with CLI

`nifcloud` module comes with `nifcloud-debugcli` command. You can use it like below:

```
## Set credentials and default region
$ export AWS_ACCESS_KEY_ID=<Your NIFCLOUD Access Key ID>
$ export AWS_SECRET_ACCESS_KEY=<Your NIFCLOUD Secret Access Key>
$ export AWS_DEFAULT_REGION=jp-east-1

## Show available services
$ nifcloud-debugcli help

## Show available actions for the service
$ nifcloud-debugcli computing help

## Show available parameters for the action
$ nifcloud-debugcli computing create-key-pair help

## Run the command actually
$ nifcloud-debugcli computing create-key-pair --key-name foobar123 --password foobar123 
```

## Notes for Developer Preview

* It is not recommended to integrate this module into production systems.
* There will be some request parameters which can not be specified, and response items which can not be retrieved.
* Significant change of the specification will be made without any notice.

## License

See [LICENSE.txt](LICENSE.txt).
