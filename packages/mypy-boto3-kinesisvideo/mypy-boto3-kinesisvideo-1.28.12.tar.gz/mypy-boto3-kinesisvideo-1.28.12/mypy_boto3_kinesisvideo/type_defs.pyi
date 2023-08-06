"""
Type annotations for kinesisvideo service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/type_defs/)

Usage::

    ```python
    from mypy_boto3_kinesisvideo.type_defs import SingleMasterConfigurationOutputTypeDef

    data: SingleMasterConfigurationOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    APINameType,
    ChannelProtocolType,
    ChannelRoleType,
    ChannelTypeType,
    ConfigurationStatusType,
    FormatType,
    ImageSelectorTypeType,
    MediaStorageConfigurationStatusType,
    MediaUriTypeType,
    RecorderStatusType,
    StatusType,
    StrategyOnFullSizeType,
    SyncStatusType,
    UpdateDataRetentionOperationType,
    UploaderStatusType,
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
    "SingleMasterConfigurationOutputTypeDef",
    "ChannelNameConditionTypeDef",
    "SingleMasterConfigurationTypeDef",
    "TagTypeDef",
    "CreateSignalingChannelOutputTypeDef",
    "CreateStreamInputRequestTypeDef",
    "CreateStreamOutputTypeDef",
    "DeleteEdgeConfigurationInputRequestTypeDef",
    "DeleteSignalingChannelInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "LocalSizeConfigOutputTypeDef",
    "LocalSizeConfigTypeDef",
    "DescribeEdgeConfigurationInputRequestTypeDef",
    "DescribeImageGenerationConfigurationInputRequestTypeDef",
    "DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateTypeDef",
    "DescribeMappedResourceConfigurationInputRequestTypeDef",
    "MappedResourceConfigurationListItemTypeDef",
    "DescribeMediaStorageConfigurationInputRequestTypeDef",
    "MediaStorageConfigurationOutputTypeDef",
    "DescribeNotificationConfigurationInputRequestTypeDef",
    "DescribeSignalingChannelInputRequestTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "StreamInfoTypeDef",
    "LastRecorderStatusTypeDef",
    "LastUploaderStatusTypeDef",
    "GetDataEndpointInputRequestTypeDef",
    "GetDataEndpointOutputTypeDef",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ImageGenerationDestinationConfigOutputTypeDef",
    "ImageGenerationDestinationConfigTypeDef",
    "ListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef",
    "ListEdgeAgentConfigurationsInputRequestTypeDef",
    "StreamNameConditionTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "MediaSourceConfigOutputTypeDef",
    "MediaSourceConfigTypeDef",
    "MediaStorageConfigurationTypeDef",
    "NotificationDestinationConfigOutputTypeDef",
    "NotificationDestinationConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ScheduleConfigOutputTypeDef",
    "ScheduleConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagStreamInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UntagStreamInputRequestTypeDef",
    "UpdateDataRetentionInputRequestTypeDef",
    "UpdateStreamInputRequestTypeDef",
    "ChannelInfoTypeDef",
    "ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef",
    "ListSignalingChannelsInputRequestTypeDef",
    "UpdateSignalingChannelInputRequestTypeDef",
    "CreateSignalingChannelInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "DeletionConfigOutputTypeDef",
    "DeletionConfigTypeDef",
    "DescribeMappedResourceConfigurationOutputTypeDef",
    "DescribeMediaStorageConfigurationOutputTypeDef",
    "DescribeStreamOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "EdgeAgentStatusTypeDef",
    "GetSignalingChannelEndpointInputRequestTypeDef",
    "GetSignalingChannelEndpointOutputTypeDef",
    "ImageGenerationConfigurationOutputTypeDef",
    "ImageGenerationConfigurationTypeDef",
    "ListStreamsInputListStreamsPaginateTypeDef",
    "ListStreamsInputRequestTypeDef",
    "UpdateMediaStorageConfigurationInputRequestTypeDef",
    "NotificationConfigurationOutputTypeDef",
    "NotificationConfigurationTypeDef",
    "RecorderConfigOutputTypeDef",
    "UploaderConfigOutputTypeDef",
    "RecorderConfigTypeDef",
    "UploaderConfigTypeDef",
    "DescribeSignalingChannelOutputTypeDef",
    "ListSignalingChannelsOutputTypeDef",
    "DescribeImageGenerationConfigurationOutputTypeDef",
    "UpdateImageGenerationConfigurationInputRequestTypeDef",
    "DescribeNotificationConfigurationOutputTypeDef",
    "UpdateNotificationConfigurationInputRequestTypeDef",
    "EdgeConfigOutputTypeDef",
    "EdgeConfigTypeDef",
    "DescribeEdgeConfigurationOutputTypeDef",
    "ListEdgeAgentConfigurationsEdgeConfigTypeDef",
    "StartEdgeConfigurationUpdateOutputTypeDef",
    "StartEdgeConfigurationUpdateInputRequestTypeDef",
    "ListEdgeAgentConfigurationsOutputTypeDef",
)

SingleMasterConfigurationOutputTypeDef = TypedDict(
    "SingleMasterConfigurationOutputTypeDef",
    {
        "MessageTtlSeconds": int,
    },
    total=False,
)

ChannelNameConditionTypeDef = TypedDict(
    "ChannelNameConditionTypeDef",
    {
        "ComparisonOperator": Literal["BEGINS_WITH"],
        "ComparisonValue": str,
    },
    total=False,
)

SingleMasterConfigurationTypeDef = TypedDict(
    "SingleMasterConfigurationTypeDef",
    {
        "MessageTtlSeconds": int,
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

CreateSignalingChannelOutputTypeDef = TypedDict(
    "CreateSignalingChannelOutputTypeDef",
    {
        "ChannelARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamInputRequestTypeDef = TypedDict(
    "_RequiredCreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalCreateStreamInputRequestTypeDef = TypedDict(
    "_OptionalCreateStreamInputRequestTypeDef",
    {
        "DeviceName": str,
        "MediaType": str,
        "KmsKeyId": str,
        "DataRetentionInHours": int,
        "Tags": Mapping[str, str],
    },
    total=False,
)

class CreateStreamInputRequestTypeDef(
    _RequiredCreateStreamInputRequestTypeDef, _OptionalCreateStreamInputRequestTypeDef
):
    pass

CreateStreamOutputTypeDef = TypedDict(
    "CreateStreamOutputTypeDef",
    {
        "StreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEdgeConfigurationInputRequestTypeDef = TypedDict(
    "DeleteEdgeConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

_RequiredDeleteSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredDeleteSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalDeleteSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalDeleteSignalingChannelInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class DeleteSignalingChannelInputRequestTypeDef(
    _RequiredDeleteSignalingChannelInputRequestTypeDef,
    _OptionalDeleteSignalingChannelInputRequestTypeDef,
):
    pass

_RequiredDeleteStreamInputRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamInputRequestTypeDef",
    {
        "StreamARN": str,
    },
)
_OptionalDeleteStreamInputRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class DeleteStreamInputRequestTypeDef(
    _RequiredDeleteStreamInputRequestTypeDef, _OptionalDeleteStreamInputRequestTypeDef
):
    pass

LocalSizeConfigOutputTypeDef = TypedDict(
    "LocalSizeConfigOutputTypeDef",
    {
        "MaxLocalMediaSizeInMB": int,
        "StrategyOnFullSize": StrategyOnFullSizeType,
    },
    total=False,
)

LocalSizeConfigTypeDef = TypedDict(
    "LocalSizeConfigTypeDef",
    {
        "MaxLocalMediaSizeInMB": int,
        "StrategyOnFullSize": StrategyOnFullSizeType,
    },
    total=False,
)

DescribeEdgeConfigurationInputRequestTypeDef = TypedDict(
    "DescribeEdgeConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeImageGenerationConfigurationInputRequestTypeDef = TypedDict(
    "DescribeImageGenerationConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateTypeDef = TypedDict(
    "DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeMappedResourceConfigurationInputRequestTypeDef = TypedDict(
    "DescribeMappedResourceConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

MappedResourceConfigurationListItemTypeDef = TypedDict(
    "MappedResourceConfigurationListItemTypeDef",
    {
        "Type": str,
        "ARN": str,
    },
    total=False,
)

DescribeMediaStorageConfigurationInputRequestTypeDef = TypedDict(
    "DescribeMediaStorageConfigurationInputRequestTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
    },
    total=False,
)

_RequiredMediaStorageConfigurationOutputTypeDef = TypedDict(
    "_RequiredMediaStorageConfigurationOutputTypeDef",
    {
        "Status": MediaStorageConfigurationStatusType,
    },
)
_OptionalMediaStorageConfigurationOutputTypeDef = TypedDict(
    "_OptionalMediaStorageConfigurationOutputTypeDef",
    {
        "StreamARN": str,
    },
    total=False,
)

class MediaStorageConfigurationOutputTypeDef(
    _RequiredMediaStorageConfigurationOutputTypeDef, _OptionalMediaStorageConfigurationOutputTypeDef
):
    pass

DescribeNotificationConfigurationInputRequestTypeDef = TypedDict(
    "DescribeNotificationConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeSignalingChannelInputRequestTypeDef = TypedDict(
    "DescribeSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
    },
    total=False,
)

DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": StatusType,
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)

LastRecorderStatusTypeDef = TypedDict(
    "LastRecorderStatusTypeDef",
    {
        "JobStatusDetails": str,
        "LastCollectedTime": datetime,
        "LastUpdatedTime": datetime,
        "RecorderStatus": RecorderStatusType,
    },
    total=False,
)

LastUploaderStatusTypeDef = TypedDict(
    "LastUploaderStatusTypeDef",
    {
        "JobStatusDetails": str,
        "LastCollectedTime": datetime,
        "LastUpdatedTime": datetime,
        "UploaderStatus": UploaderStatusType,
    },
    total=False,
)

_RequiredGetDataEndpointInputRequestTypeDef = TypedDict(
    "_RequiredGetDataEndpointInputRequestTypeDef",
    {
        "APIName": APINameType,
    },
)
_OptionalGetDataEndpointInputRequestTypeDef = TypedDict(
    "_OptionalGetDataEndpointInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class GetDataEndpointInputRequestTypeDef(
    _RequiredGetDataEndpointInputRequestTypeDef, _OptionalGetDataEndpointInputRequestTypeDef
):
    pass

GetDataEndpointOutputTypeDef = TypedDict(
    "GetDataEndpointOutputTypeDef",
    {
        "DataEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SingleMasterChannelEndpointConfigurationTypeDef = TypedDict(
    "SingleMasterChannelEndpointConfigurationTypeDef",
    {
        "Protocols": Sequence[ChannelProtocolType],
        "Role": ChannelRoleType,
    },
    total=False,
)

ResourceEndpointListItemTypeDef = TypedDict(
    "ResourceEndpointListItemTypeDef",
    {
        "Protocol": ChannelProtocolType,
        "ResourceEndpoint": str,
    },
    total=False,
)

ImageGenerationDestinationConfigOutputTypeDef = TypedDict(
    "ImageGenerationDestinationConfigOutputTypeDef",
    {
        "Uri": str,
        "DestinationRegion": str,
    },
)

ImageGenerationDestinationConfigTypeDef = TypedDict(
    "ImageGenerationDestinationConfigTypeDef",
    {
        "Uri": str,
        "DestinationRegion": str,
    },
)

_RequiredListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef = TypedDict(
    "_RequiredListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef",
    {
        "HubDeviceArn": str,
    },
)
_OptionalListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef = TypedDict(
    "_OptionalListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef(
    _RequiredListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef,
    _OptionalListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef,
):
    pass

_RequiredListEdgeAgentConfigurationsInputRequestTypeDef = TypedDict(
    "_RequiredListEdgeAgentConfigurationsInputRequestTypeDef",
    {
        "HubDeviceArn": str,
    },
)
_OptionalListEdgeAgentConfigurationsInputRequestTypeDef = TypedDict(
    "_OptionalListEdgeAgentConfigurationsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListEdgeAgentConfigurationsInputRequestTypeDef(
    _RequiredListEdgeAgentConfigurationsInputRequestTypeDef,
    _OptionalListEdgeAgentConfigurationsInputRequestTypeDef,
):
    pass

StreamNameConditionTypeDef = TypedDict(
    "StreamNameConditionTypeDef",
    {
        "ComparisonOperator": Literal["BEGINS_WITH"],
        "ComparisonValue": str,
    },
    total=False,
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "NextToken": str,
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaSourceConfigOutputTypeDef = TypedDict(
    "MediaSourceConfigOutputTypeDef",
    {
        "MediaUriSecretArn": str,
        "MediaUriType": MediaUriTypeType,
    },
)

MediaSourceConfigTypeDef = TypedDict(
    "MediaSourceConfigTypeDef",
    {
        "MediaUriSecretArn": str,
        "MediaUriType": MediaUriTypeType,
    },
)

_RequiredMediaStorageConfigurationTypeDef = TypedDict(
    "_RequiredMediaStorageConfigurationTypeDef",
    {
        "Status": MediaStorageConfigurationStatusType,
    },
)
_OptionalMediaStorageConfigurationTypeDef = TypedDict(
    "_OptionalMediaStorageConfigurationTypeDef",
    {
        "StreamARN": str,
    },
    total=False,
)

class MediaStorageConfigurationTypeDef(
    _RequiredMediaStorageConfigurationTypeDef, _OptionalMediaStorageConfigurationTypeDef
):
    pass

NotificationDestinationConfigOutputTypeDef = TypedDict(
    "NotificationDestinationConfigOutputTypeDef",
    {
        "Uri": str,
    },
)

NotificationDestinationConfigTypeDef = TypedDict(
    "NotificationDestinationConfigTypeDef",
    {
        "Uri": str,
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

ScheduleConfigOutputTypeDef = TypedDict(
    "ScheduleConfigOutputTypeDef",
    {
        "ScheduleExpression": str,
        "DurationInSeconds": int,
    },
)

ScheduleConfigTypeDef = TypedDict(
    "ScheduleConfigTypeDef",
    {
        "ScheduleExpression": str,
        "DurationInSeconds": int,
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

_RequiredTagStreamInputRequestTypeDef = TypedDict(
    "_RequiredTagStreamInputRequestTypeDef",
    {
        "Tags": Mapping[str, str],
    },
)
_OptionalTagStreamInputRequestTypeDef = TypedDict(
    "_OptionalTagStreamInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

class TagStreamInputRequestTypeDef(
    _RequiredTagStreamInputRequestTypeDef, _OptionalTagStreamInputRequestTypeDef
):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeyList": Sequence[str],
    },
)

_RequiredUntagStreamInputRequestTypeDef = TypedDict(
    "_RequiredUntagStreamInputRequestTypeDef",
    {
        "TagKeyList": Sequence[str],
    },
)
_OptionalUntagStreamInputRequestTypeDef = TypedDict(
    "_OptionalUntagStreamInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

class UntagStreamInputRequestTypeDef(
    _RequiredUntagStreamInputRequestTypeDef, _OptionalUntagStreamInputRequestTypeDef
):
    pass

_RequiredUpdateDataRetentionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDataRetentionInputRequestTypeDef",
    {
        "CurrentVersion": str,
        "Operation": UpdateDataRetentionOperationType,
        "DataRetentionChangeInHours": int,
    },
)
_OptionalUpdateDataRetentionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDataRetentionInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class UpdateDataRetentionInputRequestTypeDef(
    _RequiredUpdateDataRetentionInputRequestTypeDef, _OptionalUpdateDataRetentionInputRequestTypeDef
):
    pass

_RequiredUpdateStreamInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
)
_OptionalUpdateStreamInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "DeviceName": str,
        "MediaType": str,
    },
    total=False,
)

class UpdateStreamInputRequestTypeDef(
    _RequiredUpdateStreamInputRequestTypeDef, _OptionalUpdateStreamInputRequestTypeDef
):
    pass

ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": ChannelTypeType,
        "ChannelStatus": StatusType,
        "CreationTime": datetime,
        "SingleMasterConfiguration": SingleMasterConfigurationOutputTypeDef,
        "Version": str,
    },
    total=False,
)

ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef = TypedDict(
    "ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef",
    {
        "ChannelNameCondition": ChannelNameConditionTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSignalingChannelsInputRequestTypeDef = TypedDict(
    "ListSignalingChannelsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChannelNameCondition": ChannelNameConditionTypeDef,
    },
    total=False,
)

_RequiredUpdateSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSignalingChannelInputRequestTypeDef",
    {
        "SingleMasterConfiguration": SingleMasterConfigurationTypeDef,
    },
    total=False,
)

class UpdateSignalingChannelInputRequestTypeDef(
    _RequiredUpdateSignalingChannelInputRequestTypeDef,
    _OptionalUpdateSignalingChannelInputRequestTypeDef,
):
    pass

_RequiredCreateSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredCreateSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": str,
    },
)
_OptionalCreateSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalCreateSignalingChannelInputRequestTypeDef",
    {
        "ChannelType": ChannelTypeType,
        "SingleMasterConfiguration": SingleMasterConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateSignalingChannelInputRequestTypeDef(
    _RequiredCreateSignalingChannelInputRequestTypeDef,
    _OptionalCreateSignalingChannelInputRequestTypeDef,
):
    pass

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

DeletionConfigOutputTypeDef = TypedDict(
    "DeletionConfigOutputTypeDef",
    {
        "EdgeRetentionInHours": int,
        "LocalSizeConfig": LocalSizeConfigOutputTypeDef,
        "DeleteAfterUpload": bool,
    },
    total=False,
)

DeletionConfigTypeDef = TypedDict(
    "DeletionConfigTypeDef",
    {
        "EdgeRetentionInHours": int,
        "LocalSizeConfig": LocalSizeConfigTypeDef,
        "DeleteAfterUpload": bool,
    },
    total=False,
)

DescribeMappedResourceConfigurationOutputTypeDef = TypedDict(
    "DescribeMappedResourceConfigurationOutputTypeDef",
    {
        "MappedResourceConfigurationList": List[MappedResourceConfigurationListItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMediaStorageConfigurationOutputTypeDef = TypedDict(
    "DescribeMediaStorageConfigurationOutputTypeDef",
    {
        "MediaStorageConfiguration": MediaStorageConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamInfo": StreamInfoTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamInfoList": List[StreamInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EdgeAgentStatusTypeDef = TypedDict(
    "EdgeAgentStatusTypeDef",
    {
        "LastRecorderStatus": LastRecorderStatusTypeDef,
        "LastUploaderStatus": LastUploaderStatusTypeDef,
    },
    total=False,
)

_RequiredGetSignalingChannelEndpointInputRequestTypeDef = TypedDict(
    "_RequiredGetSignalingChannelEndpointInputRequestTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalGetSignalingChannelEndpointInputRequestTypeDef = TypedDict(
    "_OptionalGetSignalingChannelEndpointInputRequestTypeDef",
    {
        "SingleMasterChannelEndpointConfiguration": SingleMasterChannelEndpointConfigurationTypeDef,
    },
    total=False,
)

class GetSignalingChannelEndpointInputRequestTypeDef(
    _RequiredGetSignalingChannelEndpointInputRequestTypeDef,
    _OptionalGetSignalingChannelEndpointInputRequestTypeDef,
):
    pass

GetSignalingChannelEndpointOutputTypeDef = TypedDict(
    "GetSignalingChannelEndpointOutputTypeDef",
    {
        "ResourceEndpointList": List[ResourceEndpointListItemTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImageGenerationConfigurationOutputTypeDef = TypedDict(
    "_RequiredImageGenerationConfigurationOutputTypeDef",
    {
        "Status": ConfigurationStatusType,
        "ImageSelectorType": ImageSelectorTypeType,
        "DestinationConfig": ImageGenerationDestinationConfigOutputTypeDef,
        "SamplingInterval": int,
        "Format": FormatType,
    },
)
_OptionalImageGenerationConfigurationOutputTypeDef = TypedDict(
    "_OptionalImageGenerationConfigurationOutputTypeDef",
    {
        "FormatConfig": Dict[Literal["JPEGQuality"], str],
        "WidthPixels": int,
        "HeightPixels": int,
    },
    total=False,
)

class ImageGenerationConfigurationOutputTypeDef(
    _RequiredImageGenerationConfigurationOutputTypeDef,
    _OptionalImageGenerationConfigurationOutputTypeDef,
):
    pass

_RequiredImageGenerationConfigurationTypeDef = TypedDict(
    "_RequiredImageGenerationConfigurationTypeDef",
    {
        "Status": ConfigurationStatusType,
        "ImageSelectorType": ImageSelectorTypeType,
        "DestinationConfig": ImageGenerationDestinationConfigTypeDef,
        "SamplingInterval": int,
        "Format": FormatType,
    },
)
_OptionalImageGenerationConfigurationTypeDef = TypedDict(
    "_OptionalImageGenerationConfigurationTypeDef",
    {
        "FormatConfig": Mapping[Literal["JPEGQuality"], str],
        "WidthPixels": int,
        "HeightPixels": int,
    },
    total=False,
)

class ImageGenerationConfigurationTypeDef(
    _RequiredImageGenerationConfigurationTypeDef, _OptionalImageGenerationConfigurationTypeDef
):
    pass

ListStreamsInputListStreamsPaginateTypeDef = TypedDict(
    "ListStreamsInputListStreamsPaginateTypeDef",
    {
        "StreamNameCondition": StreamNameConditionTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "StreamNameCondition": StreamNameConditionTypeDef,
    },
    total=False,
)

UpdateMediaStorageConfigurationInputRequestTypeDef = TypedDict(
    "UpdateMediaStorageConfigurationInputRequestTypeDef",
    {
        "ChannelARN": str,
        "MediaStorageConfiguration": MediaStorageConfigurationTypeDef,
    },
)

NotificationConfigurationOutputTypeDef = TypedDict(
    "NotificationConfigurationOutputTypeDef",
    {
        "Status": ConfigurationStatusType,
        "DestinationConfig": NotificationDestinationConfigOutputTypeDef,
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "Status": ConfigurationStatusType,
        "DestinationConfig": NotificationDestinationConfigTypeDef,
    },
)

_RequiredRecorderConfigOutputTypeDef = TypedDict(
    "_RequiredRecorderConfigOutputTypeDef",
    {
        "MediaSourceConfig": MediaSourceConfigOutputTypeDef,
    },
)
_OptionalRecorderConfigOutputTypeDef = TypedDict(
    "_OptionalRecorderConfigOutputTypeDef",
    {
        "ScheduleConfig": ScheduleConfigOutputTypeDef,
    },
    total=False,
)

class RecorderConfigOutputTypeDef(
    _RequiredRecorderConfigOutputTypeDef, _OptionalRecorderConfigOutputTypeDef
):
    pass

UploaderConfigOutputTypeDef = TypedDict(
    "UploaderConfigOutputTypeDef",
    {
        "ScheduleConfig": ScheduleConfigOutputTypeDef,
    },
)

_RequiredRecorderConfigTypeDef = TypedDict(
    "_RequiredRecorderConfigTypeDef",
    {
        "MediaSourceConfig": MediaSourceConfigTypeDef,
    },
)
_OptionalRecorderConfigTypeDef = TypedDict(
    "_OptionalRecorderConfigTypeDef",
    {
        "ScheduleConfig": ScheduleConfigTypeDef,
    },
    total=False,
)

class RecorderConfigTypeDef(_RequiredRecorderConfigTypeDef, _OptionalRecorderConfigTypeDef):
    pass

UploaderConfigTypeDef = TypedDict(
    "UploaderConfigTypeDef",
    {
        "ScheduleConfig": ScheduleConfigTypeDef,
    },
)

DescribeSignalingChannelOutputTypeDef = TypedDict(
    "DescribeSignalingChannelOutputTypeDef",
    {
        "ChannelInfo": ChannelInfoTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSignalingChannelsOutputTypeDef = TypedDict(
    "ListSignalingChannelsOutputTypeDef",
    {
        "ChannelInfoList": List[ChannelInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageGenerationConfigurationOutputTypeDef = TypedDict(
    "DescribeImageGenerationConfigurationOutputTypeDef",
    {
        "ImageGenerationConfiguration": ImageGenerationConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateImageGenerationConfigurationInputRequestTypeDef = TypedDict(
    "UpdateImageGenerationConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "ImageGenerationConfiguration": ImageGenerationConfigurationTypeDef,
    },
    total=False,
)

DescribeNotificationConfigurationOutputTypeDef = TypedDict(
    "DescribeNotificationConfigurationOutputTypeDef",
    {
        "NotificationConfiguration": NotificationConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNotificationConfigurationInputRequestTypeDef = TypedDict(
    "UpdateNotificationConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "NotificationConfiguration": NotificationConfigurationTypeDef,
    },
    total=False,
)

_RequiredEdgeConfigOutputTypeDef = TypedDict(
    "_RequiredEdgeConfigOutputTypeDef",
    {
        "HubDeviceArn": str,
        "RecorderConfig": RecorderConfigOutputTypeDef,
    },
)
_OptionalEdgeConfigOutputTypeDef = TypedDict(
    "_OptionalEdgeConfigOutputTypeDef",
    {
        "UploaderConfig": UploaderConfigOutputTypeDef,
        "DeletionConfig": DeletionConfigOutputTypeDef,
    },
    total=False,
)

class EdgeConfigOutputTypeDef(_RequiredEdgeConfigOutputTypeDef, _OptionalEdgeConfigOutputTypeDef):
    pass

_RequiredEdgeConfigTypeDef = TypedDict(
    "_RequiredEdgeConfigTypeDef",
    {
        "HubDeviceArn": str,
        "RecorderConfig": RecorderConfigTypeDef,
    },
)
_OptionalEdgeConfigTypeDef = TypedDict(
    "_OptionalEdgeConfigTypeDef",
    {
        "UploaderConfig": UploaderConfigTypeDef,
        "DeletionConfig": DeletionConfigTypeDef,
    },
    total=False,
)

class EdgeConfigTypeDef(_RequiredEdgeConfigTypeDef, _OptionalEdgeConfigTypeDef):
    pass

DescribeEdgeConfigurationOutputTypeDef = TypedDict(
    "DescribeEdgeConfigurationOutputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "SyncStatus": SyncStatusType,
        "FailedStatusDetails": str,
        "EdgeConfig": EdgeConfigOutputTypeDef,
        "EdgeAgentStatus": EdgeAgentStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEdgeAgentConfigurationsEdgeConfigTypeDef = TypedDict(
    "ListEdgeAgentConfigurationsEdgeConfigTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "SyncStatus": SyncStatusType,
        "FailedStatusDetails": str,
        "EdgeConfig": EdgeConfigOutputTypeDef,
    },
    total=False,
)

StartEdgeConfigurationUpdateOutputTypeDef = TypedDict(
    "StartEdgeConfigurationUpdateOutputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "SyncStatus": SyncStatusType,
        "FailedStatusDetails": str,
        "EdgeConfig": EdgeConfigOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartEdgeConfigurationUpdateInputRequestTypeDef = TypedDict(
    "_RequiredStartEdgeConfigurationUpdateInputRequestTypeDef",
    {
        "EdgeConfig": EdgeConfigTypeDef,
    },
)
_OptionalStartEdgeConfigurationUpdateInputRequestTypeDef = TypedDict(
    "_OptionalStartEdgeConfigurationUpdateInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class StartEdgeConfigurationUpdateInputRequestTypeDef(
    _RequiredStartEdgeConfigurationUpdateInputRequestTypeDef,
    _OptionalStartEdgeConfigurationUpdateInputRequestTypeDef,
):
    pass

ListEdgeAgentConfigurationsOutputTypeDef = TypedDict(
    "ListEdgeAgentConfigurationsOutputTypeDef",
    {
        "EdgeConfigs": List[ListEdgeAgentConfigurationsEdgeConfigTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
