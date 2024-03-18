import re

from botocore import docs
from botocore.docs import client, service

NIFCLOUD_DOC_BASE = 'https://pfs.nifcloud.com/api'


class ClientDocumenter(client.ClientDocumenter):

    def _add_model_driven_method(self, section, method_name):
        super()._add_model_driven_method(section, method_name)
        operation_name = self._client.meta.method_to_api_mapping[method_name]
        if self._service_name == "computing":
            replace = r"\1<%s/rest/%s.htm>\2" % (NIFCLOUD_DOC_BASE,
                                                 operation_name)
        elif self._service_name == "storage":
            replace = r"\1<%s/object-storage-service/%s.htm>\2" % (NIFCLOUD_DOC_BASE,
                                                                   operation_name)
        else:
            replace = r"\1<%s/%s/%s.htm>\2" % (NIFCLOUD_DOC_BASE,
                                               self._service_name,
                                               operation_name)
        method_intro = section.get_section('method-intro')
        replaced_text = re.sub(
            r"([\s\S]+)<.+>(.+)$",
            replace,
            method_intro.getvalue().decode('utf8')
        ).replace('AWS', 'NIFCLOUD')
        method_intro.clear_text()
        method_intro.push_write(replaced_text)


class ServiceDocumenter(service.ServiceDocumenter):

    def __init__(self, service_name, session, root_docs_path):
        self._session = session
        self._service_name = service_name
        self._root_docs_path = root_docs_path

        self._client = self._session.create_client(
            service_name, region_name='jp-east-1', nifcloud_access_key_id='foo',
            nifcloud_secret_access_key='bar')
        self._event_emitter = self._client.meta.events

        self.sections = [
            'title',
            'table-of-contents',
            'client-api',
            'client-exceptions',
            'paginator-api',
            'waiter-api'
        ]


docs.ServiceDocumenter = ServiceDocumenter
service.ClientDocumenter = ClientDocumenter
