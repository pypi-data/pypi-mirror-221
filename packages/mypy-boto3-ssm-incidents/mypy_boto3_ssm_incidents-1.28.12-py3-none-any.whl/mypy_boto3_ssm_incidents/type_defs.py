"""
Type annotations for ssm-incidents service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/type_defs/)

Usage::

    ```python
    from mypy_boto3_ssm_incidents.type_defs import AddRegionActionTypeDef

    data: AddRegionActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    IncidentRecordStatusType,
    ItemTypeType,
    RegionStatusType,
    ReplicationSetStatusType,
    SortOrderType,
    SsmTargetAccountType,
    VariableTypeType,
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
    "AddRegionActionTypeDef",
    "AttributeValueListTypeDef",
    "AutomationExecutionTypeDef",
    "ChatChannelOutputTypeDef",
    "ChatChannelTypeDef",
    "RegionMapInputValueTypeDef",
    "ResponseMetadataTypeDef",
    "EventReferenceTypeDef",
    "DeleteIncidentRecordInputRequestTypeDef",
    "DeleteRegionActionTypeDef",
    "DeleteReplicationSetInputRequestTypeDef",
    "DeleteResourcePolicyInputRequestTypeDef",
    "DeleteResponsePlanInputRequestTypeDef",
    "DeleteTimelineEventInputRequestTypeDef",
    "DynamicSsmParameterValueOutputTypeDef",
    "DynamicSsmParameterValueTypeDef",
    "EventReferenceOutputTypeDef",
    "GetIncidentRecordInputRequestTypeDef",
    "GetReplicationSetInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "PaginatorConfigTypeDef",
    "GetResourcePoliciesInputRequestTypeDef",
    "ResourcePolicyTypeDef",
    "GetResponsePlanInputRequestTypeDef",
    "GetTimelineEventInputRequestTypeDef",
    "IncidentRecordSourceTypeDef",
    "NotificationTargetItemOutputTypeDef",
    "NotificationTargetItemTypeDef",
    "PagerDutyIncidentDetailOutputTypeDef",
    "PagerDutyIncidentDetailTypeDef",
    "ListRelatedItemsInputRequestTypeDef",
    "ListReplicationSetsInputRequestTypeDef",
    "ListResponsePlansInputRequestTypeDef",
    "ResponsePlanSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PagerDutyIncidentConfigurationOutputTypeDef",
    "PagerDutyIncidentConfigurationTypeDef",
    "PutResourcePolicyInputRequestTypeDef",
    "RegionInfoTypeDef",
    "TriggerDetailsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeletionProtectionInputRequestTypeDef",
    "ConditionTypeDef",
    "CreateReplicationSetInputRequestTypeDef",
    "CreateReplicationSetOutputTypeDef",
    "CreateResponsePlanOutputTypeDef",
    "CreateTimelineEventOutputTypeDef",
    "ListReplicationSetsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "StartIncidentOutputTypeDef",
    "CreateTimelineEventInputRequestTypeDef",
    "UpdateTimelineEventInputRequestTypeDef",
    "UpdateReplicationSetActionTypeDef",
    "SsmAutomationOutputTypeDef",
    "SsmAutomationTypeDef",
    "EventSummaryTypeDef",
    "TimelineEventTypeDef",
    "GetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef",
    "GetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef",
    "GetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef",
    "ListRelatedItemsInputListRelatedItemsPaginateTypeDef",
    "ListReplicationSetsInputListReplicationSetsPaginateTypeDef",
    "ListResponsePlansInputListResponsePlansPaginateTypeDef",
    "GetResourcePoliciesOutputTypeDef",
    "IncidentRecordSummaryTypeDef",
    "IncidentRecordTypeDef",
    "IncidentTemplateOutputTypeDef",
    "IncidentTemplateTypeDef",
    "UpdateIncidentRecordInputRequestTypeDef",
    "ItemValueOutputTypeDef",
    "ItemValueTypeDef",
    "ListResponsePlansOutputTypeDef",
    "PagerDutyConfigurationOutputTypeDef",
    "PagerDutyConfigurationTypeDef",
    "ReplicationSetTypeDef",
    "FilterTypeDef",
    "UpdateReplicationSetInputRequestTypeDef",
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "ListTimelineEventsOutputTypeDef",
    "GetTimelineEventOutputTypeDef",
    "ListIncidentRecordsOutputTypeDef",
    "GetIncidentRecordOutputTypeDef",
    "ItemIdentifierOutputTypeDef",
    "ItemIdentifierTypeDef",
    "IntegrationOutputTypeDef",
    "IntegrationTypeDef",
    "GetReplicationSetOutputTypeDef",
    "ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef",
    "ListIncidentRecordsInputRequestTypeDef",
    "ListTimelineEventsInputListTimelineEventsPaginateTypeDef",
    "ListTimelineEventsInputRequestTypeDef",
    "RelatedItemOutputTypeDef",
    "RelatedItemTypeDef",
    "GetResponsePlanOutputTypeDef",
    "CreateResponsePlanInputRequestTypeDef",
    "UpdateResponsePlanInputRequestTypeDef",
    "ListRelatedItemsOutputTypeDef",
    "RelatedItemsUpdateTypeDef",
    "StartIncidentInputRequestTypeDef",
    "UpdateRelatedItemsInputRequestTypeDef",
)

_RequiredAddRegionActionTypeDef = TypedDict(
    "_RequiredAddRegionActionTypeDef",
    {
        "regionName": str,
    },
)
_OptionalAddRegionActionTypeDef = TypedDict(
    "_OptionalAddRegionActionTypeDef",
    {
        "sseKmsKeyId": str,
    },
    total=False,
)


class AddRegionActionTypeDef(_RequiredAddRegionActionTypeDef, _OptionalAddRegionActionTypeDef):
    pass


AttributeValueListTypeDef = TypedDict(
    "AttributeValueListTypeDef",
    {
        "integerValues": Sequence[int],
        "stringValues": Sequence[str],
    },
    total=False,
)

AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "ssmExecutionArn": str,
    },
    total=False,
)

ChatChannelOutputTypeDef = TypedDict(
    "ChatChannelOutputTypeDef",
    {
        "chatbotSns": List[str],
        "empty": Dict[str, Any],
    },
    total=False,
)

ChatChannelTypeDef = TypedDict(
    "ChatChannelTypeDef",
    {
        "chatbotSns": Sequence[str],
        "empty": Mapping[str, Any],
    },
    total=False,
)

RegionMapInputValueTypeDef = TypedDict(
    "RegionMapInputValueTypeDef",
    {
        "sseKmsKeyId": str,
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

EventReferenceTypeDef = TypedDict(
    "EventReferenceTypeDef",
    {
        "relatedItemId": str,
        "resource": str,
    },
    total=False,
)

DeleteIncidentRecordInputRequestTypeDef = TypedDict(
    "DeleteIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRegionActionTypeDef = TypedDict(
    "DeleteRegionActionTypeDef",
    {
        "regionName": str,
    },
)

DeleteReplicationSetInputRequestTypeDef = TypedDict(
    "DeleteReplicationSetInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteResourcePolicyInputRequestTypeDef = TypedDict(
    "DeleteResourcePolicyInputRequestTypeDef",
    {
        "policyId": str,
        "resourceArn": str,
    },
)

DeleteResponsePlanInputRequestTypeDef = TypedDict(
    "DeleteResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTimelineEventInputRequestTypeDef = TypedDict(
    "DeleteTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)

DynamicSsmParameterValueOutputTypeDef = TypedDict(
    "DynamicSsmParameterValueOutputTypeDef",
    {
        "variable": VariableTypeType,
    },
    total=False,
)

DynamicSsmParameterValueTypeDef = TypedDict(
    "DynamicSsmParameterValueTypeDef",
    {
        "variable": VariableTypeType,
    },
    total=False,
)

EventReferenceOutputTypeDef = TypedDict(
    "EventReferenceOutputTypeDef",
    {
        "relatedItemId": str,
        "resource": str,
    },
    total=False,
)

GetIncidentRecordInputRequestTypeDef = TypedDict(
    "GetIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetReplicationSetInputRequestTypeDef = TypedDict(
    "GetReplicationSetInputRequestTypeDef",
    {
        "arn": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
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

_RequiredGetResourcePoliciesInputRequestTypeDef = TypedDict(
    "_RequiredGetResourcePoliciesInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalGetResourcePoliciesInputRequestTypeDef = TypedDict(
    "_OptionalGetResourcePoliciesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class GetResourcePoliciesInputRequestTypeDef(
    _RequiredGetResourcePoliciesInputRequestTypeDef, _OptionalGetResourcePoliciesInputRequestTypeDef
):
    pass


ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policyDocument": str,
        "policyId": str,
        "ramResourceShareRegion": str,
    },
)

GetResponsePlanInputRequestTypeDef = TypedDict(
    "GetResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetTimelineEventInputRequestTypeDef = TypedDict(
    "GetTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)

_RequiredIncidentRecordSourceTypeDef = TypedDict(
    "_RequiredIncidentRecordSourceTypeDef",
    {
        "createdBy": str,
        "source": str,
    },
)
_OptionalIncidentRecordSourceTypeDef = TypedDict(
    "_OptionalIncidentRecordSourceTypeDef",
    {
        "invokedBy": str,
        "resourceArn": str,
    },
    total=False,
)


class IncidentRecordSourceTypeDef(
    _RequiredIncidentRecordSourceTypeDef, _OptionalIncidentRecordSourceTypeDef
):
    pass


NotificationTargetItemOutputTypeDef = TypedDict(
    "NotificationTargetItemOutputTypeDef",
    {
        "snsTopicArn": str,
    },
    total=False,
)

NotificationTargetItemTypeDef = TypedDict(
    "NotificationTargetItemTypeDef",
    {
        "snsTopicArn": str,
    },
    total=False,
)

_RequiredPagerDutyIncidentDetailOutputTypeDef = TypedDict(
    "_RequiredPagerDutyIncidentDetailOutputTypeDef",
    {
        "id": str,
    },
)
_OptionalPagerDutyIncidentDetailOutputTypeDef = TypedDict(
    "_OptionalPagerDutyIncidentDetailOutputTypeDef",
    {
        "autoResolve": bool,
        "secretId": str,
    },
    total=False,
)


class PagerDutyIncidentDetailOutputTypeDef(
    _RequiredPagerDutyIncidentDetailOutputTypeDef, _OptionalPagerDutyIncidentDetailOutputTypeDef
):
    pass


_RequiredPagerDutyIncidentDetailTypeDef = TypedDict(
    "_RequiredPagerDutyIncidentDetailTypeDef",
    {
        "id": str,
    },
)
_OptionalPagerDutyIncidentDetailTypeDef = TypedDict(
    "_OptionalPagerDutyIncidentDetailTypeDef",
    {
        "autoResolve": bool,
        "secretId": str,
    },
    total=False,
)


class PagerDutyIncidentDetailTypeDef(
    _RequiredPagerDutyIncidentDetailTypeDef, _OptionalPagerDutyIncidentDetailTypeDef
):
    pass


_RequiredListRelatedItemsInputRequestTypeDef = TypedDict(
    "_RequiredListRelatedItemsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
    },
)
_OptionalListRelatedItemsInputRequestTypeDef = TypedDict(
    "_OptionalListRelatedItemsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListRelatedItemsInputRequestTypeDef(
    _RequiredListRelatedItemsInputRequestTypeDef, _OptionalListRelatedItemsInputRequestTypeDef
):
    pass


ListReplicationSetsInputRequestTypeDef = TypedDict(
    "ListReplicationSetsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListResponsePlansInputRequestTypeDef = TypedDict(
    "ListResponsePlansInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredResponsePlanSummaryTypeDef = TypedDict(
    "_RequiredResponsePlanSummaryTypeDef",
    {
        "arn": str,
        "name": str,
    },
)
_OptionalResponsePlanSummaryTypeDef = TypedDict(
    "_OptionalResponsePlanSummaryTypeDef",
    {
        "displayName": str,
    },
    total=False,
)


class ResponsePlanSummaryTypeDef(
    _RequiredResponsePlanSummaryTypeDef, _OptionalResponsePlanSummaryTypeDef
):
    pass


ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

PagerDutyIncidentConfigurationOutputTypeDef = TypedDict(
    "PagerDutyIncidentConfigurationOutputTypeDef",
    {
        "serviceId": str,
    },
)

PagerDutyIncidentConfigurationTypeDef = TypedDict(
    "PagerDutyIncidentConfigurationTypeDef",
    {
        "serviceId": str,
    },
)

PutResourcePolicyInputRequestTypeDef = TypedDict(
    "PutResourcePolicyInputRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

_RequiredRegionInfoTypeDef = TypedDict(
    "_RequiredRegionInfoTypeDef",
    {
        "status": RegionStatusType,
        "statusUpdateDateTime": datetime,
    },
)
_OptionalRegionInfoTypeDef = TypedDict(
    "_OptionalRegionInfoTypeDef",
    {
        "sseKmsKeyId": str,
        "statusMessage": str,
    },
    total=False,
)


class RegionInfoTypeDef(_RequiredRegionInfoTypeDef, _OptionalRegionInfoTypeDef):
    pass


_RequiredTriggerDetailsTypeDef = TypedDict(
    "_RequiredTriggerDetailsTypeDef",
    {
        "source": str,
        "timestamp": Union[datetime, str],
    },
)
_OptionalTriggerDetailsTypeDef = TypedDict(
    "_OptionalTriggerDetailsTypeDef",
    {
        "rawData": str,
        "triggerArn": str,
    },
    total=False,
)


class TriggerDetailsTypeDef(_RequiredTriggerDetailsTypeDef, _OptionalTriggerDetailsTypeDef):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateDeletionProtectionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDeletionProtectionInputRequestTypeDef",
    {
        "arn": str,
        "deletionProtected": bool,
    },
)
_OptionalUpdateDeletionProtectionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDeletionProtectionInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateDeletionProtectionInputRequestTypeDef(
    _RequiredUpdateDeletionProtectionInputRequestTypeDef,
    _OptionalUpdateDeletionProtectionInputRequestTypeDef,
):
    pass


ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "after": Union[datetime, str],
        "before": Union[datetime, str],
        "equals": AttributeValueListTypeDef,
    },
    total=False,
)

_RequiredCreateReplicationSetInputRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationSetInputRequestTypeDef",
    {
        "regions": Mapping[str, RegionMapInputValueTypeDef],
    },
)
_OptionalCreateReplicationSetInputRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationSetInputRequestTypeDef",
    {
        "clientToken": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateReplicationSetInputRequestTypeDef(
    _RequiredCreateReplicationSetInputRequestTypeDef,
    _OptionalCreateReplicationSetInputRequestTypeDef,
):
    pass


CreateReplicationSetOutputTypeDef = TypedDict(
    "CreateReplicationSetOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateResponsePlanOutputTypeDef = TypedDict(
    "CreateResponsePlanOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTimelineEventOutputTypeDef = TypedDict(
    "CreateTimelineEventOutputTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListReplicationSetsOutputTypeDef = TypedDict(
    "ListReplicationSetsOutputTypeDef",
    {
        "nextToken": str,
        "replicationSetArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
    {
        "policyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartIncidentOutputTypeDef = TypedDict(
    "StartIncidentOutputTypeDef",
    {
        "incidentRecordArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateTimelineEventInputRequestTypeDef = TypedDict(
    "_RequiredCreateTimelineEventInputRequestTypeDef",
    {
        "eventData": str,
        "eventTime": Union[datetime, str],
        "eventType": str,
        "incidentRecordArn": str,
    },
)
_OptionalCreateTimelineEventInputRequestTypeDef = TypedDict(
    "_OptionalCreateTimelineEventInputRequestTypeDef",
    {
        "clientToken": str,
        "eventReferences": Sequence[EventReferenceTypeDef],
    },
    total=False,
)


class CreateTimelineEventInputRequestTypeDef(
    _RequiredCreateTimelineEventInputRequestTypeDef, _OptionalCreateTimelineEventInputRequestTypeDef
):
    pass


_RequiredUpdateTimelineEventInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)
_OptionalUpdateTimelineEventInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTimelineEventInputRequestTypeDef",
    {
        "clientToken": str,
        "eventData": str,
        "eventReferences": Sequence[EventReferenceTypeDef],
        "eventTime": Union[datetime, str],
        "eventType": str,
    },
    total=False,
)


class UpdateTimelineEventInputRequestTypeDef(
    _RequiredUpdateTimelineEventInputRequestTypeDef, _OptionalUpdateTimelineEventInputRequestTypeDef
):
    pass


UpdateReplicationSetActionTypeDef = TypedDict(
    "UpdateReplicationSetActionTypeDef",
    {
        "addRegionAction": AddRegionActionTypeDef,
        "deleteRegionAction": DeleteRegionActionTypeDef,
    },
    total=False,
)

_RequiredSsmAutomationOutputTypeDef = TypedDict(
    "_RequiredSsmAutomationOutputTypeDef",
    {
        "documentName": str,
        "roleArn": str,
    },
)
_OptionalSsmAutomationOutputTypeDef = TypedDict(
    "_OptionalSsmAutomationOutputTypeDef",
    {
        "documentVersion": str,
        "dynamicParameters": Dict[str, DynamicSsmParameterValueOutputTypeDef],
        "parameters": Dict[str, List[str]],
        "targetAccount": SsmTargetAccountType,
    },
    total=False,
)


class SsmAutomationOutputTypeDef(
    _RequiredSsmAutomationOutputTypeDef, _OptionalSsmAutomationOutputTypeDef
):
    pass


_RequiredSsmAutomationTypeDef = TypedDict(
    "_RequiredSsmAutomationTypeDef",
    {
        "documentName": str,
        "roleArn": str,
    },
)
_OptionalSsmAutomationTypeDef = TypedDict(
    "_OptionalSsmAutomationTypeDef",
    {
        "documentVersion": str,
        "dynamicParameters": Mapping[str, DynamicSsmParameterValueTypeDef],
        "parameters": Mapping[str, Sequence[str]],
        "targetAccount": SsmTargetAccountType,
    },
    total=False,
)


class SsmAutomationTypeDef(_RequiredSsmAutomationTypeDef, _OptionalSsmAutomationTypeDef):
    pass


_RequiredEventSummaryTypeDef = TypedDict(
    "_RequiredEventSummaryTypeDef",
    {
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
    },
)
_OptionalEventSummaryTypeDef = TypedDict(
    "_OptionalEventSummaryTypeDef",
    {
        "eventReferences": List[EventReferenceOutputTypeDef],
    },
    total=False,
)


class EventSummaryTypeDef(_RequiredEventSummaryTypeDef, _OptionalEventSummaryTypeDef):
    pass


_RequiredTimelineEventTypeDef = TypedDict(
    "_RequiredTimelineEventTypeDef",
    {
        "eventData": str,
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
    },
)
_OptionalTimelineEventTypeDef = TypedDict(
    "_OptionalTimelineEventTypeDef",
    {
        "eventReferences": List[EventReferenceOutputTypeDef],
    },
    total=False,
)


class TimelineEventTypeDef(_RequiredTimelineEventTypeDef, _OptionalTimelineEventTypeDef):
    pass


_RequiredGetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef = TypedDict(
    "_RequiredGetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef",
    {
        "arn": str,
    },
)
_OptionalGetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef = TypedDict(
    "_OptionalGetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class GetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef(
    _RequiredGetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef,
    _OptionalGetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef,
):
    pass


_RequiredGetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef = TypedDict(
    "_RequiredGetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef",
    {
        "arn": str,
    },
)
_OptionalGetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef = TypedDict(
    "_OptionalGetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class GetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef(
    _RequiredGetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef,
    _OptionalGetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef,
):
    pass


_RequiredGetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef = TypedDict(
    "_RequiredGetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalGetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef = TypedDict(
    "_OptionalGetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef(
    _RequiredGetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef,
    _OptionalGetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef,
):
    pass


_RequiredListRelatedItemsInputListRelatedItemsPaginateTypeDef = TypedDict(
    "_RequiredListRelatedItemsInputListRelatedItemsPaginateTypeDef",
    {
        "incidentRecordArn": str,
    },
)
_OptionalListRelatedItemsInputListRelatedItemsPaginateTypeDef = TypedDict(
    "_OptionalListRelatedItemsInputListRelatedItemsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListRelatedItemsInputListRelatedItemsPaginateTypeDef(
    _RequiredListRelatedItemsInputListRelatedItemsPaginateTypeDef,
    _OptionalListRelatedItemsInputListRelatedItemsPaginateTypeDef,
):
    pass


ListReplicationSetsInputListReplicationSetsPaginateTypeDef = TypedDict(
    "ListReplicationSetsInputListReplicationSetsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListResponsePlansInputListResponsePlansPaginateTypeDef = TypedDict(
    "ListResponsePlansInputListResponsePlansPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetResourcePoliciesOutputTypeDef = TypedDict(
    "GetResourcePoliciesOutputTypeDef",
    {
        "nextToken": str,
        "resourcePolicies": List[ResourcePolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredIncidentRecordSummaryTypeDef = TypedDict(
    "_RequiredIncidentRecordSummaryTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "impact": int,
        "incidentRecordSource": IncidentRecordSourceTypeDef,
        "status": IncidentRecordStatusType,
        "title": str,
    },
)
_OptionalIncidentRecordSummaryTypeDef = TypedDict(
    "_OptionalIncidentRecordSummaryTypeDef",
    {
        "resolvedTime": datetime,
    },
    total=False,
)


class IncidentRecordSummaryTypeDef(
    _RequiredIncidentRecordSummaryTypeDef, _OptionalIncidentRecordSummaryTypeDef
):
    pass


_RequiredIncidentRecordTypeDef = TypedDict(
    "_RequiredIncidentRecordTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "dedupeString": str,
        "impact": int,
        "incidentRecordSource": IncidentRecordSourceTypeDef,
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "status": IncidentRecordStatusType,
        "title": str,
    },
)
_OptionalIncidentRecordTypeDef = TypedDict(
    "_OptionalIncidentRecordTypeDef",
    {
        "automationExecutions": List[AutomationExecutionTypeDef],
        "chatChannel": ChatChannelOutputTypeDef,
        "notificationTargets": List[NotificationTargetItemOutputTypeDef],
        "resolvedTime": datetime,
        "summary": str,
    },
    total=False,
)


class IncidentRecordTypeDef(_RequiredIncidentRecordTypeDef, _OptionalIncidentRecordTypeDef):
    pass


_RequiredIncidentTemplateOutputTypeDef = TypedDict(
    "_RequiredIncidentTemplateOutputTypeDef",
    {
        "impact": int,
        "title": str,
    },
)
_OptionalIncidentTemplateOutputTypeDef = TypedDict(
    "_OptionalIncidentTemplateOutputTypeDef",
    {
        "dedupeString": str,
        "incidentTags": Dict[str, str],
        "notificationTargets": List[NotificationTargetItemOutputTypeDef],
        "summary": str,
    },
    total=False,
)


class IncidentTemplateOutputTypeDef(
    _RequiredIncidentTemplateOutputTypeDef, _OptionalIncidentTemplateOutputTypeDef
):
    pass


_RequiredIncidentTemplateTypeDef = TypedDict(
    "_RequiredIncidentTemplateTypeDef",
    {
        "impact": int,
        "title": str,
    },
)
_OptionalIncidentTemplateTypeDef = TypedDict(
    "_OptionalIncidentTemplateTypeDef",
    {
        "dedupeString": str,
        "incidentTags": Mapping[str, str],
        "notificationTargets": Sequence[NotificationTargetItemTypeDef],
        "summary": str,
    },
    total=False,
)


class IncidentTemplateTypeDef(_RequiredIncidentTemplateTypeDef, _OptionalIncidentTemplateTypeDef):
    pass


_RequiredUpdateIncidentRecordInputRequestTypeDef = TypedDict(
    "_RequiredUpdateIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateIncidentRecordInputRequestTypeDef = TypedDict(
    "_OptionalUpdateIncidentRecordInputRequestTypeDef",
    {
        "chatChannel": ChatChannelTypeDef,
        "clientToken": str,
        "impact": int,
        "notificationTargets": Sequence[NotificationTargetItemTypeDef],
        "status": IncidentRecordStatusType,
        "summary": str,
        "title": str,
    },
    total=False,
)


class UpdateIncidentRecordInputRequestTypeDef(
    _RequiredUpdateIncidentRecordInputRequestTypeDef,
    _OptionalUpdateIncidentRecordInputRequestTypeDef,
):
    pass


ItemValueOutputTypeDef = TypedDict(
    "ItemValueOutputTypeDef",
    {
        "arn": str,
        "metricDefinition": str,
        "pagerDutyIncidentDetail": PagerDutyIncidentDetailOutputTypeDef,
        "url": str,
    },
    total=False,
)

ItemValueTypeDef = TypedDict(
    "ItemValueTypeDef",
    {
        "arn": str,
        "metricDefinition": str,
        "pagerDutyIncidentDetail": PagerDutyIncidentDetailTypeDef,
        "url": str,
    },
    total=False,
)

ListResponsePlansOutputTypeDef = TypedDict(
    "ListResponsePlansOutputTypeDef",
    {
        "nextToken": str,
        "responsePlanSummaries": List[ResponsePlanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PagerDutyConfigurationOutputTypeDef = TypedDict(
    "PagerDutyConfigurationOutputTypeDef",
    {
        "name": str,
        "pagerDutyIncidentConfiguration": PagerDutyIncidentConfigurationOutputTypeDef,
        "secretId": str,
    },
)

PagerDutyConfigurationTypeDef = TypedDict(
    "PagerDutyConfigurationTypeDef",
    {
        "name": str,
        "pagerDutyIncidentConfiguration": PagerDutyIncidentConfigurationTypeDef,
        "secretId": str,
    },
)

_RequiredReplicationSetTypeDef = TypedDict(
    "_RequiredReplicationSetTypeDef",
    {
        "createdBy": str,
        "createdTime": datetime,
        "deletionProtected": bool,
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "regionMap": Dict[str, RegionInfoTypeDef],
        "status": ReplicationSetStatusType,
    },
)
_OptionalReplicationSetTypeDef = TypedDict(
    "_OptionalReplicationSetTypeDef",
    {
        "arn": str,
    },
    total=False,
)


class ReplicationSetTypeDef(_RequiredReplicationSetTypeDef, _OptionalReplicationSetTypeDef):
    pass


FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "condition": ConditionTypeDef,
        "key": str,
    },
)

_RequiredUpdateReplicationSetInputRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationSetInputRequestTypeDef",
    {
        "actions": Sequence[UpdateReplicationSetActionTypeDef],
        "arn": str,
    },
)
_OptionalUpdateReplicationSetInputRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationSetInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateReplicationSetInputRequestTypeDef(
    _RequiredUpdateReplicationSetInputRequestTypeDef,
    _OptionalUpdateReplicationSetInputRequestTypeDef,
):
    pass


ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "ssmAutomation": SsmAutomationOutputTypeDef,
    },
    total=False,
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ssmAutomation": SsmAutomationTypeDef,
    },
    total=False,
)

ListTimelineEventsOutputTypeDef = TypedDict(
    "ListTimelineEventsOutputTypeDef",
    {
        "eventSummaries": List[EventSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetTimelineEventOutputTypeDef = TypedDict(
    "GetTimelineEventOutputTypeDef",
    {
        "event": TimelineEventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListIncidentRecordsOutputTypeDef = TypedDict(
    "ListIncidentRecordsOutputTypeDef",
    {
        "incidentRecordSummaries": List[IncidentRecordSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetIncidentRecordOutputTypeDef = TypedDict(
    "GetIncidentRecordOutputTypeDef",
    {
        "incidentRecord": IncidentRecordTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ItemIdentifierOutputTypeDef = TypedDict(
    "ItemIdentifierOutputTypeDef",
    {
        "type": ItemTypeType,
        "value": ItemValueOutputTypeDef,
    },
)

ItemIdentifierTypeDef = TypedDict(
    "ItemIdentifierTypeDef",
    {
        "type": ItemTypeType,
        "value": ItemValueTypeDef,
    },
)

IntegrationOutputTypeDef = TypedDict(
    "IntegrationOutputTypeDef",
    {
        "pagerDutyConfiguration": PagerDutyConfigurationOutputTypeDef,
    },
    total=False,
)

IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "pagerDutyConfiguration": PagerDutyConfigurationTypeDef,
    },
    total=False,
)

GetReplicationSetOutputTypeDef = TypedDict(
    "GetReplicationSetOutputTypeDef",
    {
        "replicationSet": ReplicationSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef = TypedDict(
    "ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListIncidentRecordsInputRequestTypeDef = TypedDict(
    "ListIncidentRecordsInputRequestTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListTimelineEventsInputListTimelineEventsPaginateTypeDef = TypedDict(
    "_RequiredListTimelineEventsInputListTimelineEventsPaginateTypeDef",
    {
        "incidentRecordArn": str,
    },
)
_OptionalListTimelineEventsInputListTimelineEventsPaginateTypeDef = TypedDict(
    "_OptionalListTimelineEventsInputListTimelineEventsPaginateTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "sortBy": Literal["EVENT_TIME"],
        "sortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTimelineEventsInputListTimelineEventsPaginateTypeDef(
    _RequiredListTimelineEventsInputListTimelineEventsPaginateTypeDef,
    _OptionalListTimelineEventsInputListTimelineEventsPaginateTypeDef,
):
    pass


_RequiredListTimelineEventsInputRequestTypeDef = TypedDict(
    "_RequiredListTimelineEventsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
    },
)
_OptionalListTimelineEventsInputRequestTypeDef = TypedDict(
    "_OptionalListTimelineEventsInputRequestTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
        "sortBy": Literal["EVENT_TIME"],
        "sortOrder": SortOrderType,
    },
    total=False,
)


class ListTimelineEventsInputRequestTypeDef(
    _RequiredListTimelineEventsInputRequestTypeDef, _OptionalListTimelineEventsInputRequestTypeDef
):
    pass


_RequiredRelatedItemOutputTypeDef = TypedDict(
    "_RequiredRelatedItemOutputTypeDef",
    {
        "identifier": ItemIdentifierOutputTypeDef,
    },
)
_OptionalRelatedItemOutputTypeDef = TypedDict(
    "_OptionalRelatedItemOutputTypeDef",
    {
        "generatedId": str,
        "title": str,
    },
    total=False,
)


class RelatedItemOutputTypeDef(
    _RequiredRelatedItemOutputTypeDef, _OptionalRelatedItemOutputTypeDef
):
    pass


_RequiredRelatedItemTypeDef = TypedDict(
    "_RequiredRelatedItemTypeDef",
    {
        "identifier": ItemIdentifierTypeDef,
    },
)
_OptionalRelatedItemTypeDef = TypedDict(
    "_OptionalRelatedItemTypeDef",
    {
        "generatedId": str,
        "title": str,
    },
    total=False,
)


class RelatedItemTypeDef(_RequiredRelatedItemTypeDef, _OptionalRelatedItemTypeDef):
    pass


GetResponsePlanOutputTypeDef = TypedDict(
    "GetResponsePlanOutputTypeDef",
    {
        "actions": List[ActionOutputTypeDef],
        "arn": str,
        "chatChannel": ChatChannelOutputTypeDef,
        "displayName": str,
        "engagements": List[str],
        "incidentTemplate": IncidentTemplateOutputTypeDef,
        "integrations": List[IntegrationOutputTypeDef],
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateResponsePlanInputRequestTypeDef = TypedDict(
    "_RequiredCreateResponsePlanInputRequestTypeDef",
    {
        "incidentTemplate": IncidentTemplateTypeDef,
        "name": str,
    },
)
_OptionalCreateResponsePlanInputRequestTypeDef = TypedDict(
    "_OptionalCreateResponsePlanInputRequestTypeDef",
    {
        "actions": Sequence[ActionTypeDef],
        "chatChannel": ChatChannelTypeDef,
        "clientToken": str,
        "displayName": str,
        "engagements": Sequence[str],
        "integrations": Sequence[IntegrationTypeDef],
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateResponsePlanInputRequestTypeDef(
    _RequiredCreateResponsePlanInputRequestTypeDef, _OptionalCreateResponsePlanInputRequestTypeDef
):
    pass


_RequiredUpdateResponsePlanInputRequestTypeDef = TypedDict(
    "_RequiredUpdateResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateResponsePlanInputRequestTypeDef = TypedDict(
    "_OptionalUpdateResponsePlanInputRequestTypeDef",
    {
        "actions": Sequence[ActionTypeDef],
        "chatChannel": ChatChannelTypeDef,
        "clientToken": str,
        "displayName": str,
        "engagements": Sequence[str],
        "incidentTemplateDedupeString": str,
        "incidentTemplateImpact": int,
        "incidentTemplateNotificationTargets": Sequence[NotificationTargetItemTypeDef],
        "incidentTemplateSummary": str,
        "incidentTemplateTags": Mapping[str, str],
        "incidentTemplateTitle": str,
        "integrations": Sequence[IntegrationTypeDef],
    },
    total=False,
)


class UpdateResponsePlanInputRequestTypeDef(
    _RequiredUpdateResponsePlanInputRequestTypeDef, _OptionalUpdateResponsePlanInputRequestTypeDef
):
    pass


ListRelatedItemsOutputTypeDef = TypedDict(
    "ListRelatedItemsOutputTypeDef",
    {
        "nextToken": str,
        "relatedItems": List[RelatedItemOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RelatedItemsUpdateTypeDef = TypedDict(
    "RelatedItemsUpdateTypeDef",
    {
        "itemToAdd": RelatedItemTypeDef,
        "itemToRemove": ItemIdentifierTypeDef,
    },
    total=False,
)

_RequiredStartIncidentInputRequestTypeDef = TypedDict(
    "_RequiredStartIncidentInputRequestTypeDef",
    {
        "responsePlanArn": str,
    },
)
_OptionalStartIncidentInputRequestTypeDef = TypedDict(
    "_OptionalStartIncidentInputRequestTypeDef",
    {
        "clientToken": str,
        "impact": int,
        "relatedItems": Sequence[RelatedItemTypeDef],
        "title": str,
        "triggerDetails": TriggerDetailsTypeDef,
    },
    total=False,
)


class StartIncidentInputRequestTypeDef(
    _RequiredStartIncidentInputRequestTypeDef, _OptionalStartIncidentInputRequestTypeDef
):
    pass


_RequiredUpdateRelatedItemsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateRelatedItemsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "relatedItemsUpdate": RelatedItemsUpdateTypeDef,
    },
)
_OptionalUpdateRelatedItemsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateRelatedItemsInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateRelatedItemsInputRequestTypeDef(
    _RequiredUpdateRelatedItemsInputRequestTypeDef, _OptionalUpdateRelatedItemsInputRequestTypeDef
):
    pass
