from datetime import datetime as dt

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
        # Fix user data param of below actions for NIFCLOUD
        user_data_fix_target = ['RunInstances',
                                'StartInstances',
                                'RebootInstances']
        if operation_model.name in user_data_fix_target:
            serialized = self._fix_user_data_param(
                serialized
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
        for i, param in enumerate(params[prefix], 1):
            body['%s.member.%d' % (prefix, i)] = param['LoadBalancerName']
            body['%s.LoadBalancerPort.%d' % (prefix, i)] = param['LoadBalancerPort']  # noqa: E501
            body['%s.InstancePort.%d' % (prefix, i)] = param['InstancePort']
        return body

    def _fix_user_data_param(self, serialized):
        if not serialized['body'].get('UserData.Content'):
            return serialized
        serialized['body']['UserData'] = serialized['body']['UserData.Content']
        del serialized['body']['UserData.Content']
        return serialized

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


class RdbSerializer(serialize.QuerySerializer):

    def serialize_to_request(self, parameters, operation_model):
        serialized = super(RdbSerializer, self).serialize_to_request(
            parameters, operation_model
        )
        serialized['url_path'] = operation_model.http.get('requestUri', '/')
        # Fix request parameters of NiftyGetMetricStatistics for NIFCLOUD RDB
        if operation_model.name == 'NiftyGetMetricStatistics':
            serialized["body"] = _fix_get_metrics_statistics_params(
                self,
                parameters,
                operation_model.metadata['apiVersion'],
                operation_model.name
            )
        return serialized


class NasSerializer(serialize.QuerySerializer):

    def serialize_to_request(self, parameters, operation_model):
        serialized = super(NasSerializer, self).serialize_to_request(
            parameters, operation_model
        )
        serialized['url_path'] = operation_model.http.get('requestUri', '/')
        # Fix request parameters of GetMetricStatistics for NIFCLOUD NAS
        if operation_model.name == 'GetMetricStatistics':
            serialized["body"] = _fix_get_metrics_statistics_params(
                self,
                parameters,
                operation_model.metadata['apiVersion'],
                operation_model.name
            )
        return serialized


class EssSerializer(serialize.QuerySerializer):

    def serialize_to_request(self, parameters, operation_model):
        serialized = super(EssSerializer, self).serialize_to_request(
            parameters, operation_model
        )
        serialized['url_path'] = operation_model.http.get('requestUri', '/')
        # Fix request parameters of GetDeliveryLog for NIFCLOUD ESS
        if operation_model.name == 'GetDeliveryLog':
            serialized["body"] = _fix_get_delivery_log_params(
                self,
                parameters,
                operation_model.metadata['apiVersion'],
                operation_model.name
            )
        return serialized


def _fix_get_metrics_statistics_params(
         self, params, api_version, operation_model_name):
    prefix = 'Dimensions'
    body = {
        "Action": operation_model_name,
        "Version": api_version
    }
    if not params.get(prefix) and not params.get('MetricName'):
        return body
    for i, param in enumerate(params[prefix], 1):
        body['%s.member.%d.Name' % (prefix, i)] = param['Name']
        body['%s.member.%d.Value' % (prefix, i)] = param['Value']
    body['MetricName'] = params['MetricName']
    # Convert from %Y-%m-%dT%H:%M:%SZ to %Y-%m-%d %H:%M
    if params.get('StartTime'):
        if type(params.get('StartTime')) is str:
            params['StartTime'] = dt.strptime(params['StartTime'],
                                              '%Y-%m-%dT%H:%M:%SZ')
        body['StartTime'] = params['StartTime'].strftime('%Y-%m-%d %H:%M')
    if params.get('EndTime'):
        if type(params.get('EndTime')) is str:
            params['EndTime'] = dt.strptime(params['EndTime'],
                                            '%Y-%m-%dT%H:%M:%SZ')
        body['EndTime'] = params['EndTime'].strftime('%Y-%m-%d %H:%M')
    return body


def _fix_get_delivery_log_params(
         self, params, api_version, operation_model_name):
    body = {
        "Action": operation_model_name,
        "Version": api_version
    }
    if params.get('Status'):
        body['Status'] = params['Status']
    if params.get('MaxItems'):
        body['MaxItems'] = params['MaxItems']
    if params.get('NextToken'):
        body['NextToken'] = params['NextToken']
    # Convert from %Y-%m-%dT%H:%M:%SZ to %Y-%m-%d %H:%M
    if params.get('StartDate'):
        if type(params.get('StartDate')) is str:
            params['StartDate'] = dt.strptime(params['StartDate'],
                                              '%Y-%m-%dT%H:%M:%SZ')
        body['StartDate'] = params['StartDate'].strftime('%Y-%m-%dT%H:%M')
    if params.get('EndDate'):
        if type(params.get('EndDate')) is str:
            params['EndDate'] = dt.strptime(params['EndDate'],
                                            '%Y-%m-%dT%H:%M:%SZ')
        body['EndDate'] = params['EndDate'].strftime('%Y-%m-%dT%H:%M')
    return body


class DnsSerializer(serialize.RestXMLSerializer):

    def serialize_to_request(self, parameters, operation_model):
        serialized = super(DnsSerializer, self).serialize_to_request(
            parameters, operation_model
        )
        serialized['url_path'] = operation_model.http.get('requestUri', '/')
        return serialized


serialize.SERIALIZERS.update({
    'computing': ComputingSerializer,
    'script': ScriptSerializer,
    'rdb': RdbSerializer,
    'nas': NasSerializer,
    'ess': EssSerializer,
    'dns': DnsSerializer
})
