import ssl

from botocore import __version__ as botocore_version
from botocore import session
from botocore.httpsession import URLLib3Session
from botocore.session import get_session  # noqa: F401

import nifcloud

# for ncl4lb
extra_ciphers = "AES256-SHA256"

ssl_context = ssl.create_default_context()
default_ciphers = ssl_context.get_ciphers()
default_cipher_names = ":".join(c['name'] for c in default_ciphers)
ssl_context.set_ciphers(f"{default_cipher_names}:{extra_ciphers}")


class CustomURLLib3Session(URLLib3Session):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._manager.connection_pool_kw['ssl_context'] = ssl_context


class Session(session.Session):

    def __init__(self, session_vars=None, event_hooks=None,
                 include_builtin_handlers=True, profile=None):
        super(Session, self).__init__(session_vars, event_hooks,
                                      include_builtin_handlers, profile)
        self.user_agent_name = 'nifcloud'
        self.user_agent_version = nifcloud.__version__
        self.user_agent_extra = 'botocore/%s' % botocore_version

    def create_client(self, service_name, region_name=None, api_version=None,
                      use_ssl=True, verify=None, endpoint_url=None,
                      nifcloud_access_key_id=None, nifcloud_secret_access_key=None,
                      nifcloud_session_token=None, config=None):
        client = super(Session, self).create_client(
            service_name, region_name=region_name, api_version=api_version, use_ssl=use_ssl,
            verify=verify, endpoint_url=endpoint_url, aws_access_key_id=nifcloud_access_key_id,
            aws_secret_access_key=nifcloud_secret_access_key, aws_session_token=nifcloud_session_token, config=config
        )
        client._endpoint.http_session = CustomURLLib3Session()
        return client


session.Session = Session
