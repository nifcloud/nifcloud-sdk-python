import re

from botocore.docs import generate_docs  # noqa: F401
from botocore.docs import client, service

NIFCLOUD_DOC_BASE = 'https://cloud.nifty.com/api'


class ClientDocumenter(client.ClientDocumenter):

    def _add_model_driven_method(self, section, method_name):
        super()._add_model_driven_method(section, method_name)
        operation_name = self._client.meta.method_to_api_mapping[method_name]
        if self._service_name == "computing":
            replace = r"\1<%s/rest/%s.htm>\2" % (NIFCLOUD_DOC_BASE,
                                                 operation_name)
        elif self._service_name == "script":
            replace = r"\1<%s/script/start.htm>\2" % (NIFCLOUD_DOC_BASE)
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


service.ClientDocumenter = ClientDocumenter
