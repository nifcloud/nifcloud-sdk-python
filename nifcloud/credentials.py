from botocore.credentials import EnvProvider, SharedCredentialProvider

EnvProvider.ACCESS_KEY = "NIFCLOUD_ACCESS_KEY_ID"
EnvProvider.SECRET_KEY = "NIFCLOUD_SECRET_ACCESS_KEY"

SharedCredentialProvider.ACCESS_KEY = 'nifcloud_access_key_id'
SharedCredentialProvider.SECRET_KEY = 'nifcloud_secret_access_key'
