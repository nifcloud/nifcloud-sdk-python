from botocore import configprovider

configprovider.BOTOCORE_DEFAUT_SESSION_VARIABLES.update({
    'config_file': (
        None, 'AWS_CONFIG_FILE', '~/.nifcloud/config', None
    ),
    'credentials_file': (
        None, 'AWS_SHARED_CREDENTIALS_FILE', '~/.nifcloud/credentials', None
    )
})
