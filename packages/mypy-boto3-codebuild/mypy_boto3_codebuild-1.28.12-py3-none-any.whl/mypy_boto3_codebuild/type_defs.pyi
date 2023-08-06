"""
Type annotations for codebuild service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/type_defs/)

Usage::

    ```python
    from mypy_boto3_codebuild.type_defs import BatchDeleteBuildsInputRequestTypeDef

    data: BatchDeleteBuildsInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    ArtifactNamespaceType,
    ArtifactPackagingType,
    ArtifactsTypeType,
    AuthTypeType,
    BatchReportModeTypeType,
    BucketOwnerAccessType,
    BuildBatchPhaseTypeType,
    BuildPhaseTypeType,
    CacheModeType,
    CacheTypeType,
    ComputeTypeType,
    EnvironmentTypeType,
    EnvironmentVariableTypeType,
    ImagePullCredentialsTypeType,
    LanguageTypeType,
    LogsConfigStatusTypeType,
    PlatformTypeType,
    ProjectSortByTypeType,
    ProjectVisibilityTypeType,
    ReportCodeCoverageSortByTypeType,
    ReportExportConfigTypeType,
    ReportGroupSortByTypeType,
    ReportGroupStatusTypeType,
    ReportGroupTrendFieldTypeType,
    ReportPackagingTypeType,
    ReportStatusTypeType,
    ReportTypeType,
    RetryBuildBatchTypeType,
    ServerTypeType,
    SharedResourceSortByTypeType,
    SortOrderTypeType,
    SourceTypeType,
    StatusTypeType,
    WebhookBuildTypeType,
    WebhookFilterTypeType,
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
    "BatchDeleteBuildsInputRequestTypeDef",
    "BuildNotDeletedTypeDef",
    "BatchGetBuildBatchesInputRequestTypeDef",
    "BatchGetBuildsInputRequestTypeDef",
    "BatchGetProjectsInputRequestTypeDef",
    "BatchGetReportGroupsInputRequestTypeDef",
    "BatchGetReportsInputRequestTypeDef",
    "BatchRestrictionsOutputTypeDef",
    "BatchRestrictionsTypeDef",
    "BuildArtifactsTypeDef",
    "BuildBatchFilterTypeDef",
    "PhaseContextTypeDef",
    "ProjectCacheOutputTypeDef",
    "ProjectFileSystemLocationOutputTypeDef",
    "ProjectSourceVersionOutputTypeDef",
    "VpcConfigOutputTypeDef",
    "BuildStatusConfigOutputTypeDef",
    "BuildStatusConfigTypeDef",
    "ResolvedArtifactTypeDef",
    "DebugSessionTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "NetworkInterfaceTypeDef",
    "CloudWatchLogsConfigOutputTypeDef",
    "CloudWatchLogsConfigTypeDef",
    "CodeCoverageReportSummaryTypeDef",
    "CodeCoverageTypeDef",
    "ProjectArtifactsTypeDef",
    "ProjectCacheTypeDef",
    "ProjectFileSystemLocationTypeDef",
    "ProjectSourceVersionTypeDef",
    "TagTypeDef",
    "VpcConfigTypeDef",
    "WebhookFilterTypeDef",
    "DeleteBuildBatchInputRequestTypeDef",
    "DeleteProjectInputRequestTypeDef",
    "DeleteReportGroupInputRequestTypeDef",
    "DeleteReportInputRequestTypeDef",
    "DeleteResourcePolicyInputRequestTypeDef",
    "DeleteSourceCredentialsInputRequestTypeDef",
    "DeleteSourceCredentialsOutputTypeDef",
    "DeleteWebhookInputRequestTypeDef",
    "DescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef",
    "DescribeCodeCoveragesInputRequestTypeDef",
    "TestCaseFilterTypeDef",
    "TestCaseTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentVariableOutputTypeDef",
    "EnvironmentVariableTypeDef",
    "GetReportGroupTrendInputRequestTypeDef",
    "ReportGroupTrendStatsTypeDef",
    "ReportWithRawDataTypeDef",
    "GetResourcePolicyInputRequestTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GitSubmodulesConfigOutputTypeDef",
    "GitSubmodulesConfigTypeDef",
    "ImportSourceCredentialsInputRequestTypeDef",
    "ImportSourceCredentialsOutputTypeDef",
    "InvalidateProjectCacheInputRequestTypeDef",
    "ListBuildBatchesForProjectOutputTypeDef",
    "ListBuildBatchesOutputTypeDef",
    "ListBuildsForProjectInputListBuildsForProjectPaginateTypeDef",
    "ListBuildsForProjectInputRequestTypeDef",
    "ListBuildsForProjectOutputTypeDef",
    "ListBuildsInputListBuildsPaginateTypeDef",
    "ListBuildsInputRequestTypeDef",
    "ListBuildsOutputTypeDef",
    "ListProjectsInputListProjectsPaginateTypeDef",
    "ListProjectsInputRequestTypeDef",
    "ListProjectsOutputTypeDef",
    "ListReportGroupsInputListReportGroupsPaginateTypeDef",
    "ListReportGroupsInputRequestTypeDef",
    "ListReportGroupsOutputTypeDef",
    "ReportFilterTypeDef",
    "ListReportsForReportGroupOutputTypeDef",
    "ListReportsOutputTypeDef",
    "ListSharedProjectsInputListSharedProjectsPaginateTypeDef",
    "ListSharedProjectsInputRequestTypeDef",
    "ListSharedProjectsOutputTypeDef",
    "ListSharedReportGroupsInputListSharedReportGroupsPaginateTypeDef",
    "ListSharedReportGroupsInputRequestTypeDef",
    "ListSharedReportGroupsOutputTypeDef",
    "SourceCredentialsInfoTypeDef",
    "S3LogsConfigOutputTypeDef",
    "S3LogsConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectArtifactsOutputTypeDef",
    "ProjectBadgeTypeDef",
    "RegistryCredentialOutputTypeDef",
    "RegistryCredentialTypeDef",
    "SourceAuthOutputTypeDef",
    "SourceAuthTypeDef",
    "TagOutputTypeDef",
    "PutResourcePolicyInputRequestTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "S3ReportExportConfigOutputTypeDef",
    "S3ReportExportConfigTypeDef",
    "TestReportSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "RetryBuildBatchInputRequestTypeDef",
    "RetryBuildInputRequestTypeDef",
    "StopBuildBatchInputRequestTypeDef",
    "StopBuildInputRequestTypeDef",
    "UpdateProjectVisibilityInputRequestTypeDef",
    "UpdateProjectVisibilityOutputTypeDef",
    "WebhookFilterOutputTypeDef",
    "BatchDeleteBuildsOutputTypeDef",
    "DeleteBuildBatchOutputTypeDef",
    "ProjectBuildBatchConfigOutputTypeDef",
    "ProjectBuildBatchConfigTypeDef",
    "ListBuildBatchesForProjectInputListBuildBatchesForProjectPaginateTypeDef",
    "ListBuildBatchesForProjectInputRequestTypeDef",
    "ListBuildBatchesInputListBuildBatchesPaginateTypeDef",
    "ListBuildBatchesInputRequestTypeDef",
    "BuildBatchPhaseTypeDef",
    "BuildPhaseTypeDef",
    "BuildSummaryTypeDef",
    "DescribeCodeCoveragesOutputTypeDef",
    "CreateWebhookInputRequestTypeDef",
    "UpdateWebhookInputRequestTypeDef",
    "DescribeTestCasesInputDescribeTestCasesPaginateTypeDef",
    "DescribeTestCasesInputRequestTypeDef",
    "DescribeTestCasesOutputTypeDef",
    "EnvironmentLanguageTypeDef",
    "GetReportGroupTrendOutputTypeDef",
    "ListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef",
    "ListReportsForReportGroupInputRequestTypeDef",
    "ListReportsInputListReportsPaginateTypeDef",
    "ListReportsInputRequestTypeDef",
    "ListSourceCredentialsOutputTypeDef",
    "LogsConfigOutputTypeDef",
    "LogsLocationTypeDef",
    "LogsConfigTypeDef",
    "ProjectEnvironmentOutputTypeDef",
    "ProjectEnvironmentTypeDef",
    "ProjectSourceOutputTypeDef",
    "ProjectSourceTypeDef",
    "ReportExportConfigOutputTypeDef",
    "ReportExportConfigTypeDef",
    "WebhookTypeDef",
    "BuildGroupTypeDef",
    "EnvironmentPlatformTypeDef",
    "BuildTypeDef",
    "CreateProjectInputRequestTypeDef",
    "StartBuildBatchInputRequestTypeDef",
    "StartBuildInputRequestTypeDef",
    "UpdateProjectInputRequestTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "CreateReportGroupInputRequestTypeDef",
    "UpdateReportGroupInputRequestTypeDef",
    "CreateWebhookOutputTypeDef",
    "ProjectTypeDef",
    "UpdateWebhookOutputTypeDef",
    "BuildBatchTypeDef",
    "ListCuratedEnvironmentImagesOutputTypeDef",
    "BatchGetBuildsOutputTypeDef",
    "RetryBuildOutputTypeDef",
    "StartBuildOutputTypeDef",
    "StopBuildOutputTypeDef",
    "BatchGetReportGroupsOutputTypeDef",
    "CreateReportGroupOutputTypeDef",
    "UpdateReportGroupOutputTypeDef",
    "BatchGetReportsOutputTypeDef",
    "BatchGetProjectsOutputTypeDef",
    "CreateProjectOutputTypeDef",
    "UpdateProjectOutputTypeDef",
    "BatchGetBuildBatchesOutputTypeDef",
    "RetryBuildBatchOutputTypeDef",
    "StartBuildBatchOutputTypeDef",
    "StopBuildBatchOutputTypeDef",
)

BatchDeleteBuildsInputRequestTypeDef = TypedDict(
    "BatchDeleteBuildsInputRequestTypeDef",
    {
        "ids": Sequence[str],
    },
)

BuildNotDeletedTypeDef = TypedDict(
    "BuildNotDeletedTypeDef",
    {
        "id": str,
        "statusCode": str,
    },
    total=False,
)

BatchGetBuildBatchesInputRequestTypeDef = TypedDict(
    "BatchGetBuildBatchesInputRequestTypeDef",
    {
        "ids": Sequence[str],
    },
)

BatchGetBuildsInputRequestTypeDef = TypedDict(
    "BatchGetBuildsInputRequestTypeDef",
    {
        "ids": Sequence[str],
    },
)

BatchGetProjectsInputRequestTypeDef = TypedDict(
    "BatchGetProjectsInputRequestTypeDef",
    {
        "names": Sequence[str],
    },
)

BatchGetReportGroupsInputRequestTypeDef = TypedDict(
    "BatchGetReportGroupsInputRequestTypeDef",
    {
        "reportGroupArns": Sequence[str],
    },
)

BatchGetReportsInputRequestTypeDef = TypedDict(
    "BatchGetReportsInputRequestTypeDef",
    {
        "reportArns": Sequence[str],
    },
)

BatchRestrictionsOutputTypeDef = TypedDict(
    "BatchRestrictionsOutputTypeDef",
    {
        "maximumBuildsAllowed": int,
        "computeTypesAllowed": List[str],
    },
    total=False,
)

BatchRestrictionsTypeDef = TypedDict(
    "BatchRestrictionsTypeDef",
    {
        "maximumBuildsAllowed": int,
        "computeTypesAllowed": Sequence[str],
    },
    total=False,
)

BuildArtifactsTypeDef = TypedDict(
    "BuildArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
        "bucketOwnerAccess": BucketOwnerAccessType,
    },
    total=False,
)

BuildBatchFilterTypeDef = TypedDict(
    "BuildBatchFilterTypeDef",
    {
        "status": StatusTypeType,
    },
    total=False,
)

PhaseContextTypeDef = TypedDict(
    "PhaseContextTypeDef",
    {
        "statusCode": str,
        "message": str,
    },
    total=False,
)

_RequiredProjectCacheOutputTypeDef = TypedDict(
    "_RequiredProjectCacheOutputTypeDef",
    {
        "type": CacheTypeType,
    },
)
_OptionalProjectCacheOutputTypeDef = TypedDict(
    "_OptionalProjectCacheOutputTypeDef",
    {
        "location": str,
        "modes": List[CacheModeType],
    },
    total=False,
)

class ProjectCacheOutputTypeDef(
    _RequiredProjectCacheOutputTypeDef, _OptionalProjectCacheOutputTypeDef
):
    pass

ProjectFileSystemLocationOutputTypeDef = TypedDict(
    "ProjectFileSystemLocationOutputTypeDef",
    {
        "type": Literal["EFS"],
        "location": str,
        "mountPoint": str,
        "identifier": str,
        "mountOptions": str,
    },
    total=False,
)

ProjectSourceVersionOutputTypeDef = TypedDict(
    "ProjectSourceVersionOutputTypeDef",
    {
        "sourceIdentifier": str,
        "sourceVersion": str,
    },
)

VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "vpcId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
    },
    total=False,
)

BuildStatusConfigOutputTypeDef = TypedDict(
    "BuildStatusConfigOutputTypeDef",
    {
        "context": str,
        "targetUrl": str,
    },
    total=False,
)

BuildStatusConfigTypeDef = TypedDict(
    "BuildStatusConfigTypeDef",
    {
        "context": str,
        "targetUrl": str,
    },
    total=False,
)

ResolvedArtifactTypeDef = TypedDict(
    "ResolvedArtifactTypeDef",
    {
        "type": ArtifactsTypeType,
        "location": str,
        "identifier": str,
    },
    total=False,
)

DebugSessionTypeDef = TypedDict(
    "DebugSessionTypeDef",
    {
        "sessionEnabled": bool,
        "sessionTarget": str,
    },
    total=False,
)

ExportedEnvironmentVariableTypeDef = TypedDict(
    "ExportedEnvironmentVariableTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "subnetId": str,
        "networkInterfaceId": str,
    },
    total=False,
)

_RequiredCloudWatchLogsConfigOutputTypeDef = TypedDict(
    "_RequiredCloudWatchLogsConfigOutputTypeDef",
    {
        "status": LogsConfigStatusTypeType,
    },
)
_OptionalCloudWatchLogsConfigOutputTypeDef = TypedDict(
    "_OptionalCloudWatchLogsConfigOutputTypeDef",
    {
        "groupName": str,
        "streamName": str,
    },
    total=False,
)

class CloudWatchLogsConfigOutputTypeDef(
    _RequiredCloudWatchLogsConfigOutputTypeDef, _OptionalCloudWatchLogsConfigOutputTypeDef
):
    pass

_RequiredCloudWatchLogsConfigTypeDef = TypedDict(
    "_RequiredCloudWatchLogsConfigTypeDef",
    {
        "status": LogsConfigStatusTypeType,
    },
)
_OptionalCloudWatchLogsConfigTypeDef = TypedDict(
    "_OptionalCloudWatchLogsConfigTypeDef",
    {
        "groupName": str,
        "streamName": str,
    },
    total=False,
)

class CloudWatchLogsConfigTypeDef(
    _RequiredCloudWatchLogsConfigTypeDef, _OptionalCloudWatchLogsConfigTypeDef
):
    pass

CodeCoverageReportSummaryTypeDef = TypedDict(
    "CodeCoverageReportSummaryTypeDef",
    {
        "lineCoveragePercentage": float,
        "linesCovered": int,
        "linesMissed": int,
        "branchCoveragePercentage": float,
        "branchesCovered": int,
        "branchesMissed": int,
    },
    total=False,
)

CodeCoverageTypeDef = TypedDict(
    "CodeCoverageTypeDef",
    {
        "id": str,
        "reportARN": str,
        "filePath": str,
        "lineCoveragePercentage": float,
        "linesCovered": int,
        "linesMissed": int,
        "branchCoveragePercentage": float,
        "branchesCovered": int,
        "branchesMissed": int,
        "expired": datetime,
    },
    total=False,
)

_RequiredProjectArtifactsTypeDef = TypedDict(
    "_RequiredProjectArtifactsTypeDef",
    {
        "type": ArtifactsTypeType,
    },
)
_OptionalProjectArtifactsTypeDef = TypedDict(
    "_OptionalProjectArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": ArtifactNamespaceType,
        "name": str,
        "packaging": ArtifactPackagingType,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
        "bucketOwnerAccess": BucketOwnerAccessType,
    },
    total=False,
)

class ProjectArtifactsTypeDef(_RequiredProjectArtifactsTypeDef, _OptionalProjectArtifactsTypeDef):
    pass

_RequiredProjectCacheTypeDef = TypedDict(
    "_RequiredProjectCacheTypeDef",
    {
        "type": CacheTypeType,
    },
)
_OptionalProjectCacheTypeDef = TypedDict(
    "_OptionalProjectCacheTypeDef",
    {
        "location": str,
        "modes": Sequence[CacheModeType],
    },
    total=False,
)

class ProjectCacheTypeDef(_RequiredProjectCacheTypeDef, _OptionalProjectCacheTypeDef):
    pass

ProjectFileSystemLocationTypeDef = TypedDict(
    "ProjectFileSystemLocationTypeDef",
    {
        "type": Literal["EFS"],
        "location": str,
        "mountPoint": str,
        "identifier": str,
        "mountOptions": str,
    },
    total=False,
)

ProjectSourceVersionTypeDef = TypedDict(
    "ProjectSourceVersionTypeDef",
    {
        "sourceIdentifier": str,
        "sourceVersion": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "vpcId": str,
        "subnets": Sequence[str],
        "securityGroupIds": Sequence[str],
    },
    total=False,
)

_RequiredWebhookFilterTypeDef = TypedDict(
    "_RequiredWebhookFilterTypeDef",
    {
        "type": WebhookFilterTypeType,
        "pattern": str,
    },
)
_OptionalWebhookFilterTypeDef = TypedDict(
    "_OptionalWebhookFilterTypeDef",
    {
        "excludeMatchedPattern": bool,
    },
    total=False,
)

class WebhookFilterTypeDef(_RequiredWebhookFilterTypeDef, _OptionalWebhookFilterTypeDef):
    pass

DeleteBuildBatchInputRequestTypeDef = TypedDict(
    "DeleteBuildBatchInputRequestTypeDef",
    {
        "id": str,
    },
)

DeleteProjectInputRequestTypeDef = TypedDict(
    "DeleteProjectInputRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredDeleteReportGroupInputRequestTypeDef = TypedDict(
    "_RequiredDeleteReportGroupInputRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalDeleteReportGroupInputRequestTypeDef = TypedDict(
    "_OptionalDeleteReportGroupInputRequestTypeDef",
    {
        "deleteReports": bool,
    },
    total=False,
)

class DeleteReportGroupInputRequestTypeDef(
    _RequiredDeleteReportGroupInputRequestTypeDef, _OptionalDeleteReportGroupInputRequestTypeDef
):
    pass

DeleteReportInputRequestTypeDef = TypedDict(
    "DeleteReportInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteResourcePolicyInputRequestTypeDef = TypedDict(
    "DeleteResourcePolicyInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

DeleteSourceCredentialsInputRequestTypeDef = TypedDict(
    "DeleteSourceCredentialsInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteSourceCredentialsOutputTypeDef = TypedDict(
    "DeleteSourceCredentialsOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWebhookInputRequestTypeDef = TypedDict(
    "DeleteWebhookInputRequestTypeDef",
    {
        "projectName": str,
    },
)

_RequiredDescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef = TypedDict(
    "_RequiredDescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef",
    {
        "reportArn": str,
    },
)
_OptionalDescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef = TypedDict(
    "_OptionalDescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "sortBy": ReportCodeCoverageSortByTypeType,
        "minLineCoveragePercentage": float,
        "maxLineCoveragePercentage": float,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class DescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef(
    _RequiredDescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef,
    _OptionalDescribeCodeCoveragesInputDescribeCodeCoveragesPaginateTypeDef,
):
    pass

_RequiredDescribeCodeCoveragesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeCodeCoveragesInputRequestTypeDef",
    {
        "reportArn": str,
    },
)
_OptionalDescribeCodeCoveragesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeCodeCoveragesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "sortOrder": SortOrderTypeType,
        "sortBy": ReportCodeCoverageSortByTypeType,
        "minLineCoveragePercentage": float,
        "maxLineCoveragePercentage": float,
    },
    total=False,
)

class DescribeCodeCoveragesInputRequestTypeDef(
    _RequiredDescribeCodeCoveragesInputRequestTypeDef,
    _OptionalDescribeCodeCoveragesInputRequestTypeDef,
):
    pass

TestCaseFilterTypeDef = TypedDict(
    "TestCaseFilterTypeDef",
    {
        "status": str,
        "keyword": str,
    },
    total=False,
)

TestCaseTypeDef = TypedDict(
    "TestCaseTypeDef",
    {
        "reportArn": str,
        "testRawDataPath": str,
        "prefix": str,
        "name": str,
        "status": str,
        "durationInNanoSeconds": int,
        "message": str,
        "expired": datetime,
    },
    total=False,
)

EnvironmentImageTypeDef = TypedDict(
    "EnvironmentImageTypeDef",
    {
        "name": str,
        "description": str,
        "versions": List[str],
    },
    total=False,
)

_RequiredEnvironmentVariableOutputTypeDef = TypedDict(
    "_RequiredEnvironmentVariableOutputTypeDef",
    {
        "name": str,
        "value": str,
    },
)
_OptionalEnvironmentVariableOutputTypeDef = TypedDict(
    "_OptionalEnvironmentVariableOutputTypeDef",
    {
        "type": EnvironmentVariableTypeType,
    },
    total=False,
)

class EnvironmentVariableOutputTypeDef(
    _RequiredEnvironmentVariableOutputTypeDef, _OptionalEnvironmentVariableOutputTypeDef
):
    pass

_RequiredEnvironmentVariableTypeDef = TypedDict(
    "_RequiredEnvironmentVariableTypeDef",
    {
        "name": str,
        "value": str,
    },
)
_OptionalEnvironmentVariableTypeDef = TypedDict(
    "_OptionalEnvironmentVariableTypeDef",
    {
        "type": EnvironmentVariableTypeType,
    },
    total=False,
)

class EnvironmentVariableTypeDef(
    _RequiredEnvironmentVariableTypeDef, _OptionalEnvironmentVariableTypeDef
):
    pass

_RequiredGetReportGroupTrendInputRequestTypeDef = TypedDict(
    "_RequiredGetReportGroupTrendInputRequestTypeDef",
    {
        "reportGroupArn": str,
        "trendField": ReportGroupTrendFieldTypeType,
    },
)
_OptionalGetReportGroupTrendInputRequestTypeDef = TypedDict(
    "_OptionalGetReportGroupTrendInputRequestTypeDef",
    {
        "numOfReports": int,
    },
    total=False,
)

class GetReportGroupTrendInputRequestTypeDef(
    _RequiredGetReportGroupTrendInputRequestTypeDef, _OptionalGetReportGroupTrendInputRequestTypeDef
):
    pass

ReportGroupTrendStatsTypeDef = TypedDict(
    "ReportGroupTrendStatsTypeDef",
    {
        "average": str,
        "max": str,
        "min": str,
    },
    total=False,
)

ReportWithRawDataTypeDef = TypedDict(
    "ReportWithRawDataTypeDef",
    {
        "reportArn": str,
        "data": str,
    },
    total=False,
)

GetResourcePolicyInputRequestTypeDef = TypedDict(
    "GetResourcePolicyInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

GetResourcePolicyOutputTypeDef = TypedDict(
    "GetResourcePolicyOutputTypeDef",
    {
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitSubmodulesConfigOutputTypeDef = TypedDict(
    "GitSubmodulesConfigOutputTypeDef",
    {
        "fetchSubmodules": bool,
    },
)

GitSubmodulesConfigTypeDef = TypedDict(
    "GitSubmodulesConfigTypeDef",
    {
        "fetchSubmodules": bool,
    },
)

_RequiredImportSourceCredentialsInputRequestTypeDef = TypedDict(
    "_RequiredImportSourceCredentialsInputRequestTypeDef",
    {
        "token": str,
        "serverType": ServerTypeType,
        "authType": AuthTypeType,
    },
)
_OptionalImportSourceCredentialsInputRequestTypeDef = TypedDict(
    "_OptionalImportSourceCredentialsInputRequestTypeDef",
    {
        "username": str,
        "shouldOverwrite": bool,
    },
    total=False,
)

class ImportSourceCredentialsInputRequestTypeDef(
    _RequiredImportSourceCredentialsInputRequestTypeDef,
    _OptionalImportSourceCredentialsInputRequestTypeDef,
):
    pass

ImportSourceCredentialsOutputTypeDef = TypedDict(
    "ImportSourceCredentialsOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvalidateProjectCacheInputRequestTypeDef = TypedDict(
    "InvalidateProjectCacheInputRequestTypeDef",
    {
        "projectName": str,
    },
)

ListBuildBatchesForProjectOutputTypeDef = TypedDict(
    "ListBuildBatchesForProjectOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildBatchesOutputTypeDef = TypedDict(
    "ListBuildBatchesOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBuildsForProjectInputListBuildsForProjectPaginateTypeDef = TypedDict(
    "_RequiredListBuildsForProjectInputListBuildsForProjectPaginateTypeDef",
    {
        "projectName": str,
    },
)
_OptionalListBuildsForProjectInputListBuildsForProjectPaginateTypeDef = TypedDict(
    "_OptionalListBuildsForProjectInputListBuildsForProjectPaginateTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListBuildsForProjectInputListBuildsForProjectPaginateTypeDef(
    _RequiredListBuildsForProjectInputListBuildsForProjectPaginateTypeDef,
    _OptionalListBuildsForProjectInputListBuildsForProjectPaginateTypeDef,
):
    pass

_RequiredListBuildsForProjectInputRequestTypeDef = TypedDict(
    "_RequiredListBuildsForProjectInputRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalListBuildsForProjectInputRequestTypeDef = TypedDict(
    "_OptionalListBuildsForProjectInputRequestTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

class ListBuildsForProjectInputRequestTypeDef(
    _RequiredListBuildsForProjectInputRequestTypeDef,
    _OptionalListBuildsForProjectInputRequestTypeDef,
):
    pass

ListBuildsForProjectOutputTypeDef = TypedDict(
    "ListBuildsForProjectOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsInputListBuildsPaginateTypeDef = TypedDict(
    "ListBuildsInputListBuildsPaginateTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListBuildsInputRequestTypeDef = TypedDict(
    "ListBuildsInputRequestTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsInputListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsInputListProjectsPaginateTypeDef",
    {
        "sortBy": ProjectSortByTypeType,
        "sortOrder": SortOrderTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListProjectsInputRequestTypeDef = TypedDict(
    "ListProjectsInputRequestTypeDef",
    {
        "sortBy": ProjectSortByTypeType,
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "nextToken": str,
        "projects": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportGroupsInputListReportGroupsPaginateTypeDef = TypedDict(
    "ListReportGroupsInputListReportGroupsPaginateTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "sortBy": ReportGroupSortByTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListReportGroupsInputRequestTypeDef = TypedDict(
    "ListReportGroupsInputRequestTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "sortBy": ReportGroupSortByTypeType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListReportGroupsOutputTypeDef = TypedDict(
    "ListReportGroupsOutputTypeDef",
    {
        "nextToken": str,
        "reportGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportFilterTypeDef = TypedDict(
    "ReportFilterTypeDef",
    {
        "status": ReportStatusTypeType,
    },
    total=False,
)

ListReportsForReportGroupOutputTypeDef = TypedDict(
    "ListReportsForReportGroupOutputTypeDef",
    {
        "nextToken": str,
        "reports": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportsOutputTypeDef = TypedDict(
    "ListReportsOutputTypeDef",
    {
        "nextToken": str,
        "reports": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedProjectsInputListSharedProjectsPaginateTypeDef = TypedDict(
    "ListSharedProjectsInputListSharedProjectsPaginateTypeDef",
    {
        "sortBy": SharedResourceSortByTypeType,
        "sortOrder": SortOrderTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSharedProjectsInputRequestTypeDef = TypedDict(
    "ListSharedProjectsInputRequestTypeDef",
    {
        "sortBy": SharedResourceSortByTypeType,
        "sortOrder": SortOrderTypeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSharedProjectsOutputTypeDef = TypedDict(
    "ListSharedProjectsOutputTypeDef",
    {
        "nextToken": str,
        "projects": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedReportGroupsInputListSharedReportGroupsPaginateTypeDef = TypedDict(
    "ListSharedReportGroupsInputListSharedReportGroupsPaginateTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "sortBy": SharedResourceSortByTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSharedReportGroupsInputRequestTypeDef = TypedDict(
    "ListSharedReportGroupsInputRequestTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "sortBy": SharedResourceSortByTypeType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSharedReportGroupsOutputTypeDef = TypedDict(
    "ListSharedReportGroupsOutputTypeDef",
    {
        "nextToken": str,
        "reportGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceCredentialsInfoTypeDef = TypedDict(
    "SourceCredentialsInfoTypeDef",
    {
        "arn": str,
        "serverType": ServerTypeType,
        "authType": AuthTypeType,
    },
    total=False,
)

_RequiredS3LogsConfigOutputTypeDef = TypedDict(
    "_RequiredS3LogsConfigOutputTypeDef",
    {
        "status": LogsConfigStatusTypeType,
    },
)
_OptionalS3LogsConfigOutputTypeDef = TypedDict(
    "_OptionalS3LogsConfigOutputTypeDef",
    {
        "location": str,
        "encryptionDisabled": bool,
        "bucketOwnerAccess": BucketOwnerAccessType,
    },
    total=False,
)

class S3LogsConfigOutputTypeDef(
    _RequiredS3LogsConfigOutputTypeDef, _OptionalS3LogsConfigOutputTypeDef
):
    pass

_RequiredS3LogsConfigTypeDef = TypedDict(
    "_RequiredS3LogsConfigTypeDef",
    {
        "status": LogsConfigStatusTypeType,
    },
)
_OptionalS3LogsConfigTypeDef = TypedDict(
    "_OptionalS3LogsConfigTypeDef",
    {
        "location": str,
        "encryptionDisabled": bool,
        "bucketOwnerAccess": BucketOwnerAccessType,
    },
    total=False,
)

class S3LogsConfigTypeDef(_RequiredS3LogsConfigTypeDef, _OptionalS3LogsConfigTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredProjectArtifactsOutputTypeDef = TypedDict(
    "_RequiredProjectArtifactsOutputTypeDef",
    {
        "type": ArtifactsTypeType,
    },
)
_OptionalProjectArtifactsOutputTypeDef = TypedDict(
    "_OptionalProjectArtifactsOutputTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": ArtifactNamespaceType,
        "name": str,
        "packaging": ArtifactPackagingType,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
        "bucketOwnerAccess": BucketOwnerAccessType,
    },
    total=False,
)

class ProjectArtifactsOutputTypeDef(
    _RequiredProjectArtifactsOutputTypeDef, _OptionalProjectArtifactsOutputTypeDef
):
    pass

ProjectBadgeTypeDef = TypedDict(
    "ProjectBadgeTypeDef",
    {
        "badgeEnabled": bool,
        "badgeRequestUrl": str,
    },
    total=False,
)

RegistryCredentialOutputTypeDef = TypedDict(
    "RegistryCredentialOutputTypeDef",
    {
        "credential": str,
        "credentialProvider": Literal["SECRETS_MANAGER"],
    },
)

RegistryCredentialTypeDef = TypedDict(
    "RegistryCredentialTypeDef",
    {
        "credential": str,
        "credentialProvider": Literal["SECRETS_MANAGER"],
    },
)

_RequiredSourceAuthOutputTypeDef = TypedDict(
    "_RequiredSourceAuthOutputTypeDef",
    {
        "type": Literal["OAUTH"],
    },
)
_OptionalSourceAuthOutputTypeDef = TypedDict(
    "_OptionalSourceAuthOutputTypeDef",
    {
        "resource": str,
    },
    total=False,
)

class SourceAuthOutputTypeDef(_RequiredSourceAuthOutputTypeDef, _OptionalSourceAuthOutputTypeDef):
    pass

_RequiredSourceAuthTypeDef = TypedDict(
    "_RequiredSourceAuthTypeDef",
    {
        "type": Literal["OAUTH"],
    },
)
_OptionalSourceAuthTypeDef = TypedDict(
    "_OptionalSourceAuthTypeDef",
    {
        "resource": str,
    },
    total=False,
)

class SourceAuthTypeDef(_RequiredSourceAuthTypeDef, _OptionalSourceAuthTypeDef):
    pass

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

PutResourcePolicyInputRequestTypeDef = TypedDict(
    "PutResourcePolicyInputRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ReportExportConfigOutputTypeDef = TypedDict(
    "S3ReportExportConfigOutputTypeDef",
    {
        "bucket": str,
        "bucketOwner": str,
        "path": str,
        "packaging": ReportPackagingTypeType,
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

S3ReportExportConfigTypeDef = TypedDict(
    "S3ReportExportConfigTypeDef",
    {
        "bucket": str,
        "bucketOwner": str,
        "path": str,
        "packaging": ReportPackagingTypeType,
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

TestReportSummaryTypeDef = TypedDict(
    "TestReportSummaryTypeDef",
    {
        "total": int,
        "statusCounts": Dict[str, int],
        "durationInNanoSeconds": int,
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

RetryBuildBatchInputRequestTypeDef = TypedDict(
    "RetryBuildBatchInputRequestTypeDef",
    {
        "id": str,
        "idempotencyToken": str,
        "retryType": RetryBuildBatchTypeType,
    },
    total=False,
)

RetryBuildInputRequestTypeDef = TypedDict(
    "RetryBuildInputRequestTypeDef",
    {
        "id": str,
        "idempotencyToken": str,
    },
    total=False,
)

StopBuildBatchInputRequestTypeDef = TypedDict(
    "StopBuildBatchInputRequestTypeDef",
    {
        "id": str,
    },
)

StopBuildInputRequestTypeDef = TypedDict(
    "StopBuildInputRequestTypeDef",
    {
        "id": str,
    },
)

_RequiredUpdateProjectVisibilityInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectVisibilityInputRequestTypeDef",
    {
        "projectArn": str,
        "projectVisibility": ProjectVisibilityTypeType,
    },
)
_OptionalUpdateProjectVisibilityInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectVisibilityInputRequestTypeDef",
    {
        "resourceAccessRole": str,
    },
    total=False,
)

class UpdateProjectVisibilityInputRequestTypeDef(
    _RequiredUpdateProjectVisibilityInputRequestTypeDef,
    _OptionalUpdateProjectVisibilityInputRequestTypeDef,
):
    pass

UpdateProjectVisibilityOutputTypeDef = TypedDict(
    "UpdateProjectVisibilityOutputTypeDef",
    {
        "projectArn": str,
        "publicProjectAlias": str,
        "projectVisibility": ProjectVisibilityTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredWebhookFilterOutputTypeDef = TypedDict(
    "_RequiredWebhookFilterOutputTypeDef",
    {
        "type": WebhookFilterTypeType,
        "pattern": str,
    },
)
_OptionalWebhookFilterOutputTypeDef = TypedDict(
    "_OptionalWebhookFilterOutputTypeDef",
    {
        "excludeMatchedPattern": bool,
    },
    total=False,
)

class WebhookFilterOutputTypeDef(
    _RequiredWebhookFilterOutputTypeDef, _OptionalWebhookFilterOutputTypeDef
):
    pass

BatchDeleteBuildsOutputTypeDef = TypedDict(
    "BatchDeleteBuildsOutputTypeDef",
    {
        "buildsDeleted": List[str],
        "buildsNotDeleted": List[BuildNotDeletedTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBuildBatchOutputTypeDef = TypedDict(
    "DeleteBuildBatchOutputTypeDef",
    {
        "statusCode": str,
        "buildsDeleted": List[str],
        "buildsNotDeleted": List[BuildNotDeletedTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProjectBuildBatchConfigOutputTypeDef = TypedDict(
    "ProjectBuildBatchConfigOutputTypeDef",
    {
        "serviceRole": str,
        "combineArtifacts": bool,
        "restrictions": BatchRestrictionsOutputTypeDef,
        "timeoutInMins": int,
        "batchReportMode": BatchReportModeTypeType,
    },
    total=False,
)

ProjectBuildBatchConfigTypeDef = TypedDict(
    "ProjectBuildBatchConfigTypeDef",
    {
        "serviceRole": str,
        "combineArtifacts": bool,
        "restrictions": BatchRestrictionsTypeDef,
        "timeoutInMins": int,
        "batchReportMode": BatchReportModeTypeType,
    },
    total=False,
)

ListBuildBatchesForProjectInputListBuildBatchesForProjectPaginateTypeDef = TypedDict(
    "ListBuildBatchesForProjectInputListBuildBatchesForProjectPaginateTypeDef",
    {
        "projectName": str,
        "filter": BuildBatchFilterTypeDef,
        "sortOrder": SortOrderTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListBuildBatchesForProjectInputRequestTypeDef = TypedDict(
    "ListBuildBatchesForProjectInputRequestTypeDef",
    {
        "projectName": str,
        "filter": BuildBatchFilterTypeDef,
        "maxResults": int,
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

ListBuildBatchesInputListBuildBatchesPaginateTypeDef = TypedDict(
    "ListBuildBatchesInputListBuildBatchesPaginateTypeDef",
    {
        "filter": BuildBatchFilterTypeDef,
        "sortOrder": SortOrderTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListBuildBatchesInputRequestTypeDef = TypedDict(
    "ListBuildBatchesInputRequestTypeDef",
    {
        "filter": BuildBatchFilterTypeDef,
        "maxResults": int,
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

BuildBatchPhaseTypeDef = TypedDict(
    "BuildBatchPhaseTypeDef",
    {
        "phaseType": BuildBatchPhaseTypeType,
        "phaseStatus": StatusTypeType,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[PhaseContextTypeDef],
    },
    total=False,
)

BuildPhaseTypeDef = TypedDict(
    "BuildPhaseTypeDef",
    {
        "phaseType": BuildPhaseTypeType,
        "phaseStatus": StatusTypeType,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[PhaseContextTypeDef],
    },
    total=False,
)

BuildSummaryTypeDef = TypedDict(
    "BuildSummaryTypeDef",
    {
        "arn": str,
        "requestedOn": datetime,
        "buildStatus": StatusTypeType,
        "primaryArtifact": ResolvedArtifactTypeDef,
        "secondaryArtifacts": List[ResolvedArtifactTypeDef],
    },
    total=False,
)

DescribeCodeCoveragesOutputTypeDef = TypedDict(
    "DescribeCodeCoveragesOutputTypeDef",
    {
        "nextToken": str,
        "codeCoverages": List[CodeCoverageTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWebhookInputRequestTypeDef = TypedDict(
    "_RequiredCreateWebhookInputRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalCreateWebhookInputRequestTypeDef = TypedDict(
    "_OptionalCreateWebhookInputRequestTypeDef",
    {
        "branchFilter": str,
        "filterGroups": Sequence[Sequence[WebhookFilterTypeDef]],
        "buildType": WebhookBuildTypeType,
    },
    total=False,
)

class CreateWebhookInputRequestTypeDef(
    _RequiredCreateWebhookInputRequestTypeDef, _OptionalCreateWebhookInputRequestTypeDef
):
    pass

_RequiredUpdateWebhookInputRequestTypeDef = TypedDict(
    "_RequiredUpdateWebhookInputRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalUpdateWebhookInputRequestTypeDef = TypedDict(
    "_OptionalUpdateWebhookInputRequestTypeDef",
    {
        "branchFilter": str,
        "rotateSecret": bool,
        "filterGroups": Sequence[Sequence[WebhookFilterTypeDef]],
        "buildType": WebhookBuildTypeType,
    },
    total=False,
)

class UpdateWebhookInputRequestTypeDef(
    _RequiredUpdateWebhookInputRequestTypeDef, _OptionalUpdateWebhookInputRequestTypeDef
):
    pass

_RequiredDescribeTestCasesInputDescribeTestCasesPaginateTypeDef = TypedDict(
    "_RequiredDescribeTestCasesInputDescribeTestCasesPaginateTypeDef",
    {
        "reportArn": str,
    },
)
_OptionalDescribeTestCasesInputDescribeTestCasesPaginateTypeDef = TypedDict(
    "_OptionalDescribeTestCasesInputDescribeTestCasesPaginateTypeDef",
    {
        "filter": TestCaseFilterTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class DescribeTestCasesInputDescribeTestCasesPaginateTypeDef(
    _RequiredDescribeTestCasesInputDescribeTestCasesPaginateTypeDef,
    _OptionalDescribeTestCasesInputDescribeTestCasesPaginateTypeDef,
):
    pass

_RequiredDescribeTestCasesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeTestCasesInputRequestTypeDef",
    {
        "reportArn": str,
    },
)
_OptionalDescribeTestCasesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeTestCasesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filter": TestCaseFilterTypeDef,
    },
    total=False,
)

class DescribeTestCasesInputRequestTypeDef(
    _RequiredDescribeTestCasesInputRequestTypeDef, _OptionalDescribeTestCasesInputRequestTypeDef
):
    pass

DescribeTestCasesOutputTypeDef = TypedDict(
    "DescribeTestCasesOutputTypeDef",
    {
        "nextToken": str,
        "testCases": List[TestCaseTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentLanguageTypeDef = TypedDict(
    "EnvironmentLanguageTypeDef",
    {
        "language": LanguageTypeType,
        "images": List[EnvironmentImageTypeDef],
    },
    total=False,
)

GetReportGroupTrendOutputTypeDef = TypedDict(
    "GetReportGroupTrendOutputTypeDef",
    {
        "stats": ReportGroupTrendStatsTypeDef,
        "rawData": List[ReportWithRawDataTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef = TypedDict(
    "_RequiredListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef",
    {
        "reportGroupArn": str,
    },
)
_OptionalListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef = TypedDict(
    "_OptionalListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "filter": ReportFilterTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef(
    _RequiredListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef,
    _OptionalListReportsForReportGroupInputListReportsForReportGroupPaginateTypeDef,
):
    pass

_RequiredListReportsForReportGroupInputRequestTypeDef = TypedDict(
    "_RequiredListReportsForReportGroupInputRequestTypeDef",
    {
        "reportGroupArn": str,
    },
)
_OptionalListReportsForReportGroupInputRequestTypeDef = TypedDict(
    "_OptionalListReportsForReportGroupInputRequestTypeDef",
    {
        "nextToken": str,
        "sortOrder": SortOrderTypeType,
        "maxResults": int,
        "filter": ReportFilterTypeDef,
    },
    total=False,
)

class ListReportsForReportGroupInputRequestTypeDef(
    _RequiredListReportsForReportGroupInputRequestTypeDef,
    _OptionalListReportsForReportGroupInputRequestTypeDef,
):
    pass

ListReportsInputListReportsPaginateTypeDef = TypedDict(
    "ListReportsInputListReportsPaginateTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "filter": ReportFilterTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListReportsInputRequestTypeDef = TypedDict(
    "ListReportsInputRequestTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
        "maxResults": int,
        "filter": ReportFilterTypeDef,
    },
    total=False,
)

ListSourceCredentialsOutputTypeDef = TypedDict(
    "ListSourceCredentialsOutputTypeDef",
    {
        "sourceCredentialsInfos": List[SourceCredentialsInfoTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogsConfigOutputTypeDef = TypedDict(
    "LogsConfigOutputTypeDef",
    {
        "cloudWatchLogs": CloudWatchLogsConfigOutputTypeDef,
        "s3Logs": S3LogsConfigOutputTypeDef,
    },
    total=False,
)

LogsLocationTypeDef = TypedDict(
    "LogsLocationTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": CloudWatchLogsConfigOutputTypeDef,
        "s3Logs": S3LogsConfigOutputTypeDef,
    },
    total=False,
)

LogsConfigTypeDef = TypedDict(
    "LogsConfigTypeDef",
    {
        "cloudWatchLogs": CloudWatchLogsConfigTypeDef,
        "s3Logs": S3LogsConfigTypeDef,
    },
    total=False,
)

_RequiredProjectEnvironmentOutputTypeDef = TypedDict(
    "_RequiredProjectEnvironmentOutputTypeDef",
    {
        "type": EnvironmentTypeType,
        "image": str,
        "computeType": ComputeTypeType,
    },
)
_OptionalProjectEnvironmentOutputTypeDef = TypedDict(
    "_OptionalProjectEnvironmentOutputTypeDef",
    {
        "environmentVariables": List[EnvironmentVariableOutputTypeDef],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": RegistryCredentialOutputTypeDef,
        "imagePullCredentialsType": ImagePullCredentialsTypeType,
    },
    total=False,
)

class ProjectEnvironmentOutputTypeDef(
    _RequiredProjectEnvironmentOutputTypeDef, _OptionalProjectEnvironmentOutputTypeDef
):
    pass

_RequiredProjectEnvironmentTypeDef = TypedDict(
    "_RequiredProjectEnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "image": str,
        "computeType": ComputeTypeType,
    },
)
_OptionalProjectEnvironmentTypeDef = TypedDict(
    "_OptionalProjectEnvironmentTypeDef",
    {
        "environmentVariables": Sequence[EnvironmentVariableTypeDef],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": RegistryCredentialTypeDef,
        "imagePullCredentialsType": ImagePullCredentialsTypeType,
    },
    total=False,
)

class ProjectEnvironmentTypeDef(
    _RequiredProjectEnvironmentTypeDef, _OptionalProjectEnvironmentTypeDef
):
    pass

_RequiredProjectSourceOutputTypeDef = TypedDict(
    "_RequiredProjectSourceOutputTypeDef",
    {
        "type": SourceTypeType,
    },
)
_OptionalProjectSourceOutputTypeDef = TypedDict(
    "_OptionalProjectSourceOutputTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": GitSubmodulesConfigOutputTypeDef,
        "buildspec": str,
        "auth": SourceAuthOutputTypeDef,
        "reportBuildStatus": bool,
        "buildStatusConfig": BuildStatusConfigOutputTypeDef,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

class ProjectSourceOutputTypeDef(
    _RequiredProjectSourceOutputTypeDef, _OptionalProjectSourceOutputTypeDef
):
    pass

_RequiredProjectSourceTypeDef = TypedDict(
    "_RequiredProjectSourceTypeDef",
    {
        "type": SourceTypeType,
    },
)
_OptionalProjectSourceTypeDef = TypedDict(
    "_OptionalProjectSourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": GitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": SourceAuthTypeDef,
        "reportBuildStatus": bool,
        "buildStatusConfig": BuildStatusConfigTypeDef,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

class ProjectSourceTypeDef(_RequiredProjectSourceTypeDef, _OptionalProjectSourceTypeDef):
    pass

ReportExportConfigOutputTypeDef = TypedDict(
    "ReportExportConfigOutputTypeDef",
    {
        "exportConfigType": ReportExportConfigTypeType,
        "s3Destination": S3ReportExportConfigOutputTypeDef,
    },
    total=False,
)

ReportExportConfigTypeDef = TypedDict(
    "ReportExportConfigTypeDef",
    {
        "exportConfigType": ReportExportConfigTypeType,
        "s3Destination": S3ReportExportConfigTypeDef,
    },
    total=False,
)

WebhookTypeDef = TypedDict(
    "WebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[WebhookFilterOutputTypeDef]],
        "buildType": WebhookBuildTypeType,
        "lastModifiedSecret": datetime,
    },
    total=False,
)

BuildGroupTypeDef = TypedDict(
    "BuildGroupTypeDef",
    {
        "identifier": str,
        "dependsOn": List[str],
        "ignoreFailure": bool,
        "currentBuildSummary": BuildSummaryTypeDef,
        "priorBuildSummaryList": List[BuildSummaryTypeDef],
    },
    total=False,
)

EnvironmentPlatformTypeDef = TypedDict(
    "EnvironmentPlatformTypeDef",
    {
        "platform": PlatformTypeType,
        "languages": List[EnvironmentLanguageTypeDef],
    },
    total=False,
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": StatusTypeType,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[BuildPhaseTypeDef],
        "source": ProjectSourceOutputTypeDef,
        "secondarySources": List[ProjectSourceOutputTypeDef],
        "secondarySourceVersions": List[ProjectSourceVersionOutputTypeDef],
        "artifacts": BuildArtifactsTypeDef,
        "secondaryArtifacts": List[BuildArtifactsTypeDef],
        "cache": ProjectCacheOutputTypeDef,
        "environment": ProjectEnvironmentOutputTypeDef,
        "serviceRole": str,
        "logs": LogsLocationTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": VpcConfigOutputTypeDef,
        "networkInterface": NetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[ExportedEnvironmentVariableTypeDef],
        "reportArns": List[str],
        "fileSystemLocations": List[ProjectFileSystemLocationOutputTypeDef],
        "debugSession": DebugSessionTypeDef,
        "buildBatchArn": str,
    },
    total=False,
)

_RequiredCreateProjectInputRequestTypeDef = TypedDict(
    "_RequiredCreateProjectInputRequestTypeDef",
    {
        "name": str,
        "source": ProjectSourceTypeDef,
        "artifacts": ProjectArtifactsTypeDef,
        "environment": ProjectEnvironmentTypeDef,
        "serviceRole": str,
    },
)
_OptionalCreateProjectInputRequestTypeDef = TypedDict(
    "_OptionalCreateProjectInputRequestTypeDef",
    {
        "description": str,
        "secondarySources": Sequence[ProjectSourceTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": Sequence[ProjectSourceVersionTypeDef],
        "secondaryArtifacts": Sequence[ProjectArtifactsTypeDef],
        "cache": ProjectCacheTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": Sequence[TagTypeDef],
        "vpcConfig": VpcConfigTypeDef,
        "badgeEnabled": bool,
        "logsConfig": LogsConfigTypeDef,
        "fileSystemLocations": Sequence[ProjectFileSystemLocationTypeDef],
        "buildBatchConfig": ProjectBuildBatchConfigTypeDef,
        "concurrentBuildLimit": int,
    },
    total=False,
)

class CreateProjectInputRequestTypeDef(
    _RequiredCreateProjectInputRequestTypeDef, _OptionalCreateProjectInputRequestTypeDef
):
    pass

_RequiredStartBuildBatchInputRequestTypeDef = TypedDict(
    "_RequiredStartBuildBatchInputRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalStartBuildBatchInputRequestTypeDef = TypedDict(
    "_OptionalStartBuildBatchInputRequestTypeDef",
    {
        "secondarySourcesOverride": Sequence[ProjectSourceTypeDef],
        "secondarySourcesVersionOverride": Sequence[ProjectSourceVersionTypeDef],
        "sourceVersion": str,
        "artifactsOverride": ProjectArtifactsTypeDef,
        "secondaryArtifactsOverride": Sequence[ProjectArtifactsTypeDef],
        "environmentVariablesOverride": Sequence[EnvironmentVariableTypeDef],
        "sourceTypeOverride": SourceTypeType,
        "sourceLocationOverride": str,
        "sourceAuthOverride": SourceAuthTypeDef,
        "gitCloneDepthOverride": int,
        "gitSubmodulesConfigOverride": GitSubmodulesConfigTypeDef,
        "buildspecOverride": str,
        "insecureSslOverride": bool,
        "reportBuildBatchStatusOverride": bool,
        "environmentTypeOverride": EnvironmentTypeType,
        "imageOverride": str,
        "computeTypeOverride": ComputeTypeType,
        "certificateOverride": str,
        "cacheOverride": ProjectCacheTypeDef,
        "serviceRoleOverride": str,
        "privilegedModeOverride": bool,
        "buildTimeoutInMinutesOverride": int,
        "queuedTimeoutInMinutesOverride": int,
        "encryptionKeyOverride": str,
        "idempotencyToken": str,
        "logsConfigOverride": LogsConfigTypeDef,
        "registryCredentialOverride": RegistryCredentialTypeDef,
        "imagePullCredentialsTypeOverride": ImagePullCredentialsTypeType,
        "buildBatchConfigOverride": ProjectBuildBatchConfigTypeDef,
        "debugSessionEnabled": bool,
    },
    total=False,
)

class StartBuildBatchInputRequestTypeDef(
    _RequiredStartBuildBatchInputRequestTypeDef, _OptionalStartBuildBatchInputRequestTypeDef
):
    pass

_RequiredStartBuildInputRequestTypeDef = TypedDict(
    "_RequiredStartBuildInputRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalStartBuildInputRequestTypeDef = TypedDict(
    "_OptionalStartBuildInputRequestTypeDef",
    {
        "secondarySourcesOverride": Sequence[ProjectSourceTypeDef],
        "secondarySourcesVersionOverride": Sequence[ProjectSourceVersionTypeDef],
        "sourceVersion": str,
        "artifactsOverride": ProjectArtifactsTypeDef,
        "secondaryArtifactsOverride": Sequence[ProjectArtifactsTypeDef],
        "environmentVariablesOverride": Sequence[EnvironmentVariableTypeDef],
        "sourceTypeOverride": SourceTypeType,
        "sourceLocationOverride": str,
        "sourceAuthOverride": SourceAuthTypeDef,
        "gitCloneDepthOverride": int,
        "gitSubmodulesConfigOverride": GitSubmodulesConfigTypeDef,
        "buildspecOverride": str,
        "insecureSslOverride": bool,
        "reportBuildStatusOverride": bool,
        "buildStatusConfigOverride": BuildStatusConfigTypeDef,
        "environmentTypeOverride": EnvironmentTypeType,
        "imageOverride": str,
        "computeTypeOverride": ComputeTypeType,
        "certificateOverride": str,
        "cacheOverride": ProjectCacheTypeDef,
        "serviceRoleOverride": str,
        "privilegedModeOverride": bool,
        "timeoutInMinutesOverride": int,
        "queuedTimeoutInMinutesOverride": int,
        "encryptionKeyOverride": str,
        "idempotencyToken": str,
        "logsConfigOverride": LogsConfigTypeDef,
        "registryCredentialOverride": RegistryCredentialTypeDef,
        "imagePullCredentialsTypeOverride": ImagePullCredentialsTypeType,
        "debugSessionEnabled": bool,
    },
    total=False,
)

class StartBuildInputRequestTypeDef(
    _RequiredStartBuildInputRequestTypeDef, _OptionalStartBuildInputRequestTypeDef
):
    pass

_RequiredUpdateProjectInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateProjectInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectInputRequestTypeDef",
    {
        "description": str,
        "source": ProjectSourceTypeDef,
        "secondarySources": Sequence[ProjectSourceTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": Sequence[ProjectSourceVersionTypeDef],
        "artifacts": ProjectArtifactsTypeDef,
        "secondaryArtifacts": Sequence[ProjectArtifactsTypeDef],
        "cache": ProjectCacheTypeDef,
        "environment": ProjectEnvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": Sequence[TagTypeDef],
        "vpcConfig": VpcConfigTypeDef,
        "badgeEnabled": bool,
        "logsConfig": LogsConfigTypeDef,
        "fileSystemLocations": Sequence[ProjectFileSystemLocationTypeDef],
        "buildBatchConfig": ProjectBuildBatchConfigTypeDef,
        "concurrentBuildLimit": int,
    },
    total=False,
)

class UpdateProjectInputRequestTypeDef(
    _RequiredUpdateProjectInputRequestTypeDef, _OptionalUpdateProjectInputRequestTypeDef
):
    pass

ReportGroupTypeDef = TypedDict(
    "ReportGroupTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ReportTypeType,
        "exportConfig": ReportExportConfigOutputTypeDef,
        "created": datetime,
        "lastModified": datetime,
        "tags": List[TagOutputTypeDef],
        "status": ReportGroupStatusTypeType,
    },
    total=False,
)

ReportTypeDef = TypedDict(
    "ReportTypeDef",
    {
        "arn": str,
        "type": ReportTypeType,
        "name": str,
        "reportGroupArn": str,
        "executionId": str,
        "status": ReportStatusTypeType,
        "created": datetime,
        "expired": datetime,
        "exportConfig": ReportExportConfigOutputTypeDef,
        "truncated": bool,
        "testSummary": TestReportSummaryTypeDef,
        "codeCoverageSummary": CodeCoverageReportSummaryTypeDef,
    },
    total=False,
)

_RequiredCreateReportGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateReportGroupInputRequestTypeDef",
    {
        "name": str,
        "type": ReportTypeType,
        "exportConfig": ReportExportConfigTypeDef,
    },
)
_OptionalCreateReportGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateReportGroupInputRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateReportGroupInputRequestTypeDef(
    _RequiredCreateReportGroupInputRequestTypeDef, _OptionalCreateReportGroupInputRequestTypeDef
):
    pass

_RequiredUpdateReportGroupInputRequestTypeDef = TypedDict(
    "_RequiredUpdateReportGroupInputRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateReportGroupInputRequestTypeDef = TypedDict(
    "_OptionalUpdateReportGroupInputRequestTypeDef",
    {
        "exportConfig": ReportExportConfigTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class UpdateReportGroupInputRequestTypeDef(
    _RequiredUpdateReportGroupInputRequestTypeDef, _OptionalUpdateReportGroupInputRequestTypeDef
):
    pass

CreateWebhookOutputTypeDef = TypedDict(
    "CreateWebhookOutputTypeDef",
    {
        "webhook": WebhookTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ProjectSourceOutputTypeDef,
        "secondarySources": List[ProjectSourceOutputTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": List[ProjectSourceVersionOutputTypeDef],
        "artifacts": ProjectArtifactsOutputTypeDef,
        "secondaryArtifacts": List[ProjectArtifactsOutputTypeDef],
        "cache": ProjectCacheOutputTypeDef,
        "environment": ProjectEnvironmentOutputTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[TagOutputTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": WebhookTypeDef,
        "vpcConfig": VpcConfigOutputTypeDef,
        "badge": ProjectBadgeTypeDef,
        "logsConfig": LogsConfigOutputTypeDef,
        "fileSystemLocations": List[ProjectFileSystemLocationOutputTypeDef],
        "buildBatchConfig": ProjectBuildBatchConfigOutputTypeDef,
        "concurrentBuildLimit": int,
        "projectVisibility": ProjectVisibilityTypeType,
        "publicProjectAlias": str,
        "resourceAccessRole": str,
    },
    total=False,
)

UpdateWebhookOutputTypeDef = TypedDict(
    "UpdateWebhookOutputTypeDef",
    {
        "webhook": WebhookTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BuildBatchTypeDef = TypedDict(
    "BuildBatchTypeDef",
    {
        "id": str,
        "arn": str,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildBatchStatus": StatusTypeType,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[BuildBatchPhaseTypeDef],
        "source": ProjectSourceOutputTypeDef,
        "secondarySources": List[ProjectSourceOutputTypeDef],
        "secondarySourceVersions": List[ProjectSourceVersionOutputTypeDef],
        "artifacts": BuildArtifactsTypeDef,
        "secondaryArtifacts": List[BuildArtifactsTypeDef],
        "cache": ProjectCacheOutputTypeDef,
        "environment": ProjectEnvironmentOutputTypeDef,
        "serviceRole": str,
        "logConfig": LogsConfigOutputTypeDef,
        "buildTimeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "complete": bool,
        "initiator": str,
        "vpcConfig": VpcConfigOutputTypeDef,
        "encryptionKey": str,
        "buildBatchNumber": int,
        "fileSystemLocations": List[ProjectFileSystemLocationOutputTypeDef],
        "buildBatchConfig": ProjectBuildBatchConfigOutputTypeDef,
        "buildGroups": List[BuildGroupTypeDef],
        "debugSessionEnabled": bool,
    },
    total=False,
)

ListCuratedEnvironmentImagesOutputTypeDef = TypedDict(
    "ListCuratedEnvironmentImagesOutputTypeDef",
    {
        "platforms": List[EnvironmentPlatformTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBuildsOutputTypeDef = TypedDict(
    "BatchGetBuildsOutputTypeDef",
    {
        "builds": List[BuildTypeDef],
        "buildsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetryBuildOutputTypeDef = TypedDict(
    "RetryBuildOutputTypeDef",
    {
        "build": BuildTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartBuildOutputTypeDef = TypedDict(
    "StartBuildOutputTypeDef",
    {
        "build": BuildTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBuildOutputTypeDef = TypedDict(
    "StopBuildOutputTypeDef",
    {
        "build": BuildTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetReportGroupsOutputTypeDef = TypedDict(
    "BatchGetReportGroupsOutputTypeDef",
    {
        "reportGroups": List[ReportGroupTypeDef],
        "reportGroupsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReportGroupOutputTypeDef = TypedDict(
    "CreateReportGroupOutputTypeDef",
    {
        "reportGroup": ReportGroupTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateReportGroupOutputTypeDef = TypedDict(
    "UpdateReportGroupOutputTypeDef",
    {
        "reportGroup": ReportGroupTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetReportsOutputTypeDef = TypedDict(
    "BatchGetReportsOutputTypeDef",
    {
        "reports": List[ReportTypeDef],
        "reportsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetProjectsOutputTypeDef = TypedDict(
    "BatchGetProjectsOutputTypeDef",
    {
        "projects": List[ProjectTypeDef],
        "projectsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBuildBatchesOutputTypeDef = TypedDict(
    "BatchGetBuildBatchesOutputTypeDef",
    {
        "buildBatches": List[BuildBatchTypeDef],
        "buildBatchesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetryBuildBatchOutputTypeDef = TypedDict(
    "RetryBuildBatchOutputTypeDef",
    {
        "buildBatch": BuildBatchTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartBuildBatchOutputTypeDef = TypedDict(
    "StartBuildBatchOutputTypeDef",
    {
        "buildBatch": BuildBatchTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBuildBatchOutputTypeDef = TypedDict(
    "StopBuildBatchOutputTypeDef",
    {
        "buildBatch": BuildBatchTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
