"""
Type annotations for license-manager service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/type_defs/)

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AcceptGrantRequestRequestTypeDef

    data: AcceptGrantRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    ActivationOverrideBehaviorType,
    AllowedOperationType,
    CheckoutTypeType,
    EntitlementDataUnitType,
    EntitlementUnitType,
    GrantStatusType,
    InventoryFilterConditionType,
    LicenseConfigurationStatusType,
    LicenseConversionTaskStatusType,
    LicenseCountingTypeType,
    LicenseDeletionStatusType,
    LicenseStatusType,
    ReceivedStatusType,
    RenewTypeType,
    ReportFrequencyTypeType,
    ReportTypeType,
    ResourceTypeType,
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
    "AcceptGrantRequestRequestTypeDef",
    "AcceptGrantResponseTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationOutputTypeDef",
    "BorrowConfigurationTypeDef",
    "CheckInLicenseRequestRequestTypeDef",
    "EntitlementDataTypeDef",
    "MetadataTypeDef",
    "EntitlementDataOutputTypeDef",
    "MetadataOutputTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ProvisionalConfigurationOutputTypeDef",
    "ProvisionalConfigurationTypeDef",
    "CreateGrantRequestRequestTypeDef",
    "CreateGrantResponseTypeDef",
    "OptionsTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "TagTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "LicenseConversionContextTypeDef",
    "CreateLicenseConversionTaskForResourceResponseTypeDef",
    "ReportContextTypeDef",
    "ReportFrequencyTypeDef",
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    "DatetimeRangeTypeDef",
    "EntitlementTypeDef",
    "IssuerTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenRequestRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "DatetimeRangeOutputTypeDef",
    "DeleteGrantRequestRequestTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseConfigurationRequestRequestTypeDef",
    "DeleteLicenseManagerReportGeneratorRequestRequestTypeDef",
    "DeleteLicenseRequestRequestTypeDef",
    "DeleteLicenseResponseTypeDef",
    "DeleteTokenRequestRequestTypeDef",
    "EntitlementOutputTypeDef",
    "EntitlementUsageTypeDef",
    "ExtendLicenseConsumptionRequestRequestTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenRequestRequestTypeDef",
    "GetAccessTokenResponseTypeDef",
    "GetGrantRequestRequestTypeDef",
    "GetLicenseConfigurationRequestRequestTypeDef",
    "ManagedResourceSummaryTypeDef",
    "TagOutputTypeDef",
    "GetLicenseConversionTaskRequestRequestTypeDef",
    "LicenseConversionContextOutputTypeDef",
    "GetLicenseManagerReportGeneratorRequestRequestTypeDef",
    "GetLicenseRequestRequestTypeDef",
    "GetLicenseUsageRequestRequestTypeDef",
    "OrganizationConfigurationOutputTypeDef",
    "OptionsOutputTypeDef",
    "IssuerDetailsTypeDef",
    "ReceivedMetadataTypeDef",
    "InventoryFilterTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseSpecificationOutputTypeDef",
    "LicenseSpecificationTypeDef",
    "ListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef",
    "ListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    "ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    "ListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef",
    "ListLicenseSpecificationsForResourceRequestRequestTypeDef",
    "ListLicenseVersionsRequestRequestTypeDef",
    "ResourceInventoryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TokenDataTypeDef",
    "OrganizationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ProductInformationFilterOutputTypeDef",
    "ProductInformationFilterTypeDef",
    "RejectGrantRequestRequestTypeDef",
    "RejectGrantResponseTypeDef",
    "ReportContextOutputTypeDef",
    "ReportFrequencyOutputTypeDef",
    "S3LocationTypeDef",
    "ResponseMetadataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CheckoutLicenseRequestRequestTypeDef",
    "CheckoutBorrowLicenseRequestRequestTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "LicenseOperationFailureTypeDef",
    "ConsumptionConfigurationOutputTypeDef",
    "ConsumptionConfigurationTypeDef",
    "CreateGrantVersionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateLicenseConversionTaskForResourceRequestRequestTypeDef",
    "CreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    "UpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    "LicenseUsageTypeDef",
    "ListDistributedGrantsRequestRequestTypeDef",
    "ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateTypeDef",
    "ListLicenseConfigurationsRequestRequestTypeDef",
    "ListLicenseConversionTasksRequestRequestTypeDef",
    "ListLicenseManagerReportGeneratorsRequestRequestTypeDef",
    "ListLicensesRequestRequestTypeDef",
    "ListReceivedGrantsForOrganizationRequestRequestTypeDef",
    "ListReceivedGrantsRequestRequestTypeDef",
    "ListReceivedLicensesForOrganizationRequestRequestTypeDef",
    "ListReceivedLicensesRequestRequestTypeDef",
    "ListTokensRequestRequestTypeDef",
    "ListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef",
    "ListUsageForLicenseConfigurationRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "GetLicenseConversionTaskResponseTypeDef",
    "LicenseConversionTaskTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "GrantTypeDef",
    "ListResourceInventoryRequestListResourceInventoryPaginateTypeDef",
    "ListResourceInventoryRequestRequestTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "UpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTokensResponseTypeDef",
    "UpdateServiceSettingsRequestRequestTypeDef",
    "ProductInformationOutputTypeDef",
    "ProductInformationTypeDef",
    "ReportGeneratorTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "GrantedLicenseTypeDef",
    "LicenseTypeDef",
    "CreateLicenseRequestRequestTypeDef",
    "CreateLicenseVersionRequestRequestTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "ListLicenseConversionTasksResponseTypeDef",
    "GetGrantResponseTypeDef",
    "ListDistributedGrantsResponseTypeDef",
    "ListReceivedGrantsForOrganizationResponseTypeDef",
    "ListReceivedGrantsResponseTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "LicenseConfigurationTypeDef",
    "CreateLicenseConfigurationRequestRequestTypeDef",
    "UpdateLicenseConfigurationRequestRequestTypeDef",
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    "ListReceivedLicensesForOrganizationResponseTypeDef",
    "ListReceivedLicensesResponseTypeDef",
    "GetLicenseResponseTypeDef",
    "ListLicenseVersionsResponseTypeDef",
    "ListLicensesResponseTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
)

AcceptGrantRequestRequestTypeDef = TypedDict(
    "AcceptGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)

AcceptGrantResponseTypeDef = TypedDict(
    "AcceptGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef",
    {
        "LastRunTime": datetime,
    },
    total=False,
)

BorrowConfigurationOutputTypeDef = TypedDict(
    "BorrowConfigurationOutputTypeDef",
    {
        "AllowEarlyCheckIn": bool,
        "MaxTimeToLiveInMinutes": int,
    },
)

BorrowConfigurationTypeDef = TypedDict(
    "BorrowConfigurationTypeDef",
    {
        "AllowEarlyCheckIn": bool,
        "MaxTimeToLiveInMinutes": int,
    },
)

_RequiredCheckInLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredCheckInLicenseRequestRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
    },
)
_OptionalCheckInLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalCheckInLicenseRequestRequestTypeDef",
    {
        "Beneficiary": str,
    },
    total=False,
)


class CheckInLicenseRequestRequestTypeDef(
    _RequiredCheckInLicenseRequestRequestTypeDef, _OptionalCheckInLicenseRequestRequestTypeDef
):
    pass


_RequiredEntitlementDataTypeDef = TypedDict(
    "_RequiredEntitlementDataTypeDef",
    {
        "Name": str,
        "Unit": EntitlementDataUnitType,
    },
)
_OptionalEntitlementDataTypeDef = TypedDict(
    "_OptionalEntitlementDataTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class EntitlementDataTypeDef(_RequiredEntitlementDataTypeDef, _OptionalEntitlementDataTypeDef):
    pass


MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

_RequiredEntitlementDataOutputTypeDef = TypedDict(
    "_RequiredEntitlementDataOutputTypeDef",
    {
        "Name": str,
        "Unit": EntitlementDataUnitType,
    },
)
_OptionalEntitlementDataOutputTypeDef = TypedDict(
    "_OptionalEntitlementDataOutputTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class EntitlementDataOutputTypeDef(
    _RequiredEntitlementDataOutputTypeDef, _OptionalEntitlementDataOutputTypeDef
):
    pass


MetadataOutputTypeDef = TypedDict(
    "MetadataOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

ConsumedLicenseSummaryTypeDef = TypedDict(
    "ConsumedLicenseSummaryTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "ConsumedLicenses": int,
    },
    total=False,
)

ProvisionalConfigurationOutputTypeDef = TypedDict(
    "ProvisionalConfigurationOutputTypeDef",
    {
        "MaxTimeToLiveInMinutes": int,
    },
)

ProvisionalConfigurationTypeDef = TypedDict(
    "ProvisionalConfigurationTypeDef",
    {
        "MaxTimeToLiveInMinutes": int,
    },
)

CreateGrantRequestRequestTypeDef = TypedDict(
    "CreateGrantRequestRequestTypeDef",
    {
        "ClientToken": str,
        "GrantName": str,
        "LicenseArn": str,
        "Principals": Sequence[str],
        "HomeRegion": str,
        "AllowedOperations": Sequence[AllowedOperationType],
    },
)

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptionsTypeDef = TypedDict(
    "OptionsTypeDef",
    {
        "ActivationOverrideBehavior": ActivationOverrideBehaviorType,
    },
    total=False,
)

CreateGrantVersionResponseTypeDef = TypedDict(
    "CreateGrantVersionResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

CreateLicenseConfigurationResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LicenseConversionContextTypeDef = TypedDict(
    "LicenseConversionContextTypeDef",
    {
        "UsageOperation": str,
    },
    total=False,
)

CreateLicenseConversionTaskForResourceResponseTypeDef = TypedDict(
    "CreateLicenseConversionTaskForResourceResponseTypeDef",
    {
        "LicenseConversionTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportContextTypeDef = TypedDict(
    "ReportContextTypeDef",
    {
        "licenseConfigurationArns": Sequence[str],
    },
)

ReportFrequencyTypeDef = TypedDict(
    "ReportFrequencyTypeDef",
    {
        "value": int,
        "period": ReportFrequencyTypeType,
    },
    total=False,
)

CreateLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDatetimeRangeTypeDef = TypedDict(
    "_RequiredDatetimeRangeTypeDef",
    {
        "Begin": str,
    },
)
_OptionalDatetimeRangeTypeDef = TypedDict(
    "_OptionalDatetimeRangeTypeDef",
    {
        "End": str,
    },
    total=False,
)


class DatetimeRangeTypeDef(_RequiredDatetimeRangeTypeDef, _OptionalDatetimeRangeTypeDef):
    pass


_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef",
    {
        "Name": str,
        "Unit": EntitlementUnitType,
    },
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {
        "Value": str,
        "MaxCount": int,
        "Overage": bool,
        "AllowCheckIn": bool,
    },
    total=False,
)


class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass


_RequiredIssuerTypeDef = TypedDict(
    "_RequiredIssuerTypeDef",
    {
        "Name": str,
    },
)
_OptionalIssuerTypeDef = TypedDict(
    "_OptionalIssuerTypeDef",
    {
        "SignKey": str,
    },
    total=False,
)


class IssuerTypeDef(_RequiredIssuerTypeDef, _OptionalIssuerTypeDef):
    pass


CreateLicenseResponseTypeDef = TypedDict(
    "CreateLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "Status": LicenseStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLicenseVersionResponseTypeDef = TypedDict(
    "CreateLicenseVersionResponseTypeDef",
    {
        "LicenseArn": str,
        "Version": str,
        "Status": LicenseStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTokenRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTokenRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "ClientToken": str,
    },
)
_OptionalCreateTokenRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTokenRequestRequestTypeDef",
    {
        "RoleArns": Sequence[str],
        "ExpirationInDays": int,
        "TokenProperties": Sequence[str],
    },
    total=False,
)


class CreateTokenRequestRequestTypeDef(
    _RequiredCreateTokenRequestRequestTypeDef, _OptionalCreateTokenRequestRequestTypeDef
):
    pass


CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "TokenId": str,
        "TokenType": Literal["REFRESH_TOKEN"],
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDatetimeRangeOutputTypeDef = TypedDict(
    "_RequiredDatetimeRangeOutputTypeDef",
    {
        "Begin": str,
    },
)
_OptionalDatetimeRangeOutputTypeDef = TypedDict(
    "_OptionalDatetimeRangeOutputTypeDef",
    {
        "End": str,
    },
    total=False,
)


class DatetimeRangeOutputTypeDef(
    _RequiredDatetimeRangeOutputTypeDef, _OptionalDatetimeRangeOutputTypeDef
):
    pass


_RequiredDeleteGrantRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
        "Version": str,
    },
)
_OptionalDeleteGrantRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteGrantRequestRequestTypeDef",
    {
        "StatusReason": str,
    },
    total=False,
)


class DeleteGrantRequestRequestTypeDef(
    _RequiredDeleteGrantRequestRequestTypeDef, _OptionalDeleteGrantRequestRequestTypeDef
):
    pass


DeleteGrantResponseTypeDef = TypedDict(
    "DeleteGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

DeleteLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "DeleteLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)

DeleteLicenseRequestRequestTypeDef = TypedDict(
    "DeleteLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "SourceVersion": str,
    },
)

DeleteLicenseResponseTypeDef = TypedDict(
    "DeleteLicenseResponseTypeDef",
    {
        "Status": LicenseDeletionStatusType,
        "DeletionDate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTokenRequestRequestTypeDef = TypedDict(
    "DeleteTokenRequestRequestTypeDef",
    {
        "TokenId": str,
    },
)

_RequiredEntitlementOutputTypeDef = TypedDict(
    "_RequiredEntitlementOutputTypeDef",
    {
        "Name": str,
        "Unit": EntitlementUnitType,
    },
)
_OptionalEntitlementOutputTypeDef = TypedDict(
    "_OptionalEntitlementOutputTypeDef",
    {
        "Value": str,
        "MaxCount": int,
        "Overage": bool,
        "AllowCheckIn": bool,
    },
    total=False,
)


class EntitlementOutputTypeDef(
    _RequiredEntitlementOutputTypeDef, _OptionalEntitlementOutputTypeDef
):
    pass


_RequiredEntitlementUsageTypeDef = TypedDict(
    "_RequiredEntitlementUsageTypeDef",
    {
        "Name": str,
        "ConsumedValue": str,
        "Unit": EntitlementDataUnitType,
    },
)
_OptionalEntitlementUsageTypeDef = TypedDict(
    "_OptionalEntitlementUsageTypeDef",
    {
        "MaxCount": str,
    },
    total=False,
)


class EntitlementUsageTypeDef(_RequiredEntitlementUsageTypeDef, _OptionalEntitlementUsageTypeDef):
    pass


_RequiredExtendLicenseConsumptionRequestRequestTypeDef = TypedDict(
    "_RequiredExtendLicenseConsumptionRequestRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
    },
)
_OptionalExtendLicenseConsumptionRequestRequestTypeDef = TypedDict(
    "_OptionalExtendLicenseConsumptionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ExtendLicenseConsumptionRequestRequestTypeDef(
    _RequiredExtendLicenseConsumptionRequestRequestTypeDef,
    _OptionalExtendLicenseConsumptionRequestRequestTypeDef,
):
    pass


ExtendLicenseConsumptionResponseTypeDef = TypedDict(
    "ExtendLicenseConsumptionResponseTypeDef",
    {
        "LicenseConsumptionToken": str,
        "Expiration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
    total=False,
)

_RequiredGetAccessTokenRequestRequestTypeDef = TypedDict(
    "_RequiredGetAccessTokenRequestRequestTypeDef",
    {
        "Token": str,
    },
)
_OptionalGetAccessTokenRequestRequestTypeDef = TypedDict(
    "_OptionalGetAccessTokenRequestRequestTypeDef",
    {
        "TokenProperties": Sequence[str],
    },
    total=False,
)


class GetAccessTokenRequestRequestTypeDef(
    _RequiredGetAccessTokenRequestRequestTypeDef, _OptionalGetAccessTokenRequestRequestTypeDef
):
    pass


GetAccessTokenResponseTypeDef = TypedDict(
    "GetAccessTokenResponseTypeDef",
    {
        "AccessToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGrantRequestRequestTypeDef = TypedDict(
    "_RequiredGetGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)
_OptionalGetGrantRequestRequestTypeDef = TypedDict(
    "_OptionalGetGrantRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class GetGrantRequestRequestTypeDef(
    _RequiredGetGrantRequestRequestTypeDef, _OptionalGetGrantRequestRequestTypeDef
):
    pass


GetLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "GetLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "AssociationCount": int,
    },
    total=False,
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

GetLicenseConversionTaskRequestRequestTypeDef = TypedDict(
    "GetLicenseConversionTaskRequestRequestTypeDef",
    {
        "LicenseConversionTaskId": str,
    },
)

LicenseConversionContextOutputTypeDef = TypedDict(
    "LicenseConversionContextOutputTypeDef",
    {
        "UsageOperation": str,
    },
    total=False,
)

GetLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)

_RequiredGetLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredGetLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)
_OptionalGetLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalGetLicenseRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class GetLicenseRequestRequestTypeDef(
    _RequiredGetLicenseRequestRequestTypeDef, _OptionalGetLicenseRequestRequestTypeDef
):
    pass


GetLicenseUsageRequestRequestTypeDef = TypedDict(
    "GetLicenseUsageRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)

OrganizationConfigurationOutputTypeDef = TypedDict(
    "OrganizationConfigurationOutputTypeDef",
    {
        "EnableIntegration": bool,
    },
)

OptionsOutputTypeDef = TypedDict(
    "OptionsOutputTypeDef",
    {
        "ActivationOverrideBehavior": ActivationOverrideBehaviorType,
    },
    total=False,
)

IssuerDetailsTypeDef = TypedDict(
    "IssuerDetailsTypeDef",
    {
        "Name": str,
        "SignKey": str,
        "KeyFingerprint": str,
    },
    total=False,
)

ReceivedMetadataTypeDef = TypedDict(
    "ReceivedMetadataTypeDef",
    {
        "ReceivedStatus": ReceivedStatusType,
        "ReceivedStatusReason": str,
        "AllowedOperations": List[AllowedOperationType],
    },
    total=False,
)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef",
    {
        "Name": str,
        "Condition": InventoryFilterConditionType,
    },
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceTypeType,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "AmiAssociationScope": str,
    },
    total=False,
)

LicenseConfigurationUsageTypeDef = TypedDict(
    "LicenseConfigurationUsageTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceTypeType,
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)

_RequiredLicenseSpecificationOutputTypeDef = TypedDict(
    "_RequiredLicenseSpecificationOutputTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalLicenseSpecificationOutputTypeDef = TypedDict(
    "_OptionalLicenseSpecificationOutputTypeDef",
    {
        "AmiAssociationScope": str,
    },
    total=False,
)


class LicenseSpecificationOutputTypeDef(
    _RequiredLicenseSpecificationOutputTypeDef, _OptionalLicenseSpecificationOutputTypeDef
):
    pass


_RequiredLicenseSpecificationTypeDef = TypedDict(
    "_RequiredLicenseSpecificationTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalLicenseSpecificationTypeDef = TypedDict(
    "_OptionalLicenseSpecificationTypeDef",
    {
        "AmiAssociationScope": str,
    },
    total=False,
)


class LicenseSpecificationTypeDef(
    _RequiredLicenseSpecificationTypeDef, _OptionalLicenseSpecificationTypeDef
):
    pass


_RequiredListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef = TypedDict(
    "_RequiredListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef = TypedDict(
    "_OptionalListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef(
    _RequiredListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef,
    _OptionalListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef,
):
    pass


_RequiredListAssociationsForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListAssociationsForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAssociationsForLicenseConfigurationRequestRequestTypeDef(
    _RequiredListAssociationsForLicenseConfigurationRequestRequestTypeDef,
    _OptionalListAssociationsForLicenseConfigurationRequestRequestTypeDef,
):
    pass


_RequiredListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef(
    _RequiredListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef,
    _OptionalListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef,
):
    pass


_RequiredListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef = TypedDict(
    "_RequiredListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef = TypedDict(
    "_OptionalListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef(
    _RequiredListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef,
    _OptionalListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef,
):
    pass


_RequiredListLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListLicenseSpecificationsForResourceRequestRequestTypeDef(
    _RequiredListLicenseSpecificationsForResourceRequestRequestTypeDef,
    _OptionalListLicenseSpecificationsForResourceRequestRequestTypeDef,
):
    pass


_RequiredListLicenseVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLicenseVersionsRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)
_OptionalListLicenseVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLicenseVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListLicenseVersionsRequestRequestTypeDef(
    _RequiredListLicenseVersionsRequestRequestTypeDef,
    _OptionalListLicenseVersionsRequestRequestTypeDef,
):
    pass


ResourceInventoryTypeDef = TypedDict(
    "ResourceInventoryTypeDef",
    {
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

TokenDataTypeDef = TypedDict(
    "TokenDataTypeDef",
    {
        "TokenId": str,
        "TokenType": str,
        "LicenseArn": str,
        "ExpirationTime": str,
        "TokenProperties": List[str],
        "RoleArns": List[str],
        "Status": str,
    },
    total=False,
)

OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef",
    {
        "EnableIntegration": bool,
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

_RequiredProductInformationFilterOutputTypeDef = TypedDict(
    "_RequiredProductInformationFilterOutputTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterComparator": str,
    },
)
_OptionalProductInformationFilterOutputTypeDef = TypedDict(
    "_OptionalProductInformationFilterOutputTypeDef",
    {
        "ProductInformationFilterValue": List[str],
    },
    total=False,
)


class ProductInformationFilterOutputTypeDef(
    _RequiredProductInformationFilterOutputTypeDef, _OptionalProductInformationFilterOutputTypeDef
):
    pass


_RequiredProductInformationFilterTypeDef = TypedDict(
    "_RequiredProductInformationFilterTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterComparator": str,
    },
)
_OptionalProductInformationFilterTypeDef = TypedDict(
    "_OptionalProductInformationFilterTypeDef",
    {
        "ProductInformationFilterValue": Sequence[str],
    },
    total=False,
)


class ProductInformationFilterTypeDef(
    _RequiredProductInformationFilterTypeDef, _OptionalProductInformationFilterTypeDef
):
    pass


RejectGrantRequestRequestTypeDef = TypedDict(
    "RejectGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)

RejectGrantResponseTypeDef = TypedDict(
    "RejectGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportContextOutputTypeDef = TypedDict(
    "ReportContextOutputTypeDef",
    {
        "licenseConfigurationArns": List[str],
    },
)

ReportFrequencyOutputTypeDef = TypedDict(
    "ReportFrequencyOutputTypeDef",
    {
        "value": int,
        "period": ReportFrequencyTypeType,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredCheckoutLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredCheckoutLicenseRequestRequestTypeDef",
    {
        "ProductSKU": str,
        "CheckoutType": CheckoutTypeType,
        "KeyFingerprint": str,
        "Entitlements": Sequence[EntitlementDataTypeDef],
        "ClientToken": str,
    },
)
_OptionalCheckoutLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalCheckoutLicenseRequestRequestTypeDef",
    {
        "Beneficiary": str,
        "NodeId": str,
    },
    total=False,
)


class CheckoutLicenseRequestRequestTypeDef(
    _RequiredCheckoutLicenseRequestRequestTypeDef, _OptionalCheckoutLicenseRequestRequestTypeDef
):
    pass


_RequiredCheckoutBorrowLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredCheckoutBorrowLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "Entitlements": Sequence[EntitlementDataTypeDef],
        "DigitalSignatureMethod": Literal["JWT_PS384"],
        "ClientToken": str,
    },
)
_OptionalCheckoutBorrowLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalCheckoutBorrowLicenseRequestRequestTypeDef",
    {
        "NodeId": str,
        "CheckoutMetadata": Sequence[MetadataTypeDef],
    },
    total=False,
)


class CheckoutBorrowLicenseRequestRequestTypeDef(
    _RequiredCheckoutBorrowLicenseRequestRequestTypeDef,
    _OptionalCheckoutBorrowLicenseRequestRequestTypeDef,
):
    pass


CheckoutLicenseResponseTypeDef = TypedDict(
    "CheckoutLicenseResponseTypeDef",
    {
        "CheckoutType": CheckoutTypeType,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List[EntitlementDataOutputTypeDef],
        "SignedToken": str,
        "NodeId": str,
        "IssuedAt": str,
        "Expiration": str,
        "LicenseArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CheckoutBorrowLicenseResponseTypeDef = TypedDict(
    "CheckoutBorrowLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List[EntitlementDataOutputTypeDef],
        "NodeId": str,
        "SignedToken": str,
        "IssuedAt": str,
        "Expiration": str,
        "CheckoutMetadata": List[MetadataOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LicenseOperationFailureTypeDef = TypedDict(
    "LicenseOperationFailureTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceTypeType,
        "ErrorMessage": str,
        "FailureTime": datetime,
        "OperationName": str,
        "ResourceOwnerId": str,
        "OperationRequestedBy": str,
        "MetadataList": List[MetadataOutputTypeDef],
    },
    total=False,
)

ConsumptionConfigurationOutputTypeDef = TypedDict(
    "ConsumptionConfigurationOutputTypeDef",
    {
        "RenewType": RenewTypeType,
        "ProvisionalConfiguration": ProvisionalConfigurationOutputTypeDef,
        "BorrowConfiguration": BorrowConfigurationOutputTypeDef,
    },
    total=False,
)

ConsumptionConfigurationTypeDef = TypedDict(
    "ConsumptionConfigurationTypeDef",
    {
        "RenewType": RenewTypeType,
        "ProvisionalConfiguration": ProvisionalConfigurationTypeDef,
        "BorrowConfiguration": BorrowConfigurationTypeDef,
    },
    total=False,
)

_RequiredCreateGrantVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGrantVersionRequestRequestTypeDef",
    {
        "ClientToken": str,
        "GrantArn": str,
    },
)
_OptionalCreateGrantVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGrantVersionRequestRequestTypeDef",
    {
        "GrantName": str,
        "AllowedOperations": Sequence[AllowedOperationType],
        "Status": GrantStatusType,
        "StatusReason": str,
        "SourceVersion": str,
        "Options": OptionsTypeDef,
    },
    total=False,
)


class CreateGrantVersionRequestRequestTypeDef(
    _RequiredCreateGrantVersionRequestRequestTypeDef,
    _OptionalCreateGrantVersionRequestRequestTypeDef,
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

CreateLicenseConversionTaskForResourceRequestRequestTypeDef = TypedDict(
    "CreateLicenseConversionTaskForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "SourceLicenseContext": LicenseConversionContextTypeDef,
        "DestinationLicenseContext": LicenseConversionContextTypeDef,
    },
)

_RequiredCreateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "ReportGeneratorName": str,
        "Type": Sequence[ReportTypeType],
        "ReportContext": ReportContextTypeDef,
        "ReportFrequency": ReportFrequencyTypeDef,
        "ClientToken": str,
    },
)
_OptionalCreateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateLicenseManagerReportGeneratorRequestRequestTypeDef(
    _RequiredCreateLicenseManagerReportGeneratorRequestRequestTypeDef,
    _OptionalCreateLicenseManagerReportGeneratorRequestRequestTypeDef,
):
    pass


_RequiredUpdateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ReportGeneratorName": str,
        "Type": Sequence[ReportTypeType],
        "ReportContext": ReportContextTypeDef,
        "ReportFrequency": ReportFrequencyTypeDef,
        "ClientToken": str,
    },
)
_OptionalUpdateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateLicenseManagerReportGeneratorRequestRequestTypeDef(
    _RequiredUpdateLicenseManagerReportGeneratorRequestRequestTypeDef,
    _OptionalUpdateLicenseManagerReportGeneratorRequestRequestTypeDef,
):
    pass


LicenseUsageTypeDef = TypedDict(
    "LicenseUsageTypeDef",
    {
        "EntitlementUsages": List[EntitlementUsageTypeDef],
    },
    total=False,
)

ListDistributedGrantsRequestRequestTypeDef = TypedDict(
    "ListDistributedGrantsRequestRequestTypeDef",
    {
        "GrantArns": Sequence[str],
        "Filters": Sequence[FilterTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateTypeDef = TypedDict(
    "ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateTypeDef",
    {
        "LicenseConfigurationArns": Sequence[str],
        "Filters": Sequence[FilterTypeDef],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListLicenseConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLicenseConfigurationsRequestRequestTypeDef",
    {
        "LicenseConfigurationArns": Sequence[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": Sequence[FilterTypeDef],
    },
    total=False,
)

ListLicenseConversionTasksRequestRequestTypeDef = TypedDict(
    "ListLicenseConversionTasksRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": Sequence[FilterTypeDef],
    },
    total=False,
)

ListLicenseManagerReportGeneratorsRequestRequestTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsRequestRequestTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLicensesRequestRequestTypeDef = TypedDict(
    "ListLicensesRequestRequestTypeDef",
    {
        "LicenseArns": Sequence[str],
        "Filters": Sequence[FilterTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListReceivedGrantsForOrganizationRequestRequestTypeDef = TypedDict(
    "_RequiredListReceivedGrantsForOrganizationRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)
_OptionalListReceivedGrantsForOrganizationRequestRequestTypeDef = TypedDict(
    "_OptionalListReceivedGrantsForOrganizationRequestRequestTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListReceivedGrantsForOrganizationRequestRequestTypeDef(
    _RequiredListReceivedGrantsForOrganizationRequestRequestTypeDef,
    _OptionalListReceivedGrantsForOrganizationRequestRequestTypeDef,
):
    pass


ListReceivedGrantsRequestRequestTypeDef = TypedDict(
    "ListReceivedGrantsRequestRequestTypeDef",
    {
        "GrantArns": Sequence[str],
        "Filters": Sequence[FilterTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReceivedLicensesForOrganizationRequestRequestTypeDef = TypedDict(
    "ListReceivedLicensesForOrganizationRequestRequestTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReceivedLicensesRequestRequestTypeDef = TypedDict(
    "ListReceivedLicensesRequestRequestTypeDef",
    {
        "LicenseArns": Sequence[str],
        "Filters": Sequence[FilterTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTokensRequestRequestTypeDef = TypedDict(
    "ListTokensRequestRequestTypeDef",
    {
        "TokenIds": Sequence[str],
        "Filters": Sequence[FilterTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef = TypedDict(
    "_RequiredListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef = TypedDict(
    "_OptionalListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef(
    _RequiredListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef,
    _OptionalListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef,
):
    pass


_RequiredListUsageForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredListUsageForLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListUsageForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalListUsageForLicenseConfigurationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": Sequence[FilterTypeDef],
    },
    total=False,
)


class ListUsageForLicenseConfigurationRequestRequestTypeDef(
    _RequiredListUsageForLicenseConfigurationRequestRequestTypeDef,
    _OptionalListUsageForLicenseConfigurationRequestRequestTypeDef,
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseConversionTaskResponseTypeDef = TypedDict(
    "GetLicenseConversionTaskResponseTypeDef",
    {
        "LicenseConversionTaskId": str,
        "ResourceArn": str,
        "SourceLicenseContext": LicenseConversionContextOutputTypeDef,
        "DestinationLicenseContext": LicenseConversionContextOutputTypeDef,
        "StatusMessage": str,
        "Status": LicenseConversionTaskStatusType,
        "StartTime": datetime,
        "LicenseConversionTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LicenseConversionTaskTypeDef = TypedDict(
    "LicenseConversionTaskTypeDef",
    {
        "LicenseConversionTaskId": str,
        "ResourceArn": str,
        "SourceLicenseContext": LicenseConversionContextOutputTypeDef,
        "DestinationLicenseContext": LicenseConversionContextOutputTypeDef,
        "Status": LicenseConversionTaskStatusType,
        "StatusMessage": str,
        "StartTime": datetime,
        "LicenseConversionTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": OrganizationConfigurationOutputTypeDef,
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGrantTypeDef = TypedDict(
    "_RequiredGrantTypeDef",
    {
        "GrantArn": str,
        "GrantName": str,
        "ParentArn": str,
        "LicenseArn": str,
        "GranteePrincipalArn": str,
        "HomeRegion": str,
        "GrantStatus": GrantStatusType,
        "Version": str,
        "GrantedOperations": List[AllowedOperationType],
    },
)
_OptionalGrantTypeDef = TypedDict(
    "_OptionalGrantTypeDef",
    {
        "StatusReason": str,
        "Options": OptionsOutputTypeDef,
    },
    total=False,
)


class GrantTypeDef(_RequiredGrantTypeDef, _OptionalGrantTypeDef):
    pass


ListResourceInventoryRequestListResourceInventoryPaginateTypeDef = TypedDict(
    "ListResourceInventoryRequestListResourceInventoryPaginateTypeDef",
    {
        "Filters": Sequence[InventoryFilterTypeDef],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListResourceInventoryRequestRequestTypeDef = TypedDict(
    "ListResourceInventoryRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": Sequence[InventoryFilterTypeDef],
    },
    total=False,
)

ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[LicenseConfigurationAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[LicenseConfigurationUsageTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List[LicenseSpecificationOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalUpdateLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "AddLicenseSpecifications": Sequence[LicenseSpecificationTypeDef],
        "RemoveLicenseSpecifications": Sequence[LicenseSpecificationTypeDef],
    },
    total=False,
)


class UpdateLicenseSpecificationsForResourceRequestRequestTypeDef(
    _RequiredUpdateLicenseSpecificationsForResourceRequestRequestTypeDef,
    _OptionalUpdateLicenseSpecificationsForResourceRequestRequestTypeDef,
):
    pass


ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List[ResourceInventoryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTokensResponseTypeDef = TypedDict(
    "ListTokensResponseTypeDef",
    {
        "Tokens": List[TokenDataTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "UpdateServiceSettingsRequestRequestTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": OrganizationConfigurationTypeDef,
        "EnableCrossAccountsDiscovery": bool,
    },
    total=False,
)

ProductInformationOutputTypeDef = TypedDict(
    "ProductInformationOutputTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[ProductInformationFilterOutputTypeDef],
    },
)

ProductInformationTypeDef = TypedDict(
    "ProductInformationTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": Sequence[ProductInformationFilterTypeDef],
    },
)

ReportGeneratorTypeDef = TypedDict(
    "ReportGeneratorTypeDef",
    {
        "ReportGeneratorName": str,
        "ReportType": List[ReportTypeType],
        "ReportContext": ReportContextOutputTypeDef,
        "ReportFrequency": ReportFrequencyOutputTypeDef,
        "LicenseManagerReportGeneratorArn": str,
        "LastRunStatus": str,
        "LastRunFailureReason": str,
        "LastReportGenerationTime": str,
        "ReportCreatorAccount": str,
        "Description": str,
        "S3Location": S3LocationTypeDef,
        "CreateTime": str,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

ListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {
        "LicenseOperationFailureList": List[LicenseOperationFailureTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantedLicenseTypeDef = TypedDict(
    "GrantedLicenseTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": IssuerDetailsTypeDef,
        "HomeRegion": str,
        "Status": LicenseStatusType,
        "Validity": DatetimeRangeOutputTypeDef,
        "Beneficiary": str,
        "Entitlements": List[EntitlementOutputTypeDef],
        "ConsumptionConfiguration": ConsumptionConfigurationOutputTypeDef,
        "LicenseMetadata": List[MetadataOutputTypeDef],
        "CreateTime": str,
        "Version": str,
        "ReceivedMetadata": ReceivedMetadataTypeDef,
    },
    total=False,
)

LicenseTypeDef = TypedDict(
    "LicenseTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": IssuerDetailsTypeDef,
        "HomeRegion": str,
        "Status": LicenseStatusType,
        "Validity": DatetimeRangeOutputTypeDef,
        "Beneficiary": str,
        "Entitlements": List[EntitlementOutputTypeDef],
        "ConsumptionConfiguration": ConsumptionConfigurationOutputTypeDef,
        "LicenseMetadata": List[MetadataOutputTypeDef],
        "CreateTime": str,
        "Version": str,
    },
    total=False,
)

_RequiredCreateLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseRequestRequestTypeDef",
    {
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": IssuerTypeDef,
        "HomeRegion": str,
        "Validity": DatetimeRangeTypeDef,
        "Entitlements": Sequence[EntitlementTypeDef],
        "Beneficiary": str,
        "ConsumptionConfiguration": ConsumptionConfigurationTypeDef,
        "ClientToken": str,
    },
)
_OptionalCreateLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseRequestRequestTypeDef",
    {
        "LicenseMetadata": Sequence[MetadataTypeDef],
    },
    total=False,
)


class CreateLicenseRequestRequestTypeDef(
    _RequiredCreateLicenseRequestRequestTypeDef, _OptionalCreateLicenseRequestRequestTypeDef
):
    pass


_RequiredCreateLicenseVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseVersionRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "Issuer": IssuerTypeDef,
        "HomeRegion": str,
        "Validity": DatetimeRangeTypeDef,
        "Entitlements": Sequence[EntitlementTypeDef],
        "ConsumptionConfiguration": ConsumptionConfigurationTypeDef,
        "Status": LicenseStatusType,
        "ClientToken": str,
    },
)
_OptionalCreateLicenseVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseVersionRequestRequestTypeDef",
    {
        "LicenseMetadata": Sequence[MetadataTypeDef],
        "SourceVersion": str,
    },
    total=False,
)


class CreateLicenseVersionRequestRequestTypeDef(
    _RequiredCreateLicenseVersionRequestRequestTypeDef,
    _OptionalCreateLicenseVersionRequestRequestTypeDef,
):
    pass


GetLicenseUsageResponseTypeDef = TypedDict(
    "GetLicenseUsageResponseTypeDef",
    {
        "LicenseUsage": LicenseUsageTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseConversionTasksResponseTypeDef = TypedDict(
    "ListLicenseConversionTasksResponseTypeDef",
    {
        "LicenseConversionTasks": List[LicenseConversionTaskTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGrantResponseTypeDef = TypedDict(
    "GetGrantResponseTypeDef",
    {
        "Grant": GrantTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributedGrantsResponseTypeDef = TypedDict(
    "ListDistributedGrantsResponseTypeDef",
    {
        "Grants": List[GrantTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedGrantsForOrganizationResponseTypeDef = TypedDict(
    "ListReceivedGrantsForOrganizationResponseTypeDef",
    {
        "Grants": List[GrantTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedGrantsResponseTypeDef = TypedDict(
    "ListReceivedGrantsResponseTypeDef",
    {
        "Grants": List[GrantTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseConfigurationResponseTypeDef = TypedDict(
    "GetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingTypeType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[ConsumedLicenseSummaryTypeDef],
        "ManagedResourceSummaryList": List[ManagedResourceSummaryTypeDef],
        "Tags": List[TagOutputTypeDef],
        "ProductInformationList": List[ProductInformationOutputTypeDef],
        "AutomatedDiscoveryInformation": AutomatedDiscoveryInformationTypeDef,
        "DisassociateWhenNotFound": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingTypeType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "DisassociateWhenNotFound": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[ConsumedLicenseSummaryTypeDef],
        "ManagedResourceSummaryList": List[ManagedResourceSummaryTypeDef],
        "ProductInformationList": List[ProductInformationOutputTypeDef],
        "AutomatedDiscoveryInformation": AutomatedDiscoveryInformationTypeDef,
    },
    total=False,
)

_RequiredCreateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "LicenseCountingType": LicenseCountingTypeType,
    },
)
_OptionalCreateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseConfigurationRequestRequestTypeDef",
    {
        "Description": str,
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "LicenseRules": Sequence[str],
        "Tags": Sequence[TagTypeDef],
        "DisassociateWhenNotFound": bool,
        "ProductInformationList": Sequence[ProductInformationTypeDef],
    },
    total=False,
)


class CreateLicenseConfigurationRequestRequestTypeDef(
    _RequiredCreateLicenseConfigurationRequestRequestTypeDef,
    _OptionalCreateLicenseConfigurationRequestRequestTypeDef,
):
    pass


_RequiredUpdateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalUpdateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationStatus": LicenseConfigurationStatusType,
        "LicenseRules": Sequence[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "Name": str,
        "Description": str,
        "ProductInformationList": Sequence[ProductInformationTypeDef],
        "DisassociateWhenNotFound": bool,
    },
    total=False,
)


class UpdateLicenseConfigurationRequestRequestTypeDef(
    _RequiredUpdateLicenseConfigurationRequestRequestTypeDef,
    _OptionalUpdateLicenseConfigurationRequestRequestTypeDef,
):
    pass


GetLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    {
        "ReportGenerator": ReportGeneratorTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseManagerReportGeneratorsResponseTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    {
        "ReportGenerators": List[ReportGeneratorTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedLicensesForOrganizationResponseTypeDef = TypedDict(
    "ListReceivedLicensesForOrganizationResponseTypeDef",
    {
        "Licenses": List[GrantedLicenseTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedLicensesResponseTypeDef = TypedDict(
    "ListReceivedLicensesResponseTypeDef",
    {
        "Licenses": List[GrantedLicenseTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseResponseTypeDef = TypedDict(
    "GetLicenseResponseTypeDef",
    {
        "License": LicenseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseVersionsResponseTypeDef = TypedDict(
    "ListLicenseVersionsResponseTypeDef",
    {
        "Licenses": List[LicenseTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicensesResponseTypeDef = TypedDict(
    "ListLicensesResponseTypeDef",
    {
        "Licenses": List[LicenseTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List[LicenseConfigurationTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
