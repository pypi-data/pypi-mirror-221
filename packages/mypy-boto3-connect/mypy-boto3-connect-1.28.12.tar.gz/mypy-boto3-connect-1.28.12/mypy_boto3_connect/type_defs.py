"""
Type annotations for connect service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/type_defs/)

Usage::

    ```python
    from mypy_boto3_connect.type_defs import ActionSummaryTypeDef

    data: ActionSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionTypeType,
    AgentStatusStateType,
    AgentStatusTypeType,
    BehaviorTypeType,
    ChannelType,
    ContactFlowModuleStateType,
    ContactFlowModuleStatusType,
    ContactFlowStateType,
    ContactFlowTypeType,
    ContactInitiationMethodType,
    ContactStateType,
    CurrentMetricNameType,
    DirectoryTypeType,
    EvaluationFormQuestionTypeType,
    EvaluationFormScoringModeType,
    EvaluationFormScoringStatusType,
    EvaluationFormSingleSelectQuestionDisplayModeType,
    EvaluationFormVersionStatusType,
    EvaluationStatusType,
    EventSourceNameType,
    GroupingType,
    HierarchyGroupMatchTypeType,
    HistoricalMetricNameType,
    HoursOfOperationDaysType,
    InstanceAttributeTypeType,
    InstanceStatusType,
    InstanceStorageResourceTypeType,
    IntegrationTypeType,
    LexVersionType,
    MonitorCapabilityType,
    NumericQuestionPropertyAutomationLabelType,
    ParticipantRoleType,
    ParticipantTimerTypeType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    PhoneNumberWorkflowStatusType,
    PhoneTypeType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    ReferenceStatusType,
    ReferenceTypeType,
    RehydrationTypeType,
    RulePublishStatusType,
    SingleSelectQuestionRuleCategoryAutomationConditionType,
    SortOrderType,
    SourceTypeType,
    StatisticType,
    StorageTypeType,
    StringComparisonTypeType,
    TaskTemplateFieldTypeType,
    TaskTemplateStatusType,
    TimerEligibleParticipantRolesType,
    TrafficDistributionGroupStatusType,
    TrafficTypeType,
    UnitType,
    UseCaseTypeType,
    VocabularyLanguageCodeType,
    VocabularyStateType,
    VoiceRecordingTrackType,
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
    "ActionSummaryTypeDef",
    "ActivateEvaluationFormRequestRequestTypeDef",
    "ActivateEvaluationFormResponseTypeDef",
    "AgentContactReferenceTypeDef",
    "AgentInfoTypeDef",
    "AgentStatusReferenceTypeDef",
    "AgentStatusSummaryTypeDef",
    "AgentStatusTypeDef",
    "AnswerMachineDetectionConfigTypeDef",
    "AssociateApprovedOriginRequestRequestTypeDef",
    "AssociateBotRequestRequestTypeDef",
    "AssociateDefaultVocabularyRequestRequestTypeDef",
    "AssociateInstanceStorageConfigRequestRequestTypeDef",
    "AssociateInstanceStorageConfigResponseTypeDef",
    "AssociateLambdaFunctionRequestRequestTypeDef",
    "AssociateLexBotRequestRequestTypeDef",
    "AssociatePhoneNumberContactFlowRequestRequestTypeDef",
    "AssociateQueueQuickConnectsRequestRequestTypeDef",
    "AssociateRoutingProfileQueuesRequestRequestTypeDef",
    "AssociateSecurityKeyRequestRequestTypeDef",
    "AssociateSecurityKeyResponseTypeDef",
    "AttachmentReferenceTypeDef",
    "AttributeTypeDef",
    "AvailableNumberSummaryTypeDef",
    "ChatMessageTypeDef",
    "ChatParticipantRoleConfigTypeDef",
    "ChatStreamingConfigurationTypeDef",
    "ClaimPhoneNumberRequestRequestTypeDef",
    "ClaimPhoneNumberResponseTypeDef",
    "ClaimedPhoneNumberSummaryTypeDef",
    "ContactFilterTypeDef",
    "ContactFlowModuleSummaryTypeDef",
    "ContactFlowModuleTypeDef",
    "ContactFlowSummaryTypeDef",
    "ContactFlowTypeDef",
    "ContactTypeDef",
    "ControlPlaneTagFilterTypeDef",
    "CreateAgentStatusRequestRequestTypeDef",
    "CreateAgentStatusResponseTypeDef",
    "CreateContactFlowModuleRequestRequestTypeDef",
    "CreateContactFlowModuleResponseTypeDef",
    "CreateContactFlowRequestRequestTypeDef",
    "CreateContactFlowResponseTypeDef",
    "CreateEvaluationFormRequestRequestTypeDef",
    "CreateEvaluationFormResponseTypeDef",
    "CreateHoursOfOperationRequestRequestTypeDef",
    "CreateHoursOfOperationResponseTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreateIntegrationAssociationRequestRequestTypeDef",
    "CreateIntegrationAssociationResponseTypeDef",
    "CreateParticipantRequestRequestTypeDef",
    "CreateParticipantResponseTypeDef",
    "CreatePromptRequestRequestTypeDef",
    "CreatePromptResponseTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateQuickConnectRequestRequestTypeDef",
    "CreateQuickConnectResponseTypeDef",
    "CreateRoutingProfileRequestRequestTypeDef",
    "CreateRoutingProfileResponseTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateSecurityProfileRequestRequestTypeDef",
    "CreateSecurityProfileResponseTypeDef",
    "CreateTaskTemplateRequestRequestTypeDef",
    "CreateTaskTemplateResponseTypeDef",
    "CreateTrafficDistributionGroupRequestRequestTypeDef",
    "CreateTrafficDistributionGroupResponseTypeDef",
    "CreateUseCaseRequestRequestTypeDef",
    "CreateUseCaseResponseTypeDef",
    "CreateUserHierarchyGroupRequestRequestTypeDef",
    "CreateUserHierarchyGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVocabularyRequestRequestTypeDef",
    "CreateVocabularyResponseTypeDef",
    "CredentialsTypeDef",
    "CrossChannelBehaviorOutputTypeDef",
    "CrossChannelBehaviorTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricOutputTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricSortCriteriaTypeDef",
    "CurrentMetricTypeDef",
    "DateReferenceTypeDef",
    "DeactivateEvaluationFormRequestRequestTypeDef",
    "DeactivateEvaluationFormResponseTypeDef",
    "DefaultVocabularyTypeDef",
    "DeleteContactEvaluationRequestRequestTypeDef",
    "DeleteContactFlowModuleRequestRequestTypeDef",
    "DeleteContactFlowRequestRequestTypeDef",
    "DeleteEvaluationFormRequestRequestTypeDef",
    "DeleteHoursOfOperationRequestRequestTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteIntegrationAssociationRequestRequestTypeDef",
    "DeletePromptRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "DeleteQuickConnectRequestRequestTypeDef",
    "DeleteRoutingProfileRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DeleteSecurityProfileRequestRequestTypeDef",
    "DeleteTaskTemplateRequestRequestTypeDef",
    "DeleteTrafficDistributionGroupRequestRequestTypeDef",
    "DeleteUseCaseRequestRequestTypeDef",
    "DeleteUserHierarchyGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteVocabularyRequestRequestTypeDef",
    "DeleteVocabularyResponseTypeDef",
    "DescribeAgentStatusRequestRequestTypeDef",
    "DescribeAgentStatusResponseTypeDef",
    "DescribeContactEvaluationRequestRequestTypeDef",
    "DescribeContactEvaluationResponseTypeDef",
    "DescribeContactFlowModuleRequestRequestTypeDef",
    "DescribeContactFlowModuleResponseTypeDef",
    "DescribeContactFlowRequestRequestTypeDef",
    "DescribeContactFlowResponseTypeDef",
    "DescribeContactRequestRequestTypeDef",
    "DescribeContactResponseTypeDef",
    "DescribeEvaluationFormRequestRequestTypeDef",
    "DescribeEvaluationFormResponseTypeDef",
    "DescribeHoursOfOperationRequestRequestTypeDef",
    "DescribeHoursOfOperationResponseTypeDef",
    "DescribeInstanceAttributeRequestRequestTypeDef",
    "DescribeInstanceAttributeResponseTypeDef",
    "DescribeInstanceRequestRequestTypeDef",
    "DescribeInstanceResponseTypeDef",
    "DescribeInstanceStorageConfigRequestRequestTypeDef",
    "DescribeInstanceStorageConfigResponseTypeDef",
    "DescribePhoneNumberRequestRequestTypeDef",
    "DescribePhoneNumberResponseTypeDef",
    "DescribePromptRequestRequestTypeDef",
    "DescribePromptResponseTypeDef",
    "DescribeQueueRequestRequestTypeDef",
    "DescribeQueueResponseTypeDef",
    "DescribeQuickConnectRequestRequestTypeDef",
    "DescribeQuickConnectResponseTypeDef",
    "DescribeRoutingProfileRequestRequestTypeDef",
    "DescribeRoutingProfileResponseTypeDef",
    "DescribeRuleRequestRequestTypeDef",
    "DescribeRuleResponseTypeDef",
    "DescribeSecurityProfileRequestRequestTypeDef",
    "DescribeSecurityProfileResponseTypeDef",
    "DescribeTrafficDistributionGroupRequestRequestTypeDef",
    "DescribeTrafficDistributionGroupResponseTypeDef",
    "DescribeUserHierarchyGroupRequestRequestTypeDef",
    "DescribeUserHierarchyGroupResponseTypeDef",
    "DescribeUserHierarchyStructureRequestRequestTypeDef",
    "DescribeUserHierarchyStructureResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DescribeVocabularyRequestRequestTypeDef",
    "DescribeVocabularyResponseTypeDef",
    "DimensionsTypeDef",
    "DisassociateApprovedOriginRequestRequestTypeDef",
    "DisassociateBotRequestRequestTypeDef",
    "DisassociateInstanceStorageConfigRequestRequestTypeDef",
    "DisassociateLambdaFunctionRequestRequestTypeDef",
    "DisassociateLexBotRequestRequestTypeDef",
    "DisassociatePhoneNumberContactFlowRequestRequestTypeDef",
    "DisassociateQueueQuickConnectsRequestRequestTypeDef",
    "DisassociateRoutingProfileQueuesRequestRequestTypeDef",
    "DisassociateSecurityKeyRequestRequestTypeDef",
    "DismissUserContactRequestRequestTypeDef",
    "DistributionOutputTypeDef",
    "DistributionTypeDef",
    "EmailReferenceTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionConfigOutputTypeDef",
    "EncryptionConfigTypeDef",
    "EvaluationAnswerDataOutputTypeDef",
    "EvaluationAnswerDataTypeDef",
    "EvaluationAnswerInputTypeDef",
    "EvaluationAnswerOutputTypeDef",
    "EvaluationFormContentTypeDef",
    "EvaluationFormItemOutputTypeDef",
    "EvaluationFormItemTypeDef",
    "EvaluationFormNumericQuestionAutomationOutputTypeDef",
    "EvaluationFormNumericQuestionAutomationTypeDef",
    "EvaluationFormNumericQuestionOptionOutputTypeDef",
    "EvaluationFormNumericQuestionOptionTypeDef",
    "EvaluationFormNumericQuestionPropertiesOutputTypeDef",
    "EvaluationFormNumericQuestionPropertiesTypeDef",
    "EvaluationFormQuestionOutputTypeDef",
    "EvaluationFormQuestionTypeDef",
    "EvaluationFormQuestionTypePropertiesOutputTypeDef",
    "EvaluationFormQuestionTypePropertiesTypeDef",
    "EvaluationFormScoringStrategyOutputTypeDef",
    "EvaluationFormScoringStrategyTypeDef",
    "EvaluationFormSectionOutputTypeDef",
    "EvaluationFormSectionTypeDef",
    "EvaluationFormSingleSelectQuestionAutomationOptionOutputTypeDef",
    "EvaluationFormSingleSelectQuestionAutomationOptionTypeDef",
    "EvaluationFormSingleSelectQuestionAutomationOutputTypeDef",
    "EvaluationFormSingleSelectQuestionAutomationTypeDef",
    "EvaluationFormSingleSelectQuestionOptionOutputTypeDef",
    "EvaluationFormSingleSelectQuestionOptionTypeDef",
    "EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef",
    "EvaluationFormSingleSelectQuestionPropertiesTypeDef",
    "EvaluationFormSummaryTypeDef",
    "EvaluationFormTypeDef",
    "EvaluationFormVersionSummaryTypeDef",
    "EvaluationMetadataTypeDef",
    "EvaluationNoteOutputTypeDef",
    "EvaluationNoteTypeDef",
    "EvaluationScoreTypeDef",
    "EvaluationSummaryTypeDef",
    "EvaluationTypeDef",
    "EventBridgeActionDefinitionOutputTypeDef",
    "EventBridgeActionDefinitionTypeDef",
    "FilterV2TypeDef",
    "FiltersTypeDef",
    "GetContactAttributesRequestRequestTypeDef",
    "GetContactAttributesResponseTypeDef",
    "GetCurrentMetricDataRequestRequestTypeDef",
    "GetCurrentMetricDataResponseTypeDef",
    "GetCurrentUserDataRequestRequestTypeDef",
    "GetCurrentUserDataResponseTypeDef",
    "GetFederationTokenRequestRequestTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetMetricDataRequestGetMetricDataPaginateTypeDef",
    "GetMetricDataRequestRequestTypeDef",
    "GetMetricDataResponseTypeDef",
    "GetMetricDataV2RequestRequestTypeDef",
    "GetMetricDataV2ResponseTypeDef",
    "GetPromptFileRequestRequestTypeDef",
    "GetPromptFileResponseTypeDef",
    "GetTaskTemplateRequestRequestTypeDef",
    "GetTaskTemplateResponseTypeDef",
    "GetTrafficDistributionRequestRequestTypeDef",
    "GetTrafficDistributionResponseTypeDef",
    "HierarchyGroupConditionTypeDef",
    "HierarchyGroupSummaryReferenceTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyLevelTypeDef",
    "HierarchyLevelUpdateTypeDef",
    "HierarchyPathReferenceTypeDef",
    "HierarchyPathTypeDef",
    "HierarchyStructureTypeDef",
    "HierarchyStructureUpdateTypeDef",
    "HistoricalMetricDataTypeDef",
    "HistoricalMetricOutputTypeDef",
    "HistoricalMetricResultTypeDef",
    "HistoricalMetricTypeDef",
    "HoursOfOperationConfigOutputTypeDef",
    "HoursOfOperationConfigTypeDef",
    "HoursOfOperationSearchCriteriaTypeDef",
    "HoursOfOperationSearchFilterTypeDef",
    "HoursOfOperationSummaryTypeDef",
    "HoursOfOperationTimeSliceOutputTypeDef",
    "HoursOfOperationTimeSliceTypeDef",
    "HoursOfOperationTypeDef",
    "InstanceStatusReasonTypeDef",
    "InstanceStorageConfigOutputTypeDef",
    "InstanceStorageConfigTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "IntegrationAssociationSummaryTypeDef",
    "InvisibleFieldInfoOutputTypeDef",
    "InvisibleFieldInfoTypeDef",
    "KinesisFirehoseConfigOutputTypeDef",
    "KinesisFirehoseConfigTypeDef",
    "KinesisStreamConfigOutputTypeDef",
    "KinesisStreamConfigTypeDef",
    "KinesisVideoStreamConfigOutputTypeDef",
    "KinesisVideoStreamConfigTypeDef",
    "LexBotConfigTypeDef",
    "LexBotOutputTypeDef",
    "LexBotTypeDef",
    "LexV2BotOutputTypeDef",
    "LexV2BotTypeDef",
    "ListAgentStatusRequestListAgentStatusesPaginateTypeDef",
    "ListAgentStatusRequestRequestTypeDef",
    "ListAgentStatusResponseTypeDef",
    "ListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef",
    "ListApprovedOriginsRequestRequestTypeDef",
    "ListApprovedOriginsResponseTypeDef",
    "ListBotsRequestListBotsPaginateTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef",
    "ListContactEvaluationsRequestRequestTypeDef",
    "ListContactEvaluationsResponseTypeDef",
    "ListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef",
    "ListContactFlowModulesRequestRequestTypeDef",
    "ListContactFlowModulesResponseTypeDef",
    "ListContactFlowsRequestListContactFlowsPaginateTypeDef",
    "ListContactFlowsRequestRequestTypeDef",
    "ListContactFlowsResponseTypeDef",
    "ListContactReferencesRequestListContactReferencesPaginateTypeDef",
    "ListContactReferencesRequestRequestTypeDef",
    "ListContactReferencesResponseTypeDef",
    "ListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef",
    "ListDefaultVocabulariesRequestRequestTypeDef",
    "ListDefaultVocabulariesResponseTypeDef",
    "ListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef",
    "ListEvaluationFormVersionsRequestRequestTypeDef",
    "ListEvaluationFormVersionsResponseTypeDef",
    "ListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef",
    "ListEvaluationFormsRequestRequestTypeDef",
    "ListEvaluationFormsResponseTypeDef",
    "ListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef",
    "ListHoursOfOperationsRequestRequestTypeDef",
    "ListHoursOfOperationsResponseTypeDef",
    "ListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef",
    "ListInstanceAttributesRequestRequestTypeDef",
    "ListInstanceAttributesResponseTypeDef",
    "ListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef",
    "ListInstanceStorageConfigsRequestRequestTypeDef",
    "ListInstanceStorageConfigsResponseTypeDef",
    "ListInstancesRequestListInstancesPaginateTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef",
    "ListIntegrationAssociationsRequestRequestTypeDef",
    "ListIntegrationAssociationsResponseTypeDef",
    "ListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef",
    "ListLambdaFunctionsRequestRequestTypeDef",
    "ListLambdaFunctionsResponseTypeDef",
    "ListLexBotsRequestListLexBotsPaginateTypeDef",
    "ListLexBotsRequestRequestTypeDef",
    "ListLexBotsResponseTypeDef",
    "ListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListPhoneNumbersSummaryTypeDef",
    "ListPhoneNumbersV2RequestListPhoneNumbersV2PaginateTypeDef",
    "ListPhoneNumbersV2RequestRequestTypeDef",
    "ListPhoneNumbersV2ResponseTypeDef",
    "ListPromptsRequestListPromptsPaginateTypeDef",
    "ListPromptsRequestRequestTypeDef",
    "ListPromptsResponseTypeDef",
    "ListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef",
    "ListQueueQuickConnectsRequestRequestTypeDef",
    "ListQueueQuickConnectsResponseTypeDef",
    "ListQueuesRequestListQueuesPaginateTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResponseTypeDef",
    "ListQuickConnectsRequestListQuickConnectsPaginateTypeDef",
    "ListQuickConnectsRequestRequestTypeDef",
    "ListQuickConnectsResponseTypeDef",
    "ListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef",
    "ListRoutingProfileQueuesRequestRequestTypeDef",
    "ListRoutingProfileQueuesResponseTypeDef",
    "ListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef",
    "ListRoutingProfilesRequestRequestTypeDef",
    "ListRoutingProfilesResponseTypeDef",
    "ListRulesRequestListRulesPaginateTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListSecurityKeysRequestListSecurityKeysPaginateTypeDef",
    "ListSecurityKeysRequestRequestTypeDef",
    "ListSecurityKeysResponseTypeDef",
    "ListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef",
    "ListSecurityProfilePermissionsRequestRequestTypeDef",
    "ListSecurityProfilePermissionsResponseTypeDef",
    "ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef",
    "ListSecurityProfilesRequestRequestTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef",
    "ListTaskTemplatesRequestRequestTypeDef",
    "ListTaskTemplatesResponseTypeDef",
    "ListTrafficDistributionGroupsRequestListTrafficDistributionGroupsPaginateTypeDef",
    "ListTrafficDistributionGroupsRequestRequestTypeDef",
    "ListTrafficDistributionGroupsResponseTypeDef",
    "ListUseCasesRequestListUseCasesPaginateTypeDef",
    "ListUseCasesRequestRequestTypeDef",
    "ListUseCasesResponseTypeDef",
    "ListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef",
    "ListUserHierarchyGroupsRequestRequestTypeDef",
    "ListUserHierarchyGroupsResponseTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MediaConcurrencyOutputTypeDef",
    "MediaConcurrencyTypeDef",
    "MetricDataV2TypeDef",
    "MetricFilterV2OutputTypeDef",
    "MetricFilterV2TypeDef",
    "MetricResultV2TypeDef",
    "MetricV2OutputTypeDef",
    "MetricV2TypeDef",
    "MonitorContactRequestRequestTypeDef",
    "MonitorContactResponseTypeDef",
    "NotificationRecipientTypeOutputTypeDef",
    "NotificationRecipientTypeTypeDef",
    "NumberReferenceTypeDef",
    "NumericQuestionPropertyValueAutomationOutputTypeDef",
    "NumericQuestionPropertyValueAutomationTypeDef",
    "OutboundCallerConfigOutputTypeDef",
    "OutboundCallerConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantDetailsToAddTypeDef",
    "ParticipantDetailsTypeDef",
    "ParticipantTimerConfigurationTypeDef",
    "ParticipantTimerValueTypeDef",
    "ParticipantTokenCredentialsTypeDef",
    "PersistentChatTypeDef",
    "PhoneNumberQuickConnectConfigOutputTypeDef",
    "PhoneNumberQuickConnectConfigTypeDef",
    "PhoneNumberStatusTypeDef",
    "PhoneNumberSummaryTypeDef",
    "PromptSearchCriteriaTypeDef",
    "PromptSearchFilterTypeDef",
    "PromptSummaryTypeDef",
    "PromptTypeDef",
    "PutUserStatusRequestRequestTypeDef",
    "QueueInfoTypeDef",
    "QueueQuickConnectConfigOutputTypeDef",
    "QueueQuickConnectConfigTypeDef",
    "QueueReferenceTypeDef",
    "QueueSearchCriteriaTypeDef",
    "QueueSearchFilterTypeDef",
    "QueueSummaryTypeDef",
    "QueueTypeDef",
    "QuickConnectConfigOutputTypeDef",
    "QuickConnectConfigTypeDef",
    "QuickConnectSearchCriteriaTypeDef",
    "QuickConnectSearchFilterTypeDef",
    "QuickConnectSummaryTypeDef",
    "QuickConnectTypeDef",
    "ReadOnlyFieldInfoOutputTypeDef",
    "ReadOnlyFieldInfoTypeDef",
    "ReferenceOutputTypeDef",
    "ReferenceSummaryTypeDef",
    "ReferenceTypeDef",
    "ReleasePhoneNumberRequestRequestTypeDef",
    "ReplicateInstanceRequestRequestTypeDef",
    "ReplicateInstanceResponseTypeDef",
    "RequiredFieldInfoOutputTypeDef",
    "RequiredFieldInfoTypeDef",
    "ResourceTagsSearchCriteriaTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeContactRecordingRequestRequestTypeDef",
    "RoutingProfileQueueConfigSummaryTypeDef",
    "RoutingProfileQueueConfigTypeDef",
    "RoutingProfileQueueReferenceTypeDef",
    "RoutingProfileReferenceTypeDef",
    "RoutingProfileSearchCriteriaTypeDef",
    "RoutingProfileSearchFilterTypeDef",
    "RoutingProfileSummaryTypeDef",
    "RoutingProfileTypeDef",
    "RuleActionOutputTypeDef",
    "RuleActionTypeDef",
    "RuleSummaryTypeDef",
    "RuleTriggerEventSourceOutputTypeDef",
    "RuleTriggerEventSourceTypeDef",
    "RuleTypeDef",
    "S3ConfigOutputTypeDef",
    "S3ConfigTypeDef",
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    "SearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SearchHoursOfOperationsRequestRequestTypeDef",
    "SearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef",
    "SearchHoursOfOperationsResponseTypeDef",
    "SearchPromptsRequestRequestTypeDef",
    "SearchPromptsRequestSearchPromptsPaginateTypeDef",
    "SearchPromptsResponseTypeDef",
    "SearchQueuesRequestRequestTypeDef",
    "SearchQueuesRequestSearchQueuesPaginateTypeDef",
    "SearchQueuesResponseTypeDef",
    "SearchQuickConnectsRequestRequestTypeDef",
    "SearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef",
    "SearchQuickConnectsResponseTypeDef",
    "SearchResourceTagsRequestRequestTypeDef",
    "SearchResourceTagsRequestSearchResourceTagsPaginateTypeDef",
    "SearchResourceTagsResponseTypeDef",
    "SearchRoutingProfilesRequestRequestTypeDef",
    "SearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef",
    "SearchRoutingProfilesResponseTypeDef",
    "SearchSecurityProfilesRequestRequestTypeDef",
    "SearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef",
    "SearchSecurityProfilesResponseTypeDef",
    "SearchUsersRequestRequestTypeDef",
    "SearchUsersRequestSearchUsersPaginateTypeDef",
    "SearchUsersResponseTypeDef",
    "SearchVocabulariesRequestRequestTypeDef",
    "SearchVocabulariesRequestSearchVocabulariesPaginateTypeDef",
    "SearchVocabulariesResponseTypeDef",
    "SecurityKeyTypeDef",
    "SecurityProfileSearchCriteriaTypeDef",
    "SecurityProfileSearchSummaryTypeDef",
    "SecurityProfileSummaryTypeDef",
    "SecurityProfileTypeDef",
    "SecurityProfilesSearchFilterTypeDef",
    "SendNotificationActionDefinitionOutputTypeDef",
    "SendNotificationActionDefinitionTypeDef",
    "SingleSelectQuestionRuleCategoryAutomationOutputTypeDef",
    "SingleSelectQuestionRuleCategoryAutomationTypeDef",
    "StartChatContactRequestRequestTypeDef",
    "StartChatContactResponseTypeDef",
    "StartContactEvaluationRequestRequestTypeDef",
    "StartContactEvaluationResponseTypeDef",
    "StartContactRecordingRequestRequestTypeDef",
    "StartContactStreamingRequestRequestTypeDef",
    "StartContactStreamingResponseTypeDef",
    "StartOutboundVoiceContactRequestRequestTypeDef",
    "StartOutboundVoiceContactResponseTypeDef",
    "StartTaskContactRequestRequestTypeDef",
    "StartTaskContactResponseTypeDef",
    "StopContactRecordingRequestRequestTypeDef",
    "StopContactRequestRequestTypeDef",
    "StopContactStreamingRequestRequestTypeDef",
    "StringConditionTypeDef",
    "StringReferenceTypeDef",
    "SubmitContactEvaluationRequestRequestTypeDef",
    "SubmitContactEvaluationResponseTypeDef",
    "SuspendContactRecordingRequestRequestTypeDef",
    "TagConditionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagSearchConditionTypeDef",
    "TagSetTypeDef",
    "TaskActionDefinitionOutputTypeDef",
    "TaskActionDefinitionTypeDef",
    "TaskTemplateConstraintsOutputTypeDef",
    "TaskTemplateConstraintsTypeDef",
    "TaskTemplateDefaultFieldValueOutputTypeDef",
    "TaskTemplateDefaultFieldValueTypeDef",
    "TaskTemplateDefaultsOutputTypeDef",
    "TaskTemplateDefaultsTypeDef",
    "TaskTemplateFieldIdentifierOutputTypeDef",
    "TaskTemplateFieldIdentifierTypeDef",
    "TaskTemplateFieldOutputTypeDef",
    "TaskTemplateFieldTypeDef",
    "TaskTemplateMetadataTypeDef",
    "TelephonyConfigOutputTypeDef",
    "TelephonyConfigTypeDef",
    "ThresholdOutputTypeDef",
    "ThresholdTypeDef",
    "ThresholdV2OutputTypeDef",
    "ThresholdV2TypeDef",
    "TrafficDistributionGroupSummaryTypeDef",
    "TrafficDistributionGroupTypeDef",
    "TransferContactRequestRequestTypeDef",
    "TransferContactResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentStatusRequestRequestTypeDef",
    "UpdateContactAttributesRequestRequestTypeDef",
    "UpdateContactEvaluationRequestRequestTypeDef",
    "UpdateContactEvaluationResponseTypeDef",
    "UpdateContactFlowContentRequestRequestTypeDef",
    "UpdateContactFlowMetadataRequestRequestTypeDef",
    "UpdateContactFlowModuleContentRequestRequestTypeDef",
    "UpdateContactFlowModuleMetadataRequestRequestTypeDef",
    "UpdateContactFlowNameRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
    "UpdateContactScheduleRequestRequestTypeDef",
    "UpdateEvaluationFormRequestRequestTypeDef",
    "UpdateEvaluationFormResponseTypeDef",
    "UpdateHoursOfOperationRequestRequestTypeDef",
    "UpdateInstanceAttributeRequestRequestTypeDef",
    "UpdateInstanceStorageConfigRequestRequestTypeDef",
    "UpdateParticipantRoleConfigChannelInfoTypeDef",
    "UpdateParticipantRoleConfigRequestRequestTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdatePromptRequestRequestTypeDef",
    "UpdatePromptResponseTypeDef",
    "UpdateQueueHoursOfOperationRequestRequestTypeDef",
    "UpdateQueueMaxContactsRequestRequestTypeDef",
    "UpdateQueueNameRequestRequestTypeDef",
    "UpdateQueueOutboundCallerConfigRequestRequestTypeDef",
    "UpdateQueueStatusRequestRequestTypeDef",
    "UpdateQuickConnectConfigRequestRequestTypeDef",
    "UpdateQuickConnectNameRequestRequestTypeDef",
    "UpdateRoutingProfileConcurrencyRequestRequestTypeDef",
    "UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef",
    "UpdateRoutingProfileNameRequestRequestTypeDef",
    "UpdateRoutingProfileQueuesRequestRequestTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "UpdateSecurityProfileRequestRequestTypeDef",
    "UpdateTaskTemplateRequestRequestTypeDef",
    "UpdateTaskTemplateResponseTypeDef",
    "UpdateTrafficDistributionRequestRequestTypeDef",
    "UpdateUserHierarchyGroupNameRequestRequestTypeDef",
    "UpdateUserHierarchyRequestRequestTypeDef",
    "UpdateUserHierarchyStructureRequestRequestTypeDef",
    "UpdateUserIdentityInfoRequestRequestTypeDef",
    "UpdateUserPhoneConfigRequestRequestTypeDef",
    "UpdateUserRoutingProfileRequestRequestTypeDef",
    "UpdateUserSecurityProfilesRequestRequestTypeDef",
    "UrlReferenceTypeDef",
    "UseCaseTypeDef",
    "UserDataFiltersTypeDef",
    "UserDataTypeDef",
    "UserIdentityInfoLiteTypeDef",
    "UserIdentityInfoOutputTypeDef",
    "UserIdentityInfoTypeDef",
    "UserPhoneConfigOutputTypeDef",
    "UserPhoneConfigTypeDef",
    "UserQuickConnectConfigOutputTypeDef",
    "UserQuickConnectConfigTypeDef",
    "UserReferenceTypeDef",
    "UserSearchCriteriaTypeDef",
    "UserSearchFilterTypeDef",
    "UserSearchSummaryTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "VocabularySummaryTypeDef",
    "VocabularyTypeDef",
    "VoiceRecordingConfigurationTypeDef",
    "WisdomInfoTypeDef",
)

ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "ActionType": ActionTypeType,
    },
)

ActivateEvaluationFormRequestRequestTypeDef = TypedDict(
    "ActivateEvaluationFormRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationFormId": str,
        "EvaluationFormVersion": int,
    },
)

ActivateEvaluationFormResponseTypeDef = TypedDict(
    "ActivateEvaluationFormResponseTypeDef",
    {
        "EvaluationFormId": str,
        "EvaluationFormArn": str,
        "EvaluationFormVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AgentContactReferenceTypeDef = TypedDict(
    "AgentContactReferenceTypeDef",
    {
        "ContactId": str,
        "Channel": ChannelType,
        "InitiationMethod": ContactInitiationMethodType,
        "AgentContactState": ContactStateType,
        "StateStartTimestamp": datetime,
        "ConnectedToAgentTimestamp": datetime,
        "Queue": "QueueReferenceTypeDef",
    },
    total=False,
)

AgentInfoTypeDef = TypedDict(
    "AgentInfoTypeDef",
    {
        "Id": str,
        "ConnectedToAgentTimestamp": datetime,
    },
    total=False,
)

AgentStatusReferenceTypeDef = TypedDict(
    "AgentStatusReferenceTypeDef",
    {
        "StatusStartTimestamp": datetime,
        "StatusArn": str,
        "StatusName": str,
    },
    total=False,
)

AgentStatusSummaryTypeDef = TypedDict(
    "AgentStatusSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": AgentStatusTypeType,
    },
    total=False,
)

AgentStatusTypeDef = TypedDict(
    "AgentStatusTypeDef",
    {
        "AgentStatusARN": str,
        "AgentStatusId": str,
        "Name": str,
        "Description": str,
        "Type": AgentStatusTypeType,
        "DisplayOrder": int,
        "State": AgentStatusStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

AnswerMachineDetectionConfigTypeDef = TypedDict(
    "AnswerMachineDetectionConfigTypeDef",
    {
        "EnableAnswerMachineDetection": bool,
        "AwaitAnswerMachinePrompt": bool,
    },
    total=False,
)

AssociateApprovedOriginRequestRequestTypeDef = TypedDict(
    "AssociateApprovedOriginRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

_RequiredAssociateBotRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateBotRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalAssociateBotRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateBotRequestRequestTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)


class AssociateBotRequestRequestTypeDef(
    _RequiredAssociateBotRequestRequestTypeDef, _OptionalAssociateBotRequestRequestTypeDef
):
    pass


_RequiredAssociateDefaultVocabularyRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateDefaultVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LanguageCode": VocabularyLanguageCodeType,
    },
)
_OptionalAssociateDefaultVocabularyRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateDefaultVocabularyRequestRequestTypeDef",
    {
        "VocabularyId": str,
    },
    total=False,
)


class AssociateDefaultVocabularyRequestRequestTypeDef(
    _RequiredAssociateDefaultVocabularyRequestRequestTypeDef,
    _OptionalAssociateDefaultVocabularyRequestRequestTypeDef,
):
    pass


AssociateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "AssociateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

AssociateInstanceStorageConfigResponseTypeDef = TypedDict(
    "AssociateInstanceStorageConfigResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateLambdaFunctionRequestRequestTypeDef = TypedDict(
    "AssociateLambdaFunctionRequestRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

AssociateLexBotRequestRequestTypeDef = TypedDict(
    "AssociateLexBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexBot": "LexBotTypeDef",
    },
)

AssociatePhoneNumberContactFlowRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumberContactFlowRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

AssociateQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "AssociateQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": Sequence[str],
    },
)

AssociateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "AssociateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": Sequence["RoutingProfileQueueConfigTypeDef"],
    },
)

AssociateSecurityKeyRequestRequestTypeDef = TypedDict(
    "AssociateSecurityKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Key": str,
    },
)

AssociateSecurityKeyResponseTypeDef = TypedDict(
    "AssociateSecurityKeyResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentReferenceTypeDef = TypedDict(
    "AttachmentReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
        "Status": ReferenceStatusType,
    },
    total=False,
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
    total=False,
)

AvailableNumberSummaryTypeDef = TypedDict(
    "AvailableNumberSummaryTypeDef",
    {
        "PhoneNumber": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
    },
    total=False,
)

ChatMessageTypeDef = TypedDict(
    "ChatMessageTypeDef",
    {
        "ContentType": str,
        "Content": str,
    },
)

ChatParticipantRoleConfigTypeDef = TypedDict(
    "ChatParticipantRoleConfigTypeDef",
    {
        "ParticipantTimerConfigList": Sequence["ParticipantTimerConfigurationTypeDef"],
    },
)

ChatStreamingConfigurationTypeDef = TypedDict(
    "ChatStreamingConfigurationTypeDef",
    {
        "StreamingEndpointArn": str,
    },
)

_RequiredClaimPhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredClaimPhoneNumberRequestRequestTypeDef",
    {
        "TargetArn": str,
        "PhoneNumber": str,
    },
)
_OptionalClaimPhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalClaimPhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberDescription": str,
        "Tags": Mapping[str, str],
        "ClientToken": str,
    },
    total=False,
)


class ClaimPhoneNumberRequestRequestTypeDef(
    _RequiredClaimPhoneNumberRequestRequestTypeDef, _OptionalClaimPhoneNumberRequestRequestTypeDef
):
    pass


ClaimPhoneNumberResponseTypeDef = TypedDict(
    "ClaimPhoneNumberResponseTypeDef",
    {
        "PhoneNumberId": str,
        "PhoneNumberArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClaimedPhoneNumberSummaryTypeDef = TypedDict(
    "ClaimedPhoneNumberSummaryTypeDef",
    {
        "PhoneNumberId": str,
        "PhoneNumberArn": str,
        "PhoneNumber": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
        "PhoneNumberDescription": str,
        "TargetArn": str,
        "Tags": Dict[str, str],
        "PhoneNumberStatus": "PhoneNumberStatusTypeDef",
    },
    total=False,
)

ContactFilterTypeDef = TypedDict(
    "ContactFilterTypeDef",
    {
        "ContactStates": Sequence[ContactStateType],
    },
    total=False,
)

ContactFlowModuleSummaryTypeDef = TypedDict(
    "ContactFlowModuleSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "State": ContactFlowModuleStateType,
    },
    total=False,
)

ContactFlowModuleTypeDef = TypedDict(
    "ContactFlowModuleTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Content": str,
        "Description": str,
        "State": ContactFlowModuleStateType,
        "Status": ContactFlowModuleStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

ContactFlowSummaryTypeDef = TypedDict(
    "ContactFlowSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "ContactFlowType": ContactFlowTypeType,
        "ContactFlowState": ContactFlowStateType,
    },
    total=False,
)

ContactFlowTypeDef = TypedDict(
    "ContactFlowTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "State": ContactFlowStateType,
        "Description": str,
        "Content": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "Arn": str,
        "Id": str,
        "InitialContactId": str,
        "PreviousContactId": str,
        "InitiationMethod": ContactInitiationMethodType,
        "Name": str,
        "Description": str,
        "Channel": ChannelType,
        "QueueInfo": "QueueInfoTypeDef",
        "AgentInfo": "AgentInfoTypeDef",
        "InitiationTimestamp": datetime,
        "DisconnectTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ScheduledTimestamp": datetime,
        "RelatedContactId": str,
        "WisdomInfo": "WisdomInfoTypeDef",
    },
    total=False,
)

ControlPlaneTagFilterTypeDef = TypedDict(
    "ControlPlaneTagFilterTypeDef",
    {
        "OrConditions": Sequence[Sequence["TagConditionTypeDef"]],
        "AndConditions": Sequence["TagConditionTypeDef"],
        "TagCondition": "TagConditionTypeDef",
    },
    total=False,
)

_RequiredCreateAgentStatusRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "State": AgentStatusStateType,
    },
)
_OptionalCreateAgentStatusRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAgentStatusRequestRequestTypeDef",
    {
        "Description": str,
        "DisplayOrder": int,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateAgentStatusRequestRequestTypeDef(
    _RequiredCreateAgentStatusRequestRequestTypeDef, _OptionalCreateAgentStatusRequestRequestTypeDef
):
    pass


CreateAgentStatusResponseTypeDef = TypedDict(
    "CreateAgentStatusResponseTypeDef",
    {
        "AgentStatusARN": str,
        "AgentStatusId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContactFlowModuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Content": str,
    },
)
_OptionalCreateContactFlowModuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactFlowModuleRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
        "ClientToken": str,
    },
    total=False,
)


class CreateContactFlowModuleRequestRequestTypeDef(
    _RequiredCreateContactFlowModuleRequestRequestTypeDef,
    _OptionalCreateContactFlowModuleRequestRequestTypeDef,
):
    pass


CreateContactFlowModuleResponseTypeDef = TypedDict(
    "CreateContactFlowModuleResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContactFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "Content": str,
    },
)
_OptionalCreateContactFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactFlowRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateContactFlowRequestRequestTypeDef(
    _RequiredCreateContactFlowRequestRequestTypeDef, _OptionalCreateContactFlowRequestRequestTypeDef
):
    pass


CreateContactFlowResponseTypeDef = TypedDict(
    "CreateContactFlowResponseTypeDef",
    {
        "ContactFlowId": str,
        "ContactFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEvaluationFormRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEvaluationFormRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Title": str,
        "Items": Sequence["EvaluationFormItemTypeDef"],
    },
)
_OptionalCreateEvaluationFormRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEvaluationFormRequestRequestTypeDef",
    {
        "Description": str,
        "ScoringStrategy": "EvaluationFormScoringStrategyTypeDef",
        "ClientToken": str,
    },
    total=False,
)


class CreateEvaluationFormRequestRequestTypeDef(
    _RequiredCreateEvaluationFormRequestRequestTypeDef,
    _OptionalCreateEvaluationFormRequestRequestTypeDef,
):
    pass


CreateEvaluationFormResponseTypeDef = TypedDict(
    "CreateEvaluationFormResponseTypeDef",
    {
        "EvaluationFormId": str,
        "EvaluationFormArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "TimeZone": str,
        "Config": Sequence["HoursOfOperationConfigTypeDef"],
    },
)
_OptionalCreateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHoursOfOperationRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateHoursOfOperationRequestRequestTypeDef(
    _RequiredCreateHoursOfOperationRequestRequestTypeDef,
    _OptionalCreateHoursOfOperationRequestRequestTypeDef,
):
    pass


CreateHoursOfOperationResponseTypeDef = TypedDict(
    "CreateHoursOfOperationResponseTypeDef",
    {
        "HoursOfOperationId": str,
        "HoursOfOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceRequestRequestTypeDef",
    {
        "IdentityManagementType": DirectoryTypeType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
)
_OptionalCreateInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InstanceAlias": str,
        "DirectoryId": str,
    },
    total=False,
)


class CreateInstanceRequestRequestTypeDef(
    _RequiredCreateInstanceRequestRequestTypeDef, _OptionalCreateInstanceRequestRequestTypeDef
):
    pass


CreateInstanceResponseTypeDef = TypedDict(
    "CreateInstanceResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationAssociationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationArn": str,
    },
)
_OptionalCreateIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationAssociationRequestRequestTypeDef",
    {
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceTypeType,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateIntegrationAssociationRequestRequestTypeDef(
    _RequiredCreateIntegrationAssociationRequestRequestTypeDef,
    _OptionalCreateIntegrationAssociationRequestRequestTypeDef,
):
    pass


CreateIntegrationAssociationResponseTypeDef = TypedDict(
    "CreateIntegrationAssociationResponseTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateParticipantRequestRequestTypeDef = TypedDict(
    "_RequiredCreateParticipantRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ParticipantDetails": "ParticipantDetailsToAddTypeDef",
    },
)
_OptionalCreateParticipantRequestRequestTypeDef = TypedDict(
    "_OptionalCreateParticipantRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class CreateParticipantRequestRequestTypeDef(
    _RequiredCreateParticipantRequestRequestTypeDef, _OptionalCreateParticipantRequestRequestTypeDef
):
    pass


CreateParticipantResponseTypeDef = TypedDict(
    "CreateParticipantResponseTypeDef",
    {
        "ParticipantCredentials": "ParticipantTokenCredentialsTypeDef",
        "ParticipantId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePromptRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePromptRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "S3Uri": str,
    },
)
_OptionalCreatePromptRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePromptRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreatePromptRequestRequestTypeDef(
    _RequiredCreatePromptRequestRequestTypeDef, _OptionalCreatePromptRequestRequestTypeDef
):
    pass


CreatePromptResponseTypeDef = TypedDict(
    "CreatePromptResponseTypeDef",
    {
        "PromptARN": str,
        "PromptId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQueueRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "HoursOfOperationId": str,
    },
)
_OptionalCreateQueueRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQueueRequestRequestTypeDef",
    {
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
        "MaxContacts": int,
        "QuickConnectIds": Sequence[str],
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateQueueRequestRequestTypeDef(
    _RequiredCreateQueueRequestRequestTypeDef, _OptionalCreateQueueRequestRequestTypeDef
):
    pass


CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef",
    {
        "QueueArn": str,
        "QueueId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuickConnectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)
_OptionalCreateQuickConnectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQuickConnectRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateQuickConnectRequestRequestTypeDef(
    _RequiredCreateQuickConnectRequestRequestTypeDef,
    _OptionalCreateQuickConnectRequestRequestTypeDef,
):
    pass


CreateQuickConnectResponseTypeDef = TypedDict(
    "CreateQuickConnectResponseTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoutingProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Description": str,
        "DefaultOutboundQueueId": str,
        "MediaConcurrencies": Sequence["MediaConcurrencyTypeDef"],
    },
)
_OptionalCreateRoutingProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoutingProfileRequestRequestTypeDef",
    {
        "QueueConfigs": Sequence["RoutingProfileQueueConfigTypeDef"],
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateRoutingProfileRequestRequestTypeDef(
    _RequiredCreateRoutingProfileRequestRequestTypeDef,
    _OptionalCreateRoutingProfileRequestRequestTypeDef,
):
    pass


CreateRoutingProfileResponseTypeDef = TypedDict(
    "CreateRoutingProfileResponseTypeDef",
    {
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "TriggerEventSource": "RuleTriggerEventSourceTypeDef",
        "Function": str,
        "Actions": Sequence["RuleActionTypeDef"],
        "PublishStatus": RulePublishStatusType,
    },
)
_OptionalCreateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class CreateRuleRequestRequestTypeDef(
    _RequiredCreateRuleRequestRequestTypeDef, _OptionalCreateRuleRequestRequestTypeDef
):
    pass


CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "RuleArn": str,
        "RuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileName": str,
        "InstanceId": str,
    },
)
_OptionalCreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityProfileRequestRequestTypeDef",
    {
        "Description": str,
        "Permissions": Sequence[str],
        "Tags": Mapping[str, str],
        "AllowedAccessControlTags": Mapping[str, str],
        "TagRestrictedResources": Sequence[str],
    },
    total=False,
)


class CreateSecurityProfileRequestRequestTypeDef(
    _RequiredCreateSecurityProfileRequestRequestTypeDef,
    _OptionalCreateSecurityProfileRequestRequestTypeDef,
):
    pass


CreateSecurityProfileResponseTypeDef = TypedDict(
    "CreateSecurityProfileResponseTypeDef",
    {
        "SecurityProfileId": str,
        "SecurityProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTaskTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTaskTemplateRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Fields": Sequence["TaskTemplateFieldTypeDef"],
    },
)
_OptionalCreateTaskTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTaskTemplateRequestRequestTypeDef",
    {
        "Description": str,
        "ContactFlowId": str,
        "Constraints": "TaskTemplateConstraintsTypeDef",
        "Defaults": "TaskTemplateDefaultsTypeDef",
        "Status": TaskTemplateStatusType,
        "ClientToken": str,
    },
    total=False,
)


class CreateTaskTemplateRequestRequestTypeDef(
    _RequiredCreateTaskTemplateRequestRequestTypeDef,
    _OptionalCreateTaskTemplateRequestRequestTypeDef,
):
    pass


CreateTaskTemplateResponseTypeDef = TypedDict(
    "CreateTaskTemplateResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficDistributionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficDistributionGroupRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
    },
)
_OptionalCreateTrafficDistributionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficDistributionGroupRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateTrafficDistributionGroupRequestRequestTypeDef(
    _RequiredCreateTrafficDistributionGroupRequestRequestTypeDef,
    _OptionalCreateTrafficDistributionGroupRequestRequestTypeDef,
):
    pass


CreateTrafficDistributionGroupResponseTypeDef = TypedDict(
    "CreateTrafficDistributionGroupResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUseCaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUseCaseRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseType": UseCaseTypeType,
    },
)
_OptionalCreateUseCaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUseCaseRequestRequestTypeDef",
    {
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateUseCaseRequestRequestTypeDef(
    _RequiredCreateUseCaseRequestRequestTypeDef, _OptionalCreateUseCaseRequestRequestTypeDef
):
    pass


CreateUseCaseResponseTypeDef = TypedDict(
    "CreateUseCaseResponseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserHierarchyGroupRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
    },
)
_OptionalCreateUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserHierarchyGroupRequestRequestTypeDef",
    {
        "ParentGroupId": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateUserHierarchyGroupRequestRequestTypeDef(
    _RequiredCreateUserHierarchyGroupRequestRequestTypeDef,
    _OptionalCreateUserHierarchyGroupRequestRequestTypeDef,
):
    pass


CreateUserHierarchyGroupResponseTypeDef = TypedDict(
    "CreateUserHierarchyGroupResponseTypeDef",
    {
        "HierarchyGroupId": str,
        "HierarchyGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "Username": str,
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "SecurityProfileIds": Sequence[str],
        "RoutingProfileId": str,
        "InstanceId": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "Password": str,
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "DirectoryUserId": str,
        "HierarchyGroupId": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass


CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
        "UserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVocabularyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyName": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "Content": str,
    },
)
_OptionalCreateVocabularyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVocabularyRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateVocabularyRequestRequestTypeDef(
    _RequiredCreateVocabularyRequestRequestTypeDef, _OptionalCreateVocabularyRequestRequestTypeDef
):
    pass


CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyArn": str,
        "VocabularyId": str,
        "State": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessToken": str,
        "AccessTokenExpiration": datetime,
        "RefreshToken": str,
        "RefreshTokenExpiration": datetime,
    },
    total=False,
)

CrossChannelBehaviorOutputTypeDef = TypedDict(
    "CrossChannelBehaviorOutputTypeDef",
    {
        "BehaviorType": BehaviorTypeType,
    },
)

CrossChannelBehaviorTypeDef = TypedDict(
    "CrossChannelBehaviorTypeDef",
    {
        "BehaviorType": BehaviorTypeType,
    },
)

CurrentMetricDataTypeDef = TypedDict(
    "CurrentMetricDataTypeDef",
    {
        "Metric": "CurrentMetricOutputTypeDef",
        "Value": float,
    },
    total=False,
)

CurrentMetricOutputTypeDef = TypedDict(
    "CurrentMetricOutputTypeDef",
    {
        "Name": CurrentMetricNameType,
        "Unit": UnitType,
    },
    total=False,
)

CurrentMetricResultTypeDef = TypedDict(
    "CurrentMetricResultTypeDef",
    {
        "Dimensions": "DimensionsTypeDef",
        "Collections": List["CurrentMetricDataTypeDef"],
    },
    total=False,
)

CurrentMetricSortCriteriaTypeDef = TypedDict(
    "CurrentMetricSortCriteriaTypeDef",
    {
        "SortByMetric": CurrentMetricNameType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

CurrentMetricTypeDef = TypedDict(
    "CurrentMetricTypeDef",
    {
        "Name": CurrentMetricNameType,
        "Unit": UnitType,
    },
    total=False,
)

DateReferenceTypeDef = TypedDict(
    "DateReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

DeactivateEvaluationFormRequestRequestTypeDef = TypedDict(
    "DeactivateEvaluationFormRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationFormId": str,
        "EvaluationFormVersion": int,
    },
)

DeactivateEvaluationFormResponseTypeDef = TypedDict(
    "DeactivateEvaluationFormResponseTypeDef",
    {
        "EvaluationFormId": str,
        "EvaluationFormArn": str,
        "EvaluationFormVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultVocabularyTypeDef = TypedDict(
    "DefaultVocabularyTypeDef",
    {
        "InstanceId": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "VocabularyId": str,
        "VocabularyName": str,
    },
)

DeleteContactEvaluationRequestRequestTypeDef = TypedDict(
    "DeleteContactEvaluationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationId": str,
    },
)

DeleteContactFlowModuleRequestRequestTypeDef = TypedDict(
    "DeleteContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
    },
)

DeleteContactFlowRequestRequestTypeDef = TypedDict(
    "DeleteContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

_RequiredDeleteEvaluationFormRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteEvaluationFormRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationFormId": str,
    },
)
_OptionalDeleteEvaluationFormRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteEvaluationFormRequestRequestTypeDef",
    {
        "EvaluationFormVersion": int,
    },
    total=False,
)


class DeleteEvaluationFormRequestRequestTypeDef(
    _RequiredDeleteEvaluationFormRequestRequestTypeDef,
    _OptionalDeleteEvaluationFormRequestRequestTypeDef,
):
    pass


DeleteHoursOfOperationRequestRequestTypeDef = TypedDict(
    "DeleteHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)

DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeleteIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationAssociationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)

DeletePromptRequestRequestTypeDef = TypedDict(
    "DeletePromptRequestRequestTypeDef",
    {
        "InstanceId": str,
        "PromptId": str,
    },
)

DeleteQueueRequestRequestTypeDef = TypedDict(
    "DeleteQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)

DeleteQuickConnectRequestRequestTypeDef = TypedDict(
    "DeleteQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DeleteRoutingProfileRequestRequestTypeDef = TypedDict(
    "DeleteRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RuleId": str,
    },
)

DeleteSecurityProfileRequestRequestTypeDef = TypedDict(
    "DeleteSecurityProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SecurityProfileId": str,
    },
)

DeleteTaskTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTaskTemplateRequestRequestTypeDef",
    {
        "InstanceId": str,
        "TaskTemplateId": str,
    },
)

DeleteTrafficDistributionGroupRequestRequestTypeDef = TypedDict(
    "DeleteTrafficDistributionGroupRequestRequestTypeDef",
    {
        "TrafficDistributionGroupId": str,
    },
)

DeleteUseCaseRequestRequestTypeDef = TypedDict(
    "DeleteUseCaseRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseId": str,
    },
)

DeleteUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "DeleteUserHierarchyGroupRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "InstanceId": str,
        "UserId": str,
    },
)

DeleteVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyId": str,
    },
)

DeleteVocabularyResponseTypeDef = TypedDict(
    "DeleteVocabularyResponseTypeDef",
    {
        "VocabularyArn": str,
        "VocabularyId": str,
        "State": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAgentStatusRequestRequestTypeDef = TypedDict(
    "DescribeAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AgentStatusId": str,
    },
)

DescribeAgentStatusResponseTypeDef = TypedDict(
    "DescribeAgentStatusResponseTypeDef",
    {
        "AgentStatus": "AgentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactEvaluationRequestRequestTypeDef = TypedDict(
    "DescribeContactEvaluationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationId": str,
    },
)

DescribeContactEvaluationResponseTypeDef = TypedDict(
    "DescribeContactEvaluationResponseTypeDef",
    {
        "Evaluation": "EvaluationTypeDef",
        "EvaluationForm": "EvaluationFormContentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactFlowModuleRequestRequestTypeDef = TypedDict(
    "DescribeContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
    },
)

DescribeContactFlowModuleResponseTypeDef = TypedDict(
    "DescribeContactFlowModuleResponseTypeDef",
    {
        "ContactFlowModule": "ContactFlowModuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactFlowRequestRequestTypeDef = TypedDict(
    "DescribeContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

DescribeContactFlowResponseTypeDef = TypedDict(
    "DescribeContactFlowResponseTypeDef",
    {
        "ContactFlow": "ContactFlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactRequestRequestTypeDef = TypedDict(
    "DescribeContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
    },
)

DescribeContactResponseTypeDef = TypedDict(
    "DescribeContactResponseTypeDef",
    {
        "Contact": "ContactTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEvaluationFormRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEvaluationFormRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationFormId": str,
    },
)
_OptionalDescribeEvaluationFormRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEvaluationFormRequestRequestTypeDef",
    {
        "EvaluationFormVersion": int,
    },
    total=False,
)


class DescribeEvaluationFormRequestRequestTypeDef(
    _RequiredDescribeEvaluationFormRequestRequestTypeDef,
    _OptionalDescribeEvaluationFormRequestRequestTypeDef,
):
    pass


DescribeEvaluationFormResponseTypeDef = TypedDict(
    "DescribeEvaluationFormResponseTypeDef",
    {
        "EvaluationForm": "EvaluationFormTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHoursOfOperationRequestRequestTypeDef = TypedDict(
    "DescribeHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)

DescribeHoursOfOperationResponseTypeDef = TypedDict(
    "DescribeHoursOfOperationResponseTypeDef",
    {
        "HoursOfOperation": "HoursOfOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAttributeRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
    },
)

DescribeInstanceAttributeResponseTypeDef = TypedDict(
    "DescribeInstanceAttributeResponseTypeDef",
    {
        "Attribute": "AttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRequestRequestTypeDef = TypedDict(
    "DescribeInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeInstanceResponseTypeDef = TypedDict(
    "DescribeInstanceResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "DescribeInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DescribeInstanceStorageConfigResponseTypeDef = TypedDict(
    "DescribeInstanceStorageConfigResponseTypeDef",
    {
        "StorageConfig": "InstanceStorageConfigOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePhoneNumberRequestRequestTypeDef = TypedDict(
    "DescribePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

DescribePhoneNumberResponseTypeDef = TypedDict(
    "DescribePhoneNumberResponseTypeDef",
    {
        "ClaimedPhoneNumberSummary": "ClaimedPhoneNumberSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePromptRequestRequestTypeDef = TypedDict(
    "DescribePromptRequestRequestTypeDef",
    {
        "InstanceId": str,
        "PromptId": str,
    },
)

DescribePromptResponseTypeDef = TypedDict(
    "DescribePromptResponseTypeDef",
    {
        "Prompt": "PromptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueueRequestRequestTypeDef = TypedDict(
    "DescribeQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)

DescribeQueueResponseTypeDef = TypedDict(
    "DescribeQueueResponseTypeDef",
    {
        "Queue": "QueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuickConnectRequestRequestTypeDef = TypedDict(
    "DescribeQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DescribeQuickConnectResponseTypeDef = TypedDict(
    "DescribeQuickConnectResponseTypeDef",
    {
        "QuickConnect": "QuickConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoutingProfileRequestRequestTypeDef = TypedDict(
    "DescribeRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)

DescribeRoutingProfileResponseTypeDef = TypedDict(
    "DescribeRoutingProfileResponseTypeDef",
    {
        "RoutingProfile": "RoutingProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleRequestRequestTypeDef = TypedDict(
    "DescribeRuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RuleId": str,
    },
)

DescribeRuleResponseTypeDef = TypedDict(
    "DescribeRuleResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityProfileRequestRequestTypeDef = TypedDict(
    "DescribeSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
    },
)

DescribeSecurityProfileResponseTypeDef = TypedDict(
    "DescribeSecurityProfileResponseTypeDef",
    {
        "SecurityProfile": "SecurityProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficDistributionGroupRequestRequestTypeDef = TypedDict(
    "DescribeTrafficDistributionGroupRequestRequestTypeDef",
    {
        "TrafficDistributionGroupId": str,
    },
)

DescribeTrafficDistributionGroupResponseTypeDef = TypedDict(
    "DescribeTrafficDistributionGroupResponseTypeDef",
    {
        "TrafficDistributionGroup": "TrafficDistributionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "DescribeUserHierarchyGroupRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "DescribeUserHierarchyGroupResponseTypeDef",
    {
        "HierarchyGroup": "HierarchyGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyStructureRequestRequestTypeDef = TypedDict(
    "DescribeUserHierarchyStructureRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "DescribeUserHierarchyStructureResponseTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVocabularyRequestRequestTypeDef = TypedDict(
    "DescribeVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyId": str,
    },
)

DescribeVocabularyResponseTypeDef = TypedDict(
    "DescribeVocabularyResponseTypeDef",
    {
        "Vocabulary": "VocabularyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionsTypeDef = TypedDict(
    "DimensionsTypeDef",
    {
        "Queue": "QueueReferenceTypeDef",
        "Channel": ChannelType,
        "RoutingProfile": "RoutingProfileReferenceTypeDef",
    },
    total=False,
)

DisassociateApprovedOriginRequestRequestTypeDef = TypedDict(
    "DisassociateApprovedOriginRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

_RequiredDisassociateBotRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateBotRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDisassociateBotRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateBotRequestRequestTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)


class DisassociateBotRequestRequestTypeDef(
    _RequiredDisassociateBotRequestRequestTypeDef, _OptionalDisassociateBotRequestRequestTypeDef
):
    pass


DisassociateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "DisassociateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DisassociateLambdaFunctionRequestRequestTypeDef = TypedDict(
    "DisassociateLambdaFunctionRequestRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

DisassociateLexBotRequestRequestTypeDef = TypedDict(
    "DisassociateLexBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "BotName": str,
        "LexRegion": str,
    },
)

DisassociatePhoneNumberContactFlowRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumberContactFlowRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "InstanceId": str,
    },
)

DisassociateQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "DisassociateQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": Sequence[str],
    },
)

DisassociateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "DisassociateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueReferences": Sequence["RoutingProfileQueueReferenceTypeDef"],
    },
)

DisassociateSecurityKeyRequestRequestTypeDef = TypedDict(
    "DisassociateSecurityKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
    },
)

DismissUserContactRequestRequestTypeDef = TypedDict(
    "DismissUserContactRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
        "ContactId": str,
    },
)

DistributionOutputTypeDef = TypedDict(
    "DistributionOutputTypeDef",
    {
        "Region": str,
        "Percentage": int,
    },
)

DistributionTypeDef = TypedDict(
    "DistributionTypeDef",
    {
        "Region": str,
        "Percentage": int,
    },
)

EmailReferenceTypeDef = TypedDict(
    "EmailReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigOutputTypeDef = TypedDict(
    "EncryptionConfigOutputTypeDef",
    {
        "EncryptionType": Literal["KMS"],
        "KeyId": str,
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "EncryptionType": Literal["KMS"],
        "KeyId": str,
    },
)

EvaluationAnswerDataOutputTypeDef = TypedDict(
    "EvaluationAnswerDataOutputTypeDef",
    {
        "StringValue": str,
        "NumericValue": float,
        "NotApplicable": bool,
    },
    total=False,
)

EvaluationAnswerDataTypeDef = TypedDict(
    "EvaluationAnswerDataTypeDef",
    {
        "StringValue": str,
        "NumericValue": float,
        "NotApplicable": bool,
    },
    total=False,
)

EvaluationAnswerInputTypeDef = TypedDict(
    "EvaluationAnswerInputTypeDef",
    {
        "Value": "EvaluationAnswerDataTypeDef",
    },
    total=False,
)

EvaluationAnswerOutputTypeDef = TypedDict(
    "EvaluationAnswerOutputTypeDef",
    {
        "Value": "EvaluationAnswerDataOutputTypeDef",
        "SystemSuggestedValue": "EvaluationAnswerDataOutputTypeDef",
    },
    total=False,
)

_RequiredEvaluationFormContentTypeDef = TypedDict(
    "_RequiredEvaluationFormContentTypeDef",
    {
        "EvaluationFormVersion": int,
        "EvaluationFormId": str,
        "EvaluationFormArn": str,
        "Title": str,
        "Items": List["EvaluationFormItemOutputTypeDef"],
    },
)
_OptionalEvaluationFormContentTypeDef = TypedDict(
    "_OptionalEvaluationFormContentTypeDef",
    {
        "Description": str,
        "ScoringStrategy": "EvaluationFormScoringStrategyOutputTypeDef",
    },
    total=False,
)


class EvaluationFormContentTypeDef(
    _RequiredEvaluationFormContentTypeDef, _OptionalEvaluationFormContentTypeDef
):
    pass


EvaluationFormItemOutputTypeDef = TypedDict(
    "EvaluationFormItemOutputTypeDef",
    {
        "Section": Dict[str, Any],
        "Question": "EvaluationFormQuestionOutputTypeDef",
    },
    total=False,
)

EvaluationFormItemTypeDef = TypedDict(
    "EvaluationFormItemTypeDef",
    {
        "Section": Dict[str, Any],
        "Question": "EvaluationFormQuestionTypeDef",
    },
    total=False,
)

EvaluationFormNumericQuestionAutomationOutputTypeDef = TypedDict(
    "EvaluationFormNumericQuestionAutomationOutputTypeDef",
    {
        "PropertyValue": "NumericQuestionPropertyValueAutomationOutputTypeDef",
    },
    total=False,
)

EvaluationFormNumericQuestionAutomationTypeDef = TypedDict(
    "EvaluationFormNumericQuestionAutomationTypeDef",
    {
        "PropertyValue": "NumericQuestionPropertyValueAutomationTypeDef",
    },
    total=False,
)

_RequiredEvaluationFormNumericQuestionOptionOutputTypeDef = TypedDict(
    "_RequiredEvaluationFormNumericQuestionOptionOutputTypeDef",
    {
        "MinValue": int,
        "MaxValue": int,
    },
)
_OptionalEvaluationFormNumericQuestionOptionOutputTypeDef = TypedDict(
    "_OptionalEvaluationFormNumericQuestionOptionOutputTypeDef",
    {
        "Score": int,
        "AutomaticFail": bool,
    },
    total=False,
)


class EvaluationFormNumericQuestionOptionOutputTypeDef(
    _RequiredEvaluationFormNumericQuestionOptionOutputTypeDef,
    _OptionalEvaluationFormNumericQuestionOptionOutputTypeDef,
):
    pass


_RequiredEvaluationFormNumericQuestionOptionTypeDef = TypedDict(
    "_RequiredEvaluationFormNumericQuestionOptionTypeDef",
    {
        "MinValue": int,
        "MaxValue": int,
    },
)
_OptionalEvaluationFormNumericQuestionOptionTypeDef = TypedDict(
    "_OptionalEvaluationFormNumericQuestionOptionTypeDef",
    {
        "Score": int,
        "AutomaticFail": bool,
    },
    total=False,
)


class EvaluationFormNumericQuestionOptionTypeDef(
    _RequiredEvaluationFormNumericQuestionOptionTypeDef,
    _OptionalEvaluationFormNumericQuestionOptionTypeDef,
):
    pass


_RequiredEvaluationFormNumericQuestionPropertiesOutputTypeDef = TypedDict(
    "_RequiredEvaluationFormNumericQuestionPropertiesOutputTypeDef",
    {
        "MinValue": int,
        "MaxValue": int,
    },
)
_OptionalEvaluationFormNumericQuestionPropertiesOutputTypeDef = TypedDict(
    "_OptionalEvaluationFormNumericQuestionPropertiesOutputTypeDef",
    {
        "Options": List["EvaluationFormNumericQuestionOptionOutputTypeDef"],
        "Automation": "EvaluationFormNumericQuestionAutomationOutputTypeDef",
    },
    total=False,
)


class EvaluationFormNumericQuestionPropertiesOutputTypeDef(
    _RequiredEvaluationFormNumericQuestionPropertiesOutputTypeDef,
    _OptionalEvaluationFormNumericQuestionPropertiesOutputTypeDef,
):
    pass


_RequiredEvaluationFormNumericQuestionPropertiesTypeDef = TypedDict(
    "_RequiredEvaluationFormNumericQuestionPropertiesTypeDef",
    {
        "MinValue": int,
        "MaxValue": int,
    },
)
_OptionalEvaluationFormNumericQuestionPropertiesTypeDef = TypedDict(
    "_OptionalEvaluationFormNumericQuestionPropertiesTypeDef",
    {
        "Options": Sequence["EvaluationFormNumericQuestionOptionTypeDef"],
        "Automation": "EvaluationFormNumericQuestionAutomationTypeDef",
    },
    total=False,
)


class EvaluationFormNumericQuestionPropertiesTypeDef(
    _RequiredEvaluationFormNumericQuestionPropertiesTypeDef,
    _OptionalEvaluationFormNumericQuestionPropertiesTypeDef,
):
    pass


_RequiredEvaluationFormQuestionOutputTypeDef = TypedDict(
    "_RequiredEvaluationFormQuestionOutputTypeDef",
    {
        "Title": str,
        "RefId": str,
        "QuestionType": EvaluationFormQuestionTypeType,
    },
)
_OptionalEvaluationFormQuestionOutputTypeDef = TypedDict(
    "_OptionalEvaluationFormQuestionOutputTypeDef",
    {
        "Instructions": str,
        "NotApplicableEnabled": bool,
        "QuestionTypeProperties": "EvaluationFormQuestionTypePropertiesOutputTypeDef",
        "Weight": float,
    },
    total=False,
)


class EvaluationFormQuestionOutputTypeDef(
    _RequiredEvaluationFormQuestionOutputTypeDef, _OptionalEvaluationFormQuestionOutputTypeDef
):
    pass


_RequiredEvaluationFormQuestionTypeDef = TypedDict(
    "_RequiredEvaluationFormQuestionTypeDef",
    {
        "Title": str,
        "RefId": str,
        "QuestionType": EvaluationFormQuestionTypeType,
    },
)
_OptionalEvaluationFormQuestionTypeDef = TypedDict(
    "_OptionalEvaluationFormQuestionTypeDef",
    {
        "Instructions": str,
        "NotApplicableEnabled": bool,
        "QuestionTypeProperties": "EvaluationFormQuestionTypePropertiesTypeDef",
        "Weight": float,
    },
    total=False,
)


class EvaluationFormQuestionTypeDef(
    _RequiredEvaluationFormQuestionTypeDef, _OptionalEvaluationFormQuestionTypeDef
):
    pass


EvaluationFormQuestionTypePropertiesOutputTypeDef = TypedDict(
    "EvaluationFormQuestionTypePropertiesOutputTypeDef",
    {
        "Numeric": "EvaluationFormNumericQuestionPropertiesOutputTypeDef",
        "SingleSelect": "EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef",
    },
    total=False,
)

EvaluationFormQuestionTypePropertiesTypeDef = TypedDict(
    "EvaluationFormQuestionTypePropertiesTypeDef",
    {
        "Numeric": "EvaluationFormNumericQuestionPropertiesTypeDef",
        "SingleSelect": "EvaluationFormSingleSelectQuestionPropertiesTypeDef",
    },
    total=False,
)

EvaluationFormScoringStrategyOutputTypeDef = TypedDict(
    "EvaluationFormScoringStrategyOutputTypeDef",
    {
        "Mode": EvaluationFormScoringModeType,
        "Status": EvaluationFormScoringStatusType,
    },
)

EvaluationFormScoringStrategyTypeDef = TypedDict(
    "EvaluationFormScoringStrategyTypeDef",
    {
        "Mode": EvaluationFormScoringModeType,
        "Status": EvaluationFormScoringStatusType,
    },
)

_RequiredEvaluationFormSectionOutputTypeDef = TypedDict(
    "_RequiredEvaluationFormSectionOutputTypeDef",
    {
        "Title": str,
        "RefId": str,
        "Items": List[Dict[str, Any]],
    },
)
_OptionalEvaluationFormSectionOutputTypeDef = TypedDict(
    "_OptionalEvaluationFormSectionOutputTypeDef",
    {
        "Instructions": str,
        "Weight": float,
    },
    total=False,
)


class EvaluationFormSectionOutputTypeDef(
    _RequiredEvaluationFormSectionOutputTypeDef, _OptionalEvaluationFormSectionOutputTypeDef
):
    pass


_RequiredEvaluationFormSectionTypeDef = TypedDict(
    "_RequiredEvaluationFormSectionTypeDef",
    {
        "Title": str,
        "RefId": str,
        "Items": Sequence[Dict[str, Any]],
    },
)
_OptionalEvaluationFormSectionTypeDef = TypedDict(
    "_OptionalEvaluationFormSectionTypeDef",
    {
        "Instructions": str,
        "Weight": float,
    },
    total=False,
)


class EvaluationFormSectionTypeDef(
    _RequiredEvaluationFormSectionTypeDef, _OptionalEvaluationFormSectionTypeDef
):
    pass


EvaluationFormSingleSelectQuestionAutomationOptionOutputTypeDef = TypedDict(
    "EvaluationFormSingleSelectQuestionAutomationOptionOutputTypeDef",
    {
        "RuleCategory": "SingleSelectQuestionRuleCategoryAutomationOutputTypeDef",
    },
    total=False,
)

EvaluationFormSingleSelectQuestionAutomationOptionTypeDef = TypedDict(
    "EvaluationFormSingleSelectQuestionAutomationOptionTypeDef",
    {
        "RuleCategory": "SingleSelectQuestionRuleCategoryAutomationTypeDef",
    },
    total=False,
)

_RequiredEvaluationFormSingleSelectQuestionAutomationOutputTypeDef = TypedDict(
    "_RequiredEvaluationFormSingleSelectQuestionAutomationOutputTypeDef",
    {
        "Options": List["EvaluationFormSingleSelectQuestionAutomationOptionOutputTypeDef"],
    },
)
_OptionalEvaluationFormSingleSelectQuestionAutomationOutputTypeDef = TypedDict(
    "_OptionalEvaluationFormSingleSelectQuestionAutomationOutputTypeDef",
    {
        "DefaultOptionRefId": str,
    },
    total=False,
)


class EvaluationFormSingleSelectQuestionAutomationOutputTypeDef(
    _RequiredEvaluationFormSingleSelectQuestionAutomationOutputTypeDef,
    _OptionalEvaluationFormSingleSelectQuestionAutomationOutputTypeDef,
):
    pass


_RequiredEvaluationFormSingleSelectQuestionAutomationTypeDef = TypedDict(
    "_RequiredEvaluationFormSingleSelectQuestionAutomationTypeDef",
    {
        "Options": Sequence["EvaluationFormSingleSelectQuestionAutomationOptionTypeDef"],
    },
)
_OptionalEvaluationFormSingleSelectQuestionAutomationTypeDef = TypedDict(
    "_OptionalEvaluationFormSingleSelectQuestionAutomationTypeDef",
    {
        "DefaultOptionRefId": str,
    },
    total=False,
)


class EvaluationFormSingleSelectQuestionAutomationTypeDef(
    _RequiredEvaluationFormSingleSelectQuestionAutomationTypeDef,
    _OptionalEvaluationFormSingleSelectQuestionAutomationTypeDef,
):
    pass


_RequiredEvaluationFormSingleSelectQuestionOptionOutputTypeDef = TypedDict(
    "_RequiredEvaluationFormSingleSelectQuestionOptionOutputTypeDef",
    {
        "RefId": str,
        "Text": str,
    },
)
_OptionalEvaluationFormSingleSelectQuestionOptionOutputTypeDef = TypedDict(
    "_OptionalEvaluationFormSingleSelectQuestionOptionOutputTypeDef",
    {
        "Score": int,
        "AutomaticFail": bool,
    },
    total=False,
)


class EvaluationFormSingleSelectQuestionOptionOutputTypeDef(
    _RequiredEvaluationFormSingleSelectQuestionOptionOutputTypeDef,
    _OptionalEvaluationFormSingleSelectQuestionOptionOutputTypeDef,
):
    pass


_RequiredEvaluationFormSingleSelectQuestionOptionTypeDef = TypedDict(
    "_RequiredEvaluationFormSingleSelectQuestionOptionTypeDef",
    {
        "RefId": str,
        "Text": str,
    },
)
_OptionalEvaluationFormSingleSelectQuestionOptionTypeDef = TypedDict(
    "_OptionalEvaluationFormSingleSelectQuestionOptionTypeDef",
    {
        "Score": int,
        "AutomaticFail": bool,
    },
    total=False,
)


class EvaluationFormSingleSelectQuestionOptionTypeDef(
    _RequiredEvaluationFormSingleSelectQuestionOptionTypeDef,
    _OptionalEvaluationFormSingleSelectQuestionOptionTypeDef,
):
    pass


_RequiredEvaluationFormSingleSelectQuestionPropertiesOutputTypeDef = TypedDict(
    "_RequiredEvaluationFormSingleSelectQuestionPropertiesOutputTypeDef",
    {
        "Options": List["EvaluationFormSingleSelectQuestionOptionOutputTypeDef"],
    },
)
_OptionalEvaluationFormSingleSelectQuestionPropertiesOutputTypeDef = TypedDict(
    "_OptionalEvaluationFormSingleSelectQuestionPropertiesOutputTypeDef",
    {
        "DisplayAs": EvaluationFormSingleSelectQuestionDisplayModeType,
        "Automation": "EvaluationFormSingleSelectQuestionAutomationOutputTypeDef",
    },
    total=False,
)


class EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef(
    _RequiredEvaluationFormSingleSelectQuestionPropertiesOutputTypeDef,
    _OptionalEvaluationFormSingleSelectQuestionPropertiesOutputTypeDef,
):
    pass


_RequiredEvaluationFormSingleSelectQuestionPropertiesTypeDef = TypedDict(
    "_RequiredEvaluationFormSingleSelectQuestionPropertiesTypeDef",
    {
        "Options": Sequence["EvaluationFormSingleSelectQuestionOptionTypeDef"],
    },
)
_OptionalEvaluationFormSingleSelectQuestionPropertiesTypeDef = TypedDict(
    "_OptionalEvaluationFormSingleSelectQuestionPropertiesTypeDef",
    {
        "DisplayAs": EvaluationFormSingleSelectQuestionDisplayModeType,
        "Automation": "EvaluationFormSingleSelectQuestionAutomationTypeDef",
    },
    total=False,
)


class EvaluationFormSingleSelectQuestionPropertiesTypeDef(
    _RequiredEvaluationFormSingleSelectQuestionPropertiesTypeDef,
    _OptionalEvaluationFormSingleSelectQuestionPropertiesTypeDef,
):
    pass


_RequiredEvaluationFormSummaryTypeDef = TypedDict(
    "_RequiredEvaluationFormSummaryTypeDef",
    {
        "EvaluationFormId": str,
        "EvaluationFormArn": str,
        "Title": str,
        "CreatedTime": datetime,
        "CreatedBy": str,
        "LastModifiedTime": datetime,
        "LastModifiedBy": str,
        "LatestVersion": int,
    },
)
_OptionalEvaluationFormSummaryTypeDef = TypedDict(
    "_OptionalEvaluationFormSummaryTypeDef",
    {
        "LastActivatedTime": datetime,
        "LastActivatedBy": str,
        "ActiveVersion": int,
    },
    total=False,
)


class EvaluationFormSummaryTypeDef(
    _RequiredEvaluationFormSummaryTypeDef, _OptionalEvaluationFormSummaryTypeDef
):
    pass


_RequiredEvaluationFormTypeDef = TypedDict(
    "_RequiredEvaluationFormTypeDef",
    {
        "EvaluationFormId": str,
        "EvaluationFormVersion": int,
        "Locked": bool,
        "EvaluationFormArn": str,
        "Title": str,
        "Status": EvaluationFormVersionStatusType,
        "Items": List["EvaluationFormItemOutputTypeDef"],
        "CreatedTime": datetime,
        "CreatedBy": str,
        "LastModifiedTime": datetime,
        "LastModifiedBy": str,
    },
)
_OptionalEvaluationFormTypeDef = TypedDict(
    "_OptionalEvaluationFormTypeDef",
    {
        "Description": str,
        "ScoringStrategy": "EvaluationFormScoringStrategyOutputTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class EvaluationFormTypeDef(_RequiredEvaluationFormTypeDef, _OptionalEvaluationFormTypeDef):
    pass


EvaluationFormVersionSummaryTypeDef = TypedDict(
    "EvaluationFormVersionSummaryTypeDef",
    {
        "EvaluationFormArn": str,
        "EvaluationFormId": str,
        "EvaluationFormVersion": int,
        "Locked": bool,
        "Status": EvaluationFormVersionStatusType,
        "CreatedTime": datetime,
        "CreatedBy": str,
        "LastModifiedTime": datetime,
        "LastModifiedBy": str,
    },
)

_RequiredEvaluationMetadataTypeDef = TypedDict(
    "_RequiredEvaluationMetadataTypeDef",
    {
        "ContactId": str,
        "EvaluatorArn": str,
    },
)
_OptionalEvaluationMetadataTypeDef = TypedDict(
    "_OptionalEvaluationMetadataTypeDef",
    {
        "ContactAgentId": str,
        "Score": "EvaluationScoreTypeDef",
    },
    total=False,
)


class EvaluationMetadataTypeDef(
    _RequiredEvaluationMetadataTypeDef, _OptionalEvaluationMetadataTypeDef
):
    pass


EvaluationNoteOutputTypeDef = TypedDict(
    "EvaluationNoteOutputTypeDef",
    {
        "Value": str,
    },
    total=False,
)

EvaluationNoteTypeDef = TypedDict(
    "EvaluationNoteTypeDef",
    {
        "Value": str,
    },
    total=False,
)

EvaluationScoreTypeDef = TypedDict(
    "EvaluationScoreTypeDef",
    {
        "Percentage": float,
        "NotApplicable": bool,
        "AutomaticFail": bool,
    },
    total=False,
)

_RequiredEvaluationSummaryTypeDef = TypedDict(
    "_RequiredEvaluationSummaryTypeDef",
    {
        "EvaluationId": str,
        "EvaluationArn": str,
        "EvaluationFormTitle": str,
        "EvaluationFormId": str,
        "Status": EvaluationStatusType,
        "EvaluatorArn": str,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalEvaluationSummaryTypeDef = TypedDict(
    "_OptionalEvaluationSummaryTypeDef",
    {
        "Score": "EvaluationScoreTypeDef",
    },
    total=False,
)


class EvaluationSummaryTypeDef(
    _RequiredEvaluationSummaryTypeDef, _OptionalEvaluationSummaryTypeDef
):
    pass


_RequiredEvaluationTypeDef = TypedDict(
    "_RequiredEvaluationTypeDef",
    {
        "EvaluationId": str,
        "EvaluationArn": str,
        "Metadata": "EvaluationMetadataTypeDef",
        "Answers": Dict[str, "EvaluationAnswerOutputTypeDef"],
        "Notes": Dict[str, "EvaluationNoteOutputTypeDef"],
        "Status": EvaluationStatusType,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalEvaluationTypeDef = TypedDict(
    "_OptionalEvaluationTypeDef",
    {
        "Scores": Dict[str, "EvaluationScoreTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)


class EvaluationTypeDef(_RequiredEvaluationTypeDef, _OptionalEvaluationTypeDef):
    pass


EventBridgeActionDefinitionOutputTypeDef = TypedDict(
    "EventBridgeActionDefinitionOutputTypeDef",
    {
        "Name": str,
    },
)

EventBridgeActionDefinitionTypeDef = TypedDict(
    "EventBridgeActionDefinitionTypeDef",
    {
        "Name": str,
    },
)

FilterV2TypeDef = TypedDict(
    "FilterV2TypeDef",
    {
        "FilterKey": str,
        "FilterValues": Sequence[str],
    },
    total=False,
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "Queues": Sequence[str],
        "Channels": Sequence[ChannelType],
        "RoutingProfiles": Sequence[str],
    },
    total=False,
)

GetContactAttributesRequestRequestTypeDef = TypedDict(
    "GetContactAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InitialContactId": str,
    },
)

GetContactAttributesResponseTypeDef = TypedDict(
    "GetContactAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCurrentMetricDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetCurrentMetricDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": "FiltersTypeDef",
        "CurrentMetrics": Sequence["CurrentMetricTypeDef"],
    },
)
_OptionalGetCurrentMetricDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetCurrentMetricDataRequestRequestTypeDef",
    {
        "Groupings": Sequence[GroupingType],
        "NextToken": str,
        "MaxResults": int,
        "SortCriteria": Sequence["CurrentMetricSortCriteriaTypeDef"],
    },
    total=False,
)


class GetCurrentMetricDataRequestRequestTypeDef(
    _RequiredGetCurrentMetricDataRequestRequestTypeDef,
    _OptionalGetCurrentMetricDataRequestRequestTypeDef,
):
    pass


GetCurrentMetricDataResponseTypeDef = TypedDict(
    "GetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["CurrentMetricResultTypeDef"],
        "DataSnapshotTime": datetime,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCurrentUserDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetCurrentUserDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": "UserDataFiltersTypeDef",
    },
)
_OptionalGetCurrentUserDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetCurrentUserDataRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetCurrentUserDataRequestRequestTypeDef(
    _RequiredGetCurrentUserDataRequestRequestTypeDef,
    _OptionalGetCurrentUserDataRequestRequestTypeDef,
):
    pass


GetCurrentUserDataResponseTypeDef = TypedDict(
    "GetCurrentUserDataResponseTypeDef",
    {
        "NextToken": str,
        "UserDataList": List["UserDataTypeDef"],
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFederationTokenRequestRequestTypeDef = TypedDict(
    "GetFederationTokenRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "SignInUrl": str,
        "UserArn": str,
        "UserId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricDataRequestGetMetricDataPaginateTypeDef = TypedDict(
    "_RequiredGetMetricDataRequestGetMetricDataPaginateTypeDef",
    {
        "InstanceId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Filters": "FiltersTypeDef",
        "HistoricalMetrics": Sequence["HistoricalMetricTypeDef"],
    },
)
_OptionalGetMetricDataRequestGetMetricDataPaginateTypeDef = TypedDict(
    "_OptionalGetMetricDataRequestGetMetricDataPaginateTypeDef",
    {
        "Groupings": Sequence[GroupingType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class GetMetricDataRequestGetMetricDataPaginateTypeDef(
    _RequiredGetMetricDataRequestGetMetricDataPaginateTypeDef,
    _OptionalGetMetricDataRequestGetMetricDataPaginateTypeDef,
):
    pass


_RequiredGetMetricDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetMetricDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Filters": "FiltersTypeDef",
        "HistoricalMetrics": Sequence["HistoricalMetricTypeDef"],
    },
)
_OptionalGetMetricDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetMetricDataRequestRequestTypeDef",
    {
        "Groupings": Sequence[GroupingType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetMetricDataRequestRequestTypeDef(
    _RequiredGetMetricDataRequestRequestTypeDef, _OptionalGetMetricDataRequestRequestTypeDef
):
    pass


GetMetricDataResponseTypeDef = TypedDict(
    "GetMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["HistoricalMetricResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricDataV2RequestRequestTypeDef = TypedDict(
    "_RequiredGetMetricDataV2RequestRequestTypeDef",
    {
        "ResourceArn": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Filters": Sequence["FilterV2TypeDef"],
        "Metrics": Sequence["MetricV2TypeDef"],
    },
)
_OptionalGetMetricDataV2RequestRequestTypeDef = TypedDict(
    "_OptionalGetMetricDataV2RequestRequestTypeDef",
    {
        "Groupings": Sequence[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetMetricDataV2RequestRequestTypeDef(
    _RequiredGetMetricDataV2RequestRequestTypeDef, _OptionalGetMetricDataV2RequestRequestTypeDef
):
    pass


GetMetricDataV2ResponseTypeDef = TypedDict(
    "GetMetricDataV2ResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["MetricResultV2TypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPromptFileRequestRequestTypeDef = TypedDict(
    "GetPromptFileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "PromptId": str,
    },
)

GetPromptFileResponseTypeDef = TypedDict(
    "GetPromptFileResponseTypeDef",
    {
        "PromptPresignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTaskTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredGetTaskTemplateRequestRequestTypeDef",
    {
        "InstanceId": str,
        "TaskTemplateId": str,
    },
)
_OptionalGetTaskTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalGetTaskTemplateRequestRequestTypeDef",
    {
        "SnapshotVersion": str,
    },
    total=False,
)


class GetTaskTemplateRequestRequestTypeDef(
    _RequiredGetTaskTemplateRequestRequestTypeDef, _OptionalGetTaskTemplateRequestRequestTypeDef
):
    pass


GetTaskTemplateResponseTypeDef = TypedDict(
    "GetTaskTemplateResponseTypeDef",
    {
        "InstanceId": str,
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "ContactFlowId": str,
        "Constraints": "TaskTemplateConstraintsOutputTypeDef",
        "Defaults": "TaskTemplateDefaultsOutputTypeDef",
        "Fields": List["TaskTemplateFieldOutputTypeDef"],
        "Status": TaskTemplateStatusType,
        "LastModifiedTime": datetime,
        "CreatedTime": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficDistributionRequestRequestTypeDef = TypedDict(
    "GetTrafficDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetTrafficDistributionResponseTypeDef = TypedDict(
    "GetTrafficDistributionResponseTypeDef",
    {
        "TelephonyConfig": "TelephonyConfigOutputTypeDef",
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HierarchyGroupConditionTypeDef = TypedDict(
    "HierarchyGroupConditionTypeDef",
    {
        "Value": str,
        "HierarchyGroupMatchType": HierarchyGroupMatchTypeType,
    },
    total=False,
)

HierarchyGroupSummaryReferenceTypeDef = TypedDict(
    "HierarchyGroupSummaryReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

HierarchyGroupSummaryTypeDef = TypedDict(
    "HierarchyGroupSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HierarchyGroupTypeDef = TypedDict(
    "HierarchyGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "LevelId": str,
        "HierarchyPath": "HierarchyPathTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

HierarchyLevelTypeDef = TypedDict(
    "HierarchyLevelTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HierarchyLevelUpdateTypeDef = TypedDict(
    "HierarchyLevelUpdateTypeDef",
    {
        "Name": str,
    },
)

HierarchyPathReferenceTypeDef = TypedDict(
    "HierarchyPathReferenceTypeDef",
    {
        "LevelOne": "HierarchyGroupSummaryReferenceTypeDef",
        "LevelTwo": "HierarchyGroupSummaryReferenceTypeDef",
        "LevelThree": "HierarchyGroupSummaryReferenceTypeDef",
        "LevelFour": "HierarchyGroupSummaryReferenceTypeDef",
        "LevelFive": "HierarchyGroupSummaryReferenceTypeDef",
    },
    total=False,
)

HierarchyPathTypeDef = TypedDict(
    "HierarchyPathTypeDef",
    {
        "LevelOne": "HierarchyGroupSummaryTypeDef",
        "LevelTwo": "HierarchyGroupSummaryTypeDef",
        "LevelThree": "HierarchyGroupSummaryTypeDef",
        "LevelFour": "HierarchyGroupSummaryTypeDef",
        "LevelFive": "HierarchyGroupSummaryTypeDef",
    },
    total=False,
)

HierarchyStructureTypeDef = TypedDict(
    "HierarchyStructureTypeDef",
    {
        "LevelOne": "HierarchyLevelTypeDef",
        "LevelTwo": "HierarchyLevelTypeDef",
        "LevelThree": "HierarchyLevelTypeDef",
        "LevelFour": "HierarchyLevelTypeDef",
        "LevelFive": "HierarchyLevelTypeDef",
    },
    total=False,
)

HierarchyStructureUpdateTypeDef = TypedDict(
    "HierarchyStructureUpdateTypeDef",
    {
        "LevelOne": "HierarchyLevelUpdateTypeDef",
        "LevelTwo": "HierarchyLevelUpdateTypeDef",
        "LevelThree": "HierarchyLevelUpdateTypeDef",
        "LevelFour": "HierarchyLevelUpdateTypeDef",
        "LevelFive": "HierarchyLevelUpdateTypeDef",
    },
    total=False,
)

HistoricalMetricDataTypeDef = TypedDict(
    "HistoricalMetricDataTypeDef",
    {
        "Metric": "HistoricalMetricOutputTypeDef",
        "Value": float,
    },
    total=False,
)

HistoricalMetricOutputTypeDef = TypedDict(
    "HistoricalMetricOutputTypeDef",
    {
        "Name": HistoricalMetricNameType,
        "Threshold": "ThresholdOutputTypeDef",
        "Statistic": StatisticType,
        "Unit": UnitType,
    },
    total=False,
)

HistoricalMetricResultTypeDef = TypedDict(
    "HistoricalMetricResultTypeDef",
    {
        "Dimensions": "DimensionsTypeDef",
        "Collections": List["HistoricalMetricDataTypeDef"],
    },
    total=False,
)

HistoricalMetricTypeDef = TypedDict(
    "HistoricalMetricTypeDef",
    {
        "Name": HistoricalMetricNameType,
        "Threshold": "ThresholdTypeDef",
        "Statistic": StatisticType,
        "Unit": UnitType,
    },
    total=False,
)

HoursOfOperationConfigOutputTypeDef = TypedDict(
    "HoursOfOperationConfigOutputTypeDef",
    {
        "Day": HoursOfOperationDaysType,
        "StartTime": "HoursOfOperationTimeSliceOutputTypeDef",
        "EndTime": "HoursOfOperationTimeSliceOutputTypeDef",
    },
)

HoursOfOperationConfigTypeDef = TypedDict(
    "HoursOfOperationConfigTypeDef",
    {
        "Day": HoursOfOperationDaysType,
        "StartTime": "HoursOfOperationTimeSliceTypeDef",
        "EndTime": "HoursOfOperationTimeSliceTypeDef",
    },
)

HoursOfOperationSearchCriteriaTypeDef = TypedDict(
    "HoursOfOperationSearchCriteriaTypeDef",
    {
        "OrConditions": Sequence[Dict[str, Any]],
        "AndConditions": Sequence[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
    },
    total=False,
)

HoursOfOperationSearchFilterTypeDef = TypedDict(
    "HoursOfOperationSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

HoursOfOperationSummaryTypeDef = TypedDict(
    "HoursOfOperationSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HoursOfOperationTimeSliceOutputTypeDef = TypedDict(
    "HoursOfOperationTimeSliceOutputTypeDef",
    {
        "Hours": int,
        "Minutes": int,
    },
)

HoursOfOperationTimeSliceTypeDef = TypedDict(
    "HoursOfOperationTimeSliceTypeDef",
    {
        "Hours": int,
        "Minutes": int,
    },
)

HoursOfOperationTypeDef = TypedDict(
    "HoursOfOperationTypeDef",
    {
        "HoursOfOperationId": str,
        "HoursOfOperationArn": str,
        "Name": str,
        "Description": str,
        "TimeZone": str,
        "Config": List["HoursOfOperationConfigOutputTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

InstanceStatusReasonTypeDef = TypedDict(
    "InstanceStatusReasonTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredInstanceStorageConfigOutputTypeDef = TypedDict(
    "_RequiredInstanceStorageConfigOutputTypeDef",
    {
        "StorageType": StorageTypeType,
    },
)
_OptionalInstanceStorageConfigOutputTypeDef = TypedDict(
    "_OptionalInstanceStorageConfigOutputTypeDef",
    {
        "AssociationId": str,
        "S3Config": "S3ConfigOutputTypeDef",
        "KinesisVideoStreamConfig": "KinesisVideoStreamConfigOutputTypeDef",
        "KinesisStreamConfig": "KinesisStreamConfigOutputTypeDef",
        "KinesisFirehoseConfig": "KinesisFirehoseConfigOutputTypeDef",
    },
    total=False,
)


class InstanceStorageConfigOutputTypeDef(
    _RequiredInstanceStorageConfigOutputTypeDef, _OptionalInstanceStorageConfigOutputTypeDef
):
    pass


_RequiredInstanceStorageConfigTypeDef = TypedDict(
    "_RequiredInstanceStorageConfigTypeDef",
    {
        "StorageType": StorageTypeType,
    },
)
_OptionalInstanceStorageConfigTypeDef = TypedDict(
    "_OptionalInstanceStorageConfigTypeDef",
    {
        "AssociationId": str,
        "S3Config": "S3ConfigTypeDef",
        "KinesisVideoStreamConfig": "KinesisVideoStreamConfigTypeDef",
        "KinesisStreamConfig": "KinesisStreamConfigTypeDef",
        "KinesisFirehoseConfig": "KinesisFirehoseConfigTypeDef",
    },
    total=False,
)


class InstanceStorageConfigTypeDef(
    _RequiredInstanceStorageConfigTypeDef, _OptionalInstanceStorageConfigTypeDef
):
    pass


InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryTypeType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatusType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
        "InstanceAccessUrl": str,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryTypeType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatusType,
        "StatusReason": "InstanceStatusReasonTypeDef",
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
        "InstanceAccessUrl": str,
    },
    total=False,
)

IntegrationAssociationSummaryTypeDef = TypedDict(
    "IntegrationAssociationSummaryTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "InstanceId": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationArn": str,
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceTypeType,
    },
    total=False,
)

InvisibleFieldInfoOutputTypeDef = TypedDict(
    "InvisibleFieldInfoOutputTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierOutputTypeDef",
    },
    total=False,
)

InvisibleFieldInfoTypeDef = TypedDict(
    "InvisibleFieldInfoTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
    },
    total=False,
)

KinesisFirehoseConfigOutputTypeDef = TypedDict(
    "KinesisFirehoseConfigOutputTypeDef",
    {
        "FirehoseArn": str,
    },
)

KinesisFirehoseConfigTypeDef = TypedDict(
    "KinesisFirehoseConfigTypeDef",
    {
        "FirehoseArn": str,
    },
)

KinesisStreamConfigOutputTypeDef = TypedDict(
    "KinesisStreamConfigOutputTypeDef",
    {
        "StreamArn": str,
    },
)

KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "StreamArn": str,
    },
)

KinesisVideoStreamConfigOutputTypeDef = TypedDict(
    "KinesisVideoStreamConfigOutputTypeDef",
    {
        "Prefix": str,
        "RetentionPeriodHours": int,
        "EncryptionConfig": "EncryptionConfigOutputTypeDef",
    },
)

KinesisVideoStreamConfigTypeDef = TypedDict(
    "KinesisVideoStreamConfigTypeDef",
    {
        "Prefix": str,
        "RetentionPeriodHours": int,
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
)

LexBotConfigTypeDef = TypedDict(
    "LexBotConfigTypeDef",
    {
        "LexBot": "LexBotOutputTypeDef",
        "LexV2Bot": "LexV2BotOutputTypeDef",
    },
    total=False,
)

LexBotOutputTypeDef = TypedDict(
    "LexBotOutputTypeDef",
    {
        "Name": str,
        "LexRegion": str,
    },
)

LexBotTypeDef = TypedDict(
    "LexBotTypeDef",
    {
        "Name": str,
        "LexRegion": str,
    },
)

LexV2BotOutputTypeDef = TypedDict(
    "LexV2BotOutputTypeDef",
    {
        "AliasArn": str,
    },
    total=False,
)

LexV2BotTypeDef = TypedDict(
    "LexV2BotTypeDef",
    {
        "AliasArn": str,
    },
    total=False,
)

_RequiredListAgentStatusRequestListAgentStatusesPaginateTypeDef = TypedDict(
    "_RequiredListAgentStatusRequestListAgentStatusesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListAgentStatusRequestListAgentStatusesPaginateTypeDef = TypedDict(
    "_OptionalListAgentStatusRequestListAgentStatusesPaginateTypeDef",
    {
        "AgentStatusTypes": Sequence[AgentStatusTypeType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListAgentStatusRequestListAgentStatusesPaginateTypeDef(
    _RequiredListAgentStatusRequestListAgentStatusesPaginateTypeDef,
    _OptionalListAgentStatusRequestListAgentStatusesPaginateTypeDef,
):
    pass


_RequiredListAgentStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListAgentStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListAgentStatusRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "AgentStatusTypes": Sequence[AgentStatusTypeType],
    },
    total=False,
)


class ListAgentStatusRequestRequestTypeDef(
    _RequiredListAgentStatusRequestRequestTypeDef, _OptionalListAgentStatusRequestRequestTypeDef
):
    pass


ListAgentStatusResponseTypeDef = TypedDict(
    "ListAgentStatusResponseTypeDef",
    {
        "NextToken": str,
        "AgentStatusSummaryList": List["AgentStatusSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef = TypedDict(
    "_RequiredListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef = TypedDict(
    "_OptionalListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef(
    _RequiredListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef,
    _OptionalListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef,
):
    pass


_RequiredListApprovedOriginsRequestRequestTypeDef = TypedDict(
    "_RequiredListApprovedOriginsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListApprovedOriginsRequestRequestTypeDef = TypedDict(
    "_OptionalListApprovedOriginsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListApprovedOriginsRequestRequestTypeDef(
    _RequiredListApprovedOriginsRequestRequestTypeDef,
    _OptionalListApprovedOriginsRequestRequestTypeDef,
):
    pass


ListApprovedOriginsResponseTypeDef = TypedDict(
    "ListApprovedOriginsResponseTypeDef",
    {
        "Origins": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotsRequestListBotsPaginateTypeDef = TypedDict(
    "_RequiredListBotsRequestListBotsPaginateTypeDef",
    {
        "InstanceId": str,
        "LexVersion": LexVersionType,
    },
)
_OptionalListBotsRequestListBotsPaginateTypeDef = TypedDict(
    "_OptionalListBotsRequestListBotsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListBotsRequestListBotsPaginateTypeDef(
    _RequiredListBotsRequestListBotsPaginateTypeDef, _OptionalListBotsRequestListBotsPaginateTypeDef
):
    pass


_RequiredListBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListBotsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexVersion": LexVersionType,
    },
)
_OptionalListBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListBotsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListBotsRequestRequestTypeDef(
    _RequiredListBotsRequestRequestTypeDef, _OptionalListBotsRequestRequestTypeDef
):
    pass


ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "LexBots": List["LexBotConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef = TypedDict(
    "_RequiredListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
    },
)
_OptionalListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef = TypedDict(
    "_OptionalListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef(
    _RequiredListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef,
    _OptionalListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef,
):
    pass


_RequiredListContactEvaluationsRequestRequestTypeDef = TypedDict(
    "_RequiredListContactEvaluationsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
    },
)
_OptionalListContactEvaluationsRequestRequestTypeDef = TypedDict(
    "_OptionalListContactEvaluationsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListContactEvaluationsRequestRequestTypeDef(
    _RequiredListContactEvaluationsRequestRequestTypeDef,
    _OptionalListContactEvaluationsRequestRequestTypeDef,
):
    pass


ListContactEvaluationsResponseTypeDef = TypedDict(
    "ListContactEvaluationsResponseTypeDef",
    {
        "EvaluationSummaryList": List["EvaluationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef = TypedDict(
    "_RequiredListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef = TypedDict(
    "_OptionalListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef",
    {
        "ContactFlowModuleState": ContactFlowModuleStateType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef(
    _RequiredListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef,
    _OptionalListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef,
):
    pass


_RequiredListContactFlowModulesRequestRequestTypeDef = TypedDict(
    "_RequiredListContactFlowModulesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListContactFlowModulesRequestRequestTypeDef = TypedDict(
    "_OptionalListContactFlowModulesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ContactFlowModuleState": ContactFlowModuleStateType,
    },
    total=False,
)


class ListContactFlowModulesRequestRequestTypeDef(
    _RequiredListContactFlowModulesRequestRequestTypeDef,
    _OptionalListContactFlowModulesRequestRequestTypeDef,
):
    pass


ListContactFlowModulesResponseTypeDef = TypedDict(
    "ListContactFlowModulesResponseTypeDef",
    {
        "ContactFlowModulesSummaryList": List["ContactFlowModuleSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactFlowsRequestListContactFlowsPaginateTypeDef = TypedDict(
    "_RequiredListContactFlowsRequestListContactFlowsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListContactFlowsRequestListContactFlowsPaginateTypeDef = TypedDict(
    "_OptionalListContactFlowsRequestListContactFlowsPaginateTypeDef",
    {
        "ContactFlowTypes": Sequence[ContactFlowTypeType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListContactFlowsRequestListContactFlowsPaginateTypeDef(
    _RequiredListContactFlowsRequestListContactFlowsPaginateTypeDef,
    _OptionalListContactFlowsRequestListContactFlowsPaginateTypeDef,
):
    pass


_RequiredListContactFlowsRequestRequestTypeDef = TypedDict(
    "_RequiredListContactFlowsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListContactFlowsRequestRequestTypeDef = TypedDict(
    "_OptionalListContactFlowsRequestRequestTypeDef",
    {
        "ContactFlowTypes": Sequence[ContactFlowTypeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListContactFlowsRequestRequestTypeDef(
    _RequiredListContactFlowsRequestRequestTypeDef, _OptionalListContactFlowsRequestRequestTypeDef
):
    pass


ListContactFlowsResponseTypeDef = TypedDict(
    "ListContactFlowsResponseTypeDef",
    {
        "ContactFlowSummaryList": List["ContactFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactReferencesRequestListContactReferencesPaginateTypeDef = TypedDict(
    "_RequiredListContactReferencesRequestListContactReferencesPaginateTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ReferenceTypes": Sequence[ReferenceTypeType],
    },
)
_OptionalListContactReferencesRequestListContactReferencesPaginateTypeDef = TypedDict(
    "_OptionalListContactReferencesRequestListContactReferencesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListContactReferencesRequestListContactReferencesPaginateTypeDef(
    _RequiredListContactReferencesRequestListContactReferencesPaginateTypeDef,
    _OptionalListContactReferencesRequestListContactReferencesPaginateTypeDef,
):
    pass


_RequiredListContactReferencesRequestRequestTypeDef = TypedDict(
    "_RequiredListContactReferencesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ReferenceTypes": Sequence[ReferenceTypeType],
    },
)
_OptionalListContactReferencesRequestRequestTypeDef = TypedDict(
    "_OptionalListContactReferencesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListContactReferencesRequestRequestTypeDef(
    _RequiredListContactReferencesRequestRequestTypeDef,
    _OptionalListContactReferencesRequestRequestTypeDef,
):
    pass


ListContactReferencesResponseTypeDef = TypedDict(
    "ListContactReferencesResponseTypeDef",
    {
        "ReferenceSummaryList": List["ReferenceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef = TypedDict(
    "_RequiredListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef = TypedDict(
    "_OptionalListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef",
    {
        "LanguageCode": VocabularyLanguageCodeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef(
    _RequiredListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef,
    _OptionalListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef,
):
    pass


_RequiredListDefaultVocabulariesRequestRequestTypeDef = TypedDict(
    "_RequiredListDefaultVocabulariesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListDefaultVocabulariesRequestRequestTypeDef = TypedDict(
    "_OptionalListDefaultVocabulariesRequestRequestTypeDef",
    {
        "LanguageCode": VocabularyLanguageCodeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDefaultVocabulariesRequestRequestTypeDef(
    _RequiredListDefaultVocabulariesRequestRequestTypeDef,
    _OptionalListDefaultVocabulariesRequestRequestTypeDef,
):
    pass


ListDefaultVocabulariesResponseTypeDef = TypedDict(
    "ListDefaultVocabulariesResponseTypeDef",
    {
        "DefaultVocabularyList": List["DefaultVocabularyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef = TypedDict(
    "_RequiredListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef",
    {
        "InstanceId": str,
        "EvaluationFormId": str,
    },
)
_OptionalListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef = TypedDict(
    "_OptionalListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef(
    _RequiredListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef,
    _OptionalListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef,
):
    pass


_RequiredListEvaluationFormVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListEvaluationFormVersionsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationFormId": str,
    },
)
_OptionalListEvaluationFormVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListEvaluationFormVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListEvaluationFormVersionsRequestRequestTypeDef(
    _RequiredListEvaluationFormVersionsRequestRequestTypeDef,
    _OptionalListEvaluationFormVersionsRequestRequestTypeDef,
):
    pass


ListEvaluationFormVersionsResponseTypeDef = TypedDict(
    "ListEvaluationFormVersionsResponseTypeDef",
    {
        "EvaluationFormVersionSummaryList": List["EvaluationFormVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef = TypedDict(
    "_RequiredListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef = TypedDict(
    "_OptionalListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef(
    _RequiredListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef,
    _OptionalListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef,
):
    pass


_RequiredListEvaluationFormsRequestRequestTypeDef = TypedDict(
    "_RequiredListEvaluationFormsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListEvaluationFormsRequestRequestTypeDef = TypedDict(
    "_OptionalListEvaluationFormsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListEvaluationFormsRequestRequestTypeDef(
    _RequiredListEvaluationFormsRequestRequestTypeDef,
    _OptionalListEvaluationFormsRequestRequestTypeDef,
):
    pass


ListEvaluationFormsResponseTypeDef = TypedDict(
    "ListEvaluationFormsResponseTypeDef",
    {
        "EvaluationFormSummaryList": List["EvaluationFormSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef = TypedDict(
    "_RequiredListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef = TypedDict(
    "_OptionalListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef(
    _RequiredListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef,
    _OptionalListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef,
):
    pass


_RequiredListHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListHoursOfOperationsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListHoursOfOperationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListHoursOfOperationsRequestRequestTypeDef(
    _RequiredListHoursOfOperationsRequestRequestTypeDef,
    _OptionalListHoursOfOperationsRequestRequestTypeDef,
):
    pass


ListHoursOfOperationsResponseTypeDef = TypedDict(
    "ListHoursOfOperationsResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List["HoursOfOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef = TypedDict(
    "_RequiredListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef = TypedDict(
    "_OptionalListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef(
    _RequiredListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef,
    _OptionalListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef,
):
    pass


_RequiredListInstanceAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListInstanceAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListInstanceAttributesRequestRequestTypeDef(
    _RequiredListInstanceAttributesRequestRequestTypeDef,
    _OptionalListInstanceAttributesRequestRequestTypeDef,
):
    pass


ListInstanceAttributesResponseTypeDef = TypedDict(
    "ListInstanceAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef = TypedDict(
    "_RequiredListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)
_OptionalListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef = TypedDict(
    "_OptionalListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef(
    _RequiredListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef,
    _OptionalListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef,
):
    pass


_RequiredListInstanceStorageConfigsRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceStorageConfigsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)
_OptionalListInstanceStorageConfigsRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceStorageConfigsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListInstanceStorageConfigsRequestRequestTypeDef(
    _RequiredListInstanceStorageConfigsRequestRequestTypeDef,
    _OptionalListInstanceStorageConfigsRequestRequestTypeDef,
):
    pass


ListInstanceStorageConfigsResponseTypeDef = TypedDict(
    "ListInstanceStorageConfigsResponseTypeDef",
    {
        "StorageConfigs": List["InstanceStorageConfigOutputTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestListInstancesPaginateTypeDef = TypedDict(
    "ListInstancesRequestListInstancesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "InstanceSummaryList": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef = TypedDict(
    "_RequiredListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef = TypedDict(
    "_OptionalListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef",
    {
        "IntegrationType": IntegrationTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef(
    _RequiredListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef,
    _OptionalListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef,
):
    pass


_RequiredListIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntegrationAssociationsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntegrationAssociationsRequestRequestTypeDef",
    {
        "IntegrationType": IntegrationTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIntegrationAssociationsRequestRequestTypeDef(
    _RequiredListIntegrationAssociationsRequestRequestTypeDef,
    _OptionalListIntegrationAssociationsRequestRequestTypeDef,
):
    pass


ListIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListIntegrationAssociationsResponseTypeDef",
    {
        "IntegrationAssociationSummaryList": List["IntegrationAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef = TypedDict(
    "_RequiredListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef = TypedDict(
    "_OptionalListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef(
    _RequiredListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef,
    _OptionalListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef,
):
    pass


_RequiredListLambdaFunctionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLambdaFunctionsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLambdaFunctionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLambdaFunctionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListLambdaFunctionsRequestRequestTypeDef(
    _RequiredListLambdaFunctionsRequestRequestTypeDef,
    _OptionalListLambdaFunctionsRequestRequestTypeDef,
):
    pass


ListLambdaFunctionsResponseTypeDef = TypedDict(
    "ListLambdaFunctionsResponseTypeDef",
    {
        "LambdaFunctions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLexBotsRequestListLexBotsPaginateTypeDef = TypedDict(
    "_RequiredListLexBotsRequestListLexBotsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLexBotsRequestListLexBotsPaginateTypeDef = TypedDict(
    "_OptionalListLexBotsRequestListLexBotsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListLexBotsRequestListLexBotsPaginateTypeDef(
    _RequiredListLexBotsRequestListLexBotsPaginateTypeDef,
    _OptionalListLexBotsRequestListLexBotsPaginateTypeDef,
):
    pass


_RequiredListLexBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListLexBotsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLexBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListLexBotsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListLexBotsRequestRequestTypeDef(
    _RequiredListLexBotsRequestRequestTypeDef, _OptionalListLexBotsRequestRequestTypeDef
):
    pass


ListLexBotsResponseTypeDef = TypedDict(
    "ListLexBotsResponseTypeDef",
    {
        "LexBots": List["LexBotOutputTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef = TypedDict(
    "_RequiredListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef = TypedDict(
    "_OptionalListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef",
    {
        "PhoneNumberTypes": Sequence[PhoneNumberTypeType],
        "PhoneNumberCountryCodes": Sequence[PhoneNumberCountryCodeType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef(
    _RequiredListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef,
    _OptionalListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef,
):
    pass


_RequiredListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "_RequiredListPhoneNumbersRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "_OptionalListPhoneNumbersRequestRequestTypeDef",
    {
        "PhoneNumberTypes": Sequence[PhoneNumberTypeType],
        "PhoneNumberCountryCodes": Sequence[PhoneNumberCountryCodeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPhoneNumbersRequestRequestTypeDef(
    _RequiredListPhoneNumbersRequestRequestTypeDef, _OptionalListPhoneNumbersRequestRequestTypeDef
):
    pass


ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumberSummaryList": List["PhoneNumberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersSummaryTypeDef = TypedDict(
    "ListPhoneNumbersSummaryTypeDef",
    {
        "PhoneNumberId": str,
        "PhoneNumberArn": str,
        "PhoneNumber": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
        "TargetArn": str,
    },
    total=False,
)

ListPhoneNumbersV2RequestListPhoneNumbersV2PaginateTypeDef = TypedDict(
    "ListPhoneNumbersV2RequestListPhoneNumbersV2PaginateTypeDef",
    {
        "TargetArn": str,
        "PhoneNumberCountryCodes": Sequence[PhoneNumberCountryCodeType],
        "PhoneNumberTypes": Sequence[PhoneNumberTypeType],
        "PhoneNumberPrefix": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListPhoneNumbersV2RequestRequestTypeDef = TypedDict(
    "ListPhoneNumbersV2RequestRequestTypeDef",
    {
        "TargetArn": str,
        "MaxResults": int,
        "NextToken": str,
        "PhoneNumberCountryCodes": Sequence[PhoneNumberCountryCodeType],
        "PhoneNumberTypes": Sequence[PhoneNumberTypeType],
        "PhoneNumberPrefix": str,
    },
    total=False,
)

ListPhoneNumbersV2ResponseTypeDef = TypedDict(
    "ListPhoneNumbersV2ResponseTypeDef",
    {
        "NextToken": str,
        "ListPhoneNumbersSummaryList": List["ListPhoneNumbersSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPromptsRequestListPromptsPaginateTypeDef = TypedDict(
    "_RequiredListPromptsRequestListPromptsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPromptsRequestListPromptsPaginateTypeDef = TypedDict(
    "_OptionalListPromptsRequestListPromptsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListPromptsRequestListPromptsPaginateTypeDef(
    _RequiredListPromptsRequestListPromptsPaginateTypeDef,
    _OptionalListPromptsRequestListPromptsPaginateTypeDef,
):
    pass


_RequiredListPromptsRequestRequestTypeDef = TypedDict(
    "_RequiredListPromptsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPromptsRequestRequestTypeDef = TypedDict(
    "_OptionalListPromptsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPromptsRequestRequestTypeDef(
    _RequiredListPromptsRequestRequestTypeDef, _OptionalListPromptsRequestRequestTypeDef
):
    pass


ListPromptsResponseTypeDef = TypedDict(
    "ListPromptsResponseTypeDef",
    {
        "PromptSummaryList": List["PromptSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef = TypedDict(
    "_RequiredListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef = TypedDict(
    "_OptionalListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef(
    _RequiredListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef,
    _OptionalListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef,
):
    pass


_RequiredListQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "_RequiredListQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalListQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "_OptionalListQueueQuickConnectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListQueueQuickConnectsRequestRequestTypeDef(
    _RequiredListQueueQuickConnectsRequestRequestTypeDef,
    _OptionalListQueueQuickConnectsRequestRequestTypeDef,
):
    pass


ListQueueQuickConnectsResponseTypeDef = TypedDict(
    "ListQueueQuickConnectsResponseTypeDef",
    {
        "NextToken": str,
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueuesRequestListQueuesPaginateTypeDef = TypedDict(
    "_RequiredListQueuesRequestListQueuesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQueuesRequestListQueuesPaginateTypeDef = TypedDict(
    "_OptionalListQueuesRequestListQueuesPaginateTypeDef",
    {
        "QueueTypes": Sequence[QueueTypeType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListQueuesRequestListQueuesPaginateTypeDef(
    _RequiredListQueuesRequestListQueuesPaginateTypeDef,
    _OptionalListQueuesRequestListQueuesPaginateTypeDef,
):
    pass


_RequiredListQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredListQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalListQueuesRequestRequestTypeDef",
    {
        "QueueTypes": Sequence[QueueTypeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListQueuesRequestRequestTypeDef(
    _RequiredListQueuesRequestRequestTypeDef, _OptionalListQueuesRequestRequestTypeDef
):
    pass


ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {
        "QueueSummaryList": List["QueueSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQuickConnectsRequestListQuickConnectsPaginateTypeDef = TypedDict(
    "_RequiredListQuickConnectsRequestListQuickConnectsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQuickConnectsRequestListQuickConnectsPaginateTypeDef = TypedDict(
    "_OptionalListQuickConnectsRequestListQuickConnectsPaginateTypeDef",
    {
        "QuickConnectTypes": Sequence[QuickConnectTypeType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListQuickConnectsRequestListQuickConnectsPaginateTypeDef(
    _RequiredListQuickConnectsRequestListQuickConnectsPaginateTypeDef,
    _OptionalListQuickConnectsRequestListQuickConnectsPaginateTypeDef,
):
    pass


_RequiredListQuickConnectsRequestRequestTypeDef = TypedDict(
    "_RequiredListQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQuickConnectsRequestRequestTypeDef = TypedDict(
    "_OptionalListQuickConnectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "QuickConnectTypes": Sequence[QuickConnectTypeType],
    },
    total=False,
)


class ListQuickConnectsRequestRequestTypeDef(
    _RequiredListQuickConnectsRequestRequestTypeDef, _OptionalListQuickConnectsRequestRequestTypeDef
):
    pass


ListQuickConnectsResponseTypeDef = TypedDict(
    "ListQuickConnectsResponseTypeDef",
    {
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef = TypedDict(
    "_RequiredListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef = TypedDict(
    "_OptionalListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef(
    _RequiredListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef,
    _OptionalListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef,
):
    pass


_RequiredListRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredListRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalListRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalListRoutingProfileQueuesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListRoutingProfileQueuesRequestRequestTypeDef(
    _RequiredListRoutingProfileQueuesRequestRequestTypeDef,
    _OptionalListRoutingProfileQueuesRequestRequestTypeDef,
):
    pass


ListRoutingProfileQueuesResponseTypeDef = TypedDict(
    "ListRoutingProfileQueuesResponseTypeDef",
    {
        "NextToken": str,
        "RoutingProfileQueueConfigSummaryList": List["RoutingProfileQueueConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef = TypedDict(
    "_RequiredListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef = TypedDict(
    "_OptionalListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef(
    _RequiredListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef,
    _OptionalListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef,
):
    pass


_RequiredListRoutingProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListRoutingProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListRoutingProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListRoutingProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListRoutingProfilesRequestRequestTypeDef(
    _RequiredListRoutingProfilesRequestRequestTypeDef,
    _OptionalListRoutingProfilesRequestRequestTypeDef,
):
    pass


ListRoutingProfilesResponseTypeDef = TypedDict(
    "ListRoutingProfilesResponseTypeDef",
    {
        "RoutingProfileSummaryList": List["RoutingProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "_RequiredListRulesRequestListRulesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "_OptionalListRulesRequestListRulesPaginateTypeDef",
    {
        "PublishStatus": RulePublishStatusType,
        "EventSourceName": EventSourceNameType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListRulesRequestListRulesPaginateTypeDef(
    _RequiredListRulesRequestListRulesPaginateTypeDef,
    _OptionalListRulesRequestListRulesPaginateTypeDef,
):
    pass


_RequiredListRulesRequestRequestTypeDef = TypedDict(
    "_RequiredListRulesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListRulesRequestRequestTypeDef = TypedDict(
    "_OptionalListRulesRequestRequestTypeDef",
    {
        "PublishStatus": RulePublishStatusType,
        "EventSourceName": EventSourceNameType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListRulesRequestRequestTypeDef(
    _RequiredListRulesRequestRequestTypeDef, _OptionalListRulesRequestRequestTypeDef
):
    pass


ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "RuleSummaryList": List["RuleSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityKeysRequestListSecurityKeysPaginateTypeDef = TypedDict(
    "_RequiredListSecurityKeysRequestListSecurityKeysPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityKeysRequestListSecurityKeysPaginateTypeDef = TypedDict(
    "_OptionalListSecurityKeysRequestListSecurityKeysPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListSecurityKeysRequestListSecurityKeysPaginateTypeDef(
    _RequiredListSecurityKeysRequestListSecurityKeysPaginateTypeDef,
    _OptionalListSecurityKeysRequestListSecurityKeysPaginateTypeDef,
):
    pass


_RequiredListSecurityKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityKeysRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityKeysRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListSecurityKeysRequestRequestTypeDef(
    _RequiredListSecurityKeysRequestRequestTypeDef, _OptionalListSecurityKeysRequestRequestTypeDef
):
    pass


ListSecurityKeysResponseTypeDef = TypedDict(
    "ListSecurityKeysResponseTypeDef",
    {
        "SecurityKeys": List["SecurityKeyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef = TypedDict(
    "_RequiredListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
    },
)
_OptionalListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef = TypedDict(
    "_OptionalListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef(
    _RequiredListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef,
    _OptionalListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef,
):
    pass


_RequiredListSecurityProfilePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilePermissionsRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
    },
)
_OptionalListSecurityProfilePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilePermissionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListSecurityProfilePermissionsRequestRequestTypeDef(
    _RequiredListSecurityProfilePermissionsRequestRequestTypeDef,
    _OptionalListSecurityProfilePermissionsRequestRequestTypeDef,
):
    pass


ListSecurityProfilePermissionsResponseTypeDef = TypedDict(
    "ListSecurityProfilePermissionsResponseTypeDef",
    {
        "Permissions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef = TypedDict(
    "_RequiredListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef = TypedDict(
    "_OptionalListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef(
    _RequiredListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef,
    _OptionalListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef,
):
    pass


_RequiredListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListSecurityProfilesRequestRequestTypeDef(
    _RequiredListSecurityProfilesRequestRequestTypeDef,
    _OptionalListSecurityProfilesRequestRequestTypeDef,
):
    pass


ListSecurityProfilesResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseTypeDef",
    {
        "SecurityProfileSummaryList": List["SecurityProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef = TypedDict(
    "_RequiredListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef = TypedDict(
    "_OptionalListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef",
    {
        "Status": TaskTemplateStatusType,
        "Name": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef(
    _RequiredListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef,
    _OptionalListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef,
):
    pass


_RequiredListTaskTemplatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTaskTemplatesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListTaskTemplatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTaskTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Status": TaskTemplateStatusType,
        "Name": str,
    },
    total=False,
)


class ListTaskTemplatesRequestRequestTypeDef(
    _RequiredListTaskTemplatesRequestRequestTypeDef, _OptionalListTaskTemplatesRequestRequestTypeDef
):
    pass


ListTaskTemplatesResponseTypeDef = TypedDict(
    "ListTaskTemplatesResponseTypeDef",
    {
        "TaskTemplates": List["TaskTemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficDistributionGroupsRequestListTrafficDistributionGroupsPaginateTypeDef = TypedDict(
    "ListTrafficDistributionGroupsRequestListTrafficDistributionGroupsPaginateTypeDef",
    {
        "InstanceId": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTrafficDistributionGroupsRequestRequestTypeDef = TypedDict(
    "ListTrafficDistributionGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "InstanceId": str,
    },
    total=False,
)

ListTrafficDistributionGroupsResponseTypeDef = TypedDict(
    "ListTrafficDistributionGroupsResponseTypeDef",
    {
        "NextToken": str,
        "TrafficDistributionGroupSummaryList": List["TrafficDistributionGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUseCasesRequestListUseCasesPaginateTypeDef = TypedDict(
    "_RequiredListUseCasesRequestListUseCasesPaginateTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)
_OptionalListUseCasesRequestListUseCasesPaginateTypeDef = TypedDict(
    "_OptionalListUseCasesRequestListUseCasesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListUseCasesRequestListUseCasesPaginateTypeDef(
    _RequiredListUseCasesRequestListUseCasesPaginateTypeDef,
    _OptionalListUseCasesRequestListUseCasesPaginateTypeDef,
):
    pass


_RequiredListUseCasesRequestRequestTypeDef = TypedDict(
    "_RequiredListUseCasesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)
_OptionalListUseCasesRequestRequestTypeDef = TypedDict(
    "_OptionalListUseCasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUseCasesRequestRequestTypeDef(
    _RequiredListUseCasesRequestRequestTypeDef, _OptionalListUseCasesRequestRequestTypeDef
):
    pass


ListUseCasesResponseTypeDef = TypedDict(
    "ListUseCasesResponseTypeDef",
    {
        "UseCaseSummaryList": List["UseCaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef = TypedDict(
    "_RequiredListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef = TypedDict(
    "_OptionalListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef(
    _RequiredListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef,
    _OptionalListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef,
):
    pass


_RequiredListUserHierarchyGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserHierarchyGroupsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUserHierarchyGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserHierarchyGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUserHierarchyGroupsRequestRequestTypeDef(
    _RequiredListUserHierarchyGroupsRequestRequestTypeDef,
    _OptionalListUserHierarchyGroupsRequestRequestTypeDef,
):
    pass


ListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "ListUserHierarchyGroupsResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List["HierarchyGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "_RequiredListUsersRequestListUsersPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "_OptionalListUsersRequestListUsersPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListUsersRequestListUsersPaginateTypeDef(
    _RequiredListUsersRequestListUsersPaginateTypeDef,
    _OptionalListUsersRequestListUsersPaginateTypeDef,
):
    pass


_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass


ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "UserSummaryList": List["UserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMediaConcurrencyOutputTypeDef = TypedDict(
    "_RequiredMediaConcurrencyOutputTypeDef",
    {
        "Channel": ChannelType,
        "Concurrency": int,
    },
)
_OptionalMediaConcurrencyOutputTypeDef = TypedDict(
    "_OptionalMediaConcurrencyOutputTypeDef",
    {
        "CrossChannelBehavior": "CrossChannelBehaviorOutputTypeDef",
    },
    total=False,
)


class MediaConcurrencyOutputTypeDef(
    _RequiredMediaConcurrencyOutputTypeDef, _OptionalMediaConcurrencyOutputTypeDef
):
    pass


_RequiredMediaConcurrencyTypeDef = TypedDict(
    "_RequiredMediaConcurrencyTypeDef",
    {
        "Channel": ChannelType,
        "Concurrency": int,
    },
)
_OptionalMediaConcurrencyTypeDef = TypedDict(
    "_OptionalMediaConcurrencyTypeDef",
    {
        "CrossChannelBehavior": "CrossChannelBehaviorTypeDef",
    },
    total=False,
)


class MediaConcurrencyTypeDef(_RequiredMediaConcurrencyTypeDef, _OptionalMediaConcurrencyTypeDef):
    pass


MetricDataV2TypeDef = TypedDict(
    "MetricDataV2TypeDef",
    {
        "Metric": "MetricV2OutputTypeDef",
        "Value": float,
    },
    total=False,
)

MetricFilterV2OutputTypeDef = TypedDict(
    "MetricFilterV2OutputTypeDef",
    {
        "MetricFilterKey": str,
        "MetricFilterValues": List[str],
    },
    total=False,
)

MetricFilterV2TypeDef = TypedDict(
    "MetricFilterV2TypeDef",
    {
        "MetricFilterKey": str,
        "MetricFilterValues": Sequence[str],
    },
    total=False,
)

MetricResultV2TypeDef = TypedDict(
    "MetricResultV2TypeDef",
    {
        "Dimensions": Dict[str, str],
        "Collections": List["MetricDataV2TypeDef"],
    },
    total=False,
)

MetricV2OutputTypeDef = TypedDict(
    "MetricV2OutputTypeDef",
    {
        "Name": str,
        "Threshold": List["ThresholdV2OutputTypeDef"],
        "MetricFilters": List["MetricFilterV2OutputTypeDef"],
    },
    total=False,
)

MetricV2TypeDef = TypedDict(
    "MetricV2TypeDef",
    {
        "Name": str,
        "Threshold": Sequence["ThresholdV2TypeDef"],
        "MetricFilters": Sequence["MetricFilterV2TypeDef"],
    },
    total=False,
)

_RequiredMonitorContactRequestRequestTypeDef = TypedDict(
    "_RequiredMonitorContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "UserId": str,
    },
)
_OptionalMonitorContactRequestRequestTypeDef = TypedDict(
    "_OptionalMonitorContactRequestRequestTypeDef",
    {
        "AllowedMonitorCapabilities": Sequence[MonitorCapabilityType],
        "ClientToken": str,
    },
    total=False,
)


class MonitorContactRequestRequestTypeDef(
    _RequiredMonitorContactRequestRequestTypeDef, _OptionalMonitorContactRequestRequestTypeDef
):
    pass


MonitorContactResponseTypeDef = TypedDict(
    "MonitorContactResponseTypeDef",
    {
        "ContactId": str,
        "ContactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationRecipientTypeOutputTypeDef = TypedDict(
    "NotificationRecipientTypeOutputTypeDef",
    {
        "UserTags": Dict[str, str],
        "UserIds": List[str],
    },
    total=False,
)

NotificationRecipientTypeTypeDef = TypedDict(
    "NotificationRecipientTypeTypeDef",
    {
        "UserTags": Mapping[str, str],
        "UserIds": Sequence[str],
    },
    total=False,
)

NumberReferenceTypeDef = TypedDict(
    "NumberReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

NumericQuestionPropertyValueAutomationOutputTypeDef = TypedDict(
    "NumericQuestionPropertyValueAutomationOutputTypeDef",
    {
        "Label": NumericQuestionPropertyAutomationLabelType,
    },
)

NumericQuestionPropertyValueAutomationTypeDef = TypedDict(
    "NumericQuestionPropertyValueAutomationTypeDef",
    {
        "Label": NumericQuestionPropertyAutomationLabelType,
    },
)

OutboundCallerConfigOutputTypeDef = TypedDict(
    "OutboundCallerConfigOutputTypeDef",
    {
        "OutboundCallerIdName": str,
        "OutboundCallerIdNumberId": str,
        "OutboundFlowId": str,
    },
    total=False,
)

OutboundCallerConfigTypeDef = TypedDict(
    "OutboundCallerConfigTypeDef",
    {
        "OutboundCallerIdName": str,
        "OutboundCallerIdNumberId": str,
        "OutboundFlowId": str,
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

ParticipantDetailsToAddTypeDef = TypedDict(
    "ParticipantDetailsToAddTypeDef",
    {
        "ParticipantRole": ParticipantRoleType,
        "DisplayName": str,
    },
    total=False,
)

ParticipantDetailsTypeDef = TypedDict(
    "ParticipantDetailsTypeDef",
    {
        "DisplayName": str,
    },
)

ParticipantTimerConfigurationTypeDef = TypedDict(
    "ParticipantTimerConfigurationTypeDef",
    {
        "ParticipantRole": TimerEligibleParticipantRolesType,
        "TimerType": ParticipantTimerTypeType,
        "TimerValue": "ParticipantTimerValueTypeDef",
    },
)

ParticipantTimerValueTypeDef = TypedDict(
    "ParticipantTimerValueTypeDef",
    {
        "ParticipantTimerAction": Literal["Unset"],
        "ParticipantTimerDurationInMinutes": int,
    },
    total=False,
)

ParticipantTokenCredentialsTypeDef = TypedDict(
    "ParticipantTokenCredentialsTypeDef",
    {
        "ParticipantToken": str,
        "Expiry": str,
    },
    total=False,
)

PersistentChatTypeDef = TypedDict(
    "PersistentChatTypeDef",
    {
        "RehydrationType": RehydrationTypeType,
        "SourceContactId": str,
    },
    total=False,
)

PhoneNumberQuickConnectConfigOutputTypeDef = TypedDict(
    "PhoneNumberQuickConnectConfigOutputTypeDef",
    {
        "PhoneNumber": str,
    },
)

PhoneNumberQuickConnectConfigTypeDef = TypedDict(
    "PhoneNumberQuickConnectConfigTypeDef",
    {
        "PhoneNumber": str,
    },
)

PhoneNumberStatusTypeDef = TypedDict(
    "PhoneNumberStatusTypeDef",
    {
        "Status": PhoneNumberWorkflowStatusType,
        "Message": str,
    },
    total=False,
)

PhoneNumberSummaryTypeDef = TypedDict(
    "PhoneNumberSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": PhoneNumberTypeType,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
    },
    total=False,
)

PromptSearchCriteriaTypeDef = TypedDict(
    "PromptSearchCriteriaTypeDef",
    {
        "OrConditions": Sequence[Dict[str, Any]],
        "AndConditions": Sequence[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
    },
    total=False,
)

PromptSearchFilterTypeDef = TypedDict(
    "PromptSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

PromptSummaryTypeDef = TypedDict(
    "PromptSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

PromptTypeDef = TypedDict(
    "PromptTypeDef",
    {
        "PromptARN": str,
        "PromptId": str,
        "Name": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

PutUserStatusRequestRequestTypeDef = TypedDict(
    "PutUserStatusRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
        "AgentStatusId": str,
    },
)

QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef",
    {
        "Id": str,
        "EnqueueTimestamp": datetime,
    },
    total=False,
)

QueueQuickConnectConfigOutputTypeDef = TypedDict(
    "QueueQuickConnectConfigOutputTypeDef",
    {
        "QueueId": str,
        "ContactFlowId": str,
    },
)

QueueQuickConnectConfigTypeDef = TypedDict(
    "QueueQuickConnectConfigTypeDef",
    {
        "QueueId": str,
        "ContactFlowId": str,
    },
)

QueueReferenceTypeDef = TypedDict(
    "QueueReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

QueueSearchCriteriaTypeDef = TypedDict(
    "QueueSearchCriteriaTypeDef",
    {
        "OrConditions": Sequence[Dict[str, Any]],
        "AndConditions": Sequence[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
        "QueueTypeCondition": Literal["STANDARD"],
    },
    total=False,
)

QueueSearchFilterTypeDef = TypedDict(
    "QueueSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "QueueType": QueueTypeType,
    },
    total=False,
)

QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": str,
        "QueueArn": str,
        "QueueId": str,
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigOutputTypeDef",
        "HoursOfOperationId": str,
        "MaxContacts": int,
        "Status": QueueStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredQuickConnectConfigOutputTypeDef = TypedDict(
    "_RequiredQuickConnectConfigOutputTypeDef",
    {
        "QuickConnectType": QuickConnectTypeType,
    },
)
_OptionalQuickConnectConfigOutputTypeDef = TypedDict(
    "_OptionalQuickConnectConfigOutputTypeDef",
    {
        "UserConfig": "UserQuickConnectConfigOutputTypeDef",
        "QueueConfig": "QueueQuickConnectConfigOutputTypeDef",
        "PhoneConfig": "PhoneNumberQuickConnectConfigOutputTypeDef",
    },
    total=False,
)


class QuickConnectConfigOutputTypeDef(
    _RequiredQuickConnectConfigOutputTypeDef, _OptionalQuickConnectConfigOutputTypeDef
):
    pass


_RequiredQuickConnectConfigTypeDef = TypedDict(
    "_RequiredQuickConnectConfigTypeDef",
    {
        "QuickConnectType": QuickConnectTypeType,
    },
)
_OptionalQuickConnectConfigTypeDef = TypedDict(
    "_OptionalQuickConnectConfigTypeDef",
    {
        "UserConfig": "UserQuickConnectConfigTypeDef",
        "QueueConfig": "QueueQuickConnectConfigTypeDef",
        "PhoneConfig": "PhoneNumberQuickConnectConfigTypeDef",
    },
    total=False,
)


class QuickConnectConfigTypeDef(
    _RequiredQuickConnectConfigTypeDef, _OptionalQuickConnectConfigTypeDef
):
    pass


QuickConnectSearchCriteriaTypeDef = TypedDict(
    "QuickConnectSearchCriteriaTypeDef",
    {
        "OrConditions": Sequence[Dict[str, Any]],
        "AndConditions": Sequence[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
    },
    total=False,
)

QuickConnectSearchFilterTypeDef = TypedDict(
    "QuickConnectSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

QuickConnectSummaryTypeDef = TypedDict(
    "QuickConnectSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "QuickConnectType": QuickConnectTypeType,
    },
    total=False,
)

QuickConnectTypeDef = TypedDict(
    "QuickConnectTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "Name": str,
        "Description": str,
        "QuickConnectConfig": "QuickConnectConfigOutputTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ReadOnlyFieldInfoOutputTypeDef = TypedDict(
    "ReadOnlyFieldInfoOutputTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierOutputTypeDef",
    },
    total=False,
)

ReadOnlyFieldInfoTypeDef = TypedDict(
    "ReadOnlyFieldInfoTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
    },
    total=False,
)

ReferenceOutputTypeDef = TypedDict(
    "ReferenceOutputTypeDef",
    {
        "Value": str,
        "Type": ReferenceTypeType,
    },
)

ReferenceSummaryTypeDef = TypedDict(
    "ReferenceSummaryTypeDef",
    {
        "Url": "UrlReferenceTypeDef",
        "Attachment": "AttachmentReferenceTypeDef",
        "String": "StringReferenceTypeDef",
        "Number": "NumberReferenceTypeDef",
        "Date": "DateReferenceTypeDef",
        "Email": "EmailReferenceTypeDef",
    },
    total=False,
)

ReferenceTypeDef = TypedDict(
    "ReferenceTypeDef",
    {
        "Value": str,
        "Type": ReferenceTypeType,
    },
)

_RequiredReleasePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredReleasePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalReleasePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalReleasePhoneNumberRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class ReleasePhoneNumberRequestRequestTypeDef(
    _RequiredReleasePhoneNumberRequestRequestTypeDef,
    _OptionalReleasePhoneNumberRequestRequestTypeDef,
):
    pass


_RequiredReplicateInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredReplicateInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ReplicaRegion": str,
        "ReplicaAlias": str,
    },
)
_OptionalReplicateInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalReplicateInstanceRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class ReplicateInstanceRequestRequestTypeDef(
    _RequiredReplicateInstanceRequestRequestTypeDef, _OptionalReplicateInstanceRequestRequestTypeDef
):
    pass


ReplicateInstanceResponseTypeDef = TypedDict(
    "ReplicateInstanceResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequiredFieldInfoOutputTypeDef = TypedDict(
    "RequiredFieldInfoOutputTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierOutputTypeDef",
    },
    total=False,
)

RequiredFieldInfoTypeDef = TypedDict(
    "RequiredFieldInfoTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
    },
    total=False,
)

ResourceTagsSearchCriteriaTypeDef = TypedDict(
    "ResourceTagsSearchCriteriaTypeDef",
    {
        "TagSearchCondition": "TagSearchConditionTypeDef",
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

ResumeContactRecordingRequestRequestTypeDef = TypedDict(
    "ResumeContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

RoutingProfileQueueConfigSummaryTypeDef = TypedDict(
    "RoutingProfileQueueConfigSummaryTypeDef",
    {
        "QueueId": str,
        "QueueArn": str,
        "QueueName": str,
        "Priority": int,
        "Delay": int,
        "Channel": ChannelType,
    },
)

RoutingProfileQueueConfigTypeDef = TypedDict(
    "RoutingProfileQueueConfigTypeDef",
    {
        "QueueReference": "RoutingProfileQueueReferenceTypeDef",
        "Priority": int,
        "Delay": int,
    },
)

RoutingProfileQueueReferenceTypeDef = TypedDict(
    "RoutingProfileQueueReferenceTypeDef",
    {
        "QueueId": str,
        "Channel": ChannelType,
    },
)

RoutingProfileReferenceTypeDef = TypedDict(
    "RoutingProfileReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

RoutingProfileSearchCriteriaTypeDef = TypedDict(
    "RoutingProfileSearchCriteriaTypeDef",
    {
        "OrConditions": Sequence[Dict[str, Any]],
        "AndConditions": Sequence[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
    },
    total=False,
)

RoutingProfileSearchFilterTypeDef = TypedDict(
    "RoutingProfileSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

RoutingProfileSummaryTypeDef = TypedDict(
    "RoutingProfileSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

RoutingProfileTypeDef = TypedDict(
    "RoutingProfileTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "Description": str,
        "MediaConcurrencies": List["MediaConcurrencyOutputTypeDef"],
        "DefaultOutboundQueueId": str,
        "Tags": Dict[str, str],
        "NumberOfAssociatedQueues": int,
        "NumberOfAssociatedUsers": int,
    },
    total=False,
)

_RequiredRuleActionOutputTypeDef = TypedDict(
    "_RequiredRuleActionOutputTypeDef",
    {
        "ActionType": ActionTypeType,
    },
)
_OptionalRuleActionOutputTypeDef = TypedDict(
    "_OptionalRuleActionOutputTypeDef",
    {
        "TaskAction": "TaskActionDefinitionOutputTypeDef",
        "EventBridgeAction": "EventBridgeActionDefinitionOutputTypeDef",
        "AssignContactCategoryAction": Dict[str, Any],
        "SendNotificationAction": "SendNotificationActionDefinitionOutputTypeDef",
    },
    total=False,
)


class RuleActionOutputTypeDef(_RequiredRuleActionOutputTypeDef, _OptionalRuleActionOutputTypeDef):
    pass


_RequiredRuleActionTypeDef = TypedDict(
    "_RequiredRuleActionTypeDef",
    {
        "ActionType": ActionTypeType,
    },
)
_OptionalRuleActionTypeDef = TypedDict(
    "_OptionalRuleActionTypeDef",
    {
        "TaskAction": "TaskActionDefinitionTypeDef",
        "EventBridgeAction": "EventBridgeActionDefinitionTypeDef",
        "AssignContactCategoryAction": Mapping[str, Any],
        "SendNotificationAction": "SendNotificationActionDefinitionTypeDef",
    },
    total=False,
)


class RuleActionTypeDef(_RequiredRuleActionTypeDef, _OptionalRuleActionTypeDef):
    pass


RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Name": str,
        "RuleId": str,
        "RuleArn": str,
        "EventSourceName": EventSourceNameType,
        "PublishStatus": RulePublishStatusType,
        "ActionSummaries": List["ActionSummaryTypeDef"],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
)

_RequiredRuleTriggerEventSourceOutputTypeDef = TypedDict(
    "_RequiredRuleTriggerEventSourceOutputTypeDef",
    {
        "EventSourceName": EventSourceNameType,
    },
)
_OptionalRuleTriggerEventSourceOutputTypeDef = TypedDict(
    "_OptionalRuleTriggerEventSourceOutputTypeDef",
    {
        "IntegrationAssociationId": str,
    },
    total=False,
)


class RuleTriggerEventSourceOutputTypeDef(
    _RequiredRuleTriggerEventSourceOutputTypeDef, _OptionalRuleTriggerEventSourceOutputTypeDef
):
    pass


_RequiredRuleTriggerEventSourceTypeDef = TypedDict(
    "_RequiredRuleTriggerEventSourceTypeDef",
    {
        "EventSourceName": EventSourceNameType,
    },
)
_OptionalRuleTriggerEventSourceTypeDef = TypedDict(
    "_OptionalRuleTriggerEventSourceTypeDef",
    {
        "IntegrationAssociationId": str,
    },
    total=False,
)


class RuleTriggerEventSourceTypeDef(
    _RequiredRuleTriggerEventSourceTypeDef, _OptionalRuleTriggerEventSourceTypeDef
):
    pass


_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Name": str,
        "RuleId": str,
        "RuleArn": str,
        "TriggerEventSource": "RuleTriggerEventSourceOutputTypeDef",
        "Function": str,
        "Actions": List["RuleActionOutputTypeDef"],
        "PublishStatus": RulePublishStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass


_RequiredS3ConfigOutputTypeDef = TypedDict(
    "_RequiredS3ConfigOutputTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
    },
)
_OptionalS3ConfigOutputTypeDef = TypedDict(
    "_OptionalS3ConfigOutputTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigOutputTypeDef",
    },
    total=False,
)


class S3ConfigOutputTypeDef(_RequiredS3ConfigOutputTypeDef, _OptionalS3ConfigOutputTypeDef):
    pass


_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
    total=False,
)


class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass


_RequiredSearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "_RequiredSearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "TargetArn": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
    },
)
_OptionalSearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "_OptionalSearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "PhoneNumberPrefix": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class SearchAvailablePhoneNumbersRequestRequestTypeDef(
    _RequiredSearchAvailablePhoneNumbersRequestRequestTypeDef,
    _OptionalSearchAvailablePhoneNumbersRequestRequestTypeDef,
):
    pass


_RequiredSearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef = TypedDict(
    "_RequiredSearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef",
    {
        "TargetArn": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
    },
)
_OptionalSearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef = TypedDict(
    "_OptionalSearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef",
    {
        "PhoneNumberPrefix": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef(
    _RequiredSearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef,
    _OptionalSearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef,
):
    pass


SearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseTypeDef",
    {
        "NextToken": str,
        "AvailableNumbersList": List["AvailableNumberSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchHoursOfOperationsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchHoursOfOperationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SearchFilter": "HoursOfOperationSearchFilterTypeDef",
        "SearchCriteria": "HoursOfOperationSearchCriteriaTypeDef",
    },
    total=False,
)


class SearchHoursOfOperationsRequestRequestTypeDef(
    _RequiredSearchHoursOfOperationsRequestRequestTypeDef,
    _OptionalSearchHoursOfOperationsRequestRequestTypeDef,
):
    pass


_RequiredSearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef = TypedDict(
    "_RequiredSearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef = TypedDict(
    "_OptionalSearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef",
    {
        "SearchFilter": "HoursOfOperationSearchFilterTypeDef",
        "SearchCriteria": "HoursOfOperationSearchCriteriaTypeDef",
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef(
    _RequiredSearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef,
    _OptionalSearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef,
):
    pass


SearchHoursOfOperationsResponseTypeDef = TypedDict(
    "SearchHoursOfOperationsResponseTypeDef",
    {
        "HoursOfOperations": List["HoursOfOperationTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPromptsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchPromptsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchPromptsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchPromptsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SearchFilter": "PromptSearchFilterTypeDef",
        "SearchCriteria": "PromptSearchCriteriaTypeDef",
    },
    total=False,
)


class SearchPromptsRequestRequestTypeDef(
    _RequiredSearchPromptsRequestRequestTypeDef, _OptionalSearchPromptsRequestRequestTypeDef
):
    pass


_RequiredSearchPromptsRequestSearchPromptsPaginateTypeDef = TypedDict(
    "_RequiredSearchPromptsRequestSearchPromptsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchPromptsRequestSearchPromptsPaginateTypeDef = TypedDict(
    "_OptionalSearchPromptsRequestSearchPromptsPaginateTypeDef",
    {
        "SearchFilter": "PromptSearchFilterTypeDef",
        "SearchCriteria": "PromptSearchCriteriaTypeDef",
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchPromptsRequestSearchPromptsPaginateTypeDef(
    _RequiredSearchPromptsRequestSearchPromptsPaginateTypeDef,
    _OptionalSearchPromptsRequestSearchPromptsPaginateTypeDef,
):
    pass


SearchPromptsResponseTypeDef = TypedDict(
    "SearchPromptsResponseTypeDef",
    {
        "Prompts": List["PromptTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchQueuesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SearchFilter": "QueueSearchFilterTypeDef",
        "SearchCriteria": "QueueSearchCriteriaTypeDef",
    },
    total=False,
)


class SearchQueuesRequestRequestTypeDef(
    _RequiredSearchQueuesRequestRequestTypeDef, _OptionalSearchQueuesRequestRequestTypeDef
):
    pass


_RequiredSearchQueuesRequestSearchQueuesPaginateTypeDef = TypedDict(
    "_RequiredSearchQueuesRequestSearchQueuesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchQueuesRequestSearchQueuesPaginateTypeDef = TypedDict(
    "_OptionalSearchQueuesRequestSearchQueuesPaginateTypeDef",
    {
        "SearchFilter": "QueueSearchFilterTypeDef",
        "SearchCriteria": "QueueSearchCriteriaTypeDef",
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchQueuesRequestSearchQueuesPaginateTypeDef(
    _RequiredSearchQueuesRequestSearchQueuesPaginateTypeDef,
    _OptionalSearchQueuesRequestSearchQueuesPaginateTypeDef,
):
    pass


SearchQueuesResponseTypeDef = TypedDict(
    "SearchQueuesResponseTypeDef",
    {
        "Queues": List["QueueTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchQuickConnectsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchQuickConnectsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchQuickConnectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SearchFilter": "QuickConnectSearchFilterTypeDef",
        "SearchCriteria": "QuickConnectSearchCriteriaTypeDef",
    },
    total=False,
)


class SearchQuickConnectsRequestRequestTypeDef(
    _RequiredSearchQuickConnectsRequestRequestTypeDef,
    _OptionalSearchQuickConnectsRequestRequestTypeDef,
):
    pass


_RequiredSearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef = TypedDict(
    "_RequiredSearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef = TypedDict(
    "_OptionalSearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef",
    {
        "SearchFilter": "QuickConnectSearchFilterTypeDef",
        "SearchCriteria": "QuickConnectSearchCriteriaTypeDef",
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef(
    _RequiredSearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef,
    _OptionalSearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef,
):
    pass


SearchQuickConnectsResponseTypeDef = TypedDict(
    "SearchQuickConnectsResponseTypeDef",
    {
        "QuickConnects": List["QuickConnectTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchResourceTagsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchResourceTagsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchResourceTagsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchResourceTagsRequestRequestTypeDef",
    {
        "ResourceTypes": Sequence[str],
        "NextToken": str,
        "MaxResults": int,
        "SearchCriteria": "ResourceTagsSearchCriteriaTypeDef",
    },
    total=False,
)


class SearchResourceTagsRequestRequestTypeDef(
    _RequiredSearchResourceTagsRequestRequestTypeDef,
    _OptionalSearchResourceTagsRequestRequestTypeDef,
):
    pass


_RequiredSearchResourceTagsRequestSearchResourceTagsPaginateTypeDef = TypedDict(
    "_RequiredSearchResourceTagsRequestSearchResourceTagsPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchResourceTagsRequestSearchResourceTagsPaginateTypeDef = TypedDict(
    "_OptionalSearchResourceTagsRequestSearchResourceTagsPaginateTypeDef",
    {
        "ResourceTypes": Sequence[str],
        "SearchCriteria": "ResourceTagsSearchCriteriaTypeDef",
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchResourceTagsRequestSearchResourceTagsPaginateTypeDef(
    _RequiredSearchResourceTagsRequestSearchResourceTagsPaginateTypeDef,
    _OptionalSearchResourceTagsRequestSearchResourceTagsPaginateTypeDef,
):
    pass


SearchResourceTagsResponseTypeDef = TypedDict(
    "SearchResourceTagsResponseTypeDef",
    {
        "Tags": List["TagSetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchRoutingProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchRoutingProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchRoutingProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchRoutingProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SearchFilter": "RoutingProfileSearchFilterTypeDef",
        "SearchCriteria": "RoutingProfileSearchCriteriaTypeDef",
    },
    total=False,
)


class SearchRoutingProfilesRequestRequestTypeDef(
    _RequiredSearchRoutingProfilesRequestRequestTypeDef,
    _OptionalSearchRoutingProfilesRequestRequestTypeDef,
):
    pass


_RequiredSearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef = TypedDict(
    "_RequiredSearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef = TypedDict(
    "_OptionalSearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef",
    {
        "SearchFilter": "RoutingProfileSearchFilterTypeDef",
        "SearchCriteria": "RoutingProfileSearchCriteriaTypeDef",
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef(
    _RequiredSearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef,
    _OptionalSearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef,
):
    pass


SearchRoutingProfilesResponseTypeDef = TypedDict(
    "SearchRoutingProfilesResponseTypeDef",
    {
        "RoutingProfiles": List["RoutingProfileTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchSecurityProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchSecurityProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SearchCriteria": "SecurityProfileSearchCriteriaTypeDef",
        "SearchFilter": "SecurityProfilesSearchFilterTypeDef",
    },
    total=False,
)


class SearchSecurityProfilesRequestRequestTypeDef(
    _RequiredSearchSecurityProfilesRequestRequestTypeDef,
    _OptionalSearchSecurityProfilesRequestRequestTypeDef,
):
    pass


_RequiredSearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef = TypedDict(
    "_RequiredSearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef = TypedDict(
    "_OptionalSearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef",
    {
        "SearchCriteria": "SecurityProfileSearchCriteriaTypeDef",
        "SearchFilter": "SecurityProfilesSearchFilterTypeDef",
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef(
    _RequiredSearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef,
    _OptionalSearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef,
):
    pass


SearchSecurityProfilesResponseTypeDef = TypedDict(
    "SearchSecurityProfilesResponseTypeDef",
    {
        "SecurityProfiles": List["SecurityProfileSearchSummaryTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchUsersRequestRequestTypeDef = TypedDict(
    "SearchUsersRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": str,
        "MaxResults": int,
        "SearchFilter": "UserSearchFilterTypeDef",
        "SearchCriteria": "UserSearchCriteriaTypeDef",
    },
    total=False,
)

SearchUsersRequestSearchUsersPaginateTypeDef = TypedDict(
    "SearchUsersRequestSearchUsersPaginateTypeDef",
    {
        "InstanceId": str,
        "SearchFilter": "UserSearchFilterTypeDef",
        "SearchCriteria": "UserSearchCriteriaTypeDef",
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

SearchUsersResponseTypeDef = TypedDict(
    "SearchUsersResponseTypeDef",
    {
        "Users": List["UserSearchSummaryTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchVocabulariesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchVocabulariesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchVocabulariesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchVocabulariesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "State": VocabularyStateType,
        "NameStartsWith": str,
        "LanguageCode": VocabularyLanguageCodeType,
    },
    total=False,
)


class SearchVocabulariesRequestRequestTypeDef(
    _RequiredSearchVocabulariesRequestRequestTypeDef,
    _OptionalSearchVocabulariesRequestRequestTypeDef,
):
    pass


_RequiredSearchVocabulariesRequestSearchVocabulariesPaginateTypeDef = TypedDict(
    "_RequiredSearchVocabulariesRequestSearchVocabulariesPaginateTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchVocabulariesRequestSearchVocabulariesPaginateTypeDef = TypedDict(
    "_OptionalSearchVocabulariesRequestSearchVocabulariesPaginateTypeDef",
    {
        "State": VocabularyStateType,
        "NameStartsWith": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchVocabulariesRequestSearchVocabulariesPaginateTypeDef(
    _RequiredSearchVocabulariesRequestSearchVocabulariesPaginateTypeDef,
    _OptionalSearchVocabulariesRequestSearchVocabulariesPaginateTypeDef,
):
    pass


SearchVocabulariesResponseTypeDef = TypedDict(
    "SearchVocabulariesResponseTypeDef",
    {
        "VocabularySummaryList": List["VocabularySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityKeyTypeDef = TypedDict(
    "SecurityKeyTypeDef",
    {
        "AssociationId": str,
        "Key": str,
        "CreationTime": datetime,
    },
    total=False,
)

SecurityProfileSearchCriteriaTypeDef = TypedDict(
    "SecurityProfileSearchCriteriaTypeDef",
    {
        "OrConditions": Sequence[Dict[str, Any]],
        "AndConditions": Sequence[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
    },
    total=False,
)

SecurityProfileSearchSummaryTypeDef = TypedDict(
    "SecurityProfileSearchSummaryTypeDef",
    {
        "Id": str,
        "OrganizationResourceId": str,
        "Arn": str,
        "SecurityProfileName": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

SecurityProfileSummaryTypeDef = TypedDict(
    "SecurityProfileSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

SecurityProfileTypeDef = TypedDict(
    "SecurityProfileTypeDef",
    {
        "Id": str,
        "OrganizationResourceId": str,
        "Arn": str,
        "SecurityProfileName": str,
        "Description": str,
        "Tags": Dict[str, str],
        "AllowedAccessControlTags": Dict[str, str],
        "TagRestrictedResources": List[str],
    },
    total=False,
)

SecurityProfilesSearchFilterTypeDef = TypedDict(
    "SecurityProfilesSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

_RequiredSendNotificationActionDefinitionOutputTypeDef = TypedDict(
    "_RequiredSendNotificationActionDefinitionOutputTypeDef",
    {
        "DeliveryMethod": Literal["EMAIL"],
        "Content": str,
        "ContentType": Literal["PLAIN_TEXT"],
        "Recipient": "NotificationRecipientTypeOutputTypeDef",
    },
)
_OptionalSendNotificationActionDefinitionOutputTypeDef = TypedDict(
    "_OptionalSendNotificationActionDefinitionOutputTypeDef",
    {
        "Subject": str,
    },
    total=False,
)


class SendNotificationActionDefinitionOutputTypeDef(
    _RequiredSendNotificationActionDefinitionOutputTypeDef,
    _OptionalSendNotificationActionDefinitionOutputTypeDef,
):
    pass


_RequiredSendNotificationActionDefinitionTypeDef = TypedDict(
    "_RequiredSendNotificationActionDefinitionTypeDef",
    {
        "DeliveryMethod": Literal["EMAIL"],
        "Content": str,
        "ContentType": Literal["PLAIN_TEXT"],
        "Recipient": "NotificationRecipientTypeTypeDef",
    },
)
_OptionalSendNotificationActionDefinitionTypeDef = TypedDict(
    "_OptionalSendNotificationActionDefinitionTypeDef",
    {
        "Subject": str,
    },
    total=False,
)


class SendNotificationActionDefinitionTypeDef(
    _RequiredSendNotificationActionDefinitionTypeDef,
    _OptionalSendNotificationActionDefinitionTypeDef,
):
    pass


SingleSelectQuestionRuleCategoryAutomationOutputTypeDef = TypedDict(
    "SingleSelectQuestionRuleCategoryAutomationOutputTypeDef",
    {
        "Category": str,
        "Condition": SingleSelectQuestionRuleCategoryAutomationConditionType,
        "OptionRefId": str,
    },
)

SingleSelectQuestionRuleCategoryAutomationTypeDef = TypedDict(
    "SingleSelectQuestionRuleCategoryAutomationTypeDef",
    {
        "Category": str,
        "Condition": SingleSelectQuestionRuleCategoryAutomationConditionType,
        "OptionRefId": str,
    },
)

_RequiredStartChatContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartChatContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "ParticipantDetails": "ParticipantDetailsTypeDef",
    },
)
_OptionalStartChatContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartChatContactRequestRequestTypeDef",
    {
        "Attributes": Mapping[str, str],
        "InitialMessage": "ChatMessageTypeDef",
        "ClientToken": str,
        "ChatDurationInMinutes": int,
        "SupportedMessagingContentTypes": Sequence[str],
        "PersistentChat": "PersistentChatTypeDef",
        "RelatedContactId": str,
    },
    total=False,
)


class StartChatContactRequestRequestTypeDef(
    _RequiredStartChatContactRequestRequestTypeDef, _OptionalStartChatContactRequestRequestTypeDef
):
    pass


StartChatContactResponseTypeDef = TypedDict(
    "StartChatContactResponseTypeDef",
    {
        "ContactId": str,
        "ParticipantId": str,
        "ParticipantToken": str,
        "ContinuedFromContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartContactEvaluationRequestRequestTypeDef = TypedDict(
    "_RequiredStartContactEvaluationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "EvaluationFormId": str,
    },
)
_OptionalStartContactEvaluationRequestRequestTypeDef = TypedDict(
    "_OptionalStartContactEvaluationRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class StartContactEvaluationRequestRequestTypeDef(
    _RequiredStartContactEvaluationRequestRequestTypeDef,
    _OptionalStartContactEvaluationRequestRequestTypeDef,
):
    pass


StartContactEvaluationResponseTypeDef = TypedDict(
    "StartContactEvaluationResponseTypeDef",
    {
        "EvaluationId": str,
        "EvaluationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartContactRecordingRequestRequestTypeDef = TypedDict(
    "StartContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
        "VoiceRecordingConfiguration": "VoiceRecordingConfigurationTypeDef",
    },
)

StartContactStreamingRequestRequestTypeDef = TypedDict(
    "StartContactStreamingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ChatStreamingConfiguration": "ChatStreamingConfigurationTypeDef",
        "ClientToken": str,
    },
)

StartContactStreamingResponseTypeDef = TypedDict(
    "StartContactStreamingResponseTypeDef",
    {
        "StreamingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartOutboundVoiceContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartOutboundVoiceContactRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "ContactFlowId": str,
        "InstanceId": str,
    },
)
_OptionalStartOutboundVoiceContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartOutboundVoiceContactRequestRequestTypeDef",
    {
        "ClientToken": str,
        "SourcePhoneNumber": str,
        "QueueId": str,
        "Attributes": Mapping[str, str],
        "AnswerMachineDetectionConfig": "AnswerMachineDetectionConfigTypeDef",
        "CampaignId": str,
        "TrafficType": TrafficTypeType,
    },
    total=False,
)


class StartOutboundVoiceContactRequestRequestTypeDef(
    _RequiredStartOutboundVoiceContactRequestRequestTypeDef,
    _OptionalStartOutboundVoiceContactRequestRequestTypeDef,
):
    pass


StartOutboundVoiceContactResponseTypeDef = TypedDict(
    "StartOutboundVoiceContactResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTaskContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartTaskContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
    },
)
_OptionalStartTaskContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartTaskContactRequestRequestTypeDef",
    {
        "PreviousContactId": str,
        "ContactFlowId": str,
        "Attributes": Mapping[str, str],
        "References": Mapping[str, "ReferenceTypeDef"],
        "Description": str,
        "ClientToken": str,
        "ScheduledTime": Union[datetime, str],
        "TaskTemplateId": str,
        "QuickConnectId": str,
        "RelatedContactId": str,
    },
    total=False,
)


class StartTaskContactRequestRequestTypeDef(
    _RequiredStartTaskContactRequestRequestTypeDef, _OptionalStartTaskContactRequestRequestTypeDef
):
    pass


StartTaskContactResponseTypeDef = TypedDict(
    "StartTaskContactResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopContactRecordingRequestRequestTypeDef = TypedDict(
    "StopContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

StopContactRequestRequestTypeDef = TypedDict(
    "StopContactRequestRequestTypeDef",
    {
        "ContactId": str,
        "InstanceId": str,
    },
)

StopContactStreamingRequestRequestTypeDef = TypedDict(
    "StopContactStreamingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "StreamingId": str,
    },
)

StringConditionTypeDef = TypedDict(
    "StringConditionTypeDef",
    {
        "FieldName": str,
        "Value": str,
        "ComparisonType": StringComparisonTypeType,
    },
    total=False,
)

StringReferenceTypeDef = TypedDict(
    "StringReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

_RequiredSubmitContactEvaluationRequestRequestTypeDef = TypedDict(
    "_RequiredSubmitContactEvaluationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationId": str,
    },
)
_OptionalSubmitContactEvaluationRequestRequestTypeDef = TypedDict(
    "_OptionalSubmitContactEvaluationRequestRequestTypeDef",
    {
        "Answers": Mapping[str, "EvaluationAnswerInputTypeDef"],
        "Notes": Mapping[str, "EvaluationNoteTypeDef"],
    },
    total=False,
)


class SubmitContactEvaluationRequestRequestTypeDef(
    _RequiredSubmitContactEvaluationRequestRequestTypeDef,
    _OptionalSubmitContactEvaluationRequestRequestTypeDef,
):
    pass


SubmitContactEvaluationResponseTypeDef = TypedDict(
    "SubmitContactEvaluationResponseTypeDef",
    {
        "EvaluationId": str,
        "EvaluationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuspendContactRecordingRequestRequestTypeDef = TypedDict(
    "SuspendContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

TagConditionTypeDef = TypedDict(
    "TagConditionTypeDef",
    {
        "TagKey": str,
        "TagValue": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TagSearchConditionTypeDef = TypedDict(
    "TagSearchConditionTypeDef",
    {
        "tagKey": str,
        "tagValue": str,
        "tagKeyComparisonType": StringComparisonTypeType,
        "tagValueComparisonType": StringComparisonTypeType,
    },
    total=False,
)

TagSetTypeDef = TypedDict(
    "TagSetTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredTaskActionDefinitionOutputTypeDef = TypedDict(
    "_RequiredTaskActionDefinitionOutputTypeDef",
    {
        "Name": str,
        "ContactFlowId": str,
    },
)
_OptionalTaskActionDefinitionOutputTypeDef = TypedDict(
    "_OptionalTaskActionDefinitionOutputTypeDef",
    {
        "Description": str,
        "References": Dict[str, "ReferenceOutputTypeDef"],
    },
    total=False,
)


class TaskActionDefinitionOutputTypeDef(
    _RequiredTaskActionDefinitionOutputTypeDef, _OptionalTaskActionDefinitionOutputTypeDef
):
    pass


_RequiredTaskActionDefinitionTypeDef = TypedDict(
    "_RequiredTaskActionDefinitionTypeDef",
    {
        "Name": str,
        "ContactFlowId": str,
    },
)
_OptionalTaskActionDefinitionTypeDef = TypedDict(
    "_OptionalTaskActionDefinitionTypeDef",
    {
        "Description": str,
        "References": Mapping[str, "ReferenceTypeDef"],
    },
    total=False,
)


class TaskActionDefinitionTypeDef(
    _RequiredTaskActionDefinitionTypeDef, _OptionalTaskActionDefinitionTypeDef
):
    pass


TaskTemplateConstraintsOutputTypeDef = TypedDict(
    "TaskTemplateConstraintsOutputTypeDef",
    {
        "RequiredFields": List["RequiredFieldInfoOutputTypeDef"],
        "ReadOnlyFields": List["ReadOnlyFieldInfoOutputTypeDef"],
        "InvisibleFields": List["InvisibleFieldInfoOutputTypeDef"],
    },
    total=False,
)

TaskTemplateConstraintsTypeDef = TypedDict(
    "TaskTemplateConstraintsTypeDef",
    {
        "RequiredFields": Sequence["RequiredFieldInfoTypeDef"],
        "ReadOnlyFields": Sequence["ReadOnlyFieldInfoTypeDef"],
        "InvisibleFields": Sequence["InvisibleFieldInfoTypeDef"],
    },
    total=False,
)

TaskTemplateDefaultFieldValueOutputTypeDef = TypedDict(
    "TaskTemplateDefaultFieldValueOutputTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierOutputTypeDef",
        "DefaultValue": str,
    },
    total=False,
)

TaskTemplateDefaultFieldValueTypeDef = TypedDict(
    "TaskTemplateDefaultFieldValueTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
        "DefaultValue": str,
    },
    total=False,
)

TaskTemplateDefaultsOutputTypeDef = TypedDict(
    "TaskTemplateDefaultsOutputTypeDef",
    {
        "DefaultFieldValues": List["TaskTemplateDefaultFieldValueOutputTypeDef"],
    },
    total=False,
)

TaskTemplateDefaultsTypeDef = TypedDict(
    "TaskTemplateDefaultsTypeDef",
    {
        "DefaultFieldValues": Sequence["TaskTemplateDefaultFieldValueTypeDef"],
    },
    total=False,
)

TaskTemplateFieldIdentifierOutputTypeDef = TypedDict(
    "TaskTemplateFieldIdentifierOutputTypeDef",
    {
        "Name": str,
    },
    total=False,
)

TaskTemplateFieldIdentifierTypeDef = TypedDict(
    "TaskTemplateFieldIdentifierTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredTaskTemplateFieldOutputTypeDef = TypedDict(
    "_RequiredTaskTemplateFieldOutputTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierOutputTypeDef",
    },
)
_OptionalTaskTemplateFieldOutputTypeDef = TypedDict(
    "_OptionalTaskTemplateFieldOutputTypeDef",
    {
        "Description": str,
        "Type": TaskTemplateFieldTypeType,
        "SingleSelectOptions": List[str],
    },
    total=False,
)


class TaskTemplateFieldOutputTypeDef(
    _RequiredTaskTemplateFieldOutputTypeDef, _OptionalTaskTemplateFieldOutputTypeDef
):
    pass


_RequiredTaskTemplateFieldTypeDef = TypedDict(
    "_RequiredTaskTemplateFieldTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
    },
)
_OptionalTaskTemplateFieldTypeDef = TypedDict(
    "_OptionalTaskTemplateFieldTypeDef",
    {
        "Description": str,
        "Type": TaskTemplateFieldTypeType,
        "SingleSelectOptions": Sequence[str],
    },
    total=False,
)


class TaskTemplateFieldTypeDef(
    _RequiredTaskTemplateFieldTypeDef, _OptionalTaskTemplateFieldTypeDef
):
    pass


TaskTemplateMetadataTypeDef = TypedDict(
    "TaskTemplateMetadataTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Status": TaskTemplateStatusType,
        "LastModifiedTime": datetime,
        "CreatedTime": datetime,
    },
    total=False,
)

TelephonyConfigOutputTypeDef = TypedDict(
    "TelephonyConfigOutputTypeDef",
    {
        "Distributions": List["DistributionOutputTypeDef"],
    },
)

TelephonyConfigTypeDef = TypedDict(
    "TelephonyConfigTypeDef",
    {
        "Distributions": Sequence["DistributionTypeDef"],
    },
)

ThresholdOutputTypeDef = TypedDict(
    "ThresholdOutputTypeDef",
    {
        "Comparison": Literal["LT"],
        "ThresholdValue": float,
    },
    total=False,
)

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Comparison": Literal["LT"],
        "ThresholdValue": float,
    },
    total=False,
)

ThresholdV2OutputTypeDef = TypedDict(
    "ThresholdV2OutputTypeDef",
    {
        "Comparison": str,
        "ThresholdValue": float,
    },
    total=False,
)

ThresholdV2TypeDef = TypedDict(
    "ThresholdV2TypeDef",
    {
        "Comparison": str,
        "ThresholdValue": float,
    },
    total=False,
)

TrafficDistributionGroupSummaryTypeDef = TypedDict(
    "TrafficDistributionGroupSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "InstanceArn": str,
        "Status": TrafficDistributionGroupStatusType,
    },
    total=False,
)

TrafficDistributionGroupTypeDef = TypedDict(
    "TrafficDistributionGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "InstanceArn": str,
        "Status": TrafficDistributionGroupStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredTransferContactRequestRequestTypeDef = TypedDict(
    "_RequiredTransferContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ContactFlowId": str,
    },
)
_OptionalTransferContactRequestRequestTypeDef = TypedDict(
    "_OptionalTransferContactRequestRequestTypeDef",
    {
        "QueueId": str,
        "UserId": str,
        "ClientToken": str,
    },
    total=False,
)


class TransferContactRequestRequestTypeDef(
    _RequiredTransferContactRequestRequestTypeDef, _OptionalTransferContactRequestRequestTypeDef
):
    pass


TransferContactResponseTypeDef = TypedDict(
    "TransferContactResponseTypeDef",
    {
        "ContactId": str,
        "ContactArn": str,
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

_RequiredUpdateAgentStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AgentStatusId": str,
    },
)
_OptionalUpdateAgentStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentStatusRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "State": AgentStatusStateType,
        "DisplayOrder": int,
        "ResetOrderNumber": bool,
    },
    total=False,
)


class UpdateAgentStatusRequestRequestTypeDef(
    _RequiredUpdateAgentStatusRequestRequestTypeDef, _OptionalUpdateAgentStatusRequestRequestTypeDef
):
    pass


UpdateContactAttributesRequestRequestTypeDef = TypedDict(
    "UpdateContactAttributesRequestRequestTypeDef",
    {
        "InitialContactId": str,
        "InstanceId": str,
        "Attributes": Mapping[str, str],
    },
)

_RequiredUpdateContactEvaluationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactEvaluationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationId": str,
    },
)
_OptionalUpdateContactEvaluationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactEvaluationRequestRequestTypeDef",
    {
        "Answers": Mapping[str, "EvaluationAnswerInputTypeDef"],
        "Notes": Mapping[str, "EvaluationNoteTypeDef"],
    },
    total=False,
)


class UpdateContactEvaluationRequestRequestTypeDef(
    _RequiredUpdateContactEvaluationRequestRequestTypeDef,
    _OptionalUpdateContactEvaluationRequestRequestTypeDef,
):
    pass


UpdateContactEvaluationResponseTypeDef = TypedDict(
    "UpdateContactEvaluationResponseTypeDef",
    {
        "EvaluationId": str,
        "EvaluationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContactFlowContentRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowContentRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Content": str,
    },
)

_RequiredUpdateContactFlowMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactFlowMetadataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)
_OptionalUpdateContactFlowMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactFlowMetadataRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ContactFlowState": ContactFlowStateType,
    },
    total=False,
)


class UpdateContactFlowMetadataRequestRequestTypeDef(
    _RequiredUpdateContactFlowMetadataRequestRequestTypeDef,
    _OptionalUpdateContactFlowMetadataRequestRequestTypeDef,
):
    pass


UpdateContactFlowModuleContentRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowModuleContentRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
        "Content": str,
    },
)

_RequiredUpdateContactFlowModuleMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactFlowModuleMetadataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
    },
)
_OptionalUpdateContactFlowModuleMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactFlowModuleMetadataRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "State": ContactFlowModuleStateType,
    },
    total=False,
)


class UpdateContactFlowModuleMetadataRequestRequestTypeDef(
    _RequiredUpdateContactFlowModuleMetadataRequestRequestTypeDef,
    _OptionalUpdateContactFlowModuleMetadataRequestRequestTypeDef,
):
    pass


_RequiredUpdateContactFlowNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactFlowNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)
_OptionalUpdateContactFlowNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactFlowNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateContactFlowNameRequestRequestTypeDef(
    _RequiredUpdateContactFlowNameRequestRequestTypeDef,
    _OptionalUpdateContactFlowNameRequestRequestTypeDef,
):
    pass


_RequiredUpdateContactRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
    },
)
_OptionalUpdateContactRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "References": Mapping[str, "ReferenceTypeDef"],
    },
    total=False,
)


class UpdateContactRequestRequestTypeDef(
    _RequiredUpdateContactRequestRequestTypeDef, _OptionalUpdateContactRequestRequestTypeDef
):
    pass


UpdateContactScheduleRequestRequestTypeDef = TypedDict(
    "UpdateContactScheduleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ScheduledTime": Union[datetime, str],
    },
)

_RequiredUpdateEvaluationFormRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEvaluationFormRequestRequestTypeDef",
    {
        "InstanceId": str,
        "EvaluationFormId": str,
        "EvaluationFormVersion": int,
        "Title": str,
        "Items": Sequence["EvaluationFormItemTypeDef"],
    },
)
_OptionalUpdateEvaluationFormRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEvaluationFormRequestRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Description": str,
        "ScoringStrategy": "EvaluationFormScoringStrategyTypeDef",
        "ClientToken": str,
    },
    total=False,
)


class UpdateEvaluationFormRequestRequestTypeDef(
    _RequiredUpdateEvaluationFormRequestRequestTypeDef,
    _OptionalUpdateEvaluationFormRequestRequestTypeDef,
):
    pass


UpdateEvaluationFormResponseTypeDef = TypedDict(
    "UpdateEvaluationFormResponseTypeDef",
    {
        "EvaluationFormId": str,
        "EvaluationFormArn": str,
        "EvaluationFormVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)
_OptionalUpdateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateHoursOfOperationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "TimeZone": str,
        "Config": Sequence["HoursOfOperationConfigTypeDef"],
    },
    total=False,
)


class UpdateHoursOfOperationRequestRequestTypeDef(
    _RequiredUpdateHoursOfOperationRequestRequestTypeDef,
    _OptionalUpdateHoursOfOperationRequestRequestTypeDef,
):
    pass


UpdateInstanceAttributeRequestRequestTypeDef = TypedDict(
    "UpdateInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
)

UpdateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "UpdateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

UpdateParticipantRoleConfigChannelInfoTypeDef = TypedDict(
    "UpdateParticipantRoleConfigChannelInfoTypeDef",
    {
        "Chat": "ChatParticipantRoleConfigTypeDef",
    },
    total=False,
)

UpdateParticipantRoleConfigRequestRequestTypeDef = TypedDict(
    "UpdateParticipantRoleConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ChannelConfiguration": "UpdateParticipantRoleConfigChannelInfoTypeDef",
    },
)

_RequiredUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "TargetArn": str,
    },
)
_OptionalUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class UpdatePhoneNumberRequestRequestTypeDef(
    _RequiredUpdatePhoneNumberRequestRequestTypeDef, _OptionalUpdatePhoneNumberRequestRequestTypeDef
):
    pass


UpdatePhoneNumberResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumberId": str,
        "PhoneNumberArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePromptRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePromptRequestRequestTypeDef",
    {
        "InstanceId": str,
        "PromptId": str,
    },
)
_OptionalUpdatePromptRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePromptRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "S3Uri": str,
    },
    total=False,
)


class UpdatePromptRequestRequestTypeDef(
    _RequiredUpdatePromptRequestRequestTypeDef, _OptionalUpdatePromptRequestRequestTypeDef
):
    pass


UpdatePromptResponseTypeDef = TypedDict(
    "UpdatePromptResponseTypeDef",
    {
        "PromptARN": str,
        "PromptId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateQueueHoursOfOperationRequestRequestTypeDef = TypedDict(
    "UpdateQueueHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "HoursOfOperationId": str,
    },
)

_RequiredUpdateQueueMaxContactsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueMaxContactsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalUpdateQueueMaxContactsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueMaxContactsRequestRequestTypeDef",
    {
        "MaxContacts": int,
    },
    total=False,
)


class UpdateQueueMaxContactsRequestRequestTypeDef(
    _RequiredUpdateQueueMaxContactsRequestRequestTypeDef,
    _OptionalUpdateQueueMaxContactsRequestRequestTypeDef,
):
    pass


_RequiredUpdateQueueNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalUpdateQueueNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateQueueNameRequestRequestTypeDef(
    _RequiredUpdateQueueNameRequestRequestTypeDef, _OptionalUpdateQueueNameRequestRequestTypeDef
):
    pass


UpdateQueueOutboundCallerConfigRequestRequestTypeDef = TypedDict(
    "UpdateQueueOutboundCallerConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
    },
)

UpdateQueueStatusRequestRequestTypeDef = TypedDict(
    "UpdateQueueStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "Status": QueueStatusType,
    },
)

UpdateQuickConnectConfigRequestRequestTypeDef = TypedDict(
    "UpdateQuickConnectConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)

_RequiredUpdateQuickConnectNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQuickConnectNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)
_OptionalUpdateQuickConnectNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQuickConnectNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateQuickConnectNameRequestRequestTypeDef(
    _RequiredUpdateQuickConnectNameRequestRequestTypeDef,
    _OptionalUpdateQuickConnectNameRequestRequestTypeDef,
):
    pass


UpdateRoutingProfileConcurrencyRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileConcurrencyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "MediaConcurrencies": Sequence["MediaConcurrencyTypeDef"],
    },
)

UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "DefaultOutboundQueueId": str,
    },
)

_RequiredUpdateRoutingProfileNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoutingProfileNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalUpdateRoutingProfileNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoutingProfileNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateRoutingProfileNameRequestRequestTypeDef(
    _RequiredUpdateRoutingProfileNameRequestRequestTypeDef,
    _OptionalUpdateRoutingProfileNameRequestRequestTypeDef,
):
    pass


UpdateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": Sequence["RoutingProfileQueueConfigTypeDef"],
    },
)

UpdateRuleRequestRequestTypeDef = TypedDict(
    "UpdateRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "InstanceId": str,
        "Name": str,
        "Function": str,
        "Actions": Sequence["RuleActionTypeDef"],
        "PublishStatus": RulePublishStatusType,
    },
)

_RequiredUpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
    },
)
_OptionalUpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityProfileRequestRequestTypeDef",
    {
        "Description": str,
        "Permissions": Sequence[str],
        "AllowedAccessControlTags": Mapping[str, str],
        "TagRestrictedResources": Sequence[str],
    },
    total=False,
)


class UpdateSecurityProfileRequestRequestTypeDef(
    _RequiredUpdateSecurityProfileRequestRequestTypeDef,
    _OptionalUpdateSecurityProfileRequestRequestTypeDef,
):
    pass


_RequiredUpdateTaskTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTaskTemplateRequestRequestTypeDef",
    {
        "TaskTemplateId": str,
        "InstanceId": str,
    },
)
_OptionalUpdateTaskTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTaskTemplateRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ContactFlowId": str,
        "Constraints": "TaskTemplateConstraintsTypeDef",
        "Defaults": "TaskTemplateDefaultsTypeDef",
        "Status": TaskTemplateStatusType,
        "Fields": Sequence["TaskTemplateFieldTypeDef"],
    },
    total=False,
)


class UpdateTaskTemplateRequestRequestTypeDef(
    _RequiredUpdateTaskTemplateRequestRequestTypeDef,
    _OptionalUpdateTaskTemplateRequestRequestTypeDef,
):
    pass


UpdateTaskTemplateResponseTypeDef = TypedDict(
    "UpdateTaskTemplateResponseTypeDef",
    {
        "InstanceId": str,
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "ContactFlowId": str,
        "Constraints": "TaskTemplateConstraintsOutputTypeDef",
        "Defaults": "TaskTemplateDefaultsOutputTypeDef",
        "Fields": List["TaskTemplateFieldOutputTypeDef"],
        "Status": TaskTemplateStatusType,
        "LastModifiedTime": datetime,
        "CreatedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrafficDistributionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrafficDistributionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateTrafficDistributionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrafficDistributionRequestRequestTypeDef",
    {
        "TelephonyConfig": "TelephonyConfigTypeDef",
    },
    total=False,
)


class UpdateTrafficDistributionRequestRequestTypeDef(
    _RequiredUpdateTrafficDistributionRequestRequestTypeDef,
    _OptionalUpdateTrafficDistributionRequestRequestTypeDef,
):
    pass


UpdateUserHierarchyGroupNameRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyGroupNameRequestRequestTypeDef",
    {
        "Name": str,
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

_RequiredUpdateUserHierarchyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserHierarchyRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)
_OptionalUpdateUserHierarchyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserHierarchyRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
    },
    total=False,
)


class UpdateUserHierarchyRequestRequestTypeDef(
    _RequiredUpdateUserHierarchyRequestRequestTypeDef,
    _OptionalUpdateUserHierarchyRequestRequestTypeDef,
):
    pass


UpdateUserHierarchyStructureRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyStructureRequestRequestTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureUpdateTypeDef",
        "InstanceId": str,
    },
)

UpdateUserIdentityInfoRequestRequestTypeDef = TypedDict(
    "UpdateUserIdentityInfoRequestRequestTypeDef",
    {
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserPhoneConfigRequestRequestTypeDef = TypedDict(
    "UpdateUserPhoneConfigRequestRequestTypeDef",
    {
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserRoutingProfileRequestRequestTypeDef = TypedDict(
    "UpdateUserRoutingProfileRequestRequestTypeDef",
    {
        "RoutingProfileId": str,
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserSecurityProfilesRequestRequestTypeDef = TypedDict(
    "UpdateUserSecurityProfilesRequestRequestTypeDef",
    {
        "SecurityProfileIds": Sequence[str],
        "UserId": str,
        "InstanceId": str,
    },
)

UrlReferenceTypeDef = TypedDict(
    "UrlReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

UseCaseTypeDef = TypedDict(
    "UseCaseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "UseCaseType": UseCaseTypeType,
    },
    total=False,
)

UserDataFiltersTypeDef = TypedDict(
    "UserDataFiltersTypeDef",
    {
        "Queues": Sequence[str],
        "ContactFilter": "ContactFilterTypeDef",
        "RoutingProfiles": Sequence[str],
        "Agents": Sequence[str],
        "UserHierarchyGroups": Sequence[str],
    },
    total=False,
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "User": "UserReferenceTypeDef",
        "RoutingProfile": "RoutingProfileReferenceTypeDef",
        "HierarchyPath": "HierarchyPathReferenceTypeDef",
        "Status": "AgentStatusReferenceTypeDef",
        "AvailableSlotsByChannel": Dict[ChannelType, int],
        "MaxSlotsByChannel": Dict[ChannelType, int],
        "ActiveSlotsByChannel": Dict[ChannelType, int],
        "Contacts": List["AgentContactReferenceTypeDef"],
        "NextStatus": str,
    },
    total=False,
)

UserIdentityInfoLiteTypeDef = TypedDict(
    "UserIdentityInfoLiteTypeDef",
    {
        "FirstName": str,
        "LastName": str,
    },
    total=False,
)

UserIdentityInfoOutputTypeDef = TypedDict(
    "UserIdentityInfoOutputTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "SecondaryEmail": str,
        "Mobile": str,
    },
    total=False,
)

UserIdentityInfoTypeDef = TypedDict(
    "UserIdentityInfoTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "SecondaryEmail": str,
        "Mobile": str,
    },
    total=False,
)

_RequiredUserPhoneConfigOutputTypeDef = TypedDict(
    "_RequiredUserPhoneConfigOutputTypeDef",
    {
        "PhoneType": PhoneTypeType,
    },
)
_OptionalUserPhoneConfigOutputTypeDef = TypedDict(
    "_OptionalUserPhoneConfigOutputTypeDef",
    {
        "AutoAccept": bool,
        "AfterContactWorkTimeLimit": int,
        "DeskPhoneNumber": str,
    },
    total=False,
)


class UserPhoneConfigOutputTypeDef(
    _RequiredUserPhoneConfigOutputTypeDef, _OptionalUserPhoneConfigOutputTypeDef
):
    pass


_RequiredUserPhoneConfigTypeDef = TypedDict(
    "_RequiredUserPhoneConfigTypeDef",
    {
        "PhoneType": PhoneTypeType,
    },
)
_OptionalUserPhoneConfigTypeDef = TypedDict(
    "_OptionalUserPhoneConfigTypeDef",
    {
        "AutoAccept": bool,
        "AfterContactWorkTimeLimit": int,
        "DeskPhoneNumber": str,
    },
    total=False,
)


class UserPhoneConfigTypeDef(_RequiredUserPhoneConfigTypeDef, _OptionalUserPhoneConfigTypeDef):
    pass


UserQuickConnectConfigOutputTypeDef = TypedDict(
    "UserQuickConnectConfigOutputTypeDef",
    {
        "UserId": str,
        "ContactFlowId": str,
    },
)

UserQuickConnectConfigTypeDef = TypedDict(
    "UserQuickConnectConfigTypeDef",
    {
        "UserId": str,
        "ContactFlowId": str,
    },
)

UserReferenceTypeDef = TypedDict(
    "UserReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

UserSearchCriteriaTypeDef = TypedDict(
    "UserSearchCriteriaTypeDef",
    {
        "OrConditions": Sequence[Dict[str, Any]],
        "AndConditions": Sequence[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
        "HierarchyGroupCondition": "HierarchyGroupConditionTypeDef",
    },
    total=False,
)

UserSearchFilterTypeDef = TypedDict(
    "UserSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

UserSearchSummaryTypeDef = TypedDict(
    "UserSearchSummaryTypeDef",
    {
        "Arn": str,
        "DirectoryUserId": str,
        "HierarchyGroupId": str,
        "Id": str,
        "IdentityInfo": "UserIdentityInfoLiteTypeDef",
        "PhoneConfig": "UserPhoneConfigOutputTypeDef",
        "RoutingProfileId": str,
        "SecurityProfileIds": List[str],
        "Tags": Dict[str, str],
        "Username": str,
    },
    total=False,
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
        "IdentityInfo": "UserIdentityInfoOutputTypeDef",
        "PhoneConfig": "UserPhoneConfigOutputTypeDef",
        "DirectoryUserId": str,
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredVocabularySummaryTypeDef = TypedDict(
    "_RequiredVocabularySummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Arn": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "State": VocabularyStateType,
        "LastModifiedTime": datetime,
    },
)
_OptionalVocabularySummaryTypeDef = TypedDict(
    "_OptionalVocabularySummaryTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class VocabularySummaryTypeDef(
    _RequiredVocabularySummaryTypeDef, _OptionalVocabularySummaryTypeDef
):
    pass


_RequiredVocabularyTypeDef = TypedDict(
    "_RequiredVocabularyTypeDef",
    {
        "Name": str,
        "Id": str,
        "Arn": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "State": VocabularyStateType,
        "LastModifiedTime": datetime,
    },
)
_OptionalVocabularyTypeDef = TypedDict(
    "_OptionalVocabularyTypeDef",
    {
        "FailureReason": str,
        "Content": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class VocabularyTypeDef(_RequiredVocabularyTypeDef, _OptionalVocabularyTypeDef):
    pass


VoiceRecordingConfigurationTypeDef = TypedDict(
    "VoiceRecordingConfigurationTypeDef",
    {
        "VoiceRecordingTrack": VoiceRecordingTrackType,
    },
    total=False,
)

WisdomInfoTypeDef = TypedDict(
    "WisdomInfoTypeDef",
    {
        "SessionArn": str,
    },
    total=False,
)
