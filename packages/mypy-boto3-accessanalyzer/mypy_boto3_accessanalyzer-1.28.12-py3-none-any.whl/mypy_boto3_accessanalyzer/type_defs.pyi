"""
Type annotations for accessanalyzer service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/type_defs/)

Usage::

    ```python
    from mypy_boto3_accessanalyzer.type_defs import AccessPreviewStatusReasonTypeDef

    data: AccessPreviewStatusReasonTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AccessPreviewStatusReasonCodeType,
    AccessPreviewStatusType,
    AclPermissionType,
    AnalyzerStatusType,
    FindingChangeTypeType,
    FindingSourceTypeType,
    FindingStatusType,
    FindingStatusUpdateType,
    JobErrorCodeType,
    JobStatusType,
    KmsGrantOperationType,
    LocaleType,
    OrderByType,
    PolicyTypeType,
    ReasonCodeType,
    ResourceTypeType,
    TypeType,
    ValidatePolicyFindingTypeType,
    ValidatePolicyResourceTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessPreviewStatusReasonTypeDef",
    "AclGranteeOutputTypeDef",
    "AclGranteeTypeDef",
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "StatusReasonTypeDef",
    "ApplyArchiveRuleRequestRequestTypeDef",
    "CriterionOutputTypeDef",
    "CancelPolicyGenerationRequestRequestTypeDef",
    "TrailTypeDef",
    "TrailPropertiesTypeDef",
    "EbsSnapshotConfigurationOutputTypeDef",
    "EcrRepositoryConfigurationOutputTypeDef",
    "EfsFileSystemConfigurationOutputTypeDef",
    "IamRoleConfigurationOutputTypeDef",
    "SecretsManagerSecretConfigurationOutputTypeDef",
    "SnsTopicConfigurationOutputTypeDef",
    "SqsQueueConfigurationOutputTypeDef",
    "EbsSnapshotConfigurationTypeDef",
    "EcrRepositoryConfigurationTypeDef",
    "EfsFileSystemConfigurationTypeDef",
    "IamRoleConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SnsTopicConfigurationTypeDef",
    "SqsQueueConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "CriterionTypeDef",
    "DeleteAnalyzerRequestRequestTypeDef",
    "DeleteArchiveRuleRequestRequestTypeDef",
    "FindingSourceDetailTypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewRequestRequestTypeDef",
    "GetAnalyzedResourceRequestRequestTypeDef",
    "GetAnalyzerRequestRequestTypeDef",
    "GetArchiveRuleRequestRequestTypeDef",
    "GetFindingRequestRequestTypeDef",
    "GetGeneratedPolicyRequestRequestTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConstraintsOutputTypeDef",
    "KmsGrantConstraintsTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccessPreviewsRequestRequestTypeDef",
    "ListAnalyzedResourcesRequestRequestTypeDef",
    "ListAnalyzersRequestRequestTypeDef",
    "ListArchiveRulesRequestRequestTypeDef",
    "SortCriteriaTypeDef",
    "ListPolicyGenerationsRequestRequestTypeDef",
    "PolicyGenerationTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "VpcConfigurationOutputTypeDef",
    "VpcConfigurationTypeDef",
    "SubstringTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PositionTypeDef",
    "RdsDbClusterSnapshotAttributeValueOutputTypeDef",
    "RdsDbClusterSnapshotAttributeValueTypeDef",
    "RdsDbSnapshotAttributeValueOutputTypeDef",
    "RdsDbSnapshotAttributeValueTypeDef",
    "S3PublicAccessBlockConfigurationOutputTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "StartResourceScanRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "ValidatePolicyRequestRequestTypeDef",
    "AccessPreviewSummaryTypeDef",
    "S3BucketAclGrantConfigurationOutputTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "AnalyzerSummaryTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "CreateAccessPreviewResponseTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "CreateArchiveRuleRequestRequestTypeDef",
    "InlineArchiveRuleTypeDef",
    "ListAccessPreviewFindingsRequestRequestTypeDef",
    "UpdateArchiveRuleRequestRequestTypeDef",
    "FindingSourceTypeDef",
    "JobDetailsTypeDef",
    "KmsGrantConfigurationOutputTypeDef",
    "KmsGrantConfigurationTypeDef",
    "ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef",
    "ListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef",
    "ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef",
    "ListAnalyzersRequestListAnalyzersPaginateTypeDef",
    "ListArchiveRulesRequestListArchiveRulesPaginateTypeDef",
    "ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef",
    "ValidatePolicyRequestValidatePolicyPaginateTypeDef",
    "ListFindingsRequestListFindingsPaginateTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "NetworkOriginConfigurationOutputTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "PathElementTypeDef",
    "SpanTypeDef",
    "RdsDbClusterSnapshotConfigurationOutputTypeDef",
    "RdsDbClusterSnapshotConfigurationTypeDef",
    "RdsDbSnapshotConfigurationOutputTypeDef",
    "RdsDbSnapshotConfigurationTypeDef",
    "ListAccessPreviewsResponseTypeDef",
    "GetAnalyzerResponseTypeDef",
    "ListAnalyzersResponseTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "StartPolicyGenerationRequestRequestTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "CreateAnalyzerRequestRequestTypeDef",
    "AccessPreviewFindingTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "KmsKeyConfigurationOutputTypeDef",
    "KmsKeyConfigurationTypeDef",
    "S3AccessPointConfigurationOutputTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "LocationTypeDef",
    "GeneratedPolicyResultTypeDef",
    "ListAccessPreviewFindingsResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "GetFindingResponseTypeDef",
    "S3BucketConfigurationOutputTypeDef",
    "S3BucketConfigurationTypeDef",
    "ValidatePolicyFindingTypeDef",
    "GetGeneratedPolicyResponseTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationTypeDef",
    "ValidatePolicyResponseTypeDef",
    "AccessPreviewTypeDef",
    "CreateAccessPreviewRequestRequestTypeDef",
    "GetAccessPreviewResponseTypeDef",
)

AccessPreviewStatusReasonTypeDef = TypedDict(
    "AccessPreviewStatusReasonTypeDef",
    {
        "code": AccessPreviewStatusReasonCodeType,
    },
)

AclGranteeOutputTypeDef = TypedDict(
    "AclGranteeOutputTypeDef",
    {
        "id": str,
        "uri": str,
    },
    total=False,
)

AclGranteeTypeDef = TypedDict(
    "AclGranteeTypeDef",
    {
        "id": str,
        "uri": str,
    },
    total=False,
)

AnalyzedResourceSummaryTypeDef = TypedDict(
    "AnalyzedResourceSummaryTypeDef",
    {
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
    },
)

_RequiredAnalyzedResourceTypeDef = TypedDict(
    "_RequiredAnalyzedResourceTypeDef",
    {
        "resourceArn": str,
        "resourceType": ResourceTypeType,
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "isPublic": bool,
        "resourceOwnerAccount": str,
    },
)
_OptionalAnalyzedResourceTypeDef = TypedDict(
    "_OptionalAnalyzedResourceTypeDef",
    {
        "actions": List[str],
        "sharedVia": List[str],
        "status": FindingStatusType,
        "error": str,
    },
    total=False,
)

class AnalyzedResourceTypeDef(_RequiredAnalyzedResourceTypeDef, _OptionalAnalyzedResourceTypeDef):
    pass

StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "code": ReasonCodeType,
    },
)

_RequiredApplyArchiveRuleRequestRequestTypeDef = TypedDict(
    "_RequiredApplyArchiveRuleRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "ruleName": str,
    },
)
_OptionalApplyArchiveRuleRequestRequestTypeDef = TypedDict(
    "_OptionalApplyArchiveRuleRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class ApplyArchiveRuleRequestRequestTypeDef(
    _RequiredApplyArchiveRuleRequestRequestTypeDef, _OptionalApplyArchiveRuleRequestRequestTypeDef
):
    pass

CriterionOutputTypeDef = TypedDict(
    "CriterionOutputTypeDef",
    {
        "eq": List[str],
        "neq": List[str],
        "contains": List[str],
        "exists": bool,
    },
    total=False,
)

CancelPolicyGenerationRequestRequestTypeDef = TypedDict(
    "CancelPolicyGenerationRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

_RequiredTrailTypeDef = TypedDict(
    "_RequiredTrailTypeDef",
    {
        "cloudTrailArn": str,
    },
)
_OptionalTrailTypeDef = TypedDict(
    "_OptionalTrailTypeDef",
    {
        "regions": Sequence[str],
        "allRegions": bool,
    },
    total=False,
)

class TrailTypeDef(_RequiredTrailTypeDef, _OptionalTrailTypeDef):
    pass

_RequiredTrailPropertiesTypeDef = TypedDict(
    "_RequiredTrailPropertiesTypeDef",
    {
        "cloudTrailArn": str,
    },
)
_OptionalTrailPropertiesTypeDef = TypedDict(
    "_OptionalTrailPropertiesTypeDef",
    {
        "regions": List[str],
        "allRegions": bool,
    },
    total=False,
)

class TrailPropertiesTypeDef(_RequiredTrailPropertiesTypeDef, _OptionalTrailPropertiesTypeDef):
    pass

EbsSnapshotConfigurationOutputTypeDef = TypedDict(
    "EbsSnapshotConfigurationOutputTypeDef",
    {
        "userIds": List[str],
        "groups": List[str],
        "kmsKeyId": str,
    },
    total=False,
)

EcrRepositoryConfigurationOutputTypeDef = TypedDict(
    "EcrRepositoryConfigurationOutputTypeDef",
    {
        "repositoryPolicy": str,
    },
    total=False,
)

EfsFileSystemConfigurationOutputTypeDef = TypedDict(
    "EfsFileSystemConfigurationOutputTypeDef",
    {
        "fileSystemPolicy": str,
    },
    total=False,
)

IamRoleConfigurationOutputTypeDef = TypedDict(
    "IamRoleConfigurationOutputTypeDef",
    {
        "trustPolicy": str,
    },
    total=False,
)

SecretsManagerSecretConfigurationOutputTypeDef = TypedDict(
    "SecretsManagerSecretConfigurationOutputTypeDef",
    {
        "kmsKeyId": str,
        "secretPolicy": str,
    },
    total=False,
)

SnsTopicConfigurationOutputTypeDef = TypedDict(
    "SnsTopicConfigurationOutputTypeDef",
    {
        "topicPolicy": str,
    },
    total=False,
)

SqsQueueConfigurationOutputTypeDef = TypedDict(
    "SqsQueueConfigurationOutputTypeDef",
    {
        "queuePolicy": str,
    },
    total=False,
)

EbsSnapshotConfigurationTypeDef = TypedDict(
    "EbsSnapshotConfigurationTypeDef",
    {
        "userIds": Sequence[str],
        "groups": Sequence[str],
        "kmsKeyId": str,
    },
    total=False,
)

EcrRepositoryConfigurationTypeDef = TypedDict(
    "EcrRepositoryConfigurationTypeDef",
    {
        "repositoryPolicy": str,
    },
    total=False,
)

EfsFileSystemConfigurationTypeDef = TypedDict(
    "EfsFileSystemConfigurationTypeDef",
    {
        "fileSystemPolicy": str,
    },
    total=False,
)

IamRoleConfigurationTypeDef = TypedDict(
    "IamRoleConfigurationTypeDef",
    {
        "trustPolicy": str,
    },
    total=False,
)

SecretsManagerSecretConfigurationTypeDef = TypedDict(
    "SecretsManagerSecretConfigurationTypeDef",
    {
        "kmsKeyId": str,
        "secretPolicy": str,
    },
    total=False,
)

SnsTopicConfigurationTypeDef = TypedDict(
    "SnsTopicConfigurationTypeDef",
    {
        "topicPolicy": str,
    },
    total=False,
)

SqsQueueConfigurationTypeDef = TypedDict(
    "SqsQueueConfigurationTypeDef",
    {
        "queuePolicy": str,
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

CriterionTypeDef = TypedDict(
    "CriterionTypeDef",
    {
        "eq": Sequence[str],
        "neq": Sequence[str],
        "contains": Sequence[str],
        "exists": bool,
    },
    total=False,
)

_RequiredDeleteAnalyzerRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
    },
)
_OptionalDeleteAnalyzerRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAnalyzerRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAnalyzerRequestRequestTypeDef(
    _RequiredDeleteAnalyzerRequestRequestTypeDef, _OptionalDeleteAnalyzerRequestRequestTypeDef
):
    pass

_RequiredDeleteArchiveRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
    },
)
_OptionalDeleteArchiveRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteArchiveRuleRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteArchiveRuleRequestRequestTypeDef(
    _RequiredDeleteArchiveRuleRequestRequestTypeDef, _OptionalDeleteArchiveRuleRequestRequestTypeDef
):
    pass

FindingSourceDetailTypeDef = TypedDict(
    "FindingSourceDetailTypeDef",
    {
        "accessPointArn": str,
        "accessPointAccount": str,
    },
    total=False,
)

GeneratedPolicyTypeDef = TypedDict(
    "GeneratedPolicyTypeDef",
    {
        "policy": str,
    },
)

GetAccessPreviewRequestRequestTypeDef = TypedDict(
    "GetAccessPreviewRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)

GetAnalyzedResourceRequestRequestTypeDef = TypedDict(
    "GetAnalyzedResourceRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)

GetAnalyzerRequestRequestTypeDef = TypedDict(
    "GetAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
    },
)

GetArchiveRuleRequestRequestTypeDef = TypedDict(
    "GetArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
    },
)

GetFindingRequestRequestTypeDef = TypedDict(
    "GetFindingRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
    },
)

_RequiredGetGeneratedPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetGeneratedPolicyRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalGetGeneratedPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetGeneratedPolicyRequestRequestTypeDef",
    {
        "includeResourcePlaceholders": bool,
        "includeServiceLevelTemplate": bool,
    },
    total=False,
)

class GetGeneratedPolicyRequestRequestTypeDef(
    _RequiredGetGeneratedPolicyRequestRequestTypeDef,
    _OptionalGetGeneratedPolicyRequestRequestTypeDef,
):
    pass

JobErrorTypeDef = TypedDict(
    "JobErrorTypeDef",
    {
        "code": JobErrorCodeType,
        "message": str,
    },
)

KmsGrantConstraintsOutputTypeDef = TypedDict(
    "KmsGrantConstraintsOutputTypeDef",
    {
        "encryptionContextEquals": Dict[str, str],
        "encryptionContextSubset": Dict[str, str],
    },
    total=False,
)

KmsGrantConstraintsTypeDef = TypedDict(
    "KmsGrantConstraintsTypeDef",
    {
        "encryptionContextEquals": Mapping[str, str],
        "encryptionContextSubset": Mapping[str, str],
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

_RequiredListAccessPreviewsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPreviewsRequestRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListAccessPreviewsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPreviewsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAccessPreviewsRequestRequestTypeDef(
    _RequiredListAccessPreviewsRequestRequestTypeDef,
    _OptionalListAccessPreviewsRequestRequestTypeDef,
):
    pass

_RequiredListAnalyzedResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListAnalyzedResourcesRequestRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListAnalyzedResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListAnalyzedResourcesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAnalyzedResourcesRequestRequestTypeDef(
    _RequiredListAnalyzedResourcesRequestRequestTypeDef,
    _OptionalListAnalyzedResourcesRequestRequestTypeDef,
):
    pass

ListAnalyzersRequestRequestTypeDef = TypedDict(
    "ListAnalyzersRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "type": TypeType,
    },
    total=False,
)

_RequiredListArchiveRulesRequestRequestTypeDef = TypedDict(
    "_RequiredListArchiveRulesRequestRequestTypeDef",
    {
        "analyzerName": str,
    },
)
_OptionalListArchiveRulesRequestRequestTypeDef = TypedDict(
    "_OptionalListArchiveRulesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListArchiveRulesRequestRequestTypeDef(
    _RequiredListArchiveRulesRequestRequestTypeDef, _OptionalListArchiveRulesRequestRequestTypeDef
):
    pass

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": str,
        "orderBy": OrderByType,
    },
    total=False,
)

ListPolicyGenerationsRequestRequestTypeDef = TypedDict(
    "ListPolicyGenerationsRequestRequestTypeDef",
    {
        "principalArn": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredPolicyGenerationTypeDef = TypedDict(
    "_RequiredPolicyGenerationTypeDef",
    {
        "jobId": str,
        "principalArn": str,
        "status": JobStatusType,
        "startedOn": datetime,
    },
)
_OptionalPolicyGenerationTypeDef = TypedDict(
    "_OptionalPolicyGenerationTypeDef",
    {
        "completedOn": datetime,
    },
    total=False,
)

class PolicyGenerationTypeDef(_RequiredPolicyGenerationTypeDef, _OptionalPolicyGenerationTypeDef):
    pass

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

VpcConfigurationOutputTypeDef = TypedDict(
    "VpcConfigurationOutputTypeDef",
    {
        "vpcId": str,
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "vpcId": str,
    },
)

SubstringTypeDef = TypedDict(
    "SubstringTypeDef",
    {
        "start": int,
        "length": int,
    },
)

PolicyGenerationDetailsTypeDef = TypedDict(
    "PolicyGenerationDetailsTypeDef",
    {
        "principalArn": str,
    },
)

PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "line": int,
        "column": int,
        "offset": int,
    },
)

RdsDbClusterSnapshotAttributeValueOutputTypeDef = TypedDict(
    "RdsDbClusterSnapshotAttributeValueOutputTypeDef",
    {
        "accountIds": List[str],
    },
    total=False,
)

RdsDbClusterSnapshotAttributeValueTypeDef = TypedDict(
    "RdsDbClusterSnapshotAttributeValueTypeDef",
    {
        "accountIds": Sequence[str],
    },
    total=False,
)

RdsDbSnapshotAttributeValueOutputTypeDef = TypedDict(
    "RdsDbSnapshotAttributeValueOutputTypeDef",
    {
        "accountIds": List[str],
    },
    total=False,
)

RdsDbSnapshotAttributeValueTypeDef = TypedDict(
    "RdsDbSnapshotAttributeValueTypeDef",
    {
        "accountIds": Sequence[str],
    },
    total=False,
)

S3PublicAccessBlockConfigurationOutputTypeDef = TypedDict(
    "S3PublicAccessBlockConfigurationOutputTypeDef",
    {
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
)

S3PublicAccessBlockConfigurationTypeDef = TypedDict(
    "S3PublicAccessBlockConfigurationTypeDef",
    {
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
)

_RequiredStartResourceScanRequestRequestTypeDef = TypedDict(
    "_RequiredStartResourceScanRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)
_OptionalStartResourceScanRequestRequestTypeDef = TypedDict(
    "_OptionalStartResourceScanRequestRequestTypeDef",
    {
        "resourceOwnerAccount": str,
    },
    total=False,
)

class StartResourceScanRequestRequestTypeDef(
    _RequiredStartResourceScanRequestRequestTypeDef, _OptionalStartResourceScanRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "status": FindingStatusUpdateType,
    },
)
_OptionalUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsRequestRequestTypeDef",
    {
        "ids": Sequence[str],
        "resourceArn": str,
        "clientToken": str,
    },
    total=False,
)

class UpdateFindingsRequestRequestTypeDef(
    _RequiredUpdateFindingsRequestRequestTypeDef, _OptionalUpdateFindingsRequestRequestTypeDef
):
    pass

_RequiredValidatePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredValidatePolicyRequestRequestTypeDef",
    {
        "policyDocument": str,
        "policyType": PolicyTypeType,
    },
)
_OptionalValidatePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalValidatePolicyRequestRequestTypeDef",
    {
        "locale": LocaleType,
        "maxResults": int,
        "nextToken": str,
        "validatePolicyResourceType": ValidatePolicyResourceTypeType,
    },
    total=False,
)

class ValidatePolicyRequestRequestTypeDef(
    _RequiredValidatePolicyRequestRequestTypeDef, _OptionalValidatePolicyRequestRequestTypeDef
):
    pass

_RequiredAccessPreviewSummaryTypeDef = TypedDict(
    "_RequiredAccessPreviewSummaryTypeDef",
    {
        "id": str,
        "analyzerArn": str,
        "createdAt": datetime,
        "status": AccessPreviewStatusType,
    },
)
_OptionalAccessPreviewSummaryTypeDef = TypedDict(
    "_OptionalAccessPreviewSummaryTypeDef",
    {
        "statusReason": AccessPreviewStatusReasonTypeDef,
    },
    total=False,
)

class AccessPreviewSummaryTypeDef(
    _RequiredAccessPreviewSummaryTypeDef, _OptionalAccessPreviewSummaryTypeDef
):
    pass

S3BucketAclGrantConfigurationOutputTypeDef = TypedDict(
    "S3BucketAclGrantConfigurationOutputTypeDef",
    {
        "permission": AclPermissionType,
        "grantee": AclGranteeOutputTypeDef,
    },
)

S3BucketAclGrantConfigurationTypeDef = TypedDict(
    "S3BucketAclGrantConfigurationTypeDef",
    {
        "permission": AclPermissionType,
        "grantee": AclGranteeTypeDef,
    },
)

_RequiredAnalyzerSummaryTypeDef = TypedDict(
    "_RequiredAnalyzerSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TypeType,
        "createdAt": datetime,
        "status": AnalyzerStatusType,
    },
)
_OptionalAnalyzerSummaryTypeDef = TypedDict(
    "_OptionalAnalyzerSummaryTypeDef",
    {
        "lastResourceAnalyzed": str,
        "lastResourceAnalyzedAt": datetime,
        "tags": Dict[str, str],
        "statusReason": StatusReasonTypeDef,
    },
    total=False,
)

class AnalyzerSummaryTypeDef(_RequiredAnalyzerSummaryTypeDef, _OptionalAnalyzerSummaryTypeDef):
    pass

ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "ruleName": str,
        "filter": Dict[str, CriterionOutputTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)

_RequiredCloudTrailDetailsTypeDef = TypedDict(
    "_RequiredCloudTrailDetailsTypeDef",
    {
        "trails": Sequence[TrailTypeDef],
        "accessRole": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalCloudTrailDetailsTypeDef = TypedDict(
    "_OptionalCloudTrailDetailsTypeDef",
    {
        "endTime": Union[datetime, str],
    },
    total=False,
)

class CloudTrailDetailsTypeDef(
    _RequiredCloudTrailDetailsTypeDef, _OptionalCloudTrailDetailsTypeDef
):
    pass

CloudTrailPropertiesTypeDef = TypedDict(
    "CloudTrailPropertiesTypeDef",
    {
        "trailProperties": List[TrailPropertiesTypeDef],
        "startTime": datetime,
        "endTime": datetime,
    },
)

CreateAccessPreviewResponseTypeDef = TypedDict(
    "CreateAccessPreviewResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAnalyzerResponseTypeDef = TypedDict(
    "CreateAnalyzerResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAnalyzedResourceResponseTypeDef = TypedDict(
    "GetAnalyzedResourceResponseTypeDef",
    {
        "resource": AnalyzedResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAnalyzedResourcesResponseTypeDef = TypedDict(
    "ListAnalyzedResourcesResponseTypeDef",
    {
        "analyzedResources": List[AnalyzedResourceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartPolicyGenerationResponseTypeDef = TypedDict(
    "StartPolicyGenerationResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateArchiveRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "filter": Mapping[str, CriterionTypeDef],
    },
)
_OptionalCreateArchiveRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateArchiveRuleRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateArchiveRuleRequestRequestTypeDef(
    _RequiredCreateArchiveRuleRequestRequestTypeDef, _OptionalCreateArchiveRuleRequestRequestTypeDef
):
    pass

InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef",
    {
        "ruleName": str,
        "filter": Mapping[str, CriterionTypeDef],
    },
)

_RequiredListAccessPreviewFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPreviewFindingsRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)
_OptionalListAccessPreviewFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPreviewFindingsRequestRequestTypeDef",
    {
        "filter": Mapping[str, CriterionTypeDef],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAccessPreviewFindingsRequestRequestTypeDef(
    _RequiredListAccessPreviewFindingsRequestRequestTypeDef,
    _OptionalListAccessPreviewFindingsRequestRequestTypeDef,
):
    pass

_RequiredUpdateArchiveRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "filter": Mapping[str, CriterionTypeDef],
    },
)
_OptionalUpdateArchiveRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateArchiveRuleRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateArchiveRuleRequestRequestTypeDef(
    _RequiredUpdateArchiveRuleRequestRequestTypeDef, _OptionalUpdateArchiveRuleRequestRequestTypeDef
):
    pass

_RequiredFindingSourceTypeDef = TypedDict(
    "_RequiredFindingSourceTypeDef",
    {
        "type": FindingSourceTypeType,
    },
)
_OptionalFindingSourceTypeDef = TypedDict(
    "_OptionalFindingSourceTypeDef",
    {
        "detail": FindingSourceDetailTypeDef,
    },
    total=False,
)

class FindingSourceTypeDef(_RequiredFindingSourceTypeDef, _OptionalFindingSourceTypeDef):
    pass

_RequiredJobDetailsTypeDef = TypedDict(
    "_RequiredJobDetailsTypeDef",
    {
        "jobId": str,
        "status": JobStatusType,
        "startedOn": datetime,
    },
)
_OptionalJobDetailsTypeDef = TypedDict(
    "_OptionalJobDetailsTypeDef",
    {
        "completedOn": datetime,
        "jobError": JobErrorTypeDef,
    },
    total=False,
)

class JobDetailsTypeDef(_RequiredJobDetailsTypeDef, _OptionalJobDetailsTypeDef):
    pass

_RequiredKmsGrantConfigurationOutputTypeDef = TypedDict(
    "_RequiredKmsGrantConfigurationOutputTypeDef",
    {
        "operations": List[KmsGrantOperationType],
        "granteePrincipal": str,
        "issuingAccount": str,
    },
)
_OptionalKmsGrantConfigurationOutputTypeDef = TypedDict(
    "_OptionalKmsGrantConfigurationOutputTypeDef",
    {
        "retiringPrincipal": str,
        "constraints": KmsGrantConstraintsOutputTypeDef,
    },
    total=False,
)

class KmsGrantConfigurationOutputTypeDef(
    _RequiredKmsGrantConfigurationOutputTypeDef, _OptionalKmsGrantConfigurationOutputTypeDef
):
    pass

_RequiredKmsGrantConfigurationTypeDef = TypedDict(
    "_RequiredKmsGrantConfigurationTypeDef",
    {
        "operations": Sequence[KmsGrantOperationType],
        "granteePrincipal": str,
        "issuingAccount": str,
    },
)
_OptionalKmsGrantConfigurationTypeDef = TypedDict(
    "_OptionalKmsGrantConfigurationTypeDef",
    {
        "retiringPrincipal": str,
        "constraints": KmsGrantConstraintsTypeDef,
    },
    total=False,
)

class KmsGrantConfigurationTypeDef(
    _RequiredKmsGrantConfigurationTypeDef, _OptionalKmsGrantConfigurationTypeDef
):
    pass

_RequiredListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef = TypedDict(
    "_RequiredListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)
_OptionalListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef = TypedDict(
    "_OptionalListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef",
    {
        "filter": Mapping[str, CriterionTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef(
    _RequiredListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef,
    _OptionalListAccessPreviewFindingsRequestListAccessPreviewFindingsPaginateTypeDef,
):
    pass

_RequiredListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef = TypedDict(
    "_RequiredListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef = TypedDict(
    "_OptionalListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef(
    _RequiredListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef,
    _OptionalListAccessPreviewsRequestListAccessPreviewsPaginateTypeDef,
):
    pass

_RequiredListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef = TypedDict(
    "_RequiredListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef = TypedDict(
    "_OptionalListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef",
    {
        "resourceType": ResourceTypeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef(
    _RequiredListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef,
    _OptionalListAnalyzedResourcesRequestListAnalyzedResourcesPaginateTypeDef,
):
    pass

ListAnalyzersRequestListAnalyzersPaginateTypeDef = TypedDict(
    "ListAnalyzersRequestListAnalyzersPaginateTypeDef",
    {
        "type": TypeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListArchiveRulesRequestListArchiveRulesPaginateTypeDef = TypedDict(
    "_RequiredListArchiveRulesRequestListArchiveRulesPaginateTypeDef",
    {
        "analyzerName": str,
    },
)
_OptionalListArchiveRulesRequestListArchiveRulesPaginateTypeDef = TypedDict(
    "_OptionalListArchiveRulesRequestListArchiveRulesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListArchiveRulesRequestListArchiveRulesPaginateTypeDef(
    _RequiredListArchiveRulesRequestListArchiveRulesPaginateTypeDef,
    _OptionalListArchiveRulesRequestListArchiveRulesPaginateTypeDef,
):
    pass

ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef = TypedDict(
    "ListPolicyGenerationsRequestListPolicyGenerationsPaginateTypeDef",
    {
        "principalArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredValidatePolicyRequestValidatePolicyPaginateTypeDef = TypedDict(
    "_RequiredValidatePolicyRequestValidatePolicyPaginateTypeDef",
    {
        "policyDocument": str,
        "policyType": PolicyTypeType,
    },
)
_OptionalValidatePolicyRequestValidatePolicyPaginateTypeDef = TypedDict(
    "_OptionalValidatePolicyRequestValidatePolicyPaginateTypeDef",
    {
        "locale": LocaleType,
        "validatePolicyResourceType": ValidatePolicyResourceTypeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ValidatePolicyRequestValidatePolicyPaginateTypeDef(
    _RequiredValidatePolicyRequestValidatePolicyPaginateTypeDef,
    _OptionalValidatePolicyRequestValidatePolicyPaginateTypeDef,
):
    pass

_RequiredListFindingsRequestListFindingsPaginateTypeDef = TypedDict(
    "_RequiredListFindingsRequestListFindingsPaginateTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListFindingsRequestListFindingsPaginateTypeDef = TypedDict(
    "_OptionalListFindingsRequestListFindingsPaginateTypeDef",
    {
        "filter": Mapping[str, CriterionTypeDef],
        "sort": SortCriteriaTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListFindingsRequestListFindingsPaginateTypeDef(
    _RequiredListFindingsRequestListFindingsPaginateTypeDef,
    _OptionalListFindingsRequestListFindingsPaginateTypeDef,
):
    pass

_RequiredListFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredListFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
    },
)
_OptionalListFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalListFindingsRequestRequestTypeDef",
    {
        "filter": Mapping[str, CriterionTypeDef],
        "sort": SortCriteriaTypeDef,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListFindingsRequestRequestTypeDef(
    _RequiredListFindingsRequestRequestTypeDef, _OptionalListFindingsRequestRequestTypeDef
):
    pass

ListPolicyGenerationsResponseTypeDef = TypedDict(
    "ListPolicyGenerationsResponseTypeDef",
    {
        "policyGenerations": List[PolicyGenerationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetworkOriginConfigurationOutputTypeDef = TypedDict(
    "NetworkOriginConfigurationOutputTypeDef",
    {
        "vpcConfiguration": VpcConfigurationOutputTypeDef,
        "internetConfiguration": Dict[str, Any],
    },
    total=False,
)

NetworkOriginConfigurationTypeDef = TypedDict(
    "NetworkOriginConfigurationTypeDef",
    {
        "vpcConfiguration": VpcConfigurationTypeDef,
        "internetConfiguration": Mapping[str, Any],
    },
    total=False,
)

PathElementTypeDef = TypedDict(
    "PathElementTypeDef",
    {
        "index": int,
        "key": str,
        "substring": SubstringTypeDef,
        "value": str,
    },
    total=False,
)

SpanTypeDef = TypedDict(
    "SpanTypeDef",
    {
        "start": PositionTypeDef,
        "end": PositionTypeDef,
    },
)

RdsDbClusterSnapshotConfigurationOutputTypeDef = TypedDict(
    "RdsDbClusterSnapshotConfigurationOutputTypeDef",
    {
        "attributes": Dict[str, RdsDbClusterSnapshotAttributeValueOutputTypeDef],
        "kmsKeyId": str,
    },
    total=False,
)

RdsDbClusterSnapshotConfigurationTypeDef = TypedDict(
    "RdsDbClusterSnapshotConfigurationTypeDef",
    {
        "attributes": Mapping[str, RdsDbClusterSnapshotAttributeValueTypeDef],
        "kmsKeyId": str,
    },
    total=False,
)

RdsDbSnapshotConfigurationOutputTypeDef = TypedDict(
    "RdsDbSnapshotConfigurationOutputTypeDef",
    {
        "attributes": Dict[str, RdsDbSnapshotAttributeValueOutputTypeDef],
        "kmsKeyId": str,
    },
    total=False,
)

RdsDbSnapshotConfigurationTypeDef = TypedDict(
    "RdsDbSnapshotConfigurationTypeDef",
    {
        "attributes": Mapping[str, RdsDbSnapshotAttributeValueTypeDef],
        "kmsKeyId": str,
    },
    total=False,
)

ListAccessPreviewsResponseTypeDef = TypedDict(
    "ListAccessPreviewsResponseTypeDef",
    {
        "accessPreviews": List[AccessPreviewSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAnalyzerResponseTypeDef = TypedDict(
    "GetAnalyzerResponseTypeDef",
    {
        "analyzer": AnalyzerSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAnalyzersResponseTypeDef = TypedDict(
    "ListAnalyzersResponseTypeDef",
    {
        "analyzers": List[AnalyzerSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetArchiveRuleResponseTypeDef = TypedDict(
    "GetArchiveRuleResponseTypeDef",
    {
        "archiveRule": ArchiveRuleSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListArchiveRulesResponseTypeDef = TypedDict(
    "ListArchiveRulesResponseTypeDef",
    {
        "archiveRules": List[ArchiveRuleSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredStartPolicyGenerationRequestRequestTypeDef = TypedDict(
    "_RequiredStartPolicyGenerationRequestRequestTypeDef",
    {
        "policyGenerationDetails": PolicyGenerationDetailsTypeDef,
    },
)
_OptionalStartPolicyGenerationRequestRequestTypeDef = TypedDict(
    "_OptionalStartPolicyGenerationRequestRequestTypeDef",
    {
        "cloudTrailDetails": CloudTrailDetailsTypeDef,
        "clientToken": str,
    },
    total=False,
)

class StartPolicyGenerationRequestRequestTypeDef(
    _RequiredStartPolicyGenerationRequestRequestTypeDef,
    _OptionalStartPolicyGenerationRequestRequestTypeDef,
):
    pass

_RequiredGeneratedPolicyPropertiesTypeDef = TypedDict(
    "_RequiredGeneratedPolicyPropertiesTypeDef",
    {
        "principalArn": str,
    },
)
_OptionalGeneratedPolicyPropertiesTypeDef = TypedDict(
    "_OptionalGeneratedPolicyPropertiesTypeDef",
    {
        "isComplete": bool,
        "cloudTrailProperties": CloudTrailPropertiesTypeDef,
    },
    total=False,
)

class GeneratedPolicyPropertiesTypeDef(
    _RequiredGeneratedPolicyPropertiesTypeDef, _OptionalGeneratedPolicyPropertiesTypeDef
):
    pass

_RequiredCreateAnalyzerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
        "type": TypeType,
    },
)
_OptionalCreateAnalyzerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnalyzerRequestRequestTypeDef",
    {
        "archiveRules": Sequence[InlineArchiveRuleTypeDef],
        "tags": Mapping[str, str],
        "clientToken": str,
    },
    total=False,
)

class CreateAnalyzerRequestRequestTypeDef(
    _RequiredCreateAnalyzerRequestRequestTypeDef, _OptionalCreateAnalyzerRequestRequestTypeDef
):
    pass

_RequiredAccessPreviewFindingTypeDef = TypedDict(
    "_RequiredAccessPreviewFindingTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "createdAt": datetime,
        "changeType": FindingChangeTypeType,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
    },
)
_OptionalAccessPreviewFindingTypeDef = TypedDict(
    "_OptionalAccessPreviewFindingTypeDef",
    {
        "existingFindingId": str,
        "existingFindingStatus": FindingStatusType,
        "principal": Dict[str, str],
        "action": List[str],
        "condition": Dict[str, str],
        "resource": str,
        "isPublic": bool,
        "error": str,
        "sources": List[FindingSourceTypeDef],
    },
    total=False,
)

class AccessPreviewFindingTypeDef(
    _RequiredAccessPreviewFindingTypeDef, _OptionalAccessPreviewFindingTypeDef
):
    pass

_RequiredFindingSummaryTypeDef = TypedDict(
    "_RequiredFindingSummaryTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
    },
)
_OptionalFindingSummaryTypeDef = TypedDict(
    "_OptionalFindingSummaryTypeDef",
    {
        "principal": Dict[str, str],
        "action": List[str],
        "resource": str,
        "isPublic": bool,
        "error": str,
        "sources": List[FindingSourceTypeDef],
    },
    total=False,
)

class FindingSummaryTypeDef(_RequiredFindingSummaryTypeDef, _OptionalFindingSummaryTypeDef):
    pass

_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "id": str,
        "resourceType": ResourceTypeType,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "analyzedAt": datetime,
        "updatedAt": datetime,
        "status": FindingStatusType,
        "resourceOwnerAccount": str,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "principal": Dict[str, str],
        "action": List[str],
        "resource": str,
        "isPublic": bool,
        "error": str,
        "sources": List[FindingSourceTypeDef],
    },
    total=False,
)

class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass

KmsKeyConfigurationOutputTypeDef = TypedDict(
    "KmsKeyConfigurationOutputTypeDef",
    {
        "keyPolicies": Dict[str, str],
        "grants": List[KmsGrantConfigurationOutputTypeDef],
    },
    total=False,
)

KmsKeyConfigurationTypeDef = TypedDict(
    "KmsKeyConfigurationTypeDef",
    {
        "keyPolicies": Mapping[str, str],
        "grants": Sequence[KmsGrantConfigurationTypeDef],
    },
    total=False,
)

S3AccessPointConfigurationOutputTypeDef = TypedDict(
    "S3AccessPointConfigurationOutputTypeDef",
    {
        "accessPointPolicy": str,
        "publicAccessBlock": S3PublicAccessBlockConfigurationOutputTypeDef,
        "networkOrigin": NetworkOriginConfigurationOutputTypeDef,
    },
    total=False,
)

S3AccessPointConfigurationTypeDef = TypedDict(
    "S3AccessPointConfigurationTypeDef",
    {
        "accessPointPolicy": str,
        "publicAccessBlock": S3PublicAccessBlockConfigurationTypeDef,
        "networkOrigin": NetworkOriginConfigurationTypeDef,
    },
    total=False,
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "path": List[PathElementTypeDef],
        "span": SpanTypeDef,
    },
)

_RequiredGeneratedPolicyResultTypeDef = TypedDict(
    "_RequiredGeneratedPolicyResultTypeDef",
    {
        "properties": GeneratedPolicyPropertiesTypeDef,
    },
)
_OptionalGeneratedPolicyResultTypeDef = TypedDict(
    "_OptionalGeneratedPolicyResultTypeDef",
    {
        "generatedPolicies": List[GeneratedPolicyTypeDef],
    },
    total=False,
)

class GeneratedPolicyResultTypeDef(
    _RequiredGeneratedPolicyResultTypeDef, _OptionalGeneratedPolicyResultTypeDef
):
    pass

ListAccessPreviewFindingsResponseTypeDef = TypedDict(
    "ListAccessPreviewFindingsResponseTypeDef",
    {
        "findings": List[AccessPreviewFindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findings": List[FindingSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetFindingResponseTypeDef = TypedDict(
    "GetFindingResponseTypeDef",
    {
        "finding": FindingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

S3BucketConfigurationOutputTypeDef = TypedDict(
    "S3BucketConfigurationOutputTypeDef",
    {
        "bucketPolicy": str,
        "bucketAclGrants": List[S3BucketAclGrantConfigurationOutputTypeDef],
        "bucketPublicAccessBlock": S3PublicAccessBlockConfigurationOutputTypeDef,
        "accessPoints": Dict[str, S3AccessPointConfigurationOutputTypeDef],
    },
    total=False,
)

S3BucketConfigurationTypeDef = TypedDict(
    "S3BucketConfigurationTypeDef",
    {
        "bucketPolicy": str,
        "bucketAclGrants": Sequence[S3BucketAclGrantConfigurationTypeDef],
        "bucketPublicAccessBlock": S3PublicAccessBlockConfigurationTypeDef,
        "accessPoints": Mapping[str, S3AccessPointConfigurationTypeDef],
    },
    total=False,
)

ValidatePolicyFindingTypeDef = TypedDict(
    "ValidatePolicyFindingTypeDef",
    {
        "findingDetails": str,
        "findingType": ValidatePolicyFindingTypeType,
        "issueCode": str,
        "learnMoreLink": str,
        "locations": List[LocationTypeDef],
    },
)

GetGeneratedPolicyResponseTypeDef = TypedDict(
    "GetGeneratedPolicyResponseTypeDef",
    {
        "jobDetails": JobDetailsTypeDef,
        "generatedPolicyResult": GeneratedPolicyResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConfigurationOutputTypeDef = TypedDict(
    "ConfigurationOutputTypeDef",
    {
        "ebsSnapshot": EbsSnapshotConfigurationOutputTypeDef,
        "ecrRepository": EcrRepositoryConfigurationOutputTypeDef,
        "iamRole": IamRoleConfigurationOutputTypeDef,
        "efsFileSystem": EfsFileSystemConfigurationOutputTypeDef,
        "kmsKey": KmsKeyConfigurationOutputTypeDef,
        "rdsDbClusterSnapshot": RdsDbClusterSnapshotConfigurationOutputTypeDef,
        "rdsDbSnapshot": RdsDbSnapshotConfigurationOutputTypeDef,
        "secretsManagerSecret": SecretsManagerSecretConfigurationOutputTypeDef,
        "s3Bucket": S3BucketConfigurationOutputTypeDef,
        "snsTopic": SnsTopicConfigurationOutputTypeDef,
        "sqsQueue": SqsQueueConfigurationOutputTypeDef,
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "ebsSnapshot": EbsSnapshotConfigurationTypeDef,
        "ecrRepository": EcrRepositoryConfigurationTypeDef,
        "iamRole": IamRoleConfigurationTypeDef,
        "efsFileSystem": EfsFileSystemConfigurationTypeDef,
        "kmsKey": KmsKeyConfigurationTypeDef,
        "rdsDbClusterSnapshot": RdsDbClusterSnapshotConfigurationTypeDef,
        "rdsDbSnapshot": RdsDbSnapshotConfigurationTypeDef,
        "secretsManagerSecret": SecretsManagerSecretConfigurationTypeDef,
        "s3Bucket": S3BucketConfigurationTypeDef,
        "snsTopic": SnsTopicConfigurationTypeDef,
        "sqsQueue": SqsQueueConfigurationTypeDef,
    },
    total=False,
)

ValidatePolicyResponseTypeDef = TypedDict(
    "ValidatePolicyResponseTypeDef",
    {
        "findings": List[ValidatePolicyFindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredAccessPreviewTypeDef = TypedDict(
    "_RequiredAccessPreviewTypeDef",
    {
        "id": str,
        "analyzerArn": str,
        "configurations": Dict[str, ConfigurationOutputTypeDef],
        "createdAt": datetime,
        "status": AccessPreviewStatusType,
    },
)
_OptionalAccessPreviewTypeDef = TypedDict(
    "_OptionalAccessPreviewTypeDef",
    {
        "statusReason": AccessPreviewStatusReasonTypeDef,
    },
    total=False,
)

class AccessPreviewTypeDef(_RequiredAccessPreviewTypeDef, _OptionalAccessPreviewTypeDef):
    pass

_RequiredCreateAccessPreviewRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPreviewRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "configurations": Mapping[str, ConfigurationTypeDef],
    },
)
_OptionalCreateAccessPreviewRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPreviewRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateAccessPreviewRequestRequestTypeDef(
    _RequiredCreateAccessPreviewRequestRequestTypeDef,
    _OptionalCreateAccessPreviewRequestRequestTypeDef,
):
    pass

GetAccessPreviewResponseTypeDef = TypedDict(
    "GetAccessPreviewResponseTypeDef",
    {
        "accessPreview": AccessPreviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
