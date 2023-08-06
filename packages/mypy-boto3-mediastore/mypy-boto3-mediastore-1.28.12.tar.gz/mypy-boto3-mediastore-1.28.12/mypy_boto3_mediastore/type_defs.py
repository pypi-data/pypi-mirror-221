"""
Type annotations for mediastore service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediastore.type_defs import ContainerTypeDef

    data: ContainerTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import ContainerLevelMetricsType, ContainerStatusType, MethodNameType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ContainerTypeDef",
    "CorsRuleOutputTypeDef",
    "CorsRuleTypeDef",
    "TagTypeDef",
    "DeleteContainerInputRequestTypeDef",
    "DeleteContainerPolicyInputRequestTypeDef",
    "DeleteCorsPolicyInputRequestTypeDef",
    "DeleteLifecyclePolicyInputRequestTypeDef",
    "DeleteMetricPolicyInputRequestTypeDef",
    "DescribeContainerInputRequestTypeDef",
    "GetContainerPolicyInputRequestTypeDef",
    "GetContainerPolicyOutputTypeDef",
    "GetCorsPolicyInputRequestTypeDef",
    "GetLifecyclePolicyInputRequestTypeDef",
    "GetLifecyclePolicyOutputTypeDef",
    "GetMetricPolicyInputRequestTypeDef",
    "ListContainersInputListContainersPaginateTypeDef",
    "ListContainersInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "TagOutputTypeDef",
    "MetricPolicyRuleOutputTypeDef",
    "MetricPolicyRuleTypeDef",
    "PaginatorConfigTypeDef",
    "PutContainerPolicyInputRequestTypeDef",
    "PutLifecyclePolicyInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartAccessLoggingInputRequestTypeDef",
    "StopAccessLoggingInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "CreateContainerOutputTypeDef",
    "DescribeContainerOutputTypeDef",
    "ListContainersOutputTypeDef",
    "GetCorsPolicyOutputTypeDef",
    "PutCorsPolicyInputRequestTypeDef",
    "CreateContainerInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MetricPolicyOutputTypeDef",
    "MetricPolicyTypeDef",
    "GetMetricPolicyOutputTypeDef",
    "PutMetricPolicyInputRequestTypeDef",
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": ContainerStatusType,
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

_RequiredCorsRuleOutputTypeDef = TypedDict(
    "_RequiredCorsRuleOutputTypeDef",
    {
        "AllowedOrigins": List[str],
        "AllowedHeaders": List[str],
    },
)
_OptionalCorsRuleOutputTypeDef = TypedDict(
    "_OptionalCorsRuleOutputTypeDef",
    {
        "AllowedMethods": List[MethodNameType],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)


class CorsRuleOutputTypeDef(_RequiredCorsRuleOutputTypeDef, _OptionalCorsRuleOutputTypeDef):
    pass


_RequiredCorsRuleTypeDef = TypedDict(
    "_RequiredCorsRuleTypeDef",
    {
        "AllowedOrigins": Sequence[str],
        "AllowedHeaders": Sequence[str],
    },
)
_OptionalCorsRuleTypeDef = TypedDict(
    "_OptionalCorsRuleTypeDef",
    {
        "AllowedMethods": Sequence[MethodNameType],
        "MaxAgeSeconds": int,
        "ExposeHeaders": Sequence[str],
    },
    total=False,
)


class CorsRuleTypeDef(_RequiredCorsRuleTypeDef, _OptionalCorsRuleTypeDef):
    pass


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


DeleteContainerInputRequestTypeDef = TypedDict(
    "DeleteContainerInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteContainerPolicyInputRequestTypeDef = TypedDict(
    "DeleteContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteCorsPolicyInputRequestTypeDef = TypedDict(
    "DeleteCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteLifecyclePolicyInputRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteMetricPolicyInputRequestTypeDef = TypedDict(
    "DeleteMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DescribeContainerInputRequestTypeDef = TypedDict(
    "DescribeContainerInputRequestTypeDef",
    {
        "ContainerName": str,
    },
    total=False,
)

GetContainerPolicyInputRequestTypeDef = TypedDict(
    "GetContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetContainerPolicyOutputTypeDef = TypedDict(
    "GetContainerPolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCorsPolicyInputRequestTypeDef = TypedDict(
    "GetCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetLifecyclePolicyInputRequestTypeDef = TypedDict(
    "GetLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetLifecyclePolicyOutputTypeDef = TypedDict(
    "GetLifecyclePolicyOutputTypeDef",
    {
        "LifecyclePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricPolicyInputRequestTypeDef = TypedDict(
    "GetMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

ListContainersInputListContainersPaginateTypeDef = TypedDict(
    "ListContainersInputListContainersPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListContainersInputRequestTypeDef = TypedDict(
    "ListContainersInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "Resource": str,
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


MetricPolicyRuleOutputTypeDef = TypedDict(
    "MetricPolicyRuleOutputTypeDef",
    {
        "ObjectGroup": str,
        "ObjectGroupName": str,
    },
)

MetricPolicyRuleTypeDef = TypedDict(
    "MetricPolicyRuleTypeDef",
    {
        "ObjectGroup": str,
        "ObjectGroupName": str,
    },
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

PutContainerPolicyInputRequestTypeDef = TypedDict(
    "PutContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "Policy": str,
    },
)

PutLifecyclePolicyInputRequestTypeDef = TypedDict(
    "PutLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "LifecyclePolicy": str,
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

StartAccessLoggingInputRequestTypeDef = TypedDict(
    "StartAccessLoggingInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

StopAccessLoggingInputRequestTypeDef = TypedDict(
    "StopAccessLoggingInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": Sequence[str],
    },
)

CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef",
    {
        "Container": ContainerTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef",
    {
        "Container": ContainerTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainersOutputTypeDef = TypedDict(
    "ListContainersOutputTypeDef",
    {
        "Containers": List[ContainerTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCorsPolicyOutputTypeDef = TypedDict(
    "GetCorsPolicyOutputTypeDef",
    {
        "CorsPolicy": List[CorsRuleOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutCorsPolicyInputRequestTypeDef = TypedDict(
    "PutCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "CorsPolicy": Sequence[CorsRuleTypeDef],
    },
)

_RequiredCreateContainerInputRequestTypeDef = TypedDict(
    "_RequiredCreateContainerInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
_OptionalCreateContainerInputRequestTypeDef = TypedDict(
    "_OptionalCreateContainerInputRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateContainerInputRequestTypeDef(
    _RequiredCreateContainerInputRequestTypeDef, _OptionalCreateContainerInputRequestTypeDef
):
    pass


TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "Resource": str,
        "Tags": Sequence[TagTypeDef],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMetricPolicyOutputTypeDef = TypedDict(
    "_RequiredMetricPolicyOutputTypeDef",
    {
        "ContainerLevelMetrics": ContainerLevelMetricsType,
    },
)
_OptionalMetricPolicyOutputTypeDef = TypedDict(
    "_OptionalMetricPolicyOutputTypeDef",
    {
        "MetricPolicyRules": List[MetricPolicyRuleOutputTypeDef],
    },
    total=False,
)


class MetricPolicyOutputTypeDef(
    _RequiredMetricPolicyOutputTypeDef, _OptionalMetricPolicyOutputTypeDef
):
    pass


_RequiredMetricPolicyTypeDef = TypedDict(
    "_RequiredMetricPolicyTypeDef",
    {
        "ContainerLevelMetrics": ContainerLevelMetricsType,
    },
)
_OptionalMetricPolicyTypeDef = TypedDict(
    "_OptionalMetricPolicyTypeDef",
    {
        "MetricPolicyRules": Sequence[MetricPolicyRuleTypeDef],
    },
    total=False,
)


class MetricPolicyTypeDef(_RequiredMetricPolicyTypeDef, _OptionalMetricPolicyTypeDef):
    pass


GetMetricPolicyOutputTypeDef = TypedDict(
    "GetMetricPolicyOutputTypeDef",
    {
        "MetricPolicy": MetricPolicyOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutMetricPolicyInputRequestTypeDef = TypedDict(
    "PutMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "MetricPolicy": MetricPolicyTypeDef,
    },
)
