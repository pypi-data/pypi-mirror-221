"""
Type annotations for iot service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot/type_defs/)

Usage::

    ```python
    from mypy_boto3_iot.type_defs import AbortCriteriaOutputTypeDef

    data: AbortCriteriaOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ActionTypeType,
    AggregationTypeNameType,
    AuditCheckRunStatusType,
    AuditFindingSeverityType,
    AuditFrequencyType,
    AuditMitigationActionsExecutionStatusType,
    AuditMitigationActionsTaskStatusType,
    AuditTaskStatusType,
    AuditTaskTypeType,
    AuthDecisionType,
    AuthorizerStatusType,
    AutoRegistrationStatusType,
    AwsJobAbortCriteriaFailureTypeType,
    BehaviorCriteriaTypeType,
    CACertificateStatusType,
    CannedAccessControlListType,
    CertificateModeType,
    CertificateStatusType,
    ComparisonOperatorType,
    ConfidenceLevelType,
    CustomMetricTypeType,
    DayOfWeekType,
    DetectMitigationActionExecutionStatusType,
    DetectMitigationActionsTaskStatusType,
    DeviceDefenderIndexingModeType,
    DimensionValueOperatorType,
    DomainConfigurationStatusType,
    DomainTypeType,
    DynamicGroupStatusType,
    DynamoKeyTypeType,
    EventTypeType,
    FieldTypeType,
    FleetMetricUnitType,
    IndexStatusType,
    JobEndBehaviorType,
    JobExecutionFailureTypeType,
    JobExecutionStatusType,
    JobStatusType,
    LogLevelType,
    LogTargetTypeType,
    MessageFormatType,
    MitigationActionTypeType,
    ModelStatusType,
    NamedShadowIndexingModeType,
    OTAUpdateStatusType,
    PackageVersionActionType,
    PackageVersionStatusType,
    ProtocolType,
    ReportTypeType,
    ResourceTypeType,
    RetryableFailureTypeType,
    ServerCertificateStatusType,
    ServiceTypeType,
    StatusType,
    TargetSelectionType,
    TemplateTypeType,
    ThingConnectivityIndexingModeType,
    ThingGroupIndexingModeType,
    ThingIndexingModeType,
    TopicRuleDestinationStatusType,
    VerificationStateType,
    ViolationEventTypeType,
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
    "AbortCriteriaOutputTypeDef",
    "AbortCriteriaTypeDef",
    "AcceptCertificateTransferRequestRequestTypeDef",
    "CloudwatchAlarmActionOutputTypeDef",
    "CloudwatchLogsActionOutputTypeDef",
    "CloudwatchMetricActionOutputTypeDef",
    "DynamoDBActionOutputTypeDef",
    "ElasticsearchActionOutputTypeDef",
    "FirehoseActionOutputTypeDef",
    "IotAnalyticsActionOutputTypeDef",
    "IotEventsActionOutputTypeDef",
    "KafkaActionOutputTypeDef",
    "KinesisActionOutputTypeDef",
    "LambdaActionOutputTypeDef",
    "OpenSearchActionOutputTypeDef",
    "S3ActionOutputTypeDef",
    "SalesforceActionOutputTypeDef",
    "SnsActionOutputTypeDef",
    "SqsActionOutputTypeDef",
    "StepFunctionsActionOutputTypeDef",
    "CloudwatchAlarmActionTypeDef",
    "CloudwatchLogsActionTypeDef",
    "CloudwatchMetricActionTypeDef",
    "DynamoDBActionTypeDef",
    "ElasticsearchActionTypeDef",
    "FirehoseActionTypeDef",
    "IotAnalyticsActionTypeDef",
    "IotEventsActionTypeDef",
    "KafkaActionTypeDef",
    "KinesisActionTypeDef",
    "LambdaActionTypeDef",
    "OpenSearchActionTypeDef",
    "S3ActionTypeDef",
    "SalesforceActionTypeDef",
    "SnsActionTypeDef",
    "SqsActionTypeDef",
    "StepFunctionsActionTypeDef",
    "MetricValueOutputTypeDef",
    "ViolationEventAdditionalInfoTypeDef",
    "AddThingToBillingGroupRequestRequestTypeDef",
    "AddThingToThingGroupRequestRequestTypeDef",
    "AddThingsToThingGroupParamsOutputTypeDef",
    "AddThingsToThingGroupParamsTypeDef",
    "AggregationTypeOutputTypeDef",
    "AggregationTypeTypeDef",
    "AlertTargetOutputTypeDef",
    "AlertTargetTypeDef",
    "PolicyTypeDef",
    "AssetPropertyTimestampOutputTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyVariantOutputTypeDef",
    "AssetPropertyVariantTypeDef",
    "AssociateTargetsWithJobRequestRequestTypeDef",
    "AssociateTargetsWithJobResponseTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "AttachPrincipalPolicyRequestRequestTypeDef",
    "AttachSecurityProfileRequestRequestTypeDef",
    "AttachThingPrincipalRequestRequestTypeDef",
    "AttributePayloadOutputTypeDef",
    "AttributePayloadTypeDef",
    "AuditCheckConfigurationOutputTypeDef",
    "AuditCheckConfigurationTypeDef",
    "AuditCheckDetailsTypeDef",
    "AuditMitigationActionExecutionMetadataTypeDef",
    "AuditMitigationActionsTaskMetadataTypeDef",
    "AuditMitigationActionsTaskTargetOutputTypeDef",
    "AuditMitigationActionsTaskTargetTypeDef",
    "AuditNotificationTargetOutputTypeDef",
    "AuditNotificationTargetTypeDef",
    "AuditTaskMetadataTypeDef",
    "AuthInfoOutputTypeDef",
    "AuthInfoTypeDef",
    "AuthorizerConfigOutputTypeDef",
    "AuthorizerConfigTypeDef",
    "AuthorizerDescriptionTypeDef",
    "AuthorizerSummaryTypeDef",
    "AwsJobAbortCriteriaTypeDef",
    "AwsJobRateIncreaseCriteriaOutputTypeDef",
    "AwsJobRateIncreaseCriteriaTypeDef",
    "AwsJobPresignedUrlConfigOutputTypeDef",
    "AwsJobPresignedUrlConfigTypeDef",
    "AwsJobTimeoutConfigTypeDef",
    "MachineLearningDetectionConfigOutputTypeDef",
    "StatisticalThresholdOutputTypeDef",
    "MachineLearningDetectionConfigTypeDef",
    "MetricValueTypeDef",
    "StatisticalThresholdTypeDef",
    "BehaviorModelTrainingSummaryTypeDef",
    "MetricDimensionOutputTypeDef",
    "MetricDimensionTypeDef",
    "BillingGroupMetadataTypeDef",
    "BillingGroupPropertiesOutputTypeDef",
    "BillingGroupPropertiesTypeDef",
    "BucketTypeDef",
    "TermsAggregationTypeDef",
    "CertificateValidityTypeDef",
    "CACertificateTypeDef",
    "CancelAuditMitigationActionsTaskRequestRequestTypeDef",
    "CancelAuditTaskRequestRequestTypeDef",
    "CancelCertificateTransferRequestRequestTypeDef",
    "CancelDetectMitigationActionsTaskRequestRequestTypeDef",
    "CancelJobExecutionRequestRequestTypeDef",
    "CancelJobRequestRequestTypeDef",
    "CancelJobResponseTypeDef",
    "TransferDataTypeDef",
    "CertificateTypeDef",
    "CodeSigningCertificateChainOutputTypeDef",
    "CodeSigningCertificateChainTypeDef",
    "CodeSigningSignatureOutputTypeDef",
    "CodeSigningSignatureTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationTypeDef",
    "ConfirmTopicRuleDestinationRequestRequestTypeDef",
    "TagTypeDef",
    "CreateAuthorizerResponseTypeDef",
    "CreateBillingGroupResponseTypeDef",
    "CreateCertificateFromCsrRequestRequestTypeDef",
    "CreateCertificateFromCsrResponseTypeDef",
    "CreateCustomMetricResponseTypeDef",
    "CreateDimensionResponseTypeDef",
    "TlsConfigTypeDef",
    "CreateDomainConfigurationResponseTypeDef",
    "CreateDynamicThingGroupResponseTypeDef",
    "CreateFleetMetricResponseTypeDef",
    "PresignedUrlConfigTypeDef",
    "TimeoutConfigTypeDef",
    "CreateJobResponseTypeDef",
    "MaintenanceWindowTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreateKeysAndCertificateRequestRequestTypeDef",
    "KeyPairTypeDef",
    "CreateMitigationActionResponseTypeDef",
    "CreateOTAUpdateResponseTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "CreatePackageVersionRequestRequestTypeDef",
    "CreatePackageVersionResponseTypeDef",
    "CreatePolicyResponseTypeDef",
    "CreatePolicyVersionRequestRequestTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "CreateProvisioningClaimRequestRequestTypeDef",
    "ProvisioningHookTypeDef",
    "CreateProvisioningTemplateResponseTypeDef",
    "CreateProvisioningTemplateVersionRequestRequestTypeDef",
    "CreateProvisioningTemplateVersionResponseTypeDef",
    "CreateRoleAliasResponseTypeDef",
    "CreateScheduledAuditResponseTypeDef",
    "CreateSecurityProfileResponseTypeDef",
    "CreateStreamResponseTypeDef",
    "CreateThingGroupResponseTypeDef",
    "CreateThingResponseTypeDef",
    "ThingTypePropertiesTypeDef",
    "CreateThingTypeResponseTypeDef",
    "DeleteAccountAuditConfigurationRequestRequestTypeDef",
    "DeleteAuthorizerRequestRequestTypeDef",
    "DeleteBillingGroupRequestRequestTypeDef",
    "DeleteCACertificateRequestRequestTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "DeleteCustomMetricRequestRequestTypeDef",
    "DeleteDimensionRequestRequestTypeDef",
    "DeleteDomainConfigurationRequestRequestTypeDef",
    "DeleteDynamicThingGroupRequestRequestTypeDef",
    "DeleteFleetMetricRequestRequestTypeDef",
    "DeleteJobExecutionRequestRequestTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteJobTemplateRequestRequestTypeDef",
    "DeleteMitigationActionRequestRequestTypeDef",
    "DeleteOTAUpdateRequestRequestTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageVersionRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeletePolicyVersionRequestRequestTypeDef",
    "DeleteProvisioningTemplateRequestRequestTypeDef",
    "DeleteProvisioningTemplateVersionRequestRequestTypeDef",
    "DeleteRoleAliasRequestRequestTypeDef",
    "DeleteScheduledAuditRequestRequestTypeDef",
    "DeleteSecurityProfileRequestRequestTypeDef",
    "DeleteStreamRequestRequestTypeDef",
    "DeleteThingGroupRequestRequestTypeDef",
    "DeleteThingRequestRequestTypeDef",
    "DeleteThingTypeRequestRequestTypeDef",
    "DeleteTopicRuleDestinationRequestRequestTypeDef",
    "DeleteTopicRuleRequestRequestTypeDef",
    "DeleteV2LoggingLevelRequestRequestTypeDef",
    "DeprecateThingTypeRequestRequestTypeDef",
    "DescribeAuditFindingRequestRequestTypeDef",
    "DescribeAuditMitigationActionsTaskRequestRequestTypeDef",
    "TaskStatisticsForAuditCheckTypeDef",
    "DescribeAuditTaskRequestRequestTypeDef",
    "TaskStatisticsTypeDef",
    "DescribeAuthorizerRequestRequestTypeDef",
    "DescribeBillingGroupRequestRequestTypeDef",
    "DescribeCACertificateRequestRequestTypeDef",
    "RegistrationConfigOutputTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "DescribeCustomMetricRequestRequestTypeDef",
    "DescribeCustomMetricResponseTypeDef",
    "DescribeDetectMitigationActionsTaskRequestRequestTypeDef",
    "DescribeDimensionRequestRequestTypeDef",
    "DescribeDimensionResponseTypeDef",
    "DescribeDomainConfigurationRequestRequestTypeDef",
    "ServerCertificateSummaryTypeDef",
    "TlsConfigOutputTypeDef",
    "DescribeEndpointRequestRequestTypeDef",
    "DescribeEndpointResponseTypeDef",
    "DescribeFleetMetricRequestRequestTypeDef",
    "DescribeIndexRequestRequestTypeDef",
    "DescribeIndexResponseTypeDef",
    "DescribeJobExecutionRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobTemplateRequestRequestTypeDef",
    "MaintenanceWindowOutputTypeDef",
    "PresignedUrlConfigOutputTypeDef",
    "TimeoutConfigOutputTypeDef",
    "DescribeManagedJobTemplateRequestRequestTypeDef",
    "DocumentParameterTypeDef",
    "DescribeMitigationActionRequestRequestTypeDef",
    "DescribeProvisioningTemplateRequestRequestTypeDef",
    "ProvisioningHookOutputTypeDef",
    "DescribeProvisioningTemplateVersionRequestRequestTypeDef",
    "DescribeProvisioningTemplateVersionResponseTypeDef",
    "DescribeRoleAliasRequestRequestTypeDef",
    "RoleAliasDescriptionTypeDef",
    "DescribeScheduledAuditRequestRequestTypeDef",
    "DescribeScheduledAuditResponseTypeDef",
    "DescribeSecurityProfileRequestRequestTypeDef",
    "DescribeStreamRequestRequestTypeDef",
    "DescribeThingGroupRequestRequestTypeDef",
    "DescribeThingRegistrationTaskRequestRequestTypeDef",
    "DescribeThingRegistrationTaskResponseTypeDef",
    "DescribeThingRequestRequestTypeDef",
    "DescribeThingResponseTypeDef",
    "DescribeThingTypeRequestRequestTypeDef",
    "ThingTypeMetadataTypeDef",
    "ThingTypePropertiesOutputTypeDef",
    "S3DestinationOutputTypeDef",
    "S3DestinationTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "DetachPrincipalPolicyRequestRequestTypeDef",
    "DetachSecurityProfileRequestRequestTypeDef",
    "DetachThingPrincipalRequestRequestTypeDef",
    "DetectMitigationActionExecutionTypeDef",
    "DetectMitigationActionsTaskStatisticsTypeDef",
    "DetectMitigationActionsTaskTargetOutputTypeDef",
    "ViolationEventOccurrenceRangeOutputTypeDef",
    "DetectMitigationActionsTaskTargetTypeDef",
    "DisableTopicRuleRequestRequestTypeDef",
    "DomainConfigurationSummaryTypeDef",
    "PutItemInputOutputTypeDef",
    "PutItemInputTypeDef",
    "EffectivePolicyTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableIoTLoggingParamsOutputTypeDef",
    "EnableIoTLoggingParamsTypeDef",
    "EnableTopicRuleRequestRequestTypeDef",
    "ErrorInfoTypeDef",
    "RateIncreaseCriteriaOutputTypeDef",
    "RateIncreaseCriteriaTypeDef",
    "FieldOutputTypeDef",
    "FieldTypeDef",
    "S3LocationOutputTypeDef",
    "StreamOutputTypeDef",
    "S3LocationTypeDef",
    "StreamTypeDef",
    "FleetMetricNameAndArnTypeDef",
    "GetBehaviorModelTrainingSummariesRequestGetBehaviorModelTrainingSummariesPaginateTypeDef",
    "GetBehaviorModelTrainingSummariesRequestRequestTypeDef",
    "GetCardinalityRequestRequestTypeDef",
    "GetCardinalityResponseTypeDef",
    "GetEffectivePoliciesRequestRequestTypeDef",
    "GetJobDocumentRequestRequestTypeDef",
    "GetJobDocumentResponseTypeDef",
    "GetLoggingOptionsResponseTypeDef",
    "GetOTAUpdateRequestRequestTypeDef",
    "VersionUpdateByJobsConfigOutputTypeDef",
    "GetPackageRequestRequestTypeDef",
    "GetPackageResponseTypeDef",
    "GetPackageVersionRequestRequestTypeDef",
    "GetPackageVersionResponseTypeDef",
    "GetPercentilesRequestRequestTypeDef",
    "PercentPairTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetPolicyVersionRequestRequestTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "GetRegistrationCodeResponseTypeDef",
    "GetStatisticsRequestRequestTypeDef",
    "StatisticsTypeDef",
    "GetTopicRuleDestinationRequestRequestTypeDef",
    "GetTopicRuleRequestRequestTypeDef",
    "GetV2LoggingOptionsResponseTypeDef",
    "GroupNameAndArnTypeDef",
    "HttpActionHeaderOutputTypeDef",
    "HttpActionHeaderTypeDef",
    "SigV4AuthorizationOutputTypeDef",
    "SigV4AuthorizationTypeDef",
    "HttpContextTypeDef",
    "HttpUrlDestinationConfigurationTypeDef",
    "HttpUrlDestinationPropertiesTypeDef",
    "HttpUrlDestinationSummaryTypeDef",
    "IndexingFilterOutputTypeDef",
    "IndexingFilterTypeDef",
    "IssuerCertificateIdentifierOutputTypeDef",
    "IssuerCertificateIdentifierTypeDef",
    "JobExecutionStatusDetailsTypeDef",
    "JobExecutionSummaryTypeDef",
    "RetryCriteriaOutputTypeDef",
    "RetryCriteriaTypeDef",
    "JobProcessDetailsTypeDef",
    "JobSummaryTypeDef",
    "JobTemplateSummaryTypeDef",
    "ScheduledJobRolloutTypeDef",
    "ListActiveViolationsRequestListActiveViolationsPaginateTypeDef",
    "ListActiveViolationsRequestRequestTypeDef",
    "ListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef",
    "ListAttachedPoliciesRequestRequestTypeDef",
    "ListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef",
    "ListAuditMitigationActionsExecutionsRequestRequestTypeDef",
    "ListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef",
    "ListAuditMitigationActionsTasksRequestRequestTypeDef",
    "ListAuditTasksRequestListAuditTasksPaginateTypeDef",
    "ListAuditTasksRequestRequestTypeDef",
    "ListAuthorizersRequestListAuthorizersPaginateTypeDef",
    "ListAuthorizersRequestRequestTypeDef",
    "ListBillingGroupsRequestListBillingGroupsPaginateTypeDef",
    "ListBillingGroupsRequestRequestTypeDef",
    "ListCACertificatesRequestListCACertificatesPaginateTypeDef",
    "ListCACertificatesRequestRequestTypeDef",
    "ListCertificatesByCARequestListCertificatesByCAPaginateTypeDef",
    "ListCertificatesByCARequestRequestTypeDef",
    "ListCertificatesRequestListCertificatesPaginateTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListCustomMetricsRequestListCustomMetricsPaginateTypeDef",
    "ListCustomMetricsRequestRequestTypeDef",
    "ListCustomMetricsResponseTypeDef",
    "ListDetectMitigationActionsExecutionsRequestListDetectMitigationActionsExecutionsPaginateTypeDef",
    "ListDetectMitigationActionsExecutionsRequestRequestTypeDef",
    "ListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef",
    "ListDetectMitigationActionsTasksRequestRequestTypeDef",
    "ListDimensionsRequestListDimensionsPaginateTypeDef",
    "ListDimensionsRequestRequestTypeDef",
    "ListDimensionsResponseTypeDef",
    "ListDomainConfigurationsRequestListDomainConfigurationsPaginateTypeDef",
    "ListDomainConfigurationsRequestRequestTypeDef",
    "ListFleetMetricsRequestListFleetMetricsPaginateTypeDef",
    "ListFleetMetricsRequestRequestTypeDef",
    "ListIndicesRequestListIndicesPaginateTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListIndicesResponseTypeDef",
    "ListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef",
    "ListJobExecutionsForJobRequestRequestTypeDef",
    "ListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef",
    "ListJobExecutionsForThingRequestRequestTypeDef",
    "ListJobTemplatesRequestListJobTemplatesPaginateTypeDef",
    "ListJobTemplatesRequestRequestTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListManagedJobTemplatesRequestListManagedJobTemplatesPaginateTypeDef",
    "ListManagedJobTemplatesRequestRequestTypeDef",
    "ManagedJobTemplateSummaryTypeDef",
    "ListMetricValuesRequestListMetricValuesPaginateTypeDef",
    "ListMetricValuesRequestRequestTypeDef",
    "ListMitigationActionsRequestListMitigationActionsPaginateTypeDef",
    "ListMitigationActionsRequestRequestTypeDef",
    "MitigationActionIdentifierTypeDef",
    "ListOTAUpdatesRequestListOTAUpdatesPaginateTypeDef",
    "ListOTAUpdatesRequestRequestTypeDef",
    "OTAUpdateSummaryTypeDef",
    "ListOutgoingCertificatesRequestListOutgoingCertificatesPaginateTypeDef",
    "ListOutgoingCertificatesRequestRequestTypeDef",
    "OutgoingCertificateTypeDef",
    "ListPackageVersionsRequestListPackageVersionsPaginateTypeDef",
    "ListPackageVersionsRequestRequestTypeDef",
    "PackageVersionSummaryTypeDef",
    "ListPackagesRequestListPackagesPaginateTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "PackageSummaryTypeDef",
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef",
    "ListPolicyPrincipalsRequestRequestTypeDef",
    "ListPolicyPrincipalsResponseTypeDef",
    "ListPolicyVersionsRequestRequestTypeDef",
    "PolicyVersionTypeDef",
    "ListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef",
    "ListPrincipalPoliciesRequestRequestTypeDef",
    "ListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef",
    "ListPrincipalThingsRequestRequestTypeDef",
    "ListPrincipalThingsResponseTypeDef",
    "ListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef",
    "ListProvisioningTemplateVersionsRequestRequestTypeDef",
    "ProvisioningTemplateVersionSummaryTypeDef",
    "ListProvisioningTemplatesRequestListProvisioningTemplatesPaginateTypeDef",
    "ListProvisioningTemplatesRequestRequestTypeDef",
    "ProvisioningTemplateSummaryTypeDef",
    "ListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef",
    "ListRelatedResourcesForAuditFindingRequestRequestTypeDef",
    "ListRoleAliasesRequestListRoleAliasesPaginateTypeDef",
    "ListRoleAliasesRequestRequestTypeDef",
    "ListRoleAliasesResponseTypeDef",
    "ListScheduledAuditsRequestListScheduledAuditsPaginateTypeDef",
    "ListScheduledAuditsRequestRequestTypeDef",
    "ScheduledAuditMetadataTypeDef",
    "ListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef",
    "ListSecurityProfilesForTargetRequestRequestTypeDef",
    "ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef",
    "ListSecurityProfilesRequestRequestTypeDef",
    "SecurityProfileIdentifierTypeDef",
    "ListStreamsRequestListStreamsPaginateTypeDef",
    "ListStreamsRequestRequestTypeDef",
    "StreamSummaryTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef",
    "ListTargetsForPolicyRequestRequestTypeDef",
    "ListTargetsForPolicyResponseTypeDef",
    "ListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef",
    "ListTargetsForSecurityProfileRequestRequestTypeDef",
    "SecurityProfileTargetTypeDef",
    "ListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef",
    "ListThingGroupsForThingRequestRequestTypeDef",
    "ListThingGroupsRequestListThingGroupsPaginateTypeDef",
    "ListThingGroupsRequestRequestTypeDef",
    "ListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef",
    "ListThingPrincipalsRequestRequestTypeDef",
    "ListThingPrincipalsResponseTypeDef",
    "ListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef",
    "ListThingRegistrationTaskReportsRequestRequestTypeDef",
    "ListThingRegistrationTaskReportsResponseTypeDef",
    "ListThingRegistrationTasksRequestListThingRegistrationTasksPaginateTypeDef",
    "ListThingRegistrationTasksRequestRequestTypeDef",
    "ListThingRegistrationTasksResponseTypeDef",
    "ListThingTypesRequestListThingTypesPaginateTypeDef",
    "ListThingTypesRequestRequestTypeDef",
    "ListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef",
    "ListThingsInBillingGroupRequestRequestTypeDef",
    "ListThingsInBillingGroupResponseTypeDef",
    "ListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef",
    "ListThingsInThingGroupRequestRequestTypeDef",
    "ListThingsInThingGroupResponseTypeDef",
    "ListThingsRequestListThingsPaginateTypeDef",
    "ListThingsRequestRequestTypeDef",
    "ThingAttributeTypeDef",
    "ListTopicRuleDestinationsRequestListTopicRuleDestinationsPaginateTypeDef",
    "ListTopicRuleDestinationsRequestRequestTypeDef",
    "ListTopicRulesRequestListTopicRulesPaginateTypeDef",
    "ListTopicRulesRequestRequestTypeDef",
    "TopicRuleListItemTypeDef",
    "ListV2LoggingLevelsRequestListV2LoggingLevelsPaginateTypeDef",
    "ListV2LoggingLevelsRequestRequestTypeDef",
    "ListViolationEventsRequestListViolationEventsPaginateTypeDef",
    "ListViolationEventsRequestRequestTypeDef",
    "LocationTimestampOutputTypeDef",
    "LocationTimestampTypeDef",
    "LogTargetOutputTypeDef",
    "LogTargetTypeDef",
    "LoggingOptionsPayloadTypeDef",
    "PublishFindingToSnsParamsOutputTypeDef",
    "ReplaceDefaultPolicyVersionParamsOutputTypeDef",
    "UpdateCACertificateParamsOutputTypeDef",
    "UpdateDeviceCertificateParamsOutputTypeDef",
    "PublishFindingToSnsParamsTypeDef",
    "ReplaceDefaultPolicyVersionParamsTypeDef",
    "UpdateCACertificateParamsTypeDef",
    "UpdateDeviceCertificateParamsTypeDef",
    "MqttContextTypeDef",
    "UserPropertyOutputTypeDef",
    "UserPropertyTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyVersionIdentifierOutputTypeDef",
    "PolicyVersionIdentifierTypeDef",
    "PutVerificationStateOnViolationRequestRequestTypeDef",
    "RegistrationConfigTypeDef",
    "RegisterCACertificateResponseTypeDef",
    "RegisterCertificateRequestRequestTypeDef",
    "RegisterCertificateResponseTypeDef",
    "RegisterCertificateWithoutCARequestRequestTypeDef",
    "RegisterCertificateWithoutCAResponseTypeDef",
    "RegisterThingRequestRequestTypeDef",
    "RegisterThingResponseTypeDef",
    "RejectCertificateTransferRequestRequestTypeDef",
    "RemoveThingFromBillingGroupRequestRequestTypeDef",
    "RemoveThingFromThingGroupRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SearchIndexRequestRequestTypeDef",
    "ThingGroupDocumentTypeDef",
    "SetDefaultAuthorizerRequestRequestTypeDef",
    "SetDefaultAuthorizerResponseTypeDef",
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    "SetV2LoggingOptionsRequestRequestTypeDef",
    "SigningProfileParameterOutputTypeDef",
    "SigningProfileParameterTypeDef",
    "StartAuditMitigationActionsTaskResponseTypeDef",
    "ViolationEventOccurrenceRangeTypeDef",
    "StartDetectMitigationActionsTaskResponseTypeDef",
    "StartOnDemandAuditTaskRequestRequestTypeDef",
    "StartOnDemandAuditTaskResponseTypeDef",
    "StartThingRegistrationTaskRequestRequestTypeDef",
    "StartThingRegistrationTaskResponseTypeDef",
    "StopThingRegistrationTaskRequestRequestTypeDef",
    "TlsContextTypeDef",
    "TestInvokeAuthorizerResponseTypeDef",
    "ThingConnectivityTypeDef",
    "TimestreamDimensionOutputTypeDef",
    "TimestreamTimestampOutputTypeDef",
    "TimestreamDimensionTypeDef",
    "TimestreamTimestampTypeDef",
    "VpcDestinationConfigurationTypeDef",
    "VpcDestinationSummaryTypeDef",
    "VpcDestinationPropertiesTypeDef",
    "TransferCertificateRequestRequestTypeDef",
    "TransferCertificateResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAuthorizerRequestRequestTypeDef",
    "UpdateAuthorizerResponseTypeDef",
    "UpdateBillingGroupResponseTypeDef",
    "UpdateCertificateRequestRequestTypeDef",
    "UpdateCustomMetricRequestRequestTypeDef",
    "UpdateCustomMetricResponseTypeDef",
    "UpdateDimensionRequestRequestTypeDef",
    "UpdateDimensionResponseTypeDef",
    "UpdateDomainConfigurationResponseTypeDef",
    "UpdateDynamicThingGroupResponseTypeDef",
    "UpdateMitigationActionResponseTypeDef",
    "VersionUpdateByJobsConfigTypeDef",
    "UpdatePackageRequestRequestTypeDef",
    "UpdatePackageVersionRequestRequestTypeDef",
    "UpdateRoleAliasRequestRequestTypeDef",
    "UpdateRoleAliasResponseTypeDef",
    "UpdateScheduledAuditRequestRequestTypeDef",
    "UpdateScheduledAuditResponseTypeDef",
    "UpdateStreamResponseTypeDef",
    "UpdateThingGroupResponseTypeDef",
    "UpdateThingGroupsForThingRequestRequestTypeDef",
    "UpdateTopicRuleDestinationRequestRequestTypeDef",
    "ValidationErrorTypeDef",
    "AbortConfigOutputTypeDef",
    "AbortConfigTypeDef",
    "MetricDatumTypeDef",
    "DescribeFleetMetricResponseTypeDef",
    "UpdateFleetMetricRequestRequestTypeDef",
    "AllowedTypeDef",
    "ExplicitDenyTypeDef",
    "ImplicitDenyTypeDef",
    "ListAttachedPoliciesResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPrincipalPoliciesResponseTypeDef",
    "AssetPropertyValueOutputTypeDef",
    "AssetPropertyValueTypeDef",
    "ThingGroupPropertiesOutputTypeDef",
    "CreateThingRequestRequestTypeDef",
    "ThingGroupPropertiesTypeDef",
    "UpdateThingRequestRequestTypeDef",
    "ListAuditMitigationActionsExecutionsResponseTypeDef",
    "ListAuditMitigationActionsTasksResponseTypeDef",
    "StartAuditMitigationActionsTaskRequestRequestTypeDef",
    "DescribeAccountAuditConfigurationResponseTypeDef",
    "UpdateAccountAuditConfigurationRequestRequestTypeDef",
    "ListAuditTasksResponseTypeDef",
    "TestAuthorizationRequestRequestTypeDef",
    "DescribeAuthorizerResponseTypeDef",
    "DescribeDefaultAuthorizerResponseTypeDef",
    "ListAuthorizersResponseTypeDef",
    "AwsJobAbortConfigTypeDef",
    "AwsJobExponentialRolloutRateOutputTypeDef",
    "AwsJobExponentialRolloutRateTypeDef",
    "BehaviorCriteriaOutputTypeDef",
    "BehaviorCriteriaTypeDef",
    "GetBehaviorModelTrainingSummariesResponseTypeDef",
    "MetricToRetainOutputTypeDef",
    "MetricToRetainTypeDef",
    "DescribeBillingGroupResponseTypeDef",
    "UpdateBillingGroupRequestRequestTypeDef",
    "GetBucketsAggregationResponseTypeDef",
    "BucketsAggregationTypeTypeDef",
    "CACertificateDescriptionTypeDef",
    "ListCACertificatesResponseTypeDef",
    "CertificateDescriptionTypeDef",
    "ListCertificatesByCAResponseTypeDef",
    "ListCertificatesResponseTypeDef",
    "CustomCodeSigningOutputTypeDef",
    "CustomCodeSigningTypeDef",
    "DescribeEventConfigurationsResponseTypeDef",
    "UpdateEventConfigurationsRequestRequestTypeDef",
    "CreateAuthorizerRequestRequestTypeDef",
    "CreateBillingGroupRequestRequestTypeDef",
    "CreateCustomMetricRequestRequestTypeDef",
    "CreateDimensionRequestRequestTypeDef",
    "CreateFleetMetricRequestRequestTypeDef",
    "CreatePolicyRequestRequestTypeDef",
    "CreateRoleAliasRequestRequestTypeDef",
    "CreateScheduledAuditRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateDomainConfigurationRequestRequestTypeDef",
    "UpdateDomainConfigurationRequestRequestTypeDef",
    "SchedulingConfigTypeDef",
    "CreateKeysAndCertificateResponseTypeDef",
    "CreateProvisioningClaimResponseTypeDef",
    "CreateProvisioningTemplateRequestRequestTypeDef",
    "UpdateProvisioningTemplateRequestRequestTypeDef",
    "CreateThingTypeRequestRequestTypeDef",
    "DescribeAuditTaskResponseTypeDef",
    "DescribeDomainConfigurationResponseTypeDef",
    "SchedulingConfigOutputTypeDef",
    "DescribeManagedJobTemplateResponseTypeDef",
    "DescribeProvisioningTemplateResponseTypeDef",
    "DescribeRoleAliasResponseTypeDef",
    "DescribeThingTypeResponseTypeDef",
    "ThingTypeDefinitionTypeDef",
    "DestinationOutputTypeDef",
    "DestinationTypeDef",
    "ListDetectMitigationActionsExecutionsResponseTypeDef",
    "ListDomainConfigurationsResponseTypeDef",
    "DynamoDBv2ActionOutputTypeDef",
    "DynamoDBv2ActionTypeDef",
    "GetEffectivePoliciesResponseTypeDef",
    "ExponentialRolloutRateOutputTypeDef",
    "ExponentialRolloutRateTypeDef",
    "ThingGroupIndexingConfigurationOutputTypeDef",
    "ThingGroupIndexingConfigurationTypeDef",
    "StreamFileOutputTypeDef",
    "FileLocationOutputTypeDef",
    "StreamFileTypeDef",
    "FileLocationTypeDef",
    "ListFleetMetricsResponseTypeDef",
    "GetPackageConfigurationResponseTypeDef",
    "GetPercentilesResponseTypeDef",
    "GetStatisticsResponseTypeDef",
    "ListBillingGroupsResponseTypeDef",
    "ListThingGroupsForThingResponseTypeDef",
    "ListThingGroupsResponseTypeDef",
    "ThingGroupMetadataTypeDef",
    "HttpAuthorizationOutputTypeDef",
    "HttpAuthorizationTypeDef",
    "ThingIndexingConfigurationOutputTypeDef",
    "ThingIndexingConfigurationTypeDef",
    "JobExecutionTypeDef",
    "JobExecutionSummaryForJobTypeDef",
    "JobExecutionSummaryForThingTypeDef",
    "JobExecutionsRetryConfigOutputTypeDef",
    "JobExecutionsRetryConfigTypeDef",
    "ListJobsResponseTypeDef",
    "ListJobTemplatesResponseTypeDef",
    "ListManagedJobTemplatesResponseTypeDef",
    "ListMitigationActionsResponseTypeDef",
    "ListOTAUpdatesResponseTypeDef",
    "ListOutgoingCertificatesResponseTypeDef",
    "ListPackageVersionsResponseTypeDef",
    "ListPackagesResponseTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListProvisioningTemplateVersionsResponseTypeDef",
    "ListProvisioningTemplatesResponseTypeDef",
    "ListScheduledAuditsResponseTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListStreamsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsForSecurityProfileResponseTypeDef",
    "SecurityProfileTargetMappingTypeDef",
    "ListThingsResponseTypeDef",
    "ListTopicRulesResponseTypeDef",
    "LocationActionOutputTypeDef",
    "LocationActionTypeDef",
    "LogTargetConfigurationTypeDef",
    "SetV2LoggingLevelRequestRequestTypeDef",
    "SetLoggingOptionsRequestRequestTypeDef",
    "MitigationActionParamsOutputTypeDef",
    "MitigationActionParamsTypeDef",
    "MqttHeadersOutputTypeDef",
    "MqttHeadersTypeDef",
    "ResourceIdentifierOutputTypeDef",
    "ResourceIdentifierTypeDef",
    "RegisterCACertificateRequestRequestTypeDef",
    "UpdateCACertificateRequestRequestTypeDef",
    "StartDetectMitigationActionsTaskRequestRequestTypeDef",
    "TestInvokeAuthorizerRequestRequestTypeDef",
    "ThingDocumentTypeDef",
    "TimestreamActionOutputTypeDef",
    "TimestreamActionTypeDef",
    "TopicRuleDestinationConfigurationTypeDef",
    "TopicRuleDestinationSummaryTypeDef",
    "TopicRuleDestinationTypeDef",
    "UpdatePackageConfigurationRequestRequestTypeDef",
    "ValidateSecurityProfileBehaviorsResponseTypeDef",
    "ListMetricValuesResponseTypeDef",
    "DeniedTypeDef",
    "PutAssetPropertyValueEntryOutputTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "CreateDynamicThingGroupRequestRequestTypeDef",
    "CreateThingGroupRequestRequestTypeDef",
    "UpdateDynamicThingGroupRequestRequestTypeDef",
    "UpdateThingGroupRequestRequestTypeDef",
    "AwsJobExecutionsRolloutConfigOutputTypeDef",
    "AwsJobExecutionsRolloutConfigTypeDef",
    "BehaviorOutputTypeDef",
    "BehaviorTypeDef",
    "GetBucketsAggregationRequestRequestTypeDef",
    "DescribeCACertificateResponseTypeDef",
    "DescribeCertificateResponseTypeDef",
    "ListThingTypesResponseTypeDef",
    "StartSigningJobParameterOutputTypeDef",
    "StartSigningJobParameterTypeDef",
    "JobExecutionsRolloutConfigOutputTypeDef",
    "JobExecutionsRolloutConfigTypeDef",
    "StreamInfoTypeDef",
    "CreateStreamRequestRequestTypeDef",
    "UpdateStreamRequestRequestTypeDef",
    "DescribeThingGroupResponseTypeDef",
    "HttpActionOutputTypeDef",
    "HttpActionTypeDef",
    "GetIndexingConfigurationResponseTypeDef",
    "UpdateIndexingConfigurationRequestRequestTypeDef",
    "DescribeJobExecutionResponseTypeDef",
    "ListJobExecutionsForJobResponseTypeDef",
    "ListJobExecutionsForThingResponseTypeDef",
    "ListSecurityProfilesForTargetResponseTypeDef",
    "ListV2LoggingLevelsResponseTypeDef",
    "DescribeMitigationActionResponseTypeDef",
    "MitigationActionTypeDef",
    "CreateMitigationActionRequestRequestTypeDef",
    "UpdateMitigationActionRequestRequestTypeDef",
    "RepublishActionOutputTypeDef",
    "RepublishActionTypeDef",
    "AuditSuppressionTypeDef",
    "DescribeAuditSuppressionResponseTypeDef",
    "NonCompliantResourceTypeDef",
    "RelatedResourceTypeDef",
    "CreateAuditSuppressionRequestRequestTypeDef",
    "DeleteAuditSuppressionRequestRequestTypeDef",
    "DescribeAuditSuppressionRequestRequestTypeDef",
    "ListAuditFindingsRequestListAuditFindingsPaginateTypeDef",
    "ListAuditFindingsRequestRequestTypeDef",
    "ListAuditSuppressionsRequestListAuditSuppressionsPaginateTypeDef",
    "ListAuditSuppressionsRequestRequestTypeDef",
    "UpdateAuditSuppressionRequestRequestTypeDef",
    "SearchIndexResponseTypeDef",
    "CreateTopicRuleDestinationRequestRequestTypeDef",
    "ListTopicRuleDestinationsResponseTypeDef",
    "CreateTopicRuleDestinationResponseTypeDef",
    "GetTopicRuleDestinationResponseTypeDef",
    "AuthResultTypeDef",
    "IotSiteWiseActionOutputTypeDef",
    "IotSiteWiseActionTypeDef",
    "ActiveViolationTypeDef",
    "DescribeSecurityProfileResponseTypeDef",
    "UpdateSecurityProfileResponseTypeDef",
    "ViolationEventTypeDef",
    "CreateSecurityProfileRequestRequestTypeDef",
    "UpdateSecurityProfileRequestRequestTypeDef",
    "ValidateSecurityProfileBehaviorsRequestRequestTypeDef",
    "CodeSigningOutputTypeDef",
    "CodeSigningTypeDef",
    "DescribeJobTemplateResponseTypeDef",
    "JobTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobTemplateRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "DescribeStreamResponseTypeDef",
    "DescribeAuditMitigationActionsTaskResponseTypeDef",
    "DetectMitigationActionsTaskSummaryTypeDef",
    "ListAuditSuppressionsResponseTypeDef",
    "AuditFindingTypeDef",
    "ListRelatedResourcesForAuditFindingResponseTypeDef",
    "TestAuthorizationResponseTypeDef",
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "ListActiveViolationsResponseTypeDef",
    "ListViolationEventsResponseTypeDef",
    "OTAUpdateFileOutputTypeDef",
    "OTAUpdateFileTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeDetectMitigationActionsTaskResponseTypeDef",
    "ListDetectMitigationActionsTasksResponseTypeDef",
    "DescribeAuditFindingResponseTypeDef",
    "ListAuditFindingsResponseTypeDef",
    "TopicRuleTypeDef",
    "TopicRulePayloadTypeDef",
    "OTAUpdateInfoTypeDef",
    "CreateOTAUpdateRequestRequestTypeDef",
    "GetTopicRuleResponseTypeDef",
    "CreateTopicRuleRequestRequestTypeDef",
    "ReplaceTopicRuleRequestRequestTypeDef",
    "GetOTAUpdateResponseTypeDef",
)

AbortCriteriaOutputTypeDef = TypedDict(
    "AbortCriteriaOutputTypeDef",
    {
        "failureType": JobExecutionFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

AbortCriteriaTypeDef = TypedDict(
    "AbortCriteriaTypeDef",
    {
        "failureType": JobExecutionFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

_RequiredAcceptCertificateTransferRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptCertificateTransferRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalAcceptCertificateTransferRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptCertificateTransferRequestRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)


class AcceptCertificateTransferRequestRequestTypeDef(
    _RequiredAcceptCertificateTransferRequestRequestTypeDef,
    _OptionalAcceptCertificateTransferRequestRequestTypeDef,
):
    pass


CloudwatchAlarmActionOutputTypeDef = TypedDict(
    "CloudwatchAlarmActionOutputTypeDef",
    {
        "roleArn": str,
        "alarmName": str,
        "stateReason": str,
        "stateValue": str,
    },
)

_RequiredCloudwatchLogsActionOutputTypeDef = TypedDict(
    "_RequiredCloudwatchLogsActionOutputTypeDef",
    {
        "roleArn": str,
        "logGroupName": str,
    },
)
_OptionalCloudwatchLogsActionOutputTypeDef = TypedDict(
    "_OptionalCloudwatchLogsActionOutputTypeDef",
    {
        "batchMode": bool,
    },
    total=False,
)


class CloudwatchLogsActionOutputTypeDef(
    _RequiredCloudwatchLogsActionOutputTypeDef, _OptionalCloudwatchLogsActionOutputTypeDef
):
    pass


_RequiredCloudwatchMetricActionOutputTypeDef = TypedDict(
    "_RequiredCloudwatchMetricActionOutputTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
    },
)
_OptionalCloudwatchMetricActionOutputTypeDef = TypedDict(
    "_OptionalCloudwatchMetricActionOutputTypeDef",
    {
        "metricTimestamp": str,
    },
    total=False,
)


class CloudwatchMetricActionOutputTypeDef(
    _RequiredCloudwatchMetricActionOutputTypeDef, _OptionalCloudwatchMetricActionOutputTypeDef
):
    pass


_RequiredDynamoDBActionOutputTypeDef = TypedDict(
    "_RequiredDynamoDBActionOutputTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "hashKeyField": str,
        "hashKeyValue": str,
    },
)
_OptionalDynamoDBActionOutputTypeDef = TypedDict(
    "_OptionalDynamoDBActionOutputTypeDef",
    {
        "operation": str,
        "hashKeyType": DynamoKeyTypeType,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": DynamoKeyTypeType,
        "payloadField": str,
    },
    total=False,
)


class DynamoDBActionOutputTypeDef(
    _RequiredDynamoDBActionOutputTypeDef, _OptionalDynamoDBActionOutputTypeDef
):
    pass


ElasticsearchActionOutputTypeDef = TypedDict(
    "ElasticsearchActionOutputTypeDef",
    {
        "roleArn": str,
        "endpoint": str,
        "index": str,
        "type": str,
        "id": str,
    },
)

_RequiredFirehoseActionOutputTypeDef = TypedDict(
    "_RequiredFirehoseActionOutputTypeDef",
    {
        "roleArn": str,
        "deliveryStreamName": str,
    },
)
_OptionalFirehoseActionOutputTypeDef = TypedDict(
    "_OptionalFirehoseActionOutputTypeDef",
    {
        "separator": str,
        "batchMode": bool,
    },
    total=False,
)


class FirehoseActionOutputTypeDef(
    _RequiredFirehoseActionOutputTypeDef, _OptionalFirehoseActionOutputTypeDef
):
    pass


IotAnalyticsActionOutputTypeDef = TypedDict(
    "IotAnalyticsActionOutputTypeDef",
    {
        "channelArn": str,
        "channelName": str,
        "batchMode": bool,
        "roleArn": str,
    },
    total=False,
)

_RequiredIotEventsActionOutputTypeDef = TypedDict(
    "_RequiredIotEventsActionOutputTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)
_OptionalIotEventsActionOutputTypeDef = TypedDict(
    "_OptionalIotEventsActionOutputTypeDef",
    {
        "messageId": str,
        "batchMode": bool,
    },
    total=False,
)


class IotEventsActionOutputTypeDef(
    _RequiredIotEventsActionOutputTypeDef, _OptionalIotEventsActionOutputTypeDef
):
    pass


_RequiredKafkaActionOutputTypeDef = TypedDict(
    "_RequiredKafkaActionOutputTypeDef",
    {
        "destinationArn": str,
        "topic": str,
        "clientProperties": Dict[str, str],
    },
)
_OptionalKafkaActionOutputTypeDef = TypedDict(
    "_OptionalKafkaActionOutputTypeDef",
    {
        "key": str,
        "partition": str,
    },
    total=False,
)


class KafkaActionOutputTypeDef(
    _RequiredKafkaActionOutputTypeDef, _OptionalKafkaActionOutputTypeDef
):
    pass


_RequiredKinesisActionOutputTypeDef = TypedDict(
    "_RequiredKinesisActionOutputTypeDef",
    {
        "roleArn": str,
        "streamName": str,
    },
)
_OptionalKinesisActionOutputTypeDef = TypedDict(
    "_OptionalKinesisActionOutputTypeDef",
    {
        "partitionKey": str,
    },
    total=False,
)


class KinesisActionOutputTypeDef(
    _RequiredKinesisActionOutputTypeDef, _OptionalKinesisActionOutputTypeDef
):
    pass


LambdaActionOutputTypeDef = TypedDict(
    "LambdaActionOutputTypeDef",
    {
        "functionArn": str,
    },
)

OpenSearchActionOutputTypeDef = TypedDict(
    "OpenSearchActionOutputTypeDef",
    {
        "roleArn": str,
        "endpoint": str,
        "index": str,
        "type": str,
        "id": str,
    },
)

_RequiredS3ActionOutputTypeDef = TypedDict(
    "_RequiredS3ActionOutputTypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
    },
)
_OptionalS3ActionOutputTypeDef = TypedDict(
    "_OptionalS3ActionOutputTypeDef",
    {
        "cannedAcl": CannedAccessControlListType,
    },
    total=False,
)


class S3ActionOutputTypeDef(_RequiredS3ActionOutputTypeDef, _OptionalS3ActionOutputTypeDef):
    pass


SalesforceActionOutputTypeDef = TypedDict(
    "SalesforceActionOutputTypeDef",
    {
        "token": str,
        "url": str,
    },
)

_RequiredSnsActionOutputTypeDef = TypedDict(
    "_RequiredSnsActionOutputTypeDef",
    {
        "targetArn": str,
        "roleArn": str,
    },
)
_OptionalSnsActionOutputTypeDef = TypedDict(
    "_OptionalSnsActionOutputTypeDef",
    {
        "messageFormat": MessageFormatType,
    },
    total=False,
)


class SnsActionOutputTypeDef(_RequiredSnsActionOutputTypeDef, _OptionalSnsActionOutputTypeDef):
    pass


_RequiredSqsActionOutputTypeDef = TypedDict(
    "_RequiredSqsActionOutputTypeDef",
    {
        "roleArn": str,
        "queueUrl": str,
    },
)
_OptionalSqsActionOutputTypeDef = TypedDict(
    "_OptionalSqsActionOutputTypeDef",
    {
        "useBase64": bool,
    },
    total=False,
)


class SqsActionOutputTypeDef(_RequiredSqsActionOutputTypeDef, _OptionalSqsActionOutputTypeDef):
    pass


_RequiredStepFunctionsActionOutputTypeDef = TypedDict(
    "_RequiredStepFunctionsActionOutputTypeDef",
    {
        "stateMachineName": str,
        "roleArn": str,
    },
)
_OptionalStepFunctionsActionOutputTypeDef = TypedDict(
    "_OptionalStepFunctionsActionOutputTypeDef",
    {
        "executionNamePrefix": str,
    },
    total=False,
)


class StepFunctionsActionOutputTypeDef(
    _RequiredStepFunctionsActionOutputTypeDef, _OptionalStepFunctionsActionOutputTypeDef
):
    pass


CloudwatchAlarmActionTypeDef = TypedDict(
    "CloudwatchAlarmActionTypeDef",
    {
        "roleArn": str,
        "alarmName": str,
        "stateReason": str,
        "stateValue": str,
    },
)

_RequiredCloudwatchLogsActionTypeDef = TypedDict(
    "_RequiredCloudwatchLogsActionTypeDef",
    {
        "roleArn": str,
        "logGroupName": str,
    },
)
_OptionalCloudwatchLogsActionTypeDef = TypedDict(
    "_OptionalCloudwatchLogsActionTypeDef",
    {
        "batchMode": bool,
    },
    total=False,
)


class CloudwatchLogsActionTypeDef(
    _RequiredCloudwatchLogsActionTypeDef, _OptionalCloudwatchLogsActionTypeDef
):
    pass


_RequiredCloudwatchMetricActionTypeDef = TypedDict(
    "_RequiredCloudwatchMetricActionTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
    },
)
_OptionalCloudwatchMetricActionTypeDef = TypedDict(
    "_OptionalCloudwatchMetricActionTypeDef",
    {
        "metricTimestamp": str,
    },
    total=False,
)


class CloudwatchMetricActionTypeDef(
    _RequiredCloudwatchMetricActionTypeDef, _OptionalCloudwatchMetricActionTypeDef
):
    pass


_RequiredDynamoDBActionTypeDef = TypedDict(
    "_RequiredDynamoDBActionTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "hashKeyField": str,
        "hashKeyValue": str,
    },
)
_OptionalDynamoDBActionTypeDef = TypedDict(
    "_OptionalDynamoDBActionTypeDef",
    {
        "operation": str,
        "hashKeyType": DynamoKeyTypeType,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": DynamoKeyTypeType,
        "payloadField": str,
    },
    total=False,
)


class DynamoDBActionTypeDef(_RequiredDynamoDBActionTypeDef, _OptionalDynamoDBActionTypeDef):
    pass


ElasticsearchActionTypeDef = TypedDict(
    "ElasticsearchActionTypeDef",
    {
        "roleArn": str,
        "endpoint": str,
        "index": str,
        "type": str,
        "id": str,
    },
)

_RequiredFirehoseActionTypeDef = TypedDict(
    "_RequiredFirehoseActionTypeDef",
    {
        "roleArn": str,
        "deliveryStreamName": str,
    },
)
_OptionalFirehoseActionTypeDef = TypedDict(
    "_OptionalFirehoseActionTypeDef",
    {
        "separator": str,
        "batchMode": bool,
    },
    total=False,
)


class FirehoseActionTypeDef(_RequiredFirehoseActionTypeDef, _OptionalFirehoseActionTypeDef):
    pass


IotAnalyticsActionTypeDef = TypedDict(
    "IotAnalyticsActionTypeDef",
    {
        "channelArn": str,
        "channelName": str,
        "batchMode": bool,
        "roleArn": str,
    },
    total=False,
)

_RequiredIotEventsActionTypeDef = TypedDict(
    "_RequiredIotEventsActionTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)
_OptionalIotEventsActionTypeDef = TypedDict(
    "_OptionalIotEventsActionTypeDef",
    {
        "messageId": str,
        "batchMode": bool,
    },
    total=False,
)


class IotEventsActionTypeDef(_RequiredIotEventsActionTypeDef, _OptionalIotEventsActionTypeDef):
    pass


_RequiredKafkaActionTypeDef = TypedDict(
    "_RequiredKafkaActionTypeDef",
    {
        "destinationArn": str,
        "topic": str,
        "clientProperties": Mapping[str, str],
    },
)
_OptionalKafkaActionTypeDef = TypedDict(
    "_OptionalKafkaActionTypeDef",
    {
        "key": str,
        "partition": str,
    },
    total=False,
)


class KafkaActionTypeDef(_RequiredKafkaActionTypeDef, _OptionalKafkaActionTypeDef):
    pass


_RequiredKinesisActionTypeDef = TypedDict(
    "_RequiredKinesisActionTypeDef",
    {
        "roleArn": str,
        "streamName": str,
    },
)
_OptionalKinesisActionTypeDef = TypedDict(
    "_OptionalKinesisActionTypeDef",
    {
        "partitionKey": str,
    },
    total=False,
)


class KinesisActionTypeDef(_RequiredKinesisActionTypeDef, _OptionalKinesisActionTypeDef):
    pass


LambdaActionTypeDef = TypedDict(
    "LambdaActionTypeDef",
    {
        "functionArn": str,
    },
)

OpenSearchActionTypeDef = TypedDict(
    "OpenSearchActionTypeDef",
    {
        "roleArn": str,
        "endpoint": str,
        "index": str,
        "type": str,
        "id": str,
    },
)

_RequiredS3ActionTypeDef = TypedDict(
    "_RequiredS3ActionTypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
    },
)
_OptionalS3ActionTypeDef = TypedDict(
    "_OptionalS3ActionTypeDef",
    {
        "cannedAcl": CannedAccessControlListType,
    },
    total=False,
)


class S3ActionTypeDef(_RequiredS3ActionTypeDef, _OptionalS3ActionTypeDef):
    pass


SalesforceActionTypeDef = TypedDict(
    "SalesforceActionTypeDef",
    {
        "token": str,
        "url": str,
    },
)

_RequiredSnsActionTypeDef = TypedDict(
    "_RequiredSnsActionTypeDef",
    {
        "targetArn": str,
        "roleArn": str,
    },
)
_OptionalSnsActionTypeDef = TypedDict(
    "_OptionalSnsActionTypeDef",
    {
        "messageFormat": MessageFormatType,
    },
    total=False,
)


class SnsActionTypeDef(_RequiredSnsActionTypeDef, _OptionalSnsActionTypeDef):
    pass


_RequiredSqsActionTypeDef = TypedDict(
    "_RequiredSqsActionTypeDef",
    {
        "roleArn": str,
        "queueUrl": str,
    },
)
_OptionalSqsActionTypeDef = TypedDict(
    "_OptionalSqsActionTypeDef",
    {
        "useBase64": bool,
    },
    total=False,
)


class SqsActionTypeDef(_RequiredSqsActionTypeDef, _OptionalSqsActionTypeDef):
    pass


_RequiredStepFunctionsActionTypeDef = TypedDict(
    "_RequiredStepFunctionsActionTypeDef",
    {
        "stateMachineName": str,
        "roleArn": str,
    },
)
_OptionalStepFunctionsActionTypeDef = TypedDict(
    "_OptionalStepFunctionsActionTypeDef",
    {
        "executionNamePrefix": str,
    },
    total=False,
)


class StepFunctionsActionTypeDef(
    _RequiredStepFunctionsActionTypeDef, _OptionalStepFunctionsActionTypeDef
):
    pass


MetricValueOutputTypeDef = TypedDict(
    "MetricValueOutputTypeDef",
    {
        "count": int,
        "cidrs": List[str],
        "ports": List[int],
        "number": float,
        "numbers": List[float],
        "strings": List[str],
    },
    total=False,
)

ViolationEventAdditionalInfoTypeDef = TypedDict(
    "ViolationEventAdditionalInfoTypeDef",
    {
        "confidenceLevel": ConfidenceLevelType,
    },
    total=False,
)

AddThingToBillingGroupRequestRequestTypeDef = TypedDict(
    "AddThingToBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "thingName": str,
        "thingArn": str,
    },
    total=False,
)

AddThingToThingGroupRequestRequestTypeDef = TypedDict(
    "AddThingToThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingName": str,
        "thingArn": str,
        "overrideDynamicGroups": bool,
    },
    total=False,
)

_RequiredAddThingsToThingGroupParamsOutputTypeDef = TypedDict(
    "_RequiredAddThingsToThingGroupParamsOutputTypeDef",
    {
        "thingGroupNames": List[str],
    },
)
_OptionalAddThingsToThingGroupParamsOutputTypeDef = TypedDict(
    "_OptionalAddThingsToThingGroupParamsOutputTypeDef",
    {
        "overrideDynamicGroups": bool,
    },
    total=False,
)


class AddThingsToThingGroupParamsOutputTypeDef(
    _RequiredAddThingsToThingGroupParamsOutputTypeDef,
    _OptionalAddThingsToThingGroupParamsOutputTypeDef,
):
    pass


_RequiredAddThingsToThingGroupParamsTypeDef = TypedDict(
    "_RequiredAddThingsToThingGroupParamsTypeDef",
    {
        "thingGroupNames": Sequence[str],
    },
)
_OptionalAddThingsToThingGroupParamsTypeDef = TypedDict(
    "_OptionalAddThingsToThingGroupParamsTypeDef",
    {
        "overrideDynamicGroups": bool,
    },
    total=False,
)


class AddThingsToThingGroupParamsTypeDef(
    _RequiredAddThingsToThingGroupParamsTypeDef, _OptionalAddThingsToThingGroupParamsTypeDef
):
    pass


_RequiredAggregationTypeOutputTypeDef = TypedDict(
    "_RequiredAggregationTypeOutputTypeDef",
    {
        "name": AggregationTypeNameType,
    },
)
_OptionalAggregationTypeOutputTypeDef = TypedDict(
    "_OptionalAggregationTypeOutputTypeDef",
    {
        "values": List[str],
    },
    total=False,
)


class AggregationTypeOutputTypeDef(
    _RequiredAggregationTypeOutputTypeDef, _OptionalAggregationTypeOutputTypeDef
):
    pass


_RequiredAggregationTypeTypeDef = TypedDict(
    "_RequiredAggregationTypeTypeDef",
    {
        "name": AggregationTypeNameType,
    },
)
_OptionalAggregationTypeTypeDef = TypedDict(
    "_OptionalAggregationTypeTypeDef",
    {
        "values": Sequence[str],
    },
    total=False,
)


class AggregationTypeTypeDef(_RequiredAggregationTypeTypeDef, _OptionalAggregationTypeTypeDef):
    pass


AlertTargetOutputTypeDef = TypedDict(
    "AlertTargetOutputTypeDef",
    {
        "alertTargetArn": str,
        "roleArn": str,
    },
)

AlertTargetTypeDef = TypedDict(
    "AlertTargetTypeDef",
    {
        "alertTargetArn": str,
        "roleArn": str,
    },
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "policyName": str,
        "policyArn": str,
    },
    total=False,
)

_RequiredAssetPropertyTimestampOutputTypeDef = TypedDict(
    "_RequiredAssetPropertyTimestampOutputTypeDef",
    {
        "timeInSeconds": str,
    },
)
_OptionalAssetPropertyTimestampOutputTypeDef = TypedDict(
    "_OptionalAssetPropertyTimestampOutputTypeDef",
    {
        "offsetInNanos": str,
    },
    total=False,
)


class AssetPropertyTimestampOutputTypeDef(
    _RequiredAssetPropertyTimestampOutputTypeDef, _OptionalAssetPropertyTimestampOutputTypeDef
):
    pass


_RequiredAssetPropertyTimestampTypeDef = TypedDict(
    "_RequiredAssetPropertyTimestampTypeDef",
    {
        "timeInSeconds": str,
    },
)
_OptionalAssetPropertyTimestampTypeDef = TypedDict(
    "_OptionalAssetPropertyTimestampTypeDef",
    {
        "offsetInNanos": str,
    },
    total=False,
)


class AssetPropertyTimestampTypeDef(
    _RequiredAssetPropertyTimestampTypeDef, _OptionalAssetPropertyTimestampTypeDef
):
    pass


AssetPropertyVariantOutputTypeDef = TypedDict(
    "AssetPropertyVariantOutputTypeDef",
    {
        "stringValue": str,
        "integerValue": str,
        "doubleValue": str,
        "booleanValue": str,
    },
    total=False,
)

AssetPropertyVariantTypeDef = TypedDict(
    "AssetPropertyVariantTypeDef",
    {
        "stringValue": str,
        "integerValue": str,
        "doubleValue": str,
        "booleanValue": str,
    },
    total=False,
)

_RequiredAssociateTargetsWithJobRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTargetsWithJobRequestRequestTypeDef",
    {
        "targets": Sequence[str],
        "jobId": str,
    },
)
_OptionalAssociateTargetsWithJobRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTargetsWithJobRequestRequestTypeDef",
    {
        "comment": str,
        "namespaceId": str,
    },
    total=False,
)


class AssociateTargetsWithJobRequestRequestTypeDef(
    _RequiredAssociateTargetsWithJobRequestRequestTypeDef,
    _OptionalAssociateTargetsWithJobRequestRequestTypeDef,
):
    pass


AssociateTargetsWithJobResponseTypeDef = TypedDict(
    "AssociateTargetsWithJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "target": str,
    },
)

AttachPrincipalPolicyRequestRequestTypeDef = TypedDict(
    "AttachPrincipalPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "principal": str,
    },
)

AttachSecurityProfileRequestRequestTypeDef = TypedDict(
    "AttachSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
        "securityProfileTargetArn": str,
    },
)

AttachThingPrincipalRequestRequestTypeDef = TypedDict(
    "AttachThingPrincipalRequestRequestTypeDef",
    {
        "thingName": str,
        "principal": str,
    },
)

AttributePayloadOutputTypeDef = TypedDict(
    "AttributePayloadOutputTypeDef",
    {
        "attributes": Dict[str, str],
        "merge": bool,
    },
    total=False,
)

AttributePayloadTypeDef = TypedDict(
    "AttributePayloadTypeDef",
    {
        "attributes": Mapping[str, str],
        "merge": bool,
    },
    total=False,
)

AuditCheckConfigurationOutputTypeDef = TypedDict(
    "AuditCheckConfigurationOutputTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

AuditCheckConfigurationTypeDef = TypedDict(
    "AuditCheckConfigurationTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

AuditCheckDetailsTypeDef = TypedDict(
    "AuditCheckDetailsTypeDef",
    {
        "checkRunStatus": AuditCheckRunStatusType,
        "checkCompliant": bool,
        "totalResourcesCount": int,
        "nonCompliantResourcesCount": int,
        "suppressedNonCompliantResourcesCount": int,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

AuditMitigationActionExecutionMetadataTypeDef = TypedDict(
    "AuditMitigationActionExecutionMetadataTypeDef",
    {
        "taskId": str,
        "findingId": str,
        "actionName": str,
        "actionId": str,
        "status": AuditMitigationActionsExecutionStatusType,
        "startTime": datetime,
        "endTime": datetime,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

AuditMitigationActionsTaskMetadataTypeDef = TypedDict(
    "AuditMitigationActionsTaskMetadataTypeDef",
    {
        "taskId": str,
        "startTime": datetime,
        "taskStatus": AuditMitigationActionsTaskStatusType,
    },
    total=False,
)

AuditMitigationActionsTaskTargetOutputTypeDef = TypedDict(
    "AuditMitigationActionsTaskTargetOutputTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)

AuditMitigationActionsTaskTargetTypeDef = TypedDict(
    "AuditMitigationActionsTaskTargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": Sequence[str],
        "auditCheckToReasonCodeFilter": Mapping[str, Sequence[str]],
    },
    total=False,
)

AuditNotificationTargetOutputTypeDef = TypedDict(
    "AuditNotificationTargetOutputTypeDef",
    {
        "targetArn": str,
        "roleArn": str,
        "enabled": bool,
    },
    total=False,
)

AuditNotificationTargetTypeDef = TypedDict(
    "AuditNotificationTargetTypeDef",
    {
        "targetArn": str,
        "roleArn": str,
        "enabled": bool,
    },
    total=False,
)

AuditTaskMetadataTypeDef = TypedDict(
    "AuditTaskMetadataTypeDef",
    {
        "taskId": str,
        "taskStatus": AuditTaskStatusType,
        "taskType": AuditTaskTypeType,
    },
    total=False,
)

_RequiredAuthInfoOutputTypeDef = TypedDict(
    "_RequiredAuthInfoOutputTypeDef",
    {
        "resources": List[str],
    },
)
_OptionalAuthInfoOutputTypeDef = TypedDict(
    "_OptionalAuthInfoOutputTypeDef",
    {
        "actionType": ActionTypeType,
    },
    total=False,
)


class AuthInfoOutputTypeDef(_RequiredAuthInfoOutputTypeDef, _OptionalAuthInfoOutputTypeDef):
    pass


_RequiredAuthInfoTypeDef = TypedDict(
    "_RequiredAuthInfoTypeDef",
    {
        "resources": Sequence[str],
    },
)
_OptionalAuthInfoTypeDef = TypedDict(
    "_OptionalAuthInfoTypeDef",
    {
        "actionType": ActionTypeType,
    },
    total=False,
)


class AuthInfoTypeDef(_RequiredAuthInfoTypeDef, _OptionalAuthInfoTypeDef):
    pass


AuthorizerConfigOutputTypeDef = TypedDict(
    "AuthorizerConfigOutputTypeDef",
    {
        "defaultAuthorizerName": str,
        "allowAuthorizerOverride": bool,
    },
    total=False,
)

AuthorizerConfigTypeDef = TypedDict(
    "AuthorizerConfigTypeDef",
    {
        "defaultAuthorizerName": str,
        "allowAuthorizerOverride": bool,
    },
    total=False,
)

AuthorizerDescriptionTypeDef = TypedDict(
    "AuthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": AuthorizerStatusType,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "signingDisabled": bool,
        "enableCachingForHttp": bool,
    },
    total=False,
)

AuthorizerSummaryTypeDef = TypedDict(
    "AuthorizerSummaryTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
    },
    total=False,
)

AwsJobAbortCriteriaTypeDef = TypedDict(
    "AwsJobAbortCriteriaTypeDef",
    {
        "failureType": AwsJobAbortCriteriaFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

AwsJobRateIncreaseCriteriaOutputTypeDef = TypedDict(
    "AwsJobRateIncreaseCriteriaOutputTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

AwsJobRateIncreaseCriteriaTypeDef = TypedDict(
    "AwsJobRateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

AwsJobPresignedUrlConfigOutputTypeDef = TypedDict(
    "AwsJobPresignedUrlConfigOutputTypeDef",
    {
        "expiresInSec": int,
    },
    total=False,
)

AwsJobPresignedUrlConfigTypeDef = TypedDict(
    "AwsJobPresignedUrlConfigTypeDef",
    {
        "expiresInSec": int,
    },
    total=False,
)

AwsJobTimeoutConfigTypeDef = TypedDict(
    "AwsJobTimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

MachineLearningDetectionConfigOutputTypeDef = TypedDict(
    "MachineLearningDetectionConfigOutputTypeDef",
    {
        "confidenceLevel": ConfidenceLevelType,
    },
)

StatisticalThresholdOutputTypeDef = TypedDict(
    "StatisticalThresholdOutputTypeDef",
    {
        "statistic": str,
    },
    total=False,
)

MachineLearningDetectionConfigTypeDef = TypedDict(
    "MachineLearningDetectionConfigTypeDef",
    {
        "confidenceLevel": ConfidenceLevelType,
    },
)

MetricValueTypeDef = TypedDict(
    "MetricValueTypeDef",
    {
        "count": int,
        "cidrs": Sequence[str],
        "ports": Sequence[int],
        "number": float,
        "numbers": Sequence[float],
        "strings": Sequence[str],
    },
    total=False,
)

StatisticalThresholdTypeDef = TypedDict(
    "StatisticalThresholdTypeDef",
    {
        "statistic": str,
    },
    total=False,
)

BehaviorModelTrainingSummaryTypeDef = TypedDict(
    "BehaviorModelTrainingSummaryTypeDef",
    {
        "securityProfileName": str,
        "behaviorName": str,
        "trainingDataCollectionStartDate": datetime,
        "modelStatus": ModelStatusType,
        "datapointsCollectionPercentage": float,
        "lastModelRefreshDate": datetime,
    },
    total=False,
)

_RequiredMetricDimensionOutputTypeDef = TypedDict(
    "_RequiredMetricDimensionOutputTypeDef",
    {
        "dimensionName": str,
    },
)
_OptionalMetricDimensionOutputTypeDef = TypedDict(
    "_OptionalMetricDimensionOutputTypeDef",
    {
        "operator": DimensionValueOperatorType,
    },
    total=False,
)


class MetricDimensionOutputTypeDef(
    _RequiredMetricDimensionOutputTypeDef, _OptionalMetricDimensionOutputTypeDef
):
    pass


_RequiredMetricDimensionTypeDef = TypedDict(
    "_RequiredMetricDimensionTypeDef",
    {
        "dimensionName": str,
    },
)
_OptionalMetricDimensionTypeDef = TypedDict(
    "_OptionalMetricDimensionTypeDef",
    {
        "operator": DimensionValueOperatorType,
    },
    total=False,
)


class MetricDimensionTypeDef(_RequiredMetricDimensionTypeDef, _OptionalMetricDimensionTypeDef):
    pass


BillingGroupMetadataTypeDef = TypedDict(
    "BillingGroupMetadataTypeDef",
    {
        "creationDate": datetime,
    },
    total=False,
)

BillingGroupPropertiesOutputTypeDef = TypedDict(
    "BillingGroupPropertiesOutputTypeDef",
    {
        "billingGroupDescription": str,
    },
    total=False,
)

BillingGroupPropertiesTypeDef = TypedDict(
    "BillingGroupPropertiesTypeDef",
    {
        "billingGroupDescription": str,
    },
    total=False,
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "keyValue": str,
        "count": int,
    },
    total=False,
)

TermsAggregationTypeDef = TypedDict(
    "TermsAggregationTypeDef",
    {
        "maxBuckets": int,
    },
    total=False,
)

CertificateValidityTypeDef = TypedDict(
    "CertificateValidityTypeDef",
    {
        "notBefore": datetime,
        "notAfter": datetime,
    },
    total=False,
)

CACertificateTypeDef = TypedDict(
    "CACertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CACertificateStatusType,
        "creationDate": datetime,
    },
    total=False,
)

CancelAuditMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "CancelAuditMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

CancelAuditTaskRequestRequestTypeDef = TypedDict(
    "CancelAuditTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

CancelCertificateTransferRequestRequestTypeDef = TypedDict(
    "CancelCertificateTransferRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)

CancelDetectMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "CancelDetectMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

_RequiredCancelJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredCancelJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
    },
)
_OptionalCancelJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalCancelJobExecutionRequestRequestTypeDef",
    {
        "force": bool,
        "expectedVersion": int,
        "statusDetails": Mapping[str, str],
    },
    total=False,
)


class CancelJobExecutionRequestRequestTypeDef(
    _RequiredCancelJobExecutionRequestRequestTypeDef,
    _OptionalCancelJobExecutionRequestRequestTypeDef,
):
    pass


_RequiredCancelJobRequestRequestTypeDef = TypedDict(
    "_RequiredCancelJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalCancelJobRequestRequestTypeDef = TypedDict(
    "_OptionalCancelJobRequestRequestTypeDef",
    {
        "reasonCode": str,
        "comment": str,
        "force": bool,
    },
    total=False,
)


class CancelJobRequestRequestTypeDef(
    _RequiredCancelJobRequestRequestTypeDef, _OptionalCancelJobRequestRequestTypeDef
):
    pass


CancelJobResponseTypeDef = TypedDict(
    "CancelJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransferDataTypeDef = TypedDict(
    "TransferDataTypeDef",
    {
        "transferMessage": str,
        "rejectReason": str,
        "transferDate": datetime,
        "acceptDate": datetime,
        "rejectDate": datetime,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CertificateStatusType,
        "certificateMode": CertificateModeType,
        "creationDate": datetime,
    },
    total=False,
)

CodeSigningCertificateChainOutputTypeDef = TypedDict(
    "CodeSigningCertificateChainOutputTypeDef",
    {
        "certificateName": str,
        "inlineDocument": str,
    },
    total=False,
)

CodeSigningCertificateChainTypeDef = TypedDict(
    "CodeSigningCertificateChainTypeDef",
    {
        "certificateName": str,
        "inlineDocument": str,
    },
    total=False,
)

CodeSigningSignatureOutputTypeDef = TypedDict(
    "CodeSigningSignatureOutputTypeDef",
    {
        "inlineDocument": bytes,
    },
    total=False,
)

CodeSigningSignatureTypeDef = TypedDict(
    "CodeSigningSignatureTypeDef",
    {
        "inlineDocument": Union[str, bytes, IO[Any], StreamingBody],
    },
    total=False,
)

ConfigurationOutputTypeDef = TypedDict(
    "ConfigurationOutputTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

ConfirmTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "ConfirmTopicRuleDestinationRequestRequestTypeDef",
    {
        "confirmationToken": str,
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


CreateAuthorizerResponseTypeDef = TypedDict(
    "CreateAuthorizerResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBillingGroupResponseTypeDef = TypedDict(
    "CreateBillingGroupResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "billingGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCertificateFromCsrRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCertificateFromCsrRequestRequestTypeDef",
    {
        "certificateSigningRequest": str,
    },
)
_OptionalCreateCertificateFromCsrRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCertificateFromCsrRequestRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)


class CreateCertificateFromCsrRequestRequestTypeDef(
    _RequiredCreateCertificateFromCsrRequestRequestTypeDef,
    _OptionalCreateCertificateFromCsrRequestRequestTypeDef,
):
    pass


CreateCertificateFromCsrResponseTypeDef = TypedDict(
    "CreateCertificateFromCsrResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomMetricResponseTypeDef = TypedDict(
    "CreateCustomMetricResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDimensionResponseTypeDef = TypedDict(
    "CreateDimensionResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TlsConfigTypeDef = TypedDict(
    "TlsConfigTypeDef",
    {
        "securityPolicy": str,
    },
    total=False,
)

CreateDomainConfigurationResponseTypeDef = TypedDict(
    "CreateDomainConfigurationResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDynamicThingGroupResponseTypeDef = TypedDict(
    "CreateDynamicThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetMetricResponseTypeDef = TypedDict(
    "CreateFleetMetricResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PresignedUrlConfigTypeDef = TypedDict(
    "PresignedUrlConfigTypeDef",
    {
        "roleArn": str,
        "expiresInSec": int,
    },
    total=False,
)

TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MaintenanceWindowTypeDef = TypedDict(
    "MaintenanceWindowTypeDef",
    {
        "startTime": str,
        "durationInMinutes": int,
    },
)

CreateJobTemplateResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeysAndCertificateRequestRequestTypeDef = TypedDict(
    "CreateKeysAndCertificateRequestRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "PublicKey": str,
        "PrivateKey": str,
    },
    total=False,
)

CreateMitigationActionResponseTypeDef = TypedDict(
    "CreateMitigationActionResponseTypeDef",
    {
        "actionArn": str,
        "actionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOTAUpdateResponseTypeDef = TypedDict(
    "CreateOTAUpdateResponseTypeDef",
    {
        "otaUpdateId": str,
        "awsIotJobId": str,
        "otaUpdateArn": str,
        "awsIotJobArn": str,
        "otaUpdateStatus": OTAUpdateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackageRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageRequestRequestTypeDef",
    {
        "packageName": str,
    },
)
_OptionalCreatePackageRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackageRequestRequestTypeDef",
    {
        "description": str,
        "tags": Mapping[str, str],
        "clientToken": str,
    },
    total=False,
)


class CreatePackageRequestRequestTypeDef(
    _RequiredCreatePackageRequestRequestTypeDef, _OptionalCreatePackageRequestRequestTypeDef
):
    pass


CreatePackageResponseTypeDef = TypedDict(
    "CreatePackageResponseTypeDef",
    {
        "packageName": str,
        "packageArn": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageVersionRequestRequestTypeDef",
    {
        "packageName": str,
        "versionName": str,
    },
)
_OptionalCreatePackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackageVersionRequestRequestTypeDef",
    {
        "description": str,
        "attributes": Mapping[str, str],
        "tags": Mapping[str, str],
        "clientToken": str,
    },
    total=False,
)


class CreatePackageVersionRequestRequestTypeDef(
    _RequiredCreatePackageVersionRequestRequestTypeDef,
    _OptionalCreatePackageVersionRequestRequestTypeDef,
):
    pass


CreatePackageVersionResponseTypeDef = TypedDict(
    "CreatePackageVersionResponseTypeDef",
    {
        "packageVersionArn": str,
        "packageName": str,
        "versionName": str,
        "description": str,
        "attributes": Dict[str, str],
        "status": PackageVersionStatusType,
        "errorReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePolicyResponseTypeDef = TypedDict(
    "CreatePolicyResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "policyVersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyVersionRequestRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
    },
)
_OptionalCreatePolicyVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyVersionRequestRequestTypeDef",
    {
        "setAsDefault": bool,
    },
    total=False,
)


class CreatePolicyVersionRequestRequestTypeDef(
    _RequiredCreatePolicyVersionRequestRequestTypeDef,
    _OptionalCreatePolicyVersionRequestRequestTypeDef,
):
    pass


CreatePolicyVersionResponseTypeDef = TypedDict(
    "CreatePolicyVersionResponseTypeDef",
    {
        "policyArn": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProvisioningClaimRequestRequestTypeDef = TypedDict(
    "CreateProvisioningClaimRequestRequestTypeDef",
    {
        "templateName": str,
    },
)

_RequiredProvisioningHookTypeDef = TypedDict(
    "_RequiredProvisioningHookTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalProvisioningHookTypeDef = TypedDict(
    "_OptionalProvisioningHookTypeDef",
    {
        "payloadVersion": str,
    },
    total=False,
)


class ProvisioningHookTypeDef(_RequiredProvisioningHookTypeDef, _OptionalProvisioningHookTypeDef):
    pass


CreateProvisioningTemplateResponseTypeDef = TypedDict(
    "CreateProvisioningTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "defaultVersionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisioningTemplateVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProvisioningTemplateVersionRequestRequestTypeDef",
    {
        "templateName": str,
        "templateBody": str,
    },
)
_OptionalCreateProvisioningTemplateVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProvisioningTemplateVersionRequestRequestTypeDef",
    {
        "setAsDefault": bool,
    },
    total=False,
)


class CreateProvisioningTemplateVersionRequestRequestTypeDef(
    _RequiredCreateProvisioningTemplateVersionRequestRequestTypeDef,
    _OptionalCreateProvisioningTemplateVersionRequestRequestTypeDef,
):
    pass


CreateProvisioningTemplateVersionResponseTypeDef = TypedDict(
    "CreateProvisioningTemplateVersionResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "versionId": int,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRoleAliasResponseTypeDef = TypedDict(
    "CreateRoleAliasResponseTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScheduledAuditResponseTypeDef = TypedDict(
    "CreateScheduledAuditResponseTypeDef",
    {
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSecurityProfileResponseTypeDef = TypedDict(
    "CreateSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamResponseTypeDef = TypedDict(
    "CreateStreamResponseTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "description": str,
        "streamVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateThingGroupResponseTypeDef = TypedDict(
    "CreateThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateThingResponseTypeDef = TypedDict(
    "CreateThingResponseTypeDef",
    {
        "thingName": str,
        "thingArn": str,
        "thingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThingTypePropertiesTypeDef = TypedDict(
    "ThingTypePropertiesTypeDef",
    {
        "thingTypeDescription": str,
        "searchableAttributes": Sequence[str],
    },
    total=False,
)

CreateThingTypeResponseTypeDef = TypedDict(
    "CreateThingTypeResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccountAuditConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAccountAuditConfigurationRequestRequestTypeDef",
    {
        "deleteScheduledAudits": bool,
    },
    total=False,
)

DeleteAuthorizerRequestRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)

_RequiredDeleteBillingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalDeleteBillingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBillingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteBillingGroupRequestRequestTypeDef(
    _RequiredDeleteBillingGroupRequestRequestTypeDef,
    _OptionalDeleteBillingGroupRequestRequestTypeDef,
):
    pass


DeleteCACertificateRequestRequestTypeDef = TypedDict(
    "DeleteCACertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)

_RequiredDeleteCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalDeleteCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCertificateRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)


class DeleteCertificateRequestRequestTypeDef(
    _RequiredDeleteCertificateRequestRequestTypeDef, _OptionalDeleteCertificateRequestRequestTypeDef
):
    pass


DeleteCustomMetricRequestRequestTypeDef = TypedDict(
    "DeleteCustomMetricRequestRequestTypeDef",
    {
        "metricName": str,
    },
)

DeleteDimensionRequestRequestTypeDef = TypedDict(
    "DeleteDimensionRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteDomainConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteDomainConfigurationRequestRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)

_RequiredDeleteDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDynamicThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalDeleteDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDynamicThingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteDynamicThingGroupRequestRequestTypeDef(
    _RequiredDeleteDynamicThingGroupRequestRequestTypeDef,
    _OptionalDeleteDynamicThingGroupRequestRequestTypeDef,
):
    pass


_RequiredDeleteFleetMetricRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFleetMetricRequestRequestTypeDef",
    {
        "metricName": str,
    },
)
_OptionalDeleteFleetMetricRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFleetMetricRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteFleetMetricRequestRequestTypeDef(
    _RequiredDeleteFleetMetricRequestRequestTypeDef, _OptionalDeleteFleetMetricRequestRequestTypeDef
):
    pass


_RequiredDeleteJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "executionNumber": int,
    },
)
_OptionalDeleteJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteJobExecutionRequestRequestTypeDef",
    {
        "force": bool,
        "namespaceId": str,
    },
    total=False,
)


class DeleteJobExecutionRequestRequestTypeDef(
    _RequiredDeleteJobExecutionRequestRequestTypeDef,
    _OptionalDeleteJobExecutionRequestRequestTypeDef,
):
    pass


_RequiredDeleteJobRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalDeleteJobRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteJobRequestRequestTypeDef",
    {
        "force": bool,
        "namespaceId": str,
    },
    total=False,
)


class DeleteJobRequestRequestTypeDef(
    _RequiredDeleteJobRequestRequestTypeDef, _OptionalDeleteJobRequestRequestTypeDef
):
    pass


DeleteJobTemplateRequestRequestTypeDef = TypedDict(
    "DeleteJobTemplateRequestRequestTypeDef",
    {
        "jobTemplateId": str,
    },
)

DeleteMitigationActionRequestRequestTypeDef = TypedDict(
    "DeleteMitigationActionRequestRequestTypeDef",
    {
        "actionName": str,
    },
)

_RequiredDeleteOTAUpdateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteOTAUpdateRequestRequestTypeDef",
    {
        "otaUpdateId": str,
    },
)
_OptionalDeleteOTAUpdateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteOTAUpdateRequestRequestTypeDef",
    {
        "deleteStream": bool,
        "forceDeleteAWSJob": bool,
    },
    total=False,
)


class DeleteOTAUpdateRequestRequestTypeDef(
    _RequiredDeleteOTAUpdateRequestRequestTypeDef, _OptionalDeleteOTAUpdateRequestRequestTypeDef
):
    pass


_RequiredDeletePackageRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageRequestRequestTypeDef",
    {
        "packageName": str,
    },
)
_OptionalDeletePackageRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeletePackageRequestRequestTypeDef(
    _RequiredDeletePackageRequestRequestTypeDef, _OptionalDeletePackageRequestRequestTypeDef
):
    pass


_RequiredDeletePackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageVersionRequestRequestTypeDef",
    {
        "packageName": str,
        "versionName": str,
    },
)
_OptionalDeletePackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageVersionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeletePackageVersionRequestRequestTypeDef(
    _RequiredDeletePackageVersionRequestRequestTypeDef,
    _OptionalDeletePackageVersionRequestRequestTypeDef,
):
    pass


DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "policyName": str,
    },
)

DeletePolicyVersionRequestRequestTypeDef = TypedDict(
    "DeletePolicyVersionRequestRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

DeleteProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "DeleteProvisioningTemplateRequestRequestTypeDef",
    {
        "templateName": str,
    },
)

DeleteProvisioningTemplateVersionRequestRequestTypeDef = TypedDict(
    "DeleteProvisioningTemplateVersionRequestRequestTypeDef",
    {
        "templateName": str,
        "versionId": int,
    },
)

DeleteRoleAliasRequestRequestTypeDef = TypedDict(
    "DeleteRoleAliasRequestRequestTypeDef",
    {
        "roleAlias": str,
    },
)

DeleteScheduledAuditRequestRequestTypeDef = TypedDict(
    "DeleteScheduledAuditRequestRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)

_RequiredDeleteSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalDeleteSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSecurityProfileRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteSecurityProfileRequestRequestTypeDef(
    _RequiredDeleteSecurityProfileRequestRequestTypeDef,
    _OptionalDeleteSecurityProfileRequestRequestTypeDef,
):
    pass


DeleteStreamRequestRequestTypeDef = TypedDict(
    "DeleteStreamRequestRequestTypeDef",
    {
        "streamId": str,
    },
)

_RequiredDeleteThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalDeleteThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteThingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteThingGroupRequestRequestTypeDef(
    _RequiredDeleteThingGroupRequestRequestTypeDef, _OptionalDeleteThingGroupRequestRequestTypeDef
):
    pass


_RequiredDeleteThingRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalDeleteThingRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteThingRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class DeleteThingRequestRequestTypeDef(
    _RequiredDeleteThingRequestRequestTypeDef, _OptionalDeleteThingRequestRequestTypeDef
):
    pass


DeleteThingTypeRequestRequestTypeDef = TypedDict(
    "DeleteThingTypeRequestRequestTypeDef",
    {
        "thingTypeName": str,
    },
)

DeleteTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "DeleteTopicRuleDestinationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTopicRuleRequestRequestTypeDef = TypedDict(
    "DeleteTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
    },
)

DeleteV2LoggingLevelRequestRequestTypeDef = TypedDict(
    "DeleteV2LoggingLevelRequestRequestTypeDef",
    {
        "targetType": LogTargetTypeType,
        "targetName": str,
    },
)

_RequiredDeprecateThingTypeRequestRequestTypeDef = TypedDict(
    "_RequiredDeprecateThingTypeRequestRequestTypeDef",
    {
        "thingTypeName": str,
    },
)
_OptionalDeprecateThingTypeRequestRequestTypeDef = TypedDict(
    "_OptionalDeprecateThingTypeRequestRequestTypeDef",
    {
        "undoDeprecate": bool,
    },
    total=False,
)


class DeprecateThingTypeRequestRequestTypeDef(
    _RequiredDeprecateThingTypeRequestRequestTypeDef,
    _OptionalDeprecateThingTypeRequestRequestTypeDef,
):
    pass


DescribeAuditFindingRequestRequestTypeDef = TypedDict(
    "DescribeAuditFindingRequestRequestTypeDef",
    {
        "findingId": str,
    },
)

DescribeAuditMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "DescribeAuditMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

TaskStatisticsForAuditCheckTypeDef = TypedDict(
    "TaskStatisticsForAuditCheckTypeDef",
    {
        "totalFindingsCount": int,
        "failedFindingsCount": int,
        "succeededFindingsCount": int,
        "skippedFindingsCount": int,
        "canceledFindingsCount": int,
    },
    total=False,
)

DescribeAuditTaskRequestRequestTypeDef = TypedDict(
    "DescribeAuditTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

TaskStatisticsTypeDef = TypedDict(
    "TaskStatisticsTypeDef",
    {
        "totalChecks": int,
        "inProgressChecks": int,
        "waitingForDataCollectionChecks": int,
        "compliantChecks": int,
        "nonCompliantChecks": int,
        "failedChecks": int,
        "canceledChecks": int,
    },
    total=False,
)

DescribeAuthorizerRequestRequestTypeDef = TypedDict(
    "DescribeAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)

DescribeBillingGroupRequestRequestTypeDef = TypedDict(
    "DescribeBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
    },
)

DescribeCACertificateRequestRequestTypeDef = TypedDict(
    "DescribeCACertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)

RegistrationConfigOutputTypeDef = TypedDict(
    "RegistrationConfigOutputTypeDef",
    {
        "templateBody": str,
        "roleArn": str,
        "templateName": str,
    },
    total=False,
)

DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)

DescribeCustomMetricRequestRequestTypeDef = TypedDict(
    "DescribeCustomMetricRequestRequestTypeDef",
    {
        "metricName": str,
    },
)

DescribeCustomMetricResponseTypeDef = TypedDict(
    "DescribeCustomMetricResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "metricType": CustomMetricTypeType,
        "displayName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDetectMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "DescribeDetectMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeDimensionRequestRequestTypeDef = TypedDict(
    "DescribeDimensionRequestRequestTypeDef",
    {
        "name": str,
    },
)

DescribeDimensionResponseTypeDef = TypedDict(
    "DescribeDimensionResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeDomainConfigurationRequestRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)

ServerCertificateSummaryTypeDef = TypedDict(
    "ServerCertificateSummaryTypeDef",
    {
        "serverCertificateArn": str,
        "serverCertificateStatus": ServerCertificateStatusType,
        "serverCertificateStatusDetail": str,
    },
    total=False,
)

TlsConfigOutputTypeDef = TypedDict(
    "TlsConfigOutputTypeDef",
    {
        "securityPolicy": str,
    },
    total=False,
)

DescribeEndpointRequestRequestTypeDef = TypedDict(
    "DescribeEndpointRequestRequestTypeDef",
    {
        "endpointType": str,
    },
    total=False,
)

DescribeEndpointResponseTypeDef = TypedDict(
    "DescribeEndpointResponseTypeDef",
    {
        "endpointAddress": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetMetricRequestRequestTypeDef = TypedDict(
    "DescribeFleetMetricRequestRequestTypeDef",
    {
        "metricName": str,
    },
)

DescribeIndexRequestRequestTypeDef = TypedDict(
    "DescribeIndexRequestRequestTypeDef",
    {
        "indexName": str,
    },
)

DescribeIndexResponseTypeDef = TypedDict(
    "DescribeIndexResponseTypeDef",
    {
        "indexName": str,
        "indexStatus": IndexStatusType,
        "schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
    },
)
_OptionalDescribeJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeJobExecutionRequestRequestTypeDef",
    {
        "executionNumber": int,
    },
    total=False,
)


class DescribeJobExecutionRequestRequestTypeDef(
    _RequiredDescribeJobExecutionRequestRequestTypeDef,
    _OptionalDescribeJobExecutionRequestRequestTypeDef,
):
    pass


DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeJobTemplateRequestRequestTypeDef = TypedDict(
    "DescribeJobTemplateRequestRequestTypeDef",
    {
        "jobTemplateId": str,
    },
)

MaintenanceWindowOutputTypeDef = TypedDict(
    "MaintenanceWindowOutputTypeDef",
    {
        "startTime": str,
        "durationInMinutes": int,
    },
)

PresignedUrlConfigOutputTypeDef = TypedDict(
    "PresignedUrlConfigOutputTypeDef",
    {
        "roleArn": str,
        "expiresInSec": int,
    },
    total=False,
)

TimeoutConfigOutputTypeDef = TypedDict(
    "TimeoutConfigOutputTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

_RequiredDescribeManagedJobTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeManagedJobTemplateRequestRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalDescribeManagedJobTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeManagedJobTemplateRequestRequestTypeDef",
    {
        "templateVersion": str,
    },
    total=False,
)


class DescribeManagedJobTemplateRequestRequestTypeDef(
    _RequiredDescribeManagedJobTemplateRequestRequestTypeDef,
    _OptionalDescribeManagedJobTemplateRequestRequestTypeDef,
):
    pass


DocumentParameterTypeDef = TypedDict(
    "DocumentParameterTypeDef",
    {
        "key": str,
        "description": str,
        "regex": str,
        "example": str,
        "optional": bool,
    },
    total=False,
)

DescribeMitigationActionRequestRequestTypeDef = TypedDict(
    "DescribeMitigationActionRequestRequestTypeDef",
    {
        "actionName": str,
    },
)

DescribeProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "DescribeProvisioningTemplateRequestRequestTypeDef",
    {
        "templateName": str,
    },
)

_RequiredProvisioningHookOutputTypeDef = TypedDict(
    "_RequiredProvisioningHookOutputTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalProvisioningHookOutputTypeDef = TypedDict(
    "_OptionalProvisioningHookOutputTypeDef",
    {
        "payloadVersion": str,
    },
    total=False,
)


class ProvisioningHookOutputTypeDef(
    _RequiredProvisioningHookOutputTypeDef, _OptionalProvisioningHookOutputTypeDef
):
    pass


DescribeProvisioningTemplateVersionRequestRequestTypeDef = TypedDict(
    "DescribeProvisioningTemplateVersionRequestRequestTypeDef",
    {
        "templateName": str,
        "versionId": int,
    },
)

DescribeProvisioningTemplateVersionResponseTypeDef = TypedDict(
    "DescribeProvisioningTemplateVersionResponseTypeDef",
    {
        "versionId": int,
        "creationDate": datetime,
        "templateBody": str,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoleAliasRequestRequestTypeDef = TypedDict(
    "DescribeRoleAliasRequestRequestTypeDef",
    {
        "roleAlias": str,
    },
)

RoleAliasDescriptionTypeDef = TypedDict(
    "RoleAliasDescriptionTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "roleArn": str,
        "owner": str,
        "credentialDurationSeconds": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

DescribeScheduledAuditRequestRequestTypeDef = TypedDict(
    "DescribeScheduledAuditRequestRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)

DescribeScheduledAuditResponseTypeDef = TypedDict(
    "DescribeScheduledAuditResponseTypeDef",
    {
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "targetCheckNames": List[str],
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityProfileRequestRequestTypeDef = TypedDict(
    "DescribeSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)

DescribeStreamRequestRequestTypeDef = TypedDict(
    "DescribeStreamRequestRequestTypeDef",
    {
        "streamId": str,
    },
)

DescribeThingGroupRequestRequestTypeDef = TypedDict(
    "DescribeThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)

DescribeThingRegistrationTaskRequestRequestTypeDef = TypedDict(
    "DescribeThingRegistrationTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeThingRegistrationTaskResponseTypeDef = TypedDict(
    "DescribeThingRegistrationTaskResponseTypeDef",
    {
        "taskId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
        "status": StatusType,
        "message": str,
        "successCount": int,
        "failureCount": int,
        "percentageProgress": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingRequestRequestTypeDef = TypedDict(
    "DescribeThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)

DescribeThingResponseTypeDef = TypedDict(
    "DescribeThingResponseTypeDef",
    {
        "defaultClientId": str,
        "thingName": str,
        "thingId": str,
        "thingArn": str,
        "thingTypeName": str,
        "attributes": Dict[str, str],
        "version": int,
        "billingGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingTypeRequestRequestTypeDef = TypedDict(
    "DescribeThingTypeRequestRequestTypeDef",
    {
        "thingTypeName": str,
    },
)

ThingTypeMetadataTypeDef = TypedDict(
    "ThingTypeMetadataTypeDef",
    {
        "deprecated": bool,
        "deprecationDate": datetime,
        "creationDate": datetime,
    },
    total=False,
)

ThingTypePropertiesOutputTypeDef = TypedDict(
    "ThingTypePropertiesOutputTypeDef",
    {
        "thingTypeDescription": str,
        "searchableAttributes": List[str],
    },
    total=False,
)

S3DestinationOutputTypeDef = TypedDict(
    "S3DestinationOutputTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "target": str,
    },
)

DetachPrincipalPolicyRequestRequestTypeDef = TypedDict(
    "DetachPrincipalPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "principal": str,
    },
)

DetachSecurityProfileRequestRequestTypeDef = TypedDict(
    "DetachSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
        "securityProfileTargetArn": str,
    },
)

DetachThingPrincipalRequestRequestTypeDef = TypedDict(
    "DetachThingPrincipalRequestRequestTypeDef",
    {
        "thingName": str,
        "principal": str,
    },
)

DetectMitigationActionExecutionTypeDef = TypedDict(
    "DetectMitigationActionExecutionTypeDef",
    {
        "taskId": str,
        "violationId": str,
        "actionName": str,
        "thingName": str,
        "executionStartDate": datetime,
        "executionEndDate": datetime,
        "status": DetectMitigationActionExecutionStatusType,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

DetectMitigationActionsTaskStatisticsTypeDef = TypedDict(
    "DetectMitigationActionsTaskStatisticsTypeDef",
    {
        "actionsExecuted": int,
        "actionsSkipped": int,
        "actionsFailed": int,
    },
    total=False,
)

DetectMitigationActionsTaskTargetOutputTypeDef = TypedDict(
    "DetectMitigationActionsTaskTargetOutputTypeDef",
    {
        "violationIds": List[str],
        "securityProfileName": str,
        "behaviorName": str,
    },
    total=False,
)

ViolationEventOccurrenceRangeOutputTypeDef = TypedDict(
    "ViolationEventOccurrenceRangeOutputTypeDef",
    {
        "startTime": datetime,
        "endTime": datetime,
    },
)

DetectMitigationActionsTaskTargetTypeDef = TypedDict(
    "DetectMitigationActionsTaskTargetTypeDef",
    {
        "violationIds": Sequence[str],
        "securityProfileName": str,
        "behaviorName": str,
    },
    total=False,
)

DisableTopicRuleRequestRequestTypeDef = TypedDict(
    "DisableTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
    },
)

DomainConfigurationSummaryTypeDef = TypedDict(
    "DomainConfigurationSummaryTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "serviceType": ServiceTypeType,
    },
    total=False,
)

PutItemInputOutputTypeDef = TypedDict(
    "PutItemInputOutputTypeDef",
    {
        "tableName": str,
    },
)

PutItemInputTypeDef = TypedDict(
    "PutItemInputTypeDef",
    {
        "tableName": str,
    },
)

EffectivePolicyTypeDef = TypedDict(
    "EffectivePolicyTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
    },
    total=False,
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableIoTLoggingParamsOutputTypeDef = TypedDict(
    "EnableIoTLoggingParamsOutputTypeDef",
    {
        "roleArnForLogging": str,
        "logLevel": LogLevelType,
    },
)

EnableIoTLoggingParamsTypeDef = TypedDict(
    "EnableIoTLoggingParamsTypeDef",
    {
        "roleArnForLogging": str,
        "logLevel": LogLevelType,
    },
)

EnableTopicRuleRequestRequestTypeDef = TypedDict(
    "EnableTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

RateIncreaseCriteriaOutputTypeDef = TypedDict(
    "RateIncreaseCriteriaOutputTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

RateIncreaseCriteriaTypeDef = TypedDict(
    "RateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

FieldOutputTypeDef = TypedDict(
    "FieldOutputTypeDef",
    {
        "name": str,
        "type": FieldTypeType,
    },
    total=False,
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "name": str,
        "type": FieldTypeType,
    },
    total=False,
)

S3LocationOutputTypeDef = TypedDict(
    "S3LocationOutputTypeDef",
    {
        "bucket": str,
        "key": str,
        "version": str,
    },
    total=False,
)

StreamOutputTypeDef = TypedDict(
    "StreamOutputTypeDef",
    {
        "streamId": str,
        "fileId": int,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "version": str,
    },
    total=False,
)

StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "streamId": str,
        "fileId": int,
    },
    total=False,
)

FleetMetricNameAndArnTypeDef = TypedDict(
    "FleetMetricNameAndArnTypeDef",
    {
        "metricName": str,
        "metricArn": str,
    },
    total=False,
)

GetBehaviorModelTrainingSummariesRequestGetBehaviorModelTrainingSummariesPaginateTypeDef = (
    TypedDict(
        "GetBehaviorModelTrainingSummariesRequestGetBehaviorModelTrainingSummariesPaginateTypeDef",
        {
            "securityProfileName": str,
            "PaginationConfig": "PaginatorConfigTypeDef",
        },
        total=False,
    )
)

GetBehaviorModelTrainingSummariesRequestRequestTypeDef = TypedDict(
    "GetBehaviorModelTrainingSummariesRequestRequestTypeDef",
    {
        "securityProfileName": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredGetCardinalityRequestRequestTypeDef = TypedDict(
    "_RequiredGetCardinalityRequestRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetCardinalityRequestRequestTypeDef = TypedDict(
    "_OptionalGetCardinalityRequestRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
    },
    total=False,
)


class GetCardinalityRequestRequestTypeDef(
    _RequiredGetCardinalityRequestRequestTypeDef, _OptionalGetCardinalityRequestRequestTypeDef
):
    pass


GetCardinalityResponseTypeDef = TypedDict(
    "GetCardinalityResponseTypeDef",
    {
        "cardinality": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEffectivePoliciesRequestRequestTypeDef = TypedDict(
    "GetEffectivePoliciesRequestRequestTypeDef",
    {
        "principal": str,
        "cognitoIdentityPoolId": str,
        "thingName": str,
    },
    total=False,
)

GetJobDocumentRequestRequestTypeDef = TypedDict(
    "GetJobDocumentRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

GetJobDocumentResponseTypeDef = TypedDict(
    "GetJobDocumentResponseTypeDef",
    {
        "document": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggingOptionsResponseTypeDef = TypedDict(
    "GetLoggingOptionsResponseTypeDef",
    {
        "roleArn": str,
        "logLevel": LogLevelType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOTAUpdateRequestRequestTypeDef = TypedDict(
    "GetOTAUpdateRequestRequestTypeDef",
    {
        "otaUpdateId": str,
    },
)

VersionUpdateByJobsConfigOutputTypeDef = TypedDict(
    "VersionUpdateByJobsConfigOutputTypeDef",
    {
        "enabled": bool,
        "roleArn": str,
    },
    total=False,
)

GetPackageRequestRequestTypeDef = TypedDict(
    "GetPackageRequestRequestTypeDef",
    {
        "packageName": str,
    },
)

GetPackageResponseTypeDef = TypedDict(
    "GetPackageResponseTypeDef",
    {
        "packageName": str,
        "packageArn": str,
        "description": str,
        "defaultVersionName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPackageVersionRequestRequestTypeDef = TypedDict(
    "GetPackageVersionRequestRequestTypeDef",
    {
        "packageName": str,
        "versionName": str,
    },
)

GetPackageVersionResponseTypeDef = TypedDict(
    "GetPackageVersionResponseTypeDef",
    {
        "packageVersionArn": str,
        "packageName": str,
        "versionName": str,
        "description": str,
        "attributes": Dict[str, str],
        "status": PackageVersionStatusType,
        "errorReason": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPercentilesRequestRequestTypeDef = TypedDict(
    "_RequiredGetPercentilesRequestRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetPercentilesRequestRequestTypeDef = TypedDict(
    "_OptionalGetPercentilesRequestRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
        "percents": Sequence[float],
    },
    total=False,
)


class GetPercentilesRequestRequestTypeDef(
    _RequiredGetPercentilesRequestRequestTypeDef, _OptionalGetPercentilesRequestRequestTypeDef
):
    pass


PercentPairTypeDef = TypedDict(
    "PercentPairTypeDef",
    {
        "percent": float,
        "value": float,
    },
    total=False,
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "policyName": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "defaultVersionId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyVersionRequestRequestTypeDef = TypedDict(
    "GetPolicyVersionRequestRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

GetPolicyVersionResponseTypeDef = TypedDict(
    "GetPolicyVersionResponseTypeDef",
    {
        "policyArn": str,
        "policyName": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistrationCodeResponseTypeDef = TypedDict(
    "GetRegistrationCodeResponseTypeDef",
    {
        "registrationCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredGetStatisticsRequestRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalGetStatisticsRequestRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
    },
    total=False,
)


class GetStatisticsRequestRequestTypeDef(
    _RequiredGetStatisticsRequestRequestTypeDef, _OptionalGetStatisticsRequestRequestTypeDef
):
    pass


StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "count": int,
        "average": float,
        "sum": float,
        "minimum": float,
        "maximum": float,
        "sumOfSquares": float,
        "variance": float,
        "stdDeviation": float,
    },
    total=False,
)

GetTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "GetTopicRuleDestinationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetTopicRuleRequestRequestTypeDef = TypedDict(
    "GetTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
    },
)

GetV2LoggingOptionsResponseTypeDef = TypedDict(
    "GetV2LoggingOptionsResponseTypeDef",
    {
        "roleArn": str,
        "defaultLogLevel": LogLevelType,
        "disableAllLogs": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupNameAndArnTypeDef = TypedDict(
    "GroupNameAndArnTypeDef",
    {
        "groupName": str,
        "groupArn": str,
    },
    total=False,
)

HttpActionHeaderOutputTypeDef = TypedDict(
    "HttpActionHeaderOutputTypeDef",
    {
        "key": str,
        "value": str,
    },
)

HttpActionHeaderTypeDef = TypedDict(
    "HttpActionHeaderTypeDef",
    {
        "key": str,
        "value": str,
    },
)

SigV4AuthorizationOutputTypeDef = TypedDict(
    "SigV4AuthorizationOutputTypeDef",
    {
        "signingRegion": str,
        "serviceName": str,
        "roleArn": str,
    },
)

SigV4AuthorizationTypeDef = TypedDict(
    "SigV4AuthorizationTypeDef",
    {
        "signingRegion": str,
        "serviceName": str,
        "roleArn": str,
    },
)

HttpContextTypeDef = TypedDict(
    "HttpContextTypeDef",
    {
        "headers": Mapping[str, str],
        "queryString": str,
    },
    total=False,
)

HttpUrlDestinationConfigurationTypeDef = TypedDict(
    "HttpUrlDestinationConfigurationTypeDef",
    {
        "confirmationUrl": str,
    },
)

HttpUrlDestinationPropertiesTypeDef = TypedDict(
    "HttpUrlDestinationPropertiesTypeDef",
    {
        "confirmationUrl": str,
    },
    total=False,
)

HttpUrlDestinationSummaryTypeDef = TypedDict(
    "HttpUrlDestinationSummaryTypeDef",
    {
        "confirmationUrl": str,
    },
    total=False,
)

IndexingFilterOutputTypeDef = TypedDict(
    "IndexingFilterOutputTypeDef",
    {
        "namedShadowNames": List[str],
    },
    total=False,
)

IndexingFilterTypeDef = TypedDict(
    "IndexingFilterTypeDef",
    {
        "namedShadowNames": Sequence[str],
    },
    total=False,
)

IssuerCertificateIdentifierOutputTypeDef = TypedDict(
    "IssuerCertificateIdentifierOutputTypeDef",
    {
        "issuerCertificateSubject": str,
        "issuerId": str,
        "issuerCertificateSerialNumber": str,
    },
    total=False,
)

IssuerCertificateIdentifierTypeDef = TypedDict(
    "IssuerCertificateIdentifierTypeDef",
    {
        "issuerCertificateSubject": str,
        "issuerId": str,
        "issuerCertificateSerialNumber": str,
    },
    total=False,
)

JobExecutionStatusDetailsTypeDef = TypedDict(
    "JobExecutionStatusDetailsTypeDef",
    {
        "detailsMap": Dict[str, str],
    },
    total=False,
)

JobExecutionSummaryTypeDef = TypedDict(
    "JobExecutionSummaryTypeDef",
    {
        "status": JobExecutionStatusType,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
        "retryAttempt": int,
    },
    total=False,
)

RetryCriteriaOutputTypeDef = TypedDict(
    "RetryCriteriaOutputTypeDef",
    {
        "failureType": RetryableFailureTypeType,
        "numberOfRetries": int,
    },
)

RetryCriteriaTypeDef = TypedDict(
    "RetryCriteriaTypeDef",
    {
        "failureType": RetryableFailureTypeType,
        "numberOfRetries": int,
    },
)

JobProcessDetailsTypeDef = TypedDict(
    "JobProcessDetailsTypeDef",
    {
        "processingTargets": List[str],
        "numberOfCanceledThings": int,
        "numberOfSucceededThings": int,
        "numberOfFailedThings": int,
        "numberOfRejectedThings": int,
        "numberOfQueuedThings": int,
        "numberOfInProgressThings": int,
        "numberOfRemovedThings": int,
        "numberOfTimedOutThings": int,
    },
    total=False,
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": TargetSelectionType,
        "status": JobStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
        "isConcurrent": bool,
    },
    total=False,
)

JobTemplateSummaryTypeDef = TypedDict(
    "JobTemplateSummaryTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "description": str,
        "createdAt": datetime,
    },
    total=False,
)

ScheduledJobRolloutTypeDef = TypedDict(
    "ScheduledJobRolloutTypeDef",
    {
        "startTime": str,
    },
    total=False,
)

ListActiveViolationsRequestListActiveViolationsPaginateTypeDef = TypedDict(
    "ListActiveViolationsRequestListActiveViolationsPaginateTypeDef",
    {
        "thingName": str,
        "securityProfileName": str,
        "behaviorCriteriaType": BehaviorCriteriaTypeType,
        "listSuppressedAlerts": bool,
        "verificationState": VerificationStateType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListActiveViolationsRequestRequestTypeDef = TypedDict(
    "ListActiveViolationsRequestRequestTypeDef",
    {
        "thingName": str,
        "securityProfileName": str,
        "behaviorCriteriaType": BehaviorCriteriaTypeType,
        "listSuppressedAlerts": bool,
        "verificationState": VerificationStateType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef = TypedDict(
    "_RequiredListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef",
    {
        "target": str,
    },
)
_OptionalListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef = TypedDict(
    "_OptionalListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef",
    {
        "recursive": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef(
    _RequiredListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef,
    _OptionalListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef,
):
    pass


_RequiredListAttachedPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttachedPoliciesRequestRequestTypeDef",
    {
        "target": str,
    },
)
_OptionalListAttachedPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttachedPoliciesRequestRequestTypeDef",
    {
        "recursive": bool,
        "marker": str,
        "pageSize": int,
    },
    total=False,
)


class ListAttachedPoliciesRequestRequestTypeDef(
    _RequiredListAttachedPoliciesRequestRequestTypeDef,
    _OptionalListAttachedPoliciesRequestRequestTypeDef,
):
    pass


_RequiredListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef = TypedDict(
    "_RequiredListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef",
    {
        "taskId": str,
        "findingId": str,
    },
)
_OptionalListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef = TypedDict(
    "_OptionalListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef",
    {
        "actionStatus": AuditMitigationActionsExecutionStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef(
    _RequiredListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef,
    _OptionalListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef,
):
    pass


_RequiredListAuditMitigationActionsExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAuditMitigationActionsExecutionsRequestRequestTypeDef",
    {
        "taskId": str,
        "findingId": str,
    },
)
_OptionalListAuditMitigationActionsExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAuditMitigationActionsExecutionsRequestRequestTypeDef",
    {
        "actionStatus": AuditMitigationActionsExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAuditMitigationActionsExecutionsRequestRequestTypeDef(
    _RequiredListAuditMitigationActionsExecutionsRequestRequestTypeDef,
    _OptionalListAuditMitigationActionsExecutionsRequestRequestTypeDef,
):
    pass


_RequiredListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef = TypedDict(
    "_RequiredListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef = TypedDict(
    "_OptionalListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef",
    {
        "auditTaskId": str,
        "findingId": str,
        "taskStatus": AuditMitigationActionsTaskStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef(
    _RequiredListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef,
    _OptionalListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef,
):
    pass


_RequiredListAuditMitigationActionsTasksRequestRequestTypeDef = TypedDict(
    "_RequiredListAuditMitigationActionsTasksRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListAuditMitigationActionsTasksRequestRequestTypeDef = TypedDict(
    "_OptionalListAuditMitigationActionsTasksRequestRequestTypeDef",
    {
        "auditTaskId": str,
        "findingId": str,
        "taskStatus": AuditMitigationActionsTaskStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAuditMitigationActionsTasksRequestRequestTypeDef(
    _RequiredListAuditMitigationActionsTasksRequestRequestTypeDef,
    _OptionalListAuditMitigationActionsTasksRequestRequestTypeDef,
):
    pass


_RequiredListAuditTasksRequestListAuditTasksPaginateTypeDef = TypedDict(
    "_RequiredListAuditTasksRequestListAuditTasksPaginateTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListAuditTasksRequestListAuditTasksPaginateTypeDef = TypedDict(
    "_OptionalListAuditTasksRequestListAuditTasksPaginateTypeDef",
    {
        "taskType": AuditTaskTypeType,
        "taskStatus": AuditTaskStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListAuditTasksRequestListAuditTasksPaginateTypeDef(
    _RequiredListAuditTasksRequestListAuditTasksPaginateTypeDef,
    _OptionalListAuditTasksRequestListAuditTasksPaginateTypeDef,
):
    pass


_RequiredListAuditTasksRequestRequestTypeDef = TypedDict(
    "_RequiredListAuditTasksRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListAuditTasksRequestRequestTypeDef = TypedDict(
    "_OptionalListAuditTasksRequestRequestTypeDef",
    {
        "taskType": AuditTaskTypeType,
        "taskStatus": AuditTaskStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAuditTasksRequestRequestTypeDef(
    _RequiredListAuditTasksRequestRequestTypeDef, _OptionalListAuditTasksRequestRequestTypeDef
):
    pass


ListAuthorizersRequestListAuthorizersPaginateTypeDef = TypedDict(
    "ListAuthorizersRequestListAuthorizersPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "status": AuthorizerStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListAuthorizersRequestRequestTypeDef = TypedDict(
    "ListAuthorizersRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
        "status": AuthorizerStatusType,
    },
    total=False,
)

ListBillingGroupsRequestListBillingGroupsPaginateTypeDef = TypedDict(
    "ListBillingGroupsRequestListBillingGroupsPaginateTypeDef",
    {
        "namePrefixFilter": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListBillingGroupsRequestRequestTypeDef = TypedDict(
    "ListBillingGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "namePrefixFilter": str,
    },
    total=False,
)

ListCACertificatesRequestListCACertificatesPaginateTypeDef = TypedDict(
    "ListCACertificatesRequestListCACertificatesPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "templateName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListCACertificatesRequestRequestTypeDef = TypedDict(
    "ListCACertificatesRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
        "templateName": str,
    },
    total=False,
)

_RequiredListCertificatesByCARequestListCertificatesByCAPaginateTypeDef = TypedDict(
    "_RequiredListCertificatesByCARequestListCertificatesByCAPaginateTypeDef",
    {
        "caCertificateId": str,
    },
)
_OptionalListCertificatesByCARequestListCertificatesByCAPaginateTypeDef = TypedDict(
    "_OptionalListCertificatesByCARequestListCertificatesByCAPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListCertificatesByCARequestListCertificatesByCAPaginateTypeDef(
    _RequiredListCertificatesByCARequestListCertificatesByCAPaginateTypeDef,
    _OptionalListCertificatesByCARequestListCertificatesByCAPaginateTypeDef,
):
    pass


_RequiredListCertificatesByCARequestRequestTypeDef = TypedDict(
    "_RequiredListCertificatesByCARequestRequestTypeDef",
    {
        "caCertificateId": str,
    },
)
_OptionalListCertificatesByCARequestRequestTypeDef = TypedDict(
    "_OptionalListCertificatesByCARequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)


class ListCertificatesByCARequestRequestTypeDef(
    _RequiredListCertificatesByCARequestRequestTypeDef,
    _OptionalListCertificatesByCARequestRequestTypeDef,
):
    pass


ListCertificatesRequestListCertificatesPaginateTypeDef = TypedDict(
    "ListCertificatesRequestListCertificatesPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListCertificatesRequestRequestTypeDef = TypedDict(
    "ListCertificatesRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListCustomMetricsRequestListCustomMetricsPaginateTypeDef = TypedDict(
    "ListCustomMetricsRequestListCustomMetricsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListCustomMetricsRequestRequestTypeDef = TypedDict(
    "ListCustomMetricsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListCustomMetricsResponseTypeDef = TypedDict(
    "ListCustomMetricsResponseTypeDef",
    {
        "metricNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectMitigationActionsExecutionsRequestListDetectMitigationActionsExecutionsPaginateTypeDef = TypedDict(
    "ListDetectMitigationActionsExecutionsRequestListDetectMitigationActionsExecutionsPaginateTypeDef",
    {
        "taskId": str,
        "violationId": str,
        "thingName": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDetectMitigationActionsExecutionsRequestRequestTypeDef = TypedDict(
    "ListDetectMitigationActionsExecutionsRequestRequestTypeDef",
    {
        "taskId": str,
        "violationId": str,
        "thingName": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef = TypedDict(
    "_RequiredListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef = TypedDict(
    "_OptionalListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef(
    _RequiredListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef,
    _OptionalListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef,
):
    pass


_RequiredListDetectMitigationActionsTasksRequestRequestTypeDef = TypedDict(
    "_RequiredListDetectMitigationActionsTasksRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListDetectMitigationActionsTasksRequestRequestTypeDef = TypedDict(
    "_OptionalListDetectMitigationActionsTasksRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListDetectMitigationActionsTasksRequestRequestTypeDef(
    _RequiredListDetectMitigationActionsTasksRequestRequestTypeDef,
    _OptionalListDetectMitigationActionsTasksRequestRequestTypeDef,
):
    pass


ListDimensionsRequestListDimensionsPaginateTypeDef = TypedDict(
    "ListDimensionsRequestListDimensionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDimensionsRequestRequestTypeDef = TypedDict(
    "ListDimensionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDimensionsResponseTypeDef = TypedDict(
    "ListDimensionsResponseTypeDef",
    {
        "dimensionNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainConfigurationsRequestListDomainConfigurationsPaginateTypeDef = TypedDict(
    "ListDomainConfigurationsRequestListDomainConfigurationsPaginateTypeDef",
    {
        "serviceType": ServiceTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDomainConfigurationsRequestRequestTypeDef = TypedDict(
    "ListDomainConfigurationsRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "serviceType": ServiceTypeType,
    },
    total=False,
)

ListFleetMetricsRequestListFleetMetricsPaginateTypeDef = TypedDict(
    "ListFleetMetricsRequestListFleetMetricsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListFleetMetricsRequestRequestTypeDef = TypedDict(
    "ListFleetMetricsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListIndicesRequestListIndicesPaginateTypeDef = TypedDict(
    "ListIndicesRequestListIndicesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListIndicesRequestRequestTypeDef = TypedDict(
    "ListIndicesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "indexNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef = TypedDict(
    "_RequiredListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef",
    {
        "jobId": str,
    },
)
_OptionalListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef = TypedDict(
    "_OptionalListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef",
    {
        "status": JobExecutionStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef(
    _RequiredListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef,
    _OptionalListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef,
):
    pass


_RequiredListJobExecutionsForJobRequestRequestTypeDef = TypedDict(
    "_RequiredListJobExecutionsForJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalListJobExecutionsForJobRequestRequestTypeDef = TypedDict(
    "_OptionalListJobExecutionsForJobRequestRequestTypeDef",
    {
        "status": JobExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListJobExecutionsForJobRequestRequestTypeDef(
    _RequiredListJobExecutionsForJobRequestRequestTypeDef,
    _OptionalListJobExecutionsForJobRequestRequestTypeDef,
):
    pass


_RequiredListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef = TypedDict(
    "_RequiredListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef = TypedDict(
    "_OptionalListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef",
    {
        "status": JobExecutionStatusType,
        "namespaceId": str,
        "jobId": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef(
    _RequiredListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef,
    _OptionalListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef,
):
    pass


_RequiredListJobExecutionsForThingRequestRequestTypeDef = TypedDict(
    "_RequiredListJobExecutionsForThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListJobExecutionsForThingRequestRequestTypeDef = TypedDict(
    "_OptionalListJobExecutionsForThingRequestRequestTypeDef",
    {
        "status": JobExecutionStatusType,
        "namespaceId": str,
        "maxResults": int,
        "nextToken": str,
        "jobId": str,
    },
    total=False,
)


class ListJobExecutionsForThingRequestRequestTypeDef(
    _RequiredListJobExecutionsForThingRequestRequestTypeDef,
    _OptionalListJobExecutionsForThingRequestRequestTypeDef,
):
    pass


ListJobTemplatesRequestListJobTemplatesPaginateTypeDef = TypedDict(
    "ListJobTemplatesRequestListJobTemplatesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListJobTemplatesRequestRequestTypeDef = TypedDict(
    "ListJobTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "status": JobStatusType,
        "targetSelection": TargetSelectionType,
        "thingGroupName": str,
        "thingGroupId": str,
        "namespaceId": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "status": JobStatusType,
        "targetSelection": TargetSelectionType,
        "maxResults": int,
        "nextToken": str,
        "thingGroupName": str,
        "thingGroupId": str,
        "namespaceId": str,
    },
    total=False,
)

ListManagedJobTemplatesRequestListManagedJobTemplatesPaginateTypeDef = TypedDict(
    "ListManagedJobTemplatesRequestListManagedJobTemplatesPaginateTypeDef",
    {
        "templateName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListManagedJobTemplatesRequestRequestTypeDef = TypedDict(
    "ListManagedJobTemplatesRequestRequestTypeDef",
    {
        "templateName": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ManagedJobTemplateSummaryTypeDef = TypedDict(
    "ManagedJobTemplateSummaryTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "environments": List[str],
        "templateVersion": str,
    },
    total=False,
)

_RequiredListMetricValuesRequestListMetricValuesPaginateTypeDef = TypedDict(
    "_RequiredListMetricValuesRequestListMetricValuesPaginateTypeDef",
    {
        "thingName": str,
        "metricName": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListMetricValuesRequestListMetricValuesPaginateTypeDef = TypedDict(
    "_OptionalListMetricValuesRequestListMetricValuesPaginateTypeDef",
    {
        "dimensionName": str,
        "dimensionValueOperator": DimensionValueOperatorType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListMetricValuesRequestListMetricValuesPaginateTypeDef(
    _RequiredListMetricValuesRequestListMetricValuesPaginateTypeDef,
    _OptionalListMetricValuesRequestListMetricValuesPaginateTypeDef,
):
    pass


_RequiredListMetricValuesRequestRequestTypeDef = TypedDict(
    "_RequiredListMetricValuesRequestRequestTypeDef",
    {
        "thingName": str,
        "metricName": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListMetricValuesRequestRequestTypeDef = TypedDict(
    "_OptionalListMetricValuesRequestRequestTypeDef",
    {
        "dimensionName": str,
        "dimensionValueOperator": DimensionValueOperatorType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListMetricValuesRequestRequestTypeDef(
    _RequiredListMetricValuesRequestRequestTypeDef, _OptionalListMetricValuesRequestRequestTypeDef
):
    pass


ListMitigationActionsRequestListMitigationActionsPaginateTypeDef = TypedDict(
    "ListMitigationActionsRequestListMitigationActionsPaginateTypeDef",
    {
        "actionType": MitigationActionTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListMitigationActionsRequestRequestTypeDef = TypedDict(
    "ListMitigationActionsRequestRequestTypeDef",
    {
        "actionType": MitigationActionTypeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

MitigationActionIdentifierTypeDef = TypedDict(
    "MitigationActionIdentifierTypeDef",
    {
        "actionName": str,
        "actionArn": str,
        "creationDate": datetime,
    },
    total=False,
)

ListOTAUpdatesRequestListOTAUpdatesPaginateTypeDef = TypedDict(
    "ListOTAUpdatesRequestListOTAUpdatesPaginateTypeDef",
    {
        "otaUpdateStatus": OTAUpdateStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListOTAUpdatesRequestRequestTypeDef = TypedDict(
    "ListOTAUpdatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "otaUpdateStatus": OTAUpdateStatusType,
    },
    total=False,
)

OTAUpdateSummaryTypeDef = TypedDict(
    "OTAUpdateSummaryTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
    },
    total=False,
)

ListOutgoingCertificatesRequestListOutgoingCertificatesPaginateTypeDef = TypedDict(
    "ListOutgoingCertificatesRequestListOutgoingCertificatesPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListOutgoingCertificatesRequestRequestTypeDef = TypedDict(
    "ListOutgoingCertificatesRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

OutgoingCertificateTypeDef = TypedDict(
    "OutgoingCertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
    },
    total=False,
)

_RequiredListPackageVersionsRequestListPackageVersionsPaginateTypeDef = TypedDict(
    "_RequiredListPackageVersionsRequestListPackageVersionsPaginateTypeDef",
    {
        "packageName": str,
    },
)
_OptionalListPackageVersionsRequestListPackageVersionsPaginateTypeDef = TypedDict(
    "_OptionalListPackageVersionsRequestListPackageVersionsPaginateTypeDef",
    {
        "status": PackageVersionStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListPackageVersionsRequestListPackageVersionsPaginateTypeDef(
    _RequiredListPackageVersionsRequestListPackageVersionsPaginateTypeDef,
    _OptionalListPackageVersionsRequestListPackageVersionsPaginateTypeDef,
):
    pass


_RequiredListPackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionsRequestRequestTypeDef",
    {
        "packageName": str,
    },
)
_OptionalListPackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionsRequestRequestTypeDef",
    {
        "status": PackageVersionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListPackageVersionsRequestRequestTypeDef(
    _RequiredListPackageVersionsRequestRequestTypeDef,
    _OptionalListPackageVersionsRequestRequestTypeDef,
):
    pass


PackageVersionSummaryTypeDef = TypedDict(
    "PackageVersionSummaryTypeDef",
    {
        "packageName": str,
        "versionName": str,
        "status": PackageVersionStatusType,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

ListPackagesRequestListPackagesPaginateTypeDef = TypedDict(
    "ListPackagesRequestListPackagesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListPackagesRequestRequestTypeDef = TypedDict(
    "ListPackagesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {
        "packageName": str,
        "defaultVersionName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

ListPoliciesRequestListPoliciesPaginateTypeDef = TypedDict(
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)

_RequiredListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef = TypedDict(
    "_RequiredListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef",
    {
        "policyName": str,
    },
)
_OptionalListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef = TypedDict(
    "_OptionalListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef(
    _RequiredListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef,
    _OptionalListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef,
):
    pass


_RequiredListPolicyPrincipalsRequestRequestTypeDef = TypedDict(
    "_RequiredListPolicyPrincipalsRequestRequestTypeDef",
    {
        "policyName": str,
    },
)
_OptionalListPolicyPrincipalsRequestRequestTypeDef = TypedDict(
    "_OptionalListPolicyPrincipalsRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)


class ListPolicyPrincipalsRequestRequestTypeDef(
    _RequiredListPolicyPrincipalsRequestRequestTypeDef,
    _OptionalListPolicyPrincipalsRequestRequestTypeDef,
):
    pass


ListPolicyPrincipalsResponseTypeDef = TypedDict(
    "ListPolicyPrincipalsResponseTypeDef",
    {
        "principals": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyVersionsRequestRequestTypeDef = TypedDict(
    "ListPolicyVersionsRequestRequestTypeDef",
    {
        "policyName": str,
    },
)

PolicyVersionTypeDef = TypedDict(
    "PolicyVersionTypeDef",
    {
        "versionId": str,
        "isDefaultVersion": bool,
        "createDate": datetime,
    },
    total=False,
)

_RequiredListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef = TypedDict(
    "_RequiredListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef",
    {
        "principal": str,
    },
)
_OptionalListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef = TypedDict(
    "_OptionalListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef(
    _RequiredListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef,
    _OptionalListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef,
):
    pass


_RequiredListPrincipalPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListPrincipalPoliciesRequestRequestTypeDef",
    {
        "principal": str,
    },
)
_OptionalListPrincipalPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListPrincipalPoliciesRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)


class ListPrincipalPoliciesRequestRequestTypeDef(
    _RequiredListPrincipalPoliciesRequestRequestTypeDef,
    _OptionalListPrincipalPoliciesRequestRequestTypeDef,
):
    pass


_RequiredListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef = TypedDict(
    "_RequiredListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef",
    {
        "principal": str,
    },
)
_OptionalListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef = TypedDict(
    "_OptionalListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef(
    _RequiredListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef,
    _OptionalListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef,
):
    pass


_RequiredListPrincipalThingsRequestRequestTypeDef = TypedDict(
    "_RequiredListPrincipalThingsRequestRequestTypeDef",
    {
        "principal": str,
    },
)
_OptionalListPrincipalThingsRequestRequestTypeDef = TypedDict(
    "_OptionalListPrincipalThingsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListPrincipalThingsRequestRequestTypeDef(
    _RequiredListPrincipalThingsRequestRequestTypeDef,
    _OptionalListPrincipalThingsRequestRequestTypeDef,
):
    pass


ListPrincipalThingsResponseTypeDef = TypedDict(
    "ListPrincipalThingsResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef = TypedDict(
    "_RequiredListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef",
    {
        "templateName": str,
    },
)
_OptionalListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef = TypedDict(
    "_OptionalListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef(
    _RequiredListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef,
    _OptionalListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef,
):
    pass


_RequiredListProvisioningTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListProvisioningTemplateVersionsRequestRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalListProvisioningTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListProvisioningTemplateVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListProvisioningTemplateVersionsRequestRequestTypeDef(
    _RequiredListProvisioningTemplateVersionsRequestRequestTypeDef,
    _OptionalListProvisioningTemplateVersionsRequestRequestTypeDef,
):
    pass


ProvisioningTemplateVersionSummaryTypeDef = TypedDict(
    "ProvisioningTemplateVersionSummaryTypeDef",
    {
        "versionId": int,
        "creationDate": datetime,
        "isDefaultVersion": bool,
    },
    total=False,
)

ListProvisioningTemplatesRequestListProvisioningTemplatesPaginateTypeDef = TypedDict(
    "ListProvisioningTemplatesRequestListProvisioningTemplatesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListProvisioningTemplatesRequestRequestTypeDef = TypedDict(
    "ListProvisioningTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ProvisioningTemplateSummaryTypeDef = TypedDict(
    "ProvisioningTemplateSummaryTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "enabled": bool,
        "type": TemplateTypeType,
    },
    total=False,
)

_RequiredListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef = TypedDict(
    "_RequiredListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef",
    {
        "findingId": str,
    },
)
_OptionalListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef = TypedDict(
    "_OptionalListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef(
    _RequiredListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef,
    _OptionalListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef,
):
    pass


_RequiredListRelatedResourcesForAuditFindingRequestRequestTypeDef = TypedDict(
    "_RequiredListRelatedResourcesForAuditFindingRequestRequestTypeDef",
    {
        "findingId": str,
    },
)
_OptionalListRelatedResourcesForAuditFindingRequestRequestTypeDef = TypedDict(
    "_OptionalListRelatedResourcesForAuditFindingRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListRelatedResourcesForAuditFindingRequestRequestTypeDef(
    _RequiredListRelatedResourcesForAuditFindingRequestRequestTypeDef,
    _OptionalListRelatedResourcesForAuditFindingRequestRequestTypeDef,
):
    pass


ListRoleAliasesRequestListRoleAliasesPaginateTypeDef = TypedDict(
    "ListRoleAliasesRequestListRoleAliasesPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListRoleAliasesRequestRequestTypeDef = TypedDict(
    "ListRoleAliasesRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListRoleAliasesResponseTypeDef = TypedDict(
    "ListRoleAliasesResponseTypeDef",
    {
        "roleAliases": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScheduledAuditsRequestListScheduledAuditsPaginateTypeDef = TypedDict(
    "ListScheduledAuditsRequestListScheduledAuditsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListScheduledAuditsRequestRequestTypeDef = TypedDict(
    "ListScheduledAuditsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ScheduledAuditMetadataTypeDef = TypedDict(
    "ScheduledAuditMetadataTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
    },
    total=False,
)

_RequiredListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef = (
    TypedDict(
        "_RequiredListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef",
        {
            "securityProfileTargetArn": str,
        },
    )
)
_OptionalListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef = (
    TypedDict(
        "_OptionalListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef",
        {
            "recursive": bool,
            "PaginationConfig": "PaginatorConfigTypeDef",
        },
        total=False,
    )
)


class ListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef(
    _RequiredListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef,
    _OptionalListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef,
):
    pass


_RequiredListSecurityProfilesForTargetRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilesForTargetRequestRequestTypeDef",
    {
        "securityProfileTargetArn": str,
    },
)
_OptionalListSecurityProfilesForTargetRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilesForTargetRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "recursive": bool,
    },
    total=False,
)


class ListSecurityProfilesForTargetRequestRequestTypeDef(
    _RequiredListSecurityProfilesForTargetRequestRequestTypeDef,
    _OptionalListSecurityProfilesForTargetRequestRequestTypeDef,
):
    pass


ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef = TypedDict(
    "ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef",
    {
        "dimensionName": str,
        "metricName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "ListSecurityProfilesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "dimensionName": str,
        "metricName": str,
    },
    total=False,
)

SecurityProfileIdentifierTypeDef = TypedDict(
    "SecurityProfileIdentifierTypeDef",
    {
        "name": str,
        "arn": str,
    },
)

ListStreamsRequestListStreamsPaginateTypeDef = TypedDict(
    "ListStreamsRequestListStreamsPaginateTypeDef",
    {
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListStreamsRequestRequestTypeDef = TypedDict(
    "ListStreamsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "ascendingOrder": bool,
    },
    total=False,
)

StreamSummaryTypeDef = TypedDict(
    "StreamSummaryTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
    },
    total=False,
)

_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(
    _RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
    _OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
):
    pass


_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass


_RequiredTagOutputTypeDef = TypedDict(
    "_RequiredTagOutputTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagOutputTypeDef = TypedDict(
    "_OptionalTagOutputTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagOutputTypeDef(_RequiredTagOutputTypeDef, _OptionalTagOutputTypeDef):
    pass


_RequiredListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef = TypedDict(
    "_RequiredListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef",
    {
        "policyName": str,
    },
)
_OptionalListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef = TypedDict(
    "_OptionalListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef(
    _RequiredListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef,
    _OptionalListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef,
):
    pass


_RequiredListTargetsForPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredListTargetsForPolicyRequestRequestTypeDef",
    {
        "policyName": str,
    },
)
_OptionalListTargetsForPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalListTargetsForPolicyRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
    },
    total=False,
)


class ListTargetsForPolicyRequestRequestTypeDef(
    _RequiredListTargetsForPolicyRequestRequestTypeDef,
    _OptionalListTargetsForPolicyRequestRequestTypeDef,
):
    pass


ListTargetsForPolicyResponseTypeDef = TypedDict(
    "ListTargetsForPolicyResponseTypeDef",
    {
        "targets": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef = (
    TypedDict(
        "_RequiredListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef",
        {
            "securityProfileName": str,
        },
    )
)
_OptionalListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef = (
    TypedDict(
        "_OptionalListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef",
        {
            "PaginationConfig": "PaginatorConfigTypeDef",
        },
        total=False,
    )
)


class ListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef(
    _RequiredListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef,
    _OptionalListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef,
):
    pass


_RequiredListTargetsForSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredListTargetsForSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalListTargetsForSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalListTargetsForSecurityProfileRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListTargetsForSecurityProfileRequestRequestTypeDef(
    _RequiredListTargetsForSecurityProfileRequestRequestTypeDef,
    _OptionalListTargetsForSecurityProfileRequestRequestTypeDef,
):
    pass


SecurityProfileTargetTypeDef = TypedDict(
    "SecurityProfileTargetTypeDef",
    {
        "arn": str,
    },
)

_RequiredListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef = TypedDict(
    "_RequiredListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef = TypedDict(
    "_OptionalListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef(
    _RequiredListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef,
    _OptionalListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef,
):
    pass


_RequiredListThingGroupsForThingRequestRequestTypeDef = TypedDict(
    "_RequiredListThingGroupsForThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListThingGroupsForThingRequestRequestTypeDef = TypedDict(
    "_OptionalListThingGroupsForThingRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingGroupsForThingRequestRequestTypeDef(
    _RequiredListThingGroupsForThingRequestRequestTypeDef,
    _OptionalListThingGroupsForThingRequestRequestTypeDef,
):
    pass


ListThingGroupsRequestListThingGroupsPaginateTypeDef = TypedDict(
    "ListThingGroupsRequestListThingGroupsPaginateTypeDef",
    {
        "parentGroup": str,
        "namePrefixFilter": str,
        "recursive": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListThingGroupsRequestRequestTypeDef = TypedDict(
    "ListThingGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "parentGroup": str,
        "namePrefixFilter": str,
        "recursive": bool,
    },
    total=False,
)

_RequiredListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef = TypedDict(
    "_RequiredListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef = TypedDict(
    "_OptionalListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef(
    _RequiredListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef,
    _OptionalListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef,
):
    pass


_RequiredListThingPrincipalsRequestRequestTypeDef = TypedDict(
    "_RequiredListThingPrincipalsRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListThingPrincipalsRequestRequestTypeDef = TypedDict(
    "_OptionalListThingPrincipalsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingPrincipalsRequestRequestTypeDef(
    _RequiredListThingPrincipalsRequestRequestTypeDef,
    _OptionalListThingPrincipalsRequestRequestTypeDef,
):
    pass


ListThingPrincipalsResponseTypeDef = TypedDict(
    "ListThingPrincipalsResponseTypeDef",
    {
        "principals": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef = TypedDict(
    "_RequiredListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef",
    {
        "taskId": str,
        "reportType": ReportTypeType,
    },
)
_OptionalListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef = TypedDict(
    "_OptionalListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef(
    _RequiredListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef,
    _OptionalListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef,
):
    pass


_RequiredListThingRegistrationTaskReportsRequestRequestTypeDef = TypedDict(
    "_RequiredListThingRegistrationTaskReportsRequestRequestTypeDef",
    {
        "taskId": str,
        "reportType": ReportTypeType,
    },
)
_OptionalListThingRegistrationTaskReportsRequestRequestTypeDef = TypedDict(
    "_OptionalListThingRegistrationTaskReportsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingRegistrationTaskReportsRequestRequestTypeDef(
    _RequiredListThingRegistrationTaskReportsRequestRequestTypeDef,
    _OptionalListThingRegistrationTaskReportsRequestRequestTypeDef,
):
    pass


ListThingRegistrationTaskReportsResponseTypeDef = TypedDict(
    "ListThingRegistrationTaskReportsResponseTypeDef",
    {
        "resourceLinks": List[str],
        "reportType": ReportTypeType,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingRegistrationTasksRequestListThingRegistrationTasksPaginateTypeDef = TypedDict(
    "ListThingRegistrationTasksRequestListThingRegistrationTasksPaginateTypeDef",
    {
        "status": StatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListThingRegistrationTasksRequestRequestTypeDef = TypedDict(
    "ListThingRegistrationTasksRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "status": StatusType,
    },
    total=False,
)

ListThingRegistrationTasksResponseTypeDef = TypedDict(
    "ListThingRegistrationTasksResponseTypeDef",
    {
        "taskIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingTypesRequestListThingTypesPaginateTypeDef = TypedDict(
    "ListThingTypesRequestListThingTypesPaginateTypeDef",
    {
        "thingTypeName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListThingTypesRequestRequestTypeDef = TypedDict(
    "ListThingTypesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "thingTypeName": str,
    },
    total=False,
)

_RequiredListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef = TypedDict(
    "_RequiredListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef = TypedDict(
    "_OptionalListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef(
    _RequiredListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef,
    _OptionalListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef,
):
    pass


_RequiredListThingsInBillingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListThingsInBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalListThingsInBillingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListThingsInBillingGroupRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingsInBillingGroupRequestRequestTypeDef(
    _RequiredListThingsInBillingGroupRequestRequestTypeDef,
    _OptionalListThingsInBillingGroupRequestRequestTypeDef,
):
    pass


ListThingsInBillingGroupResponseTypeDef = TypedDict(
    "ListThingsInBillingGroupResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef = TypedDict(
    "_RequiredListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef = TypedDict(
    "_OptionalListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef",
    {
        "recursive": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef(
    _RequiredListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef,
    _OptionalListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef,
):
    pass


_RequiredListThingsInThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListThingsInThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalListThingsInThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListThingsInThingGroupRequestRequestTypeDef",
    {
        "recursive": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListThingsInThingGroupRequestRequestTypeDef(
    _RequiredListThingsInThingGroupRequestRequestTypeDef,
    _OptionalListThingsInThingGroupRequestRequestTypeDef,
):
    pass


ListThingsInThingGroupResponseTypeDef = TypedDict(
    "ListThingsInThingGroupResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingsRequestListThingsPaginateTypeDef = TypedDict(
    "ListThingsRequestListThingsPaginateTypeDef",
    {
        "attributeName": str,
        "attributeValue": str,
        "thingTypeName": str,
        "usePrefixAttributeValue": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListThingsRequestRequestTypeDef = TypedDict(
    "ListThingsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "attributeName": str,
        "attributeValue": str,
        "thingTypeName": str,
        "usePrefixAttributeValue": bool,
    },
    total=False,
)

ThingAttributeTypeDef = TypedDict(
    "ThingAttributeTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)

ListTopicRuleDestinationsRequestListTopicRuleDestinationsPaginateTypeDef = TypedDict(
    "ListTopicRuleDestinationsRequestListTopicRuleDestinationsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTopicRuleDestinationsRequestRequestTypeDef = TypedDict(
    "ListTopicRuleDestinationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTopicRulesRequestListTopicRulesPaginateTypeDef = TypedDict(
    "ListTopicRulesRequestListTopicRulesPaginateTypeDef",
    {
        "topic": str,
        "ruleDisabled": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTopicRulesRequestRequestTypeDef = TypedDict(
    "ListTopicRulesRequestRequestTypeDef",
    {
        "topic": str,
        "maxResults": int,
        "nextToken": str,
        "ruleDisabled": bool,
    },
    total=False,
)

TopicRuleListItemTypeDef = TypedDict(
    "TopicRuleListItemTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)

ListV2LoggingLevelsRequestListV2LoggingLevelsPaginateTypeDef = TypedDict(
    "ListV2LoggingLevelsRequestListV2LoggingLevelsPaginateTypeDef",
    {
        "targetType": LogTargetTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListV2LoggingLevelsRequestRequestTypeDef = TypedDict(
    "ListV2LoggingLevelsRequestRequestTypeDef",
    {
        "targetType": LogTargetTypeType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListViolationEventsRequestListViolationEventsPaginateTypeDef = TypedDict(
    "_RequiredListViolationEventsRequestListViolationEventsPaginateTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListViolationEventsRequestListViolationEventsPaginateTypeDef = TypedDict(
    "_OptionalListViolationEventsRequestListViolationEventsPaginateTypeDef",
    {
        "thingName": str,
        "securityProfileName": str,
        "behaviorCriteriaType": BehaviorCriteriaTypeType,
        "listSuppressedAlerts": bool,
        "verificationState": VerificationStateType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListViolationEventsRequestListViolationEventsPaginateTypeDef(
    _RequiredListViolationEventsRequestListViolationEventsPaginateTypeDef,
    _OptionalListViolationEventsRequestListViolationEventsPaginateTypeDef,
):
    pass


_RequiredListViolationEventsRequestRequestTypeDef = TypedDict(
    "_RequiredListViolationEventsRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListViolationEventsRequestRequestTypeDef = TypedDict(
    "_OptionalListViolationEventsRequestRequestTypeDef",
    {
        "thingName": str,
        "securityProfileName": str,
        "behaviorCriteriaType": BehaviorCriteriaTypeType,
        "listSuppressedAlerts": bool,
        "verificationState": VerificationStateType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListViolationEventsRequestRequestTypeDef(
    _RequiredListViolationEventsRequestRequestTypeDef,
    _OptionalListViolationEventsRequestRequestTypeDef,
):
    pass


_RequiredLocationTimestampOutputTypeDef = TypedDict(
    "_RequiredLocationTimestampOutputTypeDef",
    {
        "value": str,
    },
)
_OptionalLocationTimestampOutputTypeDef = TypedDict(
    "_OptionalLocationTimestampOutputTypeDef",
    {
        "unit": str,
    },
    total=False,
)


class LocationTimestampOutputTypeDef(
    _RequiredLocationTimestampOutputTypeDef, _OptionalLocationTimestampOutputTypeDef
):
    pass


_RequiredLocationTimestampTypeDef = TypedDict(
    "_RequiredLocationTimestampTypeDef",
    {
        "value": str,
    },
)
_OptionalLocationTimestampTypeDef = TypedDict(
    "_OptionalLocationTimestampTypeDef",
    {
        "unit": str,
    },
    total=False,
)


class LocationTimestampTypeDef(
    _RequiredLocationTimestampTypeDef, _OptionalLocationTimestampTypeDef
):
    pass


_RequiredLogTargetOutputTypeDef = TypedDict(
    "_RequiredLogTargetOutputTypeDef",
    {
        "targetType": LogTargetTypeType,
    },
)
_OptionalLogTargetOutputTypeDef = TypedDict(
    "_OptionalLogTargetOutputTypeDef",
    {
        "targetName": str,
    },
    total=False,
)


class LogTargetOutputTypeDef(_RequiredLogTargetOutputTypeDef, _OptionalLogTargetOutputTypeDef):
    pass


_RequiredLogTargetTypeDef = TypedDict(
    "_RequiredLogTargetTypeDef",
    {
        "targetType": LogTargetTypeType,
    },
)
_OptionalLogTargetTypeDef = TypedDict(
    "_OptionalLogTargetTypeDef",
    {
        "targetName": str,
    },
    total=False,
)


class LogTargetTypeDef(_RequiredLogTargetTypeDef, _OptionalLogTargetTypeDef):
    pass


_RequiredLoggingOptionsPayloadTypeDef = TypedDict(
    "_RequiredLoggingOptionsPayloadTypeDef",
    {
        "roleArn": str,
    },
)
_OptionalLoggingOptionsPayloadTypeDef = TypedDict(
    "_OptionalLoggingOptionsPayloadTypeDef",
    {
        "logLevel": LogLevelType,
    },
    total=False,
)


class LoggingOptionsPayloadTypeDef(
    _RequiredLoggingOptionsPayloadTypeDef, _OptionalLoggingOptionsPayloadTypeDef
):
    pass


PublishFindingToSnsParamsOutputTypeDef = TypedDict(
    "PublishFindingToSnsParamsOutputTypeDef",
    {
        "topicArn": str,
    },
)

ReplaceDefaultPolicyVersionParamsOutputTypeDef = TypedDict(
    "ReplaceDefaultPolicyVersionParamsOutputTypeDef",
    {
        "templateName": Literal["BLANK_POLICY"],
    },
)

UpdateCACertificateParamsOutputTypeDef = TypedDict(
    "UpdateCACertificateParamsOutputTypeDef",
    {
        "action": Literal["DEACTIVATE"],
    },
)

UpdateDeviceCertificateParamsOutputTypeDef = TypedDict(
    "UpdateDeviceCertificateParamsOutputTypeDef",
    {
        "action": Literal["DEACTIVATE"],
    },
)

PublishFindingToSnsParamsTypeDef = TypedDict(
    "PublishFindingToSnsParamsTypeDef",
    {
        "topicArn": str,
    },
)

ReplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "ReplaceDefaultPolicyVersionParamsTypeDef",
    {
        "templateName": Literal["BLANK_POLICY"],
    },
)

UpdateCACertificateParamsTypeDef = TypedDict(
    "UpdateCACertificateParamsTypeDef",
    {
        "action": Literal["DEACTIVATE"],
    },
)

UpdateDeviceCertificateParamsTypeDef = TypedDict(
    "UpdateDeviceCertificateParamsTypeDef",
    {
        "action": Literal["DEACTIVATE"],
    },
)

MqttContextTypeDef = TypedDict(
    "MqttContextTypeDef",
    {
        "username": str,
        "password": Union[str, bytes, IO[Any], StreamingBody],
        "clientId": str,
    },
    total=False,
)

UserPropertyOutputTypeDef = TypedDict(
    "UserPropertyOutputTypeDef",
    {
        "key": str,
        "value": str,
    },
)

UserPropertyTypeDef = TypedDict(
    "UserPropertyTypeDef",
    {
        "key": str,
        "value": str,
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

PolicyVersionIdentifierOutputTypeDef = TypedDict(
    "PolicyVersionIdentifierOutputTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
    total=False,
)

PolicyVersionIdentifierTypeDef = TypedDict(
    "PolicyVersionIdentifierTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
    total=False,
)

_RequiredPutVerificationStateOnViolationRequestRequestTypeDef = TypedDict(
    "_RequiredPutVerificationStateOnViolationRequestRequestTypeDef",
    {
        "violationId": str,
        "verificationState": VerificationStateType,
    },
)
_OptionalPutVerificationStateOnViolationRequestRequestTypeDef = TypedDict(
    "_OptionalPutVerificationStateOnViolationRequestRequestTypeDef",
    {
        "verificationStateDescription": str,
    },
    total=False,
)


class PutVerificationStateOnViolationRequestRequestTypeDef(
    _RequiredPutVerificationStateOnViolationRequestRequestTypeDef,
    _OptionalPutVerificationStateOnViolationRequestRequestTypeDef,
):
    pass


RegistrationConfigTypeDef = TypedDict(
    "RegistrationConfigTypeDef",
    {
        "templateBody": str,
        "roleArn": str,
        "templateName": str,
    },
    total=False,
)

RegisterCACertificateResponseTypeDef = TypedDict(
    "RegisterCACertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterCertificateRequestRequestTypeDef",
    {
        "certificatePem": str,
    },
)
_OptionalRegisterCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterCertificateRequestRequestTypeDef",
    {
        "caCertificatePem": str,
        "setAsActive": bool,
        "status": CertificateStatusType,
    },
    total=False,
)


class RegisterCertificateRequestRequestTypeDef(
    _RequiredRegisterCertificateRequestRequestTypeDef,
    _OptionalRegisterCertificateRequestRequestTypeDef,
):
    pass


RegisterCertificateResponseTypeDef = TypedDict(
    "RegisterCertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterCertificateWithoutCARequestRequestTypeDef = TypedDict(
    "_RequiredRegisterCertificateWithoutCARequestRequestTypeDef",
    {
        "certificatePem": str,
    },
)
_OptionalRegisterCertificateWithoutCARequestRequestTypeDef = TypedDict(
    "_OptionalRegisterCertificateWithoutCARequestRequestTypeDef",
    {
        "status": CertificateStatusType,
    },
    total=False,
)


class RegisterCertificateWithoutCARequestRequestTypeDef(
    _RequiredRegisterCertificateWithoutCARequestRequestTypeDef,
    _OptionalRegisterCertificateWithoutCARequestRequestTypeDef,
):
    pass


RegisterCertificateWithoutCAResponseTypeDef = TypedDict(
    "RegisterCertificateWithoutCAResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterThingRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterThingRequestRequestTypeDef",
    {
        "templateBody": str,
    },
)
_OptionalRegisterThingRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterThingRequestRequestTypeDef",
    {
        "parameters": Mapping[str, str],
    },
    total=False,
)


class RegisterThingRequestRequestTypeDef(
    _RequiredRegisterThingRequestRequestTypeDef, _OptionalRegisterThingRequestRequestTypeDef
):
    pass


RegisterThingResponseTypeDef = TypedDict(
    "RegisterThingResponseTypeDef",
    {
        "certificatePem": str,
        "resourceArns": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectCertificateTransferRequestRequestTypeDef = TypedDict(
    "_RequiredRejectCertificateTransferRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalRejectCertificateTransferRequestRequestTypeDef = TypedDict(
    "_OptionalRejectCertificateTransferRequestRequestTypeDef",
    {
        "rejectReason": str,
    },
    total=False,
)


class RejectCertificateTransferRequestRequestTypeDef(
    _RequiredRejectCertificateTransferRequestRequestTypeDef,
    _OptionalRejectCertificateTransferRequestRequestTypeDef,
):
    pass


RemoveThingFromBillingGroupRequestRequestTypeDef = TypedDict(
    "RemoveThingFromBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "thingName": str,
        "thingArn": str,
    },
    total=False,
)

RemoveThingFromThingGroupRequestRequestTypeDef = TypedDict(
    "RemoveThingFromThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingName": str,
        "thingArn": str,
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

_RequiredSearchIndexRequestRequestTypeDef = TypedDict(
    "_RequiredSearchIndexRequestRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalSearchIndexRequestRequestTypeDef = TypedDict(
    "_OptionalSearchIndexRequestRequestTypeDef",
    {
        "indexName": str,
        "nextToken": str,
        "maxResults": int,
        "queryVersion": str,
    },
    total=False,
)


class SearchIndexRequestRequestTypeDef(
    _RequiredSearchIndexRequestRequestTypeDef, _OptionalSearchIndexRequestRequestTypeDef
):
    pass


ThingGroupDocumentTypeDef = TypedDict(
    "ThingGroupDocumentTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupDescription": str,
        "attributes": Dict[str, str],
        "parentGroupNames": List[str],
    },
    total=False,
)

SetDefaultAuthorizerRequestRequestTypeDef = TypedDict(
    "SetDefaultAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)

SetDefaultAuthorizerResponseTypeDef = TypedDict(
    "SetDefaultAuthorizerResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetDefaultPolicyVersionRequestRequestTypeDef = TypedDict(
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

SetV2LoggingOptionsRequestRequestTypeDef = TypedDict(
    "SetV2LoggingOptionsRequestRequestTypeDef",
    {
        "roleArn": str,
        "defaultLogLevel": LogLevelType,
        "disableAllLogs": bool,
    },
    total=False,
)

SigningProfileParameterOutputTypeDef = TypedDict(
    "SigningProfileParameterOutputTypeDef",
    {
        "certificateArn": str,
        "platform": str,
        "certificatePathOnDevice": str,
    },
    total=False,
)

SigningProfileParameterTypeDef = TypedDict(
    "SigningProfileParameterTypeDef",
    {
        "certificateArn": str,
        "platform": str,
        "certificatePathOnDevice": str,
    },
    total=False,
)

StartAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "StartAuditMitigationActionsTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ViolationEventOccurrenceRangeTypeDef = TypedDict(
    "ViolationEventOccurrenceRangeTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)

StartDetectMitigationActionsTaskResponseTypeDef = TypedDict(
    "StartDetectMitigationActionsTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartOnDemandAuditTaskRequestRequestTypeDef = TypedDict(
    "StartOnDemandAuditTaskRequestRequestTypeDef",
    {
        "targetCheckNames": Sequence[str],
    },
)

StartOnDemandAuditTaskResponseTypeDef = TypedDict(
    "StartOnDemandAuditTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartThingRegistrationTaskRequestRequestTypeDef = TypedDict(
    "StartThingRegistrationTaskRequestRequestTypeDef",
    {
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
    },
)

StartThingRegistrationTaskResponseTypeDef = TypedDict(
    "StartThingRegistrationTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopThingRegistrationTaskRequestRequestTypeDef = TypedDict(
    "StopThingRegistrationTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

TlsContextTypeDef = TypedDict(
    "TlsContextTypeDef",
    {
        "serverName": str,
    },
    total=False,
)

TestInvokeAuthorizerResponseTypeDef = TypedDict(
    "TestInvokeAuthorizerResponseTypeDef",
    {
        "isAuthenticated": bool,
        "principalId": str,
        "policyDocuments": List[str],
        "refreshAfterInSeconds": int,
        "disconnectAfterInSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThingConnectivityTypeDef = TypedDict(
    "ThingConnectivityTypeDef",
    {
        "connected": bool,
        "timestamp": int,
        "disconnectReason": str,
    },
    total=False,
)

TimestreamDimensionOutputTypeDef = TypedDict(
    "TimestreamDimensionOutputTypeDef",
    {
        "name": str,
        "value": str,
    },
)

TimestreamTimestampOutputTypeDef = TypedDict(
    "TimestreamTimestampOutputTypeDef",
    {
        "value": str,
        "unit": str,
    },
)

TimestreamDimensionTypeDef = TypedDict(
    "TimestreamDimensionTypeDef",
    {
        "name": str,
        "value": str,
    },
)

TimestreamTimestampTypeDef = TypedDict(
    "TimestreamTimestampTypeDef",
    {
        "value": str,
        "unit": str,
    },
)

_RequiredVpcDestinationConfigurationTypeDef = TypedDict(
    "_RequiredVpcDestinationConfigurationTypeDef",
    {
        "subnetIds": Sequence[str],
        "vpcId": str,
        "roleArn": str,
    },
)
_OptionalVpcDestinationConfigurationTypeDef = TypedDict(
    "_OptionalVpcDestinationConfigurationTypeDef",
    {
        "securityGroups": Sequence[str],
    },
    total=False,
)


class VpcDestinationConfigurationTypeDef(
    _RequiredVpcDestinationConfigurationTypeDef, _OptionalVpcDestinationConfigurationTypeDef
):
    pass


VpcDestinationSummaryTypeDef = TypedDict(
    "VpcDestinationSummaryTypeDef",
    {
        "subnetIds": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "roleArn": str,
    },
    total=False,
)

VpcDestinationPropertiesTypeDef = TypedDict(
    "VpcDestinationPropertiesTypeDef",
    {
        "subnetIds": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredTransferCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredTransferCertificateRequestRequestTypeDef",
    {
        "certificateId": str,
        "targetAwsAccount": str,
    },
)
_OptionalTransferCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalTransferCertificateRequestRequestTypeDef",
    {
        "transferMessage": str,
    },
    total=False,
)


class TransferCertificateRequestRequestTypeDef(
    _RequiredTransferCertificateRequestRequestTypeDef,
    _OptionalTransferCertificateRequestRequestTypeDef,
):
    pass


TransferCertificateResponseTypeDef = TypedDict(
    "TransferCertificateResponseTypeDef",
    {
        "transferredCertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)
_OptionalUpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAuthorizerRequestRequestTypeDef",
    {
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Mapping[str, str],
        "status": AuthorizerStatusType,
        "enableCachingForHttp": bool,
    },
    total=False,
)


class UpdateAuthorizerRequestRequestTypeDef(
    _RequiredUpdateAuthorizerRequestRequestTypeDef, _OptionalUpdateAuthorizerRequestRequestTypeDef
):
    pass


UpdateAuthorizerResponseTypeDef = TypedDict(
    "UpdateAuthorizerResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBillingGroupResponseTypeDef = TypedDict(
    "UpdateBillingGroupResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCertificateRequestRequestTypeDef = TypedDict(
    "UpdateCertificateRequestRequestTypeDef",
    {
        "certificateId": str,
        "newStatus": CertificateStatusType,
    },
)

UpdateCustomMetricRequestRequestTypeDef = TypedDict(
    "UpdateCustomMetricRequestRequestTypeDef",
    {
        "metricName": str,
        "displayName": str,
    },
)

UpdateCustomMetricResponseTypeDef = TypedDict(
    "UpdateCustomMetricResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "metricType": CustomMetricTypeType,
        "displayName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDimensionRequestRequestTypeDef = TypedDict(
    "UpdateDimensionRequestRequestTypeDef",
    {
        "name": str,
        "stringValues": Sequence[str],
    },
)

UpdateDimensionResponseTypeDef = TypedDict(
    "UpdateDimensionResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainConfigurationResponseTypeDef = TypedDict(
    "UpdateDomainConfigurationResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDynamicThingGroupResponseTypeDef = TypedDict(
    "UpdateDynamicThingGroupResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMitigationActionResponseTypeDef = TypedDict(
    "UpdateMitigationActionResponseTypeDef",
    {
        "actionArn": str,
        "actionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VersionUpdateByJobsConfigTypeDef = TypedDict(
    "VersionUpdateByJobsConfigTypeDef",
    {
        "enabled": bool,
        "roleArn": str,
    },
    total=False,
)

_RequiredUpdatePackageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageRequestRequestTypeDef",
    {
        "packageName": str,
    },
)
_OptionalUpdatePackageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageRequestRequestTypeDef",
    {
        "description": str,
        "defaultVersionName": str,
        "unsetDefaultVersion": bool,
        "clientToken": str,
    },
    total=False,
)


class UpdatePackageRequestRequestTypeDef(
    _RequiredUpdatePackageRequestRequestTypeDef, _OptionalUpdatePackageRequestRequestTypeDef
):
    pass


_RequiredUpdatePackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageVersionRequestRequestTypeDef",
    {
        "packageName": str,
        "versionName": str,
    },
)
_OptionalUpdatePackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageVersionRequestRequestTypeDef",
    {
        "description": str,
        "attributes": Mapping[str, str],
        "action": PackageVersionActionType,
        "clientToken": str,
    },
    total=False,
)


class UpdatePackageVersionRequestRequestTypeDef(
    _RequiredUpdatePackageVersionRequestRequestTypeDef,
    _OptionalUpdatePackageVersionRequestRequestTypeDef,
):
    pass


_RequiredUpdateRoleAliasRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoleAliasRequestRequestTypeDef",
    {
        "roleAlias": str,
    },
)
_OptionalUpdateRoleAliasRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoleAliasRequestRequestTypeDef",
    {
        "roleArn": str,
        "credentialDurationSeconds": int,
    },
    total=False,
)


class UpdateRoleAliasRequestRequestTypeDef(
    _RequiredUpdateRoleAliasRequestRequestTypeDef, _OptionalUpdateRoleAliasRequestRequestTypeDef
):
    pass


UpdateRoleAliasResponseTypeDef = TypedDict(
    "UpdateRoleAliasResponseTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScheduledAuditRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduledAuditRequestRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)
_OptionalUpdateScheduledAuditRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduledAuditRequestRequestTypeDef",
    {
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "targetCheckNames": Sequence[str],
    },
    total=False,
)


class UpdateScheduledAuditRequestRequestTypeDef(
    _RequiredUpdateScheduledAuditRequestRequestTypeDef,
    _OptionalUpdateScheduledAuditRequestRequestTypeDef,
):
    pass


UpdateScheduledAuditResponseTypeDef = TypedDict(
    "UpdateScheduledAuditResponseTypeDef",
    {
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStreamResponseTypeDef = TypedDict(
    "UpdateStreamResponseTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "description": str,
        "streamVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThingGroupResponseTypeDef = TypedDict(
    "UpdateThingGroupResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThingGroupsForThingRequestRequestTypeDef = TypedDict(
    "UpdateThingGroupsForThingRequestRequestTypeDef",
    {
        "thingName": str,
        "thingGroupsToAdd": Sequence[str],
        "thingGroupsToRemove": Sequence[str],
        "overrideDynamicGroups": bool,
    },
    total=False,
)

UpdateTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "UpdateTopicRuleDestinationRequestRequestTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
    },
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "errorMessage": str,
    },
    total=False,
)

AbortConfigOutputTypeDef = TypedDict(
    "AbortConfigOutputTypeDef",
    {
        "criteriaList": List[AbortCriteriaOutputTypeDef],
    },
)

AbortConfigTypeDef = TypedDict(
    "AbortConfigTypeDef",
    {
        "criteriaList": Sequence[AbortCriteriaTypeDef],
    },
)

MetricDatumTypeDef = TypedDict(
    "MetricDatumTypeDef",
    {
        "timestamp": datetime,
        "value": MetricValueOutputTypeDef,
    },
    total=False,
)

DescribeFleetMetricResponseTypeDef = TypedDict(
    "DescribeFleetMetricResponseTypeDef",
    {
        "metricName": str,
        "queryString": str,
        "aggregationType": AggregationTypeOutputTypeDef,
        "period": int,
        "aggregationField": str,
        "description": str,
        "queryVersion": str,
        "indexName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "unit": FleetMetricUnitType,
        "version": int,
        "metricArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetMetricRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetMetricRequestRequestTypeDef",
    {
        "metricName": str,
        "indexName": str,
    },
)
_OptionalUpdateFleetMetricRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetMetricRequestRequestTypeDef",
    {
        "queryString": str,
        "aggregationType": AggregationTypeTypeDef,
        "period": int,
        "aggregationField": str,
        "description": str,
        "queryVersion": str,
        "unit": FleetMetricUnitType,
        "expectedVersion": int,
    },
    total=False,
)


class UpdateFleetMetricRequestRequestTypeDef(
    _RequiredUpdateFleetMetricRequestRequestTypeDef, _OptionalUpdateFleetMetricRequestRequestTypeDef
):
    pass


AllowedTypeDef = TypedDict(
    "AllowedTypeDef",
    {
        "policies": List[PolicyTypeDef],
    },
    total=False,
)

ExplicitDenyTypeDef = TypedDict(
    "ExplicitDenyTypeDef",
    {
        "policies": List[PolicyTypeDef],
    },
    total=False,
)

ImplicitDenyTypeDef = TypedDict(
    "ImplicitDenyTypeDef",
    {
        "policies": List[PolicyTypeDef],
    },
    total=False,
)

ListAttachedPoliciesResponseTypeDef = TypedDict(
    "ListAttachedPoliciesResponseTypeDef",
    {
        "policies": List[PolicyTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "policies": List[PolicyTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPrincipalPoliciesResponseTypeDef = TypedDict(
    "ListPrincipalPoliciesResponseTypeDef",
    {
        "policies": List[PolicyTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssetPropertyValueOutputTypeDef = TypedDict(
    "_RequiredAssetPropertyValueOutputTypeDef",
    {
        "value": AssetPropertyVariantOutputTypeDef,
        "timestamp": AssetPropertyTimestampOutputTypeDef,
    },
)
_OptionalAssetPropertyValueOutputTypeDef = TypedDict(
    "_OptionalAssetPropertyValueOutputTypeDef",
    {
        "quality": str,
    },
    total=False,
)


class AssetPropertyValueOutputTypeDef(
    _RequiredAssetPropertyValueOutputTypeDef, _OptionalAssetPropertyValueOutputTypeDef
):
    pass


_RequiredAssetPropertyValueTypeDef = TypedDict(
    "_RequiredAssetPropertyValueTypeDef",
    {
        "value": AssetPropertyVariantTypeDef,
        "timestamp": AssetPropertyTimestampTypeDef,
    },
)
_OptionalAssetPropertyValueTypeDef = TypedDict(
    "_OptionalAssetPropertyValueTypeDef",
    {
        "quality": str,
    },
    total=False,
)


class AssetPropertyValueTypeDef(
    _RequiredAssetPropertyValueTypeDef, _OptionalAssetPropertyValueTypeDef
):
    pass


ThingGroupPropertiesOutputTypeDef = TypedDict(
    "ThingGroupPropertiesOutputTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": AttributePayloadOutputTypeDef,
    },
    total=False,
)

_RequiredCreateThingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalCreateThingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThingRequestRequestTypeDef",
    {
        "thingTypeName": str,
        "attributePayload": AttributePayloadTypeDef,
        "billingGroupName": str,
    },
    total=False,
)


class CreateThingRequestRequestTypeDef(
    _RequiredCreateThingRequestRequestTypeDef, _OptionalCreateThingRequestRequestTypeDef
):
    pass


ThingGroupPropertiesTypeDef = TypedDict(
    "ThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": AttributePayloadTypeDef,
    },
    total=False,
)

_RequiredUpdateThingRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalUpdateThingRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThingRequestRequestTypeDef",
    {
        "thingTypeName": str,
        "attributePayload": AttributePayloadTypeDef,
        "expectedVersion": int,
        "removeThingType": bool,
    },
    total=False,
)


class UpdateThingRequestRequestTypeDef(
    _RequiredUpdateThingRequestRequestTypeDef, _OptionalUpdateThingRequestRequestTypeDef
):
    pass


ListAuditMitigationActionsExecutionsResponseTypeDef = TypedDict(
    "ListAuditMitigationActionsExecutionsResponseTypeDef",
    {
        "actionsExecutions": List[AuditMitigationActionExecutionMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuditMitigationActionsTasksResponseTypeDef = TypedDict(
    "ListAuditMitigationActionsTasksResponseTypeDef",
    {
        "tasks": List[AuditMitigationActionsTaskMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartAuditMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "StartAuditMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
        "target": AuditMitigationActionsTaskTargetTypeDef,
        "auditCheckToActionsMapping": Mapping[str, Sequence[str]],
        "clientRequestToken": str,
    },
)

DescribeAccountAuditConfigurationResponseTypeDef = TypedDict(
    "DescribeAccountAuditConfigurationResponseTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Dict[
            Literal["SNS"], AuditNotificationTargetOutputTypeDef
        ],
        "auditCheckConfigurations": Dict[str, AuditCheckConfigurationOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAccountAuditConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAccountAuditConfigurationRequestRequestTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Mapping[
            Literal["SNS"], AuditNotificationTargetTypeDef
        ],
        "auditCheckConfigurations": Mapping[str, AuditCheckConfigurationTypeDef],
    },
    total=False,
)

ListAuditTasksResponseTypeDef = TypedDict(
    "ListAuditTasksResponseTypeDef",
    {
        "tasks": List[AuditTaskMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTestAuthorizationRequestRequestTypeDef = TypedDict(
    "_RequiredTestAuthorizationRequestRequestTypeDef",
    {
        "authInfos": Sequence[AuthInfoTypeDef],
    },
)
_OptionalTestAuthorizationRequestRequestTypeDef = TypedDict(
    "_OptionalTestAuthorizationRequestRequestTypeDef",
    {
        "principal": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyNamesToAdd": Sequence[str],
        "policyNamesToSkip": Sequence[str],
    },
    total=False,
)


class TestAuthorizationRequestRequestTypeDef(
    _RequiredTestAuthorizationRequestRequestTypeDef, _OptionalTestAuthorizationRequestRequestTypeDef
):
    pass


DescribeAuthorizerResponseTypeDef = TypedDict(
    "DescribeAuthorizerResponseTypeDef",
    {
        "authorizerDescription": AuthorizerDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDefaultAuthorizerResponseTypeDef = TypedDict(
    "DescribeDefaultAuthorizerResponseTypeDef",
    {
        "authorizerDescription": AuthorizerDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuthorizersResponseTypeDef = TypedDict(
    "ListAuthorizersResponseTypeDef",
    {
        "authorizers": List[AuthorizerSummaryTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AwsJobAbortConfigTypeDef = TypedDict(
    "AwsJobAbortConfigTypeDef",
    {
        "abortCriteriaList": Sequence[AwsJobAbortCriteriaTypeDef],
    },
)

AwsJobExponentialRolloutRateOutputTypeDef = TypedDict(
    "AwsJobExponentialRolloutRateOutputTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": AwsJobRateIncreaseCriteriaOutputTypeDef,
    },
)

AwsJobExponentialRolloutRateTypeDef = TypedDict(
    "AwsJobExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": AwsJobRateIncreaseCriteriaTypeDef,
    },
)

BehaviorCriteriaOutputTypeDef = TypedDict(
    "BehaviorCriteriaOutputTypeDef",
    {
        "comparisonOperator": ComparisonOperatorType,
        "value": MetricValueOutputTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": StatisticalThresholdOutputTypeDef,
        "mlDetectionConfig": MachineLearningDetectionConfigOutputTypeDef,
    },
    total=False,
)

BehaviorCriteriaTypeDef = TypedDict(
    "BehaviorCriteriaTypeDef",
    {
        "comparisonOperator": ComparisonOperatorType,
        "value": MetricValueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": StatisticalThresholdTypeDef,
        "mlDetectionConfig": MachineLearningDetectionConfigTypeDef,
    },
    total=False,
)

GetBehaviorModelTrainingSummariesResponseTypeDef = TypedDict(
    "GetBehaviorModelTrainingSummariesResponseTypeDef",
    {
        "summaries": List[BehaviorModelTrainingSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMetricToRetainOutputTypeDef = TypedDict(
    "_RequiredMetricToRetainOutputTypeDef",
    {
        "metric": str,
    },
)
_OptionalMetricToRetainOutputTypeDef = TypedDict(
    "_OptionalMetricToRetainOutputTypeDef",
    {
        "metricDimension": MetricDimensionOutputTypeDef,
    },
    total=False,
)


class MetricToRetainOutputTypeDef(
    _RequiredMetricToRetainOutputTypeDef, _OptionalMetricToRetainOutputTypeDef
):
    pass


_RequiredMetricToRetainTypeDef = TypedDict(
    "_RequiredMetricToRetainTypeDef",
    {
        "metric": str,
    },
)
_OptionalMetricToRetainTypeDef = TypedDict(
    "_OptionalMetricToRetainTypeDef",
    {
        "metricDimension": MetricDimensionTypeDef,
    },
    total=False,
)


class MetricToRetainTypeDef(_RequiredMetricToRetainTypeDef, _OptionalMetricToRetainTypeDef):
    pass


DescribeBillingGroupResponseTypeDef = TypedDict(
    "DescribeBillingGroupResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupId": str,
        "billingGroupArn": str,
        "version": int,
        "billingGroupProperties": BillingGroupPropertiesOutputTypeDef,
        "billingGroupMetadata": BillingGroupMetadataTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBillingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupProperties": BillingGroupPropertiesTypeDef,
    },
)
_OptionalUpdateBillingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBillingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class UpdateBillingGroupRequestRequestTypeDef(
    _RequiredUpdateBillingGroupRequestRequestTypeDef,
    _OptionalUpdateBillingGroupRequestRequestTypeDef,
):
    pass


GetBucketsAggregationResponseTypeDef = TypedDict(
    "GetBucketsAggregationResponseTypeDef",
    {
        "totalCount": int,
        "buckets": List[BucketTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BucketsAggregationTypeTypeDef = TypedDict(
    "BucketsAggregationTypeTypeDef",
    {
        "termsAggregation": TermsAggregationTypeDef,
    },
    total=False,
)

CACertificateDescriptionTypeDef = TypedDict(
    "CACertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CACertificateStatusType,
        "certificatePem": str,
        "ownedBy": str,
        "creationDate": datetime,
        "autoRegistrationStatus": AutoRegistrationStatusType,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "generationId": str,
        "validity": CertificateValidityTypeDef,
        "certificateMode": CertificateModeType,
    },
    total=False,
)

ListCACertificatesResponseTypeDef = TypedDict(
    "ListCACertificatesResponseTypeDef",
    {
        "certificates": List[CACertificateTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateDescriptionTypeDef = TypedDict(
    "CertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "caCertificateId": str,
        "status": CertificateStatusType,
        "certificatePem": str,
        "ownedBy": str,
        "previousOwnedBy": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "transferData": TransferDataTypeDef,
        "generationId": str,
        "validity": CertificateValidityTypeDef,
        "certificateMode": CertificateModeType,
    },
    total=False,
)

ListCertificatesByCAResponseTypeDef = TypedDict(
    "ListCertificatesByCAResponseTypeDef",
    {
        "certificates": List[CertificateTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {
        "certificates": List[CertificateTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomCodeSigningOutputTypeDef = TypedDict(
    "CustomCodeSigningOutputTypeDef",
    {
        "signature": CodeSigningSignatureOutputTypeDef,
        "certificateChain": CodeSigningCertificateChainOutputTypeDef,
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)

CustomCodeSigningTypeDef = TypedDict(
    "CustomCodeSigningTypeDef",
    {
        "signature": CodeSigningSignatureTypeDef,
        "certificateChain": CodeSigningCertificateChainTypeDef,
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)

DescribeEventConfigurationsResponseTypeDef = TypedDict(
    "DescribeEventConfigurationsResponseTypeDef",
    {
        "eventConfigurations": Dict[EventTypeType, ConfigurationOutputTypeDef],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEventConfigurationsRequestRequestTypeDef = TypedDict(
    "UpdateEventConfigurationsRequestRequestTypeDef",
    {
        "eventConfigurations": Mapping[EventTypeType, ConfigurationTypeDef],
    },
    total=False,
)

_RequiredCreateAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
        "authorizerFunctionArn": str,
    },
)
_OptionalCreateAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAuthorizerRequestRequestTypeDef",
    {
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Mapping[str, str],
        "status": AuthorizerStatusType,
        "tags": Sequence[TagTypeDef],
        "signingDisabled": bool,
        "enableCachingForHttp": bool,
    },
    total=False,
)


class CreateAuthorizerRequestRequestTypeDef(
    _RequiredCreateAuthorizerRequestRequestTypeDef, _OptionalCreateAuthorizerRequestRequestTypeDef
):
    pass


_RequiredCreateBillingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalCreateBillingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBillingGroupRequestRequestTypeDef",
    {
        "billingGroupProperties": BillingGroupPropertiesTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateBillingGroupRequestRequestTypeDef(
    _RequiredCreateBillingGroupRequestRequestTypeDef,
    _OptionalCreateBillingGroupRequestRequestTypeDef,
):
    pass


_RequiredCreateCustomMetricRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomMetricRequestRequestTypeDef",
    {
        "metricName": str,
        "metricType": CustomMetricTypeType,
        "clientRequestToken": str,
    },
)
_OptionalCreateCustomMetricRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomMetricRequestRequestTypeDef",
    {
        "displayName": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateCustomMetricRequestRequestTypeDef(
    _RequiredCreateCustomMetricRequestRequestTypeDef,
    _OptionalCreateCustomMetricRequestRequestTypeDef,
):
    pass


_RequiredCreateDimensionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDimensionRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": Sequence[str],
        "clientRequestToken": str,
    },
)
_OptionalCreateDimensionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDimensionRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateDimensionRequestRequestTypeDef(
    _RequiredCreateDimensionRequestRequestTypeDef, _OptionalCreateDimensionRequestRequestTypeDef
):
    pass


_RequiredCreateFleetMetricRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetMetricRequestRequestTypeDef",
    {
        "metricName": str,
        "queryString": str,
        "aggregationType": AggregationTypeTypeDef,
        "period": int,
        "aggregationField": str,
    },
)
_OptionalCreateFleetMetricRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetMetricRequestRequestTypeDef",
    {
        "description": str,
        "queryVersion": str,
        "indexName": str,
        "unit": FleetMetricUnitType,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateFleetMetricRequestRequestTypeDef(
    _RequiredCreateFleetMetricRequestRequestTypeDef, _OptionalCreateFleetMetricRequestRequestTypeDef
):
    pass


_RequiredCreatePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
    },
)
_OptionalCreatePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreatePolicyRequestRequestTypeDef(
    _RequiredCreatePolicyRequestRequestTypeDef, _OptionalCreatePolicyRequestRequestTypeDef
):
    pass


_RequiredCreateRoleAliasRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoleAliasRequestRequestTypeDef",
    {
        "roleAlias": str,
        "roleArn": str,
    },
)
_OptionalCreateRoleAliasRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoleAliasRequestRequestTypeDef",
    {
        "credentialDurationSeconds": int,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateRoleAliasRequestRequestTypeDef(
    _RequiredCreateRoleAliasRequestRequestTypeDef, _OptionalCreateRoleAliasRequestRequestTypeDef
):
    pass


_RequiredCreateScheduledAuditRequestRequestTypeDef = TypedDict(
    "_RequiredCreateScheduledAuditRequestRequestTypeDef",
    {
        "frequency": AuditFrequencyType,
        "targetCheckNames": Sequence[str],
        "scheduledAuditName": str,
    },
)
_OptionalCreateScheduledAuditRequestRequestTypeDef = TypedDict(
    "_OptionalCreateScheduledAuditRequestRequestTypeDef",
    {
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateScheduledAuditRequestRequestTypeDef(
    _RequiredCreateScheduledAuditRequestRequestTypeDef,
    _OptionalCreateScheduledAuditRequestRequestTypeDef,
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

_RequiredCreateDomainConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainConfigurationRequestRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)
_OptionalCreateDomainConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainConfigurationRequestRequestTypeDef",
    {
        "domainName": str,
        "serverCertificateArns": Sequence[str],
        "validationCertificateArn": str,
        "authorizerConfig": AuthorizerConfigTypeDef,
        "serviceType": ServiceTypeType,
        "tags": Sequence[TagTypeDef],
        "tlsConfig": TlsConfigTypeDef,
    },
    total=False,
)


class CreateDomainConfigurationRequestRequestTypeDef(
    _RequiredCreateDomainConfigurationRequestRequestTypeDef,
    _OptionalCreateDomainConfigurationRequestRequestTypeDef,
):
    pass


_RequiredUpdateDomainConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainConfigurationRequestRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)
_OptionalUpdateDomainConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainConfigurationRequestRequestTypeDef",
    {
        "authorizerConfig": AuthorizerConfigTypeDef,
        "domainConfigurationStatus": DomainConfigurationStatusType,
        "removeAuthorizerConfig": bool,
        "tlsConfig": TlsConfigTypeDef,
    },
    total=False,
)


class UpdateDomainConfigurationRequestRequestTypeDef(
    _RequiredUpdateDomainConfigurationRequestRequestTypeDef,
    _OptionalUpdateDomainConfigurationRequestRequestTypeDef,
):
    pass


SchedulingConfigTypeDef = TypedDict(
    "SchedulingConfigTypeDef",
    {
        "startTime": str,
        "endTime": str,
        "endBehavior": JobEndBehaviorType,
        "maintenanceWindows": Sequence[MaintenanceWindowTypeDef],
    },
    total=False,
)

CreateKeysAndCertificateResponseTypeDef = TypedDict(
    "CreateKeysAndCertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "keyPair": KeyPairTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProvisioningClaimResponseTypeDef = TypedDict(
    "CreateProvisioningClaimResponseTypeDef",
    {
        "certificateId": str,
        "certificatePem": str,
        "keyPair": KeyPairTypeDef,
        "expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProvisioningTemplateRequestRequestTypeDef",
    {
        "templateName": str,
        "templateBody": str,
        "provisioningRoleArn": str,
    },
)
_OptionalCreateProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProvisioningTemplateRequestRequestTypeDef",
    {
        "description": str,
        "enabled": bool,
        "preProvisioningHook": ProvisioningHookTypeDef,
        "tags": Sequence[TagTypeDef],
        "type": TemplateTypeType,
    },
    total=False,
)


class CreateProvisioningTemplateRequestRequestTypeDef(
    _RequiredCreateProvisioningTemplateRequestRequestTypeDef,
    _OptionalCreateProvisioningTemplateRequestRequestTypeDef,
):
    pass


_RequiredUpdateProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProvisioningTemplateRequestRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalUpdateProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProvisioningTemplateRequestRequestTypeDef",
    {
        "description": str,
        "enabled": bool,
        "defaultVersionId": int,
        "provisioningRoleArn": str,
        "preProvisioningHook": ProvisioningHookTypeDef,
        "removePreProvisioningHook": bool,
    },
    total=False,
)


class UpdateProvisioningTemplateRequestRequestTypeDef(
    _RequiredUpdateProvisioningTemplateRequestRequestTypeDef,
    _OptionalUpdateProvisioningTemplateRequestRequestTypeDef,
):
    pass


_RequiredCreateThingTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThingTypeRequestRequestTypeDef",
    {
        "thingTypeName": str,
    },
)
_OptionalCreateThingTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThingTypeRequestRequestTypeDef",
    {
        "thingTypeProperties": ThingTypePropertiesTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateThingTypeRequestRequestTypeDef(
    _RequiredCreateThingTypeRequestRequestTypeDef, _OptionalCreateThingTypeRequestRequestTypeDef
):
    pass


DescribeAuditTaskResponseTypeDef = TypedDict(
    "DescribeAuditTaskResponseTypeDef",
    {
        "taskStatus": AuditTaskStatusType,
        "taskType": AuditTaskTypeType,
        "taskStartTime": datetime,
        "taskStatistics": TaskStatisticsTypeDef,
        "scheduledAuditName": str,
        "auditDetails": Dict[str, AuditCheckDetailsTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainConfigurationResponseTypeDef = TypedDict(
    "DescribeDomainConfigurationResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "domainName": str,
        "serverCertificates": List[ServerCertificateSummaryTypeDef],
        "authorizerConfig": AuthorizerConfigOutputTypeDef,
        "domainConfigurationStatus": DomainConfigurationStatusType,
        "serviceType": ServiceTypeType,
        "domainType": DomainTypeType,
        "lastStatusChangeDate": datetime,
        "tlsConfig": TlsConfigOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SchedulingConfigOutputTypeDef = TypedDict(
    "SchedulingConfigOutputTypeDef",
    {
        "startTime": str,
        "endTime": str,
        "endBehavior": JobEndBehaviorType,
        "maintenanceWindows": List[MaintenanceWindowOutputTypeDef],
    },
    total=False,
)

DescribeManagedJobTemplateResponseTypeDef = TypedDict(
    "DescribeManagedJobTemplateResponseTypeDef",
    {
        "templateName": str,
        "templateArn": str,
        "description": str,
        "templateVersion": str,
        "environments": List[str],
        "documentParameters": List[DocumentParameterTypeDef],
        "document": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningTemplateResponseTypeDef = TypedDict(
    "DescribeProvisioningTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "defaultVersionId": int,
        "templateBody": str,
        "enabled": bool,
        "provisioningRoleArn": str,
        "preProvisioningHook": ProvisioningHookOutputTypeDef,
        "type": TemplateTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoleAliasResponseTypeDef = TypedDict(
    "DescribeRoleAliasResponseTypeDef",
    {
        "roleAliasDescription": RoleAliasDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingTypeResponseTypeDef = TypedDict(
    "DescribeThingTypeResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeId": str,
        "thingTypeArn": str,
        "thingTypeProperties": ThingTypePropertiesOutputTypeDef,
        "thingTypeMetadata": ThingTypeMetadataTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThingTypeDefinitionTypeDef = TypedDict(
    "ThingTypeDefinitionTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": ThingTypePropertiesOutputTypeDef,
        "thingTypeMetadata": ThingTypeMetadataTypeDef,
    },
    total=False,
)

DestinationOutputTypeDef = TypedDict(
    "DestinationOutputTypeDef",
    {
        "s3Destination": S3DestinationOutputTypeDef,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3Destination": S3DestinationTypeDef,
    },
    total=False,
)

ListDetectMitigationActionsExecutionsResponseTypeDef = TypedDict(
    "ListDetectMitigationActionsExecutionsResponseTypeDef",
    {
        "actionsExecutions": List[DetectMitigationActionExecutionTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainConfigurationsResponseTypeDef = TypedDict(
    "ListDomainConfigurationsResponseTypeDef",
    {
        "domainConfigurations": List[DomainConfigurationSummaryTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DynamoDBv2ActionOutputTypeDef = TypedDict(
    "DynamoDBv2ActionOutputTypeDef",
    {
        "roleArn": str,
        "putItem": PutItemInputOutputTypeDef,
    },
)

DynamoDBv2ActionTypeDef = TypedDict(
    "DynamoDBv2ActionTypeDef",
    {
        "roleArn": str,
        "putItem": PutItemInputTypeDef,
    },
)

GetEffectivePoliciesResponseTypeDef = TypedDict(
    "GetEffectivePoliciesResponseTypeDef",
    {
        "effectivePolicies": List[EffectivePolicyTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExponentialRolloutRateOutputTypeDef = TypedDict(
    "ExponentialRolloutRateOutputTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": RateIncreaseCriteriaOutputTypeDef,
    },
)

ExponentialRolloutRateTypeDef = TypedDict(
    "ExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": RateIncreaseCriteriaTypeDef,
    },
)

_RequiredThingGroupIndexingConfigurationOutputTypeDef = TypedDict(
    "_RequiredThingGroupIndexingConfigurationOutputTypeDef",
    {
        "thingGroupIndexingMode": ThingGroupIndexingModeType,
    },
)
_OptionalThingGroupIndexingConfigurationOutputTypeDef = TypedDict(
    "_OptionalThingGroupIndexingConfigurationOutputTypeDef",
    {
        "managedFields": List[FieldOutputTypeDef],
        "customFields": List[FieldOutputTypeDef],
    },
    total=False,
)


class ThingGroupIndexingConfigurationOutputTypeDef(
    _RequiredThingGroupIndexingConfigurationOutputTypeDef,
    _OptionalThingGroupIndexingConfigurationOutputTypeDef,
):
    pass


_RequiredThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_RequiredThingGroupIndexingConfigurationTypeDef",
    {
        "thingGroupIndexingMode": ThingGroupIndexingModeType,
    },
)
_OptionalThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_OptionalThingGroupIndexingConfigurationTypeDef",
    {
        "managedFields": Sequence[FieldTypeDef],
        "customFields": Sequence[FieldTypeDef],
    },
    total=False,
)


class ThingGroupIndexingConfigurationTypeDef(
    _RequiredThingGroupIndexingConfigurationTypeDef, _OptionalThingGroupIndexingConfigurationTypeDef
):
    pass


StreamFileOutputTypeDef = TypedDict(
    "StreamFileOutputTypeDef",
    {
        "fileId": int,
        "s3Location": S3LocationOutputTypeDef,
    },
    total=False,
)

FileLocationOutputTypeDef = TypedDict(
    "FileLocationOutputTypeDef",
    {
        "stream": StreamOutputTypeDef,
        "s3Location": S3LocationOutputTypeDef,
    },
    total=False,
)

StreamFileTypeDef = TypedDict(
    "StreamFileTypeDef",
    {
        "fileId": int,
        "s3Location": S3LocationTypeDef,
    },
    total=False,
)

FileLocationTypeDef = TypedDict(
    "FileLocationTypeDef",
    {
        "stream": StreamTypeDef,
        "s3Location": S3LocationTypeDef,
    },
    total=False,
)

ListFleetMetricsResponseTypeDef = TypedDict(
    "ListFleetMetricsResponseTypeDef",
    {
        "fleetMetrics": List[FleetMetricNameAndArnTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPackageConfigurationResponseTypeDef = TypedDict(
    "GetPackageConfigurationResponseTypeDef",
    {
        "versionUpdateByJobsConfig": VersionUpdateByJobsConfigOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPercentilesResponseTypeDef = TypedDict(
    "GetPercentilesResponseTypeDef",
    {
        "percentiles": List[PercentPairTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStatisticsResponseTypeDef = TypedDict(
    "GetStatisticsResponseTypeDef",
    {
        "statistics": StatisticsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBillingGroupsResponseTypeDef = TypedDict(
    "ListBillingGroupsResponseTypeDef",
    {
        "billingGroups": List[GroupNameAndArnTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingGroupsForThingResponseTypeDef = TypedDict(
    "ListThingGroupsForThingResponseTypeDef",
    {
        "thingGroups": List[GroupNameAndArnTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingGroupsResponseTypeDef = TypedDict(
    "ListThingGroupsResponseTypeDef",
    {
        "thingGroups": List[GroupNameAndArnTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThingGroupMetadataTypeDef = TypedDict(
    "ThingGroupMetadataTypeDef",
    {
        "parentGroupName": str,
        "rootToParentThingGroups": List[GroupNameAndArnTypeDef],
        "creationDate": datetime,
    },
    total=False,
)

HttpAuthorizationOutputTypeDef = TypedDict(
    "HttpAuthorizationOutputTypeDef",
    {
        "sigv4": SigV4AuthorizationOutputTypeDef,
    },
    total=False,
)

HttpAuthorizationTypeDef = TypedDict(
    "HttpAuthorizationTypeDef",
    {
        "sigv4": SigV4AuthorizationTypeDef,
    },
    total=False,
)

_RequiredThingIndexingConfigurationOutputTypeDef = TypedDict(
    "_RequiredThingIndexingConfigurationOutputTypeDef",
    {
        "thingIndexingMode": ThingIndexingModeType,
    },
)
_OptionalThingIndexingConfigurationOutputTypeDef = TypedDict(
    "_OptionalThingIndexingConfigurationOutputTypeDef",
    {
        "thingConnectivityIndexingMode": ThingConnectivityIndexingModeType,
        "deviceDefenderIndexingMode": DeviceDefenderIndexingModeType,
        "namedShadowIndexingMode": NamedShadowIndexingModeType,
        "managedFields": List[FieldOutputTypeDef],
        "customFields": List[FieldOutputTypeDef],
        "filter": IndexingFilterOutputTypeDef,
    },
    total=False,
)


class ThingIndexingConfigurationOutputTypeDef(
    _RequiredThingIndexingConfigurationOutputTypeDef,
    _OptionalThingIndexingConfigurationOutputTypeDef,
):
    pass


_RequiredThingIndexingConfigurationTypeDef = TypedDict(
    "_RequiredThingIndexingConfigurationTypeDef",
    {
        "thingIndexingMode": ThingIndexingModeType,
    },
)
_OptionalThingIndexingConfigurationTypeDef = TypedDict(
    "_OptionalThingIndexingConfigurationTypeDef",
    {
        "thingConnectivityIndexingMode": ThingConnectivityIndexingModeType,
        "deviceDefenderIndexingMode": DeviceDefenderIndexingModeType,
        "namedShadowIndexingMode": NamedShadowIndexingModeType,
        "managedFields": Sequence[FieldTypeDef],
        "customFields": Sequence[FieldTypeDef],
        "filter": IndexingFilterTypeDef,
    },
    total=False,
)


class ThingIndexingConfigurationTypeDef(
    _RequiredThingIndexingConfigurationTypeDef, _OptionalThingIndexingConfigurationTypeDef
):
    pass


JobExecutionTypeDef = TypedDict(
    "JobExecutionTypeDef",
    {
        "jobId": str,
        "status": JobExecutionStatusType,
        "forceCanceled": bool,
        "statusDetails": JobExecutionStatusDetailsTypeDef,
        "thingArn": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
        "versionNumber": int,
        "approximateSecondsBeforeTimedOut": int,
    },
    total=False,
)

JobExecutionSummaryForJobTypeDef = TypedDict(
    "JobExecutionSummaryForJobTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": JobExecutionSummaryTypeDef,
    },
    total=False,
)

JobExecutionSummaryForThingTypeDef = TypedDict(
    "JobExecutionSummaryForThingTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": JobExecutionSummaryTypeDef,
    },
    total=False,
)

JobExecutionsRetryConfigOutputTypeDef = TypedDict(
    "JobExecutionsRetryConfigOutputTypeDef",
    {
        "criteriaList": List[RetryCriteriaOutputTypeDef],
    },
)

JobExecutionsRetryConfigTypeDef = TypedDict(
    "JobExecutionsRetryConfigTypeDef",
    {
        "criteriaList": Sequence[RetryCriteriaTypeDef],
    },
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "jobs": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobTemplatesResponseTypeDef = TypedDict(
    "ListJobTemplatesResponseTypeDef",
    {
        "jobTemplates": List[JobTemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedJobTemplatesResponseTypeDef = TypedDict(
    "ListManagedJobTemplatesResponseTypeDef",
    {
        "managedJobTemplates": List[ManagedJobTemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMitigationActionsResponseTypeDef = TypedDict(
    "ListMitigationActionsResponseTypeDef",
    {
        "actionIdentifiers": List[MitigationActionIdentifierTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOTAUpdatesResponseTypeDef = TypedDict(
    "ListOTAUpdatesResponseTypeDef",
    {
        "otaUpdates": List[OTAUpdateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOutgoingCertificatesResponseTypeDef = TypedDict(
    "ListOutgoingCertificatesResponseTypeDef",
    {
        "outgoingCertificates": List[OutgoingCertificateTypeDef],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackageVersionsResponseTypeDef = TypedDict(
    "ListPackageVersionsResponseTypeDef",
    {
        "packageVersionSummaries": List[PackageVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagesResponseTypeDef = TypedDict(
    "ListPackagesResponseTypeDef",
    {
        "packageSummaries": List[PackageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyVersionsResponseTypeDef = TypedDict(
    "ListPolicyVersionsResponseTypeDef",
    {
        "policyVersions": List[PolicyVersionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisioningTemplateVersionsResponseTypeDef = TypedDict(
    "ListProvisioningTemplateVersionsResponseTypeDef",
    {
        "versions": List[ProvisioningTemplateVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisioningTemplatesResponseTypeDef = TypedDict(
    "ListProvisioningTemplatesResponseTypeDef",
    {
        "templates": List[ProvisioningTemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScheduledAuditsResponseTypeDef = TypedDict(
    "ListScheduledAuditsResponseTypeDef",
    {
        "scheduledAudits": List[ScheduledAuditMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityProfilesResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseTypeDef",
    {
        "securityProfileIdentifiers": List[SecurityProfileIdentifierTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsResponseTypeDef = TypedDict(
    "ListStreamsResponseTypeDef",
    {
        "streams": List[StreamSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetsForSecurityProfileResponseTypeDef = TypedDict(
    "ListTargetsForSecurityProfileResponseTypeDef",
    {
        "securityProfileTargets": List[SecurityProfileTargetTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityProfileTargetMappingTypeDef = TypedDict(
    "SecurityProfileTargetMappingTypeDef",
    {
        "securityProfileIdentifier": SecurityProfileIdentifierTypeDef,
        "target": SecurityProfileTargetTypeDef,
    },
    total=False,
)

ListThingsResponseTypeDef = TypedDict(
    "ListThingsResponseTypeDef",
    {
        "things": List[ThingAttributeTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicRulesResponseTypeDef = TypedDict(
    "ListTopicRulesResponseTypeDef",
    {
        "rules": List[TopicRuleListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLocationActionOutputTypeDef = TypedDict(
    "_RequiredLocationActionOutputTypeDef",
    {
        "roleArn": str,
        "trackerName": str,
        "deviceId": str,
        "latitude": str,
        "longitude": str,
    },
)
_OptionalLocationActionOutputTypeDef = TypedDict(
    "_OptionalLocationActionOutputTypeDef",
    {
        "timestamp": LocationTimestampOutputTypeDef,
    },
    total=False,
)


class LocationActionOutputTypeDef(
    _RequiredLocationActionOutputTypeDef, _OptionalLocationActionOutputTypeDef
):
    pass


_RequiredLocationActionTypeDef = TypedDict(
    "_RequiredLocationActionTypeDef",
    {
        "roleArn": str,
        "trackerName": str,
        "deviceId": str,
        "latitude": str,
        "longitude": str,
    },
)
_OptionalLocationActionTypeDef = TypedDict(
    "_OptionalLocationActionTypeDef",
    {
        "timestamp": LocationTimestampTypeDef,
    },
    total=False,
)


class LocationActionTypeDef(_RequiredLocationActionTypeDef, _OptionalLocationActionTypeDef):
    pass


LogTargetConfigurationTypeDef = TypedDict(
    "LogTargetConfigurationTypeDef",
    {
        "logTarget": LogTargetOutputTypeDef,
        "logLevel": LogLevelType,
    },
    total=False,
)

SetV2LoggingLevelRequestRequestTypeDef = TypedDict(
    "SetV2LoggingLevelRequestRequestTypeDef",
    {
        "logTarget": LogTargetTypeDef,
        "logLevel": LogLevelType,
    },
)

SetLoggingOptionsRequestRequestTypeDef = TypedDict(
    "SetLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptionsPayload": LoggingOptionsPayloadTypeDef,
    },
)

MitigationActionParamsOutputTypeDef = TypedDict(
    "MitigationActionParamsOutputTypeDef",
    {
        "updateDeviceCertificateParams": UpdateDeviceCertificateParamsOutputTypeDef,
        "updateCACertificateParams": UpdateCACertificateParamsOutputTypeDef,
        "addThingsToThingGroupParams": AddThingsToThingGroupParamsOutputTypeDef,
        "replaceDefaultPolicyVersionParams": ReplaceDefaultPolicyVersionParamsOutputTypeDef,
        "enableIoTLoggingParams": EnableIoTLoggingParamsOutputTypeDef,
        "publishFindingToSnsParams": PublishFindingToSnsParamsOutputTypeDef,
    },
    total=False,
)

MitigationActionParamsTypeDef = TypedDict(
    "MitigationActionParamsTypeDef",
    {
        "updateDeviceCertificateParams": UpdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": UpdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": AddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ReplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": EnableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": PublishFindingToSnsParamsTypeDef,
    },
    total=False,
)

MqttHeadersOutputTypeDef = TypedDict(
    "MqttHeadersOutputTypeDef",
    {
        "payloadFormatIndicator": str,
        "contentType": str,
        "responseTopic": str,
        "correlationData": str,
        "messageExpiry": str,
        "userProperties": List[UserPropertyOutputTypeDef],
    },
    total=False,
)

MqttHeadersTypeDef = TypedDict(
    "MqttHeadersTypeDef",
    {
        "payloadFormatIndicator": str,
        "contentType": str,
        "responseTopic": str,
        "correlationData": str,
        "messageExpiry": str,
        "userProperties": Sequence[UserPropertyTypeDef],
    },
    total=False,
)

ResourceIdentifierOutputTypeDef = TypedDict(
    "ResourceIdentifierOutputTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": PolicyVersionIdentifierOutputTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
        "issuerCertificateIdentifier": IssuerCertificateIdentifierOutputTypeDef,
        "deviceCertificateArn": str,
    },
    total=False,
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": PolicyVersionIdentifierTypeDef,
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
        "issuerCertificateIdentifier": IssuerCertificateIdentifierTypeDef,
        "deviceCertificateArn": str,
    },
    total=False,
)

_RequiredRegisterCACertificateRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterCACertificateRequestRequestTypeDef",
    {
        "caCertificate": str,
    },
)
_OptionalRegisterCACertificateRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterCACertificateRequestRequestTypeDef",
    {
        "verificationCertificate": str,
        "setAsActive": bool,
        "allowAutoRegistration": bool,
        "registrationConfig": RegistrationConfigTypeDef,
        "tags": Sequence[TagTypeDef],
        "certificateMode": CertificateModeType,
    },
    total=False,
)


class RegisterCACertificateRequestRequestTypeDef(
    _RequiredRegisterCACertificateRequestRequestTypeDef,
    _OptionalRegisterCACertificateRequestRequestTypeDef,
):
    pass


_RequiredUpdateCACertificateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCACertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalUpdateCACertificateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCACertificateRequestRequestTypeDef",
    {
        "newStatus": CACertificateStatusType,
        "newAutoRegistrationStatus": AutoRegistrationStatusType,
        "registrationConfig": RegistrationConfigTypeDef,
        "removeAutoRegistration": bool,
    },
    total=False,
)


class UpdateCACertificateRequestRequestTypeDef(
    _RequiredUpdateCACertificateRequestRequestTypeDef,
    _OptionalUpdateCACertificateRequestRequestTypeDef,
):
    pass


_RequiredStartDetectMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartDetectMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
        "target": DetectMitigationActionsTaskTargetTypeDef,
        "actions": Sequence[str],
        "clientRequestToken": str,
    },
)
_OptionalStartDetectMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartDetectMitigationActionsTaskRequestRequestTypeDef",
    {
        "violationEventOccurrenceRange": ViolationEventOccurrenceRangeTypeDef,
        "includeOnlyActiveViolations": bool,
        "includeSuppressedAlerts": bool,
    },
    total=False,
)


class StartDetectMitigationActionsTaskRequestRequestTypeDef(
    _RequiredStartDetectMitigationActionsTaskRequestRequestTypeDef,
    _OptionalStartDetectMitigationActionsTaskRequestRequestTypeDef,
):
    pass


_RequiredTestInvokeAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredTestInvokeAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)
_OptionalTestInvokeAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalTestInvokeAuthorizerRequestRequestTypeDef",
    {
        "token": str,
        "tokenSignature": str,
        "httpContext": HttpContextTypeDef,
        "mqttContext": MqttContextTypeDef,
        "tlsContext": TlsContextTypeDef,
    },
    total=False,
)


class TestInvokeAuthorizerRequestRequestTypeDef(
    _RequiredTestInvokeAuthorizerRequestRequestTypeDef,
    _OptionalTestInvokeAuthorizerRequestRequestTypeDef,
):
    pass


ThingDocumentTypeDef = TypedDict(
    "ThingDocumentTypeDef",
    {
        "thingName": str,
        "thingId": str,
        "thingTypeName": str,
        "thingGroupNames": List[str],
        "attributes": Dict[str, str],
        "shadow": str,
        "deviceDefender": str,
        "connectivity": ThingConnectivityTypeDef,
    },
    total=False,
)

_RequiredTimestreamActionOutputTypeDef = TypedDict(
    "_RequiredTimestreamActionOutputTypeDef",
    {
        "roleArn": str,
        "databaseName": str,
        "tableName": str,
        "dimensions": List[TimestreamDimensionOutputTypeDef],
    },
)
_OptionalTimestreamActionOutputTypeDef = TypedDict(
    "_OptionalTimestreamActionOutputTypeDef",
    {
        "timestamp": TimestreamTimestampOutputTypeDef,
    },
    total=False,
)


class TimestreamActionOutputTypeDef(
    _RequiredTimestreamActionOutputTypeDef, _OptionalTimestreamActionOutputTypeDef
):
    pass


_RequiredTimestreamActionTypeDef = TypedDict(
    "_RequiredTimestreamActionTypeDef",
    {
        "roleArn": str,
        "databaseName": str,
        "tableName": str,
        "dimensions": Sequence[TimestreamDimensionTypeDef],
    },
)
_OptionalTimestreamActionTypeDef = TypedDict(
    "_OptionalTimestreamActionTypeDef",
    {
        "timestamp": TimestreamTimestampTypeDef,
    },
    total=False,
)


class TimestreamActionTypeDef(_RequiredTimestreamActionTypeDef, _OptionalTimestreamActionTypeDef):
    pass


TopicRuleDestinationConfigurationTypeDef = TypedDict(
    "TopicRuleDestinationConfigurationTypeDef",
    {
        "httpUrlConfiguration": HttpUrlDestinationConfigurationTypeDef,
        "vpcConfiguration": VpcDestinationConfigurationTypeDef,
    },
    total=False,
)

TopicRuleDestinationSummaryTypeDef = TypedDict(
    "TopicRuleDestinationSummaryTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "statusReason": str,
        "httpUrlSummary": HttpUrlDestinationSummaryTypeDef,
        "vpcDestinationSummary": VpcDestinationSummaryTypeDef,
    },
    total=False,
)

TopicRuleDestinationTypeDef = TypedDict(
    "TopicRuleDestinationTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "statusReason": str,
        "httpUrlProperties": HttpUrlDestinationPropertiesTypeDef,
        "vpcProperties": VpcDestinationPropertiesTypeDef,
    },
    total=False,
)

UpdatePackageConfigurationRequestRequestTypeDef = TypedDict(
    "UpdatePackageConfigurationRequestRequestTypeDef",
    {
        "versionUpdateByJobsConfig": VersionUpdateByJobsConfigTypeDef,
        "clientToken": str,
    },
    total=False,
)

ValidateSecurityProfileBehaviorsResponseTypeDef = TypedDict(
    "ValidateSecurityProfileBehaviorsResponseTypeDef",
    {
        "valid": bool,
        "validationErrors": List[ValidationErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricValuesResponseTypeDef = TypedDict(
    "ListMetricValuesResponseTypeDef",
    {
        "metricDatumList": List[MetricDatumTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeniedTypeDef = TypedDict(
    "DeniedTypeDef",
    {
        "implicitDeny": ImplicitDenyTypeDef,
        "explicitDeny": ExplicitDenyTypeDef,
    },
    total=False,
)

_RequiredPutAssetPropertyValueEntryOutputTypeDef = TypedDict(
    "_RequiredPutAssetPropertyValueEntryOutputTypeDef",
    {
        "propertyValues": List[AssetPropertyValueOutputTypeDef],
    },
)
_OptionalPutAssetPropertyValueEntryOutputTypeDef = TypedDict(
    "_OptionalPutAssetPropertyValueEntryOutputTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)


class PutAssetPropertyValueEntryOutputTypeDef(
    _RequiredPutAssetPropertyValueEntryOutputTypeDef,
    _OptionalPutAssetPropertyValueEntryOutputTypeDef,
):
    pass


_RequiredPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_RequiredPutAssetPropertyValueEntryTypeDef",
    {
        "propertyValues": Sequence[AssetPropertyValueTypeDef],
    },
)
_OptionalPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_OptionalPutAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)


class PutAssetPropertyValueEntryTypeDef(
    _RequiredPutAssetPropertyValueEntryTypeDef, _OptionalPutAssetPropertyValueEntryTypeDef
):
    pass


_RequiredCreateDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDynamicThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "queryString": str,
    },
)
_OptionalCreateDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDynamicThingGroupRequestRequestTypeDef",
    {
        "thingGroupProperties": ThingGroupPropertiesTypeDef,
        "indexName": str,
        "queryVersion": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateDynamicThingGroupRequestRequestTypeDef(
    _RequiredCreateDynamicThingGroupRequestRequestTypeDef,
    _OptionalCreateDynamicThingGroupRequestRequestTypeDef,
):
    pass


_RequiredCreateThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalCreateThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThingGroupRequestRequestTypeDef",
    {
        "parentGroupName": str,
        "thingGroupProperties": ThingGroupPropertiesTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateThingGroupRequestRequestTypeDef(
    _RequiredCreateThingGroupRequestRequestTypeDef, _OptionalCreateThingGroupRequestRequestTypeDef
):
    pass


_RequiredUpdateDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDynamicThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupProperties": ThingGroupPropertiesTypeDef,
    },
)
_OptionalUpdateDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDynamicThingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
    },
    total=False,
)


class UpdateDynamicThingGroupRequestRequestTypeDef(
    _RequiredUpdateDynamicThingGroupRequestRequestTypeDef,
    _OptionalUpdateDynamicThingGroupRequestRequestTypeDef,
):
    pass


_RequiredUpdateThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupProperties": ThingGroupPropertiesTypeDef,
    },
)
_OptionalUpdateThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)


class UpdateThingGroupRequestRequestTypeDef(
    _RequiredUpdateThingGroupRequestRequestTypeDef, _OptionalUpdateThingGroupRequestRequestTypeDef
):
    pass


AwsJobExecutionsRolloutConfigOutputTypeDef = TypedDict(
    "AwsJobExecutionsRolloutConfigOutputTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": AwsJobExponentialRolloutRateOutputTypeDef,
    },
    total=False,
)

AwsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "AwsJobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": AwsJobExponentialRolloutRateTypeDef,
    },
    total=False,
)

_RequiredBehaviorOutputTypeDef = TypedDict(
    "_RequiredBehaviorOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalBehaviorOutputTypeDef = TypedDict(
    "_OptionalBehaviorOutputTypeDef",
    {
        "metric": str,
        "metricDimension": MetricDimensionOutputTypeDef,
        "criteria": BehaviorCriteriaOutputTypeDef,
        "suppressAlerts": bool,
    },
    total=False,
)


class BehaviorOutputTypeDef(_RequiredBehaviorOutputTypeDef, _OptionalBehaviorOutputTypeDef):
    pass


_RequiredBehaviorTypeDef = TypedDict(
    "_RequiredBehaviorTypeDef",
    {
        "name": str,
    },
)
_OptionalBehaviorTypeDef = TypedDict(
    "_OptionalBehaviorTypeDef",
    {
        "metric": str,
        "metricDimension": MetricDimensionTypeDef,
        "criteria": BehaviorCriteriaTypeDef,
        "suppressAlerts": bool,
    },
    total=False,
)


class BehaviorTypeDef(_RequiredBehaviorTypeDef, _OptionalBehaviorTypeDef):
    pass


_RequiredGetBucketsAggregationRequestRequestTypeDef = TypedDict(
    "_RequiredGetBucketsAggregationRequestRequestTypeDef",
    {
        "queryString": str,
        "aggregationField": str,
        "bucketsAggregationType": BucketsAggregationTypeTypeDef,
    },
)
_OptionalGetBucketsAggregationRequestRequestTypeDef = TypedDict(
    "_OptionalGetBucketsAggregationRequestRequestTypeDef",
    {
        "indexName": str,
        "queryVersion": str,
    },
    total=False,
)


class GetBucketsAggregationRequestRequestTypeDef(
    _RequiredGetBucketsAggregationRequestRequestTypeDef,
    _OptionalGetBucketsAggregationRequestRequestTypeDef,
):
    pass


DescribeCACertificateResponseTypeDef = TypedDict(
    "DescribeCACertificateResponseTypeDef",
    {
        "certificateDescription": CACertificateDescriptionTypeDef,
        "registrationConfig": RegistrationConfigOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef",
    {
        "certificateDescription": CertificateDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingTypesResponseTypeDef = TypedDict(
    "ListThingTypesResponseTypeDef",
    {
        "thingTypes": List[ThingTypeDefinitionTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSigningJobParameterOutputTypeDef = TypedDict(
    "StartSigningJobParameterOutputTypeDef",
    {
        "signingProfileParameter": SigningProfileParameterOutputTypeDef,
        "signingProfileName": str,
        "destination": DestinationOutputTypeDef,
    },
    total=False,
)

StartSigningJobParameterTypeDef = TypedDict(
    "StartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": SigningProfileParameterTypeDef,
        "signingProfileName": str,
        "destination": DestinationTypeDef,
    },
    total=False,
)

JobExecutionsRolloutConfigOutputTypeDef = TypedDict(
    "JobExecutionsRolloutConfigOutputTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ExponentialRolloutRateOutputTypeDef,
    },
    total=False,
)

JobExecutionsRolloutConfigTypeDef = TypedDict(
    "JobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ExponentialRolloutRateTypeDef,
    },
    total=False,
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
        "files": List[StreamFileOutputTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "roleArn": str,
    },
    total=False,
)

_RequiredCreateStreamRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStreamRequestRequestTypeDef",
    {
        "streamId": str,
        "files": Sequence[StreamFileTypeDef],
        "roleArn": str,
    },
)
_OptionalCreateStreamRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStreamRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateStreamRequestRequestTypeDef(
    _RequiredCreateStreamRequestRequestTypeDef, _OptionalCreateStreamRequestRequestTypeDef
):
    pass


_RequiredUpdateStreamRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamRequestRequestTypeDef",
    {
        "streamId": str,
    },
)
_OptionalUpdateStreamRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamRequestRequestTypeDef",
    {
        "description": str,
        "files": Sequence[StreamFileTypeDef],
        "roleArn": str,
    },
    total=False,
)


class UpdateStreamRequestRequestTypeDef(
    _RequiredUpdateStreamRequestRequestTypeDef, _OptionalUpdateStreamRequestRequestTypeDef
):
    pass


DescribeThingGroupResponseTypeDef = TypedDict(
    "DescribeThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupArn": str,
        "version": int,
        "thingGroupProperties": ThingGroupPropertiesOutputTypeDef,
        "thingGroupMetadata": ThingGroupMetadataTypeDef,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "status": DynamicGroupStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHttpActionOutputTypeDef = TypedDict(
    "_RequiredHttpActionOutputTypeDef",
    {
        "url": str,
    },
)
_OptionalHttpActionOutputTypeDef = TypedDict(
    "_OptionalHttpActionOutputTypeDef",
    {
        "confirmationUrl": str,
        "headers": List[HttpActionHeaderOutputTypeDef],
        "auth": HttpAuthorizationOutputTypeDef,
    },
    total=False,
)


class HttpActionOutputTypeDef(_RequiredHttpActionOutputTypeDef, _OptionalHttpActionOutputTypeDef):
    pass


_RequiredHttpActionTypeDef = TypedDict(
    "_RequiredHttpActionTypeDef",
    {
        "url": str,
    },
)
_OptionalHttpActionTypeDef = TypedDict(
    "_OptionalHttpActionTypeDef",
    {
        "confirmationUrl": str,
        "headers": Sequence[HttpActionHeaderTypeDef],
        "auth": HttpAuthorizationTypeDef,
    },
    total=False,
)


class HttpActionTypeDef(_RequiredHttpActionTypeDef, _OptionalHttpActionTypeDef):
    pass


GetIndexingConfigurationResponseTypeDef = TypedDict(
    "GetIndexingConfigurationResponseTypeDef",
    {
        "thingIndexingConfiguration": ThingIndexingConfigurationOutputTypeDef,
        "thingGroupIndexingConfiguration": ThingGroupIndexingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIndexingConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateIndexingConfigurationRequestRequestTypeDef",
    {
        "thingIndexingConfiguration": ThingIndexingConfigurationTypeDef,
        "thingGroupIndexingConfiguration": ThingGroupIndexingConfigurationTypeDef,
    },
    total=False,
)

DescribeJobExecutionResponseTypeDef = TypedDict(
    "DescribeJobExecutionResponseTypeDef",
    {
        "execution": JobExecutionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobExecutionsForJobResponseTypeDef = TypedDict(
    "ListJobExecutionsForJobResponseTypeDef",
    {
        "executionSummaries": List[JobExecutionSummaryForJobTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobExecutionsForThingResponseTypeDef = TypedDict(
    "ListJobExecutionsForThingResponseTypeDef",
    {
        "executionSummaries": List[JobExecutionSummaryForThingTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityProfilesForTargetResponseTypeDef = TypedDict(
    "ListSecurityProfilesForTargetResponseTypeDef",
    {
        "securityProfileTargetMappings": List[SecurityProfileTargetMappingTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListV2LoggingLevelsResponseTypeDef = TypedDict(
    "ListV2LoggingLevelsResponseTypeDef",
    {
        "logTargetConfigurations": List[LogTargetConfigurationTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMitigationActionResponseTypeDef = TypedDict(
    "DescribeMitigationActionResponseTypeDef",
    {
        "actionName": str,
        "actionType": MitigationActionTypeType,
        "actionArn": str,
        "actionId": str,
        "roleArn": str,
        "actionParams": MitigationActionParamsOutputTypeDef,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MitigationActionTypeDef = TypedDict(
    "MitigationActionTypeDef",
    {
        "name": str,
        "id": str,
        "roleArn": str,
        "actionParams": MitigationActionParamsOutputTypeDef,
    },
    total=False,
)

_RequiredCreateMitigationActionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMitigationActionRequestRequestTypeDef",
    {
        "actionName": str,
        "roleArn": str,
        "actionParams": MitigationActionParamsTypeDef,
    },
)
_OptionalCreateMitigationActionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMitigationActionRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateMitigationActionRequestRequestTypeDef(
    _RequiredCreateMitigationActionRequestRequestTypeDef,
    _OptionalCreateMitigationActionRequestRequestTypeDef,
):
    pass


_RequiredUpdateMitigationActionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMitigationActionRequestRequestTypeDef",
    {
        "actionName": str,
    },
)
_OptionalUpdateMitigationActionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMitigationActionRequestRequestTypeDef",
    {
        "roleArn": str,
        "actionParams": MitigationActionParamsTypeDef,
    },
    total=False,
)


class UpdateMitigationActionRequestRequestTypeDef(
    _RequiredUpdateMitigationActionRequestRequestTypeDef,
    _OptionalUpdateMitigationActionRequestRequestTypeDef,
):
    pass


_RequiredRepublishActionOutputTypeDef = TypedDict(
    "_RequiredRepublishActionOutputTypeDef",
    {
        "roleArn": str,
        "topic": str,
    },
)
_OptionalRepublishActionOutputTypeDef = TypedDict(
    "_OptionalRepublishActionOutputTypeDef",
    {
        "qos": int,
        "headers": MqttHeadersOutputTypeDef,
    },
    total=False,
)


class RepublishActionOutputTypeDef(
    _RequiredRepublishActionOutputTypeDef, _OptionalRepublishActionOutputTypeDef
):
    pass


_RequiredRepublishActionTypeDef = TypedDict(
    "_RequiredRepublishActionTypeDef",
    {
        "roleArn": str,
        "topic": str,
    },
)
_OptionalRepublishActionTypeDef = TypedDict(
    "_OptionalRepublishActionTypeDef",
    {
        "qos": int,
        "headers": MqttHeadersTypeDef,
    },
    total=False,
)


class RepublishActionTypeDef(_RequiredRepublishActionTypeDef, _OptionalRepublishActionTypeDef):
    pass


_RequiredAuditSuppressionTypeDef = TypedDict(
    "_RequiredAuditSuppressionTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierOutputTypeDef,
    },
)
_OptionalAuditSuppressionTypeDef = TypedDict(
    "_OptionalAuditSuppressionTypeDef",
    {
        "expirationDate": datetime,
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)


class AuditSuppressionTypeDef(_RequiredAuditSuppressionTypeDef, _OptionalAuditSuppressionTypeDef):
    pass


DescribeAuditSuppressionResponseTypeDef = TypedDict(
    "DescribeAuditSuppressionResponseTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierOutputTypeDef,
        "expirationDate": datetime,
        "suppressIndefinitely": bool,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NonCompliantResourceTypeDef = TypedDict(
    "NonCompliantResourceTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIdentifier": ResourceIdentifierOutputTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

RelatedResourceTypeDef = TypedDict(
    "RelatedResourceTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIdentifier": ResourceIdentifierOutputTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

_RequiredCreateAuditSuppressionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAuditSuppressionRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierTypeDef,
        "clientRequestToken": str,
    },
)
_OptionalCreateAuditSuppressionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAuditSuppressionRequestRequestTypeDef",
    {
        "expirationDate": Union[datetime, str],
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)


class CreateAuditSuppressionRequestRequestTypeDef(
    _RequiredCreateAuditSuppressionRequestRequestTypeDef,
    _OptionalCreateAuditSuppressionRequestRequestTypeDef,
):
    pass


DeleteAuditSuppressionRequestRequestTypeDef = TypedDict(
    "DeleteAuditSuppressionRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierTypeDef,
    },
)

DescribeAuditSuppressionRequestRequestTypeDef = TypedDict(
    "DescribeAuditSuppressionRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierTypeDef,
    },
)

ListAuditFindingsRequestListAuditFindingsPaginateTypeDef = TypedDict(
    "ListAuditFindingsRequestListAuditFindingsPaginateTypeDef",
    {
        "taskId": str,
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierTypeDef,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "listSuppressedFindings": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListAuditFindingsRequestRequestTypeDef = TypedDict(
    "ListAuditFindingsRequestRequestTypeDef",
    {
        "taskId": str,
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierTypeDef,
        "maxResults": int,
        "nextToken": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "listSuppressedFindings": bool,
    },
    total=False,
)

ListAuditSuppressionsRequestListAuditSuppressionsPaginateTypeDef = TypedDict(
    "ListAuditSuppressionsRequestListAuditSuppressionsPaginateTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierTypeDef,
        "ascendingOrder": bool,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListAuditSuppressionsRequestRequestTypeDef = TypedDict(
    "ListAuditSuppressionsRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierTypeDef,
        "ascendingOrder": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredUpdateAuditSuppressionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAuditSuppressionRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": ResourceIdentifierTypeDef,
    },
)
_OptionalUpdateAuditSuppressionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAuditSuppressionRequestRequestTypeDef",
    {
        "expirationDate": Union[datetime, str],
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)


class UpdateAuditSuppressionRequestRequestTypeDef(
    _RequiredUpdateAuditSuppressionRequestRequestTypeDef,
    _OptionalUpdateAuditSuppressionRequestRequestTypeDef,
):
    pass


SearchIndexResponseTypeDef = TypedDict(
    "SearchIndexResponseTypeDef",
    {
        "nextToken": str,
        "things": List[ThingDocumentTypeDef],
        "thingGroups": List[ThingGroupDocumentTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "CreateTopicRuleDestinationRequestRequestTypeDef",
    {
        "destinationConfiguration": TopicRuleDestinationConfigurationTypeDef,
    },
)

ListTopicRuleDestinationsResponseTypeDef = TypedDict(
    "ListTopicRuleDestinationsResponseTypeDef",
    {
        "destinationSummaries": List[TopicRuleDestinationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTopicRuleDestinationResponseTypeDef = TypedDict(
    "CreateTopicRuleDestinationResponseTypeDef",
    {
        "topicRuleDestination": TopicRuleDestinationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTopicRuleDestinationResponseTypeDef = TypedDict(
    "GetTopicRuleDestinationResponseTypeDef",
    {
        "topicRuleDestination": TopicRuleDestinationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthResultTypeDef = TypedDict(
    "AuthResultTypeDef",
    {
        "authInfo": AuthInfoOutputTypeDef,
        "allowed": AllowedTypeDef,
        "denied": DeniedTypeDef,
        "authDecision": AuthDecisionType,
        "missingContextValues": List[str],
    },
    total=False,
)

IotSiteWiseActionOutputTypeDef = TypedDict(
    "IotSiteWiseActionOutputTypeDef",
    {
        "putAssetPropertyValueEntries": List[PutAssetPropertyValueEntryOutputTypeDef],
        "roleArn": str,
    },
)

IotSiteWiseActionTypeDef = TypedDict(
    "IotSiteWiseActionTypeDef",
    {
        "putAssetPropertyValueEntries": Sequence[PutAssetPropertyValueEntryTypeDef],
        "roleArn": str,
    },
)

ActiveViolationTypeDef = TypedDict(
    "ActiveViolationTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": BehaviorOutputTypeDef,
        "lastViolationValue": MetricValueOutputTypeDef,
        "violationEventAdditionalInfo": ViolationEventAdditionalInfoTypeDef,
        "verificationState": VerificationStateType,
        "verificationStateDescription": str,
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)

DescribeSecurityProfileResponseTypeDef = TypedDict(
    "DescribeSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List[BehaviorOutputTypeDef],
        "alertTargets": Dict[Literal["SNS"], AlertTargetOutputTypeDef],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List[MetricToRetainOutputTypeDef],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSecurityProfileResponseTypeDef = TypedDict(
    "UpdateSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List[BehaviorOutputTypeDef],
        "alertTargets": Dict[Literal["SNS"], AlertTargetOutputTypeDef],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List[MetricToRetainOutputTypeDef],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ViolationEventTypeDef = TypedDict(
    "ViolationEventTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": BehaviorOutputTypeDef,
        "metricValue": MetricValueOutputTypeDef,
        "violationEventAdditionalInfo": ViolationEventAdditionalInfoTypeDef,
        "violationEventType": ViolationEventTypeType,
        "verificationState": VerificationStateType,
        "verificationStateDescription": str,
        "violationEventTime": datetime,
    },
    total=False,
)

_RequiredCreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalCreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileDescription": str,
        "behaviors": Sequence[BehaviorTypeDef],
        "alertTargets": Mapping[Literal["SNS"], AlertTargetTypeDef],
        "additionalMetricsToRetain": Sequence[str],
        "additionalMetricsToRetainV2": Sequence[MetricToRetainTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateSecurityProfileRequestRequestTypeDef(
    _RequiredCreateSecurityProfileRequestRequestTypeDef,
    _OptionalCreateSecurityProfileRequestRequestTypeDef,
):
    pass


_RequiredUpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalUpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileDescription": str,
        "behaviors": Sequence[BehaviorTypeDef],
        "alertTargets": Mapping[Literal["SNS"], AlertTargetTypeDef],
        "additionalMetricsToRetain": Sequence[str],
        "additionalMetricsToRetainV2": Sequence[MetricToRetainTypeDef],
        "deleteBehaviors": bool,
        "deleteAlertTargets": bool,
        "deleteAdditionalMetricsToRetain": bool,
        "expectedVersion": int,
    },
    total=False,
)


class UpdateSecurityProfileRequestRequestTypeDef(
    _RequiredUpdateSecurityProfileRequestRequestTypeDef,
    _OptionalUpdateSecurityProfileRequestRequestTypeDef,
):
    pass


ValidateSecurityProfileBehaviorsRequestRequestTypeDef = TypedDict(
    "ValidateSecurityProfileBehaviorsRequestRequestTypeDef",
    {
        "behaviors": Sequence[BehaviorTypeDef],
    },
)

CodeSigningOutputTypeDef = TypedDict(
    "CodeSigningOutputTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": StartSigningJobParameterOutputTypeDef,
        "customCodeSigning": CustomCodeSigningOutputTypeDef,
    },
    total=False,
)

CodeSigningTypeDef = TypedDict(
    "CodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": StartSigningJobParameterTypeDef,
        "customCodeSigning": CustomCodeSigningTypeDef,
    },
    total=False,
)

DescribeJobTemplateResponseTypeDef = TypedDict(
    "DescribeJobTemplateResponseTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "description": str,
        "documentSource": str,
        "document": str,
        "createdAt": datetime,
        "presignedUrlConfig": PresignedUrlConfigOutputTypeDef,
        "jobExecutionsRolloutConfig": JobExecutionsRolloutConfigOutputTypeDef,
        "abortConfig": AbortConfigOutputTypeDef,
        "timeoutConfig": TimeoutConfigOutputTypeDef,
        "jobExecutionsRetryConfig": JobExecutionsRetryConfigOutputTypeDef,
        "maintenanceWindows": List[MaintenanceWindowOutputTypeDef],
        "destinationPackageVersions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "targetSelection": TargetSelectionType,
        "status": JobStatusType,
        "forceCanceled": bool,
        "reasonCode": str,
        "comment": str,
        "targets": List[str],
        "description": str,
        "presignedUrlConfig": PresignedUrlConfigOutputTypeDef,
        "jobExecutionsRolloutConfig": JobExecutionsRolloutConfigOutputTypeDef,
        "abortConfig": AbortConfigOutputTypeDef,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
        "jobProcessDetails": JobProcessDetailsTypeDef,
        "timeoutConfig": TimeoutConfigOutputTypeDef,
        "namespaceId": str,
        "jobTemplateArn": str,
        "jobExecutionsRetryConfig": JobExecutionsRetryConfigOutputTypeDef,
        "documentParameters": Dict[str, str],
        "isConcurrent": bool,
        "schedulingConfig": SchedulingConfigOutputTypeDef,
        "scheduledJobRollouts": List[ScheduledJobRolloutTypeDef],
        "destinationPackageVersions": List[str],
    },
    total=False,
)

_RequiredCreateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestRequestTypeDef",
    {
        "jobId": str,
        "targets": Sequence[str],
    },
)
_OptionalCreateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestRequestTypeDef",
    {
        "documentSource": str,
        "document": str,
        "description": str,
        "presignedUrlConfig": PresignedUrlConfigTypeDef,
        "targetSelection": TargetSelectionType,
        "jobExecutionsRolloutConfig": JobExecutionsRolloutConfigTypeDef,
        "abortConfig": AbortConfigTypeDef,
        "timeoutConfig": TimeoutConfigTypeDef,
        "tags": Sequence[TagTypeDef],
        "namespaceId": str,
        "jobTemplateArn": str,
        "jobExecutionsRetryConfig": JobExecutionsRetryConfigTypeDef,
        "documentParameters": Mapping[str, str],
        "schedulingConfig": SchedulingConfigTypeDef,
        "destinationPackageVersions": Sequence[str],
    },
    total=False,
)


class CreateJobRequestRequestTypeDef(
    _RequiredCreateJobRequestRequestTypeDef, _OptionalCreateJobRequestRequestTypeDef
):
    pass


_RequiredCreateJobTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobTemplateRequestRequestTypeDef",
    {
        "jobTemplateId": str,
        "description": str,
    },
)
_OptionalCreateJobTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobTemplateRequestRequestTypeDef",
    {
        "jobArn": str,
        "documentSource": str,
        "document": str,
        "presignedUrlConfig": PresignedUrlConfigTypeDef,
        "jobExecutionsRolloutConfig": JobExecutionsRolloutConfigTypeDef,
        "abortConfig": AbortConfigTypeDef,
        "timeoutConfig": TimeoutConfigTypeDef,
        "tags": Sequence[TagTypeDef],
        "jobExecutionsRetryConfig": JobExecutionsRetryConfigTypeDef,
        "maintenanceWindows": Sequence[MaintenanceWindowTypeDef],
        "destinationPackageVersions": Sequence[str],
    },
    total=False,
)


class CreateJobTemplateRequestRequestTypeDef(
    _RequiredCreateJobTemplateRequestRequestTypeDef, _OptionalCreateJobTemplateRequestRequestTypeDef
):
    pass


_RequiredUpdateJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalUpdateJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobRequestRequestTypeDef",
    {
        "description": str,
        "presignedUrlConfig": PresignedUrlConfigTypeDef,
        "jobExecutionsRolloutConfig": JobExecutionsRolloutConfigTypeDef,
        "abortConfig": AbortConfigTypeDef,
        "timeoutConfig": TimeoutConfigTypeDef,
        "namespaceId": str,
        "jobExecutionsRetryConfig": JobExecutionsRetryConfigTypeDef,
    },
    total=False,
)


class UpdateJobRequestRequestTypeDef(
    _RequiredUpdateJobRequestRequestTypeDef, _OptionalUpdateJobRequestRequestTypeDef
):
    pass


DescribeStreamResponseTypeDef = TypedDict(
    "DescribeStreamResponseTypeDef",
    {
        "streamInfo": StreamInfoTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "DescribeAuditMitigationActionsTaskResponseTypeDef",
    {
        "taskStatus": AuditMitigationActionsTaskStatusType,
        "startTime": datetime,
        "endTime": datetime,
        "taskStatistics": Dict[str, TaskStatisticsForAuditCheckTypeDef],
        "target": AuditMitigationActionsTaskTargetOutputTypeDef,
        "auditCheckToActionsMapping": Dict[str, List[str]],
        "actionsDefinition": List[MitigationActionTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectMitigationActionsTaskSummaryTypeDef = TypedDict(
    "DetectMitigationActionsTaskSummaryTypeDef",
    {
        "taskId": str,
        "taskStatus": DetectMitigationActionsTaskStatusType,
        "taskStartTime": datetime,
        "taskEndTime": datetime,
        "target": DetectMitigationActionsTaskTargetOutputTypeDef,
        "violationEventOccurrenceRange": ViolationEventOccurrenceRangeOutputTypeDef,
        "onlyActiveViolationsIncluded": bool,
        "suppressedAlertsIncluded": bool,
        "actionsDefinition": List[MitigationActionTypeDef],
        "taskStatistics": DetectMitigationActionsTaskStatisticsTypeDef,
    },
    total=False,
)

ListAuditSuppressionsResponseTypeDef = TypedDict(
    "ListAuditSuppressionsResponseTypeDef",
    {
        "suppressions": List[AuditSuppressionTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuditFindingTypeDef = TypedDict(
    "AuditFindingTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": AuditFindingSeverityType,
        "nonCompliantResource": NonCompliantResourceTypeDef,
        "relatedResources": List[RelatedResourceTypeDef],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
        "isSuppressed": bool,
    },
    total=False,
)

ListRelatedResourcesForAuditFindingResponseTypeDef = TypedDict(
    "ListRelatedResourcesForAuditFindingResponseTypeDef",
    {
        "relatedResources": List[RelatedResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestAuthorizationResponseTypeDef = TypedDict(
    "TestAuthorizationResponseTypeDef",
    {
        "authResults": List[AuthResultTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "dynamoDB": DynamoDBActionOutputTypeDef,
        "dynamoDBv2": DynamoDBv2ActionOutputTypeDef,
        "lambda": LambdaActionOutputTypeDef,
        "sns": SnsActionOutputTypeDef,
        "sqs": SqsActionOutputTypeDef,
        "kinesis": KinesisActionOutputTypeDef,
        "republish": RepublishActionOutputTypeDef,
        "s3": S3ActionOutputTypeDef,
        "firehose": FirehoseActionOutputTypeDef,
        "cloudwatchMetric": CloudwatchMetricActionOutputTypeDef,
        "cloudwatchAlarm": CloudwatchAlarmActionOutputTypeDef,
        "cloudwatchLogs": CloudwatchLogsActionOutputTypeDef,
        "elasticsearch": ElasticsearchActionOutputTypeDef,
        "salesforce": SalesforceActionOutputTypeDef,
        "iotAnalytics": IotAnalyticsActionOutputTypeDef,
        "iotEvents": IotEventsActionOutputTypeDef,
        "iotSiteWise": IotSiteWiseActionOutputTypeDef,
        "stepFunctions": StepFunctionsActionOutputTypeDef,
        "timestream": TimestreamActionOutputTypeDef,
        "http": HttpActionOutputTypeDef,
        "kafka": KafkaActionOutputTypeDef,
        "openSearch": OpenSearchActionOutputTypeDef,
        "location": LocationActionOutputTypeDef,
    },
    total=False,
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "dynamoDB": DynamoDBActionTypeDef,
        "dynamoDBv2": DynamoDBv2ActionTypeDef,
        "lambda": LambdaActionTypeDef,
        "sns": SnsActionTypeDef,
        "sqs": SqsActionTypeDef,
        "kinesis": KinesisActionTypeDef,
        "republish": RepublishActionTypeDef,
        "s3": S3ActionTypeDef,
        "firehose": FirehoseActionTypeDef,
        "cloudwatchMetric": CloudwatchMetricActionTypeDef,
        "cloudwatchAlarm": CloudwatchAlarmActionTypeDef,
        "cloudwatchLogs": CloudwatchLogsActionTypeDef,
        "elasticsearch": ElasticsearchActionTypeDef,
        "salesforce": SalesforceActionTypeDef,
        "iotAnalytics": IotAnalyticsActionTypeDef,
        "iotEvents": IotEventsActionTypeDef,
        "iotSiteWise": IotSiteWiseActionTypeDef,
        "stepFunctions": StepFunctionsActionTypeDef,
        "timestream": TimestreamActionTypeDef,
        "http": HttpActionTypeDef,
        "kafka": KafkaActionTypeDef,
        "openSearch": OpenSearchActionTypeDef,
        "location": LocationActionTypeDef,
    },
    total=False,
)

ListActiveViolationsResponseTypeDef = TypedDict(
    "ListActiveViolationsResponseTypeDef",
    {
        "activeViolations": List[ActiveViolationTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListViolationEventsResponseTypeDef = TypedDict(
    "ListViolationEventsResponseTypeDef",
    {
        "violationEvents": List[ViolationEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OTAUpdateFileOutputTypeDef = TypedDict(
    "OTAUpdateFileOutputTypeDef",
    {
        "fileName": str,
        "fileType": int,
        "fileVersion": str,
        "fileLocation": FileLocationOutputTypeDef,
        "codeSigning": CodeSigningOutputTypeDef,
        "attributes": Dict[str, str],
    },
    total=False,
)

OTAUpdateFileTypeDef = TypedDict(
    "OTAUpdateFileTypeDef",
    {
        "fileName": str,
        "fileType": int,
        "fileVersion": str,
        "fileLocation": FileLocationTypeDef,
        "codeSigning": CodeSigningTypeDef,
        "attributes": Mapping[str, str],
    },
    total=False,
)

DescribeJobResponseTypeDef = TypedDict(
    "DescribeJobResponseTypeDef",
    {
        "documentSource": str,
        "job": JobTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDetectMitigationActionsTaskResponseTypeDef = TypedDict(
    "DescribeDetectMitigationActionsTaskResponseTypeDef",
    {
        "taskSummary": DetectMitigationActionsTaskSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectMitigationActionsTasksResponseTypeDef = TypedDict(
    "ListDetectMitigationActionsTasksResponseTypeDef",
    {
        "tasks": List[DetectMitigationActionsTaskSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditFindingResponseTypeDef = TypedDict(
    "DescribeAuditFindingResponseTypeDef",
    {
        "finding": AuditFindingTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuditFindingsResponseTypeDef = TypedDict(
    "ListAuditFindingsResponseTypeDef",
    {
        "findings": List[AuditFindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TopicRuleTypeDef = TypedDict(
    "TopicRuleTypeDef",
    {
        "ruleName": str,
        "sql": str,
        "description": str,
        "createdAt": datetime,
        "actions": List[ActionOutputTypeDef],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ActionOutputTypeDef,
    },
    total=False,
)

_RequiredTopicRulePayloadTypeDef = TypedDict(
    "_RequiredTopicRulePayloadTypeDef",
    {
        "sql": str,
        "actions": Sequence[ActionTypeDef],
    },
)
_OptionalTopicRulePayloadTypeDef = TypedDict(
    "_OptionalTopicRulePayloadTypeDef",
    {
        "description": str,
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ActionTypeDef,
    },
    total=False,
)


class TopicRulePayloadTypeDef(_RequiredTopicRulePayloadTypeDef, _OptionalTopicRulePayloadTypeDef):
    pass


OTAUpdateInfoTypeDef = TypedDict(
    "OTAUpdateInfoTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "description": str,
        "targets": List[str],
        "protocols": List[ProtocolType],
        "awsJobExecutionsRolloutConfig": AwsJobExecutionsRolloutConfigOutputTypeDef,
        "awsJobPresignedUrlConfig": AwsJobPresignedUrlConfigOutputTypeDef,
        "targetSelection": TargetSelectionType,
        "otaUpdateFiles": List[OTAUpdateFileOutputTypeDef],
        "otaUpdateStatus": OTAUpdateStatusType,
        "awsIotJobId": str,
        "awsIotJobArn": str,
        "errorInfo": ErrorInfoTypeDef,
        "additionalParameters": Dict[str, str],
    },
    total=False,
)

_RequiredCreateOTAUpdateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOTAUpdateRequestRequestTypeDef",
    {
        "otaUpdateId": str,
        "targets": Sequence[str],
        "files": Sequence[OTAUpdateFileTypeDef],
        "roleArn": str,
    },
)
_OptionalCreateOTAUpdateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOTAUpdateRequestRequestTypeDef",
    {
        "description": str,
        "protocols": Sequence[ProtocolType],
        "targetSelection": TargetSelectionType,
        "awsJobExecutionsRolloutConfig": AwsJobExecutionsRolloutConfigTypeDef,
        "awsJobPresignedUrlConfig": AwsJobPresignedUrlConfigTypeDef,
        "awsJobAbortConfig": AwsJobAbortConfigTypeDef,
        "awsJobTimeoutConfig": AwsJobTimeoutConfigTypeDef,
        "additionalParameters": Mapping[str, str],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateOTAUpdateRequestRequestTypeDef(
    _RequiredCreateOTAUpdateRequestRequestTypeDef, _OptionalCreateOTAUpdateRequestRequestTypeDef
):
    pass


GetTopicRuleResponseTypeDef = TypedDict(
    "GetTopicRuleResponseTypeDef",
    {
        "ruleArn": str,
        "rule": TopicRuleTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTopicRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
        "topicRulePayload": TopicRulePayloadTypeDef,
    },
)
_OptionalCreateTopicRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTopicRuleRequestRequestTypeDef",
    {
        "tags": str,
    },
    total=False,
)


class CreateTopicRuleRequestRequestTypeDef(
    _RequiredCreateTopicRuleRequestRequestTypeDef, _OptionalCreateTopicRuleRequestRequestTypeDef
):
    pass


ReplaceTopicRuleRequestRequestTypeDef = TypedDict(
    "ReplaceTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
        "topicRulePayload": TopicRulePayloadTypeDef,
    },
)

GetOTAUpdateResponseTypeDef = TypedDict(
    "GetOTAUpdateResponseTypeDef",
    {
        "otaUpdateInfo": OTAUpdateInfoTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
