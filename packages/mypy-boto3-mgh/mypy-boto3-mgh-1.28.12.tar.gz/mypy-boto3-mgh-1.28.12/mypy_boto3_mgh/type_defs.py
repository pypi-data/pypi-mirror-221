"""
Type annotations for mgh service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/type_defs/)

Usage::

    ```python
    from mypy_boto3_mgh.type_defs import ApplicationStateTypeDef

    data: ApplicationStateTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import ApplicationStatusType, ResourceAttributeTypeType, StatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationStateTypeDef",
    "CreatedArtifactTypeDef",
    "DiscoveredResourceTypeDef",
    "CreateProgressUpdateStreamRequestRequestTypeDef",
    "CreatedArtifactOutputTypeDef",
    "DeleteProgressUpdateStreamRequestRequestTypeDef",
    "DescribeApplicationStateRequestRequestTypeDef",
    "DescribeApplicationStateResultTypeDef",
    "DescribeMigrationTaskRequestRequestTypeDef",
    "DisassociateCreatedArtifactRequestRequestTypeDef",
    "DisassociateDiscoveredResourceRequestRequestTypeDef",
    "DiscoveredResourceOutputTypeDef",
    "ImportMigrationTaskRequestRequestTypeDef",
    "ListApplicationStatesRequestListApplicationStatesPaginateTypeDef",
    "ListApplicationStatesRequestRequestTypeDef",
    "ListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef",
    "ListCreatedArtifactsRequestRequestTypeDef",
    "ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListMigrationTasksRequestListMigrationTasksPaginateTypeDef",
    "ListMigrationTasksRequestRequestTypeDef",
    "MigrationTaskSummaryTypeDef",
    "ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef",
    "ListProgressUpdateStreamsRequestRequestTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "ResourceAttributeOutputTypeDef",
    "TaskOutputTypeDef",
    "NotifyApplicationStateRequestRequestTypeDef",
    "TaskTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceAttributeTypeDef",
    "ResponseMetadataTypeDef",
    "ListApplicationStatesResultTypeDef",
    "AssociateCreatedArtifactRequestRequestTypeDef",
    "AssociateDiscoveredResourceRequestRequestTypeDef",
    "ListCreatedArtifactsResultTypeDef",
    "ListDiscoveredResourcesResultTypeDef",
    "ListMigrationTasksResultTypeDef",
    "ListProgressUpdateStreamsResultTypeDef",
    "MigrationTaskTypeDef",
    "NotifyMigrationTaskStateRequestRequestTypeDef",
    "PutResourceAttributesRequestRequestTypeDef",
    "DescribeMigrationTaskResultTypeDef",
)

ApplicationStateTypeDef = TypedDict(
    "ApplicationStateTypeDef",
    {
        "ApplicationId": str,
        "ApplicationStatus": ApplicationStatusType,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

_RequiredCreatedArtifactTypeDef = TypedDict(
    "_RequiredCreatedArtifactTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatedArtifactTypeDef = TypedDict(
    "_OptionalCreatedArtifactTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreatedArtifactTypeDef(_RequiredCreatedArtifactTypeDef, _OptionalCreatedArtifactTypeDef):
    pass


_RequiredDiscoveredResourceTypeDef = TypedDict(
    "_RequiredDiscoveredResourceTypeDef",
    {
        "ConfigurationId": str,
    },
)
_OptionalDiscoveredResourceTypeDef = TypedDict(
    "_OptionalDiscoveredResourceTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class DiscoveredResourceTypeDef(
    _RequiredDiscoveredResourceTypeDef, _OptionalDiscoveredResourceTypeDef
):
    pass


_RequiredCreateProgressUpdateStreamRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProgressUpdateStreamRequestRequestTypeDef",
    {
        "ProgressUpdateStreamName": str,
    },
)
_OptionalCreateProgressUpdateStreamRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProgressUpdateStreamRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateProgressUpdateStreamRequestRequestTypeDef(
    _RequiredCreateProgressUpdateStreamRequestRequestTypeDef,
    _OptionalCreateProgressUpdateStreamRequestRequestTypeDef,
):
    pass


_RequiredCreatedArtifactOutputTypeDef = TypedDict(
    "_RequiredCreatedArtifactOutputTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatedArtifactOutputTypeDef = TypedDict(
    "_OptionalCreatedArtifactOutputTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreatedArtifactOutputTypeDef(
    _RequiredCreatedArtifactOutputTypeDef, _OptionalCreatedArtifactOutputTypeDef
):
    pass


_RequiredDeleteProgressUpdateStreamRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteProgressUpdateStreamRequestRequestTypeDef",
    {
        "ProgressUpdateStreamName": str,
    },
)
_OptionalDeleteProgressUpdateStreamRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteProgressUpdateStreamRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteProgressUpdateStreamRequestRequestTypeDef(
    _RequiredDeleteProgressUpdateStreamRequestRequestTypeDef,
    _OptionalDeleteProgressUpdateStreamRequestRequestTypeDef,
):
    pass


DescribeApplicationStateRequestRequestTypeDef = TypedDict(
    "DescribeApplicationStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DescribeApplicationStateResultTypeDef = TypedDict(
    "DescribeApplicationStateResultTypeDef",
    {
        "ApplicationStatus": ApplicationStatusType,
        "LastUpdatedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMigrationTaskRequestRequestTypeDef = TypedDict(
    "DescribeMigrationTaskRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)

_RequiredDisassociateCreatedArtifactRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateCreatedArtifactRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "CreatedArtifactName": str,
    },
)
_OptionalDisassociateCreatedArtifactRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateCreatedArtifactRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisassociateCreatedArtifactRequestRequestTypeDef(
    _RequiredDisassociateCreatedArtifactRequestRequestTypeDef,
    _OptionalDisassociateCreatedArtifactRequestRequestTypeDef,
):
    pass


_RequiredDisassociateDiscoveredResourceRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateDiscoveredResourceRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "ConfigurationId": str,
    },
)
_OptionalDisassociateDiscoveredResourceRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateDiscoveredResourceRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisassociateDiscoveredResourceRequestRequestTypeDef(
    _RequiredDisassociateDiscoveredResourceRequestRequestTypeDef,
    _OptionalDisassociateDiscoveredResourceRequestRequestTypeDef,
):
    pass


_RequiredDiscoveredResourceOutputTypeDef = TypedDict(
    "_RequiredDiscoveredResourceOutputTypeDef",
    {
        "ConfigurationId": str,
    },
)
_OptionalDiscoveredResourceOutputTypeDef = TypedDict(
    "_OptionalDiscoveredResourceOutputTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class DiscoveredResourceOutputTypeDef(
    _RequiredDiscoveredResourceOutputTypeDef, _OptionalDiscoveredResourceOutputTypeDef
):
    pass


_RequiredImportMigrationTaskRequestRequestTypeDef = TypedDict(
    "_RequiredImportMigrationTaskRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
_OptionalImportMigrationTaskRequestRequestTypeDef = TypedDict(
    "_OptionalImportMigrationTaskRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ImportMigrationTaskRequestRequestTypeDef(
    _RequiredImportMigrationTaskRequestRequestTypeDef,
    _OptionalImportMigrationTaskRequestRequestTypeDef,
):
    pass


ListApplicationStatesRequestListApplicationStatesPaginateTypeDef = TypedDict(
    "ListApplicationStatesRequestListApplicationStatesPaginateTypeDef",
    {
        "ApplicationIds": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListApplicationStatesRequestRequestTypeDef = TypedDict(
    "ListApplicationStatesRequestRequestTypeDef",
    {
        "ApplicationIds": Sequence[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef = TypedDict(
    "_RequiredListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
_OptionalListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef = TypedDict(
    "_OptionalListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef(
    _RequiredListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef,
    _OptionalListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef,
):
    pass


_RequiredListCreatedArtifactsRequestRequestTypeDef = TypedDict(
    "_RequiredListCreatedArtifactsRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
_OptionalListCreatedArtifactsRequestRequestTypeDef = TypedDict(
    "_OptionalListCreatedArtifactsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListCreatedArtifactsRequestRequestTypeDef(
    _RequiredListCreatedArtifactsRequestRequestTypeDef,
    _OptionalListCreatedArtifactsRequestRequestTypeDef,
):
    pass


_RequiredListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
_OptionalListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef(
    _RequiredListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef,
    _OptionalListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef,
):
    pass


_RequiredListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
_OptionalListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDiscoveredResourcesRequestRequestTypeDef(
    _RequiredListDiscoveredResourcesRequestRequestTypeDef,
    _OptionalListDiscoveredResourcesRequestRequestTypeDef,
):
    pass


ListMigrationTasksRequestListMigrationTasksPaginateTypeDef = TypedDict(
    "ListMigrationTasksRequestListMigrationTasksPaginateTypeDef",
    {
        "ResourceName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListMigrationTasksRequestRequestTypeDef = TypedDict(
    "ListMigrationTasksRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResourceName": str,
    },
    total=False,
)

MigrationTaskSummaryTypeDef = TypedDict(
    "MigrationTaskSummaryTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": StatusType,
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)

ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef = TypedDict(
    "ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListProgressUpdateStreamsRequestRequestTypeDef = TypedDict(
    "ListProgressUpdateStreamsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ProgressUpdateStreamSummaryTypeDef = TypedDict(
    "ProgressUpdateStreamSummaryTypeDef",
    {
        "ProgressUpdateStreamName": str,
    },
    total=False,
)

ResourceAttributeOutputTypeDef = TypedDict(
    "ResourceAttributeOutputTypeDef",
    {
        "Type": ResourceAttributeTypeType,
        "Value": str,
    },
)

_RequiredTaskOutputTypeDef = TypedDict(
    "_RequiredTaskOutputTypeDef",
    {
        "Status": StatusType,
    },
)
_OptionalTaskOutputTypeDef = TypedDict(
    "_OptionalTaskOutputTypeDef",
    {
        "StatusDetail": str,
        "ProgressPercent": int,
    },
    total=False,
)


class TaskOutputTypeDef(_RequiredTaskOutputTypeDef, _OptionalTaskOutputTypeDef):
    pass


_RequiredNotifyApplicationStateRequestRequestTypeDef = TypedDict(
    "_RequiredNotifyApplicationStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Status": ApplicationStatusType,
    },
)
_OptionalNotifyApplicationStateRequestRequestTypeDef = TypedDict(
    "_OptionalNotifyApplicationStateRequestRequestTypeDef",
    {
        "UpdateDateTime": Union[datetime, str],
        "DryRun": bool,
    },
    total=False,
)


class NotifyApplicationStateRequestRequestTypeDef(
    _RequiredNotifyApplicationStateRequestRequestTypeDef,
    _OptionalNotifyApplicationStateRequestRequestTypeDef,
):
    pass


_RequiredTaskTypeDef = TypedDict(
    "_RequiredTaskTypeDef",
    {
        "Status": StatusType,
    },
)
_OptionalTaskTypeDef = TypedDict(
    "_OptionalTaskTypeDef",
    {
        "StatusDetail": str,
        "ProgressPercent": int,
    },
    total=False,
)


class TaskTypeDef(_RequiredTaskTypeDef, _OptionalTaskTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResourceAttributeTypeDef = TypedDict(
    "ResourceAttributeTypeDef",
    {
        "Type": ResourceAttributeTypeType,
        "Value": str,
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

ListApplicationStatesResultTypeDef = TypedDict(
    "ListApplicationStatesResultTypeDef",
    {
        "ApplicationStateList": List[ApplicationStateTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateCreatedArtifactRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateCreatedArtifactRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "CreatedArtifact": CreatedArtifactTypeDef,
    },
)
_OptionalAssociateCreatedArtifactRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateCreatedArtifactRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AssociateCreatedArtifactRequestRequestTypeDef(
    _RequiredAssociateCreatedArtifactRequestRequestTypeDef,
    _OptionalAssociateCreatedArtifactRequestRequestTypeDef,
):
    pass


_RequiredAssociateDiscoveredResourceRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateDiscoveredResourceRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "DiscoveredResource": DiscoveredResourceTypeDef,
    },
)
_OptionalAssociateDiscoveredResourceRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateDiscoveredResourceRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AssociateDiscoveredResourceRequestRequestTypeDef(
    _RequiredAssociateDiscoveredResourceRequestRequestTypeDef,
    _OptionalAssociateDiscoveredResourceRequestRequestTypeDef,
):
    pass


ListCreatedArtifactsResultTypeDef = TypedDict(
    "ListCreatedArtifactsResultTypeDef",
    {
        "NextToken": str,
        "CreatedArtifactList": List[CreatedArtifactOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDiscoveredResourcesResultTypeDef = TypedDict(
    "ListDiscoveredResourcesResultTypeDef",
    {
        "NextToken": str,
        "DiscoveredResourceList": List[DiscoveredResourceOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMigrationTasksResultTypeDef = TypedDict(
    "ListMigrationTasksResultTypeDef",
    {
        "NextToken": str,
        "MigrationTaskSummaryList": List[MigrationTaskSummaryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProgressUpdateStreamsResultTypeDef = TypedDict(
    "ListProgressUpdateStreamsResultTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[ProgressUpdateStreamSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MigrationTaskTypeDef = TypedDict(
    "MigrationTaskTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": TaskOutputTypeDef,
        "UpdateDateTime": datetime,
        "ResourceAttributeList": List[ResourceAttributeOutputTypeDef],
    },
    total=False,
)

_RequiredNotifyMigrationTaskStateRequestRequestTypeDef = TypedDict(
    "_RequiredNotifyMigrationTaskStateRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": TaskTypeDef,
        "UpdateDateTime": Union[datetime, str],
        "NextUpdateSeconds": int,
    },
)
_OptionalNotifyMigrationTaskStateRequestRequestTypeDef = TypedDict(
    "_OptionalNotifyMigrationTaskStateRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class NotifyMigrationTaskStateRequestRequestTypeDef(
    _RequiredNotifyMigrationTaskStateRequestRequestTypeDef,
    _OptionalNotifyMigrationTaskStateRequestRequestTypeDef,
):
    pass


_RequiredPutResourceAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutResourceAttributesRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "ResourceAttributeList": Sequence[ResourceAttributeTypeDef],
    },
)
_OptionalPutResourceAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutResourceAttributesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class PutResourceAttributesRequestRequestTypeDef(
    _RequiredPutResourceAttributesRequestRequestTypeDef,
    _OptionalPutResourceAttributesRequestRequestTypeDef,
):
    pass


DescribeMigrationTaskResultTypeDef = TypedDict(
    "DescribeMigrationTaskResultTypeDef",
    {
        "MigrationTask": MigrationTaskTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
