"""
Type annotations for chime-sdk-identity service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_identity.type_defs import IdentityTypeDef

    data: IdentityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AllowMessagesType,
    AppInstanceUserEndpointTypeType,
    EndpointStatusReasonType,
    EndpointStatusType,
    StandardMessagesType,
    TargetedMessagesType,
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
    "IdentityTypeDef",
    "AppInstanceBotSummaryTypeDef",
    "ChannelRetentionSettingsOutputTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "EndpointStateTypeDef",
    "EndpointAttributesOutputTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "ExpirationSettingsOutputTypeDef",
    "CreateAppInstanceAdminRequestRequestTypeDef",
    "TagTypeDef",
    "CreateAppInstanceBotResponseTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "ExpirationSettingsTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    "DeleteAppInstanceBotRequestRequestTypeDef",
    "DeleteAppInstanceRequestRequestTypeDef",
    "DeleteAppInstanceUserRequestRequestTypeDef",
    "DeregisterAppInstanceUserEndpointRequestRequestTypeDef",
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    "DescribeAppInstanceBotRequestRequestTypeDef",
    "DescribeAppInstanceRequestRequestTypeDef",
    "DescribeAppInstanceUserEndpointRequestRequestTypeDef",
    "DescribeAppInstanceUserRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointAttributesTypeDef",
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    "InvokedByOutputTypeDef",
    "InvokedByTypeDef",
    "ListAppInstanceAdminsRequestRequestTypeDef",
    "ListAppInstanceBotsRequestRequestTypeDef",
    "ListAppInstanceUserEndpointsRequestRequestTypeDef",
    "ListAppInstanceUsersRequestRequestTypeDef",
    "ListAppInstancesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    "ResponseMetadataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppInstanceBotResponseTypeDef",
    "UpdateAppInstanceRequestRequestTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserEndpointRequestRequestTypeDef",
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    "UpdateAppInstanceUserRequestRequestTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "ListAppInstanceBotsResponseTypeDef",
    "AppInstanceRetentionSettingsOutputTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "ListAppInstancesResponseTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "AppInstanceUserEndpointSummaryTypeDef",
    "AppInstanceUserEndpointTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "AppInstanceUserTypeDef",
    "PutAppInstanceUserExpirationSettingsResponseTypeDef",
    "CreateAppInstanceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAppInstanceUserRequestRequestTypeDef",
    "PutAppInstanceUserExpirationSettingsRequestRequestTypeDef",
    "RegisterAppInstanceUserEndpointRequestRequestTypeDef",
    "LexConfigurationOutputTypeDef",
    "LexConfigurationTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    "ListAppInstanceUserEndpointsResponseTypeDef",
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationTypeDef",
    "AppInstanceBotTypeDef",
    "CreateAppInstanceBotRequestRequestTypeDef",
    "UpdateAppInstanceBotRequestRequestTypeDef",
    "DescribeAppInstanceBotResponseTypeDef",
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

AppInstanceBotSummaryTypeDef = TypedDict(
    "AppInstanceBotSummaryTypeDef",
    {
        "AppInstanceBotArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
)

ChannelRetentionSettingsOutputTypeDef = TypedDict(
    "ChannelRetentionSettingsOutputTypeDef",
    {
        "RetentionDays": int,
    },
    total=False,
)

ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef",
    {
        "RetentionDays": int,
    },
    total=False,
)

AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
)

AppInstanceTypeDef = TypedDict(
    "AppInstanceTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Metadata": str,
    },
    total=False,
)

_RequiredEndpointStateTypeDef = TypedDict(
    "_RequiredEndpointStateTypeDef",
    {
        "Status": EndpointStatusType,
    },
)
_OptionalEndpointStateTypeDef = TypedDict(
    "_OptionalEndpointStateTypeDef",
    {
        "StatusReason": EndpointStatusReasonType,
    },
    total=False,
)

class EndpointStateTypeDef(_RequiredEndpointStateTypeDef, _OptionalEndpointStateTypeDef):
    pass

_RequiredEndpointAttributesOutputTypeDef = TypedDict(
    "_RequiredEndpointAttributesOutputTypeDef",
    {
        "DeviceToken": str,
    },
)
_OptionalEndpointAttributesOutputTypeDef = TypedDict(
    "_OptionalEndpointAttributesOutputTypeDef",
    {
        "VoipDeviceToken": str,
    },
    total=False,
)

class EndpointAttributesOutputTypeDef(
    _RequiredEndpointAttributesOutputTypeDef, _OptionalEndpointAttributesOutputTypeDef
):
    pass

AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
)

ExpirationSettingsOutputTypeDef = TypedDict(
    "ExpirationSettingsOutputTypeDef",
    {
        "ExpirationDays": int,
        "ExpirationCriterion": Literal["CREATED_TIMESTAMP"],
    },
)

CreateAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateAppInstanceBotResponseTypeDef = TypedDict(
    "CreateAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBotArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppInstanceResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExpirationSettingsTypeDef = TypedDict(
    "ExpirationSettingsTypeDef",
    {
        "ExpirationDays": int,
        "ExpirationCriterion": Literal["CREATED_TIMESTAMP"],
    },
)

CreateAppInstanceUserResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceBotRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
    },
)

DeleteAppInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DeregisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "DeregisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)

DescribeAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceBotRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
    },
)

DescribeAppInstanceRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)

DescribeAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEndpointAttributesTypeDef = TypedDict(
    "_RequiredEndpointAttributesTypeDef",
    {
        "DeviceToken": str,
    },
)
_OptionalEndpointAttributesTypeDef = TypedDict(
    "_OptionalEndpointAttributesTypeDef",
    {
        "VoipDeviceToken": str,
    },
    total=False,
)

class EndpointAttributesTypeDef(
    _RequiredEndpointAttributesTypeDef, _OptionalEndpointAttributesTypeDef
):
    pass

GetAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

InvokedByOutputTypeDef = TypedDict(
    "InvokedByOutputTypeDef",
    {
        "StandardMessages": StandardMessagesType,
        "TargetedMessages": TargetedMessagesType,
    },
)

InvokedByTypeDef = TypedDict(
    "InvokedByTypeDef",
    {
        "StandardMessages": StandardMessagesType,
        "TargetedMessages": TargetedMessagesType,
    },
)

_RequiredListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceAdminsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceAdminsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceAdminsRequestRequestTypeDef(
    _RequiredListAppInstanceAdminsRequestRequestTypeDef,
    _OptionalListAppInstanceAdminsRequestRequestTypeDef,
):
    pass

_RequiredListAppInstanceBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceBotsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceBotsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceBotsRequestRequestTypeDef(
    _RequiredListAppInstanceBotsRequestRequestTypeDef,
    _OptionalListAppInstanceBotsRequestRequestTypeDef,
):
    pass

_RequiredListAppInstanceUserEndpointsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceUserEndpointsRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)
_OptionalListAppInstanceUserEndpointsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceUserEndpointsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceUserEndpointsRequestRequestTypeDef(
    _RequiredListAppInstanceUserEndpointsRequestRequestTypeDef,
    _OptionalListAppInstanceUserEndpointsRequestRequestTypeDef,
):
    pass

_RequiredListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceUsersRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceUsersRequestRequestTypeDef(
    _RequiredListAppInstanceUsersRequestRequestTypeDef,
    _OptionalListAppInstanceUsersRequestRequestTypeDef,
):
    pass

ListAppInstancesRequestRequestTypeDef = TypedDict(
    "ListAppInstancesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
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

RegisterAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAppInstanceBotResponseTypeDef = TypedDict(
    "UpdateAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBotArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppInstanceRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
    },
)

UpdateAppInstanceResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)
_OptionalUpdateAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "Name": str,
        "AllowMessages": AllowMessagesType,
    },
    total=False,
)

class UpdateAppInstanceUserEndpointRequestRequestTypeDef(
    _RequiredUpdateAppInstanceUserEndpointRequestRequestTypeDef,
    _OptionalUpdateAppInstanceUserEndpointRequestRequestTypeDef,
):
    pass

UpdateAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
    },
)

UpdateAppInstanceUserResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef",
    {
        "Admin": IdentityTypeDef,
    },
    total=False,
)

AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {
        "Admin": IdentityTypeDef,
        "AppInstanceArn": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

CreateAppInstanceAdminResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": IdentityTypeDef,
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstanceBotsResponseTypeDef = TypedDict(
    "ListAppInstanceBotsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceBots": List[AppInstanceBotSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AppInstanceRetentionSettingsOutputTypeDef = TypedDict(
    "AppInstanceRetentionSettingsOutputTypeDef",
    {
        "ChannelRetentionSettings": ChannelRetentionSettingsOutputTypeDef,
    },
    total=False,
)

AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {
        "ChannelRetentionSettings": ChannelRetentionSettingsTypeDef,
    },
    total=False,
)

ListAppInstancesResponseTypeDef = TypedDict(
    "ListAppInstancesResponseTypeDef",
    {
        "AppInstances": List[AppInstanceSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseTypeDef",
    {
        "AppInstance": AppInstanceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AppInstanceUserEndpointSummaryTypeDef = TypedDict(
    "AppInstanceUserEndpointSummaryTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "Name": str,
        "Type": AppInstanceUserEndpointTypeType,
        "AllowMessages": AllowMessagesType,
        "EndpointState": EndpointStateTypeDef,
    },
    total=False,
)

AppInstanceUserEndpointTypeDef = TypedDict(
    "AppInstanceUserEndpointTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "Name": str,
        "Type": AppInstanceUserEndpointTypeType,
        "ResourceArn": str,
        "EndpointAttributes": EndpointAttributesOutputTypeDef,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "AllowMessages": AllowMessagesType,
        "EndpointState": EndpointStateTypeDef,
    },
    total=False,
)

ListAppInstanceUsersResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List[AppInstanceUserSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AppInstanceUserTypeDef = TypedDict(
    "AppInstanceUserTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "ExpirationSettings": ExpirationSettingsOutputTypeDef,
    },
    total=False,
)

PutAppInstanceUserExpirationSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceUserExpirationSettingsResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ExpirationSettings": ExpirationSettingsOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateAppInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceRequestRequestTypeDef",
    {
        "Metadata": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateAppInstanceRequestRequestTypeDef(
    _RequiredCreateAppInstanceRequestRequestTypeDef, _OptionalCreateAppInstanceRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredCreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUserId": str,
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceUserRequestRequestTypeDef",
    {
        "Metadata": str,
        "Tags": Sequence[TagTypeDef],
        "ExpirationSettings": ExpirationSettingsTypeDef,
    },
    total=False,
)

class CreateAppInstanceUserRequestRequestTypeDef(
    _RequiredCreateAppInstanceUserRequestRequestTypeDef,
    _OptionalCreateAppInstanceUserRequestRequestTypeDef,
):
    pass

_RequiredPutAppInstanceUserExpirationSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredPutAppInstanceUserExpirationSettingsRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)
_OptionalPutAppInstanceUserExpirationSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalPutAppInstanceUserExpirationSettingsRequestRequestTypeDef",
    {
        "ExpirationSettings": ExpirationSettingsTypeDef,
    },
    total=False,
)

class PutAppInstanceUserExpirationSettingsRequestRequestTypeDef(
    _RequiredPutAppInstanceUserExpirationSettingsRequestRequestTypeDef,
    _OptionalPutAppInstanceUserExpirationSettingsRequestRequestTypeDef,
):
    pass

_RequiredRegisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Type": AppInstanceUserEndpointTypeType,
        "ResourceArn": str,
        "EndpointAttributes": EndpointAttributesTypeDef,
        "ClientRequestToken": str,
    },
)
_OptionalRegisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "Name": str,
        "AllowMessages": AllowMessagesType,
    },
    total=False,
)

class RegisterAppInstanceUserEndpointRequestRequestTypeDef(
    _RequiredRegisterAppInstanceUserEndpointRequestRequestTypeDef,
    _OptionalRegisterAppInstanceUserEndpointRequestRequestTypeDef,
):
    pass

_RequiredLexConfigurationOutputTypeDef = TypedDict(
    "_RequiredLexConfigurationOutputTypeDef",
    {
        "LexBotAliasArn": str,
        "LocaleId": str,
    },
)
_OptionalLexConfigurationOutputTypeDef = TypedDict(
    "_OptionalLexConfigurationOutputTypeDef",
    {
        "RespondsTo": Literal["STANDARD_MESSAGES"],
        "InvokedBy": InvokedByOutputTypeDef,
        "WelcomeIntent": str,
    },
    total=False,
)

class LexConfigurationOutputTypeDef(
    _RequiredLexConfigurationOutputTypeDef, _OptionalLexConfigurationOutputTypeDef
):
    pass

_RequiredLexConfigurationTypeDef = TypedDict(
    "_RequiredLexConfigurationTypeDef",
    {
        "LexBotAliasArn": str,
        "LocaleId": str,
    },
)
_OptionalLexConfigurationTypeDef = TypedDict(
    "_OptionalLexConfigurationTypeDef",
    {
        "RespondsTo": Literal["STANDARD_MESSAGES"],
        "InvokedBy": InvokedByTypeDef,
        "WelcomeIntent": str,
    },
    total=False,
)

class LexConfigurationTypeDef(_RequiredLexConfigurationTypeDef, _OptionalLexConfigurationTypeDef):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstanceAdminsResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List[AppInstanceAdminSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceAdminResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": AppInstanceAdminTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsOutputTypeDef,
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsOutputTypeDef,
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceRetentionSettings": AppInstanceRetentionSettingsTypeDef,
    },
)

ListAppInstanceUserEndpointsResponseTypeDef = TypedDict(
    "ListAppInstanceUserEndpointsResponseTypeDef",
    {
        "AppInstanceUserEndpoints": List[AppInstanceUserEndpointSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserEndpoint": AppInstanceUserEndpointTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUser": AppInstanceUserTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationOutputTypeDef = TypedDict(
    "ConfigurationOutputTypeDef",
    {
        "Lex": LexConfigurationOutputTypeDef,
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Lex": LexConfigurationTypeDef,
    },
)

AppInstanceBotTypeDef = TypedDict(
    "AppInstanceBotTypeDef",
    {
        "AppInstanceBotArn": str,
        "Name": str,
        "Configuration": ConfigurationOutputTypeDef,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Metadata": str,
    },
    total=False,
)

_RequiredCreateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "ClientRequestToken": str,
        "Configuration": ConfigurationTypeDef,
    },
)
_OptionalCreateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceBotRequestRequestTypeDef",
    {
        "Name": str,
        "Metadata": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateAppInstanceBotRequestRequestTypeDef(
    _RequiredCreateAppInstanceBotRequestRequestTypeDef,
    _OptionalCreateAppInstanceBotRequestRequestTypeDef,
):
    pass

_RequiredUpdateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
        "Name": str,
        "Metadata": str,
    },
)
_OptionalUpdateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppInstanceBotRequestRequestTypeDef",
    {
        "Configuration": ConfigurationTypeDef,
    },
    total=False,
)

class UpdateAppInstanceBotRequestRequestTypeDef(
    _RequiredUpdateAppInstanceBotRequestRequestTypeDef,
    _OptionalUpdateAppInstanceBotRequestRequestTypeDef,
):
    pass

DescribeAppInstanceBotResponseTypeDef = TypedDict(
    "DescribeAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBot": AppInstanceBotTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
