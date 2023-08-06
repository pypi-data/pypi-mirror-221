"""
Type annotations for iotanalytics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityOutputTypeDef

    data: AddAttributesActivityOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ChannelStatusType,
    ComputeTypeType,
    DatasetActionTypeType,
    DatasetContentStateType,
    DatasetStatusType,
    DatastoreStatusType,
    FileFormatTypeType,
    ReprocessingStatusType,
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
    "AddAttributesActivityOutputTypeDef",
    "AddAttributesActivityTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "MessageTypeDef",
    "CancelPipelineReprocessingRequestRequestTypeDef",
    "ChannelActivityOutputTypeDef",
    "ChannelActivityTypeDef",
    "ChannelMessagesTypeDef",
    "EstimatedResourceSizeTypeDef",
    "CustomerManagedChannelS3StorageOutputTypeDef",
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    "CustomerManagedChannelS3StorageTypeDef",
    "RetentionPeriodOutputTypeDef",
    "ColumnOutputTypeDef",
    "ColumnTypeDef",
    "ResourceConfigurationOutputTypeDef",
    "ResourceConfigurationTypeDef",
    "RetentionPeriodTypeDef",
    "TagTypeDef",
    "CreateDatasetContentRequestRequestTypeDef",
    "CreateDatasetContentResponseTypeDef",
    "VersioningConfigurationTypeDef",
    "CreatePipelineResponseTypeDef",
    "CustomerManagedDatastoreS3StorageOutputTypeDef",
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    "CustomerManagedDatastoreS3StorageTypeDef",
    "DatasetActionSummaryTypeDef",
    "IotEventsDestinationConfigurationOutputTypeDef",
    "IotEventsDestinationConfigurationTypeDef",
    "DatasetContentStatusTypeDef",
    "DatasetContentVersionValueOutputTypeDef",
    "DatasetContentVersionValueTypeDef",
    "DatasetEntryTypeDef",
    "ScheduleOutputTypeDef",
    "TriggeringDatasetOutputTypeDef",
    "ScheduleTypeDef",
    "TriggeringDatasetTypeDef",
    "VersioningConfigurationOutputTypeDef",
    "DatastoreActivityOutputTypeDef",
    "DatastoreActivityTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    "PartitionOutputTypeDef",
    "TimestampPartitionOutputTypeDef",
    "PartitionTypeDef",
    "TimestampPartitionTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteDatasetContentRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatastoreRequestRequestTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeltaTimeOutputTypeDef",
    "DeltaTimeSessionWindowConfigurationOutputTypeDef",
    "DeltaTimeSessionWindowConfigurationTypeDef",
    "DeltaTimeTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatastoreRequestRequestTypeDef",
    "LoggingOptionsOutputTypeDef",
    "DescribePipelineRequestRequestTypeDef",
    "DeviceRegistryEnrichActivityOutputTypeDef",
    "DeviceRegistryEnrichActivityTypeDef",
    "DeviceShadowEnrichActivityOutputTypeDef",
    "DeviceShadowEnrichActivityTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FilterActivityOutputTypeDef",
    "FilterActivityTypeDef",
    "GetDatasetContentRequestRequestTypeDef",
    "GlueConfigurationOutputTypeDef",
    "GlueConfigurationTypeDef",
    "LambdaActivityOutputTypeDef",
    "LambdaActivityTypeDef",
    "ListChannelsRequestListChannelsPaginateTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListDatasetContentsRequestListDatasetContentsPaginateTypeDef",
    "ListDatasetContentsRequestRequestTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    "ListDatastoresRequestRequestTypeDef",
    "ListPipelinesRequestListPipelinesPaginateTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "LoggingOptionsTypeDef",
    "MathActivityOutputTypeDef",
    "MathActivityTypeDef",
    "OutputFileUriValueOutputTypeDef",
    "OutputFileUriValueTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveAttributesActivityOutputTypeDef",
    "SelectAttributesActivityOutputTypeDef",
    "RemoveAttributesActivityTypeDef",
    "SelectAttributesActivityTypeDef",
    "ReprocessingSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "RunPipelineActivityResponseTypeDef",
    "SampleChannelDataRequestRequestTypeDef",
    "SampleChannelDataResponseTypeDef",
    "StartPipelineReprocessingResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchPutMessageResponseTypeDef",
    "BatchPutMessageRequestRequestTypeDef",
    "StartPipelineReprocessingRequestRequestTypeDef",
    "ChannelStatisticsTypeDef",
    "DatastoreStatisticsTypeDef",
    "ChannelStorageOutputTypeDef",
    "ChannelStorageSummaryTypeDef",
    "ChannelStorageTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDatastoreResponseTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DatasetContentSummaryTypeDef",
    "GetDatasetContentResponseTypeDef",
    "DatasetTriggerOutputTypeDef",
    "DatasetTriggerTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageOutputTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    "DatastorePartitionOutputTypeDef",
    "DatastorePartitionTypeDef",
    "QueryFilterOutputTypeDef",
    "LateDataRuleConfigurationOutputTypeDef",
    "LateDataRuleConfigurationTypeDef",
    "QueryFilterTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "S3DestinationConfigurationOutputTypeDef",
    "S3DestinationConfigurationTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "VariableOutputTypeDef",
    "VariableTypeDef",
    "PipelineActivityOutputTypeDef",
    "PipelineActivityTypeDef",
    "PipelineSummaryTypeDef",
    "ChannelTypeDef",
    "ChannelSummaryTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "ParquetConfigurationOutputTypeDef",
    "ParquetConfigurationTypeDef",
    "ListDatasetContentsResponseTypeDef",
    "DatasetSummaryTypeDef",
    "DatastoreStorageOutputTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreStorageTypeDef",
    "DatastorePartitionsOutputTypeDef",
    "DatastorePartitionsTypeDef",
    "SqlQueryDatasetActionOutputTypeDef",
    "LateDataRuleOutputTypeDef",
    "LateDataRuleTypeDef",
    "SqlQueryDatasetActionTypeDef",
    "DatasetContentDeliveryDestinationOutputTypeDef",
    "DatasetContentDeliveryDestinationTypeDef",
    "ContainerDatasetActionOutputTypeDef",
    "ContainerDatasetActionTypeDef",
    "PipelineTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "RunPipelineActivityRequestRequestTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "FileFormatConfigurationOutputTypeDef",
    "FileFormatConfigurationTypeDef",
    "ListDatasetsResponseTypeDef",
    "DatastoreSummaryTypeDef",
    "DatasetContentDeliveryRuleOutputTypeDef",
    "DatasetContentDeliveryRuleTypeDef",
    "DatasetActionOutputTypeDef",
    "DatasetActionTypeDef",
    "DescribePipelineResponseTypeDef",
    "DatastoreTypeDef",
    "CreateDatastoreRequestRequestTypeDef",
    "UpdateDatastoreRequestRequestTypeDef",
    "ListDatastoresResponseTypeDef",
    "DatasetTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "DescribeDatastoreResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
)

_RequiredAddAttributesActivityOutputTypeDef = TypedDict(
    "_RequiredAddAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": Dict[str, str],
    },
)
_OptionalAddAttributesActivityOutputTypeDef = TypedDict(
    "_OptionalAddAttributesActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class AddAttributesActivityOutputTypeDef(
    _RequiredAddAttributesActivityOutputTypeDef, _OptionalAddAttributesActivityOutputTypeDef
):
    pass


_RequiredAddAttributesActivityTypeDef = TypedDict(
    "_RequiredAddAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Mapping[str, str],
    },
)
_OptionalAddAttributesActivityTypeDef = TypedDict(
    "_OptionalAddAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class AddAttributesActivityTypeDef(
    _RequiredAddAttributesActivityTypeDef, _OptionalAddAttributesActivityTypeDef
):
    pass


BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": str,
        "payload": Union[str, bytes, IO[Any], StreamingBody],
    },
)

CancelPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "CancelPipelineReprocessingRequestRequestTypeDef",
    {
        "pipelineName": str,
        "reprocessingId": str,
    },
)

_RequiredChannelActivityOutputTypeDef = TypedDict(
    "_RequiredChannelActivityOutputTypeDef",
    {
        "name": str,
        "channelName": str,
    },
)
_OptionalChannelActivityOutputTypeDef = TypedDict(
    "_OptionalChannelActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class ChannelActivityOutputTypeDef(
    _RequiredChannelActivityOutputTypeDef, _OptionalChannelActivityOutputTypeDef
):
    pass


_RequiredChannelActivityTypeDef = TypedDict(
    "_RequiredChannelActivityTypeDef",
    {
        "name": str,
        "channelName": str,
    },
)
_OptionalChannelActivityTypeDef = TypedDict(
    "_OptionalChannelActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class ChannelActivityTypeDef(_RequiredChannelActivityTypeDef, _OptionalChannelActivityTypeDef):
    pass


ChannelMessagesTypeDef = TypedDict(
    "ChannelMessagesTypeDef",
    {
        "s3Paths": Sequence[str],
    },
    total=False,
)

EstimatedResourceSizeTypeDef = TypedDict(
    "EstimatedResourceSizeTypeDef",
    {
        "estimatedSizeInBytes": float,
        "estimatedOn": datetime,
    },
    total=False,
)

_RequiredCustomerManagedChannelS3StorageOutputTypeDef = TypedDict(
    "_RequiredCustomerManagedChannelS3StorageOutputTypeDef",
    {
        "bucket": str,
        "roleArn": str,
    },
)
_OptionalCustomerManagedChannelS3StorageOutputTypeDef = TypedDict(
    "_OptionalCustomerManagedChannelS3StorageOutputTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class CustomerManagedChannelS3StorageOutputTypeDef(
    _RequiredCustomerManagedChannelS3StorageOutputTypeDef,
    _OptionalCustomerManagedChannelS3StorageOutputTypeDef,
):
    pass


CustomerManagedChannelS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredCustomerManagedChannelS3StorageTypeDef = TypedDict(
    "_RequiredCustomerManagedChannelS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
    },
)
_OptionalCustomerManagedChannelS3StorageTypeDef = TypedDict(
    "_OptionalCustomerManagedChannelS3StorageTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class CustomerManagedChannelS3StorageTypeDef(
    _RequiredCustomerManagedChannelS3StorageTypeDef, _OptionalCustomerManagedChannelS3StorageTypeDef
):
    pass


RetentionPeriodOutputTypeDef = TypedDict(
    "RetentionPeriodOutputTypeDef",
    {
        "unlimited": bool,
        "numberOfDays": int,
    },
    total=False,
)

ColumnOutputTypeDef = TypedDict(
    "ColumnOutputTypeDef",
    {
        "name": str,
        "type": str,
    },
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)

ResourceConfigurationOutputTypeDef = TypedDict(
    "ResourceConfigurationOutputTypeDef",
    {
        "computeType": ComputeTypeType,
        "volumeSizeInGB": int,
    },
)

ResourceConfigurationTypeDef = TypedDict(
    "ResourceConfigurationTypeDef",
    {
        "computeType": ComputeTypeType,
        "volumeSizeInGB": int,
    },
)

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "unlimited": bool,
        "numberOfDays": int,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredCreateDatasetContentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalCreateDatasetContentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetContentRequestRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)


class CreateDatasetContentRequestRequestTypeDef(
    _RequiredCreateDatasetContentRequestRequestTypeDef,
    _OptionalCreateDatasetContentRequestRequestTypeDef,
):
    pass


CreateDatasetContentResponseTypeDef = TypedDict(
    "CreateDatasetContentResponseTypeDef",
    {
        "versionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "unlimited": bool,
        "maxVersions": int,
    },
    total=False,
)

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomerManagedDatastoreS3StorageOutputTypeDef = TypedDict(
    "_RequiredCustomerManagedDatastoreS3StorageOutputTypeDef",
    {
        "bucket": str,
        "roleArn": str,
    },
)
_OptionalCustomerManagedDatastoreS3StorageOutputTypeDef = TypedDict(
    "_OptionalCustomerManagedDatastoreS3StorageOutputTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class CustomerManagedDatastoreS3StorageOutputTypeDef(
    _RequiredCustomerManagedDatastoreS3StorageOutputTypeDef,
    _OptionalCustomerManagedDatastoreS3StorageOutputTypeDef,
):
    pass


CustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_RequiredCustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
    },
)
_OptionalCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_OptionalCustomerManagedDatastoreS3StorageTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class CustomerManagedDatastoreS3StorageTypeDef(
    _RequiredCustomerManagedDatastoreS3StorageTypeDef,
    _OptionalCustomerManagedDatastoreS3StorageTypeDef,
):
    pass


DatasetActionSummaryTypeDef = TypedDict(
    "DatasetActionSummaryTypeDef",
    {
        "actionName": str,
        "actionType": DatasetActionTypeType,
    },
    total=False,
)

IotEventsDestinationConfigurationOutputTypeDef = TypedDict(
    "IotEventsDestinationConfigurationOutputTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)

IotEventsDestinationConfigurationTypeDef = TypedDict(
    "IotEventsDestinationConfigurationTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)

DatasetContentStatusTypeDef = TypedDict(
    "DatasetContentStatusTypeDef",
    {
        "state": DatasetContentStateType,
        "reason": str,
    },
    total=False,
)

DatasetContentVersionValueOutputTypeDef = TypedDict(
    "DatasetContentVersionValueOutputTypeDef",
    {
        "datasetName": str,
    },
)

DatasetContentVersionValueTypeDef = TypedDict(
    "DatasetContentVersionValueTypeDef",
    {
        "datasetName": str,
    },
)

DatasetEntryTypeDef = TypedDict(
    "DatasetEntryTypeDef",
    {
        "entryName": str,
        "dataURI": str,
    },
    total=False,
)

ScheduleOutputTypeDef = TypedDict(
    "ScheduleOutputTypeDef",
    {
        "expression": str,
    },
    total=False,
)

TriggeringDatasetOutputTypeDef = TypedDict(
    "TriggeringDatasetOutputTypeDef",
    {
        "name": str,
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "expression": str,
    },
    total=False,
)

TriggeringDatasetTypeDef = TypedDict(
    "TriggeringDatasetTypeDef",
    {
        "name": str,
    },
)

VersioningConfigurationOutputTypeDef = TypedDict(
    "VersioningConfigurationOutputTypeDef",
    {
        "unlimited": bool,
        "maxVersions": int,
    },
    total=False,
)

DatastoreActivityOutputTypeDef = TypedDict(
    "DatastoreActivityOutputTypeDef",
    {
        "name": str,
        "datastoreName": str,
    },
)

DatastoreActivityTypeDef = TypedDict(
    "DatastoreActivityTypeDef",
    {
        "name": str,
        "datastoreName": str,
    },
)

_RequiredIotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef = TypedDict(
    "_RequiredIotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef",
    {
        "bucket": str,
    },
)
_OptionalIotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef = TypedDict(
    "_OptionalIotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class IotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef(
    _RequiredIotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef,
    _OptionalIotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef,
):
    pass


IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
    },
    total=False,
)

_RequiredIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_RequiredIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
    },
)
_OptionalIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_OptionalIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)


class IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef(
    _RequiredIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef,
    _OptionalIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef,
):
    pass


PartitionOutputTypeDef = TypedDict(
    "PartitionOutputTypeDef",
    {
        "attributeName": str,
    },
)

_RequiredTimestampPartitionOutputTypeDef = TypedDict(
    "_RequiredTimestampPartitionOutputTypeDef",
    {
        "attributeName": str,
    },
)
_OptionalTimestampPartitionOutputTypeDef = TypedDict(
    "_OptionalTimestampPartitionOutputTypeDef",
    {
        "timestampFormat": str,
    },
    total=False,
)


class TimestampPartitionOutputTypeDef(
    _RequiredTimestampPartitionOutputTypeDef, _OptionalTimestampPartitionOutputTypeDef
):
    pass


PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "attributeName": str,
    },
)

_RequiredTimestampPartitionTypeDef = TypedDict(
    "_RequiredTimestampPartitionTypeDef",
    {
        "attributeName": str,
    },
)
_OptionalTimestampPartitionTypeDef = TypedDict(
    "_OptionalTimestampPartitionTypeDef",
    {
        "timestampFormat": str,
    },
    total=False,
)


class TimestampPartitionTypeDef(
    _RequiredTimestampPartitionTypeDef, _OptionalTimestampPartitionTypeDef
):
    pass


DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)

_RequiredDeleteDatasetContentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalDeleteDatasetContentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDatasetContentRequestRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)


class DeleteDatasetContentRequestRequestTypeDef(
    _RequiredDeleteDatasetContentRequestRequestTypeDef,
    _OptionalDeleteDatasetContentRequestRequestTypeDef,
):
    pass


DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)

DeleteDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)

DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)

DeltaTimeOutputTypeDef = TypedDict(
    "DeltaTimeOutputTypeDef",
    {
        "offsetSeconds": int,
        "timeExpression": str,
    },
)

DeltaTimeSessionWindowConfigurationOutputTypeDef = TypedDict(
    "DeltaTimeSessionWindowConfigurationOutputTypeDef",
    {
        "timeoutInMinutes": int,
    },
)

DeltaTimeSessionWindowConfigurationTypeDef = TypedDict(
    "DeltaTimeSessionWindowConfigurationTypeDef",
    {
        "timeoutInMinutes": int,
    },
)

DeltaTimeTypeDef = TypedDict(
    "DeltaTimeTypeDef",
    {
        "offsetSeconds": int,
        "timeExpression": str,
    },
)

_RequiredDescribeChannelRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalDescribeChannelRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelRequestRequestTypeDef",
    {
        "includeStatistics": bool,
    },
    total=False,
)


class DescribeChannelRequestRequestTypeDef(
    _RequiredDescribeChannelRequestRequestTypeDef, _OptionalDescribeChannelRequestRequestTypeDef
):
    pass


DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)

_RequiredDescribeDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalDescribeDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDatastoreRequestRequestTypeDef",
    {
        "includeStatistics": bool,
    },
    total=False,
)


class DescribeDatastoreRequestRequestTypeDef(
    _RequiredDescribeDatastoreRequestRequestTypeDef, _OptionalDescribeDatastoreRequestRequestTypeDef
):
    pass


LoggingOptionsOutputTypeDef = TypedDict(
    "LoggingOptionsOutputTypeDef",
    {
        "roleArn": str,
        "level": Literal["ERROR"],
        "enabled": bool,
    },
)

DescribePipelineRequestRequestTypeDef = TypedDict(
    "DescribePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)

_RequiredDeviceRegistryEnrichActivityOutputTypeDef = TypedDict(
    "_RequiredDeviceRegistryEnrichActivityOutputTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
    },
)
_OptionalDeviceRegistryEnrichActivityOutputTypeDef = TypedDict(
    "_OptionalDeviceRegistryEnrichActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class DeviceRegistryEnrichActivityOutputTypeDef(
    _RequiredDeviceRegistryEnrichActivityOutputTypeDef,
    _OptionalDeviceRegistryEnrichActivityOutputTypeDef,
):
    pass


_RequiredDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceRegistryEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
    },
)
_OptionalDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceRegistryEnrichActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class DeviceRegistryEnrichActivityTypeDef(
    _RequiredDeviceRegistryEnrichActivityTypeDef, _OptionalDeviceRegistryEnrichActivityTypeDef
):
    pass


_RequiredDeviceShadowEnrichActivityOutputTypeDef = TypedDict(
    "_RequiredDeviceShadowEnrichActivityOutputTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
    },
)
_OptionalDeviceShadowEnrichActivityOutputTypeDef = TypedDict(
    "_OptionalDeviceShadowEnrichActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class DeviceShadowEnrichActivityOutputTypeDef(
    _RequiredDeviceShadowEnrichActivityOutputTypeDef,
    _OptionalDeviceShadowEnrichActivityOutputTypeDef,
):
    pass


_RequiredDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceShadowEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
    },
)
_OptionalDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceShadowEnrichActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class DeviceShadowEnrichActivityTypeDef(
    _RequiredDeviceShadowEnrichActivityTypeDef, _OptionalDeviceShadowEnrichActivityTypeDef
):
    pass


EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFilterActivityOutputTypeDef = TypedDict(
    "_RequiredFilterActivityOutputTypeDef",
    {
        "name": str,
        "filter": str,
    },
)
_OptionalFilterActivityOutputTypeDef = TypedDict(
    "_OptionalFilterActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class FilterActivityOutputTypeDef(
    _RequiredFilterActivityOutputTypeDef, _OptionalFilterActivityOutputTypeDef
):
    pass


_RequiredFilterActivityTypeDef = TypedDict(
    "_RequiredFilterActivityTypeDef",
    {
        "name": str,
        "filter": str,
    },
)
_OptionalFilterActivityTypeDef = TypedDict(
    "_OptionalFilterActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class FilterActivityTypeDef(_RequiredFilterActivityTypeDef, _OptionalFilterActivityTypeDef):
    pass


_RequiredGetDatasetContentRequestRequestTypeDef = TypedDict(
    "_RequiredGetDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalGetDatasetContentRequestRequestTypeDef = TypedDict(
    "_OptionalGetDatasetContentRequestRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)


class GetDatasetContentRequestRequestTypeDef(
    _RequiredGetDatasetContentRequestRequestTypeDef, _OptionalGetDatasetContentRequestRequestTypeDef
):
    pass


GlueConfigurationOutputTypeDef = TypedDict(
    "GlueConfigurationOutputTypeDef",
    {
        "tableName": str,
        "databaseName": str,
    },
)

GlueConfigurationTypeDef = TypedDict(
    "GlueConfigurationTypeDef",
    {
        "tableName": str,
        "databaseName": str,
    },
)

_RequiredLambdaActivityOutputTypeDef = TypedDict(
    "_RequiredLambdaActivityOutputTypeDef",
    {
        "name": str,
        "lambdaName": str,
        "batchSize": int,
    },
)
_OptionalLambdaActivityOutputTypeDef = TypedDict(
    "_OptionalLambdaActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class LambdaActivityOutputTypeDef(
    _RequiredLambdaActivityOutputTypeDef, _OptionalLambdaActivityOutputTypeDef
):
    pass


_RequiredLambdaActivityTypeDef = TypedDict(
    "_RequiredLambdaActivityTypeDef",
    {
        "name": str,
        "lambdaName": str,
        "batchSize": int,
    },
)
_OptionalLambdaActivityTypeDef = TypedDict(
    "_OptionalLambdaActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class LambdaActivityTypeDef(_RequiredLambdaActivityTypeDef, _OptionalLambdaActivityTypeDef):
    pass


ListChannelsRequestListChannelsPaginateTypeDef = TypedDict(
    "ListChannelsRequestListChannelsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListDatasetContentsRequestListDatasetContentsPaginateTypeDef = TypedDict(
    "_RequiredListDatasetContentsRequestListDatasetContentsPaginateTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalListDatasetContentsRequestListDatasetContentsPaginateTypeDef = TypedDict(
    "_OptionalListDatasetContentsRequestListDatasetContentsPaginateTypeDef",
    {
        "scheduledOnOrAfter": Union[datetime, str],
        "scheduledBefore": Union[datetime, str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListDatasetContentsRequestListDatasetContentsPaginateTypeDef(
    _RequiredListDatasetContentsRequestListDatasetContentsPaginateTypeDef,
    _OptionalListDatasetContentsRequestListDatasetContentsPaginateTypeDef,
):
    pass


_RequiredListDatasetContentsRequestRequestTypeDef = TypedDict(
    "_RequiredListDatasetContentsRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalListDatasetContentsRequestRequestTypeDef = TypedDict(
    "_OptionalListDatasetContentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "scheduledOnOrAfter": Union[datetime, str],
        "scheduledBefore": Union[datetime, str],
    },
    total=False,
)


class ListDatasetContentsRequestRequestTypeDef(
    _RequiredListDatasetContentsRequestRequestTypeDef,
    _OptionalListDatasetContentsRequestRequestTypeDef,
):
    pass


ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatastoresRequestListDatastoresPaginateTypeDef = TypedDict(
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDatastoresRequestRequestTypeDef = TypedDict(
    "ListDatastoresRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPipelinesRequestListPipelinesPaginateTypeDef = TypedDict(
    "ListPipelinesRequestListPipelinesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
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

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": Literal["ERROR"],
        "enabled": bool,
    },
)

_RequiredMathActivityOutputTypeDef = TypedDict(
    "_RequiredMathActivityOutputTypeDef",
    {
        "name": str,
        "attribute": str,
        "math": str,
    },
)
_OptionalMathActivityOutputTypeDef = TypedDict(
    "_OptionalMathActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class MathActivityOutputTypeDef(
    _RequiredMathActivityOutputTypeDef, _OptionalMathActivityOutputTypeDef
):
    pass


_RequiredMathActivityTypeDef = TypedDict(
    "_RequiredMathActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "math": str,
    },
)
_OptionalMathActivityTypeDef = TypedDict(
    "_OptionalMathActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class MathActivityTypeDef(_RequiredMathActivityTypeDef, _OptionalMathActivityTypeDef):
    pass


OutputFileUriValueOutputTypeDef = TypedDict(
    "OutputFileUriValueOutputTypeDef",
    {
        "fileName": str,
    },
)

OutputFileUriValueTypeDef = TypedDict(
    "OutputFileUriValueTypeDef",
    {
        "fileName": str,
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

_RequiredRemoveAttributesActivityOutputTypeDef = TypedDict(
    "_RequiredRemoveAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": List[str],
    },
)
_OptionalRemoveAttributesActivityOutputTypeDef = TypedDict(
    "_OptionalRemoveAttributesActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class RemoveAttributesActivityOutputTypeDef(
    _RequiredRemoveAttributesActivityOutputTypeDef, _OptionalRemoveAttributesActivityOutputTypeDef
):
    pass


_RequiredSelectAttributesActivityOutputTypeDef = TypedDict(
    "_RequiredSelectAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": List[str],
    },
)
_OptionalSelectAttributesActivityOutputTypeDef = TypedDict(
    "_OptionalSelectAttributesActivityOutputTypeDef",
    {
        "next": str,
    },
    total=False,
)


class SelectAttributesActivityOutputTypeDef(
    _RequiredSelectAttributesActivityOutputTypeDef, _OptionalSelectAttributesActivityOutputTypeDef
):
    pass


_RequiredRemoveAttributesActivityTypeDef = TypedDict(
    "_RequiredRemoveAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Sequence[str],
    },
)
_OptionalRemoveAttributesActivityTypeDef = TypedDict(
    "_OptionalRemoveAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class RemoveAttributesActivityTypeDef(
    _RequiredRemoveAttributesActivityTypeDef, _OptionalRemoveAttributesActivityTypeDef
):
    pass


_RequiredSelectAttributesActivityTypeDef = TypedDict(
    "_RequiredSelectAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Sequence[str],
    },
)
_OptionalSelectAttributesActivityTypeDef = TypedDict(
    "_OptionalSelectAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)


class SelectAttributesActivityTypeDef(
    _RequiredSelectAttributesActivityTypeDef, _OptionalSelectAttributesActivityTypeDef
):
    pass


ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {
        "id": str,
        "status": ReprocessingStatusType,
        "creationTime": datetime,
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

RunPipelineActivityResponseTypeDef = TypedDict(
    "RunPipelineActivityResponseTypeDef",
    {
        "payloads": List[bytes],
        "logResult": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSampleChannelDataRequestRequestTypeDef = TypedDict(
    "_RequiredSampleChannelDataRequestRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalSampleChannelDataRequestRequestTypeDef = TypedDict(
    "_OptionalSampleChannelDataRequestRequestTypeDef",
    {
        "maxMessages": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
    total=False,
)


class SampleChannelDataRequestRequestTypeDef(
    _RequiredSampleChannelDataRequestRequestTypeDef, _OptionalSampleChannelDataRequestRequestTypeDef
):
    pass


SampleChannelDataResponseTypeDef = TypedDict(
    "SampleChannelDataResponseTypeDef",
    {
        "payloads": List[bytes],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartPipelineReprocessingResponseTypeDef = TypedDict(
    "StartPipelineReprocessingResponseTypeDef",
    {
        "reprocessingId": str,
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

BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {
        "batchPutMessageErrorEntries": List[BatchPutMessageErrorEntryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutMessageRequestRequestTypeDef = TypedDict(
    "BatchPutMessageRequestRequestTypeDef",
    {
        "channelName": str,
        "messages": Sequence[MessageTypeDef],
    },
)

_RequiredStartPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "_RequiredStartPipelineReprocessingRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalStartPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "_OptionalStartPipelineReprocessingRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "channelMessages": ChannelMessagesTypeDef,
    },
    total=False,
)


class StartPipelineReprocessingRequestRequestTypeDef(
    _RequiredStartPipelineReprocessingRequestRequestTypeDef,
    _OptionalStartPipelineReprocessingRequestRequestTypeDef,
):
    pass


ChannelStatisticsTypeDef = TypedDict(
    "ChannelStatisticsTypeDef",
    {
        "size": EstimatedResourceSizeTypeDef,
    },
    total=False,
)

DatastoreStatisticsTypeDef = TypedDict(
    "DatastoreStatisticsTypeDef",
    {
        "size": EstimatedResourceSizeTypeDef,
    },
    total=False,
)

ChannelStorageOutputTypeDef = TypedDict(
    "ChannelStorageOutputTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": CustomerManagedChannelS3StorageOutputTypeDef,
    },
    total=False,
)

ChannelStorageSummaryTypeDef = TypedDict(
    "ChannelStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": CustomerManagedChannelS3StorageSummaryTypeDef,
    },
    total=False,
)

ChannelStorageTypeDef = TypedDict(
    "ChannelStorageTypeDef",
    {
        "serviceManagedS3": Mapping[str, Any],
        "customerManagedS3": CustomerManagedChannelS3StorageTypeDef,
    },
    total=False,
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "channelName": str,
        "channelArn": str,
        "retentionPeriod": RetentionPeriodOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetName": str,
        "datasetArn": str,
        "retentionPeriod": RetentionPeriodOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatastoreResponseTypeDef = TypedDict(
    "CreateDatastoreResponseTypeDef",
    {
        "datastoreName": str,
        "datastoreArn": str,
        "retentionPeriod": RetentionPeriodOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SchemaDefinitionOutputTypeDef = TypedDict(
    "SchemaDefinitionOutputTypeDef",
    {
        "columns": List[ColumnOutputTypeDef],
    },
    total=False,
)

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": Sequence[ColumnTypeDef],
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

DatasetContentSummaryTypeDef = TypedDict(
    "DatasetContentSummaryTypeDef",
    {
        "version": str,
        "status": DatasetContentStatusTypeDef,
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)

GetDatasetContentResponseTypeDef = TypedDict(
    "GetDatasetContentResponseTypeDef",
    {
        "entries": List[DatasetEntryTypeDef],
        "timestamp": datetime,
        "status": DatasetContentStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatasetTriggerOutputTypeDef = TypedDict(
    "DatasetTriggerOutputTypeDef",
    {
        "schedule": ScheduleOutputTypeDef,
        "dataset": TriggeringDatasetOutputTypeDef,
    },
    total=False,
)

DatasetTriggerTypeDef = TypedDict(
    "DatasetTriggerTypeDef",
    {
        "schedule": ScheduleTypeDef,
        "dataset": TriggeringDatasetTypeDef,
    },
    total=False,
)

DatastoreIotSiteWiseMultiLayerStorageOutputTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageOutputTypeDef",
    {
        "customerManagedS3Storage": IotSiteWiseCustomerManagedDatastoreS3StorageOutputTypeDef,
    },
)

DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    {
        "customerManagedS3Storage": IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef,
    },
    total=False,
)

DatastoreIotSiteWiseMultiLayerStorageTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    {
        "customerManagedS3Storage": IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef,
    },
)

DatastorePartitionOutputTypeDef = TypedDict(
    "DatastorePartitionOutputTypeDef",
    {
        "attributePartition": PartitionOutputTypeDef,
        "timestampPartition": TimestampPartitionOutputTypeDef,
    },
    total=False,
)

DatastorePartitionTypeDef = TypedDict(
    "DatastorePartitionTypeDef",
    {
        "attributePartition": PartitionTypeDef,
        "timestampPartition": TimestampPartitionTypeDef,
    },
    total=False,
)

QueryFilterOutputTypeDef = TypedDict(
    "QueryFilterOutputTypeDef",
    {
        "deltaTime": DeltaTimeOutputTypeDef,
    },
    total=False,
)

LateDataRuleConfigurationOutputTypeDef = TypedDict(
    "LateDataRuleConfigurationOutputTypeDef",
    {
        "deltaTimeSessionWindowConfiguration": DeltaTimeSessionWindowConfigurationOutputTypeDef,
    },
    total=False,
)

LateDataRuleConfigurationTypeDef = TypedDict(
    "LateDataRuleConfigurationTypeDef",
    {
        "deltaTimeSessionWindowConfiguration": DeltaTimeSessionWindowConfigurationTypeDef,
    },
    total=False,
)

QueryFilterTypeDef = TypedDict(
    "QueryFilterTypeDef",
    {
        "deltaTime": DeltaTimeTypeDef,
    },
    total=False,
)

DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": LoggingOptionsOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredS3DestinationConfigurationOutputTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationOutputTypeDef",
    {
        "bucket": str,
        "key": str,
        "roleArn": str,
    },
)
_OptionalS3DestinationConfigurationOutputTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationOutputTypeDef",
    {
        "glueConfiguration": GlueConfigurationOutputTypeDef,
    },
    total=False,
)


class S3DestinationConfigurationOutputTypeDef(
    _RequiredS3DestinationConfigurationOutputTypeDef,
    _OptionalS3DestinationConfigurationOutputTypeDef,
):
    pass


_RequiredS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "roleArn": str,
    },
)
_OptionalS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationTypeDef",
    {
        "glueConfiguration": GlueConfigurationTypeDef,
    },
    total=False,
)


class S3DestinationConfigurationTypeDef(
    _RequiredS3DestinationConfigurationTypeDef, _OptionalS3DestinationConfigurationTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
    },
)

_RequiredVariableOutputTypeDef = TypedDict(
    "_RequiredVariableOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalVariableOutputTypeDef = TypedDict(
    "_OptionalVariableOutputTypeDef",
    {
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": DatasetContentVersionValueOutputTypeDef,
        "outputFileUriValue": OutputFileUriValueOutputTypeDef,
    },
    total=False,
)


class VariableOutputTypeDef(_RequiredVariableOutputTypeDef, _OptionalVariableOutputTypeDef):
    pass


_RequiredVariableTypeDef = TypedDict(
    "_RequiredVariableTypeDef",
    {
        "name": str,
    },
)
_OptionalVariableTypeDef = TypedDict(
    "_OptionalVariableTypeDef",
    {
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": DatasetContentVersionValueTypeDef,
        "outputFileUriValue": OutputFileUriValueTypeDef,
    },
    total=False,
)


class VariableTypeDef(_RequiredVariableTypeDef, _OptionalVariableTypeDef):
    pass


PipelineActivityOutputTypeDef = TypedDict(
    "PipelineActivityOutputTypeDef",
    {
        "channel": ChannelActivityOutputTypeDef,
        "lambda": LambdaActivityOutputTypeDef,
        "datastore": DatastoreActivityOutputTypeDef,
        "addAttributes": AddAttributesActivityOutputTypeDef,
        "removeAttributes": RemoveAttributesActivityOutputTypeDef,
        "selectAttributes": SelectAttributesActivityOutputTypeDef,
        "filter": FilterActivityOutputTypeDef,
        "math": MathActivityOutputTypeDef,
        "deviceRegistryEnrich": DeviceRegistryEnrichActivityOutputTypeDef,
        "deviceShadowEnrich": DeviceShadowEnrichActivityOutputTypeDef,
    },
    total=False,
)

PipelineActivityTypeDef = TypedDict(
    "PipelineActivityTypeDef",
    {
        "channel": ChannelActivityTypeDef,
        "lambda": LambdaActivityTypeDef,
        "datastore": DatastoreActivityTypeDef,
        "addAttributes": AddAttributesActivityTypeDef,
        "removeAttributes": RemoveAttributesActivityTypeDef,
        "selectAttributes": SelectAttributesActivityTypeDef,
        "filter": FilterActivityTypeDef,
        "math": MathActivityTypeDef,
        "deviceRegistryEnrich": DeviceRegistryEnrichActivityTypeDef,
        "deviceShadowEnrich": DeviceShadowEnrichActivityTypeDef,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List[ReprocessingSummaryTypeDef],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "name": str,
        "storage": ChannelStorageOutputTypeDef,
        "arn": str,
        "status": ChannelStatusType,
        "retentionPeriod": RetentionPeriodOutputTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
    },
    total=False,
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "channelName": str,
        "channelStorage": ChannelStorageSummaryTypeDef,
        "status": ChannelStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
    },
    total=False,
)

_RequiredCreateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "channelStorage": ChannelStorageTypeDef,
        "retentionPeriod": RetentionPeriodTypeDef,
        "tags": Sequence[TagTypeDef],
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
        "channelName": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "channelStorage": ChannelStorageTypeDef,
        "retentionPeriod": RetentionPeriodTypeDef,
    },
    total=False,
)


class UpdateChannelRequestRequestTypeDef(
    _RequiredUpdateChannelRequestRequestTypeDef, _OptionalUpdateChannelRequestRequestTypeDef
):
    pass


ParquetConfigurationOutputTypeDef = TypedDict(
    "ParquetConfigurationOutputTypeDef",
    {
        "schemaDefinition": SchemaDefinitionOutputTypeDef,
    },
    total=False,
)

ParquetConfigurationTypeDef = TypedDict(
    "ParquetConfigurationTypeDef",
    {
        "schemaDefinition": SchemaDefinitionTypeDef,
    },
    total=False,
)

ListDatasetContentsResponseTypeDef = TypedDict(
    "ListDatasetContentsResponseTypeDef",
    {
        "datasetContentSummaries": List[DatasetContentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "datasetName": str,
        "status": DatasetStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List[DatasetTriggerOutputTypeDef],
        "actions": List[DatasetActionSummaryTypeDef],
    },
    total=False,
)

DatastoreStorageOutputTypeDef = TypedDict(
    "DatastoreStorageOutputTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": CustomerManagedDatastoreS3StorageOutputTypeDef,
        "iotSiteWiseMultiLayerStorage": DatastoreIotSiteWiseMultiLayerStorageOutputTypeDef,
    },
    total=False,
)

DatastoreStorageSummaryTypeDef = TypedDict(
    "DatastoreStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": CustomerManagedDatastoreS3StorageSummaryTypeDef,
        "iotSiteWiseMultiLayerStorage": DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef,
    },
    total=False,
)

DatastoreStorageTypeDef = TypedDict(
    "DatastoreStorageTypeDef",
    {
        "serviceManagedS3": Mapping[str, Any],
        "customerManagedS3": CustomerManagedDatastoreS3StorageTypeDef,
        "iotSiteWiseMultiLayerStorage": DatastoreIotSiteWiseMultiLayerStorageTypeDef,
    },
    total=False,
)

DatastorePartitionsOutputTypeDef = TypedDict(
    "DatastorePartitionsOutputTypeDef",
    {
        "partitions": List[DatastorePartitionOutputTypeDef],
    },
    total=False,
)

DatastorePartitionsTypeDef = TypedDict(
    "DatastorePartitionsTypeDef",
    {
        "partitions": Sequence[DatastorePartitionTypeDef],
    },
    total=False,
)

_RequiredSqlQueryDatasetActionOutputTypeDef = TypedDict(
    "_RequiredSqlQueryDatasetActionOutputTypeDef",
    {
        "sqlQuery": str,
    },
)
_OptionalSqlQueryDatasetActionOutputTypeDef = TypedDict(
    "_OptionalSqlQueryDatasetActionOutputTypeDef",
    {
        "filters": List[QueryFilterOutputTypeDef],
    },
    total=False,
)


class SqlQueryDatasetActionOutputTypeDef(
    _RequiredSqlQueryDatasetActionOutputTypeDef, _OptionalSqlQueryDatasetActionOutputTypeDef
):
    pass


_RequiredLateDataRuleOutputTypeDef = TypedDict(
    "_RequiredLateDataRuleOutputTypeDef",
    {
        "ruleConfiguration": LateDataRuleConfigurationOutputTypeDef,
    },
)
_OptionalLateDataRuleOutputTypeDef = TypedDict(
    "_OptionalLateDataRuleOutputTypeDef",
    {
        "ruleName": str,
    },
    total=False,
)


class LateDataRuleOutputTypeDef(
    _RequiredLateDataRuleOutputTypeDef, _OptionalLateDataRuleOutputTypeDef
):
    pass


_RequiredLateDataRuleTypeDef = TypedDict(
    "_RequiredLateDataRuleTypeDef",
    {
        "ruleConfiguration": LateDataRuleConfigurationTypeDef,
    },
)
_OptionalLateDataRuleTypeDef = TypedDict(
    "_OptionalLateDataRuleTypeDef",
    {
        "ruleName": str,
    },
    total=False,
)


class LateDataRuleTypeDef(_RequiredLateDataRuleTypeDef, _OptionalLateDataRuleTypeDef):
    pass


_RequiredSqlQueryDatasetActionTypeDef = TypedDict(
    "_RequiredSqlQueryDatasetActionTypeDef",
    {
        "sqlQuery": str,
    },
)
_OptionalSqlQueryDatasetActionTypeDef = TypedDict(
    "_OptionalSqlQueryDatasetActionTypeDef",
    {
        "filters": Sequence[QueryFilterTypeDef],
    },
    total=False,
)


class SqlQueryDatasetActionTypeDef(
    _RequiredSqlQueryDatasetActionTypeDef, _OptionalSqlQueryDatasetActionTypeDef
):
    pass


DatasetContentDeliveryDestinationOutputTypeDef = TypedDict(
    "DatasetContentDeliveryDestinationOutputTypeDef",
    {
        "iotEventsDestinationConfiguration": IotEventsDestinationConfigurationOutputTypeDef,
        "s3DestinationConfiguration": S3DestinationConfigurationOutputTypeDef,
    },
    total=False,
)

DatasetContentDeliveryDestinationTypeDef = TypedDict(
    "DatasetContentDeliveryDestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": IotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": S3DestinationConfigurationTypeDef,
    },
    total=False,
)

_RequiredContainerDatasetActionOutputTypeDef = TypedDict(
    "_RequiredContainerDatasetActionOutputTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ResourceConfigurationOutputTypeDef,
    },
)
_OptionalContainerDatasetActionOutputTypeDef = TypedDict(
    "_OptionalContainerDatasetActionOutputTypeDef",
    {
        "variables": List[VariableOutputTypeDef],
    },
    total=False,
)


class ContainerDatasetActionOutputTypeDef(
    _RequiredContainerDatasetActionOutputTypeDef, _OptionalContainerDatasetActionOutputTypeDef
):
    pass


_RequiredContainerDatasetActionTypeDef = TypedDict(
    "_RequiredContainerDatasetActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ResourceConfigurationTypeDef,
    },
)
_OptionalContainerDatasetActionTypeDef = TypedDict(
    "_OptionalContainerDatasetActionTypeDef",
    {
        "variables": Sequence[VariableTypeDef],
    },
    total=False,
)


class ContainerDatasetActionTypeDef(
    _RequiredContainerDatasetActionTypeDef, _OptionalContainerDatasetActionTypeDef
):
    pass


PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "name": str,
        "arn": str,
        "activities": List[PipelineActivityOutputTypeDef],
        "reprocessingSummaries": List[ReprocessingSummaryTypeDef],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

_RequiredCreatePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": Sequence[PipelineActivityTypeDef],
    },
)
_OptionalCreatePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreatePipelineRequestRequestTypeDef(
    _RequiredCreatePipelineRequestRequestTypeDef, _OptionalCreatePipelineRequestRequestTypeDef
):
    pass


RunPipelineActivityRequestRequestTypeDef = TypedDict(
    "RunPipelineActivityRequestRequestTypeDef",
    {
        "pipelineActivity": PipelineActivityTypeDef,
        "payloads": Sequence[Union[str, bytes, IO[Any], StreamingBody]],
    },
)

UpdatePipelineRequestRequestTypeDef = TypedDict(
    "UpdatePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": Sequence[PipelineActivityTypeDef],
    },
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "pipelineSummaries": List[PipelineSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "channel": ChannelTypeDef,
        "statistics": ChannelStatisticsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "channelSummaries": List[ChannelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FileFormatConfigurationOutputTypeDef = TypedDict(
    "FileFormatConfigurationOutputTypeDef",
    {
        "jsonConfiguration": Dict[str, Any],
        "parquetConfiguration": ParquetConfigurationOutputTypeDef,
    },
    total=False,
)

FileFormatConfigurationTypeDef = TypedDict(
    "FileFormatConfigurationTypeDef",
    {
        "jsonConfiguration": Mapping[str, Any],
        "parquetConfiguration": ParquetConfigurationTypeDef,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasetSummaries": List[DatasetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": DatastoreStorageSummaryTypeDef,
        "status": DatastoreStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
        "fileFormatType": FileFormatTypeType,
        "datastorePartitions": DatastorePartitionsOutputTypeDef,
    },
    total=False,
)

_RequiredDatasetContentDeliveryRuleOutputTypeDef = TypedDict(
    "_RequiredDatasetContentDeliveryRuleOutputTypeDef",
    {
        "destination": DatasetContentDeliveryDestinationOutputTypeDef,
    },
)
_OptionalDatasetContentDeliveryRuleOutputTypeDef = TypedDict(
    "_OptionalDatasetContentDeliveryRuleOutputTypeDef",
    {
        "entryName": str,
    },
    total=False,
)


class DatasetContentDeliveryRuleOutputTypeDef(
    _RequiredDatasetContentDeliveryRuleOutputTypeDef,
    _OptionalDatasetContentDeliveryRuleOutputTypeDef,
):
    pass


_RequiredDatasetContentDeliveryRuleTypeDef = TypedDict(
    "_RequiredDatasetContentDeliveryRuleTypeDef",
    {
        "destination": DatasetContentDeliveryDestinationTypeDef,
    },
)
_OptionalDatasetContentDeliveryRuleTypeDef = TypedDict(
    "_OptionalDatasetContentDeliveryRuleTypeDef",
    {
        "entryName": str,
    },
    total=False,
)


class DatasetContentDeliveryRuleTypeDef(
    _RequiredDatasetContentDeliveryRuleTypeDef, _OptionalDatasetContentDeliveryRuleTypeDef
):
    pass


DatasetActionOutputTypeDef = TypedDict(
    "DatasetActionOutputTypeDef",
    {
        "actionName": str,
        "queryAction": SqlQueryDatasetActionOutputTypeDef,
        "containerAction": ContainerDatasetActionOutputTypeDef,
    },
    total=False,
)

DatasetActionTypeDef = TypedDict(
    "DatasetActionTypeDef",
    {
        "actionName": str,
        "queryAction": SqlQueryDatasetActionTypeDef,
        "containerAction": ContainerDatasetActionTypeDef,
    },
    total=False,
)

DescribePipelineResponseTypeDef = TypedDict(
    "DescribePipelineResponseTypeDef",
    {
        "pipeline": PipelineTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatastoreTypeDef = TypedDict(
    "DatastoreTypeDef",
    {
        "name": str,
        "storage": DatastoreStorageOutputTypeDef,
        "arn": str,
        "status": DatastoreStatusType,
        "retentionPeriod": RetentionPeriodOutputTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
        "fileFormatConfiguration": FileFormatConfigurationOutputTypeDef,
        "datastorePartitions": DatastorePartitionsOutputTypeDef,
    },
    total=False,
)

_RequiredCreateDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalCreateDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatastoreRequestRequestTypeDef",
    {
        "datastoreStorage": DatastoreStorageTypeDef,
        "retentionPeriod": RetentionPeriodTypeDef,
        "tags": Sequence[TagTypeDef],
        "fileFormatConfiguration": FileFormatConfigurationTypeDef,
        "datastorePartitions": DatastorePartitionsTypeDef,
    },
    total=False,
)


class CreateDatastoreRequestRequestTypeDef(
    _RequiredCreateDatastoreRequestRequestTypeDef, _OptionalCreateDatastoreRequestRequestTypeDef
):
    pass


_RequiredUpdateDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalUpdateDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatastoreRequestRequestTypeDef",
    {
        "retentionPeriod": RetentionPeriodTypeDef,
        "datastoreStorage": DatastoreStorageTypeDef,
        "fileFormatConfiguration": FileFormatConfigurationTypeDef,
    },
    total=False,
)


class UpdateDatastoreRequestRequestTypeDef(
    _RequiredUpdateDatastoreRequestRequestTypeDef, _OptionalUpdateDatastoreRequestRequestTypeDef
):
    pass


ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List[DatastoreSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": str,
        "arn": str,
        "actions": List[DatasetActionOutputTypeDef],
        "triggers": List[DatasetTriggerOutputTypeDef],
        "contentDeliveryRules": List[DatasetContentDeliveryRuleOutputTypeDef],
        "status": DatasetStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "retentionPeriod": RetentionPeriodOutputTypeDef,
        "versioningConfiguration": VersioningConfigurationOutputTypeDef,
        "lateDataRules": List[LateDataRuleOutputTypeDef],
    },
    total=False,
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
        "actions": Sequence[DatasetActionTypeDef],
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "triggers": Sequence[DatasetTriggerTypeDef],
        "contentDeliveryRules": Sequence[DatasetContentDeliveryRuleTypeDef],
        "retentionPeriod": RetentionPeriodTypeDef,
        "versioningConfiguration": VersioningConfigurationTypeDef,
        "tags": Sequence[TagTypeDef],
        "lateDataRules": Sequence[LateDataRuleTypeDef],
    },
    total=False,
)


class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass


_RequiredUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
        "actions": Sequence[DatasetActionTypeDef],
    },
)
_OptionalUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestRequestTypeDef",
    {
        "triggers": Sequence[DatasetTriggerTypeDef],
        "contentDeliveryRules": Sequence[DatasetContentDeliveryRuleTypeDef],
        "retentionPeriod": RetentionPeriodTypeDef,
        "versioningConfiguration": VersioningConfigurationTypeDef,
        "lateDataRules": Sequence[LateDataRuleTypeDef],
    },
    total=False,
)


class UpdateDatasetRequestRequestTypeDef(
    _RequiredUpdateDatasetRequestRequestTypeDef, _OptionalUpdateDatasetRequestRequestTypeDef
):
    pass


DescribeDatastoreResponseTypeDef = TypedDict(
    "DescribeDatastoreResponseTypeDef",
    {
        "datastore": DatastoreTypeDef,
        "statistics": DatastoreStatisticsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "dataset": DatasetTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
