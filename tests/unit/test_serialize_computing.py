import pytest
from botocore.model import ServiceModel

from nifcloud import serialize


class TestComputingSerializer(object):
    computing_model_metadata = {
        "apiVersion": "3.0",
        "endpointPrefix": "computing",
        "protocol": "computing",
        "serviceAbbreviation": "computing",
        "serviceFullName": "NIFCLOUD Computing",
        "serviceId": "computing",
        "signatureVersion": "v2",
        "uid": "computing-2016-11-15",
        "xmlNamespace": "https://computing.api.nifcloud.com/api/"
    }

    def test_ComputingSerializer(self):
        computing_model = {
            "metadata": self.computing_model_metadata,
            "operations": {
                "ComputingOperation": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/api/"
                    },
                    "input": {
                        "shape": "ComputingOperationRequest"
                    },
                    "name": "ComputingOperation",
                    "output": {
                        "shape": "ComputingOperationResult"
                    }
                }
            },
            "shapes": {
                "ComputingOperationRequest": {
                    "members": {
                        "Parameter": {
                            "locationName": "Parameter",
                            "shape": "String"
                        }
                    },
                    "name": "ComputingOperationRequest",
                    "type": "structure"
                },
                "ComputingOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "ComputingOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
            }
        }

        computing_service_model = ServiceModel(computing_model)
        params = {
            "Parameter": "test"
        }
        computing_serializer = serialize.ComputingSerializer()
        res = computing_serializer.serialize_to_request(
            params, computing_service_model.operation_model("ComputingOperation"))
        assert res["body"] == {"Action": "ComputingOperation", "Parameter": "test", "Version": "3.0"}
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/api/"

    @pytest.mark.parametrize("api_name", [
        'RunInstances',
        'StartInstances',
        'RebootInstances',
    ])
    def test_ComputingSerializer_fix_user_data_param(self, api_name):
        computing_model = {
            "metadata": self.computing_model_metadata,
            "operations": {
                api_name: {
                    "http": {
                        "method": "POST",
                        "requestUri": "/api/"
                    },
                    "input": {
                        "shape": "ComputingOperationRequest"
                    },
                    "name": api_name,
                    "output": {
                        "shape": "ComputingOperationResult"
                    }
                }
            },
            "shapes": {
                "ComputingOperationRequest": {
                    "members": {
                        "UserData": {
                            "locationName": "UserData",
                            "shape": "RequestUserData"
                        }
                    },
                    "name": "ComputingOperationRequest",
                    "type": "structure"
                },
                "ComputingOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "ComputingOperationResult",
                    "type": "structure"
                },
                "RequestUserData": {
                    "members": {
                        "Content": {
                            "locationName": "Content",
                            "shape": "String"
                        },
                        "Encoding": {
                            "locationName": "Encoding",
                            "shape": "String"
                        }
                    },
                    "name": "RequestUserData",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
            }
        }
        computing_service_model = ServiceModel(computing_model)
        params = {
            "UserData": {
                "Content": "test_content",
                "Encoding": "test_content_encoding"
            }
        }
        computing_serializer = serialize.ComputingSerializer()
        res = computing_serializer.serialize_to_request(params, computing_service_model.operation_model(api_name))
        assert res["body"] == {
            "Action": api_name,
            "UserData": "test_content",
            "UserData.Encoding": "test_content_encoding",
            "Version": "3.0"
        }
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/api/"

    def test_ComputingSerializer_fix_describe_load_balancers_params(self):
        computing_model = {
            "metadata": self.computing_model_metadata,
            "operations": {
                "DescribeLoadBalancers": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/api/"
                    },
                    "input": {
                        "shape": "DescribeLoadBalancersRequest"
                    },
                    "name": "DescribeLoadBalancers",
                    "output": {
                        "shape": "ComputingOperationResult"
                    }
                }
            },
            "shapes": {
                "DescribeLoadBalancersRequest": {
                    "members": {
                        "LoadBalancerNames": {
                            "locationName": "LoadBalancerNames",
                            "shape": "ListOfRequestLoadBalancerNames"
                        },
                        "Patamator": {
                            "locationName": "Patamator",
                            "shape": "String"
                        }
                    },
                    "name": "DescribeLoadBalancersRequest",
                    "type": "structure"
                },
                "ListOfRequestLoadBalancerNames": {
                    "member": {
                        "locationName": "member",
                        "shape": "RequestLoadBalancerNames"
                    },
                    "name": "ListOfRequestLoadBalancerNames",
                    "type": "list"
                },
                "RequestLoadBalancerNames": {
                    "members": {
                        "InstancePort": {
                            "locationName": "InstancePort",
                            "shape": "Integer"
                        },
                        "LoadBalancerName": {
                            "locationName": "LoadBalancerName",
                            "shape": "String"
                        },
                        "LoadBalancerPort": {
                            "locationName": "LoadBalancerPort",
                            "shape": "Integer"
                        }
                    },
                    "name": "RequestLoadBalancerNames",
                    "type": "structure"
                },
                "ComputingOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "ComputingOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
                "Integer": {
                    "name": "Integer",
                    "type": "integer"
                },
            }
        }
        computing_service_model = ServiceModel(computing_model)
        params = {}
        computing_serializer = serialize.ComputingSerializer()
        res = computing_serializer.serialize_to_request(
            params, computing_service_model.operation_model("DescribeLoadBalancers"))
        assert res["body"] == {
            "Action": "DescribeLoadBalancers",
            "Version": "3.0"
        }
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/api/"

    def test_ComputingSerializer_fix_describe_load_balancers_params_with_loadbalancer_name(self):
        computing_model = {
            "metadata": self.computing_model_metadata,
            "operations": {
                "DescribeLoadBalancers": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/api/"
                    },
                    "input": {
                        "shape": "DescribeLoadBalancersRequest"
                    },
                    "name": "DescribeLoadBalancers",
                    "output": {
                        "shape": "ComputingOperationResult"
                    }
                }
            },
            "shapes": {
                "DescribeLoadBalancersRequest": {
                    "members": {
                        "LoadBalancerNames": {
                            "locationName": "LoadBalancerNames",
                            "shape": "ListOfRequestLoadBalancerNames"
                        },
                        "Patamator": {
                            "locationName": "Patamator",
                            "shape": "String"
                        }
                    },
                    "name": "DescribeLoadBalancersRequest",
                    "type": "structure"
                },
                "ListOfRequestLoadBalancerNames": {
                    "member": {
                        "locationName": "member",
                        "shape": "RequestLoadBalancerNames"
                    },
                    "name": "ListOfRequestLoadBalancerNames",
                    "type": "list"
                },
                "RequestLoadBalancerNames": {
                    "members": {
                        "InstancePort": {
                            "locationName": "InstancePort",
                            "shape": "Integer"
                        },
                        "LoadBalancerName": {
                            "locationName": "LoadBalancerName",
                            "shape": "String"
                        },
                        "LoadBalancerPort": {
                            "locationName": "LoadBalancerPort",
                            "shape": "Integer"
                        }
                    },
                    "name": "RequestLoadBalancerNames",
                    "type": "structure"
                },
                "ComputingOperationResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "ComputingOperationResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
                "Integer": {
                    "name": "Integer",
                    "type": "integer"
                },
            }
        }
        computing_service_model = ServiceModel(computing_model)
        params = {
            "LoadBalancerNames": [
                    {
                        "LoadBalancerName": "test_load_balancer_name",
                        "LoadBalancerPort": "test_load_balancer_port",
                        "InstancePort": "test_instance_port"
                    }
                ]
        }
        computing_serializer = serialize.ComputingSerializer()
        res = computing_serializer.serialize_to_request(
            params, computing_service_model.operation_model("DescribeLoadBalancers"))
        assert res["body"] == {
            "Action": "DescribeLoadBalancers",
            "Version": "3.0",
            "LoadBalancerNames.member.1": "test_load_balancer_name",
            "LoadBalancerNames.LoadBalancerPort.1": "test_load_balancer_port",
            "LoadBalancerNames.InstancePort.1": "test_instance_port"
        }
        assert res["headers"] == {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/api/"
