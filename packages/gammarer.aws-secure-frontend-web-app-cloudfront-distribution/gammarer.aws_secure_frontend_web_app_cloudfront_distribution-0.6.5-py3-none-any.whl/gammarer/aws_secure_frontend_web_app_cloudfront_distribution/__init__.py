'''
# AWS Secure Frontend Web App CloudFront Distribution (for AWS CDK v2)

AWS CloudFront distribution for frontend web app (spa) optimized.

## Install

### TypeScript

```shell
npm install @gammarer/aws-secure-frontend-web-app-cloudfront-distribution
# or
yarn add @gammarer/aws-secure-frontend-web-app-cloudfront-distribution
```

### Python

```shell
pip install gammarer.aws-secure-frontend-web-app-cloudfront-distribution
```

## Example

```shell
npm install @gammarer/aws-secure-frontend-web-app-cloudfront-distribution
```

```python
import { SecureFrontendWebAppCloudFrontDistribution } from '@gammarer/aws-secure-frontend-web-app-cloudfront-distribution';

new SecureFrontendWebAppCloudFrontDistribution(stack, 'SecureFrontendWebAppCloudFrontDistribution', {
  accessLogBucket: new s3.Bucket(stack, 'LogBucket'),
  certificate: new acm.Certificate(stack, 'Certificate', {
    domainName: 'example.com',
  }),
  distributionDomainName: 'example.com',
  originAccessIdentity: new cloudfront.OriginAccessIdentity(stack, 'OriginAccessIdentity'),
  originBucket: new s3.Bucket(stack, 'OriginBucket'),
});
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_certificatemanager as _aws_cdk_aws_certificatemanager_ceddda9d
import aws_cdk.aws_cloudfront as _aws_cdk_aws_cloudfront_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


class SecureFrontendWebAppCloudFrontDistribution(
    _aws_cdk_aws_cloudfront_ceddda9d.Distribution,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gammarer/aws-secure-frontend-web-app-cloudfront-distribution.SecureFrontendWebAppCloudFrontDistribution",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_log_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        certificate: _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate,
        domain_name: builtins.str,
        origin_access_identity: _aws_cdk_aws_cloudfront_ceddda9d.IOriginAccessIdentity,
        origin_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        comment: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_log_bucket: 
        :param certificate: 
        :param domain_name: 
        :param origin_access_identity: 
        :param origin_bucket: 
        :param comment: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab68d83b630cc02546d77e48c8646f50b0e2f872bcc124abfd93eb26fa3bfc75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SecureFrontendWebAppCloudFrontDistributionProps(
            access_log_bucket=access_log_bucket,
            certificate=certificate,
            domain_name=domain_name,
            origin_access_identity=origin_access_identity,
            origin_bucket=origin_bucket,
            comment=comment,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@gammarer/aws-secure-frontend-web-app-cloudfront-distribution.SecureFrontendWebAppCloudFrontDistributionProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_log_bucket": "accessLogBucket",
        "certificate": "certificate",
        "domain_name": "domainName",
        "origin_access_identity": "originAccessIdentity",
        "origin_bucket": "originBucket",
        "comment": "comment",
    },
)
class SecureFrontendWebAppCloudFrontDistributionProps:
    def __init__(
        self,
        *,
        access_log_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        certificate: _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate,
        domain_name: builtins.str,
        origin_access_identity: _aws_cdk_aws_cloudfront_ceddda9d.IOriginAccessIdentity,
        origin_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        comment: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_log_bucket: 
        :param certificate: 
        :param domain_name: 
        :param origin_access_identity: 
        :param origin_bucket: 
        :param comment: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46fcd4037c1afe9dd0632bd9133c92d55839ac1c45b0d25a564b359716dceb26)
            check_type(argname="argument access_log_bucket", value=access_log_bucket, expected_type=type_hints["access_log_bucket"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument origin_access_identity", value=origin_access_identity, expected_type=type_hints["origin_access_identity"])
            check_type(argname="argument origin_bucket", value=origin_bucket, expected_type=type_hints["origin_bucket"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_log_bucket": access_log_bucket,
            "certificate": certificate,
            "domain_name": domain_name,
            "origin_access_identity": origin_access_identity,
            "origin_bucket": origin_bucket,
        }
        if comment is not None:
            self._values["comment"] = comment

    @builtins.property
    def access_log_bucket(self) -> _aws_cdk_aws_s3_ceddda9d.IBucket:
        result = self._values.get("access_log_bucket")
        assert result is not None, "Required property 'access_log_bucket' is missing"
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.IBucket, result)

    @builtins.property
    def certificate(self) -> _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate:
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_access_identity(
        self,
    ) -> _aws_cdk_aws_cloudfront_ceddda9d.IOriginAccessIdentity:
        result = self._values.get("origin_access_identity")
        assert result is not None, "Required property 'origin_access_identity' is missing"
        return typing.cast(_aws_cdk_aws_cloudfront_ceddda9d.IOriginAccessIdentity, result)

    @builtins.property
    def origin_bucket(self) -> _aws_cdk_aws_s3_ceddda9d.IBucket:
        result = self._values.get("origin_bucket")
        assert result is not None, "Required property 'origin_bucket' is missing"
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.IBucket, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecureFrontendWebAppCloudFrontDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SecureFrontendWebAppCloudFrontDistribution",
    "SecureFrontendWebAppCloudFrontDistributionProps",
]

publication.publish()

def _typecheckingstub__ab68d83b630cc02546d77e48c8646f50b0e2f872bcc124abfd93eb26fa3bfc75(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_log_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    certificate: _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate,
    domain_name: builtins.str,
    origin_access_identity: _aws_cdk_aws_cloudfront_ceddda9d.IOriginAccessIdentity,
    origin_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    comment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46fcd4037c1afe9dd0632bd9133c92d55839ac1c45b0d25a564b359716dceb26(
    *,
    access_log_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    certificate: _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate,
    domain_name: builtins.str,
    origin_access_identity: _aws_cdk_aws_cloudfront_ceddda9d.IOriginAccessIdentity,
    origin_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    comment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
