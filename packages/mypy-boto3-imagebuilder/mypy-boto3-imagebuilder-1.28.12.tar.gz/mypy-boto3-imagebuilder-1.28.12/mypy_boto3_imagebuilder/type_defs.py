"""
Type annotations for imagebuilder service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/type_defs/)

Usage::

    ```python
    from mypy_boto3_imagebuilder.type_defs import SeverityCountsTypeDef

    data: SeverityCountsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    BuildTypeType,
    ComponentTypeType,
    DiskImageFormatType,
    EbsVolumeTypeType,
    ImageScanStatusType,
    ImageSourceType,
    ImageStatusType,
    ImageTypeType,
    OwnershipType,
    PipelineExecutionStartConditionType,
    PipelineStatusType,
    PlatformType,
    WorkflowExecutionStatusType,
    WorkflowStepExecutionRollbackStatusType,
    WorkflowStepExecutionStatusType,
    WorkflowTypeType,
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
    "SeverityCountsTypeDef",
    "SystemsManagerAgentOutputTypeDef",
    "SystemsManagerAgentTypeDef",
    "LaunchPermissionConfigurationOutputTypeDef",
    "LaunchPermissionConfigurationTypeDef",
    "ImageStateTypeDef",
    "CancelImageCreationRequestRequestTypeDef",
    "CancelImageCreationResponseTypeDef",
    "ComponentParameterOutputTypeDef",
    "ComponentParameterTypeDef",
    "ComponentParameterDetailTypeDef",
    "ComponentStateTypeDef",
    "ComponentVersionTypeDef",
    "TargetContainerRepositoryOutputTypeDef",
    "TargetContainerRepositoryTypeDef",
    "ContainerRecipeSummaryTypeDef",
    "ContainerTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateContainerRecipeResponseTypeDef",
    "CreateDistributionConfigurationResponseTypeDef",
    "ImageTestsConfigurationTypeDef",
    "ScheduleTypeDef",
    "CreateImagePipelineResponseTypeDef",
    "CreateImageRecipeResponseTypeDef",
    "CreateImageResponseTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "CreateInfrastructureConfigurationResponseTypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteComponentResponseTypeDef",
    "DeleteContainerRecipeRequestRequestTypeDef",
    "DeleteContainerRecipeResponseTypeDef",
    "DeleteDistributionConfigurationRequestRequestTypeDef",
    "DeleteDistributionConfigurationResponseTypeDef",
    "DeleteImagePipelineRequestRequestTypeDef",
    "DeleteImagePipelineResponseTypeDef",
    "DeleteImageRecipeRequestRequestTypeDef",
    "DeleteImageRecipeResponseTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteImageResponseTypeDef",
    "DeleteInfrastructureConfigurationRequestRequestTypeDef",
    "DeleteInfrastructureConfigurationResponseTypeDef",
    "DistributionConfigurationSummaryTypeDef",
    "LaunchTemplateConfigurationOutputTypeDef",
    "S3ExportConfigurationOutputTypeDef",
    "LaunchTemplateConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "EbsInstanceBlockDeviceSpecificationOutputTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EcrConfigurationOutputTypeDef",
    "EcrConfigurationTypeDef",
    "FastLaunchLaunchTemplateSpecificationOutputTypeDef",
    "FastLaunchSnapshotConfigurationOutputTypeDef",
    "FastLaunchLaunchTemplateSpecificationTypeDef",
    "FastLaunchSnapshotConfigurationTypeDef",
    "FilterTypeDef",
    "GetComponentPolicyRequestRequestTypeDef",
    "GetComponentPolicyResponseTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetContainerRecipePolicyRequestRequestTypeDef",
    "GetContainerRecipePolicyResponseTypeDef",
    "GetContainerRecipeRequestRequestTypeDef",
    "GetDistributionConfigurationRequestRequestTypeDef",
    "GetImagePipelineRequestRequestTypeDef",
    "GetImagePolicyRequestRequestTypeDef",
    "GetImagePolicyResponseTypeDef",
    "GetImageRecipePolicyRequestRequestTypeDef",
    "GetImageRecipePolicyResponseTypeDef",
    "GetImageRecipeRequestRequestTypeDef",
    "GetImageRequestRequestTypeDef",
    "GetInfrastructureConfigurationRequestRequestTypeDef",
    "GetWorkflowExecutionRequestRequestTypeDef",
    "GetWorkflowExecutionResponseTypeDef",
    "GetWorkflowStepExecutionRequestRequestTypeDef",
    "GetWorkflowStepExecutionResponseTypeDef",
    "ImagePackageTypeDef",
    "ImageTestsConfigurationOutputTypeDef",
    "ScheduleOutputTypeDef",
    "ImageRecipeSummaryTypeDef",
    "ImageScanFindingsFilterTypeDef",
    "ImageScanStateTypeDef",
    "ImageVersionTypeDef",
    "ImportComponentRequestRequestTypeDef",
    "ImportComponentResponseTypeDef",
    "ImportVmImageRequestRequestTypeDef",
    "ImportVmImageResponseTypeDef",
    "InfrastructureConfigurationSummaryTypeDef",
    "InstanceMetadataOptionsOutputTypeDef",
    "ListComponentBuildVersionsRequestRequestTypeDef",
    "ListImagePackagesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkflowExecutionsRequestRequestTypeDef",
    "WorkflowExecutionMetadataTypeDef",
    "ListWorkflowStepExecutionsRequestRequestTypeDef",
    "WorkflowStepMetadataTypeDef",
    "S3LogsOutputTypeDef",
    "S3LogsTypeDef",
    "VulnerablePackageTypeDef",
    "PutComponentPolicyRequestRequestTypeDef",
    "PutComponentPolicyResponseTypeDef",
    "PutContainerRecipePolicyRequestRequestTypeDef",
    "PutContainerRecipePolicyResponseTypeDef",
    "PutImagePolicyRequestRequestTypeDef",
    "PutImagePolicyResponseTypeDef",
    "PutImageRecipePolicyRequestRequestTypeDef",
    "PutImageRecipePolicyResponseTypeDef",
    "RemediationRecommendationTypeDef",
    "ResponseMetadataTypeDef",
    "StartImagePipelineExecutionRequestRequestTypeDef",
    "StartImagePipelineExecutionResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDistributionConfigurationResponseTypeDef",
    "UpdateImagePipelineResponseTypeDef",
    "UpdateInfrastructureConfigurationResponseTypeDef",
    "AccountAggregationTypeDef",
    "ImageAggregationTypeDef",
    "ImagePipelineAggregationTypeDef",
    "VulnerabilityIdAggregationTypeDef",
    "AdditionalInstanceConfigurationOutputTypeDef",
    "AdditionalInstanceConfigurationTypeDef",
    "AmiDistributionConfigurationOutputTypeDef",
    "AmiDistributionConfigurationTypeDef",
    "AmiTypeDef",
    "ComponentConfigurationOutputTypeDef",
    "ComponentConfigurationTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ListComponentsResponseTypeDef",
    "ContainerDistributionConfigurationOutputTypeDef",
    "ContainerDistributionConfigurationTypeDef",
    "ListContainerRecipesResponseTypeDef",
    "CvssScoreDetailsTypeDef",
    "ListDistributionConfigurationsResponseTypeDef",
    "InstanceBlockDeviceMappingOutputTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "ImageScanningConfigurationOutputTypeDef",
    "ImageScanningConfigurationTypeDef",
    "FastLaunchConfigurationOutputTypeDef",
    "FastLaunchConfigurationTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListContainerRecipesRequestRequestTypeDef",
    "ListDistributionConfigurationsRequestRequestTypeDef",
    "ListImageBuildVersionsRequestRequestTypeDef",
    "ListImagePipelineImagesRequestRequestTypeDef",
    "ListImagePipelinesRequestRequestTypeDef",
    "ListImageRecipesRequestRequestTypeDef",
    "ListImageScanFindingAggregationsRequestRequestTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    "ListImagePackagesResponseTypeDef",
    "ListImageRecipesResponseTypeDef",
    "ListImageScanFindingsRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListInfrastructureConfigurationsResponseTypeDef",
    "ListWorkflowExecutionsResponseTypeDef",
    "ListWorkflowStepExecutionsResponseTypeDef",
    "LoggingOutputTypeDef",
    "LoggingTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "RemediationTypeDef",
    "ImageScanFindingAggregationTypeDef",
    "OutputResourcesTypeDef",
    "ListComponentBuildVersionsResponseTypeDef",
    "GetComponentResponseTypeDef",
    "InspectorScoreDetailsTypeDef",
    "ImageRecipeTypeDef",
    "InstanceConfigurationOutputTypeDef",
    "CreateImageRecipeRequestRequestTypeDef",
    "InstanceConfigurationTypeDef",
    "ImagePipelineTypeDef",
    "CreateImagePipelineRequestRequestTypeDef",
    "CreateImageRequestRequestTypeDef",
    "UpdateImagePipelineRequestRequestTypeDef",
    "DistributionOutputTypeDef",
    "DistributionTypeDef",
    "InfrastructureConfigurationTypeDef",
    "CreateInfrastructureConfigurationRequestRequestTypeDef",
    "UpdateInfrastructureConfigurationRequestRequestTypeDef",
    "ListImageScanFindingAggregationsResponseTypeDef",
    "ImageSummaryTypeDef",
    "ImageScanFindingTypeDef",
    "GetImageRecipeResponseTypeDef",
    "ContainerRecipeTypeDef",
    "CreateContainerRecipeRequestRequestTypeDef",
    "GetImagePipelineResponseTypeDef",
    "ListImagePipelinesResponseTypeDef",
    "DistributionConfigurationTypeDef",
    "CreateDistributionConfigurationRequestRequestTypeDef",
    "UpdateDistributionConfigurationRequestRequestTypeDef",
    "GetInfrastructureConfigurationResponseTypeDef",
    "ListImageBuildVersionsResponseTypeDef",
    "ListImagePipelineImagesResponseTypeDef",
    "ListImageScanFindingsResponseTypeDef",
    "GetContainerRecipeResponseTypeDef",
    "GetDistributionConfigurationResponseTypeDef",
    "ImageTypeDef",
    "GetImageResponseTypeDef",
)

SeverityCountsTypeDef = TypedDict(
    "SeverityCountsTypeDef",
    {
        "all": int,
        "critical": int,
        "high": int,
        "medium": int,
    },
    total=False,
)

SystemsManagerAgentOutputTypeDef = TypedDict(
    "SystemsManagerAgentOutputTypeDef",
    {
        "uninstallAfterBuild": bool,
    },
    total=False,
)

SystemsManagerAgentTypeDef = TypedDict(
    "SystemsManagerAgentTypeDef",
    {
        "uninstallAfterBuild": bool,
    },
    total=False,
)

LaunchPermissionConfigurationOutputTypeDef = TypedDict(
    "LaunchPermissionConfigurationOutputTypeDef",
    {
        "userIds": List[str],
        "userGroups": List[str],
        "organizationArns": List[str],
        "organizationalUnitArns": List[str],
    },
    total=False,
)

LaunchPermissionConfigurationTypeDef = TypedDict(
    "LaunchPermissionConfigurationTypeDef",
    {
        "userIds": Sequence[str],
        "userGroups": Sequence[str],
        "organizationArns": Sequence[str],
        "organizationalUnitArns": Sequence[str],
    },
    total=False,
)

ImageStateTypeDef = TypedDict(
    "ImageStateTypeDef",
    {
        "status": ImageStatusType,
        "reason": str,
    },
    total=False,
)

CancelImageCreationRequestRequestTypeDef = TypedDict(
    "CancelImageCreationRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
        "clientToken": str,
    },
)

CancelImageCreationResponseTypeDef = TypedDict(
    "CancelImageCreationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComponentParameterOutputTypeDef = TypedDict(
    "ComponentParameterOutputTypeDef",
    {
        "name": str,
        "value": List[str],
    },
)

ComponentParameterTypeDef = TypedDict(
    "ComponentParameterTypeDef",
    {
        "name": str,
        "value": Sequence[str],
    },
)

_RequiredComponentParameterDetailTypeDef = TypedDict(
    "_RequiredComponentParameterDetailTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalComponentParameterDetailTypeDef = TypedDict(
    "_OptionalComponentParameterDetailTypeDef",
    {
        "defaultValue": List[str],
        "description": str,
    },
    total=False,
)


class ComponentParameterDetailTypeDef(
    _RequiredComponentParameterDetailTypeDef, _OptionalComponentParameterDetailTypeDef
):
    pass


ComponentStateTypeDef = TypedDict(
    "ComponentStateTypeDef",
    {
        "status": Literal["DEPRECATED"],
        "reason": str,
    },
    total=False,
)

ComponentVersionTypeDef = TypedDict(
    "ComponentVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "type": ComponentTypeType,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)

TargetContainerRepositoryOutputTypeDef = TypedDict(
    "TargetContainerRepositoryOutputTypeDef",
    {
        "service": Literal["ECR"],
        "repositoryName": str,
    },
)

TargetContainerRepositoryTypeDef = TypedDict(
    "TargetContainerRepositoryTypeDef",
    {
        "service": Literal["ECR"],
        "repositoryName": str,
    },
)

ContainerRecipeSummaryTypeDef = TypedDict(
    "ContainerRecipeSummaryTypeDef",
    {
        "arn": str,
        "containerType": Literal["DOCKER"],
        "name": str,
        "platform": PlatformType,
        "owner": str,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "region": str,
        "imageUris": List[str],
    },
    total=False,
)

_RequiredCreateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComponentRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "clientToken": str,
    },
)
_OptionalCreateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComponentRequestRequestTypeDef",
    {
        "description": str,
        "changeDescription": str,
        "supportedOsVersions": Sequence[str],
        "data": str,
        "uri": str,
        "kmsKeyId": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateComponentRequestRequestTypeDef(
    _RequiredCreateComponentRequestRequestTypeDef, _OptionalCreateComponentRequestRequestTypeDef
):
    pass


CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContainerRecipeResponseTypeDef = TypedDict(
    "CreateContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionConfigurationResponseTypeDef = TypedDict(
    "CreateDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageTestsConfigurationTypeDef = TypedDict(
    "ImageTestsConfigurationTypeDef",
    {
        "imageTestsEnabled": bool,
        "timeoutMinutes": int,
    },
    total=False,
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "scheduleExpression": str,
        "timezone": str,
        "pipelineExecutionStartCondition": PipelineExecutionStartConditionType,
    },
    total=False,
)

CreateImagePipelineResponseTypeDef = TypedDict(
    "CreateImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageRecipeResponseTypeDef = TypedDict(
    "CreateImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageResponseTypeDef = TypedDict(
    "CreateImageResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "httpTokens": str,
        "httpPutResponseHopLimit": int,
    },
    total=False,
)

CreateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "CreateInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": str,
        "reason": str,
    },
    total=False,
)

CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
        "version": str,
        "source": str,
    },
    total=False,
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)

DeleteComponentResponseTypeDef = TypedDict(
    "DeleteComponentResponseTypeDef",
    {
        "requestId": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerRecipeRequestRequestTypeDef = TypedDict(
    "DeleteContainerRecipeRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

DeleteContainerRecipeResponseTypeDef = TypedDict(
    "DeleteContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)

DeleteDistributionConfigurationResponseTypeDef = TypedDict(
    "DeleteDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImagePipelineRequestRequestTypeDef = TypedDict(
    "DeleteImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)

DeleteImagePipelineResponseTypeDef = TypedDict(
    "DeleteImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageRecipeRequestRequestTypeDef = TypedDict(
    "DeleteImageRecipeRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

DeleteImageRecipeResponseTypeDef = TypedDict(
    "DeleteImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)

DeleteImageResponseTypeDef = TypedDict(
    "DeleteImageResponseTypeDef",
    {
        "requestId": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)

DeleteInfrastructureConfigurationResponseTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DistributionConfigurationSummaryTypeDef = TypedDict(
    "DistributionConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
        "regions": List[str],
    },
    total=False,
)

_RequiredLaunchTemplateConfigurationOutputTypeDef = TypedDict(
    "_RequiredLaunchTemplateConfigurationOutputTypeDef",
    {
        "launchTemplateId": str,
    },
)
_OptionalLaunchTemplateConfigurationOutputTypeDef = TypedDict(
    "_OptionalLaunchTemplateConfigurationOutputTypeDef",
    {
        "accountId": str,
        "setDefaultVersion": bool,
    },
    total=False,
)


class LaunchTemplateConfigurationOutputTypeDef(
    _RequiredLaunchTemplateConfigurationOutputTypeDef,
    _OptionalLaunchTemplateConfigurationOutputTypeDef,
):
    pass


_RequiredS3ExportConfigurationOutputTypeDef = TypedDict(
    "_RequiredS3ExportConfigurationOutputTypeDef",
    {
        "roleName": str,
        "diskImageFormat": DiskImageFormatType,
        "s3Bucket": str,
    },
)
_OptionalS3ExportConfigurationOutputTypeDef = TypedDict(
    "_OptionalS3ExportConfigurationOutputTypeDef",
    {
        "s3Prefix": str,
    },
    total=False,
)


class S3ExportConfigurationOutputTypeDef(
    _RequiredS3ExportConfigurationOutputTypeDef, _OptionalS3ExportConfigurationOutputTypeDef
):
    pass


_RequiredLaunchTemplateConfigurationTypeDef = TypedDict(
    "_RequiredLaunchTemplateConfigurationTypeDef",
    {
        "launchTemplateId": str,
    },
)
_OptionalLaunchTemplateConfigurationTypeDef = TypedDict(
    "_OptionalLaunchTemplateConfigurationTypeDef",
    {
        "accountId": str,
        "setDefaultVersion": bool,
    },
    total=False,
)


class LaunchTemplateConfigurationTypeDef(
    _RequiredLaunchTemplateConfigurationTypeDef, _OptionalLaunchTemplateConfigurationTypeDef
):
    pass


_RequiredS3ExportConfigurationTypeDef = TypedDict(
    "_RequiredS3ExportConfigurationTypeDef",
    {
        "roleName": str,
        "diskImageFormat": DiskImageFormatType,
        "s3Bucket": str,
    },
)
_OptionalS3ExportConfigurationTypeDef = TypedDict(
    "_OptionalS3ExportConfigurationTypeDef",
    {
        "s3Prefix": str,
    },
    total=False,
)


class S3ExportConfigurationTypeDef(
    _RequiredS3ExportConfigurationTypeDef, _OptionalS3ExportConfigurationTypeDef
):
    pass


EbsInstanceBlockDeviceSpecificationOutputTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationOutputTypeDef",
    {
        "encrypted": bool,
        "deleteOnTermination": bool,
        "iops": int,
        "kmsKeyId": str,
        "snapshotId": str,
        "volumeSize": int,
        "volumeType": EbsVolumeTypeType,
        "throughput": int,
    },
    total=False,
)

EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "encrypted": bool,
        "deleteOnTermination": bool,
        "iops": int,
        "kmsKeyId": str,
        "snapshotId": str,
        "volumeSize": int,
        "volumeType": EbsVolumeTypeType,
        "throughput": int,
    },
    total=False,
)

EcrConfigurationOutputTypeDef = TypedDict(
    "EcrConfigurationOutputTypeDef",
    {
        "repositoryName": str,
        "containerTags": List[str],
    },
    total=False,
)

EcrConfigurationTypeDef = TypedDict(
    "EcrConfigurationTypeDef",
    {
        "repositoryName": str,
        "containerTags": Sequence[str],
    },
    total=False,
)

FastLaunchLaunchTemplateSpecificationOutputTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationOutputTypeDef",
    {
        "launchTemplateId": str,
        "launchTemplateName": str,
        "launchTemplateVersion": str,
    },
    total=False,
)

FastLaunchSnapshotConfigurationOutputTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationOutputTypeDef",
    {
        "targetResourceCount": int,
    },
    total=False,
)

FastLaunchLaunchTemplateSpecificationTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": str,
        "launchTemplateName": str,
        "launchTemplateVersion": str,
    },
    total=False,
)

FastLaunchSnapshotConfigurationTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationTypeDef",
    {
        "targetResourceCount": int,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
    },
    total=False,
)

GetComponentPolicyRequestRequestTypeDef = TypedDict(
    "GetComponentPolicyRequestRequestTypeDef",
    {
        "componentArn": str,
    },
)

GetComponentPolicyResponseTypeDef = TypedDict(
    "GetComponentPolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)

GetContainerRecipePolicyRequestRequestTypeDef = TypedDict(
    "GetContainerRecipePolicyRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

GetContainerRecipePolicyResponseTypeDef = TypedDict(
    "GetContainerRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerRecipeRequestRequestTypeDef = TypedDict(
    "GetContainerRecipeRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

GetDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "GetDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)

GetImagePipelineRequestRequestTypeDef = TypedDict(
    "GetImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)

GetImagePolicyRequestRequestTypeDef = TypedDict(
    "GetImagePolicyRequestRequestTypeDef",
    {
        "imageArn": str,
    },
)

GetImagePolicyResponseTypeDef = TypedDict(
    "GetImagePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRecipePolicyRequestRequestTypeDef = TypedDict(
    "GetImageRecipePolicyRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

GetImageRecipePolicyResponseTypeDef = TypedDict(
    "GetImageRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRecipeRequestRequestTypeDef = TypedDict(
    "GetImageRecipeRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

GetImageRequestRequestTypeDef = TypedDict(
    "GetImageRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)

GetInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "GetInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)

GetWorkflowExecutionRequestRequestTypeDef = TypedDict(
    "GetWorkflowExecutionRequestRequestTypeDef",
    {
        "workflowExecutionId": str,
    },
)

GetWorkflowExecutionResponseTypeDef = TypedDict(
    "GetWorkflowExecutionResponseTypeDef",
    {
        "requestId": str,
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "type": WorkflowTypeType,
        "status": WorkflowExecutionStatusType,
        "message": str,
        "totalStepCount": int,
        "totalStepsSucceeded": int,
        "totalStepsFailed": int,
        "totalStepsSkipped": int,
        "startTime": str,
        "endTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowStepExecutionRequestRequestTypeDef = TypedDict(
    "GetWorkflowStepExecutionRequestRequestTypeDef",
    {
        "stepExecutionId": str,
    },
)

GetWorkflowStepExecutionResponseTypeDef = TypedDict(
    "GetWorkflowStepExecutionResponseTypeDef",
    {
        "requestId": str,
        "stepExecutionId": str,
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "name": str,
        "description": str,
        "action": str,
        "status": WorkflowStepExecutionStatusType,
        "rollbackStatus": WorkflowStepExecutionRollbackStatusType,
        "message": str,
        "inputs": str,
        "outputs": str,
        "startTime": str,
        "endTime": str,
        "onFailure": str,
        "timeoutSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImagePackageTypeDef = TypedDict(
    "ImagePackageTypeDef",
    {
        "packageName": str,
        "packageVersion": str,
    },
    total=False,
)

ImageTestsConfigurationOutputTypeDef = TypedDict(
    "ImageTestsConfigurationOutputTypeDef",
    {
        "imageTestsEnabled": bool,
        "timeoutMinutes": int,
    },
    total=False,
)

ScheduleOutputTypeDef = TypedDict(
    "ScheduleOutputTypeDef",
    {
        "scheduleExpression": str,
        "timezone": str,
        "pipelineExecutionStartCondition": PipelineExecutionStartConditionType,
    },
    total=False,
)

ImageRecipeSummaryTypeDef = TypedDict(
    "ImageRecipeSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "platform": PlatformType,
        "owner": str,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ImageScanFindingsFilterTypeDef = TypedDict(
    "ImageScanFindingsFilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
    },
    total=False,
)

ImageScanStateTypeDef = TypedDict(
    "ImageScanStateTypeDef",
    {
        "status": ImageScanStatusType,
        "reason": str,
    },
    total=False,
)

ImageVersionTypeDef = TypedDict(
    "ImageVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ImageTypeType,
        "version": str,
        "platform": PlatformType,
        "osVersion": str,
        "owner": str,
        "dateCreated": str,
        "buildType": BuildTypeType,
        "imageSource": ImageSourceType,
    },
    total=False,
)

_RequiredImportComponentRequestRequestTypeDef = TypedDict(
    "_RequiredImportComponentRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "type": ComponentTypeType,
        "format": Literal["SHELL"],
        "platform": PlatformType,
        "clientToken": str,
    },
)
_OptionalImportComponentRequestRequestTypeDef = TypedDict(
    "_OptionalImportComponentRequestRequestTypeDef",
    {
        "description": str,
        "changeDescription": str,
        "data": str,
        "uri": str,
        "kmsKeyId": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class ImportComponentRequestRequestTypeDef(
    _RequiredImportComponentRequestRequestTypeDef, _OptionalImportComponentRequestRequestTypeDef
):
    pass


ImportComponentResponseTypeDef = TypedDict(
    "ImportComponentResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportVmImageRequestRequestTypeDef = TypedDict(
    "_RequiredImportVmImageRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "vmImportTaskId": str,
        "clientToken": str,
    },
)
_OptionalImportVmImageRequestRequestTypeDef = TypedDict(
    "_OptionalImportVmImageRequestRequestTypeDef",
    {
        "description": str,
        "osVersion": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class ImportVmImageRequestRequestTypeDef(
    _RequiredImportVmImageRequestRequestTypeDef, _OptionalImportVmImageRequestRequestTypeDef
):
    pass


ImportVmImageResponseTypeDef = TypedDict(
    "ImportVmImageResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InfrastructureConfigurationSummaryTypeDef = TypedDict(
    "InfrastructureConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "dateCreated": str,
        "dateUpdated": str,
        "resourceTags": Dict[str, str],
        "tags": Dict[str, str],
        "instanceTypes": List[str],
        "instanceProfileName": str,
    },
    total=False,
)

InstanceMetadataOptionsOutputTypeDef = TypedDict(
    "InstanceMetadataOptionsOutputTypeDef",
    {
        "httpTokens": str,
        "httpPutResponseHopLimit": int,
    },
    total=False,
)

_RequiredListComponentBuildVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentBuildVersionsRequestRequestTypeDef",
    {
        "componentVersionArn": str,
    },
)
_OptionalListComponentBuildVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentBuildVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListComponentBuildVersionsRequestRequestTypeDef(
    _RequiredListComponentBuildVersionsRequestRequestTypeDef,
    _OptionalListComponentBuildVersionsRequestRequestTypeDef,
):
    pass


_RequiredListImagePackagesRequestRequestTypeDef = TypedDict(
    "_RequiredListImagePackagesRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)
_OptionalListImagePackagesRequestRequestTypeDef = TypedDict(
    "_OptionalListImagePackagesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListImagePackagesRequestRequestTypeDef(
    _RequiredListImagePackagesRequestRequestTypeDef, _OptionalListImagePackagesRequestRequestTypeDef
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

_RequiredListWorkflowExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkflowExecutionsRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)
_OptionalListWorkflowExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkflowExecutionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListWorkflowExecutionsRequestRequestTypeDef(
    _RequiredListWorkflowExecutionsRequestRequestTypeDef,
    _OptionalListWorkflowExecutionsRequestRequestTypeDef,
):
    pass


WorkflowExecutionMetadataTypeDef = TypedDict(
    "WorkflowExecutionMetadataTypeDef",
    {
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "type": WorkflowTypeType,
        "status": WorkflowExecutionStatusType,
        "message": str,
        "totalStepCount": int,
        "totalStepsSucceeded": int,
        "totalStepsFailed": int,
        "totalStepsSkipped": int,
        "startTime": str,
        "endTime": str,
    },
    total=False,
)

_RequiredListWorkflowStepExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkflowStepExecutionsRequestRequestTypeDef",
    {
        "workflowExecutionId": str,
    },
)
_OptionalListWorkflowStepExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkflowStepExecutionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListWorkflowStepExecutionsRequestRequestTypeDef(
    _RequiredListWorkflowStepExecutionsRequestRequestTypeDef,
    _OptionalListWorkflowStepExecutionsRequestRequestTypeDef,
):
    pass


WorkflowStepMetadataTypeDef = TypedDict(
    "WorkflowStepMetadataTypeDef",
    {
        "stepExecutionId": str,
        "name": str,
        "description": str,
        "action": str,
        "status": WorkflowStepExecutionStatusType,
        "rollbackStatus": WorkflowStepExecutionRollbackStatusType,
        "message": str,
        "inputs": str,
        "outputs": str,
        "startTime": str,
        "endTime": str,
    },
    total=False,
)

S3LogsOutputTypeDef = TypedDict(
    "S3LogsOutputTypeDef",
    {
        "s3BucketName": str,
        "s3KeyPrefix": str,
    },
    total=False,
)

S3LogsTypeDef = TypedDict(
    "S3LogsTypeDef",
    {
        "s3BucketName": str,
        "s3KeyPrefix": str,
    },
    total=False,
)

VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "name": str,
        "version": str,
        "sourceLayerHash": str,
        "epoch": int,
        "release": str,
        "arch": str,
        "packageManager": str,
        "filePath": str,
        "fixedInVersion": str,
        "remediation": str,
    },
    total=False,
)

PutComponentPolicyRequestRequestTypeDef = TypedDict(
    "PutComponentPolicyRequestRequestTypeDef",
    {
        "componentArn": str,
        "policy": str,
    },
)

PutComponentPolicyResponseTypeDef = TypedDict(
    "PutComponentPolicyResponseTypeDef",
    {
        "requestId": str,
        "componentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutContainerRecipePolicyRequestRequestTypeDef = TypedDict(
    "PutContainerRecipePolicyRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
        "policy": str,
    },
)

PutContainerRecipePolicyResponseTypeDef = TypedDict(
    "PutContainerRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImagePolicyRequestRequestTypeDef = TypedDict(
    "PutImagePolicyRequestRequestTypeDef",
    {
        "imageArn": str,
        "policy": str,
    },
)

PutImagePolicyResponseTypeDef = TypedDict(
    "PutImagePolicyResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImageRecipePolicyRequestRequestTypeDef = TypedDict(
    "PutImageRecipePolicyRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
        "policy": str,
    },
)

PutImageRecipePolicyResponseTypeDef = TypedDict(
    "PutImageRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemediationRecommendationTypeDef = TypedDict(
    "RemediationRecommendationTypeDef",
    {
        "text": str,
        "url": str,
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

StartImagePipelineExecutionRequestRequestTypeDef = TypedDict(
    "StartImagePipelineExecutionRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "clientToken": str,
    },
)

StartImagePipelineExecutionResponseTypeDef = TypedDict(
    "StartImagePipelineExecutionResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
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

UpdateDistributionConfigurationResponseTypeDef = TypedDict(
    "UpdateDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateImagePipelineResponseTypeDef = TypedDict(
    "UpdateImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "UpdateInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountAggregationTypeDef = TypedDict(
    "AccountAggregationTypeDef",
    {
        "accountId": str,
        "severityCounts": SeverityCountsTypeDef,
    },
    total=False,
)

ImageAggregationTypeDef = TypedDict(
    "ImageAggregationTypeDef",
    {
        "imageBuildVersionArn": str,
        "severityCounts": SeverityCountsTypeDef,
    },
    total=False,
)

ImagePipelineAggregationTypeDef = TypedDict(
    "ImagePipelineAggregationTypeDef",
    {
        "imagePipelineArn": str,
        "severityCounts": SeverityCountsTypeDef,
    },
    total=False,
)

VulnerabilityIdAggregationTypeDef = TypedDict(
    "VulnerabilityIdAggregationTypeDef",
    {
        "vulnerabilityId": str,
        "severityCounts": SeverityCountsTypeDef,
    },
    total=False,
)

AdditionalInstanceConfigurationOutputTypeDef = TypedDict(
    "AdditionalInstanceConfigurationOutputTypeDef",
    {
        "systemsManagerAgent": SystemsManagerAgentOutputTypeDef,
        "userDataOverride": str,
    },
    total=False,
)

AdditionalInstanceConfigurationTypeDef = TypedDict(
    "AdditionalInstanceConfigurationTypeDef",
    {
        "systemsManagerAgent": SystemsManagerAgentTypeDef,
        "userDataOverride": str,
    },
    total=False,
)

AmiDistributionConfigurationOutputTypeDef = TypedDict(
    "AmiDistributionConfigurationOutputTypeDef",
    {
        "name": str,
        "description": str,
        "targetAccountIds": List[str],
        "amiTags": Dict[str, str],
        "kmsKeyId": str,
        "launchPermission": LaunchPermissionConfigurationOutputTypeDef,
    },
    total=False,
)

AmiDistributionConfigurationTypeDef = TypedDict(
    "AmiDistributionConfigurationTypeDef",
    {
        "name": str,
        "description": str,
        "targetAccountIds": Sequence[str],
        "amiTags": Mapping[str, str],
        "kmsKeyId": str,
        "launchPermission": LaunchPermissionConfigurationTypeDef,
    },
    total=False,
)

AmiTypeDef = TypedDict(
    "AmiTypeDef",
    {
        "region": str,
        "image": str,
        "name": str,
        "description": str,
        "state": ImageStateTypeDef,
        "accountId": str,
    },
    total=False,
)

_RequiredComponentConfigurationOutputTypeDef = TypedDict(
    "_RequiredComponentConfigurationOutputTypeDef",
    {
        "componentArn": str,
    },
)
_OptionalComponentConfigurationOutputTypeDef = TypedDict(
    "_OptionalComponentConfigurationOutputTypeDef",
    {
        "parameters": List[ComponentParameterOutputTypeDef],
    },
    total=False,
)


class ComponentConfigurationOutputTypeDef(
    _RequiredComponentConfigurationOutputTypeDef, _OptionalComponentConfigurationOutputTypeDef
):
    pass


_RequiredComponentConfigurationTypeDef = TypedDict(
    "_RequiredComponentConfigurationTypeDef",
    {
        "componentArn": str,
    },
)
_OptionalComponentConfigurationTypeDef = TypedDict(
    "_OptionalComponentConfigurationTypeDef",
    {
        "parameters": Sequence[ComponentParameterTypeDef],
    },
    total=False,
)


class ComponentConfigurationTypeDef(
    _RequiredComponentConfigurationTypeDef, _OptionalComponentConfigurationTypeDef
):
    pass


ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "state": ComponentStateTypeDef,
        "type": ComponentTypeType,
        "owner": str,
        "description": str,
        "changeDescription": str,
        "dateCreated": str,
        "tags": Dict[str, str],
        "publisher": str,
        "obfuscate": bool,
    },
    total=False,
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "changeDescription": str,
        "type": ComponentTypeType,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "state": ComponentStateTypeDef,
        "parameters": List[ComponentParameterDetailTypeDef],
        "owner": str,
        "data": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "dateCreated": str,
        "tags": Dict[str, str],
        "publisher": str,
        "obfuscate": bool,
    },
    total=False,
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "requestId": str,
        "componentVersionList": List[ComponentVersionTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredContainerDistributionConfigurationOutputTypeDef = TypedDict(
    "_RequiredContainerDistributionConfigurationOutputTypeDef",
    {
        "targetRepository": TargetContainerRepositoryOutputTypeDef,
    },
)
_OptionalContainerDistributionConfigurationOutputTypeDef = TypedDict(
    "_OptionalContainerDistributionConfigurationOutputTypeDef",
    {
        "description": str,
        "containerTags": List[str],
    },
    total=False,
)


class ContainerDistributionConfigurationOutputTypeDef(
    _RequiredContainerDistributionConfigurationOutputTypeDef,
    _OptionalContainerDistributionConfigurationOutputTypeDef,
):
    pass


_RequiredContainerDistributionConfigurationTypeDef = TypedDict(
    "_RequiredContainerDistributionConfigurationTypeDef",
    {
        "targetRepository": TargetContainerRepositoryTypeDef,
    },
)
_OptionalContainerDistributionConfigurationTypeDef = TypedDict(
    "_OptionalContainerDistributionConfigurationTypeDef",
    {
        "description": str,
        "containerTags": Sequence[str],
    },
    total=False,
)


class ContainerDistributionConfigurationTypeDef(
    _RequiredContainerDistributionConfigurationTypeDef,
    _OptionalContainerDistributionConfigurationTypeDef,
):
    pass


ListContainerRecipesResponseTypeDef = TypedDict(
    "ListContainerRecipesResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeSummaryList": List[ContainerRecipeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "scoreSource": str,
        "cvssSource": str,
        "version": str,
        "score": float,
        "scoringVector": str,
        "adjustments": List[CvssScoreAdjustmentTypeDef],
    },
    total=False,
)

ListDistributionConfigurationsResponseTypeDef = TypedDict(
    "ListDistributionConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationSummaryList": List[DistributionConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceBlockDeviceMappingOutputTypeDef = TypedDict(
    "InstanceBlockDeviceMappingOutputTypeDef",
    {
        "deviceName": str,
        "ebs": EbsInstanceBlockDeviceSpecificationOutputTypeDef,
        "virtualName": str,
        "noDevice": str,
    },
    total=False,
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "deviceName": str,
        "ebs": EbsInstanceBlockDeviceSpecificationTypeDef,
        "virtualName": str,
        "noDevice": str,
    },
    total=False,
)

ImageScanningConfigurationOutputTypeDef = TypedDict(
    "ImageScanningConfigurationOutputTypeDef",
    {
        "imageScanningEnabled": bool,
        "ecrConfiguration": EcrConfigurationOutputTypeDef,
    },
    total=False,
)

ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef",
    {
        "imageScanningEnabled": bool,
        "ecrConfiguration": EcrConfigurationTypeDef,
    },
    total=False,
)

_RequiredFastLaunchConfigurationOutputTypeDef = TypedDict(
    "_RequiredFastLaunchConfigurationOutputTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalFastLaunchConfigurationOutputTypeDef = TypedDict(
    "_OptionalFastLaunchConfigurationOutputTypeDef",
    {
        "snapshotConfiguration": FastLaunchSnapshotConfigurationOutputTypeDef,
        "maxParallelLaunches": int,
        "launchTemplate": FastLaunchLaunchTemplateSpecificationOutputTypeDef,
        "accountId": str,
    },
    total=False,
)


class FastLaunchConfigurationOutputTypeDef(
    _RequiredFastLaunchConfigurationOutputTypeDef, _OptionalFastLaunchConfigurationOutputTypeDef
):
    pass


_RequiredFastLaunchConfigurationTypeDef = TypedDict(
    "_RequiredFastLaunchConfigurationTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalFastLaunchConfigurationTypeDef = TypedDict(
    "_OptionalFastLaunchConfigurationTypeDef",
    {
        "snapshotConfiguration": FastLaunchSnapshotConfigurationTypeDef,
        "maxParallelLaunches": int,
        "launchTemplate": FastLaunchLaunchTemplateSpecificationTypeDef,
        "accountId": str,
    },
    total=False,
)


class FastLaunchConfigurationTypeDef(
    _RequiredFastLaunchConfigurationTypeDef, _OptionalFastLaunchConfigurationTypeDef
):
    pass


ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": Sequence[FilterTypeDef],
        "byName": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListContainerRecipesRequestRequestTypeDef = TypedDict(
    "ListContainerRecipesRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDistributionConfigurationsRequestRequestTypeDef = TypedDict(
    "ListDistributionConfigurationsRequestRequestTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListImageBuildVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListImageBuildVersionsRequestRequestTypeDef",
    {
        "imageVersionArn": str,
    },
)
_OptionalListImageBuildVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListImageBuildVersionsRequestRequestTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListImageBuildVersionsRequestRequestTypeDef(
    _RequiredListImageBuildVersionsRequestRequestTypeDef,
    _OptionalListImageBuildVersionsRequestRequestTypeDef,
):
    pass


_RequiredListImagePipelineImagesRequestRequestTypeDef = TypedDict(
    "_RequiredListImagePipelineImagesRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)
_OptionalListImagePipelineImagesRequestRequestTypeDef = TypedDict(
    "_OptionalListImagePipelineImagesRequestRequestTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListImagePipelineImagesRequestRequestTypeDef(
    _RequiredListImagePipelineImagesRequestRequestTypeDef,
    _OptionalListImagePipelineImagesRequestRequestTypeDef,
):
    pass


ListImagePipelinesRequestRequestTypeDef = TypedDict(
    "ListImagePipelinesRequestRequestTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImageRecipesRequestRequestTypeDef = TypedDict(
    "ListImageRecipesRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImageScanFindingAggregationsRequestRequestTypeDef = TypedDict(
    "ListImageScanFindingAggregationsRequestRequestTypeDef",
    {
        "filter": FilterTypeDef,
        "nextToken": str,
    },
    total=False,
)

ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": Sequence[FilterTypeDef],
        "byName": bool,
        "maxResults": int,
        "nextToken": str,
        "includeDeprecated": bool,
    },
    total=False,
)

ListInfrastructureConfigurationsRequestRequestTypeDef = TypedDict(
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImagePackagesResponseTypeDef = TypedDict(
    "ListImagePackagesResponseTypeDef",
    {
        "requestId": str,
        "imagePackageList": List[ImagePackageTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageRecipesResponseTypeDef = TypedDict(
    "ListImageRecipesResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeSummaryList": List[ImageRecipeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageScanFindingsRequestRequestTypeDef = TypedDict(
    "ListImageScanFindingsRequestRequestTypeDef",
    {
        "filters": Sequence[ImageScanFindingsFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "requestId": str,
        "imageVersionList": List[ImageVersionTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInfrastructureConfigurationsResponseTypeDef = TypedDict(
    "ListInfrastructureConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationSummaryList": List[InfrastructureConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowExecutionsResponseTypeDef = TypedDict(
    "ListWorkflowExecutionsResponseTypeDef",
    {
        "requestId": str,
        "workflowExecutions": List[WorkflowExecutionMetadataTypeDef],
        "imageBuildVersionArn": str,
        "message": str,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowStepExecutionsResponseTypeDef = TypedDict(
    "ListWorkflowStepExecutionsResponseTypeDef",
    {
        "requestId": str,
        "steps": List[WorkflowStepMetadataTypeDef],
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "message": str,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingOutputTypeDef = TypedDict(
    "LoggingOutputTypeDef",
    {
        "s3Logs": S3LogsOutputTypeDef,
    },
    total=False,
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "s3Logs": S3LogsTypeDef,
    },
    total=False,
)

_RequiredPackageVulnerabilityDetailsTypeDef = TypedDict(
    "_RequiredPackageVulnerabilityDetailsTypeDef",
    {
        "vulnerabilityId": str,
    },
)
_OptionalPackageVulnerabilityDetailsTypeDef = TypedDict(
    "_OptionalPackageVulnerabilityDetailsTypeDef",
    {
        "vulnerablePackages": List[VulnerablePackageTypeDef],
        "source": str,
        "cvss": List[CvssScoreTypeDef],
        "relatedVulnerabilities": List[str],
        "sourceUrl": str,
        "vendorSeverity": str,
        "vendorCreatedAt": datetime,
        "vendorUpdatedAt": datetime,
        "referenceUrls": List[str],
    },
    total=False,
)


class PackageVulnerabilityDetailsTypeDef(
    _RequiredPackageVulnerabilityDetailsTypeDef, _OptionalPackageVulnerabilityDetailsTypeDef
):
    pass


RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": RemediationRecommendationTypeDef,
    },
    total=False,
)

ImageScanFindingAggregationTypeDef = TypedDict(
    "ImageScanFindingAggregationTypeDef",
    {
        "accountAggregation": AccountAggregationTypeDef,
        "imageAggregation": ImageAggregationTypeDef,
        "imagePipelineAggregation": ImagePipelineAggregationTypeDef,
        "vulnerabilityIdAggregation": VulnerabilityIdAggregationTypeDef,
    },
    total=False,
)

OutputResourcesTypeDef = TypedDict(
    "OutputResourcesTypeDef",
    {
        "amis": List[AmiTypeDef],
        "containers": List[ContainerTypeDef],
    },
    total=False,
)

ListComponentBuildVersionsResponseTypeDef = TypedDict(
    "ListComponentBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "componentSummaryList": List[ComponentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "requestId": str,
        "component": ComponentTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InspectorScoreDetailsTypeDef = TypedDict(
    "InspectorScoreDetailsTypeDef",
    {
        "adjustedCvss": CvssScoreDetailsTypeDef,
    },
    total=False,
)

ImageRecipeTypeDef = TypedDict(
    "ImageRecipeTypeDef",
    {
        "arn": str,
        "type": ImageTypeType,
        "name": str,
        "description": str,
        "platform": PlatformType,
        "owner": str,
        "version": str,
        "components": List[ComponentConfigurationOutputTypeDef],
        "parentImage": str,
        "blockDeviceMappings": List[InstanceBlockDeviceMappingOutputTypeDef],
        "dateCreated": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
        "additionalInstanceConfiguration": AdditionalInstanceConfigurationOutputTypeDef,
    },
    total=False,
)

InstanceConfigurationOutputTypeDef = TypedDict(
    "InstanceConfigurationOutputTypeDef",
    {
        "image": str,
        "blockDeviceMappings": List[InstanceBlockDeviceMappingOutputTypeDef],
    },
    total=False,
)

_RequiredCreateImageRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageRecipeRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "components": Sequence[ComponentConfigurationTypeDef],
        "parentImage": str,
        "clientToken": str,
    },
)
_OptionalCreateImageRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageRecipeRequestRequestTypeDef",
    {
        "description": str,
        "blockDeviceMappings": Sequence[InstanceBlockDeviceMappingTypeDef],
        "tags": Mapping[str, str],
        "workingDirectory": str,
        "additionalInstanceConfiguration": AdditionalInstanceConfigurationTypeDef,
    },
    total=False,
)


class CreateImageRecipeRequestRequestTypeDef(
    _RequiredCreateImageRecipeRequestRequestTypeDef, _OptionalCreateImageRecipeRequestRequestTypeDef
):
    pass


InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "image": str,
        "blockDeviceMappings": Sequence[InstanceBlockDeviceMappingTypeDef],
    },
    total=False,
)

ImagePipelineTypeDef = TypedDict(
    "ImagePipelineTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "platform": PlatformType,
        "enhancedImageMetadataEnabled": bool,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "infrastructureConfigurationArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": ImageTestsConfigurationOutputTypeDef,
        "schedule": ScheduleOutputTypeDef,
        "status": PipelineStatusType,
        "dateCreated": str,
        "dateUpdated": str,
        "dateLastRun": str,
        "dateNextRun": str,
        "tags": Dict[str, str],
        "imageScanningConfiguration": ImageScanningConfigurationOutputTypeDef,
    },
    total=False,
)

_RequiredCreateImagePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImagePipelineRequestRequestTypeDef",
    {
        "name": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalCreateImagePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImagePipelineRequestRequestTypeDef",
    {
        "description": str,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": ImageTestsConfigurationTypeDef,
        "enhancedImageMetadataEnabled": bool,
        "schedule": ScheduleTypeDef,
        "status": PipelineStatusType,
        "tags": Mapping[str, str],
        "imageScanningConfiguration": ImageScanningConfigurationTypeDef,
    },
    total=False,
)


class CreateImagePipelineRequestRequestTypeDef(
    _RequiredCreateImagePipelineRequestRequestTypeDef,
    _OptionalCreateImagePipelineRequestRequestTypeDef,
):
    pass


_RequiredCreateImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalCreateImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": ImageTestsConfigurationTypeDef,
        "enhancedImageMetadataEnabled": bool,
        "tags": Mapping[str, str],
        "imageScanningConfiguration": ImageScanningConfigurationTypeDef,
    },
    total=False,
)


class CreateImageRequestRequestTypeDef(
    _RequiredCreateImageRequestRequestTypeDef, _OptionalCreateImageRequestRequestTypeDef
):
    pass


_RequiredUpdateImagePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalUpdateImagePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateImagePipelineRequestRequestTypeDef",
    {
        "description": str,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": ImageTestsConfigurationTypeDef,
        "enhancedImageMetadataEnabled": bool,
        "schedule": ScheduleTypeDef,
        "status": PipelineStatusType,
        "imageScanningConfiguration": ImageScanningConfigurationTypeDef,
    },
    total=False,
)


class UpdateImagePipelineRequestRequestTypeDef(
    _RequiredUpdateImagePipelineRequestRequestTypeDef,
    _OptionalUpdateImagePipelineRequestRequestTypeDef,
):
    pass


_RequiredDistributionOutputTypeDef = TypedDict(
    "_RequiredDistributionOutputTypeDef",
    {
        "region": str,
    },
)
_OptionalDistributionOutputTypeDef = TypedDict(
    "_OptionalDistributionOutputTypeDef",
    {
        "amiDistributionConfiguration": AmiDistributionConfigurationOutputTypeDef,
        "containerDistributionConfiguration": ContainerDistributionConfigurationOutputTypeDef,
        "licenseConfigurationArns": List[str],
        "launchTemplateConfigurations": List[LaunchTemplateConfigurationOutputTypeDef],
        "s3ExportConfiguration": S3ExportConfigurationOutputTypeDef,
        "fastLaunchConfigurations": List[FastLaunchConfigurationOutputTypeDef],
    },
    total=False,
)


class DistributionOutputTypeDef(
    _RequiredDistributionOutputTypeDef, _OptionalDistributionOutputTypeDef
):
    pass


_RequiredDistributionTypeDef = TypedDict(
    "_RequiredDistributionTypeDef",
    {
        "region": str,
    },
)
_OptionalDistributionTypeDef = TypedDict(
    "_OptionalDistributionTypeDef",
    {
        "amiDistributionConfiguration": AmiDistributionConfigurationTypeDef,
        "containerDistributionConfiguration": ContainerDistributionConfigurationTypeDef,
        "licenseConfigurationArns": Sequence[str],
        "launchTemplateConfigurations": Sequence[LaunchTemplateConfigurationTypeDef],
        "s3ExportConfiguration": S3ExportConfigurationTypeDef,
        "fastLaunchConfigurations": Sequence[FastLaunchConfigurationTypeDef],
    },
    total=False,
)


class DistributionTypeDef(_RequiredDistributionTypeDef, _OptionalDistributionTypeDef):
    pass


InfrastructureConfigurationTypeDef = TypedDict(
    "InfrastructureConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "instanceTypes": List[str],
        "instanceProfileName": str,
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": LoggingOutputTypeDef,
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "dateCreated": str,
        "dateUpdated": str,
        "resourceTags": Dict[str, str],
        "instanceMetadataOptions": InstanceMetadataOptionsOutputTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "instanceProfileName": str,
        "clientToken": str,
    },
)
_OptionalCreateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "instanceTypes": Sequence[str],
        "securityGroupIds": Sequence[str],
        "subnetId": str,
        "logging": LoggingTypeDef,
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "resourceTags": Mapping[str, str],
        "instanceMetadataOptions": InstanceMetadataOptionsTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateInfrastructureConfigurationRequestRequestTypeDef(
    _RequiredCreateInfrastructureConfigurationRequestRequestTypeDef,
    _OptionalCreateInfrastructureConfigurationRequestRequestTypeDef,
):
    pass


_RequiredUpdateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "instanceProfileName": str,
        "clientToken": str,
    },
)
_OptionalUpdateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "instanceTypes": Sequence[str],
        "securityGroupIds": Sequence[str],
        "subnetId": str,
        "logging": LoggingTypeDef,
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "resourceTags": Mapping[str, str],
        "instanceMetadataOptions": InstanceMetadataOptionsTypeDef,
    },
    total=False,
)


class UpdateInfrastructureConfigurationRequestRequestTypeDef(
    _RequiredUpdateInfrastructureConfigurationRequestRequestTypeDef,
    _OptionalUpdateInfrastructureConfigurationRequestRequestTypeDef,
):
    pass


ListImageScanFindingAggregationsResponseTypeDef = TypedDict(
    "ListImageScanFindingAggregationsResponseTypeDef",
    {
        "requestId": str,
        "aggregationType": str,
        "responses": List[ImageScanFindingAggregationTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageSummaryTypeDef = TypedDict(
    "ImageSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ImageTypeType,
        "version": str,
        "platform": PlatformType,
        "osVersion": str,
        "state": ImageStateTypeDef,
        "owner": str,
        "dateCreated": str,
        "outputResources": OutputResourcesTypeDef,
        "tags": Dict[str, str],
        "buildType": BuildTypeType,
        "imageSource": ImageSourceType,
    },
    total=False,
)

ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "awsAccountId": str,
        "imageBuildVersionArn": str,
        "imagePipelineArn": str,
        "type": str,
        "description": str,
        "title": str,
        "remediation": RemediationTypeDef,
        "severity": str,
        "firstObservedAt": datetime,
        "updatedAt": datetime,
        "inspectorScore": float,
        "inspectorScoreDetails": InspectorScoreDetailsTypeDef,
        "packageVulnerabilityDetails": PackageVulnerabilityDetailsTypeDef,
        "fixAvailable": str,
    },
    total=False,
)

GetImageRecipeResponseTypeDef = TypedDict(
    "GetImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "imageRecipe": ImageRecipeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainerRecipeTypeDef = TypedDict(
    "ContainerRecipeTypeDef",
    {
        "arn": str,
        "containerType": Literal["DOCKER"],
        "name": str,
        "description": str,
        "platform": PlatformType,
        "owner": str,
        "version": str,
        "components": List[ComponentConfigurationOutputTypeDef],
        "instanceConfiguration": InstanceConfigurationOutputTypeDef,
        "dockerfileTemplateData": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
        "targetRepository": TargetContainerRepositoryOutputTypeDef,
    },
    total=False,
)

_RequiredCreateContainerRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContainerRecipeRequestRequestTypeDef",
    {
        "containerType": Literal["DOCKER"],
        "name": str,
        "semanticVersion": str,
        "components": Sequence[ComponentConfigurationTypeDef],
        "parentImage": str,
        "targetRepository": TargetContainerRepositoryTypeDef,
        "clientToken": str,
    },
)
_OptionalCreateContainerRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContainerRecipeRequestRequestTypeDef",
    {
        "description": str,
        "instanceConfiguration": InstanceConfigurationTypeDef,
        "dockerfileTemplateData": str,
        "dockerfileTemplateUri": str,
        "platformOverride": PlatformType,
        "imageOsVersionOverride": str,
        "tags": Mapping[str, str],
        "workingDirectory": str,
        "kmsKeyId": str,
    },
    total=False,
)


class CreateContainerRecipeRequestRequestTypeDef(
    _RequiredCreateContainerRecipeRequestRequestTypeDef,
    _OptionalCreateContainerRecipeRequestRequestTypeDef,
):
    pass


GetImagePipelineResponseTypeDef = TypedDict(
    "GetImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "imagePipeline": ImagePipelineTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagePipelinesResponseTypeDef = TypedDict(
    "ListImagePipelinesResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineList": List[ImagePipelineTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDistributionConfigurationTypeDef = TypedDict(
    "_RequiredDistributionConfigurationTypeDef",
    {
        "timeoutMinutes": int,
    },
)
_OptionalDistributionConfigurationTypeDef = TypedDict(
    "_OptionalDistributionConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "distributions": List[DistributionOutputTypeDef],
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class DistributionConfigurationTypeDef(
    _RequiredDistributionConfigurationTypeDef, _OptionalDistributionConfigurationTypeDef
):
    pass


_RequiredCreateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDistributionConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "distributions": Sequence[DistributionTypeDef],
        "clientToken": str,
    },
)
_OptionalCreateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDistributionConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateDistributionConfigurationRequestRequestTypeDef(
    _RequiredCreateDistributionConfigurationRequestRequestTypeDef,
    _OptionalCreateDistributionConfigurationRequestRequestTypeDef,
):
    pass


_RequiredUpdateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
        "distributions": Sequence[DistributionTypeDef],
        "clientToken": str,
    },
)
_OptionalUpdateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDistributionConfigurationRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class UpdateDistributionConfigurationRequestRequestTypeDef(
    _RequiredUpdateDistributionConfigurationRequestRequestTypeDef,
    _OptionalUpdateDistributionConfigurationRequestRequestTypeDef,
):
    pass


GetInfrastructureConfigurationResponseTypeDef = TypedDict(
    "GetInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfiguration": InfrastructureConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageBuildVersionsResponseTypeDef = TypedDict(
    "ListImageBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List[ImageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagePipelineImagesResponseTypeDef = TypedDict(
    "ListImagePipelineImagesResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List[ImageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageScanFindingsResponseTypeDef = TypedDict(
    "ListImageScanFindingsResponseTypeDef",
    {
        "requestId": str,
        "findings": List[ImageScanFindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerRecipeResponseTypeDef = TypedDict(
    "GetContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "containerRecipe": ContainerRecipeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionConfigurationResponseTypeDef = TypedDict(
    "GetDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfiguration": DistributionConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "arn": str,
        "type": ImageTypeType,
        "name": str,
        "version": str,
        "platform": PlatformType,
        "enhancedImageMetadataEnabled": bool,
        "osVersion": str,
        "state": ImageStateTypeDef,
        "imageRecipe": ImageRecipeTypeDef,
        "containerRecipe": ContainerRecipeTypeDef,
        "sourcePipelineName": str,
        "sourcePipelineArn": str,
        "infrastructureConfiguration": InfrastructureConfigurationTypeDef,
        "distributionConfiguration": DistributionConfigurationTypeDef,
        "imageTestsConfiguration": ImageTestsConfigurationOutputTypeDef,
        "dateCreated": str,
        "outputResources": OutputResourcesTypeDef,
        "tags": Dict[str, str],
        "buildType": BuildTypeType,
        "imageSource": ImageSourceType,
        "scanState": ImageScanStateTypeDef,
        "imageScanningConfiguration": ImageScanningConfigurationOutputTypeDef,
    },
    total=False,
)

GetImageResponseTypeDef = TypedDict(
    "GetImageResponseTypeDef",
    {
        "requestId": str,
        "image": ImageTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
