"""
Type annotations for s3control service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/type_defs/)

Usage::

    ```python
    from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadOutputTypeDef

    data: AbortIncompleteMultipartUploadOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AsyncOperationNameType,
    BucketCannedACLType,
    BucketLocationConstraintType,
    BucketVersioningStatusType,
    DeleteMarkerReplicationStatusType,
    ExistingObjectReplicationStatusType,
    ExpirationStatusType,
    FormatType,
    JobManifestFieldNameType,
    JobManifestFormatType,
    JobReportScopeType,
    JobStatusType,
    MetricsStatusType,
    MFADeleteStatusType,
    MFADeleteType,
    MultiRegionAccessPointStatusType,
    NetworkOriginType,
    ObjectLambdaAccessPointAliasStatusType,
    ObjectLambdaAllowedFeatureType,
    ObjectLambdaTransformationConfigurationActionType,
    OperationNameType,
    ReplicaModificationsStatusType,
    ReplicationRuleStatusType,
    ReplicationStatusType,
    ReplicationStorageClassType,
    ReplicationTimeStatusType,
    RequestedJobStatusType,
    S3CannedAccessControlListType,
    S3ChecksumAlgorithmType,
    S3GlacierJobTierType,
    S3GranteeTypeIdentifierType,
    S3MetadataDirectiveType,
    S3ObjectLockLegalHoldStatusType,
    S3ObjectLockModeType,
    S3ObjectLockRetentionModeType,
    S3PermissionType,
    S3SSEAlgorithmType,
    S3StorageClassType,
    SseKmsEncryptedObjectsStatusType,
    TransitionStorageClassType,
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
    "AbortIncompleteMultipartUploadOutputTypeDef",
    "AbortIncompleteMultipartUploadTypeDef",
    "AccessControlTranslationOutputTypeDef",
    "AccessControlTranslationTypeDef",
    "VpcConfigurationOutputTypeDef",
    "ActivityMetricsOutputTypeDef",
    "AdvancedCostOptimizationMetricsOutputTypeDef",
    "AdvancedDataProtectionMetricsOutputTypeDef",
    "DetailedStatusCodesMetricsOutputTypeDef",
    "ActivityMetricsTypeDef",
    "AdvancedCostOptimizationMetricsTypeDef",
    "AdvancedDataProtectionMetricsTypeDef",
    "DetailedStatusCodesMetricsTypeDef",
    "AsyncErrorDetailsTypeDef",
    "DeleteMultiRegionAccessPointInputOutputTypeDef",
    "PutMultiRegionAccessPointPolicyInputOutputTypeDef",
    "AwsLambdaTransformationOutputTypeDef",
    "AwsLambdaTransformationTypeDef",
    "CloudWatchMetricsOutputTypeDef",
    "CloudWatchMetricsTypeDef",
    "ObjectLambdaAccessPointAliasTypeDef",
    "ResponseMetadataTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "VpcConfigurationTypeDef",
    "CreateBucketConfigurationTypeDef",
    "JobReportTypeDef",
    "S3TagTypeDef",
    "PublicAccessBlockConfigurationOutputTypeDef",
    "RegionOutputTypeDef",
    "RegionTypeDef",
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    "DeleteAccessPointRequestRequestTypeDef",
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    "DeleteBucketPolicyRequestRequestTypeDef",
    "DeleteBucketReplicationRequestRequestTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketTaggingRequestRequestTypeDef",
    "DeleteJobTaggingRequestRequestTypeDef",
    "DeleteMarkerReplicationOutputTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeleteMultiRegionAccessPointInputTypeDef",
    "DeletePublicAccessBlockRequestRequestTypeDef",
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeMultiRegionAccessPointOperationRequestRequestTypeDef",
    "EncryptionConfigurationOutputTypeDef",
    "EncryptionConfigurationTypeDef",
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    "ExcludeOutputTypeDef",
    "ExcludeTypeDef",
    "ExistingObjectReplicationOutputTypeDef",
    "ExistingObjectReplicationTypeDef",
    "SSEKMSEncryptionOutputTypeDef",
    "SSEKMSEncryptionTypeDef",
    "GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointPolicyRequestRequestTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef",
    "PolicyStatusTypeDef",
    "GetAccessPointPolicyStatusRequestRequestTypeDef",
    "GetAccessPointRequestRequestTypeDef",
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    "GetBucketPolicyRequestRequestTypeDef",
    "GetBucketReplicationRequestRequestTypeDef",
    "GetBucketRequestRequestTypeDef",
    "GetBucketTaggingRequestRequestTypeDef",
    "S3TagOutputTypeDef",
    "GetBucketVersioningRequestRequestTypeDef",
    "GetJobTaggingRequestRequestTypeDef",
    "GetMultiRegionAccessPointPolicyRequestRequestTypeDef",
    "GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef",
    "GetMultiRegionAccessPointRequestRequestTypeDef",
    "GetMultiRegionAccessPointRoutesRequestRequestTypeDef",
    "MultiRegionAccessPointRouteOutputTypeDef",
    "GetPublicAccessBlockRequestRequestTypeDef",
    "GetStorageLensConfigurationRequestRequestTypeDef",
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    "StorageLensTagOutputTypeDef",
    "IncludeOutputTypeDef",
    "IncludeTypeDef",
    "JobFailureTypeDef",
    "JobReportOutputTypeDef",
    "JobManifestGeneratorFilterOutputTypeDef",
    "JobManifestGeneratorFilterTypeDef",
    "JobManifestLocationOutputTypeDef",
    "JobManifestLocationTypeDef",
    "JobManifestSpecOutputTypeDef",
    "JobManifestSpecTypeDef",
    "LambdaInvokeOperationOutputTypeDef",
    "S3InitiateRestoreObjectOperationOutputTypeDef",
    "LambdaInvokeOperationTypeDef",
    "S3InitiateRestoreObjectOperationTypeDef",
    "JobTimersTypeDef",
    "LifecycleExpirationOutputTypeDef",
    "LifecycleExpirationTypeDef",
    "NoncurrentVersionExpirationOutputTypeDef",
    "NoncurrentVersionTransitionOutputTypeDef",
    "TransitionOutputTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "TransitionTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccessPointsForObjectLambdaRequestRequestTypeDef",
    "ListAccessPointsRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListMultiRegionAccessPointsRequestRequestTypeDef",
    "ListRegionalBucketsRequestRequestTypeDef",
    "RegionalBucketTypeDef",
    "ListStorageLensConfigurationEntryTypeDef",
    "ListStorageLensConfigurationsRequestRequestTypeDef",
    "ReplicationTimeValueOutputTypeDef",
    "ReplicationTimeValueTypeDef",
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    "MultiRegionAccessPointRegionalResponseTypeDef",
    "RegionReportTypeDef",
    "MultiRegionAccessPointRouteTypeDef",
    "SelectionCriteriaOutputTypeDef",
    "SelectionCriteriaTypeDef",
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointPolicyRequestRequestTypeDef",
    "PutBucketPolicyRequestRequestTypeDef",
    "VersioningConfigurationTypeDef",
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    "StorageLensTagTypeDef",
    "ReplicaModificationsOutputTypeDef",
    "ReplicaModificationsTypeDef",
    "S3ObjectOwnerOutputTypeDef",
    "S3ObjectOwnerTypeDef",
    "S3ObjectMetadataOutputTypeDef",
    "S3ObjectMetadataTypeDef",
    "S3GranteeOutputTypeDef",
    "S3GranteeTypeDef",
    "S3ObjectLockLegalHoldOutputTypeDef",
    "S3ObjectLockLegalHoldTypeDef",
    "S3RetentionOutputTypeDef",
    "S3RetentionTypeDef",
    "SSEKMSOutputTypeDef",
    "SSEKMSTypeDef",
    "SseKmsEncryptedObjectsOutputTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StorageLensAwsOrgOutputTypeDef",
    "StorageLensAwsOrgTypeDef",
    "UpdateJobPriorityRequestRequestTypeDef",
    "UpdateJobStatusRequestRequestTypeDef",
    "AccessPointTypeDef",
    "ObjectLambdaContentTransformationOutputTypeDef",
    "ObjectLambdaContentTransformationTypeDef",
    "ObjectLambdaAccessPointTypeDef",
    "CreateAccessPointForObjectLambdaResultTypeDef",
    "CreateAccessPointResultTypeDef",
    "CreateBucketResultTypeDef",
    "CreateJobResultTypeDef",
    "CreateMultiRegionAccessPointResultTypeDef",
    "DeleteMultiRegionAccessPointResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyResultTypeDef",
    "GetBucketPolicyResultTypeDef",
    "GetBucketResultTypeDef",
    "GetBucketVersioningResultTypeDef",
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusResultTypeDef",
    "PutPublicAccessBlockRequestRequestTypeDef",
    "CreateAccessPointRequestRequestTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "PutJobTaggingRequestRequestTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "S3SetObjectTaggingOperationTypeDef",
    "TaggingTypeDef",
    "GetAccessPointForObjectLambdaResultTypeDef",
    "GetAccessPointResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "CreateMultiRegionAccessPointInputOutputTypeDef",
    "CreateMultiRegionAccessPointInputTypeDef",
    "DeleteMultiRegionAccessPointRequestRequestTypeDef",
    "GeneratedManifestEncryptionOutputTypeDef",
    "GeneratedManifestEncryptionTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyStatusResultTypeDef",
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    "GetBucketTaggingResultTypeDef",
    "GetJobTaggingResultTypeDef",
    "LifecycleRuleAndOperatorOutputTypeDef",
    "ReplicationRuleAndOperatorOutputTypeDef",
    "S3SetObjectTaggingOperationOutputTypeDef",
    "GetMultiRegionAccessPointRoutesResultTypeDef",
    "GetStorageLensConfigurationTaggingResultTypeDef",
    "S3GeneratedManifestDescriptorTypeDef",
    "JobManifestOutputTypeDef",
    "JobManifestTypeDef",
    "JobProgressSummaryTypeDef",
    "ListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef",
    "ListRegionalBucketsResultTypeDef",
    "ListStorageLensConfigurationsResultTypeDef",
    "MetricsOutputTypeDef",
    "ReplicationTimeOutputTypeDef",
    "MetricsTypeDef",
    "ReplicationTimeTypeDef",
    "MultiRegionAccessPointPolicyDocumentTypeDef",
    "MultiRegionAccessPointsAsyncResponseTypeDef",
    "MultiRegionAccessPointReportTypeDef",
    "SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef",
    "PrefixLevelStorageMetricsOutputTypeDef",
    "PrefixLevelStorageMetricsTypeDef",
    "PutBucketVersioningRequestRequestTypeDef",
    "PutMultiRegionAccessPointPolicyRequestRequestTypeDef",
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    "S3GrantOutputTypeDef",
    "S3GrantTypeDef",
    "S3SetObjectLegalHoldOperationOutputTypeDef",
    "S3SetObjectLegalHoldOperationTypeDef",
    "S3SetObjectRetentionOperationOutputTypeDef",
    "S3SetObjectRetentionOperationTypeDef",
    "StorageLensDataExportEncryptionOutputTypeDef",
    "StorageLensDataExportEncryptionTypeDef",
    "SourceSelectionCriteriaOutputTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "ListAccessPointsResultTypeDef",
    "ObjectLambdaTransformationConfigurationOutputTypeDef",
    "ObjectLambdaTransformationConfigurationTypeDef",
    "ListAccessPointsForObjectLambdaResultTypeDef",
    "LifecycleRuleFilterTypeDef",
    "ReplicationRuleFilterTypeDef",
    "PutBucketTaggingRequestRequestTypeDef",
    "AsyncRequestParametersTypeDef",
    "CreateMultiRegionAccessPointRequestRequestTypeDef",
    "S3ManifestOutputLocationOutputTypeDef",
    "S3ManifestOutputLocationTypeDef",
    "LifecycleRuleFilterOutputTypeDef",
    "ReplicationRuleFilterOutputTypeDef",
    "JobListDescriptorTypeDef",
    "DestinationOutputTypeDef",
    "DestinationTypeDef",
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    "AsyncResponseDetailsTypeDef",
    "GetMultiRegionAccessPointResultTypeDef",
    "ListMultiRegionAccessPointsResultTypeDef",
    "PrefixLevelOutputTypeDef",
    "PrefixLevelTypeDef",
    "S3AccessControlListOutputTypeDef",
    "S3CopyObjectOperationOutputTypeDef",
    "S3AccessControlListTypeDef",
    "S3CopyObjectOperationTypeDef",
    "S3BucketDestinationOutputTypeDef",
    "S3BucketDestinationTypeDef",
    "ObjectLambdaConfigurationOutputTypeDef",
    "ObjectLambdaConfigurationTypeDef",
    "LifecycleRuleTypeDef",
    "S3JobManifestGeneratorOutputTypeDef",
    "S3JobManifestGeneratorTypeDef",
    "LifecycleRuleOutputTypeDef",
    "ListJobsResultTypeDef",
    "ReplicationRuleOutputTypeDef",
    "ReplicationRuleTypeDef",
    "AsyncOperationTypeDef",
    "BucketLevelOutputTypeDef",
    "BucketLevelTypeDef",
    "S3AccessControlPolicyOutputTypeDef",
    "S3AccessControlPolicyTypeDef",
    "StorageLensDataExportOutputTypeDef",
    "StorageLensDataExportTypeDef",
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "LifecycleConfigurationTypeDef",
    "JobManifestGeneratorOutputTypeDef",
    "JobManifestGeneratorTypeDef",
    "GetBucketLifecycleConfigurationResultTypeDef",
    "ReplicationConfigurationOutputTypeDef",
    "ReplicationConfigurationTypeDef",
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    "AccountLevelOutputTypeDef",
    "AccountLevelTypeDef",
    "S3SetObjectAclOperationOutputTypeDef",
    "S3SetObjectAclOperationTypeDef",
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    "GetBucketReplicationResultTypeDef",
    "PutBucketReplicationRequestRequestTypeDef",
    "StorageLensConfigurationOutputTypeDef",
    "StorageLensConfigurationTypeDef",
    "JobOperationOutputTypeDef",
    "JobOperationTypeDef",
    "GetStorageLensConfigurationResultTypeDef",
    "PutStorageLensConfigurationRequestRequestTypeDef",
    "JobDescriptorTypeDef",
    "CreateJobRequestRequestTypeDef",
    "DescribeJobResultTypeDef",
)

AbortIncompleteMultipartUploadOutputTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadOutputTypeDef",
    {
        "DaysAfterInitiation": int,
    },
    total=False,
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": int,
    },
    total=False,
)

AccessControlTranslationOutputTypeDef = TypedDict(
    "AccessControlTranslationOutputTypeDef",
    {
        "Owner": Literal["Destination"],
    },
)

AccessControlTranslationTypeDef = TypedDict(
    "AccessControlTranslationTypeDef",
    {
        "Owner": Literal["Destination"],
    },
)

VpcConfigurationOutputTypeDef = TypedDict(
    "VpcConfigurationOutputTypeDef",
    {
        "VpcId": str,
    },
)

ActivityMetricsOutputTypeDef = TypedDict(
    "ActivityMetricsOutputTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

AdvancedCostOptimizationMetricsOutputTypeDef = TypedDict(
    "AdvancedCostOptimizationMetricsOutputTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

AdvancedDataProtectionMetricsOutputTypeDef = TypedDict(
    "AdvancedDataProtectionMetricsOutputTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

DetailedStatusCodesMetricsOutputTypeDef = TypedDict(
    "DetailedStatusCodesMetricsOutputTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

ActivityMetricsTypeDef = TypedDict(
    "ActivityMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

AdvancedCostOptimizationMetricsTypeDef = TypedDict(
    "AdvancedCostOptimizationMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

AdvancedDataProtectionMetricsTypeDef = TypedDict(
    "AdvancedDataProtectionMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

DetailedStatusCodesMetricsTypeDef = TypedDict(
    "DetailedStatusCodesMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

AsyncErrorDetailsTypeDef = TypedDict(
    "AsyncErrorDetailsTypeDef",
    {
        "Code": str,
        "Message": str,
        "Resource": str,
        "RequestId": str,
    },
    total=False,
)

DeleteMultiRegionAccessPointInputOutputTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointInputOutputTypeDef",
    {
        "Name": str,
    },
)

PutMultiRegionAccessPointPolicyInputOutputTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyInputOutputTypeDef",
    {
        "Name": str,
        "Policy": str,
    },
)

_RequiredAwsLambdaTransformationOutputTypeDef = TypedDict(
    "_RequiredAwsLambdaTransformationOutputTypeDef",
    {
        "FunctionArn": str,
    },
)
_OptionalAwsLambdaTransformationOutputTypeDef = TypedDict(
    "_OptionalAwsLambdaTransformationOutputTypeDef",
    {
        "FunctionPayload": str,
    },
    total=False,
)


class AwsLambdaTransformationOutputTypeDef(
    _RequiredAwsLambdaTransformationOutputTypeDef, _OptionalAwsLambdaTransformationOutputTypeDef
):
    pass


_RequiredAwsLambdaTransformationTypeDef = TypedDict(
    "_RequiredAwsLambdaTransformationTypeDef",
    {
        "FunctionArn": str,
    },
)
_OptionalAwsLambdaTransformationTypeDef = TypedDict(
    "_OptionalAwsLambdaTransformationTypeDef",
    {
        "FunctionPayload": str,
    },
    total=False,
)


class AwsLambdaTransformationTypeDef(
    _RequiredAwsLambdaTransformationTypeDef, _OptionalAwsLambdaTransformationTypeDef
):
    pass


CloudWatchMetricsOutputTypeDef = TypedDict(
    "CloudWatchMetricsOutputTypeDef",
    {
        "IsEnabled": bool,
    },
)

CloudWatchMetricsTypeDef = TypedDict(
    "CloudWatchMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
)

ObjectLambdaAccessPointAliasTypeDef = TypedDict(
    "ObjectLambdaAccessPointAliasTypeDef",
    {
        "Value": str,
        "Status": ObjectLambdaAccessPointAliasStatusType,
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

PublicAccessBlockConfigurationTypeDef = TypedDict(
    "PublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "VpcId": str,
    },
)

CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
    },
    total=False,
)

_RequiredJobReportTypeDef = TypedDict(
    "_RequiredJobReportTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalJobReportTypeDef = TypedDict(
    "_OptionalJobReportTypeDef",
    {
        "Bucket": str,
        "Format": Literal["Report_CSV_20180820"],
        "Prefix": str,
        "ReportScope": JobReportScopeType,
    },
    total=False,
)


class JobReportTypeDef(_RequiredJobReportTypeDef, _OptionalJobReportTypeDef):
    pass


S3TagTypeDef = TypedDict(
    "S3TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

PublicAccessBlockConfigurationOutputTypeDef = TypedDict(
    "PublicAccessBlockConfigurationOutputTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

_RequiredRegionOutputTypeDef = TypedDict(
    "_RequiredRegionOutputTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalRegionOutputTypeDef = TypedDict(
    "_OptionalRegionOutputTypeDef",
    {
        "BucketAccountId": str,
    },
    total=False,
)


class RegionOutputTypeDef(_RequiredRegionOutputTypeDef, _OptionalRegionOutputTypeDef):
    pass


_RequiredRegionTypeDef = TypedDict(
    "_RequiredRegionTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalRegionTypeDef = TypedDict(
    "_OptionalRegionTypeDef",
    {
        "BucketAccountId": str,
    },
    total=False,
)


class RegionTypeDef(_RequiredRegionTypeDef, _OptionalRegionTypeDef):
    pass


DeleteAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketPolicyRequestRequestTypeDef = TypedDict(
    "DeleteBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketReplicationRequestRequestTypeDef = TypedDict(
    "DeleteBucketReplicationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketRequestRequestTypeDef = TypedDict(
    "DeleteBucketRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketTaggingRequestRequestTypeDef = TypedDict(
    "DeleteBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteJobTaggingRequestRequestTypeDef = TypedDict(
    "DeleteJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

DeleteMarkerReplicationOutputTypeDef = TypedDict(
    "DeleteMarkerReplicationOutputTypeDef",
    {
        "Status": DeleteMarkerReplicationStatusType,
    },
)

DeleteMarkerReplicationTypeDef = TypedDict(
    "DeleteMarkerReplicationTypeDef",
    {
        "Status": DeleteMarkerReplicationStatusType,
    },
)

DeleteMultiRegionAccessPointInputTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointInputTypeDef",
    {
        "Name": str,
    },
)

DeletePublicAccessBlockRequestRequestTypeDef = TypedDict(
    "DeletePublicAccessBlockRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

DeleteStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

DescribeMultiRegionAccessPointOperationRequestRequestTypeDef = TypedDict(
    "DescribeMultiRegionAccessPointOperationRequestRequestTypeDef",
    {
        "AccountId": str,
        "RequestTokenARN": str,
    },
)

EncryptionConfigurationOutputTypeDef = TypedDict(
    "EncryptionConfigurationOutputTypeDef",
    {
        "ReplicaKmsKeyID": str,
    },
    total=False,
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "ReplicaKmsKeyID": str,
    },
    total=False,
)

EstablishedMultiRegionAccessPointPolicyTypeDef = TypedDict(
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

ExcludeOutputTypeDef = TypedDict(
    "ExcludeOutputTypeDef",
    {
        "Buckets": List[str],
        "Regions": List[str],
    },
    total=False,
)

ExcludeTypeDef = TypedDict(
    "ExcludeTypeDef",
    {
        "Buckets": Sequence[str],
        "Regions": Sequence[str],
    },
    total=False,
)

ExistingObjectReplicationOutputTypeDef = TypedDict(
    "ExistingObjectReplicationOutputTypeDef",
    {
        "Status": ExistingObjectReplicationStatusType,
    },
)

ExistingObjectReplicationTypeDef = TypedDict(
    "ExistingObjectReplicationTypeDef",
    {
        "Status": ExistingObjectReplicationStatusType,
    },
)

SSEKMSEncryptionOutputTypeDef = TypedDict(
    "SSEKMSEncryptionOutputTypeDef",
    {
        "KeyId": str,
    },
)

SSEKMSEncryptionTypeDef = TypedDict(
    "SSEKMSEncryptionTypeDef",
    {
        "KeyId": str,
    },
)

GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

PolicyStatusTypeDef = TypedDict(
    "PolicyStatusTypeDef",
    {
        "IsPublic": bool,
    },
    total=False,
)

GetAccessPointPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointRequestRequestTypeDef = TypedDict(
    "GetAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketPolicyRequestRequestTypeDef = TypedDict(
    "GetBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketReplicationRequestRequestTypeDef = TypedDict(
    "GetBucketReplicationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketRequestRequestTypeDef = TypedDict(
    "GetBucketRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketTaggingRequestRequestTypeDef = TypedDict(
    "GetBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

S3TagOutputTypeDef = TypedDict(
    "S3TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

GetBucketVersioningRequestRequestTypeDef = TypedDict(
    "GetBucketVersioningRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetJobTaggingRequestRequestTypeDef = TypedDict(
    "GetJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

GetMultiRegionAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointRoutesRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointRoutesRequestRequestTypeDef",
    {
        "AccountId": str,
        "Mrap": str,
    },
)

_RequiredMultiRegionAccessPointRouteOutputTypeDef = TypedDict(
    "_RequiredMultiRegionAccessPointRouteOutputTypeDef",
    {
        "TrafficDialPercentage": int,
    },
)
_OptionalMultiRegionAccessPointRouteOutputTypeDef = TypedDict(
    "_OptionalMultiRegionAccessPointRouteOutputTypeDef",
    {
        "Bucket": str,
        "Region": str,
    },
    total=False,
)


class MultiRegionAccessPointRouteOutputTypeDef(
    _RequiredMultiRegionAccessPointRouteOutputTypeDef,
    _OptionalMultiRegionAccessPointRouteOutputTypeDef,
):
    pass


GetPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "GetPublicAccessBlockRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

GetStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

StorageLensTagOutputTypeDef = TypedDict(
    "StorageLensTagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

IncludeOutputTypeDef = TypedDict(
    "IncludeOutputTypeDef",
    {
        "Buckets": List[str],
        "Regions": List[str],
    },
    total=False,
)

IncludeTypeDef = TypedDict(
    "IncludeTypeDef",
    {
        "Buckets": Sequence[str],
        "Regions": Sequence[str],
    },
    total=False,
)

JobFailureTypeDef = TypedDict(
    "JobFailureTypeDef",
    {
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

_RequiredJobReportOutputTypeDef = TypedDict(
    "_RequiredJobReportOutputTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalJobReportOutputTypeDef = TypedDict(
    "_OptionalJobReportOutputTypeDef",
    {
        "Bucket": str,
        "Format": Literal["Report_CSV_20180820"],
        "Prefix": str,
        "ReportScope": JobReportScopeType,
    },
    total=False,
)


class JobReportOutputTypeDef(_RequiredJobReportOutputTypeDef, _OptionalJobReportOutputTypeDef):
    pass


JobManifestGeneratorFilterOutputTypeDef = TypedDict(
    "JobManifestGeneratorFilterOutputTypeDef",
    {
        "EligibleForReplication": bool,
        "CreatedAfter": datetime,
        "CreatedBefore": datetime,
        "ObjectReplicationStatuses": List[ReplicationStatusType],
    },
    total=False,
)

JobManifestGeneratorFilterTypeDef = TypedDict(
    "JobManifestGeneratorFilterTypeDef",
    {
        "EligibleForReplication": bool,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "ObjectReplicationStatuses": Sequence[ReplicationStatusType],
    },
    total=False,
)

_RequiredJobManifestLocationOutputTypeDef = TypedDict(
    "_RequiredJobManifestLocationOutputTypeDef",
    {
        "ObjectArn": str,
        "ETag": str,
    },
)
_OptionalJobManifestLocationOutputTypeDef = TypedDict(
    "_OptionalJobManifestLocationOutputTypeDef",
    {
        "ObjectVersionId": str,
    },
    total=False,
)


class JobManifestLocationOutputTypeDef(
    _RequiredJobManifestLocationOutputTypeDef, _OptionalJobManifestLocationOutputTypeDef
):
    pass


_RequiredJobManifestLocationTypeDef = TypedDict(
    "_RequiredJobManifestLocationTypeDef",
    {
        "ObjectArn": str,
        "ETag": str,
    },
)
_OptionalJobManifestLocationTypeDef = TypedDict(
    "_OptionalJobManifestLocationTypeDef",
    {
        "ObjectVersionId": str,
    },
    total=False,
)


class JobManifestLocationTypeDef(
    _RequiredJobManifestLocationTypeDef, _OptionalJobManifestLocationTypeDef
):
    pass


_RequiredJobManifestSpecOutputTypeDef = TypedDict(
    "_RequiredJobManifestSpecOutputTypeDef",
    {
        "Format": JobManifestFormatType,
    },
)
_OptionalJobManifestSpecOutputTypeDef = TypedDict(
    "_OptionalJobManifestSpecOutputTypeDef",
    {
        "Fields": List[JobManifestFieldNameType],
    },
    total=False,
)


class JobManifestSpecOutputTypeDef(
    _RequiredJobManifestSpecOutputTypeDef, _OptionalJobManifestSpecOutputTypeDef
):
    pass


_RequiredJobManifestSpecTypeDef = TypedDict(
    "_RequiredJobManifestSpecTypeDef",
    {
        "Format": JobManifestFormatType,
    },
)
_OptionalJobManifestSpecTypeDef = TypedDict(
    "_OptionalJobManifestSpecTypeDef",
    {
        "Fields": Sequence[JobManifestFieldNameType],
    },
    total=False,
)


class JobManifestSpecTypeDef(_RequiredJobManifestSpecTypeDef, _OptionalJobManifestSpecTypeDef):
    pass


LambdaInvokeOperationOutputTypeDef = TypedDict(
    "LambdaInvokeOperationOutputTypeDef",
    {
        "FunctionArn": str,
    },
    total=False,
)

S3InitiateRestoreObjectOperationOutputTypeDef = TypedDict(
    "S3InitiateRestoreObjectOperationOutputTypeDef",
    {
        "ExpirationInDays": int,
        "GlacierJobTier": S3GlacierJobTierType,
    },
    total=False,
)

LambdaInvokeOperationTypeDef = TypedDict(
    "LambdaInvokeOperationTypeDef",
    {
        "FunctionArn": str,
    },
    total=False,
)

S3InitiateRestoreObjectOperationTypeDef = TypedDict(
    "S3InitiateRestoreObjectOperationTypeDef",
    {
        "ExpirationInDays": int,
        "GlacierJobTier": S3GlacierJobTierType,
    },
    total=False,
)

JobTimersTypeDef = TypedDict(
    "JobTimersTypeDef",
    {
        "ElapsedTimeInActiveSeconds": int,
    },
    total=False,
)

LifecycleExpirationOutputTypeDef = TypedDict(
    "LifecycleExpirationOutputTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "ExpiredObjectDeleteMarker": bool,
    },
    total=False,
)

LifecycleExpirationTypeDef = TypedDict(
    "LifecycleExpirationTypeDef",
    {
        "Date": Union[datetime, str],
        "Days": int,
        "ExpiredObjectDeleteMarker": bool,
    },
    total=False,
)

NoncurrentVersionExpirationOutputTypeDef = TypedDict(
    "NoncurrentVersionExpirationOutputTypeDef",
    {
        "NoncurrentDays": int,
        "NewerNoncurrentVersions": int,
    },
    total=False,
)

NoncurrentVersionTransitionOutputTypeDef = TypedDict(
    "NoncurrentVersionTransitionOutputTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

TransitionOutputTypeDef = TypedDict(
    "TransitionOutputTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef",
    {
        "NoncurrentDays": int,
        "NewerNoncurrentVersions": int,
    },
    total=False,
)

NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": Union[datetime, str],
        "Days": int,
        "StorageClass": TransitionStorageClassType,
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

_RequiredListAccessPointsForObjectLambdaRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPointsForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessPointsForObjectLambdaRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPointsForObjectLambdaRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAccessPointsForObjectLambdaRequestRequestTypeDef(
    _RequiredListAccessPointsForObjectLambdaRequestRequestTypeDef,
    _OptionalListAccessPointsForObjectLambdaRequestRequestTypeDef,
):
    pass


_RequiredListAccessPointsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessPointsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessPointsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessPointsRequestRequestTypeDef",
    {
        "Bucket": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAccessPointsRequestRequestTypeDef(
    _RequiredListAccessPointsRequestRequestTypeDef, _OptionalListAccessPointsRequestRequestTypeDef
):
    pass


_RequiredListJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobsRequestRequestTypeDef",
    {
        "JobStatuses": Sequence[JobStatusType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListJobsRequestRequestTypeDef(
    _RequiredListJobsRequestRequestTypeDef, _OptionalListJobsRequestRequestTypeDef
):
    pass


_RequiredListMultiRegionAccessPointsRequestRequestTypeDef = TypedDict(
    "_RequiredListMultiRegionAccessPointsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListMultiRegionAccessPointsRequestRequestTypeDef = TypedDict(
    "_OptionalListMultiRegionAccessPointsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListMultiRegionAccessPointsRequestRequestTypeDef(
    _RequiredListMultiRegionAccessPointsRequestRequestTypeDef,
    _OptionalListMultiRegionAccessPointsRequestRequestTypeDef,
):
    pass


_RequiredListRegionalBucketsRequestRequestTypeDef = TypedDict(
    "_RequiredListRegionalBucketsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListRegionalBucketsRequestRequestTypeDef = TypedDict(
    "_OptionalListRegionalBucketsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "OutpostId": str,
    },
    total=False,
)


class ListRegionalBucketsRequestRequestTypeDef(
    _RequiredListRegionalBucketsRequestRequestTypeDef,
    _OptionalListRegionalBucketsRequestRequestTypeDef,
):
    pass


_RequiredRegionalBucketTypeDef = TypedDict(
    "_RequiredRegionalBucketTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
    },
)
_OptionalRegionalBucketTypeDef = TypedDict(
    "_OptionalRegionalBucketTypeDef",
    {
        "BucketArn": str,
        "OutpostId": str,
    },
    total=False,
)


class RegionalBucketTypeDef(_RequiredRegionalBucketTypeDef, _OptionalRegionalBucketTypeDef):
    pass


_RequiredListStorageLensConfigurationEntryTypeDef = TypedDict(
    "_RequiredListStorageLensConfigurationEntryTypeDef",
    {
        "Id": str,
        "StorageLensArn": str,
        "HomeRegion": str,
    },
)
_OptionalListStorageLensConfigurationEntryTypeDef = TypedDict(
    "_OptionalListStorageLensConfigurationEntryTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)


class ListStorageLensConfigurationEntryTypeDef(
    _RequiredListStorageLensConfigurationEntryTypeDef,
    _OptionalListStorageLensConfigurationEntryTypeDef,
):
    pass


_RequiredListStorageLensConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListStorageLensConfigurationsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListStorageLensConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListStorageLensConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListStorageLensConfigurationsRequestRequestTypeDef(
    _RequiredListStorageLensConfigurationsRequestRequestTypeDef,
    _OptionalListStorageLensConfigurationsRequestRequestTypeDef,
):
    pass


ReplicationTimeValueOutputTypeDef = TypedDict(
    "ReplicationTimeValueOutputTypeDef",
    {
        "Minutes": int,
    },
    total=False,
)

ReplicationTimeValueTypeDef = TypedDict(
    "ReplicationTimeValueTypeDef",
    {
        "Minutes": int,
    },
    total=False,
)

ProposedMultiRegionAccessPointPolicyTypeDef = TypedDict(
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

MultiRegionAccessPointRegionalResponseTypeDef = TypedDict(
    "MultiRegionAccessPointRegionalResponseTypeDef",
    {
        "Name": str,
        "RequestStatus": str,
    },
    total=False,
)

RegionReportTypeDef = TypedDict(
    "RegionReportTypeDef",
    {
        "Bucket": str,
        "Region": str,
        "BucketAccountId": str,
    },
    total=False,
)

_RequiredMultiRegionAccessPointRouteTypeDef = TypedDict(
    "_RequiredMultiRegionAccessPointRouteTypeDef",
    {
        "TrafficDialPercentage": int,
    },
)
_OptionalMultiRegionAccessPointRouteTypeDef = TypedDict(
    "_OptionalMultiRegionAccessPointRouteTypeDef",
    {
        "Bucket": str,
        "Region": str,
    },
    total=False,
)


class MultiRegionAccessPointRouteTypeDef(
    _RequiredMultiRegionAccessPointRouteTypeDef, _OptionalMultiRegionAccessPointRouteTypeDef
):
    pass


SelectionCriteriaOutputTypeDef = TypedDict(
    "SelectionCriteriaOutputTypeDef",
    {
        "Delimiter": str,
        "MaxDepth": int,
        "MinStorageBytesPercentage": float,
    },
    total=False,
)

SelectionCriteriaTypeDef = TypedDict(
    "SelectionCriteriaTypeDef",
    {
        "Delimiter": str,
        "MaxDepth": int,
        "MinStorageBytesPercentage": float,
    },
    total=False,
)

PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)

PutAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "PutAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)

_RequiredPutBucketPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Policy": str,
    },
)
_OptionalPutBucketPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketPolicyRequestRequestTypeDef",
    {
        "ConfirmRemoveSelfBucketAccess": bool,
    },
    total=False,
)


class PutBucketPolicyRequestRequestTypeDef(
    _RequiredPutBucketPolicyRequestRequestTypeDef, _OptionalPutBucketPolicyRequestRequestTypeDef
):
    pass


VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "MFADelete": MFADeleteType,
        "Status": BucketVersioningStatusType,
    },
    total=False,
)

PutMultiRegionAccessPointPolicyInputTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    {
        "Name": str,
        "Policy": str,
    },
)

StorageLensTagTypeDef = TypedDict(
    "StorageLensTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

ReplicaModificationsOutputTypeDef = TypedDict(
    "ReplicaModificationsOutputTypeDef",
    {
        "Status": ReplicaModificationsStatusType,
    },
)

ReplicaModificationsTypeDef = TypedDict(
    "ReplicaModificationsTypeDef",
    {
        "Status": ReplicaModificationsStatusType,
    },
)

S3ObjectOwnerOutputTypeDef = TypedDict(
    "S3ObjectOwnerOutputTypeDef",
    {
        "ID": str,
        "DisplayName": str,
    },
    total=False,
)

S3ObjectOwnerTypeDef = TypedDict(
    "S3ObjectOwnerTypeDef",
    {
        "ID": str,
        "DisplayName": str,
    },
    total=False,
)

S3ObjectMetadataOutputTypeDef = TypedDict(
    "S3ObjectMetadataOutputTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": datetime,
        "RequesterCharged": bool,
        "SSEAlgorithm": S3SSEAlgorithmType,
    },
    total=False,
)

S3ObjectMetadataTypeDef = TypedDict(
    "S3ObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Mapping[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": Union[datetime, str],
        "RequesterCharged": bool,
        "SSEAlgorithm": S3SSEAlgorithmType,
    },
    total=False,
)

S3GranteeOutputTypeDef = TypedDict(
    "S3GranteeOutputTypeDef",
    {
        "TypeIdentifier": S3GranteeTypeIdentifierType,
        "Identifier": str,
        "DisplayName": str,
    },
    total=False,
)

S3GranteeTypeDef = TypedDict(
    "S3GranteeTypeDef",
    {
        "TypeIdentifier": S3GranteeTypeIdentifierType,
        "Identifier": str,
        "DisplayName": str,
    },
    total=False,
)

S3ObjectLockLegalHoldOutputTypeDef = TypedDict(
    "S3ObjectLockLegalHoldOutputTypeDef",
    {
        "Status": S3ObjectLockLegalHoldStatusType,
    },
)

S3ObjectLockLegalHoldTypeDef = TypedDict(
    "S3ObjectLockLegalHoldTypeDef",
    {
        "Status": S3ObjectLockLegalHoldStatusType,
    },
)

S3RetentionOutputTypeDef = TypedDict(
    "S3RetentionOutputTypeDef",
    {
        "RetainUntilDate": datetime,
        "Mode": S3ObjectLockRetentionModeType,
    },
    total=False,
)

S3RetentionTypeDef = TypedDict(
    "S3RetentionTypeDef",
    {
        "RetainUntilDate": Union[datetime, str],
        "Mode": S3ObjectLockRetentionModeType,
    },
    total=False,
)

SSEKMSOutputTypeDef = TypedDict(
    "SSEKMSOutputTypeDef",
    {
        "KeyId": str,
    },
)

SSEKMSTypeDef = TypedDict(
    "SSEKMSTypeDef",
    {
        "KeyId": str,
    },
)

SseKmsEncryptedObjectsOutputTypeDef = TypedDict(
    "SseKmsEncryptedObjectsOutputTypeDef",
    {
        "Status": SseKmsEncryptedObjectsStatusType,
    },
)

SseKmsEncryptedObjectsTypeDef = TypedDict(
    "SseKmsEncryptedObjectsTypeDef",
    {
        "Status": SseKmsEncryptedObjectsStatusType,
    },
)

StorageLensAwsOrgOutputTypeDef = TypedDict(
    "StorageLensAwsOrgOutputTypeDef",
    {
        "Arn": str,
    },
)

StorageLensAwsOrgTypeDef = TypedDict(
    "StorageLensAwsOrgTypeDef",
    {
        "Arn": str,
    },
)

UpdateJobPriorityRequestRequestTypeDef = TypedDict(
    "UpdateJobPriorityRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Priority": int,
    },
)

_RequiredUpdateJobStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "RequestedJobStatus": RequestedJobStatusType,
    },
)
_OptionalUpdateJobStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobStatusRequestRequestTypeDef",
    {
        "StatusUpdateReason": str,
    },
    total=False,
)


class UpdateJobStatusRequestRequestTypeDef(
    _RequiredUpdateJobStatusRequestRequestTypeDef, _OptionalUpdateJobStatusRequestRequestTypeDef
):
    pass


_RequiredAccessPointTypeDef = TypedDict(
    "_RequiredAccessPointTypeDef",
    {
        "Name": str,
        "NetworkOrigin": NetworkOriginType,
        "Bucket": str,
    },
)
_OptionalAccessPointTypeDef = TypedDict(
    "_OptionalAccessPointTypeDef",
    {
        "VpcConfiguration": VpcConfigurationOutputTypeDef,
        "AccessPointArn": str,
        "Alias": str,
        "BucketAccountId": str,
    },
    total=False,
)


class AccessPointTypeDef(_RequiredAccessPointTypeDef, _OptionalAccessPointTypeDef):
    pass


ObjectLambdaContentTransformationOutputTypeDef = TypedDict(
    "ObjectLambdaContentTransformationOutputTypeDef",
    {
        "AwsLambda": AwsLambdaTransformationOutputTypeDef,
    },
    total=False,
)

ObjectLambdaContentTransformationTypeDef = TypedDict(
    "ObjectLambdaContentTransformationTypeDef",
    {
        "AwsLambda": AwsLambdaTransformationTypeDef,
    },
    total=False,
)

_RequiredObjectLambdaAccessPointTypeDef = TypedDict(
    "_RequiredObjectLambdaAccessPointTypeDef",
    {
        "Name": str,
    },
)
_OptionalObjectLambdaAccessPointTypeDef = TypedDict(
    "_OptionalObjectLambdaAccessPointTypeDef",
    {
        "ObjectLambdaAccessPointArn": str,
        "Alias": ObjectLambdaAccessPointAliasTypeDef,
    },
    total=False,
)


class ObjectLambdaAccessPointTypeDef(
    _RequiredObjectLambdaAccessPointTypeDef, _OptionalObjectLambdaAccessPointTypeDef
):
    pass


CreateAccessPointForObjectLambdaResultTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaResultTypeDef",
    {
        "ObjectLambdaAccessPointArn": str,
        "Alias": ObjectLambdaAccessPointAliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAccessPointResultTypeDef = TypedDict(
    "CreateAccessPointResultTypeDef",
    {
        "AccessPointArn": str,
        "Alias": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateBucketResultTypeDef = TypedDict(
    "CreateBucketResultTypeDef",
    {
        "Location": str,
        "BucketArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateMultiRegionAccessPointResultTypeDef = TypedDict(
    "CreateMultiRegionAccessPointResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteMultiRegionAccessPointResultTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAccessPointPolicyForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAccessPointPolicyResultTypeDef = TypedDict(
    "GetAccessPointPolicyResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBucketPolicyResultTypeDef = TypedDict(
    "GetBucketPolicyResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBucketResultTypeDef = TypedDict(
    "GetBucketResultTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBucketVersioningResultTypeDef = TypedDict(
    "GetBucketVersioningResultTypeDef",
    {
        "Status": BucketVersioningStatusType,
        "MFADelete": MFADeleteStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutMultiRegionAccessPointPolicyResultTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateJobPriorityResultTypeDef = TypedDict(
    "UpdateJobPriorityResultTypeDef",
    {
        "JobId": str,
        "Priority": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateJobStatusResultTypeDef = TypedDict(
    "UpdateJobStatusResultTypeDef",
    {
        "JobId": str,
        "Status": JobStatusType,
        "StatusUpdateReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "PutPublicAccessBlockRequestRequestTypeDef",
    {
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationTypeDef,
        "AccountId": str,
    },
)

_RequiredCreateAccessPointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Bucket": str,
    },
)
_OptionalCreateAccessPointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPointRequestRequestTypeDef",
    {
        "VpcConfiguration": VpcConfigurationTypeDef,
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationTypeDef,
        "BucketAccountId": str,
    },
    total=False,
)


class CreateAccessPointRequestRequestTypeDef(
    _RequiredCreateAccessPointRequestRequestTypeDef, _OptionalCreateAccessPointRequestRequestTypeDef
):
    pass


_RequiredCreateBucketRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBucketRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalCreateBucketRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBucketRequestRequestTypeDef",
    {
        "ACL": BucketCannedACLType,
        "CreateBucketConfiguration": CreateBucketConfigurationTypeDef,
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ObjectLockEnabledForBucket": bool,
        "OutpostId": str,
    },
    total=False,
)


class CreateBucketRequestRequestTypeDef(
    _RequiredCreateBucketRequestRequestTypeDef, _OptionalCreateBucketRequestRequestTypeDef
):
    pass


LifecycleRuleAndOperatorTypeDef = TypedDict(
    "LifecycleRuleAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": Sequence[S3TagTypeDef],
        "ObjectSizeGreaterThan": int,
        "ObjectSizeLessThan": int,
    },
    total=False,
)

PutJobTaggingRequestRequestTypeDef = TypedDict(
    "PutJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Tags": Sequence[S3TagTypeDef],
    },
)

ReplicationRuleAndOperatorTypeDef = TypedDict(
    "ReplicationRuleAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": Sequence[S3TagTypeDef],
    },
    total=False,
)

S3SetObjectTaggingOperationTypeDef = TypedDict(
    "S3SetObjectTaggingOperationTypeDef",
    {
        "TagSet": Sequence[S3TagTypeDef],
    },
    total=False,
)

TaggingTypeDef = TypedDict(
    "TaggingTypeDef",
    {
        "TagSet": Sequence[S3TagTypeDef],
    },
)

GetAccessPointForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaResultTypeDef",
    {
        "Name": str,
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationOutputTypeDef,
        "CreationDate": datetime,
        "Alias": ObjectLambdaAccessPointAliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAccessPointResultTypeDef = TypedDict(
    "GetAccessPointResultTypeDef",
    {
        "Name": str,
        "Bucket": str,
        "NetworkOrigin": NetworkOriginType,
        "VpcConfiguration": VpcConfigurationOutputTypeDef,
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationOutputTypeDef,
        "CreationDate": datetime,
        "Alias": str,
        "AccessPointArn": str,
        "Endpoints": Dict[str, str],
        "BucketAccountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateMultiRegionAccessPointInputOutputTypeDef = TypedDict(
    "_RequiredCreateMultiRegionAccessPointInputOutputTypeDef",
    {
        "Name": str,
        "Regions": List[RegionOutputTypeDef],
    },
)
_OptionalCreateMultiRegionAccessPointInputOutputTypeDef = TypedDict(
    "_OptionalCreateMultiRegionAccessPointInputOutputTypeDef",
    {
        "PublicAccessBlock": PublicAccessBlockConfigurationOutputTypeDef,
    },
    total=False,
)


class CreateMultiRegionAccessPointInputOutputTypeDef(
    _RequiredCreateMultiRegionAccessPointInputOutputTypeDef,
    _OptionalCreateMultiRegionAccessPointInputOutputTypeDef,
):
    pass


_RequiredCreateMultiRegionAccessPointInputTypeDef = TypedDict(
    "_RequiredCreateMultiRegionAccessPointInputTypeDef",
    {
        "Name": str,
        "Regions": Sequence[RegionTypeDef],
    },
)
_OptionalCreateMultiRegionAccessPointInputTypeDef = TypedDict(
    "_OptionalCreateMultiRegionAccessPointInputTypeDef",
    {
        "PublicAccessBlock": PublicAccessBlockConfigurationTypeDef,
    },
    total=False,
)


class CreateMultiRegionAccessPointInputTypeDef(
    _RequiredCreateMultiRegionAccessPointInputTypeDef,
    _OptionalCreateMultiRegionAccessPointInputTypeDef,
):
    pass


DeleteMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": DeleteMultiRegionAccessPointInputTypeDef,
    },
)

GeneratedManifestEncryptionOutputTypeDef = TypedDict(
    "GeneratedManifestEncryptionOutputTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": SSEKMSEncryptionOutputTypeDef,
    },
    total=False,
)

GeneratedManifestEncryptionTypeDef = TypedDict(
    "GeneratedManifestEncryptionTypeDef",
    {
        "SSES3": Mapping[str, Any],
        "SSEKMS": SSEKMSEncryptionTypeDef,
    },
    total=False,
)

GetAccessPointPolicyStatusForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    {
        "PolicyStatus": PolicyStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusResultTypeDef",
    {
        "PolicyStatus": PolicyStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMultiRegionAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    {
        "Established": PolicyStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBucketTaggingResultTypeDef = TypedDict(
    "GetBucketTaggingResultTypeDef",
    {
        "TagSet": List[S3TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetJobTaggingResultTypeDef = TypedDict(
    "GetJobTaggingResultTypeDef",
    {
        "Tags": List[S3TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LifecycleRuleAndOperatorOutputTypeDef = TypedDict(
    "LifecycleRuleAndOperatorOutputTypeDef",
    {
        "Prefix": str,
        "Tags": List[S3TagOutputTypeDef],
        "ObjectSizeGreaterThan": int,
        "ObjectSizeLessThan": int,
    },
    total=False,
)

ReplicationRuleAndOperatorOutputTypeDef = TypedDict(
    "ReplicationRuleAndOperatorOutputTypeDef",
    {
        "Prefix": str,
        "Tags": List[S3TagOutputTypeDef],
    },
    total=False,
)

S3SetObjectTaggingOperationOutputTypeDef = TypedDict(
    "S3SetObjectTaggingOperationOutputTypeDef",
    {
        "TagSet": List[S3TagOutputTypeDef],
    },
    total=False,
)

GetMultiRegionAccessPointRoutesResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointRoutesResultTypeDef",
    {
        "Mrap": str,
        "Routes": List[MultiRegionAccessPointRouteOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetStorageLensConfigurationTaggingResultTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingResultTypeDef",
    {
        "Tags": List[StorageLensTagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

S3GeneratedManifestDescriptorTypeDef = TypedDict(
    "S3GeneratedManifestDescriptorTypeDef",
    {
        "Format": Literal["S3InventoryReport_CSV_20211130"],
        "Location": JobManifestLocationOutputTypeDef,
    },
    total=False,
)

JobManifestOutputTypeDef = TypedDict(
    "JobManifestOutputTypeDef",
    {
        "Spec": JobManifestSpecOutputTypeDef,
        "Location": JobManifestLocationOutputTypeDef,
    },
)

JobManifestTypeDef = TypedDict(
    "JobManifestTypeDef",
    {
        "Spec": JobManifestSpecTypeDef,
        "Location": JobManifestLocationTypeDef,
    },
)

JobProgressSummaryTypeDef = TypedDict(
    "JobProgressSummaryTypeDef",
    {
        "TotalNumberOfTasks": int,
        "NumberOfTasksSucceeded": int,
        "NumberOfTasksFailed": int,
        "Timers": JobTimersTypeDef,
    },
    total=False,
)

_RequiredListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef = TypedDict(
    "_RequiredListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef = TypedDict(
    "_OptionalListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef(
    _RequiredListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef,
    _OptionalListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef,
):
    pass


ListRegionalBucketsResultTypeDef = TypedDict(
    "ListRegionalBucketsResultTypeDef",
    {
        "RegionalBucketList": List[RegionalBucketTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStorageLensConfigurationsResultTypeDef = TypedDict(
    "ListStorageLensConfigurationsResultTypeDef",
    {
        "NextToken": str,
        "StorageLensConfigurationList": List[ListStorageLensConfigurationEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredMetricsOutputTypeDef = TypedDict(
    "_RequiredMetricsOutputTypeDef",
    {
        "Status": MetricsStatusType,
    },
)
_OptionalMetricsOutputTypeDef = TypedDict(
    "_OptionalMetricsOutputTypeDef",
    {
        "EventThreshold": ReplicationTimeValueOutputTypeDef,
    },
    total=False,
)


class MetricsOutputTypeDef(_RequiredMetricsOutputTypeDef, _OptionalMetricsOutputTypeDef):
    pass


ReplicationTimeOutputTypeDef = TypedDict(
    "ReplicationTimeOutputTypeDef",
    {
        "Status": ReplicationTimeStatusType,
        "Time": ReplicationTimeValueOutputTypeDef,
    },
)

_RequiredMetricsTypeDef = TypedDict(
    "_RequiredMetricsTypeDef",
    {
        "Status": MetricsStatusType,
    },
)
_OptionalMetricsTypeDef = TypedDict(
    "_OptionalMetricsTypeDef",
    {
        "EventThreshold": ReplicationTimeValueTypeDef,
    },
    total=False,
)


class MetricsTypeDef(_RequiredMetricsTypeDef, _OptionalMetricsTypeDef):
    pass


ReplicationTimeTypeDef = TypedDict(
    "ReplicationTimeTypeDef",
    {
        "Status": ReplicationTimeStatusType,
        "Time": ReplicationTimeValueTypeDef,
    },
)

MultiRegionAccessPointPolicyDocumentTypeDef = TypedDict(
    "MultiRegionAccessPointPolicyDocumentTypeDef",
    {
        "Established": EstablishedMultiRegionAccessPointPolicyTypeDef,
        "Proposed": ProposedMultiRegionAccessPointPolicyTypeDef,
    },
    total=False,
)

MultiRegionAccessPointsAsyncResponseTypeDef = TypedDict(
    "MultiRegionAccessPointsAsyncResponseTypeDef",
    {
        "Regions": List[MultiRegionAccessPointRegionalResponseTypeDef],
    },
    total=False,
)

MultiRegionAccessPointReportTypeDef = TypedDict(
    "MultiRegionAccessPointReportTypeDef",
    {
        "Name": str,
        "Alias": str,
        "CreatedAt": datetime,
        "PublicAccessBlock": PublicAccessBlockConfigurationOutputTypeDef,
        "Status": MultiRegionAccessPointStatusType,
        "Regions": List[RegionReportTypeDef],
    },
    total=False,
)

SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef = TypedDict(
    "SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef",
    {
        "AccountId": str,
        "Mrap": str,
        "RouteUpdates": Sequence[MultiRegionAccessPointRouteTypeDef],
    },
)

PrefixLevelStorageMetricsOutputTypeDef = TypedDict(
    "PrefixLevelStorageMetricsOutputTypeDef",
    {
        "IsEnabled": bool,
        "SelectionCriteria": SelectionCriteriaOutputTypeDef,
    },
    total=False,
)

PrefixLevelStorageMetricsTypeDef = TypedDict(
    "PrefixLevelStorageMetricsTypeDef",
    {
        "IsEnabled": bool,
        "SelectionCriteria": SelectionCriteriaTypeDef,
    },
    total=False,
)

_RequiredPutBucketVersioningRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketVersioningRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "VersioningConfiguration": VersioningConfigurationTypeDef,
    },
)
_OptionalPutBucketVersioningRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketVersioningRequestRequestTypeDef",
    {
        "MFA": str,
    },
    total=False,
)


class PutBucketVersioningRequestRequestTypeDef(
    _RequiredPutBucketVersioningRequestRequestTypeDef,
    _OptionalPutBucketVersioningRequestRequestTypeDef,
):
    pass


PutMultiRegionAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": PutMultiRegionAccessPointPolicyInputTypeDef,
    },
)

PutStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "Tags": Sequence[StorageLensTagTypeDef],
    },
)

S3GrantOutputTypeDef = TypedDict(
    "S3GrantOutputTypeDef",
    {
        "Grantee": S3GranteeOutputTypeDef,
        "Permission": S3PermissionType,
    },
    total=False,
)

S3GrantTypeDef = TypedDict(
    "S3GrantTypeDef",
    {
        "Grantee": S3GranteeTypeDef,
        "Permission": S3PermissionType,
    },
    total=False,
)

S3SetObjectLegalHoldOperationOutputTypeDef = TypedDict(
    "S3SetObjectLegalHoldOperationOutputTypeDef",
    {
        "LegalHold": S3ObjectLockLegalHoldOutputTypeDef,
    },
)

S3SetObjectLegalHoldOperationTypeDef = TypedDict(
    "S3SetObjectLegalHoldOperationTypeDef",
    {
        "LegalHold": S3ObjectLockLegalHoldTypeDef,
    },
)

_RequiredS3SetObjectRetentionOperationOutputTypeDef = TypedDict(
    "_RequiredS3SetObjectRetentionOperationOutputTypeDef",
    {
        "Retention": S3RetentionOutputTypeDef,
    },
)
_OptionalS3SetObjectRetentionOperationOutputTypeDef = TypedDict(
    "_OptionalS3SetObjectRetentionOperationOutputTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)


class S3SetObjectRetentionOperationOutputTypeDef(
    _RequiredS3SetObjectRetentionOperationOutputTypeDef,
    _OptionalS3SetObjectRetentionOperationOutputTypeDef,
):
    pass


_RequiredS3SetObjectRetentionOperationTypeDef = TypedDict(
    "_RequiredS3SetObjectRetentionOperationTypeDef",
    {
        "Retention": S3RetentionTypeDef,
    },
)
_OptionalS3SetObjectRetentionOperationTypeDef = TypedDict(
    "_OptionalS3SetObjectRetentionOperationTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)


class S3SetObjectRetentionOperationTypeDef(
    _RequiredS3SetObjectRetentionOperationTypeDef, _OptionalS3SetObjectRetentionOperationTypeDef
):
    pass


StorageLensDataExportEncryptionOutputTypeDef = TypedDict(
    "StorageLensDataExportEncryptionOutputTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": SSEKMSOutputTypeDef,
    },
    total=False,
)

StorageLensDataExportEncryptionTypeDef = TypedDict(
    "StorageLensDataExportEncryptionTypeDef",
    {
        "SSES3": Mapping[str, Any],
        "SSEKMS": SSEKMSTypeDef,
    },
    total=False,
)

SourceSelectionCriteriaOutputTypeDef = TypedDict(
    "SourceSelectionCriteriaOutputTypeDef",
    {
        "SseKmsEncryptedObjects": SseKmsEncryptedObjectsOutputTypeDef,
        "ReplicaModifications": ReplicaModificationsOutputTypeDef,
    },
    total=False,
)

SourceSelectionCriteriaTypeDef = TypedDict(
    "SourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": SseKmsEncryptedObjectsTypeDef,
        "ReplicaModifications": ReplicaModificationsTypeDef,
    },
    total=False,
)

ListAccessPointsResultTypeDef = TypedDict(
    "ListAccessPointsResultTypeDef",
    {
        "AccessPointList": List[AccessPointTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ObjectLambdaTransformationConfigurationOutputTypeDef = TypedDict(
    "ObjectLambdaTransformationConfigurationOutputTypeDef",
    {
        "Actions": List[ObjectLambdaTransformationConfigurationActionType],
        "ContentTransformation": ObjectLambdaContentTransformationOutputTypeDef,
    },
)

ObjectLambdaTransformationConfigurationTypeDef = TypedDict(
    "ObjectLambdaTransformationConfigurationTypeDef",
    {
        "Actions": Sequence[ObjectLambdaTransformationConfigurationActionType],
        "ContentTransformation": ObjectLambdaContentTransformationTypeDef,
    },
)

ListAccessPointsForObjectLambdaResultTypeDef = TypedDict(
    "ListAccessPointsForObjectLambdaResultTypeDef",
    {
        "ObjectLambdaAccessPointList": List[ObjectLambdaAccessPointTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": S3TagTypeDef,
        "And": LifecycleRuleAndOperatorTypeDef,
        "ObjectSizeGreaterThan": int,
        "ObjectSizeLessThan": int,
    },
    total=False,
)

ReplicationRuleFilterTypeDef = TypedDict(
    "ReplicationRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": S3TagTypeDef,
        "And": ReplicationRuleAndOperatorTypeDef,
    },
    total=False,
)

PutBucketTaggingRequestRequestTypeDef = TypedDict(
    "PutBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Tagging": TaggingTypeDef,
    },
)

AsyncRequestParametersTypeDef = TypedDict(
    "AsyncRequestParametersTypeDef",
    {
        "CreateMultiRegionAccessPointRequest": CreateMultiRegionAccessPointInputOutputTypeDef,
        "DeleteMultiRegionAccessPointRequest": DeleteMultiRegionAccessPointInputOutputTypeDef,
        "PutMultiRegionAccessPointPolicyRequest": PutMultiRegionAccessPointPolicyInputOutputTypeDef,
    },
    total=False,
)

CreateMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "CreateMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": CreateMultiRegionAccessPointInputTypeDef,
    },
)

_RequiredS3ManifestOutputLocationOutputTypeDef = TypedDict(
    "_RequiredS3ManifestOutputLocationOutputTypeDef",
    {
        "Bucket": str,
        "ManifestFormat": Literal["S3InventoryReport_CSV_20211130"],
    },
)
_OptionalS3ManifestOutputLocationOutputTypeDef = TypedDict(
    "_OptionalS3ManifestOutputLocationOutputTypeDef",
    {
        "ExpectedManifestBucketOwner": str,
        "ManifestPrefix": str,
        "ManifestEncryption": GeneratedManifestEncryptionOutputTypeDef,
    },
    total=False,
)


class S3ManifestOutputLocationOutputTypeDef(
    _RequiredS3ManifestOutputLocationOutputTypeDef, _OptionalS3ManifestOutputLocationOutputTypeDef
):
    pass


_RequiredS3ManifestOutputLocationTypeDef = TypedDict(
    "_RequiredS3ManifestOutputLocationTypeDef",
    {
        "Bucket": str,
        "ManifestFormat": Literal["S3InventoryReport_CSV_20211130"],
    },
)
_OptionalS3ManifestOutputLocationTypeDef = TypedDict(
    "_OptionalS3ManifestOutputLocationTypeDef",
    {
        "ExpectedManifestBucketOwner": str,
        "ManifestPrefix": str,
        "ManifestEncryption": GeneratedManifestEncryptionTypeDef,
    },
    total=False,
)


class S3ManifestOutputLocationTypeDef(
    _RequiredS3ManifestOutputLocationTypeDef, _OptionalS3ManifestOutputLocationTypeDef
):
    pass


LifecycleRuleFilterOutputTypeDef = TypedDict(
    "LifecycleRuleFilterOutputTypeDef",
    {
        "Prefix": str,
        "Tag": S3TagOutputTypeDef,
        "And": LifecycleRuleAndOperatorOutputTypeDef,
        "ObjectSizeGreaterThan": int,
        "ObjectSizeLessThan": int,
    },
    total=False,
)

ReplicationRuleFilterOutputTypeDef = TypedDict(
    "ReplicationRuleFilterOutputTypeDef",
    {
        "Prefix": str,
        "Tag": S3TagOutputTypeDef,
        "And": ReplicationRuleAndOperatorOutputTypeDef,
    },
    total=False,
)

JobListDescriptorTypeDef = TypedDict(
    "JobListDescriptorTypeDef",
    {
        "JobId": str,
        "Description": str,
        "Operation": OperationNameType,
        "Priority": int,
        "Status": JobStatusType,
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "ProgressSummary": JobProgressSummaryTypeDef,
    },
    total=False,
)

_RequiredDestinationOutputTypeDef = TypedDict(
    "_RequiredDestinationOutputTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDestinationOutputTypeDef = TypedDict(
    "_OptionalDestinationOutputTypeDef",
    {
        "Account": str,
        "ReplicationTime": ReplicationTimeOutputTypeDef,
        "AccessControlTranslation": AccessControlTranslationOutputTypeDef,
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
        "Metrics": MetricsOutputTypeDef,
        "StorageClass": ReplicationStorageClassType,
    },
    total=False,
)


class DestinationOutputTypeDef(
    _RequiredDestinationOutputTypeDef, _OptionalDestinationOutputTypeDef
):
    pass


_RequiredDestinationTypeDef = TypedDict(
    "_RequiredDestinationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "Account": str,
        "ReplicationTime": ReplicationTimeTypeDef,
        "AccessControlTranslation": AccessControlTranslationTypeDef,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "Metrics": MetricsTypeDef,
        "StorageClass": ReplicationStorageClassType,
    },
    total=False,
)


class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass


GetMultiRegionAccessPointPolicyResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    {
        "Policy": MultiRegionAccessPointPolicyDocumentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AsyncResponseDetailsTypeDef = TypedDict(
    "AsyncResponseDetailsTypeDef",
    {
        "MultiRegionAccessPointDetails": MultiRegionAccessPointsAsyncResponseTypeDef,
        "ErrorDetails": AsyncErrorDetailsTypeDef,
    },
    total=False,
)

GetMultiRegionAccessPointResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointResultTypeDef",
    {
        "AccessPoint": MultiRegionAccessPointReportTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMultiRegionAccessPointsResultTypeDef = TypedDict(
    "ListMultiRegionAccessPointsResultTypeDef",
    {
        "AccessPoints": List[MultiRegionAccessPointReportTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PrefixLevelOutputTypeDef = TypedDict(
    "PrefixLevelOutputTypeDef",
    {
        "StorageMetrics": PrefixLevelStorageMetricsOutputTypeDef,
    },
)

PrefixLevelTypeDef = TypedDict(
    "PrefixLevelTypeDef",
    {
        "StorageMetrics": PrefixLevelStorageMetricsTypeDef,
    },
)

_RequiredS3AccessControlListOutputTypeDef = TypedDict(
    "_RequiredS3AccessControlListOutputTypeDef",
    {
        "Owner": S3ObjectOwnerOutputTypeDef,
    },
)
_OptionalS3AccessControlListOutputTypeDef = TypedDict(
    "_OptionalS3AccessControlListOutputTypeDef",
    {
        "Grants": List[S3GrantOutputTypeDef],
    },
    total=False,
)


class S3AccessControlListOutputTypeDef(
    _RequiredS3AccessControlListOutputTypeDef, _OptionalS3AccessControlListOutputTypeDef
):
    pass


S3CopyObjectOperationOutputTypeDef = TypedDict(
    "S3CopyObjectOperationOutputTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": S3CannedAccessControlListType,
        "AccessControlGrants": List[S3GrantOutputTypeDef],
        "MetadataDirective": S3MetadataDirectiveType,
        "ModifiedSinceConstraint": datetime,
        "NewObjectMetadata": S3ObjectMetadataOutputTypeDef,
        "NewObjectTagging": List[S3TagOutputTypeDef],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": S3StorageClassType,
        "UnModifiedSinceConstraint": datetime,
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": S3ObjectLockLegalHoldStatusType,
        "ObjectLockMode": S3ObjectLockModeType,
        "ObjectLockRetainUntilDate": datetime,
        "BucketKeyEnabled": bool,
        "ChecksumAlgorithm": S3ChecksumAlgorithmType,
    },
    total=False,
)

_RequiredS3AccessControlListTypeDef = TypedDict(
    "_RequiredS3AccessControlListTypeDef",
    {
        "Owner": S3ObjectOwnerTypeDef,
    },
)
_OptionalS3AccessControlListTypeDef = TypedDict(
    "_OptionalS3AccessControlListTypeDef",
    {
        "Grants": Sequence[S3GrantTypeDef],
    },
    total=False,
)


class S3AccessControlListTypeDef(
    _RequiredS3AccessControlListTypeDef, _OptionalS3AccessControlListTypeDef
):
    pass


S3CopyObjectOperationTypeDef = TypedDict(
    "S3CopyObjectOperationTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": S3CannedAccessControlListType,
        "AccessControlGrants": Sequence[S3GrantTypeDef],
        "MetadataDirective": S3MetadataDirectiveType,
        "ModifiedSinceConstraint": Union[datetime, str],
        "NewObjectMetadata": S3ObjectMetadataTypeDef,
        "NewObjectTagging": Sequence[S3TagTypeDef],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": S3StorageClassType,
        "UnModifiedSinceConstraint": Union[datetime, str],
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": S3ObjectLockLegalHoldStatusType,
        "ObjectLockMode": S3ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "BucketKeyEnabled": bool,
        "ChecksumAlgorithm": S3ChecksumAlgorithmType,
    },
    total=False,
)

_RequiredS3BucketDestinationOutputTypeDef = TypedDict(
    "_RequiredS3BucketDestinationOutputTypeDef",
    {
        "Format": FormatType,
        "OutputSchemaVersion": Literal["V_1"],
        "AccountId": str,
        "Arn": str,
    },
)
_OptionalS3BucketDestinationOutputTypeDef = TypedDict(
    "_OptionalS3BucketDestinationOutputTypeDef",
    {
        "Prefix": str,
        "Encryption": StorageLensDataExportEncryptionOutputTypeDef,
    },
    total=False,
)


class S3BucketDestinationOutputTypeDef(
    _RequiredS3BucketDestinationOutputTypeDef, _OptionalS3BucketDestinationOutputTypeDef
):
    pass


_RequiredS3BucketDestinationTypeDef = TypedDict(
    "_RequiredS3BucketDestinationTypeDef",
    {
        "Format": FormatType,
        "OutputSchemaVersion": Literal["V_1"],
        "AccountId": str,
        "Arn": str,
    },
)
_OptionalS3BucketDestinationTypeDef = TypedDict(
    "_OptionalS3BucketDestinationTypeDef",
    {
        "Prefix": str,
        "Encryption": StorageLensDataExportEncryptionTypeDef,
    },
    total=False,
)


class S3BucketDestinationTypeDef(
    _RequiredS3BucketDestinationTypeDef, _OptionalS3BucketDestinationTypeDef
):
    pass


_RequiredObjectLambdaConfigurationOutputTypeDef = TypedDict(
    "_RequiredObjectLambdaConfigurationOutputTypeDef",
    {
        "SupportingAccessPoint": str,
        "TransformationConfigurations": List[ObjectLambdaTransformationConfigurationOutputTypeDef],
    },
)
_OptionalObjectLambdaConfigurationOutputTypeDef = TypedDict(
    "_OptionalObjectLambdaConfigurationOutputTypeDef",
    {
        "CloudWatchMetricsEnabled": bool,
        "AllowedFeatures": List[ObjectLambdaAllowedFeatureType],
    },
    total=False,
)


class ObjectLambdaConfigurationOutputTypeDef(
    _RequiredObjectLambdaConfigurationOutputTypeDef, _OptionalObjectLambdaConfigurationOutputTypeDef
):
    pass


_RequiredObjectLambdaConfigurationTypeDef = TypedDict(
    "_RequiredObjectLambdaConfigurationTypeDef",
    {
        "SupportingAccessPoint": str,
        "TransformationConfigurations": Sequence[ObjectLambdaTransformationConfigurationTypeDef],
    },
)
_OptionalObjectLambdaConfigurationTypeDef = TypedDict(
    "_OptionalObjectLambdaConfigurationTypeDef",
    {
        "CloudWatchMetricsEnabled": bool,
        "AllowedFeatures": Sequence[ObjectLambdaAllowedFeatureType],
    },
    total=False,
)


class ObjectLambdaConfigurationTypeDef(
    _RequiredObjectLambdaConfigurationTypeDef, _OptionalObjectLambdaConfigurationTypeDef
):
    pass


_RequiredLifecycleRuleTypeDef = TypedDict(
    "_RequiredLifecycleRuleTypeDef",
    {
        "Status": ExpirationStatusType,
    },
)
_OptionalLifecycleRuleTypeDef = TypedDict(
    "_OptionalLifecycleRuleTypeDef",
    {
        "Expiration": LifecycleExpirationTypeDef,
        "ID": str,
        "Filter": LifecycleRuleFilterTypeDef,
        "Transitions": Sequence[TransitionTypeDef],
        "NoncurrentVersionTransitions": Sequence[NoncurrentVersionTransitionTypeDef],
        "NoncurrentVersionExpiration": NoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": AbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)


class LifecycleRuleTypeDef(_RequiredLifecycleRuleTypeDef, _OptionalLifecycleRuleTypeDef):
    pass


_RequiredS3JobManifestGeneratorOutputTypeDef = TypedDict(
    "_RequiredS3JobManifestGeneratorOutputTypeDef",
    {
        "SourceBucket": str,
        "EnableManifestOutput": bool,
    },
)
_OptionalS3JobManifestGeneratorOutputTypeDef = TypedDict(
    "_OptionalS3JobManifestGeneratorOutputTypeDef",
    {
        "ExpectedBucketOwner": str,
        "ManifestOutputLocation": S3ManifestOutputLocationOutputTypeDef,
        "Filter": JobManifestGeneratorFilterOutputTypeDef,
    },
    total=False,
)


class S3JobManifestGeneratorOutputTypeDef(
    _RequiredS3JobManifestGeneratorOutputTypeDef, _OptionalS3JobManifestGeneratorOutputTypeDef
):
    pass


_RequiredS3JobManifestGeneratorTypeDef = TypedDict(
    "_RequiredS3JobManifestGeneratorTypeDef",
    {
        "SourceBucket": str,
        "EnableManifestOutput": bool,
    },
)
_OptionalS3JobManifestGeneratorTypeDef = TypedDict(
    "_OptionalS3JobManifestGeneratorTypeDef",
    {
        "ExpectedBucketOwner": str,
        "ManifestOutputLocation": S3ManifestOutputLocationTypeDef,
        "Filter": JobManifestGeneratorFilterTypeDef,
    },
    total=False,
)


class S3JobManifestGeneratorTypeDef(
    _RequiredS3JobManifestGeneratorTypeDef, _OptionalS3JobManifestGeneratorTypeDef
):
    pass


_RequiredLifecycleRuleOutputTypeDef = TypedDict(
    "_RequiredLifecycleRuleOutputTypeDef",
    {
        "Status": ExpirationStatusType,
    },
)
_OptionalLifecycleRuleOutputTypeDef = TypedDict(
    "_OptionalLifecycleRuleOutputTypeDef",
    {
        "Expiration": LifecycleExpirationOutputTypeDef,
        "ID": str,
        "Filter": LifecycleRuleFilterOutputTypeDef,
        "Transitions": List[TransitionOutputTypeDef],
        "NoncurrentVersionTransitions": List[NoncurrentVersionTransitionOutputTypeDef],
        "NoncurrentVersionExpiration": NoncurrentVersionExpirationOutputTypeDef,
        "AbortIncompleteMultipartUpload": AbortIncompleteMultipartUploadOutputTypeDef,
    },
    total=False,
)


class LifecycleRuleOutputTypeDef(
    _RequiredLifecycleRuleOutputTypeDef, _OptionalLifecycleRuleOutputTypeDef
):
    pass


ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "NextToken": str,
        "Jobs": List[JobListDescriptorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredReplicationRuleOutputTypeDef = TypedDict(
    "_RequiredReplicationRuleOutputTypeDef",
    {
        "Status": ReplicationRuleStatusType,
        "Destination": DestinationOutputTypeDef,
        "Bucket": str,
    },
)
_OptionalReplicationRuleOutputTypeDef = TypedDict(
    "_OptionalReplicationRuleOutputTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": ReplicationRuleFilterOutputTypeDef,
        "SourceSelectionCriteria": SourceSelectionCriteriaOutputTypeDef,
        "ExistingObjectReplication": ExistingObjectReplicationOutputTypeDef,
        "DeleteMarkerReplication": DeleteMarkerReplicationOutputTypeDef,
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
        "Status": ReplicationRuleStatusType,
        "Destination": DestinationTypeDef,
        "Bucket": str,
    },
)
_OptionalReplicationRuleTypeDef = TypedDict(
    "_OptionalReplicationRuleTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": ReplicationRuleFilterTypeDef,
        "SourceSelectionCriteria": SourceSelectionCriteriaTypeDef,
        "ExistingObjectReplication": ExistingObjectReplicationTypeDef,
        "DeleteMarkerReplication": DeleteMarkerReplicationTypeDef,
    },
    total=False,
)


class ReplicationRuleTypeDef(_RequiredReplicationRuleTypeDef, _OptionalReplicationRuleTypeDef):
    pass


AsyncOperationTypeDef = TypedDict(
    "AsyncOperationTypeDef",
    {
        "CreationTime": datetime,
        "Operation": AsyncOperationNameType,
        "RequestTokenARN": str,
        "RequestParameters": AsyncRequestParametersTypeDef,
        "RequestStatus": str,
        "ResponseDetails": AsyncResponseDetailsTypeDef,
    },
    total=False,
)

BucketLevelOutputTypeDef = TypedDict(
    "BucketLevelOutputTypeDef",
    {
        "ActivityMetrics": ActivityMetricsOutputTypeDef,
        "PrefixLevel": PrefixLevelOutputTypeDef,
        "AdvancedCostOptimizationMetrics": AdvancedCostOptimizationMetricsOutputTypeDef,
        "AdvancedDataProtectionMetrics": AdvancedDataProtectionMetricsOutputTypeDef,
        "DetailedStatusCodesMetrics": DetailedStatusCodesMetricsOutputTypeDef,
    },
    total=False,
)

BucketLevelTypeDef = TypedDict(
    "BucketLevelTypeDef",
    {
        "ActivityMetrics": ActivityMetricsTypeDef,
        "PrefixLevel": PrefixLevelTypeDef,
        "AdvancedCostOptimizationMetrics": AdvancedCostOptimizationMetricsTypeDef,
        "AdvancedDataProtectionMetrics": AdvancedDataProtectionMetricsTypeDef,
        "DetailedStatusCodesMetrics": DetailedStatusCodesMetricsTypeDef,
    },
    total=False,
)

S3AccessControlPolicyOutputTypeDef = TypedDict(
    "S3AccessControlPolicyOutputTypeDef",
    {
        "AccessControlList": S3AccessControlListOutputTypeDef,
        "CannedAccessControlList": S3CannedAccessControlListType,
    },
    total=False,
)

S3AccessControlPolicyTypeDef = TypedDict(
    "S3AccessControlPolicyTypeDef",
    {
        "AccessControlList": S3AccessControlListTypeDef,
        "CannedAccessControlList": S3CannedAccessControlListType,
    },
    total=False,
)

StorageLensDataExportOutputTypeDef = TypedDict(
    "StorageLensDataExportOutputTypeDef",
    {
        "S3BucketDestination": S3BucketDestinationOutputTypeDef,
        "CloudWatchMetrics": CloudWatchMetricsOutputTypeDef,
    },
    total=False,
)

StorageLensDataExportTypeDef = TypedDict(
    "StorageLensDataExportTypeDef",
    {
        "S3BucketDestination": S3BucketDestinationTypeDef,
        "CloudWatchMetrics": CloudWatchMetricsTypeDef,
    },
    total=False,
)

GetAccessPointConfigurationForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    {
        "Configuration": ObjectLambdaConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": ObjectLambdaConfigurationTypeDef,
    },
)

PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef = TypedDict(
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": ObjectLambdaConfigurationTypeDef,
    },
)

LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef",
    {
        "Rules": Sequence[LifecycleRuleTypeDef],
    },
    total=False,
)

JobManifestGeneratorOutputTypeDef = TypedDict(
    "JobManifestGeneratorOutputTypeDef",
    {
        "S3JobManifestGenerator": S3JobManifestGeneratorOutputTypeDef,
    },
    total=False,
)

JobManifestGeneratorTypeDef = TypedDict(
    "JobManifestGeneratorTypeDef",
    {
        "S3JobManifestGenerator": S3JobManifestGeneratorTypeDef,
    },
    total=False,
)

GetBucketLifecycleConfigurationResultTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationResultTypeDef",
    {
        "Rules": List[LifecycleRuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ReplicationConfigurationOutputTypeDef = TypedDict(
    "ReplicationConfigurationOutputTypeDef",
    {
        "Role": str,
        "Rules": List[ReplicationRuleOutputTypeDef],
    },
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": Sequence[ReplicationRuleTypeDef],
    },
)

DescribeMultiRegionAccessPointOperationResultTypeDef = TypedDict(
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    {
        "AsyncOperation": AsyncOperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredAccountLevelOutputTypeDef = TypedDict(
    "_RequiredAccountLevelOutputTypeDef",
    {
        "BucketLevel": BucketLevelOutputTypeDef,
    },
)
_OptionalAccountLevelOutputTypeDef = TypedDict(
    "_OptionalAccountLevelOutputTypeDef",
    {
        "ActivityMetrics": ActivityMetricsOutputTypeDef,
        "AdvancedCostOptimizationMetrics": AdvancedCostOptimizationMetricsOutputTypeDef,
        "AdvancedDataProtectionMetrics": AdvancedDataProtectionMetricsOutputTypeDef,
        "DetailedStatusCodesMetrics": DetailedStatusCodesMetricsOutputTypeDef,
    },
    total=False,
)


class AccountLevelOutputTypeDef(
    _RequiredAccountLevelOutputTypeDef, _OptionalAccountLevelOutputTypeDef
):
    pass


_RequiredAccountLevelTypeDef = TypedDict(
    "_RequiredAccountLevelTypeDef",
    {
        "BucketLevel": BucketLevelTypeDef,
    },
)
_OptionalAccountLevelTypeDef = TypedDict(
    "_OptionalAccountLevelTypeDef",
    {
        "ActivityMetrics": ActivityMetricsTypeDef,
        "AdvancedCostOptimizationMetrics": AdvancedCostOptimizationMetricsTypeDef,
        "AdvancedDataProtectionMetrics": AdvancedDataProtectionMetricsTypeDef,
        "DetailedStatusCodesMetrics": DetailedStatusCodesMetricsTypeDef,
    },
    total=False,
)


class AccountLevelTypeDef(_RequiredAccountLevelTypeDef, _OptionalAccountLevelTypeDef):
    pass


S3SetObjectAclOperationOutputTypeDef = TypedDict(
    "S3SetObjectAclOperationOutputTypeDef",
    {
        "AccessControlPolicy": S3AccessControlPolicyOutputTypeDef,
    },
    total=False,
)

S3SetObjectAclOperationTypeDef = TypedDict(
    "S3SetObjectAclOperationTypeDef",
    {
        "AccessControlPolicy": S3AccessControlPolicyTypeDef,
    },
    total=False,
)

_RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
_OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "LifecycleConfiguration": LifecycleConfigurationTypeDef,
    },
    total=False,
)


class PutBucketLifecycleConfigurationRequestRequestTypeDef(
    _RequiredPutBucketLifecycleConfigurationRequestRequestTypeDef,
    _OptionalPutBucketLifecycleConfigurationRequestRequestTypeDef,
):
    pass


GetBucketReplicationResultTypeDef = TypedDict(
    "GetBucketReplicationResultTypeDef",
    {
        "ReplicationConfiguration": ReplicationConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutBucketReplicationRequestRequestTypeDef = TypedDict(
    "PutBucketReplicationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "ReplicationConfiguration": ReplicationConfigurationTypeDef,
    },
)

_RequiredStorageLensConfigurationOutputTypeDef = TypedDict(
    "_RequiredStorageLensConfigurationOutputTypeDef",
    {
        "Id": str,
        "AccountLevel": AccountLevelOutputTypeDef,
        "IsEnabled": bool,
    },
)
_OptionalStorageLensConfigurationOutputTypeDef = TypedDict(
    "_OptionalStorageLensConfigurationOutputTypeDef",
    {
        "Include": IncludeOutputTypeDef,
        "Exclude": ExcludeOutputTypeDef,
        "DataExport": StorageLensDataExportOutputTypeDef,
        "AwsOrg": StorageLensAwsOrgOutputTypeDef,
        "StorageLensArn": str,
    },
    total=False,
)


class StorageLensConfigurationOutputTypeDef(
    _RequiredStorageLensConfigurationOutputTypeDef, _OptionalStorageLensConfigurationOutputTypeDef
):
    pass


_RequiredStorageLensConfigurationTypeDef = TypedDict(
    "_RequiredStorageLensConfigurationTypeDef",
    {
        "Id": str,
        "AccountLevel": AccountLevelTypeDef,
        "IsEnabled": bool,
    },
)
_OptionalStorageLensConfigurationTypeDef = TypedDict(
    "_OptionalStorageLensConfigurationTypeDef",
    {
        "Include": IncludeTypeDef,
        "Exclude": ExcludeTypeDef,
        "DataExport": StorageLensDataExportTypeDef,
        "AwsOrg": StorageLensAwsOrgTypeDef,
        "StorageLensArn": str,
    },
    total=False,
)


class StorageLensConfigurationTypeDef(
    _RequiredStorageLensConfigurationTypeDef, _OptionalStorageLensConfigurationTypeDef
):
    pass


JobOperationOutputTypeDef = TypedDict(
    "JobOperationOutputTypeDef",
    {
        "LambdaInvoke": LambdaInvokeOperationOutputTypeDef,
        "S3PutObjectCopy": S3CopyObjectOperationOutputTypeDef,
        "S3PutObjectAcl": S3SetObjectAclOperationOutputTypeDef,
        "S3PutObjectTagging": S3SetObjectTaggingOperationOutputTypeDef,
        "S3DeleteObjectTagging": Dict[str, Any],
        "S3InitiateRestoreObject": S3InitiateRestoreObjectOperationOutputTypeDef,
        "S3PutObjectLegalHold": S3SetObjectLegalHoldOperationOutputTypeDef,
        "S3PutObjectRetention": S3SetObjectRetentionOperationOutputTypeDef,
        "S3ReplicateObject": Dict[str, Any],
    },
    total=False,
)

JobOperationTypeDef = TypedDict(
    "JobOperationTypeDef",
    {
        "LambdaInvoke": LambdaInvokeOperationTypeDef,
        "S3PutObjectCopy": S3CopyObjectOperationTypeDef,
        "S3PutObjectAcl": S3SetObjectAclOperationTypeDef,
        "S3PutObjectTagging": S3SetObjectTaggingOperationTypeDef,
        "S3DeleteObjectTagging": Mapping[str, Any],
        "S3InitiateRestoreObject": S3InitiateRestoreObjectOperationTypeDef,
        "S3PutObjectLegalHold": S3SetObjectLegalHoldOperationTypeDef,
        "S3PutObjectRetention": S3SetObjectRetentionOperationTypeDef,
        "S3ReplicateObject": Mapping[str, Any],
    },
    total=False,
)

GetStorageLensConfigurationResultTypeDef = TypedDict(
    "GetStorageLensConfigurationResultTypeDef",
    {
        "StorageLensConfiguration": StorageLensConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredPutStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "StorageLensConfiguration": StorageLensConfigurationTypeDef,
    },
)
_OptionalPutStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutStorageLensConfigurationRequestRequestTypeDef",
    {
        "Tags": Sequence[StorageLensTagTypeDef],
    },
    total=False,
)


class PutStorageLensConfigurationRequestRequestTypeDef(
    _RequiredPutStorageLensConfigurationRequestRequestTypeDef,
    _OptionalPutStorageLensConfigurationRequestRequestTypeDef,
):
    pass


JobDescriptorTypeDef = TypedDict(
    "JobDescriptorTypeDef",
    {
        "JobId": str,
        "ConfirmationRequired": bool,
        "Description": str,
        "JobArn": str,
        "Status": JobStatusType,
        "Manifest": JobManifestOutputTypeDef,
        "Operation": JobOperationOutputTypeDef,
        "Priority": int,
        "ProgressSummary": JobProgressSummaryTypeDef,
        "StatusUpdateReason": str,
        "FailureReasons": List[JobFailureTypeDef],
        "Report": JobReportOutputTypeDef,
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "RoleArn": str,
        "SuspendedDate": datetime,
        "SuspendedCause": str,
        "ManifestGenerator": JobManifestGeneratorOutputTypeDef,
        "GeneratedManifestDescriptor": S3GeneratedManifestDescriptorTypeDef,
    },
    total=False,
)

_RequiredCreateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestRequestTypeDef",
    {
        "AccountId": str,
        "Operation": JobOperationTypeDef,
        "Report": JobReportTypeDef,
        "ClientRequestToken": str,
        "Priority": int,
        "RoleArn": str,
    },
)
_OptionalCreateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestRequestTypeDef",
    {
        "ConfirmationRequired": bool,
        "Manifest": JobManifestTypeDef,
        "Description": str,
        "Tags": Sequence[S3TagTypeDef],
        "ManifestGenerator": JobManifestGeneratorTypeDef,
    },
    total=False,
)


class CreateJobRequestRequestTypeDef(
    _RequiredCreateJobRequestRequestTypeDef, _OptionalCreateJobRequestRequestTypeDef
):
    pass


DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "Job": JobDescriptorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
