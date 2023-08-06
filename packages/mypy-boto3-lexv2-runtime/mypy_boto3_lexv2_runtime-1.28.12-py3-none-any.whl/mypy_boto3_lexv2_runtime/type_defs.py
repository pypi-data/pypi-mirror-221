"""
Type annotations for lexv2-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_lexv2_runtime.type_defs import ActiveContextOutputTypeDef

    data: ActiveContextOutputTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ConfirmationStateType,
    DialogActionTypeType,
    IntentStateType,
    MessageContentTypeType,
    SentimentTypeType,
    ShapeType,
    StyleTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveContextOutputTypeDef",
    "ActiveContextTimeToLiveOutputTypeDef",
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ButtonOutputTypeDef",
    "ButtonTypeDef",
    "ConfidenceScoreTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "DeleteSessionResponseTypeDef",
    "DialogActionOutputTypeDef",
    "DialogActionTypeDef",
    "ElicitSubSlotOutputTypeDef",
    "ElicitSubSlotTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "ImageResponseCardOutputTypeDef",
    "ImageResponseCardTypeDef",
    "IntentOutputTypeDef",
    "IntentTypeDef",
    "InterpretationTypeDef",
    "MessageOutputTypeDef",
    "MessageTypeDef",
    "PutSessionRequestRequestTypeDef",
    "PutSessionResponseTypeDef",
    "RecognizeTextRequestRequestTypeDef",
    "RecognizeTextResponseTypeDef",
    "RecognizeUtteranceRequestRequestTypeDef",
    "RecognizeUtteranceResponseTypeDef",
    "RecognizedBotMemberTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeHintDetailsOutputTypeDef",
    "RuntimeHintDetailsTypeDef",
    "RuntimeHintValueOutputTypeDef",
    "RuntimeHintValueTypeDef",
    "RuntimeHintsOutputTypeDef",
    "RuntimeHintsTypeDef",
    "SentimentResponseTypeDef",
    "SentimentScoreTypeDef",
    "SessionStateOutputTypeDef",
    "SessionStateTypeDef",
    "SlotOutputTypeDef",
    "SlotTypeDef",
    "ValueOutputTypeDef",
    "ValueTypeDef",
)

ActiveContextOutputTypeDef = TypedDict(
    "ActiveContextOutputTypeDef",
    {
        "name": str,
        "timeToLive": "ActiveContextTimeToLiveOutputTypeDef",
        "contextAttributes": Dict[str, str],
    },
)

ActiveContextTimeToLiveOutputTypeDef = TypedDict(
    "ActiveContextTimeToLiveOutputTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": "ActiveContextTimeToLiveTypeDef",
        "contextAttributes": Mapping[str, str],
    },
)

ButtonOutputTypeDef = TypedDict(
    "ButtonOutputTypeDef",
    {
        "text": str,
        "value": str,
    },
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

ConfidenceScoreTypeDef = TypedDict(
    "ConfidenceScoreTypeDef",
    {
        "score": float,
    },
    total=False,
)

DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
    },
)

DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
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
        "slotToElicit": str,
        "slotElicitationStyle": StyleTypeType,
        "subSlotToElicit": "ElicitSubSlotOutputTypeDef",
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
        "slotToElicit": str,
        "slotElicitationStyle": StyleTypeType,
        "subSlotToElicit": "ElicitSubSlotTypeDef",
    },
    total=False,
)


class DialogActionTypeDef(_RequiredDialogActionTypeDef, _OptionalDialogActionTypeDef):
    pass


_RequiredElicitSubSlotOutputTypeDef = TypedDict(
    "_RequiredElicitSubSlotOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalElicitSubSlotOutputTypeDef = TypedDict(
    "_OptionalElicitSubSlotOutputTypeDef",
    {
        "subSlotToElicit": Dict[str, Any],
    },
    total=False,
)


class ElicitSubSlotOutputTypeDef(
    _RequiredElicitSubSlotOutputTypeDef, _OptionalElicitSubSlotOutputTypeDef
):
    pass


_RequiredElicitSubSlotTypeDef = TypedDict(
    "_RequiredElicitSubSlotTypeDef",
    {
        "name": str,
    },
)
_OptionalElicitSubSlotTypeDef = TypedDict(
    "_OptionalElicitSubSlotTypeDef",
    {
        "subSlotToElicit": Dict[str, Any],
    },
    total=False,
)


class ElicitSubSlotTypeDef(_RequiredElicitSubSlotTypeDef, _OptionalElicitSubSlotTypeDef):
    pass


GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
    },
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "sessionId": str,
        "messages": List["MessageOutputTypeDef"],
        "interpretations": List["InterpretationTypeDef"],
        "sessionState": "SessionStateOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImageResponseCardOutputTypeDef = TypedDict(
    "_RequiredImageResponseCardOutputTypeDef",
    {
        "title": str,
    },
)
_OptionalImageResponseCardOutputTypeDef = TypedDict(
    "_OptionalImageResponseCardOutputTypeDef",
    {
        "subtitle": str,
        "imageUrl": str,
        "buttons": List["ButtonOutputTypeDef"],
    },
    total=False,
)


class ImageResponseCardOutputTypeDef(
    _RequiredImageResponseCardOutputTypeDef, _OptionalImageResponseCardOutputTypeDef
):
    pass


_RequiredImageResponseCardTypeDef = TypedDict(
    "_RequiredImageResponseCardTypeDef",
    {
        "title": str,
    },
)
_OptionalImageResponseCardTypeDef = TypedDict(
    "_OptionalImageResponseCardTypeDef",
    {
        "subtitle": str,
        "imageUrl": str,
        "buttons": Sequence["ButtonTypeDef"],
    },
    total=False,
)


class ImageResponseCardTypeDef(
    _RequiredImageResponseCardTypeDef, _OptionalImageResponseCardTypeDef
):
    pass


_RequiredIntentOutputTypeDef = TypedDict(
    "_RequiredIntentOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalIntentOutputTypeDef = TypedDict(
    "_OptionalIntentOutputTypeDef",
    {
        "slots": Dict[str, "SlotOutputTypeDef"],
        "state": IntentStateType,
        "confirmationState": ConfirmationStateType,
    },
    total=False,
)


class IntentOutputTypeDef(_RequiredIntentOutputTypeDef, _OptionalIntentOutputTypeDef):
    pass


_RequiredIntentTypeDef = TypedDict(
    "_RequiredIntentTypeDef",
    {
        "name": str,
    },
)
_OptionalIntentTypeDef = TypedDict(
    "_OptionalIntentTypeDef",
    {
        "slots": Mapping[str, "SlotTypeDef"],
        "state": IntentStateType,
        "confirmationState": ConfirmationStateType,
    },
    total=False,
)


class IntentTypeDef(_RequiredIntentTypeDef, _OptionalIntentTypeDef):
    pass


InterpretationTypeDef = TypedDict(
    "InterpretationTypeDef",
    {
        "nluConfidence": "ConfidenceScoreTypeDef",
        "sentimentResponse": "SentimentResponseTypeDef",
        "intent": "IntentOutputTypeDef",
    },
    total=False,
)

_RequiredMessageOutputTypeDef = TypedDict(
    "_RequiredMessageOutputTypeDef",
    {
        "contentType": MessageContentTypeType,
    },
)
_OptionalMessageOutputTypeDef = TypedDict(
    "_OptionalMessageOutputTypeDef",
    {
        "content": str,
        "imageResponseCard": "ImageResponseCardOutputTypeDef",
    },
    total=False,
)


class MessageOutputTypeDef(_RequiredMessageOutputTypeDef, _OptionalMessageOutputTypeDef):
    pass


_RequiredMessageTypeDef = TypedDict(
    "_RequiredMessageTypeDef",
    {
        "contentType": MessageContentTypeType,
    },
)
_OptionalMessageTypeDef = TypedDict(
    "_OptionalMessageTypeDef",
    {
        "content": str,
        "imageResponseCard": "ImageResponseCardTypeDef",
    },
    total=False,
)


class MessageTypeDef(_RequiredMessageTypeDef, _OptionalMessageTypeDef):
    pass


_RequiredPutSessionRequestRequestTypeDef = TypedDict(
    "_RequiredPutSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "sessionState": "SessionStateTypeDef",
    },
)
_OptionalPutSessionRequestRequestTypeDef = TypedDict(
    "_OptionalPutSessionRequestRequestTypeDef",
    {
        "messages": Sequence["MessageTypeDef"],
        "requestAttributes": Mapping[str, str],
        "responseContentType": str,
    },
    total=False,
)


class PutSessionRequestRequestTypeDef(
    _RequiredPutSessionRequestRequestTypeDef, _OptionalPutSessionRequestRequestTypeDef
):
    pass


PutSessionResponseTypeDef = TypedDict(
    "PutSessionResponseTypeDef",
    {
        "contentType": str,
        "messages": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "audioStream": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecognizeTextRequestRequestTypeDef = TypedDict(
    "_RequiredRecognizeTextRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "text": str,
    },
)
_OptionalRecognizeTextRequestRequestTypeDef = TypedDict(
    "_OptionalRecognizeTextRequestRequestTypeDef",
    {
        "sessionState": "SessionStateTypeDef",
        "requestAttributes": Mapping[str, str],
    },
    total=False,
)


class RecognizeTextRequestRequestTypeDef(
    _RequiredRecognizeTextRequestRequestTypeDef, _OptionalRecognizeTextRequestRequestTypeDef
):
    pass


RecognizeTextResponseTypeDef = TypedDict(
    "RecognizeTextResponseTypeDef",
    {
        "messages": List["MessageOutputTypeDef"],
        "sessionState": "SessionStateOutputTypeDef",
        "interpretations": List["InterpretationTypeDef"],
        "requestAttributes": Dict[str, str],
        "sessionId": str,
        "recognizedBotMember": "RecognizedBotMemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecognizeUtteranceRequestRequestTypeDef = TypedDict(
    "_RequiredRecognizeUtteranceRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "requestContentType": str,
    },
)
_OptionalRecognizeUtteranceRequestRequestTypeDef = TypedDict(
    "_OptionalRecognizeUtteranceRequestRequestTypeDef",
    {
        "sessionState": str,
        "requestAttributes": str,
        "responseContentType": str,
        "inputStream": Union[str, bytes, IO[Any], StreamingBody],
    },
    total=False,
)


class RecognizeUtteranceRequestRequestTypeDef(
    _RequiredRecognizeUtteranceRequestRequestTypeDef,
    _OptionalRecognizeUtteranceRequestRequestTypeDef,
):
    pass


RecognizeUtteranceResponseTypeDef = TypedDict(
    "RecognizeUtteranceResponseTypeDef",
    {
        "inputMode": str,
        "contentType": str,
        "messages": str,
        "interpretations": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "inputTranscript": str,
        "audioStream": StreamingBody,
        "recognizedBotMember": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecognizedBotMemberTypeDef = TypedDict(
    "_RequiredRecognizedBotMemberTypeDef",
    {
        "botId": str,
    },
)
_OptionalRecognizedBotMemberTypeDef = TypedDict(
    "_OptionalRecognizedBotMemberTypeDef",
    {
        "botName": str,
    },
    total=False,
)


class RecognizedBotMemberTypeDef(
    _RequiredRecognizedBotMemberTypeDef, _OptionalRecognizedBotMemberTypeDef
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

RuntimeHintDetailsOutputTypeDef = TypedDict(
    "RuntimeHintDetailsOutputTypeDef",
    {
        "runtimeHintValues": List["RuntimeHintValueOutputTypeDef"],
        "subSlotHints": Dict[str, Dict[str, Any]],
    },
    total=False,
)

RuntimeHintDetailsTypeDef = TypedDict(
    "RuntimeHintDetailsTypeDef",
    {
        "runtimeHintValues": Sequence["RuntimeHintValueTypeDef"],
        "subSlotHints": Mapping[str, Dict[str, Any]],
    },
    total=False,
)

RuntimeHintValueOutputTypeDef = TypedDict(
    "RuntimeHintValueOutputTypeDef",
    {
        "phrase": str,
    },
)

RuntimeHintValueTypeDef = TypedDict(
    "RuntimeHintValueTypeDef",
    {
        "phrase": str,
    },
)

RuntimeHintsOutputTypeDef = TypedDict(
    "RuntimeHintsOutputTypeDef",
    {
        "slotHints": Dict[str, Dict[str, "RuntimeHintDetailsOutputTypeDef"]],
    },
    total=False,
)

RuntimeHintsTypeDef = TypedDict(
    "RuntimeHintsTypeDef",
    {
        "slotHints": Mapping[str, Mapping[str, "RuntimeHintDetailsTypeDef"]],
    },
    total=False,
)

SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentiment": SentimentTypeType,
        "sentimentScore": "SentimentScoreTypeDef",
    },
    total=False,
)

SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "positive": float,
        "negative": float,
        "neutral": float,
        "mixed": float,
    },
    total=False,
)

SessionStateOutputTypeDef = TypedDict(
    "SessionStateOutputTypeDef",
    {
        "dialogAction": "DialogActionOutputTypeDef",
        "intent": "IntentOutputTypeDef",
        "activeContexts": List["ActiveContextOutputTypeDef"],
        "sessionAttributes": Dict[str, str],
        "originatingRequestId": str,
        "runtimeHints": "RuntimeHintsOutputTypeDef",
    },
    total=False,
)

SessionStateTypeDef = TypedDict(
    "SessionStateTypeDef",
    {
        "dialogAction": "DialogActionTypeDef",
        "intent": "IntentTypeDef",
        "activeContexts": Sequence["ActiveContextTypeDef"],
        "sessionAttributes": Mapping[str, str],
        "originatingRequestId": str,
        "runtimeHints": "RuntimeHintsTypeDef",
    },
    total=False,
)

SlotOutputTypeDef = TypedDict(
    "SlotOutputTypeDef",
    {
        "value": "ValueOutputTypeDef",
        "shape": ShapeType,
        "values": List[Dict[str, Any]],
        "subSlots": Dict[str, Dict[str, Any]],
    },
    total=False,
)

SlotTypeDef = TypedDict(
    "SlotTypeDef",
    {
        "value": "ValueTypeDef",
        "shape": ShapeType,
        "values": Sequence[Dict[str, Any]],
        "subSlots": Mapping[str, Dict[str, Any]],
    },
    total=False,
)

_RequiredValueOutputTypeDef = TypedDict(
    "_RequiredValueOutputTypeDef",
    {
        "interpretedValue": str,
    },
)
_OptionalValueOutputTypeDef = TypedDict(
    "_OptionalValueOutputTypeDef",
    {
        "originalValue": str,
        "resolvedValues": List[str],
    },
    total=False,
)


class ValueOutputTypeDef(_RequiredValueOutputTypeDef, _OptionalValueOutputTypeDef):
    pass


_RequiredValueTypeDef = TypedDict(
    "_RequiredValueTypeDef",
    {
        "interpretedValue": str,
    },
)
_OptionalValueTypeDef = TypedDict(
    "_OptionalValueTypeDef",
    {
        "originalValue": str,
        "resolvedValues": Sequence[str],
    },
    total=False,
)


class ValueTypeDef(_RequiredValueTypeDef, _OptionalValueTypeDef):
    pass
