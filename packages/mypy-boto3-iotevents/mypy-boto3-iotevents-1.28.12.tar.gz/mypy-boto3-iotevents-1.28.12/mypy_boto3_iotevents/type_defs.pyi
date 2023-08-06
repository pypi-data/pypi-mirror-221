"""
Type annotations for iotevents service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotevents.type_defs import AcknowledgeFlowOutputTypeDef

    data: AcknowledgeFlowOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AlarmModelVersionStatusType,
    AnalysisResultLevelType,
    AnalysisStatusType,
    ComparisonOperatorType,
    DetectorModelVersionStatusType,
    EvaluationMethodType,
    InputStatusType,
    LoggingLevelType,
    PayloadTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcknowledgeFlowOutputTypeDef",
    "AcknowledgeFlowTypeDef",
    "ClearTimerActionOutputTypeDef",
    "ResetTimerActionOutputTypeDef",
    "SetTimerActionOutputTypeDef",
    "SetVariableActionOutputTypeDef",
    "ClearTimerActionTypeDef",
    "ResetTimerActionTypeDef",
    "SetTimerActionTypeDef",
    "SetVariableActionTypeDef",
    "InitializationConfigurationOutputTypeDef",
    "InitializationConfigurationTypeDef",
    "AlarmModelSummaryTypeDef",
    "AlarmModelVersionSummaryTypeDef",
    "SimpleRuleOutputTypeDef",
    "SimpleRuleTypeDef",
    "AnalysisResultLocationTypeDef",
    "AssetPropertyTimestampOutputTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyVariantOutputTypeDef",
    "AssetPropertyVariantTypeDef",
    "AttributeOutputTypeDef",
    "AttributeTypeDef",
    "TagTypeDef",
    "CreateAlarmModelResponseTypeDef",
    "DetectorModelConfigurationTypeDef",
    "InputConfigurationTypeDef",
    "DeleteAlarmModelRequestRequestTypeDef",
    "DeleteDetectorModelRequestRequestTypeDef",
    "DeleteInputRequestRequestTypeDef",
    "DescribeAlarmModelRequestRequestTypeDef",
    "DescribeDetectorModelAnalysisRequestRequestTypeDef",
    "DescribeDetectorModelAnalysisResponseTypeDef",
    "DescribeDetectorModelRequestRequestTypeDef",
    "DescribeInputRequestRequestTypeDef",
    "DetectorDebugOptionOutputTypeDef",
    "DetectorDebugOptionTypeDef",
    "DetectorModelSummaryTypeDef",
    "DetectorModelVersionSummaryTypeDef",
    "PayloadOutputTypeDef",
    "PayloadTypeDef",
    "EmailContentOutputTypeDef",
    "EmailContentTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDetectorModelAnalysisResultsRequestRequestTypeDef",
    "IotEventsInputIdentifierTypeDef",
    "InputSummaryTypeDef",
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    "ListAlarmModelVersionsRequestRequestTypeDef",
    "ListAlarmModelsRequestRequestTypeDef",
    "ListDetectorModelVersionsRequestRequestTypeDef",
    "ListDetectorModelsRequestRequestTypeDef",
    "RoutedResourceTypeDef",
    "ListInputsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "SSOIdentityOutputTypeDef",
    "SSOIdentityTypeDef",
    "ResponseMetadataTypeDef",
    "StartDetectorModelAnalysisResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAlarmModelResponseTypeDef",
    "AlarmCapabilitiesOutputTypeDef",
    "AlarmCapabilitiesTypeDef",
    "ListAlarmModelsResponseTypeDef",
    "ListAlarmModelVersionsResponseTypeDef",
    "AlarmRuleOutputTypeDef",
    "AlarmRuleTypeDef",
    "AnalysisResultTypeDef",
    "AssetPropertyValueOutputTypeDef",
    "AssetPropertyValueTypeDef",
    "InputDefinitionOutputTypeDef",
    "InputDefinitionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateDetectorModelResponseTypeDef",
    "UpdateDetectorModelResponseTypeDef",
    "CreateInputResponseTypeDef",
    "UpdateInputResponseTypeDef",
    "LoggingOptionsOutputTypeDef",
    "LoggingOptionsTypeDef",
    "ListDetectorModelsResponseTypeDef",
    "ListDetectorModelVersionsResponseTypeDef",
    "DynamoDBActionOutputTypeDef",
    "DynamoDBv2ActionOutputTypeDef",
    "FirehoseActionOutputTypeDef",
    "IotEventsActionOutputTypeDef",
    "IotTopicPublishActionOutputTypeDef",
    "LambdaActionOutputTypeDef",
    "SNSTopicPublishActionOutputTypeDef",
    "SqsActionOutputTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "FirehoseActionTypeDef",
    "IotEventsActionTypeDef",
    "IotTopicPublishActionTypeDef",
    "LambdaActionTypeDef",
    "SNSTopicPublishActionTypeDef",
    "SqsActionTypeDef",
    "ListInputsResponseTypeDef",
    "IotSiteWiseInputIdentifierTypeDef",
    "ListInputRoutingsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RecipientDetailOutputTypeDef",
    "RecipientDetailTypeDef",
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    "IotSiteWiseActionOutputTypeDef",
    "IotSiteWiseActionTypeDef",
    "InputTypeDef",
    "CreateInputRequestRequestTypeDef",
    "UpdateInputRequestRequestTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "NotificationTargetActionsOutputTypeDef",
    "NotificationTargetActionsTypeDef",
    "InputIdentifierTypeDef",
    "EmailRecipientsOutputTypeDef",
    "SMSConfigurationOutputTypeDef",
    "EmailRecipientsTypeDef",
    "SMSConfigurationTypeDef",
    "ActionOutputTypeDef",
    "AlarmActionOutputTypeDef",
    "ActionTypeDef",
    "AlarmActionTypeDef",
    "DescribeInputResponseTypeDef",
    "ListInputRoutingsRequestRequestTypeDef",
    "EmailConfigurationOutputTypeDef",
    "EmailConfigurationTypeDef",
    "EventOutputTypeDef",
    "TransitionEventOutputTypeDef",
    "AlarmEventActionsOutputTypeDef",
    "EventTypeDef",
    "TransitionEventTypeDef",
    "AlarmEventActionsTypeDef",
    "NotificationActionOutputTypeDef",
    "NotificationActionTypeDef",
    "OnEnterLifecycleOutputTypeDef",
    "OnExitLifecycleOutputTypeDef",
    "OnInputLifecycleOutputTypeDef",
    "OnEnterLifecycleTypeDef",
    "OnExitLifecycleTypeDef",
    "OnInputLifecycleTypeDef",
    "AlarmNotificationOutputTypeDef",
    "AlarmNotificationTypeDef",
    "StateOutputTypeDef",
    "StateTypeDef",
    "DescribeAlarmModelResponseTypeDef",
    "CreateAlarmModelRequestRequestTypeDef",
    "UpdateAlarmModelRequestRequestTypeDef",
    "DetectorModelDefinitionOutputTypeDef",
    "DetectorModelDefinitionTypeDef",
    "DetectorModelTypeDef",
    "CreateDetectorModelRequestRequestTypeDef",
    "StartDetectorModelAnalysisRequestRequestTypeDef",
    "UpdateDetectorModelRequestRequestTypeDef",
    "DescribeDetectorModelResponseTypeDef",
)

AcknowledgeFlowOutputTypeDef = TypedDict(
    "AcknowledgeFlowOutputTypeDef",
    {
        "enabled": bool,
    },
)

AcknowledgeFlowTypeDef = TypedDict(
    "AcknowledgeFlowTypeDef",
    {
        "enabled": bool,
    },
)

ClearTimerActionOutputTypeDef = TypedDict(
    "ClearTimerActionOutputTypeDef",
    {
        "timerName": str,
    },
)

ResetTimerActionOutputTypeDef = TypedDict(
    "ResetTimerActionOutputTypeDef",
    {
        "timerName": str,
    },
)

_RequiredSetTimerActionOutputTypeDef = TypedDict(
    "_RequiredSetTimerActionOutputTypeDef",
    {
        "timerName": str,
    },
)
_OptionalSetTimerActionOutputTypeDef = TypedDict(
    "_OptionalSetTimerActionOutputTypeDef",
    {
        "seconds": int,
        "durationExpression": str,
    },
    total=False,
)

class SetTimerActionOutputTypeDef(
    _RequiredSetTimerActionOutputTypeDef, _OptionalSetTimerActionOutputTypeDef
):
    pass

SetVariableActionOutputTypeDef = TypedDict(
    "SetVariableActionOutputTypeDef",
    {
        "variableName": str,
        "value": str,
    },
)

ClearTimerActionTypeDef = TypedDict(
    "ClearTimerActionTypeDef",
    {
        "timerName": str,
    },
)

ResetTimerActionTypeDef = TypedDict(
    "ResetTimerActionTypeDef",
    {
        "timerName": str,
    },
)

_RequiredSetTimerActionTypeDef = TypedDict(
    "_RequiredSetTimerActionTypeDef",
    {
        "timerName": str,
    },
)
_OptionalSetTimerActionTypeDef = TypedDict(
    "_OptionalSetTimerActionTypeDef",
    {
        "seconds": int,
        "durationExpression": str,
    },
    total=False,
)

class SetTimerActionTypeDef(_RequiredSetTimerActionTypeDef, _OptionalSetTimerActionTypeDef):
    pass

SetVariableActionTypeDef = TypedDict(
    "SetVariableActionTypeDef",
    {
        "variableName": str,
        "value": str,
    },
)

InitializationConfigurationOutputTypeDef = TypedDict(
    "InitializationConfigurationOutputTypeDef",
    {
        "disabledOnInitialization": bool,
    },
)

InitializationConfigurationTypeDef = TypedDict(
    "InitializationConfigurationTypeDef",
    {
        "disabledOnInitialization": bool,
    },
)

AlarmModelSummaryTypeDef = TypedDict(
    "AlarmModelSummaryTypeDef",
    {
        "creationTime": datetime,
        "alarmModelDescription": str,
        "alarmModelName": str,
    },
    total=False,
)

AlarmModelVersionSummaryTypeDef = TypedDict(
    "AlarmModelVersionSummaryTypeDef",
    {
        "alarmModelName": str,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "statusMessage": str,
    },
    total=False,
)

SimpleRuleOutputTypeDef = TypedDict(
    "SimpleRuleOutputTypeDef",
    {
        "inputProperty": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": str,
    },
)

SimpleRuleTypeDef = TypedDict(
    "SimpleRuleTypeDef",
    {
        "inputProperty": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": str,
    },
)

AnalysisResultLocationTypeDef = TypedDict(
    "AnalysisResultLocationTypeDef",
    {
        "path": str,
    },
    total=False,
)

_RequiredAssetPropertyTimestampOutputTypeDef = TypedDict(
    "_RequiredAssetPropertyTimestampOutputTypeDef",
    {
        "timeInSeconds": str,
    },
)
_OptionalAssetPropertyTimestampOutputTypeDef = TypedDict(
    "_OptionalAssetPropertyTimestampOutputTypeDef",
    {
        "offsetInNanos": str,
    },
    total=False,
)

class AssetPropertyTimestampOutputTypeDef(
    _RequiredAssetPropertyTimestampOutputTypeDef, _OptionalAssetPropertyTimestampOutputTypeDef
):
    pass

_RequiredAssetPropertyTimestampTypeDef = TypedDict(
    "_RequiredAssetPropertyTimestampTypeDef",
    {
        "timeInSeconds": str,
    },
)
_OptionalAssetPropertyTimestampTypeDef = TypedDict(
    "_OptionalAssetPropertyTimestampTypeDef",
    {
        "offsetInNanos": str,
    },
    total=False,
)

class AssetPropertyTimestampTypeDef(
    _RequiredAssetPropertyTimestampTypeDef, _OptionalAssetPropertyTimestampTypeDef
):
    pass

AssetPropertyVariantOutputTypeDef = TypedDict(
    "AssetPropertyVariantOutputTypeDef",
    {
        "stringValue": str,
        "integerValue": str,
        "doubleValue": str,
        "booleanValue": str,
    },
    total=False,
)

AssetPropertyVariantTypeDef = TypedDict(
    "AssetPropertyVariantTypeDef",
    {
        "stringValue": str,
        "integerValue": str,
        "doubleValue": str,
        "booleanValue": str,
    },
    total=False,
)

AttributeOutputTypeDef = TypedDict(
    "AttributeOutputTypeDef",
    {
        "jsonPath": str,
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "jsonPath": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

CreateAlarmModelResponseTypeDef = TypedDict(
    "CreateAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectorModelConfigurationTypeDef = TypedDict(
    "DetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": DetectorModelVersionStatusType,
        "key": str,
        "evaluationMethod": EvaluationMethodType,
    },
    total=False,
)

_RequiredInputConfigurationTypeDef = TypedDict(
    "_RequiredInputConfigurationTypeDef",
    {
        "inputName": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": InputStatusType,
    },
)
_OptionalInputConfigurationTypeDef = TypedDict(
    "_OptionalInputConfigurationTypeDef",
    {
        "inputDescription": str,
    },
    total=False,
)

class InputConfigurationTypeDef(
    _RequiredInputConfigurationTypeDef, _OptionalInputConfigurationTypeDef
):
    pass

DeleteAlarmModelRequestRequestTypeDef = TypedDict(
    "DeleteAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
    },
)

DeleteDetectorModelRequestRequestTypeDef = TypedDict(
    "DeleteDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
    },
)

DeleteInputRequestRequestTypeDef = TypedDict(
    "DeleteInputRequestRequestTypeDef",
    {
        "inputName": str,
    },
)

_RequiredDescribeAlarmModelRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
    },
)
_OptionalDescribeAlarmModelRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAlarmModelRequestRequestTypeDef",
    {
        "alarmModelVersion": str,
    },
    total=False,
)

class DescribeAlarmModelRequestRequestTypeDef(
    _RequiredDescribeAlarmModelRequestRequestTypeDef,
    _OptionalDescribeAlarmModelRequestRequestTypeDef,
):
    pass

DescribeDetectorModelAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisRequestRequestTypeDef",
    {
        "analysisId": str,
    },
)

DescribeDetectorModelAnalysisResponseTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisResponseTypeDef",
    {
        "status": AnalysisStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDetectorModelRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalDescribeDetectorModelRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDetectorModelRequestRequestTypeDef",
    {
        "detectorModelVersion": str,
    },
    total=False,
)

class DescribeDetectorModelRequestRequestTypeDef(
    _RequiredDescribeDetectorModelRequestRequestTypeDef,
    _OptionalDescribeDetectorModelRequestRequestTypeDef,
):
    pass

DescribeInputRequestRequestTypeDef = TypedDict(
    "DescribeInputRequestRequestTypeDef",
    {
        "inputName": str,
    },
)

_RequiredDetectorDebugOptionOutputTypeDef = TypedDict(
    "_RequiredDetectorDebugOptionOutputTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalDetectorDebugOptionOutputTypeDef = TypedDict(
    "_OptionalDetectorDebugOptionOutputTypeDef",
    {
        "keyValue": str,
    },
    total=False,
)

class DetectorDebugOptionOutputTypeDef(
    _RequiredDetectorDebugOptionOutputTypeDef, _OptionalDetectorDebugOptionOutputTypeDef
):
    pass

_RequiredDetectorDebugOptionTypeDef = TypedDict(
    "_RequiredDetectorDebugOptionTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalDetectorDebugOptionTypeDef = TypedDict(
    "_OptionalDetectorDebugOptionTypeDef",
    {
        "keyValue": str,
    },
    total=False,
)

class DetectorDebugOptionTypeDef(
    _RequiredDetectorDebugOptionTypeDef, _OptionalDetectorDebugOptionTypeDef
):
    pass

DetectorModelSummaryTypeDef = TypedDict(
    "DetectorModelSummaryTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDescription": str,
        "creationTime": datetime,
    },
    total=False,
)

DetectorModelVersionSummaryTypeDef = TypedDict(
    "DetectorModelVersionSummaryTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": DetectorModelVersionStatusType,
        "evaluationMethod": EvaluationMethodType,
    },
    total=False,
)

PayloadOutputTypeDef = TypedDict(
    "PayloadOutputTypeDef",
    {
        "contentExpression": str,
        "type": PayloadTypeType,
    },
)

PayloadTypeDef = TypedDict(
    "PayloadTypeDef",
    {
        "contentExpression": str,
        "type": PayloadTypeType,
    },
)

EmailContentOutputTypeDef = TypedDict(
    "EmailContentOutputTypeDef",
    {
        "subject": str,
        "additionalMessage": str,
    },
    total=False,
)

EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "subject": str,
        "additionalMessage": str,
    },
    total=False,
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDetectorModelAnalysisResultsRequestRequestTypeDef = TypedDict(
    "_RequiredGetDetectorModelAnalysisResultsRequestRequestTypeDef",
    {
        "analysisId": str,
    },
)
_OptionalGetDetectorModelAnalysisResultsRequestRequestTypeDef = TypedDict(
    "_OptionalGetDetectorModelAnalysisResultsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetDetectorModelAnalysisResultsRequestRequestTypeDef(
    _RequiredGetDetectorModelAnalysisResultsRequestRequestTypeDef,
    _OptionalGetDetectorModelAnalysisResultsRequestRequestTypeDef,
):
    pass

IotEventsInputIdentifierTypeDef = TypedDict(
    "IotEventsInputIdentifierTypeDef",
    {
        "inputName": str,
    },
)

InputSummaryTypeDef = TypedDict(
    "InputSummaryTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": InputStatusType,
    },
    total=False,
)

IotSiteWiseAssetModelPropertyIdentifierTypeDef = TypedDict(
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    {
        "assetModelId": str,
        "propertyId": str,
    },
)

_RequiredListAlarmModelVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAlarmModelVersionsRequestRequestTypeDef",
    {
        "alarmModelName": str,
    },
)
_OptionalListAlarmModelVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAlarmModelVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAlarmModelVersionsRequestRequestTypeDef(
    _RequiredListAlarmModelVersionsRequestRequestTypeDef,
    _OptionalListAlarmModelVersionsRequestRequestTypeDef,
):
    pass

ListAlarmModelsRequestRequestTypeDef = TypedDict(
    "ListAlarmModelsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListDetectorModelVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDetectorModelVersionsRequestRequestTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalListDetectorModelVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDetectorModelVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDetectorModelVersionsRequestRequestTypeDef(
    _RequiredListDetectorModelVersionsRequestRequestTypeDef,
    _OptionalListDetectorModelVersionsRequestRequestTypeDef,
):
    pass

ListDetectorModelsRequestRequestTypeDef = TypedDict(
    "ListDetectorModelsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

RoutedResourceTypeDef = TypedDict(
    "RoutedResourceTypeDef",
    {
        "name": str,
        "arn": str,
    },
    total=False,
)

ListInputsRequestRequestTypeDef = TypedDict(
    "ListInputsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredSSOIdentityOutputTypeDef = TypedDict(
    "_RequiredSSOIdentityOutputTypeDef",
    {
        "identityStoreId": str,
    },
)
_OptionalSSOIdentityOutputTypeDef = TypedDict(
    "_OptionalSSOIdentityOutputTypeDef",
    {
        "userId": str,
    },
    total=False,
)

class SSOIdentityOutputTypeDef(
    _RequiredSSOIdentityOutputTypeDef, _OptionalSSOIdentityOutputTypeDef
):
    pass

_RequiredSSOIdentityTypeDef = TypedDict(
    "_RequiredSSOIdentityTypeDef",
    {
        "identityStoreId": str,
    },
)
_OptionalSSOIdentityTypeDef = TypedDict(
    "_OptionalSSOIdentityTypeDef",
    {
        "userId": str,
    },
    total=False,
)

class SSOIdentityTypeDef(_RequiredSSOIdentityTypeDef, _OptionalSSOIdentityTypeDef):
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

StartDetectorModelAnalysisResponseTypeDef = TypedDict(
    "StartDetectorModelAnalysisResponseTypeDef",
    {
        "analysisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAlarmModelResponseTypeDef = TypedDict(
    "UpdateAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AlarmCapabilitiesOutputTypeDef = TypedDict(
    "AlarmCapabilitiesOutputTypeDef",
    {
        "initializationConfiguration": InitializationConfigurationOutputTypeDef,
        "acknowledgeFlow": AcknowledgeFlowOutputTypeDef,
    },
    total=False,
)

AlarmCapabilitiesTypeDef = TypedDict(
    "AlarmCapabilitiesTypeDef",
    {
        "initializationConfiguration": InitializationConfigurationTypeDef,
        "acknowledgeFlow": AcknowledgeFlowTypeDef,
    },
    total=False,
)

ListAlarmModelsResponseTypeDef = TypedDict(
    "ListAlarmModelsResponseTypeDef",
    {
        "alarmModelSummaries": List[AlarmModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAlarmModelVersionsResponseTypeDef = TypedDict(
    "ListAlarmModelVersionsResponseTypeDef",
    {
        "alarmModelVersionSummaries": List[AlarmModelVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AlarmRuleOutputTypeDef = TypedDict(
    "AlarmRuleOutputTypeDef",
    {
        "simpleRule": SimpleRuleOutputTypeDef,
    },
    total=False,
)

AlarmRuleTypeDef = TypedDict(
    "AlarmRuleTypeDef",
    {
        "simpleRule": SimpleRuleTypeDef,
    },
    total=False,
)

AnalysisResultTypeDef = TypedDict(
    "AnalysisResultTypeDef",
    {
        "type": str,
        "level": AnalysisResultLevelType,
        "message": str,
        "locations": List[AnalysisResultLocationTypeDef],
    },
    total=False,
)

AssetPropertyValueOutputTypeDef = TypedDict(
    "AssetPropertyValueOutputTypeDef",
    {
        "value": AssetPropertyVariantOutputTypeDef,
        "timestamp": AssetPropertyTimestampOutputTypeDef,
        "quality": str,
    },
    total=False,
)

AssetPropertyValueTypeDef = TypedDict(
    "AssetPropertyValueTypeDef",
    {
        "value": AssetPropertyVariantTypeDef,
        "timestamp": AssetPropertyTimestampTypeDef,
        "quality": str,
    },
    total=False,
)

InputDefinitionOutputTypeDef = TypedDict(
    "InputDefinitionOutputTypeDef",
    {
        "attributes": List[AttributeOutputTypeDef],
    },
)

InputDefinitionTypeDef = TypedDict(
    "InputDefinitionTypeDef",
    {
        "attributes": Sequence[AttributeTypeDef],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

CreateDetectorModelResponseTypeDef = TypedDict(
    "CreateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": DetectorModelConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDetectorModelResponseTypeDef = TypedDict(
    "UpdateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": DetectorModelConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInputResponseTypeDef = TypedDict(
    "CreateInputResponseTypeDef",
    {
        "inputConfiguration": InputConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInputResponseTypeDef = TypedDict(
    "UpdateInputResponseTypeDef",
    {
        "inputConfiguration": InputConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLoggingOptionsOutputTypeDef = TypedDict(
    "_RequiredLoggingOptionsOutputTypeDef",
    {
        "roleArn": str,
        "level": LoggingLevelType,
        "enabled": bool,
    },
)
_OptionalLoggingOptionsOutputTypeDef = TypedDict(
    "_OptionalLoggingOptionsOutputTypeDef",
    {
        "detectorDebugOptions": List[DetectorDebugOptionOutputTypeDef],
    },
    total=False,
)

class LoggingOptionsOutputTypeDef(
    _RequiredLoggingOptionsOutputTypeDef, _OptionalLoggingOptionsOutputTypeDef
):
    pass

_RequiredLoggingOptionsTypeDef = TypedDict(
    "_RequiredLoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": LoggingLevelType,
        "enabled": bool,
    },
)
_OptionalLoggingOptionsTypeDef = TypedDict(
    "_OptionalLoggingOptionsTypeDef",
    {
        "detectorDebugOptions": Sequence[DetectorDebugOptionTypeDef],
    },
    total=False,
)

class LoggingOptionsTypeDef(_RequiredLoggingOptionsTypeDef, _OptionalLoggingOptionsTypeDef):
    pass

ListDetectorModelsResponseTypeDef = TypedDict(
    "ListDetectorModelsResponseTypeDef",
    {
        "detectorModelSummaries": List[DetectorModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectorModelVersionsResponseTypeDef = TypedDict(
    "ListDetectorModelVersionsResponseTypeDef",
    {
        "detectorModelVersionSummaries": List[DetectorModelVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDynamoDBActionOutputTypeDef = TypedDict(
    "_RequiredDynamoDBActionOutputTypeDef",
    {
        "hashKeyField": str,
        "hashKeyValue": str,
        "tableName": str,
    },
)
_OptionalDynamoDBActionOutputTypeDef = TypedDict(
    "_OptionalDynamoDBActionOutputTypeDef",
    {
        "hashKeyType": str,
        "rangeKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "operation": str,
        "payloadField": str,
        "payload": PayloadOutputTypeDef,
    },
    total=False,
)

class DynamoDBActionOutputTypeDef(
    _RequiredDynamoDBActionOutputTypeDef, _OptionalDynamoDBActionOutputTypeDef
):
    pass

_RequiredDynamoDBv2ActionOutputTypeDef = TypedDict(
    "_RequiredDynamoDBv2ActionOutputTypeDef",
    {
        "tableName": str,
    },
)
_OptionalDynamoDBv2ActionOutputTypeDef = TypedDict(
    "_OptionalDynamoDBv2ActionOutputTypeDef",
    {
        "payload": PayloadOutputTypeDef,
    },
    total=False,
)

class DynamoDBv2ActionOutputTypeDef(
    _RequiredDynamoDBv2ActionOutputTypeDef, _OptionalDynamoDBv2ActionOutputTypeDef
):
    pass

_RequiredFirehoseActionOutputTypeDef = TypedDict(
    "_RequiredFirehoseActionOutputTypeDef",
    {
        "deliveryStreamName": str,
    },
)
_OptionalFirehoseActionOutputTypeDef = TypedDict(
    "_OptionalFirehoseActionOutputTypeDef",
    {
        "separator": str,
        "payload": PayloadOutputTypeDef,
    },
    total=False,
)

class FirehoseActionOutputTypeDef(
    _RequiredFirehoseActionOutputTypeDef, _OptionalFirehoseActionOutputTypeDef
):
    pass

_RequiredIotEventsActionOutputTypeDef = TypedDict(
    "_RequiredIotEventsActionOutputTypeDef",
    {
        "inputName": str,
    },
)
_OptionalIotEventsActionOutputTypeDef = TypedDict(
    "_OptionalIotEventsActionOutputTypeDef",
    {
        "payload": PayloadOutputTypeDef,
    },
    total=False,
)

class IotEventsActionOutputTypeDef(
    _RequiredIotEventsActionOutputTypeDef, _OptionalIotEventsActionOutputTypeDef
):
    pass

_RequiredIotTopicPublishActionOutputTypeDef = TypedDict(
    "_RequiredIotTopicPublishActionOutputTypeDef",
    {
        "mqttTopic": str,
    },
)
_OptionalIotTopicPublishActionOutputTypeDef = TypedDict(
    "_OptionalIotTopicPublishActionOutputTypeDef",
    {
        "payload": PayloadOutputTypeDef,
    },
    total=False,
)

class IotTopicPublishActionOutputTypeDef(
    _RequiredIotTopicPublishActionOutputTypeDef, _OptionalIotTopicPublishActionOutputTypeDef
):
    pass

_RequiredLambdaActionOutputTypeDef = TypedDict(
    "_RequiredLambdaActionOutputTypeDef",
    {
        "functionArn": str,
    },
)
_OptionalLambdaActionOutputTypeDef = TypedDict(
    "_OptionalLambdaActionOutputTypeDef",
    {
        "payload": PayloadOutputTypeDef,
    },
    total=False,
)

class LambdaActionOutputTypeDef(
    _RequiredLambdaActionOutputTypeDef, _OptionalLambdaActionOutputTypeDef
):
    pass

_RequiredSNSTopicPublishActionOutputTypeDef = TypedDict(
    "_RequiredSNSTopicPublishActionOutputTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalSNSTopicPublishActionOutputTypeDef = TypedDict(
    "_OptionalSNSTopicPublishActionOutputTypeDef",
    {
        "payload": PayloadOutputTypeDef,
    },
    total=False,
)

class SNSTopicPublishActionOutputTypeDef(
    _RequiredSNSTopicPublishActionOutputTypeDef, _OptionalSNSTopicPublishActionOutputTypeDef
):
    pass

_RequiredSqsActionOutputTypeDef = TypedDict(
    "_RequiredSqsActionOutputTypeDef",
    {
        "queueUrl": str,
    },
)
_OptionalSqsActionOutputTypeDef = TypedDict(
    "_OptionalSqsActionOutputTypeDef",
    {
        "useBase64": bool,
        "payload": PayloadOutputTypeDef,
    },
    total=False,
)

class SqsActionOutputTypeDef(_RequiredSqsActionOutputTypeDef, _OptionalSqsActionOutputTypeDef):
    pass

_RequiredDynamoDBActionTypeDef = TypedDict(
    "_RequiredDynamoDBActionTypeDef",
    {
        "hashKeyField": str,
        "hashKeyValue": str,
        "tableName": str,
    },
)
_OptionalDynamoDBActionTypeDef = TypedDict(
    "_OptionalDynamoDBActionTypeDef",
    {
        "hashKeyType": str,
        "rangeKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "operation": str,
        "payloadField": str,
        "payload": PayloadTypeDef,
    },
    total=False,
)

class DynamoDBActionTypeDef(_RequiredDynamoDBActionTypeDef, _OptionalDynamoDBActionTypeDef):
    pass

_RequiredDynamoDBv2ActionTypeDef = TypedDict(
    "_RequiredDynamoDBv2ActionTypeDef",
    {
        "tableName": str,
    },
)
_OptionalDynamoDBv2ActionTypeDef = TypedDict(
    "_OptionalDynamoDBv2ActionTypeDef",
    {
        "payload": PayloadTypeDef,
    },
    total=False,
)

class DynamoDBv2ActionTypeDef(_RequiredDynamoDBv2ActionTypeDef, _OptionalDynamoDBv2ActionTypeDef):
    pass

_RequiredFirehoseActionTypeDef = TypedDict(
    "_RequiredFirehoseActionTypeDef",
    {
        "deliveryStreamName": str,
    },
)
_OptionalFirehoseActionTypeDef = TypedDict(
    "_OptionalFirehoseActionTypeDef",
    {
        "separator": str,
        "payload": PayloadTypeDef,
    },
    total=False,
)

class FirehoseActionTypeDef(_RequiredFirehoseActionTypeDef, _OptionalFirehoseActionTypeDef):
    pass

_RequiredIotEventsActionTypeDef = TypedDict(
    "_RequiredIotEventsActionTypeDef",
    {
        "inputName": str,
    },
)
_OptionalIotEventsActionTypeDef = TypedDict(
    "_OptionalIotEventsActionTypeDef",
    {
        "payload": PayloadTypeDef,
    },
    total=False,
)

class IotEventsActionTypeDef(_RequiredIotEventsActionTypeDef, _OptionalIotEventsActionTypeDef):
    pass

_RequiredIotTopicPublishActionTypeDef = TypedDict(
    "_RequiredIotTopicPublishActionTypeDef",
    {
        "mqttTopic": str,
    },
)
_OptionalIotTopicPublishActionTypeDef = TypedDict(
    "_OptionalIotTopicPublishActionTypeDef",
    {
        "payload": PayloadTypeDef,
    },
    total=False,
)

class IotTopicPublishActionTypeDef(
    _RequiredIotTopicPublishActionTypeDef, _OptionalIotTopicPublishActionTypeDef
):
    pass

_RequiredLambdaActionTypeDef = TypedDict(
    "_RequiredLambdaActionTypeDef",
    {
        "functionArn": str,
    },
)
_OptionalLambdaActionTypeDef = TypedDict(
    "_OptionalLambdaActionTypeDef",
    {
        "payload": PayloadTypeDef,
    },
    total=False,
)

class LambdaActionTypeDef(_RequiredLambdaActionTypeDef, _OptionalLambdaActionTypeDef):
    pass

_RequiredSNSTopicPublishActionTypeDef = TypedDict(
    "_RequiredSNSTopicPublishActionTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalSNSTopicPublishActionTypeDef = TypedDict(
    "_OptionalSNSTopicPublishActionTypeDef",
    {
        "payload": PayloadTypeDef,
    },
    total=False,
)

class SNSTopicPublishActionTypeDef(
    _RequiredSNSTopicPublishActionTypeDef, _OptionalSNSTopicPublishActionTypeDef
):
    pass

_RequiredSqsActionTypeDef = TypedDict(
    "_RequiredSqsActionTypeDef",
    {
        "queueUrl": str,
    },
)
_OptionalSqsActionTypeDef = TypedDict(
    "_OptionalSqsActionTypeDef",
    {
        "useBase64": bool,
        "payload": PayloadTypeDef,
    },
    total=False,
)

class SqsActionTypeDef(_RequiredSqsActionTypeDef, _OptionalSqsActionTypeDef):
    pass

ListInputsResponseTypeDef = TypedDict(
    "ListInputsResponseTypeDef",
    {
        "inputSummaries": List[InputSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IotSiteWiseInputIdentifierTypeDef = TypedDict(
    "IotSiteWiseInputIdentifierTypeDef",
    {
        "iotSiteWiseAssetModelPropertyIdentifier": IotSiteWiseAssetModelPropertyIdentifierTypeDef,
    },
    total=False,
)

ListInputRoutingsResponseTypeDef = TypedDict(
    "ListInputRoutingsResponseTypeDef",
    {
        "routedResources": List[RoutedResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecipientDetailOutputTypeDef = TypedDict(
    "RecipientDetailOutputTypeDef",
    {
        "ssoIdentity": SSOIdentityOutputTypeDef,
    },
    total=False,
)

RecipientDetailTypeDef = TypedDict(
    "RecipientDetailTypeDef",
    {
        "ssoIdentity": SSOIdentityTypeDef,
    },
    total=False,
)

GetDetectorModelAnalysisResultsResponseTypeDef = TypedDict(
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    {
        "analysisResults": List[AnalysisResultTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IotSiteWiseActionOutputTypeDef = TypedDict(
    "IotSiteWiseActionOutputTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValue": AssetPropertyValueOutputTypeDef,
    },
    total=False,
)

IotSiteWiseActionTypeDef = TypedDict(
    "IotSiteWiseActionTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValue": AssetPropertyValueTypeDef,
    },
    total=False,
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "inputConfiguration": InputConfigurationTypeDef,
        "inputDefinition": InputDefinitionOutputTypeDef,
    },
    total=False,
)

_RequiredCreateInputRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInputRequestRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": InputDefinitionTypeDef,
    },
)
_OptionalCreateInputRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInputRequestRequestTypeDef",
    {
        "inputDescription": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateInputRequestRequestTypeDef(
    _RequiredCreateInputRequestRequestTypeDef, _OptionalCreateInputRequestRequestTypeDef
):
    pass

_RequiredUpdateInputRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInputRequestRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": InputDefinitionTypeDef,
    },
)
_OptionalUpdateInputRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInputRequestRequestTypeDef",
    {
        "inputDescription": str,
    },
    total=False,
)

class UpdateInputRequestRequestTypeDef(
    _RequiredUpdateInputRequestRequestTypeDef, _OptionalUpdateInputRequestRequestTypeDef
):
    pass

DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": LoggingOptionsOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
    },
)

NotificationTargetActionsOutputTypeDef = TypedDict(
    "NotificationTargetActionsOutputTypeDef",
    {
        "lambdaAction": LambdaActionOutputTypeDef,
    },
    total=False,
)

NotificationTargetActionsTypeDef = TypedDict(
    "NotificationTargetActionsTypeDef",
    {
        "lambdaAction": LambdaActionTypeDef,
    },
    total=False,
)

InputIdentifierTypeDef = TypedDict(
    "InputIdentifierTypeDef",
    {
        "iotEventsInputIdentifier": IotEventsInputIdentifierTypeDef,
        "iotSiteWiseInputIdentifier": IotSiteWiseInputIdentifierTypeDef,
    },
    total=False,
)

EmailRecipientsOutputTypeDef = TypedDict(
    "EmailRecipientsOutputTypeDef",
    {
        "to": List[RecipientDetailOutputTypeDef],
    },
    total=False,
)

_RequiredSMSConfigurationOutputTypeDef = TypedDict(
    "_RequiredSMSConfigurationOutputTypeDef",
    {
        "recipients": List[RecipientDetailOutputTypeDef],
    },
)
_OptionalSMSConfigurationOutputTypeDef = TypedDict(
    "_OptionalSMSConfigurationOutputTypeDef",
    {
        "senderId": str,
        "additionalMessage": str,
    },
    total=False,
)

class SMSConfigurationOutputTypeDef(
    _RequiredSMSConfigurationOutputTypeDef, _OptionalSMSConfigurationOutputTypeDef
):
    pass

EmailRecipientsTypeDef = TypedDict(
    "EmailRecipientsTypeDef",
    {
        "to": Sequence[RecipientDetailTypeDef],
    },
    total=False,
)

_RequiredSMSConfigurationTypeDef = TypedDict(
    "_RequiredSMSConfigurationTypeDef",
    {
        "recipients": Sequence[RecipientDetailTypeDef],
    },
)
_OptionalSMSConfigurationTypeDef = TypedDict(
    "_OptionalSMSConfigurationTypeDef",
    {
        "senderId": str,
        "additionalMessage": str,
    },
    total=False,
)

class SMSConfigurationTypeDef(_RequiredSMSConfigurationTypeDef, _OptionalSMSConfigurationTypeDef):
    pass

ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "setVariable": SetVariableActionOutputTypeDef,
        "sns": SNSTopicPublishActionOutputTypeDef,
        "iotTopicPublish": IotTopicPublishActionOutputTypeDef,
        "setTimer": SetTimerActionOutputTypeDef,
        "clearTimer": ClearTimerActionOutputTypeDef,
        "resetTimer": ResetTimerActionOutputTypeDef,
        "lambda": LambdaActionOutputTypeDef,
        "iotEvents": IotEventsActionOutputTypeDef,
        "sqs": SqsActionOutputTypeDef,
        "firehose": FirehoseActionOutputTypeDef,
        "dynamoDB": DynamoDBActionOutputTypeDef,
        "dynamoDBv2": DynamoDBv2ActionOutputTypeDef,
        "iotSiteWise": IotSiteWiseActionOutputTypeDef,
    },
    total=False,
)

AlarmActionOutputTypeDef = TypedDict(
    "AlarmActionOutputTypeDef",
    {
        "sns": SNSTopicPublishActionOutputTypeDef,
        "iotTopicPublish": IotTopicPublishActionOutputTypeDef,
        "lambda": LambdaActionOutputTypeDef,
        "iotEvents": IotEventsActionOutputTypeDef,
        "sqs": SqsActionOutputTypeDef,
        "firehose": FirehoseActionOutputTypeDef,
        "dynamoDB": DynamoDBActionOutputTypeDef,
        "dynamoDBv2": DynamoDBv2ActionOutputTypeDef,
        "iotSiteWise": IotSiteWiseActionOutputTypeDef,
    },
    total=False,
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "setVariable": SetVariableActionTypeDef,
        "sns": SNSTopicPublishActionTypeDef,
        "iotTopicPublish": IotTopicPublishActionTypeDef,
        "setTimer": SetTimerActionTypeDef,
        "clearTimer": ClearTimerActionTypeDef,
        "resetTimer": ResetTimerActionTypeDef,
        "lambda": LambdaActionTypeDef,
        "iotEvents": IotEventsActionTypeDef,
        "sqs": SqsActionTypeDef,
        "firehose": FirehoseActionTypeDef,
        "dynamoDB": DynamoDBActionTypeDef,
        "dynamoDBv2": DynamoDBv2ActionTypeDef,
        "iotSiteWise": IotSiteWiseActionTypeDef,
    },
    total=False,
)

AlarmActionTypeDef = TypedDict(
    "AlarmActionTypeDef",
    {
        "sns": SNSTopicPublishActionTypeDef,
        "iotTopicPublish": IotTopicPublishActionTypeDef,
        "lambda": LambdaActionTypeDef,
        "iotEvents": IotEventsActionTypeDef,
        "sqs": SqsActionTypeDef,
        "firehose": FirehoseActionTypeDef,
        "dynamoDB": DynamoDBActionTypeDef,
        "dynamoDBv2": DynamoDBv2ActionTypeDef,
        "iotSiteWise": IotSiteWiseActionTypeDef,
    },
    total=False,
)

DescribeInputResponseTypeDef = TypedDict(
    "DescribeInputResponseTypeDef",
    {
        "input": InputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInputRoutingsRequestRequestTypeDef = TypedDict(
    "_RequiredListInputRoutingsRequestRequestTypeDef",
    {
        "inputIdentifier": InputIdentifierTypeDef,
    },
)
_OptionalListInputRoutingsRequestRequestTypeDef = TypedDict(
    "_OptionalListInputRoutingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListInputRoutingsRequestRequestTypeDef(
    _RequiredListInputRoutingsRequestRequestTypeDef, _OptionalListInputRoutingsRequestRequestTypeDef
):
    pass

_RequiredEmailConfigurationOutputTypeDef = TypedDict(
    "_RequiredEmailConfigurationOutputTypeDef",
    {
        "from": str,
        "recipients": EmailRecipientsOutputTypeDef,
    },
)
_OptionalEmailConfigurationOutputTypeDef = TypedDict(
    "_OptionalEmailConfigurationOutputTypeDef",
    {
        "content": EmailContentOutputTypeDef,
    },
    total=False,
)

class EmailConfigurationOutputTypeDef(
    _RequiredEmailConfigurationOutputTypeDef, _OptionalEmailConfigurationOutputTypeDef
):
    pass

_RequiredEmailConfigurationTypeDef = TypedDict(
    "_RequiredEmailConfigurationTypeDef",
    {
        "from": str,
        "recipients": EmailRecipientsTypeDef,
    },
)
_OptionalEmailConfigurationTypeDef = TypedDict(
    "_OptionalEmailConfigurationTypeDef",
    {
        "content": EmailContentTypeDef,
    },
    total=False,
)

class EmailConfigurationTypeDef(
    _RequiredEmailConfigurationTypeDef, _OptionalEmailConfigurationTypeDef
):
    pass

_RequiredEventOutputTypeDef = TypedDict(
    "_RequiredEventOutputTypeDef",
    {
        "eventName": str,
    },
)
_OptionalEventOutputTypeDef = TypedDict(
    "_OptionalEventOutputTypeDef",
    {
        "condition": str,
        "actions": List[ActionOutputTypeDef],
    },
    total=False,
)

class EventOutputTypeDef(_RequiredEventOutputTypeDef, _OptionalEventOutputTypeDef):
    pass

_RequiredTransitionEventOutputTypeDef = TypedDict(
    "_RequiredTransitionEventOutputTypeDef",
    {
        "eventName": str,
        "condition": str,
        "nextState": str,
    },
)
_OptionalTransitionEventOutputTypeDef = TypedDict(
    "_OptionalTransitionEventOutputTypeDef",
    {
        "actions": List[ActionOutputTypeDef],
    },
    total=False,
)

class TransitionEventOutputTypeDef(
    _RequiredTransitionEventOutputTypeDef, _OptionalTransitionEventOutputTypeDef
):
    pass

AlarmEventActionsOutputTypeDef = TypedDict(
    "AlarmEventActionsOutputTypeDef",
    {
        "alarmActions": List[AlarmActionOutputTypeDef],
    },
    total=False,
)

_RequiredEventTypeDef = TypedDict(
    "_RequiredEventTypeDef",
    {
        "eventName": str,
    },
)
_OptionalEventTypeDef = TypedDict(
    "_OptionalEventTypeDef",
    {
        "condition": str,
        "actions": Sequence[ActionTypeDef],
    },
    total=False,
)

class EventTypeDef(_RequiredEventTypeDef, _OptionalEventTypeDef):
    pass

_RequiredTransitionEventTypeDef = TypedDict(
    "_RequiredTransitionEventTypeDef",
    {
        "eventName": str,
        "condition": str,
        "nextState": str,
    },
)
_OptionalTransitionEventTypeDef = TypedDict(
    "_OptionalTransitionEventTypeDef",
    {
        "actions": Sequence[ActionTypeDef],
    },
    total=False,
)

class TransitionEventTypeDef(_RequiredTransitionEventTypeDef, _OptionalTransitionEventTypeDef):
    pass

AlarmEventActionsTypeDef = TypedDict(
    "AlarmEventActionsTypeDef",
    {
        "alarmActions": Sequence[AlarmActionTypeDef],
    },
    total=False,
)

_RequiredNotificationActionOutputTypeDef = TypedDict(
    "_RequiredNotificationActionOutputTypeDef",
    {
        "action": NotificationTargetActionsOutputTypeDef,
    },
)
_OptionalNotificationActionOutputTypeDef = TypedDict(
    "_OptionalNotificationActionOutputTypeDef",
    {
        "smsConfigurations": List[SMSConfigurationOutputTypeDef],
        "emailConfigurations": List[EmailConfigurationOutputTypeDef],
    },
    total=False,
)

class NotificationActionOutputTypeDef(
    _RequiredNotificationActionOutputTypeDef, _OptionalNotificationActionOutputTypeDef
):
    pass

_RequiredNotificationActionTypeDef = TypedDict(
    "_RequiredNotificationActionTypeDef",
    {
        "action": NotificationTargetActionsTypeDef,
    },
)
_OptionalNotificationActionTypeDef = TypedDict(
    "_OptionalNotificationActionTypeDef",
    {
        "smsConfigurations": Sequence[SMSConfigurationTypeDef],
        "emailConfigurations": Sequence[EmailConfigurationTypeDef],
    },
    total=False,
)

class NotificationActionTypeDef(
    _RequiredNotificationActionTypeDef, _OptionalNotificationActionTypeDef
):
    pass

OnEnterLifecycleOutputTypeDef = TypedDict(
    "OnEnterLifecycleOutputTypeDef",
    {
        "events": List[EventOutputTypeDef],
    },
    total=False,
)

OnExitLifecycleOutputTypeDef = TypedDict(
    "OnExitLifecycleOutputTypeDef",
    {
        "events": List[EventOutputTypeDef],
    },
    total=False,
)

OnInputLifecycleOutputTypeDef = TypedDict(
    "OnInputLifecycleOutputTypeDef",
    {
        "events": List[EventOutputTypeDef],
        "transitionEvents": List[TransitionEventOutputTypeDef],
    },
    total=False,
)

OnEnterLifecycleTypeDef = TypedDict(
    "OnEnterLifecycleTypeDef",
    {
        "events": Sequence[EventTypeDef],
    },
    total=False,
)

OnExitLifecycleTypeDef = TypedDict(
    "OnExitLifecycleTypeDef",
    {
        "events": Sequence[EventTypeDef],
    },
    total=False,
)

OnInputLifecycleTypeDef = TypedDict(
    "OnInputLifecycleTypeDef",
    {
        "events": Sequence[EventTypeDef],
        "transitionEvents": Sequence[TransitionEventTypeDef],
    },
    total=False,
)

AlarmNotificationOutputTypeDef = TypedDict(
    "AlarmNotificationOutputTypeDef",
    {
        "notificationActions": List[NotificationActionOutputTypeDef],
    },
    total=False,
)

AlarmNotificationTypeDef = TypedDict(
    "AlarmNotificationTypeDef",
    {
        "notificationActions": Sequence[NotificationActionTypeDef],
    },
    total=False,
)

_RequiredStateOutputTypeDef = TypedDict(
    "_RequiredStateOutputTypeDef",
    {
        "stateName": str,
    },
)
_OptionalStateOutputTypeDef = TypedDict(
    "_OptionalStateOutputTypeDef",
    {
        "onInput": OnInputLifecycleOutputTypeDef,
        "onEnter": OnEnterLifecycleOutputTypeDef,
        "onExit": OnExitLifecycleOutputTypeDef,
    },
    total=False,
)

class StateOutputTypeDef(_RequiredStateOutputTypeDef, _OptionalStateOutputTypeDef):
    pass

_RequiredStateTypeDef = TypedDict(
    "_RequiredStateTypeDef",
    {
        "stateName": str,
    },
)
_OptionalStateTypeDef = TypedDict(
    "_OptionalStateTypeDef",
    {
        "onInput": OnInputLifecycleTypeDef,
        "onEnter": OnEnterLifecycleTypeDef,
        "onExit": OnExitLifecycleTypeDef,
    },
    total=False,
)

class StateTypeDef(_RequiredStateTypeDef, _OptionalStateTypeDef):
    pass

DescribeAlarmModelResponseTypeDef = TypedDict(
    "DescribeAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "statusMessage": str,
        "alarmModelName": str,
        "alarmModelDescription": str,
        "roleArn": str,
        "key": str,
        "severity": int,
        "alarmRule": AlarmRuleOutputTypeDef,
        "alarmNotification": AlarmNotificationOutputTypeDef,
        "alarmEventActions": AlarmEventActionsOutputTypeDef,
        "alarmCapabilities": AlarmCapabilitiesOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAlarmModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": AlarmRuleTypeDef,
    },
)
_OptionalCreateAlarmModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelDescription": str,
        "tags": Sequence[TagTypeDef],
        "key": str,
        "severity": int,
        "alarmNotification": AlarmNotificationTypeDef,
        "alarmEventActions": AlarmEventActionsTypeDef,
        "alarmCapabilities": AlarmCapabilitiesTypeDef,
    },
    total=False,
)

class CreateAlarmModelRequestRequestTypeDef(
    _RequiredCreateAlarmModelRequestRequestTypeDef, _OptionalCreateAlarmModelRequestRequestTypeDef
):
    pass

_RequiredUpdateAlarmModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": AlarmRuleTypeDef,
    },
)
_OptionalUpdateAlarmModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelDescription": str,
        "severity": int,
        "alarmNotification": AlarmNotificationTypeDef,
        "alarmEventActions": AlarmEventActionsTypeDef,
        "alarmCapabilities": AlarmCapabilitiesTypeDef,
    },
    total=False,
)

class UpdateAlarmModelRequestRequestTypeDef(
    _RequiredUpdateAlarmModelRequestRequestTypeDef, _OptionalUpdateAlarmModelRequestRequestTypeDef
):
    pass

DetectorModelDefinitionOutputTypeDef = TypedDict(
    "DetectorModelDefinitionOutputTypeDef",
    {
        "states": List[StateOutputTypeDef],
        "initialStateName": str,
    },
)

DetectorModelDefinitionTypeDef = TypedDict(
    "DetectorModelDefinitionTypeDef",
    {
        "states": Sequence[StateTypeDef],
        "initialStateName": str,
    },
)

DetectorModelTypeDef = TypedDict(
    "DetectorModelTypeDef",
    {
        "detectorModelDefinition": DetectorModelDefinitionOutputTypeDef,
        "detectorModelConfiguration": DetectorModelConfigurationTypeDef,
    },
    total=False,
)

_RequiredCreateDetectorModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
        "roleArn": str,
    },
)
_OptionalCreateDetectorModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelDescription": str,
        "key": str,
        "tags": Sequence[TagTypeDef],
        "evaluationMethod": EvaluationMethodType,
    },
    total=False,
)

class CreateDetectorModelRequestRequestTypeDef(
    _RequiredCreateDetectorModelRequestRequestTypeDef,
    _OptionalCreateDetectorModelRequestRequestTypeDef,
):
    pass

StartDetectorModelAnalysisRequestRequestTypeDef = TypedDict(
    "StartDetectorModelAnalysisRequestRequestTypeDef",
    {
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
    },
)

_RequiredUpdateDetectorModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
        "roleArn": str,
    },
)
_OptionalUpdateDetectorModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelDescription": str,
        "evaluationMethod": EvaluationMethodType,
    },
    total=False,
)

class UpdateDetectorModelRequestRequestTypeDef(
    _RequiredUpdateDetectorModelRequestRequestTypeDef,
    _OptionalUpdateDetectorModelRequestRequestTypeDef,
):
    pass

DescribeDetectorModelResponseTypeDef = TypedDict(
    "DescribeDetectorModelResponseTypeDef",
    {
        "detectorModel": DetectorModelTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
