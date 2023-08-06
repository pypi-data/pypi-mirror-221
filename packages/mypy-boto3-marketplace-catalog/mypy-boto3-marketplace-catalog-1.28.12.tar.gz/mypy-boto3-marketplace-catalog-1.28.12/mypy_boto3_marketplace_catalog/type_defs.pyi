"""
Type annotations for marketplace-catalog service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/type_defs/)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import CancelChangeSetRequestRequestTypeDef

    data: CancelChangeSetRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from .literals import ChangeStatusType, FailureCodeType, OwnershipTypeType, SortOrderType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelChangeSetRequestRequestTypeDef",
    "CancelChangeSetResponseTypeDef",
    "ChangeSetSummaryListItemTypeDef",
    "EntityOutputTypeDef",
    "ErrorDetailTypeDef",
    "EntityTypeDef",
    "TagTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DescribeChangeSetRequestRequestTypeDef",
    "DescribeEntityRequestRequestTypeDef",
    "DescribeEntityResponseTypeDef",
    "EntitySummaryTypeDef",
    "FilterTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "SortTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartChangeSetResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ChangeSummaryTypeDef",
    "ChangeTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListChangeSetsRequestListChangeSetsPaginateTypeDef",
    "ListChangeSetsRequestRequestTypeDef",
    "ListEntitiesRequestListEntitiesPaginateTypeDef",
    "ListEntitiesRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "StartChangeSetRequestRequestTypeDef",
)

CancelChangeSetRequestRequestTypeDef = TypedDict(
    "CancelChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

CancelChangeSetResponseTypeDef = TypedDict(
    "CancelChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeSetSummaryListItemTypeDef = TypedDict(
    "ChangeSetSummaryListItemTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "EntityIdList": List[str],
        "FailureCode": FailureCodeType,
    },
    total=False,
)

_RequiredEntityOutputTypeDef = TypedDict(
    "_RequiredEntityOutputTypeDef",
    {
        "Type": str,
    },
)
_OptionalEntityOutputTypeDef = TypedDict(
    "_OptionalEntityOutputTypeDef",
    {
        "Identifier": str,
    },
    total=False,
)

class EntityOutputTypeDef(_RequiredEntityOutputTypeDef, _OptionalEntityOutputTypeDef):
    pass

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredEntityTypeDef = TypedDict(
    "_RequiredEntityTypeDef",
    {
        "Type": str,
    },
)
_OptionalEntityTypeDef = TypedDict(
    "_OptionalEntityTypeDef",
    {
        "Identifier": str,
    },
    total=False,
)

class EntityTypeDef(_RequiredEntityTypeDef, _OptionalEntityTypeDef):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeChangeSetRequestRequestTypeDef = TypedDict(
    "DescribeChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

DescribeEntityRequestRequestTypeDef = TypedDict(
    "DescribeEntityRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityId": str,
    },
)

DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntitySummaryTypeDef = TypedDict(
    "EntitySummaryTypeDef",
    {
        "Name": str,
        "EntityType": str,
        "EntityId": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Visibility": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "ValueList": Sequence[str],
    },
    total=False,
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "SortBy": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
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

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
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

StartChangeSetResponseTypeDef = TypedDict(
    "StartChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

ListChangeSetsResponseTypeDef = TypedDict(
    "ListChangeSetsResponseTypeDef",
    {
        "ChangeSetSummaryList": List[ChangeSetSummaryListItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeSummaryTypeDef = TypedDict(
    "ChangeSummaryTypeDef",
    {
        "ChangeType": str,
        "Entity": EntityOutputTypeDef,
        "Details": str,
        "ErrorDetailList": List[ErrorDetailTypeDef],
        "ChangeName": str,
    },
    total=False,
)

_RequiredChangeTypeDef = TypedDict(
    "_RequiredChangeTypeDef",
    {
        "ChangeType": str,
        "Entity": EntityTypeDef,
        "Details": str,
    },
)
_OptionalChangeTypeDef = TypedDict(
    "_OptionalChangeTypeDef",
    {
        "EntityTags": Sequence[TagTypeDef],
        "ChangeName": str,
    },
    total=False,
)

class ChangeTypeDef(_RequiredChangeTypeDef, _OptionalChangeTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "EntitySummaryList": List[EntitySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChangeSetsRequestListChangeSetsPaginateTypeDef = TypedDict(
    "_RequiredListChangeSetsRequestListChangeSetsPaginateTypeDef",
    {
        "Catalog": str,
    },
)
_OptionalListChangeSetsRequestListChangeSetsPaginateTypeDef = TypedDict(
    "_OptionalListChangeSetsRequestListChangeSetsPaginateTypeDef",
    {
        "FilterList": Sequence[FilterTypeDef],
        "Sort": SortTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListChangeSetsRequestListChangeSetsPaginateTypeDef(
    _RequiredListChangeSetsRequestListChangeSetsPaginateTypeDef,
    _OptionalListChangeSetsRequestListChangeSetsPaginateTypeDef,
):
    pass

_RequiredListChangeSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListChangeSetsRequestRequestTypeDef",
    {
        "Catalog": str,
    },
)
_OptionalListChangeSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListChangeSetsRequestRequestTypeDef",
    {
        "FilterList": Sequence[FilterTypeDef],
        "Sort": SortTypeDef,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChangeSetsRequestRequestTypeDef(
    _RequiredListChangeSetsRequestRequestTypeDef, _OptionalListChangeSetsRequestRequestTypeDef
):
    pass

_RequiredListEntitiesRequestListEntitiesPaginateTypeDef = TypedDict(
    "_RequiredListEntitiesRequestListEntitiesPaginateTypeDef",
    {
        "Catalog": str,
        "EntityType": str,
    },
)
_OptionalListEntitiesRequestListEntitiesPaginateTypeDef = TypedDict(
    "_OptionalListEntitiesRequestListEntitiesPaginateTypeDef",
    {
        "FilterList": Sequence[FilterTypeDef],
        "Sort": SortTypeDef,
        "OwnershipType": OwnershipTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListEntitiesRequestListEntitiesPaginateTypeDef(
    _RequiredListEntitiesRequestListEntitiesPaginateTypeDef,
    _OptionalListEntitiesRequestListEntitiesPaginateTypeDef,
):
    pass

_RequiredListEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredListEntitiesRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityType": str,
    },
)
_OptionalListEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalListEntitiesRequestRequestTypeDef",
    {
        "FilterList": Sequence[FilterTypeDef],
        "Sort": SortTypeDef,
        "NextToken": str,
        "MaxResults": int,
        "OwnershipType": OwnershipTypeType,
    },
    total=False,
)

class ListEntitiesRequestRequestTypeDef(
    _RequiredListEntitiesRequestRequestTypeDef, _OptionalListEntitiesRequestRequestTypeDef
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChangeSetResponseTypeDef = TypedDict(
    "DescribeChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "FailureCode": FailureCodeType,
        "FailureDescription": str,
        "ChangeSet": List[ChangeSummaryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartChangeSetRequestRequestTypeDef = TypedDict(
    "_RequiredStartChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSet": Sequence[ChangeTypeDef],
    },
)
_OptionalStartChangeSetRequestRequestTypeDef = TypedDict(
    "_OptionalStartChangeSetRequestRequestTypeDef",
    {
        "ChangeSetName": str,
        "ClientRequestToken": str,
        "ChangeSetTags": Sequence[TagTypeDef],
    },
    total=False,
)

class StartChangeSetRequestRequestTypeDef(
    _RequiredStartChangeSetRequestRequestTypeDef, _OptionalStartChangeSetRequestRequestTypeDef
):
    pass
