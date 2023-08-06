"""
Type annotations for emr-serverless service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/type_defs/)

Usage::

    ```python
    from mypy_boto3_emr_serverless.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import ApplicationStateType, ArchitectureType, JobRunStateType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSummaryTypeDef",
    "AutoStartConfigOutputTypeDef",
    "AutoStopConfigOutputTypeDef",
    "ImageConfigurationTypeDef",
    "MaximumAllowedResourcesOutputTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "AutoStartConfigTypeDef",
    "AutoStopConfigTypeDef",
    "CancelJobRunRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CloudWatchLoggingConfigurationOutputTypeDef",
    "CloudWatchLoggingConfigurationTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationTypeDef",
    "ImageConfigurationInputTypeDef",
    "MaximumAllowedResourcesTypeDef",
    "NetworkConfigurationTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetDashboardForJobRunRequestRequestTypeDef",
    "GetJobRunRequestRequestTypeDef",
    "HiveOutputTypeDef",
    "HiveTypeDef",
    "WorkerResourceConfigOutputTypeDef",
    "WorkerResourceConfigTypeDef",
    "SparkSubmitOutputTypeDef",
    "SparkSubmitTypeDef",
    "JobRunSummaryTypeDef",
    "ResourceUtilizationTypeDef",
    "TotalResourceUtilizationTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ManagedPersistenceMonitoringConfigurationOutputTypeDef",
    "ManagedPersistenceMonitoringConfigurationTypeDef",
    "S3MonitoringConfigurationOutputTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "WorkerTypeSpecificationTypeDef",
    "CancelJobRunResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "GetDashboardForJobRunResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "WorkerTypeSpecificationInputTypeDef",
    "InitialCapacityConfigOutputTypeDef",
    "InitialCapacityConfigTypeDef",
    "JobDriverOutputTypeDef",
    "JobDriverTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    "MonitoringConfigurationOutputTypeDef",
    "MonitoringConfigurationTypeDef",
    "ApplicationTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "ConfigurationOverridesOutputTypeDef",
    "ConfigurationOverridesTypeDef",
    "GetApplicationResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "JobRunTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "GetJobRunResponseTypeDef",
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "stateDetails": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "architecture": ArchitectureType,
    },
)

AutoStartConfigOutputTypeDef = TypedDict(
    "AutoStartConfigOutputTypeDef",
    {
        "enabled": bool,
    },
)

AutoStopConfigOutputTypeDef = TypedDict(
    "AutoStopConfigOutputTypeDef",
    {
        "enabled": bool,
        "idleTimeoutMinutes": int,
    },
)

ImageConfigurationTypeDef = TypedDict(
    "ImageConfigurationTypeDef",
    {
        "imageUri": str,
        "resolvedImageDigest": str,
    },
)

MaximumAllowedResourcesOutputTypeDef = TypedDict(
    "MaximumAllowedResourcesOutputTypeDef",
    {
        "cpu": str,
        "memory": str,
        "disk": str,
    },
)

NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
    },
)

AutoStartConfigTypeDef = TypedDict(
    "AutoStartConfigTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

AutoStopConfigTypeDef = TypedDict(
    "AutoStopConfigTypeDef",
    {
        "enabled": bool,
        "idleTimeoutMinutes": int,
    },
    total=False,
)

CancelJobRunRequestRequestTypeDef = TypedDict(
    "CancelJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
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

CloudWatchLoggingConfigurationOutputTypeDef = TypedDict(
    "CloudWatchLoggingConfigurationOutputTypeDef",
    {
        "enabled": bool,
        "logGroupName": str,
        "logStreamNamePrefix": str,
        "encryptionKeyArn": str,
        "logTypes": Dict[str, List[str]],
    },
)

_RequiredCloudWatchLoggingConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingConfigurationTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalCloudWatchLoggingConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingConfigurationTypeDef",
    {
        "logGroupName": str,
        "logStreamNamePrefix": str,
        "encryptionKeyArn": str,
        "logTypes": Mapping[str, Sequence[str]],
    },
    total=False,
)


class CloudWatchLoggingConfigurationTypeDef(
    _RequiredCloudWatchLoggingConfigurationTypeDef, _OptionalCloudWatchLoggingConfigurationTypeDef
):
    pass


ConfigurationOutputTypeDef = TypedDict(
    "ConfigurationOutputTypeDef",
    {
        "classification": str,
        "properties": Dict[str, str],
        "configurations": List[Dict[str, Any]],
    },
)

_RequiredConfigurationTypeDef = TypedDict(
    "_RequiredConfigurationTypeDef",
    {
        "classification": str,
    },
)
_OptionalConfigurationTypeDef = TypedDict(
    "_OptionalConfigurationTypeDef",
    {
        "properties": Mapping[str, str],
        "configurations": Sequence[Dict[str, Any]],
    },
    total=False,
)


class ConfigurationTypeDef(_RequiredConfigurationTypeDef, _OptionalConfigurationTypeDef):
    pass


ImageConfigurationInputTypeDef = TypedDict(
    "ImageConfigurationInputTypeDef",
    {
        "imageUri": str,
    },
    total=False,
)

_RequiredMaximumAllowedResourcesTypeDef = TypedDict(
    "_RequiredMaximumAllowedResourcesTypeDef",
    {
        "cpu": str,
        "memory": str,
    },
)
_OptionalMaximumAllowedResourcesTypeDef = TypedDict(
    "_OptionalMaximumAllowedResourcesTypeDef",
    {
        "disk": str,
    },
    total=False,
)


class MaximumAllowedResourcesTypeDef(
    _RequiredMaximumAllowedResourcesTypeDef, _OptionalMaximumAllowedResourcesTypeDef
):
    pass


NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "subnetIds": Sequence[str],
        "securityGroupIds": Sequence[str],
    },
    total=False,
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

GetDashboardForJobRunRequestRequestTypeDef = TypedDict(
    "GetDashboardForJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
    },
)

GetJobRunRequestRequestTypeDef = TypedDict(
    "GetJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
    },
)

HiveOutputTypeDef = TypedDict(
    "HiveOutputTypeDef",
    {
        "query": str,
        "initQueryFile": str,
        "parameters": str,
    },
)

_RequiredHiveTypeDef = TypedDict(
    "_RequiredHiveTypeDef",
    {
        "query": str,
    },
)
_OptionalHiveTypeDef = TypedDict(
    "_OptionalHiveTypeDef",
    {
        "initQueryFile": str,
        "parameters": str,
    },
    total=False,
)


class HiveTypeDef(_RequiredHiveTypeDef, _OptionalHiveTypeDef):
    pass


WorkerResourceConfigOutputTypeDef = TypedDict(
    "WorkerResourceConfigOutputTypeDef",
    {
        "cpu": str,
        "memory": str,
        "disk": str,
    },
)

_RequiredWorkerResourceConfigTypeDef = TypedDict(
    "_RequiredWorkerResourceConfigTypeDef",
    {
        "cpu": str,
        "memory": str,
    },
)
_OptionalWorkerResourceConfigTypeDef = TypedDict(
    "_OptionalWorkerResourceConfigTypeDef",
    {
        "disk": str,
    },
    total=False,
)


class WorkerResourceConfigTypeDef(
    _RequiredWorkerResourceConfigTypeDef, _OptionalWorkerResourceConfigTypeDef
):
    pass


SparkSubmitOutputTypeDef = TypedDict(
    "SparkSubmitOutputTypeDef",
    {
        "entryPoint": str,
        "entryPointArguments": List[str],
        "sparkSubmitParameters": str,
    },
)

_RequiredSparkSubmitTypeDef = TypedDict(
    "_RequiredSparkSubmitTypeDef",
    {
        "entryPoint": str,
    },
)
_OptionalSparkSubmitTypeDef = TypedDict(
    "_OptionalSparkSubmitTypeDef",
    {
        "entryPointArguments": Sequence[str],
        "sparkSubmitParameters": str,
    },
    total=False,
)


class SparkSubmitTypeDef(_RequiredSparkSubmitTypeDef, _OptionalSparkSubmitTypeDef):
    pass


JobRunSummaryTypeDef = TypedDict(
    "JobRunSummaryTypeDef",
    {
        "applicationId": str,
        "id": str,
        "name": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
        "type": str,
    },
)

ResourceUtilizationTypeDef = TypedDict(
    "ResourceUtilizationTypeDef",
    {
        "vCPUHour": float,
        "memoryGBHour": float,
        "storageGBHour": float,
    },
)

TotalResourceUtilizationTypeDef = TypedDict(
    "TotalResourceUtilizationTypeDef",
    {
        "vCPUHour": float,
        "memoryGBHour": float,
        "storageGBHour": float,
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

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "states": Sequence[ApplicationStateType],
    },
    total=False,
)

_RequiredListJobRunsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobRunsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListJobRunsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobRunsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "createdAtAfter": Union[datetime, str],
        "createdAtBefore": Union[datetime, str],
        "states": Sequence[JobRunStateType],
    },
    total=False,
)


class ListJobRunsRequestRequestTypeDef(
    _RequiredListJobRunsRequestRequestTypeDef, _OptionalListJobRunsRequestRequestTypeDef
):
    pass


ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ManagedPersistenceMonitoringConfigurationOutputTypeDef = TypedDict(
    "ManagedPersistenceMonitoringConfigurationOutputTypeDef",
    {
        "enabled": bool,
        "encryptionKeyArn": str,
    },
)

ManagedPersistenceMonitoringConfigurationTypeDef = TypedDict(
    "ManagedPersistenceMonitoringConfigurationTypeDef",
    {
        "enabled": bool,
        "encryptionKeyArn": str,
    },
    total=False,
)

S3MonitoringConfigurationOutputTypeDef = TypedDict(
    "S3MonitoringConfigurationOutputTypeDef",
    {
        "logUri": str,
        "encryptionKeyArn": str,
    },
)

S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
        "encryptionKeyArn": str,
    },
    total=False,
)

StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

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

WorkerTypeSpecificationTypeDef = TypedDict(
    "WorkerTypeSpecificationTypeDef",
    {
        "imageConfiguration": ImageConfigurationTypeDef,
    },
)

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "applicationId": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDashboardForJobRunResponseTypeDef = TypedDict(
    "GetDashboardForJobRunResponseTypeDef",
    {
        "url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applications": List[ApplicationSummaryTypeDef],
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

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

WorkerTypeSpecificationInputTypeDef = TypedDict(
    "WorkerTypeSpecificationInputTypeDef",
    {
        "imageConfiguration": ImageConfigurationInputTypeDef,
    },
    total=False,
)

InitialCapacityConfigOutputTypeDef = TypedDict(
    "InitialCapacityConfigOutputTypeDef",
    {
        "workerCount": int,
        "workerConfiguration": WorkerResourceConfigOutputTypeDef,
    },
)

_RequiredInitialCapacityConfigTypeDef = TypedDict(
    "_RequiredInitialCapacityConfigTypeDef",
    {
        "workerCount": int,
    },
)
_OptionalInitialCapacityConfigTypeDef = TypedDict(
    "_OptionalInitialCapacityConfigTypeDef",
    {
        "workerConfiguration": WorkerResourceConfigTypeDef,
    },
    total=False,
)


class InitialCapacityConfigTypeDef(
    _RequiredInitialCapacityConfigTypeDef, _OptionalInitialCapacityConfigTypeDef
):
    pass


JobDriverOutputTypeDef = TypedDict(
    "JobDriverOutputTypeDef",
    {
        "sparkSubmit": SparkSubmitOutputTypeDef,
        "hive": HiveOutputTypeDef,
    },
)

JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmit": SparkSubmitTypeDef,
        "hive": HiveTypeDef,
    },
    total=False,
)

ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "jobRuns": List[JobRunSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "states": Sequence[ApplicationStateType],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "_RequiredListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "_OptionalListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "createdAtAfter": Union[datetime, str],
        "createdAtBefore": Union[datetime, str],
        "states": Sequence[JobRunStateType],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListJobRunsRequestListJobRunsPaginateTypeDef(
    _RequiredListJobRunsRequestListJobRunsPaginateTypeDef,
    _OptionalListJobRunsRequestListJobRunsPaginateTypeDef,
):
    pass


MonitoringConfigurationOutputTypeDef = TypedDict(
    "MonitoringConfigurationOutputTypeDef",
    {
        "s3MonitoringConfiguration": S3MonitoringConfigurationOutputTypeDef,
        "managedPersistenceMonitoringConfiguration": (
            ManagedPersistenceMonitoringConfigurationOutputTypeDef
        ),
        "cloudWatchLoggingConfiguration": CloudWatchLoggingConfigurationOutputTypeDef,
    },
)

MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "s3MonitoringConfiguration": S3MonitoringConfigurationTypeDef,
        "managedPersistenceMonitoringConfiguration": (
            ManagedPersistenceMonitoringConfigurationTypeDef
        ),
        "cloudWatchLoggingConfiguration": CloudWatchLoggingConfigurationTypeDef,
    },
    total=False,
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "applicationId": str,
        "name": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "stateDetails": str,
        "initialCapacity": Dict[str, InitialCapacityConfigOutputTypeDef],
        "maximumCapacity": MaximumAllowedResourcesOutputTypeDef,
        "createdAt": datetime,
        "updatedAt": datetime,
        "tags": Dict[str, str],
        "autoStartConfiguration": AutoStartConfigOutputTypeDef,
        "autoStopConfiguration": AutoStopConfigOutputTypeDef,
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "architecture": ArchitectureType,
        "imageConfiguration": ImageConfigurationTypeDef,
        "workerTypeSpecifications": Dict[str, WorkerTypeSpecificationTypeDef],
    },
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "releaseLabel": str,
        "type": str,
        "clientToken": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "initialCapacity": Mapping[str, InitialCapacityConfigTypeDef],
        "maximumCapacity": MaximumAllowedResourcesTypeDef,
        "tags": Mapping[str, str],
        "autoStartConfiguration": AutoStartConfigTypeDef,
        "autoStopConfiguration": AutoStopConfigTypeDef,
        "networkConfiguration": NetworkConfigurationTypeDef,
        "architecture": ArchitectureType,
        "imageConfiguration": ImageConfigurationInputTypeDef,
        "workerTypeSpecifications": Mapping[str, WorkerTypeSpecificationInputTypeDef],
    },
    total=False,
)


class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass


_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
        "clientToken": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "initialCapacity": Mapping[str, InitialCapacityConfigTypeDef],
        "maximumCapacity": MaximumAllowedResourcesTypeDef,
        "autoStartConfiguration": AutoStartConfigTypeDef,
        "autoStopConfiguration": AutoStopConfigTypeDef,
        "networkConfiguration": NetworkConfigurationTypeDef,
        "architecture": ArchitectureType,
        "imageConfiguration": ImageConfigurationInputTypeDef,
        "workerTypeSpecifications": Mapping[str, WorkerTypeSpecificationInputTypeDef],
        "releaseLabel": str,
    },
    total=False,
)


class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass


ConfigurationOverridesOutputTypeDef = TypedDict(
    "ConfigurationOverridesOutputTypeDef",
    {
        "applicationConfiguration": List["ConfigurationOutputTypeDef"],
        "monitoringConfiguration": MonitoringConfigurationOutputTypeDef,
    },
)

ConfigurationOverridesTypeDef = TypedDict(
    "ConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": Sequence["ConfigurationTypeDef"],
        "monitoringConfiguration": MonitoringConfigurationTypeDef,
    },
    total=False,
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "application": ApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "application": ApplicationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "name": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
        "configurationOverrides": ConfigurationOverridesOutputTypeDef,
        "jobDriver": JobDriverOutputTypeDef,
        "tags": Dict[str, str],
        "totalResourceUtilization": TotalResourceUtilizationTypeDef,
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "totalExecutionDurationSeconds": int,
        "executionTimeoutMinutes": int,
        "billedResourceUtilization": ResourceUtilizationTypeDef,
    },
)

_RequiredStartJobRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "clientToken": str,
        "executionRoleArn": str,
    },
)
_OptionalStartJobRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartJobRunRequestRequestTypeDef",
    {
        "jobDriver": JobDriverTypeDef,
        "configurationOverrides": ConfigurationOverridesTypeDef,
        "tags": Mapping[str, str],
        "executionTimeoutMinutes": int,
        "name": str,
    },
    total=False,
)


class StartJobRunRequestRequestTypeDef(
    _RequiredStartJobRunRequestRequestTypeDef, _OptionalStartJobRunRequestRequestTypeDef
):
    pass


GetJobRunResponseTypeDef = TypedDict(
    "GetJobRunResponseTypeDef",
    {
        "jobRun": JobRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
