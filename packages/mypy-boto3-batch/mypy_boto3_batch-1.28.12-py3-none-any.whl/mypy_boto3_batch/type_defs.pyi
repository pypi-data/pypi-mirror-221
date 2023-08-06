"""
Type annotations for batch service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/type_defs/)

Usage::

    ```python
    from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef

    data: ArrayPropertiesDetailTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ArrayJobDependencyType,
    AssignPublicIpType,
    CEStateType,
    CEStatusType,
    CETypeType,
    CRAllocationStrategyType,
    CRTypeType,
    CRUpdateAllocationStrategyType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    JobDefinitionTypeType,
    JobStatusType,
    JQStateType,
    JQStatusType,
    LogDriverType,
    OrchestrationTypeType,
    PlatformCapabilityType,
    ResourceTypeType,
    RetryActionType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArrayPropertiesDetailTypeDef",
    "ArrayPropertiesSummaryTypeDef",
    "ArrayPropertiesTypeDef",
    "NetworkInterfaceTypeDef",
    "CancelJobRequestRequestTypeDef",
    "EksConfigurationOutputTypeDef",
    "UpdatePolicyOutputTypeDef",
    "ComputeEnvironmentOrderOutputTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "Ec2ConfigurationOutputTypeDef",
    "LaunchTemplateSpecificationOutputTypeDef",
    "Ec2ConfigurationTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "EphemeralStorageOutputTypeDef",
    "FargatePlatformConfigurationOutputTypeDef",
    "KeyValuePairOutputTypeDef",
    "MountPointOutputTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "ResourceRequirementOutputTypeDef",
    "RuntimePlatformOutputTypeDef",
    "SecretOutputTypeDef",
    "UlimitOutputTypeDef",
    "KeyValuePairTypeDef",
    "ResourceRequirementTypeDef",
    "EphemeralStorageTypeDef",
    "FargatePlatformConfigurationTypeDef",
    "MountPointTypeDef",
    "NetworkConfigurationTypeDef",
    "RuntimePlatformTypeDef",
    "SecretTypeDef",
    "UlimitTypeDef",
    "ContainerSummaryTypeDef",
    "EksConfigurationTypeDef",
    "CreateComputeEnvironmentResponseTypeDef",
    "CreateJobQueueResponseTypeDef",
    "CreateSchedulingPolicyResponseTypeDef",
    "DeleteComputeEnvironmentRequestRequestTypeDef",
    "DeleteJobQueueRequestRequestTypeDef",
    "DeleteSchedulingPolicyRequestRequestTypeDef",
    "DeregisterJobDefinitionRequestRequestTypeDef",
    "DescribeComputeEnvironmentsRequestDescribeComputeEnvironmentsPaginateTypeDef",
    "DescribeComputeEnvironmentsRequestRequestTypeDef",
    "DescribeJobDefinitionsRequestDescribeJobDefinitionsPaginateTypeDef",
    "DescribeJobDefinitionsRequestRequestTypeDef",
    "DescribeJobQueuesRequestDescribeJobQueuesPaginateTypeDef",
    "DescribeJobQueuesRequestRequestTypeDef",
    "DescribeJobsRequestRequestTypeDef",
    "DescribeSchedulingPoliciesRequestRequestTypeDef",
    "DeviceOutputTypeDef",
    "DeviceTypeDef",
    "EFSAuthorizationConfigOutputTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EksAttemptContainerDetailTypeDef",
    "EksContainerEnvironmentVariableOutputTypeDef",
    "EksContainerResourceRequirementsOutputTypeDef",
    "EksContainerSecurityContextOutputTypeDef",
    "EksContainerVolumeMountOutputTypeDef",
    "EksContainerEnvironmentVariableTypeDef",
    "EksContainerResourceRequirementsTypeDef",
    "EksContainerSecurityContextTypeDef",
    "EksContainerVolumeMountTypeDef",
    "EksEmptyDirOutputTypeDef",
    "EksEmptyDirTypeDef",
    "EksHostPathOutputTypeDef",
    "EksHostPathTypeDef",
    "EksMetadataOutputTypeDef",
    "EksMetadataTypeDef",
    "EksSecretOutputTypeDef",
    "EksSecretTypeDef",
    "EvaluateOnExitOutputTypeDef",
    "EvaluateOnExitTypeDef",
    "ShareAttributesOutputTypeDef",
    "ShareAttributesTypeDef",
    "HostOutputTypeDef",
    "HostTypeDef",
    "JobTimeoutOutputTypeDef",
    "JobDependencyOutputTypeDef",
    "JobDependencyTypeDef",
    "NodeDetailsTypeDef",
    "NodePropertiesSummaryTypeDef",
    "JobTimeoutTypeDef",
    "KeyValuesPairTypeDef",
    "TmpfsOutputTypeDef",
    "TmpfsTypeDef",
    "ListSchedulingPoliciesRequestListSchedulingPoliciesPaginateTypeDef",
    "ListSchedulingPoliciesRequestRequestTypeDef",
    "SchedulingPolicyListingDetailTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterJobDefinitionResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SubmitJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TerminateJobRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePolicyTypeDef",
    "UpdateComputeEnvironmentResponseTypeDef",
    "UpdateJobQueueResponseTypeDef",
    "AttemptContainerDetailTypeDef",
    "JobQueueDetailTypeDef",
    "CreateJobQueueRequestRequestTypeDef",
    "UpdateJobQueueRequestRequestTypeDef",
    "ComputeResourceOutputTypeDef",
    "ComputeResourceTypeDef",
    "ComputeResourceUpdateTypeDef",
    "LogConfigurationOutputTypeDef",
    "ContainerOverridesTypeDef",
    "LogConfigurationTypeDef",
    "EFSVolumeConfigurationOutputTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EksAttemptDetailTypeDef",
    "EksContainerDetailTypeDef",
    "EksContainerOutputTypeDef",
    "EksContainerOverrideTypeDef",
    "EksContainerTypeDef",
    "EksVolumeOutputTypeDef",
    "EksVolumeTypeDef",
    "RetryStrategyOutputTypeDef",
    "RetryStrategyTypeDef",
    "FairsharePolicyOutputTypeDef",
    "FairsharePolicyTypeDef",
    "JobSummaryTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListJobsRequestRequestTypeDef",
    "LinuxParametersOutputTypeDef",
    "LinuxParametersTypeDef",
    "ListSchedulingPoliciesResponseTypeDef",
    "AttemptDetailTypeDef",
    "DescribeJobQueuesResponseTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "CreateComputeEnvironmentRequestRequestTypeDef",
    "UpdateComputeEnvironmentRequestRequestTypeDef",
    "NodePropertyOverrideTypeDef",
    "VolumeOutputTypeDef",
    "VolumeTypeDef",
    "EksPodPropertiesOverrideTypeDef",
    "EksPodPropertiesDetailTypeDef",
    "EksPodPropertiesOutputTypeDef",
    "EksPodPropertiesTypeDef",
    "SchedulingPolicyDetailTypeDef",
    "CreateSchedulingPolicyRequestRequestTypeDef",
    "UpdateSchedulingPolicyRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "DescribeComputeEnvironmentsResponseTypeDef",
    "NodeOverridesTypeDef",
    "ContainerDetailTypeDef",
    "ContainerPropertiesOutputTypeDef",
    "ContainerPropertiesTypeDef",
    "EksPropertiesOverrideTypeDef",
    "EksPropertiesDetailTypeDef",
    "EksPropertiesOutputTypeDef",
    "EksPropertiesTypeDef",
    "DescribeSchedulingPoliciesResponseTypeDef",
    "NodeRangePropertyOutputTypeDef",
    "NodeRangePropertyTypeDef",
    "SubmitJobRequestRequestTypeDef",
    "NodePropertiesOutputTypeDef",
    "NodePropertiesTypeDef",
    "JobDefinitionTypeDef",
    "JobDetailTypeDef",
    "RegisterJobDefinitionRequestRequestTypeDef",
    "DescribeJobDefinitionsResponseTypeDef",
    "DescribeJobsResponseTypeDef",
)

ArrayPropertiesDetailTypeDef = TypedDict(
    "ArrayPropertiesDetailTypeDef",
    {
        "statusSummary": Dict[str, int],
        "size": int,
        "index": int,
    },
    total=False,
)

ArrayPropertiesSummaryTypeDef = TypedDict(
    "ArrayPropertiesSummaryTypeDef",
    {
        "size": int,
        "index": int,
    },
    total=False,
)

ArrayPropertiesTypeDef = TypedDict(
    "ArrayPropertiesTypeDef",
    {
        "size": int,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": str,
        "ipv6Address": str,
        "privateIpv4Address": str,
    },
    total=False,
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)

EksConfigurationOutputTypeDef = TypedDict(
    "EksConfigurationOutputTypeDef",
    {
        "eksClusterArn": str,
        "kubernetesNamespace": str,
    },
)

UpdatePolicyOutputTypeDef = TypedDict(
    "UpdatePolicyOutputTypeDef",
    {
        "terminateJobsOnUpdate": bool,
        "jobExecutionTimeoutMinutes": int,
    },
    total=False,
)

ComputeEnvironmentOrderOutputTypeDef = TypedDict(
    "ComputeEnvironmentOrderOutputTypeDef",
    {
        "order": int,
        "computeEnvironment": str,
    },
)

ComputeEnvironmentOrderTypeDef = TypedDict(
    "ComputeEnvironmentOrderTypeDef",
    {
        "order": int,
        "computeEnvironment": str,
    },
)

_RequiredEc2ConfigurationOutputTypeDef = TypedDict(
    "_RequiredEc2ConfigurationOutputTypeDef",
    {
        "imageType": str,
    },
)
_OptionalEc2ConfigurationOutputTypeDef = TypedDict(
    "_OptionalEc2ConfigurationOutputTypeDef",
    {
        "imageIdOverride": str,
        "imageKubernetesVersion": str,
    },
    total=False,
)

class Ec2ConfigurationOutputTypeDef(
    _RequiredEc2ConfigurationOutputTypeDef, _OptionalEc2ConfigurationOutputTypeDef
):
    pass

LaunchTemplateSpecificationOutputTypeDef = TypedDict(
    "LaunchTemplateSpecificationOutputTypeDef",
    {
        "launchTemplateId": str,
        "launchTemplateName": str,
        "version": str,
    },
    total=False,
)

_RequiredEc2ConfigurationTypeDef = TypedDict(
    "_RequiredEc2ConfigurationTypeDef",
    {
        "imageType": str,
    },
)
_OptionalEc2ConfigurationTypeDef = TypedDict(
    "_OptionalEc2ConfigurationTypeDef",
    {
        "imageIdOverride": str,
        "imageKubernetesVersion": str,
    },
    total=False,
)

class Ec2ConfigurationTypeDef(_RequiredEc2ConfigurationTypeDef, _OptionalEc2ConfigurationTypeDef):
    pass

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": str,
        "launchTemplateName": str,
        "version": str,
    },
    total=False,
)

EphemeralStorageOutputTypeDef = TypedDict(
    "EphemeralStorageOutputTypeDef",
    {
        "sizeInGiB": int,
    },
)

FargatePlatformConfigurationOutputTypeDef = TypedDict(
    "FargatePlatformConfigurationOutputTypeDef",
    {
        "platformVersion": str,
    },
    total=False,
)

KeyValuePairOutputTypeDef = TypedDict(
    "KeyValuePairOutputTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

MountPointOutputTypeDef = TypedDict(
    "MountPointOutputTypeDef",
    {
        "containerPath": str,
        "readOnly": bool,
        "sourceVolume": str,
    },
    total=False,
)

NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "assignPublicIp": AssignPublicIpType,
    },
    total=False,
)

ResourceRequirementOutputTypeDef = TypedDict(
    "ResourceRequirementOutputTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

RuntimePlatformOutputTypeDef = TypedDict(
    "RuntimePlatformOutputTypeDef",
    {
        "operatingSystemFamily": str,
        "cpuArchitecture": str,
    },
    total=False,
)

SecretOutputTypeDef = TypedDict(
    "SecretOutputTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

UlimitOutputTypeDef = TypedDict(
    "UlimitOutputTypeDef",
    {
        "hardLimit": int,
        "name": str,
        "softLimit": int,
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

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

EphemeralStorageTypeDef = TypedDict(
    "EphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

FargatePlatformConfigurationTypeDef = TypedDict(
    "FargatePlatformConfigurationTypeDef",
    {
        "platformVersion": str,
    },
    total=False,
)

MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "containerPath": str,
        "readOnly": bool,
        "sourceVolume": str,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "assignPublicIp": AssignPublicIpType,
    },
    total=False,
)

RuntimePlatformTypeDef = TypedDict(
    "RuntimePlatformTypeDef",
    {
        "operatingSystemFamily": str,
        "cpuArchitecture": str,
    },
    total=False,
)

SecretTypeDef = TypedDict(
    "SecretTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

UlimitTypeDef = TypedDict(
    "UlimitTypeDef",
    {
        "hardLimit": int,
        "name": str,
        "softLimit": int,
    },
)

ContainerSummaryTypeDef = TypedDict(
    "ContainerSummaryTypeDef",
    {
        "exitCode": int,
        "reason": str,
    },
    total=False,
)

EksConfigurationTypeDef = TypedDict(
    "EksConfigurationTypeDef",
    {
        "eksClusterArn": str,
        "kubernetesNamespace": str,
    },
)

CreateComputeEnvironmentResponseTypeDef = TypedDict(
    "CreateComputeEnvironmentResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobQueueResponseTypeDef = TypedDict(
    "CreateJobQueueResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchedulingPolicyResponseTypeDef = TypedDict(
    "CreateSchedulingPolicyResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironment": str,
    },
)

DeleteJobQueueRequestRequestTypeDef = TypedDict(
    "DeleteJobQueueRequestRequestTypeDef",
    {
        "jobQueue": str,
    },
)

DeleteSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "DeleteSchedulingPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeregisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeregisterJobDefinitionRequestRequestTypeDef",
    {
        "jobDefinition": str,
    },
)

DescribeComputeEnvironmentsRequestDescribeComputeEnvironmentsPaginateTypeDef = TypedDict(
    "DescribeComputeEnvironmentsRequestDescribeComputeEnvironmentsPaginateTypeDef",
    {
        "computeEnvironments": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeComputeEnvironmentsRequestRequestTypeDef = TypedDict(
    "DescribeComputeEnvironmentsRequestRequestTypeDef",
    {
        "computeEnvironments": Sequence[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeJobDefinitionsRequestDescribeJobDefinitionsPaginateTypeDef = TypedDict(
    "DescribeJobDefinitionsRequestDescribeJobDefinitionsPaginateTypeDef",
    {
        "jobDefinitions": Sequence[str],
        "jobDefinitionName": str,
        "status": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeJobDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeJobDefinitionsRequestRequestTypeDef",
    {
        "jobDefinitions": Sequence[str],
        "maxResults": int,
        "jobDefinitionName": str,
        "status": str,
        "nextToken": str,
    },
    total=False,
)

DescribeJobQueuesRequestDescribeJobQueuesPaginateTypeDef = TypedDict(
    "DescribeJobQueuesRequestDescribeJobQueuesPaginateTypeDef",
    {
        "jobQueues": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeJobQueuesRequestRequestTypeDef = TypedDict(
    "DescribeJobQueuesRequestRequestTypeDef",
    {
        "jobQueues": Sequence[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeJobsRequestRequestTypeDef = TypedDict(
    "DescribeJobsRequestRequestTypeDef",
    {
        "jobs": Sequence[str],
    },
)

DescribeSchedulingPoliciesRequestRequestTypeDef = TypedDict(
    "DescribeSchedulingPoliciesRequestRequestTypeDef",
    {
        "arns": Sequence[str],
    },
)

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

EksAttemptContainerDetailTypeDef = TypedDict(
    "EksAttemptContainerDetailTypeDef",
    {
        "exitCode": int,
        "reason": str,
    },
    total=False,
)

_RequiredEksContainerEnvironmentVariableOutputTypeDef = TypedDict(
    "_RequiredEksContainerEnvironmentVariableOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalEksContainerEnvironmentVariableOutputTypeDef = TypedDict(
    "_OptionalEksContainerEnvironmentVariableOutputTypeDef",
    {
        "value": str,
    },
    total=False,
)

class EksContainerEnvironmentVariableOutputTypeDef(
    _RequiredEksContainerEnvironmentVariableOutputTypeDef,
    _OptionalEksContainerEnvironmentVariableOutputTypeDef,
):
    pass

EksContainerResourceRequirementsOutputTypeDef = TypedDict(
    "EksContainerResourceRequirementsOutputTypeDef",
    {
        "limits": Dict[str, str],
        "requests": Dict[str, str],
    },
    total=False,
)

EksContainerSecurityContextOutputTypeDef = TypedDict(
    "EksContainerSecurityContextOutputTypeDef",
    {
        "runAsUser": int,
        "runAsGroup": int,
        "privileged": bool,
        "readOnlyRootFilesystem": bool,
        "runAsNonRoot": bool,
    },
    total=False,
)

EksContainerVolumeMountOutputTypeDef = TypedDict(
    "EksContainerVolumeMountOutputTypeDef",
    {
        "name": str,
        "mountPath": str,
        "readOnly": bool,
    },
    total=False,
)

_RequiredEksContainerEnvironmentVariableTypeDef = TypedDict(
    "_RequiredEksContainerEnvironmentVariableTypeDef",
    {
        "name": str,
    },
)
_OptionalEksContainerEnvironmentVariableTypeDef = TypedDict(
    "_OptionalEksContainerEnvironmentVariableTypeDef",
    {
        "value": str,
    },
    total=False,
)

class EksContainerEnvironmentVariableTypeDef(
    _RequiredEksContainerEnvironmentVariableTypeDef, _OptionalEksContainerEnvironmentVariableTypeDef
):
    pass

EksContainerResourceRequirementsTypeDef = TypedDict(
    "EksContainerResourceRequirementsTypeDef",
    {
        "limits": Mapping[str, str],
        "requests": Mapping[str, str],
    },
    total=False,
)

EksContainerSecurityContextTypeDef = TypedDict(
    "EksContainerSecurityContextTypeDef",
    {
        "runAsUser": int,
        "runAsGroup": int,
        "privileged": bool,
        "readOnlyRootFilesystem": bool,
        "runAsNonRoot": bool,
    },
    total=False,
)

EksContainerVolumeMountTypeDef = TypedDict(
    "EksContainerVolumeMountTypeDef",
    {
        "name": str,
        "mountPath": str,
        "readOnly": bool,
    },
    total=False,
)

EksEmptyDirOutputTypeDef = TypedDict(
    "EksEmptyDirOutputTypeDef",
    {
        "medium": str,
        "sizeLimit": str,
    },
    total=False,
)

EksEmptyDirTypeDef = TypedDict(
    "EksEmptyDirTypeDef",
    {
        "medium": str,
        "sizeLimit": str,
    },
    total=False,
)

EksHostPathOutputTypeDef = TypedDict(
    "EksHostPathOutputTypeDef",
    {
        "path": str,
    },
    total=False,
)

EksHostPathTypeDef = TypedDict(
    "EksHostPathTypeDef",
    {
        "path": str,
    },
    total=False,
)

EksMetadataOutputTypeDef = TypedDict(
    "EksMetadataOutputTypeDef",
    {
        "labels": Dict[str, str],
    },
    total=False,
)

EksMetadataTypeDef = TypedDict(
    "EksMetadataTypeDef",
    {
        "labels": Mapping[str, str],
    },
    total=False,
)

_RequiredEksSecretOutputTypeDef = TypedDict(
    "_RequiredEksSecretOutputTypeDef",
    {
        "secretName": str,
    },
)
_OptionalEksSecretOutputTypeDef = TypedDict(
    "_OptionalEksSecretOutputTypeDef",
    {
        "optional": bool,
    },
    total=False,
)

class EksSecretOutputTypeDef(_RequiredEksSecretOutputTypeDef, _OptionalEksSecretOutputTypeDef):
    pass

_RequiredEksSecretTypeDef = TypedDict(
    "_RequiredEksSecretTypeDef",
    {
        "secretName": str,
    },
)
_OptionalEksSecretTypeDef = TypedDict(
    "_OptionalEksSecretTypeDef",
    {
        "optional": bool,
    },
    total=False,
)

class EksSecretTypeDef(_RequiredEksSecretTypeDef, _OptionalEksSecretTypeDef):
    pass

_RequiredEvaluateOnExitOutputTypeDef = TypedDict(
    "_RequiredEvaluateOnExitOutputTypeDef",
    {
        "action": RetryActionType,
    },
)
_OptionalEvaluateOnExitOutputTypeDef = TypedDict(
    "_OptionalEvaluateOnExitOutputTypeDef",
    {
        "onStatusReason": str,
        "onReason": str,
        "onExitCode": str,
    },
    total=False,
)

class EvaluateOnExitOutputTypeDef(
    _RequiredEvaluateOnExitOutputTypeDef, _OptionalEvaluateOnExitOutputTypeDef
):
    pass

_RequiredEvaluateOnExitTypeDef = TypedDict(
    "_RequiredEvaluateOnExitTypeDef",
    {
        "action": RetryActionType,
    },
)
_OptionalEvaluateOnExitTypeDef = TypedDict(
    "_OptionalEvaluateOnExitTypeDef",
    {
        "onStatusReason": str,
        "onReason": str,
        "onExitCode": str,
    },
    total=False,
)

class EvaluateOnExitTypeDef(_RequiredEvaluateOnExitTypeDef, _OptionalEvaluateOnExitTypeDef):
    pass

_RequiredShareAttributesOutputTypeDef = TypedDict(
    "_RequiredShareAttributesOutputTypeDef",
    {
        "shareIdentifier": str,
    },
)
_OptionalShareAttributesOutputTypeDef = TypedDict(
    "_OptionalShareAttributesOutputTypeDef",
    {
        "weightFactor": float,
    },
    total=False,
)

class ShareAttributesOutputTypeDef(
    _RequiredShareAttributesOutputTypeDef, _OptionalShareAttributesOutputTypeDef
):
    pass

_RequiredShareAttributesTypeDef = TypedDict(
    "_RequiredShareAttributesTypeDef",
    {
        "shareIdentifier": str,
    },
)
_OptionalShareAttributesTypeDef = TypedDict(
    "_OptionalShareAttributesTypeDef",
    {
        "weightFactor": float,
    },
    total=False,
)

class ShareAttributesTypeDef(_RequiredShareAttributesTypeDef, _OptionalShareAttributesTypeDef):
    pass

HostOutputTypeDef = TypedDict(
    "HostOutputTypeDef",
    {
        "sourcePath": str,
    },
    total=False,
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "sourcePath": str,
    },
    total=False,
)

JobTimeoutOutputTypeDef = TypedDict(
    "JobTimeoutOutputTypeDef",
    {
        "attemptDurationSeconds": int,
    },
    total=False,
)

JobDependencyOutputTypeDef = TypedDict(
    "JobDependencyOutputTypeDef",
    {
        "jobId": str,
        "type": ArrayJobDependencyType,
    },
    total=False,
)

JobDependencyTypeDef = TypedDict(
    "JobDependencyTypeDef",
    {
        "jobId": str,
        "type": ArrayJobDependencyType,
    },
    total=False,
)

NodeDetailsTypeDef = TypedDict(
    "NodeDetailsTypeDef",
    {
        "nodeIndex": int,
        "isMainNode": bool,
    },
    total=False,
)

NodePropertiesSummaryTypeDef = TypedDict(
    "NodePropertiesSummaryTypeDef",
    {
        "isMainNode": bool,
        "numNodes": int,
        "nodeIndex": int,
    },
    total=False,
)

JobTimeoutTypeDef = TypedDict(
    "JobTimeoutTypeDef",
    {
        "attemptDurationSeconds": int,
    },
    total=False,
)

KeyValuesPairTypeDef = TypedDict(
    "KeyValuesPairTypeDef",
    {
        "name": str,
        "values": Sequence[str],
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

ListSchedulingPoliciesRequestListSchedulingPoliciesPaginateTypeDef = TypedDict(
    "ListSchedulingPoliciesRequestListSchedulingPoliciesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSchedulingPoliciesRequestRequestTypeDef = TypedDict(
    "ListSchedulingPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

SchedulingPolicyListingDetailTypeDef = TypedDict(
    "SchedulingPolicyListingDetailTypeDef",
    {
        "arn": str,
    },
)

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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

RegisterJobDefinitionResponseTypeDef = TypedDict(
    "RegisterJobDefinitionResponseTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

SubmitJobResponseTypeDef = TypedDict(
    "SubmitJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "jobId": str,
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

TerminateJobRequestRequestTypeDef = TypedDict(
    "TerminateJobRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdatePolicyTypeDef = TypedDict(
    "UpdatePolicyTypeDef",
    {
        "terminateJobsOnUpdate": bool,
        "jobExecutionTimeoutMinutes": int,
    },
    total=False,
)

UpdateComputeEnvironmentResponseTypeDef = TypedDict(
    "UpdateComputeEnvironmentResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJobQueueResponseTypeDef = TypedDict(
    "UpdateJobQueueResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttemptContainerDetailTypeDef = TypedDict(
    "AttemptContainerDetailTypeDef",
    {
        "containerInstanceArn": str,
        "taskArn": str,
        "exitCode": int,
        "reason": str,
        "logStreamName": str,
        "networkInterfaces": List[NetworkInterfaceTypeDef],
    },
    total=False,
)

_RequiredJobQueueDetailTypeDef = TypedDict(
    "_RequiredJobQueueDetailTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": JQStateType,
        "priority": int,
        "computeEnvironmentOrder": List[ComputeEnvironmentOrderOutputTypeDef],
    },
)
_OptionalJobQueueDetailTypeDef = TypedDict(
    "_OptionalJobQueueDetailTypeDef",
    {
        "schedulingPolicyArn": str,
        "status": JQStatusType,
        "statusReason": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class JobQueueDetailTypeDef(_RequiredJobQueueDetailTypeDef, _OptionalJobQueueDetailTypeDef):
    pass

_RequiredCreateJobQueueRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobQueueRequestRequestTypeDef",
    {
        "jobQueueName": str,
        "priority": int,
        "computeEnvironmentOrder": Sequence[ComputeEnvironmentOrderTypeDef],
    },
)
_OptionalCreateJobQueueRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobQueueRequestRequestTypeDef",
    {
        "state": JQStateType,
        "schedulingPolicyArn": str,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateJobQueueRequestRequestTypeDef(
    _RequiredCreateJobQueueRequestRequestTypeDef, _OptionalCreateJobQueueRequestRequestTypeDef
):
    pass

_RequiredUpdateJobQueueRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobQueueRequestRequestTypeDef",
    {
        "jobQueue": str,
    },
)
_OptionalUpdateJobQueueRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobQueueRequestRequestTypeDef",
    {
        "state": JQStateType,
        "schedulingPolicyArn": str,
        "priority": int,
        "computeEnvironmentOrder": Sequence[ComputeEnvironmentOrderTypeDef],
    },
    total=False,
)

class UpdateJobQueueRequestRequestTypeDef(
    _RequiredUpdateJobQueueRequestRequestTypeDef, _OptionalUpdateJobQueueRequestRequestTypeDef
):
    pass

_RequiredComputeResourceOutputTypeDef = TypedDict(
    "_RequiredComputeResourceOutputTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": List[str],
    },
)
_OptionalComputeResourceOutputTypeDef = TypedDict(
    "_OptionalComputeResourceOutputTypeDef",
    {
        "allocationStrategy": CRAllocationStrategyType,
        "minvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": LaunchTemplateSpecificationOutputTypeDef,
        "ec2Configuration": List[Ec2ConfigurationOutputTypeDef],
    },
    total=False,
)

class ComputeResourceOutputTypeDef(
    _RequiredComputeResourceOutputTypeDef, _OptionalComputeResourceOutputTypeDef
):
    pass

_RequiredComputeResourceTypeDef = TypedDict(
    "_RequiredComputeResourceTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": Sequence[str],
    },
)
_OptionalComputeResourceTypeDef = TypedDict(
    "_OptionalComputeResourceTypeDef",
    {
        "allocationStrategy": CRAllocationStrategyType,
        "minvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": Sequence[str],
        "imageId": str,
        "securityGroupIds": Sequence[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Mapping[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": LaunchTemplateSpecificationTypeDef,
        "ec2Configuration": Sequence[Ec2ConfigurationTypeDef],
    },
    total=False,
)

class ComputeResourceTypeDef(_RequiredComputeResourceTypeDef, _OptionalComputeResourceTypeDef):
    pass

ComputeResourceUpdateTypeDef = TypedDict(
    "ComputeResourceUpdateTypeDef",
    {
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "subnets": Sequence[str],
        "securityGroupIds": Sequence[str],
        "allocationStrategy": CRUpdateAllocationStrategyType,
        "instanceTypes": Sequence[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Mapping[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "launchTemplate": LaunchTemplateSpecificationTypeDef,
        "ec2Configuration": Sequence[Ec2ConfigurationTypeDef],
        "updateToLatestImageVersion": bool,
        "type": CRTypeType,
        "imageId": str,
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

ContainerOverridesTypeDef = TypedDict(
    "ContainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": Sequence[str],
        "instanceType": str,
        "environment": Sequence[KeyValuePairTypeDef],
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

EksAttemptDetailTypeDef = TypedDict(
    "EksAttemptDetailTypeDef",
    {
        "containers": List[EksAttemptContainerDetailTypeDef],
        "podName": str,
        "nodeName": str,
        "startedAt": int,
        "stoppedAt": int,
        "statusReason": str,
    },
    total=False,
)

EksContainerDetailTypeDef = TypedDict(
    "EksContainerDetailTypeDef",
    {
        "name": str,
        "image": str,
        "imagePullPolicy": str,
        "command": List[str],
        "args": List[str],
        "env": List[EksContainerEnvironmentVariableOutputTypeDef],
        "resources": EksContainerResourceRequirementsOutputTypeDef,
        "exitCode": int,
        "reason": str,
        "volumeMounts": List[EksContainerVolumeMountOutputTypeDef],
        "securityContext": EksContainerSecurityContextOutputTypeDef,
    },
    total=False,
)

_RequiredEksContainerOutputTypeDef = TypedDict(
    "_RequiredEksContainerOutputTypeDef",
    {
        "image": str,
    },
)
_OptionalEksContainerOutputTypeDef = TypedDict(
    "_OptionalEksContainerOutputTypeDef",
    {
        "name": str,
        "imagePullPolicy": str,
        "command": List[str],
        "args": List[str],
        "env": List[EksContainerEnvironmentVariableOutputTypeDef],
        "resources": EksContainerResourceRequirementsOutputTypeDef,
        "volumeMounts": List[EksContainerVolumeMountOutputTypeDef],
        "securityContext": EksContainerSecurityContextOutputTypeDef,
    },
    total=False,
)

class EksContainerOutputTypeDef(
    _RequiredEksContainerOutputTypeDef, _OptionalEksContainerOutputTypeDef
):
    pass

EksContainerOverrideTypeDef = TypedDict(
    "EksContainerOverrideTypeDef",
    {
        "image": str,
        "command": Sequence[str],
        "args": Sequence[str],
        "env": Sequence[EksContainerEnvironmentVariableTypeDef],
        "resources": EksContainerResourceRequirementsTypeDef,
    },
    total=False,
)

_RequiredEksContainerTypeDef = TypedDict(
    "_RequiredEksContainerTypeDef",
    {
        "image": str,
    },
)
_OptionalEksContainerTypeDef = TypedDict(
    "_OptionalEksContainerTypeDef",
    {
        "name": str,
        "imagePullPolicy": str,
        "command": Sequence[str],
        "args": Sequence[str],
        "env": Sequence[EksContainerEnvironmentVariableTypeDef],
        "resources": EksContainerResourceRequirementsTypeDef,
        "volumeMounts": Sequence[EksContainerVolumeMountTypeDef],
        "securityContext": EksContainerSecurityContextTypeDef,
    },
    total=False,
)

class EksContainerTypeDef(_RequiredEksContainerTypeDef, _OptionalEksContainerTypeDef):
    pass

_RequiredEksVolumeOutputTypeDef = TypedDict(
    "_RequiredEksVolumeOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalEksVolumeOutputTypeDef = TypedDict(
    "_OptionalEksVolumeOutputTypeDef",
    {
        "hostPath": EksHostPathOutputTypeDef,
        "emptyDir": EksEmptyDirOutputTypeDef,
        "secret": EksSecretOutputTypeDef,
    },
    total=False,
)

class EksVolumeOutputTypeDef(_RequiredEksVolumeOutputTypeDef, _OptionalEksVolumeOutputTypeDef):
    pass

_RequiredEksVolumeTypeDef = TypedDict(
    "_RequiredEksVolumeTypeDef",
    {
        "name": str,
    },
)
_OptionalEksVolumeTypeDef = TypedDict(
    "_OptionalEksVolumeTypeDef",
    {
        "hostPath": EksHostPathTypeDef,
        "emptyDir": EksEmptyDirTypeDef,
        "secret": EksSecretTypeDef,
    },
    total=False,
)

class EksVolumeTypeDef(_RequiredEksVolumeTypeDef, _OptionalEksVolumeTypeDef):
    pass

RetryStrategyOutputTypeDef = TypedDict(
    "RetryStrategyOutputTypeDef",
    {
        "attempts": int,
        "evaluateOnExit": List[EvaluateOnExitOutputTypeDef],
    },
    total=False,
)

RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "attempts": int,
        "evaluateOnExit": Sequence[EvaluateOnExitTypeDef],
    },
    total=False,
)

FairsharePolicyOutputTypeDef = TypedDict(
    "FairsharePolicyOutputTypeDef",
    {
        "shareDecaySeconds": int,
        "computeReservation": int,
        "shareDistribution": List[ShareAttributesOutputTypeDef],
    },
    total=False,
)

FairsharePolicyTypeDef = TypedDict(
    "FairsharePolicyTypeDef",
    {
        "shareDecaySeconds": int,
        "computeReservation": int,
        "shareDistribution": Sequence[ShareAttributesTypeDef],
    },
    total=False,
)

_RequiredJobSummaryTypeDef = TypedDict(
    "_RequiredJobSummaryTypeDef",
    {
        "jobId": str,
        "jobName": str,
    },
)
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "jobArn": str,
        "createdAt": int,
        "status": JobStatusType,
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": ContainerSummaryTypeDef,
        "arrayProperties": ArrayPropertiesSummaryTypeDef,
        "nodeProperties": NodePropertiesSummaryTypeDef,
        "jobDefinition": str,
    },
    total=False,
)

class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass

ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "jobQueue": str,
        "arrayJobId": str,
        "multiNodeJobId": str,
        "jobStatus": JobStatusType,
        "filters": Sequence[KeyValuesPairTypeDef],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "jobQueue": str,
        "arrayJobId": str,
        "multiNodeJobId": str,
        "jobStatus": JobStatusType,
        "maxResults": int,
        "nextToken": str,
        "filters": Sequence[KeyValuesPairTypeDef],
    },
    total=False,
)

LinuxParametersOutputTypeDef = TypedDict(
    "LinuxParametersOutputTypeDef",
    {
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
        "devices": Sequence[DeviceTypeDef],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": Sequence[TmpfsTypeDef],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ListSchedulingPoliciesResponseTypeDef = TypedDict(
    "ListSchedulingPoliciesResponseTypeDef",
    {
        "schedulingPolicies": List[SchedulingPolicyListingDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttemptDetailTypeDef = TypedDict(
    "AttemptDetailTypeDef",
    {
        "container": AttemptContainerDetailTypeDef,
        "startedAt": int,
        "stoppedAt": int,
        "statusReason": str,
    },
    total=False,
)

DescribeJobQueuesResponseTypeDef = TypedDict(
    "DescribeJobQueuesResponseTypeDef",
    {
        "jobQueues": List[JobQueueDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredComputeEnvironmentDetailTypeDef = TypedDict(
    "_RequiredComputeEnvironmentDetailTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
    },
)
_OptionalComputeEnvironmentDetailTypeDef = TypedDict(
    "_OptionalComputeEnvironmentDetailTypeDef",
    {
        "unmanagedvCpus": int,
        "ecsClusterArn": str,
        "tags": Dict[str, str],
        "type": CETypeType,
        "state": CEStateType,
        "status": CEStatusType,
        "statusReason": str,
        "computeResources": ComputeResourceOutputTypeDef,
        "serviceRole": str,
        "updatePolicy": UpdatePolicyOutputTypeDef,
        "eksConfiguration": EksConfigurationOutputTypeDef,
        "containerOrchestrationType": OrchestrationTypeType,
        "uuid": str,
    },
    total=False,
)

class ComputeEnvironmentDetailTypeDef(
    _RequiredComputeEnvironmentDetailTypeDef, _OptionalComputeEnvironmentDetailTypeDef
):
    pass

_RequiredCreateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironmentName": str,
        "type": CETypeType,
    },
)
_OptionalCreateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComputeEnvironmentRequestRequestTypeDef",
    {
        "state": CEStateType,
        "unmanagedvCpus": int,
        "computeResources": ComputeResourceTypeDef,
        "serviceRole": str,
        "tags": Mapping[str, str],
        "eksConfiguration": EksConfigurationTypeDef,
    },
    total=False,
)

class CreateComputeEnvironmentRequestRequestTypeDef(
    _RequiredCreateComputeEnvironmentRequestRequestTypeDef,
    _OptionalCreateComputeEnvironmentRequestRequestTypeDef,
):
    pass

_RequiredUpdateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironment": str,
    },
)
_OptionalUpdateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComputeEnvironmentRequestRequestTypeDef",
    {
        "state": CEStateType,
        "unmanagedvCpus": int,
        "computeResources": ComputeResourceUpdateTypeDef,
        "serviceRole": str,
        "updatePolicy": UpdatePolicyTypeDef,
    },
    total=False,
)

class UpdateComputeEnvironmentRequestRequestTypeDef(
    _RequiredUpdateComputeEnvironmentRequestRequestTypeDef,
    _OptionalUpdateComputeEnvironmentRequestRequestTypeDef,
):
    pass

_RequiredNodePropertyOverrideTypeDef = TypedDict(
    "_RequiredNodePropertyOverrideTypeDef",
    {
        "targetNodes": str,
    },
)
_OptionalNodePropertyOverrideTypeDef = TypedDict(
    "_OptionalNodePropertyOverrideTypeDef",
    {
        "containerOverrides": ContainerOverridesTypeDef,
    },
    total=False,
)

class NodePropertyOverrideTypeDef(
    _RequiredNodePropertyOverrideTypeDef, _OptionalNodePropertyOverrideTypeDef
):
    pass

VolumeOutputTypeDef = TypedDict(
    "VolumeOutputTypeDef",
    {
        "host": HostOutputTypeDef,
        "name": str,
        "efsVolumeConfiguration": EFSVolumeConfigurationOutputTypeDef,
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "host": HostTypeDef,
        "name": str,
        "efsVolumeConfiguration": EFSVolumeConfigurationTypeDef,
    },
    total=False,
)

EksPodPropertiesOverrideTypeDef = TypedDict(
    "EksPodPropertiesOverrideTypeDef",
    {
        "containers": Sequence[EksContainerOverrideTypeDef],
        "metadata": EksMetadataTypeDef,
    },
    total=False,
)

EksPodPropertiesDetailTypeDef = TypedDict(
    "EksPodPropertiesDetailTypeDef",
    {
        "serviceAccountName": str,
        "hostNetwork": bool,
        "dnsPolicy": str,
        "containers": List[EksContainerDetailTypeDef],
        "volumes": List[EksVolumeOutputTypeDef],
        "podName": str,
        "nodeName": str,
        "metadata": EksMetadataOutputTypeDef,
    },
    total=False,
)

EksPodPropertiesOutputTypeDef = TypedDict(
    "EksPodPropertiesOutputTypeDef",
    {
        "serviceAccountName": str,
        "hostNetwork": bool,
        "dnsPolicy": str,
        "containers": List[EksContainerOutputTypeDef],
        "volumes": List[EksVolumeOutputTypeDef],
        "metadata": EksMetadataOutputTypeDef,
    },
    total=False,
)

EksPodPropertiesTypeDef = TypedDict(
    "EksPodPropertiesTypeDef",
    {
        "serviceAccountName": str,
        "hostNetwork": bool,
        "dnsPolicy": str,
        "containers": Sequence[EksContainerTypeDef],
        "volumes": Sequence[EksVolumeTypeDef],
        "metadata": EksMetadataTypeDef,
    },
    total=False,
)

_RequiredSchedulingPolicyDetailTypeDef = TypedDict(
    "_RequiredSchedulingPolicyDetailTypeDef",
    {
        "name": str,
        "arn": str,
    },
)
_OptionalSchedulingPolicyDetailTypeDef = TypedDict(
    "_OptionalSchedulingPolicyDetailTypeDef",
    {
        "fairsharePolicy": FairsharePolicyOutputTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

class SchedulingPolicyDetailTypeDef(
    _RequiredSchedulingPolicyDetailTypeDef, _OptionalSchedulingPolicyDetailTypeDef
):
    pass

_RequiredCreateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSchedulingPolicyRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSchedulingPolicyRequestRequestTypeDef",
    {
        "fairsharePolicy": FairsharePolicyTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateSchedulingPolicyRequestRequestTypeDef(
    _RequiredCreateSchedulingPolicyRequestRequestTypeDef,
    _OptionalCreateSchedulingPolicyRequestRequestTypeDef,
):
    pass

_RequiredUpdateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSchedulingPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSchedulingPolicyRequestRequestTypeDef",
    {
        "fairsharePolicy": FairsharePolicyTypeDef,
    },
    total=False,
)

class UpdateSchedulingPolicyRequestRequestTypeDef(
    _RequiredUpdateSchedulingPolicyRequestRequestTypeDef,
    _OptionalUpdateSchedulingPolicyRequestRequestTypeDef,
):
    pass

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "jobSummaryList": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "DescribeComputeEnvironmentsResponseTypeDef",
    {
        "computeEnvironments": List[ComputeEnvironmentDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NodeOverridesTypeDef = TypedDict(
    "NodeOverridesTypeDef",
    {
        "numNodes": int,
        "nodePropertyOverrides": Sequence[NodePropertyOverrideTypeDef],
    },
    total=False,
)

ContainerDetailTypeDef = TypedDict(
    "ContainerDetailTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "executionRoleArn": str,
        "volumes": List[VolumeOutputTypeDef],
        "environment": List[KeyValuePairOutputTypeDef],
        "mountPoints": List[MountPointOutputTypeDef],
        "readonlyRootFilesystem": bool,
        "ulimits": List[UlimitOutputTypeDef],
        "privileged": bool,
        "user": str,
        "exitCode": int,
        "reason": str,
        "containerInstanceArn": str,
        "taskArn": str,
        "logStreamName": str,
        "instanceType": str,
        "networkInterfaces": List[NetworkInterfaceTypeDef],
        "resourceRequirements": List[ResourceRequirementOutputTypeDef],
        "linuxParameters": LinuxParametersOutputTypeDef,
        "logConfiguration": LogConfigurationOutputTypeDef,
        "secrets": List[SecretOutputTypeDef],
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "fargatePlatformConfiguration": FargatePlatformConfigurationOutputTypeDef,
        "ephemeralStorage": EphemeralStorageOutputTypeDef,
        "runtimePlatform": RuntimePlatformOutputTypeDef,
    },
    total=False,
)

ContainerPropertiesOutputTypeDef = TypedDict(
    "ContainerPropertiesOutputTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "executionRoleArn": str,
        "volumes": List[VolumeOutputTypeDef],
        "environment": List[KeyValuePairOutputTypeDef],
        "mountPoints": List[MountPointOutputTypeDef],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[UlimitOutputTypeDef],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[ResourceRequirementOutputTypeDef],
        "linuxParameters": LinuxParametersOutputTypeDef,
        "logConfiguration": LogConfigurationOutputTypeDef,
        "secrets": List[SecretOutputTypeDef],
        "networkConfiguration": NetworkConfigurationOutputTypeDef,
        "fargatePlatformConfiguration": FargatePlatformConfigurationOutputTypeDef,
        "ephemeralStorage": EphemeralStorageOutputTypeDef,
        "runtimePlatform": RuntimePlatformOutputTypeDef,
    },
    total=False,
)

ContainerPropertiesTypeDef = TypedDict(
    "ContainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": Sequence[str],
        "jobRoleArn": str,
        "executionRoleArn": str,
        "volumes": Sequence[VolumeTypeDef],
        "environment": Sequence[KeyValuePairTypeDef],
        "mountPoints": Sequence[MountPointTypeDef],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": Sequence[UlimitTypeDef],
        "user": str,
        "instanceType": str,
        "resourceRequirements": Sequence[ResourceRequirementTypeDef],
        "linuxParameters": LinuxParametersTypeDef,
        "logConfiguration": LogConfigurationTypeDef,
        "secrets": Sequence[SecretTypeDef],
        "networkConfiguration": NetworkConfigurationTypeDef,
        "fargatePlatformConfiguration": FargatePlatformConfigurationTypeDef,
        "ephemeralStorage": EphemeralStorageTypeDef,
        "runtimePlatform": RuntimePlatformTypeDef,
    },
    total=False,
)

EksPropertiesOverrideTypeDef = TypedDict(
    "EksPropertiesOverrideTypeDef",
    {
        "podProperties": EksPodPropertiesOverrideTypeDef,
    },
    total=False,
)

EksPropertiesDetailTypeDef = TypedDict(
    "EksPropertiesDetailTypeDef",
    {
        "podProperties": EksPodPropertiesDetailTypeDef,
    },
    total=False,
)

EksPropertiesOutputTypeDef = TypedDict(
    "EksPropertiesOutputTypeDef",
    {
        "podProperties": EksPodPropertiesOutputTypeDef,
    },
    total=False,
)

EksPropertiesTypeDef = TypedDict(
    "EksPropertiesTypeDef",
    {
        "podProperties": EksPodPropertiesTypeDef,
    },
    total=False,
)

DescribeSchedulingPoliciesResponseTypeDef = TypedDict(
    "DescribeSchedulingPoliciesResponseTypeDef",
    {
        "schedulingPolicies": List[SchedulingPolicyDetailTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNodeRangePropertyOutputTypeDef = TypedDict(
    "_RequiredNodeRangePropertyOutputTypeDef",
    {
        "targetNodes": str,
    },
)
_OptionalNodeRangePropertyOutputTypeDef = TypedDict(
    "_OptionalNodeRangePropertyOutputTypeDef",
    {
        "container": ContainerPropertiesOutputTypeDef,
    },
    total=False,
)

class NodeRangePropertyOutputTypeDef(
    _RequiredNodeRangePropertyOutputTypeDef, _OptionalNodeRangePropertyOutputTypeDef
):
    pass

_RequiredNodeRangePropertyTypeDef = TypedDict(
    "_RequiredNodeRangePropertyTypeDef",
    {
        "targetNodes": str,
    },
)
_OptionalNodeRangePropertyTypeDef = TypedDict(
    "_OptionalNodeRangePropertyTypeDef",
    {
        "container": ContainerPropertiesTypeDef,
    },
    total=False,
)

class NodeRangePropertyTypeDef(
    _RequiredNodeRangePropertyTypeDef, _OptionalNodeRangePropertyTypeDef
):
    pass

_RequiredSubmitJobRequestRequestTypeDef = TypedDict(
    "_RequiredSubmitJobRequestRequestTypeDef",
    {
        "jobName": str,
        "jobQueue": str,
        "jobDefinition": str,
    },
)
_OptionalSubmitJobRequestRequestTypeDef = TypedDict(
    "_OptionalSubmitJobRequestRequestTypeDef",
    {
        "shareIdentifier": str,
        "schedulingPriorityOverride": int,
        "arrayProperties": ArrayPropertiesTypeDef,
        "dependsOn": Sequence[JobDependencyTypeDef],
        "parameters": Mapping[str, str],
        "containerOverrides": ContainerOverridesTypeDef,
        "nodeOverrides": NodeOverridesTypeDef,
        "retryStrategy": RetryStrategyTypeDef,
        "propagateTags": bool,
        "timeout": JobTimeoutTypeDef,
        "tags": Mapping[str, str],
        "eksPropertiesOverride": EksPropertiesOverrideTypeDef,
    },
    total=False,
)

class SubmitJobRequestRequestTypeDef(
    _RequiredSubmitJobRequestRequestTypeDef, _OptionalSubmitJobRequestRequestTypeDef
):
    pass

NodePropertiesOutputTypeDef = TypedDict(
    "NodePropertiesOutputTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[NodeRangePropertyOutputTypeDef],
    },
)

NodePropertiesTypeDef = TypedDict(
    "NodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": Sequence[NodeRangePropertyTypeDef],
    },
)

_RequiredJobDefinitionTypeDef = TypedDict(
    "_RequiredJobDefinitionTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "type": str,
    },
)
_OptionalJobDefinitionTypeDef = TypedDict(
    "_OptionalJobDefinitionTypeDef",
    {
        "status": str,
        "schedulingPriority": int,
        "parameters": Dict[str, str],
        "retryStrategy": RetryStrategyOutputTypeDef,
        "containerProperties": ContainerPropertiesOutputTypeDef,
        "timeout": JobTimeoutOutputTypeDef,
        "nodeProperties": NodePropertiesOutputTypeDef,
        "tags": Dict[str, str],
        "propagateTags": bool,
        "platformCapabilities": List[PlatformCapabilityType],
        "eksProperties": EksPropertiesOutputTypeDef,
        "containerOrchestrationType": OrchestrationTypeType,
    },
    total=False,
)

class JobDefinitionTypeDef(_RequiredJobDefinitionTypeDef, _OptionalJobDefinitionTypeDef):
    pass

_RequiredJobDetailTypeDef = TypedDict(
    "_RequiredJobDetailTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": JobStatusType,
        "startedAt": int,
        "jobDefinition": str,
    },
)
_OptionalJobDetailTypeDef = TypedDict(
    "_OptionalJobDetailTypeDef",
    {
        "jobArn": str,
        "shareIdentifier": str,
        "schedulingPriority": int,
        "attempts": List[AttemptDetailTypeDef],
        "statusReason": str,
        "createdAt": int,
        "retryStrategy": RetryStrategyOutputTypeDef,
        "stoppedAt": int,
        "dependsOn": List[JobDependencyOutputTypeDef],
        "parameters": Dict[str, str],
        "container": ContainerDetailTypeDef,
        "nodeDetails": NodeDetailsTypeDef,
        "nodeProperties": NodePropertiesOutputTypeDef,
        "arrayProperties": ArrayPropertiesDetailTypeDef,
        "timeout": JobTimeoutOutputTypeDef,
        "tags": Dict[str, str],
        "propagateTags": bool,
        "platformCapabilities": List[PlatformCapabilityType],
        "eksProperties": EksPropertiesDetailTypeDef,
        "eksAttempts": List[EksAttemptDetailTypeDef],
        "isCancelled": bool,
        "isTerminated": bool,
    },
    total=False,
)

class JobDetailTypeDef(_RequiredJobDetailTypeDef, _OptionalJobDetailTypeDef):
    pass

_RequiredRegisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterJobDefinitionRequestRequestTypeDef",
    {
        "jobDefinitionName": str,
        "type": JobDefinitionTypeType,
    },
)
_OptionalRegisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterJobDefinitionRequestRequestTypeDef",
    {
        "parameters": Mapping[str, str],
        "schedulingPriority": int,
        "containerProperties": ContainerPropertiesTypeDef,
        "nodeProperties": NodePropertiesTypeDef,
        "retryStrategy": RetryStrategyTypeDef,
        "propagateTags": bool,
        "timeout": JobTimeoutTypeDef,
        "tags": Mapping[str, str],
        "platformCapabilities": Sequence[PlatformCapabilityType],
        "eksProperties": EksPropertiesTypeDef,
    },
    total=False,
)

class RegisterJobDefinitionRequestRequestTypeDef(
    _RequiredRegisterJobDefinitionRequestRequestTypeDef,
    _OptionalRegisterJobDefinitionRequestRequestTypeDef,
):
    pass

DescribeJobDefinitionsResponseTypeDef = TypedDict(
    "DescribeJobDefinitionsResponseTypeDef",
    {
        "jobDefinitions": List[JobDefinitionTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobsResponseTypeDef = TypedDict(
    "DescribeJobsResponseTypeDef",
    {
        "jobs": List[JobDetailTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
