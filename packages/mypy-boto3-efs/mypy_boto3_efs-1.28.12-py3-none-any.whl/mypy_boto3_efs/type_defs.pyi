"""
Type annotations for efs service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/type_defs/)

Usage::

    ```python
    from mypy_boto3_efs.type_defs import PosixUserOutputTypeDef

    data: PosixUserOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    LifeCycleStateType,
    PerformanceModeType,
    ReplicationStatusType,
    ResourceIdTypeType,
    ResourceType,
    StatusType,
    ThroughputModeType,
    TransitionToIARulesType,
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
    "PosixUserOutputTypeDef",
    "TagOutputTypeDef",
    "BackupPolicyOutputTypeDef",
    "BackupPolicyTypeDef",
    "PosixUserTypeDef",
    "TagTypeDef",
    "CreateMountTargetRequestRequestTypeDef",
    "DestinationToCreateTypeDef",
    "CreationInfoOutputTypeDef",
    "CreationInfoTypeDef",
    "DeleteAccessPointRequestRequestTypeDef",
    "DeleteFileSystemPolicyRequestRequestTypeDef",
    "DeleteFileSystemRequestRequestTypeDef",
    "DeleteMountTargetRequestRequestTypeDef",
    "DeleteReplicationConfigurationRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DescribeAccessPointsRequestRequestTypeDef",
    "DescribeAccountPreferencesRequestRequestTypeDef",
    "ResourceIdPreferenceTypeDef",
    "DescribeBackupPolicyRequestRequestTypeDef",
    "DescribeFileSystemPolicyRequestRequestTypeDef",
    "DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef",
    "DescribeFileSystemsRequestRequestTypeDef",
    "DescribeLifecycleConfigurationRequestRequestTypeDef",
    "DescribeMountTargetSecurityGroupsRequestRequestTypeDef",
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    "DescribeMountTargetsRequestDescribeMountTargetsPaginateTypeDef",
    "DescribeMountTargetsRequestRequestTypeDef",
    "MountTargetDescriptionTypeDef",
    "DescribeReplicationConfigurationsRequestRequestTypeDef",
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DestinationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FileSystemSizeTypeDef",
    "FileSystemPolicyDescriptionTypeDef",
    "LifecyclePolicyOutputTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ModifyMountTargetSecurityGroupsRequestRequestTypeDef",
    "MountTargetDescriptionResponseMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "PutAccountPreferencesRequestRequestTypeDef",
    "PutFileSystemPolicyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFileSystemRequestRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "BackupPolicyDescriptionTypeDef",
    "PutBackupPolicyRequestRequestTypeDef",
    "CreateFileSystemRequestRequestTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateReplicationConfigurationRequestRequestTypeDef",
    "RootDirectoryOutputTypeDef",
    "RootDirectoryTypeDef",
    "DescribeAccountPreferencesResponseTypeDef",
    "PutAccountPreferencesResponseTypeDef",
    "DescribeMountTargetsResponseTypeDef",
    "ReplicationConfigurationDescriptionResponseMetadataTypeDef",
    "ReplicationConfigurationDescriptionTypeDef",
    "FileSystemDescriptionResponseMetadataTypeDef",
    "FileSystemDescriptionTypeDef",
    "LifecycleConfigurationDescriptionTypeDef",
    "PutLifecycleConfigurationRequestRequestTypeDef",
    "AccessPointDescriptionResponseMetadataTypeDef",
    "AccessPointDescriptionTypeDef",
    "CreateAccessPointRequestRequestTypeDef",
    "DescribeReplicationConfigurationsResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeAccessPointsResponseTypeDef",
)

_RequiredPosixUserOutputTypeDef = TypedDict(
    "_RequiredPosixUserOutputTypeDef",
    {
        "Uid": int,
        "Gid": int,
    },
)
_OptionalPosixUserOutputTypeDef = TypedDict(
    "_OptionalPosixUserOutputTypeDef",
    {
        "SecondaryGids": List[int],
    },
    total=False,
)

class PosixUserOutputTypeDef(_RequiredPosixUserOutputTypeDef, _OptionalPosixUserOutputTypeDef):
    pass

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

BackupPolicyOutputTypeDef = TypedDict(
    "BackupPolicyOutputTypeDef",
    {
        "Status": StatusType,
    },
)

BackupPolicyTypeDef = TypedDict(
    "BackupPolicyTypeDef",
    {
        "Status": StatusType,
    },
)

_RequiredPosixUserTypeDef = TypedDict(
    "_RequiredPosixUserTypeDef",
    {
        "Uid": int,
        "Gid": int,
    },
)
_OptionalPosixUserTypeDef = TypedDict(
    "_OptionalPosixUserTypeDef",
    {
        "SecondaryGids": Sequence[int],
    },
    total=False,
)

class PosixUserTypeDef(_RequiredPosixUserTypeDef, _OptionalPosixUserTypeDef):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredCreateMountTargetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMountTargetRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "SubnetId": str,
    },
)
_OptionalCreateMountTargetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMountTargetRequestRequestTypeDef",
    {
        "IpAddress": str,
        "SecurityGroups": Sequence[str],
    },
    total=False,
)

class CreateMountTargetRequestRequestTypeDef(
    _RequiredCreateMountTargetRequestRequestTypeDef, _OptionalCreateMountTargetRequestRequestTypeDef
):
    pass

DestinationToCreateTypeDef = TypedDict(
    "DestinationToCreateTypeDef",
    {
        "Region": str,
        "AvailabilityZoneName": str,
        "KmsKeyId": str,
    },
    total=False,
)

CreationInfoOutputTypeDef = TypedDict(
    "CreationInfoOutputTypeDef",
    {
        "OwnerUid": int,
        "OwnerGid": int,
        "Permissions": str,
    },
)

CreationInfoTypeDef = TypedDict(
    "CreationInfoTypeDef",
    {
        "OwnerUid": int,
        "OwnerGid": int,
        "Permissions": str,
    },
)

DeleteAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestRequestTypeDef",
    {
        "AccessPointId": str,
    },
)

DeleteFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "DeleteFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DeleteFileSystemRequestRequestTypeDef = TypedDict(
    "DeleteFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DeleteMountTargetRequestRequestTypeDef = TypedDict(
    "DeleteMountTargetRequestRequestTypeDef",
    {
        "MountTargetId": str,
    },
)

DeleteReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteReplicationConfigurationRequestRequestTypeDef",
    {
        "SourceFileSystemId": str,
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "TagKeys": Sequence[str],
    },
)

DescribeAccessPointsRequestRequestTypeDef = TypedDict(
    "DescribeAccessPointsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "AccessPointId": str,
        "FileSystemId": str,
    },
    total=False,
)

DescribeAccountPreferencesRequestRequestTypeDef = TypedDict(
    "DescribeAccountPreferencesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ResourceIdPreferenceTypeDef = TypedDict(
    "ResourceIdPreferenceTypeDef",
    {
        "ResourceIdType": ResourceIdTypeType,
        "Resources": List[ResourceType],
    },
    total=False,
)

DescribeBackupPolicyRequestRequestTypeDef = TypedDict(
    "DescribeBackupPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef = TypedDict(
    "DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef",
    {
        "CreationToken": str,
        "FileSystemId": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeFileSystemsRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemsRequestRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
        "CreationToken": str,
        "FileSystemId": str,
    },
    total=False,
)

DescribeLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLifecycleConfigurationRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeMountTargetSecurityGroupsRequestRequestTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsRequestRequestTypeDef",
    {
        "MountTargetId": str,
    },
)

DescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMountTargetsRequestDescribeMountTargetsPaginateTypeDef = TypedDict(
    "DescribeMountTargetsRequestDescribeMountTargetsPaginateTypeDef",
    {
        "FileSystemId": str,
        "MountTargetId": str,
        "AccessPointId": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeMountTargetsRequestRequestTypeDef = TypedDict(
    "DescribeMountTargetsRequestRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
        "FileSystemId": str,
        "MountTargetId": str,
        "AccessPointId": str,
    },
    total=False,
)

_RequiredMountTargetDescriptionTypeDef = TypedDict(
    "_RequiredMountTargetDescriptionTypeDef",
    {
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": LifeCycleStateType,
    },
)
_OptionalMountTargetDescriptionTypeDef = TypedDict(
    "_OptionalMountTargetDescriptionTypeDef",
    {
        "OwnerId": str,
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
        "VpcId": str,
    },
    total=False,
)

class MountTargetDescriptionTypeDef(
    _RequiredMountTargetDescriptionTypeDef, _OptionalMountTargetDescriptionTypeDef
):
    pass

DescribeReplicationConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeReplicationConfigurationsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredDescribeTagsRequestDescribeTagsPaginateTypeDef = TypedDict(
    "_RequiredDescribeTagsRequestDescribeTagsPaginateTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDescribeTagsRequestDescribeTagsPaginateTypeDef = TypedDict(
    "_OptionalDescribeTagsRequestDescribeTagsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class DescribeTagsRequestDescribeTagsPaginateTypeDef(
    _RequiredDescribeTagsRequestDescribeTagsPaginateTypeDef,
    _OptionalDescribeTagsRequestDescribeTagsPaginateTypeDef,
):
    pass

_RequiredDescribeTagsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDescribeTagsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTagsRequestRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)

class DescribeTagsRequestRequestTypeDef(
    _RequiredDescribeTagsRequestRequestTypeDef, _OptionalDescribeTagsRequestRequestTypeDef
):
    pass

_RequiredDestinationTypeDef = TypedDict(
    "_RequiredDestinationTypeDef",
    {
        "Status": ReplicationStatusType,
        "FileSystemId": str,
        "Region": str,
    },
)
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "LastReplicatedTimestamp": datetime,
    },
    total=False,
)

class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFileSystemSizeTypeDef = TypedDict(
    "_RequiredFileSystemSizeTypeDef",
    {
        "Value": int,
    },
)
_OptionalFileSystemSizeTypeDef = TypedDict(
    "_OptionalFileSystemSizeTypeDef",
    {
        "Timestamp": datetime,
        "ValueInIA": int,
        "ValueInStandard": int,
    },
    total=False,
)

class FileSystemSizeTypeDef(_RequiredFileSystemSizeTypeDef, _OptionalFileSystemSizeTypeDef):
    pass

FileSystemPolicyDescriptionTypeDef = TypedDict(
    "FileSystemPolicyDescriptionTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecyclePolicyOutputTypeDef = TypedDict(
    "LifecyclePolicyOutputTypeDef",
    {
        "TransitionToIA": TransitionToIARulesType,
        "TransitionToPrimaryStorageClass": Literal["AFTER_1_ACCESS"],
    },
    total=False,
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "TransitionToIA": TransitionToIARulesType,
        "TransitionToPrimaryStorageClass": Literal["AFTER_1_ACCESS"],
    },
    total=False,
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
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

_RequiredModifyMountTargetSecurityGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyMountTargetSecurityGroupsRequestRequestTypeDef",
    {
        "MountTargetId": str,
    },
)
_OptionalModifyMountTargetSecurityGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyMountTargetSecurityGroupsRequestRequestTypeDef",
    {
        "SecurityGroups": Sequence[str],
    },
    total=False,
)

class ModifyMountTargetSecurityGroupsRequestRequestTypeDef(
    _RequiredModifyMountTargetSecurityGroupsRequestRequestTypeDef,
    _OptionalModifyMountTargetSecurityGroupsRequestRequestTypeDef,
):
    pass

MountTargetDescriptionResponseMetadataTypeDef = TypedDict(
    "MountTargetDescriptionResponseMetadataTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": LifeCycleStateType,
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PutAccountPreferencesRequestRequestTypeDef = TypedDict(
    "PutAccountPreferencesRequestRequestTypeDef",
    {
        "ResourceIdType": ResourceIdTypeType,
    },
)

_RequiredPutFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
    },
)
_OptionalPutFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutFileSystemPolicyRequestRequestTypeDef",
    {
        "BypassPolicyLockoutSafetyCheck": bool,
    },
    total=False,
)

class PutFileSystemPolicyRequestRequestTypeDef(
    _RequiredPutFileSystemPolicyRequestRequestTypeDef,
    _OptionalPutFileSystemPolicyRequestRequestTypeDef,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateFileSystemRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalUpdateFileSystemRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFileSystemRequestRequestTypeDef",
    {
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
    },
    total=False,
)

class UpdateFileSystemRequestRequestTypeDef(
    _RequiredUpdateFileSystemRequestRequestTypeDef, _OptionalUpdateFileSystemRequestRequestTypeDef
):
    pass

DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {
        "Marker": str,
        "Tags": List[TagOutputTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackupPolicyDescriptionTypeDef = TypedDict(
    "BackupPolicyDescriptionTypeDef",
    {
        "BackupPolicy": BackupPolicyOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutBackupPolicyRequestRequestTypeDef = TypedDict(
    "PutBackupPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "BackupPolicy": BackupPolicyTypeDef,
    },
)

_RequiredCreateFileSystemRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFileSystemRequestRequestTypeDef",
    {
        "CreationToken": str,
    },
)
_OptionalCreateFileSystemRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFileSystemRequestRequestTypeDef",
    {
        "PerformanceMode": PerformanceModeType,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
        "AvailabilityZoneName": str,
        "Backup": bool,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateFileSystemRequestRequestTypeDef(
    _RequiredCreateFileSystemRequestRequestTypeDef, _OptionalCreateFileSystemRequestRequestTypeDef
):
    pass

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Tags": Sequence[TagTypeDef],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence[TagTypeDef],
    },
)

CreateReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "CreateReplicationConfigurationRequestRequestTypeDef",
    {
        "SourceFileSystemId": str,
        "Destinations": Sequence[DestinationToCreateTypeDef],
    },
)

RootDirectoryOutputTypeDef = TypedDict(
    "RootDirectoryOutputTypeDef",
    {
        "Path": str,
        "CreationInfo": CreationInfoOutputTypeDef,
    },
    total=False,
)

RootDirectoryTypeDef = TypedDict(
    "RootDirectoryTypeDef",
    {
        "Path": str,
        "CreationInfo": CreationInfoTypeDef,
    },
    total=False,
)

DescribeAccountPreferencesResponseTypeDef = TypedDict(
    "DescribeAccountPreferencesResponseTypeDef",
    {
        "ResourceIdPreference": ResourceIdPreferenceTypeDef,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAccountPreferencesResponseTypeDef = TypedDict(
    "PutAccountPreferencesResponseTypeDef",
    {
        "ResourceIdPreference": ResourceIdPreferenceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMountTargetsResponseTypeDef = TypedDict(
    "DescribeMountTargetsResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[MountTargetDescriptionTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationConfigurationDescriptionResponseMetadataTypeDef = TypedDict(
    "ReplicationConfigurationDescriptionResponseMetadataTypeDef",
    {
        "SourceFileSystemId": str,
        "SourceFileSystemRegion": str,
        "SourceFileSystemArn": str,
        "OriginalSourceFileSystemArn": str,
        "CreationTime": datetime,
        "Destinations": List[DestinationTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationConfigurationDescriptionTypeDef = TypedDict(
    "ReplicationConfigurationDescriptionTypeDef",
    {
        "SourceFileSystemId": str,
        "SourceFileSystemRegion": str,
        "SourceFileSystemArn": str,
        "OriginalSourceFileSystemArn": str,
        "CreationTime": datetime,
        "Destinations": List[DestinationTypeDef],
    },
)

FileSystemDescriptionResponseMetadataTypeDef = TypedDict(
    "FileSystemDescriptionResponseMetadataTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "FileSystemArn": str,
        "CreationTime": datetime,
        "LifeCycleState": LifeCycleStateType,
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": FileSystemSizeTypeDef,
        "PerformanceMode": PerformanceModeType,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
        "AvailabilityZoneName": str,
        "AvailabilityZoneId": str,
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFileSystemDescriptionTypeDef = TypedDict(
    "_RequiredFileSystemDescriptionTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": LifeCycleStateType,
        "NumberOfMountTargets": int,
        "SizeInBytes": FileSystemSizeTypeDef,
        "PerformanceMode": PerformanceModeType,
        "Tags": List[TagOutputTypeDef],
    },
)
_OptionalFileSystemDescriptionTypeDef = TypedDict(
    "_OptionalFileSystemDescriptionTypeDef",
    {
        "FileSystemArn": str,
        "Name": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
        "AvailabilityZoneName": str,
        "AvailabilityZoneId": str,
    },
    total=False,
)

class FileSystemDescriptionTypeDef(
    _RequiredFileSystemDescriptionTypeDef, _OptionalFileSystemDescriptionTypeDef
):
    pass

LifecycleConfigurationDescriptionTypeDef = TypedDict(
    "LifecycleConfigurationDescriptionTypeDef",
    {
        "LifecyclePolicies": List[LifecyclePolicyOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "PutLifecycleConfigurationRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "LifecyclePolicies": Sequence[LifecyclePolicyTypeDef],
    },
)

AccessPointDescriptionResponseMetadataTypeDef = TypedDict(
    "AccessPointDescriptionResponseMetadataTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List[TagOutputTypeDef],
        "AccessPointId": str,
        "AccessPointArn": str,
        "FileSystemId": str,
        "PosixUser": PosixUserOutputTypeDef,
        "RootDirectory": RootDirectoryOutputTypeDef,
        "OwnerId": str,
        "LifeCycleState": LifeCycleStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccessPointDescriptionTypeDef = TypedDict(
    "AccessPointDescriptionTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List[TagOutputTypeDef],
        "AccessPointId": str,
        "AccessPointArn": str,
        "FileSystemId": str,
        "PosixUser": PosixUserOutputTypeDef,
        "RootDirectory": RootDirectoryOutputTypeDef,
        "OwnerId": str,
        "LifeCycleState": LifeCycleStateType,
    },
    total=False,
)

_RequiredCreateAccessPointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPointRequestRequestTypeDef",
    {
        "ClientToken": str,
        "FileSystemId": str,
    },
)
_OptionalCreateAccessPointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPointRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
        "PosixUser": PosixUserTypeDef,
        "RootDirectory": RootDirectoryTypeDef,
    },
    total=False,
)

class CreateAccessPointRequestRequestTypeDef(
    _RequiredCreateAccessPointRequestRequestTypeDef, _OptionalCreateAccessPointRequestRequestTypeDef
):
    pass

DescribeReplicationConfigurationsResponseTypeDef = TypedDict(
    "DescribeReplicationConfigurationsResponseTypeDef",
    {
        "Replications": List[ReplicationConfigurationDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[FileSystemDescriptionTypeDef],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccessPointsResponseTypeDef = TypedDict(
    "DescribeAccessPointsResponseTypeDef",
    {
        "AccessPoints": List[AccessPointDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
