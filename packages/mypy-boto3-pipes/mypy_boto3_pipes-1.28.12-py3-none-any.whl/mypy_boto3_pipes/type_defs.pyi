"""
Type annotations for pipes service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pipes/type_defs/)

Usage::

    ```python
    from mypy_boto3_pipes.type_defs import AwsVpcConfigurationOutputTypeDef

    data: AwsVpcConfigurationOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AssignPublicIpType,
    BatchJobDependencyTypeType,
    BatchResourceRequirementTypeType,
    DynamoDBStreamStartPositionType,
    EcsResourceRequirementTypeType,
    KinesisStreamStartPositionType,
    LaunchTypeType,
    MSKStartPositionType,
    PipeStateType,
    PipeTargetInvocationTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    RequestedPipeStateDescribeResponseType,
    RequestedPipeStateType,
    SelfManagedKafkaStartPositionType,
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
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesOutputTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchEnvironmentVariableOutputTypeDef",
    "BatchResourceRequirementOutputTypeDef",
    "BatchEnvironmentVariableTypeDef",
    "BatchResourceRequirementTypeDef",
    "BatchJobDependencyOutputTypeDef",
    "BatchJobDependencyTypeDef",
    "BatchRetryStrategyOutputTypeDef",
    "BatchRetryStrategyTypeDef",
    "CapacityProviderStrategyItemOutputTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "ResponseMetadataTypeDef",
    "DeadLetterConfigOutputTypeDef",
    "DeadLetterConfigTypeDef",
    "DeletePipeRequestRequestTypeDef",
    "DescribePipeRequestRequestTypeDef",
    "EcsEnvironmentFileOutputTypeDef",
    "EcsEnvironmentVariableOutputTypeDef",
    "EcsResourceRequirementOutputTypeDef",
    "EcsEnvironmentFileTypeDef",
    "EcsEnvironmentVariableTypeDef",
    "EcsResourceRequirementTypeDef",
    "EcsEphemeralStorageOutputTypeDef",
    "EcsEphemeralStorageTypeDef",
    "EcsInferenceAcceleratorOverrideOutputTypeDef",
    "EcsInferenceAcceleratorOverrideTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "ListPipesRequestRequestTypeDef",
    "PipeTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MQBrokerAccessCredentialsOutputTypeDef",
    "MQBrokerAccessCredentialsTypeDef",
    "MSKAccessCredentialsOutputTypeDef",
    "MSKAccessCredentialsTypeDef",
    "PipeEnrichmentHttpParametersOutputTypeDef",
    "PipeEnrichmentHttpParametersTypeDef",
    "PipeSourceSqsQueueParametersOutputTypeDef",
    "PipeSourceSqsQueueParametersTypeDef",
    "SelfManagedKafkaAccessConfigurationCredentialsOutputTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcOutputTypeDef",
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    "PipeTargetCloudWatchLogsParametersOutputTypeDef",
    "PipeTargetCloudWatchLogsParametersTypeDef",
    "PlacementConstraintOutputTypeDef",
    "PlacementStrategyOutputTypeDef",
    "TagOutputTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "TagTypeDef",
    "PipeTargetEventBridgeEventBusParametersOutputTypeDef",
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    "PipeTargetHttpParametersOutputTypeDef",
    "PipeTargetHttpParametersTypeDef",
    "PipeTargetKinesisStreamParametersOutputTypeDef",
    "PipeTargetKinesisStreamParametersTypeDef",
    "PipeTargetLambdaFunctionParametersOutputTypeDef",
    "PipeTargetLambdaFunctionParametersTypeDef",
    "PipeTargetRedshiftDataParametersOutputTypeDef",
    "PipeTargetSqsQueueParametersOutputTypeDef",
    "PipeTargetStateMachineParametersOutputTypeDef",
    "PipeTargetRedshiftDataParametersTypeDef",
    "PipeTargetSqsQueueParametersTypeDef",
    "PipeTargetStateMachineParametersTypeDef",
    "SageMakerPipelineParameterOutputTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "StartPipeRequestRequestTypeDef",
    "StopPipeRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePipeSourceSqsQueueParametersTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "BatchContainerOverridesOutputTypeDef",
    "BatchContainerOverridesTypeDef",
    "CreatePipeResponseTypeDef",
    "DeletePipeResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartPipeResponseTypeDef",
    "StopPipeResponseTypeDef",
    "UpdatePipeResponseTypeDef",
    "PipeSourceDynamoDBStreamParametersOutputTypeDef",
    "PipeSourceKinesisStreamParametersOutputTypeDef",
    "PipeSourceDynamoDBStreamParametersTypeDef",
    "PipeSourceKinesisStreamParametersTypeDef",
    "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    "EcsContainerOverrideOutputTypeDef",
    "EcsContainerOverrideTypeDef",
    "FilterCriteriaOutputTypeDef",
    "FilterCriteriaTypeDef",
    "ListPipesRequestListPipesPaginateTypeDef",
    "ListPipesResponseTypeDef",
    "PipeSourceActiveMQBrokerParametersOutputTypeDef",
    "PipeSourceRabbitMQBrokerParametersOutputTypeDef",
    "PipeSourceActiveMQBrokerParametersTypeDef",
    "PipeSourceRabbitMQBrokerParametersTypeDef",
    "UpdatePipeSourceActiveMQBrokerParametersTypeDef",
    "UpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    "PipeSourceManagedStreamingKafkaParametersOutputTypeDef",
    "PipeSourceManagedStreamingKafkaParametersTypeDef",
    "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
    "PipeEnrichmentParametersOutputTypeDef",
    "PipeEnrichmentParametersTypeDef",
    "PipeSourceSelfManagedKafkaParametersOutputTypeDef",
    "PipeSourceSelfManagedKafkaParametersTypeDef",
    "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    "PipeTargetSageMakerPipelineParametersOutputTypeDef",
    "PipeTargetSageMakerPipelineParametersTypeDef",
    "PipeTargetBatchJobParametersOutputTypeDef",
    "PipeTargetBatchJobParametersTypeDef",
    "EcsTaskOverrideOutputTypeDef",
    "EcsTaskOverrideTypeDef",
    "PipeSourceParametersOutputTypeDef",
    "PipeSourceParametersTypeDef",
    "UpdatePipeSourceParametersTypeDef",
    "PipeTargetEcsTaskParametersOutputTypeDef",
    "PipeTargetEcsTaskParametersTypeDef",
    "PipeTargetParametersOutputTypeDef",
    "PipeTargetParametersTypeDef",
    "DescribePipeResponseTypeDef",
    "CreatePipeRequestRequestTypeDef",
    "UpdatePipeRequestRequestTypeDef",
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
        "AssignPublicIp": AssignPublicIpType,
        "SecurityGroups": List[str],
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
        "AssignPublicIp": AssignPublicIpType,
        "SecurityGroups": Sequence[str],
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

BatchEnvironmentVariableOutputTypeDef = TypedDict(
    "BatchEnvironmentVariableOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

BatchResourceRequirementOutputTypeDef = TypedDict(
    "BatchResourceRequirementOutputTypeDef",
    {
        "Type": BatchResourceRequirementTypeType,
        "Value": str,
    },
)

BatchEnvironmentVariableTypeDef = TypedDict(
    "BatchEnvironmentVariableTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

BatchResourceRequirementTypeDef = TypedDict(
    "BatchResourceRequirementTypeDef",
    {
        "Type": BatchResourceRequirementTypeType,
        "Value": str,
    },
)

BatchJobDependencyOutputTypeDef = TypedDict(
    "BatchJobDependencyOutputTypeDef",
    {
        "JobId": str,
        "Type": BatchJobDependencyTypeType,
    },
    total=False,
)

BatchJobDependencyTypeDef = TypedDict(
    "BatchJobDependencyTypeDef",
    {
        "JobId": str,
        "Type": BatchJobDependencyTypeType,
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

_RequiredCapacityProviderStrategyItemOutputTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemOutputTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemOutputTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemOutputTypeDef",
    {
        "base": int,
        "weight": int,
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
        "base": int,
        "weight": int,
    },
    total=False,
)

class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
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

DeletePipeRequestRequestTypeDef = TypedDict(
    "DeletePipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribePipeRequestRequestTypeDef = TypedDict(
    "DescribePipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

EcsEnvironmentFileOutputTypeDef = TypedDict(
    "EcsEnvironmentFileOutputTypeDef",
    {
        "type": Literal["s3"],
        "value": str,
    },
)

EcsEnvironmentVariableOutputTypeDef = TypedDict(
    "EcsEnvironmentVariableOutputTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

EcsResourceRequirementOutputTypeDef = TypedDict(
    "EcsResourceRequirementOutputTypeDef",
    {
        "type": EcsResourceRequirementTypeType,
        "value": str,
    },
)

EcsEnvironmentFileTypeDef = TypedDict(
    "EcsEnvironmentFileTypeDef",
    {
        "type": Literal["s3"],
        "value": str,
    },
)

EcsEnvironmentVariableTypeDef = TypedDict(
    "EcsEnvironmentVariableTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

EcsResourceRequirementTypeDef = TypedDict(
    "EcsResourceRequirementTypeDef",
    {
        "type": EcsResourceRequirementTypeType,
        "value": str,
    },
)

EcsEphemeralStorageOutputTypeDef = TypedDict(
    "EcsEphemeralStorageOutputTypeDef",
    {
        "sizeInGiB": int,
    },
)

EcsEphemeralStorageTypeDef = TypedDict(
    "EcsEphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

EcsInferenceAcceleratorOverrideOutputTypeDef = TypedDict(
    "EcsInferenceAcceleratorOverrideOutputTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
    total=False,
)

EcsInferenceAcceleratorOverrideTypeDef = TypedDict(
    "EcsInferenceAcceleratorOverrideTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
    total=False,
)

FilterOutputTypeDef = TypedDict(
    "FilterOutputTypeDef",
    {
        "Pattern": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Pattern": str,
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

ListPipesRequestRequestTypeDef = TypedDict(
    "ListPipesRequestRequestTypeDef",
    {
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "Limit": int,
        "NamePrefix": str,
        "NextToken": str,
        "SourcePrefix": str,
        "TargetPrefix": str,
    },
    total=False,
)

PipeTypeDef = TypedDict(
    "PipeTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "Enrichment": str,
        "LastModifiedTime": datetime,
        "Name": str,
        "Source": str,
        "StateReason": str,
        "Target": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

MQBrokerAccessCredentialsOutputTypeDef = TypedDict(
    "MQBrokerAccessCredentialsOutputTypeDef",
    {
        "BasicAuth": str,
    },
    total=False,
)

MQBrokerAccessCredentialsTypeDef = TypedDict(
    "MQBrokerAccessCredentialsTypeDef",
    {
        "BasicAuth": str,
    },
    total=False,
)

MSKAccessCredentialsOutputTypeDef = TypedDict(
    "MSKAccessCredentialsOutputTypeDef",
    {
        "ClientCertificateTlsAuth": str,
        "SaslScram512Auth": str,
    },
    total=False,
)

MSKAccessCredentialsTypeDef = TypedDict(
    "MSKAccessCredentialsTypeDef",
    {
        "ClientCertificateTlsAuth": str,
        "SaslScram512Auth": str,
    },
    total=False,
)

PipeEnrichmentHttpParametersOutputTypeDef = TypedDict(
    "PipeEnrichmentHttpParametersOutputTypeDef",
    {
        "HeaderParameters": Dict[str, str],
        "PathParameterValues": List[str],
        "QueryStringParameters": Dict[str, str],
    },
    total=False,
)

PipeEnrichmentHttpParametersTypeDef = TypedDict(
    "PipeEnrichmentHttpParametersTypeDef",
    {
        "HeaderParameters": Mapping[str, str],
        "PathParameterValues": Sequence[str],
        "QueryStringParameters": Mapping[str, str],
    },
    total=False,
)

PipeSourceSqsQueueParametersOutputTypeDef = TypedDict(
    "PipeSourceSqsQueueParametersOutputTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

PipeSourceSqsQueueParametersTypeDef = TypedDict(
    "PipeSourceSqsQueueParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

SelfManagedKafkaAccessConfigurationCredentialsOutputTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationCredentialsOutputTypeDef",
    {
        "BasicAuth": str,
        "ClientCertificateTlsAuth": str,
        "SaslScram256Auth": str,
        "SaslScram512Auth": str,
    },
    total=False,
)

SelfManagedKafkaAccessConfigurationVpcOutputTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationVpcOutputTypeDef",
    {
        "SecurityGroup": List[str],
        "Subnets": List[str],
    },
    total=False,
)

SelfManagedKafkaAccessConfigurationCredentialsTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    {
        "BasicAuth": str,
        "ClientCertificateTlsAuth": str,
        "SaslScram256Auth": str,
        "SaslScram512Auth": str,
    },
    total=False,
)

SelfManagedKafkaAccessConfigurationVpcTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    {
        "SecurityGroup": Sequence[str],
        "Subnets": Sequence[str],
    },
    total=False,
)

PipeTargetCloudWatchLogsParametersOutputTypeDef = TypedDict(
    "PipeTargetCloudWatchLogsParametersOutputTypeDef",
    {
        "LogStreamName": str,
        "Timestamp": str,
    },
    total=False,
)

PipeTargetCloudWatchLogsParametersTypeDef = TypedDict(
    "PipeTargetCloudWatchLogsParametersTypeDef",
    {
        "LogStreamName": str,
        "Timestamp": str,
    },
    total=False,
)

PlacementConstraintOutputTypeDef = TypedDict(
    "PlacementConstraintOutputTypeDef",
    {
        "expression": str,
        "type": PlacementConstraintTypeType,
    },
    total=False,
)

PlacementStrategyOutputTypeDef = TypedDict(
    "PlacementStrategyOutputTypeDef",
    {
        "field": str,
        "type": PlacementStrategyTypeType,
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
        "expression": str,
        "type": PlacementConstraintTypeType,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "field": str,
        "type": PlacementStrategyTypeType,
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

PipeTargetEventBridgeEventBusParametersOutputTypeDef = TypedDict(
    "PipeTargetEventBridgeEventBusParametersOutputTypeDef",
    {
        "DetailType": str,
        "EndpointId": str,
        "Resources": List[str],
        "Source": str,
        "Time": str,
    },
    total=False,
)

PipeTargetEventBridgeEventBusParametersTypeDef = TypedDict(
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    {
        "DetailType": str,
        "EndpointId": str,
        "Resources": Sequence[str],
        "Source": str,
        "Time": str,
    },
    total=False,
)

PipeTargetHttpParametersOutputTypeDef = TypedDict(
    "PipeTargetHttpParametersOutputTypeDef",
    {
        "HeaderParameters": Dict[str, str],
        "PathParameterValues": List[str],
        "QueryStringParameters": Dict[str, str],
    },
    total=False,
)

PipeTargetHttpParametersTypeDef = TypedDict(
    "PipeTargetHttpParametersTypeDef",
    {
        "HeaderParameters": Mapping[str, str],
        "PathParameterValues": Sequence[str],
        "QueryStringParameters": Mapping[str, str],
    },
    total=False,
)

PipeTargetKinesisStreamParametersOutputTypeDef = TypedDict(
    "PipeTargetKinesisStreamParametersOutputTypeDef",
    {
        "PartitionKey": str,
    },
)

PipeTargetKinesisStreamParametersTypeDef = TypedDict(
    "PipeTargetKinesisStreamParametersTypeDef",
    {
        "PartitionKey": str,
    },
)

PipeTargetLambdaFunctionParametersOutputTypeDef = TypedDict(
    "PipeTargetLambdaFunctionParametersOutputTypeDef",
    {
        "InvocationType": PipeTargetInvocationTypeType,
    },
    total=False,
)

PipeTargetLambdaFunctionParametersTypeDef = TypedDict(
    "PipeTargetLambdaFunctionParametersTypeDef",
    {
        "InvocationType": PipeTargetInvocationTypeType,
    },
    total=False,
)

_RequiredPipeTargetRedshiftDataParametersOutputTypeDef = TypedDict(
    "_RequiredPipeTargetRedshiftDataParametersOutputTypeDef",
    {
        "Database": str,
        "Sqls": List[str],
    },
)
_OptionalPipeTargetRedshiftDataParametersOutputTypeDef = TypedDict(
    "_OptionalPipeTargetRedshiftDataParametersOutputTypeDef",
    {
        "DbUser": str,
        "SecretManagerArn": str,
        "StatementName": str,
        "WithEvent": bool,
    },
    total=False,
)

class PipeTargetRedshiftDataParametersOutputTypeDef(
    _RequiredPipeTargetRedshiftDataParametersOutputTypeDef,
    _OptionalPipeTargetRedshiftDataParametersOutputTypeDef,
):
    pass

PipeTargetSqsQueueParametersOutputTypeDef = TypedDict(
    "PipeTargetSqsQueueParametersOutputTypeDef",
    {
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)

PipeTargetStateMachineParametersOutputTypeDef = TypedDict(
    "PipeTargetStateMachineParametersOutputTypeDef",
    {
        "InvocationType": PipeTargetInvocationTypeType,
    },
    total=False,
)

_RequiredPipeTargetRedshiftDataParametersTypeDef = TypedDict(
    "_RequiredPipeTargetRedshiftDataParametersTypeDef",
    {
        "Database": str,
        "Sqls": Sequence[str],
    },
)
_OptionalPipeTargetRedshiftDataParametersTypeDef = TypedDict(
    "_OptionalPipeTargetRedshiftDataParametersTypeDef",
    {
        "DbUser": str,
        "SecretManagerArn": str,
        "StatementName": str,
        "WithEvent": bool,
    },
    total=False,
)

class PipeTargetRedshiftDataParametersTypeDef(
    _RequiredPipeTargetRedshiftDataParametersTypeDef,
    _OptionalPipeTargetRedshiftDataParametersTypeDef,
):
    pass

PipeTargetSqsQueueParametersTypeDef = TypedDict(
    "PipeTargetSqsQueueParametersTypeDef",
    {
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)

PipeTargetStateMachineParametersTypeDef = TypedDict(
    "PipeTargetStateMachineParametersTypeDef",
    {
        "InvocationType": PipeTargetInvocationTypeType,
    },
    total=False,
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

StartPipeRequestRequestTypeDef = TypedDict(
    "StartPipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopPipeRequestRequestTypeDef = TypedDict(
    "StopPipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

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

UpdatePipeSourceSqsQueueParametersTypeDef = TypedDict(
    "UpdatePipeSourceSqsQueueParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
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

BatchContainerOverridesOutputTypeDef = TypedDict(
    "BatchContainerOverridesOutputTypeDef",
    {
        "Command": List[str],
        "Environment": List[BatchEnvironmentVariableOutputTypeDef],
        "InstanceType": str,
        "ResourceRequirements": List[BatchResourceRequirementOutputTypeDef],
    },
    total=False,
)

BatchContainerOverridesTypeDef = TypedDict(
    "BatchContainerOverridesTypeDef",
    {
        "Command": Sequence[str],
        "Environment": Sequence[BatchEnvironmentVariableTypeDef],
        "InstanceType": str,
        "ResourceRequirements": Sequence[BatchResourceRequirementTypeDef],
    },
    total=False,
)

CreatePipeResponseTypeDef = TypedDict(
    "CreatePipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeletePipeResponseTypeDef = TypedDict(
    "DeletePipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "LastModifiedTime": datetime,
        "Name": str,
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

StartPipeResponseTypeDef = TypedDict(
    "StartPipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopPipeResponseTypeDef = TypedDict(
    "StopPipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePipeResponseTypeDef = TypedDict(
    "UpdatePipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredPipeSourceDynamoDBStreamParametersOutputTypeDef = TypedDict(
    "_RequiredPipeSourceDynamoDBStreamParametersOutputTypeDef",
    {
        "StartingPosition": DynamoDBStreamStartPositionType,
    },
)
_OptionalPipeSourceDynamoDBStreamParametersOutputTypeDef = TypedDict(
    "_OptionalPipeSourceDynamoDBStreamParametersOutputTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": DeadLetterConfigOutputTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "ParallelizationFactor": int,
    },
    total=False,
)

class PipeSourceDynamoDBStreamParametersOutputTypeDef(
    _RequiredPipeSourceDynamoDBStreamParametersOutputTypeDef,
    _OptionalPipeSourceDynamoDBStreamParametersOutputTypeDef,
):
    pass

_RequiredPipeSourceKinesisStreamParametersOutputTypeDef = TypedDict(
    "_RequiredPipeSourceKinesisStreamParametersOutputTypeDef",
    {
        "StartingPosition": KinesisStreamStartPositionType,
    },
)
_OptionalPipeSourceKinesisStreamParametersOutputTypeDef = TypedDict(
    "_OptionalPipeSourceKinesisStreamParametersOutputTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": DeadLetterConfigOutputTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "ParallelizationFactor": int,
        "StartingPositionTimestamp": datetime,
    },
    total=False,
)

class PipeSourceKinesisStreamParametersOutputTypeDef(
    _RequiredPipeSourceKinesisStreamParametersOutputTypeDef,
    _OptionalPipeSourceKinesisStreamParametersOutputTypeDef,
):
    pass

_RequiredPipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "_RequiredPipeSourceDynamoDBStreamParametersTypeDef",
    {
        "StartingPosition": DynamoDBStreamStartPositionType,
    },
)
_OptionalPipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "_OptionalPipeSourceDynamoDBStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "ParallelizationFactor": int,
    },
    total=False,
)

class PipeSourceDynamoDBStreamParametersTypeDef(
    _RequiredPipeSourceDynamoDBStreamParametersTypeDef,
    _OptionalPipeSourceDynamoDBStreamParametersTypeDef,
):
    pass

_RequiredPipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "_RequiredPipeSourceKinesisStreamParametersTypeDef",
    {
        "StartingPosition": KinesisStreamStartPositionType,
    },
)
_OptionalPipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "_OptionalPipeSourceKinesisStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "ParallelizationFactor": int,
        "StartingPositionTimestamp": Union[datetime, str],
    },
    total=False,
)

class PipeSourceKinesisStreamParametersTypeDef(
    _RequiredPipeSourceKinesisStreamParametersTypeDef,
    _OptionalPipeSourceKinesisStreamParametersTypeDef,
):
    pass

UpdatePipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "ParallelizationFactor": int,
    },
    total=False,
)

UpdatePipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": DeadLetterConfigTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "ParallelizationFactor": int,
    },
    total=False,
)

EcsContainerOverrideOutputTypeDef = TypedDict(
    "EcsContainerOverrideOutputTypeDef",
    {
        "Command": List[str],
        "Cpu": int,
        "Environment": List[EcsEnvironmentVariableOutputTypeDef],
        "EnvironmentFiles": List[EcsEnvironmentFileOutputTypeDef],
        "Memory": int,
        "MemoryReservation": int,
        "Name": str,
        "ResourceRequirements": List[EcsResourceRequirementOutputTypeDef],
    },
    total=False,
)

EcsContainerOverrideTypeDef = TypedDict(
    "EcsContainerOverrideTypeDef",
    {
        "Command": Sequence[str],
        "Cpu": int,
        "Environment": Sequence[EcsEnvironmentVariableTypeDef],
        "EnvironmentFiles": Sequence[EcsEnvironmentFileTypeDef],
        "Memory": int,
        "MemoryReservation": int,
        "Name": str,
        "ResourceRequirements": Sequence[EcsResourceRequirementTypeDef],
    },
    total=False,
)

FilterCriteriaOutputTypeDef = TypedDict(
    "FilterCriteriaOutputTypeDef",
    {
        "Filters": List[FilterOutputTypeDef],
    },
    total=False,
)

FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
    },
    total=False,
)

ListPipesRequestListPipesPaginateTypeDef = TypedDict(
    "ListPipesRequestListPipesPaginateTypeDef",
    {
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "NamePrefix": str,
        "SourcePrefix": str,
        "TargetPrefix": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPipesResponseTypeDef = TypedDict(
    "ListPipesResponseTypeDef",
    {
        "NextToken": str,
        "Pipes": List[PipeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredPipeSourceActiveMQBrokerParametersOutputTypeDef = TypedDict(
    "_RequiredPipeSourceActiveMQBrokerParametersOutputTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsOutputTypeDef,
        "QueueName": str,
    },
)
_OptionalPipeSourceActiveMQBrokerParametersOutputTypeDef = TypedDict(
    "_OptionalPipeSourceActiveMQBrokerParametersOutputTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

class PipeSourceActiveMQBrokerParametersOutputTypeDef(
    _RequiredPipeSourceActiveMQBrokerParametersOutputTypeDef,
    _OptionalPipeSourceActiveMQBrokerParametersOutputTypeDef,
):
    pass

_RequiredPipeSourceRabbitMQBrokerParametersOutputTypeDef = TypedDict(
    "_RequiredPipeSourceRabbitMQBrokerParametersOutputTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsOutputTypeDef,
        "QueueName": str,
    },
)
_OptionalPipeSourceRabbitMQBrokerParametersOutputTypeDef = TypedDict(
    "_OptionalPipeSourceRabbitMQBrokerParametersOutputTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "VirtualHost": str,
    },
    total=False,
)

class PipeSourceRabbitMQBrokerParametersOutputTypeDef(
    _RequiredPipeSourceRabbitMQBrokerParametersOutputTypeDef,
    _OptionalPipeSourceRabbitMQBrokerParametersOutputTypeDef,
):
    pass

_RequiredPipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "_RequiredPipeSourceActiveMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "QueueName": str,
    },
)
_OptionalPipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "_OptionalPipeSourceActiveMQBrokerParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

class PipeSourceActiveMQBrokerParametersTypeDef(
    _RequiredPipeSourceActiveMQBrokerParametersTypeDef,
    _OptionalPipeSourceActiveMQBrokerParametersTypeDef,
):
    pass

_RequiredPipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "_RequiredPipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
        "QueueName": str,
    },
)
_OptionalPipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "_OptionalPipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "VirtualHost": str,
    },
    total=False,
)

class PipeSourceRabbitMQBrokerParametersTypeDef(
    _RequiredPipeSourceRabbitMQBrokerParametersTypeDef,
    _OptionalPipeSourceRabbitMQBrokerParametersTypeDef,
):
    pass

_RequiredUpdatePipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "_RequiredUpdatePipeSourceActiveMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
    },
)
_OptionalUpdatePipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "_OptionalUpdatePipeSourceActiveMQBrokerParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

class UpdatePipeSourceActiveMQBrokerParametersTypeDef(
    _RequiredUpdatePipeSourceActiveMQBrokerParametersTypeDef,
    _OptionalUpdatePipeSourceActiveMQBrokerParametersTypeDef,
):
    pass

_RequiredUpdatePipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "_RequiredUpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "Credentials": MQBrokerAccessCredentialsTypeDef,
    },
)
_OptionalUpdatePipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "_OptionalUpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

class UpdatePipeSourceRabbitMQBrokerParametersTypeDef(
    _RequiredUpdatePipeSourceRabbitMQBrokerParametersTypeDef,
    _OptionalUpdatePipeSourceRabbitMQBrokerParametersTypeDef,
):
    pass

_RequiredPipeSourceManagedStreamingKafkaParametersOutputTypeDef = TypedDict(
    "_RequiredPipeSourceManagedStreamingKafkaParametersOutputTypeDef",
    {
        "TopicName": str,
    },
)
_OptionalPipeSourceManagedStreamingKafkaParametersOutputTypeDef = TypedDict(
    "_OptionalPipeSourceManagedStreamingKafkaParametersOutputTypeDef",
    {
        "BatchSize": int,
        "ConsumerGroupID": str,
        "Credentials": MSKAccessCredentialsOutputTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "StartingPosition": MSKStartPositionType,
    },
    total=False,
)

class PipeSourceManagedStreamingKafkaParametersOutputTypeDef(
    _RequiredPipeSourceManagedStreamingKafkaParametersOutputTypeDef,
    _OptionalPipeSourceManagedStreamingKafkaParametersOutputTypeDef,
):
    pass

_RequiredPipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "_RequiredPipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "TopicName": str,
    },
)
_OptionalPipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "_OptionalPipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "BatchSize": int,
        "ConsumerGroupID": str,
        "Credentials": MSKAccessCredentialsTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "StartingPosition": MSKStartPositionType,
    },
    total=False,
)

class PipeSourceManagedStreamingKafkaParametersTypeDef(
    _RequiredPipeSourceManagedStreamingKafkaParametersTypeDef,
    _OptionalPipeSourceManagedStreamingKafkaParametersTypeDef,
):
    pass

UpdatePipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "BatchSize": int,
        "Credentials": MSKAccessCredentialsTypeDef,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

PipeEnrichmentParametersOutputTypeDef = TypedDict(
    "PipeEnrichmentParametersOutputTypeDef",
    {
        "HttpParameters": PipeEnrichmentHttpParametersOutputTypeDef,
        "InputTemplate": str,
    },
    total=False,
)

PipeEnrichmentParametersTypeDef = TypedDict(
    "PipeEnrichmentParametersTypeDef",
    {
        "HttpParameters": PipeEnrichmentHttpParametersTypeDef,
        "InputTemplate": str,
    },
    total=False,
)

_RequiredPipeSourceSelfManagedKafkaParametersOutputTypeDef = TypedDict(
    "_RequiredPipeSourceSelfManagedKafkaParametersOutputTypeDef",
    {
        "TopicName": str,
    },
)
_OptionalPipeSourceSelfManagedKafkaParametersOutputTypeDef = TypedDict(
    "_OptionalPipeSourceSelfManagedKafkaParametersOutputTypeDef",
    {
        "AdditionalBootstrapServers": List[str],
        "BatchSize": int,
        "ConsumerGroupID": str,
        "Credentials": SelfManagedKafkaAccessConfigurationCredentialsOutputTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "ServerRootCaCertificate": str,
        "StartingPosition": SelfManagedKafkaStartPositionType,
        "Vpc": SelfManagedKafkaAccessConfigurationVpcOutputTypeDef,
    },
    total=False,
)

class PipeSourceSelfManagedKafkaParametersOutputTypeDef(
    _RequiredPipeSourceSelfManagedKafkaParametersOutputTypeDef,
    _OptionalPipeSourceSelfManagedKafkaParametersOutputTypeDef,
):
    pass

_RequiredPipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "_RequiredPipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "TopicName": str,
    },
)
_OptionalPipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "_OptionalPipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "AdditionalBootstrapServers": Sequence[str],
        "BatchSize": int,
        "ConsumerGroupID": str,
        "Credentials": SelfManagedKafkaAccessConfigurationCredentialsTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "ServerRootCaCertificate": str,
        "StartingPosition": SelfManagedKafkaStartPositionType,
        "Vpc": SelfManagedKafkaAccessConfigurationVpcTypeDef,
    },
    total=False,
)

class PipeSourceSelfManagedKafkaParametersTypeDef(
    _RequiredPipeSourceSelfManagedKafkaParametersTypeDef,
    _OptionalPipeSourceSelfManagedKafkaParametersTypeDef,
):
    pass

UpdatePipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "BatchSize": int,
        "Credentials": SelfManagedKafkaAccessConfigurationCredentialsTypeDef,
        "MaximumBatchingWindowInSeconds": int,
        "ServerRootCaCertificate": str,
        "Vpc": SelfManagedKafkaAccessConfigurationVpcTypeDef,
    },
    total=False,
)

PipeTargetSageMakerPipelineParametersOutputTypeDef = TypedDict(
    "PipeTargetSageMakerPipelineParametersOutputTypeDef",
    {
        "PipelineParameterList": List[SageMakerPipelineParameterOutputTypeDef],
    },
    total=False,
)

PipeTargetSageMakerPipelineParametersTypeDef = TypedDict(
    "PipeTargetSageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": Sequence[SageMakerPipelineParameterTypeDef],
    },
    total=False,
)

_RequiredPipeTargetBatchJobParametersOutputTypeDef = TypedDict(
    "_RequiredPipeTargetBatchJobParametersOutputTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
    },
)
_OptionalPipeTargetBatchJobParametersOutputTypeDef = TypedDict(
    "_OptionalPipeTargetBatchJobParametersOutputTypeDef",
    {
        "ArrayProperties": BatchArrayPropertiesOutputTypeDef,
        "ContainerOverrides": BatchContainerOverridesOutputTypeDef,
        "DependsOn": List[BatchJobDependencyOutputTypeDef],
        "Parameters": Dict[str, str],
        "RetryStrategy": BatchRetryStrategyOutputTypeDef,
    },
    total=False,
)

class PipeTargetBatchJobParametersOutputTypeDef(
    _RequiredPipeTargetBatchJobParametersOutputTypeDef,
    _OptionalPipeTargetBatchJobParametersOutputTypeDef,
):
    pass

_RequiredPipeTargetBatchJobParametersTypeDef = TypedDict(
    "_RequiredPipeTargetBatchJobParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
    },
)
_OptionalPipeTargetBatchJobParametersTypeDef = TypedDict(
    "_OptionalPipeTargetBatchJobParametersTypeDef",
    {
        "ArrayProperties": BatchArrayPropertiesTypeDef,
        "ContainerOverrides": BatchContainerOverridesTypeDef,
        "DependsOn": Sequence[BatchJobDependencyTypeDef],
        "Parameters": Mapping[str, str],
        "RetryStrategy": BatchRetryStrategyTypeDef,
    },
    total=False,
)

class PipeTargetBatchJobParametersTypeDef(
    _RequiredPipeTargetBatchJobParametersTypeDef, _OptionalPipeTargetBatchJobParametersTypeDef
):
    pass

EcsTaskOverrideOutputTypeDef = TypedDict(
    "EcsTaskOverrideOutputTypeDef",
    {
        "ContainerOverrides": List[EcsContainerOverrideOutputTypeDef],
        "Cpu": str,
        "EphemeralStorage": EcsEphemeralStorageOutputTypeDef,
        "ExecutionRoleArn": str,
        "InferenceAcceleratorOverrides": List[EcsInferenceAcceleratorOverrideOutputTypeDef],
        "Memory": str,
        "TaskRoleArn": str,
    },
    total=False,
)

EcsTaskOverrideTypeDef = TypedDict(
    "EcsTaskOverrideTypeDef",
    {
        "ContainerOverrides": Sequence[EcsContainerOverrideTypeDef],
        "Cpu": str,
        "EphemeralStorage": EcsEphemeralStorageTypeDef,
        "ExecutionRoleArn": str,
        "InferenceAcceleratorOverrides": Sequence[EcsInferenceAcceleratorOverrideTypeDef],
        "Memory": str,
        "TaskRoleArn": str,
    },
    total=False,
)

PipeSourceParametersOutputTypeDef = TypedDict(
    "PipeSourceParametersOutputTypeDef",
    {
        "ActiveMQBrokerParameters": PipeSourceActiveMQBrokerParametersOutputTypeDef,
        "DynamoDBStreamParameters": PipeSourceDynamoDBStreamParametersOutputTypeDef,
        "FilterCriteria": FilterCriteriaOutputTypeDef,
        "KinesisStreamParameters": PipeSourceKinesisStreamParametersOutputTypeDef,
        "ManagedStreamingKafkaParameters": PipeSourceManagedStreamingKafkaParametersOutputTypeDef,
        "RabbitMQBrokerParameters": PipeSourceRabbitMQBrokerParametersOutputTypeDef,
        "SelfManagedKafkaParameters": PipeSourceSelfManagedKafkaParametersOutputTypeDef,
        "SqsQueueParameters": PipeSourceSqsQueueParametersOutputTypeDef,
    },
    total=False,
)

PipeSourceParametersTypeDef = TypedDict(
    "PipeSourceParametersTypeDef",
    {
        "ActiveMQBrokerParameters": PipeSourceActiveMQBrokerParametersTypeDef,
        "DynamoDBStreamParameters": PipeSourceDynamoDBStreamParametersTypeDef,
        "FilterCriteria": FilterCriteriaTypeDef,
        "KinesisStreamParameters": PipeSourceKinesisStreamParametersTypeDef,
        "ManagedStreamingKafkaParameters": PipeSourceManagedStreamingKafkaParametersTypeDef,
        "RabbitMQBrokerParameters": PipeSourceRabbitMQBrokerParametersTypeDef,
        "SelfManagedKafkaParameters": PipeSourceSelfManagedKafkaParametersTypeDef,
        "SqsQueueParameters": PipeSourceSqsQueueParametersTypeDef,
    },
    total=False,
)

UpdatePipeSourceParametersTypeDef = TypedDict(
    "UpdatePipeSourceParametersTypeDef",
    {
        "ActiveMQBrokerParameters": UpdatePipeSourceActiveMQBrokerParametersTypeDef,
        "DynamoDBStreamParameters": UpdatePipeSourceDynamoDBStreamParametersTypeDef,
        "FilterCriteria": FilterCriteriaTypeDef,
        "KinesisStreamParameters": UpdatePipeSourceKinesisStreamParametersTypeDef,
        "ManagedStreamingKafkaParameters": UpdatePipeSourceManagedStreamingKafkaParametersTypeDef,
        "RabbitMQBrokerParameters": UpdatePipeSourceRabbitMQBrokerParametersTypeDef,
        "SelfManagedKafkaParameters": UpdatePipeSourceSelfManagedKafkaParametersTypeDef,
        "SqsQueueParameters": UpdatePipeSourceSqsQueueParametersTypeDef,
    },
    total=False,
)

_RequiredPipeTargetEcsTaskParametersOutputTypeDef = TypedDict(
    "_RequiredPipeTargetEcsTaskParametersOutputTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalPipeTargetEcsTaskParametersOutputTypeDef = TypedDict(
    "_OptionalPipeTargetEcsTaskParametersOutputTypeDef",
    {
        "CapacityProviderStrategy": List[CapacityProviderStrategyItemOutputTypeDef],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "Group": str,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": NetworkConfigurationOutputTypeDef,
        "Overrides": EcsTaskOverrideOutputTypeDef,
        "PlacementConstraints": List[PlacementConstraintOutputTypeDef],
        "PlacementStrategy": List[PlacementStrategyOutputTypeDef],
        "PlatformVersion": str,
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": List[TagOutputTypeDef],
        "TaskCount": int,
    },
    total=False,
)

class PipeTargetEcsTaskParametersOutputTypeDef(
    _RequiredPipeTargetEcsTaskParametersOutputTypeDef,
    _OptionalPipeTargetEcsTaskParametersOutputTypeDef,
):
    pass

_RequiredPipeTargetEcsTaskParametersTypeDef = TypedDict(
    "_RequiredPipeTargetEcsTaskParametersTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalPipeTargetEcsTaskParametersTypeDef = TypedDict(
    "_OptionalPipeTargetEcsTaskParametersTypeDef",
    {
        "CapacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "Group": str,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "Overrides": EcsTaskOverrideTypeDef,
        "PlacementConstraints": Sequence[PlacementConstraintTypeDef],
        "PlacementStrategy": Sequence[PlacementStrategyTypeDef],
        "PlatformVersion": str,
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": Sequence[TagTypeDef],
        "TaskCount": int,
    },
    total=False,
)

class PipeTargetEcsTaskParametersTypeDef(
    _RequiredPipeTargetEcsTaskParametersTypeDef, _OptionalPipeTargetEcsTaskParametersTypeDef
):
    pass

PipeTargetParametersOutputTypeDef = TypedDict(
    "PipeTargetParametersOutputTypeDef",
    {
        "BatchJobParameters": PipeTargetBatchJobParametersOutputTypeDef,
        "CloudWatchLogsParameters": PipeTargetCloudWatchLogsParametersOutputTypeDef,
        "EcsTaskParameters": PipeTargetEcsTaskParametersOutputTypeDef,
        "EventBridgeEventBusParameters": PipeTargetEventBridgeEventBusParametersOutputTypeDef,
        "HttpParameters": PipeTargetHttpParametersOutputTypeDef,
        "InputTemplate": str,
        "KinesisStreamParameters": PipeTargetKinesisStreamParametersOutputTypeDef,
        "LambdaFunctionParameters": PipeTargetLambdaFunctionParametersOutputTypeDef,
        "RedshiftDataParameters": PipeTargetRedshiftDataParametersOutputTypeDef,
        "SageMakerPipelineParameters": PipeTargetSageMakerPipelineParametersOutputTypeDef,
        "SqsQueueParameters": PipeTargetSqsQueueParametersOutputTypeDef,
        "StepFunctionStateMachineParameters": PipeTargetStateMachineParametersOutputTypeDef,
    },
    total=False,
)

PipeTargetParametersTypeDef = TypedDict(
    "PipeTargetParametersTypeDef",
    {
        "BatchJobParameters": PipeTargetBatchJobParametersTypeDef,
        "CloudWatchLogsParameters": PipeTargetCloudWatchLogsParametersTypeDef,
        "EcsTaskParameters": PipeTargetEcsTaskParametersTypeDef,
        "EventBridgeEventBusParameters": PipeTargetEventBridgeEventBusParametersTypeDef,
        "HttpParameters": PipeTargetHttpParametersTypeDef,
        "InputTemplate": str,
        "KinesisStreamParameters": PipeTargetKinesisStreamParametersTypeDef,
        "LambdaFunctionParameters": PipeTargetLambdaFunctionParametersTypeDef,
        "RedshiftDataParameters": PipeTargetRedshiftDataParametersTypeDef,
        "SageMakerPipelineParameters": PipeTargetSageMakerPipelineParametersTypeDef,
        "SqsQueueParameters": PipeTargetSqsQueueParametersTypeDef,
        "StepFunctionStateMachineParameters": PipeTargetStateMachineParametersTypeDef,
    },
    total=False,
)

DescribePipeResponseTypeDef = TypedDict(
    "DescribePipeResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "Description": str,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "Enrichment": str,
        "EnrichmentParameters": PipeEnrichmentParametersOutputTypeDef,
        "LastModifiedTime": datetime,
        "Name": str,
        "RoleArn": str,
        "Source": str,
        "SourceParameters": PipeSourceParametersOutputTypeDef,
        "StateReason": str,
        "Tags": Dict[str, str],
        "Target": str,
        "TargetParameters": PipeTargetParametersOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreatePipeRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePipeRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Source": str,
        "Target": str,
    },
)
_OptionalCreatePipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePipeRequestRequestTypeDef",
    {
        "Description": str,
        "DesiredState": RequestedPipeStateType,
        "Enrichment": str,
        "EnrichmentParameters": PipeEnrichmentParametersTypeDef,
        "SourceParameters": PipeSourceParametersTypeDef,
        "Tags": Mapping[str, str],
        "TargetParameters": PipeTargetParametersTypeDef,
    },
    total=False,
)

class CreatePipeRequestRequestTypeDef(
    _RequiredCreatePipeRequestRequestTypeDef, _OptionalCreatePipeRequestRequestTypeDef
):
    pass

_RequiredUpdatePipeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePipeRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalUpdatePipeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePipeRequestRequestTypeDef",
    {
        "Description": str,
        "DesiredState": RequestedPipeStateType,
        "Enrichment": str,
        "EnrichmentParameters": PipeEnrichmentParametersTypeDef,
        "SourceParameters": UpdatePipeSourceParametersTypeDef,
        "Target": str,
        "TargetParameters": PipeTargetParametersTypeDef,
    },
    total=False,
)

class UpdatePipeRequestRequestTypeDef(
    _RequiredUpdatePipeRequestRequestTypeDef, _OptionalUpdatePipeRequestRequestTypeDef
):
    pass
