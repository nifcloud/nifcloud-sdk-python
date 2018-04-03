from botocore import auth


class SigV2ComputingAuth(auth.SigV2Auth):
    def calc_signature(self, request, params):
        if 'AWSAccessKeyId' in params:
            params['AccessKeyId'] = params['AWSAccessKeyId']
            del params['AWSAccessKeyId']
        return super(SigV2ComputingAuth, self).calc_signature(request, params)


auth.AUTH_TYPE_MAPS.update({
    'v2-computing': SigV2ComputingAuth
})
