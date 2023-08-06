"""
Type annotations for securityhub service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/type_defs/)

Usage::

    ```python
    from mypy_boto3_securityhub.type_defs import AcceptAdministratorInvitationRequestRequestTypeDef

    data: AcceptAdministratorInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AdminStatusType,
    AssociationStatusType,
    AutoEnableStandardsType,
    AwsIamAccessKeyStatusType,
    AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType,
    ComplianceStatusType,
    ControlFindingGeneratorType,
    ControlStatusType,
    FindingHistoryUpdateSourceTypeType,
    IntegrationTypeType,
    MalwareStateType,
    MalwareTypeType,
    MapFilterComparisonType,
    NetworkDirectionType,
    PartitionType,
    RecordStateType,
    RegionAvailabilityStatusType,
    RuleStatusType,
    SeverityLabelType,
    SeverityRatingType,
    SortOrderType,
    StandardsStatusType,
    StatusReasonCodeType,
    StringFilterComparisonType,
    ThreatIntelIndicatorCategoryType,
    ThreatIntelIndicatorTypeType,
    UnprocessedErrorCodeType,
    VerificationStateType,
    VulnerabilityFixAvailableType,
    WorkflowStateType,
    WorkflowStatusType,
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
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    "AcceptInvitationRequestRequestTypeDef",
    "AccountDetailsTypeDef",
    "ActionLocalIpDetailsOutputTypeDef",
    "ActionLocalIpDetailsTypeDef",
    "ActionLocalPortDetailsOutputTypeDef",
    "ActionLocalPortDetailsTypeDef",
    "DnsRequestActionOutputTypeDef",
    "CityOutputTypeDef",
    "CountryOutputTypeDef",
    "GeoLocationOutputTypeDef",
    "IpOrganizationDetailsOutputTypeDef",
    "CityTypeDef",
    "CountryTypeDef",
    "GeoLocationTypeDef",
    "IpOrganizationDetailsTypeDef",
    "ActionRemotePortDetailsOutputTypeDef",
    "ActionRemotePortDetailsTypeDef",
    "ActionTargetTypeDef",
    "DnsRequestActionTypeDef",
    "AdjustmentOutputTypeDef",
    "AdjustmentTypeDef",
    "AdminAccountTypeDef",
    "AssociatedStandardOutputTypeDef",
    "AssociatedStandardTypeDef",
    "AssociationStateDetailsOutputTypeDef",
    "AssociationStateDetailsTypeDef",
    "NoteUpdateOutputTypeDef",
    "RelatedFindingOutputTypeDef",
    "SeverityUpdateOutputTypeDef",
    "WorkflowUpdateOutputTypeDef",
    "NoteUpdateTypeDef",
    "RelatedFindingTypeDef",
    "SeverityUpdateTypeDef",
    "WorkflowUpdateTypeDef",
    "MapFilterOutputTypeDef",
    "NumberFilterOutputTypeDef",
    "StringFilterOutputTypeDef",
    "MapFilterTypeDef",
    "NumberFilterTypeDef",
    "StringFilterTypeDef",
    "AutomationRulesMetadataTypeDef",
    "AvailabilityZoneOutputTypeDef",
    "AvailabilityZoneTypeDef",
    "AwsAmazonMqBrokerEncryptionOptionsDetailsOutputTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef",
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsOutputTypeDef",
    "AwsAmazonMqBrokerUsersDetailsOutputTypeDef",
    "AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef",
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef",
    "AwsAmazonMqBrokerUsersDetailsTypeDef",
    "AwsAmazonMqBrokerLogsPendingDetailsOutputTypeDef",
    "AwsAmazonMqBrokerLogsPendingDetailsTypeDef",
    "AwsApiCallActionDomainDetailsOutputTypeDef",
    "AwsApiCallActionDomainDetailsTypeDef",
    "AwsApiGatewayAccessLogSettingsOutputTypeDef",
    "AwsApiGatewayAccessLogSettingsTypeDef",
    "AwsApiGatewayCanarySettingsOutputTypeDef",
    "AwsApiGatewayCanarySettingsTypeDef",
    "AwsApiGatewayEndpointConfigurationOutputTypeDef",
    "AwsApiGatewayEndpointConfigurationTypeDef",
    "AwsApiGatewayMethodSettingsOutputTypeDef",
    "AwsApiGatewayMethodSettingsTypeDef",
    "AwsCorsConfigurationOutputTypeDef",
    "AwsCorsConfigurationTypeDef",
    "AwsApiGatewayV2RouteSettingsOutputTypeDef",
    "AwsApiGatewayV2RouteSettingsTypeDef",
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsOutputTypeDef",
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsOutputTypeDef",
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsOutputTypeDef",
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiLogConfigDetailsOutputTypeDef",
    "AwsAppSyncGraphQlApiLogConfigDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsOutputTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsOutputTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsOutputTypeDef",
    "AwsAutoScalingLaunchConfigurationMetadataOptionsOutputTypeDef",
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef",
    "AwsBackupBackupPlanLifecycleDetailsOutputTypeDef",
    "AwsBackupBackupPlanLifecycleDetailsTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsOutputTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsTypeDef",
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsOutputTypeDef",
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef",
    "AwsBackupRecoveryPointCreatedByDetailsOutputTypeDef",
    "AwsBackupRecoveryPointCreatedByDetailsTypeDef",
    "AwsBackupRecoveryPointLifecycleDetailsOutputTypeDef",
    "AwsBackupRecoveryPointLifecycleDetailsTypeDef",
    "AwsCertificateManagerCertificateExtendedKeyUsageOutputTypeDef",
    "AwsCertificateManagerCertificateKeyUsageOutputTypeDef",
    "AwsCertificateManagerCertificateOptionsOutputTypeDef",
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    "AwsCertificateManagerCertificateOptionsTypeDef",
    "AwsCertificateManagerCertificateResourceRecordOutputTypeDef",
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    "AwsCloudFormationStackDriftInformationDetailsOutputTypeDef",
    "AwsCloudFormationStackOutputsDetailsOutputTypeDef",
    "AwsCloudFormationStackDriftInformationDetailsTypeDef",
    "AwsCloudFormationStackOutputsDetailsTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorOutputTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionDefaultCacheBehaviorOutputTypeDef",
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionLoggingOutputTypeDef",
    "AwsCloudFrontDistributionViewerCertificateOutputTypeDef",
    "AwsCloudFrontDistributionLoggingTypeDef",
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    "AwsCloudFrontDistributionOriginS3OriginConfigOutputTypeDef",
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    "AwsCloudTrailTrailDetailsOutputTypeDef",
    "AwsCloudTrailTrailDetailsTypeDef",
    "AwsCloudWatchAlarmDimensionsDetailsOutputTypeDef",
    "AwsCloudWatchAlarmDimensionsDetailsTypeDef",
    "AwsCodeBuildProjectArtifactsDetailsOutputTypeDef",
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    "AwsCodeBuildProjectSourceOutputTypeDef",
    "AwsCodeBuildProjectVpcConfigOutputTypeDef",
    "AwsCodeBuildProjectSourceTypeDef",
    "AwsCodeBuildProjectVpcConfigTypeDef",
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsOutputTypeDef",
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialOutputTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsOutputTypeDef",
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsOutputTypeDef",
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    "AwsDynamoDbTableAttributeDefinitionOutputTypeDef",
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    "AwsDynamoDbTableBillingModeSummaryOutputTypeDef",
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    "AwsDynamoDbTableKeySchemaOutputTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOutputTypeDef",
    "AwsDynamoDbTableRestoreSummaryOutputTypeDef",
    "AwsDynamoDbTableSseDescriptionOutputTypeDef",
    "AwsDynamoDbTableStreamSpecificationOutputTypeDef",
    "AwsDynamoDbTableKeySchemaTypeDef",
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    "AwsDynamoDbTableSseDescriptionTypeDef",
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    "AwsDynamoDbTableProjectionOutputTypeDef",
    "AwsDynamoDbTableProjectionTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOverrideOutputTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    "AwsEc2EipDetailsOutputTypeDef",
    "AwsEc2EipDetailsTypeDef",
    "AwsEc2InstanceMetadataOptionsOutputTypeDef",
    "AwsEc2InstanceMonitoringDetailsOutputTypeDef",
    "AwsEc2InstanceNetworkInterfacesDetailsOutputTypeDef",
    "AwsEc2InstanceMetadataOptionsTypeDef",
    "AwsEc2InstanceMonitoringDetailsTypeDef",
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef",
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataLicenseSetDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataMonitoringDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataPlacementDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef",
    "AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef",
    "AwsEc2LaunchTemplateDataPlacementDetailsTypeDef",
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef",
    "AwsEc2NetworkAclAssociationOutputTypeDef",
    "AwsEc2NetworkAclAssociationTypeDef",
    "IcmpTypeCodeOutputTypeDef",
    "PortRangeFromToOutputTypeDef",
    "IcmpTypeCodeTypeDef",
    "PortRangeFromToTypeDef",
    "AwsEc2NetworkInterfaceAttachmentOutputTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceIpV6AddressDetailOutputTypeDef",
    "AwsEc2NetworkInterfacePrivateIpAddressDetailOutputTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupOutputTypeDef",
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "PropagatingVgwSetDetailsOutputTypeDef",
    "RouteSetDetailsOutputTypeDef",
    "PropagatingVgwSetDetailsTypeDef",
    "RouteSetDetailsTypeDef",
    "AwsEc2SecurityGroupIpRangeOutputTypeDef",
    "AwsEc2SecurityGroupIpv6RangeOutputTypeDef",
    "AwsEc2SecurityGroupPrefixListIdOutputTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairOutputTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "Ipv6CidrBlockAssociationOutputTypeDef",
    "Ipv6CidrBlockAssociationTypeDef",
    "AwsEc2TransitGatewayDetailsOutputTypeDef",
    "AwsEc2TransitGatewayDetailsTypeDef",
    "AwsEc2VolumeAttachmentOutputTypeDef",
    "AwsEc2VolumeAttachmentTypeDef",
    "CidrBlockAssociationOutputTypeDef",
    "CidrBlockAssociationTypeDef",
    "AwsEc2VpcEndpointServiceServiceTypeDetailsOutputTypeDef",
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionStatusDetailsOutputTypeDef",
    "AwsEc2VpcPeeringConnectionStatusDetailsTypeDef",
    "VpcInfoCidrBlockSetDetailsOutputTypeDef",
    "VpcInfoIpv6CidrBlockSetDetailsOutputTypeDef",
    "VpcInfoPeeringOptionsDetailsOutputTypeDef",
    "VpcInfoCidrBlockSetDetailsTypeDef",
    "VpcInfoIpv6CidrBlockSetDetailsTypeDef",
    "VpcInfoPeeringOptionsDetailsTypeDef",
    "AwsEc2VpnConnectionRoutesDetailsOutputTypeDef",
    "AwsEc2VpnConnectionVgwTelemetryDetailsOutputTypeDef",
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    "AwsEcrContainerImageDetailsOutputTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "AwsEcrRepositoryImageScanningConfigurationDetailsOutputTypeDef",
    "AwsEcrRepositoryLifecyclePolicyDetailsOutputTypeDef",
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    "AwsEcsClusterClusterSettingsDetailsOutputTypeDef",
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsOutputTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsOutputTypeDef",
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    "AwsMountPointOutputTypeDef",
    "AwsMountPointTypeDef",
    "AwsEcsServiceCapacityProviderStrategyDetailsOutputTypeDef",
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsOutputTypeDef",
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    "AwsEcsServiceDeploymentControllerDetailsOutputTypeDef",
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    "AwsEcsServiceLoadBalancersDetailsOutputTypeDef",
    "AwsEcsServicePlacementConstraintsDetailsOutputTypeDef",
    "AwsEcsServicePlacementStrategiesDetailsOutputTypeDef",
    "AwsEcsServiceServiceRegistriesDetailsOutputTypeDef",
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesHostDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    "AwsEcsTaskVolumeHostDetailsOutputTypeDef",
    "AwsEcsTaskVolumeHostDetailsTypeDef",
    "AwsEfsAccessPointPosixUserDetailsOutputTypeDef",
    "AwsEfsAccessPointPosixUserDetailsTypeDef",
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsOutputTypeDef",
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkOutputTypeDef",
    "AwsElasticBeanstalkEnvironmentOptionSettingOutputTypeDef",
    "AwsElasticBeanstalkEnvironmentTierOutputTypeDef",
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsOutputTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsOutputTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsOutputTypeDef",
    "AwsElasticsearchDomainServiceSoftwareOptionsOutputTypeDef",
    "AwsElasticsearchDomainVPCOptionsOutputTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsOutputTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigOutputTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    "AwsElbAppCookieStickinessPolicyOutputTypeDef",
    "AwsElbAppCookieStickinessPolicyTypeDef",
    "AwsElbLbCookieStickinessPolicyOutputTypeDef",
    "AwsElbLbCookieStickinessPolicyTypeDef",
    "AwsElbLoadBalancerAccessLogOutputTypeDef",
    "AwsElbLoadBalancerAccessLogTypeDef",
    "AwsElbLoadBalancerAdditionalAttributeOutputTypeDef",
    "AwsElbLoadBalancerAdditionalAttributeTypeDef",
    "AwsElbLoadBalancerConnectionDrainingOutputTypeDef",
    "AwsElbLoadBalancerConnectionSettingsOutputTypeDef",
    "AwsElbLoadBalancerCrossZoneLoadBalancingOutputTypeDef",
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    "AwsElbLoadBalancerHealthCheckOutputTypeDef",
    "AwsElbLoadBalancerInstanceOutputTypeDef",
    "AwsElbLoadBalancerSourceSecurityGroupOutputTypeDef",
    "AwsElbLoadBalancerHealthCheckTypeDef",
    "AwsElbLoadBalancerInstanceTypeDef",
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    "AwsElbLoadBalancerListenerOutputTypeDef",
    "AwsElbLoadBalancerListenerTypeDef",
    "AwsElbv2LoadBalancerAttributeOutputTypeDef",
    "AwsElbv2LoadBalancerAttributeTypeDef",
    "LoadBalancerStateOutputTypeDef",
    "LoadBalancerStateTypeDef",
    "AwsEventSchemasRegistryDetailsOutputTypeDef",
    "AwsEventSchemasRegistryDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef",
    "AwsGuardDutyDetectorFeaturesDetailsOutputTypeDef",
    "AwsGuardDutyDetectorFeaturesDetailsTypeDef",
    "AwsIamAccessKeySessionContextAttributesOutputTypeDef",
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    "AwsIamAccessKeySessionContextSessionIssuerOutputTypeDef",
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    "AwsIamAttachedManagedPolicyOutputTypeDef",
    "AwsIamAttachedManagedPolicyTypeDef",
    "AwsIamGroupPolicyOutputTypeDef",
    "AwsIamGroupPolicyTypeDef",
    "AwsIamInstanceProfileRoleOutputTypeDef",
    "AwsIamInstanceProfileRoleTypeDef",
    "AwsIamPermissionsBoundaryOutputTypeDef",
    "AwsIamPermissionsBoundaryTypeDef",
    "AwsIamPolicyVersionOutputTypeDef",
    "AwsIamPolicyVersionTypeDef",
    "AwsIamRolePolicyOutputTypeDef",
    "AwsIamRolePolicyTypeDef",
    "AwsIamUserPolicyOutputTypeDef",
    "AwsIamUserPolicyTypeDef",
    "AwsKinesisStreamStreamEncryptionDetailsOutputTypeDef",
    "AwsKinesisStreamStreamEncryptionDetailsTypeDef",
    "AwsKmsKeyDetailsOutputTypeDef",
    "AwsKmsKeyDetailsTypeDef",
    "AwsLambdaFunctionCodeOutputTypeDef",
    "AwsLambdaFunctionCodeTypeDef",
    "AwsLambdaFunctionDeadLetterConfigOutputTypeDef",
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    "AwsLambdaFunctionLayerOutputTypeDef",
    "AwsLambdaFunctionTracingConfigOutputTypeDef",
    "AwsLambdaFunctionVpcConfigOutputTypeDef",
    "AwsLambdaFunctionLayerTypeDef",
    "AwsLambdaFunctionTracingConfigTypeDef",
    "AwsLambdaFunctionVpcConfigTypeDef",
    "AwsLambdaFunctionEnvironmentErrorOutputTypeDef",
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    "AwsLambdaLayerVersionDetailsOutputTypeDef",
    "AwsLambdaLayerVersionDetailsTypeDef",
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsOutputTypeDef",
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionOutputTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    "AwsRdsDbClusterAssociatedRoleOutputTypeDef",
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    "AwsRdsDbClusterMemberOutputTypeDef",
    "AwsRdsDbClusterOptionGroupMembershipOutputTypeDef",
    "AwsRdsDbDomainMembershipOutputTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupOutputTypeDef",
    "AwsRdsDbClusterMemberTypeDef",
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    "AwsRdsDbDomainMembershipTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef",
    "AwsRdsDbInstanceAssociatedRoleOutputTypeDef",
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    "AwsRdsDbInstanceEndpointOutputTypeDef",
    "AwsRdsDbOptionGroupMembershipOutputTypeDef",
    "AwsRdsDbParameterGroupOutputTypeDef",
    "AwsRdsDbProcessorFeatureOutputTypeDef",
    "AwsRdsDbStatusInfoOutputTypeDef",
    "AwsRdsDbInstanceEndpointTypeDef",
    "AwsRdsDbOptionGroupMembershipTypeDef",
    "AwsRdsDbParameterGroupTypeDef",
    "AwsRdsDbProcessorFeatureTypeDef",
    "AwsRdsDbStatusInfoTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsOutputTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    "AwsRdsDbSecurityGroupEc2SecurityGroupOutputTypeDef",
    "AwsRdsDbSecurityGroupIpRangeOutputTypeDef",
    "AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef",
    "AwsRdsDbSecurityGroupIpRangeTypeDef",
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneOutputTypeDef",
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    "AwsRdsEventSubscriptionDetailsOutputTypeDef",
    "AwsRdsEventSubscriptionDetailsTypeDef",
    "AwsRedshiftClusterClusterNodeOutputTypeDef",
    "AwsRedshiftClusterClusterNodeTypeDef",
    "AwsRedshiftClusterClusterParameterStatusOutputTypeDef",
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    "AwsRedshiftClusterClusterSecurityGroupOutputTypeDef",
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    "AwsRedshiftClusterClusterSnapshotCopyStatusOutputTypeDef",
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    "AwsRedshiftClusterDeferredMaintenanceWindowOutputTypeDef",
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    "AwsRedshiftClusterElasticIpStatusOutputTypeDef",
    "AwsRedshiftClusterEndpointOutputTypeDef",
    "AwsRedshiftClusterHsmStatusOutputTypeDef",
    "AwsRedshiftClusterIamRoleOutputTypeDef",
    "AwsRedshiftClusterLoggingStatusOutputTypeDef",
    "AwsRedshiftClusterPendingModifiedValuesOutputTypeDef",
    "AwsRedshiftClusterResizeInfoOutputTypeDef",
    "AwsRedshiftClusterRestoreStatusOutputTypeDef",
    "AwsRedshiftClusterVpcSecurityGroupOutputTypeDef",
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    "AwsRedshiftClusterEndpointTypeDef",
    "AwsRedshiftClusterHsmStatusTypeDef",
    "AwsRedshiftClusterIamRoleTypeDef",
    "AwsRedshiftClusterLoggingStatusTypeDef",
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    "AwsRedshiftClusterResizeInfoTypeDef",
    "AwsRedshiftClusterRestoreStatusTypeDef",
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    "AwsS3AccountPublicAccessBlockDetailsOutputTypeDef",
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    "AwsS3BucketBucketVersioningConfigurationOutputTypeDef",
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    "AwsS3BucketLoggingConfigurationOutputTypeDef",
    "AwsS3BucketLoggingConfigurationTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleOutputTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsOutputTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef",
    "AwsS3BucketServerSideEncryptionByDefaultOutputTypeDef",
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    "AwsS3BucketWebsiteConfigurationRedirectToOutputTypeDef",
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionOutputTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectOutputTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    "AwsS3ObjectDetailsOutputTypeDef",
    "AwsS3ObjectDetailsTypeDef",
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsOutputTypeDef",
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef",
    "AwsSecretsManagerSecretRotationRulesOutputTypeDef",
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    "BooleanFilterOutputTypeDef",
    "IpFilterOutputTypeDef",
    "KeywordFilterOutputTypeDef",
    "BooleanFilterTypeDef",
    "IpFilterTypeDef",
    "KeywordFilterTypeDef",
    "AwsSecurityFindingIdentifierOutputTypeDef",
    "AwsSecurityFindingIdentifierTypeDef",
    "MalwareOutputTypeDef",
    "NoteOutputTypeDef",
    "PatchSummaryOutputTypeDef",
    "ProcessDetailsOutputTypeDef",
    "SeverityOutputTypeDef",
    "ThreatIntelIndicatorOutputTypeDef",
    "WorkflowOutputTypeDef",
    "MalwareTypeDef",
    "NoteTypeDef",
    "PatchSummaryTypeDef",
    "ProcessDetailsTypeDef",
    "SeverityTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "WorkflowTypeDef",
    "AwsSnsTopicSubscriptionOutputTypeDef",
    "AwsSnsTopicSubscriptionTypeDef",
    "AwsSqsQueueDetailsOutputTypeDef",
    "AwsSqsQueueDetailsTypeDef",
    "AwsSsmComplianceSummaryOutputTypeDef",
    "AwsSsmComplianceSummaryTypeDef",
    "AwsStepFunctionStateMachineTracingConfigurationDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef",
    "AwsWafRateBasedRuleMatchPredicateOutputTypeDef",
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRateBasedRuleMatchPredicateOutputTypeDef",
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRulePredicateListDetailsOutputTypeDef",
    "AwsWafRegionalRulePredicateListDetailsTypeDef",
    "AwsWafRegionalRuleGroupRulesActionDetailsOutputTypeDef",
    "AwsWafRegionalRuleGroupRulesActionDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListActionDetailsOutputTypeDef",
    "AwsWafRegionalWebAclRulesListActionDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsOutputTypeDef",
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef",
    "AwsWafRulePredicateListDetailsOutputTypeDef",
    "AwsWafRulePredicateListDetailsTypeDef",
    "AwsWafRuleGroupRulesActionDetailsOutputTypeDef",
    "AwsWafRuleGroupRulesActionDetailsTypeDef",
    "WafActionOutputTypeDef",
    "WafExcludedRuleOutputTypeDef",
    "WafOverrideActionOutputTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "AwsWafv2CustomHttpHeaderOutputTypeDef",
    "AwsWafv2CustomHttpHeaderTypeDef",
    "AwsWafv2VisibilityConfigDetailsOutputTypeDef",
    "AwsWafv2VisibilityConfigDetailsTypeDef",
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsOutputTypeDef",
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef",
    "AwsXrayEncryptionConfigDetailsOutputTypeDef",
    "AwsXrayEncryptionConfigDetailsTypeDef",
    "BatchDeleteAutomationRulesRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UnprocessedAutomationRuleTypeDef",
    "BatchDisableStandardsRequestRequestTypeDef",
    "StandardsSubscriptionRequestTypeDef",
    "BatchGetAutomationRulesRequestRequestTypeDef",
    "BatchGetSecurityControlsRequestRequestTypeDef",
    "SecurityControlTypeDef",
    "UnprocessedSecurityControlTypeDef",
    "StandardsControlAssociationIdTypeDef",
    "StandardsControlAssociationDetailTypeDef",
    "ImportFindingsErrorTypeDef",
    "StandardsControlAssociationUpdateTypeDef",
    "CellOutputTypeDef",
    "CellTypeDef",
    "ClassificationStatusOutputTypeDef",
    "ClassificationStatusTypeDef",
    "StatusReasonOutputTypeDef",
    "StatusReasonTypeDef",
    "VolumeMountOutputTypeDef",
    "VolumeMountTypeDef",
    "CreateActionTargetRequestRequestTypeDef",
    "CreateFindingAggregatorRequestRequestTypeDef",
    "ResultTypeDef",
    "DateRangeOutputTypeDef",
    "DateRangeTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeleteActionTargetRequestRequestTypeDef",
    "DeleteFindingAggregatorRequestRequestTypeDef",
    "DeleteInsightRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeActionTargetsRequestRequestTypeDef",
    "DescribeHubRequestRequestTypeDef",
    "DescribeProductsRequestRequestTypeDef",
    "ProductTypeDef",
    "DescribeStandardsControlsRequestRequestTypeDef",
    "StandardsControlTypeDef",
    "DescribeStandardsRequestRequestTypeDef",
    "DisableImportFindingsForProductRequestRequestTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "EnableImportFindingsForProductRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "EnableSecurityHubRequestRequestTypeDef",
    "FilePathsOutputTypeDef",
    "FilePathsTypeDef",
    "FindingAggregatorTypeDef",
    "FindingHistoryUpdateSourceTypeDef",
    "FindingHistoryUpdateTypeDef",
    "FindingProviderSeverityOutputTypeDef",
    "FindingProviderSeverityTypeDef",
    "FirewallPolicyStatefulRuleGroupReferencesDetailsOutputTypeDef",
    "FirewallPolicyStatelessRuleGroupReferencesDetailsOutputTypeDef",
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    "InvitationTypeDef",
    "GetEnabledStandardsRequestRequestTypeDef",
    "GetFindingAggregatorRequestRequestTypeDef",
    "SortCriterionTypeDef",
    "GetInsightResultsRequestRequestTypeDef",
    "GetInsightsRequestRequestTypeDef",
    "GetMembersRequestRequestTypeDef",
    "MemberTypeDef",
    "InsightResultValueTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "ListAutomationRulesRequestRequestTypeDef",
    "ListEnabledProductsForImportRequestRequestTypeDef",
    "ListFindingAggregatorsRequestRequestTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListSecurityControlDefinitionsRequestRequestTypeDef",
    "SecurityControlDefinitionTypeDef",
    "ListStandardsControlAssociationsRequestRequestTypeDef",
    "StandardsControlAssociationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PortRangeOutputTypeDef",
    "PortRangeTypeDef",
    "RangeOutputTypeDef",
    "RecordOutputTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "RecommendationOutputTypeDef",
    "RecommendationTypeDef",
    "RuleGroupSourceListDetailsOutputTypeDef",
    "RuleGroupSourceListDetailsTypeDef",
    "RuleGroupSourceStatefulRulesHeaderDetailsOutputTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef",
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    "RuleGroupVariablesIpSetsDetailsOutputTypeDef",
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    "RuleGroupVariablesPortSetsDetailsOutputTypeDef",
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    "SoftwarePackageOutputTypeDef",
    "SoftwarePackageTypeDef",
    "StandardsManagedByTypeDef",
    "StandardsControlAssociationIdOutputTypeDef",
    "StandardsControlAssociationUpdateOutputTypeDef",
    "StandardsStatusReasonTypeDef",
    "StatelessCustomPublishMetricActionDimensionOutputTypeDef",
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateActionTargetRequestRequestTypeDef",
    "UpdateFindingAggregatorRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    "UpdateStandardsControlRequestRequestTypeDef",
    "VulnerabilityVendorOutputTypeDef",
    "VulnerabilityVendorTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "ActionRemoteIpDetailsOutputTypeDef",
    "ActionRemoteIpDetailsTypeDef",
    "CvssOutputTypeDef",
    "CvssTypeDef",
    "AssociationSetDetailsOutputTypeDef",
    "AssociationSetDetailsTypeDef",
    "AutomationRulesFindingFieldsUpdateOutputTypeDef",
    "AutomationRulesFindingFieldsUpdateTypeDef",
    "AwsAmazonMqBrokerLogsDetailsOutputTypeDef",
    "AwsAmazonMqBrokerLogsDetailsTypeDef",
    "AwsApiGatewayRestApiDetailsOutputTypeDef",
    "AwsApiGatewayRestApiDetailsTypeDef",
    "AwsApiGatewayStageDetailsOutputTypeDef",
    "AwsApiGatewayStageDetailsTypeDef",
    "AwsApiGatewayV2ApiDetailsOutputTypeDef",
    "AwsApiGatewayV2ApiDetailsTypeDef",
    "AwsApiGatewayV2StageDetailsOutputTypeDef",
    "AwsApiGatewayV2StageDetailsTypeDef",
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsOutputTypeDef",
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsOutputTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsOutputTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    "AwsBackupBackupPlanRuleCopyActionsDetailsOutputTypeDef",
    "AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef",
    "AwsBackupBackupVaultDetailsOutputTypeDef",
    "AwsBackupBackupVaultDetailsTypeDef",
    "AwsBackupRecoveryPointDetailsOutputTypeDef",
    "AwsBackupRecoveryPointDetailsTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    "AwsCloudFormationStackDetailsOutputTypeDef",
    "AwsCloudFormationStackDetailsTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    "AwsCloudWatchAlarmDetailsOutputTypeDef",
    "AwsCloudWatchAlarmDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentOutputTypeDef",
    "AwsCodeBuildProjectEnvironmentTypeDef",
    "AwsCodeBuildProjectLogsConfigDetailsOutputTypeDef",
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexOutputTypeDef",
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    "AwsEc2InstanceDetailsOutputTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef",
    "AwsEc2NetworkAclEntryOutputTypeDef",
    "AwsEc2NetworkAclEntryTypeDef",
    "AwsEc2NetworkInterfaceDetailsOutputTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2SecurityGroupIpPermissionOutputTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SubnetDetailsOutputTypeDef",
    "AwsEc2SubnetDetailsTypeDef",
    "AwsEc2VolumeDetailsOutputTypeDef",
    "AwsEc2VolumeDetailsTypeDef",
    "AwsEc2VpcDetailsOutputTypeDef",
    "AwsEc2VpcDetailsTypeDef",
    "AwsEc2VpcEndpointServiceDetailsOutputTypeDef",
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsOutputTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    "AwsEcrRepositoryDetailsOutputTypeDef",
    "AwsEcrRepositoryDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsOutputTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    "AwsEcsContainerDetailsOutputTypeDef",
    "AwsEcsContainerDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDetailsOutputTypeDef",
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskVolumeDetailsOutputTypeDef",
    "AwsEcsTaskVolumeDetailsTypeDef",
    "AwsEfsAccessPointRootDirectoryDetailsOutputTypeDef",
    "AwsEfsAccessPointRootDirectoryDetailsTypeDef",
    "AwsEksClusterLoggingDetailsOutputTypeDef",
    "AwsEksClusterLoggingDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsOutputTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsOutputTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    "AwsElbLoadBalancerPoliciesOutputTypeDef",
    "AwsElbLoadBalancerPoliciesTypeDef",
    "AwsElbLoadBalancerAttributesOutputTypeDef",
    "AwsElbLoadBalancerAttributesTypeDef",
    "AwsElbLoadBalancerListenerDescriptionOutputTypeDef",
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    "AwsElbv2LoadBalancerDetailsOutputTypeDef",
    "AwsElbv2LoadBalancerDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef",
    "AwsIamAccessKeySessionContextOutputTypeDef",
    "AwsIamAccessKeySessionContextTypeDef",
    "AwsIamGroupDetailsOutputTypeDef",
    "AwsIamGroupDetailsTypeDef",
    "AwsIamInstanceProfileOutputTypeDef",
    "AwsIamInstanceProfileTypeDef",
    "AwsIamPolicyDetailsOutputTypeDef",
    "AwsIamPolicyDetailsTypeDef",
    "AwsIamUserDetailsOutputTypeDef",
    "AwsIamUserDetailsTypeDef",
    "AwsKinesisStreamDetailsOutputTypeDef",
    "AwsKinesisStreamDetailsTypeDef",
    "AwsLambdaFunctionEnvironmentOutputTypeDef",
    "AwsLambdaFunctionEnvironmentTypeDef",
    "AwsNetworkFirewallFirewallDetailsOutputTypeDef",
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    "AwsRdsDbClusterDetailsOutputTypeDef",
    "AwsRdsDbClusterDetailsTypeDef",
    "AwsRdsDbClusterSnapshotDetailsOutputTypeDef",
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    "AwsRdsDbSnapshotDetailsOutputTypeDef",
    "AwsRdsDbSnapshotDetailsTypeDef",
    "AwsRdsDbPendingModifiedValuesOutputTypeDef",
    "AwsRdsDbPendingModifiedValuesTypeDef",
    "AwsRdsDbSecurityGroupDetailsOutputTypeDef",
    "AwsRdsDbSecurityGroupDetailsTypeDef",
    "AwsRdsDbSubnetGroupSubnetOutputTypeDef",
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    "AwsRedshiftClusterClusterParameterGroupOutputTypeDef",
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDetailsOutputTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef",
    "AwsS3BucketServerSideEncryptionRuleOutputTypeDef",
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleOutputTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    "AwsSageMakerNotebookInstanceDetailsOutputTypeDef",
    "AwsSageMakerNotebookInstanceDetailsTypeDef",
    "AwsSecretsManagerSecretDetailsOutputTypeDef",
    "AwsSecretsManagerSecretDetailsTypeDef",
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    "BatchUpdateFindingsRequestRequestTypeDef",
    "GetFindingHistoryRequestRequestTypeDef",
    "AwsSnsTopicDetailsOutputTypeDef",
    "AwsSnsTopicDetailsTypeDef",
    "AwsSsmPatchOutputTypeDef",
    "AwsSsmPatchTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef",
    "AwsWafRateBasedRuleDetailsOutputTypeDef",
    "AwsWafRateBasedRuleDetailsTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsOutputTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    "AwsWafRegionalRuleDetailsOutputTypeDef",
    "AwsWafRegionalRuleDetailsTypeDef",
    "AwsWafRegionalRuleGroupRulesDetailsOutputTypeDef",
    "AwsWafRegionalRuleGroupRulesDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListDetailsOutputTypeDef",
    "AwsWafRegionalWebAclRulesListDetailsTypeDef",
    "AwsWafRuleDetailsOutputTypeDef",
    "AwsWafRuleDetailsTypeDef",
    "AwsWafRuleGroupRulesDetailsOutputTypeDef",
    "AwsWafRuleGroupRulesDetailsTypeDef",
    "AwsWafWebAclRuleOutputTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsOutputTypeDef",
    "AwsWafv2CustomResponseDetailsOutputTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsTypeDef",
    "AwsWafv2CustomResponseDetailsTypeDef",
    "AwsWafv2WebAclCaptchaConfigDetailsOutputTypeDef",
    "AwsWafv2WebAclCaptchaConfigDetailsTypeDef",
    "CreateActionTargetResponseTypeDef",
    "CreateAutomationRuleResponseTypeDef",
    "CreateFindingAggregatorResponseTypeDef",
    "CreateInsightResponseTypeDef",
    "DeleteActionTargetResponseTypeDef",
    "DeleteInsightResponseTypeDef",
    "DescribeActionTargetsResponseTypeDef",
    "DescribeHubResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "EnableImportFindingsForProductResponseTypeDef",
    "GetFindingAggregatorResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "ListAutomationRulesResponseTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateFindingAggregatorResponseTypeDef",
    "BatchDeleteAutomationRulesResponseTypeDef",
    "BatchUpdateAutomationRulesResponseTypeDef",
    "BatchEnableStandardsRequestRequestTypeDef",
    "BatchGetSecurityControlsResponseTypeDef",
    "BatchGetStandardsControlAssociationsRequestRequestTypeDef",
    "BatchImportFindingsResponseTypeDef",
    "BatchUpdateStandardsControlAssociationsRequestRequestTypeDef",
    "ComplianceOutputTypeDef",
    "ComplianceTypeDef",
    "ContainerDetailsOutputTypeDef",
    "ContainerDetailsTypeDef",
    "CreateMembersResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "InviteMembersResponseTypeDef",
    "DateFilterOutputTypeDef",
    "DateFilterTypeDef",
    "DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef",
    "DescribeProductsRequestDescribeProductsPaginateTypeDef",
    "DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef",
    "DescribeStandardsRequestDescribeStandardsPaginateTypeDef",
    "GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef",
    "GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef",
    "GetInsightsRequestGetInsightsPaginateTypeDef",
    "ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef",
    "ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef",
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    "ListMembersRequestListMembersPaginateTypeDef",
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    "ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef",
    "ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef",
    "DescribeProductsResponseTypeDef",
    "DescribeStandardsControlsResponseTypeDef",
    "ThreatOutputTypeDef",
    "ThreatTypeDef",
    "ListFindingAggregatorsResponseTypeDef",
    "FindingHistoryRecordTypeDef",
    "FindingProviderFieldsOutputTypeDef",
    "FindingProviderFieldsTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "GetMembersResponseTypeDef",
    "ListMembersResponseTypeDef",
    "InsightResultsTypeDef",
    "ListSecurityControlDefinitionsResponseTypeDef",
    "ListStandardsControlAssociationsResponseTypeDef",
    "NetworkOutputTypeDef",
    "NetworkPathComponentDetailsOutputTypeDef",
    "NetworkPathComponentDetailsTypeDef",
    "NetworkTypeDef",
    "PageOutputTypeDef",
    "PageTypeDef",
    "RemediationOutputTypeDef",
    "RemediationTypeDef",
    "RuleGroupSourceStatefulRulesDetailsOutputTypeDef",
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    "RuleGroupVariablesOutputTypeDef",
    "RuleGroupVariablesTypeDef",
    "StandardTypeDef",
    "UnprocessedStandardsControlAssociationTypeDef",
    "UnprocessedStandardsControlAssociationUpdateTypeDef",
    "StandardsSubscriptionTypeDef",
    "StatelessCustomPublishMetricActionOutputTypeDef",
    "StatelessCustomPublishMetricActionTypeDef",
    "AwsApiCallActionOutputTypeDef",
    "NetworkConnectionActionOutputTypeDef",
    "PortProbeDetailOutputTypeDef",
    "AwsApiCallActionTypeDef",
    "NetworkConnectionActionTypeDef",
    "PortProbeDetailTypeDef",
    "VulnerabilityOutputTypeDef",
    "VulnerabilityTypeDef",
    "AwsEc2RouteTableDetailsOutputTypeDef",
    "AwsEc2RouteTableDetailsTypeDef",
    "AutomationRulesActionOutputTypeDef",
    "AutomationRulesActionTypeDef",
    "AwsAmazonMqBrokerDetailsOutputTypeDef",
    "AwsAmazonMqBrokerDetailsTypeDef",
    "AwsAppSyncGraphQlApiDetailsOutputTypeDef",
    "AwsAppSyncGraphQlApiDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationDetailsOutputTypeDef",
    "AwsAthenaWorkGroupConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    "AwsBackupBackupPlanRuleDetailsOutputTypeDef",
    "AwsBackupBackupPlanRuleDetailsTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    "AwsCloudFrontDistributionOriginItemOutputTypeDef",
    "AwsCloudFrontDistributionOriginItemTypeDef",
    "AwsCloudFrontDistributionOriginGroupOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    "AwsCodeBuildProjectDetailsOutputTypeDef",
    "AwsCodeBuildProjectDetailsTypeDef",
    "AwsDynamoDbTableReplicaOutputTypeDef",
    "AwsDynamoDbTableReplicaTypeDef",
    "AwsEc2LaunchTemplateDataDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataDetailsTypeDef",
    "AwsEc2NetworkAclDetailsOutputTypeDef",
    "AwsEc2NetworkAclDetailsTypeDef",
    "AwsEc2SecurityGroupDetailsOutputTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsOutputTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsTypeDef",
    "AwsEc2VpnConnectionDetailsOutputTypeDef",
    "AwsEc2VpnConnectionDetailsTypeDef",
    "AwsEcsClusterConfigurationDetailsOutputTypeDef",
    "AwsEcsClusterConfigurationDetailsTypeDef",
    "AwsEcsServiceDetailsOutputTypeDef",
    "AwsEcsServiceDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    "AwsEcsTaskDetailsOutputTypeDef",
    "AwsEcsTaskDetailsTypeDef",
    "AwsEfsAccessPointDetailsOutputTypeDef",
    "AwsEfsAccessPointDetailsTypeDef",
    "AwsEksClusterDetailsOutputTypeDef",
    "AwsEksClusterDetailsTypeDef",
    "AwsElasticsearchDomainDetailsOutputTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AwsElbLoadBalancerDetailsOutputTypeDef",
    "AwsElbLoadBalancerDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef",
    "AwsIamAccessKeyDetailsOutputTypeDef",
    "AwsIamAccessKeyDetailsTypeDef",
    "AwsIamRoleDetailsOutputTypeDef",
    "AwsIamRoleDetailsTypeDef",
    "AwsLambdaFunctionDetailsOutputTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "AwsOpenSearchServiceDomainDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    "AwsRdsDbSubnetGroupOutputTypeDef",
    "AwsRdsDbSubnetGroupTypeDef",
    "AwsRedshiftClusterDetailsOutputTypeDef",
    "AwsRedshiftClusterDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationFilterOutputTypeDef",
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    "AwsS3BucketObjectLockConfigurationOutputTypeDef",
    "AwsS3BucketObjectLockConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    "AwsS3BucketWebsiteConfigurationOutputTypeDef",
    "AwsS3BucketWebsiteConfigurationTypeDef",
    "BatchUpdateFindingsResponseTypeDef",
    "AwsSsmPatchComplianceDetailsOutputTypeDef",
    "AwsSsmPatchComplianceDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef",
    "AwsWafRegionalRuleGroupDetailsOutputTypeDef",
    "AwsWafRegionalRuleGroupDetailsTypeDef",
    "AwsWafRegionalWebAclDetailsOutputTypeDef",
    "AwsWafRegionalWebAclDetailsTypeDef",
    "AwsWafRuleGroupDetailsOutputTypeDef",
    "AwsWafRuleGroupDetailsTypeDef",
    "AwsWafWebAclDetailsOutputTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "AwsWafv2ActionAllowDetailsOutputTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsOutputTypeDef",
    "AwsWafv2RulesActionCountDetailsOutputTypeDef",
    "AwsWafv2ActionBlockDetailsOutputTypeDef",
    "AwsWafv2ActionAllowDetailsTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsTypeDef",
    "AwsWafv2RulesActionCountDetailsTypeDef",
    "AwsWafv2ActionBlockDetailsTypeDef",
    "AutomationRulesFindingFiltersOutputTypeDef",
    "AwsSecurityFindingFiltersOutputTypeDef",
    "AutomationRulesFindingFiltersTypeDef",
    "AwsSecurityFindingFiltersTypeDef",
    "GetFindingHistoryResponseTypeDef",
    "GetInsightResultsResponseTypeDef",
    "NetworkHeaderOutputTypeDef",
    "NetworkHeaderTypeDef",
    "OccurrencesOutputTypeDef",
    "OccurrencesTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionOutputTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    "DescribeStandardsResponseTypeDef",
    "BatchGetStandardsControlAssociationsResponseTypeDef",
    "BatchUpdateStandardsControlAssociationsResponseTypeDef",
    "BatchDisableStandardsResponseTypeDef",
    "BatchEnableStandardsResponseTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "StatelessCustomActionDefinitionOutputTypeDef",
    "StatelessCustomActionDefinitionTypeDef",
    "PortProbeActionOutputTypeDef",
    "PortProbeActionTypeDef",
    "AwsAthenaWorkGroupDetailsOutputTypeDef",
    "AwsAthenaWorkGroupDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsTypeDef",
    "AwsCertificateManagerCertificateDetailsOutputTypeDef",
    "AwsCertificateManagerCertificateDetailsTypeDef",
    "AwsCloudFrontDistributionOriginsOutputTypeDef",
    "AwsCloudFrontDistributionOriginsTypeDef",
    "AwsCloudFrontDistributionOriginGroupsOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    "AwsDynamoDbTableDetailsOutputTypeDef",
    "AwsDynamoDbTableDetailsTypeDef",
    "AwsEc2LaunchTemplateDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDetailsTypeDef",
    "AwsEcsClusterDetailsOutputTypeDef",
    "AwsEcsClusterDetailsTypeDef",
    "AwsEcsTaskDefinitionDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDataSourcesDetailsTypeDef",
    "AwsRdsDbInstanceDetailsOutputTypeDef",
    "AwsRdsDbInstanceDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationDetailOutputTypeDef",
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    "AwsStepFunctionStateMachineDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineDetailsTypeDef",
    "AwsWafv2RulesActionDetailsOutputTypeDef",
    "AwsWafv2WebAclActionDetailsOutputTypeDef",
    "AwsWafv2RulesActionDetailsTypeDef",
    "AwsWafv2WebAclActionDetailsTypeDef",
    "AutomationRulesConfigTypeDef",
    "InsightTypeDef",
    "CreateAutomationRuleRequestRequestTypeDef",
    "UpdateAutomationRulesRequestItemTypeDef",
    "CreateInsightRequestRequestTypeDef",
    "GetFindingsRequestGetFindingsPaginateTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "UpdateInsightRequestRequestTypeDef",
    "NetworkPathComponentOutputTypeDef",
    "NetworkPathComponentTypeDef",
    "CustomDataIdentifiersDetectionsOutputTypeDef",
    "SensitiveDataDetectionsOutputTypeDef",
    "CustomDataIdentifiersDetectionsTypeDef",
    "SensitiveDataDetectionsTypeDef",
    "RuleGroupSourceStatelessRulesDetailsOutputTypeDef",
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef",
    "RuleGroupSourceCustomActionsDetailsOutputTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "AwsBackupBackupPlanDetailsOutputTypeDef",
    "AwsBackupBackupPlanDetailsTypeDef",
    "AwsCloudFrontDistributionDetailsOutputTypeDef",
    "AwsCloudFrontDistributionDetailsTypeDef",
    "AwsGuardDutyDetectorDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationOutputTypeDef",
    "AwsS3BucketNotificationConfigurationTypeDef",
    "AwsWafv2RulesDetailsOutputTypeDef",
    "AwsWafv2RulesDetailsTypeDef",
    "BatchGetAutomationRulesResponseTypeDef",
    "GetInsightsResponseTypeDef",
    "BatchUpdateAutomationRulesRequestRequestTypeDef",
    "CustomDataIdentifiersResultOutputTypeDef",
    "SensitiveDataResultOutputTypeDef",
    "CustomDataIdentifiersResultTypeDef",
    "SensitiveDataResultTypeDef",
    "FirewallPolicyDetailsOutputTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef",
    "FirewallPolicyDetailsTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    "AwsWafv2RuleGroupDetailsOutputTypeDef",
    "AwsWafv2WebAclDetailsOutputTypeDef",
    "AwsWafv2RuleGroupDetailsTypeDef",
    "AwsWafv2WebAclDetailsTypeDef",
    "ClassificationResultOutputTypeDef",
    "ClassificationResultTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef",
    "RuleGroupSourceOutputTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    "RuleGroupSourceTypeDef",
    "AwsS3BucketDetailsOutputTypeDef",
    "AwsS3BucketDetailsTypeDef",
    "DataClassificationDetailsOutputTypeDef",
    "DataClassificationDetailsTypeDef",
    "RuleGroupDetailsOutputTypeDef",
    "RuleGroupDetailsTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsOutputTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    "ResourceDetailsOutputTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceOutputTypeDef",
    "ResourceTypeDef",
    "AwsSecurityFindingOutputTypeDef",
    "AwsSecurityFindingTypeDef",
    "GetFindingsResponseTypeDef",
    "BatchImportFindingsRequestRequestTypeDef",
)

AcceptAdministratorInvitationRequestRequestTypeDef = TypedDict(
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    {
        "AdministratorId": str,
        "InvitationId": str,
    },
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "MasterId": str,
        "InvitationId": str,
    },
)

_RequiredAccountDetailsTypeDef = TypedDict(
    "_RequiredAccountDetailsTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalAccountDetailsTypeDef = TypedDict(
    "_OptionalAccountDetailsTypeDef",
    {
        "Email": str,
    },
    total=False,
)


class AccountDetailsTypeDef(_RequiredAccountDetailsTypeDef, _OptionalAccountDetailsTypeDef):
    pass


ActionLocalIpDetailsOutputTypeDef = TypedDict(
    "ActionLocalIpDetailsOutputTypeDef",
    {
        "IpAddressV4": str,
    },
)

ActionLocalIpDetailsTypeDef = TypedDict(
    "ActionLocalIpDetailsTypeDef",
    {
        "IpAddressV4": str,
    },
    total=False,
)

ActionLocalPortDetailsOutputTypeDef = TypedDict(
    "ActionLocalPortDetailsOutputTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
)

ActionLocalPortDetailsTypeDef = TypedDict(
    "ActionLocalPortDetailsTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
    total=False,
)

DnsRequestActionOutputTypeDef = TypedDict(
    "DnsRequestActionOutputTypeDef",
    {
        "Domain": str,
        "Protocol": str,
        "Blocked": bool,
    },
)

CityOutputTypeDef = TypedDict(
    "CityOutputTypeDef",
    {
        "CityName": str,
    },
)

CountryOutputTypeDef = TypedDict(
    "CountryOutputTypeDef",
    {
        "CountryCode": str,
        "CountryName": str,
    },
)

GeoLocationOutputTypeDef = TypedDict(
    "GeoLocationOutputTypeDef",
    {
        "Lon": float,
        "Lat": float,
    },
)

IpOrganizationDetailsOutputTypeDef = TypedDict(
    "IpOrganizationDetailsOutputTypeDef",
    {
        "Asn": int,
        "AsnOrg": str,
        "Isp": str,
        "Org": str,
    },
)

CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": str,
    },
    total=False,
)

CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": str,
        "CountryName": str,
    },
    total=False,
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lon": float,
        "Lat": float,
    },
    total=False,
)

IpOrganizationDetailsTypeDef = TypedDict(
    "IpOrganizationDetailsTypeDef",
    {
        "Asn": int,
        "AsnOrg": str,
        "Isp": str,
        "Org": str,
    },
    total=False,
)

ActionRemotePortDetailsOutputTypeDef = TypedDict(
    "ActionRemotePortDetailsOutputTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
)

ActionRemotePortDetailsTypeDef = TypedDict(
    "ActionRemotePortDetailsTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
    total=False,
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ActionTargetArn": str,
        "Name": str,
        "Description": str,
    },
)

DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": str,
        "Protocol": str,
        "Blocked": bool,
    },
    total=False,
)

AdjustmentOutputTypeDef = TypedDict(
    "AdjustmentOutputTypeDef",
    {
        "Metric": str,
        "Reason": str,
    },
)

AdjustmentTypeDef = TypedDict(
    "AdjustmentTypeDef",
    {
        "Metric": str,
        "Reason": str,
    },
    total=False,
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AccountId": str,
        "Status": AdminStatusType,
    },
)

AssociatedStandardOutputTypeDef = TypedDict(
    "AssociatedStandardOutputTypeDef",
    {
        "StandardsId": str,
    },
)

AssociatedStandardTypeDef = TypedDict(
    "AssociatedStandardTypeDef",
    {
        "StandardsId": str,
    },
    total=False,
)

AssociationStateDetailsOutputTypeDef = TypedDict(
    "AssociationStateDetailsOutputTypeDef",
    {
        "State": str,
        "StatusMessage": str,
    },
)

AssociationStateDetailsTypeDef = TypedDict(
    "AssociationStateDetailsTypeDef",
    {
        "State": str,
        "StatusMessage": str,
    },
    total=False,
)

NoteUpdateOutputTypeDef = TypedDict(
    "NoteUpdateOutputTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
    },
)

RelatedFindingOutputTypeDef = TypedDict(
    "RelatedFindingOutputTypeDef",
    {
        "ProductArn": str,
        "Id": str,
    },
)

SeverityUpdateOutputTypeDef = TypedDict(
    "SeverityUpdateOutputTypeDef",
    {
        "Normalized": int,
        "Product": float,
        "Label": SeverityLabelType,
    },
)

WorkflowUpdateOutputTypeDef = TypedDict(
    "WorkflowUpdateOutputTypeDef",
    {
        "Status": WorkflowStatusType,
    },
)

NoteUpdateTypeDef = TypedDict(
    "NoteUpdateTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
    },
)

RelatedFindingTypeDef = TypedDict(
    "RelatedFindingTypeDef",
    {
        "ProductArn": str,
        "Id": str,
    },
)

SeverityUpdateTypeDef = TypedDict(
    "SeverityUpdateTypeDef",
    {
        "Normalized": int,
        "Product": float,
        "Label": SeverityLabelType,
    },
    total=False,
)

WorkflowUpdateTypeDef = TypedDict(
    "WorkflowUpdateTypeDef",
    {
        "Status": WorkflowStatusType,
    },
    total=False,
)

MapFilterOutputTypeDef = TypedDict(
    "MapFilterOutputTypeDef",
    {
        "Key": str,
        "Value": str,
        "Comparison": MapFilterComparisonType,
    },
)

NumberFilterOutputTypeDef = TypedDict(
    "NumberFilterOutputTypeDef",
    {
        "Gte": float,
        "Lte": float,
        "Eq": float,
    },
)

StringFilterOutputTypeDef = TypedDict(
    "StringFilterOutputTypeDef",
    {
        "Value": str,
        "Comparison": StringFilterComparisonType,
    },
)

MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Comparison": MapFilterComparisonType,
    },
    total=False,
)

NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef",
    {
        "Gte": float,
        "Lte": float,
        "Eq": float,
    },
    total=False,
)

StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "Value": str,
        "Comparison": StringFilterComparisonType,
    },
    total=False,
)

AutomationRulesMetadataTypeDef = TypedDict(
    "AutomationRulesMetadataTypeDef",
    {
        "RuleArn": str,
        "RuleStatus": RuleStatusType,
        "RuleOrder": int,
        "RuleName": str,
        "Description": str,
        "IsTerminal": bool,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "CreatedBy": str,
    },
)

AvailabilityZoneOutputTypeDef = TypedDict(
    "AvailabilityZoneOutputTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
    },
    total=False,
)

AwsAmazonMqBrokerEncryptionOptionsDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerEncryptionOptionsDetailsOutputTypeDef",
    {
        "KmsKeyId": str,
        "UseAwsOwnedKey": bool,
    },
)

AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleName": str,
        "RoleSearchMatching": str,
        "RoleSearchSubtree": bool,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserRoleName": str,
        "UserSearchMatching": str,
        "UserSearchSubtree": bool,
    },
)

AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsOutputTypeDef",
    {
        "DayOfWeek": str,
        "TimeOfDay": str,
        "TimeZone": str,
    },
)

AwsAmazonMqBrokerUsersDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerUsersDetailsOutputTypeDef",
    {
        "PendingChange": str,
        "Username": str,
    },
)

AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef",
    {
        "KmsKeyId": str,
        "UseAwsOwnedKey": bool,
    },
    total=False,
)

AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef",
    {
        "Hosts": Sequence[str],
        "RoleBase": str,
        "RoleName": str,
        "RoleSearchMatching": str,
        "RoleSearchSubtree": bool,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserRoleName": str,
        "UserSearchMatching": str,
        "UserSearchSubtree": bool,
    },
    total=False,
)

AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef",
    {
        "DayOfWeek": str,
        "TimeOfDay": str,
        "TimeZone": str,
    },
    total=False,
)

AwsAmazonMqBrokerUsersDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerUsersDetailsTypeDef",
    {
        "PendingChange": str,
        "Username": str,
    },
    total=False,
)

AwsAmazonMqBrokerLogsPendingDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerLogsPendingDetailsOutputTypeDef",
    {
        "Audit": bool,
        "General": bool,
    },
)

AwsAmazonMqBrokerLogsPendingDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLogsPendingDetailsTypeDef",
    {
        "Audit": bool,
        "General": bool,
    },
    total=False,
)

AwsApiCallActionDomainDetailsOutputTypeDef = TypedDict(
    "AwsApiCallActionDomainDetailsOutputTypeDef",
    {
        "Domain": str,
    },
)

AwsApiCallActionDomainDetailsTypeDef = TypedDict(
    "AwsApiCallActionDomainDetailsTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

AwsApiGatewayAccessLogSettingsOutputTypeDef = TypedDict(
    "AwsApiGatewayAccessLogSettingsOutputTypeDef",
    {
        "Format": str,
        "DestinationArn": str,
    },
)

AwsApiGatewayAccessLogSettingsTypeDef = TypedDict(
    "AwsApiGatewayAccessLogSettingsTypeDef",
    {
        "Format": str,
        "DestinationArn": str,
    },
    total=False,
)

AwsApiGatewayCanarySettingsOutputTypeDef = TypedDict(
    "AwsApiGatewayCanarySettingsOutputTypeDef",
    {
        "PercentTraffic": float,
        "DeploymentId": str,
        "StageVariableOverrides": Dict[str, str],
        "UseStageCache": bool,
    },
)

AwsApiGatewayCanarySettingsTypeDef = TypedDict(
    "AwsApiGatewayCanarySettingsTypeDef",
    {
        "PercentTraffic": float,
        "DeploymentId": str,
        "StageVariableOverrides": Mapping[str, str],
        "UseStageCache": bool,
    },
    total=False,
)

AwsApiGatewayEndpointConfigurationOutputTypeDef = TypedDict(
    "AwsApiGatewayEndpointConfigurationOutputTypeDef",
    {
        "Types": List[str],
    },
)

AwsApiGatewayEndpointConfigurationTypeDef = TypedDict(
    "AwsApiGatewayEndpointConfigurationTypeDef",
    {
        "Types": Sequence[str],
    },
    total=False,
)

AwsApiGatewayMethodSettingsOutputTypeDef = TypedDict(
    "AwsApiGatewayMethodSettingsOutputTypeDef",
    {
        "MetricsEnabled": bool,
        "LoggingLevel": str,
        "DataTraceEnabled": bool,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
        "CachingEnabled": bool,
        "CacheTtlInSeconds": int,
        "CacheDataEncrypted": bool,
        "RequireAuthorizationForCacheControl": bool,
        "UnauthorizedCacheControlHeaderStrategy": str,
        "HttpMethod": str,
        "ResourcePath": str,
    },
)

AwsApiGatewayMethodSettingsTypeDef = TypedDict(
    "AwsApiGatewayMethodSettingsTypeDef",
    {
        "MetricsEnabled": bool,
        "LoggingLevel": str,
        "DataTraceEnabled": bool,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
        "CachingEnabled": bool,
        "CacheTtlInSeconds": int,
        "CacheDataEncrypted": bool,
        "RequireAuthorizationForCacheControl": bool,
        "UnauthorizedCacheControlHeaderStrategy": str,
        "HttpMethod": str,
        "ResourcePath": str,
    },
    total=False,
)

AwsCorsConfigurationOutputTypeDef = TypedDict(
    "AwsCorsConfigurationOutputTypeDef",
    {
        "AllowOrigins": List[str],
        "AllowCredentials": bool,
        "ExposeHeaders": List[str],
        "MaxAge": int,
        "AllowMethods": List[str],
        "AllowHeaders": List[str],
    },
)

AwsCorsConfigurationTypeDef = TypedDict(
    "AwsCorsConfigurationTypeDef",
    {
        "AllowOrigins": Sequence[str],
        "AllowCredentials": bool,
        "ExposeHeaders": Sequence[str],
        "MaxAge": int,
        "AllowMethods": Sequence[str],
        "AllowHeaders": Sequence[str],
    },
    total=False,
)

AwsApiGatewayV2RouteSettingsOutputTypeDef = TypedDict(
    "AwsApiGatewayV2RouteSettingsOutputTypeDef",
    {
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "DataTraceEnabled": bool,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
)

AwsApiGatewayV2RouteSettingsTypeDef = TypedDict(
    "AwsApiGatewayV2RouteSettingsTypeDef",
    {
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "DataTraceEnabled": bool,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsOutputTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsOutputTypeDef",
    {
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerUri": str,
        "IdentityValidationExpression": str,
    },
)

AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsOutputTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsOutputTypeDef",
    {
        "AuthTtL": int,
        "ClientId": str,
        "IatTtL": int,
        "Issuer": str,
    },
)

AwsAppSyncGraphQlApiUserPoolConfigDetailsOutputTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsOutputTypeDef",
    {
        "AppIdClientRegex": str,
        "AwsRegion": str,
        "DefaultAction": str,
        "UserPoolId": str,
    },
)

AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef",
    {
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerUri": str,
        "IdentityValidationExpression": str,
    },
    total=False,
)

AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef",
    {
        "AuthTtL": int,
        "ClientId": str,
        "IatTtL": int,
        "Issuer": str,
    },
    total=False,
)

AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef",
    {
        "AppIdClientRegex": str,
        "AwsRegion": str,
        "DefaultAction": str,
        "UserPoolId": str,
    },
    total=False,
)

AwsAppSyncGraphQlApiLogConfigDetailsOutputTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiLogConfigDetailsOutputTypeDef",
    {
        "CloudWatchLogsRoleArn": str,
        "ExcludeVerboseContent": bool,
        "FieldLogLevel": str,
    },
)

AwsAppSyncGraphQlApiLogConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiLogConfigDetailsTypeDef",
    {
        "CloudWatchLogsRoleArn": str,
        "ExcludeVerboseContent": bool,
        "FieldLogLevel": str,
    },
    total=False,
)

AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsOutputTypeDef",
    {
        "EncryptionOption": str,
        "KmsKey": str,
    },
)

AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef",
    {
        "EncryptionOption": str,
        "KmsKey": str,
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsOutputTypeDef",
    {
        "Value": str,
    },
)

AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    {
        "Value": str,
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationOutputTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
)

AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsOutputTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsOutputTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": str,
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": str,
    },
    total=False,
)

AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsOutputTypeDef",
    {
        "DeleteOnTermination": bool,
        "Encrypted": bool,
        "Iops": int,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
    },
)

AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    {
        "DeleteOnTermination": bool,
        "Encrypted": bool,
        "Iops": int,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
    },
    total=False,
)

AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsOutputTypeDef",
    {
        "Enabled": bool,
    },
)

AwsAutoScalingLaunchConfigurationMetadataOptionsOutputTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationMetadataOptionsOutputTypeDef",
    {
        "HttpEndpoint": str,
        "HttpPutResponseHopLimit": int,
        "HttpTokens": str,
    },
)

AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    {
        "HttpEndpoint": str,
        "HttpPutResponseHopLimit": int,
        "HttpTokens": str,
    },
    total=False,
)

AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef",
    {
        "BackupOptions": Dict[str, str],
        "ResourceType": str,
    },
)

AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef",
    {
        "BackupOptions": Mapping[str, str],
        "ResourceType": str,
    },
    total=False,
)

AwsBackupBackupPlanLifecycleDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanLifecycleDetailsOutputTypeDef",
    {
        "DeleteAfterDays": int,
        "MoveToColdStorageAfterDays": int,
    },
)

AwsBackupBackupPlanLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanLifecycleDetailsTypeDef",
    {
        "DeleteAfterDays": int,
        "MoveToColdStorageAfterDays": int,
    },
    total=False,
)

AwsBackupBackupVaultNotificationsDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupVaultNotificationsDetailsOutputTypeDef",
    {
        "BackupVaultEvents": List[str],
        "SnsTopicArn": str,
    },
)

AwsBackupBackupVaultNotificationsDetailsTypeDef = TypedDict(
    "AwsBackupBackupVaultNotificationsDetailsTypeDef",
    {
        "BackupVaultEvents": Sequence[str],
        "SnsTopicArn": str,
    },
    total=False,
)

AwsBackupRecoveryPointCalculatedLifecycleDetailsOutputTypeDef = TypedDict(
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsOutputTypeDef",
    {
        "DeleteAt": str,
        "MoveToColdStorageAt": str,
    },
)

AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef",
    {
        "DeleteAt": str,
        "MoveToColdStorageAt": str,
    },
    total=False,
)

AwsBackupRecoveryPointCreatedByDetailsOutputTypeDef = TypedDict(
    "AwsBackupRecoveryPointCreatedByDetailsOutputTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
    },
)

AwsBackupRecoveryPointCreatedByDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointCreatedByDetailsTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
    },
    total=False,
)

AwsBackupRecoveryPointLifecycleDetailsOutputTypeDef = TypedDict(
    "AwsBackupRecoveryPointLifecycleDetailsOutputTypeDef",
    {
        "DeleteAfterDays": int,
        "MoveToColdStorageAfterDays": int,
    },
)

AwsBackupRecoveryPointLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointLifecycleDetailsTypeDef",
    {
        "DeleteAfterDays": int,
        "MoveToColdStorageAfterDays": int,
    },
    total=False,
)

AwsCertificateManagerCertificateExtendedKeyUsageOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateExtendedKeyUsageOutputTypeDef",
    {
        "Name": str,
        "OId": str,
    },
)

AwsCertificateManagerCertificateKeyUsageOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateKeyUsageOutputTypeDef",
    {
        "Name": str,
    },
)

AwsCertificateManagerCertificateOptionsOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateOptionsOutputTypeDef",
    {
        "CertificateTransparencyLoggingPreference": str,
    },
)

AwsCertificateManagerCertificateExtendedKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    {
        "Name": str,
        "OId": str,
    },
    total=False,
)

AwsCertificateManagerCertificateKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    {
        "Name": str,
    },
    total=False,
)

AwsCertificateManagerCertificateOptionsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateOptionsTypeDef",
    {
        "CertificateTransparencyLoggingPreference": str,
    },
    total=False,
)

AwsCertificateManagerCertificateResourceRecordOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateResourceRecordOutputTypeDef",
    {
        "Name": str,
        "Type": str,
        "Value": str,
    },
)

AwsCertificateManagerCertificateResourceRecordTypeDef = TypedDict(
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    {
        "Name": str,
        "Type": str,
        "Value": str,
    },
    total=False,
)

AwsCloudFormationStackDriftInformationDetailsOutputTypeDef = TypedDict(
    "AwsCloudFormationStackDriftInformationDetailsOutputTypeDef",
    {
        "StackDriftStatus": str,
    },
)

AwsCloudFormationStackOutputsDetailsOutputTypeDef = TypedDict(
    "AwsCloudFormationStackOutputsDetailsOutputTypeDef",
    {
        "Description": str,
        "OutputKey": str,
        "OutputValue": str,
    },
)

AwsCloudFormationStackDriftInformationDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackDriftInformationDetailsTypeDef",
    {
        "StackDriftStatus": str,
    },
    total=False,
)

AwsCloudFormationStackOutputsDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackOutputsDetailsTypeDef",
    {
        "Description": str,
        "OutputKey": str,
        "OutputValue": str,
    },
    total=False,
)

AwsCloudFrontDistributionCacheBehaviorOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorOutputTypeDef",
    {
        "ViewerProtocolPolicy": str,
    },
)

AwsCloudFrontDistributionCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": str,
    },
    total=False,
)

AwsCloudFrontDistributionDefaultCacheBehaviorOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionDefaultCacheBehaviorOutputTypeDef",
    {
        "ViewerProtocolPolicy": str,
    },
)

AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": str,
    },
    total=False,
)

AwsCloudFrontDistributionLoggingOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionLoggingOutputTypeDef",
    {
        "Bucket": str,
        "Enabled": bool,
        "IncludeCookies": bool,
        "Prefix": str,
    },
)

AwsCloudFrontDistributionViewerCertificateOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionViewerCertificateOutputTypeDef",
    {
        "AcmCertificateArn": str,
        "Certificate": str,
        "CertificateSource": str,
        "CloudFrontDefaultCertificate": bool,
        "IamCertificateId": str,
        "MinimumProtocolVersion": str,
        "SslSupportMethod": str,
    },
)

AwsCloudFrontDistributionLoggingTypeDef = TypedDict(
    "AwsCloudFrontDistributionLoggingTypeDef",
    {
        "Bucket": str,
        "Enabled": bool,
        "IncludeCookies": bool,
        "Prefix": str,
    },
    total=False,
)

AwsCloudFrontDistributionViewerCertificateTypeDef = TypedDict(
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    {
        "AcmCertificateArn": str,
        "Certificate": str,
        "CertificateSource": str,
        "CloudFrontDefaultCertificate": bool,
        "IamCertificateId": str,
        "MinimumProtocolVersion": str,
        "SslSupportMethod": str,
    },
    total=False,
)

AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef",
    {
        "Items": List[str],
        "Quantity": int,
    },
)

AwsCloudFrontDistributionOriginSslProtocolsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginSslProtocolsTypeDef",
    {
        "Items": Sequence[str],
        "Quantity": int,
    },
    total=False,
)

AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef",
    {
        "Items": List[int],
        "Quantity": int,
    },
)

AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    {
        "Items": Sequence[int],
        "Quantity": int,
    },
    total=False,
)

AwsCloudFrontDistributionOriginS3OriginConfigOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginS3OriginConfigOutputTypeDef",
    {
        "OriginAccessIdentity": str,
    },
)

AwsCloudFrontDistributionOriginS3OriginConfigTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    {
        "OriginAccessIdentity": str,
    },
    total=False,
)

AwsCloudTrailTrailDetailsOutputTypeDef = TypedDict(
    "AwsCloudTrailTrailDetailsOutputTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "HasCustomEventSelectors": bool,
        "HomeRegion": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "IsOrganizationTrail": bool,
        "KmsKeyId": str,
        "LogFileValidationEnabled": bool,
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicArn": str,
        "SnsTopicName": str,
        "TrailArn": str,
    },
)

AwsCloudTrailTrailDetailsTypeDef = TypedDict(
    "AwsCloudTrailTrailDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "HasCustomEventSelectors": bool,
        "HomeRegion": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "IsOrganizationTrail": bool,
        "KmsKeyId": str,
        "LogFileValidationEnabled": bool,
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicArn": str,
        "SnsTopicName": str,
        "TrailArn": str,
    },
    total=False,
)

AwsCloudWatchAlarmDimensionsDetailsOutputTypeDef = TypedDict(
    "AwsCloudWatchAlarmDimensionsDetailsOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

AwsCloudWatchAlarmDimensionsDetailsTypeDef = TypedDict(
    "AwsCloudWatchAlarmDimensionsDetailsTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsCodeBuildProjectArtifactsDetailsOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectArtifactsDetailsOutputTypeDef",
    {
        "ArtifactIdentifier": str,
        "EncryptionDisabled": bool,
        "Location": str,
        "Name": str,
        "NamespaceType": str,
        "OverrideArtifactName": bool,
        "Packaging": str,
        "Path": str,
        "Type": str,
    },
)

AwsCodeBuildProjectArtifactsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    {
        "ArtifactIdentifier": str,
        "EncryptionDisabled": bool,
        "Location": str,
        "Name": str,
        "NamespaceType": str,
        "OverrideArtifactName": bool,
        "Packaging": str,
        "Path": str,
        "Type": str,
    },
    total=False,
)

AwsCodeBuildProjectSourceOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceOutputTypeDef",
    {
        "Type": str,
        "Location": str,
        "GitCloneDepth": int,
        "InsecureSsl": bool,
    },
)

AwsCodeBuildProjectVpcConfigOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigOutputTypeDef",
    {
        "VpcId": str,
        "Subnets": List[str],
        "SecurityGroupIds": List[str],
    },
)

AwsCodeBuildProjectSourceTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceTypeDef",
    {
        "Type": str,
        "Location": str,
        "GitCloneDepth": int,
        "InsecureSsl": bool,
    },
    total=False,
)

AwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigTypeDef",
    {
        "VpcId": str,
        "Subnets": Sequence[str],
        "SecurityGroupIds": Sequence[str],
    },
    total=False,
)

AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsOutputTypeDef",
    {
        "Name": str,
        "Type": str,
        "Value": str,
    },
)

AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    {
        "Name": str,
        "Type": str,
        "Value": str,
    },
    total=False,
)

AwsCodeBuildProjectEnvironmentRegistryCredentialOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentRegistryCredentialOutputTypeDef",
    {
        "Credential": str,
        "CredentialProvider": str,
    },
)

AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    {
        "Credential": str,
        "CredentialProvider": str,
    },
    total=False,
)

AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsOutputTypeDef",
    {
        "GroupName": str,
        "Status": str,
        "StreamName": str,
    },
)

AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    {
        "GroupName": str,
        "Status": str,
        "StreamName": str,
    },
    total=False,
)

AwsCodeBuildProjectLogsConfigS3LogsDetailsOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsOutputTypeDef",
    {
        "EncryptionDisabled": bool,
        "Location": str,
        "Status": str,
    },
)

AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    {
        "EncryptionDisabled": bool,
        "Location": str,
        "Status": str,
    },
    total=False,
)

AwsDynamoDbTableAttributeDefinitionOutputTypeDef = TypedDict(
    "AwsDynamoDbTableAttributeDefinitionOutputTypeDef",
    {
        "AttributeName": str,
        "AttributeType": str,
    },
)

AwsDynamoDbTableAttributeDefinitionTypeDef = TypedDict(
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": str,
    },
    total=False,
)

AwsDynamoDbTableBillingModeSummaryOutputTypeDef = TypedDict(
    "AwsDynamoDbTableBillingModeSummaryOutputTypeDef",
    {
        "BillingMode": str,
        "LastUpdateToPayPerRequestDateTime": str,
    },
)

AwsDynamoDbTableBillingModeSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    {
        "BillingMode": str,
        "LastUpdateToPayPerRequestDateTime": str,
    },
    total=False,
)

AwsDynamoDbTableKeySchemaOutputTypeDef = TypedDict(
    "AwsDynamoDbTableKeySchemaOutputTypeDef",
    {
        "AttributeName": str,
        "KeyType": str,
    },
)

AwsDynamoDbTableProvisionedThroughputOutputTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputOutputTypeDef",
    {
        "LastDecreaseDateTime": str,
        "LastIncreaseDateTime": str,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

AwsDynamoDbTableRestoreSummaryOutputTypeDef = TypedDict(
    "AwsDynamoDbTableRestoreSummaryOutputTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": str,
        "RestoreInProgress": bool,
    },
)

AwsDynamoDbTableSseDescriptionOutputTypeDef = TypedDict(
    "AwsDynamoDbTableSseDescriptionOutputTypeDef",
    {
        "InaccessibleEncryptionDateTime": str,
        "Status": str,
        "SseType": str,
        "KmsMasterKeyArn": str,
    },
)

AwsDynamoDbTableStreamSpecificationOutputTypeDef = TypedDict(
    "AwsDynamoDbTableStreamSpecificationOutputTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": str,
    },
)

AwsDynamoDbTableKeySchemaTypeDef = TypedDict(
    "AwsDynamoDbTableKeySchemaTypeDef",
    {
        "AttributeName": str,
        "KeyType": str,
    },
    total=False,
)

AwsDynamoDbTableProvisionedThroughputTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    {
        "LastDecreaseDateTime": str,
        "LastIncreaseDateTime": str,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

AwsDynamoDbTableRestoreSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": str,
        "RestoreInProgress": bool,
    },
    total=False,
)

AwsDynamoDbTableSseDescriptionTypeDef = TypedDict(
    "AwsDynamoDbTableSseDescriptionTypeDef",
    {
        "InaccessibleEncryptionDateTime": str,
        "Status": str,
        "SseType": str,
        "KmsMasterKeyArn": str,
    },
    total=False,
)

AwsDynamoDbTableStreamSpecificationTypeDef = TypedDict(
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": str,
    },
    total=False,
)

AwsDynamoDbTableProjectionOutputTypeDef = TypedDict(
    "AwsDynamoDbTableProjectionOutputTypeDef",
    {
        "NonKeyAttributes": List[str],
        "ProjectionType": str,
    },
)

AwsDynamoDbTableProjectionTypeDef = TypedDict(
    "AwsDynamoDbTableProjectionTypeDef",
    {
        "NonKeyAttributes": Sequence[str],
        "ProjectionType": str,
    },
    total=False,
)

AwsDynamoDbTableProvisionedThroughputOverrideOutputTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputOverrideOutputTypeDef",
    {
        "ReadCapacityUnits": int,
    },
)

AwsDynamoDbTableProvisionedThroughputOverrideTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
)

AwsEc2EipDetailsOutputTypeDef = TypedDict(
    "AwsEc2EipDetailsOutputTypeDef",
    {
        "InstanceId": str,
        "PublicIp": str,
        "AllocationId": str,
        "AssociationId": str,
        "Domain": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "NetworkInterfaceId": str,
        "NetworkInterfaceOwnerId": str,
        "PrivateIpAddress": str,
    },
)

AwsEc2EipDetailsTypeDef = TypedDict(
    "AwsEc2EipDetailsTypeDef",
    {
        "InstanceId": str,
        "PublicIp": str,
        "AllocationId": str,
        "AssociationId": str,
        "Domain": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "NetworkInterfaceId": str,
        "NetworkInterfaceOwnerId": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

AwsEc2InstanceMetadataOptionsOutputTypeDef = TypedDict(
    "AwsEc2InstanceMetadataOptionsOutputTypeDef",
    {
        "HttpEndpoint": str,
        "HttpProtocolIpv6": str,
        "HttpPutResponseHopLimit": int,
        "HttpTokens": str,
        "InstanceMetadataTags": str,
    },
)

AwsEc2InstanceMonitoringDetailsOutputTypeDef = TypedDict(
    "AwsEc2InstanceMonitoringDetailsOutputTypeDef",
    {
        "State": str,
    },
)

AwsEc2InstanceNetworkInterfacesDetailsOutputTypeDef = TypedDict(
    "AwsEc2InstanceNetworkInterfacesDetailsOutputTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)

AwsEc2InstanceMetadataOptionsTypeDef = TypedDict(
    "AwsEc2InstanceMetadataOptionsTypeDef",
    {
        "HttpEndpoint": str,
        "HttpProtocolIpv6": str,
        "HttpPutResponseHopLimit": int,
        "HttpTokens": str,
        "InstanceMetadataTags": str,
    },
    total=False,
)

AwsEc2InstanceMonitoringDetailsTypeDef = TypedDict(
    "AwsEc2InstanceMonitoringDetailsTypeDef",
    {
        "State": str,
    },
    total=False,
)

AwsEc2InstanceNetworkInterfacesDetailsTypeDef = TypedDict(
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    {
        "NetworkInterfaceId": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsOutputTypeDef",
    {
        "DeleteOnTermination": bool,
        "Encrypted": bool,
        "Iops": int,
        "KmsKeyId": str,
        "SnapshotId": str,
        "Throughput": int,
        "VolumeSize": int,
        "VolumeType": str,
    },
)

AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef",
    {
        "DeleteOnTermination": bool,
        "Encrypted": bool,
        "Iops": int,
        "KmsKeyId": str,
        "SnapshotId": str,
        "Throughput": int,
        "VolumeSize": int,
        "VolumeType": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsOutputTypeDef",
    {
        "CapacityReservationId": str,
        "CapacityReservationResourceGroupArn": str,
    },
)

AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef",
    {
        "CapacityReservationId": str,
        "CapacityReservationResourceGroupArn": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataCpuOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsOutputTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
    },
)

AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
    },
    total=False,
)

AwsEc2LaunchTemplateDataCreditSpecificationDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsOutputTypeDef",
    {
        "CpuCredits": str,
    },
)

AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef",
    {
        "CpuCredits": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsOutputTypeDef",
    {
        "Type": str,
    },
)

AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsOutputTypeDef",
    {
        "Count": int,
        "Type": str,
    },
)

AwsEc2LaunchTemplateDataEnclaveOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsOutputTypeDef",
    {
        "Enabled": bool,
    },
)

AwsEc2LaunchTemplateDataHibernationOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsOutputTypeDef",
    {
        "Configured": bool,
    },
)

AwsEc2LaunchTemplateDataIamInstanceProfileDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
)

AwsEc2LaunchTemplateDataLicenseSetDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataLicenseSetDetailsOutputTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsOutputTypeDef",
    {
        "AutoRecovery": str,
    },
)

AwsEc2LaunchTemplateDataMetadataOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsOutputTypeDef",
    {
        "HttpEndpoint": str,
        "HttpProtocolIpv6": str,
        "HttpTokens": str,
        "HttpPutResponseHopLimit": int,
        "InstanceMetadataTags": str,
    },
)

AwsEc2LaunchTemplateDataMonitoringDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMonitoringDetailsOutputTypeDef",
    {
        "Enabled": bool,
    },
)

AwsEc2LaunchTemplateDataPlacementDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataPlacementDetailsOutputTypeDef",
    {
        "Affinity": str,
        "AvailabilityZone": str,
        "GroupName": str,
        "HostId": str,
        "HostResourceGroupArn": str,
        "PartitionNumber": int,
        "SpreadDomain": str,
        "Tenancy": str,
    },
)

AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsOutputTypeDef",
    {
        "EnableResourceNameDnsAAAARecord": bool,
        "EnableResourceNameDnsARecord": bool,
        "HostnameType": str,
    },
)

AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef",
    {
        "Type": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef",
    {
        "Count": int,
        "Type": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef",
    {
        "AutoRecovery": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef",
    {
        "HttpEndpoint": str,
        "HttpProtocolIpv6": str,
        "HttpTokens": str,
        "HttpPutResponseHopLimit": int,
        "InstanceMetadataTags": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AwsEc2LaunchTemplateDataPlacementDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataPlacementDetailsTypeDef",
    {
        "Affinity": str,
        "AvailabilityZone": str,
        "GroupName": str,
        "HostId": str,
        "HostResourceGroupArn": str,
        "PartitionNumber": int,
        "SpreadDomain": str,
        "Tenancy": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef",
    {
        "EnableResourceNameDnsAAAARecord": bool,
        "EnableResourceNameDnsARecord": bool,
        "HostnameType": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsOutputTypeDef",
    {
        "BlockDurationMinutes": int,
        "InstanceInterruptionBehavior": str,
        "MaxPrice": str,
        "SpotInstanceType": str,
        "ValidUntil": str,
    },
)

AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef",
    {
        "BlockDurationMinutes": int,
        "InstanceInterruptionBehavior": str,
        "MaxPrice": str,
        "SpotInstanceType": str,
        "ValidUntil": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsOutputTypeDef",
    {
        "Max": int,
        "Min": int,
    },
)

AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef",
    {
        "Max": int,
        "Min": int,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsOutputTypeDef = (
    TypedDict(
        "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsOutputTypeDef",
        {
            "Max": int,
            "Min": int,
        },
    )
)

AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef",
    {
        "Max": int,
        "Min": int,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsOutputTypeDef = (
    TypedDict(
        "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsOutputTypeDef",
        {
            "Max": int,
            "Min": int,
        },
    )
)

AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef",
    {
        "Max": int,
        "Min": int,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsOutputTypeDef",
    {
        "Max": float,
        "Min": float,
    },
)

AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsOutputTypeDef",
    {
        "Max": int,
        "Min": int,
    },
)

AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsOutputTypeDef",
    {
        "Max": int,
        "Min": int,
    },
)

AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsOutputTypeDef",
    {
        "Max": float,
        "Min": float,
    },
)

AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsOutputTypeDef",
    {
        "Max": int,
        "Min": int,
    },
)

AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef",
    {
        "Max": float,
        "Min": float,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef",
    {
        "Max": int,
        "Min": int,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef",
    {
        "Max": int,
        "Min": int,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef",
    {
        "Max": float,
        "Min": float,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef",
    {
        "Max": int,
        "Min": int,
    },
    total=False,
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsOutputTypeDef",
    {
        "Ipv4Prefix": str,
    },
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsOutputTypeDef",
    {
        "Ipv6Address": str,
    },
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsOutputTypeDef",
    {
        "Ipv6Prefix": str,
    },
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsOutputTypeDef",
    {
        "Primary": bool,
        "PrivateIpAddress": str,
    },
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef",
    {
        "Ipv4Prefix": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef",
    {
        "Ipv6Address": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef",
    {
        "Ipv6Prefix": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef",
    {
        "Primary": bool,
        "PrivateIpAddress": str,
    },
    total=False,
)

AwsEc2NetworkAclAssociationOutputTypeDef = TypedDict(
    "AwsEc2NetworkAclAssociationOutputTypeDef",
    {
        "NetworkAclAssociationId": str,
        "NetworkAclId": str,
        "SubnetId": str,
    },
)

AwsEc2NetworkAclAssociationTypeDef = TypedDict(
    "AwsEc2NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": str,
        "NetworkAclId": str,
        "SubnetId": str,
    },
    total=False,
)

IcmpTypeCodeOutputTypeDef = TypedDict(
    "IcmpTypeCodeOutputTypeDef",
    {
        "Code": int,
        "Type": int,
    },
)

PortRangeFromToOutputTypeDef = TypedDict(
    "PortRangeFromToOutputTypeDef",
    {
        "From": int,
        "To": int,
    },
)

IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": int,
        "Type": int,
    },
    total=False,
)

PortRangeFromToTypeDef = TypedDict(
    "PortRangeFromToTypeDef",
    {
        "From": int,
        "To": int,
    },
    total=False,
)

AwsEc2NetworkInterfaceAttachmentOutputTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceAttachmentOutputTypeDef",
    {
        "AttachTime": str,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": str,
    },
)

AwsEc2NetworkInterfaceAttachmentTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": str,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": str,
    },
    total=False,
)

AwsEc2NetworkInterfaceIpV6AddressDetailOutputTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceIpV6AddressDetailOutputTypeDef",
    {
        "IpV6Address": str,
    },
)

AwsEc2NetworkInterfacePrivateIpAddressDetailOutputTypeDef = TypedDict(
    "AwsEc2NetworkInterfacePrivateIpAddressDetailOutputTypeDef",
    {
        "PrivateIpAddress": str,
        "PrivateDnsName": str,
    },
)

AwsEc2NetworkInterfaceSecurityGroupOutputTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceSecurityGroupOutputTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
    },
)

AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    {
        "IpV6Address": str,
    },
    total=False,
)

AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    {
        "PrivateIpAddress": str,
        "PrivateDnsName": str,
    },
    total=False,
)

AwsEc2NetworkInterfaceSecurityGroupTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
    },
    total=False,
)

PropagatingVgwSetDetailsOutputTypeDef = TypedDict(
    "PropagatingVgwSetDetailsOutputTypeDef",
    {
        "GatewayId": str,
    },
)

RouteSetDetailsOutputTypeDef = TypedDict(
    "RouteSetDetailsOutputTypeDef",
    {
        "CarrierGatewayId": str,
        "CoreNetworkArn": str,
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "LocalGatewayId": str,
        "NatGatewayId": str,
        "NetworkInterfaceId": str,
        "Origin": str,
        "State": str,
        "TransitGatewayId": str,
        "VpcPeeringConnectionId": str,
    },
)

PropagatingVgwSetDetailsTypeDef = TypedDict(
    "PropagatingVgwSetDetailsTypeDef",
    {
        "GatewayId": str,
    },
    total=False,
)

RouteSetDetailsTypeDef = TypedDict(
    "RouteSetDetailsTypeDef",
    {
        "CarrierGatewayId": str,
        "CoreNetworkArn": str,
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "LocalGatewayId": str,
        "NatGatewayId": str,
        "NetworkInterfaceId": str,
        "Origin": str,
        "State": str,
        "TransitGatewayId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

AwsEc2SecurityGroupIpRangeOutputTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpRangeOutputTypeDef",
    {
        "CidrIp": str,
    },
)

AwsEc2SecurityGroupIpv6RangeOutputTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpv6RangeOutputTypeDef",
    {
        "CidrIpv6": str,
    },
)

AwsEc2SecurityGroupPrefixListIdOutputTypeDef = TypedDict(
    "AwsEc2SecurityGroupPrefixListIdOutputTypeDef",
    {
        "PrefixListId": str,
    },
)

AwsEc2SecurityGroupUserIdGroupPairOutputTypeDef = TypedDict(
    "AwsEc2SecurityGroupUserIdGroupPairOutputTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
)

AwsEc2SecurityGroupIpRangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpRangeTypeDef",
    {
        "CidrIp": str,
    },
    total=False,
)

AwsEc2SecurityGroupIpv6RangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    {
        "CidrIpv6": str,
    },
    total=False,
)

AwsEc2SecurityGroupPrefixListIdTypeDef = TypedDict(
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    {
        "PrefixListId": str,
    },
    total=False,
)

AwsEc2SecurityGroupUserIdGroupPairTypeDef = TypedDict(
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

Ipv6CidrBlockAssociationOutputTypeDef = TypedDict(
    "Ipv6CidrBlockAssociationOutputTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "CidrBlockState": str,
    },
)

Ipv6CidrBlockAssociationTypeDef = TypedDict(
    "Ipv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "CidrBlockState": str,
    },
    total=False,
)

AwsEc2TransitGatewayDetailsOutputTypeDef = TypedDict(
    "AwsEc2TransitGatewayDetailsOutputTypeDef",
    {
        "Id": str,
        "Description": str,
        "DefaultRouteTablePropagation": str,
        "AutoAcceptSharedAttachments": str,
        "DefaultRouteTableAssociation": str,
        "TransitGatewayCidrBlocks": List[str],
        "AssociationDefaultRouteTableId": str,
        "PropagationDefaultRouteTableId": str,
        "VpnEcmpSupport": str,
        "DnsSupport": str,
        "MulticastSupport": str,
        "AmazonSideAsn": int,
    },
)

AwsEc2TransitGatewayDetailsTypeDef = TypedDict(
    "AwsEc2TransitGatewayDetailsTypeDef",
    {
        "Id": str,
        "Description": str,
        "DefaultRouteTablePropagation": str,
        "AutoAcceptSharedAttachments": str,
        "DefaultRouteTableAssociation": str,
        "TransitGatewayCidrBlocks": Sequence[str],
        "AssociationDefaultRouteTableId": str,
        "PropagationDefaultRouteTableId": str,
        "VpnEcmpSupport": str,
        "DnsSupport": str,
        "MulticastSupport": str,
        "AmazonSideAsn": int,
    },
    total=False,
)

AwsEc2VolumeAttachmentOutputTypeDef = TypedDict(
    "AwsEc2VolumeAttachmentOutputTypeDef",
    {
        "AttachTime": str,
        "DeleteOnTermination": bool,
        "InstanceId": str,
        "Status": str,
    },
)

AwsEc2VolumeAttachmentTypeDef = TypedDict(
    "AwsEc2VolumeAttachmentTypeDef",
    {
        "AttachTime": str,
        "DeleteOnTermination": bool,
        "InstanceId": str,
        "Status": str,
    },
    total=False,
)

CidrBlockAssociationOutputTypeDef = TypedDict(
    "CidrBlockAssociationOutputTypeDef",
    {
        "AssociationId": str,
        "CidrBlock": str,
        "CidrBlockState": str,
    },
)

CidrBlockAssociationTypeDef = TypedDict(
    "CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "CidrBlock": str,
        "CidrBlockState": str,
    },
    total=False,
)

AwsEc2VpcEndpointServiceServiceTypeDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceServiceTypeDetailsOutputTypeDef",
    {
        "ServiceType": str,
    },
)

AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    {
        "ServiceType": str,
    },
    total=False,
)

AwsEc2VpcPeeringConnectionStatusDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionStatusDetailsOutputTypeDef",
    {
        "Code": str,
        "Message": str,
    },
)

AwsEc2VpcPeeringConnectionStatusDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionStatusDetailsTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

VpcInfoCidrBlockSetDetailsOutputTypeDef = TypedDict(
    "VpcInfoCidrBlockSetDetailsOutputTypeDef",
    {
        "CidrBlock": str,
    },
)

VpcInfoIpv6CidrBlockSetDetailsOutputTypeDef = TypedDict(
    "VpcInfoIpv6CidrBlockSetDetailsOutputTypeDef",
    {
        "Ipv6CidrBlock": str,
    },
)

VpcInfoPeeringOptionsDetailsOutputTypeDef = TypedDict(
    "VpcInfoPeeringOptionsDetailsOutputTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
)

VpcInfoCidrBlockSetDetailsTypeDef = TypedDict(
    "VpcInfoCidrBlockSetDetailsTypeDef",
    {
        "CidrBlock": str,
    },
    total=False,
)

VpcInfoIpv6CidrBlockSetDetailsTypeDef = TypedDict(
    "VpcInfoIpv6CidrBlockSetDetailsTypeDef",
    {
        "Ipv6CidrBlock": str,
    },
    total=False,
)

VpcInfoPeeringOptionsDetailsTypeDef = TypedDict(
    "VpcInfoPeeringOptionsDetailsTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

AwsEc2VpnConnectionRoutesDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionRoutesDetailsOutputTypeDef",
    {
        "DestinationCidrBlock": str,
        "State": str,
    },
)

AwsEc2VpnConnectionVgwTelemetryDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionVgwTelemetryDetailsOutputTypeDef",
    {
        "AcceptedRouteCount": int,
        "CertificateArn": str,
        "LastStatusChange": str,
        "OutsideIpAddress": str,
        "Status": str,
        "StatusMessage": str,
    },
)

AwsEc2VpnConnectionRoutesDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    {
        "DestinationCidrBlock": str,
        "State": str,
    },
    total=False,
)

AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    {
        "AcceptedRouteCount": int,
        "CertificateArn": str,
        "LastStatusChange": str,
        "OutsideIpAddress": str,
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)

AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef",
    {
        "DpdTimeoutSeconds": int,
        "IkeVersions": List[str],
        "OutsideIpAddress": str,
        "Phase1DhGroupNumbers": List[int],
        "Phase1EncryptionAlgorithms": List[str],
        "Phase1IntegrityAlgorithms": List[str],
        "Phase1LifetimeSeconds": int,
        "Phase2DhGroupNumbers": List[int],
        "Phase2EncryptionAlgorithms": List[str],
        "Phase2IntegrityAlgorithms": List[str],
        "Phase2LifetimeSeconds": int,
        "PreSharedKey": str,
        "RekeyFuzzPercentage": int,
        "RekeyMarginTimeSeconds": int,
        "ReplayWindowSize": int,
        "TunnelInsideCidr": str,
    },
)

AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    {
        "DpdTimeoutSeconds": int,
        "IkeVersions": Sequence[str],
        "OutsideIpAddress": str,
        "Phase1DhGroupNumbers": Sequence[int],
        "Phase1EncryptionAlgorithms": Sequence[str],
        "Phase1IntegrityAlgorithms": Sequence[str],
        "Phase1LifetimeSeconds": int,
        "Phase2DhGroupNumbers": Sequence[int],
        "Phase2EncryptionAlgorithms": Sequence[str],
        "Phase2IntegrityAlgorithms": Sequence[str],
        "Phase2LifetimeSeconds": int,
        "PreSharedKey": str,
        "RekeyFuzzPercentage": int,
        "RekeyMarginTimeSeconds": int,
        "ReplayWindowSize": int,
        "TunnelInsideCidr": str,
    },
    total=False,
)

AwsEcrContainerImageDetailsOutputTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsOutputTypeDef",
    {
        "RegistryId": str,
        "RepositoryName": str,
        "Architecture": str,
        "ImageDigest": str,
        "ImageTags": List[str],
        "ImagePublishedAt": str,
    },
)

AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "RegistryId": str,
        "RepositoryName": str,
        "Architecture": str,
        "ImageDigest": str,
        "ImageTags": Sequence[str],
        "ImagePublishedAt": str,
    },
    total=False,
)

AwsEcrRepositoryImageScanningConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcrRepositoryImageScanningConfigurationDetailsOutputTypeDef",
    {
        "ScanOnPush": bool,
    },
)

AwsEcrRepositoryLifecyclePolicyDetailsOutputTypeDef = TypedDict(
    "AwsEcrRepositoryLifecyclePolicyDetailsOutputTypeDef",
    {
        "LifecyclePolicyText": str,
        "RegistryId": str,
    },
)

AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    {
        "ScanOnPush": bool,
    },
    total=False,
)

AwsEcrRepositoryLifecyclePolicyDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    {
        "LifecyclePolicyText": str,
        "RegistryId": str,
    },
    total=False,
)

AwsEcsClusterClusterSettingsDetailsOutputTypeDef = TypedDict(
    "AwsEcsClusterClusterSettingsDetailsOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

AwsEcsClusterClusterSettingsDetailsTypeDef = TypedDict(
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsOutputTypeDef = (
    TypedDict(
        "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsOutputTypeDef",
        {
            "CloudWatchEncryptionEnabled": bool,
            "CloudWatchLogGroupName": str,
            "S3BucketName": str,
            "S3EncryptionEnabled": bool,
            "S3KeyPrefix": str,
        },
    )
)

AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    {
        "CloudWatchEncryptionEnabled": bool,
        "CloudWatchLogGroupName": str,
        "S3BucketName": str,
        "S3EncryptionEnabled": bool,
        "S3KeyPrefix": str,
    },
    total=False,
)

AwsEcsClusterDefaultCapacityProviderStrategyDetailsOutputTypeDef = TypedDict(
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsOutputTypeDef",
    {
        "Base": int,
        "CapacityProvider": str,
        "Weight": int,
    },
)

AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": int,
        "CapacityProvider": str,
        "Weight": int,
    },
    total=False,
)

AwsMountPointOutputTypeDef = TypedDict(
    "AwsMountPointOutputTypeDef",
    {
        "SourceVolume": str,
        "ContainerPath": str,
    },
)

AwsMountPointTypeDef = TypedDict(
    "AwsMountPointTypeDef",
    {
        "SourceVolume": str,
        "ContainerPath": str,
    },
    total=False,
)

AwsEcsServiceCapacityProviderStrategyDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceCapacityProviderStrategyDetailsOutputTypeDef",
    {
        "Base": int,
        "CapacityProvider": str,
        "Weight": int,
    },
)

AwsEcsServiceCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": int,
        "CapacityProvider": str,
        "Weight": int,
    },
    total=False,
)

AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsOutputTypeDef",
    {
        "Enable": bool,
        "Rollback": bool,
    },
)

AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    {
        "Enable": bool,
        "Rollback": bool,
    },
    total=False,
)

AwsEcsServiceDeploymentControllerDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceDeploymentControllerDetailsOutputTypeDef",
    {
        "Type": str,
    },
)

AwsEcsServiceDeploymentControllerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    {
        "Type": str,
    },
    total=False,
)

AwsEcsServiceLoadBalancersDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceLoadBalancersDetailsOutputTypeDef",
    {
        "ContainerName": str,
        "ContainerPort": int,
        "LoadBalancerName": str,
        "TargetGroupArn": str,
    },
)

AwsEcsServicePlacementConstraintsDetailsOutputTypeDef = TypedDict(
    "AwsEcsServicePlacementConstraintsDetailsOutputTypeDef",
    {
        "Expression": str,
        "Type": str,
    },
)

AwsEcsServicePlacementStrategiesDetailsOutputTypeDef = TypedDict(
    "AwsEcsServicePlacementStrategiesDetailsOutputTypeDef",
    {
        "Field": str,
        "Type": str,
    },
)

AwsEcsServiceServiceRegistriesDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceServiceRegistriesDetailsOutputTypeDef",
    {
        "ContainerName": str,
        "ContainerPort": int,
        "Port": int,
        "RegistryArn": str,
    },
)

AwsEcsServiceLoadBalancersDetailsTypeDef = TypedDict(
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    {
        "ContainerName": str,
        "ContainerPort": int,
        "LoadBalancerName": str,
        "TargetGroupArn": str,
    },
    total=False,
)

AwsEcsServicePlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    {
        "Expression": str,
        "Type": str,
    },
    total=False,
)

AwsEcsServicePlacementStrategiesDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    {
        "Field": str,
        "Type": str,
    },
    total=False,
)

AwsEcsServiceServiceRegistriesDetailsTypeDef = TypedDict(
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    {
        "ContainerName": str,
        "ContainerPort": int,
        "Port": int,
        "RegistryArn": str,
    },
    total=False,
)

AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef",
    {
        "AssignPublicIp": str,
        "SecurityGroups": List[str],
        "Subnets": List[str],
    },
)

AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    {
        "AssignPublicIp": str,
        "SecurityGroups": Sequence[str],
        "Subnets": Sequence[str],
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsOutputTypeDef",
    {
        "Condition": str,
        "ContainerName": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    {
        "Condition": str,
        "ContainerName": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsOutputTypeDef",
    {
        "Type": str,
        "Value": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsOutputTypeDef",
    {
        "Hostname": str,
        "IpAddress": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef",
    {
        "Options": Dict[str, str],
        "Type": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef",
    {
        "Command": List[str],
        "Interval": int,
        "Retries": int,
        "StartPeriod": int,
        "Timeout": int,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsOutputTypeDef",
    {
        "ContainerPath": str,
        "ReadOnly": bool,
        "SourceVolume": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsOutputTypeDef",
    {
        "ContainerPort": int,
        "HostPort": int,
        "Protocol": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsOutputTypeDef",
    {
        "CredentialsParameter": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsOutputTypeDef",
    {
        "Type": str,
        "Value": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsOutputTypeDef",
    {
        "Name": str,
        "ValueFrom": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsOutputTypeDef",
    {
        "Namespace": str,
        "Value": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsOutputTypeDef",
    {
        "HardLimit": int,
        "Name": str,
        "SoftLimit": int,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsOutputTypeDef",
    {
        "ReadOnly": bool,
        "SourceContainer": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    {
        "Type": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    {
        "Hostname": str,
        "IpAddress": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    {
        "Options": Mapping[str, str],
        "Type": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    {
        "Command": Sequence[str],
        "Interval": int,
        "Retries": int,
        "StartPeriod": int,
        "Timeout": int,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    {
        "ContainerPath": str,
        "ReadOnly": bool,
        "SourceVolume": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    {
        "ContainerPort": int,
        "HostPort": int,
        "Protocol": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    {
        "CredentialsParameter": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    {
        "Type": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    {
        "Name": str,
        "ValueFrom": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    {
        "Namespace": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    {
        "HardLimit": int,
        "Name": str,
        "SoftLimit": int,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    {
        "ReadOnly": bool,
        "SourceContainer": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef",
    {
        "Add": List[str],
        "Drop": List[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    {
        "Add": Sequence[str],
        "Drop": Sequence[str],
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef",
    {
        "ContainerPath": str,
        "HostPath": str,
        "Permissions": List[str],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef",
    {
        "ContainerPath": str,
        "MountOptions": List[str],
        "Size": int,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    {
        "ContainerPath": str,
        "HostPath": str,
        "Permissions": Sequence[str],
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    {
        "ContainerPath": str,
        "MountOptions": Sequence[str],
        "Size": int,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsOutputTypeDef = (
    TypedDict(
        "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsOutputTypeDef",
        {
            "Name": str,
            "ValueFrom": str,
        },
    )
)

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    {
        "Name": str,
        "ValueFrom": str,
    },
    total=False,
)

AwsEcsTaskDefinitionInferenceAcceleratorsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsOutputTypeDef",
    {
        "DeviceName": str,
        "DeviceType": str,
    },
)

AwsEcsTaskDefinitionPlacementConstraintsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsOutputTypeDef",
    {
        "Expression": str,
        "Type": str,
    },
)

AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    {
        "DeviceName": str,
        "DeviceType": str,
    },
    total=False,
)

AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    {
        "Expression": str,
        "Type": str,
    },
    total=False,
)

AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef",
    {
        "Autoprovision": bool,
        "Driver": str,
        "DriverOpts": Dict[str, str],
        "Labels": Dict[str, str],
        "Scope": str,
    },
)

AwsEcsTaskDefinitionVolumesHostDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesHostDetailsOutputTypeDef",
    {
        "SourcePath": str,
    },
)

AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    {
        "Autoprovision": bool,
        "Driver": str,
        "DriverOpts": Mapping[str, str],
        "Labels": Mapping[str, str],
        "Scope": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesHostDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    {
        "SourcePath": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsOutputTypeDef = (
    TypedDict(
        "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsOutputTypeDef",
        {
            "AccessPointId": str,
            "Iam": str,
        },
    )
)

AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    {
        "AccessPointId": str,
        "Iam": str,
    },
    total=False,
)

AwsEcsTaskVolumeHostDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskVolumeHostDetailsOutputTypeDef",
    {
        "SourcePath": str,
    },
)

AwsEcsTaskVolumeHostDetailsTypeDef = TypedDict(
    "AwsEcsTaskVolumeHostDetailsTypeDef",
    {
        "SourcePath": str,
    },
    total=False,
)

AwsEfsAccessPointPosixUserDetailsOutputTypeDef = TypedDict(
    "AwsEfsAccessPointPosixUserDetailsOutputTypeDef",
    {
        "Gid": str,
        "SecondaryGids": List[str],
        "Uid": str,
    },
)

AwsEfsAccessPointPosixUserDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointPosixUserDetailsTypeDef",
    {
        "Gid": str,
        "SecondaryGids": Sequence[str],
        "Uid": str,
    },
    total=False,
)

AwsEfsAccessPointRootDirectoryCreationInfoDetailsOutputTypeDef = TypedDict(
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsOutputTypeDef",
    {
        "OwnerGid": str,
        "OwnerUid": str,
        "Permissions": str,
    },
)

AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef",
    {
        "OwnerGid": str,
        "OwnerUid": str,
        "Permissions": str,
    },
    total=False,
)

AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef = TypedDict(
    "AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "EndpointPublicAccess": bool,
    },
)

AwsEksClusterResourcesVpcConfigDetailsTypeDef = TypedDict(
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "SubnetIds": Sequence[str],
        "EndpointPublicAccess": bool,
    },
    total=False,
)

AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef = TypedDict(
    "AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef",
    {
        "Enabled": bool,
        "Types": List[str],
    },
)

AwsEksClusterLoggingClusterLoggingDetailsTypeDef = TypedDict(
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    {
        "Enabled": bool,
        "Types": Sequence[str],
    },
    total=False,
)

AwsElasticBeanstalkEnvironmentEnvironmentLinkOutputTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkOutputTypeDef",
    {
        "EnvironmentName": str,
        "LinkName": str,
    },
)

AwsElasticBeanstalkEnvironmentOptionSettingOutputTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentOptionSettingOutputTypeDef",
    {
        "Namespace": str,
        "OptionName": str,
        "ResourceName": str,
        "Value": str,
    },
)

AwsElasticBeanstalkEnvironmentTierOutputTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentTierOutputTypeDef",
    {
        "Name": str,
        "Type": str,
        "Version": str,
    },
)

AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    {
        "EnvironmentName": str,
        "LinkName": str,
    },
    total=False,
)

AwsElasticBeanstalkEnvironmentOptionSettingTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    {
        "Namespace": str,
        "OptionName": str,
        "ResourceName": str,
        "Value": str,
    },
    total=False,
)

AwsElasticBeanstalkEnvironmentTierTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    {
        "Name": str,
        "Type": str,
        "Version": str,
    },
    total=False,
)

AwsElasticsearchDomainDomainEndpointOptionsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainDomainEndpointOptionsOutputTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": str,
    },
)

AwsElasticsearchDomainEncryptionAtRestOptionsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainEncryptionAtRestOptionsOutputTypeDef",
    {
        "Enabled": bool,
        "KmsKeyId": str,
    },
)

AwsElasticsearchDomainNodeToNodeEncryptionOptionsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsOutputTypeDef",
    {
        "Enabled": bool,
    },
)

AwsElasticsearchDomainServiceSoftwareOptionsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainServiceSoftwareOptionsOutputTypeDef",
    {
        "AutomatedUpdateDate": str,
        "Cancellable": bool,
        "CurrentVersion": str,
        "Description": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "UpdateStatus": str,
    },
)

AwsElasticsearchDomainVPCOptionsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VPCId": str,
    },
)

AwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": str,
    },
    total=False,
)

AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {
        "Enabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AwsElasticsearchDomainServiceSoftwareOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    {
        "AutomatedUpdateDate": str,
        "Cancellable": bool,
        "CurrentVersion": str,
        "Description": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "UpdateStatus": str,
    },
    total=False,
)

AwsElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "SecurityGroupIds": Sequence[str],
        "SubnetIds": Sequence[str],
        "VPCId": str,
    },
    total=False,
)

AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsOutputTypeDef",
    {
        "AvailabilityZoneCount": int,
    },
)

AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": int,
    },
    total=False,
)

AwsElasticsearchDomainLogPublishingOptionsLogConfigOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigOutputTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "Enabled": bool,
    },
)

AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "Enabled": bool,
    },
    total=False,
)

AwsElbAppCookieStickinessPolicyOutputTypeDef = TypedDict(
    "AwsElbAppCookieStickinessPolicyOutputTypeDef",
    {
        "CookieName": str,
        "PolicyName": str,
    },
)

AwsElbAppCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbAppCookieStickinessPolicyTypeDef",
    {
        "CookieName": str,
        "PolicyName": str,
    },
    total=False,
)

AwsElbLbCookieStickinessPolicyOutputTypeDef = TypedDict(
    "AwsElbLbCookieStickinessPolicyOutputTypeDef",
    {
        "CookieExpirationPeriod": int,
        "PolicyName": str,
    },
)

AwsElbLbCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbLbCookieStickinessPolicyTypeDef",
    {
        "CookieExpirationPeriod": int,
        "PolicyName": str,
    },
    total=False,
)

AwsElbLoadBalancerAccessLogOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerAccessLogOutputTypeDef",
    {
        "EmitInterval": int,
        "Enabled": bool,
        "S3BucketName": str,
        "S3BucketPrefix": str,
    },
)

AwsElbLoadBalancerAccessLogTypeDef = TypedDict(
    "AwsElbLoadBalancerAccessLogTypeDef",
    {
        "EmitInterval": int,
        "Enabled": bool,
        "S3BucketName": str,
        "S3BucketPrefix": str,
    },
    total=False,
)

AwsElbLoadBalancerAdditionalAttributeOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerAdditionalAttributeOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

AwsElbLoadBalancerAdditionalAttributeTypeDef = TypedDict(
    "AwsElbLoadBalancerAdditionalAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

AwsElbLoadBalancerConnectionDrainingOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionDrainingOutputTypeDef",
    {
        "Enabled": bool,
        "Timeout": int,
    },
)

AwsElbLoadBalancerConnectionSettingsOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionSettingsOutputTypeDef",
    {
        "IdleTimeout": int,
    },
)

AwsElbLoadBalancerCrossZoneLoadBalancingOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerCrossZoneLoadBalancingOutputTypeDef",
    {
        "Enabled": bool,
    },
)

AwsElbLoadBalancerConnectionDrainingTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    {
        "Enabled": bool,
        "Timeout": int,
    },
    total=False,
)

AwsElbLoadBalancerConnectionSettingsTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    {
        "IdleTimeout": int,
    },
    total=False,
)

AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef = TypedDict(
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef",
    {
        "InstancePort": int,
        "PolicyNames": List[str],
    },
)

AwsElbLoadBalancerBackendServerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    {
        "InstancePort": int,
        "PolicyNames": Sequence[str],
    },
    total=False,
)

AwsElbLoadBalancerHealthCheckOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerHealthCheckOutputTypeDef",
    {
        "HealthyThreshold": int,
        "Interval": int,
        "Target": str,
        "Timeout": int,
        "UnhealthyThreshold": int,
    },
)

AwsElbLoadBalancerInstanceOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerInstanceOutputTypeDef",
    {
        "InstanceId": str,
    },
)

AwsElbLoadBalancerSourceSecurityGroupOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerSourceSecurityGroupOutputTypeDef",
    {
        "GroupName": str,
        "OwnerAlias": str,
    },
)

AwsElbLoadBalancerHealthCheckTypeDef = TypedDict(
    "AwsElbLoadBalancerHealthCheckTypeDef",
    {
        "HealthyThreshold": int,
        "Interval": int,
        "Target": str,
        "Timeout": int,
        "UnhealthyThreshold": int,
    },
    total=False,
)

AwsElbLoadBalancerInstanceTypeDef = TypedDict(
    "AwsElbLoadBalancerInstanceTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

AwsElbLoadBalancerSourceSecurityGroupTypeDef = TypedDict(
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    {
        "GroupName": str,
        "OwnerAlias": str,
    },
    total=False,
)

AwsElbLoadBalancerListenerOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerOutputTypeDef",
    {
        "InstancePort": int,
        "InstanceProtocol": str,
        "LoadBalancerPort": int,
        "Protocol": str,
        "SslCertificateId": str,
    },
)

AwsElbLoadBalancerListenerTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerTypeDef",
    {
        "InstancePort": int,
        "InstanceProtocol": str,
        "LoadBalancerPort": int,
        "Protocol": str,
        "SslCertificateId": str,
    },
    total=False,
)

AwsElbv2LoadBalancerAttributeOutputTypeDef = TypedDict(
    "AwsElbv2LoadBalancerAttributeOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

AwsElbv2LoadBalancerAttributeTypeDef = TypedDict(
    "AwsElbv2LoadBalancerAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

LoadBalancerStateOutputTypeDef = TypedDict(
    "LoadBalancerStateOutputTypeDef",
    {
        "Code": str,
        "Reason": str,
    },
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": str,
        "Reason": str,
    },
    total=False,
)

AwsEventSchemasRegistryDetailsOutputTypeDef = TypedDict(
    "AwsEventSchemasRegistryDetailsOutputTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
    },
)

AwsEventSchemasRegistryDetailsTypeDef = TypedDict(
    "AwsEventSchemasRegistryDetailsTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesCloudTrailDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsOutputTypeDef",
    {
        "Status": str,
    },
)

AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef",
    {
        "Status": str,
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesDnsLogsDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsOutputTypeDef",
    {
        "Status": str,
    },
)

AwsGuardDutyDetectorDataSourcesFlowLogsDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsOutputTypeDef",
    {
        "Status": str,
    },
)

AwsGuardDutyDetectorDataSourcesS3LogsDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsOutputTypeDef",
    {
        "Status": str,
    },
)

AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef",
    {
        "Status": str,
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef",
    {
        "Status": str,
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef",
    {
        "Status": str,
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsOutputTypeDef",
    {
        "Status": str,
    },
)

AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef",
    {
        "Status": str,
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsOutputTypeDef",
    {
        "Reason": str,
        "Status": str,
    },
)

AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef",
    {
        "Reason": str,
        "Status": str,
    },
    total=False,
)

AwsGuardDutyDetectorFeaturesDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorFeaturesDetailsOutputTypeDef",
    {
        "Name": str,
        "Status": str,
    },
)

AwsGuardDutyDetectorFeaturesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorFeaturesDetailsTypeDef",
    {
        "Name": str,
        "Status": str,
    },
    total=False,
)

AwsIamAccessKeySessionContextAttributesOutputTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextAttributesOutputTypeDef",
    {
        "MfaAuthenticated": bool,
        "CreationDate": str,
    },
)

AwsIamAccessKeySessionContextAttributesTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    {
        "MfaAuthenticated": bool,
        "CreationDate": str,
    },
    total=False,
)

AwsIamAccessKeySessionContextSessionIssuerOutputTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerOutputTypeDef",
    {
        "Type": str,
        "PrincipalId": str,
        "Arn": str,
        "AccountId": str,
        "UserName": str,
    },
)

AwsIamAccessKeySessionContextSessionIssuerTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    {
        "Type": str,
        "PrincipalId": str,
        "Arn": str,
        "AccountId": str,
        "UserName": str,
    },
    total=False,
)

AwsIamAttachedManagedPolicyOutputTypeDef = TypedDict(
    "AwsIamAttachedManagedPolicyOutputTypeDef",
    {
        "PolicyName": str,
        "PolicyArn": str,
    },
)

AwsIamAttachedManagedPolicyTypeDef = TypedDict(
    "AwsIamAttachedManagedPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyArn": str,
    },
    total=False,
)

AwsIamGroupPolicyOutputTypeDef = TypedDict(
    "AwsIamGroupPolicyOutputTypeDef",
    {
        "PolicyName": str,
    },
)

AwsIamGroupPolicyTypeDef = TypedDict(
    "AwsIamGroupPolicyTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

AwsIamInstanceProfileRoleOutputTypeDef = TypedDict(
    "AwsIamInstanceProfileRoleOutputTypeDef",
    {
        "Arn": str,
        "AssumeRolePolicyDocument": str,
        "CreateDate": str,
        "Path": str,
        "RoleId": str,
        "RoleName": str,
    },
)

AwsIamInstanceProfileRoleTypeDef = TypedDict(
    "AwsIamInstanceProfileRoleTypeDef",
    {
        "Arn": str,
        "AssumeRolePolicyDocument": str,
        "CreateDate": str,
        "Path": str,
        "RoleId": str,
        "RoleName": str,
    },
    total=False,
)

AwsIamPermissionsBoundaryOutputTypeDef = TypedDict(
    "AwsIamPermissionsBoundaryOutputTypeDef",
    {
        "PermissionsBoundaryArn": str,
        "PermissionsBoundaryType": str,
    },
)

AwsIamPermissionsBoundaryTypeDef = TypedDict(
    "AwsIamPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryArn": str,
        "PermissionsBoundaryType": str,
    },
    total=False,
)

AwsIamPolicyVersionOutputTypeDef = TypedDict(
    "AwsIamPolicyVersionOutputTypeDef",
    {
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": str,
    },
)

AwsIamPolicyVersionTypeDef = TypedDict(
    "AwsIamPolicyVersionTypeDef",
    {
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": str,
    },
    total=False,
)

AwsIamRolePolicyOutputTypeDef = TypedDict(
    "AwsIamRolePolicyOutputTypeDef",
    {
        "PolicyName": str,
    },
)

AwsIamRolePolicyTypeDef = TypedDict(
    "AwsIamRolePolicyTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

AwsIamUserPolicyOutputTypeDef = TypedDict(
    "AwsIamUserPolicyOutputTypeDef",
    {
        "PolicyName": str,
    },
)

AwsIamUserPolicyTypeDef = TypedDict(
    "AwsIamUserPolicyTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

AwsKinesisStreamStreamEncryptionDetailsOutputTypeDef = TypedDict(
    "AwsKinesisStreamStreamEncryptionDetailsOutputTypeDef",
    {
        "EncryptionType": str,
        "KeyId": str,
    },
)

AwsKinesisStreamStreamEncryptionDetailsTypeDef = TypedDict(
    "AwsKinesisStreamStreamEncryptionDetailsTypeDef",
    {
        "EncryptionType": str,
        "KeyId": str,
    },
    total=False,
)

AwsKmsKeyDetailsOutputTypeDef = TypedDict(
    "AwsKmsKeyDetailsOutputTypeDef",
    {
        "AWSAccountId": str,
        "CreationDate": float,
        "KeyId": str,
        "KeyManager": str,
        "KeyState": str,
        "Origin": str,
        "Description": str,
        "KeyRotationStatus": bool,
    },
)

AwsKmsKeyDetailsTypeDef = TypedDict(
    "AwsKmsKeyDetailsTypeDef",
    {
        "AWSAccountId": str,
        "CreationDate": float,
        "KeyId": str,
        "KeyManager": str,
        "KeyState": str,
        "Origin": str,
        "Description": str,
        "KeyRotationStatus": bool,
    },
    total=False,
)

AwsLambdaFunctionCodeOutputTypeDef = TypedDict(
    "AwsLambdaFunctionCodeOutputTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ZipFile": str,
    },
)

AwsLambdaFunctionCodeTypeDef = TypedDict(
    "AwsLambdaFunctionCodeTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ZipFile": str,
    },
    total=False,
)

AwsLambdaFunctionDeadLetterConfigOutputTypeDef = TypedDict(
    "AwsLambdaFunctionDeadLetterConfigOutputTypeDef",
    {
        "TargetArn": str,
    },
)

AwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    {
        "TargetArn": str,
    },
    total=False,
)

AwsLambdaFunctionLayerOutputTypeDef = TypedDict(
    "AwsLambdaFunctionLayerOutputTypeDef",
    {
        "Arn": str,
        "CodeSize": int,
    },
)

AwsLambdaFunctionTracingConfigOutputTypeDef = TypedDict(
    "AwsLambdaFunctionTracingConfigOutputTypeDef",
    {
        "Mode": str,
    },
)

AwsLambdaFunctionVpcConfigOutputTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VpcId": str,
    },
)

AwsLambdaFunctionLayerTypeDef = TypedDict(
    "AwsLambdaFunctionLayerTypeDef",
    {
        "Arn": str,
        "CodeSize": int,
    },
    total=False,
)

AwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "AwsLambdaFunctionTracingConfigTypeDef",
    {
        "Mode": str,
    },
    total=False,
)

AwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "SubnetIds": Sequence[str],
        "VpcId": str,
    },
    total=False,
)

AwsLambdaFunctionEnvironmentErrorOutputTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentErrorOutputTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
)

AwsLambdaFunctionEnvironmentErrorTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

AwsLambdaLayerVersionDetailsOutputTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsOutputTypeDef",
    {
        "Version": int,
        "CompatibleRuntimes": List[str],
        "CreatedDate": str,
    },
)

AwsLambdaLayerVersionDetailsTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsTypeDef",
    {
        "Version": int,
        "CompatibleRuntimes": Sequence[str],
        "CreatedDate": str,
    },
    total=False,
)

AwsNetworkFirewallFirewallSubnetMappingsDetailsOutputTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsOutputTypeDef",
    {
        "SubnetId": str,
    },
)

AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    {
        "SubnetId": str,
    },
    total=False,
)

AwsOpenSearchServiceDomainMasterUserOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsOutputTypeDef",
    {
        "MasterUserArn": str,
        "MasterUserName": str,
        "MasterUserPassword": str,
    },
)

AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef",
    {
        "MasterUserArn": str,
        "MasterUserName": str,
        "MasterUserPassword": str,
    },
    total=False,
)

AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsOutputTypeDef",
    {
        "AvailabilityZoneCount": int,
    },
)

AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": int,
    },
    total=False,
)

AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsOutputTypeDef",
    {
        "CustomEndpointCertificateArn": str,
        "CustomEndpointEnabled": bool,
        "EnforceHTTPS": bool,
        "CustomEndpoint": str,
        "TLSSecurityPolicy": str,
    },
)

AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsOutputTypeDef",
    {
        "Enabled": bool,
        "KmsKeyId": str,
    },
)

AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsOutputTypeDef",
    {
        "Enabled": bool,
    },
)

AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsOutputTypeDef",
    {
        "AutomatedUpdateDate": str,
        "Cancellable": bool,
        "CurrentVersion": str,
        "Description": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "UpdateStatus": str,
        "OptionalDeployment": bool,
    },
)

AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
    },
)

AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    {
        "CustomEndpointCertificateArn": str,
        "CustomEndpointEnabled": bool,
        "EnforceHTTPS": bool,
        "CustomEndpoint": str,
        "TLSSecurityPolicy": str,
    },
    total=False,
)

AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    {
        "Enabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    {
        "AutomatedUpdateDate": str,
        "Cancellable": bool,
        "CurrentVersion": str,
        "Description": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "UpdateStatus": str,
        "OptionalDeployment": bool,
    },
    total=False,
)

AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "SubnetIds": Sequence[str],
    },
    total=False,
)

AwsOpenSearchServiceDomainLogPublishingOptionOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionOutputTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "Enabled": bool,
    },
)

AwsOpenSearchServiceDomainLogPublishingOptionTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "Enabled": bool,
    },
    total=False,
)

AwsRdsDbClusterAssociatedRoleOutputTypeDef = TypedDict(
    "AwsRdsDbClusterAssociatedRoleOutputTypeDef",
    {
        "RoleArn": str,
        "Status": str,
    },
)

AwsRdsDbClusterAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    {
        "RoleArn": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbClusterMemberOutputTypeDef = TypedDict(
    "AwsRdsDbClusterMemberOutputTypeDef",
    {
        "IsClusterWriter": bool,
        "PromotionTier": int,
        "DbInstanceIdentifier": str,
        "DbClusterParameterGroupStatus": str,
    },
)

AwsRdsDbClusterOptionGroupMembershipOutputTypeDef = TypedDict(
    "AwsRdsDbClusterOptionGroupMembershipOutputTypeDef",
    {
        "DbClusterOptionGroupName": str,
        "Status": str,
    },
)

AwsRdsDbDomainMembershipOutputTypeDef = TypedDict(
    "AwsRdsDbDomainMembershipOutputTypeDef",
    {
        "Domain": str,
        "Status": str,
        "Fqdn": str,
        "IamRoleName": str,
    },
)

AwsRdsDbInstanceVpcSecurityGroupOutputTypeDef = TypedDict(
    "AwsRdsDbInstanceVpcSecurityGroupOutputTypeDef",
    {
        "VpcSecurityGroupId": str,
        "Status": str,
    },
)

AwsRdsDbClusterMemberTypeDef = TypedDict(
    "AwsRdsDbClusterMemberTypeDef",
    {
        "IsClusterWriter": bool,
        "PromotionTier": int,
        "DbInstanceIdentifier": str,
        "DbClusterParameterGroupStatus": str,
    },
    total=False,
)

AwsRdsDbClusterOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    {
        "DbClusterOptionGroupName": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbDomainMembershipTypeDef = TypedDict(
    "AwsRdsDbDomainMembershipTypeDef",
    {
        "Domain": str,
        "Status": str,
        "Fqdn": str,
        "IamRoleName": str,
    },
    total=False,
)

AwsRdsDbInstanceVpcSecurityGroupTypeDef = TypedDict(
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    {
        "VpcSecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List[str],
    },
)

AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": Sequence[str],
    },
    total=False,
)

AwsRdsDbInstanceAssociatedRoleOutputTypeDef = TypedDict(
    "AwsRdsDbInstanceAssociatedRoleOutputTypeDef",
    {
        "RoleArn": str,
        "FeatureName": str,
        "Status": str,
    },
)

AwsRdsDbInstanceAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    {
        "RoleArn": str,
        "FeatureName": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbInstanceEndpointOutputTypeDef = TypedDict(
    "AwsRdsDbInstanceEndpointOutputTypeDef",
    {
        "Address": str,
        "Port": int,
        "HostedZoneId": str,
    },
)

AwsRdsDbOptionGroupMembershipOutputTypeDef = TypedDict(
    "AwsRdsDbOptionGroupMembershipOutputTypeDef",
    {
        "OptionGroupName": str,
        "Status": str,
    },
)

AwsRdsDbParameterGroupOutputTypeDef = TypedDict(
    "AwsRdsDbParameterGroupOutputTypeDef",
    {
        "DbParameterGroupName": str,
        "ParameterApplyStatus": str,
    },
)

AwsRdsDbProcessorFeatureOutputTypeDef = TypedDict(
    "AwsRdsDbProcessorFeatureOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

AwsRdsDbStatusInfoOutputTypeDef = TypedDict(
    "AwsRdsDbStatusInfoOutputTypeDef",
    {
        "StatusType": str,
        "Normal": bool,
        "Status": str,
        "Message": str,
    },
)

AwsRdsDbInstanceEndpointTypeDef = TypedDict(
    "AwsRdsDbInstanceEndpointTypeDef",
    {
        "Address": str,
        "Port": int,
        "HostedZoneId": str,
    },
    total=False,
)

AwsRdsDbOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbOptionGroupMembershipTypeDef",
    {
        "OptionGroupName": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbParameterGroupTypeDef = TypedDict(
    "AwsRdsDbParameterGroupTypeDef",
    {
        "DbParameterGroupName": str,
        "ParameterApplyStatus": str,
    },
    total=False,
)

AwsRdsDbProcessorFeatureTypeDef = TypedDict(
    "AwsRdsDbProcessorFeatureTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsRdsDbStatusInfoTypeDef = TypedDict(
    "AwsRdsDbStatusInfoTypeDef",
    {
        "StatusType": str,
        "Normal": bool,
        "Status": str,
        "Message": str,
    },
    total=False,
)

AwsRdsPendingCloudWatchLogsExportsOutputTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsOutputTypeDef",
    {
        "LogTypesToEnable": List[str],
        "LogTypesToDisable": List[str],
    },
)

AwsRdsPendingCloudWatchLogsExportsTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": Sequence[str],
        "LogTypesToDisable": Sequence[str],
    },
    total=False,
)

AwsRdsDbSecurityGroupEc2SecurityGroupOutputTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupEc2SecurityGroupOutputTypeDef",
    {
        "Ec2SecurityGroupId": str,
        "Ec2SecurityGroupName": str,
        "Ec2SecurityGroupOwnerId": str,
        "Status": str,
    },
)

AwsRdsDbSecurityGroupIpRangeOutputTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupIpRangeOutputTypeDef",
    {
        "CidrIp": str,
        "Status": str,
    },
)

AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef",
    {
        "Ec2SecurityGroupId": str,
        "Ec2SecurityGroupName": str,
        "Ec2SecurityGroupOwnerId": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbSecurityGroupIpRangeTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupIpRangeTypeDef",
    {
        "CidrIp": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbSubnetGroupSubnetAvailabilityZoneOutputTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneOutputTypeDef",
    {
        "Name": str,
    },
)

AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

AwsRdsEventSubscriptionDetailsOutputTypeDef = TypedDict(
    "AwsRdsEventSubscriptionDetailsOutputTypeDef",
    {
        "CustSubscriptionId": str,
        "CustomerAwsId": str,
        "Enabled": bool,
        "EventCategoriesList": List[str],
        "EventSubscriptionArn": str,
        "SnsTopicArn": str,
        "SourceIdsList": List[str],
        "SourceType": str,
        "Status": str,
        "SubscriptionCreationTime": str,
    },
)

AwsRdsEventSubscriptionDetailsTypeDef = TypedDict(
    "AwsRdsEventSubscriptionDetailsTypeDef",
    {
        "CustSubscriptionId": str,
        "CustomerAwsId": str,
        "Enabled": bool,
        "EventCategoriesList": Sequence[str],
        "EventSubscriptionArn": str,
        "SnsTopicArn": str,
        "SourceIdsList": Sequence[str],
        "SourceType": str,
        "Status": str,
        "SubscriptionCreationTime": str,
    },
    total=False,
)

AwsRedshiftClusterClusterNodeOutputTypeDef = TypedDict(
    "AwsRedshiftClusterClusterNodeOutputTypeDef",
    {
        "NodeRole": str,
        "PrivateIpAddress": str,
        "PublicIpAddress": str,
    },
)

AwsRedshiftClusterClusterNodeTypeDef = TypedDict(
    "AwsRedshiftClusterClusterNodeTypeDef",
    {
        "NodeRole": str,
        "PrivateIpAddress": str,
        "PublicIpAddress": str,
    },
    total=False,
)

AwsRedshiftClusterClusterParameterStatusOutputTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterStatusOutputTypeDef",
    {
        "ParameterName": str,
        "ParameterApplyStatus": str,
        "ParameterApplyErrorDescription": str,
    },
)

AwsRedshiftClusterClusterParameterStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    {
        "ParameterName": str,
        "ParameterApplyStatus": str,
        "ParameterApplyErrorDescription": str,
    },
    total=False,
)

AwsRedshiftClusterClusterSecurityGroupOutputTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSecurityGroupOutputTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Status": str,
    },
)

AwsRedshiftClusterClusterSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Status": str,
    },
    total=False,
)

AwsRedshiftClusterClusterSnapshotCopyStatusOutputTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSnapshotCopyStatusOutputTypeDef",
    {
        "DestinationRegion": str,
        "ManualSnapshotRetentionPeriod": int,
        "RetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
)

AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "ManualSnapshotRetentionPeriod": int,
        "RetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

AwsRedshiftClusterDeferredMaintenanceWindowOutputTypeDef = TypedDict(
    "AwsRedshiftClusterDeferredMaintenanceWindowOutputTypeDef",
    {
        "DeferMaintenanceEndTime": str,
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": str,
    },
)

AwsRedshiftClusterDeferredMaintenanceWindowTypeDef = TypedDict(
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceEndTime": str,
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": str,
    },
    total=False,
)

AwsRedshiftClusterElasticIpStatusOutputTypeDef = TypedDict(
    "AwsRedshiftClusterElasticIpStatusOutputTypeDef",
    {
        "ElasticIp": str,
        "Status": str,
    },
)

AwsRedshiftClusterEndpointOutputTypeDef = TypedDict(
    "AwsRedshiftClusterEndpointOutputTypeDef",
    {
        "Address": str,
        "Port": int,
    },
)

AwsRedshiftClusterHsmStatusOutputTypeDef = TypedDict(
    "AwsRedshiftClusterHsmStatusOutputTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "Status": str,
    },
)

AwsRedshiftClusterIamRoleOutputTypeDef = TypedDict(
    "AwsRedshiftClusterIamRoleOutputTypeDef",
    {
        "ApplyStatus": str,
        "IamRoleArn": str,
    },
)

AwsRedshiftClusterLoggingStatusOutputTypeDef = TypedDict(
    "AwsRedshiftClusterLoggingStatusOutputTypeDef",
    {
        "BucketName": str,
        "LastFailureMessage": str,
        "LastFailureTime": str,
        "LastSuccessfulDeliveryTime": str,
        "LoggingEnabled": bool,
        "S3KeyPrefix": str,
    },
)

AwsRedshiftClusterPendingModifiedValuesOutputTypeDef = TypedDict(
    "AwsRedshiftClusterPendingModifiedValuesOutputTypeDef",
    {
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "ClusterType": str,
        "ClusterVersion": str,
        "EncryptionType": str,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
    },
)

AwsRedshiftClusterResizeInfoOutputTypeDef = TypedDict(
    "AwsRedshiftClusterResizeInfoOutputTypeDef",
    {
        "AllowCancelResize": bool,
        "ResizeType": str,
    },
)

AwsRedshiftClusterRestoreStatusOutputTypeDef = TypedDict(
    "AwsRedshiftClusterRestoreStatusOutputTypeDef",
    {
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ProgressInMegaBytes": int,
        "SnapshotSizeInMegaBytes": int,
        "Status": str,
    },
)

AwsRedshiftClusterVpcSecurityGroupOutputTypeDef = TypedDict(
    "AwsRedshiftClusterVpcSecurityGroupOutputTypeDef",
    {
        "Status": str,
        "VpcSecurityGroupId": str,
    },
)

AwsRedshiftClusterElasticIpStatusTypeDef = TypedDict(
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    {
        "ElasticIp": str,
        "Status": str,
    },
    total=False,
)

AwsRedshiftClusterEndpointTypeDef = TypedDict(
    "AwsRedshiftClusterEndpointTypeDef",
    {
        "Address": str,
        "Port": int,
    },
    total=False,
)

AwsRedshiftClusterHsmStatusTypeDef = TypedDict(
    "AwsRedshiftClusterHsmStatusTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "Status": str,
    },
    total=False,
)

AwsRedshiftClusterIamRoleTypeDef = TypedDict(
    "AwsRedshiftClusterIamRoleTypeDef",
    {
        "ApplyStatus": str,
        "IamRoleArn": str,
    },
    total=False,
)

AwsRedshiftClusterLoggingStatusTypeDef = TypedDict(
    "AwsRedshiftClusterLoggingStatusTypeDef",
    {
        "BucketName": str,
        "LastFailureMessage": str,
        "LastFailureTime": str,
        "LastSuccessfulDeliveryTime": str,
        "LoggingEnabled": bool,
        "S3KeyPrefix": str,
    },
    total=False,
)

AwsRedshiftClusterPendingModifiedValuesTypeDef = TypedDict(
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    {
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "ClusterType": str,
        "ClusterVersion": str,
        "EncryptionType": str,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
    },
    total=False,
)

AwsRedshiftClusterResizeInfoTypeDef = TypedDict(
    "AwsRedshiftClusterResizeInfoTypeDef",
    {
        "AllowCancelResize": bool,
        "ResizeType": str,
    },
    total=False,
)

AwsRedshiftClusterRestoreStatusTypeDef = TypedDict(
    "AwsRedshiftClusterRestoreStatusTypeDef",
    {
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ProgressInMegaBytes": int,
        "SnapshotSizeInMegaBytes": int,
        "Status": str,
    },
    total=False,
)

AwsRedshiftClusterVpcSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    {
        "Status": str,
        "VpcSecurityGroupId": str,
    },
    total=False,
)

AwsS3AccountPublicAccessBlockDetailsOutputTypeDef = TypedDict(
    "AwsS3AccountPublicAccessBlockDetailsOutputTypeDef",
    {
        "BlockPublicAcls": bool,
        "BlockPublicPolicy": bool,
        "IgnorePublicAcls": bool,
        "RestrictPublicBuckets": bool,
    },
)

AwsS3AccountPublicAccessBlockDetailsTypeDef = TypedDict(
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    {
        "BlockPublicAcls": bool,
        "BlockPublicPolicy": bool,
        "IgnorePublicAcls": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsOutputTypeDef",
    {
        "DaysAfterInitiation": int,
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef = (
    TypedDict(
        "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
        {
            "DaysAfterInitiation": int,
        },
        total=False,
    )
)

AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsOutputTypeDef",
    {
        "Days": int,
        "StorageClass": str,
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsOutputTypeDef",
    {
        "Date": str,
        "Days": int,
        "StorageClass": str,
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    {
        "Days": int,
        "StorageClass": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    {
        "Date": str,
        "Days": int,
        "StorageClass": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

AwsS3BucketBucketVersioningConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketBucketVersioningConfigurationOutputTypeDef",
    {
        "IsMfaDeleteEnabled": bool,
        "Status": str,
    },
)

AwsS3BucketBucketVersioningConfigurationTypeDef = TypedDict(
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    {
        "IsMfaDeleteEnabled": bool,
        "Status": str,
    },
    total=False,
)

AwsS3BucketLoggingConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketLoggingConfigurationOutputTypeDef",
    {
        "DestinationBucketName": str,
        "LogFilePrefix": str,
    },
)

AwsS3BucketLoggingConfigurationTypeDef = TypedDict(
    "AwsS3BucketLoggingConfigurationTypeDef",
    {
        "DestinationBucketName": str,
        "LogFilePrefix": str,
    },
    total=False,
)

AwsS3BucketNotificationConfigurationS3KeyFilterRuleOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleOutputTypeDef",
    {
        "Name": AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType,
        "Value": str,
    },
)

AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    {
        "Name": AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType,
        "Value": str,
    },
    total=False,
)

AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsOutputTypeDef",
    {
        "Days": int,
        "Mode": str,
        "Years": int,
    },
)

AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef",
    {
        "Days": int,
        "Mode": str,
        "Years": int,
    },
    total=False,
)

AwsS3BucketServerSideEncryptionByDefaultOutputTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionByDefaultOutputTypeDef",
    {
        "SSEAlgorithm": str,
        "KMSMasterKeyID": str,
    },
)

AwsS3BucketServerSideEncryptionByDefaultTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    {
        "SSEAlgorithm": str,
        "KMSMasterKeyID": str,
    },
    total=False,
)

AwsS3BucketWebsiteConfigurationRedirectToOutputTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRedirectToOutputTypeDef",
    {
        "Hostname": str,
        "Protocol": str,
    },
)

AwsS3BucketWebsiteConfigurationRedirectToTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    {
        "Hostname": str,
        "Protocol": str,
    },
    total=False,
)

AwsS3BucketWebsiteConfigurationRoutingRuleConditionOutputTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionOutputTypeDef",
    {
        "HttpErrorCodeReturnedEquals": str,
        "KeyPrefixEquals": str,
    },
)

AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    {
        "HttpErrorCodeReturnedEquals": str,
        "KeyPrefixEquals": str,
    },
    total=False,
)

AwsS3BucketWebsiteConfigurationRoutingRuleRedirectOutputTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectOutputTypeDef",
    {
        "Hostname": str,
        "HttpRedirectCode": str,
        "Protocol": str,
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
)

AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    {
        "Hostname": str,
        "HttpRedirectCode": str,
        "Protocol": str,
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

AwsS3ObjectDetailsOutputTypeDef = TypedDict(
    "AwsS3ObjectDetailsOutputTypeDef",
    {
        "LastModified": str,
        "ETag": str,
        "VersionId": str,
        "ContentType": str,
        "ServerSideEncryption": str,
        "SSEKMSKeyId": str,
    },
)

AwsS3ObjectDetailsTypeDef = TypedDict(
    "AwsS3ObjectDetailsTypeDef",
    {
        "LastModified": str,
        "ETag": str,
        "VersionId": str,
        "ContentType": str,
        "ServerSideEncryption": str,
        "SSEKMSKeyId": str,
    },
    total=False,
)

AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsOutputTypeDef",
    {
        "MinimumInstanceMetadataServiceVersion": str,
    },
)

AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef",
    {
        "MinimumInstanceMetadataServiceVersion": str,
    },
    total=False,
)

AwsSecretsManagerSecretRotationRulesOutputTypeDef = TypedDict(
    "AwsSecretsManagerSecretRotationRulesOutputTypeDef",
    {
        "AutomaticallyAfterDays": int,
    },
)

AwsSecretsManagerSecretRotationRulesTypeDef = TypedDict(
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    {
        "AutomaticallyAfterDays": int,
    },
    total=False,
)

BooleanFilterOutputTypeDef = TypedDict(
    "BooleanFilterOutputTypeDef",
    {
        "Value": bool,
    },
)

IpFilterOutputTypeDef = TypedDict(
    "IpFilterOutputTypeDef",
    {
        "Cidr": str,
    },
)

KeywordFilterOutputTypeDef = TypedDict(
    "KeywordFilterOutputTypeDef",
    {
        "Value": str,
    },
)

BooleanFilterTypeDef = TypedDict(
    "BooleanFilterTypeDef",
    {
        "Value": bool,
    },
    total=False,
)

IpFilterTypeDef = TypedDict(
    "IpFilterTypeDef",
    {
        "Cidr": str,
    },
    total=False,
)

KeywordFilterTypeDef = TypedDict(
    "KeywordFilterTypeDef",
    {
        "Value": str,
    },
    total=False,
)

AwsSecurityFindingIdentifierOutputTypeDef = TypedDict(
    "AwsSecurityFindingIdentifierOutputTypeDef",
    {
        "Id": str,
        "ProductArn": str,
    },
)

AwsSecurityFindingIdentifierTypeDef = TypedDict(
    "AwsSecurityFindingIdentifierTypeDef",
    {
        "Id": str,
        "ProductArn": str,
    },
)

MalwareOutputTypeDef = TypedDict(
    "MalwareOutputTypeDef",
    {
        "Name": str,
        "Type": MalwareTypeType,
        "Path": str,
        "State": MalwareStateType,
    },
)

NoteOutputTypeDef = TypedDict(
    "NoteOutputTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
        "UpdatedAt": str,
    },
)

PatchSummaryOutputTypeDef = TypedDict(
    "PatchSummaryOutputTypeDef",
    {
        "Id": str,
        "InstalledCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "InstalledOtherCount": int,
        "InstalledRejectedCount": int,
        "InstalledPendingReboot": int,
        "OperationStartTime": str,
        "OperationEndTime": str,
        "RebootOption": str,
        "Operation": str,
    },
)

ProcessDetailsOutputTypeDef = TypedDict(
    "ProcessDetailsOutputTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
)

SeverityOutputTypeDef = TypedDict(
    "SeverityOutputTypeDef",
    {
        "Product": float,
        "Label": SeverityLabelType,
        "Normalized": int,
        "Original": str,
    },
)

ThreatIntelIndicatorOutputTypeDef = TypedDict(
    "ThreatIntelIndicatorOutputTypeDef",
    {
        "Type": ThreatIntelIndicatorTypeType,
        "Value": str,
        "Category": ThreatIntelIndicatorCategoryType,
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
)

WorkflowOutputTypeDef = TypedDict(
    "WorkflowOutputTypeDef",
    {
        "Status": WorkflowStatusType,
    },
)

_RequiredMalwareTypeDef = TypedDict(
    "_RequiredMalwareTypeDef",
    {
        "Name": str,
    },
)
_OptionalMalwareTypeDef = TypedDict(
    "_OptionalMalwareTypeDef",
    {
        "Type": MalwareTypeType,
        "Path": str,
        "State": MalwareStateType,
    },
    total=False,
)


class MalwareTypeDef(_RequiredMalwareTypeDef, _OptionalMalwareTypeDef):
    pass


NoteTypeDef = TypedDict(
    "NoteTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
        "UpdatedAt": str,
    },
)

_RequiredPatchSummaryTypeDef = TypedDict(
    "_RequiredPatchSummaryTypeDef",
    {
        "Id": str,
    },
)
_OptionalPatchSummaryTypeDef = TypedDict(
    "_OptionalPatchSummaryTypeDef",
    {
        "InstalledCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "InstalledOtherCount": int,
        "InstalledRejectedCount": int,
        "InstalledPendingReboot": int,
        "OperationStartTime": str,
        "OperationEndTime": str,
        "RebootOption": str,
        "Operation": str,
    },
    total=False,
)


class PatchSummaryTypeDef(_RequiredPatchSummaryTypeDef, _OptionalPatchSummaryTypeDef):
    pass


ProcessDetailsTypeDef = TypedDict(
    "ProcessDetailsTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "Product": float,
        "Label": SeverityLabelType,
        "Normalized": int,
        "Original": str,
    },
    total=False,
)

ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": ThreatIntelIndicatorTypeType,
        "Value": str,
        "Category": ThreatIntelIndicatorCategoryType,
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Status": WorkflowStatusType,
    },
    total=False,
)

AwsSnsTopicSubscriptionOutputTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionOutputTypeDef",
    {
        "Endpoint": str,
        "Protocol": str,
    },
)

AwsSnsTopicSubscriptionTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionTypeDef",
    {
        "Endpoint": str,
        "Protocol": str,
    },
    total=False,
)

AwsSqsQueueDetailsOutputTypeDef = TypedDict(
    "AwsSqsQueueDetailsOutputTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": int,
        "KmsMasterKeyId": str,
        "QueueName": str,
        "DeadLetterTargetArn": str,
    },
)

AwsSqsQueueDetailsTypeDef = TypedDict(
    "AwsSqsQueueDetailsTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": int,
        "KmsMasterKeyId": str,
        "QueueName": str,
        "DeadLetterTargetArn": str,
    },
    total=False,
)

AwsSsmComplianceSummaryOutputTypeDef = TypedDict(
    "AwsSsmComplianceSummaryOutputTypeDef",
    {
        "Status": str,
        "CompliantCriticalCount": int,
        "CompliantHighCount": int,
        "CompliantMediumCount": int,
        "ExecutionType": str,
        "NonCompliantCriticalCount": int,
        "CompliantInformationalCount": int,
        "NonCompliantInformationalCount": int,
        "CompliantUnspecifiedCount": int,
        "NonCompliantLowCount": int,
        "NonCompliantHighCount": int,
        "CompliantLowCount": int,
        "ComplianceType": str,
        "PatchBaselineId": str,
        "OverallSeverity": str,
        "NonCompliantMediumCount": int,
        "NonCompliantUnspecifiedCount": int,
        "PatchGroup": str,
    },
)

AwsSsmComplianceSummaryTypeDef = TypedDict(
    "AwsSsmComplianceSummaryTypeDef",
    {
        "Status": str,
        "CompliantCriticalCount": int,
        "CompliantHighCount": int,
        "CompliantMediumCount": int,
        "ExecutionType": str,
        "NonCompliantCriticalCount": int,
        "CompliantInformationalCount": int,
        "NonCompliantInformationalCount": int,
        "CompliantUnspecifiedCount": int,
        "NonCompliantLowCount": int,
        "NonCompliantHighCount": int,
        "CompliantLowCount": int,
        "ComplianceType": str,
        "PatchBaselineId": str,
        "OverallSeverity": str,
        "NonCompliantMediumCount": int,
        "NonCompliantUnspecifiedCount": int,
        "PatchGroup": str,
    },
    total=False,
)

AwsStepFunctionStateMachineTracingConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsStepFunctionStateMachineTracingConfigurationDetailsOutputTypeDef",
    {
        "Enabled": bool,
    },
)

AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsOutputTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsOutputTypeDef",
    {
        "LogGroupArn": str,
    },
)

AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef",
    {
        "LogGroupArn": str,
    },
    total=False,
)

AwsWafRateBasedRuleMatchPredicateOutputTypeDef = TypedDict(
    "AwsWafRateBasedRuleMatchPredicateOutputTypeDef",
    {
        "DataId": str,
        "Negated": bool,
        "Type": str,
    },
)

AwsWafRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": str,
        "Negated": bool,
        "Type": str,
    },
    total=False,
)

AwsWafRegionalRateBasedRuleMatchPredicateOutputTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleMatchPredicateOutputTypeDef",
    {
        "DataId": str,
        "Negated": bool,
        "Type": str,
    },
)

AwsWafRegionalRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": str,
        "Negated": bool,
        "Type": str,
    },
    total=False,
)

AwsWafRegionalRulePredicateListDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRulePredicateListDetailsOutputTypeDef",
    {
        "DataId": str,
        "Negated": bool,
        "Type": str,
    },
)

AwsWafRegionalRulePredicateListDetailsTypeDef = TypedDict(
    "AwsWafRegionalRulePredicateListDetailsTypeDef",
    {
        "DataId": str,
        "Negated": bool,
        "Type": str,
    },
    total=False,
)

AwsWafRegionalRuleGroupRulesActionDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesActionDetailsOutputTypeDef",
    {
        "Type": str,
    },
)

AwsWafRegionalRuleGroupRulesActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesActionDetailsTypeDef",
    {
        "Type": str,
    },
    total=False,
)

AwsWafRegionalWebAclRulesListActionDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListActionDetailsOutputTypeDef",
    {
        "Type": str,
    },
)

AwsWafRegionalWebAclRulesListActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListActionDetailsTypeDef",
    {
        "Type": str,
    },
    total=False,
)

AwsWafRegionalWebAclRulesListOverrideActionDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsOutputTypeDef",
    {
        "Type": str,
    },
)

AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef",
    {
        "Type": str,
    },
    total=False,
)

AwsWafRulePredicateListDetailsOutputTypeDef = TypedDict(
    "AwsWafRulePredicateListDetailsOutputTypeDef",
    {
        "DataId": str,
        "Negated": bool,
        "Type": str,
    },
)

AwsWafRulePredicateListDetailsTypeDef = TypedDict(
    "AwsWafRulePredicateListDetailsTypeDef",
    {
        "DataId": str,
        "Negated": bool,
        "Type": str,
    },
    total=False,
)

AwsWafRuleGroupRulesActionDetailsOutputTypeDef = TypedDict(
    "AwsWafRuleGroupRulesActionDetailsOutputTypeDef",
    {
        "Type": str,
    },
)

AwsWafRuleGroupRulesActionDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupRulesActionDetailsTypeDef",
    {
        "Type": str,
    },
    total=False,
)

WafActionOutputTypeDef = TypedDict(
    "WafActionOutputTypeDef",
    {
        "Type": str,
    },
)

WafExcludedRuleOutputTypeDef = TypedDict(
    "WafExcludedRuleOutputTypeDef",
    {
        "RuleId": str,
    },
)

WafOverrideActionOutputTypeDef = TypedDict(
    "WafOverrideActionOutputTypeDef",
    {
        "Type": str,
    },
)

WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": str,
    },
    total=False,
)

WafExcludedRuleTypeDef = TypedDict(
    "WafExcludedRuleTypeDef",
    {
        "RuleId": str,
    },
    total=False,
)

WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": str,
    },
    total=False,
)

AwsWafv2CustomHttpHeaderOutputTypeDef = TypedDict(
    "AwsWafv2CustomHttpHeaderOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

AwsWafv2CustomHttpHeaderTypeDef = TypedDict(
    "AwsWafv2CustomHttpHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsWafv2VisibilityConfigDetailsOutputTypeDef = TypedDict(
    "AwsWafv2VisibilityConfigDetailsOutputTypeDef",
    {
        "CloudWatchMetricsEnabled": bool,
        "MetricName": str,
        "SampledRequestsEnabled": bool,
    },
)

AwsWafv2VisibilityConfigDetailsTypeDef = TypedDict(
    "AwsWafv2VisibilityConfigDetailsTypeDef",
    {
        "CloudWatchMetricsEnabled": bool,
        "MetricName": str,
        "SampledRequestsEnabled": bool,
    },
    total=False,
)

AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsOutputTypeDef = TypedDict(
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsOutputTypeDef",
    {
        "ImmunityTime": int,
    },
)

AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef",
    {
        "ImmunityTime": int,
    },
    total=False,
)

AwsXrayEncryptionConfigDetailsOutputTypeDef = TypedDict(
    "AwsXrayEncryptionConfigDetailsOutputTypeDef",
    {
        "KeyId": str,
        "Status": str,
        "Type": str,
    },
)

AwsXrayEncryptionConfigDetailsTypeDef = TypedDict(
    "AwsXrayEncryptionConfigDetailsTypeDef",
    {
        "KeyId": str,
        "Status": str,
        "Type": str,
    },
    total=False,
)

BatchDeleteAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchDeleteAutomationRulesRequestRequestTypeDef",
    {
        "AutomationRulesArns": Sequence[str],
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

UnprocessedAutomationRuleTypeDef = TypedDict(
    "UnprocessedAutomationRuleTypeDef",
    {
        "RuleArn": str,
        "ErrorCode": int,
        "ErrorMessage": str,
    },
)

BatchDisableStandardsRequestRequestTypeDef = TypedDict(
    "BatchDisableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": Sequence[str],
    },
)

_RequiredStandardsSubscriptionRequestTypeDef = TypedDict(
    "_RequiredStandardsSubscriptionRequestTypeDef",
    {
        "StandardsArn": str,
    },
)
_OptionalStandardsSubscriptionRequestTypeDef = TypedDict(
    "_OptionalStandardsSubscriptionRequestTypeDef",
    {
        "StandardsInput": Mapping[str, str],
    },
    total=False,
)


class StandardsSubscriptionRequestTypeDef(
    _RequiredStandardsSubscriptionRequestTypeDef, _OptionalStandardsSubscriptionRequestTypeDef
):
    pass


BatchGetAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchGetAutomationRulesRequestRequestTypeDef",
    {
        "AutomationRulesArns": Sequence[str],
    },
)

BatchGetSecurityControlsRequestRequestTypeDef = TypedDict(
    "BatchGetSecurityControlsRequestRequestTypeDef",
    {
        "SecurityControlIds": Sequence[str],
    },
)

SecurityControlTypeDef = TypedDict(
    "SecurityControlTypeDef",
    {
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": SeverityRatingType,
        "SecurityControlStatus": ControlStatusType,
    },
)

UnprocessedSecurityControlTypeDef = TypedDict(
    "UnprocessedSecurityControlTypeDef",
    {
        "SecurityControlId": str,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": str,
    },
)

StandardsControlAssociationIdTypeDef = TypedDict(
    "StandardsControlAssociationIdTypeDef",
    {
        "SecurityControlId": str,
        "StandardsArn": str,
    },
)

StandardsControlAssociationDetailTypeDef = TypedDict(
    "StandardsControlAssociationDetailTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "AssociationStatus": AssociationStatusType,
        "RelatedRequirements": List[str],
        "UpdatedAt": datetime,
        "UpdatedReason": str,
        "StandardsControlTitle": str,
        "StandardsControlDescription": str,
        "StandardsControlArns": List[str],
    },
)

ImportFindingsErrorTypeDef = TypedDict(
    "ImportFindingsErrorTypeDef",
    {
        "Id": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

_RequiredStandardsControlAssociationUpdateTypeDef = TypedDict(
    "_RequiredStandardsControlAssociationUpdateTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "AssociationStatus": AssociationStatusType,
    },
)
_OptionalStandardsControlAssociationUpdateTypeDef = TypedDict(
    "_OptionalStandardsControlAssociationUpdateTypeDef",
    {
        "UpdatedReason": str,
    },
    total=False,
)


class StandardsControlAssociationUpdateTypeDef(
    _RequiredStandardsControlAssociationUpdateTypeDef,
    _OptionalStandardsControlAssociationUpdateTypeDef,
):
    pass


CellOutputTypeDef = TypedDict(
    "CellOutputTypeDef",
    {
        "Column": int,
        "Row": int,
        "ColumnName": str,
        "CellReference": str,
    },
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "Column": int,
        "Row": int,
        "ColumnName": str,
        "CellReference": str,
    },
    total=False,
)

ClassificationStatusOutputTypeDef = TypedDict(
    "ClassificationStatusOutputTypeDef",
    {
        "Code": str,
        "Reason": str,
    },
)

ClassificationStatusTypeDef = TypedDict(
    "ClassificationStatusTypeDef",
    {
        "Code": str,
        "Reason": str,
    },
    total=False,
)

StatusReasonOutputTypeDef = TypedDict(
    "StatusReasonOutputTypeDef",
    {
        "ReasonCode": str,
        "Description": str,
    },
)

_RequiredStatusReasonTypeDef = TypedDict(
    "_RequiredStatusReasonTypeDef",
    {
        "ReasonCode": str,
    },
)
_OptionalStatusReasonTypeDef = TypedDict(
    "_OptionalStatusReasonTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class StatusReasonTypeDef(_RequiredStatusReasonTypeDef, _OptionalStatusReasonTypeDef):
    pass


VolumeMountOutputTypeDef = TypedDict(
    "VolumeMountOutputTypeDef",
    {
        "Name": str,
        "MountPath": str,
    },
)

VolumeMountTypeDef = TypedDict(
    "VolumeMountTypeDef",
    {
        "Name": str,
        "MountPath": str,
    },
    total=False,
)

CreateActionTargetRequestRequestTypeDef = TypedDict(
    "CreateActionTargetRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Id": str,
    },
)

_RequiredCreateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFindingAggregatorRequestRequestTypeDef",
    {
        "RegionLinkingMode": str,
    },
)
_OptionalCreateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFindingAggregatorRequestRequestTypeDef",
    {
        "Regions": Sequence[str],
    },
    total=False,
)


class CreateFindingAggregatorRequestRequestTypeDef(
    _RequiredCreateFindingAggregatorRequestRequestTypeDef,
    _OptionalCreateFindingAggregatorRequestRequestTypeDef,
):
    pass


ResultTypeDef = TypedDict(
    "ResultTypeDef",
    {
        "AccountId": str,
        "ProcessingResult": str,
    },
)

DateRangeOutputTypeDef = TypedDict(
    "DateRangeOutputTypeDef",
    {
        "Value": int,
        "Unit": Literal["DAYS"],
    },
)

DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef",
    {
        "Value": int,
        "Unit": Literal["DAYS"],
    },
    total=False,
)

DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

DeleteActionTargetRequestRequestTypeDef = TypedDict(
    "DeleteActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
    },
)

DeleteFindingAggregatorRequestRequestTypeDef = TypedDict(
    "DeleteFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)

DeleteInsightRequestRequestTypeDef = TypedDict(
    "DeleteInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)

DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
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

DescribeActionTargetsRequestRequestTypeDef = TypedDict(
    "DescribeActionTargetsRequestRequestTypeDef",
    {
        "ActionTargetArns": Sequence[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeHubRequestRequestTypeDef = TypedDict(
    "DescribeHubRequestRequestTypeDef",
    {
        "HubArn": str,
    },
    total=False,
)

DescribeProductsRequestRequestTypeDef = TypedDict(
    "DescribeProductsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ProductArn": str,
    },
    total=False,
)

ProductTypeDef = TypedDict(
    "ProductTypeDef",
    {
        "ProductArn": str,
        "ProductName": str,
        "CompanyName": str,
        "Description": str,
        "Categories": List[str],
        "IntegrationTypes": List[IntegrationTypeType],
        "MarketplaceUrl": str,
        "ActivationUrl": str,
        "ProductSubscriptionResourcePolicy": str,
    },
)

_RequiredDescribeStandardsControlsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeStandardsControlsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArn": str,
    },
)
_OptionalDescribeStandardsControlsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeStandardsControlsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeStandardsControlsRequestRequestTypeDef(
    _RequiredDescribeStandardsControlsRequestRequestTypeDef,
    _OptionalDescribeStandardsControlsRequestRequestTypeDef,
):
    pass


StandardsControlTypeDef = TypedDict(
    "StandardsControlTypeDef",
    {
        "StandardsControlArn": str,
        "ControlStatus": ControlStatusType,
        "DisabledReason": str,
        "ControlStatusUpdatedAt": datetime,
        "ControlId": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": SeverityRatingType,
        "RelatedRequirements": List[str],
    },
)

DescribeStandardsRequestRequestTypeDef = TypedDict(
    "DescribeStandardsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DisableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "DisableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductSubscriptionArn": str,
    },
)

DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

DisassociateMembersRequestRequestTypeDef = TypedDict(
    "DisassociateMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

EnableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "EnableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductArn": str,
    },
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

EnableSecurityHubRequestRequestTypeDef = TypedDict(
    "EnableSecurityHubRequestRequestTypeDef",
    {
        "Tags": Mapping[str, str],
        "EnableDefaultStandards": bool,
        "ControlFindingGenerator": ControlFindingGeneratorType,
    },
    total=False,
)

FilePathsOutputTypeDef = TypedDict(
    "FilePathsOutputTypeDef",
    {
        "FilePath": str,
        "FileName": str,
        "ResourceId": str,
        "Hash": str,
    },
)

FilePathsTypeDef = TypedDict(
    "FilePathsTypeDef",
    {
        "FilePath": str,
        "FileName": str,
        "ResourceId": str,
        "Hash": str,
    },
    total=False,
)

FindingAggregatorTypeDef = TypedDict(
    "FindingAggregatorTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)

FindingHistoryUpdateSourceTypeDef = TypedDict(
    "FindingHistoryUpdateSourceTypeDef",
    {
        "Type": FindingHistoryUpdateSourceTypeType,
        "Identity": str,
    },
)

FindingHistoryUpdateTypeDef = TypedDict(
    "FindingHistoryUpdateTypeDef",
    {
        "UpdatedField": str,
        "OldValue": str,
        "NewValue": str,
    },
)

FindingProviderSeverityOutputTypeDef = TypedDict(
    "FindingProviderSeverityOutputTypeDef",
    {
        "Label": SeverityLabelType,
        "Original": str,
    },
)

FindingProviderSeverityTypeDef = TypedDict(
    "FindingProviderSeverityTypeDef",
    {
        "Label": SeverityLabelType,
        "Original": str,
    },
    total=False,
)

FirewallPolicyStatefulRuleGroupReferencesDetailsOutputTypeDef = TypedDict(
    "FirewallPolicyStatefulRuleGroupReferencesDetailsOutputTypeDef",
    {
        "ResourceArn": str,
    },
)

FirewallPolicyStatelessRuleGroupReferencesDetailsOutputTypeDef = TypedDict(
    "FirewallPolicyStatelessRuleGroupReferencesDetailsOutputTypeDef",
    {
        "Priority": int,
        "ResourceArn": str,
    },
)

FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef = TypedDict(
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef = TypedDict(
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    {
        "Priority": int,
        "ResourceArn": str,
    },
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "AccountId": str,
        "InvitationId": str,
        "InvitedAt": datetime,
        "MemberStatus": str,
    },
)

GetEnabledStandardsRequestRequestTypeDef = TypedDict(
    "GetEnabledStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": Sequence[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetFindingAggregatorRequestRequestTypeDef = TypedDict(
    "GetFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "Field": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

GetInsightResultsRequestRequestTypeDef = TypedDict(
    "GetInsightResultsRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)

GetInsightsRequestRequestTypeDef = TypedDict(
    "GetInsightsRequestRequestTypeDef",
    {
        "InsightArns": Sequence[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "AdministratorId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
)

InsightResultValueTypeDef = TypedDict(
    "InsightResultValueTypeDef",
    {
        "GroupByAttributeValue": str,
        "Count": int,
    },
)

InviteMembersRequestRequestTypeDef = TypedDict(
    "InviteMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)

ListAutomationRulesRequestRequestTypeDef = TypedDict(
    "ListAutomationRulesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEnabledProductsForImportRequestRequestTypeDef = TypedDict(
    "ListEnabledProductsForImportRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFindingAggregatorsRequestRequestTypeDef = TypedDict(
    "ListFindingAggregatorsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "OnlyAssociated": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSecurityControlDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSecurityControlDefinitionsRequestRequestTypeDef",
    {
        "StandardsArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

SecurityControlDefinitionTypeDef = TypedDict(
    "SecurityControlDefinitionTypeDef",
    {
        "SecurityControlId": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": SeverityRatingType,
        "CurrentRegionAvailability": RegionAvailabilityStatusType,
    },
)

_RequiredListStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListStandardsControlAssociationsRequestRequestTypeDef",
    {
        "SecurityControlId": str,
    },
)
_OptionalListStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListStandardsControlAssociationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListStandardsControlAssociationsRequestRequestTypeDef(
    _RequiredListStandardsControlAssociationsRequestRequestTypeDef,
    _OptionalListStandardsControlAssociationsRequestRequestTypeDef,
):
    pass


StandardsControlAssociationSummaryTypeDef = TypedDict(
    "StandardsControlAssociationSummaryTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "AssociationStatus": AssociationStatusType,
        "RelatedRequirements": List[str],
        "UpdatedAt": datetime,
        "UpdatedReason": str,
        "StandardsControlTitle": str,
        "StandardsControlDescription": str,
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

PortRangeOutputTypeDef = TypedDict(
    "PortRangeOutputTypeDef",
    {
        "Begin": int,
        "End": int,
    },
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "Begin": int,
        "End": int,
    },
    total=False,
)

RangeOutputTypeDef = TypedDict(
    "RangeOutputTypeDef",
    {
        "Start": int,
        "End": int,
        "StartColumn": int,
    },
)

RecordOutputTypeDef = TypedDict(
    "RecordOutputTypeDef",
    {
        "JsonPath": str,
        "RecordIndex": int,
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "Start": int,
        "End": int,
        "StartColumn": int,
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "JsonPath": str,
        "RecordIndex": int,
    },
    total=False,
)

RecommendationOutputTypeDef = TypedDict(
    "RecommendationOutputTypeDef",
    {
        "Text": str,
        "Url": str,
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Text": str,
        "Url": str,
    },
    total=False,
)

RuleGroupSourceListDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceListDetailsOutputTypeDef",
    {
        "GeneratedRulesType": str,
        "TargetTypes": List[str],
        "Targets": List[str],
    },
)

RuleGroupSourceListDetailsTypeDef = TypedDict(
    "RuleGroupSourceListDetailsTypeDef",
    {
        "GeneratedRulesType": str,
        "TargetTypes": Sequence[str],
        "Targets": Sequence[str],
    },
    total=False,
)

RuleGroupSourceStatefulRulesHeaderDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesHeaderDetailsOutputTypeDef",
    {
        "Destination": str,
        "DestinationPort": str,
        "Direction": str,
        "Protocol": str,
        "Source": str,
        "SourcePort": str,
    },
)

RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef",
    {
        "Keyword": str,
        "Settings": List[str],
    },
)

RuleGroupSourceStatefulRulesHeaderDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    {
        "Destination": str,
        "DestinationPort": str,
        "Direction": str,
        "Protocol": str,
        "Source": str,
        "SourcePort": str,
    },
    total=False,
)

RuleGroupSourceStatefulRulesOptionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    {
        "Keyword": str,
        "Settings": Sequence[str],
    },
    total=False,
)

RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsOutputTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
)

RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

RuleGroupSourceStatelessRuleMatchAttributesDestinationsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsOutputTypeDef",
    {
        "AddressDefinition": str,
    },
)

RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    {
        "AddressDefinition": str,
    },
    total=False,
)

RuleGroupSourceStatelessRuleMatchAttributesSourcePortsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsOutputTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
)

RuleGroupSourceStatelessRuleMatchAttributesSourcesOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesOutputTypeDef",
    {
        "AddressDefinition": str,
    },
)

RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef",
    {
        "Flags": List[str],
        "Masks": List[str],
    },
)

RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    {
        "AddressDefinition": str,
    },
    total=False,
)

RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    {
        "Flags": Sequence[str],
        "Masks": Sequence[str],
    },
    total=False,
)

RuleGroupVariablesIpSetsDetailsOutputTypeDef = TypedDict(
    "RuleGroupVariablesIpSetsDetailsOutputTypeDef",
    {
        "Definition": List[str],
    },
)

RuleGroupVariablesIpSetsDetailsTypeDef = TypedDict(
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    {
        "Definition": Sequence[str],
    },
    total=False,
)

RuleGroupVariablesPortSetsDetailsOutputTypeDef = TypedDict(
    "RuleGroupVariablesPortSetsDetailsOutputTypeDef",
    {
        "Definition": List[str],
    },
)

RuleGroupVariablesPortSetsDetailsTypeDef = TypedDict(
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    {
        "Definition": Sequence[str],
    },
    total=False,
)

SoftwarePackageOutputTypeDef = TypedDict(
    "SoftwarePackageOutputTypeDef",
    {
        "Name": str,
        "Version": str,
        "Epoch": str,
        "Release": str,
        "Architecture": str,
        "PackageManager": str,
        "FilePath": str,
        "FixedInVersion": str,
        "Remediation": str,
        "SourceLayerHash": str,
        "SourceLayerArn": str,
    },
)

SoftwarePackageTypeDef = TypedDict(
    "SoftwarePackageTypeDef",
    {
        "Name": str,
        "Version": str,
        "Epoch": str,
        "Release": str,
        "Architecture": str,
        "PackageManager": str,
        "FilePath": str,
        "FixedInVersion": str,
        "Remediation": str,
        "SourceLayerHash": str,
        "SourceLayerArn": str,
    },
    total=False,
)

StandardsManagedByTypeDef = TypedDict(
    "StandardsManagedByTypeDef",
    {
        "Company": str,
        "Product": str,
    },
)

StandardsControlAssociationIdOutputTypeDef = TypedDict(
    "StandardsControlAssociationIdOutputTypeDef",
    {
        "SecurityControlId": str,
        "StandardsArn": str,
    },
)

StandardsControlAssociationUpdateOutputTypeDef = TypedDict(
    "StandardsControlAssociationUpdateOutputTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "AssociationStatus": AssociationStatusType,
        "UpdatedReason": str,
    },
)

StandardsStatusReasonTypeDef = TypedDict(
    "StandardsStatusReasonTypeDef",
    {
        "StatusReasonCode": StatusReasonCodeType,
    },
)

StatelessCustomPublishMetricActionDimensionOutputTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionDimensionOutputTypeDef",
    {
        "Value": str,
    },
)

StatelessCustomPublishMetricActionDimensionTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    {
        "Value": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateActionTargetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
    },
)
_OptionalUpdateActionTargetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateActionTargetRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateActionTargetRequestRequestTypeDef(
    _RequiredUpdateActionTargetRequestRequestTypeDef,
    _OptionalUpdateActionTargetRequestRequestTypeDef,
):
    pass


_RequiredUpdateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
        "RegionLinkingMode": str,
    },
)
_OptionalUpdateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingAggregatorRequestRequestTypeDef",
    {
        "Regions": Sequence[str],
    },
    total=False,
)


class UpdateFindingAggregatorRequestRequestTypeDef(
    _RequiredUpdateFindingAggregatorRequestRequestTypeDef,
    _OptionalUpdateFindingAggregatorRequestRequestTypeDef,
):
    pass


_RequiredUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnable": bool,
    },
)
_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnableStandards": AutoEnableStandardsType,
    },
    total=False,
)


class UpdateOrganizationConfigurationRequestRequestTypeDef(
    _RequiredUpdateOrganizationConfigurationRequestRequestTypeDef,
    _OptionalUpdateOrganizationConfigurationRequestRequestTypeDef,
):
    pass


UpdateSecurityHubConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    {
        "AutoEnableControls": bool,
        "ControlFindingGenerator": ControlFindingGeneratorType,
    },
    total=False,
)

_RequiredUpdateStandardsControlRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStandardsControlRequestRequestTypeDef",
    {
        "StandardsControlArn": str,
    },
)
_OptionalUpdateStandardsControlRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStandardsControlRequestRequestTypeDef",
    {
        "ControlStatus": ControlStatusType,
        "DisabledReason": str,
    },
    total=False,
)


class UpdateStandardsControlRequestRequestTypeDef(
    _RequiredUpdateStandardsControlRequestRequestTypeDef,
    _OptionalUpdateStandardsControlRequestRequestTypeDef,
):
    pass


VulnerabilityVendorOutputTypeDef = TypedDict(
    "VulnerabilityVendorOutputTypeDef",
    {
        "Name": str,
        "Url": str,
        "VendorSeverity": str,
        "VendorCreatedAt": str,
        "VendorUpdatedAt": str,
    },
)

_RequiredVulnerabilityVendorTypeDef = TypedDict(
    "_RequiredVulnerabilityVendorTypeDef",
    {
        "Name": str,
    },
)
_OptionalVulnerabilityVendorTypeDef = TypedDict(
    "_OptionalVulnerabilityVendorTypeDef",
    {
        "Url": str,
        "VendorSeverity": str,
        "VendorCreatedAt": str,
        "VendorUpdatedAt": str,
    },
    total=False,
)


class VulnerabilityVendorTypeDef(
    _RequiredVulnerabilityVendorTypeDef, _OptionalVulnerabilityVendorTypeDef
):
    pass


CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "AccountDetails": Sequence[AccountDetailsTypeDef],
    },
)

ActionRemoteIpDetailsOutputTypeDef = TypedDict(
    "ActionRemoteIpDetailsOutputTypeDef",
    {
        "IpAddressV4": str,
        "Organization": IpOrganizationDetailsOutputTypeDef,
        "Country": CountryOutputTypeDef,
        "City": CityOutputTypeDef,
        "GeoLocation": GeoLocationOutputTypeDef,
    },
)

ActionRemoteIpDetailsTypeDef = TypedDict(
    "ActionRemoteIpDetailsTypeDef",
    {
        "IpAddressV4": str,
        "Organization": IpOrganizationDetailsTypeDef,
        "Country": CountryTypeDef,
        "City": CityTypeDef,
        "GeoLocation": GeoLocationTypeDef,
    },
    total=False,
)

CvssOutputTypeDef = TypedDict(
    "CvssOutputTypeDef",
    {
        "Version": str,
        "BaseScore": float,
        "BaseVector": str,
        "Source": str,
        "Adjustments": List[AdjustmentOutputTypeDef],
    },
)

CvssTypeDef = TypedDict(
    "CvssTypeDef",
    {
        "Version": str,
        "BaseScore": float,
        "BaseVector": str,
        "Source": str,
        "Adjustments": Sequence[AdjustmentTypeDef],
    },
    total=False,
)

AssociationSetDetailsOutputTypeDef = TypedDict(
    "AssociationSetDetailsOutputTypeDef",
    {
        "AssociationState": AssociationStateDetailsOutputTypeDef,
        "GatewayId": str,
        "Main": bool,
        "RouteTableAssociationId": str,
        "RouteTableId": str,
        "SubnetId": str,
    },
)

AssociationSetDetailsTypeDef = TypedDict(
    "AssociationSetDetailsTypeDef",
    {
        "AssociationState": AssociationStateDetailsTypeDef,
        "GatewayId": str,
        "Main": bool,
        "RouteTableAssociationId": str,
        "RouteTableId": str,
        "SubnetId": str,
    },
    total=False,
)

AutomationRulesFindingFieldsUpdateOutputTypeDef = TypedDict(
    "AutomationRulesFindingFieldsUpdateOutputTypeDef",
    {
        "Note": NoteUpdateOutputTypeDef,
        "Severity": SeverityUpdateOutputTypeDef,
        "VerificationState": VerificationStateType,
        "Confidence": int,
        "Criticality": int,
        "Types": List[str],
        "UserDefinedFields": Dict[str, str],
        "Workflow": WorkflowUpdateOutputTypeDef,
        "RelatedFindings": List[RelatedFindingOutputTypeDef],
    },
)

AutomationRulesFindingFieldsUpdateTypeDef = TypedDict(
    "AutomationRulesFindingFieldsUpdateTypeDef",
    {
        "Note": NoteUpdateTypeDef,
        "Severity": SeverityUpdateTypeDef,
        "VerificationState": VerificationStateType,
        "Confidence": int,
        "Criticality": int,
        "Types": Sequence[str],
        "UserDefinedFields": Mapping[str, str],
        "Workflow": WorkflowUpdateTypeDef,
        "RelatedFindings": Sequence[RelatedFindingTypeDef],
    },
    total=False,
)

AwsAmazonMqBrokerLogsDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerLogsDetailsOutputTypeDef",
    {
        "Audit": bool,
        "General": bool,
        "AuditLogGroup": str,
        "GeneralLogGroup": str,
        "Pending": AwsAmazonMqBrokerLogsPendingDetailsOutputTypeDef,
    },
)

AwsAmazonMqBrokerLogsDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLogsDetailsTypeDef",
    {
        "Audit": bool,
        "General": bool,
        "AuditLogGroup": str,
        "GeneralLogGroup": str,
        "Pending": AwsAmazonMqBrokerLogsPendingDetailsTypeDef,
    },
    total=False,
)

AwsApiGatewayRestApiDetailsOutputTypeDef = TypedDict(
    "AwsApiGatewayRestApiDetailsOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedDate": str,
        "Version": str,
        "BinaryMediaTypes": List[str],
        "MinimumCompressionSize": int,
        "ApiKeySource": str,
        "EndpointConfiguration": AwsApiGatewayEndpointConfigurationOutputTypeDef,
    },
)

AwsApiGatewayRestApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayRestApiDetailsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedDate": str,
        "Version": str,
        "BinaryMediaTypes": Sequence[str],
        "MinimumCompressionSize": int,
        "ApiKeySource": str,
        "EndpointConfiguration": AwsApiGatewayEndpointConfigurationTypeDef,
    },
    total=False,
)

AwsApiGatewayStageDetailsOutputTypeDef = TypedDict(
    "AwsApiGatewayStageDetailsOutputTypeDef",
    {
        "DeploymentId": str,
        "ClientCertificateId": str,
        "StageName": str,
        "Description": str,
        "CacheClusterEnabled": bool,
        "CacheClusterSize": str,
        "CacheClusterStatus": str,
        "MethodSettings": List[AwsApiGatewayMethodSettingsOutputTypeDef],
        "Variables": Dict[str, str],
        "DocumentationVersion": str,
        "AccessLogSettings": AwsApiGatewayAccessLogSettingsOutputTypeDef,
        "CanarySettings": AwsApiGatewayCanarySettingsOutputTypeDef,
        "TracingEnabled": bool,
        "CreatedDate": str,
        "LastUpdatedDate": str,
        "WebAclArn": str,
    },
)

AwsApiGatewayStageDetailsTypeDef = TypedDict(
    "AwsApiGatewayStageDetailsTypeDef",
    {
        "DeploymentId": str,
        "ClientCertificateId": str,
        "StageName": str,
        "Description": str,
        "CacheClusterEnabled": bool,
        "CacheClusterSize": str,
        "CacheClusterStatus": str,
        "MethodSettings": Sequence[AwsApiGatewayMethodSettingsTypeDef],
        "Variables": Mapping[str, str],
        "DocumentationVersion": str,
        "AccessLogSettings": AwsApiGatewayAccessLogSettingsTypeDef,
        "CanarySettings": AwsApiGatewayCanarySettingsTypeDef,
        "TracingEnabled": bool,
        "CreatedDate": str,
        "LastUpdatedDate": str,
        "WebAclArn": str,
    },
    total=False,
)

AwsApiGatewayV2ApiDetailsOutputTypeDef = TypedDict(
    "AwsApiGatewayV2ApiDetailsOutputTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": str,
        "Description": str,
        "Version": str,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "CorsConfiguration": AwsCorsConfigurationOutputTypeDef,
    },
)

AwsApiGatewayV2ApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2ApiDetailsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": str,
        "Description": str,
        "Version": str,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "CorsConfiguration": AwsCorsConfigurationTypeDef,
    },
    total=False,
)

AwsApiGatewayV2StageDetailsOutputTypeDef = TypedDict(
    "AwsApiGatewayV2StageDetailsOutputTypeDef",
    {
        "ClientCertificateId": str,
        "CreatedDate": str,
        "Description": str,
        "DefaultRouteSettings": AwsApiGatewayV2RouteSettingsOutputTypeDef,
        "DeploymentId": str,
        "LastUpdatedDate": str,
        "RouteSettings": AwsApiGatewayV2RouteSettingsOutputTypeDef,
        "StageName": str,
        "StageVariables": Dict[str, str],
        "AccessLogSettings": AwsApiGatewayAccessLogSettingsOutputTypeDef,
        "AutoDeploy": bool,
        "LastDeploymentStatusMessage": str,
        "ApiGatewayManaged": bool,
    },
)

AwsApiGatewayV2StageDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2StageDetailsTypeDef",
    {
        "ClientCertificateId": str,
        "CreatedDate": str,
        "Description": str,
        "DefaultRouteSettings": AwsApiGatewayV2RouteSettingsTypeDef,
        "DeploymentId": str,
        "LastUpdatedDate": str,
        "RouteSettings": AwsApiGatewayV2RouteSettingsTypeDef,
        "StageName": str,
        "StageVariables": Mapping[str, str],
        "AccessLogSettings": AwsApiGatewayAccessLogSettingsTypeDef,
        "AutoDeploy": bool,
        "LastDeploymentStatusMessage": str,
        "ApiGatewayManaged": bool,
    },
    total=False,
)

AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsOutputTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsOutputTypeDef",
    {
        "AuthenticationType": str,
        "LambdaAuthorizerConfig": AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsOutputTypeDef,
        "OpenIdConnectConfig": AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsOutputTypeDef,
        "UserPoolConfig": AwsAppSyncGraphQlApiUserPoolConfigDetailsOutputTypeDef,
    },
)

AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef",
    {
        "AuthenticationType": str,
        "LambdaAuthorizerConfig": AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef,
        "OpenIdConnectConfig": AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef,
        "UserPoolConfig": AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef,
    },
    total=False,
)

AwsAthenaWorkGroupConfigurationResultConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsOutputTypeDef",
    {
        "EncryptionConfiguration": AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsOutputTypeDef,
    },
)

AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef",
    {
        "EncryptionConfiguration": (
            AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef
        ),
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef",
    {
        "LaunchTemplateSpecification": AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputTypeDef,
        "Overrides": List[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsOutputTypeDef
        ],
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    {
        "LaunchTemplateSpecification": AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": Sequence[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef
        ],
    },
    total=False,
)

AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsOutputTypeDef",
    {
        "DeviceName": str,
        "Ebs": AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsOutputTypeDef,
        "NoDevice": bool,
        "VirtualName": str,
    },
)

AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    {
        "DeviceName": str,
        "Ebs": AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef,
        "NoDevice": bool,
        "VirtualName": str,
    },
    total=False,
)

AwsBackupBackupPlanRuleCopyActionsDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleCopyActionsDetailsOutputTypeDef",
    {
        "DestinationBackupVaultArn": str,
        "Lifecycle": AwsBackupBackupPlanLifecycleDetailsOutputTypeDef,
    },
)

AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef",
    {
        "DestinationBackupVaultArn": str,
        "Lifecycle": AwsBackupBackupPlanLifecycleDetailsTypeDef,
    },
    total=False,
)

AwsBackupBackupVaultDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupVaultDetailsOutputTypeDef",
    {
        "BackupVaultArn": str,
        "BackupVaultName": str,
        "EncryptionKeyArn": str,
        "Notifications": AwsBackupBackupVaultNotificationsDetailsOutputTypeDef,
        "AccessPolicy": str,
    },
)

AwsBackupBackupVaultDetailsTypeDef = TypedDict(
    "AwsBackupBackupVaultDetailsTypeDef",
    {
        "BackupVaultArn": str,
        "BackupVaultName": str,
        "EncryptionKeyArn": str,
        "Notifications": AwsBackupBackupVaultNotificationsDetailsTypeDef,
        "AccessPolicy": str,
    },
    total=False,
)

AwsBackupRecoveryPointDetailsOutputTypeDef = TypedDict(
    "AwsBackupRecoveryPointDetailsOutputTypeDef",
    {
        "BackupSizeInBytes": int,
        "BackupVaultArn": str,
        "BackupVaultName": str,
        "CalculatedLifecycle": AwsBackupRecoveryPointCalculatedLifecycleDetailsOutputTypeDef,
        "CompletionDate": str,
        "CreatedBy": AwsBackupRecoveryPointCreatedByDetailsOutputTypeDef,
        "CreationDate": str,
        "EncryptionKeyArn": str,
        "IamRoleArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": str,
        "Lifecycle": AwsBackupRecoveryPointLifecycleDetailsOutputTypeDef,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "SourceBackupVaultArn": str,
        "Status": str,
        "StatusMessage": str,
        "StorageClass": str,
    },
)

AwsBackupRecoveryPointDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointDetailsTypeDef",
    {
        "BackupSizeInBytes": int,
        "BackupVaultArn": str,
        "BackupVaultName": str,
        "CalculatedLifecycle": AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef,
        "CompletionDate": str,
        "CreatedBy": AwsBackupRecoveryPointCreatedByDetailsTypeDef,
        "CreationDate": str,
        "EncryptionKeyArn": str,
        "IamRoleArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": str,
        "Lifecycle": AwsBackupRecoveryPointLifecycleDetailsTypeDef,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "SourceBackupVaultArn": str,
        "Status": str,
        "StatusMessage": str,
        "StorageClass": str,
    },
    total=False,
)

AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef",
    {
        "DomainName": str,
        "ResourceRecord": AwsCertificateManagerCertificateResourceRecordOutputTypeDef,
        "ValidationDomain": str,
        "ValidationEmails": List[str],
        "ValidationMethod": str,
        "ValidationStatus": str,
    },
)

AwsCertificateManagerCertificateDomainValidationOptionTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    {
        "DomainName": str,
        "ResourceRecord": AwsCertificateManagerCertificateResourceRecordTypeDef,
        "ValidationDomain": str,
        "ValidationEmails": Sequence[str],
        "ValidationMethod": str,
        "ValidationStatus": str,
    },
    total=False,
)

AwsCloudFormationStackDetailsOutputTypeDef = TypedDict(
    "AwsCloudFormationStackDetailsOutputTypeDef",
    {
        "Capabilities": List[str],
        "CreationTime": str,
        "Description": str,
        "DisableRollback": bool,
        "DriftInformation": AwsCloudFormationStackDriftInformationDetailsOutputTypeDef,
        "EnableTerminationProtection": bool,
        "LastUpdatedTime": str,
        "NotificationArns": List[str],
        "Outputs": List[AwsCloudFormationStackOutputsDetailsOutputTypeDef],
        "RoleArn": str,
        "StackId": str,
        "StackName": str,
        "StackStatus": str,
        "StackStatusReason": str,
        "TimeoutInMinutes": int,
    },
)

AwsCloudFormationStackDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackDetailsTypeDef",
    {
        "Capabilities": Sequence[str],
        "CreationTime": str,
        "Description": str,
        "DisableRollback": bool,
        "DriftInformation": AwsCloudFormationStackDriftInformationDetailsTypeDef,
        "EnableTerminationProtection": bool,
        "LastUpdatedTime": str,
        "NotificationArns": Sequence[str],
        "Outputs": Sequence[AwsCloudFormationStackOutputsDetailsTypeDef],
        "RoleArn": str,
        "StackId": str,
        "StackName": str,
        "StackStatus": str,
        "StackStatusReason": str,
        "TimeoutInMinutes": int,
    },
    total=False,
)

AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef",
    {
        "Items": List[AwsCloudFrontDistributionCacheBehaviorOutputTypeDef],
    },
)

AwsCloudFrontDistributionCacheBehaviorsTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    {
        "Items": Sequence[AwsCloudFrontDistributionCacheBehaviorTypeDef],
    },
    total=False,
)

AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef",
    {
        "HttpPort": int,
        "HttpsPort": int,
        "OriginKeepaliveTimeout": int,
        "OriginProtocolPolicy": str,
        "OriginReadTimeout": int,
        "OriginSslProtocols": AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef,
    },
)

AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef",
    {
        "HttpPort": int,
        "HttpsPort": int,
        "OriginKeepaliveTimeout": int,
        "OriginProtocolPolicy": str,
        "OriginReadTimeout": int,
        "OriginSslProtocols": AwsCloudFrontDistributionOriginSslProtocolsTypeDef,
    },
    total=False,
)

AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef",
    {
        "StatusCodes": AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef,
    },
)

AwsCloudFrontDistributionOriginGroupFailoverTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    {
        "StatusCodes": AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef,
    },
    total=False,
)

AwsCloudWatchAlarmDetailsOutputTypeDef = TypedDict(
    "AwsCloudWatchAlarmDetailsOutputTypeDef",
    {
        "ActionsEnabled": bool,
        "AlarmActions": List[str],
        "AlarmArn": str,
        "AlarmConfigurationUpdatedTimestamp": str,
        "AlarmDescription": str,
        "AlarmName": str,
        "ComparisonOperator": str,
        "DatapointsToAlarm": int,
        "Dimensions": List[AwsCloudWatchAlarmDimensionsDetailsOutputTypeDef],
        "EvaluateLowSampleCountPercentile": str,
        "EvaluationPeriods": int,
        "ExtendedStatistic": str,
        "InsufficientDataActions": List[str],
        "MetricName": str,
        "Namespace": str,
        "OkActions": List[str],
        "Period": int,
        "Statistic": str,
        "Threshold": float,
        "ThresholdMetricId": str,
        "TreatMissingData": str,
        "Unit": str,
    },
)

AwsCloudWatchAlarmDetailsTypeDef = TypedDict(
    "AwsCloudWatchAlarmDetailsTypeDef",
    {
        "ActionsEnabled": bool,
        "AlarmActions": Sequence[str],
        "AlarmArn": str,
        "AlarmConfigurationUpdatedTimestamp": str,
        "AlarmDescription": str,
        "AlarmName": str,
        "ComparisonOperator": str,
        "DatapointsToAlarm": int,
        "Dimensions": Sequence[AwsCloudWatchAlarmDimensionsDetailsTypeDef],
        "EvaluateLowSampleCountPercentile": str,
        "EvaluationPeriods": int,
        "ExtendedStatistic": str,
        "InsufficientDataActions": Sequence[str],
        "MetricName": str,
        "Namespace": str,
        "OkActions": Sequence[str],
        "Period": int,
        "Statistic": str,
        "Threshold": float,
        "ThresholdMetricId": str,
        "TreatMissingData": str,
        "Unit": str,
    },
    total=False,
)

AwsCodeBuildProjectEnvironmentOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentOutputTypeDef",
    {
        "Certificate": str,
        "EnvironmentVariables": List[
            AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsOutputTypeDef
        ],
        "PrivilegedMode": bool,
        "ImagePullCredentialsType": str,
        "RegistryCredential": AwsCodeBuildProjectEnvironmentRegistryCredentialOutputTypeDef,
        "Type": str,
    },
)

AwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": str,
        "EnvironmentVariables": Sequence[
            AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef
        ],
        "PrivilegedMode": bool,
        "ImagePullCredentialsType": str,
        "RegistryCredential": AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef,
        "Type": str,
    },
    total=False,
)

AwsCodeBuildProjectLogsConfigDetailsOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigDetailsOutputTypeDef",
    {
        "CloudWatchLogs": AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsOutputTypeDef,
        "S3Logs": AwsCodeBuildProjectLogsConfigS3LogsDetailsOutputTypeDef,
    },
)

AwsCodeBuildProjectLogsConfigDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    {
        "CloudWatchLogs": AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef,
        "S3Logs": AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef,
    },
    total=False,
)

AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef = TypedDict(
    "AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef",
    {
        "Backfilling": bool,
        "IndexArn": str,
        "IndexName": str,
        "IndexSizeBytes": int,
        "IndexStatus": str,
        "ItemCount": int,
        "KeySchema": List[AwsDynamoDbTableKeySchemaOutputTypeDef],
        "Projection": AwsDynamoDbTableProjectionOutputTypeDef,
        "ProvisionedThroughput": AwsDynamoDbTableProvisionedThroughputOutputTypeDef,
    },
)

AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef = TypedDict(
    "AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef",
    {
        "IndexArn": str,
        "IndexName": str,
        "KeySchema": List[AwsDynamoDbTableKeySchemaOutputTypeDef],
        "Projection": AwsDynamoDbTableProjectionOutputTypeDef,
    },
)

AwsDynamoDbTableGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    {
        "Backfilling": bool,
        "IndexArn": str,
        "IndexName": str,
        "IndexSizeBytes": int,
        "IndexStatus": str,
        "ItemCount": int,
        "KeySchema": Sequence[AwsDynamoDbTableKeySchemaTypeDef],
        "Projection": AwsDynamoDbTableProjectionTypeDef,
        "ProvisionedThroughput": AwsDynamoDbTableProvisionedThroughputTypeDef,
    },
    total=False,
)

AwsDynamoDbTableLocalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    {
        "IndexArn": str,
        "IndexName": str,
        "KeySchema": Sequence[AwsDynamoDbTableKeySchemaTypeDef],
        "Projection": AwsDynamoDbTableProjectionTypeDef,
    },
    total=False,
)

AwsDynamoDbTableReplicaGlobalSecondaryIndexOutputTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexOutputTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": AwsDynamoDbTableProvisionedThroughputOverrideOutputTypeDef,
    },
)

AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": AwsDynamoDbTableProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

AwsEc2InstanceDetailsOutputTypeDef = TypedDict(
    "AwsEc2InstanceDetailsOutputTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
        "NetworkInterfaces": List[AwsEc2InstanceNetworkInterfacesDetailsOutputTypeDef],
        "VirtualizationType": str,
        "MetadataOptions": AwsEc2InstanceMetadataOptionsOutputTypeDef,
        "Monitoring": AwsEc2InstanceMonitoringDetailsOutputTypeDef,
    },
)

AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": Sequence[str],
        "IpV6Addresses": Sequence[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
        "NetworkInterfaces": Sequence[AwsEc2InstanceNetworkInterfacesDetailsTypeDef],
        "VirtualizationType": str,
        "MetadataOptions": AwsEc2InstanceMetadataOptionsTypeDef,
        "Monitoring": AwsEc2InstanceMonitoringDetailsTypeDef,
    },
    total=False,
)

AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsOutputTypeDef",
    {
        "DeviceName": str,
        "Ebs": AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsOutputTypeDef,
        "NoDevice": str,
        "VirtualName": str,
    },
)

AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef",
    {
        "DeviceName": str,
        "Ebs": AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef,
        "NoDevice": str,
        "VirtualName": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsOutputTypeDef",
    {
        "CapacityReservationPreference": str,
        "CapacityReservationTarget": AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsOutputTypeDef,
    },
)

AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef",
    {
        "CapacityReservationPreference": str,
        "CapacityReservationTarget": AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsOutputTypeDef",
    {
        "MarketType": str,
        "SpotOptions": AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsOutputTypeDef,
    },
)

AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef",
    {
        "MarketType": str,
        "SpotOptions": AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef,
    },
    total=False,
)

AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef",
    {
        "AcceleratorCount": (
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsOutputTypeDef
        ),
        "AcceleratorManufacturers": List[str],
        "AcceleratorNames": List[str],
        "AcceleratorTotalMemoryMiB": AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsOutputTypeDef,
        "AcceleratorTypes": List[str],
        "BareMetal": str,
        "BaselineEbsBandwidthMbps": (
            AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsOutputTypeDef
        ),
        "BurstablePerformance": str,
        "CpuManufacturers": List[str],
        "ExcludedInstanceTypes": List[str],
        "InstanceGenerations": List[str],
        "LocalStorage": str,
        "LocalStorageTypes": List[str],
        "MemoryGiBPerVCpu": (
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsOutputTypeDef
        ),
        "MemoryMiB": AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsOutputTypeDef,
        "NetworkInterfaceCount": (
            AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsOutputTypeDef
        ),
        "OnDemandMaxPricePercentageOverLowestPrice": int,
        "RequireHibernateSupport": bool,
        "SpotMaxPricePercentageOverLowestPrice": int,
        "TotalLocalStorageGB": (
            AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsOutputTypeDef
        ),
        "VCpuCount": AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsOutputTypeDef,
    },
)

AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef",
    {
        "AcceleratorCount": (
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef
        ),
        "AcceleratorManufacturers": Sequence[str],
        "AcceleratorNames": Sequence[str],
        "AcceleratorTotalMemoryMiB": (
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef
        ),
        "AcceleratorTypes": Sequence[str],
        "BareMetal": str,
        "BaselineEbsBandwidthMbps": (
            AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef
        ),
        "BurstablePerformance": str,
        "CpuManufacturers": Sequence[str],
        "ExcludedInstanceTypes": Sequence[str],
        "InstanceGenerations": Sequence[str],
        "LocalStorage": str,
        "LocalStorageTypes": Sequence[str],
        "MemoryGiBPerVCpu": (
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef
        ),
        "MemoryMiB": AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef,
        "NetworkInterfaceCount": (
            AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef
        ),
        "OnDemandMaxPricePercentageOverLowestPrice": int,
        "RequireHibernateSupport": bool,
        "SpotMaxPricePercentageOverLowestPrice": int,
        "TotalLocalStorageGB": (
            AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef
        ),
        "VCpuCount": AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef,
    },
    total=False,
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef",
    {
        "AssociateCarrierIpAddress": bool,
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "InterfaceType": str,
        "Ipv4PrefixCount": int,
        "Ipv4Prefixes": List[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsOutputTypeDef
        ],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsOutputTypeDef
        ],
        "Ipv6PrefixCount": int,
        "Ipv6Prefixes": List[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsOutputTypeDef
        ],
        "NetworkCardIndex": int,
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsOutputTypeDef
        ],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
    },
)

AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef",
    {
        "AssociateCarrierIpAddress": bool,
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": Sequence[str],
        "InterfaceType": str,
        "Ipv4PrefixCount": int,
        "Ipv4Prefixes": Sequence[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef
        ],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": Sequence[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef
        ],
        "Ipv6PrefixCount": int,
        "Ipv6Prefixes": Sequence[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef
        ],
        "NetworkCardIndex": int,
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": Sequence[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef
        ],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
    },
    total=False,
)

AwsEc2NetworkAclEntryOutputTypeDef = TypedDict(
    "AwsEc2NetworkAclEntryOutputTypeDef",
    {
        "CidrBlock": str,
        "Egress": bool,
        "IcmpTypeCode": IcmpTypeCodeOutputTypeDef,
        "Ipv6CidrBlock": str,
        "PortRange": PortRangeFromToOutputTypeDef,
        "Protocol": str,
        "RuleAction": str,
        "RuleNumber": int,
    },
)

AwsEc2NetworkAclEntryTypeDef = TypedDict(
    "AwsEc2NetworkAclEntryTypeDef",
    {
        "CidrBlock": str,
        "Egress": bool,
        "IcmpTypeCode": IcmpTypeCodeTypeDef,
        "Ipv6CidrBlock": str,
        "PortRange": PortRangeFromToTypeDef,
        "Protocol": str,
        "RuleAction": str,
        "RuleNumber": int,
    },
    total=False,
)

AwsEc2NetworkInterfaceDetailsOutputTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsOutputTypeDef",
    {
        "Attachment": AwsEc2NetworkInterfaceAttachmentOutputTypeDef,
        "NetworkInterfaceId": str,
        "SecurityGroups": List[AwsEc2NetworkInterfaceSecurityGroupOutputTypeDef],
        "SourceDestCheck": bool,
        "IpV6Addresses": List[AwsEc2NetworkInterfaceIpV6AddressDetailOutputTypeDef],
        "PrivateIpAddresses": List[AwsEc2NetworkInterfacePrivateIpAddressDetailOutputTypeDef],
        "PublicDnsName": str,
        "PublicIp": str,
    },
)

AwsEc2NetworkInterfaceDetailsTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    {
        "Attachment": AwsEc2NetworkInterfaceAttachmentTypeDef,
        "NetworkInterfaceId": str,
        "SecurityGroups": Sequence[AwsEc2NetworkInterfaceSecurityGroupTypeDef],
        "SourceDestCheck": bool,
        "IpV6Addresses": Sequence[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef],
        "PrivateIpAddresses": Sequence[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef],
        "PublicDnsName": str,
        "PublicIp": str,
    },
    total=False,
)

AwsEc2SecurityGroupIpPermissionOutputTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionOutputTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "UserIdGroupPairs": List[AwsEc2SecurityGroupUserIdGroupPairOutputTypeDef],
        "IpRanges": List[AwsEc2SecurityGroupIpRangeOutputTypeDef],
        "Ipv6Ranges": List[AwsEc2SecurityGroupIpv6RangeOutputTypeDef],
        "PrefixListIds": List[AwsEc2SecurityGroupPrefixListIdOutputTypeDef],
    },
)

AwsEc2SecurityGroupIpPermissionTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "UserIdGroupPairs": Sequence[AwsEc2SecurityGroupUserIdGroupPairTypeDef],
        "IpRanges": Sequence[AwsEc2SecurityGroupIpRangeTypeDef],
        "Ipv6Ranges": Sequence[AwsEc2SecurityGroupIpv6RangeTypeDef],
        "PrefixListIds": Sequence[AwsEc2SecurityGroupPrefixListIdTypeDef],
    },
    total=False,
)

AwsEc2SubnetDetailsOutputTypeDef = TypedDict(
    "AwsEc2SubnetDetailsOutputTypeDef",
    {
        "AssignIpv6AddressOnCreation": bool,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "AvailableIpAddressCount": int,
        "CidrBlock": str,
        "DefaultForAz": bool,
        "MapPublicIpOnLaunch": bool,
        "OwnerId": str,
        "State": str,
        "SubnetArn": str,
        "SubnetId": str,
        "VpcId": str,
        "Ipv6CidrBlockAssociationSet": List[Ipv6CidrBlockAssociationOutputTypeDef],
    },
)

AwsEc2SubnetDetailsTypeDef = TypedDict(
    "AwsEc2SubnetDetailsTypeDef",
    {
        "AssignIpv6AddressOnCreation": bool,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "AvailableIpAddressCount": int,
        "CidrBlock": str,
        "DefaultForAz": bool,
        "MapPublicIpOnLaunch": bool,
        "OwnerId": str,
        "State": str,
        "SubnetArn": str,
        "SubnetId": str,
        "VpcId": str,
        "Ipv6CidrBlockAssociationSet": Sequence[Ipv6CidrBlockAssociationTypeDef],
    },
    total=False,
)

AwsEc2VolumeDetailsOutputTypeDef = TypedDict(
    "AwsEc2VolumeDetailsOutputTypeDef",
    {
        "CreateTime": str,
        "DeviceName": str,
        "Encrypted": bool,
        "Size": int,
        "SnapshotId": str,
        "Status": str,
        "KmsKeyId": str,
        "Attachments": List[AwsEc2VolumeAttachmentOutputTypeDef],
        "VolumeId": str,
        "VolumeType": str,
        "VolumeScanStatus": str,
    },
)

AwsEc2VolumeDetailsTypeDef = TypedDict(
    "AwsEc2VolumeDetailsTypeDef",
    {
        "CreateTime": str,
        "DeviceName": str,
        "Encrypted": bool,
        "Size": int,
        "SnapshotId": str,
        "Status": str,
        "KmsKeyId": str,
        "Attachments": Sequence[AwsEc2VolumeAttachmentTypeDef],
        "VolumeId": str,
        "VolumeType": str,
        "VolumeScanStatus": str,
    },
    total=False,
)

AwsEc2VpcDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcDetailsOutputTypeDef",
    {
        "CidrBlockAssociationSet": List[CidrBlockAssociationOutputTypeDef],
        "Ipv6CidrBlockAssociationSet": List[Ipv6CidrBlockAssociationOutputTypeDef],
        "DhcpOptionsId": str,
        "State": str,
    },
)

AwsEc2VpcDetailsTypeDef = TypedDict(
    "AwsEc2VpcDetailsTypeDef",
    {
        "CidrBlockAssociationSet": Sequence[CidrBlockAssociationTypeDef],
        "Ipv6CidrBlockAssociationSet": Sequence[Ipv6CidrBlockAssociationTypeDef],
        "DhcpOptionsId": str,
        "State": str,
    },
    total=False,
)

AwsEc2VpcEndpointServiceDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsOutputTypeDef",
    {
        "AcceptanceRequired": bool,
        "AvailabilityZones": List[str],
        "BaseEndpointDnsNames": List[str],
        "ManagesVpcEndpoints": bool,
        "GatewayLoadBalancerArns": List[str],
        "NetworkLoadBalancerArns": List[str],
        "PrivateDnsName": str,
        "ServiceId": str,
        "ServiceName": str,
        "ServiceState": str,
        "ServiceType": List[AwsEc2VpcEndpointServiceServiceTypeDetailsOutputTypeDef],
    },
)

AwsEc2VpcEndpointServiceDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    {
        "AcceptanceRequired": bool,
        "AvailabilityZones": Sequence[str],
        "BaseEndpointDnsNames": Sequence[str],
        "ManagesVpcEndpoints": bool,
        "GatewayLoadBalancerArns": Sequence[str],
        "NetworkLoadBalancerArns": Sequence[str],
        "PrivateDnsName": str,
        "ServiceId": str,
        "ServiceName": str,
        "ServiceState": str,
        "ServiceType": Sequence[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef],
    },
    total=False,
)

AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef",
    {
        "CidrBlock": str,
        "CidrBlockSet": List[VpcInfoCidrBlockSetDetailsOutputTypeDef],
        "Ipv6CidrBlockSet": List[VpcInfoIpv6CidrBlockSetDetailsOutputTypeDef],
        "OwnerId": str,
        "PeeringOptions": VpcInfoPeeringOptionsDetailsOutputTypeDef,
        "Region": str,
        "VpcId": str,
    },
)

AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef",
    {
        "CidrBlock": str,
        "CidrBlockSet": Sequence[VpcInfoCidrBlockSetDetailsTypeDef],
        "Ipv6CidrBlockSet": Sequence[VpcInfoIpv6CidrBlockSetDetailsTypeDef],
        "OwnerId": str,
        "PeeringOptions": VpcInfoPeeringOptionsDetailsTypeDef,
        "Region": str,
        "VpcId": str,
    },
    total=False,
)

AwsEc2VpnConnectionOptionsDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsDetailsOutputTypeDef",
    {
        "StaticRoutesOnly": bool,
        "TunnelOptions": List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef],
    },
)

AwsEc2VpnConnectionOptionsDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    {
        "StaticRoutesOnly": bool,
        "TunnelOptions": Sequence[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef],
    },
    total=False,
)

AwsEcrRepositoryDetailsOutputTypeDef = TypedDict(
    "AwsEcrRepositoryDetailsOutputTypeDef",
    {
        "Arn": str,
        "ImageScanningConfiguration": (
            AwsEcrRepositoryImageScanningConfigurationDetailsOutputTypeDef
        ),
        "ImageTagMutability": str,
        "LifecyclePolicy": AwsEcrRepositoryLifecyclePolicyDetailsOutputTypeDef,
        "RepositoryName": str,
        "RepositoryPolicyText": str,
    },
)

AwsEcrRepositoryDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryDetailsTypeDef",
    {
        "Arn": str,
        "ImageScanningConfiguration": AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef,
        "ImageTagMutability": str,
        "LifecyclePolicy": AwsEcrRepositoryLifecyclePolicyDetailsTypeDef,
        "RepositoryName": str,
        "RepositoryPolicyText": str,
    },
    total=False,
)

AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsOutputTypeDef",
    {
        "KmsKeyId": str,
        "LogConfiguration": AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsOutputTypeDef,
        "Logging": str,
    },
)

AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    {
        "KmsKeyId": str,
        "LogConfiguration": (
            AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef
        ),
        "Logging": str,
    },
    total=False,
)

AwsEcsContainerDetailsOutputTypeDef = TypedDict(
    "AwsEcsContainerDetailsOutputTypeDef",
    {
        "Name": str,
        "Image": str,
        "MountPoints": List[AwsMountPointOutputTypeDef],
        "Privileged": bool,
    },
)

AwsEcsContainerDetailsTypeDef = TypedDict(
    "AwsEcsContainerDetailsTypeDef",
    {
        "Name": str,
        "Image": str,
        "MountPoints": Sequence[AwsMountPointTypeDef],
        "Privileged": bool,
    },
    total=False,
)

AwsEcsServiceDeploymentConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDetailsOutputTypeDef",
    {
        "DeploymentCircuitBreaker": (
            AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsOutputTypeDef
        ),
        "MaximumPercent": int,
        "MinimumHealthyPercent": int,
    },
)

AwsEcsServiceDeploymentConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    {
        "DeploymentCircuitBreaker": (
            AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef
        ),
        "MaximumPercent": int,
        "MinimumHealthyPercent": int,
    },
    total=False,
)

AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef",
    {
        "AwsVpcConfiguration": (
            AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef
        ),
    },
)

AwsEcsServiceNetworkConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    {
        "AwsVpcConfiguration": AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef",
    {
        "Capabilities": (
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef
        ),
        "Devices": List[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef
        ],
        "InitProcessEnabled": bool,
        "MaxSwap": int,
        "SharedMemorySize": int,
        "Swappiness": int,
        "Tmpfs": List[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef
        ],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    {
        "Capabilities": (
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef
        ),
        "Devices": Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef
        ],
        "InitProcessEnabled": bool,
        "MaxSwap": int,
        "SharedMemorySize": int,
        "Swappiness": int,
        "Tmpfs": Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef
        ],
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef",
    {
        "LogDriver": str,
        "Options": Dict[str, str],
        "SecretOptions": List[
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsOutputTypeDef
        ],
    },
)

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    {
        "LogDriver": str,
        "Options": Mapping[str, str],
        "SecretOptions": Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef
        ],
    },
    total=False,
)

AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef",
    {
        "ContainerName": str,
        "ProxyConfigurationProperties": List[
            AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsOutputTypeDef
        ],
        "Type": str,
    },
)

AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    {
        "ContainerName": str,
        "ProxyConfigurationProperties": Sequence[
            AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef
        ],
        "Type": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsOutputTypeDef",
    {
        "AuthorizationConfig": (
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsOutputTypeDef
        ),
        "FilesystemId": str,
        "RootDirectory": str,
        "TransitEncryption": str,
        "TransitEncryptionPort": int,
    },
)

AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    {
        "AuthorizationConfig": (
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef
        ),
        "FilesystemId": str,
        "RootDirectory": str,
        "TransitEncryption": str,
        "TransitEncryptionPort": int,
    },
    total=False,
)

AwsEcsTaskVolumeDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskVolumeDetailsOutputTypeDef",
    {
        "Name": str,
        "Host": AwsEcsTaskVolumeHostDetailsOutputTypeDef,
    },
)

AwsEcsTaskVolumeDetailsTypeDef = TypedDict(
    "AwsEcsTaskVolumeDetailsTypeDef",
    {
        "Name": str,
        "Host": AwsEcsTaskVolumeHostDetailsTypeDef,
    },
    total=False,
)

AwsEfsAccessPointRootDirectoryDetailsOutputTypeDef = TypedDict(
    "AwsEfsAccessPointRootDirectoryDetailsOutputTypeDef",
    {
        "CreationInfo": AwsEfsAccessPointRootDirectoryCreationInfoDetailsOutputTypeDef,
        "Path": str,
    },
)

AwsEfsAccessPointRootDirectoryDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointRootDirectoryDetailsTypeDef",
    {
        "CreationInfo": AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef,
        "Path": str,
    },
    total=False,
)

AwsEksClusterLoggingDetailsOutputTypeDef = TypedDict(
    "AwsEksClusterLoggingDetailsOutputTypeDef",
    {
        "ClusterLogging": List[AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef],
    },
)

AwsEksClusterLoggingDetailsTypeDef = TypedDict(
    "AwsEksClusterLoggingDetailsTypeDef",
    {
        "ClusterLogging": Sequence[AwsEksClusterLoggingClusterLoggingDetailsTypeDef],
    },
    total=False,
)

AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef",
    {
        "ApplicationName": str,
        "Cname": str,
        "DateCreated": str,
        "DateUpdated": str,
        "Description": str,
        "EndpointUrl": str,
        "EnvironmentArn": str,
        "EnvironmentId": str,
        "EnvironmentLinks": List[AwsElasticBeanstalkEnvironmentEnvironmentLinkOutputTypeDef],
        "EnvironmentName": str,
        "OptionSettings": List[AwsElasticBeanstalkEnvironmentOptionSettingOutputTypeDef],
        "PlatformArn": str,
        "SolutionStackName": str,
        "Status": str,
        "Tier": AwsElasticBeanstalkEnvironmentTierOutputTypeDef,
        "VersionLabel": str,
    },
)

AwsElasticBeanstalkEnvironmentDetailsTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    {
        "ApplicationName": str,
        "Cname": str,
        "DateCreated": str,
        "DateUpdated": str,
        "Description": str,
        "EndpointUrl": str,
        "EnvironmentArn": str,
        "EnvironmentId": str,
        "EnvironmentLinks": Sequence[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef],
        "EnvironmentName": str,
        "OptionSettings": Sequence[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef],
        "PlatformArn": str,
        "SolutionStackName": str,
        "Status": str,
        "Tier": AwsElasticBeanstalkEnvironmentTierTypeDef,
        "VersionLabel": str,
    },
    total=False,
)

AwsElasticsearchDomainElasticsearchClusterConfigDetailsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsOutputTypeDef",
    {
        "DedicatedMasterCount": int,
        "DedicatedMasterEnabled": bool,
        "DedicatedMasterType": str,
        "InstanceCount": int,
        "InstanceType": str,
        "ZoneAwarenessConfig": (
            AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsOutputTypeDef
        ),
        "ZoneAwarenessEnabled": bool,
    },
)

AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    {
        "DedicatedMasterCount": int,
        "DedicatedMasterEnabled": bool,
        "DedicatedMasterType": str,
        "InstanceCount": int,
        "InstanceType": str,
        "ZoneAwarenessConfig": (
            AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef
        ),
        "ZoneAwarenessEnabled": bool,
    },
    total=False,
)

AwsElasticsearchDomainLogPublishingOptionsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsOutputTypeDef",
    {
        "IndexSlowLogs": AwsElasticsearchDomainLogPublishingOptionsLogConfigOutputTypeDef,
        "SearchSlowLogs": AwsElasticsearchDomainLogPublishingOptionsLogConfigOutputTypeDef,
        "AuditLogs": AwsElasticsearchDomainLogPublishingOptionsLogConfigOutputTypeDef,
    },
)

AwsElasticsearchDomainLogPublishingOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    {
        "IndexSlowLogs": AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef,
        "SearchSlowLogs": AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef,
        "AuditLogs": AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef,
    },
    total=False,
)

AwsElbLoadBalancerPoliciesOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerPoliciesOutputTypeDef",
    {
        "AppCookieStickinessPolicies": List[AwsElbAppCookieStickinessPolicyOutputTypeDef],
        "LbCookieStickinessPolicies": List[AwsElbLbCookieStickinessPolicyOutputTypeDef],
        "OtherPolicies": List[str],
    },
)

AwsElbLoadBalancerPoliciesTypeDef = TypedDict(
    "AwsElbLoadBalancerPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": Sequence[AwsElbAppCookieStickinessPolicyTypeDef],
        "LbCookieStickinessPolicies": Sequence[AwsElbLbCookieStickinessPolicyTypeDef],
        "OtherPolicies": Sequence[str],
    },
    total=False,
)

AwsElbLoadBalancerAttributesOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerAttributesOutputTypeDef",
    {
        "AccessLog": AwsElbLoadBalancerAccessLogOutputTypeDef,
        "ConnectionDraining": AwsElbLoadBalancerConnectionDrainingOutputTypeDef,
        "ConnectionSettings": AwsElbLoadBalancerConnectionSettingsOutputTypeDef,
        "CrossZoneLoadBalancing": AwsElbLoadBalancerCrossZoneLoadBalancingOutputTypeDef,
        "AdditionalAttributes": List[AwsElbLoadBalancerAdditionalAttributeOutputTypeDef],
    },
)

AwsElbLoadBalancerAttributesTypeDef = TypedDict(
    "AwsElbLoadBalancerAttributesTypeDef",
    {
        "AccessLog": AwsElbLoadBalancerAccessLogTypeDef,
        "ConnectionDraining": AwsElbLoadBalancerConnectionDrainingTypeDef,
        "ConnectionSettings": AwsElbLoadBalancerConnectionSettingsTypeDef,
        "CrossZoneLoadBalancing": AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef,
        "AdditionalAttributes": Sequence[AwsElbLoadBalancerAdditionalAttributeTypeDef],
    },
    total=False,
)

AwsElbLoadBalancerListenerDescriptionOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionOutputTypeDef",
    {
        "Listener": AwsElbLoadBalancerListenerOutputTypeDef,
        "PolicyNames": List[str],
    },
)

AwsElbLoadBalancerListenerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    {
        "Listener": AwsElbLoadBalancerListenerTypeDef,
        "PolicyNames": Sequence[str],
    },
    total=False,
)

AwsElbv2LoadBalancerDetailsOutputTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsOutputTypeDef",
    {
        "AvailabilityZones": List[AvailabilityZoneOutputTypeDef],
        "CanonicalHostedZoneId": str,
        "CreatedTime": str,
        "DNSName": str,
        "IpAddressType": str,
        "Scheme": str,
        "SecurityGroups": List[str],
        "State": LoadBalancerStateOutputTypeDef,
        "Type": str,
        "VpcId": str,
        "LoadBalancerAttributes": List[AwsElbv2LoadBalancerAttributeOutputTypeDef],
    },
)

AwsElbv2LoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": Sequence[AvailabilityZoneTypeDef],
        "CanonicalHostedZoneId": str,
        "CreatedTime": str,
        "DNSName": str,
        "IpAddressType": str,
        "Scheme": str,
        "SecurityGroups": Sequence[str],
        "State": LoadBalancerStateTypeDef,
        "Type": str,
        "VpcId": str,
        "LoadBalancerAttributes": Sequence[AwsElbv2LoadBalancerAttributeTypeDef],
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesKubernetesDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsOutputTypeDef",
    {
        "AuditLogs": AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsOutputTypeDef,
    },
)

AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef",
    {
        "AuditLogs": AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef,
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsOutputTypeDef",
    {
        "EbsVolumes": AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsOutputTypeDef,
    },
)

AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef",
    {
        "EbsVolumes": AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef,
    },
    total=False,
)

AwsIamAccessKeySessionContextOutputTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextOutputTypeDef",
    {
        "Attributes": AwsIamAccessKeySessionContextAttributesOutputTypeDef,
        "SessionIssuer": AwsIamAccessKeySessionContextSessionIssuerOutputTypeDef,
    },
)

AwsIamAccessKeySessionContextTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextTypeDef",
    {
        "Attributes": AwsIamAccessKeySessionContextAttributesTypeDef,
        "SessionIssuer": AwsIamAccessKeySessionContextSessionIssuerTypeDef,
    },
    total=False,
)

AwsIamGroupDetailsOutputTypeDef = TypedDict(
    "AwsIamGroupDetailsOutputTypeDef",
    {
        "AttachedManagedPolicies": List[AwsIamAttachedManagedPolicyOutputTypeDef],
        "CreateDate": str,
        "GroupId": str,
        "GroupName": str,
        "GroupPolicyList": List[AwsIamGroupPolicyOutputTypeDef],
        "Path": str,
    },
)

AwsIamGroupDetailsTypeDef = TypedDict(
    "AwsIamGroupDetailsTypeDef",
    {
        "AttachedManagedPolicies": Sequence[AwsIamAttachedManagedPolicyTypeDef],
        "CreateDate": str,
        "GroupId": str,
        "GroupName": str,
        "GroupPolicyList": Sequence[AwsIamGroupPolicyTypeDef],
        "Path": str,
    },
    total=False,
)

AwsIamInstanceProfileOutputTypeDef = TypedDict(
    "AwsIamInstanceProfileOutputTypeDef",
    {
        "Arn": str,
        "CreateDate": str,
        "InstanceProfileId": str,
        "InstanceProfileName": str,
        "Path": str,
        "Roles": List[AwsIamInstanceProfileRoleOutputTypeDef],
    },
)

AwsIamInstanceProfileTypeDef = TypedDict(
    "AwsIamInstanceProfileTypeDef",
    {
        "Arn": str,
        "CreateDate": str,
        "InstanceProfileId": str,
        "InstanceProfileName": str,
        "Path": str,
        "Roles": Sequence[AwsIamInstanceProfileRoleTypeDef],
    },
    total=False,
)

AwsIamPolicyDetailsOutputTypeDef = TypedDict(
    "AwsIamPolicyDetailsOutputTypeDef",
    {
        "AttachmentCount": int,
        "CreateDate": str,
        "DefaultVersionId": str,
        "Description": str,
        "IsAttachable": bool,
        "Path": str,
        "PermissionsBoundaryUsageCount": int,
        "PolicyId": str,
        "PolicyName": str,
        "PolicyVersionList": List[AwsIamPolicyVersionOutputTypeDef],
        "UpdateDate": str,
    },
)

AwsIamPolicyDetailsTypeDef = TypedDict(
    "AwsIamPolicyDetailsTypeDef",
    {
        "AttachmentCount": int,
        "CreateDate": str,
        "DefaultVersionId": str,
        "Description": str,
        "IsAttachable": bool,
        "Path": str,
        "PermissionsBoundaryUsageCount": int,
        "PolicyId": str,
        "PolicyName": str,
        "PolicyVersionList": Sequence[AwsIamPolicyVersionTypeDef],
        "UpdateDate": str,
    },
    total=False,
)

AwsIamUserDetailsOutputTypeDef = TypedDict(
    "AwsIamUserDetailsOutputTypeDef",
    {
        "AttachedManagedPolicies": List[AwsIamAttachedManagedPolicyOutputTypeDef],
        "CreateDate": str,
        "GroupList": List[str],
        "Path": str,
        "PermissionsBoundary": AwsIamPermissionsBoundaryOutputTypeDef,
        "UserId": str,
        "UserName": str,
        "UserPolicyList": List[AwsIamUserPolicyOutputTypeDef],
    },
)

AwsIamUserDetailsTypeDef = TypedDict(
    "AwsIamUserDetailsTypeDef",
    {
        "AttachedManagedPolicies": Sequence[AwsIamAttachedManagedPolicyTypeDef],
        "CreateDate": str,
        "GroupList": Sequence[str],
        "Path": str,
        "PermissionsBoundary": AwsIamPermissionsBoundaryTypeDef,
        "UserId": str,
        "UserName": str,
        "UserPolicyList": Sequence[AwsIamUserPolicyTypeDef],
    },
    total=False,
)

AwsKinesisStreamDetailsOutputTypeDef = TypedDict(
    "AwsKinesisStreamDetailsOutputTypeDef",
    {
        "Name": str,
        "Arn": str,
        "StreamEncryption": AwsKinesisStreamStreamEncryptionDetailsOutputTypeDef,
        "ShardCount": int,
        "RetentionPeriodHours": int,
    },
)

AwsKinesisStreamDetailsTypeDef = TypedDict(
    "AwsKinesisStreamDetailsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "StreamEncryption": AwsKinesisStreamStreamEncryptionDetailsTypeDef,
        "ShardCount": int,
        "RetentionPeriodHours": int,
    },
    total=False,
)

AwsLambdaFunctionEnvironmentOutputTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentOutputTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": AwsLambdaFunctionEnvironmentErrorOutputTypeDef,
    },
)

AwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentTypeDef",
    {
        "Variables": Mapping[str, str],
        "Error": AwsLambdaFunctionEnvironmentErrorTypeDef,
    },
    total=False,
)

AwsNetworkFirewallFirewallDetailsOutputTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallDetailsOutputTypeDef",
    {
        "DeleteProtection": bool,
        "Description": str,
        "FirewallArn": str,
        "FirewallId": str,
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "FirewallPolicyChangeProtection": bool,
        "SubnetChangeProtection": bool,
        "SubnetMappings": List[AwsNetworkFirewallFirewallSubnetMappingsDetailsOutputTypeDef],
        "VpcId": str,
    },
)

AwsNetworkFirewallFirewallDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    {
        "DeleteProtection": bool,
        "Description": str,
        "FirewallArn": str,
        "FirewallId": str,
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "FirewallPolicyChangeProtection": bool,
        "SubnetChangeProtection": bool,
        "SubnetMappings": Sequence[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef],
        "VpcId": str,
    },
    total=False,
)

AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsOutputTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "MasterUserOptions": AwsOpenSearchServiceDomainMasterUserOptionsDetailsOutputTypeDef,
    },
)

AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "MasterUserOptions": AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef,
    },
    total=False,
)

AwsOpenSearchServiceDomainClusterConfigDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigDetailsOutputTypeDef",
    {
        "InstanceCount": int,
        "WarmEnabled": bool,
        "WarmCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessConfig": (
            AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsOutputTypeDef
        ),
        "DedicatedMasterCount": int,
        "InstanceType": str,
        "WarmType": str,
        "ZoneAwarenessEnabled": bool,
        "DedicatedMasterType": str,
    },
)

AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    {
        "InstanceCount": int,
        "WarmEnabled": bool,
        "WarmCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessConfig": (
            AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef
        ),
        "DedicatedMasterCount": int,
        "InstanceType": str,
        "WarmType": str,
        "ZoneAwarenessEnabled": bool,
        "DedicatedMasterType": str,
    },
    total=False,
)

AwsOpenSearchServiceDomainLogPublishingOptionsDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsOutputTypeDef",
    {
        "IndexSlowLogs": AwsOpenSearchServiceDomainLogPublishingOptionOutputTypeDef,
        "SearchSlowLogs": AwsOpenSearchServiceDomainLogPublishingOptionOutputTypeDef,
        "AuditLogs": AwsOpenSearchServiceDomainLogPublishingOptionOutputTypeDef,
    },
)

AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    {
        "IndexSlowLogs": AwsOpenSearchServiceDomainLogPublishingOptionTypeDef,
        "SearchSlowLogs": AwsOpenSearchServiceDomainLogPublishingOptionTypeDef,
        "AuditLogs": AwsOpenSearchServiceDomainLogPublishingOptionTypeDef,
    },
    total=False,
)

AwsRdsDbClusterDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbClusterDetailsOutputTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DatabaseName": str,
        "Status": str,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "CustomEndpoints": List[str],
        "MultiAz": bool,
        "Engine": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReadReplicaIdentifiers": List[str],
        "VpcSecurityGroups": List[AwsRdsDbInstanceVpcSecurityGroupOutputTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "AssociatedRoles": List[AwsRdsDbClusterAssociatedRoleOutputTypeDef],
        "ClusterCreateTime": str,
        "EnabledCloudWatchLogsExports": List[str],
        "EngineMode": str,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamStatus": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
        "DomainMemberships": List[AwsRdsDbDomainMembershipOutputTypeDef],
        "DbClusterParameterGroup": str,
        "DbSubnetGroup": str,
        "DbClusterOptionGroupMemberships": List[AwsRdsDbClusterOptionGroupMembershipOutputTypeDef],
        "DbClusterIdentifier": str,
        "DbClusterMembers": List[AwsRdsDbClusterMemberOutputTypeDef],
        "IamDatabaseAuthenticationEnabled": bool,
    },
)

AwsRdsDbClusterDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterDetailsTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": Sequence[str],
        "BackupRetentionPeriod": int,
        "DatabaseName": str,
        "Status": str,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "CustomEndpoints": Sequence[str],
        "MultiAz": bool,
        "Engine": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReadReplicaIdentifiers": Sequence[str],
        "VpcSecurityGroups": Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "AssociatedRoles": Sequence[AwsRdsDbClusterAssociatedRoleTypeDef],
        "ClusterCreateTime": str,
        "EnabledCloudWatchLogsExports": Sequence[str],
        "EngineMode": str,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamStatus": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
        "DomainMemberships": Sequence[AwsRdsDbDomainMembershipTypeDef],
        "DbClusterParameterGroup": str,
        "DbSubnetGroup": str,
        "DbClusterOptionGroupMemberships": Sequence[AwsRdsDbClusterOptionGroupMembershipTypeDef],
        "DbClusterIdentifier": str,
        "DbClusterMembers": Sequence[AwsRdsDbClusterMemberTypeDef],
        "IamDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

AwsRdsDbClusterSnapshotDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDetailsOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "SnapshotCreateTime": str,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": str,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterIdentifier": str,
        "DbClusterSnapshotIdentifier": str,
        "IamDatabaseAuthenticationEnabled": bool,
        "DbClusterSnapshotAttributes": List[
            AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef
        ],
    },
)

AwsRdsDbClusterSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "SnapshotCreateTime": str,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": str,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterIdentifier": str,
        "DbClusterSnapshotIdentifier": str,
        "IamDatabaseAuthenticationEnabled": bool,
        "DbClusterSnapshotAttributes": Sequence[
            AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef
        ],
    },
    total=False,
)

AwsRdsDbSnapshotDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbSnapshotDetailsOutputTypeDef",
    {
        "DbSnapshotIdentifier": str,
        "DbInstanceIdentifier": str,
        "SnapshotCreateTime": str,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": str,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDbSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "Timezone": str,
        "IamDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List[AwsRdsDbProcessorFeatureOutputTypeDef],
        "DbiResourceId": str,
    },
)

AwsRdsDbSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbSnapshotDetailsTypeDef",
    {
        "DbSnapshotIdentifier": str,
        "DbInstanceIdentifier": str,
        "SnapshotCreateTime": str,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": str,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDbSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "Timezone": str,
        "IamDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": Sequence[AwsRdsDbProcessorFeatureTypeDef],
        "DbiResourceId": str,
    },
    total=False,
)

AwsRdsDbPendingModifiedValuesOutputTypeDef = TypedDict(
    "AwsRdsDbPendingModifiedValuesOutputTypeDef",
    {
        "DbInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DbInstanceIdentifier": str,
        "StorageType": str,
        "CaCertificateIdentifier": str,
        "DbSubnetGroupName": str,
        "PendingCloudWatchLogsExports": AwsRdsPendingCloudWatchLogsExportsOutputTypeDef,
        "ProcessorFeatures": List[AwsRdsDbProcessorFeatureOutputTypeDef],
    },
)

AwsRdsDbPendingModifiedValuesTypeDef = TypedDict(
    "AwsRdsDbPendingModifiedValuesTypeDef",
    {
        "DbInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DbInstanceIdentifier": str,
        "StorageType": str,
        "CaCertificateIdentifier": str,
        "DbSubnetGroupName": str,
        "PendingCloudWatchLogsExports": AwsRdsPendingCloudWatchLogsExportsTypeDef,
        "ProcessorFeatures": Sequence[AwsRdsDbProcessorFeatureTypeDef],
    },
    total=False,
)

AwsRdsDbSecurityGroupDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupDetailsOutputTypeDef",
    {
        "DbSecurityGroupArn": str,
        "DbSecurityGroupDescription": str,
        "DbSecurityGroupName": str,
        "Ec2SecurityGroups": List[AwsRdsDbSecurityGroupEc2SecurityGroupOutputTypeDef],
        "IpRanges": List[AwsRdsDbSecurityGroupIpRangeOutputTypeDef],
        "OwnerId": str,
        "VpcId": str,
    },
)

AwsRdsDbSecurityGroupDetailsTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupDetailsTypeDef",
    {
        "DbSecurityGroupArn": str,
        "DbSecurityGroupDescription": str,
        "DbSecurityGroupName": str,
        "Ec2SecurityGroups": Sequence[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef],
        "IpRanges": Sequence[AwsRdsDbSecurityGroupIpRangeTypeDef],
        "OwnerId": str,
        "VpcId": str,
    },
    total=False,
)

AwsRdsDbSubnetGroupSubnetOutputTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetOutputTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": AwsRdsDbSubnetGroupSubnetAvailabilityZoneOutputTypeDef,
        "SubnetStatus": str,
    },
)

AwsRdsDbSubnetGroupSubnetTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

AwsRedshiftClusterClusterParameterGroupOutputTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterGroupOutputTypeDef",
    {
        "ClusterParameterStatusList": List[AwsRedshiftClusterClusterParameterStatusOutputTypeDef],
        "ParameterApplyStatus": str,
        "ParameterGroupName": str,
    },
)

AwsRedshiftClusterClusterParameterGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    {
        "ClusterParameterStatusList": Sequence[AwsRedshiftClusterClusterParameterStatusTypeDef],
        "ParameterApplyStatus": str,
        "ParameterGroupName": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsOutputTypeDef",
    {
        "Prefix": str,
        "Tag": AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsOutputTypeDef,
        "Type": str,
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    {
        "Prefix": str,
        "Tag": AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef,
        "Type": str,
    },
    total=False,
)

AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef",
    {
        "FilterRules": List[AwsS3BucketNotificationConfigurationS3KeyFilterRuleOutputTypeDef],
    },
)

AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    {
        "FilterRules": Sequence[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef],
    },
    total=False,
)

AwsS3BucketObjectLockConfigurationRuleDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationRuleDetailsOutputTypeDef",
    {
        "DefaultRetention": (
            AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsOutputTypeDef
        ),
    },
)

AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef",
    {
        "DefaultRetention": AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef,
    },
    total=False,
)

AwsS3BucketServerSideEncryptionRuleOutputTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionRuleOutputTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": AwsS3BucketServerSideEncryptionByDefaultOutputTypeDef,
    },
)

AwsS3BucketServerSideEncryptionRuleTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": AwsS3BucketServerSideEncryptionByDefaultTypeDef,
    },
    total=False,
)

AwsS3BucketWebsiteConfigurationRoutingRuleOutputTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleOutputTypeDef",
    {
        "Condition": AwsS3BucketWebsiteConfigurationRoutingRuleConditionOutputTypeDef,
        "Redirect": AwsS3BucketWebsiteConfigurationRoutingRuleRedirectOutputTypeDef,
    },
)

AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    {
        "Condition": AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef,
        "Redirect": AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef,
    },
    total=False,
)

AwsSageMakerNotebookInstanceDetailsOutputTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceDetailsOutputTypeDef",
    {
        "AcceleratorTypes": List[str],
        "AdditionalCodeRepositories": List[str],
        "DefaultCodeRepository": str,
        "DirectInternetAccess": str,
        "FailureReason": str,
        "InstanceMetadataServiceConfiguration": (
            AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsOutputTypeDef
        ),
        "InstanceType": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "NotebookInstanceArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": str,
        "PlatformIdentifier": str,
        "RoleArn": str,
        "RootAccess": str,
        "SecurityGroups": List[str],
        "SubnetId": str,
        "Url": str,
        "VolumeSizeInGB": int,
    },
)

AwsSageMakerNotebookInstanceDetailsTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceDetailsTypeDef",
    {
        "AcceleratorTypes": Sequence[str],
        "AdditionalCodeRepositories": Sequence[str],
        "DefaultCodeRepository": str,
        "DirectInternetAccess": str,
        "FailureReason": str,
        "InstanceMetadataServiceConfiguration": (
            AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef
        ),
        "InstanceType": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "NotebookInstanceArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": str,
        "PlatformIdentifier": str,
        "RoleArn": str,
        "RootAccess": str,
        "SecurityGroups": Sequence[str],
        "SubnetId": str,
        "Url": str,
        "VolumeSizeInGB": int,
    },
    total=False,
)

AwsSecretsManagerSecretDetailsOutputTypeDef = TypedDict(
    "AwsSecretsManagerSecretDetailsOutputTypeDef",
    {
        "RotationRules": AwsSecretsManagerSecretRotationRulesOutputTypeDef,
        "RotationOccurredWithinFrequency": bool,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaArn": str,
        "Deleted": bool,
        "Name": str,
        "Description": str,
    },
)

AwsSecretsManagerSecretDetailsTypeDef = TypedDict(
    "AwsSecretsManagerSecretDetailsTypeDef",
    {
        "RotationRules": AwsSecretsManagerSecretRotationRulesTypeDef,
        "RotationOccurredWithinFrequency": bool,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaArn": str,
        "Deleted": bool,
        "Name": str,
        "Description": str,
    },
    total=False,
)

BatchUpdateFindingsUnprocessedFindingTypeDef = TypedDict(
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierOutputTypeDef,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

_RequiredBatchUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpdateFindingsRequestRequestTypeDef",
    {
        "FindingIdentifiers": Sequence[AwsSecurityFindingIdentifierTypeDef],
    },
)
_OptionalBatchUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpdateFindingsRequestRequestTypeDef",
    {
        "Note": NoteUpdateTypeDef,
        "Severity": SeverityUpdateTypeDef,
        "VerificationState": VerificationStateType,
        "Confidence": int,
        "Criticality": int,
        "Types": Sequence[str],
        "UserDefinedFields": Mapping[str, str],
        "Workflow": WorkflowUpdateTypeDef,
        "RelatedFindings": Sequence[RelatedFindingTypeDef],
    },
    total=False,
)


class BatchUpdateFindingsRequestRequestTypeDef(
    _RequiredBatchUpdateFindingsRequestRequestTypeDef,
    _OptionalBatchUpdateFindingsRequestRequestTypeDef,
):
    pass


_RequiredGetFindingHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetFindingHistoryRequestRequestTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierTypeDef,
    },
)
_OptionalGetFindingHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetFindingHistoryRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetFindingHistoryRequestRequestTypeDef(
    _RequiredGetFindingHistoryRequestRequestTypeDef, _OptionalGetFindingHistoryRequestRequestTypeDef
):
    pass


AwsSnsTopicDetailsOutputTypeDef = TypedDict(
    "AwsSnsTopicDetailsOutputTypeDef",
    {
        "KmsMasterKeyId": str,
        "Subscription": List[AwsSnsTopicSubscriptionOutputTypeDef],
        "TopicName": str,
        "Owner": str,
        "SqsSuccessFeedbackRoleArn": str,
        "SqsFailureFeedbackRoleArn": str,
        "ApplicationSuccessFeedbackRoleArn": str,
        "FirehoseSuccessFeedbackRoleArn": str,
        "FirehoseFailureFeedbackRoleArn": str,
        "HttpSuccessFeedbackRoleArn": str,
        "HttpFailureFeedbackRoleArn": str,
    },
)

AwsSnsTopicDetailsTypeDef = TypedDict(
    "AwsSnsTopicDetailsTypeDef",
    {
        "KmsMasterKeyId": str,
        "Subscription": Sequence[AwsSnsTopicSubscriptionTypeDef],
        "TopicName": str,
        "Owner": str,
        "SqsSuccessFeedbackRoleArn": str,
        "SqsFailureFeedbackRoleArn": str,
        "ApplicationSuccessFeedbackRoleArn": str,
        "FirehoseSuccessFeedbackRoleArn": str,
        "FirehoseFailureFeedbackRoleArn": str,
        "HttpSuccessFeedbackRoleArn": str,
        "HttpFailureFeedbackRoleArn": str,
    },
    total=False,
)

AwsSsmPatchOutputTypeDef = TypedDict(
    "AwsSsmPatchOutputTypeDef",
    {
        "ComplianceSummary": AwsSsmComplianceSummaryOutputTypeDef,
    },
)

AwsSsmPatchTypeDef = TypedDict(
    "AwsSsmPatchTypeDef",
    {
        "ComplianceSummary": AwsSsmComplianceSummaryTypeDef,
    },
    total=False,
)

AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsOutputTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsOutputTypeDef",
    {
        "CloudWatchLogsLogGroup": AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsOutputTypeDef,
    },
)

AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef",
    {
        "CloudWatchLogsLogGroup": AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef,
    },
    total=False,
)

AwsWafRateBasedRuleDetailsOutputTypeDef = TypedDict(
    "AwsWafRateBasedRuleDetailsOutputTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "RateKey": str,
        "RateLimit": int,
        "RuleId": str,
        "MatchPredicates": List[AwsWafRateBasedRuleMatchPredicateOutputTypeDef],
    },
)

AwsWafRateBasedRuleDetailsTypeDef = TypedDict(
    "AwsWafRateBasedRuleDetailsTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "RateKey": str,
        "RateLimit": int,
        "RuleId": str,
        "MatchPredicates": Sequence[AwsWafRateBasedRuleMatchPredicateTypeDef],
    },
    total=False,
)

AwsWafRegionalRateBasedRuleDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleDetailsOutputTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "RateKey": str,
        "RateLimit": int,
        "RuleId": str,
        "MatchPredicates": List[AwsWafRegionalRateBasedRuleMatchPredicateOutputTypeDef],
    },
)

AwsWafRegionalRateBasedRuleDetailsTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "RateKey": str,
        "RateLimit": int,
        "RuleId": str,
        "MatchPredicates": Sequence[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef],
    },
    total=False,
)

AwsWafRegionalRuleDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRuleDetailsOutputTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "PredicateList": List[AwsWafRegionalRulePredicateListDetailsOutputTypeDef],
        "RuleId": str,
    },
)

AwsWafRegionalRuleDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleDetailsTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "PredicateList": Sequence[AwsWafRegionalRulePredicateListDetailsTypeDef],
        "RuleId": str,
    },
    total=False,
)

AwsWafRegionalRuleGroupRulesDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesDetailsOutputTypeDef",
    {
        "Action": AwsWafRegionalRuleGroupRulesActionDetailsOutputTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
)

AwsWafRegionalRuleGroupRulesDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesDetailsTypeDef",
    {
        "Action": AwsWafRegionalRuleGroupRulesActionDetailsTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)

AwsWafRegionalWebAclRulesListDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListDetailsOutputTypeDef",
    {
        "Action": AwsWafRegionalWebAclRulesListActionDetailsOutputTypeDef,
        "OverrideAction": AwsWafRegionalWebAclRulesListOverrideActionDetailsOutputTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
)

AwsWafRegionalWebAclRulesListDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListDetailsTypeDef",
    {
        "Action": AwsWafRegionalWebAclRulesListActionDetailsTypeDef,
        "OverrideAction": AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)

AwsWafRuleDetailsOutputTypeDef = TypedDict(
    "AwsWafRuleDetailsOutputTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "PredicateList": List[AwsWafRulePredicateListDetailsOutputTypeDef],
        "RuleId": str,
    },
)

AwsWafRuleDetailsTypeDef = TypedDict(
    "AwsWafRuleDetailsTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "PredicateList": Sequence[AwsWafRulePredicateListDetailsTypeDef],
        "RuleId": str,
    },
    total=False,
)

AwsWafRuleGroupRulesDetailsOutputTypeDef = TypedDict(
    "AwsWafRuleGroupRulesDetailsOutputTypeDef",
    {
        "Action": AwsWafRuleGroupRulesActionDetailsOutputTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
)

AwsWafRuleGroupRulesDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupRulesDetailsTypeDef",
    {
        "Action": AwsWafRuleGroupRulesActionDetailsTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)

AwsWafWebAclRuleOutputTypeDef = TypedDict(
    "AwsWafWebAclRuleOutputTypeDef",
    {
        "Action": WafActionOutputTypeDef,
        "ExcludedRules": List[WafExcludedRuleOutputTypeDef],
        "OverrideAction": WafOverrideActionOutputTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
)

AwsWafWebAclRuleTypeDef = TypedDict(
    "AwsWafWebAclRuleTypeDef",
    {
        "Action": WafActionTypeDef,
        "ExcludedRules": Sequence[WafExcludedRuleTypeDef],
        "OverrideAction": WafOverrideActionTypeDef,
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)

AwsWafv2CustomRequestHandlingDetailsOutputTypeDef = TypedDict(
    "AwsWafv2CustomRequestHandlingDetailsOutputTypeDef",
    {
        "InsertHeaders": List[AwsWafv2CustomHttpHeaderOutputTypeDef],
    },
)

AwsWafv2CustomResponseDetailsOutputTypeDef = TypedDict(
    "AwsWafv2CustomResponseDetailsOutputTypeDef",
    {
        "CustomResponseBodyKey": str,
        "ResponseCode": int,
        "ResponseHeaders": List[AwsWafv2CustomHttpHeaderOutputTypeDef],
    },
)

AwsWafv2CustomRequestHandlingDetailsTypeDef = TypedDict(
    "AwsWafv2CustomRequestHandlingDetailsTypeDef",
    {
        "InsertHeaders": Sequence[AwsWafv2CustomHttpHeaderTypeDef],
    },
    total=False,
)

AwsWafv2CustomResponseDetailsTypeDef = TypedDict(
    "AwsWafv2CustomResponseDetailsTypeDef",
    {
        "CustomResponseBodyKey": str,
        "ResponseCode": int,
        "ResponseHeaders": Sequence[AwsWafv2CustomHttpHeaderTypeDef],
    },
    total=False,
)

AwsWafv2WebAclCaptchaConfigDetailsOutputTypeDef = TypedDict(
    "AwsWafv2WebAclCaptchaConfigDetailsOutputTypeDef",
    {
        "ImmunityTimeProperty": AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsOutputTypeDef,
    },
)

AwsWafv2WebAclCaptchaConfigDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclCaptchaConfigDetailsTypeDef",
    {
        "ImmunityTimeProperty": AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef,
    },
    total=False,
)

CreateActionTargetResponseTypeDef = TypedDict(
    "CreateActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAutomationRuleResponseTypeDef = TypedDict(
    "CreateAutomationRuleResponseTypeDef",
    {
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFindingAggregatorResponseTypeDef = TypedDict(
    "CreateFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateInsightResponseTypeDef = TypedDict(
    "CreateInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteActionTargetResponseTypeDef = TypedDict(
    "DeleteActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteInsightResponseTypeDef = TypedDict(
    "DeleteInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeActionTargetsResponseTypeDef = TypedDict(
    "DescribeActionTargetsResponseTypeDef",
    {
        "ActionTargets": List[ActionTargetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeHubResponseTypeDef = TypedDict(
    "DescribeHubResponseTypeDef",
    {
        "HubArn": str,
        "SubscribedAt": str,
        "AutoEnableControls": bool,
        "ControlFindingGenerator": ControlFindingGeneratorType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "AutoEnableStandards": AutoEnableStandardsType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EnableImportFindingsForProductResponseTypeDef = TypedDict(
    "EnableImportFindingsForProductResponseTypeDef",
    {
        "ProductSubscriptionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetFindingAggregatorResponseTypeDef = TypedDict(
    "GetFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "InvitationsCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAutomationRulesResponseTypeDef = TypedDict(
    "ListAutomationRulesResponseTypeDef",
    {
        "AutomationRulesMetadata": List[AutomationRulesMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ListEnabledProductsForImportResponseTypeDef",
    {
        "ProductSubscriptions": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "AdminAccounts": List[AdminAccountTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFindingAggregatorResponseTypeDef = TypedDict(
    "UpdateFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchDeleteAutomationRulesResponseTypeDef = TypedDict(
    "BatchDeleteAutomationRulesResponseTypeDef",
    {
        "ProcessedAutomationRules": List[str],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchUpdateAutomationRulesResponseTypeDef = TypedDict(
    "BatchUpdateAutomationRulesResponseTypeDef",
    {
        "ProcessedAutomationRules": List[str],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchEnableStandardsRequestRequestTypeDef = TypedDict(
    "BatchEnableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionRequests": Sequence[StandardsSubscriptionRequestTypeDef],
    },
)

BatchGetSecurityControlsResponseTypeDef = TypedDict(
    "BatchGetSecurityControlsResponseTypeDef",
    {
        "SecurityControls": List[SecurityControlTypeDef],
        "UnprocessedIds": List[UnprocessedSecurityControlTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchGetStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "BatchGetStandardsControlAssociationsRequestRequestTypeDef",
    {
        "StandardsControlAssociationIds": Sequence[StandardsControlAssociationIdTypeDef],
    },
)

BatchImportFindingsResponseTypeDef = TypedDict(
    "BatchImportFindingsResponseTypeDef",
    {
        "FailedCount": int,
        "SuccessCount": int,
        "FailedFindings": List[ImportFindingsErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchUpdateStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "BatchUpdateStandardsControlAssociationsRequestRequestTypeDef",
    {
        "StandardsControlAssociationUpdates": Sequence[StandardsControlAssociationUpdateTypeDef],
    },
)

ComplianceOutputTypeDef = TypedDict(
    "ComplianceOutputTypeDef",
    {
        "Status": ComplianceStatusType,
        "RelatedRequirements": List[str],
        "StatusReasons": List[StatusReasonOutputTypeDef],
        "SecurityControlId": str,
        "AssociatedStandards": List[AssociatedStandardOutputTypeDef],
    },
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "Status": ComplianceStatusType,
        "RelatedRequirements": Sequence[str],
        "StatusReasons": Sequence[StatusReasonTypeDef],
        "SecurityControlId": str,
        "AssociatedStandards": Sequence[AssociatedStandardTypeDef],
    },
    total=False,
)

ContainerDetailsOutputTypeDef = TypedDict(
    "ContainerDetailsOutputTypeDef",
    {
        "ContainerRuntime": str,
        "Name": str,
        "ImageId": str,
        "ImageName": str,
        "LaunchedAt": str,
        "VolumeMounts": List[VolumeMountOutputTypeDef],
        "Privileged": bool,
    },
)

ContainerDetailsTypeDef = TypedDict(
    "ContainerDetailsTypeDef",
    {
        "ContainerRuntime": str,
        "Name": str,
        "ImageId": str,
        "ImageName": str,
        "LaunchedAt": str,
        "VolumeMounts": Sequence[VolumeMountTypeDef],
        "Privileged": bool,
    },
    total=False,
)

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DateFilterOutputTypeDef = TypedDict(
    "DateFilterOutputTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": DateRangeOutputTypeDef,
    },
)

DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": DateRangeTypeDef,
    },
    total=False,
)

DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef = TypedDict(
    "DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef",
    {
        "ActionTargetArns": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

DescribeProductsRequestDescribeProductsPaginateTypeDef = TypedDict(
    "DescribeProductsRequestDescribeProductsPaginateTypeDef",
    {
        "ProductArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredDescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef = TypedDict(
    "_RequiredDescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef",
    {
        "StandardsSubscriptionArn": str,
    },
)
_OptionalDescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef = TypedDict(
    "_OptionalDescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef(
    _RequiredDescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef,
    _OptionalDescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef,
):
    pass


DescribeStandardsRequestDescribeStandardsPaginateTypeDef = TypedDict(
    "DescribeStandardsRequestDescribeStandardsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef = TypedDict(
    "GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef",
    {
        "StandardsSubscriptionArns": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredGetFindingHistoryRequestGetFindingHistoryPaginateTypeDef = TypedDict(
    "_RequiredGetFindingHistoryRequestGetFindingHistoryPaginateTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierTypeDef,
    },
)
_OptionalGetFindingHistoryRequestGetFindingHistoryPaginateTypeDef = TypedDict(
    "_OptionalGetFindingHistoryRequestGetFindingHistoryPaginateTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef(
    _RequiredGetFindingHistoryRequestGetFindingHistoryPaginateTypeDef,
    _OptionalGetFindingHistoryRequestGetFindingHistoryPaginateTypeDef,
):
    pass


GetInsightsRequestGetInsightsPaginateTypeDef = TypedDict(
    "GetInsightsRequestGetInsightsPaginateTypeDef",
    {
        "InsightArns": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef = TypedDict(
    "ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef = TypedDict(
    "ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListInvitationsRequestListInvitationsPaginateTypeDef = TypedDict(
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListMembersRequestListMembersPaginateTypeDef = TypedDict(
    "ListMembersRequestListMembersPaginateTypeDef",
    {
        "OnlyAssociated": bool,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef = TypedDict(
    "ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef",
    {
        "StandardsArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef = TypedDict(
    "_RequiredListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef",
    {
        "SecurityControlId": str,
    },
)
_OptionalListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef = TypedDict(
    "_OptionalListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef(
    _RequiredListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef,
    _OptionalListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef,
):
    pass


DescribeProductsResponseTypeDef = TypedDict(
    "DescribeProductsResponseTypeDef",
    {
        "Products": List[ProductTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStandardsControlsResponseTypeDef = TypedDict(
    "DescribeStandardsControlsResponseTypeDef",
    {
        "Controls": List[StandardsControlTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ThreatOutputTypeDef = TypedDict(
    "ThreatOutputTypeDef",
    {
        "Name": str,
        "Severity": str,
        "ItemCount": int,
        "FilePaths": List[FilePathsOutputTypeDef],
    },
)

ThreatTypeDef = TypedDict(
    "ThreatTypeDef",
    {
        "Name": str,
        "Severity": str,
        "ItemCount": int,
        "FilePaths": Sequence[FilePathsTypeDef],
    },
    total=False,
)

ListFindingAggregatorsResponseTypeDef = TypedDict(
    "ListFindingAggregatorsResponseTypeDef",
    {
        "FindingAggregators": List[FindingAggregatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FindingHistoryRecordTypeDef = TypedDict(
    "FindingHistoryRecordTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierOutputTypeDef,
        "UpdateTime": datetime,
        "FindingCreated": bool,
        "UpdateSource": FindingHistoryUpdateSourceTypeDef,
        "Updates": List[FindingHistoryUpdateTypeDef],
        "NextToken": str,
    },
)

FindingProviderFieldsOutputTypeDef = TypedDict(
    "FindingProviderFieldsOutputTypeDef",
    {
        "Confidence": int,
        "Criticality": int,
        "RelatedFindings": List[RelatedFindingOutputTypeDef],
        "Severity": FindingProviderSeverityOutputTypeDef,
        "Types": List[str],
    },
)

FindingProviderFieldsTypeDef = TypedDict(
    "FindingProviderFieldsTypeDef",
    {
        "Confidence": int,
        "Criticality": int,
        "RelatedFindings": Sequence[RelatedFindingTypeDef],
        "Severity": FindingProviderSeverityTypeDef,
        "Types": Sequence[str],
    },
    total=False,
)

GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "Administrator": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List[InvitationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List[MemberTypeDef],
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "Members": List[MemberTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

InsightResultsTypeDef = TypedDict(
    "InsightResultsTypeDef",
    {
        "InsightArn": str,
        "GroupByAttribute": str,
        "ResultValues": List[InsightResultValueTypeDef],
    },
)

ListSecurityControlDefinitionsResponseTypeDef = TypedDict(
    "ListSecurityControlDefinitionsResponseTypeDef",
    {
        "SecurityControlDefinitions": List[SecurityControlDefinitionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStandardsControlAssociationsResponseTypeDef = TypedDict(
    "ListStandardsControlAssociationsResponseTypeDef",
    {
        "StandardsControlAssociationSummaries": List[StandardsControlAssociationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetworkOutputTypeDef = TypedDict(
    "NetworkOutputTypeDef",
    {
        "Direction": NetworkDirectionType,
        "Protocol": str,
        "OpenPortRange": PortRangeOutputTypeDef,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
)

NetworkPathComponentDetailsOutputTypeDef = TypedDict(
    "NetworkPathComponentDetailsOutputTypeDef",
    {
        "Address": List[str],
        "PortRanges": List[PortRangeOutputTypeDef],
    },
)

NetworkPathComponentDetailsTypeDef = TypedDict(
    "NetworkPathComponentDetailsTypeDef",
    {
        "Address": Sequence[str],
        "PortRanges": Sequence[PortRangeTypeDef],
    },
    total=False,
)

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Direction": NetworkDirectionType,
        "Protocol": str,
        "OpenPortRange": PortRangeTypeDef,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

PageOutputTypeDef = TypedDict(
    "PageOutputTypeDef",
    {
        "PageNumber": int,
        "LineRange": RangeOutputTypeDef,
        "OffsetRange": RangeOutputTypeDef,
    },
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "PageNumber": int,
        "LineRange": RangeTypeDef,
        "OffsetRange": RangeTypeDef,
    },
    total=False,
)

RemediationOutputTypeDef = TypedDict(
    "RemediationOutputTypeDef",
    {
        "Recommendation": RecommendationOutputTypeDef,
    },
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "Recommendation": RecommendationTypeDef,
    },
    total=False,
)

RuleGroupSourceStatefulRulesDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesDetailsOutputTypeDef",
    {
        "Action": str,
        "Header": RuleGroupSourceStatefulRulesHeaderDetailsOutputTypeDef,
        "RuleOptions": List[RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef],
    },
)

RuleGroupSourceStatefulRulesDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    {
        "Action": str,
        "Header": RuleGroupSourceStatefulRulesHeaderDetailsTypeDef,
        "RuleOptions": Sequence[RuleGroupSourceStatefulRulesOptionsDetailsTypeDef],
    },
    total=False,
)

RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef",
    {
        "DestinationPorts": List[
            RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsOutputTypeDef
        ],
        "Destinations": List[RuleGroupSourceStatelessRuleMatchAttributesDestinationsOutputTypeDef],
        "Protocols": List[int],
        "SourcePorts": List[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsOutputTypeDef],
        "Sources": List[RuleGroupSourceStatelessRuleMatchAttributesSourcesOutputTypeDef],
        "TcpFlags": List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef],
    },
)

RuleGroupSourceStatelessRuleMatchAttributesTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    {
        "DestinationPorts": Sequence[
            RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef
        ],
        "Destinations": Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef],
        "Protocols": Sequence[int],
        "SourcePorts": Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef],
        "Sources": Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef],
        "TcpFlags": Sequence[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef],
    },
    total=False,
)

RuleGroupVariablesOutputTypeDef = TypedDict(
    "RuleGroupVariablesOutputTypeDef",
    {
        "IpSets": RuleGroupVariablesIpSetsDetailsOutputTypeDef,
        "PortSets": RuleGroupVariablesPortSetsDetailsOutputTypeDef,
    },
)

RuleGroupVariablesTypeDef = TypedDict(
    "RuleGroupVariablesTypeDef",
    {
        "IpSets": RuleGroupVariablesIpSetsDetailsTypeDef,
        "PortSets": RuleGroupVariablesPortSetsDetailsTypeDef,
    },
    total=False,
)

StandardTypeDef = TypedDict(
    "StandardTypeDef",
    {
        "StandardsArn": str,
        "Name": str,
        "Description": str,
        "EnabledByDefault": bool,
        "StandardsManagedBy": StandardsManagedByTypeDef,
    },
)

UnprocessedStandardsControlAssociationTypeDef = TypedDict(
    "UnprocessedStandardsControlAssociationTypeDef",
    {
        "StandardsControlAssociationId": StandardsControlAssociationIdOutputTypeDef,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": str,
    },
)

UnprocessedStandardsControlAssociationUpdateTypeDef = TypedDict(
    "UnprocessedStandardsControlAssociationUpdateTypeDef",
    {
        "StandardsControlAssociationUpdate": StandardsControlAssociationUpdateOutputTypeDef,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": str,
    },
)

StandardsSubscriptionTypeDef = TypedDict(
    "StandardsSubscriptionTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": StandardsStatusType,
        "StandardsStatusReason": StandardsStatusReasonTypeDef,
    },
)

StatelessCustomPublishMetricActionOutputTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionOutputTypeDef",
    {
        "Dimensions": List[StatelessCustomPublishMetricActionDimensionOutputTypeDef],
    },
)

StatelessCustomPublishMetricActionTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionTypeDef",
    {
        "Dimensions": Sequence[StatelessCustomPublishMetricActionDimensionTypeDef],
    },
    total=False,
)

AwsApiCallActionOutputTypeDef = TypedDict(
    "AwsApiCallActionOutputTypeDef",
    {
        "Api": str,
        "ServiceName": str,
        "CallerType": str,
        "RemoteIpDetails": ActionRemoteIpDetailsOutputTypeDef,
        "DomainDetails": AwsApiCallActionDomainDetailsOutputTypeDef,
        "AffectedResources": Dict[str, str],
        "FirstSeen": str,
        "LastSeen": str,
    },
)

NetworkConnectionActionOutputTypeDef = TypedDict(
    "NetworkConnectionActionOutputTypeDef",
    {
        "ConnectionDirection": str,
        "RemoteIpDetails": ActionRemoteIpDetailsOutputTypeDef,
        "RemotePortDetails": ActionRemotePortDetailsOutputTypeDef,
        "LocalPortDetails": ActionLocalPortDetailsOutputTypeDef,
        "Protocol": str,
        "Blocked": bool,
    },
)

PortProbeDetailOutputTypeDef = TypedDict(
    "PortProbeDetailOutputTypeDef",
    {
        "LocalPortDetails": ActionLocalPortDetailsOutputTypeDef,
        "LocalIpDetails": ActionLocalIpDetailsOutputTypeDef,
        "RemoteIpDetails": ActionRemoteIpDetailsOutputTypeDef,
    },
)

AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": str,
        "ServiceName": str,
        "CallerType": str,
        "RemoteIpDetails": ActionRemoteIpDetailsTypeDef,
        "DomainDetails": AwsApiCallActionDomainDetailsTypeDef,
        "AffectedResources": Mapping[str, str],
        "FirstSeen": str,
        "LastSeen": str,
    },
    total=False,
)

NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "ConnectionDirection": str,
        "RemoteIpDetails": ActionRemoteIpDetailsTypeDef,
        "RemotePortDetails": ActionRemotePortDetailsTypeDef,
        "LocalPortDetails": ActionLocalPortDetailsTypeDef,
        "Protocol": str,
        "Blocked": bool,
    },
    total=False,
)

PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": ActionLocalPortDetailsTypeDef,
        "LocalIpDetails": ActionLocalIpDetailsTypeDef,
        "RemoteIpDetails": ActionRemoteIpDetailsTypeDef,
    },
    total=False,
)

VulnerabilityOutputTypeDef = TypedDict(
    "VulnerabilityOutputTypeDef",
    {
        "Id": str,
        "VulnerablePackages": List[SoftwarePackageOutputTypeDef],
        "Cvss": List[CvssOutputTypeDef],
        "RelatedVulnerabilities": List[str],
        "Vendor": VulnerabilityVendorOutputTypeDef,
        "ReferenceUrls": List[str],
        "FixAvailable": VulnerabilityFixAvailableType,
    },
)

_RequiredVulnerabilityTypeDef = TypedDict(
    "_RequiredVulnerabilityTypeDef",
    {
        "Id": str,
    },
)
_OptionalVulnerabilityTypeDef = TypedDict(
    "_OptionalVulnerabilityTypeDef",
    {
        "VulnerablePackages": Sequence[SoftwarePackageTypeDef],
        "Cvss": Sequence[CvssTypeDef],
        "RelatedVulnerabilities": Sequence[str],
        "Vendor": VulnerabilityVendorTypeDef,
        "ReferenceUrls": Sequence[str],
        "FixAvailable": VulnerabilityFixAvailableType,
    },
    total=False,
)


class VulnerabilityTypeDef(_RequiredVulnerabilityTypeDef, _OptionalVulnerabilityTypeDef):
    pass


AwsEc2RouteTableDetailsOutputTypeDef = TypedDict(
    "AwsEc2RouteTableDetailsOutputTypeDef",
    {
        "AssociationSet": List[AssociationSetDetailsOutputTypeDef],
        "OwnerId": str,
        "PropagatingVgwSet": List[PropagatingVgwSetDetailsOutputTypeDef],
        "RouteTableId": str,
        "RouteSet": List[RouteSetDetailsOutputTypeDef],
        "VpcId": str,
    },
)

AwsEc2RouteTableDetailsTypeDef = TypedDict(
    "AwsEc2RouteTableDetailsTypeDef",
    {
        "AssociationSet": Sequence[AssociationSetDetailsTypeDef],
        "OwnerId": str,
        "PropagatingVgwSet": Sequence[PropagatingVgwSetDetailsTypeDef],
        "RouteTableId": str,
        "RouteSet": Sequence[RouteSetDetailsTypeDef],
        "VpcId": str,
    },
    total=False,
)

AutomationRulesActionOutputTypeDef = TypedDict(
    "AutomationRulesActionOutputTypeDef",
    {
        "Type": Literal["FINDING_FIELDS_UPDATE"],
        "FindingFieldsUpdate": AutomationRulesFindingFieldsUpdateOutputTypeDef,
    },
)

AutomationRulesActionTypeDef = TypedDict(
    "AutomationRulesActionTypeDef",
    {
        "Type": Literal["FINDING_FIELDS_UPDATE"],
        "FindingFieldsUpdate": AutomationRulesFindingFieldsUpdateTypeDef,
    },
    total=False,
)

AwsAmazonMqBrokerDetailsOutputTypeDef = TypedDict(
    "AwsAmazonMqBrokerDetailsOutputTypeDef",
    {
        "AuthenticationStrategy": str,
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerName": str,
        "DeploymentMode": str,
        "EncryptionOptions": AwsAmazonMqBrokerEncryptionOptionsDetailsOutputTypeDef,
        "EngineType": str,
        "EngineVersion": str,
        "HostInstanceType": str,
        "BrokerId": str,
        "LdapServerMetadata": AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef,
        "Logs": AwsAmazonMqBrokerLogsDetailsOutputTypeDef,
        "MaintenanceWindowStartTime": (
            AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsOutputTypeDef
        ),
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "StorageType": str,
        "SubnetIds": List[str],
        "Users": List[AwsAmazonMqBrokerUsersDetailsOutputTypeDef],
    },
)

AwsAmazonMqBrokerDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerDetailsTypeDef",
    {
        "AuthenticationStrategy": str,
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerName": str,
        "DeploymentMode": str,
        "EncryptionOptions": AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef,
        "EngineType": str,
        "EngineVersion": str,
        "HostInstanceType": str,
        "BrokerId": str,
        "LdapServerMetadata": AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef,
        "Logs": AwsAmazonMqBrokerLogsDetailsTypeDef,
        "MaintenanceWindowStartTime": AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef,
        "PubliclyAccessible": bool,
        "SecurityGroups": Sequence[str],
        "StorageType": str,
        "SubnetIds": Sequence[str],
        "Users": Sequence[AwsAmazonMqBrokerUsersDetailsTypeDef],
    },
    total=False,
)

AwsAppSyncGraphQlApiDetailsOutputTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiDetailsOutputTypeDef",
    {
        "ApiId": str,
        "Id": str,
        "OpenIdConnectConfig": AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsOutputTypeDef,
        "Name": str,
        "LambdaAuthorizerConfig": AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsOutputTypeDef,
        "XrayEnabled": bool,
        "Arn": str,
        "UserPoolConfig": AwsAppSyncGraphQlApiUserPoolConfigDetailsOutputTypeDef,
        "AuthenticationType": str,
        "LogConfig": AwsAppSyncGraphQlApiLogConfigDetailsOutputTypeDef,
        "AdditionalAuthenticationProviders": List[
            AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsOutputTypeDef
        ],
        "WafWebAclArn": str,
    },
)

AwsAppSyncGraphQlApiDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiDetailsTypeDef",
    {
        "ApiId": str,
        "Id": str,
        "OpenIdConnectConfig": AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef,
        "Name": str,
        "LambdaAuthorizerConfig": AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef,
        "XrayEnabled": bool,
        "Arn": str,
        "UserPoolConfig": AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef,
        "AuthenticationType": str,
        "LogConfig": AwsAppSyncGraphQlApiLogConfigDetailsTypeDef,
        "AdditionalAuthenticationProviders": Sequence[
            AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef
        ],
        "WafWebAclArn": str,
    },
    total=False,
)

AwsAthenaWorkGroupConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationDetailsOutputTypeDef",
    {
        "ResultConfiguration": (
            AwsAthenaWorkGroupConfigurationResultConfigurationDetailsOutputTypeDef
        ),
    },
)

AwsAthenaWorkGroupConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationDetailsTypeDef",
    {
        "ResultConfiguration": AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef,
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef",
    {
        "InstancesDistribution": AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsOutputTypeDef,
        "LaunchTemplate": (
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef
        ),
    },
)

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    {
        "InstancesDistribution": (
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef
        ),
        "LaunchTemplate": (
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef
        ),
    },
    total=False,
)

AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BlockDeviceMappings": List[
            AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsOutputTypeDef
        ],
        "ClassicLinkVpcId": str,
        "ClassicLinkVpcSecurityGroups": List[str],
        "CreatedTime": str,
        "EbsOptimized": bool,
        "IamInstanceProfile": str,
        "ImageId": str,
        "InstanceMonitoring": (
            AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsOutputTypeDef
        ),
        "InstanceType": str,
        "KernelId": str,
        "KeyName": str,
        "LaunchConfigurationName": str,
        "PlacementTenancy": str,
        "RamdiskId": str,
        "SecurityGroups": List[str],
        "SpotPrice": str,
        "UserData": str,
        "MetadataOptions": AwsAutoScalingLaunchConfigurationMetadataOptionsOutputTypeDef,
    },
)

AwsAutoScalingLaunchConfigurationDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BlockDeviceMappings": Sequence[
            AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef
        ],
        "ClassicLinkVpcId": str,
        "ClassicLinkVpcSecurityGroups": Sequence[str],
        "CreatedTime": str,
        "EbsOptimized": bool,
        "IamInstanceProfile": str,
        "ImageId": str,
        "InstanceMonitoring": AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef,
        "InstanceType": str,
        "KernelId": str,
        "KeyName": str,
        "LaunchConfigurationName": str,
        "PlacementTenancy": str,
        "RamdiskId": str,
        "SecurityGroups": Sequence[str],
        "SpotPrice": str,
        "UserData": str,
        "MetadataOptions": AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef,
    },
    total=False,
)

AwsBackupBackupPlanRuleDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleDetailsOutputTypeDef",
    {
        "TargetBackupVault": str,
        "StartWindowMinutes": int,
        "ScheduleExpression": str,
        "RuleName": str,
        "RuleId": str,
        "EnableContinuousBackup": bool,
        "CompletionWindowMinutes": int,
        "CopyActions": List[AwsBackupBackupPlanRuleCopyActionsDetailsOutputTypeDef],
        "Lifecycle": AwsBackupBackupPlanLifecycleDetailsOutputTypeDef,
    },
)

AwsBackupBackupPlanRuleDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleDetailsTypeDef",
    {
        "TargetBackupVault": str,
        "StartWindowMinutes": int,
        "ScheduleExpression": str,
        "RuleName": str,
        "RuleId": str,
        "EnableContinuousBackup": bool,
        "CompletionWindowMinutes": int,
        "CopyActions": Sequence[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef],
        "Lifecycle": AwsBackupBackupPlanLifecycleDetailsTypeDef,
    },
    total=False,
)

AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef",
    {
        "DomainValidationOptions": List[
            AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef
        ],
        "RenewalStatus": str,
        "RenewalStatusReason": str,
        "UpdatedAt": str,
    },
)

AwsCertificateManagerCertificateRenewalSummaryTypeDef = TypedDict(
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    {
        "DomainValidationOptions": Sequence[
            AwsCertificateManagerCertificateDomainValidationOptionTypeDef
        ],
        "RenewalStatus": str,
        "RenewalStatusReason": str,
        "UpdatedAt": str,
    },
    total=False,
)

AwsCloudFrontDistributionOriginItemOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemOutputTypeDef",
    {
        "DomainName": str,
        "Id": str,
        "OriginPath": str,
        "S3OriginConfig": AwsCloudFrontDistributionOriginS3OriginConfigOutputTypeDef,
        "CustomOriginConfig": AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef,
    },
)

AwsCloudFrontDistributionOriginItemTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemTypeDef",
    {
        "DomainName": str,
        "Id": str,
        "OriginPath": str,
        "S3OriginConfig": AwsCloudFrontDistributionOriginS3OriginConfigTypeDef,
        "CustomOriginConfig": AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef,
    },
    total=False,
)

AwsCloudFrontDistributionOriginGroupOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupOutputTypeDef",
    {
        "FailoverCriteria": AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef,
    },
)

AwsCloudFrontDistributionOriginGroupTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    {
        "FailoverCriteria": AwsCloudFrontDistributionOriginGroupFailoverTypeDef,
    },
    total=False,
)

AwsCodeBuildProjectDetailsOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsOutputTypeDef",
    {
        "EncryptionKey": str,
        "Artifacts": List[AwsCodeBuildProjectArtifactsDetailsOutputTypeDef],
        "Environment": AwsCodeBuildProjectEnvironmentOutputTypeDef,
        "Name": str,
        "Source": AwsCodeBuildProjectSourceOutputTypeDef,
        "ServiceRole": str,
        "LogsConfig": AwsCodeBuildProjectLogsConfigDetailsOutputTypeDef,
        "VpcConfig": AwsCodeBuildProjectVpcConfigOutputTypeDef,
        "SecondaryArtifacts": List[AwsCodeBuildProjectArtifactsDetailsOutputTypeDef],
    },
)

AwsCodeBuildProjectDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsTypeDef",
    {
        "EncryptionKey": str,
        "Artifacts": Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef],
        "Environment": AwsCodeBuildProjectEnvironmentTypeDef,
        "Name": str,
        "Source": AwsCodeBuildProjectSourceTypeDef,
        "ServiceRole": str,
        "LogsConfig": AwsCodeBuildProjectLogsConfigDetailsTypeDef,
        "VpcConfig": AwsCodeBuildProjectVpcConfigTypeDef,
        "SecondaryArtifacts": Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef],
    },
    total=False,
)

AwsDynamoDbTableReplicaOutputTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaOutputTypeDef",
    {
        "GlobalSecondaryIndexes": List[AwsDynamoDbTableReplicaGlobalSecondaryIndexOutputTypeDef],
        "KmsMasterKeyId": str,
        "ProvisionedThroughputOverride": AwsDynamoDbTableProvisionedThroughputOverrideOutputTypeDef,
        "RegionName": str,
        "ReplicaStatus": str,
        "ReplicaStatusDescription": str,
    },
)

AwsDynamoDbTableReplicaTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaTypeDef",
    {
        "GlobalSecondaryIndexes": Sequence[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef],
        "KmsMasterKeyId": str,
        "ProvisionedThroughputOverride": AwsDynamoDbTableProvisionedThroughputOverrideTypeDef,
        "RegionName": str,
        "ReplicaStatus": str,
        "ReplicaStatusDescription": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDataDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataDetailsOutputTypeDef",
    {
        "BlockDeviceMappingSet": List[
            AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsOutputTypeDef
        ],
        "CapacityReservationSpecification": (
            AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsOutputTypeDef
        ),
        "CpuOptions": AwsEc2LaunchTemplateDataCpuOptionsDetailsOutputTypeDef,
        "CreditSpecification": AwsEc2LaunchTemplateDataCreditSpecificationDetailsOutputTypeDef,
        "DisableApiStop": bool,
        "DisableApiTermination": bool,
        "EbsOptimized": bool,
        "ElasticGpuSpecificationSet": List[
            AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsOutputTypeDef
        ],
        "ElasticInferenceAcceleratorSet": List[
            AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsOutputTypeDef
        ],
        "EnclaveOptions": AwsEc2LaunchTemplateDataEnclaveOptionsDetailsOutputTypeDef,
        "HibernationOptions": AwsEc2LaunchTemplateDataHibernationOptionsDetailsOutputTypeDef,
        "IamInstanceProfile": AwsEc2LaunchTemplateDataIamInstanceProfileDetailsOutputTypeDef,
        "ImageId": str,
        "InstanceInitiatedShutdownBehavior": str,
        "InstanceMarketOptions": AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsOutputTypeDef,
        "InstanceRequirements": AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef,
        "InstanceType": str,
        "KernelId": str,
        "KeyName": str,
        "LicenseSet": List[AwsEc2LaunchTemplateDataLicenseSetDetailsOutputTypeDef],
        "MaintenanceOptions": AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsOutputTypeDef,
        "MetadataOptions": AwsEc2LaunchTemplateDataMetadataOptionsDetailsOutputTypeDef,
        "Monitoring": AwsEc2LaunchTemplateDataMonitoringDetailsOutputTypeDef,
        "NetworkInterfaceSet": List[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef
        ],
        "Placement": AwsEc2LaunchTemplateDataPlacementDetailsOutputTypeDef,
        "PrivateDnsNameOptions": AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsOutputTypeDef,
        "RamDiskId": str,
        "SecurityGroupIdSet": List[str],
        "SecurityGroupSet": List[str],
        "UserData": str,
    },
)

AwsEc2LaunchTemplateDataDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataDetailsTypeDef",
    {
        "BlockDeviceMappingSet": Sequence[
            AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef
        ],
        "CapacityReservationSpecification": (
            AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef
        ),
        "CpuOptions": AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef,
        "CreditSpecification": AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef,
        "DisableApiStop": bool,
        "DisableApiTermination": bool,
        "EbsOptimized": bool,
        "ElasticGpuSpecificationSet": Sequence[
            AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef
        ],
        "ElasticInferenceAcceleratorSet": Sequence[
            AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef
        ],
        "EnclaveOptions": AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef,
        "HibernationOptions": AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef,
        "IamInstanceProfile": AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef,
        "ImageId": str,
        "InstanceInitiatedShutdownBehavior": str,
        "InstanceMarketOptions": AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef,
        "InstanceRequirements": AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef,
        "InstanceType": str,
        "KernelId": str,
        "KeyName": str,
        "LicenseSet": Sequence[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef],
        "MaintenanceOptions": AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef,
        "MetadataOptions": AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef,
        "Monitoring": AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef,
        "NetworkInterfaceSet": Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef],
        "Placement": AwsEc2LaunchTemplateDataPlacementDetailsTypeDef,
        "PrivateDnsNameOptions": AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef,
        "RamDiskId": str,
        "SecurityGroupIdSet": Sequence[str],
        "SecurityGroupSet": Sequence[str],
        "UserData": str,
    },
    total=False,
)

AwsEc2NetworkAclDetailsOutputTypeDef = TypedDict(
    "AwsEc2NetworkAclDetailsOutputTypeDef",
    {
        "IsDefault": bool,
        "NetworkAclId": str,
        "OwnerId": str,
        "VpcId": str,
        "Associations": List[AwsEc2NetworkAclAssociationOutputTypeDef],
        "Entries": List[AwsEc2NetworkAclEntryOutputTypeDef],
    },
)

AwsEc2NetworkAclDetailsTypeDef = TypedDict(
    "AwsEc2NetworkAclDetailsTypeDef",
    {
        "IsDefault": bool,
        "NetworkAclId": str,
        "OwnerId": str,
        "VpcId": str,
        "Associations": Sequence[AwsEc2NetworkAclAssociationTypeDef],
        "Entries": Sequence[AwsEc2NetworkAclEntryTypeDef],
    },
    total=False,
)

AwsEc2SecurityGroupDetailsOutputTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsOutputTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
        "OwnerId": str,
        "VpcId": str,
        "IpPermissions": List[AwsEc2SecurityGroupIpPermissionOutputTypeDef],
        "IpPermissionsEgress": List[AwsEc2SecurityGroupIpPermissionOutputTypeDef],
    },
)

AwsEc2SecurityGroupDetailsTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
        "OwnerId": str,
        "VpcId": str,
        "IpPermissions": Sequence[AwsEc2SecurityGroupIpPermissionTypeDef],
        "IpPermissionsEgress": Sequence[AwsEc2SecurityGroupIpPermissionTypeDef],
    },
    total=False,
)

AwsEc2VpcPeeringConnectionDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionDetailsOutputTypeDef",
    {
        "AccepterVpcInfo": AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef,
        "ExpirationTime": str,
        "RequesterVpcInfo": AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef,
        "Status": AwsEc2VpcPeeringConnectionStatusDetailsOutputTypeDef,
        "VpcPeeringConnectionId": str,
    },
)

AwsEc2VpcPeeringConnectionDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionDetailsTypeDef",
    {
        "AccepterVpcInfo": AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef,
        "ExpirationTime": str,
        "RequesterVpcInfo": AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef,
        "Status": AwsEc2VpcPeeringConnectionStatusDetailsTypeDef,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

AwsEc2VpnConnectionDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsOutputTypeDef",
    {
        "VpnConnectionId": str,
        "State": str,
        "CustomerGatewayId": str,
        "CustomerGatewayConfiguration": str,
        "Type": str,
        "VpnGatewayId": str,
        "Category": str,
        "VgwTelemetry": List[AwsEc2VpnConnectionVgwTelemetryDetailsOutputTypeDef],
        "Options": AwsEc2VpnConnectionOptionsDetailsOutputTypeDef,
        "Routes": List[AwsEc2VpnConnectionRoutesDetailsOutputTypeDef],
        "TransitGatewayId": str,
    },
)

AwsEc2VpnConnectionDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsTypeDef",
    {
        "VpnConnectionId": str,
        "State": str,
        "CustomerGatewayId": str,
        "CustomerGatewayConfiguration": str,
        "Type": str,
        "VpnGatewayId": str,
        "Category": str,
        "VgwTelemetry": Sequence[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef],
        "Options": AwsEc2VpnConnectionOptionsDetailsTypeDef,
        "Routes": Sequence[AwsEc2VpnConnectionRoutesDetailsTypeDef],
        "TransitGatewayId": str,
    },
    total=False,
)

AwsEcsClusterConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsClusterConfigurationDetailsOutputTypeDef",
    {
        "ExecuteCommandConfiguration": (
            AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsOutputTypeDef
        ),
    },
)

AwsEcsClusterConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationDetailsTypeDef",
    {
        "ExecuteCommandConfiguration": (
            AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef
        ),
    },
    total=False,
)

AwsEcsServiceDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceDetailsOutputTypeDef",
    {
        "CapacityProviderStrategy": List[AwsEcsServiceCapacityProviderStrategyDetailsOutputTypeDef],
        "Cluster": str,
        "DeploymentConfiguration": AwsEcsServiceDeploymentConfigurationDetailsOutputTypeDef,
        "DeploymentController": AwsEcsServiceDeploymentControllerDetailsOutputTypeDef,
        "DesiredCount": int,
        "EnableEcsManagedTags": bool,
        "EnableExecuteCommand": bool,
        "HealthCheckGracePeriodSeconds": int,
        "LaunchType": str,
        "LoadBalancers": List[AwsEcsServiceLoadBalancersDetailsOutputTypeDef],
        "Name": str,
        "NetworkConfiguration": AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef,
        "PlacementConstraints": List[AwsEcsServicePlacementConstraintsDetailsOutputTypeDef],
        "PlacementStrategies": List[AwsEcsServicePlacementStrategiesDetailsOutputTypeDef],
        "PlatformVersion": str,
        "PropagateTags": str,
        "Role": str,
        "SchedulingStrategy": str,
        "ServiceArn": str,
        "ServiceName": str,
        "ServiceRegistries": List[AwsEcsServiceServiceRegistriesDetailsOutputTypeDef],
        "TaskDefinition": str,
    },
)

AwsEcsServiceDetailsTypeDef = TypedDict(
    "AwsEcsServiceDetailsTypeDef",
    {
        "CapacityProviderStrategy": Sequence[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef],
        "Cluster": str,
        "DeploymentConfiguration": AwsEcsServiceDeploymentConfigurationDetailsTypeDef,
        "DeploymentController": AwsEcsServiceDeploymentControllerDetailsTypeDef,
        "DesiredCount": int,
        "EnableEcsManagedTags": bool,
        "EnableExecuteCommand": bool,
        "HealthCheckGracePeriodSeconds": int,
        "LaunchType": str,
        "LoadBalancers": Sequence[AwsEcsServiceLoadBalancersDetailsTypeDef],
        "Name": str,
        "NetworkConfiguration": AwsEcsServiceNetworkConfigurationDetailsTypeDef,
        "PlacementConstraints": Sequence[AwsEcsServicePlacementConstraintsDetailsTypeDef],
        "PlacementStrategies": Sequence[AwsEcsServicePlacementStrategiesDetailsTypeDef],
        "PlatformVersion": str,
        "PropagateTags": str,
        "Role": str,
        "SchedulingStrategy": str,
        "ServiceArn": str,
        "ServiceName": str,
        "ServiceRegistries": Sequence[AwsEcsServiceServiceRegistriesDetailsTypeDef],
        "TaskDefinition": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef",
    {
        "Command": List[str],
        "Cpu": int,
        "DependsOn": List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsOutputTypeDef],
        "DisableNetworking": bool,
        "DnsSearchDomains": List[str],
        "DnsServers": List[str],
        "DockerLabels": Dict[str, str],
        "DockerSecurityOptions": List[str],
        "EntryPoint": List[str],
        "Environment": List[
            AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsOutputTypeDef
        ],
        "EnvironmentFiles": List[
            AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsOutputTypeDef
        ],
        "Essential": bool,
        "ExtraHosts": List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsOutputTypeDef],
        "FirelensConfiguration": (
            AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef
        ),
        "HealthCheck": AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef,
        "Hostname": str,
        "Image": str,
        "Interactive": bool,
        "Links": List[str],
        "LinuxParameters": (
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef
        ),
        "LogConfiguration": (
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef
        ),
        "Memory": int,
        "MemoryReservation": int,
        "MountPoints": List[
            AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsOutputTypeDef
        ],
        "Name": str,
        "PortMappings": List[
            AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsOutputTypeDef
        ],
        "Privileged": bool,
        "PseudoTerminal": bool,
        "ReadonlyRootFilesystem": bool,
        "RepositoryCredentials": (
            AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsOutputTypeDef
        ),
        "ResourceRequirements": List[
            AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsOutputTypeDef
        ],
        "Secrets": List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsOutputTypeDef],
        "StartTimeout": int,
        "StopTimeout": int,
        "SystemControls": List[
            AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsOutputTypeDef
        ],
        "Ulimits": List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsOutputTypeDef],
        "User": str,
        "VolumesFrom": List[
            AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsOutputTypeDef
        ],
        "WorkingDirectory": str,
    },
)

AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    {
        "Command": Sequence[str],
        "Cpu": int,
        "DependsOn": Sequence[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef],
        "DisableNetworking": bool,
        "DnsSearchDomains": Sequence[str],
        "DnsServers": Sequence[str],
        "DockerLabels": Mapping[str, str],
        "DockerSecurityOptions": Sequence[str],
        "EntryPoint": Sequence[str],
        "Environment": Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef],
        "EnvironmentFiles": Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef
        ],
        "Essential": bool,
        "ExtraHosts": Sequence[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef],
        "FirelensConfiguration": (
            AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef
        ),
        "HealthCheck": AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef,
        "Hostname": str,
        "Image": str,
        "Interactive": bool,
        "Links": Sequence[str],
        "LinuxParameters": AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef,
        "LogConfiguration": AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef,
        "Memory": int,
        "MemoryReservation": int,
        "MountPoints": Sequence[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef],
        "Name": str,
        "PortMappings": Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef
        ],
        "Privileged": bool,
        "PseudoTerminal": bool,
        "ReadonlyRootFilesystem": bool,
        "RepositoryCredentials": (
            AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef
        ),
        "ResourceRequirements": Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef
        ],
        "Secrets": Sequence[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef],
        "StartTimeout": int,
        "StopTimeout": int,
        "SystemControls": Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef
        ],
        "Ulimits": Sequence[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef],
        "User": str,
        "VolumesFrom": Sequence[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef],
        "WorkingDirectory": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef",
    {
        "DockerVolumeConfiguration": (
            AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef
        ),
        "EfsVolumeConfiguration": (
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsOutputTypeDef
        ),
        "Host": AwsEcsTaskDefinitionVolumesHostDetailsOutputTypeDef,
        "Name": str,
    },
)

AwsEcsTaskDefinitionVolumesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    {
        "DockerVolumeConfiguration": (
            AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef
        ),
        "EfsVolumeConfiguration": AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef,
        "Host": AwsEcsTaskDefinitionVolumesHostDetailsTypeDef,
        "Name": str,
    },
    total=False,
)

AwsEcsTaskDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDetailsOutputTypeDef",
    {
        "ClusterArn": str,
        "TaskDefinitionArn": str,
        "Version": str,
        "CreatedAt": str,
        "StartedAt": str,
        "StartedBy": str,
        "Group": str,
        "Volumes": List[AwsEcsTaskVolumeDetailsOutputTypeDef],
        "Containers": List[AwsEcsContainerDetailsOutputTypeDef],
    },
)

AwsEcsTaskDetailsTypeDef = TypedDict(
    "AwsEcsTaskDetailsTypeDef",
    {
        "ClusterArn": str,
        "TaskDefinitionArn": str,
        "Version": str,
        "CreatedAt": str,
        "StartedAt": str,
        "StartedBy": str,
        "Group": str,
        "Volumes": Sequence[AwsEcsTaskVolumeDetailsTypeDef],
        "Containers": Sequence[AwsEcsContainerDetailsTypeDef],
    },
    total=False,
)

AwsEfsAccessPointDetailsOutputTypeDef = TypedDict(
    "AwsEfsAccessPointDetailsOutputTypeDef",
    {
        "AccessPointId": str,
        "Arn": str,
        "ClientToken": str,
        "FileSystemId": str,
        "PosixUser": AwsEfsAccessPointPosixUserDetailsOutputTypeDef,
        "RootDirectory": AwsEfsAccessPointRootDirectoryDetailsOutputTypeDef,
    },
)

AwsEfsAccessPointDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointDetailsTypeDef",
    {
        "AccessPointId": str,
        "Arn": str,
        "ClientToken": str,
        "FileSystemId": str,
        "PosixUser": AwsEfsAccessPointPosixUserDetailsTypeDef,
        "RootDirectory": AwsEfsAccessPointRootDirectoryDetailsTypeDef,
    },
    total=False,
)

AwsEksClusterDetailsOutputTypeDef = TypedDict(
    "AwsEksClusterDetailsOutputTypeDef",
    {
        "Arn": str,
        "CertificateAuthorityData": str,
        "ClusterStatus": str,
        "Endpoint": str,
        "Name": str,
        "ResourcesVpcConfig": AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef,
        "RoleArn": str,
        "Version": str,
        "Logging": AwsEksClusterLoggingDetailsOutputTypeDef,
    },
)

AwsEksClusterDetailsTypeDef = TypedDict(
    "AwsEksClusterDetailsTypeDef",
    {
        "Arn": str,
        "CertificateAuthorityData": str,
        "ClusterStatus": str,
        "Endpoint": str,
        "Name": str,
        "ResourcesVpcConfig": AwsEksClusterResourcesVpcConfigDetailsTypeDef,
        "RoleArn": str,
        "Version": str,
        "Logging": AwsEksClusterLoggingDetailsTypeDef,
    },
    total=False,
)

AwsElasticsearchDomainDetailsOutputTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsOutputTypeDef",
    {
        "AccessPolicies": str,
        "DomainEndpointOptions": AwsElasticsearchDomainDomainEndpointOptionsOutputTypeDef,
        "DomainId": str,
        "DomainName": str,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": (
            AwsElasticsearchDomainElasticsearchClusterConfigDetailsOutputTypeDef
        ),
        "EncryptionAtRestOptions": AwsElasticsearchDomainEncryptionAtRestOptionsOutputTypeDef,
        "LogPublishingOptions": AwsElasticsearchDomainLogPublishingOptionsOutputTypeDef,
        "NodeToNodeEncryptionOptions": (
            AwsElasticsearchDomainNodeToNodeEncryptionOptionsOutputTypeDef
        ),
        "ServiceSoftwareOptions": AwsElasticsearchDomainServiceSoftwareOptionsOutputTypeDef,
        "VPCOptions": AwsElasticsearchDomainVPCOptionsOutputTypeDef,
    },
)

AwsElasticsearchDomainDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsTypeDef",
    {
        "AccessPolicies": str,
        "DomainEndpointOptions": AwsElasticsearchDomainDomainEndpointOptionsTypeDef,
        "DomainId": str,
        "DomainName": str,
        "Endpoint": str,
        "Endpoints": Mapping[str, str],
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": (
            AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef
        ),
        "EncryptionAtRestOptions": AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef,
        "LogPublishingOptions": AwsElasticsearchDomainLogPublishingOptionsTypeDef,
        "NodeToNodeEncryptionOptions": AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef,
        "ServiceSoftwareOptions": AwsElasticsearchDomainServiceSoftwareOptionsTypeDef,
        "VPCOptions": AwsElasticsearchDomainVPCOptionsTypeDef,
    },
    total=False,
)

AwsElbLoadBalancerDetailsOutputTypeDef = TypedDict(
    "AwsElbLoadBalancerDetailsOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackendServerDescriptions": List[AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef],
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "CreatedTime": str,
        "DnsName": str,
        "HealthCheck": AwsElbLoadBalancerHealthCheckOutputTypeDef,
        "Instances": List[AwsElbLoadBalancerInstanceOutputTypeDef],
        "ListenerDescriptions": List[AwsElbLoadBalancerListenerDescriptionOutputTypeDef],
        "LoadBalancerAttributes": AwsElbLoadBalancerAttributesOutputTypeDef,
        "LoadBalancerName": str,
        "Policies": AwsElbLoadBalancerPoliciesOutputTypeDef,
        "Scheme": str,
        "SecurityGroups": List[str],
        "SourceSecurityGroup": AwsElbLoadBalancerSourceSecurityGroupOutputTypeDef,
        "Subnets": List[str],
        "VpcId": str,
    },
)

AwsElbLoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbLoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "BackendServerDescriptions": Sequence[AwsElbLoadBalancerBackendServerDescriptionTypeDef],
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "CreatedTime": str,
        "DnsName": str,
        "HealthCheck": AwsElbLoadBalancerHealthCheckTypeDef,
        "Instances": Sequence[AwsElbLoadBalancerInstanceTypeDef],
        "ListenerDescriptions": Sequence[AwsElbLoadBalancerListenerDescriptionTypeDef],
        "LoadBalancerAttributes": AwsElbLoadBalancerAttributesTypeDef,
        "LoadBalancerName": str,
        "Policies": AwsElbLoadBalancerPoliciesTypeDef,
        "Scheme": str,
        "SecurityGroups": Sequence[str],
        "SourceSecurityGroup": AwsElbLoadBalancerSourceSecurityGroupTypeDef,
        "Subnets": Sequence[str],
        "VpcId": str,
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsOutputTypeDef",
    {
        "ScanEc2InstanceWithFindings": AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsOutputTypeDef,
        "ServiceRole": str,
    },
)

AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef",
    {
        "ScanEc2InstanceWithFindings": AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef,
        "ServiceRole": str,
    },
    total=False,
)

AwsIamAccessKeyDetailsOutputTypeDef = TypedDict(
    "AwsIamAccessKeyDetailsOutputTypeDef",
    {
        "UserName": str,
        "Status": AwsIamAccessKeyStatusType,
        "CreatedAt": str,
        "PrincipalId": str,
        "PrincipalType": str,
        "PrincipalName": str,
        "AccountId": str,
        "AccessKeyId": str,
        "SessionContext": AwsIamAccessKeySessionContextOutputTypeDef,
    },
)

AwsIamAccessKeyDetailsTypeDef = TypedDict(
    "AwsIamAccessKeyDetailsTypeDef",
    {
        "UserName": str,
        "Status": AwsIamAccessKeyStatusType,
        "CreatedAt": str,
        "PrincipalId": str,
        "PrincipalType": str,
        "PrincipalName": str,
        "AccountId": str,
        "AccessKeyId": str,
        "SessionContext": AwsIamAccessKeySessionContextTypeDef,
    },
    total=False,
)

AwsIamRoleDetailsOutputTypeDef = TypedDict(
    "AwsIamRoleDetailsOutputTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "AttachedManagedPolicies": List[AwsIamAttachedManagedPolicyOutputTypeDef],
        "CreateDate": str,
        "InstanceProfileList": List[AwsIamInstanceProfileOutputTypeDef],
        "PermissionsBoundary": AwsIamPermissionsBoundaryOutputTypeDef,
        "RoleId": str,
        "RoleName": str,
        "RolePolicyList": List[AwsIamRolePolicyOutputTypeDef],
        "MaxSessionDuration": int,
        "Path": str,
    },
)

AwsIamRoleDetailsTypeDef = TypedDict(
    "AwsIamRoleDetailsTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "AttachedManagedPolicies": Sequence[AwsIamAttachedManagedPolicyTypeDef],
        "CreateDate": str,
        "InstanceProfileList": Sequence[AwsIamInstanceProfileTypeDef],
        "PermissionsBoundary": AwsIamPermissionsBoundaryTypeDef,
        "RoleId": str,
        "RoleName": str,
        "RolePolicyList": Sequence[AwsIamRolePolicyTypeDef],
        "MaxSessionDuration": int,
        "Path": str,
    },
    total=False,
)

AwsLambdaFunctionDetailsOutputTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsOutputTypeDef",
    {
        "Code": AwsLambdaFunctionCodeOutputTypeDef,
        "CodeSha256": str,
        "DeadLetterConfig": AwsLambdaFunctionDeadLetterConfigOutputTypeDef,
        "Environment": AwsLambdaFunctionEnvironmentOutputTypeDef,
        "FunctionName": str,
        "Handler": str,
        "KmsKeyArn": str,
        "LastModified": str,
        "Layers": List[AwsLambdaFunctionLayerOutputTypeDef],
        "MasterArn": str,
        "MemorySize": int,
        "RevisionId": str,
        "Role": str,
        "Runtime": str,
        "Timeout": int,
        "TracingConfig": AwsLambdaFunctionTracingConfigOutputTypeDef,
        "VpcConfig": AwsLambdaFunctionVpcConfigOutputTypeDef,
        "Version": str,
        "Architectures": List[str],
        "PackageType": str,
    },
)

AwsLambdaFunctionDetailsTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsTypeDef",
    {
        "Code": AwsLambdaFunctionCodeTypeDef,
        "CodeSha256": str,
        "DeadLetterConfig": AwsLambdaFunctionDeadLetterConfigTypeDef,
        "Environment": AwsLambdaFunctionEnvironmentTypeDef,
        "FunctionName": str,
        "Handler": str,
        "KmsKeyArn": str,
        "LastModified": str,
        "Layers": Sequence[AwsLambdaFunctionLayerTypeDef],
        "MasterArn": str,
        "MemorySize": int,
        "RevisionId": str,
        "Role": str,
        "Runtime": str,
        "Timeout": int,
        "TracingConfig": AwsLambdaFunctionTracingConfigTypeDef,
        "VpcConfig": AwsLambdaFunctionVpcConfigTypeDef,
        "Version": str,
        "Architectures": Sequence[str],
        "PackageType": str,
    },
    total=False,
)

AwsOpenSearchServiceDomainDetailsOutputTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDetailsOutputTypeDef",
    {
        "Arn": str,
        "AccessPolicies": str,
        "DomainName": str,
        "Id": str,
        "DomainEndpoint": str,
        "EngineVersion": str,
        "EncryptionAtRestOptions": (
            AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsOutputTypeDef
        ),
        "NodeToNodeEncryptionOptions": (
            AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsOutputTypeDef
        ),
        "ServiceSoftwareOptions": (
            AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsOutputTypeDef
        ),
        "ClusterConfig": AwsOpenSearchServiceDomainClusterConfigDetailsOutputTypeDef,
        "DomainEndpointOptions": (
            AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsOutputTypeDef
        ),
        "VpcOptions": AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef,
        "LogPublishingOptions": AwsOpenSearchServiceDomainLogPublishingOptionsDetailsOutputTypeDef,
        "DomainEndpoints": Dict[str, str],
        "AdvancedSecurityOptions": (
            AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsOutputTypeDef
        ),
    },
)

AwsOpenSearchServiceDomainDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    {
        "Arn": str,
        "AccessPolicies": str,
        "DomainName": str,
        "Id": str,
        "DomainEndpoint": str,
        "EngineVersion": str,
        "EncryptionAtRestOptions": AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef,
        "NodeToNodeEncryptionOptions": (
            AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef
        ),
        "ServiceSoftwareOptions": AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef,
        "ClusterConfig": AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef,
        "DomainEndpointOptions": AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef,
        "VpcOptions": AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef,
        "LogPublishingOptions": AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef,
        "DomainEndpoints": Mapping[str, str],
        "AdvancedSecurityOptions": AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef,
    },
    total=False,
)

AwsRdsDbSubnetGroupOutputTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupOutputTypeDef",
    {
        "DbSubnetGroupName": str,
        "DbSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[AwsRdsDbSubnetGroupSubnetOutputTypeDef],
        "DbSubnetGroupArn": str,
    },
)

AwsRdsDbSubnetGroupTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupTypeDef",
    {
        "DbSubnetGroupName": str,
        "DbSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": Sequence[AwsRdsDbSubnetGroupSubnetTypeDef],
        "DbSubnetGroupArn": str,
    },
    total=False,
)

AwsRedshiftClusterDetailsOutputTypeDef = TypedDict(
    "AwsRedshiftClusterDetailsOutputTypeDef",
    {
        "AllowVersionUpgrade": bool,
        "AutomatedSnapshotRetentionPeriod": int,
        "AvailabilityZone": str,
        "ClusterAvailabilityStatus": str,
        "ClusterCreateTime": str,
        "ClusterIdentifier": str,
        "ClusterNodes": List[AwsRedshiftClusterClusterNodeOutputTypeDef],
        "ClusterParameterGroups": List[AwsRedshiftClusterClusterParameterGroupOutputTypeDef],
        "ClusterPublicKey": str,
        "ClusterRevisionNumber": str,
        "ClusterSecurityGroups": List[AwsRedshiftClusterClusterSecurityGroupOutputTypeDef],
        "ClusterSnapshotCopyStatus": AwsRedshiftClusterClusterSnapshotCopyStatusOutputTypeDef,
        "ClusterStatus": str,
        "ClusterSubnetGroupName": str,
        "ClusterVersion": str,
        "DBName": str,
        "DeferredMaintenanceWindows": List[
            AwsRedshiftClusterDeferredMaintenanceWindowOutputTypeDef
        ],
        "ElasticIpStatus": AwsRedshiftClusterElasticIpStatusOutputTypeDef,
        "ElasticResizeNumberOfNodeOptions": str,
        "Encrypted": bool,
        "Endpoint": AwsRedshiftClusterEndpointOutputTypeDef,
        "EnhancedVpcRouting": bool,
        "ExpectedNextSnapshotScheduleTime": str,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "HsmStatus": AwsRedshiftClusterHsmStatusOutputTypeDef,
        "IamRoles": List[AwsRedshiftClusterIamRoleOutputTypeDef],
        "KmsKeyId": str,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "MasterUsername": str,
        "NextMaintenanceWindowStartTime": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "PendingActions": List[str],
        "PendingModifiedValues": AwsRedshiftClusterPendingModifiedValuesOutputTypeDef,
        "PreferredMaintenanceWindow": str,
        "PubliclyAccessible": bool,
        "ResizeInfo": AwsRedshiftClusterResizeInfoOutputTypeDef,
        "RestoreStatus": AwsRedshiftClusterRestoreStatusOutputTypeDef,
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": str,
        "VpcId": str,
        "VpcSecurityGroups": List[AwsRedshiftClusterVpcSecurityGroupOutputTypeDef],
        "LoggingStatus": AwsRedshiftClusterLoggingStatusOutputTypeDef,
    },
)

AwsRedshiftClusterDetailsTypeDef = TypedDict(
    "AwsRedshiftClusterDetailsTypeDef",
    {
        "AllowVersionUpgrade": bool,
        "AutomatedSnapshotRetentionPeriod": int,
        "AvailabilityZone": str,
        "ClusterAvailabilityStatus": str,
        "ClusterCreateTime": str,
        "ClusterIdentifier": str,
        "ClusterNodes": Sequence[AwsRedshiftClusterClusterNodeTypeDef],
        "ClusterParameterGroups": Sequence[AwsRedshiftClusterClusterParameterGroupTypeDef],
        "ClusterPublicKey": str,
        "ClusterRevisionNumber": str,
        "ClusterSecurityGroups": Sequence[AwsRedshiftClusterClusterSecurityGroupTypeDef],
        "ClusterSnapshotCopyStatus": AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef,
        "ClusterStatus": str,
        "ClusterSubnetGroupName": str,
        "ClusterVersion": str,
        "DBName": str,
        "DeferredMaintenanceWindows": Sequence[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef],
        "ElasticIpStatus": AwsRedshiftClusterElasticIpStatusTypeDef,
        "ElasticResizeNumberOfNodeOptions": str,
        "Encrypted": bool,
        "Endpoint": AwsRedshiftClusterEndpointTypeDef,
        "EnhancedVpcRouting": bool,
        "ExpectedNextSnapshotScheduleTime": str,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "HsmStatus": AwsRedshiftClusterHsmStatusTypeDef,
        "IamRoles": Sequence[AwsRedshiftClusterIamRoleTypeDef],
        "KmsKeyId": str,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "MasterUsername": str,
        "NextMaintenanceWindowStartTime": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "PendingActions": Sequence[str],
        "PendingModifiedValues": AwsRedshiftClusterPendingModifiedValuesTypeDef,
        "PreferredMaintenanceWindow": str,
        "PubliclyAccessible": bool,
        "ResizeInfo": AwsRedshiftClusterResizeInfoTypeDef,
        "RestoreStatus": AwsRedshiftClusterRestoreStatusTypeDef,
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": str,
        "VpcId": str,
        "VpcSecurityGroups": Sequence[AwsRedshiftClusterVpcSecurityGroupTypeDef],
        "LoggingStatus": AwsRedshiftClusterLoggingStatusTypeDef,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef",
    {
        "Operands": List[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsOutputTypeDef
        ],
        "Prefix": str,
        "Tag": AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsOutputTypeDef,
        "Type": str,
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    {
        "Operands": Sequence[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef
        ],
        "Prefix": str,
        "Tag": AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef,
        "Type": str,
    },
    total=False,
)

AwsS3BucketNotificationConfigurationFilterOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationFilterOutputTypeDef",
    {
        "S3KeyFilter": AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef,
    },
)

AwsS3BucketNotificationConfigurationFilterTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    {
        "S3KeyFilter": AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef,
    },
    total=False,
)

AwsS3BucketObjectLockConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationOutputTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": AwsS3BucketObjectLockConfigurationRuleDetailsOutputTypeDef,
    },
)

AwsS3BucketObjectLockConfigurationTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef,
    },
    total=False,
)

AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef",
    {
        "Rules": List[AwsS3BucketServerSideEncryptionRuleOutputTypeDef],
    },
)

AwsS3BucketServerSideEncryptionConfigurationTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": Sequence[AwsS3BucketServerSideEncryptionRuleTypeDef],
    },
    total=False,
)

AwsS3BucketWebsiteConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationOutputTypeDef",
    {
        "ErrorDocument": str,
        "IndexDocumentSuffix": str,
        "RedirectAllRequestsTo": AwsS3BucketWebsiteConfigurationRedirectToOutputTypeDef,
        "RoutingRules": List[AwsS3BucketWebsiteConfigurationRoutingRuleOutputTypeDef],
    },
)

AwsS3BucketWebsiteConfigurationTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": str,
        "IndexDocumentSuffix": str,
        "RedirectAllRequestsTo": AwsS3BucketWebsiteConfigurationRedirectToTypeDef,
        "RoutingRules": Sequence[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef],
    },
    total=False,
)

BatchUpdateFindingsResponseTypeDef = TypedDict(
    "BatchUpdateFindingsResponseTypeDef",
    {
        "ProcessedFindings": List[AwsSecurityFindingIdentifierOutputTypeDef],
        "UnprocessedFindings": List[BatchUpdateFindingsUnprocessedFindingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AwsSsmPatchComplianceDetailsOutputTypeDef = TypedDict(
    "AwsSsmPatchComplianceDetailsOutputTypeDef",
    {
        "Patch": AwsSsmPatchOutputTypeDef,
    },
)

AwsSsmPatchComplianceDetailsTypeDef = TypedDict(
    "AwsSsmPatchComplianceDetailsTypeDef",
    {
        "Patch": AwsSsmPatchTypeDef,
    },
    total=False,
)

AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef",
    {
        "Destinations": List[
            AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsOutputTypeDef
        ],
        "IncludeExecutionData": bool,
        "Level": str,
    },
)

AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef",
    {
        "Destinations": Sequence[
            AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef
        ],
        "IncludeExecutionData": bool,
        "Level": str,
    },
    total=False,
)

AwsWafRegionalRuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupDetailsOutputTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "RuleGroupId": str,
        "Rules": List[AwsWafRegionalRuleGroupRulesDetailsOutputTypeDef],
    },
)

AwsWafRegionalRuleGroupDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupDetailsTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "RuleGroupId": str,
        "Rules": Sequence[AwsWafRegionalRuleGroupRulesDetailsTypeDef],
    },
    total=False,
)

AwsWafRegionalWebAclDetailsOutputTypeDef = TypedDict(
    "AwsWafRegionalWebAclDetailsOutputTypeDef",
    {
        "DefaultAction": str,
        "MetricName": str,
        "Name": str,
        "RulesList": List[AwsWafRegionalWebAclRulesListDetailsOutputTypeDef],
        "WebAclId": str,
    },
)

AwsWafRegionalWebAclDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclDetailsTypeDef",
    {
        "DefaultAction": str,
        "MetricName": str,
        "Name": str,
        "RulesList": Sequence[AwsWafRegionalWebAclRulesListDetailsTypeDef],
        "WebAclId": str,
    },
    total=False,
)

AwsWafRuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsWafRuleGroupDetailsOutputTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "RuleGroupId": str,
        "Rules": List[AwsWafRuleGroupRulesDetailsOutputTypeDef],
    },
)

AwsWafRuleGroupDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupDetailsTypeDef",
    {
        "MetricName": str,
        "Name": str,
        "RuleGroupId": str,
        "Rules": Sequence[AwsWafRuleGroupRulesDetailsTypeDef],
    },
    total=False,
)

AwsWafWebAclDetailsOutputTypeDef = TypedDict(
    "AwsWafWebAclDetailsOutputTypeDef",
    {
        "Name": str,
        "DefaultAction": str,
        "Rules": List[AwsWafWebAclRuleOutputTypeDef],
        "WebAclId": str,
    },
)

AwsWafWebAclDetailsTypeDef = TypedDict(
    "AwsWafWebAclDetailsTypeDef",
    {
        "Name": str,
        "DefaultAction": str,
        "Rules": Sequence[AwsWafWebAclRuleTypeDef],
        "WebAclId": str,
    },
    total=False,
)

AwsWafv2ActionAllowDetailsOutputTypeDef = TypedDict(
    "AwsWafv2ActionAllowDetailsOutputTypeDef",
    {
        "CustomRequestHandling": AwsWafv2CustomRequestHandlingDetailsOutputTypeDef,
    },
)

AwsWafv2RulesActionCaptchaDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RulesActionCaptchaDetailsOutputTypeDef",
    {
        "CustomRequestHandling": AwsWafv2CustomRequestHandlingDetailsOutputTypeDef,
    },
)

AwsWafv2RulesActionCountDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RulesActionCountDetailsOutputTypeDef",
    {
        "CustomRequestHandling": AwsWafv2CustomRequestHandlingDetailsOutputTypeDef,
    },
)

AwsWafv2ActionBlockDetailsOutputTypeDef = TypedDict(
    "AwsWafv2ActionBlockDetailsOutputTypeDef",
    {
        "CustomResponse": AwsWafv2CustomResponseDetailsOutputTypeDef,
    },
)

AwsWafv2ActionAllowDetailsTypeDef = TypedDict(
    "AwsWafv2ActionAllowDetailsTypeDef",
    {
        "CustomRequestHandling": AwsWafv2CustomRequestHandlingDetailsTypeDef,
    },
    total=False,
)

AwsWafv2RulesActionCaptchaDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionCaptchaDetailsTypeDef",
    {
        "CustomRequestHandling": AwsWafv2CustomRequestHandlingDetailsTypeDef,
    },
    total=False,
)

AwsWafv2RulesActionCountDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionCountDetailsTypeDef",
    {
        "CustomRequestHandling": AwsWafv2CustomRequestHandlingDetailsTypeDef,
    },
    total=False,
)

AwsWafv2ActionBlockDetailsTypeDef = TypedDict(
    "AwsWafv2ActionBlockDetailsTypeDef",
    {
        "CustomResponse": AwsWafv2CustomResponseDetailsTypeDef,
    },
    total=False,
)

AutomationRulesFindingFiltersOutputTypeDef = TypedDict(
    "AutomationRulesFindingFiltersOutputTypeDef",
    {
        "ProductArn": List[StringFilterOutputTypeDef],
        "AwsAccountId": List[StringFilterOutputTypeDef],
        "Id": List[StringFilterOutputTypeDef],
        "GeneratorId": List[StringFilterOutputTypeDef],
        "Type": List[StringFilterOutputTypeDef],
        "FirstObservedAt": List[DateFilterOutputTypeDef],
        "LastObservedAt": List[DateFilterOutputTypeDef],
        "CreatedAt": List[DateFilterOutputTypeDef],
        "UpdatedAt": List[DateFilterOutputTypeDef],
        "Confidence": List[NumberFilterOutputTypeDef],
        "Criticality": List[NumberFilterOutputTypeDef],
        "Title": List[StringFilterOutputTypeDef],
        "Description": List[StringFilterOutputTypeDef],
        "SourceUrl": List[StringFilterOutputTypeDef],
        "ProductName": List[StringFilterOutputTypeDef],
        "CompanyName": List[StringFilterOutputTypeDef],
        "SeverityLabel": List[StringFilterOutputTypeDef],
        "ResourceType": List[StringFilterOutputTypeDef],
        "ResourceId": List[StringFilterOutputTypeDef],
        "ResourcePartition": List[StringFilterOutputTypeDef],
        "ResourceRegion": List[StringFilterOutputTypeDef],
        "ResourceTags": List[MapFilterOutputTypeDef],
        "ResourceDetailsOther": List[MapFilterOutputTypeDef],
        "ComplianceStatus": List[StringFilterOutputTypeDef],
        "ComplianceSecurityControlId": List[StringFilterOutputTypeDef],
        "ComplianceAssociatedStandardsId": List[StringFilterOutputTypeDef],
        "VerificationState": List[StringFilterOutputTypeDef],
        "WorkflowStatus": List[StringFilterOutputTypeDef],
        "RecordState": List[StringFilterOutputTypeDef],
        "RelatedFindingsProductArn": List[StringFilterOutputTypeDef],
        "RelatedFindingsId": List[StringFilterOutputTypeDef],
        "NoteText": List[StringFilterOutputTypeDef],
        "NoteUpdatedAt": List[DateFilterOutputTypeDef],
        "NoteUpdatedBy": List[StringFilterOutputTypeDef],
        "UserDefinedFields": List[MapFilterOutputTypeDef],
    },
)

AwsSecurityFindingFiltersOutputTypeDef = TypedDict(
    "AwsSecurityFindingFiltersOutputTypeDef",
    {
        "ProductArn": List[StringFilterOutputTypeDef],
        "AwsAccountId": List[StringFilterOutputTypeDef],
        "Id": List[StringFilterOutputTypeDef],
        "GeneratorId": List[StringFilterOutputTypeDef],
        "Region": List[StringFilterOutputTypeDef],
        "Type": List[StringFilterOutputTypeDef],
        "FirstObservedAt": List[DateFilterOutputTypeDef],
        "LastObservedAt": List[DateFilterOutputTypeDef],
        "CreatedAt": List[DateFilterOutputTypeDef],
        "UpdatedAt": List[DateFilterOutputTypeDef],
        "SeverityProduct": List[NumberFilterOutputTypeDef],
        "SeverityNormalized": List[NumberFilterOutputTypeDef],
        "SeverityLabel": List[StringFilterOutputTypeDef],
        "Confidence": List[NumberFilterOutputTypeDef],
        "Criticality": List[NumberFilterOutputTypeDef],
        "Title": List[StringFilterOutputTypeDef],
        "Description": List[StringFilterOutputTypeDef],
        "RecommendationText": List[StringFilterOutputTypeDef],
        "SourceUrl": List[StringFilterOutputTypeDef],
        "ProductFields": List[MapFilterOutputTypeDef],
        "ProductName": List[StringFilterOutputTypeDef],
        "CompanyName": List[StringFilterOutputTypeDef],
        "UserDefinedFields": List[MapFilterOutputTypeDef],
        "MalwareName": List[StringFilterOutputTypeDef],
        "MalwareType": List[StringFilterOutputTypeDef],
        "MalwarePath": List[StringFilterOutputTypeDef],
        "MalwareState": List[StringFilterOutputTypeDef],
        "NetworkDirection": List[StringFilterOutputTypeDef],
        "NetworkProtocol": List[StringFilterOutputTypeDef],
        "NetworkSourceIpV4": List[IpFilterOutputTypeDef],
        "NetworkSourceIpV6": List[IpFilterOutputTypeDef],
        "NetworkSourcePort": List[NumberFilterOutputTypeDef],
        "NetworkSourceDomain": List[StringFilterOutputTypeDef],
        "NetworkSourceMac": List[StringFilterOutputTypeDef],
        "NetworkDestinationIpV4": List[IpFilterOutputTypeDef],
        "NetworkDestinationIpV6": List[IpFilterOutputTypeDef],
        "NetworkDestinationPort": List[NumberFilterOutputTypeDef],
        "NetworkDestinationDomain": List[StringFilterOutputTypeDef],
        "ProcessName": List[StringFilterOutputTypeDef],
        "ProcessPath": List[StringFilterOutputTypeDef],
        "ProcessPid": List[NumberFilterOutputTypeDef],
        "ProcessParentPid": List[NumberFilterOutputTypeDef],
        "ProcessLaunchedAt": List[DateFilterOutputTypeDef],
        "ProcessTerminatedAt": List[DateFilterOutputTypeDef],
        "ThreatIntelIndicatorType": List[StringFilterOutputTypeDef],
        "ThreatIntelIndicatorValue": List[StringFilterOutputTypeDef],
        "ThreatIntelIndicatorCategory": List[StringFilterOutputTypeDef],
        "ThreatIntelIndicatorLastObservedAt": List[DateFilterOutputTypeDef],
        "ThreatIntelIndicatorSource": List[StringFilterOutputTypeDef],
        "ThreatIntelIndicatorSourceUrl": List[StringFilterOutputTypeDef],
        "ResourceType": List[StringFilterOutputTypeDef],
        "ResourceId": List[StringFilterOutputTypeDef],
        "ResourcePartition": List[StringFilterOutputTypeDef],
        "ResourceRegion": List[StringFilterOutputTypeDef],
        "ResourceTags": List[MapFilterOutputTypeDef],
        "ResourceAwsEc2InstanceType": List[StringFilterOutputTypeDef],
        "ResourceAwsEc2InstanceImageId": List[StringFilterOutputTypeDef],
        "ResourceAwsEc2InstanceIpV4Addresses": List[IpFilterOutputTypeDef],
        "ResourceAwsEc2InstanceIpV6Addresses": List[IpFilterOutputTypeDef],
        "ResourceAwsEc2InstanceKeyName": List[StringFilterOutputTypeDef],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[StringFilterOutputTypeDef],
        "ResourceAwsEc2InstanceVpcId": List[StringFilterOutputTypeDef],
        "ResourceAwsEc2InstanceSubnetId": List[StringFilterOutputTypeDef],
        "ResourceAwsEc2InstanceLaunchedAt": List[DateFilterOutputTypeDef],
        "ResourceAwsS3BucketOwnerId": List[StringFilterOutputTypeDef],
        "ResourceAwsS3BucketOwnerName": List[StringFilterOutputTypeDef],
        "ResourceAwsIamAccessKeyUserName": List[StringFilterOutputTypeDef],
        "ResourceAwsIamAccessKeyPrincipalName": List[StringFilterOutputTypeDef],
        "ResourceAwsIamAccessKeyStatus": List[StringFilterOutputTypeDef],
        "ResourceAwsIamAccessKeyCreatedAt": List[DateFilterOutputTypeDef],
        "ResourceAwsIamUserUserName": List[StringFilterOutputTypeDef],
        "ResourceContainerName": List[StringFilterOutputTypeDef],
        "ResourceContainerImageId": List[StringFilterOutputTypeDef],
        "ResourceContainerImageName": List[StringFilterOutputTypeDef],
        "ResourceContainerLaunchedAt": List[DateFilterOutputTypeDef],
        "ResourceDetailsOther": List[MapFilterOutputTypeDef],
        "ComplianceStatus": List[StringFilterOutputTypeDef],
        "VerificationState": List[StringFilterOutputTypeDef],
        "WorkflowState": List[StringFilterOutputTypeDef],
        "WorkflowStatus": List[StringFilterOutputTypeDef],
        "RecordState": List[StringFilterOutputTypeDef],
        "RelatedFindingsProductArn": List[StringFilterOutputTypeDef],
        "RelatedFindingsId": List[StringFilterOutputTypeDef],
        "NoteText": List[StringFilterOutputTypeDef],
        "NoteUpdatedAt": List[DateFilterOutputTypeDef],
        "NoteUpdatedBy": List[StringFilterOutputTypeDef],
        "Keyword": List[KeywordFilterOutputTypeDef],
        "FindingProviderFieldsConfidence": List[NumberFilterOutputTypeDef],
        "FindingProviderFieldsCriticality": List[NumberFilterOutputTypeDef],
        "FindingProviderFieldsRelatedFindingsId": List[StringFilterOutputTypeDef],
        "FindingProviderFieldsRelatedFindingsProductArn": List[StringFilterOutputTypeDef],
        "FindingProviderFieldsSeverityLabel": List[StringFilterOutputTypeDef],
        "FindingProviderFieldsSeverityOriginal": List[StringFilterOutputTypeDef],
        "FindingProviderFieldsTypes": List[StringFilterOutputTypeDef],
        "Sample": List[BooleanFilterOutputTypeDef],
        "ComplianceSecurityControlId": List[StringFilterOutputTypeDef],
        "ComplianceAssociatedStandardsId": List[StringFilterOutputTypeDef],
    },
)

AutomationRulesFindingFiltersTypeDef = TypedDict(
    "AutomationRulesFindingFiltersTypeDef",
    {
        "ProductArn": Sequence[StringFilterTypeDef],
        "AwsAccountId": Sequence[StringFilterTypeDef],
        "Id": Sequence[StringFilterTypeDef],
        "GeneratorId": Sequence[StringFilterTypeDef],
        "Type": Sequence[StringFilterTypeDef],
        "FirstObservedAt": Sequence[DateFilterTypeDef],
        "LastObservedAt": Sequence[DateFilterTypeDef],
        "CreatedAt": Sequence[DateFilterTypeDef],
        "UpdatedAt": Sequence[DateFilterTypeDef],
        "Confidence": Sequence[NumberFilterTypeDef],
        "Criticality": Sequence[NumberFilterTypeDef],
        "Title": Sequence[StringFilterTypeDef],
        "Description": Sequence[StringFilterTypeDef],
        "SourceUrl": Sequence[StringFilterTypeDef],
        "ProductName": Sequence[StringFilterTypeDef],
        "CompanyName": Sequence[StringFilterTypeDef],
        "SeverityLabel": Sequence[StringFilterTypeDef],
        "ResourceType": Sequence[StringFilterTypeDef],
        "ResourceId": Sequence[StringFilterTypeDef],
        "ResourcePartition": Sequence[StringFilterTypeDef],
        "ResourceRegion": Sequence[StringFilterTypeDef],
        "ResourceTags": Sequence[MapFilterTypeDef],
        "ResourceDetailsOther": Sequence[MapFilterTypeDef],
        "ComplianceStatus": Sequence[StringFilterTypeDef],
        "ComplianceSecurityControlId": Sequence[StringFilterTypeDef],
        "ComplianceAssociatedStandardsId": Sequence[StringFilterTypeDef],
        "VerificationState": Sequence[StringFilterTypeDef],
        "WorkflowStatus": Sequence[StringFilterTypeDef],
        "RecordState": Sequence[StringFilterTypeDef],
        "RelatedFindingsProductArn": Sequence[StringFilterTypeDef],
        "RelatedFindingsId": Sequence[StringFilterTypeDef],
        "NoteText": Sequence[StringFilterTypeDef],
        "NoteUpdatedAt": Sequence[DateFilterTypeDef],
        "NoteUpdatedBy": Sequence[StringFilterTypeDef],
        "UserDefinedFields": Sequence[MapFilterTypeDef],
    },
    total=False,
)

AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": Sequence[StringFilterTypeDef],
        "AwsAccountId": Sequence[StringFilterTypeDef],
        "Id": Sequence[StringFilterTypeDef],
        "GeneratorId": Sequence[StringFilterTypeDef],
        "Region": Sequence[StringFilterTypeDef],
        "Type": Sequence[StringFilterTypeDef],
        "FirstObservedAt": Sequence[DateFilterTypeDef],
        "LastObservedAt": Sequence[DateFilterTypeDef],
        "CreatedAt": Sequence[DateFilterTypeDef],
        "UpdatedAt": Sequence[DateFilterTypeDef],
        "SeverityProduct": Sequence[NumberFilterTypeDef],
        "SeverityNormalized": Sequence[NumberFilterTypeDef],
        "SeverityLabel": Sequence[StringFilterTypeDef],
        "Confidence": Sequence[NumberFilterTypeDef],
        "Criticality": Sequence[NumberFilterTypeDef],
        "Title": Sequence[StringFilterTypeDef],
        "Description": Sequence[StringFilterTypeDef],
        "RecommendationText": Sequence[StringFilterTypeDef],
        "SourceUrl": Sequence[StringFilterTypeDef],
        "ProductFields": Sequence[MapFilterTypeDef],
        "ProductName": Sequence[StringFilterTypeDef],
        "CompanyName": Sequence[StringFilterTypeDef],
        "UserDefinedFields": Sequence[MapFilterTypeDef],
        "MalwareName": Sequence[StringFilterTypeDef],
        "MalwareType": Sequence[StringFilterTypeDef],
        "MalwarePath": Sequence[StringFilterTypeDef],
        "MalwareState": Sequence[StringFilterTypeDef],
        "NetworkDirection": Sequence[StringFilterTypeDef],
        "NetworkProtocol": Sequence[StringFilterTypeDef],
        "NetworkSourceIpV4": Sequence[IpFilterTypeDef],
        "NetworkSourceIpV6": Sequence[IpFilterTypeDef],
        "NetworkSourcePort": Sequence[NumberFilterTypeDef],
        "NetworkSourceDomain": Sequence[StringFilterTypeDef],
        "NetworkSourceMac": Sequence[StringFilterTypeDef],
        "NetworkDestinationIpV4": Sequence[IpFilterTypeDef],
        "NetworkDestinationIpV6": Sequence[IpFilterTypeDef],
        "NetworkDestinationPort": Sequence[NumberFilterTypeDef],
        "NetworkDestinationDomain": Sequence[StringFilterTypeDef],
        "ProcessName": Sequence[StringFilterTypeDef],
        "ProcessPath": Sequence[StringFilterTypeDef],
        "ProcessPid": Sequence[NumberFilterTypeDef],
        "ProcessParentPid": Sequence[NumberFilterTypeDef],
        "ProcessLaunchedAt": Sequence[DateFilterTypeDef],
        "ProcessTerminatedAt": Sequence[DateFilterTypeDef],
        "ThreatIntelIndicatorType": Sequence[StringFilterTypeDef],
        "ThreatIntelIndicatorValue": Sequence[StringFilterTypeDef],
        "ThreatIntelIndicatorCategory": Sequence[StringFilterTypeDef],
        "ThreatIntelIndicatorLastObservedAt": Sequence[DateFilterTypeDef],
        "ThreatIntelIndicatorSource": Sequence[StringFilterTypeDef],
        "ThreatIntelIndicatorSourceUrl": Sequence[StringFilterTypeDef],
        "ResourceType": Sequence[StringFilterTypeDef],
        "ResourceId": Sequence[StringFilterTypeDef],
        "ResourcePartition": Sequence[StringFilterTypeDef],
        "ResourceRegion": Sequence[StringFilterTypeDef],
        "ResourceTags": Sequence[MapFilterTypeDef],
        "ResourceAwsEc2InstanceType": Sequence[StringFilterTypeDef],
        "ResourceAwsEc2InstanceImageId": Sequence[StringFilterTypeDef],
        "ResourceAwsEc2InstanceIpV4Addresses": Sequence[IpFilterTypeDef],
        "ResourceAwsEc2InstanceIpV6Addresses": Sequence[IpFilterTypeDef],
        "ResourceAwsEc2InstanceKeyName": Sequence[StringFilterTypeDef],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": Sequence[StringFilterTypeDef],
        "ResourceAwsEc2InstanceVpcId": Sequence[StringFilterTypeDef],
        "ResourceAwsEc2InstanceSubnetId": Sequence[StringFilterTypeDef],
        "ResourceAwsEc2InstanceLaunchedAt": Sequence[DateFilterTypeDef],
        "ResourceAwsS3BucketOwnerId": Sequence[StringFilterTypeDef],
        "ResourceAwsS3BucketOwnerName": Sequence[StringFilterTypeDef],
        "ResourceAwsIamAccessKeyUserName": Sequence[StringFilterTypeDef],
        "ResourceAwsIamAccessKeyPrincipalName": Sequence[StringFilterTypeDef],
        "ResourceAwsIamAccessKeyStatus": Sequence[StringFilterTypeDef],
        "ResourceAwsIamAccessKeyCreatedAt": Sequence[DateFilterTypeDef],
        "ResourceAwsIamUserUserName": Sequence[StringFilterTypeDef],
        "ResourceContainerName": Sequence[StringFilterTypeDef],
        "ResourceContainerImageId": Sequence[StringFilterTypeDef],
        "ResourceContainerImageName": Sequence[StringFilterTypeDef],
        "ResourceContainerLaunchedAt": Sequence[DateFilterTypeDef],
        "ResourceDetailsOther": Sequence[MapFilterTypeDef],
        "ComplianceStatus": Sequence[StringFilterTypeDef],
        "VerificationState": Sequence[StringFilterTypeDef],
        "WorkflowState": Sequence[StringFilterTypeDef],
        "WorkflowStatus": Sequence[StringFilterTypeDef],
        "RecordState": Sequence[StringFilterTypeDef],
        "RelatedFindingsProductArn": Sequence[StringFilterTypeDef],
        "RelatedFindingsId": Sequence[StringFilterTypeDef],
        "NoteText": Sequence[StringFilterTypeDef],
        "NoteUpdatedAt": Sequence[DateFilterTypeDef],
        "NoteUpdatedBy": Sequence[StringFilterTypeDef],
        "Keyword": Sequence[KeywordFilterTypeDef],
        "FindingProviderFieldsConfidence": Sequence[NumberFilterTypeDef],
        "FindingProviderFieldsCriticality": Sequence[NumberFilterTypeDef],
        "FindingProviderFieldsRelatedFindingsId": Sequence[StringFilterTypeDef],
        "FindingProviderFieldsRelatedFindingsProductArn": Sequence[StringFilterTypeDef],
        "FindingProviderFieldsSeverityLabel": Sequence[StringFilterTypeDef],
        "FindingProviderFieldsSeverityOriginal": Sequence[StringFilterTypeDef],
        "FindingProviderFieldsTypes": Sequence[StringFilterTypeDef],
        "Sample": Sequence[BooleanFilterTypeDef],
        "ComplianceSecurityControlId": Sequence[StringFilterTypeDef],
        "ComplianceAssociatedStandardsId": Sequence[StringFilterTypeDef],
    },
    total=False,
)

GetFindingHistoryResponseTypeDef = TypedDict(
    "GetFindingHistoryResponseTypeDef",
    {
        "Records": List[FindingHistoryRecordTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetInsightResultsResponseTypeDef = TypedDict(
    "GetInsightResultsResponseTypeDef",
    {
        "InsightResults": InsightResultsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

NetworkHeaderOutputTypeDef = TypedDict(
    "NetworkHeaderOutputTypeDef",
    {
        "Protocol": str,
        "Destination": NetworkPathComponentDetailsOutputTypeDef,
        "Source": NetworkPathComponentDetailsOutputTypeDef,
    },
)

NetworkHeaderTypeDef = TypedDict(
    "NetworkHeaderTypeDef",
    {
        "Protocol": str,
        "Destination": NetworkPathComponentDetailsTypeDef,
        "Source": NetworkPathComponentDetailsTypeDef,
    },
    total=False,
)

OccurrencesOutputTypeDef = TypedDict(
    "OccurrencesOutputTypeDef",
    {
        "LineRanges": List[RangeOutputTypeDef],
        "OffsetRanges": List[RangeOutputTypeDef],
        "Pages": List[PageOutputTypeDef],
        "Records": List[RecordOutputTypeDef],
        "Cells": List[CellOutputTypeDef],
    },
)

OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "LineRanges": Sequence[RangeTypeDef],
        "OffsetRanges": Sequence[RangeTypeDef],
        "Pages": Sequence[PageTypeDef],
        "Records": Sequence[RecordTypeDef],
        "Cells": Sequence[CellTypeDef],
    },
    total=False,
)

RuleGroupSourceStatelessRuleDefinitionOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleDefinitionOutputTypeDef",
    {
        "Actions": List[str],
        "MatchAttributes": RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef,
    },
)

RuleGroupSourceStatelessRuleDefinitionTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    {
        "Actions": Sequence[str],
        "MatchAttributes": RuleGroupSourceStatelessRuleMatchAttributesTypeDef,
    },
    total=False,
)

DescribeStandardsResponseTypeDef = TypedDict(
    "DescribeStandardsResponseTypeDef",
    {
        "Standards": List[StandardTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchGetStandardsControlAssociationsResponseTypeDef = TypedDict(
    "BatchGetStandardsControlAssociationsResponseTypeDef",
    {
        "StandardsControlAssociationDetails": List[StandardsControlAssociationDetailTypeDef],
        "UnprocessedAssociations": List[UnprocessedStandardsControlAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchUpdateStandardsControlAssociationsResponseTypeDef = TypedDict(
    "BatchUpdateStandardsControlAssociationsResponseTypeDef",
    {
        "UnprocessedAssociationUpdates": List[UnprocessedStandardsControlAssociationUpdateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchDisableStandardsResponseTypeDef = TypedDict(
    "BatchDisableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchEnableStandardsResponseTypeDef = TypedDict(
    "BatchEnableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetEnabledStandardsResponseTypeDef = TypedDict(
    "GetEnabledStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StatelessCustomActionDefinitionOutputTypeDef = TypedDict(
    "StatelessCustomActionDefinitionOutputTypeDef",
    {
        "PublishMetricAction": StatelessCustomPublishMetricActionOutputTypeDef,
    },
)

StatelessCustomActionDefinitionTypeDef = TypedDict(
    "StatelessCustomActionDefinitionTypeDef",
    {
        "PublishMetricAction": StatelessCustomPublishMetricActionTypeDef,
    },
    total=False,
)

PortProbeActionOutputTypeDef = TypedDict(
    "PortProbeActionOutputTypeDef",
    {
        "PortProbeDetails": List[PortProbeDetailOutputTypeDef],
        "Blocked": bool,
    },
)

PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "PortProbeDetails": Sequence[PortProbeDetailTypeDef],
        "Blocked": bool,
    },
    total=False,
)

AwsAthenaWorkGroupDetailsOutputTypeDef = TypedDict(
    "AwsAthenaWorkGroupDetailsOutputTypeDef",
    {
        "Name": str,
        "Description": str,
        "State": str,
        "Configuration": AwsAthenaWorkGroupConfigurationDetailsOutputTypeDef,
    },
)

AwsAthenaWorkGroupDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupDetailsTypeDef",
    {
        "Name": str,
        "Description": str,
        "State": str,
        "Configuration": AwsAthenaWorkGroupConfigurationDetailsTypeDef,
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef",
    {
        "LaunchConfigurationName": str,
        "LoadBalancerNames": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "CreatedTime": str,
        "MixedInstancesPolicy": (
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef
        ),
        "AvailabilityZones": List[
            AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsOutputTypeDef
        ],
        "LaunchTemplate": (
            AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationOutputTypeDef
        ),
        "CapacityRebalance": bool,
    },
)

AwsAutoScalingAutoScalingGroupDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    {
        "LaunchConfigurationName": str,
        "LoadBalancerNames": Sequence[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "CreatedTime": str,
        "MixedInstancesPolicy": AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef,
        "AvailabilityZones": Sequence[
            AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef
        ],
        "LaunchTemplate": (
            AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef
        ),
        "CapacityRebalance": bool,
    },
    total=False,
)

AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef",
    {
        "BackupPlanName": str,
        "AdvancedBackupSettings": List[
            AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef
        ],
        "BackupPlanRule": List[AwsBackupBackupPlanRuleDetailsOutputTypeDef],
    },
)

AwsBackupBackupPlanBackupPlanDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanBackupPlanDetailsTypeDef",
    {
        "BackupPlanName": str,
        "AdvancedBackupSettings": Sequence[AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef],
        "BackupPlanRule": Sequence[AwsBackupBackupPlanRuleDetailsTypeDef],
    },
    total=False,
)

AwsCertificateManagerCertificateDetailsOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsOutputTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": str,
        "DomainName": str,
        "DomainValidationOptions": List[
            AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef
        ],
        "ExtendedKeyUsages": List[AwsCertificateManagerCertificateExtendedKeyUsageOutputTypeDef],
        "FailureReason": str,
        "ImportedAt": str,
        "InUseBy": List[str],
        "IssuedAt": str,
        "Issuer": str,
        "KeyAlgorithm": str,
        "KeyUsages": List[AwsCertificateManagerCertificateKeyUsageOutputTypeDef],
        "NotAfter": str,
        "NotBefore": str,
        "Options": AwsCertificateManagerCertificateOptionsOutputTypeDef,
        "RenewalEligibility": str,
        "RenewalSummary": AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef,
        "Serial": str,
        "SignatureAlgorithm": str,
        "Status": str,
        "Subject": str,
        "SubjectAlternativeNames": List[str],
        "Type": str,
    },
)

AwsCertificateManagerCertificateDetailsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": str,
        "DomainName": str,
        "DomainValidationOptions": Sequence[
            AwsCertificateManagerCertificateDomainValidationOptionTypeDef
        ],
        "ExtendedKeyUsages": Sequence[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef],
        "FailureReason": str,
        "ImportedAt": str,
        "InUseBy": Sequence[str],
        "IssuedAt": str,
        "Issuer": str,
        "KeyAlgorithm": str,
        "KeyUsages": Sequence[AwsCertificateManagerCertificateKeyUsageTypeDef],
        "NotAfter": str,
        "NotBefore": str,
        "Options": AwsCertificateManagerCertificateOptionsTypeDef,
        "RenewalEligibility": str,
        "RenewalSummary": AwsCertificateManagerCertificateRenewalSummaryTypeDef,
        "Serial": str,
        "SignatureAlgorithm": str,
        "Status": str,
        "Subject": str,
        "SubjectAlternativeNames": Sequence[str],
        "Type": str,
    },
    total=False,
)

AwsCloudFrontDistributionOriginsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsOutputTypeDef",
    {
        "Items": List[AwsCloudFrontDistributionOriginItemOutputTypeDef],
    },
)

AwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsTypeDef",
    {
        "Items": Sequence[AwsCloudFrontDistributionOriginItemTypeDef],
    },
    total=False,
)

AwsCloudFrontDistributionOriginGroupsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsOutputTypeDef",
    {
        "Items": List[AwsCloudFrontDistributionOriginGroupOutputTypeDef],
    },
)

AwsCloudFrontDistributionOriginGroupsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    {
        "Items": Sequence[AwsCloudFrontDistributionOriginGroupTypeDef],
    },
    total=False,
)

AwsDynamoDbTableDetailsOutputTypeDef = TypedDict(
    "AwsDynamoDbTableDetailsOutputTypeDef",
    {
        "AttributeDefinitions": List[AwsDynamoDbTableAttributeDefinitionOutputTypeDef],
        "BillingModeSummary": AwsDynamoDbTableBillingModeSummaryOutputTypeDef,
        "CreationDateTime": str,
        "GlobalSecondaryIndexes": List[AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef],
        "GlobalTableVersion": str,
        "ItemCount": int,
        "KeySchema": List[AwsDynamoDbTableKeySchemaOutputTypeDef],
        "LatestStreamArn": str,
        "LatestStreamLabel": str,
        "LocalSecondaryIndexes": List[AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef],
        "ProvisionedThroughput": AwsDynamoDbTableProvisionedThroughputOutputTypeDef,
        "Replicas": List[AwsDynamoDbTableReplicaOutputTypeDef],
        "RestoreSummary": AwsDynamoDbTableRestoreSummaryOutputTypeDef,
        "SseDescription": AwsDynamoDbTableSseDescriptionOutputTypeDef,
        "StreamSpecification": AwsDynamoDbTableStreamSpecificationOutputTypeDef,
        "TableId": str,
        "TableName": str,
        "TableSizeBytes": int,
        "TableStatus": str,
    },
)

AwsDynamoDbTableDetailsTypeDef = TypedDict(
    "AwsDynamoDbTableDetailsTypeDef",
    {
        "AttributeDefinitions": Sequence[AwsDynamoDbTableAttributeDefinitionTypeDef],
        "BillingModeSummary": AwsDynamoDbTableBillingModeSummaryTypeDef,
        "CreationDateTime": str,
        "GlobalSecondaryIndexes": Sequence[AwsDynamoDbTableGlobalSecondaryIndexTypeDef],
        "GlobalTableVersion": str,
        "ItemCount": int,
        "KeySchema": Sequence[AwsDynamoDbTableKeySchemaTypeDef],
        "LatestStreamArn": str,
        "LatestStreamLabel": str,
        "LocalSecondaryIndexes": Sequence[AwsDynamoDbTableLocalSecondaryIndexTypeDef],
        "ProvisionedThroughput": AwsDynamoDbTableProvisionedThroughputTypeDef,
        "Replicas": Sequence[AwsDynamoDbTableReplicaTypeDef],
        "RestoreSummary": AwsDynamoDbTableRestoreSummaryTypeDef,
        "SseDescription": AwsDynamoDbTableSseDescriptionTypeDef,
        "StreamSpecification": AwsDynamoDbTableStreamSpecificationTypeDef,
        "TableId": str,
        "TableName": str,
        "TableSizeBytes": int,
        "TableStatus": str,
    },
    total=False,
)

AwsEc2LaunchTemplateDetailsOutputTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDetailsOutputTypeDef",
    {
        "LaunchTemplateName": str,
        "Id": str,
        "LaunchTemplateData": AwsEc2LaunchTemplateDataDetailsOutputTypeDef,
        "DefaultVersionNumber": int,
        "LatestVersionNumber": int,
    },
)

AwsEc2LaunchTemplateDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDetailsTypeDef",
    {
        "LaunchTemplateName": str,
        "Id": str,
        "LaunchTemplateData": AwsEc2LaunchTemplateDataDetailsTypeDef,
        "DefaultVersionNumber": int,
        "LatestVersionNumber": int,
    },
    total=False,
)

AwsEcsClusterDetailsOutputTypeDef = TypedDict(
    "AwsEcsClusterDetailsOutputTypeDef",
    {
        "ClusterArn": str,
        "ActiveServicesCount": int,
        "CapacityProviders": List[str],
        "ClusterSettings": List[AwsEcsClusterClusterSettingsDetailsOutputTypeDef],
        "Configuration": AwsEcsClusterConfigurationDetailsOutputTypeDef,
        "DefaultCapacityProviderStrategy": List[
            AwsEcsClusterDefaultCapacityProviderStrategyDetailsOutputTypeDef
        ],
        "ClusterName": str,
        "RegisteredContainerInstancesCount": int,
        "RunningTasksCount": int,
        "Status": str,
    },
)

AwsEcsClusterDetailsTypeDef = TypedDict(
    "AwsEcsClusterDetailsTypeDef",
    {
        "ClusterArn": str,
        "ActiveServicesCount": int,
        "CapacityProviders": Sequence[str],
        "ClusterSettings": Sequence[AwsEcsClusterClusterSettingsDetailsTypeDef],
        "Configuration": AwsEcsClusterConfigurationDetailsTypeDef,
        "DefaultCapacityProviderStrategy": Sequence[
            AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef
        ],
        "ClusterName": str,
        "RegisteredContainerInstancesCount": int,
        "RunningTasksCount": int,
        "Status": str,
    },
    total=False,
)

AwsEcsTaskDefinitionDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionDetailsOutputTypeDef",
    {
        "ContainerDefinitions": List[AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef],
        "Cpu": str,
        "ExecutionRoleArn": str,
        "Family": str,
        "InferenceAccelerators": List[
            AwsEcsTaskDefinitionInferenceAcceleratorsDetailsOutputTypeDef
        ],
        "IpcMode": str,
        "Memory": str,
        "NetworkMode": str,
        "PidMode": str,
        "PlacementConstraints": List[AwsEcsTaskDefinitionPlacementConstraintsDetailsOutputTypeDef],
        "ProxyConfiguration": AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef,
        "RequiresCompatibilities": List[str],
        "TaskRoleArn": str,
        "Volumes": List[AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef],
    },
)

AwsEcsTaskDefinitionDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionDetailsTypeDef",
    {
        "ContainerDefinitions": Sequence[AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef],
        "Cpu": str,
        "ExecutionRoleArn": str,
        "Family": str,
        "InferenceAccelerators": Sequence[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef],
        "IpcMode": str,
        "Memory": str,
        "NetworkMode": str,
        "PidMode": str,
        "PlacementConstraints": Sequence[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef],
        "ProxyConfiguration": AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef,
        "RequiresCompatibilities": Sequence[str],
        "TaskRoleArn": str,
        "Volumes": Sequence[AwsEcsTaskDefinitionVolumesDetailsTypeDef],
    },
    total=False,
)

AwsGuardDutyDetectorDataSourcesDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesDetailsOutputTypeDef",
    {
        "CloudTrail": AwsGuardDutyDetectorDataSourcesCloudTrailDetailsOutputTypeDef,
        "DnsLogs": AwsGuardDutyDetectorDataSourcesDnsLogsDetailsOutputTypeDef,
        "FlowLogs": AwsGuardDutyDetectorDataSourcesFlowLogsDetailsOutputTypeDef,
        "Kubernetes": AwsGuardDutyDetectorDataSourcesKubernetesDetailsOutputTypeDef,
        "MalwareProtection": AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsOutputTypeDef,
        "S3Logs": AwsGuardDutyDetectorDataSourcesS3LogsDetailsOutputTypeDef,
    },
)

AwsGuardDutyDetectorDataSourcesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesDetailsTypeDef",
    {
        "CloudTrail": AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef,
        "DnsLogs": AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef,
        "FlowLogs": AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef,
        "Kubernetes": AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef,
        "MalwareProtection": AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef,
        "S3Logs": AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef,
    },
    total=False,
)

AwsRdsDbInstanceDetailsOutputTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsOutputTypeDef",
    {
        "AssociatedRoles": List[AwsRdsDbInstanceAssociatedRoleOutputTypeDef],
        "CACertificateIdentifier": str,
        "DBClusterIdentifier": str,
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "DbInstancePort": int,
        "DbiResourceId": str,
        "DBName": str,
        "DeletionProtection": bool,
        "Endpoint": AwsRdsDbInstanceEndpointOutputTypeDef,
        "Engine": str,
        "EngineVersion": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "InstanceCreateTime": str,
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "StorageEncrypted": bool,
        "TdeCredentialArn": str,
        "VpcSecurityGroups": List[AwsRdsDbInstanceVpcSecurityGroupOutputTypeDef],
        "MultiAz": bool,
        "EnhancedMonitoringResourceArn": str,
        "DbInstanceStatus": str,
        "MasterUsername": str,
        "AllocatedStorage": int,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DbSecurityGroups": List[str],
        "DbParameterGroups": List[AwsRdsDbParameterGroupOutputTypeDef],
        "AvailabilityZone": str,
        "DbSubnetGroup": AwsRdsDbSubnetGroupOutputTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": AwsRdsDbPendingModifiedValuesOutputTypeDef,
        "LatestRestorableTime": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[AwsRdsDbOptionGroupMembershipOutputTypeDef],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "StatusInfos": List[AwsRdsDbStatusInfoOutputTypeDef],
        "StorageType": str,
        "DomainMemberships": List[AwsRdsDbDomainMembershipOutputTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "Timezone": str,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKmsKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudWatchLogsExports": List[str],
        "ProcessorFeatures": List[AwsRdsDbProcessorFeatureOutputTypeDef],
        "ListenerEndpoint": AwsRdsDbInstanceEndpointOutputTypeDef,
        "MaxAllocatedStorage": int,
    },
)

AwsRdsDbInstanceDetailsTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsTypeDef",
    {
        "AssociatedRoles": Sequence[AwsRdsDbInstanceAssociatedRoleTypeDef],
        "CACertificateIdentifier": str,
        "DBClusterIdentifier": str,
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "DbInstancePort": int,
        "DbiResourceId": str,
        "DBName": str,
        "DeletionProtection": bool,
        "Endpoint": AwsRdsDbInstanceEndpointTypeDef,
        "Engine": str,
        "EngineVersion": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "InstanceCreateTime": str,
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "StorageEncrypted": bool,
        "TdeCredentialArn": str,
        "VpcSecurityGroups": Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef],
        "MultiAz": bool,
        "EnhancedMonitoringResourceArn": str,
        "DbInstanceStatus": str,
        "MasterUsername": str,
        "AllocatedStorage": int,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DbSecurityGroups": Sequence[str],
        "DbParameterGroups": Sequence[AwsRdsDbParameterGroupTypeDef],
        "AvailabilityZone": str,
        "DbSubnetGroup": AwsRdsDbSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": AwsRdsDbPendingModifiedValuesTypeDef,
        "LatestRestorableTime": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": Sequence[str],
        "ReadReplicaDBClusterIdentifiers": Sequence[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": Sequence[AwsRdsDbOptionGroupMembershipTypeDef],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "StatusInfos": Sequence[AwsRdsDbStatusInfoTypeDef],
        "StorageType": str,
        "DomainMemberships": Sequence[AwsRdsDbDomainMembershipTypeDef],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "Timezone": str,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKmsKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudWatchLogsExports": Sequence[str],
        "ProcessorFeatures": Sequence[AwsRdsDbProcessorFeatureTypeDef],
        "ListenerEndpoint": AwsRdsDbInstanceEndpointTypeDef,
        "MaxAllocatedStorage": int,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef",
    {
        "Predicate": (
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef
        ),
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    {
        "Predicate": AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef,
    },
    total=False,
)

AwsS3BucketNotificationConfigurationDetailOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailOutputTypeDef",
    {
        "Events": List[str],
        "Filter": AwsS3BucketNotificationConfigurationFilterOutputTypeDef,
        "Destination": str,
        "Type": str,
    },
)

AwsS3BucketNotificationConfigurationDetailTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    {
        "Events": Sequence[str],
        "Filter": AwsS3BucketNotificationConfigurationFilterTypeDef,
        "Destination": str,
        "Type": str,
    },
    total=False,
)

AwsStepFunctionStateMachineDetailsOutputTypeDef = TypedDict(
    "AwsStepFunctionStateMachineDetailsOutputTypeDef",
    {
        "Label": str,
        "LoggingConfiguration": AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef,
        "Name": str,
        "RoleArn": str,
        "StateMachineArn": str,
        "Status": str,
        "TracingConfiguration": AwsStepFunctionStateMachineTracingConfigurationDetailsOutputTypeDef,
        "Type": str,
    },
)

AwsStepFunctionStateMachineDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineDetailsTypeDef",
    {
        "Label": str,
        "LoggingConfiguration": AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef,
        "Name": str,
        "RoleArn": str,
        "StateMachineArn": str,
        "Status": str,
        "TracingConfiguration": AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef,
        "Type": str,
    },
    total=False,
)

AwsWafv2RulesActionDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RulesActionDetailsOutputTypeDef",
    {
        "Allow": AwsWafv2ActionAllowDetailsOutputTypeDef,
        "Block": AwsWafv2ActionBlockDetailsOutputTypeDef,
        "Captcha": AwsWafv2RulesActionCaptchaDetailsOutputTypeDef,
        "Count": AwsWafv2RulesActionCountDetailsOutputTypeDef,
    },
)

AwsWafv2WebAclActionDetailsOutputTypeDef = TypedDict(
    "AwsWafv2WebAclActionDetailsOutputTypeDef",
    {
        "Allow": AwsWafv2ActionAllowDetailsOutputTypeDef,
        "Block": AwsWafv2ActionBlockDetailsOutputTypeDef,
    },
)

AwsWafv2RulesActionDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionDetailsTypeDef",
    {
        "Allow": AwsWafv2ActionAllowDetailsTypeDef,
        "Block": AwsWafv2ActionBlockDetailsTypeDef,
        "Captcha": AwsWafv2RulesActionCaptchaDetailsTypeDef,
        "Count": AwsWafv2RulesActionCountDetailsTypeDef,
    },
    total=False,
)

AwsWafv2WebAclActionDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclActionDetailsTypeDef",
    {
        "Allow": AwsWafv2ActionAllowDetailsTypeDef,
        "Block": AwsWafv2ActionBlockDetailsTypeDef,
    },
    total=False,
)

AutomationRulesConfigTypeDef = TypedDict(
    "AutomationRulesConfigTypeDef",
    {
        "RuleArn": str,
        "RuleStatus": RuleStatusType,
        "RuleOrder": int,
        "RuleName": str,
        "Description": str,
        "IsTerminal": bool,
        "Criteria": AutomationRulesFindingFiltersOutputTypeDef,
        "Actions": List[AutomationRulesActionOutputTypeDef],
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "CreatedBy": str,
    },
)

InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": AwsSecurityFindingFiltersOutputTypeDef,
        "GroupByAttribute": str,
    },
)

_RequiredCreateAutomationRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAutomationRuleRequestRequestTypeDef",
    {
        "RuleOrder": int,
        "RuleName": str,
        "Description": str,
        "Criteria": AutomationRulesFindingFiltersTypeDef,
        "Actions": Sequence[AutomationRulesActionTypeDef],
    },
)
_OptionalCreateAutomationRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAutomationRuleRequestRequestTypeDef",
    {
        "Tags": Mapping[str, str],
        "RuleStatus": RuleStatusType,
        "IsTerminal": bool,
    },
    total=False,
)


class CreateAutomationRuleRequestRequestTypeDef(
    _RequiredCreateAutomationRuleRequestRequestTypeDef,
    _OptionalCreateAutomationRuleRequestRequestTypeDef,
):
    pass


_RequiredUpdateAutomationRulesRequestItemTypeDef = TypedDict(
    "_RequiredUpdateAutomationRulesRequestItemTypeDef",
    {
        "RuleArn": str,
    },
)
_OptionalUpdateAutomationRulesRequestItemTypeDef = TypedDict(
    "_OptionalUpdateAutomationRulesRequestItemTypeDef",
    {
        "RuleStatus": RuleStatusType,
        "RuleOrder": int,
        "Description": str,
        "RuleName": str,
        "IsTerminal": bool,
        "Criteria": AutomationRulesFindingFiltersTypeDef,
        "Actions": Sequence[AutomationRulesActionTypeDef],
    },
    total=False,
)


class UpdateAutomationRulesRequestItemTypeDef(
    _RequiredUpdateAutomationRulesRequestItemTypeDef,
    _OptionalUpdateAutomationRulesRequestItemTypeDef,
):
    pass


CreateInsightRequestRequestTypeDef = TypedDict(
    "CreateInsightRequestRequestTypeDef",
    {
        "Name": str,
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "GroupByAttribute": str,
    },
)

GetFindingsRequestGetFindingsPaginateTypeDef = TypedDict(
    "GetFindingsRequestGetFindingsPaginateTypeDef",
    {
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "SortCriteria": Sequence[SortCriterionTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "SortCriteria": Sequence[SortCriterionTypeDef],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsRequestRequestTypeDef",
    {
        "Filters": AwsSecurityFindingFiltersTypeDef,
    },
)
_OptionalUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsRequestRequestTypeDef",
    {
        "Note": NoteUpdateTypeDef,
        "RecordState": RecordStateType,
    },
    total=False,
)


class UpdateFindingsRequestRequestTypeDef(
    _RequiredUpdateFindingsRequestRequestTypeDef, _OptionalUpdateFindingsRequestRequestTypeDef
):
    pass


_RequiredUpdateInsightRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)
_OptionalUpdateInsightRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInsightRequestRequestTypeDef",
    {
        "Name": str,
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "GroupByAttribute": str,
    },
    total=False,
)


class UpdateInsightRequestRequestTypeDef(
    _RequiredUpdateInsightRequestRequestTypeDef, _OptionalUpdateInsightRequestRequestTypeDef
):
    pass


NetworkPathComponentOutputTypeDef = TypedDict(
    "NetworkPathComponentOutputTypeDef",
    {
        "ComponentId": str,
        "ComponentType": str,
        "Egress": NetworkHeaderOutputTypeDef,
        "Ingress": NetworkHeaderOutputTypeDef,
    },
)

NetworkPathComponentTypeDef = TypedDict(
    "NetworkPathComponentTypeDef",
    {
        "ComponentId": str,
        "ComponentType": str,
        "Egress": NetworkHeaderTypeDef,
        "Ingress": NetworkHeaderTypeDef,
    },
    total=False,
)

CustomDataIdentifiersDetectionsOutputTypeDef = TypedDict(
    "CustomDataIdentifiersDetectionsOutputTypeDef",
    {
        "Count": int,
        "Arn": str,
        "Name": str,
        "Occurrences": OccurrencesOutputTypeDef,
    },
)

SensitiveDataDetectionsOutputTypeDef = TypedDict(
    "SensitiveDataDetectionsOutputTypeDef",
    {
        "Count": int,
        "Type": str,
        "Occurrences": OccurrencesOutputTypeDef,
    },
)

CustomDataIdentifiersDetectionsTypeDef = TypedDict(
    "CustomDataIdentifiersDetectionsTypeDef",
    {
        "Count": int,
        "Arn": str,
        "Name": str,
        "Occurrences": OccurrencesTypeDef,
    },
    total=False,
)

SensitiveDataDetectionsTypeDef = TypedDict(
    "SensitiveDataDetectionsTypeDef",
    {
        "Count": int,
        "Type": str,
        "Occurrences": OccurrencesTypeDef,
    },
    total=False,
)

RuleGroupSourceStatelessRulesDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesDetailsOutputTypeDef",
    {
        "Priority": int,
        "RuleDefinition": RuleGroupSourceStatelessRuleDefinitionOutputTypeDef,
    },
)

RuleGroupSourceStatelessRulesDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    {
        "Priority": int,
        "RuleDefinition": RuleGroupSourceStatelessRuleDefinitionTypeDef,
    },
    total=False,
)

FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef = TypedDict(
    "FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef",
    {
        "ActionDefinition": StatelessCustomActionDefinitionOutputTypeDef,
        "ActionName": str,
    },
)

RuleGroupSourceCustomActionsDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceCustomActionsDetailsOutputTypeDef",
    {
        "ActionDefinition": StatelessCustomActionDefinitionOutputTypeDef,
        "ActionName": str,
    },
)

FirewallPolicyStatelessCustomActionsDetailsTypeDef = TypedDict(
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    {
        "ActionDefinition": StatelessCustomActionDefinitionTypeDef,
        "ActionName": str,
    },
    total=False,
)

RuleGroupSourceCustomActionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    {
        "ActionDefinition": StatelessCustomActionDefinitionTypeDef,
        "ActionName": str,
    },
    total=False,
)

ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "ActionType": str,
        "NetworkConnectionAction": NetworkConnectionActionOutputTypeDef,
        "AwsApiCallAction": AwsApiCallActionOutputTypeDef,
        "DnsRequestAction": DnsRequestActionOutputTypeDef,
        "PortProbeAction": PortProbeActionOutputTypeDef,
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": str,
        "NetworkConnectionAction": NetworkConnectionActionTypeDef,
        "AwsApiCallAction": AwsApiCallActionTypeDef,
        "DnsRequestAction": DnsRequestActionTypeDef,
        "PortProbeAction": PortProbeActionTypeDef,
    },
    total=False,
)

AwsBackupBackupPlanDetailsOutputTypeDef = TypedDict(
    "AwsBackupBackupPlanDetailsOutputTypeDef",
    {
        "BackupPlan": AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef,
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "VersionId": str,
    },
)

AwsBackupBackupPlanDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanDetailsTypeDef",
    {
        "BackupPlan": AwsBackupBackupPlanBackupPlanDetailsTypeDef,
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "VersionId": str,
    },
    total=False,
)

AwsCloudFrontDistributionDetailsOutputTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsOutputTypeDef",
    {
        "CacheBehaviors": AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef,
        "DefaultCacheBehavior": AwsCloudFrontDistributionDefaultCacheBehaviorOutputTypeDef,
        "DefaultRootObject": str,
        "DomainName": str,
        "ETag": str,
        "LastModifiedTime": str,
        "Logging": AwsCloudFrontDistributionLoggingOutputTypeDef,
        "Origins": AwsCloudFrontDistributionOriginsOutputTypeDef,
        "OriginGroups": AwsCloudFrontDistributionOriginGroupsOutputTypeDef,
        "ViewerCertificate": AwsCloudFrontDistributionViewerCertificateOutputTypeDef,
        "Status": str,
        "WebAclId": str,
    },
)

AwsCloudFrontDistributionDetailsTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsTypeDef",
    {
        "CacheBehaviors": AwsCloudFrontDistributionCacheBehaviorsTypeDef,
        "DefaultCacheBehavior": AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef,
        "DefaultRootObject": str,
        "DomainName": str,
        "ETag": str,
        "LastModifiedTime": str,
        "Logging": AwsCloudFrontDistributionLoggingTypeDef,
        "Origins": AwsCloudFrontDistributionOriginsTypeDef,
        "OriginGroups": AwsCloudFrontDistributionOriginGroupsTypeDef,
        "ViewerCertificate": AwsCloudFrontDistributionViewerCertificateTypeDef,
        "Status": str,
        "WebAclId": str,
    },
    total=False,
)

AwsGuardDutyDetectorDetailsOutputTypeDef = TypedDict(
    "AwsGuardDutyDetectorDetailsOutputTypeDef",
    {
        "DataSources": AwsGuardDutyDetectorDataSourcesDetailsOutputTypeDef,
        "Features": List[AwsGuardDutyDetectorFeaturesDetailsOutputTypeDef],
        "FindingPublishingFrequency": str,
        "ServiceRole": str,
        "Status": str,
    },
)

AwsGuardDutyDetectorDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDetailsTypeDef",
    {
        "DataSources": AwsGuardDutyDetectorDataSourcesDetailsTypeDef,
        "Features": Sequence[AwsGuardDutyDetectorFeaturesDetailsTypeDef],
        "FindingPublishingFrequency": str,
        "ServiceRole": str,
        "Status": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef",
    {
        "AbortIncompleteMultipartUpload": AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsOutputTypeDef,
        "ExpirationDate": str,
        "ExpirationInDays": int,
        "ExpiredObjectDeleteMarker": bool,
        "Filter": AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef,
        "ID": str,
        "NoncurrentVersionExpirationInDays": int,
        "NoncurrentVersionTransitions": List[
            AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsOutputTypeDef
        ],
        "Prefix": str,
        "Status": str,
        "Transitions": List[
            AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsOutputTypeDef
        ],
    },
)

AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    {
        "AbortIncompleteMultipartUpload": (
            AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef
        ),
        "ExpirationDate": str,
        "ExpirationInDays": int,
        "ExpiredObjectDeleteMarker": bool,
        "Filter": AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef,
        "ID": str,
        "NoncurrentVersionExpirationInDays": int,
        "NoncurrentVersionTransitions": Sequence[
            AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef
        ],
        "Prefix": str,
        "Status": str,
        "Transitions": Sequence[
            AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef
        ],
    },
    total=False,
)

AwsS3BucketNotificationConfigurationOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationOutputTypeDef",
    {
        "Configurations": List[AwsS3BucketNotificationConfigurationDetailOutputTypeDef],
    },
)

AwsS3BucketNotificationConfigurationTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationTypeDef",
    {
        "Configurations": Sequence[AwsS3BucketNotificationConfigurationDetailTypeDef],
    },
    total=False,
)

AwsWafv2RulesDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RulesDetailsOutputTypeDef",
    {
        "Action": AwsWafv2RulesActionDetailsOutputTypeDef,
        "Name": str,
        "OverrideAction": str,
        "Priority": int,
        "VisibilityConfig": AwsWafv2VisibilityConfigDetailsOutputTypeDef,
    },
)

AwsWafv2RulesDetailsTypeDef = TypedDict(
    "AwsWafv2RulesDetailsTypeDef",
    {
        "Action": AwsWafv2RulesActionDetailsTypeDef,
        "Name": str,
        "OverrideAction": str,
        "Priority": int,
        "VisibilityConfig": AwsWafv2VisibilityConfigDetailsTypeDef,
    },
    total=False,
)

BatchGetAutomationRulesResponseTypeDef = TypedDict(
    "BatchGetAutomationRulesResponseTypeDef",
    {
        "Rules": List[AutomationRulesConfigTypeDef],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetInsightsResponseTypeDef = TypedDict(
    "GetInsightsResponseTypeDef",
    {
        "Insights": List[InsightTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchUpdateAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchUpdateAutomationRulesRequestRequestTypeDef",
    {
        "UpdateAutomationRulesRequestItems": Sequence[UpdateAutomationRulesRequestItemTypeDef],
    },
)

CustomDataIdentifiersResultOutputTypeDef = TypedDict(
    "CustomDataIdentifiersResultOutputTypeDef",
    {
        "Detections": List[CustomDataIdentifiersDetectionsOutputTypeDef],
        "TotalCount": int,
    },
)

SensitiveDataResultOutputTypeDef = TypedDict(
    "SensitiveDataResultOutputTypeDef",
    {
        "Category": str,
        "Detections": List[SensitiveDataDetectionsOutputTypeDef],
        "TotalCount": int,
    },
)

CustomDataIdentifiersResultTypeDef = TypedDict(
    "CustomDataIdentifiersResultTypeDef",
    {
        "Detections": Sequence[CustomDataIdentifiersDetectionsTypeDef],
        "TotalCount": int,
    },
    total=False,
)

SensitiveDataResultTypeDef = TypedDict(
    "SensitiveDataResultTypeDef",
    {
        "Category": str,
        "Detections": Sequence[SensitiveDataDetectionsTypeDef],
        "TotalCount": int,
    },
    total=False,
)

FirewallPolicyDetailsOutputTypeDef = TypedDict(
    "FirewallPolicyDetailsOutputTypeDef",
    {
        "StatefulRuleGroupReferences": List[
            FirewallPolicyStatefulRuleGroupReferencesDetailsOutputTypeDef
        ],
        "StatelessCustomActions": List[FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef],
        "StatelessDefaultActions": List[str],
        "StatelessFragmentDefaultActions": List[str],
        "StatelessRuleGroupReferences": List[
            FirewallPolicyStatelessRuleGroupReferencesDetailsOutputTypeDef
        ],
    },
)

RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef",
    {
        "CustomActions": List[RuleGroupSourceCustomActionsDetailsOutputTypeDef],
        "StatelessRules": List[RuleGroupSourceStatelessRulesDetailsOutputTypeDef],
    },
)

FirewallPolicyDetailsTypeDef = TypedDict(
    "FirewallPolicyDetailsTypeDef",
    {
        "StatefulRuleGroupReferences": Sequence[
            FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef
        ],
        "StatelessCustomActions": Sequence[FirewallPolicyStatelessCustomActionsDetailsTypeDef],
        "StatelessDefaultActions": Sequence[str],
        "StatelessFragmentDefaultActions": Sequence[str],
        "StatelessRuleGroupReferences": Sequence[
            FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef
        ],
    },
    total=False,
)

RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    {
        "CustomActions": Sequence[RuleGroupSourceCustomActionsDetailsTypeDef],
        "StatelessRules": Sequence[RuleGroupSourceStatelessRulesDetailsTypeDef],
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef",
    {
        "Rules": List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef],
    },
)

AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    {
        "Rules": Sequence[AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef],
    },
    total=False,
)

AwsWafv2RuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsWafv2RuleGroupDetailsOutputTypeDef",
    {
        "Capacity": int,
        "Description": str,
        "Id": str,
        "Name": str,
        "Arn": str,
        "Rules": List[AwsWafv2RulesDetailsOutputTypeDef],
        "Scope": str,
        "VisibilityConfig": AwsWafv2VisibilityConfigDetailsOutputTypeDef,
    },
)

AwsWafv2WebAclDetailsOutputTypeDef = TypedDict(
    "AwsWafv2WebAclDetailsOutputTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ManagedbyFirewallManager": bool,
        "Id": str,
        "Capacity": int,
        "CaptchaConfig": AwsWafv2WebAclCaptchaConfigDetailsOutputTypeDef,
        "DefaultAction": AwsWafv2WebAclActionDetailsOutputTypeDef,
        "Description": str,
        "Rules": List[AwsWafv2RulesDetailsOutputTypeDef],
        "VisibilityConfig": AwsWafv2VisibilityConfigDetailsOutputTypeDef,
    },
)

AwsWafv2RuleGroupDetailsTypeDef = TypedDict(
    "AwsWafv2RuleGroupDetailsTypeDef",
    {
        "Capacity": int,
        "Description": str,
        "Id": str,
        "Name": str,
        "Arn": str,
        "Rules": Sequence[AwsWafv2RulesDetailsTypeDef],
        "Scope": str,
        "VisibilityConfig": AwsWafv2VisibilityConfigDetailsTypeDef,
    },
    total=False,
)

AwsWafv2WebAclDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclDetailsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ManagedbyFirewallManager": bool,
        "Id": str,
        "Capacity": int,
        "CaptchaConfig": AwsWafv2WebAclCaptchaConfigDetailsTypeDef,
        "DefaultAction": AwsWafv2WebAclActionDetailsTypeDef,
        "Description": str,
        "Rules": Sequence[AwsWafv2RulesDetailsTypeDef],
        "VisibilityConfig": AwsWafv2VisibilityConfigDetailsTypeDef,
    },
    total=False,
)

ClassificationResultOutputTypeDef = TypedDict(
    "ClassificationResultOutputTypeDef",
    {
        "MimeType": str,
        "SizeClassified": int,
        "AdditionalOccurrences": bool,
        "Status": ClassificationStatusOutputTypeDef,
        "SensitiveData": List[SensitiveDataResultOutputTypeDef],
        "CustomDataIdentifiers": CustomDataIdentifiersResultOutputTypeDef,
    },
)

ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "MimeType": str,
        "SizeClassified": int,
        "AdditionalOccurrences": bool,
        "Status": ClassificationStatusTypeDef,
        "SensitiveData": Sequence[SensitiveDataResultTypeDef],
        "CustomDataIdentifiers": CustomDataIdentifiersResultTypeDef,
    },
    total=False,
)

AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef",
    {
        "FirewallPolicy": FirewallPolicyDetailsOutputTypeDef,
        "FirewallPolicyArn": str,
        "FirewallPolicyId": str,
        "FirewallPolicyName": str,
        "Description": str,
    },
)

RuleGroupSourceOutputTypeDef = TypedDict(
    "RuleGroupSourceOutputTypeDef",
    {
        "RulesSourceList": RuleGroupSourceListDetailsOutputTypeDef,
        "RulesString": str,
        "StatefulRules": List[RuleGroupSourceStatefulRulesDetailsOutputTypeDef],
        "StatelessRulesAndCustomActions": (
            RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef
        ),
    },
)

AwsNetworkFirewallFirewallPolicyDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    {
        "FirewallPolicy": FirewallPolicyDetailsTypeDef,
        "FirewallPolicyArn": str,
        "FirewallPolicyId": str,
        "FirewallPolicyName": str,
        "Description": str,
    },
    total=False,
)

RuleGroupSourceTypeDef = TypedDict(
    "RuleGroupSourceTypeDef",
    {
        "RulesSourceList": RuleGroupSourceListDetailsTypeDef,
        "RulesString": str,
        "StatefulRules": Sequence[RuleGroupSourceStatefulRulesDetailsTypeDef],
        "StatelessRulesAndCustomActions": (
            RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef
        ),
    },
    total=False,
)

AwsS3BucketDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketDetailsOutputTypeDef",
    {
        "OwnerId": str,
        "OwnerName": str,
        "OwnerAccountId": str,
        "CreatedAt": str,
        "ServerSideEncryptionConfiguration": (
            AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef
        ),
        "BucketLifecycleConfiguration": AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef,
        "PublicAccessBlockConfiguration": AwsS3AccountPublicAccessBlockDetailsOutputTypeDef,
        "AccessControlList": str,
        "BucketLoggingConfiguration": AwsS3BucketLoggingConfigurationOutputTypeDef,
        "BucketWebsiteConfiguration": AwsS3BucketWebsiteConfigurationOutputTypeDef,
        "BucketNotificationConfiguration": AwsS3BucketNotificationConfigurationOutputTypeDef,
        "BucketVersioningConfiguration": AwsS3BucketBucketVersioningConfigurationOutputTypeDef,
        "ObjectLockConfiguration": AwsS3BucketObjectLockConfigurationOutputTypeDef,
    },
)

AwsS3BucketDetailsTypeDef = TypedDict(
    "AwsS3BucketDetailsTypeDef",
    {
        "OwnerId": str,
        "OwnerName": str,
        "OwnerAccountId": str,
        "CreatedAt": str,
        "ServerSideEncryptionConfiguration": AwsS3BucketServerSideEncryptionConfigurationTypeDef,
        "BucketLifecycleConfiguration": AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef,
        "PublicAccessBlockConfiguration": AwsS3AccountPublicAccessBlockDetailsTypeDef,
        "AccessControlList": str,
        "BucketLoggingConfiguration": AwsS3BucketLoggingConfigurationTypeDef,
        "BucketWebsiteConfiguration": AwsS3BucketWebsiteConfigurationTypeDef,
        "BucketNotificationConfiguration": AwsS3BucketNotificationConfigurationTypeDef,
        "BucketVersioningConfiguration": AwsS3BucketBucketVersioningConfigurationTypeDef,
        "ObjectLockConfiguration": AwsS3BucketObjectLockConfigurationTypeDef,
    },
    total=False,
)

DataClassificationDetailsOutputTypeDef = TypedDict(
    "DataClassificationDetailsOutputTypeDef",
    {
        "DetailedResultsLocation": str,
        "Result": ClassificationResultOutputTypeDef,
    },
)

DataClassificationDetailsTypeDef = TypedDict(
    "DataClassificationDetailsTypeDef",
    {
        "DetailedResultsLocation": str,
        "Result": ClassificationResultTypeDef,
    },
    total=False,
)

RuleGroupDetailsOutputTypeDef = TypedDict(
    "RuleGroupDetailsOutputTypeDef",
    {
        "RuleVariables": RuleGroupVariablesOutputTypeDef,
        "RulesSource": RuleGroupSourceOutputTypeDef,
    },
)

RuleGroupDetailsTypeDef = TypedDict(
    "RuleGroupDetailsTypeDef",
    {
        "RuleVariables": RuleGroupVariablesTypeDef,
        "RulesSource": RuleGroupSourceTypeDef,
    },
    total=False,
)

AwsNetworkFirewallRuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsOutputTypeDef",
    {
        "Capacity": int,
        "Description": str,
        "RuleGroup": RuleGroupDetailsOutputTypeDef,
        "RuleGroupArn": str,
        "RuleGroupId": str,
        "RuleGroupName": str,
        "Type": str,
    },
)

AwsNetworkFirewallRuleGroupDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    {
        "Capacity": int,
        "Description": str,
        "RuleGroup": RuleGroupDetailsTypeDef,
        "RuleGroupArn": str,
        "RuleGroupId": str,
        "RuleGroupName": str,
        "Type": str,
    },
    total=False,
)

ResourceDetailsOutputTypeDef = TypedDict(
    "ResourceDetailsOutputTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef,
        "AwsCodeBuildProject": AwsCodeBuildProjectDetailsOutputTypeDef,
        "AwsCloudFrontDistribution": AwsCloudFrontDistributionDetailsOutputTypeDef,
        "AwsEc2Instance": AwsEc2InstanceDetailsOutputTypeDef,
        "AwsEc2NetworkInterface": AwsEc2NetworkInterfaceDetailsOutputTypeDef,
        "AwsEc2SecurityGroup": AwsEc2SecurityGroupDetailsOutputTypeDef,
        "AwsEc2Volume": AwsEc2VolumeDetailsOutputTypeDef,
        "AwsEc2Vpc": AwsEc2VpcDetailsOutputTypeDef,
        "AwsEc2Eip": AwsEc2EipDetailsOutputTypeDef,
        "AwsEc2Subnet": AwsEc2SubnetDetailsOutputTypeDef,
        "AwsEc2NetworkAcl": AwsEc2NetworkAclDetailsOutputTypeDef,
        "AwsElbv2LoadBalancer": AwsElbv2LoadBalancerDetailsOutputTypeDef,
        "AwsElasticBeanstalkEnvironment": AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef,
        "AwsElasticsearchDomain": AwsElasticsearchDomainDetailsOutputTypeDef,
        "AwsS3Bucket": AwsS3BucketDetailsOutputTypeDef,
        "AwsS3AccountPublicAccessBlock": AwsS3AccountPublicAccessBlockDetailsOutputTypeDef,
        "AwsS3Object": AwsS3ObjectDetailsOutputTypeDef,
        "AwsSecretsManagerSecret": AwsSecretsManagerSecretDetailsOutputTypeDef,
        "AwsIamAccessKey": AwsIamAccessKeyDetailsOutputTypeDef,
        "AwsIamUser": AwsIamUserDetailsOutputTypeDef,
        "AwsIamPolicy": AwsIamPolicyDetailsOutputTypeDef,
        "AwsApiGatewayV2Stage": AwsApiGatewayV2StageDetailsOutputTypeDef,
        "AwsApiGatewayV2Api": AwsApiGatewayV2ApiDetailsOutputTypeDef,
        "AwsDynamoDbTable": AwsDynamoDbTableDetailsOutputTypeDef,
        "AwsApiGatewayStage": AwsApiGatewayStageDetailsOutputTypeDef,
        "AwsApiGatewayRestApi": AwsApiGatewayRestApiDetailsOutputTypeDef,
        "AwsCloudTrailTrail": AwsCloudTrailTrailDetailsOutputTypeDef,
        "AwsSsmPatchCompliance": AwsSsmPatchComplianceDetailsOutputTypeDef,
        "AwsCertificateManagerCertificate": AwsCertificateManagerCertificateDetailsOutputTypeDef,
        "AwsRedshiftCluster": AwsRedshiftClusterDetailsOutputTypeDef,
        "AwsElbLoadBalancer": AwsElbLoadBalancerDetailsOutputTypeDef,
        "AwsIamGroup": AwsIamGroupDetailsOutputTypeDef,
        "AwsIamRole": AwsIamRoleDetailsOutputTypeDef,
        "AwsKmsKey": AwsKmsKeyDetailsOutputTypeDef,
        "AwsLambdaFunction": AwsLambdaFunctionDetailsOutputTypeDef,
        "AwsLambdaLayerVersion": AwsLambdaLayerVersionDetailsOutputTypeDef,
        "AwsRdsDbInstance": AwsRdsDbInstanceDetailsOutputTypeDef,
        "AwsSnsTopic": AwsSnsTopicDetailsOutputTypeDef,
        "AwsSqsQueue": AwsSqsQueueDetailsOutputTypeDef,
        "AwsWafWebAcl": AwsWafWebAclDetailsOutputTypeDef,
        "AwsRdsDbSnapshot": AwsRdsDbSnapshotDetailsOutputTypeDef,
        "AwsRdsDbClusterSnapshot": AwsRdsDbClusterSnapshotDetailsOutputTypeDef,
        "AwsRdsDbCluster": AwsRdsDbClusterDetailsOutputTypeDef,
        "AwsEcsCluster": AwsEcsClusterDetailsOutputTypeDef,
        "AwsEcsContainer": AwsEcsContainerDetailsOutputTypeDef,
        "AwsEcsTaskDefinition": AwsEcsTaskDefinitionDetailsOutputTypeDef,
        "Container": ContainerDetailsOutputTypeDef,
        "Other": Dict[str, str],
        "AwsRdsEventSubscription": AwsRdsEventSubscriptionDetailsOutputTypeDef,
        "AwsEcsService": AwsEcsServiceDetailsOutputTypeDef,
        "AwsAutoScalingLaunchConfiguration": AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef,
        "AwsEc2VpnConnection": AwsEc2VpnConnectionDetailsOutputTypeDef,
        "AwsEcrContainerImage": AwsEcrContainerImageDetailsOutputTypeDef,
        "AwsOpenSearchServiceDomain": AwsOpenSearchServiceDomainDetailsOutputTypeDef,
        "AwsEc2VpcEndpointService": AwsEc2VpcEndpointServiceDetailsOutputTypeDef,
        "AwsXrayEncryptionConfig": AwsXrayEncryptionConfigDetailsOutputTypeDef,
        "AwsWafRateBasedRule": AwsWafRateBasedRuleDetailsOutputTypeDef,
        "AwsWafRegionalRateBasedRule": AwsWafRegionalRateBasedRuleDetailsOutputTypeDef,
        "AwsEcrRepository": AwsEcrRepositoryDetailsOutputTypeDef,
        "AwsEksCluster": AwsEksClusterDetailsOutputTypeDef,
        "AwsNetworkFirewallFirewallPolicy": AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef,
        "AwsNetworkFirewallFirewall": AwsNetworkFirewallFirewallDetailsOutputTypeDef,
        "AwsNetworkFirewallRuleGroup": AwsNetworkFirewallRuleGroupDetailsOutputTypeDef,
        "AwsRdsDbSecurityGroup": AwsRdsDbSecurityGroupDetailsOutputTypeDef,
        "AwsKinesisStream": AwsKinesisStreamDetailsOutputTypeDef,
        "AwsEc2TransitGateway": AwsEc2TransitGatewayDetailsOutputTypeDef,
        "AwsEfsAccessPoint": AwsEfsAccessPointDetailsOutputTypeDef,
        "AwsCloudFormationStack": AwsCloudFormationStackDetailsOutputTypeDef,
        "AwsCloudWatchAlarm": AwsCloudWatchAlarmDetailsOutputTypeDef,
        "AwsEc2VpcPeeringConnection": AwsEc2VpcPeeringConnectionDetailsOutputTypeDef,
        "AwsWafRegionalRuleGroup": AwsWafRegionalRuleGroupDetailsOutputTypeDef,
        "AwsWafRegionalRule": AwsWafRegionalRuleDetailsOutputTypeDef,
        "AwsWafRegionalWebAcl": AwsWafRegionalWebAclDetailsOutputTypeDef,
        "AwsWafRule": AwsWafRuleDetailsOutputTypeDef,
        "AwsWafRuleGroup": AwsWafRuleGroupDetailsOutputTypeDef,
        "AwsEcsTask": AwsEcsTaskDetailsOutputTypeDef,
        "AwsBackupBackupVault": AwsBackupBackupVaultDetailsOutputTypeDef,
        "AwsBackupBackupPlan": AwsBackupBackupPlanDetailsOutputTypeDef,
        "AwsBackupRecoveryPoint": AwsBackupRecoveryPointDetailsOutputTypeDef,
        "AwsEc2LaunchTemplate": AwsEc2LaunchTemplateDetailsOutputTypeDef,
        "AwsSageMakerNotebookInstance": AwsSageMakerNotebookInstanceDetailsOutputTypeDef,
        "AwsWafv2WebAcl": AwsWafv2WebAclDetailsOutputTypeDef,
        "AwsWafv2RuleGroup": AwsWafv2RuleGroupDetailsOutputTypeDef,
        "AwsEc2RouteTable": AwsEc2RouteTableDetailsOutputTypeDef,
        "AwsAmazonMqBroker": AwsAmazonMqBrokerDetailsOutputTypeDef,
        "AwsAppSyncGraphQlApi": AwsAppSyncGraphQlApiDetailsOutputTypeDef,
        "AwsEventSchemasRegistry": AwsEventSchemasRegistryDetailsOutputTypeDef,
        "AwsGuardDutyDetector": AwsGuardDutyDetectorDetailsOutputTypeDef,
        "AwsStepFunctionStateMachine": AwsStepFunctionStateMachineDetailsOutputTypeDef,
        "AwsAthenaWorkGroup": AwsAthenaWorkGroupDetailsOutputTypeDef,
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": AwsAutoScalingAutoScalingGroupDetailsTypeDef,
        "AwsCodeBuildProject": AwsCodeBuildProjectDetailsTypeDef,
        "AwsCloudFrontDistribution": AwsCloudFrontDistributionDetailsTypeDef,
        "AwsEc2Instance": AwsEc2InstanceDetailsTypeDef,
        "AwsEc2NetworkInterface": AwsEc2NetworkInterfaceDetailsTypeDef,
        "AwsEc2SecurityGroup": AwsEc2SecurityGroupDetailsTypeDef,
        "AwsEc2Volume": AwsEc2VolumeDetailsTypeDef,
        "AwsEc2Vpc": AwsEc2VpcDetailsTypeDef,
        "AwsEc2Eip": AwsEc2EipDetailsTypeDef,
        "AwsEc2Subnet": AwsEc2SubnetDetailsTypeDef,
        "AwsEc2NetworkAcl": AwsEc2NetworkAclDetailsTypeDef,
        "AwsElbv2LoadBalancer": AwsElbv2LoadBalancerDetailsTypeDef,
        "AwsElasticBeanstalkEnvironment": AwsElasticBeanstalkEnvironmentDetailsTypeDef,
        "AwsElasticsearchDomain": AwsElasticsearchDomainDetailsTypeDef,
        "AwsS3Bucket": AwsS3BucketDetailsTypeDef,
        "AwsS3AccountPublicAccessBlock": AwsS3AccountPublicAccessBlockDetailsTypeDef,
        "AwsS3Object": AwsS3ObjectDetailsTypeDef,
        "AwsSecretsManagerSecret": AwsSecretsManagerSecretDetailsTypeDef,
        "AwsIamAccessKey": AwsIamAccessKeyDetailsTypeDef,
        "AwsIamUser": AwsIamUserDetailsTypeDef,
        "AwsIamPolicy": AwsIamPolicyDetailsTypeDef,
        "AwsApiGatewayV2Stage": AwsApiGatewayV2StageDetailsTypeDef,
        "AwsApiGatewayV2Api": AwsApiGatewayV2ApiDetailsTypeDef,
        "AwsDynamoDbTable": AwsDynamoDbTableDetailsTypeDef,
        "AwsApiGatewayStage": AwsApiGatewayStageDetailsTypeDef,
        "AwsApiGatewayRestApi": AwsApiGatewayRestApiDetailsTypeDef,
        "AwsCloudTrailTrail": AwsCloudTrailTrailDetailsTypeDef,
        "AwsSsmPatchCompliance": AwsSsmPatchComplianceDetailsTypeDef,
        "AwsCertificateManagerCertificate": AwsCertificateManagerCertificateDetailsTypeDef,
        "AwsRedshiftCluster": AwsRedshiftClusterDetailsTypeDef,
        "AwsElbLoadBalancer": AwsElbLoadBalancerDetailsTypeDef,
        "AwsIamGroup": AwsIamGroupDetailsTypeDef,
        "AwsIamRole": AwsIamRoleDetailsTypeDef,
        "AwsKmsKey": AwsKmsKeyDetailsTypeDef,
        "AwsLambdaFunction": AwsLambdaFunctionDetailsTypeDef,
        "AwsLambdaLayerVersion": AwsLambdaLayerVersionDetailsTypeDef,
        "AwsRdsDbInstance": AwsRdsDbInstanceDetailsTypeDef,
        "AwsSnsTopic": AwsSnsTopicDetailsTypeDef,
        "AwsSqsQueue": AwsSqsQueueDetailsTypeDef,
        "AwsWafWebAcl": AwsWafWebAclDetailsTypeDef,
        "AwsRdsDbSnapshot": AwsRdsDbSnapshotDetailsTypeDef,
        "AwsRdsDbClusterSnapshot": AwsRdsDbClusterSnapshotDetailsTypeDef,
        "AwsRdsDbCluster": AwsRdsDbClusterDetailsTypeDef,
        "AwsEcsCluster": AwsEcsClusterDetailsTypeDef,
        "AwsEcsContainer": AwsEcsContainerDetailsTypeDef,
        "AwsEcsTaskDefinition": AwsEcsTaskDefinitionDetailsTypeDef,
        "Container": ContainerDetailsTypeDef,
        "Other": Mapping[str, str],
        "AwsRdsEventSubscription": AwsRdsEventSubscriptionDetailsTypeDef,
        "AwsEcsService": AwsEcsServiceDetailsTypeDef,
        "AwsAutoScalingLaunchConfiguration": AwsAutoScalingLaunchConfigurationDetailsTypeDef,
        "AwsEc2VpnConnection": AwsEc2VpnConnectionDetailsTypeDef,
        "AwsEcrContainerImage": AwsEcrContainerImageDetailsTypeDef,
        "AwsOpenSearchServiceDomain": AwsOpenSearchServiceDomainDetailsTypeDef,
        "AwsEc2VpcEndpointService": AwsEc2VpcEndpointServiceDetailsTypeDef,
        "AwsXrayEncryptionConfig": AwsXrayEncryptionConfigDetailsTypeDef,
        "AwsWafRateBasedRule": AwsWafRateBasedRuleDetailsTypeDef,
        "AwsWafRegionalRateBasedRule": AwsWafRegionalRateBasedRuleDetailsTypeDef,
        "AwsEcrRepository": AwsEcrRepositoryDetailsTypeDef,
        "AwsEksCluster": AwsEksClusterDetailsTypeDef,
        "AwsNetworkFirewallFirewallPolicy": AwsNetworkFirewallFirewallPolicyDetailsTypeDef,
        "AwsNetworkFirewallFirewall": AwsNetworkFirewallFirewallDetailsTypeDef,
        "AwsNetworkFirewallRuleGroup": AwsNetworkFirewallRuleGroupDetailsTypeDef,
        "AwsRdsDbSecurityGroup": AwsRdsDbSecurityGroupDetailsTypeDef,
        "AwsKinesisStream": AwsKinesisStreamDetailsTypeDef,
        "AwsEc2TransitGateway": AwsEc2TransitGatewayDetailsTypeDef,
        "AwsEfsAccessPoint": AwsEfsAccessPointDetailsTypeDef,
        "AwsCloudFormationStack": AwsCloudFormationStackDetailsTypeDef,
        "AwsCloudWatchAlarm": AwsCloudWatchAlarmDetailsTypeDef,
        "AwsEc2VpcPeeringConnection": AwsEc2VpcPeeringConnectionDetailsTypeDef,
        "AwsWafRegionalRuleGroup": AwsWafRegionalRuleGroupDetailsTypeDef,
        "AwsWafRegionalRule": AwsWafRegionalRuleDetailsTypeDef,
        "AwsWafRegionalWebAcl": AwsWafRegionalWebAclDetailsTypeDef,
        "AwsWafRule": AwsWafRuleDetailsTypeDef,
        "AwsWafRuleGroup": AwsWafRuleGroupDetailsTypeDef,
        "AwsEcsTask": AwsEcsTaskDetailsTypeDef,
        "AwsBackupBackupVault": AwsBackupBackupVaultDetailsTypeDef,
        "AwsBackupBackupPlan": AwsBackupBackupPlanDetailsTypeDef,
        "AwsBackupRecoveryPoint": AwsBackupRecoveryPointDetailsTypeDef,
        "AwsEc2LaunchTemplate": AwsEc2LaunchTemplateDetailsTypeDef,
        "AwsSageMakerNotebookInstance": AwsSageMakerNotebookInstanceDetailsTypeDef,
        "AwsWafv2WebAcl": AwsWafv2WebAclDetailsTypeDef,
        "AwsWafv2RuleGroup": AwsWafv2RuleGroupDetailsTypeDef,
        "AwsEc2RouteTable": AwsEc2RouteTableDetailsTypeDef,
        "AwsAmazonMqBroker": AwsAmazonMqBrokerDetailsTypeDef,
        "AwsAppSyncGraphQlApi": AwsAppSyncGraphQlApiDetailsTypeDef,
        "AwsEventSchemasRegistry": AwsEventSchemasRegistryDetailsTypeDef,
        "AwsGuardDutyDetector": AwsGuardDutyDetectorDetailsTypeDef,
        "AwsStepFunctionStateMachine": AwsStepFunctionStateMachineDetailsTypeDef,
        "AwsAthenaWorkGroup": AwsAthenaWorkGroupDetailsTypeDef,
    },
    total=False,
)

ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": PartitionType,
        "Region": str,
        "ResourceRole": str,
        "Tags": Dict[str, str],
        "DataClassification": DataClassificationDetailsOutputTypeDef,
        "Details": ResourceDetailsOutputTypeDef,
    },
)

_RequiredResourceTypeDef = TypedDict(
    "_RequiredResourceTypeDef",
    {
        "Type": str,
        "Id": str,
    },
)
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "Partition": PartitionType,
        "Region": str,
        "ResourceRole": str,
        "Tags": Mapping[str, str],
        "DataClassification": DataClassificationDetailsTypeDef,
        "Details": ResourceDetailsTypeDef,
    },
    total=False,
)


class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
    pass


AwsSecurityFindingOutputTypeDef = TypedDict(
    "AwsSecurityFindingOutputTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "ProductName": str,
        "CompanyName": str,
        "Region": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": SeverityOutputTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": RemediationOutputTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[MalwareOutputTypeDef],
        "Network": NetworkOutputTypeDef,
        "NetworkPath": List[NetworkPathComponentOutputTypeDef],
        "Process": ProcessDetailsOutputTypeDef,
        "Threats": List[ThreatOutputTypeDef],
        "ThreatIntelIndicators": List[ThreatIntelIndicatorOutputTypeDef],
        "Resources": List[ResourceOutputTypeDef],
        "Compliance": ComplianceOutputTypeDef,
        "VerificationState": VerificationStateType,
        "WorkflowState": WorkflowStateType,
        "Workflow": WorkflowOutputTypeDef,
        "RecordState": RecordStateType,
        "RelatedFindings": List[RelatedFindingOutputTypeDef],
        "Note": NoteOutputTypeDef,
        "Vulnerabilities": List[VulnerabilityOutputTypeDef],
        "PatchSummary": PatchSummaryOutputTypeDef,
        "Action": ActionOutputTypeDef,
        "FindingProviderFields": FindingProviderFieldsOutputTypeDef,
        "Sample": bool,
    },
)

_RequiredAwsSecurityFindingTypeDef = TypedDict(
    "_RequiredAwsSecurityFindingTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Title": str,
        "Description": str,
        "Resources": Sequence[ResourceTypeDef],
    },
)
_OptionalAwsSecurityFindingTypeDef = TypedDict(
    "_OptionalAwsSecurityFindingTypeDef",
    {
        "ProductName": str,
        "CompanyName": str,
        "Region": str,
        "Types": Sequence[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "Severity": SeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Remediation": RemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Mapping[str, str],
        "UserDefinedFields": Mapping[str, str],
        "Malware": Sequence[MalwareTypeDef],
        "Network": NetworkTypeDef,
        "NetworkPath": Sequence[NetworkPathComponentTypeDef],
        "Process": ProcessDetailsTypeDef,
        "Threats": Sequence[ThreatTypeDef],
        "ThreatIntelIndicators": Sequence[ThreatIntelIndicatorTypeDef],
        "Compliance": ComplianceTypeDef,
        "VerificationState": VerificationStateType,
        "WorkflowState": WorkflowStateType,
        "Workflow": WorkflowTypeDef,
        "RecordState": RecordStateType,
        "RelatedFindings": Sequence[RelatedFindingTypeDef],
        "Note": NoteTypeDef,
        "Vulnerabilities": Sequence[VulnerabilityTypeDef],
        "PatchSummary": PatchSummaryTypeDef,
        "Action": ActionTypeDef,
        "FindingProviderFields": FindingProviderFieldsTypeDef,
        "Sample": bool,
    },
    total=False,
)


class AwsSecurityFindingTypeDef(
    _RequiredAwsSecurityFindingTypeDef, _OptionalAwsSecurityFindingTypeDef
):
    pass


GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List[AwsSecurityFindingOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchImportFindingsRequestRequestTypeDef = TypedDict(
    "BatchImportFindingsRequestRequestTypeDef",
    {
        "Findings": Sequence[AwsSecurityFindingTypeDef],
    },
)
