"""
Type annotations for events service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/type_defs/)

Usage::

    ```python
    from mypy_boto3_events.type_defs import ActivateEventSourceRequestRequestTypeDef

    data: ActivateEventSourceRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ApiDestinationHttpMethodType,
    ApiDestinationStateType,
    ArchiveStateType,
    AssignPublicIpType,
    ConnectionAuthorizationTypeType,
    ConnectionOAuthHttpMethodType,
    ConnectionStateType,
    EndpointStateType,
    EventSourceStateType,
    LaunchTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    ReplayStateType,
    ReplicationStateType,
    RuleStateType,
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
    "ActivateEventSourceRequestRequestTypeDef",
    "ApiDestinationTypeDef",
    "ArchiveTypeDef",
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesOutputTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchRetryStrategyOutputTypeDef",
    "BatchRetryStrategyTypeDef",
    "CancelReplayRequestRequestTypeDef",
    "CancelReplayResponseTypeDef",
    "CapacityProviderStrategyItemOutputTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "ConditionTypeDef",
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    "ConnectionBasicAuthResponseParametersTypeDef",
    "ConnectionBodyParameterOutputTypeDef",
    "ConnectionBodyParameterTypeDef",
    "ConnectionHeaderParameterOutputTypeDef",
    "ConnectionHeaderParameterTypeDef",
    "ConnectionQueryStringParameterOutputTypeDef",
    "ConnectionQueryStringParameterTypeDef",
    "ConnectionOAuthClientResponseParametersTypeDef",
    "ConnectionTypeDef",
    "CreateApiDestinationRequestRequestTypeDef",
    "CreateApiDestinationResponseTypeDef",
    "CreateArchiveRequestRequestTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    "CreateConnectionResponseTypeDef",
    "EndpointEventBusTypeDef",
    "ReplicationConfigTypeDef",
    "EndpointEventBusOutputTypeDef",
    "ReplicationConfigOutputTypeDef",
    "TagTypeDef",
    "CreateEventBusResponseTypeDef",
    "CreatePartnerEventSourceRequestRequestTypeDef",
    "CreatePartnerEventSourceResponseTypeDef",
    "DeactivateEventSourceRequestRequestTypeDef",
    "DeadLetterConfigOutputTypeDef",
    "DeadLetterConfigTypeDef",
    "DeauthorizeConnectionRequestRequestTypeDef",
    "DeauthorizeConnectionResponseTypeDef",
    "DeleteApiDestinationRequestRequestTypeDef",
    "DeleteArchiveRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "DeleteEventBusRequestRequestTypeDef",
    "DeletePartnerEventSourceRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DescribeApiDestinationRequestRequestTypeDef",
    "DescribeApiDestinationResponseTypeDef",
    "DescribeArchiveRequestRequestTypeDef",
    "DescribeArchiveResponseTypeDef",
    "DescribeConnectionRequestRequestTypeDef",
    "DescribeEndpointRequestRequestTypeDef",
    "DescribeEventBusRequestRequestTypeDef",
    "DescribeEventBusResponseTypeDef",
    "DescribeEventSourceRequestRequestTypeDef",
    "DescribeEventSourceResponseTypeDef",
    "DescribePartnerEventSourceRequestRequestTypeDef",
    "DescribePartnerEventSourceResponseTypeDef",
    "DescribeReplayRequestRequestTypeDef",
    "ReplayDestinationOutputTypeDef",
    "DescribeRuleRequestRequestTypeDef",
    "DescribeRuleResponseTypeDef",
    "DisableRuleRequestRequestTypeDef",
    "PlacementConstraintOutputTypeDef",
    "PlacementStrategyOutputTypeDef",
    "TagOutputTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableRuleRequestRequestTypeDef",
    "EventBusTypeDef",
    "EventSourceTypeDef",
    "PrimaryOutputTypeDef",
    "SecondaryOutputTypeDef",
    "PrimaryTypeDef",
    "SecondaryTypeDef",
    "HttpParametersOutputTypeDef",
    "HttpParametersTypeDef",
    "InputTransformerOutputTypeDef",
    "InputTransformerTypeDef",
    "KinesisParametersOutputTypeDef",
    "KinesisParametersTypeDef",
    "ListApiDestinationsRequestRequestTypeDef",
    "ListArchivesRequestRequestTypeDef",
    "ListConnectionsRequestRequestTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEventBusesRequestRequestTypeDef",
    "ListEventSourcesRequestRequestTypeDef",
    "ListPartnerEventSourceAccountsRequestRequestTypeDef",
    "PartnerEventSourceAccountTypeDef",
    "ListPartnerEventSourcesRequestRequestTypeDef",
    "PartnerEventSourceTypeDef",
    "ListReplaysRequestRequestTypeDef",
    "ReplayTypeDef",
    "ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef",
    "ListRuleNamesByTargetRequestRequestTypeDef",
    "ListRuleNamesByTargetResponseTypeDef",
    "ListRulesRequestListRulesPaginateTypeDef",
    "ListRulesRequestRequestTypeDef",
    "RuleTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTargetsByRuleRequestListTargetsByRulePaginateTypeDef",
    "ListTargetsByRuleRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutEventsRequestEntryTypeDef",
    "PutEventsResultEntryTypeDef",
    "PutPartnerEventsRequestEntryTypeDef",
    "PutPartnerEventsResultEntryTypeDef",
    "PutRuleResponseTypeDef",
    "PutTargetsResultEntryTypeDef",
    "RedshiftDataParametersOutputTypeDef",
    "RedshiftDataParametersTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "RemoveTargetsRequestRequestTypeDef",
    "RemoveTargetsResultEntryTypeDef",
    "ReplayDestinationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryPolicyOutputTypeDef",
    "RetryPolicyTypeDef",
    "RunCommandTargetOutputTypeDef",
    "RunCommandTargetTypeDef",
    "SageMakerPipelineParameterOutputTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SqsParametersOutputTypeDef",
    "SqsParametersTypeDef",
    "StartReplayResponseTypeDef",
    "TestEventPatternRequestRequestTypeDef",
    "TestEventPatternResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiDestinationRequestRequestTypeDef",
    "UpdateApiDestinationResponseTypeDef",
    "UpdateArchiveRequestRequestTypeDef",
    "UpdateArchiveResponseTypeDef",
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    "UpdateConnectionResponseTypeDef",
    "ListApiDestinationsResponseTypeDef",
    "ListArchivesResponseTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "BatchParametersOutputTypeDef",
    "BatchParametersTypeDef",
    "PutPermissionRequestRequestTypeDef",
    "ConnectionHttpParametersOutputTypeDef",
    "ConnectionHttpParametersTypeDef",
    "ListConnectionsResponseTypeDef",
    "CreateEventBusRequestRequestTypeDef",
    "PutRuleRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DescribeReplayResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListEventBusesResponseTypeDef",
    "ListEventSourcesResponseTypeDef",
    "FailoverConfigOutputTypeDef",
    "FailoverConfigTypeDef",
    "ListPartnerEventSourceAccountsResponseTypeDef",
    "ListPartnerEventSourcesResponseTypeDef",
    "ListReplaysResponseTypeDef",
    "ListRulesResponseTypeDef",
    "PutEventsRequestRequestTypeDef",
    "PutEventsResponseTypeDef",
    "PutPartnerEventsRequestRequestTypeDef",
    "PutPartnerEventsResponseTypeDef",
    "PutTargetsResponseTypeDef",
    "RemoveTargetsResponseTypeDef",
    "StartReplayRequestRequestTypeDef",
    "RunCommandParametersOutputTypeDef",
    "RunCommandParametersTypeDef",
    "SageMakerPipelineParametersOutputTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "EcsParametersOutputTypeDef",
    "EcsParametersTypeDef",
    "ConnectionOAuthResponseParametersTypeDef",
    "CreateConnectionOAuthRequestParametersTypeDef",
    "UpdateConnectionOAuthRequestParametersTypeDef",
    "RoutingConfigOutputTypeDef",
    "RoutingConfigTypeDef",
    "TargetOutputTypeDef",
    "TargetTypeDef",
    "ConnectionAuthResponseParametersTypeDef",
    "CreateConnectionAuthRequestParametersTypeDef",
    "UpdateConnectionAuthRequestParametersTypeDef",
    "CreateEndpointResponseTypeDef",
    "DescribeEndpointResponseTypeDef",
    "EndpointTypeDef",
    "UpdateEndpointResponseTypeDef",
    "CreateEndpointRequestRequestTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "ListTargetsByRuleResponseTypeDef",
    "PutTargetsRequestRequestTypeDef",
    "DescribeConnectionResponseTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "ListEndpointsResponseTypeDef",
)

ActivateEventSourceRequestRequestTypeDef = TypedDict(
    "ActivateEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

ApiDestinationTypeDef = TypedDict(
    "ApiDestinationTypeDef",
    {
        "ApiDestinationArn": str,
        "Name": str,
        "ApiDestinationState": ApiDestinationStateType,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ArchiveTypeDef = TypedDict(
    "ArchiveTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
    },
    total=False,
)

_RequiredAwsVpcConfigurationOutputTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationOutputTypeDef",
    {
        "Subnets": List[str],
    },
)
_OptionalAwsVpcConfigurationOutputTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationOutputTypeDef",
    {
        "SecurityGroups": List[str],
        "AssignPublicIp": AssignPublicIpType,
    },
    total=False,
)


class AwsVpcConfigurationOutputTypeDef(
    _RequiredAwsVpcConfigurationOutputTypeDef, _OptionalAwsVpcConfigurationOutputTypeDef
):
    pass


_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef",
    {
        "Subnets": Sequence[str],
    },
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {
        "SecurityGroups": Sequence[str],
        "AssignPublicIp": AssignPublicIpType,
    },
    total=False,
)


class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass


BatchArrayPropertiesOutputTypeDef = TypedDict(
    "BatchArrayPropertiesOutputTypeDef",
    {
        "Size": int,
    },
    total=False,
)

BatchArrayPropertiesTypeDef = TypedDict(
    "BatchArrayPropertiesTypeDef",
    {
        "Size": int,
    },
    total=False,
)

BatchRetryStrategyOutputTypeDef = TypedDict(
    "BatchRetryStrategyOutputTypeDef",
    {
        "Attempts": int,
    },
    total=False,
)

BatchRetryStrategyTypeDef = TypedDict(
    "BatchRetryStrategyTypeDef",
    {
        "Attempts": int,
    },
    total=False,
)

CancelReplayRequestRequestTypeDef = TypedDict(
    "CancelReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
    },
)

CancelReplayResponseTypeDef = TypedDict(
    "CancelReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCapacityProviderStrategyItemOutputTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemOutputTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemOutputTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemOutputTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)


class CapacityProviderStrategyItemOutputTypeDef(
    _RequiredCapacityProviderStrategyItemOutputTypeDef,
    _OptionalCapacityProviderStrategyItemOutputTypeDef,
):
    pass


_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)


class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass


ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Type": str,
        "Key": str,
        "Value": str,
    },
)

ConnectionApiKeyAuthResponseParametersTypeDef = TypedDict(
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    {
        "ApiKeyName": str,
    },
    total=False,
)

ConnectionBasicAuthResponseParametersTypeDef = TypedDict(
    "ConnectionBasicAuthResponseParametersTypeDef",
    {
        "Username": str,
    },
    total=False,
)

ConnectionBodyParameterOutputTypeDef = TypedDict(
    "ConnectionBodyParameterOutputTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionBodyParameterTypeDef = TypedDict(
    "ConnectionBodyParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionHeaderParameterOutputTypeDef = TypedDict(
    "ConnectionHeaderParameterOutputTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionHeaderParameterTypeDef = TypedDict(
    "ConnectionHeaderParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionQueryStringParameterOutputTypeDef = TypedDict(
    "ConnectionQueryStringParameterOutputTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionQueryStringParameterTypeDef = TypedDict(
    "ConnectionQueryStringParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionOAuthClientResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthClientResponseParametersTypeDef",
    {
        "ClientID": str,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionArn": str,
        "Name": str,
        "ConnectionState": ConnectionStateType,
        "StateReason": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
    },
    total=False,
)

_RequiredCreateApiDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
    },
)
_OptionalCreateApiDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApiDestinationRequestRequestTypeDef",
    {
        "Description": str,
        "InvocationRateLimitPerSecond": int,
    },
    total=False,
)


class CreateApiDestinationRequestRequestTypeDef(
    _RequiredCreateApiDestinationRequestRequestTypeDef,
    _OptionalCreateApiDestinationRequestRequestTypeDef,
):
    pass


CreateApiDestinationResponseTypeDef = TypedDict(
    "CreateApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateArchiveRequestRequestTypeDef = TypedDict(
    "_RequiredCreateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
    },
)
_OptionalCreateArchiveRequestRequestTypeDef = TypedDict(
    "_OptionalCreateArchiveRequestRequestTypeDef",
    {
        "Description": str,
        "EventPattern": str,
        "RetentionDays": int,
    },
    total=False,
)


class CreateArchiveRequestRequestTypeDef(
    _RequiredCreateArchiveRequestRequestTypeDef, _OptionalCreateArchiveRequestRequestTypeDef
):
    pass


CreateArchiveResponseTypeDef = TypedDict(
    "CreateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": str,
        "ApiKeyValue": str,
    },
)

CreateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

CreateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": str,
        "ClientSecret": str,
    },
)

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointEventBusTypeDef = TypedDict(
    "EndpointEventBusTypeDef",
    {
        "EventBusArn": str,
    },
)

ReplicationConfigTypeDef = TypedDict(
    "ReplicationConfigTypeDef",
    {
        "State": ReplicationStateType,
    },
    total=False,
)

EndpointEventBusOutputTypeDef = TypedDict(
    "EndpointEventBusOutputTypeDef",
    {
        "EventBusArn": str,
    },
)

ReplicationConfigOutputTypeDef = TypedDict(
    "ReplicationConfigOutputTypeDef",
    {
        "State": ReplicationStateType,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateEventBusResponseTypeDef = TypedDict(
    "CreateEventBusResponseTypeDef",
    {
        "EventBusArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "CreatePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)

CreatePartnerEventSourceResponseTypeDef = TypedDict(
    "CreatePartnerEventSourceResponseTypeDef",
    {
        "EventSourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateEventSourceRequestRequestTypeDef = TypedDict(
    "DeactivateEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeadLetterConfigOutputTypeDef = TypedDict(
    "DeadLetterConfigOutputTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

DeauthorizeConnectionRequestRequestTypeDef = TypedDict(
    "DeauthorizeConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeauthorizeConnectionResponseTypeDef = TypedDict(
    "DeauthorizeConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApiDestinationRequestRequestTypeDef = TypedDict(
    "DeleteApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteArchiveRequestRequestTypeDef = TypedDict(
    "DeleteArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteEventBusRequestRequestTypeDef = TypedDict(
    "DeleteEventBusRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeletePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "DeletePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)

_RequiredDeleteRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
        "Force": bool,
    },
    total=False,
)


class DeleteRuleRequestRequestTypeDef(
    _RequiredDeleteRuleRequestRequestTypeDef, _OptionalDeleteRuleRequestRequestTypeDef
):
    pass


DescribeApiDestinationRequestRequestTypeDef = TypedDict(
    "DescribeApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeApiDestinationResponseTypeDef = TypedDict(
    "DescribeApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "Name": str,
        "Description": str,
        "ApiDestinationState": ApiDestinationStateType,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeArchiveRequestRequestTypeDef = TypedDict(
    "DescribeArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)

DescribeArchiveResponseTypeDef = TypedDict(
    "DescribeArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "ArchiveName": str,
        "EventSourceArn": str,
        "Description": str,
        "EventPattern": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionRequestRequestTypeDef = TypedDict(
    "DescribeConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredDescribeEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEndpointRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEndpointRequestRequestTypeDef",
    {
        "HomeRegion": str,
    },
    total=False,
)


class DescribeEndpointRequestRequestTypeDef(
    _RequiredDescribeEndpointRequestRequestTypeDef, _OptionalDescribeEndpointRequestRequestTypeDef
):
    pass


DescribeEventBusRequestRequestTypeDef = TypedDict(
    "DescribeEventBusRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

DescribeEventBusResponseTypeDef = TypedDict(
    "DescribeEventBusResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSourceRequestRequestTypeDef = TypedDict(
    "DescribeEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeEventSourceResponseTypeDef = TypedDict(
    "DescribeEventSourceResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": EventSourceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "DescribePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribePartnerEventSourceResponseTypeDef = TypedDict(
    "DescribePartnerEventSourceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplayRequestRequestTypeDef = TypedDict(
    "DescribeReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
    },
)

_RequiredReplayDestinationOutputTypeDef = TypedDict(
    "_RequiredReplayDestinationOutputTypeDef",
    {
        "Arn": str,
    },
)
_OptionalReplayDestinationOutputTypeDef = TypedDict(
    "_OptionalReplayDestinationOutputTypeDef",
    {
        "FilterArns": List[str],
    },
    total=False,
)


class ReplayDestinationOutputTypeDef(
    _RequiredReplayDestinationOutputTypeDef, _OptionalReplayDestinationOutputTypeDef
):
    pass


_RequiredDescribeRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)


class DescribeRuleRequestRequestTypeDef(
    _RequiredDescribeRuleRequestRequestTypeDef, _OptionalDescribeRuleRequestRequestTypeDef
):
    pass


DescribeRuleResponseTypeDef = TypedDict(
    "DescribeRuleResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": RuleStateType,
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
        "CreatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDisableRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDisableRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDisableRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)


class DisableRuleRequestRequestTypeDef(
    _RequiredDisableRuleRequestRequestTypeDef, _OptionalDisableRuleRequestRequestTypeDef
):
    pass


PlacementConstraintOutputTypeDef = TypedDict(
    "PlacementConstraintOutputTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyOutputTypeDef = TypedDict(
    "PlacementStrategyOutputTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
    },
    total=False,
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
    },
    total=False,
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableRuleRequestRequestTypeDef = TypedDict(
    "_RequiredEnableRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalEnableRuleRequestRequestTypeDef = TypedDict(
    "_OptionalEnableRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)


class EnableRuleRequestRequestTypeDef(
    _RequiredEnableRuleRequestRequestTypeDef, _OptionalEnableRuleRequestRequestTypeDef
):
    pass


EventBusTypeDef = TypedDict(
    "EventBusTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Policy": str,
    },
    total=False,
)

EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": EventSourceStateType,
    },
    total=False,
)

PrimaryOutputTypeDef = TypedDict(
    "PrimaryOutputTypeDef",
    {
        "HealthCheck": str,
    },
)

SecondaryOutputTypeDef = TypedDict(
    "SecondaryOutputTypeDef",
    {
        "Route": str,
    },
)

PrimaryTypeDef = TypedDict(
    "PrimaryTypeDef",
    {
        "HealthCheck": str,
    },
)

SecondaryTypeDef = TypedDict(
    "SecondaryTypeDef",
    {
        "Route": str,
    },
)

HttpParametersOutputTypeDef = TypedDict(
    "HttpParametersOutputTypeDef",
    {
        "PathParameterValues": List[str],
        "HeaderParameters": Dict[str, str],
        "QueryStringParameters": Dict[str, str],
    },
    total=False,
)

HttpParametersTypeDef = TypedDict(
    "HttpParametersTypeDef",
    {
        "PathParameterValues": Sequence[str],
        "HeaderParameters": Mapping[str, str],
        "QueryStringParameters": Mapping[str, str],
    },
    total=False,
)

_RequiredInputTransformerOutputTypeDef = TypedDict(
    "_RequiredInputTransformerOutputTypeDef",
    {
        "InputTemplate": str,
    },
)
_OptionalInputTransformerOutputTypeDef = TypedDict(
    "_OptionalInputTransformerOutputTypeDef",
    {
        "InputPathsMap": Dict[str, str],
    },
    total=False,
)


class InputTransformerOutputTypeDef(
    _RequiredInputTransformerOutputTypeDef, _OptionalInputTransformerOutputTypeDef
):
    pass


_RequiredInputTransformerTypeDef = TypedDict(
    "_RequiredInputTransformerTypeDef",
    {
        "InputTemplate": str,
    },
)
_OptionalInputTransformerTypeDef = TypedDict(
    "_OptionalInputTransformerTypeDef",
    {
        "InputPathsMap": Mapping[str, str],
    },
    total=False,
)


class InputTransformerTypeDef(_RequiredInputTransformerTypeDef, _OptionalInputTransformerTypeDef):
    pass


KinesisParametersOutputTypeDef = TypedDict(
    "KinesisParametersOutputTypeDef",
    {
        "PartitionKeyPath": str,
    },
)

KinesisParametersTypeDef = TypedDict(
    "KinesisParametersTypeDef",
    {
        "PartitionKeyPath": str,
    },
)

ListApiDestinationsRequestRequestTypeDef = TypedDict(
    "ListApiDestinationsRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "ConnectionArn": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListArchivesRequestRequestTypeDef = TypedDict(
    "ListArchivesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "EventSourceArn": str,
        "State": ArchiveStateType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListConnectionsRequestRequestTypeDef = TypedDict(
    "ListConnectionsRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "ConnectionState": ConnectionStateType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListEndpointsRequestRequestTypeDef = TypedDict(
    "ListEndpointsRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "HomeRegion": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventBusesRequestRequestTypeDef = TypedDict(
    "ListEventBusesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListEventSourcesRequestRequestTypeDef = TypedDict(
    "ListEventSourcesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

_RequiredListPartnerEventSourceAccountsRequestRequestTypeDef = TypedDict(
    "_RequiredListPartnerEventSourceAccountsRequestRequestTypeDef",
    {
        "EventSourceName": str,
    },
)
_OptionalListPartnerEventSourceAccountsRequestRequestTypeDef = TypedDict(
    "_OptionalListPartnerEventSourceAccountsRequestRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListPartnerEventSourceAccountsRequestRequestTypeDef(
    _RequiredListPartnerEventSourceAccountsRequestRequestTypeDef,
    _OptionalListPartnerEventSourceAccountsRequestRequestTypeDef,
):
    pass


PartnerEventSourceAccountTypeDef = TypedDict(
    "PartnerEventSourceAccountTypeDef",
    {
        "Account": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "State": EventSourceStateType,
    },
    total=False,
)

_RequiredListPartnerEventSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListPartnerEventSourcesRequestRequestTypeDef",
    {
        "NamePrefix": str,
    },
)
_OptionalListPartnerEventSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListPartnerEventSourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListPartnerEventSourcesRequestRequestTypeDef(
    _RequiredListPartnerEventSourcesRequestRequestTypeDef,
    _OptionalListPartnerEventSourcesRequestRequestTypeDef,
):
    pass


PartnerEventSourceTypeDef = TypedDict(
    "PartnerEventSourceTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

ListReplaysRequestRequestTypeDef = TypedDict(
    "ListReplaysRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "State": ReplayStateType,
        "EventSourceArn": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ReplayTypeDef = TypedDict(
    "ReplayTypeDef",
    {
        "ReplayName": str,
        "EventSourceArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
    },
    total=False,
)

_RequiredListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef = TypedDict(
    "_RequiredListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef",
    {
        "TargetArn": str,
    },
)
_OptionalListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef = TypedDict(
    "_OptionalListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef",
    {
        "EventBusName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef(
    _RequiredListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef,
    _OptionalListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef,
):
    pass


_RequiredListRuleNamesByTargetRequestRequestTypeDef = TypedDict(
    "_RequiredListRuleNamesByTargetRequestRequestTypeDef",
    {
        "TargetArn": str,
    },
)
_OptionalListRuleNamesByTargetRequestRequestTypeDef = TypedDict(
    "_OptionalListRuleNamesByTargetRequestRequestTypeDef",
    {
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListRuleNamesByTargetRequestRequestTypeDef(
    _RequiredListRuleNamesByTargetRequestRequestTypeDef,
    _OptionalListRuleNamesByTargetRequestRequestTypeDef,
):
    pass


ListRuleNamesByTargetResponseTypeDef = TypedDict(
    "ListRuleNamesByTargetResponseTypeDef",
    {
        "RuleNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "ListRulesRequestListRulesPaginateTypeDef",
    {
        "NamePrefix": str,
        "EventBusName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": RuleStateType,
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

_RequiredListTargetsByRuleRequestListTargetsByRulePaginateTypeDef = TypedDict(
    "_RequiredListTargetsByRuleRequestListTargetsByRulePaginateTypeDef",
    {
        "Rule": str,
    },
)
_OptionalListTargetsByRuleRequestListTargetsByRulePaginateTypeDef = TypedDict(
    "_OptionalListTargetsByRuleRequestListTargetsByRulePaginateTypeDef",
    {
        "EventBusName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTargetsByRuleRequestListTargetsByRulePaginateTypeDef(
    _RequiredListTargetsByRuleRequestListTargetsByRulePaginateTypeDef,
    _OptionalListTargetsByRuleRequestListTargetsByRulePaginateTypeDef,
):
    pass


_RequiredListTargetsByRuleRequestRequestTypeDef = TypedDict(
    "_RequiredListTargetsByRuleRequestRequestTypeDef",
    {
        "Rule": str,
    },
)
_OptionalListTargetsByRuleRequestRequestTypeDef = TypedDict(
    "_OptionalListTargetsByRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListTargetsByRuleRequestRequestTypeDef(
    _RequiredListTargetsByRuleRequestRequestTypeDef, _OptionalListTargetsByRuleRequestRequestTypeDef
):
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

PutEventsRequestEntryTypeDef = TypedDict(
    "PutEventsRequestEntryTypeDef",
    {
        "Time": Union[datetime, str],
        "Source": str,
        "Resources": Sequence[str],
        "DetailType": str,
        "Detail": str,
        "EventBusName": str,
        "TraceHeader": str,
    },
    total=False,
)

PutEventsResultEntryTypeDef = TypedDict(
    "PutEventsResultEntryTypeDef",
    {
        "EventId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutPartnerEventsRequestEntryTypeDef = TypedDict(
    "PutPartnerEventsRequestEntryTypeDef",
    {
        "Time": Union[datetime, str],
        "Source": str,
        "Resources": Sequence[str],
        "DetailType": str,
        "Detail": str,
    },
    total=False,
)

PutPartnerEventsResultEntryTypeDef = TypedDict(
    "PutPartnerEventsResultEntryTypeDef",
    {
        "EventId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutRuleResponseTypeDef = TypedDict(
    "PutRuleResponseTypeDef",
    {
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutTargetsResultEntryTypeDef = TypedDict(
    "PutTargetsResultEntryTypeDef",
    {
        "TargetId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredRedshiftDataParametersOutputTypeDef = TypedDict(
    "_RequiredRedshiftDataParametersOutputTypeDef",
    {
        "Database": str,
    },
)
_OptionalRedshiftDataParametersOutputTypeDef = TypedDict(
    "_OptionalRedshiftDataParametersOutputTypeDef",
    {
        "SecretManagerArn": str,
        "DbUser": str,
        "Sql": str,
        "StatementName": str,
        "WithEvent": bool,
        "Sqls": List[str],
    },
    total=False,
)


class RedshiftDataParametersOutputTypeDef(
    _RequiredRedshiftDataParametersOutputTypeDef, _OptionalRedshiftDataParametersOutputTypeDef
):
    pass


_RequiredRedshiftDataParametersTypeDef = TypedDict(
    "_RequiredRedshiftDataParametersTypeDef",
    {
        "Database": str,
    },
)
_OptionalRedshiftDataParametersTypeDef = TypedDict(
    "_OptionalRedshiftDataParametersTypeDef",
    {
        "SecretManagerArn": str,
        "DbUser": str,
        "Sql": str,
        "StatementName": str,
        "WithEvent": bool,
        "Sqls": Sequence[str],
    },
    total=False,
)


class RedshiftDataParametersTypeDef(
    _RequiredRedshiftDataParametersTypeDef, _OptionalRedshiftDataParametersTypeDef
):
    pass


RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "StatementId": str,
        "RemoveAllPermissions": bool,
        "EventBusName": str,
    },
    total=False,
)

_RequiredRemoveTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredRemoveTargetsRequestRequestTypeDef",
    {
        "Rule": str,
        "Ids": Sequence[str],
    },
)
_OptionalRemoveTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalRemoveTargetsRequestRequestTypeDef",
    {
        "EventBusName": str,
        "Force": bool,
    },
    total=False,
)


class RemoveTargetsRequestRequestTypeDef(
    _RequiredRemoveTargetsRequestRequestTypeDef, _OptionalRemoveTargetsRequestRequestTypeDef
):
    pass


RemoveTargetsResultEntryTypeDef = TypedDict(
    "RemoveTargetsResultEntryTypeDef",
    {
        "TargetId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredReplayDestinationTypeDef = TypedDict(
    "_RequiredReplayDestinationTypeDef",
    {
        "Arn": str,
    },
)
_OptionalReplayDestinationTypeDef = TypedDict(
    "_OptionalReplayDestinationTypeDef",
    {
        "FilterArns": Sequence[str],
    },
    total=False,
)


class ReplayDestinationTypeDef(
    _RequiredReplayDestinationTypeDef, _OptionalReplayDestinationTypeDef
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

RetryPolicyOutputTypeDef = TypedDict(
    "RetryPolicyOutputTypeDef",
    {
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
    },
    total=False,
)

RetryPolicyTypeDef = TypedDict(
    "RetryPolicyTypeDef",
    {
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
    },
    total=False,
)

RunCommandTargetOutputTypeDef = TypedDict(
    "RunCommandTargetOutputTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)

RunCommandTargetTypeDef = TypedDict(
    "RunCommandTargetTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
)

SageMakerPipelineParameterOutputTypeDef = TypedDict(
    "SageMakerPipelineParameterOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

SqsParametersOutputTypeDef = TypedDict(
    "SqsParametersOutputTypeDef",
    {
        "MessageGroupId": str,
    },
    total=False,
)

SqsParametersTypeDef = TypedDict(
    "SqsParametersTypeDef",
    {
        "MessageGroupId": str,
    },
    total=False,
)

StartReplayResponseTypeDef = TypedDict(
    "StartReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ReplayStartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestEventPatternRequestRequestTypeDef = TypedDict(
    "TestEventPatternRequestRequestTypeDef",
    {
        "EventPattern": str,
        "Event": str,
    },
)

TestEventPatternResponseTypeDef = TypedDict(
    "TestEventPatternResponseTypeDef",
    {
        "Result": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateApiDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateApiDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApiDestinationRequestRequestTypeDef",
    {
        "Description": str,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
    },
    total=False,
)


class UpdateApiDestinationRequestRequestTypeDef(
    _RequiredUpdateApiDestinationRequestRequestTypeDef,
    _OptionalUpdateApiDestinationRequestRequestTypeDef,
):
    pass


UpdateApiDestinationResponseTypeDef = TypedDict(
    "UpdateApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateArchiveRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)
_OptionalUpdateArchiveRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateArchiveRequestRequestTypeDef",
    {
        "Description": str,
        "EventPattern": str,
        "RetentionDays": int,
    },
    total=False,
)


class UpdateArchiveRequestRequestTypeDef(
    _RequiredUpdateArchiveRequestRequestTypeDef, _OptionalUpdateArchiveRequestRequestTypeDef
):
    pass


UpdateArchiveResponseTypeDef = TypedDict(
    "UpdateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": str,
        "ApiKeyValue": str,
    },
    total=False,
)

UpdateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": str,
        "Password": str,
    },
    total=False,
)

UpdateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": str,
        "ClientSecret": str,
    },
    total=False,
)

UpdateConnectionResponseTypeDef = TypedDict(
    "UpdateConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApiDestinationsResponseTypeDef = TypedDict(
    "ListApiDestinationsResponseTypeDef",
    {
        "ApiDestinations": List[ApiDestinationTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArchivesResponseTypeDef = TypedDict(
    "ListArchivesResponseTypeDef",
    {
        "Archives": List[ArchiveTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "awsvpcConfiguration": AwsVpcConfigurationOutputTypeDef,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": AwsVpcConfigurationTypeDef,
    },
    total=False,
)

_RequiredBatchParametersOutputTypeDef = TypedDict(
    "_RequiredBatchParametersOutputTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
    },
)
_OptionalBatchParametersOutputTypeDef = TypedDict(
    "_OptionalBatchParametersOutputTypeDef",
    {
        "ArrayProperties": BatchArrayPropertiesOutputTypeDef,
        "RetryStrategy": BatchRetryStrategyOutputTypeDef,
    },
    total=False,
)


class BatchParametersOutputTypeDef(
    _RequiredBatchParametersOutputTypeDef, _OptionalBatchParametersOutputTypeDef
):
    pass


_RequiredBatchParametersTypeDef = TypedDict(
    "_RequiredBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
    },
)
_OptionalBatchParametersTypeDef = TypedDict(
    "_OptionalBatchParametersTypeDef",
    {
        "ArrayProperties": BatchArrayPropertiesTypeDef,
        "RetryStrategy": BatchRetryStrategyTypeDef,
    },
    total=False,
)


class BatchParametersTypeDef(_RequiredBatchParametersTypeDef, _OptionalBatchParametersTypeDef):
    pass


PutPermissionRequestRequestTypeDef = TypedDict(
    "PutPermissionRequestRequestTypeDef",
    {
        "EventBusName": str,
        "Action": str,
        "Principal": str,
        "StatementId": str,
        "Condition": ConditionTypeDef,
        "Policy": str,
    },
    total=False,
)

ConnectionHttpParametersOutputTypeDef = TypedDict(
    "ConnectionHttpParametersOutputTypeDef",
    {
        "HeaderParameters": List[ConnectionHeaderParameterOutputTypeDef],
        "QueryStringParameters": List[ConnectionQueryStringParameterOutputTypeDef],
        "BodyParameters": List[ConnectionBodyParameterOutputTypeDef],
    },
    total=False,
)

ConnectionHttpParametersTypeDef = TypedDict(
    "ConnectionHttpParametersTypeDef",
    {
        "HeaderParameters": Sequence[ConnectionHeaderParameterTypeDef],
        "QueryStringParameters": Sequence[ConnectionQueryStringParameterTypeDef],
        "BodyParameters": Sequence[ConnectionBodyParameterTypeDef],
    },
    total=False,
)

ListConnectionsResponseTypeDef = TypedDict(
    "ListConnectionsResponseTypeDef",
    {
        "Connections": List[ConnectionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventBusRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventBusRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateEventBusRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventBusRequestRequestTypeDef",
    {
        "EventSourceName": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateEventBusRequestRequestTypeDef(
    _RequiredCreateEventBusRequestRequestTypeDef, _OptionalCreateEventBusRequestRequestTypeDef
):
    pass


_RequiredPutRuleRequestRequestTypeDef = TypedDict(
    "_RequiredPutRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalPutRuleRequestRequestTypeDef = TypedDict(
    "_OptionalPutRuleRequestRequestTypeDef",
    {
        "ScheduleExpression": str,
        "EventPattern": str,
        "State": RuleStateType,
        "Description": str,
        "RoleArn": str,
        "Tags": Sequence[TagTypeDef],
        "EventBusName": str,
    },
    total=False,
)


class PutRuleRequestRequestTypeDef(
    _RequiredPutRuleRequestRequestTypeDef, _OptionalPutRuleRequestRequestTypeDef
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

DescribeReplayResponseTypeDef = TypedDict(
    "DescribeReplayResponseTypeDef",
    {
        "ReplayName": str,
        "ReplayArn": str,
        "Description": str,
        "State": ReplayStateType,
        "StateReason": str,
        "EventSourceArn": str,
        "Destination": ReplayDestinationOutputTypeDef,
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventBusesResponseTypeDef = TypedDict(
    "ListEventBusesResponseTypeDef",
    {
        "EventBuses": List[EventBusTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSourcesResponseTypeDef = TypedDict(
    "ListEventSourcesResponseTypeDef",
    {
        "EventSources": List[EventSourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverConfigOutputTypeDef = TypedDict(
    "FailoverConfigOutputTypeDef",
    {
        "Primary": PrimaryOutputTypeDef,
        "Secondary": SecondaryOutputTypeDef,
    },
)

FailoverConfigTypeDef = TypedDict(
    "FailoverConfigTypeDef",
    {
        "Primary": PrimaryTypeDef,
        "Secondary": SecondaryTypeDef,
    },
)

ListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "ListPartnerEventSourceAccountsResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List[PartnerEventSourceAccountTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartnerEventSourcesResponseTypeDef = TypedDict(
    "ListPartnerEventSourcesResponseTypeDef",
    {
        "PartnerEventSources": List[PartnerEventSourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplaysResponseTypeDef = TypedDict(
    "ListReplaysResponseTypeDef",
    {
        "Replays": List[ReplayTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "Rules": List[RuleTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutEventsRequestRequestTypeDef = TypedDict(
    "_RequiredPutEventsRequestRequestTypeDef",
    {
        "Entries": Sequence[PutEventsRequestEntryTypeDef],
    },
)
_OptionalPutEventsRequestRequestTypeDef = TypedDict(
    "_OptionalPutEventsRequestRequestTypeDef",
    {
        "EndpointId": str,
    },
    total=False,
)


class PutEventsRequestRequestTypeDef(
    _RequiredPutEventsRequestRequestTypeDef, _OptionalPutEventsRequestRequestTypeDef
):
    pass


PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List[PutEventsResultEntryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPartnerEventsRequestRequestTypeDef = TypedDict(
    "PutPartnerEventsRequestRequestTypeDef",
    {
        "Entries": Sequence[PutPartnerEventsRequestEntryTypeDef],
    },
)

PutPartnerEventsResponseTypeDef = TypedDict(
    "PutPartnerEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List[PutPartnerEventsResultEntryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutTargetsResponseTypeDef = TypedDict(
    "PutTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[PutTargetsResultEntryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTargetsResponseTypeDef = TypedDict(
    "RemoveTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[RemoveTargetsResultEntryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReplayRequestRequestTypeDef = TypedDict(
    "_RequiredStartReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
        "EventSourceArn": str,
        "EventStartTime": Union[datetime, str],
        "EventEndTime": Union[datetime, str],
        "Destination": ReplayDestinationTypeDef,
    },
)
_OptionalStartReplayRequestRequestTypeDef = TypedDict(
    "_OptionalStartReplayRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class StartReplayRequestRequestTypeDef(
    _RequiredStartReplayRequestRequestTypeDef, _OptionalStartReplayRequestRequestTypeDef
):
    pass


RunCommandParametersOutputTypeDef = TypedDict(
    "RunCommandParametersOutputTypeDef",
    {
        "RunCommandTargets": List[RunCommandTargetOutputTypeDef],
    },
)

RunCommandParametersTypeDef = TypedDict(
    "RunCommandParametersTypeDef",
    {
        "RunCommandTargets": Sequence[RunCommandTargetTypeDef],
    },
)

SageMakerPipelineParametersOutputTypeDef = TypedDict(
    "SageMakerPipelineParametersOutputTypeDef",
    {
        "PipelineParameterList": List[SageMakerPipelineParameterOutputTypeDef],
    },
    total=False,
)

SageMakerPipelineParametersTypeDef = TypedDict(
    "SageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": Sequence[SageMakerPipelineParameterTypeDef],
    },
    total=False,
)

_RequiredEcsParametersOutputTypeDef = TypedDict(
    "_RequiredEcsParametersOutputTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalEcsParametersOutputTypeDef = TypedDict(
    "_OptionalEcsParametersOutputTypeDef",
    {
        "TaskCount": int,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": NetworkConfigurationOutputTypeDef,
        "PlatformVersion": str,
        "Group": str,
        "CapacityProviderStrategy": List[CapacityProviderStrategyItemOutputTypeDef],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "PlacementConstraints": List[PlacementConstraintOutputTypeDef],
        "PlacementStrategy": List[PlacementStrategyOutputTypeDef],
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)


class EcsParametersOutputTypeDef(
    _RequiredEcsParametersOutputTypeDef, _OptionalEcsParametersOutputTypeDef
):
    pass


_RequiredEcsParametersTypeDef = TypedDict(
    "_RequiredEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalEcsParametersTypeDef = TypedDict(
    "_OptionalEcsParametersTypeDef",
    {
        "TaskCount": int,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
        "CapacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "PlacementConstraints": Sequence[PlacementConstraintTypeDef],
        "PlacementStrategy": Sequence[PlacementStrategyTypeDef],
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class EcsParametersTypeDef(_RequiredEcsParametersTypeDef, _OptionalEcsParametersTypeDef):
    pass


ConnectionOAuthResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthResponseParametersTypeDef",
    {
        "ClientParameters": ConnectionOAuthClientResponseParametersTypeDef,
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
        "OAuthHttpParameters": ConnectionHttpParametersOutputTypeDef,
    },
    total=False,
)

_RequiredCreateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "_RequiredCreateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": CreateConnectionOAuthClientRequestParametersTypeDef,
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
    },
)
_OptionalCreateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "_OptionalCreateConnectionOAuthRequestParametersTypeDef",
    {
        "OAuthHttpParameters": ConnectionHttpParametersTypeDef,
    },
    total=False,
)


class CreateConnectionOAuthRequestParametersTypeDef(
    _RequiredCreateConnectionOAuthRequestParametersTypeDef,
    _OptionalCreateConnectionOAuthRequestParametersTypeDef,
):
    pass


UpdateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": UpdateConnectionOAuthClientRequestParametersTypeDef,
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
        "OAuthHttpParameters": ConnectionHttpParametersTypeDef,
    },
    total=False,
)

RoutingConfigOutputTypeDef = TypedDict(
    "RoutingConfigOutputTypeDef",
    {
        "FailoverConfig": FailoverConfigOutputTypeDef,
    },
)

RoutingConfigTypeDef = TypedDict(
    "RoutingConfigTypeDef",
    {
        "FailoverConfig": FailoverConfigTypeDef,
    },
)

_RequiredTargetOutputTypeDef = TypedDict(
    "_RequiredTargetOutputTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
)
_OptionalTargetOutputTypeDef = TypedDict(
    "_OptionalTargetOutputTypeDef",
    {
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": InputTransformerOutputTypeDef,
        "KinesisParameters": KinesisParametersOutputTypeDef,
        "RunCommandParameters": RunCommandParametersOutputTypeDef,
        "EcsParameters": EcsParametersOutputTypeDef,
        "BatchParameters": BatchParametersOutputTypeDef,
        "SqsParameters": SqsParametersOutputTypeDef,
        "HttpParameters": HttpParametersOutputTypeDef,
        "RedshiftDataParameters": RedshiftDataParametersOutputTypeDef,
        "SageMakerPipelineParameters": SageMakerPipelineParametersOutputTypeDef,
        "DeadLetterConfig": DeadLetterConfigOutputTypeDef,
        "RetryPolicy": RetryPolicyOutputTypeDef,
    },
    total=False,
)


class TargetOutputTypeDef(_RequiredTargetOutputTypeDef, _OptionalTargetOutputTypeDef):
    pass


_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": InputTransformerTypeDef,
        "KinesisParameters": KinesisParametersTypeDef,
        "RunCommandParameters": RunCommandParametersTypeDef,
        "EcsParameters": EcsParametersTypeDef,
        "BatchParameters": BatchParametersTypeDef,
        "SqsParameters": SqsParametersTypeDef,
        "HttpParameters": HttpParametersTypeDef,
        "RedshiftDataParameters": RedshiftDataParametersTypeDef,
        "SageMakerPipelineParameters": SageMakerPipelineParametersTypeDef,
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "RetryPolicy": RetryPolicyTypeDef,
    },
    total=False,
)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass


ConnectionAuthResponseParametersTypeDef = TypedDict(
    "ConnectionAuthResponseParametersTypeDef",
    {
        "BasicAuthParameters": ConnectionBasicAuthResponseParametersTypeDef,
        "OAuthParameters": ConnectionOAuthResponseParametersTypeDef,
        "ApiKeyAuthParameters": ConnectionApiKeyAuthResponseParametersTypeDef,
        "InvocationHttpParameters": ConnectionHttpParametersOutputTypeDef,
    },
    total=False,
)

CreateConnectionAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": CreateConnectionBasicAuthRequestParametersTypeDef,
        "OAuthParameters": CreateConnectionOAuthRequestParametersTypeDef,
        "ApiKeyAuthParameters": CreateConnectionApiKeyAuthRequestParametersTypeDef,
        "InvocationHttpParameters": ConnectionHttpParametersTypeDef,
    },
    total=False,
)

UpdateConnectionAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": UpdateConnectionBasicAuthRequestParametersTypeDef,
        "OAuthParameters": UpdateConnectionOAuthRequestParametersTypeDef,
        "ApiKeyAuthParameters": UpdateConnectionApiKeyAuthRequestParametersTypeDef,
        "InvocationHttpParameters": ConnectionHttpParametersTypeDef,
    },
    total=False,
)

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "RoutingConfig": RoutingConfigOutputTypeDef,
        "ReplicationConfig": ReplicationConfigOutputTypeDef,
        "EventBuses": List[EndpointEventBusOutputTypeDef],
        "RoleArn": str,
        "State": EndpointStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointResponseTypeDef = TypedDict(
    "DescribeEndpointResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "RoutingConfig": RoutingConfigOutputTypeDef,
        "ReplicationConfig": ReplicationConfigOutputTypeDef,
        "EventBuses": List[EndpointEventBusOutputTypeDef],
        "RoleArn": str,
        "EndpointId": str,
        "EndpointUrl": str,
        "State": EndpointStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "RoutingConfig": RoutingConfigOutputTypeDef,
        "ReplicationConfig": ReplicationConfigOutputTypeDef,
        "EventBuses": List[EndpointEventBusOutputTypeDef],
        "RoleArn": str,
        "EndpointId": str,
        "EndpointUrl": str,
        "State": EndpointStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

UpdateEndpointResponseTypeDef = TypedDict(
    "UpdateEndpointResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "RoutingConfig": RoutingConfigOutputTypeDef,
        "ReplicationConfig": ReplicationConfigOutputTypeDef,
        "EventBuses": List[EndpointEventBusOutputTypeDef],
        "RoleArn": str,
        "EndpointId": str,
        "EndpointUrl": str,
        "State": EndpointStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointRequestRequestTypeDef",
    {
        "Name": str,
        "RoutingConfig": RoutingConfigTypeDef,
        "EventBuses": Sequence[EndpointEventBusTypeDef],
    },
)
_OptionalCreateEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointRequestRequestTypeDef",
    {
        "Description": str,
        "ReplicationConfig": ReplicationConfigTypeDef,
        "RoleArn": str,
    },
    total=False,
)


class CreateEndpointRequestRequestTypeDef(
    _RequiredCreateEndpointRequestRequestTypeDef, _OptionalCreateEndpointRequestRequestTypeDef
):
    pass


_RequiredUpdateEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEndpointRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEndpointRequestRequestTypeDef",
    {
        "Description": str,
        "RoutingConfig": RoutingConfigTypeDef,
        "ReplicationConfig": ReplicationConfigTypeDef,
        "EventBuses": Sequence[EndpointEventBusTypeDef],
        "RoleArn": str,
    },
    total=False,
)


class UpdateEndpointRequestRequestTypeDef(
    _RequiredUpdateEndpointRequestRequestTypeDef, _OptionalUpdateEndpointRequestRequestTypeDef
):
    pass


ListTargetsByRuleResponseTypeDef = TypedDict(
    "ListTargetsByRuleResponseTypeDef",
    {
        "Targets": List[TargetOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredPutTargetsRequestRequestTypeDef",
    {
        "Rule": str,
        "Targets": Sequence[TargetTypeDef],
    },
)
_OptionalPutTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalPutTargetsRequestRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)


class PutTargetsRequestRequestTypeDef(
    _RequiredPutTargetsRequestRequestTypeDef, _OptionalPutTargetsRequestRequestTypeDef
):
    pass


DescribeConnectionResponseTypeDef = TypedDict(
    "DescribeConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "Name": str,
        "Description": str,
        "ConnectionState": ConnectionStateType,
        "StateReason": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "SecretArn": str,
        "AuthParameters": ConnectionAuthResponseParametersTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "AuthParameters": CreateConnectionAuthRequestParametersTypeDef,
    },
)
_OptionalCreateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreateConnectionRequestRequestTypeDef(
    _RequiredCreateConnectionRequestRequestTypeDef, _OptionalCreateConnectionRequestRequestTypeDef
):
    pass


_RequiredUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestRequestTypeDef",
    {
        "Description": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "AuthParameters": UpdateConnectionAuthRequestParametersTypeDef,
    },
    total=False,
)


class UpdateConnectionRequestRequestTypeDef(
    _RequiredUpdateConnectionRequestRequestTypeDef, _OptionalUpdateConnectionRequestRequestTypeDef
):
    pass


ListEndpointsResponseTypeDef = TypedDict(
    "ListEndpointsResponseTypeDef",
    {
        "Endpoints": List[EndpointTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
