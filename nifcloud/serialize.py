from botocore import serialize


# handles both Hoge.1 / Hoges.member.1 parameter according to locationName
class ComputingSerializer(serialize.EC2Serializer):

    def serialize_to_request(self, parameters, operation_model):
        serialized = super(ComputingSerializer, self).serialize_to_request(
            parameters, operation_model
        )
        serialized['url_path'] = operation_model.http.get('requestUri', '/')
        # Fix request parameters of DescribeLoadBalancers for NIFCLOUD
        if operation_model.name == 'DescribeLoadBalancers':
            serialized["body"] = self._fix_describe_load_balancers_params(
                parameters, operation_model.metadata['apiVersion']
            )
        return serialized

    def _fix_describe_load_balancers_params(self, params, api_version):
        prefix = 'LoadBalancerNames'
        body = {
            "Action": "DescribeLoadBalancers",
            "Version": api_version
        }
        if not params.get(prefix):
            return body
        for i, param in enumerate(params[prefix]):
            i += 1
            body['%s.member.%d' % (prefix, i)] = param['LoadBalancerName']
            body['%s.LoadBalancerPort.%d' % (prefix, i)] = param['LoadBalancerPort']  # noqa: E501
            body['%s.InstancePort.%d' % (prefix, i)] = param['InstancePort']
        return body

    def _serialize_type_list(self, serialized, value, shape, prefix=''):
        # 'locationName' is renamed to 'name'
        # https://github.com/boto/botocore/blob/cccfdf86bc64877ad41e0af74b752b8a49fc4d33/botocore/model.py#L118
        if shape.member.serialization.get('name'):
            serializer = serialize.QuerySerializer()
        else:
            serializer = super(ComputingSerializer, self)
        serializer._serialize_type_list(serialized, value, shape, prefix)


class ScriptSerializer(serialize.QuerySerializer):
    def serialize_to_request(self, parameters, operation_model):
        serialized = super(ScriptSerializer, self).serialize_to_request(
            parameters, operation_model
        )
        target = '%s.%s' % (operation_model.metadata['targetPrefix'],
                            operation_model.name)
        serialized['headers']['X-Amz-Target'] = target
        serialized['url_path'] = operation_model.http.get('requestUri', '/')
        del serialized['body']['Action']
        del serialized['body']['Version']
        return serialized


serialize.SERIALIZERS.update({
    'computing': ComputingSerializer,
    'script': ScriptSerializer
})
