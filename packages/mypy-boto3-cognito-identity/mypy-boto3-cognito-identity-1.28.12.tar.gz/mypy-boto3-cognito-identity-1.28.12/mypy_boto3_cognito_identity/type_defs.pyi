"""
Type annotations for cognito-identity service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/type_defs/)

Usage::

    ```python
    from mypy_boto3_cognito_identity.type_defs import CognitoIdentityProviderOutputTypeDef

    data: CognitoIdentityProviderOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AmbiguousRoleResolutionTypeType,
    ErrorCodeType,
    MappingRuleMatchTypeType,
    RoleMappingTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CognitoIdentityProviderOutputTypeDef",
    "CognitoIdentityProviderTypeDef",
    "CredentialsTypeDef",
    "DeleteIdentitiesInputRequestTypeDef",
    "UnprocessedIdentityIdTypeDef",
    "DeleteIdentityPoolInputRequestTypeDef",
    "DescribeIdentityInputRequestTypeDef",
    "DescribeIdentityPoolInputRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCredentialsForIdentityInputRequestTypeDef",
    "GetIdInputRequestTypeDef",
    "GetIdResponseTypeDef",
    "GetIdentityPoolRolesInputRequestTypeDef",
    "GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "GetOpenIdTokenInputRequestTypeDef",
    "GetOpenIdTokenResponseTypeDef",
    "GetPrincipalTagAttributeMapInputRequestTypeDef",
    "GetPrincipalTagAttributeMapResponseTypeDef",
    "IdentityDescriptionResponseMetadataTypeDef",
    "IdentityDescriptionTypeDef",
    "IdentityPoolShortDescriptionTypeDef",
    "ListIdentitiesInputRequestTypeDef",
    "ListIdentityPoolsInputListIdentityPoolsPaginateTypeDef",
    "ListIdentityPoolsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LookupDeveloperIdentityInputRequestTypeDef",
    "LookupDeveloperIdentityResponseTypeDef",
    "MappingRuleOutputTypeDef",
    "MappingRuleTypeDef",
    "MergeDeveloperIdentitiesInputRequestTypeDef",
    "MergeDeveloperIdentitiesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SetPrincipalTagAttributeMapInputRequestTypeDef",
    "SetPrincipalTagAttributeMapResponseTypeDef",
    "TagResourceInputRequestTypeDef",
    "UnlinkDeveloperIdentityInputRequestTypeDef",
    "UnlinkIdentityInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "IdentityPoolTypeDef",
    "CreateIdentityPoolInputRequestTypeDef",
    "IdentityPoolRequestTypeDef",
    "GetCredentialsForIdentityResponseTypeDef",
    "DeleteIdentitiesResponseTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoolsResponseTypeDef",
    "RulesConfigurationTypeOutputTypeDef",
    "RulesConfigurationTypeTypeDef",
    "RoleMappingOutputTypeDef",
    "RoleMappingTypeDef",
    "GetIdentityPoolRolesResponseTypeDef",
    "SetIdentityPoolRolesInputRequestTypeDef",
)

CognitoIdentityProviderOutputTypeDef = TypedDict(
    "CognitoIdentityProviderOutputTypeDef",
    {
        "ProviderName": str,
        "ClientId": str,
        "ServerSideTokenCheck": bool,
    },
    total=False,
)

CognitoIdentityProviderTypeDef = TypedDict(
    "CognitoIdentityProviderTypeDef",
    {
        "ProviderName": str,
        "ClientId": str,
        "ServerSideTokenCheck": bool,
    },
    total=False,
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretKey": str,
        "SessionToken": str,
        "Expiration": datetime,
    },
    total=False,
)

DeleteIdentitiesInputRequestTypeDef = TypedDict(
    "DeleteIdentitiesInputRequestTypeDef",
    {
        "IdentityIdsToDelete": Sequence[str],
    },
)

UnprocessedIdentityIdTypeDef = TypedDict(
    "UnprocessedIdentityIdTypeDef",
    {
        "IdentityId": str,
        "ErrorCode": ErrorCodeType,
    },
    total=False,
)

DeleteIdentityPoolInputRequestTypeDef = TypedDict(
    "DeleteIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

DescribeIdentityInputRequestTypeDef = TypedDict(
    "DescribeIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
    },
)

DescribeIdentityPoolInputRequestTypeDef = TypedDict(
    "DescribeIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCredentialsForIdentityInputRequestTypeDef = TypedDict(
    "_RequiredGetCredentialsForIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
    },
)
_OptionalGetCredentialsForIdentityInputRequestTypeDef = TypedDict(
    "_OptionalGetCredentialsForIdentityInputRequestTypeDef",
    {
        "Logins": Mapping[str, str],
        "CustomRoleArn": str,
    },
    total=False,
)

class GetCredentialsForIdentityInputRequestTypeDef(
    _RequiredGetCredentialsForIdentityInputRequestTypeDef,
    _OptionalGetCredentialsForIdentityInputRequestTypeDef,
):
    pass

_RequiredGetIdInputRequestTypeDef = TypedDict(
    "_RequiredGetIdInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
_OptionalGetIdInputRequestTypeDef = TypedDict(
    "_OptionalGetIdInputRequestTypeDef",
    {
        "AccountId": str,
        "Logins": Mapping[str, str],
    },
    total=False,
)

class GetIdInputRequestTypeDef(
    _RequiredGetIdInputRequestTypeDef, _OptionalGetIdInputRequestTypeDef
):
    pass

GetIdResponseTypeDef = TypedDict(
    "GetIdResponseTypeDef",
    {
        "IdentityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "GetIdentityPoolRolesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

_RequiredGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef = TypedDict(
    "_RequiredGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Logins": Mapping[str, str],
    },
)
_OptionalGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef = TypedDict(
    "_OptionalGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "PrincipalTags": Mapping[str, str],
        "TokenDuration": int,
    },
    total=False,
)

class GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef(
    _RequiredGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef,
    _OptionalGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef,
):
    pass

GetOpenIdTokenForDeveloperIdentityResponseTypeDef = TypedDict(
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOpenIdTokenInputRequestTypeDef = TypedDict(
    "_RequiredGetOpenIdTokenInputRequestTypeDef",
    {
        "IdentityId": str,
    },
)
_OptionalGetOpenIdTokenInputRequestTypeDef = TypedDict(
    "_OptionalGetOpenIdTokenInputRequestTypeDef",
    {
        "Logins": Mapping[str, str],
    },
    total=False,
)

class GetOpenIdTokenInputRequestTypeDef(
    _RequiredGetOpenIdTokenInputRequestTypeDef, _OptionalGetOpenIdTokenInputRequestTypeDef
):
    pass

GetOpenIdTokenResponseTypeDef = TypedDict(
    "GetOpenIdTokenResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
    },
)

GetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityDescriptionResponseMetadataTypeDef = TypedDict(
    "IdentityDescriptionResponseMetadataTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityDescriptionTypeDef = TypedDict(
    "IdentityDescriptionTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)

IdentityPoolShortDescriptionTypeDef = TypedDict(
    "IdentityPoolShortDescriptionTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
    },
    total=False,
)

_RequiredListIdentitiesInputRequestTypeDef = TypedDict(
    "_RequiredListIdentitiesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "MaxResults": int,
    },
)
_OptionalListIdentitiesInputRequestTypeDef = TypedDict(
    "_OptionalListIdentitiesInputRequestTypeDef",
    {
        "NextToken": str,
        "HideDisabled": bool,
    },
    total=False,
)

class ListIdentitiesInputRequestTypeDef(
    _RequiredListIdentitiesInputRequestTypeDef, _OptionalListIdentitiesInputRequestTypeDef
):
    pass

ListIdentityPoolsInputListIdentityPoolsPaginateTypeDef = TypedDict(
    "ListIdentityPoolsInputListIdentityPoolsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

_RequiredListIdentityPoolsInputRequestTypeDef = TypedDict(
    "_RequiredListIdentityPoolsInputRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListIdentityPoolsInputRequestTypeDef = TypedDict(
    "_OptionalListIdentityPoolsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListIdentityPoolsInputRequestTypeDef(
    _RequiredListIdentityPoolsInputRequestTypeDef, _OptionalListIdentityPoolsInputRequestTypeDef
):
    pass

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
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

_RequiredLookupDeveloperIdentityInputRequestTypeDef = TypedDict(
    "_RequiredLookupDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
_OptionalLookupDeveloperIdentityInputRequestTypeDef = TypedDict(
    "_OptionalLookupDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifier": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class LookupDeveloperIdentityInputRequestTypeDef(
    _RequiredLookupDeveloperIdentityInputRequestTypeDef,
    _OptionalLookupDeveloperIdentityInputRequestTypeDef,
):
    pass

LookupDeveloperIdentityResponseTypeDef = TypedDict(
    "LookupDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifierList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MappingRuleOutputTypeDef = TypedDict(
    "MappingRuleOutputTypeDef",
    {
        "Claim": str,
        "MatchType": MappingRuleMatchTypeType,
        "Value": str,
        "RoleARN": str,
    },
)

MappingRuleTypeDef = TypedDict(
    "MappingRuleTypeDef",
    {
        "Claim": str,
        "MatchType": MappingRuleMatchTypeType,
        "Value": str,
        "RoleARN": str,
    },
)

MergeDeveloperIdentitiesInputRequestTypeDef = TypedDict(
    "MergeDeveloperIdentitiesInputRequestTypeDef",
    {
        "SourceUserIdentifier": str,
        "DestinationUserIdentifier": str,
        "DeveloperProviderName": str,
        "IdentityPoolId": str,
    },
)

MergeDeveloperIdentitiesResponseTypeDef = TypedDict(
    "MergeDeveloperIdentitiesResponseTypeDef",
    {
        "IdentityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredSetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "_RequiredSetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
    },
)
_OptionalSetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "_OptionalSetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "UseDefaults": bool,
        "PrincipalTags": Mapping[str, str],
    },
    total=False,
)

class SetPrincipalTagAttributeMapInputRequestTypeDef(
    _RequiredSetPrincipalTagAttributeMapInputRequestTypeDef,
    _OptionalSetPrincipalTagAttributeMapInputRequestTypeDef,
):
    pass

SetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "SetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UnlinkDeveloperIdentityInputRequestTypeDef = TypedDict(
    "UnlinkDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "DeveloperProviderName": str,
        "DeveloperUserIdentifier": str,
    },
)

UnlinkIdentityInputRequestTypeDef = TypedDict(
    "UnlinkIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "Logins": Mapping[str, str],
        "LoginsToRemove": Sequence[str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

IdentityPoolTypeDef = TypedDict(
    "IdentityPoolTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[CognitoIdentityProviderOutputTypeDef],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIdentityPoolInputRequestTypeDef = TypedDict(
    "_RequiredCreateIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
    },
)
_OptionalCreateIdentityPoolInputRequestTypeDef = TypedDict(
    "_OptionalCreateIdentityPoolInputRequestTypeDef",
    {
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Mapping[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": Sequence[str],
        "CognitoIdentityProviders": Sequence[CognitoIdentityProviderTypeDef],
        "SamlProviderARNs": Sequence[str],
        "IdentityPoolTags": Mapping[str, str],
    },
    total=False,
)

class CreateIdentityPoolInputRequestTypeDef(
    _RequiredCreateIdentityPoolInputRequestTypeDef, _OptionalCreateIdentityPoolInputRequestTypeDef
):
    pass

_RequiredIdentityPoolRequestTypeDef = TypedDict(
    "_RequiredIdentityPoolRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
    },
)
_OptionalIdentityPoolRequestTypeDef = TypedDict(
    "_OptionalIdentityPoolRequestTypeDef",
    {
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Mapping[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": Sequence[str],
        "CognitoIdentityProviders": Sequence[CognitoIdentityProviderTypeDef],
        "SamlProviderARNs": Sequence[str],
        "IdentityPoolTags": Mapping[str, str],
    },
    total=False,
)

class IdentityPoolRequestTypeDef(
    _RequiredIdentityPoolRequestTypeDef, _OptionalIdentityPoolRequestTypeDef
):
    pass

GetCredentialsForIdentityResponseTypeDef = TypedDict(
    "GetCredentialsForIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Credentials": CredentialsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIdentitiesResponseTypeDef = TypedDict(
    "DeleteIdentitiesResponseTypeDef",
    {
        "UnprocessedIdentityIds": List[UnprocessedIdentityIdTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentitiesResponseTypeDef = TypedDict(
    "ListIdentitiesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List[IdentityDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityPoolsResponseTypeDef = TypedDict(
    "ListIdentityPoolsResponseTypeDef",
    {
        "IdentityPools": List[IdentityPoolShortDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RulesConfigurationTypeOutputTypeDef = TypedDict(
    "RulesConfigurationTypeOutputTypeDef",
    {
        "Rules": List[MappingRuleOutputTypeDef],
    },
)

RulesConfigurationTypeTypeDef = TypedDict(
    "RulesConfigurationTypeTypeDef",
    {
        "Rules": Sequence[MappingRuleTypeDef],
    },
)

_RequiredRoleMappingOutputTypeDef = TypedDict(
    "_RequiredRoleMappingOutputTypeDef",
    {
        "Type": RoleMappingTypeType,
    },
)
_OptionalRoleMappingOutputTypeDef = TypedDict(
    "_OptionalRoleMappingOutputTypeDef",
    {
        "AmbiguousRoleResolution": AmbiguousRoleResolutionTypeType,
        "RulesConfiguration": RulesConfigurationTypeOutputTypeDef,
    },
    total=False,
)

class RoleMappingOutputTypeDef(
    _RequiredRoleMappingOutputTypeDef, _OptionalRoleMappingOutputTypeDef
):
    pass

_RequiredRoleMappingTypeDef = TypedDict(
    "_RequiredRoleMappingTypeDef",
    {
        "Type": RoleMappingTypeType,
    },
)
_OptionalRoleMappingTypeDef = TypedDict(
    "_OptionalRoleMappingTypeDef",
    {
        "AmbiguousRoleResolution": AmbiguousRoleResolutionTypeType,
        "RulesConfiguration": RulesConfigurationTypeTypeDef,
    },
    total=False,
)

class RoleMappingTypeDef(_RequiredRoleMappingTypeDef, _OptionalRoleMappingTypeDef):
    pass

GetIdentityPoolRolesResponseTypeDef = TypedDict(
    "GetIdentityPoolRolesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[str, RoleMappingOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "_RequiredSetIdentityPoolRolesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Mapping[str, str],
    },
)
_OptionalSetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "_OptionalSetIdentityPoolRolesInputRequestTypeDef",
    {
        "RoleMappings": Mapping[str, RoleMappingTypeDef],
    },
    total=False,
)

class SetIdentityPoolRolesInputRequestTypeDef(
    _RequiredSetIdentityPoolRolesInputRequestTypeDef,
    _OptionalSetIdentityPoolRolesInputRequestTypeDef,
):
    pass
