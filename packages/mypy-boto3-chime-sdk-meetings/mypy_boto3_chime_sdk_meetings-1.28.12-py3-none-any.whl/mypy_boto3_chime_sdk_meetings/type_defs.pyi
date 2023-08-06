"""
Type annotations for chime-sdk-meetings service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_meetings.type_defs import AttendeeCapabilitiesOutputTypeDef

    data: AttendeeCapabilitiesOutputTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from .literals import (
    MediaCapabilitiesType,
    MeetingFeatureStatusType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribePartialResultsStabilityType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
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
    "AttendeeCapabilitiesOutputTypeDef",
    "AttendeeCapabilitiesTypeDef",
    "AttendeeIdItemTypeDef",
    "AudioFeaturesOutputTypeDef",
    "AudioFeaturesTypeDef",
    "CreateAttendeeErrorTypeDef",
    "NotificationsConfigurationTypeDef",
    "TagTypeDef",
    "DeleteAttendeeRequestRequestTypeDef",
    "DeleteMeetingRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "GetAttendeeRequestRequestTypeDef",
    "GetMeetingRequestRequestTypeDef",
    "ListAttendeesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "MediaPlacementTypeDef",
    "ResponseMetadataTypeDef",
    "StopMeetingTranscriptionRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AttendeeTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestRequestTypeDef",
    "UpdateAttendeeCapabilitiesRequestRequestTypeDef",
    "BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef",
    "MeetingFeaturesConfigurationOutputTypeDef",
    "MeetingFeaturesConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TranscriptionConfigurationTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "CreateAttendeeResponseTypeDef",
    "GetAttendeeResponseTypeDef",
    "ListAttendeesResponseTypeDef",
    "UpdateAttendeeCapabilitiesResponseTypeDef",
    "BatchCreateAttendeeRequestRequestTypeDef",
    "MeetingTypeDef",
    "CreateMeetingRequestRequestTypeDef",
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    "StartMeetingTranscriptionRequestRequestTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "GetMeetingResponseTypeDef",
)

AttendeeCapabilitiesOutputTypeDef = TypedDict(
    "AttendeeCapabilitiesOutputTypeDef",
    {
        "Audio": MediaCapabilitiesType,
        "Video": MediaCapabilitiesType,
        "Content": MediaCapabilitiesType,
    },
)

AttendeeCapabilitiesTypeDef = TypedDict(
    "AttendeeCapabilitiesTypeDef",
    {
        "Audio": MediaCapabilitiesType,
        "Video": MediaCapabilitiesType,
        "Content": MediaCapabilitiesType,
    },
)

AttendeeIdItemTypeDef = TypedDict(
    "AttendeeIdItemTypeDef",
    {
        "AttendeeId": str,
    },
)

AudioFeaturesOutputTypeDef = TypedDict(
    "AudioFeaturesOutputTypeDef",
    {
        "EchoReduction": MeetingFeatureStatusType,
    },
    total=False,
)

AudioFeaturesTypeDef = TypedDict(
    "AudioFeaturesTypeDef",
    {
        "EchoReduction": MeetingFeatureStatusType,
    },
    total=False,
)

CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {
        "ExternalUserId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

NotificationsConfigurationTypeDef = TypedDict(
    "NotificationsConfigurationTypeDef",
    {
        "LambdaFunctionArn": str,
        "SnsTopicArn": str,
        "SqsQueueArn": str,
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

DeleteAttendeeRequestRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

DeleteMeetingRequestRequestTypeDef = TypedDict(
    "DeleteMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "_RequiredEngineTranscribeMedicalSettingsTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "Specialty": TranscribeMedicalSpecialtyType,
        "Type": TranscribeMedicalTypeType,
    },
)
_OptionalEngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "_OptionalEngineTranscribeMedicalSettingsTypeDef",
    {
        "VocabularyName": str,
        "Region": TranscribeMedicalRegionType,
        "ContentIdentificationType": Literal["PHI"],
    },
    total=False,
)

class EngineTranscribeMedicalSettingsTypeDef(
    _RequiredEngineTranscribeMedicalSettingsTypeDef, _OptionalEngineTranscribeMedicalSettingsTypeDef
):
    pass

EngineTranscribeSettingsTypeDef = TypedDict(
    "EngineTranscribeSettingsTypeDef",
    {
        "LanguageCode": TranscribeLanguageCodeType,
        "VocabularyFilterMethod": TranscribeVocabularyFilterMethodType,
        "VocabularyFilterName": str,
        "VocabularyName": str,
        "Region": TranscribeRegionType,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": TranscribePartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "LanguageModelName": str,
        "IdentifyLanguage": bool,
        "LanguageOptions": str,
        "PreferredLanguage": TranscribeLanguageCodeType,
        "VocabularyNames": str,
        "VocabularyFilterNames": str,
    },
    total=False,
)

GetAttendeeRequestRequestTypeDef = TypedDict(
    "GetAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

GetMeetingRequestRequestTypeDef = TypedDict(
    "GetMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

_RequiredListAttendeesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttendeesRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
_OptionalListAttendeesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttendeesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAttendeesRequestRequestTypeDef(
    _RequiredListAttendeesRequestRequestTypeDef, _OptionalListAttendeesRequestRequestTypeDef
):
    pass

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

MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "AudioFallbackUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
        "ScreenDataUrl": str,
        "ScreenViewingUrl": str,
        "ScreenSharingUrl": str,
        "EventIngestionUrl": str,
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

StopMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StopMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": str,
        "AttendeeId": str,
        "JoinToken": str,
        "Capabilities": AttendeeCapabilitiesOutputTypeDef,
    },
    total=False,
)

_RequiredCreateAttendeeRequestItemTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestItemTypeDef",
    {
        "ExternalUserId": str,
    },
)
_OptionalCreateAttendeeRequestItemTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestItemTypeDef",
    {
        "Capabilities": AttendeeCapabilitiesTypeDef,
    },
    total=False,
)

class CreateAttendeeRequestItemTypeDef(
    _RequiredCreateAttendeeRequestItemTypeDef, _OptionalCreateAttendeeRequestItemTypeDef
):
    pass

_RequiredCreateAttendeeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
    },
)
_OptionalCreateAttendeeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestRequestTypeDef",
    {
        "Capabilities": AttendeeCapabilitiesTypeDef,
    },
    total=False,
)

class CreateAttendeeRequestRequestTypeDef(
    _RequiredCreateAttendeeRequestRequestTypeDef, _OptionalCreateAttendeeRequestRequestTypeDef
):
    pass

UpdateAttendeeCapabilitiesRequestRequestTypeDef = TypedDict(
    "UpdateAttendeeCapabilitiesRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "Capabilities": AttendeeCapabilitiesTypeDef,
    },
)

BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef = TypedDict(
    "BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExcludedAttendeeIds": Sequence[AttendeeIdItemTypeDef],
        "Capabilities": AttendeeCapabilitiesTypeDef,
    },
)

MeetingFeaturesConfigurationOutputTypeDef = TypedDict(
    "MeetingFeaturesConfigurationOutputTypeDef",
    {
        "Audio": AudioFeaturesOutputTypeDef,
    },
    total=False,
)

MeetingFeaturesConfigurationTypeDef = TypedDict(
    "MeetingFeaturesConfigurationTypeDef",
    {
        "Audio": AudioFeaturesTypeDef,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

TranscriptionConfigurationTypeDef = TypedDict(
    "TranscriptionConfigurationTypeDef",
    {
        "EngineTranscribeSettings": EngineTranscribeSettingsTypeDef,
        "EngineTranscribeMedicalSettings": EngineTranscribeMedicalSettingsTypeDef,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateAttendeeResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List[AttendeeTypeDef],
        "Errors": List[CreateAttendeeErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAttendeeResponseTypeDef = TypedDict(
    "GetAttendeeResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttendeesResponseTypeDef = TypedDict(
    "ListAttendeesResponseTypeDef",
    {
        "Attendees": List[AttendeeTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAttendeeCapabilitiesResponseTypeDef = TypedDict(
    "UpdateAttendeeCapabilitiesResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateAttendeeRequestRequestTypeDef = TypedDict(
    "BatchCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Attendees": Sequence[CreateAttendeeRequestItemTypeDef],
    },
)

MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": str,
        "MeetingHostId": str,
        "ExternalMeetingId": str,
        "MediaRegion": str,
        "MediaPlacement": MediaPlacementTypeDef,
        "MeetingFeatures": MeetingFeaturesConfigurationOutputTypeDef,
        "PrimaryMeetingId": str,
        "TenantIds": List[str],
        "MeetingArn": str,
    },
    total=False,
)

_RequiredCreateMeetingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
    },
)
_OptionalCreateMeetingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingRequestRequestTypeDef",
    {
        "MeetingHostId": str,
        "NotificationsConfiguration": NotificationsConfigurationTypeDef,
        "MeetingFeatures": MeetingFeaturesConfigurationTypeDef,
        "PrimaryMeetingId": str,
        "TenantIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateMeetingRequestRequestTypeDef(
    _RequiredCreateMeetingRequestRequestTypeDef, _OptionalCreateMeetingRequestRequestTypeDef
):
    pass

_RequiredCreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
        "Attendees": Sequence[CreateAttendeeRequestItemTypeDef],
    },
)
_OptionalCreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "MeetingHostId": str,
        "MeetingFeatures": MeetingFeaturesConfigurationTypeDef,
        "NotificationsConfiguration": NotificationsConfigurationTypeDef,
        "PrimaryMeetingId": str,
        "TenantIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateMeetingWithAttendeesRequestRequestTypeDef(
    _RequiredCreateMeetingWithAttendeesRequestRequestTypeDef,
    _OptionalCreateMeetingWithAttendeesRequestRequestTypeDef,
):
    pass

StartMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StartMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TranscriptionConfiguration": TranscriptionConfigurationTypeDef,
    },
)

CreateMeetingResponseTypeDef = TypedDict(
    "CreateMeetingResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMeetingWithAttendeesResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "Attendees": List[AttendeeTypeDef],
        "Errors": List[CreateAttendeeErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMeetingResponseTypeDef = TypedDict(
    "GetMeetingResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
