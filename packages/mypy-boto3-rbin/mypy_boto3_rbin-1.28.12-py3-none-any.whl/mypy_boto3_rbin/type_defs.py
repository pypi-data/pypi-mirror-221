"""
Type annotations for rbin service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/type_defs/)

Usage::

    ```python
    from mypy_boto3_rbin.type_defs import ResourceTagTypeDef

    data: ResourceTagTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import LockStateType, ResourceTypeType, RuleStatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ResourceTagTypeDef",
    "RetentionPeriodTypeDef",
    "TagTypeDef",
    "ResourceTagOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodOutputTypeDef",
    "TagOutputTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "GetRuleRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "UnlockDelayOutputTypeDef",
    "UnlockDelayTypeDef",
    "UnlockRuleRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ListRulesRequestRequestTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "RuleSummaryTypeDef",
    "UpdateRuleResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListRulesRequestListRulesPaginateTypeDef",
    "LockConfigurationOutputTypeDef",
    "LockConfigurationTypeDef",
    "ListRulesResponseTypeDef",
    "CreateRuleResponseTypeDef",
    "GetRuleResponseTypeDef",
    "LockRuleResponseTypeDef",
    "UnlockRuleResponseTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "LockRuleRequestRequestTypeDef",
)

_RequiredResourceTagTypeDef = TypedDict(
    "_RequiredResourceTagTypeDef",
    {
        "ResourceTagKey": str,
    },
)
_OptionalResourceTagTypeDef = TypedDict(
    "_OptionalResourceTagTypeDef",
    {
        "ResourceTagValue": str,
    },
    total=False,
)


class ResourceTagTypeDef(_RequiredResourceTagTypeDef, _OptionalResourceTagTypeDef):
    pass


RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "RetentionPeriodValue": int,
        "RetentionPeriodUnit": Literal["DAYS"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredResourceTagOutputTypeDef = TypedDict(
    "_RequiredResourceTagOutputTypeDef",
    {
        "ResourceTagKey": str,
    },
)
_OptionalResourceTagOutputTypeDef = TypedDict(
    "_OptionalResourceTagOutputTypeDef",
    {
        "ResourceTagValue": str,
    },
    total=False,
)


class ResourceTagOutputTypeDef(
    _RequiredResourceTagOutputTypeDef, _OptionalResourceTagOutputTypeDef
):
    pass


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

RetentionPeriodOutputTypeDef = TypedDict(
    "RetentionPeriodOutputTypeDef",
    {
        "RetentionPeriodValue": int,
        "RetentionPeriodUnit": Literal["DAYS"],
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "Identifier": str,
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

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

UnlockDelayOutputTypeDef = TypedDict(
    "UnlockDelayOutputTypeDef",
    {
        "UnlockDelayValue": int,
        "UnlockDelayUnit": Literal["DAYS"],
    },
)

UnlockDelayTypeDef = TypedDict(
    "UnlockDelayTypeDef",
    {
        "UnlockDelayValue": int,
        "UnlockDelayUnit": Literal["DAYS"],
    },
)

UnlockRuleRequestRequestTypeDef = TypedDict(
    "UnlockRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredListRulesRequestRequestTypeDef = TypedDict(
    "_RequiredListRulesRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeType,
    },
)
_OptionalListRulesRequestRequestTypeDef = TypedDict(
    "_OptionalListRulesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ResourceTags": Sequence[ResourceTagTypeDef],
        "LockState": LockStateType,
    },
    total=False,
)


class ListRulesRequestRequestTypeDef(
    _RequiredListRulesRequestRequestTypeDef, _OptionalListRulesRequestRequestTypeDef
):
    pass


_RequiredUpdateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleRequestRequestTypeDef",
    {
        "RetentionPeriod": RetentionPeriodTypeDef,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "ResourceTags": Sequence[ResourceTagTypeDef],
    },
    total=False,
)


class UpdateRuleRequestRequestTypeDef(
    _RequiredUpdateRuleRequestRequestTypeDef, _OptionalUpdateRuleRequestRequestTypeDef
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "RetentionPeriod": RetentionPeriodOutputTypeDef,
        "LockState": LockStateType,
    },
    total=False,
)

UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": RetentionPeriodOutputTypeDef,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "ResourceTags": List[ResourceTagOutputTypeDef],
        "Status": RuleStatusType,
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "_RequiredListRulesRequestListRulesPaginateTypeDef",
    {
        "ResourceType": ResourceTypeType,
    },
)
_OptionalListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "_OptionalListRulesRequestListRulesPaginateTypeDef",
    {
        "ResourceTags": Sequence[ResourceTagTypeDef],
        "LockState": LockStateType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListRulesRequestListRulesPaginateTypeDef(
    _RequiredListRulesRequestListRulesPaginateTypeDef,
    _OptionalListRulesRequestListRulesPaginateTypeDef,
):
    pass


LockConfigurationOutputTypeDef = TypedDict(
    "LockConfigurationOutputTypeDef",
    {
        "UnlockDelay": UnlockDelayOutputTypeDef,
    },
)

LockConfigurationTypeDef = TypedDict(
    "LockConfigurationTypeDef",
    {
        "UnlockDelay": UnlockDelayTypeDef,
    },
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "Rules": List[RuleSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": RetentionPeriodOutputTypeDef,
        "Description": str,
        "Tags": List[TagOutputTypeDef],
        "ResourceType": ResourceTypeType,
        "ResourceTags": List[ResourceTagOutputTypeDef],
        "Status": RuleStatusType,
        "LockConfiguration": LockConfigurationOutputTypeDef,
        "LockState": LockStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": RetentionPeriodOutputTypeDef,
        "ResourceTags": List[ResourceTagOutputTypeDef],
        "Status": RuleStatusType,
        "LockConfiguration": LockConfigurationOutputTypeDef,
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LockRuleResponseTypeDef = TypedDict(
    "LockRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": RetentionPeriodOutputTypeDef,
        "ResourceTags": List[ResourceTagOutputTypeDef],
        "Status": RuleStatusType,
        "LockConfiguration": LockConfigurationOutputTypeDef,
        "LockState": LockStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UnlockRuleResponseTypeDef = TypedDict(
    "UnlockRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": RetentionPeriodOutputTypeDef,
        "ResourceTags": List[ResourceTagOutputTypeDef],
        "Status": RuleStatusType,
        "LockConfiguration": LockConfigurationOutputTypeDef,
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestRequestTypeDef",
    {
        "RetentionPeriod": RetentionPeriodTypeDef,
        "ResourceType": ResourceTypeType,
    },
)
_OptionalCreateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Sequence[TagTypeDef],
        "ResourceTags": Sequence[ResourceTagTypeDef],
        "LockConfiguration": LockConfigurationTypeDef,
    },
    total=False,
)


class CreateRuleRequestRequestTypeDef(
    _RequiredCreateRuleRequestRequestTypeDef, _OptionalCreateRuleRequestRequestTypeDef
):
    pass


LockRuleRequestRequestTypeDef = TypedDict(
    "LockRuleRequestRequestTypeDef",
    {
        "Identifier": str,
        "LockConfiguration": LockConfigurationTypeDef,
    },
)
