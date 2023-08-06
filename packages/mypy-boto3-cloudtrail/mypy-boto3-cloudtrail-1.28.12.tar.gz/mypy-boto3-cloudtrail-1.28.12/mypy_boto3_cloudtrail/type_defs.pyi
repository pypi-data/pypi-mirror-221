"""
Type annotations for cloudtrail service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudtrail.type_defs import TagTypeDef

    data: TagTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    DeliveryStatusType,
    DestinationTypeType,
    EventDataStoreStatusType,
    ImportFailureStatusType,
    ImportStatusType,
    InsightTypeType,
    LookupAttributeKeyType,
    QueryStatusType,
    ReadWriteTypeType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "TagTypeDef",
    "AdvancedFieldSelectorOutputTypeDef",
    "AdvancedFieldSelectorTypeDef",
    "CancelQueryRequestRequestTypeDef",
    "CancelQueryResponseTypeDef",
    "ChannelTypeDef",
    "DestinationTypeDef",
    "DestinationOutputTypeDef",
    "TagOutputTypeDef",
    "CreateTrailResponseTypeDef",
    "DataResourceOutputTypeDef",
    "DataResourceTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteEventDataStoreRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteTrailRequestRequestTypeDef",
    "DeregisterOrganizationDelegatedAdminRequestRequestTypeDef",
    "DescribeQueryRequestRequestTypeDef",
    "QueryStatisticsForDescribeQueryTypeDef",
    "DescribeTrailsRequestRequestTypeDef",
    "TrailTypeDef",
    "ResourceTypeDef",
    "GetChannelRequestRequestTypeDef",
    "IngestionStatusTypeDef",
    "GetEventDataStoreRequestRequestTypeDef",
    "GetEventSelectorsRequestRequestTypeDef",
    "GetImportRequestRequestTypeDef",
    "ImportStatisticsTypeDef",
    "GetInsightSelectorsRequestRequestTypeDef",
    "InsightSelectorOutputTypeDef",
    "GetQueryResultsRequestRequestTypeDef",
    "QueryStatisticsTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetTrailRequestRequestTypeDef",
    "GetTrailStatusRequestRequestTypeDef",
    "GetTrailStatusResponseTypeDef",
    "ImportFailureListItemTypeDef",
    "S3ImportSourceOutputTypeDef",
    "S3ImportSourceTypeDef",
    "ImportsListItemTypeDef",
    "InsightSelectorTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListEventDataStoresRequestRequestTypeDef",
    "ListImportFailuresRequestListImportFailuresPaginateTypeDef",
    "ListImportFailuresRequestRequestTypeDef",
    "ListImportsRequestListImportsPaginateTypeDef",
    "ListImportsRequestRequestTypeDef",
    "ListPublicKeysRequestListPublicKeysPaginateTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "PublicKeyTypeDef",
    "ListQueriesRequestRequestTypeDef",
    "QueryTypeDef",
    "ListTagsRequestListTagsPaginateTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTrailsRequestListTrailsPaginateTypeDef",
    "ListTrailsRequestRequestTypeDef",
    "TrailInfoTypeDef",
    "LookupAttributeTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RegisterOrganizationDelegatedAdminRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreEventDataStoreRequestRequestTypeDef",
    "StartEventDataStoreIngestionRequestRequestTypeDef",
    "StartLoggingRequestRequestTypeDef",
    "StartQueryRequestRequestTypeDef",
    "StartQueryResponseTypeDef",
    "StopEventDataStoreIngestionRequestRequestTypeDef",
    "StopImportRequestRequestTypeDef",
    "StopLoggingRequestRequestTypeDef",
    "UpdateTrailRequestRequestTypeDef",
    "UpdateTrailResponseTypeDef",
    "AddTagsRequestRequestTypeDef",
    "CreateTrailRequestRequestTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "AdvancedEventSelectorOutputTypeDef",
    "AdvancedEventSelectorTypeDef",
    "ListChannelsResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "ResourceTagTypeDef",
    "EventSelectorOutputTypeDef",
    "EventSelectorTypeDef",
    "DescribeQueryResponseTypeDef",
    "DescribeTrailsResponseTypeDef",
    "GetTrailResponseTypeDef",
    "EventTypeDef",
    "GetInsightSelectorsResponseTypeDef",
    "PutInsightSelectorsResponseTypeDef",
    "GetQueryResultsResponseTypeDef",
    "ListImportFailuresResponseTypeDef",
    "ImportSourceOutputTypeDef",
    "ImportSourceTypeDef",
    "ListImportsResponseTypeDef",
    "PutInsightSelectorsRequestRequestTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListQueriesResponseTypeDef",
    "ListTrailsResponseTypeDef",
    "LookupEventsRequestLookupEventsPaginateTypeDef",
    "LookupEventsRequestRequestTypeDef",
    "CreateEventDataStoreResponseTypeDef",
    "EventDataStoreTypeDef",
    "GetEventDataStoreResponseTypeDef",
    "RestoreEventDataStoreResponseTypeDef",
    "SourceConfigTypeDef",
    "UpdateEventDataStoreResponseTypeDef",
    "CreateEventDataStoreRequestRequestTypeDef",
    "UpdateEventDataStoreRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "GetEventSelectorsResponseTypeDef",
    "PutEventSelectorsResponseTypeDef",
    "PutEventSelectorsRequestRequestTypeDef",
    "LookupEventsResponseTypeDef",
    "GetImportResponseTypeDef",
    "StartImportResponseTypeDef",
    "StopImportResponseTypeDef",
    "StartImportRequestRequestTypeDef",
    "ListEventDataStoresResponseTypeDef",
    "GetChannelResponseTypeDef",
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

_RequiredAdvancedFieldSelectorOutputTypeDef = TypedDict(
    "_RequiredAdvancedFieldSelectorOutputTypeDef",
    {
        "Field": str,
    },
)
_OptionalAdvancedFieldSelectorOutputTypeDef = TypedDict(
    "_OptionalAdvancedFieldSelectorOutputTypeDef",
    {
        "Equals": List[str],
        "StartsWith": List[str],
        "EndsWith": List[str],
        "NotEquals": List[str],
        "NotStartsWith": List[str],
        "NotEndsWith": List[str],
    },
    total=False,
)

class AdvancedFieldSelectorOutputTypeDef(
    _RequiredAdvancedFieldSelectorOutputTypeDef, _OptionalAdvancedFieldSelectorOutputTypeDef
):
    pass

_RequiredAdvancedFieldSelectorTypeDef = TypedDict(
    "_RequiredAdvancedFieldSelectorTypeDef",
    {
        "Field": str,
    },
)
_OptionalAdvancedFieldSelectorTypeDef = TypedDict(
    "_OptionalAdvancedFieldSelectorTypeDef",
    {
        "Equals": Sequence[str],
        "StartsWith": Sequence[str],
        "EndsWith": Sequence[str],
        "NotEquals": Sequence[str],
        "NotStartsWith": Sequence[str],
        "NotEndsWith": Sequence[str],
    },
    total=False,
)

class AdvancedFieldSelectorTypeDef(
    _RequiredAdvancedFieldSelectorTypeDef, _OptionalAdvancedFieldSelectorTypeDef
):
    pass

_RequiredCancelQueryRequestRequestTypeDef = TypedDict(
    "_RequiredCancelQueryRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
_OptionalCancelQueryRequestRequestTypeDef = TypedDict(
    "_OptionalCancelQueryRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
    total=False,
)

class CancelQueryRequestRequestTypeDef(
    _RequiredCancelQueryRequestRequestTypeDef, _OptionalCancelQueryRequestRequestTypeDef
):
    pass

CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryStatus": QueryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "Type": DestinationTypeType,
        "Location": str,
    },
)

DestinationOutputTypeDef = TypedDict(
    "DestinationOutputTypeDef",
    {
        "Type": DestinationTypeType,
        "Location": str,
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

CreateTrailResponseTypeDef = TypedDict(
    "CreateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataResourceOutputTypeDef = TypedDict(
    "DataResourceOutputTypeDef",
    {
        "Type": str,
        "Values": List[str],
    },
    total=False,
)

DataResourceTypeDef = TypedDict(
    "DataResourceTypeDef",
    {
        "Type": str,
        "Values": Sequence[str],
    },
    total=False,
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "Channel": str,
    },
)

DeleteEventDataStoreRequestRequestTypeDef = TypedDict(
    "DeleteEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteTrailRequestRequestTypeDef = TypedDict(
    "DeleteTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeregisterOrganizationDelegatedAdminRequestRequestTypeDef = TypedDict(
    "DeregisterOrganizationDelegatedAdminRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
    },
)

DescribeQueryRequestRequestTypeDef = TypedDict(
    "DescribeQueryRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "QueryId": str,
        "QueryAlias": str,
    },
    total=False,
)

QueryStatisticsForDescribeQueryTypeDef = TypedDict(
    "QueryStatisticsForDescribeQueryTypeDef",
    {
        "EventsMatched": int,
        "EventsScanned": int,
        "BytesScanned": int,
        "ExecutionTimeInMillis": int,
        "CreationTime": datetime,
    },
    total=False,
)

DescribeTrailsRequestRequestTypeDef = TypedDict(
    "DescribeTrailsRequestRequestTypeDef",
    {
        "trailNameList": Sequence[str],
        "includeShadowTrails": bool,
    },
    total=False,
)

TrailTypeDef = TypedDict(
    "TrailTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "HasInsightSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "ResourceType": str,
        "ResourceName": str,
    },
    total=False,
)

GetChannelRequestRequestTypeDef = TypedDict(
    "GetChannelRequestRequestTypeDef",
    {
        "Channel": str,
    },
)

IngestionStatusTypeDef = TypedDict(
    "IngestionStatusTypeDef",
    {
        "LatestIngestionSuccessTime": datetime,
        "LatestIngestionSuccessEventID": str,
        "LatestIngestionErrorCode": str,
        "LatestIngestionAttemptTime": datetime,
        "LatestIngestionAttemptEventID": str,
    },
    total=False,
)

GetEventDataStoreRequestRequestTypeDef = TypedDict(
    "GetEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

GetEventSelectorsRequestRequestTypeDef = TypedDict(
    "GetEventSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)

GetImportRequestRequestTypeDef = TypedDict(
    "GetImportRequestRequestTypeDef",
    {
        "ImportId": str,
    },
)

ImportStatisticsTypeDef = TypedDict(
    "ImportStatisticsTypeDef",
    {
        "PrefixesFound": int,
        "PrefixesCompleted": int,
        "FilesCompleted": int,
        "EventsCompleted": int,
        "FailedEntries": int,
    },
    total=False,
)

GetInsightSelectorsRequestRequestTypeDef = TypedDict(
    "GetInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)

InsightSelectorOutputTypeDef = TypedDict(
    "InsightSelectorOutputTypeDef",
    {
        "InsightType": InsightTypeType,
    },
    total=False,
)

_RequiredGetQueryResultsRequestRequestTypeDef = TypedDict(
    "_RequiredGetQueryResultsRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
_OptionalGetQueryResultsRequestRequestTypeDef = TypedDict(
    "_OptionalGetQueryResultsRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "NextToken": str,
        "MaxQueryResults": int,
    },
    total=False,
)

class GetQueryResultsRequestRequestTypeDef(
    _RequiredGetQueryResultsRequestRequestTypeDef, _OptionalGetQueryResultsRequestRequestTypeDef
):
    pass

QueryStatisticsTypeDef = TypedDict(
    "QueryStatisticsTypeDef",
    {
        "ResultsCount": int,
        "TotalResultsCount": int,
        "BytesScanned": int,
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
        "ResourceArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrailRequestRequestTypeDef = TypedDict(
    "GetTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetTrailStatusRequestRequestTypeDef = TypedDict(
    "GetTrailStatusRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetTrailStatusResponseTypeDef = TypedDict(
    "GetTrailStatusResponseTypeDef",
    {
        "IsLogging": bool,
        "LatestDeliveryError": str,
        "LatestNotificationError": str,
        "LatestDeliveryTime": datetime,
        "LatestNotificationTime": datetime,
        "StartLoggingTime": datetime,
        "StopLoggingTime": datetime,
        "LatestCloudWatchLogsDeliveryError": str,
        "LatestCloudWatchLogsDeliveryTime": datetime,
        "LatestDigestDeliveryTime": datetime,
        "LatestDigestDeliveryError": str,
        "LatestDeliveryAttemptTime": str,
        "LatestNotificationAttemptTime": str,
        "LatestNotificationAttemptSucceeded": str,
        "LatestDeliveryAttemptSucceeded": str,
        "TimeLoggingStarted": str,
        "TimeLoggingStopped": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportFailureListItemTypeDef = TypedDict(
    "ImportFailureListItemTypeDef",
    {
        "Location": str,
        "Status": ImportFailureStatusType,
        "ErrorType": str,
        "ErrorMessage": str,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

S3ImportSourceOutputTypeDef = TypedDict(
    "S3ImportSourceOutputTypeDef",
    {
        "S3LocationUri": str,
        "S3BucketRegion": str,
        "S3BucketAccessRoleArn": str,
    },
)

S3ImportSourceTypeDef = TypedDict(
    "S3ImportSourceTypeDef",
    {
        "S3LocationUri": str,
        "S3BucketRegion": str,
        "S3BucketAccessRoleArn": str,
    },
)

ImportsListItemTypeDef = TypedDict(
    "ImportsListItemTypeDef",
    {
        "ImportId": str,
        "ImportStatus": ImportStatusType,
        "Destinations": List[str],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

InsightSelectorTypeDef = TypedDict(
    "InsightSelectorTypeDef",
    {
        "InsightType": InsightTypeType,
    },
    total=False,
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListEventDataStoresRequestRequestTypeDef = TypedDict(
    "ListEventDataStoresRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListImportFailuresRequestListImportFailuresPaginateTypeDef = TypedDict(
    "_RequiredListImportFailuresRequestListImportFailuresPaginateTypeDef",
    {
        "ImportId": str,
    },
)
_OptionalListImportFailuresRequestListImportFailuresPaginateTypeDef = TypedDict(
    "_OptionalListImportFailuresRequestListImportFailuresPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListImportFailuresRequestListImportFailuresPaginateTypeDef(
    _RequiredListImportFailuresRequestListImportFailuresPaginateTypeDef,
    _OptionalListImportFailuresRequestListImportFailuresPaginateTypeDef,
):
    pass

_RequiredListImportFailuresRequestRequestTypeDef = TypedDict(
    "_RequiredListImportFailuresRequestRequestTypeDef",
    {
        "ImportId": str,
    },
)
_OptionalListImportFailuresRequestRequestTypeDef = TypedDict(
    "_OptionalListImportFailuresRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListImportFailuresRequestRequestTypeDef(
    _RequiredListImportFailuresRequestRequestTypeDef,
    _OptionalListImportFailuresRequestRequestTypeDef,
):
    pass

ListImportsRequestListImportsPaginateTypeDef = TypedDict(
    "ListImportsRequestListImportsPaginateTypeDef",
    {
        "Destination": str,
        "ImportStatus": ImportStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListImportsRequestRequestTypeDef = TypedDict(
    "ListImportsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "Destination": str,
        "ImportStatus": ImportStatusType,
        "NextToken": str,
    },
    total=False,
)

ListPublicKeysRequestListPublicKeysPaginateTypeDef = TypedDict(
    "ListPublicKeysRequestListPublicKeysPaginateTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
    },
    total=False,
)

PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)

_RequiredListQueriesRequestRequestTypeDef = TypedDict(
    "_RequiredListQueriesRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
_OptionalListQueriesRequestRequestTypeDef = TypedDict(
    "_OptionalListQueriesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "QueryStatus": QueryStatusType,
    },
    total=False,
)

class ListQueriesRequestRequestTypeDef(
    _RequiredListQueriesRequestRequestTypeDef, _OptionalListQueriesRequestRequestTypeDef
):
    pass

QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "QueryId": str,
        "QueryStatus": QueryStatusType,
        "CreationTime": datetime,
    },
    total=False,
)

_RequiredListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "_RequiredListTagsRequestListTagsPaginateTypeDef",
    {
        "ResourceIdList": Sequence[str],
    },
)
_OptionalListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "_OptionalListTagsRequestListTagsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListTagsRequestListTagsPaginateTypeDef(
    _RequiredListTagsRequestListTagsPaginateTypeDef, _OptionalListTagsRequestListTagsPaginateTypeDef
):
    pass

_RequiredListTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestRequestTypeDef",
    {
        "ResourceIdList": Sequence[str],
    },
)
_OptionalListTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsRequestRequestTypeDef(
    _RequiredListTagsRequestRequestTypeDef, _OptionalListTagsRequestRequestTypeDef
):
    pass

ListTrailsRequestListTrailsPaginateTypeDef = TypedDict(
    "ListTrailsRequestListTrailsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTrailsRequestRequestTypeDef = TypedDict(
    "ListTrailsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

TrailInfoTypeDef = TypedDict(
    "TrailInfoTypeDef",
    {
        "TrailARN": str,
        "Name": str,
        "HomeRegion": str,
    },
    total=False,
)

LookupAttributeTypeDef = TypedDict(
    "LookupAttributeTypeDef",
    {
        "AttributeKey": LookupAttributeKeyType,
        "AttributeValue": str,
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
        "ResourcePolicy": str,
    },
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterOrganizationDelegatedAdminRequestRequestTypeDef = TypedDict(
    "RegisterOrganizationDelegatedAdminRequestRequestTypeDef",
    {
        "MemberAccountId": str,
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

RestoreEventDataStoreRequestRequestTypeDef = TypedDict(
    "RestoreEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

StartEventDataStoreIngestionRequestRequestTypeDef = TypedDict(
    "StartEventDataStoreIngestionRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

StartLoggingRequestRequestTypeDef = TypedDict(
    "StartLoggingRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartQueryRequestRequestTypeDef = TypedDict(
    "StartQueryRequestRequestTypeDef",
    {
        "QueryStatement": str,
        "DeliveryS3Uri": str,
        "QueryAlias": str,
        "QueryParameters": Sequence[str],
    },
    total=False,
)

StartQueryResponseTypeDef = TypedDict(
    "StartQueryResponseTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEventDataStoreIngestionRequestRequestTypeDef = TypedDict(
    "StopEventDataStoreIngestionRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

StopImportRequestRequestTypeDef = TypedDict(
    "StopImportRequestRequestTypeDef",
    {
        "ImportId": str,
    },
)

StopLoggingRequestRequestTypeDef = TypedDict(
    "StopLoggingRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredUpdateTrailRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateTrailRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrailRequestRequestTypeDef",
    {
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "EnableLogFileValidation": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

class UpdateTrailRequestRequestTypeDef(
    _RequiredUpdateTrailRequestRequestTypeDef, _OptionalUpdateTrailRequestRequestTypeDef
):
    pass

UpdateTrailResponseTypeDef = TypedDict(
    "UpdateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsRequestRequestTypeDef = TypedDict(
    "AddTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagsList": Sequence[TagTypeDef],
    },
)

_RequiredCreateTrailRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrailRequestRequestTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
    },
)
_OptionalCreateTrailRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrailRequestRequestTypeDef",
    {
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "EnableLogFileValidation": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "TagsList": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateTrailRequestRequestTypeDef(
    _RequiredCreateTrailRequestRequestTypeDef, _OptionalCreateTrailRequestRequestTypeDef
):
    pass

RemoveTagsRequestRequestTypeDef = TypedDict(
    "RemoveTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagsList": Sequence[TagTypeDef],
    },
)

_RequiredAdvancedEventSelectorOutputTypeDef = TypedDict(
    "_RequiredAdvancedEventSelectorOutputTypeDef",
    {
        "FieldSelectors": List[AdvancedFieldSelectorOutputTypeDef],
    },
)
_OptionalAdvancedEventSelectorOutputTypeDef = TypedDict(
    "_OptionalAdvancedEventSelectorOutputTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class AdvancedEventSelectorOutputTypeDef(
    _RequiredAdvancedEventSelectorOutputTypeDef, _OptionalAdvancedEventSelectorOutputTypeDef
):
    pass

_RequiredAdvancedEventSelectorTypeDef = TypedDict(
    "_RequiredAdvancedEventSelectorTypeDef",
    {
        "FieldSelectors": Sequence[AdvancedFieldSelectorTypeDef],
    },
)
_OptionalAdvancedEventSelectorTypeDef = TypedDict(
    "_OptionalAdvancedEventSelectorTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class AdvancedEventSelectorTypeDef(
    _RequiredAdvancedEventSelectorTypeDef, _OptionalAdvancedEventSelectorTypeDef
):
    pass

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List[ChannelTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestRequestTypeDef",
    {
        "Name": str,
        "Source": str,
        "Destinations": Sequence[DestinationTypeDef],
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateChannelRequestRequestTypeDef(
    _RequiredCreateChannelRequestRequestTypeDef, _OptionalCreateChannelRequestRequestTypeDef
):
    pass

_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "Channel": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "Destinations": Sequence[DestinationTypeDef],
        "Name": str,
    },
    total=False,
)

class UpdateChannelRequestRequestTypeDef(
    _RequiredUpdateChannelRequestRequestTypeDef, _OptionalUpdateChannelRequestRequestTypeDef
):
    pass

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "Destinations": List[DestinationOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "Destinations": List[DestinationOutputTypeDef],
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "ResourceId": str,
        "TagsList": List[TagOutputTypeDef],
    },
    total=False,
)

EventSelectorOutputTypeDef = TypedDict(
    "EventSelectorOutputTypeDef",
    {
        "ReadWriteType": ReadWriteTypeType,
        "IncludeManagementEvents": bool,
        "DataResources": List[DataResourceOutputTypeDef],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

EventSelectorTypeDef = TypedDict(
    "EventSelectorTypeDef",
    {
        "ReadWriteType": ReadWriteTypeType,
        "IncludeManagementEvents": bool,
        "DataResources": Sequence[DataResourceTypeDef],
        "ExcludeManagementEventSources": Sequence[str],
    },
    total=False,
)

DescribeQueryResponseTypeDef = TypedDict(
    "DescribeQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryString": str,
        "QueryStatus": QueryStatusType,
        "QueryStatistics": QueryStatisticsForDescribeQueryTypeDef,
        "ErrorMessage": str,
        "DeliveryS3Uri": str,
        "DeliveryStatus": DeliveryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrailsResponseTypeDef = TypedDict(
    "DescribeTrailsResponseTypeDef",
    {
        "trailList": List[TrailTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrailResponseTypeDef = TypedDict(
    "GetTrailResponseTypeDef",
    {
        "Trail": TrailTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List[ResourceTypeDef],
        "CloudTrailEvent": str,
    },
    total=False,
)

GetInsightSelectorsResponseTypeDef = TypedDict(
    "GetInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[InsightSelectorOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInsightSelectorsResponseTypeDef = TypedDict(
    "PutInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[InsightSelectorOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryResultsResponseTypeDef = TypedDict(
    "GetQueryResultsResponseTypeDef",
    {
        "QueryStatus": QueryStatusType,
        "QueryStatistics": QueryStatisticsTypeDef,
        "QueryResultRows": List[List[Dict[str, str]]],
        "NextToken": str,
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportFailuresResponseTypeDef = TypedDict(
    "ListImportFailuresResponseTypeDef",
    {
        "Failures": List[ImportFailureListItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSourceOutputTypeDef = TypedDict(
    "ImportSourceOutputTypeDef",
    {
        "S3": S3ImportSourceOutputTypeDef,
    },
)

ImportSourceTypeDef = TypedDict(
    "ImportSourceTypeDef",
    {
        "S3": S3ImportSourceTypeDef,
    },
)

ListImportsResponseTypeDef = TypedDict(
    "ListImportsResponseTypeDef",
    {
        "Imports": List[ImportsListItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInsightSelectorsRequestRequestTypeDef = TypedDict(
    "PutInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
        "InsightSelectors": Sequence[InsightSelectorTypeDef],
    },
)

ListPublicKeysResponseTypeDef = TypedDict(
    "ListPublicKeysResponseTypeDef",
    {
        "PublicKeyList": List[PublicKeyTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueriesResponseTypeDef = TypedDict(
    "ListQueriesResponseTypeDef",
    {
        "Queries": List[QueryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrailsResponseTypeDef = TypedDict(
    "ListTrailsResponseTypeDef",
    {
        "Trails": List[TrailInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LookupEventsRequestLookupEventsPaginateTypeDef = TypedDict(
    "LookupEventsRequestLookupEventsPaginateTypeDef",
    {
        "LookupAttributes": Sequence[LookupAttributeTypeDef],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "EventCategory": Literal["insight"],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

LookupEventsRequestRequestTypeDef = TypedDict(
    "LookupEventsRequestRequestTypeDef",
    {
        "LookupAttributes": Sequence[LookupAttributeTypeDef],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "EventCategory": Literal["insight"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

CreateEventDataStoreResponseTypeDef = TypedDict(
    "CreateEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "TagsList": List[TagOutputTypeDef],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventDataStoreTypeDef = TypedDict(
    "EventDataStoreTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "TerminationProtectionEnabled": bool,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

GetEventDataStoreResponseTypeDef = TypedDict(
    "GetEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreEventDataStoreResponseTypeDef = TypedDict(
    "RestoreEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {
        "ApplyToAllRegions": bool,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
    },
    total=False,
)

UpdateEventDataStoreResponseTypeDef = TypedDict(
    "UpdateEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventDataStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventDataStoreRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateEventDataStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventDataStoreRequestRequestTypeDef",
    {
        "AdvancedEventSelectors": Sequence[AdvancedEventSelectorTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "TagsList": Sequence[TagTypeDef],
        "KmsKeyId": str,
        "StartIngestion": bool,
    },
    total=False,
)

class CreateEventDataStoreRequestRequestTypeDef(
    _RequiredCreateEventDataStoreRequestRequestTypeDef,
    _OptionalCreateEventDataStoreRequestRequestTypeDef,
):
    pass

_RequiredUpdateEventDataStoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
_OptionalUpdateEventDataStoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventDataStoreRequestRequestTypeDef",
    {
        "Name": str,
        "AdvancedEventSelectors": Sequence[AdvancedEventSelectorTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

class UpdateEventDataStoreRequestRequestTypeDef(
    _RequiredUpdateEventDataStoreRequestRequestTypeDef,
    _OptionalUpdateEventDataStoreRequestRequestTypeDef,
):
    pass

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "ResourceTagList": List[ResourceTagTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventSelectorsResponseTypeDef = TypedDict(
    "GetEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List[EventSelectorOutputTypeDef],
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEventSelectorsResponseTypeDef = TypedDict(
    "PutEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List[EventSelectorOutputTypeDef],
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutEventSelectorsRequestRequestTypeDef = TypedDict(
    "_RequiredPutEventSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)
_OptionalPutEventSelectorsRequestRequestTypeDef = TypedDict(
    "_OptionalPutEventSelectorsRequestRequestTypeDef",
    {
        "EventSelectors": Sequence[EventSelectorTypeDef],
        "AdvancedEventSelectors": Sequence[AdvancedEventSelectorTypeDef],
    },
    total=False,
)

class PutEventSelectorsRequestRequestTypeDef(
    _RequiredPutEventSelectorsRequestRequestTypeDef, _OptionalPutEventSelectorsRequestRequestTypeDef
):
    pass

LookupEventsResponseTypeDef = TypedDict(
    "LookupEventsResponseTypeDef",
    {
        "Events": List[EventTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportResponseTypeDef = TypedDict(
    "GetImportResponseTypeDef",
    {
        "ImportId": str,
        "Destinations": List[str],
        "ImportSource": ImportSourceOutputTypeDef,
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ImportStatistics": ImportStatisticsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "ImportId": str,
        "Destinations": List[str],
        "ImportSource": ImportSourceOutputTypeDef,
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopImportResponseTypeDef = TypedDict(
    "StopImportResponseTypeDef",
    {
        "ImportId": str,
        "ImportSource": ImportSourceOutputTypeDef,
        "Destinations": List[str],
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatistics": ImportStatisticsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportRequestRequestTypeDef = TypedDict(
    "StartImportRequestRequestTypeDef",
    {
        "Destinations": Sequence[str],
        "ImportSource": ImportSourceTypeDef,
        "StartEventTime": Union[datetime, str],
        "EndEventTime": Union[datetime, str],
        "ImportId": str,
    },
    total=False,
)

ListEventDataStoresResponseTypeDef = TypedDict(
    "ListEventDataStoresResponseTypeDef",
    {
        "EventDataStores": List[EventDataStoreTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelResponseTypeDef = TypedDict(
    "GetChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "SourceConfig": SourceConfigTypeDef,
        "Destinations": List[DestinationOutputTypeDef],
        "IngestionStatus": IngestionStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
