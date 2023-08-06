"""
Type annotations for ecr service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr/type_defs/)

Usage::

    ```python
    from mypy_boto3_ecr.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    EncryptionTypeType,
    FindingSeverityType,
    ImageFailureCodeType,
    ImageTagMutabilityType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    LifecyclePolicyPreviewStatusType,
    ReplicationStatusType,
    ScanFrequencyType,
    ScanStatusType,
    ScanTypeType,
    TagStatusType,
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
    "AttributeTypeDef",
    "AuthorizationDataTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "ImageIdentifierTypeDef",
    "ImageIdentifierOutputTypeDef",
    "BatchGetRepositoryScanningConfigurationRequestRequestTypeDef",
    "RepositoryScanningConfigurationFailureTypeDef",
    "CompleteLayerUploadRequestRequestTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreatePullThroughCacheRuleRequestRequestTypeDef",
    "CreatePullThroughCacheRuleResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "ImageScanningConfigurationTypeDef",
    "TagTypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreTypeDef",
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeletePullThroughCacheRuleRequestRequestTypeDef",
    "DeletePullThroughCacheRuleResponseTypeDef",
    "DeleteRegistryPolicyResponseTypeDef",
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "ImageReplicationStatusTypeDef",
    "WaiterConfigTypeDef",
    "ImageScanStatusTypeDef",
    "DescribeImagesFilterTypeDef",
    "DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef",
    "DescribePullThroughCacheRulesRequestRequestTypeDef",
    "PullThroughCacheRuleTypeDef",
    "DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef",
    "DescribeRepositoriesRequestRequestTypeDef",
    "EncryptionConfigurationOutputTypeDef",
    "GetAuthorizationTokenRequestRequestTypeDef",
    "GetDownloadUrlForLayerRequestRequestTypeDef",
    "GetDownloadUrlForLayerResponseTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "GetLifecyclePolicyRequestRequestTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "GetRegistryPolicyResponseTypeDef",
    "GetRepositoryPolicyRequestRequestTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "ImageScanningConfigurationOutputTypeDef",
    "InitiateLayerUploadRequestRequestTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "ListImagesFilterTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "VulnerablePackageTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageRequestRequestTypeDef",
    "PutImageTagMutabilityRequestRequestTypeDef",
    "PutImageTagMutabilityResponseTypeDef",
    "PutLifecyclePolicyRequestRequestTypeDef",
    "PutLifecyclePolicyResponseTypeDef",
    "PutRegistryPolicyRequestRequestTypeDef",
    "PutRegistryPolicyResponseTypeDef",
    "RecommendationTypeDef",
    "ScanningRepositoryFilterOutputTypeDef",
    "ScanningRepositoryFilterTypeDef",
    "ReplicationDestinationOutputTypeDef",
    "ReplicationDestinationTypeDef",
    "RepositoryFilterOutputTypeDef",
    "RepositoryFilterTypeDef",
    "ResponseMetadataTypeDef",
    "SetRepositoryPolicyRequestRequestTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "StartLifecyclePolicyPreviewRequestRequestTypeDef",
    "StartLifecyclePolicyPreviewResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UploadLayerPartRequestRequestTypeDef",
    "UploadLayerPartResponseTypeDef",
    "ImageScanFindingTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "ResourceDetailsTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageRequestRequestTypeDef",
    "BatchGetImageRequestRequestTypeDef",
    "DescribeImageReplicationStatusRequestRequestTypeDef",
    "DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef",
    "DescribeImageScanFindingsRequestRequestTypeDef",
    "StartImageScanRequestRequestTypeDef",
    "ImageFailureTypeDef",
    "ImageTypeDef",
    "ListImagesResponseTypeDef",
    "PutImageScanningConfigurationRequestRequestTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CvssScoreDetailsTypeDef",
    "DescribeImageReplicationStatusResponseTypeDef",
    "DescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef",
    "StartImageScanResponseTypeDef",
    "DescribeImagesRequestDescribeImagesPaginateTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribePullThroughCacheRulesResponseTypeDef",
    "GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef",
    "GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef",
    "GetLifecyclePolicyPreviewRequestRequestTypeDef",
    "ImageDetailTypeDef",
    "PutImageScanningConfigurationResponseTypeDef",
    "RepositoryTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "ListImagesRequestListImagesPaginateTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "RemediationTypeDef",
    "RegistryScanningRuleOutputTypeDef",
    "RepositoryScanningConfigurationTypeDef",
    "RegistryScanningRuleTypeDef",
    "ReplicationRuleOutputTypeDef",
    "ReplicationRuleTypeDef",
    "ResourceTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "BatchGetImageResponseTypeDef",
    "PutImageResponseTypeDef",
    "ScoreDetailsTypeDef",
    "DescribeImagesResponseTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "GetLifecyclePolicyPreviewResponseTypeDef",
    "RegistryScanningConfigurationTypeDef",
    "BatchGetRepositoryScanningConfigurationResponseTypeDef",
    "PutRegistryScanningConfigurationRequestRequestTypeDef",
    "ReplicationConfigurationOutputTypeDef",
    "ReplicationConfigurationTypeDef",
    "EnhancedImageScanFindingTypeDef",
    "GetRegistryScanningConfigurationResponseTypeDef",
    "PutRegistryScanningConfigurationResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "PutReplicationConfigurationResponseTypeDef",
    "PutReplicationConfigurationRequestRequestTypeDef",
    "ImageScanFindingsTypeDef",
    "DescribeImageScanFindingsResponseTypeDef",
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "key": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "value": str,
    },
    total=False,
)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": str,
        "expiresAt": datetime,
        "proxyEndpoint": str,
    },
    total=False,
)

AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "architecture": str,
        "author": str,
        "imageHash": str,
        "imageTags": List[str],
        "platform": str,
        "pushedAt": datetime,
        "registry": str,
        "repositoryName": str,
    },
    total=False,
)

_RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigests": Sequence[str],
    },
)
_OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class BatchCheckLayerAvailabilityRequestRequestTypeDef(
    _RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef,
    _OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef,
):
    pass

LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": str,
        "failureCode": LayerFailureCodeType,
        "failureReason": str,
    },
    total=False,
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": str,
        "layerAvailability": LayerAvailabilityType,
        "layerSize": int,
        "mediaType": str,
    },
    total=False,
)

ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef",
    {
        "imageDigest": str,
        "imageTag": str,
    },
    total=False,
)

ImageIdentifierOutputTypeDef = TypedDict(
    "ImageIdentifierOutputTypeDef",
    {
        "imageDigest": str,
        "imageTag": str,
    },
    total=False,
)

BatchGetRepositoryScanningConfigurationRequestRequestTypeDef = TypedDict(
    "BatchGetRepositoryScanningConfigurationRequestRequestTypeDef",
    {
        "repositoryNames": Sequence[str],
    },
)

RepositoryScanningConfigurationFailureTypeDef = TypedDict(
    "RepositoryScanningConfigurationFailureTypeDef",
    {
        "repositoryName": str,
        "failureCode": Literal["REPOSITORY_NOT_FOUND"],
        "failureReason": str,
    },
    total=False,
)

_RequiredCompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "_RequiredCompleteLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "layerDigests": Sequence[str],
    },
)
_OptionalCompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "_OptionalCompleteLayerUploadRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class CompleteLayerUploadRequestRequestTypeDef(
    _RequiredCompleteLayerUploadRequestRequestTypeDef,
    _OptionalCompleteLayerUploadRequestRequestTypeDef,
):
    pass

CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
    },
)
_OptionalCreatePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePullThroughCacheRuleRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class CreatePullThroughCacheRuleRequestRequestTypeDef(
    _RequiredCreatePullThroughCacheRuleRequestRequestTypeDef,
    _OptionalCreatePullThroughCacheRuleRequestRequestTypeDef,
):
    pass

CreatePullThroughCacheRuleResponseTypeDef = TypedDict(
    "CreatePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "encryptionType": EncryptionTypeType,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "kmsKey": str,
    },
    total=False,
)

class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass

ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef",
    {
        "scanOnPush": bool,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": str,
        "reason": str,
    },
    total=False,
)

CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
        "source": str,
        "version": str,
    },
    total=False,
)

_RequiredDeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DeleteLifecyclePolicyRequestRequestTypeDef(
    _RequiredDeleteLifecyclePolicyRequestRequestTypeDef,
    _OptionalDeleteLifecyclePolicyRequestRequestTypeDef,
):
    pass

DeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
    },
)
_OptionalDeletePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePullThroughCacheRuleRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DeletePullThroughCacheRuleRequestRequestTypeDef(
    _RequiredDeletePullThroughCacheRuleRequestRequestTypeDef,
    _OptionalDeletePullThroughCacheRuleRequestRequestTypeDef,
):
    pass

DeletePullThroughCacheRuleResponseTypeDef = TypedDict(
    "DeletePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegistryPolicyResponseTypeDef = TypedDict(
    "DeleteRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DeleteRepositoryPolicyRequestRequestTypeDef(
    _RequiredDeleteRepositoryPolicyRequestRequestTypeDef,
    _OptionalDeleteRepositoryPolicyRequestRequestTypeDef,
):
    pass

DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryRequestRequestTypeDef",
    {
        "registryId": str,
        "force": bool,
    },
    total=False,
)

class DeleteRepositoryRequestRequestTypeDef(
    _RequiredDeleteRepositoryRequestRequestTypeDef, _OptionalDeleteRepositoryRequestRequestTypeDef
):
    pass

ImageReplicationStatusTypeDef = TypedDict(
    "ImageReplicationStatusTypeDef",
    {
        "region": str,
        "registryId": str,
        "status": ReplicationStatusType,
        "failureCode": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

ImageScanStatusTypeDef = TypedDict(
    "ImageScanStatusTypeDef",
    {
        "status": ScanStatusType,
        "description": str,
    },
    total=False,
)

DescribeImagesFilterTypeDef = TypedDict(
    "DescribeImagesFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef = TypedDict(
    "DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef",
    {
        "registryId": str,
        "ecrRepositoryPrefixes": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribePullThroughCacheRulesRequestRequestTypeDef = TypedDict(
    "DescribePullThroughCacheRulesRequestRequestTypeDef",
    {
        "registryId": str,
        "ecrRepositoryPrefixes": Sequence[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

PullThroughCacheRuleTypeDef = TypedDict(
    "PullThroughCacheRuleTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
    },
    total=False,
)

DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef = TypedDict(
    "DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef",
    {
        "registryId": str,
        "repositoryNames": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeRepositoriesRequestRequestTypeDef = TypedDict(
    "DescribeRepositoriesRequestRequestTypeDef",
    {
        "registryId": str,
        "repositoryNames": Sequence[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredEncryptionConfigurationOutputTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationOutputTypeDef",
    {
        "encryptionType": EncryptionTypeType,
    },
)
_OptionalEncryptionConfigurationOutputTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationOutputTypeDef",
    {
        "kmsKey": str,
    },
    total=False,
)

class EncryptionConfigurationOutputTypeDef(
    _RequiredEncryptionConfigurationOutputTypeDef, _OptionalEncryptionConfigurationOutputTypeDef
):
    pass

GetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "GetAuthorizationTokenRequestRequestTypeDef",
    {
        "registryIds": Sequence[str],
    },
    total=False,
)

_RequiredGetDownloadUrlForLayerRequestRequestTypeDef = TypedDict(
    "_RequiredGetDownloadUrlForLayerRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigest": str,
    },
)
_OptionalGetDownloadUrlForLayerRequestRequestTypeDef = TypedDict(
    "_OptionalGetDownloadUrlForLayerRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class GetDownloadUrlForLayerRequestRequestTypeDef(
    _RequiredGetDownloadUrlForLayerRequestRequestTypeDef,
    _OptionalGetDownloadUrlForLayerRequestRequestTypeDef,
):
    pass

GetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "GetDownloadUrlForLayerResponseTypeDef",
    {
        "downloadUrl": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "LifecyclePolicyPreviewFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

LifecyclePolicyPreviewSummaryTypeDef = TypedDict(
    "LifecyclePolicyPreviewSummaryTypeDef",
    {
        "expiringImageTotalCount": int,
    },
    total=False,
)

_RequiredGetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class GetLifecyclePolicyRequestRequestTypeDef(
    _RequiredGetLifecyclePolicyRequestRequestTypeDef,
    _OptionalGetLifecyclePolicyRequestRequestTypeDef,
):
    pass

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryPolicyResponseTypeDef = TypedDict(
    "GetRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class GetRepositoryPolicyRequestRequestTypeDef(
    _RequiredGetRepositoryPolicyRequestRequestTypeDef,
    _OptionalGetRepositoryPolicyRequestRequestTypeDef,
):
    pass

GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageScanFindingsSummaryTypeDef = TypedDict(
    "ImageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[FindingSeverityType, int],
    },
    total=False,
)

ImageScanningConfigurationOutputTypeDef = TypedDict(
    "ImageScanningConfigurationOutputTypeDef",
    {
        "scanOnPush": bool,
    },
    total=False,
)

_RequiredInitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "_RequiredInitiateLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalInitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "_OptionalInitiateLayerUploadRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class InitiateLayerUploadRequestRequestTypeDef(
    _RequiredInitiateLayerUploadRequestRequestTypeDef,
    _OptionalInitiateLayerUploadRequestRequestTypeDef,
):
    pass

InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecyclePolicyRuleActionTypeDef = TypedDict(
    "LifecyclePolicyRuleActionTypeDef",
    {
        "type": Literal["EXPIRE"],
    },
    total=False,
)

ListImagesFilterTypeDef = TypedDict(
    "ListImagesFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "arch": str,
        "epoch": int,
        "filePath": str,
        "name": str,
        "packageManager": str,
        "release": str,
        "sourceLayerHash": str,
        "version": str,
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

_RequiredPutImageRequestRequestTypeDef = TypedDict(
    "_RequiredPutImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageManifest": str,
    },
)
_OptionalPutImageRequestRequestTypeDef = TypedDict(
    "_OptionalPutImageRequestRequestTypeDef",
    {
        "registryId": str,
        "imageManifestMediaType": str,
        "imageTag": str,
        "imageDigest": str,
    },
    total=False,
)

class PutImageRequestRequestTypeDef(
    _RequiredPutImageRequestRequestTypeDef, _OptionalPutImageRequestRequestTypeDef
):
    pass

_RequiredPutImageTagMutabilityRequestRequestTypeDef = TypedDict(
    "_RequiredPutImageTagMutabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
    },
)
_OptionalPutImageTagMutabilityRequestRequestTypeDef = TypedDict(
    "_OptionalPutImageTagMutabilityRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class PutImageTagMutabilityRequestRequestTypeDef(
    _RequiredPutImageTagMutabilityRequestRequestTypeDef,
    _OptionalPutImageTagMutabilityRequestRequestTypeDef,
):
    pass

PutImageTagMutabilityResponseTypeDef = TypedDict(
    "PutImageTagMutabilityResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "lifecyclePolicyText": str,
    },
)
_OptionalPutLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutLifecyclePolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class PutLifecyclePolicyRequestRequestTypeDef(
    _RequiredPutLifecyclePolicyRequestRequestTypeDef,
    _OptionalPutLifecyclePolicyRequestRequestTypeDef,
):
    pass

PutLifecyclePolicyResponseTypeDef = TypedDict(
    "PutLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryPolicyRequestRequestTypeDef = TypedDict(
    "PutRegistryPolicyRequestRequestTypeDef",
    {
        "policyText": str,
    },
)

PutRegistryPolicyResponseTypeDef = TypedDict(
    "PutRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "url": str,
        "text": str,
    },
    total=False,
)

ScanningRepositoryFilterOutputTypeDef = TypedDict(
    "ScanningRepositoryFilterOutputTypeDef",
    {
        "filter": str,
        "filterType": Literal["WILDCARD"],
    },
)

ScanningRepositoryFilterTypeDef = TypedDict(
    "ScanningRepositoryFilterTypeDef",
    {
        "filter": str,
        "filterType": Literal["WILDCARD"],
    },
)

ReplicationDestinationOutputTypeDef = TypedDict(
    "ReplicationDestinationOutputTypeDef",
    {
        "region": str,
        "registryId": str,
    },
)

ReplicationDestinationTypeDef = TypedDict(
    "ReplicationDestinationTypeDef",
    {
        "region": str,
        "registryId": str,
    },
)

RepositoryFilterOutputTypeDef = TypedDict(
    "RepositoryFilterOutputTypeDef",
    {
        "filter": str,
        "filterType": Literal["PREFIX_MATCH"],
    },
)

RepositoryFilterTypeDef = TypedDict(
    "RepositoryFilterTypeDef",
    {
        "filter": str,
        "filterType": Literal["PREFIX_MATCH"],
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

_RequiredSetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredSetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "policyText": str,
    },
)
_OptionalSetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalSetRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
        "force": bool,
    },
    total=False,
)

class SetRepositoryPolicyRequestRequestTypeDef(
    _RequiredSetRepositoryPolicyRequestRequestTypeDef,
    _OptionalSetRepositoryPolicyRequestRequestTypeDef,
):
    pass

SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "_RequiredStartLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalStartLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "_OptionalStartLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "registryId": str,
        "lifecyclePolicyText": str,
    },
    total=False,
)

class StartLifecyclePolicyPreviewRequestRequestTypeDef(
    _RequiredStartLifecyclePolicyPreviewRequestRequestTypeDef,
    _OptionalStartLifecyclePolicyPreviewRequestRequestTypeDef,
):
    pass

StartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
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

_RequiredUploadLayerPartRequestRequestTypeDef = TypedDict(
    "_RequiredUploadLayerPartRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "partFirstByte": int,
        "partLastByte": int,
        "layerPartBlob": Union[str, bytes, IO[Any], StreamingBody],
    },
)
_OptionalUploadLayerPartRequestRequestTypeDef = TypedDict(
    "_OptionalUploadLayerPartRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class UploadLayerPartRequestRequestTypeDef(
    _RequiredUploadLayerPartRequestRequestTypeDef, _OptionalUploadLayerPartRequestRequestTypeDef
):
    pass

UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": FindingSeverityType,
        "attributes": List[AttributeTypeDef],
    },
    total=False,
)

GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": List[AuthorizationDataTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "awsEcrContainerImage": AwsEcrContainerImageDetailsTypeDef,
    },
    total=False,
)

BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List[LayerTypeDef],
        "failures": List[LayerFailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteImageRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
    },
)
_OptionalBatchDeleteImageRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteImageRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class BatchDeleteImageRequestRequestTypeDef(
    _RequiredBatchDeleteImageRequestRequestTypeDef, _OptionalBatchDeleteImageRequestRequestTypeDef
):
    pass

_RequiredBatchGetImageRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
    },
)
_OptionalBatchGetImageRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetImageRequestRequestTypeDef",
    {
        "registryId": str,
        "acceptedMediaTypes": Sequence[str],
    },
    total=False,
)

class BatchGetImageRequestRequestTypeDef(
    _RequiredBatchGetImageRequestRequestTypeDef, _OptionalBatchGetImageRequestRequestTypeDef
):
    pass

_RequiredDescribeImageReplicationStatusRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImageReplicationStatusRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
    },
)
_OptionalDescribeImageReplicationStatusRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImageReplicationStatusRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DescribeImageReplicationStatusRequestRequestTypeDef(
    _RequiredDescribeImageReplicationStatusRequestRequestTypeDef,
    _OptionalDescribeImageReplicationStatusRequestRequestTypeDef,
):
    pass

_RequiredDescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef = TypedDict(
    "_RequiredDescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
    },
)
_OptionalDescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef = TypedDict(
    "_OptionalDescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef",
    {
        "registryId": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef(
    _RequiredDescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef,
    _OptionalDescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef,
):
    pass

_RequiredDescribeImageScanFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImageScanFindingsRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
    },
)
_OptionalDescribeImageScanFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImageScanFindingsRequestRequestTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeImageScanFindingsRequestRequestTypeDef(
    _RequiredDescribeImageScanFindingsRequestRequestTypeDef,
    _OptionalDescribeImageScanFindingsRequestRequestTypeDef,
):
    pass

_RequiredStartImageScanRequestRequestTypeDef = TypedDict(
    "_RequiredStartImageScanRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
    },
)
_OptionalStartImageScanRequestRequestTypeDef = TypedDict(
    "_OptionalStartImageScanRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class StartImageScanRequestRequestTypeDef(
    _RequiredStartImageScanRequestRequestTypeDef, _OptionalStartImageScanRequestRequestTypeDef
):
    pass

ImageFailureTypeDef = TypedDict(
    "ImageFailureTypeDef",
    {
        "imageId": ImageIdentifierOutputTypeDef,
        "failureCode": ImageFailureCodeType,
        "failureReason": str,
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ImageIdentifierOutputTypeDef,
        "imageManifest": str,
        "imageManifestMediaType": str,
    },
    total=False,
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "imageIds": List[ImageIdentifierOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutImageScanningConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutImageScanningConfigurationRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageScanningConfiguration": ImageScanningConfigurationTypeDef,
    },
)
_OptionalPutImageScanningConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutImageScanningConfigurationRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class PutImageScanningConfigurationRequestRequestTypeDef(
    _RequiredPutImageScanningConfigurationRequestRequestTypeDef,
    _OptionalPutImageScanningConfigurationRequestRequestTypeDef,
):
    pass

_RequiredCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryRequestRequestTypeDef",
    {
        "registryId": str,
        "tags": Sequence[TagTypeDef],
        "imageTagMutability": ImageTagMutabilityType,
        "imageScanningConfiguration": ImageScanningConfigurationTypeDef,
        "encryptionConfiguration": EncryptionConfigurationTypeDef,
    },
    total=False,
)

class CreateRepositoryRequestRequestTypeDef(
    _RequiredCreateRepositoryRequestRequestTypeDef, _OptionalCreateRepositoryRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "adjustments": List[CvssScoreAdjustmentTypeDef],
        "score": float,
        "scoreSource": str,
        "scoringVector": str,
        "version": str,
    },
    total=False,
)

DescribeImageReplicationStatusResponseTypeDef = TypedDict(
    "DescribeImageReplicationStatusResponseTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierOutputTypeDef,
        "replicationStatuses": List[ImageReplicationStatusTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef = TypedDict(
    "_RequiredDescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef",
    {
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
    },
)
_OptionalDescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef = TypedDict(
    "_OptionalDescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef(
    _RequiredDescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef,
    _OptionalDescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef,
):
    pass

StartImageScanResponseTypeDef = TypedDict(
    "StartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ImageIdentifierOutputTypeDef,
        "imageScanStatus": ImageScanStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImagesRequestDescribeImagesPaginateTypeDef = TypedDict(
    "_RequiredDescribeImagesRequestDescribeImagesPaginateTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDescribeImagesRequestDescribeImagesPaginateTypeDef = TypedDict(
    "_OptionalDescribeImagesRequestDescribeImagesPaginateTypeDef",
    {
        "registryId": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
        "filter": DescribeImagesFilterTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class DescribeImagesRequestDescribeImagesPaginateTypeDef(
    _RequiredDescribeImagesRequestDescribeImagesPaginateTypeDef,
    _OptionalDescribeImagesRequestDescribeImagesPaginateTypeDef,
):
    pass

_RequiredDescribeImagesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDescribeImagesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImagesRequestRequestTypeDef",
    {
        "registryId": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
        "nextToken": str,
        "maxResults": int,
        "filter": DescribeImagesFilterTypeDef,
    },
    total=False,
)

class DescribeImagesRequestRequestTypeDef(
    _RequiredDescribeImagesRequestRequestTypeDef, _OptionalDescribeImagesRequestRequestTypeDef
):
    pass

DescribePullThroughCacheRulesResponseTypeDef = TypedDict(
    "DescribePullThroughCacheRulesResponseTypeDef",
    {
        "pullThroughCacheRules": List[PullThroughCacheRuleTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef",
    {
        "registryId": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
        "filter": LifecyclePolicyPreviewFilterTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef(
    _RequiredGetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef,
    _OptionalGetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef,
):
    pass

_RequiredGetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef",
    {
        "registryId": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
        "nextToken": str,
        "maxResults": int,
        "filter": LifecyclePolicyPreviewFilterTypeDef,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef(
    _RequiredGetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef,
    _OptionalGetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef,
):
    pass

_RequiredGetLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "registryId": str,
        "imageIds": Sequence[ImageIdentifierTypeDef],
        "nextToken": str,
        "maxResults": int,
        "filter": LifecyclePolicyPreviewFilterTypeDef,
    },
    total=False,
)

class GetLifecyclePolicyPreviewRequestRequestTypeDef(
    _RequiredGetLifecyclePolicyPreviewRequestRequestTypeDef,
    _OptionalGetLifecyclePolicyPreviewRequestRequestTypeDef,
):
    pass

ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": ImageScanStatusTypeDef,
        "imageScanFindingsSummary": ImageScanFindingsSummaryTypeDef,
        "imageManifestMediaType": str,
        "artifactMediaType": str,
        "lastRecordedPullTime": datetime,
    },
    total=False,
)

PutImageScanningConfigurationResponseTypeDef = TypedDict(
    "PutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": ImageScanningConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": ImageTagMutabilityType,
        "imageScanningConfiguration": ImageScanningConfigurationOutputTypeDef,
        "encryptionConfiguration": EncryptionConfigurationOutputTypeDef,
    },
    total=False,
)

LifecyclePolicyPreviewResultTypeDef = TypedDict(
    "LifecyclePolicyPreviewResultTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": LifecyclePolicyRuleActionTypeDef,
        "appliedRulePriority": int,
    },
    total=False,
)

_RequiredListImagesRequestListImagesPaginateTypeDef = TypedDict(
    "_RequiredListImagesRequestListImagesPaginateTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListImagesRequestListImagesPaginateTypeDef = TypedDict(
    "_OptionalListImagesRequestListImagesPaginateTypeDef",
    {
        "registryId": str,
        "filter": ListImagesFilterTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListImagesRequestListImagesPaginateTypeDef(
    _RequiredListImagesRequestListImagesPaginateTypeDef,
    _OptionalListImagesRequestListImagesPaginateTypeDef,
):
    pass

_RequiredListImagesRequestRequestTypeDef = TypedDict(
    "_RequiredListImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListImagesRequestRequestTypeDef = TypedDict(
    "_OptionalListImagesRequestRequestTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
        "filter": ListImagesFilterTypeDef,
    },
    total=False,
)

class ListImagesRequestRequestTypeDef(
    _RequiredListImagesRequestRequestTypeDef, _OptionalListImagesRequestRequestTypeDef
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PackageVulnerabilityDetailsTypeDef = TypedDict(
    "PackageVulnerabilityDetailsTypeDef",
    {
        "cvss": List[CvssScoreTypeDef],
        "referenceUrls": List[str],
        "relatedVulnerabilities": List[str],
        "source": str,
        "sourceUrl": str,
        "vendorCreatedAt": datetime,
        "vendorSeverity": str,
        "vendorUpdatedAt": datetime,
        "vulnerabilityId": str,
        "vulnerablePackages": List[VulnerablePackageTypeDef],
    },
    total=False,
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": RecommendationTypeDef,
    },
    total=False,
)

RegistryScanningRuleOutputTypeDef = TypedDict(
    "RegistryScanningRuleOutputTypeDef",
    {
        "scanFrequency": ScanFrequencyType,
        "repositoryFilters": List[ScanningRepositoryFilterOutputTypeDef],
    },
)

RepositoryScanningConfigurationTypeDef = TypedDict(
    "RepositoryScanningConfigurationTypeDef",
    {
        "repositoryArn": str,
        "repositoryName": str,
        "scanOnPush": bool,
        "scanFrequency": ScanFrequencyType,
        "appliedScanFilters": List[ScanningRepositoryFilterOutputTypeDef],
    },
    total=False,
)

RegistryScanningRuleTypeDef = TypedDict(
    "RegistryScanningRuleTypeDef",
    {
        "scanFrequency": ScanFrequencyType,
        "repositoryFilters": Sequence[ScanningRepositoryFilterTypeDef],
    },
)

_RequiredReplicationRuleOutputTypeDef = TypedDict(
    "_RequiredReplicationRuleOutputTypeDef",
    {
        "destinations": List[ReplicationDestinationOutputTypeDef],
    },
)
_OptionalReplicationRuleOutputTypeDef = TypedDict(
    "_OptionalReplicationRuleOutputTypeDef",
    {
        "repositoryFilters": List[RepositoryFilterOutputTypeDef],
    },
    total=False,
)

class ReplicationRuleOutputTypeDef(
    _RequiredReplicationRuleOutputTypeDef, _OptionalReplicationRuleOutputTypeDef
):
    pass

_RequiredReplicationRuleTypeDef = TypedDict(
    "_RequiredReplicationRuleTypeDef",
    {
        "destinations": Sequence[ReplicationDestinationTypeDef],
    },
)
_OptionalReplicationRuleTypeDef = TypedDict(
    "_OptionalReplicationRuleTypeDef",
    {
        "repositoryFilters": Sequence[RepositoryFilterTypeDef],
    },
    total=False,
)

class ReplicationRuleTypeDef(_RequiredReplicationRuleTypeDef, _OptionalReplicationRuleTypeDef):
    pass

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "details": ResourceDetailsTypeDef,
        "id": str,
        "tags": Dict[str, str],
        "type": str,
    },
    total=False,
)

BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {
        "imageIds": List[ImageIdentifierOutputTypeDef],
        "failures": List[ImageFailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetImageResponseTypeDef = TypedDict(
    "BatchGetImageResponseTypeDef",
    {
        "images": List[ImageTypeDef],
        "failures": List[ImageFailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef",
    {
        "image": ImageTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScoreDetailsTypeDef = TypedDict(
    "ScoreDetailsTypeDef",
    {
        "cvss": CvssScoreDetailsTypeDef,
    },
    total=False,
)

DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {
        "imageDetails": List[ImageDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef",
    {
        "repository": RepositoryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef",
    {
        "repository": RepositoryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List[RepositoryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "nextToken": str,
        "previewResults": List[LifecyclePolicyPreviewResultTypeDef],
        "summary": LifecyclePolicyPreviewSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistryScanningConfigurationTypeDef = TypedDict(
    "RegistryScanningConfigurationTypeDef",
    {
        "scanType": ScanTypeType,
        "rules": List[RegistryScanningRuleOutputTypeDef],
    },
    total=False,
)

BatchGetRepositoryScanningConfigurationResponseTypeDef = TypedDict(
    "BatchGetRepositoryScanningConfigurationResponseTypeDef",
    {
        "scanningConfigurations": List[RepositoryScanningConfigurationTypeDef],
        "failures": List[RepositoryScanningConfigurationFailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryScanningConfigurationRequestRequestTypeDef = TypedDict(
    "PutRegistryScanningConfigurationRequestRequestTypeDef",
    {
        "scanType": ScanTypeType,
        "rules": Sequence[RegistryScanningRuleTypeDef],
    },
    total=False,
)

ReplicationConfigurationOutputTypeDef = TypedDict(
    "ReplicationConfigurationOutputTypeDef",
    {
        "rules": List[ReplicationRuleOutputTypeDef],
    },
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "rules": Sequence[ReplicationRuleTypeDef],
    },
)

EnhancedImageScanFindingTypeDef = TypedDict(
    "EnhancedImageScanFindingTypeDef",
    {
        "awsAccountId": str,
        "description": str,
        "findingArn": str,
        "firstObservedAt": datetime,
        "lastObservedAt": datetime,
        "packageVulnerabilityDetails": PackageVulnerabilityDetailsTypeDef,
        "remediation": RemediationTypeDef,
        "resources": List[ResourceTypeDef],
        "score": float,
        "scoreDetails": ScoreDetailsTypeDef,
        "severity": str,
        "status": str,
        "title": str,
        "type": str,
        "updatedAt": datetime,
    },
    total=False,
)

GetRegistryScanningConfigurationResponseTypeDef = TypedDict(
    "GetRegistryScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "scanningConfiguration": RegistryScanningConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryScanningConfigurationResponseTypeDef = TypedDict(
    "PutRegistryScanningConfigurationResponseTypeDef",
    {
        "registryScanningConfiguration": RegistryScanningConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {
        "registryId": str,
        "replicationConfiguration": ReplicationConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutReplicationConfigurationResponseTypeDef = TypedDict(
    "PutReplicationConfigurationResponseTypeDef",
    {
        "replicationConfiguration": ReplicationConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutReplicationConfigurationRequestRequestTypeDef",
    {
        "replicationConfiguration": ReplicationConfigurationTypeDef,
    },
)

ImageScanFindingsTypeDef = TypedDict(
    "ImageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[FindingSeverityType, int],
        "findings": List[ImageScanFindingTypeDef],
        "enhancedFindings": List[EnhancedImageScanFindingTypeDef],
    },
    total=False,
)

DescribeImageScanFindingsResponseTypeDef = TypedDict(
    "DescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ImageIdentifierOutputTypeDef,
        "imageScanStatus": ImageScanStatusTypeDef,
        "imageScanFindings": ImageScanFindingsTypeDef,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
