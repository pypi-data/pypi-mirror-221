"""
Type annotations for kinesisanalytics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/type_defs/)

Usage::

    ```python
    from mypy_boto3_kinesisanalytics.type_defs import CloudWatchLoggingOptionTypeDef

    data: CloudWatchLoggingOptionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import ApplicationStatusType, InputStartingPositionType, RecordFormatTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "ApplicationSummaryTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CSVMappingParametersOutputTypeDef",
    "CSVMappingParametersTypeDef",
    "TagTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DeleteApplicationOutputRequestRequestTypeDef",
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DestinationSchemaOutputTypeDef",
    "DestinationSchemaTypeDef",
    "InputStartingPositionConfigurationTypeDef",
    "S3ConfigurationTypeDef",
    "InputParallelismOutputTypeDef",
    "InputStartingPositionConfigurationOutputTypeDef",
    "KinesisFirehoseInputDescriptionTypeDef",
    "KinesisStreamsInputDescriptionTypeDef",
    "InputLambdaProcessorDescriptionTypeDef",
    "InputLambdaProcessorTypeDef",
    "InputLambdaProcessorUpdateTypeDef",
    "InputParallelismTypeDef",
    "InputParallelismUpdateTypeDef",
    "RecordColumnTypeDef",
    "KinesisFirehoseInputTypeDef",
    "KinesisStreamsInputTypeDef",
    "KinesisFirehoseInputUpdateTypeDef",
    "KinesisStreamsInputUpdateTypeDef",
    "JSONMappingParametersOutputTypeDef",
    "JSONMappingParametersTypeDef",
    "KinesisFirehoseOutputDescriptionTypeDef",
    "KinesisFirehoseOutputTypeDef",
    "KinesisFirehoseOutputUpdateTypeDef",
    "KinesisStreamsOutputDescriptionTypeDef",
    "KinesisStreamsOutputTypeDef",
    "KinesisStreamsOutputUpdateTypeDef",
    "LambdaOutputDescriptionTypeDef",
    "LambdaOutputTypeDef",
    "LambdaOutputUpdateTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "RecordColumnOutputTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "InputConfigurationTypeDef",
    "InputProcessingConfigurationDescriptionTypeDef",
    "InputProcessingConfigurationTypeDef",
    "InputProcessingConfigurationUpdateTypeDef",
    "MappingParametersOutputTypeDef",
    "MappingParametersTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DiscoverInputSchemaRequestRequestTypeDef",
    "RecordFormatOutputTypeDef",
    "RecordFormatTypeDef",
    "AddApplicationOutputRequestRequestTypeDef",
    "SourceSchemaOutputTypeDef",
    "InputSchemaUpdateTypeDef",
    "SourceSchemaTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "InputDescriptionTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "InputUpdateTypeDef",
    "InputTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ApplicationDetailTypeDef",
    "AddApplicationInputRequestRequestTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    "ApplicationUpdateTypeDef",
    "DescribeApplicationResponseTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
)

CloudWatchLoggingOptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionTypeDef",
    {
        "LogStreamARN": str,
        "RoleARN": str,
    },
)

_RequiredCloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingOptionDescriptionTypeDef",
    {
        "LogStreamARN": str,
        "RoleARN": str,
    },
)
_OptionalCloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingOptionDescriptionTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
    },
    total=False,
)


class CloudWatchLoggingOptionDescriptionTypeDef(
    _RequiredCloudWatchLoggingOptionDescriptionTypeDef,
    _OptionalCloudWatchLoggingOptionDescriptionTypeDef,
):
    pass


ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
    },
)

_RequiredCloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingOptionUpdateTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
    },
)
_OptionalCloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingOptionUpdateTypeDef",
    {
        "LogStreamARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)


class CloudWatchLoggingOptionUpdateTypeDef(
    _RequiredCloudWatchLoggingOptionUpdateTypeDef, _OptionalCloudWatchLoggingOptionUpdateTypeDef
):
    pass


CSVMappingParametersOutputTypeDef = TypedDict(
    "CSVMappingParametersOutputTypeDef",
    {
        "RecordRowDelimiter": str,
        "RecordColumnDelimiter": str,
    },
)

CSVMappingParametersTypeDef = TypedDict(
    "CSVMappingParametersTypeDef",
    {
        "RecordRowDelimiter": str,
        "RecordColumnDelimiter": str,
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


DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "CloudWatchLoggingOptionId": str,
    },
)

DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
    },
)

DeleteApplicationOutputRequestRequestTypeDef = TypedDict(
    "DeleteApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "OutputId": str,
    },
)

DeleteApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceId": str,
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CreateTimestamp": Union[datetime, str],
    },
)

DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)

DestinationSchemaOutputTypeDef = TypedDict(
    "DestinationSchemaOutputTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)

DestinationSchemaTypeDef = TypedDict(
    "DestinationSchemaTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)

InputStartingPositionConfigurationTypeDef = TypedDict(
    "InputStartingPositionConfigurationTypeDef",
    {
        "InputStartingPosition": InputStartingPositionType,
    },
    total=False,
)

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "FileKey": str,
    },
)

InputParallelismOutputTypeDef = TypedDict(
    "InputParallelismOutputTypeDef",
    {
        "Count": int,
    },
    total=False,
)

InputStartingPositionConfigurationOutputTypeDef = TypedDict(
    "InputStartingPositionConfigurationOutputTypeDef",
    {
        "InputStartingPosition": InputStartingPositionType,
    },
    total=False,
)

KinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseInputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

KinesisStreamsInputDescriptionTypeDef = TypedDict(
    "KinesisStreamsInputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

InputLambdaProcessorDescriptionTypeDef = TypedDict(
    "InputLambdaProcessorDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

InputLambdaProcessorTypeDef = TypedDict(
    "InputLambdaProcessorTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

InputLambdaProcessorUpdateTypeDef = TypedDict(
    "InputLambdaProcessorUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

InputParallelismTypeDef = TypedDict(
    "InputParallelismTypeDef",
    {
        "Count": int,
    },
    total=False,
)

InputParallelismUpdateTypeDef = TypedDict(
    "InputParallelismUpdateTypeDef",
    {
        "CountUpdate": int,
    },
    total=False,
)

_RequiredRecordColumnTypeDef = TypedDict(
    "_RequiredRecordColumnTypeDef",
    {
        "Name": str,
        "SqlType": str,
    },
)
_OptionalRecordColumnTypeDef = TypedDict(
    "_OptionalRecordColumnTypeDef",
    {
        "Mapping": str,
    },
    total=False,
)


class RecordColumnTypeDef(_RequiredRecordColumnTypeDef, _OptionalRecordColumnTypeDef):
    pass


KinesisFirehoseInputTypeDef = TypedDict(
    "KinesisFirehoseInputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisStreamsInputTypeDef = TypedDict(
    "KinesisStreamsInputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisFirehoseInputUpdateTypeDef = TypedDict(
    "KinesisFirehoseInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

KinesisStreamsInputUpdateTypeDef = TypedDict(
    "KinesisStreamsInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

JSONMappingParametersOutputTypeDef = TypedDict(
    "JSONMappingParametersOutputTypeDef",
    {
        "RecordRowPath": str,
    },
)

JSONMappingParametersTypeDef = TypedDict(
    "JSONMappingParametersTypeDef",
    {
        "RecordRowPath": str,
    },
)

KinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

KinesisFirehoseOutputTypeDef = TypedDict(
    "KinesisFirehoseOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "KinesisFirehoseOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

KinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "KinesisStreamsOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

KinesisStreamsOutputTypeDef = TypedDict(
    "KinesisStreamsOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisStreamsOutputUpdateTypeDef = TypedDict(
    "KinesisStreamsOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

LambdaOutputDescriptionTypeDef = TypedDict(
    "LambdaOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
    total=False,
)

LambdaOutputTypeDef = TypedDict(
    "LambdaOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

LambdaOutputUpdateTypeDef = TypedDict(
    "LambdaOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
        "RoleARNUpdate": str,
    },
    total=False,
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "Limit": int,
        "ExclusiveStartApplicationName": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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


_RequiredRecordColumnOutputTypeDef = TypedDict(
    "_RequiredRecordColumnOutputTypeDef",
    {
        "Name": str,
        "SqlType": str,
    },
)
_OptionalRecordColumnOutputTypeDef = TypedDict(
    "_OptionalRecordColumnOutputTypeDef",
    {
        "Mapping": str,
    },
    total=False,
)


class RecordColumnOutputTypeDef(
    _RequiredRecordColumnOutputTypeDef, _OptionalRecordColumnOutputTypeDef
):
    pass


S3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "S3ReferenceDataSourceDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": str,
    },
)

S3ReferenceDataSourceTypeDef = TypedDict(
    "S3ReferenceDataSourceTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": str,
    },
)

S3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "S3ReferenceDataSourceUpdateTypeDef",
    {
        "BucketARNUpdate": str,
        "FileKeyUpdate": str,
        "ReferenceRoleARNUpdate": str,
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

StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "CloudWatchLoggingOption": CloudWatchLoggingOptionTypeDef,
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationSummary": ApplicationSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List[ApplicationSummaryTypeDef],
        "HasMoreApplications": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "Id": str,
        "InputStartingPositionConfiguration": InputStartingPositionConfigurationTypeDef,
    },
)

InputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "InputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": InputLambdaProcessorDescriptionTypeDef,
    },
    total=False,
)

InputProcessingConfigurationTypeDef = TypedDict(
    "InputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": InputLambdaProcessorTypeDef,
    },
)

InputProcessingConfigurationUpdateTypeDef = TypedDict(
    "InputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": InputLambdaProcessorUpdateTypeDef,
    },
)

MappingParametersOutputTypeDef = TypedDict(
    "MappingParametersOutputTypeDef",
    {
        "JSONMappingParameters": JSONMappingParametersOutputTypeDef,
        "CSVMappingParameters": CSVMappingParametersOutputTypeDef,
    },
    total=False,
)

MappingParametersTypeDef = TypedDict(
    "MappingParametersTypeDef",
    {
        "JSONMappingParameters": JSONMappingParametersTypeDef,
        "CSVMappingParameters": CSVMappingParametersTypeDef,
    },
    total=False,
)

OutputDescriptionTypeDef = TypedDict(
    "OutputDescriptionTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": KinesisStreamsOutputDescriptionTypeDef,
        "KinesisFirehoseOutputDescription": KinesisFirehoseOutputDescriptionTypeDef,
        "LambdaOutputDescription": LambdaOutputDescriptionTypeDef,
        "DestinationSchema": DestinationSchemaOutputTypeDef,
    },
    total=False,
)

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "Name": str,
        "DestinationSchema": DestinationSchemaTypeDef,
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "KinesisStreamsOutput": KinesisStreamsOutputTypeDef,
        "KinesisFirehoseOutput": KinesisFirehoseOutputTypeDef,
        "LambdaOutput": LambdaOutputTypeDef,
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass


_RequiredOutputUpdateTypeDef = TypedDict(
    "_RequiredOutputUpdateTypeDef",
    {
        "OutputId": str,
    },
)
_OptionalOutputUpdateTypeDef = TypedDict(
    "_OptionalOutputUpdateTypeDef",
    {
        "NameUpdate": str,
        "KinesisStreamsOutputUpdate": KinesisStreamsOutputUpdateTypeDef,
        "KinesisFirehoseOutputUpdate": KinesisFirehoseOutputUpdateTypeDef,
        "LambdaOutputUpdate": LambdaOutputUpdateTypeDef,
        "DestinationSchemaUpdate": DestinationSchemaTypeDef,
    },
    total=False,
)


class OutputUpdateTypeDef(_RequiredOutputUpdateTypeDef, _OptionalOutputUpdateTypeDef):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "InputConfigurations": Sequence[InputConfigurationTypeDef],
    },
)

AddApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfiguration": InputProcessingConfigurationTypeDef,
    },
)

DiscoverInputSchemaRequestRequestTypeDef = TypedDict(
    "DiscoverInputSchemaRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
        "InputStartingPositionConfiguration": InputStartingPositionConfigurationTypeDef,
        "S3Configuration": S3ConfigurationTypeDef,
        "InputProcessingConfiguration": InputProcessingConfigurationTypeDef,
    },
    total=False,
)

_RequiredRecordFormatOutputTypeDef = TypedDict(
    "_RequiredRecordFormatOutputTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)
_OptionalRecordFormatOutputTypeDef = TypedDict(
    "_OptionalRecordFormatOutputTypeDef",
    {
        "MappingParameters": MappingParametersOutputTypeDef,
    },
    total=False,
)


class RecordFormatOutputTypeDef(
    _RequiredRecordFormatOutputTypeDef, _OptionalRecordFormatOutputTypeDef
):
    pass


_RequiredRecordFormatTypeDef = TypedDict(
    "_RequiredRecordFormatTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)
_OptionalRecordFormatTypeDef = TypedDict(
    "_OptionalRecordFormatTypeDef",
    {
        "MappingParameters": MappingParametersTypeDef,
    },
    total=False,
)


class RecordFormatTypeDef(_RequiredRecordFormatTypeDef, _OptionalRecordFormatTypeDef):
    pass


AddApplicationOutputRequestRequestTypeDef = TypedDict(
    "AddApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Output": OutputTypeDef,
    },
)

_RequiredSourceSchemaOutputTypeDef = TypedDict(
    "_RequiredSourceSchemaOutputTypeDef",
    {
        "RecordFormat": RecordFormatOutputTypeDef,
        "RecordColumns": List[RecordColumnOutputTypeDef],
    },
)
_OptionalSourceSchemaOutputTypeDef = TypedDict(
    "_OptionalSourceSchemaOutputTypeDef",
    {
        "RecordEncoding": str,
    },
    total=False,
)


class SourceSchemaOutputTypeDef(
    _RequiredSourceSchemaOutputTypeDef, _OptionalSourceSchemaOutputTypeDef
):
    pass


InputSchemaUpdateTypeDef = TypedDict(
    "InputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": RecordFormatTypeDef,
        "RecordEncodingUpdate": str,
        "RecordColumnUpdates": Sequence[RecordColumnTypeDef],
    },
    total=False,
)

_RequiredSourceSchemaTypeDef = TypedDict(
    "_RequiredSourceSchemaTypeDef",
    {
        "RecordFormat": RecordFormatTypeDef,
        "RecordColumns": Sequence[RecordColumnTypeDef],
    },
)
_OptionalSourceSchemaTypeDef = TypedDict(
    "_OptionalSourceSchemaTypeDef",
    {
        "RecordEncoding": str,
    },
    total=False,
)


class SourceSchemaTypeDef(_RequiredSourceSchemaTypeDef, _OptionalSourceSchemaTypeDef):
    pass


DiscoverInputSchemaResponseTypeDef = TypedDict(
    "DiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": SourceSchemaOutputTypeDef,
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputDescriptionTypeDef = TypedDict(
    "InputDescriptionTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": InputProcessingConfigurationDescriptionTypeDef,
        "KinesisStreamsInputDescription": KinesisStreamsInputDescriptionTypeDef,
        "KinesisFirehoseInputDescription": KinesisFirehoseInputDescriptionTypeDef,
        "InputSchema": SourceSchemaOutputTypeDef,
        "InputParallelism": InputParallelismOutputTypeDef,
        "InputStartingPositionConfiguration": InputStartingPositionConfigurationOutputTypeDef,
    },
    total=False,
)

_RequiredReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_RequiredReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": S3ReferenceDataSourceDescriptionTypeDef,
    },
)
_OptionalReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_OptionalReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceSchema": SourceSchemaOutputTypeDef,
    },
    total=False,
)


class ReferenceDataSourceDescriptionTypeDef(
    _RequiredReferenceDataSourceDescriptionTypeDef, _OptionalReferenceDataSourceDescriptionTypeDef
):
    pass


_RequiredInputUpdateTypeDef = TypedDict(
    "_RequiredInputUpdateTypeDef",
    {
        "InputId": str,
    },
)
_OptionalInputUpdateTypeDef = TypedDict(
    "_OptionalInputUpdateTypeDef",
    {
        "NamePrefixUpdate": str,
        "InputProcessingConfigurationUpdate": InputProcessingConfigurationUpdateTypeDef,
        "KinesisStreamsInputUpdate": KinesisStreamsInputUpdateTypeDef,
        "KinesisFirehoseInputUpdate": KinesisFirehoseInputUpdateTypeDef,
        "InputSchemaUpdate": InputSchemaUpdateTypeDef,
        "InputParallelismUpdate": InputParallelismUpdateTypeDef,
    },
    total=False,
)


class InputUpdateTypeDef(_RequiredInputUpdateTypeDef, _OptionalInputUpdateTypeDef):
    pass


_RequiredInputTypeDef = TypedDict(
    "_RequiredInputTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": SourceSchemaTypeDef,
    },
)
_OptionalInputTypeDef = TypedDict(
    "_OptionalInputTypeDef",
    {
        "InputProcessingConfiguration": InputProcessingConfigurationTypeDef,
        "KinesisStreamsInput": KinesisStreamsInputTypeDef,
        "KinesisFirehoseInput": KinesisFirehoseInputTypeDef,
        "InputParallelism": InputParallelismTypeDef,
    },
    total=False,
)


class InputTypeDef(_RequiredInputTypeDef, _OptionalInputTypeDef):
    pass


_RequiredReferenceDataSourceTypeDef = TypedDict(
    "_RequiredReferenceDataSourceTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": SourceSchemaTypeDef,
    },
)
_OptionalReferenceDataSourceTypeDef = TypedDict(
    "_OptionalReferenceDataSourceTypeDef",
    {
        "S3ReferenceDataSource": S3ReferenceDataSourceTypeDef,
    },
    total=False,
)


class ReferenceDataSourceTypeDef(
    _RequiredReferenceDataSourceTypeDef, _OptionalReferenceDataSourceTypeDef
):
    pass


_RequiredReferenceDataSourceUpdateTypeDef = TypedDict(
    "_RequiredReferenceDataSourceUpdateTypeDef",
    {
        "ReferenceId": str,
    },
)
_OptionalReferenceDataSourceUpdateTypeDef = TypedDict(
    "_OptionalReferenceDataSourceUpdateTypeDef",
    {
        "TableNameUpdate": str,
        "S3ReferenceDataSourceUpdate": S3ReferenceDataSourceUpdateTypeDef,
        "ReferenceSchemaUpdate": SourceSchemaTypeDef,
    },
    total=False,
)


class ReferenceDataSourceUpdateTypeDef(
    _RequiredReferenceDataSourceUpdateTypeDef, _OptionalReferenceDataSourceUpdateTypeDef
):
    pass


_RequiredApplicationDetailTypeDef = TypedDict(
    "_RequiredApplicationDetailTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
    },
)
_OptionalApplicationDetailTypeDef = TypedDict(
    "_OptionalApplicationDetailTypeDef",
    {
        "ApplicationDescription": str,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "InputDescriptions": List[InputDescriptionTypeDef],
        "OutputDescriptions": List[OutputDescriptionTypeDef],
        "ReferenceDataSourceDescriptions": List[ReferenceDataSourceDescriptionTypeDef],
        "CloudWatchLoggingOptionDescriptions": List[CloudWatchLoggingOptionDescriptionTypeDef],
        "ApplicationCode": str,
    },
    total=False,
)


class ApplicationDetailTypeDef(
    _RequiredApplicationDetailTypeDef, _OptionalApplicationDetailTypeDef
):
    pass


AddApplicationInputRequestRequestTypeDef = TypedDict(
    "AddApplicationInputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Input": InputTypeDef,
    },
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "ApplicationDescription": str,
        "Inputs": Sequence[InputTypeDef],
        "Outputs": Sequence[OutputTypeDef],
        "CloudWatchLoggingOptions": Sequence[CloudWatchLoggingOptionTypeDef],
        "ApplicationCode": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass


AddApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceDataSource": ReferenceDataSourceTypeDef,
    },
)

ApplicationUpdateTypeDef = TypedDict(
    "ApplicationUpdateTypeDef",
    {
        "InputUpdates": Sequence[InputUpdateTypeDef],
        "ApplicationCodeUpdate": str,
        "OutputUpdates": Sequence[OutputUpdateTypeDef],
        "ReferenceDataSourceUpdates": Sequence[ReferenceDataSourceUpdateTypeDef],
        "CloudWatchLoggingOptionUpdates": Sequence[CloudWatchLoggingOptionUpdateTypeDef],
    },
    total=False,
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationDetail": ApplicationDetailTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ApplicationUpdate": ApplicationUpdateTypeDef,
    },
)
