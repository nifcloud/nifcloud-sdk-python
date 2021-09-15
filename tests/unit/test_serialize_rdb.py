from botocore.model import ServiceModel

from nifcloud import serialize


class TestRdbSerializer(object):
    rdb_model_metadata = {
        "apiVersion": "2013-05-15N2013-12-16",
        "endpointPrefix": "rdb",
        "protocol": "rdb",
        "serviceAbbreviation": "rdb",
        "serviceFullName": "NIFCLOUD RDB",
        "serviceId": "rdb",
        "signatureVersion": "v4",
        "uid": "rdb-2013-05-15N2013-12-16"
    }

    def test_RdbSerializer(self):
        rdb_model = {
            "metadata": self.rdb_model_metadata,
            "operations": {
                "RdbOperation": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "RdbOperationRequest"
                    },
                    "name": "rdbOperation",
                    "output": {
                        "shape": "RdbOperationResult"
                    }
                }
            },
            "shapes": {
                "RdbOperationRequest": {
                    "members": {
                        "Parameter": {
                            "locationName": "Parameter",
                            "shape": "String"
                        }
                    },
                    "name": "RdbOperationRequest",
                    "type": "structure"
                },
                "RdbOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "RdbOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
            }
        }

        rdb_service_model = ServiceModel(rdb_model)
        params = {
            "Parameter": "test"
        }
        rdb_serializer = serialize.RdbSerializer()
        res = rdb_serializer.serialize_to_request(
            params, rdb_service_model.operation_model("RdbOperation"))
        assert res["body"] == {"Action": "RdbOperation", "Parameter": "test", "Version": "2013-05-15N2013-12-16"}
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"

    def test_RdbSerializer_fix_get_metrics_statistics_params(self):
        rdb_model = {
            "metadata": self.rdb_model_metadata,
            "operations": {
                "NiftyGetMetricStatistics": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "NiftyGetMetricStatisticsRequest"
                    },
                    "name": "NiftyGetMetricStatistics",
                    "output": {
                        "resultWrapper": "RdbOperationResult",
                        "shape": "RdbOperationResult"
                    }
                },
            },
            "shapes": {
                "NiftyGetMetricStatisticsRequest": {
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
                    "name": "NiftyGetMetricStatisticsRequest",
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
                "RdbOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "RdbOperationResult",
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

        rdb_service_model = ServiceModel(rdb_model)
        params = {}
        rdb_serializer = serialize.RdbSerializer()
        res = rdb_serializer.serialize_to_request(
            params, rdb_service_model.operation_model("NiftyGetMetricStatistics"))
        assert res["body"] == {
            "Action": "NiftyGetMetricStatistics",
            "Version": "2013-05-15N2013-12-16"
        }
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"

    def test_RdbSerializer_fix_get_metrics_statistics_params_MetricName_Dimensions(self):
        rdb_model = {
            "metadata": self.rdb_model_metadata,
            "operations": {
                "NiftyGetMetricStatistics": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/"
                    },
                    "input": {
                        "shape": "NiftyGetMetricStatisticsRequest"
                    },
                    "name": "NiftyGetMetricStatistics",
                    "output": {
                        "resultWrapper": "RdbOperationResult",
                        "shape": "RdbOperationResult"
                    }
                },
            },
            "shapes": {
                "NiftyGetMetricStatisticsRequest": {
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
                    "name": "NiftyGetMetricStatisticsRequest",
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
                "RdbOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "RdbOperationResult",
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

        rdb_service_model = ServiceModel(rdb_model)
        params = {
            "MetricName": "test_metric_name",
            "Dimensions": [
                {"Name": "test_dimensions_name", "Value": "test_value"}
            ]
        }
        rdb_serializer = serialize.RdbSerializer()
        res = rdb_serializer.serialize_to_request(
            params, rdb_service_model.operation_model("NiftyGetMetricStatistics"))
        assert res["body"] == {
            "Action": "NiftyGetMetricStatistics",
            "MetricName": "test_metric_name",
            "Version": "2013-05-15N2013-12-16",
            "Dimensions.member.1.Name": "test_dimensions_name",
            "Dimensions.member.1.Value": "test_value"
        }
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/"
