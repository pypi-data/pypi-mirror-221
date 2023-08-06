"""
Type annotations for lex-models service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_models/type_defs/)

Usage::

    ```python
    from mypy_boto3_lex_models.type_defs import BotChannelAssociationTypeDef

    data: BotChannelAssociationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ChannelStatusType,
    ChannelTypeType,
    ContentTypeType,
    DestinationType,
    ExportStatusType,
    ExportTypeType,
    FulfillmentActivityTypeType,
    ImportStatusType,
    LocaleType,
    LogTypeType,
    MergeStrategyType,
    MigrationAlertTypeType,
    MigrationSortAttributeType,
    MigrationStatusType,
    MigrationStrategyType,
    ObfuscationSettingType,
    ProcessBehaviorType,
    ResourceTypeType,
    SlotConstraintType,
    SlotValueSelectionStrategyType,
    SortOrderType,
    StatusType,
    StatusTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BotChannelAssociationTypeDef",
    "BotMetadataTypeDef",
    "BuiltinIntentMetadataTypeDef",
    "BuiltinIntentSlotTypeDef",
    "BuiltinSlotTypeMetadataTypeDef",
    "CodeHookOutputTypeDef",
    "CodeHookTypeDef",
    "LogSettingsRequestTypeDef",
    "LogSettingsResponseTypeDef",
    "CreateBotVersionRequestRequestTypeDef",
    "IntentOutputTypeDef",
    "CreateIntentVersionRequestRequestTypeDef",
    "InputContextOutputTypeDef",
    "KendraConfigurationOutputTypeDef",
    "OutputContextOutputTypeDef",
    "CreateSlotTypeVersionRequestRequestTypeDef",
    "EnumerationValueOutputTypeDef",
    "DeleteBotAliasRequestRequestTypeDef",
    "DeleteBotChannelAssociationRequestRequestTypeDef",
    "DeleteBotRequestRequestTypeDef",
    "DeleteBotVersionRequestRequestTypeDef",
    "DeleteIntentRequestRequestTypeDef",
    "DeleteIntentVersionRequestRequestTypeDef",
    "DeleteSlotTypeRequestRequestTypeDef",
    "DeleteSlotTypeVersionRequestRequestTypeDef",
    "DeleteUtterancesRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnumerationValueTypeDef",
    "GetBotAliasRequestRequestTypeDef",
    "GetBotAliasesRequestGetBotAliasesPaginateTypeDef",
    "GetBotAliasesRequestRequestTypeDef",
    "GetBotChannelAssociationRequestRequestTypeDef",
    "GetBotChannelAssociationResponseTypeDef",
    "GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef",
    "GetBotChannelAssociationsRequestRequestTypeDef",
    "GetBotRequestRequestTypeDef",
    "GetBotVersionsRequestGetBotVersionsPaginateTypeDef",
    "GetBotVersionsRequestRequestTypeDef",
    "GetBotsRequestGetBotsPaginateTypeDef",
    "GetBotsRequestRequestTypeDef",
    "GetBuiltinIntentRequestRequestTypeDef",
    "GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef",
    "GetBuiltinIntentsRequestRequestTypeDef",
    "GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef",
    "GetBuiltinSlotTypesRequestRequestTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetExportResponseTypeDef",
    "GetImportRequestRequestTypeDef",
    "GetImportResponseTypeDef",
    "GetIntentRequestRequestTypeDef",
    "GetIntentVersionsRequestGetIntentVersionsPaginateTypeDef",
    "GetIntentVersionsRequestRequestTypeDef",
    "IntentMetadataTypeDef",
    "GetIntentsRequestGetIntentsPaginateTypeDef",
    "GetIntentsRequestRequestTypeDef",
    "GetMigrationRequestRequestTypeDef",
    "MigrationAlertTypeDef",
    "GetMigrationsRequestRequestTypeDef",
    "MigrationSummaryTypeDef",
    "GetSlotTypeRequestRequestTypeDef",
    "GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef",
    "GetSlotTypeVersionsRequestRequestTypeDef",
    "SlotTypeMetadataTypeDef",
    "GetSlotTypesRequestGetSlotTypesPaginateTypeDef",
    "GetSlotTypesRequestRequestTypeDef",
    "GetUtterancesViewRequestRequestTypeDef",
    "InputContextTypeDef",
    "IntentTypeDef",
    "KendraConfigurationTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "MessageOutputTypeDef",
    "MessageTypeDef",
    "OutputContextTypeDef",
    "PaginatorConfigTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "SlotDefaultValueOutputTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotTypeRegexConfigurationOutputTypeDef",
    "SlotTypeRegexConfigurationTypeDef",
    "StartMigrationRequestRequestTypeDef",
    "StartMigrationResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UtteranceDataTypeDef",
    "GetBotChannelAssociationsResponseTypeDef",
    "GetBotVersionsResponseTypeDef",
    "GetBotsResponseTypeDef",
    "GetBuiltinIntentsResponseTypeDef",
    "GetBuiltinIntentResponseTypeDef",
    "GetBuiltinSlotTypesResponseTypeDef",
    "FulfillmentActivityOutputTypeDef",
    "FulfillmentActivityTypeDef",
    "ConversationLogsRequestTypeDef",
    "ConversationLogsResponseTypeDef",
    "GetIntentVersionsResponseTypeDef",
    "GetIntentsResponseTypeDef",
    "GetMigrationResponseTypeDef",
    "GetMigrationsResponseTypeDef",
    "GetSlotTypeVersionsResponseTypeDef",
    "GetSlotTypesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartImportResponseTypeDef",
    "PromptOutputTypeDef",
    "StatementOutputTypeDef",
    "PromptTypeDef",
    "StatementTypeDef",
    "StartImportRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "SlotDefaultValueSpecOutputTypeDef",
    "SlotDefaultValueSpecTypeDef",
    "SlotTypeConfigurationOutputTypeDef",
    "SlotTypeConfigurationTypeDef",
    "UtteranceListTypeDef",
    "PutBotAliasRequestRequestTypeDef",
    "BotAliasMetadataTypeDef",
    "GetBotAliasResponseTypeDef",
    "PutBotAliasResponseTypeDef",
    "CreateBotVersionResponseTypeDef",
    "FollowUpPromptOutputTypeDef",
    "GetBotResponseTypeDef",
    "PutBotResponseTypeDef",
    "FollowUpPromptTypeDef",
    "PutBotRequestRequestTypeDef",
    "SlotOutputTypeDef",
    "SlotTypeDef",
    "CreateSlotTypeVersionResponseTypeDef",
    "GetSlotTypeResponseTypeDef",
    "PutSlotTypeResponseTypeDef",
    "PutSlotTypeRequestRequestTypeDef",
    "GetUtterancesViewResponseTypeDef",
    "GetBotAliasesResponseTypeDef",
    "CreateIntentVersionResponseTypeDef",
    "GetIntentResponseTypeDef",
    "PutIntentResponseTypeDef",
    "PutIntentRequestRequestTypeDef",
)

BotChannelAssociationTypeDef = TypedDict(
    "BotChannelAssociationTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelTypeType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatusType,
        "failureReason": str,
    },
    total=False,
)

BotMetadataTypeDef = TypedDict(
    "BotMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "status": StatusType,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

BuiltinIntentMetadataTypeDef = TypedDict(
    "BuiltinIntentMetadataTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
    },
    total=False,
)

BuiltinIntentSlotTypeDef = TypedDict(
    "BuiltinIntentSlotTypeDef",
    {
        "name": str,
    },
    total=False,
)

BuiltinSlotTypeMetadataTypeDef = TypedDict(
    "BuiltinSlotTypeMetadataTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
    },
    total=False,
)

CodeHookOutputTypeDef = TypedDict(
    "CodeHookOutputTypeDef",
    {
        "uri": str,
        "messageVersion": str,
    },
)

CodeHookTypeDef = TypedDict(
    "CodeHookTypeDef",
    {
        "uri": str,
        "messageVersion": str,
    },
)

_RequiredLogSettingsRequestTypeDef = TypedDict(
    "_RequiredLogSettingsRequestTypeDef",
    {
        "logType": LogTypeType,
        "destination": DestinationType,
        "resourceArn": str,
    },
)
_OptionalLogSettingsRequestTypeDef = TypedDict(
    "_OptionalLogSettingsRequestTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class LogSettingsRequestTypeDef(
    _RequiredLogSettingsRequestTypeDef, _OptionalLogSettingsRequestTypeDef
):
    pass


LogSettingsResponseTypeDef = TypedDict(
    "LogSettingsResponseTypeDef",
    {
        "logType": LogTypeType,
        "destination": DestinationType,
        "kmsKeyArn": str,
        "resourceArn": str,
        "resourcePrefix": str,
    },
    total=False,
)

_RequiredCreateBotVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotVersionRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateBotVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotVersionRequestRequestTypeDef",
    {
        "checksum": str,
    },
    total=False,
)


class CreateBotVersionRequestRequestTypeDef(
    _RequiredCreateBotVersionRequestRequestTypeDef, _OptionalCreateBotVersionRequestRequestTypeDef
):
    pass


IntentOutputTypeDef = TypedDict(
    "IntentOutputTypeDef",
    {
        "intentName": str,
        "intentVersion": str,
    },
)

_RequiredCreateIntentVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntentVersionRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateIntentVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntentVersionRequestRequestTypeDef",
    {
        "checksum": str,
    },
    total=False,
)


class CreateIntentVersionRequestRequestTypeDef(
    _RequiredCreateIntentVersionRequestRequestTypeDef,
    _OptionalCreateIntentVersionRequestRequestTypeDef,
):
    pass


InputContextOutputTypeDef = TypedDict(
    "InputContextOutputTypeDef",
    {
        "name": str,
    },
)

_RequiredKendraConfigurationOutputTypeDef = TypedDict(
    "_RequiredKendraConfigurationOutputTypeDef",
    {
        "kendraIndex": str,
        "role": str,
    },
)
_OptionalKendraConfigurationOutputTypeDef = TypedDict(
    "_OptionalKendraConfigurationOutputTypeDef",
    {
        "queryFilterString": str,
    },
    total=False,
)


class KendraConfigurationOutputTypeDef(
    _RequiredKendraConfigurationOutputTypeDef, _OptionalKendraConfigurationOutputTypeDef
):
    pass


OutputContextOutputTypeDef = TypedDict(
    "OutputContextOutputTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

_RequiredCreateSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSlotTypeVersionRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSlotTypeVersionRequestRequestTypeDef",
    {
        "checksum": str,
    },
    total=False,
)


class CreateSlotTypeVersionRequestRequestTypeDef(
    _RequiredCreateSlotTypeVersionRequestRequestTypeDef,
    _OptionalCreateSlotTypeVersionRequestRequestTypeDef,
):
    pass


_RequiredEnumerationValueOutputTypeDef = TypedDict(
    "_RequiredEnumerationValueOutputTypeDef",
    {
        "value": str,
    },
)
_OptionalEnumerationValueOutputTypeDef = TypedDict(
    "_OptionalEnumerationValueOutputTypeDef",
    {
        "synonyms": List[str],
    },
    total=False,
)


class EnumerationValueOutputTypeDef(
    _RequiredEnumerationValueOutputTypeDef, _OptionalEnumerationValueOutputTypeDef
):
    pass


DeleteBotAliasRequestRequestTypeDef = TypedDict(
    "DeleteBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)

DeleteBotChannelAssociationRequestRequestTypeDef = TypedDict(
    "DeleteBotChannelAssociationRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)

DeleteBotRequestRequestTypeDef = TypedDict(
    "DeleteBotRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteBotVersionRequestRequestTypeDef = TypedDict(
    "DeleteBotVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteIntentRequestRequestTypeDef = TypedDict(
    "DeleteIntentRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteIntentVersionRequestRequestTypeDef = TypedDict(
    "DeleteIntentVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteSlotTypeVersionRequestRequestTypeDef = TypedDict(
    "DeleteSlotTypeVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteUtterancesRequestRequestTypeDef = TypedDict(
    "DeleteUtterancesRequestRequestTypeDef",
    {
        "botName": str,
        "userId": str,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnumerationValueTypeDef = TypedDict(
    "_RequiredEnumerationValueTypeDef",
    {
        "value": str,
    },
)
_OptionalEnumerationValueTypeDef = TypedDict(
    "_OptionalEnumerationValueTypeDef",
    {
        "synonyms": Sequence[str],
    },
    total=False,
)


class EnumerationValueTypeDef(_RequiredEnumerationValueTypeDef, _OptionalEnumerationValueTypeDef):
    pass


GetBotAliasRequestRequestTypeDef = TypedDict(
    "GetBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)

_RequiredGetBotAliasesRequestGetBotAliasesPaginateTypeDef = TypedDict(
    "_RequiredGetBotAliasesRequestGetBotAliasesPaginateTypeDef",
    {
        "botName": str,
    },
)
_OptionalGetBotAliasesRequestGetBotAliasesPaginateTypeDef = TypedDict(
    "_OptionalGetBotAliasesRequestGetBotAliasesPaginateTypeDef",
    {
        "nameContains": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class GetBotAliasesRequestGetBotAliasesPaginateTypeDef(
    _RequiredGetBotAliasesRequestGetBotAliasesPaginateTypeDef,
    _OptionalGetBotAliasesRequestGetBotAliasesPaginateTypeDef,
):
    pass


_RequiredGetBotAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredGetBotAliasesRequestRequestTypeDef",
    {
        "botName": str,
    },
)
_OptionalGetBotAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalGetBotAliasesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)


class GetBotAliasesRequestRequestTypeDef(
    _RequiredGetBotAliasesRequestRequestTypeDef, _OptionalGetBotAliasesRequestRequestTypeDef
):
    pass


GetBotChannelAssociationRequestRequestTypeDef = TypedDict(
    "GetBotChannelAssociationRequestRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)

GetBotChannelAssociationResponseTypeDef = TypedDict(
    "GetBotChannelAssociationResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelTypeType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatusType,
        "failureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef = TypedDict(
    "_RequiredGetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef",
    {
        "botName": str,
        "botAlias": str,
    },
)
_OptionalGetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef = TypedDict(
    "_OptionalGetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef",
    {
        "nameContains": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class GetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef(
    _RequiredGetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef,
    _OptionalGetBotChannelAssociationsRequestGetBotChannelAssociationsPaginateTypeDef,
):
    pass


_RequiredGetBotChannelAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetBotChannelAssociationsRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
    },
)
_OptionalGetBotChannelAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetBotChannelAssociationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)


class GetBotChannelAssociationsRequestRequestTypeDef(
    _RequiredGetBotChannelAssociationsRequestRequestTypeDef,
    _OptionalGetBotChannelAssociationsRequestRequestTypeDef,
):
    pass


GetBotRequestRequestTypeDef = TypedDict(
    "GetBotRequestRequestTypeDef",
    {
        "name": str,
        "versionOrAlias": str,
    },
)

_RequiredGetBotVersionsRequestGetBotVersionsPaginateTypeDef = TypedDict(
    "_RequiredGetBotVersionsRequestGetBotVersionsPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalGetBotVersionsRequestGetBotVersionsPaginateTypeDef = TypedDict(
    "_OptionalGetBotVersionsRequestGetBotVersionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class GetBotVersionsRequestGetBotVersionsPaginateTypeDef(
    _RequiredGetBotVersionsRequestGetBotVersionsPaginateTypeDef,
    _OptionalGetBotVersionsRequestGetBotVersionsPaginateTypeDef,
):
    pass


_RequiredGetBotVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetBotVersionsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetBotVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetBotVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetBotVersionsRequestRequestTypeDef(
    _RequiredGetBotVersionsRequestRequestTypeDef, _OptionalGetBotVersionsRequestRequestTypeDef
):
    pass


GetBotsRequestGetBotsPaginateTypeDef = TypedDict(
    "GetBotsRequestGetBotsPaginateTypeDef",
    {
        "nameContains": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

GetBotsRequestRequestTypeDef = TypedDict(
    "GetBotsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetBuiltinIntentRequestRequestTypeDef = TypedDict(
    "GetBuiltinIntentRequestRequestTypeDef",
    {
        "signature": str,
    },
)

GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef = TypedDict(
    "GetBuiltinIntentsRequestGetBuiltinIntentsPaginateTypeDef",
    {
        "locale": LocaleType,
        "signatureContains": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

GetBuiltinIntentsRequestRequestTypeDef = TypedDict(
    "GetBuiltinIntentsRequestRequestTypeDef",
    {
        "locale": LocaleType,
        "signatureContains": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef = TypedDict(
    "GetBuiltinSlotTypesRequestGetBuiltinSlotTypesPaginateTypeDef",
    {
        "locale": LocaleType,
        "signatureContains": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

GetBuiltinSlotTypesRequestRequestTypeDef = TypedDict(
    "GetBuiltinSlotTypesRequestRequestTypeDef",
    {
        "locale": LocaleType,
        "signatureContains": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetExportRequestRequestTypeDef = TypedDict(
    "GetExportRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
    },
)

GetExportResponseTypeDef = TypedDict(
    "GetExportResponseTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
        "exportStatus": ExportStatusType,
        "failureReason": str,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportRequestRequestTypeDef = TypedDict(
    "GetImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

GetImportResponseTypeDef = TypedDict(
    "GetImportResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "failureReason": List[str],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentRequestRequestTypeDef = TypedDict(
    "GetIntentRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

_RequiredGetIntentVersionsRequestGetIntentVersionsPaginateTypeDef = TypedDict(
    "_RequiredGetIntentVersionsRequestGetIntentVersionsPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalGetIntentVersionsRequestGetIntentVersionsPaginateTypeDef = TypedDict(
    "_OptionalGetIntentVersionsRequestGetIntentVersionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class GetIntentVersionsRequestGetIntentVersionsPaginateTypeDef(
    _RequiredGetIntentVersionsRequestGetIntentVersionsPaginateTypeDef,
    _OptionalGetIntentVersionsRequestGetIntentVersionsPaginateTypeDef,
):
    pass


_RequiredGetIntentVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetIntentVersionsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetIntentVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetIntentVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetIntentVersionsRequestRequestTypeDef(
    _RequiredGetIntentVersionsRequestRequestTypeDef, _OptionalGetIntentVersionsRequestRequestTypeDef
):
    pass


IntentMetadataTypeDef = TypedDict(
    "IntentMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

GetIntentsRequestGetIntentsPaginateTypeDef = TypedDict(
    "GetIntentsRequestGetIntentsPaginateTypeDef",
    {
        "nameContains": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

GetIntentsRequestRequestTypeDef = TypedDict(
    "GetIntentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetMigrationRequestRequestTypeDef = TypedDict(
    "GetMigrationRequestRequestTypeDef",
    {
        "migrationId": str,
    },
)

MigrationAlertTypeDef = TypedDict(
    "MigrationAlertTypeDef",
    {
        "type": MigrationAlertTypeType,
        "message": str,
        "details": List[str],
        "referenceURLs": List[str],
    },
    total=False,
)

GetMigrationsRequestRequestTypeDef = TypedDict(
    "GetMigrationsRequestRequestTypeDef",
    {
        "sortByAttribute": MigrationSortAttributeType,
        "sortByOrder": SortOrderType,
        "v1BotNameContains": str,
        "migrationStatusEquals": MigrationStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

MigrationSummaryTypeDef = TypedDict(
    "MigrationSummaryTypeDef",
    {
        "migrationId": str,
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationStatus": MigrationStatusType,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
    },
    total=False,
)

GetSlotTypeRequestRequestTypeDef = TypedDict(
    "GetSlotTypeRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

_RequiredGetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef = TypedDict(
    "_RequiredGetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalGetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef = TypedDict(
    "_OptionalGetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class GetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef(
    _RequiredGetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef,
    _OptionalGetSlotTypeVersionsRequestGetSlotTypeVersionsPaginateTypeDef,
):
    pass


_RequiredGetSlotTypeVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSlotTypeVersionsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetSlotTypeVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSlotTypeVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetSlotTypeVersionsRequestRequestTypeDef(
    _RequiredGetSlotTypeVersionsRequestRequestTypeDef,
    _OptionalGetSlotTypeVersionsRequestRequestTypeDef,
):
    pass


SlotTypeMetadataTypeDef = TypedDict(
    "SlotTypeMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

GetSlotTypesRequestGetSlotTypesPaginateTypeDef = TypedDict(
    "GetSlotTypesRequestGetSlotTypesPaginateTypeDef",
    {
        "nameContains": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

GetSlotTypesRequestRequestTypeDef = TypedDict(
    "GetSlotTypesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetUtterancesViewRequestRequestTypeDef = TypedDict(
    "GetUtterancesViewRequestRequestTypeDef",
    {
        "botName": str,
        "botVersions": Sequence[str],
        "statusType": StatusTypeType,
    },
)

InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)

IntentTypeDef = TypedDict(
    "IntentTypeDef",
    {
        "intentName": str,
        "intentVersion": str,
    },
)

_RequiredKendraConfigurationTypeDef = TypedDict(
    "_RequiredKendraConfigurationTypeDef",
    {
        "kendraIndex": str,
        "role": str,
    },
)
_OptionalKendraConfigurationTypeDef = TypedDict(
    "_OptionalKendraConfigurationTypeDef",
    {
        "queryFilterString": str,
    },
    total=False,
)


class KendraConfigurationTypeDef(
    _RequiredKendraConfigurationTypeDef, _OptionalKendraConfigurationTypeDef
):
    pass


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

_RequiredMessageOutputTypeDef = TypedDict(
    "_RequiredMessageOutputTypeDef",
    {
        "contentType": ContentTypeType,
        "content": str,
    },
)
_OptionalMessageOutputTypeDef = TypedDict(
    "_OptionalMessageOutputTypeDef",
    {
        "groupNumber": int,
    },
    total=False,
)


class MessageOutputTypeDef(_RequiredMessageOutputTypeDef, _OptionalMessageOutputTypeDef):
    pass


_RequiredMessageTypeDef = TypedDict(
    "_RequiredMessageTypeDef",
    {
        "contentType": ContentTypeType,
        "content": str,
    },
)
_OptionalMessageTypeDef = TypedDict(
    "_OptionalMessageTypeDef",
    {
        "groupNumber": int,
    },
    total=False,
)


class MessageTypeDef(_RequiredMessageTypeDef, _OptionalMessageTypeDef):
    pass


OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
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

SlotDefaultValueOutputTypeDef = TypedDict(
    "SlotDefaultValueOutputTypeDef",
    {
        "defaultValue": str,
    },
)

SlotDefaultValueTypeDef = TypedDict(
    "SlotDefaultValueTypeDef",
    {
        "defaultValue": str,
    },
)

SlotTypeRegexConfigurationOutputTypeDef = TypedDict(
    "SlotTypeRegexConfigurationOutputTypeDef",
    {
        "pattern": str,
    },
)

SlotTypeRegexConfigurationTypeDef = TypedDict(
    "SlotTypeRegexConfigurationTypeDef",
    {
        "pattern": str,
    },
)

StartMigrationRequestRequestTypeDef = TypedDict(
    "StartMigrationRequestRequestTypeDef",
    {
        "v1BotName": str,
        "v1BotVersion": str,
        "v2BotName": str,
        "v2BotRole": str,
        "migrationStrategy": MigrationStrategyType,
    },
)

StartMigrationResponseTypeDef = TypedDict(
    "StartMigrationResponseTypeDef",
    {
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationId": str,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
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

UtteranceDataTypeDef = TypedDict(
    "UtteranceDataTypeDef",
    {
        "utteranceString": str,
        "count": int,
        "distinctUsers": int,
        "firstUtteredDate": datetime,
        "lastUtteredDate": datetime,
    },
    total=False,
)

GetBotChannelAssociationsResponseTypeDef = TypedDict(
    "GetBotChannelAssociationsResponseTypeDef",
    {
        "botChannelAssociations": List[BotChannelAssociationTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotVersionsResponseTypeDef = TypedDict(
    "GetBotVersionsResponseTypeDef",
    {
        "bots": List[BotMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotsResponseTypeDef = TypedDict(
    "GetBotsResponseTypeDef",
    {
        "bots": List[BotMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinIntentsResponseTypeDef = TypedDict(
    "GetBuiltinIntentsResponseTypeDef",
    {
        "intents": List[BuiltinIntentMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinIntentResponseTypeDef = TypedDict(
    "GetBuiltinIntentResponseTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
        "slots": List[BuiltinIntentSlotTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinSlotTypesResponseTypeDef = TypedDict(
    "GetBuiltinSlotTypesResponseTypeDef",
    {
        "slotTypes": List[BuiltinSlotTypeMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFulfillmentActivityOutputTypeDef = TypedDict(
    "_RequiredFulfillmentActivityOutputTypeDef",
    {
        "type": FulfillmentActivityTypeType,
    },
)
_OptionalFulfillmentActivityOutputTypeDef = TypedDict(
    "_OptionalFulfillmentActivityOutputTypeDef",
    {
        "codeHook": CodeHookOutputTypeDef,
    },
    total=False,
)


class FulfillmentActivityOutputTypeDef(
    _RequiredFulfillmentActivityOutputTypeDef, _OptionalFulfillmentActivityOutputTypeDef
):
    pass


_RequiredFulfillmentActivityTypeDef = TypedDict(
    "_RequiredFulfillmentActivityTypeDef",
    {
        "type": FulfillmentActivityTypeType,
    },
)
_OptionalFulfillmentActivityTypeDef = TypedDict(
    "_OptionalFulfillmentActivityTypeDef",
    {
        "codeHook": CodeHookTypeDef,
    },
    total=False,
)


class FulfillmentActivityTypeDef(
    _RequiredFulfillmentActivityTypeDef, _OptionalFulfillmentActivityTypeDef
):
    pass


ConversationLogsRequestTypeDef = TypedDict(
    "ConversationLogsRequestTypeDef",
    {
        "logSettings": Sequence[LogSettingsRequestTypeDef],
        "iamRoleArn": str,
    },
)

ConversationLogsResponseTypeDef = TypedDict(
    "ConversationLogsResponseTypeDef",
    {
        "logSettings": List[LogSettingsResponseTypeDef],
        "iamRoleArn": str,
    },
    total=False,
)

GetIntentVersionsResponseTypeDef = TypedDict(
    "GetIntentVersionsResponseTypeDef",
    {
        "intents": List[IntentMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentsResponseTypeDef = TypedDict(
    "GetIntentsResponseTypeDef",
    {
        "intents": List[IntentMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMigrationResponseTypeDef = TypedDict(
    "GetMigrationResponseTypeDef",
    {
        "migrationId": str,
        "v1BotName": str,
        "v1BotVersion": str,
        "v1BotLocale": LocaleType,
        "v2BotId": str,
        "v2BotRole": str,
        "migrationStatus": MigrationStatusType,
        "migrationStrategy": MigrationStrategyType,
        "migrationTimestamp": datetime,
        "alerts": List[MigrationAlertTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMigrationsResponseTypeDef = TypedDict(
    "GetMigrationsResponseTypeDef",
    {
        "migrationSummaries": List[MigrationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypeVersionsResponseTypeDef = TypedDict(
    "GetSlotTypeVersionsResponseTypeDef",
    {
        "slotTypes": List[SlotTypeMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypesResponseTypeDef = TypedDict(
    "GetSlotTypesResponseTypeDef",
    {
        "slotTypes": List[SlotTypeMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "tags": List[TagOutputTypeDef],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPromptOutputTypeDef = TypedDict(
    "_RequiredPromptOutputTypeDef",
    {
        "messages": List[MessageOutputTypeDef],
        "maxAttempts": int,
    },
)
_OptionalPromptOutputTypeDef = TypedDict(
    "_OptionalPromptOutputTypeDef",
    {
        "responseCard": str,
    },
    total=False,
)


class PromptOutputTypeDef(_RequiredPromptOutputTypeDef, _OptionalPromptOutputTypeDef):
    pass


_RequiredStatementOutputTypeDef = TypedDict(
    "_RequiredStatementOutputTypeDef",
    {
        "messages": List[MessageOutputTypeDef],
    },
)
_OptionalStatementOutputTypeDef = TypedDict(
    "_OptionalStatementOutputTypeDef",
    {
        "responseCard": str,
    },
    total=False,
)


class StatementOutputTypeDef(_RequiredStatementOutputTypeDef, _OptionalStatementOutputTypeDef):
    pass


_RequiredPromptTypeDef = TypedDict(
    "_RequiredPromptTypeDef",
    {
        "messages": Sequence[MessageTypeDef],
        "maxAttempts": int,
    },
)
_OptionalPromptTypeDef = TypedDict(
    "_OptionalPromptTypeDef",
    {
        "responseCard": str,
    },
    total=False,
)


class PromptTypeDef(_RequiredPromptTypeDef, _OptionalPromptTypeDef):
    pass


_RequiredStatementTypeDef = TypedDict(
    "_RequiredStatementTypeDef",
    {
        "messages": Sequence[MessageTypeDef],
    },
)
_OptionalStatementTypeDef = TypedDict(
    "_OptionalStatementTypeDef",
    {
        "responseCard": str,
    },
    total=False,
)


class StatementTypeDef(_RequiredStatementTypeDef, _OptionalStatementTypeDef):
    pass


_RequiredStartImportRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportRequestRequestTypeDef",
    {
        "payload": Union[str, bytes, IO[Any], StreamingBody],
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
    },
)
_OptionalStartImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class StartImportRequestRequestTypeDef(
    _RequiredStartImportRequestRequestTypeDef, _OptionalStartImportRequestRequestTypeDef
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

SlotDefaultValueSpecOutputTypeDef = TypedDict(
    "SlotDefaultValueSpecOutputTypeDef",
    {
        "defaultValueList": List[SlotDefaultValueOutputTypeDef],
    },
)

SlotDefaultValueSpecTypeDef = TypedDict(
    "SlotDefaultValueSpecTypeDef",
    {
        "defaultValueList": Sequence[SlotDefaultValueTypeDef],
    },
)

SlotTypeConfigurationOutputTypeDef = TypedDict(
    "SlotTypeConfigurationOutputTypeDef",
    {
        "regexConfiguration": SlotTypeRegexConfigurationOutputTypeDef,
    },
    total=False,
)

SlotTypeConfigurationTypeDef = TypedDict(
    "SlotTypeConfigurationTypeDef",
    {
        "regexConfiguration": SlotTypeRegexConfigurationTypeDef,
    },
    total=False,
)

UtteranceListTypeDef = TypedDict(
    "UtteranceListTypeDef",
    {
        "botVersion": str,
        "utterances": List[UtteranceDataTypeDef],
    },
    total=False,
)

_RequiredPutBotAliasRequestRequestTypeDef = TypedDict(
    "_RequiredPutBotAliasRequestRequestTypeDef",
    {
        "name": str,
        "botVersion": str,
        "botName": str,
    },
)
_OptionalPutBotAliasRequestRequestTypeDef = TypedDict(
    "_OptionalPutBotAliasRequestRequestTypeDef",
    {
        "description": str,
        "checksum": str,
        "conversationLogs": ConversationLogsRequestTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class PutBotAliasRequestRequestTypeDef(
    _RequiredPutBotAliasRequestRequestTypeDef, _OptionalPutBotAliasRequestRequestTypeDef
):
    pass


BotAliasMetadataTypeDef = TypedDict(
    "BotAliasMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ConversationLogsResponseTypeDef,
    },
    total=False,
)

GetBotAliasResponseTypeDef = TypedDict(
    "GetBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ConversationLogsResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutBotAliasResponseTypeDef = TypedDict(
    "PutBotAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": ConversationLogsResponseTypeDef,
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBotVersionResponseTypeDef = TypedDict(
    "CreateBotVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[IntentOutputTypeDef],
        "clarificationPrompt": PromptOutputTypeDef,
        "abortStatement": StatementOutputTypeDef,
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "enableModelImprovements": bool,
        "detectSentiment": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FollowUpPromptOutputTypeDef = TypedDict(
    "FollowUpPromptOutputTypeDef",
    {
        "prompt": PromptOutputTypeDef,
        "rejectionStatement": StatementOutputTypeDef,
    },
)

GetBotResponseTypeDef = TypedDict(
    "GetBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[IntentOutputTypeDef],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": PromptOutputTypeDef,
        "abortStatement": StatementOutputTypeDef,
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "detectSentiment": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutBotResponseTypeDef = TypedDict(
    "PutBotResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List[IntentOutputTypeDef],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": PromptOutputTypeDef,
        "abortStatement": StatementOutputTypeDef,
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "createVersion": bool,
        "detectSentiment": bool,
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FollowUpPromptTypeDef = TypedDict(
    "FollowUpPromptTypeDef",
    {
        "prompt": PromptTypeDef,
        "rejectionStatement": StatementTypeDef,
    },
)

_RequiredPutBotRequestRequestTypeDef = TypedDict(
    "_RequiredPutBotRequestRequestTypeDef",
    {
        "name": str,
        "locale": LocaleType,
        "childDirected": bool,
    },
)
_OptionalPutBotRequestRequestTypeDef = TypedDict(
    "_OptionalPutBotRequestRequestTypeDef",
    {
        "description": str,
        "intents": Sequence[IntentTypeDef],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": PromptTypeDef,
        "abortStatement": StatementTypeDef,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "processBehavior": ProcessBehaviorType,
        "detectSentiment": bool,
        "createVersion": bool,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class PutBotRequestRequestTypeDef(
    _RequiredPutBotRequestRequestTypeDef, _OptionalPutBotRequestRequestTypeDef
):
    pass


_RequiredSlotOutputTypeDef = TypedDict(
    "_RequiredSlotOutputTypeDef",
    {
        "name": str,
        "slotConstraint": SlotConstraintType,
    },
)
_OptionalSlotOutputTypeDef = TypedDict(
    "_OptionalSlotOutputTypeDef",
    {
        "description": str,
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": PromptOutputTypeDef,
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
        "obfuscationSetting": ObfuscationSettingType,
        "defaultValueSpec": SlotDefaultValueSpecOutputTypeDef,
    },
    total=False,
)


class SlotOutputTypeDef(_RequiredSlotOutputTypeDef, _OptionalSlotOutputTypeDef):
    pass


_RequiredSlotTypeDef = TypedDict(
    "_RequiredSlotTypeDef",
    {
        "name": str,
        "slotConstraint": SlotConstraintType,
    },
)
_OptionalSlotTypeDef = TypedDict(
    "_OptionalSlotTypeDef",
    {
        "description": str,
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": PromptTypeDef,
        "priority": int,
        "sampleUtterances": Sequence[str],
        "responseCard": str,
        "obfuscationSetting": ObfuscationSettingType,
        "defaultValueSpec": SlotDefaultValueSpecTypeDef,
    },
    total=False,
)


class SlotTypeDef(_RequiredSlotTypeDef, _OptionalSlotTypeDef):
    pass


CreateSlotTypeVersionResponseTypeDef = TypedDict(
    "CreateSlotTypeVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[EnumerationValueOutputTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[SlotTypeConfigurationOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypeResponseTypeDef = TypedDict(
    "GetSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[EnumerationValueOutputTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[SlotTypeConfigurationOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSlotTypeResponseTypeDef = TypedDict(
    "PutSlotTypeResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List[EnumerationValueOutputTypeDef],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List[SlotTypeConfigurationOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSlotTypeRequestRequestTypeDef = TypedDict(
    "_RequiredPutSlotTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutSlotTypeRequestRequestTypeDef = TypedDict(
    "_OptionalPutSlotTypeRequestRequestTypeDef",
    {
        "description": str,
        "enumerationValues": Sequence[EnumerationValueTypeDef],
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": Sequence[SlotTypeConfigurationTypeDef],
    },
    total=False,
)


class PutSlotTypeRequestRequestTypeDef(
    _RequiredPutSlotTypeRequestRequestTypeDef, _OptionalPutSlotTypeRequestRequestTypeDef
):
    pass


GetUtterancesViewResponseTypeDef = TypedDict(
    "GetUtterancesViewResponseTypeDef",
    {
        "botName": str,
        "utterances": List[UtteranceListTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotAliasesResponseTypeDef = TypedDict(
    "GetBotAliasesResponseTypeDef",
    {
        "BotAliases": List[BotAliasMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIntentVersionResponseTypeDef = TypedDict(
    "CreateIntentVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[SlotOutputTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": PromptOutputTypeDef,
        "rejectionStatement": StatementOutputTypeDef,
        "followUpPrompt": FollowUpPromptOutputTypeDef,
        "conclusionStatement": StatementOutputTypeDef,
        "dialogCodeHook": CodeHookOutputTypeDef,
        "fulfillmentActivity": FulfillmentActivityOutputTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": KendraConfigurationOutputTypeDef,
        "inputContexts": List[InputContextOutputTypeDef],
        "outputContexts": List[OutputContextOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentResponseTypeDef = TypedDict(
    "GetIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[SlotOutputTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": PromptOutputTypeDef,
        "rejectionStatement": StatementOutputTypeDef,
        "followUpPrompt": FollowUpPromptOutputTypeDef,
        "conclusionStatement": StatementOutputTypeDef,
        "dialogCodeHook": CodeHookOutputTypeDef,
        "fulfillmentActivity": FulfillmentActivityOutputTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": KendraConfigurationOutputTypeDef,
        "inputContexts": List[InputContextOutputTypeDef],
        "outputContexts": List[OutputContextOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutIntentResponseTypeDef = TypedDict(
    "PutIntentResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List[SlotOutputTypeDef],
        "sampleUtterances": List[str],
        "confirmationPrompt": PromptOutputTypeDef,
        "rejectionStatement": StatementOutputTypeDef,
        "followUpPrompt": FollowUpPromptOutputTypeDef,
        "conclusionStatement": StatementOutputTypeDef,
        "dialogCodeHook": CodeHookOutputTypeDef,
        "fulfillmentActivity": FulfillmentActivityOutputTypeDef,
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "createVersion": bool,
        "kendraConfiguration": KendraConfigurationOutputTypeDef,
        "inputContexts": List[InputContextOutputTypeDef],
        "outputContexts": List[OutputContextOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutIntentRequestRequestTypeDef = TypedDict(
    "_RequiredPutIntentRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutIntentRequestRequestTypeDef = TypedDict(
    "_OptionalPutIntentRequestRequestTypeDef",
    {
        "description": str,
        "slots": Sequence[SlotTypeDef],
        "sampleUtterances": Sequence[str],
        "confirmationPrompt": PromptTypeDef,
        "rejectionStatement": StatementTypeDef,
        "followUpPrompt": FollowUpPromptTypeDef,
        "conclusionStatement": StatementTypeDef,
        "dialogCodeHook": CodeHookTypeDef,
        "fulfillmentActivity": FulfillmentActivityTypeDef,
        "parentIntentSignature": str,
        "checksum": str,
        "createVersion": bool,
        "kendraConfiguration": KendraConfigurationTypeDef,
        "inputContexts": Sequence[InputContextTypeDef],
        "outputContexts": Sequence[OutputContextTypeDef],
    },
    total=False,
)


class PutIntentRequestRequestTypeDef(
    _RequiredPutIntentRequestRequestTypeDef, _OptionalPutIntentRequestRequestTypeDef
):
    pass
