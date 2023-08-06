"""
Type annotations for cognito-idp service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/type_defs/)

Usage::

    ```python
    from mypy_boto3_cognito_idp.type_defs import RecoveryOptionTypeOutputTypeDef

    data: RecoveryOptionTypeOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AccountTakeoverEventActionTypeType,
    AdvancedSecurityModeTypeType,
    AliasAttributeTypeType,
    AttributeDataTypeType,
    AuthFlowTypeType,
    ChallengeNameType,
    ChallengeNameTypeType,
    ChallengeResponseType,
    CompromisedCredentialsEventActionTypeType,
    DefaultEmailOptionTypeType,
    DeletionProtectionTypeType,
    DeliveryMediumTypeType,
    DeviceRememberedStatusTypeType,
    DomainStatusTypeType,
    EmailSendingAccountTypeType,
    EventFilterTypeType,
    EventResponseTypeType,
    EventTypeType,
    ExplicitAuthFlowsTypeType,
    FeedbackValueTypeType,
    IdentityProviderTypeTypeType,
    MessageActionTypeType,
    OAuthFlowTypeType,
    PreventUserExistenceErrorTypesType,
    RecoveryOptionNameTypeType,
    RiskDecisionTypeType,
    RiskLevelTypeType,
    StatusTypeType,
    TimeUnitsTypeType,
    UserImportJobStatusTypeType,
    UsernameAttributeTypeType,
    UserPoolMfaTypeType,
    UserStatusTypeType,
    VerifiedAttributeTypeType,
    VerifySoftwareTokenResponseTypeType,
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
    "RecoveryOptionTypeOutputTypeDef",
    "RecoveryOptionTypeTypeDef",
    "AccountTakeoverActionTypeOutputTypeDef",
    "AccountTakeoverActionTypeTypeDef",
    "AdminAddUserToGroupRequestRequestTypeDef",
    "AdminConfirmSignUpRequestRequestTypeDef",
    "MessageTemplateTypeOutputTypeDef",
    "MessageTemplateTypeTypeDef",
    "AttributeTypeTypeDef",
    "AdminDeleteUserAttributesRequestRequestTypeDef",
    "AdminDeleteUserRequestRequestTypeDef",
    "ProviderUserIdentifierTypeTypeDef",
    "AdminDisableUserRequestRequestTypeDef",
    "AdminEnableUserRequestRequestTypeDef",
    "AdminForgetDeviceRequestRequestTypeDef",
    "AdminGetDeviceRequestRequestTypeDef",
    "AdminGetUserRequestRequestTypeDef",
    "AttributeTypeOutputTypeDef",
    "MFAOptionTypeOutputTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AdminListDevicesRequestRequestTypeDef",
    "AdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef",
    "AdminListGroupsForUserRequestRequestTypeDef",
    "GroupTypeTypeDef",
    "AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef",
    "AdminListUserAuthEventsRequestRequestTypeDef",
    "AdminRemoveUserFromGroupRequestRequestTypeDef",
    "AdminResetUserPasswordRequestRequestTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "AdminSetUserPasswordRequestRequestTypeDef",
    "MFAOptionTypeTypeDef",
    "AdminUpdateAuthEventFeedbackRequestRequestTypeDef",
    "AdminUpdateDeviceStatusRequestRequestTypeDef",
    "AdminUserGlobalSignOutRequestRequestTypeDef",
    "AnalyticsConfigurationTypeOutputTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AssociateSoftwareTokenRequestRequestTypeDef",
    "AssociateSoftwareTokenResponseTypeDef",
    "ChallengeResponseTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "NewDeviceMetadataTypeTypeDef",
    "ChangePasswordRequestRequestTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeOutputTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "ConfirmDeviceResponseTypeDef",
    "UserContextDataTypeTypeDef",
    "HttpHeaderTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "IdentityProviderTypeTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "CreateUserImportJobRequestRequestTypeDef",
    "UserImportJobTypeTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "CreateUserPoolDomainResponseTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "SmsConfigurationTypeTypeDef",
    "UserAttributeUpdateSettingsTypeTypeDef",
    "UserPoolAddOnsTypeTypeDef",
    "UsernameConfigurationTypeTypeDef",
    "VerificationMessageTemplateTypeTypeDef",
    "CustomDomainConfigTypeOutputTypeDef",
    "CustomEmailLambdaVersionConfigTypeOutputTypeDef",
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    "CustomSMSLambdaVersionConfigTypeOutputTypeDef",
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteResourceServerRequestRequestTypeDef",
    "DeleteUserAttributesRequestRequestTypeDef",
    "DeleteUserPoolClientRequestRequestTypeDef",
    "DeleteUserPoolDomainRequestRequestTypeDef",
    "DeleteUserPoolRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeIdentityProviderRequestRequestTypeDef",
    "DescribeResourceServerRequestRequestTypeDef",
    "DescribeRiskConfigurationRequestRequestTypeDef",
    "DescribeUserImportJobRequestRequestTypeDef",
    "DescribeUserPoolClientRequestRequestTypeDef",
    "DescribeUserPoolDomainRequestRequestTypeDef",
    "DescribeUserPoolRequestRequestTypeDef",
    "DeviceConfigurationTypeOutputTypeDef",
    "EmailConfigurationTypeOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ForgetDeviceRequestRequestTypeDef",
    "GetCSVHeaderRequestRequestTypeDef",
    "GetCSVHeaderResponseTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetIdentityProviderByIdentifierRequestRequestTypeDef",
    "GetSigningCertificateRequestRequestTypeDef",
    "GetSigningCertificateResponseTypeDef",
    "GetUICustomizationRequestRequestTypeDef",
    "UICustomizationTypeTypeDef",
    "GetUserAttributeVerificationCodeRequestRequestTypeDef",
    "GetUserPoolMfaConfigRequestRequestTypeDef",
    "SoftwareTokenMfaConfigTypeOutputTypeDef",
    "GetUserRequestRequestTypeDef",
    "GlobalSignOutRequestRequestTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ProviderDescriptionTypeDef",
    "ListResourceServersRequestListResourceServersPaginateTypeDef",
    "ListResourceServersRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserImportJobsRequestRequestTypeDef",
    "ListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef",
    "ListUserPoolClientsRequestRequestTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "ListUserPoolsRequestListUserPoolsPaginateTypeDef",
    "ListUserPoolsRequestRequestTypeDef",
    "ListUsersInGroupRequestListUsersInGroupPaginateTypeDef",
    "ListUsersInGroupRequestRequestTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListUsersRequestRequestTypeDef",
    "NotifyEmailTypeOutputTypeDef",
    "NotifyEmailTypeTypeDef",
    "NumberAttributeConstraintsTypeOutputTypeDef",
    "NumberAttributeConstraintsTypeTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeOutputTypeDef",
    "PasswordPolicyTypeTypeDef",
    "ResourceServerScopeTypeOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeTokenRequestRequestTypeDef",
    "RiskExceptionConfigurationTypeOutputTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "StringAttributeConstraintsTypeOutputTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "SetUICustomizationRequestRequestTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "SmsConfigurationTypeOutputTypeDef",
    "StartUserImportJobRequestRequestTypeDef",
    "StopUserImportJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TokenValidityUnitsTypeOutputTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAuthEventFeedbackRequestRequestTypeDef",
    "UpdateDeviceStatusRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UpdateUserPoolDomainResponseTypeDef",
    "UserAttributeUpdateSettingsTypeOutputTypeDef",
    "UserPoolAddOnsTypeOutputTypeDef",
    "UsernameConfigurationTypeOutputTypeDef",
    "VerificationMessageTemplateTypeOutputTypeDef",
    "VerifySoftwareTokenRequestRequestTypeDef",
    "VerifySoftwareTokenResponseTypeDef",
    "VerifyUserAttributeRequestRequestTypeDef",
    "AccountRecoverySettingTypeOutputTypeDef",
    "AccountRecoverySettingTypeTypeDef",
    "AccountTakeoverActionsTypeOutputTypeDef",
    "AccountTakeoverActionsTypeTypeDef",
    "AdminCreateUserConfigTypeOutputTypeDef",
    "AdminCreateUserConfigTypeTypeDef",
    "AdminCreateUserRequestRequestTypeDef",
    "AdminUpdateUserAttributesRequestRequestTypeDef",
    "UpdateUserAttributesRequestRequestTypeDef",
    "AdminDisableProviderForUserRequestRequestTypeDef",
    "AdminLinkProviderForUserRequestRequestTypeDef",
    "DeviceTypeTypeDef",
    "AdminGetUserResponseTypeDef",
    "GetUserResponseTypeDef",
    "UserTypeTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "GetGroupResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "UpdateGroupResponseTypeDef",
    "AdminSetUserMFAPreferenceRequestRequestTypeDef",
    "SetUserMFAPreferenceRequestRequestTypeDef",
    "AdminSetUserSettingsRequestRequestTypeDef",
    "SetUserSettingsRequestRequestTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "ForgotPasswordResponseTypeDef",
    "GetUserAttributeVerificationCodeResponseTypeDef",
    "ResendConfirmationCodeResponseTypeDef",
    "SignUpResponseTypeDef",
    "UpdateUserAttributesResponseTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeOutputTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "ConfirmDeviceRequestRequestTypeDef",
    "ConfirmForgotPasswordRequestRequestTypeDef",
    "ConfirmSignUpRequestRequestTypeDef",
    "ForgotPasswordRequestRequestTypeDef",
    "InitiateAuthRequestRequestTypeDef",
    "ResendConfirmationCodeRequestRequestTypeDef",
    "RespondToAuthChallengeRequestRequestTypeDef",
    "SignUpRequestRequestTypeDef",
    "ContextDataTypeTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "DescribeIdentityProviderResponseTypeDef",
    "GetIdentityProviderByIdentifierResponseTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "CreateResourceServerRequestRequestTypeDef",
    "UpdateResourceServerRequestRequestTypeDef",
    "CreateUserImportJobResponseTypeDef",
    "DescribeUserImportJobResponseTypeDef",
    "ListUserImportJobsResponseTypeDef",
    "StartUserImportJobResponseTypeDef",
    "StopUserImportJobResponseTypeDef",
    "CreateUserPoolClientRequestRequestTypeDef",
    "UpdateUserPoolClientRequestRequestTypeDef",
    "CreateUserPoolDomainRequestRequestTypeDef",
    "UpdateUserPoolDomainRequestRequestTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "DomainDescriptionTypeTypeDef",
    "LambdaConfigTypeOutputTypeDef",
    "LambdaConfigTypeTypeDef",
    "GetUICustomizationResponseTypeDef",
    "SetUICustomizationResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "NotifyConfigurationTypeOutputTypeDef",
    "NotifyConfigurationTypeTypeDef",
    "UserPoolPolicyTypeOutputTypeDef",
    "UserPoolPolicyTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "SchemaAttributeTypeOutputTypeDef",
    "SchemaAttributeTypeTypeDef",
    "SmsMfaConfigTypeOutputTypeDef",
    "UserPoolClientTypeTypeDef",
    "AdminGetDeviceResponseTypeDef",
    "AdminListDevicesResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "AdminCreateUserResponseTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "AdminInitiateAuthResponseTypeDef",
    "AdminRespondToAuthChallengeResponseTypeDef",
    "InitiateAuthResponseTypeDef",
    "RespondToAuthChallengeResponseTypeDef",
    "AdminInitiateAuthRequestRequestTypeDef",
    "AdminRespondToAuthChallengeRequestRequestTypeDef",
    "SetUserPoolMfaConfigRequestRequestTypeDef",
    "DescribeUserPoolDomainResponseTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "AccountTakeoverRiskConfigurationTypeOutputTypeDef",
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    "UpdateUserPoolRequestRequestTypeDef",
    "CreateResourceServerResponseTypeDef",
    "DescribeResourceServerResponseTypeDef",
    "ListResourceServersResponseTypeDef",
    "UpdateResourceServerResponseTypeDef",
    "UserPoolTypeTypeDef",
    "AddCustomAttributesRequestRequestTypeDef",
    "CreateUserPoolRequestRequestTypeDef",
    "GetUserPoolMfaConfigResponseTypeDef",
    "SetUserPoolMfaConfigResponseTypeDef",
    "CreateUserPoolClientResponseTypeDef",
    "DescribeUserPoolClientResponseTypeDef",
    "UpdateUserPoolClientResponseTypeDef",
    "ListUserPoolsResponseTypeDef",
    "RiskConfigurationTypeTypeDef",
    "SetRiskConfigurationRequestRequestTypeDef",
    "CreateUserPoolResponseTypeDef",
    "DescribeUserPoolResponseTypeDef",
    "DescribeRiskConfigurationResponseTypeDef",
    "SetRiskConfigurationResponseTypeDef",
)

RecoveryOptionTypeOutputTypeDef = TypedDict(
    "RecoveryOptionTypeOutputTypeDef",
    {
        "Priority": int,
        "Name": RecoveryOptionNameTypeType,
    },
)

RecoveryOptionTypeTypeDef = TypedDict(
    "RecoveryOptionTypeTypeDef",
    {
        "Priority": int,
        "Name": RecoveryOptionNameTypeType,
    },
)

AccountTakeoverActionTypeOutputTypeDef = TypedDict(
    "AccountTakeoverActionTypeOutputTypeDef",
    {
        "Notify": bool,
        "EventAction": AccountTakeoverEventActionTypeType,
    },
)

AccountTakeoverActionTypeTypeDef = TypedDict(
    "AccountTakeoverActionTypeTypeDef",
    {
        "Notify": bool,
        "EventAction": AccountTakeoverEventActionTypeType,
    },
)

AdminAddUserToGroupRequestRequestTypeDef = TypedDict(
    "AdminAddUserToGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)

_RequiredAdminConfirmSignUpRequestRequestTypeDef = TypedDict(
    "_RequiredAdminConfirmSignUpRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminConfirmSignUpRequestRequestTypeDef = TypedDict(
    "_OptionalAdminConfirmSignUpRequestRequestTypeDef",
    {
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class AdminConfirmSignUpRequestRequestTypeDef(
    _RequiredAdminConfirmSignUpRequestRequestTypeDef,
    _OptionalAdminConfirmSignUpRequestRequestTypeDef,
):
    pass

MessageTemplateTypeOutputTypeDef = TypedDict(
    "MessageTemplateTypeOutputTypeDef",
    {
        "SMSMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
    },
    total=False,
)

MessageTemplateTypeTypeDef = TypedDict(
    "MessageTemplateTypeTypeDef",
    {
        "SMSMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
    },
    total=False,
)

_RequiredAttributeTypeTypeDef = TypedDict(
    "_RequiredAttributeTypeTypeDef",
    {
        "Name": str,
    },
)
_OptionalAttributeTypeTypeDef = TypedDict(
    "_OptionalAttributeTypeTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class AttributeTypeTypeDef(_RequiredAttributeTypeTypeDef, _OptionalAttributeTypeTypeDef):
    pass

AdminDeleteUserAttributesRequestRequestTypeDef = TypedDict(
    "AdminDeleteUserAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributeNames": Sequence[str],
    },
)

AdminDeleteUserRequestRequestTypeDef = TypedDict(
    "AdminDeleteUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

ProviderUserIdentifierTypeTypeDef = TypedDict(
    "ProviderUserIdentifierTypeTypeDef",
    {
        "ProviderName": str,
        "ProviderAttributeName": str,
        "ProviderAttributeValue": str,
    },
    total=False,
)

AdminDisableUserRequestRequestTypeDef = TypedDict(
    "AdminDisableUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminEnableUserRequestRequestTypeDef = TypedDict(
    "AdminEnableUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminForgetDeviceRequestRequestTypeDef = TypedDict(
    "AdminForgetDeviceRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
    },
)

AdminGetDeviceRequestRequestTypeDef = TypedDict(
    "AdminGetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
        "UserPoolId": str,
        "Username": str,
    },
)

AdminGetUserRequestRequestTypeDef = TypedDict(
    "AdminGetUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

_RequiredAttributeTypeOutputTypeDef = TypedDict(
    "_RequiredAttributeTypeOutputTypeDef",
    {
        "Name": str,
    },
)
_OptionalAttributeTypeOutputTypeDef = TypedDict(
    "_OptionalAttributeTypeOutputTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class AttributeTypeOutputTypeDef(
    _RequiredAttributeTypeOutputTypeDef, _OptionalAttributeTypeOutputTypeDef
):
    pass

MFAOptionTypeOutputTypeDef = TypedDict(
    "MFAOptionTypeOutputTypeDef",
    {
        "DeliveryMedium": DeliveryMediumTypeType,
        "AttributeName": str,
    },
    total=False,
)

AnalyticsMetadataTypeTypeDef = TypedDict(
    "AnalyticsMetadataTypeTypeDef",
    {
        "AnalyticsEndpointId": str,
    },
    total=False,
)

_RequiredAdminListDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredAdminListDevicesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminListDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalAdminListDevicesRequestRequestTypeDef",
    {
        "Limit": int,
        "PaginationToken": str,
    },
    total=False,
)

class AdminListDevicesRequestRequestTypeDef(
    _RequiredAdminListDevicesRequestRequestTypeDef, _OptionalAdminListDevicesRequestRequestTypeDef
):
    pass

_RequiredAdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef = TypedDict(
    "_RequiredAdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
    },
)
_OptionalAdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef = TypedDict(
    "_OptionalAdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class AdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef(
    _RequiredAdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef,
    _OptionalAdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef,
):
    pass

_RequiredAdminListGroupsForUserRequestRequestTypeDef = TypedDict(
    "_RequiredAdminListGroupsForUserRequestRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
    },
)
_OptionalAdminListGroupsForUserRequestRequestTypeDef = TypedDict(
    "_OptionalAdminListGroupsForUserRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class AdminListGroupsForUserRequestRequestTypeDef(
    _RequiredAdminListGroupsForUserRequestRequestTypeDef,
    _OptionalAdminListGroupsForUserRequestRequestTypeDef,
):
    pass

GroupTypeTypeDef = TypedDict(
    "GroupTypeTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredAdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef = TypedDict(
    "_RequiredAdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef = TypedDict(
    "_OptionalAdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef(
    _RequiredAdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef,
    _OptionalAdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef,
):
    pass

_RequiredAdminListUserAuthEventsRequestRequestTypeDef = TypedDict(
    "_RequiredAdminListUserAuthEventsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminListUserAuthEventsRequestRequestTypeDef = TypedDict(
    "_OptionalAdminListUserAuthEventsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class AdminListUserAuthEventsRequestRequestTypeDef(
    _RequiredAdminListUserAuthEventsRequestRequestTypeDef,
    _OptionalAdminListUserAuthEventsRequestRequestTypeDef,
):
    pass

AdminRemoveUserFromGroupRequestRequestTypeDef = TypedDict(
    "AdminRemoveUserFromGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)

_RequiredAdminResetUserPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredAdminResetUserPasswordRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminResetUserPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalAdminResetUserPasswordRequestRequestTypeDef",
    {
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class AdminResetUserPasswordRequestRequestTypeDef(
    _RequiredAdminResetUserPasswordRequestRequestTypeDef,
    _OptionalAdminResetUserPasswordRequestRequestTypeDef,
):
    pass

SMSMfaSettingsTypeTypeDef = TypedDict(
    "SMSMfaSettingsTypeTypeDef",
    {
        "Enabled": bool,
        "PreferredMfa": bool,
    },
    total=False,
)

SoftwareTokenMfaSettingsTypeTypeDef = TypedDict(
    "SoftwareTokenMfaSettingsTypeTypeDef",
    {
        "Enabled": bool,
        "PreferredMfa": bool,
    },
    total=False,
)

_RequiredAdminSetUserPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredAdminSetUserPasswordRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "Password": str,
    },
)
_OptionalAdminSetUserPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalAdminSetUserPasswordRequestRequestTypeDef",
    {
        "Permanent": bool,
    },
    total=False,
)

class AdminSetUserPasswordRequestRequestTypeDef(
    _RequiredAdminSetUserPasswordRequestRequestTypeDef,
    _OptionalAdminSetUserPasswordRequestRequestTypeDef,
):
    pass

MFAOptionTypeTypeDef = TypedDict(
    "MFAOptionTypeTypeDef",
    {
        "DeliveryMedium": DeliveryMediumTypeType,
        "AttributeName": str,
    },
    total=False,
)

AdminUpdateAuthEventFeedbackRequestRequestTypeDef = TypedDict(
    "AdminUpdateAuthEventFeedbackRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)

_RequiredAdminUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "_RequiredAdminUpdateDeviceStatusRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
    },
)
_OptionalAdminUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "_OptionalAdminUpdateDeviceStatusRequestRequestTypeDef",
    {
        "DeviceRememberedStatus": DeviceRememberedStatusTypeType,
    },
    total=False,
)

class AdminUpdateDeviceStatusRequestRequestTypeDef(
    _RequiredAdminUpdateDeviceStatusRequestRequestTypeDef,
    _OptionalAdminUpdateDeviceStatusRequestRequestTypeDef,
):
    pass

AdminUserGlobalSignOutRequestRequestTypeDef = TypedDict(
    "AdminUserGlobalSignOutRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AnalyticsConfigurationTypeOutputTypeDef = TypedDict(
    "AnalyticsConfigurationTypeOutputTypeDef",
    {
        "ApplicationId": str,
        "ApplicationArn": str,
        "RoleArn": str,
        "ExternalId": str,
        "UserDataShared": bool,
    },
    total=False,
)

AnalyticsConfigurationTypeTypeDef = TypedDict(
    "AnalyticsConfigurationTypeTypeDef",
    {
        "ApplicationId": str,
        "ApplicationArn": str,
        "RoleArn": str,
        "ExternalId": str,
        "UserDataShared": bool,
    },
    total=False,
)

AssociateSoftwareTokenRequestRequestTypeDef = TypedDict(
    "AssociateSoftwareTokenRequestRequestTypeDef",
    {
        "AccessToken": str,
        "Session": str,
    },
    total=False,
)

AssociateSoftwareTokenResponseTypeDef = TypedDict(
    "AssociateSoftwareTokenResponseTypeDef",
    {
        "SecretCode": str,
        "Session": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChallengeResponseTypeTypeDef = TypedDict(
    "ChallengeResponseTypeTypeDef",
    {
        "ChallengeName": ChallengeNameType,
        "ChallengeResponse": ChallengeResponseType,
    },
    total=False,
)

EventContextDataTypeTypeDef = TypedDict(
    "EventContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "DeviceName": str,
        "Timezone": str,
        "City": str,
        "Country": str,
    },
    total=False,
)

_RequiredEventFeedbackTypeTypeDef = TypedDict(
    "_RequiredEventFeedbackTypeTypeDef",
    {
        "FeedbackValue": FeedbackValueTypeType,
        "Provider": str,
    },
)
_OptionalEventFeedbackTypeTypeDef = TypedDict(
    "_OptionalEventFeedbackTypeTypeDef",
    {
        "FeedbackDate": datetime,
    },
    total=False,
)

class EventFeedbackTypeTypeDef(
    _RequiredEventFeedbackTypeTypeDef, _OptionalEventFeedbackTypeTypeDef
):
    pass

EventRiskTypeTypeDef = TypedDict(
    "EventRiskTypeTypeDef",
    {
        "RiskDecision": RiskDecisionTypeType,
        "RiskLevel": RiskLevelTypeType,
        "CompromisedCredentialsDetected": bool,
    },
    total=False,
)

NewDeviceMetadataTypeTypeDef = TypedDict(
    "NewDeviceMetadataTypeTypeDef",
    {
        "DeviceKey": str,
        "DeviceGroupKey": str,
    },
    total=False,
)

ChangePasswordRequestRequestTypeDef = TypedDict(
    "ChangePasswordRequestRequestTypeDef",
    {
        "PreviousPassword": str,
        "ProposedPassword": str,
        "AccessToken": str,
    },
)

CodeDeliveryDetailsTypeTypeDef = TypedDict(
    "CodeDeliveryDetailsTypeTypeDef",
    {
        "Destination": str,
        "DeliveryMedium": DeliveryMediumTypeType,
        "AttributeName": str,
    },
    total=False,
)

CompromisedCredentialsActionsTypeOutputTypeDef = TypedDict(
    "CompromisedCredentialsActionsTypeOutputTypeDef",
    {
        "EventAction": CompromisedCredentialsEventActionTypeType,
    },
)

CompromisedCredentialsActionsTypeTypeDef = TypedDict(
    "CompromisedCredentialsActionsTypeTypeDef",
    {
        "EventAction": CompromisedCredentialsEventActionTypeType,
    },
)

DeviceSecretVerifierConfigTypeTypeDef = TypedDict(
    "DeviceSecretVerifierConfigTypeTypeDef",
    {
        "PasswordVerifier": str,
        "Salt": str,
    },
    total=False,
)

ConfirmDeviceResponseTypeDef = TypedDict(
    "ConfirmDeviceResponseTypeDef",
    {
        "UserConfirmationNecessary": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserContextDataTypeTypeDef = TypedDict(
    "UserContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "EncodedData": str,
    },
    total=False,
)

HttpHeaderTypeDef = TypedDict(
    "HttpHeaderTypeDef",
    {
        "headerName": str,
        "headerValue": str,
    },
    total=False,
)

_RequiredCreateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)
_OptionalCreateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestRequestTypeDef",
    {
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
    },
    total=False,
)

class CreateGroupRequestRequestTypeDef(
    _RequiredCreateGroupRequestRequestTypeDef, _OptionalCreateGroupRequestRequestTypeDef
):
    pass

_RequiredCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "ProviderDetails": Mapping[str, str],
    },
)
_OptionalCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIdentityProviderRequestRequestTypeDef",
    {
        "AttributeMapping": Mapping[str, str],
        "IdpIdentifiers": Sequence[str],
    },
    total=False,
)

class CreateIdentityProviderRequestRequestTypeDef(
    _RequiredCreateIdentityProviderRequestRequestTypeDef,
    _OptionalCreateIdentityProviderRequestRequestTypeDef,
):
    pass

IdentityProviderTypeTypeDef = TypedDict(
    "IdentityProviderTypeTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ResourceServerScopeTypeTypeDef = TypedDict(
    "ResourceServerScopeTypeTypeDef",
    {
        "ScopeName": str,
        "ScopeDescription": str,
    },
)

CreateUserImportJobRequestRequestTypeDef = TypedDict(
    "CreateUserImportJobRequestRequestTypeDef",
    {
        "JobName": str,
        "UserPoolId": str,
        "CloudWatchLogsRoleArn": str,
    },
)

UserImportJobTypeTypeDef = TypedDict(
    "UserImportJobTypeTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": UserImportJobStatusTypeType,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

TokenValidityUnitsTypeTypeDef = TypedDict(
    "TokenValidityUnitsTypeTypeDef",
    {
        "AccessToken": TimeUnitsTypeType,
        "IdToken": TimeUnitsTypeType,
        "RefreshToken": TimeUnitsTypeType,
    },
    total=False,
)

CustomDomainConfigTypeTypeDef = TypedDict(
    "CustomDomainConfigTypeTypeDef",
    {
        "CertificateArn": str,
    },
)

CreateUserPoolDomainResponseTypeDef = TypedDict(
    "CreateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceConfigurationTypeTypeDef = TypedDict(
    "DeviceConfigurationTypeTypeDef",
    {
        "ChallengeRequiredOnNewDevice": bool,
        "DeviceOnlyRememberedOnUserPrompt": bool,
    },
    total=False,
)

EmailConfigurationTypeTypeDef = TypedDict(
    "EmailConfigurationTypeTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": EmailSendingAccountTypeType,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

_RequiredSmsConfigurationTypeTypeDef = TypedDict(
    "_RequiredSmsConfigurationTypeTypeDef",
    {
        "SnsCallerArn": str,
    },
)
_OptionalSmsConfigurationTypeTypeDef = TypedDict(
    "_OptionalSmsConfigurationTypeTypeDef",
    {
        "ExternalId": str,
        "SnsRegion": str,
    },
    total=False,
)

class SmsConfigurationTypeTypeDef(
    _RequiredSmsConfigurationTypeTypeDef, _OptionalSmsConfigurationTypeTypeDef
):
    pass

UserAttributeUpdateSettingsTypeTypeDef = TypedDict(
    "UserAttributeUpdateSettingsTypeTypeDef",
    {
        "AttributesRequireVerificationBeforeUpdate": Sequence[VerifiedAttributeTypeType],
    },
    total=False,
)

UserPoolAddOnsTypeTypeDef = TypedDict(
    "UserPoolAddOnsTypeTypeDef",
    {
        "AdvancedSecurityMode": AdvancedSecurityModeTypeType,
    },
)

UsernameConfigurationTypeTypeDef = TypedDict(
    "UsernameConfigurationTypeTypeDef",
    {
        "CaseSensitive": bool,
    },
)

VerificationMessageTemplateTypeTypeDef = TypedDict(
    "VerificationMessageTemplateTypeTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": DefaultEmailOptionTypeType,
    },
    total=False,
)

CustomDomainConfigTypeOutputTypeDef = TypedDict(
    "CustomDomainConfigTypeOutputTypeDef",
    {
        "CertificateArn": str,
    },
)

CustomEmailLambdaVersionConfigTypeOutputTypeDef = TypedDict(
    "CustomEmailLambdaVersionConfigTypeOutputTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

CustomEmailLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

CustomSMSLambdaVersionConfigTypeOutputTypeDef = TypedDict(
    "CustomSMSLambdaVersionConfigTypeOutputTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

CustomSMSLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)

DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)

DeleteResourceServerRequestRequestTypeDef = TypedDict(
    "DeleteResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)

DeleteUserAttributesRequestRequestTypeDef = TypedDict(
    "DeleteUserAttributesRequestRequestTypeDef",
    {
        "UserAttributeNames": Sequence[str],
        "AccessToken": str,
    },
)

DeleteUserPoolClientRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)

DeleteUserPoolDomainRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
    },
)

DeleteUserPoolRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

DescribeIdentityProviderRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)

DescribeResourceServerRequestRequestTypeDef = TypedDict(
    "DescribeResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)

_RequiredDescribeRiskConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRiskConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalDescribeRiskConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRiskConfigurationRequestRequestTypeDef",
    {
        "ClientId": str,
    },
    total=False,
)

class DescribeRiskConfigurationRequestRequestTypeDef(
    _RequiredDescribeRiskConfigurationRequestRequestTypeDef,
    _OptionalDescribeRiskConfigurationRequestRequestTypeDef,
):
    pass

DescribeUserImportJobRequestRequestTypeDef = TypedDict(
    "DescribeUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

DescribeUserPoolClientRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)

DescribeUserPoolDomainRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
    },
)

DescribeUserPoolRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

DeviceConfigurationTypeOutputTypeDef = TypedDict(
    "DeviceConfigurationTypeOutputTypeDef",
    {
        "ChallengeRequiredOnNewDevice": bool,
        "DeviceOnlyRememberedOnUserPrompt": bool,
    },
    total=False,
)

EmailConfigurationTypeOutputTypeDef = TypedDict(
    "EmailConfigurationTypeOutputTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": EmailSendingAccountTypeType,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredForgetDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredForgetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
    },
)
_OptionalForgetDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalForgetDeviceRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
    total=False,
)

class ForgetDeviceRequestRequestTypeDef(
    _RequiredForgetDeviceRequestRequestTypeDef, _OptionalForgetDeviceRequestRequestTypeDef
):
    pass

GetCSVHeaderRequestRequestTypeDef = TypedDict(
    "GetCSVHeaderRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetCSVHeaderResponseTypeDef = TypedDict(
    "GetCSVHeaderResponseTypeDef",
    {
        "UserPoolId": str,
        "CSVHeader": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredGetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
    },
)
_OptionalGetDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalGetDeviceRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
    total=False,
)

class GetDeviceRequestRequestTypeDef(
    _RequiredGetDeviceRequestRequestTypeDef, _OptionalGetDeviceRequestRequestTypeDef
):
    pass

GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)

GetIdentityProviderByIdentifierRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "IdpIdentifier": str,
    },
)

GetSigningCertificateRequestRequestTypeDef = TypedDict(
    "GetSigningCertificateRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetSigningCertificateResponseTypeDef = TypedDict(
    "GetSigningCertificateResponseTypeDef",
    {
        "Certificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUICustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredGetUICustomizationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalGetUICustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalGetUICustomizationRequestRequestTypeDef",
    {
        "ClientId": str,
    },
    total=False,
)

class GetUICustomizationRequestRequestTypeDef(
    _RequiredGetUICustomizationRequestRequestTypeDef,
    _OptionalGetUICustomizationRequestRequestTypeDef,
):
    pass

UICustomizationTypeTypeDef = TypedDict(
    "UICustomizationTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredGetUserAttributeVerificationCodeRequestRequestTypeDef = TypedDict(
    "_RequiredGetUserAttributeVerificationCodeRequestRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
    },
)
_OptionalGetUserAttributeVerificationCodeRequestRequestTypeDef = TypedDict(
    "_OptionalGetUserAttributeVerificationCodeRequestRequestTypeDef",
    {
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class GetUserAttributeVerificationCodeRequestRequestTypeDef(
    _RequiredGetUserAttributeVerificationCodeRequestRequestTypeDef,
    _OptionalGetUserAttributeVerificationCodeRequestRequestTypeDef,
):
    pass

GetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "GetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

SoftwareTokenMfaConfigTypeOutputTypeDef = TypedDict(
    "SoftwareTokenMfaConfigTypeOutputTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

GlobalSignOutRequestRequestTypeDef = TypedDict(
    "GlobalSignOutRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

_RequiredListDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredListDevicesRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)
_OptionalListDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalListDevicesRequestRequestTypeDef",
    {
        "Limit": int,
        "PaginationToken": str,
    },
    total=False,
)

class ListDevicesRequestRequestTypeDef(
    _RequiredListDevicesRequestRequestTypeDef, _OptionalListDevicesRequestRequestTypeDef
):
    pass

_RequiredListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "_RequiredListGroupsRequestListGroupsPaginateTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "_OptionalListGroupsRequestListGroupsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListGroupsRequestListGroupsPaginateTypeDef(
    _RequiredListGroupsRequestListGroupsPaginateTypeDef,
    _OptionalListGroupsRequestListGroupsPaginateTypeDef,
):
    pass

_RequiredListGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class ListGroupsRequestRequestTypeDef(
    _RequiredListGroupsRequestRequestTypeDef, _OptionalListGroupsRequestRequestTypeDef
):
    pass

_RequiredListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef = TypedDict(
    "_RequiredListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef = TypedDict(
    "_OptionalListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef(
    _RequiredListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef,
    _OptionalListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef,
):
    pass

_RequiredListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_RequiredListIdentityProvidersRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_OptionalListIdentityProvidersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListIdentityProvidersRequestRequestTypeDef(
    _RequiredListIdentityProvidersRequestRequestTypeDef,
    _OptionalListIdentityProvidersRequestRequestTypeDef,
):
    pass

ProviderDescriptionTypeDef = TypedDict(
    "ProviderDescriptionTypeDef",
    {
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredListResourceServersRequestListResourceServersPaginateTypeDef = TypedDict(
    "_RequiredListResourceServersRequestListResourceServersPaginateTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListResourceServersRequestListResourceServersPaginateTypeDef = TypedDict(
    "_OptionalListResourceServersRequestListResourceServersPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListResourceServersRequestListResourceServersPaginateTypeDef(
    _RequiredListResourceServersRequestListResourceServersPaginateTypeDef,
    _OptionalListResourceServersRequestListResourceServersPaginateTypeDef,
):
    pass

_RequiredListResourceServersRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceServersRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListResourceServersRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceServersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListResourceServersRequestRequestTypeDef(
    _RequiredListResourceServersRequestRequestTypeDef,
    _OptionalListResourceServersRequestRequestTypeDef,
):
    pass

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserImportJobsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": int,
    },
)
_OptionalListUserImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserImportJobsRequestRequestTypeDef",
    {
        "PaginationToken": str,
    },
    total=False,
)

class ListUserImportJobsRequestRequestTypeDef(
    _RequiredListUserImportJobsRequestRequestTypeDef,
    _OptionalListUserImportJobsRequestRequestTypeDef,
):
    pass

_RequiredListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef = TypedDict(
    "_RequiredListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef = TypedDict(
    "_OptionalListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef(
    _RequiredListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef,
    _OptionalListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef,
):
    pass

_RequiredListUserPoolClientsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserPoolClientsRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListUserPoolClientsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserPoolClientsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListUserPoolClientsRequestRequestTypeDef(
    _RequiredListUserPoolClientsRequestRequestTypeDef,
    _OptionalListUserPoolClientsRequestRequestTypeDef,
):
    pass

UserPoolClientDescriptionTypeDef = TypedDict(
    "UserPoolClientDescriptionTypeDef",
    {
        "ClientId": str,
        "UserPoolId": str,
        "ClientName": str,
    },
    total=False,
)

ListUserPoolsRequestListUserPoolsPaginateTypeDef = TypedDict(
    "ListUserPoolsRequestListUserPoolsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

_RequiredListUserPoolsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserPoolsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListUserPoolsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserPoolsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListUserPoolsRequestRequestTypeDef(
    _RequiredListUserPoolsRequestRequestTypeDef, _OptionalListUserPoolsRequestRequestTypeDef
):
    pass

_RequiredListUsersInGroupRequestListUsersInGroupPaginateTypeDef = TypedDict(
    "_RequiredListUsersInGroupRequestListUsersInGroupPaginateTypeDef",
    {
        "UserPoolId": str,
        "GroupName": str,
    },
)
_OptionalListUsersInGroupRequestListUsersInGroupPaginateTypeDef = TypedDict(
    "_OptionalListUsersInGroupRequestListUsersInGroupPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListUsersInGroupRequestListUsersInGroupPaginateTypeDef(
    _RequiredListUsersInGroupRequestListUsersInGroupPaginateTypeDef,
    _OptionalListUsersInGroupRequestListUsersInGroupPaginateTypeDef,
):
    pass

_RequiredListUsersInGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersInGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "GroupName": str,
    },
)
_OptionalListUsersInGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersInGroupRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class ListUsersInGroupRequestRequestTypeDef(
    _RequiredListUsersInGroupRequestRequestTypeDef, _OptionalListUsersInGroupRequestRequestTypeDef
):
    pass

_RequiredListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "_RequiredListUsersRequestListUsersPaginateTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "_OptionalListUsersRequestListUsersPaginateTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "Filter": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListUsersRequestListUsersPaginateTypeDef(
    _RequiredListUsersRequestListUsersPaginateTypeDef,
    _OptionalListUsersRequestListUsersPaginateTypeDef,
):
    pass

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "AttributesToGet": Sequence[str],
        "Limit": int,
        "PaginationToken": str,
        "Filter": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

_RequiredNotifyEmailTypeOutputTypeDef = TypedDict(
    "_RequiredNotifyEmailTypeOutputTypeDef",
    {
        "Subject": str,
    },
)
_OptionalNotifyEmailTypeOutputTypeDef = TypedDict(
    "_OptionalNotifyEmailTypeOutputTypeDef",
    {
        "HtmlBody": str,
        "TextBody": str,
    },
    total=False,
)

class NotifyEmailTypeOutputTypeDef(
    _RequiredNotifyEmailTypeOutputTypeDef, _OptionalNotifyEmailTypeOutputTypeDef
):
    pass

_RequiredNotifyEmailTypeTypeDef = TypedDict(
    "_RequiredNotifyEmailTypeTypeDef",
    {
        "Subject": str,
    },
)
_OptionalNotifyEmailTypeTypeDef = TypedDict(
    "_OptionalNotifyEmailTypeTypeDef",
    {
        "HtmlBody": str,
        "TextBody": str,
    },
    total=False,
)

class NotifyEmailTypeTypeDef(_RequiredNotifyEmailTypeTypeDef, _OptionalNotifyEmailTypeTypeDef):
    pass

NumberAttributeConstraintsTypeOutputTypeDef = TypedDict(
    "NumberAttributeConstraintsTypeOutputTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
    total=False,
)

NumberAttributeConstraintsTypeTypeDef = TypedDict(
    "NumberAttributeConstraintsTypeTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
    total=False,
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

PasswordPolicyTypeOutputTypeDef = TypedDict(
    "PasswordPolicyTypeOutputTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

PasswordPolicyTypeTypeDef = TypedDict(
    "PasswordPolicyTypeTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

ResourceServerScopeTypeOutputTypeDef = TypedDict(
    "ResourceServerScopeTypeOutputTypeDef",
    {
        "ScopeName": str,
        "ScopeDescription": str,
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

_RequiredRevokeTokenRequestRequestTypeDef = TypedDict(
    "_RequiredRevokeTokenRequestRequestTypeDef",
    {
        "Token": str,
        "ClientId": str,
    },
)
_OptionalRevokeTokenRequestRequestTypeDef = TypedDict(
    "_OptionalRevokeTokenRequestRequestTypeDef",
    {
        "ClientSecret": str,
    },
    total=False,
)

class RevokeTokenRequestRequestTypeDef(
    _RequiredRevokeTokenRequestRequestTypeDef, _OptionalRevokeTokenRequestRequestTypeDef
):
    pass

RiskExceptionConfigurationTypeOutputTypeDef = TypedDict(
    "RiskExceptionConfigurationTypeOutputTypeDef",
    {
        "BlockedIPRangeList": List[str],
        "SkippedIPRangeList": List[str],
    },
    total=False,
)

RiskExceptionConfigurationTypeTypeDef = TypedDict(
    "RiskExceptionConfigurationTypeTypeDef",
    {
        "BlockedIPRangeList": Sequence[str],
        "SkippedIPRangeList": Sequence[str],
    },
    total=False,
)

StringAttributeConstraintsTypeOutputTypeDef = TypedDict(
    "StringAttributeConstraintsTypeOutputTypeDef",
    {
        "MinLength": str,
        "MaxLength": str,
    },
    total=False,
)

StringAttributeConstraintsTypeTypeDef = TypedDict(
    "StringAttributeConstraintsTypeTypeDef",
    {
        "MinLength": str,
        "MaxLength": str,
    },
    total=False,
)

_RequiredSetUICustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredSetUICustomizationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetUICustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalSetUICustomizationRequestRequestTypeDef",
    {
        "ClientId": str,
        "CSS": str,
        "ImageFile": Union[str, bytes, IO[Any], StreamingBody],
    },
    total=False,
)

class SetUICustomizationRequestRequestTypeDef(
    _RequiredSetUICustomizationRequestRequestTypeDef,
    _OptionalSetUICustomizationRequestRequestTypeDef,
):
    pass

SoftwareTokenMfaConfigTypeTypeDef = TypedDict(
    "SoftwareTokenMfaConfigTypeTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

_RequiredSmsConfigurationTypeOutputTypeDef = TypedDict(
    "_RequiredSmsConfigurationTypeOutputTypeDef",
    {
        "SnsCallerArn": str,
    },
)
_OptionalSmsConfigurationTypeOutputTypeDef = TypedDict(
    "_OptionalSmsConfigurationTypeOutputTypeDef",
    {
        "ExternalId": str,
        "SnsRegion": str,
    },
    total=False,
)

class SmsConfigurationTypeOutputTypeDef(
    _RequiredSmsConfigurationTypeOutputTypeDef, _OptionalSmsConfigurationTypeOutputTypeDef
):
    pass

StartUserImportJobRequestRequestTypeDef = TypedDict(
    "StartUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

StopUserImportJobRequestRequestTypeDef = TypedDict(
    "StopUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TokenValidityUnitsTypeOutputTypeDef = TypedDict(
    "TokenValidityUnitsTypeOutputTypeDef",
    {
        "AccessToken": TimeUnitsTypeType,
        "IdToken": TimeUnitsTypeType,
        "RefreshToken": TimeUnitsTypeType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAuthEventFeedbackRequestRequestTypeDef = TypedDict(
    "UpdateAuthEventFeedbackRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackToken": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)

_RequiredUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceStatusRequestRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
    },
)
_OptionalUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceStatusRequestRequestTypeDef",
    {
        "DeviceRememberedStatus": DeviceRememberedStatusTypeType,
    },
    total=False,
)

class UpdateDeviceStatusRequestRequestTypeDef(
    _RequiredUpdateDeviceStatusRequestRequestTypeDef,
    _OptionalUpdateDeviceStatusRequestRequestTypeDef,
):
    pass

_RequiredUpdateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)
_OptionalUpdateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestRequestTypeDef",
    {
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
    },
    total=False,
)

class UpdateGroupRequestRequestTypeDef(
    _RequiredUpdateGroupRequestRequestTypeDef, _OptionalUpdateGroupRequestRequestTypeDef
):
    pass

_RequiredUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)
_OptionalUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentityProviderRequestRequestTypeDef",
    {
        "ProviderDetails": Mapping[str, str],
        "AttributeMapping": Mapping[str, str],
        "IdpIdentifiers": Sequence[str],
    },
    total=False,
)

class UpdateIdentityProviderRequestRequestTypeDef(
    _RequiredUpdateIdentityProviderRequestRequestTypeDef,
    _OptionalUpdateIdentityProviderRequestRequestTypeDef,
):
    pass

UpdateUserPoolDomainResponseTypeDef = TypedDict(
    "UpdateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserAttributeUpdateSettingsTypeOutputTypeDef = TypedDict(
    "UserAttributeUpdateSettingsTypeOutputTypeDef",
    {
        "AttributesRequireVerificationBeforeUpdate": List[VerifiedAttributeTypeType],
    },
    total=False,
)

UserPoolAddOnsTypeOutputTypeDef = TypedDict(
    "UserPoolAddOnsTypeOutputTypeDef",
    {
        "AdvancedSecurityMode": AdvancedSecurityModeTypeType,
    },
)

UsernameConfigurationTypeOutputTypeDef = TypedDict(
    "UsernameConfigurationTypeOutputTypeDef",
    {
        "CaseSensitive": bool,
    },
)

VerificationMessageTemplateTypeOutputTypeDef = TypedDict(
    "VerificationMessageTemplateTypeOutputTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": DefaultEmailOptionTypeType,
    },
    total=False,
)

_RequiredVerifySoftwareTokenRequestRequestTypeDef = TypedDict(
    "_RequiredVerifySoftwareTokenRequestRequestTypeDef",
    {
        "UserCode": str,
    },
)
_OptionalVerifySoftwareTokenRequestRequestTypeDef = TypedDict(
    "_OptionalVerifySoftwareTokenRequestRequestTypeDef",
    {
        "AccessToken": str,
        "Session": str,
        "FriendlyDeviceName": str,
    },
    total=False,
)

class VerifySoftwareTokenRequestRequestTypeDef(
    _RequiredVerifySoftwareTokenRequestRequestTypeDef,
    _OptionalVerifySoftwareTokenRequestRequestTypeDef,
):
    pass

VerifySoftwareTokenResponseTypeDef = TypedDict(
    "VerifySoftwareTokenResponseTypeDef",
    {
        "Status": VerifySoftwareTokenResponseTypeType,
        "Session": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyUserAttributeRequestRequestTypeDef = TypedDict(
    "VerifyUserAttributeRequestRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
        "Code": str,
    },
)

AccountRecoverySettingTypeOutputTypeDef = TypedDict(
    "AccountRecoverySettingTypeOutputTypeDef",
    {
        "RecoveryMechanisms": List[RecoveryOptionTypeOutputTypeDef],
    },
    total=False,
)

AccountRecoverySettingTypeTypeDef = TypedDict(
    "AccountRecoverySettingTypeTypeDef",
    {
        "RecoveryMechanisms": Sequence[RecoveryOptionTypeTypeDef],
    },
    total=False,
)

AccountTakeoverActionsTypeOutputTypeDef = TypedDict(
    "AccountTakeoverActionsTypeOutputTypeDef",
    {
        "LowAction": AccountTakeoverActionTypeOutputTypeDef,
        "MediumAction": AccountTakeoverActionTypeOutputTypeDef,
        "HighAction": AccountTakeoverActionTypeOutputTypeDef,
    },
    total=False,
)

AccountTakeoverActionsTypeTypeDef = TypedDict(
    "AccountTakeoverActionsTypeTypeDef",
    {
        "LowAction": AccountTakeoverActionTypeTypeDef,
        "MediumAction": AccountTakeoverActionTypeTypeDef,
        "HighAction": AccountTakeoverActionTypeTypeDef,
    },
    total=False,
)

AdminCreateUserConfigTypeOutputTypeDef = TypedDict(
    "AdminCreateUserConfigTypeOutputTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": MessageTemplateTypeOutputTypeDef,
    },
    total=False,
)

AdminCreateUserConfigTypeTypeDef = TypedDict(
    "AdminCreateUserConfigTypeTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": MessageTemplateTypeTypeDef,
    },
    total=False,
)

_RequiredAdminCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredAdminCreateUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalAdminCreateUserRequestRequestTypeDef",
    {
        "UserAttributes": Sequence[AttributeTypeTypeDef],
        "ValidationData": Sequence[AttributeTypeTypeDef],
        "TemporaryPassword": str,
        "ForceAliasCreation": bool,
        "MessageAction": MessageActionTypeType,
        "DesiredDeliveryMediums": Sequence[DeliveryMediumTypeType],
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class AdminCreateUserRequestRequestTypeDef(
    _RequiredAdminCreateUserRequestRequestTypeDef, _OptionalAdminCreateUserRequestRequestTypeDef
):
    pass

_RequiredAdminUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredAdminUpdateUserAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributes": Sequence[AttributeTypeTypeDef],
    },
)
_OptionalAdminUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalAdminUpdateUserAttributesRequestRequestTypeDef",
    {
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class AdminUpdateUserAttributesRequestRequestTypeDef(
    _RequiredAdminUpdateUserAttributesRequestRequestTypeDef,
    _OptionalAdminUpdateUserAttributesRequestRequestTypeDef,
):
    pass

_RequiredUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserAttributesRequestRequestTypeDef",
    {
        "UserAttributes": Sequence[AttributeTypeTypeDef],
        "AccessToken": str,
    },
)
_OptionalUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserAttributesRequestRequestTypeDef",
    {
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class UpdateUserAttributesRequestRequestTypeDef(
    _RequiredUpdateUserAttributesRequestRequestTypeDef,
    _OptionalUpdateUserAttributesRequestRequestTypeDef,
):
    pass

AdminDisableProviderForUserRequestRequestTypeDef = TypedDict(
    "AdminDisableProviderForUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "User": ProviderUserIdentifierTypeTypeDef,
    },
)

AdminLinkProviderForUserRequestRequestTypeDef = TypedDict(
    "AdminLinkProviderForUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "DestinationUser": ProviderUserIdentifierTypeTypeDef,
        "SourceUser": ProviderUserIdentifierTypeTypeDef,
    },
)

DeviceTypeTypeDef = TypedDict(
    "DeviceTypeTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[AttributeTypeOutputTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)

AdminGetUserResponseTypeDef = TypedDict(
    "AdminGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[AttributeTypeOutputTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List[MFAOptionTypeOutputTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[AttributeTypeOutputTypeDef],
        "MFAOptions": List[MFAOptionTypeOutputTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserTypeTypeDef = TypedDict(
    "UserTypeTypeDef",
    {
        "Username": str,
        "Attributes": List[AttributeTypeOutputTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List[MFAOptionTypeOutputTypeDef],
    },
    total=False,
)

AdminListGroupsForUserResponseTypeDef = TypedDict(
    "AdminListGroupsForUserResponseTypeDef",
    {
        "Groups": List[GroupTypeTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": GroupTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": GroupTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List[GroupTypeTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": GroupTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "_RequiredAdminSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
    },
)
_OptionalAdminSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "_OptionalAdminSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "SMSMfaSettings": SMSMfaSettingsTypeTypeDef,
        "SoftwareTokenMfaSettings": SoftwareTokenMfaSettingsTypeTypeDef,
    },
    total=False,
)

class AdminSetUserMFAPreferenceRequestRequestTypeDef(
    _RequiredAdminSetUserMFAPreferenceRequestRequestTypeDef,
    _OptionalAdminSetUserMFAPreferenceRequestRequestTypeDef,
):
    pass

_RequiredSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "_RequiredSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)
_OptionalSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "_OptionalSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "SMSMfaSettings": SMSMfaSettingsTypeTypeDef,
        "SoftwareTokenMfaSettings": SoftwareTokenMfaSettingsTypeTypeDef,
    },
    total=False,
)

class SetUserMFAPreferenceRequestRequestTypeDef(
    _RequiredSetUserMFAPreferenceRequestRequestTypeDef,
    _OptionalSetUserMFAPreferenceRequestRequestTypeDef,
):
    pass

AdminSetUserSettingsRequestRequestTypeDef = TypedDict(
    "AdminSetUserSettingsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "MFAOptions": Sequence[MFAOptionTypeTypeDef],
    },
)

SetUserSettingsRequestRequestTypeDef = TypedDict(
    "SetUserSettingsRequestRequestTypeDef",
    {
        "AccessToken": str,
        "MFAOptions": Sequence[MFAOptionTypeTypeDef],
    },
)

AuthEventTypeTypeDef = TypedDict(
    "AuthEventTypeTypeDef",
    {
        "EventId": str,
        "EventType": EventTypeType,
        "CreationDate": datetime,
        "EventResponse": EventResponseTypeType,
        "EventRisk": EventRiskTypeTypeDef,
        "ChallengeResponses": List[ChallengeResponseTypeTypeDef],
        "EventContextData": EventContextDataTypeTypeDef,
        "EventFeedback": EventFeedbackTypeTypeDef,
    },
    total=False,
)

AuthenticationResultTypeTypeDef = TypedDict(
    "AuthenticationResultTypeTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": NewDeviceMetadataTypeTypeDef,
    },
    total=False,
)

ForgotPasswordResponseTypeDef = TypedDict(
    "ForgotPasswordResponseTypeDef",
    {
        "CodeDeliveryDetails": CodeDeliveryDetailsTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": CodeDeliveryDetailsTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResendConfirmationCodeResponseTypeDef = TypedDict(
    "ResendConfirmationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": CodeDeliveryDetailsTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SignUpResponseTypeDef = TypedDict(
    "SignUpResponseTypeDef",
    {
        "UserConfirmed": bool,
        "CodeDeliveryDetails": CodeDeliveryDetailsTypeTypeDef,
        "UserSub": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserAttributesResponseTypeDef = TypedDict(
    "UpdateUserAttributesResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List[CodeDeliveryDetailsTypeTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCompromisedCredentialsRiskConfigurationTypeOutputTypeDef = TypedDict(
    "_RequiredCompromisedCredentialsRiskConfigurationTypeOutputTypeDef",
    {
        "Actions": CompromisedCredentialsActionsTypeOutputTypeDef,
    },
)
_OptionalCompromisedCredentialsRiskConfigurationTypeOutputTypeDef = TypedDict(
    "_OptionalCompromisedCredentialsRiskConfigurationTypeOutputTypeDef",
    {
        "EventFilter": List[EventFilterTypeType],
    },
    total=False,
)

class CompromisedCredentialsRiskConfigurationTypeOutputTypeDef(
    _RequiredCompromisedCredentialsRiskConfigurationTypeOutputTypeDef,
    _OptionalCompromisedCredentialsRiskConfigurationTypeOutputTypeDef,
):
    pass

_RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "_RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef",
    {
        "Actions": CompromisedCredentialsActionsTypeTypeDef,
    },
)
_OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "_OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef",
    {
        "EventFilter": Sequence[EventFilterTypeType],
    },
    total=False,
)

class CompromisedCredentialsRiskConfigurationTypeTypeDef(
    _RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef,
    _OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef,
):
    pass

_RequiredConfirmDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredConfirmDeviceRequestRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
    },
)
_OptionalConfirmDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalConfirmDeviceRequestRequestTypeDef",
    {
        "DeviceSecretVerifierConfig": DeviceSecretVerifierConfigTypeTypeDef,
        "DeviceName": str,
    },
    total=False,
)

class ConfirmDeviceRequestRequestTypeDef(
    _RequiredConfirmDeviceRequestRequestTypeDef, _OptionalConfirmDeviceRequestRequestTypeDef
):
    pass

_RequiredConfirmForgotPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredConfirmForgotPasswordRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
        "Password": str,
    },
)
_OptionalConfirmForgotPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalConfirmForgotPasswordRequestRequestTypeDef",
    {
        "SecretHash": str,
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "UserContextData": UserContextDataTypeTypeDef,
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class ConfirmForgotPasswordRequestRequestTypeDef(
    _RequiredConfirmForgotPasswordRequestRequestTypeDef,
    _OptionalConfirmForgotPasswordRequestRequestTypeDef,
):
    pass

_RequiredConfirmSignUpRequestRequestTypeDef = TypedDict(
    "_RequiredConfirmSignUpRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
    },
)
_OptionalConfirmSignUpRequestRequestTypeDef = TypedDict(
    "_OptionalConfirmSignUpRequestRequestTypeDef",
    {
        "SecretHash": str,
        "ForceAliasCreation": bool,
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "UserContextData": UserContextDataTypeTypeDef,
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class ConfirmSignUpRequestRequestTypeDef(
    _RequiredConfirmSignUpRequestRequestTypeDef, _OptionalConfirmSignUpRequestRequestTypeDef
):
    pass

_RequiredForgotPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredForgotPasswordRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
    },
)
_OptionalForgotPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalForgotPasswordRequestRequestTypeDef",
    {
        "SecretHash": str,
        "UserContextData": UserContextDataTypeTypeDef,
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class ForgotPasswordRequestRequestTypeDef(
    _RequiredForgotPasswordRequestRequestTypeDef, _OptionalForgotPasswordRequestRequestTypeDef
):
    pass

_RequiredInitiateAuthRequestRequestTypeDef = TypedDict(
    "_RequiredInitiateAuthRequestRequestTypeDef",
    {
        "AuthFlow": AuthFlowTypeType,
        "ClientId": str,
    },
)
_OptionalInitiateAuthRequestRequestTypeDef = TypedDict(
    "_OptionalInitiateAuthRequestRequestTypeDef",
    {
        "AuthParameters": Mapping[str, str],
        "ClientMetadata": Mapping[str, str],
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "UserContextData": UserContextDataTypeTypeDef,
    },
    total=False,
)

class InitiateAuthRequestRequestTypeDef(
    _RequiredInitiateAuthRequestRequestTypeDef, _OptionalInitiateAuthRequestRequestTypeDef
):
    pass

_RequiredResendConfirmationCodeRequestRequestTypeDef = TypedDict(
    "_RequiredResendConfirmationCodeRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
    },
)
_OptionalResendConfirmationCodeRequestRequestTypeDef = TypedDict(
    "_OptionalResendConfirmationCodeRequestRequestTypeDef",
    {
        "SecretHash": str,
        "UserContextData": UserContextDataTypeTypeDef,
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class ResendConfirmationCodeRequestRequestTypeDef(
    _RequiredResendConfirmationCodeRequestRequestTypeDef,
    _OptionalResendConfirmationCodeRequestRequestTypeDef,
):
    pass

_RequiredRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "_RequiredRespondToAuthChallengeRequestRequestTypeDef",
    {
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
    },
)
_OptionalRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "_OptionalRespondToAuthChallengeRequestRequestTypeDef",
    {
        "Session": str,
        "ChallengeResponses": Mapping[str, str],
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "UserContextData": UserContextDataTypeTypeDef,
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class RespondToAuthChallengeRequestRequestTypeDef(
    _RequiredRespondToAuthChallengeRequestRequestTypeDef,
    _OptionalRespondToAuthChallengeRequestRequestTypeDef,
):
    pass

_RequiredSignUpRequestRequestTypeDef = TypedDict(
    "_RequiredSignUpRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "Password": str,
    },
)
_OptionalSignUpRequestRequestTypeDef = TypedDict(
    "_OptionalSignUpRequestRequestTypeDef",
    {
        "SecretHash": str,
        "UserAttributes": Sequence[AttributeTypeTypeDef],
        "ValidationData": Sequence[AttributeTypeTypeDef],
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "UserContextData": UserContextDataTypeTypeDef,
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class SignUpRequestRequestTypeDef(
    _RequiredSignUpRequestRequestTypeDef, _OptionalSignUpRequestRequestTypeDef
):
    pass

_RequiredContextDataTypeTypeDef = TypedDict(
    "_RequiredContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": Sequence[HttpHeaderTypeDef],
    },
)
_OptionalContextDataTypeTypeDef = TypedDict(
    "_OptionalContextDataTypeTypeDef",
    {
        "EncodedData": str,
    },
    total=False,
)

class ContextDataTypeTypeDef(_RequiredContextDataTypeTypeDef, _OptionalContextDataTypeTypeDef):
    pass

CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityProviderResponseTypeDef = TypedDict(
    "DescribeIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierResponseTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceServerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
    },
)
_OptionalCreateResourceServerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResourceServerRequestRequestTypeDef",
    {
        "Scopes": Sequence[ResourceServerScopeTypeTypeDef],
    },
    total=False,
)

class CreateResourceServerRequestRequestTypeDef(
    _RequiredCreateResourceServerRequestRequestTypeDef,
    _OptionalCreateResourceServerRequestRequestTypeDef,
):
    pass

_RequiredUpdateResourceServerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
    },
)
_OptionalUpdateResourceServerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceServerRequestRequestTypeDef",
    {
        "Scopes": Sequence[ResourceServerScopeTypeTypeDef],
    },
    total=False,
)

class UpdateResourceServerRequestRequestTypeDef(
    _RequiredUpdateResourceServerRequestRequestTypeDef,
    _OptionalUpdateResourceServerRequestRequestTypeDef,
):
    pass

CreateUserImportJobResponseTypeDef = TypedDict(
    "CreateUserImportJobResponseTypeDef",
    {
        "UserImportJob": UserImportJobTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserImportJobResponseTypeDef = TypedDict(
    "DescribeUserImportJobResponseTypeDef",
    {
        "UserImportJob": UserImportJobTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserImportJobsResponseTypeDef = TypedDict(
    "ListUserImportJobsResponseTypeDef",
    {
        "UserImportJobs": List[UserImportJobTypeTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartUserImportJobResponseTypeDef = TypedDict(
    "StartUserImportJobResponseTypeDef",
    {
        "UserImportJob": UserImportJobTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopUserImportJobResponseTypeDef = TypedDict(
    "StopUserImportJobResponseTypeDef",
    {
        "UserImportJob": UserImportJobTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserPoolClientRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
    },
)
_OptionalCreateUserPoolClientRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolClientRequestRequestTypeDef",
    {
        "GenerateSecret": bool,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": TokenValidityUnitsTypeTypeDef,
        "ReadAttributes": Sequence[str],
        "WriteAttributes": Sequence[str],
        "ExplicitAuthFlows": Sequence[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": Sequence[str],
        "CallbackURLs": Sequence[str],
        "LogoutURLs": Sequence[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": Sequence[OAuthFlowTypeType],
        "AllowedOAuthScopes": Sequence[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": AnalyticsConfigurationTypeTypeDef,
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
        "EnablePropagateAdditionalUserContextData": bool,
        "AuthSessionValidity": int,
    },
    total=False,
)

class CreateUserPoolClientRequestRequestTypeDef(
    _RequiredCreateUserPoolClientRequestRequestTypeDef,
    _OptionalCreateUserPoolClientRequestRequestTypeDef,
):
    pass

_RequiredUpdateUserPoolClientRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)
_OptionalUpdateUserPoolClientRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserPoolClientRequestRequestTypeDef",
    {
        "ClientName": str,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": TokenValidityUnitsTypeTypeDef,
        "ReadAttributes": Sequence[str],
        "WriteAttributes": Sequence[str],
        "ExplicitAuthFlows": Sequence[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": Sequence[str],
        "CallbackURLs": Sequence[str],
        "LogoutURLs": Sequence[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": Sequence[OAuthFlowTypeType],
        "AllowedOAuthScopes": Sequence[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": AnalyticsConfigurationTypeTypeDef,
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
        "EnablePropagateAdditionalUserContextData": bool,
        "AuthSessionValidity": int,
    },
    total=False,
)

class UpdateUserPoolClientRequestRequestTypeDef(
    _RequiredUpdateUserPoolClientRequestRequestTypeDef,
    _OptionalUpdateUserPoolClientRequestRequestTypeDef,
):
    pass

_RequiredCreateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
    },
)
_OptionalCreateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolDomainRequestRequestTypeDef",
    {
        "CustomDomainConfig": CustomDomainConfigTypeTypeDef,
    },
    total=False,
)

class CreateUserPoolDomainRequestRequestTypeDef(
    _RequiredCreateUserPoolDomainRequestRequestTypeDef,
    _OptionalCreateUserPoolDomainRequestRequestTypeDef,
):
    pass

UpdateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "UpdateUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
        "CustomDomainConfig": CustomDomainConfigTypeTypeDef,
    },
)

SmsMfaConfigTypeTypeDef = TypedDict(
    "SmsMfaConfigTypeTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": SmsConfigurationTypeTypeDef,
    },
    total=False,
)

DomainDescriptionTypeTypeDef = TypedDict(
    "DomainDescriptionTypeTypeDef",
    {
        "UserPoolId": str,
        "AWSAccountId": str,
        "Domain": str,
        "S3Bucket": str,
        "CloudFrontDistribution": str,
        "Version": str,
        "Status": DomainStatusTypeType,
        "CustomDomainConfig": CustomDomainConfigTypeOutputTypeDef,
    },
    total=False,
)

LambdaConfigTypeOutputTypeDef = TypedDict(
    "LambdaConfigTypeOutputTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
        "CustomSMSSender": CustomSMSLambdaVersionConfigTypeOutputTypeDef,
        "CustomEmailSender": CustomEmailLambdaVersionConfigTypeOutputTypeDef,
        "KMSKeyID": str,
    },
    total=False,
)

LambdaConfigTypeTypeDef = TypedDict(
    "LambdaConfigTypeTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
        "CustomSMSSender": CustomSMSLambdaVersionConfigTypeTypeDef,
        "CustomEmailSender": CustomEmailLambdaVersionConfigTypeTypeDef,
        "KMSKeyID": str,
    },
    total=False,
)

GetUICustomizationResponseTypeDef = TypedDict(
    "GetUICustomizationResponseTypeDef",
    {
        "UICustomization": UICustomizationTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetUICustomizationResponseTypeDef = TypedDict(
    "SetUICustomizationResponseTypeDef",
    {
        "UICustomization": UICustomizationTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "Providers": List[ProviderDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserPoolClientsResponseTypeDef = TypedDict(
    "ListUserPoolClientsResponseTypeDef",
    {
        "UserPoolClients": List[UserPoolClientDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNotifyConfigurationTypeOutputTypeDef = TypedDict(
    "_RequiredNotifyConfigurationTypeOutputTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalNotifyConfigurationTypeOutputTypeDef = TypedDict(
    "_OptionalNotifyConfigurationTypeOutputTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "BlockEmail": NotifyEmailTypeOutputTypeDef,
        "NoActionEmail": NotifyEmailTypeOutputTypeDef,
        "MfaEmail": NotifyEmailTypeOutputTypeDef,
    },
    total=False,
)

class NotifyConfigurationTypeOutputTypeDef(
    _RequiredNotifyConfigurationTypeOutputTypeDef, _OptionalNotifyConfigurationTypeOutputTypeDef
):
    pass

_RequiredNotifyConfigurationTypeTypeDef = TypedDict(
    "_RequiredNotifyConfigurationTypeTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalNotifyConfigurationTypeTypeDef = TypedDict(
    "_OptionalNotifyConfigurationTypeTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "BlockEmail": NotifyEmailTypeTypeDef,
        "NoActionEmail": NotifyEmailTypeTypeDef,
        "MfaEmail": NotifyEmailTypeTypeDef,
    },
    total=False,
)

class NotifyConfigurationTypeTypeDef(
    _RequiredNotifyConfigurationTypeTypeDef, _OptionalNotifyConfigurationTypeTypeDef
):
    pass

UserPoolPolicyTypeOutputTypeDef = TypedDict(
    "UserPoolPolicyTypeOutputTypeDef",
    {
        "PasswordPolicy": PasswordPolicyTypeOutputTypeDef,
    },
    total=False,
)

UserPoolPolicyTypeTypeDef = TypedDict(
    "UserPoolPolicyTypeTypeDef",
    {
        "PasswordPolicy": PasswordPolicyTypeTypeDef,
    },
    total=False,
)

ResourceServerTypeTypeDef = TypedDict(
    "ResourceServerTypeTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ResourceServerScopeTypeOutputTypeDef],
    },
    total=False,
)

SchemaAttributeTypeOutputTypeDef = TypedDict(
    "SchemaAttributeTypeOutputTypeDef",
    {
        "Name": str,
        "AttributeDataType": AttributeDataTypeType,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": NumberAttributeConstraintsTypeOutputTypeDef,
        "StringAttributeConstraints": StringAttributeConstraintsTypeOutputTypeDef,
    },
    total=False,
)

SchemaAttributeTypeTypeDef = TypedDict(
    "SchemaAttributeTypeTypeDef",
    {
        "Name": str,
        "AttributeDataType": AttributeDataTypeType,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": NumberAttributeConstraintsTypeTypeDef,
        "StringAttributeConstraints": StringAttributeConstraintsTypeTypeDef,
    },
    total=False,
)

SmsMfaConfigTypeOutputTypeDef = TypedDict(
    "SmsMfaConfigTypeOutputTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": SmsConfigurationTypeOutputTypeDef,
    },
    total=False,
)

UserPoolClientTypeTypeDef = TypedDict(
    "UserPoolClientTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": TokenValidityUnitsTypeOutputTypeDef,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[OAuthFlowTypeType],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": AnalyticsConfigurationTypeOutputTypeDef,
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
        "EnablePropagateAdditionalUserContextData": bool,
        "AuthSessionValidity": int,
    },
    total=False,
)

AdminGetDeviceResponseTypeDef = TypedDict(
    "AdminGetDeviceResponseTypeDef",
    {
        "Device": DeviceTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminListDevicesResponseTypeDef = TypedDict(
    "AdminListDevicesResponseTypeDef",
    {
        "Devices": List[DeviceTypeTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "Device": DeviceTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List[DeviceTypeTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminCreateUserResponseTypeDef = TypedDict(
    "AdminCreateUserResponseTypeDef",
    {
        "User": UserTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersInGroupResponseTypeDef = TypedDict(
    "ListUsersInGroupResponseTypeDef",
    {
        "Users": List[UserTypeTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List[UserTypeTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminListUserAuthEventsResponseTypeDef = TypedDict(
    "AdminListUserAuthEventsResponseTypeDef",
    {
        "AuthEvents": List[AuthEventTypeTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminInitiateAuthResponseTypeDef = TypedDict(
    "AdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": AuthenticationResultTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "AdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": AuthenticationResultTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitiateAuthResponseTypeDef = TypedDict(
    "InitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": AuthenticationResultTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RespondToAuthChallengeResponseTypeDef = TypedDict(
    "RespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": AuthenticationResultTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminInitiateAuthRequestRequestTypeDef = TypedDict(
    "_RequiredAdminInitiateAuthRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "AuthFlow": AuthFlowTypeType,
    },
)
_OptionalAdminInitiateAuthRequestRequestTypeDef = TypedDict(
    "_OptionalAdminInitiateAuthRequestRequestTypeDef",
    {
        "AuthParameters": Mapping[str, str],
        "ClientMetadata": Mapping[str, str],
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "ContextData": ContextDataTypeTypeDef,
    },
    total=False,
)

class AdminInitiateAuthRequestRequestTypeDef(
    _RequiredAdminInitiateAuthRequestRequestTypeDef, _OptionalAdminInitiateAuthRequestRequestTypeDef
):
    pass

_RequiredAdminRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "_RequiredAdminRespondToAuthChallengeRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
    },
)
_OptionalAdminRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "_OptionalAdminRespondToAuthChallengeRequestRequestTypeDef",
    {
        "ChallengeResponses": Mapping[str, str],
        "Session": str,
        "AnalyticsMetadata": AnalyticsMetadataTypeTypeDef,
        "ContextData": ContextDataTypeTypeDef,
        "ClientMetadata": Mapping[str, str],
    },
    total=False,
)

class AdminRespondToAuthChallengeRequestRequestTypeDef(
    _RequiredAdminRespondToAuthChallengeRequestRequestTypeDef,
    _OptionalAdminRespondToAuthChallengeRequestRequestTypeDef,
):
    pass

_RequiredSetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "_RequiredSetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "_OptionalSetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "SmsMfaConfiguration": SmsMfaConfigTypeTypeDef,
        "SoftwareTokenMfaConfiguration": SoftwareTokenMfaConfigTypeTypeDef,
        "MfaConfiguration": UserPoolMfaTypeType,
    },
    total=False,
)

class SetUserPoolMfaConfigRequestRequestTypeDef(
    _RequiredSetUserPoolMfaConfigRequestRequestTypeDef,
    _OptionalSetUserPoolMfaConfigRequestRequestTypeDef,
):
    pass

DescribeUserPoolDomainResponseTypeDef = TypedDict(
    "DescribeUserPoolDomainResponseTypeDef",
    {
        "DomainDescription": DomainDescriptionTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserPoolDescriptionTypeTypeDef = TypedDict(
    "UserPoolDescriptionTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": LambdaConfigTypeOutputTypeDef,
        "Status": StatusTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredAccountTakeoverRiskConfigurationTypeOutputTypeDef = TypedDict(
    "_RequiredAccountTakeoverRiskConfigurationTypeOutputTypeDef",
    {
        "Actions": AccountTakeoverActionsTypeOutputTypeDef,
    },
)
_OptionalAccountTakeoverRiskConfigurationTypeOutputTypeDef = TypedDict(
    "_OptionalAccountTakeoverRiskConfigurationTypeOutputTypeDef",
    {
        "NotifyConfiguration": NotifyConfigurationTypeOutputTypeDef,
    },
    total=False,
)

class AccountTakeoverRiskConfigurationTypeOutputTypeDef(
    _RequiredAccountTakeoverRiskConfigurationTypeOutputTypeDef,
    _OptionalAccountTakeoverRiskConfigurationTypeOutputTypeDef,
):
    pass

_RequiredAccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "_RequiredAccountTakeoverRiskConfigurationTypeTypeDef",
    {
        "Actions": AccountTakeoverActionsTypeTypeDef,
    },
)
_OptionalAccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "_OptionalAccountTakeoverRiskConfigurationTypeTypeDef",
    {
        "NotifyConfiguration": NotifyConfigurationTypeTypeDef,
    },
    total=False,
)

class AccountTakeoverRiskConfigurationTypeTypeDef(
    _RequiredAccountTakeoverRiskConfigurationTypeTypeDef,
    _OptionalAccountTakeoverRiskConfigurationTypeTypeDef,
):
    pass

_RequiredUpdateUserPoolRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalUpdateUserPoolRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserPoolRequestRequestTypeDef",
    {
        "Policies": UserPoolPolicyTypeTypeDef,
        "DeletionProtection": DeletionProtectionTypeType,
        "LambdaConfig": LambdaConfigTypeTypeDef,
        "AutoVerifiedAttributes": Sequence[VerifiedAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": VerificationMessageTemplateTypeTypeDef,
        "SmsAuthenticationMessage": str,
        "UserAttributeUpdateSettings": UserAttributeUpdateSettingsTypeTypeDef,
        "MfaConfiguration": UserPoolMfaTypeType,
        "DeviceConfiguration": DeviceConfigurationTypeTypeDef,
        "EmailConfiguration": EmailConfigurationTypeTypeDef,
        "SmsConfiguration": SmsConfigurationTypeTypeDef,
        "UserPoolTags": Mapping[str, str],
        "AdminCreateUserConfig": AdminCreateUserConfigTypeTypeDef,
        "UserPoolAddOns": UserPoolAddOnsTypeTypeDef,
        "AccountRecoverySetting": AccountRecoverySettingTypeTypeDef,
    },
    total=False,
)

class UpdateUserPoolRequestRequestTypeDef(
    _RequiredUpdateUserPoolRequestRequestTypeDef, _OptionalUpdateUserPoolRequestRequestTypeDef
):
    pass

CreateResourceServerResponseTypeDef = TypedDict(
    "CreateResourceServerResponseTypeDef",
    {
        "ResourceServer": ResourceServerTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceServerResponseTypeDef = TypedDict(
    "DescribeResourceServerResponseTypeDef",
    {
        "ResourceServer": ResourceServerTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceServersResponseTypeDef = TypedDict(
    "ListResourceServersResponseTypeDef",
    {
        "ResourceServers": List[ResourceServerTypeTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResourceServerResponseTypeDef = TypedDict(
    "UpdateResourceServerResponseTypeDef",
    {
        "ResourceServer": ResourceServerTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserPoolTypeTypeDef = TypedDict(
    "UserPoolTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": UserPoolPolicyTypeOutputTypeDef,
        "DeletionProtection": DeletionProtectionTypeType,
        "LambdaConfig": LambdaConfigTypeOutputTypeDef,
        "Status": StatusTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List[SchemaAttributeTypeOutputTypeDef],
        "AutoVerifiedAttributes": List[VerifiedAttributeTypeType],
        "AliasAttributes": List[AliasAttributeTypeType],
        "UsernameAttributes": List[UsernameAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": VerificationMessageTemplateTypeOutputTypeDef,
        "SmsAuthenticationMessage": str,
        "UserAttributeUpdateSettings": UserAttributeUpdateSettingsTypeOutputTypeDef,
        "MfaConfiguration": UserPoolMfaTypeType,
        "DeviceConfiguration": DeviceConfigurationTypeOutputTypeDef,
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": EmailConfigurationTypeOutputTypeDef,
        "SmsConfiguration": SmsConfigurationTypeOutputTypeDef,
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": AdminCreateUserConfigTypeOutputTypeDef,
        "UserPoolAddOns": UserPoolAddOnsTypeOutputTypeDef,
        "UsernameConfiguration": UsernameConfigurationTypeOutputTypeDef,
        "Arn": str,
        "AccountRecoverySetting": AccountRecoverySettingTypeOutputTypeDef,
    },
    total=False,
)

AddCustomAttributesRequestRequestTypeDef = TypedDict(
    "AddCustomAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "CustomAttributes": Sequence[SchemaAttributeTypeTypeDef],
    },
)

_RequiredCreateUserPoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)
_OptionalCreateUserPoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolRequestRequestTypeDef",
    {
        "Policies": UserPoolPolicyTypeTypeDef,
        "DeletionProtection": DeletionProtectionTypeType,
        "LambdaConfig": LambdaConfigTypeTypeDef,
        "AutoVerifiedAttributes": Sequence[VerifiedAttributeTypeType],
        "AliasAttributes": Sequence[AliasAttributeTypeType],
        "UsernameAttributes": Sequence[UsernameAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": VerificationMessageTemplateTypeTypeDef,
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": UserPoolMfaTypeType,
        "UserAttributeUpdateSettings": UserAttributeUpdateSettingsTypeTypeDef,
        "DeviceConfiguration": DeviceConfigurationTypeTypeDef,
        "EmailConfiguration": EmailConfigurationTypeTypeDef,
        "SmsConfiguration": SmsConfigurationTypeTypeDef,
        "UserPoolTags": Mapping[str, str],
        "AdminCreateUserConfig": AdminCreateUserConfigTypeTypeDef,
        "Schema": Sequence[SchemaAttributeTypeTypeDef],
        "UserPoolAddOns": UserPoolAddOnsTypeTypeDef,
        "UsernameConfiguration": UsernameConfigurationTypeTypeDef,
        "AccountRecoverySetting": AccountRecoverySettingTypeTypeDef,
    },
    total=False,
)

class CreateUserPoolRequestRequestTypeDef(
    _RequiredCreateUserPoolRequestRequestTypeDef, _OptionalCreateUserPoolRequestRequestTypeDef
):
    pass

GetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "GetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": SmsMfaConfigTypeOutputTypeDef,
        "SoftwareTokenMfaConfiguration": SoftwareTokenMfaConfigTypeOutputTypeDef,
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "SetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": SmsMfaConfigTypeOutputTypeDef,
        "SoftwareTokenMfaConfiguration": SoftwareTokenMfaConfigTypeOutputTypeDef,
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserPoolClientResponseTypeDef = TypedDict(
    "CreateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": UserPoolClientTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolClientResponseTypeDef = TypedDict(
    "DescribeUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": UserPoolClientTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserPoolClientResponseTypeDef = TypedDict(
    "UpdateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": UserPoolClientTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserPoolsResponseTypeDef = TypedDict(
    "ListUserPoolsResponseTypeDef",
    {
        "UserPools": List[UserPoolDescriptionTypeTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RiskConfigurationTypeTypeDef = TypedDict(
    "RiskConfigurationTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": (
            CompromisedCredentialsRiskConfigurationTypeOutputTypeDef
        ),
        "AccountTakeoverRiskConfiguration": AccountTakeoverRiskConfigurationTypeOutputTypeDef,
        "RiskExceptionConfiguration": RiskExceptionConfigurationTypeOutputTypeDef,
        "LastModifiedDate": datetime,
    },
    total=False,
)

_RequiredSetRiskConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredSetRiskConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetRiskConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalSetRiskConfigurationRequestRequestTypeDef",
    {
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": (
            CompromisedCredentialsRiskConfigurationTypeTypeDef
        ),
        "AccountTakeoverRiskConfiguration": AccountTakeoverRiskConfigurationTypeTypeDef,
        "RiskExceptionConfiguration": RiskExceptionConfigurationTypeTypeDef,
    },
    total=False,
)

class SetRiskConfigurationRequestRequestTypeDef(
    _RequiredSetRiskConfigurationRequestRequestTypeDef,
    _OptionalSetRiskConfigurationRequestRequestTypeDef,
):
    pass

CreateUserPoolResponseTypeDef = TypedDict(
    "CreateUserPoolResponseTypeDef",
    {
        "UserPool": UserPoolTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolResponseTypeDef = TypedDict(
    "DescribeUserPoolResponseTypeDef",
    {
        "UserPool": UserPoolTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRiskConfigurationResponseTypeDef = TypedDict(
    "DescribeRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": RiskConfigurationTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetRiskConfigurationResponseTypeDef = TypedDict(
    "SetRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": RiskConfigurationTypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
