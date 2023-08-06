"""
Type annotations for datasync service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datasync/type_defs/)

Usage::

    ```python
    from mypy_boto3_datasync.type_defs import CredentialsTypeDef

    data: CredentialsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AgentStatusType,
    AtimeType,
    AzureAccessTierType,
    DiscoveryJobStatusType,
    DiscoveryResourceTypeType,
    EfsInTransitEncryptionType,
    EndpointTypeType,
    GidType,
    HdfsAuthenticationTypeType,
    HdfsDataTransferProtectionType,
    HdfsRpcProtectionType,
    LocationFilterNameType,
    LogLevelType,
    MtimeType,
    NfsVersionType,
    ObjectStorageServerProtocolType,
    ObjectTagsType,
    OperatorType,
    OverwriteModeType,
    PhaseStatusType,
    PosixPermissionsType,
    PreserveDeletedFilesType,
    PreserveDevicesType,
    RecommendationStatusType,
    S3StorageClassType,
    SmbSecurityDescriptorCopyFlagsType,
    SmbVersionType,
    StorageSystemConnectivityStatusType,
    TaskExecutionStatusType,
    TaskFilterNameType,
    TaskQueueingType,
    TaskStatusType,
    TransferModeType,
    UidType,
    VerifyModeType,
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
    "CredentialsTypeDef",
    "DiscoveryServerConfigurationTypeDef",
    "TagListEntryTypeDef",
    "ResponseMetadataTypeDef",
    "AgentListEntryTypeDef",
    "AzureBlobSasConfigurationTypeDef",
    "CancelTaskExecutionRequestRequestTypeDef",
    "CapacityTypeDef",
    "Ec2ConfigTypeDef",
    "HdfsNameNodeTypeDef",
    "QopConfigurationTypeDef",
    "NfsMountOptionsTypeDef",
    "OnPremConfigTypeDef",
    "S3ConfigTypeDef",
    "SmbMountOptionsTypeDef",
    "FilterRuleTypeDef",
    "OptionsTypeDef",
    "TaskScheduleTypeDef",
    "DeleteAgentRequestRequestTypeDef",
    "DeleteLocationRequestRequestTypeDef",
    "DeleteTaskRequestRequestTypeDef",
    "DescribeAgentRequestRequestTypeDef",
    "PrivateLinkConfigTypeDef",
    "DescribeDiscoveryJobRequestRequestTypeDef",
    "DescribeLocationAzureBlobRequestRequestTypeDef",
    "DescribeLocationEfsRequestRequestTypeDef",
    "Ec2ConfigOutputTypeDef",
    "DescribeLocationFsxLustreRequestRequestTypeDef",
    "DescribeLocationFsxOntapRequestRequestTypeDef",
    "DescribeLocationFsxOpenZfsRequestRequestTypeDef",
    "DescribeLocationFsxWindowsRequestRequestTypeDef",
    "DescribeLocationHdfsRequestRequestTypeDef",
    "HdfsNameNodeOutputTypeDef",
    "QopConfigurationOutputTypeDef",
    "DescribeLocationNfsRequestRequestTypeDef",
    "NfsMountOptionsOutputTypeDef",
    "OnPremConfigOutputTypeDef",
    "DescribeLocationObjectStorageRequestRequestTypeDef",
    "DescribeLocationS3RequestRequestTypeDef",
    "S3ConfigOutputTypeDef",
    "DescribeLocationSmbRequestRequestTypeDef",
    "SmbMountOptionsOutputTypeDef",
    "DescribeStorageSystemRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeStorageSystemResourceMetricsRequestRequestTypeDef",
    "DescribeStorageSystemResourcesRequestRequestTypeDef",
    "DiscoveryServerConfigurationOutputTypeDef",
    "DescribeTaskExecutionRequestRequestTypeDef",
    "FilterRuleOutputTypeDef",
    "OptionsOutputTypeDef",
    "TaskExecutionResultDetailTypeDef",
    "DescribeTaskRequestRequestTypeDef",
    "TaskScheduleOutputTypeDef",
    "DiscoveryJobListEntryTypeDef",
    "GenerateRecommendationsRequestRequestTypeDef",
    "IOPSTypeDef",
    "LatencyTypeDef",
    "ListAgentsRequestRequestTypeDef",
    "ListDiscoveryJobsRequestRequestTypeDef",
    "LocationFilterTypeDef",
    "LocationListEntryTypeDef",
    "ListStorageSystemsRequestRequestTypeDef",
    "StorageSystemListEntryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagListEntryOutputTypeDef",
    "ListTaskExecutionsRequestRequestTypeDef",
    "TaskExecutionListEntryTypeDef",
    "TaskFilterTypeDef",
    "TaskListEntryTypeDef",
    "MaxP95PerformanceTypeDef",
    "RecommendationTypeDef",
    "ThroughputTypeDef",
    "RemoveStorageSystemRequestRequestTypeDef",
    "StopDiscoveryJobRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentRequestRequestTypeDef",
    "UpdateDiscoveryJobRequestRequestTypeDef",
    "UpdateLocationObjectStorageRequestRequestTypeDef",
    "UpdateStorageSystemRequestRequestTypeDef",
    "AddStorageSystemRequestRequestTypeDef",
    "CreateAgentRequestRequestTypeDef",
    "CreateLocationFsxLustreRequestRequestTypeDef",
    "CreateLocationFsxWindowsRequestRequestTypeDef",
    "CreateLocationObjectStorageRequestRequestTypeDef",
    "StartDiscoveryJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "AddStorageSystemResponseTypeDef",
    "CreateAgentResponseTypeDef",
    "CreateLocationAzureBlobResponseTypeDef",
    "CreateLocationEfsResponseTypeDef",
    "CreateLocationFsxLustreResponseTypeDef",
    "CreateLocationFsxOntapResponseTypeDef",
    "CreateLocationFsxOpenZfsResponseTypeDef",
    "CreateLocationFsxWindowsResponseTypeDef",
    "CreateLocationHdfsResponseTypeDef",
    "CreateLocationNfsResponseTypeDef",
    "CreateLocationObjectStorageResponseTypeDef",
    "CreateLocationS3ResponseTypeDef",
    "CreateLocationSmbResponseTypeDef",
    "CreateTaskResponseTypeDef",
    "DescribeDiscoveryJobResponseTypeDef",
    "DescribeLocationAzureBlobResponseTypeDef",
    "DescribeLocationFsxLustreResponseTypeDef",
    "DescribeLocationFsxWindowsResponseTypeDef",
    "DescribeLocationObjectStorageResponseTypeDef",
    "StartDiscoveryJobResponseTypeDef",
    "StartTaskExecutionResponseTypeDef",
    "ListAgentsResponseTypeDef",
    "CreateLocationAzureBlobRequestRequestTypeDef",
    "UpdateLocationAzureBlobRequestRequestTypeDef",
    "CreateLocationEfsRequestRequestTypeDef",
    "CreateLocationHdfsRequestRequestTypeDef",
    "UpdateLocationHdfsRequestRequestTypeDef",
    "FsxProtocolNfsTypeDef",
    "CreateLocationNfsRequestRequestTypeDef",
    "UpdateLocationNfsRequestRequestTypeDef",
    "CreateLocationS3RequestRequestTypeDef",
    "CreateLocationSmbRequestRequestTypeDef",
    "FsxProtocolSmbTypeDef",
    "UpdateLocationSmbRequestRequestTypeDef",
    "StartTaskExecutionRequestRequestTypeDef",
    "UpdateTaskExecutionRequestRequestTypeDef",
    "CreateTaskRequestRequestTypeDef",
    "UpdateTaskRequestRequestTypeDef",
    "DescribeAgentResponseTypeDef",
    "DescribeLocationEfsResponseTypeDef",
    "DescribeLocationHdfsResponseTypeDef",
    "FsxProtocolNfsOutputTypeDef",
    "DescribeLocationNfsResponseTypeDef",
    "DescribeLocationS3ResponseTypeDef",
    "DescribeLocationSmbResponseTypeDef",
    "FsxProtocolSmbOutputTypeDef",
    "DescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef",
    "ListAgentsRequestListAgentsPaginateTypeDef",
    "ListDiscoveryJobsRequestListDiscoveryJobsPaginateTypeDef",
    "ListStorageSystemsRequestListStorageSystemsPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTaskExecutionsRequestListTaskExecutionsPaginateTypeDef",
    "DescribeStorageSystemResponseTypeDef",
    "DescribeTaskExecutionResponseTypeDef",
    "DescribeTaskResponseTypeDef",
    "ListDiscoveryJobsResponseTypeDef",
    "ListLocationsRequestListLocationsPaginateTypeDef",
    "ListLocationsRequestRequestTypeDef",
    "ListLocationsResponseTypeDef",
    "ListStorageSystemsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskExecutionsResponseTypeDef",
    "ListTasksRequestListTasksPaginateTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListTasksResponseTypeDef",
    "NetAppONTAPClusterTypeDef",
    "NetAppONTAPSVMTypeDef",
    "NetAppONTAPVolumeTypeDef",
    "P95MetricsTypeDef",
    "FsxProtocolTypeDef",
    "FsxProtocolOutputTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceMetricsTypeDef",
    "CreateLocationFsxOntapRequestRequestTypeDef",
    "CreateLocationFsxOpenZfsRequestRequestTypeDef",
    "DescribeLocationFsxOntapResponseTypeDef",
    "DescribeLocationFsxOpenZfsResponseTypeDef",
    "DescribeStorageSystemResourcesResponseTypeDef",
    "DescribeStorageSystemResourceMetricsResponseTypeDef",
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

_RequiredDiscoveryServerConfigurationTypeDef = TypedDict(
    "_RequiredDiscoveryServerConfigurationTypeDef",
    {
        "ServerHostname": str,
    },
)
_OptionalDiscoveryServerConfigurationTypeDef = TypedDict(
    "_OptionalDiscoveryServerConfigurationTypeDef",
    {
        "ServerPort": int,
    },
    total=False,
)

class DiscoveryServerConfigurationTypeDef(
    _RequiredDiscoveryServerConfigurationTypeDef, _OptionalDiscoveryServerConfigurationTypeDef
):
    pass

_RequiredTagListEntryTypeDef = TypedDict(
    "_RequiredTagListEntryTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagListEntryTypeDef = TypedDict(
    "_OptionalTagListEntryTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagListEntryTypeDef(_RequiredTagListEntryTypeDef, _OptionalTagListEntryTypeDef):
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

AgentListEntryTypeDef = TypedDict(
    "AgentListEntryTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatusType,
    },
)

AzureBlobSasConfigurationTypeDef = TypedDict(
    "AzureBlobSasConfigurationTypeDef",
    {
        "Token": str,
    },
)

CancelTaskExecutionRequestRequestTypeDef = TypedDict(
    "CancelTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "Used": int,
        "Provisioned": int,
        "LogicalUsed": int,
    },
)

Ec2ConfigTypeDef = TypedDict(
    "Ec2ConfigTypeDef",
    {
        "SubnetArn": str,
        "SecurityGroupArns": Sequence[str],
    },
)

HdfsNameNodeTypeDef = TypedDict(
    "HdfsNameNodeTypeDef",
    {
        "Hostname": str,
        "Port": int,
    },
)

QopConfigurationTypeDef = TypedDict(
    "QopConfigurationTypeDef",
    {
        "RpcProtection": HdfsRpcProtectionType,
        "DataTransferProtection": HdfsDataTransferProtectionType,
    },
    total=False,
)

NfsMountOptionsTypeDef = TypedDict(
    "NfsMountOptionsTypeDef",
    {
        "Version": NfsVersionType,
    },
    total=False,
)

OnPremConfigTypeDef = TypedDict(
    "OnPremConfigTypeDef",
    {
        "AgentArns": Sequence[str],
    },
)

S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "BucketAccessRoleArn": str,
    },
)

SmbMountOptionsTypeDef = TypedDict(
    "SmbMountOptionsTypeDef",
    {
        "Version": SmbVersionType,
    },
    total=False,
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef",
    {
        "FilterType": Literal["SIMPLE_PATTERN"],
        "Value": str,
    },
    total=False,
)

OptionsTypeDef = TypedDict(
    "OptionsTypeDef",
    {
        "VerifyMode": VerifyModeType,
        "OverwriteMode": OverwriteModeType,
        "Atime": AtimeType,
        "Mtime": MtimeType,
        "Uid": UidType,
        "Gid": GidType,
        "PreserveDeletedFiles": PreserveDeletedFilesType,
        "PreserveDevices": PreserveDevicesType,
        "PosixPermissions": PosixPermissionsType,
        "BytesPerSecond": int,
        "TaskQueueing": TaskQueueingType,
        "LogLevel": LogLevelType,
        "TransferMode": TransferModeType,
        "SecurityDescriptorCopyFlags": SmbSecurityDescriptorCopyFlagsType,
        "ObjectTags": ObjectTagsType,
    },
    total=False,
)

TaskScheduleTypeDef = TypedDict(
    "TaskScheduleTypeDef",
    {
        "ScheduleExpression": str,
    },
)

DeleteAgentRequestRequestTypeDef = TypedDict(
    "DeleteAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
    },
)

DeleteLocationRequestRequestTypeDef = TypedDict(
    "DeleteLocationRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DeleteTaskRequestRequestTypeDef = TypedDict(
    "DeleteTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)

DescribeAgentRequestRequestTypeDef = TypedDict(
    "DescribeAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
    },
)

PrivateLinkConfigTypeDef = TypedDict(
    "PrivateLinkConfigTypeDef",
    {
        "VpcEndpointId": str,
        "PrivateLinkEndpoint": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
    },
)

DescribeDiscoveryJobRequestRequestTypeDef = TypedDict(
    "DescribeDiscoveryJobRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
    },
)

DescribeLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "DescribeLocationAzureBlobRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationEfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationEfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

Ec2ConfigOutputTypeDef = TypedDict(
    "Ec2ConfigOutputTypeDef",
    {
        "SubnetArn": str,
        "SecurityGroupArns": List[str],
    },
)

DescribeLocationFsxLustreRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxLustreRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxOntapRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxOntapRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxOpenZfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxOpenZfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxWindowsRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxWindowsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationHdfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationHdfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

HdfsNameNodeOutputTypeDef = TypedDict(
    "HdfsNameNodeOutputTypeDef",
    {
        "Hostname": str,
        "Port": int,
    },
)

QopConfigurationOutputTypeDef = TypedDict(
    "QopConfigurationOutputTypeDef",
    {
        "RpcProtection": HdfsRpcProtectionType,
        "DataTransferProtection": HdfsDataTransferProtectionType,
    },
)

DescribeLocationNfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationNfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

NfsMountOptionsOutputTypeDef = TypedDict(
    "NfsMountOptionsOutputTypeDef",
    {
        "Version": NfsVersionType,
    },
)

OnPremConfigOutputTypeDef = TypedDict(
    "OnPremConfigOutputTypeDef",
    {
        "AgentArns": List[str],
    },
)

DescribeLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "DescribeLocationObjectStorageRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationS3RequestRequestTypeDef = TypedDict(
    "DescribeLocationS3RequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

S3ConfigOutputTypeDef = TypedDict(
    "S3ConfigOutputTypeDef",
    {
        "BucketAccessRoleArn": str,
    },
)

DescribeLocationSmbRequestRequestTypeDef = TypedDict(
    "DescribeLocationSmbRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

SmbMountOptionsOutputTypeDef = TypedDict(
    "SmbMountOptionsOutputTypeDef",
    {
        "Version": SmbVersionType,
    },
)

DescribeStorageSystemRequestRequestTypeDef = TypedDict(
    "DescribeStorageSystemRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
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

_RequiredDescribeStorageSystemResourceMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeStorageSystemResourceMetricsRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResourceType": DiscoveryResourceTypeType,
        "ResourceId": str,
    },
)
_OptionalDescribeStorageSystemResourceMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeStorageSystemResourceMetricsRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeStorageSystemResourceMetricsRequestRequestTypeDef(
    _RequiredDescribeStorageSystemResourceMetricsRequestRequestTypeDef,
    _OptionalDescribeStorageSystemResourceMetricsRequestRequestTypeDef,
):
    pass

_RequiredDescribeStorageSystemResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeStorageSystemResourcesRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResourceType": DiscoveryResourceTypeType,
    },
)
_OptionalDescribeStorageSystemResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeStorageSystemResourcesRequestRequestTypeDef",
    {
        "ResourceIds": Sequence[str],
        "Filter": Mapping[Literal["SVM"], Sequence[str]],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeStorageSystemResourcesRequestRequestTypeDef(
    _RequiredDescribeStorageSystemResourcesRequestRequestTypeDef,
    _OptionalDescribeStorageSystemResourcesRequestRequestTypeDef,
):
    pass

DiscoveryServerConfigurationOutputTypeDef = TypedDict(
    "DiscoveryServerConfigurationOutputTypeDef",
    {
        "ServerHostname": str,
        "ServerPort": int,
    },
)

DescribeTaskExecutionRequestRequestTypeDef = TypedDict(
    "DescribeTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

FilterRuleOutputTypeDef = TypedDict(
    "FilterRuleOutputTypeDef",
    {
        "FilterType": Literal["SIMPLE_PATTERN"],
        "Value": str,
    },
)

OptionsOutputTypeDef = TypedDict(
    "OptionsOutputTypeDef",
    {
        "VerifyMode": VerifyModeType,
        "OverwriteMode": OverwriteModeType,
        "Atime": AtimeType,
        "Mtime": MtimeType,
        "Uid": UidType,
        "Gid": GidType,
        "PreserveDeletedFiles": PreserveDeletedFilesType,
        "PreserveDevices": PreserveDevicesType,
        "PosixPermissions": PosixPermissionsType,
        "BytesPerSecond": int,
        "TaskQueueing": TaskQueueingType,
        "LogLevel": LogLevelType,
        "TransferMode": TransferModeType,
        "SecurityDescriptorCopyFlags": SmbSecurityDescriptorCopyFlagsType,
        "ObjectTags": ObjectTagsType,
    },
)

TaskExecutionResultDetailTypeDef = TypedDict(
    "TaskExecutionResultDetailTypeDef",
    {
        "PrepareDuration": int,
        "PrepareStatus": PhaseStatusType,
        "TotalDuration": int,
        "TransferDuration": int,
        "TransferStatus": PhaseStatusType,
        "VerifyDuration": int,
        "VerifyStatus": PhaseStatusType,
        "ErrorCode": str,
        "ErrorDetail": str,
    },
)

DescribeTaskRequestRequestTypeDef = TypedDict(
    "DescribeTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)

TaskScheduleOutputTypeDef = TypedDict(
    "TaskScheduleOutputTypeDef",
    {
        "ScheduleExpression": str,
    },
)

DiscoveryJobListEntryTypeDef = TypedDict(
    "DiscoveryJobListEntryTypeDef",
    {
        "DiscoveryJobArn": str,
        "Status": DiscoveryJobStatusType,
    },
)

GenerateRecommendationsRequestRequestTypeDef = TypedDict(
    "GenerateRecommendationsRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResourceIds": Sequence[str],
        "ResourceType": DiscoveryResourceTypeType,
    },
)

IOPSTypeDef = TypedDict(
    "IOPSTypeDef",
    {
        "Read": float,
        "Write": float,
        "Other": float,
        "Total": float,
    },
)

LatencyTypeDef = TypedDict(
    "LatencyTypeDef",
    {
        "Read": float,
        "Write": float,
        "Other": float,
    },
)

ListAgentsRequestRequestTypeDef = TypedDict(
    "ListAgentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDiscoveryJobsRequestRequestTypeDef = TypedDict(
    "ListDiscoveryJobsRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

LocationFilterTypeDef = TypedDict(
    "LocationFilterTypeDef",
    {
        "Name": LocationFilterNameType,
        "Values": Sequence[str],
        "Operator": OperatorType,
    },
)

LocationListEntryTypeDef = TypedDict(
    "LocationListEntryTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
    },
)

ListStorageSystemsRequestRequestTypeDef = TypedDict(
    "ListStorageSystemsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

StorageSystemListEntryTypeDef = TypedDict(
    "StorageSystemListEntryTypeDef",
    {
        "StorageSystemArn": str,
        "Name": str,
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

TagListEntryOutputTypeDef = TypedDict(
    "TagListEntryOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

ListTaskExecutionsRequestRequestTypeDef = TypedDict(
    "ListTaskExecutionsRequestRequestTypeDef",
    {
        "TaskArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

TaskExecutionListEntryTypeDef = TypedDict(
    "TaskExecutionListEntryTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": TaskExecutionStatusType,
    },
)

TaskFilterTypeDef = TypedDict(
    "TaskFilterTypeDef",
    {
        "Name": TaskFilterNameType,
        "Values": Sequence[str],
        "Operator": OperatorType,
    },
)

TaskListEntryTypeDef = TypedDict(
    "TaskListEntryTypeDef",
    {
        "TaskArn": str,
        "Status": TaskStatusType,
        "Name": str,
    },
)

MaxP95PerformanceTypeDef = TypedDict(
    "MaxP95PerformanceTypeDef",
    {
        "IopsRead": float,
        "IopsWrite": float,
        "IopsOther": float,
        "IopsTotal": float,
        "ThroughputRead": float,
        "ThroughputWrite": float,
        "ThroughputOther": float,
        "ThroughputTotal": float,
        "LatencyRead": float,
        "LatencyWrite": float,
        "LatencyOther": float,
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "StorageType": str,
        "StorageConfiguration": Dict[str, str],
        "EstimatedMonthlyStorageCost": str,
    },
)

ThroughputTypeDef = TypedDict(
    "ThroughputTypeDef",
    {
        "Read": float,
        "Write": float,
        "Other": float,
        "Total": float,
    },
)

RemoveStorageSystemRequestRequestTypeDef = TypedDict(
    "RemoveStorageSystemRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
    },
)

StopDiscoveryJobRequestRequestTypeDef = TypedDict(
    "StopDiscoveryJobRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Keys": Sequence[str],
    },
)

_RequiredUpdateAgentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
    },
)
_OptionalUpdateAgentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateAgentRequestRequestTypeDef(
    _RequiredUpdateAgentRequestRequestTypeDef, _OptionalUpdateAgentRequestRequestTypeDef
):
    pass

UpdateDiscoveryJobRequestRequestTypeDef = TypedDict(
    "UpdateDiscoveryJobRequestRequestTypeDef",
    {
        "DiscoveryJobArn": str,
        "CollectionDurationMinutes": int,
    },
)

_RequiredUpdateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationObjectStorageRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationObjectStorageRequestRequestTypeDef",
    {
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "Subdirectory": str,
        "AccessKey": str,
        "SecretKey": str,
        "AgentArns": Sequence[str],
        "ServerCertificate": Union[str, bytes, IO[Any], StreamingBody],
    },
    total=False,
)

class UpdateLocationObjectStorageRequestRequestTypeDef(
    _RequiredUpdateLocationObjectStorageRequestRequestTypeDef,
    _OptionalUpdateLocationObjectStorageRequestRequestTypeDef,
):
    pass

_RequiredUpdateStorageSystemRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStorageSystemRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
    },
)
_OptionalUpdateStorageSystemRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStorageSystemRequestRequestTypeDef",
    {
        "ServerConfiguration": DiscoveryServerConfigurationTypeDef,
        "AgentArns": Sequence[str],
        "Name": str,
        "CloudWatchLogGroupArn": str,
        "Credentials": CredentialsTypeDef,
    },
    total=False,
)

class UpdateStorageSystemRequestRequestTypeDef(
    _RequiredUpdateStorageSystemRequestRequestTypeDef,
    _OptionalUpdateStorageSystemRequestRequestTypeDef,
):
    pass

_RequiredAddStorageSystemRequestRequestTypeDef = TypedDict(
    "_RequiredAddStorageSystemRequestRequestTypeDef",
    {
        "ServerConfiguration": DiscoveryServerConfigurationTypeDef,
        "SystemType": Literal["NetAppONTAP"],
        "AgentArns": Sequence[str],
        "ClientToken": str,
        "Credentials": CredentialsTypeDef,
    },
)
_OptionalAddStorageSystemRequestRequestTypeDef = TypedDict(
    "_OptionalAddStorageSystemRequestRequestTypeDef",
    {
        "CloudWatchLogGroupArn": str,
        "Tags": Sequence[TagListEntryTypeDef],
        "Name": str,
    },
    total=False,
)

class AddStorageSystemRequestRequestTypeDef(
    _RequiredAddStorageSystemRequestRequestTypeDef, _OptionalAddStorageSystemRequestRequestTypeDef
):
    pass

_RequiredCreateAgentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAgentRequestRequestTypeDef",
    {
        "ActivationKey": str,
    },
)
_OptionalCreateAgentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAgentRequestRequestTypeDef",
    {
        "AgentName": str,
        "Tags": Sequence[TagListEntryTypeDef],
        "VpcEndpointId": str,
        "SubnetArns": Sequence[str],
        "SecurityGroupArns": Sequence[str],
    },
    total=False,
)

class CreateAgentRequestRequestTypeDef(
    _RequiredCreateAgentRequestRequestTypeDef, _OptionalCreateAgentRequestRequestTypeDef
):
    pass

_RequiredCreateLocationFsxLustreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxLustreRequestRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "SecurityGroupArns": Sequence[str],
    },
)
_OptionalCreateLocationFsxLustreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxLustreRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class CreateLocationFsxLustreRequestRequestTypeDef(
    _RequiredCreateLocationFsxLustreRequestRequestTypeDef,
    _OptionalCreateLocationFsxLustreRequestRequestTypeDef,
):
    pass

_RequiredCreateLocationFsxWindowsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxWindowsRequestRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "SecurityGroupArns": Sequence[str],
        "User": str,
        "Password": str,
    },
)
_OptionalCreateLocationFsxWindowsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxWindowsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": Sequence[TagListEntryTypeDef],
        "Domain": str,
    },
    total=False,
)

class CreateLocationFsxWindowsRequestRequestTypeDef(
    _RequiredCreateLocationFsxWindowsRequestRequestTypeDef,
    _OptionalCreateLocationFsxWindowsRequestRequestTypeDef,
):
    pass

_RequiredCreateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationObjectStorageRequestRequestTypeDef",
    {
        "ServerHostname": str,
        "BucketName": str,
        "AgentArns": Sequence[str],
    },
)
_OptionalCreateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationObjectStorageRequestRequestTypeDef",
    {
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "Subdirectory": str,
        "AccessKey": str,
        "SecretKey": str,
        "Tags": Sequence[TagListEntryTypeDef],
        "ServerCertificate": Union[str, bytes, IO[Any], StreamingBody],
    },
    total=False,
)

class CreateLocationObjectStorageRequestRequestTypeDef(
    _RequiredCreateLocationObjectStorageRequestRequestTypeDef,
    _OptionalCreateLocationObjectStorageRequestRequestTypeDef,
):
    pass

_RequiredStartDiscoveryJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartDiscoveryJobRequestRequestTypeDef",
    {
        "StorageSystemArn": str,
        "CollectionDurationMinutes": int,
        "ClientToken": str,
    },
)
_OptionalStartDiscoveryJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartDiscoveryJobRequestRequestTypeDef",
    {
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class StartDiscoveryJobRequestRequestTypeDef(
    _RequiredStartDiscoveryJobRequestRequestTypeDef, _OptionalStartDiscoveryJobRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagListEntryTypeDef],
    },
)

AddStorageSystemResponseTypeDef = TypedDict(
    "AddStorageSystemResponseTypeDef",
    {
        "StorageSystemArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAgentResponseTypeDef = TypedDict(
    "CreateAgentResponseTypeDef",
    {
        "AgentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationAzureBlobResponseTypeDef = TypedDict(
    "CreateLocationAzureBlobResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationEfsResponseTypeDef = TypedDict(
    "CreateLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationFsxLustreResponseTypeDef = TypedDict(
    "CreateLocationFsxLustreResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationFsxOntapResponseTypeDef = TypedDict(
    "CreateLocationFsxOntapResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationFsxOpenZfsResponseTypeDef = TypedDict(
    "CreateLocationFsxOpenZfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationFsxWindowsResponseTypeDef = TypedDict(
    "CreateLocationFsxWindowsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationHdfsResponseTypeDef = TypedDict(
    "CreateLocationHdfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationNfsResponseTypeDef = TypedDict(
    "CreateLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationObjectStorageResponseTypeDef = TypedDict(
    "CreateLocationObjectStorageResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationS3ResponseTypeDef = TypedDict(
    "CreateLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLocationSmbResponseTypeDef = TypedDict(
    "CreateLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTaskResponseTypeDef = TypedDict(
    "CreateTaskResponseTypeDef",
    {
        "TaskArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDiscoveryJobResponseTypeDef = TypedDict(
    "DescribeDiscoveryJobResponseTypeDef",
    {
        "StorageSystemArn": str,
        "DiscoveryJobArn": str,
        "CollectionDurationMinutes": int,
        "Status": DiscoveryJobStatusType,
        "JobStartTime": datetime,
        "JobEndTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationAzureBlobResponseTypeDef = TypedDict(
    "DescribeLocationAzureBlobResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AuthenticationType": Literal["SAS"],
        "BlobType": Literal["BLOCK"],
        "AccessTier": AzureAccessTierType,
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationFsxLustreResponseTypeDef = TypedDict(
    "DescribeLocationFsxLustreResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationFsxWindowsResponseTypeDef = TypedDict(
    "DescribeLocationFsxWindowsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "User": str,
        "Domain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationObjectStorageResponseTypeDef = TypedDict(
    "DescribeLocationObjectStorageResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AccessKey": str,
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ServerCertificate": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartDiscoveryJobResponseTypeDef = TypedDict(
    "StartDiscoveryJobResponseTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartTaskExecutionResponseTypeDef = TypedDict(
    "StartTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAgentsResponseTypeDef = TypedDict(
    "ListAgentsResponseTypeDef",
    {
        "Agents": List[AgentListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationAzureBlobRequestRequestTypeDef",
    {
        "ContainerUrl": str,
        "AuthenticationType": Literal["SAS"],
        "AgentArns": Sequence[str],
    },
)
_OptionalCreateLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationAzureBlobRequestRequestTypeDef",
    {
        "SasConfiguration": AzureBlobSasConfigurationTypeDef,
        "BlobType": Literal["BLOCK"],
        "AccessTier": AzureAccessTierType,
        "Subdirectory": str,
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class CreateLocationAzureBlobRequestRequestTypeDef(
    _RequiredCreateLocationAzureBlobRequestRequestTypeDef,
    _OptionalCreateLocationAzureBlobRequestRequestTypeDef,
):
    pass

_RequiredUpdateLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationAzureBlobRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationAzureBlobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationAzureBlobRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "AuthenticationType": Literal["SAS"],
        "SasConfiguration": AzureBlobSasConfigurationTypeDef,
        "BlobType": Literal["BLOCK"],
        "AccessTier": AzureAccessTierType,
        "AgentArns": Sequence[str],
    },
    total=False,
)

class UpdateLocationAzureBlobRequestRequestTypeDef(
    _RequiredUpdateLocationAzureBlobRequestRequestTypeDef,
    _OptionalUpdateLocationAzureBlobRequestRequestTypeDef,
):
    pass

_RequiredCreateLocationEfsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationEfsRequestRequestTypeDef",
    {
        "EfsFilesystemArn": str,
        "Ec2Config": Ec2ConfigTypeDef,
    },
)
_OptionalCreateLocationEfsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationEfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": Sequence[TagListEntryTypeDef],
        "AccessPointArn": str,
        "FileSystemAccessRoleArn": str,
        "InTransitEncryption": EfsInTransitEncryptionType,
    },
    total=False,
)

class CreateLocationEfsRequestRequestTypeDef(
    _RequiredCreateLocationEfsRequestRequestTypeDef, _OptionalCreateLocationEfsRequestRequestTypeDef
):
    pass

_RequiredCreateLocationHdfsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationHdfsRequestRequestTypeDef",
    {
        "NameNodes": Sequence[HdfsNameNodeTypeDef],
        "AuthenticationType": HdfsAuthenticationTypeType,
        "AgentArns": Sequence[str],
    },
)
_OptionalCreateLocationHdfsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationHdfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "BlockSize": int,
        "ReplicationFactor": int,
        "KmsKeyProviderUri": str,
        "QopConfiguration": QopConfigurationTypeDef,
        "SimpleUser": str,
        "KerberosPrincipal": str,
        "KerberosKeytab": Union[str, bytes, IO[Any], StreamingBody],
        "KerberosKrb5Conf": Union[str, bytes, IO[Any], StreamingBody],
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class CreateLocationHdfsRequestRequestTypeDef(
    _RequiredCreateLocationHdfsRequestRequestTypeDef,
    _OptionalCreateLocationHdfsRequestRequestTypeDef,
):
    pass

_RequiredUpdateLocationHdfsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationHdfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationHdfsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationHdfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "NameNodes": Sequence[HdfsNameNodeTypeDef],
        "BlockSize": int,
        "ReplicationFactor": int,
        "KmsKeyProviderUri": str,
        "QopConfiguration": QopConfigurationTypeDef,
        "AuthenticationType": HdfsAuthenticationTypeType,
        "SimpleUser": str,
        "KerberosPrincipal": str,
        "KerberosKeytab": Union[str, bytes, IO[Any], StreamingBody],
        "KerberosKrb5Conf": Union[str, bytes, IO[Any], StreamingBody],
        "AgentArns": Sequence[str],
    },
    total=False,
)

class UpdateLocationHdfsRequestRequestTypeDef(
    _RequiredUpdateLocationHdfsRequestRequestTypeDef,
    _OptionalUpdateLocationHdfsRequestRequestTypeDef,
):
    pass

FsxProtocolNfsTypeDef = TypedDict(
    "FsxProtocolNfsTypeDef",
    {
        "MountOptions": NfsMountOptionsTypeDef,
    },
    total=False,
)

_RequiredCreateLocationNfsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationNfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "ServerHostname": str,
        "OnPremConfig": OnPremConfigTypeDef,
    },
)
_OptionalCreateLocationNfsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationNfsRequestRequestTypeDef",
    {
        "MountOptions": NfsMountOptionsTypeDef,
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class CreateLocationNfsRequestRequestTypeDef(
    _RequiredCreateLocationNfsRequestRequestTypeDef, _OptionalCreateLocationNfsRequestRequestTypeDef
):
    pass

_RequiredUpdateLocationNfsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationNfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationNfsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationNfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "OnPremConfig": OnPremConfigTypeDef,
        "MountOptions": NfsMountOptionsTypeDef,
    },
    total=False,
)

class UpdateLocationNfsRequestRequestTypeDef(
    _RequiredUpdateLocationNfsRequestRequestTypeDef, _OptionalUpdateLocationNfsRequestRequestTypeDef
):
    pass

_RequiredCreateLocationS3RequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationS3RequestRequestTypeDef",
    {
        "S3BucketArn": str,
        "S3Config": S3ConfigTypeDef,
    },
)
_OptionalCreateLocationS3RequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationS3RequestRequestTypeDef",
    {
        "Subdirectory": str,
        "S3StorageClass": S3StorageClassType,
        "AgentArns": Sequence[str],
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class CreateLocationS3RequestRequestTypeDef(
    _RequiredCreateLocationS3RequestRequestTypeDef, _OptionalCreateLocationS3RequestRequestTypeDef
):
    pass

_RequiredCreateLocationSmbRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationSmbRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "ServerHostname": str,
        "User": str,
        "Password": str,
        "AgentArns": Sequence[str],
    },
)
_OptionalCreateLocationSmbRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationSmbRequestRequestTypeDef",
    {
        "Domain": str,
        "MountOptions": SmbMountOptionsTypeDef,
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class CreateLocationSmbRequestRequestTypeDef(
    _RequiredCreateLocationSmbRequestRequestTypeDef, _OptionalCreateLocationSmbRequestRequestTypeDef
):
    pass

_RequiredFsxProtocolSmbTypeDef = TypedDict(
    "_RequiredFsxProtocolSmbTypeDef",
    {
        "Password": str,
        "User": str,
    },
)
_OptionalFsxProtocolSmbTypeDef = TypedDict(
    "_OptionalFsxProtocolSmbTypeDef",
    {
        "Domain": str,
        "MountOptions": SmbMountOptionsTypeDef,
    },
    total=False,
)

class FsxProtocolSmbTypeDef(_RequiredFsxProtocolSmbTypeDef, _OptionalFsxProtocolSmbTypeDef):
    pass

_RequiredUpdateLocationSmbRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationSmbRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationSmbRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationSmbRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "User": str,
        "Domain": str,
        "Password": str,
        "AgentArns": Sequence[str],
        "MountOptions": SmbMountOptionsTypeDef,
    },
    total=False,
)

class UpdateLocationSmbRequestRequestTypeDef(
    _RequiredUpdateLocationSmbRequestRequestTypeDef, _OptionalUpdateLocationSmbRequestRequestTypeDef
):
    pass

_RequiredStartTaskExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartTaskExecutionRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)
_OptionalStartTaskExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartTaskExecutionRequestRequestTypeDef",
    {
        "OverrideOptions": OptionsTypeDef,
        "Includes": Sequence[FilterRuleTypeDef],
        "Excludes": Sequence[FilterRuleTypeDef],
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class StartTaskExecutionRequestRequestTypeDef(
    _RequiredStartTaskExecutionRequestRequestTypeDef,
    _OptionalStartTaskExecutionRequestRequestTypeDef,
):
    pass

UpdateTaskExecutionRequestRequestTypeDef = TypedDict(
    "UpdateTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
        "Options": OptionsTypeDef,
    },
)

_RequiredCreateTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTaskRequestRequestTypeDef",
    {
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
    },
)
_OptionalCreateTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTaskRequestRequestTypeDef",
    {
        "CloudWatchLogGroupArn": str,
        "Name": str,
        "Options": OptionsTypeDef,
        "Excludes": Sequence[FilterRuleTypeDef],
        "Schedule": TaskScheduleTypeDef,
        "Tags": Sequence[TagListEntryTypeDef],
        "Includes": Sequence[FilterRuleTypeDef],
    },
    total=False,
)

class CreateTaskRequestRequestTypeDef(
    _RequiredCreateTaskRequestRequestTypeDef, _OptionalCreateTaskRequestRequestTypeDef
):
    pass

_RequiredUpdateTaskRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)
_OptionalUpdateTaskRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTaskRequestRequestTypeDef",
    {
        "Options": OptionsTypeDef,
        "Excludes": Sequence[FilterRuleTypeDef],
        "Schedule": TaskScheduleTypeDef,
        "Name": str,
        "CloudWatchLogGroupArn": str,
        "Includes": Sequence[FilterRuleTypeDef],
    },
    total=False,
)

class UpdateTaskRequestRequestTypeDef(
    _RequiredUpdateTaskRequestRequestTypeDef, _OptionalUpdateTaskRequestRequestTypeDef
):
    pass

DescribeAgentResponseTypeDef = TypedDict(
    "DescribeAgentResponseTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatusType,
        "LastConnectionTime": datetime,
        "CreationTime": datetime,
        "EndpointType": EndpointTypeType,
        "PrivateLinkConfig": PrivateLinkConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationEfsResponseTypeDef = TypedDict(
    "DescribeLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "Ec2Config": Ec2ConfigOutputTypeDef,
        "CreationTime": datetime,
        "AccessPointArn": str,
        "FileSystemAccessRoleArn": str,
        "InTransitEncryption": EfsInTransitEncryptionType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationHdfsResponseTypeDef = TypedDict(
    "DescribeLocationHdfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "NameNodes": List[HdfsNameNodeOutputTypeDef],
        "BlockSize": int,
        "ReplicationFactor": int,
        "KmsKeyProviderUri": str,
        "QopConfiguration": QopConfigurationOutputTypeDef,
        "AuthenticationType": HdfsAuthenticationTypeType,
        "SimpleUser": str,
        "KerberosPrincipal": str,
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FsxProtocolNfsOutputTypeDef = TypedDict(
    "FsxProtocolNfsOutputTypeDef",
    {
        "MountOptions": NfsMountOptionsOutputTypeDef,
    },
)

DescribeLocationNfsResponseTypeDef = TypedDict(
    "DescribeLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "OnPremConfig": OnPremConfigOutputTypeDef,
        "MountOptions": NfsMountOptionsOutputTypeDef,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationS3ResponseTypeDef = TypedDict(
    "DescribeLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "S3StorageClass": S3StorageClassType,
        "S3Config": S3ConfigOutputTypeDef,
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationSmbResponseTypeDef = TypedDict(
    "DescribeLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AgentArns": List[str],
        "User": str,
        "Domain": str,
        "MountOptions": SmbMountOptionsOutputTypeDef,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FsxProtocolSmbOutputTypeDef = TypedDict(
    "FsxProtocolSmbOutputTypeDef",
    {
        "Domain": str,
        "MountOptions": SmbMountOptionsOutputTypeDef,
        "Password": str,
        "User": str,
    },
)

_RequiredDescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef = TypedDict(
    "_RequiredDescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef",
    {
        "DiscoveryJobArn": str,
        "ResourceType": DiscoveryResourceTypeType,
        "ResourceId": str,
    },
)
_OptionalDescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef = TypedDict(
    "_OptionalDescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class DescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef(
    _RequiredDescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef,
    _OptionalDescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef,
):
    pass

ListAgentsRequestListAgentsPaginateTypeDef = TypedDict(
    "ListAgentsRequestListAgentsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListDiscoveryJobsRequestListDiscoveryJobsPaginateTypeDef = TypedDict(
    "ListDiscoveryJobsRequestListDiscoveryJobsPaginateTypeDef",
    {
        "StorageSystemArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListStorageSystemsRequestListStorageSystemsPaginateTypeDef = TypedDict(
    "ListStorageSystemsRequestListStorageSystemsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(
    _RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
    _OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
):
    pass

ListTaskExecutionsRequestListTaskExecutionsPaginateTypeDef = TypedDict(
    "ListTaskExecutionsRequestListTaskExecutionsPaginateTypeDef",
    {
        "TaskArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeStorageSystemResponseTypeDef = TypedDict(
    "DescribeStorageSystemResponseTypeDef",
    {
        "StorageSystemArn": str,
        "ServerConfiguration": DiscoveryServerConfigurationOutputTypeDef,
        "SystemType": Literal["NetAppONTAP"],
        "AgentArns": List[str],
        "Name": str,
        "ErrorMessage": str,
        "ConnectivityStatus": StorageSystemConnectivityStatusType,
        "CloudWatchLogGroupArn": str,
        "CreationTime": datetime,
        "SecretsManagerArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTaskExecutionResponseTypeDef = TypedDict(
    "DescribeTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": TaskExecutionStatusType,
        "Options": OptionsOutputTypeDef,
        "Excludes": List[FilterRuleOutputTypeDef],
        "Includes": List[FilterRuleOutputTypeDef],
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "Result": TaskExecutionResultDetailTypeDef,
        "BytesCompressed": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTaskResponseTypeDef = TypedDict(
    "DescribeTaskResponseTypeDef",
    {
        "TaskArn": str,
        "Status": TaskStatusType,
        "Name": str,
        "CurrentTaskExecutionArn": str,
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": str,
        "SourceNetworkInterfaceArns": List[str],
        "DestinationNetworkInterfaceArns": List[str],
        "Options": OptionsOutputTypeDef,
        "Excludes": List[FilterRuleOutputTypeDef],
        "Schedule": TaskScheduleOutputTypeDef,
        "ErrorCode": str,
        "ErrorDetail": str,
        "CreationTime": datetime,
        "Includes": List[FilterRuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDiscoveryJobsResponseTypeDef = TypedDict(
    "ListDiscoveryJobsResponseTypeDef",
    {
        "DiscoveryJobs": List[DiscoveryJobListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLocationsRequestListLocationsPaginateTypeDef = TypedDict(
    "ListLocationsRequestListLocationsPaginateTypeDef",
    {
        "Filters": Sequence[LocationFilterTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListLocationsRequestRequestTypeDef = TypedDict(
    "ListLocationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": Sequence[LocationFilterTypeDef],
    },
    total=False,
)

ListLocationsResponseTypeDef = TypedDict(
    "ListLocationsResponseTypeDef",
    {
        "Locations": List[LocationListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStorageSystemsResponseTypeDef = TypedDict(
    "ListStorageSystemsResponseTypeDef",
    {
        "StorageSystems": List[StorageSystemListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagListEntryOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTaskExecutionsResponseTypeDef = TypedDict(
    "ListTaskExecutionsResponseTypeDef",
    {
        "TaskExecutions": List[TaskExecutionListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTasksRequestListTasksPaginateTypeDef = TypedDict(
    "ListTasksRequestListTasksPaginateTypeDef",
    {
        "Filters": Sequence[TaskFilterTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListTasksRequestRequestTypeDef = TypedDict(
    "ListTasksRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": Sequence[TaskFilterTypeDef],
    },
    total=False,
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {
        "Tasks": List[TaskListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetAppONTAPClusterTypeDef = TypedDict(
    "NetAppONTAPClusterTypeDef",
    {
        "CifsShareCount": int,
        "NfsExportedVolumes": int,
        "ResourceId": str,
        "ClusterName": str,
        "MaxP95Performance": MaxP95PerformanceTypeDef,
        "ClusterBlockStorageSize": int,
        "ClusterBlockStorageUsed": int,
        "ClusterBlockStorageLogicalUsed": int,
        "Recommendations": List[RecommendationTypeDef],
        "RecommendationStatus": RecommendationStatusType,
        "LunCount": int,
    },
)

NetAppONTAPSVMTypeDef = TypedDict(
    "NetAppONTAPSVMTypeDef",
    {
        "ClusterUuid": str,
        "ResourceId": str,
        "SvmName": str,
        "CifsShareCount": int,
        "EnabledProtocols": List[str],
        "TotalCapacityUsed": int,
        "TotalCapacityProvisioned": int,
        "TotalLogicalCapacityUsed": int,
        "MaxP95Performance": MaxP95PerformanceTypeDef,
        "Recommendations": List[RecommendationTypeDef],
        "NfsExportedVolumes": int,
        "RecommendationStatus": RecommendationStatusType,
        "TotalSnapshotCapacityUsed": int,
        "LunCount": int,
    },
)

NetAppONTAPVolumeTypeDef = TypedDict(
    "NetAppONTAPVolumeTypeDef",
    {
        "VolumeName": str,
        "ResourceId": str,
        "CifsShareCount": int,
        "SecurityStyle": str,
        "SvmUuid": str,
        "SvmName": str,
        "CapacityUsed": int,
        "CapacityProvisioned": int,
        "LogicalCapacityUsed": int,
        "NfsExported": bool,
        "SnapshotCapacityUsed": int,
        "MaxP95Performance": MaxP95PerformanceTypeDef,
        "Recommendations": List[RecommendationTypeDef],
        "RecommendationStatus": RecommendationStatusType,
        "LunCount": int,
    },
)

P95MetricsTypeDef = TypedDict(
    "P95MetricsTypeDef",
    {
        "IOPS": IOPSTypeDef,
        "Throughput": ThroughputTypeDef,
        "Latency": LatencyTypeDef,
    },
)

FsxProtocolTypeDef = TypedDict(
    "FsxProtocolTypeDef",
    {
        "NFS": FsxProtocolNfsTypeDef,
        "SMB": FsxProtocolSmbTypeDef,
    },
    total=False,
)

FsxProtocolOutputTypeDef = TypedDict(
    "FsxProtocolOutputTypeDef",
    {
        "NFS": FsxProtocolNfsOutputTypeDef,
        "SMB": FsxProtocolSmbOutputTypeDef,
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "NetAppONTAPSVMs": List[NetAppONTAPSVMTypeDef],
        "NetAppONTAPVolumes": List[NetAppONTAPVolumeTypeDef],
        "NetAppONTAPClusters": List[NetAppONTAPClusterTypeDef],
    },
)

ResourceMetricsTypeDef = TypedDict(
    "ResourceMetricsTypeDef",
    {
        "Timestamp": datetime,
        "P95Metrics": P95MetricsTypeDef,
        "Capacity": CapacityTypeDef,
        "ResourceId": str,
        "ResourceType": DiscoveryResourceTypeType,
    },
)

_RequiredCreateLocationFsxOntapRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxOntapRequestRequestTypeDef",
    {
        "Protocol": FsxProtocolTypeDef,
        "SecurityGroupArns": Sequence[str],
        "StorageVirtualMachineArn": str,
    },
)
_OptionalCreateLocationFsxOntapRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxOntapRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class CreateLocationFsxOntapRequestRequestTypeDef(
    _RequiredCreateLocationFsxOntapRequestRequestTypeDef,
    _OptionalCreateLocationFsxOntapRequestRequestTypeDef,
):
    pass

_RequiredCreateLocationFsxOpenZfsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxOpenZfsRequestRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "Protocol": FsxProtocolTypeDef,
        "SecurityGroupArns": Sequence[str],
    },
)
_OptionalCreateLocationFsxOpenZfsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxOpenZfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": Sequence[TagListEntryTypeDef],
    },
    total=False,
)

class CreateLocationFsxOpenZfsRequestRequestTypeDef(
    _RequiredCreateLocationFsxOpenZfsRequestRequestTypeDef,
    _OptionalCreateLocationFsxOpenZfsRequestRequestTypeDef,
):
    pass

DescribeLocationFsxOntapResponseTypeDef = TypedDict(
    "DescribeLocationFsxOntapResponseTypeDef",
    {
        "CreationTime": datetime,
        "LocationArn": str,
        "LocationUri": str,
        "Protocol": FsxProtocolOutputTypeDef,
        "SecurityGroupArns": List[str],
        "StorageVirtualMachineArn": str,
        "FsxFilesystemArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLocationFsxOpenZfsResponseTypeDef = TypedDict(
    "DescribeLocationFsxOpenZfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "Protocol": FsxProtocolOutputTypeDef,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStorageSystemResourcesResponseTypeDef = TypedDict(
    "DescribeStorageSystemResourcesResponseTypeDef",
    {
        "ResourceDetails": ResourceDetailsTypeDef,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStorageSystemResourceMetricsResponseTypeDef = TypedDict(
    "DescribeStorageSystemResourceMetricsResponseTypeDef",
    {
        "Metrics": List[ResourceMetricsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
