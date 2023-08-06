"""
Type annotations for migrationhubstrategy service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/type_defs/)

Usage::

    ```python
    from mypy_boto3_migrationhubstrategy.type_defs import AnalysisStatusUnionTypeDef

    data: AnalysisStatusUnionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AnalysisTypeType,
    AntipatternReportStatusType,
    ApplicationComponentCriteriaType,
    ApplicationModeType,
    AppTypeType,
    AppUnitErrorCategoryType,
    AssessmentStatusType,
    AuthTypeType,
    AwsManagedTargetDestinationType,
    BinaryAnalyzerNameType,
    CollectorHealthType,
    ConditionType,
    DatabaseManagementPreferenceType,
    DataSourceTypeType,
    GroupNameType,
    HeterogeneousTargetDatabaseEngineType,
    ImportFileTaskStatusType,
    InclusionStatusType,
    NoPreferenceTargetDestinationType,
    OSTypeType,
    OutputFormatType,
    RecommendationReportStatusType,
    ResourceSubTypeType,
    RuntimeAnalysisStatusType,
    RunTimeAnalyzerNameType,
    RunTimeAssessmentStatusType,
    SelfManageTargetDestinationType,
    ServerCriteriaType,
    ServerErrorCategoryType,
    ServerOsTypeType,
    SeverityType,
    SortOrderType,
    SourceCodeAnalyzerNameType,
    SrcCodeOrDbAnalysisStatusType,
    StrategyRecommendationType,
    StrategyType,
    TargetDatabaseEngineType,
    TargetDestinationType,
    TransformationToolNameType,
    VersionControlType,
    VersionControlTypeType,
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
    "AnalysisStatusUnionTypeDef",
    "AnalyzerNameUnionTypeDef",
    "S3ObjectTypeDef",
    "AntipatternSeveritySummaryTypeDef",
    "AppUnitErrorTypeDef",
    "DatabaseConfigDetailTypeDef",
    "SourceCodeRepositoryTypeDef",
    "ApplicationComponentStatusSummaryTypeDef",
    "ApplicationComponentSummaryTypeDef",
    "ServerStatusSummaryTypeDef",
    "ServerSummaryTypeDef",
    "StrategySummaryTypeDef",
    "AssessmentTargetOutputTypeDef",
    "AssessmentTargetTypeDef",
    "AssociatedApplicationTypeDef",
    "AwsManagedResourcesOutputTypeDef",
    "AwsManagedResourcesTypeDef",
    "BusinessGoalsOutputTypeDef",
    "BusinessGoalsTypeDef",
    "IPAddressBasedRemoteInfoTypeDef",
    "PipelineInfoTypeDef",
    "RemoteSourceCodeAnalysisServerInfoTypeDef",
    "VcenterBasedRemoteInfoTypeDef",
    "VersionControlInfoTypeDef",
    "DataCollectionDetailsTypeDef",
    "HeterogeneousOutputTypeDef",
    "HomogeneousOutputTypeDef",
    "NoDatabaseMigrationPreferenceOutputTypeDef",
    "HeterogeneousTypeDef",
    "HomogeneousTypeDef",
    "NoDatabaseMigrationPreferenceTypeDef",
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    "GetAssessmentRequestRequestTypeDef",
    "GetImportFileTaskRequestRequestTypeDef",
    "GetImportFileTaskResponseTypeDef",
    "GetLatestAssessmentIdResponseTypeDef",
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    "RecommendationReportDetailsTypeDef",
    "GetServerDetailsRequestGetServerDetailsPaginateTypeDef",
    "GetServerDetailsRequestRequestTypeDef",
    "GetServerStrategiesRequestRequestTypeDef",
    "GroupTypeDef",
    "ImportFileTaskInformationTypeDef",
    "ListCollectorsRequestListCollectorsPaginateTypeDef",
    "ListCollectorsRequestRequestTypeDef",
    "ListImportFileTaskRequestListImportFileTaskPaginateTypeDef",
    "ListImportFileTaskRequestRequestTypeDef",
    "NoManagementPreferenceOutputTypeDef",
    "SelfManageResourcesOutputTypeDef",
    "NoManagementPreferenceTypeDef",
    "SelfManageResourcesTypeDef",
    "NetworkInfoTypeDef",
    "OSInfoTypeDef",
    "PaginatorConfigTypeDef",
    "TransformationToolTypeDef",
    "ResponseMetadataTypeDef",
    "ServerErrorTypeDef",
    "SourceCodeTypeDef",
    "StartAssessmentResponseTypeDef",
    "StartImportFileTaskResponseTypeDef",
    "StartRecommendationReportGenerationResponseTypeDef",
    "StopAssessmentRequestRequestTypeDef",
    "StrategyOptionTypeDef",
    "AntipatternReportResultTypeDef",
    "AssessmentSummaryTypeDef",
    "StartAssessmentRequestRequestTypeDef",
    "PrioritizeBusinessGoalsOutputTypeDef",
    "PrioritizeBusinessGoalsTypeDef",
    "ConfigurationSummaryTypeDef",
    "GetAssessmentResponseTypeDef",
    "DatabaseMigrationPreferenceOutputTypeDef",
    "DatabaseMigrationPreferenceTypeDef",
    "GetRecommendationReportDetailsResponseTypeDef",
    "ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef",
    "ListApplicationComponentsRequestRequestTypeDef",
    "ListServersRequestListServersPaginateTypeDef",
    "ListServersRequestRequestTypeDef",
    "StartImportFileTaskRequestRequestTypeDef",
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    "ListImportFileTaskResponseTypeDef",
    "ManagementPreferenceOutputTypeDef",
    "ManagementPreferenceTypeDef",
    "SystemInfoTypeDef",
    "RecommendationSetTypeDef",
    "UpdateApplicationComponentConfigRequestRequestTypeDef",
    "UpdateServerConfigRequestRequestTypeDef",
    "ResultTypeDef",
    "GetPortfolioSummaryResponseTypeDef",
    "CollectorTypeDef",
    "DatabasePreferencesOutputTypeDef",
    "DatabasePreferencesTypeDef",
    "ApplicationPreferencesOutputTypeDef",
    "ApplicationPreferencesTypeDef",
    "ApplicationComponentStrategyTypeDef",
    "ServerDetailTypeDef",
    "ServerStrategyTypeDef",
    "ApplicationComponentDetailTypeDef",
    "ListCollectorsResponseTypeDef",
    "GetPortfolioPreferencesResponseTypeDef",
    "PutPortfolioPreferencesRequestRequestTypeDef",
    "GetApplicationComponentStrategiesResponseTypeDef",
    "GetServerDetailsResponseTypeDef",
    "ListServersResponseTypeDef",
    "GetServerStrategiesResponseTypeDef",
    "GetApplicationComponentDetailsResponseTypeDef",
    "ListApplicationComponentsResponseTypeDef",
)

AnalysisStatusUnionTypeDef = TypedDict(
    "AnalysisStatusUnionTypeDef",
    {
        "runtimeAnalysisStatus": RuntimeAnalysisStatusType,
        "srcCodeOrDbAnalysisStatus": SrcCodeOrDbAnalysisStatusType,
    },
    total=False,
)

AnalyzerNameUnionTypeDef = TypedDict(
    "AnalyzerNameUnionTypeDef",
    {
        "binaryAnalyzerName": BinaryAnalyzerNameType,
        "runTimeAnalyzerName": RunTimeAnalyzerNameType,
        "sourceCodeAnalyzerName": SourceCodeAnalyzerNameType,
    },
    total=False,
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "s3Bucket": str,
        "s3key": str,
    },
    total=False,
)

AntipatternSeveritySummaryTypeDef = TypedDict(
    "AntipatternSeveritySummaryTypeDef",
    {
        "count": int,
        "severity": SeverityType,
    },
    total=False,
)

AppUnitErrorTypeDef = TypedDict(
    "AppUnitErrorTypeDef",
    {
        "appUnitErrorCategory": AppUnitErrorCategoryType,
    },
    total=False,
)

DatabaseConfigDetailTypeDef = TypedDict(
    "DatabaseConfigDetailTypeDef",
    {
        "secretName": str,
    },
    total=False,
)

SourceCodeRepositoryTypeDef = TypedDict(
    "SourceCodeRepositoryTypeDef",
    {
        "branch": str,
        "projectName": str,
        "repository": str,
        "versionControlType": str,
    },
    total=False,
)

ApplicationComponentStatusSummaryTypeDef = TypedDict(
    "ApplicationComponentStatusSummaryTypeDef",
    {
        "count": int,
        "srcCodeOrDbAnalysisStatus": SrcCodeOrDbAnalysisStatusType,
    },
    total=False,
)

ApplicationComponentSummaryTypeDef = TypedDict(
    "ApplicationComponentSummaryTypeDef",
    {
        "appType": AppTypeType,
        "count": int,
    },
    total=False,
)

ServerStatusSummaryTypeDef = TypedDict(
    "ServerStatusSummaryTypeDef",
    {
        "count": int,
        "runTimeAssessmentStatus": RunTimeAssessmentStatusType,
    },
    total=False,
)

ServerSummaryTypeDef = TypedDict(
    "ServerSummaryTypeDef",
    {
        "ServerOsType": ServerOsTypeType,
        "count": int,
    },
    total=False,
)

StrategySummaryTypeDef = TypedDict(
    "StrategySummaryTypeDef",
    {
        "count": int,
        "strategy": StrategyType,
    },
    total=False,
)

AssessmentTargetOutputTypeDef = TypedDict(
    "AssessmentTargetOutputTypeDef",
    {
        "condition": ConditionType,
        "name": str,
        "values": List[str],
    },
)

AssessmentTargetTypeDef = TypedDict(
    "AssessmentTargetTypeDef",
    {
        "condition": ConditionType,
        "name": str,
        "values": Sequence[str],
    },
)

AssociatedApplicationTypeDef = TypedDict(
    "AssociatedApplicationTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

AwsManagedResourcesOutputTypeDef = TypedDict(
    "AwsManagedResourcesOutputTypeDef",
    {
        "targetDestination": List[AwsManagedTargetDestinationType],
    },
)

AwsManagedResourcesTypeDef = TypedDict(
    "AwsManagedResourcesTypeDef",
    {
        "targetDestination": Sequence[AwsManagedTargetDestinationType],
    },
)

BusinessGoalsOutputTypeDef = TypedDict(
    "BusinessGoalsOutputTypeDef",
    {
        "licenseCostReduction": int,
        "modernizeInfrastructureWithCloudNativeTechnologies": int,
        "reduceOperationalOverheadWithManagedServices": int,
        "speedOfMigration": int,
    },
    total=False,
)

BusinessGoalsTypeDef = TypedDict(
    "BusinessGoalsTypeDef",
    {
        "licenseCostReduction": int,
        "modernizeInfrastructureWithCloudNativeTechnologies": int,
        "reduceOperationalOverheadWithManagedServices": int,
        "speedOfMigration": int,
    },
    total=False,
)

IPAddressBasedRemoteInfoTypeDef = TypedDict(
    "IPAddressBasedRemoteInfoTypeDef",
    {
        "authType": AuthTypeType,
        "ipAddressConfigurationTimeStamp": str,
        "osType": OSTypeType,
    },
    total=False,
)

PipelineInfoTypeDef = TypedDict(
    "PipelineInfoTypeDef",
    {
        "pipelineConfigurationTimeStamp": str,
        "pipelineType": Literal["AZURE_DEVOPS"],
    },
    total=False,
)

RemoteSourceCodeAnalysisServerInfoTypeDef = TypedDict(
    "RemoteSourceCodeAnalysisServerInfoTypeDef",
    {
        "remoteSourceCodeAnalysisServerConfigurationTimestamp": str,
    },
    total=False,
)

VcenterBasedRemoteInfoTypeDef = TypedDict(
    "VcenterBasedRemoteInfoTypeDef",
    {
        "osType": OSTypeType,
        "vcenterConfigurationTimeStamp": str,
    },
    total=False,
)

VersionControlInfoTypeDef = TypedDict(
    "VersionControlInfoTypeDef",
    {
        "versionControlConfigurationTimeStamp": str,
        "versionControlType": VersionControlTypeType,
    },
    total=False,
)

DataCollectionDetailsTypeDef = TypedDict(
    "DataCollectionDetailsTypeDef",
    {
        "completionTime": datetime,
        "failed": int,
        "inProgress": int,
        "servers": int,
        "startTime": datetime,
        "status": AssessmentStatusType,
        "statusMessage": str,
        "success": int,
    },
    total=False,
)

HeterogeneousOutputTypeDef = TypedDict(
    "HeterogeneousOutputTypeDef",
    {
        "targetDatabaseEngine": List[HeterogeneousTargetDatabaseEngineType],
    },
)

HomogeneousOutputTypeDef = TypedDict(
    "HomogeneousOutputTypeDef",
    {
        "targetDatabaseEngine": List[Literal["None specified"]],
    },
    total=False,
)

NoDatabaseMigrationPreferenceOutputTypeDef = TypedDict(
    "NoDatabaseMigrationPreferenceOutputTypeDef",
    {
        "targetDatabaseEngine": List[TargetDatabaseEngineType],
    },
)

HeterogeneousTypeDef = TypedDict(
    "HeterogeneousTypeDef",
    {
        "targetDatabaseEngine": Sequence[HeterogeneousTargetDatabaseEngineType],
    },
)

HomogeneousTypeDef = TypedDict(
    "HomogeneousTypeDef",
    {
        "targetDatabaseEngine": Sequence[Literal["None specified"]],
    },
    total=False,
)

NoDatabaseMigrationPreferenceTypeDef = TypedDict(
    "NoDatabaseMigrationPreferenceTypeDef",
    {
        "targetDatabaseEngine": Sequence[TargetDatabaseEngineType],
    },
)

GetApplicationComponentDetailsRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)

GetApplicationComponentStrategiesRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)

GetAssessmentRequestRequestTypeDef = TypedDict(
    "GetAssessmentRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetImportFileTaskRequestRequestTypeDef = TypedDict(
    "GetImportFileTaskRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetImportFileTaskResponseTypeDef = TypedDict(
    "GetImportFileTaskResponseTypeDef",
    {
        "completionTime": datetime,
        "id": str,
        "importName": str,
        "inputS3Bucket": str,
        "inputS3Key": str,
        "numberOfRecordsFailed": int,
        "numberOfRecordsSuccess": int,
        "startTime": datetime,
        "status": ImportFileTaskStatusType,
        "statusReportS3Bucket": str,
        "statusReportS3Key": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLatestAssessmentIdResponseTypeDef = TypedDict(
    "GetLatestAssessmentIdResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationReportDetailsRequestRequestTypeDef = TypedDict(
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    {
        "id": str,
    },
)

RecommendationReportDetailsTypeDef = TypedDict(
    "RecommendationReportDetailsTypeDef",
    {
        "completionTime": datetime,
        "s3Bucket": str,
        "s3Keys": List[str],
        "startTime": datetime,
        "status": RecommendationReportStatusType,
        "statusMessage": str,
    },
    total=False,
)

_RequiredGetServerDetailsRequestGetServerDetailsPaginateTypeDef = TypedDict(
    "_RequiredGetServerDetailsRequestGetServerDetailsPaginateTypeDef",
    {
        "serverId": str,
    },
)
_OptionalGetServerDetailsRequestGetServerDetailsPaginateTypeDef = TypedDict(
    "_OptionalGetServerDetailsRequestGetServerDetailsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class GetServerDetailsRequestGetServerDetailsPaginateTypeDef(
    _RequiredGetServerDetailsRequestGetServerDetailsPaginateTypeDef,
    _OptionalGetServerDetailsRequestGetServerDetailsPaginateTypeDef,
):
    pass

_RequiredGetServerDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetServerDetailsRequestRequestTypeDef",
    {
        "serverId": str,
    },
)
_OptionalGetServerDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetServerDetailsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class GetServerDetailsRequestRequestTypeDef(
    _RequiredGetServerDetailsRequestRequestTypeDef, _OptionalGetServerDetailsRequestRequestTypeDef
):
    pass

GetServerStrategiesRequestRequestTypeDef = TypedDict(
    "GetServerStrategiesRequestRequestTypeDef",
    {
        "serverId": str,
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "name": GroupNameType,
        "value": str,
    },
    total=False,
)

ImportFileTaskInformationTypeDef = TypedDict(
    "ImportFileTaskInformationTypeDef",
    {
        "completionTime": datetime,
        "id": str,
        "importName": str,
        "inputS3Bucket": str,
        "inputS3Key": str,
        "numberOfRecordsFailed": int,
        "numberOfRecordsSuccess": int,
        "startTime": datetime,
        "status": ImportFileTaskStatusType,
        "statusReportS3Bucket": str,
        "statusReportS3Key": str,
    },
    total=False,
)

ListCollectorsRequestListCollectorsPaginateTypeDef = TypedDict(
    "ListCollectorsRequestListCollectorsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListCollectorsRequestRequestTypeDef = TypedDict(
    "ListCollectorsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImportFileTaskRequestListImportFileTaskPaginateTypeDef = TypedDict(
    "ListImportFileTaskRequestListImportFileTaskPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListImportFileTaskRequestRequestTypeDef = TypedDict(
    "ListImportFileTaskRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

NoManagementPreferenceOutputTypeDef = TypedDict(
    "NoManagementPreferenceOutputTypeDef",
    {
        "targetDestination": List[NoPreferenceTargetDestinationType],
    },
)

SelfManageResourcesOutputTypeDef = TypedDict(
    "SelfManageResourcesOutputTypeDef",
    {
        "targetDestination": List[SelfManageTargetDestinationType],
    },
)

NoManagementPreferenceTypeDef = TypedDict(
    "NoManagementPreferenceTypeDef",
    {
        "targetDestination": Sequence[NoPreferenceTargetDestinationType],
    },
)

SelfManageResourcesTypeDef = TypedDict(
    "SelfManageResourcesTypeDef",
    {
        "targetDestination": Sequence[SelfManageTargetDestinationType],
    },
)

NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "interfaceName": str,
        "ipAddress": str,
        "macAddress": str,
        "netMask": str,
    },
)

OSInfoTypeDef = TypedDict(
    "OSInfoTypeDef",
    {
        "type": OSTypeType,
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

TransformationToolTypeDef = TypedDict(
    "TransformationToolTypeDef",
    {
        "description": str,
        "name": TransformationToolNameType,
        "tranformationToolInstallationLink": str,
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

ServerErrorTypeDef = TypedDict(
    "ServerErrorTypeDef",
    {
        "serverErrorCategory": ServerErrorCategoryType,
    },
    total=False,
)

SourceCodeTypeDef = TypedDict(
    "SourceCodeTypeDef",
    {
        "location": str,
        "projectName": str,
        "sourceVersion": str,
        "versionControl": VersionControlType,
    },
    total=False,
)

StartAssessmentResponseTypeDef = TypedDict(
    "StartAssessmentResponseTypeDef",
    {
        "assessmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportFileTaskResponseTypeDef = TypedDict(
    "StartImportFileTaskResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRecommendationReportGenerationResponseTypeDef = TypedDict(
    "StartRecommendationReportGenerationResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAssessmentRequestRequestTypeDef = TypedDict(
    "StopAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)

StrategyOptionTypeDef = TypedDict(
    "StrategyOptionTypeDef",
    {
        "isPreferred": bool,
        "strategy": StrategyType,
        "targetDestination": TargetDestinationType,
        "toolName": TransformationToolNameType,
    },
    total=False,
)

AntipatternReportResultTypeDef = TypedDict(
    "AntipatternReportResultTypeDef",
    {
        "analyzerName": AnalyzerNameUnionTypeDef,
        "antiPatternReportS3Object": S3ObjectTypeDef,
        "antipatternReportStatus": AntipatternReportStatusType,
        "antipatternReportStatusMessage": str,
    },
    total=False,
)

AssessmentSummaryTypeDef = TypedDict(
    "AssessmentSummaryTypeDef",
    {
        "antipatternReportS3Object": S3ObjectTypeDef,
        "antipatternReportStatus": AntipatternReportStatusType,
        "antipatternReportStatusMessage": str,
        "lastAnalyzedTimestamp": datetime,
        "listAntipatternSeveritySummary": List[AntipatternSeveritySummaryTypeDef],
        "listApplicationComponentStatusSummary": List[ApplicationComponentStatusSummaryTypeDef],
        "listApplicationComponentStrategySummary": List[StrategySummaryTypeDef],
        "listApplicationComponentSummary": List[ApplicationComponentSummaryTypeDef],
        "listServerStatusSummary": List[ServerStatusSummaryTypeDef],
        "listServerStrategySummary": List[StrategySummaryTypeDef],
        "listServerSummary": List[ServerSummaryTypeDef],
    },
    total=False,
)

StartAssessmentRequestRequestTypeDef = TypedDict(
    "StartAssessmentRequestRequestTypeDef",
    {
        "assessmentTargets": Sequence[AssessmentTargetTypeDef],
        "s3bucketForAnalysisData": str,
        "s3bucketForReportData": str,
    },
    total=False,
)

PrioritizeBusinessGoalsOutputTypeDef = TypedDict(
    "PrioritizeBusinessGoalsOutputTypeDef",
    {
        "businessGoals": BusinessGoalsOutputTypeDef,
    },
    total=False,
)

PrioritizeBusinessGoalsTypeDef = TypedDict(
    "PrioritizeBusinessGoalsTypeDef",
    {
        "businessGoals": BusinessGoalsTypeDef,
    },
    total=False,
)

ConfigurationSummaryTypeDef = TypedDict(
    "ConfigurationSummaryTypeDef",
    {
        "ipAddressBasedRemoteInfoList": List[IPAddressBasedRemoteInfoTypeDef],
        "pipelineInfoList": List[PipelineInfoTypeDef],
        "remoteSourceCodeAnalysisServerInfo": RemoteSourceCodeAnalysisServerInfoTypeDef,
        "vcenterBasedRemoteInfoList": List[VcenterBasedRemoteInfoTypeDef],
        "versionControlInfoList": List[VersionControlInfoTypeDef],
    },
    total=False,
)

GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "assessmentTargets": List[AssessmentTargetOutputTypeDef],
        "dataCollectionDetails": DataCollectionDetailsTypeDef,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatabaseMigrationPreferenceOutputTypeDef = TypedDict(
    "DatabaseMigrationPreferenceOutputTypeDef",
    {
        "heterogeneous": HeterogeneousOutputTypeDef,
        "homogeneous": HomogeneousOutputTypeDef,
        "noPreference": NoDatabaseMigrationPreferenceOutputTypeDef,
    },
    total=False,
)

DatabaseMigrationPreferenceTypeDef = TypedDict(
    "DatabaseMigrationPreferenceTypeDef",
    {
        "heterogeneous": HeterogeneousTypeDef,
        "homogeneous": HomogeneousTypeDef,
        "noPreference": NoDatabaseMigrationPreferenceTypeDef,
    },
    total=False,
)

GetRecommendationReportDetailsResponseTypeDef = TypedDict(
    "GetRecommendationReportDetailsResponseTypeDef",
    {
        "id": str,
        "recommendationReportDetails": RecommendationReportDetailsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef = TypedDict(
    "ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef",
    {
        "applicationComponentCriteria": ApplicationComponentCriteriaType,
        "filterValue": str,
        "groupIdFilter": Sequence[GroupTypeDef],
        "sort": SortOrderType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListApplicationComponentsRequestRequestTypeDef = TypedDict(
    "ListApplicationComponentsRequestRequestTypeDef",
    {
        "applicationComponentCriteria": ApplicationComponentCriteriaType,
        "filterValue": str,
        "groupIdFilter": Sequence[GroupTypeDef],
        "maxResults": int,
        "nextToken": str,
        "sort": SortOrderType,
    },
    total=False,
)

ListServersRequestListServersPaginateTypeDef = TypedDict(
    "ListServersRequestListServersPaginateTypeDef",
    {
        "filterValue": str,
        "groupIdFilter": Sequence[GroupTypeDef],
        "serverCriteria": ServerCriteriaType,
        "sort": SortOrderType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "filterValue": str,
        "groupIdFilter": Sequence[GroupTypeDef],
        "maxResults": int,
        "nextToken": str,
        "serverCriteria": ServerCriteriaType,
        "sort": SortOrderType,
    },
    total=False,
)

_RequiredStartImportFileTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportFileTaskRequestRequestTypeDef",
    {
        "S3Bucket": str,
        "name": str,
        "s3key": str,
    },
)
_OptionalStartImportFileTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportFileTaskRequestRequestTypeDef",
    {
        "dataSourceType": DataSourceTypeType,
        "groupId": Sequence[GroupTypeDef],
        "s3bucketForReportData": str,
    },
    total=False,
)

class StartImportFileTaskRequestRequestTypeDef(
    _RequiredStartImportFileTaskRequestRequestTypeDef,
    _OptionalStartImportFileTaskRequestRequestTypeDef,
):
    pass

StartRecommendationReportGenerationRequestRequestTypeDef = TypedDict(
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    {
        "groupIdFilter": Sequence[GroupTypeDef],
        "outputFormat": OutputFormatType,
    },
    total=False,
)

ListImportFileTaskResponseTypeDef = TypedDict(
    "ListImportFileTaskResponseTypeDef",
    {
        "nextToken": str,
        "taskInfos": List[ImportFileTaskInformationTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagementPreferenceOutputTypeDef = TypedDict(
    "ManagementPreferenceOutputTypeDef",
    {
        "awsManagedResources": AwsManagedResourcesOutputTypeDef,
        "noPreference": NoManagementPreferenceOutputTypeDef,
        "selfManageResources": SelfManageResourcesOutputTypeDef,
    },
    total=False,
)

ManagementPreferenceTypeDef = TypedDict(
    "ManagementPreferenceTypeDef",
    {
        "awsManagedResources": AwsManagedResourcesTypeDef,
        "noPreference": NoManagementPreferenceTypeDef,
        "selfManageResources": SelfManageResourcesTypeDef,
    },
    total=False,
)

SystemInfoTypeDef = TypedDict(
    "SystemInfoTypeDef",
    {
        "cpuArchitecture": str,
        "fileSystemType": str,
        "networkInfoList": List[NetworkInfoTypeDef],
        "osInfo": OSInfoTypeDef,
    },
    total=False,
)

RecommendationSetTypeDef = TypedDict(
    "RecommendationSetTypeDef",
    {
        "strategy": StrategyType,
        "targetDestination": TargetDestinationType,
        "transformationTool": TransformationToolTypeDef,
    },
    total=False,
)

_RequiredUpdateApplicationComponentConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationComponentConfigRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)
_OptionalUpdateApplicationComponentConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationComponentConfigRequestRequestTypeDef",
    {
        "appType": AppTypeType,
        "configureOnly": bool,
        "inclusionStatus": InclusionStatusType,
        "secretsManagerKey": str,
        "sourceCodeList": Sequence[SourceCodeTypeDef],
        "strategyOption": StrategyOptionTypeDef,
    },
    total=False,
)

class UpdateApplicationComponentConfigRequestRequestTypeDef(
    _RequiredUpdateApplicationComponentConfigRequestRequestTypeDef,
    _OptionalUpdateApplicationComponentConfigRequestRequestTypeDef,
):
    pass

_RequiredUpdateServerConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServerConfigRequestRequestTypeDef",
    {
        "serverId": str,
    },
)
_OptionalUpdateServerConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServerConfigRequestRequestTypeDef",
    {
        "strategyOption": StrategyOptionTypeDef,
    },
    total=False,
)

class UpdateServerConfigRequestRequestTypeDef(
    _RequiredUpdateServerConfigRequestRequestTypeDef,
    _OptionalUpdateServerConfigRequestRequestTypeDef,
):
    pass

ResultTypeDef = TypedDict(
    "ResultTypeDef",
    {
        "analysisStatus": AnalysisStatusUnionTypeDef,
        "analysisType": AnalysisTypeType,
        "antipatternReportResultList": List[AntipatternReportResultTypeDef],
        "statusMessage": str,
    },
    total=False,
)

GetPortfolioSummaryResponseTypeDef = TypedDict(
    "GetPortfolioSummaryResponseTypeDef",
    {
        "assessmentSummary": AssessmentSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CollectorTypeDef = TypedDict(
    "CollectorTypeDef",
    {
        "collectorHealth": CollectorHealthType,
        "collectorId": str,
        "collectorVersion": str,
        "configurationSummary": ConfigurationSummaryTypeDef,
        "hostName": str,
        "ipAddress": str,
        "lastActivityTimeStamp": str,
        "registeredTimeStamp": str,
    },
    total=False,
)

DatabasePreferencesOutputTypeDef = TypedDict(
    "DatabasePreferencesOutputTypeDef",
    {
        "databaseManagementPreference": DatabaseManagementPreferenceType,
        "databaseMigrationPreference": DatabaseMigrationPreferenceOutputTypeDef,
    },
    total=False,
)

DatabasePreferencesTypeDef = TypedDict(
    "DatabasePreferencesTypeDef",
    {
        "databaseManagementPreference": DatabaseManagementPreferenceType,
        "databaseMigrationPreference": DatabaseMigrationPreferenceTypeDef,
    },
    total=False,
)

ApplicationPreferencesOutputTypeDef = TypedDict(
    "ApplicationPreferencesOutputTypeDef",
    {
        "managementPreference": ManagementPreferenceOutputTypeDef,
    },
    total=False,
)

ApplicationPreferencesTypeDef = TypedDict(
    "ApplicationPreferencesTypeDef",
    {
        "managementPreference": ManagementPreferenceTypeDef,
    },
    total=False,
)

ApplicationComponentStrategyTypeDef = TypedDict(
    "ApplicationComponentStrategyTypeDef",
    {
        "isPreferred": bool,
        "recommendation": RecommendationSetTypeDef,
        "status": StrategyRecommendationType,
    },
    total=False,
)

ServerDetailTypeDef = TypedDict(
    "ServerDetailTypeDef",
    {
        "antipatternReportS3Object": S3ObjectTypeDef,
        "antipatternReportStatus": AntipatternReportStatusType,
        "antipatternReportStatusMessage": str,
        "applicationComponentStrategySummary": List[StrategySummaryTypeDef],
        "dataCollectionStatus": RunTimeAssessmentStatusType,
        "id": str,
        "lastAnalyzedTimestamp": datetime,
        "listAntipatternSeveritySummary": List[AntipatternSeveritySummaryTypeDef],
        "name": str,
        "recommendationSet": RecommendationSetTypeDef,
        "serverError": ServerErrorTypeDef,
        "serverType": str,
        "statusMessage": str,
        "systemInfo": SystemInfoTypeDef,
    },
    total=False,
)

ServerStrategyTypeDef = TypedDict(
    "ServerStrategyTypeDef",
    {
        "isPreferred": bool,
        "numberOfApplicationComponents": int,
        "recommendation": RecommendationSetTypeDef,
        "status": StrategyRecommendationType,
    },
    total=False,
)

ApplicationComponentDetailTypeDef = TypedDict(
    "ApplicationComponentDetailTypeDef",
    {
        "analysisStatus": SrcCodeOrDbAnalysisStatusType,
        "antipatternReportS3Object": S3ObjectTypeDef,
        "antipatternReportStatus": AntipatternReportStatusType,
        "antipatternReportStatusMessage": str,
        "appType": AppTypeType,
        "appUnitError": AppUnitErrorTypeDef,
        "associatedServerId": str,
        "databaseConfigDetail": DatabaseConfigDetailTypeDef,
        "id": str,
        "inclusionStatus": InclusionStatusType,
        "lastAnalyzedTimestamp": datetime,
        "listAntipatternSeveritySummary": List[AntipatternSeveritySummaryTypeDef],
        "moreServerAssociationExists": bool,
        "name": str,
        "osDriver": str,
        "osVersion": str,
        "recommendationSet": RecommendationSetTypeDef,
        "resourceSubType": ResourceSubTypeType,
        "resultList": List[ResultTypeDef],
        "runtimeStatus": RuntimeAnalysisStatusType,
        "runtimeStatusMessage": str,
        "sourceCodeRepositories": List[SourceCodeRepositoryTypeDef],
        "statusMessage": str,
    },
    total=False,
)

ListCollectorsResponseTypeDef = TypedDict(
    "ListCollectorsResponseTypeDef",
    {
        "Collectors": List[CollectorTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortfolioPreferencesResponseTypeDef = TypedDict(
    "GetPortfolioPreferencesResponseTypeDef",
    {
        "applicationMode": ApplicationModeType,
        "applicationPreferences": ApplicationPreferencesOutputTypeDef,
        "databasePreferences": DatabasePreferencesOutputTypeDef,
        "prioritizeBusinessGoals": PrioritizeBusinessGoalsOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPortfolioPreferencesRequestRequestTypeDef = TypedDict(
    "PutPortfolioPreferencesRequestRequestTypeDef",
    {
        "applicationMode": ApplicationModeType,
        "applicationPreferences": ApplicationPreferencesTypeDef,
        "databasePreferences": DatabasePreferencesTypeDef,
        "prioritizeBusinessGoals": PrioritizeBusinessGoalsTypeDef,
    },
    total=False,
)

GetApplicationComponentStrategiesResponseTypeDef = TypedDict(
    "GetApplicationComponentStrategiesResponseTypeDef",
    {
        "applicationComponentStrategies": List[ApplicationComponentStrategyTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServerDetailsResponseTypeDef = TypedDict(
    "GetServerDetailsResponseTypeDef",
    {
        "associatedApplications": List[AssociatedApplicationTypeDef],
        "nextToken": str,
        "serverDetail": ServerDetailTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "nextToken": str,
        "serverInfos": List[ServerDetailTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServerStrategiesResponseTypeDef = TypedDict(
    "GetServerStrategiesResponseTypeDef",
    {
        "serverStrategies": List[ServerStrategyTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationComponentDetailsResponseTypeDef = TypedDict(
    "GetApplicationComponentDetailsResponseTypeDef",
    {
        "applicationComponentDetail": ApplicationComponentDetailTypeDef,
        "associatedApplications": List[AssociatedApplicationTypeDef],
        "associatedServerIds": List[str],
        "moreApplicationResource": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationComponentsResponseTypeDef = TypedDict(
    "ListApplicationComponentsResponseTypeDef",
    {
        "applicationComponentInfos": List[ApplicationComponentDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
