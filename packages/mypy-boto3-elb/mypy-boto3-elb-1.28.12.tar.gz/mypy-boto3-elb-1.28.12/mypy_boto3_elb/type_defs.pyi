"""
Type annotations for elb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/type_defs/)

Usage::

    ```python
    from mypy_boto3_elb.type_defs import AccessLogOutputTypeDef

    data: AccessLogOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessLogOutputTypeDef",
    "AccessLogTypeDef",
    "AddAvailabilityZonesInputRequestTypeDef",
    "AddAvailabilityZonesOutputTypeDef",
    "TagTypeDef",
    "AdditionalAttributeOutputTypeDef",
    "AdditionalAttributeTypeDef",
    "AppCookieStickinessPolicyTypeDef",
    "ApplySecurityGroupsToLoadBalancerInputRequestTypeDef",
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    "AttachLoadBalancerToSubnetsInputRequestTypeDef",
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    "BackendServerDescriptionTypeDef",
    "HealthCheckTypeDef",
    "HealthCheckOutputTypeDef",
    "ConnectionDrainingOutputTypeDef",
    "ConnectionDrainingTypeDef",
    "ConnectionSettingsOutputTypeDef",
    "ConnectionSettingsTypeDef",
    "ListenerTypeDef",
    "CreateAccessPointOutputTypeDef",
    "CreateAppCookieStickinessPolicyInputRequestTypeDef",
    "CreateLBCookieStickinessPolicyInputRequestTypeDef",
    "PolicyAttributeTypeDef",
    "CrossZoneLoadBalancingOutputTypeDef",
    "CrossZoneLoadBalancingTypeDef",
    "DeleteAccessPointInputRequestTypeDef",
    "DeleteLoadBalancerListenerInputRequestTypeDef",
    "DeleteLoadBalancerPolicyInputRequestTypeDef",
    "InstanceTypeDef",
    "InstanceOutputTypeDef",
    "DescribeAccessPointsInputDescribeLoadBalancersPaginateTypeDef",
    "DescribeAccessPointsInputRequestTypeDef",
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "LimitTypeDef",
    "WaiterConfigTypeDef",
    "InstanceStateTypeDef",
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    "DescribeLoadBalancerPoliciesInputRequestTypeDef",
    "DescribeLoadBalancerPolicyTypesInputRequestTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DetachLoadBalancerFromSubnetsInputRequestTypeDef",
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    "LBCookieStickinessPolicyTypeDef",
    "ListenerOutputTypeDef",
    "SourceSecurityGroupTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyAttributeDescriptionTypeDef",
    "PolicyAttributeTypeDescriptionTypeDef",
    "RemoveAvailabilityZonesInputRequestTypeDef",
    "RemoveAvailabilityZonesOutputTypeDef",
    "TagKeyOnlyTypeDef",
    "ResponseMetadataTypeDef",
    "SetLoadBalancerListenerSSLCertificateInputRequestTypeDef",
    "SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef",
    "SetLoadBalancerPoliciesOfListenerInputRequestTypeDef",
    "TagOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "ConfigureHealthCheckInputRequestTypeDef",
    "ConfigureHealthCheckOutputTypeDef",
    "CreateAccessPointInputRequestTypeDef",
    "CreateLoadBalancerListenerInputRequestTypeDef",
    "CreateLoadBalancerPolicyInputRequestTypeDef",
    "LoadBalancerAttributesOutputTypeDef",
    "LoadBalancerAttributesTypeDef",
    "DeregisterEndPointsInputRequestTypeDef",
    "DescribeEndPointStateInputRequestTypeDef",
    "RegisterEndPointsInputRequestTypeDef",
    "DeregisterEndPointsOutputTypeDef",
    "RegisterEndPointsOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef",
    "DescribeEndPointStateInputInstanceDeregisteredWaitTypeDef",
    "DescribeEndPointStateInputInstanceInServiceWaitTypeDef",
    "DescribeEndPointStateOutputTypeDef",
    "PoliciesTypeDef",
    "ListenerDescriptionTypeDef",
    "PolicyDescriptionTypeDef",
    "PolicyTypeDescriptionTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "TagDescriptionTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeAccessPointsOutputTypeDef",
)

_RequiredAccessLogOutputTypeDef = TypedDict(
    "_RequiredAccessLogOutputTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalAccessLogOutputTypeDef = TypedDict(
    "_OptionalAccessLogOutputTypeDef",
    {
        "S3BucketName": str,
        "EmitInterval": int,
        "S3BucketPrefix": str,
    },
    total=False,
)

class AccessLogOutputTypeDef(_RequiredAccessLogOutputTypeDef, _OptionalAccessLogOutputTypeDef):
    pass

_RequiredAccessLogTypeDef = TypedDict(
    "_RequiredAccessLogTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalAccessLogTypeDef = TypedDict(
    "_OptionalAccessLogTypeDef",
    {
        "S3BucketName": str,
        "EmitInterval": int,
        "S3BucketPrefix": str,
    },
    total=False,
)

class AccessLogTypeDef(_RequiredAccessLogTypeDef, _OptionalAccessLogTypeDef):
    pass

AddAvailabilityZonesInputRequestTypeDef = TypedDict(
    "AddAvailabilityZonesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "AvailabilityZones": Sequence[str],
    },
)

AddAvailabilityZonesOutputTypeDef = TypedDict(
    "AddAvailabilityZonesOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

AdditionalAttributeOutputTypeDef = TypedDict(
    "AdditionalAttributeOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

AdditionalAttributeTypeDef = TypedDict(
    "AdditionalAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

AppCookieStickinessPolicyTypeDef = TypedDict(
    "AppCookieStickinessPolicyTypeDef",
    {
        "PolicyName": str,
        "CookieName": str,
    },
    total=False,
)

ApplySecurityGroupsToLoadBalancerInputRequestTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "SecurityGroups": Sequence[str],
    },
)

ApplySecurityGroupsToLoadBalancerOutputTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachLoadBalancerToSubnetsInputRequestTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Subnets": Sequence[str],
    },
)

AttachLoadBalancerToSubnetsOutputTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    {
        "Subnets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackendServerDescriptionTypeDef = TypedDict(
    "BackendServerDescriptionTypeDef",
    {
        "InstancePort": int,
        "PolicyNames": List[str],
    },
    total=False,
)

HealthCheckTypeDef = TypedDict(
    "HealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
)

HealthCheckOutputTypeDef = TypedDict(
    "HealthCheckOutputTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
)

_RequiredConnectionDrainingOutputTypeDef = TypedDict(
    "_RequiredConnectionDrainingOutputTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalConnectionDrainingOutputTypeDef = TypedDict(
    "_OptionalConnectionDrainingOutputTypeDef",
    {
        "Timeout": int,
    },
    total=False,
)

class ConnectionDrainingOutputTypeDef(
    _RequiredConnectionDrainingOutputTypeDef, _OptionalConnectionDrainingOutputTypeDef
):
    pass

_RequiredConnectionDrainingTypeDef = TypedDict(
    "_RequiredConnectionDrainingTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalConnectionDrainingTypeDef = TypedDict(
    "_OptionalConnectionDrainingTypeDef",
    {
        "Timeout": int,
    },
    total=False,
)

class ConnectionDrainingTypeDef(
    _RequiredConnectionDrainingTypeDef, _OptionalConnectionDrainingTypeDef
):
    pass

ConnectionSettingsOutputTypeDef = TypedDict(
    "ConnectionSettingsOutputTypeDef",
    {
        "IdleTimeout": int,
    },
)

ConnectionSettingsTypeDef = TypedDict(
    "ConnectionSettingsTypeDef",
    {
        "IdleTimeout": int,
    },
)

_RequiredListenerTypeDef = TypedDict(
    "_RequiredListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstancePort": int,
    },
)
_OptionalListenerTypeDef = TypedDict(
    "_OptionalListenerTypeDef",
    {
        "InstanceProtocol": str,
        "SSLCertificateId": str,
    },
    total=False,
)

class ListenerTypeDef(_RequiredListenerTypeDef, _OptionalListenerTypeDef):
    pass

CreateAccessPointOutputTypeDef = TypedDict(
    "CreateAccessPointOutputTypeDef",
    {
        "DNSName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppCookieStickinessPolicyInputRequestTypeDef = TypedDict(
    "CreateAppCookieStickinessPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "CookieName": str,
    },
)

_RequiredCreateLBCookieStickinessPolicyInputRequestTypeDef = TypedDict(
    "_RequiredCreateLBCookieStickinessPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
    },
)
_OptionalCreateLBCookieStickinessPolicyInputRequestTypeDef = TypedDict(
    "_OptionalCreateLBCookieStickinessPolicyInputRequestTypeDef",
    {
        "CookieExpirationPeriod": int,
    },
    total=False,
)

class CreateLBCookieStickinessPolicyInputRequestTypeDef(
    _RequiredCreateLBCookieStickinessPolicyInputRequestTypeDef,
    _OptionalCreateLBCookieStickinessPolicyInputRequestTypeDef,
):
    pass

PolicyAttributeTypeDef = TypedDict(
    "PolicyAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
    },
    total=False,
)

CrossZoneLoadBalancingOutputTypeDef = TypedDict(
    "CrossZoneLoadBalancingOutputTypeDef",
    {
        "Enabled": bool,
    },
)

CrossZoneLoadBalancingTypeDef = TypedDict(
    "CrossZoneLoadBalancingTypeDef",
    {
        "Enabled": bool,
    },
)

DeleteAccessPointInputRequestTypeDef = TypedDict(
    "DeleteAccessPointInputRequestTypeDef",
    {
        "LoadBalancerName": str,
    },
)

DeleteLoadBalancerListenerInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPorts": Sequence[int],
    },
)

DeleteLoadBalancerPolicyInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

InstanceOutputTypeDef = TypedDict(
    "InstanceOutputTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

DescribeAccessPointsInputDescribeLoadBalancersPaginateTypeDef = TypedDict(
    "DescribeAccessPointsInputDescribeLoadBalancersPaginateTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeAccessPointsInputRequestTypeDef = TypedDict(
    "DescribeAccessPointsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

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

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "InstanceId": str,
        "State": str,
        "ReasonCode": str,
        "Description": str,
    },
    total=False,
)

DescribeLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
    },
)

DescribeLoadBalancerPoliciesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyNames": Sequence[str],
    },
    total=False,
)

DescribeLoadBalancerPolicyTypesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesInputRequestTypeDef",
    {
        "PolicyTypeNames": Sequence[str],
    },
    total=False,
)

DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
    },
)

DetachLoadBalancerFromSubnetsInputRequestTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Subnets": Sequence[str],
    },
)

DetachLoadBalancerFromSubnetsOutputTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    {
        "Subnets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LBCookieStickinessPolicyTypeDef = TypedDict(
    "LBCookieStickinessPolicyTypeDef",
    {
        "PolicyName": str,
        "CookieExpirationPeriod": int,
    },
    total=False,
)

_RequiredListenerOutputTypeDef = TypedDict(
    "_RequiredListenerOutputTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstancePort": int,
    },
)
_OptionalListenerOutputTypeDef = TypedDict(
    "_OptionalListenerOutputTypeDef",
    {
        "InstanceProtocol": str,
        "SSLCertificateId": str,
    },
    total=False,
)

class ListenerOutputTypeDef(_RequiredListenerOutputTypeDef, _OptionalListenerOutputTypeDef):
    pass

SourceSecurityGroupTypeDef = TypedDict(
    "SourceSecurityGroupTypeDef",
    {
        "OwnerAlias": str,
        "GroupName": str,
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

PolicyAttributeDescriptionTypeDef = TypedDict(
    "PolicyAttributeDescriptionTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
    },
    total=False,
)

PolicyAttributeTypeDescriptionTypeDef = TypedDict(
    "PolicyAttributeTypeDescriptionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": str,
        "Description": str,
        "DefaultValue": str,
        "Cardinality": str,
    },
    total=False,
)

RemoveAvailabilityZonesInputRequestTypeDef = TypedDict(
    "RemoveAvailabilityZonesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "AvailabilityZones": Sequence[str],
    },
)

RemoveAvailabilityZonesOutputTypeDef = TypedDict(
    "RemoveAvailabilityZonesOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagKeyOnlyTypeDef = TypedDict(
    "TagKeyOnlyTypeDef",
    {
        "Key": str,
    },
    total=False,
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

SetLoadBalancerListenerSSLCertificateInputRequestTypeDef = TypedDict(
    "SetLoadBalancerListenerSSLCertificateInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPort": int,
        "SSLCertificateId": str,
    },
)

SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef = TypedDict(
    "SetLoadBalancerPoliciesForBackendServerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "InstancePort": int,
        "PolicyNames": Sequence[str],
    },
)

SetLoadBalancerPoliciesOfListenerInputRequestTypeDef = TypedDict(
    "SetLoadBalancerPoliciesOfListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPort": int,
        "PolicyNames": Sequence[str],
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

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)

ConfigureHealthCheckInputRequestTypeDef = TypedDict(
    "ConfigureHealthCheckInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "HealthCheck": HealthCheckTypeDef,
    },
)

ConfigureHealthCheckOutputTypeDef = TypedDict(
    "ConfigureHealthCheckOutputTypeDef",
    {
        "HealthCheck": HealthCheckOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAccessPointInputRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPointInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Listeners": Sequence[ListenerTypeDef],
    },
)
_OptionalCreateAccessPointInputRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPointInputRequestTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "Subnets": Sequence[str],
        "SecurityGroups": Sequence[str],
        "Scheme": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateAccessPointInputRequestTypeDef(
    _RequiredCreateAccessPointInputRequestTypeDef, _OptionalCreateAccessPointInputRequestTypeDef
):
    pass

CreateLoadBalancerListenerInputRequestTypeDef = TypedDict(
    "CreateLoadBalancerListenerInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Listeners": Sequence[ListenerTypeDef],
    },
)

_RequiredCreateLoadBalancerPolicyInputRequestTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerPolicyInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "PolicyTypeName": str,
    },
)
_OptionalCreateLoadBalancerPolicyInputRequestTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerPolicyInputRequestTypeDef",
    {
        "PolicyAttributes": Sequence[PolicyAttributeTypeDef],
    },
    total=False,
)

class CreateLoadBalancerPolicyInputRequestTypeDef(
    _RequiredCreateLoadBalancerPolicyInputRequestTypeDef,
    _OptionalCreateLoadBalancerPolicyInputRequestTypeDef,
):
    pass

LoadBalancerAttributesOutputTypeDef = TypedDict(
    "LoadBalancerAttributesOutputTypeDef",
    {
        "CrossZoneLoadBalancing": CrossZoneLoadBalancingOutputTypeDef,
        "AccessLog": AccessLogOutputTypeDef,
        "ConnectionDraining": ConnectionDrainingOutputTypeDef,
        "ConnectionSettings": ConnectionSettingsOutputTypeDef,
        "AdditionalAttributes": List[AdditionalAttributeOutputTypeDef],
    },
    total=False,
)

LoadBalancerAttributesTypeDef = TypedDict(
    "LoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": CrossZoneLoadBalancingTypeDef,
        "AccessLog": AccessLogTypeDef,
        "ConnectionDraining": ConnectionDrainingTypeDef,
        "ConnectionSettings": ConnectionSettingsTypeDef,
        "AdditionalAttributes": Sequence[AdditionalAttributeTypeDef],
    },
    total=False,
)

DeregisterEndPointsInputRequestTypeDef = TypedDict(
    "DeregisterEndPointsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": Sequence[InstanceTypeDef],
    },
)

_RequiredDescribeEndPointStateInputRequestTypeDef = TypedDict(
    "_RequiredDescribeEndPointStateInputRequestTypeDef",
    {
        "LoadBalancerName": str,
    },
)
_OptionalDescribeEndPointStateInputRequestTypeDef = TypedDict(
    "_OptionalDescribeEndPointStateInputRequestTypeDef",
    {
        "Instances": Sequence[InstanceTypeDef],
    },
    total=False,
)

class DescribeEndPointStateInputRequestTypeDef(
    _RequiredDescribeEndPointStateInputRequestTypeDef,
    _OptionalDescribeEndPointStateInputRequestTypeDef,
):
    pass

RegisterEndPointsInputRequestTypeDef = TypedDict(
    "RegisterEndPointsInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": Sequence[InstanceTypeDef],
    },
)

DeregisterEndPointsOutputTypeDef = TypedDict(
    "DeregisterEndPointsOutputTypeDef",
    {
        "Instances": List[InstanceOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterEndPointsOutputTypeDef = TypedDict(
    "RegisterEndPointsOutputTypeDef",
    {
        "Instances": List[InstanceOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredDescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef = TypedDict(
    "_RequiredDescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef",
    {
        "LoadBalancerName": str,
    },
)
_OptionalDescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef = TypedDict(
    "_OptionalDescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef",
    {
        "Instances": Sequence[InstanceTypeDef],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef(
    _RequiredDescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef,
    _OptionalDescribeEndPointStateInputAnyInstanceInServiceWaitTypeDef,
):
    pass

_RequiredDescribeEndPointStateInputInstanceDeregisteredWaitTypeDef = TypedDict(
    "_RequiredDescribeEndPointStateInputInstanceDeregisteredWaitTypeDef",
    {
        "LoadBalancerName": str,
    },
)
_OptionalDescribeEndPointStateInputInstanceDeregisteredWaitTypeDef = TypedDict(
    "_OptionalDescribeEndPointStateInputInstanceDeregisteredWaitTypeDef",
    {
        "Instances": Sequence[InstanceTypeDef],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeEndPointStateInputInstanceDeregisteredWaitTypeDef(
    _RequiredDescribeEndPointStateInputInstanceDeregisteredWaitTypeDef,
    _OptionalDescribeEndPointStateInputInstanceDeregisteredWaitTypeDef,
):
    pass

_RequiredDescribeEndPointStateInputInstanceInServiceWaitTypeDef = TypedDict(
    "_RequiredDescribeEndPointStateInputInstanceInServiceWaitTypeDef",
    {
        "LoadBalancerName": str,
    },
)
_OptionalDescribeEndPointStateInputInstanceInServiceWaitTypeDef = TypedDict(
    "_OptionalDescribeEndPointStateInputInstanceInServiceWaitTypeDef",
    {
        "Instances": Sequence[InstanceTypeDef],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeEndPointStateInputInstanceInServiceWaitTypeDef(
    _RequiredDescribeEndPointStateInputInstanceInServiceWaitTypeDef,
    _OptionalDescribeEndPointStateInputInstanceInServiceWaitTypeDef,
):
    pass

DescribeEndPointStateOutputTypeDef = TypedDict(
    "DescribeEndPointStateOutputTypeDef",
    {
        "InstanceStates": List[InstanceStateTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PoliciesTypeDef = TypedDict(
    "PoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List[AppCookieStickinessPolicyTypeDef],
        "LBCookieStickinessPolicies": List[LBCookieStickinessPolicyTypeDef],
        "OtherPolicies": List[str],
    },
    total=False,
)

ListenerDescriptionTypeDef = TypedDict(
    "ListenerDescriptionTypeDef",
    {
        "Listener": ListenerOutputTypeDef,
        "PolicyNames": List[str],
    },
    total=False,
)

PolicyDescriptionTypeDef = TypedDict(
    "PolicyDescriptionTypeDef",
    {
        "PolicyName": str,
        "PolicyTypeName": str,
        "PolicyAttributeDescriptions": List[PolicyAttributeDescriptionTypeDef],
    },
    total=False,
)

PolicyTypeDescriptionTypeDef = TypedDict(
    "PolicyTypeDescriptionTypeDef",
    {
        "PolicyTypeName": str,
        "Description": str,
        "PolicyAttributeTypeDescriptions": List[PolicyAttributeTypeDescriptionTypeDef],
    },
    total=False,
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "LoadBalancerNames": Sequence[str],
        "Tags": Sequence[TagKeyOnlyTypeDef],
    },
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "LoadBalancerName": str,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "LoadBalancerAttributes": LoadBalancerAttributesOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": LoadBalancerAttributesOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": LoadBalancerAttributesTypeDef,
    },
)

LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {
        "LoadBalancerName": str,
        "DNSName": str,
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "ListenerDescriptions": List[ListenerDescriptionTypeDef],
        "Policies": PoliciesTypeDef,
        "BackendServerDescriptions": List[BackendServerDescriptionTypeDef],
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "VPCId": str,
        "Instances": List[InstanceOutputTypeDef],
        "HealthCheck": HealthCheckOutputTypeDef,
        "SourceSecurityGroup": SourceSecurityGroupTypeDef,
        "SecurityGroups": List[str],
        "CreatedTime": datetime,
        "Scheme": str,
    },
    total=False,
)

DescribeLoadBalancerPoliciesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    {
        "PolicyDescriptions": List[PolicyDescriptionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerPolicyTypesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    {
        "PolicyTypeDescriptions": List[PolicyTypeDescriptionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "TagDescriptions": List[TagDescriptionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccessPointsOutputTypeDef = TypedDict(
    "DescribeAccessPointsOutputTypeDef",
    {
        "LoadBalancerDescriptions": List[LoadBalancerDescriptionTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
