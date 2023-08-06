"""
Type annotations for wafv2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/type_defs/)

Usage::

    ```python
    from mypy_boto3_wafv2.type_defs import APIKeySummaryTypeDef

    data: APIKeySummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ActionValueType,
    BodyParsingFallbackBehaviorType,
    ComparisonOperatorType,
    CountryCodeType,
    FailureReasonType,
    FallbackBehaviorType,
    FilterBehaviorType,
    FilterRequirementType,
    ForwardedIPPositionType,
    InspectionLevelType,
    IPAddressVersionType,
    JsonMatchScopeType,
    LabelMatchScopeType,
    MapMatchScopeType,
    OversizeHandlingType,
    PayloadTypeType,
    PlatformType,
    PositionalConstraintType,
    RateBasedStatementAggregateKeyTypeType,
    ResourceTypeType,
    ResponseContentTypeType,
    ScopeType,
    SensitivityLevelType,
    SizeInspectionLimitType,
    TextTransformationTypeType,
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
    "APIKeySummaryTypeDef",
    "AWSManagedRulesBotControlRuleSetOutputTypeDef",
    "AWSManagedRulesBotControlRuleSetTypeDef",
    "ActionConditionOutputTypeDef",
    "ActionConditionTypeDef",
    "AddressFieldOutputTypeDef",
    "AddressFieldTypeDef",
    "AndStatementOutputTypeDef",
    "AndStatementTypeDef",
    "AssociateWebACLRequestRequestTypeDef",
    "RequestBodyAssociatedResourceTypeConfigOutputTypeDef",
    "RequestBodyAssociatedResourceTypeConfigTypeDef",
    "BodyOutputTypeDef",
    "BodyTypeDef",
    "TextTransformationOutputTypeDef",
    "TextTransformationTypeDef",
    "ImmunityTimePropertyOutputTypeDef",
    "ImmunityTimePropertyTypeDef",
    "CaptchaResponseTypeDef",
    "ChallengeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "LabelNameConditionOutputTypeDef",
    "LabelNameConditionTypeDef",
    "CookieMatchPatternOutputTypeDef",
    "CookieMatchPatternTypeDef",
    "CreateAPIKeyRequestRequestTypeDef",
    "TagTypeDef",
    "IPSetSummaryTypeDef",
    "RegexTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "CustomResponseBodyTypeDef",
    "VisibilityConfigTypeDef",
    "RuleGroupSummaryTypeDef",
    "WebACLSummaryTypeDef",
    "CustomHTTPHeaderOutputTypeDef",
    "CustomHTTPHeaderTypeDef",
    "CustomResponseBodyOutputTypeDef",
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeletePermissionPolicyRequestRequestTypeDef",
    "DeleteRegexPatternSetRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteWebACLRequestRequestTypeDef",
    "DescribeAllManagedProductsRequestRequestTypeDef",
    "ManagedProductDescriptorTypeDef",
    "DescribeManagedProductsByVendorRequestRequestTypeDef",
    "DescribeManagedRuleGroupRequestRequestTypeDef",
    "LabelSummaryTypeDef",
    "DisassociateWebACLRequestRequestTypeDef",
    "EmailFieldOutputTypeDef",
    "EmailFieldTypeDef",
    "ExcludedRuleOutputTypeDef",
    "ExcludedRuleTypeDef",
    "HeaderOrderOutputTypeDef",
    "SingleHeaderOutputTypeDef",
    "SingleQueryArgumentOutputTypeDef",
    "HeaderOrderTypeDef",
    "SingleHeaderTypeDef",
    "SingleQueryArgumentTypeDef",
    "VisibilityConfigOutputTypeDef",
    "ForwardedIPConfigOutputTypeDef",
    "ForwardedIPConfigTypeDef",
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    "GetDecryptedAPIKeyRequestRequestTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "IPSetTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetManagedRuleSetRequestRequestTypeDef",
    "GetMobileSdkReleaseRequestRequestTypeDef",
    "GetPermissionPolicyRequestRequestTypeDef",
    "GetRateBasedStatementManagedKeysRequestRequestTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "GetRegexPatternSetRequestRequestTypeDef",
    "GetRuleGroupRequestRequestTypeDef",
    "TimeWindowTypeDef",
    "TimeWindowOutputTypeDef",
    "GetWebACLForResourceRequestRequestTypeDef",
    "GetWebACLRequestRequestTypeDef",
    "HTTPHeaderTypeDef",
    "HeaderMatchPatternOutputTypeDef",
    "HeaderMatchPatternTypeDef",
    "IPSetForwardedIPConfigOutputTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "JsonMatchPatternOutputTypeDef",
    "JsonMatchPatternTypeDef",
    "LabelMatchStatementOutputTypeDef",
    "LabelMatchStatementTypeDef",
    "LabelOutputTypeDef",
    "LabelTypeDef",
    "ListAPIKeysRequestRequestTypeDef",
    "ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    "ManagedRuleGroupVersionTypeDef",
    "ListAvailableManagedRuleGroupsRequestRequestTypeDef",
    "ManagedRuleGroupSummaryTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListManagedRuleSetsRequestRequestTypeDef",
    "ManagedRuleSetSummaryTypeDef",
    "ListMobileSdkReleasesRequestRequestTypeDef",
    "ReleaseSummaryTypeDef",
    "ListRegexPatternSetsRequestRequestTypeDef",
    "ListResourcesForWebACLRequestRequestTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWebACLsRequestRequestTypeDef",
    "PasswordFieldOutputTypeDef",
    "UsernameFieldOutputTypeDef",
    "PasswordFieldTypeDef",
    "UsernameFieldTypeDef",
    "ManagedRuleSetVersionTypeDef",
    "TagOutputTypeDef",
    "NotStatementOutputTypeDef",
    "NotStatementTypeDef",
    "OrStatementOutputTypeDef",
    "OrStatementTypeDef",
    "PhoneNumberFieldOutputTypeDef",
    "PhoneNumberFieldTypeDef",
    "VersionToPublishTypeDef",
    "PutPermissionPolicyRequestRequestTypeDef",
    "RateLimitLabelNamespaceOutputTypeDef",
    "RateLimitLabelNamespaceTypeDef",
    "RegexOutputTypeDef",
    "ResponseInspectionBodyContainsOutputTypeDef",
    "ResponseInspectionBodyContainsTypeDef",
    "ResponseInspectionHeaderOutputTypeDef",
    "ResponseInspectionHeaderTypeDef",
    "ResponseInspectionJsonOutputTypeDef",
    "ResponseInspectionJsonTypeDef",
    "ResponseInspectionStatusCodeOutputTypeDef",
    "ResponseInspectionStatusCodeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef",
    "AssociationConfigOutputTypeDef",
    "AssociationConfigTypeDef",
    "RateLimitCookieOutputTypeDef",
    "RateLimitHeaderOutputTypeDef",
    "RateLimitQueryArgumentOutputTypeDef",
    "RateLimitQueryStringOutputTypeDef",
    "RateLimitUriPathOutputTypeDef",
    "RateLimitCookieTypeDef",
    "RateLimitHeaderTypeDef",
    "RateLimitQueryArgumentTypeDef",
    "RateLimitQueryStringTypeDef",
    "RateLimitUriPathTypeDef",
    "CaptchaConfigOutputTypeDef",
    "ChallengeConfigOutputTypeDef",
    "CaptchaConfigTypeDef",
    "ChallengeConfigTypeDef",
    "CheckCapacityResponseTypeDef",
    "CreateAPIKeyResponseTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    "GetDecryptedAPIKeyResponseTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "ListAPIKeysResponseTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "PutManagedRuleSetVersionsResponseTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateWebACLResponseTypeDef",
    "ConditionOutputTypeDef",
    "ConditionTypeDef",
    "CookiesOutputTypeDef",
    "CookiesTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "CreateRegexPatternSetRequestRequestTypeDef",
    "UpdateRegexPatternSetRequestRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "CreateWebACLResponseTypeDef",
    "ListWebACLsResponseTypeDef",
    "CustomRequestHandlingOutputTypeDef",
    "CustomResponseOutputTypeDef",
    "CustomRequestHandlingTypeDef",
    "CustomResponseTypeDef",
    "DescribeAllManagedProductsResponseTypeDef",
    "DescribeManagedProductsByVendorResponseTypeDef",
    "GeoMatchStatementOutputTypeDef",
    "GeoMatchStatementTypeDef",
    "GetIPSetResponseTypeDef",
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    "GetSampledRequestsRequestRequestTypeDef",
    "HTTPRequestTypeDef",
    "HeadersOutputTypeDef",
    "HeadersTypeDef",
    "IPSetReferenceStatementOutputTypeDef",
    "IPSetReferenceStatementTypeDef",
    "JsonBodyOutputTypeDef",
    "JsonBodyTypeDef",
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    "ListManagedRuleSetsResponseTypeDef",
    "ListMobileSdkReleasesResponseTypeDef",
    "RequestInspectionOutputTypeDef",
    "RequestInspectionTypeDef",
    "ManagedRuleSetTypeDef",
    "MobileSdkReleaseTypeDef",
    "TagInfoForResourceTypeDef",
    "RequestInspectionACFPOutputTypeDef",
    "RequestInspectionACFPTypeDef",
    "PutManagedRuleSetVersionsRequestRequestTypeDef",
    "RegexPatternSetTypeDef",
    "ResponseInspectionOutputTypeDef",
    "ResponseInspectionTypeDef",
    "RateBasedStatementCustomKeyOutputTypeDef",
    "RateBasedStatementCustomKeyTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "AllowActionOutputTypeDef",
    "CaptchaActionOutputTypeDef",
    "ChallengeActionOutputTypeDef",
    "CountActionOutputTypeDef",
    "BlockActionOutputTypeDef",
    "AllowActionTypeDef",
    "CaptchaActionTypeDef",
    "ChallengeActionTypeDef",
    "CountActionTypeDef",
    "BlockActionTypeDef",
    "SampledHTTPRequestTypeDef",
    "FieldToMatchOutputTypeDef",
    "FieldToMatchTypeDef",
    "GetManagedRuleSetResponseTypeDef",
    "GetMobileSdkReleaseResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "AWSManagedRulesACFPRuleSetOutputTypeDef",
    "AWSManagedRulesATPRuleSetOutputTypeDef",
    "AWSManagedRulesACFPRuleSetTypeDef",
    "AWSManagedRulesATPRuleSetTypeDef",
    "RateBasedStatementOutputTypeDef",
    "RateBasedStatementTypeDef",
    "LoggingFilterOutputTypeDef",
    "LoggingFilterTypeDef",
    "OverrideActionOutputTypeDef",
    "DefaultActionOutputTypeDef",
    "RuleActionOutputTypeDef",
    "OverrideActionTypeDef",
    "DefaultActionTypeDef",
    "RuleActionTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "ByteMatchStatementOutputTypeDef",
    "RegexMatchStatementOutputTypeDef",
    "RegexPatternSetReferenceStatementOutputTypeDef",
    "SizeConstraintStatementOutputTypeDef",
    "SqliMatchStatementOutputTypeDef",
    "XssMatchStatementOutputTypeDef",
    "ByteMatchStatementTypeDef",
    "RegexMatchStatementTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "SizeConstraintStatementTypeDef",
    "SqliMatchStatementTypeDef",
    "XssMatchStatementTypeDef",
    "ManagedRuleGroupConfigOutputTypeDef",
    "ManagedRuleGroupConfigTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "RuleActionOverrideOutputTypeDef",
    "RuleOutputTypeDef",
    "RuleSummaryTypeDef",
    "RuleActionOverrideTypeDef",
    "RuleTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutLoggingConfigurationRequestRequestTypeDef",
    "ManagedRuleGroupStatementOutputTypeDef",
    "RuleGroupReferenceStatementOutputTypeDef",
    "RuleGroupTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "ManagedRuleGroupStatementTypeDef",
    "RuleGroupReferenceStatementTypeDef",
    "CheckCapacityRequestRequestTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateWebACLRequestRequestTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateWebACLRequestRequestTypeDef",
    "FirewallManagerStatementTypeDef",
    "StatementOutputTypeDef",
    "GetRuleGroupResponseTypeDef",
    "StatementTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "WebACLTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLResponseTypeDef",
)

APIKeySummaryTypeDef = TypedDict(
    "APIKeySummaryTypeDef",
    {
        "TokenDomains": List[str],
        "APIKey": str,
        "CreationTimestamp": datetime,
        "Version": int,
    },
    total=False,
)

AWSManagedRulesBotControlRuleSetOutputTypeDef = TypedDict(
    "AWSManagedRulesBotControlRuleSetOutputTypeDef",
    {
        "InspectionLevel": InspectionLevelType,
    },
)

AWSManagedRulesBotControlRuleSetTypeDef = TypedDict(
    "AWSManagedRulesBotControlRuleSetTypeDef",
    {
        "InspectionLevel": InspectionLevelType,
    },
)

ActionConditionOutputTypeDef = TypedDict(
    "ActionConditionOutputTypeDef",
    {
        "Action": ActionValueType,
    },
)

ActionConditionTypeDef = TypedDict(
    "ActionConditionTypeDef",
    {
        "Action": ActionValueType,
    },
)

AddressFieldOutputTypeDef = TypedDict(
    "AddressFieldOutputTypeDef",
    {
        "Identifier": str,
    },
)

AddressFieldTypeDef = TypedDict(
    "AddressFieldTypeDef",
    {
        "Identifier": str,
    },
)

AndStatementOutputTypeDef = TypedDict(
    "AndStatementOutputTypeDef",
    {
        "Statements": List["StatementOutputTypeDef"],
    },
)

AndStatementTypeDef = TypedDict(
    "AndStatementTypeDef",
    {
        "Statements": Sequence["StatementTypeDef"],
    },
)

AssociateWebACLRequestRequestTypeDef = TypedDict(
    "AssociateWebACLRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "ResourceArn": str,
    },
)

RequestBodyAssociatedResourceTypeConfigOutputTypeDef = TypedDict(
    "RequestBodyAssociatedResourceTypeConfigOutputTypeDef",
    {
        "DefaultSizeInspectionLimit": SizeInspectionLimitType,
    },
)

RequestBodyAssociatedResourceTypeConfigTypeDef = TypedDict(
    "RequestBodyAssociatedResourceTypeConfigTypeDef",
    {
        "DefaultSizeInspectionLimit": SizeInspectionLimitType,
    },
)

BodyOutputTypeDef = TypedDict(
    "BodyOutputTypeDef",
    {
        "OversizeHandling": OversizeHandlingType,
    },
    total=False,
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "OversizeHandling": OversizeHandlingType,
    },
    total=False,
)

TextTransformationOutputTypeDef = TypedDict(
    "TextTransformationOutputTypeDef",
    {
        "Priority": int,
        "Type": TextTransformationTypeType,
    },
)

TextTransformationTypeDef = TypedDict(
    "TextTransformationTypeDef",
    {
        "Priority": int,
        "Type": TextTransformationTypeType,
    },
)

ImmunityTimePropertyOutputTypeDef = TypedDict(
    "ImmunityTimePropertyOutputTypeDef",
    {
        "ImmunityTime": int,
    },
)

ImmunityTimePropertyTypeDef = TypedDict(
    "ImmunityTimePropertyTypeDef",
    {
        "ImmunityTime": int,
    },
)

CaptchaResponseTypeDef = TypedDict(
    "CaptchaResponseTypeDef",
    {
        "ResponseCode": int,
        "SolveTimestamp": int,
        "FailureReason": FailureReasonType,
    },
    total=False,
)

ChallengeResponseTypeDef = TypedDict(
    "ChallengeResponseTypeDef",
    {
        "ResponseCode": int,
        "SolveTimestamp": int,
        "FailureReason": FailureReasonType,
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

LabelNameConditionOutputTypeDef = TypedDict(
    "LabelNameConditionOutputTypeDef",
    {
        "LabelName": str,
    },
)

LabelNameConditionTypeDef = TypedDict(
    "LabelNameConditionTypeDef",
    {
        "LabelName": str,
    },
)

CookieMatchPatternOutputTypeDef = TypedDict(
    "CookieMatchPatternOutputTypeDef",
    {
        "All": Dict[str, Any],
        "IncludedCookies": List[str],
        "ExcludedCookies": List[str],
    },
    total=False,
)

CookieMatchPatternTypeDef = TypedDict(
    "CookieMatchPatternTypeDef",
    {
        "All": Mapping[str, Any],
        "IncludedCookies": Sequence[str],
        "ExcludedCookies": Sequence[str],
    },
    total=False,
)

CreateAPIKeyRequestRequestTypeDef = TypedDict(
    "CreateAPIKeyRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "TokenDomains": Sequence[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

RegexTypeDef = TypedDict(
    "RegexTypeDef",
    {
        "RegexString": str,
    },
    total=False,
)

RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

CustomResponseBodyTypeDef = TypedDict(
    "CustomResponseBodyTypeDef",
    {
        "ContentType": ResponseContentTypeType,
        "Content": str,
    },
)

VisibilityConfigTypeDef = TypedDict(
    "VisibilityConfigTypeDef",
    {
        "SampledRequestsEnabled": bool,
        "CloudWatchMetricsEnabled": bool,
        "MetricName": str,
    },
)

RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

CustomHTTPHeaderOutputTypeDef = TypedDict(
    "CustomHTTPHeaderOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

CustomHTTPHeaderTypeDef = TypedDict(
    "CustomHTTPHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

CustomResponseBodyOutputTypeDef = TypedDict(
    "CustomResponseBodyOutputTypeDef",
    {
        "ContentType": ResponseContentTypeType,
        "Content": str,
    },
)

DeleteFirewallManagerRuleGroupsRequestRequestTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "WebACLLockToken": str,
    },
)

DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeletePermissionPolicyRequestRequestTypeDef = TypedDict(
    "DeletePermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteRegexPatternSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteWebACLRequestRequestTypeDef = TypedDict(
    "DeleteWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DescribeAllManagedProductsRequestRequestTypeDef = TypedDict(
    "DescribeAllManagedProductsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)

ManagedProductDescriptorTypeDef = TypedDict(
    "ManagedProductDescriptorTypeDef",
    {
        "VendorName": str,
        "ManagedRuleSetName": str,
        "ProductId": str,
        "ProductLink": str,
        "ProductTitle": str,
        "ProductDescription": str,
        "SnsTopicArn": str,
        "IsVersioningSupported": bool,
        "IsAdvancedManagedRuleSet": bool,
    },
    total=False,
)

DescribeManagedProductsByVendorRequestRequestTypeDef = TypedDict(
    "DescribeManagedProductsByVendorRequestRequestTypeDef",
    {
        "VendorName": str,
        "Scope": ScopeType,
    },
)

_RequiredDescribeManagedRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeManagedRuleGroupRequestRequestTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Scope": ScopeType,
    },
)
_OptionalDescribeManagedRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeManagedRuleGroupRequestRequestTypeDef",
    {
        "VersionName": str,
    },
    total=False,
)


class DescribeManagedRuleGroupRequestRequestTypeDef(
    _RequiredDescribeManagedRuleGroupRequestRequestTypeDef,
    _OptionalDescribeManagedRuleGroupRequestRequestTypeDef,
):
    pass


LabelSummaryTypeDef = TypedDict(
    "LabelSummaryTypeDef",
    {
        "Name": str,
    },
    total=False,
)

DisassociateWebACLRequestRequestTypeDef = TypedDict(
    "DisassociateWebACLRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

EmailFieldOutputTypeDef = TypedDict(
    "EmailFieldOutputTypeDef",
    {
        "Identifier": str,
    },
)

EmailFieldTypeDef = TypedDict(
    "EmailFieldTypeDef",
    {
        "Identifier": str,
    },
)

ExcludedRuleOutputTypeDef = TypedDict(
    "ExcludedRuleOutputTypeDef",
    {
        "Name": str,
    },
)

ExcludedRuleTypeDef = TypedDict(
    "ExcludedRuleTypeDef",
    {
        "Name": str,
    },
)

HeaderOrderOutputTypeDef = TypedDict(
    "HeaderOrderOutputTypeDef",
    {
        "OversizeHandling": OversizeHandlingType,
    },
)

SingleHeaderOutputTypeDef = TypedDict(
    "SingleHeaderOutputTypeDef",
    {
        "Name": str,
    },
)

SingleQueryArgumentOutputTypeDef = TypedDict(
    "SingleQueryArgumentOutputTypeDef",
    {
        "Name": str,
    },
)

HeaderOrderTypeDef = TypedDict(
    "HeaderOrderTypeDef",
    {
        "OversizeHandling": OversizeHandlingType,
    },
)

SingleHeaderTypeDef = TypedDict(
    "SingleHeaderTypeDef",
    {
        "Name": str,
    },
)

SingleQueryArgumentTypeDef = TypedDict(
    "SingleQueryArgumentTypeDef",
    {
        "Name": str,
    },
)

VisibilityConfigOutputTypeDef = TypedDict(
    "VisibilityConfigOutputTypeDef",
    {
        "SampledRequestsEnabled": bool,
        "CloudWatchMetricsEnabled": bool,
        "MetricName": str,
    },
)

ForwardedIPConfigOutputTypeDef = TypedDict(
    "ForwardedIPConfigOutputTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
    },
)

ForwardedIPConfigTypeDef = TypedDict(
    "ForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
    },
)

GenerateMobileSdkReleaseUrlRequestRequestTypeDef = TypedDict(
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "ReleaseVersion": str,
    },
)

GetDecryptedAPIKeyRequestRequestTypeDef = TypedDict(
    "GetDecryptedAPIKeyRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "APIKey": str,
    },
)

GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

_RequiredIPSetTypeDef = TypedDict(
    "_RequiredIPSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
    },
)
_OptionalIPSetTypeDef = TypedDict(
    "_OptionalIPSetTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class IPSetTypeDef(_RequiredIPSetTypeDef, _OptionalIPSetTypeDef):
    pass


GetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetManagedRuleSetRequestRequestTypeDef = TypedDict(
    "GetManagedRuleSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetMobileSdkReleaseRequestRequestTypeDef = TypedDict(
    "GetMobileSdkReleaseRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "ReleaseVersion": str,
    },
)

GetPermissionPolicyRequestRequestTypeDef = TypedDict(
    "GetPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

_RequiredGetRateBasedStatementManagedKeysRequestRequestTypeDef = TypedDict(
    "_RequiredGetRateBasedStatementManagedKeysRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "WebACLName": str,
        "WebACLId": str,
        "RuleName": str,
    },
)
_OptionalGetRateBasedStatementManagedKeysRequestRequestTypeDef = TypedDict(
    "_OptionalGetRateBasedStatementManagedKeysRequestRequestTypeDef",
    {
        "RuleGroupRuleName": str,
    },
    total=False,
)


class GetRateBasedStatementManagedKeysRequestRequestTypeDef(
    _RequiredGetRateBasedStatementManagedKeysRequestRequestTypeDef,
    _OptionalGetRateBasedStatementManagedKeysRequestRequestTypeDef,
):
    pass


RateBasedStatementManagedKeysIPSetTypeDef = TypedDict(
    "RateBasedStatementManagedKeysIPSetTypeDef",
    {
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
    },
    total=False,
)

GetRegexPatternSetRequestRequestTypeDef = TypedDict(
    "GetRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetRuleGroupRequestRequestTypeDef = TypedDict(
    "GetRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "ARN": str,
    },
    total=False,
)

TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

TimeWindowOutputTypeDef = TypedDict(
    "TimeWindowOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
)

GetWebACLForResourceRequestRequestTypeDef = TypedDict(
    "GetWebACLForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetWebACLRequestRequestTypeDef = TypedDict(
    "GetWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

HTTPHeaderTypeDef = TypedDict(
    "HTTPHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

HeaderMatchPatternOutputTypeDef = TypedDict(
    "HeaderMatchPatternOutputTypeDef",
    {
        "All": Dict[str, Any],
        "IncludedHeaders": List[str],
        "ExcludedHeaders": List[str],
    },
    total=False,
)

HeaderMatchPatternTypeDef = TypedDict(
    "HeaderMatchPatternTypeDef",
    {
        "All": Mapping[str, Any],
        "IncludedHeaders": Sequence[str],
        "ExcludedHeaders": Sequence[str],
    },
    total=False,
)

IPSetForwardedIPConfigOutputTypeDef = TypedDict(
    "IPSetForwardedIPConfigOutputTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
        "Position": ForwardedIPPositionType,
    },
)

IPSetForwardedIPConfigTypeDef = TypedDict(
    "IPSetForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
        "Position": ForwardedIPPositionType,
    },
)

JsonMatchPatternOutputTypeDef = TypedDict(
    "JsonMatchPatternOutputTypeDef",
    {
        "All": Dict[str, Any],
        "IncludedPaths": List[str],
    },
    total=False,
)

JsonMatchPatternTypeDef = TypedDict(
    "JsonMatchPatternTypeDef",
    {
        "All": Mapping[str, Any],
        "IncludedPaths": Sequence[str],
    },
    total=False,
)

LabelMatchStatementOutputTypeDef = TypedDict(
    "LabelMatchStatementOutputTypeDef",
    {
        "Scope": LabelMatchScopeType,
        "Key": str,
    },
)

LabelMatchStatementTypeDef = TypedDict(
    "LabelMatchStatementTypeDef",
    {
        "Scope": LabelMatchScopeType,
        "Key": str,
    },
)

LabelOutputTypeDef = TypedDict(
    "LabelOutputTypeDef",
    {
        "Name": str,
    },
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": str,
    },
)

_RequiredListAPIKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListAPIKeysRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListAPIKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListAPIKeysRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListAPIKeysRequestRequestTypeDef(
    _RequiredListAPIKeysRequestRequestTypeDef, _OptionalListAPIKeysRequestRequestTypeDef
):
    pass


_RequiredListAvailableManagedRuleGroupVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Scope": ScopeType,
    },
)
_OptionalListAvailableManagedRuleGroupVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef(
    _RequiredListAvailableManagedRuleGroupVersionsRequestRequestTypeDef,
    _OptionalListAvailableManagedRuleGroupVersionsRequestRequestTypeDef,
):
    pass


ManagedRuleGroupVersionTypeDef = TypedDict(
    "ManagedRuleGroupVersionTypeDef",
    {
        "Name": str,
        "LastUpdateTimestamp": datetime,
    },
    total=False,
)

_RequiredListAvailableManagedRuleGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListAvailableManagedRuleGroupsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListAvailableManagedRuleGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListAvailableManagedRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListAvailableManagedRuleGroupsRequestRequestTypeDef(
    _RequiredListAvailableManagedRuleGroupsRequestRequestTypeDef,
    _OptionalListAvailableManagedRuleGroupsRequestRequestTypeDef,
):
    pass


ManagedRuleGroupSummaryTypeDef = TypedDict(
    "ManagedRuleGroupSummaryTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "VersioningSupported": bool,
        "Description": str,
    },
    total=False,
)

_RequiredListIPSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListIPSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListIPSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListIPSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListIPSetsRequestRequestTypeDef(
    _RequiredListIPSetsRequestRequestTypeDef, _OptionalListIPSetsRequestRequestTypeDef
):
    pass


_RequiredListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListLoggingConfigurationsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListLoggingConfigurationsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListLoggingConfigurationsRequestRequestTypeDef(
    _RequiredListLoggingConfigurationsRequestRequestTypeDef,
    _OptionalListLoggingConfigurationsRequestRequestTypeDef,
):
    pass


_RequiredListManagedRuleSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListManagedRuleSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListManagedRuleSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListManagedRuleSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListManagedRuleSetsRequestRequestTypeDef(
    _RequiredListManagedRuleSetsRequestRequestTypeDef,
    _OptionalListManagedRuleSetsRequestRequestTypeDef,
):
    pass


ManagedRuleSetSummaryTypeDef = TypedDict(
    "ManagedRuleSetSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
        "LabelNamespace": str,
    },
    total=False,
)

_RequiredListMobileSdkReleasesRequestRequestTypeDef = TypedDict(
    "_RequiredListMobileSdkReleasesRequestRequestTypeDef",
    {
        "Platform": PlatformType,
    },
)
_OptionalListMobileSdkReleasesRequestRequestTypeDef = TypedDict(
    "_OptionalListMobileSdkReleasesRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListMobileSdkReleasesRequestRequestTypeDef(
    _RequiredListMobileSdkReleasesRequestRequestTypeDef,
    _OptionalListMobileSdkReleasesRequestRequestTypeDef,
):
    pass


ReleaseSummaryTypeDef = TypedDict(
    "ReleaseSummaryTypeDef",
    {
        "ReleaseVersion": str,
        "Timestamp": datetime,
    },
    total=False,
)

_RequiredListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListRegexPatternSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListRegexPatternSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListRegexPatternSetsRequestRequestTypeDef(
    _RequiredListRegexPatternSetsRequestRequestTypeDef,
    _OptionalListRegexPatternSetsRequestRequestTypeDef,
):
    pass


_RequiredListResourcesForWebACLRequestRequestTypeDef = TypedDict(
    "_RequiredListResourcesForWebACLRequestRequestTypeDef",
    {
        "WebACLArn": str,
    },
)
_OptionalListResourcesForWebACLRequestRequestTypeDef = TypedDict(
    "_OptionalListResourcesForWebACLRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeType,
    },
    total=False,
)


class ListResourcesForWebACLRequestRequestTypeDef(
    _RequiredListResourcesForWebACLRequestRequestTypeDef,
    _OptionalListResourcesForWebACLRequestRequestTypeDef,
):
    pass


_RequiredListRuleGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListRuleGroupsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListRuleGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListRuleGroupsRequestRequestTypeDef(
    _RequiredListRuleGroupsRequestRequestTypeDef, _OptionalListRuleGroupsRequestRequestTypeDef
):
    pass


_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass


_RequiredListWebACLsRequestRequestTypeDef = TypedDict(
    "_RequiredListWebACLsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListWebACLsRequestRequestTypeDef = TypedDict(
    "_OptionalListWebACLsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)


class ListWebACLsRequestRequestTypeDef(
    _RequiredListWebACLsRequestRequestTypeDef, _OptionalListWebACLsRequestRequestTypeDef
):
    pass


PasswordFieldOutputTypeDef = TypedDict(
    "PasswordFieldOutputTypeDef",
    {
        "Identifier": str,
    },
)

UsernameFieldOutputTypeDef = TypedDict(
    "UsernameFieldOutputTypeDef",
    {
        "Identifier": str,
    },
)

PasswordFieldTypeDef = TypedDict(
    "PasswordFieldTypeDef",
    {
        "Identifier": str,
    },
)

UsernameFieldTypeDef = TypedDict(
    "UsernameFieldTypeDef",
    {
        "Identifier": str,
    },
)

ManagedRuleSetVersionTypeDef = TypedDict(
    "ManagedRuleSetVersionTypeDef",
    {
        "AssociatedRuleGroupArn": str,
        "Capacity": int,
        "ForecastedLifetime": int,
        "PublishTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ExpiryTimestamp": datetime,
    },
    total=False,
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

NotStatementOutputTypeDef = TypedDict(
    "NotStatementOutputTypeDef",
    {
        "Statement": "StatementOutputTypeDef",
    },
)

NotStatementTypeDef = TypedDict(
    "NotStatementTypeDef",
    {
        "Statement": "StatementTypeDef",
    },
)

OrStatementOutputTypeDef = TypedDict(
    "OrStatementOutputTypeDef",
    {
        "Statements": List["StatementOutputTypeDef"],
    },
)

OrStatementTypeDef = TypedDict(
    "OrStatementTypeDef",
    {
        "Statements": Sequence[Dict[str, Any]],
    },
)

PhoneNumberFieldOutputTypeDef = TypedDict(
    "PhoneNumberFieldOutputTypeDef",
    {
        "Identifier": str,
    },
)

PhoneNumberFieldTypeDef = TypedDict(
    "PhoneNumberFieldTypeDef",
    {
        "Identifier": str,
    },
)

VersionToPublishTypeDef = TypedDict(
    "VersionToPublishTypeDef",
    {
        "AssociatedRuleGroupArn": str,
        "ForecastedLifetime": int,
    },
    total=False,
)

PutPermissionPolicyRequestRequestTypeDef = TypedDict(
    "PutPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

RateLimitLabelNamespaceOutputTypeDef = TypedDict(
    "RateLimitLabelNamespaceOutputTypeDef",
    {
        "Namespace": str,
    },
)

RateLimitLabelNamespaceTypeDef = TypedDict(
    "RateLimitLabelNamespaceTypeDef",
    {
        "Namespace": str,
    },
)

RegexOutputTypeDef = TypedDict(
    "RegexOutputTypeDef",
    {
        "RegexString": str,
    },
    total=False,
)

ResponseInspectionBodyContainsOutputTypeDef = TypedDict(
    "ResponseInspectionBodyContainsOutputTypeDef",
    {
        "SuccessStrings": List[str],
        "FailureStrings": List[str],
    },
)

ResponseInspectionBodyContainsTypeDef = TypedDict(
    "ResponseInspectionBodyContainsTypeDef",
    {
        "SuccessStrings": Sequence[str],
        "FailureStrings": Sequence[str],
    },
)

ResponseInspectionHeaderOutputTypeDef = TypedDict(
    "ResponseInspectionHeaderOutputTypeDef",
    {
        "Name": str,
        "SuccessValues": List[str],
        "FailureValues": List[str],
    },
)

ResponseInspectionHeaderTypeDef = TypedDict(
    "ResponseInspectionHeaderTypeDef",
    {
        "Name": str,
        "SuccessValues": Sequence[str],
        "FailureValues": Sequence[str],
    },
)

ResponseInspectionJsonOutputTypeDef = TypedDict(
    "ResponseInspectionJsonOutputTypeDef",
    {
        "Identifier": str,
        "SuccessValues": List[str],
        "FailureValues": List[str],
    },
)

ResponseInspectionJsonTypeDef = TypedDict(
    "ResponseInspectionJsonTypeDef",
    {
        "Identifier": str,
        "SuccessValues": Sequence[str],
        "FailureValues": Sequence[str],
    },
)

ResponseInspectionStatusCodeOutputTypeDef = TypedDict(
    "ResponseInspectionStatusCodeOutputTypeDef",
    {
        "SuccessCodes": List[int],
        "FailureCodes": List[int],
    },
)

ResponseInspectionStatusCodeTypeDef = TypedDict(
    "ResponseInspectionStatusCodeTypeDef",
    {
        "SuccessCodes": Sequence[int],
        "FailureCodes": Sequence[int],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateIPSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "Addresses": Sequence[str],
        "LockToken": str,
    },
)
_OptionalUpdateIPSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIPSetRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateIPSetRequestRequestTypeDef(
    _RequiredUpdateIPSetRequestRequestTypeDef, _OptionalUpdateIPSetRequestRequestTypeDef
):
    pass


UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef = TypedDict(
    "UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
        "VersionToExpire": str,
        "ExpiryTimestamp": Union[datetime, str],
    },
)

AssociationConfigOutputTypeDef = TypedDict(
    "AssociationConfigOutputTypeDef",
    {
        "RequestBody": Dict[
            Literal["CLOUDFRONT"], RequestBodyAssociatedResourceTypeConfigOutputTypeDef
        ],
    },
    total=False,
)

AssociationConfigTypeDef = TypedDict(
    "AssociationConfigTypeDef",
    {
        "RequestBody": Mapping[
            Literal["CLOUDFRONT"], RequestBodyAssociatedResourceTypeConfigTypeDef
        ],
    },
    total=False,
)

RateLimitCookieOutputTypeDef = TypedDict(
    "RateLimitCookieOutputTypeDef",
    {
        "Name": str,
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

RateLimitHeaderOutputTypeDef = TypedDict(
    "RateLimitHeaderOutputTypeDef",
    {
        "Name": str,
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

RateLimitQueryArgumentOutputTypeDef = TypedDict(
    "RateLimitQueryArgumentOutputTypeDef",
    {
        "Name": str,
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

RateLimitQueryStringOutputTypeDef = TypedDict(
    "RateLimitQueryStringOutputTypeDef",
    {
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

RateLimitUriPathOutputTypeDef = TypedDict(
    "RateLimitUriPathOutputTypeDef",
    {
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

RateLimitCookieTypeDef = TypedDict(
    "RateLimitCookieTypeDef",
    {
        "Name": str,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

RateLimitHeaderTypeDef = TypedDict(
    "RateLimitHeaderTypeDef",
    {
        "Name": str,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

RateLimitQueryArgumentTypeDef = TypedDict(
    "RateLimitQueryArgumentTypeDef",
    {
        "Name": str,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

RateLimitQueryStringTypeDef = TypedDict(
    "RateLimitQueryStringTypeDef",
    {
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

RateLimitUriPathTypeDef = TypedDict(
    "RateLimitUriPathTypeDef",
    {
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

CaptchaConfigOutputTypeDef = TypedDict(
    "CaptchaConfigOutputTypeDef",
    {
        "ImmunityTimeProperty": ImmunityTimePropertyOutputTypeDef,
    },
    total=False,
)

ChallengeConfigOutputTypeDef = TypedDict(
    "ChallengeConfigOutputTypeDef",
    {
        "ImmunityTimeProperty": ImmunityTimePropertyOutputTypeDef,
    },
    total=False,
)

CaptchaConfigTypeDef = TypedDict(
    "CaptchaConfigTypeDef",
    {
        "ImmunityTimeProperty": ImmunityTimePropertyTypeDef,
    },
    total=False,
)

ChallengeConfigTypeDef = TypedDict(
    "ChallengeConfigTypeDef",
    {
        "ImmunityTimeProperty": ImmunityTimePropertyTypeDef,
    },
    total=False,
)

CheckCapacityResponseTypeDef = TypedDict(
    "CheckCapacityResponseTypeDef",
    {
        "Capacity": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAPIKeyResponseTypeDef = TypedDict(
    "CreateAPIKeyResponseTypeDef",
    {
        "APIKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteFirewallManagerRuleGroupsResponseTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    {
        "NextWebACLLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GenerateMobileSdkReleaseUrlResponseTypeDef = TypedDict(
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    {
        "Url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDecryptedAPIKeyResponseTypeDef = TypedDict(
    "GetDecryptedAPIKeyResponseTypeDef",
    {
        "TokenDomains": List[str],
        "CreationTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPermissionPolicyResponseTypeDef = TypedDict(
    "GetPermissionPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAPIKeysResponseTypeDef = TypedDict(
    "ListAPIKeysResponseTypeDef",
    {
        "NextMarker": str,
        "APIKeySummaries": List[APIKeySummaryTypeDef],
        "ApplicationIntegrationURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListResourcesForWebACLResponseTypeDef = TypedDict(
    "ListResourcesForWebACLResponseTypeDef",
    {
        "ResourceArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutManagedRuleSetVersionsResponseTypeDef = TypedDict(
    "PutManagedRuleSetVersionsResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateManagedRuleSetVersionExpiryDateResponseTypeDef = TypedDict(
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    {
        "ExpiringVersion": str,
        "ExpiryTimestamp": datetime,
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConditionOutputTypeDef = TypedDict(
    "ConditionOutputTypeDef",
    {
        "ActionCondition": ActionConditionOutputTypeDef,
        "LabelNameCondition": LabelNameConditionOutputTypeDef,
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ActionCondition": ActionConditionTypeDef,
        "LabelNameCondition": LabelNameConditionTypeDef,
    },
    total=False,
)

CookiesOutputTypeDef = TypedDict(
    "CookiesOutputTypeDef",
    {
        "MatchPattern": CookieMatchPatternOutputTypeDef,
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)

CookiesTypeDef = TypedDict(
    "CookiesTypeDef",
    {
        "MatchPattern": CookieMatchPatternTypeDef,
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)

_RequiredCreateIPSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": Sequence[str],
    },
)
_OptionalCreateIPSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIPSetRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateIPSetRequestRequestTypeDef(
    _RequiredCreateIPSetRequestRequestTypeDef, _OptionalCreateIPSetRequestRequestTypeDef
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "Summary": IPSetSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "NextMarker": str,
        "IPSets": List[IPSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "RegularExpressionList": Sequence[RegexTypeDef],
    },
)
_OptionalCreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRegexPatternSetRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateRegexPatternSetRequestRequestTypeDef(
    _RequiredCreateRegexPatternSetRequestRequestTypeDef,
    _OptionalCreateRegexPatternSetRequestRequestTypeDef,
):
    pass


_RequiredUpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "RegularExpressionList": Sequence[RegexTypeDef],
        "LockToken": str,
    },
)
_OptionalUpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRegexPatternSetRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateRegexPatternSetRequestRequestTypeDef(
    _RequiredUpdateRegexPatternSetRequestRequestTypeDef,
    _OptionalUpdateRegexPatternSetRequestRequestTypeDef,
):
    pass


CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "Summary": RegexPatternSetSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRegexPatternSetsResponseTypeDef = TypedDict(
    "ListRegexPatternSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List[RegexPatternSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "Summary": RuleGroupSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List[RuleGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef",
    {
        "Summary": WebACLSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListWebACLsResponseTypeDef = TypedDict(
    "ListWebACLsResponseTypeDef",
    {
        "NextMarker": str,
        "WebACLs": List[WebACLSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CustomRequestHandlingOutputTypeDef = TypedDict(
    "CustomRequestHandlingOutputTypeDef",
    {
        "InsertHeaders": List[CustomHTTPHeaderOutputTypeDef],
    },
)

_RequiredCustomResponseOutputTypeDef = TypedDict(
    "_RequiredCustomResponseOutputTypeDef",
    {
        "ResponseCode": int,
    },
)
_OptionalCustomResponseOutputTypeDef = TypedDict(
    "_OptionalCustomResponseOutputTypeDef",
    {
        "CustomResponseBodyKey": str,
        "ResponseHeaders": List[CustomHTTPHeaderOutputTypeDef],
    },
    total=False,
)


class CustomResponseOutputTypeDef(
    _RequiredCustomResponseOutputTypeDef, _OptionalCustomResponseOutputTypeDef
):
    pass


CustomRequestHandlingTypeDef = TypedDict(
    "CustomRequestHandlingTypeDef",
    {
        "InsertHeaders": Sequence[CustomHTTPHeaderTypeDef],
    },
)

_RequiredCustomResponseTypeDef = TypedDict(
    "_RequiredCustomResponseTypeDef",
    {
        "ResponseCode": int,
    },
)
_OptionalCustomResponseTypeDef = TypedDict(
    "_OptionalCustomResponseTypeDef",
    {
        "CustomResponseBodyKey": str,
        "ResponseHeaders": Sequence[CustomHTTPHeaderTypeDef],
    },
    total=False,
)


class CustomResponseTypeDef(_RequiredCustomResponseTypeDef, _OptionalCustomResponseTypeDef):
    pass


DescribeAllManagedProductsResponseTypeDef = TypedDict(
    "DescribeAllManagedProductsResponseTypeDef",
    {
        "ManagedProducts": List[ManagedProductDescriptorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeManagedProductsByVendorResponseTypeDef = TypedDict(
    "DescribeManagedProductsByVendorResponseTypeDef",
    {
        "ManagedProducts": List[ManagedProductDescriptorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GeoMatchStatementOutputTypeDef = TypedDict(
    "GeoMatchStatementOutputTypeDef",
    {
        "CountryCodes": List[CountryCodeType],
        "ForwardedIPConfig": ForwardedIPConfigOutputTypeDef,
    },
    total=False,
)

GeoMatchStatementTypeDef = TypedDict(
    "GeoMatchStatementTypeDef",
    {
        "CountryCodes": Sequence[CountryCodeType],
        "ForwardedIPConfig": ForwardedIPConfigTypeDef,
    },
    total=False,
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": IPSetTypeDef,
        "LockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRateBasedStatementManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    {
        "ManagedKeysIPV4": RateBasedStatementManagedKeysIPSetTypeDef,
        "ManagedKeysIPV6": RateBasedStatementManagedKeysIPSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSampledRequestsRequestRequestTypeDef = TypedDict(
    "GetSampledRequestsRequestRequestTypeDef",
    {
        "WebAclArn": str,
        "RuleMetricName": str,
        "Scope": ScopeType,
        "TimeWindow": TimeWindowTypeDef,
        "MaxItems": int,
    },
)

HTTPRequestTypeDef = TypedDict(
    "HTTPRequestTypeDef",
    {
        "ClientIP": str,
        "Country": str,
        "URI": str,
        "Method": str,
        "HTTPVersion": str,
        "Headers": List[HTTPHeaderTypeDef],
    },
    total=False,
)

HeadersOutputTypeDef = TypedDict(
    "HeadersOutputTypeDef",
    {
        "MatchPattern": HeaderMatchPatternOutputTypeDef,
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)

HeadersTypeDef = TypedDict(
    "HeadersTypeDef",
    {
        "MatchPattern": HeaderMatchPatternTypeDef,
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)

_RequiredIPSetReferenceStatementOutputTypeDef = TypedDict(
    "_RequiredIPSetReferenceStatementOutputTypeDef",
    {
        "ARN": str,
    },
)
_OptionalIPSetReferenceStatementOutputTypeDef = TypedDict(
    "_OptionalIPSetReferenceStatementOutputTypeDef",
    {
        "IPSetForwardedIPConfig": IPSetForwardedIPConfigOutputTypeDef,
    },
    total=False,
)


class IPSetReferenceStatementOutputTypeDef(
    _RequiredIPSetReferenceStatementOutputTypeDef, _OptionalIPSetReferenceStatementOutputTypeDef
):
    pass


_RequiredIPSetReferenceStatementTypeDef = TypedDict(
    "_RequiredIPSetReferenceStatementTypeDef",
    {
        "ARN": str,
    },
)
_OptionalIPSetReferenceStatementTypeDef = TypedDict(
    "_OptionalIPSetReferenceStatementTypeDef",
    {
        "IPSetForwardedIPConfig": IPSetForwardedIPConfigTypeDef,
    },
    total=False,
)


class IPSetReferenceStatementTypeDef(
    _RequiredIPSetReferenceStatementTypeDef, _OptionalIPSetReferenceStatementTypeDef
):
    pass


_RequiredJsonBodyOutputTypeDef = TypedDict(
    "_RequiredJsonBodyOutputTypeDef",
    {
        "MatchPattern": JsonMatchPatternOutputTypeDef,
        "MatchScope": JsonMatchScopeType,
    },
)
_OptionalJsonBodyOutputTypeDef = TypedDict(
    "_OptionalJsonBodyOutputTypeDef",
    {
        "InvalidFallbackBehavior": BodyParsingFallbackBehaviorType,
        "OversizeHandling": OversizeHandlingType,
    },
    total=False,
)


class JsonBodyOutputTypeDef(_RequiredJsonBodyOutputTypeDef, _OptionalJsonBodyOutputTypeDef):
    pass


_RequiredJsonBodyTypeDef = TypedDict(
    "_RequiredJsonBodyTypeDef",
    {
        "MatchPattern": JsonMatchPatternTypeDef,
        "MatchScope": JsonMatchScopeType,
    },
)
_OptionalJsonBodyTypeDef = TypedDict(
    "_OptionalJsonBodyTypeDef",
    {
        "InvalidFallbackBehavior": BodyParsingFallbackBehaviorType,
        "OversizeHandling": OversizeHandlingType,
    },
    total=False,
)


class JsonBodyTypeDef(_RequiredJsonBodyTypeDef, _OptionalJsonBodyTypeDef):
    pass


ListAvailableManagedRuleGroupVersionsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    {
        "NextMarker": str,
        "Versions": List[ManagedRuleGroupVersionTypeDef],
        "CurrentDefaultVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAvailableManagedRuleGroupsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleGroups": List[ManagedRuleGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListManagedRuleSetsResponseTypeDef = TypedDict(
    "ListManagedRuleSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleSets": List[ManagedRuleSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMobileSdkReleasesResponseTypeDef = TypedDict(
    "ListMobileSdkReleasesResponseTypeDef",
    {
        "ReleaseSummaries": List[ReleaseSummaryTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RequestInspectionOutputTypeDef = TypedDict(
    "RequestInspectionOutputTypeDef",
    {
        "PayloadType": PayloadTypeType,
        "UsernameField": UsernameFieldOutputTypeDef,
        "PasswordField": PasswordFieldOutputTypeDef,
    },
)

RequestInspectionTypeDef = TypedDict(
    "RequestInspectionTypeDef",
    {
        "PayloadType": PayloadTypeType,
        "UsernameField": UsernameFieldTypeDef,
        "PasswordField": PasswordFieldTypeDef,
    },
)

_RequiredManagedRuleSetTypeDef = TypedDict(
    "_RequiredManagedRuleSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
    },
)
_OptionalManagedRuleSetTypeDef = TypedDict(
    "_OptionalManagedRuleSetTypeDef",
    {
        "Description": str,
        "PublishedVersions": Dict[str, ManagedRuleSetVersionTypeDef],
        "RecommendedVersion": str,
        "LabelNamespace": str,
    },
    total=False,
)


class ManagedRuleSetTypeDef(_RequiredManagedRuleSetTypeDef, _OptionalManagedRuleSetTypeDef):
    pass


MobileSdkReleaseTypeDef = TypedDict(
    "MobileSdkReleaseTypeDef",
    {
        "ReleaseVersion": str,
        "Timestamp": datetime,
        "ReleaseNotes": str,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

TagInfoForResourceTypeDef = TypedDict(
    "TagInfoForResourceTypeDef",
    {
        "ResourceARN": str,
        "TagList": List[TagOutputTypeDef],
    },
    total=False,
)

_RequiredRequestInspectionACFPOutputTypeDef = TypedDict(
    "_RequiredRequestInspectionACFPOutputTypeDef",
    {
        "PayloadType": PayloadTypeType,
    },
)
_OptionalRequestInspectionACFPOutputTypeDef = TypedDict(
    "_OptionalRequestInspectionACFPOutputTypeDef",
    {
        "UsernameField": UsernameFieldOutputTypeDef,
        "PasswordField": PasswordFieldOutputTypeDef,
        "EmailField": EmailFieldOutputTypeDef,
        "PhoneNumberFields": List[PhoneNumberFieldOutputTypeDef],
        "AddressFields": List[AddressFieldOutputTypeDef],
    },
    total=False,
)


class RequestInspectionACFPOutputTypeDef(
    _RequiredRequestInspectionACFPOutputTypeDef, _OptionalRequestInspectionACFPOutputTypeDef
):
    pass


_RequiredRequestInspectionACFPTypeDef = TypedDict(
    "_RequiredRequestInspectionACFPTypeDef",
    {
        "PayloadType": PayloadTypeType,
    },
)
_OptionalRequestInspectionACFPTypeDef = TypedDict(
    "_OptionalRequestInspectionACFPTypeDef",
    {
        "UsernameField": UsernameFieldTypeDef,
        "PasswordField": PasswordFieldTypeDef,
        "EmailField": EmailFieldTypeDef,
        "PhoneNumberFields": Sequence[PhoneNumberFieldTypeDef],
        "AddressFields": Sequence[AddressFieldTypeDef],
    },
    total=False,
)


class RequestInspectionACFPTypeDef(
    _RequiredRequestInspectionACFPTypeDef, _OptionalRequestInspectionACFPTypeDef
):
    pass


_RequiredPutManagedRuleSetVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutManagedRuleSetVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)
_OptionalPutManagedRuleSetVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutManagedRuleSetVersionsRequestRequestTypeDef",
    {
        "RecommendedVersion": str,
        "VersionsToPublish": Mapping[str, VersionToPublishTypeDef],
    },
    total=False,
)


class PutManagedRuleSetVersionsRequestRequestTypeDef(
    _RequiredPutManagedRuleSetVersionsRequestRequestTypeDef,
    _OptionalPutManagedRuleSetVersionsRequestRequestTypeDef,
):
    pass


RegexPatternSetTypeDef = TypedDict(
    "RegexPatternSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "Description": str,
        "RegularExpressionList": List[RegexOutputTypeDef],
    },
    total=False,
)

ResponseInspectionOutputTypeDef = TypedDict(
    "ResponseInspectionOutputTypeDef",
    {
        "StatusCode": ResponseInspectionStatusCodeOutputTypeDef,
        "Header": ResponseInspectionHeaderOutputTypeDef,
        "BodyContains": ResponseInspectionBodyContainsOutputTypeDef,
        "Json": ResponseInspectionJsonOutputTypeDef,
    },
    total=False,
)

ResponseInspectionTypeDef = TypedDict(
    "ResponseInspectionTypeDef",
    {
        "StatusCode": ResponseInspectionStatusCodeTypeDef,
        "Header": ResponseInspectionHeaderTypeDef,
        "BodyContains": ResponseInspectionBodyContainsTypeDef,
        "Json": ResponseInspectionJsonTypeDef,
    },
    total=False,
)

RateBasedStatementCustomKeyOutputTypeDef = TypedDict(
    "RateBasedStatementCustomKeyOutputTypeDef",
    {
        "Header": RateLimitHeaderOutputTypeDef,
        "Cookie": RateLimitCookieOutputTypeDef,
        "QueryArgument": RateLimitQueryArgumentOutputTypeDef,
        "QueryString": RateLimitQueryStringOutputTypeDef,
        "HTTPMethod": Dict[str, Any],
        "ForwardedIP": Dict[str, Any],
        "IP": Dict[str, Any],
        "LabelNamespace": RateLimitLabelNamespaceOutputTypeDef,
        "UriPath": RateLimitUriPathOutputTypeDef,
    },
    total=False,
)

RateBasedStatementCustomKeyTypeDef = TypedDict(
    "RateBasedStatementCustomKeyTypeDef",
    {
        "Header": RateLimitHeaderTypeDef,
        "Cookie": RateLimitCookieTypeDef,
        "QueryArgument": RateLimitQueryArgumentTypeDef,
        "QueryString": RateLimitQueryStringTypeDef,
        "HTTPMethod": Mapping[str, Any],
        "ForwardedIP": Mapping[str, Any],
        "IP": Mapping[str, Any],
        "LabelNamespace": RateLimitLabelNamespaceTypeDef,
        "UriPath": RateLimitUriPathTypeDef,
    },
    total=False,
)

FilterOutputTypeDef = TypedDict(
    "FilterOutputTypeDef",
    {
        "Behavior": FilterBehaviorType,
        "Requirement": FilterRequirementType,
        "Conditions": List[ConditionOutputTypeDef],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Behavior": FilterBehaviorType,
        "Requirement": FilterRequirementType,
        "Conditions": Sequence[ConditionTypeDef],
    },
)

AllowActionOutputTypeDef = TypedDict(
    "AllowActionOutputTypeDef",
    {
        "CustomRequestHandling": CustomRequestHandlingOutputTypeDef,
    },
    total=False,
)

CaptchaActionOutputTypeDef = TypedDict(
    "CaptchaActionOutputTypeDef",
    {
        "CustomRequestHandling": CustomRequestHandlingOutputTypeDef,
    },
    total=False,
)

ChallengeActionOutputTypeDef = TypedDict(
    "ChallengeActionOutputTypeDef",
    {
        "CustomRequestHandling": CustomRequestHandlingOutputTypeDef,
    },
    total=False,
)

CountActionOutputTypeDef = TypedDict(
    "CountActionOutputTypeDef",
    {
        "CustomRequestHandling": CustomRequestHandlingOutputTypeDef,
    },
    total=False,
)

BlockActionOutputTypeDef = TypedDict(
    "BlockActionOutputTypeDef",
    {
        "CustomResponse": CustomResponseOutputTypeDef,
    },
    total=False,
)

AllowActionTypeDef = TypedDict(
    "AllowActionTypeDef",
    {
        "CustomRequestHandling": CustomRequestHandlingTypeDef,
    },
    total=False,
)

CaptchaActionTypeDef = TypedDict(
    "CaptchaActionTypeDef",
    {
        "CustomRequestHandling": CustomRequestHandlingTypeDef,
    },
    total=False,
)

ChallengeActionTypeDef = TypedDict(
    "ChallengeActionTypeDef",
    {
        "CustomRequestHandling": CustomRequestHandlingTypeDef,
    },
    total=False,
)

CountActionTypeDef = TypedDict(
    "CountActionTypeDef",
    {
        "CustomRequestHandling": CustomRequestHandlingTypeDef,
    },
    total=False,
)

BlockActionTypeDef = TypedDict(
    "BlockActionTypeDef",
    {
        "CustomResponse": CustomResponseTypeDef,
    },
    total=False,
)

_RequiredSampledHTTPRequestTypeDef = TypedDict(
    "_RequiredSampledHTTPRequestTypeDef",
    {
        "Request": HTTPRequestTypeDef,
        "Weight": int,
    },
)
_OptionalSampledHTTPRequestTypeDef = TypedDict(
    "_OptionalSampledHTTPRequestTypeDef",
    {
        "Timestamp": datetime,
        "Action": str,
        "RuleNameWithinRuleGroup": str,
        "RequestHeadersInserted": List[HTTPHeaderTypeDef],
        "ResponseCodeSent": int,
        "Labels": List[LabelOutputTypeDef],
        "CaptchaResponse": CaptchaResponseTypeDef,
        "ChallengeResponse": ChallengeResponseTypeDef,
        "OverriddenAction": str,
    },
    total=False,
)


class SampledHTTPRequestTypeDef(
    _RequiredSampledHTTPRequestTypeDef, _OptionalSampledHTTPRequestTypeDef
):
    pass


FieldToMatchOutputTypeDef = TypedDict(
    "FieldToMatchOutputTypeDef",
    {
        "SingleHeader": SingleHeaderOutputTypeDef,
        "SingleQueryArgument": SingleQueryArgumentOutputTypeDef,
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": BodyOutputTypeDef,
        "Method": Dict[str, Any],
        "JsonBody": JsonBodyOutputTypeDef,
        "Headers": HeadersOutputTypeDef,
        "Cookies": CookiesOutputTypeDef,
        "HeaderOrder": HeaderOrderOutputTypeDef,
    },
    total=False,
)

FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "SingleHeader": SingleHeaderTypeDef,
        "SingleQueryArgument": SingleQueryArgumentTypeDef,
        "AllQueryArguments": Mapping[str, Any],
        "UriPath": Mapping[str, Any],
        "QueryString": Mapping[str, Any],
        "Body": BodyTypeDef,
        "Method": Mapping[str, Any],
        "JsonBody": JsonBodyTypeDef,
        "Headers": HeadersTypeDef,
        "Cookies": CookiesTypeDef,
        "HeaderOrder": HeaderOrderTypeDef,
    },
    total=False,
)

GetManagedRuleSetResponseTypeDef = TypedDict(
    "GetManagedRuleSetResponseTypeDef",
    {
        "ManagedRuleSet": ManagedRuleSetTypeDef,
        "LockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMobileSdkReleaseResponseTypeDef = TypedDict(
    "GetMobileSdkReleaseResponseTypeDef",
    {
        "MobileSdkRelease": MobileSdkReleaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextMarker": str,
        "TagInfoForResource": TagInfoForResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": RegexPatternSetTypeDef,
        "LockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredAWSManagedRulesACFPRuleSetOutputTypeDef = TypedDict(
    "_RequiredAWSManagedRulesACFPRuleSetOutputTypeDef",
    {
        "CreationPath": str,
        "RegistrationPagePath": str,
        "RequestInspection": RequestInspectionACFPOutputTypeDef,
    },
)
_OptionalAWSManagedRulesACFPRuleSetOutputTypeDef = TypedDict(
    "_OptionalAWSManagedRulesACFPRuleSetOutputTypeDef",
    {
        "ResponseInspection": ResponseInspectionOutputTypeDef,
        "EnableRegexInPath": bool,
    },
    total=False,
)


class AWSManagedRulesACFPRuleSetOutputTypeDef(
    _RequiredAWSManagedRulesACFPRuleSetOutputTypeDef,
    _OptionalAWSManagedRulesACFPRuleSetOutputTypeDef,
):
    pass


_RequiredAWSManagedRulesATPRuleSetOutputTypeDef = TypedDict(
    "_RequiredAWSManagedRulesATPRuleSetOutputTypeDef",
    {
        "LoginPath": str,
    },
)
_OptionalAWSManagedRulesATPRuleSetOutputTypeDef = TypedDict(
    "_OptionalAWSManagedRulesATPRuleSetOutputTypeDef",
    {
        "RequestInspection": RequestInspectionOutputTypeDef,
        "ResponseInspection": ResponseInspectionOutputTypeDef,
        "EnableRegexInPath": bool,
    },
    total=False,
)


class AWSManagedRulesATPRuleSetOutputTypeDef(
    _RequiredAWSManagedRulesATPRuleSetOutputTypeDef, _OptionalAWSManagedRulesATPRuleSetOutputTypeDef
):
    pass


_RequiredAWSManagedRulesACFPRuleSetTypeDef = TypedDict(
    "_RequiredAWSManagedRulesACFPRuleSetTypeDef",
    {
        "CreationPath": str,
        "RegistrationPagePath": str,
        "RequestInspection": RequestInspectionACFPTypeDef,
    },
)
_OptionalAWSManagedRulesACFPRuleSetTypeDef = TypedDict(
    "_OptionalAWSManagedRulesACFPRuleSetTypeDef",
    {
        "ResponseInspection": ResponseInspectionTypeDef,
        "EnableRegexInPath": bool,
    },
    total=False,
)


class AWSManagedRulesACFPRuleSetTypeDef(
    _RequiredAWSManagedRulesACFPRuleSetTypeDef, _OptionalAWSManagedRulesACFPRuleSetTypeDef
):
    pass


_RequiredAWSManagedRulesATPRuleSetTypeDef = TypedDict(
    "_RequiredAWSManagedRulesATPRuleSetTypeDef",
    {
        "LoginPath": str,
    },
)
_OptionalAWSManagedRulesATPRuleSetTypeDef = TypedDict(
    "_OptionalAWSManagedRulesATPRuleSetTypeDef",
    {
        "RequestInspection": RequestInspectionTypeDef,
        "ResponseInspection": ResponseInspectionTypeDef,
        "EnableRegexInPath": bool,
    },
    total=False,
)


class AWSManagedRulesATPRuleSetTypeDef(
    _RequiredAWSManagedRulesATPRuleSetTypeDef, _OptionalAWSManagedRulesATPRuleSetTypeDef
):
    pass


_RequiredRateBasedStatementOutputTypeDef = TypedDict(
    "_RequiredRateBasedStatementOutputTypeDef",
    {
        "Limit": int,
        "AggregateKeyType": RateBasedStatementAggregateKeyTypeType,
    },
)
_OptionalRateBasedStatementOutputTypeDef = TypedDict(
    "_OptionalRateBasedStatementOutputTypeDef",
    {
        "ScopeDownStatement": "StatementOutputTypeDef",
        "ForwardedIPConfig": ForwardedIPConfigOutputTypeDef,
        "CustomKeys": List[RateBasedStatementCustomKeyOutputTypeDef],
    },
    total=False,
)


class RateBasedStatementOutputTypeDef(
    _RequiredRateBasedStatementOutputTypeDef, _OptionalRateBasedStatementOutputTypeDef
):
    pass


_RequiredRateBasedStatementTypeDef = TypedDict(
    "_RequiredRateBasedStatementTypeDef",
    {
        "Limit": int,
        "AggregateKeyType": RateBasedStatementAggregateKeyTypeType,
    },
)
_OptionalRateBasedStatementTypeDef = TypedDict(
    "_OptionalRateBasedStatementTypeDef",
    {
        "ScopeDownStatement": "StatementTypeDef",
        "ForwardedIPConfig": ForwardedIPConfigTypeDef,
        "CustomKeys": Sequence[RateBasedStatementCustomKeyTypeDef],
    },
    total=False,
)


class RateBasedStatementTypeDef(
    _RequiredRateBasedStatementTypeDef, _OptionalRateBasedStatementTypeDef
):
    pass


LoggingFilterOutputTypeDef = TypedDict(
    "LoggingFilterOutputTypeDef",
    {
        "Filters": List[FilterOutputTypeDef],
        "DefaultBehavior": FilterBehaviorType,
    },
)

LoggingFilterTypeDef = TypedDict(
    "LoggingFilterTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "DefaultBehavior": FilterBehaviorType,
    },
)

OverrideActionOutputTypeDef = TypedDict(
    "OverrideActionOutputTypeDef",
    {
        "Count": CountActionOutputTypeDef,
        "None": Dict[str, Any],
    },
    total=False,
)

DefaultActionOutputTypeDef = TypedDict(
    "DefaultActionOutputTypeDef",
    {
        "Block": BlockActionOutputTypeDef,
        "Allow": AllowActionOutputTypeDef,
    },
    total=False,
)

RuleActionOutputTypeDef = TypedDict(
    "RuleActionOutputTypeDef",
    {
        "Block": BlockActionOutputTypeDef,
        "Allow": AllowActionOutputTypeDef,
        "Count": CountActionOutputTypeDef,
        "Captcha": CaptchaActionOutputTypeDef,
        "Challenge": ChallengeActionOutputTypeDef,
    },
    total=False,
)

OverrideActionTypeDef = TypedDict(
    "OverrideActionTypeDef",
    {
        "Count": CountActionTypeDef,
        "None": Mapping[str, Any],
    },
    total=False,
)

DefaultActionTypeDef = TypedDict(
    "DefaultActionTypeDef",
    {
        "Block": BlockActionTypeDef,
        "Allow": AllowActionTypeDef,
    },
    total=False,
)

RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "Block": BlockActionTypeDef,
        "Allow": AllowActionTypeDef,
        "Count": CountActionTypeDef,
        "Captcha": CaptchaActionTypeDef,
        "Challenge": ChallengeActionTypeDef,
    },
    total=False,
)

GetSampledRequestsResponseTypeDef = TypedDict(
    "GetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List[SampledHTTPRequestTypeDef],
        "PopulationSize": int,
        "TimeWindow": TimeWindowOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ByteMatchStatementOutputTypeDef = TypedDict(
    "ByteMatchStatementOutputTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationOutputTypeDef],
        "PositionalConstraint": PositionalConstraintType,
    },
)

RegexMatchStatementOutputTypeDef = TypedDict(
    "RegexMatchStatementOutputTypeDef",
    {
        "RegexString": str,
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

RegexPatternSetReferenceStatementOutputTypeDef = TypedDict(
    "RegexPatternSetReferenceStatementOutputTypeDef",
    {
        "ARN": str,
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

SizeConstraintStatementOutputTypeDef = TypedDict(
    "SizeConstraintStatementOutputTypeDef",
    {
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

_RequiredSqliMatchStatementOutputTypeDef = TypedDict(
    "_RequiredSqliMatchStatementOutputTypeDef",
    {
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)
_OptionalSqliMatchStatementOutputTypeDef = TypedDict(
    "_OptionalSqliMatchStatementOutputTypeDef",
    {
        "SensitivityLevel": SensitivityLevelType,
    },
    total=False,
)


class SqliMatchStatementOutputTypeDef(
    _RequiredSqliMatchStatementOutputTypeDef, _OptionalSqliMatchStatementOutputTypeDef
):
    pass


XssMatchStatementOutputTypeDef = TypedDict(
    "XssMatchStatementOutputTypeDef",
    {
        "FieldToMatch": FieldToMatchOutputTypeDef,
        "TextTransformations": List[TextTransformationOutputTypeDef],
    },
)

ByteMatchStatementTypeDef = TypedDict(
    "ByteMatchStatementTypeDef",
    {
        "SearchString": Union[str, bytes, IO[Any], StreamingBody],
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
        "PositionalConstraint": PositionalConstraintType,
    },
)

RegexMatchStatementTypeDef = TypedDict(
    "RegexMatchStatementTypeDef",
    {
        "RegexString": str,
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

RegexPatternSetReferenceStatementTypeDef = TypedDict(
    "RegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

SizeConstraintStatementTypeDef = TypedDict(
    "SizeConstraintStatementTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

_RequiredSqliMatchStatementTypeDef = TypedDict(
    "_RequiredSqliMatchStatementTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)
_OptionalSqliMatchStatementTypeDef = TypedDict(
    "_OptionalSqliMatchStatementTypeDef",
    {
        "SensitivityLevel": SensitivityLevelType,
    },
    total=False,
)


class SqliMatchStatementTypeDef(
    _RequiredSqliMatchStatementTypeDef, _OptionalSqliMatchStatementTypeDef
):
    pass


XssMatchStatementTypeDef = TypedDict(
    "XssMatchStatementTypeDef",
    {
        "FieldToMatch": FieldToMatchTypeDef,
        "TextTransformations": Sequence[TextTransformationTypeDef],
    },
)

ManagedRuleGroupConfigOutputTypeDef = TypedDict(
    "ManagedRuleGroupConfigOutputTypeDef",
    {
        "LoginPath": str,
        "PayloadType": PayloadTypeType,
        "UsernameField": UsernameFieldOutputTypeDef,
        "PasswordField": PasswordFieldOutputTypeDef,
        "AWSManagedRulesBotControlRuleSet": AWSManagedRulesBotControlRuleSetOutputTypeDef,
        "AWSManagedRulesATPRuleSet": AWSManagedRulesATPRuleSetOutputTypeDef,
        "AWSManagedRulesACFPRuleSet": AWSManagedRulesACFPRuleSetOutputTypeDef,
    },
    total=False,
)

ManagedRuleGroupConfigTypeDef = TypedDict(
    "ManagedRuleGroupConfigTypeDef",
    {
        "LoginPath": str,
        "PayloadType": PayloadTypeType,
        "UsernameField": UsernameFieldTypeDef,
        "PasswordField": PasswordFieldTypeDef,
        "AWSManagedRulesBotControlRuleSet": AWSManagedRulesBotControlRuleSetTypeDef,
        "AWSManagedRulesATPRuleSet": AWSManagedRulesATPRuleSetTypeDef,
        "AWSManagedRulesACFPRuleSet": AWSManagedRulesACFPRuleSetTypeDef,
    },
    total=False,
)

_RequiredLoggingConfigurationOutputTypeDef = TypedDict(
    "_RequiredLoggingConfigurationOutputTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
    },
)
_OptionalLoggingConfigurationOutputTypeDef = TypedDict(
    "_OptionalLoggingConfigurationOutputTypeDef",
    {
        "RedactedFields": List[FieldToMatchOutputTypeDef],
        "ManagedByFirewallManager": bool,
        "LoggingFilter": LoggingFilterOutputTypeDef,
    },
    total=False,
)


class LoggingConfigurationOutputTypeDef(
    _RequiredLoggingConfigurationOutputTypeDef, _OptionalLoggingConfigurationOutputTypeDef
):
    pass


_RequiredLoggingConfigurationTypeDef = TypedDict(
    "_RequiredLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": Sequence[str],
    },
)
_OptionalLoggingConfigurationTypeDef = TypedDict(
    "_OptionalLoggingConfigurationTypeDef",
    {
        "RedactedFields": Sequence[FieldToMatchTypeDef],
        "ManagedByFirewallManager": bool,
        "LoggingFilter": LoggingFilterTypeDef,
    },
    total=False,
)


class LoggingConfigurationTypeDef(
    _RequiredLoggingConfigurationTypeDef, _OptionalLoggingConfigurationTypeDef
):
    pass


RuleActionOverrideOutputTypeDef = TypedDict(
    "RuleActionOverrideOutputTypeDef",
    {
        "Name": str,
        "ActionToUse": RuleActionOutputTypeDef,
    },
)

_RequiredRuleOutputTypeDef = TypedDict(
    "_RequiredRuleOutputTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": "StatementOutputTypeDef",
        "VisibilityConfig": VisibilityConfigOutputTypeDef,
    },
)
_OptionalRuleOutputTypeDef = TypedDict(
    "_OptionalRuleOutputTypeDef",
    {
        "Action": RuleActionOutputTypeDef,
        "OverrideAction": OverrideActionOutputTypeDef,
        "RuleLabels": List[LabelOutputTypeDef],
        "CaptchaConfig": CaptchaConfigOutputTypeDef,
        "ChallengeConfig": ChallengeConfigOutputTypeDef,
    },
    total=False,
)


class RuleOutputTypeDef(_RequiredRuleOutputTypeDef, _OptionalRuleOutputTypeDef):
    pass


RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Name": str,
        "Action": RuleActionOutputTypeDef,
    },
    total=False,
)

RuleActionOverrideTypeDef = TypedDict(
    "RuleActionOverrideTypeDef",
    {
        "Name": str,
        "ActionToUse": RuleActionTypeDef,
    },
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": "StatementTypeDef",
        "VisibilityConfig": VisibilityConfigTypeDef,
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Action": RuleActionTypeDef,
        "OverrideAction": OverrideActionTypeDef,
        "RuleLabels": Sequence[LabelTypeDef],
        "CaptchaConfig": CaptchaConfigTypeDef,
        "ChallengeConfig": ChallengeConfigTypeDef,
    },
    total=False,
)


class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass


GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List[LoggingConfigurationOutputTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutLoggingConfigurationResponseTypeDef = TypedDict(
    "PutLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutLoggingConfigurationRequestRequestTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationTypeDef,
    },
)

_RequiredManagedRuleGroupStatementOutputTypeDef = TypedDict(
    "_RequiredManagedRuleGroupStatementOutputTypeDef",
    {
        "VendorName": str,
        "Name": str,
    },
)
_OptionalManagedRuleGroupStatementOutputTypeDef = TypedDict(
    "_OptionalManagedRuleGroupStatementOutputTypeDef",
    {
        "Version": str,
        "ExcludedRules": List[ExcludedRuleOutputTypeDef],
        "ScopeDownStatement": Dict[str, Any],
        "ManagedRuleGroupConfigs": List[ManagedRuleGroupConfigOutputTypeDef],
        "RuleActionOverrides": List[RuleActionOverrideOutputTypeDef],
    },
    total=False,
)


class ManagedRuleGroupStatementOutputTypeDef(
    _RequiredManagedRuleGroupStatementOutputTypeDef, _OptionalManagedRuleGroupStatementOutputTypeDef
):
    pass


_RequiredRuleGroupReferenceStatementOutputTypeDef = TypedDict(
    "_RequiredRuleGroupReferenceStatementOutputTypeDef",
    {
        "ARN": str,
    },
)
_OptionalRuleGroupReferenceStatementOutputTypeDef = TypedDict(
    "_OptionalRuleGroupReferenceStatementOutputTypeDef",
    {
        "ExcludedRules": List[ExcludedRuleOutputTypeDef],
        "RuleActionOverrides": List[RuleActionOverrideOutputTypeDef],
    },
    total=False,
)


class RuleGroupReferenceStatementOutputTypeDef(
    _RequiredRuleGroupReferenceStatementOutputTypeDef,
    _OptionalRuleGroupReferenceStatementOutputTypeDef,
):
    pass


_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef",
    {
        "Name": str,
        "Id": str,
        "Capacity": int,
        "ARN": str,
        "VisibilityConfig": VisibilityConfigOutputTypeDef,
    },
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef",
    {
        "Description": str,
        "Rules": List[RuleOutputTypeDef],
        "LabelNamespace": str,
        "CustomResponseBodies": Dict[str, CustomResponseBodyOutputTypeDef],
        "AvailableLabels": List[LabelSummaryTypeDef],
        "ConsumedLabels": List[LabelSummaryTypeDef],
    },
    total=False,
)


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass


DescribeManagedRuleGroupResponseTypeDef = TypedDict(
    "DescribeManagedRuleGroupResponseTypeDef",
    {
        "VersionName": str,
        "SnsTopicArn": str,
        "Capacity": int,
        "Rules": List[RuleSummaryTypeDef],
        "LabelNamespace": str,
        "AvailableLabels": List[LabelSummaryTypeDef],
        "ConsumedLabels": List[LabelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredManagedRuleGroupStatementTypeDef = TypedDict(
    "_RequiredManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
    },
)
_OptionalManagedRuleGroupStatementTypeDef = TypedDict(
    "_OptionalManagedRuleGroupStatementTypeDef",
    {
        "Version": str,
        "ExcludedRules": Sequence[ExcludedRuleTypeDef],
        "ScopeDownStatement": "StatementTypeDef",
        "ManagedRuleGroupConfigs": Sequence[ManagedRuleGroupConfigTypeDef],
        "RuleActionOverrides": Sequence[RuleActionOverrideTypeDef],
    },
    total=False,
)


class ManagedRuleGroupStatementTypeDef(
    _RequiredManagedRuleGroupStatementTypeDef, _OptionalManagedRuleGroupStatementTypeDef
):
    pass


_RequiredRuleGroupReferenceStatementTypeDef = TypedDict(
    "_RequiredRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
    },
)
_OptionalRuleGroupReferenceStatementTypeDef = TypedDict(
    "_OptionalRuleGroupReferenceStatementTypeDef",
    {
        "ExcludedRules": Sequence[ExcludedRuleTypeDef],
        "RuleActionOverrides": Sequence[RuleActionOverrideTypeDef],
    },
    total=False,
)


class RuleGroupReferenceStatementTypeDef(
    _RequiredRuleGroupReferenceStatementTypeDef, _OptionalRuleGroupReferenceStatementTypeDef
):
    pass


CheckCapacityRequestRequestTypeDef = TypedDict(
    "CheckCapacityRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "Rules": Sequence[RuleTypeDef],
    },
)

_RequiredCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Capacity": int,
        "VisibilityConfig": VisibilityConfigTypeDef,
    },
)
_OptionalCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleGroupRequestRequestTypeDef",
    {
        "Description": str,
        "Rules": Sequence[RuleTypeDef],
        "Tags": Sequence[TagTypeDef],
        "CustomResponseBodies": Mapping[str, CustomResponseBodyTypeDef],
    },
    total=False,
)


class CreateRuleGroupRequestRequestTypeDef(
    _RequiredCreateRuleGroupRequestRequestTypeDef, _OptionalCreateRuleGroupRequestRequestTypeDef
):
    pass


_RequiredCreateWebACLRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "DefaultAction": DefaultActionTypeDef,
        "VisibilityConfig": VisibilityConfigTypeDef,
    },
)
_OptionalCreateWebACLRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWebACLRequestRequestTypeDef",
    {
        "Description": str,
        "Rules": Sequence[RuleTypeDef],
        "Tags": Sequence[TagTypeDef],
        "CustomResponseBodies": Mapping[str, CustomResponseBodyTypeDef],
        "CaptchaConfig": CaptchaConfigTypeDef,
        "ChallengeConfig": ChallengeConfigTypeDef,
        "TokenDomains": Sequence[str],
        "AssociationConfig": AssociationConfigTypeDef,
    },
    total=False,
)


class CreateWebACLRequestRequestTypeDef(
    _RequiredCreateWebACLRequestRequestTypeDef, _OptionalCreateWebACLRequestRequestTypeDef
):
    pass


_RequiredUpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "LockToken": str,
    },
)
_OptionalUpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleGroupRequestRequestTypeDef",
    {
        "Description": str,
        "Rules": Sequence[RuleTypeDef],
        "CustomResponseBodies": Mapping[str, CustomResponseBodyTypeDef],
    },
    total=False,
)


class UpdateRuleGroupRequestRequestTypeDef(
    _RequiredUpdateRuleGroupRequestRequestTypeDef, _OptionalUpdateRuleGroupRequestRequestTypeDef
):
    pass


_RequiredUpdateWebACLRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "DefaultAction": DefaultActionTypeDef,
        "VisibilityConfig": VisibilityConfigTypeDef,
        "LockToken": str,
    },
)
_OptionalUpdateWebACLRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWebACLRequestRequestTypeDef",
    {
        "Description": str,
        "Rules": Sequence[RuleTypeDef],
        "CustomResponseBodies": Mapping[str, CustomResponseBodyTypeDef],
        "CaptchaConfig": CaptchaConfigTypeDef,
        "ChallengeConfig": ChallengeConfigTypeDef,
        "TokenDomains": Sequence[str],
        "AssociationConfig": AssociationConfigTypeDef,
    },
    total=False,
)


class UpdateWebACLRequestRequestTypeDef(
    _RequiredUpdateWebACLRequestRequestTypeDef, _OptionalUpdateWebACLRequestRequestTypeDef
):
    pass


FirewallManagerStatementTypeDef = TypedDict(
    "FirewallManagerStatementTypeDef",
    {
        "ManagedRuleGroupStatement": ManagedRuleGroupStatementOutputTypeDef,
        "RuleGroupReferenceStatement": RuleGroupReferenceStatementOutputTypeDef,
    },
    total=False,
)

StatementOutputTypeDef = TypedDict(
    "StatementOutputTypeDef",
    {
        "ByteMatchStatement": ByteMatchStatementOutputTypeDef,
        "SqliMatchStatement": SqliMatchStatementOutputTypeDef,
        "XssMatchStatement": XssMatchStatementOutputTypeDef,
        "SizeConstraintStatement": SizeConstraintStatementOutputTypeDef,
        "GeoMatchStatement": GeoMatchStatementOutputTypeDef,
        "RuleGroupReferenceStatement": RuleGroupReferenceStatementOutputTypeDef,
        "IPSetReferenceStatement": IPSetReferenceStatementOutputTypeDef,
        "RegexPatternSetReferenceStatement": RegexPatternSetReferenceStatementOutputTypeDef,
        "RateBasedStatement": Dict[str, Any],
        "AndStatement": Dict[str, Any],
        "OrStatement": Dict[str, Any],
        "NotStatement": Dict[str, Any],
        "ManagedRuleGroupStatement": Dict[str, Any],
        "LabelMatchStatement": LabelMatchStatementOutputTypeDef,
        "RegexMatchStatement": RegexMatchStatementOutputTypeDef,
    },
    total=False,
)

GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": RuleGroupTypeDef,
        "LockToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "ByteMatchStatement": ByteMatchStatementTypeDef,
        "SqliMatchStatement": SqliMatchStatementTypeDef,
        "XssMatchStatement": XssMatchStatementTypeDef,
        "SizeConstraintStatement": SizeConstraintStatementTypeDef,
        "GeoMatchStatement": GeoMatchStatementTypeDef,
        "RuleGroupReferenceStatement": RuleGroupReferenceStatementTypeDef,
        "IPSetReferenceStatement": IPSetReferenceStatementTypeDef,
        "RegexPatternSetReferenceStatement": RegexPatternSetReferenceStatementTypeDef,
        "RateBasedStatement": Dict[str, Any],
        "AndStatement": Dict[str, Any],
        "OrStatement": Dict[str, Any],
        "NotStatement": Dict[str, Any],
        "ManagedRuleGroupStatement": Dict[str, Any],
        "LabelMatchStatement": LabelMatchStatementTypeDef,
        "RegexMatchStatement": RegexMatchStatementTypeDef,
    },
    total=False,
)

FirewallManagerRuleGroupTypeDef = TypedDict(
    "FirewallManagerRuleGroupTypeDef",
    {
        "Name": str,
        "Priority": int,
        "FirewallManagerStatement": FirewallManagerStatementTypeDef,
        "OverrideAction": OverrideActionOutputTypeDef,
        "VisibilityConfig": VisibilityConfigOutputTypeDef,
    },
)

_RequiredWebACLTypeDef = TypedDict(
    "_RequiredWebACLTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "DefaultAction": DefaultActionOutputTypeDef,
        "VisibilityConfig": VisibilityConfigOutputTypeDef,
    },
)
_OptionalWebACLTypeDef = TypedDict(
    "_OptionalWebACLTypeDef",
    {
        "Description": str,
        "Rules": List[RuleOutputTypeDef],
        "Capacity": int,
        "PreProcessFirewallManagerRuleGroups": List[FirewallManagerRuleGroupTypeDef],
        "PostProcessFirewallManagerRuleGroups": List[FirewallManagerRuleGroupTypeDef],
        "ManagedByFirewallManager": bool,
        "LabelNamespace": str,
        "CustomResponseBodies": Dict[str, CustomResponseBodyOutputTypeDef],
        "CaptchaConfig": CaptchaConfigOutputTypeDef,
        "ChallengeConfig": ChallengeConfigOutputTypeDef,
        "TokenDomains": List[str],
        "AssociationConfig": AssociationConfigOutputTypeDef,
    },
    total=False,
)


class WebACLTypeDef(_RequiredWebACLTypeDef, _OptionalWebACLTypeDef):
    pass


GetWebACLForResourceResponseTypeDef = TypedDict(
    "GetWebACLForResourceResponseTypeDef",
    {
        "WebACL": WebACLTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": WebACLTypeDef,
        "LockToken": str,
        "ApplicationIntegrationURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
