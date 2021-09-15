from botocore.model import ServiceModel

from nifcloud import serialize


class TestEssSerializer(object):
    ess_model_metadata = {
        "apiVersion": "2010-12-01N2014-05-28",
        "endpointPrefix": "ess",
        "protocol": "ess",
        "serviceAbbreviation": "ess",
        "serviceFullName": "NIFCLOUD ESS",
        "serviceId": "ess",
        "signatureVersion": "v4",
        "signingName": "email",
        "uid": "ess-2010-12-01N2014-05-28"
    }

    def test_EssSerializer(self):
        ess_model = {
            "metadata": self.ess_model_metadata,
            "operations": {
                "EssOperation": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "EssOperationRequest"
                    },
                    "name": "essOperation",
                    "output": {
                        "shape": "EssOperationResult"
                    }
                }
            },
            "shapes": {
                "EssOperationRequest": {
                    "members": {
                        "Parameter": {
                            "locationName": "Parameter",
                            "shape": "String"
                        }
                    },
                    "name": "EssOperationRequest",
                    "type": "structure"
                },
                "EssOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "EssOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
            }
        }

        ess_service_model = ServiceModel(ess_model)
        params = {
            "Parameter": "test"
        }
        ess_serializer = serialize.EssSerializer()
        res = ess_serializer.serialize_to_request(
            params, ess_service_model.operation_model("EssOperation"))
        assert res["body"] == {"Action": "EssOperation", "Parameter": "test", "Version": "2010-12-01N2014-05-28"}
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"

    def test_EssSerializer_GetDeliveryLog(self):
        ess_model = {
            "metadata": self.ess_model_metadata,
            "operations": {
                "GetDeliveryLog": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "GetDeliveryLogRequest"
                    },
                    "name": "essOperation",
                    "output": {
                        "shape": "EssOperationResult"
                    }
                }
            },
            "shapes": {
                "GetDeliveryLogRequest": {
                    "members": {
                        "EndDate": {
                            "locationName": "EndDate",
                            "shape": "TStamp"
                        },
                        "MaxItems": {
                            "locationName": "MaxItems",
                            "shape": "Integer"
                        },
                        "NextToken": {
                            "locationName": "NextToken",
                            "shape": "String"
                        },
                        "StartDate": {
                            "locationName": "StartDate",
                            "shape": "TStamp"
                        },
                        "Status": {
                            "locationName": "Status",
                            "shape": "Integer"
                        }
                    },
                    "name": "GetDeliveryLogRequest",
                    "required": [
                        "EndDate",
                        "StartDate"
                    ],
                    "type": "structure"
                },
                "EssOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "EssOperationResult",
                    "type": "structure"
                },
                "Integer": {
                    "name": "Integer",
                    "type": "integer"
                },
                "TStamp": {
                    "name": "TStamp",
                    "type": "timestamp"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                }
            }
        }

        ess_service_model = ServiceModel(ess_model)
        params = {}
        ess_serializer = serialize.EssSerializer()
        res = ess_serializer.serialize_to_request(
            params, ess_service_model.operation_model("GetDeliveryLog"))
        assert res["body"] == {"Action": "GetDeliveryLog", "Version": "2010-12-01N2014-05-28"}
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"

    def test_EssSerializer_GetDeliveryLog_with_status(self):
        ess_model = {
            "metadata": self.ess_model_metadata,
            "operations": {
                "GetDeliveryLog": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "GetDeliveryLogRequest"
                    },
                    "name": "essOperation",
                    "output": {
                        "shape": "EssOperationResult"
                    }
                }
            },
            "shapes": {
                "GetDeliveryLogRequest": {
                    "members": {
                        "EndDate": {
                            "locationName": "EndDate",
                            "shape": "TStamp"
                        },
                        "MaxItems": {
                            "locationName": "MaxItems",
                            "shape": "Integer"
                        },
                        "NextToken": {
                            "locationName": "NextToken",
                            "shape": "String"
                        },
                        "StartDate": {
                            "locationName": "StartDate",
                            "shape": "TStamp"
                        },
                        "Status": {
                            "locationName": "Status",
                            "shape": "Integer"
                        }
                    },
                    "name": "GetDeliveryLogRequest",
                    "required": [
                        "EndDate",
                        "StartDate"
                    ],
                    "type": "structure"
                },
                "EssOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "EssOperationResult",
                    "type": "structure"
                },
                "Integer": {
                    "name": "Integer",
                    "type": "integer"
                },
                "TStamp": {
                    "name": "TStamp",
                    "type": "timestamp"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                }
            }
        }

        ess_service_model = ServiceModel(ess_model)
        params = {
            "Status": "test_status",
            "MaxItems": 1,
            "NextToken": "test_token",
            "StartDate": "2017-12-13T00:00:00Z",
            "EndDate": "2017-12-13T23:59:00Z"
        }
        ess_serializer = serialize.EssSerializer()
        res = ess_serializer.serialize_to_request(
            params, ess_service_model.operation_model("GetDeliveryLog"))
        assert res["body"] == {
            "Action": "GetDeliveryLog",
            "Version": "2010-12-01N2014-05-28",
            "Status": "test_status",
            "MaxItems": 1,
            "NextToken": "test_token",
            "StartDate": "2017-12-13T00:00",
            "EndDate": "2017-12-13T23:59"
        }
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"
