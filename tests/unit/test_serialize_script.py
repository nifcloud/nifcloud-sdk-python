from botocore.model import ServiceModel

from nifcloud import serialize


class TestScriptSerializer(object):
    script_model_metadata = {
        "apiVersion": "2015-09-01",
        "endpointPrefix": "script",
        "protocol": "script",
        "serviceAbbreviation": "script",
        "serviceFullName": "NIFCLOUD Script",
        "serviceId": "script",
        "signatureVersion": "v4",
        "targetPrefix": "2015-09-01",
        "uid": "script-2015-09-01"
    }

    def test_ScriptSerializer(self):
        script_model = {
            "metadata": self.script_model_metadata,
            "operations": {
                "ExecuteScript": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/2015-09-01/"
                    },
                    "input": {
                        "shape": "ExecuteScriptRequest"
                    },
                    "name": "ExecuteScript",
                    "output": {
                        "resultWrapper": "ExecuteScriptResult",
                        "shape": "ExecuteScriptResult"
                    }
                }
            },
            "shapes": {
                "ExecuteScriptRequest": {
                    "members": {
                        "Body": {
                            "locationName": "Body",
                            "shape": "String"
                        },
                        "Header": {
                            "locationName": "Header",
                            "shape": "String"
                        },
                        "Method": {
                            "locationName": "Method",
                            "shape": "String"
                        },
                        "Query": {
                            "locationName": "Query",
                            "shape": "String"
                        },
                        "ScriptIdentifier": {
                            "locationName": "ScriptIdentifier",
                            "shape": "String"
                        }
                    },
                    "name": "ExecuteScriptRequest",
                    "required": [
                        "Method",
                        "ScriptIdentifier"
                    ],
                    "type": "structure"
                },
                "ExecuteScriptResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "ExecuteScriptResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
            }
        }

        script_service_model = ServiceModel(script_model)
        params = {
            "Body": "test_body",
            "Header": "test_header",
            "Method": "test_method",
            "Query": "test_query",
            "ScriptIdentifier": "test_script_identifier"
        }
        script_serializer = serialize.ScriptSerializer()
        res = script_serializer.serialize_to_request(
            params, script_service_model.operation_model("ExecuteScript"))
        assert res["body"] == {
            "Body": "test_body",
            "Header": "test_header",
            "Method": "test_method",
            "Query": "test_query",
            "ScriptIdentifier": "test_script_identifier"
        }
        assert res["headers"] == {
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "X-Amz-Target": "2015-09-01.ExecuteScript"
        }
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/2015-09-01/"

    def test_ScriptSerializer_delete_action_version(self):
        script_model = {
            "metadata": self.script_model_metadata,
            "operations": {
                "ExecuteScript": {
                    "http": {
                        "method": "POST",
                        "requestUri": "/2015-09-01/"
                    },
                    "input": {
                        "shape": "ExecuteScriptRequest"
                    },
                    "name": "ExecuteScript",
                    "output": {
                        "resultWrapper": "ExecuteScriptResult",
                        "shape": "ExecuteScriptResult"
                    }
                }
            },
            "shapes": {
                "ExecuteScriptRequest": {
                    "members": {
                        "Body": {
                            "locationName": "Body",
                            "shape": "String"
                        },
                        "Header": {
                            "locationName": "Header",
                            "shape": "String"
                        },
                        "Method": {
                            "locationName": "Method",
                            "shape": "String"
                        },
                        "Query": {
                            "locationName": "Query",
                            "shape": "String"
                        },
                        "ScriptIdentifier": {
                            "locationName": "ScriptIdentifier",
                            "shape": "String"
                        },
                        "Action": {
                            "locationName": "Action",
                            "shape": "String"
                        },
                        "Version": {
                            "locationName": "Version",
                            "shape": "String"
                        },
                    },
                    "name": "ExecuteScriptRequest",
                    "required": [
                        "Method",
                        "ScriptIdentifier"
                    ],
                    "type": "structure"
                },
                "ExecuteScriptResult": {
                    "members": {
                        "Response": {
                            "locationName": "Response",
                            "shape": "String"
                        }
                    },
                    "name": "ExecuteScriptResult",
                    "type": "structure"
                },
                "String": {
                    "name": "String",
                    "type": "string"
                },
            }
        }

        script_service_model = ServiceModel(script_model)
        params = {
            "Body": "test_body",
            "Header": "test_header",
            "Method": "test_method",
            "Query": "test_query",
            "ScriptIdentifier": "test_script_identifier",
            "Action": "test_action",
            "Version": "test_version"
        }
        script_serializer = serialize.ScriptSerializer()
        res = script_serializer.serialize_to_request(
            params, script_service_model.operation_model("ExecuteScript"))
        assert res["body"] == {
            "Body": "test_body",
            "Header": "test_header",
            "Method": "test_method",
            "Query": "test_query",
            "ScriptIdentifier": "test_script_identifier"
        }
        assert res["headers"] == {
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "X-Amz-Target": "2015-09-01.ExecuteScript"
        }
        assert res["method"] == "POST"
        assert res["query_string"] == ""
        assert res["url_path"] == "/2015-09-01/"
