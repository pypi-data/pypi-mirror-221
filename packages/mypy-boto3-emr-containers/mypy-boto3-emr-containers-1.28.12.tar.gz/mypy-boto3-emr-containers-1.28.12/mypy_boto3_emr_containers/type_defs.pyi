"""
Type annotations for emr-containers service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/type_defs/)

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import CancelJobRunRequestRequestTypeDef

    data: CancelJobRunRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    EndpointStateType,
    FailureReasonType,
    JobRunStateType,
    PersistentAppUIType,
    TemplateParameterDataTypeType,
    VirtualClusterStateType,
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
    "CancelJobRunRequestRequestTypeDef",
    "CancelJobRunResponseTypeDef",
    "CertificateTypeDef",
    "CloudWatchMonitoringConfigurationOutputTypeDef",
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationTypeDef",
    "EksInfoOutputTypeDef",
    "EksInfoTypeDef",
    "ContainerLogRotationConfigurationOutputTypeDef",
    "ContainerLogRotationConfigurationTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreateManagedEndpointResponseTypeDef",
    "CreateVirtualClusterResponseTypeDef",
    "CredentialsTypeDef",
    "DeleteJobTemplateRequestRequestTypeDef",
    "DeleteJobTemplateResponseTypeDef",
    "DeleteManagedEndpointRequestRequestTypeDef",
    "DeleteManagedEndpointResponseTypeDef",
    "DeleteVirtualClusterRequestRequestTypeDef",
    "DeleteVirtualClusterResponseTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeJobTemplateRequestRequestTypeDef",
    "DescribeManagedEndpointRequestRequestTypeDef",
    "DescribeVirtualClusterRequestRequestTypeDef",
    "GetManagedEndpointSessionCredentialsRequestRequestTypeDef",
    "SparkSqlJobDriverOutputTypeDef",
    "SparkSubmitJobDriverOutputTypeDef",
    "SparkSqlJobDriverTypeDef",
    "SparkSubmitJobDriverTypeDef",
    "RetryPolicyConfigurationOutputTypeDef",
    "RetryPolicyExecutionTypeDef",
    "TemplateParameterConfigurationOutputTypeDef",
    "TemplateParameterConfigurationTypeDef",
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobTemplatesRequestListJobTemplatesPaginateTypeDef",
    "ListJobTemplatesRequestRequestTypeDef",
    "ListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef",
    "ListManagedEndpointsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVirtualClustersRequestListVirtualClustersPaginateTypeDef",
    "ListVirtualClustersRequestRequestTypeDef",
    "S3MonitoringConfigurationOutputTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParametricCloudWatchMonitoringConfigurationOutputTypeDef",
    "ParametricCloudWatchMonitoringConfigurationTypeDef",
    "ParametricS3MonitoringConfigurationOutputTypeDef",
    "ParametricS3MonitoringConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryPolicyConfigurationTypeDef",
    "StartJobRunResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ContainerInfoOutputTypeDef",
    "ContainerInfoTypeDef",
    "GetManagedEndpointSessionCredentialsResponseTypeDef",
    "JobDriverOutputTypeDef",
    "JobDriverTypeDef",
    "MonitoringConfigurationOutputTypeDef",
    "MonitoringConfigurationTypeDef",
    "ParametricMonitoringConfigurationOutputTypeDef",
    "ParametricMonitoringConfigurationTypeDef",
    "ContainerProviderOutputTypeDef",
    "ContainerProviderTypeDef",
    "ConfigurationOverridesOutputTypeDef",
    "ConfigurationOverridesTypeDef",
    "ParametricConfigurationOverridesOutputTypeDef",
    "ParametricConfigurationOverridesTypeDef",
    "VirtualClusterTypeDef",
    "CreateVirtualClusterRequestRequestTypeDef",
    "EndpointTypeDef",
    "JobRunTypeDef",
    "CreateManagedEndpointRequestRequestTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "JobTemplateDataOutputTypeDef",
    "JobTemplateDataTypeDef",
    "DescribeVirtualClusterResponseTypeDef",
    "ListVirtualClustersResponseTypeDef",
    "DescribeManagedEndpointResponseTypeDef",
    "ListManagedEndpointsResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "ListJobRunsResponseTypeDef",
    "JobTemplateTypeDef",
    "CreateJobTemplateRequestRequestTypeDef",
    "DescribeJobTemplateResponseTypeDef",
    "ListJobTemplatesResponseTypeDef",
)

CancelJobRunRequestRequestTypeDef = TypedDict(
    "CancelJobRunRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "certificateArn": str,
        "certificateData": str,
    },
    total=False,
)

_RequiredCloudWatchMonitoringConfigurationOutputTypeDef = TypedDict(
    "_RequiredCloudWatchMonitoringConfigurationOutputTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalCloudWatchMonitoringConfigurationOutputTypeDef = TypedDict(
    "_OptionalCloudWatchMonitoringConfigurationOutputTypeDef",
    {
        "logStreamNamePrefix": str,
    },
    total=False,
)

class CloudWatchMonitoringConfigurationOutputTypeDef(
    _RequiredCloudWatchMonitoringConfigurationOutputTypeDef,
    _OptionalCloudWatchMonitoringConfigurationOutputTypeDef,
):
    pass

_RequiredCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchMonitoringConfigurationTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchMonitoringConfigurationTypeDef",
    {
        "logStreamNamePrefix": str,
    },
    total=False,
)

class CloudWatchMonitoringConfigurationTypeDef(
    _RequiredCloudWatchMonitoringConfigurationTypeDef,
    _OptionalCloudWatchMonitoringConfigurationTypeDef,
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

EksInfoOutputTypeDef = TypedDict(
    "EksInfoOutputTypeDef",
    {
        "namespace": str,
    },
    total=False,
)

EksInfoTypeDef = TypedDict(
    "EksInfoTypeDef",
    {
        "namespace": str,
    },
    total=False,
)

ContainerLogRotationConfigurationOutputTypeDef = TypedDict(
    "ContainerLogRotationConfigurationOutputTypeDef",
    {
        "rotationSize": str,
        "maxFilesToKeep": int,
    },
)

ContainerLogRotationConfigurationTypeDef = TypedDict(
    "ContainerLogRotationConfigurationTypeDef",
    {
        "rotationSize": str,
        "maxFilesToKeep": int,
    },
)

CreateJobTemplateResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateManagedEndpointResponseTypeDef = TypedDict(
    "CreateManagedEndpointResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVirtualClusterResponseTypeDef = TypedDict(
    "CreateVirtualClusterResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "token": str,
    },
    total=False,
)

DeleteJobTemplateRequestRequestTypeDef = TypedDict(
    "DeleteJobTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteJobTemplateResponseTypeDef = TypedDict(
    "DeleteJobTemplateResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteManagedEndpointRequestRequestTypeDef = TypedDict(
    "DeleteManagedEndpointRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DeleteManagedEndpointResponseTypeDef = TypedDict(
    "DeleteManagedEndpointResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVirtualClusterRequestRequestTypeDef = TypedDict(
    "DeleteVirtualClusterRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteVirtualClusterResponseTypeDef = TypedDict(
    "DeleteVirtualClusterResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DescribeJobTemplateRequestRequestTypeDef = TypedDict(
    "DescribeJobTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeManagedEndpointRequestRequestTypeDef = TypedDict(
    "DescribeManagedEndpointRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DescribeVirtualClusterRequestRequestTypeDef = TypedDict(
    "DescribeVirtualClusterRequestRequestTypeDef",
    {
        "id": str,
    },
)

_RequiredGetManagedEndpointSessionCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredGetManagedEndpointSessionCredentialsRequestRequestTypeDef",
    {
        "endpointIdentifier": str,
        "virtualClusterIdentifier": str,
        "executionRoleArn": str,
        "credentialType": str,
    },
)
_OptionalGetManagedEndpointSessionCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalGetManagedEndpointSessionCredentialsRequestRequestTypeDef",
    {
        "durationInSeconds": int,
        "logContext": str,
        "clientToken": str,
    },
    total=False,
)

class GetManagedEndpointSessionCredentialsRequestRequestTypeDef(
    _RequiredGetManagedEndpointSessionCredentialsRequestRequestTypeDef,
    _OptionalGetManagedEndpointSessionCredentialsRequestRequestTypeDef,
):
    pass

SparkSqlJobDriverOutputTypeDef = TypedDict(
    "SparkSqlJobDriverOutputTypeDef",
    {
        "entryPoint": str,
        "sparkSqlParameters": str,
    },
    total=False,
)

_RequiredSparkSubmitJobDriverOutputTypeDef = TypedDict(
    "_RequiredSparkSubmitJobDriverOutputTypeDef",
    {
        "entryPoint": str,
    },
)
_OptionalSparkSubmitJobDriverOutputTypeDef = TypedDict(
    "_OptionalSparkSubmitJobDriverOutputTypeDef",
    {
        "entryPointArguments": List[str],
        "sparkSubmitParameters": str,
    },
    total=False,
)

class SparkSubmitJobDriverOutputTypeDef(
    _RequiredSparkSubmitJobDriverOutputTypeDef, _OptionalSparkSubmitJobDriverOutputTypeDef
):
    pass

SparkSqlJobDriverTypeDef = TypedDict(
    "SparkSqlJobDriverTypeDef",
    {
        "entryPoint": str,
        "sparkSqlParameters": str,
    },
    total=False,
)

_RequiredSparkSubmitJobDriverTypeDef = TypedDict(
    "_RequiredSparkSubmitJobDriverTypeDef",
    {
        "entryPoint": str,
    },
)
_OptionalSparkSubmitJobDriverTypeDef = TypedDict(
    "_OptionalSparkSubmitJobDriverTypeDef",
    {
        "entryPointArguments": Sequence[str],
        "sparkSubmitParameters": str,
    },
    total=False,
)

class SparkSubmitJobDriverTypeDef(
    _RequiredSparkSubmitJobDriverTypeDef, _OptionalSparkSubmitJobDriverTypeDef
):
    pass

RetryPolicyConfigurationOutputTypeDef = TypedDict(
    "RetryPolicyConfigurationOutputTypeDef",
    {
        "maxAttempts": int,
    },
)

RetryPolicyExecutionTypeDef = TypedDict(
    "RetryPolicyExecutionTypeDef",
    {
        "currentAttemptCount": int,
    },
)

TemplateParameterConfigurationOutputTypeDef = TypedDict(
    "TemplateParameterConfigurationOutputTypeDef",
    {
        "type": TemplateParameterDataTypeType,
        "defaultValue": str,
    },
    total=False,
)

TemplateParameterConfigurationTypeDef = TypedDict(
    "TemplateParameterConfigurationTypeDef",
    {
        "type": TemplateParameterDataTypeType,
        "defaultValue": str,
    },
    total=False,
)

_RequiredListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "_RequiredListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "virtualClusterId": str,
    },
)
_OptionalListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "_OptionalListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "createdBefore": Union[datetime, str],
        "createdAfter": Union[datetime, str],
        "name": str,
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
        "virtualClusterId": str,
    },
)
_OptionalListJobRunsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobRunsRequestRequestTypeDef",
    {
        "createdBefore": Union[datetime, str],
        "createdAfter": Union[datetime, str],
        "name": str,
        "states": Sequence[JobRunStateType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListJobRunsRequestRequestTypeDef(
    _RequiredListJobRunsRequestRequestTypeDef, _OptionalListJobRunsRequestRequestTypeDef
):
    pass

ListJobTemplatesRequestListJobTemplatesPaginateTypeDef = TypedDict(
    "ListJobTemplatesRequestListJobTemplatesPaginateTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListJobTemplatesRequestRequestTypeDef = TypedDict(
    "ListJobTemplatesRequestRequestTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef = TypedDict(
    "_RequiredListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef",
    {
        "virtualClusterId": str,
    },
)
_OptionalListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef = TypedDict(
    "_OptionalListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef",
    {
        "createdBefore": Union[datetime, str],
        "createdAfter": Union[datetime, str],
        "types": Sequence[str],
        "states": Sequence[EndpointStateType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef(
    _RequiredListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef,
    _OptionalListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef,
):
    pass

_RequiredListManagedEndpointsRequestRequestTypeDef = TypedDict(
    "_RequiredListManagedEndpointsRequestRequestTypeDef",
    {
        "virtualClusterId": str,
    },
)
_OptionalListManagedEndpointsRequestRequestTypeDef = TypedDict(
    "_OptionalListManagedEndpointsRequestRequestTypeDef",
    {
        "createdBefore": Union[datetime, str],
        "createdAfter": Union[datetime, str],
        "types": Sequence[str],
        "states": Sequence[EndpointStateType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListManagedEndpointsRequestRequestTypeDef(
    _RequiredListManagedEndpointsRequestRequestTypeDef,
    _OptionalListManagedEndpointsRequestRequestTypeDef,
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

ListVirtualClustersRequestListVirtualClustersPaginateTypeDef = TypedDict(
    "ListVirtualClustersRequestListVirtualClustersPaginateTypeDef",
    {
        "containerProviderId": str,
        "containerProviderType": Literal["EKS"],
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "states": Sequence[VirtualClusterStateType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListVirtualClustersRequestRequestTypeDef = TypedDict(
    "ListVirtualClustersRequestRequestTypeDef",
    {
        "containerProviderId": str,
        "containerProviderType": Literal["EKS"],
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "states": Sequence[VirtualClusterStateType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

S3MonitoringConfigurationOutputTypeDef = TypedDict(
    "S3MonitoringConfigurationOutputTypeDef",
    {
        "logUri": str,
    },
)

S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
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

ParametricCloudWatchMonitoringConfigurationOutputTypeDef = TypedDict(
    "ParametricCloudWatchMonitoringConfigurationOutputTypeDef",
    {
        "logGroupName": str,
        "logStreamNamePrefix": str,
    },
    total=False,
)

ParametricCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "ParametricCloudWatchMonitoringConfigurationTypeDef",
    {
        "logGroupName": str,
        "logStreamNamePrefix": str,
    },
    total=False,
)

ParametricS3MonitoringConfigurationOutputTypeDef = TypedDict(
    "ParametricS3MonitoringConfigurationOutputTypeDef",
    {
        "logUri": str,
    },
    total=False,
)

ParametricS3MonitoringConfigurationTypeDef = TypedDict(
    "ParametricS3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
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

RetryPolicyConfigurationTypeDef = TypedDict(
    "RetryPolicyConfigurationTypeDef",
    {
        "maxAttempts": int,
    },
)

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ContainerInfoOutputTypeDef = TypedDict(
    "ContainerInfoOutputTypeDef",
    {
        "eksInfo": EksInfoOutputTypeDef,
    },
    total=False,
)

ContainerInfoTypeDef = TypedDict(
    "ContainerInfoTypeDef",
    {
        "eksInfo": EksInfoTypeDef,
    },
    total=False,
)

GetManagedEndpointSessionCredentialsResponseTypeDef = TypedDict(
    "GetManagedEndpointSessionCredentialsResponseTypeDef",
    {
        "id": str,
        "credentials": CredentialsTypeDef,
        "expiresAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobDriverOutputTypeDef = TypedDict(
    "JobDriverOutputTypeDef",
    {
        "sparkSubmitJobDriver": SparkSubmitJobDriverOutputTypeDef,
        "sparkSqlJobDriver": SparkSqlJobDriverOutputTypeDef,
    },
    total=False,
)

JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmitJobDriver": SparkSubmitJobDriverTypeDef,
        "sparkSqlJobDriver": SparkSqlJobDriverTypeDef,
    },
    total=False,
)

MonitoringConfigurationOutputTypeDef = TypedDict(
    "MonitoringConfigurationOutputTypeDef",
    {
        "persistentAppUI": PersistentAppUIType,
        "cloudWatchMonitoringConfiguration": CloudWatchMonitoringConfigurationOutputTypeDef,
        "s3MonitoringConfiguration": S3MonitoringConfigurationOutputTypeDef,
        "containerLogRotationConfiguration": ContainerLogRotationConfigurationOutputTypeDef,
    },
    total=False,
)

MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "persistentAppUI": PersistentAppUIType,
        "cloudWatchMonitoringConfiguration": CloudWatchMonitoringConfigurationTypeDef,
        "s3MonitoringConfiguration": S3MonitoringConfigurationTypeDef,
        "containerLogRotationConfiguration": ContainerLogRotationConfigurationTypeDef,
    },
    total=False,
)

ParametricMonitoringConfigurationOutputTypeDef = TypedDict(
    "ParametricMonitoringConfigurationOutputTypeDef",
    {
        "persistentAppUI": str,
        "cloudWatchMonitoringConfiguration": (
            ParametricCloudWatchMonitoringConfigurationOutputTypeDef
        ),
        "s3MonitoringConfiguration": ParametricS3MonitoringConfigurationOutputTypeDef,
    },
    total=False,
)

ParametricMonitoringConfigurationTypeDef = TypedDict(
    "ParametricMonitoringConfigurationTypeDef",
    {
        "persistentAppUI": str,
        "cloudWatchMonitoringConfiguration": ParametricCloudWatchMonitoringConfigurationTypeDef,
        "s3MonitoringConfiguration": ParametricS3MonitoringConfigurationTypeDef,
    },
    total=False,
)

_RequiredContainerProviderOutputTypeDef = TypedDict(
    "_RequiredContainerProviderOutputTypeDef",
    {
        "type": Literal["EKS"],
        "id": str,
    },
)
_OptionalContainerProviderOutputTypeDef = TypedDict(
    "_OptionalContainerProviderOutputTypeDef",
    {
        "info": ContainerInfoOutputTypeDef,
    },
    total=False,
)

class ContainerProviderOutputTypeDef(
    _RequiredContainerProviderOutputTypeDef, _OptionalContainerProviderOutputTypeDef
):
    pass

_RequiredContainerProviderTypeDef = TypedDict(
    "_RequiredContainerProviderTypeDef",
    {
        "type": Literal["EKS"],
        "id": str,
    },
)
_OptionalContainerProviderTypeDef = TypedDict(
    "_OptionalContainerProviderTypeDef",
    {
        "info": ContainerInfoTypeDef,
    },
    total=False,
)

class ContainerProviderTypeDef(
    _RequiredContainerProviderTypeDef, _OptionalContainerProviderTypeDef
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

ParametricConfigurationOverridesOutputTypeDef = TypedDict(
    "ParametricConfigurationOverridesOutputTypeDef",
    {
        "applicationConfiguration": List["ConfigurationOutputTypeDef"],
        "monitoringConfiguration": ParametricMonitoringConfigurationOutputTypeDef,
    },
    total=False,
)

ParametricConfigurationOverridesTypeDef = TypedDict(
    "ParametricConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": Sequence["ConfigurationTypeDef"],
        "monitoringConfiguration": ParametricMonitoringConfigurationTypeDef,
    },
    total=False,
)

VirtualClusterTypeDef = TypedDict(
    "VirtualClusterTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "state": VirtualClusterStateType,
        "containerProvider": ContainerProviderOutputTypeDef,
        "createdAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateVirtualClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualClusterRequestRequestTypeDef",
    {
        "name": str,
        "containerProvider": ContainerProviderTypeDef,
        "clientToken": str,
    },
)
_OptionalCreateVirtualClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualClusterRequestRequestTypeDef",
    {
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateVirtualClusterRequestRequestTypeDef(
    _RequiredCreateVirtualClusterRequestRequestTypeDef,
    _OptionalCreateVirtualClusterRequestRequestTypeDef,
):
    pass

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "type": str,
        "state": EndpointStateType,
        "releaseLabel": str,
        "executionRoleArn": str,
        "certificateArn": str,
        "certificateAuthority": CertificateTypeDef,
        "configurationOverrides": ConfigurationOverridesOutputTypeDef,
        "serverUrl": str,
        "createdAt": datetime,
        "securityGroup": str,
        "subnetIds": List[str],
        "stateDetails": str,
        "failureReason": FailureReasonType,
        "tags": Dict[str, str],
    },
    total=False,
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "id": str,
        "name": str,
        "virtualClusterId": str,
        "arn": str,
        "state": JobRunStateType,
        "clientToken": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "configurationOverrides": ConfigurationOverridesOutputTypeDef,
        "jobDriver": JobDriverOutputTypeDef,
        "createdAt": datetime,
        "createdBy": str,
        "finishedAt": datetime,
        "stateDetails": str,
        "failureReason": FailureReasonType,
        "tags": Dict[str, str],
        "retryPolicyConfiguration": RetryPolicyConfigurationOutputTypeDef,
        "retryPolicyExecution": RetryPolicyExecutionTypeDef,
    },
    total=False,
)

_RequiredCreateManagedEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateManagedEndpointRequestRequestTypeDef",
    {
        "name": str,
        "virtualClusterId": str,
        "type": str,
        "releaseLabel": str,
        "executionRoleArn": str,
        "clientToken": str,
    },
)
_OptionalCreateManagedEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateManagedEndpointRequestRequestTypeDef",
    {
        "certificateArn": str,
        "configurationOverrides": ConfigurationOverridesTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateManagedEndpointRequestRequestTypeDef(
    _RequiredCreateManagedEndpointRequestRequestTypeDef,
    _OptionalCreateManagedEndpointRequestRequestTypeDef,
):
    pass

_RequiredStartJobRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartJobRunRequestRequestTypeDef",
    {
        "virtualClusterId": str,
        "clientToken": str,
    },
)
_OptionalStartJobRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartJobRunRequestRequestTypeDef",
    {
        "name": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": JobDriverTypeDef,
        "configurationOverrides": ConfigurationOverridesTypeDef,
        "tags": Mapping[str, str],
        "jobTemplateId": str,
        "jobTemplateParameters": Mapping[str, str],
        "retryPolicyConfiguration": RetryPolicyConfigurationTypeDef,
    },
    total=False,
)

class StartJobRunRequestRequestTypeDef(
    _RequiredStartJobRunRequestRequestTypeDef, _OptionalStartJobRunRequestRequestTypeDef
):
    pass

_RequiredJobTemplateDataOutputTypeDef = TypedDict(
    "_RequiredJobTemplateDataOutputTypeDef",
    {
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": JobDriverOutputTypeDef,
    },
)
_OptionalJobTemplateDataOutputTypeDef = TypedDict(
    "_OptionalJobTemplateDataOutputTypeDef",
    {
        "configurationOverrides": ParametricConfigurationOverridesOutputTypeDef,
        "parameterConfiguration": Dict[str, TemplateParameterConfigurationOutputTypeDef],
        "jobTags": Dict[str, str],
    },
    total=False,
)

class JobTemplateDataOutputTypeDef(
    _RequiredJobTemplateDataOutputTypeDef, _OptionalJobTemplateDataOutputTypeDef
):
    pass

_RequiredJobTemplateDataTypeDef = TypedDict(
    "_RequiredJobTemplateDataTypeDef",
    {
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": JobDriverTypeDef,
    },
)
_OptionalJobTemplateDataTypeDef = TypedDict(
    "_OptionalJobTemplateDataTypeDef",
    {
        "configurationOverrides": ParametricConfigurationOverridesTypeDef,
        "parameterConfiguration": Mapping[str, TemplateParameterConfigurationTypeDef],
        "jobTags": Mapping[str, str],
    },
    total=False,
)

class JobTemplateDataTypeDef(_RequiredJobTemplateDataTypeDef, _OptionalJobTemplateDataTypeDef):
    pass

DescribeVirtualClusterResponseTypeDef = TypedDict(
    "DescribeVirtualClusterResponseTypeDef",
    {
        "virtualCluster": VirtualClusterTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualClustersResponseTypeDef = TypedDict(
    "ListVirtualClustersResponseTypeDef",
    {
        "virtualClusters": List[VirtualClusterTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeManagedEndpointResponseTypeDef = TypedDict(
    "DescribeManagedEndpointResponseTypeDef",
    {
        "endpoint": EndpointTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedEndpointsResponseTypeDef = TypedDict(
    "ListManagedEndpointsResponseTypeDef",
    {
        "endpoints": List[EndpointTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "jobRun": JobRunTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "jobRuns": List[JobRunTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredJobTemplateTypeDef = TypedDict(
    "_RequiredJobTemplateTypeDef",
    {
        "jobTemplateData": JobTemplateDataOutputTypeDef,
    },
)
_OptionalJobTemplateTypeDef = TypedDict(
    "_OptionalJobTemplateTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "tags": Dict[str, str],
        "kmsKeyArn": str,
        "decryptionError": str,
    },
    total=False,
)

class JobTemplateTypeDef(_RequiredJobTemplateTypeDef, _OptionalJobTemplateTypeDef):
    pass

_RequiredCreateJobTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobTemplateRequestRequestTypeDef",
    {
        "name": str,
        "clientToken": str,
        "jobTemplateData": JobTemplateDataTypeDef,
    },
)
_OptionalCreateJobTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobTemplateRequestRequestTypeDef",
    {
        "tags": Mapping[str, str],
        "kmsKeyArn": str,
    },
    total=False,
)

class CreateJobTemplateRequestRequestTypeDef(
    _RequiredCreateJobTemplateRequestRequestTypeDef, _OptionalCreateJobTemplateRequestRequestTypeDef
):
    pass

DescribeJobTemplateResponseTypeDef = TypedDict(
    "DescribeJobTemplateResponseTypeDef",
    {
        "jobTemplate": JobTemplateTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobTemplatesResponseTypeDef = TypedDict(
    "ListJobTemplatesResponseTypeDef",
    {
        "templates": List[JobTemplateTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
