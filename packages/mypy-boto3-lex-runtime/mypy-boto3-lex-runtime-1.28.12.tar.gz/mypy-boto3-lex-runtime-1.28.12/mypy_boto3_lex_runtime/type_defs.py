"""
Type annotations for lex-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_lex_runtime.type_defs import ActiveContextTimeToLiveOutputTypeDef

    data: ActiveContextTimeToLiveOutputTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ConfirmationStatusType,
    DialogActionTypeType,
    DialogStateType,
    FulfillmentStateType,
    MessageFormatTypeType,
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
    "ActiveContextTimeToLiveOutputTypeDef",
    "ActiveContextTimeToLiveTypeDef",
    "ButtonTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "DeleteSessionResponseTypeDef",
    "DialogActionOutputTypeDef",
    "DialogActionTypeDef",
    "GetSessionRequestRequestTypeDef",
    "IntentSummaryOutputTypeDef",
    "IntentConfidenceTypeDef",
    "IntentSummaryTypeDef",
    "PostContentRequestRequestTypeDef",
    "PostContentResponseTypeDef",
    "SentimentResponseTypeDef",
    "PutSessionResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ActiveContextOutputTypeDef",
    "ActiveContextTypeDef",
    "GenericAttachmentTypeDef",
    "PredictedIntentTypeDef",
    "GetSessionResponseTypeDef",
    "PostTextRequestRequestTypeDef",
    "PutSessionRequestRequestTypeDef",
    "ResponseCardTypeDef",
    "PostTextResponseTypeDef",
)

ActiveContextTimeToLiveOutputTypeDef = TypedDict(
    "ActiveContextTimeToLiveOutputTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
    total=False,
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
    total=False,
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
    },
)

DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDialogActionOutputTypeDef = TypedDict(
    "_RequiredDialogActionOutputTypeDef",
    {
        "type": DialogActionTypeType,
    },
)
_OptionalDialogActionOutputTypeDef = TypedDict(
    "_OptionalDialogActionOutputTypeDef",
    {
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": FulfillmentStateType,
        "message": str,
        "messageFormat": MessageFormatTypeType,
    },
    total=False,
)


class DialogActionOutputTypeDef(
    _RequiredDialogActionOutputTypeDef, _OptionalDialogActionOutputTypeDef
):
    pass


_RequiredDialogActionTypeDef = TypedDict(
    "_RequiredDialogActionTypeDef",
    {
        "type": DialogActionTypeType,
    },
)
_OptionalDialogActionTypeDef = TypedDict(
    "_OptionalDialogActionTypeDef",
    {
        "intentName": str,
        "slots": Mapping[str, str],
        "slotToElicit": str,
        "fulfillmentState": FulfillmentStateType,
        "message": str,
        "messageFormat": MessageFormatTypeType,
    },
    total=False,
)


class DialogActionTypeDef(_RequiredDialogActionTypeDef, _OptionalDialogActionTypeDef):
    pass


_RequiredGetSessionRequestRequestTypeDef = TypedDict(
    "_RequiredGetSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
    },
)
_OptionalGetSessionRequestRequestTypeDef = TypedDict(
    "_OptionalGetSessionRequestRequestTypeDef",
    {
        "checkpointLabelFilter": str,
    },
    total=False,
)


class GetSessionRequestRequestTypeDef(
    _RequiredGetSessionRequestRequestTypeDef, _OptionalGetSessionRequestRequestTypeDef
):
    pass


_RequiredIntentSummaryOutputTypeDef = TypedDict(
    "_RequiredIntentSummaryOutputTypeDef",
    {
        "dialogActionType": DialogActionTypeType,
    },
)
_OptionalIntentSummaryOutputTypeDef = TypedDict(
    "_OptionalIntentSummaryOutputTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Dict[str, str],
        "confirmationStatus": ConfirmationStatusType,
        "fulfillmentState": FulfillmentStateType,
        "slotToElicit": str,
    },
    total=False,
)


class IntentSummaryOutputTypeDef(
    _RequiredIntentSummaryOutputTypeDef, _OptionalIntentSummaryOutputTypeDef
):
    pass


IntentConfidenceTypeDef = TypedDict(
    "IntentConfidenceTypeDef",
    {
        "score": float,
    },
    total=False,
)

_RequiredIntentSummaryTypeDef = TypedDict(
    "_RequiredIntentSummaryTypeDef",
    {
        "dialogActionType": DialogActionTypeType,
    },
)
_OptionalIntentSummaryTypeDef = TypedDict(
    "_OptionalIntentSummaryTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Mapping[str, str],
        "confirmationStatus": ConfirmationStatusType,
        "fulfillmentState": FulfillmentStateType,
        "slotToElicit": str,
    },
    total=False,
)


class IntentSummaryTypeDef(_RequiredIntentSummaryTypeDef, _OptionalIntentSummaryTypeDef):
    pass


_RequiredPostContentRequestRequestTypeDef = TypedDict(
    "_RequiredPostContentRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "contentType": str,
        "inputStream": Union[str, bytes, IO[Any], StreamingBody],
    },
)
_OptionalPostContentRequestRequestTypeDef = TypedDict(
    "_OptionalPostContentRequestRequestTypeDef",
    {
        "sessionAttributes": str,
        "requestAttributes": str,
        "accept": str,
        "activeContexts": str,
    },
    total=False,
)


class PostContentRequestRequestTypeDef(
    _RequiredPostContentRequestRequestTypeDef, _OptionalPostContentRequestRequestTypeDef
):
    pass


PostContentResponseTypeDef = TypedDict(
    "PostContentResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "nluIntentConfidence": str,
        "alternativeIntents": str,
        "slots": str,
        "sessionAttributes": str,
        "sentimentResponse": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "inputTranscript": str,
        "encodedInputTranscript": str,
        "audioStream": StreamingBody,
        "botVersion": str,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentimentLabel": str,
        "sentimentScore": str,
    },
    total=False,
)

PutSessionResponseTypeDef = TypedDict(
    "PutSessionResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "slots": str,
        "sessionAttributes": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "audioStream": StreamingBody,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ActiveContextOutputTypeDef = TypedDict(
    "ActiveContextOutputTypeDef",
    {
        "name": str,
        "timeToLive": ActiveContextTimeToLiveOutputTypeDef,
        "parameters": Dict[str, str],
    },
)

ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": ActiveContextTimeToLiveTypeDef,
        "parameters": Mapping[str, str],
    },
)

GenericAttachmentTypeDef = TypedDict(
    "GenericAttachmentTypeDef",
    {
        "title": str,
        "subTitle": str,
        "attachmentLinkUrl": str,
        "imageUrl": str,
        "buttons": List[ButtonTypeDef],
    },
    total=False,
)

PredictedIntentTypeDef = TypedDict(
    "PredictedIntentTypeDef",
    {
        "intentName": str,
        "nluIntentConfidence": IntentConfidenceTypeDef,
        "slots": Dict[str, str],
    },
    total=False,
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "recentIntentSummaryView": List[IntentSummaryOutputTypeDef],
        "sessionAttributes": Dict[str, str],
        "sessionId": str,
        "dialogAction": DialogActionOutputTypeDef,
        "activeContexts": List[ActiveContextOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPostTextRequestRequestTypeDef = TypedDict(
    "_RequiredPostTextRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "inputText": str,
    },
)
_OptionalPostTextRequestRequestTypeDef = TypedDict(
    "_OptionalPostTextRequestRequestTypeDef",
    {
        "sessionAttributes": Mapping[str, str],
        "requestAttributes": Mapping[str, str],
        "activeContexts": Sequence[ActiveContextTypeDef],
    },
    total=False,
)


class PostTextRequestRequestTypeDef(
    _RequiredPostTextRequestRequestTypeDef, _OptionalPostTextRequestRequestTypeDef
):
    pass


_RequiredPutSessionRequestRequestTypeDef = TypedDict(
    "_RequiredPutSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
    },
)
_OptionalPutSessionRequestRequestTypeDef = TypedDict(
    "_OptionalPutSessionRequestRequestTypeDef",
    {
        "sessionAttributes": Mapping[str, str],
        "dialogAction": DialogActionTypeDef,
        "recentIntentSummaryView": Sequence[IntentSummaryTypeDef],
        "accept": str,
        "activeContexts": Sequence[ActiveContextTypeDef],
    },
    total=False,
)


class PutSessionRequestRequestTypeDef(
    _RequiredPutSessionRequestRequestTypeDef, _OptionalPutSessionRequestRequestTypeDef
):
    pass


ResponseCardTypeDef = TypedDict(
    "ResponseCardTypeDef",
    {
        "version": str,
        "contentType": Literal["application/vnd.amazonaws.card.generic"],
        "genericAttachments": List[GenericAttachmentTypeDef],
    },
    total=False,
)

PostTextResponseTypeDef = TypedDict(
    "PostTextResponseTypeDef",
    {
        "intentName": str,
        "nluIntentConfidence": IntentConfidenceTypeDef,
        "alternativeIntents": List[PredictedIntentTypeDef],
        "slots": Dict[str, str],
        "sessionAttributes": Dict[str, str],
        "message": str,
        "sentimentResponse": SentimentResponseTypeDef,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "responseCard": ResponseCardTypeDef,
        "sessionId": str,
        "botVersion": str,
        "activeContexts": List[ActiveContextOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
