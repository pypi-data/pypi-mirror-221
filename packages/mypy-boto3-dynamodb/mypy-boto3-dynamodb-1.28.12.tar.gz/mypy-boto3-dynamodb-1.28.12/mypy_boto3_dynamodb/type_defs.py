"""
Type annotations for dynamodb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/type_defs/)

Usage::

    ```python
    from mypy_boto3_dynamodb.type_defs import ArchivalSummaryTableResponseMetadataTypeDef

    data: ArchivalSummaryTableResponseMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Mapping, Sequence, Set, Union

from boto3.dynamodb.conditions import ConditionBase

from .literals import (
    AttributeActionType,
    BackupStatusType,
    BackupTypeFilterType,
    BackupTypeType,
    BatchStatementErrorCodeEnumType,
    BillingModeType,
    ComparisonOperatorType,
    ConditionalOperatorType,
    ContinuousBackupsStatusType,
    ContributorInsightsActionType,
    ContributorInsightsStatusType,
    DestinationStatusType,
    ExportFormatType,
    ExportStatusType,
    GlobalTableStatusType,
    ImportStatusType,
    IndexStatusType,
    InputCompressionTypeType,
    InputFormatType,
    KeyTypeType,
    PointInTimeRecoveryStatusType,
    ProjectionTypeType,
    ReplicaStatusType,
    ReturnConsumedCapacityType,
    ReturnItemCollectionMetricsType,
    ReturnValuesOnConditionCheckFailureType,
    ReturnValueType,
    S3SseAlgorithmType,
    ScalarAttributeTypeType,
    SelectType,
    SSEStatusType,
    SSETypeType,
    StreamViewTypeType,
    TableClassType,
    TableStatusType,
    TimeToLiveStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArchivalSummaryTableResponseMetadataTypeDef",
    "ArchivalSummaryTableTypeDef",
    "ArchivalSummaryTypeDef",
    "AttributeDefinitionOutputTypeDef",
    "AttributeDefinitionServiceResourceTypeDef",
    "AttributeDefinitionTableOutputTypeDef",
    "AttributeDefinitionTableTypeDef",
    "AttributeDefinitionTypeDef",
    "AttributeValueServiceResourceTypeDef",
    "AttributeValueTableTypeDef",
    "AttributeValueTypeDef",
    "AttributeValueUpdateTableTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    "BackupDetailsTypeDef",
    "BackupSummaryTableTypeDef",
    "BackupSummaryTypeDef",
    "KeysAndAttributesServiceResourceTypeDef",
    "KeysAndAttributesServiceResourceOutputTypeDef",
    "ItemCollectionMetricsServiceResourceTypeDef",
    "BillingModeSummaryTableResponseMetadataTypeDef",
    "BillingModeSummaryTableTypeDef",
    "BillingModeSummaryTypeDef",
    "CapacityServiceResourceTypeDef",
    "CapacityTableTypeDef",
    "CapacityTypeDef",
    "ConditionTableTypeDef",
    "PointInTimeRecoveryDescriptionTypeDef",
    "ContributorInsightsSummaryTypeDef",
    "CreateBackupInputRequestTypeDef",
    "KeySchemaElementTableTypeDef",
    "ProjectionTableTypeDef",
    "ProvisionedThroughputTableTypeDef",
    "KeySchemaElementTypeDef",
    "ProjectionTypeDef",
    "ProvisionedThroughputTypeDef",
    "ReplicaTypeDef",
    "CreateReplicaActionTypeDef",
    "ProvisionedThroughputOverrideTableTypeDef",
    "ProvisionedThroughputOverrideTypeDef",
    "SSESpecificationTypeDef",
    "StreamSpecificationTypeDef",
    "TagTypeDef",
    "KeySchemaElementServiceResourceTypeDef",
    "ProvisionedThroughputServiceResourceTypeDef",
    "SSESpecificationServiceResourceTypeDef",
    "StreamSpecificationServiceResourceTypeDef",
    "TagServiceResourceTypeDef",
    "CsvOptionsOutputTypeDef",
    "CsvOptionsTypeDef",
    "DeleteBackupInputRequestTypeDef",
    "DeleteGlobalSecondaryIndexActionTableTypeDef",
    "DeleteGlobalSecondaryIndexActionTypeDef",
    "ExpectedAttributeValueTableTypeDef",
    "ItemCollectionMetricsTableTypeDef",
    "DeleteReplicaActionTypeDef",
    "DeleteReplicationGroupMemberActionTableTypeDef",
    "DeleteReplicationGroupMemberActionTypeDef",
    "DeleteRequestServiceResourceOutputTypeDef",
    "DeleteRequestServiceResourceTypeDef",
    "DeleteTableInputRequestTypeDef",
    "DescribeBackupInputRequestTypeDef",
    "DescribeContinuousBackupsInputRequestTypeDef",
    "DescribeContributorInsightsInputRequestTypeDef",
    "FailureExceptionTypeDef",
    "EndpointTypeDef",
    "DescribeExportInputRequestTypeDef",
    "ExportDescriptionTypeDef",
    "DescribeGlobalTableInputRequestTypeDef",
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    "DescribeImportInputRequestTypeDef",
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    "KinesisDataStreamDestinationTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeTableInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    "DescribeTimeToLiveInputRequestTypeDef",
    "TimeToLiveDescriptionTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportSummaryTypeDef",
    "ExportTableToPointInTimeInputRequestTypeDef",
    "GetItemInputTableGetItemTypeDef",
    "KeySchemaElementTableOutputTypeDef",
    "ProjectionTableOutputTypeDef",
    "ProvisionedThroughputDescriptionTableTypeDef",
    "KeySchemaElementOutputTypeDef",
    "ProjectionOutputTypeDef",
    "ProvisionedThroughputDescriptionTypeDef",
    "ProvisionedThroughputOutputTypeDef",
    "ProjectionServiceResourceTypeDef",
    "ReplicaOutputTypeDef",
    "S3BucketSourceOutputTypeDef",
    "S3BucketSourceTypeDef",
    "KinesisStreamingDestinationInputRequestTypeDef",
    "KinesisStreamingDestinationOutputTypeDef",
    "ListBackupsInputListBackupsPaginateTypeDef",
    "ListBackupsInputRequestTypeDef",
    "ListContributorInsightsInputRequestTypeDef",
    "ListExportsInputRequestTypeDef",
    "ListGlobalTablesInputRequestTypeDef",
    "ListImportsInputRequestTypeDef",
    "ListTablesInputListTablesPaginateTypeDef",
    "ListTablesInputRequestTypeDef",
    "ListTablesOutputTableTypeDef",
    "ListTablesOutputTypeDef",
    "ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef",
    "ListTagsOfResourceInputRequestTypeDef",
    "TagTableTypeDef",
    "TagOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PointInTimeRecoverySpecificationTypeDef",
    "ProvisionedThroughputDescriptionTableResponseMetadataTypeDef",
    "ProvisionedThroughputOverrideOutputTypeDef",
    "ProvisionedThroughputOverrideTableOutputTypeDef",
    "PutRequestServiceResourceOutputTypeDef",
    "PutRequestServiceResourceTypeDef",
    "TableClassSummaryTableTypeDef",
    "TableClassSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreSummaryTableResponseMetadataTypeDef",
    "RestoreSummaryTableTypeDef",
    "RestoreSummaryTypeDef",
    "SSEDescriptionTableResponseMetadataTypeDef",
    "SSEDescriptionTableTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationOutputTypeDef",
    "SSESpecificationTableTypeDef",
    "StreamSpecificationOutputTypeDef",
    "StreamSpecificationTableOutputTypeDef",
    "StreamSpecificationTableResponseMetadataTypeDef",
    "StreamSpecificationTableTypeDef",
    "TableBatchWriterRequestTypeDef",
    "TableClassSummaryTableResponseMetadataTypeDef",
    "TimeToLiveSpecificationOutputTypeDef",
    "TimeToLiveSpecificationTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateContributorInsightsInputRequestTypeDef",
    "UpdateContributorInsightsOutputTypeDef",
    "AttributeValueUpdateTypeDef",
    "BatchStatementErrorTypeDef",
    "BatchStatementRequestTypeDef",
    "ConditionCheckTypeDef",
    "ConditionTypeDef",
    "DeleteRequestOutputTypeDef",
    "DeleteRequestTypeDef",
    "DeleteTypeDef",
    "ExecuteStatementInputRequestTypeDef",
    "ExpectedAttributeValueTypeDef",
    "GetItemInputRequestTypeDef",
    "GetTypeDef",
    "ItemCollectionMetricsTypeDef",
    "ItemResponseTypeDef",
    "KeysAndAttributesOutputTypeDef",
    "KeysAndAttributesTypeDef",
    "ParameterizedStatementTypeDef",
    "PutRequestOutputTypeDef",
    "PutRequestTypeDef",
    "PutTypeDef",
    "UpdateTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyUpdateTypeDef",
    "CreateBackupOutputTypeDef",
    "ListBackupsOutputTableTypeDef",
    "ListBackupsOutputTypeDef",
    "BatchGetItemInputServiceResourceBatchGetItemTypeDef",
    "ConsumedCapacityServiceResourceTypeDef",
    "ConsumedCapacityTableTypeDef",
    "ConsumedCapacityTypeDef",
    "QueryInputQueryPaginateTypeDef",
    "QueryInputTableQueryTypeDef",
    "ScanInputScanPaginateTypeDef",
    "ScanInputTableScanTypeDef",
    "ContinuousBackupsDescriptionTypeDef",
    "ListContributorInsightsOutputTypeDef",
    "CreateGlobalSecondaryIndexActionTableTypeDef",
    "UpdateGlobalSecondaryIndexActionTableTypeDef",
    "LocalSecondaryIndexTypeDef",
    "CreateGlobalSecondaryIndexActionTypeDef",
    "GlobalSecondaryIndexTypeDef",
    "UpdateGlobalSecondaryIndexActionTypeDef",
    "CreateGlobalTableInputRequestTypeDef",
    "ReplicaGlobalSecondaryIndexTableTypeDef",
    "ReplicaGlobalSecondaryIndexTypeDef",
    "TagResourceInputRequestTypeDef",
    "InputFormatOptionsOutputTypeDef",
    "InputFormatOptionsTypeDef",
    "DeleteItemInputTableDeleteItemTypeDef",
    "PutItemInputTablePutItemTypeDef",
    "UpdateItemInputTableUpdateItemTypeDef",
    "ReplicaUpdateTypeDef",
    "DescribeContributorInsightsOutputTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeExportOutputTypeDef",
    "ExportTableToPointInTimeOutputTypeDef",
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    "DescribeTableInputTableExistsWaitTypeDef",
    "DescribeTableInputTableNotExistsWaitTypeDef",
    "DescribeTimeToLiveOutputTypeDef",
    "ListExportsOutputTypeDef",
    "LocalSecondaryIndexDescriptionTableTypeDef",
    "GlobalSecondaryIndexDescriptionTableTypeDef",
    "LocalSecondaryIndexDescriptionTypeDef",
    "LocalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexDescriptionTypeDef",
    "GlobalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexOutputTypeDef",
    "SourceTableDetailsTypeDef",
    "GlobalSecondaryIndexServiceResourceTypeDef",
    "LocalSecondaryIndexServiceResourceTypeDef",
    "GlobalTableTypeDef",
    "ImportSummaryTypeDef",
    "ListTagsOfResourceOutputTableTypeDef",
    "ListTagsOfResourceOutputTypeDef",
    "UpdateContinuousBackupsInputRequestTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTableTypeDef",
    "WriteRequestServiceResourceOutputTypeDef",
    "WriteRequestServiceResourceTypeDef",
    "UpdateTimeToLiveOutputTypeDef",
    "UpdateTimeToLiveInputRequestTypeDef",
    "BatchStatementResponseTypeDef",
    "BatchExecuteStatementInputRequestTypeDef",
    "QueryInputRequestTypeDef",
    "ScanInputRequestTypeDef",
    "DeleteItemInputRequestTypeDef",
    "PutItemInputRequestTypeDef",
    "UpdateItemInputRequestTypeDef",
    "TransactGetItemTypeDef",
    "BatchGetItemInputRequestTypeDef",
    "ExecuteTransactionInputRequestTypeDef",
    "WriteRequestOutputTypeDef",
    "WriteRequestTypeDef",
    "TransactWriteItemTypeDef",
    "AutoScalingSettingsDescriptionTypeDef",
    "AutoScalingSettingsUpdateTypeDef",
    "BatchGetItemOutputServiceResourceTypeDef",
    "DeleteItemOutputTableTypeDef",
    "GetItemOutputTableTypeDef",
    "PutItemOutputTableTypeDef",
    "QueryOutputTableTypeDef",
    "ScanOutputTableTypeDef",
    "UpdateItemOutputTableTypeDef",
    "BatchGetItemOutputTypeDef",
    "DeleteItemOutputTypeDef",
    "ExecuteStatementOutputTypeDef",
    "ExecuteTransactionOutputTypeDef",
    "GetItemOutputTypeDef",
    "PutItemOutputTypeDef",
    "QueryOutputTypeDef",
    "ScanOutputTypeDef",
    "TransactGetItemsOutputTypeDef",
    "TransactWriteItemsOutputTypeDef",
    "UpdateItemOutputTypeDef",
    "DescribeContinuousBackupsOutputTypeDef",
    "UpdateContinuousBackupsOutputTypeDef",
    "GlobalSecondaryIndexUpdateTableTypeDef",
    "CreateTableInputRequestTypeDef",
    "RestoreTableFromBackupInputRequestTypeDef",
    "RestoreTableToPointInTimeInputRequestTypeDef",
    "TableCreationParametersTypeDef",
    "GlobalSecondaryIndexUpdateTypeDef",
    "CreateReplicationGroupMemberActionTableTypeDef",
    "UpdateReplicationGroupMemberActionTableTypeDef",
    "CreateReplicationGroupMemberActionTypeDef",
    "UpdateReplicationGroupMemberActionTypeDef",
    "UpdateGlobalTableInputRequestTypeDef",
    "SourceTableFeatureDetailsTypeDef",
    "TableCreationParametersOutputTypeDef",
    "CreateTableInputServiceResourceCreateTableTypeDef",
    "ListGlobalTablesOutputTypeDef",
    "ListImportsOutputTypeDef",
    "ReplicaDescriptionTypeDef",
    "ReplicaDescriptionTableTypeDef",
    "BatchWriteItemOutputServiceResourceTypeDef",
    "BatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "TransactGetItemsInputRequestTypeDef",
    "BatchWriteItemOutputTypeDef",
    "BatchWriteItemInputRequestTypeDef",
    "TransactWriteItemsInputRequestTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ImportTableInputRequestTypeDef",
    "ReplicationGroupUpdateTableTypeDef",
    "ReplicationGroupUpdateTypeDef",
    "BackupDescriptionTypeDef",
    "ImportTableDescriptionTypeDef",
    "GlobalTableDescriptionTypeDef",
    "TableDescriptionTypeDef",
    "TableDescriptionTableTypeDef",
    "ReplicaAutoScalingDescriptionTypeDef",
    "ReplicaSettingsDescriptionTypeDef",
    "ReplicaAutoScalingUpdateTypeDef",
    "ReplicaSettingsUpdateTypeDef",
    "UpdateTableInputTableUpdateTypeDef",
    "UpdateTableInputRequestTypeDef",
    "DeleteBackupOutputTypeDef",
    "DescribeBackupOutputTypeDef",
    "DescribeImportOutputTypeDef",
    "ImportTableOutputTypeDef",
    "CreateGlobalTableOutputTypeDef",
    "DescribeGlobalTableOutputTypeDef",
    "UpdateGlobalTableOutputTypeDef",
    "CreateTableOutputTypeDef",
    "DeleteTableOutputTypeDef",
    "DescribeTableOutputTypeDef",
    "RestoreTableFromBackupOutputTypeDef",
    "RestoreTableToPointInTimeOutputTypeDef",
    "UpdateTableOutputTypeDef",
    "DeleteTableOutputTableTypeDef",
    "TableAutoScalingDescriptionTypeDef",
    "DescribeGlobalTableSettingsOutputTypeDef",
    "UpdateGlobalTableSettingsOutputTypeDef",
    "UpdateTableReplicaAutoScalingInputRequestTypeDef",
    "UpdateGlobalTableSettingsInputRequestTypeDef",
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    "UpdateTableReplicaAutoScalingOutputTypeDef",
)

ArchivalSummaryTableResponseMetadataTypeDef = TypedDict(
    "ArchivalSummaryTableResponseMetadataTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ArchivalSummaryTableTypeDef = TypedDict(
    "ArchivalSummaryTableTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
    },
    total=False,
)

ArchivalSummaryTypeDef = TypedDict(
    "ArchivalSummaryTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
    },
    total=False,
)

AttributeDefinitionOutputTypeDef = TypedDict(
    "AttributeDefinitionOutputTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeDefinitionServiceResourceTypeDef = TypedDict(
    "AttributeDefinitionServiceResourceTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeDefinitionTableOutputTypeDef = TypedDict(
    "AttributeDefinitionTableOutputTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeDefinitionTableTypeDef = TypedDict(
    "AttributeDefinitionTableTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeDefinitionTypeDef = TypedDict(
    "AttributeDefinitionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeValueServiceResourceTypeDef = TypedDict(
    "AttributeValueServiceResourceTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Dict[str, Any]],
        "L": List[Dict[str, Any]],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

AttributeValueTableTypeDef = TypedDict(
    "AttributeValueTableTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Dict[str, Any]],
        "L": List[Dict[str, Any]],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": Sequence[str],
        "NS": Sequence[str],
        "BS": Sequence[bytes],
        "M": Mapping[str, Any],
        "L": Sequence[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

AttributeValueUpdateTableTypeDef = TypedDict(
    "AttributeValueUpdateTableTypeDef",
    {
        "Value": Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
        "Action": AttributeActionType,
    },
    total=False,
)

_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "DisableScaleIn": bool,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
    },
    total=False,
)


class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
):
    pass


_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "DisableScaleIn": bool,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
    },
    total=False,
)


class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
):
    pass


_RequiredBackupDetailsTypeDef = TypedDict(
    "_RequiredBackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupCreationDateTime": datetime,
    },
)
_OptionalBackupDetailsTypeDef = TypedDict(
    "_OptionalBackupDetailsTypeDef",
    {
        "BackupSizeBytes": int,
        "BackupExpiryDateTime": datetime,
    },
    total=False,
)


class BackupDetailsTypeDef(_RequiredBackupDetailsTypeDef, _OptionalBackupDetailsTypeDef):
    pass


BackupSummaryTableTypeDef = TypedDict(
    "BackupSummaryTableTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "BackupArn": str,
        "BackupName": str,
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupSizeBytes": int,
    },
    total=False,
)

BackupSummaryTypeDef = TypedDict(
    "BackupSummaryTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "BackupArn": str,
        "BackupName": str,
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupSizeBytes": int,
    },
    total=False,
)

_RequiredKeysAndAttributesServiceResourceTypeDef = TypedDict(
    "_RequiredKeysAndAttributesServiceResourceTypeDef",
    {
        "Keys": Sequence[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)
_OptionalKeysAndAttributesServiceResourceTypeDef = TypedDict(
    "_OptionalKeysAndAttributesServiceResourceTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)


class KeysAndAttributesServiceResourceTypeDef(
    _RequiredKeysAndAttributesServiceResourceTypeDef,
    _OptionalKeysAndAttributesServiceResourceTypeDef,
):
    pass


_RequiredKeysAndAttributesServiceResourceOutputTypeDef = TypedDict(
    "_RequiredKeysAndAttributesServiceResourceOutputTypeDef",
    {
        "Keys": List[Dict[str, "AttributeValueServiceResourceTypeDef"]],
    },
)
_OptionalKeysAndAttributesServiceResourceOutputTypeDef = TypedDict(
    "_OptionalKeysAndAttributesServiceResourceOutputTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)


class KeysAndAttributesServiceResourceOutputTypeDef(
    _RequiredKeysAndAttributesServiceResourceOutputTypeDef,
    _OptionalKeysAndAttributesServiceResourceOutputTypeDef,
):
    pass


ItemCollectionMetricsServiceResourceTypeDef = TypedDict(
    "ItemCollectionMetricsServiceResourceTypeDef",
    {
        "ItemCollectionKey": Dict[str, "AttributeValueServiceResourceTypeDef"],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

BillingModeSummaryTableResponseMetadataTypeDef = TypedDict(
    "BillingModeSummaryTableResponseMetadataTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BillingModeSummaryTableTypeDef = TypedDict(
    "BillingModeSummaryTableTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

BillingModeSummaryTypeDef = TypedDict(
    "BillingModeSummaryTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

CapacityServiceResourceTypeDef = TypedDict(
    "CapacityServiceResourceTypeDef",
    {
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "CapacityUnits": float,
    },
    total=False,
)

CapacityTableTypeDef = TypedDict(
    "CapacityTableTypeDef",
    {
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "CapacityUnits": float,
    },
    total=False,
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "CapacityUnits": float,
    },
    total=False,
)

_RequiredConditionTableTypeDef = TypedDict(
    "_RequiredConditionTableTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalConditionTableTypeDef = TypedDict(
    "_OptionalConditionTableTypeDef",
    {
        "AttributeValueList": Sequence[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
    },
    total=False,
)


class ConditionTableTypeDef(_RequiredConditionTableTypeDef, _OptionalConditionTableTypeDef):
    pass


PointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "PointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": PointInTimeRecoveryStatusType,
        "EarliestRestorableDateTime": datetime,
        "LatestRestorableDateTime": datetime,
    },
    total=False,
)

ContributorInsightsSummaryTypeDef = TypedDict(
    "ContributorInsightsSummaryTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
    },
    total=False,
)

CreateBackupInputRequestTypeDef = TypedDict(
    "CreateBackupInputRequestTypeDef",
    {
        "TableName": str,
        "BackupName": str,
    },
)

KeySchemaElementTableTypeDef = TypedDict(
    "KeySchemaElementTableTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

ProjectionTableTypeDef = TypedDict(
    "ProjectionTableTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": Sequence[str],
    },
    total=False,
)

ProvisionedThroughputTableTypeDef = TypedDict(
    "ProvisionedThroughputTableTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

ProjectionTypeDef = TypedDict(
    "ProjectionTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": Sequence[str],
    },
    total=False,
)

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

ReplicaTypeDef = TypedDict(
    "ReplicaTypeDef",
    {
        "RegionName": str,
    },
    total=False,
)

CreateReplicaActionTypeDef = TypedDict(
    "CreateReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

ProvisionedThroughputOverrideTableTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTableTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
)

ProvisionedThroughputOverrideTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
)

SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": bool,
        "SSEType": SSETypeType,
        "KMSMasterKeyId": str,
    },
    total=False,
)

_RequiredStreamSpecificationTypeDef = TypedDict(
    "_RequiredStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
    },
)
_OptionalStreamSpecificationTypeDef = TypedDict(
    "_OptionalStreamSpecificationTypeDef",
    {
        "StreamViewType": StreamViewTypeType,
    },
    total=False,
)


class StreamSpecificationTypeDef(
    _RequiredStreamSpecificationTypeDef, _OptionalStreamSpecificationTypeDef
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

KeySchemaElementServiceResourceTypeDef = TypedDict(
    "KeySchemaElementServiceResourceTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

ProvisionedThroughputServiceResourceTypeDef = TypedDict(
    "ProvisionedThroughputServiceResourceTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

SSESpecificationServiceResourceTypeDef = TypedDict(
    "SSESpecificationServiceResourceTypeDef",
    {
        "Enabled": bool,
        "SSEType": SSETypeType,
        "KMSMasterKeyId": str,
    },
    total=False,
)

_RequiredStreamSpecificationServiceResourceTypeDef = TypedDict(
    "_RequiredStreamSpecificationServiceResourceTypeDef",
    {
        "StreamEnabled": bool,
    },
)
_OptionalStreamSpecificationServiceResourceTypeDef = TypedDict(
    "_OptionalStreamSpecificationServiceResourceTypeDef",
    {
        "StreamViewType": StreamViewTypeType,
    },
    total=False,
)


class StreamSpecificationServiceResourceTypeDef(
    _RequiredStreamSpecificationServiceResourceTypeDef,
    _OptionalStreamSpecificationServiceResourceTypeDef,
):
    pass


TagServiceResourceTypeDef = TypedDict(
    "TagServiceResourceTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CsvOptionsOutputTypeDef = TypedDict(
    "CsvOptionsOutputTypeDef",
    {
        "Delimiter": str,
        "HeaderList": List[str],
    },
    total=False,
)

CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": str,
        "HeaderList": Sequence[str],
    },
    total=False,
)

DeleteBackupInputRequestTypeDef = TypedDict(
    "DeleteBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)

DeleteGlobalSecondaryIndexActionTableTypeDef = TypedDict(
    "DeleteGlobalSecondaryIndexActionTableTypeDef",
    {
        "IndexName": str,
    },
)

DeleteGlobalSecondaryIndexActionTypeDef = TypedDict(
    "DeleteGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
    },
)

ExpectedAttributeValueTableTypeDef = TypedDict(
    "ExpectedAttributeValueTableTypeDef",
    {
        "Value": Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
        "Exists": bool,
        "ComparisonOperator": ComparisonOperatorType,
        "AttributeValueList": Sequence[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
    },
    total=False,
)

ItemCollectionMetricsTableTypeDef = TypedDict(
    "ItemCollectionMetricsTableTypeDef",
    {
        "ItemCollectionKey": Dict[str, "AttributeValueTableTypeDef"],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

DeleteReplicaActionTypeDef = TypedDict(
    "DeleteReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteReplicationGroupMemberActionTableTypeDef = TypedDict(
    "DeleteReplicationGroupMemberActionTableTypeDef",
    {
        "RegionName": str,
    },
)

DeleteReplicationGroupMemberActionTypeDef = TypedDict(
    "DeleteReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteRequestServiceResourceOutputTypeDef = TypedDict(
    "DeleteRequestServiceResourceOutputTypeDef",
    {
        "Key": Dict[str, "AttributeValueServiceResourceTypeDef"],
    },
)

DeleteRequestServiceResourceTypeDef = TypedDict(
    "DeleteRequestServiceResourceTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)

DeleteTableInputRequestTypeDef = TypedDict(
    "DeleteTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeBackupInputRequestTypeDef = TypedDict(
    "DescribeBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)

DescribeContinuousBackupsInputRequestTypeDef = TypedDict(
    "DescribeContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
    },
)

_RequiredDescribeContributorInsightsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDescribeContributorInsightsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeContributorInsightsInputRequestTypeDef",
    {
        "IndexName": str,
    },
    total=False,
)


class DescribeContributorInsightsInputRequestTypeDef(
    _RequiredDescribeContributorInsightsInputRequestTypeDef,
    _OptionalDescribeContributorInsightsInputRequestTypeDef,
):
    pass


FailureExceptionTypeDef = TypedDict(
    "FailureExceptionTypeDef",
    {
        "ExceptionName": str,
        "ExceptionDescription": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

DescribeExportInputRequestTypeDef = TypedDict(
    "DescribeExportInputRequestTypeDef",
    {
        "ExportArn": str,
    },
)

ExportDescriptionTypeDef = TypedDict(
    "ExportDescriptionTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatusType,
        "StartTime": datetime,
        "EndTime": datetime,
        "ExportManifest": str,
        "TableArn": str,
        "TableId": str,
        "ExportTime": datetime,
        "ClientToken": str,
        "S3Bucket": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithmType,
        "S3SseKmsKeyId": str,
        "FailureCode": str,
        "FailureMessage": str,
        "ExportFormat": ExportFormatType,
        "BilledSizeBytes": int,
        "ItemCount": int,
    },
    total=False,
)

DescribeGlobalTableInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeImportInputRequestTypeDef = TypedDict(
    "DescribeImportInputRequestTypeDef",
    {
        "ImportArn": str,
    },
)

DescribeKinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
    },
)

KinesisDataStreamDestinationTypeDef = TypedDict(
    "KinesisDataStreamDestinationTypeDef",
    {
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "DestinationStatusDescription": str,
    },
    total=False,
)

DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "AccountMaxReadCapacityUnits": int,
        "AccountMaxWriteCapacityUnits": int,
        "TableMaxReadCapacityUnits": int,
        "TableMaxWriteCapacityUnits": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableInputRequestTypeDef = TypedDict(
    "DescribeTableInputRequestTypeDef",
    {
        "TableName": str,
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

DescribeTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeTimeToLiveInputRequestTypeDef = TypedDict(
    "DescribeTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
    },
)

TimeToLiveDescriptionTypeDef = TypedDict(
    "TimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": TimeToLiveStatusType,
        "AttributeName": str,
    },
    total=False,
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatusType,
    },
    total=False,
)

_RequiredExportTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_RequiredExportTableToPointInTimeInputRequestTypeDef",
    {
        "TableArn": str,
        "S3Bucket": str,
    },
)
_OptionalExportTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_OptionalExportTableToPointInTimeInputRequestTypeDef",
    {
        "ExportTime": Union[datetime, str],
        "ClientToken": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithmType,
        "S3SseKmsKeyId": str,
        "ExportFormat": ExportFormatType,
    },
    total=False,
)


class ExportTableToPointInTimeInputRequestTypeDef(
    _RequiredExportTableToPointInTimeInputRequestTypeDef,
    _OptionalExportTableToPointInTimeInputRequestTypeDef,
):
    pass


_RequiredGetItemInputTableGetItemTypeDef = TypedDict(
    "_RequiredGetItemInputTableGetItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalGetItemInputTableGetItemTypeDef = TypedDict(
    "_OptionalGetItemInputTableGetItemTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)


class GetItemInputTableGetItemTypeDef(
    _RequiredGetItemInputTableGetItemTypeDef, _OptionalGetItemInputTableGetItemTypeDef
):
    pass


KeySchemaElementTableOutputTypeDef = TypedDict(
    "KeySchemaElementTableOutputTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

ProjectionTableOutputTypeDef = TypedDict(
    "ProjectionTableOutputTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": List[str],
    },
    total=False,
)

ProvisionedThroughputDescriptionTableTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTableTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

KeySchemaElementOutputTypeDef = TypedDict(
    "KeySchemaElementOutputTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

ProjectionOutputTypeDef = TypedDict(
    "ProjectionOutputTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": List[str],
    },
    total=False,
)

ProvisionedThroughputDescriptionTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ProvisionedThroughputOutputTypeDef = TypedDict(
    "ProvisionedThroughputOutputTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

ProjectionServiceResourceTypeDef = TypedDict(
    "ProjectionServiceResourceTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": Sequence[str],
    },
    total=False,
)

ReplicaOutputTypeDef = TypedDict(
    "ReplicaOutputTypeDef",
    {
        "RegionName": str,
    },
    total=False,
)

_RequiredS3BucketSourceOutputTypeDef = TypedDict(
    "_RequiredS3BucketSourceOutputTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalS3BucketSourceOutputTypeDef = TypedDict(
    "_OptionalS3BucketSourceOutputTypeDef",
    {
        "S3BucketOwner": str,
        "S3KeyPrefix": str,
    },
    total=False,
)


class S3BucketSourceOutputTypeDef(
    _RequiredS3BucketSourceOutputTypeDef, _OptionalS3BucketSourceOutputTypeDef
):
    pass


_RequiredS3BucketSourceTypeDef = TypedDict(
    "_RequiredS3BucketSourceTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalS3BucketSourceTypeDef = TypedDict(
    "_OptionalS3BucketSourceTypeDef",
    {
        "S3BucketOwner": str,
        "S3KeyPrefix": str,
    },
    total=False,
)


class S3BucketSourceTypeDef(_RequiredS3BucketSourceTypeDef, _OptionalS3BucketSourceTypeDef):
    pass


KinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "KinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
    },
)

KinesisStreamingDestinationOutputTypeDef = TypedDict(
    "KinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupsInputListBackupsPaginateTypeDef = TypedDict(
    "ListBackupsInputListBackupsPaginateTypeDef",
    {
        "TableName": str,
        "TimeRangeLowerBound": Union[datetime, str],
        "TimeRangeUpperBound": Union[datetime, str],
        "BackupType": BackupTypeFilterType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListBackupsInputRequestTypeDef = TypedDict(
    "ListBackupsInputRequestTypeDef",
    {
        "TableName": str,
        "Limit": int,
        "TimeRangeLowerBound": Union[datetime, str],
        "TimeRangeUpperBound": Union[datetime, str],
        "ExclusiveStartBackupArn": str,
        "BackupType": BackupTypeFilterType,
    },
    total=False,
)

ListContributorInsightsInputRequestTypeDef = TypedDict(
    "ListContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListExportsInputRequestTypeDef = TypedDict(
    "ListExportsInputRequestTypeDef",
    {
        "TableArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGlobalTablesInputRequestTypeDef = TypedDict(
    "ListGlobalTablesInputRequestTypeDef",
    {
        "ExclusiveStartGlobalTableName": str,
        "Limit": int,
        "RegionName": str,
    },
    total=False,
)

ListImportsInputRequestTypeDef = TypedDict(
    "ListImportsInputRequestTypeDef",
    {
        "TableArn": str,
        "PageSize": int,
        "NextToken": str,
    },
    total=False,
)

ListTablesInputListTablesPaginateTypeDef = TypedDict(
    "ListTablesInputListTablesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTablesInputRequestTypeDef = TypedDict(
    "ListTablesInputRequestTypeDef",
    {
        "ExclusiveStartTableName": str,
        "Limit": int,
    },
    total=False,
)

ListTablesOutputTableTypeDef = TypedDict(
    "ListTablesOutputTableTypeDef",
    {
        "TableNames": List[str],
        "LastEvaluatedTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesOutputTypeDef = TypedDict(
    "ListTablesOutputTypeDef",
    {
        "TableNames": List[str],
        "LastEvaluatedTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsOfResourceInputListTagsOfResourcePaginateTypeDef = TypedDict(
    "_RequiredListTagsOfResourceInputListTagsOfResourcePaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsOfResourceInputListTagsOfResourcePaginateTypeDef = TypedDict(
    "_OptionalListTagsOfResourceInputListTagsOfResourcePaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef(
    _RequiredListTagsOfResourceInputListTagsOfResourcePaginateTypeDef,
    _OptionalListTagsOfResourceInputListTagsOfResourcePaginateTypeDef,
):
    pass


_RequiredListTagsOfResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsOfResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsOfResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsOfResourceInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsOfResourceInputRequestTypeDef(
    _RequiredListTagsOfResourceInputRequestTypeDef, _OptionalListTagsOfResourceInputRequestTypeDef
):
    pass


TagTableTypeDef = TypedDict(
    "TagTableTypeDef",
    {
        "Key": str,
        "Value": str,
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

PointInTimeRecoverySpecificationTypeDef = TypedDict(
    "PointInTimeRecoverySpecificationTypeDef",
    {
        "PointInTimeRecoveryEnabled": bool,
    },
)

ProvisionedThroughputDescriptionTableResponseMetadataTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTableResponseMetadataTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionedThroughputOverrideOutputTypeDef = TypedDict(
    "ProvisionedThroughputOverrideOutputTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
)

ProvisionedThroughputOverrideTableOutputTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTableOutputTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
)

PutRequestServiceResourceOutputTypeDef = TypedDict(
    "PutRequestServiceResourceOutputTypeDef",
    {
        "Item": Dict[str, "AttributeValueServiceResourceTypeDef"],
    },
)

PutRequestServiceResourceTypeDef = TypedDict(
    "PutRequestServiceResourceTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)

TableClassSummaryTableTypeDef = TypedDict(
    "TableClassSummaryTableTypeDef",
    {
        "TableClass": TableClassType,
        "LastUpdateDateTime": datetime,
    },
    total=False,
)

TableClassSummaryTypeDef = TypedDict(
    "TableClassSummaryTypeDef",
    {
        "TableClass": TableClassType,
        "LastUpdateDateTime": datetime,
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

RestoreSummaryTableResponseMetadataTypeDef = TypedDict(
    "RestoreSummaryTableResponseMetadataTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreSummaryTableTypeDef = TypedDict(
    "_RequiredRestoreSummaryTableTypeDef",
    {
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
)
_OptionalRestoreSummaryTableTypeDef = TypedDict(
    "_OptionalRestoreSummaryTableTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
    },
    total=False,
)


class RestoreSummaryTableTypeDef(
    _RequiredRestoreSummaryTableTypeDef, _OptionalRestoreSummaryTableTypeDef
):
    pass


_RequiredRestoreSummaryTypeDef = TypedDict(
    "_RequiredRestoreSummaryTypeDef",
    {
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
)
_OptionalRestoreSummaryTypeDef = TypedDict(
    "_OptionalRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
    },
    total=False,
)


class RestoreSummaryTypeDef(_RequiredRestoreSummaryTypeDef, _OptionalRestoreSummaryTypeDef):
    pass


SSEDescriptionTableResponseMetadataTypeDef = TypedDict(
    "SSEDescriptionTableResponseMetadataTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SSEDescriptionTableTypeDef = TypedDict(
    "SSEDescriptionTableTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

SSESpecificationOutputTypeDef = TypedDict(
    "SSESpecificationOutputTypeDef",
    {
        "Enabled": bool,
        "SSEType": SSETypeType,
        "KMSMasterKeyId": str,
    },
    total=False,
)

SSESpecificationTableTypeDef = TypedDict(
    "SSESpecificationTableTypeDef",
    {
        "Enabled": bool,
        "SSEType": SSETypeType,
        "KMSMasterKeyId": str,
    },
    total=False,
)

_RequiredStreamSpecificationOutputTypeDef = TypedDict(
    "_RequiredStreamSpecificationOutputTypeDef",
    {
        "StreamEnabled": bool,
    },
)
_OptionalStreamSpecificationOutputTypeDef = TypedDict(
    "_OptionalStreamSpecificationOutputTypeDef",
    {
        "StreamViewType": StreamViewTypeType,
    },
    total=False,
)


class StreamSpecificationOutputTypeDef(
    _RequiredStreamSpecificationOutputTypeDef, _OptionalStreamSpecificationOutputTypeDef
):
    pass


_RequiredStreamSpecificationTableOutputTypeDef = TypedDict(
    "_RequiredStreamSpecificationTableOutputTypeDef",
    {
        "StreamEnabled": bool,
    },
)
_OptionalStreamSpecificationTableOutputTypeDef = TypedDict(
    "_OptionalStreamSpecificationTableOutputTypeDef",
    {
        "StreamViewType": StreamViewTypeType,
    },
    total=False,
)


class StreamSpecificationTableOutputTypeDef(
    _RequiredStreamSpecificationTableOutputTypeDef, _OptionalStreamSpecificationTableOutputTypeDef
):
    pass


StreamSpecificationTableResponseMetadataTypeDef = TypedDict(
    "StreamSpecificationTableResponseMetadataTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": StreamViewTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStreamSpecificationTableTypeDef = TypedDict(
    "_RequiredStreamSpecificationTableTypeDef",
    {
        "StreamEnabled": bool,
    },
)
_OptionalStreamSpecificationTableTypeDef = TypedDict(
    "_OptionalStreamSpecificationTableTypeDef",
    {
        "StreamViewType": StreamViewTypeType,
    },
    total=False,
)


class StreamSpecificationTableTypeDef(
    _RequiredStreamSpecificationTableTypeDef, _OptionalStreamSpecificationTableTypeDef
):
    pass


TableBatchWriterRequestTypeDef = TypedDict(
    "TableBatchWriterRequestTypeDef",
    {
        "overwrite_by_pkeys": List[str],
    },
    total=False,
)

TableClassSummaryTableResponseMetadataTypeDef = TypedDict(
    "TableClassSummaryTableResponseMetadataTypeDef",
    {
        "TableClass": TableClassType,
        "LastUpdateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TimeToLiveSpecificationOutputTypeDef = TypedDict(
    "TimeToLiveSpecificationOutputTypeDef",
    {
        "Enabled": bool,
        "AttributeName": str,
    },
)

TimeToLiveSpecificationTypeDef = TypedDict(
    "TimeToLiveSpecificationTypeDef",
    {
        "Enabled": bool,
        "AttributeName": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateContributorInsightsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "ContributorInsightsAction": ContributorInsightsActionType,
    },
)
_OptionalUpdateContributorInsightsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateContributorInsightsInputRequestTypeDef",
    {
        "IndexName": str,
    },
    total=False,
)


class UpdateContributorInsightsInputRequestTypeDef(
    _RequiredUpdateContributorInsightsInputRequestTypeDef,
    _OptionalUpdateContributorInsightsInputRequestTypeDef,
):
    pass


UpdateContributorInsightsOutputTypeDef = TypedDict(
    "UpdateContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeValueUpdateTypeDef = TypedDict(
    "AttributeValueUpdateTypeDef",
    {
        "Value": Union[
            AttributeValueTypeDef,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "Action": AttributeActionType,
    },
    total=False,
)

BatchStatementErrorTypeDef = TypedDict(
    "BatchStatementErrorTypeDef",
    {
        "Code": BatchStatementErrorCodeEnumType,
        "Message": str,
        "Item": Dict[str, AttributeValueTypeDef],
    },
    total=False,
)

_RequiredBatchStatementRequestTypeDef = TypedDict(
    "_RequiredBatchStatementRequestTypeDef",
    {
        "Statement": str,
    },
)
_OptionalBatchStatementRequestTypeDef = TypedDict(
    "_OptionalBatchStatementRequestTypeDef",
    {
        "Parameters": Sequence[
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ConsistentRead": bool,
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class BatchStatementRequestTypeDef(
    _RequiredBatchStatementRequestTypeDef, _OptionalBatchStatementRequestTypeDef
):
    pass


_RequiredConditionCheckTypeDef = TypedDict(
    "_RequiredConditionCheckTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "TableName": str,
        "ConditionExpression": str,
    },
)
_OptionalConditionCheckTypeDef = TypedDict(
    "_OptionalConditionCheckTypeDef",
    {
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class ConditionCheckTypeDef(_RequiredConditionCheckTypeDef, _OptionalConditionCheckTypeDef):
    pass


_RequiredConditionTypeDef = TypedDict(
    "_RequiredConditionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalConditionTypeDef = TypedDict(
    "_OptionalConditionTypeDef",
    {
        "AttributeValueList": Sequence[
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
    total=False,
)


class ConditionTypeDef(_RequiredConditionTypeDef, _OptionalConditionTypeDef):
    pass


DeleteRequestOutputTypeDef = TypedDict(
    "DeleteRequestOutputTypeDef",
    {
        "Key": Dict[str, AttributeValueTypeDef],
    },
)

DeleteRequestTypeDef = TypedDict(
    "DeleteRequestTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
    },
)

_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "TableName": str,
    },
)
_OptionalDeleteTypeDef = TypedDict(
    "_OptionalDeleteTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass


_RequiredExecuteStatementInputRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementInputRequestTypeDef",
    {
        "Statement": str,
    },
)
_OptionalExecuteStatementInputRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementInputRequestTypeDef",
    {
        "Parameters": Sequence[
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ConsistentRead": bool,
        "NextToken": str,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "Limit": int,
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class ExecuteStatementInputRequestTypeDef(
    _RequiredExecuteStatementInputRequestTypeDef, _OptionalExecuteStatementInputRequestTypeDef
):
    pass


ExpectedAttributeValueTypeDef = TypedDict(
    "ExpectedAttributeValueTypeDef",
    {
        "Value": Union[
            AttributeValueTypeDef,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "Exists": bool,
        "ComparisonOperator": ComparisonOperatorType,
        "AttributeValueList": Sequence[
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
    total=False,
)

_RequiredGetItemInputRequestTypeDef = TypedDict(
    "_RequiredGetItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
    },
)
_OptionalGetItemInputRequestTypeDef = TypedDict(
    "_OptionalGetItemInputRequestTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)


class GetItemInputRequestTypeDef(
    _RequiredGetItemInputRequestTypeDef, _OptionalGetItemInputRequestTypeDef
):
    pass


_RequiredGetTypeDef = TypedDict(
    "_RequiredGetTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "TableName": str,
    },
)
_OptionalGetTypeDef = TypedDict(
    "_OptionalGetTypeDef",
    {
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)


class GetTypeDef(_RequiredGetTypeDef, _OptionalGetTypeDef):
    pass


ItemCollectionMetricsTypeDef = TypedDict(
    "ItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[str, AttributeValueTypeDef],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "Item": Dict[str, AttributeValueTypeDef],
    },
    total=False,
)

_RequiredKeysAndAttributesOutputTypeDef = TypedDict(
    "_RequiredKeysAndAttributesOutputTypeDef",
    {
        "Keys": List[Dict[str, AttributeValueTypeDef]],
    },
)
_OptionalKeysAndAttributesOutputTypeDef = TypedDict(
    "_OptionalKeysAndAttributesOutputTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)


class KeysAndAttributesOutputTypeDef(
    _RequiredKeysAndAttributesOutputTypeDef, _OptionalKeysAndAttributesOutputTypeDef
):
    pass


_RequiredKeysAndAttributesTypeDef = TypedDict(
    "_RequiredKeysAndAttributesTypeDef",
    {
        "Keys": Sequence[
            Mapping[
                str,
                Union[
                    AttributeValueTypeDef,
                    Union[
                        bytes,
                        bytearray,
                        str,
                        int,
                        Decimal,
                        bool,
                        Set[int],
                        Set[Decimal],
                        Set[str],
                        Set[bytes],
                        Set[bytearray],
                        Sequence[Any],
                        Mapping[str, Any],
                        None,
                    ],
                ],
            ]
        ],
    },
)
_OptionalKeysAndAttributesTypeDef = TypedDict(
    "_OptionalKeysAndAttributesTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
    },
    total=False,
)


class KeysAndAttributesTypeDef(
    _RequiredKeysAndAttributesTypeDef, _OptionalKeysAndAttributesTypeDef
):
    pass


_RequiredParameterizedStatementTypeDef = TypedDict(
    "_RequiredParameterizedStatementTypeDef",
    {
        "Statement": str,
    },
)
_OptionalParameterizedStatementTypeDef = TypedDict(
    "_OptionalParameterizedStatementTypeDef",
    {
        "Parameters": Sequence[
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class ParameterizedStatementTypeDef(
    _RequiredParameterizedStatementTypeDef, _OptionalParameterizedStatementTypeDef
):
    pass


PutRequestOutputTypeDef = TypedDict(
    "PutRequestOutputTypeDef",
    {
        "Item": Dict[str, AttributeValueTypeDef],
    },
)

PutRequestTypeDef = TypedDict(
    "PutRequestTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
    },
)

_RequiredPutTypeDef = TypedDict(
    "_RequiredPutTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "TableName": str,
    },
)
_OptionalPutTypeDef = TypedDict(
    "_OptionalPutTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class PutTypeDef(_RequiredPutTypeDef, _OptionalPutTypeDef):
    pass


_RequiredUpdateTypeDef = TypedDict(
    "_RequiredUpdateTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "UpdateExpression": str,
        "TableName": str,
    },
)
_OptionalUpdateTypeDef = TypedDict(
    "_OptionalUpdateTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class UpdateTypeDef(_RequiredUpdateTypeDef, _OptionalUpdateTypeDef):
    pass


AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": (
            AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef
        ),
    },
    total=False,
)

_RequiredAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingPolicyUpdateTypeDef",
    {
        "TargetTrackingScalingPolicyConfiguration": (
            AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef
        ),
    },
)
_OptionalAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)


class AutoScalingPolicyUpdateTypeDef(
    _RequiredAutoScalingPolicyUpdateTypeDef, _OptionalAutoScalingPolicyUpdateTypeDef
):
    pass


CreateBackupOutputTypeDef = TypedDict(
    "CreateBackupOutputTypeDef",
    {
        "BackupDetails": BackupDetailsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupsOutputTableTypeDef = TypedDict(
    "ListBackupsOutputTableTypeDef",
    {
        "BackupSummaries": List[BackupSummaryTableTypeDef],
        "LastEvaluatedBackupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupsOutputTypeDef = TypedDict(
    "ListBackupsOutputTypeDef",
    {
        "BackupSummaries": List[BackupSummaryTypeDef],
        "LastEvaluatedBackupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetItemInputServiceResourceBatchGetItemTypeDef = TypedDict(
    "_RequiredBatchGetItemInputServiceResourceBatchGetItemTypeDef",
    {
        "RequestItems": Mapping[str, KeysAndAttributesServiceResourceTypeDef],
    },
)
_OptionalBatchGetItemInputServiceResourceBatchGetItemTypeDef = TypedDict(
    "_OptionalBatchGetItemInputServiceResourceBatchGetItemTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)


class BatchGetItemInputServiceResourceBatchGetItemTypeDef(
    _RequiredBatchGetItemInputServiceResourceBatchGetItemTypeDef,
    _OptionalBatchGetItemInputServiceResourceBatchGetItemTypeDef,
):
    pass


ConsumedCapacityServiceResourceTypeDef = TypedDict(
    "ConsumedCapacityServiceResourceTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": CapacityServiceResourceTypeDef,
        "LocalSecondaryIndexes": Dict[str, CapacityServiceResourceTypeDef],
        "GlobalSecondaryIndexes": Dict[str, CapacityServiceResourceTypeDef],
    },
    total=False,
)

ConsumedCapacityTableTypeDef = TypedDict(
    "ConsumedCapacityTableTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": CapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[str, CapacityTableTypeDef],
        "GlobalSecondaryIndexes": Dict[str, CapacityTableTypeDef],
    },
    total=False,
)

ConsumedCapacityTypeDef = TypedDict(
    "ConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": CapacityTypeDef,
        "LocalSecondaryIndexes": Dict[str, CapacityTypeDef],
        "GlobalSecondaryIndexes": Dict[str, CapacityTypeDef],
    },
    total=False,
)

_RequiredQueryInputQueryPaginateTypeDef = TypedDict(
    "_RequiredQueryInputQueryPaginateTypeDef",
    {
        "TableName": str,
    },
)
_OptionalQueryInputQueryPaginateTypeDef = TypedDict(
    "_OptionalQueryInputQueryPaginateTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": Sequence[str],
        "ConsistentRead": bool,
        "KeyConditions": Mapping[str, ConditionTableTypeDef],
        "QueryFilter": Mapping[str, ConditionTableTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "KeyConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class QueryInputQueryPaginateTypeDef(
    _RequiredQueryInputQueryPaginateTypeDef, _OptionalQueryInputQueryPaginateTypeDef
):
    pass


QueryInputTableQueryTypeDef = TypedDict(
    "QueryInputTableQueryTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "ConsistentRead": bool,
        "KeyConditions": Mapping[str, ConditionTableTypeDef],
        "QueryFilter": Mapping[str, ConditionTableTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ExclusiveStartKey": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": Union[str, ConditionBase],
        "KeyConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

_RequiredScanInputScanPaginateTypeDef = TypedDict(
    "_RequiredScanInputScanPaginateTypeDef",
    {
        "TableName": str,
    },
)
_OptionalScanInputScanPaginateTypeDef = TypedDict(
    "_OptionalScanInputScanPaginateTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": Sequence[str],
        "Select": SelectType,
        "ScanFilter": Mapping[str, ConditionTableTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ScanInputScanPaginateTypeDef(
    _RequiredScanInputScanPaginateTypeDef, _OptionalScanInputScanPaginateTypeDef
):
    pass


ScanInputTableScanTypeDef = TypedDict(
    "ScanInputTableScanTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "Select": SelectType,
        "ScanFilter": Mapping[str, ConditionTableTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ExclusiveStartKey": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
    },
    total=False,
)

_RequiredContinuousBackupsDescriptionTypeDef = TypedDict(
    "_RequiredContinuousBackupsDescriptionTypeDef",
    {
        "ContinuousBackupsStatus": ContinuousBackupsStatusType,
    },
)
_OptionalContinuousBackupsDescriptionTypeDef = TypedDict(
    "_OptionalContinuousBackupsDescriptionTypeDef",
    {
        "PointInTimeRecoveryDescription": PointInTimeRecoveryDescriptionTypeDef,
    },
    total=False,
)


class ContinuousBackupsDescriptionTypeDef(
    _RequiredContinuousBackupsDescriptionTypeDef, _OptionalContinuousBackupsDescriptionTypeDef
):
    pass


ListContributorInsightsOutputTypeDef = TypedDict(
    "ListContributorInsightsOutputTypeDef",
    {
        "ContributorInsightsSummaries": List[ContributorInsightsSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGlobalSecondaryIndexActionTableTypeDef = TypedDict(
    "_RequiredCreateGlobalSecondaryIndexActionTableTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTableTypeDef],
        "Projection": ProjectionTableTypeDef,
    },
)
_OptionalCreateGlobalSecondaryIndexActionTableTypeDef = TypedDict(
    "_OptionalCreateGlobalSecondaryIndexActionTableTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTableTypeDef,
    },
    total=False,
)


class CreateGlobalSecondaryIndexActionTableTypeDef(
    _RequiredCreateGlobalSecondaryIndexActionTableTypeDef,
    _OptionalCreateGlobalSecondaryIndexActionTableTypeDef,
):
    pass


UpdateGlobalSecondaryIndexActionTableTypeDef = TypedDict(
    "UpdateGlobalSecondaryIndexActionTableTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughput": ProvisionedThroughputTableTypeDef,
    },
)

LocalSecondaryIndexTypeDef = TypedDict(
    "LocalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
    },
)

_RequiredCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_RequiredCreateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
    },
)
_OptionalCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_OptionalCreateGlobalSecondaryIndexActionTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
    total=False,
)


class CreateGlobalSecondaryIndexActionTypeDef(
    _RequiredCreateGlobalSecondaryIndexActionTypeDef,
    _OptionalCreateGlobalSecondaryIndexActionTypeDef,
):
    pass


_RequiredGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
        "Projection": ProjectionTypeDef,
    },
)
_OptionalGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalGlobalSecondaryIndexTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
    total=False,
)


class GlobalSecondaryIndexTypeDef(
    _RequiredGlobalSecondaryIndexTypeDef, _OptionalGlobalSecondaryIndexTypeDef
):
    pass


UpdateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "UpdateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
    },
)

CreateGlobalTableInputRequestTypeDef = TypedDict(
    "CreateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": Sequence[ReplicaTypeDef],
    },
)

_RequiredReplicaGlobalSecondaryIndexTableTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexTableTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexTableTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexTableTypeDef",
    {
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTableTypeDef,
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexTableTypeDef(
    _RequiredReplicaGlobalSecondaryIndexTableTypeDef,
    _OptionalReplicaGlobalSecondaryIndexTableTypeDef,
):
    pass


_RequiredReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexTypeDef",
    {
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexTypeDef(
    _RequiredReplicaGlobalSecondaryIndexTypeDef, _OptionalReplicaGlobalSecondaryIndexTypeDef
):
    pass


TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

InputFormatOptionsOutputTypeDef = TypedDict(
    "InputFormatOptionsOutputTypeDef",
    {
        "Csv": CsvOptionsOutputTypeDef,
    },
    total=False,
)

InputFormatOptionsTypeDef = TypedDict(
    "InputFormatOptionsTypeDef",
    {
        "Csv": CsvOptionsTypeDef,
    },
    total=False,
)

_RequiredDeleteItemInputTableDeleteItemTypeDef = TypedDict(
    "_RequiredDeleteItemInputTableDeleteItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalDeleteItemInputTableDeleteItemTypeDef = TypedDict(
    "_OptionalDeleteItemInputTableDeleteItemTypeDef",
    {
        "Expected": Mapping[str, ExpectedAttributeValueTableTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class DeleteItemInputTableDeleteItemTypeDef(
    _RequiredDeleteItemInputTableDeleteItemTypeDef, _OptionalDeleteItemInputTableDeleteItemTypeDef
):
    pass


_RequiredPutItemInputTablePutItemTypeDef = TypedDict(
    "_RequiredPutItemInputTablePutItemTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalPutItemInputTablePutItemTypeDef = TypedDict(
    "_OptionalPutItemInputTablePutItemTypeDef",
    {
        "Expected": Mapping[str, ExpectedAttributeValueTableTypeDef],
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionalOperator": ConditionalOperatorType,
        "ConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class PutItemInputTablePutItemTypeDef(
    _RequiredPutItemInputTablePutItemTypeDef, _OptionalPutItemInputTablePutItemTypeDef
):
    pass


_RequiredUpdateItemInputTableUpdateItemTypeDef = TypedDict(
    "_RequiredUpdateItemInputTableUpdateItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)
_OptionalUpdateItemInputTableUpdateItemTypeDef = TypedDict(
    "_OptionalUpdateItemInputTableUpdateItemTypeDef",
    {
        "AttributeUpdates": Mapping[str, AttributeValueUpdateTableTypeDef],
        "Expected": Mapping[str, ExpectedAttributeValueTableTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "UpdateExpression": str,
        "ConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class UpdateItemInputTableUpdateItemTypeDef(
    _RequiredUpdateItemInputTableUpdateItemTypeDef, _OptionalUpdateItemInputTableUpdateItemTypeDef
):
    pass


ReplicaUpdateTypeDef = TypedDict(
    "ReplicaUpdateTypeDef",
    {
        "Create": CreateReplicaActionTypeDef,
        "Delete": DeleteReplicaActionTypeDef,
    },
    total=False,
)

DescribeContributorInsightsOutputTypeDef = TypedDict(
    "DescribeContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsRuleList": List[str],
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "LastUpdateDateTime": datetime,
        "FailureException": FailureExceptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List[EndpointTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportOutputTypeDef = TypedDict(
    "DescribeExportOutputTypeDef",
    {
        "ExportDescription": ExportDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportTableToPointInTimeOutputTypeDef = TypedDict(
    "ExportTableToPointInTimeOutputTypeDef",
    {
        "ExportDescription": ExportDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKinesisStreamingDestinationOutputTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "KinesisDataStreamDestinations": List[KinesisDataStreamDestinationTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTableInputTableExistsWaitTypeDef = TypedDict(
    "_RequiredDescribeTableInputTableExistsWaitTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDescribeTableInputTableExistsWaitTypeDef = TypedDict(
    "_OptionalDescribeTableInputTableExistsWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeTableInputTableExistsWaitTypeDef(
    _RequiredDescribeTableInputTableExistsWaitTypeDef,
    _OptionalDescribeTableInputTableExistsWaitTypeDef,
):
    pass


_RequiredDescribeTableInputTableNotExistsWaitTypeDef = TypedDict(
    "_RequiredDescribeTableInputTableNotExistsWaitTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDescribeTableInputTableNotExistsWaitTypeDef = TypedDict(
    "_OptionalDescribeTableInputTableNotExistsWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeTableInputTableNotExistsWaitTypeDef(
    _RequiredDescribeTableInputTableNotExistsWaitTypeDef,
    _OptionalDescribeTableInputTableNotExistsWaitTypeDef,
):
    pass


DescribeTimeToLiveOutputTypeDef = TypedDict(
    "DescribeTimeToLiveOutputTypeDef",
    {
        "TimeToLiveDescription": TimeToLiveDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "ExportSummaries": List[ExportSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalSecondaryIndexDescriptionTableTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTableTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementTableOutputTypeDef],
        "Projection": ProjectionTableOutputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

GlobalSecondaryIndexDescriptionTableTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTableTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementTableOutputTypeDef],
        "Projection": ProjectionTableOutputTypeDef,
        "IndexStatus": IndexStatusType,
        "Backfilling": bool,
        "ProvisionedThroughput": ProvisionedThroughputDescriptionTableTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

LocalSecondaryIndexDescriptionTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementOutputTypeDef],
        "Projection": ProjectionOutputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

LocalSecondaryIndexInfoTypeDef = TypedDict(
    "LocalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementOutputTypeDef],
        "Projection": ProjectionOutputTypeDef,
    },
    total=False,
)

GlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementOutputTypeDef],
        "Projection": ProjectionOutputTypeDef,
        "IndexStatus": IndexStatusType,
        "Backfilling": bool,
        "ProvisionedThroughput": ProvisionedThroughputDescriptionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

GlobalSecondaryIndexInfoTypeDef = TypedDict(
    "GlobalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementOutputTypeDef],
        "Projection": ProjectionOutputTypeDef,
        "ProvisionedThroughput": ProvisionedThroughputOutputTypeDef,
    },
    total=False,
)

_RequiredGlobalSecondaryIndexOutputTypeDef = TypedDict(
    "_RequiredGlobalSecondaryIndexOutputTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[KeySchemaElementOutputTypeDef],
        "Projection": ProjectionOutputTypeDef,
    },
)
_OptionalGlobalSecondaryIndexOutputTypeDef = TypedDict(
    "_OptionalGlobalSecondaryIndexOutputTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputOutputTypeDef,
    },
    total=False,
)


class GlobalSecondaryIndexOutputTypeDef(
    _RequiredGlobalSecondaryIndexOutputTypeDef, _OptionalGlobalSecondaryIndexOutputTypeDef
):
    pass


_RequiredSourceTableDetailsTypeDef = TypedDict(
    "_RequiredSourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "KeySchema": List[KeySchemaElementOutputTypeDef],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": ProvisionedThroughputOutputTypeDef,
    },
)
_OptionalSourceTableDetailsTypeDef = TypedDict(
    "_OptionalSourceTableDetailsTypeDef",
    {
        "TableArn": str,
        "TableSizeBytes": int,
        "ItemCount": int,
        "BillingMode": BillingModeType,
    },
    total=False,
)


class SourceTableDetailsTypeDef(
    _RequiredSourceTableDetailsTypeDef, _OptionalSourceTableDetailsTypeDef
):
    pass


_RequiredGlobalSecondaryIndexServiceResourceTypeDef = TypedDict(
    "_RequiredGlobalSecondaryIndexServiceResourceTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementServiceResourceTypeDef],
        "Projection": ProjectionServiceResourceTypeDef,
    },
)
_OptionalGlobalSecondaryIndexServiceResourceTypeDef = TypedDict(
    "_OptionalGlobalSecondaryIndexServiceResourceTypeDef",
    {
        "ProvisionedThroughput": ProvisionedThroughputServiceResourceTypeDef,
    },
    total=False,
)


class GlobalSecondaryIndexServiceResourceTypeDef(
    _RequiredGlobalSecondaryIndexServiceResourceTypeDef,
    _OptionalGlobalSecondaryIndexServiceResourceTypeDef,
):
    pass


LocalSecondaryIndexServiceResourceTypeDef = TypedDict(
    "LocalSecondaryIndexServiceResourceTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence[KeySchemaElementServiceResourceTypeDef],
        "Projection": ProjectionServiceResourceTypeDef,
    },
)

GlobalTableTypeDef = TypedDict(
    "GlobalTableTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": List[ReplicaOutputTypeDef],
    },
    total=False,
)

ImportSummaryTypeDef = TypedDict(
    "ImportSummaryTypeDef",
    {
        "ImportArn": str,
        "ImportStatus": ImportStatusType,
        "TableArn": str,
        "S3BucketSource": S3BucketSourceOutputTypeDef,
        "CloudWatchLogGroupArn": str,
        "InputFormat": InputFormatType,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ListTagsOfResourceOutputTableTypeDef = TypedDict(
    "ListTagsOfResourceOutputTableTypeDef",
    {
        "Tags": List[TagTableTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsOfResourceOutputTypeDef = TypedDict(
    "ListTagsOfResourceOutputTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContinuousBackupsInputRequestTypeDef = TypedDict(
    "UpdateContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
        "PointInTimeRecoverySpecification": PointInTimeRecoverySpecificationTypeDef,
    },
)

ReplicaGlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideOutputTypeDef,
    },
    total=False,
)

ReplicaGlobalSecondaryIndexDescriptionTableTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexDescriptionTableTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTableOutputTypeDef,
    },
    total=False,
)

WriteRequestServiceResourceOutputTypeDef = TypedDict(
    "WriteRequestServiceResourceOutputTypeDef",
    {
        "PutRequest": PutRequestServiceResourceOutputTypeDef,
        "DeleteRequest": DeleteRequestServiceResourceOutputTypeDef,
    },
    total=False,
)

WriteRequestServiceResourceTypeDef = TypedDict(
    "WriteRequestServiceResourceTypeDef",
    {
        "PutRequest": PutRequestServiceResourceTypeDef,
        "DeleteRequest": DeleteRequestServiceResourceTypeDef,
    },
    total=False,
)

UpdateTimeToLiveOutputTypeDef = TypedDict(
    "UpdateTimeToLiveOutputTypeDef",
    {
        "TimeToLiveSpecification": TimeToLiveSpecificationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTimeToLiveInputRequestTypeDef = TypedDict(
    "UpdateTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
        "TimeToLiveSpecification": TimeToLiveSpecificationTypeDef,
    },
)

BatchStatementResponseTypeDef = TypedDict(
    "BatchStatementResponseTypeDef",
    {
        "Error": BatchStatementErrorTypeDef,
        "TableName": str,
        "Item": Dict[str, AttributeValueTypeDef],
    },
    total=False,
)

_RequiredBatchExecuteStatementInputRequestTypeDef = TypedDict(
    "_RequiredBatchExecuteStatementInputRequestTypeDef",
    {
        "Statements": Sequence[BatchStatementRequestTypeDef],
    },
)
_OptionalBatchExecuteStatementInputRequestTypeDef = TypedDict(
    "_OptionalBatchExecuteStatementInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)


class BatchExecuteStatementInputRequestTypeDef(
    _RequiredBatchExecuteStatementInputRequestTypeDef,
    _OptionalBatchExecuteStatementInputRequestTypeDef,
):
    pass


_RequiredQueryInputRequestTypeDef = TypedDict(
    "_RequiredQueryInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalQueryInputRequestTypeDef = TypedDict(
    "_OptionalQueryInputRequestTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "ConsistentRead": bool,
        "KeyConditions": Mapping[str, ConditionTypeDef],
        "QueryFilter": Mapping[str, ConditionTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ExclusiveStartKey": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "KeyConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
    },
    total=False,
)


class QueryInputRequestTypeDef(
    _RequiredQueryInputRequestTypeDef, _OptionalQueryInputRequestTypeDef
):
    pass


_RequiredScanInputRequestTypeDef = TypedDict(
    "_RequiredScanInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalScanInputRequestTypeDef = TypedDict(
    "_OptionalScanInputRequestTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "Select": SelectType,
        "ScanFilter": Mapping[str, ConditionTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ExclusiveStartKey": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ConsistentRead": bool,
    },
    total=False,
)


class ScanInputRequestTypeDef(_RequiredScanInputRequestTypeDef, _OptionalScanInputRequestTypeDef):
    pass


_RequiredDeleteItemInputRequestTypeDef = TypedDict(
    "_RequiredDeleteItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
    },
)
_OptionalDeleteItemInputRequestTypeDef = TypedDict(
    "_OptionalDeleteItemInputRequestTypeDef",
    {
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class DeleteItemInputRequestTypeDef(
    _RequiredDeleteItemInputRequestTypeDef, _OptionalDeleteItemInputRequestTypeDef
):
    pass


_RequiredPutItemInputRequestTypeDef = TypedDict(
    "_RequiredPutItemInputRequestTypeDef",
    {
        "TableName": str,
        "Item": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
    },
)
_OptionalPutItemInputRequestTypeDef = TypedDict(
    "_OptionalPutItemInputRequestTypeDef",
    {
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionalOperator": ConditionalOperatorType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class PutItemInputRequestTypeDef(
    _RequiredPutItemInputRequestTypeDef, _OptionalPutItemInputRequestTypeDef
):
    pass


_RequiredUpdateItemInputRequestTypeDef = TypedDict(
    "_RequiredUpdateItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
    },
)
_OptionalUpdateItemInputRequestTypeDef = TypedDict(
    "_OptionalUpdateItemInputRequestTypeDef",
    {
        "AttributeUpdates": Mapping[str, AttributeValueUpdateTypeDef],
        "Expected": Mapping[str, ExpectedAttributeValueTypeDef],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "UpdateExpression": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Mapping[str, str],
        "ExpressionAttributeValues": Mapping[
            str,
            Union[
                AttributeValueTypeDef,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)


class UpdateItemInputRequestTypeDef(
    _RequiredUpdateItemInputRequestTypeDef, _OptionalUpdateItemInputRequestTypeDef
):
    pass


TransactGetItemTypeDef = TypedDict(
    "TransactGetItemTypeDef",
    {
        "Get": GetTypeDef,
    },
)

_RequiredBatchGetItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchGetItemInputRequestTypeDef",
    {
        "RequestItems": Mapping[str, KeysAndAttributesTypeDef],
    },
)
_OptionalBatchGetItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchGetItemInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)


class BatchGetItemInputRequestTypeDef(
    _RequiredBatchGetItemInputRequestTypeDef, _OptionalBatchGetItemInputRequestTypeDef
):
    pass


_RequiredExecuteTransactionInputRequestTypeDef = TypedDict(
    "_RequiredExecuteTransactionInputRequestTypeDef",
    {
        "TransactStatements": Sequence[ParameterizedStatementTypeDef],
    },
)
_OptionalExecuteTransactionInputRequestTypeDef = TypedDict(
    "_OptionalExecuteTransactionInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)


class ExecuteTransactionInputRequestTypeDef(
    _RequiredExecuteTransactionInputRequestTypeDef, _OptionalExecuteTransactionInputRequestTypeDef
):
    pass


WriteRequestOutputTypeDef = TypedDict(
    "WriteRequestOutputTypeDef",
    {
        "PutRequest": PutRequestOutputTypeDef,
        "DeleteRequest": DeleteRequestOutputTypeDef,
    },
    total=False,
)

WriteRequestTypeDef = TypedDict(
    "WriteRequestTypeDef",
    {
        "PutRequest": PutRequestTypeDef,
        "DeleteRequest": DeleteRequestTypeDef,
    },
    total=False,
)

TransactWriteItemTypeDef = TypedDict(
    "TransactWriteItemTypeDef",
    {
        "ConditionCheck": ConditionCheckTypeDef,
        "Put": PutTypeDef,
        "Delete": DeleteTypeDef,
        "Update": UpdateTypeDef,
    },
    total=False,
)

AutoScalingSettingsDescriptionTypeDef = TypedDict(
    "AutoScalingSettingsDescriptionTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[AutoScalingPolicyDescriptionTypeDef],
    },
    total=False,
)

AutoScalingSettingsUpdateTypeDef = TypedDict(
    "AutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": AutoScalingPolicyUpdateTypeDef,
    },
    total=False,
)

BatchGetItemOutputServiceResourceTypeDef = TypedDict(
    "BatchGetItemOutputServiceResourceTypeDef",
    {
        "Responses": Dict[str, List[Dict[str, "AttributeValueServiceResourceTypeDef"]]],
        "UnprocessedKeys": Dict[str, KeysAndAttributesServiceResourceOutputTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityServiceResourceTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteItemOutputTableTypeDef = TypedDict(
    "DeleteItemOutputTableTypeDef",
    {
        "Attributes": Dict[str, "AttributeValueTableTypeDef"],
        "ConsumedCapacity": ConsumedCapacityTableTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTableTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetItemOutputTableTypeDef = TypedDict(
    "GetItemOutputTableTypeDef",
    {
        "Item": Dict[str, "AttributeValueTableTypeDef"],
        "ConsumedCapacity": ConsumedCapacityTableTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutItemOutputTableTypeDef = TypedDict(
    "PutItemOutputTableTypeDef",
    {
        "Attributes": Dict[str, "AttributeValueTableTypeDef"],
        "ConsumedCapacity": ConsumedCapacityTableTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTableTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryOutputTableTypeDef = TypedDict(
    "QueryOutputTableTypeDef",
    {
        "Items": List[Dict[str, "AttributeValueTableTypeDef"]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, "AttributeValueTableTypeDef"],
        "ConsumedCapacity": ConsumedCapacityTableTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScanOutputTableTypeDef = TypedDict(
    "ScanOutputTableTypeDef",
    {
        "Items": List[Dict[str, "AttributeValueTableTypeDef"]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, "AttributeValueTableTypeDef"],
        "ConsumedCapacity": ConsumedCapacityTableTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateItemOutputTableTypeDef = TypedDict(
    "UpdateItemOutputTableTypeDef",
    {
        "Attributes": Dict[str, "AttributeValueTableTypeDef"],
        "ConsumedCapacity": ConsumedCapacityTableTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTableTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetItemOutputTypeDef = TypedDict(
    "BatchGetItemOutputTypeDef",
    {
        "Responses": Dict[str, List[Dict[str, AttributeValueTypeDef]]],
        "UnprocessedKeys": Dict[str, KeysAndAttributesOutputTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteItemOutputTypeDef = TypedDict(
    "DeleteItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "NextToken": str,
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteTransactionOutputTypeDef = TypedDict(
    "ExecuteTransactionOutputTypeDef",
    {
        "Responses": List[ItemResponseTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetItemOutputTypeDef = TypedDict(
    "GetItemOutputTypeDef",
    {
        "Item": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutItemOutputTypeDef = TypedDict(
    "PutItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryOutputTypeDef = TypedDict(
    "QueryOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScanOutputTypeDef = TypedDict(
    "ScanOutputTypeDef",
    {
        "Items": List[Dict[str, AttributeValueTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransactGetItemsOutputTypeDef = TypedDict(
    "TransactGetItemsOutputTypeDef",
    {
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "Responses": List[ItemResponseTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransactWriteItemsOutputTypeDef = TypedDict(
    "TransactWriteItemsOutputTypeDef",
    {
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ItemCollectionMetrics": Dict[str, List[ItemCollectionMetricsTypeDef]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateItemOutputTypeDef = TypedDict(
    "UpdateItemOutputTypeDef",
    {
        "Attributes": Dict[str, AttributeValueTypeDef],
        "ConsumedCapacity": ConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ItemCollectionMetricsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContinuousBackupsOutputTypeDef = TypedDict(
    "DescribeContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": ContinuousBackupsDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContinuousBackupsOutputTypeDef = TypedDict(
    "UpdateContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": ContinuousBackupsDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlobalSecondaryIndexUpdateTableTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTableTypeDef",
    {
        "Update": UpdateGlobalSecondaryIndexActionTableTypeDef,
        "Create": CreateGlobalSecondaryIndexActionTableTypeDef,
        "Delete": DeleteGlobalSecondaryIndexActionTableTypeDef,
    },
    total=False,
)

_RequiredCreateTableInputRequestTypeDef = TypedDict(
    "_RequiredCreateTableInputRequestTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "TableName": str,
        "KeySchema": Sequence[KeySchemaElementTypeDef],
    },
)
_OptionalCreateTableInputRequestTypeDef = TypedDict(
    "_OptionalCreateTableInputRequestTypeDef",
    {
        "LocalSecondaryIndexes": Sequence[LocalSecondaryIndexTypeDef],
        "GlobalSecondaryIndexes": Sequence[GlobalSecondaryIndexTypeDef],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "StreamSpecification": StreamSpecificationTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "TableClass": TableClassType,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)


class CreateTableInputRequestTypeDef(
    _RequiredCreateTableInputRequestTypeDef, _OptionalCreateTableInputRequestTypeDef
):
    pass


_RequiredRestoreTableFromBackupInputRequestTypeDef = TypedDict(
    "_RequiredRestoreTableFromBackupInputRequestTypeDef",
    {
        "TargetTableName": str,
        "BackupArn": str,
    },
)
_OptionalRestoreTableFromBackupInputRequestTypeDef = TypedDict(
    "_OptionalRestoreTableFromBackupInputRequestTypeDef",
    {
        "BillingModeOverride": BillingModeType,
        "GlobalSecondaryIndexOverride": Sequence[GlobalSecondaryIndexTypeDef],
        "LocalSecondaryIndexOverride": Sequence[LocalSecondaryIndexTypeDef],
        "ProvisionedThroughputOverride": ProvisionedThroughputTypeDef,
        "SSESpecificationOverride": SSESpecificationTypeDef,
    },
    total=False,
)


class RestoreTableFromBackupInputRequestTypeDef(
    _RequiredRestoreTableFromBackupInputRequestTypeDef,
    _OptionalRestoreTableFromBackupInputRequestTypeDef,
):
    pass


_RequiredRestoreTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_RequiredRestoreTableToPointInTimeInputRequestTypeDef",
    {
        "TargetTableName": str,
    },
)
_OptionalRestoreTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_OptionalRestoreTableToPointInTimeInputRequestTypeDef",
    {
        "SourceTableArn": str,
        "SourceTableName": str,
        "UseLatestRestorableTime": bool,
        "RestoreDateTime": Union[datetime, str],
        "BillingModeOverride": BillingModeType,
        "GlobalSecondaryIndexOverride": Sequence[GlobalSecondaryIndexTypeDef],
        "LocalSecondaryIndexOverride": Sequence[LocalSecondaryIndexTypeDef],
        "ProvisionedThroughputOverride": ProvisionedThroughputTypeDef,
        "SSESpecificationOverride": SSESpecificationTypeDef,
    },
    total=False,
)


class RestoreTableToPointInTimeInputRequestTypeDef(
    _RequiredRestoreTableToPointInTimeInputRequestTypeDef,
    _OptionalRestoreTableToPointInTimeInputRequestTypeDef,
):
    pass


_RequiredTableCreationParametersTypeDef = TypedDict(
    "_RequiredTableCreationParametersTypeDef",
    {
        "TableName": str,
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "KeySchema": Sequence[KeySchemaElementTypeDef],
    },
)
_OptionalTableCreationParametersTypeDef = TypedDict(
    "_OptionalTableCreationParametersTypeDef",
    {
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "GlobalSecondaryIndexes": Sequence[GlobalSecondaryIndexTypeDef],
    },
    total=False,
)


class TableCreationParametersTypeDef(
    _RequiredTableCreationParametersTypeDef, _OptionalTableCreationParametersTypeDef
):
    pass


GlobalSecondaryIndexUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTypeDef",
    {
        "Update": UpdateGlobalSecondaryIndexActionTypeDef,
        "Create": CreateGlobalSecondaryIndexActionTypeDef,
        "Delete": DeleteGlobalSecondaryIndexActionTypeDef,
    },
    total=False,
)

_RequiredCreateReplicationGroupMemberActionTableTypeDef = TypedDict(
    "_RequiredCreateReplicationGroupMemberActionTableTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalCreateReplicationGroupMemberActionTableTypeDef = TypedDict(
    "_OptionalCreateReplicationGroupMemberActionTableTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTableTypeDef,
        "GlobalSecondaryIndexes": Sequence[ReplicaGlobalSecondaryIndexTableTypeDef],
        "TableClassOverride": TableClassType,
    },
    total=False,
)


class CreateReplicationGroupMemberActionTableTypeDef(
    _RequiredCreateReplicationGroupMemberActionTableTypeDef,
    _OptionalCreateReplicationGroupMemberActionTableTypeDef,
):
    pass


_RequiredUpdateReplicationGroupMemberActionTableTypeDef = TypedDict(
    "_RequiredUpdateReplicationGroupMemberActionTableTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalUpdateReplicationGroupMemberActionTableTypeDef = TypedDict(
    "_OptionalUpdateReplicationGroupMemberActionTableTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTableTypeDef,
        "GlobalSecondaryIndexes": Sequence[ReplicaGlobalSecondaryIndexTableTypeDef],
        "TableClassOverride": TableClassType,
    },
    total=False,
)


class UpdateReplicationGroupMemberActionTableTypeDef(
    _RequiredUpdateReplicationGroupMemberActionTableTypeDef,
    _OptionalUpdateReplicationGroupMemberActionTableTypeDef,
):
    pass


_RequiredCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredCreateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalCreateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": Sequence[ReplicaGlobalSecondaryIndexTypeDef],
        "TableClassOverride": TableClassType,
    },
    total=False,
)


class CreateReplicationGroupMemberActionTypeDef(
    _RequiredCreateReplicationGroupMemberActionTypeDef,
    _OptionalCreateReplicationGroupMemberActionTypeDef,
):
    pass


_RequiredUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredUpdateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalUpdateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": Sequence[ReplicaGlobalSecondaryIndexTypeDef],
        "TableClassOverride": TableClassType,
    },
    total=False,
)


class UpdateReplicationGroupMemberActionTypeDef(
    _RequiredUpdateReplicationGroupMemberActionTypeDef,
    _OptionalUpdateReplicationGroupMemberActionTypeDef,
):
    pass


UpdateGlobalTableInputRequestTypeDef = TypedDict(
    "UpdateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaUpdates": Sequence[ReplicaUpdateTypeDef],
    },
)

SourceTableFeatureDetailsTypeDef = TypedDict(
    "SourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": List[LocalSecondaryIndexInfoTypeDef],
        "GlobalSecondaryIndexes": List[GlobalSecondaryIndexInfoTypeDef],
        "StreamDescription": StreamSpecificationOutputTypeDef,
        "TimeToLiveDescription": TimeToLiveDescriptionTypeDef,
        "SSEDescription": SSEDescriptionTypeDef,
    },
    total=False,
)

_RequiredTableCreationParametersOutputTypeDef = TypedDict(
    "_RequiredTableCreationParametersOutputTypeDef",
    {
        "TableName": str,
        "AttributeDefinitions": List[AttributeDefinitionOutputTypeDef],
        "KeySchema": List[KeySchemaElementOutputTypeDef],
    },
)
_OptionalTableCreationParametersOutputTypeDef = TypedDict(
    "_OptionalTableCreationParametersOutputTypeDef",
    {
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputOutputTypeDef,
        "SSESpecification": SSESpecificationOutputTypeDef,
        "GlobalSecondaryIndexes": List[GlobalSecondaryIndexOutputTypeDef],
    },
    total=False,
)


class TableCreationParametersOutputTypeDef(
    _RequiredTableCreationParametersOutputTypeDef, _OptionalTableCreationParametersOutputTypeDef
):
    pass


_RequiredCreateTableInputServiceResourceCreateTableTypeDef = TypedDict(
    "_RequiredCreateTableInputServiceResourceCreateTableTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionServiceResourceTypeDef],
        "TableName": str,
        "KeySchema": Sequence[KeySchemaElementServiceResourceTypeDef],
    },
)
_OptionalCreateTableInputServiceResourceCreateTableTypeDef = TypedDict(
    "_OptionalCreateTableInputServiceResourceCreateTableTypeDef",
    {
        "LocalSecondaryIndexes": Sequence[LocalSecondaryIndexServiceResourceTypeDef],
        "GlobalSecondaryIndexes": Sequence[GlobalSecondaryIndexServiceResourceTypeDef],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputServiceResourceTypeDef,
        "StreamSpecification": StreamSpecificationServiceResourceTypeDef,
        "SSESpecification": SSESpecificationServiceResourceTypeDef,
        "Tags": Sequence[TagServiceResourceTypeDef],
        "TableClass": TableClassType,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)


class CreateTableInputServiceResourceCreateTableTypeDef(
    _RequiredCreateTableInputServiceResourceCreateTableTypeDef,
    _OptionalCreateTableInputServiceResourceCreateTableTypeDef,
):
    pass


ListGlobalTablesOutputTypeDef = TypedDict(
    "ListGlobalTablesOutputTypeDef",
    {
        "GlobalTables": List[GlobalTableTypeDef],
        "LastEvaluatedGlobalTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef",
    {
        "ImportSummaryList": List[ImportSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicaDescriptionTypeDef = TypedDict(
    "ReplicaDescriptionTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideOutputTypeDef,
        "GlobalSecondaryIndexes": List[ReplicaGlobalSecondaryIndexDescriptionTypeDef],
        "ReplicaInaccessibleDateTime": datetime,
        "ReplicaTableClassSummary": TableClassSummaryTypeDef,
    },
    total=False,
)

ReplicaDescriptionTableTypeDef = TypedDict(
    "ReplicaDescriptionTableTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ProvisionedThroughputOverrideTableOutputTypeDef,
        "GlobalSecondaryIndexes": List[ReplicaGlobalSecondaryIndexDescriptionTableTypeDef],
        "ReplicaInaccessibleDateTime": datetime,
        "ReplicaTableClassSummary": TableClassSummaryTableTypeDef,
    },
    total=False,
)

BatchWriteItemOutputServiceResourceTypeDef = TypedDict(
    "BatchWriteItemOutputServiceResourceTypeDef",
    {
        "UnprocessedItems": Dict[str, List[WriteRequestServiceResourceOutputTypeDef]],
        "ItemCollectionMetrics": Dict[str, List[ItemCollectionMetricsServiceResourceTypeDef]],
        "ConsumedCapacity": List[ConsumedCapacityServiceResourceTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchWriteItemInputServiceResourceBatchWriteItemTypeDef = TypedDict(
    "_RequiredBatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    {
        "RequestItems": Mapping[str, Sequence[WriteRequestServiceResourceTypeDef]],
    },
)
_OptionalBatchWriteItemInputServiceResourceBatchWriteItemTypeDef = TypedDict(
    "_OptionalBatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
    },
    total=False,
)


class BatchWriteItemInputServiceResourceBatchWriteItemTypeDef(
    _RequiredBatchWriteItemInputServiceResourceBatchWriteItemTypeDef,
    _OptionalBatchWriteItemInputServiceResourceBatchWriteItemTypeDef,
):
    pass


BatchExecuteStatementOutputTypeDef = TypedDict(
    "BatchExecuteStatementOutputTypeDef",
    {
        "Responses": List[BatchStatementResponseTypeDef],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTransactGetItemsInputRequestTypeDef = TypedDict(
    "_RequiredTransactGetItemsInputRequestTypeDef",
    {
        "TransactItems": Sequence[TransactGetItemTypeDef],
    },
)
_OptionalTransactGetItemsInputRequestTypeDef = TypedDict(
    "_OptionalTransactGetItemsInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)


class TransactGetItemsInputRequestTypeDef(
    _RequiredTransactGetItemsInputRequestTypeDef, _OptionalTransactGetItemsInputRequestTypeDef
):
    pass


BatchWriteItemOutputTypeDef = TypedDict(
    "BatchWriteItemOutputTypeDef",
    {
        "UnprocessedItems": Dict[str, List[WriteRequestOutputTypeDef]],
        "ItemCollectionMetrics": Dict[str, List[ItemCollectionMetricsTypeDef]],
        "ConsumedCapacity": List[ConsumedCapacityTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchWriteItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchWriteItemInputRequestTypeDef",
    {
        "RequestItems": Mapping[str, Sequence[WriteRequestTypeDef]],
    },
)
_OptionalBatchWriteItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchWriteItemInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
    },
    total=False,
)


class BatchWriteItemInputRequestTypeDef(
    _RequiredBatchWriteItemInputRequestTypeDef, _OptionalBatchWriteItemInputRequestTypeDef
):
    pass


_RequiredTransactWriteItemsInputRequestTypeDef = TypedDict(
    "_RequiredTransactWriteItemsInputRequestTypeDef",
    {
        "TransactItems": Sequence[TransactWriteItemTypeDef],
    },
)
_OptionalTransactWriteItemsInputRequestTypeDef = TypedDict(
    "_OptionalTransactWriteItemsInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ClientRequestToken": str,
    },
    total=False,
)


class TransactWriteItemsInputRequestTypeDef(
    _RequiredTransactWriteItemsInputRequestTypeDef, _OptionalTransactWriteItemsInputRequestTypeDef
):
    pass


ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    {
        "IndexName": str,
        "IndexStatus": IndexStatusType,
        "ProvisionedReadCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ProvisionedWriteCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
    },
    total=False,
)

_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexStatus": IndexStatusType,
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
):
    pass


GlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedWriteCapacityAutoScalingUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)

_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettingsUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)


class GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass


ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityAutoScalingUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)

_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettingsUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass


_RequiredImportTableInputRequestTypeDef = TypedDict(
    "_RequiredImportTableInputRequestTypeDef",
    {
        "S3BucketSource": S3BucketSourceTypeDef,
        "InputFormat": InputFormatType,
        "TableCreationParameters": TableCreationParametersTypeDef,
    },
)
_OptionalImportTableInputRequestTypeDef = TypedDict(
    "_OptionalImportTableInputRequestTypeDef",
    {
        "ClientToken": str,
        "InputFormatOptions": InputFormatOptionsTypeDef,
        "InputCompressionType": InputCompressionTypeType,
    },
    total=False,
)


class ImportTableInputRequestTypeDef(
    _RequiredImportTableInputRequestTypeDef, _OptionalImportTableInputRequestTypeDef
):
    pass


ReplicationGroupUpdateTableTypeDef = TypedDict(
    "ReplicationGroupUpdateTableTypeDef",
    {
        "Create": CreateReplicationGroupMemberActionTableTypeDef,
        "Update": UpdateReplicationGroupMemberActionTableTypeDef,
        "Delete": DeleteReplicationGroupMemberActionTableTypeDef,
    },
    total=False,
)

ReplicationGroupUpdateTypeDef = TypedDict(
    "ReplicationGroupUpdateTypeDef",
    {
        "Create": CreateReplicationGroupMemberActionTypeDef,
        "Update": UpdateReplicationGroupMemberActionTypeDef,
        "Delete": DeleteReplicationGroupMemberActionTypeDef,
    },
    total=False,
)

BackupDescriptionTypeDef = TypedDict(
    "BackupDescriptionTypeDef",
    {
        "BackupDetails": BackupDetailsTypeDef,
        "SourceTableDetails": SourceTableDetailsTypeDef,
        "SourceTableFeatureDetails": SourceTableFeatureDetailsTypeDef,
    },
    total=False,
)

ImportTableDescriptionTypeDef = TypedDict(
    "ImportTableDescriptionTypeDef",
    {
        "ImportArn": str,
        "ImportStatus": ImportStatusType,
        "TableArn": str,
        "TableId": str,
        "ClientToken": str,
        "S3BucketSource": S3BucketSourceOutputTypeDef,
        "ErrorCount": int,
        "CloudWatchLogGroupArn": str,
        "InputFormat": InputFormatType,
        "InputFormatOptions": InputFormatOptionsOutputTypeDef,
        "InputCompressionType": InputCompressionTypeType,
        "TableCreationParameters": TableCreationParametersOutputTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "ProcessedSizeBytes": int,
        "ProcessedItemCount": int,
        "ImportedItemCount": int,
        "FailureCode": str,
        "FailureMessage": str,
    },
    total=False,
)

GlobalTableDescriptionTypeDef = TypedDict(
    "GlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": List[ReplicaDescriptionTypeDef],
        "GlobalTableArn": str,
        "CreationDateTime": datetime,
        "GlobalTableStatus": GlobalTableStatusType,
        "GlobalTableName": str,
    },
    total=False,
)

TableDescriptionTypeDef = TypedDict(
    "TableDescriptionTypeDef",
    {
        "AttributeDefinitions": List[AttributeDefinitionOutputTypeDef],
        "TableName": str,
        "KeySchema": List[KeySchemaElementOutputTypeDef],
        "TableStatus": TableStatusType,
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ProvisionedThroughputDescriptionTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": BillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[LocalSecondaryIndexDescriptionTypeDef],
        "GlobalSecondaryIndexes": List[GlobalSecondaryIndexDescriptionTypeDef],
        "StreamSpecification": StreamSpecificationOutputTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ReplicaDescriptionTypeDef],
        "RestoreSummary": RestoreSummaryTypeDef,
        "SSEDescription": SSEDescriptionTypeDef,
        "ArchivalSummary": ArchivalSummaryTypeDef,
        "TableClassSummary": TableClassSummaryTypeDef,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

TableDescriptionTableTypeDef = TypedDict(
    "TableDescriptionTableTypeDef",
    {
        "AttributeDefinitions": List[AttributeDefinitionTableOutputTypeDef],
        "TableName": str,
        "KeySchema": List[KeySchemaElementTableOutputTypeDef],
        "TableStatus": TableStatusType,
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ProvisionedThroughputDescriptionTableTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": BillingModeSummaryTableTypeDef,
        "LocalSecondaryIndexes": List[LocalSecondaryIndexDescriptionTableTypeDef],
        "GlobalSecondaryIndexes": List[GlobalSecondaryIndexDescriptionTableTypeDef],
        "StreamSpecification": StreamSpecificationTableOutputTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ReplicaDescriptionTableTypeDef],
        "RestoreSummary": RestoreSummaryTableTypeDef,
        "SSEDescription": SSEDescriptionTableTypeDef,
        "ArchivalSummary": ArchivalSummaryTableTypeDef,
        "TableClassSummary": TableClassSummaryTableTypeDef,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

ReplicaAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaAutoScalingDescriptionTypeDef",
    {
        "RegionName": str,
        "GlobalSecondaryIndexes": List[ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ReplicaStatus": ReplicaStatusType,
    },
    total=False,
)

_RequiredReplicaSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaSettingsDescriptionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaSettingsDescriptionTypeDef",
    {
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaBillingModeSummary": BillingModeSummaryTypeDef,
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ReplicaProvisionedWriteCapacityUnits": int,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": AutoScalingSettingsDescriptionTypeDef,
        "ReplicaGlobalSecondaryIndexSettings": List[
            ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef
        ],
        "ReplicaTableClassSummary": TableClassSummaryTypeDef,
    },
    total=False,
)


class ReplicaSettingsDescriptionTypeDef(
    _RequiredReplicaSettingsDescriptionTypeDef, _OptionalReplicaSettingsDescriptionTypeDef
):
    pass


_RequiredReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_RequiredReplicaAutoScalingUpdateTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_OptionalReplicaAutoScalingUpdateTypeDef",
    {
        "ReplicaGlobalSecondaryIndexUpdates": Sequence[
            ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef
        ],
        "ReplicaProvisionedReadCapacityAutoScalingUpdate": AutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)


class ReplicaAutoScalingUpdateTypeDef(
    _RequiredReplicaAutoScalingUpdateTypeDef, _OptionalReplicaAutoScalingUpdateTypeDef
):
    pass


_RequiredReplicaSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaSettingsUpdateTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaSettingsUpdateTypeDef",
    {
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": AutoScalingSettingsUpdateTypeDef,
        "ReplicaGlobalSecondaryIndexSettingsUpdate": Sequence[
            ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef
        ],
        "ReplicaTableClass": TableClassType,
    },
    total=False,
)


class ReplicaSettingsUpdateTypeDef(
    _RequiredReplicaSettingsUpdateTypeDef, _OptionalReplicaSettingsUpdateTypeDef
):
    pass


UpdateTableInputTableUpdateTypeDef = TypedDict(
    "UpdateTableInputTableUpdateTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTableTypeDef],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTableTypeDef,
        "GlobalSecondaryIndexUpdates": Sequence[GlobalSecondaryIndexUpdateTableTypeDef],
        "StreamSpecification": StreamSpecificationTableTypeDef,
        "SSESpecification": SSESpecificationTableTypeDef,
        "ReplicaUpdates": Sequence[ReplicationGroupUpdateTableTypeDef],
        "TableClass": TableClassType,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

_RequiredUpdateTableInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalUpdateTableInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTableInputRequestTypeDef",
    {
        "AttributeDefinitions": Sequence[AttributeDefinitionTypeDef],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": ProvisionedThroughputTypeDef,
        "GlobalSecondaryIndexUpdates": Sequence[GlobalSecondaryIndexUpdateTypeDef],
        "StreamSpecification": StreamSpecificationTypeDef,
        "SSESpecification": SSESpecificationTypeDef,
        "ReplicaUpdates": Sequence[ReplicationGroupUpdateTypeDef],
        "TableClass": TableClassType,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)


class UpdateTableInputRequestTypeDef(
    _RequiredUpdateTableInputRequestTypeDef, _OptionalUpdateTableInputRequestTypeDef
):
    pass


DeleteBackupOutputTypeDef = TypedDict(
    "DeleteBackupOutputTypeDef",
    {
        "BackupDescription": BackupDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupOutputTypeDef = TypedDict(
    "DescribeBackupOutputTypeDef",
    {
        "BackupDescription": BackupDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportOutputTypeDef = TypedDict(
    "DescribeImportOutputTypeDef",
    {
        "ImportTableDescription": ImportTableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportTableOutputTypeDef = TypedDict(
    "ImportTableOutputTypeDef",
    {
        "ImportTableDescription": ImportTableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGlobalTableOutputTypeDef = TypedDict(
    "CreateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalTableOutputTypeDef = TypedDict(
    "DescribeGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalTableOutputTypeDef = TypedDict(
    "UpdateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": GlobalTableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTableOutputTypeDef = TypedDict(
    "CreateTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTableOutputTypeDef = TypedDict(
    "DeleteTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableOutputTypeDef = TypedDict(
    "DescribeTableOutputTypeDef",
    {
        "Table": TableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreTableFromBackupOutputTypeDef = TypedDict(
    "RestoreTableFromBackupOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreTableToPointInTimeOutputTypeDef = TypedDict(
    "RestoreTableToPointInTimeOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTableOutputTypeDef = TypedDict(
    "UpdateTableOutputTypeDef",
    {
        "TableDescription": TableDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTableOutputTableTypeDef = TypedDict(
    "DeleteTableOutputTableTypeDef",
    {
        "TableDescription": TableDescriptionTableTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TableAutoScalingDescriptionTypeDef = TypedDict(
    "TableAutoScalingDescriptionTypeDef",
    {
        "TableName": str,
        "TableStatus": TableStatusType,
        "Replicas": List[ReplicaAutoScalingDescriptionTypeDef],
    },
    total=False,
)

DescribeGlobalTableSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List[ReplicaSettingsDescriptionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalTableSettingsOutputTypeDef = TypedDict(
    "UpdateGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List[ReplicaSettingsDescriptionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef",
    {
        "GlobalSecondaryIndexUpdates": Sequence[GlobalSecondaryIndexAutoScalingUpdateTypeDef],
        "ProvisionedWriteCapacityAutoScalingUpdate": AutoScalingSettingsUpdateTypeDef,
        "ReplicaUpdates": Sequence[ReplicaAutoScalingUpdateTypeDef],
    },
    total=False,
)


class UpdateTableReplicaAutoScalingInputRequestTypeDef(
    _RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef,
    _OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef,
):
    pass


_RequiredUpdateGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)
_OptionalUpdateGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableBillingMode": BillingModeType,
        "GlobalTableProvisionedWriteCapacityUnits": int,
        "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate": (
            AutoScalingSettingsUpdateTypeDef
        ),
        "GlobalTableGlobalSecondaryIndexSettingsUpdate": Sequence[
            GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef
        ],
        "ReplicaSettingsUpdate": Sequence[ReplicaSettingsUpdateTypeDef],
    },
    total=False,
)


class UpdateGlobalTableSettingsInputRequestTypeDef(
    _RequiredUpdateGlobalTableSettingsInputRequestTypeDef,
    _OptionalUpdateGlobalTableSettingsInputRequestTypeDef,
):
    pass


DescribeTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": TableAutoScalingDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": TableAutoScalingDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
