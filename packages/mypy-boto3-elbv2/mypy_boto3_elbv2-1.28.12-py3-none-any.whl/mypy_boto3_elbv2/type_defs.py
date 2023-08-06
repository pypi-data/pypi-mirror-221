"""
Type annotations for elbv2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/type_defs/)

Usage::

    ```python
    from mypy_boto3_elbv2.type_defs import AuthenticateCognitoActionConfigOutputTypeDef

    data: AuthenticateCognitoActionConfigOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ActionTypeEnumType,
    AuthenticateCognitoActionConditionalBehaviorEnumType,
    AuthenticateOidcActionConditionalBehaviorEnumType,
    IpAddressTypeType,
    LoadBalancerSchemeEnumType,
    LoadBalancerStateEnumType,
    LoadBalancerTypeEnumType,
    ProtocolEnumType,
    RedirectActionStatusCodeEnumType,
    TargetGroupIpAddressTypeEnumType,
    TargetHealthReasonEnumType,
    TargetHealthStateEnumType,
    TargetTypeEnumType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AuthenticateCognitoActionConfigOutputTypeDef",
    "AuthenticateOidcActionConfigOutputTypeDef",
    "FixedResponseActionConfigOutputTypeDef",
    "RedirectActionConfigOutputTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "FixedResponseActionConfigTypeDef",
    "RedirectActionConfigTypeDef",
    "CertificateTypeDef",
    "CertificateOutputTypeDef",
    "TagTypeDef",
    "LoadBalancerAddressTypeDef",
    "CipherTypeDef",
    "SubnetMappingTypeDef",
    "MatcherTypeDef",
    "DeleteListenerInputRequestTypeDef",
    "DeleteLoadBalancerInputRequestTypeDef",
    "DeleteRuleInputRequestTypeDef",
    "DeleteTargetGroupInputRequestTypeDef",
    "TargetDescriptionTypeDef",
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "LimitTypeDef",
    "DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef",
    "DescribeListenerCertificatesInputRequestTypeDef",
    "DescribeListenersInputDescribeListenersPaginateTypeDef",
    "DescribeListenersInputRequestTypeDef",
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    "LoadBalancerAttributeOutputTypeDef",
    "DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef",
    "WaiterConfigTypeDef",
    "DescribeLoadBalancersInputRequestTypeDef",
    "DescribeRulesInputDescribeRulesPaginateTypeDef",
    "DescribeRulesInputRequestTypeDef",
    "DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef",
    "DescribeSSLPoliciesInputRequestTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DescribeTargetGroupAttributesInputRequestTypeDef",
    "TargetGroupAttributeOutputTypeDef",
    "DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef",
    "DescribeTargetGroupsInputRequestTypeDef",
    "TargetGroupStickinessConfigOutputTypeDef",
    "TargetGroupTupleOutputTypeDef",
    "TargetGroupStickinessConfigTypeDef",
    "TargetGroupTupleTypeDef",
    "HostHeaderConditionConfigOutputTypeDef",
    "HostHeaderConditionConfigTypeDef",
    "HttpHeaderConditionConfigOutputTypeDef",
    "HttpHeaderConditionConfigTypeDef",
    "HttpRequestMethodConditionConfigOutputTypeDef",
    "HttpRequestMethodConditionConfigTypeDef",
    "LoadBalancerAttributeTypeDef",
    "LoadBalancerStateTypeDef",
    "MatcherOutputTypeDef",
    "TargetGroupAttributeTypeDef",
    "PaginatorConfigTypeDef",
    "PathPatternConditionConfigOutputTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringKeyValuePairOutputTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SourceIpConditionConfigOutputTypeDef",
    "SourceIpConditionConfigTypeDef",
    "RulePriorityPairTypeDef",
    "SetIpAddressTypeInputRequestTypeDef",
    "SetIpAddressTypeOutputTypeDef",
    "SetSecurityGroupsInputRequestTypeDef",
    "SetSecurityGroupsOutputTypeDef",
    "TagOutputTypeDef",
    "TargetDescriptionOutputTypeDef",
    "TargetHealthTypeDef",
    "AddListenerCertificatesInputRequestTypeDef",
    "RemoveListenerCertificatesInputRequestTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "AvailabilityZoneTypeDef",
    "SslPolicyTypeDef",
    "CreateLoadBalancerInputRequestTypeDef",
    "SetSubnetsInputRequestTypeDef",
    "CreateTargetGroupInputRequestTypeDef",
    "ModifyTargetGroupInputRequestTypeDef",
    "DeregisterTargetsInputRequestTypeDef",
    "DescribeTargetHealthInputRequestTypeDef",
    "RegisterTargetsInputRequestTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef",
    "DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef",
    "DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef",
    "DescribeTargetHealthInputTargetDeregisteredWaitTypeDef",
    "DescribeTargetHealthInputTargetInServiceWaitTypeDef",
    "DescribeTargetGroupAttributesOutputTypeDef",
    "ModifyTargetGroupAttributesOutputTypeDef",
    "ForwardActionConfigOutputTypeDef",
    "ForwardActionConfigTypeDef",
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    "TargetGroupTypeDef",
    "ModifyTargetGroupAttributesInputRequestTypeDef",
    "QueryStringConditionConfigOutputTypeDef",
    "QueryStringConditionConfigTypeDef",
    "SetRulePrioritiesInputRequestTypeDef",
    "TagDescriptionTypeDef",
    "TargetHealthDescriptionTypeDef",
    "LoadBalancerTypeDef",
    "SetSubnetsOutputTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "CreateTargetGroupOutputTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "ModifyTargetGroupOutputTypeDef",
    "RuleConditionOutputTypeDef",
    "RuleConditionTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeTargetHealthOutputTypeDef",
    "CreateLoadBalancerOutputTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "ListenerTypeDef",
    "CreateListenerInputRequestTypeDef",
    "ModifyListenerInputRequestTypeDef",
    "RuleTypeDef",
    "CreateRuleInputRequestTypeDef",
    "ModifyRuleInputRequestTypeDef",
    "CreateListenerOutputTypeDef",
    "DescribeListenersOutputTypeDef",
    "ModifyListenerOutputTypeDef",
    "CreateRuleOutputTypeDef",
    "DescribeRulesOutputTypeDef",
    "ModifyRuleOutputTypeDef",
    "SetRulePrioritiesOutputTypeDef",
)

_RequiredAuthenticateCognitoActionConfigOutputTypeDef = TypedDict(
    "_RequiredAuthenticateCognitoActionConfigOutputTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
    },
)
_OptionalAuthenticateCognitoActionConfigOutputTypeDef = TypedDict(
    "_OptionalAuthenticateCognitoActionConfigOutputTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": AuthenticateCognitoActionConditionalBehaviorEnumType,
    },
    total=False,
)


class AuthenticateCognitoActionConfigOutputTypeDef(
    _RequiredAuthenticateCognitoActionConfigOutputTypeDef,
    _OptionalAuthenticateCognitoActionConfigOutputTypeDef,
):
    pass


_RequiredAuthenticateOidcActionConfigOutputTypeDef = TypedDict(
    "_RequiredAuthenticateOidcActionConfigOutputTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalAuthenticateOidcActionConfigOutputTypeDef = TypedDict(
    "_OptionalAuthenticateOidcActionConfigOutputTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": AuthenticateOidcActionConditionalBehaviorEnumType,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class AuthenticateOidcActionConfigOutputTypeDef(
    _RequiredAuthenticateOidcActionConfigOutputTypeDef,
    _OptionalAuthenticateOidcActionConfigOutputTypeDef,
):
    pass


_RequiredFixedResponseActionConfigOutputTypeDef = TypedDict(
    "_RequiredFixedResponseActionConfigOutputTypeDef",
    {
        "StatusCode": str,
    },
)
_OptionalFixedResponseActionConfigOutputTypeDef = TypedDict(
    "_OptionalFixedResponseActionConfigOutputTypeDef",
    {
        "MessageBody": str,
        "ContentType": str,
    },
    total=False,
)


class FixedResponseActionConfigOutputTypeDef(
    _RequiredFixedResponseActionConfigOutputTypeDef, _OptionalFixedResponseActionConfigOutputTypeDef
):
    pass


_RequiredRedirectActionConfigOutputTypeDef = TypedDict(
    "_RequiredRedirectActionConfigOutputTypeDef",
    {
        "StatusCode": RedirectActionStatusCodeEnumType,
    },
)
_OptionalRedirectActionConfigOutputTypeDef = TypedDict(
    "_OptionalRedirectActionConfigOutputTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
    },
    total=False,
)


class RedirectActionConfigOutputTypeDef(
    _RequiredRedirectActionConfigOutputTypeDef, _OptionalRedirectActionConfigOutputTypeDef
):
    pass


_RequiredAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateCognitoActionConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
    },
)
_OptionalAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateCognitoActionConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Mapping[str, str],
        "OnUnauthenticatedRequest": AuthenticateCognitoActionConditionalBehaviorEnumType,
    },
    total=False,
)


class AuthenticateCognitoActionConfigTypeDef(
    _RequiredAuthenticateCognitoActionConfigTypeDef, _OptionalAuthenticateCognitoActionConfigTypeDef
):
    pass


_RequiredAuthenticateOidcActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateOidcActionConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalAuthenticateOidcActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateOidcActionConfigTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Mapping[str, str],
        "OnUnauthenticatedRequest": AuthenticateOidcActionConditionalBehaviorEnumType,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class AuthenticateOidcActionConfigTypeDef(
    _RequiredAuthenticateOidcActionConfigTypeDef, _OptionalAuthenticateOidcActionConfigTypeDef
):
    pass


_RequiredFixedResponseActionConfigTypeDef = TypedDict(
    "_RequiredFixedResponseActionConfigTypeDef",
    {
        "StatusCode": str,
    },
)
_OptionalFixedResponseActionConfigTypeDef = TypedDict(
    "_OptionalFixedResponseActionConfigTypeDef",
    {
        "MessageBody": str,
        "ContentType": str,
    },
    total=False,
)


class FixedResponseActionConfigTypeDef(
    _RequiredFixedResponseActionConfigTypeDef, _OptionalFixedResponseActionConfigTypeDef
):
    pass


_RequiredRedirectActionConfigTypeDef = TypedDict(
    "_RequiredRedirectActionConfigTypeDef",
    {
        "StatusCode": RedirectActionStatusCodeEnumType,
    },
)
_OptionalRedirectActionConfigTypeDef = TypedDict(
    "_OptionalRedirectActionConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
    },
    total=False,
)


class RedirectActionConfigTypeDef(
    _RequiredRedirectActionConfigTypeDef, _OptionalRedirectActionConfigTypeDef
):
    pass


CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateArn": str,
        "IsDefault": bool,
    },
    total=False,
)

CertificateOutputTypeDef = TypedDict(
    "CertificateOutputTypeDef",
    {
        "CertificateArn": str,
        "IsDefault": bool,
    },
    total=False,
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


LoadBalancerAddressTypeDef = TypedDict(
    "LoadBalancerAddressTypeDef",
    {
        "IpAddress": str,
        "AllocationId": str,
        "PrivateIPv4Address": str,
        "IPv6Address": str,
    },
    total=False,
)

CipherTypeDef = TypedDict(
    "CipherTypeDef",
    {
        "Name": str,
        "Priority": int,
    },
    total=False,
)

SubnetMappingTypeDef = TypedDict(
    "SubnetMappingTypeDef",
    {
        "SubnetId": str,
        "AllocationId": str,
        "PrivateIPv4Address": str,
        "IPv6Address": str,
    },
    total=False,
)

MatcherTypeDef = TypedDict(
    "MatcherTypeDef",
    {
        "HttpCode": str,
        "GrpcCode": str,
    },
    total=False,
)

DeleteListenerInputRequestTypeDef = TypedDict(
    "DeleteListenerInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DeleteLoadBalancerInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)

DeleteRuleInputRequestTypeDef = TypedDict(
    "DeleteRuleInputRequestTypeDef",
    {
        "RuleArn": str,
    },
)

DeleteTargetGroupInputRequestTypeDef = TypedDict(
    "DeleteTargetGroupInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)

_RequiredTargetDescriptionTypeDef = TypedDict(
    "_RequiredTargetDescriptionTypeDef",
    {
        "Id": str,
    },
)
_OptionalTargetDescriptionTypeDef = TypedDict(
    "_OptionalTargetDescriptionTypeDef",
    {
        "Port": int,
        "AvailabilityZone": str,
    },
    total=False,
)


class TargetDescriptionTypeDef(
    _RequiredTargetDescriptionTypeDef, _OptionalTargetDescriptionTypeDef
):
    pass


DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef = TypedDict(
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeAccountLimitsInputRequestTypeDef = TypedDict(
    "DescribeAccountLimitsInputRequestTypeDef",
    {
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Name": str,
        "Max": str,
    },
    total=False,
)

_RequiredDescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef = TypedDict(
    "_RequiredDescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalDescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef = TypedDict(
    "_OptionalDescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef(
    _RequiredDescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef,
    _OptionalDescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef,
):
    pass


_RequiredDescribeListenerCertificatesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalDescribeListenerCertificatesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeListenerCertificatesInputRequestTypeDef",
    {
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)


class DescribeListenerCertificatesInputRequestTypeDef(
    _RequiredDescribeListenerCertificatesInputRequestTypeDef,
    _OptionalDescribeListenerCertificatesInputRequestTypeDef,
):
    pass


DescribeListenersInputDescribeListenersPaginateTypeDef = TypedDict(
    "DescribeListenersInputDescribeListenersPaginateTypeDef",
    {
        "LoadBalancerArn": str,
        "ListenerArns": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeListenersInputRequestTypeDef = TypedDict(
    "DescribeListenersInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "ListenerArns": Sequence[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)

LoadBalancerAttributeOutputTypeDef = TypedDict(
    "LoadBalancerAttributeOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef = TypedDict(
    "DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef",
    {
        "LoadBalancerArns": Sequence[str],
        "Names": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

DescribeLoadBalancersInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancersInputRequestTypeDef",
    {
        "LoadBalancerArns": Sequence[str],
        "Names": Sequence[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeRulesInputDescribeRulesPaginateTypeDef = TypedDict(
    "DescribeRulesInputDescribeRulesPaginateTypeDef",
    {
        "ListenerArn": str,
        "RuleArns": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeRulesInputRequestTypeDef = TypedDict(
    "DescribeRulesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "RuleArns": Sequence[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef = TypedDict(
    "DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef",
    {
        "Names": Sequence[str],
        "LoadBalancerType": LoadBalancerTypeEnumType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeSSLPoliciesInputRequestTypeDef = TypedDict(
    "DescribeSSLPoliciesInputRequestTypeDef",
    {
        "Names": Sequence[str],
        "Marker": str,
        "PageSize": int,
        "LoadBalancerType": LoadBalancerTypeEnumType,
    },
    total=False,
)

DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
    },
)

DescribeTargetGroupAttributesInputRequestTypeDef = TypedDict(
    "DescribeTargetGroupAttributesInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)

TargetGroupAttributeOutputTypeDef = TypedDict(
    "TargetGroupAttributeOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef = TypedDict(
    "DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef",
    {
        "LoadBalancerArn": str,
        "TargetGroupArns": Sequence[str],
        "Names": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeTargetGroupsInputRequestTypeDef = TypedDict(
    "DescribeTargetGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "TargetGroupArns": Sequence[str],
        "Names": Sequence[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

TargetGroupStickinessConfigOutputTypeDef = TypedDict(
    "TargetGroupStickinessConfigOutputTypeDef",
    {
        "Enabled": bool,
        "DurationSeconds": int,
    },
    total=False,
)

TargetGroupTupleOutputTypeDef = TypedDict(
    "TargetGroupTupleOutputTypeDef",
    {
        "TargetGroupArn": str,
        "Weight": int,
    },
    total=False,
)

TargetGroupStickinessConfigTypeDef = TypedDict(
    "TargetGroupStickinessConfigTypeDef",
    {
        "Enabled": bool,
        "DurationSeconds": int,
    },
    total=False,
)

TargetGroupTupleTypeDef = TypedDict(
    "TargetGroupTupleTypeDef",
    {
        "TargetGroupArn": str,
        "Weight": int,
    },
    total=False,
)

HostHeaderConditionConfigOutputTypeDef = TypedDict(
    "HostHeaderConditionConfigOutputTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

HostHeaderConditionConfigTypeDef = TypedDict(
    "HostHeaderConditionConfigTypeDef",
    {
        "Values": Sequence[str],
    },
    total=False,
)

HttpHeaderConditionConfigOutputTypeDef = TypedDict(
    "HttpHeaderConditionConfigOutputTypeDef",
    {
        "HttpHeaderName": str,
        "Values": List[str],
    },
    total=False,
)

HttpHeaderConditionConfigTypeDef = TypedDict(
    "HttpHeaderConditionConfigTypeDef",
    {
        "HttpHeaderName": str,
        "Values": Sequence[str],
    },
    total=False,
)

HttpRequestMethodConditionConfigOutputTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigOutputTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

HttpRequestMethodConditionConfigTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigTypeDef",
    {
        "Values": Sequence[str],
    },
    total=False,
)

LoadBalancerAttributeTypeDef = TypedDict(
    "LoadBalancerAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": LoadBalancerStateEnumType,
        "Reason": str,
    },
    total=False,
)

MatcherOutputTypeDef = TypedDict(
    "MatcherOutputTypeDef",
    {
        "HttpCode": str,
        "GrpcCode": str,
    },
    total=False,
)

TargetGroupAttributeTypeDef = TypedDict(
    "TargetGroupAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PathPatternConditionConfigOutputTypeDef = TypedDict(
    "PathPatternConditionConfigOutputTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

PathPatternConditionConfigTypeDef = TypedDict(
    "PathPatternConditionConfigTypeDef",
    {
        "Values": Sequence[str],
    },
    total=False,
)

QueryStringKeyValuePairOutputTypeDef = TypedDict(
    "QueryStringKeyValuePairOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

QueryStringKeyValuePairTypeDef = TypedDict(
    "QueryStringKeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
        "TagKeys": Sequence[str],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

SourceIpConditionConfigOutputTypeDef = TypedDict(
    "SourceIpConditionConfigOutputTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

SourceIpConditionConfigTypeDef = TypedDict(
    "SourceIpConditionConfigTypeDef",
    {
        "Values": Sequence[str],
    },
    total=False,
)

RulePriorityPairTypeDef = TypedDict(
    "RulePriorityPairTypeDef",
    {
        "RuleArn": str,
        "Priority": int,
    },
    total=False,
)

SetIpAddressTypeInputRequestTypeDef = TypedDict(
    "SetIpAddressTypeInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "IpAddressType": IpAddressTypeType,
    },
)

SetIpAddressTypeOutputTypeDef = TypedDict(
    "SetIpAddressTypeOutputTypeDef",
    {
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSecurityGroupsInputRequestTypeDef = TypedDict(
    "SetSecurityGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "SecurityGroups": Sequence[str],
    },
)

SetSecurityGroupsOutputTypeDef = TypedDict(
    "SetSecurityGroupsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTagOutputTypeDef = TypedDict(
    "_RequiredTagOutputTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagOutputTypeDef = TypedDict(
    "_OptionalTagOutputTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagOutputTypeDef(_RequiredTagOutputTypeDef, _OptionalTagOutputTypeDef):
    pass


_RequiredTargetDescriptionOutputTypeDef = TypedDict(
    "_RequiredTargetDescriptionOutputTypeDef",
    {
        "Id": str,
    },
)
_OptionalTargetDescriptionOutputTypeDef = TypedDict(
    "_OptionalTargetDescriptionOutputTypeDef",
    {
        "Port": int,
        "AvailabilityZone": str,
    },
    total=False,
)


class TargetDescriptionOutputTypeDef(
    _RequiredTargetDescriptionOutputTypeDef, _OptionalTargetDescriptionOutputTypeDef
):
    pass


TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": TargetHealthStateEnumType,
        "Reason": TargetHealthReasonEnumType,
        "Description": str,
    },
    total=False,
)

AddListenerCertificatesInputRequestTypeDef = TypedDict(
    "AddListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Certificates": Sequence[CertificateTypeDef],
    },
)

RemoveListenerCertificatesInputRequestTypeDef = TypedDict(
    "RemoveListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Certificates": Sequence[CertificateTypeDef],
    },
)

AddListenerCertificatesOutputTypeDef = TypedDict(
    "AddListenerCertificatesOutputTypeDef",
    {
        "Certificates": List[CertificateOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenerCertificatesOutputTypeDef = TypedDict(
    "DescribeListenerCertificatesOutputTypeDef",
    {
        "Certificates": List[CertificateOutputTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceArns": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "OutpostId": str,
        "LoadBalancerAddresses": List[LoadBalancerAddressTypeDef],
    },
    total=False,
)

SslPolicyTypeDef = TypedDict(
    "SslPolicyTypeDef",
    {
        "SslProtocols": List[str],
        "Ciphers": List[CipherTypeDef],
        "Name": str,
        "SupportedLoadBalancerTypes": List[str],
    },
    total=False,
)

_RequiredCreateLoadBalancerInputRequestTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateLoadBalancerInputRequestTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerInputRequestTypeDef",
    {
        "Subnets": Sequence[str],
        "SubnetMappings": Sequence[SubnetMappingTypeDef],
        "SecurityGroups": Sequence[str],
        "Scheme": LoadBalancerSchemeEnumType,
        "Tags": Sequence[TagTypeDef],
        "Type": LoadBalancerTypeEnumType,
        "IpAddressType": IpAddressTypeType,
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)


class CreateLoadBalancerInputRequestTypeDef(
    _RequiredCreateLoadBalancerInputRequestTypeDef, _OptionalCreateLoadBalancerInputRequestTypeDef
):
    pass


_RequiredSetSubnetsInputRequestTypeDef = TypedDict(
    "_RequiredSetSubnetsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)
_OptionalSetSubnetsInputRequestTypeDef = TypedDict(
    "_OptionalSetSubnetsInputRequestTypeDef",
    {
        "Subnets": Sequence[str],
        "SubnetMappings": Sequence[SubnetMappingTypeDef],
        "IpAddressType": IpAddressTypeType,
    },
    total=False,
)


class SetSubnetsInputRequestTypeDef(
    _RequiredSetSubnetsInputRequestTypeDef, _OptionalSetSubnetsInputRequestTypeDef
):
    pass


_RequiredCreateTargetGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateTargetGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateTargetGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateTargetGroupInputRequestTypeDef",
    {
        "Protocol": ProtocolEnumType,
        "ProtocolVersion": str,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "Matcher": MatcherTypeDef,
        "TargetType": TargetTypeEnumType,
        "Tags": Sequence[TagTypeDef],
        "IpAddressType": TargetGroupIpAddressTypeEnumType,
    },
    total=False,
)


class CreateTargetGroupInputRequestTypeDef(
    _RequiredCreateTargetGroupInputRequestTypeDef, _OptionalCreateTargetGroupInputRequestTypeDef
):
    pass


_RequiredModifyTargetGroupInputRequestTypeDef = TypedDict(
    "_RequiredModifyTargetGroupInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)
_OptionalModifyTargetGroupInputRequestTypeDef = TypedDict(
    "_OptionalModifyTargetGroupInputRequestTypeDef",
    {
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckPath": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "Matcher": MatcherTypeDef,
    },
    total=False,
)


class ModifyTargetGroupInputRequestTypeDef(
    _RequiredModifyTargetGroupInputRequestTypeDef, _OptionalModifyTargetGroupInputRequestTypeDef
):
    pass


DeregisterTargetsInputRequestTypeDef = TypedDict(
    "DeregisterTargetsInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": Sequence[TargetDescriptionTypeDef],
    },
)

_RequiredDescribeTargetHealthInputRequestTypeDef = TypedDict(
    "_RequiredDescribeTargetHealthInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)
_OptionalDescribeTargetHealthInputRequestTypeDef = TypedDict(
    "_OptionalDescribeTargetHealthInputRequestTypeDef",
    {
        "Targets": Sequence[TargetDescriptionTypeDef],
    },
    total=False,
)


class DescribeTargetHealthInputRequestTypeDef(
    _RequiredDescribeTargetHealthInputRequestTypeDef,
    _OptionalDescribeTargetHealthInputRequestTypeDef,
):
    pass


RegisterTargetsInputRequestTypeDef = TypedDict(
    "RegisterTargetsInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": Sequence[TargetDescriptionTypeDef],
    },
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "Limits": List[LimitTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List[LoadBalancerAttributeOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List[LoadBalancerAttributeOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef = TypedDict(
    "DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef",
    {
        "LoadBalancerArns": Sequence[str],
        "Names": Sequence[str],
        "Marker": str,
        "PageSize": int,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef = TypedDict(
    "DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef",
    {
        "LoadBalancerArns": Sequence[str],
        "Names": Sequence[str],
        "Marker": str,
        "PageSize": int,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef = TypedDict(
    "DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef",
    {
        "LoadBalancerArns": Sequence[str],
        "Names": Sequence[str],
        "Marker": str,
        "PageSize": int,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

_RequiredDescribeTargetHealthInputTargetDeregisteredWaitTypeDef = TypedDict(
    "_RequiredDescribeTargetHealthInputTargetDeregisteredWaitTypeDef",
    {
        "TargetGroupArn": str,
    },
)
_OptionalDescribeTargetHealthInputTargetDeregisteredWaitTypeDef = TypedDict(
    "_OptionalDescribeTargetHealthInputTargetDeregisteredWaitTypeDef",
    {
        "Targets": Sequence[TargetDescriptionTypeDef],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeTargetHealthInputTargetDeregisteredWaitTypeDef(
    _RequiredDescribeTargetHealthInputTargetDeregisteredWaitTypeDef,
    _OptionalDescribeTargetHealthInputTargetDeregisteredWaitTypeDef,
):
    pass


_RequiredDescribeTargetHealthInputTargetInServiceWaitTypeDef = TypedDict(
    "_RequiredDescribeTargetHealthInputTargetInServiceWaitTypeDef",
    {
        "TargetGroupArn": str,
    },
)
_OptionalDescribeTargetHealthInputTargetInServiceWaitTypeDef = TypedDict(
    "_OptionalDescribeTargetHealthInputTargetInServiceWaitTypeDef",
    {
        "Targets": Sequence[TargetDescriptionTypeDef],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeTargetHealthInputTargetInServiceWaitTypeDef(
    _RequiredDescribeTargetHealthInputTargetInServiceWaitTypeDef,
    _OptionalDescribeTargetHealthInputTargetInServiceWaitTypeDef,
):
    pass


DescribeTargetGroupAttributesOutputTypeDef = TypedDict(
    "DescribeTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List[TargetGroupAttributeOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTargetGroupAttributesOutputTypeDef = TypedDict(
    "ModifyTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List[TargetGroupAttributeOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ForwardActionConfigOutputTypeDef = TypedDict(
    "ForwardActionConfigOutputTypeDef",
    {
        "TargetGroups": List[TargetGroupTupleOutputTypeDef],
        "TargetGroupStickinessConfig": TargetGroupStickinessConfigOutputTypeDef,
    },
    total=False,
)

ForwardActionConfigTypeDef = TypedDict(
    "ForwardActionConfigTypeDef",
    {
        "TargetGroups": Sequence[TargetGroupTupleTypeDef],
        "TargetGroupStickinessConfig": TargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ModifyLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "Attributes": Sequence[LoadBalancerAttributeTypeDef],
    },
)

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": ProtocolEnumType,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": MatcherOutputTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": TargetTypeEnumType,
        "ProtocolVersion": str,
        "IpAddressType": TargetGroupIpAddressTypeEnumType,
    },
    total=False,
)

ModifyTargetGroupAttributesInputRequestTypeDef = TypedDict(
    "ModifyTargetGroupAttributesInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Attributes": Sequence[TargetGroupAttributeTypeDef],
    },
)

QueryStringConditionConfigOutputTypeDef = TypedDict(
    "QueryStringConditionConfigOutputTypeDef",
    {
        "Values": List[QueryStringKeyValuePairOutputTypeDef],
    },
    total=False,
)

QueryStringConditionConfigTypeDef = TypedDict(
    "QueryStringConditionConfigTypeDef",
    {
        "Values": Sequence[QueryStringKeyValuePairTypeDef],
    },
    total=False,
)

SetRulePrioritiesInputRequestTypeDef = TypedDict(
    "SetRulePrioritiesInputRequestTypeDef",
    {
        "RulePriorities": Sequence[RulePriorityPairTypeDef],
    },
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceArn": str,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

TargetHealthDescriptionTypeDef = TypedDict(
    "TargetHealthDescriptionTypeDef",
    {
        "Target": TargetDescriptionOutputTypeDef,
        "HealthCheckPort": str,
        "TargetHealth": TargetHealthTypeDef,
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": LoadBalancerSchemeEnumType,
        "VpcId": str,
        "State": LoadBalancerStateTypeDef,
        "Type": LoadBalancerTypeEnumType,
        "AvailabilityZones": List[AvailabilityZoneTypeDef],
        "SecurityGroups": List[str],
        "IpAddressType": IpAddressTypeType,
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)

SetSubnetsOutputTypeDef = TypedDict(
    "SetSubnetsOutputTypeDef",
    {
        "AvailabilityZones": List[AvailabilityZoneTypeDef],
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSSLPoliciesOutputTypeDef = TypedDict(
    "DescribeSSLPoliciesOutputTypeDef",
    {
        "SslPolicies": List[SslPolicyTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredActionOutputTypeDef = TypedDict(
    "_RequiredActionOutputTypeDef",
    {
        "Type": ActionTypeEnumType,
    },
)
_OptionalActionOutputTypeDef = TypedDict(
    "_OptionalActionOutputTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": AuthenticateOidcActionConfigOutputTypeDef,
        "AuthenticateCognitoConfig": AuthenticateCognitoActionConfigOutputTypeDef,
        "Order": int,
        "RedirectConfig": RedirectActionConfigOutputTypeDef,
        "FixedResponseConfig": FixedResponseActionConfigOutputTypeDef,
        "ForwardConfig": ForwardActionConfigOutputTypeDef,
    },
    total=False,
)


class ActionOutputTypeDef(_RequiredActionOutputTypeDef, _OptionalActionOutputTypeDef):
    pass


_RequiredActionTypeDef = TypedDict(
    "_RequiredActionTypeDef",
    {
        "Type": ActionTypeEnumType,
    },
)
_OptionalActionTypeDef = TypedDict(
    "_OptionalActionTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": AuthenticateOidcActionConfigTypeDef,
        "AuthenticateCognitoConfig": AuthenticateCognitoActionConfigTypeDef,
        "Order": int,
        "RedirectConfig": RedirectActionConfigTypeDef,
        "FixedResponseConfig": FixedResponseActionConfigTypeDef,
        "ForwardConfig": ForwardActionConfigTypeDef,
    },
    total=False,
)


class ActionTypeDef(_RequiredActionTypeDef, _OptionalActionTypeDef):
    pass


CreateTargetGroupOutputTypeDef = TypedDict(
    "CreateTargetGroupOutputTypeDef",
    {
        "TargetGroups": List[TargetGroupTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetGroupsOutputTypeDef = TypedDict(
    "DescribeTargetGroupsOutputTypeDef",
    {
        "TargetGroups": List[TargetGroupTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTargetGroupOutputTypeDef = TypedDict(
    "ModifyTargetGroupOutputTypeDef",
    {
        "TargetGroups": List[TargetGroupTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RuleConditionOutputTypeDef = TypedDict(
    "RuleConditionOutputTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": HostHeaderConditionConfigOutputTypeDef,
        "PathPatternConfig": PathPatternConditionConfigOutputTypeDef,
        "HttpHeaderConfig": HttpHeaderConditionConfigOutputTypeDef,
        "QueryStringConfig": QueryStringConditionConfigOutputTypeDef,
        "HttpRequestMethodConfig": HttpRequestMethodConditionConfigOutputTypeDef,
        "SourceIpConfig": SourceIpConditionConfigOutputTypeDef,
    },
    total=False,
)

RuleConditionTypeDef = TypedDict(
    "RuleConditionTypeDef",
    {
        "Field": str,
        "Values": Sequence[str],
        "HostHeaderConfig": HostHeaderConditionConfigTypeDef,
        "PathPatternConfig": PathPatternConditionConfigTypeDef,
        "HttpHeaderConfig": HttpHeaderConditionConfigTypeDef,
        "QueryStringConfig": QueryStringConditionConfigTypeDef,
        "HttpRequestMethodConfig": HttpRequestMethodConditionConfigTypeDef,
        "SourceIpConfig": SourceIpConditionConfigTypeDef,
    },
    total=False,
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "TagDescriptions": List[TagDescriptionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetHealthOutputTypeDef = TypedDict(
    "DescribeTargetHealthOutputTypeDef",
    {
        "TargetHealthDescriptions": List[TargetHealthDescriptionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoadBalancerOutputTypeDef = TypedDict(
    "CreateLoadBalancerOutputTypeDef",
    {
        "LoadBalancers": List[LoadBalancerTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancersOutputTypeDef = TypedDict(
    "DescribeLoadBalancersOutputTypeDef",
    {
        "LoadBalancers": List[LoadBalancerTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": ProtocolEnumType,
        "Certificates": List[CertificateOutputTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[ActionOutputTypeDef],
        "AlpnPolicy": List[str],
    },
    total=False,
)

_RequiredCreateListenerInputRequestTypeDef = TypedDict(
    "_RequiredCreateListenerInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "DefaultActions": Sequence[ActionTypeDef],
    },
)
_OptionalCreateListenerInputRequestTypeDef = TypedDict(
    "_OptionalCreateListenerInputRequestTypeDef",
    {
        "Protocol": ProtocolEnumType,
        "Port": int,
        "SslPolicy": str,
        "Certificates": Sequence[CertificateTypeDef],
        "AlpnPolicy": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateListenerInputRequestTypeDef(
    _RequiredCreateListenerInputRequestTypeDef, _OptionalCreateListenerInputRequestTypeDef
):
    pass


_RequiredModifyListenerInputRequestTypeDef = TypedDict(
    "_RequiredModifyListenerInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalModifyListenerInputRequestTypeDef = TypedDict(
    "_OptionalModifyListenerInputRequestTypeDef",
    {
        "Port": int,
        "Protocol": ProtocolEnumType,
        "SslPolicy": str,
        "Certificates": Sequence[CertificateTypeDef],
        "DefaultActions": Sequence[ActionTypeDef],
        "AlpnPolicy": Sequence[str],
    },
    total=False,
)


class ModifyListenerInputRequestTypeDef(
    _RequiredModifyListenerInputRequestTypeDef, _OptionalModifyListenerInputRequestTypeDef
):
    pass


RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[RuleConditionOutputTypeDef],
        "Actions": List[ActionOutputTypeDef],
        "IsDefault": bool,
    },
    total=False,
)

_RequiredCreateRuleInputRequestTypeDef = TypedDict(
    "_RequiredCreateRuleInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Conditions": Sequence[RuleConditionTypeDef],
        "Priority": int,
        "Actions": Sequence[ActionTypeDef],
    },
)
_OptionalCreateRuleInputRequestTypeDef = TypedDict(
    "_OptionalCreateRuleInputRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateRuleInputRequestTypeDef(
    _RequiredCreateRuleInputRequestTypeDef, _OptionalCreateRuleInputRequestTypeDef
):
    pass


_RequiredModifyRuleInputRequestTypeDef = TypedDict(
    "_RequiredModifyRuleInputRequestTypeDef",
    {
        "RuleArn": str,
    },
)
_OptionalModifyRuleInputRequestTypeDef = TypedDict(
    "_OptionalModifyRuleInputRequestTypeDef",
    {
        "Conditions": Sequence[RuleConditionTypeDef],
        "Actions": Sequence[ActionTypeDef],
    },
    total=False,
)


class ModifyRuleInputRequestTypeDef(
    _RequiredModifyRuleInputRequestTypeDef, _OptionalModifyRuleInputRequestTypeDef
):
    pass


CreateListenerOutputTypeDef = TypedDict(
    "CreateListenerOutputTypeDef",
    {
        "Listeners": List[ListenerTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenersOutputTypeDef = TypedDict(
    "DescribeListenersOutputTypeDef",
    {
        "Listeners": List[ListenerTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyListenerOutputTypeDef = TypedDict(
    "ModifyListenerOutputTypeDef",
    {
        "Listeners": List[ListenerTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleOutputTypeDef = TypedDict(
    "CreateRuleOutputTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRulesOutputTypeDef = TypedDict(
    "DescribeRulesOutputTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyRuleOutputTypeDef = TypedDict(
    "ModifyRuleOutputTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetRulePrioritiesOutputTypeDef = TypedDict(
    "SetRulePrioritiesOutputTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
