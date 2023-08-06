"""
Type annotations for license-manager-user-subscriptions service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/type_defs/)

Usage::

    ```python
    from mypy_boto3_license_manager_user_subscriptions.type_defs import ActiveDirectoryIdentityProviderOutputTypeDef

    data: ActiveDirectoryIdentityProviderOutputTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveDirectoryIdentityProviderOutputTypeDef",
    "ActiveDirectoryIdentityProviderTypeDef",
    "FilterTypeDef",
    "SettingsOutputTypeDef",
    "InstanceSummaryTypeDef",
    "ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "SettingsTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateSettingsTypeDef",
    "IdentityProviderOutputTypeDef",
    "IdentityProviderTypeDef",
    "ListInstancesRequestListInstancesPaginateTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "IdentityProviderSummaryTypeDef",
    "InstanceUserSummaryTypeDef",
    "ProductUserSummaryTypeDef",
    "AssociateUserRequestRequestTypeDef",
    "DeregisterIdentityProviderRequestRequestTypeDef",
    "DisassociateUserRequestRequestTypeDef",
    "ListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef",
    "ListProductSubscriptionsRequestRequestTypeDef",
    "ListUserAssociationsRequestListUserAssociationsPaginateTypeDef",
    "ListUserAssociationsRequestRequestTypeDef",
    "RegisterIdentityProviderRequestRequestTypeDef",
    "StartProductSubscriptionRequestRequestTypeDef",
    "StopProductSubscriptionRequestRequestTypeDef",
    "UpdateIdentityProviderSettingsRequestRequestTypeDef",
    "DeregisterIdentityProviderResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "RegisterIdentityProviderResponseTypeDef",
    "UpdateIdentityProviderSettingsResponseTypeDef",
    "AssociateUserResponseTypeDef",
    "DisassociateUserResponseTypeDef",
    "ListUserAssociationsResponseTypeDef",
    "ListProductSubscriptionsResponseTypeDef",
    "StartProductSubscriptionResponseTypeDef",
    "StopProductSubscriptionResponseTypeDef",
)

ActiveDirectoryIdentityProviderOutputTypeDef = TypedDict(
    "ActiveDirectoryIdentityProviderOutputTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

ActiveDirectoryIdentityProviderTypeDef = TypedDict(
    "ActiveDirectoryIdentityProviderTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Attribute": str,
        "Operation": str,
        "Value": str,
    },
    total=False,
)

SettingsOutputTypeDef = TypedDict(
    "SettingsOutputTypeDef",
    {
        "SecurityGroupId": str,
        "Subnets": List[str],
    },
)

_RequiredInstanceSummaryTypeDef = TypedDict(
    "_RequiredInstanceSummaryTypeDef",
    {
        "InstanceId": str,
        "Products": List[str],
        "Status": str,
    },
)
_OptionalInstanceSummaryTypeDef = TypedDict(
    "_OptionalInstanceSummaryTypeDef",
    {
        "LastStatusCheckDate": str,
        "StatusMessage": str,
    },
    total=False,
)


class InstanceSummaryTypeDef(_RequiredInstanceSummaryTypeDef, _OptionalInstanceSummaryTypeDef):
    pass


ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef = TypedDict(
    "ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "ListIdentityProvidersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
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

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "SecurityGroupId": str,
        "Subnets": Sequence[str],
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

_RequiredUpdateSettingsTypeDef = TypedDict(
    "_RequiredUpdateSettingsTypeDef",
    {
        "AddSubnets": Sequence[str],
        "RemoveSubnets": Sequence[str],
    },
)
_OptionalUpdateSettingsTypeDef = TypedDict(
    "_OptionalUpdateSettingsTypeDef",
    {
        "SecurityGroupId": str,
    },
    total=False,
)


class UpdateSettingsTypeDef(_RequiredUpdateSettingsTypeDef, _OptionalUpdateSettingsTypeDef):
    pass


IdentityProviderOutputTypeDef = TypedDict(
    "IdentityProviderOutputTypeDef",
    {
        "ActiveDirectoryIdentityProvider": ActiveDirectoryIdentityProviderOutputTypeDef,
    },
    total=False,
)

IdentityProviderTypeDef = TypedDict(
    "IdentityProviderTypeDef",
    {
        "ActiveDirectoryIdentityProvider": ActiveDirectoryIdentityProviderTypeDef,
    },
    total=False,
)

ListInstancesRequestListInstancesPaginateTypeDef = TypedDict(
    "ListInstancesRequestListInstancesPaginateTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "InstanceSummaries": List[InstanceSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIdentityProviderSummaryTypeDef = TypedDict(
    "_RequiredIdentityProviderSummaryTypeDef",
    {
        "IdentityProvider": IdentityProviderOutputTypeDef,
        "Product": str,
        "Settings": SettingsOutputTypeDef,
        "Status": str,
    },
)
_OptionalIdentityProviderSummaryTypeDef = TypedDict(
    "_OptionalIdentityProviderSummaryTypeDef",
    {
        "FailureMessage": str,
    },
    total=False,
)


class IdentityProviderSummaryTypeDef(
    _RequiredIdentityProviderSummaryTypeDef, _OptionalIdentityProviderSummaryTypeDef
):
    pass


_RequiredInstanceUserSummaryTypeDef = TypedDict(
    "_RequiredInstanceUserSummaryTypeDef",
    {
        "IdentityProvider": IdentityProviderOutputTypeDef,
        "InstanceId": str,
        "Status": str,
        "Username": str,
    },
)
_OptionalInstanceUserSummaryTypeDef = TypedDict(
    "_OptionalInstanceUserSummaryTypeDef",
    {
        "AssociationDate": str,
        "DisassociationDate": str,
        "Domain": str,
        "StatusMessage": str,
    },
    total=False,
)


class InstanceUserSummaryTypeDef(
    _RequiredInstanceUserSummaryTypeDef, _OptionalInstanceUserSummaryTypeDef
):
    pass


_RequiredProductUserSummaryTypeDef = TypedDict(
    "_RequiredProductUserSummaryTypeDef",
    {
        "IdentityProvider": IdentityProviderOutputTypeDef,
        "Product": str,
        "Status": str,
        "Username": str,
    },
)
_OptionalProductUserSummaryTypeDef = TypedDict(
    "_OptionalProductUserSummaryTypeDef",
    {
        "Domain": str,
        "StatusMessage": str,
        "SubscriptionEndDate": str,
        "SubscriptionStartDate": str,
    },
    total=False,
)


class ProductUserSummaryTypeDef(
    _RequiredProductUserSummaryTypeDef, _OptionalProductUserSummaryTypeDef
):
    pass


_RequiredAssociateUserRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateUserRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
        "Username": str,
    },
)
_OptionalAssociateUserRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateUserRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)


class AssociateUserRequestRequestTypeDef(
    _RequiredAssociateUserRequestRequestTypeDef, _OptionalAssociateUserRequestRequestTypeDef
):
    pass


DeregisterIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeregisterIdentityProviderRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
    },
)

_RequiredDisassociateUserRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateUserRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
        "Username": str,
    },
)
_OptionalDisassociateUserRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateUserRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)


class DisassociateUserRequestRequestTypeDef(
    _RequiredDisassociateUserRequestRequestTypeDef, _OptionalDisassociateUserRequestRequestTypeDef
):
    pass


_RequiredListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef = TypedDict(
    "_RequiredListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
    },
)
_OptionalListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef = TypedDict(
    "_OptionalListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef(
    _RequiredListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef,
    _OptionalListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef,
):
    pass


_RequiredListProductSubscriptionsRequestRequestTypeDef = TypedDict(
    "_RequiredListProductSubscriptionsRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
    },
)
_OptionalListProductSubscriptionsRequestRequestTypeDef = TypedDict(
    "_OptionalListProductSubscriptionsRequestRequestTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListProductSubscriptionsRequestRequestTypeDef(
    _RequiredListProductSubscriptionsRequestRequestTypeDef,
    _OptionalListProductSubscriptionsRequestRequestTypeDef,
):
    pass


_RequiredListUserAssociationsRequestListUserAssociationsPaginateTypeDef = TypedDict(
    "_RequiredListUserAssociationsRequestListUserAssociationsPaginateTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
    },
)
_OptionalListUserAssociationsRequestListUserAssociationsPaginateTypeDef = TypedDict(
    "_OptionalListUserAssociationsRequestListUserAssociationsPaginateTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListUserAssociationsRequestListUserAssociationsPaginateTypeDef(
    _RequiredListUserAssociationsRequestListUserAssociationsPaginateTypeDef,
    _OptionalListUserAssociationsRequestListUserAssociationsPaginateTypeDef,
):
    pass


_RequiredListUserAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserAssociationsRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
    },
)
_OptionalListUserAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserAssociationsRequestRequestTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListUserAssociationsRequestRequestTypeDef(
    _RequiredListUserAssociationsRequestRequestTypeDef,
    _OptionalListUserAssociationsRequestRequestTypeDef,
):
    pass


_RequiredRegisterIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterIdentityProviderRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
    },
)
_OptionalRegisterIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterIdentityProviderRequestRequestTypeDef",
    {
        "Settings": SettingsTypeDef,
    },
    total=False,
)


class RegisterIdentityProviderRequestRequestTypeDef(
    _RequiredRegisterIdentityProviderRequestRequestTypeDef,
    _OptionalRegisterIdentityProviderRequestRequestTypeDef,
):
    pass


_RequiredStartProductSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredStartProductSubscriptionRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Username": str,
    },
)
_OptionalStartProductSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalStartProductSubscriptionRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)


class StartProductSubscriptionRequestRequestTypeDef(
    _RequiredStartProductSubscriptionRequestRequestTypeDef,
    _OptionalStartProductSubscriptionRequestRequestTypeDef,
):
    pass


_RequiredStopProductSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredStopProductSubscriptionRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Username": str,
    },
)
_OptionalStopProductSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalStopProductSubscriptionRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)


class StopProductSubscriptionRequestRequestTypeDef(
    _RequiredStopProductSubscriptionRequestRequestTypeDef,
    _OptionalStopProductSubscriptionRequestRequestTypeDef,
):
    pass


UpdateIdentityProviderSettingsRequestRequestTypeDef = TypedDict(
    "UpdateIdentityProviderSettingsRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "UpdateSettings": UpdateSettingsTypeDef,
    },
)

DeregisterIdentityProviderResponseTypeDef = TypedDict(
    "DeregisterIdentityProviderResponseTypeDef",
    {
        "IdentityProviderSummary": IdentityProviderSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "IdentityProviderSummaries": List[IdentityProviderSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterIdentityProviderResponseTypeDef = TypedDict(
    "RegisterIdentityProviderResponseTypeDef",
    {
        "IdentityProviderSummary": IdentityProviderSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIdentityProviderSettingsResponseTypeDef = TypedDict(
    "UpdateIdentityProviderSettingsResponseTypeDef",
    {
        "IdentityProviderSummary": IdentityProviderSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateUserResponseTypeDef = TypedDict(
    "AssociateUserResponseTypeDef",
    {
        "InstanceUserSummary": InstanceUserSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateUserResponseTypeDef = TypedDict(
    "DisassociateUserResponseTypeDef",
    {
        "InstanceUserSummary": InstanceUserSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserAssociationsResponseTypeDef = TypedDict(
    "ListUserAssociationsResponseTypeDef",
    {
        "InstanceUserSummaries": List[InstanceUserSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProductSubscriptionsResponseTypeDef = TypedDict(
    "ListProductSubscriptionsResponseTypeDef",
    {
        "NextToken": str,
        "ProductUserSummaries": List[ProductUserSummaryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartProductSubscriptionResponseTypeDef = TypedDict(
    "StartProductSubscriptionResponseTypeDef",
    {
        "ProductUserSummary": ProductUserSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopProductSubscriptionResponseTypeDef = TypedDict(
    "StopProductSubscriptionResponseTypeDef",
    {
        "ProductUserSummary": ProductUserSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
