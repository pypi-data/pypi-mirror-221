"""
Type annotations for chime-sdk-media-pipelines service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.type_defs import ActiveSpeakerOnlyConfigurationOutputTypeDef

    data: ActiveSpeakerOnlyConfigurationOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActiveSpeakerPositionType,
    ArtifactsConcatenationStateType,
    ArtifactsStateType,
    AudioChannelsOptionType,
    AudioMuxTypeType,
    BorderColorType,
    CallAnalyticsLanguageCodeType,
    CanvasOrientationType,
    ContentRedactionOutputType,
    ContentShareLayoutOptionType,
    FragmentSelectorTypeType,
    HighlightColorType,
    HorizontalTilePositionType,
    LiveConnectorMuxTypeType,
    MediaInsightsPipelineConfigurationElementTypeType,
    MediaPipelineStatusType,
    MediaPipelineStatusUpdateType,
    PartialResultsStabilityType,
    ParticipantRoleType,
    PresenterPositionType,
    RealTimeAlertRuleTypeType,
    RecordingFileFormatType,
    ResolutionOptionType,
    TileOrderType,
    VerticalTilePositionType,
    VocabularyFilterMethodType,
    VoiceAnalyticsConfigurationStatusType,
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
    "ActiveSpeakerOnlyConfigurationOutputTypeDef",
    "ActiveSpeakerOnlyConfigurationTypeDef",
    "PostCallAnalyticsSettingsOutputTypeDef",
    "PostCallAnalyticsSettingsTypeDef",
    "AmazonTranscribeProcessorConfigurationOutputTypeDef",
    "AmazonTranscribeProcessorConfigurationTypeDef",
    "AudioConcatenationConfigurationOutputTypeDef",
    "CompositedVideoConcatenationConfigurationOutputTypeDef",
    "ContentConcatenationConfigurationOutputTypeDef",
    "DataChannelConcatenationConfigurationOutputTypeDef",
    "MeetingEventsConcatenationConfigurationOutputTypeDef",
    "TranscriptionMessagesConcatenationConfigurationOutputTypeDef",
    "VideoConcatenationConfigurationOutputTypeDef",
    "AudioConcatenationConfigurationTypeDef",
    "CompositedVideoConcatenationConfigurationTypeDef",
    "ContentConcatenationConfigurationTypeDef",
    "DataChannelConcatenationConfigurationTypeDef",
    "MeetingEventsConcatenationConfigurationTypeDef",
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    "VideoConcatenationConfigurationTypeDef",
    "AudioArtifactsConfigurationOutputTypeDef",
    "ContentArtifactsConfigurationOutputTypeDef",
    "VideoArtifactsConfigurationOutputTypeDef",
    "AudioArtifactsConfigurationTypeDef",
    "ContentArtifactsConfigurationTypeDef",
    "VideoArtifactsConfigurationTypeDef",
    "ChannelDefinitionOutputTypeDef",
    "ChannelDefinitionTypeDef",
    "S3BucketSinkConfigurationOutputTypeDef",
    "S3BucketSinkConfigurationTypeDef",
    "TagTypeDef",
    "S3RecordingSinkRuntimeConfigurationTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "DeleteMediaPipelineRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "TimestampRangeOutputTypeDef",
    "TimestampRangeTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "GetMediaPipelineRequestRequestTypeDef",
    "HorizontalLayoutConfigurationOutputTypeDef",
    "PresenterOnlyConfigurationOutputTypeDef",
    "VerticalLayoutConfigurationOutputTypeDef",
    "VideoAttributeOutputTypeDef",
    "HorizontalLayoutConfigurationTypeDef",
    "PresenterOnlyConfigurationTypeDef",
    "VerticalLayoutConfigurationTypeDef",
    "VideoAttributeTypeDef",
    "IssueDetectionConfigurationOutputTypeDef",
    "IssueDetectionConfigurationTypeDef",
    "KeywordMatchConfigurationOutputTypeDef",
    "KeywordMatchConfigurationTypeDef",
    "KinesisDataStreamSinkConfigurationOutputTypeDef",
    "KinesisDataStreamSinkConfigurationTypeDef",
    "RecordingStreamConfigurationOutputTypeDef",
    "RecordingStreamConfigurationTypeDef",
    "LambdaFunctionSinkConfigurationOutputTypeDef",
    "LambdaFunctionSinkConfigurationTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "MediaCapturePipelineSummaryTypeDef",
    "ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef",
    "MediaInsightsPipelineConfigurationSummaryTypeDef",
    "ListMediaPipelinesRequestRequestTypeDef",
    "MediaPipelineSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "LiveConnectorRTMPConfigurationOutputTypeDef",
    "LiveConnectorRTMPConfigurationTypeDef",
    "S3RecordingSinkConfigurationOutputTypeDef",
    "SnsTopicSinkConfigurationOutputTypeDef",
    "SqsQueueSinkConfigurationOutputTypeDef",
    "VoiceAnalyticsProcessorConfigurationOutputTypeDef",
    "S3RecordingSinkConfigurationTypeDef",
    "SnsTopicSinkConfigurationTypeDef",
    "SqsQueueSinkConfigurationTypeDef",
    "VoiceAnalyticsProcessorConfigurationTypeDef",
    "S3RecordingSinkRuntimeConfigurationOutputTypeDef",
    "SentimentConfigurationOutputTypeDef",
    "SentimentConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "SelectedVideoStreamsOutputTypeDef",
    "SelectedVideoStreamsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateMediaInsightsPipelineStatusRequestRequestTypeDef",
    "AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef",
    "AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    "ArtifactsConcatenationConfigurationOutputTypeDef",
    "ArtifactsConcatenationConfigurationTypeDef",
    "StreamChannelDefinitionOutputTypeDef",
    "StreamChannelDefinitionTypeDef",
    "ConcatenationSinkOutputTypeDef",
    "ConcatenationSinkTypeDef",
    "TagResourceRequestRequestTypeDef",
    "FragmentSelectorOutputTypeDef",
    "FragmentSelectorTypeDef",
    "GridViewConfigurationOutputTypeDef",
    "GridViewConfigurationTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    "ListMediaPipelinesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LiveConnectorSinkConfigurationOutputTypeDef",
    "LiveConnectorSinkConfigurationTypeDef",
    "RealTimeAlertRuleOutputTypeDef",
    "RealTimeAlertRuleTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "MediaInsightsPipelineConfigurationElementOutputTypeDef",
    "MediaInsightsPipelineConfigurationElementTypeDef",
    "ChimeSdkMeetingConcatenationConfigurationOutputTypeDef",
    "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    "StreamConfigurationOutputTypeDef",
    "StreamConfigurationTypeDef",
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef",
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
    "CompositedVideoArtifactsConfigurationOutputTypeDef",
    "CompositedVideoArtifactsConfigurationTypeDef",
    "RealTimeAlertConfigurationOutputTypeDef",
    "RealTimeAlertConfigurationTypeDef",
    "MediaCapturePipelineSourceConfigurationOutputTypeDef",
    "MediaCapturePipelineSourceConfigurationTypeDef",
    "KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef",
    "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
    "ArtifactsConfigurationOutputTypeDef",
    "ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef",
    "ArtifactsConfigurationTypeDef",
    "ChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    "MediaInsightsPipelineConfigurationTypeDef",
    "CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "ConcatenationSourceOutputTypeDef",
    "ConcatenationSourceTypeDef",
    "MediaInsightsPipelineTypeDef",
    "CreateMediaInsightsPipelineRequestRequestTypeDef",
    "ChimeSdkMeetingConfigurationOutputTypeDef",
    "LiveConnectorSourceConfigurationOutputTypeDef",
    "ChimeSdkMeetingConfigurationTypeDef",
    "LiveConnectorSourceConfigurationTypeDef",
    "CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    "GetMediaInsightsPipelineConfigurationResponseTypeDef",
    "UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    "MediaConcatenationPipelineTypeDef",
    "CreateMediaConcatenationPipelineRequestRequestTypeDef",
    "CreateMediaInsightsPipelineResponseTypeDef",
    "MediaCapturePipelineTypeDef",
    "MediaLiveConnectorPipelineTypeDef",
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    "CreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    "CreateMediaConcatenationPipelineResponseTypeDef",
    "CreateMediaCapturePipelineResponseTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    "MediaPipelineTypeDef",
    "GetMediaPipelineResponseTypeDef",
)

ActiveSpeakerOnlyConfigurationOutputTypeDef = TypedDict(
    "ActiveSpeakerOnlyConfigurationOutputTypeDef",
    {
        "ActiveSpeakerPosition": ActiveSpeakerPositionType,
    },
    total=False,
)

ActiveSpeakerOnlyConfigurationTypeDef = TypedDict(
    "ActiveSpeakerOnlyConfigurationTypeDef",
    {
        "ActiveSpeakerPosition": ActiveSpeakerPositionType,
    },
    total=False,
)

_RequiredPostCallAnalyticsSettingsOutputTypeDef = TypedDict(
    "_RequiredPostCallAnalyticsSettingsOutputTypeDef",
    {
        "OutputLocation": str,
        "DataAccessRoleArn": str,
    },
)
_OptionalPostCallAnalyticsSettingsOutputTypeDef = TypedDict(
    "_OptionalPostCallAnalyticsSettingsOutputTypeDef",
    {
        "ContentRedactionOutput": ContentRedactionOutputType,
        "OutputEncryptionKMSKeyId": str,
    },
    total=False,
)

class PostCallAnalyticsSettingsOutputTypeDef(
    _RequiredPostCallAnalyticsSettingsOutputTypeDef, _OptionalPostCallAnalyticsSettingsOutputTypeDef
):
    pass

_RequiredPostCallAnalyticsSettingsTypeDef = TypedDict(
    "_RequiredPostCallAnalyticsSettingsTypeDef",
    {
        "OutputLocation": str,
        "DataAccessRoleArn": str,
    },
)
_OptionalPostCallAnalyticsSettingsTypeDef = TypedDict(
    "_OptionalPostCallAnalyticsSettingsTypeDef",
    {
        "ContentRedactionOutput": ContentRedactionOutputType,
        "OutputEncryptionKMSKeyId": str,
    },
    total=False,
)

class PostCallAnalyticsSettingsTypeDef(
    _RequiredPostCallAnalyticsSettingsTypeDef, _OptionalPostCallAnalyticsSettingsTypeDef
):
    pass

AmazonTranscribeProcessorConfigurationOutputTypeDef = TypedDict(
    "AmazonTranscribeProcessorConfigurationOutputTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "ShowSpeakerLabel": bool,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "LanguageModelName": str,
        "FilterPartialResults": bool,
        "IdentifyLanguage": bool,
        "LanguageOptions": str,
        "PreferredLanguage": CallAnalyticsLanguageCodeType,
        "VocabularyNames": str,
        "VocabularyFilterNames": str,
    },
    total=False,
)

AmazonTranscribeProcessorConfigurationTypeDef = TypedDict(
    "AmazonTranscribeProcessorConfigurationTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "ShowSpeakerLabel": bool,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "LanguageModelName": str,
        "FilterPartialResults": bool,
        "IdentifyLanguage": bool,
        "LanguageOptions": str,
        "PreferredLanguage": CallAnalyticsLanguageCodeType,
        "VocabularyNames": str,
        "VocabularyFilterNames": str,
    },
    total=False,
)

AudioConcatenationConfigurationOutputTypeDef = TypedDict(
    "AudioConcatenationConfigurationOutputTypeDef",
    {
        "State": Literal["Enabled"],
    },
)

CompositedVideoConcatenationConfigurationOutputTypeDef = TypedDict(
    "CompositedVideoConcatenationConfigurationOutputTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

ContentConcatenationConfigurationOutputTypeDef = TypedDict(
    "ContentConcatenationConfigurationOutputTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

DataChannelConcatenationConfigurationOutputTypeDef = TypedDict(
    "DataChannelConcatenationConfigurationOutputTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

MeetingEventsConcatenationConfigurationOutputTypeDef = TypedDict(
    "MeetingEventsConcatenationConfigurationOutputTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

TranscriptionMessagesConcatenationConfigurationOutputTypeDef = TypedDict(
    "TranscriptionMessagesConcatenationConfigurationOutputTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

VideoConcatenationConfigurationOutputTypeDef = TypedDict(
    "VideoConcatenationConfigurationOutputTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

AudioConcatenationConfigurationTypeDef = TypedDict(
    "AudioConcatenationConfigurationTypeDef",
    {
        "State": Literal["Enabled"],
    },
)

CompositedVideoConcatenationConfigurationTypeDef = TypedDict(
    "CompositedVideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

ContentConcatenationConfigurationTypeDef = TypedDict(
    "ContentConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

DataChannelConcatenationConfigurationTypeDef = TypedDict(
    "DataChannelConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

MeetingEventsConcatenationConfigurationTypeDef = TypedDict(
    "MeetingEventsConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

TranscriptionMessagesConcatenationConfigurationTypeDef = TypedDict(
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

VideoConcatenationConfigurationTypeDef = TypedDict(
    "VideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

AudioArtifactsConfigurationOutputTypeDef = TypedDict(
    "AudioArtifactsConfigurationOutputTypeDef",
    {
        "MuxType": AudioMuxTypeType,
    },
)

_RequiredContentArtifactsConfigurationOutputTypeDef = TypedDict(
    "_RequiredContentArtifactsConfigurationOutputTypeDef",
    {
        "State": ArtifactsStateType,
    },
)
_OptionalContentArtifactsConfigurationOutputTypeDef = TypedDict(
    "_OptionalContentArtifactsConfigurationOutputTypeDef",
    {
        "MuxType": Literal["ContentOnly"],
    },
    total=False,
)

class ContentArtifactsConfigurationOutputTypeDef(
    _RequiredContentArtifactsConfigurationOutputTypeDef,
    _OptionalContentArtifactsConfigurationOutputTypeDef,
):
    pass

_RequiredVideoArtifactsConfigurationOutputTypeDef = TypedDict(
    "_RequiredVideoArtifactsConfigurationOutputTypeDef",
    {
        "State": ArtifactsStateType,
    },
)
_OptionalVideoArtifactsConfigurationOutputTypeDef = TypedDict(
    "_OptionalVideoArtifactsConfigurationOutputTypeDef",
    {
        "MuxType": Literal["VideoOnly"],
    },
    total=False,
)

class VideoArtifactsConfigurationOutputTypeDef(
    _RequiredVideoArtifactsConfigurationOutputTypeDef,
    _OptionalVideoArtifactsConfigurationOutputTypeDef,
):
    pass

AudioArtifactsConfigurationTypeDef = TypedDict(
    "AudioArtifactsConfigurationTypeDef",
    {
        "MuxType": AudioMuxTypeType,
    },
)

_RequiredContentArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredContentArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
    },
)
_OptionalContentArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalContentArtifactsConfigurationTypeDef",
    {
        "MuxType": Literal["ContentOnly"],
    },
    total=False,
)

class ContentArtifactsConfigurationTypeDef(
    _RequiredContentArtifactsConfigurationTypeDef, _OptionalContentArtifactsConfigurationTypeDef
):
    pass

_RequiredVideoArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredVideoArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
    },
)
_OptionalVideoArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalVideoArtifactsConfigurationTypeDef",
    {
        "MuxType": Literal["VideoOnly"],
    },
    total=False,
)

class VideoArtifactsConfigurationTypeDef(
    _RequiredVideoArtifactsConfigurationTypeDef, _OptionalVideoArtifactsConfigurationTypeDef
):
    pass

_RequiredChannelDefinitionOutputTypeDef = TypedDict(
    "_RequiredChannelDefinitionOutputTypeDef",
    {
        "ChannelId": int,
    },
)
_OptionalChannelDefinitionOutputTypeDef = TypedDict(
    "_OptionalChannelDefinitionOutputTypeDef",
    {
        "ParticipantRole": ParticipantRoleType,
    },
    total=False,
)

class ChannelDefinitionOutputTypeDef(
    _RequiredChannelDefinitionOutputTypeDef, _OptionalChannelDefinitionOutputTypeDef
):
    pass

_RequiredChannelDefinitionTypeDef = TypedDict(
    "_RequiredChannelDefinitionTypeDef",
    {
        "ChannelId": int,
    },
)
_OptionalChannelDefinitionTypeDef = TypedDict(
    "_OptionalChannelDefinitionTypeDef",
    {
        "ParticipantRole": ParticipantRoleType,
    },
    total=False,
)

class ChannelDefinitionTypeDef(
    _RequiredChannelDefinitionTypeDef, _OptionalChannelDefinitionTypeDef
):
    pass

S3BucketSinkConfigurationOutputTypeDef = TypedDict(
    "S3BucketSinkConfigurationOutputTypeDef",
    {
        "Destination": str,
    },
)

S3BucketSinkConfigurationTypeDef = TypedDict(
    "S3BucketSinkConfigurationTypeDef",
    {
        "Destination": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

S3RecordingSinkRuntimeConfigurationTypeDef = TypedDict(
    "S3RecordingSinkRuntimeConfigurationTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
    },
)

DeleteMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteMediaPipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TimestampRangeOutputTypeDef = TypedDict(
    "TimestampRangeOutputTypeDef",
    {
        "StartTimestamp": datetime,
        "EndTimestamp": datetime,
    },
)

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
)

GetMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "GetMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

GetMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "GetMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetMediaPipelineRequestRequestTypeDef = TypedDict(
    "GetMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

HorizontalLayoutConfigurationOutputTypeDef = TypedDict(
    "HorizontalLayoutConfigurationOutputTypeDef",
    {
        "TileOrder": TileOrderType,
        "TilePosition": HorizontalTilePositionType,
        "TileCount": int,
        "TileAspectRatio": str,
    },
    total=False,
)

PresenterOnlyConfigurationOutputTypeDef = TypedDict(
    "PresenterOnlyConfigurationOutputTypeDef",
    {
        "PresenterPosition": PresenterPositionType,
    },
    total=False,
)

VerticalLayoutConfigurationOutputTypeDef = TypedDict(
    "VerticalLayoutConfigurationOutputTypeDef",
    {
        "TileOrder": TileOrderType,
        "TilePosition": VerticalTilePositionType,
        "TileCount": int,
        "TileAspectRatio": str,
    },
    total=False,
)

VideoAttributeOutputTypeDef = TypedDict(
    "VideoAttributeOutputTypeDef",
    {
        "CornerRadius": int,
        "BorderColor": BorderColorType,
        "HighlightColor": HighlightColorType,
        "BorderThickness": int,
    },
    total=False,
)

HorizontalLayoutConfigurationTypeDef = TypedDict(
    "HorizontalLayoutConfigurationTypeDef",
    {
        "TileOrder": TileOrderType,
        "TilePosition": HorizontalTilePositionType,
        "TileCount": int,
        "TileAspectRatio": str,
    },
    total=False,
)

PresenterOnlyConfigurationTypeDef = TypedDict(
    "PresenterOnlyConfigurationTypeDef",
    {
        "PresenterPosition": PresenterPositionType,
    },
    total=False,
)

VerticalLayoutConfigurationTypeDef = TypedDict(
    "VerticalLayoutConfigurationTypeDef",
    {
        "TileOrder": TileOrderType,
        "TilePosition": VerticalTilePositionType,
        "TileCount": int,
        "TileAspectRatio": str,
    },
    total=False,
)

VideoAttributeTypeDef = TypedDict(
    "VideoAttributeTypeDef",
    {
        "CornerRadius": int,
        "BorderColor": BorderColorType,
        "HighlightColor": HighlightColorType,
        "BorderThickness": int,
    },
    total=False,
)

IssueDetectionConfigurationOutputTypeDef = TypedDict(
    "IssueDetectionConfigurationOutputTypeDef",
    {
        "RuleName": str,
    },
)

IssueDetectionConfigurationTypeDef = TypedDict(
    "IssueDetectionConfigurationTypeDef",
    {
        "RuleName": str,
    },
)

_RequiredKeywordMatchConfigurationOutputTypeDef = TypedDict(
    "_RequiredKeywordMatchConfigurationOutputTypeDef",
    {
        "RuleName": str,
        "Keywords": List[str],
    },
)
_OptionalKeywordMatchConfigurationOutputTypeDef = TypedDict(
    "_OptionalKeywordMatchConfigurationOutputTypeDef",
    {
        "Negate": bool,
    },
    total=False,
)

class KeywordMatchConfigurationOutputTypeDef(
    _RequiredKeywordMatchConfigurationOutputTypeDef, _OptionalKeywordMatchConfigurationOutputTypeDef
):
    pass

_RequiredKeywordMatchConfigurationTypeDef = TypedDict(
    "_RequiredKeywordMatchConfigurationTypeDef",
    {
        "RuleName": str,
        "Keywords": Sequence[str],
    },
)
_OptionalKeywordMatchConfigurationTypeDef = TypedDict(
    "_OptionalKeywordMatchConfigurationTypeDef",
    {
        "Negate": bool,
    },
    total=False,
)

class KeywordMatchConfigurationTypeDef(
    _RequiredKeywordMatchConfigurationTypeDef, _OptionalKeywordMatchConfigurationTypeDef
):
    pass

KinesisDataStreamSinkConfigurationOutputTypeDef = TypedDict(
    "KinesisDataStreamSinkConfigurationOutputTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

KinesisDataStreamSinkConfigurationTypeDef = TypedDict(
    "KinesisDataStreamSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

RecordingStreamConfigurationOutputTypeDef = TypedDict(
    "RecordingStreamConfigurationOutputTypeDef",
    {
        "StreamArn": str,
    },
    total=False,
)

RecordingStreamConfigurationTypeDef = TypedDict(
    "RecordingStreamConfigurationTypeDef",
    {
        "StreamArn": str,
    },
    total=False,
)

LambdaFunctionSinkConfigurationOutputTypeDef = TypedDict(
    "LambdaFunctionSinkConfigurationOutputTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

LambdaFunctionSinkConfigurationTypeDef = TypedDict(
    "LambdaFunctionSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

ListMediaCapturePipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

MediaCapturePipelineSummaryTypeDef = TypedDict(
    "MediaCapturePipelineSummaryTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
    },
    total=False,
)

ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef = TypedDict(
    "ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

MediaInsightsPipelineConfigurationSummaryTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationSummaryTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "MediaInsightsPipelineConfigurationId": str,
        "MediaInsightsPipelineConfigurationArn": str,
    },
    total=False,
)

ListMediaPipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaPipelinesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

MediaPipelineSummaryTypeDef = TypedDict(
    "MediaPipelineSummaryTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredLiveConnectorRTMPConfigurationOutputTypeDef = TypedDict(
    "_RequiredLiveConnectorRTMPConfigurationOutputTypeDef",
    {
        "Url": str,
    },
)
_OptionalLiveConnectorRTMPConfigurationOutputTypeDef = TypedDict(
    "_OptionalLiveConnectorRTMPConfigurationOutputTypeDef",
    {
        "AudioChannels": AudioChannelsOptionType,
        "AudioSampleRate": str,
    },
    total=False,
)

class LiveConnectorRTMPConfigurationOutputTypeDef(
    _RequiredLiveConnectorRTMPConfigurationOutputTypeDef,
    _OptionalLiveConnectorRTMPConfigurationOutputTypeDef,
):
    pass

_RequiredLiveConnectorRTMPConfigurationTypeDef = TypedDict(
    "_RequiredLiveConnectorRTMPConfigurationTypeDef",
    {
        "Url": str,
    },
)
_OptionalLiveConnectorRTMPConfigurationTypeDef = TypedDict(
    "_OptionalLiveConnectorRTMPConfigurationTypeDef",
    {
        "AudioChannels": AudioChannelsOptionType,
        "AudioSampleRate": str,
    },
    total=False,
)

class LiveConnectorRTMPConfigurationTypeDef(
    _RequiredLiveConnectorRTMPConfigurationTypeDef, _OptionalLiveConnectorRTMPConfigurationTypeDef
):
    pass

S3RecordingSinkConfigurationOutputTypeDef = TypedDict(
    "S3RecordingSinkConfigurationOutputTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
    },
    total=False,
)

SnsTopicSinkConfigurationOutputTypeDef = TypedDict(
    "SnsTopicSinkConfigurationOutputTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

SqsQueueSinkConfigurationOutputTypeDef = TypedDict(
    "SqsQueueSinkConfigurationOutputTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

VoiceAnalyticsProcessorConfigurationOutputTypeDef = TypedDict(
    "VoiceAnalyticsProcessorConfigurationOutputTypeDef",
    {
        "SpeakerSearchStatus": VoiceAnalyticsConfigurationStatusType,
        "VoiceToneAnalysisStatus": VoiceAnalyticsConfigurationStatusType,
    },
    total=False,
)

S3RecordingSinkConfigurationTypeDef = TypedDict(
    "S3RecordingSinkConfigurationTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
    },
    total=False,
)

SnsTopicSinkConfigurationTypeDef = TypedDict(
    "SnsTopicSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

SqsQueueSinkConfigurationTypeDef = TypedDict(
    "SqsQueueSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

VoiceAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "VoiceAnalyticsProcessorConfigurationTypeDef",
    {
        "SpeakerSearchStatus": VoiceAnalyticsConfigurationStatusType,
        "VoiceToneAnalysisStatus": VoiceAnalyticsConfigurationStatusType,
    },
    total=False,
)

S3RecordingSinkRuntimeConfigurationOutputTypeDef = TypedDict(
    "S3RecordingSinkRuntimeConfigurationOutputTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
    },
)

SentimentConfigurationOutputTypeDef = TypedDict(
    "SentimentConfigurationOutputTypeDef",
    {
        "RuleName": str,
        "SentimentType": Literal["NEGATIVE"],
        "TimePeriod": int,
    },
)

SentimentConfigurationTypeDef = TypedDict(
    "SentimentConfigurationTypeDef",
    {
        "RuleName": str,
        "SentimentType": Literal["NEGATIVE"],
        "TimePeriod": int,
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

SelectedVideoStreamsOutputTypeDef = TypedDict(
    "SelectedVideoStreamsOutputTypeDef",
    {
        "AttendeeIds": List[str],
        "ExternalUserIds": List[str],
    },
    total=False,
)

SelectedVideoStreamsTypeDef = TypedDict(
    "SelectedVideoStreamsTypeDef",
    {
        "AttendeeIds": Sequence[str],
        "ExternalUserIds": Sequence[str],
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateMediaInsightsPipelineStatusRequestRequestTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineStatusRequestRequestTypeDef",
    {
        "Identifier": str,
        "UpdateStatus": MediaPipelineStatusUpdateType,
    },
)

_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef = TypedDict(
    "_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
    },
)
_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef = TypedDict(
    "_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef",
    {
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "LanguageModelName": str,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "FilterPartialResults": bool,
        "PostCallAnalyticsSettings": PostCallAnalyticsSettingsOutputTypeDef,
        "CallAnalyticsStreamCategories": List[str],
    },
    total=False,
)

class AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef(
    _RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef,
    _OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef,
):
    pass

_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
    },
)
_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    {
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "LanguageModelName": str,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "FilterPartialResults": bool,
        "PostCallAnalyticsSettings": PostCallAnalyticsSettingsTypeDef,
        "CallAnalyticsStreamCategories": Sequence[str],
    },
    total=False,
)

class AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef(
    _RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef,
    _OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef,
):
    pass

ArtifactsConcatenationConfigurationOutputTypeDef = TypedDict(
    "ArtifactsConcatenationConfigurationOutputTypeDef",
    {
        "Audio": AudioConcatenationConfigurationOutputTypeDef,
        "Video": VideoConcatenationConfigurationOutputTypeDef,
        "Content": ContentConcatenationConfigurationOutputTypeDef,
        "DataChannel": DataChannelConcatenationConfigurationOutputTypeDef,
        "TranscriptionMessages": TranscriptionMessagesConcatenationConfigurationOutputTypeDef,
        "MeetingEvents": MeetingEventsConcatenationConfigurationOutputTypeDef,
        "CompositedVideo": CompositedVideoConcatenationConfigurationOutputTypeDef,
    },
)

ArtifactsConcatenationConfigurationTypeDef = TypedDict(
    "ArtifactsConcatenationConfigurationTypeDef",
    {
        "Audio": AudioConcatenationConfigurationTypeDef,
        "Video": VideoConcatenationConfigurationTypeDef,
        "Content": ContentConcatenationConfigurationTypeDef,
        "DataChannel": DataChannelConcatenationConfigurationTypeDef,
        "TranscriptionMessages": TranscriptionMessagesConcatenationConfigurationTypeDef,
        "MeetingEvents": MeetingEventsConcatenationConfigurationTypeDef,
        "CompositedVideo": CompositedVideoConcatenationConfigurationTypeDef,
    },
)

_RequiredStreamChannelDefinitionOutputTypeDef = TypedDict(
    "_RequiredStreamChannelDefinitionOutputTypeDef",
    {
        "NumberOfChannels": int,
    },
)
_OptionalStreamChannelDefinitionOutputTypeDef = TypedDict(
    "_OptionalStreamChannelDefinitionOutputTypeDef",
    {
        "ChannelDefinitions": List[ChannelDefinitionOutputTypeDef],
    },
    total=False,
)

class StreamChannelDefinitionOutputTypeDef(
    _RequiredStreamChannelDefinitionOutputTypeDef, _OptionalStreamChannelDefinitionOutputTypeDef
):
    pass

_RequiredStreamChannelDefinitionTypeDef = TypedDict(
    "_RequiredStreamChannelDefinitionTypeDef",
    {
        "NumberOfChannels": int,
    },
)
_OptionalStreamChannelDefinitionTypeDef = TypedDict(
    "_OptionalStreamChannelDefinitionTypeDef",
    {
        "ChannelDefinitions": Sequence[ChannelDefinitionTypeDef],
    },
    total=False,
)

class StreamChannelDefinitionTypeDef(
    _RequiredStreamChannelDefinitionTypeDef, _OptionalStreamChannelDefinitionTypeDef
):
    pass

ConcatenationSinkOutputTypeDef = TypedDict(
    "ConcatenationSinkOutputTypeDef",
    {
        "Type": Literal["S3Bucket"],
        "S3BucketSinkConfiguration": S3BucketSinkConfigurationOutputTypeDef,
    },
)

ConcatenationSinkTypeDef = TypedDict(
    "ConcatenationSinkTypeDef",
    {
        "Type": Literal["S3Bucket"],
        "S3BucketSinkConfiguration": S3BucketSinkConfigurationTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

FragmentSelectorOutputTypeDef = TypedDict(
    "FragmentSelectorOutputTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": TimestampRangeOutputTypeDef,
    },
)

FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": TimestampRangeTypeDef,
    },
)

_RequiredGridViewConfigurationOutputTypeDef = TypedDict(
    "_RequiredGridViewConfigurationOutputTypeDef",
    {
        "ContentShareLayout": ContentShareLayoutOptionType,
    },
)
_OptionalGridViewConfigurationOutputTypeDef = TypedDict(
    "_OptionalGridViewConfigurationOutputTypeDef",
    {
        "PresenterOnlyConfiguration": PresenterOnlyConfigurationOutputTypeDef,
        "ActiveSpeakerOnlyConfiguration": ActiveSpeakerOnlyConfigurationOutputTypeDef,
        "HorizontalLayoutConfiguration": HorizontalLayoutConfigurationOutputTypeDef,
        "VerticalLayoutConfiguration": VerticalLayoutConfigurationOutputTypeDef,
        "VideoAttribute": VideoAttributeOutputTypeDef,
        "CanvasOrientation": CanvasOrientationType,
    },
    total=False,
)

class GridViewConfigurationOutputTypeDef(
    _RequiredGridViewConfigurationOutputTypeDef, _OptionalGridViewConfigurationOutputTypeDef
):
    pass

_RequiredGridViewConfigurationTypeDef = TypedDict(
    "_RequiredGridViewConfigurationTypeDef",
    {
        "ContentShareLayout": ContentShareLayoutOptionType,
    },
)
_OptionalGridViewConfigurationTypeDef = TypedDict(
    "_OptionalGridViewConfigurationTypeDef",
    {
        "PresenterOnlyConfiguration": PresenterOnlyConfigurationTypeDef,
        "ActiveSpeakerOnlyConfiguration": ActiveSpeakerOnlyConfigurationTypeDef,
        "HorizontalLayoutConfiguration": HorizontalLayoutConfigurationTypeDef,
        "VerticalLayoutConfiguration": VerticalLayoutConfigurationTypeDef,
        "VideoAttribute": VideoAttributeTypeDef,
        "CanvasOrientation": CanvasOrientationType,
    },
    total=False,
)

class GridViewConfigurationTypeDef(
    _RequiredGridViewConfigurationTypeDef, _OptionalGridViewConfigurationTypeDef
):
    pass

ListMediaCapturePipelinesResponseTypeDef = TypedDict(
    "ListMediaCapturePipelinesResponseTypeDef",
    {
        "MediaCapturePipelines": List[MediaCapturePipelineSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMediaInsightsPipelineConfigurationsResponseTypeDef = TypedDict(
    "ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    {
        "MediaInsightsPipelineConfigurations": List[
            MediaInsightsPipelineConfigurationSummaryTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMediaPipelinesResponseTypeDef = TypedDict(
    "ListMediaPipelinesResponseTypeDef",
    {
        "MediaPipelines": List[MediaPipelineSummaryTypeDef],
        "NextToken": str,
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

LiveConnectorSinkConfigurationOutputTypeDef = TypedDict(
    "LiveConnectorSinkConfigurationOutputTypeDef",
    {
        "SinkType": Literal["RTMP"],
        "RTMPConfiguration": LiveConnectorRTMPConfigurationOutputTypeDef,
    },
)

LiveConnectorSinkConfigurationTypeDef = TypedDict(
    "LiveConnectorSinkConfigurationTypeDef",
    {
        "SinkType": Literal["RTMP"],
        "RTMPConfiguration": LiveConnectorRTMPConfigurationTypeDef,
    },
)

_RequiredRealTimeAlertRuleOutputTypeDef = TypedDict(
    "_RequiredRealTimeAlertRuleOutputTypeDef",
    {
        "Type": RealTimeAlertRuleTypeType,
    },
)
_OptionalRealTimeAlertRuleOutputTypeDef = TypedDict(
    "_OptionalRealTimeAlertRuleOutputTypeDef",
    {
        "KeywordMatchConfiguration": KeywordMatchConfigurationOutputTypeDef,
        "SentimentConfiguration": SentimentConfigurationOutputTypeDef,
        "IssueDetectionConfiguration": IssueDetectionConfigurationOutputTypeDef,
    },
    total=False,
)

class RealTimeAlertRuleOutputTypeDef(
    _RequiredRealTimeAlertRuleOutputTypeDef, _OptionalRealTimeAlertRuleOutputTypeDef
):
    pass

_RequiredRealTimeAlertRuleTypeDef = TypedDict(
    "_RequiredRealTimeAlertRuleTypeDef",
    {
        "Type": RealTimeAlertRuleTypeType,
    },
)
_OptionalRealTimeAlertRuleTypeDef = TypedDict(
    "_OptionalRealTimeAlertRuleTypeDef",
    {
        "KeywordMatchConfiguration": KeywordMatchConfigurationTypeDef,
        "SentimentConfiguration": SentimentConfigurationTypeDef,
        "IssueDetectionConfiguration": IssueDetectionConfigurationTypeDef,
    },
    total=False,
)

class RealTimeAlertRuleTypeDef(
    _RequiredRealTimeAlertRuleTypeDef, _OptionalRealTimeAlertRuleTypeDef
):
    pass

SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "SelectedVideoStreams": SelectedVideoStreamsOutputTypeDef,
    },
    total=False,
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "SelectedVideoStreams": SelectedVideoStreamsTypeDef,
    },
    total=False,
)

_RequiredMediaInsightsPipelineConfigurationElementOutputTypeDef = TypedDict(
    "_RequiredMediaInsightsPipelineConfigurationElementOutputTypeDef",
    {
        "Type": MediaInsightsPipelineConfigurationElementTypeType,
    },
)
_OptionalMediaInsightsPipelineConfigurationElementOutputTypeDef = TypedDict(
    "_OptionalMediaInsightsPipelineConfigurationElementOutputTypeDef",
    {
        "AmazonTranscribeCallAnalyticsProcessorConfiguration": (
            AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef
        ),
        "AmazonTranscribeProcessorConfiguration": (
            AmazonTranscribeProcessorConfigurationOutputTypeDef
        ),
        "KinesisDataStreamSinkConfiguration": KinesisDataStreamSinkConfigurationOutputTypeDef,
        "S3RecordingSinkConfiguration": S3RecordingSinkConfigurationOutputTypeDef,
        "VoiceAnalyticsProcessorConfiguration": VoiceAnalyticsProcessorConfigurationOutputTypeDef,
        "LambdaFunctionSinkConfiguration": LambdaFunctionSinkConfigurationOutputTypeDef,
        "SqsQueueSinkConfiguration": SqsQueueSinkConfigurationOutputTypeDef,
        "SnsTopicSinkConfiguration": SnsTopicSinkConfigurationOutputTypeDef,
    },
    total=False,
)

class MediaInsightsPipelineConfigurationElementOutputTypeDef(
    _RequiredMediaInsightsPipelineConfigurationElementOutputTypeDef,
    _OptionalMediaInsightsPipelineConfigurationElementOutputTypeDef,
):
    pass

_RequiredMediaInsightsPipelineConfigurationElementTypeDef = TypedDict(
    "_RequiredMediaInsightsPipelineConfigurationElementTypeDef",
    {
        "Type": MediaInsightsPipelineConfigurationElementTypeType,
    },
)
_OptionalMediaInsightsPipelineConfigurationElementTypeDef = TypedDict(
    "_OptionalMediaInsightsPipelineConfigurationElementTypeDef",
    {
        "AmazonTranscribeCallAnalyticsProcessorConfiguration": (
            AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef
        ),
        "AmazonTranscribeProcessorConfiguration": AmazonTranscribeProcessorConfigurationTypeDef,
        "KinesisDataStreamSinkConfiguration": KinesisDataStreamSinkConfigurationTypeDef,
        "S3RecordingSinkConfiguration": S3RecordingSinkConfigurationTypeDef,
        "VoiceAnalyticsProcessorConfiguration": VoiceAnalyticsProcessorConfigurationTypeDef,
        "LambdaFunctionSinkConfiguration": LambdaFunctionSinkConfigurationTypeDef,
        "SqsQueueSinkConfiguration": SqsQueueSinkConfigurationTypeDef,
        "SnsTopicSinkConfiguration": SnsTopicSinkConfigurationTypeDef,
    },
    total=False,
)

class MediaInsightsPipelineConfigurationElementTypeDef(
    _RequiredMediaInsightsPipelineConfigurationElementTypeDef,
    _OptionalMediaInsightsPipelineConfigurationElementTypeDef,
):
    pass

ChimeSdkMeetingConcatenationConfigurationOutputTypeDef = TypedDict(
    "ChimeSdkMeetingConcatenationConfigurationOutputTypeDef",
    {
        "ArtifactsConfiguration": ArtifactsConcatenationConfigurationOutputTypeDef,
    },
)

ChimeSdkMeetingConcatenationConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    {
        "ArtifactsConfiguration": ArtifactsConcatenationConfigurationTypeDef,
    },
)

_RequiredStreamConfigurationOutputTypeDef = TypedDict(
    "_RequiredStreamConfigurationOutputTypeDef",
    {
        "StreamArn": str,
        "StreamChannelDefinition": StreamChannelDefinitionOutputTypeDef,
    },
)
_OptionalStreamConfigurationOutputTypeDef = TypedDict(
    "_OptionalStreamConfigurationOutputTypeDef",
    {
        "FragmentNumber": str,
    },
    total=False,
)

class StreamConfigurationOutputTypeDef(
    _RequiredStreamConfigurationOutputTypeDef, _OptionalStreamConfigurationOutputTypeDef
):
    pass

_RequiredStreamConfigurationTypeDef = TypedDict(
    "_RequiredStreamConfigurationTypeDef",
    {
        "StreamArn": str,
        "StreamChannelDefinition": StreamChannelDefinitionTypeDef,
    },
)
_OptionalStreamConfigurationTypeDef = TypedDict(
    "_OptionalStreamConfigurationTypeDef",
    {
        "FragmentNumber": str,
    },
    total=False,
)

class StreamConfigurationTypeDef(
    _RequiredStreamConfigurationTypeDef, _OptionalStreamConfigurationTypeDef
):
    pass

KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef = TypedDict(
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef",
    {
        "Streams": List[RecordingStreamConfigurationOutputTypeDef],
        "FragmentSelector": FragmentSelectorOutputTypeDef,
    },
)

KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
    {
        "Streams": Sequence[RecordingStreamConfigurationTypeDef],
        "FragmentSelector": FragmentSelectorTypeDef,
    },
)

_RequiredCompositedVideoArtifactsConfigurationOutputTypeDef = TypedDict(
    "_RequiredCompositedVideoArtifactsConfigurationOutputTypeDef",
    {
        "GridViewConfiguration": GridViewConfigurationOutputTypeDef,
    },
)
_OptionalCompositedVideoArtifactsConfigurationOutputTypeDef = TypedDict(
    "_OptionalCompositedVideoArtifactsConfigurationOutputTypeDef",
    {
        "Layout": Literal["GridView"],
        "Resolution": ResolutionOptionType,
    },
    total=False,
)

class CompositedVideoArtifactsConfigurationOutputTypeDef(
    _RequiredCompositedVideoArtifactsConfigurationOutputTypeDef,
    _OptionalCompositedVideoArtifactsConfigurationOutputTypeDef,
):
    pass

_RequiredCompositedVideoArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredCompositedVideoArtifactsConfigurationTypeDef",
    {
        "GridViewConfiguration": GridViewConfigurationTypeDef,
    },
)
_OptionalCompositedVideoArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalCompositedVideoArtifactsConfigurationTypeDef",
    {
        "Layout": Literal["GridView"],
        "Resolution": ResolutionOptionType,
    },
    total=False,
)

class CompositedVideoArtifactsConfigurationTypeDef(
    _RequiredCompositedVideoArtifactsConfigurationTypeDef,
    _OptionalCompositedVideoArtifactsConfigurationTypeDef,
):
    pass

RealTimeAlertConfigurationOutputTypeDef = TypedDict(
    "RealTimeAlertConfigurationOutputTypeDef",
    {
        "Disabled": bool,
        "Rules": List[RealTimeAlertRuleOutputTypeDef],
    },
    total=False,
)

RealTimeAlertConfigurationTypeDef = TypedDict(
    "RealTimeAlertConfigurationTypeDef",
    {
        "Disabled": bool,
        "Rules": Sequence[RealTimeAlertRuleTypeDef],
    },
    total=False,
)

MediaCapturePipelineSourceConfigurationOutputTypeDef = TypedDict(
    "MediaCapturePipelineSourceConfigurationOutputTypeDef",
    {
        "MediaPipelineArn": str,
        "ChimeSdkMeetingConfiguration": ChimeSdkMeetingConcatenationConfigurationOutputTypeDef,
    },
)

MediaCapturePipelineSourceConfigurationTypeDef = TypedDict(
    "MediaCapturePipelineSourceConfigurationTypeDef",
    {
        "MediaPipelineArn": str,
        "ChimeSdkMeetingConfiguration": ChimeSdkMeetingConcatenationConfigurationTypeDef,
    },
)

KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef = TypedDict(
    "KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef",
    {
        "Streams": List[StreamConfigurationOutputTypeDef],
        "MediaEncoding": Literal["pcm"],
        "MediaSampleRate": int,
    },
)

KinesisVideoStreamSourceRuntimeConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
    {
        "Streams": Sequence[StreamConfigurationTypeDef],
        "MediaEncoding": Literal["pcm"],
        "MediaSampleRate": int,
    },
)

_RequiredArtifactsConfigurationOutputTypeDef = TypedDict(
    "_RequiredArtifactsConfigurationOutputTypeDef",
    {
        "Audio": AudioArtifactsConfigurationOutputTypeDef,
        "Video": VideoArtifactsConfigurationOutputTypeDef,
        "Content": ContentArtifactsConfigurationOutputTypeDef,
    },
)
_OptionalArtifactsConfigurationOutputTypeDef = TypedDict(
    "_OptionalArtifactsConfigurationOutputTypeDef",
    {
        "CompositedVideo": CompositedVideoArtifactsConfigurationOutputTypeDef,
    },
    total=False,
)

class ArtifactsConfigurationOutputTypeDef(
    _RequiredArtifactsConfigurationOutputTypeDef, _OptionalArtifactsConfigurationOutputTypeDef
):
    pass

_RequiredChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef = TypedDict(
    "_RequiredChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef",
    {
        "Arn": str,
        "MuxType": LiveConnectorMuxTypeType,
    },
)
_OptionalChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef = TypedDict(
    "_OptionalChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef",
    {
        "CompositedVideo": CompositedVideoArtifactsConfigurationOutputTypeDef,
        "SourceConfiguration": SourceConfigurationOutputTypeDef,
    },
    total=False,
)

class ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef(
    _RequiredChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef,
    _OptionalChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef,
):
    pass

_RequiredArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredArtifactsConfigurationTypeDef",
    {
        "Audio": AudioArtifactsConfigurationTypeDef,
        "Video": VideoArtifactsConfigurationTypeDef,
        "Content": ContentArtifactsConfigurationTypeDef,
    },
)
_OptionalArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalArtifactsConfigurationTypeDef",
    {
        "CompositedVideo": CompositedVideoArtifactsConfigurationTypeDef,
    },
    total=False,
)

class ArtifactsConfigurationTypeDef(
    _RequiredArtifactsConfigurationTypeDef, _OptionalArtifactsConfigurationTypeDef
):
    pass

_RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef = TypedDict(
    "_RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    {
        "Arn": str,
        "MuxType": LiveConnectorMuxTypeType,
    },
)
_OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef = TypedDict(
    "_OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    {
        "CompositedVideo": CompositedVideoArtifactsConfigurationTypeDef,
        "SourceConfiguration": SourceConfigurationTypeDef,
    },
    total=False,
)

class ChimeSdkMeetingLiveConnectorConfigurationTypeDef(
    _RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef,
    _OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef,
):
    pass

MediaInsightsPipelineConfigurationTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "MediaInsightsPipelineConfigurationArn": str,
        "ResourceAccessRoleArn": str,
        "RealTimeAlertConfiguration": RealTimeAlertConfigurationOutputTypeDef,
        "Elements": List[MediaInsightsPipelineConfigurationElementOutputTypeDef],
        "MediaInsightsPipelineConfigurationId": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "ResourceAccessRoleArn": str,
        "Elements": Sequence[MediaInsightsPipelineConfigurationElementTypeDef],
    },
)
_OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "RealTimeAlertConfiguration": RealTimeAlertConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef(
    _RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
    _OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "ResourceAccessRoleArn": str,
        "Elements": Sequence[MediaInsightsPipelineConfigurationElementTypeDef],
    },
)
_OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "RealTimeAlertConfiguration": RealTimeAlertConfigurationTypeDef,
    },
    total=False,
)

class UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef(
    _RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
    _OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
):
    pass

ConcatenationSourceOutputTypeDef = TypedDict(
    "ConcatenationSourceOutputTypeDef",
    {
        "Type": Literal["MediaCapturePipeline"],
        "MediaCapturePipelineSourceConfiguration": (
            MediaCapturePipelineSourceConfigurationOutputTypeDef
        ),
    },
)

ConcatenationSourceTypeDef = TypedDict(
    "ConcatenationSourceTypeDef",
    {
        "Type": Literal["MediaCapturePipeline"],
        "MediaCapturePipelineSourceConfiguration": MediaCapturePipelineSourceConfigurationTypeDef,
    },
)

MediaInsightsPipelineTypeDef = TypedDict(
    "MediaInsightsPipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "MediaInsightsPipelineConfigurationArn": str,
        "Status": MediaPipelineStatusType,
        "KinesisVideoStreamSourceRuntimeConfiguration": (
            KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef
        ),
        "MediaInsightsRuntimeMetadata": Dict[str, str],
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration": (
            KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef
        ),
        "S3RecordingSinkRuntimeConfiguration": S3RecordingSinkRuntimeConfigurationOutputTypeDef,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

_RequiredCreateMediaInsightsPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaInsightsPipelineRequestRequestTypeDef",
    {
        "MediaInsightsPipelineConfigurationArn": str,
    },
)
_OptionalCreateMediaInsightsPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaInsightsPipelineRequestRequestTypeDef",
    {
        "KinesisVideoStreamSourceRuntimeConfiguration": (
            KinesisVideoStreamSourceRuntimeConfigurationTypeDef
        ),
        "MediaInsightsRuntimeMetadata": Mapping[str, str],
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration": (
            KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef
        ),
        "S3RecordingSinkRuntimeConfiguration": S3RecordingSinkRuntimeConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateMediaInsightsPipelineRequestRequestTypeDef(
    _RequiredCreateMediaInsightsPipelineRequestRequestTypeDef,
    _OptionalCreateMediaInsightsPipelineRequestRequestTypeDef,
):
    pass

ChimeSdkMeetingConfigurationOutputTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationOutputTypeDef",
    {
        "SourceConfiguration": SourceConfigurationOutputTypeDef,
        "ArtifactsConfiguration": ArtifactsConfigurationOutputTypeDef,
    },
    total=False,
)

LiveConnectorSourceConfigurationOutputTypeDef = TypedDict(
    "LiveConnectorSourceConfigurationOutputTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "ChimeSdkMeetingLiveConnectorConfiguration": (
            ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef
        ),
    },
)

ChimeSdkMeetingConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationTypeDef",
    {
        "SourceConfiguration": SourceConfigurationTypeDef,
        "ArtifactsConfiguration": ArtifactsConfigurationTypeDef,
    },
    total=False,
)

LiveConnectorSourceConfigurationTypeDef = TypedDict(
    "LiveConnectorSourceConfigurationTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "ChimeSdkMeetingLiveConnectorConfiguration": (
            ChimeSdkMeetingLiveConnectorConfigurationTypeDef
        ),
    },
)

CreateMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "GetMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaConcatenationPipelineTypeDef = TypedDict(
    "MediaConcatenationPipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "Sources": List[ConcatenationSourceOutputTypeDef],
        "Sinks": List[ConcatenationSinkOutputTypeDef],
        "Status": MediaPipelineStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef",
    {
        "Sources": Sequence[ConcatenationSourceTypeDef],
        "Sinks": Sequence[ConcatenationSinkTypeDef],
    },
)
_OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateMediaConcatenationPipelineRequestRequestTypeDef(
    _RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef,
    _OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef,
):
    pass

CreateMediaInsightsPipelineResponseTypeDef = TypedDict(
    "CreateMediaInsightsPipelineResponseTypeDef",
    {
        "MediaInsightsPipeline": MediaInsightsPipelineTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaCapturePipelineTypeDef = TypedDict(
    "MediaCapturePipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "Status": MediaPipelineStatusType,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ChimeSdkMeetingConfiguration": ChimeSdkMeetingConfigurationOutputTypeDef,
    },
    total=False,
)

MediaLiveConnectorPipelineTypeDef = TypedDict(
    "MediaLiveConnectorPipelineTypeDef",
    {
        "Sources": List[LiveConnectorSourceConfigurationOutputTypeDef],
        "Sinks": List[LiveConnectorSinkConfigurationOutputTypeDef],
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "Status": MediaPipelineStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredCreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
    },
)
_OptionalCreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ChimeSdkMeetingConfiguration": ChimeSdkMeetingConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateMediaCapturePipelineRequestRequestTypeDef(
    _RequiredCreateMediaCapturePipelineRequestRequestTypeDef,
    _OptionalCreateMediaCapturePipelineRequestRequestTypeDef,
):
    pass

_RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    {
        "Sources": Sequence[LiveConnectorSourceConfigurationTypeDef],
        "Sinks": Sequence[LiveConnectorSinkConfigurationTypeDef],
    },
)
_OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateMediaLiveConnectorPipelineRequestRequestTypeDef(
    _RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef,
    _OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef,
):
    pass

CreateMediaConcatenationPipelineResponseTypeDef = TypedDict(
    "CreateMediaConcatenationPipelineResponseTypeDef",
    {
        "MediaConcatenationPipeline": MediaConcatenationPipelineTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMediaCapturePipelineResponseTypeDef = TypedDict(
    "CreateMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMediaCapturePipelineResponseTypeDef = TypedDict(
    "GetMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMediaLiveConnectorPipelineResponseTypeDef = TypedDict(
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    {
        "MediaLiveConnectorPipeline": MediaLiveConnectorPipelineTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaPipelineTypeDef = TypedDict(
    "MediaPipelineTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "MediaLiveConnectorPipeline": MediaLiveConnectorPipelineTypeDef,
        "MediaConcatenationPipeline": MediaConcatenationPipelineTypeDef,
        "MediaInsightsPipeline": MediaInsightsPipelineTypeDef,
    },
    total=False,
)

GetMediaPipelineResponseTypeDef = TypedDict(
    "GetMediaPipelineResponseTypeDef",
    {
        "MediaPipeline": MediaPipelineTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
