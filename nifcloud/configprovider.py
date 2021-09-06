from botocore import configprovider

configprovider.BOTOCORE_DEFAUT_SESSION_VARIABLES.update({
    'profile': (None, ['NIFCLOUD_DEFAULT_PROFILE', 'NIFCLOUD_PROFILE'], None, None),
    'region': ('region', 'NIFCLOUD_DEFAULT_REGION', None, None),
    'data_path': ('data_path', 'NIFCLOUD_DATA_PATH', None, None),
    'config_file': (None, 'NIFCLOUD_CONFIG_FILE', '~/.nifcloud/config', None),
    'credentials_file': (
        None, 'NIFCLOUD_SHARED_CREDENTIALS_FILE', '~/.nifcloud/credentials', None
    )
})
