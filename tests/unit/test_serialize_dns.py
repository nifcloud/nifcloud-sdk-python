from botocore.model import ServiceModel

from nifcloud import serialize


class TestDnsSerializer(object):
    dns_model_metadata = {
        "apiVersion": "2012-12-12N2013-12-16",
        "endpointPrefix": "dns",
        "protocol": "rest-xml",
        "serviceAbbreviation": "dns",
        "serviceFullName": "NIFCLOUD DNS",
        "serviceId": "dns",
        "signatureVersion": "v3",
        "uid": "dns-2012-12-12N2013-12-16"
    }

    def test_DnsSerializer(self):
        dns_model = {
            "metadata": self.dns_model_metadata,
            "operations": {
                "DnsOperation": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/2012-12-12N2013-12-16/operation"
                    },
                    "input": {
                        "locationName": "DnsOperationRequest",
                        "shape": "DnsOperationRequest",
                        "xmlNamespace": {
                            "uri": "https://route53.amazonaws.com/doc/2012-12-12/"
                        }
                    },
                    "name": "DnsOperation",
                    "output": {
                        "shape": "DnsOperationResult"
                    }
                },
            },
            "shapes": {
                "DnsOperationRequest": {
                    "members": {
                        "Parameter": {
                            "locationName": "Parameter",
                            "shape": "String"
                        },
                    },
                    "name": "DnsOperationRequest",
                    "type": "structure"
                },
                "DnsOperationResult": {
                    "members": {
                        "HostedZone": {
                            "locationName": "HostedZone",
                            "shape": "String"
                        }
                    },
                    "name": "DnsOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
            }
        }

        dns_service_model = ServiceModel(dns_model)
        params = {
            "Parameter": "test"
        }
        dns_serializer = serialize.DnsSerializer()
        res = dns_serializer.serialize_to_request(
            params, dns_service_model.operation_model("DnsOperation"))
        assert res["body"] == b'<DnsOperationRequest xmlns="https://route53.amazonaws.com/doc/2012-12-12/"><Parameter>test</Parameter></DnsOperationRequest>'  # noqa: E501
        assert res["headers"] == {}
        assert res["method"] == "POST"
        assert res["query_string"] == {}
        assert res["url_path"] == "/2012-12-12N2013-12-16/operation"
