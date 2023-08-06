"""
Type annotations for firehose service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_firehose/type_defs/)

Usage::

    ```python
    from mypy_boto3_firehose.type_defs import AmazonOpenSearchServerlessBufferingHintsOutputTypeDef

    data: AmazonOpenSearchServerlessBufferingHintsOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AmazonOpenSearchServerlessS3BackupModeType,
    AmazonopensearchserviceIndexRotationPeriodType,
    AmazonopensearchserviceS3BackupModeType,
    CompressionFormatType,
    ContentEncodingType,
    DeliveryStreamEncryptionStatusType,
    DeliveryStreamFailureTypeType,
    DeliveryStreamStatusType,
    DeliveryStreamTypeType,
    ElasticsearchIndexRotationPeriodType,
    ElasticsearchS3BackupModeType,
    HECEndpointTypeType,
    HttpEndpointS3BackupModeType,
    KeyTypeType,
    OrcCompressionType,
    OrcFormatVersionType,
    ParquetCompressionType,
    ParquetWriterVersionType,
    ProcessorParameterNameType,
    ProcessorTypeType,
    RedshiftS3BackupModeType,
    S3BackupModeType,
    SplunkS3BackupModeType,
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
    "AmazonOpenSearchServerlessBufferingHintsOutputTypeDef",
    "AmazonOpenSearchServerlessBufferingHintsTypeDef",
    "AmazonOpenSearchServerlessRetryOptionsTypeDef",
    "CloudWatchLoggingOptionsTypeDef",
    "VpcConfigurationTypeDef",
    "AmazonOpenSearchServerlessRetryOptionsOutputTypeDef",
    "CloudWatchLoggingOptionsOutputTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "AmazonopensearchserviceBufferingHintsOutputTypeDef",
    "AmazonopensearchserviceBufferingHintsTypeDef",
    "AmazonopensearchserviceRetryOptionsTypeDef",
    "AmazonopensearchserviceRetryOptionsOutputTypeDef",
    "BufferingHintsOutputTypeDef",
    "BufferingHintsTypeDef",
    "CopyCommandOutputTypeDef",
    "CopyCommandTypeDef",
    "DeliveryStreamEncryptionConfigurationInputTypeDef",
    "KinesisStreamSourceConfigurationTypeDef",
    "TagTypeDef",
    "CreateDeliveryStreamOutputTypeDef",
    "SchemaConfigurationOutputTypeDef",
    "SchemaConfigurationTypeDef",
    "DeleteDeliveryStreamInputRequestTypeDef",
    "FailureDescriptionTypeDef",
    "DescribeDeliveryStreamInputRequestTypeDef",
    "HiveJsonSerDeOutputTypeDef",
    "OpenXJsonSerDeOutputTypeDef",
    "HiveJsonSerDeTypeDef",
    "OpenXJsonSerDeTypeDef",
    "RetryOptionsOutputTypeDef",
    "RetryOptionsTypeDef",
    "ElasticsearchBufferingHintsOutputTypeDef",
    "ElasticsearchBufferingHintsTypeDef",
    "ElasticsearchRetryOptionsTypeDef",
    "ElasticsearchRetryOptionsOutputTypeDef",
    "KMSEncryptionConfigOutputTypeDef",
    "KMSEncryptionConfigTypeDef",
    "HttpEndpointBufferingHintsOutputTypeDef",
    "HttpEndpointBufferingHintsTypeDef",
    "HttpEndpointCommonAttributeOutputTypeDef",
    "HttpEndpointCommonAttributeTypeDef",
    "HttpEndpointConfigurationTypeDef",
    "HttpEndpointDescriptionTypeDef",
    "HttpEndpointRetryOptionsTypeDef",
    "HttpEndpointRetryOptionsOutputTypeDef",
    "KinesisStreamSourceDescriptionTypeDef",
    "ListDeliveryStreamsInputRequestTypeDef",
    "ListDeliveryStreamsOutputTypeDef",
    "ListTagsForDeliveryStreamInputRequestTypeDef",
    "TagOutputTypeDef",
    "OrcSerDeOutputTypeDef",
    "OrcSerDeTypeDef",
    "ParquetSerDeOutputTypeDef",
    "ParquetSerDeTypeDef",
    "ProcessorParameterOutputTypeDef",
    "ProcessorParameterTypeDef",
    "RecordTypeDef",
    "PutRecordBatchResponseEntryTypeDef",
    "PutRecordOutputTypeDef",
    "RedshiftRetryOptionsTypeDef",
    "RedshiftRetryOptionsOutputTypeDef",
    "ResponseMetadataTypeDef",
    "SplunkRetryOptionsTypeDef",
    "SplunkRetryOptionsOutputTypeDef",
    "StopDeliveryStreamEncryptionInputRequestTypeDef",
    "UntagDeliveryStreamInputRequestTypeDef",
    "StartDeliveryStreamEncryptionInputRequestTypeDef",
    "TagDeliveryStreamInputRequestTypeDef",
    "DeliveryStreamEncryptionConfigurationTypeDef",
    "DeserializerOutputTypeDef",
    "DeserializerTypeDef",
    "DynamicPartitioningConfigurationOutputTypeDef",
    "DynamicPartitioningConfigurationTypeDef",
    "EncryptionConfigurationOutputTypeDef",
    "EncryptionConfigurationTypeDef",
    "HttpEndpointRequestConfigurationOutputTypeDef",
    "HttpEndpointRequestConfigurationTypeDef",
    "SourceDescriptionTypeDef",
    "ListTagsForDeliveryStreamOutputTypeDef",
    "SerializerOutputTypeDef",
    "SerializerTypeDef",
    "ProcessorOutputTypeDef",
    "ProcessorTypeDef",
    "PutRecordBatchInputRequestTypeDef",
    "PutRecordInputRequestTypeDef",
    "PutRecordBatchOutputTypeDef",
    "InputFormatConfigurationOutputTypeDef",
    "InputFormatConfigurationTypeDef",
    "S3DestinationDescriptionTypeDef",
    "S3DestinationConfigurationTypeDef",
    "S3DestinationUpdateTypeDef",
    "OutputFormatConfigurationOutputTypeDef",
    "OutputFormatConfigurationTypeDef",
    "ProcessingConfigurationOutputTypeDef",
    "ProcessingConfigurationTypeDef",
    "DataFormatConversionConfigurationOutputTypeDef",
    "DataFormatConversionConfigurationTypeDef",
    "AmazonOpenSearchServerlessDestinationDescriptionTypeDef",
    "AmazonopensearchserviceDestinationDescriptionTypeDef",
    "ElasticsearchDestinationDescriptionTypeDef",
    "HttpEndpointDestinationDescriptionTypeDef",
    "RedshiftDestinationDescriptionTypeDef",
    "SplunkDestinationDescriptionTypeDef",
    "AmazonOpenSearchServerlessDestinationConfigurationTypeDef",
    "AmazonOpenSearchServerlessDestinationUpdateTypeDef",
    "AmazonopensearchserviceDestinationConfigurationTypeDef",
    "AmazonopensearchserviceDestinationUpdateTypeDef",
    "ElasticsearchDestinationConfigurationTypeDef",
    "ElasticsearchDestinationUpdateTypeDef",
    "HttpEndpointDestinationConfigurationTypeDef",
    "HttpEndpointDestinationUpdateTypeDef",
    "RedshiftDestinationConfigurationTypeDef",
    "RedshiftDestinationUpdateTypeDef",
    "SplunkDestinationConfigurationTypeDef",
    "SplunkDestinationUpdateTypeDef",
    "ExtendedS3DestinationDescriptionTypeDef",
    "ExtendedS3DestinationConfigurationTypeDef",
    "ExtendedS3DestinationUpdateTypeDef",
    "DestinationDescriptionTypeDef",
    "CreateDeliveryStreamInputRequestTypeDef",
    "UpdateDestinationInputRequestTypeDef",
    "DeliveryStreamDescriptionTypeDef",
    "DescribeDeliveryStreamOutputTypeDef",
)

AmazonOpenSearchServerlessBufferingHintsOutputTypeDef = TypedDict(
    "AmazonOpenSearchServerlessBufferingHintsOutputTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

AmazonOpenSearchServerlessBufferingHintsTypeDef = TypedDict(
    "AmazonOpenSearchServerlessBufferingHintsTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

AmazonOpenSearchServerlessRetryOptionsTypeDef = TypedDict(
    "AmazonOpenSearchServerlessRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

CloudWatchLoggingOptionsTypeDef = TypedDict(
    "CloudWatchLoggingOptionsTypeDef",
    {
        "Enabled": bool,
        "LogGroupName": str,
        "LogStreamName": str,
    },
    total=False,
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIds": Sequence[str],
        "RoleARN": str,
        "SecurityGroupIds": Sequence[str],
    },
)

AmazonOpenSearchServerlessRetryOptionsOutputTypeDef = TypedDict(
    "AmazonOpenSearchServerlessRetryOptionsOutputTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

CloudWatchLoggingOptionsOutputTypeDef = TypedDict(
    "CloudWatchLoggingOptionsOutputTypeDef",
    {
        "Enabled": bool,
        "LogGroupName": str,
        "LogStreamName": str,
    },
    total=False,
)

VpcConfigurationDescriptionTypeDef = TypedDict(
    "VpcConfigurationDescriptionTypeDef",
    {
        "SubnetIds": List[str],
        "RoleARN": str,
        "SecurityGroupIds": List[str],
        "VpcId": str,
    },
)

AmazonopensearchserviceBufferingHintsOutputTypeDef = TypedDict(
    "AmazonopensearchserviceBufferingHintsOutputTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

AmazonopensearchserviceBufferingHintsTypeDef = TypedDict(
    "AmazonopensearchserviceBufferingHintsTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

AmazonopensearchserviceRetryOptionsTypeDef = TypedDict(
    "AmazonopensearchserviceRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

AmazonopensearchserviceRetryOptionsOutputTypeDef = TypedDict(
    "AmazonopensearchserviceRetryOptionsOutputTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

BufferingHintsOutputTypeDef = TypedDict(
    "BufferingHintsOutputTypeDef",
    {
        "SizeInMBs": int,
        "IntervalInSeconds": int,
    },
    total=False,
)

BufferingHintsTypeDef = TypedDict(
    "BufferingHintsTypeDef",
    {
        "SizeInMBs": int,
        "IntervalInSeconds": int,
    },
    total=False,
)

_RequiredCopyCommandOutputTypeDef = TypedDict(
    "_RequiredCopyCommandOutputTypeDef",
    {
        "DataTableName": str,
    },
)
_OptionalCopyCommandOutputTypeDef = TypedDict(
    "_OptionalCopyCommandOutputTypeDef",
    {
        "DataTableColumns": str,
        "CopyOptions": str,
    },
    total=False,
)


class CopyCommandOutputTypeDef(
    _RequiredCopyCommandOutputTypeDef, _OptionalCopyCommandOutputTypeDef
):
    pass


_RequiredCopyCommandTypeDef = TypedDict(
    "_RequiredCopyCommandTypeDef",
    {
        "DataTableName": str,
    },
)
_OptionalCopyCommandTypeDef = TypedDict(
    "_OptionalCopyCommandTypeDef",
    {
        "DataTableColumns": str,
        "CopyOptions": str,
    },
    total=False,
)


class CopyCommandTypeDef(_RequiredCopyCommandTypeDef, _OptionalCopyCommandTypeDef):
    pass


_RequiredDeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "_RequiredDeliveryStreamEncryptionConfigurationInputTypeDef",
    {
        "KeyType": KeyTypeType,
    },
)
_OptionalDeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "_OptionalDeliveryStreamEncryptionConfigurationInputTypeDef",
    {
        "KeyARN": str,
    },
    total=False,
)


class DeliveryStreamEncryptionConfigurationInputTypeDef(
    _RequiredDeliveryStreamEncryptionConfigurationInputTypeDef,
    _OptionalDeliveryStreamEncryptionConfigurationInputTypeDef,
):
    pass


KinesisStreamSourceConfigurationTypeDef = TypedDict(
    "KinesisStreamSourceConfigurationTypeDef",
    {
        "KinesisStreamARN": str,
        "RoleARN": str,
    },
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


CreateDeliveryStreamOutputTypeDef = TypedDict(
    "CreateDeliveryStreamOutputTypeDef",
    {
        "DeliveryStreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SchemaConfigurationOutputTypeDef = TypedDict(
    "SchemaConfigurationOutputTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)

SchemaConfigurationTypeDef = TypedDict(
    "SchemaConfigurationTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)

_RequiredDeleteDeliveryStreamInputRequestTypeDef = TypedDict(
    "_RequiredDeleteDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalDeleteDeliveryStreamInputRequestTypeDef = TypedDict(
    "_OptionalDeleteDeliveryStreamInputRequestTypeDef",
    {
        "AllowForceDelete": bool,
    },
    total=False,
)


class DeleteDeliveryStreamInputRequestTypeDef(
    _RequiredDeleteDeliveryStreamInputRequestTypeDef,
    _OptionalDeleteDeliveryStreamInputRequestTypeDef,
):
    pass


FailureDescriptionTypeDef = TypedDict(
    "FailureDescriptionTypeDef",
    {
        "Type": DeliveryStreamFailureTypeType,
        "Details": str,
    },
)

_RequiredDescribeDeliveryStreamInputRequestTypeDef = TypedDict(
    "_RequiredDescribeDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalDescribeDeliveryStreamInputRequestTypeDef = TypedDict(
    "_OptionalDescribeDeliveryStreamInputRequestTypeDef",
    {
        "Limit": int,
        "ExclusiveStartDestinationId": str,
    },
    total=False,
)


class DescribeDeliveryStreamInputRequestTypeDef(
    _RequiredDescribeDeliveryStreamInputRequestTypeDef,
    _OptionalDescribeDeliveryStreamInputRequestTypeDef,
):
    pass


HiveJsonSerDeOutputTypeDef = TypedDict(
    "HiveJsonSerDeOutputTypeDef",
    {
        "TimestampFormats": List[str],
    },
    total=False,
)

OpenXJsonSerDeOutputTypeDef = TypedDict(
    "OpenXJsonSerDeOutputTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Dict[str, str],
    },
    total=False,
)

HiveJsonSerDeTypeDef = TypedDict(
    "HiveJsonSerDeTypeDef",
    {
        "TimestampFormats": Sequence[str],
    },
    total=False,
)

OpenXJsonSerDeTypeDef = TypedDict(
    "OpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Mapping[str, str],
    },
    total=False,
)

RetryOptionsOutputTypeDef = TypedDict(
    "RetryOptionsOutputTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

RetryOptionsTypeDef = TypedDict(
    "RetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

ElasticsearchBufferingHintsOutputTypeDef = TypedDict(
    "ElasticsearchBufferingHintsOutputTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

ElasticsearchBufferingHintsTypeDef = TypedDict(
    "ElasticsearchBufferingHintsTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

ElasticsearchRetryOptionsTypeDef = TypedDict(
    "ElasticsearchRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

ElasticsearchRetryOptionsOutputTypeDef = TypedDict(
    "ElasticsearchRetryOptionsOutputTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

KMSEncryptionConfigOutputTypeDef = TypedDict(
    "KMSEncryptionConfigOutputTypeDef",
    {
        "AWSKMSKeyARN": str,
    },
)

KMSEncryptionConfigTypeDef = TypedDict(
    "KMSEncryptionConfigTypeDef",
    {
        "AWSKMSKeyARN": str,
    },
)

HttpEndpointBufferingHintsOutputTypeDef = TypedDict(
    "HttpEndpointBufferingHintsOutputTypeDef",
    {
        "SizeInMBs": int,
        "IntervalInSeconds": int,
    },
    total=False,
)

HttpEndpointBufferingHintsTypeDef = TypedDict(
    "HttpEndpointBufferingHintsTypeDef",
    {
        "SizeInMBs": int,
        "IntervalInSeconds": int,
    },
    total=False,
)

HttpEndpointCommonAttributeOutputTypeDef = TypedDict(
    "HttpEndpointCommonAttributeOutputTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
    },
)

HttpEndpointCommonAttributeTypeDef = TypedDict(
    "HttpEndpointCommonAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
    },
)

_RequiredHttpEndpointConfigurationTypeDef = TypedDict(
    "_RequiredHttpEndpointConfigurationTypeDef",
    {
        "Url": str,
    },
)
_OptionalHttpEndpointConfigurationTypeDef = TypedDict(
    "_OptionalHttpEndpointConfigurationTypeDef",
    {
        "Name": str,
        "AccessKey": str,
    },
    total=False,
)


class HttpEndpointConfigurationTypeDef(
    _RequiredHttpEndpointConfigurationTypeDef, _OptionalHttpEndpointConfigurationTypeDef
):
    pass


HttpEndpointDescriptionTypeDef = TypedDict(
    "HttpEndpointDescriptionTypeDef",
    {
        "Url": str,
        "Name": str,
    },
    total=False,
)

HttpEndpointRetryOptionsTypeDef = TypedDict(
    "HttpEndpointRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

HttpEndpointRetryOptionsOutputTypeDef = TypedDict(
    "HttpEndpointRetryOptionsOutputTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

KinesisStreamSourceDescriptionTypeDef = TypedDict(
    "KinesisStreamSourceDescriptionTypeDef",
    {
        "KinesisStreamARN": str,
        "RoleARN": str,
        "DeliveryStartTimestamp": datetime,
    },
    total=False,
)

ListDeliveryStreamsInputRequestTypeDef = TypedDict(
    "ListDeliveryStreamsInputRequestTypeDef",
    {
        "Limit": int,
        "DeliveryStreamType": DeliveryStreamTypeType,
        "ExclusiveStartDeliveryStreamName": str,
    },
    total=False,
)

ListDeliveryStreamsOutputTypeDef = TypedDict(
    "ListDeliveryStreamsOutputTypeDef",
    {
        "DeliveryStreamNames": List[str],
        "HasMoreDeliveryStreams": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForDeliveryStreamInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalListTagsForDeliveryStreamInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForDeliveryStreamInputRequestTypeDef",
    {
        "ExclusiveStartTagKey": str,
        "Limit": int,
    },
    total=False,
)


class ListTagsForDeliveryStreamInputRequestTypeDef(
    _RequiredListTagsForDeliveryStreamInputRequestTypeDef,
    _OptionalListTagsForDeliveryStreamInputRequestTypeDef,
):
    pass


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


OrcSerDeOutputTypeDef = TypedDict(
    "OrcSerDeOutputTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": OrcCompressionType,
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": OrcFormatVersionType,
    },
    total=False,
)

OrcSerDeTypeDef = TypedDict(
    "OrcSerDeTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": OrcCompressionType,
        "BloomFilterColumns": Sequence[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": OrcFormatVersionType,
    },
    total=False,
)

ParquetSerDeOutputTypeDef = TypedDict(
    "ParquetSerDeOutputTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": ParquetCompressionType,
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": ParquetWriterVersionType,
    },
    total=False,
)

ParquetSerDeTypeDef = TypedDict(
    "ParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": ParquetCompressionType,
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": ParquetWriterVersionType,
    },
    total=False,
)

ProcessorParameterOutputTypeDef = TypedDict(
    "ProcessorParameterOutputTypeDef",
    {
        "ParameterName": ProcessorParameterNameType,
        "ParameterValue": str,
    },
)

ProcessorParameterTypeDef = TypedDict(
    "ProcessorParameterTypeDef",
    {
        "ParameterName": ProcessorParameterNameType,
        "ParameterValue": str,
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Data": Union[str, bytes, IO[Any], StreamingBody],
    },
)

PutRecordBatchResponseEntryTypeDef = TypedDict(
    "PutRecordBatchResponseEntryTypeDef",
    {
        "RecordId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutRecordOutputTypeDef = TypedDict(
    "PutRecordOutputTypeDef",
    {
        "RecordId": str,
        "Encrypted": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedshiftRetryOptionsTypeDef = TypedDict(
    "RedshiftRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

RedshiftRetryOptionsOutputTypeDef = TypedDict(
    "RedshiftRetryOptionsOutputTypeDef",
    {
        "DurationInSeconds": int,
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

SplunkRetryOptionsTypeDef = TypedDict(
    "SplunkRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

SplunkRetryOptionsOutputTypeDef = TypedDict(
    "SplunkRetryOptionsOutputTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

StopDeliveryStreamEncryptionInputRequestTypeDef = TypedDict(
    "StopDeliveryStreamEncryptionInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)

UntagDeliveryStreamInputRequestTypeDef = TypedDict(
    "UntagDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredStartDeliveryStreamEncryptionInputRequestTypeDef = TypedDict(
    "_RequiredStartDeliveryStreamEncryptionInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalStartDeliveryStreamEncryptionInputRequestTypeDef = TypedDict(
    "_OptionalStartDeliveryStreamEncryptionInputRequestTypeDef",
    {
        "DeliveryStreamEncryptionConfigurationInput": (
            DeliveryStreamEncryptionConfigurationInputTypeDef
        ),
    },
    total=False,
)


class StartDeliveryStreamEncryptionInputRequestTypeDef(
    _RequiredStartDeliveryStreamEncryptionInputRequestTypeDef,
    _OptionalStartDeliveryStreamEncryptionInputRequestTypeDef,
):
    pass


TagDeliveryStreamInputRequestTypeDef = TypedDict(
    "TagDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Tags": Sequence[TagTypeDef],
    },
)

DeliveryStreamEncryptionConfigurationTypeDef = TypedDict(
    "DeliveryStreamEncryptionConfigurationTypeDef",
    {
        "KeyARN": str,
        "KeyType": KeyTypeType,
        "Status": DeliveryStreamEncryptionStatusType,
        "FailureDescription": FailureDescriptionTypeDef,
    },
    total=False,
)

DeserializerOutputTypeDef = TypedDict(
    "DeserializerOutputTypeDef",
    {
        "OpenXJsonSerDe": OpenXJsonSerDeOutputTypeDef,
        "HiveJsonSerDe": HiveJsonSerDeOutputTypeDef,
    },
    total=False,
)

DeserializerTypeDef = TypedDict(
    "DeserializerTypeDef",
    {
        "OpenXJsonSerDe": OpenXJsonSerDeTypeDef,
        "HiveJsonSerDe": HiveJsonSerDeTypeDef,
    },
    total=False,
)

DynamicPartitioningConfigurationOutputTypeDef = TypedDict(
    "DynamicPartitioningConfigurationOutputTypeDef",
    {
        "RetryOptions": RetryOptionsOutputTypeDef,
        "Enabled": bool,
    },
    total=False,
)

DynamicPartitioningConfigurationTypeDef = TypedDict(
    "DynamicPartitioningConfigurationTypeDef",
    {
        "RetryOptions": RetryOptionsTypeDef,
        "Enabled": bool,
    },
    total=False,
)

EncryptionConfigurationOutputTypeDef = TypedDict(
    "EncryptionConfigurationOutputTypeDef",
    {
        "NoEncryptionConfig": Literal["NoEncryption"],
        "KMSEncryptionConfig": KMSEncryptionConfigOutputTypeDef,
    },
    total=False,
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": Literal["NoEncryption"],
        "KMSEncryptionConfig": KMSEncryptionConfigTypeDef,
    },
    total=False,
)

HttpEndpointRequestConfigurationOutputTypeDef = TypedDict(
    "HttpEndpointRequestConfigurationOutputTypeDef",
    {
        "ContentEncoding": ContentEncodingType,
        "CommonAttributes": List[HttpEndpointCommonAttributeOutputTypeDef],
    },
    total=False,
)

HttpEndpointRequestConfigurationTypeDef = TypedDict(
    "HttpEndpointRequestConfigurationTypeDef",
    {
        "ContentEncoding": ContentEncodingType,
        "CommonAttributes": Sequence[HttpEndpointCommonAttributeTypeDef],
    },
    total=False,
)

SourceDescriptionTypeDef = TypedDict(
    "SourceDescriptionTypeDef",
    {
        "KinesisStreamSourceDescription": KinesisStreamSourceDescriptionTypeDef,
    },
    total=False,
)

ListTagsForDeliveryStreamOutputTypeDef = TypedDict(
    "ListTagsForDeliveryStreamOutputTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "HasMoreTags": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SerializerOutputTypeDef = TypedDict(
    "SerializerOutputTypeDef",
    {
        "ParquetSerDe": ParquetSerDeOutputTypeDef,
        "OrcSerDe": OrcSerDeOutputTypeDef,
    },
    total=False,
)

SerializerTypeDef = TypedDict(
    "SerializerTypeDef",
    {
        "ParquetSerDe": ParquetSerDeTypeDef,
        "OrcSerDe": OrcSerDeTypeDef,
    },
    total=False,
)

_RequiredProcessorOutputTypeDef = TypedDict(
    "_RequiredProcessorOutputTypeDef",
    {
        "Type": ProcessorTypeType,
    },
)
_OptionalProcessorOutputTypeDef = TypedDict(
    "_OptionalProcessorOutputTypeDef",
    {
        "Parameters": List[ProcessorParameterOutputTypeDef],
    },
    total=False,
)


class ProcessorOutputTypeDef(_RequiredProcessorOutputTypeDef, _OptionalProcessorOutputTypeDef):
    pass


_RequiredProcessorTypeDef = TypedDict(
    "_RequiredProcessorTypeDef",
    {
        "Type": ProcessorTypeType,
    },
)
_OptionalProcessorTypeDef = TypedDict(
    "_OptionalProcessorTypeDef",
    {
        "Parameters": Sequence[ProcessorParameterTypeDef],
    },
    total=False,
)


class ProcessorTypeDef(_RequiredProcessorTypeDef, _OptionalProcessorTypeDef):
    pass


PutRecordBatchInputRequestTypeDef = TypedDict(
    "PutRecordBatchInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Records": Sequence[RecordTypeDef],
    },
)

PutRecordInputRequestTypeDef = TypedDict(
    "PutRecordInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Record": RecordTypeDef,
    },
)

PutRecordBatchOutputTypeDef = TypedDict(
    "PutRecordBatchOutputTypeDef",
    {
        "FailedPutCount": int,
        "Encrypted": bool,
        "RequestResponses": List[PutRecordBatchResponseEntryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputFormatConfigurationOutputTypeDef = TypedDict(
    "InputFormatConfigurationOutputTypeDef",
    {
        "Deserializer": DeserializerOutputTypeDef,
    },
    total=False,
)

InputFormatConfigurationTypeDef = TypedDict(
    "InputFormatConfigurationTypeDef",
    {
        "Deserializer": DeserializerTypeDef,
    },
    total=False,
)

_RequiredS3DestinationDescriptionTypeDef = TypedDict(
    "_RequiredS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "BufferingHints": BufferingHintsOutputTypeDef,
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
    },
)
_OptionalS3DestinationDescriptionTypeDef = TypedDict(
    "_OptionalS3DestinationDescriptionTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsOutputTypeDef,
    },
    total=False,
)


class S3DestinationDescriptionTypeDef(
    _RequiredS3DestinationDescriptionTypeDef, _OptionalS3DestinationDescriptionTypeDef
):
    pass


_RequiredS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
    },
)
_OptionalS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": BufferingHintsTypeDef,
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class S3DestinationConfigurationTypeDef(
    _RequiredS3DestinationConfigurationTypeDef, _OptionalS3DestinationConfigurationTypeDef
):
    pass


S3DestinationUpdateTypeDef = TypedDict(
    "S3DestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": BufferingHintsTypeDef,
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

OutputFormatConfigurationOutputTypeDef = TypedDict(
    "OutputFormatConfigurationOutputTypeDef",
    {
        "Serializer": SerializerOutputTypeDef,
    },
    total=False,
)

OutputFormatConfigurationTypeDef = TypedDict(
    "OutputFormatConfigurationTypeDef",
    {
        "Serializer": SerializerTypeDef,
    },
    total=False,
)

ProcessingConfigurationOutputTypeDef = TypedDict(
    "ProcessingConfigurationOutputTypeDef",
    {
        "Enabled": bool,
        "Processors": List[ProcessorOutputTypeDef],
    },
    total=False,
)

ProcessingConfigurationTypeDef = TypedDict(
    "ProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": Sequence[ProcessorTypeDef],
    },
    total=False,
)

DataFormatConversionConfigurationOutputTypeDef = TypedDict(
    "DataFormatConversionConfigurationOutputTypeDef",
    {
        "SchemaConfiguration": SchemaConfigurationOutputTypeDef,
        "InputFormatConfiguration": InputFormatConfigurationOutputTypeDef,
        "OutputFormatConfiguration": OutputFormatConfigurationOutputTypeDef,
        "Enabled": bool,
    },
    total=False,
)

DataFormatConversionConfigurationTypeDef = TypedDict(
    "DataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": SchemaConfigurationTypeDef,
        "InputFormatConfiguration": InputFormatConfigurationTypeDef,
        "OutputFormatConfiguration": OutputFormatConfigurationTypeDef,
        "Enabled": bool,
    },
    total=False,
)

AmazonOpenSearchServerlessDestinationDescriptionTypeDef = TypedDict(
    "AmazonOpenSearchServerlessDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "CollectionEndpoint": str,
        "IndexName": str,
        "BufferingHints": AmazonOpenSearchServerlessBufferingHintsOutputTypeDef,
        "RetryOptions": AmazonOpenSearchServerlessRetryOptionsOutputTypeDef,
        "S3BackupMode": AmazonOpenSearchServerlessS3BackupModeType,
        "S3DestinationDescription": S3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationOutputTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsOutputTypeDef,
        "VpcConfigurationDescription": VpcConfigurationDescriptionTypeDef,
    },
    total=False,
)

AmazonopensearchserviceDestinationDescriptionTypeDef = TypedDict(
    "AmazonopensearchserviceDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": AmazonopensearchserviceIndexRotationPeriodType,
        "BufferingHints": AmazonopensearchserviceBufferingHintsOutputTypeDef,
        "RetryOptions": AmazonopensearchserviceRetryOptionsOutputTypeDef,
        "S3BackupMode": AmazonopensearchserviceS3BackupModeType,
        "S3DestinationDescription": S3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationOutputTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsOutputTypeDef,
        "VpcConfigurationDescription": VpcConfigurationDescriptionTypeDef,
    },
    total=False,
)

ElasticsearchDestinationDescriptionTypeDef = TypedDict(
    "ElasticsearchDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": ElasticsearchIndexRotationPeriodType,
        "BufferingHints": ElasticsearchBufferingHintsOutputTypeDef,
        "RetryOptions": ElasticsearchRetryOptionsOutputTypeDef,
        "S3BackupMode": ElasticsearchS3BackupModeType,
        "S3DestinationDescription": S3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationOutputTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsOutputTypeDef,
        "VpcConfigurationDescription": VpcConfigurationDescriptionTypeDef,
    },
    total=False,
)

HttpEndpointDestinationDescriptionTypeDef = TypedDict(
    "HttpEndpointDestinationDescriptionTypeDef",
    {
        "EndpointConfiguration": HttpEndpointDescriptionTypeDef,
        "BufferingHints": HttpEndpointBufferingHintsOutputTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsOutputTypeDef,
        "RequestConfiguration": HttpEndpointRequestConfigurationOutputTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationOutputTypeDef,
        "RoleARN": str,
        "RetryOptions": HttpEndpointRetryOptionsOutputTypeDef,
        "S3BackupMode": HttpEndpointS3BackupModeType,
        "S3DestinationDescription": S3DestinationDescriptionTypeDef,
    },
    total=False,
)

_RequiredRedshiftDestinationDescriptionTypeDef = TypedDict(
    "_RequiredRedshiftDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": CopyCommandOutputTypeDef,
        "Username": str,
        "S3DestinationDescription": S3DestinationDescriptionTypeDef,
    },
)
_OptionalRedshiftDestinationDescriptionTypeDef = TypedDict(
    "_OptionalRedshiftDestinationDescriptionTypeDef",
    {
        "RetryOptions": RedshiftRetryOptionsOutputTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationOutputTypeDef,
        "S3BackupMode": RedshiftS3BackupModeType,
        "S3BackupDescription": S3DestinationDescriptionTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsOutputTypeDef,
    },
    total=False,
)


class RedshiftDestinationDescriptionTypeDef(
    _RequiredRedshiftDestinationDescriptionTypeDef, _OptionalRedshiftDestinationDescriptionTypeDef
):
    pass


SplunkDestinationDescriptionTypeDef = TypedDict(
    "SplunkDestinationDescriptionTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": HECEndpointTypeType,
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": SplunkRetryOptionsOutputTypeDef,
        "S3BackupMode": SplunkS3BackupModeType,
        "S3DestinationDescription": S3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationOutputTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsOutputTypeDef,
    },
    total=False,
)

_RequiredAmazonOpenSearchServerlessDestinationConfigurationTypeDef = TypedDict(
    "_RequiredAmazonOpenSearchServerlessDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": S3DestinationConfigurationTypeDef,
    },
)
_OptionalAmazonOpenSearchServerlessDestinationConfigurationTypeDef = TypedDict(
    "_OptionalAmazonOpenSearchServerlessDestinationConfigurationTypeDef",
    {
        "CollectionEndpoint": str,
        "BufferingHints": AmazonOpenSearchServerlessBufferingHintsTypeDef,
        "RetryOptions": AmazonOpenSearchServerlessRetryOptionsTypeDef,
        "S3BackupMode": AmazonOpenSearchServerlessS3BackupModeType,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
        "VpcConfiguration": VpcConfigurationTypeDef,
    },
    total=False,
)


class AmazonOpenSearchServerlessDestinationConfigurationTypeDef(
    _RequiredAmazonOpenSearchServerlessDestinationConfigurationTypeDef,
    _OptionalAmazonOpenSearchServerlessDestinationConfigurationTypeDef,
):
    pass


AmazonOpenSearchServerlessDestinationUpdateTypeDef = TypedDict(
    "AmazonOpenSearchServerlessDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "CollectionEndpoint": str,
        "IndexName": str,
        "BufferingHints": AmazonOpenSearchServerlessBufferingHintsTypeDef,
        "RetryOptions": AmazonOpenSearchServerlessRetryOptionsTypeDef,
        "S3Update": S3DestinationUpdateTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredAmazonopensearchserviceDestinationConfigurationTypeDef = TypedDict(
    "_RequiredAmazonopensearchserviceDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": S3DestinationConfigurationTypeDef,
    },
)
_OptionalAmazonopensearchserviceDestinationConfigurationTypeDef = TypedDict(
    "_OptionalAmazonopensearchserviceDestinationConfigurationTypeDef",
    {
        "DomainARN": str,
        "ClusterEndpoint": str,
        "TypeName": str,
        "IndexRotationPeriod": AmazonopensearchserviceIndexRotationPeriodType,
        "BufferingHints": AmazonopensearchserviceBufferingHintsTypeDef,
        "RetryOptions": AmazonopensearchserviceRetryOptionsTypeDef,
        "S3BackupMode": AmazonopensearchserviceS3BackupModeType,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
        "VpcConfiguration": VpcConfigurationTypeDef,
    },
    total=False,
)


class AmazonopensearchserviceDestinationConfigurationTypeDef(
    _RequiredAmazonopensearchserviceDestinationConfigurationTypeDef,
    _OptionalAmazonopensearchserviceDestinationConfigurationTypeDef,
):
    pass


AmazonopensearchserviceDestinationUpdateTypeDef = TypedDict(
    "AmazonopensearchserviceDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": AmazonopensearchserviceIndexRotationPeriodType,
        "BufferingHints": AmazonopensearchserviceBufferingHintsTypeDef,
        "RetryOptions": AmazonopensearchserviceRetryOptionsTypeDef,
        "S3Update": S3DestinationUpdateTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_RequiredElasticsearchDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": S3DestinationConfigurationTypeDef,
    },
)
_OptionalElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_OptionalElasticsearchDestinationConfigurationTypeDef",
    {
        "DomainARN": str,
        "ClusterEndpoint": str,
        "TypeName": str,
        "IndexRotationPeriod": ElasticsearchIndexRotationPeriodType,
        "BufferingHints": ElasticsearchBufferingHintsTypeDef,
        "RetryOptions": ElasticsearchRetryOptionsTypeDef,
        "S3BackupMode": ElasticsearchS3BackupModeType,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
        "VpcConfiguration": VpcConfigurationTypeDef,
    },
    total=False,
)


class ElasticsearchDestinationConfigurationTypeDef(
    _RequiredElasticsearchDestinationConfigurationTypeDef,
    _OptionalElasticsearchDestinationConfigurationTypeDef,
):
    pass


ElasticsearchDestinationUpdateTypeDef = TypedDict(
    "ElasticsearchDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": ElasticsearchIndexRotationPeriodType,
        "BufferingHints": ElasticsearchBufferingHintsTypeDef,
        "RetryOptions": ElasticsearchRetryOptionsTypeDef,
        "S3Update": S3DestinationUpdateTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredHttpEndpointDestinationConfigurationTypeDef = TypedDict(
    "_RequiredHttpEndpointDestinationConfigurationTypeDef",
    {
        "EndpointConfiguration": HttpEndpointConfigurationTypeDef,
        "S3Configuration": S3DestinationConfigurationTypeDef,
    },
)
_OptionalHttpEndpointDestinationConfigurationTypeDef = TypedDict(
    "_OptionalHttpEndpointDestinationConfigurationTypeDef",
    {
        "BufferingHints": HttpEndpointBufferingHintsTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
        "RequestConfiguration": HttpEndpointRequestConfigurationTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "RoleARN": str,
        "RetryOptions": HttpEndpointRetryOptionsTypeDef,
        "S3BackupMode": HttpEndpointS3BackupModeType,
    },
    total=False,
)


class HttpEndpointDestinationConfigurationTypeDef(
    _RequiredHttpEndpointDestinationConfigurationTypeDef,
    _OptionalHttpEndpointDestinationConfigurationTypeDef,
):
    pass


HttpEndpointDestinationUpdateTypeDef = TypedDict(
    "HttpEndpointDestinationUpdateTypeDef",
    {
        "EndpointConfiguration": HttpEndpointConfigurationTypeDef,
        "BufferingHints": HttpEndpointBufferingHintsTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
        "RequestConfiguration": HttpEndpointRequestConfigurationTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "RoleARN": str,
        "RetryOptions": HttpEndpointRetryOptionsTypeDef,
        "S3BackupMode": HttpEndpointS3BackupModeType,
        "S3Update": S3DestinationUpdateTypeDef,
    },
    total=False,
)

_RequiredRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_RequiredRedshiftDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": CopyCommandTypeDef,
        "Username": str,
        "Password": str,
        "S3Configuration": S3DestinationConfigurationTypeDef,
    },
)
_OptionalRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_OptionalRedshiftDestinationConfigurationTypeDef",
    {
        "RetryOptions": RedshiftRetryOptionsTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "S3BackupMode": RedshiftS3BackupModeType,
        "S3BackupConfiguration": S3DestinationConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class RedshiftDestinationConfigurationTypeDef(
    _RequiredRedshiftDestinationConfigurationTypeDef,
    _OptionalRedshiftDestinationConfigurationTypeDef,
):
    pass


RedshiftDestinationUpdateTypeDef = TypedDict(
    "RedshiftDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": CopyCommandTypeDef,
        "Username": str,
        "Password": str,
        "RetryOptions": RedshiftRetryOptionsTypeDef,
        "S3Update": S3DestinationUpdateTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "S3BackupMode": RedshiftS3BackupModeType,
        "S3BackupUpdate": S3DestinationUpdateTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredSplunkDestinationConfigurationTypeDef = TypedDict(
    "_RequiredSplunkDestinationConfigurationTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": HECEndpointTypeType,
        "HECToken": str,
        "S3Configuration": S3DestinationConfigurationTypeDef,
    },
)
_OptionalSplunkDestinationConfigurationTypeDef = TypedDict(
    "_OptionalSplunkDestinationConfigurationTypeDef",
    {
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": SplunkRetryOptionsTypeDef,
        "S3BackupMode": SplunkS3BackupModeType,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class SplunkDestinationConfigurationTypeDef(
    _RequiredSplunkDestinationConfigurationTypeDef, _OptionalSplunkDestinationConfigurationTypeDef
):
    pass


SplunkDestinationUpdateTypeDef = TypedDict(
    "SplunkDestinationUpdateTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": HECEndpointTypeType,
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": SplunkRetryOptionsTypeDef,
        "S3BackupMode": SplunkS3BackupModeType,
        "S3Update": S3DestinationUpdateTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredExtendedS3DestinationDescriptionTypeDef = TypedDict(
    "_RequiredExtendedS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "BufferingHints": BufferingHintsOutputTypeDef,
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
    },
)
_OptionalExtendedS3DestinationDescriptionTypeDef = TypedDict(
    "_OptionalExtendedS3DestinationDescriptionTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsOutputTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationOutputTypeDef,
        "S3BackupMode": S3BackupModeType,
        "S3BackupDescription": S3DestinationDescriptionTypeDef,
        "DataFormatConversionConfiguration": DataFormatConversionConfigurationOutputTypeDef,
        "DynamicPartitioningConfiguration": DynamicPartitioningConfigurationOutputTypeDef,
    },
    total=False,
)


class ExtendedS3DestinationDescriptionTypeDef(
    _RequiredExtendedS3DestinationDescriptionTypeDef,
    _OptionalExtendedS3DestinationDescriptionTypeDef,
):
    pass


_RequiredExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredExtendedS3DestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
    },
)
_OptionalExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalExtendedS3DestinationConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": BufferingHintsTypeDef,
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "S3BackupMode": S3BackupModeType,
        "S3BackupConfiguration": S3DestinationConfigurationTypeDef,
        "DataFormatConversionConfiguration": DataFormatConversionConfigurationTypeDef,
        "DynamicPartitioningConfiguration": DynamicPartitioningConfigurationTypeDef,
    },
    total=False,
)


class ExtendedS3DestinationConfigurationTypeDef(
    _RequiredExtendedS3DestinationConfigurationTypeDef,
    _OptionalExtendedS3DestinationConfigurationTypeDef,
):
    pass


ExtendedS3DestinationUpdateTypeDef = TypedDict(
    "ExtendedS3DestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": BufferingHintsTypeDef,
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": CloudWatchLoggingOptionsTypeDef,
        "ProcessingConfiguration": ProcessingConfigurationTypeDef,
        "S3BackupMode": S3BackupModeType,
        "S3BackupUpdate": S3DestinationUpdateTypeDef,
        "DataFormatConversionConfiguration": DataFormatConversionConfigurationTypeDef,
        "DynamicPartitioningConfiguration": DynamicPartitioningConfigurationTypeDef,
    },
    total=False,
)

_RequiredDestinationDescriptionTypeDef = TypedDict(
    "_RequiredDestinationDescriptionTypeDef",
    {
        "DestinationId": str,
    },
)
_OptionalDestinationDescriptionTypeDef = TypedDict(
    "_OptionalDestinationDescriptionTypeDef",
    {
        "S3DestinationDescription": S3DestinationDescriptionTypeDef,
        "ExtendedS3DestinationDescription": ExtendedS3DestinationDescriptionTypeDef,
        "RedshiftDestinationDescription": RedshiftDestinationDescriptionTypeDef,
        "ElasticsearchDestinationDescription": ElasticsearchDestinationDescriptionTypeDef,
        "AmazonopensearchserviceDestinationDescription": (
            AmazonopensearchserviceDestinationDescriptionTypeDef
        ),
        "SplunkDestinationDescription": SplunkDestinationDescriptionTypeDef,
        "HttpEndpointDestinationDescription": HttpEndpointDestinationDescriptionTypeDef,
        "AmazonOpenSearchServerlessDestinationDescription": (
            AmazonOpenSearchServerlessDestinationDescriptionTypeDef
        ),
    },
    total=False,
)


class DestinationDescriptionTypeDef(
    _RequiredDestinationDescriptionTypeDef, _OptionalDestinationDescriptionTypeDef
):
    pass


_RequiredCreateDeliveryStreamInputRequestTypeDef = TypedDict(
    "_RequiredCreateDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalCreateDeliveryStreamInputRequestTypeDef = TypedDict(
    "_OptionalCreateDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamType": DeliveryStreamTypeType,
        "KinesisStreamSourceConfiguration": KinesisStreamSourceConfigurationTypeDef,
        "DeliveryStreamEncryptionConfigurationInput": (
            DeliveryStreamEncryptionConfigurationInputTypeDef
        ),
        "S3DestinationConfiguration": S3DestinationConfigurationTypeDef,
        "ExtendedS3DestinationConfiguration": ExtendedS3DestinationConfigurationTypeDef,
        "RedshiftDestinationConfiguration": RedshiftDestinationConfigurationTypeDef,
        "ElasticsearchDestinationConfiguration": ElasticsearchDestinationConfigurationTypeDef,
        "AmazonopensearchserviceDestinationConfiguration": (
            AmazonopensearchserviceDestinationConfigurationTypeDef
        ),
        "SplunkDestinationConfiguration": SplunkDestinationConfigurationTypeDef,
        "HttpEndpointDestinationConfiguration": HttpEndpointDestinationConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "AmazonOpenSearchServerlessDestinationConfiguration": (
            AmazonOpenSearchServerlessDestinationConfigurationTypeDef
        ),
    },
    total=False,
)


class CreateDeliveryStreamInputRequestTypeDef(
    _RequiredCreateDeliveryStreamInputRequestTypeDef,
    _OptionalCreateDeliveryStreamInputRequestTypeDef,
):
    pass


_RequiredUpdateDestinationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDestinationInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "CurrentDeliveryStreamVersionId": str,
        "DestinationId": str,
    },
)
_OptionalUpdateDestinationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDestinationInputRequestTypeDef",
    {
        "S3DestinationUpdate": S3DestinationUpdateTypeDef,
        "ExtendedS3DestinationUpdate": ExtendedS3DestinationUpdateTypeDef,
        "RedshiftDestinationUpdate": RedshiftDestinationUpdateTypeDef,
        "ElasticsearchDestinationUpdate": ElasticsearchDestinationUpdateTypeDef,
        "AmazonopensearchserviceDestinationUpdate": AmazonopensearchserviceDestinationUpdateTypeDef,
        "SplunkDestinationUpdate": SplunkDestinationUpdateTypeDef,
        "HttpEndpointDestinationUpdate": HttpEndpointDestinationUpdateTypeDef,
        "AmazonOpenSearchServerlessDestinationUpdate": (
            AmazonOpenSearchServerlessDestinationUpdateTypeDef
        ),
    },
    total=False,
)


class UpdateDestinationInputRequestTypeDef(
    _RequiredUpdateDestinationInputRequestTypeDef, _OptionalUpdateDestinationInputRequestTypeDef
):
    pass


_RequiredDeliveryStreamDescriptionTypeDef = TypedDict(
    "_RequiredDeliveryStreamDescriptionTypeDef",
    {
        "DeliveryStreamName": str,
        "DeliveryStreamARN": str,
        "DeliveryStreamStatus": DeliveryStreamStatusType,
        "DeliveryStreamType": DeliveryStreamTypeType,
        "VersionId": str,
        "Destinations": List[DestinationDescriptionTypeDef],
        "HasMoreDestinations": bool,
    },
)
_OptionalDeliveryStreamDescriptionTypeDef = TypedDict(
    "_OptionalDeliveryStreamDescriptionTypeDef",
    {
        "FailureDescription": FailureDescriptionTypeDef,
        "DeliveryStreamEncryptionConfiguration": DeliveryStreamEncryptionConfigurationTypeDef,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Source": SourceDescriptionTypeDef,
    },
    total=False,
)


class DeliveryStreamDescriptionTypeDef(
    _RequiredDeliveryStreamDescriptionTypeDef, _OptionalDeliveryStreamDescriptionTypeDef
):
    pass


DescribeDeliveryStreamOutputTypeDef = TypedDict(
    "DescribeDeliveryStreamOutputTypeDef",
    {
        "DeliveryStreamDescription": DeliveryStreamDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
