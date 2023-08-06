"""
Type annotations for cloud9 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloud9/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloud9.type_defs import TagTypeDef

    data: TagTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    ConnectionTypeType,
    EnvironmentLifecycleStatusType,
    EnvironmentStatusType,
    EnvironmentTypeType,
    ManagedCredentialsActionType,
    ManagedCredentialsStatusType,
    MemberPermissionsType,
    PermissionsType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "TagTypeDef",
    "CreateEnvironmentEC2ResultTypeDef",
    "CreateEnvironmentMembershipRequestRequestTypeDef",
    "EnvironmentMemberTypeDef",
    "DeleteEnvironmentMembershipRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DescribeEnvironmentMembershipsRequestDescribeEnvironmentMembershipsPaginateTypeDef",
    "DescribeEnvironmentMembershipsRequestRequestTypeDef",
    "DescribeEnvironmentStatusRequestRequestTypeDef",
    "DescribeEnvironmentStatusResultTypeDef",
    "DescribeEnvironmentsRequestRequestTypeDef",
    "EnvironmentLifecycleTypeDef",
    "ListEnvironmentsRequestListEnvironmentsPaginateTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListEnvironmentsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEnvironmentMembershipRequestRequestTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
    "CreateEnvironmentEC2RequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateEnvironmentMembershipResultTypeDef",
    "DescribeEnvironmentMembershipsResultTypeDef",
    "UpdateEnvironmentMembershipResultTypeDef",
    "EnvironmentTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "DescribeEnvironmentsResultTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateEnvironmentEC2ResultTypeDef = TypedDict(
    "CreateEnvironmentEC2ResultTypeDef",
    {
        "environmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "CreateEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
        "permissions": MemberPermissionsType,
    },
)

_RequiredEnvironmentMemberTypeDef = TypedDict(
    "_RequiredEnvironmentMemberTypeDef",
    {
        "permissions": PermissionsType,
        "userId": str,
        "userArn": str,
        "environmentId": str,
    },
)
_OptionalEnvironmentMemberTypeDef = TypedDict(
    "_OptionalEnvironmentMemberTypeDef",
    {
        "lastAccess": datetime,
    },
    total=False,
)


class EnvironmentMemberTypeDef(
    _RequiredEnvironmentMemberTypeDef, _OptionalEnvironmentMemberTypeDef
):
    pass


DeleteEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

DescribeEnvironmentMembershipsRequestDescribeEnvironmentMembershipsPaginateTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsRequestDescribeEnvironmentMembershipsPaginateTypeDef",
    {
        "userArn": str,
        "environmentId": str,
        "permissions": Sequence[PermissionsType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeEnvironmentMembershipsRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsRequestRequestTypeDef",
    {
        "userArn": str,
        "environmentId": str,
        "permissions": Sequence[PermissionsType],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeEnvironmentStatusRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentStatusRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

DescribeEnvironmentStatusResultTypeDef = TypedDict(
    "DescribeEnvironmentStatusResultTypeDef",
    {
        "status": EnvironmentStatusType,
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentsRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentsRequestRequestTypeDef",
    {
        "environmentIds": Sequence[str],
    },
)

EnvironmentLifecycleTypeDef = TypedDict(
    "EnvironmentLifecycleTypeDef",
    {
        "status": EnvironmentLifecycleStatusType,
        "reason": str,
        "failureResource": str,
    },
    total=False,
)

ListEnvironmentsRequestListEnvironmentsPaginateTypeDef = TypedDict(
    "ListEnvironmentsRequestListEnvironmentsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEnvironmentsResultTypeDef = TypedDict(
    "ListEnvironmentsResultTypeDef",
    {
        "nextToken": str,
        "environmentIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "UpdateEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
        "permissions": MemberPermissionsType,
    },
)

_RequiredUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "managedCredentialsAction": ManagedCredentialsActionType,
    },
    total=False,
)


class UpdateEnvironmentRequestRequestTypeDef(
    _RequiredUpdateEnvironmentRequestRequestTypeDef, _OptionalUpdateEnvironmentRequestRequestTypeDef
):
    pass


_RequiredCreateEnvironmentEC2RequestRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentEC2RequestRequestTypeDef",
    {
        "name": str,
        "instanceType": str,
    },
)
_OptionalCreateEnvironmentEC2RequestRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentEC2RequestRequestTypeDef",
    {
        "description": str,
        "clientRequestToken": str,
        "subnetId": str,
        "imageId": str,
        "automaticStopTimeMinutes": int,
        "ownerArn": str,
        "tags": Sequence[TagTypeDef],
        "connectionType": ConnectionTypeType,
        "dryRun": bool,
    },
    total=False,
)


class CreateEnvironmentEC2RequestRequestTypeDef(
    _RequiredCreateEnvironmentEC2RequestRequestTypeDef,
    _OptionalCreateEnvironmentEC2RequestRequestTypeDef,
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

CreateEnvironmentMembershipResultTypeDef = TypedDict(
    "CreateEnvironmentMembershipResultTypeDef",
    {
        "membership": EnvironmentMemberTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentMembershipsResultTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsResultTypeDef",
    {
        "memberships": List[EnvironmentMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEnvironmentMembershipResultTypeDef = TypedDict(
    "UpdateEnvironmentMembershipResultTypeDef",
    {
        "membership": EnvironmentMemberTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnvironmentTypeDef = TypedDict(
    "_RequiredEnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "arn": str,
        "ownerArn": str,
    },
)
_OptionalEnvironmentTypeDef = TypedDict(
    "_OptionalEnvironmentTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "connectionType": ConnectionTypeType,
        "lifecycle": EnvironmentLifecycleTypeDef,
        "managedCredentialsStatus": ManagedCredentialsStatusType,
    },
    total=False,
)


class EnvironmentTypeDef(_RequiredEnvironmentTypeDef, _OptionalEnvironmentTypeDef):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentsResultTypeDef = TypedDict(
    "DescribeEnvironmentsResultTypeDef",
    {
        "environments": List[EnvironmentTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
