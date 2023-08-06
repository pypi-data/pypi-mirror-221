"""
Type annotations for ecs service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/type_defs/)

Usage::

    ```python
    from mypy_boto3_ecs.type_defs import AttachmentStateChangeTypeDef

    data: AttachmentStateChangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AgentUpdateStatusType,
    ApplicationProtocolType,
    AssignPublicIpType,
    CapacityProviderStatusType,
    CapacityProviderUpdateStatusType,
    ClusterFieldType,
    CompatibilityType,
    ConnectivityType,
    ContainerConditionType,
    ContainerInstanceFieldType,
    ContainerInstanceStatusType,
    CPUArchitectureType,
    DeploymentControllerTypeType,
    DeploymentRolloutStateType,
    DesiredStatusType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    ExecuteCommandLoggingType,
    FirelensConfigurationTypeType,
    HealthStatusType,
    InstanceHealthCheckStateType,
    IpcModeType,
    LaunchTypeType,
    LogDriverType,
    ManagedScalingStatusType,
    ManagedTerminationProtectionType,
    NetworkModeType,
    OSFamilyType,
    PidModeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    PropagateTagsType,
    ResourceTypeType,
    SchedulingStrategyType,
    ScopeType,
    SettingNameType,
    SortOrderType,
    StabilityStatusType,
    TaskDefinitionFamilyStatusType,
    TaskDefinitionStatusType,
    TaskStopCodeType,
    TransportProtocolType,
    UlimitNameType,
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
    "AttachmentStateChangeTypeDef",
    "KeyValuePairOutputTypeDef",
    "AttributeOutputTypeDef",
    "AttributeTypeDef",
    "ManagedScalingOutputTypeDef",
    "ManagedScalingTypeDef",
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemOutputTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "TagOutputTypeDef",
    "ClusterServiceConnectDefaultsRequestTypeDef",
    "ClusterServiceConnectDefaultsTypeDef",
    "ClusterSettingOutputTypeDef",
    "ClusterSettingTypeDef",
    "ContainerDependencyOutputTypeDef",
    "EnvironmentFileOutputTypeDef",
    "FirelensConfigurationOutputTypeDef",
    "HealthCheckOutputTypeDef",
    "HostEntryOutputTypeDef",
    "MountPointOutputTypeDef",
    "PortMappingOutputTypeDef",
    "RepositoryCredentialsOutputTypeDef",
    "ResourceRequirementOutputTypeDef",
    "SecretOutputTypeDef",
    "SystemControlOutputTypeDef",
    "UlimitOutputTypeDef",
    "VolumeFromOutputTypeDef",
    "ContainerDependencyTypeDef",
    "EnvironmentFileTypeDef",
    "FirelensConfigurationTypeDef",
    "HealthCheckTypeDef",
    "HostEntryTypeDef",
    "KeyValuePairTypeDef",
    "MountPointTypeDef",
    "PortMappingTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "SecretTypeDef",
    "SystemControlTypeDef",
    "UlimitTypeDef",
    "VolumeFromTypeDef",
    "InstanceHealthCheckResultTypeDef",
    "ResourceOutputTypeDef",
    "VersionInfoOutputTypeDef",
    "NetworkBindingTypeDef",
    "ManagedAgentTypeDef",
    "NetworkBindingOutputTypeDef",
    "NetworkInterfaceTypeDef",
    "TagTypeDef",
    "DeploymentControllerTypeDef",
    "LoadBalancerTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "ServiceRegistryTypeDef",
    "ScaleTypeDef",
    "DeleteAccountSettingRequestRequestTypeDef",
    "SettingTypeDef",
    "DeleteCapacityProviderRequestRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteTaskDefinitionsRequestRequestTypeDef",
    "FailureTypeDef",
    "DeleteTaskSetRequestRequestTypeDef",
    "DeploymentAlarmsOutputTypeDef",
    "DeploymentAlarmsTypeDef",
    "DeploymentCircuitBreakerOutputTypeDef",
    "DeploymentCircuitBreakerTypeDef",
    "DeploymentControllerOutputTypeDef",
    "ServiceConnectServiceResourceTypeDef",
    "DeregisterContainerInstanceRequestRequestTypeDef",
    "DeregisterTaskDefinitionRequestRequestTypeDef",
    "DescribeCapacityProvidersRequestRequestTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeContainerInstancesRequestRequestTypeDef",
    "DescribeServicesRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeTaskDefinitionRequestRequestTypeDef",
    "DescribeTaskSetsRequestRequestTypeDef",
    "DescribeTasksRequestRequestTypeDef",
    "DeviceOutputTypeDef",
    "DeviceTypeDef",
    "DiscoverPollEndpointRequestRequestTypeDef",
    "DiscoverPollEndpointResponseTypeDef",
    "DockerVolumeConfigurationOutputTypeDef",
    "DockerVolumeConfigurationTypeDef",
    "EFSAuthorizationConfigOutputTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EphemeralStorageOutputTypeDef",
    "EphemeralStorageTypeDef",
    "ExecuteCommandLogConfigurationOutputTypeDef",
    "ExecuteCommandLogConfigurationTypeDef",
    "ExecuteCommandRequestRequestTypeDef",
    "SessionTypeDef",
    "FSxWindowsFileServerAuthorizationConfigOutputTypeDef",
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    "GetTaskProtectionRequestRequestTypeDef",
    "ProtectedTaskTypeDef",
    "HostVolumePropertiesOutputTypeDef",
    "HostVolumePropertiesTypeDef",
    "InferenceAcceleratorOutputTypeDef",
    "InferenceAcceleratorOverrideOutputTypeDef",
    "InferenceAcceleratorOverrideTypeDef",
    "InferenceAcceleratorTypeDef",
    "KernelCapabilitiesOutputTypeDef",
    "KernelCapabilitiesTypeDef",
    "TmpfsOutputTypeDef",
    "TmpfsTypeDef",
    "ListAccountSettingsRequestListAccountSettingsPaginateTypeDef",
    "ListAccountSettingsRequestRequestTypeDef",
    "ListAttributesRequestListAttributesPaginateTypeDef",
    "ListAttributesRequestRequestTypeDef",
    "ListClustersRequestListClustersPaginateTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListContainerInstancesRequestListContainerInstancesPaginateTypeDef",
    "ListContainerInstancesRequestRequestTypeDef",
    "ListContainerInstancesResponseTypeDef",
    "ListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef",
    "ListServicesByNamespaceRequestRequestTypeDef",
    "ListServicesByNamespaceResponseTypeDef",
    "ListServicesRequestListServicesPaginateTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTaskDefinitionFamiliesRequestListTaskDefinitionFamiliesPaginateTypeDef",
    "ListTaskDefinitionFamiliesRequestRequestTypeDef",
    "ListTaskDefinitionFamiliesResponseTypeDef",
    "ListTaskDefinitionsRequestListTaskDefinitionsPaginateTypeDef",
    "ListTaskDefinitionsRequestRequestTypeDef",
    "ListTaskDefinitionsResponseTypeDef",
    "ListTasksRequestListTasksPaginateTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListTasksResponseTypeDef",
    "LoadBalancerOutputTypeDef",
    "ManagedAgentStateChangeTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementConstraintOutputTypeDef",
    "PlacementStrategyOutputTypeDef",
    "PlatformDeviceTypeDef",
    "PutAccountSettingDefaultRequestRequestTypeDef",
    "PutAccountSettingRequestRequestTypeDef",
    "ResourceTypeDef",
    "VersionInfoTypeDef",
    "RuntimePlatformTypeDef",
    "TaskDefinitionPlacementConstraintTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimePlatformOutputTypeDef",
    "ScaleOutputTypeDef",
    "ServiceConnectClientAliasOutputTypeDef",
    "ServiceConnectClientAliasTypeDef",
    "ServiceEventTypeDef",
    "ServiceRegistryOutputTypeDef",
    "StopTaskRequestRequestTypeDef",
    "SubmitAttachmentStateChangesResponseTypeDef",
    "SubmitContainerStateChangeResponseTypeDef",
    "SubmitTaskStateChangeResponseTypeDef",
    "TaskDefinitionPlacementConstraintOutputTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContainerAgentRequestRequestTypeDef",
    "UpdateContainerInstancesStateRequestRequestTypeDef",
    "UpdateServicePrimaryTaskSetRequestRequestTypeDef",
    "UpdateTaskProtectionRequestRequestTypeDef",
    "SubmitAttachmentStateChangesRequestRequestTypeDef",
    "AttachmentTypeDef",
    "ProxyConfigurationOutputTypeDef",
    "DeleteAttributesResponseTypeDef",
    "ListAttributesResponseTypeDef",
    "PutAttributesResponseTypeDef",
    "DeleteAttributesRequestRequestTypeDef",
    "PutAttributesRequestRequestTypeDef",
    "AutoScalingGroupProviderOutputTypeDef",
    "AutoScalingGroupProviderTypeDef",
    "AutoScalingGroupProviderUpdateTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "PutClusterCapacityProvidersRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateClusterSettingsRequestRequestTypeDef",
    "ContainerOverrideOutputTypeDef",
    "LogConfigurationOutputTypeDef",
    "ProxyConfigurationTypeDef",
    "ContainerOverrideTypeDef",
    "LogConfigurationTypeDef",
    "ContainerInstanceHealthStatusTypeDef",
    "ContainerStateChangeTypeDef",
    "SubmitContainerStateChangeRequestRequestTypeDef",
    "ContainerTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UpdateTaskSetRequestRequestTypeDef",
    "DeleteAccountSettingResponseTypeDef",
    "ListAccountSettingsResponseTypeDef",
    "PutAccountSettingDefaultResponseTypeDef",
    "PutAccountSettingResponseTypeDef",
    "DeploymentConfigurationOutputTypeDef",
    "DeploymentConfigurationTypeDef",
    "DescribeServicesRequestServicesInactiveWaitTypeDef",
    "DescribeServicesRequestServicesStableWaitTypeDef",
    "DescribeTasksRequestTasksRunningWaitTypeDef",
    "DescribeTasksRequestTasksStoppedWaitTypeDef",
    "EFSVolumeConfigurationOutputTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "ExecuteCommandConfigurationOutputTypeDef",
    "ExecuteCommandConfigurationTypeDef",
    "ExecuteCommandResponseTypeDef",
    "FSxWindowsFileServerVolumeConfigurationOutputTypeDef",
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    "GetTaskProtectionResponseTypeDef",
    "UpdateTaskProtectionResponseTypeDef",
    "LinuxParametersOutputTypeDef",
    "LinuxParametersTypeDef",
    "RegisterContainerInstanceRequestRequestTypeDef",
    "ServiceConnectServiceOutputTypeDef",
    "ServiceConnectServiceTypeDef",
    "CapacityProviderTypeDef",
    "CreateCapacityProviderRequestRequestTypeDef",
    "UpdateCapacityProviderRequestRequestTypeDef",
    "TaskSetTypeDef",
    "CreateTaskSetRequestRequestTypeDef",
    "TaskOverrideOutputTypeDef",
    "TaskOverrideTypeDef",
    "ContainerInstanceTypeDef",
    "SubmitTaskStateChangeRequestRequestTypeDef",
    "ClusterConfigurationOutputTypeDef",
    "ClusterConfigurationTypeDef",
    "VolumeOutputTypeDef",
    "VolumeTypeDef",
    "ContainerDefinitionOutputTypeDef",
    "ContainerDefinitionTypeDef",
    "ServiceConnectConfigurationOutputTypeDef",
    "ServiceConnectConfigurationTypeDef",
    "CreateCapacityProviderResponseTypeDef",
    "DeleteCapacityProviderResponseTypeDef",
    "DescribeCapacityProvidersResponseTypeDef",
    "UpdateCapacityProviderResponseTypeDef",
    "CreateTaskSetResponseTypeDef",
    "DeleteTaskSetResponseTypeDef",
    "DescribeTaskSetsResponseTypeDef",
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    "UpdateTaskSetResponseTypeDef",
    "TaskTypeDef",
    "RunTaskRequestRequestTypeDef",
    "StartTaskRequestRequestTypeDef",
    "DeregisterContainerInstanceResponseTypeDef",
    "DescribeContainerInstancesResponseTypeDef",
    "RegisterContainerInstanceResponseTypeDef",
    "UpdateContainerAgentResponseTypeDef",
    "UpdateContainerInstancesStateResponseTypeDef",
    "ClusterTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "TaskDefinitionTypeDef",
    "RegisterTaskDefinitionRequestRequestTypeDef",
    "DeploymentTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "DescribeTasksResponseTypeDef",
    "RunTaskResponseTypeDef",
    "StartTaskResponseTypeDef",
    "StopTaskResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "PutClusterCapacityProvidersResponseTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateClusterSettingsResponseTypeDef",
    "DeleteTaskDefinitionsResponseTypeDef",
    "DeregisterTaskDefinitionResponseTypeDef",
    "DescribeTaskDefinitionResponseTypeDef",
    "RegisterTaskDefinitionResponseTypeDef",
    "ServiceTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteServiceResponseTypeDef",
    "DescribeServicesResponseTypeDef",
    "UpdateServiceResponseTypeDef",
)

AttachmentStateChangeTypeDef = TypedDict(
    "AttachmentStateChangeTypeDef",
    {
        "attachmentArn": str,
        "status": str,
    },
)

KeyValuePairOutputTypeDef = TypedDict(
    "KeyValuePairOutputTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

_RequiredAttributeOutputTypeDef = TypedDict(
    "_RequiredAttributeOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalAttributeOutputTypeDef = TypedDict(
    "_OptionalAttributeOutputTypeDef",
    {
        "value": str,
        "targetType": Literal["container-instance"],
        "targetId": str,
    },
    total=False,
)

class AttributeOutputTypeDef(_RequiredAttributeOutputTypeDef, _OptionalAttributeOutputTypeDef):
    pass

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "name": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "value": str,
        "targetType": Literal["container-instance"],
        "targetId": str,
    },
    total=False,
)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

ManagedScalingOutputTypeDef = TypedDict(
    "ManagedScalingOutputTypeDef",
    {
        "status": ManagedScalingStatusType,
        "targetCapacity": int,
        "minimumScalingStepSize": int,
        "maximumScalingStepSize": int,
        "instanceWarmupPeriod": int,
    },
    total=False,
)

ManagedScalingTypeDef = TypedDict(
    "ManagedScalingTypeDef",
    {
        "status": ManagedScalingStatusType,
        "targetCapacity": int,
        "minimumScalingStepSize": int,
        "maximumScalingStepSize": int,
        "instanceWarmupPeriod": int,
    },
    total=False,
)

_RequiredAwsVpcConfigurationOutputTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationOutputTypeDef",
    {
        "subnets": List[str],
    },
)
_OptionalAwsVpcConfigurationOutputTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationOutputTypeDef",
    {
        "securityGroups": List[str],
        "assignPublicIp": AssignPublicIpType,
    },
    total=False,
)

class AwsVpcConfigurationOutputTypeDef(
    _RequiredAwsVpcConfigurationOutputTypeDef, _OptionalAwsVpcConfigurationOutputTypeDef
):
    pass

_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef",
    {
        "subnets": Sequence[str],
    },
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {
        "securityGroups": Sequence[str],
        "assignPublicIp": AssignPublicIpType,
    },
    total=False,
)

class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass

_RequiredCapacityProviderStrategyItemOutputTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemOutputTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemOutputTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemOutputTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)

class CapacityProviderStrategyItemOutputTypeDef(
    _RequiredCapacityProviderStrategyItemOutputTypeDef,
    _OptionalCapacityProviderStrategyItemOutputTypeDef,
):
    pass

_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)

class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

ClusterServiceConnectDefaultsRequestTypeDef = TypedDict(
    "ClusterServiceConnectDefaultsRequestTypeDef",
    {
        "namespace": str,
    },
)

ClusterServiceConnectDefaultsTypeDef = TypedDict(
    "ClusterServiceConnectDefaultsTypeDef",
    {
        "namespace": str,
    },
    total=False,
)

ClusterSettingOutputTypeDef = TypedDict(
    "ClusterSettingOutputTypeDef",
    {
        "name": Literal["containerInsights"],
        "value": str,
    },
    total=False,
)

ClusterSettingTypeDef = TypedDict(
    "ClusterSettingTypeDef",
    {
        "name": Literal["containerInsights"],
        "value": str,
    },
    total=False,
)

ContainerDependencyOutputTypeDef = TypedDict(
    "ContainerDependencyOutputTypeDef",
    {
        "containerName": str,
        "condition": ContainerConditionType,
    },
)

EnvironmentFileOutputTypeDef = TypedDict(
    "EnvironmentFileOutputTypeDef",
    {
        "value": str,
        "type": Literal["s3"],
    },
)

_RequiredFirelensConfigurationOutputTypeDef = TypedDict(
    "_RequiredFirelensConfigurationOutputTypeDef",
    {
        "type": FirelensConfigurationTypeType,
    },
)
_OptionalFirelensConfigurationOutputTypeDef = TypedDict(
    "_OptionalFirelensConfigurationOutputTypeDef",
    {
        "options": Dict[str, str],
    },
    total=False,
)

class FirelensConfigurationOutputTypeDef(
    _RequiredFirelensConfigurationOutputTypeDef, _OptionalFirelensConfigurationOutputTypeDef
):
    pass

_RequiredHealthCheckOutputTypeDef = TypedDict(
    "_RequiredHealthCheckOutputTypeDef",
    {
        "command": List[str],
    },
)
_OptionalHealthCheckOutputTypeDef = TypedDict(
    "_OptionalHealthCheckOutputTypeDef",
    {
        "interval": int,
        "timeout": int,
        "retries": int,
        "startPeriod": int,
    },
    total=False,
)

class HealthCheckOutputTypeDef(
    _RequiredHealthCheckOutputTypeDef, _OptionalHealthCheckOutputTypeDef
):
    pass

HostEntryOutputTypeDef = TypedDict(
    "HostEntryOutputTypeDef",
    {
        "hostname": str,
        "ipAddress": str,
    },
)

MountPointOutputTypeDef = TypedDict(
    "MountPointOutputTypeDef",
    {
        "sourceVolume": str,
        "containerPath": str,
        "readOnly": bool,
    },
    total=False,
)

PortMappingOutputTypeDef = TypedDict(
    "PortMappingOutputTypeDef",
    {
        "containerPort": int,
        "hostPort": int,
        "protocol": TransportProtocolType,
        "name": str,
        "appProtocol": ApplicationProtocolType,
        "containerPortRange": str,
    },
    total=False,
)

RepositoryCredentialsOutputTypeDef = TypedDict(
    "RepositoryCredentialsOutputTypeDef",
    {
        "credentialsParameter": str,
    },
)

ResourceRequirementOutputTypeDef = TypedDict(
    "ResourceRequirementOutputTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

SecretOutputTypeDef = TypedDict(
    "SecretOutputTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

SystemControlOutputTypeDef = TypedDict(
    "SystemControlOutputTypeDef",
    {
        "namespace": str,
        "value": str,
    },
    total=False,
)

UlimitOutputTypeDef = TypedDict(
    "UlimitOutputTypeDef",
    {
        "name": UlimitNameType,
        "softLimit": int,
        "hardLimit": int,
    },
)

VolumeFromOutputTypeDef = TypedDict(
    "VolumeFromOutputTypeDef",
    {
        "sourceContainer": str,
        "readOnly": bool,
    },
    total=False,
)

ContainerDependencyTypeDef = TypedDict(
    "ContainerDependencyTypeDef",
    {
        "containerName": str,
        "condition": ContainerConditionType,
    },
)

EnvironmentFileTypeDef = TypedDict(
    "EnvironmentFileTypeDef",
    {
        "value": str,
        "type": Literal["s3"],
    },
)

_RequiredFirelensConfigurationTypeDef = TypedDict(
    "_RequiredFirelensConfigurationTypeDef",
    {
        "type": FirelensConfigurationTypeType,
    },
)
_OptionalFirelensConfigurationTypeDef = TypedDict(
    "_OptionalFirelensConfigurationTypeDef",
    {
        "options": Mapping[str, str],
    },
    total=False,
)

class FirelensConfigurationTypeDef(
    _RequiredFirelensConfigurationTypeDef, _OptionalFirelensConfigurationTypeDef
):
    pass

_RequiredHealthCheckTypeDef = TypedDict(
    "_RequiredHealthCheckTypeDef",
    {
        "command": Sequence[str],
    },
)
_OptionalHealthCheckTypeDef = TypedDict(
    "_OptionalHealthCheckTypeDef",
    {
        "interval": int,
        "timeout": int,
        "retries": int,
        "startPeriod": int,
    },
    total=False,
)

class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, _OptionalHealthCheckTypeDef):
    pass

HostEntryTypeDef = TypedDict(
    "HostEntryTypeDef",
    {
        "hostname": str,
        "ipAddress": str,
    },
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "sourceVolume": str,
        "containerPath": str,
        "readOnly": bool,
    },
    total=False,
)

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "containerPort": int,
        "hostPort": int,
        "protocol": TransportProtocolType,
        "name": str,
        "appProtocol": ApplicationProtocolType,
        "containerPortRange": str,
    },
    total=False,
)

RepositoryCredentialsTypeDef = TypedDict(
    "RepositoryCredentialsTypeDef",
    {
        "credentialsParameter": str,
    },
)

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

SecretTypeDef = TypedDict(
    "SecretTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

SystemControlTypeDef = TypedDict(
    "SystemControlTypeDef",
    {
        "namespace": str,
        "value": str,
    },
    total=False,
)

UlimitTypeDef = TypedDict(
    "UlimitTypeDef",
    {
        "name": UlimitNameType,
        "softLimit": int,
        "hardLimit": int,
    },
)

VolumeFromTypeDef = TypedDict(
    "VolumeFromTypeDef",
    {
        "sourceContainer": str,
        "readOnly": bool,
    },
    total=False,
)

InstanceHealthCheckResultTypeDef = TypedDict(
    "InstanceHealthCheckResultTypeDef",
    {
        "type": Literal["CONTAINER_RUNTIME"],
        "status": InstanceHealthCheckStateType,
        "lastUpdated": datetime,
        "lastStatusChange": datetime,
    },
    total=False,
)

ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

VersionInfoOutputTypeDef = TypedDict(
    "VersionInfoOutputTypeDef",
    {
        "agentVersion": str,
        "agentHash": str,
        "dockerVersion": str,
    },
    total=False,
)

NetworkBindingTypeDef = TypedDict(
    "NetworkBindingTypeDef",
    {
        "bindIP": str,
        "containerPort": int,
        "hostPort": int,
        "protocol": TransportProtocolType,
        "containerPortRange": str,
        "hostPortRange": str,
    },
    total=False,
)

ManagedAgentTypeDef = TypedDict(
    "ManagedAgentTypeDef",
    {
        "lastStartedAt": datetime,
        "name": Literal["ExecuteCommandAgent"],
        "reason": str,
        "lastStatus": str,
    },
    total=False,
)

NetworkBindingOutputTypeDef = TypedDict(
    "NetworkBindingOutputTypeDef",
    {
        "bindIP": str,
        "containerPort": int,
        "hostPort": int,
        "protocol": TransportProtocolType,
        "containerPortRange": str,
        "hostPortRange": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": str,
        "privateIpv4Address": str,
        "ipv6Address": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

DeploymentControllerTypeDef = TypedDict(
    "DeploymentControllerTypeDef",
    {
        "type": DeploymentControllerTypeType,
    },
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "targetGroupArn": str,
        "loadBalancerName": str,
        "containerName": str,
        "containerPort": int,
    },
    total=False,
)

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
    },
    total=False,
)

ServiceRegistryTypeDef = TypedDict(
    "ServiceRegistryTypeDef",
    {
        "registryArn": str,
        "port": int,
        "containerName": str,
        "containerPort": int,
    },
    total=False,
)

ScaleTypeDef = TypedDict(
    "ScaleTypeDef",
    {
        "value": float,
        "unit": Literal["PERCENT"],
    },
    total=False,
)

_RequiredDeleteAccountSettingRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAccountSettingRequestRequestTypeDef",
    {
        "name": SettingNameType,
    },
)
_OptionalDeleteAccountSettingRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAccountSettingRequestRequestTypeDef",
    {
        "principalArn": str,
    },
    total=False,
)

class DeleteAccountSettingRequestRequestTypeDef(
    _RequiredDeleteAccountSettingRequestRequestTypeDef,
    _OptionalDeleteAccountSettingRequestRequestTypeDef,
):
    pass

SettingTypeDef = TypedDict(
    "SettingTypeDef",
    {
        "name": SettingNameType,
        "value": str,
        "principalArn": str,
    },
    total=False,
)

DeleteCapacityProviderRequestRequestTypeDef = TypedDict(
    "DeleteCapacityProviderRequestRequestTypeDef",
    {
        "capacityProvider": str,
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "cluster": str,
    },
)

_RequiredDeleteServiceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteServiceRequestRequestTypeDef",
    {
        "service": str,
    },
)
_OptionalDeleteServiceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteServiceRequestRequestTypeDef",
    {
        "cluster": str,
        "force": bool,
    },
    total=False,
)

class DeleteServiceRequestRequestTypeDef(
    _RequiredDeleteServiceRequestRequestTypeDef, _OptionalDeleteServiceRequestRequestTypeDef
):
    pass

DeleteTaskDefinitionsRequestRequestTypeDef = TypedDict(
    "DeleteTaskDefinitionsRequestRequestTypeDef",
    {
        "taskDefinitions": Sequence[str],
    },
)

FailureTypeDef = TypedDict(
    "FailureTypeDef",
    {
        "arn": str,
        "reason": str,
        "detail": str,
    },
    total=False,
)

_RequiredDeleteTaskSetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSet": str,
    },
)
_OptionalDeleteTaskSetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTaskSetRequestRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)

class DeleteTaskSetRequestRequestTypeDef(
    _RequiredDeleteTaskSetRequestRequestTypeDef, _OptionalDeleteTaskSetRequestRequestTypeDef
):
    pass

DeploymentAlarmsOutputTypeDef = TypedDict(
    "DeploymentAlarmsOutputTypeDef",
    {
        "alarmNames": List[str],
        "enable": bool,
        "rollback": bool,
    },
)

DeploymentAlarmsTypeDef = TypedDict(
    "DeploymentAlarmsTypeDef",
    {
        "alarmNames": Sequence[str],
        "enable": bool,
        "rollback": bool,
    },
)

DeploymentCircuitBreakerOutputTypeDef = TypedDict(
    "DeploymentCircuitBreakerOutputTypeDef",
    {
        "enable": bool,
        "rollback": bool,
    },
)

DeploymentCircuitBreakerTypeDef = TypedDict(
    "DeploymentCircuitBreakerTypeDef",
    {
        "enable": bool,
        "rollback": bool,
    },
)

DeploymentControllerOutputTypeDef = TypedDict(
    "DeploymentControllerOutputTypeDef",
    {
        "type": DeploymentControllerTypeType,
    },
)

ServiceConnectServiceResourceTypeDef = TypedDict(
    "ServiceConnectServiceResourceTypeDef",
    {
        "discoveryName": str,
        "discoveryArn": str,
    },
    total=False,
)

_RequiredDeregisterContainerInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterContainerInstanceRequestRequestTypeDef",
    {
        "containerInstance": str,
    },
)
_OptionalDeregisterContainerInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterContainerInstanceRequestRequestTypeDef",
    {
        "cluster": str,
        "force": bool,
    },
    total=False,
)

class DeregisterContainerInstanceRequestRequestTypeDef(
    _RequiredDeregisterContainerInstanceRequestRequestTypeDef,
    _OptionalDeregisterContainerInstanceRequestRequestTypeDef,
):
    pass

DeregisterTaskDefinitionRequestRequestTypeDef = TypedDict(
    "DeregisterTaskDefinitionRequestRequestTypeDef",
    {
        "taskDefinition": str,
    },
)

DescribeCapacityProvidersRequestRequestTypeDef = TypedDict(
    "DescribeCapacityProvidersRequestRequestTypeDef",
    {
        "capacityProviders": Sequence[str],
        "include": Sequence[Literal["TAGS"]],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "clusters": Sequence[str],
        "include": Sequence[ClusterFieldType],
    },
    total=False,
)

_RequiredDescribeContainerInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeContainerInstancesRequestRequestTypeDef",
    {
        "containerInstances": Sequence[str],
    },
)
_OptionalDescribeContainerInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeContainerInstancesRequestRequestTypeDef",
    {
        "cluster": str,
        "include": Sequence[ContainerInstanceFieldType],
    },
    total=False,
)

class DescribeContainerInstancesRequestRequestTypeDef(
    _RequiredDescribeContainerInstancesRequestRequestTypeDef,
    _OptionalDescribeContainerInstancesRequestRequestTypeDef,
):
    pass

_RequiredDescribeServicesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeServicesRequestRequestTypeDef",
    {
        "services": Sequence[str],
    },
)
_OptionalDescribeServicesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeServicesRequestRequestTypeDef",
    {
        "cluster": str,
        "include": Sequence[Literal["TAGS"]],
    },
    total=False,
)

class DescribeServicesRequestRequestTypeDef(
    _RequiredDescribeServicesRequestRequestTypeDef, _OptionalDescribeServicesRequestRequestTypeDef
):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

_RequiredDescribeTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTaskDefinitionRequestRequestTypeDef",
    {
        "taskDefinition": str,
    },
)
_OptionalDescribeTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTaskDefinitionRequestRequestTypeDef",
    {
        "include": Sequence[Literal["TAGS"]],
    },
    total=False,
)

class DescribeTaskDefinitionRequestRequestTypeDef(
    _RequiredDescribeTaskDefinitionRequestRequestTypeDef,
    _OptionalDescribeTaskDefinitionRequestRequestTypeDef,
):
    pass

_RequiredDescribeTaskSetsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTaskSetsRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
    },
)
_OptionalDescribeTaskSetsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTaskSetsRequestRequestTypeDef",
    {
        "taskSets": Sequence[str],
        "include": Sequence[Literal["TAGS"]],
    },
    total=False,
)

class DescribeTaskSetsRequestRequestTypeDef(
    _RequiredDescribeTaskSetsRequestRequestTypeDef, _OptionalDescribeTaskSetsRequestRequestTypeDef
):
    pass

_RequiredDescribeTasksRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTasksRequestRequestTypeDef",
    {
        "tasks": Sequence[str],
    },
)
_OptionalDescribeTasksRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTasksRequestRequestTypeDef",
    {
        "cluster": str,
        "include": Sequence[Literal["TAGS"]],
    },
    total=False,
)

class DescribeTasksRequestRequestTypeDef(
    _RequiredDescribeTasksRequestRequestTypeDef, _OptionalDescribeTasksRequestRequestTypeDef
):
    pass

_RequiredDeviceOutputTypeDef = TypedDict(
    "_RequiredDeviceOutputTypeDef",
    {
        "hostPath": str,
    },
)
_OptionalDeviceOutputTypeDef = TypedDict(
    "_OptionalDeviceOutputTypeDef",
    {
        "containerPath": str,
        "permissions": List[DeviceCgroupPermissionType],
    },
    total=False,
)

class DeviceOutputTypeDef(_RequiredDeviceOutputTypeDef, _OptionalDeviceOutputTypeDef):
    pass

_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef",
    {
        "hostPath": str,
    },
)
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {
        "containerPath": str,
        "permissions": Sequence[DeviceCgroupPermissionType],
    },
    total=False,
)

class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass

DiscoverPollEndpointRequestRequestTypeDef = TypedDict(
    "DiscoverPollEndpointRequestRequestTypeDef",
    {
        "containerInstance": str,
        "cluster": str,
    },
    total=False,
)

DiscoverPollEndpointResponseTypeDef = TypedDict(
    "DiscoverPollEndpointResponseTypeDef",
    {
        "endpoint": str,
        "telemetryEndpoint": str,
        "serviceConnectEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DockerVolumeConfigurationOutputTypeDef = TypedDict(
    "DockerVolumeConfigurationOutputTypeDef",
    {
        "scope": ScopeType,
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)

DockerVolumeConfigurationTypeDef = TypedDict(
    "DockerVolumeConfigurationTypeDef",
    {
        "scope": ScopeType,
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Mapping[str, str],
        "labels": Mapping[str, str],
    },
    total=False,
)

EFSAuthorizationConfigOutputTypeDef = TypedDict(
    "EFSAuthorizationConfigOutputTypeDef",
    {
        "accessPointId": str,
        "iam": EFSAuthorizationConfigIAMType,
    },
    total=False,
)

EFSAuthorizationConfigTypeDef = TypedDict(
    "EFSAuthorizationConfigTypeDef",
    {
        "accessPointId": str,
        "iam": EFSAuthorizationConfigIAMType,
    },
    total=False,
)

EphemeralStorageOutputTypeDef = TypedDict(
    "EphemeralStorageOutputTypeDef",
    {
        "sizeInGiB": int,
    },
)

EphemeralStorageTypeDef = TypedDict(
    "EphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

ExecuteCommandLogConfigurationOutputTypeDef = TypedDict(
    "ExecuteCommandLogConfigurationOutputTypeDef",
    {
        "cloudWatchLogGroupName": str,
        "cloudWatchEncryptionEnabled": bool,
        "s3BucketName": str,
        "s3EncryptionEnabled": bool,
        "s3KeyPrefix": str,
    },
    total=False,
)

ExecuteCommandLogConfigurationTypeDef = TypedDict(
    "ExecuteCommandLogConfigurationTypeDef",
    {
        "cloudWatchLogGroupName": str,
        "cloudWatchEncryptionEnabled": bool,
        "s3BucketName": str,
        "s3EncryptionEnabled": bool,
        "s3KeyPrefix": str,
    },
    total=False,
)

_RequiredExecuteCommandRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteCommandRequestRequestTypeDef",
    {
        "command": str,
        "interactive": bool,
        "task": str,
    },
)
_OptionalExecuteCommandRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteCommandRequestRequestTypeDef",
    {
        "cluster": str,
        "container": str,
    },
    total=False,
)

class ExecuteCommandRequestRequestTypeDef(
    _RequiredExecuteCommandRequestRequestTypeDef, _OptionalExecuteCommandRequestRequestTypeDef
):
    pass

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "sessionId": str,
        "streamUrl": str,
        "tokenValue": str,
    },
    total=False,
)

FSxWindowsFileServerAuthorizationConfigOutputTypeDef = TypedDict(
    "FSxWindowsFileServerAuthorizationConfigOutputTypeDef",
    {
        "credentialsParameter": str,
        "domain": str,
    },
)

FSxWindowsFileServerAuthorizationConfigTypeDef = TypedDict(
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    {
        "credentialsParameter": str,
        "domain": str,
    },
)

_RequiredGetTaskProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetTaskProtectionRequestRequestTypeDef",
    {
        "cluster": str,
    },
)
_OptionalGetTaskProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetTaskProtectionRequestRequestTypeDef",
    {
        "tasks": Sequence[str],
    },
    total=False,
)

class GetTaskProtectionRequestRequestTypeDef(
    _RequiredGetTaskProtectionRequestRequestTypeDef, _OptionalGetTaskProtectionRequestRequestTypeDef
):
    pass

ProtectedTaskTypeDef = TypedDict(
    "ProtectedTaskTypeDef",
    {
        "taskArn": str,
        "protectionEnabled": bool,
        "expirationDate": datetime,
    },
    total=False,
)

HostVolumePropertiesOutputTypeDef = TypedDict(
    "HostVolumePropertiesOutputTypeDef",
    {
        "sourcePath": str,
    },
    total=False,
)

HostVolumePropertiesTypeDef = TypedDict(
    "HostVolumePropertiesTypeDef",
    {
        "sourcePath": str,
    },
    total=False,
)

InferenceAcceleratorOutputTypeDef = TypedDict(
    "InferenceAcceleratorOutputTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
)

InferenceAcceleratorOverrideOutputTypeDef = TypedDict(
    "InferenceAcceleratorOverrideOutputTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
    total=False,
)

InferenceAcceleratorOverrideTypeDef = TypedDict(
    "InferenceAcceleratorOverrideTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
    total=False,
)

InferenceAcceleratorTypeDef = TypedDict(
    "InferenceAcceleratorTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
)

KernelCapabilitiesOutputTypeDef = TypedDict(
    "KernelCapabilitiesOutputTypeDef",
    {
        "add": List[str],
        "drop": List[str],
    },
    total=False,
)

KernelCapabilitiesTypeDef = TypedDict(
    "KernelCapabilitiesTypeDef",
    {
        "add": Sequence[str],
        "drop": Sequence[str],
    },
    total=False,
)

_RequiredTmpfsOutputTypeDef = TypedDict(
    "_RequiredTmpfsOutputTypeDef",
    {
        "containerPath": str,
        "size": int,
    },
)
_OptionalTmpfsOutputTypeDef = TypedDict(
    "_OptionalTmpfsOutputTypeDef",
    {
        "mountOptions": List[str],
    },
    total=False,
)

class TmpfsOutputTypeDef(_RequiredTmpfsOutputTypeDef, _OptionalTmpfsOutputTypeDef):
    pass

_RequiredTmpfsTypeDef = TypedDict(
    "_RequiredTmpfsTypeDef",
    {
        "containerPath": str,
        "size": int,
    },
)
_OptionalTmpfsTypeDef = TypedDict(
    "_OptionalTmpfsTypeDef",
    {
        "mountOptions": Sequence[str],
    },
    total=False,
)

class TmpfsTypeDef(_RequiredTmpfsTypeDef, _OptionalTmpfsTypeDef):
    pass

ListAccountSettingsRequestListAccountSettingsPaginateTypeDef = TypedDict(
    "ListAccountSettingsRequestListAccountSettingsPaginateTypeDef",
    {
        "name": SettingNameType,
        "value": str,
        "principalArn": str,
        "effectiveSettings": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListAccountSettingsRequestRequestTypeDef = TypedDict(
    "ListAccountSettingsRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
        "principalArn": str,
        "effectiveSettings": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListAttributesRequestListAttributesPaginateTypeDef = TypedDict(
    "_RequiredListAttributesRequestListAttributesPaginateTypeDef",
    {
        "targetType": Literal["container-instance"],
    },
)
_OptionalListAttributesRequestListAttributesPaginateTypeDef = TypedDict(
    "_OptionalListAttributesRequestListAttributesPaginateTypeDef",
    {
        "cluster": str,
        "attributeName": str,
        "attributeValue": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListAttributesRequestListAttributesPaginateTypeDef(
    _RequiredListAttributesRequestListAttributesPaginateTypeDef,
    _OptionalListAttributesRequestListAttributesPaginateTypeDef,
):
    pass

_RequiredListAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttributesRequestRequestTypeDef",
    {
        "targetType": Literal["container-instance"],
    },
)
_OptionalListAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttributesRequestRequestTypeDef",
    {
        "cluster": str,
        "attributeName": str,
        "attributeValue": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAttributesRequestRequestTypeDef(
    _RequiredListAttributesRequestRequestTypeDef, _OptionalListAttributesRequestRequestTypeDef
):
    pass

ListClustersRequestListClustersPaginateTypeDef = TypedDict(
    "ListClustersRequestListClustersPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "clusterArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainerInstancesRequestListContainerInstancesPaginateTypeDef = TypedDict(
    "ListContainerInstancesRequestListContainerInstancesPaginateTypeDef",
    {
        "cluster": str,
        "filter": str,
        "status": ContainerInstanceStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListContainerInstancesRequestRequestTypeDef = TypedDict(
    "ListContainerInstancesRequestRequestTypeDef",
    {
        "cluster": str,
        "filter": str,
        "nextToken": str,
        "maxResults": int,
        "status": ContainerInstanceStatusType,
    },
    total=False,
)

ListContainerInstancesResponseTypeDef = TypedDict(
    "ListContainerInstancesResponseTypeDef",
    {
        "containerInstanceArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef = TypedDict(
    "_RequiredListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef",
    {
        "namespace": str,
    },
)
_OptionalListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef = TypedDict(
    "_OptionalListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef(
    _RequiredListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef,
    _OptionalListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef,
):
    pass

_RequiredListServicesByNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredListServicesByNamespaceRequestRequestTypeDef",
    {
        "namespace": str,
    },
)
_OptionalListServicesByNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalListServicesByNamespaceRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListServicesByNamespaceRequestRequestTypeDef(
    _RequiredListServicesByNamespaceRequestRequestTypeDef,
    _OptionalListServicesByNamespaceRequestRequestTypeDef,
):
    pass

ListServicesByNamespaceResponseTypeDef = TypedDict(
    "ListServicesByNamespaceResponseTypeDef",
    {
        "serviceArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestListServicesPaginateTypeDef = TypedDict(
    "ListServicesRequestListServicesPaginateTypeDef",
    {
        "cluster": str,
        "launchType": LaunchTypeType,
        "schedulingStrategy": SchedulingStrategyType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "cluster": str,
        "nextToken": str,
        "maxResults": int,
        "launchType": LaunchTypeType,
        "schedulingStrategy": SchedulingStrategyType,
    },
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "serviceArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTaskDefinitionFamiliesRequestListTaskDefinitionFamiliesPaginateTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesRequestListTaskDefinitionFamiliesPaginateTypeDef",
    {
        "familyPrefix": str,
        "status": TaskDefinitionFamilyStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTaskDefinitionFamiliesRequestRequestTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesRequestRequestTypeDef",
    {
        "familyPrefix": str,
        "status": TaskDefinitionFamilyStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTaskDefinitionFamiliesResponseTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesResponseTypeDef",
    {
        "families": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskDefinitionsRequestListTaskDefinitionsPaginateTypeDef = TypedDict(
    "ListTaskDefinitionsRequestListTaskDefinitionsPaginateTypeDef",
    {
        "familyPrefix": str,
        "status": TaskDefinitionStatusType,
        "sort": SortOrderType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTaskDefinitionsRequestRequestTypeDef = TypedDict(
    "ListTaskDefinitionsRequestRequestTypeDef",
    {
        "familyPrefix": str,
        "status": TaskDefinitionStatusType,
        "sort": SortOrderType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTaskDefinitionsResponseTypeDef = TypedDict(
    "ListTaskDefinitionsResponseTypeDef",
    {
        "taskDefinitionArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksRequestListTasksPaginateTypeDef = TypedDict(
    "ListTasksRequestListTasksPaginateTypeDef",
    {
        "cluster": str,
        "containerInstance": str,
        "family": str,
        "startedBy": str,
        "serviceName": str,
        "desiredStatus": DesiredStatusType,
        "launchType": LaunchTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTasksRequestRequestTypeDef = TypedDict(
    "ListTasksRequestRequestTypeDef",
    {
        "cluster": str,
        "containerInstance": str,
        "family": str,
        "nextToken": str,
        "maxResults": int,
        "startedBy": str,
        "serviceName": str,
        "desiredStatus": DesiredStatusType,
        "launchType": LaunchTypeType,
    },
    total=False,
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {
        "taskArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancerOutputTypeDef = TypedDict(
    "LoadBalancerOutputTypeDef",
    {
        "targetGroupArn": str,
        "loadBalancerName": str,
        "containerName": str,
        "containerPort": int,
    },
    total=False,
)

_RequiredManagedAgentStateChangeTypeDef = TypedDict(
    "_RequiredManagedAgentStateChangeTypeDef",
    {
        "containerName": str,
        "managedAgentName": Literal["ExecuteCommandAgent"],
        "status": str,
    },
)
_OptionalManagedAgentStateChangeTypeDef = TypedDict(
    "_OptionalManagedAgentStateChangeTypeDef",
    {
        "reason": str,
    },
    total=False,
)

class ManagedAgentStateChangeTypeDef(
    _RequiredManagedAgentStateChangeTypeDef, _OptionalManagedAgentStateChangeTypeDef
):
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

PlacementConstraintOutputTypeDef = TypedDict(
    "PlacementConstraintOutputTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyOutputTypeDef = TypedDict(
    "PlacementStrategyOutputTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
    },
    total=False,
)

PlatformDeviceTypeDef = TypedDict(
    "PlatformDeviceTypeDef",
    {
        "id": str,
        "type": Literal["GPU"],
    },
)

PutAccountSettingDefaultRequestRequestTypeDef = TypedDict(
    "PutAccountSettingDefaultRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
    },
)

_RequiredPutAccountSettingRequestRequestTypeDef = TypedDict(
    "_RequiredPutAccountSettingRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
    },
)
_OptionalPutAccountSettingRequestRequestTypeDef = TypedDict(
    "_OptionalPutAccountSettingRequestRequestTypeDef",
    {
        "principalArn": str,
    },
    total=False,
)

class PutAccountSettingRequestRequestTypeDef(
    _RequiredPutAccountSettingRequestRequestTypeDef, _OptionalPutAccountSettingRequestRequestTypeDef
):
    pass

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": Sequence[str],
    },
    total=False,
)

VersionInfoTypeDef = TypedDict(
    "VersionInfoTypeDef",
    {
        "agentVersion": str,
        "agentHash": str,
        "dockerVersion": str,
    },
    total=False,
)

RuntimePlatformTypeDef = TypedDict(
    "RuntimePlatformTypeDef",
    {
        "cpuArchitecture": CPUArchitectureType,
        "operatingSystemFamily": OSFamilyType,
    },
    total=False,
)

TaskDefinitionPlacementConstraintTypeDef = TypedDict(
    "TaskDefinitionPlacementConstraintTypeDef",
    {
        "type": Literal["memberOf"],
        "expression": str,
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

RuntimePlatformOutputTypeDef = TypedDict(
    "RuntimePlatformOutputTypeDef",
    {
        "cpuArchitecture": CPUArchitectureType,
        "operatingSystemFamily": OSFamilyType,
    },
    total=False,
)

ScaleOutputTypeDef = TypedDict(
    "ScaleOutputTypeDef",
    {
        "value": float,
        "unit": Literal["PERCENT"],
    },
    total=False,
)

_RequiredServiceConnectClientAliasOutputTypeDef = TypedDict(
    "_RequiredServiceConnectClientAliasOutputTypeDef",
    {
        "port": int,
    },
)
_OptionalServiceConnectClientAliasOutputTypeDef = TypedDict(
    "_OptionalServiceConnectClientAliasOutputTypeDef",
    {
        "dnsName": str,
    },
    total=False,
)

class ServiceConnectClientAliasOutputTypeDef(
    _RequiredServiceConnectClientAliasOutputTypeDef, _OptionalServiceConnectClientAliasOutputTypeDef
):
    pass

_RequiredServiceConnectClientAliasTypeDef = TypedDict(
    "_RequiredServiceConnectClientAliasTypeDef",
    {
        "port": int,
    },
)
_OptionalServiceConnectClientAliasTypeDef = TypedDict(
    "_OptionalServiceConnectClientAliasTypeDef",
    {
        "dnsName": str,
    },
    total=False,
)

class ServiceConnectClientAliasTypeDef(
    _RequiredServiceConnectClientAliasTypeDef, _OptionalServiceConnectClientAliasTypeDef
):
    pass

ServiceEventTypeDef = TypedDict(
    "ServiceEventTypeDef",
    {
        "id": str,
        "createdAt": datetime,
        "message": str,
    },
    total=False,
)

ServiceRegistryOutputTypeDef = TypedDict(
    "ServiceRegistryOutputTypeDef",
    {
        "registryArn": str,
        "port": int,
        "containerName": str,
        "containerPort": int,
    },
    total=False,
)

_RequiredStopTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStopTaskRequestRequestTypeDef",
    {
        "task": str,
    },
)
_OptionalStopTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStopTaskRequestRequestTypeDef",
    {
        "cluster": str,
        "reason": str,
    },
    total=False,
)

class StopTaskRequestRequestTypeDef(
    _RequiredStopTaskRequestRequestTypeDef, _OptionalStopTaskRequestRequestTypeDef
):
    pass

SubmitAttachmentStateChangesResponseTypeDef = TypedDict(
    "SubmitAttachmentStateChangesResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitContainerStateChangeResponseTypeDef = TypedDict(
    "SubmitContainerStateChangeResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitTaskStateChangeResponseTypeDef = TypedDict(
    "SubmitTaskStateChangeResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TaskDefinitionPlacementConstraintOutputTypeDef = TypedDict(
    "TaskDefinitionPlacementConstraintOutputTypeDef",
    {
        "type": Literal["memberOf"],
        "expression": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateContainerAgentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContainerAgentRequestRequestTypeDef",
    {
        "containerInstance": str,
    },
)
_OptionalUpdateContainerAgentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContainerAgentRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class UpdateContainerAgentRequestRequestTypeDef(
    _RequiredUpdateContainerAgentRequestRequestTypeDef,
    _OptionalUpdateContainerAgentRequestRequestTypeDef,
):
    pass

_RequiredUpdateContainerInstancesStateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContainerInstancesStateRequestRequestTypeDef",
    {
        "containerInstances": Sequence[str],
        "status": ContainerInstanceStatusType,
    },
)
_OptionalUpdateContainerInstancesStateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContainerInstancesStateRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class UpdateContainerInstancesStateRequestRequestTypeDef(
    _RequiredUpdateContainerInstancesStateRequestRequestTypeDef,
    _OptionalUpdateContainerInstancesStateRequestRequestTypeDef,
):
    pass

UpdateServicePrimaryTaskSetRequestRequestTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "primaryTaskSet": str,
    },
)

_RequiredUpdateTaskProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTaskProtectionRequestRequestTypeDef",
    {
        "cluster": str,
        "tasks": Sequence[str],
        "protectionEnabled": bool,
    },
)
_OptionalUpdateTaskProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTaskProtectionRequestRequestTypeDef",
    {
        "expiresInMinutes": int,
    },
    total=False,
)

class UpdateTaskProtectionRequestRequestTypeDef(
    _RequiredUpdateTaskProtectionRequestRequestTypeDef,
    _OptionalUpdateTaskProtectionRequestRequestTypeDef,
):
    pass

_RequiredSubmitAttachmentStateChangesRequestRequestTypeDef = TypedDict(
    "_RequiredSubmitAttachmentStateChangesRequestRequestTypeDef",
    {
        "attachments": Sequence[AttachmentStateChangeTypeDef],
    },
)
_OptionalSubmitAttachmentStateChangesRequestRequestTypeDef = TypedDict(
    "_OptionalSubmitAttachmentStateChangesRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class SubmitAttachmentStateChangesRequestRequestTypeDef(
    _RequiredSubmitAttachmentStateChangesRequestRequestTypeDef,
    _OptionalSubmitAttachmentStateChangesRequestRequestTypeDef,
):
    pass

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[KeyValuePairOutputTypeDef],
    },
    total=False,
)

_RequiredProxyConfigurationOutputTypeDef = TypedDict(
    "_RequiredProxyConfigurationOutputTypeDef",
    {
        "containerName": str,
    },
)
_OptionalProxyConfigurationOutputTypeDef = TypedDict(
    "_OptionalProxyConfigurationOutputTypeDef",
    {
        "type": Literal["APPMESH"],
        "properties": List[KeyValuePairOutputTypeDef],
    },
    total=False,
)

class ProxyConfigurationOutputTypeDef(
    _RequiredProxyConfigurationOutputTypeDef, _OptionalProxyConfigurationOutputTypeDef
):
    pass

DeleteAttributesResponseTypeDef = TypedDict(
    "DeleteAttributesResponseTypeDef",
    {
        "attributes": List[AttributeOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttributesResponseTypeDef = TypedDict(
    "ListAttributesResponseTypeDef",
    {
        "attributes": List[AttributeOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAttributesResponseTypeDef = TypedDict(
    "PutAttributesResponseTypeDef",
    {
        "attributes": List[AttributeOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAttributesRequestRequestTypeDef",
    {
        "attributes": Sequence[AttributeTypeDef],
    },
)
_OptionalDeleteAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAttributesRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class DeleteAttributesRequestRequestTypeDef(
    _RequiredDeleteAttributesRequestRequestTypeDef, _OptionalDeleteAttributesRequestRequestTypeDef
):
    pass

_RequiredPutAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutAttributesRequestRequestTypeDef",
    {
        "attributes": Sequence[AttributeTypeDef],
    },
)
_OptionalPutAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutAttributesRequestRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)

class PutAttributesRequestRequestTypeDef(
    _RequiredPutAttributesRequestRequestTypeDef, _OptionalPutAttributesRequestRequestTypeDef
):
    pass

_RequiredAutoScalingGroupProviderOutputTypeDef = TypedDict(
    "_RequiredAutoScalingGroupProviderOutputTypeDef",
    {
        "autoScalingGroupArn": str,
    },
)
_OptionalAutoScalingGroupProviderOutputTypeDef = TypedDict(
    "_OptionalAutoScalingGroupProviderOutputTypeDef",
    {
        "managedScaling": ManagedScalingOutputTypeDef,
        "managedTerminationProtection": ManagedTerminationProtectionType,
    },
    total=False,
)

class AutoScalingGroupProviderOutputTypeDef(
    _RequiredAutoScalingGroupProviderOutputTypeDef, _OptionalAutoScalingGroupProviderOutputTypeDef
):
    pass

_RequiredAutoScalingGroupProviderTypeDef = TypedDict(
    "_RequiredAutoScalingGroupProviderTypeDef",
    {
        "autoScalingGroupArn": str,
    },
)
_OptionalAutoScalingGroupProviderTypeDef = TypedDict(
    "_OptionalAutoScalingGroupProviderTypeDef",
    {
        "managedScaling": ManagedScalingTypeDef,
        "managedTerminationProtection": ManagedTerminationProtectionType,
    },
    total=False,
)

class AutoScalingGroupProviderTypeDef(
    _RequiredAutoScalingGroupProviderTypeDef, _OptionalAutoScalingGroupProviderTypeDef
):
    pass

AutoScalingGroupProviderUpdateTypeDef = TypedDict(
    "AutoScalingGroupProviderUpdateTypeDef",
    {
        "managedScaling": ManagedScalingTypeDef,
        "managedTerminationProtection": ManagedTerminationProtectionType,
    },
    total=False,
)

NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "awsvpcConfiguration": AwsVpcConfigurationOutputTypeDef,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": AwsVpcConfigurationTypeDef,
    },
    total=False,
)

PutClusterCapacityProvidersRequestRequestTypeDef = TypedDict(
    "PutClusterCapacityProvidersRequestRequestTypeDef",
    {
        "cluster": str,
        "capacityProviders": Sequence[str],
        "defaultCapacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterSettingsRequestRequestTypeDef = TypedDict(
    "UpdateClusterSettingsRequestRequestTypeDef",
    {
        "cluster": str,
        "settings": Sequence[ClusterSettingTypeDef],
    },
)

ContainerOverrideOutputTypeDef = TypedDict(
    "ContainerOverrideOutputTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[KeyValuePairOutputTypeDef],
        "environmentFiles": List[EnvironmentFileOutputTypeDef],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[ResourceRequirementOutputTypeDef],
    },
    total=False,
)

_RequiredLogConfigurationOutputTypeDef = TypedDict(
    "_RequiredLogConfigurationOutputTypeDef",
    {
        "logDriver": LogDriverType,
    },
)
_OptionalLogConfigurationOutputTypeDef = TypedDict(
    "_OptionalLogConfigurationOutputTypeDef",
    {
        "options": Dict[str, str],
        "secretOptions": List[SecretOutputTypeDef],
    },
    total=False,
)

class LogConfigurationOutputTypeDef(
    _RequiredLogConfigurationOutputTypeDef, _OptionalLogConfigurationOutputTypeDef
):
    pass

_RequiredProxyConfigurationTypeDef = TypedDict(
    "_RequiredProxyConfigurationTypeDef",
    {
        "containerName": str,
    },
)
_OptionalProxyConfigurationTypeDef = TypedDict(
    "_OptionalProxyConfigurationTypeDef",
    {
        "type": Literal["APPMESH"],
        "properties": Sequence[KeyValuePairTypeDef],
    },
    total=False,
)

class ProxyConfigurationTypeDef(
    _RequiredProxyConfigurationTypeDef, _OptionalProxyConfigurationTypeDef
):
    pass

ContainerOverrideTypeDef = TypedDict(
    "ContainerOverrideTypeDef",
    {
        "name": str,
        "command": Sequence[str],
        "environment": Sequence[KeyValuePairTypeDef],
        "environmentFiles": Sequence[EnvironmentFileTypeDef],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": Sequence[ResourceRequirementTypeDef],
    },
    total=False,
)

_RequiredLogConfigurationTypeDef = TypedDict(
    "_RequiredLogConfigurationTypeDef",
    {
        "logDriver": LogDriverType,
    },
)
_OptionalLogConfigurationTypeDef = TypedDict(
    "_OptionalLogConfigurationTypeDef",
    {
        "options": Mapping[str, str],
        "secretOptions": Sequence[SecretTypeDef],
    },
    total=False,
)

class LogConfigurationTypeDef(_RequiredLogConfigurationTypeDef, _OptionalLogConfigurationTypeDef):
    pass

ContainerInstanceHealthStatusTypeDef = TypedDict(
    "ContainerInstanceHealthStatusTypeDef",
    {
        "overallStatus": InstanceHealthCheckStateType,
        "details": List[InstanceHealthCheckResultTypeDef],
    },
    total=False,
)

ContainerStateChangeTypeDef = TypedDict(
    "ContainerStateChangeTypeDef",
    {
        "containerName": str,
        "imageDigest": str,
        "runtimeId": str,
        "exitCode": int,
        "networkBindings": Sequence[NetworkBindingTypeDef],
        "reason": str,
        "status": str,
    },
    total=False,
)

SubmitContainerStateChangeRequestRequestTypeDef = TypedDict(
    "SubmitContainerStateChangeRequestRequestTypeDef",
    {
        "cluster": str,
        "task": str,
        "containerName": str,
        "runtimeId": str,
        "status": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": Sequence[NetworkBindingTypeDef],
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[NetworkBindingOutputTypeDef],
        "networkInterfaces": List[NetworkInterfaceTypeDef],
        "healthStatus": HealthStatusType,
        "managedAgents": List[ManagedAgentTypeDef],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

UpdateTaskSetRequestRequestTypeDef = TypedDict(
    "UpdateTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSet": str,
        "scale": ScaleTypeDef,
    },
)

DeleteAccountSettingResponseTypeDef = TypedDict(
    "DeleteAccountSettingResponseTypeDef",
    {
        "setting": SettingTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountSettingsResponseTypeDef = TypedDict(
    "ListAccountSettingsResponseTypeDef",
    {
        "settings": List[SettingTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAccountSettingDefaultResponseTypeDef = TypedDict(
    "PutAccountSettingDefaultResponseTypeDef",
    {
        "setting": SettingTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAccountSettingResponseTypeDef = TypedDict(
    "PutAccountSettingResponseTypeDef",
    {
        "setting": SettingTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentConfigurationOutputTypeDef = TypedDict(
    "DeploymentConfigurationOutputTypeDef",
    {
        "deploymentCircuitBreaker": DeploymentCircuitBreakerOutputTypeDef,
        "maximumPercent": int,
        "minimumHealthyPercent": int,
        "alarms": DeploymentAlarmsOutputTypeDef,
    },
    total=False,
)

DeploymentConfigurationTypeDef = TypedDict(
    "DeploymentConfigurationTypeDef",
    {
        "deploymentCircuitBreaker": DeploymentCircuitBreakerTypeDef,
        "maximumPercent": int,
        "minimumHealthyPercent": int,
        "alarms": DeploymentAlarmsTypeDef,
    },
    total=False,
)

_RequiredDescribeServicesRequestServicesInactiveWaitTypeDef = TypedDict(
    "_RequiredDescribeServicesRequestServicesInactiveWaitTypeDef",
    {
        "services": Sequence[str],
    },
)
_OptionalDescribeServicesRequestServicesInactiveWaitTypeDef = TypedDict(
    "_OptionalDescribeServicesRequestServicesInactiveWaitTypeDef",
    {
        "cluster": str,
        "include": Sequence[Literal["TAGS"]],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeServicesRequestServicesInactiveWaitTypeDef(
    _RequiredDescribeServicesRequestServicesInactiveWaitTypeDef,
    _OptionalDescribeServicesRequestServicesInactiveWaitTypeDef,
):
    pass

_RequiredDescribeServicesRequestServicesStableWaitTypeDef = TypedDict(
    "_RequiredDescribeServicesRequestServicesStableWaitTypeDef",
    {
        "services": Sequence[str],
    },
)
_OptionalDescribeServicesRequestServicesStableWaitTypeDef = TypedDict(
    "_OptionalDescribeServicesRequestServicesStableWaitTypeDef",
    {
        "cluster": str,
        "include": Sequence[Literal["TAGS"]],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeServicesRequestServicesStableWaitTypeDef(
    _RequiredDescribeServicesRequestServicesStableWaitTypeDef,
    _OptionalDescribeServicesRequestServicesStableWaitTypeDef,
):
    pass

_RequiredDescribeTasksRequestTasksRunningWaitTypeDef = TypedDict(
    "_RequiredDescribeTasksRequestTasksRunningWaitTypeDef",
    {
        "tasks": Sequence[str],
    },
)
_OptionalDescribeTasksRequestTasksRunningWaitTypeDef = TypedDict(
    "_OptionalDescribeTasksRequestTasksRunningWaitTypeDef",
    {
        "cluster": str,
        "include": Sequence[Literal["TAGS"]],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeTasksRequestTasksRunningWaitTypeDef(
    _RequiredDescribeTasksRequestTasksRunningWaitTypeDef,
    _OptionalDescribeTasksRequestTasksRunningWaitTypeDef,
):
    pass

_RequiredDescribeTasksRequestTasksStoppedWaitTypeDef = TypedDict(
    "_RequiredDescribeTasksRequestTasksStoppedWaitTypeDef",
    {
        "tasks": Sequence[str],
    },
)
_OptionalDescribeTasksRequestTasksStoppedWaitTypeDef = TypedDict(
    "_OptionalDescribeTasksRequestTasksStoppedWaitTypeDef",
    {
        "cluster": str,
        "include": Sequence[Literal["TAGS"]],
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeTasksRequestTasksStoppedWaitTypeDef(
    _RequiredDescribeTasksRequestTasksStoppedWaitTypeDef,
    _OptionalDescribeTasksRequestTasksStoppedWaitTypeDef,
):
    pass

_RequiredEFSVolumeConfigurationOutputTypeDef = TypedDict(
    "_RequiredEFSVolumeConfigurationOutputTypeDef",
    {
        "fileSystemId": str,
    },
)
_OptionalEFSVolumeConfigurationOutputTypeDef = TypedDict(
    "_OptionalEFSVolumeConfigurationOutputTypeDef",
    {
        "rootDirectory": str,
        "transitEncryption": EFSTransitEncryptionType,
        "transitEncryptionPort": int,
        "authorizationConfig": EFSAuthorizationConfigOutputTypeDef,
    },
    total=False,
)

class EFSVolumeConfigurationOutputTypeDef(
    _RequiredEFSVolumeConfigurationOutputTypeDef, _OptionalEFSVolumeConfigurationOutputTypeDef
):
    pass

_RequiredEFSVolumeConfigurationTypeDef = TypedDict(
    "_RequiredEFSVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
    },
)
_OptionalEFSVolumeConfigurationTypeDef = TypedDict(
    "_OptionalEFSVolumeConfigurationTypeDef",
    {
        "rootDirectory": str,
        "transitEncryption": EFSTransitEncryptionType,
        "transitEncryptionPort": int,
        "authorizationConfig": EFSAuthorizationConfigTypeDef,
    },
    total=False,
)

class EFSVolumeConfigurationTypeDef(
    _RequiredEFSVolumeConfigurationTypeDef, _OptionalEFSVolumeConfigurationTypeDef
):
    pass

ExecuteCommandConfigurationOutputTypeDef = TypedDict(
    "ExecuteCommandConfigurationOutputTypeDef",
    {
        "kmsKeyId": str,
        "logging": ExecuteCommandLoggingType,
        "logConfiguration": ExecuteCommandLogConfigurationOutputTypeDef,
    },
    total=False,
)

ExecuteCommandConfigurationTypeDef = TypedDict(
    "ExecuteCommandConfigurationTypeDef",
    {
        "kmsKeyId": str,
        "logging": ExecuteCommandLoggingType,
        "logConfiguration": ExecuteCommandLogConfigurationTypeDef,
    },
    total=False,
)

ExecuteCommandResponseTypeDef = TypedDict(
    "ExecuteCommandResponseTypeDef",
    {
        "clusterArn": str,
        "containerArn": str,
        "containerName": str,
        "interactive": bool,
        "session": SessionTypeDef,
        "taskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FSxWindowsFileServerVolumeConfigurationOutputTypeDef = TypedDict(
    "FSxWindowsFileServerVolumeConfigurationOutputTypeDef",
    {
        "fileSystemId": str,
        "rootDirectory": str,
        "authorizationConfig": FSxWindowsFileServerAuthorizationConfigOutputTypeDef,
    },
)

FSxWindowsFileServerVolumeConfigurationTypeDef = TypedDict(
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
        "rootDirectory": str,
        "authorizationConfig": FSxWindowsFileServerAuthorizationConfigTypeDef,
    },
)

GetTaskProtectionResponseTypeDef = TypedDict(
    "GetTaskProtectionResponseTypeDef",
    {
        "protectedTasks": List[ProtectedTaskTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTaskProtectionResponseTypeDef = TypedDict(
    "UpdateTaskProtectionResponseTypeDef",
    {
        "protectedTasks": List[ProtectedTaskTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LinuxParametersOutputTypeDef = TypedDict(
    "LinuxParametersOutputTypeDef",
    {
        "capabilities": KernelCapabilitiesOutputTypeDef,
        "devices": List[DeviceOutputTypeDef],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[TmpfsOutputTypeDef],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "capabilities": KernelCapabilitiesTypeDef,
        "devices": Sequence[DeviceTypeDef],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": Sequence[TmpfsTypeDef],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

RegisterContainerInstanceRequestRequestTypeDef = TypedDict(
    "RegisterContainerInstanceRequestRequestTypeDef",
    {
        "cluster": str,
        "instanceIdentityDocument": str,
        "instanceIdentityDocumentSignature": str,
        "totalResources": Sequence[ResourceTypeDef],
        "versionInfo": VersionInfoTypeDef,
        "containerInstanceArn": str,
        "attributes": Sequence[AttributeTypeDef],
        "platformDevices": Sequence[PlatformDeviceTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

_RequiredServiceConnectServiceOutputTypeDef = TypedDict(
    "_RequiredServiceConnectServiceOutputTypeDef",
    {
        "portName": str,
    },
)
_OptionalServiceConnectServiceOutputTypeDef = TypedDict(
    "_OptionalServiceConnectServiceOutputTypeDef",
    {
        "discoveryName": str,
        "clientAliases": List[ServiceConnectClientAliasOutputTypeDef],
        "ingressPortOverride": int,
    },
    total=False,
)

class ServiceConnectServiceOutputTypeDef(
    _RequiredServiceConnectServiceOutputTypeDef, _OptionalServiceConnectServiceOutputTypeDef
):
    pass

_RequiredServiceConnectServiceTypeDef = TypedDict(
    "_RequiredServiceConnectServiceTypeDef",
    {
        "portName": str,
    },
)
_OptionalServiceConnectServiceTypeDef = TypedDict(
    "_OptionalServiceConnectServiceTypeDef",
    {
        "discoveryName": str,
        "clientAliases": Sequence[ServiceConnectClientAliasTypeDef],
        "ingressPortOverride": int,
    },
    total=False,
)

class ServiceConnectServiceTypeDef(
    _RequiredServiceConnectServiceTypeDef, _OptionalServiceConnectServiceTypeDef
):
    pass

CapacityProviderTypeDef = TypedDict(
    "CapacityProviderTypeDef",
    {
        "capacityProviderArn": str,
        "name": str,
        "status": CapacityProviderStatusType,
        "autoScalingGroupProvider": AutoScalingGroupProviderOutputTypeDef,
        "updateStatus": CapacityProviderUpdateStatusType,
        "updateStatusReason": str,
        "tags": List[TagOutputTypeDef],
    },
    total=False,
)

_RequiredCreateCapacityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCapacityProviderRequestRequestTypeDef",
    {
        "name": str,
        "autoScalingGroupProvider": AutoScalingGroupProviderTypeDef,
    },
)
_OptionalCreateCapacityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCapacityProviderRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateCapacityProviderRequestRequestTypeDef(
    _RequiredCreateCapacityProviderRequestRequestTypeDef,
    _OptionalCreateCapacityProviderRequestRequestTypeDef,
):
    pass

UpdateCapacityProviderRequestRequestTypeDef = TypedDict(
    "UpdateCapacityProviderRequestRequestTypeDef",
    {
        "name": str,
        "autoScalingGroupProvider": AutoScalingGroupProviderUpdateTypeDef,
    },
)

TaskSetTypeDef = TypedDict(
    "TaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List[CapacityProviderStrategyItemOutputTypeDef],
        "platformVersion": str,
        "platformFamily": str,
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "loadBalancers": List[LoadBalancerOutputTypeDef],
        "serviceRegistries": List[ServiceRegistryOutputTypeDef],
        "scale": ScaleOutputTypeDef,
        "stabilityStatus": StabilityStatusType,
        "stabilityStatusAt": datetime,
        "tags": List[TagOutputTypeDef],
    },
    total=False,
)

_RequiredCreateTaskSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTaskSetRequestRequestTypeDef",
    {
        "service": str,
        "cluster": str,
        "taskDefinition": str,
    },
)
_OptionalCreateTaskSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTaskSetRequestRequestTypeDef",
    {
        "externalId": str,
        "networkConfiguration": NetworkConfigurationTypeDef,
        "loadBalancers": Sequence[LoadBalancerTypeDef],
        "serviceRegistries": Sequence[ServiceRegistryTypeDef],
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
        "platformVersion": str,
        "scale": ScaleTypeDef,
        "clientToken": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateTaskSetRequestRequestTypeDef(
    _RequiredCreateTaskSetRequestRequestTypeDef, _OptionalCreateTaskSetRequestRequestTypeDef
):
    pass

TaskOverrideOutputTypeDef = TypedDict(
    "TaskOverrideOutputTypeDef",
    {
        "containerOverrides": List[ContainerOverrideOutputTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[InferenceAcceleratorOverrideOutputTypeDef],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
        "ephemeralStorage": EphemeralStorageOutputTypeDef,
    },
    total=False,
)

TaskOverrideTypeDef = TypedDict(
    "TaskOverrideTypeDef",
    {
        "containerOverrides": Sequence[ContainerOverrideTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": Sequence[InferenceAcceleratorOverrideTypeDef],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
        "ephemeralStorage": EphemeralStorageTypeDef,
    },
    total=False,
)

ContainerInstanceTypeDef = TypedDict(
    "ContainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": VersionInfoOutputTypeDef,
        "remainingResources": List[ResourceOutputTypeDef],
        "registeredResources": List[ResourceOutputTypeDef],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": AgentUpdateStatusType,
        "attributes": List[AttributeOutputTypeDef],
        "registeredAt": datetime,
        "attachments": List[AttachmentTypeDef],
        "tags": List[TagOutputTypeDef],
        "healthStatus": ContainerInstanceHealthStatusTypeDef,
    },
    total=False,
)

SubmitTaskStateChangeRequestRequestTypeDef = TypedDict(
    "SubmitTaskStateChangeRequestRequestTypeDef",
    {
        "cluster": str,
        "task": str,
        "status": str,
        "reason": str,
        "containers": Sequence[ContainerStateChangeTypeDef],
        "attachments": Sequence[AttachmentStateChangeTypeDef],
        "managedAgents": Sequence[ManagedAgentStateChangeTypeDef],
        "pullStartedAt": Union[datetime, str],
        "pullStoppedAt": Union[datetime, str],
        "executionStoppedAt": Union[datetime, str],
    },
    total=False,
)

ClusterConfigurationOutputTypeDef = TypedDict(
    "ClusterConfigurationOutputTypeDef",
    {
        "executeCommandConfiguration": ExecuteCommandConfigurationOutputTypeDef,
    },
    total=False,
)

ClusterConfigurationTypeDef = TypedDict(
    "ClusterConfigurationTypeDef",
    {
        "executeCommandConfiguration": ExecuteCommandConfigurationTypeDef,
    },
    total=False,
)

VolumeOutputTypeDef = TypedDict(
    "VolumeOutputTypeDef",
    {
        "name": str,
        "host": HostVolumePropertiesOutputTypeDef,
        "dockerVolumeConfiguration": DockerVolumeConfigurationOutputTypeDef,
        "efsVolumeConfiguration": EFSVolumeConfigurationOutputTypeDef,
        "fsxWindowsFileServerVolumeConfiguration": (
            FSxWindowsFileServerVolumeConfigurationOutputTypeDef
        ),
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "name": str,
        "host": HostVolumePropertiesTypeDef,
        "dockerVolumeConfiguration": DockerVolumeConfigurationTypeDef,
        "efsVolumeConfiguration": EFSVolumeConfigurationTypeDef,
        "fsxWindowsFileServerVolumeConfiguration": FSxWindowsFileServerVolumeConfigurationTypeDef,
    },
    total=False,
)

ContainerDefinitionOutputTypeDef = TypedDict(
    "ContainerDefinitionOutputTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": RepositoryCredentialsOutputTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[PortMappingOutputTypeDef],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[KeyValuePairOutputTypeDef],
        "environmentFiles": List[EnvironmentFileOutputTypeDef],
        "mountPoints": List[MountPointOutputTypeDef],
        "volumesFrom": List[VolumeFromOutputTypeDef],
        "linuxParameters": LinuxParametersOutputTypeDef,
        "secrets": List[SecretOutputTypeDef],
        "dependsOn": List[ContainerDependencyOutputTypeDef],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[HostEntryOutputTypeDef],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[UlimitOutputTypeDef],
        "logConfiguration": LogConfigurationOutputTypeDef,
        "healthCheck": HealthCheckOutputTypeDef,
        "systemControls": List[SystemControlOutputTypeDef],
        "resourceRequirements": List[ResourceRequirementOutputTypeDef],
        "firelensConfiguration": FirelensConfigurationOutputTypeDef,
        "credentialSpecs": List[str],
    },
    total=False,
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": RepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": Sequence[str],
        "portMappings": Sequence[PortMappingTypeDef],
        "essential": bool,
        "entryPoint": Sequence[str],
        "command": Sequence[str],
        "environment": Sequence[KeyValuePairTypeDef],
        "environmentFiles": Sequence[EnvironmentFileTypeDef],
        "mountPoints": Sequence[MountPointTypeDef],
        "volumesFrom": Sequence[VolumeFromTypeDef],
        "linuxParameters": LinuxParametersTypeDef,
        "secrets": Sequence[SecretTypeDef],
        "dependsOn": Sequence[ContainerDependencyTypeDef],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": Sequence[str],
        "dnsSearchDomains": Sequence[str],
        "extraHosts": Sequence[HostEntryTypeDef],
        "dockerSecurityOptions": Sequence[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Mapping[str, str],
        "ulimits": Sequence[UlimitTypeDef],
        "logConfiguration": LogConfigurationTypeDef,
        "healthCheck": HealthCheckTypeDef,
        "systemControls": Sequence[SystemControlTypeDef],
        "resourceRequirements": Sequence[ResourceRequirementTypeDef],
        "firelensConfiguration": FirelensConfigurationTypeDef,
        "credentialSpecs": Sequence[str],
    },
    total=False,
)

_RequiredServiceConnectConfigurationOutputTypeDef = TypedDict(
    "_RequiredServiceConnectConfigurationOutputTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalServiceConnectConfigurationOutputTypeDef = TypedDict(
    "_OptionalServiceConnectConfigurationOutputTypeDef",
    {
        "namespace": str,
        "services": List[ServiceConnectServiceOutputTypeDef],
        "logConfiguration": LogConfigurationOutputTypeDef,
    },
    total=False,
)

class ServiceConnectConfigurationOutputTypeDef(
    _RequiredServiceConnectConfigurationOutputTypeDef,
    _OptionalServiceConnectConfigurationOutputTypeDef,
):
    pass

_RequiredServiceConnectConfigurationTypeDef = TypedDict(
    "_RequiredServiceConnectConfigurationTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalServiceConnectConfigurationTypeDef = TypedDict(
    "_OptionalServiceConnectConfigurationTypeDef",
    {
        "namespace": str,
        "services": Sequence[ServiceConnectServiceTypeDef],
        "logConfiguration": LogConfigurationTypeDef,
    },
    total=False,
)

class ServiceConnectConfigurationTypeDef(
    _RequiredServiceConnectConfigurationTypeDef, _OptionalServiceConnectConfigurationTypeDef
):
    pass

CreateCapacityProviderResponseTypeDef = TypedDict(
    "CreateCapacityProviderResponseTypeDef",
    {
        "capacityProvider": CapacityProviderTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCapacityProviderResponseTypeDef = TypedDict(
    "DeleteCapacityProviderResponseTypeDef",
    {
        "capacityProvider": CapacityProviderTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityProvidersResponseTypeDef = TypedDict(
    "DescribeCapacityProvidersResponseTypeDef",
    {
        "capacityProviders": List[CapacityProviderTypeDef],
        "failures": List[FailureTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCapacityProviderResponseTypeDef = TypedDict(
    "UpdateCapacityProviderResponseTypeDef",
    {
        "capacityProvider": CapacityProviderTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTaskSetResponseTypeDef = TypedDict(
    "CreateTaskSetResponseTypeDef",
    {
        "taskSet": TaskSetTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTaskSetResponseTypeDef = TypedDict(
    "DeleteTaskSetResponseTypeDef",
    {
        "taskSet": TaskSetTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskSetsResponseTypeDef = TypedDict(
    "DescribeTaskSetsResponseTypeDef",
    {
        "taskSets": List[TaskSetTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServicePrimaryTaskSetResponseTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    {
        "taskSet": TaskSetTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTaskSetResponseTypeDef = TypedDict(
    "UpdateTaskSetResponseTypeDef",
    {
        "taskSet": TaskSetTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "attachments": List[AttachmentTypeDef],
        "attributes": List[AttributeOutputTypeDef],
        "availabilityZone": str,
        "capacityProviderName": str,
        "clusterArn": str,
        "connectivity": ConnectivityType,
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ContainerTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "enableExecuteCommand": bool,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": HealthStatusType,
        "inferenceAccelerators": List[InferenceAcceleratorOutputTypeDef],
        "lastStatus": str,
        "launchType": LaunchTypeType,
        "memory": str,
        "overrides": TaskOverrideOutputTypeDef,
        "platformVersion": str,
        "platformFamily": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": TaskStopCodeType,
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[TagOutputTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
        "ephemeralStorage": EphemeralStorageOutputTypeDef,
    },
    total=False,
)

_RequiredRunTaskRequestRequestTypeDef = TypedDict(
    "_RequiredRunTaskRequestRequestTypeDef",
    {
        "taskDefinition": str,
    },
)
_OptionalRunTaskRequestRequestTypeDef = TypedDict(
    "_OptionalRunTaskRequestRequestTypeDef",
    {
        "capacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
        "cluster": str,
        "count": int,
        "enableECSManagedTags": bool,
        "enableExecuteCommand": bool,
        "group": str,
        "launchType": LaunchTypeType,
        "networkConfiguration": NetworkConfigurationTypeDef,
        "overrides": TaskOverrideTypeDef,
        "placementConstraints": Sequence[PlacementConstraintTypeDef],
        "placementStrategy": Sequence[PlacementStrategyTypeDef],
        "platformVersion": str,
        "propagateTags": PropagateTagsType,
        "referenceId": str,
        "startedBy": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class RunTaskRequestRequestTypeDef(
    _RequiredRunTaskRequestRequestTypeDef, _OptionalRunTaskRequestRequestTypeDef
):
    pass

_RequiredStartTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartTaskRequestRequestTypeDef",
    {
        "containerInstances": Sequence[str],
        "taskDefinition": str,
    },
)
_OptionalStartTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartTaskRequestRequestTypeDef",
    {
        "cluster": str,
        "enableECSManagedTags": bool,
        "enableExecuteCommand": bool,
        "group": str,
        "networkConfiguration": NetworkConfigurationTypeDef,
        "overrides": TaskOverrideTypeDef,
        "propagateTags": PropagateTagsType,
        "referenceId": str,
        "startedBy": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class StartTaskRequestRequestTypeDef(
    _RequiredStartTaskRequestRequestTypeDef, _OptionalStartTaskRequestRequestTypeDef
):
    pass

DeregisterContainerInstanceResponseTypeDef = TypedDict(
    "DeregisterContainerInstanceResponseTypeDef",
    {
        "containerInstance": ContainerInstanceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContainerInstancesResponseTypeDef = TypedDict(
    "DescribeContainerInstancesResponseTypeDef",
    {
        "containerInstances": List[ContainerInstanceTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterContainerInstanceResponseTypeDef = TypedDict(
    "RegisterContainerInstanceResponseTypeDef",
    {
        "containerInstance": ContainerInstanceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContainerAgentResponseTypeDef = TypedDict(
    "UpdateContainerAgentResponseTypeDef",
    {
        "containerInstance": ContainerInstanceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContainerInstancesStateResponseTypeDef = TypedDict(
    "UpdateContainerInstancesStateResponseTypeDef",
    {
        "containerInstances": List[ContainerInstanceTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "configuration": ClusterConfigurationOutputTypeDef,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[KeyValuePairOutputTypeDef],
        "tags": List[TagOutputTypeDef],
        "settings": List[ClusterSettingOutputTypeDef],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List[CapacityProviderStrategyItemOutputTypeDef],
        "attachments": List[AttachmentTypeDef],
        "attachmentsStatus": str,
        "serviceConnectDefaults": ClusterServiceConnectDefaultsTypeDef,
    },
    total=False,
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "clusterName": str,
        "tags": Sequence[TagTypeDef],
        "settings": Sequence[ClusterSettingTypeDef],
        "configuration": ClusterConfigurationTypeDef,
        "capacityProviders": Sequence[str],
        "defaultCapacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
        "serviceConnectDefaults": ClusterServiceConnectDefaultsRequestTypeDef,
    },
    total=False,
)

_RequiredUpdateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterRequestRequestTypeDef",
    {
        "cluster": str,
    },
)
_OptionalUpdateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterRequestRequestTypeDef",
    {
        "settings": Sequence[ClusterSettingTypeDef],
        "configuration": ClusterConfigurationTypeDef,
        "serviceConnectDefaults": ClusterServiceConnectDefaultsRequestTypeDef,
    },
    total=False,
)

class UpdateClusterRequestRequestTypeDef(
    _RequiredUpdateClusterRequestRequestTypeDef, _OptionalUpdateClusterRequestRequestTypeDef
):
    pass

TaskDefinitionTypeDef = TypedDict(
    "TaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List[ContainerDefinitionOutputTypeDef],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": NetworkModeType,
        "revision": int,
        "volumes": List[VolumeOutputTypeDef],
        "status": TaskDefinitionStatusType,
        "requiresAttributes": List[AttributeOutputTypeDef],
        "placementConstraints": List[TaskDefinitionPlacementConstraintOutputTypeDef],
        "compatibilities": List[CompatibilityType],
        "runtimePlatform": RuntimePlatformOutputTypeDef,
        "requiresCompatibilities": List[CompatibilityType],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List[InferenceAcceleratorOutputTypeDef],
        "pidMode": PidModeType,
        "ipcMode": IpcModeType,
        "proxyConfiguration": ProxyConfigurationOutputTypeDef,
        "registeredAt": datetime,
        "deregisteredAt": datetime,
        "registeredBy": str,
        "ephemeralStorage": EphemeralStorageOutputTypeDef,
    },
    total=False,
)

_RequiredRegisterTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterTaskDefinitionRequestRequestTypeDef",
    {
        "family": str,
        "containerDefinitions": Sequence[ContainerDefinitionTypeDef],
    },
)
_OptionalRegisterTaskDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterTaskDefinitionRequestRequestTypeDef",
    {
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": NetworkModeType,
        "volumes": Sequence[VolumeTypeDef],
        "placementConstraints": Sequence[TaskDefinitionPlacementConstraintTypeDef],
        "requiresCompatibilities": Sequence[CompatibilityType],
        "cpu": str,
        "memory": str,
        "tags": Sequence[TagTypeDef],
        "pidMode": PidModeType,
        "ipcMode": IpcModeType,
        "proxyConfiguration": ProxyConfigurationTypeDef,
        "inferenceAccelerators": Sequence[InferenceAcceleratorTypeDef],
        "ephemeralStorage": EphemeralStorageTypeDef,
        "runtimePlatform": RuntimePlatformTypeDef,
    },
    total=False,
)

class RegisterTaskDefinitionRequestRequestTypeDef(
    _RequiredRegisterTaskDefinitionRequestRequestTypeDef,
    _OptionalRegisterTaskDefinitionRequestRequestTypeDef,
):
    pass

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "failedTasks": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityProviderStrategy": List[CapacityProviderStrategyItemOutputTypeDef],
        "launchType": LaunchTypeType,
        "platformVersion": str,
        "platformFamily": str,
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "rolloutState": DeploymentRolloutStateType,
        "rolloutStateReason": str,
        "serviceConnectConfiguration": ServiceConnectConfigurationOutputTypeDef,
        "serviceConnectResources": List[ServiceConnectServiceResourceTypeDef],
    },
    total=False,
)

_RequiredCreateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalCreateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestRequestTypeDef",
    {
        "cluster": str,
        "taskDefinition": str,
        "loadBalancers": Sequence[LoadBalancerTypeDef],
        "serviceRegistries": Sequence[ServiceRegistryTypeDef],
        "desiredCount": int,
        "clientToken": str,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
        "platformVersion": str,
        "role": str,
        "deploymentConfiguration": DeploymentConfigurationTypeDef,
        "placementConstraints": Sequence[PlacementConstraintTypeDef],
        "placementStrategy": Sequence[PlacementStrategyTypeDef],
        "networkConfiguration": NetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": SchedulingStrategyType,
        "deploymentController": DeploymentControllerTypeDef,
        "tags": Sequence[TagTypeDef],
        "enableECSManagedTags": bool,
        "propagateTags": PropagateTagsType,
        "enableExecuteCommand": bool,
        "serviceConnectConfiguration": ServiceConnectConfigurationTypeDef,
    },
    total=False,
)

class CreateServiceRequestRequestTypeDef(
    _RequiredCreateServiceRequestRequestTypeDef, _OptionalCreateServiceRequestRequestTypeDef
):
    pass

_RequiredUpdateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceRequestRequestTypeDef",
    {
        "service": str,
    },
)
_OptionalUpdateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceRequestRequestTypeDef",
    {
        "cluster": str,
        "desiredCount": int,
        "taskDefinition": str,
        "capacityProviderStrategy": Sequence[CapacityProviderStrategyItemTypeDef],
        "deploymentConfiguration": DeploymentConfigurationTypeDef,
        "networkConfiguration": NetworkConfigurationTypeDef,
        "placementConstraints": Sequence[PlacementConstraintTypeDef],
        "placementStrategy": Sequence[PlacementStrategyTypeDef],
        "platformVersion": str,
        "forceNewDeployment": bool,
        "healthCheckGracePeriodSeconds": int,
        "enableExecuteCommand": bool,
        "enableECSManagedTags": bool,
        "loadBalancers": Sequence[LoadBalancerTypeDef],
        "propagateTags": PropagateTagsType,
        "serviceRegistries": Sequence[ServiceRegistryTypeDef],
        "serviceConnectConfiguration": ServiceConnectConfigurationTypeDef,
    },
    total=False,
)

class UpdateServiceRequestRequestTypeDef(
    _RequiredUpdateServiceRequestRequestTypeDef, _OptionalUpdateServiceRequestRequestTypeDef
):
    pass

DescribeTasksResponseTypeDef = TypedDict(
    "DescribeTasksResponseTypeDef",
    {
        "tasks": List[TaskTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RunTaskResponseTypeDef = TypedDict(
    "RunTaskResponseTypeDef",
    {
        "tasks": List[TaskTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTaskResponseTypeDef = TypedDict(
    "StartTaskResponseTypeDef",
    {
        "tasks": List[TaskTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTaskResponseTypeDef = TypedDict(
    "StopTaskResponseTypeDef",
    {
        "task": TaskTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "clusters": List[ClusterTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutClusterCapacityProvidersResponseTypeDef = TypedDict(
    "PutClusterCapacityProvidersResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterResponseTypeDef = TypedDict(
    "UpdateClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterSettingsResponseTypeDef = TypedDict(
    "UpdateClusterSettingsResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTaskDefinitionsResponseTypeDef = TypedDict(
    "DeleteTaskDefinitionsResponseTypeDef",
    {
        "taskDefinitions": List[TaskDefinitionTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTaskDefinitionResponseTypeDef = TypedDict(
    "DeregisterTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": TaskDefinitionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskDefinitionResponseTypeDef = TypedDict(
    "DescribeTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": TaskDefinitionTypeDef,
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterTaskDefinitionResponseTypeDef = TypedDict(
    "RegisterTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": TaskDefinitionTypeDef,
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[LoadBalancerOutputTypeDef],
        "serviceRegistries": List[ServiceRegistryOutputTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List[CapacityProviderStrategyItemOutputTypeDef],
        "platformVersion": str,
        "platformFamily": str,
        "taskDefinition": str,
        "deploymentConfiguration": DeploymentConfigurationOutputTypeDef,
        "taskSets": List[TaskSetTypeDef],
        "deployments": List[DeploymentTypeDef],
        "roleArn": str,
        "events": List[ServiceEventTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[PlacementConstraintOutputTypeDef],
        "placementStrategy": List[PlacementStrategyOutputTypeDef],
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": SchedulingStrategyType,
        "deploymentController": DeploymentControllerOutputTypeDef,
        "tags": List[TagOutputTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": PropagateTagsType,
        "enableExecuteCommand": bool,
    },
    total=False,
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "service": ServiceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "service": ServiceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {
        "services": List[ServiceTypeDef],
        "failures": List[FailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "service": ServiceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
