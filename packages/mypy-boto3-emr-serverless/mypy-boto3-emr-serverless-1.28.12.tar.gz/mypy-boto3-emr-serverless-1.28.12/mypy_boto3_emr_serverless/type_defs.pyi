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
    "CancelJobRunResponseTypeDef",
    "CloudWatchLoggingConfigurationOutputTypeDef",
    "CloudWatchLoggingConfigurationTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationTypeDef",
    "ImageConfigurationInputTypeDef",
    "MaximumAllowedResourcesTypeDef",
    "NetworkConfigurationTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetDashboardForJobRunRequestRequestTypeDef",
    "GetDashboardForJobRunResponseTypeDef",
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
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedPersistenceMonitoringConfigurationOutputTypeDef",
    "ManagedPersistenceMonitoringConfigurationTypeDef",
    "S3MonitoringConfigurationOutputTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "WorkerTypeSpecificationTypeDef",
    "WorkerTypeSpecificationInputTypeDef",
    "InitialCapacityConfigOutputTypeDef",
    "InitialCapacityConfigTypeDef",
    "JobDriverOutputTypeDef",
    "JobDriverTypeDef",
    "ListJobRunsResponseTypeDef",
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

_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {
        "name": str,
        "stateDetails": str,
        "architecture": ArchitectureType,
    },
    total=False,
)

class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass

AutoStartConfigOutputTypeDef = TypedDict(
    "AutoStartConfigOutputTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

AutoStopConfigOutputTypeDef = TypedDict(
    "AutoStopConfigOutputTypeDef",
    {
        "enabled": bool,
        "idleTimeoutMinutes": int,
    },
    total=False,
)

_RequiredImageConfigurationTypeDef = TypedDict(
    "_RequiredImageConfigurationTypeDef",
    {
        "imageUri": str,
    },
)
_OptionalImageConfigurationTypeDef = TypedDict(
    "_OptionalImageConfigurationTypeDef",
    {
        "resolvedImageDigest": str,
    },
    total=False,
)

class ImageConfigurationTypeDef(
    _RequiredImageConfigurationTypeDef, _OptionalImageConfigurationTypeDef
):
    pass

_RequiredMaximumAllowedResourcesOutputTypeDef = TypedDict(
    "_RequiredMaximumAllowedResourcesOutputTypeDef",
    {
        "cpu": str,
        "memory": str,
    },
)
_OptionalMaximumAllowedResourcesOutputTypeDef = TypedDict(
    "_OptionalMaximumAllowedResourcesOutputTypeDef",
    {
        "disk": str,
    },
    total=False,
)

class MaximumAllowedResourcesOutputTypeDef(
    _RequiredMaximumAllowedResourcesOutputTypeDef, _OptionalMaximumAllowedResourcesOutputTypeDef
):
    pass

NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
    },
    total=False,
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

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCloudWatchLoggingConfigurationOutputTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingConfigurationOutputTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalCloudWatchLoggingConfigurationOutputTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingConfigurationOutputTypeDef",
    {
        "logGroupName": str,
        "logStreamNamePrefix": str,
        "encryptionKeyArn": str,
        "logTypes": Dict[str, List[str]],
    },
    total=False,
)

class CloudWatchLoggingConfigurationOutputTypeDef(
    _RequiredCloudWatchLoggingConfigurationOutputTypeDef,
    _OptionalCloudWatchLoggingConfigurationOutputTypeDef,
):
    pass

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

_RequiredConfigurationOutputTypeDef = TypedDict(
    "_RequiredConfigurationOutputTypeDef",
    {
        "classification": str,
    },
)
_OptionalConfigurationOutputTypeDef = TypedDict(
    "_OptionalConfigurationOutputTypeDef",
    {
        "properties": Dict[str, str],
        "configurations": List[Dict[str, Any]],
    },
    total=False,
)

class ConfigurationOutputTypeDef(
    _RequiredConfigurationOutputTypeDef, _OptionalConfigurationOutputTypeDef
):
    pass

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

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "applicationId": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

