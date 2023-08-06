"""
Type annotations for lexv2-models service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/type_defs/)

Usage::

    ```python
    from mypy_boto3_lexv2_models.type_defs import ActiveContextTypeDef

    data: ActiveContextTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AggregatedUtterancesFilterOperatorType,
    AggregatedUtterancesSortAttributeType,
    AnalyticsBinByNameType,
    AnalyticsCommonFilterNameType,
    AnalyticsFilterOperatorType,
    AnalyticsIntentFieldType,
    AnalyticsIntentFilterNameType,
    AnalyticsIntentMetricNameType,
    AnalyticsIntentStageFieldType,
    AnalyticsIntentStageFilterNameType,
    AnalyticsIntentStageMetricNameType,
    AnalyticsIntervalType,
    AnalyticsMetricStatisticType,
    AnalyticsModalityType,
    AnalyticsNodeTypeType,
    AnalyticsSessionFieldType,
    AnalyticsSessionFilterNameType,
    AnalyticsSessionMetricNameType,
    AnalyticsSessionSortByNameType,
    AnalyticsSortOrderType,
    AnalyticsUtteranceFieldType,
    AnalyticsUtteranceFilterNameType,
    AnalyticsUtteranceMetricNameType,
    AssociatedTranscriptFilterNameType,
    BotAliasStatusType,
    BotFilterNameType,
    BotFilterOperatorType,
    BotLocaleFilterOperatorType,
    BotLocaleStatusType,
    BotRecommendationStatusType,
    BotStatusType,
    BotTypeType,
    ConversationEndStateType,
    ConversationLogsInputModeFilterType,
    CustomVocabularyStatusType,
    DialogActionTypeType,
    EffectType,
    ErrorCodeType,
    ExportFilterOperatorType,
    ExportStatusType,
    ImportExportFileFormatType,
    ImportFilterOperatorType,
    ImportResourceTypeType,
    ImportStatusType,
    IntentFilterOperatorType,
    IntentSortAttributeType,
    IntentStateType,
    MergeStrategyType,
    MessageSelectionStrategyType,
    ObfuscationSettingTypeType,
    PromptAttemptType,
    SearchOrderType,
    SlotConstraintType,
    SlotFilterOperatorType,
    SlotShapeType,
    SlotSortAttributeType,
    SlotTypeCategoryType,
    SlotTypeFilterNameType,
    SlotTypeFilterOperatorType,
    SlotTypeSortAttributeType,
    SlotValueResolutionStrategyType,
    SortOrderType,
    TestExecutionApiModeType,
    TestExecutionModalityType,
    TestExecutionSortAttributeType,
    TestExecutionStatusType,
    TestResultMatchStatusType,
    TestResultTypeFilterType,
    TestSetDiscrepancyReportStatusType,
    TestSetGenerationStatusType,
    TestSetModalityType,
    TestSetSortAttributeType,
    TestSetStatusType,
    TimeDimensionType,
    UtteranceContentTypeType,
    VoiceEngineType,
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
    "ActiveContextTypeDef",
    "AdvancedRecognitionSettingOutputTypeDef",
    "AdvancedRecognitionSettingTypeDef",
    "ExecutionErrorDetailsTypeDef",
    "AgentTurnSpecificationTypeDef",
    "AggregatedUtterancesFilterTypeDef",
    "AggregatedUtterancesSortByTypeDef",
    "AggregatedUtterancesSummaryTypeDef",
    "AllowedInputTypesOutputTypeDef",
    "AllowedInputTypesTypeDef",
    "AnalyticsBinBySpecificationTypeDef",
    "AnalyticsBinKeyTypeDef",
    "AnalyticsIntentFilterTypeDef",
    "AnalyticsIntentGroupByKeyTypeDef",
    "AnalyticsIntentGroupBySpecificationTypeDef",
    "AnalyticsIntentMetricResultTypeDef",
    "AnalyticsIntentMetricTypeDef",
    "AnalyticsIntentNodeSummaryTypeDef",
    "AnalyticsIntentStageFilterTypeDef",
    "AnalyticsIntentStageGroupByKeyTypeDef",
    "AnalyticsIntentStageGroupBySpecificationTypeDef",
    "AnalyticsIntentStageMetricResultTypeDef",
    "AnalyticsIntentStageMetricTypeDef",
    "AnalyticsPathFilterTypeDef",
    "AnalyticsSessionFilterTypeDef",
    "AnalyticsSessionGroupByKeyTypeDef",
    "AnalyticsSessionGroupBySpecificationTypeDef",
    "AnalyticsSessionMetricResultTypeDef",
    "AnalyticsSessionMetricTypeDef",
    "AnalyticsUtteranceAttributeResultTypeDef",
    "AnalyticsUtteranceAttributeTypeDef",
    "AnalyticsUtteranceFilterTypeDef",
    "AnalyticsUtteranceGroupByKeyTypeDef",
    "AnalyticsUtteranceGroupBySpecificationTypeDef",
    "AnalyticsUtteranceMetricResultTypeDef",
    "AnalyticsUtteranceMetricTypeDef",
    "AssociatedTranscriptFilterTypeDef",
    "AssociatedTranscriptTypeDef",
    "AudioSpecificationOutputTypeDef",
    "DTMFSpecificationOutputTypeDef",
    "AudioSpecificationTypeDef",
    "DTMFSpecificationTypeDef",
    "S3BucketLogDestinationOutputTypeDef",
    "S3BucketLogDestinationTypeDef",
    "NewCustomVocabularyItemTypeDef",
    "CustomVocabularyItemOutputTypeDef",
    "FailedCustomVocabularyItemTypeDef",
    "CustomVocabularyEntryIdTypeDef",
    "CustomVocabularyItemTypeDef",
    "BotAliasHistoryEventTypeDef",
    "BotAliasSummaryTypeDef",
    "BotAliasTestExecutionTargetOutputTypeDef",
    "BotAliasTestExecutionTargetTypeDef",
    "BotExportSpecificationOutputTypeDef",
    "BotExportSpecificationTypeDef",
    "BotFilterTypeDef",
    "DataPrivacyOutputTypeDef",
    "DataPrivacyTypeDef",
    "BotLocaleExportSpecificationOutputTypeDef",
    "BotLocaleExportSpecificationTypeDef",
    "BotLocaleFilterTypeDef",
    "BotLocaleHistoryEventTypeDef",
    "VoiceSettingsOutputTypeDef",
    "VoiceSettingsTypeDef",
    "BotLocaleSortByTypeDef",
    "BotLocaleSummaryTypeDef",
    "BotMemberOutputTypeDef",
    "BotMemberTypeDef",
    "IntentStatisticsTypeDef",
    "SlotTypeStatisticsTypeDef",
    "BotRecommendationSummaryTypeDef",
    "BotSortByTypeDef",
    "BotSummaryTypeDef",
    "BotVersionLocaleDetailsOutputTypeDef",
    "BotVersionLocaleDetailsTypeDef",
    "BotVersionSortByTypeDef",
    "BotVersionSummaryTypeDef",
    "BuildBotLocaleRequestRequestTypeDef",
    "BuildBotLocaleResponseTypeDef",
    "BuiltInIntentSortByTypeDef",
    "BuiltInIntentSummaryTypeDef",
    "BuiltInSlotTypeSortByTypeDef",
    "BuiltInSlotTypeSummaryTypeDef",
    "ButtonOutputTypeDef",
    "ButtonTypeDef",
    "CloudWatchLogGroupLogDestinationOutputTypeDef",
    "CloudWatchLogGroupLogDestinationTypeDef",
    "LambdaCodeHookOutputTypeDef",
    "LambdaCodeHookTypeDef",
    "SubSlotTypeCompositionOutputTypeDef",
    "SubSlotTypeCompositionTypeDef",
    "ConditionOutputTypeDef",
    "ConditionTypeDef",
    "ConversationLevelIntentClassificationResultItemTypeDef",
    "ConversationLevelResultDetailTypeDef",
    "ConversationLevelSlotResolutionResultItemTypeDef",
    "ConversationLevelTestResultsFilterByTypeDef",
    "ConversationLogsDataSourceFilterByOutputTypeDef",
    "ConversationLogsDataSourceFilterByTypeDef",
    "SentimentAnalysisSettingsTypeDef",
    "SentimentAnalysisSettingsOutputTypeDef",
    "DialogCodeHookSettingsTypeDef",
    "InputContextTypeDef",
    "KendraConfigurationTypeDef",
    "OutputContextTypeDef",
    "SampleUtteranceTypeDef",
    "DialogCodeHookSettingsOutputTypeDef",
    "InputContextOutputTypeDef",
    "KendraConfigurationOutputTypeDef",
    "OutputContextOutputTypeDef",
    "SampleUtteranceOutputTypeDef",
    "CreateResourcePolicyRequestRequestTypeDef",
    "CreateResourcePolicyResponseTypeDef",
    "PrincipalTypeDef",
    "CreateResourcePolicyStatementResponseTypeDef",
    "MultipleValuesSettingTypeDef",
    "ObfuscationSettingTypeDef",
    "MultipleValuesSettingOutputTypeDef",
    "ObfuscationSettingOutputTypeDef",
    "CreateUploadUrlResponseTypeDef",
    "CustomPayloadOutputTypeDef",
    "CustomPayloadTypeDef",
    "CustomVocabularyExportSpecificationOutputTypeDef",
    "CustomVocabularyExportSpecificationTypeDef",
    "CustomVocabularyImportSpecificationOutputTypeDef",
    "CustomVocabularyImportSpecificationTypeDef",
    "DateRangeFilterOutputTypeDef",
    "DateRangeFilterTypeDef",
    "DeleteBotAliasRequestRequestTypeDef",
    "DeleteBotAliasResponseTypeDef",
    "DeleteBotLocaleRequestRequestTypeDef",
    "DeleteBotLocaleResponseTypeDef",
    "DeleteBotRequestRequestTypeDef",
    "DeleteBotResponseTypeDef",
    "DeleteBotVersionRequestRequestTypeDef",
    "DeleteBotVersionResponseTypeDef",
    "DeleteCustomVocabularyRequestRequestTypeDef",
    "DeleteCustomVocabularyResponseTypeDef",
    "DeleteExportRequestRequestTypeDef",
    "DeleteExportResponseTypeDef",
    "DeleteImportRequestRequestTypeDef",
    "DeleteImportResponseTypeDef",
    "DeleteIntentRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "DeleteResourcePolicyStatementRequestRequestTypeDef",
    "DeleteResourcePolicyStatementResponseTypeDef",
    "DeleteSlotRequestRequestTypeDef",
    "DeleteSlotTypeRequestRequestTypeDef",
    "DeleteTestSetRequestRequestTypeDef",
    "DeleteUtterancesRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeBotAliasRequestRequestTypeDef",
    "ParentBotNetworkTypeDef",
    "DescribeBotLocaleRequestRequestTypeDef",
    "DescribeBotRecommendationRequestRequestTypeDef",
    "EncryptionSettingOutputTypeDef",
    "DescribeBotRequestRequestTypeDef",
    "DescribeBotVersionRequestRequestTypeDef",
    "DescribeCustomVocabularyMetadataRequestRequestTypeDef",
    "DescribeCustomVocabularyMetadataResponseTypeDef",
    "DescribeExportRequestRequestTypeDef",
    "DescribeImportRequestRequestTypeDef",
    "DescribeIntentRequestRequestTypeDef",
    "SlotPriorityOutputTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeSlotRequestRequestTypeDef",
    "DescribeSlotTypeRequestRequestTypeDef",
    "DescribeTestExecutionRequestRequestTypeDef",
    "DescribeTestSetDiscrepancyReportRequestRequestTypeDef",
    "DescribeTestSetGenerationRequestRequestTypeDef",
    "TestSetStorageLocationOutputTypeDef",
    "DescribeTestSetRequestRequestTypeDef",
    "DialogActionOutputTypeDef",
    "DialogActionTypeDef",
    "IntentOverrideOutputTypeDef",
    "IntentOverrideTypeDef",
    "ElicitationCodeHookInvocationSettingOutputTypeDef",
    "ElicitationCodeHookInvocationSettingTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionSettingTypeDef",
    "ExportFilterTypeDef",
    "TestSetExportSpecificationOutputTypeDef",
    "TestSetExportSpecificationTypeDef",
    "ExportSortByTypeDef",
    "GetTestExecutionArtifactsUrlRequestRequestTypeDef",
    "GetTestExecutionArtifactsUrlResponseTypeDef",
    "GrammarSlotTypeSourceOutputTypeDef",
    "GrammarSlotTypeSourceTypeDef",
    "ImportFilterTypeDef",
    "ImportSortByTypeDef",
    "ImportSummaryTypeDef",
    "RuntimeHintsTypeDef",
    "IntentClassificationTestResultItemCountsTypeDef",
    "IntentFilterTypeDef",
    "IntentSortByTypeDef",
    "InvokedIntentSampleTypeDef",
    "ListBotAliasesRequestRequestTypeDef",
    "ListBotRecommendationsRequestRequestTypeDef",
    "ListCustomVocabularyItemsRequestRequestTypeDef",
    "ListRecommendedIntentsRequestRequestTypeDef",
    "RecommendedIntentSummaryTypeDef",
    "SessionDataSortByTypeDef",
    "SlotTypeFilterTypeDef",
    "SlotTypeSortByTypeDef",
    "SlotTypeSummaryTypeDef",
    "SlotFilterTypeDef",
    "SlotSortByTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TestExecutionSortByTypeDef",
    "ListTestSetRecordsRequestRequestTypeDef",
    "TestSetSortByTypeDef",
    "UtteranceDataSortByTypeDef",
    "PlainTextMessageOutputTypeDef",
    "SSMLMessageOutputTypeDef",
    "PlainTextMessageTypeDef",
    "SSMLMessageTypeDef",
    "OverallTestResultItemTypeDef",
    "PathFormatOutputTypeDef",
    "PathFormatTypeDef",
    "TextInputSpecificationOutputTypeDef",
    "TextInputSpecificationTypeDef",
    "RelativeAggregationDurationOutputTypeDef",
    "RelativeAggregationDurationTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeHintValueTypeDef",
    "SampleValueOutputTypeDef",
    "SampleValueTypeDef",
    "SlotDefaultValueOutputTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotPriorityTypeDef",
    "SlotResolutionTestResultItemCountsTypeDef",
    "SlotValueOutputTypeDef",
    "SlotValueTypeDef",
    "SlotValueRegexFilterOutputTypeDef",
    "SlotValueRegexFilterTypeDef",
    "TestSetStorageLocationTypeDef",
    "StopBotRecommendationRequestRequestTypeDef",
    "StopBotRecommendationResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestSetIntentDiscrepancyItemTypeDef",
    "TestSetSlotDiscrepancyItemTypeDef",
    "TestSetDiscrepancyReportBotAliasTargetOutputTypeDef",
    "TestSetDiscrepancyReportBotAliasTargetTypeDef",
    "TestSetImportInputLocationOutputTypeDef",
    "TestSetImportInputLocationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateExportRequestRequestTypeDef",
    "UpdateResourcePolicyRequestRequestTypeDef",
    "UpdateResourcePolicyResponseTypeDef",
    "UpdateTestSetRequestRequestTypeDef",
    "UserTurnIntentOutputTypeDef",
    "UserTurnSlotOutputTypeDef",
    "UtteranceAudioInputSpecificationTypeDef",
    "AgentTurnResultTypeDef",
    "AnalyticsIntentResultTypeDef",
    "ListIntentMetricsRequestRequestTypeDef",
    "ListIntentPathsResponseTypeDef",
    "AnalyticsIntentStageResultTypeDef",
    "ListIntentStageMetricsRequestRequestTypeDef",
    "ListIntentPathsRequestRequestTypeDef",
    "AnalyticsSessionResultTypeDef",
    "ListSessionMetricsRequestRequestTypeDef",
    "AnalyticsUtteranceResultTypeDef",
    "ListUtteranceMetricsRequestRequestTypeDef",
    "SearchAssociatedTranscriptsRequestRequestTypeDef",
    "SearchAssociatedTranscriptsResponseTypeDef",
    "AudioAndDTMFInputSpecificationOutputTypeDef",
    "AudioAndDTMFInputSpecificationTypeDef",
    "AudioLogDestinationOutputTypeDef",
    "AudioLogDestinationTypeDef",
    "BatchCreateCustomVocabularyItemRequestRequestTypeDef",
    "ListCustomVocabularyItemsResponseTypeDef",
    "BatchCreateCustomVocabularyItemResponseTypeDef",
    "BatchDeleteCustomVocabularyItemResponseTypeDef",
    "BatchUpdateCustomVocabularyItemResponseTypeDef",
    "BatchDeleteCustomVocabularyItemRequestRequestTypeDef",
    "BatchUpdateCustomVocabularyItemRequestRequestTypeDef",
    "ListBotAliasesResponseTypeDef",
    "TestExecutionTargetOutputTypeDef",
    "TestExecutionTargetTypeDef",
    "BotImportSpecificationOutputTypeDef",
    "BotImportSpecificationTypeDef",
    "BotLocaleImportSpecificationOutputTypeDef",
    "CreateBotLocaleResponseTypeDef",
    "DescribeBotLocaleResponseTypeDef",
    "UpdateBotLocaleResponseTypeDef",
    "BotLocaleImportSpecificationTypeDef",
    "CreateBotLocaleRequestRequestTypeDef",
    "UpdateBotLocaleRequestRequestTypeDef",
    "ListBotLocalesRequestRequestTypeDef",
    "ListBotLocalesResponseTypeDef",
    "CreateBotResponseTypeDef",
    "DescribeBotResponseTypeDef",
    "UpdateBotResponseTypeDef",
    "CreateBotRequestRequestTypeDef",
    "UpdateBotRequestRequestTypeDef",
    "BotRecommendationResultStatisticsTypeDef",
    "ListBotRecommendationsResponseTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateBotVersionRequestRequestTypeDef",
    "ListBotVersionsRequestRequestTypeDef",
    "ListBotVersionsResponseTypeDef",
    "ListBuiltInIntentsRequestRequestTypeDef",
    "ListBuiltInIntentsResponseTypeDef",
    "ListBuiltInSlotTypesRequestRequestTypeDef",
    "ListBuiltInSlotTypesResponseTypeDef",
    "ImageResponseCardOutputTypeDef",
    "ImageResponseCardTypeDef",
    "TextLogDestinationOutputTypeDef",
    "TextLogDestinationTypeDef",
    "CodeHookSpecificationOutputTypeDef",
    "CodeHookSpecificationTypeDef",
    "CompositeSlotTypeSettingOutputTypeDef",
    "CompositeSlotTypeSettingTypeDef",
    "ConversationLevelTestResultItemTypeDef",
    "TestExecutionResultFilterByTypeDef",
    "ConversationLogsDataSourceOutputTypeDef",
    "ConversationLogsDataSourceTypeDef",
    "IntentSummaryTypeDef",
    "CreateResourcePolicyStatementRequestRequestTypeDef",
    "LexTranscriptFilterOutputTypeDef",
    "LexTranscriptFilterTypeDef",
    "DescribeBotAliasRequestBotAliasAvailableWaitTypeDef",
    "DescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef",
    "DescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef",
    "DescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef",
    "DescribeBotRequestBotAvailableWaitTypeDef",
    "DescribeBotVersionRequestBotVersionAvailableWaitTypeDef",
    "DescribeExportRequestBotExportCompletedWaitTypeDef",
    "DescribeImportRequestBotImportCompletedWaitTypeDef",
    "DescribeBotVersionResponseTypeDef",
    "DescribeTestSetResponseTypeDef",
    "TestSetSummaryTypeDef",
    "UpdateTestSetResponseTypeDef",
    "DialogStateOutputTypeDef",
    "DialogStateTypeDef",
    "UpdateBotRecommendationRequestRequestTypeDef",
    "ExportResourceSpecificationOutputTypeDef",
    "ExportResourceSpecificationTypeDef",
    "ListExportsRequestRequestTypeDef",
    "GrammarSlotTypeSettingOutputTypeDef",
    "GrammarSlotTypeSettingTypeDef",
    "ListImportsRequestRequestTypeDef",
    "ListImportsResponseTypeDef",
    "InputSessionStateSpecificationTypeDef",
    "IntentClassificationTestResultItemTypeDef",
    "ListIntentsRequestRequestTypeDef",
    "SessionSpecificationTypeDef",
    "ListRecommendedIntentsResponseTypeDef",
    "ListSessionAnalyticsDataRequestRequestTypeDef",
    "ListSlotTypesRequestRequestTypeDef",
    "ListSlotTypesResponseTypeDef",
    "ListSlotsRequestRequestTypeDef",
    "ListTestExecutionsRequestRequestTypeDef",
    "ListTestSetsRequestRequestTypeDef",
    "ListUtteranceAnalyticsDataRequestRequestTypeDef",
    "OverallTestResultsTypeDef",
    "UtteranceAggregationDurationOutputTypeDef",
    "UtteranceAggregationDurationTypeDef",
    "RuntimeHintDetailsTypeDef",
    "SlotTypeValueOutputTypeDef",
    "SlotTypeValueTypeDef",
    "SlotDefaultValueSpecificationOutputTypeDef",
    "SlotDefaultValueSpecificationTypeDef",
    "SlotResolutionTestResultItemTypeDef",
    "SlotValueOverrideOutputTypeDef",
    "SlotValueOverrideTypeDef",
    "SlotValueSelectionSettingOutputTypeDef",
    "SlotValueSelectionSettingTypeDef",
    "TestSetDiscrepancyErrorsTypeDef",
    "TestSetDiscrepancyReportResourceTargetOutputTypeDef",
    "TestSetDiscrepancyReportResourceTargetTypeDef",
    "TestSetImportResourceSpecificationOutputTypeDef",
    "TestSetImportResourceSpecificationTypeDef",
    "UserTurnOutputSpecificationTypeDef",
    "UtteranceInputSpecificationTypeDef",
    "ListIntentMetricsResponseTypeDef",
    "ListIntentStageMetricsResponseTypeDef",
    "ListSessionMetricsResponseTypeDef",
    "ListUtteranceMetricsResponseTypeDef",
    "PromptAttemptSpecificationOutputTypeDef",
    "PromptAttemptSpecificationTypeDef",
    "AudioLogSettingOutputTypeDef",
    "AudioLogSettingTypeDef",
    "DescribeTestExecutionResponseTypeDef",
    "StartTestExecutionResponseTypeDef",
    "TestExecutionSummaryTypeDef",
    "StartTestExecutionRequestRequestTypeDef",
    "BotRecommendationResultsTypeDef",
    "MessageOutputTypeDef",
    "UtteranceBotResponseTypeDef",
    "MessageTypeDef",
    "TextLogSettingOutputTypeDef",
    "TextLogSettingTypeDef",
    "BotAliasLocaleSettingsOutputTypeDef",
    "BotAliasLocaleSettingsTypeDef",
    "ConversationLevelTestResultsTypeDef",
    "ListTestExecutionResultItemsRequestRequestTypeDef",
    "TestSetGenerationDataSourceOutputTypeDef",
    "TestSetGenerationDataSourceTypeDef",
    "ListIntentsResponseTypeDef",
    "TranscriptFilterOutputTypeDef",
    "TranscriptFilterTypeDef",
    "ListTestSetsResponseTypeDef",
    "CreateExportResponseTypeDef",
    "DescribeExportResponseTypeDef",
    "ExportSummaryTypeDef",
    "UpdateExportResponseTypeDef",
    "CreateExportRequestRequestTypeDef",
    "ExternalSourceSettingOutputTypeDef",
    "ExternalSourceSettingTypeDef",
    "IntentClassificationTestResultsTypeDef",
    "ListSessionAnalyticsDataResponseTypeDef",
    "ListAggregatedUtterancesResponseTypeDef",
    "ListAggregatedUtterancesRequestRequestTypeDef",
    "IntentLevelSlotResolutionTestResultItemTypeDef",
    "CreateTestSetDiscrepancyReportResponseTypeDef",
    "DescribeTestSetDiscrepancyReportResponseTypeDef",
    "CreateTestSetDiscrepancyReportRequestRequestTypeDef",
    "ImportResourceSpecificationOutputTypeDef",
    "ImportResourceSpecificationTypeDef",
    "UserTurnInputSpecificationTypeDef",
    "ListTestExecutionsResponseTypeDef",
    "MessageGroupOutputTypeDef",
    "UtteranceSpecificationTypeDef",
    "MessageGroupTypeDef",
    "ConversationLogSettingsOutputTypeDef",
    "ConversationLogSettingsTypeDef",
    "DescribeTestSetGenerationResponseTypeDef",
    "StartTestSetGenerationResponseTypeDef",
    "StartTestSetGenerationRequestRequestTypeDef",
    "S3BucketTranscriptSourceOutputTypeDef",
    "S3BucketTranscriptSourceTypeDef",
    "ListExportsResponseTypeDef",
    "CreateSlotTypeResponseTypeDef",
    "DescribeSlotTypeResponseTypeDef",
    "UpdateSlotTypeResponseTypeDef",
    "CreateSlotTypeRequestRequestTypeDef",
    "UpdateSlotTypeRequestRequestTypeDef",
    "IntentLevelSlotResolutionTestResultsTypeDef",
    "DescribeImportResponseTypeDef",
    "StartImportResponseTypeDef",
    "StartImportRequestRequestTypeDef",
    "UserTurnResultTypeDef",
    "UserTurnSpecificationTypeDef",
    "FulfillmentStartResponseSpecificationOutputTypeDef",
    "FulfillmentUpdateResponseSpecificationOutputTypeDef",
    "PromptSpecificationOutputTypeDef",
    "ResponseSpecificationOutputTypeDef",
    "StillWaitingResponseSpecificationOutputTypeDef",
    "ListUtteranceAnalyticsDataResponseTypeDef",
    "FulfillmentStartResponseSpecificationTypeDef",
    "FulfillmentUpdateResponseSpecificationTypeDef",
    "PromptSpecificationTypeDef",
    "ResponseSpecificationTypeDef",
    "StillWaitingResponseSpecificationTypeDef",
    "CreateBotAliasResponseTypeDef",
    "DescribeBotAliasResponseTypeDef",
    "UpdateBotAliasResponseTypeDef",
    "CreateBotAliasRequestRequestTypeDef",
    "UpdateBotAliasRequestRequestTypeDef",
    "TranscriptSourceSettingOutputTypeDef",
    "TranscriptSourceSettingTypeDef",
    "TestSetTurnResultTypeDef",
    "TurnSpecificationTypeDef",
    "FulfillmentUpdatesSpecificationOutputTypeDef",
    "SlotSummaryTypeDef",
    "ConditionalBranchOutputTypeDef",
    "DefaultConditionalBranchOutputTypeDef",
    "WaitAndContinueSpecificationOutputTypeDef",
    "FulfillmentUpdatesSpecificationTypeDef",
    "ConditionalBranchTypeDef",
    "DefaultConditionalBranchTypeDef",
    "WaitAndContinueSpecificationTypeDef",
    "DescribeBotRecommendationResponseTypeDef",
    "StartBotRecommendationResponseTypeDef",
    "UpdateBotRecommendationResponseTypeDef",
    "StartBotRecommendationRequestRequestTypeDef",
    "UtteranceLevelTestResultItemTypeDef",
    "TestSetTurnRecordTypeDef",
    "ListSlotsResponseTypeDef",
    "ConditionalSpecificationOutputTypeDef",
    "SubSlotValueElicitationSettingOutputTypeDef",
    "ConditionalSpecificationTypeDef",
    "SubSlotValueElicitationSettingTypeDef",
    "UtteranceLevelTestResultsTypeDef",
    "ListTestSetRecordsResponseTypeDef",
    "IntentClosingSettingOutputTypeDef",
    "PostDialogCodeHookInvocationSpecificationOutputTypeDef",
    "PostFulfillmentStatusSpecificationOutputTypeDef",
    "SpecificationsOutputTypeDef",
    "IntentClosingSettingTypeDef",
    "PostDialogCodeHookInvocationSpecificationTypeDef",
    "PostFulfillmentStatusSpecificationTypeDef",
    "SpecificationsTypeDef",
    "TestExecutionResultItemsTypeDef",
    "DialogCodeHookInvocationSettingOutputTypeDef",
    "FulfillmentCodeHookSettingsOutputTypeDef",
    "SubSlotSettingOutputTypeDef",
    "DialogCodeHookInvocationSettingTypeDef",
    "FulfillmentCodeHookSettingsTypeDef",
    "SubSlotSettingTypeDef",
    "ListTestExecutionResultItemsResponseTypeDef",
    "InitialResponseSettingOutputTypeDef",
    "IntentConfirmationSettingOutputTypeDef",
    "SlotCaptureSettingOutputTypeDef",
    "InitialResponseSettingTypeDef",
    "IntentConfirmationSettingTypeDef",
    "SlotCaptureSettingTypeDef",
    "CreateIntentResponseTypeDef",
    "DescribeIntentResponseTypeDef",
    "UpdateIntentResponseTypeDef",
    "SlotValueElicitationSettingOutputTypeDef",
    "CreateIntentRequestRequestTypeDef",
    "UpdateIntentRequestRequestTypeDef",
    "SlotValueElicitationSettingTypeDef",
    "CreateSlotResponseTypeDef",
    "DescribeSlotResponseTypeDef",
    "UpdateSlotResponseTypeDef",
    "CreateSlotRequestRequestTypeDef",
    "UpdateSlotRequestRequestTypeDef",
)

ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
    },
)

AdvancedRecognitionSettingOutputTypeDef = TypedDict(
    "AdvancedRecognitionSettingOutputTypeDef",
    {
        "audioRecognitionStrategy": Literal["UseSlotValuesAsCustomVocabulary"],
    },
    total=False,
)

AdvancedRecognitionSettingTypeDef = TypedDict(
    "AdvancedRecognitionSettingTypeDef",
    {
        "audioRecognitionStrategy": Literal["UseSlotValuesAsCustomVocabulary"],
    },
    total=False,
)

ExecutionErrorDetailsTypeDef = TypedDict(
    "ExecutionErrorDetailsTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
    },
)

AgentTurnSpecificationTypeDef = TypedDict(
    "AgentTurnSpecificationTypeDef",
    {
        "agentPrompt": str,
    },
)

AggregatedUtterancesFilterTypeDef = TypedDict(
    "AggregatedUtterancesFilterTypeDef",
    {
        "name": Literal["Utterance"],
        "values": Sequence[str],
        "operator": AggregatedUtterancesFilterOperatorType,
    },
)

AggregatedUtterancesSortByTypeDef = TypedDict(
    "AggregatedUtterancesSortByTypeDef",
    {
        "attribute": AggregatedUtterancesSortAttributeType,
        "order": SortOrderType,
    },
)

AggregatedUtterancesSummaryTypeDef = TypedDict(
    "AggregatedUtterancesSummaryTypeDef",
    {
        "utterance": str,
        "hitCount": int,
        "missedCount": int,
        "utteranceFirstRecordedInAggregationDuration": datetime,
        "utteranceLastRecordedInAggregationDuration": datetime,
        "containsDataFromDeletedResources": bool,
    },
    total=False,
)

AllowedInputTypesOutputTypeDef = TypedDict(
    "AllowedInputTypesOutputTypeDef",
    {
        "allowAudioInput": bool,
        "allowDTMFInput": bool,
    },
)

AllowedInputTypesTypeDef = TypedDict(
    "AllowedInputTypesTypeDef",
    {
        "allowAudioInput": bool,
        "allowDTMFInput": bool,
    },
)

_RequiredAnalyticsBinBySpecificationTypeDef = TypedDict(
    "_RequiredAnalyticsBinBySpecificationTypeDef",
    {
        "name": AnalyticsBinByNameType,
        "interval": AnalyticsIntervalType,
    },
)
_OptionalAnalyticsBinBySpecificationTypeDef = TypedDict(
    "_OptionalAnalyticsBinBySpecificationTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)


class AnalyticsBinBySpecificationTypeDef(
    _RequiredAnalyticsBinBySpecificationTypeDef, _OptionalAnalyticsBinBySpecificationTypeDef
):
    pass


AnalyticsBinKeyTypeDef = TypedDict(
    "AnalyticsBinKeyTypeDef",
    {
        "name": AnalyticsBinByNameType,
        "value": int,
    },
    total=False,
)

AnalyticsIntentFilterTypeDef = TypedDict(
    "AnalyticsIntentFilterTypeDef",
    {
        "name": AnalyticsIntentFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": Sequence[str],
    },
)

AnalyticsIntentGroupByKeyTypeDef = TypedDict(
    "AnalyticsIntentGroupByKeyTypeDef",
    {
        "name": AnalyticsIntentFieldType,
        "value": str,
    },
    total=False,
)

AnalyticsIntentGroupBySpecificationTypeDef = TypedDict(
    "AnalyticsIntentGroupBySpecificationTypeDef",
    {
        "name": AnalyticsIntentFieldType,
    },
)

AnalyticsIntentMetricResultTypeDef = TypedDict(
    "AnalyticsIntentMetricResultTypeDef",
    {
        "name": AnalyticsIntentMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredAnalyticsIntentMetricTypeDef = TypedDict(
    "_RequiredAnalyticsIntentMetricTypeDef",
    {
        "name": AnalyticsIntentMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
    },
)
_OptionalAnalyticsIntentMetricTypeDef = TypedDict(
    "_OptionalAnalyticsIntentMetricTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)


class AnalyticsIntentMetricTypeDef(
    _RequiredAnalyticsIntentMetricTypeDef, _OptionalAnalyticsIntentMetricTypeDef
):
    pass


AnalyticsIntentNodeSummaryTypeDef = TypedDict(
    "AnalyticsIntentNodeSummaryTypeDef",
    {
        "intentName": str,
        "intentPath": str,
        "intentCount": int,
        "intentLevel": int,
        "nodeType": AnalyticsNodeTypeType,
    },
    total=False,
)

AnalyticsIntentStageFilterTypeDef = TypedDict(
    "AnalyticsIntentStageFilterTypeDef",
    {
        "name": AnalyticsIntentStageFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": Sequence[str],
    },
)

AnalyticsIntentStageGroupByKeyTypeDef = TypedDict(
    "AnalyticsIntentStageGroupByKeyTypeDef",
    {
        "name": AnalyticsIntentStageFieldType,
        "value": str,
    },
    total=False,
)

AnalyticsIntentStageGroupBySpecificationTypeDef = TypedDict(
    "AnalyticsIntentStageGroupBySpecificationTypeDef",
    {
        "name": AnalyticsIntentStageFieldType,
    },
)

AnalyticsIntentStageMetricResultTypeDef = TypedDict(
    "AnalyticsIntentStageMetricResultTypeDef",
    {
        "name": AnalyticsIntentStageMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredAnalyticsIntentStageMetricTypeDef = TypedDict(
    "_RequiredAnalyticsIntentStageMetricTypeDef",
    {
        "name": AnalyticsIntentStageMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
    },
)
_OptionalAnalyticsIntentStageMetricTypeDef = TypedDict(
    "_OptionalAnalyticsIntentStageMetricTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)


class AnalyticsIntentStageMetricTypeDef(
    _RequiredAnalyticsIntentStageMetricTypeDef, _OptionalAnalyticsIntentStageMetricTypeDef
):
    pass


AnalyticsPathFilterTypeDef = TypedDict(
    "AnalyticsPathFilterTypeDef",
    {
        "name": AnalyticsCommonFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": Sequence[str],
    },
)

AnalyticsSessionFilterTypeDef = TypedDict(
    "AnalyticsSessionFilterTypeDef",
    {
        "name": AnalyticsSessionFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": Sequence[str],
    },
)

AnalyticsSessionGroupByKeyTypeDef = TypedDict(
    "AnalyticsSessionGroupByKeyTypeDef",
    {
        "name": AnalyticsSessionFieldType,
        "value": str,
    },
    total=False,
)

AnalyticsSessionGroupBySpecificationTypeDef = TypedDict(
    "AnalyticsSessionGroupBySpecificationTypeDef",
    {
        "name": AnalyticsSessionFieldType,
    },
)

AnalyticsSessionMetricResultTypeDef = TypedDict(
    "AnalyticsSessionMetricResultTypeDef",
    {
        "name": AnalyticsSessionMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredAnalyticsSessionMetricTypeDef = TypedDict(
    "_RequiredAnalyticsSessionMetricTypeDef",
    {
        "name": AnalyticsSessionMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
    },
)
_OptionalAnalyticsSessionMetricTypeDef = TypedDict(
    "_OptionalAnalyticsSessionMetricTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)


class AnalyticsSessionMetricTypeDef(
    _RequiredAnalyticsSessionMetricTypeDef, _OptionalAnalyticsSessionMetricTypeDef
):
    pass


AnalyticsUtteranceAttributeResultTypeDef = TypedDict(
    "AnalyticsUtteranceAttributeResultTypeDef",
    {
        "lastUsedIntent": str,
    },
    total=False,
)

AnalyticsUtteranceAttributeTypeDef = TypedDict(
    "AnalyticsUtteranceAttributeTypeDef",
    {
        "name": Literal["LastUsedIntent"],
    },
)

AnalyticsUtteranceFilterTypeDef = TypedDict(
    "AnalyticsUtteranceFilterTypeDef",
    {
        "name": AnalyticsUtteranceFilterNameType,
        "operator": AnalyticsFilterOperatorType,
        "values": Sequence[str],
    },
)

AnalyticsUtteranceGroupByKeyTypeDef = TypedDict(
    "AnalyticsUtteranceGroupByKeyTypeDef",
    {
        "name": AnalyticsUtteranceFieldType,
        "value": str,
    },
    total=False,
)

AnalyticsUtteranceGroupBySpecificationTypeDef = TypedDict(
    "AnalyticsUtteranceGroupBySpecificationTypeDef",
    {
        "name": AnalyticsUtteranceFieldType,
    },
)

AnalyticsUtteranceMetricResultTypeDef = TypedDict(
    "AnalyticsUtteranceMetricResultTypeDef",
    {
        "name": AnalyticsUtteranceMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
        "value": float,
    },
    total=False,
)

_RequiredAnalyticsUtteranceMetricTypeDef = TypedDict(
    "_RequiredAnalyticsUtteranceMetricTypeDef",
    {
        "name": AnalyticsUtteranceMetricNameType,
        "statistic": AnalyticsMetricStatisticType,
    },
)
_OptionalAnalyticsUtteranceMetricTypeDef = TypedDict(
    "_OptionalAnalyticsUtteranceMetricTypeDef",
    {
        "order": AnalyticsSortOrderType,
    },
    total=False,
)


class AnalyticsUtteranceMetricTypeDef(
    _RequiredAnalyticsUtteranceMetricTypeDef, _OptionalAnalyticsUtteranceMetricTypeDef
):
    pass


AssociatedTranscriptFilterTypeDef = TypedDict(
    "AssociatedTranscriptFilterTypeDef",
    {
        "name": AssociatedTranscriptFilterNameType,
        "values": Sequence[str],
    },
)

AssociatedTranscriptTypeDef = TypedDict(
    "AssociatedTranscriptTypeDef",
    {
        "transcript": str,
    },
    total=False,
)

AudioSpecificationOutputTypeDef = TypedDict(
    "AudioSpecificationOutputTypeDef",
    {
        "maxLengthMs": int,
        "endTimeoutMs": int,
    },
)

DTMFSpecificationOutputTypeDef = TypedDict(
    "DTMFSpecificationOutputTypeDef",
    {
        "maxLength": int,
        "endTimeoutMs": int,
        "deletionCharacter": str,
        "endCharacter": str,
    },
)

AudioSpecificationTypeDef = TypedDict(
    "AudioSpecificationTypeDef",
    {
        "maxLengthMs": int,
        "endTimeoutMs": int,
    },
)

DTMFSpecificationTypeDef = TypedDict(
    "DTMFSpecificationTypeDef",
    {
        "maxLength": int,
        "endTimeoutMs": int,
        "deletionCharacter": str,
        "endCharacter": str,
    },
)

_RequiredS3BucketLogDestinationOutputTypeDef = TypedDict(
    "_RequiredS3BucketLogDestinationOutputTypeDef",
    {
        "s3BucketArn": str,
        "logPrefix": str,
    },
)
_OptionalS3BucketLogDestinationOutputTypeDef = TypedDict(
    "_OptionalS3BucketLogDestinationOutputTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class S3BucketLogDestinationOutputTypeDef(
    _RequiredS3BucketLogDestinationOutputTypeDef, _OptionalS3BucketLogDestinationOutputTypeDef
):
    pass


_RequiredS3BucketLogDestinationTypeDef = TypedDict(
    "_RequiredS3BucketLogDestinationTypeDef",
    {
        "s3BucketArn": str,
        "logPrefix": str,
    },
)
_OptionalS3BucketLogDestinationTypeDef = TypedDict(
    "_OptionalS3BucketLogDestinationTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class S3BucketLogDestinationTypeDef(
    _RequiredS3BucketLogDestinationTypeDef, _OptionalS3BucketLogDestinationTypeDef
):
    pass


_RequiredNewCustomVocabularyItemTypeDef = TypedDict(
    "_RequiredNewCustomVocabularyItemTypeDef",
    {
        "phrase": str,
    },
)
_OptionalNewCustomVocabularyItemTypeDef = TypedDict(
    "_OptionalNewCustomVocabularyItemTypeDef",
    {
        "weight": int,
        "displayAs": str,
    },
    total=False,
)


class NewCustomVocabularyItemTypeDef(
    _RequiredNewCustomVocabularyItemTypeDef, _OptionalNewCustomVocabularyItemTypeDef
):
    pass


_RequiredCustomVocabularyItemOutputTypeDef = TypedDict(
    "_RequiredCustomVocabularyItemOutputTypeDef",
    {
        "itemId": str,
        "phrase": str,
    },
)
_OptionalCustomVocabularyItemOutputTypeDef = TypedDict(
    "_OptionalCustomVocabularyItemOutputTypeDef",
    {
        "weight": int,
        "displayAs": str,
    },
    total=False,
)


class CustomVocabularyItemOutputTypeDef(
    _RequiredCustomVocabularyItemOutputTypeDef, _OptionalCustomVocabularyItemOutputTypeDef
):
    pass


FailedCustomVocabularyItemTypeDef = TypedDict(
    "FailedCustomVocabularyItemTypeDef",
    {
        "itemId": str,
        "errorMessage": str,
        "errorCode": ErrorCodeType,
    },
    total=False,
)

CustomVocabularyEntryIdTypeDef = TypedDict(
    "CustomVocabularyEntryIdTypeDef",
    {
        "itemId": str,
    },
)

_RequiredCustomVocabularyItemTypeDef = TypedDict(
    "_RequiredCustomVocabularyItemTypeDef",
    {
        "itemId": str,
        "phrase": str,
    },
)
_OptionalCustomVocabularyItemTypeDef = TypedDict(
    "_OptionalCustomVocabularyItemTypeDef",
    {
        "weight": int,
        "displayAs": str,
    },
    total=False,
)


class CustomVocabularyItemTypeDef(
    _RequiredCustomVocabularyItemTypeDef, _OptionalCustomVocabularyItemTypeDef
):
    pass


BotAliasHistoryEventTypeDef = TypedDict(
    "BotAliasHistoryEventTypeDef",
    {
        "botVersion": str,
        "startDate": datetime,
        "endDate": datetime,
    },
    total=False,
)

BotAliasSummaryTypeDef = TypedDict(
    "BotAliasSummaryTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasStatus": BotAliasStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

BotAliasTestExecutionTargetOutputTypeDef = TypedDict(
    "BotAliasTestExecutionTargetOutputTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
    },
)

BotAliasTestExecutionTargetTypeDef = TypedDict(
    "BotAliasTestExecutionTargetTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
    },
)

BotExportSpecificationOutputTypeDef = TypedDict(
    "BotExportSpecificationOutputTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

BotExportSpecificationTypeDef = TypedDict(
    "BotExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

BotFilterTypeDef = TypedDict(
    "BotFilterTypeDef",
    {
        "name": BotFilterNameType,
        "values": Sequence[str],
        "operator": BotFilterOperatorType,
    },
)

DataPrivacyOutputTypeDef = TypedDict(
    "DataPrivacyOutputTypeDef",
    {
        "childDirected": bool,
    },
)

DataPrivacyTypeDef = TypedDict(
    "DataPrivacyTypeDef",
    {
        "childDirected": bool,
    },
)

BotLocaleExportSpecificationOutputTypeDef = TypedDict(
    "BotLocaleExportSpecificationOutputTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BotLocaleExportSpecificationTypeDef = TypedDict(
    "BotLocaleExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BotLocaleFilterTypeDef = TypedDict(
    "BotLocaleFilterTypeDef",
    {
        "name": Literal["BotLocaleName"],
        "values": Sequence[str],
        "operator": BotLocaleFilterOperatorType,
    },
)

BotLocaleHistoryEventTypeDef = TypedDict(
    "BotLocaleHistoryEventTypeDef",
    {
        "event": str,
        "eventDate": datetime,
    },
)

_RequiredVoiceSettingsOutputTypeDef = TypedDict(
    "_RequiredVoiceSettingsOutputTypeDef",
    {
        "voiceId": str,
    },
)
_OptionalVoiceSettingsOutputTypeDef = TypedDict(
    "_OptionalVoiceSettingsOutputTypeDef",
    {
        "engine": VoiceEngineType,
    },
    total=False,
)


class VoiceSettingsOutputTypeDef(
    _RequiredVoiceSettingsOutputTypeDef, _OptionalVoiceSettingsOutputTypeDef
):
    pass


_RequiredVoiceSettingsTypeDef = TypedDict(
    "_RequiredVoiceSettingsTypeDef",
    {
        "voiceId": str,
    },
)
_OptionalVoiceSettingsTypeDef = TypedDict(
    "_OptionalVoiceSettingsTypeDef",
    {
        "engine": VoiceEngineType,
    },
    total=False,
)


class VoiceSettingsTypeDef(_RequiredVoiceSettingsTypeDef, _OptionalVoiceSettingsTypeDef):
    pass


BotLocaleSortByTypeDef = TypedDict(
    "BotLocaleSortByTypeDef",
    {
        "attribute": Literal["BotLocaleName"],
        "order": SortOrderType,
    },
)

BotLocaleSummaryTypeDef = TypedDict(
    "BotLocaleSummaryTypeDef",
    {
        "localeId": str,
        "localeName": str,
        "description": str,
        "botLocaleStatus": BotLocaleStatusType,
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
    },
    total=False,
)

BotMemberOutputTypeDef = TypedDict(
    "BotMemberOutputTypeDef",
    {
        "botMemberId": str,
        "botMemberName": str,
        "botMemberAliasId": str,
        "botMemberAliasName": str,
        "botMemberVersion": str,
    },
)

BotMemberTypeDef = TypedDict(
    "BotMemberTypeDef",
    {
        "botMemberId": str,
        "botMemberName": str,
        "botMemberAliasId": str,
        "botMemberAliasName": str,
        "botMemberVersion": str,
    },
)

IntentStatisticsTypeDef = TypedDict(
    "IntentStatisticsTypeDef",
    {
        "discoveredIntentCount": int,
    },
    total=False,
)

SlotTypeStatisticsTypeDef = TypedDict(
    "SlotTypeStatisticsTypeDef",
    {
        "discoveredSlotTypeCount": int,
    },
    total=False,
)

_RequiredBotRecommendationSummaryTypeDef = TypedDict(
    "_RequiredBotRecommendationSummaryTypeDef",
    {
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
    },
)
_OptionalBotRecommendationSummaryTypeDef = TypedDict(
    "_OptionalBotRecommendationSummaryTypeDef",
    {
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)


class BotRecommendationSummaryTypeDef(
    _RequiredBotRecommendationSummaryTypeDef, _OptionalBotRecommendationSummaryTypeDef
):
    pass


BotSortByTypeDef = TypedDict(
    "BotSortByTypeDef",
    {
        "attribute": Literal["BotName"],
        "order": SortOrderType,
    },
)

BotSummaryTypeDef = TypedDict(
    "BotSummaryTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "botStatus": BotStatusType,
        "latestBotVersion": str,
        "lastUpdatedDateTime": datetime,
        "botType": BotTypeType,
    },
    total=False,
)

BotVersionLocaleDetailsOutputTypeDef = TypedDict(
    "BotVersionLocaleDetailsOutputTypeDef",
    {
        "sourceBotVersion": str,
    },
)

BotVersionLocaleDetailsTypeDef = TypedDict(
    "BotVersionLocaleDetailsTypeDef",
    {
        "sourceBotVersion": str,
    },
)

BotVersionSortByTypeDef = TypedDict(
    "BotVersionSortByTypeDef",
    {
        "attribute": Literal["BotVersion"],
        "order": SortOrderType,
    },
)

BotVersionSummaryTypeDef = TypedDict(
    "BotVersionSummaryTypeDef",
    {
        "botName": str,
        "botVersion": str,
        "description": str,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
    },
    total=False,
)

BuildBotLocaleRequestRequestTypeDef = TypedDict(
    "BuildBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BuildBotLocaleResponseTypeDef = TypedDict(
    "BuildBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "lastBuildSubmittedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BuiltInIntentSortByTypeDef = TypedDict(
    "BuiltInIntentSortByTypeDef",
    {
        "attribute": Literal["IntentSignature"],
        "order": SortOrderType,
    },
)

BuiltInIntentSummaryTypeDef = TypedDict(
    "BuiltInIntentSummaryTypeDef",
    {
        "intentSignature": str,
        "description": str,
    },
    total=False,
)

BuiltInSlotTypeSortByTypeDef = TypedDict(
    "BuiltInSlotTypeSortByTypeDef",
    {
        "attribute": Literal["SlotTypeSignature"],
        "order": SortOrderType,
    },
)

BuiltInSlotTypeSummaryTypeDef = TypedDict(
    "BuiltInSlotTypeSummaryTypeDef",
    {
        "slotTypeSignature": str,
        "description": str,
    },
    total=False,
)

ButtonOutputTypeDef = TypedDict(
    "ButtonOutputTypeDef",
    {
        "text": str,
        "value": str,
    },
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

CloudWatchLogGroupLogDestinationOutputTypeDef = TypedDict(
    "CloudWatchLogGroupLogDestinationOutputTypeDef",
    {
        "cloudWatchLogGroupArn": str,
        "logPrefix": str,
    },
)

CloudWatchLogGroupLogDestinationTypeDef = TypedDict(
    "CloudWatchLogGroupLogDestinationTypeDef",
    {
        "cloudWatchLogGroupArn": str,
        "logPrefix": str,
    },
)

LambdaCodeHookOutputTypeDef = TypedDict(
    "LambdaCodeHookOutputTypeDef",
    {
        "lambdaARN": str,
        "codeHookInterfaceVersion": str,
    },
)

LambdaCodeHookTypeDef = TypedDict(
    "LambdaCodeHookTypeDef",
    {
        "lambdaARN": str,
        "codeHookInterfaceVersion": str,
    },
)

SubSlotTypeCompositionOutputTypeDef = TypedDict(
    "SubSlotTypeCompositionOutputTypeDef",
    {
        "name": str,
        "slotTypeId": str,
    },
)

SubSlotTypeCompositionTypeDef = TypedDict(
    "SubSlotTypeCompositionTypeDef",
    {
        "name": str,
        "slotTypeId": str,
    },
)

ConditionOutputTypeDef = TypedDict(
    "ConditionOutputTypeDef",
    {
        "expressionString": str,
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "expressionString": str,
    },
)

ConversationLevelIntentClassificationResultItemTypeDef = TypedDict(
    "ConversationLevelIntentClassificationResultItemTypeDef",
    {
        "intentName": str,
        "matchResult": TestResultMatchStatusType,
    },
)

_RequiredConversationLevelResultDetailTypeDef = TypedDict(
    "_RequiredConversationLevelResultDetailTypeDef",
    {
        "endToEndResult": TestResultMatchStatusType,
    },
)
_OptionalConversationLevelResultDetailTypeDef = TypedDict(
    "_OptionalConversationLevelResultDetailTypeDef",
    {
        "speechTranscriptionResult": TestResultMatchStatusType,
    },
    total=False,
)


class ConversationLevelResultDetailTypeDef(
    _RequiredConversationLevelResultDetailTypeDef, _OptionalConversationLevelResultDetailTypeDef
):
    pass


ConversationLevelSlotResolutionResultItemTypeDef = TypedDict(
    "ConversationLevelSlotResolutionResultItemTypeDef",
    {
        "intentName": str,
        "slotName": str,
        "matchResult": TestResultMatchStatusType,
    },
)

ConversationLevelTestResultsFilterByTypeDef = TypedDict(
    "ConversationLevelTestResultsFilterByTypeDef",
    {
        "endToEndResult": TestResultMatchStatusType,
    },
    total=False,
)

ConversationLogsDataSourceFilterByOutputTypeDef = TypedDict(
    "ConversationLogsDataSourceFilterByOutputTypeDef",
    {
        "startTime": datetime,
        "endTime": datetime,
        "inputMode": ConversationLogsInputModeFilterType,
    },
)

ConversationLogsDataSourceFilterByTypeDef = TypedDict(
    "ConversationLogsDataSourceFilterByTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "inputMode": ConversationLogsInputModeFilterType,
    },
)

SentimentAnalysisSettingsTypeDef = TypedDict(
    "SentimentAnalysisSettingsTypeDef",
    {
        "detectSentiment": bool,
    },
)

SentimentAnalysisSettingsOutputTypeDef = TypedDict(
    "SentimentAnalysisSettingsOutputTypeDef",
    {
        "detectSentiment": bool,
    },
)

DialogCodeHookSettingsTypeDef = TypedDict(
    "DialogCodeHookSettingsTypeDef",
    {
        "enabled": bool,
    },
)

InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)

_RequiredKendraConfigurationTypeDef = TypedDict(
    "_RequiredKendraConfigurationTypeDef",
    {
        "kendraIndex": str,
    },
)
_OptionalKendraConfigurationTypeDef = TypedDict(
    "_OptionalKendraConfigurationTypeDef",
    {
        "queryFilterStringEnabled": bool,
        "queryFilterString": str,
    },
    total=False,
)


class KendraConfigurationTypeDef(
    _RequiredKendraConfigurationTypeDef, _OptionalKendraConfigurationTypeDef
):
    pass


OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

SampleUtteranceTypeDef = TypedDict(
    "SampleUtteranceTypeDef",
    {
        "utterance": str,
    },
)

DialogCodeHookSettingsOutputTypeDef = TypedDict(
    "DialogCodeHookSettingsOutputTypeDef",
    {
        "enabled": bool,
    },
)

InputContextOutputTypeDef = TypedDict(
    "InputContextOutputTypeDef",
    {
        "name": str,
    },
)

_RequiredKendraConfigurationOutputTypeDef = TypedDict(
    "_RequiredKendraConfigurationOutputTypeDef",
    {
        "kendraIndex": str,
    },
)
_OptionalKendraConfigurationOutputTypeDef = TypedDict(
    "_OptionalKendraConfigurationOutputTypeDef",
    {
        "queryFilterStringEnabled": bool,
        "queryFilterString": str,
    },
    total=False,
)


class KendraConfigurationOutputTypeDef(
    _RequiredKendraConfigurationOutputTypeDef, _OptionalKendraConfigurationOutputTypeDef
):
    pass


OutputContextOutputTypeDef = TypedDict(
    "OutputContextOutputTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

SampleUtteranceOutputTypeDef = TypedDict(
    "SampleUtteranceOutputTypeDef",
    {
        "utterance": str,
    },
)

CreateResourcePolicyRequestRequestTypeDef = TypedDict(
    "CreateResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
        "policy": str,
    },
)

CreateResourcePolicyResponseTypeDef = TypedDict(
    "CreateResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "service": str,
        "arn": str,
    },
    total=False,
)

CreateResourcePolicyStatementResponseTypeDef = TypedDict(
    "CreateResourcePolicyStatementResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MultipleValuesSettingTypeDef = TypedDict(
    "MultipleValuesSettingTypeDef",
    {
        "allowMultipleValues": bool,
    },
    total=False,
)

ObfuscationSettingTypeDef = TypedDict(
    "ObfuscationSettingTypeDef",
    {
        "obfuscationSettingType": ObfuscationSettingTypeType,
    },
)

MultipleValuesSettingOutputTypeDef = TypedDict(
    "MultipleValuesSettingOutputTypeDef",
    {
        "allowMultipleValues": bool,
    },
    total=False,
)

ObfuscationSettingOutputTypeDef = TypedDict(
    "ObfuscationSettingOutputTypeDef",
    {
        "obfuscationSettingType": ObfuscationSettingTypeType,
    },
)

CreateUploadUrlResponseTypeDef = TypedDict(
    "CreateUploadUrlResponseTypeDef",
    {
        "importId": str,
        "uploadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomPayloadOutputTypeDef = TypedDict(
    "CustomPayloadOutputTypeDef",
    {
        "value": str,
    },
)

CustomPayloadTypeDef = TypedDict(
    "CustomPayloadTypeDef",
    {
        "value": str,
    },
)

CustomVocabularyExportSpecificationOutputTypeDef = TypedDict(
    "CustomVocabularyExportSpecificationOutputTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

CustomVocabularyExportSpecificationTypeDef = TypedDict(
    "CustomVocabularyExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

CustomVocabularyImportSpecificationOutputTypeDef = TypedDict(
    "CustomVocabularyImportSpecificationOutputTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

CustomVocabularyImportSpecificationTypeDef = TypedDict(
    "CustomVocabularyImportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DateRangeFilterOutputTypeDef = TypedDict(
    "DateRangeFilterOutputTypeDef",
    {
        "startDateTime": datetime,
        "endDateTime": datetime,
    },
)

DateRangeFilterTypeDef = TypedDict(
    "DateRangeFilterTypeDef",
    {
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
    },
)

_RequiredDeleteBotAliasRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botId": str,
    },
)
_OptionalDeleteBotAliasRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBotAliasRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)


class DeleteBotAliasRequestRequestTypeDef(
    _RequiredDeleteBotAliasRequestRequestTypeDef, _OptionalDeleteBotAliasRequestRequestTypeDef
):
    pass


DeleteBotAliasResponseTypeDef = TypedDict(
    "DeleteBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botId": str,
        "botAliasStatus": BotAliasStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotLocaleRequestRequestTypeDef = TypedDict(
    "DeleteBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DeleteBotLocaleResponseTypeDef = TypedDict(
    "DeleteBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBotRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBotRequestRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalDeleteBotRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBotRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)


class DeleteBotRequestRequestTypeDef(
    _RequiredDeleteBotRequestRequestTypeDef, _OptionalDeleteBotRequestRequestTypeDef
):
    pass


DeleteBotResponseTypeDef = TypedDict(
    "DeleteBotResponseTypeDef",
    {
        "botId": str,
        "botStatus": BotStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBotVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)
_OptionalDeleteBotVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBotVersionRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)


class DeleteBotVersionRequestRequestTypeDef(
    _RequiredDeleteBotVersionRequestRequestTypeDef, _OptionalDeleteBotVersionRequestRequestTypeDef
):
    pass


DeleteBotVersionResponseTypeDef = TypedDict(
    "DeleteBotVersionResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "botStatus": BotStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteCustomVocabularyRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DeleteCustomVocabularyResponseTypeDef = TypedDict(
    "DeleteCustomVocabularyResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyStatus": CustomVocabularyStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExportRequestRequestTypeDef = TypedDict(
    "DeleteExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)

DeleteExportResponseTypeDef = TypedDict(
    "DeleteExportResponseTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImportRequestRequestTypeDef = TypedDict(
    "DeleteImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

DeleteImportResponseTypeDef = TypedDict(
    "DeleteImportResponseTypeDef",
    {
        "importId": str,
        "importStatus": ImportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIntentRequestRequestTypeDef = TypedDict(
    "DeleteIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

_RequiredDeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalDeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePolicyRequestRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)


class DeleteResourcePolicyRequestRequestTypeDef(
    _RequiredDeleteResourcePolicyRequestRequestTypeDef,
    _OptionalDeleteResourcePolicyRequestRequestTypeDef,
):
    pass


DeleteResourcePolicyResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePolicyStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "statementId": str,
    },
)
_OptionalDeleteResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePolicyStatementRequestRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)


class DeleteResourcePolicyStatementRequestRequestTypeDef(
    _RequiredDeleteResourcePolicyStatementRequestRequestTypeDef,
    _OptionalDeleteResourcePolicyStatementRequestRequestTypeDef,
):
    pass


DeleteResourcePolicyStatementResponseTypeDef = TypedDict(
    "DeleteResourcePolicyStatementResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSlotRequestRequestTypeDef = TypedDict(
    "DeleteSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)

_RequiredDeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalDeleteSlotTypeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSlotTypeRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)


class DeleteSlotTypeRequestRequestTypeDef(
    _RequiredDeleteSlotTypeRequestRequestTypeDef, _OptionalDeleteSlotTypeRequestRequestTypeDef
):
    pass


DeleteTestSetRequestRequestTypeDef = TypedDict(
    "DeleteTestSetRequestRequestTypeDef",
    {
        "testSetId": str,
    },
)

_RequiredDeleteUtterancesRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteUtterancesRequestRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalDeleteUtterancesRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteUtterancesRequestRequestTypeDef",
    {
        "localeId": str,
        "sessionId": str,
    },
    total=False,
)


class DeleteUtterancesRequestRequestTypeDef(
    _RequiredDeleteUtterancesRequestRequestTypeDef, _OptionalDeleteUtterancesRequestRequestTypeDef
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

DescribeBotAliasRequestRequestTypeDef = TypedDict(
    "DescribeBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botId": str,
    },
)

ParentBotNetworkTypeDef = TypedDict(
    "ParentBotNetworkTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

DescribeBotLocaleRequestRequestTypeDef = TypedDict(
    "DescribeBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeBotRecommendationRequestRequestTypeDef = TypedDict(
    "DescribeBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
    },
)

EncryptionSettingOutputTypeDef = TypedDict(
    "EncryptionSettingOutputTypeDef",
    {
        "kmsKeyArn": str,
        "botLocaleExportPassword": str,
        "associatedTranscriptsPassword": str,
    },
    total=False,
)

DescribeBotRequestRequestTypeDef = TypedDict(
    "DescribeBotRequestRequestTypeDef",
    {
        "botId": str,
    },
)

DescribeBotVersionRequestRequestTypeDef = TypedDict(
    "DescribeBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

DescribeCustomVocabularyMetadataRequestRequestTypeDef = TypedDict(
    "DescribeCustomVocabularyMetadataRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeCustomVocabularyMetadataResponseTypeDef = TypedDict(
    "DescribeCustomVocabularyMetadataResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyStatus": CustomVocabularyStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportRequestRequestTypeDef = TypedDict(
    "DescribeExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)

DescribeImportRequestRequestTypeDef = TypedDict(
    "DescribeImportRequestRequestTypeDef",
    {
        "importId": str,
    },
)

DescribeIntentRequestRequestTypeDef = TypedDict(
    "DescribeIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

SlotPriorityOutputTypeDef = TypedDict(
    "SlotPriorityOutputTypeDef",
    {
        "priority": int,
        "slotId": str,
    },
)

DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotRequestRequestTypeDef = TypedDict(
    "DescribeSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)

DescribeSlotTypeRequestRequestTypeDef = TypedDict(
    "DescribeSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeTestExecutionRequestRequestTypeDef = TypedDict(
    "DescribeTestExecutionRequestRequestTypeDef",
    {
        "testExecutionId": str,
    },
)

DescribeTestSetDiscrepancyReportRequestRequestTypeDef = TypedDict(
    "DescribeTestSetDiscrepancyReportRequestRequestTypeDef",
    {
        "testSetDiscrepancyReportId": str,
    },
)

DescribeTestSetGenerationRequestRequestTypeDef = TypedDict(
    "DescribeTestSetGenerationRequestRequestTypeDef",
    {
        "testSetGenerationId": str,
    },
)

_RequiredTestSetStorageLocationOutputTypeDef = TypedDict(
    "_RequiredTestSetStorageLocationOutputTypeDef",
    {
        "s3BucketName": str,
        "s3Path": str,
    },
)
_OptionalTestSetStorageLocationOutputTypeDef = TypedDict(
    "_OptionalTestSetStorageLocationOutputTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class TestSetStorageLocationOutputTypeDef(
    _RequiredTestSetStorageLocationOutputTypeDef, _OptionalTestSetStorageLocationOutputTypeDef
):
    pass


DescribeTestSetRequestRequestTypeDef = TypedDict(
    "DescribeTestSetRequestRequestTypeDef",
    {
        "testSetId": str,
    },
)

_RequiredDialogActionOutputTypeDef = TypedDict(
    "_RequiredDialogActionOutputTypeDef",
    {
        "type": DialogActionTypeType,
    },
)
_OptionalDialogActionOutputTypeDef = TypedDict(
    "_OptionalDialogActionOutputTypeDef",
    {
        "slotToElicit": str,
        "suppressNextMessage": bool,
    },
    total=False,
)


class DialogActionOutputTypeDef(
    _RequiredDialogActionOutputTypeDef, _OptionalDialogActionOutputTypeDef
):
    pass


_RequiredDialogActionTypeDef = TypedDict(
    "_RequiredDialogActionTypeDef",
    {
        "type": DialogActionTypeType,
    },
)
_OptionalDialogActionTypeDef = TypedDict(
    "_OptionalDialogActionTypeDef",
    {
        "slotToElicit": str,
        "suppressNextMessage": bool,
    },
    total=False,
)


class DialogActionTypeDef(_RequiredDialogActionTypeDef, _OptionalDialogActionTypeDef):
    pass


IntentOverrideOutputTypeDef = TypedDict(
    "IntentOverrideOutputTypeDef",
    {
        "name": str,
        "slots": Dict[str, "SlotValueOverrideOutputTypeDef"],
    },
    total=False,
)

IntentOverrideTypeDef = TypedDict(
    "IntentOverrideTypeDef",
    {
        "name": str,
        "slots": Mapping[str, "SlotValueOverrideTypeDef"],
    },
    total=False,
)

_RequiredElicitationCodeHookInvocationSettingOutputTypeDef = TypedDict(
    "_RequiredElicitationCodeHookInvocationSettingOutputTypeDef",
    {
        "enableCodeHookInvocation": bool,
    },
)
_OptionalElicitationCodeHookInvocationSettingOutputTypeDef = TypedDict(
    "_OptionalElicitationCodeHookInvocationSettingOutputTypeDef",
    {
        "invocationLabel": str,
    },
    total=False,
)


class ElicitationCodeHookInvocationSettingOutputTypeDef(
    _RequiredElicitationCodeHookInvocationSettingOutputTypeDef,
    _OptionalElicitationCodeHookInvocationSettingOutputTypeDef,
):
    pass


_RequiredElicitationCodeHookInvocationSettingTypeDef = TypedDict(
    "_RequiredElicitationCodeHookInvocationSettingTypeDef",
    {
        "enableCodeHookInvocation": bool,
    },
)
_OptionalElicitationCodeHookInvocationSettingTypeDef = TypedDict(
    "_OptionalElicitationCodeHookInvocationSettingTypeDef",
    {
        "invocationLabel": str,
    },
    total=False,
)


class ElicitationCodeHookInvocationSettingTypeDef(
    _RequiredElicitationCodeHookInvocationSettingTypeDef,
    _OptionalElicitationCodeHookInvocationSettingTypeDef,
):
    pass


EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionSettingTypeDef = TypedDict(
    "EncryptionSettingTypeDef",
    {
        "kmsKeyArn": str,
        "botLocaleExportPassword": str,
        "associatedTranscriptsPassword": str,
    },
    total=False,
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef",
    {
        "name": Literal["ExportResourceType"],
        "values": Sequence[str],
        "operator": ExportFilterOperatorType,
    },
)

TestSetExportSpecificationOutputTypeDef = TypedDict(
    "TestSetExportSpecificationOutputTypeDef",
    {
        "testSetId": str,
    },
)

TestSetExportSpecificationTypeDef = TypedDict(
    "TestSetExportSpecificationTypeDef",
    {
        "testSetId": str,
    },
)

ExportSortByTypeDef = TypedDict(
    "ExportSortByTypeDef",
    {
        "attribute": Literal["LastUpdatedDateTime"],
        "order": SortOrderType,
    },
)

GetTestExecutionArtifactsUrlRequestRequestTypeDef = TypedDict(
    "GetTestExecutionArtifactsUrlRequestRequestTypeDef",
    {
        "testExecutionId": str,
    },
)

GetTestExecutionArtifactsUrlResponseTypeDef = TypedDict(
    "GetTestExecutionArtifactsUrlResponseTypeDef",
    {
        "testExecutionId": str,
        "downloadArtifactsUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGrammarSlotTypeSourceOutputTypeDef = TypedDict(
    "_RequiredGrammarSlotTypeSourceOutputTypeDef",
    {
        "s3BucketName": str,
        "s3ObjectKey": str,
    },
)
_OptionalGrammarSlotTypeSourceOutputTypeDef = TypedDict(
    "_OptionalGrammarSlotTypeSourceOutputTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class GrammarSlotTypeSourceOutputTypeDef(
    _RequiredGrammarSlotTypeSourceOutputTypeDef, _OptionalGrammarSlotTypeSourceOutputTypeDef
):
    pass


_RequiredGrammarSlotTypeSourceTypeDef = TypedDict(
    "_RequiredGrammarSlotTypeSourceTypeDef",
    {
        "s3BucketName": str,
        "s3ObjectKey": str,
    },
)
_OptionalGrammarSlotTypeSourceTypeDef = TypedDict(
    "_OptionalGrammarSlotTypeSourceTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class GrammarSlotTypeSourceTypeDef(
    _RequiredGrammarSlotTypeSourceTypeDef, _OptionalGrammarSlotTypeSourceTypeDef
):
    pass


ImportFilterTypeDef = TypedDict(
    "ImportFilterTypeDef",
    {
        "name": Literal["ImportResourceType"],
        "values": Sequence[str],
        "operator": ImportFilterOperatorType,
    },
)

ImportSortByTypeDef = TypedDict(
    "ImportSortByTypeDef",
    {
        "attribute": Literal["LastUpdatedDateTime"],
        "order": SortOrderType,
    },
)

ImportSummaryTypeDef = TypedDict(
    "ImportSummaryTypeDef",
    {
        "importId": str,
        "importedResourceId": str,
        "importedResourceName": str,
        "importStatus": ImportStatusType,
        "mergeStrategy": MergeStrategyType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "importedResourceType": ImportResourceTypeType,
    },
    total=False,
)

RuntimeHintsTypeDef = TypedDict(
    "RuntimeHintsTypeDef",
    {
        "slotHints": Dict[str, Dict[str, "RuntimeHintDetailsTypeDef"]],
    },
    total=False,
)

_RequiredIntentClassificationTestResultItemCountsTypeDef = TypedDict(
    "_RequiredIntentClassificationTestResultItemCountsTypeDef",
    {
        "totalResultCount": int,
        "intentMatchResultCounts": Dict[TestResultMatchStatusType, int],
    },
)
_OptionalIntentClassificationTestResultItemCountsTypeDef = TypedDict(
    "_OptionalIntentClassificationTestResultItemCountsTypeDef",
    {
        "speechTranscriptionResultCounts": Dict[TestResultMatchStatusType, int],
    },
    total=False,
)


class IntentClassificationTestResultItemCountsTypeDef(
    _RequiredIntentClassificationTestResultItemCountsTypeDef,
    _OptionalIntentClassificationTestResultItemCountsTypeDef,
):
    pass


IntentFilterTypeDef = TypedDict(
    "IntentFilterTypeDef",
    {
        "name": Literal["IntentName"],
        "values": Sequence[str],
        "operator": IntentFilterOperatorType,
    },
)

IntentSortByTypeDef = TypedDict(
    "IntentSortByTypeDef",
    {
        "attribute": IntentSortAttributeType,
        "order": SortOrderType,
    },
)

InvokedIntentSampleTypeDef = TypedDict(
    "InvokedIntentSampleTypeDef",
    {
        "intentName": str,
    },
    total=False,
)

_RequiredListBotAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListBotAliasesRequestRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalListBotAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListBotAliasesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBotAliasesRequestRequestTypeDef(
    _RequiredListBotAliasesRequestRequestTypeDef, _OptionalListBotAliasesRequestRequestTypeDef
):
    pass


_RequiredListBotRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredListBotRecommendationsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListBotRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalListBotRecommendationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBotRecommendationsRequestRequestTypeDef(
    _RequiredListBotRecommendationsRequestRequestTypeDef,
    _OptionalListBotRecommendationsRequestRequestTypeDef,
):
    pass


_RequiredListCustomVocabularyItemsRequestRequestTypeDef = TypedDict(
    "_RequiredListCustomVocabularyItemsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListCustomVocabularyItemsRequestRequestTypeDef = TypedDict(
    "_OptionalListCustomVocabularyItemsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListCustomVocabularyItemsRequestRequestTypeDef(
    _RequiredListCustomVocabularyItemsRequestRequestTypeDef,
    _OptionalListCustomVocabularyItemsRequestRequestTypeDef,
):
    pass


_RequiredListRecommendedIntentsRequestRequestTypeDef = TypedDict(
    "_RequiredListRecommendedIntentsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
    },
)
_OptionalListRecommendedIntentsRequestRequestTypeDef = TypedDict(
    "_OptionalListRecommendedIntentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListRecommendedIntentsRequestRequestTypeDef(
    _RequiredListRecommendedIntentsRequestRequestTypeDef,
    _OptionalListRecommendedIntentsRequestRequestTypeDef,
):
    pass


RecommendedIntentSummaryTypeDef = TypedDict(
    "RecommendedIntentSummaryTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "sampleUtterancesCount": int,
    },
    total=False,
)

SessionDataSortByTypeDef = TypedDict(
    "SessionDataSortByTypeDef",
    {
        "name": AnalyticsSessionSortByNameType,
        "order": AnalyticsSortOrderType,
    },
)

SlotTypeFilterTypeDef = TypedDict(
    "SlotTypeFilterTypeDef",
    {
        "name": SlotTypeFilterNameType,
        "values": Sequence[str],
        "operator": SlotTypeFilterOperatorType,
    },
)

SlotTypeSortByTypeDef = TypedDict(
    "SlotTypeSortByTypeDef",
    {
        "attribute": SlotTypeSortAttributeType,
        "order": SortOrderType,
    },
)

SlotTypeSummaryTypeDef = TypedDict(
    "SlotTypeSummaryTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "parentSlotTypeSignature": str,
        "lastUpdatedDateTime": datetime,
        "slotTypeCategory": SlotTypeCategoryType,
    },
    total=False,
)

SlotFilterTypeDef = TypedDict(
    "SlotFilterTypeDef",
    {
        "name": Literal["SlotName"],
        "values": Sequence[str],
        "operator": SlotFilterOperatorType,
    },
)

SlotSortByTypeDef = TypedDict(
    "SlotSortByTypeDef",
    {
        "attribute": SlotSortAttributeType,
        "order": SortOrderType,
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestExecutionSortByTypeDef = TypedDict(
    "TestExecutionSortByTypeDef",
    {
        "attribute": TestExecutionSortAttributeType,
        "order": SortOrderType,
    },
)

_RequiredListTestSetRecordsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestSetRecordsRequestRequestTypeDef",
    {
        "testSetId": str,
    },
)
_OptionalListTestSetRecordsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestSetRecordsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTestSetRecordsRequestRequestTypeDef(
    _RequiredListTestSetRecordsRequestRequestTypeDef,
    _OptionalListTestSetRecordsRequestRequestTypeDef,
):
    pass


TestSetSortByTypeDef = TypedDict(
    "TestSetSortByTypeDef",
    {
        "attribute": TestSetSortAttributeType,
        "order": SortOrderType,
    },
)

UtteranceDataSortByTypeDef = TypedDict(
    "UtteranceDataSortByTypeDef",
    {
        "name": Literal["UtteranceTimestamp"],
        "order": AnalyticsSortOrderType,
    },
)

PlainTextMessageOutputTypeDef = TypedDict(
    "PlainTextMessageOutputTypeDef",
    {
        "value": str,
    },
)

SSMLMessageOutputTypeDef = TypedDict(
    "SSMLMessageOutputTypeDef",
    {
        "value": str,
    },
)

PlainTextMessageTypeDef = TypedDict(
    "PlainTextMessageTypeDef",
    {
        "value": str,
    },
)

SSMLMessageTypeDef = TypedDict(
    "SSMLMessageTypeDef",
    {
        "value": str,
    },
)

_RequiredOverallTestResultItemTypeDef = TypedDict(
    "_RequiredOverallTestResultItemTypeDef",
    {
        "multiTurnConversation": bool,
        "totalResultCount": int,
        "endToEndResultCounts": Dict[TestResultMatchStatusType, int],
    },
)
_OptionalOverallTestResultItemTypeDef = TypedDict(
    "_OptionalOverallTestResultItemTypeDef",
    {
        "speechTranscriptionResultCounts": Dict[TestResultMatchStatusType, int],
    },
    total=False,
)


class OverallTestResultItemTypeDef(
    _RequiredOverallTestResultItemTypeDef, _OptionalOverallTestResultItemTypeDef
):
    pass


PathFormatOutputTypeDef = TypedDict(
    "PathFormatOutputTypeDef",
    {
        "objectPrefixes": List[str],
    },
    total=False,
)

PathFormatTypeDef = TypedDict(
    "PathFormatTypeDef",
    {
        "objectPrefixes": Sequence[str],
    },
    total=False,
)

TextInputSpecificationOutputTypeDef = TypedDict(
    "TextInputSpecificationOutputTypeDef",
    {
        "startTimeoutMs": int,
    },
)

TextInputSpecificationTypeDef = TypedDict(
    "TextInputSpecificationTypeDef",
    {
        "startTimeoutMs": int,
    },
)

RelativeAggregationDurationOutputTypeDef = TypedDict(
    "RelativeAggregationDurationOutputTypeDef",
    {
        "timeDimension": TimeDimensionType,
        "timeValue": int,
    },
)

RelativeAggregationDurationTypeDef = TypedDict(
    "RelativeAggregationDurationTypeDef",
    {
        "timeDimension": TimeDimensionType,
        "timeValue": int,
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

RuntimeHintValueTypeDef = TypedDict(
    "RuntimeHintValueTypeDef",
    {
        "phrase": str,
    },
)

SampleValueOutputTypeDef = TypedDict(
    "SampleValueOutputTypeDef",
    {
        "value": str,
    },
)

SampleValueTypeDef = TypedDict(
    "SampleValueTypeDef",
    {
        "value": str,
    },
)

SlotDefaultValueOutputTypeDef = TypedDict(
    "SlotDefaultValueOutputTypeDef",
    {
        "defaultValue": str,
    },
)

SlotDefaultValueTypeDef = TypedDict(
    "SlotDefaultValueTypeDef",
    {
        "defaultValue": str,
    },
)

SlotPriorityTypeDef = TypedDict(
    "SlotPriorityTypeDef",
    {
        "priority": int,
        "slotId": str,
    },
)

_RequiredSlotResolutionTestResultItemCountsTypeDef = TypedDict(
    "_RequiredSlotResolutionTestResultItemCountsTypeDef",
    {
        "totalResultCount": int,
        "slotMatchResultCounts": Dict[TestResultMatchStatusType, int],
    },
)
_OptionalSlotResolutionTestResultItemCountsTypeDef = TypedDict(
    "_OptionalSlotResolutionTestResultItemCountsTypeDef",
    {
        "speechTranscriptionResultCounts": Dict[TestResultMatchStatusType, int],
    },
    total=False,
)


class SlotResolutionTestResultItemCountsTypeDef(
    _RequiredSlotResolutionTestResultItemCountsTypeDef,
    _OptionalSlotResolutionTestResultItemCountsTypeDef,
):
    pass


SlotValueOutputTypeDef = TypedDict(
    "SlotValueOutputTypeDef",
    {
        "interpretedValue": str,
    },
    total=False,
)

SlotValueTypeDef = TypedDict(
    "SlotValueTypeDef",
    {
        "interpretedValue": str,
    },
    total=False,
)

SlotValueRegexFilterOutputTypeDef = TypedDict(
    "SlotValueRegexFilterOutputTypeDef",
    {
        "pattern": str,
    },
)

SlotValueRegexFilterTypeDef = TypedDict(
    "SlotValueRegexFilterTypeDef",
    {
        "pattern": str,
    },
)

_RequiredTestSetStorageLocationTypeDef = TypedDict(
    "_RequiredTestSetStorageLocationTypeDef",
    {
        "s3BucketName": str,
        "s3Path": str,
    },
)
_OptionalTestSetStorageLocationTypeDef = TypedDict(
    "_OptionalTestSetStorageLocationTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class TestSetStorageLocationTypeDef(
    _RequiredTestSetStorageLocationTypeDef, _OptionalTestSetStorageLocationTypeDef
):
    pass


StopBotRecommendationRequestRequestTypeDef = TypedDict(
    "StopBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
    },
)

StopBotRecommendationResponseTypeDef = TypedDict(
    "StopBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Mapping[str, str],
    },
)

TestSetIntentDiscrepancyItemTypeDef = TypedDict(
    "TestSetIntentDiscrepancyItemTypeDef",
    {
        "intentName": str,
        "errorMessage": str,
    },
)

TestSetSlotDiscrepancyItemTypeDef = TypedDict(
    "TestSetSlotDiscrepancyItemTypeDef",
    {
        "intentName": str,
        "slotName": str,
        "errorMessage": str,
    },
)

TestSetDiscrepancyReportBotAliasTargetOutputTypeDef = TypedDict(
    "TestSetDiscrepancyReportBotAliasTargetOutputTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
    },
)

TestSetDiscrepancyReportBotAliasTargetTypeDef = TypedDict(
    "TestSetDiscrepancyReportBotAliasTargetTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
    },
)

TestSetImportInputLocationOutputTypeDef = TypedDict(
    "TestSetImportInputLocationOutputTypeDef",
    {
        "s3BucketName": str,
        "s3Path": str,
    },
)

TestSetImportInputLocationTypeDef = TypedDict(
    "TestSetImportInputLocationTypeDef",
    {
        "s3BucketName": str,
        "s3Path": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateExportRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)
_OptionalUpdateExportRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExportRequestRequestTypeDef",
    {
        "filePassword": str,
    },
    total=False,
)


class UpdateExportRequestRequestTypeDef(
    _RequiredUpdateExportRequestRequestTypeDef, _OptionalUpdateExportRequestRequestTypeDef
):
    pass


_RequiredUpdateResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
        "policy": str,
    },
)
_OptionalUpdateResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourcePolicyRequestRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)


class UpdateResourcePolicyRequestRequestTypeDef(
    _RequiredUpdateResourcePolicyRequestRequestTypeDef,
    _OptionalUpdateResourcePolicyRequestRequestTypeDef,
):
    pass


UpdateResourcePolicyResponseTypeDef = TypedDict(
    "UpdateResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTestSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTestSetRequestRequestTypeDef",
    {
        "testSetId": str,
        "testSetName": str,
    },
)
_OptionalUpdateTestSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTestSetRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class UpdateTestSetRequestRequestTypeDef(
    _RequiredUpdateTestSetRequestRequestTypeDef, _OptionalUpdateTestSetRequestRequestTypeDef
):
    pass


_RequiredUserTurnIntentOutputTypeDef = TypedDict(
    "_RequiredUserTurnIntentOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalUserTurnIntentOutputTypeDef = TypedDict(
    "_OptionalUserTurnIntentOutputTypeDef",
    {
        "slots": Dict[str, "UserTurnSlotOutputTypeDef"],
    },
    total=False,
)


class UserTurnIntentOutputTypeDef(
    _RequiredUserTurnIntentOutputTypeDef, _OptionalUserTurnIntentOutputTypeDef
):
    pass


UserTurnSlotOutputTypeDef = TypedDict(
    "UserTurnSlotOutputTypeDef",
    {
        "value": str,
        "values": List[Dict[str, Any]],
        "subSlots": Dict[str, Dict[str, Any]],
    },
    total=False,
)

UtteranceAudioInputSpecificationTypeDef = TypedDict(
    "UtteranceAudioInputSpecificationTypeDef",
    {
        "audioFileS3Location": str,
    },
)

_RequiredAgentTurnResultTypeDef = TypedDict(
    "_RequiredAgentTurnResultTypeDef",
    {
        "expectedAgentPrompt": str,
    },
)
_OptionalAgentTurnResultTypeDef = TypedDict(
    "_OptionalAgentTurnResultTypeDef",
    {
        "actualAgentPrompt": str,
        "errorDetails": ExecutionErrorDetailsTypeDef,
        "actualElicitedSlot": str,
        "actualIntent": str,
    },
    total=False,
)


class AgentTurnResultTypeDef(_RequiredAgentTurnResultTypeDef, _OptionalAgentTurnResultTypeDef):
    pass


AnalyticsIntentResultTypeDef = TypedDict(
    "AnalyticsIntentResultTypeDef",
    {
        "binKeys": List[AnalyticsBinKeyTypeDef],
        "groupByKeys": List[AnalyticsIntentGroupByKeyTypeDef],
        "metricsResults": List[AnalyticsIntentMetricResultTypeDef],
    },
    total=False,
)

_RequiredListIntentMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntentMetricsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "metrics": Sequence[AnalyticsIntentMetricTypeDef],
    },
)
_OptionalListIntentMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntentMetricsRequestRequestTypeDef",
    {
        "binBy": Sequence[AnalyticsBinBySpecificationTypeDef],
        "groupBy": Sequence[AnalyticsIntentGroupBySpecificationTypeDef],
        "filters": Sequence[AnalyticsIntentFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListIntentMetricsRequestRequestTypeDef(
    _RequiredListIntentMetricsRequestRequestTypeDef, _OptionalListIntentMetricsRequestRequestTypeDef
):
    pass


ListIntentPathsResponseTypeDef = TypedDict(
    "ListIntentPathsResponseTypeDef",
    {
        "nodeSummaries": List[AnalyticsIntentNodeSummaryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnalyticsIntentStageResultTypeDef = TypedDict(
    "AnalyticsIntentStageResultTypeDef",
    {
        "binKeys": List[AnalyticsBinKeyTypeDef],
        "groupByKeys": List[AnalyticsIntentStageGroupByKeyTypeDef],
        "metricsResults": List[AnalyticsIntentStageMetricResultTypeDef],
    },
    total=False,
)

_RequiredListIntentStageMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntentStageMetricsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "metrics": Sequence[AnalyticsIntentStageMetricTypeDef],
    },
)
_OptionalListIntentStageMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntentStageMetricsRequestRequestTypeDef",
    {
        "binBy": Sequence[AnalyticsBinBySpecificationTypeDef],
        "groupBy": Sequence[AnalyticsIntentStageGroupBySpecificationTypeDef],
        "filters": Sequence[AnalyticsIntentStageFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListIntentStageMetricsRequestRequestTypeDef(
    _RequiredListIntentStageMetricsRequestRequestTypeDef,
    _OptionalListIntentStageMetricsRequestRequestTypeDef,
):
    pass


_RequiredListIntentPathsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntentPathsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "intentPath": str,
    },
)
_OptionalListIntentPathsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntentPathsRequestRequestTypeDef",
    {
        "filters": Sequence[AnalyticsPathFilterTypeDef],
    },
    total=False,
)


class ListIntentPathsRequestRequestTypeDef(
    _RequiredListIntentPathsRequestRequestTypeDef, _OptionalListIntentPathsRequestRequestTypeDef
):
    pass


AnalyticsSessionResultTypeDef = TypedDict(
    "AnalyticsSessionResultTypeDef",
    {
        "binKeys": List[AnalyticsBinKeyTypeDef],
        "groupByKeys": List[AnalyticsSessionGroupByKeyTypeDef],
        "metricsResults": List[AnalyticsSessionMetricResultTypeDef],
    },
    total=False,
)

_RequiredListSessionMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListSessionMetricsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "metrics": Sequence[AnalyticsSessionMetricTypeDef],
    },
)
_OptionalListSessionMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListSessionMetricsRequestRequestTypeDef",
    {
        "binBy": Sequence[AnalyticsBinBySpecificationTypeDef],
        "groupBy": Sequence[AnalyticsSessionGroupBySpecificationTypeDef],
        "filters": Sequence[AnalyticsSessionFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListSessionMetricsRequestRequestTypeDef(
    _RequiredListSessionMetricsRequestRequestTypeDef,
    _OptionalListSessionMetricsRequestRequestTypeDef,
):
    pass


AnalyticsUtteranceResultTypeDef = TypedDict(
    "AnalyticsUtteranceResultTypeDef",
    {
        "binKeys": List[AnalyticsBinKeyTypeDef],
        "groupByKeys": List[AnalyticsUtteranceGroupByKeyTypeDef],
        "metricsResults": List[AnalyticsUtteranceMetricResultTypeDef],
        "attributeResults": List[AnalyticsUtteranceAttributeResultTypeDef],
    },
    total=False,
)

_RequiredListUtteranceMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredListUtteranceMetricsRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "metrics": Sequence[AnalyticsUtteranceMetricTypeDef],
    },
)
_OptionalListUtteranceMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalListUtteranceMetricsRequestRequestTypeDef",
    {
        "binBy": Sequence[AnalyticsBinBySpecificationTypeDef],
        "groupBy": Sequence[AnalyticsUtteranceGroupBySpecificationTypeDef],
        "attributes": Sequence[AnalyticsUtteranceAttributeTypeDef],
        "filters": Sequence[AnalyticsUtteranceFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListUtteranceMetricsRequestRequestTypeDef(
    _RequiredListUtteranceMetricsRequestRequestTypeDef,
    _OptionalListUtteranceMetricsRequestRequestTypeDef,
):
    pass


_RequiredSearchAssociatedTranscriptsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchAssociatedTranscriptsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "filters": Sequence[AssociatedTranscriptFilterTypeDef],
    },
)
_OptionalSearchAssociatedTranscriptsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchAssociatedTranscriptsRequestRequestTypeDef",
    {
        "searchOrder": SearchOrderType,
        "maxResults": int,
        "nextIndex": int,
    },
    total=False,
)


class SearchAssociatedTranscriptsRequestRequestTypeDef(
    _RequiredSearchAssociatedTranscriptsRequestRequestTypeDef,
    _OptionalSearchAssociatedTranscriptsRequestRequestTypeDef,
):
    pass


SearchAssociatedTranscriptsResponseTypeDef = TypedDict(
    "SearchAssociatedTranscriptsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "nextIndex": int,
        "associatedTranscripts": List[AssociatedTranscriptTypeDef],
        "totalResults": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAudioAndDTMFInputSpecificationOutputTypeDef = TypedDict(
    "_RequiredAudioAndDTMFInputSpecificationOutputTypeDef",
    {
        "startTimeoutMs": int,
    },
)
_OptionalAudioAndDTMFInputSpecificationOutputTypeDef = TypedDict(
    "_OptionalAudioAndDTMFInputSpecificationOutputTypeDef",
    {
        "audioSpecification": AudioSpecificationOutputTypeDef,
        "dtmfSpecification": DTMFSpecificationOutputTypeDef,
    },
    total=False,
)


class AudioAndDTMFInputSpecificationOutputTypeDef(
    _RequiredAudioAndDTMFInputSpecificationOutputTypeDef,
    _OptionalAudioAndDTMFInputSpecificationOutputTypeDef,
):
    pass


_RequiredAudioAndDTMFInputSpecificationTypeDef = TypedDict(
    "_RequiredAudioAndDTMFInputSpecificationTypeDef",
    {
        "startTimeoutMs": int,
    },
)
_OptionalAudioAndDTMFInputSpecificationTypeDef = TypedDict(
    "_OptionalAudioAndDTMFInputSpecificationTypeDef",
    {
        "audioSpecification": AudioSpecificationTypeDef,
        "dtmfSpecification": DTMFSpecificationTypeDef,
    },
    total=False,
)


class AudioAndDTMFInputSpecificationTypeDef(
    _RequiredAudioAndDTMFInputSpecificationTypeDef, _OptionalAudioAndDTMFInputSpecificationTypeDef
):
    pass


AudioLogDestinationOutputTypeDef = TypedDict(
    "AudioLogDestinationOutputTypeDef",
    {
        "s3Bucket": S3BucketLogDestinationOutputTypeDef,
    },
)

AudioLogDestinationTypeDef = TypedDict(
    "AudioLogDestinationTypeDef",
    {
        "s3Bucket": S3BucketLogDestinationTypeDef,
    },
)

BatchCreateCustomVocabularyItemRequestRequestTypeDef = TypedDict(
    "BatchCreateCustomVocabularyItemRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyItemList": Sequence[NewCustomVocabularyItemTypeDef],
    },
)

ListCustomVocabularyItemsResponseTypeDef = TypedDict(
    "ListCustomVocabularyItemsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyItems": List[CustomVocabularyItemOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateCustomVocabularyItemResponseTypeDef = TypedDict(
    "BatchCreateCustomVocabularyItemResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "errors": List[FailedCustomVocabularyItemTypeDef],
        "resources": List[CustomVocabularyItemOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteCustomVocabularyItemResponseTypeDef = TypedDict(
    "BatchDeleteCustomVocabularyItemResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "errors": List[FailedCustomVocabularyItemTypeDef],
        "resources": List[CustomVocabularyItemOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateCustomVocabularyItemResponseTypeDef = TypedDict(
    "BatchUpdateCustomVocabularyItemResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "errors": List[FailedCustomVocabularyItemTypeDef],
        "resources": List[CustomVocabularyItemOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteCustomVocabularyItemRequestRequestTypeDef = TypedDict(
    "BatchDeleteCustomVocabularyItemRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyItemList": Sequence[CustomVocabularyEntryIdTypeDef],
    },
)

BatchUpdateCustomVocabularyItemRequestRequestTypeDef = TypedDict(
    "BatchUpdateCustomVocabularyItemRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "customVocabularyItemList": Sequence[CustomVocabularyItemTypeDef],
    },
)

ListBotAliasesResponseTypeDef = TypedDict(
    "ListBotAliasesResponseTypeDef",
    {
        "botAliasSummaries": List[BotAliasSummaryTypeDef],
        "nextToken": str,
        "botId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestExecutionTargetOutputTypeDef = TypedDict(
    "TestExecutionTargetOutputTypeDef",
    {
        "botAliasTarget": BotAliasTestExecutionTargetOutputTypeDef,
    },
    total=False,
)

TestExecutionTargetTypeDef = TypedDict(
    "TestExecutionTargetTypeDef",
    {
        "botAliasTarget": BotAliasTestExecutionTargetTypeDef,
    },
    total=False,
)

_RequiredBotImportSpecificationOutputTypeDef = TypedDict(
    "_RequiredBotImportSpecificationOutputTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": DataPrivacyOutputTypeDef,
    },
)
_OptionalBotImportSpecificationOutputTypeDef = TypedDict(
    "_OptionalBotImportSpecificationOutputTypeDef",
    {
        "idleSessionTTLInSeconds": int,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
    },
    total=False,
)


class BotImportSpecificationOutputTypeDef(
    _RequiredBotImportSpecificationOutputTypeDef, _OptionalBotImportSpecificationOutputTypeDef
):
    pass


_RequiredBotImportSpecificationTypeDef = TypedDict(
    "_RequiredBotImportSpecificationTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": DataPrivacyTypeDef,
    },
)
_OptionalBotImportSpecificationTypeDef = TypedDict(
    "_OptionalBotImportSpecificationTypeDef",
    {
        "idleSessionTTLInSeconds": int,
        "botTags": Mapping[str, str],
        "testBotAliasTags": Mapping[str, str],
    },
    total=False,
)


class BotImportSpecificationTypeDef(
    _RequiredBotImportSpecificationTypeDef, _OptionalBotImportSpecificationTypeDef
):
    pass


_RequiredBotLocaleImportSpecificationOutputTypeDef = TypedDict(
    "_RequiredBotLocaleImportSpecificationOutputTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalBotLocaleImportSpecificationOutputTypeDef = TypedDict(
    "_OptionalBotLocaleImportSpecificationOutputTypeDef",
    {
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": VoiceSettingsOutputTypeDef,
    },
    total=False,
)


class BotLocaleImportSpecificationOutputTypeDef(
    _RequiredBotLocaleImportSpecificationOutputTypeDef,
    _OptionalBotLocaleImportSpecificationOutputTypeDef,
):
    pass


CreateBotLocaleResponseTypeDef = TypedDict(
    "CreateBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeName": str,
        "localeId": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": VoiceSettingsOutputTypeDef,
        "botLocaleStatus": BotLocaleStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotLocaleResponseTypeDef = TypedDict(
    "DescribeBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "localeName": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": VoiceSettingsOutputTypeDef,
        "intentsCount": int,
        "slotTypesCount": int,
        "botLocaleStatus": BotLocaleStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
        "botLocaleHistoryEvents": List[BotLocaleHistoryEventTypeDef],
        "recommendedActions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotLocaleResponseTypeDef = TypedDict(
    "UpdateBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "localeName": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": VoiceSettingsOutputTypeDef,
        "botLocaleStatus": BotLocaleStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "recommendedActions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBotLocaleImportSpecificationTypeDef = TypedDict(
    "_RequiredBotLocaleImportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalBotLocaleImportSpecificationTypeDef = TypedDict(
    "_OptionalBotLocaleImportSpecificationTypeDef",
    {
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": VoiceSettingsTypeDef,
    },
    total=False,
)


class BotLocaleImportSpecificationTypeDef(
    _RequiredBotLocaleImportSpecificationTypeDef, _OptionalBotLocaleImportSpecificationTypeDef
):
    pass


_RequiredCreateBotLocaleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": float,
    },
)
_OptionalCreateBotLocaleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotLocaleRequestRequestTypeDef",
    {
        "description": str,
        "voiceSettings": VoiceSettingsTypeDef,
    },
    total=False,
)


class CreateBotLocaleRequestRequestTypeDef(
    _RequiredCreateBotLocaleRequestRequestTypeDef, _OptionalCreateBotLocaleRequestRequestTypeDef
):
    pass


_RequiredUpdateBotLocaleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBotLocaleRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": float,
    },
)
_OptionalUpdateBotLocaleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBotLocaleRequestRequestTypeDef",
    {
        "description": str,
        "voiceSettings": VoiceSettingsTypeDef,
    },
    total=False,
)


class UpdateBotLocaleRequestRequestTypeDef(
    _RequiredUpdateBotLocaleRequestRequestTypeDef, _OptionalUpdateBotLocaleRequestRequestTypeDef
):
    pass


_RequiredListBotLocalesRequestRequestTypeDef = TypedDict(
    "_RequiredListBotLocalesRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)
_OptionalListBotLocalesRequestRequestTypeDef = TypedDict(
    "_OptionalListBotLocalesRequestRequestTypeDef",
    {
        "sortBy": BotLocaleSortByTypeDef,
        "filters": Sequence[BotLocaleFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBotLocalesRequestRequestTypeDef(
    _RequiredListBotLocalesRequestRequestTypeDef, _OptionalListBotLocalesRequestRequestTypeDef
):
    pass


ListBotLocalesResponseTypeDef = TypedDict(
    "ListBotLocalesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "nextToken": str,
        "botLocaleSummaries": List[BotLocaleSummaryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBotResponseTypeDef = TypedDict(
    "CreateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": DataPrivacyOutputTypeDef,
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
        "botType": BotTypeType,
        "botMembers": List[BotMemberOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotResponseTypeDef = TypedDict(
    "DescribeBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": DataPrivacyOutputTypeDef,
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "botType": BotTypeType,
        "botMembers": List[BotMemberOutputTypeDef],
        "failureReasons": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotResponseTypeDef = TypedDict(
    "UpdateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": DataPrivacyOutputTypeDef,
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "botType": BotTypeType,
        "botMembers": List[BotMemberOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotRequestRequestTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": DataPrivacyTypeDef,
        "idleSessionTTLInSeconds": int,
    },
)
_OptionalCreateBotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotRequestRequestTypeDef",
    {
        "description": str,
        "botTags": Mapping[str, str],
        "testBotAliasTags": Mapping[str, str],
        "botType": BotTypeType,
        "botMembers": Sequence[BotMemberTypeDef],
    },
    total=False,
)


class CreateBotRequestRequestTypeDef(
    _RequiredCreateBotRequestRequestTypeDef, _OptionalCreateBotRequestRequestTypeDef
):
    pass


_RequiredUpdateBotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBotRequestRequestTypeDef",
    {
        "botId": str,
        "botName": str,
        "roleArn": str,
        "dataPrivacy": DataPrivacyTypeDef,
        "idleSessionTTLInSeconds": int,
    },
)
_OptionalUpdateBotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBotRequestRequestTypeDef",
    {
        "description": str,
        "botType": BotTypeType,
        "botMembers": Sequence[BotMemberTypeDef],
    },
    total=False,
)


class UpdateBotRequestRequestTypeDef(
    _RequiredUpdateBotRequestRequestTypeDef, _OptionalUpdateBotRequestRequestTypeDef
):
    pass


BotRecommendationResultStatisticsTypeDef = TypedDict(
    "BotRecommendationResultStatisticsTypeDef",
    {
        "intents": IntentStatisticsTypeDef,
        "slotTypes": SlotTypeStatisticsTypeDef,
    },
    total=False,
)

ListBotRecommendationsResponseTypeDef = TypedDict(
    "ListBotRecommendationsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationSummaries": List[BotRecommendationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotsRequestRequestTypeDef = TypedDict(
    "ListBotsRequestRequestTypeDef",
    {
        "sortBy": BotSortByTypeDef,
        "filters": Sequence[BotFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "botSummaries": List[BotSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBotVersionResponseTypeDef = TypedDict(
    "CreateBotVersionResponseTypeDef",
    {
        "botId": str,
        "description": str,
        "botVersion": str,
        "botVersionLocaleSpecification": Dict[str, BotVersionLocaleDetailsOutputTypeDef],
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotVersionRequestRequestTypeDef",
    {
        "botId": str,
        "botVersionLocaleSpecification": Mapping[str, BotVersionLocaleDetailsTypeDef],
    },
)
_OptionalCreateBotVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotVersionRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class CreateBotVersionRequestRequestTypeDef(
    _RequiredCreateBotVersionRequestRequestTypeDef, _OptionalCreateBotVersionRequestRequestTypeDef
):
    pass


_RequiredListBotVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListBotVersionsRequestRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalListBotVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListBotVersionsRequestRequestTypeDef",
    {
        "sortBy": BotVersionSortByTypeDef,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBotVersionsRequestRequestTypeDef(
    _RequiredListBotVersionsRequestRequestTypeDef, _OptionalListBotVersionsRequestRequestTypeDef
):
    pass


ListBotVersionsResponseTypeDef = TypedDict(
    "ListBotVersionsResponseTypeDef",
    {
        "botId": str,
        "botVersionSummaries": List[BotVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBuiltInIntentsRequestRequestTypeDef = TypedDict(
    "_RequiredListBuiltInIntentsRequestRequestTypeDef",
    {
        "localeId": str,
    },
)
_OptionalListBuiltInIntentsRequestRequestTypeDef = TypedDict(
    "_OptionalListBuiltInIntentsRequestRequestTypeDef",
    {
        "sortBy": BuiltInIntentSortByTypeDef,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBuiltInIntentsRequestRequestTypeDef(
    _RequiredListBuiltInIntentsRequestRequestTypeDef,
    _OptionalListBuiltInIntentsRequestRequestTypeDef,
):
    pass


ListBuiltInIntentsResponseTypeDef = TypedDict(
    "ListBuiltInIntentsResponseTypeDef",
    {
        "builtInIntentSummaries": List[BuiltInIntentSummaryTypeDef],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBuiltInSlotTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListBuiltInSlotTypesRequestRequestTypeDef",
    {
        "localeId": str,
    },
)
_OptionalListBuiltInSlotTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListBuiltInSlotTypesRequestRequestTypeDef",
    {
        "sortBy": BuiltInSlotTypeSortByTypeDef,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBuiltInSlotTypesRequestRequestTypeDef(
    _RequiredListBuiltInSlotTypesRequestRequestTypeDef,
    _OptionalListBuiltInSlotTypesRequestRequestTypeDef,
):
    pass


ListBuiltInSlotTypesResponseTypeDef = TypedDict(
    "ListBuiltInSlotTypesResponseTypeDef",
    {
        "builtInSlotTypeSummaries": List[BuiltInSlotTypeSummaryTypeDef],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImageResponseCardOutputTypeDef = TypedDict(
    "_RequiredImageResponseCardOutputTypeDef",
    {
        "title": str,
    },
)
_OptionalImageResponseCardOutputTypeDef = TypedDict(
    "_OptionalImageResponseCardOutputTypeDef",
    {
        "subtitle": str,
        "imageUrl": str,
        "buttons": List[ButtonOutputTypeDef],
    },
    total=False,
)


class ImageResponseCardOutputTypeDef(
    _RequiredImageResponseCardOutputTypeDef, _OptionalImageResponseCardOutputTypeDef
):
    pass


_RequiredImageResponseCardTypeDef = TypedDict(
    "_RequiredImageResponseCardTypeDef",
    {
        "title": str,
    },
)
_OptionalImageResponseCardTypeDef = TypedDict(
    "_OptionalImageResponseCardTypeDef",
    {
        "subtitle": str,
        "imageUrl": str,
        "buttons": Sequence[ButtonTypeDef],
    },
    total=False,
)


class ImageResponseCardTypeDef(
    _RequiredImageResponseCardTypeDef, _OptionalImageResponseCardTypeDef
):
    pass


TextLogDestinationOutputTypeDef = TypedDict(
    "TextLogDestinationOutputTypeDef",
    {
        "cloudWatch": CloudWatchLogGroupLogDestinationOutputTypeDef,
    },
)

TextLogDestinationTypeDef = TypedDict(
    "TextLogDestinationTypeDef",
    {
        "cloudWatch": CloudWatchLogGroupLogDestinationTypeDef,
    },
)

CodeHookSpecificationOutputTypeDef = TypedDict(
    "CodeHookSpecificationOutputTypeDef",
    {
        "lambdaCodeHook": LambdaCodeHookOutputTypeDef,
    },
)

CodeHookSpecificationTypeDef = TypedDict(
    "CodeHookSpecificationTypeDef",
    {
        "lambdaCodeHook": LambdaCodeHookTypeDef,
    },
)

CompositeSlotTypeSettingOutputTypeDef = TypedDict(
    "CompositeSlotTypeSettingOutputTypeDef",
    {
        "subSlots": List[SubSlotTypeCompositionOutputTypeDef],
    },
    total=False,
)

CompositeSlotTypeSettingTypeDef = TypedDict(
    "CompositeSlotTypeSettingTypeDef",
    {
        "subSlots": Sequence[SubSlotTypeCompositionTypeDef],
    },
    total=False,
)

_RequiredConversationLevelTestResultItemTypeDef = TypedDict(
    "_RequiredConversationLevelTestResultItemTypeDef",
    {
        "conversationId": str,
        "endToEndResult": TestResultMatchStatusType,
        "intentClassificationResults": List[ConversationLevelIntentClassificationResultItemTypeDef],
        "slotResolutionResults": List[ConversationLevelSlotResolutionResultItemTypeDef],
    },
)
_OptionalConversationLevelTestResultItemTypeDef = TypedDict(
    "_OptionalConversationLevelTestResultItemTypeDef",
    {
        "speechTranscriptionResult": TestResultMatchStatusType,
    },
    total=False,
)


class ConversationLevelTestResultItemTypeDef(
    _RequiredConversationLevelTestResultItemTypeDef, _OptionalConversationLevelTestResultItemTypeDef
):
    pass


_RequiredTestExecutionResultFilterByTypeDef = TypedDict(
    "_RequiredTestExecutionResultFilterByTypeDef",
    {
        "resultTypeFilter": TestResultTypeFilterType,
    },
)
_OptionalTestExecutionResultFilterByTypeDef = TypedDict(
    "_OptionalTestExecutionResultFilterByTypeDef",
    {
        "conversationLevelTestResultsFilterBy": ConversationLevelTestResultsFilterByTypeDef,
    },
    total=False,
)


class TestExecutionResultFilterByTypeDef(
    _RequiredTestExecutionResultFilterByTypeDef, _OptionalTestExecutionResultFilterByTypeDef
):
    pass


ConversationLogsDataSourceOutputTypeDef = TypedDict(
    "ConversationLogsDataSourceOutputTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "filter": ConversationLogsDataSourceFilterByOutputTypeDef,
    },
)

ConversationLogsDataSourceTypeDef = TypedDict(
    "ConversationLogsDataSourceTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "filter": ConversationLogsDataSourceFilterByTypeDef,
    },
)

IntentSummaryTypeDef = TypedDict(
    "IntentSummaryTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "inputContexts": List[InputContextOutputTypeDef],
        "outputContexts": List[OutputContextOutputTypeDef],
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

_RequiredCreateResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResourcePolicyStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "statementId": str,
        "effect": EffectType,
        "principal": Sequence[PrincipalTypeDef],
        "action": Sequence[str],
    },
)
_OptionalCreateResourcePolicyStatementRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResourcePolicyStatementRequestRequestTypeDef",
    {
        "condition": Mapping[str, Mapping[str, str]],
        "expectedRevisionId": str,
    },
    total=False,
)


class CreateResourcePolicyStatementRequestRequestTypeDef(
    _RequiredCreateResourcePolicyStatementRequestRequestTypeDef,
    _OptionalCreateResourcePolicyStatementRequestRequestTypeDef,
):
    pass


LexTranscriptFilterOutputTypeDef = TypedDict(
    "LexTranscriptFilterOutputTypeDef",
    {
        "dateRangeFilter": DateRangeFilterOutputTypeDef,
    },
    total=False,
)

LexTranscriptFilterTypeDef = TypedDict(
    "LexTranscriptFilterTypeDef",
    {
        "dateRangeFilter": DateRangeFilterTypeDef,
    },
    total=False,
)

_RequiredDescribeBotAliasRequestBotAliasAvailableWaitTypeDef = TypedDict(
    "_RequiredDescribeBotAliasRequestBotAliasAvailableWaitTypeDef",
    {
        "botAliasId": str,
        "botId": str,
    },
)
_OptionalDescribeBotAliasRequestBotAliasAvailableWaitTypeDef = TypedDict(
    "_OptionalDescribeBotAliasRequestBotAliasAvailableWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeBotAliasRequestBotAliasAvailableWaitTypeDef(
    _RequiredDescribeBotAliasRequestBotAliasAvailableWaitTypeDef,
    _OptionalDescribeBotAliasRequestBotAliasAvailableWaitTypeDef,
):
    pass


_RequiredDescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef = TypedDict(
    "_RequiredDescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalDescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef = TypedDict(
    "_OptionalDescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef(
    _RequiredDescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef,
    _OptionalDescribeBotLocaleRequestBotLocaleBuiltWaitTypeDef,
):
    pass


_RequiredDescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef = TypedDict(
    "_RequiredDescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalDescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef = TypedDict(
    "_OptionalDescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef(
    _RequiredDescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef,
    _OptionalDescribeBotLocaleRequestBotLocaleCreatedWaitTypeDef,
):
    pass


_RequiredDescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef = TypedDict(
    "_RequiredDescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalDescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef = TypedDict(
    "_OptionalDescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef(
    _RequiredDescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef,
    _OptionalDescribeBotLocaleRequestBotLocaleExpressTestingAvailableWaitTypeDef,
):
    pass


_RequiredDescribeBotRequestBotAvailableWaitTypeDef = TypedDict(
    "_RequiredDescribeBotRequestBotAvailableWaitTypeDef",
    {
        "botId": str,
    },
)
_OptionalDescribeBotRequestBotAvailableWaitTypeDef = TypedDict(
    "_OptionalDescribeBotRequestBotAvailableWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeBotRequestBotAvailableWaitTypeDef(
    _RequiredDescribeBotRequestBotAvailableWaitTypeDef,
    _OptionalDescribeBotRequestBotAvailableWaitTypeDef,
):
    pass


_RequiredDescribeBotVersionRequestBotVersionAvailableWaitTypeDef = TypedDict(
    "_RequiredDescribeBotVersionRequestBotVersionAvailableWaitTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)
_OptionalDescribeBotVersionRequestBotVersionAvailableWaitTypeDef = TypedDict(
    "_OptionalDescribeBotVersionRequestBotVersionAvailableWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeBotVersionRequestBotVersionAvailableWaitTypeDef(
    _RequiredDescribeBotVersionRequestBotVersionAvailableWaitTypeDef,
    _OptionalDescribeBotVersionRequestBotVersionAvailableWaitTypeDef,
):
    pass


_RequiredDescribeExportRequestBotExportCompletedWaitTypeDef = TypedDict(
    "_RequiredDescribeExportRequestBotExportCompletedWaitTypeDef",
    {
        "exportId": str,
    },
)
_OptionalDescribeExportRequestBotExportCompletedWaitTypeDef = TypedDict(
    "_OptionalDescribeExportRequestBotExportCompletedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeExportRequestBotExportCompletedWaitTypeDef(
    _RequiredDescribeExportRequestBotExportCompletedWaitTypeDef,
    _OptionalDescribeExportRequestBotExportCompletedWaitTypeDef,
):
    pass


_RequiredDescribeImportRequestBotImportCompletedWaitTypeDef = TypedDict(
    "_RequiredDescribeImportRequestBotImportCompletedWaitTypeDef",
    {
        "importId": str,
    },
)
_OptionalDescribeImportRequestBotImportCompletedWaitTypeDef = TypedDict(
    "_OptionalDescribeImportRequestBotImportCompletedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeImportRequestBotImportCompletedWaitTypeDef(
    _RequiredDescribeImportRequestBotImportCompletedWaitTypeDef,
    _OptionalDescribeImportRequestBotImportCompletedWaitTypeDef,
):
    pass


DescribeBotVersionResponseTypeDef = TypedDict(
    "DescribeBotVersionResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "botVersion": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": DataPrivacyOutputTypeDef,
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "parentBotNetworks": List[ParentBotNetworkTypeDef],
        "botType": BotTypeType,
        "botMembers": List[BotMemberOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTestSetResponseTypeDef = TypedDict(
    "DescribeTestSetResponseTypeDef",
    {
        "testSetId": str,
        "testSetName": str,
        "description": str,
        "modality": TestSetModalityType,
        "status": TestSetStatusType,
        "roleArn": str,
        "numTurns": int,
        "storageLocation": TestSetStorageLocationOutputTypeDef,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestSetSummaryTypeDef = TypedDict(
    "TestSetSummaryTypeDef",
    {
        "testSetId": str,
        "testSetName": str,
        "description": str,
        "modality": TestSetModalityType,
        "status": TestSetStatusType,
        "roleArn": str,
        "numTurns": int,
        "storageLocation": TestSetStorageLocationOutputTypeDef,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateTestSetResponseTypeDef = TypedDict(
    "UpdateTestSetResponseTypeDef",
    {
        "testSetId": str,
        "testSetName": str,
        "description": str,
        "modality": TestSetModalityType,
        "status": TestSetStatusType,
        "roleArn": str,
        "numTurns": int,
        "storageLocation": TestSetStorageLocationOutputTypeDef,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DialogStateOutputTypeDef = TypedDict(
    "DialogStateOutputTypeDef",
    {
        "dialogAction": DialogActionOutputTypeDef,
        "intent": IntentOverrideOutputTypeDef,
        "sessionAttributes": Dict[str, str],
    },
    total=False,
)

DialogStateTypeDef = TypedDict(
    "DialogStateTypeDef",
    {
        "dialogAction": DialogActionTypeDef,
        "intent": IntentOverrideTypeDef,
        "sessionAttributes": Mapping[str, str],
    },
    total=False,
)

UpdateBotRecommendationRequestRequestTypeDef = TypedDict(
    "UpdateBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "encryptionSetting": EncryptionSettingTypeDef,
    },
)

ExportResourceSpecificationOutputTypeDef = TypedDict(
    "ExportResourceSpecificationOutputTypeDef",
    {
        "botExportSpecification": BotExportSpecificationOutputTypeDef,
        "botLocaleExportSpecification": BotLocaleExportSpecificationOutputTypeDef,
        "customVocabularyExportSpecification": CustomVocabularyExportSpecificationOutputTypeDef,
        "testSetExportSpecification": TestSetExportSpecificationOutputTypeDef,
    },
    total=False,
)

ExportResourceSpecificationTypeDef = TypedDict(
    "ExportResourceSpecificationTypeDef",
    {
        "botExportSpecification": BotExportSpecificationTypeDef,
        "botLocaleExportSpecification": BotLocaleExportSpecificationTypeDef,
        "customVocabularyExportSpecification": CustomVocabularyExportSpecificationTypeDef,
        "testSetExportSpecification": TestSetExportSpecificationTypeDef,
    },
    total=False,
)

ListExportsRequestRequestTypeDef = TypedDict(
    "ListExportsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "sortBy": ExportSortByTypeDef,
        "filters": Sequence[ExportFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
        "localeId": str,
    },
    total=False,
)

GrammarSlotTypeSettingOutputTypeDef = TypedDict(
    "GrammarSlotTypeSettingOutputTypeDef",
    {
        "source": GrammarSlotTypeSourceOutputTypeDef,
    },
    total=False,
)

GrammarSlotTypeSettingTypeDef = TypedDict(
    "GrammarSlotTypeSettingTypeDef",
    {
        "source": GrammarSlotTypeSourceTypeDef,
    },
    total=False,
)

ListImportsRequestRequestTypeDef = TypedDict(
    "ListImportsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "sortBy": ImportSortByTypeDef,
        "filters": Sequence[ImportFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
        "localeId": str,
    },
    total=False,
)

ListImportsResponseTypeDef = TypedDict(
    "ListImportsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "importSummaries": List[ImportSummaryTypeDef],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputSessionStateSpecificationTypeDef = TypedDict(
    "InputSessionStateSpecificationTypeDef",
    {
        "sessionAttributes": Dict[str, str],
        "activeContexts": List[ActiveContextTypeDef],
        "runtimeHints": RuntimeHintsTypeDef,
    },
    total=False,
)

IntentClassificationTestResultItemTypeDef = TypedDict(
    "IntentClassificationTestResultItemTypeDef",
    {
        "intentName": str,
        "multiTurnConversation": bool,
        "resultCounts": IntentClassificationTestResultItemCountsTypeDef,
    },
)

_RequiredListIntentsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntentsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListIntentsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntentsRequestRequestTypeDef",
    {
        "sortBy": IntentSortByTypeDef,
        "filters": Sequence[IntentFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListIntentsRequestRequestTypeDef(
    _RequiredListIntentsRequestRequestTypeDef, _OptionalListIntentsRequestRequestTypeDef
):
    pass


SessionSpecificationTypeDef = TypedDict(
    "SessionSpecificationTypeDef",
    {
        "botAliasId": str,
        "botVersion": str,
        "localeId": str,
        "channel": str,
        "sessionId": str,
        "conversationStartTime": datetime,
        "conversationEndTime": datetime,
        "conversationDurationSeconds": int,
        "conversationEndState": ConversationEndStateType,
        "mode": AnalyticsModalityType,
        "numberOfTurns": int,
        "invokedIntentSamples": List[InvokedIntentSampleTypeDef],
        "originatingRequestId": str,
    },
    total=False,
)

ListRecommendedIntentsResponseTypeDef = TypedDict(
    "ListRecommendedIntentsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationId": str,
        "summaryList": List[RecommendedIntentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSessionAnalyticsDataRequestRequestTypeDef = TypedDict(
    "_RequiredListSessionAnalyticsDataRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
    },
)
_OptionalListSessionAnalyticsDataRequestRequestTypeDef = TypedDict(
    "_OptionalListSessionAnalyticsDataRequestRequestTypeDef",
    {
        "sortBy": SessionDataSortByTypeDef,
        "filters": Sequence[AnalyticsSessionFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListSessionAnalyticsDataRequestRequestTypeDef(
    _RequiredListSessionAnalyticsDataRequestRequestTypeDef,
    _OptionalListSessionAnalyticsDataRequestRequestTypeDef,
):
    pass


_RequiredListSlotTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListSlotTypesRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListSlotTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListSlotTypesRequestRequestTypeDef",
    {
        "sortBy": SlotTypeSortByTypeDef,
        "filters": Sequence[SlotTypeFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListSlotTypesRequestRequestTypeDef(
    _RequiredListSlotTypesRequestRequestTypeDef, _OptionalListSlotTypesRequestRequestTypeDef
):
    pass


ListSlotTypesResponseTypeDef = TypedDict(
    "ListSlotTypesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "slotTypeSummaries": List[SlotTypeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSlotsRequestRequestTypeDef = TypedDict(
    "_RequiredListSlotsRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalListSlotsRequestRequestTypeDef = TypedDict(
    "_OptionalListSlotsRequestRequestTypeDef",
    {
        "sortBy": SlotSortByTypeDef,
        "filters": Sequence[SlotFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListSlotsRequestRequestTypeDef(
    _RequiredListSlotsRequestRequestTypeDef, _OptionalListSlotsRequestRequestTypeDef
):
    pass


ListTestExecutionsRequestRequestTypeDef = TypedDict(
    "ListTestExecutionsRequestRequestTypeDef",
    {
        "sortBy": TestExecutionSortByTypeDef,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTestSetsRequestRequestTypeDef = TypedDict(
    "ListTestSetsRequestRequestTypeDef",
    {
        "sortBy": TestSetSortByTypeDef,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListUtteranceAnalyticsDataRequestRequestTypeDef = TypedDict(
    "_RequiredListUtteranceAnalyticsDataRequestRequestTypeDef",
    {
        "botId": str,
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
    },
)
_OptionalListUtteranceAnalyticsDataRequestRequestTypeDef = TypedDict(
    "_OptionalListUtteranceAnalyticsDataRequestRequestTypeDef",
    {
        "sortBy": UtteranceDataSortByTypeDef,
        "filters": Sequence[AnalyticsUtteranceFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListUtteranceAnalyticsDataRequestRequestTypeDef(
    _RequiredListUtteranceAnalyticsDataRequestRequestTypeDef,
    _OptionalListUtteranceAnalyticsDataRequestRequestTypeDef,
):
    pass


OverallTestResultsTypeDef = TypedDict(
    "OverallTestResultsTypeDef",
    {
        "items": List[OverallTestResultItemTypeDef],
    },
)

UtteranceAggregationDurationOutputTypeDef = TypedDict(
    "UtteranceAggregationDurationOutputTypeDef",
    {
        "relativeAggregationDuration": RelativeAggregationDurationOutputTypeDef,
    },
)

UtteranceAggregationDurationTypeDef = TypedDict(
    "UtteranceAggregationDurationTypeDef",
    {
        "relativeAggregationDuration": RelativeAggregationDurationTypeDef,
    },
)

RuntimeHintDetailsTypeDef = TypedDict(
    "RuntimeHintDetailsTypeDef",
    {
        "runtimeHintValues": List[RuntimeHintValueTypeDef],
        "subSlotHints": Dict[str, Dict[str, Any]],
    },
    total=False,
)

SlotTypeValueOutputTypeDef = TypedDict(
    "SlotTypeValueOutputTypeDef",
    {
        "sampleValue": SampleValueOutputTypeDef,
        "synonyms": List[SampleValueOutputTypeDef],
    },
    total=False,
)

SlotTypeValueTypeDef = TypedDict(
    "SlotTypeValueTypeDef",
    {
        "sampleValue": SampleValueTypeDef,
        "synonyms": Sequence[SampleValueTypeDef],
    },
    total=False,
)

SlotDefaultValueSpecificationOutputTypeDef = TypedDict(
    "SlotDefaultValueSpecificationOutputTypeDef",
    {
        "defaultValueList": List[SlotDefaultValueOutputTypeDef],
    },
)

SlotDefaultValueSpecificationTypeDef = TypedDict(
    "SlotDefaultValueSpecificationTypeDef",
    {
        "defaultValueList": Sequence[SlotDefaultValueTypeDef],
    },
)

SlotResolutionTestResultItemTypeDef = TypedDict(
    "SlotResolutionTestResultItemTypeDef",
    {
        "slotName": str,
        "resultCounts": SlotResolutionTestResultItemCountsTypeDef,
    },
)

SlotValueOverrideOutputTypeDef = TypedDict(
    "SlotValueOverrideOutputTypeDef",
    {
        "shape": SlotShapeType,
        "value": SlotValueOutputTypeDef,
        "values": List[Dict[str, Any]],
    },
    total=False,
)

SlotValueOverrideTypeDef = TypedDict(
    "SlotValueOverrideTypeDef",
    {
        "shape": SlotShapeType,
        "value": SlotValueTypeDef,
        "values": Sequence[Dict[str, Any]],
    },
    total=False,
)

_RequiredSlotValueSelectionSettingOutputTypeDef = TypedDict(
    "_RequiredSlotValueSelectionSettingOutputTypeDef",
    {
        "resolutionStrategy": SlotValueResolutionStrategyType,
    },
)
_OptionalSlotValueSelectionSettingOutputTypeDef = TypedDict(
    "_OptionalSlotValueSelectionSettingOutputTypeDef",
    {
        "regexFilter": SlotValueRegexFilterOutputTypeDef,
        "advancedRecognitionSetting": AdvancedRecognitionSettingOutputTypeDef,
    },
    total=False,
)


class SlotValueSelectionSettingOutputTypeDef(
    _RequiredSlotValueSelectionSettingOutputTypeDef, _OptionalSlotValueSelectionSettingOutputTypeDef
):
    pass


_RequiredSlotValueSelectionSettingTypeDef = TypedDict(
    "_RequiredSlotValueSelectionSettingTypeDef",
    {
        "resolutionStrategy": SlotValueResolutionStrategyType,
    },
)
_OptionalSlotValueSelectionSettingTypeDef = TypedDict(
    "_OptionalSlotValueSelectionSettingTypeDef",
    {
        "regexFilter": SlotValueRegexFilterTypeDef,
        "advancedRecognitionSetting": AdvancedRecognitionSettingTypeDef,
    },
    total=False,
)


class SlotValueSelectionSettingTypeDef(
    _RequiredSlotValueSelectionSettingTypeDef, _OptionalSlotValueSelectionSettingTypeDef
):
    pass


TestSetDiscrepancyErrorsTypeDef = TypedDict(
    "TestSetDiscrepancyErrorsTypeDef",
    {
        "intentDiscrepancies": List[TestSetIntentDiscrepancyItemTypeDef],
        "slotDiscrepancies": List[TestSetSlotDiscrepancyItemTypeDef],
    },
)

TestSetDiscrepancyReportResourceTargetOutputTypeDef = TypedDict(
    "TestSetDiscrepancyReportResourceTargetOutputTypeDef",
    {
        "botAliasTarget": TestSetDiscrepancyReportBotAliasTargetOutputTypeDef,
    },
    total=False,
)

TestSetDiscrepancyReportResourceTargetTypeDef = TypedDict(
    "TestSetDiscrepancyReportResourceTargetTypeDef",
    {
        "botAliasTarget": TestSetDiscrepancyReportBotAliasTargetTypeDef,
    },
    total=False,
)

_RequiredTestSetImportResourceSpecificationOutputTypeDef = TypedDict(
    "_RequiredTestSetImportResourceSpecificationOutputTypeDef",
    {
        "testSetName": str,
        "roleArn": str,
        "storageLocation": TestSetStorageLocationOutputTypeDef,
        "importInputLocation": TestSetImportInputLocationOutputTypeDef,
        "modality": TestSetModalityType,
    },
)
_OptionalTestSetImportResourceSpecificationOutputTypeDef = TypedDict(
    "_OptionalTestSetImportResourceSpecificationOutputTypeDef",
    {
        "description": str,
        "testSetTags": Dict[str, str],
    },
    total=False,
)


class TestSetImportResourceSpecificationOutputTypeDef(
    _RequiredTestSetImportResourceSpecificationOutputTypeDef,
    _OptionalTestSetImportResourceSpecificationOutputTypeDef,
):
    pass


_RequiredTestSetImportResourceSpecificationTypeDef = TypedDict(
    "_RequiredTestSetImportResourceSpecificationTypeDef",
    {
        "testSetName": str,
        "roleArn": str,
        "storageLocation": TestSetStorageLocationTypeDef,
        "importInputLocation": TestSetImportInputLocationTypeDef,
        "modality": TestSetModalityType,
    },
)
_OptionalTestSetImportResourceSpecificationTypeDef = TypedDict(
    "_OptionalTestSetImportResourceSpecificationTypeDef",
    {
        "description": str,
        "testSetTags": Mapping[str, str],
    },
    total=False,
)


class TestSetImportResourceSpecificationTypeDef(
    _RequiredTestSetImportResourceSpecificationTypeDef,
    _OptionalTestSetImportResourceSpecificationTypeDef,
):
    pass


_RequiredUserTurnOutputSpecificationTypeDef = TypedDict(
    "_RequiredUserTurnOutputSpecificationTypeDef",
    {
        "intent": UserTurnIntentOutputTypeDef,
    },
)
_OptionalUserTurnOutputSpecificationTypeDef = TypedDict(
    "_OptionalUserTurnOutputSpecificationTypeDef",
    {
        "activeContexts": List[ActiveContextTypeDef],
        "transcript": str,
    },
    total=False,
)


class UserTurnOutputSpecificationTypeDef(
    _RequiredUserTurnOutputSpecificationTypeDef, _OptionalUserTurnOutputSpecificationTypeDef
):
    pass


UtteranceInputSpecificationTypeDef = TypedDict(
    "UtteranceInputSpecificationTypeDef",
    {
        "textInput": str,
        "audioInput": UtteranceAudioInputSpecificationTypeDef,
    },
    total=False,
)

ListIntentMetricsResponseTypeDef = TypedDict(
    "ListIntentMetricsResponseTypeDef",
    {
        "botId": str,
        "results": List[AnalyticsIntentResultTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIntentStageMetricsResponseTypeDef = TypedDict(
    "ListIntentStageMetricsResponseTypeDef",
    {
        "botId": str,
        "results": List[AnalyticsIntentStageResultTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSessionMetricsResponseTypeDef = TypedDict(
    "ListSessionMetricsResponseTypeDef",
    {
        "botId": str,
        "results": List[AnalyticsSessionResultTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUtteranceMetricsResponseTypeDef = TypedDict(
    "ListUtteranceMetricsResponseTypeDef",
    {
        "botId": str,
        "results": List[AnalyticsUtteranceResultTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPromptAttemptSpecificationOutputTypeDef = TypedDict(
    "_RequiredPromptAttemptSpecificationOutputTypeDef",
    {
        "allowedInputTypes": AllowedInputTypesOutputTypeDef,
    },
)
_OptionalPromptAttemptSpecificationOutputTypeDef = TypedDict(
    "_OptionalPromptAttemptSpecificationOutputTypeDef",
    {
        "allowInterrupt": bool,
        "audioAndDTMFInputSpecification": AudioAndDTMFInputSpecificationOutputTypeDef,
        "textInputSpecification": TextInputSpecificationOutputTypeDef,
    },
    total=False,
)


class PromptAttemptSpecificationOutputTypeDef(
    _RequiredPromptAttemptSpecificationOutputTypeDef,
    _OptionalPromptAttemptSpecificationOutputTypeDef,
):
    pass


_RequiredPromptAttemptSpecificationTypeDef = TypedDict(
    "_RequiredPromptAttemptSpecificationTypeDef",
    {
        "allowedInputTypes": AllowedInputTypesTypeDef,
    },
)
_OptionalPromptAttemptSpecificationTypeDef = TypedDict(
    "_OptionalPromptAttemptSpecificationTypeDef",
    {
        "allowInterrupt": bool,
        "audioAndDTMFInputSpecification": AudioAndDTMFInputSpecificationTypeDef,
        "textInputSpecification": TextInputSpecificationTypeDef,
    },
    total=False,
)


class PromptAttemptSpecificationTypeDef(
    _RequiredPromptAttemptSpecificationTypeDef, _OptionalPromptAttemptSpecificationTypeDef
):
    pass


AudioLogSettingOutputTypeDef = TypedDict(
    "AudioLogSettingOutputTypeDef",
    {
        "enabled": bool,
        "destination": AudioLogDestinationOutputTypeDef,
    },
)

AudioLogSettingTypeDef = TypedDict(
    "AudioLogSettingTypeDef",
    {
        "enabled": bool,
        "destination": AudioLogDestinationTypeDef,
    },
)

DescribeTestExecutionResponseTypeDef = TypedDict(
    "DescribeTestExecutionResponseTypeDef",
    {
        "testExecutionId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "testExecutionStatus": TestExecutionStatusType,
        "testSetId": str,
        "testSetName": str,
        "target": TestExecutionTargetOutputTypeDef,
        "apiMode": TestExecutionApiModeType,
        "testExecutionModality": TestExecutionModalityType,
        "failureReasons": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTestExecutionResponseTypeDef = TypedDict(
    "StartTestExecutionResponseTypeDef",
    {
        "testExecutionId": str,
        "creationDateTime": datetime,
        "testSetId": str,
        "target": TestExecutionTargetOutputTypeDef,
        "apiMode": TestExecutionApiModeType,
        "testExecutionModality": TestExecutionModalityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestExecutionSummaryTypeDef = TypedDict(
    "TestExecutionSummaryTypeDef",
    {
        "testExecutionId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "testExecutionStatus": TestExecutionStatusType,
        "testSetId": str,
        "testSetName": str,
        "target": TestExecutionTargetOutputTypeDef,
        "apiMode": TestExecutionApiModeType,
        "testExecutionModality": TestExecutionModalityType,
    },
    total=False,
)

_RequiredStartTestExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartTestExecutionRequestRequestTypeDef",
    {
        "testSetId": str,
        "target": TestExecutionTargetTypeDef,
        "apiMode": TestExecutionApiModeType,
    },
)
_OptionalStartTestExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartTestExecutionRequestRequestTypeDef",
    {
        "testExecutionModality": TestExecutionModalityType,
    },
    total=False,
)


class StartTestExecutionRequestRequestTypeDef(
    _RequiredStartTestExecutionRequestRequestTypeDef,
    _OptionalStartTestExecutionRequestRequestTypeDef,
):
    pass


BotRecommendationResultsTypeDef = TypedDict(
    "BotRecommendationResultsTypeDef",
    {
        "botLocaleExportUrl": str,
        "associatedTranscriptsUrl": str,
        "statistics": BotRecommendationResultStatisticsTypeDef,
    },
    total=False,
)

MessageOutputTypeDef = TypedDict(
    "MessageOutputTypeDef",
    {
        "plainTextMessage": PlainTextMessageOutputTypeDef,
        "customPayload": CustomPayloadOutputTypeDef,
        "ssmlMessage": SSMLMessageOutputTypeDef,
        "imageResponseCard": ImageResponseCardOutputTypeDef,
    },
    total=False,
)

UtteranceBotResponseTypeDef = TypedDict(
    "UtteranceBotResponseTypeDef",
    {
        "content": str,
        "contentType": UtteranceContentTypeType,
        "imageResponseCard": ImageResponseCardOutputTypeDef,
    },
    total=False,
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "plainTextMessage": PlainTextMessageTypeDef,
        "customPayload": CustomPayloadTypeDef,
        "ssmlMessage": SSMLMessageTypeDef,
        "imageResponseCard": ImageResponseCardTypeDef,
    },
    total=False,
)

TextLogSettingOutputTypeDef = TypedDict(
    "TextLogSettingOutputTypeDef",
    {
        "enabled": bool,
        "destination": TextLogDestinationOutputTypeDef,
    },
)

TextLogSettingTypeDef = TypedDict(
    "TextLogSettingTypeDef",
    {
        "enabled": bool,
        "destination": TextLogDestinationTypeDef,
    },
)

_RequiredBotAliasLocaleSettingsOutputTypeDef = TypedDict(
    "_RequiredBotAliasLocaleSettingsOutputTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalBotAliasLocaleSettingsOutputTypeDef = TypedDict(
    "_OptionalBotAliasLocaleSettingsOutputTypeDef",
    {
        "codeHookSpecification": CodeHookSpecificationOutputTypeDef,
    },
    total=False,
)


class BotAliasLocaleSettingsOutputTypeDef(
    _RequiredBotAliasLocaleSettingsOutputTypeDef, _OptionalBotAliasLocaleSettingsOutputTypeDef
):
    pass


_RequiredBotAliasLocaleSettingsTypeDef = TypedDict(
    "_RequiredBotAliasLocaleSettingsTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalBotAliasLocaleSettingsTypeDef = TypedDict(
    "_OptionalBotAliasLocaleSettingsTypeDef",
    {
        "codeHookSpecification": CodeHookSpecificationTypeDef,
    },
    total=False,
)


class BotAliasLocaleSettingsTypeDef(
    _RequiredBotAliasLocaleSettingsTypeDef, _OptionalBotAliasLocaleSettingsTypeDef
):
    pass


ConversationLevelTestResultsTypeDef = TypedDict(
    "ConversationLevelTestResultsTypeDef",
    {
        "items": List[ConversationLevelTestResultItemTypeDef],
    },
)

_RequiredListTestExecutionResultItemsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestExecutionResultItemsRequestRequestTypeDef",
    {
        "testExecutionId": str,
        "resultFilterBy": TestExecutionResultFilterByTypeDef,
    },
)
_OptionalListTestExecutionResultItemsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestExecutionResultItemsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTestExecutionResultItemsRequestRequestTypeDef(
    _RequiredListTestExecutionResultItemsRequestRequestTypeDef,
    _OptionalListTestExecutionResultItemsRequestRequestTypeDef,
):
    pass


TestSetGenerationDataSourceOutputTypeDef = TypedDict(
    "TestSetGenerationDataSourceOutputTypeDef",
    {
        "conversationLogsDataSource": ConversationLogsDataSourceOutputTypeDef,
    },
    total=False,
)

TestSetGenerationDataSourceTypeDef = TypedDict(
    "TestSetGenerationDataSourceTypeDef",
    {
        "conversationLogsDataSource": ConversationLogsDataSourceTypeDef,
    },
    total=False,
)

ListIntentsResponseTypeDef = TypedDict(
    "ListIntentsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentSummaries": List[IntentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TranscriptFilterOutputTypeDef = TypedDict(
    "TranscriptFilterOutputTypeDef",
    {
        "lexTranscriptFilter": LexTranscriptFilterOutputTypeDef,
    },
    total=False,
)

TranscriptFilterTypeDef = TypedDict(
    "TranscriptFilterTypeDef",
    {
        "lexTranscriptFilter": LexTranscriptFilterTypeDef,
    },
    total=False,
)

ListTestSetsResponseTypeDef = TypedDict(
    "ListTestSetsResponseTypeDef",
    {
        "testSets": List[TestSetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExportResponseTypeDef = TypedDict(
    "CreateExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": ExportResourceSpecificationOutputTypeDef,
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportResponseTypeDef = TypedDict(
    "DescribeExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": ExportResourceSpecificationOutputTypeDef,
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "failureReasons": List[str],
        "downloadUrl": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "exportId": str,
        "resourceSpecification": ExportResourceSpecificationOutputTypeDef,
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateExportResponseTypeDef = TypedDict(
    "UpdateExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": ExportResourceSpecificationOutputTypeDef,
        "fileFormat": ImportExportFileFormatType,
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExportRequestRequestTypeDef",
    {
        "resourceSpecification": ExportResourceSpecificationTypeDef,
        "fileFormat": ImportExportFileFormatType,
    },
)
_OptionalCreateExportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExportRequestRequestTypeDef",
    {
        "filePassword": str,
    },
    total=False,
)


class CreateExportRequestRequestTypeDef(
    _RequiredCreateExportRequestRequestTypeDef, _OptionalCreateExportRequestRequestTypeDef
):
    pass


ExternalSourceSettingOutputTypeDef = TypedDict(
    "ExternalSourceSettingOutputTypeDef",
    {
        "grammarSlotTypeSetting": GrammarSlotTypeSettingOutputTypeDef,
    },
    total=False,
)

ExternalSourceSettingTypeDef = TypedDict(
    "ExternalSourceSettingTypeDef",
    {
        "grammarSlotTypeSetting": GrammarSlotTypeSettingTypeDef,
    },
    total=False,
)

IntentClassificationTestResultsTypeDef = TypedDict(
    "IntentClassificationTestResultsTypeDef",
    {
        "items": List[IntentClassificationTestResultItemTypeDef],
    },
)

ListSessionAnalyticsDataResponseTypeDef = TypedDict(
    "ListSessionAnalyticsDataResponseTypeDef",
    {
        "botId": str,
        "nextToken": str,
        "sessions": List[SessionSpecificationTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAggregatedUtterancesResponseTypeDef = TypedDict(
    "ListAggregatedUtterancesResponseTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "botVersion": str,
        "localeId": str,
        "aggregationDuration": UtteranceAggregationDurationOutputTypeDef,
        "aggregationWindowStartTime": datetime,
        "aggregationWindowEndTime": datetime,
        "aggregationLastRefreshedDateTime": datetime,
        "aggregatedUtterancesSummaries": List[AggregatedUtterancesSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAggregatedUtterancesRequestRequestTypeDef = TypedDict(
    "_RequiredListAggregatedUtterancesRequestRequestTypeDef",
    {
        "botId": str,
        "localeId": str,
        "aggregationDuration": UtteranceAggregationDurationTypeDef,
    },
)
_OptionalListAggregatedUtterancesRequestRequestTypeDef = TypedDict(
    "_OptionalListAggregatedUtterancesRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botVersion": str,
        "sortBy": AggregatedUtterancesSortByTypeDef,
        "filters": Sequence[AggregatedUtterancesFilterTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAggregatedUtterancesRequestRequestTypeDef(
    _RequiredListAggregatedUtterancesRequestRequestTypeDef,
    _OptionalListAggregatedUtterancesRequestRequestTypeDef,
):
    pass


IntentLevelSlotResolutionTestResultItemTypeDef = TypedDict(
    "IntentLevelSlotResolutionTestResultItemTypeDef",
    {
        "intentName": str,
        "multiTurnConversation": bool,
        "slotResolutionResults": List[SlotResolutionTestResultItemTypeDef],
    },
)

CreateTestSetDiscrepancyReportResponseTypeDef = TypedDict(
    "CreateTestSetDiscrepancyReportResponseTypeDef",
    {
        "testSetDiscrepancyReportId": str,
        "creationDateTime": datetime,
        "testSetId": str,
        "target": TestSetDiscrepancyReportResourceTargetOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTestSetDiscrepancyReportResponseTypeDef = TypedDict(
    "DescribeTestSetDiscrepancyReportResponseTypeDef",
    {
        "testSetDiscrepancyReportId": str,
        "testSetId": str,
        "creationDateTime": datetime,
        "target": TestSetDiscrepancyReportResourceTargetOutputTypeDef,
        "testSetDiscrepancyReportStatus": TestSetDiscrepancyReportStatusType,
        "lastUpdatedDataTime": datetime,
        "testSetDiscrepancyTopErrors": TestSetDiscrepancyErrorsTypeDef,
        "testSetDiscrepancyRawOutputUrl": str,
        "failureReasons": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTestSetDiscrepancyReportRequestRequestTypeDef = TypedDict(
    "CreateTestSetDiscrepancyReportRequestRequestTypeDef",
    {
        "testSetId": str,
        "target": TestSetDiscrepancyReportResourceTargetTypeDef,
    },
)

ImportResourceSpecificationOutputTypeDef = TypedDict(
    "ImportResourceSpecificationOutputTypeDef",
    {
        "botImportSpecification": BotImportSpecificationOutputTypeDef,
        "botLocaleImportSpecification": BotLocaleImportSpecificationOutputTypeDef,
        "customVocabularyImportSpecification": CustomVocabularyImportSpecificationOutputTypeDef,
        "testSetImportResourceSpecification": TestSetImportResourceSpecificationOutputTypeDef,
    },
    total=False,
)

ImportResourceSpecificationTypeDef = TypedDict(
    "ImportResourceSpecificationTypeDef",
    {
        "botImportSpecification": BotImportSpecificationTypeDef,
        "botLocaleImportSpecification": BotLocaleImportSpecificationTypeDef,
        "customVocabularyImportSpecification": CustomVocabularyImportSpecificationTypeDef,
        "testSetImportResourceSpecification": TestSetImportResourceSpecificationTypeDef,
    },
    total=False,
)

_RequiredUserTurnInputSpecificationTypeDef = TypedDict(
    "_RequiredUserTurnInputSpecificationTypeDef",
    {
        "utteranceInput": UtteranceInputSpecificationTypeDef,
    },
)
_OptionalUserTurnInputSpecificationTypeDef = TypedDict(
    "_OptionalUserTurnInputSpecificationTypeDef",
    {
        "requestAttributes": Dict[str, str],
        "sessionState": InputSessionStateSpecificationTypeDef,
    },
    total=False,
)


class UserTurnInputSpecificationTypeDef(
    _RequiredUserTurnInputSpecificationTypeDef, _OptionalUserTurnInputSpecificationTypeDef
):
    pass


ListTestExecutionsResponseTypeDef = TypedDict(
    "ListTestExecutionsResponseTypeDef",
    {
        "testExecutions": List[TestExecutionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMessageGroupOutputTypeDef = TypedDict(
    "_RequiredMessageGroupOutputTypeDef",
    {
        "message": MessageOutputTypeDef,
    },
)
_OptionalMessageGroupOutputTypeDef = TypedDict(
    "_OptionalMessageGroupOutputTypeDef",
    {
        "variations": List[MessageOutputTypeDef],
    },
    total=False,
)


class MessageGroupOutputTypeDef(
    _RequiredMessageGroupOutputTypeDef, _OptionalMessageGroupOutputTypeDef
):
    pass


UtteranceSpecificationTypeDef = TypedDict(
    "UtteranceSpecificationTypeDef",
    {
        "botAliasId": str,
        "botVersion": str,
        "localeId": str,
        "sessionId": str,
        "channel": str,
        "mode": AnalyticsModalityType,
        "conversationStartTime": datetime,
        "conversationEndTime": datetime,
        "utterance": str,
        "utteranceTimestamp": datetime,
        "audioVoiceDurationMillis": int,
        "utteranceUnderstood": bool,
        "inputType": str,
        "outputType": str,
        "associatedIntentName": str,
        "associatedSlotName": str,
        "intentState": IntentStateType,
        "dialogActionType": str,
        "botResponseAudioVoiceId": str,
        "slotsFilledInSession": str,
        "utteranceRequestId": str,
        "botResponses": List[UtteranceBotResponseTypeDef],
    },
    total=False,
)

_RequiredMessageGroupTypeDef = TypedDict(
    "_RequiredMessageGroupTypeDef",
    {
        "message": MessageTypeDef,
    },
)
_OptionalMessageGroupTypeDef = TypedDict(
    "_OptionalMessageGroupTypeDef",
    {
        "variations": Sequence[MessageTypeDef],
    },
    total=False,
)


class MessageGroupTypeDef(_RequiredMessageGroupTypeDef, _OptionalMessageGroupTypeDef):
    pass


ConversationLogSettingsOutputTypeDef = TypedDict(
    "ConversationLogSettingsOutputTypeDef",
    {
        "textLogSettings": List[TextLogSettingOutputTypeDef],
        "audioLogSettings": List[AudioLogSettingOutputTypeDef],
    },
    total=False,
)

ConversationLogSettingsTypeDef = TypedDict(
    "ConversationLogSettingsTypeDef",
    {
        "textLogSettings": Sequence[TextLogSettingTypeDef],
        "audioLogSettings": Sequence[AudioLogSettingTypeDef],
    },
    total=False,
)

DescribeTestSetGenerationResponseTypeDef = TypedDict(
    "DescribeTestSetGenerationResponseTypeDef",
    {
        "testSetGenerationId": str,
        "testSetGenerationStatus": TestSetGenerationStatusType,
        "failureReasons": List[str],
        "testSetId": str,
        "testSetName": str,
        "description": str,
        "storageLocation": TestSetStorageLocationOutputTypeDef,
        "generationDataSource": TestSetGenerationDataSourceOutputTypeDef,
        "roleArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTestSetGenerationResponseTypeDef = TypedDict(
    "StartTestSetGenerationResponseTypeDef",
    {
        "testSetGenerationId": str,
        "creationDateTime": datetime,
        "testSetGenerationStatus": TestSetGenerationStatusType,
        "testSetName": str,
        "description": str,
        "storageLocation": TestSetStorageLocationOutputTypeDef,
        "generationDataSource": TestSetGenerationDataSourceOutputTypeDef,
        "roleArn": str,
        "testSetTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTestSetGenerationRequestRequestTypeDef = TypedDict(
    "_RequiredStartTestSetGenerationRequestRequestTypeDef",
    {
        "testSetName": str,
        "storageLocation": TestSetStorageLocationTypeDef,
        "generationDataSource": TestSetGenerationDataSourceTypeDef,
        "roleArn": str,
    },
)
_OptionalStartTestSetGenerationRequestRequestTypeDef = TypedDict(
    "_OptionalStartTestSetGenerationRequestRequestTypeDef",
    {
        "description": str,
        "testSetTags": Mapping[str, str],
    },
    total=False,
)


class StartTestSetGenerationRequestRequestTypeDef(
    _RequiredStartTestSetGenerationRequestRequestTypeDef,
    _OptionalStartTestSetGenerationRequestRequestTypeDef,
):
    pass


_RequiredS3BucketTranscriptSourceOutputTypeDef = TypedDict(
    "_RequiredS3BucketTranscriptSourceOutputTypeDef",
    {
        "s3BucketName": str,
        "transcriptFormat": Literal["Lex"],
    },
)
_OptionalS3BucketTranscriptSourceOutputTypeDef = TypedDict(
    "_OptionalS3BucketTranscriptSourceOutputTypeDef",
    {
        "pathFormat": PathFormatOutputTypeDef,
        "transcriptFilter": TranscriptFilterOutputTypeDef,
        "kmsKeyArn": str,
    },
    total=False,
)


class S3BucketTranscriptSourceOutputTypeDef(
    _RequiredS3BucketTranscriptSourceOutputTypeDef, _OptionalS3BucketTranscriptSourceOutputTypeDef
):
    pass


_RequiredS3BucketTranscriptSourceTypeDef = TypedDict(
    "_RequiredS3BucketTranscriptSourceTypeDef",
    {
        "s3BucketName": str,
        "transcriptFormat": Literal["Lex"],
    },
)
_OptionalS3BucketTranscriptSourceTypeDef = TypedDict(
    "_OptionalS3BucketTranscriptSourceTypeDef",
    {
        "pathFormat": PathFormatTypeDef,
        "transcriptFilter": TranscriptFilterTypeDef,
        "kmsKeyArn": str,
    },
    total=False,
)


class S3BucketTranscriptSourceTypeDef(
    _RequiredS3BucketTranscriptSourceTypeDef, _OptionalS3BucketTranscriptSourceTypeDef
):
    pass


ListExportsResponseTypeDef = TypedDict(
    "ListExportsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "exportSummaries": List[ExportSummaryTypeDef],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSlotTypeResponseTypeDef = TypedDict(
    "CreateSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List[SlotTypeValueOutputTypeDef],
        "valueSelectionSetting": SlotValueSelectionSettingOutputTypeDef,
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "externalSourceSetting": ExternalSourceSettingOutputTypeDef,
        "compositeSlotTypeSetting": CompositeSlotTypeSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotTypeResponseTypeDef = TypedDict(
    "DescribeSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List[SlotTypeValueOutputTypeDef],
        "valueSelectionSetting": SlotValueSelectionSettingOutputTypeDef,
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "externalSourceSetting": ExternalSourceSettingOutputTypeDef,
        "compositeSlotTypeSetting": CompositeSlotTypeSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSlotTypeResponseTypeDef = TypedDict(
    "UpdateSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List[SlotTypeValueOutputTypeDef],
        "valueSelectionSetting": SlotValueSelectionSettingOutputTypeDef,
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "externalSourceSetting": ExternalSourceSettingOutputTypeDef,
        "compositeSlotTypeSetting": CompositeSlotTypeSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlotTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSlotTypeRequestRequestTypeDef",
    {
        "slotTypeName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalCreateSlotTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSlotTypeRequestRequestTypeDef",
    {
        "description": str,
        "slotTypeValues": Sequence[SlotTypeValueTypeDef],
        "valueSelectionSetting": SlotValueSelectionSettingTypeDef,
        "parentSlotTypeSignature": str,
        "externalSourceSetting": ExternalSourceSettingTypeDef,
        "compositeSlotTypeSetting": CompositeSlotTypeSettingTypeDef,
    },
    total=False,
)


class CreateSlotTypeRequestRequestTypeDef(
    _RequiredCreateSlotTypeRequestRequestTypeDef, _OptionalCreateSlotTypeRequestRequestTypeDef
):
    pass


_RequiredUpdateSlotTypeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSlotTypeRequestRequestTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalUpdateSlotTypeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSlotTypeRequestRequestTypeDef",
    {
        "description": str,
        "slotTypeValues": Sequence[SlotTypeValueTypeDef],
        "valueSelectionSetting": SlotValueSelectionSettingTypeDef,
        "parentSlotTypeSignature": str,
        "externalSourceSetting": ExternalSourceSettingTypeDef,
        "compositeSlotTypeSetting": CompositeSlotTypeSettingTypeDef,
    },
    total=False,
)


class UpdateSlotTypeRequestRequestTypeDef(
    _RequiredUpdateSlotTypeRequestRequestTypeDef, _OptionalUpdateSlotTypeRequestRequestTypeDef
):
    pass


IntentLevelSlotResolutionTestResultsTypeDef = TypedDict(
    "IntentLevelSlotResolutionTestResultsTypeDef",
    {
        "items": List[IntentLevelSlotResolutionTestResultItemTypeDef],
    },
)

DescribeImportResponseTypeDef = TypedDict(
    "DescribeImportResponseTypeDef",
    {
        "importId": str,
        "resourceSpecification": ImportResourceSpecificationOutputTypeDef,
        "importedResourceId": str,
        "importedResourceName": str,
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "importId": str,
        "resourceSpecification": ImportResourceSpecificationOutputTypeDef,
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportRequestRequestTypeDef",
    {
        "importId": str,
        "resourceSpecification": ImportResourceSpecificationTypeDef,
        "mergeStrategy": MergeStrategyType,
    },
)
_OptionalStartImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportRequestRequestTypeDef",
    {
        "filePassword": str,
    },
    total=False,
)


class StartImportRequestRequestTypeDef(
    _RequiredStartImportRequestRequestTypeDef, _OptionalStartImportRequestRequestTypeDef
):
    pass


_RequiredUserTurnResultTypeDef = TypedDict(
    "_RequiredUserTurnResultTypeDef",
    {
        "input": UserTurnInputSpecificationTypeDef,
        "expectedOutput": UserTurnOutputSpecificationTypeDef,
    },
)
_OptionalUserTurnResultTypeDef = TypedDict(
    "_OptionalUserTurnResultTypeDef",
    {
        "actualOutput": UserTurnOutputSpecificationTypeDef,
        "errorDetails": ExecutionErrorDetailsTypeDef,
        "endToEndResult": TestResultMatchStatusType,
        "intentMatchResult": TestResultMatchStatusType,
        "slotMatchResult": TestResultMatchStatusType,
        "speechTranscriptionResult": TestResultMatchStatusType,
        "conversationLevelResult": ConversationLevelResultDetailTypeDef,
    },
    total=False,
)


class UserTurnResultTypeDef(_RequiredUserTurnResultTypeDef, _OptionalUserTurnResultTypeDef):
    pass


UserTurnSpecificationTypeDef = TypedDict(
    "UserTurnSpecificationTypeDef",
    {
        "input": UserTurnInputSpecificationTypeDef,
        "expected": UserTurnOutputSpecificationTypeDef,
    },
)

_RequiredFulfillmentStartResponseSpecificationOutputTypeDef = TypedDict(
    "_RequiredFulfillmentStartResponseSpecificationOutputTypeDef",
    {
        "delayInSeconds": int,
        "messageGroups": List[MessageGroupOutputTypeDef],
    },
)
_OptionalFulfillmentStartResponseSpecificationOutputTypeDef = TypedDict(
    "_OptionalFulfillmentStartResponseSpecificationOutputTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class FulfillmentStartResponseSpecificationOutputTypeDef(
    _RequiredFulfillmentStartResponseSpecificationOutputTypeDef,
    _OptionalFulfillmentStartResponseSpecificationOutputTypeDef,
):
    pass


_RequiredFulfillmentUpdateResponseSpecificationOutputTypeDef = TypedDict(
    "_RequiredFulfillmentUpdateResponseSpecificationOutputTypeDef",
    {
        "frequencyInSeconds": int,
        "messageGroups": List[MessageGroupOutputTypeDef],
    },
)
_OptionalFulfillmentUpdateResponseSpecificationOutputTypeDef = TypedDict(
    "_OptionalFulfillmentUpdateResponseSpecificationOutputTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class FulfillmentUpdateResponseSpecificationOutputTypeDef(
    _RequiredFulfillmentUpdateResponseSpecificationOutputTypeDef,
    _OptionalFulfillmentUpdateResponseSpecificationOutputTypeDef,
):
    pass


_RequiredPromptSpecificationOutputTypeDef = TypedDict(
    "_RequiredPromptSpecificationOutputTypeDef",
    {
        "messageGroups": List[MessageGroupOutputTypeDef],
        "maxRetries": int,
    },
)
_OptionalPromptSpecificationOutputTypeDef = TypedDict(
    "_OptionalPromptSpecificationOutputTypeDef",
    {
        "allowInterrupt": bool,
        "messageSelectionStrategy": MessageSelectionStrategyType,
        "promptAttemptsSpecification": Dict[
            PromptAttemptType, PromptAttemptSpecificationOutputTypeDef
        ],
    },
    total=False,
)


class PromptSpecificationOutputTypeDef(
    _RequiredPromptSpecificationOutputTypeDef, _OptionalPromptSpecificationOutputTypeDef
):
    pass


_RequiredResponseSpecificationOutputTypeDef = TypedDict(
    "_RequiredResponseSpecificationOutputTypeDef",
    {
        "messageGroups": List[MessageGroupOutputTypeDef],
    },
)
_OptionalResponseSpecificationOutputTypeDef = TypedDict(
    "_OptionalResponseSpecificationOutputTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class ResponseSpecificationOutputTypeDef(
    _RequiredResponseSpecificationOutputTypeDef, _OptionalResponseSpecificationOutputTypeDef
):
    pass


_RequiredStillWaitingResponseSpecificationOutputTypeDef = TypedDict(
    "_RequiredStillWaitingResponseSpecificationOutputTypeDef",
    {
        "messageGroups": List[MessageGroupOutputTypeDef],
        "frequencyInSeconds": int,
        "timeoutInSeconds": int,
    },
)
_OptionalStillWaitingResponseSpecificationOutputTypeDef = TypedDict(
    "_OptionalStillWaitingResponseSpecificationOutputTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class StillWaitingResponseSpecificationOutputTypeDef(
    _RequiredStillWaitingResponseSpecificationOutputTypeDef,
    _OptionalStillWaitingResponseSpecificationOutputTypeDef,
):
    pass


ListUtteranceAnalyticsDataResponseTypeDef = TypedDict(
    "ListUtteranceAnalyticsDataResponseTypeDef",
    {
        "botId": str,
        "nextToken": str,
        "utterances": List[UtteranceSpecificationTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFulfillmentStartResponseSpecificationTypeDef = TypedDict(
    "_RequiredFulfillmentStartResponseSpecificationTypeDef",
    {
        "delayInSeconds": int,
        "messageGroups": Sequence[MessageGroupTypeDef],
    },
)
_OptionalFulfillmentStartResponseSpecificationTypeDef = TypedDict(
    "_OptionalFulfillmentStartResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class FulfillmentStartResponseSpecificationTypeDef(
    _RequiredFulfillmentStartResponseSpecificationTypeDef,
    _OptionalFulfillmentStartResponseSpecificationTypeDef,
):
    pass


_RequiredFulfillmentUpdateResponseSpecificationTypeDef = TypedDict(
    "_RequiredFulfillmentUpdateResponseSpecificationTypeDef",
    {
        "frequencyInSeconds": int,
        "messageGroups": Sequence[MessageGroupTypeDef],
    },
)
_OptionalFulfillmentUpdateResponseSpecificationTypeDef = TypedDict(
    "_OptionalFulfillmentUpdateResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class FulfillmentUpdateResponseSpecificationTypeDef(
    _RequiredFulfillmentUpdateResponseSpecificationTypeDef,
    _OptionalFulfillmentUpdateResponseSpecificationTypeDef,
):
    pass


_RequiredPromptSpecificationTypeDef = TypedDict(
    "_RequiredPromptSpecificationTypeDef",
    {
        "messageGroups": Sequence[MessageGroupTypeDef],
        "maxRetries": int,
    },
)
_OptionalPromptSpecificationTypeDef = TypedDict(
    "_OptionalPromptSpecificationTypeDef",
    {
        "allowInterrupt": bool,
        "messageSelectionStrategy": MessageSelectionStrategyType,
        "promptAttemptsSpecification": Mapping[
            PromptAttemptType, PromptAttemptSpecificationTypeDef
        ],
    },
    total=False,
)


class PromptSpecificationTypeDef(
    _RequiredPromptSpecificationTypeDef, _OptionalPromptSpecificationTypeDef
):
    pass


_RequiredResponseSpecificationTypeDef = TypedDict(
    "_RequiredResponseSpecificationTypeDef",
    {
        "messageGroups": Sequence[MessageGroupTypeDef],
    },
)
_OptionalResponseSpecificationTypeDef = TypedDict(
    "_OptionalResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class ResponseSpecificationTypeDef(
    _RequiredResponseSpecificationTypeDef, _OptionalResponseSpecificationTypeDef
):
    pass


_RequiredStillWaitingResponseSpecificationTypeDef = TypedDict(
    "_RequiredStillWaitingResponseSpecificationTypeDef",
    {
        "messageGroups": Sequence[MessageGroupTypeDef],
        "frequencyInSeconds": int,
        "timeoutInSeconds": int,
    },
)
_OptionalStillWaitingResponseSpecificationTypeDef = TypedDict(
    "_OptionalStillWaitingResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class StillWaitingResponseSpecificationTypeDef(
    _RequiredStillWaitingResponseSpecificationTypeDef,
    _OptionalStillWaitingResponseSpecificationTypeDef,
):
    pass


CreateBotAliasResponseTypeDef = TypedDict(
    "CreateBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, BotAliasLocaleSettingsOutputTypeDef],
        "conversationLogSettings": ConversationLogSettingsOutputTypeDef,
        "sentimentAnalysisSettings": SentimentAnalysisSettingsOutputTypeDef,
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotAliasResponseTypeDef = TypedDict(
    "DescribeBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, BotAliasLocaleSettingsOutputTypeDef],
        "conversationLogSettings": ConversationLogSettingsOutputTypeDef,
        "sentimentAnalysisSettings": SentimentAnalysisSettingsOutputTypeDef,
        "botAliasHistoryEvents": List[BotAliasHistoryEventTypeDef],
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "parentBotNetworks": List[ParentBotNetworkTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotAliasResponseTypeDef = TypedDict(
    "UpdateBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, BotAliasLocaleSettingsOutputTypeDef],
        "conversationLogSettings": ConversationLogSettingsOutputTypeDef,
        "sentimentAnalysisSettings": SentimentAnalysisSettingsOutputTypeDef,
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotAliasRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBotAliasRequestRequestTypeDef",
    {
        "botAliasName": str,
        "botId": str,
    },
)
_OptionalCreateBotAliasRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBotAliasRequestRequestTypeDef",
    {
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Mapping[str, BotAliasLocaleSettingsTypeDef],
        "conversationLogSettings": ConversationLogSettingsTypeDef,
        "sentimentAnalysisSettings": SentimentAnalysisSettingsTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateBotAliasRequestRequestTypeDef(
    _RequiredCreateBotAliasRequestRequestTypeDef, _OptionalCreateBotAliasRequestRequestTypeDef
):
    pass


_RequiredUpdateBotAliasRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBotAliasRequestRequestTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "botId": str,
    },
)
_OptionalUpdateBotAliasRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBotAliasRequestRequestTypeDef",
    {
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Mapping[str, BotAliasLocaleSettingsTypeDef],
        "conversationLogSettings": ConversationLogSettingsTypeDef,
        "sentimentAnalysisSettings": SentimentAnalysisSettingsTypeDef,
    },
    total=False,
)


class UpdateBotAliasRequestRequestTypeDef(
    _RequiredUpdateBotAliasRequestRequestTypeDef, _OptionalUpdateBotAliasRequestRequestTypeDef
):
    pass


TranscriptSourceSettingOutputTypeDef = TypedDict(
    "TranscriptSourceSettingOutputTypeDef",
    {
        "s3BucketTranscriptSource": S3BucketTranscriptSourceOutputTypeDef,
    },
    total=False,
)

TranscriptSourceSettingTypeDef = TypedDict(
    "TranscriptSourceSettingTypeDef",
    {
        "s3BucketTranscriptSource": S3BucketTranscriptSourceTypeDef,
    },
    total=False,
)

TestSetTurnResultTypeDef = TypedDict(
    "TestSetTurnResultTypeDef",
    {
        "agent": AgentTurnResultTypeDef,
        "user": UserTurnResultTypeDef,
    },
    total=False,
)

TurnSpecificationTypeDef = TypedDict(
    "TurnSpecificationTypeDef",
    {
        "agentTurn": AgentTurnSpecificationTypeDef,
        "userTurn": UserTurnSpecificationTypeDef,
    },
    total=False,
)

_RequiredFulfillmentUpdatesSpecificationOutputTypeDef = TypedDict(
    "_RequiredFulfillmentUpdatesSpecificationOutputTypeDef",
    {
        "active": bool,
    },
)
_OptionalFulfillmentUpdatesSpecificationOutputTypeDef = TypedDict(
    "_OptionalFulfillmentUpdatesSpecificationOutputTypeDef",
    {
        "startResponse": FulfillmentStartResponseSpecificationOutputTypeDef,
        "updateResponse": FulfillmentUpdateResponseSpecificationOutputTypeDef,
        "timeoutInSeconds": int,
    },
    total=False,
)


class FulfillmentUpdatesSpecificationOutputTypeDef(
    _RequiredFulfillmentUpdatesSpecificationOutputTypeDef,
    _OptionalFulfillmentUpdatesSpecificationOutputTypeDef,
):
    pass


SlotSummaryTypeDef = TypedDict(
    "SlotSummaryTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotConstraint": SlotConstraintType,
        "slotTypeId": str,
        "valueElicitationPromptSpecification": PromptSpecificationOutputTypeDef,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

_RequiredConditionalBranchOutputTypeDef = TypedDict(
    "_RequiredConditionalBranchOutputTypeDef",
    {
        "name": str,
        "condition": ConditionOutputTypeDef,
        "nextStep": DialogStateOutputTypeDef,
    },
)
_OptionalConditionalBranchOutputTypeDef = TypedDict(
    "_OptionalConditionalBranchOutputTypeDef",
    {
        "response": ResponseSpecificationOutputTypeDef,
    },
    total=False,
)


class ConditionalBranchOutputTypeDef(
    _RequiredConditionalBranchOutputTypeDef, _OptionalConditionalBranchOutputTypeDef
):
    pass


DefaultConditionalBranchOutputTypeDef = TypedDict(
    "DefaultConditionalBranchOutputTypeDef",
    {
        "nextStep": DialogStateOutputTypeDef,
        "response": ResponseSpecificationOutputTypeDef,
    },
    total=False,
)

_RequiredWaitAndContinueSpecificationOutputTypeDef = TypedDict(
    "_RequiredWaitAndContinueSpecificationOutputTypeDef",
    {
        "waitingResponse": ResponseSpecificationOutputTypeDef,
        "continueResponse": ResponseSpecificationOutputTypeDef,
    },
)
_OptionalWaitAndContinueSpecificationOutputTypeDef = TypedDict(
    "_OptionalWaitAndContinueSpecificationOutputTypeDef",
    {
        "stillWaitingResponse": StillWaitingResponseSpecificationOutputTypeDef,
        "active": bool,
    },
    total=False,
)


class WaitAndContinueSpecificationOutputTypeDef(
    _RequiredWaitAndContinueSpecificationOutputTypeDef,
    _OptionalWaitAndContinueSpecificationOutputTypeDef,
):
    pass


_RequiredFulfillmentUpdatesSpecificationTypeDef = TypedDict(
    "_RequiredFulfillmentUpdatesSpecificationTypeDef",
    {
        "active": bool,
    },
)
_OptionalFulfillmentUpdatesSpecificationTypeDef = TypedDict(
    "_OptionalFulfillmentUpdatesSpecificationTypeDef",
    {
        "startResponse": FulfillmentStartResponseSpecificationTypeDef,
        "updateResponse": FulfillmentUpdateResponseSpecificationTypeDef,
        "timeoutInSeconds": int,
    },
    total=False,
)


class FulfillmentUpdatesSpecificationTypeDef(
    _RequiredFulfillmentUpdatesSpecificationTypeDef, _OptionalFulfillmentUpdatesSpecificationTypeDef
):
    pass


_RequiredConditionalBranchTypeDef = TypedDict(
    "_RequiredConditionalBranchTypeDef",
    {
        "name": str,
        "condition": ConditionTypeDef,
        "nextStep": DialogStateTypeDef,
    },
)
_OptionalConditionalBranchTypeDef = TypedDict(
    "_OptionalConditionalBranchTypeDef",
    {
        "response": ResponseSpecificationTypeDef,
    },
    total=False,
)


class ConditionalBranchTypeDef(
    _RequiredConditionalBranchTypeDef, _OptionalConditionalBranchTypeDef
):
    pass


DefaultConditionalBranchTypeDef = TypedDict(
    "DefaultConditionalBranchTypeDef",
    {
        "nextStep": DialogStateTypeDef,
        "response": ResponseSpecificationTypeDef,
    },
    total=False,
)

_RequiredWaitAndContinueSpecificationTypeDef = TypedDict(
    "_RequiredWaitAndContinueSpecificationTypeDef",
    {
        "waitingResponse": ResponseSpecificationTypeDef,
        "continueResponse": ResponseSpecificationTypeDef,
    },
)
_OptionalWaitAndContinueSpecificationTypeDef = TypedDict(
    "_OptionalWaitAndContinueSpecificationTypeDef",
    {
        "stillWaitingResponse": StillWaitingResponseSpecificationTypeDef,
        "active": bool,
    },
    total=False,
)


class WaitAndContinueSpecificationTypeDef(
    _RequiredWaitAndContinueSpecificationTypeDef, _OptionalWaitAndContinueSpecificationTypeDef
):
    pass


DescribeBotRecommendationResponseTypeDef = TypedDict(
    "DescribeBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "transcriptSourceSetting": TranscriptSourceSettingOutputTypeDef,
        "encryptionSetting": EncryptionSettingOutputTypeDef,
        "botRecommendationResults": BotRecommendationResultsTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartBotRecommendationResponseTypeDef = TypedDict(
    "StartBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "creationDateTime": datetime,
        "transcriptSourceSetting": TranscriptSourceSettingOutputTypeDef,
        "encryptionSetting": EncryptionSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotRecommendationResponseTypeDef = TypedDict(
    "UpdateBotRecommendationResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botRecommendationStatus": BotRecommendationStatusType,
        "botRecommendationId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "transcriptSourceSetting": TranscriptSourceSettingOutputTypeDef,
        "encryptionSetting": EncryptionSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartBotRecommendationRequestRequestTypeDef = TypedDict(
    "_RequiredStartBotRecommendationRequestRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "transcriptSourceSetting": TranscriptSourceSettingTypeDef,
    },
)
_OptionalStartBotRecommendationRequestRequestTypeDef = TypedDict(
    "_OptionalStartBotRecommendationRequestRequestTypeDef",
    {
        "encryptionSetting": EncryptionSettingTypeDef,
    },
    total=False,
)


class StartBotRecommendationRequestRequestTypeDef(
    _RequiredStartBotRecommendationRequestRequestTypeDef,
    _OptionalStartBotRecommendationRequestRequestTypeDef,
):
    pass


_RequiredUtteranceLevelTestResultItemTypeDef = TypedDict(
    "_RequiredUtteranceLevelTestResultItemTypeDef",
    {
        "recordNumber": int,
        "turnResult": TestSetTurnResultTypeDef,
    },
)
_OptionalUtteranceLevelTestResultItemTypeDef = TypedDict(
    "_OptionalUtteranceLevelTestResultItemTypeDef",
    {
        "conversationId": str,
    },
    total=False,
)


class UtteranceLevelTestResultItemTypeDef(
    _RequiredUtteranceLevelTestResultItemTypeDef, _OptionalUtteranceLevelTestResultItemTypeDef
):
    pass


_RequiredTestSetTurnRecordTypeDef = TypedDict(
    "_RequiredTestSetTurnRecordTypeDef",
    {
        "recordNumber": int,
        "turnSpecification": TurnSpecificationTypeDef,
    },
)
_OptionalTestSetTurnRecordTypeDef = TypedDict(
    "_OptionalTestSetTurnRecordTypeDef",
    {
        "conversationId": str,
        "turnNumber": int,
    },
    total=False,
)


class TestSetTurnRecordTypeDef(
    _RequiredTestSetTurnRecordTypeDef, _OptionalTestSetTurnRecordTypeDef
):
    pass


ListSlotsResponseTypeDef = TypedDict(
    "ListSlotsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "slotSummaries": List[SlotSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConditionalSpecificationOutputTypeDef = TypedDict(
    "ConditionalSpecificationOutputTypeDef",
    {
        "active": bool,
        "conditionalBranches": List[ConditionalBranchOutputTypeDef],
        "defaultBranch": DefaultConditionalBranchOutputTypeDef,
    },
)

_RequiredSubSlotValueElicitationSettingOutputTypeDef = TypedDict(
    "_RequiredSubSlotValueElicitationSettingOutputTypeDef",
    {
        "promptSpecification": PromptSpecificationOutputTypeDef,
    },
)
_OptionalSubSlotValueElicitationSettingOutputTypeDef = TypedDict(
    "_OptionalSubSlotValueElicitationSettingOutputTypeDef",
    {
        "defaultValueSpecification": SlotDefaultValueSpecificationOutputTypeDef,
        "sampleUtterances": List[SampleUtteranceOutputTypeDef],
        "waitAndContinueSpecification": WaitAndContinueSpecificationOutputTypeDef,
    },
    total=False,
)


class SubSlotValueElicitationSettingOutputTypeDef(
    _RequiredSubSlotValueElicitationSettingOutputTypeDef,
    _OptionalSubSlotValueElicitationSettingOutputTypeDef,
):
    pass


ConditionalSpecificationTypeDef = TypedDict(
    "ConditionalSpecificationTypeDef",
    {
        "active": bool,
        "conditionalBranches": Sequence[ConditionalBranchTypeDef],
        "defaultBranch": DefaultConditionalBranchTypeDef,
    },
)

_RequiredSubSlotValueElicitationSettingTypeDef = TypedDict(
    "_RequiredSubSlotValueElicitationSettingTypeDef",
    {
        "promptSpecification": PromptSpecificationTypeDef,
    },
)
_OptionalSubSlotValueElicitationSettingTypeDef = TypedDict(
    "_OptionalSubSlotValueElicitationSettingTypeDef",
    {
        "defaultValueSpecification": SlotDefaultValueSpecificationTypeDef,
        "sampleUtterances": Sequence[SampleUtteranceTypeDef],
        "waitAndContinueSpecification": WaitAndContinueSpecificationTypeDef,
    },
    total=False,
)


class SubSlotValueElicitationSettingTypeDef(
    _RequiredSubSlotValueElicitationSettingTypeDef, _OptionalSubSlotValueElicitationSettingTypeDef
):
    pass


UtteranceLevelTestResultsTypeDef = TypedDict(
    "UtteranceLevelTestResultsTypeDef",
    {
        "items": List[UtteranceLevelTestResultItemTypeDef],
    },
)

ListTestSetRecordsResponseTypeDef = TypedDict(
    "ListTestSetRecordsResponseTypeDef",
    {
        "testSetRecords": List[TestSetTurnRecordTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntentClosingSettingOutputTypeDef = TypedDict(
    "IntentClosingSettingOutputTypeDef",
    {
        "closingResponse": ResponseSpecificationOutputTypeDef,
        "active": bool,
        "nextStep": DialogStateOutputTypeDef,
        "conditional": ConditionalSpecificationOutputTypeDef,
    },
    total=False,
)

PostDialogCodeHookInvocationSpecificationOutputTypeDef = TypedDict(
    "PostDialogCodeHookInvocationSpecificationOutputTypeDef",
    {
        "successResponse": ResponseSpecificationOutputTypeDef,
        "successNextStep": DialogStateOutputTypeDef,
        "successConditional": ConditionalSpecificationOutputTypeDef,
        "failureResponse": ResponseSpecificationOutputTypeDef,
        "failureNextStep": DialogStateOutputTypeDef,
        "failureConditional": ConditionalSpecificationOutputTypeDef,
        "timeoutResponse": ResponseSpecificationOutputTypeDef,
        "timeoutNextStep": DialogStateOutputTypeDef,
        "timeoutConditional": ConditionalSpecificationOutputTypeDef,
    },
    total=False,
)

PostFulfillmentStatusSpecificationOutputTypeDef = TypedDict(
    "PostFulfillmentStatusSpecificationOutputTypeDef",
    {
        "successResponse": ResponseSpecificationOutputTypeDef,
        "failureResponse": ResponseSpecificationOutputTypeDef,
        "timeoutResponse": ResponseSpecificationOutputTypeDef,
        "successNextStep": DialogStateOutputTypeDef,
        "successConditional": ConditionalSpecificationOutputTypeDef,
        "failureNextStep": DialogStateOutputTypeDef,
        "failureConditional": ConditionalSpecificationOutputTypeDef,
        "timeoutNextStep": DialogStateOutputTypeDef,
        "timeoutConditional": ConditionalSpecificationOutputTypeDef,
    },
    total=False,
)

SpecificationsOutputTypeDef = TypedDict(
    "SpecificationsOutputTypeDef",
    {
        "slotTypeId": str,
        "valueElicitationSetting": SubSlotValueElicitationSettingOutputTypeDef,
    },
)

IntentClosingSettingTypeDef = TypedDict(
    "IntentClosingSettingTypeDef",
    {
        "closingResponse": ResponseSpecificationTypeDef,
        "active": bool,
        "nextStep": DialogStateTypeDef,
        "conditional": ConditionalSpecificationTypeDef,
    },
    total=False,
)

PostDialogCodeHookInvocationSpecificationTypeDef = TypedDict(
    "PostDialogCodeHookInvocationSpecificationTypeDef",
    {
        "successResponse": ResponseSpecificationTypeDef,
        "successNextStep": DialogStateTypeDef,
        "successConditional": ConditionalSpecificationTypeDef,
        "failureResponse": ResponseSpecificationTypeDef,
        "failureNextStep": DialogStateTypeDef,
        "failureConditional": ConditionalSpecificationTypeDef,
        "timeoutResponse": ResponseSpecificationTypeDef,
        "timeoutNextStep": DialogStateTypeDef,
        "timeoutConditional": ConditionalSpecificationTypeDef,
    },
    total=False,
)

PostFulfillmentStatusSpecificationTypeDef = TypedDict(
    "PostFulfillmentStatusSpecificationTypeDef",
    {
        "successResponse": ResponseSpecificationTypeDef,
        "failureResponse": ResponseSpecificationTypeDef,
        "timeoutResponse": ResponseSpecificationTypeDef,
        "successNextStep": DialogStateTypeDef,
        "successConditional": ConditionalSpecificationTypeDef,
        "failureNextStep": DialogStateTypeDef,
        "failureConditional": ConditionalSpecificationTypeDef,
        "timeoutNextStep": DialogStateTypeDef,
        "timeoutConditional": ConditionalSpecificationTypeDef,
    },
    total=False,
)

SpecificationsTypeDef = TypedDict(
    "SpecificationsTypeDef",
    {
        "slotTypeId": str,
        "valueElicitationSetting": SubSlotValueElicitationSettingTypeDef,
    },
)

TestExecutionResultItemsTypeDef = TypedDict(
    "TestExecutionResultItemsTypeDef",
    {
        "overallTestResults": OverallTestResultsTypeDef,
        "conversationLevelTestResults": ConversationLevelTestResultsTypeDef,
        "intentClassificationTestResults": IntentClassificationTestResultsTypeDef,
        "intentLevelSlotResolutionTestResults": IntentLevelSlotResolutionTestResultsTypeDef,
        "utteranceLevelTestResults": UtteranceLevelTestResultsTypeDef,
    },
    total=False,
)

_RequiredDialogCodeHookInvocationSettingOutputTypeDef = TypedDict(
    "_RequiredDialogCodeHookInvocationSettingOutputTypeDef",
    {
        "enableCodeHookInvocation": bool,
        "active": bool,
        "postCodeHookSpecification": PostDialogCodeHookInvocationSpecificationOutputTypeDef,
    },
)
_OptionalDialogCodeHookInvocationSettingOutputTypeDef = TypedDict(
    "_OptionalDialogCodeHookInvocationSettingOutputTypeDef",
    {
        "invocationLabel": str,
    },
    total=False,
)


class DialogCodeHookInvocationSettingOutputTypeDef(
    _RequiredDialogCodeHookInvocationSettingOutputTypeDef,
    _OptionalDialogCodeHookInvocationSettingOutputTypeDef,
):
    pass


_RequiredFulfillmentCodeHookSettingsOutputTypeDef = TypedDict(
    "_RequiredFulfillmentCodeHookSettingsOutputTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalFulfillmentCodeHookSettingsOutputTypeDef = TypedDict(
    "_OptionalFulfillmentCodeHookSettingsOutputTypeDef",
    {
        "postFulfillmentStatusSpecification": PostFulfillmentStatusSpecificationOutputTypeDef,
        "fulfillmentUpdatesSpecification": FulfillmentUpdatesSpecificationOutputTypeDef,
        "active": bool,
    },
    total=False,
)


class FulfillmentCodeHookSettingsOutputTypeDef(
    _RequiredFulfillmentCodeHookSettingsOutputTypeDef,
    _OptionalFulfillmentCodeHookSettingsOutputTypeDef,
):
    pass


SubSlotSettingOutputTypeDef = TypedDict(
    "SubSlotSettingOutputTypeDef",
    {
        "expression": str,
        "slotSpecifications": Dict[str, SpecificationsOutputTypeDef],
    },
    total=False,
)

_RequiredDialogCodeHookInvocationSettingTypeDef = TypedDict(
    "_RequiredDialogCodeHookInvocationSettingTypeDef",
    {
        "enableCodeHookInvocation": bool,
        "active": bool,
        "postCodeHookSpecification": PostDialogCodeHookInvocationSpecificationTypeDef,
    },
)
_OptionalDialogCodeHookInvocationSettingTypeDef = TypedDict(
    "_OptionalDialogCodeHookInvocationSettingTypeDef",
    {
        "invocationLabel": str,
    },
    total=False,
)


class DialogCodeHookInvocationSettingTypeDef(
    _RequiredDialogCodeHookInvocationSettingTypeDef, _OptionalDialogCodeHookInvocationSettingTypeDef
):
    pass


_RequiredFulfillmentCodeHookSettingsTypeDef = TypedDict(
    "_RequiredFulfillmentCodeHookSettingsTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalFulfillmentCodeHookSettingsTypeDef = TypedDict(
    "_OptionalFulfillmentCodeHookSettingsTypeDef",
    {
        "postFulfillmentStatusSpecification": PostFulfillmentStatusSpecificationTypeDef,
        "fulfillmentUpdatesSpecification": FulfillmentUpdatesSpecificationTypeDef,
        "active": bool,
    },
    total=False,
)


class FulfillmentCodeHookSettingsTypeDef(
    _RequiredFulfillmentCodeHookSettingsTypeDef, _OptionalFulfillmentCodeHookSettingsTypeDef
):
    pass


SubSlotSettingTypeDef = TypedDict(
    "SubSlotSettingTypeDef",
    {
        "expression": str,
        "slotSpecifications": Mapping[str, SpecificationsTypeDef],
    },
    total=False,
)

ListTestExecutionResultItemsResponseTypeDef = TypedDict(
    "ListTestExecutionResultItemsResponseTypeDef",
    {
        "testExecutionResults": TestExecutionResultItemsTypeDef,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitialResponseSettingOutputTypeDef = TypedDict(
    "InitialResponseSettingOutputTypeDef",
    {
        "initialResponse": ResponseSpecificationOutputTypeDef,
        "nextStep": DialogStateOutputTypeDef,
        "conditional": ConditionalSpecificationOutputTypeDef,
        "codeHook": DialogCodeHookInvocationSettingOutputTypeDef,
    },
    total=False,
)

_RequiredIntentConfirmationSettingOutputTypeDef = TypedDict(
    "_RequiredIntentConfirmationSettingOutputTypeDef",
    {
        "promptSpecification": PromptSpecificationOutputTypeDef,
    },
)
_OptionalIntentConfirmationSettingOutputTypeDef = TypedDict(
    "_OptionalIntentConfirmationSettingOutputTypeDef",
    {
        "declinationResponse": ResponseSpecificationOutputTypeDef,
        "active": bool,
        "confirmationResponse": ResponseSpecificationOutputTypeDef,
        "confirmationNextStep": DialogStateOutputTypeDef,
        "confirmationConditional": ConditionalSpecificationOutputTypeDef,
        "declinationNextStep": DialogStateOutputTypeDef,
        "declinationConditional": ConditionalSpecificationOutputTypeDef,
        "failureResponse": ResponseSpecificationOutputTypeDef,
        "failureNextStep": DialogStateOutputTypeDef,
        "failureConditional": ConditionalSpecificationOutputTypeDef,
        "codeHook": DialogCodeHookInvocationSettingOutputTypeDef,
        "elicitationCodeHook": ElicitationCodeHookInvocationSettingOutputTypeDef,
    },
    total=False,
)


class IntentConfirmationSettingOutputTypeDef(
    _RequiredIntentConfirmationSettingOutputTypeDef, _OptionalIntentConfirmationSettingOutputTypeDef
):
    pass


SlotCaptureSettingOutputTypeDef = TypedDict(
    "SlotCaptureSettingOutputTypeDef",
    {
        "captureResponse": ResponseSpecificationOutputTypeDef,
        "captureNextStep": DialogStateOutputTypeDef,
        "captureConditional": ConditionalSpecificationOutputTypeDef,
        "failureResponse": ResponseSpecificationOutputTypeDef,
        "failureNextStep": DialogStateOutputTypeDef,
        "failureConditional": ConditionalSpecificationOutputTypeDef,
        "codeHook": DialogCodeHookInvocationSettingOutputTypeDef,
        "elicitationCodeHook": ElicitationCodeHookInvocationSettingOutputTypeDef,
    },
    total=False,
)

InitialResponseSettingTypeDef = TypedDict(
    "InitialResponseSettingTypeDef",
    {
        "initialResponse": ResponseSpecificationTypeDef,
        "nextStep": DialogStateTypeDef,
        "conditional": ConditionalSpecificationTypeDef,
        "codeHook": DialogCodeHookInvocationSettingTypeDef,
    },
    total=False,
)

_RequiredIntentConfirmationSettingTypeDef = TypedDict(
    "_RequiredIntentConfirmationSettingTypeDef",
    {
        "promptSpecification": PromptSpecificationTypeDef,
    },
)
_OptionalIntentConfirmationSettingTypeDef = TypedDict(
    "_OptionalIntentConfirmationSettingTypeDef",
    {
        "declinationResponse": ResponseSpecificationTypeDef,
        "active": bool,
        "confirmationResponse": ResponseSpecificationTypeDef,
        "confirmationNextStep": DialogStateTypeDef,
        "confirmationConditional": ConditionalSpecificationTypeDef,
        "declinationNextStep": DialogStateTypeDef,
        "declinationConditional": ConditionalSpecificationTypeDef,
        "failureResponse": ResponseSpecificationTypeDef,
        "failureNextStep": DialogStateTypeDef,
        "failureConditional": ConditionalSpecificationTypeDef,
        "codeHook": DialogCodeHookInvocationSettingTypeDef,
        "elicitationCodeHook": ElicitationCodeHookInvocationSettingTypeDef,
    },
    total=False,
)


class IntentConfirmationSettingTypeDef(
    _RequiredIntentConfirmationSettingTypeDef, _OptionalIntentConfirmationSettingTypeDef
):
    pass


SlotCaptureSettingTypeDef = TypedDict(
    "SlotCaptureSettingTypeDef",
    {
        "captureResponse": ResponseSpecificationTypeDef,
        "captureNextStep": DialogStateTypeDef,
        "captureConditional": ConditionalSpecificationTypeDef,
        "failureResponse": ResponseSpecificationTypeDef,
        "failureNextStep": DialogStateTypeDef,
        "failureConditional": ConditionalSpecificationTypeDef,
        "codeHook": DialogCodeHookInvocationSettingTypeDef,
        "elicitationCodeHook": ElicitationCodeHookInvocationSettingTypeDef,
    },
    total=False,
)

CreateIntentResponseTypeDef = TypedDict(
    "CreateIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List[SampleUtteranceOutputTypeDef],
        "dialogCodeHook": DialogCodeHookSettingsOutputTypeDef,
        "fulfillmentCodeHook": FulfillmentCodeHookSettingsOutputTypeDef,
        "intentConfirmationSetting": IntentConfirmationSettingOutputTypeDef,
        "intentClosingSetting": IntentClosingSettingOutputTypeDef,
        "inputContexts": List[InputContextOutputTypeDef],
        "outputContexts": List[OutputContextOutputTypeDef],
        "kendraConfiguration": KendraConfigurationOutputTypeDef,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "initialResponseSetting": InitialResponseSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIntentResponseTypeDef = TypedDict(
    "DescribeIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List[SampleUtteranceOutputTypeDef],
        "dialogCodeHook": DialogCodeHookSettingsOutputTypeDef,
        "fulfillmentCodeHook": FulfillmentCodeHookSettingsOutputTypeDef,
        "slotPriorities": List[SlotPriorityOutputTypeDef],
        "intentConfirmationSetting": IntentConfirmationSettingOutputTypeDef,
        "intentClosingSetting": IntentClosingSettingOutputTypeDef,
        "inputContexts": List[InputContextOutputTypeDef],
        "outputContexts": List[OutputContextOutputTypeDef],
        "kendraConfiguration": KendraConfigurationOutputTypeDef,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "initialResponseSetting": InitialResponseSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIntentResponseTypeDef = TypedDict(
    "UpdateIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List[SampleUtteranceOutputTypeDef],
        "dialogCodeHook": DialogCodeHookSettingsOutputTypeDef,
        "fulfillmentCodeHook": FulfillmentCodeHookSettingsOutputTypeDef,
        "slotPriorities": List[SlotPriorityOutputTypeDef],
        "intentConfirmationSetting": IntentConfirmationSettingOutputTypeDef,
        "intentClosingSetting": IntentClosingSettingOutputTypeDef,
        "inputContexts": List[InputContextOutputTypeDef],
        "outputContexts": List[OutputContextOutputTypeDef],
        "kendraConfiguration": KendraConfigurationOutputTypeDef,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "initialResponseSetting": InitialResponseSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSlotValueElicitationSettingOutputTypeDef = TypedDict(
    "_RequiredSlotValueElicitationSettingOutputTypeDef",
    {
        "slotConstraint": SlotConstraintType,
    },
)
_OptionalSlotValueElicitationSettingOutputTypeDef = TypedDict(
    "_OptionalSlotValueElicitationSettingOutputTypeDef",
    {
        "defaultValueSpecification": SlotDefaultValueSpecificationOutputTypeDef,
        "promptSpecification": PromptSpecificationOutputTypeDef,
        "sampleUtterances": List[SampleUtteranceOutputTypeDef],
        "waitAndContinueSpecification": WaitAndContinueSpecificationOutputTypeDef,
        "slotCaptureSetting": SlotCaptureSettingOutputTypeDef,
    },
    total=False,
)


class SlotValueElicitationSettingOutputTypeDef(
    _RequiredSlotValueElicitationSettingOutputTypeDef,
    _OptionalSlotValueElicitationSettingOutputTypeDef,
):
    pass


_RequiredCreateIntentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntentRequestRequestTypeDef",
    {
        "intentName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalCreateIntentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntentRequestRequestTypeDef",
    {
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": Sequence[SampleUtteranceTypeDef],
        "dialogCodeHook": DialogCodeHookSettingsTypeDef,
        "fulfillmentCodeHook": FulfillmentCodeHookSettingsTypeDef,
        "intentConfirmationSetting": IntentConfirmationSettingTypeDef,
        "intentClosingSetting": IntentClosingSettingTypeDef,
        "inputContexts": Sequence[InputContextTypeDef],
        "outputContexts": Sequence[OutputContextTypeDef],
        "kendraConfiguration": KendraConfigurationTypeDef,
        "initialResponseSetting": InitialResponseSettingTypeDef,
    },
    total=False,
)


class CreateIntentRequestRequestTypeDef(
    _RequiredCreateIntentRequestRequestTypeDef, _OptionalCreateIntentRequestRequestTypeDef
):
    pass


_RequiredUpdateIntentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIntentRequestRequestTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalUpdateIntentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIntentRequestRequestTypeDef",
    {
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": Sequence[SampleUtteranceTypeDef],
        "dialogCodeHook": DialogCodeHookSettingsTypeDef,
        "fulfillmentCodeHook": FulfillmentCodeHookSettingsTypeDef,
        "slotPriorities": Sequence[SlotPriorityTypeDef],
        "intentConfirmationSetting": IntentConfirmationSettingTypeDef,
        "intentClosingSetting": IntentClosingSettingTypeDef,
        "inputContexts": Sequence[InputContextTypeDef],
        "outputContexts": Sequence[OutputContextTypeDef],
        "kendraConfiguration": KendraConfigurationTypeDef,
        "initialResponseSetting": InitialResponseSettingTypeDef,
    },
    total=False,
)


class UpdateIntentRequestRequestTypeDef(
    _RequiredUpdateIntentRequestRequestTypeDef, _OptionalUpdateIntentRequestRequestTypeDef
):
    pass


_RequiredSlotValueElicitationSettingTypeDef = TypedDict(
    "_RequiredSlotValueElicitationSettingTypeDef",
    {
        "slotConstraint": SlotConstraintType,
    },
)
_OptionalSlotValueElicitationSettingTypeDef = TypedDict(
    "_OptionalSlotValueElicitationSettingTypeDef",
    {
        "defaultValueSpecification": SlotDefaultValueSpecificationTypeDef,
        "promptSpecification": PromptSpecificationTypeDef,
        "sampleUtterances": Sequence[SampleUtteranceTypeDef],
        "waitAndContinueSpecification": WaitAndContinueSpecificationTypeDef,
        "slotCaptureSetting": SlotCaptureSettingTypeDef,
    },
    total=False,
)


class SlotValueElicitationSettingTypeDef(
    _RequiredSlotValueElicitationSettingTypeDef, _OptionalSlotValueElicitationSettingTypeDef
):
    pass


CreateSlotResponseTypeDef = TypedDict(
    "CreateSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": SlotValueElicitationSettingOutputTypeDef,
        "obfuscationSetting": ObfuscationSettingOutputTypeDef,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "multipleValuesSetting": MultipleValuesSettingOutputTypeDef,
        "subSlotSetting": SubSlotSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotResponseTypeDef = TypedDict(
    "DescribeSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": SlotValueElicitationSettingOutputTypeDef,
        "obfuscationSetting": ObfuscationSettingOutputTypeDef,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "multipleValuesSetting": MultipleValuesSettingOutputTypeDef,
        "subSlotSetting": SubSlotSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSlotResponseTypeDef = TypedDict(
    "UpdateSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": SlotValueElicitationSettingOutputTypeDef,
        "obfuscationSetting": ObfuscationSettingOutputTypeDef,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "multipleValuesSetting": MultipleValuesSettingOutputTypeDef,
        "subSlotSetting": SubSlotSettingOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSlotRequestRequestTypeDef",
    {
        "slotName": str,
        "valueElicitationSetting": SlotValueElicitationSettingTypeDef,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalCreateSlotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSlotRequestRequestTypeDef",
    {
        "description": str,
        "slotTypeId": str,
        "obfuscationSetting": ObfuscationSettingTypeDef,
        "multipleValuesSetting": MultipleValuesSettingTypeDef,
        "subSlotSetting": SubSlotSettingTypeDef,
    },
    total=False,
)


class CreateSlotRequestRequestTypeDef(
    _RequiredCreateSlotRequestRequestTypeDef, _OptionalCreateSlotRequestRequestTypeDef
):
    pass


_RequiredUpdateSlotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSlotRequestRequestTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "valueElicitationSetting": SlotValueElicitationSettingTypeDef,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalUpdateSlotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSlotRequestRequestTypeDef",
    {
        "description": str,
        "slotTypeId": str,
        "obfuscationSetting": ObfuscationSettingTypeDef,
        "multipleValuesSetting": MultipleValuesSettingTypeDef,
        "subSlotSetting": SubSlotSettingTypeDef,
    },
    total=False,
)


class UpdateSlotRequestRequestTypeDef(
    _RequiredUpdateSlotRequestRequestTypeDef, _OptionalUpdateSlotRequestRequestTypeDef
):
    pass
