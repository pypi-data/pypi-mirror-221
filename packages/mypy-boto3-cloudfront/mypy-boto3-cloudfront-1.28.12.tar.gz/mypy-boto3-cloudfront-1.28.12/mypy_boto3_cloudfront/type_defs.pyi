"""
Type annotations for cloudfront service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudfront.type_defs import AliasICPRecordalTypeDef

    data: AliasICPRecordalTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    CachePolicyCookieBehaviorType,
    CachePolicyHeaderBehaviorType,
    CachePolicyQueryStringBehaviorType,
    CachePolicyTypeType,
    CertificateSourceType,
    ContinuousDeploymentPolicyTypeType,
    EventTypeType,
    FrameOptionsListType,
    FunctionStageType,
    GeoRestrictionTypeType,
    HttpVersionType,
    ICPRecordalStatusType,
    ItemSelectionType,
    MethodType,
    MinimumProtocolVersionType,
    OriginAccessControlOriginTypesType,
    OriginAccessControlSigningBehaviorsType,
    OriginProtocolPolicyType,
    OriginRequestPolicyCookieBehaviorType,
    OriginRequestPolicyHeaderBehaviorType,
    OriginRequestPolicyQueryStringBehaviorType,
    OriginRequestPolicyTypeType,
    PriceClassType,
    RealtimeMetricsSubscriptionStatusType,
    ReferrerPolicyListType,
    ResponseHeadersPolicyAccessControlAllowMethodsValuesType,
    ResponseHeadersPolicyTypeType,
    SslProtocolType,
    SSLSupportMethodType,
    ViewerProtocolPolicyType,
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
    "AliasICPRecordalTypeDef",
    "AliasesOutputTypeDef",
    "AliasesTypeDef",
    "CachedMethodsOutputTypeDef",
    "CachedMethodsTypeDef",
    "AssociateAliasRequestRequestTypeDef",
    "TrustedKeyGroupsOutputTypeDef",
    "TrustedSignersOutputTypeDef",
    "TrustedKeyGroupsTypeDef",
    "TrustedSignersTypeDef",
    "CookieNamesOutputTypeDef",
    "CookieNamesTypeDef",
    "HeadersOutputTypeDef",
    "HeadersTypeDef",
    "QueryStringNamesOutputTypeDef",
    "QueryStringNamesTypeDef",
    "CloudFrontOriginAccessIdentityConfigOutputTypeDef",
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    "ConflictingAliasTypeDef",
    "ContentTypeProfileOutputTypeDef",
    "ContentTypeProfileTypeDef",
    "StagingDistributionDnsNamesOutputTypeDef",
    "StagingDistributionDnsNamesTypeDef",
    "ContinuousDeploymentSingleHeaderConfigOutputTypeDef",
    "ContinuousDeploymentSingleHeaderConfigTypeDef",
    "SessionStickinessConfigOutputTypeDef",
    "SessionStickinessConfigTypeDef",
    "CopyDistributionRequestRequestTypeDef",
    "FunctionConfigTypeDef",
    "KeyGroupConfigTypeDef",
    "OriginAccessControlConfigTypeDef",
    "PublicKeyConfigTypeDef",
    "CustomErrorResponseOutputTypeDef",
    "CustomErrorResponseTypeDef",
    "OriginCustomHeaderOutputTypeDef",
    "OriginCustomHeaderTypeDef",
    "OriginSslProtocolsOutputTypeDef",
    "OriginSslProtocolsTypeDef",
    "DeleteCachePolicyRequestRequestTypeDef",
    "DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "DeleteContinuousDeploymentPolicyRequestRequestTypeDef",
    "DeleteDistributionRequestRequestTypeDef",
    "DeleteFieldLevelEncryptionConfigRequestRequestTypeDef",
    "DeleteFieldLevelEncryptionProfileRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteKeyGroupRequestRequestTypeDef",
    "DeleteMonitoringSubscriptionRequestRequestTypeDef",
    "DeleteOriginAccessControlRequestRequestTypeDef",
    "DeleteOriginRequestPolicyRequestRequestTypeDef",
    "DeletePublicKeyRequestRequestTypeDef",
    "DeleteRealtimeLogConfigRequestRequestTypeDef",
    "DeleteResponseHeadersPolicyRequestRequestTypeDef",
    "DeleteStreamingDistributionRequestRequestTypeDef",
    "DescribeFunctionRequestRequestTypeDef",
    "LoggingConfigOutputTypeDef",
    "ViewerCertificateOutputTypeDef",
    "LoggingConfigTypeDef",
    "ViewerCertificateTypeDef",
    "DistributionIdListTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FieldPatternsOutputTypeDef",
    "FieldPatternsTypeDef",
    "KinesisStreamConfigOutputTypeDef",
    "KinesisStreamConfigTypeDef",
    "QueryStringCacheKeysOutputTypeDef",
    "QueryStringCacheKeysTypeDef",
    "FunctionAssociationOutputTypeDef",
    "FunctionAssociationTypeDef",
    "FunctionConfigOutputTypeDef",
    "FunctionMetadataTypeDef",
    "GeoRestrictionOutputTypeDef",
    "GeoRestrictionTypeDef",
    "GetCachePolicyConfigRequestRequestTypeDef",
    "GetCachePolicyRequestRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "GetContinuousDeploymentPolicyConfigRequestRequestTypeDef",
    "GetContinuousDeploymentPolicyRequestRequestTypeDef",
    "GetDistributionConfigRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetDistributionRequestRequestTypeDef",
    "GetFieldLevelEncryptionConfigRequestRequestTypeDef",
    "GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef",
    "GetFieldLevelEncryptionProfileRequestRequestTypeDef",
    "GetFieldLevelEncryptionRequestRequestTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetFunctionResultTypeDef",
    "GetInvalidationRequestRequestTypeDef",
    "GetKeyGroupConfigRequestRequestTypeDef",
    "KeyGroupConfigOutputTypeDef",
    "GetKeyGroupRequestRequestTypeDef",
    "GetMonitoringSubscriptionRequestRequestTypeDef",
    "GetOriginAccessControlConfigRequestRequestTypeDef",
    "OriginAccessControlConfigOutputTypeDef",
    "GetOriginAccessControlRequestRequestTypeDef",
    "GetOriginRequestPolicyConfigRequestRequestTypeDef",
    "GetOriginRequestPolicyRequestRequestTypeDef",
    "GetPublicKeyConfigRequestRequestTypeDef",
    "PublicKeyConfigOutputTypeDef",
    "GetPublicKeyRequestRequestTypeDef",
    "GetRealtimeLogConfigRequestRequestTypeDef",
    "GetResponseHeadersPolicyConfigRequestRequestTypeDef",
    "GetResponseHeadersPolicyRequestRequestTypeDef",
    "GetStreamingDistributionConfigRequestRequestTypeDef",
    "GetStreamingDistributionRequestRequestTypeDef",
    "PathsOutputTypeDef",
    "PathsTypeDef",
    "InvalidationSummaryTypeDef",
    "KeyPairIdsTypeDef",
    "LambdaFunctionAssociationOutputTypeDef",
    "LambdaFunctionAssociationTypeDef",
    "ListCachePoliciesRequestRequestTypeDef",
    "ListCloudFrontOriginAccessIdentitiesRequestListCloudFrontOriginAccessIdentitiesPaginateTypeDef",
    "ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef",
    "ListConflictingAliasesRequestRequestTypeDef",
    "ListContinuousDeploymentPoliciesRequestRequestTypeDef",
    "ListDistributionsByCachePolicyIdRequestRequestTypeDef",
    "ListDistributionsByKeyGroupRequestRequestTypeDef",
    "ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef",
    "ListDistributionsByRealtimeLogConfigRequestRequestTypeDef",
    "ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef",
    "ListDistributionsByWebACLIdRequestRequestTypeDef",
    "ListDistributionsRequestListDistributionsPaginateTypeDef",
    "ListDistributionsRequestRequestTypeDef",
    "ListFieldLevelEncryptionConfigsRequestRequestTypeDef",
    "ListFieldLevelEncryptionProfilesRequestRequestTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListInvalidationsRequestListInvalidationsPaginateTypeDef",
    "ListInvalidationsRequestRequestTypeDef",
    "ListKeyGroupsRequestRequestTypeDef",
    "ListOriginAccessControlsRequestRequestTypeDef",
    "ListOriginRequestPoliciesRequestRequestTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "ListRealtimeLogConfigsRequestRequestTypeDef",
    "ListResponseHeadersPoliciesRequestRequestTypeDef",
    "ListStreamingDistributionsRequestListStreamingDistributionsPaginateTypeDef",
    "ListStreamingDistributionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RealtimeMetricsSubscriptionConfigOutputTypeDef",
    "RealtimeMetricsSubscriptionConfigTypeDef",
    "OriginAccessControlSummaryTypeDef",
    "StatusCodesOutputTypeDef",
    "StatusCodesTypeDef",
    "OriginGroupMemberOutputTypeDef",
    "OriginGroupMemberTypeDef",
    "OriginShieldOutputTypeDef",
    "S3OriginConfigOutputTypeDef",
    "OriginShieldTypeDef",
    "S3OriginConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PublicKeySummaryTypeDef",
    "PublishFunctionRequestRequestTypeDef",
    "QueryArgProfileOutputTypeDef",
    "QueryArgProfileTypeDef",
    "ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef",
    "ResponseHeadersPolicyAccessControlAllowHeadersTypeDef",
    "ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef",
    "ResponseHeadersPolicyAccessControlAllowMethodsTypeDef",
    "ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef",
    "ResponseHeadersPolicyAccessControlAllowOriginsTypeDef",
    "ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef",
    "ResponseHeadersPolicyAccessControlExposeHeadersTypeDef",
    "ResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef",
    "ResponseHeadersPolicyServerTimingHeadersConfigTypeDef",
    "ResponseHeadersPolicyContentSecurityPolicyOutputTypeDef",
    "ResponseHeadersPolicyContentSecurityPolicyTypeDef",
    "ResponseHeadersPolicyContentTypeOptionsOutputTypeDef",
    "ResponseHeadersPolicyContentTypeOptionsTypeDef",
    "ResponseHeadersPolicyCustomHeaderOutputTypeDef",
    "ResponseHeadersPolicyCustomHeaderTypeDef",
    "ResponseHeadersPolicyFrameOptionsOutputTypeDef",
    "ResponseHeadersPolicyFrameOptionsTypeDef",
    "ResponseHeadersPolicyReferrerPolicyOutputTypeDef",
    "ResponseHeadersPolicyReferrerPolicyTypeDef",
    "ResponseHeadersPolicyRemoveHeaderOutputTypeDef",
    "ResponseHeadersPolicyRemoveHeaderTypeDef",
    "ResponseHeadersPolicyStrictTransportSecurityOutputTypeDef",
    "ResponseHeadersPolicyXSSProtectionOutputTypeDef",
    "ResponseHeadersPolicyStrictTransportSecurityTypeDef",
    "ResponseHeadersPolicyXSSProtectionTypeDef",
    "ResponseMetadataTypeDef",
    "S3OriginOutputTypeDef",
    "S3OriginTypeDef",
    "StreamingLoggingConfigOutputTypeDef",
    "StreamingLoggingConfigTypeDef",
    "TagKeysTypeDef",
    "TagOutputTypeDef",
    "TagTypeDef",
    "TestFunctionRequestRequestTypeDef",
    "UpdateDistributionWithStagingConfigRequestRequestTypeDef",
    "AllowedMethodsOutputTypeDef",
    "AllowedMethodsTypeDef",
    "CachePolicyCookiesConfigOutputTypeDef",
    "CookiePreferenceOutputTypeDef",
    "OriginRequestPolicyCookiesConfigOutputTypeDef",
    "CachePolicyCookiesConfigTypeDef",
    "CookiePreferenceTypeDef",
    "OriginRequestPolicyCookiesConfigTypeDef",
    "CachePolicyHeadersConfigOutputTypeDef",
    "OriginRequestPolicyHeadersConfigOutputTypeDef",
    "CachePolicyHeadersConfigTypeDef",
    "OriginRequestPolicyHeadersConfigTypeDef",
    "CachePolicyQueryStringsConfigOutputTypeDef",
    "OriginRequestPolicyQueryStringsConfigOutputTypeDef",
    "CachePolicyQueryStringsConfigTypeDef",
    "OriginRequestPolicyQueryStringsConfigTypeDef",
    "CloudFrontOriginAccessIdentityTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    "CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    "CloudFrontOriginAccessIdentityListTypeDef",
    "ConflictingAliasesListTypeDef",
    "ContentTypeProfilesOutputTypeDef",
    "ContentTypeProfilesTypeDef",
    "ContinuousDeploymentSingleWeightConfigOutputTypeDef",
    "ContinuousDeploymentSingleWeightConfigTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "UpdateFunctionRequestRequestTypeDef",
    "CreateKeyGroupRequestRequestTypeDef",
    "UpdateKeyGroupRequestRequestTypeDef",
    "CreateOriginAccessControlRequestRequestTypeDef",
    "UpdateOriginAccessControlRequestRequestTypeDef",
    "CreatePublicKeyRequestRequestTypeDef",
    "UpdatePublicKeyRequestRequestTypeDef",
    "CustomErrorResponsesOutputTypeDef",
    "CustomErrorResponsesTypeDef",
    "CustomHeadersOutputTypeDef",
    "CustomHeadersTypeDef",
    "CustomOriginConfigOutputTypeDef",
    "CustomOriginConfigTypeDef",
    "ListDistributionsByCachePolicyIdResultTypeDef",
    "ListDistributionsByKeyGroupResultTypeDef",
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    "ListDistributionsByResponseHeadersPolicyIdResultTypeDef",
    "EncryptionEntityOutputTypeDef",
    "EncryptionEntityTypeDef",
    "EndPointOutputTypeDef",
    "EndPointTypeDef",
    "FunctionAssociationsOutputTypeDef",
    "FunctionAssociationsTypeDef",
    "FunctionSummaryTypeDef",
    "RestrictionsOutputTypeDef",
    "RestrictionsTypeDef",
    "GetDistributionRequestDistributionDeployedWaitTypeDef",
    "GetInvalidationRequestInvalidationCompletedWaitTypeDef",
    "GetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef",
    "GetKeyGroupConfigResultTypeDef",
    "KeyGroupTypeDef",
    "GetOriginAccessControlConfigResultTypeDef",
    "OriginAccessControlTypeDef",
    "GetPublicKeyConfigResultTypeDef",
    "PublicKeyTypeDef",
    "InvalidationBatchOutputTypeDef",
    "InvalidationBatchTypeDef",
    "InvalidationListTypeDef",
    "KGKeyPairIdsTypeDef",
    "SignerTypeDef",
    "LambdaFunctionAssociationsOutputTypeDef",
    "LambdaFunctionAssociationsTypeDef",
    "MonitoringSubscriptionOutputTypeDef",
    "MonitoringSubscriptionTypeDef",
    "OriginAccessControlListTypeDef",
    "OriginGroupFailoverCriteriaOutputTypeDef",
    "OriginGroupFailoverCriteriaTypeDef",
    "OriginGroupMembersOutputTypeDef",
    "OriginGroupMembersTypeDef",
    "PublicKeyListTypeDef",
    "QueryArgProfilesOutputTypeDef",
    "QueryArgProfilesTypeDef",
    "ResponseHeadersPolicyCorsConfigOutputTypeDef",
    "ResponseHeadersPolicyCorsConfigTypeDef",
    "ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef",
    "ResponseHeadersPolicyCustomHeadersConfigTypeDef",
    "ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef",
    "ResponseHeadersPolicyRemoveHeadersConfigTypeDef",
    "ResponseHeadersPolicySecurityHeadersConfigOutputTypeDef",
    "ResponseHeadersPolicySecurityHeadersConfigTypeDef",
    "StreamingDistributionSummaryTypeDef",
    "StreamingDistributionConfigOutputTypeDef",
    "StreamingDistributionConfigTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "TagsOutputTypeDef",
    "TagsTypeDef",
    "ForwardedValuesOutputTypeDef",
    "ForwardedValuesTypeDef",
    "ParametersInCacheKeyAndForwardedToOriginOutputTypeDef",
    "OriginRequestPolicyConfigOutputTypeDef",
    "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    "OriginRequestPolicyConfigTypeDef",
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    "ListConflictingAliasesResultTypeDef",
    "ContentTypeProfileConfigOutputTypeDef",
    "ContentTypeProfileConfigTypeDef",
    "TrafficConfigOutputTypeDef",
    "TrafficConfigTypeDef",
    "OriginOutputTypeDef",
    "OriginTypeDef",
    "EncryptionEntitiesOutputTypeDef",
    "EncryptionEntitiesTypeDef",
    "RealtimeLogConfigTypeDef",
    "CreateRealtimeLogConfigRequestRequestTypeDef",
    "UpdateRealtimeLogConfigRequestRequestTypeDef",
    "CreateFunctionResultTypeDef",
    "DescribeFunctionResultTypeDef",
    "FunctionListTypeDef",
    "PublishFunctionResultTypeDef",
    "TestResultTypeDef",
    "UpdateFunctionResultTypeDef",
    "CreateKeyGroupResultTypeDef",
    "GetKeyGroupResultTypeDef",
    "KeyGroupSummaryTypeDef",
    "UpdateKeyGroupResultTypeDef",
    "CreateOriginAccessControlResultTypeDef",
    "GetOriginAccessControlResultTypeDef",
    "UpdateOriginAccessControlResultTypeDef",
    "CreatePublicKeyResultTypeDef",
    "GetPublicKeyResultTypeDef",
    "UpdatePublicKeyResultTypeDef",
    "InvalidationTypeDef",
    "CreateInvalidationRequestRequestTypeDef",
    "ListInvalidationsResultTypeDef",
    "ActiveTrustedKeyGroupsTypeDef",
    "ActiveTrustedSignersTypeDef",
    "CreateMonitoringSubscriptionResultTypeDef",
    "GetMonitoringSubscriptionResultTypeDef",
    "CreateMonitoringSubscriptionRequestRequestTypeDef",
    "ListOriginAccessControlsResultTypeDef",
    "OriginGroupOutputTypeDef",
    "OriginGroupTypeDef",
    "ListPublicKeysResultTypeDef",
    "QueryArgProfileConfigOutputTypeDef",
    "QueryArgProfileConfigTypeDef",
    "ResponseHeadersPolicyConfigOutputTypeDef",
    "ResponseHeadersPolicyConfigTypeDef",
    "StreamingDistributionListTypeDef",
    "GetStreamingDistributionConfigResultTypeDef",
    "CreateStreamingDistributionRequestRequestTypeDef",
    "UpdateStreamingDistributionRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "StreamingDistributionConfigWithTagsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CacheBehaviorOutputTypeDef",
    "DefaultCacheBehaviorOutputTypeDef",
    "CacheBehaviorTypeDef",
    "DefaultCacheBehaviorTypeDef",
    "CachePolicyConfigOutputTypeDef",
    "GetOriginRequestPolicyConfigResultTypeDef",
    "OriginRequestPolicyTypeDef",
    "CachePolicyConfigTypeDef",
    "CreateOriginRequestPolicyRequestRequestTypeDef",
    "UpdateOriginRequestPolicyRequestRequestTypeDef",
    "ContinuousDeploymentPolicyConfigOutputTypeDef",
    "ContinuousDeploymentPolicyConfigTypeDef",
    "OriginsOutputTypeDef",
    "OriginsTypeDef",
    "FieldLevelEncryptionProfileConfigOutputTypeDef",
    "FieldLevelEncryptionProfileSummaryTypeDef",
    "FieldLevelEncryptionProfileConfigTypeDef",
    "CreateRealtimeLogConfigResultTypeDef",
    "GetRealtimeLogConfigResultTypeDef",
    "RealtimeLogConfigsTypeDef",
    "UpdateRealtimeLogConfigResultTypeDef",
    "ListFunctionsResultTypeDef",
    "TestFunctionResultTypeDef",
    "KeyGroupListTypeDef",
    "CreateInvalidationResultTypeDef",
    "GetInvalidationResultTypeDef",
    "StreamingDistributionTypeDef",
    "OriginGroupsOutputTypeDef",
    "OriginGroupsTypeDef",
    "FieldLevelEncryptionConfigOutputTypeDef",
    "FieldLevelEncryptionSummaryTypeDef",
    "FieldLevelEncryptionConfigTypeDef",
    "GetResponseHeadersPolicyConfigResultTypeDef",
    "ResponseHeadersPolicyTypeDef",
    "CreateResponseHeadersPolicyRequestRequestTypeDef",
    "UpdateResponseHeadersPolicyRequestRequestTypeDef",
    "ListStreamingDistributionsResultTypeDef",
    "CreateStreamingDistributionWithTagsRequestRequestTypeDef",
    "CacheBehaviorsOutputTypeDef",
    "CacheBehaviorsTypeDef",
    "CachePolicyTypeDef",
    "GetCachePolicyConfigResultTypeDef",
    "CreateOriginRequestPolicyResultTypeDef",
    "GetOriginRequestPolicyResultTypeDef",
    "OriginRequestPolicySummaryTypeDef",
    "UpdateOriginRequestPolicyResultTypeDef",
    "CreateCachePolicyRequestRequestTypeDef",
    "UpdateCachePolicyRequestRequestTypeDef",
    "ContinuousDeploymentPolicyTypeDef",
    "GetContinuousDeploymentPolicyConfigResultTypeDef",
    "CreateContinuousDeploymentPolicyRequestRequestTypeDef",
    "UpdateContinuousDeploymentPolicyRequestRequestTypeDef",
    "FieldLevelEncryptionProfileTypeDef",
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    "FieldLevelEncryptionProfileListTypeDef",
    "CreateFieldLevelEncryptionProfileRequestRequestTypeDef",
    "UpdateFieldLevelEncryptionProfileRequestRequestTypeDef",
    "ListRealtimeLogConfigsResultTypeDef",
    "ListKeyGroupsResultTypeDef",
    "CreateStreamingDistributionResultTypeDef",
    "CreateStreamingDistributionWithTagsResultTypeDef",
    "GetStreamingDistributionResultTypeDef",
    "UpdateStreamingDistributionResultTypeDef",
    "FieldLevelEncryptionTypeDef",
    "GetFieldLevelEncryptionConfigResultTypeDef",
    "FieldLevelEncryptionListTypeDef",
    "CreateFieldLevelEncryptionConfigRequestRequestTypeDef",
    "UpdateFieldLevelEncryptionConfigRequestRequestTypeDef",
    "CreateResponseHeadersPolicyResultTypeDef",
    "GetResponseHeadersPolicyResultTypeDef",
    "ResponseHeadersPolicySummaryTypeDef",
    "UpdateResponseHeadersPolicyResultTypeDef",
    "DistributionConfigOutputTypeDef",
    "DistributionSummaryTypeDef",
    "DistributionConfigTypeDef",
    "CachePolicySummaryTypeDef",
    "CreateCachePolicyResultTypeDef",
    "GetCachePolicyResultTypeDef",
    "UpdateCachePolicyResultTypeDef",
    "OriginRequestPolicyListTypeDef",
    "ContinuousDeploymentPolicySummaryTypeDef",
    "CreateContinuousDeploymentPolicyResultTypeDef",
    "GetContinuousDeploymentPolicyResultTypeDef",
    "UpdateContinuousDeploymentPolicyResultTypeDef",
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    "GetFieldLevelEncryptionProfileResultTypeDef",
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    "GetFieldLevelEncryptionResultTypeDef",
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    "ResponseHeadersPolicyListTypeDef",
    "DistributionTypeDef",
    "GetDistributionConfigResultTypeDef",
    "DistributionListTypeDef",
    "CreateDistributionRequestRequestTypeDef",
    "DistributionConfigWithTagsTypeDef",
    "UpdateDistributionRequestRequestTypeDef",
    "CachePolicyListTypeDef",
    "ListOriginRequestPoliciesResultTypeDef",
    "ContinuousDeploymentPolicyListTypeDef",
    "ListResponseHeadersPoliciesResultTypeDef",
    "CopyDistributionResultTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDistributionWithTagsResultTypeDef",
    "GetDistributionResultTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateDistributionWithStagingConfigResultTypeDef",
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    "ListDistributionsByWebACLIdResultTypeDef",
    "ListDistributionsResultTypeDef",
    "CreateDistributionWithTagsRequestRequestTypeDef",
    "ListCachePoliciesResultTypeDef",
    "ListContinuousDeploymentPoliciesResultTypeDef",
)

AliasICPRecordalTypeDef = TypedDict(
    "AliasICPRecordalTypeDef",
    {
        "CNAME": str,
        "ICPRecordalStatus": ICPRecordalStatusType,
    },
    total=False,
)

_RequiredAliasesOutputTypeDef = TypedDict(
    "_RequiredAliasesOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalAliasesOutputTypeDef = TypedDict(
    "_OptionalAliasesOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class AliasesOutputTypeDef(_RequiredAliasesOutputTypeDef, _OptionalAliasesOutputTypeDef):
    pass

_RequiredAliasesTypeDef = TypedDict(
    "_RequiredAliasesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalAliasesTypeDef = TypedDict(
    "_OptionalAliasesTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class AliasesTypeDef(_RequiredAliasesTypeDef, _OptionalAliasesTypeDef):
    pass

CachedMethodsOutputTypeDef = TypedDict(
    "CachedMethodsOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[MethodType],
    },
)

CachedMethodsTypeDef = TypedDict(
    "CachedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[MethodType],
    },
)

AssociateAliasRequestRequestTypeDef = TypedDict(
    "AssociateAliasRequestRequestTypeDef",
    {
        "TargetDistributionId": str,
        "Alias": str,
    },
)

_RequiredTrustedKeyGroupsOutputTypeDef = TypedDict(
    "_RequiredTrustedKeyGroupsOutputTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalTrustedKeyGroupsOutputTypeDef = TypedDict(
    "_OptionalTrustedKeyGroupsOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class TrustedKeyGroupsOutputTypeDef(
    _RequiredTrustedKeyGroupsOutputTypeDef, _OptionalTrustedKeyGroupsOutputTypeDef
):
    pass

_RequiredTrustedSignersOutputTypeDef = TypedDict(
    "_RequiredTrustedSignersOutputTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalTrustedSignersOutputTypeDef = TypedDict(
    "_OptionalTrustedSignersOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class TrustedSignersOutputTypeDef(
    _RequiredTrustedSignersOutputTypeDef, _OptionalTrustedSignersOutputTypeDef
):
    pass

_RequiredTrustedKeyGroupsTypeDef = TypedDict(
    "_RequiredTrustedKeyGroupsTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalTrustedKeyGroupsTypeDef = TypedDict(
    "_OptionalTrustedKeyGroupsTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class TrustedKeyGroupsTypeDef(_RequiredTrustedKeyGroupsTypeDef, _OptionalTrustedKeyGroupsTypeDef):
    pass

_RequiredTrustedSignersTypeDef = TypedDict(
    "_RequiredTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalTrustedSignersTypeDef = TypedDict(
    "_OptionalTrustedSignersTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class TrustedSignersTypeDef(_RequiredTrustedSignersTypeDef, _OptionalTrustedSignersTypeDef):
    pass

_RequiredCookieNamesOutputTypeDef = TypedDict(
    "_RequiredCookieNamesOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCookieNamesOutputTypeDef = TypedDict(
    "_OptionalCookieNamesOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class CookieNamesOutputTypeDef(
    _RequiredCookieNamesOutputTypeDef, _OptionalCookieNamesOutputTypeDef
):
    pass

_RequiredCookieNamesTypeDef = TypedDict(
    "_RequiredCookieNamesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCookieNamesTypeDef = TypedDict(
    "_OptionalCookieNamesTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class CookieNamesTypeDef(_RequiredCookieNamesTypeDef, _OptionalCookieNamesTypeDef):
    pass

_RequiredHeadersOutputTypeDef = TypedDict(
    "_RequiredHeadersOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalHeadersOutputTypeDef = TypedDict(
    "_OptionalHeadersOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class HeadersOutputTypeDef(_RequiredHeadersOutputTypeDef, _OptionalHeadersOutputTypeDef):
    pass

_RequiredHeadersTypeDef = TypedDict(
    "_RequiredHeadersTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalHeadersTypeDef = TypedDict(
    "_OptionalHeadersTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class HeadersTypeDef(_RequiredHeadersTypeDef, _OptionalHeadersTypeDef):
    pass

_RequiredQueryStringNamesOutputTypeDef = TypedDict(
    "_RequiredQueryStringNamesOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryStringNamesOutputTypeDef = TypedDict(
    "_OptionalQueryStringNamesOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class QueryStringNamesOutputTypeDef(
    _RequiredQueryStringNamesOutputTypeDef, _OptionalQueryStringNamesOutputTypeDef
):
    pass

_RequiredQueryStringNamesTypeDef = TypedDict(
    "_RequiredQueryStringNamesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryStringNamesTypeDef = TypedDict(
    "_OptionalQueryStringNamesTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class QueryStringNamesTypeDef(_RequiredQueryStringNamesTypeDef, _OptionalQueryStringNamesTypeDef):
    pass

CloudFrontOriginAccessIdentityConfigOutputTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityConfigOutputTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
    },
)

CloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
    },
)

CloudFrontOriginAccessIdentitySummaryTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "Comment": str,
    },
)

ConflictingAliasTypeDef = TypedDict(
    "ConflictingAliasTypeDef",
    {
        "Alias": str,
        "DistributionId": str,
        "AccountId": str,
    },
    total=False,
)

_RequiredContentTypeProfileOutputTypeDef = TypedDict(
    "_RequiredContentTypeProfileOutputTypeDef",
    {
        "Format": Literal["URLEncoded"],
        "ContentType": str,
    },
)
_OptionalContentTypeProfileOutputTypeDef = TypedDict(
    "_OptionalContentTypeProfileOutputTypeDef",
    {
        "ProfileId": str,
    },
    total=False,
)

class ContentTypeProfileOutputTypeDef(
    _RequiredContentTypeProfileOutputTypeDef, _OptionalContentTypeProfileOutputTypeDef
):
    pass

_RequiredContentTypeProfileTypeDef = TypedDict(
    "_RequiredContentTypeProfileTypeDef",
    {
        "Format": Literal["URLEncoded"],
        "ContentType": str,
    },
)
_OptionalContentTypeProfileTypeDef = TypedDict(
    "_OptionalContentTypeProfileTypeDef",
    {
        "ProfileId": str,
    },
    total=False,
)

class ContentTypeProfileTypeDef(
    _RequiredContentTypeProfileTypeDef, _OptionalContentTypeProfileTypeDef
):
    pass

_RequiredStagingDistributionDnsNamesOutputTypeDef = TypedDict(
    "_RequiredStagingDistributionDnsNamesOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalStagingDistributionDnsNamesOutputTypeDef = TypedDict(
    "_OptionalStagingDistributionDnsNamesOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class StagingDistributionDnsNamesOutputTypeDef(
    _RequiredStagingDistributionDnsNamesOutputTypeDef,
    _OptionalStagingDistributionDnsNamesOutputTypeDef,
):
    pass

_RequiredStagingDistributionDnsNamesTypeDef = TypedDict(
    "_RequiredStagingDistributionDnsNamesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalStagingDistributionDnsNamesTypeDef = TypedDict(
    "_OptionalStagingDistributionDnsNamesTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class StagingDistributionDnsNamesTypeDef(
    _RequiredStagingDistributionDnsNamesTypeDef, _OptionalStagingDistributionDnsNamesTypeDef
):
    pass

ContinuousDeploymentSingleHeaderConfigOutputTypeDef = TypedDict(
    "ContinuousDeploymentSingleHeaderConfigOutputTypeDef",
    {
        "Header": str,
        "Value": str,
    },
)

ContinuousDeploymentSingleHeaderConfigTypeDef = TypedDict(
    "ContinuousDeploymentSingleHeaderConfigTypeDef",
    {
        "Header": str,
        "Value": str,
    },
)

SessionStickinessConfigOutputTypeDef = TypedDict(
    "SessionStickinessConfigOutputTypeDef",
    {
        "IdleTTL": int,
        "MaximumTTL": int,
    },
)

SessionStickinessConfigTypeDef = TypedDict(
    "SessionStickinessConfigTypeDef",
    {
        "IdleTTL": int,
        "MaximumTTL": int,
    },
)

_RequiredCopyDistributionRequestRequestTypeDef = TypedDict(
    "_RequiredCopyDistributionRequestRequestTypeDef",
    {
        "PrimaryDistributionId": str,
        "CallerReference": str,
    },
)
_OptionalCopyDistributionRequestRequestTypeDef = TypedDict(
    "_OptionalCopyDistributionRequestRequestTypeDef",
    {
        "Staging": bool,
        "IfMatch": str,
    },
    total=False,
)

class CopyDistributionRequestRequestTypeDef(
    _RequiredCopyDistributionRequestRequestTypeDef, _OptionalCopyDistributionRequestRequestTypeDef
):
    pass

FunctionConfigTypeDef = TypedDict(
    "FunctionConfigTypeDef",
    {
        "Comment": str,
        "Runtime": Literal["cloudfront-js-1.0"],
    },
)

_RequiredKeyGroupConfigTypeDef = TypedDict(
    "_RequiredKeyGroupConfigTypeDef",
    {
        "Name": str,
        "Items": Sequence[str],
    },
)
_OptionalKeyGroupConfigTypeDef = TypedDict(
    "_OptionalKeyGroupConfigTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class KeyGroupConfigTypeDef(_RequiredKeyGroupConfigTypeDef, _OptionalKeyGroupConfigTypeDef):
    pass

_RequiredOriginAccessControlConfigTypeDef = TypedDict(
    "_RequiredOriginAccessControlConfigTypeDef",
    {
        "Name": str,
        "SigningProtocol": Literal["sigv4"],
        "SigningBehavior": OriginAccessControlSigningBehaviorsType,
        "OriginAccessControlOriginType": OriginAccessControlOriginTypesType,
    },
)
_OptionalOriginAccessControlConfigTypeDef = TypedDict(
    "_OptionalOriginAccessControlConfigTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class OriginAccessControlConfigTypeDef(
    _RequiredOriginAccessControlConfigTypeDef, _OptionalOriginAccessControlConfigTypeDef
):
    pass

_RequiredPublicKeyConfigTypeDef = TypedDict(
    "_RequiredPublicKeyConfigTypeDef",
    {
        "CallerReference": str,
        "Name": str,
        "EncodedKey": str,
    },
)
_OptionalPublicKeyConfigTypeDef = TypedDict(
    "_OptionalPublicKeyConfigTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class PublicKeyConfigTypeDef(_RequiredPublicKeyConfigTypeDef, _OptionalPublicKeyConfigTypeDef):
    pass

_RequiredCustomErrorResponseOutputTypeDef = TypedDict(
    "_RequiredCustomErrorResponseOutputTypeDef",
    {
        "ErrorCode": int,
    },
)
_OptionalCustomErrorResponseOutputTypeDef = TypedDict(
    "_OptionalCustomErrorResponseOutputTypeDef",
    {
        "ResponsePagePath": str,
        "ResponseCode": str,
        "ErrorCachingMinTTL": int,
    },
    total=False,
)

class CustomErrorResponseOutputTypeDef(
    _RequiredCustomErrorResponseOutputTypeDef, _OptionalCustomErrorResponseOutputTypeDef
):
    pass

_RequiredCustomErrorResponseTypeDef = TypedDict(
    "_RequiredCustomErrorResponseTypeDef",
    {
        "ErrorCode": int,
    },
)
_OptionalCustomErrorResponseTypeDef = TypedDict(
    "_OptionalCustomErrorResponseTypeDef",
    {
        "ResponsePagePath": str,
        "ResponseCode": str,
        "ErrorCachingMinTTL": int,
    },
    total=False,
)

class CustomErrorResponseTypeDef(
    _RequiredCustomErrorResponseTypeDef, _OptionalCustomErrorResponseTypeDef
):
    pass

OriginCustomHeaderOutputTypeDef = TypedDict(
    "OriginCustomHeaderOutputTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)

OriginCustomHeaderTypeDef = TypedDict(
    "OriginCustomHeaderTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)

OriginSslProtocolsOutputTypeDef = TypedDict(
    "OriginSslProtocolsOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[SslProtocolType],
    },
)

OriginSslProtocolsTypeDef = TypedDict(
    "OriginSslProtocolsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[SslProtocolType],
    },
)

_RequiredDeleteCachePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCachePolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteCachePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCachePolicyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteCachePolicyRequestRequestTypeDef(
    _RequiredDeleteCachePolicyRequestRequestTypeDef, _OptionalDeleteCachePolicyRequestRequestTypeDef
):
    pass

_RequiredDeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef(
    _RequiredDeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef,
    _OptionalDeleteCloudFrontOriginAccessIdentityRequestRequestTypeDef,
):
    pass

_RequiredDeleteContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteContinuousDeploymentPolicyRequestRequestTypeDef(
    _RequiredDeleteContinuousDeploymentPolicyRequestRequestTypeDef,
    _OptionalDeleteContinuousDeploymentPolicyRequestRequestTypeDef,
):
    pass

_RequiredDeleteDistributionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteDistributionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDistributionRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteDistributionRequestRequestTypeDef(
    _RequiredDeleteDistributionRequestRequestTypeDef,
    _OptionalDeleteDistributionRequestRequestTypeDef,
):
    pass

_RequiredDeleteFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteFieldLevelEncryptionConfigRequestRequestTypeDef(
    _RequiredDeleteFieldLevelEncryptionConfigRequestRequestTypeDef,
    _OptionalDeleteFieldLevelEncryptionConfigRequestRequestTypeDef,
):
    pass

_RequiredDeleteFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteFieldLevelEncryptionProfileRequestRequestTypeDef(
    _RequiredDeleteFieldLevelEncryptionProfileRequestRequestTypeDef,
    _OptionalDeleteFieldLevelEncryptionProfileRequestRequestTypeDef,
):
    pass

DeleteFunctionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)

_RequiredDeleteKeyGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteKeyGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteKeyGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteKeyGroupRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteKeyGroupRequestRequestTypeDef(
    _RequiredDeleteKeyGroupRequestRequestTypeDef, _OptionalDeleteKeyGroupRequestRequestTypeDef
):
    pass

DeleteMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
    },
)

_RequiredDeleteOriginAccessControlRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteOriginAccessControlRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteOriginAccessControlRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteOriginAccessControlRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteOriginAccessControlRequestRequestTypeDef(
    _RequiredDeleteOriginAccessControlRequestRequestTypeDef,
    _OptionalDeleteOriginAccessControlRequestRequestTypeDef,
):
    pass

_RequiredDeleteOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteOriginRequestPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteOriginRequestPolicyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteOriginRequestPolicyRequestRequestTypeDef(
    _RequiredDeleteOriginRequestPolicyRequestRequestTypeDef,
    _OptionalDeleteOriginRequestPolicyRequestRequestTypeDef,
):
    pass

_RequiredDeletePublicKeyRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePublicKeyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeletePublicKeyRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePublicKeyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeletePublicKeyRequestRequestTypeDef(
    _RequiredDeletePublicKeyRequestRequestTypeDef, _OptionalDeletePublicKeyRequestRequestTypeDef
):
    pass

DeleteRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "DeleteRealtimeLogConfigRequestRequestTypeDef",
    {
        "Name": str,
        "ARN": str,
    },
    total=False,
)

_RequiredDeleteResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResponseHeadersPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResponseHeadersPolicyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteResponseHeadersPolicyRequestRequestTypeDef(
    _RequiredDeleteResponseHeadersPolicyRequestRequestTypeDef,
    _OptionalDeleteResponseHeadersPolicyRequestRequestTypeDef,
):
    pass

_RequiredDeleteStreamingDistributionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamingDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteStreamingDistributionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamingDistributionRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class DeleteStreamingDistributionRequestRequestTypeDef(
    _RequiredDeleteStreamingDistributionRequestRequestTypeDef,
    _OptionalDeleteStreamingDistributionRequestRequestTypeDef,
):
    pass

_RequiredDescribeFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFunctionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFunctionRequestRequestTypeDef",
    {
        "Stage": FunctionStageType,
    },
    total=False,
)

class DescribeFunctionRequestRequestTypeDef(
    _RequiredDescribeFunctionRequestRequestTypeDef, _OptionalDescribeFunctionRequestRequestTypeDef
):
    pass

LoggingConfigOutputTypeDef = TypedDict(
    "LoggingConfigOutputTypeDef",
    {
        "Enabled": bool,
        "IncludeCookies": bool,
        "Bucket": str,
        "Prefix": str,
    },
)

ViewerCertificateOutputTypeDef = TypedDict(
    "ViewerCertificateOutputTypeDef",
    {
        "CloudFrontDefaultCertificate": bool,
        "IAMCertificateId": str,
        "ACMCertificateArn": str,
        "SSLSupportMethod": SSLSupportMethodType,
        "MinimumProtocolVersion": MinimumProtocolVersionType,
        "Certificate": str,
        "CertificateSource": CertificateSourceType,
    },
    total=False,
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "Enabled": bool,
        "IncludeCookies": bool,
        "Bucket": str,
        "Prefix": str,
    },
)

ViewerCertificateTypeDef = TypedDict(
    "ViewerCertificateTypeDef",
    {
        "CloudFrontDefaultCertificate": bool,
        "IAMCertificateId": str,
        "ACMCertificateArn": str,
        "SSLSupportMethod": SSLSupportMethodType,
        "MinimumProtocolVersion": MinimumProtocolVersionType,
        "Certificate": str,
        "CertificateSource": CertificateSourceType,
    },
    total=False,
)

_RequiredDistributionIdListTypeDef = TypedDict(
    "_RequiredDistributionIdListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalDistributionIdListTypeDef = TypedDict(
    "_OptionalDistributionIdListTypeDef",
    {
        "NextMarker": str,
        "Items": List[str],
    },
    total=False,
)

class DistributionIdListTypeDef(
    _RequiredDistributionIdListTypeDef, _OptionalDistributionIdListTypeDef
):
    pass

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFieldPatternsOutputTypeDef = TypedDict(
    "_RequiredFieldPatternsOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalFieldPatternsOutputTypeDef = TypedDict(
    "_OptionalFieldPatternsOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class FieldPatternsOutputTypeDef(
    _RequiredFieldPatternsOutputTypeDef, _OptionalFieldPatternsOutputTypeDef
):
    pass

_RequiredFieldPatternsTypeDef = TypedDict(
    "_RequiredFieldPatternsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalFieldPatternsTypeDef = TypedDict(
    "_OptionalFieldPatternsTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class FieldPatternsTypeDef(_RequiredFieldPatternsTypeDef, _OptionalFieldPatternsTypeDef):
    pass

KinesisStreamConfigOutputTypeDef = TypedDict(
    "KinesisStreamConfigOutputTypeDef",
    {
        "RoleARN": str,
        "StreamARN": str,
    },
)

KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "RoleARN": str,
        "StreamARN": str,
    },
)

_RequiredQueryStringCacheKeysOutputTypeDef = TypedDict(
    "_RequiredQueryStringCacheKeysOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryStringCacheKeysOutputTypeDef = TypedDict(
    "_OptionalQueryStringCacheKeysOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class QueryStringCacheKeysOutputTypeDef(
    _RequiredQueryStringCacheKeysOutputTypeDef, _OptionalQueryStringCacheKeysOutputTypeDef
):
    pass

_RequiredQueryStringCacheKeysTypeDef = TypedDict(
    "_RequiredQueryStringCacheKeysTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryStringCacheKeysTypeDef = TypedDict(
    "_OptionalQueryStringCacheKeysTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class QueryStringCacheKeysTypeDef(
    _RequiredQueryStringCacheKeysTypeDef, _OptionalQueryStringCacheKeysTypeDef
):
    pass

FunctionAssociationOutputTypeDef = TypedDict(
    "FunctionAssociationOutputTypeDef",
    {
        "FunctionARN": str,
        "EventType": EventTypeType,
    },
)

FunctionAssociationTypeDef = TypedDict(
    "FunctionAssociationTypeDef",
    {
        "FunctionARN": str,
        "EventType": EventTypeType,
    },
)

FunctionConfigOutputTypeDef = TypedDict(
    "FunctionConfigOutputTypeDef",
    {
        "Comment": str,
        "Runtime": Literal["cloudfront-js-1.0"],
    },
)

_RequiredFunctionMetadataTypeDef = TypedDict(
    "_RequiredFunctionMetadataTypeDef",
    {
        "FunctionARN": str,
        "LastModifiedTime": datetime,
    },
)
_OptionalFunctionMetadataTypeDef = TypedDict(
    "_OptionalFunctionMetadataTypeDef",
    {
        "Stage": FunctionStageType,
        "CreatedTime": datetime,
    },
    total=False,
)

class FunctionMetadataTypeDef(_RequiredFunctionMetadataTypeDef, _OptionalFunctionMetadataTypeDef):
    pass

_RequiredGeoRestrictionOutputTypeDef = TypedDict(
    "_RequiredGeoRestrictionOutputTypeDef",
    {
        "RestrictionType": GeoRestrictionTypeType,
        "Quantity": int,
    },
)
_OptionalGeoRestrictionOutputTypeDef = TypedDict(
    "_OptionalGeoRestrictionOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class GeoRestrictionOutputTypeDef(
    _RequiredGeoRestrictionOutputTypeDef, _OptionalGeoRestrictionOutputTypeDef
):
    pass

_RequiredGeoRestrictionTypeDef = TypedDict(
    "_RequiredGeoRestrictionTypeDef",
    {
        "RestrictionType": GeoRestrictionTypeType,
        "Quantity": int,
    },
)
_OptionalGeoRestrictionTypeDef = TypedDict(
    "_OptionalGeoRestrictionTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class GeoRestrictionTypeDef(_RequiredGeoRestrictionTypeDef, _OptionalGeoRestrictionTypeDef):
    pass

GetCachePolicyConfigRequestRequestTypeDef = TypedDict(
    "GetCachePolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCachePolicyRequestRequestTypeDef = TypedDict(
    "GetCachePolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetContinuousDeploymentPolicyConfigRequestRequestTypeDef = TypedDict(
    "GetContinuousDeploymentPolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "GetContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetDistributionConfigRequestRequestTypeDef = TypedDict(
    "GetDistributionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

GetDistributionRequestRequestTypeDef = TypedDict(
    "GetDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionRequestRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredGetFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredGetFunctionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalGetFunctionRequestRequestTypeDef",
    {
        "Stage": FunctionStageType,
    },
    total=False,
)

class GetFunctionRequestRequestTypeDef(
    _RequiredGetFunctionRequestRequestTypeDef, _OptionalGetFunctionRequestRequestTypeDef
):
    pass

GetFunctionResultTypeDef = TypedDict(
    "GetFunctionResultTypeDef",
    {
        "FunctionCode": StreamingBody,
        "ETag": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvalidationRequestRequestTypeDef = TypedDict(
    "GetInvalidationRequestRequestTypeDef",
    {
        "DistributionId": str,
        "Id": str,
    },
)

GetKeyGroupConfigRequestRequestTypeDef = TypedDict(
    "GetKeyGroupConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredKeyGroupConfigOutputTypeDef = TypedDict(
    "_RequiredKeyGroupConfigOutputTypeDef",
    {
        "Name": str,
        "Items": List[str],
    },
)
_OptionalKeyGroupConfigOutputTypeDef = TypedDict(
    "_OptionalKeyGroupConfigOutputTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class KeyGroupConfigOutputTypeDef(
    _RequiredKeyGroupConfigOutputTypeDef, _OptionalKeyGroupConfigOutputTypeDef
):
    pass

GetKeyGroupRequestRequestTypeDef = TypedDict(
    "GetKeyGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "GetMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
    },
)

GetOriginAccessControlConfigRequestRequestTypeDef = TypedDict(
    "GetOriginAccessControlConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredOriginAccessControlConfigOutputTypeDef = TypedDict(
    "_RequiredOriginAccessControlConfigOutputTypeDef",
    {
        "Name": str,
        "SigningProtocol": Literal["sigv4"],
        "SigningBehavior": OriginAccessControlSigningBehaviorsType,
        "OriginAccessControlOriginType": OriginAccessControlOriginTypesType,
    },
)
_OptionalOriginAccessControlConfigOutputTypeDef = TypedDict(
    "_OptionalOriginAccessControlConfigOutputTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class OriginAccessControlConfigOutputTypeDef(
    _RequiredOriginAccessControlConfigOutputTypeDef, _OptionalOriginAccessControlConfigOutputTypeDef
):
    pass

GetOriginAccessControlRequestRequestTypeDef = TypedDict(
    "GetOriginAccessControlRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetOriginRequestPolicyConfigRequestRequestTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "GetOriginRequestPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetPublicKeyConfigRequestRequestTypeDef = TypedDict(
    "GetPublicKeyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredPublicKeyConfigOutputTypeDef = TypedDict(
    "_RequiredPublicKeyConfigOutputTypeDef",
    {
        "CallerReference": str,
        "Name": str,
        "EncodedKey": str,
    },
)
_OptionalPublicKeyConfigOutputTypeDef = TypedDict(
    "_OptionalPublicKeyConfigOutputTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class PublicKeyConfigOutputTypeDef(
    _RequiredPublicKeyConfigOutputTypeDef, _OptionalPublicKeyConfigOutputTypeDef
):
    pass

GetPublicKeyRequestRequestTypeDef = TypedDict(
    "GetPublicKeyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "GetRealtimeLogConfigRequestRequestTypeDef",
    {
        "Name": str,
        "ARN": str,
    },
    total=False,
)

GetResponseHeadersPolicyConfigRequestRequestTypeDef = TypedDict(
    "GetResponseHeadersPolicyConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "GetResponseHeadersPolicyRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetStreamingDistributionConfigRequestRequestTypeDef = TypedDict(
    "GetStreamingDistributionConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetStreamingDistributionRequestRequestTypeDef = TypedDict(
    "GetStreamingDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredPathsOutputTypeDef = TypedDict(
    "_RequiredPathsOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalPathsOutputTypeDef = TypedDict(
    "_OptionalPathsOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class PathsOutputTypeDef(_RequiredPathsOutputTypeDef, _OptionalPathsOutputTypeDef):
    pass

_RequiredPathsTypeDef = TypedDict(
    "_RequiredPathsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalPathsTypeDef = TypedDict(
    "_OptionalPathsTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class PathsTypeDef(_RequiredPathsTypeDef, _OptionalPathsTypeDef):
    pass

InvalidationSummaryTypeDef = TypedDict(
    "InvalidationSummaryTypeDef",
    {
        "Id": str,
        "CreateTime": datetime,
        "Status": str,
    },
)

_RequiredKeyPairIdsTypeDef = TypedDict(
    "_RequiredKeyPairIdsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalKeyPairIdsTypeDef = TypedDict(
    "_OptionalKeyPairIdsTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class KeyPairIdsTypeDef(_RequiredKeyPairIdsTypeDef, _OptionalKeyPairIdsTypeDef):
    pass

_RequiredLambdaFunctionAssociationOutputTypeDef = TypedDict(
    "_RequiredLambdaFunctionAssociationOutputTypeDef",
    {
        "LambdaFunctionARN": str,
        "EventType": EventTypeType,
    },
)
_OptionalLambdaFunctionAssociationOutputTypeDef = TypedDict(
    "_OptionalLambdaFunctionAssociationOutputTypeDef",
    {
        "IncludeBody": bool,
    },
    total=False,
)

class LambdaFunctionAssociationOutputTypeDef(
    _RequiredLambdaFunctionAssociationOutputTypeDef, _OptionalLambdaFunctionAssociationOutputTypeDef
):
    pass

_RequiredLambdaFunctionAssociationTypeDef = TypedDict(
    "_RequiredLambdaFunctionAssociationTypeDef",
    {
        "LambdaFunctionARN": str,
        "EventType": EventTypeType,
    },
)
_OptionalLambdaFunctionAssociationTypeDef = TypedDict(
    "_OptionalLambdaFunctionAssociationTypeDef",
    {
        "IncludeBody": bool,
    },
    total=False,
)

class LambdaFunctionAssociationTypeDef(
    _RequiredLambdaFunctionAssociationTypeDef, _OptionalLambdaFunctionAssociationTypeDef
):
    pass

ListCachePoliciesRequestRequestTypeDef = TypedDict(
    "ListCachePoliciesRequestRequestTypeDef",
    {
        "Type": CachePolicyTypeType,
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListCloudFrontOriginAccessIdentitiesRequestListCloudFrontOriginAccessIdentitiesPaginateTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesRequestListCloudFrontOriginAccessIdentitiesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

_RequiredListConflictingAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListConflictingAliasesRequestRequestTypeDef",
    {
        "DistributionId": str,
        "Alias": str,
    },
)
_OptionalListConflictingAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListConflictingAliasesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListConflictingAliasesRequestRequestTypeDef(
    _RequiredListConflictingAliasesRequestRequestTypeDef,
    _OptionalListConflictingAliasesRequestRequestTypeDef,
):
    pass

ListContinuousDeploymentPoliciesRequestRequestTypeDef = TypedDict(
    "ListContinuousDeploymentPoliciesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

_RequiredListDistributionsByCachePolicyIdRequestRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByCachePolicyIdRequestRequestTypeDef",
    {
        "CachePolicyId": str,
    },
)
_OptionalListDistributionsByCachePolicyIdRequestRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByCachePolicyIdRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

class ListDistributionsByCachePolicyIdRequestRequestTypeDef(
    _RequiredListDistributionsByCachePolicyIdRequestRequestTypeDef,
    _OptionalListDistributionsByCachePolicyIdRequestRequestTypeDef,
):
    pass

_RequiredListDistributionsByKeyGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupId": str,
    },
)
_OptionalListDistributionsByKeyGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByKeyGroupRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

class ListDistributionsByKeyGroupRequestRequestTypeDef(
    _RequiredListDistributionsByKeyGroupRequestRequestTypeDef,
    _OptionalListDistributionsByKeyGroupRequestRequestTypeDef,
):
    pass

_RequiredListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef",
    {
        "OriginRequestPolicyId": str,
    },
)
_OptionalListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

class ListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef(
    _RequiredListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef,
    _OptionalListDistributionsByOriginRequestPolicyIdRequestRequestTypeDef,
):
    pass

ListDistributionsByRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
        "RealtimeLogConfigName": str,
        "RealtimeLogConfigArn": str,
    },
    total=False,
)

_RequiredListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyId": str,
    },
)
_OptionalListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

class ListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef(
    _RequiredListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef,
    _OptionalListDistributionsByResponseHeadersPolicyIdRequestRequestTypeDef,
):
    pass

_RequiredListDistributionsByWebACLIdRequestRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByWebACLIdRequestRequestTypeDef",
    {
        "WebACLId": str,
    },
)
_OptionalListDistributionsByWebACLIdRequestRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByWebACLIdRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

class ListDistributionsByWebACLIdRequestRequestTypeDef(
    _RequiredListDistributionsByWebACLIdRequestRequestTypeDef,
    _OptionalListDistributionsByWebACLIdRequestRequestTypeDef,
):
    pass

ListDistributionsRequestListDistributionsPaginateTypeDef = TypedDict(
    "ListDistributionsRequestListDistributionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDistributionsRequestRequestTypeDef = TypedDict(
    "ListDistributionsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListFieldLevelEncryptionConfigsRequestRequestTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListFieldLevelEncryptionProfilesRequestRequestTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListFunctionsRequestRequestTypeDef = TypedDict(
    "ListFunctionsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
        "Stage": FunctionStageType,
    },
    total=False,
)

_RequiredListInvalidationsRequestListInvalidationsPaginateTypeDef = TypedDict(
    "_RequiredListInvalidationsRequestListInvalidationsPaginateTypeDef",
    {
        "DistributionId": str,
    },
)
_OptionalListInvalidationsRequestListInvalidationsPaginateTypeDef = TypedDict(
    "_OptionalListInvalidationsRequestListInvalidationsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListInvalidationsRequestListInvalidationsPaginateTypeDef(
    _RequiredListInvalidationsRequestListInvalidationsPaginateTypeDef,
    _OptionalListInvalidationsRequestListInvalidationsPaginateTypeDef,
):
    pass

_RequiredListInvalidationsRequestRequestTypeDef = TypedDict(
    "_RequiredListInvalidationsRequestRequestTypeDef",
    {
        "DistributionId": str,
    },
)
_OptionalListInvalidationsRequestRequestTypeDef = TypedDict(
    "_OptionalListInvalidationsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

class ListInvalidationsRequestRequestTypeDef(
    _RequiredListInvalidationsRequestRequestTypeDef, _OptionalListInvalidationsRequestRequestTypeDef
):
    pass

ListKeyGroupsRequestRequestTypeDef = TypedDict(
    "ListKeyGroupsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListOriginAccessControlsRequestRequestTypeDef = TypedDict(
    "ListOriginAccessControlsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListOriginRequestPoliciesRequestRequestTypeDef = TypedDict(
    "ListOriginRequestPoliciesRequestRequestTypeDef",
    {
        "Type": OriginRequestPolicyTypeType,
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListRealtimeLogConfigsRequestRequestTypeDef = TypedDict(
    "ListRealtimeLogConfigsRequestRequestTypeDef",
    {
        "MaxItems": str,
        "Marker": str,
    },
    total=False,
)

ListResponseHeadersPoliciesRequestRequestTypeDef = TypedDict(
    "ListResponseHeadersPoliciesRequestRequestTypeDef",
    {
        "Type": ResponseHeadersPolicyTypeType,
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListStreamingDistributionsRequestListStreamingDistributionsPaginateTypeDef = TypedDict(
    "ListStreamingDistributionsRequestListStreamingDistributionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListStreamingDistributionsRequestRequestTypeDef = TypedDict(
    "ListStreamingDistributionsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Resource": str,
    },
)

RealtimeMetricsSubscriptionConfigOutputTypeDef = TypedDict(
    "RealtimeMetricsSubscriptionConfigOutputTypeDef",
    {
        "RealtimeMetricsSubscriptionStatus": RealtimeMetricsSubscriptionStatusType,
    },
)

RealtimeMetricsSubscriptionConfigTypeDef = TypedDict(
    "RealtimeMetricsSubscriptionConfigTypeDef",
    {
        "RealtimeMetricsSubscriptionStatus": RealtimeMetricsSubscriptionStatusType,
    },
)

OriginAccessControlSummaryTypeDef = TypedDict(
    "OriginAccessControlSummaryTypeDef",
    {
        "Id": str,
        "Description": str,
        "Name": str,
        "SigningProtocol": Literal["sigv4"],
        "SigningBehavior": OriginAccessControlSigningBehaviorsType,
        "OriginAccessControlOriginType": OriginAccessControlOriginTypesType,
    },
)

StatusCodesOutputTypeDef = TypedDict(
    "StatusCodesOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[int],
    },
)

StatusCodesTypeDef = TypedDict(
    "StatusCodesTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[int],
    },
)

OriginGroupMemberOutputTypeDef = TypedDict(
    "OriginGroupMemberOutputTypeDef",
    {
        "OriginId": str,
    },
)

OriginGroupMemberTypeDef = TypedDict(
    "OriginGroupMemberTypeDef",
    {
        "OriginId": str,
    },
)

_RequiredOriginShieldOutputTypeDef = TypedDict(
    "_RequiredOriginShieldOutputTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalOriginShieldOutputTypeDef = TypedDict(
    "_OptionalOriginShieldOutputTypeDef",
    {
        "OriginShieldRegion": str,
    },
    total=False,
)

class OriginShieldOutputTypeDef(
    _RequiredOriginShieldOutputTypeDef, _OptionalOriginShieldOutputTypeDef
):
    pass

S3OriginConfigOutputTypeDef = TypedDict(
    "S3OriginConfigOutputTypeDef",
    {
        "OriginAccessIdentity": str,
    },
)

_RequiredOriginShieldTypeDef = TypedDict(
    "_RequiredOriginShieldTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalOriginShieldTypeDef = TypedDict(
    "_OptionalOriginShieldTypeDef",
    {
        "OriginShieldRegion": str,
    },
    total=False,
)

class OriginShieldTypeDef(_RequiredOriginShieldTypeDef, _OptionalOriginShieldTypeDef):
    pass

S3OriginConfigTypeDef = TypedDict(
    "S3OriginConfigTypeDef",
    {
        "OriginAccessIdentity": str,
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

_RequiredPublicKeySummaryTypeDef = TypedDict(
    "_RequiredPublicKeySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatedTime": datetime,
        "EncodedKey": str,
    },
)
_OptionalPublicKeySummaryTypeDef = TypedDict(
    "_OptionalPublicKeySummaryTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class PublicKeySummaryTypeDef(_RequiredPublicKeySummaryTypeDef, _OptionalPublicKeySummaryTypeDef):
    pass

PublishFunctionRequestRequestTypeDef = TypedDict(
    "PublishFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)

QueryArgProfileOutputTypeDef = TypedDict(
    "QueryArgProfileOutputTypeDef",
    {
        "QueryArg": str,
        "ProfileId": str,
    },
)

QueryArgProfileTypeDef = TypedDict(
    "QueryArgProfileTypeDef",
    {
        "QueryArg": str,
        "ProfileId": str,
    },
)

ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[str],
    },
)

ResponseHeadersPolicyAccessControlAllowHeadersTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowHeadersTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[str],
    },
)

ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[ResponseHeadersPolicyAccessControlAllowMethodsValuesType],
    },
)

ResponseHeadersPolicyAccessControlAllowMethodsTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowMethodsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[ResponseHeadersPolicyAccessControlAllowMethodsValuesType],
    },
)

ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[str],
    },
)

ResponseHeadersPolicyAccessControlAllowOriginsTypeDef = TypedDict(
    "ResponseHeadersPolicyAccessControlAllowOriginsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[str],
    },
)

_RequiredResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

class ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef(
    _RequiredResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef,
    _OptionalResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef,
):
    pass

_RequiredResponseHeadersPolicyAccessControlExposeHeadersTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyAccessControlExposeHeadersTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalResponseHeadersPolicyAccessControlExposeHeadersTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyAccessControlExposeHeadersTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

class ResponseHeadersPolicyAccessControlExposeHeadersTypeDef(
    _RequiredResponseHeadersPolicyAccessControlExposeHeadersTypeDef,
    _OptionalResponseHeadersPolicyAccessControlExposeHeadersTypeDef,
):
    pass

_RequiredResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef",
    {
        "SamplingRate": float,
    },
    total=False,
)

class ResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef(
    _RequiredResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef,
    _OptionalResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef,
):
    pass

_RequiredResponseHeadersPolicyServerTimingHeadersConfigTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyServerTimingHeadersConfigTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalResponseHeadersPolicyServerTimingHeadersConfigTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyServerTimingHeadersConfigTypeDef",
    {
        "SamplingRate": float,
    },
    total=False,
)

class ResponseHeadersPolicyServerTimingHeadersConfigTypeDef(
    _RequiredResponseHeadersPolicyServerTimingHeadersConfigTypeDef,
    _OptionalResponseHeadersPolicyServerTimingHeadersConfigTypeDef,
):
    pass

ResponseHeadersPolicyContentSecurityPolicyOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyContentSecurityPolicyOutputTypeDef",
    {
        "Override": bool,
        "ContentSecurityPolicy": str,
    },
)

ResponseHeadersPolicyContentSecurityPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyContentSecurityPolicyTypeDef",
    {
        "Override": bool,
        "ContentSecurityPolicy": str,
    },
)

ResponseHeadersPolicyContentTypeOptionsOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyContentTypeOptionsOutputTypeDef",
    {
        "Override": bool,
    },
)

ResponseHeadersPolicyContentTypeOptionsTypeDef = TypedDict(
    "ResponseHeadersPolicyContentTypeOptionsTypeDef",
    {
        "Override": bool,
    },
)

ResponseHeadersPolicyCustomHeaderOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyCustomHeaderOutputTypeDef",
    {
        "Header": str,
        "Value": str,
        "Override": bool,
    },
)

ResponseHeadersPolicyCustomHeaderTypeDef = TypedDict(
    "ResponseHeadersPolicyCustomHeaderTypeDef",
    {
        "Header": str,
        "Value": str,
        "Override": bool,
    },
)

ResponseHeadersPolicyFrameOptionsOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyFrameOptionsOutputTypeDef",
    {
        "Override": bool,
        "FrameOption": FrameOptionsListType,
    },
)

ResponseHeadersPolicyFrameOptionsTypeDef = TypedDict(
    "ResponseHeadersPolicyFrameOptionsTypeDef",
    {
        "Override": bool,
        "FrameOption": FrameOptionsListType,
    },
)

ResponseHeadersPolicyReferrerPolicyOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyReferrerPolicyOutputTypeDef",
    {
        "Override": bool,
        "ReferrerPolicy": ReferrerPolicyListType,
    },
)

ResponseHeadersPolicyReferrerPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyReferrerPolicyTypeDef",
    {
        "Override": bool,
        "ReferrerPolicy": ReferrerPolicyListType,
    },
)

ResponseHeadersPolicyRemoveHeaderOutputTypeDef = TypedDict(
    "ResponseHeadersPolicyRemoveHeaderOutputTypeDef",
    {
        "Header": str,
    },
)

ResponseHeadersPolicyRemoveHeaderTypeDef = TypedDict(
    "ResponseHeadersPolicyRemoveHeaderTypeDef",
    {
        "Header": str,
    },
)

_RequiredResponseHeadersPolicyStrictTransportSecurityOutputTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyStrictTransportSecurityOutputTypeDef",
    {
        "Override": bool,
        "AccessControlMaxAgeSec": int,
    },
)
_OptionalResponseHeadersPolicyStrictTransportSecurityOutputTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyStrictTransportSecurityOutputTypeDef",
    {
        "IncludeSubdomains": bool,
        "Preload": bool,
    },
    total=False,
)

class ResponseHeadersPolicyStrictTransportSecurityOutputTypeDef(
    _RequiredResponseHeadersPolicyStrictTransportSecurityOutputTypeDef,
    _OptionalResponseHeadersPolicyStrictTransportSecurityOutputTypeDef,
):
    pass

_RequiredResponseHeadersPolicyXSSProtectionOutputTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyXSSProtectionOutputTypeDef",
    {
        "Override": bool,
        "Protection": bool,
    },
)
_OptionalResponseHeadersPolicyXSSProtectionOutputTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyXSSProtectionOutputTypeDef",
    {
        "ModeBlock": bool,
        "ReportUri": str,
    },
    total=False,
)

class ResponseHeadersPolicyXSSProtectionOutputTypeDef(
    _RequiredResponseHeadersPolicyXSSProtectionOutputTypeDef,
    _OptionalResponseHeadersPolicyXSSProtectionOutputTypeDef,
):
    pass

_RequiredResponseHeadersPolicyStrictTransportSecurityTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyStrictTransportSecurityTypeDef",
    {
        "Override": bool,
        "AccessControlMaxAgeSec": int,
    },
)
_OptionalResponseHeadersPolicyStrictTransportSecurityTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyStrictTransportSecurityTypeDef",
    {
        "IncludeSubdomains": bool,
        "Preload": bool,
    },
    total=False,
)

class ResponseHeadersPolicyStrictTransportSecurityTypeDef(
    _RequiredResponseHeadersPolicyStrictTransportSecurityTypeDef,
    _OptionalResponseHeadersPolicyStrictTransportSecurityTypeDef,
):
    pass

_RequiredResponseHeadersPolicyXSSProtectionTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyXSSProtectionTypeDef",
    {
        "Override": bool,
        "Protection": bool,
    },
)
_OptionalResponseHeadersPolicyXSSProtectionTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyXSSProtectionTypeDef",
    {
        "ModeBlock": bool,
        "ReportUri": str,
    },
    total=False,
)

class ResponseHeadersPolicyXSSProtectionTypeDef(
    _RequiredResponseHeadersPolicyXSSProtectionTypeDef,
    _OptionalResponseHeadersPolicyXSSProtectionTypeDef,
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

S3OriginOutputTypeDef = TypedDict(
    "S3OriginOutputTypeDef",
    {
        "DomainName": str,
        "OriginAccessIdentity": str,
    },
)

S3OriginTypeDef = TypedDict(
    "S3OriginTypeDef",
    {
        "DomainName": str,
        "OriginAccessIdentity": str,
    },
)

StreamingLoggingConfigOutputTypeDef = TypedDict(
    "StreamingLoggingConfigOutputTypeDef",
    {
        "Enabled": bool,
        "Bucket": str,
        "Prefix": str,
    },
)

StreamingLoggingConfigTypeDef = TypedDict(
    "StreamingLoggingConfigTypeDef",
    {
        "Enabled": bool,
        "Bucket": str,
        "Prefix": str,
    },
)

TagKeysTypeDef = TypedDict(
    "TagKeysTypeDef",
    {
        "Items": Sequence[str],
    },
    total=False,
)

_RequiredTagOutputTypeDef = TypedDict(
    "_RequiredTagOutputTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagOutputTypeDef = TypedDict(
    "_OptionalTagOutputTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagOutputTypeDef(_RequiredTagOutputTypeDef, _OptionalTagOutputTypeDef):
    pass

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

_RequiredTestFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredTestFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
        "EventObject": Union[str, bytes, IO[Any], StreamingBody],
    },
)
_OptionalTestFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalTestFunctionRequestRequestTypeDef",
    {
        "Stage": FunctionStageType,
    },
    total=False,
)

class TestFunctionRequestRequestTypeDef(
    _RequiredTestFunctionRequestRequestTypeDef, _OptionalTestFunctionRequestRequestTypeDef
):
    pass

_RequiredUpdateDistributionWithStagingConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDistributionWithStagingConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateDistributionWithStagingConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDistributionWithStagingConfigRequestRequestTypeDef",
    {
        "StagingDistributionId": str,
        "IfMatch": str,
    },
    total=False,
)

class UpdateDistributionWithStagingConfigRequestRequestTypeDef(
    _RequiredUpdateDistributionWithStagingConfigRequestRequestTypeDef,
    _OptionalUpdateDistributionWithStagingConfigRequestRequestTypeDef,
):
    pass

_RequiredAllowedMethodsOutputTypeDef = TypedDict(
    "_RequiredAllowedMethodsOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[MethodType],
    },
)
_OptionalAllowedMethodsOutputTypeDef = TypedDict(
    "_OptionalAllowedMethodsOutputTypeDef",
    {
        "CachedMethods": CachedMethodsOutputTypeDef,
    },
    total=False,
)

class AllowedMethodsOutputTypeDef(
    _RequiredAllowedMethodsOutputTypeDef, _OptionalAllowedMethodsOutputTypeDef
):
    pass

_RequiredAllowedMethodsTypeDef = TypedDict(
    "_RequiredAllowedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[MethodType],
    },
)
_OptionalAllowedMethodsTypeDef = TypedDict(
    "_OptionalAllowedMethodsTypeDef",
    {
        "CachedMethods": CachedMethodsTypeDef,
    },
    total=False,
)

class AllowedMethodsTypeDef(_RequiredAllowedMethodsTypeDef, _OptionalAllowedMethodsTypeDef):
    pass

_RequiredCachePolicyCookiesConfigOutputTypeDef = TypedDict(
    "_RequiredCachePolicyCookiesConfigOutputTypeDef",
    {
        "CookieBehavior": CachePolicyCookieBehaviorType,
    },
)
_OptionalCachePolicyCookiesConfigOutputTypeDef = TypedDict(
    "_OptionalCachePolicyCookiesConfigOutputTypeDef",
    {
        "Cookies": CookieNamesOutputTypeDef,
    },
    total=False,
)

class CachePolicyCookiesConfigOutputTypeDef(
    _RequiredCachePolicyCookiesConfigOutputTypeDef, _OptionalCachePolicyCookiesConfigOutputTypeDef
):
    pass

_RequiredCookiePreferenceOutputTypeDef = TypedDict(
    "_RequiredCookiePreferenceOutputTypeDef",
    {
        "Forward": ItemSelectionType,
    },
)
_OptionalCookiePreferenceOutputTypeDef = TypedDict(
    "_OptionalCookiePreferenceOutputTypeDef",
    {
        "WhitelistedNames": CookieNamesOutputTypeDef,
    },
    total=False,
)

class CookiePreferenceOutputTypeDef(
    _RequiredCookiePreferenceOutputTypeDef, _OptionalCookiePreferenceOutputTypeDef
):
    pass

_RequiredOriginRequestPolicyCookiesConfigOutputTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyCookiesConfigOutputTypeDef",
    {
        "CookieBehavior": OriginRequestPolicyCookieBehaviorType,
    },
)
_OptionalOriginRequestPolicyCookiesConfigOutputTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyCookiesConfigOutputTypeDef",
    {
        "Cookies": CookieNamesOutputTypeDef,
    },
    total=False,
)

class OriginRequestPolicyCookiesConfigOutputTypeDef(
    _RequiredOriginRequestPolicyCookiesConfigOutputTypeDef,
    _OptionalOriginRequestPolicyCookiesConfigOutputTypeDef,
):
    pass

_RequiredCachePolicyCookiesConfigTypeDef = TypedDict(
    "_RequiredCachePolicyCookiesConfigTypeDef",
    {
        "CookieBehavior": CachePolicyCookieBehaviorType,
    },
)
_OptionalCachePolicyCookiesConfigTypeDef = TypedDict(
    "_OptionalCachePolicyCookiesConfigTypeDef",
    {
        "Cookies": CookieNamesTypeDef,
    },
    total=False,
)

class CachePolicyCookiesConfigTypeDef(
    _RequiredCachePolicyCookiesConfigTypeDef, _OptionalCachePolicyCookiesConfigTypeDef
):
    pass

_RequiredCookiePreferenceTypeDef = TypedDict(
    "_RequiredCookiePreferenceTypeDef",
    {
        "Forward": ItemSelectionType,
    },
)
_OptionalCookiePreferenceTypeDef = TypedDict(
    "_OptionalCookiePreferenceTypeDef",
    {
        "WhitelistedNames": CookieNamesTypeDef,
    },
    total=False,
)

class CookiePreferenceTypeDef(_RequiredCookiePreferenceTypeDef, _OptionalCookiePreferenceTypeDef):
    pass

_RequiredOriginRequestPolicyCookiesConfigTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyCookiesConfigTypeDef",
    {
        "CookieBehavior": OriginRequestPolicyCookieBehaviorType,
    },
)
_OptionalOriginRequestPolicyCookiesConfigTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyCookiesConfigTypeDef",
    {
        "Cookies": CookieNamesTypeDef,
    },
    total=False,
)

class OriginRequestPolicyCookiesConfigTypeDef(
    _RequiredOriginRequestPolicyCookiesConfigTypeDef,
    _OptionalOriginRequestPolicyCookiesConfigTypeDef,
):
    pass

_RequiredCachePolicyHeadersConfigOutputTypeDef = TypedDict(
    "_RequiredCachePolicyHeadersConfigOutputTypeDef",
    {
        "HeaderBehavior": CachePolicyHeaderBehaviorType,
    },
)
_OptionalCachePolicyHeadersConfigOutputTypeDef = TypedDict(
    "_OptionalCachePolicyHeadersConfigOutputTypeDef",
    {
        "Headers": HeadersOutputTypeDef,
    },
    total=False,
)

class CachePolicyHeadersConfigOutputTypeDef(
    _RequiredCachePolicyHeadersConfigOutputTypeDef, _OptionalCachePolicyHeadersConfigOutputTypeDef
):
    pass

_RequiredOriginRequestPolicyHeadersConfigOutputTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyHeadersConfigOutputTypeDef",
    {
        "HeaderBehavior": OriginRequestPolicyHeaderBehaviorType,
    },
)
_OptionalOriginRequestPolicyHeadersConfigOutputTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyHeadersConfigOutputTypeDef",
    {
        "Headers": HeadersOutputTypeDef,
    },
    total=False,
)

class OriginRequestPolicyHeadersConfigOutputTypeDef(
    _RequiredOriginRequestPolicyHeadersConfigOutputTypeDef,
    _OptionalOriginRequestPolicyHeadersConfigOutputTypeDef,
):
    pass

_RequiredCachePolicyHeadersConfigTypeDef = TypedDict(
    "_RequiredCachePolicyHeadersConfigTypeDef",
    {
        "HeaderBehavior": CachePolicyHeaderBehaviorType,
    },
)
_OptionalCachePolicyHeadersConfigTypeDef = TypedDict(
    "_OptionalCachePolicyHeadersConfigTypeDef",
    {
        "Headers": HeadersTypeDef,
    },
    total=False,
)

class CachePolicyHeadersConfigTypeDef(
    _RequiredCachePolicyHeadersConfigTypeDef, _OptionalCachePolicyHeadersConfigTypeDef
):
    pass

_RequiredOriginRequestPolicyHeadersConfigTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyHeadersConfigTypeDef",
    {
        "HeaderBehavior": OriginRequestPolicyHeaderBehaviorType,
    },
)
_OptionalOriginRequestPolicyHeadersConfigTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyHeadersConfigTypeDef",
    {
        "Headers": HeadersTypeDef,
    },
    total=False,
)

class OriginRequestPolicyHeadersConfigTypeDef(
    _RequiredOriginRequestPolicyHeadersConfigTypeDef,
    _OptionalOriginRequestPolicyHeadersConfigTypeDef,
):
    pass

_RequiredCachePolicyQueryStringsConfigOutputTypeDef = TypedDict(
    "_RequiredCachePolicyQueryStringsConfigOutputTypeDef",
    {
        "QueryStringBehavior": CachePolicyQueryStringBehaviorType,
    },
)
_OptionalCachePolicyQueryStringsConfigOutputTypeDef = TypedDict(
    "_OptionalCachePolicyQueryStringsConfigOutputTypeDef",
    {
        "QueryStrings": QueryStringNamesOutputTypeDef,
    },
    total=False,
)

class CachePolicyQueryStringsConfigOutputTypeDef(
    _RequiredCachePolicyQueryStringsConfigOutputTypeDef,
    _OptionalCachePolicyQueryStringsConfigOutputTypeDef,
):
    pass

_RequiredOriginRequestPolicyQueryStringsConfigOutputTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyQueryStringsConfigOutputTypeDef",
    {
        "QueryStringBehavior": OriginRequestPolicyQueryStringBehaviorType,
    },
)
_OptionalOriginRequestPolicyQueryStringsConfigOutputTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyQueryStringsConfigOutputTypeDef",
    {
        "QueryStrings": QueryStringNamesOutputTypeDef,
    },
    total=False,
)

class OriginRequestPolicyQueryStringsConfigOutputTypeDef(
    _RequiredOriginRequestPolicyQueryStringsConfigOutputTypeDef,
    _OptionalOriginRequestPolicyQueryStringsConfigOutputTypeDef,
):
    pass

_RequiredCachePolicyQueryStringsConfigTypeDef = TypedDict(
    "_RequiredCachePolicyQueryStringsConfigTypeDef",
    {
        "QueryStringBehavior": CachePolicyQueryStringBehaviorType,
    },
)
_OptionalCachePolicyQueryStringsConfigTypeDef = TypedDict(
    "_OptionalCachePolicyQueryStringsConfigTypeDef",
    {
        "QueryStrings": QueryStringNamesTypeDef,
    },
    total=False,
)

class CachePolicyQueryStringsConfigTypeDef(
    _RequiredCachePolicyQueryStringsConfigTypeDef, _OptionalCachePolicyQueryStringsConfigTypeDef
):
    pass

_RequiredOriginRequestPolicyQueryStringsConfigTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyQueryStringsConfigTypeDef",
    {
        "QueryStringBehavior": OriginRequestPolicyQueryStringBehaviorType,
    },
)
_OptionalOriginRequestPolicyQueryStringsConfigTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyQueryStringsConfigTypeDef",
    {
        "QueryStrings": QueryStringNamesTypeDef,
    },
    total=False,
)

class OriginRequestPolicyQueryStringsConfigTypeDef(
    _RequiredOriginRequestPolicyQueryStringsConfigTypeDef,
    _OptionalOriginRequestPolicyQueryStringsConfigTypeDef,
):
    pass

_RequiredCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_RequiredCloudFrontOriginAccessIdentityTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
    },
)
_OptionalCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_OptionalCloudFrontOriginAccessIdentityTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigOutputTypeDef,
    },
    total=False,
)

class CloudFrontOriginAccessIdentityTypeDef(
    _RequiredCloudFrontOriginAccessIdentityTypeDef, _OptionalCloudFrontOriginAccessIdentityTypeDef
):
    pass

GetCloudFrontOriginAccessIdentityConfigResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigTypeDef,
    },
)

_RequiredUpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": CloudFrontOriginAccessIdentityConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef(
    _RequiredUpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef,
    _OptionalUpdateCloudFrontOriginAccessIdentityRequestRequestTypeDef,
):
    pass

_RequiredCloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "_RequiredCloudFrontOriginAccessIdentityListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalCloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "_OptionalCloudFrontOriginAccessIdentityListTypeDef",
    {
        "NextMarker": str,
        "Items": List[CloudFrontOriginAccessIdentitySummaryTypeDef],
    },
    total=False,
)

class CloudFrontOriginAccessIdentityListTypeDef(
    _RequiredCloudFrontOriginAccessIdentityListTypeDef,
    _OptionalCloudFrontOriginAccessIdentityListTypeDef,
):
    pass

ConflictingAliasesListTypeDef = TypedDict(
    "ConflictingAliasesListTypeDef",
    {
        "NextMarker": str,
        "MaxItems": int,
        "Quantity": int,
        "Items": List[ConflictingAliasTypeDef],
    },
    total=False,
)

_RequiredContentTypeProfilesOutputTypeDef = TypedDict(
    "_RequiredContentTypeProfilesOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalContentTypeProfilesOutputTypeDef = TypedDict(
    "_OptionalContentTypeProfilesOutputTypeDef",
    {
        "Items": List[ContentTypeProfileOutputTypeDef],
    },
    total=False,
)

class ContentTypeProfilesOutputTypeDef(
    _RequiredContentTypeProfilesOutputTypeDef, _OptionalContentTypeProfilesOutputTypeDef
):
    pass

_RequiredContentTypeProfilesTypeDef = TypedDict(
    "_RequiredContentTypeProfilesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalContentTypeProfilesTypeDef = TypedDict(
    "_OptionalContentTypeProfilesTypeDef",
    {
        "Items": Sequence[ContentTypeProfileTypeDef],
    },
    total=False,
)

class ContentTypeProfilesTypeDef(
    _RequiredContentTypeProfilesTypeDef, _OptionalContentTypeProfilesTypeDef
):
    pass

_RequiredContinuousDeploymentSingleWeightConfigOutputTypeDef = TypedDict(
    "_RequiredContinuousDeploymentSingleWeightConfigOutputTypeDef",
    {
        "Weight": float,
    },
)
_OptionalContinuousDeploymentSingleWeightConfigOutputTypeDef = TypedDict(
    "_OptionalContinuousDeploymentSingleWeightConfigOutputTypeDef",
    {
        "SessionStickinessConfig": SessionStickinessConfigOutputTypeDef,
    },
    total=False,
)

class ContinuousDeploymentSingleWeightConfigOutputTypeDef(
    _RequiredContinuousDeploymentSingleWeightConfigOutputTypeDef,
    _OptionalContinuousDeploymentSingleWeightConfigOutputTypeDef,
):
    pass

_RequiredContinuousDeploymentSingleWeightConfigTypeDef = TypedDict(
    "_RequiredContinuousDeploymentSingleWeightConfigTypeDef",
    {
        "Weight": float,
    },
)
_OptionalContinuousDeploymentSingleWeightConfigTypeDef = TypedDict(
    "_OptionalContinuousDeploymentSingleWeightConfigTypeDef",
    {
        "SessionStickinessConfig": SessionStickinessConfigTypeDef,
    },
    total=False,
)

class ContinuousDeploymentSingleWeightConfigTypeDef(
    _RequiredContinuousDeploymentSingleWeightConfigTypeDef,
    _OptionalContinuousDeploymentSingleWeightConfigTypeDef,
):
    pass

CreateFunctionRequestRequestTypeDef = TypedDict(
    "CreateFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "FunctionConfig": FunctionConfigTypeDef,
        "FunctionCode": Union[str, bytes, IO[Any], StreamingBody],
    },
)

UpdateFunctionRequestRequestTypeDef = TypedDict(
    "UpdateFunctionRequestRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
        "FunctionConfig": FunctionConfigTypeDef,
        "FunctionCode": Union[str, bytes, IO[Any], StreamingBody],
    },
)

CreateKeyGroupRequestRequestTypeDef = TypedDict(
    "CreateKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupConfig": KeyGroupConfigTypeDef,
    },
)

_RequiredUpdateKeyGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKeyGroupRequestRequestTypeDef",
    {
        "KeyGroupConfig": KeyGroupConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateKeyGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKeyGroupRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateKeyGroupRequestRequestTypeDef(
    _RequiredUpdateKeyGroupRequestRequestTypeDef, _OptionalUpdateKeyGroupRequestRequestTypeDef
):
    pass

CreateOriginAccessControlRequestRequestTypeDef = TypedDict(
    "CreateOriginAccessControlRequestRequestTypeDef",
    {
        "OriginAccessControlConfig": OriginAccessControlConfigTypeDef,
    },
)

_RequiredUpdateOriginAccessControlRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOriginAccessControlRequestRequestTypeDef",
    {
        "OriginAccessControlConfig": OriginAccessControlConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateOriginAccessControlRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOriginAccessControlRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateOriginAccessControlRequestRequestTypeDef(
    _RequiredUpdateOriginAccessControlRequestRequestTypeDef,
    _OptionalUpdateOriginAccessControlRequestRequestTypeDef,
):
    pass

CreatePublicKeyRequestRequestTypeDef = TypedDict(
    "CreatePublicKeyRequestRequestTypeDef",
    {
        "PublicKeyConfig": PublicKeyConfigTypeDef,
    },
)

_RequiredUpdatePublicKeyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePublicKeyRequestRequestTypeDef",
    {
        "PublicKeyConfig": PublicKeyConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdatePublicKeyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePublicKeyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdatePublicKeyRequestRequestTypeDef(
    _RequiredUpdatePublicKeyRequestRequestTypeDef, _OptionalUpdatePublicKeyRequestRequestTypeDef
):
    pass

_RequiredCustomErrorResponsesOutputTypeDef = TypedDict(
    "_RequiredCustomErrorResponsesOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCustomErrorResponsesOutputTypeDef = TypedDict(
    "_OptionalCustomErrorResponsesOutputTypeDef",
    {
        "Items": List[CustomErrorResponseOutputTypeDef],
    },
    total=False,
)

class CustomErrorResponsesOutputTypeDef(
    _RequiredCustomErrorResponsesOutputTypeDef, _OptionalCustomErrorResponsesOutputTypeDef
):
    pass

_RequiredCustomErrorResponsesTypeDef = TypedDict(
    "_RequiredCustomErrorResponsesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCustomErrorResponsesTypeDef = TypedDict(
    "_OptionalCustomErrorResponsesTypeDef",
    {
        "Items": Sequence[CustomErrorResponseTypeDef],
    },
    total=False,
)

class CustomErrorResponsesTypeDef(
    _RequiredCustomErrorResponsesTypeDef, _OptionalCustomErrorResponsesTypeDef
):
    pass

_RequiredCustomHeadersOutputTypeDef = TypedDict(
    "_RequiredCustomHeadersOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCustomHeadersOutputTypeDef = TypedDict(
    "_OptionalCustomHeadersOutputTypeDef",
    {
        "Items": List[OriginCustomHeaderOutputTypeDef],
    },
    total=False,
)

class CustomHeadersOutputTypeDef(
    _RequiredCustomHeadersOutputTypeDef, _OptionalCustomHeadersOutputTypeDef
):
    pass

_RequiredCustomHeadersTypeDef = TypedDict(
    "_RequiredCustomHeadersTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCustomHeadersTypeDef = TypedDict(
    "_OptionalCustomHeadersTypeDef",
    {
        "Items": Sequence[OriginCustomHeaderTypeDef],
    },
    total=False,
)

class CustomHeadersTypeDef(_RequiredCustomHeadersTypeDef, _OptionalCustomHeadersTypeDef):
    pass

_RequiredCustomOriginConfigOutputTypeDef = TypedDict(
    "_RequiredCustomOriginConfigOutputTypeDef",
    {
        "HTTPPort": int,
        "HTTPSPort": int,
        "OriginProtocolPolicy": OriginProtocolPolicyType,
    },
)
_OptionalCustomOriginConfigOutputTypeDef = TypedDict(
    "_OptionalCustomOriginConfigOutputTypeDef",
    {
        "OriginSslProtocols": OriginSslProtocolsOutputTypeDef,
        "OriginReadTimeout": int,
        "OriginKeepaliveTimeout": int,
    },
    total=False,
)

class CustomOriginConfigOutputTypeDef(
    _RequiredCustomOriginConfigOutputTypeDef, _OptionalCustomOriginConfigOutputTypeDef
):
    pass

_RequiredCustomOriginConfigTypeDef = TypedDict(
    "_RequiredCustomOriginConfigTypeDef",
    {
        "HTTPPort": int,
        "HTTPSPort": int,
        "OriginProtocolPolicy": OriginProtocolPolicyType,
    },
)
_OptionalCustomOriginConfigTypeDef = TypedDict(
    "_OptionalCustomOriginConfigTypeDef",
    {
        "OriginSslProtocols": OriginSslProtocolsTypeDef,
        "OriginReadTimeout": int,
        "OriginKeepaliveTimeout": int,
    },
    total=False,
)

class CustomOriginConfigTypeDef(
    _RequiredCustomOriginConfigTypeDef, _OptionalCustomOriginConfigTypeDef
):
    pass

ListDistributionsByCachePolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByCachePolicyIdResultTypeDef",
    {
        "DistributionIdList": DistributionIdListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByKeyGroupResultTypeDef = TypedDict(
    "ListDistributionsByKeyGroupResultTypeDef",
    {
        "DistributionIdList": DistributionIdListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByOriginRequestPolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    {
        "DistributionIdList": DistributionIdListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByResponseHeadersPolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByResponseHeadersPolicyIdResultTypeDef",
    {
        "DistributionIdList": DistributionIdListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionEntityOutputTypeDef = TypedDict(
    "EncryptionEntityOutputTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": FieldPatternsOutputTypeDef,
    },
)

EncryptionEntityTypeDef = TypedDict(
    "EncryptionEntityTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": FieldPatternsTypeDef,
    },
)

_RequiredEndPointOutputTypeDef = TypedDict(
    "_RequiredEndPointOutputTypeDef",
    {
        "StreamType": str,
    },
)
_OptionalEndPointOutputTypeDef = TypedDict(
    "_OptionalEndPointOutputTypeDef",
    {
        "KinesisStreamConfig": KinesisStreamConfigOutputTypeDef,
    },
    total=False,
)

class EndPointOutputTypeDef(_RequiredEndPointOutputTypeDef, _OptionalEndPointOutputTypeDef):
    pass

_RequiredEndPointTypeDef = TypedDict(
    "_RequiredEndPointTypeDef",
    {
        "StreamType": str,
    },
)
_OptionalEndPointTypeDef = TypedDict(
    "_OptionalEndPointTypeDef",
    {
        "KinesisStreamConfig": KinesisStreamConfigTypeDef,
    },
    total=False,
)

class EndPointTypeDef(_RequiredEndPointTypeDef, _OptionalEndPointTypeDef):
    pass

_RequiredFunctionAssociationsOutputTypeDef = TypedDict(
    "_RequiredFunctionAssociationsOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalFunctionAssociationsOutputTypeDef = TypedDict(
    "_OptionalFunctionAssociationsOutputTypeDef",
    {
        "Items": List[FunctionAssociationOutputTypeDef],
    },
    total=False,
)

class FunctionAssociationsOutputTypeDef(
    _RequiredFunctionAssociationsOutputTypeDef, _OptionalFunctionAssociationsOutputTypeDef
):
    pass

_RequiredFunctionAssociationsTypeDef = TypedDict(
    "_RequiredFunctionAssociationsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalFunctionAssociationsTypeDef = TypedDict(
    "_OptionalFunctionAssociationsTypeDef",
    {
        "Items": Sequence[FunctionAssociationTypeDef],
    },
    total=False,
)

class FunctionAssociationsTypeDef(
    _RequiredFunctionAssociationsTypeDef, _OptionalFunctionAssociationsTypeDef
):
    pass

_RequiredFunctionSummaryTypeDef = TypedDict(
    "_RequiredFunctionSummaryTypeDef",
    {
        "Name": str,
        "FunctionConfig": FunctionConfigOutputTypeDef,
        "FunctionMetadata": FunctionMetadataTypeDef,
    },
)
_OptionalFunctionSummaryTypeDef = TypedDict(
    "_OptionalFunctionSummaryTypeDef",
    {
        "Status": str,
    },
    total=False,
)

class FunctionSummaryTypeDef(_RequiredFunctionSummaryTypeDef, _OptionalFunctionSummaryTypeDef):
    pass

RestrictionsOutputTypeDef = TypedDict(
    "RestrictionsOutputTypeDef",
    {
        "GeoRestriction": GeoRestrictionOutputTypeDef,
    },
)

RestrictionsTypeDef = TypedDict(
    "RestrictionsTypeDef",
    {
        "GeoRestriction": GeoRestrictionTypeDef,
    },
)

_RequiredGetDistributionRequestDistributionDeployedWaitTypeDef = TypedDict(
    "_RequiredGetDistributionRequestDistributionDeployedWaitTypeDef",
    {
        "Id": str,
    },
)
_OptionalGetDistributionRequestDistributionDeployedWaitTypeDef = TypedDict(
    "_OptionalGetDistributionRequestDistributionDeployedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class GetDistributionRequestDistributionDeployedWaitTypeDef(
    _RequiredGetDistributionRequestDistributionDeployedWaitTypeDef,
    _OptionalGetDistributionRequestDistributionDeployedWaitTypeDef,
):
    pass

_RequiredGetInvalidationRequestInvalidationCompletedWaitTypeDef = TypedDict(
    "_RequiredGetInvalidationRequestInvalidationCompletedWaitTypeDef",
    {
        "DistributionId": str,
        "Id": str,
    },
)
_OptionalGetInvalidationRequestInvalidationCompletedWaitTypeDef = TypedDict(
    "_OptionalGetInvalidationRequestInvalidationCompletedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class GetInvalidationRequestInvalidationCompletedWaitTypeDef(
    _RequiredGetInvalidationRequestInvalidationCompletedWaitTypeDef,
    _OptionalGetInvalidationRequestInvalidationCompletedWaitTypeDef,
):
    pass

_RequiredGetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef = TypedDict(
    "_RequiredGetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef",
    {
        "Id": str,
    },
)
_OptionalGetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef = TypedDict(
    "_OptionalGetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class GetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef(
    _RequiredGetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef,
    _OptionalGetStreamingDistributionRequestStreamingDistributionDeployedWaitTypeDef,
):
    pass

GetKeyGroupConfigResultTypeDef = TypedDict(
    "GetKeyGroupConfigResultTypeDef",
    {
        "KeyGroupConfig": KeyGroupConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyGroupTypeDef = TypedDict(
    "KeyGroupTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "KeyGroupConfig": KeyGroupConfigOutputTypeDef,
    },
)

GetOriginAccessControlConfigResultTypeDef = TypedDict(
    "GetOriginAccessControlConfigResultTypeDef",
    {
        "OriginAccessControlConfig": OriginAccessControlConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOriginAccessControlTypeDef = TypedDict(
    "_RequiredOriginAccessControlTypeDef",
    {
        "Id": str,
    },
)
_OptionalOriginAccessControlTypeDef = TypedDict(
    "_OptionalOriginAccessControlTypeDef",
    {
        "OriginAccessControlConfig": OriginAccessControlConfigOutputTypeDef,
    },
    total=False,
)

class OriginAccessControlTypeDef(
    _RequiredOriginAccessControlTypeDef, _OptionalOriginAccessControlTypeDef
):
    pass

GetPublicKeyConfigResultTypeDef = TypedDict(
    "GetPublicKeyConfigResultTypeDef",
    {
        "PublicKeyConfig": PublicKeyConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Id": str,
        "CreatedTime": datetime,
        "PublicKeyConfig": PublicKeyConfigOutputTypeDef,
    },
)

InvalidationBatchOutputTypeDef = TypedDict(
    "InvalidationBatchOutputTypeDef",
    {
        "Paths": PathsOutputTypeDef,
        "CallerReference": str,
    },
)

InvalidationBatchTypeDef = TypedDict(
    "InvalidationBatchTypeDef",
    {
        "Paths": PathsTypeDef,
        "CallerReference": str,
    },
)

_RequiredInvalidationListTypeDef = TypedDict(
    "_RequiredInvalidationListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalInvalidationListTypeDef = TypedDict(
    "_OptionalInvalidationListTypeDef",
    {
        "NextMarker": str,
        "Items": List[InvalidationSummaryTypeDef],
    },
    total=False,
)

class InvalidationListTypeDef(_RequiredInvalidationListTypeDef, _OptionalInvalidationListTypeDef):
    pass

KGKeyPairIdsTypeDef = TypedDict(
    "KGKeyPairIdsTypeDef",
    {
        "KeyGroupId": str,
        "KeyPairIds": KeyPairIdsTypeDef,
    },
    total=False,
)

SignerTypeDef = TypedDict(
    "SignerTypeDef",
    {
        "AwsAccountNumber": str,
        "KeyPairIds": KeyPairIdsTypeDef,
    },
    total=False,
)

_RequiredLambdaFunctionAssociationsOutputTypeDef = TypedDict(
    "_RequiredLambdaFunctionAssociationsOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalLambdaFunctionAssociationsOutputTypeDef = TypedDict(
    "_OptionalLambdaFunctionAssociationsOutputTypeDef",
    {
        "Items": List[LambdaFunctionAssociationOutputTypeDef],
    },
    total=False,
)

class LambdaFunctionAssociationsOutputTypeDef(
    _RequiredLambdaFunctionAssociationsOutputTypeDef,
    _OptionalLambdaFunctionAssociationsOutputTypeDef,
):
    pass

_RequiredLambdaFunctionAssociationsTypeDef = TypedDict(
    "_RequiredLambdaFunctionAssociationsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalLambdaFunctionAssociationsTypeDef = TypedDict(
    "_OptionalLambdaFunctionAssociationsTypeDef",
    {
        "Items": Sequence[LambdaFunctionAssociationTypeDef],
    },
    total=False,
)

class LambdaFunctionAssociationsTypeDef(
    _RequiredLambdaFunctionAssociationsTypeDef, _OptionalLambdaFunctionAssociationsTypeDef
):
    pass

MonitoringSubscriptionOutputTypeDef = TypedDict(
    "MonitoringSubscriptionOutputTypeDef",
    {
        "RealtimeMetricsSubscriptionConfig": RealtimeMetricsSubscriptionConfigOutputTypeDef,
    },
    total=False,
)

MonitoringSubscriptionTypeDef = TypedDict(
    "MonitoringSubscriptionTypeDef",
    {
        "RealtimeMetricsSubscriptionConfig": RealtimeMetricsSubscriptionConfigTypeDef,
    },
    total=False,
)

_RequiredOriginAccessControlListTypeDef = TypedDict(
    "_RequiredOriginAccessControlListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalOriginAccessControlListTypeDef = TypedDict(
    "_OptionalOriginAccessControlListTypeDef",
    {
        "NextMarker": str,
        "Items": List[OriginAccessControlSummaryTypeDef],
    },
    total=False,
)

class OriginAccessControlListTypeDef(
    _RequiredOriginAccessControlListTypeDef, _OptionalOriginAccessControlListTypeDef
):
    pass

OriginGroupFailoverCriteriaOutputTypeDef = TypedDict(
    "OriginGroupFailoverCriteriaOutputTypeDef",
    {
        "StatusCodes": StatusCodesOutputTypeDef,
    },
)

OriginGroupFailoverCriteriaTypeDef = TypedDict(
    "OriginGroupFailoverCriteriaTypeDef",
    {
        "StatusCodes": StatusCodesTypeDef,
    },
)

OriginGroupMembersOutputTypeDef = TypedDict(
    "OriginGroupMembersOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[OriginGroupMemberOutputTypeDef],
    },
)

OriginGroupMembersTypeDef = TypedDict(
    "OriginGroupMembersTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[OriginGroupMemberTypeDef],
    },
)

_RequiredPublicKeyListTypeDef = TypedDict(
    "_RequiredPublicKeyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalPublicKeyListTypeDef = TypedDict(
    "_OptionalPublicKeyListTypeDef",
    {
        "NextMarker": str,
        "Items": List[PublicKeySummaryTypeDef],
    },
    total=False,
)

class PublicKeyListTypeDef(_RequiredPublicKeyListTypeDef, _OptionalPublicKeyListTypeDef):
    pass

_RequiredQueryArgProfilesOutputTypeDef = TypedDict(
    "_RequiredQueryArgProfilesOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryArgProfilesOutputTypeDef = TypedDict(
    "_OptionalQueryArgProfilesOutputTypeDef",
    {
        "Items": List[QueryArgProfileOutputTypeDef],
    },
    total=False,
)

class QueryArgProfilesOutputTypeDef(
    _RequiredQueryArgProfilesOutputTypeDef, _OptionalQueryArgProfilesOutputTypeDef
):
    pass

_RequiredQueryArgProfilesTypeDef = TypedDict(
    "_RequiredQueryArgProfilesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryArgProfilesTypeDef = TypedDict(
    "_OptionalQueryArgProfilesTypeDef",
    {
        "Items": Sequence[QueryArgProfileTypeDef],
    },
    total=False,
)

class QueryArgProfilesTypeDef(_RequiredQueryArgProfilesTypeDef, _OptionalQueryArgProfilesTypeDef):
    pass

_RequiredResponseHeadersPolicyCorsConfigOutputTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyCorsConfigOutputTypeDef",
    {
        "AccessControlAllowOrigins": ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef,
        "AccessControlAllowHeaders": ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef,
        "AccessControlAllowMethods": ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef,
        "AccessControlAllowCredentials": bool,
        "OriginOverride": bool,
    },
)
_OptionalResponseHeadersPolicyCorsConfigOutputTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyCorsConfigOutputTypeDef",
    {
        "AccessControlExposeHeaders": ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef,
        "AccessControlMaxAgeSec": int,
    },
    total=False,
)

class ResponseHeadersPolicyCorsConfigOutputTypeDef(
    _RequiredResponseHeadersPolicyCorsConfigOutputTypeDef,
    _OptionalResponseHeadersPolicyCorsConfigOutputTypeDef,
):
    pass

_RequiredResponseHeadersPolicyCorsConfigTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyCorsConfigTypeDef",
    {
        "AccessControlAllowOrigins": ResponseHeadersPolicyAccessControlAllowOriginsTypeDef,
        "AccessControlAllowHeaders": ResponseHeadersPolicyAccessControlAllowHeadersTypeDef,
        "AccessControlAllowMethods": ResponseHeadersPolicyAccessControlAllowMethodsTypeDef,
        "AccessControlAllowCredentials": bool,
        "OriginOverride": bool,
    },
)
_OptionalResponseHeadersPolicyCorsConfigTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyCorsConfigTypeDef",
    {
        "AccessControlExposeHeaders": ResponseHeadersPolicyAccessControlExposeHeadersTypeDef,
        "AccessControlMaxAgeSec": int,
    },
    total=False,
)

class ResponseHeadersPolicyCorsConfigTypeDef(
    _RequiredResponseHeadersPolicyCorsConfigTypeDef, _OptionalResponseHeadersPolicyCorsConfigTypeDef
):
    pass

_RequiredResponseHeadersPolicyCustomHeadersConfigOutputTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyCustomHeadersConfigOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalResponseHeadersPolicyCustomHeadersConfigOutputTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyCustomHeadersConfigOutputTypeDef",
    {
        "Items": List[ResponseHeadersPolicyCustomHeaderOutputTypeDef],
    },
    total=False,
)

class ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef(
    _RequiredResponseHeadersPolicyCustomHeadersConfigOutputTypeDef,
    _OptionalResponseHeadersPolicyCustomHeadersConfigOutputTypeDef,
):
    pass

_RequiredResponseHeadersPolicyCustomHeadersConfigTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyCustomHeadersConfigTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalResponseHeadersPolicyCustomHeadersConfigTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyCustomHeadersConfigTypeDef",
    {
        "Items": Sequence[ResponseHeadersPolicyCustomHeaderTypeDef],
    },
    total=False,
)

class ResponseHeadersPolicyCustomHeadersConfigTypeDef(
    _RequiredResponseHeadersPolicyCustomHeadersConfigTypeDef,
    _OptionalResponseHeadersPolicyCustomHeadersConfigTypeDef,
):
    pass

_RequiredResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef",
    {
        "Items": List[ResponseHeadersPolicyRemoveHeaderOutputTypeDef],
    },
    total=False,
)

class ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef(
    _RequiredResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef,
    _OptionalResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef,
):
    pass

_RequiredResponseHeadersPolicyRemoveHeadersConfigTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyRemoveHeadersConfigTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalResponseHeadersPolicyRemoveHeadersConfigTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyRemoveHeadersConfigTypeDef",
    {
        "Items": Sequence[ResponseHeadersPolicyRemoveHeaderTypeDef],
    },
    total=False,
)

class ResponseHeadersPolicyRemoveHeadersConfigTypeDef(
    _RequiredResponseHeadersPolicyRemoveHeadersConfigTypeDef,
    _OptionalResponseHeadersPolicyRemoveHeadersConfigTypeDef,
):
    pass

ResponseHeadersPolicySecurityHeadersConfigOutputTypeDef = TypedDict(
    "ResponseHeadersPolicySecurityHeadersConfigOutputTypeDef",
    {
        "XSSProtection": ResponseHeadersPolicyXSSProtectionOutputTypeDef,
        "FrameOptions": ResponseHeadersPolicyFrameOptionsOutputTypeDef,
        "ReferrerPolicy": ResponseHeadersPolicyReferrerPolicyOutputTypeDef,
        "ContentSecurityPolicy": ResponseHeadersPolicyContentSecurityPolicyOutputTypeDef,
        "ContentTypeOptions": ResponseHeadersPolicyContentTypeOptionsOutputTypeDef,
        "StrictTransportSecurity": ResponseHeadersPolicyStrictTransportSecurityOutputTypeDef,
    },
    total=False,
)

ResponseHeadersPolicySecurityHeadersConfigTypeDef = TypedDict(
    "ResponseHeadersPolicySecurityHeadersConfigTypeDef",
    {
        "XSSProtection": ResponseHeadersPolicyXSSProtectionTypeDef,
        "FrameOptions": ResponseHeadersPolicyFrameOptionsTypeDef,
        "ReferrerPolicy": ResponseHeadersPolicyReferrerPolicyTypeDef,
        "ContentSecurityPolicy": ResponseHeadersPolicyContentSecurityPolicyTypeDef,
        "ContentTypeOptions": ResponseHeadersPolicyContentTypeOptionsTypeDef,
        "StrictTransportSecurity": ResponseHeadersPolicyStrictTransportSecurityTypeDef,
    },
    total=False,
)

StreamingDistributionSummaryTypeDef = TypedDict(
    "StreamingDistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "S3Origin": S3OriginOutputTypeDef,
        "Aliases": AliasesOutputTypeDef,
        "TrustedSigners": TrustedSignersOutputTypeDef,
        "Comment": str,
        "PriceClass": PriceClassType,
        "Enabled": bool,
    },
)

_RequiredStreamingDistributionConfigOutputTypeDef = TypedDict(
    "_RequiredStreamingDistributionConfigOutputTypeDef",
    {
        "CallerReference": str,
        "S3Origin": S3OriginOutputTypeDef,
        "Comment": str,
        "TrustedSigners": TrustedSignersOutputTypeDef,
        "Enabled": bool,
    },
)
_OptionalStreamingDistributionConfigOutputTypeDef = TypedDict(
    "_OptionalStreamingDistributionConfigOutputTypeDef",
    {
        "Aliases": AliasesOutputTypeDef,
        "Logging": StreamingLoggingConfigOutputTypeDef,
        "PriceClass": PriceClassType,
    },
    total=False,
)

class StreamingDistributionConfigOutputTypeDef(
    _RequiredStreamingDistributionConfigOutputTypeDef,
    _OptionalStreamingDistributionConfigOutputTypeDef,
):
    pass

_RequiredStreamingDistributionConfigTypeDef = TypedDict(
    "_RequiredStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": S3OriginTypeDef,
        "Comment": str,
        "TrustedSigners": TrustedSignersTypeDef,
        "Enabled": bool,
    },
)
_OptionalStreamingDistributionConfigTypeDef = TypedDict(
    "_OptionalStreamingDistributionConfigTypeDef",
    {
        "Aliases": AliasesTypeDef,
        "Logging": StreamingLoggingConfigTypeDef,
        "PriceClass": PriceClassType,
    },
    total=False,
)

class StreamingDistributionConfigTypeDef(
    _RequiredStreamingDistributionConfigTypeDef, _OptionalStreamingDistributionConfigTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": TagKeysTypeDef,
    },
)

TagsOutputTypeDef = TypedDict(
    "TagsOutputTypeDef",
    {
        "Items": List[TagOutputTypeDef],
    },
    total=False,
)

TagsTypeDef = TypedDict(
    "TagsTypeDef",
    {
        "Items": Sequence[TagTypeDef],
    },
    total=False,
)

_RequiredForwardedValuesOutputTypeDef = TypedDict(
    "_RequiredForwardedValuesOutputTypeDef",
    {
        "QueryString": bool,
        "Cookies": CookiePreferenceOutputTypeDef,
    },
)
_OptionalForwardedValuesOutputTypeDef = TypedDict(
    "_OptionalForwardedValuesOutputTypeDef",
    {
        "Headers": HeadersOutputTypeDef,
        "QueryStringCacheKeys": QueryStringCacheKeysOutputTypeDef,
    },
    total=False,
)

class ForwardedValuesOutputTypeDef(
    _RequiredForwardedValuesOutputTypeDef, _OptionalForwardedValuesOutputTypeDef
):
    pass

_RequiredForwardedValuesTypeDef = TypedDict(
    "_RequiredForwardedValuesTypeDef",
    {
        "QueryString": bool,
        "Cookies": CookiePreferenceTypeDef,
    },
)
_OptionalForwardedValuesTypeDef = TypedDict(
    "_OptionalForwardedValuesTypeDef",
    {
        "Headers": HeadersTypeDef,
        "QueryStringCacheKeys": QueryStringCacheKeysTypeDef,
    },
    total=False,
)

class ForwardedValuesTypeDef(_RequiredForwardedValuesTypeDef, _OptionalForwardedValuesTypeDef):
    pass

_RequiredParametersInCacheKeyAndForwardedToOriginOutputTypeDef = TypedDict(
    "_RequiredParametersInCacheKeyAndForwardedToOriginOutputTypeDef",
    {
        "EnableAcceptEncodingGzip": bool,
        "HeadersConfig": CachePolicyHeadersConfigOutputTypeDef,
        "CookiesConfig": CachePolicyCookiesConfigOutputTypeDef,
        "QueryStringsConfig": CachePolicyQueryStringsConfigOutputTypeDef,
    },
)
_OptionalParametersInCacheKeyAndForwardedToOriginOutputTypeDef = TypedDict(
    "_OptionalParametersInCacheKeyAndForwardedToOriginOutputTypeDef",
    {
        "EnableAcceptEncodingBrotli": bool,
    },
    total=False,
)

class ParametersInCacheKeyAndForwardedToOriginOutputTypeDef(
    _RequiredParametersInCacheKeyAndForwardedToOriginOutputTypeDef,
    _OptionalParametersInCacheKeyAndForwardedToOriginOutputTypeDef,
):
    pass

_RequiredOriginRequestPolicyConfigOutputTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyConfigOutputTypeDef",
    {
        "Name": str,
        "HeadersConfig": OriginRequestPolicyHeadersConfigOutputTypeDef,
        "CookiesConfig": OriginRequestPolicyCookiesConfigOutputTypeDef,
        "QueryStringsConfig": OriginRequestPolicyQueryStringsConfigOutputTypeDef,
    },
)
_OptionalOriginRequestPolicyConfigOutputTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyConfigOutputTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class OriginRequestPolicyConfigOutputTypeDef(
    _RequiredOriginRequestPolicyConfigOutputTypeDef, _OptionalOriginRequestPolicyConfigOutputTypeDef
):
    pass

_RequiredParametersInCacheKeyAndForwardedToOriginTypeDef = TypedDict(
    "_RequiredParametersInCacheKeyAndForwardedToOriginTypeDef",
    {
        "EnableAcceptEncodingGzip": bool,
        "HeadersConfig": CachePolicyHeadersConfigTypeDef,
        "CookiesConfig": CachePolicyCookiesConfigTypeDef,
        "QueryStringsConfig": CachePolicyQueryStringsConfigTypeDef,
    },
)
_OptionalParametersInCacheKeyAndForwardedToOriginTypeDef = TypedDict(
    "_OptionalParametersInCacheKeyAndForwardedToOriginTypeDef",
    {
        "EnableAcceptEncodingBrotli": bool,
    },
    total=False,
)

class ParametersInCacheKeyAndForwardedToOriginTypeDef(
    _RequiredParametersInCacheKeyAndForwardedToOriginTypeDef,
    _OptionalParametersInCacheKeyAndForwardedToOriginTypeDef,
):
    pass

_RequiredOriginRequestPolicyConfigTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyConfigTypeDef",
    {
        "Name": str,
        "HeadersConfig": OriginRequestPolicyHeadersConfigTypeDef,
        "CookiesConfig": OriginRequestPolicyCookiesConfigTypeDef,
        "QueryStringsConfig": OriginRequestPolicyQueryStringsConfigTypeDef,
    },
)
_OptionalOriginRequestPolicyConfigTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyConfigTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class OriginRequestPolicyConfigTypeDef(
    _RequiredOriginRequestPolicyConfigTypeDef, _OptionalOriginRequestPolicyConfigTypeDef
):
    pass

CreateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": CloudFrontOriginAccessIdentityTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCloudFrontOriginAccessIdentitiesResultTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityList": CloudFrontOriginAccessIdentityListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConflictingAliasesResultTypeDef = TypedDict(
    "ListConflictingAliasesResultTypeDef",
    {
        "ConflictingAliasesList": ConflictingAliasesListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredContentTypeProfileConfigOutputTypeDef = TypedDict(
    "_RequiredContentTypeProfileConfigOutputTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
    },
)
_OptionalContentTypeProfileConfigOutputTypeDef = TypedDict(
    "_OptionalContentTypeProfileConfigOutputTypeDef",
    {
        "ContentTypeProfiles": ContentTypeProfilesOutputTypeDef,
    },
    total=False,
)

class ContentTypeProfileConfigOutputTypeDef(
    _RequiredContentTypeProfileConfigOutputTypeDef, _OptionalContentTypeProfileConfigOutputTypeDef
):
    pass

_RequiredContentTypeProfileConfigTypeDef = TypedDict(
    "_RequiredContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
    },
)
_OptionalContentTypeProfileConfigTypeDef = TypedDict(
    "_OptionalContentTypeProfileConfigTypeDef",
    {
        "ContentTypeProfiles": ContentTypeProfilesTypeDef,
    },
    total=False,
)

class ContentTypeProfileConfigTypeDef(
    _RequiredContentTypeProfileConfigTypeDef, _OptionalContentTypeProfileConfigTypeDef
):
    pass

_RequiredTrafficConfigOutputTypeDef = TypedDict(
    "_RequiredTrafficConfigOutputTypeDef",
    {
        "Type": ContinuousDeploymentPolicyTypeType,
    },
)
_OptionalTrafficConfigOutputTypeDef = TypedDict(
    "_OptionalTrafficConfigOutputTypeDef",
    {
        "SingleWeightConfig": ContinuousDeploymentSingleWeightConfigOutputTypeDef,
        "SingleHeaderConfig": ContinuousDeploymentSingleHeaderConfigOutputTypeDef,
    },
    total=False,
)

class TrafficConfigOutputTypeDef(
    _RequiredTrafficConfigOutputTypeDef, _OptionalTrafficConfigOutputTypeDef
):
    pass

_RequiredTrafficConfigTypeDef = TypedDict(
    "_RequiredTrafficConfigTypeDef",
    {
        "Type": ContinuousDeploymentPolicyTypeType,
    },
)
_OptionalTrafficConfigTypeDef = TypedDict(
    "_OptionalTrafficConfigTypeDef",
    {
        "SingleWeightConfig": ContinuousDeploymentSingleWeightConfigTypeDef,
        "SingleHeaderConfig": ContinuousDeploymentSingleHeaderConfigTypeDef,
    },
    total=False,
)

class TrafficConfigTypeDef(_RequiredTrafficConfigTypeDef, _OptionalTrafficConfigTypeDef):
    pass

_RequiredOriginOutputTypeDef = TypedDict(
    "_RequiredOriginOutputTypeDef",
    {
        "Id": str,
        "DomainName": str,
    },
)
_OptionalOriginOutputTypeDef = TypedDict(
    "_OptionalOriginOutputTypeDef",
    {
        "OriginPath": str,
        "CustomHeaders": CustomHeadersOutputTypeDef,
        "S3OriginConfig": S3OriginConfigOutputTypeDef,
        "CustomOriginConfig": CustomOriginConfigOutputTypeDef,
        "ConnectionAttempts": int,
        "ConnectionTimeout": int,
        "OriginShield": OriginShieldOutputTypeDef,
        "OriginAccessControlId": str,
    },
    total=False,
)

class OriginOutputTypeDef(_RequiredOriginOutputTypeDef, _OptionalOriginOutputTypeDef):
    pass

_RequiredOriginTypeDef = TypedDict(
    "_RequiredOriginTypeDef",
    {
        "Id": str,
        "DomainName": str,
    },
)
_OptionalOriginTypeDef = TypedDict(
    "_OptionalOriginTypeDef",
    {
        "OriginPath": str,
        "CustomHeaders": CustomHeadersTypeDef,
        "S3OriginConfig": S3OriginConfigTypeDef,
        "CustomOriginConfig": CustomOriginConfigTypeDef,
        "ConnectionAttempts": int,
        "ConnectionTimeout": int,
        "OriginShield": OriginShieldTypeDef,
        "OriginAccessControlId": str,
    },
    total=False,
)

class OriginTypeDef(_RequiredOriginTypeDef, _OptionalOriginTypeDef):
    pass

_RequiredEncryptionEntitiesOutputTypeDef = TypedDict(
    "_RequiredEncryptionEntitiesOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalEncryptionEntitiesOutputTypeDef = TypedDict(
    "_OptionalEncryptionEntitiesOutputTypeDef",
    {
        "Items": List[EncryptionEntityOutputTypeDef],
    },
    total=False,
)

class EncryptionEntitiesOutputTypeDef(
    _RequiredEncryptionEntitiesOutputTypeDef, _OptionalEncryptionEntitiesOutputTypeDef
):
    pass

_RequiredEncryptionEntitiesTypeDef = TypedDict(
    "_RequiredEncryptionEntitiesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalEncryptionEntitiesTypeDef = TypedDict(
    "_OptionalEncryptionEntitiesTypeDef",
    {
        "Items": Sequence[EncryptionEntityTypeDef],
    },
    total=False,
)

class EncryptionEntitiesTypeDef(
    _RequiredEncryptionEntitiesTypeDef, _OptionalEncryptionEntitiesTypeDef
):
    pass

RealtimeLogConfigTypeDef = TypedDict(
    "RealtimeLogConfigTypeDef",
    {
        "ARN": str,
        "Name": str,
        "SamplingRate": int,
        "EndPoints": List[EndPointOutputTypeDef],
        "Fields": List[str],
    },
)

CreateRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "CreateRealtimeLogConfigRequestRequestTypeDef",
    {
        "EndPoints": Sequence[EndPointTypeDef],
        "Fields": Sequence[str],
        "Name": str,
        "SamplingRate": int,
    },
)

UpdateRealtimeLogConfigRequestRequestTypeDef = TypedDict(
    "UpdateRealtimeLogConfigRequestRequestTypeDef",
    {
        "EndPoints": Sequence[EndPointTypeDef],
        "Fields": Sequence[str],
        "Name": str,
        "ARN": str,
        "SamplingRate": int,
    },
    total=False,
)

CreateFunctionResultTypeDef = TypedDict(
    "CreateFunctionResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFunctionResultTypeDef = TypedDict(
    "DescribeFunctionResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFunctionListTypeDef = TypedDict(
    "_RequiredFunctionListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalFunctionListTypeDef = TypedDict(
    "_OptionalFunctionListTypeDef",
    {
        "NextMarker": str,
        "Items": List[FunctionSummaryTypeDef],
    },
    total=False,
)

class FunctionListTypeDef(_RequiredFunctionListTypeDef, _OptionalFunctionListTypeDef):
    pass

PublishFunctionResultTypeDef = TypedDict(
    "PublishFunctionResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestResultTypeDef = TypedDict(
    "TestResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "ComputeUtilization": str,
        "FunctionExecutionLogs": List[str],
        "FunctionErrorMessage": str,
        "FunctionOutput": str,
    },
    total=False,
)

UpdateFunctionResultTypeDef = TypedDict(
    "UpdateFunctionResultTypeDef",
    {
        "FunctionSummary": FunctionSummaryTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyGroupResultTypeDef = TypedDict(
    "CreateKeyGroupResultTypeDef",
    {
        "KeyGroup": KeyGroupTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyGroupResultTypeDef = TypedDict(
    "GetKeyGroupResultTypeDef",
    {
        "KeyGroup": KeyGroupTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyGroupSummaryTypeDef = TypedDict(
    "KeyGroupSummaryTypeDef",
    {
        "KeyGroup": KeyGroupTypeDef,
    },
)

UpdateKeyGroupResultTypeDef = TypedDict(
    "UpdateKeyGroupResultTypeDef",
    {
        "KeyGroup": KeyGroupTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOriginAccessControlResultTypeDef = TypedDict(
    "CreateOriginAccessControlResultTypeDef",
    {
        "OriginAccessControl": OriginAccessControlTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOriginAccessControlResultTypeDef = TypedDict(
    "GetOriginAccessControlResultTypeDef",
    {
        "OriginAccessControl": OriginAccessControlTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateOriginAccessControlResultTypeDef = TypedDict(
    "UpdateOriginAccessControlResultTypeDef",
    {
        "OriginAccessControl": OriginAccessControlTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePublicKeyResultTypeDef = TypedDict(
    "CreatePublicKeyResultTypeDef",
    {
        "PublicKey": PublicKeyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicKeyResultTypeDef = TypedDict(
    "GetPublicKeyResultTypeDef",
    {
        "PublicKey": PublicKeyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePublicKeyResultTypeDef = TypedDict(
    "UpdatePublicKeyResultTypeDef",
    {
        "PublicKey": PublicKeyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvalidationTypeDef = TypedDict(
    "InvalidationTypeDef",
    {
        "Id": str,
        "Status": str,
        "CreateTime": datetime,
        "InvalidationBatch": InvalidationBatchOutputTypeDef,
    },
)

CreateInvalidationRequestRequestTypeDef = TypedDict(
    "CreateInvalidationRequestRequestTypeDef",
    {
        "DistributionId": str,
        "InvalidationBatch": InvalidationBatchTypeDef,
    },
)

ListInvalidationsResultTypeDef = TypedDict(
    "ListInvalidationsResultTypeDef",
    {
        "InvalidationList": InvalidationListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredActiveTrustedKeyGroupsTypeDef = TypedDict(
    "_RequiredActiveTrustedKeyGroupsTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalActiveTrustedKeyGroupsTypeDef = TypedDict(
    "_OptionalActiveTrustedKeyGroupsTypeDef",
    {
        "Items": List[KGKeyPairIdsTypeDef],
    },
    total=False,
)

class ActiveTrustedKeyGroupsTypeDef(
    _RequiredActiveTrustedKeyGroupsTypeDef, _OptionalActiveTrustedKeyGroupsTypeDef
):
    pass

_RequiredActiveTrustedSignersTypeDef = TypedDict(
    "_RequiredActiveTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalActiveTrustedSignersTypeDef = TypedDict(
    "_OptionalActiveTrustedSignersTypeDef",
    {
        "Items": List[SignerTypeDef],
    },
    total=False,
)

class ActiveTrustedSignersTypeDef(
    _RequiredActiveTrustedSignersTypeDef, _OptionalActiveTrustedSignersTypeDef
):
    pass

CreateMonitoringSubscriptionResultTypeDef = TypedDict(
    "CreateMonitoringSubscriptionResultTypeDef",
    {
        "MonitoringSubscription": MonitoringSubscriptionOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMonitoringSubscriptionResultTypeDef = TypedDict(
    "GetMonitoringSubscriptionResultTypeDef",
    {
        "MonitoringSubscription": MonitoringSubscriptionOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMonitoringSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateMonitoringSubscriptionRequestRequestTypeDef",
    {
        "DistributionId": str,
        "MonitoringSubscription": MonitoringSubscriptionTypeDef,
    },
)

ListOriginAccessControlsResultTypeDef = TypedDict(
    "ListOriginAccessControlsResultTypeDef",
    {
        "OriginAccessControlList": OriginAccessControlListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OriginGroupOutputTypeDef = TypedDict(
    "OriginGroupOutputTypeDef",
    {
        "Id": str,
        "FailoverCriteria": OriginGroupFailoverCriteriaOutputTypeDef,
        "Members": OriginGroupMembersOutputTypeDef,
    },
)

OriginGroupTypeDef = TypedDict(
    "OriginGroupTypeDef",
    {
        "Id": str,
        "FailoverCriteria": OriginGroupFailoverCriteriaTypeDef,
        "Members": OriginGroupMembersTypeDef,
    },
)

ListPublicKeysResultTypeDef = TypedDict(
    "ListPublicKeysResultTypeDef",
    {
        "PublicKeyList": PublicKeyListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredQueryArgProfileConfigOutputTypeDef = TypedDict(
    "_RequiredQueryArgProfileConfigOutputTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
    },
)
_OptionalQueryArgProfileConfigOutputTypeDef = TypedDict(
    "_OptionalQueryArgProfileConfigOutputTypeDef",
    {
        "QueryArgProfiles": QueryArgProfilesOutputTypeDef,
    },
    total=False,
)

class QueryArgProfileConfigOutputTypeDef(
    _RequiredQueryArgProfileConfigOutputTypeDef, _OptionalQueryArgProfileConfigOutputTypeDef
):
    pass

_RequiredQueryArgProfileConfigTypeDef = TypedDict(
    "_RequiredQueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
    },
)
_OptionalQueryArgProfileConfigTypeDef = TypedDict(
    "_OptionalQueryArgProfileConfigTypeDef",
    {
        "QueryArgProfiles": QueryArgProfilesTypeDef,
    },
    total=False,
)

class QueryArgProfileConfigTypeDef(
    _RequiredQueryArgProfileConfigTypeDef, _OptionalQueryArgProfileConfigTypeDef
):
    pass

_RequiredResponseHeadersPolicyConfigOutputTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyConfigOutputTypeDef",
    {
        "Name": str,
    },
)
_OptionalResponseHeadersPolicyConfigOutputTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyConfigOutputTypeDef",
    {
        "Comment": str,
        "CorsConfig": ResponseHeadersPolicyCorsConfigOutputTypeDef,
        "SecurityHeadersConfig": ResponseHeadersPolicySecurityHeadersConfigOutputTypeDef,
        "ServerTimingHeadersConfig": ResponseHeadersPolicyServerTimingHeadersConfigOutputTypeDef,
        "CustomHeadersConfig": ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef,
        "RemoveHeadersConfig": ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef,
    },
    total=False,
)

class ResponseHeadersPolicyConfigOutputTypeDef(
    _RequiredResponseHeadersPolicyConfigOutputTypeDef,
    _OptionalResponseHeadersPolicyConfigOutputTypeDef,
):
    pass

_RequiredResponseHeadersPolicyConfigTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyConfigTypeDef",
    {
        "Name": str,
    },
)
_OptionalResponseHeadersPolicyConfigTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyConfigTypeDef",
    {
        "Comment": str,
        "CorsConfig": ResponseHeadersPolicyCorsConfigTypeDef,
        "SecurityHeadersConfig": ResponseHeadersPolicySecurityHeadersConfigTypeDef,
        "ServerTimingHeadersConfig": ResponseHeadersPolicyServerTimingHeadersConfigTypeDef,
        "CustomHeadersConfig": ResponseHeadersPolicyCustomHeadersConfigTypeDef,
        "RemoveHeadersConfig": ResponseHeadersPolicyRemoveHeadersConfigTypeDef,
    },
    total=False,
)

class ResponseHeadersPolicyConfigTypeDef(
    _RequiredResponseHeadersPolicyConfigTypeDef, _OptionalResponseHeadersPolicyConfigTypeDef
):
    pass

_RequiredStreamingDistributionListTypeDef = TypedDict(
    "_RequiredStreamingDistributionListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalStreamingDistributionListTypeDef = TypedDict(
    "_OptionalStreamingDistributionListTypeDef",
    {
        "NextMarker": str,
        "Items": List[StreamingDistributionSummaryTypeDef],
    },
    total=False,
)

class StreamingDistributionListTypeDef(
    _RequiredStreamingDistributionListTypeDef, _OptionalStreamingDistributionListTypeDef
):
    pass

GetStreamingDistributionConfigResultTypeDef = TypedDict(
    "GetStreamingDistributionConfigResultTypeDef",
    {
        "StreamingDistributionConfig": StreamingDistributionConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingDistributionRequestRequestTypeDef = TypedDict(
    "CreateStreamingDistributionRequestRequestTypeDef",
    {
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
    },
)

_RequiredUpdateStreamingDistributionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamingDistributionRequestRequestTypeDef",
    {
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateStreamingDistributionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamingDistributionRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateStreamingDistributionRequestRequestTypeDef(
    _RequiredUpdateStreamingDistributionRequestRequestTypeDef,
    _OptionalUpdateStreamingDistributionRequestRequestTypeDef,
):
    pass

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": TagsOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StreamingDistributionConfigWithTagsTypeDef = TypedDict(
    "StreamingDistributionConfigWithTagsTypeDef",
    {
        "StreamingDistributionConfig": StreamingDistributionConfigTypeDef,
        "Tags": TagsTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "Tags": TagsTypeDef,
    },
)

_RequiredCacheBehaviorOutputTypeDef = TypedDict(
    "_RequiredCacheBehaviorOutputTypeDef",
    {
        "PathPattern": str,
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
    },
)
_OptionalCacheBehaviorOutputTypeDef = TypedDict(
    "_OptionalCacheBehaviorOutputTypeDef",
    {
        "TrustedSigners": TrustedSignersOutputTypeDef,
        "TrustedKeyGroups": TrustedKeyGroupsOutputTypeDef,
        "AllowedMethods": AllowedMethodsOutputTypeDef,
        "SmoothStreaming": bool,
        "Compress": bool,
        "LambdaFunctionAssociations": LambdaFunctionAssociationsOutputTypeDef,
        "FunctionAssociations": FunctionAssociationsOutputTypeDef,
        "FieldLevelEncryptionId": str,
        "RealtimeLogConfigArn": str,
        "CachePolicyId": str,
        "OriginRequestPolicyId": str,
        "ResponseHeadersPolicyId": str,
        "ForwardedValues": ForwardedValuesOutputTypeDef,
        "MinTTL": int,
        "DefaultTTL": int,
        "MaxTTL": int,
    },
    total=False,
)

class CacheBehaviorOutputTypeDef(
    _RequiredCacheBehaviorOutputTypeDef, _OptionalCacheBehaviorOutputTypeDef
):
    pass

_RequiredDefaultCacheBehaviorOutputTypeDef = TypedDict(
    "_RequiredDefaultCacheBehaviorOutputTypeDef",
    {
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
    },
)
_OptionalDefaultCacheBehaviorOutputTypeDef = TypedDict(
    "_OptionalDefaultCacheBehaviorOutputTypeDef",
    {
        "TrustedSigners": TrustedSignersOutputTypeDef,
        "TrustedKeyGroups": TrustedKeyGroupsOutputTypeDef,
        "AllowedMethods": AllowedMethodsOutputTypeDef,
        "SmoothStreaming": bool,
        "Compress": bool,
        "LambdaFunctionAssociations": LambdaFunctionAssociationsOutputTypeDef,
        "FunctionAssociations": FunctionAssociationsOutputTypeDef,
        "FieldLevelEncryptionId": str,
        "RealtimeLogConfigArn": str,
        "CachePolicyId": str,
        "OriginRequestPolicyId": str,
        "ResponseHeadersPolicyId": str,
        "ForwardedValues": ForwardedValuesOutputTypeDef,
        "MinTTL": int,
        "DefaultTTL": int,
        "MaxTTL": int,
    },
    total=False,
)

class DefaultCacheBehaviorOutputTypeDef(
    _RequiredDefaultCacheBehaviorOutputTypeDef, _OptionalDefaultCacheBehaviorOutputTypeDef
):
    pass

_RequiredCacheBehaviorTypeDef = TypedDict(
    "_RequiredCacheBehaviorTypeDef",
    {
        "PathPattern": str,
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
    },
)
_OptionalCacheBehaviorTypeDef = TypedDict(
    "_OptionalCacheBehaviorTypeDef",
    {
        "TrustedSigners": TrustedSignersTypeDef,
        "TrustedKeyGroups": TrustedKeyGroupsTypeDef,
        "AllowedMethods": AllowedMethodsTypeDef,
        "SmoothStreaming": bool,
        "Compress": bool,
        "LambdaFunctionAssociations": LambdaFunctionAssociationsTypeDef,
        "FunctionAssociations": FunctionAssociationsTypeDef,
        "FieldLevelEncryptionId": str,
        "RealtimeLogConfigArn": str,
        "CachePolicyId": str,
        "OriginRequestPolicyId": str,
        "ResponseHeadersPolicyId": str,
        "ForwardedValues": ForwardedValuesTypeDef,
        "MinTTL": int,
        "DefaultTTL": int,
        "MaxTTL": int,
    },
    total=False,
)

class CacheBehaviorTypeDef(_RequiredCacheBehaviorTypeDef, _OptionalCacheBehaviorTypeDef):
    pass

_RequiredDefaultCacheBehaviorTypeDef = TypedDict(
    "_RequiredDefaultCacheBehaviorTypeDef",
    {
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
    },
)
_OptionalDefaultCacheBehaviorTypeDef = TypedDict(
    "_OptionalDefaultCacheBehaviorTypeDef",
    {
        "TrustedSigners": TrustedSignersTypeDef,
        "TrustedKeyGroups": TrustedKeyGroupsTypeDef,
        "AllowedMethods": AllowedMethodsTypeDef,
        "SmoothStreaming": bool,
        "Compress": bool,
        "LambdaFunctionAssociations": LambdaFunctionAssociationsTypeDef,
        "FunctionAssociations": FunctionAssociationsTypeDef,
        "FieldLevelEncryptionId": str,
        "RealtimeLogConfigArn": str,
        "CachePolicyId": str,
        "OriginRequestPolicyId": str,
        "ResponseHeadersPolicyId": str,
        "ForwardedValues": ForwardedValuesTypeDef,
        "MinTTL": int,
        "DefaultTTL": int,
        "MaxTTL": int,
    },
    total=False,
)

class DefaultCacheBehaviorTypeDef(
    _RequiredDefaultCacheBehaviorTypeDef, _OptionalDefaultCacheBehaviorTypeDef
):
    pass

_RequiredCachePolicyConfigOutputTypeDef = TypedDict(
    "_RequiredCachePolicyConfigOutputTypeDef",
    {
        "Name": str,
        "MinTTL": int,
    },
)
_OptionalCachePolicyConfigOutputTypeDef = TypedDict(
    "_OptionalCachePolicyConfigOutputTypeDef",
    {
        "Comment": str,
        "DefaultTTL": int,
        "MaxTTL": int,
        "ParametersInCacheKeyAndForwardedToOrigin": (
            ParametersInCacheKeyAndForwardedToOriginOutputTypeDef
        ),
    },
    total=False,
)

class CachePolicyConfigOutputTypeDef(
    _RequiredCachePolicyConfigOutputTypeDef, _OptionalCachePolicyConfigOutputTypeDef
):
    pass

GetOriginRequestPolicyConfigResultTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigResultTypeDef",
    {
        "OriginRequestPolicyConfig": OriginRequestPolicyConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OriginRequestPolicyTypeDef = TypedDict(
    "OriginRequestPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "OriginRequestPolicyConfig": OriginRequestPolicyConfigOutputTypeDef,
    },
)

_RequiredCachePolicyConfigTypeDef = TypedDict(
    "_RequiredCachePolicyConfigTypeDef",
    {
        "Name": str,
        "MinTTL": int,
    },
)
_OptionalCachePolicyConfigTypeDef = TypedDict(
    "_OptionalCachePolicyConfigTypeDef",
    {
        "Comment": str,
        "DefaultTTL": int,
        "MaxTTL": int,
        "ParametersInCacheKeyAndForwardedToOrigin": ParametersInCacheKeyAndForwardedToOriginTypeDef,
    },
    total=False,
)

class CachePolicyConfigTypeDef(
    _RequiredCachePolicyConfigTypeDef, _OptionalCachePolicyConfigTypeDef
):
    pass

CreateOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "CreateOriginRequestPolicyRequestRequestTypeDef",
    {
        "OriginRequestPolicyConfig": OriginRequestPolicyConfigTypeDef,
    },
)

_RequiredUpdateOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOriginRequestPolicyRequestRequestTypeDef",
    {
        "OriginRequestPolicyConfig": OriginRequestPolicyConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateOriginRequestPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOriginRequestPolicyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateOriginRequestPolicyRequestRequestTypeDef(
    _RequiredUpdateOriginRequestPolicyRequestRequestTypeDef,
    _OptionalUpdateOriginRequestPolicyRequestRequestTypeDef,
):
    pass

_RequiredContinuousDeploymentPolicyConfigOutputTypeDef = TypedDict(
    "_RequiredContinuousDeploymentPolicyConfigOutputTypeDef",
    {
        "StagingDistributionDnsNames": StagingDistributionDnsNamesOutputTypeDef,
        "Enabled": bool,
    },
)
_OptionalContinuousDeploymentPolicyConfigOutputTypeDef = TypedDict(
    "_OptionalContinuousDeploymentPolicyConfigOutputTypeDef",
    {
        "TrafficConfig": TrafficConfigOutputTypeDef,
    },
    total=False,
)

class ContinuousDeploymentPolicyConfigOutputTypeDef(
    _RequiredContinuousDeploymentPolicyConfigOutputTypeDef,
    _OptionalContinuousDeploymentPolicyConfigOutputTypeDef,
):
    pass

_RequiredContinuousDeploymentPolicyConfigTypeDef = TypedDict(
    "_RequiredContinuousDeploymentPolicyConfigTypeDef",
    {
        "StagingDistributionDnsNames": StagingDistributionDnsNamesTypeDef,
        "Enabled": bool,
    },
)
_OptionalContinuousDeploymentPolicyConfigTypeDef = TypedDict(
    "_OptionalContinuousDeploymentPolicyConfigTypeDef",
    {
        "TrafficConfig": TrafficConfigTypeDef,
    },
    total=False,
)

class ContinuousDeploymentPolicyConfigTypeDef(
    _RequiredContinuousDeploymentPolicyConfigTypeDef,
    _OptionalContinuousDeploymentPolicyConfigTypeDef,
):
    pass

OriginsOutputTypeDef = TypedDict(
    "OriginsOutputTypeDef",
    {
        "Quantity": int,
        "Items": List[OriginOutputTypeDef],
    },
)

OriginsTypeDef = TypedDict(
    "OriginsTypeDef",
    {
        "Quantity": int,
        "Items": Sequence[OriginTypeDef],
    },
)

_RequiredFieldLevelEncryptionProfileConfigOutputTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileConfigOutputTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "EncryptionEntities": EncryptionEntitiesOutputTypeDef,
    },
)
_OptionalFieldLevelEncryptionProfileConfigOutputTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileConfigOutputTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class FieldLevelEncryptionProfileConfigOutputTypeDef(
    _RequiredFieldLevelEncryptionProfileConfigOutputTypeDef,
    _OptionalFieldLevelEncryptionProfileConfigOutputTypeDef,
):
    pass

_RequiredFieldLevelEncryptionProfileSummaryTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Name": str,
        "EncryptionEntities": EncryptionEntitiesOutputTypeDef,
    },
)
_OptionalFieldLevelEncryptionProfileSummaryTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileSummaryTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class FieldLevelEncryptionProfileSummaryTypeDef(
    _RequiredFieldLevelEncryptionProfileSummaryTypeDef,
    _OptionalFieldLevelEncryptionProfileSummaryTypeDef,
):
    pass

_RequiredFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "EncryptionEntities": EncryptionEntitiesTypeDef,
    },
)
_OptionalFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class FieldLevelEncryptionProfileConfigTypeDef(
    _RequiredFieldLevelEncryptionProfileConfigTypeDef,
    _OptionalFieldLevelEncryptionProfileConfigTypeDef,
):
    pass

CreateRealtimeLogConfigResultTypeDef = TypedDict(
    "CreateRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": RealtimeLogConfigTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRealtimeLogConfigResultTypeDef = TypedDict(
    "GetRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": RealtimeLogConfigTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRealtimeLogConfigsTypeDef = TypedDict(
    "_RequiredRealtimeLogConfigsTypeDef",
    {
        "MaxItems": int,
        "IsTruncated": bool,
        "Marker": str,
    },
)
_OptionalRealtimeLogConfigsTypeDef = TypedDict(
    "_OptionalRealtimeLogConfigsTypeDef",
    {
        "Items": List[RealtimeLogConfigTypeDef],
        "NextMarker": str,
    },
    total=False,
)

class RealtimeLogConfigsTypeDef(
    _RequiredRealtimeLogConfigsTypeDef, _OptionalRealtimeLogConfigsTypeDef
):
    pass

UpdateRealtimeLogConfigResultTypeDef = TypedDict(
    "UpdateRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": RealtimeLogConfigTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsResultTypeDef = TypedDict(
    "ListFunctionsResultTypeDef",
    {
        "FunctionList": FunctionListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestFunctionResultTypeDef = TypedDict(
    "TestFunctionResultTypeDef",
    {
        "TestResult": TestResultTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredKeyGroupListTypeDef = TypedDict(
    "_RequiredKeyGroupListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalKeyGroupListTypeDef = TypedDict(
    "_OptionalKeyGroupListTypeDef",
    {
        "NextMarker": str,
        "Items": List[KeyGroupSummaryTypeDef],
    },
    total=False,
)

class KeyGroupListTypeDef(_RequiredKeyGroupListTypeDef, _OptionalKeyGroupListTypeDef):
    pass

CreateInvalidationResultTypeDef = TypedDict(
    "CreateInvalidationResultTypeDef",
    {
        "Location": str,
        "Invalidation": InvalidationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvalidationResultTypeDef = TypedDict(
    "GetInvalidationResultTypeDef",
    {
        "Invalidation": InvalidationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStreamingDistributionTypeDef = TypedDict(
    "_RequiredStreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "DomainName": str,
        "ActiveTrustedSigners": ActiveTrustedSignersTypeDef,
        "StreamingDistributionConfig": StreamingDistributionConfigOutputTypeDef,
    },
)
_OptionalStreamingDistributionTypeDef = TypedDict(
    "_OptionalStreamingDistributionTypeDef",
    {
        "LastModifiedTime": datetime,
    },
    total=False,
)

class StreamingDistributionTypeDef(
    _RequiredStreamingDistributionTypeDef, _OptionalStreamingDistributionTypeDef
):
    pass

_RequiredOriginGroupsOutputTypeDef = TypedDict(
    "_RequiredOriginGroupsOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalOriginGroupsOutputTypeDef = TypedDict(
    "_OptionalOriginGroupsOutputTypeDef",
    {
        "Items": List[OriginGroupOutputTypeDef],
    },
    total=False,
)

class OriginGroupsOutputTypeDef(
    _RequiredOriginGroupsOutputTypeDef, _OptionalOriginGroupsOutputTypeDef
):
    pass

_RequiredOriginGroupsTypeDef = TypedDict(
    "_RequiredOriginGroupsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalOriginGroupsTypeDef = TypedDict(
    "_OptionalOriginGroupsTypeDef",
    {
        "Items": Sequence[OriginGroupTypeDef],
    },
    total=False,
)

class OriginGroupsTypeDef(_RequiredOriginGroupsTypeDef, _OptionalOriginGroupsTypeDef):
    pass

_RequiredFieldLevelEncryptionConfigOutputTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionConfigOutputTypeDef",
    {
        "CallerReference": str,
    },
)
_OptionalFieldLevelEncryptionConfigOutputTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionConfigOutputTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": QueryArgProfileConfigOutputTypeDef,
        "ContentTypeProfileConfig": ContentTypeProfileConfigOutputTypeDef,
    },
    total=False,
)

class FieldLevelEncryptionConfigOutputTypeDef(
    _RequiredFieldLevelEncryptionConfigOutputTypeDef,
    _OptionalFieldLevelEncryptionConfigOutputTypeDef,
):
    pass

_RequiredFieldLevelEncryptionSummaryTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
    },
)
_OptionalFieldLevelEncryptionSummaryTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionSummaryTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": QueryArgProfileConfigOutputTypeDef,
        "ContentTypeProfileConfig": ContentTypeProfileConfigOutputTypeDef,
    },
    total=False,
)

class FieldLevelEncryptionSummaryTypeDef(
    _RequiredFieldLevelEncryptionSummaryTypeDef, _OptionalFieldLevelEncryptionSummaryTypeDef
):
    pass

_RequiredFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionConfigTypeDef",
    {
        "CallerReference": str,
    },
)
_OptionalFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionConfigTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": QueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ContentTypeProfileConfigTypeDef,
    },
    total=False,
)

class FieldLevelEncryptionConfigTypeDef(
    _RequiredFieldLevelEncryptionConfigTypeDef, _OptionalFieldLevelEncryptionConfigTypeDef
):
    pass

GetResponseHeadersPolicyConfigResultTypeDef = TypedDict(
    "GetResponseHeadersPolicyConfigResultTypeDef",
    {
        "ResponseHeadersPolicyConfig": ResponseHeadersPolicyConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseHeadersPolicyTypeDef = TypedDict(
    "ResponseHeadersPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "ResponseHeadersPolicyConfig": ResponseHeadersPolicyConfigOutputTypeDef,
    },
)

CreateResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "CreateResponseHeadersPolicyRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyConfig": ResponseHeadersPolicyConfigTypeDef,
    },
)

_RequiredUpdateResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResponseHeadersPolicyRequestRequestTypeDef",
    {
        "ResponseHeadersPolicyConfig": ResponseHeadersPolicyConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateResponseHeadersPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResponseHeadersPolicyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateResponseHeadersPolicyRequestRequestTypeDef(
    _RequiredUpdateResponseHeadersPolicyRequestRequestTypeDef,
    _OptionalUpdateResponseHeadersPolicyRequestRequestTypeDef,
):
    pass

ListStreamingDistributionsResultTypeDef = TypedDict(
    "ListStreamingDistributionsResultTypeDef",
    {
        "StreamingDistributionList": StreamingDistributionListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingDistributionWithTagsRequestRequestTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsRequestRequestTypeDef",
    {
        "StreamingDistributionConfigWithTags": StreamingDistributionConfigWithTagsTypeDef,
    },
)

_RequiredCacheBehaviorsOutputTypeDef = TypedDict(
    "_RequiredCacheBehaviorsOutputTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCacheBehaviorsOutputTypeDef = TypedDict(
    "_OptionalCacheBehaviorsOutputTypeDef",
    {
        "Items": List[CacheBehaviorOutputTypeDef],
    },
    total=False,
)

class CacheBehaviorsOutputTypeDef(
    _RequiredCacheBehaviorsOutputTypeDef, _OptionalCacheBehaviorsOutputTypeDef
):
    pass

_RequiredCacheBehaviorsTypeDef = TypedDict(
    "_RequiredCacheBehaviorsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCacheBehaviorsTypeDef = TypedDict(
    "_OptionalCacheBehaviorsTypeDef",
    {
        "Items": Sequence[CacheBehaviorTypeDef],
    },
    total=False,
)

class CacheBehaviorsTypeDef(_RequiredCacheBehaviorsTypeDef, _OptionalCacheBehaviorsTypeDef):
    pass

CachePolicyTypeDef = TypedDict(
    "CachePolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "CachePolicyConfig": CachePolicyConfigOutputTypeDef,
    },
)

GetCachePolicyConfigResultTypeDef = TypedDict(
    "GetCachePolicyConfigResultTypeDef",
    {
        "CachePolicyConfig": CachePolicyConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOriginRequestPolicyResultTypeDef = TypedDict(
    "CreateOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOriginRequestPolicyResultTypeDef = TypedDict(
    "GetOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OriginRequestPolicySummaryTypeDef = TypedDict(
    "OriginRequestPolicySummaryTypeDef",
    {
        "Type": OriginRequestPolicyTypeType,
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
    },
)

UpdateOriginRequestPolicyResultTypeDef = TypedDict(
    "UpdateOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": OriginRequestPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCachePolicyRequestRequestTypeDef = TypedDict(
    "CreateCachePolicyRequestRequestTypeDef",
    {
        "CachePolicyConfig": CachePolicyConfigTypeDef,
    },
)

_RequiredUpdateCachePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCachePolicyRequestRequestTypeDef",
    {
        "CachePolicyConfig": CachePolicyConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateCachePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCachePolicyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateCachePolicyRequestRequestTypeDef(
    _RequiredUpdateCachePolicyRequestRequestTypeDef, _OptionalUpdateCachePolicyRequestRequestTypeDef
):
    pass

ContinuousDeploymentPolicyTypeDef = TypedDict(
    "ContinuousDeploymentPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "ContinuousDeploymentPolicyConfig": ContinuousDeploymentPolicyConfigOutputTypeDef,
    },
)

GetContinuousDeploymentPolicyConfigResultTypeDef = TypedDict(
    "GetContinuousDeploymentPolicyConfigResultTypeDef",
    {
        "ContinuousDeploymentPolicyConfig": ContinuousDeploymentPolicyConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "CreateContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "ContinuousDeploymentPolicyConfig": ContinuousDeploymentPolicyConfigTypeDef,
    },
)

_RequiredUpdateContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "ContinuousDeploymentPolicyConfig": ContinuousDeploymentPolicyConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateContinuousDeploymentPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContinuousDeploymentPolicyRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateContinuousDeploymentPolicyRequestRequestTypeDef(
    _RequiredUpdateContinuousDeploymentPolicyRequestRequestTypeDef,
    _OptionalUpdateContinuousDeploymentPolicyRequestRequestTypeDef,
):
    pass

FieldLevelEncryptionProfileTypeDef = TypedDict(
    "FieldLevelEncryptionProfileTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigOutputTypeDef,
    },
)

GetFieldLevelEncryptionProfileConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFieldLevelEncryptionProfileListTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalFieldLevelEncryptionProfileListTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileListTypeDef",
    {
        "NextMarker": str,
        "Items": List[FieldLevelEncryptionProfileSummaryTypeDef],
    },
    total=False,
)

class FieldLevelEncryptionProfileListTypeDef(
    _RequiredFieldLevelEncryptionProfileListTypeDef, _OptionalFieldLevelEncryptionProfileListTypeDef
):
    pass

CreateFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigTypeDef,
    },
)

_RequiredUpdateFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": FieldLevelEncryptionProfileConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateFieldLevelEncryptionProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFieldLevelEncryptionProfileRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateFieldLevelEncryptionProfileRequestRequestTypeDef(
    _RequiredUpdateFieldLevelEncryptionProfileRequestRequestTypeDef,
    _OptionalUpdateFieldLevelEncryptionProfileRequestRequestTypeDef,
):
    pass

ListRealtimeLogConfigsResultTypeDef = TypedDict(
    "ListRealtimeLogConfigsResultTypeDef",
    {
        "RealtimeLogConfigs": RealtimeLogConfigsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeyGroupsResultTypeDef = TypedDict(
    "ListKeyGroupsResultTypeDef",
    {
        "KeyGroupList": KeyGroupListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingDistributionResultTypeDef = TypedDict(
    "CreateStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": StreamingDistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingDistributionWithTagsResultTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsResultTypeDef",
    {
        "StreamingDistribution": StreamingDistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingDistributionResultTypeDef = TypedDict(
    "GetStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": StreamingDistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStreamingDistributionResultTypeDef = TypedDict(
    "UpdateStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": StreamingDistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldLevelEncryptionTypeDef = TypedDict(
    "FieldLevelEncryptionTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigOutputTypeDef,
    },
)

GetFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFieldLevelEncryptionListTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalFieldLevelEncryptionListTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionListTypeDef",
    {
        "NextMarker": str,
        "Items": List[FieldLevelEncryptionSummaryTypeDef],
    },
    total=False,
)

class FieldLevelEncryptionListTypeDef(
    _RequiredFieldLevelEncryptionListTypeDef, _OptionalFieldLevelEncryptionListTypeDef
):
    pass

CreateFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigTypeDef,
    },
)

_RequiredUpdateFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "FieldLevelEncryptionConfig": FieldLevelEncryptionConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateFieldLevelEncryptionConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFieldLevelEncryptionConfigRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateFieldLevelEncryptionConfigRequestRequestTypeDef(
    _RequiredUpdateFieldLevelEncryptionConfigRequestRequestTypeDef,
    _OptionalUpdateFieldLevelEncryptionConfigRequestRequestTypeDef,
):
    pass

CreateResponseHeadersPolicyResultTypeDef = TypedDict(
    "CreateResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResponseHeadersPolicyResultTypeDef = TypedDict(
    "GetResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseHeadersPolicySummaryTypeDef = TypedDict(
    "ResponseHeadersPolicySummaryTypeDef",
    {
        "Type": ResponseHeadersPolicyTypeType,
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
    },
)

UpdateResponseHeadersPolicyResultTypeDef = TypedDict(
    "UpdateResponseHeadersPolicyResultTypeDef",
    {
        "ResponseHeadersPolicy": ResponseHeadersPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDistributionConfigOutputTypeDef = TypedDict(
    "_RequiredDistributionConfigOutputTypeDef",
    {
        "CallerReference": str,
        "Origins": OriginsOutputTypeDef,
        "DefaultCacheBehavior": DefaultCacheBehaviorOutputTypeDef,
        "Comment": str,
        "Enabled": bool,
    },
)
_OptionalDistributionConfigOutputTypeDef = TypedDict(
    "_OptionalDistributionConfigOutputTypeDef",
    {
        "Aliases": AliasesOutputTypeDef,
        "DefaultRootObject": str,
        "OriginGroups": OriginGroupsOutputTypeDef,
        "CacheBehaviors": CacheBehaviorsOutputTypeDef,
        "CustomErrorResponses": CustomErrorResponsesOutputTypeDef,
        "Logging": LoggingConfigOutputTypeDef,
        "PriceClass": PriceClassType,
        "ViewerCertificate": ViewerCertificateOutputTypeDef,
        "Restrictions": RestrictionsOutputTypeDef,
        "WebACLId": str,
        "HttpVersion": HttpVersionType,
        "IsIPV6Enabled": bool,
        "ContinuousDeploymentPolicyId": str,
        "Staging": bool,
    },
    total=False,
)

class DistributionConfigOutputTypeDef(
    _RequiredDistributionConfigOutputTypeDef, _OptionalDistributionConfigOutputTypeDef
):
    pass

_RequiredDistributionSummaryTypeDef = TypedDict(
    "_RequiredDistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "Aliases": AliasesOutputTypeDef,
        "Origins": OriginsOutputTypeDef,
        "DefaultCacheBehavior": DefaultCacheBehaviorOutputTypeDef,
        "CacheBehaviors": CacheBehaviorsOutputTypeDef,
        "CustomErrorResponses": CustomErrorResponsesOutputTypeDef,
        "Comment": str,
        "PriceClass": PriceClassType,
        "Enabled": bool,
        "ViewerCertificate": ViewerCertificateOutputTypeDef,
        "Restrictions": RestrictionsOutputTypeDef,
        "WebACLId": str,
        "HttpVersion": HttpVersionType,
        "IsIPV6Enabled": bool,
        "Staging": bool,
    },
)
_OptionalDistributionSummaryTypeDef = TypedDict(
    "_OptionalDistributionSummaryTypeDef",
    {
        "OriginGroups": OriginGroupsOutputTypeDef,
        "AliasICPRecordals": List[AliasICPRecordalTypeDef],
    },
    total=False,
)

class DistributionSummaryTypeDef(
    _RequiredDistributionSummaryTypeDef, _OptionalDistributionSummaryTypeDef
):
    pass

_RequiredDistributionConfigTypeDef = TypedDict(
    "_RequiredDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "Origins": OriginsTypeDef,
        "DefaultCacheBehavior": DefaultCacheBehaviorTypeDef,
        "Comment": str,
        "Enabled": bool,
    },
)
_OptionalDistributionConfigTypeDef = TypedDict(
    "_OptionalDistributionConfigTypeDef",
    {
        "Aliases": AliasesTypeDef,
        "DefaultRootObject": str,
        "OriginGroups": OriginGroupsTypeDef,
        "CacheBehaviors": CacheBehaviorsTypeDef,
        "CustomErrorResponses": CustomErrorResponsesTypeDef,
        "Logging": LoggingConfigTypeDef,
        "PriceClass": PriceClassType,
        "ViewerCertificate": ViewerCertificateTypeDef,
        "Restrictions": RestrictionsTypeDef,
        "WebACLId": str,
        "HttpVersion": HttpVersionType,
        "IsIPV6Enabled": bool,
        "ContinuousDeploymentPolicyId": str,
        "Staging": bool,
    },
    total=False,
)

class DistributionConfigTypeDef(
    _RequiredDistributionConfigTypeDef, _OptionalDistributionConfigTypeDef
):
    pass

CachePolicySummaryTypeDef = TypedDict(
    "CachePolicySummaryTypeDef",
    {
        "Type": CachePolicyTypeType,
        "CachePolicy": CachePolicyTypeDef,
    },
)

CreateCachePolicyResultTypeDef = TypedDict(
    "CreateCachePolicyResultTypeDef",
    {
        "CachePolicy": CachePolicyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCachePolicyResultTypeDef = TypedDict(
    "GetCachePolicyResultTypeDef",
    {
        "CachePolicy": CachePolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCachePolicyResultTypeDef = TypedDict(
    "UpdateCachePolicyResultTypeDef",
    {
        "CachePolicy": CachePolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOriginRequestPolicyListTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalOriginRequestPolicyListTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyListTypeDef",
    {
        "NextMarker": str,
        "Items": List[OriginRequestPolicySummaryTypeDef],
    },
    total=False,
)

class OriginRequestPolicyListTypeDef(
    _RequiredOriginRequestPolicyListTypeDef, _OptionalOriginRequestPolicyListTypeDef
):
    pass

ContinuousDeploymentPolicySummaryTypeDef = TypedDict(
    "ContinuousDeploymentPolicySummaryTypeDef",
    {
        "ContinuousDeploymentPolicy": ContinuousDeploymentPolicyTypeDef,
    },
)

CreateContinuousDeploymentPolicyResultTypeDef = TypedDict(
    "CreateContinuousDeploymentPolicyResultTypeDef",
    {
        "ContinuousDeploymentPolicy": ContinuousDeploymentPolicyTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContinuousDeploymentPolicyResultTypeDef = TypedDict(
    "GetContinuousDeploymentPolicyResultTypeDef",
    {
        "ContinuousDeploymentPolicy": ContinuousDeploymentPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContinuousDeploymentPolicyResultTypeDef = TypedDict(
    "UpdateContinuousDeploymentPolicyResultTypeDef",
    {
        "ContinuousDeploymentPolicy": ContinuousDeploymentPolicyTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": FieldLevelEncryptionProfileTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFieldLevelEncryptionProfilesResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    {
        "FieldLevelEncryptionProfileList": FieldLevelEncryptionProfileListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryption": FieldLevelEncryptionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionResultTypeDef",
    {
        "FieldLevelEncryption": FieldLevelEncryptionTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryption": FieldLevelEncryptionTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFieldLevelEncryptionConfigsResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    {
        "FieldLevelEncryptionList": FieldLevelEncryptionListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResponseHeadersPolicyListTypeDef = TypedDict(
    "_RequiredResponseHeadersPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalResponseHeadersPolicyListTypeDef = TypedDict(
    "_OptionalResponseHeadersPolicyListTypeDef",
    {
        "NextMarker": str,
        "Items": List[ResponseHeadersPolicySummaryTypeDef],
    },
    total=False,
)

class ResponseHeadersPolicyListTypeDef(
    _RequiredResponseHeadersPolicyListTypeDef, _OptionalResponseHeadersPolicyListTypeDef
):
    pass

_RequiredDistributionTypeDef = TypedDict(
    "_RequiredDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "InProgressInvalidationBatches": int,
        "DomainName": str,
        "DistributionConfig": DistributionConfigOutputTypeDef,
    },
)
_OptionalDistributionTypeDef = TypedDict(
    "_OptionalDistributionTypeDef",
    {
        "ActiveTrustedSigners": ActiveTrustedSignersTypeDef,
        "ActiveTrustedKeyGroups": ActiveTrustedKeyGroupsTypeDef,
        "AliasICPRecordals": List[AliasICPRecordalTypeDef],
    },
    total=False,
)

class DistributionTypeDef(_RequiredDistributionTypeDef, _OptionalDistributionTypeDef):
    pass

GetDistributionConfigResultTypeDef = TypedDict(
    "GetDistributionConfigResultTypeDef",
    {
        "DistributionConfig": DistributionConfigOutputTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDistributionListTypeDef = TypedDict(
    "_RequiredDistributionListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalDistributionListTypeDef = TypedDict(
    "_OptionalDistributionListTypeDef",
    {
        "NextMarker": str,
        "Items": List[DistributionSummaryTypeDef],
    },
    total=False,
)

class DistributionListTypeDef(_RequiredDistributionListTypeDef, _OptionalDistributionListTypeDef):
    pass

CreateDistributionRequestRequestTypeDef = TypedDict(
    "CreateDistributionRequestRequestTypeDef",
    {
        "DistributionConfig": DistributionConfigTypeDef,
    },
)

DistributionConfigWithTagsTypeDef = TypedDict(
    "DistributionConfigWithTagsTypeDef",
    {
        "DistributionConfig": DistributionConfigTypeDef,
        "Tags": TagsTypeDef,
    },
)

_RequiredUpdateDistributionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDistributionRequestRequestTypeDef",
    {
        "DistributionConfig": DistributionConfigTypeDef,
        "Id": str,
    },
)
_OptionalUpdateDistributionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDistributionRequestRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)

class UpdateDistributionRequestRequestTypeDef(
    _RequiredUpdateDistributionRequestRequestTypeDef,
    _OptionalUpdateDistributionRequestRequestTypeDef,
):
    pass

_RequiredCachePolicyListTypeDef = TypedDict(
    "_RequiredCachePolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalCachePolicyListTypeDef = TypedDict(
    "_OptionalCachePolicyListTypeDef",
    {
        "NextMarker": str,
        "Items": List[CachePolicySummaryTypeDef],
    },
    total=False,
)

class CachePolicyListTypeDef(_RequiredCachePolicyListTypeDef, _OptionalCachePolicyListTypeDef):
    pass

ListOriginRequestPoliciesResultTypeDef = TypedDict(
    "ListOriginRequestPoliciesResultTypeDef",
    {
        "OriginRequestPolicyList": OriginRequestPolicyListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredContinuousDeploymentPolicyListTypeDef = TypedDict(
    "_RequiredContinuousDeploymentPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalContinuousDeploymentPolicyListTypeDef = TypedDict(
    "_OptionalContinuousDeploymentPolicyListTypeDef",
    {
        "NextMarker": str,
        "Items": List[ContinuousDeploymentPolicySummaryTypeDef],
    },
    total=False,
)

class ContinuousDeploymentPolicyListTypeDef(
    _RequiredContinuousDeploymentPolicyListTypeDef, _OptionalContinuousDeploymentPolicyListTypeDef
):
    pass

ListResponseHeadersPoliciesResultTypeDef = TypedDict(
    "ListResponseHeadersPoliciesResultTypeDef",
    {
        "ResponseHeadersPolicyList": ResponseHeadersPolicyListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyDistributionResultTypeDef = TypedDict(
    "CopyDistributionResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionWithTagsResultTypeDef = TypedDict(
    "CreateDistributionWithTagsResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionResultTypeDef = TypedDict(
    "GetDistributionResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDistributionWithStagingConfigResultTypeDef = TypedDict(
    "UpdateDistributionWithStagingConfigResultTypeDef",
    {
        "Distribution": DistributionTypeDef,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByRealtimeLogConfigResultTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    {
        "DistributionList": DistributionListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByWebACLIdResultTypeDef = TypedDict(
    "ListDistributionsByWebACLIdResultTypeDef",
    {
        "DistributionList": DistributionListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsResultTypeDef = TypedDict(
    "ListDistributionsResultTypeDef",
    {
        "DistributionList": DistributionListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionWithTagsRequestRequestTypeDef = TypedDict(
    "CreateDistributionWithTagsRequestRequestTypeDef",
    {
        "DistributionConfigWithTags": DistributionConfigWithTagsTypeDef,
    },
)

ListCachePoliciesResultTypeDef = TypedDict(
    "ListCachePoliciesResultTypeDef",
    {
        "CachePolicyList": CachePolicyListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContinuousDeploymentPoliciesResultTypeDef = TypedDict(
    "ListContinuousDeploymentPoliciesResultTypeDef",
    {
        "ContinuousDeploymentPolicyList": ContinuousDeploymentPolicyListTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