GetDashboardForJobRunResponseTypeDef = TypedDict(
    "GetDashboardForJobRunResponseTypeDef",
    {
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRunRequestRequestTypeDef = TypedDict(
    "GetJobRunRequestRequestTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
    },
)

_RequiredHiveOutputTypeDef = TypedDict(
    "_RequiredHiveOutputTypeDef",
    {
        "query": str,
    },
)
_OptionalHiveOutputTypeDef = TypedDict(
    "_OptionalHiveOutputTypeDef",
    {
        "initQueryFile": str,
        "parameters": str,
    },
    total=False,
)

class HiveOutputTypeDef(_RequiredHiveOutputTypeDef, _OptionalHiveOutputTypeDef):
    pass

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

_RequiredWorkerResourceConfigOutputTypeDef = TypedDict(
    "_RequiredWorkerResourceConfigOutputTypeDef",
    {
        "cpu": str,
        "memory": str,
    },
)
_OptionalWorkerResourceConfigOutputTypeDef = TypedDict(
    "_OptionalWorkerResourceConfigOutputTypeDef",
    {
        "disk": str,
    },
    total=False,
)

class WorkerResourceConfigOutputTypeDef(
    _RequiredWorkerResourceConfigOutputTypeDef, _OptionalWorkerResourceConfigOutputTypeDef
):
    pass

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

_RequiredSparkSubmitOutputTypeDef = TypedDict(
    "_RequiredSparkSubmitOutputTypeDef",
    {
        "entryPoint": str,
    },
)
_OptionalSparkSubmitOutputTypeDef = TypedDict(
    "_OptionalSparkSubmitOutputTypeDef",
    {
        "entryPointArguments": List[str],
        "sparkSubmitParameters": str,
    },
    total=False,
)

class SparkSubmitOutputTypeDef(
    _RequiredSparkSubmitOutputTypeDef, _OptionalSparkSubmitOutputTypeDef
):
    pass

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

_RequiredJobRunSummaryTypeDef = TypedDict(
    "_RequiredJobRunSummaryTypeDef",
    {
        "applicationId": str,
        "id": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
    },
)
_OptionalJobRunSummaryTypeDef = TypedDict(
    "_OptionalJobRunSummaryTypeDef",
    {
        "name": str,
        "type": str,
    },
    total=False,
)

class JobRunSummaryTypeDef(_RequiredJobRunSummaryTypeDef, _OptionalJobRunSummaryTypeDef):
    pass

ResourceUtilizationTypeDef = TypedDict(
    "ResourceUtilizationTypeDef",
    {
        "vCPUHour": float,
        "memoryGBHour": float,
        "storageGBHour": float,
    },
    total=False,
)

TotalResourceUtilizationTypeDef = TypedDict(
    "TotalResourceUtilizationTypeDef",
    {
        "vCPUHour": float,
        "memoryGBHour": float,
        "storageGBHour": float,
    },
    total=False,
)

ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "states": Sequence[ApplicationStateType],
        "PaginationConfig": "PaginatorConfigTypeDef",
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
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListJobRunsRequestListJobRunsPaginateTypeDef(
    _RequiredListJobRunsRequestListJobRunsPaginateTypeDef,
    _OptionalListJobRunsRequestListJobRunsPaginateTypeDef,
):
    pass

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

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedPersistenceMonitoringConfigurationOutputTypeDef = TypedDict(
    "ManagedPersistenceMonitoringConfigurationOutputTypeDef",
    {
        "enabled": bool,
        "encryptionKeyArn": str,
    },
    total=False,
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
    total=False,
)

S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
        "encryptionKeyArn": str,
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

StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applications": List[ApplicationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WorkerTypeSpecificationTypeDef = TypedDict(
    "WorkerTypeSpecificationTypeDef",
    {
        "imageConfiguration": ImageConfigurationTypeDef,
    },
    total=False,
)

WorkerTypeSpecificationInputTypeDef = TypedDict(
    "WorkerTypeSpecificationInputTypeDef",
    {
        "imageConfiguration": ImageConfigurationInputTypeDef,
    },
    total=False,
)

_RequiredInitialCapacityConfigOutputTypeDef = TypedDict(
    "_RequiredInitialCapacityConfigOutputTypeDef",
    {
        "workerCount": int,
    },
)
_OptionalInitialCapacityConfigOutputTypeDef = TypedDict(
    "_OptionalInitialCapacityConfigOutputTypeDef",
    {
        "workerConfiguration": WorkerResourceConfigOutputTypeDef,
    },
    total=False,
)

class InitialCapacityConfigOutputTypeDef(
    _RequiredInitialCapacityConfigOutputTypeDef, _OptionalInitialCapacityConfigOutputTypeDef
):
    pass

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
    total=False,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonitoringConfigurationOutputTypeDef = TypedDict(
    "MonitoringConfigurationOutputTypeDef",
    {
        "s3MonitoringConfiguration": S3MonitoringConfigurationOutputTypeDef,
        "managedPersistenceMonitoringConfiguration": (
            ManagedPersistenceMonitoringConfigurationOutputTypeDef
        ),
        "cloudWatchLoggingConfiguration": CloudWatchLoggingConfigurationOutputTypeDef,
    },
    total=False,
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

_RequiredApplicationTypeDef = TypedDict(
    "_RequiredApplicationTypeDef",
    {
        "applicationId": str,
        "arn": str,
        "releaseLabel": str,
        "type": str,
        "state": ApplicationStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalApplicationTypeDef = TypedDict(
    "_OptionalApplicationTypeDef",
    {
        "name": str,
        "stateDetails": str,
        "initialCapacity": Dict[str, InitialCapacityConfigOutputTypeDef],
        "maximumCapacity": MaximumAllowedResourcesOutputTypeDef,
        "tags": Dict[str, str],
        "autoStartConfiguration": AutoStartConfigOutputTypeDef,
        "autoStopConfiguration": AutoStopConfigOutputTypeDef,
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "architecture": ArchitectureType,
        "imageConfiguration": ImageConfigurationTypeDef,
        "workerTypeSpecifications": Dict[str, WorkerTypeSpecificationTypeDef],
    },
    total=False,
)

class ApplicationTypeDef(_RequiredApplicationTypeDef, _OptionalApplicationTypeDef):
    pass

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
    total=False,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "application": ApplicationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredJobRunTypeDef = TypedDict(
    "_RequiredJobRunTypeDef",
    {
        "applicationId": str,
        "jobRunId": str,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "executionRole": str,
        "state": JobRunStateType,
        "stateDetails": str,
        "releaseLabel": str,
        "jobDriver": JobDriverOutputTypeDef,
    },
)
_OptionalJobRunTypeDef = TypedDict(
    "_OptionalJobRunTypeDef",
    {
        "name": str,
        "configurationOverrides": ConfigurationOverridesOutputTypeDef,
        "tags": Dict[str, str],
        "totalResourceUtilization": TotalResourceUtilizationTypeDef,
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "totalExecutionDurationSeconds": int,
        "executionTimeoutMinutes": int,
        "billedResourceUtilization": ResourceUtilizationTypeDef,
    },
    total=False,
)

class JobRunTypeDef(_RequiredJobRunTypeDef, _OptionalJobRunTypeDef):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
