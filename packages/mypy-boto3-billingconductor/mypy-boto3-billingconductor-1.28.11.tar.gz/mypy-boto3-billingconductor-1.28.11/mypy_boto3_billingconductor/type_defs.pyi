"""
Type annotations for billingconductor service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/type_defs/)

Usage::

    ```python
    from mypy_boto3_billingconductor.type_defs import AccountAssociationsListElementTypeDef

    data: AccountAssociationsListElementTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AssociateResourceErrorReasonType,
    BillingGroupStatusType,
    CurrencyCodeType,
    CustomLineItemRelationshipType,
    CustomLineItemTypeType,
    PricingRuleScopeType,
    PricingRuleTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountAssociationsListElementTypeDef",
    "AccountGroupingTypeDef",
    "AssociateAccountsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociatePricingRulesInputRequestTypeDef",
    "AssociateResourceErrorTypeDef",
    "CustomLineItemBillingPeriodRangeTypeDef",
    "BillingGroupCostReportElementTypeDef",
    "ComputationPreferenceOutputTypeDef",
    "ListBillingGroupAccountGroupingTypeDef",
    "ComputationPreferenceTypeDef",
    "CreateFreeTierConfigTypeDef",
    "CreatePricingPlanInputRequestTypeDef",
    "CustomLineItemFlatChargeDetailsTypeDef",
    "CustomLineItemPercentageChargeDetailsTypeDef",
    "DeleteBillingGroupInputRequestTypeDef",
    "DeletePricingPlanInputRequestTypeDef",
    "DeletePricingRuleInputRequestTypeDef",
    "DisassociateAccountsInputRequestTypeDef",
    "DisassociatePricingRulesInputRequestTypeDef",
    "FreeTierConfigTypeDef",
    "ListAccountAssociationsFilterTypeDef",
    "PaginatorConfigTypeDef",
    "ListBillingGroupCostReportsFilterTypeDef",
    "ListBillingGroupsFilterTypeDef",
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    "ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef",
    "ListCustomLineItemsFilterTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    "ListPricingPlansFilterTypeDef",
    "PricingPlanListElementTypeDef",
    "ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    "ListPricingRulesFilterTypeDef",
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBillingGroupAccountGroupingOutputTypeDef",
    "UpdateBillingGroupAccountGroupingTypeDef",
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    "UpdateFreeTierConfigOutputTypeDef",
    "UpdateFreeTierConfigTypeDef",
    "UpdatePricingPlanInputRequestTypeDef",
    "AssociateAccountsOutputTypeDef",
    "AssociatePricingRulesOutputTypeDef",
    "CreateBillingGroupOutputTypeDef",
    "CreateCustomLineItemOutputTypeDef",
    "CreatePricingPlanOutputTypeDef",
    "CreatePricingRuleOutputTypeDef",
    "DeleteBillingGroupOutputTypeDef",
    "DeleteCustomLineItemOutputTypeDef",
    "DeletePricingPlanOutputTypeDef",
    "DeletePricingRuleOutputTypeDef",
    "DisassociateAccountsOutputTypeDef",
    "DisassociatePricingRulesOutputTypeDef",
    "ListAccountAssociationsOutputTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdatePricingPlanOutputTypeDef",
    "AssociateResourceResponseElementTypeDef",
    "DisassociateResourceResponseElementTypeDef",
    "BatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    "DeleteCustomLineItemInputRequestTypeDef",
    "ListBillingGroupCostReportsOutputTypeDef",
    "BillingGroupListElementTypeDef",
    "CreateBillingGroupInputRequestTypeDef",
    "CreateTieringInputTypeDef",
    "CustomLineItemChargeDetailsTypeDef",
    "TieringTypeDef",
    "ListAccountAssociationsInputRequestTypeDef",
    "ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef",
    "ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef",
    "ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef",
    "ListBillingGroupCostReportsInputRequestTypeDef",
    "ListBillingGroupsInputListBillingGroupsPaginateTypeDef",
    "ListBillingGroupsInputRequestTypeDef",
    "ListCustomLineItemChargeDetailsTypeDef",
    "ListCustomLineItemVersionsFilterTypeDef",
    "ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef",
    "ListCustomLineItemsInputRequestTypeDef",
    "ListPricingPlansInputListPricingPlansPaginateTypeDef",
    "ListPricingPlansInputRequestTypeDef",
    "ListPricingPlansOutputTypeDef",
    "ListPricingRulesInputListPricingRulesPaginateTypeDef",
    "ListPricingRulesInputRequestTypeDef",
    "ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef",
    "ListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    "UpdateBillingGroupOutputTypeDef",
    "UpdateBillingGroupInputRequestTypeDef",
    "UpdateCustomLineItemChargeDetailsTypeDef",
    "UpdateTieringInputOutputTypeDef",
    "UpdateTieringInputTypeDef",
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    "ListBillingGroupsOutputTypeDef",
    "CreatePricingRuleInputRequestTypeDef",
    "CreateCustomLineItemInputRequestTypeDef",
    "PricingRuleListElementTypeDef",
    "CustomLineItemListElementTypeDef",
    "CustomLineItemVersionListElementTypeDef",
    "UpdateCustomLineItemOutputTypeDef",
    "ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef",
    "ListCustomLineItemVersionsInputRequestTypeDef",
    "UpdateCustomLineItemInputRequestTypeDef",
    "UpdatePricingRuleOutputTypeDef",
    "UpdatePricingRuleInputRequestTypeDef",
    "ListPricingRulesOutputTypeDef",
    "ListCustomLineItemsOutputTypeDef",
    "ListCustomLineItemVersionsOutputTypeDef",
)

AccountAssociationsListElementTypeDef = TypedDict(
    "AccountAssociationsListElementTypeDef",
    {
        "AccountId": str,
        "BillingGroupArn": str,
        "AccountName": str,
        "AccountEmail": str,
    },
)

_RequiredAccountGroupingTypeDef = TypedDict(
    "_RequiredAccountGroupingTypeDef",
    {
        "LinkedAccountIds": Sequence[str],
    },
)
_OptionalAccountGroupingTypeDef = TypedDict(
    "_OptionalAccountGroupingTypeDef",
    {
        "AutoAssociate": bool,
    },
    total=False,
)

class AccountGroupingTypeDef(_RequiredAccountGroupingTypeDef, _OptionalAccountGroupingTypeDef):
    pass

AssociateAccountsInputRequestTypeDef = TypedDict(
    "AssociateAccountsInputRequestTypeDef",
    {
        "Arn": str,
        "AccountIds": Sequence[str],
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

AssociatePricingRulesInputRequestTypeDef = TypedDict(
    "AssociatePricingRulesInputRequestTypeDef",
    {
        "Arn": str,
        "PricingRuleArns": Sequence[str],
    },
)

AssociateResourceErrorTypeDef = TypedDict(
    "AssociateResourceErrorTypeDef",
    {
        "Message": str,
        "Reason": AssociateResourceErrorReasonType,
    },
)

_RequiredCustomLineItemBillingPeriodRangeTypeDef = TypedDict(
    "_RequiredCustomLineItemBillingPeriodRangeTypeDef",
    {
        "InclusiveStartBillingPeriod": str,
    },
)
_OptionalCustomLineItemBillingPeriodRangeTypeDef = TypedDict(
    "_OptionalCustomLineItemBillingPeriodRangeTypeDef",
    {
        "ExclusiveEndBillingPeriod": str,
    },
    total=False,
)

class CustomLineItemBillingPeriodRangeTypeDef(
    _RequiredCustomLineItemBillingPeriodRangeTypeDef,
    _OptionalCustomLineItemBillingPeriodRangeTypeDef,
):
    pass

BillingGroupCostReportElementTypeDef = TypedDict(
    "BillingGroupCostReportElementTypeDef",
    {
        "Arn": str,
        "AWSCost": str,
        "ProformaCost": str,
        "Margin": str,
        "MarginPercentage": str,
        "Currency": str,
    },
)

ComputationPreferenceOutputTypeDef = TypedDict(
    "ComputationPreferenceOutputTypeDef",
    {
        "PricingPlanArn": str,
    },
)

ListBillingGroupAccountGroupingTypeDef = TypedDict(
    "ListBillingGroupAccountGroupingTypeDef",
    {
        "AutoAssociate": bool,
    },
)

ComputationPreferenceTypeDef = TypedDict(
    "ComputationPreferenceTypeDef",
    {
        "PricingPlanArn": str,
    },
)

CreateFreeTierConfigTypeDef = TypedDict(
    "CreateFreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)

_RequiredCreatePricingPlanInputRequestTypeDef = TypedDict(
    "_RequiredCreatePricingPlanInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatePricingPlanInputRequestTypeDef = TypedDict(
    "_OptionalCreatePricingPlanInputRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "PricingRuleArns": Sequence[str],
        "Tags": Mapping[str, str],
    },
    total=False,
)

class CreatePricingPlanInputRequestTypeDef(
    _RequiredCreatePricingPlanInputRequestTypeDef, _OptionalCreatePricingPlanInputRequestTypeDef
):
    pass

CustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "CustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

_RequiredCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "_RequiredCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)
_OptionalCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "_OptionalCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "AssociatedValues": Sequence[str],
    },
    total=False,
)

class CustomLineItemPercentageChargeDetailsTypeDef(
    _RequiredCustomLineItemPercentageChargeDetailsTypeDef,
    _OptionalCustomLineItemPercentageChargeDetailsTypeDef,
):
    pass

DeleteBillingGroupInputRequestTypeDef = TypedDict(
    "DeleteBillingGroupInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeletePricingPlanInputRequestTypeDef = TypedDict(
    "DeletePricingPlanInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeletePricingRuleInputRequestTypeDef = TypedDict(
    "DeletePricingRuleInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DisassociateAccountsInputRequestTypeDef = TypedDict(
    "DisassociateAccountsInputRequestTypeDef",
    {
        "Arn": str,
        "AccountIds": Sequence[str],
    },
)

DisassociatePricingRulesInputRequestTypeDef = TypedDict(
    "DisassociatePricingRulesInputRequestTypeDef",
    {
        "Arn": str,
        "PricingRuleArns": Sequence[str],
    },
)

FreeTierConfigTypeDef = TypedDict(
    "FreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)

ListAccountAssociationsFilterTypeDef = TypedDict(
    "ListAccountAssociationsFilterTypeDef",
    {
        "Association": str,
        "AccountId": str,
        "AccountIds": Sequence[str],
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

ListBillingGroupCostReportsFilterTypeDef = TypedDict(
    "ListBillingGroupCostReportsFilterTypeDef",
    {
        "BillingGroupArns": Sequence[str],
    },
    total=False,
)

ListBillingGroupsFilterTypeDef = TypedDict(
    "ListBillingGroupsFilterTypeDef",
    {
        "Arns": Sequence[str],
        "PricingPlan": str,
        "Statuses": Sequence[BillingGroupStatusType],
        "AutoAssociate": bool,
    },
    total=False,
)

ListCustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

ListCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)

ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef = TypedDict(
    "ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef",
    {
        "StartBillingPeriod": str,
        "EndBillingPeriod": str,
    },
    total=False,
)

ListCustomLineItemsFilterTypeDef = TypedDict(
    "ListCustomLineItemsFilterTypeDef",
    {
        "Names": Sequence[str],
        "BillingGroups": Sequence[str],
        "Arns": Sequence[str],
    },
    total=False,
)

_RequiredListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef = TypedDict(
    "_RequiredListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    {
        "PricingRuleArn": str,
    },
)
_OptionalListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef = TypedDict(
    "_OptionalListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef(
    _RequiredListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef,
    _OptionalListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef,
):
    pass

ListPricingPlansFilterTypeDef = TypedDict(
    "ListPricingPlansFilterTypeDef",
    {
        "Arns": Sequence[str],
    },
    total=False,
)

PricingPlanListElementTypeDef = TypedDict(
    "PricingPlanListElementTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "Size": int,
        "CreationTime": int,
        "LastModifiedTime": int,
    },
)

_RequiredListPricingRulesAssociatedToPricingPlanInputRequestTypeDef = TypedDict(
    "_RequiredListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    {
        "PricingPlanArn": str,
    },
)
_OptionalListPricingRulesAssociatedToPricingPlanInputRequestTypeDef = TypedDict(
    "_OptionalListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef(
    _RequiredListPricingRulesAssociatedToPricingPlanInputRequestTypeDef,
    _OptionalListPricingRulesAssociatedToPricingPlanInputRequestTypeDef,
):
    pass

ListPricingRulesFilterTypeDef = TypedDict(
    "ListPricingRulesFilterTypeDef",
    {
        "Arns": Sequence[str],
    },
    total=False,
)

ListResourcesAssociatedToCustomLineItemFilterTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    {
        "Relationship": CustomLineItemRelationshipType,
    },
    total=False,
)

ListResourcesAssociatedToCustomLineItemResponseElementTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    {
        "Arn": str,
        "Relationship": CustomLineItemRelationshipType,
        "EndBillingPeriod": str,
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateBillingGroupAccountGroupingOutputTypeDef = TypedDict(
    "UpdateBillingGroupAccountGroupingOutputTypeDef",
    {
        "AutoAssociate": bool,
    },
)

UpdateBillingGroupAccountGroupingTypeDef = TypedDict(
    "UpdateBillingGroupAccountGroupingTypeDef",
    {
        "AutoAssociate": bool,
    },
    total=False,
)

UpdateCustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

UpdateCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)

UpdateFreeTierConfigOutputTypeDef = TypedDict(
    "UpdateFreeTierConfigOutputTypeDef",
    {
        "Activated": bool,
    },
)

UpdateFreeTierConfigTypeDef = TypedDict(
    "UpdateFreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)

_RequiredUpdatePricingPlanInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePricingPlanInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdatePricingPlanInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePricingPlanInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdatePricingPlanInputRequestTypeDef(
    _RequiredUpdatePricingPlanInputRequestTypeDef, _OptionalUpdatePricingPlanInputRequestTypeDef
):
    pass

AssociateAccountsOutputTypeDef = TypedDict(
    "AssociateAccountsOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociatePricingRulesOutputTypeDef = TypedDict(
    "AssociatePricingRulesOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateBillingGroupOutputTypeDef = TypedDict(
    "CreateBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateCustomLineItemOutputTypeDef = TypedDict(
    "CreateCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePricingPlanOutputTypeDef = TypedDict(
    "CreatePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePricingRuleOutputTypeDef = TypedDict(
    "CreatePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteBillingGroupOutputTypeDef = TypedDict(
    "DeleteBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteCustomLineItemOutputTypeDef = TypedDict(
    "DeleteCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeletePricingPlanOutputTypeDef = TypedDict(
    "DeletePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeletePricingRuleOutputTypeDef = TypedDict(
    "DeletePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisassociateAccountsOutputTypeDef = TypedDict(
    "DisassociateAccountsOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisassociatePricingRulesOutputTypeDef = TypedDict(
    "DisassociatePricingRulesOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAccountAssociationsOutputTypeDef = TypedDict(
    "ListAccountAssociationsOutputTypeDef",
    {
        "LinkedAccounts": List[AccountAssociationsListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPricingPlansAssociatedWithPricingRuleOutputTypeDef = TypedDict(
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingRuleArn": str,
        "PricingPlanArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPricingRulesAssociatedToPricingPlanOutputTypeDef = TypedDict(
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingPlanArn": str,
        "PricingRuleArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePricingPlanOutputTypeDef = TypedDict(
    "UpdatePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Size": int,
        "LastModifiedTime": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociateResourceResponseElementTypeDef = TypedDict(
    "AssociateResourceResponseElementTypeDef",
    {
        "Arn": str,
        "Error": AssociateResourceErrorTypeDef,
    },
)

DisassociateResourceResponseElementTypeDef = TypedDict(
    "DisassociateResourceResponseElementTypeDef",
    {
        "Arn": str,
        "Error": AssociateResourceErrorTypeDef,
    },
)

_RequiredBatchAssociateResourcesToCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    {
        "TargetArn": str,
        "ResourceArns": Sequence[str],
    },
)
_OptionalBatchAssociateResourcesToCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    {
        "BillingPeriodRange": CustomLineItemBillingPeriodRangeTypeDef,
    },
    total=False,
)

class BatchAssociateResourcesToCustomLineItemInputRequestTypeDef(
    _RequiredBatchAssociateResourcesToCustomLineItemInputRequestTypeDef,
    _OptionalBatchAssociateResourcesToCustomLineItemInputRequestTypeDef,
):
    pass

_RequiredBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    {
        "TargetArn": str,
        "ResourceArns": Sequence[str],
    },
)
_OptionalBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    {
        "BillingPeriodRange": CustomLineItemBillingPeriodRangeTypeDef,
    },
    total=False,
)

class BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef(
    _RequiredBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef,
    _OptionalBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef,
):
    pass

_RequiredDeleteCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredDeleteCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDeleteCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalDeleteCustomLineItemInputRequestTypeDef",
    {
        "BillingPeriodRange": CustomLineItemBillingPeriodRangeTypeDef,
    },
    total=False,
)

class DeleteCustomLineItemInputRequestTypeDef(
    _RequiredDeleteCustomLineItemInputRequestTypeDef,
    _OptionalDeleteCustomLineItemInputRequestTypeDef,
):
    pass

ListBillingGroupCostReportsOutputTypeDef = TypedDict(
    "ListBillingGroupCostReportsOutputTypeDef",
    {
        "BillingGroupCostReports": List[BillingGroupCostReportElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BillingGroupListElementTypeDef = TypedDict(
    "BillingGroupListElementTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "PrimaryAccountId": str,
        "ComputationPreference": ComputationPreferenceOutputTypeDef,
        "Size": int,
        "CreationTime": int,
        "LastModifiedTime": int,
        "Status": BillingGroupStatusType,
        "StatusReason": str,
        "AccountGrouping": ListBillingGroupAccountGroupingTypeDef,
    },
)

_RequiredCreateBillingGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateBillingGroupInputRequestTypeDef",
    {
        "Name": str,
        "AccountGrouping": AccountGroupingTypeDef,
        "ComputationPreference": ComputationPreferenceTypeDef,
    },
)
_OptionalCreateBillingGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateBillingGroupInputRequestTypeDef",
    {
        "ClientToken": str,
        "PrimaryAccountId": str,
        "Description": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)

class CreateBillingGroupInputRequestTypeDef(
    _RequiredCreateBillingGroupInputRequestTypeDef, _OptionalCreateBillingGroupInputRequestTypeDef
):
    pass

CreateTieringInputTypeDef = TypedDict(
    "CreateTieringInputTypeDef",
    {
        "FreeTier": CreateFreeTierConfigTypeDef,
    },
)

_RequiredCustomLineItemChargeDetailsTypeDef = TypedDict(
    "_RequiredCustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
    },
)
_OptionalCustomLineItemChargeDetailsTypeDef = TypedDict(
    "_OptionalCustomLineItemChargeDetailsTypeDef",
    {
        "Flat": CustomLineItemFlatChargeDetailsTypeDef,
        "Percentage": CustomLineItemPercentageChargeDetailsTypeDef,
    },
    total=False,
)

class CustomLineItemChargeDetailsTypeDef(
    _RequiredCustomLineItemChargeDetailsTypeDef, _OptionalCustomLineItemChargeDetailsTypeDef
):
    pass

TieringTypeDef = TypedDict(
    "TieringTypeDef",
    {
        "FreeTier": FreeTierConfigTypeDef,
    },
)

ListAccountAssociationsInputRequestTypeDef = TypedDict(
    "ListAccountAssociationsInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListAccountAssociationsFilterTypeDef,
        "NextToken": str,
    },
    total=False,
)

ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef = TypedDict(
    "ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListAccountAssociationsFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef = TypedDict(
    "_RequiredListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef",
    {
        "PricingRuleArn": str,
    },
)
_OptionalListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef = TypedDict(
    "_OptionalListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef",
    {
        "BillingPeriod": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef(
    _RequiredListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef,
    _OptionalListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef,
):
    pass

_RequiredListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef = TypedDict(
    "_RequiredListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef",
    {
        "PricingPlanArn": str,
    },
)
_OptionalListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef = TypedDict(
    "_OptionalListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef",
    {
        "BillingPeriod": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef(
    _RequiredListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef,
    _OptionalListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef,
):
    pass

ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef = TypedDict(
    "ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListBillingGroupCostReportsFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListBillingGroupCostReportsInputRequestTypeDef = TypedDict(
    "ListBillingGroupCostReportsInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": ListBillingGroupCostReportsFilterTypeDef,
    },
    total=False,
)

ListBillingGroupsInputListBillingGroupsPaginateTypeDef = TypedDict(
    "ListBillingGroupsInputListBillingGroupsPaginateTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListBillingGroupsFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListBillingGroupsInputRequestTypeDef = TypedDict(
    "ListBillingGroupsInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": ListBillingGroupsFilterTypeDef,
    },
    total=False,
)

ListCustomLineItemChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemChargeDetailsTypeDef",
    {
        "Flat": ListCustomLineItemFlatChargeDetailsTypeDef,
        "Percentage": ListCustomLineItemPercentageChargeDetailsTypeDef,
        "Type": CustomLineItemTypeType,
    },
)

ListCustomLineItemVersionsFilterTypeDef = TypedDict(
    "ListCustomLineItemVersionsFilterTypeDef",
    {
        "BillingPeriodRange": ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef,
    },
    total=False,
)

ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef = TypedDict(
    "ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListCustomLineItemsFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListCustomLineItemsInputRequestTypeDef = TypedDict(
    "ListCustomLineItemsInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": ListCustomLineItemsFilterTypeDef,
    },
    total=False,
)

ListPricingPlansInputListPricingPlansPaginateTypeDef = TypedDict(
    "ListPricingPlansInputListPricingPlansPaginateTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListPricingPlansFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPricingPlansInputRequestTypeDef = TypedDict(
    "ListPricingPlansInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListPricingPlansFilterTypeDef,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPricingPlansOutputTypeDef = TypedDict(
    "ListPricingPlansOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingPlans": List[PricingPlanListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPricingRulesInputListPricingRulesPaginateTypeDef = TypedDict(
    "ListPricingRulesInputListPricingRulesPaginateTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListPricingRulesFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPricingRulesInputRequestTypeDef = TypedDict(
    "ListPricingRulesInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListPricingRulesFilterTypeDef,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef = TypedDict(
    "_RequiredListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef = TypedDict(
    "_OptionalListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef",
    {
        "BillingPeriod": str,
        "Filters": ListResourcesAssociatedToCustomLineItemFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef(
    _RequiredListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef,
    _OptionalListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef,
):
    pass

_RequiredListResourcesAssociatedToCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListResourcesAssociatedToCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": ListResourcesAssociatedToCustomLineItemFilterTypeDef,
    },
    total=False,
)

class ListResourcesAssociatedToCustomLineItemInputRequestTypeDef(
    _RequiredListResourcesAssociatedToCustomLineItemInputRequestTypeDef,
    _OptionalListResourcesAssociatedToCustomLineItemInputRequestTypeDef,
):
    pass

ListResourcesAssociatedToCustomLineItemOutputTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "AssociatedResources": List[ListResourcesAssociatedToCustomLineItemResponseElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateBillingGroupOutputTypeDef = TypedDict(
    "UpdateBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "PrimaryAccountId": str,
        "PricingPlanArn": str,
        "Size": int,
        "LastModifiedTime": int,
        "Status": BillingGroupStatusType,
        "StatusReason": str,
        "AccountGrouping": UpdateBillingGroupAccountGroupingOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateBillingGroupInputRequestTypeDef = TypedDict(
    "_RequiredUpdateBillingGroupInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdateBillingGroupInputRequestTypeDef = TypedDict(
    "_OptionalUpdateBillingGroupInputRequestTypeDef",
    {
        "Name": str,
        "Status": BillingGroupStatusType,
        "ComputationPreference": ComputationPreferenceTypeDef,
        "Description": str,
        "AccountGrouping": UpdateBillingGroupAccountGroupingTypeDef,
    },
    total=False,
)

class UpdateBillingGroupInputRequestTypeDef(
    _RequiredUpdateBillingGroupInputRequestTypeDef, _OptionalUpdateBillingGroupInputRequestTypeDef
):
    pass

UpdateCustomLineItemChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemChargeDetailsTypeDef",
    {
        "Flat": UpdateCustomLineItemFlatChargeDetailsTypeDef,
        "Percentage": UpdateCustomLineItemPercentageChargeDetailsTypeDef,
    },
    total=False,
)

UpdateTieringInputOutputTypeDef = TypedDict(
    "UpdateTieringInputOutputTypeDef",
    {
        "FreeTier": UpdateFreeTierConfigOutputTypeDef,
    },
)

UpdateTieringInputTypeDef = TypedDict(
    "UpdateTieringInputTypeDef",
    {
        "FreeTier": UpdateFreeTierConfigTypeDef,
    },
)

BatchAssociateResourcesToCustomLineItemOutputTypeDef = TypedDict(
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    {
        "SuccessfullyAssociatedResources": List[AssociateResourceResponseElementTypeDef],
        "FailedAssociatedResources": List[AssociateResourceResponseElementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchDisassociateResourcesFromCustomLineItemOutputTypeDef = TypedDict(
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    {
        "SuccessfullyDisassociatedResources": List[DisassociateResourceResponseElementTypeDef],
        "FailedDisassociatedResources": List[DisassociateResourceResponseElementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListBillingGroupsOutputTypeDef = TypedDict(
    "ListBillingGroupsOutputTypeDef",
    {
        "BillingGroups": List[BillingGroupListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreatePricingRuleInputRequestTypeDef = TypedDict(
    "_RequiredCreatePricingRuleInputRequestTypeDef",
    {
        "Name": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
    },
)
_OptionalCreatePricingRuleInputRequestTypeDef = TypedDict(
    "_OptionalCreatePricingRuleInputRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "ModifierPercentage": float,
        "Service": str,
        "Tags": Mapping[str, str],
        "BillingEntity": str,
        "Tiering": CreateTieringInputTypeDef,
        "UsageType": str,
        "Operation": str,
    },
    total=False,
)

class CreatePricingRuleInputRequestTypeDef(
    _RequiredCreatePricingRuleInputRequestTypeDef, _OptionalCreatePricingRuleInputRequestTypeDef
):
    pass

_RequiredCreateCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredCreateCustomLineItemInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "BillingGroupArn": str,
        "ChargeDetails": CustomLineItemChargeDetailsTypeDef,
    },
)
_OptionalCreateCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalCreateCustomLineItemInputRequestTypeDef",
    {
        "ClientToken": str,
        "BillingPeriodRange": CustomLineItemBillingPeriodRangeTypeDef,
        "Tags": Mapping[str, str],
    },
    total=False,
)

class CreateCustomLineItemInputRequestTypeDef(
    _RequiredCreateCustomLineItemInputRequestTypeDef,
    _OptionalCreateCustomLineItemInputRequestTypeDef,
):
    pass

PricingRuleListElementTypeDef = TypedDict(
    "PricingRuleListElementTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "Service": str,
        "AssociatedPricingPlanCount": int,
        "CreationTime": int,
        "LastModifiedTime": int,
        "BillingEntity": str,
        "Tiering": TieringTypeDef,
        "UsageType": str,
        "Operation": str,
    },
)

CustomLineItemListElementTypeDef = TypedDict(
    "CustomLineItemListElementTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ChargeDetails": ListCustomLineItemChargeDetailsTypeDef,
        "CurrencyCode": CurrencyCodeType,
        "Description": str,
        "ProductCode": str,
        "BillingGroupArn": str,
        "CreationTime": int,
        "LastModifiedTime": int,
        "AssociationSize": int,
    },
)

CustomLineItemVersionListElementTypeDef = TypedDict(
    "CustomLineItemVersionListElementTypeDef",
    {
        "Name": str,
        "ChargeDetails": ListCustomLineItemChargeDetailsTypeDef,
        "CurrencyCode": CurrencyCodeType,
        "Description": str,
        "ProductCode": str,
        "BillingGroupArn": str,
        "CreationTime": int,
        "LastModifiedTime": int,
        "AssociationSize": int,
        "StartBillingPeriod": str,
        "EndBillingPeriod": str,
        "Arn": str,
        "StartTime": int,
    },
)

UpdateCustomLineItemOutputTypeDef = TypedDict(
    "UpdateCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "BillingGroupArn": str,
        "Name": str,
        "Description": str,
        "ChargeDetails": ListCustomLineItemChargeDetailsTypeDef,
        "LastModifiedTime": int,
        "AssociationSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef = TypedDict(
    "_RequiredListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef = TypedDict(
    "_OptionalListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef",
    {
        "Filters": ListCustomLineItemVersionsFilterTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef(
    _RequiredListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef,
    _OptionalListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef,
):
    pass

_RequiredListCustomLineItemVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListCustomLineItemVersionsInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListCustomLineItemVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListCustomLineItemVersionsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": ListCustomLineItemVersionsFilterTypeDef,
    },
    total=False,
)

class ListCustomLineItemVersionsInputRequestTypeDef(
    _RequiredListCustomLineItemVersionsInputRequestTypeDef,
    _OptionalListCustomLineItemVersionsInputRequestTypeDef,
):
    pass

_RequiredUpdateCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdateCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomLineItemInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ChargeDetails": UpdateCustomLineItemChargeDetailsTypeDef,
        "BillingPeriodRange": CustomLineItemBillingPeriodRangeTypeDef,
    },
    total=False,
)

class UpdateCustomLineItemInputRequestTypeDef(
    _RequiredUpdateCustomLineItemInputRequestTypeDef,
    _OptionalUpdateCustomLineItemInputRequestTypeDef,
):
    pass

UpdatePricingRuleOutputTypeDef = TypedDict(
    "UpdatePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "Service": str,
        "AssociatedPricingPlanCount": int,
        "LastModifiedTime": int,
        "BillingEntity": str,
        "Tiering": UpdateTieringInputOutputTypeDef,
        "UsageType": str,
        "Operation": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdatePricingRuleInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePricingRuleInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdatePricingRuleInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePricingRuleInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "Tiering": UpdateTieringInputTypeDef,
    },
    total=False,
)

class UpdatePricingRuleInputRequestTypeDef(
    _RequiredUpdatePricingRuleInputRequestTypeDef, _OptionalUpdatePricingRuleInputRequestTypeDef
):
    pass

ListPricingRulesOutputTypeDef = TypedDict(
    "ListPricingRulesOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingRules": List[PricingRuleListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCustomLineItemsOutputTypeDef = TypedDict(
    "ListCustomLineItemsOutputTypeDef",
    {
        "CustomLineItems": List[CustomLineItemListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCustomLineItemVersionsOutputTypeDef = TypedDict(
    "ListCustomLineItemVersionsOutputTypeDef",
    {
        "CustomLineItemVersions": List[CustomLineItemVersionListElementTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
