from botocore.model import ServiceModel

from nifcloud import serialize


class TestNasSerializer(object):
    nas_model_metadata = {
        "apiVersion": "N2016-02-24",
        "endpointPrefix": "nas",
        "protocol": "nas",
        "serviceAbbreviation": "nas",
        "serviceFullName": "NIFCLOUD NAS",
        "serviceId": "nas",
        "signatureVersion": "v4",
        "uid": "nas-N2016-02-24"
    }

    def test_NasSerializer(self):
        nas_model = {
            "metadata": self.nas_model_metadata,
            "operations": {
                "NasOperation": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "NasOperationRequest"
                    },
                    "name": "NasOperation",
                    "output": {
                        "shape": "NasOperationResult"
                    }
                }
            },
            "shapes": {
                "NasOperationRequest": {
                    "members": {
                        "Parameter": {
                            "locationName": "Parameter",
                            "shape": "String"
                        }
                    },
                    "name": "NasOperationRequest",
                    "type": "structure"
                },
                "NasOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "NasOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
            }
        }

        nas_service_model = ServiceModel(nas_model)
        params = {
            "Parameter": "test"
        }
        nas_serializer = serialize.NasSerializer()
        res = nas_serializer.serialize_to_request(
            params, nas_service_model.operation_model("NasOperation"))
        assert res["body"] == {"Action": "NasOperation", "Parameter": "test", "Version": "N2016-02-24"}
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"

    def test_NasSerializer_fix_get_metrics_statistics_params(self):
        nas_model = {
            "metadata": self.nas_model_metadata,
            "operations": {
                "GetMetricStatistics": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "GetMetricStatisticsRequest"
                    },
                    "name": "GetMetricStatistics",
                    "output": {
                        "resultWrapper": "NasOperationResult",
                        "shape": "NasOperationResult"
                    }
                },
            },
            "shapes": {
                "GetMetricStatisticsRequest": {
                    "members": {
                        "Dimensions": {
                            "locationName": "Dimensions",
                            "shape": "ListOfRequestDimensions"
                        },
                        "EndTime": {
                            "locationName": "EndTime",
                            "shape": "TStamp"
                        },
                        "MetricName": {
                            "locationName": "MetricName",
                            "shape": "String"
                        },
                        "StartTime": {
                            "locationName": "StartTime",
                            "shape": "TStamp"
                        }
                    },
                    "name": "GetMetricStatisticsRequest",
                    "type": "structure"
                },
                "ListOfRequestDimensions": {
                    "member": {
                        "locationName": "member",
                        "shape": "RequestDimensions"
                    },
                    "name": "ListOfRequestDimensions",
                    "type": "list"
                },
                "RequestDimensions": {
                    "members": {
                        "Name": {
                            "locationName": "Name",
                            "shape": "String"
                        },
                        "Value": {
                            "locationName": "Value",
                            "shape": "String"
                        }
                    },
                    "name": "RequestDimensions",
                    "required": [
                        "Name",
                        "Value"
                    ],
                    "type": "structure"
                },
                "NasOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "NasOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
                "TStamp": {
                    "name": "TStamp",
                    "type": "timestamp"
                }
            }
        }

        nas_service_model = ServiceModel(nas_model)
        params = {}
        nas_serializer = serialize.NasSerializer()
        res = nas_serializer.serialize_to_request(
            params, nas_service_model.operation_model("GetMetricStatistics"))
        assert res["body"] == {
            "Action": "GetMetricStatistics",
            "Version": "N2016-02-24"
        }
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"

    def test_NasSerializer_fix_get_metrics_statistics_params_MetricName_Dimensions(self):
        nas_model = {
            "metadata": self.nas_model_metadata,
            "operations": {
                "GetMetricStatistics": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "GetMetricStatisticsRequest"
                    },
                    "name": "GetMetricStatistics",
                    "output": {
                        "resultWrapper": "NasOperationResult",
                        "shape": "NasOperationResult"
                    }
                },
            },
            "shapes": {
                "GetMetricStatisticsRequest": {
                    "members": {
                        "Dimensions": {
                            "locationName": "Dimensions",
                            "shape": "ListOfRequestDimensions"
                        },
                        "EndTime": {
                            "locationName": "EndTime",
                            "shape": "TStamp"
                        },
                        "MetricName": {
                            "locationName": "MetricName",
                            "shape": "String"
                        },
                        "StartTime": {
                            "locationName": "StartTime",
                            "shape": "TStamp"
                        }
                    },
                    "name": "GetMetricStatisticsRequest",
                    "required": [
                        "MetricName",
                        "Dimensions"
                    ],
                    "type": "structure"
                },
                "ListOfRequestDimensions": {
                    "member": {
                        "locationName": "member",
                        "shape": "RequestDimensions"
                    },
                    "name": "ListOfRequestDimensions",
                    "type": "list"
                },
                "RequestDimensions": {
                    "members": {
                        "Name": {
                            "locationName": "Name",
                            "shape": "String"
                        },
                        "Value": {
                            "locationName": "Value",
                            "shape": "String"
                        }
                    },
                    "name": "RequestDimensions",
                    "required": [
                        "Name",
                        "Value"
                    ],
                    "type": "structure"
                },
                "NasOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "NasOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
                "TStamp": {
                    "name": "TStamp",
                    "type": "timestamp"
                }
            }
        }

        nas_service_model = ServiceModel(nas_model)
        params = {
            "MetricName": "test_metric_name",
            "Dimensions": [
                {"Name": "test_dimensions_name", "Value": "test_value"}
            ]
        }
        nas_serializer = serialize.NasSerializer()
        res = nas_serializer.serialize_to_request(
            params, nas_service_model.operation_model("GetMetricStatistics"))
        assert res["body"] == {
            "Action": "GetMetricStatistics",
            "MetricName": "test_metric_name",
            "Version": "N2016-02-24",
            "Dimensions.member.1.Name": "test_dimensions_name",
            "Dimensions.member.1.Value": "test_value"
        }
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"
