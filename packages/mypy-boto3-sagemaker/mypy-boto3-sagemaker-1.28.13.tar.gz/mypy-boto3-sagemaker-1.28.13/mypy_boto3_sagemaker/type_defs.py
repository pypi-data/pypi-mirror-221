"""
Type annotations for sagemaker service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/type_defs/)

Usage::

    ```python
    from mypy_boto3_sagemaker.type_defs import ActionSourceOutputTypeDef

    data: ActionSourceOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionStatusType,
    AggregationTransformationValueType,
    AlgorithmSortByType,
    AlgorithmStatusType,
    AppImageConfigSortKeyType,
    AppInstanceTypeType,
    AppNetworkAccessTypeType,
    AppSecurityGroupManagementType,
    AppStatusType,
    AppTypeType,
    ArtifactSourceIdTypeType,
    AssemblyTypeType,
    AssociationEdgeTypeType,
    AsyncNotificationTopicTypesType,
    AthenaResultCompressionTypeType,
    AthenaResultFormatType,
    AuthModeType,
    AutoMLAlgorithmType,
    AutoMLChannelTypeType,
    AutoMLJobObjectiveTypeType,
    AutoMLJobSecondaryStatusType,
    AutoMLJobStatusType,
    AutoMLMetricEnumType,
    AutoMLMetricExtendedEnumType,
    AutoMLModeType,
    AutoMLProblemTypeConfigNameType,
    AutoMLProcessingUnitType,
    AutoMLS3DataTypeType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    AwsManagedHumanLoopRequestSourceType,
    BatchStrategyType,
    BooleanOperatorType,
    CandidateSortByType,
    CandidateStatusType,
    CandidateStepTypeType,
    CapacitySizeTypeType,
    CaptureModeType,
    CaptureStatusType,
    ClarifyFeatureTypeType,
    ClarifyTextGranularityType,
    ClarifyTextLanguageType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CompilationJobStatusType,
    CompleteOnConvergenceType,
    CompressionTypeType,
    ConditionOutcomeType,
    ContainerModeType,
    ContentClassifierType,
    CrossAccountFilterOptionType,
    DataDistributionTypeType,
    DetailedAlgorithmStatusType,
    DetailedModelPackageStatusType,
    DeviceDeploymentStatusType,
    DeviceSubsetTypeType,
    DirectInternetAccessType,
    DirectionType,
    DomainStatusType,
    EdgePackagingJobStatusType,
    EdgePresetDeploymentStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionRoleIdentityConfigType,
    ExecutionStatusType,
    FailureHandlingPolicyType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    FeatureStatusType,
    FeatureTypeType,
    FileSystemAccessModeType,
    FileSystemTypeType,
    FillingTypeType,
    FlowDefinitionStatusType,
    FrameworkType,
    HubContentSortByType,
    HubContentStatusType,
    HubContentTypeType,
    HubSortByType,
    HubStatusType,
    HumanTaskUiStatusType,
    HyperParameterScalingTypeType,
    HyperParameterTuningJobObjectiveTypeType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    HyperParameterTuningJobStrategyTypeType,
    HyperParameterTuningJobWarmStartTypeType,
    ImageSortByType,
    ImageSortOrderType,
    ImageStatusType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    ImageVersionStatusType,
    InferenceExecutionModeType,
    InferenceExperimentStatusType,
    InferenceExperimentStopDesiredStateType,
    InputModeType,
    InstanceTypeType,
    JobTypeType,
    JoinSourceType,
    LabelingJobStatusType,
    LastUpdateStatusValueType,
    LineageTypeType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgeDeploymentPlansSortByType,
    ListEdgePackagingJobsSortByType,
    ListInferenceRecommendationsJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    MetricSetSourceType,
    ModelApprovalStatusType,
    ModelCacheSettingType,
    ModelCardExportJobSortByType,
    ModelCardExportJobSortOrderType,
    ModelCardExportJobStatusType,
    ModelCardProcessingStatusType,
    ModelCardSortByType,
    ModelCardSortOrderType,
    ModelCardStatusType,
    ModelCompressionTypeType,
    ModelMetadataFilterTypeType,
    ModelPackageGroupSortByType,
    ModelPackageGroupStatusType,
    ModelPackageSortByType,
    ModelPackageStatusType,
    ModelPackageTypeType,
    ModelSortKeyType,
    ModelVariantActionType,
    ModelVariantStatusType,
    MonitoringAlertHistorySortKeyType,
    MonitoringAlertStatusType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringProblemTypeType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceAcceleratorTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    NotebookOutputOptionType,
    ObjectiveStatusType,
    OfflineStoreStatusValueType,
    OperatorType,
    OrderKeyType,
    OutputCompressionTypeType,
    ParameterTypeType,
    PipelineExecutionStatusType,
    ProblemTypeType,
    ProcessingInstanceTypeType,
    ProcessingJobStatusType,
    ProcessingS3CompressionTypeType,
    ProcessingS3DataDistributionTypeType,
    ProcessingS3DataTypeType,
    ProcessingS3InputModeType,
    ProcessingS3UploadModeType,
    ProcessorType,
    ProductionVariantAcceleratorTypeType,
    ProductionVariantInstanceTypeType,
    ProfilingStatusType,
    ProjectSortByType,
    ProjectSortOrderType,
    ProjectStatusType,
    RecommendationJobStatusType,
    RecommendationJobSupportedEndpointTypeType,
    RecommendationJobTypeType,
    RecommendationStatusType,
    RecordWrapperType,
    RedshiftResultCompressionTypeType,
    RedshiftResultFormatType,
    RepositoryAccessModeType,
    ResourceCatalogSortOrderType,
    ResourceTypeType,
    RetentionTypeType,
    RootAccessType,
    RStudioServerProAccessStatusType,
    RStudioServerProUserGroupType,
    RuleEvaluationStatusType,
    S3DataDistributionType,
    S3DataTypeType,
    S3ModelDataTypeType,
    SagemakerServicecatalogStatusType,
    ScheduleStatusType,
    SearchSortOrderType,
    SecondaryStatusType,
    SortActionsByType,
    SortAssociationsByType,
    SortByType,
    SortContextsByType,
    SortExperimentsByType,
    SortInferenceExperimentsByType,
    SortLineageGroupsByType,
    SortOrderType,
    SortPipelineExecutionsByType,
    SortPipelinesByType,
    SortTrialComponentsByType,
    SortTrialsByType,
    SpaceSortKeyType,
    SpaceStatusType,
    SplitTypeType,
    StageStatusType,
    StepStatusType,
    StudioLifecycleConfigAppTypeType,
    StudioLifecycleConfigSortKeyType,
    TableFormatType,
    TargetDeviceType,
    TargetPlatformAcceleratorType,
    TargetPlatformArchType,
    TargetPlatformOsType,
    TrafficRoutingConfigTypeType,
    TrainingInputModeType,
    TrainingInstanceTypeType,
    TrainingJobEarlyStoppingTypeType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TrainingRepositoryAccessModeType,
    TransformInstanceTypeType,
    TransformJobStatusType,
    TrialComponentPrimaryStatusType,
    TtlDurationUnitType,
    UserProfileSortKeyType,
    UserProfileStatusType,
    VariantPropertyTypeType,
    VariantStatusType,
    VendorGuidanceType,
    WarmPoolResourceStatusType,
    WorkforceStatusType,
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
    "ActionSourceOutputTypeDef",
    "ActionSourceTypeDef",
    "AddAssociationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "TagOutputTypeDef",
    "AgentVersionTypeDef",
    "AlarmOutputTypeDef",
    "AlarmTypeDef",
    "MetricDefinitionOutputTypeDef",
    "MetricDefinitionTypeDef",
    "AlgorithmStatusItemTypeDef",
    "AlgorithmSummaryTypeDef",
    "AnnotationConsolidationConfigOutputTypeDef",
    "AnnotationConsolidationConfigTypeDef",
    "AppDetailsTypeDef",
    "AppSpecificationOutputTypeDef",
    "AppSpecificationTypeDef",
    "ArtifactSourceTypeOutputTypeDef",
    "ArtifactSourceTypeTypeDef",
    "AssociateTrialComponentRequestRequestTypeDef",
    "AsyncInferenceClientConfigOutputTypeDef",
    "AsyncInferenceClientConfigTypeDef",
    "AsyncInferenceNotificationConfigOutputTypeDef",
    "AsyncInferenceNotificationConfigTypeDef",
    "AthenaDatasetDefinitionOutputTypeDef",
    "AthenaDatasetDefinitionTypeDef",
    "AutoMLAlgorithmConfigOutputTypeDef",
    "AutoMLAlgorithmConfigTypeDef",
    "AutoMLCandidateStepTypeDef",
    "AutoMLContainerDefinitionTypeDef",
    "FinalAutoMLJobObjectiveMetricTypeDef",
    "AutoMLS3DataSourceOutputTypeDef",
    "AutoMLS3DataSourceTypeDef",
    "AutoMLDataSplitConfigOutputTypeDef",
    "AutoMLDataSplitConfigTypeDef",
    "AutoMLJobArtifactsTypeDef",
    "AutoMLJobCompletionCriteriaOutputTypeDef",
    "AutoMLJobCompletionCriteriaTypeDef",
    "AutoMLJobObjectiveOutputTypeDef",
    "AutoMLJobObjectiveTypeDef",
    "AutoMLJobStepMetadataTypeDef",
    "AutoMLPartialFailureReasonTypeDef",
    "AutoMLOutputDataConfigOutputTypeDef",
    "AutoMLOutputDataConfigTypeDef",
    "TabularResolvedAttributesTypeDef",
    "VpcConfigOutputTypeDef",
    "VpcConfigTypeDef",
    "AutoParameterOutputTypeDef",
    "AutoParameterTypeDef",
    "AutotuneOutputTypeDef",
    "AutotuneTypeDef",
    "BatchDataCaptureConfigOutputTypeDef",
    "BatchDataCaptureConfigTypeDef",
    "BatchDescribeModelPackageErrorTypeDef",
    "BatchDescribeModelPackageInputRequestTypeDef",
    "BestObjectiveNotImprovingOutputTypeDef",
    "BestObjectiveNotImprovingTypeDef",
    "MetricsSourceOutputTypeDef",
    "MetricsSourceTypeDef",
    "CacheHitResultTypeDef",
    "OutputParameterOutputTypeDef",
    "CandidateArtifactLocationsTypeDef",
    "MetricDatumTypeDef",
    "ModelRegisterSettingsOutputTypeDef",
    "TimeSeriesForecastingSettingsOutputTypeDef",
    "WorkspaceSettingsOutputTypeDef",
    "ModelRegisterSettingsTypeDef",
    "TimeSeriesForecastingSettingsTypeDef",
    "WorkspaceSettingsTypeDef",
    "CapacitySizeOutputTypeDef",
    "CapacitySizeTypeDef",
    "CaptureContentTypeHeaderOutputTypeDef",
    "CaptureContentTypeHeaderTypeDef",
    "CaptureOptionOutputTypeDef",
    "CaptureOptionTypeDef",
    "CategoricalParameterOutputTypeDef",
    "CategoricalParameterRangeOutputTypeDef",
    "CategoricalParameterRangeSpecificationOutputTypeDef",
    "CategoricalParameterRangeSpecificationTypeDef",
    "CategoricalParameterRangeTypeDef",
    "CategoricalParameterTypeDef",
    "ShuffleConfigOutputTypeDef",
    "ChannelSpecificationOutputTypeDef",
    "ChannelSpecificationTypeDef",
    "ShuffleConfigTypeDef",
    "CheckpointConfigOutputTypeDef",
    "CheckpointConfigTypeDef",
    "ClarifyCheckStepMetadataTypeDef",
    "ClarifyInferenceConfigOutputTypeDef",
    "ClarifyInferenceConfigTypeDef",
    "ClarifyShapBaselineConfigOutputTypeDef",
    "ClarifyShapBaselineConfigTypeDef",
    "ClarifyTextConfigOutputTypeDef",
    "ClarifyTextConfigTypeDef",
    "CodeRepositoryOutputTypeDef",
    "GitConfigOutputTypeDef",
    "CodeRepositoryTypeDef",
    "CognitoConfigOutputTypeDef",
    "CognitoConfigTypeDef",
    "CognitoMemberDefinitionOutputTypeDef",
    "CognitoMemberDefinitionTypeDef",
    "CollectionConfigurationOutputTypeDef",
    "CollectionConfigurationTypeDef",
    "CompilationJobSummaryTypeDef",
    "ConditionStepMetadataTypeDef",
    "MultiModelConfigOutputTypeDef",
    "MultiModelConfigTypeDef",
    "ContextSourceOutputTypeDef",
    "ContextSourceTypeDef",
    "ContinuousParameterRangeOutputTypeDef",
    "ContinuousParameterRangeSpecificationOutputTypeDef",
    "ContinuousParameterRangeSpecificationTypeDef",
    "ContinuousParameterRangeTypeDef",
    "ConvergenceDetectedOutputTypeDef",
    "ConvergenceDetectedTypeDef",
    "MetadataPropertiesTypeDef",
    "ResourceSpecTypeDef",
    "ModelDeployConfigTypeDef",
    "GitConfigTypeDef",
    "InputConfigTypeDef",
    "NeoVpcConfigTypeDef",
    "StoppingConditionTypeDef",
    "DataQualityAppSpecificationTypeDef",
    "MonitoringStoppingConditionTypeDef",
    "EdgeOutputConfigTypeDef",
    "EdgeDeploymentModelConfigTypeDef",
    "FeatureDefinitionTypeDef",
    "FlowDefinitionOutputConfigTypeDef",
    "HumanLoopRequestSourceTypeDef",
    "HubS3StorageConfigTypeDef",
    "UiTemplateTypeDef",
    "CreateImageVersionRequestRequestTypeDef",
    "InferenceExperimentScheduleTypeDef",
    "LabelingJobOutputConfigTypeDef",
    "LabelingJobStoppingConditionsTypeDef",
    "ModelBiasAppSpecificationTypeDef",
    "ModelCardExportOutputConfigTypeDef",
    "ModelCardSecurityConfigTypeDef",
    "ModelExplainabilityAppSpecificationTypeDef",
    "InferenceExecutionConfigTypeDef",
    "ModelQualityAppSpecificationTypeDef",
    "InstanceMetadataServiceConfigurationTypeDef",
    "NotebookInstanceLifecycleHookTypeDef",
    "ParallelismConfigurationTypeDef",
    "PipelineDefinitionS3LocationTypeDef",
    "CreatePresignedDomainUrlRequestRequestTypeDef",
    "CreatePresignedNotebookInstanceUrlInputRequestTypeDef",
    "ExperimentConfigTypeDef",
    "ProcessingStoppingConditionTypeDef",
    "DebugRuleConfigurationTypeDef",
    "OutputDataConfigTypeDef",
    "ProfilerConfigTypeDef",
    "ProfilerRuleConfigurationTypeDef",
    "RetryStrategyTypeDef",
    "TensorBoardOutputConfigTypeDef",
    "DataProcessingTypeDef",
    "ModelClientConfigTypeDef",
    "TransformOutputTypeDef",
    "TransformResourcesTypeDef",
    "TrialComponentArtifactTypeDef",
    "TrialComponentParameterValueTypeDef",
    "TrialComponentStatusTypeDef",
    "OidcConfigTypeDef",
    "SourceIpConfigTypeDef",
    "WorkforceVpcConfigRequestTypeDef",
    "NotificationConfigurationTypeDef",
    "CustomImageOutputTypeDef",
    "CustomImageTypeDef",
    "DataCaptureConfigSummaryTypeDef",
    "DataCatalogConfigOutputTypeDef",
    "DataCatalogConfigTypeDef",
    "DataProcessingOutputTypeDef",
    "DataQualityAppSpecificationOutputTypeDef",
    "MonitoringConstraintsResourceOutputTypeDef",
    "MonitoringStatisticsResourceOutputTypeDef",
    "MonitoringConstraintsResourceTypeDef",
    "MonitoringStatisticsResourceTypeDef",
    "EndpointInputOutputTypeDef",
    "EndpointInputTypeDef",
    "FileSystemDataSourceOutputTypeDef",
    "S3DataSourceOutputTypeDef",
    "FileSystemDataSourceTypeDef",
    "S3DataSourceTypeDef",
    "RedshiftDatasetDefinitionOutputTypeDef",
    "RedshiftDatasetDefinitionTypeDef",
    "DebugRuleConfigurationOutputTypeDef",
    "DebugRuleEvaluationStatusTypeDef",
    "DeleteActionRequestRequestTypeDef",
    "DeleteAlgorithmInputRequestTypeDef",
    "DeleteAppImageConfigRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAssociationRequestRequestTypeDef",
    "DeleteCodeRepositoryInputRequestTypeDef",
    "DeleteContextRequestRequestTypeDef",
    "DeleteDataQualityJobDefinitionRequestRequestTypeDef",
    "DeleteDeviceFleetRequestRequestTypeDef",
    "RetentionPolicyTypeDef",
    "DeleteEdgeDeploymentPlanRequestRequestTypeDef",
    "DeleteEdgeDeploymentStageRequestRequestTypeDef",
    "DeleteEndpointConfigInputRequestTypeDef",
    "DeleteEndpointInputRequestTypeDef",
    "DeleteExperimentRequestRequestTypeDef",
    "DeleteFeatureGroupRequestRequestTypeDef",
    "DeleteFlowDefinitionRequestRequestTypeDef",
    "DeleteHubContentRequestRequestTypeDef",
    "DeleteHubRequestRequestTypeDef",
    "DeleteHumanTaskUiRequestRequestTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteImageVersionRequestRequestTypeDef",
    "DeleteInferenceExperimentRequestRequestTypeDef",
    "DeleteModelBiasJobDefinitionRequestRequestTypeDef",
    "DeleteModelCardRequestRequestTypeDef",
    "DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "DeleteModelInputRequestTypeDef",
    "DeleteModelPackageGroupInputRequestTypeDef",
    "DeleteModelPackageGroupPolicyInputRequestTypeDef",
    "DeleteModelPackageInputRequestTypeDef",
    "DeleteModelQualityJobDefinitionRequestRequestTypeDef",
    "DeleteMonitoringScheduleRequestRequestTypeDef",
    "DeleteNotebookInstanceInputRequestTypeDef",
    "DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeleteProjectInputRequestTypeDef",
    "DeleteSpaceRequestRequestTypeDef",
    "DeleteStudioLifecycleConfigRequestRequestTypeDef",
    "DeleteTagsInputRequestTypeDef",
    "DeleteTrialComponentRequestRequestTypeDef",
    "DeleteTrialRequestRequestTypeDef",
    "DeleteUserProfileRequestRequestTypeDef",
    "DeleteWorkforceRequestRequestTypeDef",
    "DeleteWorkteamRequestRequestTypeDef",
    "DeployedImageTypeDef",
    "RealTimeInferenceRecommendationTypeDef",
    "DeviceSelectionConfigOutputTypeDef",
    "EdgeDeploymentConfigOutputTypeDef",
    "EdgeDeploymentStatusTypeDef",
    "DeviceSelectionConfigTypeDef",
    "EdgeDeploymentConfigTypeDef",
    "DeregisterDevicesRequestRequestTypeDef",
    "DescribeActionRequestRequestTypeDef",
    "MetadataPropertiesOutputTypeDef",
    "DescribeAlgorithmInputRequestTypeDef",
    "DescribeAppImageConfigRequestRequestTypeDef",
    "DescribeAppRequestRequestTypeDef",
    "ResourceSpecOutputTypeDef",
    "DescribeArtifactRequestRequestTypeDef",
    "DescribeAutoMLJobRequestRequestTypeDef",
    "ModelDeployConfigOutputTypeDef",
    "ModelDeployResultTypeDef",
    "DescribeAutoMLJobV2RequestRequestTypeDef",
    "DescribeCodeRepositoryInputRequestTypeDef",
    "DescribeCompilationJobRequestRequestTypeDef",
    "InputConfigOutputTypeDef",
    "ModelArtifactsTypeDef",
    "ModelDigestsTypeDef",
    "NeoVpcConfigOutputTypeDef",
    "StoppingConditionOutputTypeDef",
    "DescribeContextRequestRequestTypeDef",
    "DescribeDataQualityJobDefinitionRequestRequestTypeDef",
    "MonitoringStoppingConditionOutputTypeDef",
    "DescribeDeviceFleetRequestRequestTypeDef",
    "EdgeOutputConfigOutputTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "EdgeModelTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeEdgeDeploymentPlanRequestRequestTypeDef",
    "EdgeDeploymentModelConfigOutputTypeDef",
    "DescribeEdgePackagingJobRequestRequestTypeDef",
    "EdgePresetDeploymentOutputTypeDef",
    "DescribeEndpointConfigInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeEndpointInputRequestTypeDef",
    "DescribeExperimentRequestRequestTypeDef",
    "ExperimentSourceTypeDef",
    "DescribeFeatureGroupRequestRequestTypeDef",
    "FeatureDefinitionOutputTypeDef",
    "LastUpdateStatusTypeDef",
    "OfflineStoreStatusTypeDef",
    "DescribeFeatureMetadataRequestRequestTypeDef",
    "FeatureParameterOutputTypeDef",
    "DescribeFlowDefinitionRequestRequestTypeDef",
    "FlowDefinitionOutputConfigOutputTypeDef",
    "HumanLoopRequestSourceOutputTypeDef",
    "DescribeHubContentRequestRequestTypeDef",
    "HubContentDependencyTypeDef",
    "DescribeHubRequestRequestTypeDef",
    "HubS3StorageConfigOutputTypeDef",
    "DescribeHumanTaskUiRequestRequestTypeDef",
    "UiTemplateInfoTypeDef",
    "DescribeHyperParameterTuningJobRequestRequestTypeDef",
    "HyperParameterTuningJobCompletionDetailsTypeDef",
    "HyperParameterTuningJobConsumedResourcesTypeDef",
    "ObjectiveStatusCountersTypeDef",
    "TrainingJobStatusCountersTypeDef",
    "DescribeImageRequestRequestTypeDef",
    "DescribeImageVersionRequestRequestTypeDef",
    "DescribeInferenceExperimentRequestRequestTypeDef",
    "EndpointMetadataTypeDef",
    "InferenceExperimentScheduleOutputTypeDef",
    "DescribeInferenceRecommendationsJobRequestRequestTypeDef",
    "DescribeLabelingJobRequestRequestTypeDef",
    "LabelCountersTypeDef",
    "LabelingJobOutputConfigOutputTypeDef",
    "LabelingJobOutputTypeDef",
    "LabelingJobStoppingConditionsOutputTypeDef",
    "DescribeLineageGroupRequestRequestTypeDef",
    "DescribeModelBiasJobDefinitionRequestRequestTypeDef",
    "ModelBiasAppSpecificationOutputTypeDef",
    "DescribeModelCardExportJobRequestRequestTypeDef",
    "ModelCardExportArtifactsTypeDef",
    "ModelCardExportOutputConfigOutputTypeDef",
    "DescribeModelCardRequestRequestTypeDef",
    "ModelCardSecurityConfigOutputTypeDef",
    "DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "ModelExplainabilityAppSpecificationOutputTypeDef",
    "DescribeModelInputRequestTypeDef",
    "InferenceExecutionConfigOutputTypeDef",
    "DescribeModelPackageGroupInputRequestTypeDef",
    "DescribeModelPackageInputRequestTypeDef",
    "DescribeModelQualityJobDefinitionRequestRequestTypeDef",
    "ModelQualityAppSpecificationOutputTypeDef",
    "DescribeMonitoringScheduleRequestRequestTypeDef",
    "MonitoringExecutionSummaryTypeDef",
    "DescribeNotebookInstanceInputRequestTypeDef",
    "DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "NotebookInstanceLifecycleHookOutputTypeDef",
    "InstanceMetadataServiceConfigurationOutputTypeDef",
    "DescribePipelineDefinitionForExecutionRequestRequestTypeDef",
    "DescribePipelineExecutionRequestRequestTypeDef",
    "ParallelismConfigurationOutputTypeDef",
    "PipelineExperimentConfigTypeDef",
    "DescribePipelineRequestRequestTypeDef",
    "DescribeProcessingJobRequestRequestTypeDef",
    "ExperimentConfigOutputTypeDef",
    "ProcessingStoppingConditionOutputTypeDef",
    "DescribeProjectInputRequestTypeDef",
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    "DescribeSpaceRequestRequestTypeDef",
    "DescribeStudioLifecycleConfigRequestRequestTypeDef",
    "DescribeSubscribedWorkteamRequestRequestTypeDef",
    "SubscribedWorkteamTypeDef",
    "DescribeTrainingJobRequestRequestTypeDef",
    "MetricDataTypeDef",
    "OutputDataConfigOutputTypeDef",
    "ProfilerConfigOutputTypeDef",
    "ProfilerRuleConfigurationOutputTypeDef",
    "ProfilerRuleEvaluationStatusTypeDef",
    "RetryStrategyOutputTypeDef",
    "SecondaryStatusTransitionTypeDef",
    "TensorBoardOutputConfigOutputTypeDef",
    "WarmPoolStatusTypeDef",
    "DescribeTransformJobRequestRequestTypeDef",
    "ModelClientConfigOutputTypeDef",
    "TransformResourcesOutputTypeDef",
    "DescribeTrialComponentRequestRequestTypeDef",
    "TrialComponentArtifactOutputTypeDef",
    "TrialComponentMetricSummaryTypeDef",
    "TrialComponentParameterValueOutputTypeDef",
    "TrialComponentSourceTypeDef",
    "TrialComponentStatusOutputTypeDef",
    "DescribeTrialRequestRequestTypeDef",
    "TrialSourceTypeDef",
    "DescribeUserProfileRequestRequestTypeDef",
    "DescribeWorkforceRequestRequestTypeDef",
    "DescribeWorkteamRequestRequestTypeDef",
    "ProductionVariantServerlessUpdateConfigTypeDef",
    "DeviceDeploymentSummaryTypeDef",
    "DeviceFleetSummaryTypeDef",
    "DeviceStatsTypeDef",
    "EdgeModelSummaryTypeDef",
    "DeviceTypeDef",
    "DisassociateTrialComponentRequestRequestTypeDef",
    "DomainDetailsTypeDef",
    "FileSourceOutputTypeDef",
    "FileSourceTypeDef",
    "EMRStepMetadataTypeDef",
    "EdgeDeploymentPlanSummaryTypeDef",
    "EdgeModelStatTypeDef",
    "EdgePackagingJobSummaryTypeDef",
    "EdgeTypeDef",
    "EndpointConfigSummaryTypeDef",
    "EndpointInfoOutputTypeDef",
    "EndpointInfoTypeDef",
    "ProductionVariantServerlessConfigOutputTypeDef",
    "ProductionVariantServerlessConfigTypeDef",
    "InferenceMetricsTypeDef",
    "EndpointSummaryTypeDef",
    "EnvironmentParameterTypeDef",
    "FailStepMetadataTypeDef",
    "FeatureParameterTypeDef",
    "FileSystemConfigOutputTypeDef",
    "FileSystemConfigTypeDef",
    "FilterTypeDef",
    "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "FlowDefinitionSummaryTypeDef",
    "GetDeviceFleetReportRequestRequestTypeDef",
    "GetLineageGroupPolicyRequestRequestTypeDef",
    "GetModelPackageGroupPolicyInputRequestTypeDef",
    "PropertyNameSuggestionTypeDef",
    "GitConfigForUpdateTypeDef",
    "HubContentInfoTypeDef",
    "HubInfoTypeDef",
    "HumanLoopActivationConditionsConfigOutputTypeDef",
    "HumanLoopActivationConditionsConfigTypeDef",
    "UiConfigOutputTypeDef",
    "UiConfigTypeDef",
    "HumanTaskUiSummaryTypeDef",
    "HyperParameterTuningJobObjectiveOutputTypeDef",
    "HyperParameterTuningJobObjectiveTypeDef",
    "HyperParameterTuningInstanceConfigOutputTypeDef",
    "HyperParameterTuningInstanceConfigTypeDef",
    "ResourceLimitsOutputTypeDef",
    "ResourceLimitsTypeDef",
    "HyperbandStrategyConfigOutputTypeDef",
    "HyperbandStrategyConfigTypeDef",
    "ParentHyperParameterTuningJobOutputTypeDef",
    "ParentHyperParameterTuningJobTypeDef",
    "IamIdentityTypeDef",
    "RepositoryAuthConfigOutputTypeDef",
    "RepositoryAuthConfigTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "RecommendationMetricsTypeDef",
    "InferenceRecommendationsJobTypeDef",
    "InstanceGroupOutputTypeDef",
    "InstanceGroupTypeDef",
    "IntegerParameterRangeOutputTypeDef",
    "IntegerParameterRangeSpecificationOutputTypeDef",
    "IntegerParameterRangeSpecificationTypeDef",
    "IntegerParameterRangeTypeDef",
    "KernelSpecOutputTypeDef",
    "KernelSpecTypeDef",
    "LabelCountersForWorkteamTypeDef",
    "LabelingJobDataAttributesOutputTypeDef",
    "LabelingJobDataAttributesTypeDef",
    "LabelingJobS3DataSourceOutputTypeDef",
    "LabelingJobSnsDataSourceOutputTypeDef",
    "LabelingJobS3DataSourceTypeDef",
    "LabelingJobSnsDataSourceTypeDef",
    "LineageGroupSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListActionsRequestRequestTypeDef",
    "ListAlgorithmsInputRequestTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListAppImageConfigsRequestRequestTypeDef",
    "ListAppsRequestRequestTypeDef",
    "ListArtifactsRequestRequestTypeDef",
    "ListAssociationsRequestRequestTypeDef",
    "ListAutoMLJobsRequestRequestTypeDef",
    "ListCandidatesForAutoMLJobRequestRequestTypeDef",
    "ListCodeRepositoriesInputRequestTypeDef",
    "ListCompilationJobsRequestRequestTypeDef",
    "ListContextsRequestRequestTypeDef",
    "ListDataQualityJobDefinitionsRequestRequestTypeDef",
    "MonitoringJobDefinitionSummaryTypeDef",
    "ListDeviceFleetsRequestRequestTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListEdgeDeploymentPlansRequestRequestTypeDef",
    "ListEdgePackagingJobsRequestRequestTypeDef",
    "ListEndpointConfigsInputRequestTypeDef",
    "ListEndpointsInputRequestTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListFeatureGroupsRequestRequestTypeDef",
    "ListFlowDefinitionsRequestRequestTypeDef",
    "ListHubContentVersionsRequestRequestTypeDef",
    "ListHubContentsRequestRequestTypeDef",
    "ListHubsRequestRequestTypeDef",
    "ListHumanTaskUisRequestRequestTypeDef",
    "ListHyperParameterTuningJobsRequestRequestTypeDef",
    "ListImageVersionsRequestRequestTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListInferenceExperimentsRequestRequestTypeDef",
    "ListInferenceRecommendationsJobStepsRequestRequestTypeDef",
    "ListInferenceRecommendationsJobsRequestRequestTypeDef",
    "ListLabelingJobsForWorkteamRequestRequestTypeDef",
    "ListLabelingJobsRequestRequestTypeDef",
    "ListLineageGroupsRequestRequestTypeDef",
    "ListModelBiasJobDefinitionsRequestRequestTypeDef",
    "ListModelCardExportJobsRequestRequestTypeDef",
    "ModelCardExportJobSummaryTypeDef",
    "ListModelCardVersionsRequestRequestTypeDef",
    "ModelCardVersionSummaryTypeDef",
    "ListModelCardsRequestRequestTypeDef",
    "ModelCardSummaryTypeDef",
    "ListModelExplainabilityJobDefinitionsRequestRequestTypeDef",
    "ModelMetadataSummaryTypeDef",
    "ListModelPackageGroupsInputRequestTypeDef",
    "ModelPackageGroupSummaryTypeDef",
    "ListModelPackagesInputRequestTypeDef",
    "ModelPackageSummaryTypeDef",
    "ListModelQualityJobDefinitionsRequestRequestTypeDef",
    "ListModelsInputRequestTypeDef",
    "ModelSummaryTypeDef",
    "ListMonitoringAlertHistoryRequestRequestTypeDef",
    "MonitoringAlertHistorySummaryTypeDef",
    "ListMonitoringAlertsRequestRequestTypeDef",
    "ListMonitoringExecutionsRequestRequestTypeDef",
    "ListMonitoringSchedulesRequestRequestTypeDef",
    "MonitoringScheduleSummaryTypeDef",
    "ListNotebookInstanceLifecycleConfigsInputRequestTypeDef",
    "NotebookInstanceLifecycleConfigSummaryTypeDef",
    "ListNotebookInstancesInputRequestTypeDef",
    "NotebookInstanceSummaryTypeDef",
    "ListPipelineExecutionStepsRequestRequestTypeDef",
    "ListPipelineExecutionsRequestRequestTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "ListPipelineParametersForExecutionRequestRequestTypeDef",
    "ParameterOutputTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "PipelineSummaryTypeDef",
    "ListProcessingJobsRequestRequestTypeDef",
    "ProcessingJobSummaryTypeDef",
    "ListProjectsInputRequestTypeDef",
    "ProjectSummaryTypeDef",
    "ListResourceCatalogsRequestRequestTypeDef",
    "ResourceCatalogTypeDef",
    "ListSpacesRequestRequestTypeDef",
    "SpaceDetailsTypeDef",
    "ListStageDevicesRequestRequestTypeDef",
    "ListStudioLifecycleConfigsRequestRequestTypeDef",
    "StudioLifecycleConfigDetailsTypeDef",
    "ListSubscribedWorkteamsRequestRequestTypeDef",
    "ListTagsInputRequestTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef",
    "ListTrainingJobsRequestRequestTypeDef",
    "ListTransformJobsRequestRequestTypeDef",
    "TransformJobSummaryTypeDef",
    "ListTrialComponentsRequestRequestTypeDef",
    "ListTrialsRequestRequestTypeDef",
    "ListUserProfilesRequestRequestTypeDef",
    "UserProfileDetailsTypeDef",
    "ListWorkforcesRequestRequestTypeDef",
    "ListWorkteamsRequestRequestTypeDef",
    "OidcMemberDefinitionOutputTypeDef",
    "OidcMemberDefinitionTypeDef",
    "MonitoringGroundTruthS3InputOutputTypeDef",
    "MonitoringGroundTruthS3InputTypeDef",
    "ModelDashboardEndpointTypeDef",
    "ModelDashboardIndicatorActionTypeDef",
    "S3ModelDataSourceOutputTypeDef",
    "S3ModelDataSourceTypeDef",
    "RealTimeInferenceConfigOutputTypeDef",
    "RealTimeInferenceConfigTypeDef",
    "ModelInputOutputTypeDef",
    "ModelInputTypeDef",
    "ModelLatencyThresholdOutputTypeDef",
    "ModelLatencyThresholdTypeDef",
    "ModelMetadataFilterTypeDef",
    "ModelPackageStatusItemTypeDef",
    "ModelStepMetadataTypeDef",
    "MonitoringAppSpecificationOutputTypeDef",
    "MonitoringAppSpecificationTypeDef",
    "MonitoringClusterConfigOutputTypeDef",
    "MonitoringClusterConfigTypeDef",
    "MonitoringCsvDatasetFormatOutputTypeDef",
    "MonitoringCsvDatasetFormatTypeDef",
    "MonitoringJsonDatasetFormatOutputTypeDef",
    "MonitoringJsonDatasetFormatTypeDef",
    "MonitoringS3OutputTypeDef",
    "ScheduleConfigOutputTypeDef",
    "ScheduleConfigTypeDef",
    "NotificationConfigurationOutputTypeDef",
    "S3StorageConfigOutputTypeDef",
    "S3StorageConfigTypeDef",
    "OidcConfigForResponseTypeDef",
    "OnlineStoreSecurityConfigOutputTypeDef",
    "TtlDurationOutputTypeDef",
    "OnlineStoreSecurityConfigTypeDef",
    "TtlDurationTypeDef",
    "TargetPlatformOutputTypeDef",
    "TargetPlatformTypeDef",
    "OutputParameterTypeDef",
    "ParameterTypeDef",
    "ParentTypeDef",
    "ProductionVariantStatusTypeDef",
    "PhaseOutputTypeDef",
    "PhaseTypeDef",
    "ProcessingJobStepMetadataTypeDef",
    "QualityCheckStepMetadataTypeDef",
    "RegisterModelStepMetadataTypeDef",
    "TrainingJobStepMetadataTypeDef",
    "TransformJobStepMetadataTypeDef",
    "TuningJobStepMetaDataTypeDef",
    "SelectiveExecutionResultTypeDef",
    "ProcessingClusterConfigOutputTypeDef",
    "ProcessingClusterConfigTypeDef",
    "ProcessingFeatureStoreOutputTypeDef",
    "ProcessingS3InputOutputTypeDef",
    "ProcessingS3InputTypeDef",
    "ProcessingS3OutputTypeDef",
    "ProductionVariantCoreDumpConfigOutputTypeDef",
    "ProductionVariantCoreDumpConfigTypeDef",
    "ProfilerConfigForUpdateTypeDef",
    "PropertyNameQueryTypeDef",
    "ProvisioningParameterOutputTypeDef",
    "ProvisioningParameterTypeDef",
    "USDOutputTypeDef",
    "USDTypeDef",
    "PutModelPackageGroupPolicyInputRequestTypeDef",
    "QueryFiltersTypeDef",
    "VertexTypeDef",
    "RStudioServerProAppSettingsOutputTypeDef",
    "RStudioServerProAppSettingsTypeDef",
    "RecommendationJobCompiledOutputConfigTypeDef",
    "RecommendationJobPayloadConfigOutputTypeDef",
    "RecommendationJobPayloadConfigTypeDef",
    "RecommendationJobResourceLimitOutputTypeDef",
    "RecommendationJobVpcConfigOutputTypeDef",
    "RecommendationJobResourceLimitTypeDef",
    "RecommendationJobVpcConfigTypeDef",
    "RenderableTaskTypeDef",
    "RenderingErrorTypeDef",
    "ResourceConfigForUpdateTypeDef",
    "SearchRequestRequestTypeDef",
    "SelectedStepOutputTypeDef",
    "SelectedStepTypeDef",
    "SendPipelineExecutionStepFailureRequestRequestTypeDef",
    "ShadowModelVariantConfigOutputTypeDef",
    "ShadowModelVariantConfigTypeDef",
    "SharingSettingsOutputTypeDef",
    "SharingSettingsTypeDef",
    "SourceAlgorithmOutputTypeDef",
    "SourceAlgorithmTypeDef",
    "SourceIpConfigOutputTypeDef",
    "StartEdgeDeploymentStageRequestRequestTypeDef",
    "StartInferenceExperimentRequestRequestTypeDef",
    "StartMonitoringScheduleRequestRequestTypeDef",
    "StartNotebookInstanceInputRequestTypeDef",
    "StopAutoMLJobRequestRequestTypeDef",
    "StopCompilationJobRequestRequestTypeDef",
    "StopEdgeDeploymentStageRequestRequestTypeDef",
    "StopEdgePackagingJobRequestRequestTypeDef",
    "StopHyperParameterTuningJobRequestRequestTypeDef",
    "StopInferenceRecommendationsJobRequestRequestTypeDef",
    "StopLabelingJobRequestRequestTypeDef",
    "StopMonitoringScheduleRequestRequestTypeDef",
    "StopNotebookInstanceInputRequestTypeDef",
    "StopPipelineExecutionRequestRequestTypeDef",
    "StopProcessingJobRequestRequestTypeDef",
    "StopTrainingJobRequestRequestTypeDef",
    "StopTransformJobRequestRequestTypeDef",
    "TimeSeriesConfigOutputTypeDef",
    "TimeSeriesConfigTypeDef",
    "TimeSeriesTransformationsOutputTypeDef",
    "TimeSeriesTransformationsTypeDef",
    "TrainingRepositoryAuthConfigOutputTypeDef",
    "TrainingRepositoryAuthConfigTypeDef",
    "TransformS3DataSourceOutputTypeDef",
    "TransformS3DataSourceTypeDef",
    "UpdateActionRequestRequestTypeDef",
    "UpdateArtifactRequestRequestTypeDef",
    "UpdateContextRequestRequestTypeDef",
    "VariantPropertyTypeDef",
    "UpdateExperimentRequestRequestTypeDef",
    "UpdateHubRequestRequestTypeDef",
    "UpdateImageRequestRequestTypeDef",
    "UpdateImageVersionRequestRequestTypeDef",
    "UpdateModelCardRequestRequestTypeDef",
    "UpdateMonitoringAlertRequestRequestTypeDef",
    "UpdateTrialRequestRequestTypeDef",
    "WorkforceVpcConfigResponseTypeDef",
    "ActionSummaryTypeDef",
    "AddAssociationResponseTypeDef",
    "AssociateTrialComponentResponseTypeDef",
    "CreateActionResponseTypeDef",
    "CreateAlgorithmOutputTypeDef",
    "CreateAppImageConfigResponseTypeDef",
    "CreateAppResponseTypeDef",
    "CreateArtifactResponseTypeDef",
    "CreateAutoMLJobResponseTypeDef",
    "CreateAutoMLJobV2ResponseTypeDef",
    "CreateCodeRepositoryOutputTypeDef",
    "CreateCompilationJobResponseTypeDef",
    "CreateContextResponseTypeDef",
    "CreateDataQualityJobDefinitionResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateEdgeDeploymentPlanResponseTypeDef",
    "CreateEndpointConfigOutputTypeDef",
    "CreateEndpointOutputTypeDef",
    "CreateExperimentResponseTypeDef",
    "CreateFeatureGroupResponseTypeDef",
    "CreateFlowDefinitionResponseTypeDef",
    "CreateHubResponseTypeDef",
    "CreateHumanTaskUiResponseTypeDef",
    "CreateHyperParameterTuningJobResponseTypeDef",
    "CreateImageResponseTypeDef",
    "CreateImageVersionResponseTypeDef",
    "CreateInferenceExperimentResponseTypeDef",
    "CreateInferenceRecommendationsJobResponseTypeDef",
    "CreateLabelingJobResponseTypeDef",
    "CreateModelBiasJobDefinitionResponseTypeDef",
    "CreateModelCardExportJobResponseTypeDef",
    "CreateModelCardResponseTypeDef",
    "CreateModelExplainabilityJobDefinitionResponseTypeDef",
    "CreateModelOutputTypeDef",
    "CreateModelPackageGroupOutputTypeDef",
    "CreateModelPackageOutputTypeDef",
    "CreateModelQualityJobDefinitionResponseTypeDef",
    "CreateMonitoringScheduleResponseTypeDef",
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    "CreateNotebookInstanceOutputTypeDef",
    "CreatePipelineResponseTypeDef",
    "CreatePresignedDomainUrlResponseTypeDef",
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    "CreateProcessingJobResponseTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateSpaceResponseTypeDef",
    "CreateStudioLifecycleConfigResponseTypeDef",
    "CreateTrainingJobResponseTypeDef",
    "CreateTransformJobResponseTypeDef",
    "CreateTrialComponentResponseTypeDef",
    "CreateTrialResponseTypeDef",
    "CreateUserProfileResponseTypeDef",
    "CreateWorkforceResponseTypeDef",
    "CreateWorkteamResponseTypeDef",
    "DeleteActionResponseTypeDef",
    "DeleteArtifactResponseTypeDef",
    "DeleteAssociationResponseTypeDef",
    "DeleteContextResponseTypeDef",
    "DeleteExperimentResponseTypeDef",
    "DeleteInferenceExperimentResponseTypeDef",
    "DeletePipelineResponseTypeDef",
    "DeleteTrialComponentResponseTypeDef",
    "DeleteTrialResponseTypeDef",
    "DeleteWorkteamResponseTypeDef",
    "DescribeImageResponseTypeDef",
    "DescribeImageVersionResponseTypeDef",
    "DescribePipelineDefinitionForExecutionResponseTypeDef",
    "DescribeStudioLifecycleConfigResponseTypeDef",
    "DisassociateTrialComponentResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetLineageGroupPolicyResponseTypeDef",
    "GetModelPackageGroupPolicyOutputTypeDef",
    "GetSagemakerServicecatalogPortfolioStatusOutputTypeDef",
    "ImportHubContentResponseTypeDef",
    "ListAliasesResponseTypeDef",
    "PutModelPackageGroupPolicyOutputTypeDef",
    "RetryPipelineExecutionResponseTypeDef",
    "SendPipelineExecutionStepFailureResponseTypeDef",
    "SendPipelineExecutionStepSuccessResponseTypeDef",
    "StartInferenceExperimentResponseTypeDef",
    "StartPipelineExecutionResponseTypeDef",
    "StopInferenceExperimentResponseTypeDef",
    "StopPipelineExecutionResponseTypeDef",
    "UpdateActionResponseTypeDef",
    "UpdateAppImageConfigResponseTypeDef",
    "UpdateArtifactResponseTypeDef",
    "UpdateCodeRepositoryOutputTypeDef",
    "UpdateContextResponseTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateEndpointOutputTypeDef",
    "UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    "UpdateExperimentResponseTypeDef",
    "UpdateFeatureGroupResponseTypeDef",
    "UpdateHubResponseTypeDef",
    "UpdateImageResponseTypeDef",
    "UpdateImageVersionResponseTypeDef",
    "UpdateInferenceExperimentResponseTypeDef",
    "UpdateModelCardResponseTypeDef",
    "UpdateModelPackageOutputTypeDef",
    "UpdateMonitoringAlertResponseTypeDef",
    "UpdateMonitoringScheduleResponseTypeDef",
    "UpdatePipelineExecutionResponseTypeDef",
    "UpdatePipelineResponseTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateSpaceResponseTypeDef",
    "UpdateTrainingJobResponseTypeDef",
    "UpdateTrialComponentResponseTypeDef",
    "UpdateTrialResponseTypeDef",
    "UpdateUserProfileResponseTypeDef",
    "AddTagsInputRequestTypeDef",
    "CreateExperimentRequestRequestTypeDef",
    "CreateImageRequestRequestTypeDef",
    "CreateModelPackageGroupInputRequestTypeDef",
    "CreateStudioLifecycleConfigRequestRequestTypeDef",
    "ImportHubContentRequestRequestTypeDef",
    "AddTagsOutputTypeDef",
    "ListTagsOutputTypeDef",
    "AutoRollbackConfigOutputTypeDef",
    "AutoRollbackConfigTypeDef",
    "HyperParameterAlgorithmSpecificationOutputTypeDef",
    "HyperParameterAlgorithmSpecificationTypeDef",
    "AlgorithmStatusDetailsTypeDef",
    "ListAlgorithmsOutputTypeDef",
    "ListAppsResponseTypeDef",
    "ArtifactSourceOutputTypeDef",
    "ArtifactSourceTypeDef",
    "AsyncInferenceOutputConfigOutputTypeDef",
    "AsyncInferenceOutputConfigTypeDef",
    "AutoMLCandidateGenerationConfigOutputTypeDef",
    "CandidateGenerationConfigOutputTypeDef",
    "AutoMLCandidateGenerationConfigTypeDef",
    "CandidateGenerationConfigTypeDef",
    "AutoMLDataSourceOutputTypeDef",
    "AutoMLDataSourceTypeDef",
    "ImageClassificationJobConfigOutputTypeDef",
    "TextClassificationJobConfigOutputTypeDef",
    "ImageClassificationJobConfigTypeDef",
    "TextClassificationJobConfigTypeDef",
    "ResolvedAttributesTypeDef",
    "AutoMLJobSummaryTypeDef",
    "AutoMLProblemTypeResolvedAttributesTypeDef",
    "AutoMLSecurityConfigOutputTypeDef",
    "LabelingJobResourceConfigOutputTypeDef",
    "MonitoringNetworkConfigOutputTypeDef",
    "NetworkConfigOutputTypeDef",
    "AutoMLSecurityConfigTypeDef",
    "LabelingJobResourceConfigTypeDef",
    "MonitoringNetworkConfigTypeDef",
    "NetworkConfigTypeDef",
    "BiasOutputTypeDef",
    "DriftCheckModelDataQualityOutputTypeDef",
    "DriftCheckModelQualityOutputTypeDef",
    "ExplainabilityOutputTypeDef",
    "ModelDataQualityOutputTypeDef",
    "ModelQualityOutputTypeDef",
    "BiasTypeDef",
    "DriftCheckModelDataQualityTypeDef",
    "DriftCheckModelQualityTypeDef",
    "ExplainabilityTypeDef",
    "ModelDataQualityTypeDef",
    "ModelQualityTypeDef",
    "CallbackStepMetadataTypeDef",
    "LambdaStepMetadataTypeDef",
    "CandidatePropertiesTypeDef",
    "CanvasAppSettingsOutputTypeDef",
    "CanvasAppSettingsTypeDef",
    "RollingUpdatePolicyOutputTypeDef",
    "TrafficRoutingConfigOutputTypeDef",
    "RollingUpdatePolicyTypeDef",
    "TrafficRoutingConfigTypeDef",
    "InferenceExperimentDataStorageConfigOutputTypeDef",
    "InferenceExperimentDataStorageConfigTypeDef",
    "DataCaptureConfigOutputTypeDef",
    "DataCaptureConfigTypeDef",
    "EnvironmentParameterRangesOutputTypeDef",
    "EnvironmentParameterRangesTypeDef",
    "ClarifyShapConfigOutputTypeDef",
    "ClarifyShapConfigTypeDef",
    "CodeRepositorySummaryTypeDef",
    "DescribeCodeRepositoryOutputTypeDef",
    "DebugHookConfigOutputTypeDef",
    "DebugHookConfigTypeDef",
    "ListCompilationJobsResponseTypeDef",
    "ContextSummaryTypeDef",
    "CreateContextRequestRequestTypeDef",
    "TuningJobCompletionCriteriaOutputTypeDef",
    "TuningJobCompletionCriteriaTypeDef",
    "CreateActionRequestRequestTypeDef",
    "CreateTrialRequestRequestTypeDef",
    "CreateAppRequestRequestTypeDef",
    "JupyterServerAppSettingsTypeDef",
    "RStudioServerProDomainSettingsForUpdateTypeDef",
    "RStudioServerProDomainSettingsTypeDef",
    "TensorBoardAppSettingsTypeDef",
    "CreateCodeRepositoryInputRequestTypeDef",
    "CreateDeviceFleetRequestRequestTypeDef",
    "CreateEdgePackagingJobRequestRequestTypeDef",
    "UpdateDeviceFleetRequestRequestTypeDef",
    "CreateHubRequestRequestTypeDef",
    "CreateHumanTaskUiRequestRequestTypeDef",
    "CreateModelCardExportJobRequestRequestTypeDef",
    "CreateModelCardRequestRequestTypeDef",
    "CreateNotebookInstanceInputRequestTypeDef",
    "UpdateNotebookInstanceInputRequestTypeDef",
    "CreateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "RetryPipelineExecutionRequestRequestTypeDef",
    "UpdatePipelineExecutionRequestRequestTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "CreateTrialComponentRequestRequestTypeDef",
    "UpdateTrialComponentRequestRequestTypeDef",
    "CreateWorkforceRequestRequestTypeDef",
    "UpdateWorkforceRequestRequestTypeDef",
    "KernelGatewayAppSettingsTypeDef",
    "RSessionAppSettingsTypeDef",
    "ModelBiasBaselineConfigOutputTypeDef",
    "ModelExplainabilityBaselineConfigOutputTypeDef",
    "ModelQualityBaselineConfigOutputTypeDef",
    "DataQualityBaselineConfigOutputTypeDef",
    "MonitoringBaselineConfigOutputTypeDef",
    "ModelBiasBaselineConfigTypeDef",
    "ModelExplainabilityBaselineConfigTypeDef",
    "ModelQualityBaselineConfigTypeDef",
    "DataQualityBaselineConfigTypeDef",
    "MonitoringBaselineConfigTypeDef",
    "DataSourceOutputTypeDef",
    "DataSourceTypeDef",
    "DatasetDefinitionOutputTypeDef",
    "DatasetDefinitionTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeploymentRecommendationTypeDef",
    "DeploymentStageStatusSummaryTypeDef",
    "DeploymentStageTypeDef",
    "DescribeAppResponseTypeDef",
    "JupyterServerAppSettingsOutputTypeDef",
    "KernelGatewayAppSettingsOutputTypeDef",
    "RSessionAppSettingsOutputTypeDef",
    "RStudioServerProDomainSettingsOutputTypeDef",
    "TensorBoardAppSettingsOutputTypeDef",
    "DescribeDeviceFleetResponseTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeEdgePackagingJobResponseTypeDef",
    "DescribeEndpointInputEndpointDeletedWaitTypeDef",
    "DescribeEndpointInputEndpointInServiceWaitTypeDef",
    "DescribeImageRequestImageCreatedWaitTypeDef",
    "DescribeImageRequestImageDeletedWaitTypeDef",
    "DescribeImageRequestImageUpdatedWaitTypeDef",
    "DescribeImageVersionRequestImageVersionCreatedWaitTypeDef",
    "DescribeImageVersionRequestImageVersionDeletedWaitTypeDef",
    "DescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef",
    "DescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef",
    "DescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef",
    "DescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef",
    "DescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef",
    "DescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef",
    "ExperimentSummaryTypeDef",
    "FeatureGroupSummaryTypeDef",
    "DescribeFeatureMetadataResponseTypeDef",
    "FeatureMetadataTypeDef",
    "DescribeHubContentResponseTypeDef",
    "DescribeHubResponseTypeDef",
    "DescribeHumanTaskUiResponseTypeDef",
    "InferenceExperimentSummaryTypeDef",
    "DescribeModelCardExportJobResponseTypeDef",
    "ListMonitoringExecutionsResponseTypeDef",
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    "DescribeNotebookInstanceOutputTypeDef",
    "DescribeSubscribedWorkteamResponseTypeDef",
    "ListSubscribedWorkteamsResponseTypeDef",
    "TrainingJobSummaryTypeDef",
    "TrialSummaryTypeDef",
    "DesiredWeightAndCapacityTypeDef",
    "ListStageDevicesResponseTypeDef",
    "ListDeviceFleetsResponseTypeDef",
    "DeviceSummaryTypeDef",
    "RegisterDevicesRequestRequestTypeDef",
    "UpdateDevicesRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "DriftCheckBiasOutputTypeDef",
    "DriftCheckExplainabilityOutputTypeDef",
    "DriftCheckBiasTypeDef",
    "DriftCheckExplainabilityTypeDef",
    "ListEdgeDeploymentPlansResponseTypeDef",
    "GetDeviceFleetReportResponseTypeDef",
    "ListEdgePackagingJobsResponseTypeDef",
    "ListEndpointConfigsOutputTypeDef",
    "EndpointOutputConfigurationTypeDef",
    "EndpointPerformanceTypeDef",
    "ListEndpointsOutputTypeDef",
    "ModelConfigurationTypeDef",
    "UpdateFeatureMetadataRequestRequestTypeDef",
    "NestedFiltersTypeDef",
    "HyperParameterTrainingJobSummaryTypeDef",
    "ListFlowDefinitionsResponseTypeDef",
    "GetSearchSuggestionsResponseTypeDef",
    "UpdateCodeRepositoryInputRequestTypeDef",
    "ListHubContentVersionsResponseTypeDef",
    "ListHubContentsResponseTypeDef",
    "ListHubsResponseTypeDef",
    "HumanLoopActivationConfigOutputTypeDef",
    "HumanLoopActivationConfigTypeDef",
    "ListHumanTaskUisResponseTypeDef",
    "HyperParameterTuningResourceConfigOutputTypeDef",
    "HyperParameterTuningResourceConfigTypeDef",
    "HyperParameterTuningJobSummaryTypeDef",
    "HyperParameterTuningJobStrategyConfigOutputTypeDef",
    "HyperParameterTuningJobStrategyConfigTypeDef",
    "HyperParameterTuningJobWarmStartConfigOutputTypeDef",
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    "UserContextTypeDef",
    "ImageConfigOutputTypeDef",
    "ImageConfigTypeDef",
    "ListImagesResponseTypeDef",
    "ListImageVersionsResponseTypeDef",
    "ListInferenceRecommendationsJobsResponseTypeDef",
    "ResourceConfigOutputTypeDef",
    "ResourceConfigTypeDef",
    "ParameterRangesOutputTypeDef",
    "ParameterRangeOutputTypeDef",
    "ParameterRangeTypeDef",
    "ParameterRangesTypeDef",
    "KernelGatewayImageConfigOutputTypeDef",
    "KernelGatewayImageConfigTypeDef",
    "LabelingJobForWorkteamSummaryTypeDef",
    "LabelingJobDataSourceOutputTypeDef",
    "LabelingJobDataSourceTypeDef",
    "ListLineageGroupsResponseTypeDef",
    "ListActionsRequestListActionsPaginateTypeDef",
    "ListAlgorithmsInputListAlgorithmsPaginateTypeDef",
    "ListAliasesRequestListAliasesPaginateTypeDef",
    "ListAppImageConfigsRequestListAppImageConfigsPaginateTypeDef",
    "ListAppsRequestListAppsPaginateTypeDef",
    "ListArtifactsRequestListArtifactsPaginateTypeDef",
    "ListAssociationsRequestListAssociationsPaginateTypeDef",
    "ListAutoMLJobsRequestListAutoMLJobsPaginateTypeDef",
    "ListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef",
    "ListCodeRepositoriesInputListCodeRepositoriesPaginateTypeDef",
    "ListCompilationJobsRequestListCompilationJobsPaginateTypeDef",
    "ListContextsRequestListContextsPaginateTypeDef",
    "ListDataQualityJobDefinitionsRequestListDataQualityJobDefinitionsPaginateTypeDef",
    "ListDeviceFleetsRequestListDeviceFleetsPaginateTypeDef",
    "ListDevicesRequestListDevicesPaginateTypeDef",
    "ListDomainsRequestListDomainsPaginateTypeDef",
    "ListEdgeDeploymentPlansRequestListEdgeDeploymentPlansPaginateTypeDef",
    "ListEdgePackagingJobsRequestListEdgePackagingJobsPaginateTypeDef",
    "ListEndpointConfigsInputListEndpointConfigsPaginateTypeDef",
    "ListEndpointsInputListEndpointsPaginateTypeDef",
    "ListExperimentsRequestListExperimentsPaginateTypeDef",
    "ListFeatureGroupsRequestListFeatureGroupsPaginateTypeDef",
    "ListFlowDefinitionsRequestListFlowDefinitionsPaginateTypeDef",
    "ListHumanTaskUisRequestListHumanTaskUisPaginateTypeDef",
    "ListHyperParameterTuningJobsRequestListHyperParameterTuningJobsPaginateTypeDef",
    "ListImageVersionsRequestListImageVersionsPaginateTypeDef",
    "ListImagesRequestListImagesPaginateTypeDef",
    "ListInferenceExperimentsRequestListInferenceExperimentsPaginateTypeDef",
    "ListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef",
    "ListInferenceRecommendationsJobsRequestListInferenceRecommendationsJobsPaginateTypeDef",
    "ListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef",
    "ListLabelingJobsRequestListLabelingJobsPaginateTypeDef",
    "ListLineageGroupsRequestListLineageGroupsPaginateTypeDef",
    "ListModelBiasJobDefinitionsRequestListModelBiasJobDefinitionsPaginateTypeDef",
    "ListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef",
    "ListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef",
    "ListModelCardsRequestListModelCardsPaginateTypeDef",
    "ListModelExplainabilityJobDefinitionsRequestListModelExplainabilityJobDefinitionsPaginateTypeDef",
    "ListModelPackageGroupsInputListModelPackageGroupsPaginateTypeDef",
    "ListModelPackagesInputListModelPackagesPaginateTypeDef",
    "ListModelQualityJobDefinitionsRequestListModelQualityJobDefinitionsPaginateTypeDef",
    "ListModelsInputListModelsPaginateTypeDef",
    "ListMonitoringAlertHistoryRequestListMonitoringAlertHistoryPaginateTypeDef",
    "ListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef",
    "ListMonitoringExecutionsRequestListMonitoringExecutionsPaginateTypeDef",
    "ListMonitoringSchedulesRequestListMonitoringSchedulesPaginateTypeDef",
    "ListNotebookInstanceLifecycleConfigsInputListNotebookInstanceLifecycleConfigsPaginateTypeDef",
    "ListNotebookInstancesInputListNotebookInstancesPaginateTypeDef",
    "ListPipelineExecutionStepsRequestListPipelineExecutionStepsPaginateTypeDef",
    "ListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef",
    "ListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef",
    "ListPipelinesRequestListPipelinesPaginateTypeDef",
    "ListProcessingJobsRequestListProcessingJobsPaginateTypeDef",
    "ListResourceCatalogsRequestListResourceCatalogsPaginateTypeDef",
    "ListSpacesRequestListSpacesPaginateTypeDef",
    "ListStageDevicesRequestListStageDevicesPaginateTypeDef",
    "ListStudioLifecycleConfigsRequestListStudioLifecycleConfigsPaginateTypeDef",
    "ListSubscribedWorkteamsRequestListSubscribedWorkteamsPaginateTypeDef",
    "ListTagsInputListTagsPaginateTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef",
    "ListTrainingJobsRequestListTrainingJobsPaginateTypeDef",
    "ListTransformJobsRequestListTransformJobsPaginateTypeDef",
    "ListTrialComponentsRequestListTrialComponentsPaginateTypeDef",
    "ListTrialsRequestListTrialsPaginateTypeDef",
    "ListUserProfilesRequestListUserProfilesPaginateTypeDef",
    "ListWorkforcesRequestListWorkforcesPaginateTypeDef",
    "ListWorkteamsRequestListWorkteamsPaginateTypeDef",
    "SearchRequestSearchPaginateTypeDef",
    "ListDataQualityJobDefinitionsResponseTypeDef",
    "ListModelBiasJobDefinitionsResponseTypeDef",
    "ListModelExplainabilityJobDefinitionsResponseTypeDef",
    "ListModelQualityJobDefinitionsResponseTypeDef",
    "ListModelCardExportJobsResponseTypeDef",
    "ListModelCardVersionsResponseTypeDef",
    "ListModelCardsResponseTypeDef",
    "ListModelMetadataResponseTypeDef",
    "ListModelPackageGroupsOutputTypeDef",
    "ListModelPackagesOutputTypeDef",
    "ListModelsOutputTypeDef",
    "ListMonitoringAlertHistoryResponseTypeDef",
    "ListMonitoringSchedulesResponseTypeDef",
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    "ListNotebookInstancesOutputTypeDef",
    "ListPipelineExecutionsResponseTypeDef",
    "ListPipelineParametersForExecutionResponseTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListProcessingJobsResponseTypeDef",
    "ListProjectsOutputTypeDef",
    "ListResourceCatalogsResponseTypeDef",
    "ListSpacesResponseTypeDef",
    "ListStudioLifecycleConfigsResponseTypeDef",
    "ListTransformJobsResponseTypeDef",
    "ListUserProfilesResponseTypeDef",
    "MemberDefinitionOutputTypeDef",
    "MemberDefinitionTypeDef",
    "MonitoringAlertActionsTypeDef",
    "ModelDataSourceOutputTypeDef",
    "ModelDataSourceTypeDef",
    "ModelInfrastructureConfigOutputTypeDef",
    "ModelInfrastructureConfigTypeDef",
    "ModelPackageContainerDefinitionOutputTypeDef",
    "ModelPackageContainerDefinitionTypeDef",
    "RecommendationJobStoppingConditionsOutputTypeDef",
    "RecommendationJobStoppingConditionsTypeDef",
    "ModelMetadataSearchExpressionTypeDef",
    "ModelPackageStatusDetailsTypeDef",
    "MonitoringResourcesOutputTypeDef",
    "MonitoringResourcesTypeDef",
    "MonitoringDatasetFormatOutputTypeDef",
    "MonitoringDatasetFormatTypeDef",
    "MonitoringOutputTypeDef",
    "OfflineStoreConfigOutputTypeDef",
    "OfflineStoreConfigTypeDef",
    "OnlineStoreConfigOutputTypeDef",
    "OnlineStoreConfigTypeDef",
    "OnlineStoreConfigUpdateTypeDef",
    "OutputConfigOutputTypeDef",
    "OutputConfigTypeDef",
    "SendPipelineExecutionStepSuccessRequestRequestTypeDef",
    "PendingProductionVariantSummaryTypeDef",
    "ProductionVariantSummaryTypeDef",
    "TrafficPatternOutputTypeDef",
    "TrafficPatternTypeDef",
    "ProcessingResourcesOutputTypeDef",
    "ProcessingResourcesTypeDef",
    "ProcessingOutputTypeDef",
    "ProductionVariantOutputTypeDef",
    "ProductionVariantTypeDef",
    "SuggestionQueryTypeDef",
    "ServiceCatalogProvisioningDetailsOutputTypeDef",
    "ServiceCatalogProvisioningDetailsTypeDef",
    "ServiceCatalogProvisioningUpdateDetailsTypeDef",
    "PublicWorkforceTaskPriceOutputTypeDef",
    "PublicWorkforceTaskPriceTypeDef",
    "QueryLineageRequestRequestTypeDef",
    "QueryLineageResponseTypeDef",
    "RecommendationJobOutputConfigTypeDef",
    "RecommendationJobContainerConfigOutputTypeDef",
    "RecommendationJobContainerConfigTypeDef",
    "RenderUiTemplateRequestRequestTypeDef",
    "RenderUiTemplateResponseTypeDef",
    "UpdateTrainingJobRequestRequestTypeDef",
    "SelectiveExecutionConfigOutputTypeDef",
    "SelectiveExecutionConfigTypeDef",
    "ShadowModeConfigOutputTypeDef",
    "ShadowModeConfigTypeDef",
    "SourceAlgorithmSpecificationOutputTypeDef",
    "SourceAlgorithmSpecificationTypeDef",
    "TimeSeriesForecastingJobConfigOutputTypeDef",
    "TimeSeriesForecastingJobConfigTypeDef",
    "TrainingImageConfigOutputTypeDef",
    "TrainingImageConfigTypeDef",
    "TransformDataSourceOutputTypeDef",
    "TransformDataSourceTypeDef",
    "WorkforceTypeDef",
    "ListActionsResponseTypeDef",
    "ArtifactSummaryTypeDef",
    "CreateArtifactRequestRequestTypeDef",
    "DeleteArtifactRequestRequestTypeDef",
    "AsyncInferenceConfigOutputTypeDef",
    "AsyncInferenceConfigTypeDef",
    "TabularJobConfigOutputTypeDef",
    "TabularJobConfigTypeDef",
    "AutoMLChannelOutputTypeDef",
    "AutoMLJobChannelOutputTypeDef",
    "AutoMLChannelTypeDef",
    "AutoMLJobChannelTypeDef",
    "ListAutoMLJobsResponseTypeDef",
    "AutoMLResolvedAttributesTypeDef",
    "AutoMLJobConfigOutputTypeDef",
    "LabelingJobAlgorithmsConfigOutputTypeDef",
    "AutoMLJobConfigTypeDef",
    "LabelingJobAlgorithmsConfigTypeDef",
    "ModelMetricsOutputTypeDef",
    "ModelMetricsTypeDef",
    "PipelineExecutionStepMetadataTypeDef",
    "AutoMLCandidateTypeDef",
    "BlueGreenUpdatePolicyOutputTypeDef",
    "BlueGreenUpdatePolicyTypeDef",
    "EndpointInputConfigurationOutputTypeDef",
    "EndpointInputConfigurationTypeDef",
    "ClarifyExplainerConfigOutputTypeDef",
    "ClarifyExplainerConfigTypeDef",
    "ListCodeRepositoriesOutputTypeDef",
    "ListContextsResponseTypeDef",
    "DomainSettingsForUpdateTypeDef",
    "DomainSettingsTypeDef",
    "DefaultSpaceSettingsTypeDef",
    "SpaceSettingsTypeDef",
    "UserSettingsTypeDef",
    "ChannelOutputTypeDef",
    "ChannelTypeDef",
    "ProcessingInputOutputTypeDef",
    "ProcessingInputTypeDef",
    "DescribeEdgeDeploymentPlanResponseTypeDef",
    "CreateEdgeDeploymentPlanRequestRequestTypeDef",
    "CreateEdgeDeploymentStageRequestRequestTypeDef",
    "DefaultSpaceSettingsOutputTypeDef",
    "SpaceSettingsOutputTypeDef",
    "DomainSettingsOutputTypeDef",
    "UserSettingsOutputTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListFeatureGroupsResponseTypeDef",
    "ListInferenceExperimentsResponseTypeDef",
    "ListTrainingJobsResponseTypeDef",
    "ListTrialsResponseTypeDef",
    "UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "DriftCheckBaselinesOutputTypeDef",
    "DriftCheckBaselinesTypeDef",
    "InferenceRecommendationTypeDef",
    "RecommendationJobInferenceBenchmarkTypeDef",
    "SearchExpressionTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    "ListHyperParameterTuningJobsResponseTypeDef",
    "AssociationSummaryTypeDef",
    "DescribeActionResponseTypeDef",
    "DescribeArtifactResponseTypeDef",
    "DescribeContextResponseTypeDef",
    "DescribeExperimentResponseTypeDef",
    "DescribeLineageGroupResponseTypeDef",
    "DescribeModelCardResponseTypeDef",
    "DescribeModelPackageGroupOutputTypeDef",
    "DescribePipelineResponseTypeDef",
    "DescribeTrialComponentResponseTypeDef",
    "DescribeTrialResponseTypeDef",
    "ExperimentTypeDef",
    "ModelCardTypeDef",
    "ModelDashboardModelCardTypeDef",
    "ModelPackageGroupTypeDef",
    "PipelineTypeDef",
    "TrialComponentSimpleSummaryTypeDef",
    "TrialComponentSummaryTypeDef",
    "HyperParameterTuningJobConfigOutputTypeDef",
    "HyperParameterSpecificationOutputTypeDef",
    "HyperParameterSpecificationTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "AppImageConfigDetailsTypeDef",
    "DescribeAppImageConfigResponseTypeDef",
    "CreateAppImageConfigRequestRequestTypeDef",
    "UpdateAppImageConfigRequestRequestTypeDef",
    "ListLabelingJobsForWorkteamResponseTypeDef",
    "LabelingJobInputConfigOutputTypeDef",
    "LabelingJobInputConfigTypeDef",
    "WorkteamTypeDef",
    "CreateWorkteamRequestRequestTypeDef",
    "UpdateWorkteamRequestRequestTypeDef",
    "MonitoringAlertSummaryTypeDef",
    "ContainerDefinitionOutputTypeDef",
    "ContainerDefinitionTypeDef",
    "ModelVariantConfigSummaryTypeDef",
    "ModelVariantConfigTypeDef",
    "AdditionalInferenceSpecificationDefinitionOutputTypeDef",
    "InferenceSpecificationOutputTypeDef",
    "AdditionalInferenceSpecificationDefinitionTypeDef",
    "InferenceSpecificationTypeDef",
    "ListModelMetadataRequestListModelMetadataPaginateTypeDef",
    "ListModelMetadataRequestRequestTypeDef",
    "BatchTransformInputOutputTypeDef",
    "BatchTransformInputTypeDef",
    "MonitoringOutputConfigOutputTypeDef",
    "MonitoringOutputConfigTypeDef",
    "DescribeFeatureGroupResponseTypeDef",
    "FeatureGroupTypeDef",
    "CreateFeatureGroupRequestRequestTypeDef",
    "UpdateFeatureGroupRequestRequestTypeDef",
    "DescribeCompilationJobResponseTypeDef",
    "CreateCompilationJobRequestRequestTypeDef",
    "PendingDeploymentSummaryTypeDef",
    "ProcessingOutputConfigOutputTypeDef",
    "ProcessingOutputConfigTypeDef",
    "GetSearchSuggestionsRequestRequestTypeDef",
    "DescribeProjectOutputTypeDef",
    "ProjectTypeDef",
    "CreateProjectInputRequestTypeDef",
    "UpdateProjectInputRequestTypeDef",
    "HumanLoopConfigOutputTypeDef",
    "HumanTaskConfigOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanTaskConfigTypeDef",
    "DescribePipelineExecutionResponseTypeDef",
    "PipelineExecutionTypeDef",
    "StartPipelineExecutionRequestRequestTypeDef",
    "AlgorithmSpecificationOutputTypeDef",
    "AlgorithmSpecificationTypeDef",
    "TransformInputOutputTypeDef",
    "TransformInputTypeDef",
    "DescribeWorkforceResponseTypeDef",
    "ListWorkforcesResponseTypeDef",
    "UpdateWorkforceResponseTypeDef",
    "ListArtifactsResponseTypeDef",
    "AutoMLProblemTypeConfigOutputTypeDef",
    "AutoMLProblemTypeConfigTypeDef",
    "CreateAutoMLJobRequestRequestTypeDef",
    "PipelineExecutionStepTypeDef",
    "DescribeAutoMLJobResponseTypeDef",
    "ListCandidatesForAutoMLJobResponseTypeDef",
    "DeploymentConfigOutputTypeDef",
    "DeploymentConfigTypeDef",
    "RecommendationJobInputConfigOutputTypeDef",
    "RecommendationJobInputConfigTypeDef",
    "ExplainerConfigOutputTypeDef",
    "ExplainerConfigTypeDef",
    "CreateSpaceRequestRequestTypeDef",
    "UpdateSpaceRequestRequestTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateUserProfileRequestRequestTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "UpdateUserProfileRequestRequestTypeDef",
    "HyperParameterTrainingJobDefinitionOutputTypeDef",
    "TrainingJobDefinitionOutputTypeDef",
    "HyperParameterTrainingJobDefinitionTypeDef",
    "TrainingJobDefinitionTypeDef",
    "DescribeSpaceResponseTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeUserProfileResponseTypeDef",
    "InferenceRecommendationsJobStepTypeDef",
    "ListAssociationsResponseTypeDef",
    "TrialTypeDef",
    "ListTrialComponentsResponseTypeDef",
    "TrainingSpecificationOutputTypeDef",
    "TrainingSpecificationTypeDef",
    "ListAppImageConfigsResponseTypeDef",
    "LabelingJobSummaryTypeDef",
    "DescribeWorkteamResponseTypeDef",
    "ListWorkteamsResponseTypeDef",
    "UpdateWorkteamResponseTypeDef",
    "ListMonitoringAlertsResponseTypeDef",
    "DescribeModelOutputTypeDef",
    "ModelTypeDef",
    "CreateModelInputRequestTypeDef",
    "DescribeInferenceExperimentResponseTypeDef",
    "CreateInferenceExperimentRequestRequestTypeDef",
    "StopInferenceExperimentRequestRequestTypeDef",
    "UpdateInferenceExperimentRequestRequestTypeDef",
    "BatchDescribeModelPackageSummaryTypeDef",
    "UpdateModelPackageInputRequestTypeDef",
    "DataQualityJobInputOutputTypeDef",
    "ModelBiasJobInputOutputTypeDef",
    "ModelExplainabilityJobInputOutputTypeDef",
    "ModelQualityJobInputOutputTypeDef",
    "MonitoringInputOutputTypeDef",
    "DataQualityJobInputTypeDef",
    "ModelBiasJobInputTypeDef",
    "ModelExplainabilityJobInputTypeDef",
    "ModelQualityJobInputTypeDef",
    "MonitoringInputTypeDef",
    "DescribeProcessingJobResponseTypeDef",
    "ProcessingJobTypeDef",
    "CreateProcessingJobRequestRequestTypeDef",
    "DescribeFlowDefinitionResponseTypeDef",
    "DescribeLabelingJobResponseTypeDef",
    "CreateFlowDefinitionRequestRequestTypeDef",
    "CreateLabelingJobRequestRequestTypeDef",
    "DescribeTrainingJobResponseTypeDef",
    "TrainingJobTypeDef",
    "CreateTrainingJobRequestRequestTypeDef",
    "DescribeTransformJobResponseTypeDef",
    "TransformJobDefinitionOutputTypeDef",
    "TransformJobTypeDef",
    "CreateTransformJobRequestRequestTypeDef",
    "TransformJobDefinitionTypeDef",
    "DescribeAutoMLJobV2ResponseTypeDef",
    "CreateAutoMLJobV2RequestRequestTypeDef",
    "ListPipelineExecutionStepsResponseTypeDef",
    "CreateEndpointInputRequestTypeDef",
    "UpdateEndpointInputRequestTypeDef",
    "DescribeInferenceRecommendationsJobResponseTypeDef",
    "CreateInferenceRecommendationsJobRequestRequestTypeDef",
    "DescribeEndpointConfigOutputTypeDef",
    "DescribeEndpointOutputTypeDef",
    "CreateEndpointConfigInputRequestTypeDef",
    "DescribeHyperParameterTuningJobResponseTypeDef",
    "HyperParameterTuningJobSearchEntityTypeDef",
    "CreateHyperParameterTuningJobRequestRequestTypeDef",
    "ListInferenceRecommendationsJobStepsResponseTypeDef",
    "ListLabelingJobsResponseTypeDef",
    "BatchDescribeModelPackageOutputTypeDef",
    "DescribeDataQualityJobDefinitionResponseTypeDef",
    "DescribeModelBiasJobDefinitionResponseTypeDef",
    "DescribeModelExplainabilityJobDefinitionResponseTypeDef",
    "DescribeModelQualityJobDefinitionResponseTypeDef",
    "MonitoringJobDefinitionOutputTypeDef",
    "CreateDataQualityJobDefinitionRequestRequestTypeDef",
    "CreateModelBiasJobDefinitionRequestRequestTypeDef",
    "CreateModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "CreateModelQualityJobDefinitionRequestRequestTypeDef",
    "MonitoringJobDefinitionTypeDef",
    "AlgorithmValidationProfileOutputTypeDef",
    "ModelPackageValidationProfileOutputTypeDef",
    "TrialComponentSourceDetailTypeDef",
    "AlgorithmValidationProfileTypeDef",
    "ModelPackageValidationProfileTypeDef",
    "MonitoringScheduleConfigOutputTypeDef",
    "MonitoringScheduleConfigTypeDef",
    "AlgorithmValidationSpecificationOutputTypeDef",
    "ModelPackageValidationSpecificationOutputTypeDef",
    "TrialComponentTypeDef",
    "AlgorithmValidationSpecificationTypeDef",
    "ModelPackageValidationSpecificationTypeDef",
    "DescribeMonitoringScheduleResponseTypeDef",
    "ModelDashboardMonitoringScheduleTypeDef",
    "MonitoringScheduleTypeDef",
    "CreateMonitoringScheduleRequestRequestTypeDef",
    "UpdateMonitoringScheduleRequestRequestTypeDef",
    "DescribeAlgorithmOutputTypeDef",
    "DescribeModelPackageOutputTypeDef",
    "ModelPackageTypeDef",
    "CreateAlgorithmInputRequestTypeDef",
    "CreateModelPackageInputRequestTypeDef",
    "ModelDashboardModelTypeDef",
    "EndpointTypeDef",
    "SearchRecordTypeDef",
    "SearchResponseTypeDef",
)

_RequiredActionSourceOutputTypeDef = TypedDict(
    "_RequiredActionSourceOutputTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalActionSourceOutputTypeDef = TypedDict(
    "_OptionalActionSourceOutputTypeDef",
    {
        "SourceType": str,
        "SourceId": str,
    },
    total=False,
)


class ActionSourceOutputTypeDef(
    _RequiredActionSourceOutputTypeDef, _OptionalActionSourceOutputTypeDef
):
    pass


_RequiredActionSourceTypeDef = TypedDict(
    "_RequiredActionSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalActionSourceTypeDef = TypedDict(
    "_OptionalActionSourceTypeDef",
    {
        "SourceType": str,
        "SourceId": str,
    },
    total=False,
)


class ActionSourceTypeDef(_RequiredActionSourceTypeDef, _OptionalActionSourceTypeDef):
    pass


_RequiredAddAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredAddAssociationRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
    },
)
_OptionalAddAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalAddAssociationRequestRequestTypeDef",
    {
        "AssociationType": AssociationEdgeTypeType,
    },
    total=False,
)


class AddAssociationRequestRequestTypeDef(
    _RequiredAddAssociationRequestRequestTypeDef, _OptionalAddAssociationRequestRequestTypeDef
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {
        "Version": str,
        "AgentCount": int,
    },
)

AlarmOutputTypeDef = TypedDict(
    "AlarmOutputTypeDef",
    {
        "AlarmName": str,
    },
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
    },
    total=False,
)

MetricDefinitionOutputTypeDef = TypedDict(
    "MetricDefinitionOutputTypeDef",
    {
        "Name": str,
        "Regex": str,
    },
)

MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "Name": str,
        "Regex": str,
    },
)

_RequiredAlgorithmStatusItemTypeDef = TypedDict(
    "_RequiredAlgorithmStatusItemTypeDef",
    {
        "Name": str,
        "Status": DetailedAlgorithmStatusType,
    },
)
_OptionalAlgorithmStatusItemTypeDef = TypedDict(
    "_OptionalAlgorithmStatusItemTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class AlgorithmStatusItemTypeDef(
    _RequiredAlgorithmStatusItemTypeDef, _OptionalAlgorithmStatusItemTypeDef
):
    pass


_RequiredAlgorithmSummaryTypeDef = TypedDict(
    "_RequiredAlgorithmSummaryTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "CreationTime": datetime,
        "AlgorithmStatus": AlgorithmStatusType,
    },
)
_OptionalAlgorithmSummaryTypeDef = TypedDict(
    "_OptionalAlgorithmSummaryTypeDef",
    {
        "AlgorithmDescription": str,
    },
    total=False,
)


class AlgorithmSummaryTypeDef(_RequiredAlgorithmSummaryTypeDef, _OptionalAlgorithmSummaryTypeDef):
    pass


AnnotationConsolidationConfigOutputTypeDef = TypedDict(
    "AnnotationConsolidationConfigOutputTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
    },
)

AnnotationConsolidationConfigTypeDef = TypedDict(
    "AnnotationConsolidationConfigTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
    },
)

AppDetailsTypeDef = TypedDict(
    "AppDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
        "Status": AppStatusType,
        "CreationTime": datetime,
        "SpaceName": str,
    },
    total=False,
)

_RequiredAppSpecificationOutputTypeDef = TypedDict(
    "_RequiredAppSpecificationOutputTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalAppSpecificationOutputTypeDef = TypedDict(
    "_OptionalAppSpecificationOutputTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
    },
    total=False,
)


class AppSpecificationOutputTypeDef(
    _RequiredAppSpecificationOutputTypeDef, _OptionalAppSpecificationOutputTypeDef
):
    pass


_RequiredAppSpecificationTypeDef = TypedDict(
    "_RequiredAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalAppSpecificationTypeDef = TypedDict(
    "_OptionalAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": Sequence[str],
        "ContainerArguments": Sequence[str],
    },
    total=False,
)


class AppSpecificationTypeDef(_RequiredAppSpecificationTypeDef, _OptionalAppSpecificationTypeDef):
    pass


ArtifactSourceTypeOutputTypeDef = TypedDict(
    "ArtifactSourceTypeOutputTypeDef",
    {
        "SourceIdType": ArtifactSourceIdTypeType,
        "Value": str,
    },
)

ArtifactSourceTypeTypeDef = TypedDict(
    "ArtifactSourceTypeTypeDef",
    {
        "SourceIdType": ArtifactSourceIdTypeType,
        "Value": str,
    },
)

AssociateTrialComponentRequestRequestTypeDef = TypedDict(
    "AssociateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "TrialName": str,
    },
)

AsyncInferenceClientConfigOutputTypeDef = TypedDict(
    "AsyncInferenceClientConfigOutputTypeDef",
    {
        "MaxConcurrentInvocationsPerInstance": int,
    },
    total=False,
)

AsyncInferenceClientConfigTypeDef = TypedDict(
    "AsyncInferenceClientConfigTypeDef",
    {
        "MaxConcurrentInvocationsPerInstance": int,
    },
    total=False,
)

AsyncInferenceNotificationConfigOutputTypeDef = TypedDict(
    "AsyncInferenceNotificationConfigOutputTypeDef",
    {
        "SuccessTopic": str,
        "ErrorTopic": str,
        "IncludeInferenceResponseIn": List[AsyncNotificationTopicTypesType],
    },
    total=False,
)

AsyncInferenceNotificationConfigTypeDef = TypedDict(
    "AsyncInferenceNotificationConfigTypeDef",
    {
        "SuccessTopic": str,
        "ErrorTopic": str,
        "IncludeInferenceResponseIn": Sequence[AsyncNotificationTopicTypesType],
    },
    total=False,
)

_RequiredAthenaDatasetDefinitionOutputTypeDef = TypedDict(
    "_RequiredAthenaDatasetDefinitionOutputTypeDef",
    {
        "Catalog": str,
        "Database": str,
        "QueryString": str,
        "OutputS3Uri": str,
        "OutputFormat": AthenaResultFormatType,
    },
)
_OptionalAthenaDatasetDefinitionOutputTypeDef = TypedDict(
    "_OptionalAthenaDatasetDefinitionOutputTypeDef",
    {
        "WorkGroup": str,
        "KmsKeyId": str,
        "OutputCompression": AthenaResultCompressionTypeType,
    },
    total=False,
)


class AthenaDatasetDefinitionOutputTypeDef(
    _RequiredAthenaDatasetDefinitionOutputTypeDef, _OptionalAthenaDatasetDefinitionOutputTypeDef
):
    pass


_RequiredAthenaDatasetDefinitionTypeDef = TypedDict(
    "_RequiredAthenaDatasetDefinitionTypeDef",
    {
        "Catalog": str,
        "Database": str,
        "QueryString": str,
        "OutputS3Uri": str,
        "OutputFormat": AthenaResultFormatType,
    },
)
_OptionalAthenaDatasetDefinitionTypeDef = TypedDict(
    "_OptionalAthenaDatasetDefinitionTypeDef",
    {
        "WorkGroup": str,
        "KmsKeyId": str,
        "OutputCompression": AthenaResultCompressionTypeType,
    },
    total=False,
)


class AthenaDatasetDefinitionTypeDef(
    _RequiredAthenaDatasetDefinitionTypeDef, _OptionalAthenaDatasetDefinitionTypeDef
):
    pass


AutoMLAlgorithmConfigOutputTypeDef = TypedDict(
    "AutoMLAlgorithmConfigOutputTypeDef",
    {
        "AutoMLAlgorithms": List[AutoMLAlgorithmType],
    },
)

AutoMLAlgorithmConfigTypeDef = TypedDict(
    "AutoMLAlgorithmConfigTypeDef",
    {
        "AutoMLAlgorithms": Sequence[AutoMLAlgorithmType],
    },
)

AutoMLCandidateStepTypeDef = TypedDict(
    "AutoMLCandidateStepTypeDef",
    {
        "CandidateStepType": CandidateStepTypeType,
        "CandidateStepArn": str,
        "CandidateStepName": str,
    },
)

_RequiredAutoMLContainerDefinitionTypeDef = TypedDict(
    "_RequiredAutoMLContainerDefinitionTypeDef",
    {
        "Image": str,
        "ModelDataUrl": str,
    },
)
_OptionalAutoMLContainerDefinitionTypeDef = TypedDict(
    "_OptionalAutoMLContainerDefinitionTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)


class AutoMLContainerDefinitionTypeDef(
    _RequiredAutoMLContainerDefinitionTypeDef, _OptionalAutoMLContainerDefinitionTypeDef
):
    pass


_RequiredFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalAutoMLJobObjectiveMetricTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
        "Value": float,
    },
)
_OptionalFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalAutoMLJobObjectiveMetricTypeDef",
    {
        "Type": AutoMLJobObjectiveTypeType,
        "StandardMetricName": AutoMLMetricEnumType,
    },
    total=False,
)


class FinalAutoMLJobObjectiveMetricTypeDef(
    _RequiredFinalAutoMLJobObjectiveMetricTypeDef, _OptionalFinalAutoMLJobObjectiveMetricTypeDef
):
    pass


AutoMLS3DataSourceOutputTypeDef = TypedDict(
    "AutoMLS3DataSourceOutputTypeDef",
    {
        "S3DataType": AutoMLS3DataTypeType,
        "S3Uri": str,
    },
)

AutoMLS3DataSourceTypeDef = TypedDict(
    "AutoMLS3DataSourceTypeDef",
    {
        "S3DataType": AutoMLS3DataTypeType,
        "S3Uri": str,
    },
)

AutoMLDataSplitConfigOutputTypeDef = TypedDict(
    "AutoMLDataSplitConfigOutputTypeDef",
    {
        "ValidationFraction": float,
    },
    total=False,
)

AutoMLDataSplitConfigTypeDef = TypedDict(
    "AutoMLDataSplitConfigTypeDef",
    {
        "ValidationFraction": float,
    },
    total=False,
)

AutoMLJobArtifactsTypeDef = TypedDict(
    "AutoMLJobArtifactsTypeDef",
    {
        "CandidateDefinitionNotebookLocation": str,
        "DataExplorationNotebookLocation": str,
    },
    total=False,
)

AutoMLJobCompletionCriteriaOutputTypeDef = TypedDict(
    "AutoMLJobCompletionCriteriaOutputTypeDef",
    {
        "MaxCandidates": int,
        "MaxRuntimePerTrainingJobInSeconds": int,
        "MaxAutoMLJobRuntimeInSeconds": int,
    },
    total=False,
)

AutoMLJobCompletionCriteriaTypeDef = TypedDict(
    "AutoMLJobCompletionCriteriaTypeDef",
    {
        "MaxCandidates": int,
        "MaxRuntimePerTrainingJobInSeconds": int,
        "MaxAutoMLJobRuntimeInSeconds": int,
    },
    total=False,
)

AutoMLJobObjectiveOutputTypeDef = TypedDict(
    "AutoMLJobObjectiveOutputTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
    },
)

AutoMLJobObjectiveTypeDef = TypedDict(
    "AutoMLJobObjectiveTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
    },
)

AutoMLJobStepMetadataTypeDef = TypedDict(
    "AutoMLJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

AutoMLPartialFailureReasonTypeDef = TypedDict(
    "AutoMLPartialFailureReasonTypeDef",
    {
        "PartialFailureMessage": str,
    },
    total=False,
)

_RequiredAutoMLOutputDataConfigOutputTypeDef = TypedDict(
    "_RequiredAutoMLOutputDataConfigOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalAutoMLOutputDataConfigOutputTypeDef = TypedDict(
    "_OptionalAutoMLOutputDataConfigOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class AutoMLOutputDataConfigOutputTypeDef(
    _RequiredAutoMLOutputDataConfigOutputTypeDef, _OptionalAutoMLOutputDataConfigOutputTypeDef
):
    pass


_RequiredAutoMLOutputDataConfigTypeDef = TypedDict(
    "_RequiredAutoMLOutputDataConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalAutoMLOutputDataConfigTypeDef = TypedDict(
    "_OptionalAutoMLOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class AutoMLOutputDataConfigTypeDef(
    _RequiredAutoMLOutputDataConfigTypeDef, _OptionalAutoMLOutputDataConfigTypeDef
):
    pass


TabularResolvedAttributesTypeDef = TypedDict(
    "TabularResolvedAttributesTypeDef",
    {
        "ProblemType": ProblemTypeType,
    },
    total=False,
)

VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "Subnets": Sequence[str],
    },
)

AutoParameterOutputTypeDef = TypedDict(
    "AutoParameterOutputTypeDef",
    {
        "Name": str,
        "ValueHint": str,
    },
)

AutoParameterTypeDef = TypedDict(
    "AutoParameterTypeDef",
    {
        "Name": str,
        "ValueHint": str,
    },
)

AutotuneOutputTypeDef = TypedDict(
    "AutotuneOutputTypeDef",
    {
        "Mode": Literal["Enabled"],
    },
)

AutotuneTypeDef = TypedDict(
    "AutotuneTypeDef",
    {
        "Mode": Literal["Enabled"],
    },
)

_RequiredBatchDataCaptureConfigOutputTypeDef = TypedDict(
    "_RequiredBatchDataCaptureConfigOutputTypeDef",
    {
        "DestinationS3Uri": str,
    },
)
_OptionalBatchDataCaptureConfigOutputTypeDef = TypedDict(
    "_OptionalBatchDataCaptureConfigOutputTypeDef",
    {
        "KmsKeyId": str,
        "GenerateInferenceId": bool,
    },
    total=False,
)


class BatchDataCaptureConfigOutputTypeDef(
    _RequiredBatchDataCaptureConfigOutputTypeDef, _OptionalBatchDataCaptureConfigOutputTypeDef
):
    pass


_RequiredBatchDataCaptureConfigTypeDef = TypedDict(
    "_RequiredBatchDataCaptureConfigTypeDef",
    {
        "DestinationS3Uri": str,
    },
)
_OptionalBatchDataCaptureConfigTypeDef = TypedDict(
    "_OptionalBatchDataCaptureConfigTypeDef",
    {
        "KmsKeyId": str,
        "GenerateInferenceId": bool,
    },
    total=False,
)


class BatchDataCaptureConfigTypeDef(
    _RequiredBatchDataCaptureConfigTypeDef, _OptionalBatchDataCaptureConfigTypeDef
):
    pass


BatchDescribeModelPackageErrorTypeDef = TypedDict(
    "BatchDescribeModelPackageErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorResponse": str,
    },
)

BatchDescribeModelPackageInputRequestTypeDef = TypedDict(
    "BatchDescribeModelPackageInputRequestTypeDef",
    {
        "ModelPackageArnList": Sequence[str],
    },
)

BestObjectiveNotImprovingOutputTypeDef = TypedDict(
    "BestObjectiveNotImprovingOutputTypeDef",
    {
        "MaxNumberOfTrainingJobsNotImproving": int,
    },
    total=False,
)

BestObjectiveNotImprovingTypeDef = TypedDict(
    "BestObjectiveNotImprovingTypeDef",
    {
        "MaxNumberOfTrainingJobsNotImproving": int,
    },
    total=False,
)

_RequiredMetricsSourceOutputTypeDef = TypedDict(
    "_RequiredMetricsSourceOutputTypeDef",
    {
        "ContentType": str,
        "S3Uri": str,
    },
)
_OptionalMetricsSourceOutputTypeDef = TypedDict(
    "_OptionalMetricsSourceOutputTypeDef",
    {
        "ContentDigest": str,
    },
    total=False,
)


class MetricsSourceOutputTypeDef(
    _RequiredMetricsSourceOutputTypeDef, _OptionalMetricsSourceOutputTypeDef
):
    pass


_RequiredMetricsSourceTypeDef = TypedDict(
    "_RequiredMetricsSourceTypeDef",
    {
        "ContentType": str,
        "S3Uri": str,
    },
)
_OptionalMetricsSourceTypeDef = TypedDict(
    "_OptionalMetricsSourceTypeDef",
    {
        "ContentDigest": str,
    },
    total=False,
)


class MetricsSourceTypeDef(_RequiredMetricsSourceTypeDef, _OptionalMetricsSourceTypeDef):
    pass


CacheHitResultTypeDef = TypedDict(
    "CacheHitResultTypeDef",
    {
        "SourcePipelineExecutionArn": str,
    },
    total=False,
)

OutputParameterOutputTypeDef = TypedDict(
    "OutputParameterOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

_RequiredCandidateArtifactLocationsTypeDef = TypedDict(
    "_RequiredCandidateArtifactLocationsTypeDef",
    {
        "Explainability": str,
    },
)
_OptionalCandidateArtifactLocationsTypeDef = TypedDict(
    "_OptionalCandidateArtifactLocationsTypeDef",
    {
        "ModelInsights": str,
        "BacktestResults": str,
    },
    total=False,
)


class CandidateArtifactLocationsTypeDef(
    _RequiredCandidateArtifactLocationsTypeDef, _OptionalCandidateArtifactLocationsTypeDef
):
    pass


MetricDatumTypeDef = TypedDict(
    "MetricDatumTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
        "Value": float,
        "Set": MetricSetSourceType,
        "StandardMetricName": AutoMLMetricExtendedEnumType,
    },
    total=False,
)

ModelRegisterSettingsOutputTypeDef = TypedDict(
    "ModelRegisterSettingsOutputTypeDef",
    {
        "Status": FeatureStatusType,
        "CrossAccountModelRegisterRoleArn": str,
    },
    total=False,
)

TimeSeriesForecastingSettingsOutputTypeDef = TypedDict(
    "TimeSeriesForecastingSettingsOutputTypeDef",
    {
        "Status": FeatureStatusType,
        "AmazonForecastRoleArn": str,
    },
    total=False,
)

WorkspaceSettingsOutputTypeDef = TypedDict(
    "WorkspaceSettingsOutputTypeDef",
    {
        "S3ArtifactPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ModelRegisterSettingsTypeDef = TypedDict(
    "ModelRegisterSettingsTypeDef",
    {
        "Status": FeatureStatusType,
        "CrossAccountModelRegisterRoleArn": str,
    },
    total=False,
)

TimeSeriesForecastingSettingsTypeDef = TypedDict(
    "TimeSeriesForecastingSettingsTypeDef",
    {
        "Status": FeatureStatusType,
        "AmazonForecastRoleArn": str,
    },
    total=False,
)

WorkspaceSettingsTypeDef = TypedDict(
    "WorkspaceSettingsTypeDef",
    {
        "S3ArtifactPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

CapacitySizeOutputTypeDef = TypedDict(
    "CapacitySizeOutputTypeDef",
    {
        "Type": CapacitySizeTypeType,
        "Value": int,
    },
)

CapacitySizeTypeDef = TypedDict(
    "CapacitySizeTypeDef",
    {
        "Type": CapacitySizeTypeType,
        "Value": int,
    },
)

CaptureContentTypeHeaderOutputTypeDef = TypedDict(
    "CaptureContentTypeHeaderOutputTypeDef",
    {
        "CsvContentTypes": List[str],
        "JsonContentTypes": List[str],
    },
    total=False,
)

CaptureContentTypeHeaderTypeDef = TypedDict(
    "CaptureContentTypeHeaderTypeDef",
    {
        "CsvContentTypes": Sequence[str],
        "JsonContentTypes": Sequence[str],
    },
    total=False,
)

CaptureOptionOutputTypeDef = TypedDict(
    "CaptureOptionOutputTypeDef",
    {
        "CaptureMode": CaptureModeType,
    },
)

CaptureOptionTypeDef = TypedDict(
    "CaptureOptionTypeDef",
    {
        "CaptureMode": CaptureModeType,
    },
)

CategoricalParameterOutputTypeDef = TypedDict(
    "CategoricalParameterOutputTypeDef",
    {
        "Name": str,
        "Value": List[str],
    },
)

CategoricalParameterRangeOutputTypeDef = TypedDict(
    "CategoricalParameterRangeOutputTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

CategoricalParameterRangeSpecificationOutputTypeDef = TypedDict(
    "CategoricalParameterRangeSpecificationOutputTypeDef",
    {
        "Values": List[str],
    },
)

CategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "CategoricalParameterRangeSpecificationTypeDef",
    {
        "Values": Sequence[str],
    },
)

CategoricalParameterRangeTypeDef = TypedDict(
    "CategoricalParameterRangeTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)

CategoricalParameterTypeDef = TypedDict(
    "CategoricalParameterTypeDef",
    {
        "Name": str,
        "Value": Sequence[str],
    },
)

ShuffleConfigOutputTypeDef = TypedDict(
    "ShuffleConfigOutputTypeDef",
    {
        "Seed": int,
    },
)

_RequiredChannelSpecificationOutputTypeDef = TypedDict(
    "_RequiredChannelSpecificationOutputTypeDef",
    {
        "Name": str,
        "SupportedContentTypes": List[str],
        "SupportedInputModes": List[TrainingInputModeType],
    },
)
_OptionalChannelSpecificationOutputTypeDef = TypedDict(
    "_OptionalChannelSpecificationOutputTypeDef",
    {
        "Description": str,
        "IsRequired": bool,
        "SupportedCompressionTypes": List[CompressionTypeType],
    },
    total=False,
)


class ChannelSpecificationOutputTypeDef(
    _RequiredChannelSpecificationOutputTypeDef, _OptionalChannelSpecificationOutputTypeDef
):
    pass


_RequiredChannelSpecificationTypeDef = TypedDict(
    "_RequiredChannelSpecificationTypeDef",
    {
        "Name": str,
        "SupportedContentTypes": Sequence[str],
        "SupportedInputModes": Sequence[TrainingInputModeType],
    },
)
_OptionalChannelSpecificationTypeDef = TypedDict(
    "_OptionalChannelSpecificationTypeDef",
    {
        "Description": str,
        "IsRequired": bool,
        "SupportedCompressionTypes": Sequence[CompressionTypeType],
    },
    total=False,
)


class ChannelSpecificationTypeDef(
    _RequiredChannelSpecificationTypeDef, _OptionalChannelSpecificationTypeDef
):
    pass


ShuffleConfigTypeDef = TypedDict(
    "ShuffleConfigTypeDef",
    {
        "Seed": int,
    },
)

_RequiredCheckpointConfigOutputTypeDef = TypedDict(
    "_RequiredCheckpointConfigOutputTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalCheckpointConfigOutputTypeDef = TypedDict(
    "_OptionalCheckpointConfigOutputTypeDef",
    {
        "LocalPath": str,
    },
    total=False,
)


class CheckpointConfigOutputTypeDef(
    _RequiredCheckpointConfigOutputTypeDef, _OptionalCheckpointConfigOutputTypeDef
):
    pass


_RequiredCheckpointConfigTypeDef = TypedDict(
    "_RequiredCheckpointConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalCheckpointConfigTypeDef = TypedDict(
    "_OptionalCheckpointConfigTypeDef",
    {
        "LocalPath": str,
    },
    total=False,
)


class CheckpointConfigTypeDef(_RequiredCheckpointConfigTypeDef, _OptionalCheckpointConfigTypeDef):
    pass


ClarifyCheckStepMetadataTypeDef = TypedDict(
    "ClarifyCheckStepMetadataTypeDef",
    {
        "CheckType": str,
        "BaselineUsedForDriftCheckConstraints": str,
        "CalculatedBaselineConstraints": str,
        "ModelPackageGroupName": str,
        "ViolationReport": str,
        "CheckJobArn": str,
        "SkipCheck": bool,
        "RegisterNewBaseline": bool,
    },
    total=False,
)

ClarifyInferenceConfigOutputTypeDef = TypedDict(
    "ClarifyInferenceConfigOutputTypeDef",
    {
        "FeaturesAttribute": str,
        "ContentTemplate": str,
        "MaxRecordCount": int,
        "MaxPayloadInMB": int,
        "ProbabilityIndex": int,
        "LabelIndex": int,
        "ProbabilityAttribute": str,
        "LabelAttribute": str,
        "LabelHeaders": List[str],
        "FeatureHeaders": List[str],
        "FeatureTypes": List[ClarifyFeatureTypeType],
    },
    total=False,
)

ClarifyInferenceConfigTypeDef = TypedDict(
    "ClarifyInferenceConfigTypeDef",
    {
        "FeaturesAttribute": str,
        "ContentTemplate": str,
        "MaxRecordCount": int,
        "MaxPayloadInMB": int,
        "ProbabilityIndex": int,
        "LabelIndex": int,
        "ProbabilityAttribute": str,
        "LabelAttribute": str,
        "LabelHeaders": Sequence[str],
        "FeatureHeaders": Sequence[str],
        "FeatureTypes": Sequence[ClarifyFeatureTypeType],
    },
    total=False,
)

ClarifyShapBaselineConfigOutputTypeDef = TypedDict(
    "ClarifyShapBaselineConfigOutputTypeDef",
    {
        "MimeType": str,
        "ShapBaseline": str,
        "ShapBaselineUri": str,
    },
    total=False,
)

ClarifyShapBaselineConfigTypeDef = TypedDict(
    "ClarifyShapBaselineConfigTypeDef",
    {
        "MimeType": str,
        "ShapBaseline": str,
        "ShapBaselineUri": str,
    },
    total=False,
)

ClarifyTextConfigOutputTypeDef = TypedDict(
    "ClarifyTextConfigOutputTypeDef",
    {
        "Language": ClarifyTextLanguageType,
        "Granularity": ClarifyTextGranularityType,
    },
)

ClarifyTextConfigTypeDef = TypedDict(
    "ClarifyTextConfigTypeDef",
    {
        "Language": ClarifyTextLanguageType,
        "Granularity": ClarifyTextGranularityType,
    },
)

CodeRepositoryOutputTypeDef = TypedDict(
    "CodeRepositoryOutputTypeDef",
    {
        "RepositoryUrl": str,
    },
)

_RequiredGitConfigOutputTypeDef = TypedDict(
    "_RequiredGitConfigOutputTypeDef",
    {
        "RepositoryUrl": str,
    },
)
_OptionalGitConfigOutputTypeDef = TypedDict(
    "_OptionalGitConfigOutputTypeDef",
    {
        "Branch": str,
        "SecretArn": str,
    },
    total=False,
)


class GitConfigOutputTypeDef(_RequiredGitConfigOutputTypeDef, _OptionalGitConfigOutputTypeDef):
    pass


CodeRepositoryTypeDef = TypedDict(
    "CodeRepositoryTypeDef",
    {
        "RepositoryUrl": str,
    },
)

CognitoConfigOutputTypeDef = TypedDict(
    "CognitoConfigOutputTypeDef",
    {
        "UserPool": str,
        "ClientId": str,
    },
)

CognitoConfigTypeDef = TypedDict(
    "CognitoConfigTypeDef",
    {
        "UserPool": str,
        "ClientId": str,
    },
)

CognitoMemberDefinitionOutputTypeDef = TypedDict(
    "CognitoMemberDefinitionOutputTypeDef",
    {
        "UserPool": str,
        "UserGroup": str,
        "ClientId": str,
    },
)

CognitoMemberDefinitionTypeDef = TypedDict(
    "CognitoMemberDefinitionTypeDef",
    {
        "UserPool": str,
        "UserGroup": str,
        "ClientId": str,
    },
)

CollectionConfigurationOutputTypeDef = TypedDict(
    "CollectionConfigurationOutputTypeDef",
    {
        "CollectionName": str,
        "CollectionParameters": Dict[str, str],
    },
    total=False,
)

CollectionConfigurationTypeDef = TypedDict(
    "CollectionConfigurationTypeDef",
    {
        "CollectionName": str,
        "CollectionParameters": Mapping[str, str],
    },
    total=False,
)

_RequiredCompilationJobSummaryTypeDef = TypedDict(
    "_RequiredCompilationJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationJobStatus": CompilationJobStatusType,
    },
)
_OptionalCompilationJobSummaryTypeDef = TypedDict(
    "_OptionalCompilationJobSummaryTypeDef",
    {
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "CompilationTargetDevice": TargetDeviceType,
        "CompilationTargetPlatformOs": TargetPlatformOsType,
        "CompilationTargetPlatformArch": TargetPlatformArchType,
        "CompilationTargetPlatformAccelerator": TargetPlatformAcceleratorType,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class CompilationJobSummaryTypeDef(
    _RequiredCompilationJobSummaryTypeDef, _OptionalCompilationJobSummaryTypeDef
):
    pass


ConditionStepMetadataTypeDef = TypedDict(
    "ConditionStepMetadataTypeDef",
    {
        "Outcome": ConditionOutcomeType,
    },
    total=False,
)

MultiModelConfigOutputTypeDef = TypedDict(
    "MultiModelConfigOutputTypeDef",
    {
        "ModelCacheSetting": ModelCacheSettingType,
    },
    total=False,
)

MultiModelConfigTypeDef = TypedDict(
    "MultiModelConfigTypeDef",
    {
        "ModelCacheSetting": ModelCacheSettingType,
    },
    total=False,
)

_RequiredContextSourceOutputTypeDef = TypedDict(
    "_RequiredContextSourceOutputTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalContextSourceOutputTypeDef = TypedDict(
    "_OptionalContextSourceOutputTypeDef",
    {
        "SourceType": str,
        "SourceId": str,
    },
    total=False,
)


class ContextSourceOutputTypeDef(
    _RequiredContextSourceOutputTypeDef, _OptionalContextSourceOutputTypeDef
):
    pass


_RequiredContextSourceTypeDef = TypedDict(
    "_RequiredContextSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalContextSourceTypeDef = TypedDict(
    "_OptionalContextSourceTypeDef",
    {
        "SourceType": str,
        "SourceId": str,
    },
    total=False,
)


class ContextSourceTypeDef(_RequiredContextSourceTypeDef, _OptionalContextSourceTypeDef):
    pass


_RequiredContinuousParameterRangeOutputTypeDef = TypedDict(
    "_RequiredContinuousParameterRangeOutputTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
    },
)
_OptionalContinuousParameterRangeOutputTypeDef = TypedDict(
    "_OptionalContinuousParameterRangeOutputTypeDef",
    {
        "ScalingType": HyperParameterScalingTypeType,
    },
    total=False,
)


class ContinuousParameterRangeOutputTypeDef(
    _RequiredContinuousParameterRangeOutputTypeDef, _OptionalContinuousParameterRangeOutputTypeDef
):
    pass


ContinuousParameterRangeSpecificationOutputTypeDef = TypedDict(
    "ContinuousParameterRangeSpecificationOutputTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

ContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "ContinuousParameterRangeSpecificationTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

_RequiredContinuousParameterRangeTypeDef = TypedDict(
    "_RequiredContinuousParameterRangeTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
    },
)
_OptionalContinuousParameterRangeTypeDef = TypedDict(
    "_OptionalContinuousParameterRangeTypeDef",
    {
        "ScalingType": HyperParameterScalingTypeType,
    },
    total=False,
)


class ContinuousParameterRangeTypeDef(
    _RequiredContinuousParameterRangeTypeDef, _OptionalContinuousParameterRangeTypeDef
):
    pass


ConvergenceDetectedOutputTypeDef = TypedDict(
    "ConvergenceDetectedOutputTypeDef",
    {
        "CompleteOnConvergence": CompleteOnConvergenceType,
    },
    total=False,
)

ConvergenceDetectedTypeDef = TypedDict(
    "ConvergenceDetectedTypeDef",
    {
        "CompleteOnConvergence": CompleteOnConvergenceType,
    },
    total=False,
)

MetadataPropertiesTypeDef = TypedDict(
    "MetadataPropertiesTypeDef",
    {
        "CommitId": str,
        "Repository": str,
        "GeneratedBy": str,
        "ProjectId": str,
    },
    total=False,
)

ResourceSpecTypeDef = TypedDict(
    "ResourceSpecTypeDef",
    {
        "SageMakerImageArn": str,
        "SageMakerImageVersionArn": str,
        "InstanceType": AppInstanceTypeType,
        "LifecycleConfigArn": str,
    },
    total=False,
)

ModelDeployConfigTypeDef = TypedDict(
    "ModelDeployConfigTypeDef",
    {
        "AutoGenerateEndpointName": bool,
        "EndpointName": str,
    },
    total=False,
)

_RequiredGitConfigTypeDef = TypedDict(
    "_RequiredGitConfigTypeDef",
    {
        "RepositoryUrl": str,
    },
)
_OptionalGitConfigTypeDef = TypedDict(
    "_OptionalGitConfigTypeDef",
    {
        "Branch": str,
        "SecretArn": str,
    },
    total=False,
)


class GitConfigTypeDef(_RequiredGitConfigTypeDef, _OptionalGitConfigTypeDef):
    pass


_RequiredInputConfigTypeDef = TypedDict(
    "_RequiredInputConfigTypeDef",
    {
        "S3Uri": str,
        "DataInputConfig": str,
        "Framework": FrameworkType,
    },
)
_OptionalInputConfigTypeDef = TypedDict(
    "_OptionalInputConfigTypeDef",
    {
        "FrameworkVersion": str,
    },
    total=False,
)


class InputConfigTypeDef(_RequiredInputConfigTypeDef, _OptionalInputConfigTypeDef):
    pass


NeoVpcConfigTypeDef = TypedDict(
    "NeoVpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "Subnets": Sequence[str],
    },
)

StoppingConditionTypeDef = TypedDict(
    "StoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
        "MaxWaitTimeInSeconds": int,
    },
    total=False,
)

_RequiredDataQualityAppSpecificationTypeDef = TypedDict(
    "_RequiredDataQualityAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalDataQualityAppSpecificationTypeDef = TypedDict(
    "_OptionalDataQualityAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": Sequence[str],
        "ContainerArguments": Sequence[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
        "Environment": Mapping[str, str],
    },
    total=False,
)


class DataQualityAppSpecificationTypeDef(
    _RequiredDataQualityAppSpecificationTypeDef, _OptionalDataQualityAppSpecificationTypeDef
):
    pass


MonitoringStoppingConditionTypeDef = TypedDict(
    "MonitoringStoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

_RequiredEdgeOutputConfigTypeDef = TypedDict(
    "_RequiredEdgeOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
    },
)
_OptionalEdgeOutputConfigTypeDef = TypedDict(
    "_OptionalEdgeOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "PresetDeploymentType": Literal["GreengrassV2Component"],
        "PresetDeploymentConfig": str,
    },
    total=False,
)


class EdgeOutputConfigTypeDef(_RequiredEdgeOutputConfigTypeDef, _OptionalEdgeOutputConfigTypeDef):
    pass


EdgeDeploymentModelConfigTypeDef = TypedDict(
    "EdgeDeploymentModelConfigTypeDef",
    {
        "ModelHandle": str,
        "EdgePackagingJobName": str,
    },
)

FeatureDefinitionTypeDef = TypedDict(
    "FeatureDefinitionTypeDef",
    {
        "FeatureName": str,
        "FeatureType": FeatureTypeType,
    },
    total=False,
)

_RequiredFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_RequiredFlowDefinitionOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_OptionalFlowDefinitionOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class FlowDefinitionOutputConfigTypeDef(
    _RequiredFlowDefinitionOutputConfigTypeDef, _OptionalFlowDefinitionOutputConfigTypeDef
):
    pass


HumanLoopRequestSourceTypeDef = TypedDict(
    "HumanLoopRequestSourceTypeDef",
    {
        "AwsManagedHumanLoopRequestSource": AwsManagedHumanLoopRequestSourceType,
    },
)

HubS3StorageConfigTypeDef = TypedDict(
    "HubS3StorageConfigTypeDef",
    {
        "S3OutputPath": str,
    },
    total=False,
)

UiTemplateTypeDef = TypedDict(
    "UiTemplateTypeDef",
    {
        "Content": str,
    },
)

_RequiredCreateImageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageVersionRequestRequestTypeDef",
    {
        "BaseImage": str,
        "ClientToken": str,
        "ImageName": str,
    },
)
_OptionalCreateImageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageVersionRequestRequestTypeDef",
    {
        "Aliases": Sequence[str],
        "VendorGuidance": VendorGuidanceType,
        "JobType": JobTypeType,
        "MLFramework": str,
        "ProgrammingLang": str,
        "Processor": ProcessorType,
        "Horovod": bool,
        "ReleaseNotes": str,
    },
    total=False,
)


class CreateImageVersionRequestRequestTypeDef(
    _RequiredCreateImageVersionRequestRequestTypeDef,
    _OptionalCreateImageVersionRequestRequestTypeDef,
):
    pass


InferenceExperimentScheduleTypeDef = TypedDict(
    "InferenceExperimentScheduleTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

_RequiredLabelingJobOutputConfigTypeDef = TypedDict(
    "_RequiredLabelingJobOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalLabelingJobOutputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "SnsTopicArn": str,
    },
    total=False,
)


class LabelingJobOutputConfigTypeDef(
    _RequiredLabelingJobOutputConfigTypeDef, _OptionalLabelingJobOutputConfigTypeDef
):
    pass


LabelingJobStoppingConditionsTypeDef = TypedDict(
    "LabelingJobStoppingConditionsTypeDef",
    {
        "MaxHumanLabeledObjectCount": int,
        "MaxPercentageOfInputDatasetLabeled": int,
    },
    total=False,
)

_RequiredModelBiasAppSpecificationTypeDef = TypedDict(
    "_RequiredModelBiasAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
    },
)
_OptionalModelBiasAppSpecificationTypeDef = TypedDict(
    "_OptionalModelBiasAppSpecificationTypeDef",
    {
        "Environment": Mapping[str, str],
    },
    total=False,
)


class ModelBiasAppSpecificationTypeDef(
    _RequiredModelBiasAppSpecificationTypeDef, _OptionalModelBiasAppSpecificationTypeDef
):
    pass


ModelCardExportOutputConfigTypeDef = TypedDict(
    "ModelCardExportOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)

ModelCardSecurityConfigTypeDef = TypedDict(
    "ModelCardSecurityConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

_RequiredModelExplainabilityAppSpecificationTypeDef = TypedDict(
    "_RequiredModelExplainabilityAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
    },
)
_OptionalModelExplainabilityAppSpecificationTypeDef = TypedDict(
    "_OptionalModelExplainabilityAppSpecificationTypeDef",
    {
        "Environment": Mapping[str, str],
    },
    total=False,
)


class ModelExplainabilityAppSpecificationTypeDef(
    _RequiredModelExplainabilityAppSpecificationTypeDef,
    _OptionalModelExplainabilityAppSpecificationTypeDef,
):
    pass


InferenceExecutionConfigTypeDef = TypedDict(
    "InferenceExecutionConfigTypeDef",
    {
        "Mode": InferenceExecutionModeType,
    },
)

_RequiredModelQualityAppSpecificationTypeDef = TypedDict(
    "_RequiredModelQualityAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalModelQualityAppSpecificationTypeDef = TypedDict(
    "_OptionalModelQualityAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": Sequence[str],
        "ContainerArguments": Sequence[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
        "ProblemType": MonitoringProblemTypeType,
        "Environment": Mapping[str, str],
    },
    total=False,
)


class ModelQualityAppSpecificationTypeDef(
    _RequiredModelQualityAppSpecificationTypeDef, _OptionalModelQualityAppSpecificationTypeDef
):
    pass


InstanceMetadataServiceConfigurationTypeDef = TypedDict(
    "InstanceMetadataServiceConfigurationTypeDef",
    {
        "MinimumInstanceMetadataServiceVersion": str,
    },
)

NotebookInstanceLifecycleHookTypeDef = TypedDict(
    "NotebookInstanceLifecycleHookTypeDef",
    {
        "Content": str,
    },
    total=False,
)

ParallelismConfigurationTypeDef = TypedDict(
    "ParallelismConfigurationTypeDef",
    {
        "MaxParallelExecutionSteps": int,
    },
)

_RequiredPipelineDefinitionS3LocationTypeDef = TypedDict(
    "_RequiredPipelineDefinitionS3LocationTypeDef",
    {
        "Bucket": str,
        "ObjectKey": str,
    },
)
_OptionalPipelineDefinitionS3LocationTypeDef = TypedDict(
    "_OptionalPipelineDefinitionS3LocationTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)


class PipelineDefinitionS3LocationTypeDef(
    _RequiredPipelineDefinitionS3LocationTypeDef, _OptionalPipelineDefinitionS3LocationTypeDef
):
    pass


_RequiredCreatePresignedDomainUrlRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePresignedDomainUrlRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalCreatePresignedDomainUrlRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePresignedDomainUrlRequestRequestTypeDef",
    {
        "SessionExpirationDurationInSeconds": int,
        "ExpiresInSeconds": int,
        "SpaceName": str,
    },
    total=False,
)


class CreatePresignedDomainUrlRequestRequestTypeDef(
    _RequiredCreatePresignedDomainUrlRequestRequestTypeDef,
    _OptionalCreatePresignedDomainUrlRequestRequestTypeDef,
):
    pass


_RequiredCreatePresignedNotebookInstanceUrlInputRequestTypeDef = TypedDict(
    "_RequiredCreatePresignedNotebookInstanceUrlInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalCreatePresignedNotebookInstanceUrlInputRequestTypeDef = TypedDict(
    "_OptionalCreatePresignedNotebookInstanceUrlInputRequestTypeDef",
    {
        "SessionExpirationDurationInSeconds": int,
    },
    total=False,
)


class CreatePresignedNotebookInstanceUrlInputRequestTypeDef(
    _RequiredCreatePresignedNotebookInstanceUrlInputRequestTypeDef,
    _OptionalCreatePresignedNotebookInstanceUrlInputRequestTypeDef,
):
    pass


ExperimentConfigTypeDef = TypedDict(
    "ExperimentConfigTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
        "TrialComponentDisplayName": str,
        "RunName": str,
    },
    total=False,
)

ProcessingStoppingConditionTypeDef = TypedDict(
    "ProcessingStoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

_RequiredDebugRuleConfigurationTypeDef = TypedDict(
    "_RequiredDebugRuleConfigurationTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
    },
)
_OptionalDebugRuleConfigurationTypeDef = TypedDict(
    "_OptionalDebugRuleConfigurationTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "RuleParameters": Mapping[str, str],
    },
    total=False,
)


class DebugRuleConfigurationTypeDef(
    _RequiredDebugRuleConfigurationTypeDef, _OptionalDebugRuleConfigurationTypeDef
):
    pass


_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
        "CompressionType": OutputCompressionTypeType,
    },
    total=False,
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass


ProfilerConfigTypeDef = TypedDict(
    "ProfilerConfigTypeDef",
    {
        "S3OutputPath": str,
        "ProfilingIntervalInMilliseconds": int,
        "ProfilingParameters": Mapping[str, str],
        "DisableProfiler": bool,
    },
    total=False,
)

_RequiredProfilerRuleConfigurationTypeDef = TypedDict(
    "_RequiredProfilerRuleConfigurationTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
    },
)
_OptionalProfilerRuleConfigurationTypeDef = TypedDict(
    "_OptionalProfilerRuleConfigurationTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "RuleParameters": Mapping[str, str],
    },
    total=False,
)


class ProfilerRuleConfigurationTypeDef(
    _RequiredProfilerRuleConfigurationTypeDef, _OptionalProfilerRuleConfigurationTypeDef
):
    pass


RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "MaximumRetryAttempts": int,
    },
)

_RequiredTensorBoardOutputConfigTypeDef = TypedDict(
    "_RequiredTensorBoardOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalTensorBoardOutputConfigTypeDef = TypedDict(
    "_OptionalTensorBoardOutputConfigTypeDef",
    {
        "LocalPath": str,
    },
    total=False,
)


class TensorBoardOutputConfigTypeDef(
    _RequiredTensorBoardOutputConfigTypeDef, _OptionalTensorBoardOutputConfigTypeDef
):
    pass


DataProcessingTypeDef = TypedDict(
    "DataProcessingTypeDef",
    {
        "InputFilter": str,
        "OutputFilter": str,
        "JoinSource": JoinSourceType,
    },
    total=False,
)

ModelClientConfigTypeDef = TypedDict(
    "ModelClientConfigTypeDef",
    {
        "InvocationsTimeoutInSeconds": int,
        "InvocationsMaxRetries": int,
    },
    total=False,
)

_RequiredTransformOutputTypeDef = TypedDict(
    "_RequiredTransformOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalTransformOutputTypeDef = TypedDict(
    "_OptionalTransformOutputTypeDef",
    {
        "Accept": str,
        "AssembleWith": AssemblyTypeType,
        "KmsKeyId": str,
    },
    total=False,
)


class TransformOutputTypeDef(_RequiredTransformOutputTypeDef, _OptionalTransformOutputTypeDef):
    pass


_RequiredTransformResourcesTypeDef = TypedDict(
    "_RequiredTransformResourcesTypeDef",
    {
        "InstanceType": TransformInstanceTypeType,
        "InstanceCount": int,
    },
)
_OptionalTransformResourcesTypeDef = TypedDict(
    "_OptionalTransformResourcesTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class TransformResourcesTypeDef(
    _RequiredTransformResourcesTypeDef, _OptionalTransformResourcesTypeDef
):
    pass


_RequiredTrialComponentArtifactTypeDef = TypedDict(
    "_RequiredTrialComponentArtifactTypeDef",
    {
        "Value": str,
    },
)
_OptionalTrialComponentArtifactTypeDef = TypedDict(
    "_OptionalTrialComponentArtifactTypeDef",
    {
        "MediaType": str,
    },
    total=False,
)


class TrialComponentArtifactTypeDef(
    _RequiredTrialComponentArtifactTypeDef, _OptionalTrialComponentArtifactTypeDef
):
    pass


TrialComponentParameterValueTypeDef = TypedDict(
    "TrialComponentParameterValueTypeDef",
    {
        "StringValue": str,
        "NumberValue": float,
    },
    total=False,
)

TrialComponentStatusTypeDef = TypedDict(
    "TrialComponentStatusTypeDef",
    {
        "PrimaryStatus": TrialComponentPrimaryStatusType,
        "Message": str,
    },
    total=False,
)

OidcConfigTypeDef = TypedDict(
    "OidcConfigTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "LogoutEndpoint": str,
        "JwksUri": str,
    },
)

SourceIpConfigTypeDef = TypedDict(
    "SourceIpConfigTypeDef",
    {
        "Cidrs": Sequence[str],
    },
)

WorkforceVpcConfigRequestTypeDef = TypedDict(
    "WorkforceVpcConfigRequestTypeDef",
    {
        "VpcId": str,
        "SecurityGroupIds": Sequence[str],
        "Subnets": Sequence[str],
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "NotificationTopicArn": str,
    },
    total=False,
)

_RequiredCustomImageOutputTypeDef = TypedDict(
    "_RequiredCustomImageOutputTypeDef",
    {
        "ImageName": str,
        "AppImageConfigName": str,
    },
)
_OptionalCustomImageOutputTypeDef = TypedDict(
    "_OptionalCustomImageOutputTypeDef",
    {
        "ImageVersionNumber": int,
    },
    total=False,
)


class CustomImageOutputTypeDef(
    _RequiredCustomImageOutputTypeDef, _OptionalCustomImageOutputTypeDef
):
    pass


_RequiredCustomImageTypeDef = TypedDict(
    "_RequiredCustomImageTypeDef",
    {
        "ImageName": str,
        "AppImageConfigName": str,
    },
)
_OptionalCustomImageTypeDef = TypedDict(
    "_OptionalCustomImageTypeDef",
    {
        "ImageVersionNumber": int,
    },
    total=False,
)


class CustomImageTypeDef(_RequiredCustomImageTypeDef, _OptionalCustomImageTypeDef):
    pass


DataCaptureConfigSummaryTypeDef = TypedDict(
    "DataCaptureConfigSummaryTypeDef",
    {
        "EnableCapture": bool,
        "CaptureStatus": CaptureStatusType,
        "CurrentSamplingPercentage": int,
        "DestinationS3Uri": str,
        "KmsKeyId": str,
    },
)

DataCatalogConfigOutputTypeDef = TypedDict(
    "DataCatalogConfigOutputTypeDef",
    {
        "TableName": str,
        "Catalog": str,
        "Database": str,
    },
)

DataCatalogConfigTypeDef = TypedDict(
    "DataCatalogConfigTypeDef",
    {
        "TableName": str,
        "Catalog": str,
        "Database": str,
    },
)

DataProcessingOutputTypeDef = TypedDict(
    "DataProcessingOutputTypeDef",
    {
        "InputFilter": str,
        "OutputFilter": str,
        "JoinSource": JoinSourceType,
    },
    total=False,
)

_RequiredDataQualityAppSpecificationOutputTypeDef = TypedDict(
    "_RequiredDataQualityAppSpecificationOutputTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalDataQualityAppSpecificationOutputTypeDef = TypedDict(
    "_OptionalDataQualityAppSpecificationOutputTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
        "Environment": Dict[str, str],
    },
    total=False,
)


class DataQualityAppSpecificationOutputTypeDef(
    _RequiredDataQualityAppSpecificationOutputTypeDef,
    _OptionalDataQualityAppSpecificationOutputTypeDef,
):
    pass


MonitoringConstraintsResourceOutputTypeDef = TypedDict(
    "MonitoringConstraintsResourceOutputTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringStatisticsResourceOutputTypeDef = TypedDict(
    "MonitoringStatisticsResourceOutputTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringConstraintsResourceTypeDef = TypedDict(
    "MonitoringConstraintsResourceTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringStatisticsResourceTypeDef = TypedDict(
    "MonitoringStatisticsResourceTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

_RequiredEndpointInputOutputTypeDef = TypedDict(
    "_RequiredEndpointInputOutputTypeDef",
    {
        "EndpointName": str,
        "LocalPath": str,
    },
)
_OptionalEndpointInputOutputTypeDef = TypedDict(
    "_OptionalEndpointInputOutputTypeDef",
    {
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "FeaturesAttribute": str,
        "InferenceAttribute": str,
        "ProbabilityAttribute": str,
        "ProbabilityThresholdAttribute": float,
        "StartTimeOffset": str,
        "EndTimeOffset": str,
    },
    total=False,
)


class EndpointInputOutputTypeDef(
    _RequiredEndpointInputOutputTypeDef, _OptionalEndpointInputOutputTypeDef
):
    pass


_RequiredEndpointInputTypeDef = TypedDict(
    "_RequiredEndpointInputTypeDef",
    {
        "EndpointName": str,
        "LocalPath": str,
    },
)
_OptionalEndpointInputTypeDef = TypedDict(
    "_OptionalEndpointInputTypeDef",
    {
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "FeaturesAttribute": str,
        "InferenceAttribute": str,
        "ProbabilityAttribute": str,
        "ProbabilityThresholdAttribute": float,
        "StartTimeOffset": str,
        "EndTimeOffset": str,
    },
    total=False,
)


class EndpointInputTypeDef(_RequiredEndpointInputTypeDef, _OptionalEndpointInputTypeDef):
    pass


FileSystemDataSourceOutputTypeDef = TypedDict(
    "FileSystemDataSourceOutputTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": FileSystemAccessModeType,
        "FileSystemType": FileSystemTypeType,
        "DirectoryPath": str,
    },
)

_RequiredS3DataSourceOutputTypeDef = TypedDict(
    "_RequiredS3DataSourceOutputTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)
_OptionalS3DataSourceOutputTypeDef = TypedDict(
    "_OptionalS3DataSourceOutputTypeDef",
    {
        "S3DataDistributionType": S3DataDistributionType,
        "AttributeNames": List[str],
        "InstanceGroupNames": List[str],
    },
    total=False,
)


class S3DataSourceOutputTypeDef(
    _RequiredS3DataSourceOutputTypeDef, _OptionalS3DataSourceOutputTypeDef
):
    pass


FileSystemDataSourceTypeDef = TypedDict(
    "FileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": FileSystemAccessModeType,
        "FileSystemType": FileSystemTypeType,
        "DirectoryPath": str,
    },
)

_RequiredS3DataSourceTypeDef = TypedDict(
    "_RequiredS3DataSourceTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)
_OptionalS3DataSourceTypeDef = TypedDict(
    "_OptionalS3DataSourceTypeDef",
    {
        "S3DataDistributionType": S3DataDistributionType,
        "AttributeNames": Sequence[str],
        "InstanceGroupNames": Sequence[str],
    },
    total=False,
)


class S3DataSourceTypeDef(_RequiredS3DataSourceTypeDef, _OptionalS3DataSourceTypeDef):
    pass


_RequiredRedshiftDatasetDefinitionOutputTypeDef = TypedDict(
    "_RequiredRedshiftDatasetDefinitionOutputTypeDef",
    {
        "ClusterId": str,
        "Database": str,
        "DbUser": str,
        "QueryString": str,
        "ClusterRoleArn": str,
        "OutputS3Uri": str,
        "OutputFormat": RedshiftResultFormatType,
    },
)
_OptionalRedshiftDatasetDefinitionOutputTypeDef = TypedDict(
    "_OptionalRedshiftDatasetDefinitionOutputTypeDef",
    {
        "KmsKeyId": str,
        "OutputCompression": RedshiftResultCompressionTypeType,
    },
    total=False,
)


class RedshiftDatasetDefinitionOutputTypeDef(
    _RequiredRedshiftDatasetDefinitionOutputTypeDef, _OptionalRedshiftDatasetDefinitionOutputTypeDef
):
    pass


_RequiredRedshiftDatasetDefinitionTypeDef = TypedDict(
    "_RequiredRedshiftDatasetDefinitionTypeDef",
    {
        "ClusterId": str,
        "Database": str,
        "DbUser": str,
        "QueryString": str,
        "ClusterRoleArn": str,
        "OutputS3Uri": str,
        "OutputFormat": RedshiftResultFormatType,
    },
)
_OptionalRedshiftDatasetDefinitionTypeDef = TypedDict(
    "_OptionalRedshiftDatasetDefinitionTypeDef",
    {
        "KmsKeyId": str,
        "OutputCompression": RedshiftResultCompressionTypeType,
    },
    total=False,
)


class RedshiftDatasetDefinitionTypeDef(
    _RequiredRedshiftDatasetDefinitionTypeDef, _OptionalRedshiftDatasetDefinitionTypeDef
):
    pass


_RequiredDebugRuleConfigurationOutputTypeDef = TypedDict(
    "_RequiredDebugRuleConfigurationOutputTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
    },
)
_OptionalDebugRuleConfigurationOutputTypeDef = TypedDict(
    "_OptionalDebugRuleConfigurationOutputTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)


class DebugRuleConfigurationOutputTypeDef(
    _RequiredDebugRuleConfigurationOutputTypeDef, _OptionalDebugRuleConfigurationOutputTypeDef
):
    pass


DebugRuleEvaluationStatusTypeDef = TypedDict(
    "DebugRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": RuleEvaluationStatusType,
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

DeleteActionRequestRequestTypeDef = TypedDict(
    "DeleteActionRequestRequestTypeDef",
    {
        "ActionName": str,
    },
)

DeleteAlgorithmInputRequestTypeDef = TypedDict(
    "DeleteAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
    },
)

DeleteAppImageConfigRequestRequestTypeDef = TypedDict(
    "DeleteAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)

_RequiredDeleteAppRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)
_OptionalDeleteAppRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAppRequestRequestTypeDef",
    {
        "UserProfileName": str,
        "SpaceName": str,
    },
    total=False,
)


class DeleteAppRequestRequestTypeDef(
    _RequiredDeleteAppRequestRequestTypeDef, _OptionalDeleteAppRequestRequestTypeDef
):
    pass


DeleteAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssociationRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
    },
)

DeleteCodeRepositoryInputRequestTypeDef = TypedDict(
    "DeleteCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
    },
)

DeleteContextRequestRequestTypeDef = TypedDict(
    "DeleteContextRequestRequestTypeDef",
    {
        "ContextName": str,
    },
)

DeleteDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteDeviceFleetRequestRequestTypeDef = TypedDict(
    "DeleteDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

RetentionPolicyTypeDef = TypedDict(
    "RetentionPolicyTypeDef",
    {
        "HomeEfsFileSystem": RetentionTypeType,
    },
    total=False,
)

DeleteEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "DeleteEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
    },
)

DeleteEdgeDeploymentStageRequestRequestTypeDef = TypedDict(
    "DeleteEdgeDeploymentStageRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)

DeleteEndpointConfigInputRequestTypeDef = TypedDict(
    "DeleteEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
    },
)

DeleteEndpointInputRequestTypeDef = TypedDict(
    "DeleteEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteExperimentRequestRequestTypeDef = TypedDict(
    "DeleteExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)

DeleteFeatureGroupRequestRequestTypeDef = TypedDict(
    "DeleteFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)

DeleteFlowDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
    },
)

DeleteHubContentRequestRequestTypeDef = TypedDict(
    "DeleteHubContentRequestRequestTypeDef",
    {
        "HubName": str,
        "HubContentType": HubContentTypeType,
        "HubContentName": str,
        "HubContentVersion": str,
    },
)

DeleteHubRequestRequestTypeDef = TypedDict(
    "DeleteHubRequestRequestTypeDef",
    {
        "HubName": str,
    },
)

DeleteHumanTaskUiRequestRequestTypeDef = TypedDict(
    "DeleteHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
    },
)

DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)

_RequiredDeleteImageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteImageVersionRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDeleteImageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteImageVersionRequestRequestTypeDef",
    {
        "Version": int,
        "Alias": str,
    },
    total=False,
)


class DeleteImageVersionRequestRequestTypeDef(
    _RequiredDeleteImageVersionRequestRequestTypeDef,
    _OptionalDeleteImageVersionRequestRequestTypeDef,
):
    pass


DeleteInferenceExperimentRequestRequestTypeDef = TypedDict(
    "DeleteInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteModelCardRequestRequestTypeDef = TypedDict(
    "DeleteModelCardRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)

DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteModelInputRequestTypeDef = TypedDict(
    "DeleteModelInputRequestTypeDef",
    {
        "ModelName": str,
    },
)

DeleteModelPackageGroupInputRequestTypeDef = TypedDict(
    "DeleteModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DeleteModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "DeleteModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DeleteModelPackageInputRequestTypeDef = TypedDict(
    "DeleteModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": str,
    },
)

DeleteModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "DeleteMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

DeleteNotebookInstanceInputRequestTypeDef = TypedDict(
    "DeleteNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)

DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
    },
)

DeleteProjectInputRequestTypeDef = TypedDict(
    "DeleteProjectInputRequestTypeDef",
    {
        "ProjectName": str,
    },
)

DeleteSpaceRequestRequestTypeDef = TypedDict(
    "DeleteSpaceRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
    },
)

DeleteStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "DeleteStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
    },
)

DeleteTagsInputRequestTypeDef = TypedDict(
    "DeleteTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

DeleteTrialComponentRequestRequestTypeDef = TypedDict(
    "DeleteTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)

DeleteTrialRequestRequestTypeDef = TypedDict(
    "DeleteTrialRequestRequestTypeDef",
    {
        "TrialName": str,
    },
)

DeleteUserProfileRequestRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)

DeleteWorkforceRequestRequestTypeDef = TypedDict(
    "DeleteWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)

DeleteWorkteamRequestRequestTypeDef = TypedDict(
    "DeleteWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
    },
)

DeployedImageTypeDef = TypedDict(
    "DeployedImageTypeDef",
    {
        "SpecifiedImage": str,
        "ResolvedImage": str,
        "ResolutionTime": datetime,
    },
    total=False,
)

_RequiredRealTimeInferenceRecommendationTypeDef = TypedDict(
    "_RequiredRealTimeInferenceRecommendationTypeDef",
    {
        "RecommendationId": str,
        "InstanceType": ProductionVariantInstanceTypeType,
    },
)
_OptionalRealTimeInferenceRecommendationTypeDef = TypedDict(
    "_OptionalRealTimeInferenceRecommendationTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)


class RealTimeInferenceRecommendationTypeDef(
    _RequiredRealTimeInferenceRecommendationTypeDef, _OptionalRealTimeInferenceRecommendationTypeDef
):
    pass


_RequiredDeviceSelectionConfigOutputTypeDef = TypedDict(
    "_RequiredDeviceSelectionConfigOutputTypeDef",
    {
        "DeviceSubsetType": DeviceSubsetTypeType,
    },
)
_OptionalDeviceSelectionConfigOutputTypeDef = TypedDict(
    "_OptionalDeviceSelectionConfigOutputTypeDef",
    {
        "Percentage": int,
        "DeviceNames": List[str],
        "DeviceNameContains": str,
    },
    total=False,
)


class DeviceSelectionConfigOutputTypeDef(
    _RequiredDeviceSelectionConfigOutputTypeDef, _OptionalDeviceSelectionConfigOutputTypeDef
):
    pass


EdgeDeploymentConfigOutputTypeDef = TypedDict(
    "EdgeDeploymentConfigOutputTypeDef",
    {
        "FailureHandlingPolicy": FailureHandlingPolicyType,
    },
)

_RequiredEdgeDeploymentStatusTypeDef = TypedDict(
    "_RequiredEdgeDeploymentStatusTypeDef",
    {
        "StageStatus": StageStatusType,
        "EdgeDeploymentSuccessInStage": int,
        "EdgeDeploymentPendingInStage": int,
        "EdgeDeploymentFailedInStage": int,
    },
)
_OptionalEdgeDeploymentStatusTypeDef = TypedDict(
    "_OptionalEdgeDeploymentStatusTypeDef",
    {
        "EdgeDeploymentStatusMessage": str,
        "EdgeDeploymentStageStartTime": datetime,
    },
    total=False,
)


class EdgeDeploymentStatusTypeDef(
    _RequiredEdgeDeploymentStatusTypeDef, _OptionalEdgeDeploymentStatusTypeDef
):
    pass


_RequiredDeviceSelectionConfigTypeDef = TypedDict(
    "_RequiredDeviceSelectionConfigTypeDef",
    {
        "DeviceSubsetType": DeviceSubsetTypeType,
    },
)
_OptionalDeviceSelectionConfigTypeDef = TypedDict(
    "_OptionalDeviceSelectionConfigTypeDef",
    {
        "Percentage": int,
        "DeviceNames": Sequence[str],
        "DeviceNameContains": str,
    },
    total=False,
)


class DeviceSelectionConfigTypeDef(
    _RequiredDeviceSelectionConfigTypeDef, _OptionalDeviceSelectionConfigTypeDef
):
    pass


EdgeDeploymentConfigTypeDef = TypedDict(
    "EdgeDeploymentConfigTypeDef",
    {
        "FailureHandlingPolicy": FailureHandlingPolicyType,
    },
)

DeregisterDevicesRequestRequestTypeDef = TypedDict(
    "DeregisterDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "DeviceNames": Sequence[str],
    },
)

DescribeActionRequestRequestTypeDef = TypedDict(
    "DescribeActionRequestRequestTypeDef",
    {
        "ActionName": str,
    },
)

MetadataPropertiesOutputTypeDef = TypedDict(
    "MetadataPropertiesOutputTypeDef",
    {
        "CommitId": str,
        "Repository": str,
        "GeneratedBy": str,
        "ProjectId": str,
    },
    total=False,
)

DescribeAlgorithmInputRequestTypeDef = TypedDict(
    "DescribeAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
    },
)

DescribeAppImageConfigRequestRequestTypeDef = TypedDict(
    "DescribeAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)

_RequiredDescribeAppRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)
_OptionalDescribeAppRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAppRequestRequestTypeDef",
    {
        "UserProfileName": str,
        "SpaceName": str,
    },
    total=False,
)


class DescribeAppRequestRequestTypeDef(
    _RequiredDescribeAppRequestRequestTypeDef, _OptionalDescribeAppRequestRequestTypeDef
):
    pass


ResourceSpecOutputTypeDef = TypedDict(
    "ResourceSpecOutputTypeDef",
    {
        "SageMakerImageArn": str,
        "SageMakerImageVersionArn": str,
        "InstanceType": AppInstanceTypeType,
        "LifecycleConfigArn": str,
    },
    total=False,
)

DescribeArtifactRequestRequestTypeDef = TypedDict(
    "DescribeArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": str,
    },
)

DescribeAutoMLJobRequestRequestTypeDef = TypedDict(
    "DescribeAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

ModelDeployConfigOutputTypeDef = TypedDict(
    "ModelDeployConfigOutputTypeDef",
    {
        "AutoGenerateEndpointName": bool,
        "EndpointName": str,
    },
    total=False,
)

ModelDeployResultTypeDef = TypedDict(
    "ModelDeployResultTypeDef",
    {
        "EndpointName": str,
    },
    total=False,
)

DescribeAutoMLJobV2RequestRequestTypeDef = TypedDict(
    "DescribeAutoMLJobV2RequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

DescribeCodeRepositoryInputRequestTypeDef = TypedDict(
    "DescribeCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
    },
)

DescribeCompilationJobRequestRequestTypeDef = TypedDict(
    "DescribeCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
    },
)

_RequiredInputConfigOutputTypeDef = TypedDict(
    "_RequiredInputConfigOutputTypeDef",
    {
        "S3Uri": str,
        "DataInputConfig": str,
        "Framework": FrameworkType,
    },
)
_OptionalInputConfigOutputTypeDef = TypedDict(
    "_OptionalInputConfigOutputTypeDef",
    {
        "FrameworkVersion": str,
    },
    total=False,
)


class InputConfigOutputTypeDef(
    _RequiredInputConfigOutputTypeDef, _OptionalInputConfigOutputTypeDef
):
    pass


ModelArtifactsTypeDef = TypedDict(
    "ModelArtifactsTypeDef",
    {
        "S3ModelArtifacts": str,
    },
)

ModelDigestsTypeDef = TypedDict(
    "ModelDigestsTypeDef",
    {
        "ArtifactDigest": str,
    },
    total=False,
)

NeoVpcConfigOutputTypeDef = TypedDict(
    "NeoVpcConfigOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)

StoppingConditionOutputTypeDef = TypedDict(
    "StoppingConditionOutputTypeDef",
    {
        "MaxRuntimeInSeconds": int,
        "MaxWaitTimeInSeconds": int,
    },
    total=False,
)

DescribeContextRequestRequestTypeDef = TypedDict(
    "DescribeContextRequestRequestTypeDef",
    {
        "ContextName": str,
    },
)

DescribeDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

MonitoringStoppingConditionOutputTypeDef = TypedDict(
    "MonitoringStoppingConditionOutputTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

DescribeDeviceFleetRequestRequestTypeDef = TypedDict(
    "DescribeDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

_RequiredEdgeOutputConfigOutputTypeDef = TypedDict(
    "_RequiredEdgeOutputConfigOutputTypeDef",
    {
        "S3OutputLocation": str,
    },
)
_OptionalEdgeOutputConfigOutputTypeDef = TypedDict(
    "_OptionalEdgeOutputConfigOutputTypeDef",
    {
        "KmsKeyId": str,
        "PresetDeploymentType": Literal["GreengrassV2Component"],
        "PresetDeploymentConfig": str,
    },
    total=False,
)


class EdgeOutputConfigOutputTypeDef(
    _RequiredEdgeOutputConfigOutputTypeDef, _OptionalEdgeOutputConfigOutputTypeDef
):
    pass


_RequiredDescribeDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDeviceRequestRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)
_OptionalDescribeDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDeviceRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeDeviceRequestRequestTypeDef(
    _RequiredDescribeDeviceRequestRequestTypeDef, _OptionalDescribeDeviceRequestRequestTypeDef
):
    pass


_RequiredEdgeModelTypeDef = TypedDict(
    "_RequiredEdgeModelTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
    },
)
_OptionalEdgeModelTypeDef = TypedDict(
    "_OptionalEdgeModelTypeDef",
    {
        "LatestSampleTime": datetime,
        "LatestInference": datetime,
    },
    total=False,
)


class EdgeModelTypeDef(_RequiredEdgeModelTypeDef, _OptionalEdgeModelTypeDef):
    pass


DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)

_RequiredDescribeEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
    },
)
_OptionalDescribeEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeEdgeDeploymentPlanRequestRequestTypeDef(
    _RequiredDescribeEdgeDeploymentPlanRequestRequestTypeDef,
    _OptionalDescribeEdgeDeploymentPlanRequestRequestTypeDef,
):
    pass


EdgeDeploymentModelConfigOutputTypeDef = TypedDict(
    "EdgeDeploymentModelConfigOutputTypeDef",
    {
        "ModelHandle": str,
        "EdgePackagingJobName": str,
    },
)

DescribeEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "DescribeEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
    },
)

_RequiredEdgePresetDeploymentOutputTypeDef = TypedDict(
    "_RequiredEdgePresetDeploymentOutputTypeDef",
    {
        "Type": Literal["GreengrassV2Component"],
    },
)
_OptionalEdgePresetDeploymentOutputTypeDef = TypedDict(
    "_OptionalEdgePresetDeploymentOutputTypeDef",
    {
        "Artifact": str,
        "Status": EdgePresetDeploymentStatusType,
        "StatusMessage": str,
    },
    total=False,
)


class EdgePresetDeploymentOutputTypeDef(
    _RequiredEdgePresetDeploymentOutputTypeDef, _OptionalEdgePresetDeploymentOutputTypeDef
):
    pass


DescribeEndpointConfigInputRequestTypeDef = TypedDict(
    "DescribeEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

DescribeEndpointInputRequestTypeDef = TypedDict(
    "DescribeEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DescribeExperimentRequestRequestTypeDef = TypedDict(
    "DescribeExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)

_RequiredExperimentSourceTypeDef = TypedDict(
    "_RequiredExperimentSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalExperimentSourceTypeDef = TypedDict(
    "_OptionalExperimentSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)


class ExperimentSourceTypeDef(_RequiredExperimentSourceTypeDef, _OptionalExperimentSourceTypeDef):
    pass


_RequiredDescribeFeatureGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)
_OptionalDescribeFeatureGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFeatureGroupRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeFeatureGroupRequestRequestTypeDef(
    _RequiredDescribeFeatureGroupRequestRequestTypeDef,
    _OptionalDescribeFeatureGroupRequestRequestTypeDef,
):
    pass


FeatureDefinitionOutputTypeDef = TypedDict(
    "FeatureDefinitionOutputTypeDef",
    {
        "FeatureName": str,
        "FeatureType": FeatureTypeType,
    },
    total=False,
)

_RequiredLastUpdateStatusTypeDef = TypedDict(
    "_RequiredLastUpdateStatusTypeDef",
    {
        "Status": LastUpdateStatusValueType,
    },
)
_OptionalLastUpdateStatusTypeDef = TypedDict(
    "_OptionalLastUpdateStatusTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class LastUpdateStatusTypeDef(_RequiredLastUpdateStatusTypeDef, _OptionalLastUpdateStatusTypeDef):
    pass


_RequiredOfflineStoreStatusTypeDef = TypedDict(
    "_RequiredOfflineStoreStatusTypeDef",
    {
        "Status": OfflineStoreStatusValueType,
    },
)
_OptionalOfflineStoreStatusTypeDef = TypedDict(
    "_OptionalOfflineStoreStatusTypeDef",
    {
        "BlockedReason": str,
    },
    total=False,
)


class OfflineStoreStatusTypeDef(
    _RequiredOfflineStoreStatusTypeDef, _OptionalOfflineStoreStatusTypeDef
):
    pass


DescribeFeatureMetadataRequestRequestTypeDef = TypedDict(
    "DescribeFeatureMetadataRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "FeatureName": str,
    },
)

FeatureParameterOutputTypeDef = TypedDict(
    "FeatureParameterOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

DescribeFlowDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
    },
)

_RequiredFlowDefinitionOutputConfigOutputTypeDef = TypedDict(
    "_RequiredFlowDefinitionOutputConfigOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalFlowDefinitionOutputConfigOutputTypeDef = TypedDict(
    "_OptionalFlowDefinitionOutputConfigOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class FlowDefinitionOutputConfigOutputTypeDef(
    _RequiredFlowDefinitionOutputConfigOutputTypeDef,
    _OptionalFlowDefinitionOutputConfigOutputTypeDef,
):
    pass


HumanLoopRequestSourceOutputTypeDef = TypedDict(
    "HumanLoopRequestSourceOutputTypeDef",
    {
        "AwsManagedHumanLoopRequestSource": AwsManagedHumanLoopRequestSourceType,
    },
)

_RequiredDescribeHubContentRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeHubContentRequestRequestTypeDef",
    {
        "HubName": str,
        "HubContentType": HubContentTypeType,
        "HubContentName": str,
    },
)
_OptionalDescribeHubContentRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeHubContentRequestRequestTypeDef",
    {
        "HubContentVersion": str,
    },
    total=False,
)


class DescribeHubContentRequestRequestTypeDef(
    _RequiredDescribeHubContentRequestRequestTypeDef,
    _OptionalDescribeHubContentRequestRequestTypeDef,
):
    pass


HubContentDependencyTypeDef = TypedDict(
    "HubContentDependencyTypeDef",
    {
        "DependencyOriginPath": str,
        "DependencyCopyPath": str,
    },
    total=False,
)

DescribeHubRequestRequestTypeDef = TypedDict(
    "DescribeHubRequestRequestTypeDef",
    {
        "HubName": str,
    },
)

HubS3StorageConfigOutputTypeDef = TypedDict(
    "HubS3StorageConfigOutputTypeDef",
    {
        "S3OutputPath": str,
    },
    total=False,
)

DescribeHumanTaskUiRequestRequestTypeDef = TypedDict(
    "DescribeHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
    },
)

UiTemplateInfoTypeDef = TypedDict(
    "UiTemplateInfoTypeDef",
    {
        "Url": str,
        "ContentSha256": str,
    },
    total=False,
)

DescribeHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "DescribeHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)

HyperParameterTuningJobCompletionDetailsTypeDef = TypedDict(
    "HyperParameterTuningJobCompletionDetailsTypeDef",
    {
        "NumberOfTrainingJobsObjectiveNotImproving": int,
        "ConvergenceDetectedTime": datetime,
    },
    total=False,
)

HyperParameterTuningJobConsumedResourcesTypeDef = TypedDict(
    "HyperParameterTuningJobConsumedResourcesTypeDef",
    {
        "RuntimeInSeconds": int,
    },
    total=False,
)

ObjectiveStatusCountersTypeDef = TypedDict(
    "ObjectiveStatusCountersTypeDef",
    {
        "Succeeded": int,
        "Pending": int,
        "Failed": int,
    },
    total=False,
)

TrainingJobStatusCountersTypeDef = TypedDict(
    "TrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)

DescribeImageRequestRequestTypeDef = TypedDict(
    "DescribeImageRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)

_RequiredDescribeImageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImageVersionRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDescribeImageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImageVersionRequestRequestTypeDef",
    {
        "Version": int,
        "Alias": str,
    },
    total=False,
)


class DescribeImageVersionRequestRequestTypeDef(
    _RequiredDescribeImageVersionRequestRequestTypeDef,
    _OptionalDescribeImageVersionRequestRequestTypeDef,
):
    pass


DescribeInferenceExperimentRequestRequestTypeDef = TypedDict(
    "DescribeInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredEndpointMetadataTypeDef = TypedDict(
    "_RequiredEndpointMetadataTypeDef",
    {
        "EndpointName": str,
    },
)
_OptionalEndpointMetadataTypeDef = TypedDict(
    "_OptionalEndpointMetadataTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointStatus": EndpointStatusType,
        "FailureReason": str,
    },
    total=False,
)


class EndpointMetadataTypeDef(_RequiredEndpointMetadataTypeDef, _OptionalEndpointMetadataTypeDef):
    pass


InferenceExperimentScheduleOutputTypeDef = TypedDict(
    "InferenceExperimentScheduleOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

DescribeInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "DescribeInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

DescribeLabelingJobRequestRequestTypeDef = TypedDict(
    "DescribeLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
    },
)

LabelCountersTypeDef = TypedDict(
    "LabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)

_RequiredLabelingJobOutputConfigOutputTypeDef = TypedDict(
    "_RequiredLabelingJobOutputConfigOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalLabelingJobOutputConfigOutputTypeDef = TypedDict(
    "_OptionalLabelingJobOutputConfigOutputTypeDef",
    {
        "KmsKeyId": str,
        "SnsTopicArn": str,
    },
    total=False,
)


class LabelingJobOutputConfigOutputTypeDef(
    _RequiredLabelingJobOutputConfigOutputTypeDef, _OptionalLabelingJobOutputConfigOutputTypeDef
):
    pass


_RequiredLabelingJobOutputTypeDef = TypedDict(
    "_RequiredLabelingJobOutputTypeDef",
    {
        "OutputDatasetS3Uri": str,
    },
)
_OptionalLabelingJobOutputTypeDef = TypedDict(
    "_OptionalLabelingJobOutputTypeDef",
    {
        "FinalActiveLearningModelArn": str,
    },
    total=False,
)


class LabelingJobOutputTypeDef(
    _RequiredLabelingJobOutputTypeDef, _OptionalLabelingJobOutputTypeDef
):
    pass


LabelingJobStoppingConditionsOutputTypeDef = TypedDict(
    "LabelingJobStoppingConditionsOutputTypeDef",
    {
        "MaxHumanLabeledObjectCount": int,
        "MaxPercentageOfInputDatasetLabeled": int,
    },
    total=False,
)

DescribeLineageGroupRequestRequestTypeDef = TypedDict(
    "DescribeLineageGroupRequestRequestTypeDef",
    {
        "LineageGroupName": str,
    },
)

DescribeModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

_RequiredModelBiasAppSpecificationOutputTypeDef = TypedDict(
    "_RequiredModelBiasAppSpecificationOutputTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
    },
)
_OptionalModelBiasAppSpecificationOutputTypeDef = TypedDict(
    "_OptionalModelBiasAppSpecificationOutputTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)


class ModelBiasAppSpecificationOutputTypeDef(
    _RequiredModelBiasAppSpecificationOutputTypeDef, _OptionalModelBiasAppSpecificationOutputTypeDef
):
    pass


DescribeModelCardExportJobRequestRequestTypeDef = TypedDict(
    "DescribeModelCardExportJobRequestRequestTypeDef",
    {
        "ModelCardExportJobArn": str,
    },
)

ModelCardExportArtifactsTypeDef = TypedDict(
    "ModelCardExportArtifactsTypeDef",
    {
        "S3ExportArtifacts": str,
    },
)

ModelCardExportOutputConfigOutputTypeDef = TypedDict(
    "ModelCardExportOutputConfigOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)

_RequiredDescribeModelCardRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeModelCardRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalDescribeModelCardRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeModelCardRequestRequestTypeDef",
    {
        "ModelCardVersion": int,
    },
    total=False,
)


class DescribeModelCardRequestRequestTypeDef(
    _RequiredDescribeModelCardRequestRequestTypeDef, _OptionalDescribeModelCardRequestRequestTypeDef
):
    pass


ModelCardSecurityConfigOutputTypeDef = TypedDict(
    "ModelCardSecurityConfigOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

_RequiredModelExplainabilityAppSpecificationOutputTypeDef = TypedDict(
    "_RequiredModelExplainabilityAppSpecificationOutputTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
    },
)
_OptionalModelExplainabilityAppSpecificationOutputTypeDef = TypedDict(
    "_OptionalModelExplainabilityAppSpecificationOutputTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)


class ModelExplainabilityAppSpecificationOutputTypeDef(
    _RequiredModelExplainabilityAppSpecificationOutputTypeDef,
    _OptionalModelExplainabilityAppSpecificationOutputTypeDef,
):
    pass


DescribeModelInputRequestTypeDef = TypedDict(
    "DescribeModelInputRequestTypeDef",
    {
        "ModelName": str,
    },
)

InferenceExecutionConfigOutputTypeDef = TypedDict(
    "InferenceExecutionConfigOutputTypeDef",
    {
        "Mode": InferenceExecutionModeType,
    },
)

DescribeModelPackageGroupInputRequestTypeDef = TypedDict(
    "DescribeModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DescribeModelPackageInputRequestTypeDef = TypedDict(
    "DescribeModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": str,
    },
)

DescribeModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

_RequiredModelQualityAppSpecificationOutputTypeDef = TypedDict(
    "_RequiredModelQualityAppSpecificationOutputTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalModelQualityAppSpecificationOutputTypeDef = TypedDict(
    "_OptionalModelQualityAppSpecificationOutputTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
        "ProblemType": MonitoringProblemTypeType,
        "Environment": Dict[str, str],
    },
    total=False,
)


class ModelQualityAppSpecificationOutputTypeDef(
    _RequiredModelQualityAppSpecificationOutputTypeDef,
    _OptionalModelQualityAppSpecificationOutputTypeDef,
):
    pass


DescribeMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "DescribeMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

_RequiredMonitoringExecutionSummaryTypeDef = TypedDict(
    "_RequiredMonitoringExecutionSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "ScheduledTime": datetime,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringExecutionStatus": ExecutionStatusType,
    },
)
_OptionalMonitoringExecutionSummaryTypeDef = TypedDict(
    "_OptionalMonitoringExecutionSummaryTypeDef",
    {
        "ProcessingJobArn": str,
        "EndpointName": str,
        "FailureReason": str,
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)


class MonitoringExecutionSummaryTypeDef(
    _RequiredMonitoringExecutionSummaryTypeDef, _OptionalMonitoringExecutionSummaryTypeDef
):
    pass


DescribeNotebookInstanceInputRequestTypeDef = TypedDict(
    "DescribeNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)

NotebookInstanceLifecycleHookOutputTypeDef = TypedDict(
    "NotebookInstanceLifecycleHookOutputTypeDef",
    {
        "Content": str,
    },
    total=False,
)

InstanceMetadataServiceConfigurationOutputTypeDef = TypedDict(
    "InstanceMetadataServiceConfigurationOutputTypeDef",
    {
        "MinimumInstanceMetadataServiceVersion": str,
    },
)

DescribePipelineDefinitionForExecutionRequestRequestTypeDef = TypedDict(
    "DescribePipelineDefinitionForExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)

DescribePipelineExecutionRequestRequestTypeDef = TypedDict(
    "DescribePipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)

ParallelismConfigurationOutputTypeDef = TypedDict(
    "ParallelismConfigurationOutputTypeDef",
    {
        "MaxParallelExecutionSteps": int,
    },
)

PipelineExperimentConfigTypeDef = TypedDict(
    "PipelineExperimentConfigTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
    },
    total=False,
)

DescribePipelineRequestRequestTypeDef = TypedDict(
    "DescribePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)

DescribeProcessingJobRequestRequestTypeDef = TypedDict(
    "DescribeProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
    },
)

ExperimentConfigOutputTypeDef = TypedDict(
    "ExperimentConfigOutputTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
        "TrialComponentDisplayName": str,
        "RunName": str,
    },
    total=False,
)

ProcessingStoppingConditionOutputTypeDef = TypedDict(
    "ProcessingStoppingConditionOutputTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

DescribeProjectInputRequestTypeDef = TypedDict(
    "DescribeProjectInputRequestTypeDef",
    {
        "ProjectName": str,
    },
)

ServiceCatalogProvisionedProductDetailsTypeDef = TypedDict(
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductStatusMessage": str,
    },
    total=False,
)

DescribeSpaceRequestRequestTypeDef = TypedDict(
    "DescribeSpaceRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
    },
)

DescribeStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "DescribeStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
    },
)

DescribeSubscribedWorkteamRequestRequestTypeDef = TypedDict(
    "DescribeSubscribedWorkteamRequestRequestTypeDef",
    {
        "WorkteamArn": str,
    },
)

_RequiredSubscribedWorkteamTypeDef = TypedDict(
    "_RequiredSubscribedWorkteamTypeDef",
    {
        "WorkteamArn": str,
    },
)
_OptionalSubscribedWorkteamTypeDef = TypedDict(
    "_OptionalSubscribedWorkteamTypeDef",
    {
        "MarketplaceTitle": str,
        "SellerName": str,
        "MarketplaceDescription": str,
        "ListingId": str,
    },
    total=False,
)


class SubscribedWorkteamTypeDef(
    _RequiredSubscribedWorkteamTypeDef, _OptionalSubscribedWorkteamTypeDef
):
    pass


DescribeTrainingJobRequestRequestTypeDef = TypedDict(
    "DescribeTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)

MetricDataTypeDef = TypedDict(
    "MetricDataTypeDef",
    {
        "MetricName": str,
        "Value": float,
        "Timestamp": datetime,
    },
    total=False,
)

_RequiredOutputDataConfigOutputTypeDef = TypedDict(
    "_RequiredOutputDataConfigOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalOutputDataConfigOutputTypeDef = TypedDict(
    "_OptionalOutputDataConfigOutputTypeDef",
    {
        "KmsKeyId": str,
        "CompressionType": OutputCompressionTypeType,
    },
    total=False,
)


class OutputDataConfigOutputTypeDef(
    _RequiredOutputDataConfigOutputTypeDef, _OptionalOutputDataConfigOutputTypeDef
):
    pass


ProfilerConfigOutputTypeDef = TypedDict(
    "ProfilerConfigOutputTypeDef",
    {
        "S3OutputPath": str,
        "ProfilingIntervalInMilliseconds": int,
        "ProfilingParameters": Dict[str, str],
        "DisableProfiler": bool,
    },
    total=False,
)

_RequiredProfilerRuleConfigurationOutputTypeDef = TypedDict(
    "_RequiredProfilerRuleConfigurationOutputTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
    },
)
_OptionalProfilerRuleConfigurationOutputTypeDef = TypedDict(
    "_OptionalProfilerRuleConfigurationOutputTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)


class ProfilerRuleConfigurationOutputTypeDef(
    _RequiredProfilerRuleConfigurationOutputTypeDef, _OptionalProfilerRuleConfigurationOutputTypeDef
):
    pass


ProfilerRuleEvaluationStatusTypeDef = TypedDict(
    "ProfilerRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": RuleEvaluationStatusType,
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

RetryStrategyOutputTypeDef = TypedDict(
    "RetryStrategyOutputTypeDef",
    {
        "MaximumRetryAttempts": int,
    },
)

_RequiredSecondaryStatusTransitionTypeDef = TypedDict(
    "_RequiredSecondaryStatusTransitionTypeDef",
    {
        "Status": SecondaryStatusType,
        "StartTime": datetime,
    },
)
_OptionalSecondaryStatusTransitionTypeDef = TypedDict(
    "_OptionalSecondaryStatusTransitionTypeDef",
    {
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)


class SecondaryStatusTransitionTypeDef(
    _RequiredSecondaryStatusTransitionTypeDef, _OptionalSecondaryStatusTransitionTypeDef
):
    pass


_RequiredTensorBoardOutputConfigOutputTypeDef = TypedDict(
    "_RequiredTensorBoardOutputConfigOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalTensorBoardOutputConfigOutputTypeDef = TypedDict(
    "_OptionalTensorBoardOutputConfigOutputTypeDef",
    {
        "LocalPath": str,
    },
    total=False,
)


class TensorBoardOutputConfigOutputTypeDef(
    _RequiredTensorBoardOutputConfigOutputTypeDef, _OptionalTensorBoardOutputConfigOutputTypeDef
):
    pass


_RequiredWarmPoolStatusTypeDef = TypedDict(
    "_RequiredWarmPoolStatusTypeDef",
    {
        "Status": WarmPoolResourceStatusType,
    },
)
_OptionalWarmPoolStatusTypeDef = TypedDict(
    "_OptionalWarmPoolStatusTypeDef",
    {
        "ResourceRetainedBillableTimeInSeconds": int,
        "ReusedByJob": str,
    },
    total=False,
)


class WarmPoolStatusTypeDef(_RequiredWarmPoolStatusTypeDef, _OptionalWarmPoolStatusTypeDef):
    pass


DescribeTransformJobRequestRequestTypeDef = TypedDict(
    "DescribeTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
    },
)

ModelClientConfigOutputTypeDef = TypedDict(
    "ModelClientConfigOutputTypeDef",
    {
        "InvocationsTimeoutInSeconds": int,
        "InvocationsMaxRetries": int,
    },
    total=False,
)

_RequiredTransformResourcesOutputTypeDef = TypedDict(
    "_RequiredTransformResourcesOutputTypeDef",
    {
        "InstanceType": TransformInstanceTypeType,
        "InstanceCount": int,
    },
)
_OptionalTransformResourcesOutputTypeDef = TypedDict(
    "_OptionalTransformResourcesOutputTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class TransformResourcesOutputTypeDef(
    _RequiredTransformResourcesOutputTypeDef, _OptionalTransformResourcesOutputTypeDef
):
    pass


DescribeTrialComponentRequestRequestTypeDef = TypedDict(
    "DescribeTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)

_RequiredTrialComponentArtifactOutputTypeDef = TypedDict(
    "_RequiredTrialComponentArtifactOutputTypeDef",
    {
        "Value": str,
    },
)
_OptionalTrialComponentArtifactOutputTypeDef = TypedDict(
    "_OptionalTrialComponentArtifactOutputTypeDef",
    {
        "MediaType": str,
    },
    total=False,
)


class TrialComponentArtifactOutputTypeDef(
    _RequiredTrialComponentArtifactOutputTypeDef, _OptionalTrialComponentArtifactOutputTypeDef
):
    pass


TrialComponentMetricSummaryTypeDef = TypedDict(
    "TrialComponentMetricSummaryTypeDef",
    {
        "MetricName": str,
        "SourceArn": str,
        "TimeStamp": datetime,
        "Max": float,
        "Min": float,
        "Last": float,
        "Count": int,
        "Avg": float,
        "StdDev": float,
    },
    total=False,
)

TrialComponentParameterValueOutputTypeDef = TypedDict(
    "TrialComponentParameterValueOutputTypeDef",
    {
        "StringValue": str,
        "NumberValue": float,
    },
    total=False,
)

_RequiredTrialComponentSourceTypeDef = TypedDict(
    "_RequiredTrialComponentSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalTrialComponentSourceTypeDef = TypedDict(
    "_OptionalTrialComponentSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)


class TrialComponentSourceTypeDef(
    _RequiredTrialComponentSourceTypeDef, _OptionalTrialComponentSourceTypeDef
):
    pass


TrialComponentStatusOutputTypeDef = TypedDict(
    "TrialComponentStatusOutputTypeDef",
    {
        "PrimaryStatus": TrialComponentPrimaryStatusType,
        "Message": str,
    },
    total=False,
)

DescribeTrialRequestRequestTypeDef = TypedDict(
    "DescribeTrialRequestRequestTypeDef",
    {
        "TrialName": str,
    },
)

_RequiredTrialSourceTypeDef = TypedDict(
    "_RequiredTrialSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalTrialSourceTypeDef = TypedDict(
    "_OptionalTrialSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)


class TrialSourceTypeDef(_RequiredTrialSourceTypeDef, _OptionalTrialSourceTypeDef):
    pass


DescribeUserProfileRequestRequestTypeDef = TypedDict(
    "DescribeUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)

DescribeWorkforceRequestRequestTypeDef = TypedDict(
    "DescribeWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)

DescribeWorkteamRequestRequestTypeDef = TypedDict(
    "DescribeWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
    },
)

ProductionVariantServerlessUpdateConfigTypeDef = TypedDict(
    "ProductionVariantServerlessUpdateConfigTypeDef",
    {
        "MaxConcurrency": int,
        "ProvisionedConcurrency": int,
    },
    total=False,
)

_RequiredDeviceDeploymentSummaryTypeDef = TypedDict(
    "_RequiredDeviceDeploymentSummaryTypeDef",
    {
        "EdgeDeploymentPlanArn": str,
        "EdgeDeploymentPlanName": str,
        "StageName": str,
        "DeviceName": str,
        "DeviceArn": str,
    },
)
_OptionalDeviceDeploymentSummaryTypeDef = TypedDict(
    "_OptionalDeviceDeploymentSummaryTypeDef",
    {
        "DeployedStageName": str,
        "DeviceFleetName": str,
        "DeviceDeploymentStatus": DeviceDeploymentStatusType,
        "DeviceDeploymentStatusMessage": str,
        "Description": str,
        "DeploymentStartTime": datetime,
    },
    total=False,
)


class DeviceDeploymentSummaryTypeDef(
    _RequiredDeviceDeploymentSummaryTypeDef, _OptionalDeviceDeploymentSummaryTypeDef
):
    pass


_RequiredDeviceFleetSummaryTypeDef = TypedDict(
    "_RequiredDeviceFleetSummaryTypeDef",
    {
        "DeviceFleetArn": str,
        "DeviceFleetName": str,
    },
)
_OptionalDeviceFleetSummaryTypeDef = TypedDict(
    "_OptionalDeviceFleetSummaryTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class DeviceFleetSummaryTypeDef(
    _RequiredDeviceFleetSummaryTypeDef, _OptionalDeviceFleetSummaryTypeDef
):
    pass


DeviceStatsTypeDef = TypedDict(
    "DeviceStatsTypeDef",
    {
        "ConnectedDeviceCount": int,
        "RegisteredDeviceCount": int,
    },
)

EdgeModelSummaryTypeDef = TypedDict(
    "EdgeModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
    },
)

_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef",
    {
        "DeviceName": str,
    },
)
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {
        "Description": str,
        "IotThingName": str,
    },
    total=False,
)


class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass


DisassociateTrialComponentRequestRequestTypeDef = TypedDict(
    "DisassociateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "TrialName": str,
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "Status": DomainStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Url": str,
    },
    total=False,
)

_RequiredFileSourceOutputTypeDef = TypedDict(
    "_RequiredFileSourceOutputTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalFileSourceOutputTypeDef = TypedDict(
    "_OptionalFileSourceOutputTypeDef",
    {
        "ContentType": str,
        "ContentDigest": str,
    },
    total=False,
)


class FileSourceOutputTypeDef(_RequiredFileSourceOutputTypeDef, _OptionalFileSourceOutputTypeDef):
    pass


_RequiredFileSourceTypeDef = TypedDict(
    "_RequiredFileSourceTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalFileSourceTypeDef = TypedDict(
    "_OptionalFileSourceTypeDef",
    {
        "ContentType": str,
        "ContentDigest": str,
    },
    total=False,
)


class FileSourceTypeDef(_RequiredFileSourceTypeDef, _OptionalFileSourceTypeDef):
    pass


EMRStepMetadataTypeDef = TypedDict(
    "EMRStepMetadataTypeDef",
    {
        "ClusterId": str,
        "StepId": str,
        "StepName": str,
        "LogFilePath": str,
    },
    total=False,
)

_RequiredEdgeDeploymentPlanSummaryTypeDef = TypedDict(
    "_RequiredEdgeDeploymentPlanSummaryTypeDef",
    {
        "EdgeDeploymentPlanArn": str,
        "EdgeDeploymentPlanName": str,
        "DeviceFleetName": str,
        "EdgeDeploymentSuccess": int,
        "EdgeDeploymentPending": int,
        "EdgeDeploymentFailed": int,
    },
)
_OptionalEdgeDeploymentPlanSummaryTypeDef = TypedDict(
    "_OptionalEdgeDeploymentPlanSummaryTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class EdgeDeploymentPlanSummaryTypeDef(
    _RequiredEdgeDeploymentPlanSummaryTypeDef, _OptionalEdgeDeploymentPlanSummaryTypeDef
):
    pass


EdgeModelStatTypeDef = TypedDict(
    "EdgeModelStatTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
        "OfflineDeviceCount": int,
        "ConnectedDeviceCount": int,
        "ActiveDeviceCount": int,
        "SamplingDeviceCount": int,
    },
)

_RequiredEdgePackagingJobSummaryTypeDef = TypedDict(
    "_RequiredEdgePackagingJobSummaryTypeDef",
    {
        "EdgePackagingJobArn": str,
        "EdgePackagingJobName": str,
        "EdgePackagingJobStatus": EdgePackagingJobStatusType,
    },
)
_OptionalEdgePackagingJobSummaryTypeDef = TypedDict(
    "_OptionalEdgePackagingJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class EdgePackagingJobSummaryTypeDef(
    _RequiredEdgePackagingJobSummaryTypeDef, _OptionalEdgePackagingJobSummaryTypeDef
):
    pass


EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "AssociationType": AssociationEdgeTypeType,
    },
    total=False,
)

EndpointConfigSummaryTypeDef = TypedDict(
    "EndpointConfigSummaryTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "CreationTime": datetime,
    },
)

EndpointInfoOutputTypeDef = TypedDict(
    "EndpointInfoOutputTypeDef",
    {
        "EndpointName": str,
    },
)

EndpointInfoTypeDef = TypedDict(
    "EndpointInfoTypeDef",
    {
        "EndpointName": str,
    },
)

_RequiredProductionVariantServerlessConfigOutputTypeDef = TypedDict(
    "_RequiredProductionVariantServerlessConfigOutputTypeDef",
    {
        "MemorySizeInMB": int,
        "MaxConcurrency": int,
    },
)
_OptionalProductionVariantServerlessConfigOutputTypeDef = TypedDict(
    "_OptionalProductionVariantServerlessConfigOutputTypeDef",
    {
        "ProvisionedConcurrency": int,
    },
    total=False,
)


class ProductionVariantServerlessConfigOutputTypeDef(
    _RequiredProductionVariantServerlessConfigOutputTypeDef,
    _OptionalProductionVariantServerlessConfigOutputTypeDef,
):
    pass


_RequiredProductionVariantServerlessConfigTypeDef = TypedDict(
    "_RequiredProductionVariantServerlessConfigTypeDef",
    {
        "MemorySizeInMB": int,
        "MaxConcurrency": int,
    },
)
_OptionalProductionVariantServerlessConfigTypeDef = TypedDict(
    "_OptionalProductionVariantServerlessConfigTypeDef",
    {
        "ProvisionedConcurrency": int,
    },
    total=False,
)


class ProductionVariantServerlessConfigTypeDef(
    _RequiredProductionVariantServerlessConfigTypeDef,
    _OptionalProductionVariantServerlessConfigTypeDef,
):
    pass


InferenceMetricsTypeDef = TypedDict(
    "InferenceMetricsTypeDef",
    {
        "MaxInvocations": int,
        "ModelLatency": int,
    },
)

EndpointSummaryTypeDef = TypedDict(
    "EndpointSummaryTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": EndpointStatusType,
    },
)

EnvironmentParameterTypeDef = TypedDict(
    "EnvironmentParameterTypeDef",
    {
        "Key": str,
        "ValueType": str,
        "Value": str,
    },
)

FailStepMetadataTypeDef = TypedDict(
    "FailStepMetadataTypeDef",
    {
        "ErrorMessage": str,
    },
    total=False,
)

FeatureParameterTypeDef = TypedDict(
    "FeatureParameterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

FileSystemConfigOutputTypeDef = TypedDict(
    "FileSystemConfigOutputTypeDef",
    {
        "MountPath": str,
        "DefaultUid": int,
        "DefaultGid": int,
    },
    total=False,
)

FileSystemConfigTypeDef = TypedDict(
    "FileSystemConfigTypeDef",
    {
        "MountPath": str,
        "DefaultUid": int,
        "DefaultGid": int,
    },
    total=False,
)

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "Name": str,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "Operator": OperatorType,
        "Value": str,
    },
    total=False,
)


class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass


_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {
        "MetricName": str,
        "Value": float,
    },
)
_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {
        "Type": HyperParameterTuningJobObjectiveTypeType,
    },
    total=False,
)


class FinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef,
    _OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef,
):
    pass


_RequiredFlowDefinitionSummaryTypeDef = TypedDict(
    "_RequiredFlowDefinitionSummaryTypeDef",
    {
        "FlowDefinitionName": str,
        "FlowDefinitionArn": str,
        "FlowDefinitionStatus": FlowDefinitionStatusType,
        "CreationTime": datetime,
    },
)
_OptionalFlowDefinitionSummaryTypeDef = TypedDict(
    "_OptionalFlowDefinitionSummaryTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class FlowDefinitionSummaryTypeDef(
    _RequiredFlowDefinitionSummaryTypeDef, _OptionalFlowDefinitionSummaryTypeDef
):
    pass


GetDeviceFleetReportRequestRequestTypeDef = TypedDict(
    "GetDeviceFleetReportRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

GetLineageGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetLineageGroupPolicyRequestRequestTypeDef",
    {
        "LineageGroupName": str,
    },
)

GetModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "GetModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

PropertyNameSuggestionTypeDef = TypedDict(
    "PropertyNameSuggestionTypeDef",
    {
        "PropertyName": str,
    },
    total=False,
)

GitConfigForUpdateTypeDef = TypedDict(
    "GitConfigForUpdateTypeDef",
    {
        "SecretArn": str,
    },
    total=False,
)

_RequiredHubContentInfoTypeDef = TypedDict(
    "_RequiredHubContentInfoTypeDef",
    {
        "HubContentName": str,
        "HubContentArn": str,
        "HubContentVersion": str,
        "HubContentType": HubContentTypeType,
        "DocumentSchemaVersion": str,
        "HubContentStatus": HubContentStatusType,
        "CreationTime": datetime,
    },
)
_OptionalHubContentInfoTypeDef = TypedDict(
    "_OptionalHubContentInfoTypeDef",
    {
        "HubContentDisplayName": str,
        "HubContentDescription": str,
        "HubContentSearchKeywords": List[str],
    },
    total=False,
)


class HubContentInfoTypeDef(_RequiredHubContentInfoTypeDef, _OptionalHubContentInfoTypeDef):
    pass


_RequiredHubInfoTypeDef = TypedDict(
    "_RequiredHubInfoTypeDef",
    {
        "HubName": str,
        "HubArn": str,
        "HubStatus": HubStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalHubInfoTypeDef = TypedDict(
    "_OptionalHubInfoTypeDef",
    {
        "HubDisplayName": str,
        "HubDescription": str,
        "HubSearchKeywords": List[str],
    },
    total=False,
)


class HubInfoTypeDef(_RequiredHubInfoTypeDef, _OptionalHubInfoTypeDef):
    pass


HumanLoopActivationConditionsConfigOutputTypeDef = TypedDict(
    "HumanLoopActivationConditionsConfigOutputTypeDef",
    {
        "HumanLoopActivationConditions": str,
    },
)

HumanLoopActivationConditionsConfigTypeDef = TypedDict(
    "HumanLoopActivationConditionsConfigTypeDef",
    {
        "HumanLoopActivationConditions": str,
    },
)

UiConfigOutputTypeDef = TypedDict(
    "UiConfigOutputTypeDef",
    {
        "UiTemplateS3Uri": str,
        "HumanTaskUiArn": str,
    },
    total=False,
)

UiConfigTypeDef = TypedDict(
    "UiConfigTypeDef",
    {
        "UiTemplateS3Uri": str,
        "HumanTaskUiArn": str,
    },
    total=False,
)

HumanTaskUiSummaryTypeDef = TypedDict(
    "HumanTaskUiSummaryTypeDef",
    {
        "HumanTaskUiName": str,
        "HumanTaskUiArn": str,
        "CreationTime": datetime,
    },
)

HyperParameterTuningJobObjectiveOutputTypeDef = TypedDict(
    "HyperParameterTuningJobObjectiveOutputTypeDef",
    {
        "Type": HyperParameterTuningJobObjectiveTypeType,
        "MetricName": str,
    },
)

HyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "HyperParameterTuningJobObjectiveTypeDef",
    {
        "Type": HyperParameterTuningJobObjectiveTypeType,
        "MetricName": str,
    },
)

HyperParameterTuningInstanceConfigOutputTypeDef = TypedDict(
    "HyperParameterTuningInstanceConfigOutputTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeSizeInGB": int,
    },
)

HyperParameterTuningInstanceConfigTypeDef = TypedDict(
    "HyperParameterTuningInstanceConfigTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeSizeInGB": int,
    },
)

_RequiredResourceLimitsOutputTypeDef = TypedDict(
    "_RequiredResourceLimitsOutputTypeDef",
    {
        "MaxParallelTrainingJobs": int,
    },
)
_OptionalResourceLimitsOutputTypeDef = TypedDict(
    "_OptionalResourceLimitsOutputTypeDef",
    {
        "MaxNumberOfTrainingJobs": int,
        "MaxRuntimeInSeconds": int,
    },
    total=False,
)


class ResourceLimitsOutputTypeDef(
    _RequiredResourceLimitsOutputTypeDef, _OptionalResourceLimitsOutputTypeDef
):
    pass


_RequiredResourceLimitsTypeDef = TypedDict(
    "_RequiredResourceLimitsTypeDef",
    {
        "MaxParallelTrainingJobs": int,
    },
)
_OptionalResourceLimitsTypeDef = TypedDict(
    "_OptionalResourceLimitsTypeDef",
    {
        "MaxNumberOfTrainingJobs": int,
        "MaxRuntimeInSeconds": int,
    },
    total=False,
)


class ResourceLimitsTypeDef(_RequiredResourceLimitsTypeDef, _OptionalResourceLimitsTypeDef):
    pass


HyperbandStrategyConfigOutputTypeDef = TypedDict(
    "HyperbandStrategyConfigOutputTypeDef",
    {
        "MinResource": int,
        "MaxResource": int,
    },
    total=False,
)

HyperbandStrategyConfigTypeDef = TypedDict(
    "HyperbandStrategyConfigTypeDef",
    {
        "MinResource": int,
        "MaxResource": int,
    },
    total=False,
)

ParentHyperParameterTuningJobOutputTypeDef = TypedDict(
    "ParentHyperParameterTuningJobOutputTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
    total=False,
)

ParentHyperParameterTuningJobTypeDef = TypedDict(
    "ParentHyperParameterTuningJobTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
    total=False,
)

IamIdentityTypeDef = TypedDict(
    "IamIdentityTypeDef",
    {
        "Arn": str,
        "PrincipalId": str,
        "SourceIdentity": str,
    },
    total=False,
)

RepositoryAuthConfigOutputTypeDef = TypedDict(
    "RepositoryAuthConfigOutputTypeDef",
    {
        "RepositoryCredentialsProviderArn": str,
    },
)

RepositoryAuthConfigTypeDef = TypedDict(
    "RepositoryAuthConfigTypeDef",
    {
        "RepositoryCredentialsProviderArn": str,
    },
)

_RequiredImageTypeDef = TypedDict(
    "_RequiredImageTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": ImageStatusType,
        "LastModifiedTime": datetime,
    },
)
_OptionalImageTypeDef = TypedDict(
    "_OptionalImageTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "FailureReason": str,
    },
    total=False,
)


class ImageTypeDef(_RequiredImageTypeDef, _OptionalImageTypeDef):
    pass


_RequiredImageVersionTypeDef = TypedDict(
    "_RequiredImageVersionTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": ImageVersionStatusType,
        "LastModifiedTime": datetime,
        "Version": int,
    },
)
_OptionalImageVersionTypeDef = TypedDict(
    "_OptionalImageVersionTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class ImageVersionTypeDef(_RequiredImageVersionTypeDef, _OptionalImageVersionTypeDef):
    pass


_RequiredRecommendationMetricsTypeDef = TypedDict(
    "_RequiredRecommendationMetricsTypeDef",
    {
        "CostPerHour": float,
        "CostPerInference": float,
        "MaxInvocations": int,
        "ModelLatency": int,
    },
)
_OptionalRecommendationMetricsTypeDef = TypedDict(
    "_OptionalRecommendationMetricsTypeDef",
    {
        "CpuUtilization": float,
        "MemoryUtilization": float,
        "ModelSetupTime": int,
    },
    total=False,
)


class RecommendationMetricsTypeDef(
    _RequiredRecommendationMetricsTypeDef, _OptionalRecommendationMetricsTypeDef
):
    pass


_RequiredInferenceRecommendationsJobTypeDef = TypedDict(
    "_RequiredInferenceRecommendationsJobTypeDef",
    {
        "JobName": str,
        "JobDescription": str,
        "JobType": RecommendationJobTypeType,
        "JobArn": str,
        "Status": RecommendationJobStatusType,
        "CreationTime": datetime,
        "RoleArn": str,
        "LastModifiedTime": datetime,
    },
)
_OptionalInferenceRecommendationsJobTypeDef = TypedDict(
    "_OptionalInferenceRecommendationsJobTypeDef",
    {
        "CompletionTime": datetime,
        "FailureReason": str,
        "ModelName": str,
        "SamplePayloadUrl": str,
        "ModelPackageVersionArn": str,
    },
    total=False,
)


class InferenceRecommendationsJobTypeDef(
    _RequiredInferenceRecommendationsJobTypeDef, _OptionalInferenceRecommendationsJobTypeDef
):
    pass


InstanceGroupOutputTypeDef = TypedDict(
    "InstanceGroupOutputTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "InstanceGroupName": str,
    },
)

InstanceGroupTypeDef = TypedDict(
    "InstanceGroupTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "InstanceGroupName": str,
    },
)

_RequiredIntegerParameterRangeOutputTypeDef = TypedDict(
    "_RequiredIntegerParameterRangeOutputTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
    },
)
_OptionalIntegerParameterRangeOutputTypeDef = TypedDict(
    "_OptionalIntegerParameterRangeOutputTypeDef",
    {
        "ScalingType": HyperParameterScalingTypeType,
    },
    total=False,
)


class IntegerParameterRangeOutputTypeDef(
    _RequiredIntegerParameterRangeOutputTypeDef, _OptionalIntegerParameterRangeOutputTypeDef
):
    pass


IntegerParameterRangeSpecificationOutputTypeDef = TypedDict(
    "IntegerParameterRangeSpecificationOutputTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

IntegerParameterRangeSpecificationTypeDef = TypedDict(
    "IntegerParameterRangeSpecificationTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

_RequiredIntegerParameterRangeTypeDef = TypedDict(
    "_RequiredIntegerParameterRangeTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
    },
)
_OptionalIntegerParameterRangeTypeDef = TypedDict(
    "_OptionalIntegerParameterRangeTypeDef",
    {
        "ScalingType": HyperParameterScalingTypeType,
    },
    total=False,
)


class IntegerParameterRangeTypeDef(
    _RequiredIntegerParameterRangeTypeDef, _OptionalIntegerParameterRangeTypeDef
):
    pass


_RequiredKernelSpecOutputTypeDef = TypedDict(
    "_RequiredKernelSpecOutputTypeDef",
    {
        "Name": str,
    },
)
_OptionalKernelSpecOutputTypeDef = TypedDict(
    "_OptionalKernelSpecOutputTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class KernelSpecOutputTypeDef(_RequiredKernelSpecOutputTypeDef, _OptionalKernelSpecOutputTypeDef):
    pass


_RequiredKernelSpecTypeDef = TypedDict(
    "_RequiredKernelSpecTypeDef",
    {
        "Name": str,
    },
)
_OptionalKernelSpecTypeDef = TypedDict(
    "_OptionalKernelSpecTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class KernelSpecTypeDef(_RequiredKernelSpecTypeDef, _OptionalKernelSpecTypeDef):
    pass


LabelCountersForWorkteamTypeDef = TypedDict(
    "LabelCountersForWorkteamTypeDef",
    {
        "HumanLabeled": int,
        "PendingHuman": int,
        "Total": int,
    },
    total=False,
)

LabelingJobDataAttributesOutputTypeDef = TypedDict(
    "LabelingJobDataAttributesOutputTypeDef",
    {
        "ContentClassifiers": List[ContentClassifierType],
    },
    total=False,
)

LabelingJobDataAttributesTypeDef = TypedDict(
    "LabelingJobDataAttributesTypeDef",
    {
        "ContentClassifiers": Sequence[ContentClassifierType],
    },
    total=False,
)

LabelingJobS3DataSourceOutputTypeDef = TypedDict(
    "LabelingJobS3DataSourceOutputTypeDef",
    {
        "ManifestS3Uri": str,
    },
)

LabelingJobSnsDataSourceOutputTypeDef = TypedDict(
    "LabelingJobSnsDataSourceOutputTypeDef",
    {
        "SnsTopicArn": str,
    },
)

LabelingJobS3DataSourceTypeDef = TypedDict(
    "LabelingJobS3DataSourceTypeDef",
    {
        "ManifestS3Uri": str,
    },
)

LabelingJobSnsDataSourceTypeDef = TypedDict(
    "LabelingJobSnsDataSourceTypeDef",
    {
        "SnsTopicArn": str,
    },
)

LineageGroupSummaryTypeDef = TypedDict(
    "LineageGroupSummaryTypeDef",
    {
        "LineageGroupArn": str,
        "LineageGroupName": str,
        "DisplayName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
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

ListActionsRequestRequestTypeDef = TypedDict(
    "ListActionsRequestRequestTypeDef",
    {
        "SourceUri": str,
        "ActionType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortActionsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAlgorithmsInputRequestTypeDef = TypedDict(
    "ListAlgorithmsInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": AlgorithmSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

_RequiredListAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListAliasesRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalListAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListAliasesRequestRequestTypeDef",
    {
        "Alias": str,
        "Version": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAliasesRequestRequestTypeDef(
    _RequiredListAliasesRequestRequestTypeDef, _OptionalListAliasesRequestRequestTypeDef
):
    pass


ListAppImageConfigsRequestRequestTypeDef = TypedDict(
    "ListAppImageConfigsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "ModifiedTimeBefore": Union[datetime, str],
        "ModifiedTimeAfter": Union[datetime, str],
        "SortBy": AppImageConfigSortKeyType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
        "SortBy": Literal["CreationTime"],
        "DomainIdEquals": str,
        "UserProfileNameEquals": str,
        "SpaceNameEquals": str,
    },
    total=False,
)

ListArtifactsRequestRequestTypeDef = TypedDict(
    "ListArtifactsRequestRequestTypeDef",
    {
        "SourceUri": str,
        "ArtifactType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": Literal["CreationTime"],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAssociationsRequestRequestTypeDef = TypedDict(
    "ListAssociationsRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "SourceType": str,
        "DestinationType": str,
        "AssociationType": AssociationEdgeTypeType,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortAssociationsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAutoMLJobsRequestRequestTypeDef = TypedDict(
    "ListAutoMLJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": AutoMLJobStatusType,
        "SortOrder": AutoMLSortOrderType,
        "SortBy": AutoMLSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListCandidatesForAutoMLJobRequestRequestTypeDef = TypedDict(
    "_RequiredListCandidatesForAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)
_OptionalListCandidatesForAutoMLJobRequestRequestTypeDef = TypedDict(
    "_OptionalListCandidatesForAutoMLJobRequestRequestTypeDef",
    {
        "StatusEquals": CandidateStatusType,
        "CandidateNameEquals": str,
        "SortOrder": AutoMLSortOrderType,
        "SortBy": CandidateSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListCandidatesForAutoMLJobRequestRequestTypeDef(
    _RequiredListCandidatesForAutoMLJobRequestRequestTypeDef,
    _OptionalListCandidatesForAutoMLJobRequestRequestTypeDef,
):
    pass


ListCodeRepositoriesInputRequestTypeDef = TypedDict(
    "ListCodeRepositoriesInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": CodeRepositorySortByType,
        "SortOrder": CodeRepositorySortOrderType,
    },
    total=False,
)

ListCompilationJobsRequestRequestTypeDef = TypedDict(
    "ListCompilationJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": CompilationJobStatusType,
        "SortBy": ListCompilationJobsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListContextsRequestRequestTypeDef = TypedDict(
    "ListContextsRequestRequestTypeDef",
    {
        "SourceUri": str,
        "ContextType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortContextsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataQualityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

MonitoringJobDefinitionSummaryTypeDef = TypedDict(
    "MonitoringJobDefinitionSummaryTypeDef",
    {
        "MonitoringJobDefinitionName": str,
        "MonitoringJobDefinitionArn": str,
        "CreationTime": datetime,
        "EndpointName": str,
    },
)

ListDeviceFleetsRequestRequestTypeDef = TypedDict(
    "ListDeviceFleetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": ListDeviceFleetsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LatestHeartbeatAfter": Union[datetime, str],
        "ModelName": str,
        "DeviceFleetName": str,
    },
    total=False,
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEdgeDeploymentPlansRequestRequestTypeDef = TypedDict(
    "ListEdgeDeploymentPlansRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "DeviceFleetNameContains": str,
        "SortBy": ListEdgeDeploymentPlansSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListEdgePackagingJobsRequestRequestTypeDef = TypedDict(
    "ListEdgePackagingJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "ModelNameContains": str,
        "StatusEquals": EdgePackagingJobStatusType,
        "SortBy": ListEdgePackagingJobsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListEndpointConfigsInputRequestTypeDef = TypedDict(
    "ListEndpointConfigsInputRequestTypeDef",
    {
        "SortBy": EndpointConfigSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListEndpointsInputRequestTypeDef = TypedDict(
    "ListEndpointsInputRequestTypeDef",
    {
        "SortBy": EndpointSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": EndpointStatusType,
    },
    total=False,
)

ListExperimentsRequestRequestTypeDef = TypedDict(
    "ListExperimentsRequestRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortExperimentsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFeatureGroupsRequestRequestTypeDef = TypedDict(
    "ListFeatureGroupsRequestRequestTypeDef",
    {
        "NameContains": str,
        "FeatureGroupStatusEquals": FeatureGroupStatusType,
        "OfflineStoreStatusEquals": OfflineStoreStatusValueType,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": FeatureGroupSortOrderType,
        "SortBy": FeatureGroupSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFlowDefinitionsRequestRequestTypeDef = TypedDict(
    "ListFlowDefinitionsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListHubContentVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListHubContentVersionsRequestRequestTypeDef",
    {
        "HubName": str,
        "HubContentType": HubContentTypeType,
        "HubContentName": str,
    },
)
_OptionalListHubContentVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListHubContentVersionsRequestRequestTypeDef",
    {
        "MinVersion": str,
        "MaxSchemaVersion": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "SortBy": HubContentSortByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListHubContentVersionsRequestRequestTypeDef(
    _RequiredListHubContentVersionsRequestRequestTypeDef,
    _OptionalListHubContentVersionsRequestRequestTypeDef,
):
    pass


_RequiredListHubContentsRequestRequestTypeDef = TypedDict(
    "_RequiredListHubContentsRequestRequestTypeDef",
    {
        "HubName": str,
        "HubContentType": HubContentTypeType,
    },
)
_OptionalListHubContentsRequestRequestTypeDef = TypedDict(
    "_OptionalListHubContentsRequestRequestTypeDef",
    {
        "NameContains": str,
        "MaxSchemaVersion": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "SortBy": HubContentSortByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListHubContentsRequestRequestTypeDef(
    _RequiredListHubContentsRequestRequestTypeDef, _OptionalListHubContentsRequestRequestTypeDef
):
    pass


ListHubsRequestRequestTypeDef = TypedDict(
    "ListHubsRequestRequestTypeDef",
    {
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "SortBy": HubSortByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListHumanTaskUisRequestRequestTypeDef = TypedDict(
    "ListHumanTaskUisRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListHyperParameterTuningJobsRequestRequestTypeDef = TypedDict(
    "ListHyperParameterTuningJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": HyperParameterTuningJobSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "StatusEquals": HyperParameterTuningJobStatusType,
    },
    total=False,
)

_RequiredListImageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListImageVersionsRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalListImageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListImageVersionsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "SortBy": ImageVersionSortByType,
        "SortOrder": ImageVersionSortOrderType,
    },
    total=False,
)


class ListImageVersionsRequestRequestTypeDef(
    _RequiredListImageVersionsRequestRequestTypeDef, _OptionalListImageVersionsRequestRequestTypeDef
):
    pass


ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ImageSortByType,
        "SortOrder": ImageSortOrderType,
    },
    total=False,
)

ListInferenceExperimentsRequestRequestTypeDef = TypedDict(
    "ListInferenceExperimentsRequestRequestTypeDef",
    {
        "NameContains": str,
        "Type": Literal["ShadowMode"],
        "StatusEquals": InferenceExperimentStatusType,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "SortBy": SortInferenceExperimentsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListInferenceRecommendationsJobStepsRequestRequestTypeDef = TypedDict(
    "_RequiredListInferenceRecommendationsJobStepsRequestRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalListInferenceRecommendationsJobStepsRequestRequestTypeDef = TypedDict(
    "_OptionalListInferenceRecommendationsJobStepsRequestRequestTypeDef",
    {
        "Status": RecommendationJobStatusType,
        "StepType": Literal["BENCHMARK"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListInferenceRecommendationsJobStepsRequestRequestTypeDef(
    _RequiredListInferenceRecommendationsJobStepsRequestRequestTypeDef,
    _OptionalListInferenceRecommendationsJobStepsRequestRequestTypeDef,
):
    pass


ListInferenceRecommendationsJobsRequestRequestTypeDef = TypedDict(
    "ListInferenceRecommendationsJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": RecommendationJobStatusType,
        "SortBy": ListInferenceRecommendationsJobsSortByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "ModelNameEquals": str,
        "ModelPackageVersionArnEquals": str,
    },
    total=False,
)

_RequiredListLabelingJobsForWorkteamRequestRequestTypeDef = TypedDict(
    "_RequiredListLabelingJobsForWorkteamRequestRequestTypeDef",
    {
        "WorkteamArn": str,
    },
)
_OptionalListLabelingJobsForWorkteamRequestRequestTypeDef = TypedDict(
    "_OptionalListLabelingJobsForWorkteamRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "JobReferenceCodeContains": str,
        "SortBy": Literal["CreationTime"],
        "SortOrder": SortOrderType,
    },
    total=False,
)


class ListLabelingJobsForWorkteamRequestRequestTypeDef(
    _RequiredListLabelingJobsForWorkteamRequestRequestTypeDef,
    _OptionalListLabelingJobsForWorkteamRequestRequestTypeDef,
):
    pass


ListLabelingJobsRequestRequestTypeDef = TypedDict(
    "ListLabelingJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "NameContains": str,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "StatusEquals": LabelingJobStatusType,
    },
    total=False,
)

ListLineageGroupsRequestRequestTypeDef = TypedDict(
    "ListLineageGroupsRequestRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortLineageGroupsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListModelBiasJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

_RequiredListModelCardExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListModelCardExportJobsRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalListModelCardExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListModelCardExportJobsRequestRequestTypeDef",
    {
        "ModelCardVersion": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "ModelCardExportJobNameContains": str,
        "StatusEquals": ModelCardExportJobStatusType,
        "SortBy": ModelCardExportJobSortByType,
        "SortOrder": ModelCardExportJobSortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListModelCardExportJobsRequestRequestTypeDef(
    _RequiredListModelCardExportJobsRequestRequestTypeDef,
    _OptionalListModelCardExportJobsRequestRequestTypeDef,
):
    pass


ModelCardExportJobSummaryTypeDef = TypedDict(
    "ModelCardExportJobSummaryTypeDef",
    {
        "ModelCardExportJobName": str,
        "ModelCardExportJobArn": str,
        "Status": ModelCardExportJobStatusType,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "CreatedAt": datetime,
        "LastModifiedAt": datetime,
    },
)

_RequiredListModelCardVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListModelCardVersionsRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalListModelCardVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListModelCardVersionsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "ModelCardStatus": ModelCardStatusType,
        "NextToken": str,
        "SortBy": Literal["Version"],
        "SortOrder": ModelCardSortOrderType,
    },
    total=False,
)


class ListModelCardVersionsRequestRequestTypeDef(
    _RequiredListModelCardVersionsRequestRequestTypeDef,
    _OptionalListModelCardVersionsRequestRequestTypeDef,
):
    pass


_RequiredModelCardVersionSummaryTypeDef = TypedDict(
    "_RequiredModelCardVersionSummaryTypeDef",
    {
        "ModelCardName": str,
        "ModelCardArn": str,
        "ModelCardStatus": ModelCardStatusType,
        "ModelCardVersion": int,
        "CreationTime": datetime,
    },
)
_OptionalModelCardVersionSummaryTypeDef = TypedDict(
    "_OptionalModelCardVersionSummaryTypeDef",
    {
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ModelCardVersionSummaryTypeDef(
    _RequiredModelCardVersionSummaryTypeDef, _OptionalModelCardVersionSummaryTypeDef
):
    pass


ListModelCardsRequestRequestTypeDef = TypedDict(
    "ListModelCardsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "ModelCardStatus": ModelCardStatusType,
        "NextToken": str,
        "SortBy": ModelCardSortByType,
        "SortOrder": ModelCardSortOrderType,
    },
    total=False,
)

_RequiredModelCardSummaryTypeDef = TypedDict(
    "_RequiredModelCardSummaryTypeDef",
    {
        "ModelCardName": str,
        "ModelCardArn": str,
        "ModelCardStatus": ModelCardStatusType,
        "CreationTime": datetime,
    },
)
_OptionalModelCardSummaryTypeDef = TypedDict(
    "_OptionalModelCardSummaryTypeDef",
    {
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ModelCardSummaryTypeDef(_RequiredModelCardSummaryTypeDef, _OptionalModelCardSummaryTypeDef):
    pass


ListModelExplainabilityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ModelMetadataSummaryTypeDef = TypedDict(
    "ModelMetadataSummaryTypeDef",
    {
        "Domain": str,
        "Framework": str,
        "Task": str,
        "Model": str,
        "FrameworkVersion": str,
    },
)

ListModelPackageGroupsInputRequestTypeDef = TypedDict(
    "ListModelPackageGroupsInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ModelPackageGroupSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

_RequiredModelPackageGroupSummaryTypeDef = TypedDict(
    "_RequiredModelPackageGroupSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "CreationTime": datetime,
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
    },
)
_OptionalModelPackageGroupSummaryTypeDef = TypedDict(
    "_OptionalModelPackageGroupSummaryTypeDef",
    {
        "ModelPackageGroupDescription": str,
    },
    total=False,
)


class ModelPackageGroupSummaryTypeDef(
    _RequiredModelPackageGroupSummaryTypeDef, _OptionalModelPackageGroupSummaryTypeDef
):
    pass


ListModelPackagesInputRequestTypeDef = TypedDict(
    "ListModelPackagesInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "ModelPackageGroupName": str,
        "ModelPackageType": ModelPackageTypeType,
        "NextToken": str,
        "SortBy": ModelPackageSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

_RequiredModelPackageSummaryTypeDef = TypedDict(
    "_RequiredModelPackageSummaryTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "ModelPackageStatus": ModelPackageStatusType,
    },
)
_OptionalModelPackageSummaryTypeDef = TypedDict(
    "_OptionalModelPackageSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageDescription": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
    },
    total=False,
)


class ModelPackageSummaryTypeDef(
    _RequiredModelPackageSummaryTypeDef, _OptionalModelPackageSummaryTypeDef
):
    pass


ListModelQualityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelsInputRequestTypeDef = TypedDict(
    "ListModelsInputRequestTypeDef",
    {
        "SortBy": ModelSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "CreationTime": datetime,
    },
)

ListMonitoringAlertHistoryRequestRequestTypeDef = TypedDict(
    "ListMonitoringAlertHistoryRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringAlertName": str,
        "SortBy": MonitoringAlertHistorySortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "StatusEquals": MonitoringAlertStatusType,
    },
    total=False,
)

MonitoringAlertHistorySummaryTypeDef = TypedDict(
    "MonitoringAlertHistorySummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringAlertName": str,
        "CreationTime": datetime,
        "AlertStatus": MonitoringAlertStatusType,
    },
)

_RequiredListMonitoringAlertsRequestRequestTypeDef = TypedDict(
    "_RequiredListMonitoringAlertsRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)
_OptionalListMonitoringAlertsRequestRequestTypeDef = TypedDict(
    "_OptionalListMonitoringAlertsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListMonitoringAlertsRequestRequestTypeDef(
    _RequiredListMonitoringAlertsRequestRequestTypeDef,
    _OptionalListMonitoringAlertsRequestRequestTypeDef,
):
    pass


ListMonitoringExecutionsRequestRequestTypeDef = TypedDict(
    "ListMonitoringExecutionsRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "EndpointName": str,
        "SortBy": MonitoringExecutionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "ScheduledTimeBefore": Union[datetime, str],
        "ScheduledTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": ExecutionStatusType,
        "MonitoringJobDefinitionName": str,
        "MonitoringTypeEquals": MonitoringTypeType,
    },
    total=False,
)

ListMonitoringSchedulesRequestRequestTypeDef = TypedDict(
    "ListMonitoringSchedulesRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringScheduleSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": ScheduleStatusType,
        "MonitoringJobDefinitionName": str,
        "MonitoringTypeEquals": MonitoringTypeType,
    },
    total=False,
)

_RequiredMonitoringScheduleSummaryTypeDef = TypedDict(
    "_RequiredMonitoringScheduleSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleStatus": ScheduleStatusType,
    },
)
_OptionalMonitoringScheduleSummaryTypeDef = TypedDict(
    "_OptionalMonitoringScheduleSummaryTypeDef",
    {
        "EndpointName": str,
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)


class MonitoringScheduleSummaryTypeDef(
    _RequiredMonitoringScheduleSummaryTypeDef, _OptionalMonitoringScheduleSummaryTypeDef
):
    pass


ListNotebookInstanceLifecycleConfigsInputRequestTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": NotebookInstanceLifecycleConfigSortKeyType,
        "SortOrder": NotebookInstanceLifecycleConfigSortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
    },
    total=False,
)

_RequiredNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceLifecycleConfigSummaryTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceLifecycleConfigArn": str,
    },
)
_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class NotebookInstanceLifecycleConfigSummaryTypeDef(
    _RequiredNotebookInstanceLifecycleConfigSummaryTypeDef,
    _OptionalNotebookInstanceLifecycleConfigSummaryTypeDef,
):
    pass


ListNotebookInstancesInputRequestTypeDef = TypedDict(
    "ListNotebookInstancesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": NotebookInstanceSortKeyType,
        "SortOrder": NotebookInstanceSortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": NotebookInstanceStatusType,
        "NotebookInstanceLifecycleConfigNameContains": str,
        "DefaultCodeRepositoryContains": str,
        "AdditionalCodeRepositoryEquals": str,
    },
    total=False,
)

_RequiredNotebookInstanceSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceName": str,
        "NotebookInstanceArn": str,
    },
)
_OptionalNotebookInstanceSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceStatus": NotebookInstanceStatusType,
        "Url": str,
        "InstanceType": InstanceTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
    },
    total=False,
)


class NotebookInstanceSummaryTypeDef(
    _RequiredNotebookInstanceSummaryTypeDef, _OptionalNotebookInstanceSummaryTypeDef
):
    pass


ListPipelineExecutionStepsRequestRequestTypeDef = TypedDict(
    "ListPipelineExecutionStepsRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
    },
    total=False,
)

_RequiredListPipelineExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPipelineExecutionsRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
_OptionalListPipelineExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPipelineExecutionsRequestRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortPipelineExecutionsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPipelineExecutionsRequestRequestTypeDef(
    _RequiredListPipelineExecutionsRequestRequestTypeDef,
    _OptionalListPipelineExecutionsRequestRequestTypeDef,
):
    pass


PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "PipelineExecutionArn": str,
        "StartTime": datetime,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionFailureReason": str,
    },
    total=False,
)

_RequiredListPipelineParametersForExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredListPipelineParametersForExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)
_OptionalListPipelineParametersForExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalListPipelineParametersForExecutionRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPipelineParametersForExecutionRequestRequestTypeDef(
    _RequiredListPipelineParametersForExecutionRequestRequestTypeDef,
    _OptionalListPipelineParametersForExecutionRequestRequestTypeDef,
):
    pass


ParameterOutputTypeDef = TypedDict(
    "ParameterOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "PipelineNamePrefix": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortPipelinesByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastExecutionTime": datetime,
    },
    total=False,
)

ListProcessingJobsRequestRequestTypeDef = TypedDict(
    "ListProcessingJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": ProcessingJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredProcessingJobSummaryTypeDef = TypedDict(
    "_RequiredProcessingJobSummaryTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingJobArn": str,
        "CreationTime": datetime,
        "ProcessingJobStatus": ProcessingJobStatusType,
    },
)
_OptionalProcessingJobSummaryTypeDef = TypedDict(
    "_OptionalProcessingJobSummaryTypeDef",
    {
        "ProcessingEndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ExitMessage": str,
    },
    total=False,
)


class ProcessingJobSummaryTypeDef(
    _RequiredProcessingJobSummaryTypeDef, _OptionalProcessingJobSummaryTypeDef
):
    pass


ListProjectsInputRequestTypeDef = TypedDict(
    "ListProjectsInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ProjectSortByType,
        "SortOrder": ProjectSortOrderType,
    },
    total=False,
)

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "ProjectName": str,
        "ProjectArn": str,
        "ProjectId": str,
        "CreationTime": datetime,
        "ProjectStatus": ProjectStatusType,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "ProjectDescription": str,
    },
    total=False,
)


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass


ListResourceCatalogsRequestRequestTypeDef = TypedDict(
    "ListResourceCatalogsRequestRequestTypeDef",
    {
        "NameContains": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": ResourceCatalogSortOrderType,
        "SortBy": Literal["CreationTime"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ResourceCatalogTypeDef = TypedDict(
    "ResourceCatalogTypeDef",
    {
        "ResourceCatalogArn": str,
        "ResourceCatalogName": str,
        "Description": str,
        "CreationTime": datetime,
    },
)

ListSpacesRequestRequestTypeDef = TypedDict(
    "ListSpacesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
        "SortBy": SpaceSortKeyType,
        "DomainIdEquals": str,
        "SpaceNameContains": str,
    },
    total=False,
)

SpaceDetailsTypeDef = TypedDict(
    "SpaceDetailsTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
        "Status": SpaceStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredListStageDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredListStageDevicesRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)
_OptionalListStageDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalListStageDevicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ExcludeDevicesDeployedInOtherStage": bool,
    },
    total=False,
)


class ListStageDevicesRequestRequestTypeDef(
    _RequiredListStageDevicesRequestRequestTypeDef, _OptionalListStageDevicesRequestRequestTypeDef
):
    pass


ListStudioLifecycleConfigsRequestRequestTypeDef = TypedDict(
    "ListStudioLifecycleConfigsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "NameContains": str,
        "AppTypeEquals": StudioLifecycleConfigAppTypeType,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "ModifiedTimeBefore": Union[datetime, str],
        "ModifiedTimeAfter": Union[datetime, str],
        "SortBy": StudioLifecycleConfigSortKeyType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

StudioLifecycleConfigDetailsTypeDef = TypedDict(
    "StudioLifecycleConfigDetailsTypeDef",
    {
        "StudioLifecycleConfigArn": str,
        "StudioLifecycleConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "StudioLifecycleConfigAppType": StudioLifecycleConfigAppTypeType,
    },
    total=False,
)

ListSubscribedWorkteamsRequestRequestTypeDef = TypedDict(
    "ListSubscribedWorkteamsRequestRequestTypeDef",
    {
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListTagsInputRequestTypeDef = TypedDict(
    "_RequiredListTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsInputRequestTypeDef = TypedDict(
    "_OptionalListTagsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsInputRequestTypeDef(
    _RequiredListTagsInputRequestTypeDef, _OptionalListTagsInputRequestTypeDef
):
    pass


_RequiredListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "_RequiredListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)
_OptionalListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "_OptionalListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StatusEquals": TrainingJobStatusType,
        "SortBy": TrainingJobSortByOptionsType,
        "SortOrder": SortOrderType,
    },
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef(
    _RequiredListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef,
    _OptionalListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef,
):
    pass


ListTrainingJobsRequestRequestTypeDef = TypedDict(
    "ListTrainingJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": TrainingJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "WarmPoolStatusEquals": WarmPoolResourceStatusType,
    },
    total=False,
)

ListTransformJobsRequestRequestTypeDef = TypedDict(
    "ListTransformJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": TransformJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredTransformJobSummaryTypeDef = TypedDict(
    "_RequiredTransformJobSummaryTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformJobStatus": TransformJobStatusType,
    },
)
_OptionalTransformJobSummaryTypeDef = TypedDict(
    "_OptionalTransformJobSummaryTypeDef",
    {
        "TransformEndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)


class TransformJobSummaryTypeDef(
    _RequiredTransformJobSummaryTypeDef, _OptionalTransformJobSummaryTypeDef
):
    pass


ListTrialComponentsRequestRequestTypeDef = TypedDict(
    "ListTrialComponentsRequestRequestTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
        "SourceArn": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortTrialComponentsByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTrialsRequestRequestTypeDef = TypedDict(
    "ListTrialsRequestRequestTypeDef",
    {
        "ExperimentName": str,
        "TrialComponentName": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortTrialsByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListUserProfilesRequestRequestTypeDef = TypedDict(
    "ListUserProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
        "SortBy": UserProfileSortKeyType,
        "DomainIdEquals": str,
        "UserProfileNameContains": str,
    },
    total=False,
)

UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "Status": UserProfileStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ListWorkforcesRequestRequestTypeDef = TypedDict(
    "ListWorkforcesRequestRequestTypeDef",
    {
        "SortBy": ListWorkforcesSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkteamsRequestRequestTypeDef = TypedDict(
    "ListWorkteamsRequestRequestTypeDef",
    {
        "SortBy": ListWorkteamsSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

OidcMemberDefinitionOutputTypeDef = TypedDict(
    "OidcMemberDefinitionOutputTypeDef",
    {
        "Groups": List[str],
    },
)

OidcMemberDefinitionTypeDef = TypedDict(
    "OidcMemberDefinitionTypeDef",
    {
        "Groups": Sequence[str],
    },
)

MonitoringGroundTruthS3InputOutputTypeDef = TypedDict(
    "MonitoringGroundTruthS3InputOutputTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringGroundTruthS3InputTypeDef = TypedDict(
    "MonitoringGroundTruthS3InputTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

ModelDashboardEndpointTypeDef = TypedDict(
    "ModelDashboardEndpointTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": EndpointStatusType,
    },
)

ModelDashboardIndicatorActionTypeDef = TypedDict(
    "ModelDashboardIndicatorActionTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

S3ModelDataSourceOutputTypeDef = TypedDict(
    "S3ModelDataSourceOutputTypeDef",
    {
        "S3Uri": str,
        "S3DataType": S3ModelDataTypeType,
        "CompressionType": ModelCompressionTypeType,
    },
)

S3ModelDataSourceTypeDef = TypedDict(
    "S3ModelDataSourceTypeDef",
    {
        "S3Uri": str,
        "S3DataType": S3ModelDataTypeType,
        "CompressionType": ModelCompressionTypeType,
    },
)

RealTimeInferenceConfigOutputTypeDef = TypedDict(
    "RealTimeInferenceConfigOutputTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "InstanceCount": int,
    },
)

RealTimeInferenceConfigTypeDef = TypedDict(
    "RealTimeInferenceConfigTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "InstanceCount": int,
    },
)

ModelInputOutputTypeDef = TypedDict(
    "ModelInputOutputTypeDef",
    {
        "DataInputConfig": str,
    },
)

ModelInputTypeDef = TypedDict(
    "ModelInputTypeDef",
    {
        "DataInputConfig": str,
    },
)

ModelLatencyThresholdOutputTypeDef = TypedDict(
    "ModelLatencyThresholdOutputTypeDef",
    {
        "Percentile": str,
        "ValueInMilliseconds": int,
    },
    total=False,
)

ModelLatencyThresholdTypeDef = TypedDict(
    "ModelLatencyThresholdTypeDef",
    {
        "Percentile": str,
        "ValueInMilliseconds": int,
    },
    total=False,
)

ModelMetadataFilterTypeDef = TypedDict(
    "ModelMetadataFilterTypeDef",
    {
        "Name": ModelMetadataFilterTypeType,
        "Value": str,
    },
)

_RequiredModelPackageStatusItemTypeDef = TypedDict(
    "_RequiredModelPackageStatusItemTypeDef",
    {
        "Name": str,
        "Status": DetailedModelPackageStatusType,
    },
)
_OptionalModelPackageStatusItemTypeDef = TypedDict(
    "_OptionalModelPackageStatusItemTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)


class ModelPackageStatusItemTypeDef(
    _RequiredModelPackageStatusItemTypeDef, _OptionalModelPackageStatusItemTypeDef
):
    pass


ModelStepMetadataTypeDef = TypedDict(
    "ModelStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredMonitoringAppSpecificationOutputTypeDef = TypedDict(
    "_RequiredMonitoringAppSpecificationOutputTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalMonitoringAppSpecificationOutputTypeDef = TypedDict(
    "_OptionalMonitoringAppSpecificationOutputTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
    },
    total=False,
)


class MonitoringAppSpecificationOutputTypeDef(
    _RequiredMonitoringAppSpecificationOutputTypeDef,
    _OptionalMonitoringAppSpecificationOutputTypeDef,
):
    pass


_RequiredMonitoringAppSpecificationTypeDef = TypedDict(
    "_RequiredMonitoringAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalMonitoringAppSpecificationTypeDef = TypedDict(
    "_OptionalMonitoringAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": Sequence[str],
        "ContainerArguments": Sequence[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
    },
    total=False,
)


class MonitoringAppSpecificationTypeDef(
    _RequiredMonitoringAppSpecificationTypeDef, _OptionalMonitoringAppSpecificationTypeDef
):
    pass


_RequiredMonitoringClusterConfigOutputTypeDef = TypedDict(
    "_RequiredMonitoringClusterConfigOutputTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
    },
)
_OptionalMonitoringClusterConfigOutputTypeDef = TypedDict(
    "_OptionalMonitoringClusterConfigOutputTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class MonitoringClusterConfigOutputTypeDef(
    _RequiredMonitoringClusterConfigOutputTypeDef, _OptionalMonitoringClusterConfigOutputTypeDef
):
    pass


_RequiredMonitoringClusterConfigTypeDef = TypedDict(
    "_RequiredMonitoringClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
    },
)
_OptionalMonitoringClusterConfigTypeDef = TypedDict(
    "_OptionalMonitoringClusterConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class MonitoringClusterConfigTypeDef(
    _RequiredMonitoringClusterConfigTypeDef, _OptionalMonitoringClusterConfigTypeDef
):
    pass


MonitoringCsvDatasetFormatOutputTypeDef = TypedDict(
    "MonitoringCsvDatasetFormatOutputTypeDef",
    {
        "Header": bool,
    },
    total=False,
)

MonitoringCsvDatasetFormatTypeDef = TypedDict(
    "MonitoringCsvDatasetFormatTypeDef",
    {
        "Header": bool,
    },
    total=False,
)

MonitoringJsonDatasetFormatOutputTypeDef = TypedDict(
    "MonitoringJsonDatasetFormatOutputTypeDef",
    {
        "Line": bool,
    },
    total=False,
)

MonitoringJsonDatasetFormatTypeDef = TypedDict(
    "MonitoringJsonDatasetFormatTypeDef",
    {
        "Line": bool,
    },
    total=False,
)

_RequiredMonitoringS3OutputTypeDef = TypedDict(
    "_RequiredMonitoringS3OutputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
    },
)
_OptionalMonitoringS3OutputTypeDef = TypedDict(
    "_OptionalMonitoringS3OutputTypeDef",
    {
        "S3UploadMode": ProcessingS3UploadModeType,
    },
    total=False,
)


class MonitoringS3OutputTypeDef(
    _RequiredMonitoringS3OutputTypeDef, _OptionalMonitoringS3OutputTypeDef
):
    pass


ScheduleConfigOutputTypeDef = TypedDict(
    "ScheduleConfigOutputTypeDef",
    {
        "ScheduleExpression": str,
    },
)

ScheduleConfigTypeDef = TypedDict(
    "ScheduleConfigTypeDef",
    {
        "ScheduleExpression": str,
    },
)

NotificationConfigurationOutputTypeDef = TypedDict(
    "NotificationConfigurationOutputTypeDef",
    {
        "NotificationTopicArn": str,
    },
    total=False,
)

_RequiredS3StorageConfigOutputTypeDef = TypedDict(
    "_RequiredS3StorageConfigOutputTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalS3StorageConfigOutputTypeDef = TypedDict(
    "_OptionalS3StorageConfigOutputTypeDef",
    {
        "KmsKeyId": str,
        "ResolvedOutputS3Uri": str,
    },
    total=False,
)


class S3StorageConfigOutputTypeDef(
    _RequiredS3StorageConfigOutputTypeDef, _OptionalS3StorageConfigOutputTypeDef
):
    pass


_RequiredS3StorageConfigTypeDef = TypedDict(
    "_RequiredS3StorageConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalS3StorageConfigTypeDef = TypedDict(
    "_OptionalS3StorageConfigTypeDef",
    {
        "KmsKeyId": str,
        "ResolvedOutputS3Uri": str,
    },
    total=False,
)


class S3StorageConfigTypeDef(_RequiredS3StorageConfigTypeDef, _OptionalS3StorageConfigTypeDef):
    pass


OidcConfigForResponseTypeDef = TypedDict(
    "OidcConfigForResponseTypeDef",
    {
        "ClientId": str,
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "LogoutEndpoint": str,
        "JwksUri": str,
    },
    total=False,
)

OnlineStoreSecurityConfigOutputTypeDef = TypedDict(
    "OnlineStoreSecurityConfigOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

TtlDurationOutputTypeDef = TypedDict(
    "TtlDurationOutputTypeDef",
    {
        "Unit": TtlDurationUnitType,
        "Value": int,
    },
    total=False,
)

OnlineStoreSecurityConfigTypeDef = TypedDict(
    "OnlineStoreSecurityConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

TtlDurationTypeDef = TypedDict(
    "TtlDurationTypeDef",
    {
        "Unit": TtlDurationUnitType,
        "Value": int,
    },
    total=False,
)

_RequiredTargetPlatformOutputTypeDef = TypedDict(
    "_RequiredTargetPlatformOutputTypeDef",
    {
        "Os": TargetPlatformOsType,
        "Arch": TargetPlatformArchType,
    },
)
_OptionalTargetPlatformOutputTypeDef = TypedDict(
    "_OptionalTargetPlatformOutputTypeDef",
    {
        "Accelerator": TargetPlatformAcceleratorType,
    },
    total=False,
)


class TargetPlatformOutputTypeDef(
    _RequiredTargetPlatformOutputTypeDef, _OptionalTargetPlatformOutputTypeDef
):
    pass


_RequiredTargetPlatformTypeDef = TypedDict(
    "_RequiredTargetPlatformTypeDef",
    {
        "Os": TargetPlatformOsType,
        "Arch": TargetPlatformArchType,
    },
)
_OptionalTargetPlatformTypeDef = TypedDict(
    "_OptionalTargetPlatformTypeDef",
    {
        "Accelerator": TargetPlatformAcceleratorType,
    },
    total=False,
)


class TargetPlatformTypeDef(_RequiredTargetPlatformTypeDef, _OptionalTargetPlatformTypeDef):
    pass


OutputParameterTypeDef = TypedDict(
    "OutputParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "TrialName": str,
        "ExperimentName": str,
    },
    total=False,
)

_RequiredProductionVariantStatusTypeDef = TypedDict(
    "_RequiredProductionVariantStatusTypeDef",
    {
        "Status": VariantStatusType,
    },
)
_OptionalProductionVariantStatusTypeDef = TypedDict(
    "_OptionalProductionVariantStatusTypeDef",
    {
        "StatusMessage": str,
        "StartTime": datetime,
    },
    total=False,
)


class ProductionVariantStatusTypeDef(
    _RequiredProductionVariantStatusTypeDef, _OptionalProductionVariantStatusTypeDef
):
    pass


PhaseOutputTypeDef = TypedDict(
    "PhaseOutputTypeDef",
    {
        "InitialNumberOfUsers": int,
        "SpawnRate": int,
        "DurationInSeconds": int,
    },
    total=False,
)

PhaseTypeDef = TypedDict(
    "PhaseTypeDef",
    {
        "InitialNumberOfUsers": int,
        "SpawnRate": int,
        "DurationInSeconds": int,
    },
    total=False,
)

ProcessingJobStepMetadataTypeDef = TypedDict(
    "ProcessingJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

QualityCheckStepMetadataTypeDef = TypedDict(
    "QualityCheckStepMetadataTypeDef",
    {
        "CheckType": str,
        "BaselineUsedForDriftCheckStatistics": str,
        "BaselineUsedForDriftCheckConstraints": str,
        "CalculatedBaselineStatistics": str,
        "CalculatedBaselineConstraints": str,
        "ModelPackageGroupName": str,
        "ViolationReport": str,
        "CheckJobArn": str,
        "SkipCheck": bool,
        "RegisterNewBaseline": bool,
    },
    total=False,
)

RegisterModelStepMetadataTypeDef = TypedDict(
    "RegisterModelStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

TrainingJobStepMetadataTypeDef = TypedDict(
    "TrainingJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

TransformJobStepMetadataTypeDef = TypedDict(
    "TransformJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

TuningJobStepMetaDataTypeDef = TypedDict(
    "TuningJobStepMetaDataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

SelectiveExecutionResultTypeDef = TypedDict(
    "SelectiveExecutionResultTypeDef",
    {
        "SourcePipelineExecutionArn": str,
    },
    total=False,
)

_RequiredProcessingClusterConfigOutputTypeDef = TypedDict(
    "_RequiredProcessingClusterConfigOutputTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
    },
)
_OptionalProcessingClusterConfigOutputTypeDef = TypedDict(
    "_OptionalProcessingClusterConfigOutputTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ProcessingClusterConfigOutputTypeDef(
    _RequiredProcessingClusterConfigOutputTypeDef, _OptionalProcessingClusterConfigOutputTypeDef
):
    pass


_RequiredProcessingClusterConfigTypeDef = TypedDict(
    "_RequiredProcessingClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
    },
)
_OptionalProcessingClusterConfigTypeDef = TypedDict(
    "_OptionalProcessingClusterConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ProcessingClusterConfigTypeDef(
    _RequiredProcessingClusterConfigTypeDef, _OptionalProcessingClusterConfigTypeDef
):
    pass


ProcessingFeatureStoreOutputTypeDef = TypedDict(
    "ProcessingFeatureStoreOutputTypeDef",
    {
        "FeatureGroupName": str,
    },
)

_RequiredProcessingS3InputOutputTypeDef = TypedDict(
    "_RequiredProcessingS3InputOutputTypeDef",
    {
        "S3Uri": str,
        "S3DataType": ProcessingS3DataTypeType,
    },
)
_OptionalProcessingS3InputOutputTypeDef = TypedDict(
    "_OptionalProcessingS3InputOutputTypeDef",
    {
        "LocalPath": str,
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "S3CompressionType": ProcessingS3CompressionTypeType,
    },
    total=False,
)


class ProcessingS3InputOutputTypeDef(
    _RequiredProcessingS3InputOutputTypeDef, _OptionalProcessingS3InputOutputTypeDef
):
    pass


_RequiredProcessingS3InputTypeDef = TypedDict(
    "_RequiredProcessingS3InputTypeDef",
    {
        "S3Uri": str,
        "S3DataType": ProcessingS3DataTypeType,
    },
)
_OptionalProcessingS3InputTypeDef = TypedDict(
    "_OptionalProcessingS3InputTypeDef",
    {
        "LocalPath": str,
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "S3CompressionType": ProcessingS3CompressionTypeType,
    },
    total=False,
)


class ProcessingS3InputTypeDef(
    _RequiredProcessingS3InputTypeDef, _OptionalProcessingS3InputTypeDef
):
    pass


ProcessingS3OutputTypeDef = TypedDict(
    "ProcessingS3OutputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
        "S3UploadMode": ProcessingS3UploadModeType,
    },
)

_RequiredProductionVariantCoreDumpConfigOutputTypeDef = TypedDict(
    "_RequiredProductionVariantCoreDumpConfigOutputTypeDef",
    {
        "DestinationS3Uri": str,
    },
)
_OptionalProductionVariantCoreDumpConfigOutputTypeDef = TypedDict(
    "_OptionalProductionVariantCoreDumpConfigOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class ProductionVariantCoreDumpConfigOutputTypeDef(
    _RequiredProductionVariantCoreDumpConfigOutputTypeDef,
    _OptionalProductionVariantCoreDumpConfigOutputTypeDef,
):
    pass


_RequiredProductionVariantCoreDumpConfigTypeDef = TypedDict(
    "_RequiredProductionVariantCoreDumpConfigTypeDef",
    {
        "DestinationS3Uri": str,
    },
)
_OptionalProductionVariantCoreDumpConfigTypeDef = TypedDict(
    "_OptionalProductionVariantCoreDumpConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class ProductionVariantCoreDumpConfigTypeDef(
    _RequiredProductionVariantCoreDumpConfigTypeDef, _OptionalProductionVariantCoreDumpConfigTypeDef
):
    pass


ProfilerConfigForUpdateTypeDef = TypedDict(
    "ProfilerConfigForUpdateTypeDef",
    {
        "S3OutputPath": str,
        "ProfilingIntervalInMilliseconds": int,
        "ProfilingParameters": Mapping[str, str],
        "DisableProfiler": bool,
    },
    total=False,
)

PropertyNameQueryTypeDef = TypedDict(
    "PropertyNameQueryTypeDef",
    {
        "PropertyNameHint": str,
    },
)

ProvisioningParameterOutputTypeDef = TypedDict(
    "ProvisioningParameterOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

USDOutputTypeDef = TypedDict(
    "USDOutputTypeDef",
    {
        "Dollars": int,
        "Cents": int,
        "TenthFractionsOfACent": int,
    },
    total=False,
)

USDTypeDef = TypedDict(
    "USDTypeDef",
    {
        "Dollars": int,
        "Cents": int,
        "TenthFractionsOfACent": int,
    },
    total=False,
)

PutModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "PutModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
        "ResourcePolicy": str,
    },
)

QueryFiltersTypeDef = TypedDict(
    "QueryFiltersTypeDef",
    {
        "Types": Sequence[str],
        "LineageTypes": Sequence[LineageTypeType],
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
        "ModifiedBefore": Union[datetime, str],
        "ModifiedAfter": Union[datetime, str],
        "Properties": Mapping[str, str],
    },
    total=False,
)

VertexTypeDef = TypedDict(
    "VertexTypeDef",
    {
        "Arn": str,
        "Type": str,
        "LineageType": LineageTypeType,
    },
    total=False,
)

RStudioServerProAppSettingsOutputTypeDef = TypedDict(
    "RStudioServerProAppSettingsOutputTypeDef",
    {
        "AccessStatus": RStudioServerProAccessStatusType,
        "UserGroup": RStudioServerProUserGroupType,
    },
    total=False,
)

RStudioServerProAppSettingsTypeDef = TypedDict(
    "RStudioServerProAppSettingsTypeDef",
    {
        "AccessStatus": RStudioServerProAccessStatusType,
        "UserGroup": RStudioServerProUserGroupType,
    },
    total=False,
)

RecommendationJobCompiledOutputConfigTypeDef = TypedDict(
    "RecommendationJobCompiledOutputConfigTypeDef",
    {
        "S3OutputUri": str,
    },
    total=False,
)

RecommendationJobPayloadConfigOutputTypeDef = TypedDict(
    "RecommendationJobPayloadConfigOutputTypeDef",
    {
        "SamplePayloadUrl": str,
        "SupportedContentTypes": List[str],
    },
    total=False,
)

RecommendationJobPayloadConfigTypeDef = TypedDict(
    "RecommendationJobPayloadConfigTypeDef",
    {
        "SamplePayloadUrl": str,
        "SupportedContentTypes": Sequence[str],
    },
    total=False,
)

RecommendationJobResourceLimitOutputTypeDef = TypedDict(
    "RecommendationJobResourceLimitOutputTypeDef",
    {
        "MaxNumberOfTests": int,
        "MaxParallelOfTests": int,
    },
    total=False,
)

RecommendationJobVpcConfigOutputTypeDef = TypedDict(
    "RecommendationJobVpcConfigOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)

RecommendationJobResourceLimitTypeDef = TypedDict(
    "RecommendationJobResourceLimitTypeDef",
    {
        "MaxNumberOfTests": int,
        "MaxParallelOfTests": int,
    },
    total=False,
)

RecommendationJobVpcConfigTypeDef = TypedDict(
    "RecommendationJobVpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "Subnets": Sequence[str],
    },
)

RenderableTaskTypeDef = TypedDict(
    "RenderableTaskTypeDef",
    {
        "Input": str,
    },
)

RenderingErrorTypeDef = TypedDict(
    "RenderingErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
)

ResourceConfigForUpdateTypeDef = TypedDict(
    "ResourceConfigForUpdateTypeDef",
    {
        "KeepAlivePeriodInSeconds": int,
    },
)

_RequiredSearchRequestRequestTypeDef = TypedDict(
    "_RequiredSearchRequestRequestTypeDef",
    {
        "Resource": ResourceTypeType,
    },
)
_OptionalSearchRequestRequestTypeDef = TypedDict(
    "_OptionalSearchRequestRequestTypeDef",
    {
        "SearchExpression": "SearchExpressionTypeDef",
        "SortBy": str,
        "SortOrder": SearchSortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "CrossAccountFilterOption": CrossAccountFilterOptionType,
    },
    total=False,
)


class SearchRequestRequestTypeDef(
    _RequiredSearchRequestRequestTypeDef, _OptionalSearchRequestRequestTypeDef
):
    pass


SelectedStepOutputTypeDef = TypedDict(
    "SelectedStepOutputTypeDef",
    {
        "StepName": str,
    },
)

SelectedStepTypeDef = TypedDict(
    "SelectedStepTypeDef",
    {
        "StepName": str,
    },
)

_RequiredSendPipelineExecutionStepFailureRequestRequestTypeDef = TypedDict(
    "_RequiredSendPipelineExecutionStepFailureRequestRequestTypeDef",
    {
        "CallbackToken": str,
    },
)
_OptionalSendPipelineExecutionStepFailureRequestRequestTypeDef = TypedDict(
    "_OptionalSendPipelineExecutionStepFailureRequestRequestTypeDef",
    {
        "FailureReason": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class SendPipelineExecutionStepFailureRequestRequestTypeDef(
    _RequiredSendPipelineExecutionStepFailureRequestRequestTypeDef,
    _OptionalSendPipelineExecutionStepFailureRequestRequestTypeDef,
):
    pass


ShadowModelVariantConfigOutputTypeDef = TypedDict(
    "ShadowModelVariantConfigOutputTypeDef",
    {
        "ShadowModelVariantName": str,
        "SamplingPercentage": int,
    },
)

ShadowModelVariantConfigTypeDef = TypedDict(
    "ShadowModelVariantConfigTypeDef",
    {
        "ShadowModelVariantName": str,
        "SamplingPercentage": int,
    },
)

SharingSettingsOutputTypeDef = TypedDict(
    "SharingSettingsOutputTypeDef",
    {
        "NotebookOutputOption": NotebookOutputOptionType,
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

SharingSettingsTypeDef = TypedDict(
    "SharingSettingsTypeDef",
    {
        "NotebookOutputOption": NotebookOutputOptionType,
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

_RequiredSourceAlgorithmOutputTypeDef = TypedDict(
    "_RequiredSourceAlgorithmOutputTypeDef",
    {
        "AlgorithmName": str,
    },
)
_OptionalSourceAlgorithmOutputTypeDef = TypedDict(
    "_OptionalSourceAlgorithmOutputTypeDef",
    {
        "ModelDataUrl": str,
    },
    total=False,
)


class SourceAlgorithmOutputTypeDef(
    _RequiredSourceAlgorithmOutputTypeDef, _OptionalSourceAlgorithmOutputTypeDef
):
    pass


_RequiredSourceAlgorithmTypeDef = TypedDict(
    "_RequiredSourceAlgorithmTypeDef",
    {
        "AlgorithmName": str,
    },
)
_OptionalSourceAlgorithmTypeDef = TypedDict(
    "_OptionalSourceAlgorithmTypeDef",
    {
        "ModelDataUrl": str,
    },
    total=False,
)


class SourceAlgorithmTypeDef(_RequiredSourceAlgorithmTypeDef, _OptionalSourceAlgorithmTypeDef):
    pass


SourceIpConfigOutputTypeDef = TypedDict(
    "SourceIpConfigOutputTypeDef",
    {
        "Cidrs": List[str],
    },
)

StartEdgeDeploymentStageRequestRequestTypeDef = TypedDict(
    "StartEdgeDeploymentStageRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)

StartInferenceExperimentRequestRequestTypeDef = TypedDict(
    "StartInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "StartMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

StartNotebookInstanceInputRequestTypeDef = TypedDict(
    "StartNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

StopAutoMLJobRequestRequestTypeDef = TypedDict(
    "StopAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

StopCompilationJobRequestRequestTypeDef = TypedDict(
    "StopCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
    },
)

StopEdgeDeploymentStageRequestRequestTypeDef = TypedDict(
    "StopEdgeDeploymentStageRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)

StopEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "StopEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
    },
)

StopHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "StopHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)

StopInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "StopInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

StopLabelingJobRequestRequestTypeDef = TypedDict(
    "StopLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
    },
)

StopMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "StopMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

StopNotebookInstanceInputRequestTypeDef = TypedDict(
    "StopNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

StopPipelineExecutionRequestRequestTypeDef = TypedDict(
    "StopPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "ClientRequestToken": str,
    },
)

StopProcessingJobRequestRequestTypeDef = TypedDict(
    "StopProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
    },
)

StopTrainingJobRequestRequestTypeDef = TypedDict(
    "StopTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)

StopTransformJobRequestRequestTypeDef = TypedDict(
    "StopTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
    },
)

_RequiredTimeSeriesConfigOutputTypeDef = TypedDict(
    "_RequiredTimeSeriesConfigOutputTypeDef",
    {
        "TargetAttributeName": str,
        "TimestampAttributeName": str,
        "ItemIdentifierAttributeName": str,
    },
)
_OptionalTimeSeriesConfigOutputTypeDef = TypedDict(
    "_OptionalTimeSeriesConfigOutputTypeDef",
    {
        "GroupingAttributeNames": List[str],
    },
    total=False,
)


class TimeSeriesConfigOutputTypeDef(
    _RequiredTimeSeriesConfigOutputTypeDef, _OptionalTimeSeriesConfigOutputTypeDef
):
    pass


_RequiredTimeSeriesConfigTypeDef = TypedDict(
    "_RequiredTimeSeriesConfigTypeDef",
    {
        "TargetAttributeName": str,
        "TimestampAttributeName": str,
        "ItemIdentifierAttributeName": str,
    },
)
_OptionalTimeSeriesConfigTypeDef = TypedDict(
    "_OptionalTimeSeriesConfigTypeDef",
    {
        "GroupingAttributeNames": Sequence[str],
    },
    total=False,
)


class TimeSeriesConfigTypeDef(_RequiredTimeSeriesConfigTypeDef, _OptionalTimeSeriesConfigTypeDef):
    pass


TimeSeriesTransformationsOutputTypeDef = TypedDict(
    "TimeSeriesTransformationsOutputTypeDef",
    {
        "Filling": Dict[str, Dict[FillingTypeType, str]],
        "Aggregation": Dict[str, AggregationTransformationValueType],
    },
    total=False,
)

TimeSeriesTransformationsTypeDef = TypedDict(
    "TimeSeriesTransformationsTypeDef",
    {
        "Filling": Mapping[str, Mapping[FillingTypeType, str]],
        "Aggregation": Mapping[str, AggregationTransformationValueType],
    },
    total=False,
)

TrainingRepositoryAuthConfigOutputTypeDef = TypedDict(
    "TrainingRepositoryAuthConfigOutputTypeDef",
    {
        "TrainingRepositoryCredentialsProviderArn": str,
    },
)

TrainingRepositoryAuthConfigTypeDef = TypedDict(
    "TrainingRepositoryAuthConfigTypeDef",
    {
        "TrainingRepositoryCredentialsProviderArn": str,
    },
)

TransformS3DataSourceOutputTypeDef = TypedDict(
    "TransformS3DataSourceOutputTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)

TransformS3DataSourceTypeDef = TypedDict(
    "TransformS3DataSourceTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)

_RequiredUpdateActionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateActionRequestRequestTypeDef",
    {
        "ActionName": str,
    },
)
_OptionalUpdateActionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateActionRequestRequestTypeDef",
    {
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Mapping[str, str],
        "PropertiesToRemove": Sequence[str],
    },
    total=False,
)


class UpdateActionRequestRequestTypeDef(
    _RequiredUpdateActionRequestRequestTypeDef, _OptionalUpdateActionRequestRequestTypeDef
):
    pass


_RequiredUpdateArtifactRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": str,
    },
)
_OptionalUpdateArtifactRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateArtifactRequestRequestTypeDef",
    {
        "ArtifactName": str,
        "Properties": Mapping[str, str],
        "PropertiesToRemove": Sequence[str],
    },
    total=False,
)


class UpdateArtifactRequestRequestTypeDef(
    _RequiredUpdateArtifactRequestRequestTypeDef, _OptionalUpdateArtifactRequestRequestTypeDef
):
    pass


_RequiredUpdateContextRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContextRequestRequestTypeDef",
    {
        "ContextName": str,
    },
)
_OptionalUpdateContextRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContextRequestRequestTypeDef",
    {
        "Description": str,
        "Properties": Mapping[str, str],
        "PropertiesToRemove": Sequence[str],
    },
    total=False,
)


class UpdateContextRequestRequestTypeDef(
    _RequiredUpdateContextRequestRequestTypeDef, _OptionalUpdateContextRequestRequestTypeDef
):
    pass


VariantPropertyTypeDef = TypedDict(
    "VariantPropertyTypeDef",
    {
        "VariantPropertyType": VariantPropertyTypeType,
    },
)

_RequiredUpdateExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)
_OptionalUpdateExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExperimentRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
    },
    total=False,
)


class UpdateExperimentRequestRequestTypeDef(
    _RequiredUpdateExperimentRequestRequestTypeDef, _OptionalUpdateExperimentRequestRequestTypeDef
):
    pass


_RequiredUpdateHubRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateHubRequestRequestTypeDef",
    {
        "HubName": str,
    },
)
_OptionalUpdateHubRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateHubRequestRequestTypeDef",
    {
        "HubDescription": str,
        "HubDisplayName": str,
        "HubSearchKeywords": Sequence[str],
    },
    total=False,
)


class UpdateHubRequestRequestTypeDef(
    _RequiredUpdateHubRequestRequestTypeDef, _OptionalUpdateHubRequestRequestTypeDef
):
    pass


_RequiredUpdateImageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateImageRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalUpdateImageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateImageRequestRequestTypeDef",
    {
        "DeleteProperties": Sequence[str],
        "Description": str,
        "DisplayName": str,
        "RoleArn": str,
    },
    total=False,
)


class UpdateImageRequestRequestTypeDef(
    _RequiredUpdateImageRequestRequestTypeDef, _OptionalUpdateImageRequestRequestTypeDef
):
    pass


_RequiredUpdateImageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateImageVersionRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalUpdateImageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateImageVersionRequestRequestTypeDef",
    {
        "Alias": str,
        "Version": int,
        "AliasesToAdd": Sequence[str],
        "AliasesToDelete": Sequence[str],
        "VendorGuidance": VendorGuidanceType,
        "JobType": JobTypeType,
        "MLFramework": str,
        "ProgrammingLang": str,
        "Processor": ProcessorType,
        "Horovod": bool,
        "ReleaseNotes": str,
    },
    total=False,
)


class UpdateImageVersionRequestRequestTypeDef(
    _RequiredUpdateImageVersionRequestRequestTypeDef,
    _OptionalUpdateImageVersionRequestRequestTypeDef,
):
    pass


_RequiredUpdateModelCardRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelCardRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalUpdateModelCardRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelCardRequestRequestTypeDef",
    {
        "Content": str,
        "ModelCardStatus": ModelCardStatusType,
    },
    total=False,
)


class UpdateModelCardRequestRequestTypeDef(
    _RequiredUpdateModelCardRequestRequestTypeDef, _OptionalUpdateModelCardRequestRequestTypeDef
):
    pass


UpdateMonitoringAlertRequestRequestTypeDef = TypedDict(
    "UpdateMonitoringAlertRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringAlertName": str,
        "DatapointsToAlert": int,
        "EvaluationPeriod": int,
    },
)

_RequiredUpdateTrialRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrialRequestRequestTypeDef",
    {
        "TrialName": str,
    },
)
_OptionalUpdateTrialRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrialRequestRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class UpdateTrialRequestRequestTypeDef(
    _RequiredUpdateTrialRequestRequestTypeDef, _OptionalUpdateTrialRequestRequestTypeDef
):
    pass


_RequiredWorkforceVpcConfigResponseTypeDef = TypedDict(
    "_RequiredWorkforceVpcConfigResponseTypeDef",
    {
        "VpcId": str,
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)
_OptionalWorkforceVpcConfigResponseTypeDef = TypedDict(
    "_OptionalWorkforceVpcConfigResponseTypeDef",
    {
        "VpcEndpointId": str,
    },
    total=False,
)


class WorkforceVpcConfigResponseTypeDef(
    _RequiredWorkforceVpcConfigResponseTypeDef, _OptionalWorkforceVpcConfigResponseTypeDef
):
    pass


ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "ActionArn": str,
        "ActionName": str,
        "Source": ActionSourceOutputTypeDef,
        "ActionType": str,
        "Status": ActionStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

AddAssociationResponseTypeDef = TypedDict(
    "AddAssociationResponseTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociateTrialComponentResponseTypeDef = TypedDict(
    "AssociateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "TrialArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateActionResponseTypeDef = TypedDict(
    "CreateActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAlgorithmOutputTypeDef = TypedDict(
    "CreateAlgorithmOutputTypeDef",
    {
        "AlgorithmArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAppImageConfigResponseTypeDef = TypedDict(
    "CreateAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "AppArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateArtifactResponseTypeDef = TypedDict(
    "CreateArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAutoMLJobResponseTypeDef = TypedDict(
    "CreateAutoMLJobResponseTypeDef",
    {
        "AutoMLJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAutoMLJobV2ResponseTypeDef = TypedDict(
    "CreateAutoMLJobV2ResponseTypeDef",
    {
        "AutoMLJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateCodeRepositoryOutputTypeDef = TypedDict(
    "CreateCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateCompilationJobResponseTypeDef = TypedDict(
    "CreateCompilationJobResponseTypeDef",
    {
        "CompilationJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateContextResponseTypeDef = TypedDict(
    "CreateContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDataQualityJobDefinitionResponseTypeDef = TypedDict(
    "CreateDataQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainArn": str,
        "Url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateEdgeDeploymentPlanResponseTypeDef = TypedDict(
    "CreateEdgeDeploymentPlanResponseTypeDef",
    {
        "EdgeDeploymentPlanArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateEndpointConfigOutputTypeDef = TypedDict(
    "CreateEndpointConfigOutputTypeDef",
    {
        "EndpointConfigArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateEndpointOutputTypeDef = TypedDict(
    "CreateEndpointOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateExperimentResponseTypeDef = TypedDict(
    "CreateExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFeatureGroupResponseTypeDef = TypedDict(
    "CreateFeatureGroupResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFlowDefinitionResponseTypeDef = TypedDict(
    "CreateFlowDefinitionResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateHubResponseTypeDef = TypedDict(
    "CreateHubResponseTypeDef",
    {
        "HubArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateHumanTaskUiResponseTypeDef = TypedDict(
    "CreateHumanTaskUiResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateHyperParameterTuningJobResponseTypeDef = TypedDict(
    "CreateHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateImageResponseTypeDef = TypedDict(
    "CreateImageResponseTypeDef",
    {
        "ImageArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateImageVersionResponseTypeDef = TypedDict(
    "CreateImageVersionResponseTypeDef",
    {
        "ImageVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateInferenceExperimentResponseTypeDef = TypedDict(
    "CreateInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateInferenceRecommendationsJobResponseTypeDef = TypedDict(
    "CreateInferenceRecommendationsJobResponseTypeDef",
    {
        "JobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLabelingJobResponseTypeDef = TypedDict(
    "CreateLabelingJobResponseTypeDef",
    {
        "LabelingJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelBiasJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelBiasJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelCardExportJobResponseTypeDef = TypedDict(
    "CreateModelCardExportJobResponseTypeDef",
    {
        "ModelCardExportJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelCardResponseTypeDef = TypedDict(
    "CreateModelCardResponseTypeDef",
    {
        "ModelCardArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelExplainabilityJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelExplainabilityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelOutputTypeDef = TypedDict(
    "CreateModelOutputTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelPackageGroupOutputTypeDef = TypedDict(
    "CreateModelPackageGroupOutputTypeDef",
    {
        "ModelPackageGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelPackageOutputTypeDef = TypedDict(
    "CreateModelPackageOutputTypeDef",
    {
        "ModelPackageArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelQualityJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateMonitoringScheduleResponseTypeDef = TypedDict(
    "CreateMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateNotebookInstanceLifecycleConfigOutputTypeDef = TypedDict(
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateNotebookInstanceOutputTypeDef = TypedDict(
    "CreateNotebookInstanceOutputTypeDef",
    {
        "NotebookInstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePresignedDomainUrlResponseTypeDef = TypedDict(
    "CreatePresignedDomainUrlResponseTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePresignedNotebookInstanceUrlOutputTypeDef = TypedDict(
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateProcessingJobResponseTypeDef = TypedDict(
    "CreateProcessingJobResponseTypeDef",
    {
        "ProcessingJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ProjectId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateSpaceResponseTypeDef = TypedDict(
    "CreateSpaceResponseTypeDef",
    {
        "SpaceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateStudioLifecycleConfigResponseTypeDef = TypedDict(
    "CreateStudioLifecycleConfigResponseTypeDef",
    {
        "StudioLifecycleConfigArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTrainingJobResponseTypeDef = TypedDict(
    "CreateTrainingJobResponseTypeDef",
    {
        "TrainingJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTransformJobResponseTypeDef = TypedDict(
    "CreateTransformJobResponseTypeDef",
    {
        "TransformJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTrialComponentResponseTypeDef = TypedDict(
    "CreateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTrialResponseTypeDef = TypedDict(
    "CreateTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateUserProfileResponseTypeDef = TypedDict(
    "CreateUserProfileResponseTypeDef",
    {
        "UserProfileArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateWorkforceResponseTypeDef = TypedDict(
    "CreateWorkforceResponseTypeDef",
    {
        "WorkforceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateWorkteamResponseTypeDef = TypedDict(
    "CreateWorkteamResponseTypeDef",
    {
        "WorkteamArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteActionResponseTypeDef = TypedDict(
    "DeleteActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteArtifactResponseTypeDef = TypedDict(
    "DeleteArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteAssociationResponseTypeDef = TypedDict(
    "DeleteAssociationResponseTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteContextResponseTypeDef = TypedDict(
    "DeleteContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteExperimentResponseTypeDef = TypedDict(
    "DeleteExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteInferenceExperimentResponseTypeDef = TypedDict(
    "DeleteInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeletePipelineResponseTypeDef = TypedDict(
    "DeletePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteTrialComponentResponseTypeDef = TypedDict(
    "DeleteTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteTrialResponseTypeDef = TypedDict(
    "DeleteTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteWorkteamResponseTypeDef = TypedDict(
    "DeleteWorkteamResponseTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeImageResponseTypeDef = TypedDict(
    "DescribeImageResponseTypeDef",
    {
        "CreationTime": datetime,
        "Description": str,
        "DisplayName": str,
        "FailureReason": str,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": ImageStatusType,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeImageVersionResponseTypeDef = TypedDict(
    "DescribeImageVersionResponseTypeDef",
    {
        "BaseImage": str,
        "ContainerImage": str,
        "CreationTime": datetime,
        "FailureReason": str,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": ImageVersionStatusType,
        "LastModifiedTime": datetime,
        "Version": int,
        "VendorGuidance": VendorGuidanceType,
        "JobType": JobTypeType,
        "MLFramework": str,
        "ProgrammingLang": str,
        "Processor": ProcessorType,
        "Horovod": bool,
        "ReleaseNotes": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribePipelineDefinitionForExecutionResponseTypeDef = TypedDict(
    "DescribePipelineDefinitionForExecutionResponseTypeDef",
    {
        "PipelineDefinition": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStudioLifecycleConfigResponseTypeDef = TypedDict(
    "DescribeStudioLifecycleConfigResponseTypeDef",
    {
        "StudioLifecycleConfigArn": str,
        "StudioLifecycleConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "StudioLifecycleConfigContent": str,
        "StudioLifecycleConfigAppType": StudioLifecycleConfigAppTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisassociateTrialComponentResponseTypeDef = TypedDict(
    "DisassociateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "TrialArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetLineageGroupPolicyResponseTypeDef = TypedDict(
    "GetLineageGroupPolicyResponseTypeDef",
    {
        "LineageGroupArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetModelPackageGroupPolicyOutputTypeDef = TypedDict(
    "GetModelPackageGroupPolicyOutputTypeDef",
    {
        "ResourcePolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSagemakerServicecatalogPortfolioStatusOutputTypeDef = TypedDict(
    "GetSagemakerServicecatalogPortfolioStatusOutputTypeDef",
    {
        "Status": SagemakerServicecatalogStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ImportHubContentResponseTypeDef = TypedDict(
    "ImportHubContentResponseTypeDef",
    {
        "HubArn": str,
        "HubContentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "SageMakerImageVersionAliases": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutModelPackageGroupPolicyOutputTypeDef = TypedDict(
    "PutModelPackageGroupPolicyOutputTypeDef",
    {
        "ModelPackageGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RetryPipelineExecutionResponseTypeDef = TypedDict(
    "RetryPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SendPipelineExecutionStepFailureResponseTypeDef = TypedDict(
    "SendPipelineExecutionStepFailureResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SendPipelineExecutionStepSuccessResponseTypeDef = TypedDict(
    "SendPipelineExecutionStepSuccessResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartInferenceExperimentResponseTypeDef = TypedDict(
    "StartInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartPipelineExecutionResponseTypeDef = TypedDict(
    "StartPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopInferenceExperimentResponseTypeDef = TypedDict(
    "StopInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopPipelineExecutionResponseTypeDef = TypedDict(
    "StopPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateActionResponseTypeDef = TypedDict(
    "UpdateActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateAppImageConfigResponseTypeDef = TypedDict(
    "UpdateAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateArtifactResponseTypeDef = TypedDict(
    "UpdateArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateCodeRepositoryOutputTypeDef = TypedDict(
    "UpdateCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateContextResponseTypeDef = TypedDict(
    "UpdateContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "DomainArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateEndpointOutputTypeDef = TypedDict(
    "UpdateEndpointOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateEndpointWeightsAndCapacitiesOutputTypeDef = TypedDict(
    "UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateExperimentResponseTypeDef = TypedDict(
    "UpdateExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFeatureGroupResponseTypeDef = TypedDict(
    "UpdateFeatureGroupResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateHubResponseTypeDef = TypedDict(
    "UpdateHubResponseTypeDef",
    {
        "HubArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateImageResponseTypeDef = TypedDict(
    "UpdateImageResponseTypeDef",
    {
        "ImageArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateImageVersionResponseTypeDef = TypedDict(
    "UpdateImageVersionResponseTypeDef",
    {
        "ImageVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateInferenceExperimentResponseTypeDef = TypedDict(
    "UpdateInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateModelCardResponseTypeDef = TypedDict(
    "UpdateModelCardResponseTypeDef",
    {
        "ModelCardArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateModelPackageOutputTypeDef = TypedDict(
    "UpdateModelPackageOutputTypeDef",
    {
        "ModelPackageArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateMonitoringAlertResponseTypeDef = TypedDict(
    "UpdateMonitoringAlertResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringAlertName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateMonitoringScheduleResponseTypeDef = TypedDict(
    "UpdateMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePipelineExecutionResponseTypeDef = TypedDict(
    "UpdatePipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePipelineResponseTypeDef = TypedDict(
    "UpdatePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateSpaceResponseTypeDef = TypedDict(
    "UpdateSpaceResponseTypeDef",
    {
        "SpaceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTrainingJobResponseTypeDef = TypedDict(
    "UpdateTrainingJobResponseTypeDef",
    {
        "TrainingJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTrialComponentResponseTypeDef = TypedDict(
    "UpdateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTrialResponseTypeDef = TypedDict(
    "UpdateTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateUserProfileResponseTypeDef = TypedDict(
    "UpdateUserProfileResponseTypeDef",
    {
        "UserProfileArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredCreateExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)
_OptionalCreateExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExperimentRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateExperimentRequestRequestTypeDef(
    _RequiredCreateExperimentRequestRequestTypeDef, _OptionalCreateExperimentRequestRequestTypeDef
):
    pass


_RequiredCreateImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageRequestRequestTypeDef",
    {
        "ImageName": str,
        "RoleArn": str,
    },
)
_OptionalCreateImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageRequestRequestTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateImageRequestRequestTypeDef(
    _RequiredCreateImageRequestRequestTypeDef, _OptionalCreateImageRequestRequestTypeDef
):
    pass


_RequiredCreateModelPackageGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)
_OptionalCreateModelPackageGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupDescription": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateModelPackageGroupInputRequestTypeDef(
    _RequiredCreateModelPackageGroupInputRequestTypeDef,
    _OptionalCreateModelPackageGroupInputRequestTypeDef,
):
    pass


_RequiredCreateStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
        "StudioLifecycleConfigContent": str,
        "StudioLifecycleConfigAppType": StudioLifecycleConfigAppTypeType,
    },
)
_OptionalCreateStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStudioLifecycleConfigRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateStudioLifecycleConfigRequestRequestTypeDef(
    _RequiredCreateStudioLifecycleConfigRequestRequestTypeDef,
    _OptionalCreateStudioLifecycleConfigRequestRequestTypeDef,
):
    pass


_RequiredImportHubContentRequestRequestTypeDef = TypedDict(
    "_RequiredImportHubContentRequestRequestTypeDef",
    {
        "HubContentName": str,
        "HubContentType": HubContentTypeType,
        "DocumentSchemaVersion": str,
        "HubName": str,
        "HubContentDocument": str,
    },
)
_OptionalImportHubContentRequestRequestTypeDef = TypedDict(
    "_OptionalImportHubContentRequestRequestTypeDef",
    {
        "HubContentVersion": str,
        "HubContentDisplayName": str,
        "HubContentDescription": str,
        "HubContentMarkdown": str,
        "HubContentSearchKeywords": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class ImportHubContentRequestRequestTypeDef(
    _RequiredImportHubContentRequestRequestTypeDef, _OptionalImportHubContentRequestRequestTypeDef
):
    pass


AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AutoRollbackConfigOutputTypeDef = TypedDict(
    "AutoRollbackConfigOutputTypeDef",
    {
        "Alarms": List[AlarmOutputTypeDef],
    },
    total=False,
)

AutoRollbackConfigTypeDef = TypedDict(
    "AutoRollbackConfigTypeDef",
    {
        "Alarms": Sequence[AlarmTypeDef],
    },
    total=False,
)

_RequiredHyperParameterAlgorithmSpecificationOutputTypeDef = TypedDict(
    "_RequiredHyperParameterAlgorithmSpecificationOutputTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
    },
)
_OptionalHyperParameterAlgorithmSpecificationOutputTypeDef = TypedDict(
    "_OptionalHyperParameterAlgorithmSpecificationOutputTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": List[MetricDefinitionOutputTypeDef],
    },
    total=False,
)


class HyperParameterAlgorithmSpecificationOutputTypeDef(
    _RequiredHyperParameterAlgorithmSpecificationOutputTypeDef,
    _OptionalHyperParameterAlgorithmSpecificationOutputTypeDef,
):
    pass


_RequiredHyperParameterAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredHyperParameterAlgorithmSpecificationTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
    },
)
_OptionalHyperParameterAlgorithmSpecificationTypeDef = TypedDict(
    "_OptionalHyperParameterAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": Sequence[MetricDefinitionTypeDef],
    },
    total=False,
)


class HyperParameterAlgorithmSpecificationTypeDef(
    _RequiredHyperParameterAlgorithmSpecificationTypeDef,
    _OptionalHyperParameterAlgorithmSpecificationTypeDef,
):
    pass


AlgorithmStatusDetailsTypeDef = TypedDict(
    "AlgorithmStatusDetailsTypeDef",
    {
        "ValidationStatuses": List[AlgorithmStatusItemTypeDef],
        "ImageScanStatuses": List[AlgorithmStatusItemTypeDef],
    },
    total=False,
)

ListAlgorithmsOutputTypeDef = TypedDict(
    "ListAlgorithmsOutputTypeDef",
    {
        "AlgorithmSummaryList": List[AlgorithmSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "Apps": List[AppDetailsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredArtifactSourceOutputTypeDef = TypedDict(
    "_RequiredArtifactSourceOutputTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalArtifactSourceOutputTypeDef = TypedDict(
    "_OptionalArtifactSourceOutputTypeDef",
    {
        "SourceTypes": List[ArtifactSourceTypeOutputTypeDef],
    },
    total=False,
)


class ArtifactSourceOutputTypeDef(
    _RequiredArtifactSourceOutputTypeDef, _OptionalArtifactSourceOutputTypeDef
):
    pass


_RequiredArtifactSourceTypeDef = TypedDict(
    "_RequiredArtifactSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalArtifactSourceTypeDef = TypedDict(
    "_OptionalArtifactSourceTypeDef",
    {
        "SourceTypes": Sequence[ArtifactSourceTypeTypeDef],
    },
    total=False,
)


class ArtifactSourceTypeDef(_RequiredArtifactSourceTypeDef, _OptionalArtifactSourceTypeDef):
    pass


AsyncInferenceOutputConfigOutputTypeDef = TypedDict(
    "AsyncInferenceOutputConfigOutputTypeDef",
    {
        "KmsKeyId": str,
        "S3OutputPath": str,
        "NotificationConfig": AsyncInferenceNotificationConfigOutputTypeDef,
        "S3FailurePath": str,
    },
    total=False,
)

AsyncInferenceOutputConfigTypeDef = TypedDict(
    "AsyncInferenceOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "S3OutputPath": str,
        "NotificationConfig": AsyncInferenceNotificationConfigTypeDef,
        "S3FailurePath": str,
    },
    total=False,
)

AutoMLCandidateGenerationConfigOutputTypeDef = TypedDict(
    "AutoMLCandidateGenerationConfigOutputTypeDef",
    {
        "FeatureSpecificationS3Uri": str,
        "AlgorithmsConfig": List[AutoMLAlgorithmConfigOutputTypeDef],
    },
    total=False,
)

CandidateGenerationConfigOutputTypeDef = TypedDict(
    "CandidateGenerationConfigOutputTypeDef",
    {
        "AlgorithmsConfig": List[AutoMLAlgorithmConfigOutputTypeDef],
    },
    total=False,
)

AutoMLCandidateGenerationConfigTypeDef = TypedDict(
    "AutoMLCandidateGenerationConfigTypeDef",
    {
        "FeatureSpecificationS3Uri": str,
        "AlgorithmsConfig": Sequence[AutoMLAlgorithmConfigTypeDef],
    },
    total=False,
)

CandidateGenerationConfigTypeDef = TypedDict(
    "CandidateGenerationConfigTypeDef",
    {
        "AlgorithmsConfig": Sequence[AutoMLAlgorithmConfigTypeDef],
    },
    total=False,
)

AutoMLDataSourceOutputTypeDef = TypedDict(
    "AutoMLDataSourceOutputTypeDef",
    {
        "S3DataSource": AutoMLS3DataSourceOutputTypeDef,
    },
)

AutoMLDataSourceTypeDef = TypedDict(
    "AutoMLDataSourceTypeDef",
    {
        "S3DataSource": AutoMLS3DataSourceTypeDef,
    },
)

ImageClassificationJobConfigOutputTypeDef = TypedDict(
    "ImageClassificationJobConfigOutputTypeDef",
    {
        "CompletionCriteria": AutoMLJobCompletionCriteriaOutputTypeDef,
    },
    total=False,
)

_RequiredTextClassificationJobConfigOutputTypeDef = TypedDict(
    "_RequiredTextClassificationJobConfigOutputTypeDef",
    {
        "ContentColumn": str,
        "TargetLabelColumn": str,
    },
)
_OptionalTextClassificationJobConfigOutputTypeDef = TypedDict(
    "_OptionalTextClassificationJobConfigOutputTypeDef",
    {
        "CompletionCriteria": AutoMLJobCompletionCriteriaOutputTypeDef,
    },
    total=False,
)


class TextClassificationJobConfigOutputTypeDef(
    _RequiredTextClassificationJobConfigOutputTypeDef,
    _OptionalTextClassificationJobConfigOutputTypeDef,
):
    pass


ImageClassificationJobConfigTypeDef = TypedDict(
    "ImageClassificationJobConfigTypeDef",
    {
        "CompletionCriteria": AutoMLJobCompletionCriteriaTypeDef,
    },
    total=False,
)

_RequiredTextClassificationJobConfigTypeDef = TypedDict(
    "_RequiredTextClassificationJobConfigTypeDef",
    {
        "ContentColumn": str,
        "TargetLabelColumn": str,
    },
)
_OptionalTextClassificationJobConfigTypeDef = TypedDict(
    "_OptionalTextClassificationJobConfigTypeDef",
    {
        "CompletionCriteria": AutoMLJobCompletionCriteriaTypeDef,
    },
    total=False,
)


class TextClassificationJobConfigTypeDef(
    _RequiredTextClassificationJobConfigTypeDef, _OptionalTextClassificationJobConfigTypeDef
):
    pass


ResolvedAttributesTypeDef = TypedDict(
    "ResolvedAttributesTypeDef",
    {
        "AutoMLJobObjective": AutoMLJobObjectiveOutputTypeDef,
        "ProblemType": ProblemTypeType,
        "CompletionCriteria": AutoMLJobCompletionCriteriaOutputTypeDef,
    },
    total=False,
)

_RequiredAutoMLJobSummaryTypeDef = TypedDict(
    "_RequiredAutoMLJobSummaryTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLJobSummaryTypeDef = TypedDict(
    "_OptionalAutoMLJobSummaryTypeDef",
    {
        "EndTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List[AutoMLPartialFailureReasonTypeDef],
    },
    total=False,
)


class AutoMLJobSummaryTypeDef(_RequiredAutoMLJobSummaryTypeDef, _OptionalAutoMLJobSummaryTypeDef):
    pass


AutoMLProblemTypeResolvedAttributesTypeDef = TypedDict(
    "AutoMLProblemTypeResolvedAttributesTypeDef",
    {
        "TabularResolvedAttributes": TabularResolvedAttributesTypeDef,
    },
    total=False,
)

AutoMLSecurityConfigOutputTypeDef = TypedDict(
    "AutoMLSecurityConfigOutputTypeDef",
    {
        "VolumeKmsKeyId": str,
        "EnableInterContainerTrafficEncryption": bool,
        "VpcConfig": VpcConfigOutputTypeDef,
    },
    total=False,
)

LabelingJobResourceConfigOutputTypeDef = TypedDict(
    "LabelingJobResourceConfigOutputTypeDef",
    {
        "VolumeKmsKeyId": str,
        "VpcConfig": VpcConfigOutputTypeDef,
    },
    total=False,
)

MonitoringNetworkConfigOutputTypeDef = TypedDict(
    "MonitoringNetworkConfigOutputTypeDef",
    {
        "EnableInterContainerTrafficEncryption": bool,
        "EnableNetworkIsolation": bool,
        "VpcConfig": VpcConfigOutputTypeDef,
    },
    total=False,
)

NetworkConfigOutputTypeDef = TypedDict(
    "NetworkConfigOutputTypeDef",
    {
        "EnableInterContainerTrafficEncryption": bool,
        "EnableNetworkIsolation": bool,
        "VpcConfig": VpcConfigOutputTypeDef,
    },
    total=False,
)

AutoMLSecurityConfigTypeDef = TypedDict(
    "AutoMLSecurityConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
        "EnableInterContainerTrafficEncryption": bool,
        "VpcConfig": VpcConfigTypeDef,
    },
    total=False,
)

LabelingJobResourceConfigTypeDef = TypedDict(
    "LabelingJobResourceConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
        "VpcConfig": VpcConfigTypeDef,
    },
    total=False,
)

MonitoringNetworkConfigTypeDef = TypedDict(
    "MonitoringNetworkConfigTypeDef",
    {
        "EnableInterContainerTrafficEncryption": bool,
        "EnableNetworkIsolation": bool,
        "VpcConfig": VpcConfigTypeDef,
    },
    total=False,
)

NetworkConfigTypeDef = TypedDict(
    "NetworkConfigTypeDef",
    {
        "EnableInterContainerTrafficEncryption": bool,
        "EnableNetworkIsolation": bool,
        "VpcConfig": VpcConfigTypeDef,
    },
    total=False,
)

BiasOutputTypeDef = TypedDict(
    "BiasOutputTypeDef",
    {
        "Report": MetricsSourceOutputTypeDef,
        "PreTrainingReport": MetricsSourceOutputTypeDef,
        "PostTrainingReport": MetricsSourceOutputTypeDef,
    },
    total=False,
)

DriftCheckModelDataQualityOutputTypeDef = TypedDict(
    "DriftCheckModelDataQualityOutputTypeDef",
    {
        "Statistics": MetricsSourceOutputTypeDef,
        "Constraints": MetricsSourceOutputTypeDef,
    },
    total=False,
)

DriftCheckModelQualityOutputTypeDef = TypedDict(
    "DriftCheckModelQualityOutputTypeDef",
    {
        "Statistics": MetricsSourceOutputTypeDef,
        "Constraints": MetricsSourceOutputTypeDef,
    },
    total=False,
)

ExplainabilityOutputTypeDef = TypedDict(
    "ExplainabilityOutputTypeDef",
    {
        "Report": MetricsSourceOutputTypeDef,
    },
    total=False,
)

ModelDataQualityOutputTypeDef = TypedDict(
    "ModelDataQualityOutputTypeDef",
    {
        "Statistics": MetricsSourceOutputTypeDef,
        "Constraints": MetricsSourceOutputTypeDef,
    },
    total=False,
)

ModelQualityOutputTypeDef = TypedDict(
    "ModelQualityOutputTypeDef",
    {
        "Statistics": MetricsSourceOutputTypeDef,
        "Constraints": MetricsSourceOutputTypeDef,
    },
    total=False,
)

BiasTypeDef = TypedDict(
    "BiasTypeDef",
    {
        "Report": MetricsSourceTypeDef,
        "PreTrainingReport": MetricsSourceTypeDef,
        "PostTrainingReport": MetricsSourceTypeDef,
    },
    total=False,
)

DriftCheckModelDataQualityTypeDef = TypedDict(
    "DriftCheckModelDataQualityTypeDef",
    {
        "Statistics": MetricsSourceTypeDef,
        "Constraints": MetricsSourceTypeDef,
    },
    total=False,
)

DriftCheckModelQualityTypeDef = TypedDict(
    "DriftCheckModelQualityTypeDef",
    {
        "Statistics": MetricsSourceTypeDef,
        "Constraints": MetricsSourceTypeDef,
    },
    total=False,
)

ExplainabilityTypeDef = TypedDict(
    "ExplainabilityTypeDef",
    {
        "Report": MetricsSourceTypeDef,
    },
    total=False,
)

ModelDataQualityTypeDef = TypedDict(
    "ModelDataQualityTypeDef",
    {
        "Statistics": MetricsSourceTypeDef,
        "Constraints": MetricsSourceTypeDef,
    },
    total=False,
)

ModelQualityTypeDef = TypedDict(
    "ModelQualityTypeDef",
    {
        "Statistics": MetricsSourceTypeDef,
        "Constraints": MetricsSourceTypeDef,
    },
    total=False,
)

CallbackStepMetadataTypeDef = TypedDict(
    "CallbackStepMetadataTypeDef",
    {
        "CallbackToken": str,
        "SqsQueueUrl": str,
        "OutputParameters": List[OutputParameterOutputTypeDef],
    },
    total=False,
)

LambdaStepMetadataTypeDef = TypedDict(
    "LambdaStepMetadataTypeDef",
    {
        "Arn": str,
        "OutputParameters": List[OutputParameterOutputTypeDef],
    },
    total=False,
)

CandidatePropertiesTypeDef = TypedDict(
    "CandidatePropertiesTypeDef",
    {
        "CandidateArtifactLocations": CandidateArtifactLocationsTypeDef,
        "CandidateMetrics": List[MetricDatumTypeDef],
    },
    total=False,
)

CanvasAppSettingsOutputTypeDef = TypedDict(
    "CanvasAppSettingsOutputTypeDef",
    {
        "TimeSeriesForecastingSettings": TimeSeriesForecastingSettingsOutputTypeDef,
        "ModelRegisterSettings": ModelRegisterSettingsOutputTypeDef,
        "WorkspaceSettings": WorkspaceSettingsOutputTypeDef,
    },
    total=False,
)

CanvasAppSettingsTypeDef = TypedDict(
    "CanvasAppSettingsTypeDef",
    {
        "TimeSeriesForecastingSettings": TimeSeriesForecastingSettingsTypeDef,
        "ModelRegisterSettings": ModelRegisterSettingsTypeDef,
        "WorkspaceSettings": WorkspaceSettingsTypeDef,
    },
    total=False,
)

_RequiredRollingUpdatePolicyOutputTypeDef = TypedDict(
    "_RequiredRollingUpdatePolicyOutputTypeDef",
    {
        "MaximumBatchSize": CapacitySizeOutputTypeDef,
        "WaitIntervalInSeconds": int,
    },
)
_OptionalRollingUpdatePolicyOutputTypeDef = TypedDict(
    "_OptionalRollingUpdatePolicyOutputTypeDef",
    {
        "MaximumExecutionTimeoutInSeconds": int,
        "RollbackMaximumBatchSize": CapacitySizeOutputTypeDef,
    },
    total=False,
)


class RollingUpdatePolicyOutputTypeDef(
    _RequiredRollingUpdatePolicyOutputTypeDef, _OptionalRollingUpdatePolicyOutputTypeDef
):
    pass


_RequiredTrafficRoutingConfigOutputTypeDef = TypedDict(
    "_RequiredTrafficRoutingConfigOutputTypeDef",
    {
        "Type": TrafficRoutingConfigTypeType,
        "WaitIntervalInSeconds": int,
    },
)
_OptionalTrafficRoutingConfigOutputTypeDef = TypedDict(
    "_OptionalTrafficRoutingConfigOutputTypeDef",
    {
        "CanarySize": CapacitySizeOutputTypeDef,
        "LinearStepSize": CapacitySizeOutputTypeDef,
    },
    total=False,
)


class TrafficRoutingConfigOutputTypeDef(
    _RequiredTrafficRoutingConfigOutputTypeDef, _OptionalTrafficRoutingConfigOutputTypeDef
):
    pass


_RequiredRollingUpdatePolicyTypeDef = TypedDict(
    "_RequiredRollingUpdatePolicyTypeDef",
    {
        "MaximumBatchSize": CapacitySizeTypeDef,
        "WaitIntervalInSeconds": int,
    },
)
_OptionalRollingUpdatePolicyTypeDef = TypedDict(
    "_OptionalRollingUpdatePolicyTypeDef",
    {
        "MaximumExecutionTimeoutInSeconds": int,
        "RollbackMaximumBatchSize": CapacitySizeTypeDef,
    },
    total=False,
)


class RollingUpdatePolicyTypeDef(
    _RequiredRollingUpdatePolicyTypeDef, _OptionalRollingUpdatePolicyTypeDef
):
    pass


_RequiredTrafficRoutingConfigTypeDef = TypedDict(
    "_RequiredTrafficRoutingConfigTypeDef",
    {
        "Type": TrafficRoutingConfigTypeType,
        "WaitIntervalInSeconds": int,
    },
)
_OptionalTrafficRoutingConfigTypeDef = TypedDict(
    "_OptionalTrafficRoutingConfigTypeDef",
    {
        "CanarySize": CapacitySizeTypeDef,
        "LinearStepSize": CapacitySizeTypeDef,
    },
    total=False,
)


class TrafficRoutingConfigTypeDef(
    _RequiredTrafficRoutingConfigTypeDef, _OptionalTrafficRoutingConfigTypeDef
):
    pass


_RequiredInferenceExperimentDataStorageConfigOutputTypeDef = TypedDict(
    "_RequiredInferenceExperimentDataStorageConfigOutputTypeDef",
    {
        "Destination": str,
    },
)
_OptionalInferenceExperimentDataStorageConfigOutputTypeDef = TypedDict(
    "_OptionalInferenceExperimentDataStorageConfigOutputTypeDef",
    {
        "KmsKey": str,
        "ContentType": CaptureContentTypeHeaderOutputTypeDef,
    },
    total=False,
)


class InferenceExperimentDataStorageConfigOutputTypeDef(
    _RequiredInferenceExperimentDataStorageConfigOutputTypeDef,
    _OptionalInferenceExperimentDataStorageConfigOutputTypeDef,
):
    pass


_RequiredInferenceExperimentDataStorageConfigTypeDef = TypedDict(
    "_RequiredInferenceExperimentDataStorageConfigTypeDef",
    {
        "Destination": str,
    },
)
_OptionalInferenceExperimentDataStorageConfigTypeDef = TypedDict(
    "_OptionalInferenceExperimentDataStorageConfigTypeDef",
    {
        "KmsKey": str,
        "ContentType": CaptureContentTypeHeaderTypeDef,
    },
    total=False,
)


class InferenceExperimentDataStorageConfigTypeDef(
    _RequiredInferenceExperimentDataStorageConfigTypeDef,
    _OptionalInferenceExperimentDataStorageConfigTypeDef,
):
    pass


_RequiredDataCaptureConfigOutputTypeDef = TypedDict(
    "_RequiredDataCaptureConfigOutputTypeDef",
    {
        "InitialSamplingPercentage": int,
        "DestinationS3Uri": str,
        "CaptureOptions": List[CaptureOptionOutputTypeDef],
    },
)
_OptionalDataCaptureConfigOutputTypeDef = TypedDict(
    "_OptionalDataCaptureConfigOutputTypeDef",
    {
        "EnableCapture": bool,
        "KmsKeyId": str,
        "CaptureContentTypeHeader": CaptureContentTypeHeaderOutputTypeDef,
    },
    total=False,
)


class DataCaptureConfigOutputTypeDef(
    _RequiredDataCaptureConfigOutputTypeDef, _OptionalDataCaptureConfigOutputTypeDef
):
    pass


_RequiredDataCaptureConfigTypeDef = TypedDict(
    "_RequiredDataCaptureConfigTypeDef",
    {
        "InitialSamplingPercentage": int,
        "DestinationS3Uri": str,
        "CaptureOptions": Sequence[CaptureOptionTypeDef],
    },
)
_OptionalDataCaptureConfigTypeDef = TypedDict(
    "_OptionalDataCaptureConfigTypeDef",
    {
        "EnableCapture": bool,
        "KmsKeyId": str,
        "CaptureContentTypeHeader": CaptureContentTypeHeaderTypeDef,
    },
    total=False,
)


class DataCaptureConfigTypeDef(
    _RequiredDataCaptureConfigTypeDef, _OptionalDataCaptureConfigTypeDef
):
    pass


EnvironmentParameterRangesOutputTypeDef = TypedDict(
    "EnvironmentParameterRangesOutputTypeDef",
    {
        "CategoricalParameterRanges": List[CategoricalParameterOutputTypeDef],
    },
    total=False,
)

EnvironmentParameterRangesTypeDef = TypedDict(
    "EnvironmentParameterRangesTypeDef",
    {
        "CategoricalParameterRanges": Sequence[CategoricalParameterTypeDef],
    },
    total=False,
)

_RequiredClarifyShapConfigOutputTypeDef = TypedDict(
    "_RequiredClarifyShapConfigOutputTypeDef",
    {
        "ShapBaselineConfig": ClarifyShapBaselineConfigOutputTypeDef,
    },
)
_OptionalClarifyShapConfigOutputTypeDef = TypedDict(
    "_OptionalClarifyShapConfigOutputTypeDef",
    {
        "NumberOfSamples": int,
        "UseLogit": bool,
        "Seed": int,
        "TextConfig": ClarifyTextConfigOutputTypeDef,
    },
    total=False,
)


class ClarifyShapConfigOutputTypeDef(
    _RequiredClarifyShapConfigOutputTypeDef, _OptionalClarifyShapConfigOutputTypeDef
):
    pass


_RequiredClarifyShapConfigTypeDef = TypedDict(
    "_RequiredClarifyShapConfigTypeDef",
    {
        "ShapBaselineConfig": ClarifyShapBaselineConfigTypeDef,
    },
)
_OptionalClarifyShapConfigTypeDef = TypedDict(
    "_OptionalClarifyShapConfigTypeDef",
    {
        "NumberOfSamples": int,
        "UseLogit": bool,
        "Seed": int,
        "TextConfig": ClarifyTextConfigTypeDef,
    },
    total=False,
)


class ClarifyShapConfigTypeDef(
    _RequiredClarifyShapConfigTypeDef, _OptionalClarifyShapConfigTypeDef
):
    pass


_RequiredCodeRepositorySummaryTypeDef = TypedDict(
    "_RequiredCodeRepositorySummaryTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalCodeRepositorySummaryTypeDef = TypedDict(
    "_OptionalCodeRepositorySummaryTypeDef",
    {
        "GitConfig": GitConfigOutputTypeDef,
    },
    total=False,
)


class CodeRepositorySummaryTypeDef(
    _RequiredCodeRepositorySummaryTypeDef, _OptionalCodeRepositorySummaryTypeDef
):
    pass


DescribeCodeRepositoryOutputTypeDef = TypedDict(
    "DescribeCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": GitConfigOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredDebugHookConfigOutputTypeDef = TypedDict(
    "_RequiredDebugHookConfigOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalDebugHookConfigOutputTypeDef = TypedDict(
    "_OptionalDebugHookConfigOutputTypeDef",
    {
        "LocalPath": str,
        "HookParameters": Dict[str, str],
        "CollectionConfigurations": List[CollectionConfigurationOutputTypeDef],
    },
    total=False,
)


class DebugHookConfigOutputTypeDef(
    _RequiredDebugHookConfigOutputTypeDef, _OptionalDebugHookConfigOutputTypeDef
):
    pass


_RequiredDebugHookConfigTypeDef = TypedDict(
    "_RequiredDebugHookConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalDebugHookConfigTypeDef = TypedDict(
    "_OptionalDebugHookConfigTypeDef",
    {
        "LocalPath": str,
        "HookParameters": Mapping[str, str],
        "CollectionConfigurations": Sequence[CollectionConfigurationTypeDef],
    },
    total=False,
)


class DebugHookConfigTypeDef(_RequiredDebugHookConfigTypeDef, _OptionalDebugHookConfigTypeDef):
    pass


ListCompilationJobsResponseTypeDef = TypedDict(
    "ListCompilationJobsResponseTypeDef",
    {
        "CompilationJobSummaries": List[CompilationJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ContextSummaryTypeDef = TypedDict(
    "ContextSummaryTypeDef",
    {
        "ContextArn": str,
        "ContextName": str,
        "Source": ContextSourceOutputTypeDef,
        "ContextType": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredCreateContextRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContextRequestRequestTypeDef",
    {
        "ContextName": str,
        "Source": ContextSourceTypeDef,
        "ContextType": str,
    },
)
_OptionalCreateContextRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContextRequestRequestTypeDef",
    {
        "Description": str,
        "Properties": Mapping[str, str],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateContextRequestRequestTypeDef(
    _RequiredCreateContextRequestRequestTypeDef, _OptionalCreateContextRequestRequestTypeDef
):
    pass


TuningJobCompletionCriteriaOutputTypeDef = TypedDict(
    "TuningJobCompletionCriteriaOutputTypeDef",
    {
        "TargetObjectiveMetricValue": float,
        "BestObjectiveNotImproving": BestObjectiveNotImprovingOutputTypeDef,
        "ConvergenceDetected": ConvergenceDetectedOutputTypeDef,
    },
    total=False,
)

TuningJobCompletionCriteriaTypeDef = TypedDict(
    "TuningJobCompletionCriteriaTypeDef",
    {
        "TargetObjectiveMetricValue": float,
        "BestObjectiveNotImproving": BestObjectiveNotImprovingTypeDef,
        "ConvergenceDetected": ConvergenceDetectedTypeDef,
    },
    total=False,
)

_RequiredCreateActionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateActionRequestRequestTypeDef",
    {
        "ActionName": str,
        "Source": ActionSourceTypeDef,
        "ActionType": str,
    },
)
_OptionalCreateActionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateActionRequestRequestTypeDef",
    {
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Mapping[str, str],
        "MetadataProperties": MetadataPropertiesTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateActionRequestRequestTypeDef(
    _RequiredCreateActionRequestRequestTypeDef, _OptionalCreateActionRequestRequestTypeDef
):
    pass


_RequiredCreateTrialRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrialRequestRequestTypeDef",
    {
        "TrialName": str,
        "ExperimentName": str,
    },
)
_OptionalCreateTrialRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrialRequestRequestTypeDef",
    {
        "DisplayName": str,
        "MetadataProperties": MetadataPropertiesTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateTrialRequestRequestTypeDef(
    _RequiredCreateTrialRequestRequestTypeDef, _OptionalCreateTrialRequestRequestTypeDef
):
    pass


_RequiredCreateAppRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)
_OptionalCreateAppRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppRequestRequestTypeDef",
    {
        "UserProfileName": str,
        "Tags": Sequence[TagTypeDef],
        "ResourceSpec": ResourceSpecTypeDef,
        "SpaceName": str,
    },
    total=False,
)


class CreateAppRequestRequestTypeDef(
    _RequiredCreateAppRequestRequestTypeDef, _OptionalCreateAppRequestRequestTypeDef
):
    pass


JupyterServerAppSettingsTypeDef = TypedDict(
    "JupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecTypeDef,
        "LifecycleConfigArns": Sequence[str],
        "CodeRepositories": Sequence[CodeRepositoryTypeDef],
    },
    total=False,
)

_RequiredRStudioServerProDomainSettingsForUpdateTypeDef = TypedDict(
    "_RequiredRStudioServerProDomainSettingsForUpdateTypeDef",
    {
        "DomainExecutionRoleArn": str,
    },
)
_OptionalRStudioServerProDomainSettingsForUpdateTypeDef = TypedDict(
    "_OptionalRStudioServerProDomainSettingsForUpdateTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecTypeDef,
        "RStudioConnectUrl": str,
        "RStudioPackageManagerUrl": str,
    },
    total=False,
)


class RStudioServerProDomainSettingsForUpdateTypeDef(
    _RequiredRStudioServerProDomainSettingsForUpdateTypeDef,
    _OptionalRStudioServerProDomainSettingsForUpdateTypeDef,
):
    pass


_RequiredRStudioServerProDomainSettingsTypeDef = TypedDict(
    "_RequiredRStudioServerProDomainSettingsTypeDef",
    {
        "DomainExecutionRoleArn": str,
    },
)
_OptionalRStudioServerProDomainSettingsTypeDef = TypedDict(
    "_OptionalRStudioServerProDomainSettingsTypeDef",
    {
        "RStudioConnectUrl": str,
        "RStudioPackageManagerUrl": str,
        "DefaultResourceSpec": ResourceSpecTypeDef,
    },
    total=False,
)


class RStudioServerProDomainSettingsTypeDef(
    _RequiredRStudioServerProDomainSettingsTypeDef, _OptionalRStudioServerProDomainSettingsTypeDef
):
    pass


TensorBoardAppSettingsTypeDef = TypedDict(
    "TensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecTypeDef,
    },
    total=False,
)

_RequiredCreateCodeRepositoryInputRequestTypeDef = TypedDict(
    "_RequiredCreateCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
        "GitConfig": GitConfigTypeDef,
    },
)
_OptionalCreateCodeRepositoryInputRequestTypeDef = TypedDict(
    "_OptionalCreateCodeRepositoryInputRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateCodeRepositoryInputRequestTypeDef(
    _RequiredCreateCodeRepositoryInputRequestTypeDef,
    _OptionalCreateCodeRepositoryInputRequestTypeDef,
):
    pass


_RequiredCreateDeviceFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "OutputConfig": EdgeOutputConfigTypeDef,
    },
)
_OptionalCreateDeviceFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeviceFleetRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Description": str,
        "Tags": Sequence[TagTypeDef],
        "EnableIotRoleAlias": bool,
    },
    total=False,
)


class CreateDeviceFleetRequestRequestTypeDef(
    _RequiredCreateDeviceFleetRequestRequestTypeDef, _OptionalCreateDeviceFleetRequestRequestTypeDef
):
    pass


_RequiredCreateEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "RoleArn": str,
        "OutputConfig": EdgeOutputConfigTypeDef,
    },
)
_OptionalCreateEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEdgePackagingJobRequestRequestTypeDef",
    {
        "ResourceKey": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateEdgePackagingJobRequestRequestTypeDef(
    _RequiredCreateEdgePackagingJobRequestRequestTypeDef,
    _OptionalCreateEdgePackagingJobRequestRequestTypeDef,
):
    pass


_RequiredUpdateDeviceFleetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "OutputConfig": EdgeOutputConfigTypeDef,
    },
)
_OptionalUpdateDeviceFleetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceFleetRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Description": str,
        "EnableIotRoleAlias": bool,
    },
    total=False,
)


class UpdateDeviceFleetRequestRequestTypeDef(
    _RequiredUpdateDeviceFleetRequestRequestTypeDef, _OptionalUpdateDeviceFleetRequestRequestTypeDef
):
    pass


_RequiredCreateHubRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHubRequestRequestTypeDef",
    {
        "HubName": str,
        "HubDescription": str,
    },
)
_OptionalCreateHubRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHubRequestRequestTypeDef",
    {
        "HubDisplayName": str,
        "HubSearchKeywords": Sequence[str],
        "S3StorageConfig": HubS3StorageConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateHubRequestRequestTypeDef(
    _RequiredCreateHubRequestRequestTypeDef, _OptionalCreateHubRequestRequestTypeDef
):
    pass


_RequiredCreateHumanTaskUiRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
        "UiTemplate": UiTemplateTypeDef,
    },
)
_OptionalCreateHumanTaskUiRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHumanTaskUiRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateHumanTaskUiRequestRequestTypeDef(
    _RequiredCreateHumanTaskUiRequestRequestTypeDef, _OptionalCreateHumanTaskUiRequestRequestTypeDef
):
    pass


_RequiredCreateModelCardExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelCardExportJobRequestRequestTypeDef",
    {
        "ModelCardName": str,
        "ModelCardExportJobName": str,
        "OutputConfig": ModelCardExportOutputConfigTypeDef,
    },
)
_OptionalCreateModelCardExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelCardExportJobRequestRequestTypeDef",
    {
        "ModelCardVersion": int,
    },
    total=False,
)


class CreateModelCardExportJobRequestRequestTypeDef(
    _RequiredCreateModelCardExportJobRequestRequestTypeDef,
    _OptionalCreateModelCardExportJobRequestRequestTypeDef,
):
    pass


_RequiredCreateModelCardRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelCardRequestRequestTypeDef",
    {
        "ModelCardName": str,
        "Content": str,
        "ModelCardStatus": ModelCardStatusType,
    },
)
_OptionalCreateModelCardRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelCardRequestRequestTypeDef",
    {
        "SecurityConfig": ModelCardSecurityConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateModelCardRequestRequestTypeDef(
    _RequiredCreateModelCardRequestRequestTypeDef, _OptionalCreateModelCardRequestRequestTypeDef
):
    pass


_RequiredCreateNotebookInstanceInputRequestTypeDef = TypedDict(
    "_RequiredCreateNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
        "InstanceType": InstanceTypeType,
        "RoleArn": str,
    },
)
_OptionalCreateNotebookInstanceInputRequestTypeDef = TypedDict(
    "_OptionalCreateNotebookInstanceInputRequestTypeDef",
    {
        "SubnetId": str,
        "SecurityGroupIds": Sequence[str],
        "KmsKeyId": str,
        "Tags": Sequence[TagTypeDef],
        "LifecycleConfigName": str,
        "DirectInternetAccess": DirectInternetAccessType,
        "VolumeSizeInGB": int,
        "AcceleratorTypes": Sequence[NotebookInstanceAcceleratorTypeType],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": Sequence[str],
        "RootAccess": RootAccessType,
        "PlatformIdentifier": str,
        "InstanceMetadataServiceConfiguration": InstanceMetadataServiceConfigurationTypeDef,
    },
    total=False,
)


class CreateNotebookInstanceInputRequestTypeDef(
    _RequiredCreateNotebookInstanceInputRequestTypeDef,
    _OptionalCreateNotebookInstanceInputRequestTypeDef,
):
    pass


_RequiredUpdateNotebookInstanceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalUpdateNotebookInstanceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNotebookInstanceInputRequestTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "RoleArn": str,
        "LifecycleConfigName": str,
        "DisassociateLifecycleConfig": bool,
        "VolumeSizeInGB": int,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": Sequence[str],
        "AcceleratorTypes": Sequence[NotebookInstanceAcceleratorTypeType],
        "DisassociateAcceleratorTypes": bool,
        "DisassociateDefaultCodeRepository": bool,
        "DisassociateAdditionalCodeRepositories": bool,
        "RootAccess": RootAccessType,
        "InstanceMetadataServiceConfiguration": InstanceMetadataServiceConfigurationTypeDef,
    },
    total=False,
)


class UpdateNotebookInstanceInputRequestTypeDef(
    _RequiredUpdateNotebookInstanceInputRequestTypeDef,
    _OptionalUpdateNotebookInstanceInputRequestTypeDef,
):
    pass


_RequiredCreateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "_RequiredCreateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)
_OptionalCreateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "_OptionalCreateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "OnCreate": Sequence[NotebookInstanceLifecycleHookTypeDef],
        "OnStart": Sequence[NotebookInstanceLifecycleHookTypeDef],
    },
    total=False,
)


class CreateNotebookInstanceLifecycleConfigInputRequestTypeDef(
    _RequiredCreateNotebookInstanceLifecycleConfigInputRequestTypeDef,
    _OptionalCreateNotebookInstanceLifecycleConfigInputRequestTypeDef,
):
    pass


_RequiredUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)
_OptionalUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "OnCreate": Sequence[NotebookInstanceLifecycleHookTypeDef],
        "OnStart": Sequence[NotebookInstanceLifecycleHookTypeDef],
    },
    total=False,
)


class UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef(
    _RequiredUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef,
    _OptionalUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef,
):
    pass


_RequiredRetryPipelineExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredRetryPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "ClientRequestToken": str,
    },
)
_OptionalRetryPipelineExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalRetryPipelineExecutionRequestRequestTypeDef",
    {
        "ParallelismConfiguration": ParallelismConfigurationTypeDef,
    },
    total=False,
)


class RetryPipelineExecutionRequestRequestTypeDef(
    _RequiredRetryPipelineExecutionRequestRequestTypeDef,
    _OptionalRetryPipelineExecutionRequestRequestTypeDef,
):
    pass


_RequiredUpdatePipelineExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)
_OptionalUpdatePipelineExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionDescription": str,
        "PipelineExecutionDisplayName": str,
        "ParallelismConfiguration": ParallelismConfigurationTypeDef,
    },
    total=False,
)


class UpdatePipelineExecutionRequestRequestTypeDef(
    _RequiredUpdatePipelineExecutionRequestRequestTypeDef,
    _OptionalUpdatePipelineExecutionRequestRequestTypeDef,
):
    pass


_RequiredCreatePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
        "RoleArn": str,
    },
)
_OptionalCreatePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineRequestRequestTypeDef",
    {
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDefinitionS3Location": PipelineDefinitionS3LocationTypeDef,
        "PipelineDescription": str,
        "Tags": Sequence[TagTypeDef],
        "ParallelismConfiguration": ParallelismConfigurationTypeDef,
    },
    total=False,
)


class CreatePipelineRequestRequestTypeDef(
    _RequiredCreatePipelineRequestRequestTypeDef, _OptionalCreatePipelineRequestRequestTypeDef
):
    pass


_RequiredUpdatePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
_OptionalUpdatePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePipelineRequestRequestTypeDef",
    {
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDefinitionS3Location": PipelineDefinitionS3LocationTypeDef,
        "PipelineDescription": str,
        "RoleArn": str,
        "ParallelismConfiguration": ParallelismConfigurationTypeDef,
    },
    total=False,
)


class UpdatePipelineRequestRequestTypeDef(
    _RequiredUpdatePipelineRequestRequestTypeDef, _OptionalUpdatePipelineRequestRequestTypeDef
):
    pass


_RequiredCreateTrialComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)
_OptionalCreateTrialComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrialComponentRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Status": TrialComponentStatusTypeDef,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Parameters": Mapping[str, TrialComponentParameterValueTypeDef],
        "InputArtifacts": Mapping[str, TrialComponentArtifactTypeDef],
        "OutputArtifacts": Mapping[str, TrialComponentArtifactTypeDef],
        "MetadataProperties": MetadataPropertiesTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateTrialComponentRequestRequestTypeDef(
    _RequiredCreateTrialComponentRequestRequestTypeDef,
    _OptionalCreateTrialComponentRequestRequestTypeDef,
):
    pass


_RequiredUpdateTrialComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)
_OptionalUpdateTrialComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrialComponentRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Status": TrialComponentStatusTypeDef,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Parameters": Mapping[str, TrialComponentParameterValueTypeDef],
        "ParametersToRemove": Sequence[str],
        "InputArtifacts": Mapping[str, TrialComponentArtifactTypeDef],
        "InputArtifactsToRemove": Sequence[str],
        "OutputArtifacts": Mapping[str, TrialComponentArtifactTypeDef],
        "OutputArtifactsToRemove": Sequence[str],
    },
    total=False,
)


class UpdateTrialComponentRequestRequestTypeDef(
    _RequiredUpdateTrialComponentRequestRequestTypeDef,
    _OptionalUpdateTrialComponentRequestRequestTypeDef,
):
    pass


_RequiredCreateWorkforceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)
_OptionalCreateWorkforceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkforceRequestRequestTypeDef",
    {
        "CognitoConfig": CognitoConfigTypeDef,
        "OidcConfig": OidcConfigTypeDef,
        "SourceIpConfig": SourceIpConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
        "WorkforceVpcConfig": WorkforceVpcConfigRequestTypeDef,
    },
    total=False,
)


class CreateWorkforceRequestRequestTypeDef(
    _RequiredCreateWorkforceRequestRequestTypeDef, _OptionalCreateWorkforceRequestRequestTypeDef
):
    pass


_RequiredUpdateWorkforceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)
_OptionalUpdateWorkforceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkforceRequestRequestTypeDef",
    {
        "SourceIpConfig": SourceIpConfigTypeDef,
        "OidcConfig": OidcConfigTypeDef,
        "WorkforceVpcConfig": WorkforceVpcConfigRequestTypeDef,
    },
    total=False,
)


class UpdateWorkforceRequestRequestTypeDef(
    _RequiredUpdateWorkforceRequestRequestTypeDef, _OptionalUpdateWorkforceRequestRequestTypeDef
):
    pass


KernelGatewayAppSettingsTypeDef = TypedDict(
    "KernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecTypeDef,
        "CustomImages": Sequence[CustomImageTypeDef],
        "LifecycleConfigArns": Sequence[str],
    },
    total=False,
)

RSessionAppSettingsTypeDef = TypedDict(
    "RSessionAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecTypeDef,
        "CustomImages": Sequence[CustomImageTypeDef],
    },
    total=False,
)

ModelBiasBaselineConfigOutputTypeDef = TypedDict(
    "ModelBiasBaselineConfigOutputTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceOutputTypeDef,
    },
    total=False,
)

ModelExplainabilityBaselineConfigOutputTypeDef = TypedDict(
    "ModelExplainabilityBaselineConfigOutputTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceOutputTypeDef,
    },
    total=False,
)

ModelQualityBaselineConfigOutputTypeDef = TypedDict(
    "ModelQualityBaselineConfigOutputTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceOutputTypeDef,
    },
    total=False,
)

DataQualityBaselineConfigOutputTypeDef = TypedDict(
    "DataQualityBaselineConfigOutputTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceOutputTypeDef,
        "StatisticsResource": MonitoringStatisticsResourceOutputTypeDef,
    },
    total=False,
)

MonitoringBaselineConfigOutputTypeDef = TypedDict(
    "MonitoringBaselineConfigOutputTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceOutputTypeDef,
        "StatisticsResource": MonitoringStatisticsResourceOutputTypeDef,
    },
    total=False,
)

ModelBiasBaselineConfigTypeDef = TypedDict(
    "ModelBiasBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceTypeDef,
    },
    total=False,
)

ModelExplainabilityBaselineConfigTypeDef = TypedDict(
    "ModelExplainabilityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceTypeDef,
    },
    total=False,
)

ModelQualityBaselineConfigTypeDef = TypedDict(
    "ModelQualityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceTypeDef,
    },
    total=False,
)

DataQualityBaselineConfigTypeDef = TypedDict(
    "DataQualityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceTypeDef,
        "StatisticsResource": MonitoringStatisticsResourceTypeDef,
    },
    total=False,
)

MonitoringBaselineConfigTypeDef = TypedDict(
    "MonitoringBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": MonitoringConstraintsResourceTypeDef,
        "StatisticsResource": MonitoringStatisticsResourceTypeDef,
    },
    total=False,
)

DataSourceOutputTypeDef = TypedDict(
    "DataSourceOutputTypeDef",
    {
        "S3DataSource": S3DataSourceOutputTypeDef,
        "FileSystemDataSource": FileSystemDataSourceOutputTypeDef,
    },
    total=False,
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "S3DataSource": S3DataSourceTypeDef,
        "FileSystemDataSource": FileSystemDataSourceTypeDef,
    },
    total=False,
)

DatasetDefinitionOutputTypeDef = TypedDict(
    "DatasetDefinitionOutputTypeDef",
    {
        "AthenaDatasetDefinition": AthenaDatasetDefinitionOutputTypeDef,
        "RedshiftDatasetDefinition": RedshiftDatasetDefinitionOutputTypeDef,
        "LocalPath": str,
        "DataDistributionType": DataDistributionTypeType,
        "InputMode": InputModeType,
    },
    total=False,
)

DatasetDefinitionTypeDef = TypedDict(
    "DatasetDefinitionTypeDef",
    {
        "AthenaDatasetDefinition": AthenaDatasetDefinitionTypeDef,
        "RedshiftDatasetDefinition": RedshiftDatasetDefinitionTypeDef,
        "LocalPath": str,
        "DataDistributionType": DataDistributionTypeType,
        "InputMode": InputModeType,
    },
    total=False,
)

_RequiredDeleteDomainRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalDeleteDomainRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainRequestRequestTypeDef",
    {
        "RetentionPolicy": RetentionPolicyTypeDef,
    },
    total=False,
)


class DeleteDomainRequestRequestTypeDef(
    _RequiredDeleteDomainRequestRequestTypeDef, _OptionalDeleteDomainRequestRequestTypeDef
):
    pass


_RequiredDeploymentRecommendationTypeDef = TypedDict(
    "_RequiredDeploymentRecommendationTypeDef",
    {
        "RecommendationStatus": RecommendationStatusType,
    },
)
_OptionalDeploymentRecommendationTypeDef = TypedDict(
    "_OptionalDeploymentRecommendationTypeDef",
    {
        "RealTimeInferenceRecommendations": List[RealTimeInferenceRecommendationTypeDef],
    },
    total=False,
)


class DeploymentRecommendationTypeDef(
    _RequiredDeploymentRecommendationTypeDef, _OptionalDeploymentRecommendationTypeDef
):
    pass


DeploymentStageStatusSummaryTypeDef = TypedDict(
    "DeploymentStageStatusSummaryTypeDef",
    {
        "StageName": str,
        "DeviceSelectionConfig": DeviceSelectionConfigOutputTypeDef,
        "DeploymentConfig": EdgeDeploymentConfigOutputTypeDef,
        "DeploymentStatus": EdgeDeploymentStatusTypeDef,
    },
)

_RequiredDeploymentStageTypeDef = TypedDict(
    "_RequiredDeploymentStageTypeDef",
    {
        "StageName": str,
        "DeviceSelectionConfig": DeviceSelectionConfigTypeDef,
    },
)
_OptionalDeploymentStageTypeDef = TypedDict(
    "_OptionalDeploymentStageTypeDef",
    {
        "DeploymentConfig": EdgeDeploymentConfigTypeDef,
    },
    total=False,
)


class DeploymentStageTypeDef(_RequiredDeploymentStageTypeDef, _OptionalDeploymentStageTypeDef):
    pass


DescribeAppResponseTypeDef = TypedDict(
    "DescribeAppResponseTypeDef",
    {
        "AppArn": str,
        "AppType": AppTypeType,
        "AppName": str,
        "DomainId": str,
        "UserProfileName": str,
        "Status": AppStatusType,
        "LastHealthCheckTimestamp": datetime,
        "LastUserActivityTimestamp": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "ResourceSpec": ResourceSpecOutputTypeDef,
        "SpaceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

JupyterServerAppSettingsOutputTypeDef = TypedDict(
    "JupyterServerAppSettingsOutputTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecOutputTypeDef,
        "LifecycleConfigArns": List[str],
        "CodeRepositories": List[CodeRepositoryOutputTypeDef],
    },
    total=False,
)

KernelGatewayAppSettingsOutputTypeDef = TypedDict(
    "KernelGatewayAppSettingsOutputTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecOutputTypeDef,
        "CustomImages": List[CustomImageOutputTypeDef],
        "LifecycleConfigArns": List[str],
    },
    total=False,
)

RSessionAppSettingsOutputTypeDef = TypedDict(
    "RSessionAppSettingsOutputTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecOutputTypeDef,
        "CustomImages": List[CustomImageOutputTypeDef],
    },
    total=False,
)

_RequiredRStudioServerProDomainSettingsOutputTypeDef = TypedDict(
    "_RequiredRStudioServerProDomainSettingsOutputTypeDef",
    {
        "DomainExecutionRoleArn": str,
    },
)
_OptionalRStudioServerProDomainSettingsOutputTypeDef = TypedDict(
    "_OptionalRStudioServerProDomainSettingsOutputTypeDef",
    {
        "RStudioConnectUrl": str,
        "RStudioPackageManagerUrl": str,
        "DefaultResourceSpec": ResourceSpecOutputTypeDef,
    },
    total=False,
)


class RStudioServerProDomainSettingsOutputTypeDef(
    _RequiredRStudioServerProDomainSettingsOutputTypeDef,
    _OptionalRStudioServerProDomainSettingsOutputTypeDef,
):
    pass


TensorBoardAppSettingsOutputTypeDef = TypedDict(
    "TensorBoardAppSettingsOutputTypeDef",
    {
        "DefaultResourceSpec": ResourceSpecOutputTypeDef,
    },
    total=False,
)

DescribeDeviceFleetResponseTypeDef = TypedDict(
    "DescribeDeviceFleetResponseTypeDef",
    {
        "DeviceFleetName": str,
        "DeviceFleetArn": str,
        "OutputConfig": EdgeOutputConfigOutputTypeDef,
        "Description": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "IotRoleAlias": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "DeviceArn": str,
        "DeviceName": str,
        "Description": str,
        "DeviceFleetName": str,
        "IotThingName": str,
        "RegistrationTime": datetime,
        "LatestHeartbeat": datetime,
        "Models": List[EdgeModelTypeDef],
        "MaxModels": int,
        "NextToken": str,
        "AgentVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeEdgePackagingJobResponseTypeDef = TypedDict(
    "DescribeEdgePackagingJobResponseTypeDef",
    {
        "EdgePackagingJobArn": str,
        "EdgePackagingJobName": str,
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "RoleArn": str,
        "OutputConfig": EdgeOutputConfigOutputTypeDef,
        "ResourceKey": str,
        "EdgePackagingJobStatus": EdgePackagingJobStatusType,
        "EdgePackagingJobStatusMessage": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ModelArtifact": str,
        "ModelSignature": str,
        "PresetDeploymentOutput": EdgePresetDeploymentOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredDescribeEndpointInputEndpointDeletedWaitTypeDef = TypedDict(
    "_RequiredDescribeEndpointInputEndpointDeletedWaitTypeDef",
    {
        "EndpointName": str,
    },
)
_OptionalDescribeEndpointInputEndpointDeletedWaitTypeDef = TypedDict(
    "_OptionalDescribeEndpointInputEndpointDeletedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeEndpointInputEndpointDeletedWaitTypeDef(
    _RequiredDescribeEndpointInputEndpointDeletedWaitTypeDef,
    _OptionalDescribeEndpointInputEndpointDeletedWaitTypeDef,
):
    pass


_RequiredDescribeEndpointInputEndpointInServiceWaitTypeDef = TypedDict(
    "_RequiredDescribeEndpointInputEndpointInServiceWaitTypeDef",
    {
        "EndpointName": str,
    },
)
_OptionalDescribeEndpointInputEndpointInServiceWaitTypeDef = TypedDict(
    "_OptionalDescribeEndpointInputEndpointInServiceWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeEndpointInputEndpointInServiceWaitTypeDef(
    _RequiredDescribeEndpointInputEndpointInServiceWaitTypeDef,
    _OptionalDescribeEndpointInputEndpointInServiceWaitTypeDef,
):
    pass


_RequiredDescribeImageRequestImageCreatedWaitTypeDef = TypedDict(
    "_RequiredDescribeImageRequestImageCreatedWaitTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDescribeImageRequestImageCreatedWaitTypeDef = TypedDict(
    "_OptionalDescribeImageRequestImageCreatedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeImageRequestImageCreatedWaitTypeDef(
    _RequiredDescribeImageRequestImageCreatedWaitTypeDef,
    _OptionalDescribeImageRequestImageCreatedWaitTypeDef,
):
    pass


_RequiredDescribeImageRequestImageDeletedWaitTypeDef = TypedDict(
    "_RequiredDescribeImageRequestImageDeletedWaitTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDescribeImageRequestImageDeletedWaitTypeDef = TypedDict(
    "_OptionalDescribeImageRequestImageDeletedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeImageRequestImageDeletedWaitTypeDef(
    _RequiredDescribeImageRequestImageDeletedWaitTypeDef,
    _OptionalDescribeImageRequestImageDeletedWaitTypeDef,
):
    pass


_RequiredDescribeImageRequestImageUpdatedWaitTypeDef = TypedDict(
    "_RequiredDescribeImageRequestImageUpdatedWaitTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDescribeImageRequestImageUpdatedWaitTypeDef = TypedDict(
    "_OptionalDescribeImageRequestImageUpdatedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeImageRequestImageUpdatedWaitTypeDef(
    _RequiredDescribeImageRequestImageUpdatedWaitTypeDef,
    _OptionalDescribeImageRequestImageUpdatedWaitTypeDef,
):
    pass


_RequiredDescribeImageVersionRequestImageVersionCreatedWaitTypeDef = TypedDict(
    "_RequiredDescribeImageVersionRequestImageVersionCreatedWaitTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDescribeImageVersionRequestImageVersionCreatedWaitTypeDef = TypedDict(
    "_OptionalDescribeImageVersionRequestImageVersionCreatedWaitTypeDef",
    {
        "Version": int,
        "Alias": str,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeImageVersionRequestImageVersionCreatedWaitTypeDef(
    _RequiredDescribeImageVersionRequestImageVersionCreatedWaitTypeDef,
    _OptionalDescribeImageVersionRequestImageVersionCreatedWaitTypeDef,
):
    pass


_RequiredDescribeImageVersionRequestImageVersionDeletedWaitTypeDef = TypedDict(
    "_RequiredDescribeImageVersionRequestImageVersionDeletedWaitTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDescribeImageVersionRequestImageVersionDeletedWaitTypeDef = TypedDict(
    "_OptionalDescribeImageVersionRequestImageVersionDeletedWaitTypeDef",
    {
        "Version": int,
        "Alias": str,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeImageVersionRequestImageVersionDeletedWaitTypeDef(
    _RequiredDescribeImageVersionRequestImageVersionDeletedWaitTypeDef,
    _OptionalDescribeImageVersionRequestImageVersionDeletedWaitTypeDef,
):
    pass


_RequiredDescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef = TypedDict(
    "_RequiredDescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalDescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef = TypedDict(
    "_OptionalDescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef(
    _RequiredDescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef,
    _OptionalDescribeNotebookInstanceInputNotebookInstanceDeletedWaitTypeDef,
):
    pass


_RequiredDescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef = TypedDict(
    "_RequiredDescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalDescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef = TypedDict(
    "_OptionalDescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef(
    _RequiredDescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef,
    _OptionalDescribeNotebookInstanceInputNotebookInstanceInServiceWaitTypeDef,
):
    pass


_RequiredDescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef = TypedDict(
    "_RequiredDescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalDescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef = TypedDict(
    "_OptionalDescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef(
    _RequiredDescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef,
    _OptionalDescribeNotebookInstanceInputNotebookInstanceStoppedWaitTypeDef,
):
    pass


_RequiredDescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef = TypedDict(
    "_RequiredDescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef",
    {
        "ProcessingJobName": str,
    },
)
_OptionalDescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef = TypedDict(
    "_OptionalDescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef(
    _RequiredDescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef,
    _OptionalDescribeProcessingJobRequestProcessingJobCompletedOrStoppedWaitTypeDef,
):
    pass


_RequiredDescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef = TypedDict(
    "_RequiredDescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef",
    {
        "TrainingJobName": str,
    },
)
_OptionalDescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef = TypedDict(
    "_OptionalDescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef(
    _RequiredDescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef,
    _OptionalDescribeTrainingJobRequestTrainingJobCompletedOrStoppedWaitTypeDef,
):
    pass


_RequiredDescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef = TypedDict(
    "_RequiredDescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef",
    {
        "TransformJobName": str,
    },
)
_OptionalDescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef = TypedDict(
    "_OptionalDescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef(
    _RequiredDescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef,
    _OptionalDescribeTransformJobRequestTransformJobCompletedOrStoppedWaitTypeDef,
):
    pass


ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "ExperimentArn": str,
        "ExperimentName": str,
        "DisplayName": str,
        "ExperimentSource": ExperimentSourceTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredFeatureGroupSummaryTypeDef = TypedDict(
    "_RequiredFeatureGroupSummaryTypeDef",
    {
        "FeatureGroupName": str,
        "FeatureGroupArn": str,
        "CreationTime": datetime,
    },
)
_OptionalFeatureGroupSummaryTypeDef = TypedDict(
    "_OptionalFeatureGroupSummaryTypeDef",
    {
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": OfflineStoreStatusTypeDef,
    },
    total=False,
)


class FeatureGroupSummaryTypeDef(
    _RequiredFeatureGroupSummaryTypeDef, _OptionalFeatureGroupSummaryTypeDef
):
    pass


DescribeFeatureMetadataResponseTypeDef = TypedDict(
    "DescribeFeatureMetadataResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "FeatureName": str,
        "FeatureType": FeatureTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Description": str,
        "Parameters": List[FeatureParameterOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FeatureMetadataTypeDef = TypedDict(
    "FeatureMetadataTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "FeatureName": str,
        "FeatureType": FeatureTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Description": str,
        "Parameters": List[FeatureParameterOutputTypeDef],
    },
    total=False,
)

DescribeHubContentResponseTypeDef = TypedDict(
    "DescribeHubContentResponseTypeDef",
    {
        "HubContentName": str,
        "HubContentArn": str,
        "HubContentVersion": str,
        "HubContentType": HubContentTypeType,
        "DocumentSchemaVersion": str,
        "HubName": str,
        "HubArn": str,
        "HubContentDisplayName": str,
        "HubContentDescription": str,
        "HubContentMarkdown": str,
        "HubContentDocument": str,
        "HubContentSearchKeywords": List[str],
        "HubContentDependencies": List[HubContentDependencyTypeDef],
        "HubContentStatus": HubContentStatusType,
        "FailureReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeHubResponseTypeDef = TypedDict(
    "DescribeHubResponseTypeDef",
    {
        "HubName": str,
        "HubArn": str,
        "HubDisplayName": str,
        "HubDescription": str,
        "HubSearchKeywords": List[str],
        "S3StorageConfig": HubS3StorageConfigOutputTypeDef,
        "HubStatus": HubStatusType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeHumanTaskUiResponseTypeDef = TypedDict(
    "DescribeHumanTaskUiResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "HumanTaskUiName": str,
        "HumanTaskUiStatus": HumanTaskUiStatusType,
        "CreationTime": datetime,
        "UiTemplate": UiTemplateInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredInferenceExperimentSummaryTypeDef = TypedDict(
    "_RequiredInferenceExperimentSummaryTypeDef",
    {
        "Name": str,
        "Type": Literal["ShadowMode"],
        "Status": InferenceExperimentStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalInferenceExperimentSummaryTypeDef = TypedDict(
    "_OptionalInferenceExperimentSummaryTypeDef",
    {
        "Schedule": InferenceExperimentScheduleOutputTypeDef,
        "StatusReason": str,
        "Description": str,
        "CompletionTime": datetime,
        "RoleArn": str,
    },
    total=False,
)


class InferenceExperimentSummaryTypeDef(
    _RequiredInferenceExperimentSummaryTypeDef, _OptionalInferenceExperimentSummaryTypeDef
):
    pass


DescribeModelCardExportJobResponseTypeDef = TypedDict(
    "DescribeModelCardExportJobResponseTypeDef",
    {
        "ModelCardExportJobName": str,
        "ModelCardExportJobArn": str,
        "Status": ModelCardExportJobStatusType,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "OutputConfig": ModelCardExportOutputConfigOutputTypeDef,
        "CreatedAt": datetime,
        "LastModifiedAt": datetime,
        "FailureReason": str,
        "ExportArtifacts": ModelCardExportArtifactsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMonitoringExecutionsResponseTypeDef = TypedDict(
    "ListMonitoringExecutionsResponseTypeDef",
    {
        "MonitoringExecutionSummaries": List[MonitoringExecutionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeNotebookInstanceLifecycleConfigOutputTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": List[NotebookInstanceLifecycleHookOutputTypeDef],
        "OnStart": List[NotebookInstanceLifecycleHookOutputTypeDef],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeNotebookInstanceOutputTypeDef = TypedDict(
    "DescribeNotebookInstanceOutputTypeDef",
    {
        "NotebookInstanceArn": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": NotebookInstanceStatusType,
        "FailureReason": str,
        "Url": str,
        "InstanceType": InstanceTypeType,
        "SubnetId": str,
        "SecurityGroups": List[str],
        "RoleArn": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DirectInternetAccess": DirectInternetAccessType,
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[NotebookInstanceAcceleratorTypeType],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": RootAccessType,
        "PlatformIdentifier": str,
        "InstanceMetadataServiceConfiguration": InstanceMetadataServiceConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeSubscribedWorkteamResponseTypeDef = TypedDict(
    "DescribeSubscribedWorkteamResponseTypeDef",
    {
        "SubscribedWorkteam": SubscribedWorkteamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "ListSubscribedWorkteamsResponseTypeDef",
    {
        "SubscribedWorkteams": List[SubscribedWorkteamTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": TrainingJobStatusType,
    },
)
_OptionalTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalTrainingJobSummaryTypeDef",
    {
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "WarmPoolStatus": WarmPoolStatusTypeDef,
    },
    total=False,
)


class TrainingJobSummaryTypeDef(
    _RequiredTrainingJobSummaryTypeDef, _OptionalTrainingJobSummaryTypeDef
):
    pass


TrialSummaryTypeDef = TypedDict(
    "TrialSummaryTypeDef",
    {
        "TrialArn": str,
        "TrialName": str,
        "DisplayName": str,
        "TrialSource": TrialSourceTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredDesiredWeightAndCapacityTypeDef = TypedDict(
    "_RequiredDesiredWeightAndCapacityTypeDef",
    {
        "VariantName": str,
    },
)
_OptionalDesiredWeightAndCapacityTypeDef = TypedDict(
    "_OptionalDesiredWeightAndCapacityTypeDef",
    {
        "DesiredWeight": float,
        "DesiredInstanceCount": int,
        "ServerlessUpdateConfig": ProductionVariantServerlessUpdateConfigTypeDef,
    },
    total=False,
)


class DesiredWeightAndCapacityTypeDef(
    _RequiredDesiredWeightAndCapacityTypeDef, _OptionalDesiredWeightAndCapacityTypeDef
):
    pass


ListStageDevicesResponseTypeDef = TypedDict(
    "ListStageDevicesResponseTypeDef",
    {
        "DeviceDeploymentSummaries": List[DeviceDeploymentSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDeviceFleetsResponseTypeDef = TypedDict(
    "ListDeviceFleetsResponseTypeDef",
    {
        "DeviceFleetSummaries": List[DeviceFleetSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredDeviceSummaryTypeDef = TypedDict(
    "_RequiredDeviceSummaryTypeDef",
    {
        "DeviceName": str,
        "DeviceArn": str,
    },
)
_OptionalDeviceSummaryTypeDef = TypedDict(
    "_OptionalDeviceSummaryTypeDef",
    {
        "Description": str,
        "DeviceFleetName": str,
        "IotThingName": str,
        "RegistrationTime": datetime,
        "LatestHeartbeat": datetime,
        "Models": List[EdgeModelSummaryTypeDef],
        "AgentVersion": str,
    },
    total=False,
)


class DeviceSummaryTypeDef(_RequiredDeviceSummaryTypeDef, _OptionalDeviceSummaryTypeDef):
    pass


_RequiredRegisterDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "Devices": Sequence[DeviceTypeDef],
    },
)
_OptionalRegisterDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterDevicesRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class RegisterDevicesRequestRequestTypeDef(
    _RequiredRegisterDevicesRequestRequestTypeDef, _OptionalRegisterDevicesRequestRequestTypeDef
):
    pass


UpdateDevicesRequestRequestTypeDef = TypedDict(
    "UpdateDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "Devices": Sequence[DeviceTypeDef],
    },
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List[DomainDetailsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DriftCheckBiasOutputTypeDef = TypedDict(
    "DriftCheckBiasOutputTypeDef",
    {
        "ConfigFile": FileSourceOutputTypeDef,
        "PreTrainingConstraints": MetricsSourceOutputTypeDef,
        "PostTrainingConstraints": MetricsSourceOutputTypeDef,
    },
    total=False,
)

DriftCheckExplainabilityOutputTypeDef = TypedDict(
    "DriftCheckExplainabilityOutputTypeDef",
    {
        "Constraints": MetricsSourceOutputTypeDef,
        "ConfigFile": FileSourceOutputTypeDef,
    },
    total=False,
)

DriftCheckBiasTypeDef = TypedDict(
    "DriftCheckBiasTypeDef",
    {
        "ConfigFile": FileSourceTypeDef,
        "PreTrainingConstraints": MetricsSourceTypeDef,
        "PostTrainingConstraints": MetricsSourceTypeDef,
    },
    total=False,
)

DriftCheckExplainabilityTypeDef = TypedDict(
    "DriftCheckExplainabilityTypeDef",
    {
        "Constraints": MetricsSourceTypeDef,
        "ConfigFile": FileSourceTypeDef,
    },
    total=False,
)

ListEdgeDeploymentPlansResponseTypeDef = TypedDict(
    "ListEdgeDeploymentPlansResponseTypeDef",
    {
        "EdgeDeploymentPlanSummaries": List[EdgeDeploymentPlanSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDeviceFleetReportResponseTypeDef = TypedDict(
    "GetDeviceFleetReportResponseTypeDef",
    {
        "DeviceFleetArn": str,
        "DeviceFleetName": str,
        "OutputConfig": EdgeOutputConfigOutputTypeDef,
        "Description": str,
        "ReportGenerated": datetime,
        "DeviceStats": DeviceStatsTypeDef,
        "AgentVersions": List[AgentVersionTypeDef],
        "ModelStats": List[EdgeModelStatTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListEdgePackagingJobsResponseTypeDef = TypedDict(
    "ListEdgePackagingJobsResponseTypeDef",
    {
        "EdgePackagingJobSummaries": List[EdgePackagingJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListEndpointConfigsOutputTypeDef = TypedDict(
    "ListEndpointConfigsOutputTypeDef",
    {
        "EndpointConfigs": List[EndpointConfigSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredEndpointOutputConfigurationTypeDef = TypedDict(
    "_RequiredEndpointOutputConfigurationTypeDef",
    {
        "EndpointName": str,
        "VariantName": str,
    },
)
_OptionalEndpointOutputConfigurationTypeDef = TypedDict(
    "_OptionalEndpointOutputConfigurationTypeDef",
    {
        "InstanceType": ProductionVariantInstanceTypeType,
        "InitialInstanceCount": int,
        "ServerlessConfig": ProductionVariantServerlessConfigOutputTypeDef,
    },
    total=False,
)


class EndpointOutputConfigurationTypeDef(
    _RequiredEndpointOutputConfigurationTypeDef, _OptionalEndpointOutputConfigurationTypeDef
):
    pass


EndpointPerformanceTypeDef = TypedDict(
    "EndpointPerformanceTypeDef",
    {
        "Metrics": InferenceMetricsTypeDef,
        "EndpointInfo": EndpointInfoOutputTypeDef,
    },
)

ListEndpointsOutputTypeDef = TypedDict(
    "ListEndpointsOutputTypeDef",
    {
        "Endpoints": List[EndpointSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ModelConfigurationTypeDef = TypedDict(
    "ModelConfigurationTypeDef",
    {
        "InferenceSpecificationName": str,
        "EnvironmentParameters": List[EnvironmentParameterTypeDef],
        "CompilationJobName": str,
    },
    total=False,
)

_RequiredUpdateFeatureMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFeatureMetadataRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "FeatureName": str,
    },
)
_OptionalUpdateFeatureMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFeatureMetadataRequestRequestTypeDef",
    {
        "Description": str,
        "ParameterAdditions": Sequence[FeatureParameterTypeDef],
        "ParameterRemovals": Sequence[str],
    },
    total=False,
)


class UpdateFeatureMetadataRequestRequestTypeDef(
    _RequiredUpdateFeatureMetadataRequestRequestTypeDef,
    _OptionalUpdateFeatureMetadataRequestRequestTypeDef,
):
    pass


NestedFiltersTypeDef = TypedDict(
    "NestedFiltersTypeDef",
    {
        "NestedPropertyName": str,
        "Filters": Sequence[FilterTypeDef],
    },
)

_RequiredHyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": TrainingJobStatusType,
        "TunedHyperParameters": Dict[str, str],
    },
)
_OptionalHyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalHyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobDefinitionName": str,
        "TuningJobName": str,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": (
            FinalHyperParameterTuningJobObjectiveMetricTypeDef
        ),
        "ObjectiveStatus": ObjectiveStatusType,
    },
    total=False,
)


class HyperParameterTrainingJobSummaryTypeDef(
    _RequiredHyperParameterTrainingJobSummaryTypeDef,
    _OptionalHyperParameterTrainingJobSummaryTypeDef,
):
    pass


ListFlowDefinitionsResponseTypeDef = TypedDict(
    "ListFlowDefinitionsResponseTypeDef",
    {
        "FlowDefinitionSummaries": List[FlowDefinitionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSearchSuggestionsResponseTypeDef = TypedDict(
    "GetSearchSuggestionsResponseTypeDef",
    {
        "PropertyNameSuggestions": List[PropertyNameSuggestionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateCodeRepositoryInputRequestTypeDef = TypedDict(
    "_RequiredUpdateCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
    },
)
_OptionalUpdateCodeRepositoryInputRequestTypeDef = TypedDict(
    "_OptionalUpdateCodeRepositoryInputRequestTypeDef",
    {
        "GitConfig": GitConfigForUpdateTypeDef,
    },
    total=False,
)


class UpdateCodeRepositoryInputRequestTypeDef(
    _RequiredUpdateCodeRepositoryInputRequestTypeDef,
    _OptionalUpdateCodeRepositoryInputRequestTypeDef,
):
    pass


ListHubContentVersionsResponseTypeDef = TypedDict(
    "ListHubContentVersionsResponseTypeDef",
    {
        "HubContentSummaries": List[HubContentInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListHubContentsResponseTypeDef = TypedDict(
    "ListHubContentsResponseTypeDef",
    {
        "HubContentSummaries": List[HubContentInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListHubsResponseTypeDef = TypedDict(
    "ListHubsResponseTypeDef",
    {
        "HubSummaries": List[HubInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

HumanLoopActivationConfigOutputTypeDef = TypedDict(
    "HumanLoopActivationConfigOutputTypeDef",
    {
        "HumanLoopActivationConditionsConfig": HumanLoopActivationConditionsConfigOutputTypeDef,
    },
)

HumanLoopActivationConfigTypeDef = TypedDict(
    "HumanLoopActivationConfigTypeDef",
    {
        "HumanLoopActivationConditionsConfig": HumanLoopActivationConditionsConfigTypeDef,
    },
)

ListHumanTaskUisResponseTypeDef = TypedDict(
    "ListHumanTaskUisResponseTypeDef",
    {
        "HumanTaskUiSummaries": List[HumanTaskUiSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

HyperParameterTuningResourceConfigOutputTypeDef = TypedDict(
    "HyperParameterTuningResourceConfigOutputTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
        "AllocationStrategy": Literal["Prioritized"],
        "InstanceConfigs": List[HyperParameterTuningInstanceConfigOutputTypeDef],
    },
    total=False,
)

HyperParameterTuningResourceConfigTypeDef = TypedDict(
    "HyperParameterTuningResourceConfigTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
        "AllocationStrategy": Literal["Prioritized"],
        "InstanceConfigs": Sequence[HyperParameterTuningInstanceConfigTypeDef],
    },
    total=False,
)

_RequiredHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "CreationTime": datetime,
        "TrainingJobStatusCounters": TrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ObjectiveStatusCountersTypeDef,
    },
)
_OptionalHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "ResourceLimits": ResourceLimitsOutputTypeDef,
    },
    total=False,
)


class HyperParameterTuningJobSummaryTypeDef(
    _RequiredHyperParameterTuningJobSummaryTypeDef, _OptionalHyperParameterTuningJobSummaryTypeDef
):
    pass


HyperParameterTuningJobStrategyConfigOutputTypeDef = TypedDict(
    "HyperParameterTuningJobStrategyConfigOutputTypeDef",
    {
        "HyperbandStrategyConfig": HyperbandStrategyConfigOutputTypeDef,
    },
    total=False,
)

HyperParameterTuningJobStrategyConfigTypeDef = TypedDict(
    "HyperParameterTuningJobStrategyConfigTypeDef",
    {
        "HyperbandStrategyConfig": HyperbandStrategyConfigTypeDef,
    },
    total=False,
)

HyperParameterTuningJobWarmStartConfigOutputTypeDef = TypedDict(
    "HyperParameterTuningJobWarmStartConfigOutputTypeDef",
    {
        "ParentHyperParameterTuningJobs": List[ParentHyperParameterTuningJobOutputTypeDef],
        "WarmStartType": HyperParameterTuningJobWarmStartTypeType,
    },
)

HyperParameterTuningJobWarmStartConfigTypeDef = TypedDict(
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    {
        "ParentHyperParameterTuningJobs": Sequence[ParentHyperParameterTuningJobTypeDef],
        "WarmStartType": HyperParameterTuningJobWarmStartTypeType,
    },
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "UserProfileArn": str,
        "UserProfileName": str,
        "DomainId": str,
        "IamIdentity": IamIdentityTypeDef,
    },
    total=False,
)

_RequiredImageConfigOutputTypeDef = TypedDict(
    "_RequiredImageConfigOutputTypeDef",
    {
        "RepositoryAccessMode": RepositoryAccessModeType,
    },
)
_OptionalImageConfigOutputTypeDef = TypedDict(
    "_OptionalImageConfigOutputTypeDef",
    {
        "RepositoryAuthConfig": RepositoryAuthConfigOutputTypeDef,
    },
    total=False,
)


class ImageConfigOutputTypeDef(
    _RequiredImageConfigOutputTypeDef, _OptionalImageConfigOutputTypeDef
):
    pass


_RequiredImageConfigTypeDef = TypedDict(
    "_RequiredImageConfigTypeDef",
    {
        "RepositoryAccessMode": RepositoryAccessModeType,
    },
)
_OptionalImageConfigTypeDef = TypedDict(
    "_OptionalImageConfigTypeDef",
    {
        "RepositoryAuthConfig": RepositoryAuthConfigTypeDef,
    },
    total=False,
)


class ImageConfigTypeDef(_RequiredImageConfigTypeDef, _OptionalImageConfigTypeDef):
    pass


ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "Images": List[ImageTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListImageVersionsResponseTypeDef = TypedDict(
    "ListImageVersionsResponseTypeDef",
    {
        "ImageVersions": List[ImageVersionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListInferenceRecommendationsJobsResponseTypeDef = TypedDict(
    "ListInferenceRecommendationsJobsResponseTypeDef",
    {
        "InferenceRecommendationsJobs": List[InferenceRecommendationsJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredResourceConfigOutputTypeDef = TypedDict(
    "_RequiredResourceConfigOutputTypeDef",
    {
        "VolumeSizeInGB": int,
    },
)
_OptionalResourceConfigOutputTypeDef = TypedDict(
    "_OptionalResourceConfigOutputTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
        "InstanceGroups": List[InstanceGroupOutputTypeDef],
        "KeepAlivePeriodInSeconds": int,
    },
    total=False,
)


class ResourceConfigOutputTypeDef(
    _RequiredResourceConfigOutputTypeDef, _OptionalResourceConfigOutputTypeDef
):
    pass


_RequiredResourceConfigTypeDef = TypedDict(
    "_RequiredResourceConfigTypeDef",
    {
        "VolumeSizeInGB": int,
    },
)
_OptionalResourceConfigTypeDef = TypedDict(
    "_OptionalResourceConfigTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
        "InstanceGroups": Sequence[InstanceGroupTypeDef],
        "KeepAlivePeriodInSeconds": int,
    },
    total=False,
)


class ResourceConfigTypeDef(_RequiredResourceConfigTypeDef, _OptionalResourceConfigTypeDef):
    pass


ParameterRangesOutputTypeDef = TypedDict(
    "ParameterRangesOutputTypeDef",
    {
        "IntegerParameterRanges": List[IntegerParameterRangeOutputTypeDef],
        "ContinuousParameterRanges": List[ContinuousParameterRangeOutputTypeDef],
        "CategoricalParameterRanges": List[CategoricalParameterRangeOutputTypeDef],
        "AutoParameters": List[AutoParameterOutputTypeDef],
    },
    total=False,
)

ParameterRangeOutputTypeDef = TypedDict(
    "ParameterRangeOutputTypeDef",
    {
        "IntegerParameterRangeSpecification": IntegerParameterRangeSpecificationOutputTypeDef,
        "ContinuousParameterRangeSpecification": ContinuousParameterRangeSpecificationOutputTypeDef,
        "CategoricalParameterRangeSpecification": (
            CategoricalParameterRangeSpecificationOutputTypeDef
        ),
    },
    total=False,
)

ParameterRangeTypeDef = TypedDict(
    "ParameterRangeTypeDef",
    {
        "IntegerParameterRangeSpecification": IntegerParameterRangeSpecificationTypeDef,
        "ContinuousParameterRangeSpecification": ContinuousParameterRangeSpecificationTypeDef,
        "CategoricalParameterRangeSpecification": CategoricalParameterRangeSpecificationTypeDef,
    },
    total=False,
)

ParameterRangesTypeDef = TypedDict(
    "ParameterRangesTypeDef",
    {
        "IntegerParameterRanges": Sequence[IntegerParameterRangeTypeDef],
        "ContinuousParameterRanges": Sequence[ContinuousParameterRangeTypeDef],
        "CategoricalParameterRanges": Sequence[CategoricalParameterRangeTypeDef],
        "AutoParameters": Sequence[AutoParameterTypeDef],
    },
    total=False,
)

_RequiredKernelGatewayImageConfigOutputTypeDef = TypedDict(
    "_RequiredKernelGatewayImageConfigOutputTypeDef",
    {
        "KernelSpecs": List[KernelSpecOutputTypeDef],
    },
)
_OptionalKernelGatewayImageConfigOutputTypeDef = TypedDict(
    "_OptionalKernelGatewayImageConfigOutputTypeDef",
    {
        "FileSystemConfig": FileSystemConfigOutputTypeDef,
    },
    total=False,
)


class KernelGatewayImageConfigOutputTypeDef(
    _RequiredKernelGatewayImageConfigOutputTypeDef, _OptionalKernelGatewayImageConfigOutputTypeDef
):
    pass


_RequiredKernelGatewayImageConfigTypeDef = TypedDict(
    "_RequiredKernelGatewayImageConfigTypeDef",
    {
        "KernelSpecs": Sequence[KernelSpecTypeDef],
    },
)
_OptionalKernelGatewayImageConfigTypeDef = TypedDict(
    "_OptionalKernelGatewayImageConfigTypeDef",
    {
        "FileSystemConfig": FileSystemConfigTypeDef,
    },
    total=False,
)


class KernelGatewayImageConfigTypeDef(
    _RequiredKernelGatewayImageConfigTypeDef, _OptionalKernelGatewayImageConfigTypeDef
):
    pass


_RequiredLabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobForWorkteamSummaryTypeDef",
    {
        "JobReferenceCode": str,
        "WorkRequesterAccountId": str,
        "CreationTime": datetime,
    },
)
_OptionalLabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "_OptionalLabelingJobForWorkteamSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelCounters": LabelCountersForWorkteamTypeDef,
        "NumberOfHumanWorkersPerDataObject": int,
    },
    total=False,
)


class LabelingJobForWorkteamSummaryTypeDef(
    _RequiredLabelingJobForWorkteamSummaryTypeDef, _OptionalLabelingJobForWorkteamSummaryTypeDef
):
    pass


LabelingJobDataSourceOutputTypeDef = TypedDict(
    "LabelingJobDataSourceOutputTypeDef",
    {
        "S3DataSource": LabelingJobS3DataSourceOutputTypeDef,
        "SnsDataSource": LabelingJobSnsDataSourceOutputTypeDef,
    },
    total=False,
)

LabelingJobDataSourceTypeDef = TypedDict(
    "LabelingJobDataSourceTypeDef",
    {
        "S3DataSource": LabelingJobS3DataSourceTypeDef,
        "SnsDataSource": LabelingJobSnsDataSourceTypeDef,
    },
    total=False,
)

ListLineageGroupsResponseTypeDef = TypedDict(
    "ListLineageGroupsResponseTypeDef",
    {
        "LineageGroupSummaries": List[LineageGroupSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListActionsRequestListActionsPaginateTypeDef = TypedDict(
    "ListActionsRequestListActionsPaginateTypeDef",
    {
        "SourceUri": str,
        "ActionType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortActionsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListAlgorithmsInputListAlgorithmsPaginateTypeDef = TypedDict(
    "ListAlgorithmsInputListAlgorithmsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": AlgorithmSortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListAliasesRequestListAliasesPaginateTypeDef = TypedDict(
    "_RequiredListAliasesRequestListAliasesPaginateTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalListAliasesRequestListAliasesPaginateTypeDef = TypedDict(
    "_OptionalListAliasesRequestListAliasesPaginateTypeDef",
    {
        "Alias": str,
        "Version": int,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAliasesRequestListAliasesPaginateTypeDef(
    _RequiredListAliasesRequestListAliasesPaginateTypeDef,
    _OptionalListAliasesRequestListAliasesPaginateTypeDef,
):
    pass


ListAppImageConfigsRequestListAppImageConfigsPaginateTypeDef = TypedDict(
    "ListAppImageConfigsRequestListAppImageConfigsPaginateTypeDef",
    {
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "ModifiedTimeBefore": Union[datetime, str],
        "ModifiedTimeAfter": Union[datetime, str],
        "SortBy": AppImageConfigSortKeyType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListAppsRequestListAppsPaginateTypeDef = TypedDict(
    "ListAppsRequestListAppsPaginateTypeDef",
    {
        "SortOrder": SortOrderType,
        "SortBy": Literal["CreationTime"],
        "DomainIdEquals": str,
        "UserProfileNameEquals": str,
        "SpaceNameEquals": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListArtifactsRequestListArtifactsPaginateTypeDef = TypedDict(
    "ListArtifactsRequestListArtifactsPaginateTypeDef",
    {
        "SourceUri": str,
        "ArtifactType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": Literal["CreationTime"],
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListAssociationsRequestListAssociationsPaginateTypeDef = TypedDict(
    "ListAssociationsRequestListAssociationsPaginateTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "SourceType": str,
        "DestinationType": str,
        "AssociationType": AssociationEdgeTypeType,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortAssociationsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListAutoMLJobsRequestListAutoMLJobsPaginateTypeDef = TypedDict(
    "ListAutoMLJobsRequestListAutoMLJobsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": AutoMLJobStatusType,
        "SortOrder": AutoMLSortOrderType,
        "SortBy": AutoMLSortByType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef = TypedDict(
    "_RequiredListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef",
    {
        "AutoMLJobName": str,
    },
)
_OptionalListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef = TypedDict(
    "_OptionalListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef",
    {
        "StatusEquals": CandidateStatusType,
        "CandidateNameEquals": str,
        "SortOrder": AutoMLSortOrderType,
        "SortBy": CandidateSortByType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef(
    _RequiredListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef,
    _OptionalListCandidatesForAutoMLJobRequestListCandidatesForAutoMLJobPaginateTypeDef,
):
    pass


ListCodeRepositoriesInputListCodeRepositoriesPaginateTypeDef = TypedDict(
    "ListCodeRepositoriesInputListCodeRepositoriesPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": CodeRepositorySortByType,
        "SortOrder": CodeRepositorySortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListCompilationJobsRequestListCompilationJobsPaginateTypeDef = TypedDict(
    "ListCompilationJobsRequestListCompilationJobsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": CompilationJobStatusType,
        "SortBy": ListCompilationJobsSortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListContextsRequestListContextsPaginateTypeDef = TypedDict(
    "ListContextsRequestListContextsPaginateTypeDef",
    {
        "SourceUri": str,
        "ContextType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortContextsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListDataQualityJobDefinitionsRequestListDataQualityJobDefinitionsPaginateTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsRequestListDataQualityJobDefinitionsPaginateTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListDeviceFleetsRequestListDeviceFleetsPaginateTypeDef = TypedDict(
    "ListDeviceFleetsRequestListDeviceFleetsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": ListDeviceFleetsSortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListDevicesRequestListDevicesPaginateTypeDef = TypedDict(
    "ListDevicesRequestListDevicesPaginateTypeDef",
    {
        "LatestHeartbeatAfter": Union[datetime, str],
        "ModelName": str,
        "DeviceFleetName": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListDomainsRequestListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsRequestListDomainsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListEdgeDeploymentPlansRequestListEdgeDeploymentPlansPaginateTypeDef = TypedDict(
    "ListEdgeDeploymentPlansRequestListEdgeDeploymentPlansPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "DeviceFleetNameContains": str,
        "SortBy": ListEdgeDeploymentPlansSortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListEdgePackagingJobsRequestListEdgePackagingJobsPaginateTypeDef = TypedDict(
    "ListEdgePackagingJobsRequestListEdgePackagingJobsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "ModelNameContains": str,
        "StatusEquals": EdgePackagingJobStatusType,
        "SortBy": ListEdgePackagingJobsSortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListEndpointConfigsInputListEndpointConfigsPaginateTypeDef = TypedDict(
    "ListEndpointConfigsInputListEndpointConfigsPaginateTypeDef",
    {
        "SortBy": EndpointConfigSortKeyType,
        "SortOrder": OrderKeyType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListEndpointsInputListEndpointsPaginateTypeDef = TypedDict(
    "ListEndpointsInputListEndpointsPaginateTypeDef",
    {
        "SortBy": EndpointSortKeyType,
        "SortOrder": OrderKeyType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": EndpointStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListExperimentsRequestListExperimentsPaginateTypeDef = TypedDict(
    "ListExperimentsRequestListExperimentsPaginateTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortExperimentsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListFeatureGroupsRequestListFeatureGroupsPaginateTypeDef = TypedDict(
    "ListFeatureGroupsRequestListFeatureGroupsPaginateTypeDef",
    {
        "NameContains": str,
        "FeatureGroupStatusEquals": FeatureGroupStatusType,
        "OfflineStoreStatusEquals": OfflineStoreStatusValueType,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": FeatureGroupSortOrderType,
        "SortBy": FeatureGroupSortByType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListFlowDefinitionsRequestListFlowDefinitionsPaginateTypeDef = TypedDict(
    "ListFlowDefinitionsRequestListFlowDefinitionsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListHumanTaskUisRequestListHumanTaskUisPaginateTypeDef = TypedDict(
    "ListHumanTaskUisRequestListHumanTaskUisPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListHyperParameterTuningJobsRequestListHyperParameterTuningJobsPaginateTypeDef = TypedDict(
    "ListHyperParameterTuningJobsRequestListHyperParameterTuningJobsPaginateTypeDef",
    {
        "SortBy": HyperParameterTuningJobSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "StatusEquals": HyperParameterTuningJobStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListImageVersionsRequestListImageVersionsPaginateTypeDef = TypedDict(
    "_RequiredListImageVersionsRequestListImageVersionsPaginateTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalListImageVersionsRequestListImageVersionsPaginateTypeDef = TypedDict(
    "_OptionalListImageVersionsRequestListImageVersionsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "SortBy": ImageVersionSortByType,
        "SortOrder": ImageVersionSortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListImageVersionsRequestListImageVersionsPaginateTypeDef(
    _RequiredListImageVersionsRequestListImageVersionsPaginateTypeDef,
    _OptionalListImageVersionsRequestListImageVersionsPaginateTypeDef,
):
    pass


ListImagesRequestListImagesPaginateTypeDef = TypedDict(
    "ListImagesRequestListImagesPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": ImageSortByType,
        "SortOrder": ImageSortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListInferenceExperimentsRequestListInferenceExperimentsPaginateTypeDef = TypedDict(
    "ListInferenceExperimentsRequestListInferenceExperimentsPaginateTypeDef",
    {
        "NameContains": str,
        "Type": Literal["ShadowMode"],
        "StatusEquals": InferenceExperimentStatusType,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "SortBy": SortInferenceExperimentsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef = TypedDict(
    "_RequiredListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef",
    {
        "JobName": str,
    },
)
_OptionalListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef = TypedDict(
    "_OptionalListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef",
    {
        "Status": RecommendationJobStatusType,
        "StepType": Literal["BENCHMARK"],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef(
    _RequiredListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef,
    _OptionalListInferenceRecommendationsJobStepsRequestListInferenceRecommendationsJobStepsPaginateTypeDef,
):
    pass


ListInferenceRecommendationsJobsRequestListInferenceRecommendationsJobsPaginateTypeDef = TypedDict(
    "ListInferenceRecommendationsJobsRequestListInferenceRecommendationsJobsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": RecommendationJobStatusType,
        "SortBy": ListInferenceRecommendationsJobsSortByType,
        "SortOrder": SortOrderType,
        "ModelNameEquals": str,
        "ModelPackageVersionArnEquals": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef = TypedDict(
    "_RequiredListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef",
    {
        "WorkteamArn": str,
    },
)
_OptionalListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef = TypedDict(
    "_OptionalListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "JobReferenceCodeContains": str,
        "SortBy": Literal["CreationTime"],
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef(
    _RequiredListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef,
    _OptionalListLabelingJobsForWorkteamRequestListLabelingJobsForWorkteamPaginateTypeDef,
):
    pass


ListLabelingJobsRequestListLabelingJobsPaginateTypeDef = TypedDict(
    "ListLabelingJobsRequestListLabelingJobsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "StatusEquals": LabelingJobStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListLineageGroupsRequestListLineageGroupsPaginateTypeDef = TypedDict(
    "ListLineageGroupsRequestListLineageGroupsPaginateTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortLineageGroupsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListModelBiasJobDefinitionsRequestListModelBiasJobDefinitionsPaginateTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsRequestListModelBiasJobDefinitionsPaginateTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef = TypedDict(
    "_RequiredListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef = TypedDict(
    "_OptionalListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef",
    {
        "ModelCardVersion": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "ModelCardExportJobNameContains": str,
        "StatusEquals": ModelCardExportJobStatusType,
        "SortBy": ModelCardExportJobSortByType,
        "SortOrder": ModelCardExportJobSortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef(
    _RequiredListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef,
    _OptionalListModelCardExportJobsRequestListModelCardExportJobsPaginateTypeDef,
):
    pass


_RequiredListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef = TypedDict(
    "_RequiredListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef = TypedDict(
    "_OptionalListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "ModelCardStatus": ModelCardStatusType,
        "SortBy": Literal["Version"],
        "SortOrder": ModelCardSortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef(
    _RequiredListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef,
    _OptionalListModelCardVersionsRequestListModelCardVersionsPaginateTypeDef,
):
    pass


ListModelCardsRequestListModelCardsPaginateTypeDef = TypedDict(
    "ListModelCardsRequestListModelCardsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "NameContains": str,
        "ModelCardStatus": ModelCardStatusType,
        "SortBy": ModelCardSortByType,
        "SortOrder": ModelCardSortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListModelExplainabilityJobDefinitionsRequestListModelExplainabilityJobDefinitionsPaginateTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsRequestListModelExplainabilityJobDefinitionsPaginateTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListModelPackageGroupsInputListModelPackageGroupsPaginateTypeDef = TypedDict(
    "ListModelPackageGroupsInputListModelPackageGroupsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": ModelPackageGroupSortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListModelPackagesInputListModelPackagesPaginateTypeDef = TypedDict(
    "ListModelPackagesInputListModelPackagesPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "NameContains": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "ModelPackageGroupName": str,
        "ModelPackageType": ModelPackageTypeType,
        "SortBy": ModelPackageSortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListModelQualityJobDefinitionsRequestListModelQualityJobDefinitionsPaginateTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsRequestListModelQualityJobDefinitionsPaginateTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListModelsInputListModelsPaginateTypeDef = TypedDict(
    "ListModelsInputListModelsPaginateTypeDef",
    {
        "SortBy": ModelSortKeyType,
        "SortOrder": OrderKeyType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListMonitoringAlertHistoryRequestListMonitoringAlertHistoryPaginateTypeDef = TypedDict(
    "ListMonitoringAlertHistoryRequestListMonitoringAlertHistoryPaginateTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringAlertName": str,
        "SortBy": MonitoringAlertHistorySortKeyType,
        "SortOrder": SortOrderType,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "StatusEquals": MonitoringAlertStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef = TypedDict(
    "_RequiredListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)
_OptionalListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef = TypedDict(
    "_OptionalListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef(
    _RequiredListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef,
    _OptionalListMonitoringAlertsRequestListMonitoringAlertsPaginateTypeDef,
):
    pass


ListMonitoringExecutionsRequestListMonitoringExecutionsPaginateTypeDef = TypedDict(
    "ListMonitoringExecutionsRequestListMonitoringExecutionsPaginateTypeDef",
    {
        "MonitoringScheduleName": str,
        "EndpointName": str,
        "SortBy": MonitoringExecutionSortKeyType,
        "SortOrder": SortOrderType,
        "ScheduledTimeBefore": Union[datetime, str],
        "ScheduledTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": ExecutionStatusType,
        "MonitoringJobDefinitionName": str,
        "MonitoringTypeEquals": MonitoringTypeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListMonitoringSchedulesRequestListMonitoringSchedulesPaginateTypeDef = TypedDict(
    "ListMonitoringSchedulesRequestListMonitoringSchedulesPaginateTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringScheduleSortKeyType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": ScheduleStatusType,
        "MonitoringJobDefinitionName": str,
        "MonitoringTypeEquals": MonitoringTypeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListNotebookInstanceLifecycleConfigsInputListNotebookInstanceLifecycleConfigsPaginateTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsInputListNotebookInstanceLifecycleConfigsPaginateTypeDef",
    {
        "SortBy": NotebookInstanceLifecycleConfigSortKeyType,
        "SortOrder": NotebookInstanceLifecycleConfigSortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListNotebookInstancesInputListNotebookInstancesPaginateTypeDef = TypedDict(
    "ListNotebookInstancesInputListNotebookInstancesPaginateTypeDef",
    {
        "SortBy": NotebookInstanceSortKeyType,
        "SortOrder": NotebookInstanceSortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": NotebookInstanceStatusType,
        "NotebookInstanceLifecycleConfigNameContains": str,
        "DefaultCodeRepositoryContains": str,
        "AdditionalCodeRepositoryEquals": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPipelineExecutionStepsRequestListPipelineExecutionStepsPaginateTypeDef = TypedDict(
    "ListPipelineExecutionStepsRequestListPipelineExecutionStepsPaginateTypeDef",
    {
        "PipelineExecutionArn": str,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef = TypedDict(
    "_RequiredListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef",
    {
        "PipelineName": str,
    },
)
_OptionalListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef = TypedDict(
    "_OptionalListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortPipelineExecutionsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef(
    _RequiredListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef,
    _OptionalListPipelineExecutionsRequestListPipelineExecutionsPaginateTypeDef,
):
    pass


_RequiredListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef = TypedDict(
    "_RequiredListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)
_OptionalListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef = TypedDict(
    "_OptionalListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef(
    _RequiredListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef,
    _OptionalListPipelineParametersForExecutionRequestListPipelineParametersForExecutionPaginateTypeDef,
):
    pass


ListPipelinesRequestListPipelinesPaginateTypeDef = TypedDict(
    "ListPipelinesRequestListPipelinesPaginateTypeDef",
    {
        "PipelineNamePrefix": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortPipelinesByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListProcessingJobsRequestListProcessingJobsPaginateTypeDef = TypedDict(
    "ListProcessingJobsRequestListProcessingJobsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": ProcessingJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListResourceCatalogsRequestListResourceCatalogsPaginateTypeDef = TypedDict(
    "ListResourceCatalogsRequestListResourceCatalogsPaginateTypeDef",
    {
        "NameContains": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": ResourceCatalogSortOrderType,
        "SortBy": Literal["CreationTime"],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListSpacesRequestListSpacesPaginateTypeDef = TypedDict(
    "ListSpacesRequestListSpacesPaginateTypeDef",
    {
        "SortOrder": SortOrderType,
        "SortBy": SpaceSortKeyType,
        "DomainIdEquals": str,
        "SpaceNameContains": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListStageDevicesRequestListStageDevicesPaginateTypeDef = TypedDict(
    "_RequiredListStageDevicesRequestListStageDevicesPaginateTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)
_OptionalListStageDevicesRequestListStageDevicesPaginateTypeDef = TypedDict(
    "_OptionalListStageDevicesRequestListStageDevicesPaginateTypeDef",
    {
        "ExcludeDevicesDeployedInOtherStage": bool,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListStageDevicesRequestListStageDevicesPaginateTypeDef(
    _RequiredListStageDevicesRequestListStageDevicesPaginateTypeDef,
    _OptionalListStageDevicesRequestListStageDevicesPaginateTypeDef,
):
    pass


ListStudioLifecycleConfigsRequestListStudioLifecycleConfigsPaginateTypeDef = TypedDict(
    "ListStudioLifecycleConfigsRequestListStudioLifecycleConfigsPaginateTypeDef",
    {
        "NameContains": str,
        "AppTypeEquals": StudioLifecycleConfigAppTypeType,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "ModifiedTimeBefore": Union[datetime, str],
        "ModifiedTimeAfter": Union[datetime, str],
        "SortBy": StudioLifecycleConfigSortKeyType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListSubscribedWorkteamsRequestListSubscribedWorkteamsPaginateTypeDef = TypedDict(
    "ListSubscribedWorkteamsRequestListSubscribedWorkteamsPaginateTypeDef",
    {
        "NameContains": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListTagsInputListTagsPaginateTypeDef = TypedDict(
    "_RequiredListTagsInputListTagsPaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsInputListTagsPaginateTypeDef = TypedDict(
    "_OptionalListTagsInputListTagsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTagsInputListTagsPaginateTypeDef(
    _RequiredListTagsInputListTagsPaginateTypeDef, _OptionalListTagsInputListTagsPaginateTypeDef
):
    pass


_RequiredListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef = TypedDict(
    "_RequiredListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)
_OptionalListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef = TypedDict(
    "_OptionalListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef",
    {
        "StatusEquals": TrainingJobStatusType,
        "SortBy": TrainingJobSortByOptionsType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef(
    _RequiredListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef,
    _OptionalListTrainingJobsForHyperParameterTuningJobRequestListTrainingJobsForHyperParameterTuningJobPaginateTypeDef,
):
    pass


ListTrainingJobsRequestListTrainingJobsPaginateTypeDef = TypedDict(
    "ListTrainingJobsRequestListTrainingJobsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": TrainingJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "WarmPoolStatusEquals": WarmPoolResourceStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListTransformJobsRequestListTransformJobsPaginateTypeDef = TypedDict(
    "ListTransformJobsRequestListTransformJobsPaginateTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": TransformJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListTrialComponentsRequestListTrialComponentsPaginateTypeDef = TypedDict(
    "ListTrialComponentsRequestListTrialComponentsPaginateTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
        "SourceArn": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortTrialComponentsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListTrialsRequestListTrialsPaginateTypeDef = TypedDict(
    "ListTrialsRequestListTrialsPaginateTypeDef",
    {
        "ExperimentName": str,
        "TrialComponentName": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortTrialsByType,
        "SortOrder": SortOrderType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListUserProfilesRequestListUserProfilesPaginateTypeDef = TypedDict(
    "ListUserProfilesRequestListUserProfilesPaginateTypeDef",
    {
        "SortOrder": SortOrderType,
        "SortBy": UserProfileSortKeyType,
        "DomainIdEquals": str,
        "UserProfileNameContains": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListWorkforcesRequestListWorkforcesPaginateTypeDef = TypedDict(
    "ListWorkforcesRequestListWorkforcesPaginateTypeDef",
    {
        "SortBy": ListWorkforcesSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListWorkteamsRequestListWorkteamsPaginateTypeDef = TypedDict(
    "ListWorkteamsRequestListWorkteamsPaginateTypeDef",
    {
        "SortBy": ListWorkteamsSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredSearchRequestSearchPaginateTypeDef = TypedDict(
    "_RequiredSearchRequestSearchPaginateTypeDef",
    {
        "Resource": ResourceTypeType,
    },
)
_OptionalSearchRequestSearchPaginateTypeDef = TypedDict(
    "_OptionalSearchRequestSearchPaginateTypeDef",
    {
        "SearchExpression": "SearchExpressionTypeDef",
        "SortBy": str,
        "SortOrder": SearchSortOrderType,
        "CrossAccountFilterOption": CrossAccountFilterOptionType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SearchRequestSearchPaginateTypeDef(
    _RequiredSearchRequestSearchPaginateTypeDef, _OptionalSearchRequestSearchPaginateTypeDef
):
    pass


ListDataQualityJobDefinitionsResponseTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List[MonitoringJobDefinitionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelBiasJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List[MonitoringJobDefinitionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelExplainabilityJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List[MonitoringJobDefinitionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelQualityJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List[MonitoringJobDefinitionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelCardExportJobsResponseTypeDef = TypedDict(
    "ListModelCardExportJobsResponseTypeDef",
    {
        "ModelCardExportJobSummaries": List[ModelCardExportJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelCardVersionsResponseTypeDef = TypedDict(
    "ListModelCardVersionsResponseTypeDef",
    {
        "ModelCardVersionSummaryList": List[ModelCardVersionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelCardsResponseTypeDef = TypedDict(
    "ListModelCardsResponseTypeDef",
    {
        "ModelCardSummaries": List[ModelCardSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelMetadataResponseTypeDef = TypedDict(
    "ListModelMetadataResponseTypeDef",
    {
        "ModelMetadataSummaries": List[ModelMetadataSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelPackageGroupsOutputTypeDef = TypedDict(
    "ListModelPackageGroupsOutputTypeDef",
    {
        "ModelPackageGroupSummaryList": List[ModelPackageGroupSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelPackagesOutputTypeDef = TypedDict(
    "ListModelPackagesOutputTypeDef",
    {
        "ModelPackageSummaryList": List[ModelPackageSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListModelsOutputTypeDef = TypedDict(
    "ListModelsOutputTypeDef",
    {
        "Models": List[ModelSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMonitoringAlertHistoryResponseTypeDef = TypedDict(
    "ListMonitoringAlertHistoryResponseTypeDef",
    {
        "MonitoringAlertHistory": List[MonitoringAlertHistorySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMonitoringSchedulesResponseTypeDef = TypedDict(
    "ListMonitoringSchedulesResponseTypeDef",
    {
        "MonitoringScheduleSummaries": List[MonitoringScheduleSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListNotebookInstanceLifecycleConfigsOutputTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstanceLifecycleConfigs": List[NotebookInstanceLifecycleConfigSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListNotebookInstancesOutputTypeDef = TypedDict(
    "ListNotebookInstancesOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstances": List[NotebookInstanceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPipelineExecutionsResponseTypeDef = TypedDict(
    "ListPipelineExecutionsResponseTypeDef",
    {
        "PipelineExecutionSummaries": List[PipelineExecutionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPipelineParametersForExecutionResponseTypeDef = TypedDict(
    "ListPipelineParametersForExecutionResponseTypeDef",
    {
        "PipelineParameters": List[ParameterOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "PipelineSummaries": List[PipelineSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListProcessingJobsResponseTypeDef = TypedDict(
    "ListProcessingJobsResponseTypeDef",
    {
        "ProcessingJobSummaries": List[ProcessingJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "ProjectSummaryList": List[ProjectSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListResourceCatalogsResponseTypeDef = TypedDict(
    "ListResourceCatalogsResponseTypeDef",
    {
        "ResourceCatalogs": List[ResourceCatalogTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSpacesResponseTypeDef = TypedDict(
    "ListSpacesResponseTypeDef",
    {
        "Spaces": List[SpaceDetailsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStudioLifecycleConfigsResponseTypeDef = TypedDict(
    "ListStudioLifecycleConfigsResponseTypeDef",
    {
        "NextToken": str,
        "StudioLifecycleConfigs": List[StudioLifecycleConfigDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTransformJobsResponseTypeDef = TypedDict(
    "ListTransformJobsResponseTypeDef",
    {
        "TransformJobSummaries": List[TransformJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListUserProfilesResponseTypeDef = TypedDict(
    "ListUserProfilesResponseTypeDef",
    {
        "UserProfiles": List[UserProfileDetailsTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MemberDefinitionOutputTypeDef = TypedDict(
    "MemberDefinitionOutputTypeDef",
    {
        "CognitoMemberDefinition": CognitoMemberDefinitionOutputTypeDef,
        "OidcMemberDefinition": OidcMemberDefinitionOutputTypeDef,
    },
    total=False,
)

MemberDefinitionTypeDef = TypedDict(
    "MemberDefinitionTypeDef",
    {
        "CognitoMemberDefinition": CognitoMemberDefinitionTypeDef,
        "OidcMemberDefinition": OidcMemberDefinitionTypeDef,
    },
    total=False,
)

MonitoringAlertActionsTypeDef = TypedDict(
    "MonitoringAlertActionsTypeDef",
    {
        "ModelDashboardIndicator": ModelDashboardIndicatorActionTypeDef,
    },
    total=False,
)

ModelDataSourceOutputTypeDef = TypedDict(
    "ModelDataSourceOutputTypeDef",
    {
        "S3DataSource": S3ModelDataSourceOutputTypeDef,
    },
)

ModelDataSourceTypeDef = TypedDict(
    "ModelDataSourceTypeDef",
    {
        "S3DataSource": S3ModelDataSourceTypeDef,
    },
)

ModelInfrastructureConfigOutputTypeDef = TypedDict(
    "ModelInfrastructureConfigOutputTypeDef",
    {
        "InfrastructureType": Literal["RealTimeInference"],
        "RealTimeInferenceConfig": RealTimeInferenceConfigOutputTypeDef,
    },
)

ModelInfrastructureConfigTypeDef = TypedDict(
    "ModelInfrastructureConfigTypeDef",
    {
        "InfrastructureType": Literal["RealTimeInference"],
        "RealTimeInferenceConfig": RealTimeInferenceConfigTypeDef,
    },
)

_RequiredModelPackageContainerDefinitionOutputTypeDef = TypedDict(
    "_RequiredModelPackageContainerDefinitionOutputTypeDef",
    {
        "Image": str,
    },
)
_OptionalModelPackageContainerDefinitionOutputTypeDef = TypedDict(
    "_OptionalModelPackageContainerDefinitionOutputTypeDef",
    {
        "ContainerHostname": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
        "Environment": Dict[str, str],
        "ModelInput": ModelInputOutputTypeDef,
        "Framework": str,
        "FrameworkVersion": str,
        "NearestModelName": str,
    },
    total=False,
)


class ModelPackageContainerDefinitionOutputTypeDef(
    _RequiredModelPackageContainerDefinitionOutputTypeDef,
    _OptionalModelPackageContainerDefinitionOutputTypeDef,
):
    pass


_RequiredModelPackageContainerDefinitionTypeDef = TypedDict(
    "_RequiredModelPackageContainerDefinitionTypeDef",
    {
        "Image": str,
    },
)
_OptionalModelPackageContainerDefinitionTypeDef = TypedDict(
    "_OptionalModelPackageContainerDefinitionTypeDef",
    {
        "ContainerHostname": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
        "Environment": Mapping[str, str],
        "ModelInput": ModelInputTypeDef,
        "Framework": str,
        "FrameworkVersion": str,
        "NearestModelName": str,
    },
    total=False,
)


class ModelPackageContainerDefinitionTypeDef(
    _RequiredModelPackageContainerDefinitionTypeDef, _OptionalModelPackageContainerDefinitionTypeDef
):
    pass


RecommendationJobStoppingConditionsOutputTypeDef = TypedDict(
    "RecommendationJobStoppingConditionsOutputTypeDef",
    {
        "MaxInvocations": int,
        "ModelLatencyThresholds": List[ModelLatencyThresholdOutputTypeDef],
    },
    total=False,
)

RecommendationJobStoppingConditionsTypeDef = TypedDict(
    "RecommendationJobStoppingConditionsTypeDef",
    {
        "MaxInvocations": int,
        "ModelLatencyThresholds": Sequence[ModelLatencyThresholdTypeDef],
    },
    total=False,
)

ModelMetadataSearchExpressionTypeDef = TypedDict(
    "ModelMetadataSearchExpressionTypeDef",
    {
        "Filters": Sequence[ModelMetadataFilterTypeDef],
    },
    total=False,
)

_RequiredModelPackageStatusDetailsTypeDef = TypedDict(
    "_RequiredModelPackageStatusDetailsTypeDef",
    {
        "ValidationStatuses": List[ModelPackageStatusItemTypeDef],
    },
)
_OptionalModelPackageStatusDetailsTypeDef = TypedDict(
    "_OptionalModelPackageStatusDetailsTypeDef",
    {
        "ImageScanStatuses": List[ModelPackageStatusItemTypeDef],
    },
    total=False,
)


class ModelPackageStatusDetailsTypeDef(
    _RequiredModelPackageStatusDetailsTypeDef, _OptionalModelPackageStatusDetailsTypeDef
):
    pass


MonitoringResourcesOutputTypeDef = TypedDict(
    "MonitoringResourcesOutputTypeDef",
    {
        "ClusterConfig": MonitoringClusterConfigOutputTypeDef,
    },
)

MonitoringResourcesTypeDef = TypedDict(
    "MonitoringResourcesTypeDef",
    {
        "ClusterConfig": MonitoringClusterConfigTypeDef,
    },
)

MonitoringDatasetFormatOutputTypeDef = TypedDict(
    "MonitoringDatasetFormatOutputTypeDef",
    {
        "Csv": MonitoringCsvDatasetFormatOutputTypeDef,
        "Json": MonitoringJsonDatasetFormatOutputTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)

MonitoringDatasetFormatTypeDef = TypedDict(
    "MonitoringDatasetFormatTypeDef",
    {
        "Csv": MonitoringCsvDatasetFormatTypeDef,
        "Json": MonitoringJsonDatasetFormatTypeDef,
        "Parquet": Mapping[str, Any],
    },
    total=False,
)

MonitoringOutputTypeDef = TypedDict(
    "MonitoringOutputTypeDef",
    {
        "S3Output": MonitoringS3OutputTypeDef,
    },
)

_RequiredOfflineStoreConfigOutputTypeDef = TypedDict(
    "_RequiredOfflineStoreConfigOutputTypeDef",
    {
        "S3StorageConfig": S3StorageConfigOutputTypeDef,
    },
)
_OptionalOfflineStoreConfigOutputTypeDef = TypedDict(
    "_OptionalOfflineStoreConfigOutputTypeDef",
    {
        "DisableGlueTableCreation": bool,
        "DataCatalogConfig": DataCatalogConfigOutputTypeDef,
        "TableFormat": TableFormatType,
    },
    total=False,
)


class OfflineStoreConfigOutputTypeDef(
    _RequiredOfflineStoreConfigOutputTypeDef, _OptionalOfflineStoreConfigOutputTypeDef
):
    pass


_RequiredOfflineStoreConfigTypeDef = TypedDict(
    "_RequiredOfflineStoreConfigTypeDef",
    {
        "S3StorageConfig": S3StorageConfigTypeDef,
    },
)
_OptionalOfflineStoreConfigTypeDef = TypedDict(
    "_OptionalOfflineStoreConfigTypeDef",
    {
        "DisableGlueTableCreation": bool,
        "DataCatalogConfig": DataCatalogConfigTypeDef,
        "TableFormat": TableFormatType,
    },
    total=False,
)


class OfflineStoreConfigTypeDef(
    _RequiredOfflineStoreConfigTypeDef, _OptionalOfflineStoreConfigTypeDef
):
    pass


OnlineStoreConfigOutputTypeDef = TypedDict(
    "OnlineStoreConfigOutputTypeDef",
    {
        "SecurityConfig": OnlineStoreSecurityConfigOutputTypeDef,
        "EnableOnlineStore": bool,
        "TtlDuration": TtlDurationOutputTypeDef,
    },
    total=False,
)

OnlineStoreConfigTypeDef = TypedDict(
    "OnlineStoreConfigTypeDef",
    {
        "SecurityConfig": OnlineStoreSecurityConfigTypeDef,
        "EnableOnlineStore": bool,
        "TtlDuration": TtlDurationTypeDef,
    },
    total=False,
)

OnlineStoreConfigUpdateTypeDef = TypedDict(
    "OnlineStoreConfigUpdateTypeDef",
    {
        "TtlDuration": TtlDurationTypeDef,
    },
    total=False,
)

_RequiredOutputConfigOutputTypeDef = TypedDict(
    "_RequiredOutputConfigOutputTypeDef",
    {
        "S3OutputLocation": str,
    },
)
_OptionalOutputConfigOutputTypeDef = TypedDict(
    "_OptionalOutputConfigOutputTypeDef",
    {
        "TargetDevice": TargetDeviceType,
        "TargetPlatform": TargetPlatformOutputTypeDef,
        "CompilerOptions": str,
        "KmsKeyId": str,
    },
    total=False,
)


class OutputConfigOutputTypeDef(
    _RequiredOutputConfigOutputTypeDef, _OptionalOutputConfigOutputTypeDef
):
    pass


_RequiredOutputConfigTypeDef = TypedDict(
    "_RequiredOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
    },
)
_OptionalOutputConfigTypeDef = TypedDict(
    "_OptionalOutputConfigTypeDef",
    {
        "TargetDevice": TargetDeviceType,
        "TargetPlatform": TargetPlatformTypeDef,
        "CompilerOptions": str,
        "KmsKeyId": str,
    },
    total=False,
)


class OutputConfigTypeDef(_RequiredOutputConfigTypeDef, _OptionalOutputConfigTypeDef):
    pass


_RequiredSendPipelineExecutionStepSuccessRequestRequestTypeDef = TypedDict(
    "_RequiredSendPipelineExecutionStepSuccessRequestRequestTypeDef",
    {
        "CallbackToken": str,
    },
)
_OptionalSendPipelineExecutionStepSuccessRequestRequestTypeDef = TypedDict(
    "_OptionalSendPipelineExecutionStepSuccessRequestRequestTypeDef",
    {
        "OutputParameters": Sequence[OutputParameterTypeDef],
        "ClientRequestToken": str,
    },
    total=False,
)


class SendPipelineExecutionStepSuccessRequestRequestTypeDef(
    _RequiredSendPipelineExecutionStepSuccessRequestRequestTypeDef,
    _OptionalSendPipelineExecutionStepSuccessRequestRequestTypeDef,
):
    pass


_RequiredPendingProductionVariantSummaryTypeDef = TypedDict(
    "_RequiredPendingProductionVariantSummaryTypeDef",
    {
        "VariantName": str,
    },
)
_OptionalPendingProductionVariantSummaryTypeDef = TypedDict(
    "_OptionalPendingProductionVariantSummaryTypeDef",
    {
        "DeployedImages": List[DeployedImageTypeDef],
        "CurrentWeight": float,
        "DesiredWeight": float,
        "CurrentInstanceCount": int,
        "DesiredInstanceCount": int,
        "InstanceType": ProductionVariantInstanceTypeType,
        "AcceleratorType": ProductionVariantAcceleratorTypeType,
        "VariantStatus": List[ProductionVariantStatusTypeDef],
        "CurrentServerlessConfig": ProductionVariantServerlessConfigOutputTypeDef,
        "DesiredServerlessConfig": ProductionVariantServerlessConfigOutputTypeDef,
    },
    total=False,
)


class PendingProductionVariantSummaryTypeDef(
    _RequiredPendingProductionVariantSummaryTypeDef, _OptionalPendingProductionVariantSummaryTypeDef
):
    pass


_RequiredProductionVariantSummaryTypeDef = TypedDict(
    "_RequiredProductionVariantSummaryTypeDef",
    {
        "VariantName": str,
    },
)
_OptionalProductionVariantSummaryTypeDef = TypedDict(
    "_OptionalProductionVariantSummaryTypeDef",
    {
        "DeployedImages": List[DeployedImageTypeDef],
        "CurrentWeight": float,
        "DesiredWeight": float,
        "CurrentInstanceCount": int,
        "DesiredInstanceCount": int,
        "VariantStatus": List[ProductionVariantStatusTypeDef],
        "CurrentServerlessConfig": ProductionVariantServerlessConfigOutputTypeDef,
        "DesiredServerlessConfig": ProductionVariantServerlessConfigOutputTypeDef,
    },
    total=False,
)


class ProductionVariantSummaryTypeDef(
    _RequiredProductionVariantSummaryTypeDef, _OptionalProductionVariantSummaryTypeDef
):
    pass


TrafficPatternOutputTypeDef = TypedDict(
    "TrafficPatternOutputTypeDef",
    {
        "TrafficType": Literal["PHASES"],
        "Phases": List[PhaseOutputTypeDef],
    },
    total=False,
)

TrafficPatternTypeDef = TypedDict(
    "TrafficPatternTypeDef",
    {
        "TrafficType": Literal["PHASES"],
        "Phases": Sequence[PhaseTypeDef],
    },
    total=False,
)

ProcessingResourcesOutputTypeDef = TypedDict(
    "ProcessingResourcesOutputTypeDef",
    {
        "ClusterConfig": ProcessingClusterConfigOutputTypeDef,
    },
)

ProcessingResourcesTypeDef = TypedDict(
    "ProcessingResourcesTypeDef",
    {
        "ClusterConfig": ProcessingClusterConfigTypeDef,
    },
)

_RequiredProcessingOutputTypeDef = TypedDict(
    "_RequiredProcessingOutputTypeDef",
    {
        "OutputName": str,
    },
)
_OptionalProcessingOutputTypeDef = TypedDict(
    "_OptionalProcessingOutputTypeDef",
    {
        "S3Output": ProcessingS3OutputTypeDef,
        "FeatureStoreOutput": ProcessingFeatureStoreOutputTypeDef,
        "AppManaged": bool,
    },
    total=False,
)


class ProcessingOutputTypeDef(_RequiredProcessingOutputTypeDef, _OptionalProcessingOutputTypeDef):
    pass


_RequiredProductionVariantOutputTypeDef = TypedDict(
    "_RequiredProductionVariantOutputTypeDef",
    {
        "VariantName": str,
        "ModelName": str,
    },
)
_OptionalProductionVariantOutputTypeDef = TypedDict(
    "_OptionalProductionVariantOutputTypeDef",
    {
        "InitialInstanceCount": int,
        "InstanceType": ProductionVariantInstanceTypeType,
        "InitialVariantWeight": float,
        "AcceleratorType": ProductionVariantAcceleratorTypeType,
        "CoreDumpConfig": ProductionVariantCoreDumpConfigOutputTypeDef,
        "ServerlessConfig": ProductionVariantServerlessConfigOutputTypeDef,
        "VolumeSizeInGB": int,
        "ModelDataDownloadTimeoutInSeconds": int,
        "ContainerStartupHealthCheckTimeoutInSeconds": int,
        "EnableSSMAccess": bool,
    },
    total=False,
)


class ProductionVariantOutputTypeDef(
    _RequiredProductionVariantOutputTypeDef, _OptionalProductionVariantOutputTypeDef
):
    pass


_RequiredProductionVariantTypeDef = TypedDict(
    "_RequiredProductionVariantTypeDef",
    {
        "VariantName": str,
        "ModelName": str,
    },
)
_OptionalProductionVariantTypeDef = TypedDict(
    "_OptionalProductionVariantTypeDef",
    {
        "InitialInstanceCount": int,
        "InstanceType": ProductionVariantInstanceTypeType,
        "InitialVariantWeight": float,
        "AcceleratorType": ProductionVariantAcceleratorTypeType,
        "CoreDumpConfig": ProductionVariantCoreDumpConfigTypeDef,
        "ServerlessConfig": ProductionVariantServerlessConfigTypeDef,
        "VolumeSizeInGB": int,
        "ModelDataDownloadTimeoutInSeconds": int,
        "ContainerStartupHealthCheckTimeoutInSeconds": int,
        "EnableSSMAccess": bool,
    },
    total=False,
)


class ProductionVariantTypeDef(
    _RequiredProductionVariantTypeDef, _OptionalProductionVariantTypeDef
):
    pass


SuggestionQueryTypeDef = TypedDict(
    "SuggestionQueryTypeDef",
    {
        "PropertyNameQuery": PropertyNameQueryTypeDef,
    },
    total=False,
)

_RequiredServiceCatalogProvisioningDetailsOutputTypeDef = TypedDict(
    "_RequiredServiceCatalogProvisioningDetailsOutputTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalServiceCatalogProvisioningDetailsOutputTypeDef = TypedDict(
    "_OptionalServiceCatalogProvisioningDetailsOutputTypeDef",
    {
        "ProvisioningArtifactId": str,
        "PathId": str,
        "ProvisioningParameters": List[ProvisioningParameterOutputTypeDef],
    },
    total=False,
)


class ServiceCatalogProvisioningDetailsOutputTypeDef(
    _RequiredServiceCatalogProvisioningDetailsOutputTypeDef,
    _OptionalServiceCatalogProvisioningDetailsOutputTypeDef,
):
    pass


_RequiredServiceCatalogProvisioningDetailsTypeDef = TypedDict(
    "_RequiredServiceCatalogProvisioningDetailsTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalServiceCatalogProvisioningDetailsTypeDef = TypedDict(
    "_OptionalServiceCatalogProvisioningDetailsTypeDef",
    {
        "ProvisioningArtifactId": str,
        "PathId": str,
        "ProvisioningParameters": Sequence[ProvisioningParameterTypeDef],
    },
    total=False,
)


class ServiceCatalogProvisioningDetailsTypeDef(
    _RequiredServiceCatalogProvisioningDetailsTypeDef,
    _OptionalServiceCatalogProvisioningDetailsTypeDef,
):
    pass


ServiceCatalogProvisioningUpdateDetailsTypeDef = TypedDict(
    "ServiceCatalogProvisioningUpdateDetailsTypeDef",
    {
        "ProvisioningArtifactId": str,
        "ProvisioningParameters": Sequence[ProvisioningParameterTypeDef],
    },
    total=False,
)

PublicWorkforceTaskPriceOutputTypeDef = TypedDict(
    "PublicWorkforceTaskPriceOutputTypeDef",
    {
        "AmountInUsd": USDOutputTypeDef,
    },
    total=False,
)

PublicWorkforceTaskPriceTypeDef = TypedDict(
    "PublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": USDTypeDef,
    },
    total=False,
)

QueryLineageRequestRequestTypeDef = TypedDict(
    "QueryLineageRequestRequestTypeDef",
    {
        "StartArns": Sequence[str],
        "Direction": DirectionType,
        "IncludeEdges": bool,
        "Filters": QueryFiltersTypeDef,
        "MaxDepth": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

QueryLineageResponseTypeDef = TypedDict(
    "QueryLineageResponseTypeDef",
    {
        "Vertices": List[VertexTypeDef],
        "Edges": List[EdgeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RecommendationJobOutputConfigTypeDef = TypedDict(
    "RecommendationJobOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "CompiledOutputConfig": RecommendationJobCompiledOutputConfigTypeDef,
    },
    total=False,
)

RecommendationJobContainerConfigOutputTypeDef = TypedDict(
    "RecommendationJobContainerConfigOutputTypeDef",
    {
        "Domain": str,
        "Task": str,
        "Framework": str,
        "FrameworkVersion": str,
        "PayloadConfig": RecommendationJobPayloadConfigOutputTypeDef,
        "NearestModelName": str,
        "SupportedInstanceTypes": List[str],
        "DataInputConfig": str,
        "SupportedEndpointType": RecommendationJobSupportedEndpointTypeType,
    },
    total=False,
)

RecommendationJobContainerConfigTypeDef = TypedDict(
    "RecommendationJobContainerConfigTypeDef",
    {
        "Domain": str,
        "Task": str,
        "Framework": str,
        "FrameworkVersion": str,
        "PayloadConfig": RecommendationJobPayloadConfigTypeDef,
        "NearestModelName": str,
        "SupportedInstanceTypes": Sequence[str],
        "DataInputConfig": str,
        "SupportedEndpointType": RecommendationJobSupportedEndpointTypeType,
    },
    total=False,
)

_RequiredRenderUiTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredRenderUiTemplateRequestRequestTypeDef",
    {
        "Task": RenderableTaskTypeDef,
        "RoleArn": str,
    },
)
_OptionalRenderUiTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalRenderUiTemplateRequestRequestTypeDef",
    {
        "UiTemplate": UiTemplateTypeDef,
        "HumanTaskUiArn": str,
    },
    total=False,
)


class RenderUiTemplateRequestRequestTypeDef(
    _RequiredRenderUiTemplateRequestRequestTypeDef, _OptionalRenderUiTemplateRequestRequestTypeDef
):
    pass


RenderUiTemplateResponseTypeDef = TypedDict(
    "RenderUiTemplateResponseTypeDef",
    {
        "RenderedContent": str,
        "Errors": List[RenderingErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateTrainingJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)
_OptionalUpdateTrainingJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrainingJobRequestRequestTypeDef",
    {
        "ProfilerConfig": ProfilerConfigForUpdateTypeDef,
        "ProfilerRuleConfigurations": Sequence[ProfilerRuleConfigurationTypeDef],
        "ResourceConfig": ResourceConfigForUpdateTypeDef,
    },
    total=False,
)


class UpdateTrainingJobRequestRequestTypeDef(
    _RequiredUpdateTrainingJobRequestRequestTypeDef, _OptionalUpdateTrainingJobRequestRequestTypeDef
):
    pass


SelectiveExecutionConfigOutputTypeDef = TypedDict(
    "SelectiveExecutionConfigOutputTypeDef",
    {
        "SourcePipelineExecutionArn": str,
        "SelectedSteps": List[SelectedStepOutputTypeDef],
    },
)

SelectiveExecutionConfigTypeDef = TypedDict(
    "SelectiveExecutionConfigTypeDef",
    {
        "SourcePipelineExecutionArn": str,
        "SelectedSteps": Sequence[SelectedStepTypeDef],
    },
)

ShadowModeConfigOutputTypeDef = TypedDict(
    "ShadowModeConfigOutputTypeDef",
    {
        "SourceModelVariantName": str,
        "ShadowModelVariants": List[ShadowModelVariantConfigOutputTypeDef],
    },
)

ShadowModeConfigTypeDef = TypedDict(
    "ShadowModeConfigTypeDef",
    {
        "SourceModelVariantName": str,
        "ShadowModelVariants": Sequence[ShadowModelVariantConfigTypeDef],
    },
)

SourceAlgorithmSpecificationOutputTypeDef = TypedDict(
    "SourceAlgorithmSpecificationOutputTypeDef",
    {
        "SourceAlgorithms": List[SourceAlgorithmOutputTypeDef],
    },
)

SourceAlgorithmSpecificationTypeDef = TypedDict(
    "SourceAlgorithmSpecificationTypeDef",
    {
        "SourceAlgorithms": Sequence[SourceAlgorithmTypeDef],
    },
)

_RequiredTimeSeriesForecastingJobConfigOutputTypeDef = TypedDict(
    "_RequiredTimeSeriesForecastingJobConfigOutputTypeDef",
    {
        "ForecastFrequency": str,
        "ForecastHorizon": int,
        "TimeSeriesConfig": TimeSeriesConfigOutputTypeDef,
    },
)
_OptionalTimeSeriesForecastingJobConfigOutputTypeDef = TypedDict(
    "_OptionalTimeSeriesForecastingJobConfigOutputTypeDef",
    {
        "FeatureSpecificationS3Uri": str,
        "CompletionCriteria": AutoMLJobCompletionCriteriaOutputTypeDef,
        "ForecastQuantiles": List[str],
        "Transformations": TimeSeriesTransformationsOutputTypeDef,
    },
    total=False,
)


class TimeSeriesForecastingJobConfigOutputTypeDef(
    _RequiredTimeSeriesForecastingJobConfigOutputTypeDef,
    _OptionalTimeSeriesForecastingJobConfigOutputTypeDef,
):
    pass


_RequiredTimeSeriesForecastingJobConfigTypeDef = TypedDict(
    "_RequiredTimeSeriesForecastingJobConfigTypeDef",
    {
        "ForecastFrequency": str,
        "ForecastHorizon": int,
        "TimeSeriesConfig": TimeSeriesConfigTypeDef,
    },
)
_OptionalTimeSeriesForecastingJobConfigTypeDef = TypedDict(
    "_OptionalTimeSeriesForecastingJobConfigTypeDef",
    {
        "FeatureSpecificationS3Uri": str,
        "CompletionCriteria": AutoMLJobCompletionCriteriaTypeDef,
        "ForecastQuantiles": Sequence[str],
        "Transformations": TimeSeriesTransformationsTypeDef,
    },
    total=False,
)


class TimeSeriesForecastingJobConfigTypeDef(
    _RequiredTimeSeriesForecastingJobConfigTypeDef, _OptionalTimeSeriesForecastingJobConfigTypeDef
):
    pass


_RequiredTrainingImageConfigOutputTypeDef = TypedDict(
    "_RequiredTrainingImageConfigOutputTypeDef",
    {
        "TrainingRepositoryAccessMode": TrainingRepositoryAccessModeType,
    },
)
_OptionalTrainingImageConfigOutputTypeDef = TypedDict(
    "_OptionalTrainingImageConfigOutputTypeDef",
    {
        "TrainingRepositoryAuthConfig": TrainingRepositoryAuthConfigOutputTypeDef,
    },
    total=False,
)


class TrainingImageConfigOutputTypeDef(
    _RequiredTrainingImageConfigOutputTypeDef, _OptionalTrainingImageConfigOutputTypeDef
):
    pass


_RequiredTrainingImageConfigTypeDef = TypedDict(
    "_RequiredTrainingImageConfigTypeDef",
    {
        "TrainingRepositoryAccessMode": TrainingRepositoryAccessModeType,
    },
)
_OptionalTrainingImageConfigTypeDef = TypedDict(
    "_OptionalTrainingImageConfigTypeDef",
    {
        "TrainingRepositoryAuthConfig": TrainingRepositoryAuthConfigTypeDef,
    },
    total=False,
)


class TrainingImageConfigTypeDef(
    _RequiredTrainingImageConfigTypeDef, _OptionalTrainingImageConfigTypeDef
):
    pass


TransformDataSourceOutputTypeDef = TypedDict(
    "TransformDataSourceOutputTypeDef",
    {
        "S3DataSource": TransformS3DataSourceOutputTypeDef,
    },
)

TransformDataSourceTypeDef = TypedDict(
    "TransformDataSourceTypeDef",
    {
        "S3DataSource": TransformS3DataSourceTypeDef,
    },
)

_RequiredWorkforceTypeDef = TypedDict(
    "_RequiredWorkforceTypeDef",
    {
        "WorkforceName": str,
        "WorkforceArn": str,
    },
)
_OptionalWorkforceTypeDef = TypedDict(
    "_OptionalWorkforceTypeDef",
    {
        "LastUpdatedDate": datetime,
        "SourceIpConfig": SourceIpConfigOutputTypeDef,
        "SubDomain": str,
        "CognitoConfig": CognitoConfigOutputTypeDef,
        "OidcConfig": OidcConfigForResponseTypeDef,
        "CreateDate": datetime,
        "WorkforceVpcConfig": WorkforceVpcConfigResponseTypeDef,
        "Status": WorkforceStatusType,
        "FailureReason": str,
    },
    total=False,
)


class WorkforceTypeDef(_RequiredWorkforceTypeDef, _OptionalWorkforceTypeDef):
    pass


ListActionsResponseTypeDef = TypedDict(
    "ListActionsResponseTypeDef",
    {
        "ActionSummaries": List[ActionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ArtifactSummaryTypeDef = TypedDict(
    "ArtifactSummaryTypeDef",
    {
        "ArtifactArn": str,
        "ArtifactName": str,
        "Source": ArtifactSourceOutputTypeDef,
        "ArtifactType": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredCreateArtifactRequestRequestTypeDef = TypedDict(
    "_RequiredCreateArtifactRequestRequestTypeDef",
    {
        "Source": ArtifactSourceTypeDef,
        "ArtifactType": str,
    },
)
_OptionalCreateArtifactRequestRequestTypeDef = TypedDict(
    "_OptionalCreateArtifactRequestRequestTypeDef",
    {
        "ArtifactName": str,
        "Properties": Mapping[str, str],
        "MetadataProperties": MetadataPropertiesTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateArtifactRequestRequestTypeDef(
    _RequiredCreateArtifactRequestRequestTypeDef, _OptionalCreateArtifactRequestRequestTypeDef
):
    pass


DeleteArtifactRequestRequestTypeDef = TypedDict(
    "DeleteArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": str,
        "Source": ArtifactSourceTypeDef,
    },
    total=False,
)

_RequiredAsyncInferenceConfigOutputTypeDef = TypedDict(
    "_RequiredAsyncInferenceConfigOutputTypeDef",
    {
        "OutputConfig": AsyncInferenceOutputConfigOutputTypeDef,
    },
)
_OptionalAsyncInferenceConfigOutputTypeDef = TypedDict(
    "_OptionalAsyncInferenceConfigOutputTypeDef",
    {
        "ClientConfig": AsyncInferenceClientConfigOutputTypeDef,
    },
    total=False,
)


class AsyncInferenceConfigOutputTypeDef(
    _RequiredAsyncInferenceConfigOutputTypeDef, _OptionalAsyncInferenceConfigOutputTypeDef
):
    pass


_RequiredAsyncInferenceConfigTypeDef = TypedDict(
    "_RequiredAsyncInferenceConfigTypeDef",
    {
        "OutputConfig": AsyncInferenceOutputConfigTypeDef,
    },
)
_OptionalAsyncInferenceConfigTypeDef = TypedDict(
    "_OptionalAsyncInferenceConfigTypeDef",
    {
        "ClientConfig": AsyncInferenceClientConfigTypeDef,
    },
    total=False,
)


class AsyncInferenceConfigTypeDef(
    _RequiredAsyncInferenceConfigTypeDef, _OptionalAsyncInferenceConfigTypeDef
):
    pass


_RequiredTabularJobConfigOutputTypeDef = TypedDict(
    "_RequiredTabularJobConfigOutputTypeDef",
    {
        "TargetAttributeName": str,
    },
)
_OptionalTabularJobConfigOutputTypeDef = TypedDict(
    "_OptionalTabularJobConfigOutputTypeDef",
    {
        "CandidateGenerationConfig": CandidateGenerationConfigOutputTypeDef,
        "CompletionCriteria": AutoMLJobCompletionCriteriaOutputTypeDef,
        "FeatureSpecificationS3Uri": str,
        "Mode": AutoMLModeType,
        "GenerateCandidateDefinitionsOnly": bool,
        "ProblemType": ProblemTypeType,
        "SampleWeightAttributeName": str,
    },
    total=False,
)


class TabularJobConfigOutputTypeDef(
    _RequiredTabularJobConfigOutputTypeDef, _OptionalTabularJobConfigOutputTypeDef
):
    pass


_RequiredTabularJobConfigTypeDef = TypedDict(
    "_RequiredTabularJobConfigTypeDef",
    {
        "TargetAttributeName": str,
    },
)
_OptionalTabularJobConfigTypeDef = TypedDict(
    "_OptionalTabularJobConfigTypeDef",
    {
        "CandidateGenerationConfig": CandidateGenerationConfigTypeDef,
        "CompletionCriteria": AutoMLJobCompletionCriteriaTypeDef,
        "FeatureSpecificationS3Uri": str,
        "Mode": AutoMLModeType,
        "GenerateCandidateDefinitionsOnly": bool,
        "ProblemType": ProblemTypeType,
        "SampleWeightAttributeName": str,
    },
    total=False,
)


class TabularJobConfigTypeDef(_RequiredTabularJobConfigTypeDef, _OptionalTabularJobConfigTypeDef):
    pass


_RequiredAutoMLChannelOutputTypeDef = TypedDict(
    "_RequiredAutoMLChannelOutputTypeDef",
    {
        "DataSource": AutoMLDataSourceOutputTypeDef,
        "TargetAttributeName": str,
    },
)
_OptionalAutoMLChannelOutputTypeDef = TypedDict(
    "_OptionalAutoMLChannelOutputTypeDef",
    {
        "CompressionType": CompressionTypeType,
        "ContentType": str,
        "ChannelType": AutoMLChannelTypeType,
        "SampleWeightAttributeName": str,
    },
    total=False,
)


class AutoMLChannelOutputTypeDef(
    _RequiredAutoMLChannelOutputTypeDef, _OptionalAutoMLChannelOutputTypeDef
):
    pass


AutoMLJobChannelOutputTypeDef = TypedDict(
    "AutoMLJobChannelOutputTypeDef",
    {
        "ChannelType": AutoMLChannelTypeType,
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "DataSource": AutoMLDataSourceOutputTypeDef,
    },
    total=False,
)

_RequiredAutoMLChannelTypeDef = TypedDict(
    "_RequiredAutoMLChannelTypeDef",
    {
        "DataSource": AutoMLDataSourceTypeDef,
        "TargetAttributeName": str,
    },
)
_OptionalAutoMLChannelTypeDef = TypedDict(
    "_OptionalAutoMLChannelTypeDef",
    {
        "CompressionType": CompressionTypeType,
        "ContentType": str,
        "ChannelType": AutoMLChannelTypeType,
        "SampleWeightAttributeName": str,
    },
    total=False,
)


class AutoMLChannelTypeDef(_RequiredAutoMLChannelTypeDef, _OptionalAutoMLChannelTypeDef):
    pass


AutoMLJobChannelTypeDef = TypedDict(
    "AutoMLJobChannelTypeDef",
    {
        "ChannelType": AutoMLChannelTypeType,
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "DataSource": AutoMLDataSourceTypeDef,
    },
    total=False,
)

ListAutoMLJobsResponseTypeDef = TypedDict(
    "ListAutoMLJobsResponseTypeDef",
    {
        "AutoMLJobSummaries": List[AutoMLJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AutoMLResolvedAttributesTypeDef = TypedDict(
    "AutoMLResolvedAttributesTypeDef",
    {
        "AutoMLJobObjective": AutoMLJobObjectiveOutputTypeDef,
        "CompletionCriteria": AutoMLJobCompletionCriteriaOutputTypeDef,
        "AutoMLProblemTypeResolvedAttributes": AutoMLProblemTypeResolvedAttributesTypeDef,
    },
    total=False,
)

AutoMLJobConfigOutputTypeDef = TypedDict(
    "AutoMLJobConfigOutputTypeDef",
    {
        "CompletionCriteria": AutoMLJobCompletionCriteriaOutputTypeDef,
        "SecurityConfig": AutoMLSecurityConfigOutputTypeDef,
        "DataSplitConfig": AutoMLDataSplitConfigOutputTypeDef,
        "CandidateGenerationConfig": AutoMLCandidateGenerationConfigOutputTypeDef,
        "Mode": AutoMLModeType,
    },
    total=False,
)

_RequiredLabelingJobAlgorithmsConfigOutputTypeDef = TypedDict(
    "_RequiredLabelingJobAlgorithmsConfigOutputTypeDef",
    {
        "LabelingJobAlgorithmSpecificationArn": str,
    },
)
_OptionalLabelingJobAlgorithmsConfigOutputTypeDef = TypedDict(
    "_OptionalLabelingJobAlgorithmsConfigOutputTypeDef",
    {
        "InitialActiveLearningModelArn": str,
        "LabelingJobResourceConfig": LabelingJobResourceConfigOutputTypeDef,
    },
    total=False,
)


class LabelingJobAlgorithmsConfigOutputTypeDef(
    _RequiredLabelingJobAlgorithmsConfigOutputTypeDef,
    _OptionalLabelingJobAlgorithmsConfigOutputTypeDef,
):
    pass


AutoMLJobConfigTypeDef = TypedDict(
    "AutoMLJobConfigTypeDef",
    {
        "CompletionCriteria": AutoMLJobCompletionCriteriaTypeDef,
        "SecurityConfig": AutoMLSecurityConfigTypeDef,
        "DataSplitConfig": AutoMLDataSplitConfigTypeDef,
        "CandidateGenerationConfig": AutoMLCandidateGenerationConfigTypeDef,
        "Mode": AutoMLModeType,
    },
    total=False,
)

_RequiredLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_RequiredLabelingJobAlgorithmsConfigTypeDef",
    {
        "LabelingJobAlgorithmSpecificationArn": str,
    },
)
_OptionalLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_OptionalLabelingJobAlgorithmsConfigTypeDef",
    {
        "InitialActiveLearningModelArn": str,
        "LabelingJobResourceConfig": LabelingJobResourceConfigTypeDef,
    },
    total=False,
)


class LabelingJobAlgorithmsConfigTypeDef(
    _RequiredLabelingJobAlgorithmsConfigTypeDef, _OptionalLabelingJobAlgorithmsConfigTypeDef
):
    pass


ModelMetricsOutputTypeDef = TypedDict(
    "ModelMetricsOutputTypeDef",
    {
        "ModelQuality": ModelQualityOutputTypeDef,
        "ModelDataQuality": ModelDataQualityOutputTypeDef,
        "Bias": BiasOutputTypeDef,
        "Explainability": ExplainabilityOutputTypeDef,
    },
    total=False,
)

ModelMetricsTypeDef = TypedDict(
    "ModelMetricsTypeDef",
    {
        "ModelQuality": ModelQualityTypeDef,
        "ModelDataQuality": ModelDataQualityTypeDef,
        "Bias": BiasTypeDef,
        "Explainability": ExplainabilityTypeDef,
    },
    total=False,
)

PipelineExecutionStepMetadataTypeDef = TypedDict(
    "PipelineExecutionStepMetadataTypeDef",
    {
        "TrainingJob": TrainingJobStepMetadataTypeDef,
        "ProcessingJob": ProcessingJobStepMetadataTypeDef,
        "TransformJob": TransformJobStepMetadataTypeDef,
        "TuningJob": TuningJobStepMetaDataTypeDef,
        "Model": ModelStepMetadataTypeDef,
        "RegisterModel": RegisterModelStepMetadataTypeDef,
        "Condition": ConditionStepMetadataTypeDef,
        "Callback": CallbackStepMetadataTypeDef,
        "Lambda": LambdaStepMetadataTypeDef,
        "QualityCheck": QualityCheckStepMetadataTypeDef,
        "ClarifyCheck": ClarifyCheckStepMetadataTypeDef,
        "EMR": EMRStepMetadataTypeDef,
        "Fail": FailStepMetadataTypeDef,
        "AutoMLJob": AutoMLJobStepMetadataTypeDef,
    },
    total=False,
)

_RequiredAutoMLCandidateTypeDef = TypedDict(
    "_RequiredAutoMLCandidateTypeDef",
    {
        "CandidateName": str,
        "ObjectiveStatus": ObjectiveStatusType,
        "CandidateSteps": List[AutoMLCandidateStepTypeDef],
        "CandidateStatus": CandidateStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLCandidateTypeDef = TypedDict(
    "_OptionalAutoMLCandidateTypeDef",
    {
        "FinalAutoMLJobObjectiveMetric": FinalAutoMLJobObjectiveMetricTypeDef,
        "InferenceContainers": List[AutoMLContainerDefinitionTypeDef],
        "EndTime": datetime,
        "FailureReason": str,
        "CandidateProperties": CandidatePropertiesTypeDef,
        "InferenceContainerDefinitions": Dict[
            AutoMLProcessingUnitType, List[AutoMLContainerDefinitionTypeDef]
        ],
    },
    total=False,
)


class AutoMLCandidateTypeDef(_RequiredAutoMLCandidateTypeDef, _OptionalAutoMLCandidateTypeDef):
    pass


_RequiredBlueGreenUpdatePolicyOutputTypeDef = TypedDict(
    "_RequiredBlueGreenUpdatePolicyOutputTypeDef",
    {
        "TrafficRoutingConfiguration": TrafficRoutingConfigOutputTypeDef,
    },
)
_OptionalBlueGreenUpdatePolicyOutputTypeDef = TypedDict(
    "_OptionalBlueGreenUpdatePolicyOutputTypeDef",
    {
        "TerminationWaitInSeconds": int,
        "MaximumExecutionTimeoutInSeconds": int,
    },
    total=False,
)


class BlueGreenUpdatePolicyOutputTypeDef(
    _RequiredBlueGreenUpdatePolicyOutputTypeDef, _OptionalBlueGreenUpdatePolicyOutputTypeDef
):
    pass


_RequiredBlueGreenUpdatePolicyTypeDef = TypedDict(
    "_RequiredBlueGreenUpdatePolicyTypeDef",
    {
        "TrafficRoutingConfiguration": TrafficRoutingConfigTypeDef,
    },
)
_OptionalBlueGreenUpdatePolicyTypeDef = TypedDict(
    "_OptionalBlueGreenUpdatePolicyTypeDef",
    {
        "TerminationWaitInSeconds": int,
        "MaximumExecutionTimeoutInSeconds": int,
    },
    total=False,
)


class BlueGreenUpdatePolicyTypeDef(
    _RequiredBlueGreenUpdatePolicyTypeDef, _OptionalBlueGreenUpdatePolicyTypeDef
):
    pass


EndpointInputConfigurationOutputTypeDef = TypedDict(
    "EndpointInputConfigurationOutputTypeDef",
    {
        "InstanceType": ProductionVariantInstanceTypeType,
        "InferenceSpecificationName": str,
        "EnvironmentParameterRanges": EnvironmentParameterRangesOutputTypeDef,
        "ServerlessConfig": ProductionVariantServerlessConfigOutputTypeDef,
    },
    total=False,
)

EndpointInputConfigurationTypeDef = TypedDict(
    "EndpointInputConfigurationTypeDef",
    {
        "InstanceType": ProductionVariantInstanceTypeType,
        "InferenceSpecificationName": str,
        "EnvironmentParameterRanges": EnvironmentParameterRangesTypeDef,
        "ServerlessConfig": ProductionVariantServerlessConfigTypeDef,
    },
    total=False,
)

_RequiredClarifyExplainerConfigOutputTypeDef = TypedDict(
    "_RequiredClarifyExplainerConfigOutputTypeDef",
    {
        "ShapConfig": ClarifyShapConfigOutputTypeDef,
    },
)
_OptionalClarifyExplainerConfigOutputTypeDef = TypedDict(
    "_OptionalClarifyExplainerConfigOutputTypeDef",
    {
        "EnableExplanations": str,
        "InferenceConfig": ClarifyInferenceConfigOutputTypeDef,
    },
    total=False,
)


class ClarifyExplainerConfigOutputTypeDef(
    _RequiredClarifyExplainerConfigOutputTypeDef, _OptionalClarifyExplainerConfigOutputTypeDef
):
    pass


_RequiredClarifyExplainerConfigTypeDef = TypedDict(
    "_RequiredClarifyExplainerConfigTypeDef",
    {
        "ShapConfig": ClarifyShapConfigTypeDef,
    },
)
_OptionalClarifyExplainerConfigTypeDef = TypedDict(
    "_OptionalClarifyExplainerConfigTypeDef",
    {
        "EnableExplanations": str,
        "InferenceConfig": ClarifyInferenceConfigTypeDef,
    },
    total=False,
)


class ClarifyExplainerConfigTypeDef(
    _RequiredClarifyExplainerConfigTypeDef, _OptionalClarifyExplainerConfigTypeDef
):
    pass


ListCodeRepositoriesOutputTypeDef = TypedDict(
    "ListCodeRepositoriesOutputTypeDef",
    {
        "CodeRepositorySummaryList": List[CodeRepositorySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListContextsResponseTypeDef = TypedDict(
    "ListContextsResponseTypeDef",
    {
        "ContextSummaries": List[ContextSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DomainSettingsForUpdateTypeDef = TypedDict(
    "DomainSettingsForUpdateTypeDef",
    {
        "RStudioServerProDomainSettingsForUpdate": RStudioServerProDomainSettingsForUpdateTypeDef,
        "ExecutionRoleIdentityConfig": ExecutionRoleIdentityConfigType,
        "SecurityGroupIds": Sequence[str],
    },
    total=False,
)

DomainSettingsTypeDef = TypedDict(
    "DomainSettingsTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "RStudioServerProDomainSettings": RStudioServerProDomainSettingsTypeDef,
        "ExecutionRoleIdentityConfig": ExecutionRoleIdentityConfigType,
    },
    total=False,
)

DefaultSpaceSettingsTypeDef = TypedDict(
    "DefaultSpaceSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": Sequence[str],
        "JupyterServerAppSettings": JupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": KernelGatewayAppSettingsTypeDef,
    },
    total=False,
)

SpaceSettingsTypeDef = TypedDict(
    "SpaceSettingsTypeDef",
    {
        "JupyterServerAppSettings": JupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": KernelGatewayAppSettingsTypeDef,
    },
    total=False,
)

UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": Sequence[str],
        "SharingSettings": SharingSettingsTypeDef,
        "JupyterServerAppSettings": JupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": KernelGatewayAppSettingsTypeDef,
        "TensorBoardAppSettings": TensorBoardAppSettingsTypeDef,
        "RStudioServerProAppSettings": RStudioServerProAppSettingsTypeDef,
        "RSessionAppSettings": RSessionAppSettingsTypeDef,
        "CanvasAppSettings": CanvasAppSettingsTypeDef,
    },
    total=False,
)

_RequiredChannelOutputTypeDef = TypedDict(
    "_RequiredChannelOutputTypeDef",
    {
        "ChannelName": str,
        "DataSource": DataSourceOutputTypeDef,
    },
)
_OptionalChannelOutputTypeDef = TypedDict(
    "_OptionalChannelOutputTypeDef",
    {
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "RecordWrapperType": RecordWrapperType,
        "InputMode": TrainingInputModeType,
        "ShuffleConfig": ShuffleConfigOutputTypeDef,
    },
    total=False,
)


class ChannelOutputTypeDef(_RequiredChannelOutputTypeDef, _OptionalChannelOutputTypeDef):
    pass


_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef",
    {
        "ChannelName": str,
        "DataSource": DataSourceTypeDef,
    },
)
_OptionalChannelTypeDef = TypedDict(
    "_OptionalChannelTypeDef",
    {
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "RecordWrapperType": RecordWrapperType,
        "InputMode": TrainingInputModeType,
        "ShuffleConfig": ShuffleConfigTypeDef,
    },
    total=False,
)


class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass


_RequiredProcessingInputOutputTypeDef = TypedDict(
    "_RequiredProcessingInputOutputTypeDef",
    {
        "InputName": str,
    },
)
_OptionalProcessingInputOutputTypeDef = TypedDict(
    "_OptionalProcessingInputOutputTypeDef",
    {
        "AppManaged": bool,
        "S3Input": ProcessingS3InputOutputTypeDef,
        "DatasetDefinition": DatasetDefinitionOutputTypeDef,
    },
    total=False,
)


class ProcessingInputOutputTypeDef(
    _RequiredProcessingInputOutputTypeDef, _OptionalProcessingInputOutputTypeDef
):
    pass


_RequiredProcessingInputTypeDef = TypedDict(
    "_RequiredProcessingInputTypeDef",
    {
        "InputName": str,
    },
)
_OptionalProcessingInputTypeDef = TypedDict(
    "_OptionalProcessingInputTypeDef",
    {
        "AppManaged": bool,
        "S3Input": ProcessingS3InputTypeDef,
        "DatasetDefinition": DatasetDefinitionTypeDef,
    },
    total=False,
)


class ProcessingInputTypeDef(_RequiredProcessingInputTypeDef, _OptionalProcessingInputTypeDef):
    pass


DescribeEdgeDeploymentPlanResponseTypeDef = TypedDict(
    "DescribeEdgeDeploymentPlanResponseTypeDef",
    {
        "EdgeDeploymentPlanArn": str,
        "EdgeDeploymentPlanName": str,
        "ModelConfigs": List[EdgeDeploymentModelConfigOutputTypeDef],
        "DeviceFleetName": str,
        "EdgeDeploymentSuccess": int,
        "EdgeDeploymentPending": int,
        "EdgeDeploymentFailed": int,
        "Stages": List[DeploymentStageStatusSummaryTypeDef],
        "NextToken": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "ModelConfigs": Sequence[EdgeDeploymentModelConfigTypeDef],
        "DeviceFleetName": str,
    },
)
_OptionalCreateEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "Stages": Sequence[DeploymentStageTypeDef],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateEdgeDeploymentPlanRequestRequestTypeDef(
    _RequiredCreateEdgeDeploymentPlanRequestRequestTypeDef,
    _OptionalCreateEdgeDeploymentPlanRequestRequestTypeDef,
):
    pass


CreateEdgeDeploymentStageRequestRequestTypeDef = TypedDict(
    "CreateEdgeDeploymentStageRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "Stages": Sequence[DeploymentStageTypeDef],
    },
)

DefaultSpaceSettingsOutputTypeDef = TypedDict(
    "DefaultSpaceSettingsOutputTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "JupyterServerAppSettings": JupyterServerAppSettingsOutputTypeDef,
        "KernelGatewayAppSettings": KernelGatewayAppSettingsOutputTypeDef,
    },
    total=False,
)

SpaceSettingsOutputTypeDef = TypedDict(
    "SpaceSettingsOutputTypeDef",
    {
        "JupyterServerAppSettings": JupyterServerAppSettingsOutputTypeDef,
        "KernelGatewayAppSettings": KernelGatewayAppSettingsOutputTypeDef,
    },
    total=False,
)

DomainSettingsOutputTypeDef = TypedDict(
    "DomainSettingsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "RStudioServerProDomainSettings": RStudioServerProDomainSettingsOutputTypeDef,
        "ExecutionRoleIdentityConfig": ExecutionRoleIdentityConfigType,
    },
    total=False,
)

UserSettingsOutputTypeDef = TypedDict(
    "UserSettingsOutputTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": SharingSettingsOutputTypeDef,
        "JupyterServerAppSettings": JupyterServerAppSettingsOutputTypeDef,
        "KernelGatewayAppSettings": KernelGatewayAppSettingsOutputTypeDef,
        "TensorBoardAppSettings": TensorBoardAppSettingsOutputTypeDef,
        "RStudioServerProAppSettings": RStudioServerProAppSettingsOutputTypeDef,
        "RSessionAppSettings": RSessionAppSettingsOutputTypeDef,
        "CanvasAppSettings": CanvasAppSettingsOutputTypeDef,
    },
    total=False,
)

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "ExperimentSummaries": List[ExperimentSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListFeatureGroupsResponseTypeDef = TypedDict(
    "ListFeatureGroupsResponseTypeDef",
    {
        "FeatureGroupSummaries": List[FeatureGroupSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListInferenceExperimentsResponseTypeDef = TypedDict(
    "ListInferenceExperimentsResponseTypeDef",
    {
        "InferenceExperiments": List[InferenceExperimentSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTrainingJobsResponseTypeDef = TypedDict(
    "ListTrainingJobsResponseTypeDef",
    {
        "TrainingJobSummaries": List[TrainingJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTrialsResponseTypeDef = TypedDict(
    "ListTrialsResponseTypeDef",
    {
        "TrialSummaries": List[TrialSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef = TypedDict(
    "UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef",
    {
        "EndpointName": str,
        "DesiredWeightsAndCapacities": Sequence[DesiredWeightAndCapacityTypeDef],
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "DeviceSummaries": List[DeviceSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DriftCheckBaselinesOutputTypeDef = TypedDict(
    "DriftCheckBaselinesOutputTypeDef",
    {
        "Bias": DriftCheckBiasOutputTypeDef,
        "Explainability": DriftCheckExplainabilityOutputTypeDef,
        "ModelQuality": DriftCheckModelQualityOutputTypeDef,
        "ModelDataQuality": DriftCheckModelDataQualityOutputTypeDef,
    },
    total=False,
)

DriftCheckBaselinesTypeDef = TypedDict(
    "DriftCheckBaselinesTypeDef",
    {
        "Bias": DriftCheckBiasTypeDef,
        "Explainability": DriftCheckExplainabilityTypeDef,
        "ModelQuality": DriftCheckModelQualityTypeDef,
        "ModelDataQuality": DriftCheckModelDataQualityTypeDef,
    },
    total=False,
)

_RequiredInferenceRecommendationTypeDef = TypedDict(
    "_RequiredInferenceRecommendationTypeDef",
    {
        "Metrics": RecommendationMetricsTypeDef,
        "EndpointConfiguration": EndpointOutputConfigurationTypeDef,
        "ModelConfiguration": ModelConfigurationTypeDef,
    },
)
_OptionalInferenceRecommendationTypeDef = TypedDict(
    "_OptionalInferenceRecommendationTypeDef",
    {
        "RecommendationId": str,
        "InvocationEndTime": datetime,
        "InvocationStartTime": datetime,
    },
    total=False,
)


class InferenceRecommendationTypeDef(
    _RequiredInferenceRecommendationTypeDef, _OptionalInferenceRecommendationTypeDef
):
    pass


_RequiredRecommendationJobInferenceBenchmarkTypeDef = TypedDict(
    "_RequiredRecommendationJobInferenceBenchmarkTypeDef",
    {
        "ModelConfiguration": ModelConfigurationTypeDef,
    },
)
_OptionalRecommendationJobInferenceBenchmarkTypeDef = TypedDict(
    "_OptionalRecommendationJobInferenceBenchmarkTypeDef",
    {
        "Metrics": RecommendationMetricsTypeDef,
        "EndpointConfiguration": EndpointOutputConfigurationTypeDef,
        "FailureReason": str,
        "EndpointMetrics": InferenceMetricsTypeDef,
        "InvocationEndTime": datetime,
        "InvocationStartTime": datetime,
    },
    total=False,
)


class RecommendationJobInferenceBenchmarkTypeDef(
    _RequiredRecommendationJobInferenceBenchmarkTypeDef,
    _OptionalRecommendationJobInferenceBenchmarkTypeDef,
):
    pass


SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "Filters": Sequence[FilterTypeDef],
        "NestedFilters": Sequence[NestedFiltersTypeDef],
        "SubExpressions": Sequence[Dict[str, Any]],
        "Operator": BooleanOperatorType,
    },
    total=False,
)

ListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {
        "TrainingJobSummaries": List[HyperParameterTrainingJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "ListHyperParameterTuningJobsResponseTypeDef",
    {
        "HyperParameterTuningJobSummaries": List[HyperParameterTuningJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociationSummaryTypeDef = TypedDict(
    "AssociationSummaryTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "SourceType": str,
        "DestinationType": str,
        "AssociationType": AssociationEdgeTypeType,
        "SourceName": str,
        "DestinationName": str,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
    },
    total=False,
)

DescribeActionResponseTypeDef = TypedDict(
    "DescribeActionResponseTypeDef",
    {
        "ActionName": str,
        "ActionArn": str,
        "Source": ActionSourceOutputTypeDef,
        "ActionType": str,
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "MetadataProperties": MetadataPropertiesOutputTypeDef,
        "LineageGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeArtifactResponseTypeDef = TypedDict(
    "DescribeArtifactResponseTypeDef",
    {
        "ArtifactName": str,
        "ArtifactArn": str,
        "Source": ArtifactSourceOutputTypeDef,
        "ArtifactType": str,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "MetadataProperties": MetadataPropertiesOutputTypeDef,
        "LineageGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeContextResponseTypeDef = TypedDict(
    "DescribeContextResponseTypeDef",
    {
        "ContextName": str,
        "ContextArn": str,
        "Source": ContextSourceOutputTypeDef,
        "ContextType": str,
        "Description": str,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "LineageGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeExperimentResponseTypeDef = TypedDict(
    "DescribeExperimentResponseTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": ExperimentSourceTypeDef,
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLineageGroupResponseTypeDef = TypedDict(
    "DescribeLineageGroupResponseTypeDef",
    {
        "LineageGroupName": str,
        "LineageGroupArn": str,
        "DisplayName": str,
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeModelCardResponseTypeDef = TypedDict(
    "DescribeModelCardResponseTypeDef",
    {
        "ModelCardArn": str,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "Content": str,
        "ModelCardStatus": ModelCardStatusType,
        "SecurityConfig": ModelCardSecurityConfigOutputTypeDef,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "ModelCardProcessingStatus": ModelCardProcessingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeModelPackageGroupOutputTypeDef = TypedDict(
    "DescribeModelPackageGroupOutputTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "ModelPackageGroupDescription": str,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribePipelineResponseTypeDef = TypedDict(
    "DescribePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "PipelineStatus": Literal["Active"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastRunTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedBy": UserContextTypeDef,
        "ParallelismConfiguration": ParallelismConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTrialComponentResponseTypeDef = TypedDict(
    "DescribeTrialComponentResponseTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "Source": TrialComponentSourceTypeDef,
        "Status": TrialComponentStatusOutputTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "Parameters": Dict[str, TrialComponentParameterValueOutputTypeDef],
        "InputArtifacts": Dict[str, TrialComponentArtifactOutputTypeDef],
        "OutputArtifacts": Dict[str, TrialComponentArtifactOutputTypeDef],
        "MetadataProperties": MetadataPropertiesOutputTypeDef,
        "Metrics": List[TrialComponentMetricSummaryTypeDef],
        "LineageGroupArn": str,
        "Sources": List[TrialComponentSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTrialResponseTypeDef = TypedDict(
    "DescribeTrialResponseTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": TrialSourceTypeDef,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "MetadataProperties": MetadataPropertiesOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": ExperimentSourceTypeDef,
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

ModelCardTypeDef = TypedDict(
    "ModelCardTypeDef",
    {
        "ModelCardArn": str,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "Content": str,
        "ModelCardStatus": ModelCardStatusType,
        "SecurityConfig": ModelCardSecurityConfigOutputTypeDef,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "Tags": List[TagOutputTypeDef],
        "ModelId": str,
        "RiskRating": str,
        "ModelPackageGroupName": str,
    },
    total=False,
)

ModelDashboardModelCardTypeDef = TypedDict(
    "ModelDashboardModelCardTypeDef",
    {
        "ModelCardArn": str,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "ModelCardStatus": ModelCardStatusType,
        "SecurityConfig": ModelCardSecurityConfigOutputTypeDef,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "Tags": List[TagOutputTypeDef],
        "ModelId": str,
        "RiskRating": str,
    },
    total=False,
)

ModelPackageGroupTypeDef = TypedDict(
    "ModelPackageGroupTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "ModelPackageGroupDescription": str,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "PipelineStatus": Literal["Active"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastRunTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedBy": UserContextTypeDef,
        "ParallelismConfiguration": ParallelismConfigurationOutputTypeDef,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

TrialComponentSimpleSummaryTypeDef = TypedDict(
    "TrialComponentSimpleSummaryTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "TrialComponentSource": TrialComponentSourceTypeDef,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
    },
    total=False,
)

TrialComponentSummaryTypeDef = TypedDict(
    "TrialComponentSummaryTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "TrialComponentSource": TrialComponentSourceTypeDef,
        "Status": TrialComponentStatusOutputTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
    },
    total=False,
)

_RequiredHyperParameterTuningJobConfigOutputTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobConfigOutputTypeDef",
    {
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "ResourceLimits": ResourceLimitsOutputTypeDef,
    },
)
_OptionalHyperParameterTuningJobConfigOutputTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobConfigOutputTypeDef",
    {
        "StrategyConfig": HyperParameterTuningJobStrategyConfigOutputTypeDef,
        "HyperParameterTuningJobObjective": HyperParameterTuningJobObjectiveOutputTypeDef,
        "ParameterRanges": ParameterRangesOutputTypeDef,
        "TrainingJobEarlyStoppingType": TrainingJobEarlyStoppingTypeType,
        "TuningJobCompletionCriteria": TuningJobCompletionCriteriaOutputTypeDef,
        "RandomSeed": int,
    },
    total=False,
)


class HyperParameterTuningJobConfigOutputTypeDef(
    _RequiredHyperParameterTuningJobConfigOutputTypeDef,
    _OptionalHyperParameterTuningJobConfigOutputTypeDef,
):
    pass


_RequiredHyperParameterSpecificationOutputTypeDef = TypedDict(
    "_RequiredHyperParameterSpecificationOutputTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
    },
)
_OptionalHyperParameterSpecificationOutputTypeDef = TypedDict(
    "_OptionalHyperParameterSpecificationOutputTypeDef",
    {
        "Description": str,
        "Range": ParameterRangeOutputTypeDef,
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)


class HyperParameterSpecificationOutputTypeDef(
    _RequiredHyperParameterSpecificationOutputTypeDef,
    _OptionalHyperParameterSpecificationOutputTypeDef,
):
    pass


_RequiredHyperParameterSpecificationTypeDef = TypedDict(
    "_RequiredHyperParameterSpecificationTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
    },
)
_OptionalHyperParameterSpecificationTypeDef = TypedDict(
    "_OptionalHyperParameterSpecificationTypeDef",
    {
        "Description": str,
        "Range": ParameterRangeTypeDef,
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)


class HyperParameterSpecificationTypeDef(
    _RequiredHyperParameterSpecificationTypeDef, _OptionalHyperParameterSpecificationTypeDef
):
    pass


_RequiredHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobConfigTypeDef",
    {
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "ResourceLimits": ResourceLimitsTypeDef,
    },
)
_OptionalHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobConfigTypeDef",
    {
        "StrategyConfig": HyperParameterTuningJobStrategyConfigTypeDef,
        "HyperParameterTuningJobObjective": HyperParameterTuningJobObjectiveTypeDef,
        "ParameterRanges": ParameterRangesTypeDef,
        "TrainingJobEarlyStoppingType": TrainingJobEarlyStoppingTypeType,
        "TuningJobCompletionCriteria": TuningJobCompletionCriteriaTypeDef,
        "RandomSeed": int,
    },
    total=False,
)


class HyperParameterTuningJobConfigTypeDef(
    _RequiredHyperParameterTuningJobConfigTypeDef, _OptionalHyperParameterTuningJobConfigTypeDef
):
    pass


AppImageConfigDetailsTypeDef = TypedDict(
    "AppImageConfigDetailsTypeDef",
    {
        "AppImageConfigArn": str,
        "AppImageConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "KernelGatewayImageConfig": KernelGatewayImageConfigOutputTypeDef,
    },
    total=False,
)

DescribeAppImageConfigResponseTypeDef = TypedDict(
    "DescribeAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "AppImageConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "KernelGatewayImageConfig": KernelGatewayImageConfigOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateAppImageConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)
_OptionalCreateAppImageConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppImageConfigRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
        "KernelGatewayImageConfig": KernelGatewayImageConfigTypeDef,
    },
    total=False,
)


class CreateAppImageConfigRequestRequestTypeDef(
    _RequiredCreateAppImageConfigRequestRequestTypeDef,
    _OptionalCreateAppImageConfigRequestRequestTypeDef,
):
    pass


_RequiredUpdateAppImageConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)
_OptionalUpdateAppImageConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppImageConfigRequestRequestTypeDef",
    {
        "KernelGatewayImageConfig": KernelGatewayImageConfigTypeDef,
    },
    total=False,
)


class UpdateAppImageConfigRequestRequestTypeDef(
    _RequiredUpdateAppImageConfigRequestRequestTypeDef,
    _OptionalUpdateAppImageConfigRequestRequestTypeDef,
):
    pass


ListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "ListLabelingJobsForWorkteamResponseTypeDef",
    {
        "LabelingJobSummaryList": List[LabelingJobForWorkteamSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredLabelingJobInputConfigOutputTypeDef = TypedDict(
    "_RequiredLabelingJobInputConfigOutputTypeDef",
    {
        "DataSource": LabelingJobDataSourceOutputTypeDef,
    },
)
_OptionalLabelingJobInputConfigOutputTypeDef = TypedDict(
    "_OptionalLabelingJobInputConfigOutputTypeDef",
    {
        "DataAttributes": LabelingJobDataAttributesOutputTypeDef,
    },
    total=False,
)


class LabelingJobInputConfigOutputTypeDef(
    _RequiredLabelingJobInputConfigOutputTypeDef, _OptionalLabelingJobInputConfigOutputTypeDef
):
    pass


_RequiredLabelingJobInputConfigTypeDef = TypedDict(
    "_RequiredLabelingJobInputConfigTypeDef",
    {
        "DataSource": LabelingJobDataSourceTypeDef,
    },
)
_OptionalLabelingJobInputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobInputConfigTypeDef",
    {
        "DataAttributes": LabelingJobDataAttributesTypeDef,
    },
    total=False,
)


class LabelingJobInputConfigTypeDef(
    _RequiredLabelingJobInputConfigTypeDef, _OptionalLabelingJobInputConfigTypeDef
):
    pass


_RequiredWorkteamTypeDef = TypedDict(
    "_RequiredWorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[MemberDefinitionOutputTypeDef],
        "WorkteamArn": str,
        "Description": str,
    },
)
_OptionalWorkteamTypeDef = TypedDict(
    "_OptionalWorkteamTypeDef",
    {
        "WorkforceArn": str,
        "ProductListingIds": List[str],
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": NotificationConfigurationOutputTypeDef,
    },
    total=False,
)


class WorkteamTypeDef(_RequiredWorkteamTypeDef, _OptionalWorkteamTypeDef):
    pass


_RequiredCreateWorkteamRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": Sequence[MemberDefinitionTypeDef],
        "Description": str,
    },
)
_OptionalCreateWorkteamRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkteamRequestRequestTypeDef",
    {
        "WorkforceName": str,
        "NotificationConfiguration": NotificationConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateWorkteamRequestRequestTypeDef(
    _RequiredCreateWorkteamRequestRequestTypeDef, _OptionalCreateWorkteamRequestRequestTypeDef
):
    pass


_RequiredUpdateWorkteamRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
    },
)
_OptionalUpdateWorkteamRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkteamRequestRequestTypeDef",
    {
        "MemberDefinitions": Sequence[MemberDefinitionTypeDef],
        "Description": str,
        "NotificationConfiguration": NotificationConfigurationTypeDef,
    },
    total=False,
)


class UpdateWorkteamRequestRequestTypeDef(
    _RequiredUpdateWorkteamRequestRequestTypeDef, _OptionalUpdateWorkteamRequestRequestTypeDef
):
    pass


MonitoringAlertSummaryTypeDef = TypedDict(
    "MonitoringAlertSummaryTypeDef",
    {
        "MonitoringAlertName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "AlertStatus": MonitoringAlertStatusType,
        "DatapointsToAlert": int,
        "EvaluationPeriod": int,
        "Actions": MonitoringAlertActionsTypeDef,
    },
)

ContainerDefinitionOutputTypeDef = TypedDict(
    "ContainerDefinitionOutputTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageConfig": ImageConfigOutputTypeDef,
        "Mode": ContainerModeType,
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
        "InferenceSpecificationName": str,
        "MultiModelConfig": MultiModelConfigOutputTypeDef,
        "ModelDataSource": ModelDataSourceOutputTypeDef,
    },
    total=False,
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageConfig": ImageConfigTypeDef,
        "Mode": ContainerModeType,
        "ModelDataUrl": str,
        "Environment": Mapping[str, str],
        "ModelPackageName": str,
        "InferenceSpecificationName": str,
        "MultiModelConfig": MultiModelConfigTypeDef,
        "ModelDataSource": ModelDataSourceTypeDef,
    },
    total=False,
)

ModelVariantConfigSummaryTypeDef = TypedDict(
    "ModelVariantConfigSummaryTypeDef",
    {
        "ModelName": str,
        "VariantName": str,
        "InfrastructureConfig": ModelInfrastructureConfigOutputTypeDef,
        "Status": ModelVariantStatusType,
    },
)

ModelVariantConfigTypeDef = TypedDict(
    "ModelVariantConfigTypeDef",
    {
        "ModelName": str,
        "VariantName": str,
        "InfrastructureConfig": ModelInfrastructureConfigTypeDef,
    },
)

_RequiredAdditionalInferenceSpecificationDefinitionOutputTypeDef = TypedDict(
    "_RequiredAdditionalInferenceSpecificationDefinitionOutputTypeDef",
    {
        "Name": str,
        "Containers": List[ModelPackageContainerDefinitionOutputTypeDef],
    },
)
_OptionalAdditionalInferenceSpecificationDefinitionOutputTypeDef = TypedDict(
    "_OptionalAdditionalInferenceSpecificationDefinitionOutputTypeDef",
    {
        "Description": str,
        "SupportedTransformInstanceTypes": List[TransformInstanceTypeType],
        "SupportedRealtimeInferenceInstanceTypes": List[ProductionVariantInstanceTypeType],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)


class AdditionalInferenceSpecificationDefinitionOutputTypeDef(
    _RequiredAdditionalInferenceSpecificationDefinitionOutputTypeDef,
    _OptionalAdditionalInferenceSpecificationDefinitionOutputTypeDef,
):
    pass


_RequiredInferenceSpecificationOutputTypeDef = TypedDict(
    "_RequiredInferenceSpecificationOutputTypeDef",
    {
        "Containers": List[ModelPackageContainerDefinitionOutputTypeDef],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
)
_OptionalInferenceSpecificationOutputTypeDef = TypedDict(
    "_OptionalInferenceSpecificationOutputTypeDef",
    {
        "SupportedTransformInstanceTypes": List[TransformInstanceTypeType],
        "SupportedRealtimeInferenceInstanceTypes": List[ProductionVariantInstanceTypeType],
    },
    total=False,
)


class InferenceSpecificationOutputTypeDef(
    _RequiredInferenceSpecificationOutputTypeDef, _OptionalInferenceSpecificationOutputTypeDef
):
    pass


_RequiredAdditionalInferenceSpecificationDefinitionTypeDef = TypedDict(
    "_RequiredAdditionalInferenceSpecificationDefinitionTypeDef",
    {
        "Name": str,
        "Containers": Sequence[ModelPackageContainerDefinitionTypeDef],
    },
)
_OptionalAdditionalInferenceSpecificationDefinitionTypeDef = TypedDict(
    "_OptionalAdditionalInferenceSpecificationDefinitionTypeDef",
    {
        "Description": str,
        "SupportedTransformInstanceTypes": Sequence[TransformInstanceTypeType],
        "SupportedRealtimeInferenceInstanceTypes": Sequence[ProductionVariantInstanceTypeType],
        "SupportedContentTypes": Sequence[str],
        "SupportedResponseMIMETypes": Sequence[str],
    },
    total=False,
)


class AdditionalInferenceSpecificationDefinitionTypeDef(
    _RequiredAdditionalInferenceSpecificationDefinitionTypeDef,
    _OptionalAdditionalInferenceSpecificationDefinitionTypeDef,
):
    pass


_RequiredInferenceSpecificationTypeDef = TypedDict(
    "_RequiredInferenceSpecificationTypeDef",
    {
        "Containers": Sequence[ModelPackageContainerDefinitionTypeDef],
        "SupportedContentTypes": Sequence[str],
        "SupportedResponseMIMETypes": Sequence[str],
    },
)
_OptionalInferenceSpecificationTypeDef = TypedDict(
    "_OptionalInferenceSpecificationTypeDef",
    {
        "SupportedTransformInstanceTypes": Sequence[TransformInstanceTypeType],
        "SupportedRealtimeInferenceInstanceTypes": Sequence[ProductionVariantInstanceTypeType],
    },
    total=False,
)


class InferenceSpecificationTypeDef(
    _RequiredInferenceSpecificationTypeDef, _OptionalInferenceSpecificationTypeDef
):
    pass


ListModelMetadataRequestListModelMetadataPaginateTypeDef = TypedDict(
    "ListModelMetadataRequestListModelMetadataPaginateTypeDef",
    {
        "SearchExpression": ModelMetadataSearchExpressionTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListModelMetadataRequestRequestTypeDef = TypedDict(
    "ListModelMetadataRequestRequestTypeDef",
    {
        "SearchExpression": ModelMetadataSearchExpressionTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredBatchTransformInputOutputTypeDef = TypedDict(
    "_RequiredBatchTransformInputOutputTypeDef",
    {
        "DataCapturedDestinationS3Uri": str,
        "DatasetFormat": MonitoringDatasetFormatOutputTypeDef,
        "LocalPath": str,
    },
)
_OptionalBatchTransformInputOutputTypeDef = TypedDict(
    "_OptionalBatchTransformInputOutputTypeDef",
    {
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "FeaturesAttribute": str,
        "InferenceAttribute": str,
        "ProbabilityAttribute": str,
        "ProbabilityThresholdAttribute": float,
        "StartTimeOffset": str,
        "EndTimeOffset": str,
    },
    total=False,
)


class BatchTransformInputOutputTypeDef(
    _RequiredBatchTransformInputOutputTypeDef, _OptionalBatchTransformInputOutputTypeDef
):
    pass


_RequiredBatchTransformInputTypeDef = TypedDict(
    "_RequiredBatchTransformInputTypeDef",
    {
        "DataCapturedDestinationS3Uri": str,
        "DatasetFormat": MonitoringDatasetFormatTypeDef,
        "LocalPath": str,
    },
)
_OptionalBatchTransformInputTypeDef = TypedDict(
    "_OptionalBatchTransformInputTypeDef",
    {
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "FeaturesAttribute": str,
        "InferenceAttribute": str,
        "ProbabilityAttribute": str,
        "ProbabilityThresholdAttribute": float,
        "StartTimeOffset": str,
        "EndTimeOffset": str,
    },
    total=False,
)


class BatchTransformInputTypeDef(
    _RequiredBatchTransformInputTypeDef, _OptionalBatchTransformInputTypeDef
):
    pass


_RequiredMonitoringOutputConfigOutputTypeDef = TypedDict(
    "_RequiredMonitoringOutputConfigOutputTypeDef",
    {
        "MonitoringOutputs": List[MonitoringOutputTypeDef],
    },
)
_OptionalMonitoringOutputConfigOutputTypeDef = TypedDict(
    "_OptionalMonitoringOutputConfigOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class MonitoringOutputConfigOutputTypeDef(
    _RequiredMonitoringOutputConfigOutputTypeDef, _OptionalMonitoringOutputConfigOutputTypeDef
):
    pass


_RequiredMonitoringOutputConfigTypeDef = TypedDict(
    "_RequiredMonitoringOutputConfigTypeDef",
    {
        "MonitoringOutputs": Sequence[MonitoringOutputTypeDef],
    },
)
_OptionalMonitoringOutputConfigTypeDef = TypedDict(
    "_OptionalMonitoringOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class MonitoringOutputConfigTypeDef(
    _RequiredMonitoringOutputConfigTypeDef, _OptionalMonitoringOutputConfigTypeDef
):
    pass


DescribeFeatureGroupResponseTypeDef = TypedDict(
    "DescribeFeatureGroupResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List[FeatureDefinitionOutputTypeDef],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "OnlineStoreConfig": OnlineStoreConfigOutputTypeDef,
        "OfflineStoreConfig": OfflineStoreConfigOutputTypeDef,
        "RoleArn": str,
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": OfflineStoreStatusTypeDef,
        "LastUpdateStatus": LastUpdateStatusTypeDef,
        "FailureReason": str,
        "Description": str,
        "NextToken": str,
        "OnlineStoreTotalSizeBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FeatureGroupTypeDef = TypedDict(
    "FeatureGroupTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List[FeatureDefinitionOutputTypeDef],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "OnlineStoreConfig": OnlineStoreConfigOutputTypeDef,
        "OfflineStoreConfig": OfflineStoreConfigOutputTypeDef,
        "RoleArn": str,
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": OfflineStoreStatusTypeDef,
        "LastUpdateStatus": LastUpdateStatusTypeDef,
        "FailureReason": str,
        "Description": str,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

_RequiredCreateFeatureGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": Sequence[FeatureDefinitionTypeDef],
    },
)
_OptionalCreateFeatureGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFeatureGroupRequestRequestTypeDef",
    {
        "OnlineStoreConfig": OnlineStoreConfigTypeDef,
        "OfflineStoreConfig": OfflineStoreConfigTypeDef,
        "RoleArn": str,
        "Description": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateFeatureGroupRequestRequestTypeDef(
    _RequiredCreateFeatureGroupRequestRequestTypeDef,
    _OptionalCreateFeatureGroupRequestRequestTypeDef,
):
    pass


_RequiredUpdateFeatureGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)
_OptionalUpdateFeatureGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFeatureGroupRequestRequestTypeDef",
    {
        "FeatureAdditions": Sequence[FeatureDefinitionTypeDef],
        "OnlineStoreConfig": OnlineStoreConfigUpdateTypeDef,
    },
    total=False,
)


class UpdateFeatureGroupRequestRequestTypeDef(
    _RequiredUpdateFeatureGroupRequestRequestTypeDef,
    _OptionalUpdateFeatureGroupRequestRequestTypeDef,
):
    pass


DescribeCompilationJobResponseTypeDef = TypedDict(
    "DescribeCompilationJobResponseTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CompilationJobStatus": CompilationJobStatusType,
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "StoppingCondition": StoppingConditionOutputTypeDef,
        "InferenceImage": str,
        "ModelPackageVersionArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ModelArtifacts": ModelArtifactsTypeDef,
        "ModelDigests": ModelDigestsTypeDef,
        "RoleArn": str,
        "InputConfig": InputConfigOutputTypeDef,
        "OutputConfig": OutputConfigOutputTypeDef,
        "VpcConfig": NeoVpcConfigOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateCompilationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
        "RoleArn": str,
        "OutputConfig": OutputConfigTypeDef,
        "StoppingCondition": StoppingConditionTypeDef,
    },
)
_OptionalCreateCompilationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCompilationJobRequestRequestTypeDef",
    {
        "ModelPackageVersionArn": str,
        "InputConfig": InputConfigTypeDef,
        "VpcConfig": NeoVpcConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateCompilationJobRequestRequestTypeDef(
    _RequiredCreateCompilationJobRequestRequestTypeDef,
    _OptionalCreateCompilationJobRequestRequestTypeDef,
):
    pass


_RequiredPendingDeploymentSummaryTypeDef = TypedDict(
    "_RequiredPendingDeploymentSummaryTypeDef",
    {
        "EndpointConfigName": str,
    },
)
_OptionalPendingDeploymentSummaryTypeDef = TypedDict(
    "_OptionalPendingDeploymentSummaryTypeDef",
    {
        "ProductionVariants": List[PendingProductionVariantSummaryTypeDef],
        "StartTime": datetime,
        "ShadowProductionVariants": List[PendingProductionVariantSummaryTypeDef],
    },
    total=False,
)


class PendingDeploymentSummaryTypeDef(
    _RequiredPendingDeploymentSummaryTypeDef, _OptionalPendingDeploymentSummaryTypeDef
):
    pass


_RequiredProcessingOutputConfigOutputTypeDef = TypedDict(
    "_RequiredProcessingOutputConfigOutputTypeDef",
    {
        "Outputs": List[ProcessingOutputTypeDef],
    },
)
_OptionalProcessingOutputConfigOutputTypeDef = TypedDict(
    "_OptionalProcessingOutputConfigOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class ProcessingOutputConfigOutputTypeDef(
    _RequiredProcessingOutputConfigOutputTypeDef, _OptionalProcessingOutputConfigOutputTypeDef
):
    pass


_RequiredProcessingOutputConfigTypeDef = TypedDict(
    "_RequiredProcessingOutputConfigTypeDef",
    {
        "Outputs": Sequence[ProcessingOutputTypeDef],
    },
)
_OptionalProcessingOutputConfigTypeDef = TypedDict(
    "_OptionalProcessingOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class ProcessingOutputConfigTypeDef(
    _RequiredProcessingOutputConfigTypeDef, _OptionalProcessingOutputConfigTypeDef
):
    pass


_RequiredGetSearchSuggestionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSearchSuggestionsRequestRequestTypeDef",
    {
        "Resource": ResourceTypeType,
    },
)
_OptionalGetSearchSuggestionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSearchSuggestionsRequestRequestTypeDef",
    {
        "SuggestionQuery": SuggestionQueryTypeDef,
    },
    total=False,
)


class GetSearchSuggestionsRequestRequestTypeDef(
    _RequiredGetSearchSuggestionsRequestRequestTypeDef,
    _OptionalGetSearchSuggestionsRequestRequestTypeDef,
):
    pass


DescribeProjectOutputTypeDef = TypedDict(
    "DescribeProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "ProjectId": str,
        "ProjectDescription": str,
        "ServiceCatalogProvisioningDetails": ServiceCatalogProvisioningDetailsOutputTypeDef,
        "ServiceCatalogProvisionedProductDetails": ServiceCatalogProvisionedProductDetailsTypeDef,
        "ProjectStatus": ProjectStatusType,
        "CreatedBy": UserContextTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "ProjectId": str,
        "ProjectDescription": str,
        "ServiceCatalogProvisioningDetails": ServiceCatalogProvisioningDetailsOutputTypeDef,
        "ServiceCatalogProvisionedProductDetails": ServiceCatalogProvisionedProductDetailsTypeDef,
        "ProjectStatus": ProjectStatusType,
        "CreatedBy": UserContextTypeDef,
        "CreationTime": datetime,
        "Tags": List[TagOutputTypeDef],
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
    },
    total=False,
)

_RequiredCreateProjectInputRequestTypeDef = TypedDict(
    "_RequiredCreateProjectInputRequestTypeDef",
    {
        "ProjectName": str,
        "ServiceCatalogProvisioningDetails": ServiceCatalogProvisioningDetailsTypeDef,
    },
)
_OptionalCreateProjectInputRequestTypeDef = TypedDict(
    "_OptionalCreateProjectInputRequestTypeDef",
    {
        "ProjectDescription": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateProjectInputRequestTypeDef(
    _RequiredCreateProjectInputRequestTypeDef, _OptionalCreateProjectInputRequestTypeDef
):
    pass


_RequiredUpdateProjectInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectInputRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalUpdateProjectInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectInputRequestTypeDef",
    {
        "ProjectDescription": str,
        "ServiceCatalogProvisioningUpdateDetails": ServiceCatalogProvisioningUpdateDetailsTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class UpdateProjectInputRequestTypeDef(
    _RequiredUpdateProjectInputRequestTypeDef, _OptionalUpdateProjectInputRequestTypeDef
):
    pass


_RequiredHumanLoopConfigOutputTypeDef = TypedDict(
    "_RequiredHumanLoopConfigOutputTypeDef",
    {
        "WorkteamArn": str,
        "HumanTaskUiArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "TaskCount": int,
    },
)
_OptionalHumanLoopConfigOutputTypeDef = TypedDict(
    "_OptionalHumanLoopConfigOutputTypeDef",
    {
        "TaskAvailabilityLifetimeInSeconds": int,
        "TaskTimeLimitInSeconds": int,
        "TaskKeywords": List[str],
        "PublicWorkforceTaskPrice": PublicWorkforceTaskPriceOutputTypeDef,
    },
    total=False,
)


class HumanLoopConfigOutputTypeDef(
    _RequiredHumanLoopConfigOutputTypeDef, _OptionalHumanLoopConfigOutputTypeDef
):
    pass


_RequiredHumanTaskConfigOutputTypeDef = TypedDict(
    "_RequiredHumanTaskConfigOutputTypeDef",
    {
        "WorkteamArn": str,
        "UiConfig": UiConfigOutputTypeDef,
        "PreHumanTaskLambdaArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "AnnotationConsolidationConfig": AnnotationConsolidationConfigOutputTypeDef,
    },
)
_OptionalHumanTaskConfigOutputTypeDef = TypedDict(
    "_OptionalHumanTaskConfigOutputTypeDef",
    {
        "TaskKeywords": List[str],
        "TaskAvailabilityLifetimeInSeconds": int,
        "MaxConcurrentTaskCount": int,
        "PublicWorkforceTaskPrice": PublicWorkforceTaskPriceOutputTypeDef,
    },
    total=False,
)


class HumanTaskConfigOutputTypeDef(
    _RequiredHumanTaskConfigOutputTypeDef, _OptionalHumanTaskConfigOutputTypeDef
):
    pass


_RequiredHumanLoopConfigTypeDef = TypedDict(
    "_RequiredHumanLoopConfigTypeDef",
    {
        "WorkteamArn": str,
        "HumanTaskUiArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "TaskCount": int,
    },
)
_OptionalHumanLoopConfigTypeDef = TypedDict(
    "_OptionalHumanLoopConfigTypeDef",
    {
        "TaskAvailabilityLifetimeInSeconds": int,
        "TaskTimeLimitInSeconds": int,
        "TaskKeywords": Sequence[str],
        "PublicWorkforceTaskPrice": PublicWorkforceTaskPriceTypeDef,
    },
    total=False,
)


class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, _OptionalHumanLoopConfigTypeDef):
    pass


_RequiredHumanTaskConfigTypeDef = TypedDict(
    "_RequiredHumanTaskConfigTypeDef",
    {
        "WorkteamArn": str,
        "UiConfig": UiConfigTypeDef,
        "PreHumanTaskLambdaArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "AnnotationConsolidationConfig": AnnotationConsolidationConfigTypeDef,
    },
)
_OptionalHumanTaskConfigTypeDef = TypedDict(
    "_OptionalHumanTaskConfigTypeDef",
    {
        "TaskKeywords": Sequence[str],
        "TaskAvailabilityLifetimeInSeconds": int,
        "MaxConcurrentTaskCount": int,
        "PublicWorkforceTaskPrice": PublicWorkforceTaskPriceTypeDef,
    },
    total=False,
)


class HumanTaskConfigTypeDef(_RequiredHumanTaskConfigTypeDef, _OptionalHumanTaskConfigTypeDef):
    pass


DescribePipelineExecutionResponseTypeDef = TypedDict(
    "DescribePipelineExecutionResponseTypeDef",
    {
        "PipelineArn": str,
        "PipelineExecutionArn": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExperimentConfig": PipelineExperimentConfigTypeDef,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedBy": UserContextTypeDef,
        "ParallelismConfiguration": ParallelismConfigurationOutputTypeDef,
        "SelectiveExecutionConfig": SelectiveExecutionConfigOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "PipelineArn": str,
        "PipelineExecutionArn": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExperimentConfig": PipelineExperimentConfigTypeDef,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedBy": UserContextTypeDef,
        "ParallelismConfiguration": ParallelismConfigurationOutputTypeDef,
        "PipelineParameters": List[ParameterOutputTypeDef],
        "SelectiveExecutionConfig": SelectiveExecutionConfigOutputTypeDef,
    },
    total=False,
)

_RequiredStartPipelineExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
    },
)
_OptionalStartPipelineExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionDisplayName": str,
        "PipelineParameters": Sequence[ParameterTypeDef],
        "PipelineExecutionDescription": str,
        "ParallelismConfiguration": ParallelismConfigurationTypeDef,
        "SelectiveExecutionConfig": SelectiveExecutionConfigTypeDef,
    },
    total=False,
)


class StartPipelineExecutionRequestRequestTypeDef(
    _RequiredStartPipelineExecutionRequestRequestTypeDef,
    _OptionalStartPipelineExecutionRequestRequestTypeDef,
):
    pass


_RequiredAlgorithmSpecificationOutputTypeDef = TypedDict(
    "_RequiredAlgorithmSpecificationOutputTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
    },
)
_OptionalAlgorithmSpecificationOutputTypeDef = TypedDict(
    "_OptionalAlgorithmSpecificationOutputTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": List[MetricDefinitionOutputTypeDef],
        "EnableSageMakerMetricsTimeSeries": bool,
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "TrainingImageConfig": TrainingImageConfigOutputTypeDef,
    },
    total=False,
)


class AlgorithmSpecificationOutputTypeDef(
    _RequiredAlgorithmSpecificationOutputTypeDef, _OptionalAlgorithmSpecificationOutputTypeDef
):
    pass


_RequiredAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredAlgorithmSpecificationTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
    },
)
_OptionalAlgorithmSpecificationTypeDef = TypedDict(
    "_OptionalAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": Sequence[MetricDefinitionTypeDef],
        "EnableSageMakerMetricsTimeSeries": bool,
        "ContainerEntrypoint": Sequence[str],
        "ContainerArguments": Sequence[str],
        "TrainingImageConfig": TrainingImageConfigTypeDef,
    },
    total=False,
)


class AlgorithmSpecificationTypeDef(
    _RequiredAlgorithmSpecificationTypeDef, _OptionalAlgorithmSpecificationTypeDef
):
    pass


_RequiredTransformInputOutputTypeDef = TypedDict(
    "_RequiredTransformInputOutputTypeDef",
    {
        "DataSource": TransformDataSourceOutputTypeDef,
    },
)
_OptionalTransformInputOutputTypeDef = TypedDict(
    "_OptionalTransformInputOutputTypeDef",
    {
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "SplitType": SplitTypeType,
    },
    total=False,
)


class TransformInputOutputTypeDef(
    _RequiredTransformInputOutputTypeDef, _OptionalTransformInputOutputTypeDef
):
    pass


_RequiredTransformInputTypeDef = TypedDict(
    "_RequiredTransformInputTypeDef",
    {
        "DataSource": TransformDataSourceTypeDef,
    },
)
_OptionalTransformInputTypeDef = TypedDict(
    "_OptionalTransformInputTypeDef",
    {
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "SplitType": SplitTypeType,
    },
    total=False,
)


class TransformInputTypeDef(_RequiredTransformInputTypeDef, _OptionalTransformInputTypeDef):
    pass


DescribeWorkforceResponseTypeDef = TypedDict(
    "DescribeWorkforceResponseTypeDef",
    {
        "Workforce": WorkforceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListWorkforcesResponseTypeDef = TypedDict(
    "ListWorkforcesResponseTypeDef",
    {
        "Workforces": List[WorkforceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateWorkforceResponseTypeDef = TypedDict(
    "UpdateWorkforceResponseTypeDef",
    {
        "Workforce": WorkforceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListArtifactsResponseTypeDef = TypedDict(
    "ListArtifactsResponseTypeDef",
    {
        "ArtifactSummaries": List[ArtifactSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AutoMLProblemTypeConfigOutputTypeDef = TypedDict(
    "AutoMLProblemTypeConfigOutputTypeDef",
    {
        "ImageClassificationJobConfig": ImageClassificationJobConfigOutputTypeDef,
        "TextClassificationJobConfig": TextClassificationJobConfigOutputTypeDef,
        "TabularJobConfig": TabularJobConfigOutputTypeDef,
        "TimeSeriesForecastingJobConfig": TimeSeriesForecastingJobConfigOutputTypeDef,
    },
    total=False,
)

AutoMLProblemTypeConfigTypeDef = TypedDict(
    "AutoMLProblemTypeConfigTypeDef",
    {
        "ImageClassificationJobConfig": ImageClassificationJobConfigTypeDef,
        "TextClassificationJobConfig": TextClassificationJobConfigTypeDef,
        "TabularJobConfig": TabularJobConfigTypeDef,
        "TimeSeriesForecastingJobConfig": TimeSeriesForecastingJobConfigTypeDef,
    },
    total=False,
)

_RequiredCreateAutoMLJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
        "InputDataConfig": Sequence[AutoMLChannelTypeDef],
        "OutputDataConfig": AutoMLOutputDataConfigTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateAutoMLJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAutoMLJobRequestRequestTypeDef",
    {
        "ProblemType": ProblemTypeType,
        "AutoMLJobObjective": AutoMLJobObjectiveTypeDef,
        "AutoMLJobConfig": AutoMLJobConfigTypeDef,
        "GenerateCandidateDefinitionsOnly": bool,
        "Tags": Sequence[TagTypeDef],
        "ModelDeployConfig": ModelDeployConfigTypeDef,
    },
    total=False,
)


class CreateAutoMLJobRequestRequestTypeDef(
    _RequiredCreateAutoMLJobRequestRequestTypeDef, _OptionalCreateAutoMLJobRequestRequestTypeDef
):
    pass


PipelineExecutionStepTypeDef = TypedDict(
    "PipelineExecutionStepTypeDef",
    {
        "StepName": str,
        "StepDisplayName": str,
        "StepDescription": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StepStatus": StepStatusType,
        "CacheHitResult": CacheHitResultTypeDef,
        "AttemptCount": int,
        "FailureReason": str,
        "Metadata": PipelineExecutionStepMetadataTypeDef,
        "SelectiveExecutionResult": SelectiveExecutionResultTypeDef,
    },
    total=False,
)

DescribeAutoMLJobResponseTypeDef = TypedDict(
    "DescribeAutoMLJobResponseTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "InputDataConfig": List[AutoMLChannelOutputTypeDef],
        "OutputDataConfig": AutoMLOutputDataConfigOutputTypeDef,
        "RoleArn": str,
        "AutoMLJobObjective": AutoMLJobObjectiveOutputTypeDef,
        "ProblemType": ProblemTypeType,
        "AutoMLJobConfig": AutoMLJobConfigOutputTypeDef,
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List[AutoMLPartialFailureReasonTypeDef],
        "BestCandidate": AutoMLCandidateTypeDef,
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "GenerateCandidateDefinitionsOnly": bool,
        "AutoMLJobArtifacts": AutoMLJobArtifactsTypeDef,
        "ResolvedAttributes": ResolvedAttributesTypeDef,
        "ModelDeployConfig": ModelDeployConfigOutputTypeDef,
        "ModelDeployResult": ModelDeployResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCandidatesForAutoMLJobResponseTypeDef = TypedDict(
    "ListCandidatesForAutoMLJobResponseTypeDef",
    {
        "Candidates": List[AutoMLCandidateTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeploymentConfigOutputTypeDef = TypedDict(
    "DeploymentConfigOutputTypeDef",
    {
        "BlueGreenUpdatePolicy": BlueGreenUpdatePolicyOutputTypeDef,
        "AutoRollbackConfiguration": AutoRollbackConfigOutputTypeDef,
        "RollingUpdatePolicy": RollingUpdatePolicyOutputTypeDef,
    },
    total=False,
)

DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "BlueGreenUpdatePolicy": BlueGreenUpdatePolicyTypeDef,
        "AutoRollbackConfiguration": AutoRollbackConfigTypeDef,
        "RollingUpdatePolicy": RollingUpdatePolicyTypeDef,
    },
    total=False,
)

RecommendationJobInputConfigOutputTypeDef = TypedDict(
    "RecommendationJobInputConfigOutputTypeDef",
    {
        "ModelPackageVersionArn": str,
        "JobDurationInSeconds": int,
        "TrafficPattern": TrafficPatternOutputTypeDef,
        "ResourceLimit": RecommendationJobResourceLimitOutputTypeDef,
        "EndpointConfigurations": List[EndpointInputConfigurationOutputTypeDef],
        "VolumeKmsKeyId": str,
        "ContainerConfig": RecommendationJobContainerConfigOutputTypeDef,
        "Endpoints": List[EndpointInfoOutputTypeDef],
        "VpcConfig": RecommendationJobVpcConfigOutputTypeDef,
        "ModelName": str,
    },
    total=False,
)

RecommendationJobInputConfigTypeDef = TypedDict(
    "RecommendationJobInputConfigTypeDef",
    {
        "ModelPackageVersionArn": str,
        "JobDurationInSeconds": int,
        "TrafficPattern": TrafficPatternTypeDef,
        "ResourceLimit": RecommendationJobResourceLimitTypeDef,
        "EndpointConfigurations": Sequence[EndpointInputConfigurationTypeDef],
        "VolumeKmsKeyId": str,
        "ContainerConfig": RecommendationJobContainerConfigTypeDef,
        "Endpoints": Sequence[EndpointInfoTypeDef],
        "VpcConfig": RecommendationJobVpcConfigTypeDef,
        "ModelName": str,
    },
    total=False,
)

ExplainerConfigOutputTypeDef = TypedDict(
    "ExplainerConfigOutputTypeDef",
    {
        "ClarifyExplainerConfig": ClarifyExplainerConfigOutputTypeDef,
    },
    total=False,
)

ExplainerConfigTypeDef = TypedDict(
    "ExplainerConfigTypeDef",
    {
        "ClarifyExplainerConfig": ClarifyExplainerConfigTypeDef,
    },
    total=False,
)

_RequiredCreateSpaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSpaceRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
    },
)
_OptionalCreateSpaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSpaceRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
        "SpaceSettings": SpaceSettingsTypeDef,
    },
    total=False,
)


class CreateSpaceRequestRequestTypeDef(
    _RequiredCreateSpaceRequestRequestTypeDef, _OptionalCreateSpaceRequestRequestTypeDef
):
    pass


_RequiredUpdateSpaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSpaceRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
    },
)
_OptionalUpdateSpaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSpaceRequestRequestTypeDef",
    {
        "SpaceSettings": SpaceSettingsTypeDef,
    },
    total=False,
)


class UpdateSpaceRequestRequestTypeDef(
    _RequiredUpdateSpaceRequestRequestTypeDef, _OptionalUpdateSpaceRequestRequestTypeDef
):
    pass


_RequiredCreateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "AuthMode": AuthModeType,
        "DefaultUserSettings": UserSettingsTypeDef,
        "SubnetIds": Sequence[str],
        "VpcId": str,
    },
)
_OptionalCreateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
        "AppNetworkAccessType": AppNetworkAccessTypeType,
        "HomeEfsFileSystemKmsKeyId": str,
        "KmsKeyId": str,
        "AppSecurityGroupManagement": AppSecurityGroupManagementType,
        "DomainSettings": DomainSettingsTypeDef,
        "DefaultSpaceSettings": DefaultSpaceSettingsTypeDef,
    },
    total=False,
)


class CreateDomainRequestRequestTypeDef(
    _RequiredCreateDomainRequestRequestTypeDef, _OptionalCreateDomainRequestRequestTypeDef
):
    pass


_RequiredCreateUserProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalCreateUserProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserProfileRequestRequestTypeDef",
    {
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "Tags": Sequence[TagTypeDef],
        "UserSettings": UserSettingsTypeDef,
    },
    total=False,
)


class CreateUserProfileRequestRequestTypeDef(
    _RequiredCreateUserProfileRequestRequestTypeDef, _OptionalCreateUserProfileRequestRequestTypeDef
):
    pass


_RequiredUpdateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalUpdateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainRequestRequestTypeDef",
    {
        "DefaultUserSettings": UserSettingsTypeDef,
        "DomainSettingsForUpdate": DomainSettingsForUpdateTypeDef,
        "DefaultSpaceSettings": DefaultSpaceSettingsTypeDef,
        "AppSecurityGroupManagement": AppSecurityGroupManagementType,
    },
    total=False,
)


class UpdateDomainRequestRequestTypeDef(
    _RequiredUpdateDomainRequestRequestTypeDef, _OptionalUpdateDomainRequestRequestTypeDef
):
    pass


_RequiredUpdateUserProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalUpdateUserProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserProfileRequestRequestTypeDef",
    {
        "UserSettings": UserSettingsTypeDef,
    },
    total=False,
)


class UpdateUserProfileRequestRequestTypeDef(
    _RequiredUpdateUserProfileRequestRequestTypeDef, _OptionalUpdateUserProfileRequestRequestTypeDef
):
    pass


_RequiredHyperParameterTrainingJobDefinitionOutputTypeDef = TypedDict(
    "_RequiredHyperParameterTrainingJobDefinitionOutputTypeDef",
    {
        "AlgorithmSpecification": HyperParameterAlgorithmSpecificationOutputTypeDef,
        "RoleArn": str,
        "OutputDataConfig": OutputDataConfigOutputTypeDef,
        "StoppingCondition": StoppingConditionOutputTypeDef,
    },
)
_OptionalHyperParameterTrainingJobDefinitionOutputTypeDef = TypedDict(
    "_OptionalHyperParameterTrainingJobDefinitionOutputTypeDef",
    {
        "DefinitionName": str,
        "TuningObjective": HyperParameterTuningJobObjectiveOutputTypeDef,
        "HyperParameterRanges": ParameterRangesOutputTypeDef,
        "StaticHyperParameters": Dict[str, str],
        "InputDataConfig": List[ChannelOutputTypeDef],
        "VpcConfig": VpcConfigOutputTypeDef,
        "ResourceConfig": ResourceConfigOutputTypeDef,
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": CheckpointConfigOutputTypeDef,
        "RetryStrategy": RetryStrategyOutputTypeDef,
        "HyperParameterTuningResourceConfig": HyperParameterTuningResourceConfigOutputTypeDef,
        "Environment": Dict[str, str],
    },
    total=False,
)


class HyperParameterTrainingJobDefinitionOutputTypeDef(
    _RequiredHyperParameterTrainingJobDefinitionOutputTypeDef,
    _OptionalHyperParameterTrainingJobDefinitionOutputTypeDef,
):
    pass


_RequiredTrainingJobDefinitionOutputTypeDef = TypedDict(
    "_RequiredTrainingJobDefinitionOutputTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
        "InputDataConfig": List[ChannelOutputTypeDef],
        "OutputDataConfig": OutputDataConfigOutputTypeDef,
        "ResourceConfig": ResourceConfigOutputTypeDef,
        "StoppingCondition": StoppingConditionOutputTypeDef,
    },
)
_OptionalTrainingJobDefinitionOutputTypeDef = TypedDict(
    "_OptionalTrainingJobDefinitionOutputTypeDef",
    {
        "HyperParameters": Dict[str, str],
    },
    total=False,
)


class TrainingJobDefinitionOutputTypeDef(
    _RequiredTrainingJobDefinitionOutputTypeDef, _OptionalTrainingJobDefinitionOutputTypeDef
):
    pass


_RequiredHyperParameterTrainingJobDefinitionTypeDef = TypedDict(
    "_RequiredHyperParameterTrainingJobDefinitionTypeDef",
    {
        "AlgorithmSpecification": HyperParameterAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "StoppingCondition": StoppingConditionTypeDef,
    },
)
_OptionalHyperParameterTrainingJobDefinitionTypeDef = TypedDict(
    "_OptionalHyperParameterTrainingJobDefinitionTypeDef",
    {
        "DefinitionName": str,
        "TuningObjective": HyperParameterTuningJobObjectiveTypeDef,
        "HyperParameterRanges": ParameterRangesTypeDef,
        "StaticHyperParameters": Mapping[str, str],
        "InputDataConfig": Sequence[ChannelTypeDef],
        "VpcConfig": VpcConfigTypeDef,
        "ResourceConfig": ResourceConfigTypeDef,
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": CheckpointConfigTypeDef,
        "RetryStrategy": RetryStrategyTypeDef,
        "HyperParameterTuningResourceConfig": HyperParameterTuningResourceConfigTypeDef,
        "Environment": Mapping[str, str],
    },
    total=False,
)


class HyperParameterTrainingJobDefinitionTypeDef(
    _RequiredHyperParameterTrainingJobDefinitionTypeDef,
    _OptionalHyperParameterTrainingJobDefinitionTypeDef,
):
    pass


_RequiredTrainingJobDefinitionTypeDef = TypedDict(
    "_RequiredTrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
        "InputDataConfig": Sequence[ChannelTypeDef],
        "OutputDataConfig": OutputDataConfigTypeDef,
        "ResourceConfig": ResourceConfigTypeDef,
        "StoppingCondition": StoppingConditionTypeDef,
    },
)
_OptionalTrainingJobDefinitionTypeDef = TypedDict(
    "_OptionalTrainingJobDefinitionTypeDef",
    {
        "HyperParameters": Mapping[str, str],
    },
    total=False,
)


class TrainingJobDefinitionTypeDef(
    _RequiredTrainingJobDefinitionTypeDef, _OptionalTrainingJobDefinitionTypeDef
):
    pass


DescribeSpaceResponseTypeDef = TypedDict(
    "DescribeSpaceResponseTypeDef",
    {
        "DomainId": str,
        "SpaceArn": str,
        "SpaceName": str,
        "HomeEfsFileSystemUid": str,
        "Status": SpaceStatusType,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "SpaceSettings": SpaceSettingsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "HomeEfsFileSystemId": str,
        "SingleSignOnManagedApplicationInstanceId": str,
        "Status": DomainStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "AuthMode": AuthModeType,
        "DefaultUserSettings": UserSettingsOutputTypeDef,
        "AppNetworkAccessType": AppNetworkAccessTypeType,
        "HomeEfsFileSystemKmsKeyId": str,
        "SubnetIds": List[str],
        "Url": str,
        "VpcId": str,
        "KmsKeyId": str,
        "DomainSettings": DomainSettingsOutputTypeDef,
        "AppSecurityGroupManagement": AppSecurityGroupManagementType,
        "SecurityGroupIdForDomainBoundary": str,
        "DefaultSpaceSettings": DefaultSpaceSettingsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeUserProfileResponseTypeDef = TypedDict(
    "DescribeUserProfileResponseTypeDef",
    {
        "DomainId": str,
        "UserProfileArn": str,
        "UserProfileName": str,
        "HomeEfsFileSystemUid": str,
        "Status": UserProfileStatusType,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "UserSettings": UserSettingsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredInferenceRecommendationsJobStepTypeDef = TypedDict(
    "_RequiredInferenceRecommendationsJobStepTypeDef",
    {
        "StepType": Literal["BENCHMARK"],
        "JobName": str,
        "Status": RecommendationJobStatusType,
    },
)
_OptionalInferenceRecommendationsJobStepTypeDef = TypedDict(
    "_OptionalInferenceRecommendationsJobStepTypeDef",
    {
        "InferenceBenchmark": RecommendationJobInferenceBenchmarkTypeDef,
    },
    total=False,
)


class InferenceRecommendationsJobStepTypeDef(
    _RequiredInferenceRecommendationsJobStepTypeDef, _OptionalInferenceRecommendationsJobStepTypeDef
):
    pass


ListAssociationsResponseTypeDef = TypedDict(
    "ListAssociationsResponseTypeDef",
    {
        "AssociationSummaries": List[AssociationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TrialTypeDef = TypedDict(
    "TrialTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": TrialSourceTypeDef,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "MetadataProperties": MetadataPropertiesOutputTypeDef,
        "Tags": List[TagOutputTypeDef],
        "TrialComponentSummaries": List[TrialComponentSimpleSummaryTypeDef],
    },
    total=False,
)

ListTrialComponentsResponseTypeDef = TypedDict(
    "ListTrialComponentsResponseTypeDef",
    {
        "TrialComponentSummaries": List[TrialComponentSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredTrainingSpecificationOutputTypeDef = TypedDict(
    "_RequiredTrainingSpecificationOutputTypeDef",
    {
        "TrainingImage": str,
        "SupportedTrainingInstanceTypes": List[TrainingInstanceTypeType],
        "TrainingChannels": List[ChannelSpecificationOutputTypeDef],
    },
)
_OptionalTrainingSpecificationOutputTypeDef = TypedDict(
    "_OptionalTrainingSpecificationOutputTypeDef",
    {
        "TrainingImageDigest": str,
        "SupportedHyperParameters": List[HyperParameterSpecificationOutputTypeDef],
        "SupportsDistributedTraining": bool,
        "MetricDefinitions": List[MetricDefinitionOutputTypeDef],
        "SupportedTuningJobObjectiveMetrics": List[HyperParameterTuningJobObjectiveOutputTypeDef],
    },
    total=False,
)


class TrainingSpecificationOutputTypeDef(
    _RequiredTrainingSpecificationOutputTypeDef, _OptionalTrainingSpecificationOutputTypeDef
):
    pass


_RequiredTrainingSpecificationTypeDef = TypedDict(
    "_RequiredTrainingSpecificationTypeDef",
    {
        "TrainingImage": str,
        "SupportedTrainingInstanceTypes": Sequence[TrainingInstanceTypeType],
        "TrainingChannels": Sequence[ChannelSpecificationTypeDef],
    },
)
_OptionalTrainingSpecificationTypeDef = TypedDict(
    "_OptionalTrainingSpecificationTypeDef",
    {
        "TrainingImageDigest": str,
        "SupportedHyperParameters": Sequence[HyperParameterSpecificationTypeDef],
        "SupportsDistributedTraining": bool,
        "MetricDefinitions": Sequence[MetricDefinitionTypeDef],
        "SupportedTuningJobObjectiveMetrics": Sequence[HyperParameterTuningJobObjectiveTypeDef],
    },
    total=False,
)


class TrainingSpecificationTypeDef(
    _RequiredTrainingSpecificationTypeDef, _OptionalTrainingSpecificationTypeDef
):
    pass


ListAppImageConfigsResponseTypeDef = TypedDict(
    "ListAppImageConfigsResponseTypeDef",
    {
        "NextToken": str,
        "AppImageConfigs": List[AppImageConfigDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredLabelingJobSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": LabelingJobStatusType,
        "LabelCounters": LabelCountersTypeDef,
        "WorkteamArn": str,
        "PreHumanTaskLambdaArn": str,
    },
)
_OptionalLabelingJobSummaryTypeDef = TypedDict(
    "_OptionalLabelingJobSummaryTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
        "FailureReason": str,
        "LabelingJobOutput": LabelingJobOutputTypeDef,
        "InputConfig": LabelingJobInputConfigOutputTypeDef,
    },
    total=False,
)


class LabelingJobSummaryTypeDef(
    _RequiredLabelingJobSummaryTypeDef, _OptionalLabelingJobSummaryTypeDef
):
    pass


DescribeWorkteamResponseTypeDef = TypedDict(
    "DescribeWorkteamResponseTypeDef",
    {
        "Workteam": WorkteamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListWorkteamsResponseTypeDef = TypedDict(
    "ListWorkteamsResponseTypeDef",
    {
        "Workteams": List[WorkteamTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateWorkteamResponseTypeDef = TypedDict(
    "UpdateWorkteamResponseTypeDef",
    {
        "Workteam": WorkteamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListMonitoringAlertsResponseTypeDef = TypedDict(
    "ListMonitoringAlertsResponseTypeDef",
    {
        "MonitoringAlertSummaries": List[MonitoringAlertSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeModelOutputTypeDef = TypedDict(
    "DescribeModelOutputTypeDef",
    {
        "ModelName": str,
        "PrimaryContainer": ContainerDefinitionOutputTypeDef,
        "Containers": List[ContainerDefinitionOutputTypeDef],
        "InferenceExecutionConfig": InferenceExecutionConfigOutputTypeDef,
        "ExecutionRoleArn": str,
        "VpcConfig": VpcConfigOutputTypeDef,
        "CreationTime": datetime,
        "ModelArn": str,
        "EnableNetworkIsolation": bool,
        "DeploymentRecommendation": DeploymentRecommendationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "ModelName": str,
        "PrimaryContainer": ContainerDefinitionOutputTypeDef,
        "Containers": List[ContainerDefinitionOutputTypeDef],
        "InferenceExecutionConfig": InferenceExecutionConfigOutputTypeDef,
        "ExecutionRoleArn": str,
        "VpcConfig": VpcConfigOutputTypeDef,
        "CreationTime": datetime,
        "ModelArn": str,
        "EnableNetworkIsolation": bool,
        "Tags": List[TagOutputTypeDef],
        "DeploymentRecommendation": DeploymentRecommendationTypeDef,
    },
    total=False,
)

_RequiredCreateModelInputRequestTypeDef = TypedDict(
    "_RequiredCreateModelInputRequestTypeDef",
    {
        "ModelName": str,
        "ExecutionRoleArn": str,
    },
)
_OptionalCreateModelInputRequestTypeDef = TypedDict(
    "_OptionalCreateModelInputRequestTypeDef",
    {
        "PrimaryContainer": ContainerDefinitionTypeDef,
        "Containers": Sequence[ContainerDefinitionTypeDef],
        "InferenceExecutionConfig": InferenceExecutionConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
        "VpcConfig": VpcConfigTypeDef,
        "EnableNetworkIsolation": bool,
    },
    total=False,
)


class CreateModelInputRequestTypeDef(
    _RequiredCreateModelInputRequestTypeDef, _OptionalCreateModelInputRequestTypeDef
):
    pass


DescribeInferenceExperimentResponseTypeDef = TypedDict(
    "DescribeInferenceExperimentResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": Literal["ShadowMode"],
        "Schedule": InferenceExperimentScheduleOutputTypeDef,
        "Status": InferenceExperimentStatusType,
        "StatusReason": str,
        "Description": str,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "EndpointMetadata": EndpointMetadataTypeDef,
        "ModelVariants": List[ModelVariantConfigSummaryTypeDef],
        "DataStorageConfig": InferenceExperimentDataStorageConfigOutputTypeDef,
        "ShadowModeConfig": ShadowModeConfigOutputTypeDef,
        "KmsKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
        "Type": Literal["ShadowMode"],
        "RoleArn": str,
        "EndpointName": str,
        "ModelVariants": Sequence[ModelVariantConfigTypeDef],
        "ShadowModeConfig": ShadowModeConfigTypeDef,
    },
)
_OptionalCreateInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInferenceExperimentRequestRequestTypeDef",
    {
        "Schedule": InferenceExperimentScheduleTypeDef,
        "Description": str,
        "DataStorageConfig": InferenceExperimentDataStorageConfigTypeDef,
        "KmsKey": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateInferenceExperimentRequestRequestTypeDef(
    _RequiredCreateInferenceExperimentRequestRequestTypeDef,
    _OptionalCreateInferenceExperimentRequestRequestTypeDef,
):
    pass


_RequiredStopInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredStopInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
        "ModelVariantActions": Mapping[str, ModelVariantActionType],
    },
)
_OptionalStopInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalStopInferenceExperimentRequestRequestTypeDef",
    {
        "DesiredModelVariants": Sequence[ModelVariantConfigTypeDef],
        "DesiredState": InferenceExperimentStopDesiredStateType,
        "Reason": str,
    },
    total=False,
)


class StopInferenceExperimentRequestRequestTypeDef(
    _RequiredStopInferenceExperimentRequestRequestTypeDef,
    _OptionalStopInferenceExperimentRequestRequestTypeDef,
):
    pass


_RequiredUpdateInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInferenceExperimentRequestRequestTypeDef",
    {
        "Schedule": InferenceExperimentScheduleTypeDef,
        "Description": str,
        "ModelVariants": Sequence[ModelVariantConfigTypeDef],
        "DataStorageConfig": InferenceExperimentDataStorageConfigTypeDef,
        "ShadowModeConfig": ShadowModeConfigTypeDef,
    },
    total=False,
)


class UpdateInferenceExperimentRequestRequestTypeDef(
    _RequiredUpdateInferenceExperimentRequestRequestTypeDef,
    _OptionalUpdateInferenceExperimentRequestRequestTypeDef,
):
    pass


_RequiredBatchDescribeModelPackageSummaryTypeDef = TypedDict(
    "_RequiredBatchDescribeModelPackageSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "InferenceSpecification": InferenceSpecificationOutputTypeDef,
        "ModelPackageStatus": ModelPackageStatusType,
    },
)
_OptionalBatchDescribeModelPackageSummaryTypeDef = TypedDict(
    "_OptionalBatchDescribeModelPackageSummaryTypeDef",
    {
        "ModelPackageVersion": int,
        "ModelPackageDescription": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
    },
    total=False,
)


class BatchDescribeModelPackageSummaryTypeDef(
    _RequiredBatchDescribeModelPackageSummaryTypeDef,
    _OptionalBatchDescribeModelPackageSummaryTypeDef,
):
    pass


_RequiredUpdateModelPackageInputRequestTypeDef = TypedDict(
    "_RequiredUpdateModelPackageInputRequestTypeDef",
    {
        "ModelPackageArn": str,
    },
)
_OptionalUpdateModelPackageInputRequestTypeDef = TypedDict(
    "_OptionalUpdateModelPackageInputRequestTypeDef",
    {
        "ModelApprovalStatus": ModelApprovalStatusType,
        "ApprovalDescription": str,
        "CustomerMetadataProperties": Mapping[str, str],
        "CustomerMetadataPropertiesToRemove": Sequence[str],
        "AdditionalInferenceSpecificationsToAdd": Sequence[
            AdditionalInferenceSpecificationDefinitionTypeDef
        ],
    },
    total=False,
)


class UpdateModelPackageInputRequestTypeDef(
    _RequiredUpdateModelPackageInputRequestTypeDef, _OptionalUpdateModelPackageInputRequestTypeDef
):
    pass


DataQualityJobInputOutputTypeDef = TypedDict(
    "DataQualityJobInputOutputTypeDef",
    {
        "EndpointInput": EndpointInputOutputTypeDef,
        "BatchTransformInput": BatchTransformInputOutputTypeDef,
    },
    total=False,
)

_RequiredModelBiasJobInputOutputTypeDef = TypedDict(
    "_RequiredModelBiasJobInputOutputTypeDef",
    {
        "GroundTruthS3Input": MonitoringGroundTruthS3InputOutputTypeDef,
    },
)
_OptionalModelBiasJobInputOutputTypeDef = TypedDict(
    "_OptionalModelBiasJobInputOutputTypeDef",
    {
        "EndpointInput": EndpointInputOutputTypeDef,
        "BatchTransformInput": BatchTransformInputOutputTypeDef,
    },
    total=False,
)


class ModelBiasJobInputOutputTypeDef(
    _RequiredModelBiasJobInputOutputTypeDef, _OptionalModelBiasJobInputOutputTypeDef
):
    pass


ModelExplainabilityJobInputOutputTypeDef = TypedDict(
    "ModelExplainabilityJobInputOutputTypeDef",
    {
        "EndpointInput": EndpointInputOutputTypeDef,
        "BatchTransformInput": BatchTransformInputOutputTypeDef,
    },
    total=False,
)

_RequiredModelQualityJobInputOutputTypeDef = TypedDict(
    "_RequiredModelQualityJobInputOutputTypeDef",
    {
        "GroundTruthS3Input": MonitoringGroundTruthS3InputOutputTypeDef,
    },
)
_OptionalModelQualityJobInputOutputTypeDef = TypedDict(
    "_OptionalModelQualityJobInputOutputTypeDef",
    {
        "EndpointInput": EndpointInputOutputTypeDef,
        "BatchTransformInput": BatchTransformInputOutputTypeDef,
    },
    total=False,
)


class ModelQualityJobInputOutputTypeDef(
    _RequiredModelQualityJobInputOutputTypeDef, _OptionalModelQualityJobInputOutputTypeDef
):
    pass


MonitoringInputOutputTypeDef = TypedDict(
    "MonitoringInputOutputTypeDef",
    {
        "EndpointInput": EndpointInputOutputTypeDef,
        "BatchTransformInput": BatchTransformInputOutputTypeDef,
    },
    total=False,
)

DataQualityJobInputTypeDef = TypedDict(
    "DataQualityJobInputTypeDef",
    {
        "EndpointInput": EndpointInputTypeDef,
        "BatchTransformInput": BatchTransformInputTypeDef,
    },
    total=False,
)

_RequiredModelBiasJobInputTypeDef = TypedDict(
    "_RequiredModelBiasJobInputTypeDef",
    {
        "GroundTruthS3Input": MonitoringGroundTruthS3InputTypeDef,
    },
)
_OptionalModelBiasJobInputTypeDef = TypedDict(
    "_OptionalModelBiasJobInputTypeDef",
    {
        "EndpointInput": EndpointInputTypeDef,
        "BatchTransformInput": BatchTransformInputTypeDef,
    },
    total=False,
)


class ModelBiasJobInputTypeDef(
    _RequiredModelBiasJobInputTypeDef, _OptionalModelBiasJobInputTypeDef
):
    pass


ModelExplainabilityJobInputTypeDef = TypedDict(
    "ModelExplainabilityJobInputTypeDef",
    {
        "EndpointInput": EndpointInputTypeDef,
        "BatchTransformInput": BatchTransformInputTypeDef,
    },
    total=False,
)

_RequiredModelQualityJobInputTypeDef = TypedDict(
    "_RequiredModelQualityJobInputTypeDef",
    {
        "GroundTruthS3Input": MonitoringGroundTruthS3InputTypeDef,
    },
)
_OptionalModelQualityJobInputTypeDef = TypedDict(
    "_OptionalModelQualityJobInputTypeDef",
    {
        "EndpointInput": EndpointInputTypeDef,
        "BatchTransformInput": BatchTransformInputTypeDef,
    },
    total=False,
)


class ModelQualityJobInputTypeDef(
    _RequiredModelQualityJobInputTypeDef, _OptionalModelQualityJobInputTypeDef
):
    pass


MonitoringInputTypeDef = TypedDict(
    "MonitoringInputTypeDef",
    {
        "EndpointInput": EndpointInputTypeDef,
        "BatchTransformInput": BatchTransformInputTypeDef,
    },
    total=False,
)

DescribeProcessingJobResponseTypeDef = TypedDict(
    "DescribeProcessingJobResponseTypeDef",
    {
        "ProcessingInputs": List[ProcessingInputOutputTypeDef],
        "ProcessingOutputConfig": ProcessingOutputConfigOutputTypeDef,
        "ProcessingJobName": str,
        "ProcessingResources": ProcessingResourcesOutputTypeDef,
        "StoppingCondition": ProcessingStoppingConditionOutputTypeDef,
        "AppSpecification": AppSpecificationOutputTypeDef,
        "Environment": Dict[str, str],
        "NetworkConfig": NetworkConfigOutputTypeDef,
        "RoleArn": str,
        "ExperimentConfig": ExperimentConfigOutputTypeDef,
        "ProcessingJobArn": str,
        "ProcessingJobStatus": ProcessingJobStatusType,
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ProcessingJobTypeDef = TypedDict(
    "ProcessingJobTypeDef",
    {
        "ProcessingInputs": List[ProcessingInputOutputTypeDef],
        "ProcessingOutputConfig": ProcessingOutputConfigOutputTypeDef,
        "ProcessingJobName": str,
        "ProcessingResources": ProcessingResourcesOutputTypeDef,
        "StoppingCondition": ProcessingStoppingConditionOutputTypeDef,
        "AppSpecification": AppSpecificationOutputTypeDef,
        "Environment": Dict[str, str],
        "NetworkConfig": NetworkConfigOutputTypeDef,
        "RoleArn": str,
        "ExperimentConfig": ExperimentConfigOutputTypeDef,
        "ProcessingJobArn": str,
        "ProcessingJobStatus": ProcessingJobStatusType,
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

_RequiredCreateProcessingJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingResources": ProcessingResourcesTypeDef,
        "AppSpecification": AppSpecificationTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateProcessingJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProcessingJobRequestRequestTypeDef",
    {
        "ProcessingInputs": Sequence[ProcessingInputTypeDef],
        "ProcessingOutputConfig": ProcessingOutputConfigTypeDef,
        "StoppingCondition": ProcessingStoppingConditionTypeDef,
        "Environment": Mapping[str, str],
        "NetworkConfig": NetworkConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
        "ExperimentConfig": ExperimentConfigTypeDef,
    },
    total=False,
)


class CreateProcessingJobRequestRequestTypeDef(
    _RequiredCreateProcessingJobRequestRequestTypeDef,
    _OptionalCreateProcessingJobRequestRequestTypeDef,
):
    pass


DescribeFlowDefinitionResponseTypeDef = TypedDict(
    "DescribeFlowDefinitionResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "FlowDefinitionName": str,
        "FlowDefinitionStatus": FlowDefinitionStatusType,
        "CreationTime": datetime,
        "HumanLoopRequestSource": HumanLoopRequestSourceOutputTypeDef,
        "HumanLoopActivationConfig": HumanLoopActivationConfigOutputTypeDef,
        "HumanLoopConfig": HumanLoopConfigOutputTypeDef,
        "OutputConfig": FlowDefinitionOutputConfigOutputTypeDef,
        "RoleArn": str,
        "FailureReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeLabelingJobResponseTypeDef = TypedDict(
    "DescribeLabelingJobResponseTypeDef",
    {
        "LabelingJobStatus": LabelingJobStatusType,
        "LabelCounters": LabelCountersTypeDef,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "JobReferenceCode": str,
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "LabelAttributeName": str,
        "InputConfig": LabelingJobInputConfigOutputTypeDef,
        "OutputConfig": LabelingJobOutputConfigOutputTypeDef,
        "RoleArn": str,
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": LabelingJobStoppingConditionsOutputTypeDef,
        "LabelingJobAlgorithmsConfig": LabelingJobAlgorithmsConfigOutputTypeDef,
        "HumanTaskConfig": HumanTaskConfigOutputTypeDef,
        "Tags": List[TagOutputTypeDef],
        "LabelingJobOutput": LabelingJobOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateFlowDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
        "HumanLoopConfig": HumanLoopConfigTypeDef,
        "OutputConfig": FlowDefinitionOutputConfigTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateFlowDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFlowDefinitionRequestRequestTypeDef",
    {
        "HumanLoopRequestSource": HumanLoopRequestSourceTypeDef,
        "HumanLoopActivationConfig": HumanLoopActivationConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateFlowDefinitionRequestRequestTypeDef(
    _RequiredCreateFlowDefinitionRequestRequestTypeDef,
    _OptionalCreateFlowDefinitionRequestRequestTypeDef,
):
    pass


_RequiredCreateLabelingJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
        "LabelAttributeName": str,
        "InputConfig": LabelingJobInputConfigTypeDef,
        "OutputConfig": LabelingJobOutputConfigTypeDef,
        "RoleArn": str,
        "HumanTaskConfig": HumanTaskConfigTypeDef,
    },
)
_OptionalCreateLabelingJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLabelingJobRequestRequestTypeDef",
    {
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": LabelingJobStoppingConditionsTypeDef,
        "LabelingJobAlgorithmsConfig": LabelingJobAlgorithmsConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateLabelingJobRequestRequestTypeDef(
    _RequiredCreateLabelingJobRequestRequestTypeDef, _OptionalCreateLabelingJobRequestRequestTypeDef
):
    pass


DescribeTrainingJobResponseTypeDef = TypedDict(
    "DescribeTrainingJobResponseTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": ModelArtifactsTypeDef,
        "TrainingJobStatus": TrainingJobStatusType,
        "SecondaryStatus": SecondaryStatusType,
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": AlgorithmSpecificationOutputTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[ChannelOutputTypeDef],
        "OutputDataConfig": OutputDataConfigOutputTypeDef,
        "ResourceConfig": ResourceConfigOutputTypeDef,
        "VpcConfig": VpcConfigOutputTypeDef,
        "StoppingCondition": StoppingConditionOutputTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[SecondaryStatusTransitionTypeDef],
        "FinalMetricDataList": List[MetricDataTypeDef],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": CheckpointConfigOutputTypeDef,
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": DebugHookConfigOutputTypeDef,
        "ExperimentConfig": ExperimentConfigOutputTypeDef,
        "DebugRuleConfigurations": List[DebugRuleConfigurationOutputTypeDef],
        "TensorBoardOutputConfig": TensorBoardOutputConfigOutputTypeDef,
        "DebugRuleEvaluationStatuses": List[DebugRuleEvaluationStatusTypeDef],
        "ProfilerConfig": ProfilerConfigOutputTypeDef,
        "ProfilerRuleConfigurations": List[ProfilerRuleConfigurationOutputTypeDef],
        "ProfilerRuleEvaluationStatuses": List[ProfilerRuleEvaluationStatusTypeDef],
        "ProfilingStatus": ProfilingStatusType,
        "RetryStrategy": RetryStrategyOutputTypeDef,
        "Environment": Dict[str, str],
        "WarmPoolStatus": WarmPoolStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TrainingJobTypeDef = TypedDict(
    "TrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": ModelArtifactsTypeDef,
        "TrainingJobStatus": TrainingJobStatusType,
        "SecondaryStatus": SecondaryStatusType,
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": AlgorithmSpecificationOutputTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[ChannelOutputTypeDef],
        "OutputDataConfig": OutputDataConfigOutputTypeDef,
        "ResourceConfig": ResourceConfigOutputTypeDef,
        "VpcConfig": VpcConfigOutputTypeDef,
        "StoppingCondition": StoppingConditionOutputTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[SecondaryStatusTransitionTypeDef],
        "FinalMetricDataList": List[MetricDataTypeDef],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": CheckpointConfigOutputTypeDef,
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": DebugHookConfigOutputTypeDef,
        "ExperimentConfig": ExperimentConfigOutputTypeDef,
        "DebugRuleConfigurations": List[DebugRuleConfigurationOutputTypeDef],
        "TensorBoardOutputConfig": TensorBoardOutputConfigOutputTypeDef,
        "DebugRuleEvaluationStatuses": List[DebugRuleEvaluationStatusTypeDef],
        "ProfilerConfig": ProfilerConfigOutputTypeDef,
        "Environment": Dict[str, str],
        "RetryStrategy": RetryStrategyOutputTypeDef,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

_RequiredCreateTrainingJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
        "AlgorithmSpecification": AlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "ResourceConfig": ResourceConfigTypeDef,
        "StoppingCondition": StoppingConditionTypeDef,
    },
)
_OptionalCreateTrainingJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrainingJobRequestRequestTypeDef",
    {
        "HyperParameters": Mapping[str, str],
        "InputDataConfig": Sequence[ChannelTypeDef],
        "VpcConfig": VpcConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": CheckpointConfigTypeDef,
        "DebugHookConfig": DebugHookConfigTypeDef,
        "DebugRuleConfigurations": Sequence[DebugRuleConfigurationTypeDef],
        "TensorBoardOutputConfig": TensorBoardOutputConfigTypeDef,
        "ExperimentConfig": ExperimentConfigTypeDef,
        "ProfilerConfig": ProfilerConfigTypeDef,
        "ProfilerRuleConfigurations": Sequence[ProfilerRuleConfigurationTypeDef],
        "Environment": Mapping[str, str],
        "RetryStrategy": RetryStrategyTypeDef,
    },
    total=False,
)


class CreateTrainingJobRequestRequestTypeDef(
    _RequiredCreateTrainingJobRequestRequestTypeDef, _OptionalCreateTrainingJobRequestRequestTypeDef
):
    pass


DescribeTransformJobResponseTypeDef = TypedDict(
    "DescribeTransformJobResponseTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": TransformJobStatusType,
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": ModelClientConfigOutputTypeDef,
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "TransformInput": TransformInputOutputTypeDef,
        "TransformOutput": TransformOutputTypeDef,
        "DataCaptureConfig": BatchDataCaptureConfigOutputTypeDef,
        "TransformResources": TransformResourcesOutputTypeDef,
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": DataProcessingOutputTypeDef,
        "ExperimentConfig": ExperimentConfigOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredTransformJobDefinitionOutputTypeDef = TypedDict(
    "_RequiredTransformJobDefinitionOutputTypeDef",
    {
        "TransformInput": TransformInputOutputTypeDef,
        "TransformOutput": TransformOutputTypeDef,
        "TransformResources": TransformResourcesOutputTypeDef,
    },
)
_OptionalTransformJobDefinitionOutputTypeDef = TypedDict(
    "_OptionalTransformJobDefinitionOutputTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
    },
    total=False,
)


class TransformJobDefinitionOutputTypeDef(
    _RequiredTransformJobDefinitionOutputTypeDef, _OptionalTransformJobDefinitionOutputTypeDef
):
    pass


TransformJobTypeDef = TypedDict(
    "TransformJobTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": TransformJobStatusType,
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": ModelClientConfigOutputTypeDef,
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "TransformInput": TransformInputOutputTypeDef,
        "TransformOutput": TransformOutputTypeDef,
        "TransformResources": TransformResourcesOutputTypeDef,
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": DataProcessingOutputTypeDef,
        "ExperimentConfig": ExperimentConfigOutputTypeDef,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

_RequiredCreateTransformJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
        "ModelName": str,
        "TransformInput": TransformInputTypeDef,
        "TransformOutput": TransformOutputTypeDef,
        "TransformResources": TransformResourcesTypeDef,
    },
)
_OptionalCreateTransformJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransformJobRequestRequestTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": ModelClientConfigTypeDef,
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Mapping[str, str],
        "DataCaptureConfig": BatchDataCaptureConfigTypeDef,
        "DataProcessing": DataProcessingTypeDef,
        "Tags": Sequence[TagTypeDef],
        "ExperimentConfig": ExperimentConfigTypeDef,
    },
    total=False,
)


class CreateTransformJobRequestRequestTypeDef(
    _RequiredCreateTransformJobRequestRequestTypeDef,
    _OptionalCreateTransformJobRequestRequestTypeDef,
):
    pass


_RequiredTransformJobDefinitionTypeDef = TypedDict(
    "_RequiredTransformJobDefinitionTypeDef",
    {
        "TransformInput": TransformInputTypeDef,
        "TransformOutput": TransformOutputTypeDef,
        "TransformResources": TransformResourcesTypeDef,
    },
)
_OptionalTransformJobDefinitionTypeDef = TypedDict(
    "_OptionalTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Mapping[str, str],
    },
    total=False,
)


class TransformJobDefinitionTypeDef(
    _RequiredTransformJobDefinitionTypeDef, _OptionalTransformJobDefinitionTypeDef
):
    pass


DescribeAutoMLJobV2ResponseTypeDef = TypedDict(
    "DescribeAutoMLJobV2ResponseTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobInputDataConfig": List[AutoMLJobChannelOutputTypeDef],
        "OutputDataConfig": AutoMLOutputDataConfigOutputTypeDef,
        "RoleArn": str,
        "AutoMLJobObjective": AutoMLJobObjectiveOutputTypeDef,
        "AutoMLProblemTypeConfig": AutoMLProblemTypeConfigOutputTypeDef,
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List[AutoMLPartialFailureReasonTypeDef],
        "BestCandidate": AutoMLCandidateTypeDef,
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "ModelDeployConfig": ModelDeployConfigOutputTypeDef,
        "ModelDeployResult": ModelDeployResultTypeDef,
        "DataSplitConfig": AutoMLDataSplitConfigOutputTypeDef,
        "SecurityConfig": AutoMLSecurityConfigOutputTypeDef,
        "AutoMLJobArtifacts": AutoMLJobArtifactsTypeDef,
        "ResolvedAttributes": AutoMLResolvedAttributesTypeDef,
        "AutoMLProblemTypeConfigName": AutoMLProblemTypeConfigNameType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateAutoMLJobV2RequestRequestTypeDef = TypedDict(
    "_RequiredCreateAutoMLJobV2RequestRequestTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobInputDataConfig": Sequence[AutoMLJobChannelTypeDef],
        "OutputDataConfig": AutoMLOutputDataConfigTypeDef,
        "AutoMLProblemTypeConfig": AutoMLProblemTypeConfigTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateAutoMLJobV2RequestRequestTypeDef = TypedDict(
    "_OptionalCreateAutoMLJobV2RequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
        "SecurityConfig": AutoMLSecurityConfigTypeDef,
        "AutoMLJobObjective": AutoMLJobObjectiveTypeDef,
        "ModelDeployConfig": ModelDeployConfigTypeDef,
        "DataSplitConfig": AutoMLDataSplitConfigTypeDef,
    },
    total=False,
)


class CreateAutoMLJobV2RequestRequestTypeDef(
    _RequiredCreateAutoMLJobV2RequestRequestTypeDef, _OptionalCreateAutoMLJobV2RequestRequestTypeDef
):
    pass


ListPipelineExecutionStepsResponseTypeDef = TypedDict(
    "ListPipelineExecutionStepsResponseTypeDef",
    {
        "PipelineExecutionSteps": List[PipelineExecutionStepTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateEndpointInputRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "EndpointConfigName": str,
    },
)
_OptionalCreateEndpointInputRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointInputRequestTypeDef",
    {
        "DeploymentConfig": DeploymentConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateEndpointInputRequestTypeDef(
    _RequiredCreateEndpointInputRequestTypeDef, _OptionalCreateEndpointInputRequestTypeDef
):
    pass


_RequiredUpdateEndpointInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "EndpointConfigName": str,
    },
)
_OptionalUpdateEndpointInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEndpointInputRequestTypeDef",
    {
        "RetainAllVariantProperties": bool,
        "ExcludeRetainedVariantProperties": Sequence[VariantPropertyTypeDef],
        "DeploymentConfig": DeploymentConfigTypeDef,
        "RetainDeploymentConfig": bool,
    },
    total=False,
)


class UpdateEndpointInputRequestTypeDef(
    _RequiredUpdateEndpointInputRequestTypeDef, _OptionalUpdateEndpointInputRequestTypeDef
):
    pass


DescribeInferenceRecommendationsJobResponseTypeDef = TypedDict(
    "DescribeInferenceRecommendationsJobResponseTypeDef",
    {
        "JobName": str,
        "JobDescription": str,
        "JobType": RecommendationJobTypeType,
        "JobArn": str,
        "RoleArn": str,
        "Status": RecommendationJobStatusType,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "InputConfig": RecommendationJobInputConfigOutputTypeDef,
        "StoppingConditions": RecommendationJobStoppingConditionsOutputTypeDef,
        "InferenceRecommendations": List[InferenceRecommendationTypeDef],
        "EndpointPerformances": List[EndpointPerformanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
        "JobType": RecommendationJobTypeType,
        "RoleArn": str,
        "InputConfig": RecommendationJobInputConfigTypeDef,
    },
)
_OptionalCreateInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobDescription": str,
        "StoppingConditions": RecommendationJobStoppingConditionsTypeDef,
        "OutputConfig": RecommendationJobOutputConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateInferenceRecommendationsJobRequestRequestTypeDef(
    _RequiredCreateInferenceRecommendationsJobRequestRequestTypeDef,
    _OptionalCreateInferenceRecommendationsJobRequestRequestTypeDef,
):
    pass


DescribeEndpointConfigOutputTypeDef = TypedDict(
    "DescribeEndpointConfigOutputTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "ProductionVariants": List[ProductionVariantOutputTypeDef],
        "DataCaptureConfig": DataCaptureConfigOutputTypeDef,
        "KmsKeyId": str,
        "CreationTime": datetime,
        "AsyncInferenceConfig": AsyncInferenceConfigOutputTypeDef,
        "ExplainerConfig": ExplainerConfigOutputTypeDef,
        "ShadowProductionVariants": List[ProductionVariantOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeEndpointOutputTypeDef = TypedDict(
    "DescribeEndpointOutputTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "ProductionVariants": List[ProductionVariantSummaryTypeDef],
        "DataCaptureConfig": DataCaptureConfigSummaryTypeDef,
        "EndpointStatus": EndpointStatusType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastDeploymentConfig": DeploymentConfigOutputTypeDef,
        "AsyncInferenceConfig": AsyncInferenceConfigOutputTypeDef,
        "PendingDeploymentSummary": PendingDeploymentSummaryTypeDef,
        "ExplainerConfig": ExplainerConfigOutputTypeDef,
        "ShadowProductionVariants": List[ProductionVariantSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateEndpointConfigInputRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
        "ProductionVariants": Sequence[ProductionVariantTypeDef],
    },
)
_OptionalCreateEndpointConfigInputRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointConfigInputRequestTypeDef",
    {
        "DataCaptureConfig": DataCaptureConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
        "KmsKeyId": str,
        "AsyncInferenceConfig": AsyncInferenceConfigTypeDef,
        "ExplainerConfig": ExplainerConfigTypeDef,
        "ShadowProductionVariants": Sequence[ProductionVariantTypeDef],
    },
    total=False,
)


class CreateEndpointConfigInputRequestTypeDef(
    _RequiredCreateEndpointConfigInputRequestTypeDef,
    _OptionalCreateEndpointConfigInputRequestTypeDef,
):
    pass


DescribeHyperParameterTuningJobResponseTypeDef = TypedDict(
    "DescribeHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": HyperParameterTuningJobConfigOutputTypeDef,
        "TrainingJobDefinition": HyperParameterTrainingJobDefinitionOutputTypeDef,
        "TrainingJobDefinitions": List[HyperParameterTrainingJobDefinitionOutputTypeDef],
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": TrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ObjectiveStatusCountersTypeDef,
        "BestTrainingJob": HyperParameterTrainingJobSummaryTypeDef,
        "OverallBestTrainingJob": HyperParameterTrainingJobSummaryTypeDef,
        "WarmStartConfig": HyperParameterTuningJobWarmStartConfigOutputTypeDef,
        "FailureReason": str,
        "TuningJobCompletionDetails": HyperParameterTuningJobCompletionDetailsTypeDef,
        "ConsumedResources": HyperParameterTuningJobConsumedResourcesTypeDef,
        "Autotune": AutotuneOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

HyperParameterTuningJobSearchEntityTypeDef = TypedDict(
    "HyperParameterTuningJobSearchEntityTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": HyperParameterTuningJobConfigOutputTypeDef,
        "TrainingJobDefinition": HyperParameterTrainingJobDefinitionOutputTypeDef,
        "TrainingJobDefinitions": List[HyperParameterTrainingJobDefinitionOutputTypeDef],
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": TrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ObjectiveStatusCountersTypeDef,
        "BestTrainingJob": HyperParameterTrainingJobSummaryTypeDef,
        "OverallBestTrainingJob": HyperParameterTrainingJobSummaryTypeDef,
        "WarmStartConfig": HyperParameterTuningJobWarmStartConfigOutputTypeDef,
        "FailureReason": str,
        "Tags": List[TagOutputTypeDef],
        "TuningJobCompletionDetails": HyperParameterTuningJobCompletionDetailsTypeDef,
        "ConsumedResources": HyperParameterTuningJobConsumedResourcesTypeDef,
    },
    total=False,
)

_RequiredCreateHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobConfig": HyperParameterTuningJobConfigTypeDef,
    },
)
_OptionalCreateHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHyperParameterTuningJobRequestRequestTypeDef",
    {
        "TrainingJobDefinition": HyperParameterTrainingJobDefinitionTypeDef,
        "TrainingJobDefinitions": Sequence[HyperParameterTrainingJobDefinitionTypeDef],
        "WarmStartConfig": HyperParameterTuningJobWarmStartConfigTypeDef,
        "Tags": Sequence[TagTypeDef],
        "Autotune": AutotuneTypeDef,
    },
    total=False,
)


class CreateHyperParameterTuningJobRequestRequestTypeDef(
    _RequiredCreateHyperParameterTuningJobRequestRequestTypeDef,
    _OptionalCreateHyperParameterTuningJobRequestRequestTypeDef,
):
    pass


ListInferenceRecommendationsJobStepsResponseTypeDef = TypedDict(
    "ListInferenceRecommendationsJobStepsResponseTypeDef",
    {
        "Steps": List[InferenceRecommendationsJobStepTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLabelingJobsResponseTypeDef = TypedDict(
    "ListLabelingJobsResponseTypeDef",
    {
        "LabelingJobSummaryList": List[LabelingJobSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchDescribeModelPackageOutputTypeDef = TypedDict(
    "BatchDescribeModelPackageOutputTypeDef",
    {
        "ModelPackageSummaries": Dict[str, BatchDescribeModelPackageSummaryTypeDef],
        "BatchDescribeModelPackageErrorMap": Dict[str, BatchDescribeModelPackageErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDataQualityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeDataQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "DataQualityBaselineConfig": DataQualityBaselineConfigOutputTypeDef,
        "DataQualityAppSpecification": DataQualityAppSpecificationOutputTypeDef,
        "DataQualityJobInput": DataQualityJobInputOutputTypeDef,
        "DataQualityJobOutputConfig": MonitoringOutputConfigOutputTypeDef,
        "JobResources": MonitoringResourcesOutputTypeDef,
        "NetworkConfig": MonitoringNetworkConfigOutputTypeDef,
        "RoleArn": str,
        "StoppingCondition": MonitoringStoppingConditionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeModelBiasJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelBiasJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelBiasBaselineConfig": ModelBiasBaselineConfigOutputTypeDef,
        "ModelBiasAppSpecification": ModelBiasAppSpecificationOutputTypeDef,
        "ModelBiasJobInput": ModelBiasJobInputOutputTypeDef,
        "ModelBiasJobOutputConfig": MonitoringOutputConfigOutputTypeDef,
        "JobResources": MonitoringResourcesOutputTypeDef,
        "NetworkConfig": MonitoringNetworkConfigOutputTypeDef,
        "RoleArn": str,
        "StoppingCondition": MonitoringStoppingConditionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeModelExplainabilityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelExplainabilityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelExplainabilityBaselineConfig": ModelExplainabilityBaselineConfigOutputTypeDef,
        "ModelExplainabilityAppSpecification": ModelExplainabilityAppSpecificationOutputTypeDef,
        "ModelExplainabilityJobInput": ModelExplainabilityJobInputOutputTypeDef,
        "ModelExplainabilityJobOutputConfig": MonitoringOutputConfigOutputTypeDef,
        "JobResources": MonitoringResourcesOutputTypeDef,
        "NetworkConfig": MonitoringNetworkConfigOutputTypeDef,
        "RoleArn": str,
        "StoppingCondition": MonitoringStoppingConditionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeModelQualityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelQualityBaselineConfig": ModelQualityBaselineConfigOutputTypeDef,
        "ModelQualityAppSpecification": ModelQualityAppSpecificationOutputTypeDef,
        "ModelQualityJobInput": ModelQualityJobInputOutputTypeDef,
        "ModelQualityJobOutputConfig": MonitoringOutputConfigOutputTypeDef,
        "JobResources": MonitoringResourcesOutputTypeDef,
        "NetworkConfig": MonitoringNetworkConfigOutputTypeDef,
        "RoleArn": str,
        "StoppingCondition": MonitoringStoppingConditionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredMonitoringJobDefinitionOutputTypeDef = TypedDict(
    "_RequiredMonitoringJobDefinitionOutputTypeDef",
    {
        "MonitoringInputs": List[MonitoringInputOutputTypeDef],
        "MonitoringOutputConfig": MonitoringOutputConfigOutputTypeDef,
        "MonitoringResources": MonitoringResourcesOutputTypeDef,
        "MonitoringAppSpecification": MonitoringAppSpecificationOutputTypeDef,
        "RoleArn": str,
    },
)
_OptionalMonitoringJobDefinitionOutputTypeDef = TypedDict(
    "_OptionalMonitoringJobDefinitionOutputTypeDef",
    {
        "BaselineConfig": MonitoringBaselineConfigOutputTypeDef,
        "StoppingCondition": MonitoringStoppingConditionOutputTypeDef,
        "Environment": Dict[str, str],
        "NetworkConfig": NetworkConfigOutputTypeDef,
    },
    total=False,
)


class MonitoringJobDefinitionOutputTypeDef(
    _RequiredMonitoringJobDefinitionOutputTypeDef, _OptionalMonitoringJobDefinitionOutputTypeDef
):
    pass


_RequiredCreateDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "DataQualityAppSpecification": DataQualityAppSpecificationTypeDef,
        "DataQualityJobInput": DataQualityJobInputTypeDef,
        "DataQualityJobOutputConfig": MonitoringOutputConfigTypeDef,
        "JobResources": MonitoringResourcesTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "DataQualityBaselineConfig": DataQualityBaselineConfigTypeDef,
        "NetworkConfig": MonitoringNetworkConfigTypeDef,
        "StoppingCondition": MonitoringStoppingConditionTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateDataQualityJobDefinitionRequestRequestTypeDef(
    _RequiredCreateDataQualityJobDefinitionRequestRequestTypeDef,
    _OptionalCreateDataQualityJobDefinitionRequestRequestTypeDef,
):
    pass


_RequiredCreateModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelBiasAppSpecification": ModelBiasAppSpecificationTypeDef,
        "ModelBiasJobInput": ModelBiasJobInputTypeDef,
        "ModelBiasJobOutputConfig": MonitoringOutputConfigTypeDef,
        "JobResources": MonitoringResourcesTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "ModelBiasBaselineConfig": ModelBiasBaselineConfigTypeDef,
        "NetworkConfig": MonitoringNetworkConfigTypeDef,
        "StoppingCondition": MonitoringStoppingConditionTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateModelBiasJobDefinitionRequestRequestTypeDef(
    _RequiredCreateModelBiasJobDefinitionRequestRequestTypeDef,
    _OptionalCreateModelBiasJobDefinitionRequestRequestTypeDef,
):
    pass


_RequiredCreateModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelExplainabilityAppSpecification": ModelExplainabilityAppSpecificationTypeDef,
        "ModelExplainabilityJobInput": ModelExplainabilityJobInputTypeDef,
        "ModelExplainabilityJobOutputConfig": MonitoringOutputConfigTypeDef,
        "JobResources": MonitoringResourcesTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "ModelExplainabilityBaselineConfig": ModelExplainabilityBaselineConfigTypeDef,
        "NetworkConfig": MonitoringNetworkConfigTypeDef,
        "StoppingCondition": MonitoringStoppingConditionTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateModelExplainabilityJobDefinitionRequestRequestTypeDef(
    _RequiredCreateModelExplainabilityJobDefinitionRequestRequestTypeDef,
    _OptionalCreateModelExplainabilityJobDefinitionRequestRequestTypeDef,
):
    pass


_RequiredCreateModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelQualityAppSpecification": ModelQualityAppSpecificationTypeDef,
        "ModelQualityJobInput": ModelQualityJobInputTypeDef,
        "ModelQualityJobOutputConfig": MonitoringOutputConfigTypeDef,
        "JobResources": MonitoringResourcesTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "ModelQualityBaselineConfig": ModelQualityBaselineConfigTypeDef,
        "NetworkConfig": MonitoringNetworkConfigTypeDef,
        "StoppingCondition": MonitoringStoppingConditionTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateModelQualityJobDefinitionRequestRequestTypeDef(
    _RequiredCreateModelQualityJobDefinitionRequestRequestTypeDef,
    _OptionalCreateModelQualityJobDefinitionRequestRequestTypeDef,
):
    pass


_RequiredMonitoringJobDefinitionTypeDef = TypedDict(
    "_RequiredMonitoringJobDefinitionTypeDef",
    {
        "MonitoringInputs": Sequence[MonitoringInputTypeDef],
        "MonitoringOutputConfig": MonitoringOutputConfigTypeDef,
        "MonitoringResources": MonitoringResourcesTypeDef,
        "MonitoringAppSpecification": MonitoringAppSpecificationTypeDef,
        "RoleArn": str,
    },
)
_OptionalMonitoringJobDefinitionTypeDef = TypedDict(
    "_OptionalMonitoringJobDefinitionTypeDef",
    {
        "BaselineConfig": MonitoringBaselineConfigTypeDef,
        "StoppingCondition": MonitoringStoppingConditionTypeDef,
        "Environment": Mapping[str, str],
        "NetworkConfig": NetworkConfigTypeDef,
    },
    total=False,
)


class MonitoringJobDefinitionTypeDef(
    _RequiredMonitoringJobDefinitionTypeDef, _OptionalMonitoringJobDefinitionTypeDef
):
    pass


_RequiredAlgorithmValidationProfileOutputTypeDef = TypedDict(
    "_RequiredAlgorithmValidationProfileOutputTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": TrainingJobDefinitionOutputTypeDef,
    },
)
_OptionalAlgorithmValidationProfileOutputTypeDef = TypedDict(
    "_OptionalAlgorithmValidationProfileOutputTypeDef",
    {
        "TransformJobDefinition": TransformJobDefinitionOutputTypeDef,
    },
    total=False,
)


class AlgorithmValidationProfileOutputTypeDef(
    _RequiredAlgorithmValidationProfileOutputTypeDef,
    _OptionalAlgorithmValidationProfileOutputTypeDef,
):
    pass


ModelPackageValidationProfileOutputTypeDef = TypedDict(
    "ModelPackageValidationProfileOutputTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": TransformJobDefinitionOutputTypeDef,
    },
)

TrialComponentSourceDetailTypeDef = TypedDict(
    "TrialComponentSourceDetailTypeDef",
    {
        "SourceArn": str,
        "TrainingJob": TrainingJobTypeDef,
        "ProcessingJob": ProcessingJobTypeDef,
        "TransformJob": TransformJobTypeDef,
    },
    total=False,
)

_RequiredAlgorithmValidationProfileTypeDef = TypedDict(
    "_RequiredAlgorithmValidationProfileTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": TrainingJobDefinitionTypeDef,
    },
)
_OptionalAlgorithmValidationProfileTypeDef = TypedDict(
    "_OptionalAlgorithmValidationProfileTypeDef",
    {
        "TransformJobDefinition": TransformJobDefinitionTypeDef,
    },
    total=False,
)


class AlgorithmValidationProfileTypeDef(
    _RequiredAlgorithmValidationProfileTypeDef, _OptionalAlgorithmValidationProfileTypeDef
):
    pass


ModelPackageValidationProfileTypeDef = TypedDict(
    "ModelPackageValidationProfileTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": TransformJobDefinitionTypeDef,
    },
)

MonitoringScheduleConfigOutputTypeDef = TypedDict(
    "MonitoringScheduleConfigOutputTypeDef",
    {
        "ScheduleConfig": ScheduleConfigOutputTypeDef,
        "MonitoringJobDefinition": MonitoringJobDefinitionOutputTypeDef,
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)

MonitoringScheduleConfigTypeDef = TypedDict(
    "MonitoringScheduleConfigTypeDef",
    {
        "ScheduleConfig": ScheduleConfigTypeDef,
        "MonitoringJobDefinition": MonitoringJobDefinitionTypeDef,
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)

AlgorithmValidationSpecificationOutputTypeDef = TypedDict(
    "AlgorithmValidationSpecificationOutputTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List[AlgorithmValidationProfileOutputTypeDef],
    },
)

ModelPackageValidationSpecificationOutputTypeDef = TypedDict(
    "ModelPackageValidationSpecificationOutputTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List[ModelPackageValidationProfileOutputTypeDef],
    },
)

TrialComponentTypeDef = TypedDict(
    "TrialComponentTypeDef",
    {
        "TrialComponentName": str,
        "DisplayName": str,
        "TrialComponentArn": str,
        "Source": TrialComponentSourceTypeDef,
        "Status": TrialComponentStatusOutputTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "Parameters": Dict[str, TrialComponentParameterValueOutputTypeDef],
        "InputArtifacts": Dict[str, TrialComponentArtifactOutputTypeDef],
        "OutputArtifacts": Dict[str, TrialComponentArtifactOutputTypeDef],
        "Metrics": List[TrialComponentMetricSummaryTypeDef],
        "MetadataProperties": MetadataPropertiesOutputTypeDef,
        "SourceDetail": TrialComponentSourceDetailTypeDef,
        "LineageGroupArn": str,
        "Tags": List[TagOutputTypeDef],
        "Parents": List[ParentTypeDef],
        "RunName": str,
    },
    total=False,
)

AlgorithmValidationSpecificationTypeDef = TypedDict(
    "AlgorithmValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": Sequence[AlgorithmValidationProfileTypeDef],
    },
)

ModelPackageValidationSpecificationTypeDef = TypedDict(
    "ModelPackageValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": Sequence[ModelPackageValidationProfileTypeDef],
    },
)

DescribeMonitoringScheduleResponseTypeDef = TypedDict(
    "DescribeMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": MonitoringScheduleConfigOutputTypeDef,
        "EndpointName": str,
        "LastMonitoringExecutionSummary": MonitoringExecutionSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ModelDashboardMonitoringScheduleTypeDef = TypedDict(
    "ModelDashboardMonitoringScheduleTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": MonitoringScheduleConfigOutputTypeDef,
        "EndpointName": str,
        "MonitoringAlertSummaries": List[MonitoringAlertSummaryTypeDef],
        "LastMonitoringExecutionSummary": MonitoringExecutionSummaryTypeDef,
    },
    total=False,
)

MonitoringScheduleTypeDef = TypedDict(
    "MonitoringScheduleTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": MonitoringScheduleConfigOutputTypeDef,
        "EndpointName": str,
        "LastMonitoringExecutionSummary": MonitoringExecutionSummaryTypeDef,
        "Tags": List[TagOutputTypeDef],
    },
    total=False,
)

_RequiredCreateMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleConfig": MonitoringScheduleConfigTypeDef,
    },
)
_OptionalCreateMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMonitoringScheduleRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateMonitoringScheduleRequestRequestTypeDef(
    _RequiredCreateMonitoringScheduleRequestRequestTypeDef,
    _OptionalCreateMonitoringScheduleRequestRequestTypeDef,
):
    pass


UpdateMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "UpdateMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleConfig": MonitoringScheduleConfigTypeDef,
    },
)

DescribeAlgorithmOutputTypeDef = TypedDict(
    "DescribeAlgorithmOutputTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "TrainingSpecification": TrainingSpecificationOutputTypeDef,
        "InferenceSpecification": InferenceSpecificationOutputTypeDef,
        "ValidationSpecification": AlgorithmValidationSpecificationOutputTypeDef,
        "AlgorithmStatus": AlgorithmStatusType,
        "AlgorithmStatusDetails": AlgorithmStatusDetailsTypeDef,
        "ProductId": str,
        "CertifyForMarketplace": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeModelPackageOutputTypeDef = TypedDict(
    "DescribeModelPackageOutputTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": InferenceSpecificationOutputTypeDef,
        "SourceAlgorithmSpecification": SourceAlgorithmSpecificationOutputTypeDef,
        "ValidationSpecification": ModelPackageValidationSpecificationOutputTypeDef,
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageStatusDetails": ModelPackageStatusDetailsTypeDef,
        "CertifyForMarketplace": bool,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "CreatedBy": UserContextTypeDef,
        "MetadataProperties": MetadataPropertiesOutputTypeDef,
        "ModelMetrics": ModelMetricsOutputTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "ApprovalDescription": str,
        "CustomerMetadataProperties": Dict[str, str],
        "DriftCheckBaselines": DriftCheckBaselinesOutputTypeDef,
        "Domain": str,
        "Task": str,
        "SamplePayloadUrl": str,
        "AdditionalInferenceSpecifications": List[
            AdditionalInferenceSpecificationDefinitionOutputTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ModelPackageTypeDef = TypedDict(
    "ModelPackageTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": InferenceSpecificationOutputTypeDef,
        "SourceAlgorithmSpecification": SourceAlgorithmSpecificationOutputTypeDef,
        "ValidationSpecification": ModelPackageValidationSpecificationOutputTypeDef,
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageStatusDetails": ModelPackageStatusDetailsTypeDef,
        "CertifyForMarketplace": bool,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "CreatedBy": UserContextTypeDef,
        "MetadataProperties": MetadataPropertiesOutputTypeDef,
        "ModelMetrics": ModelMetricsOutputTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "ApprovalDescription": str,
        "Domain": str,
        "Task": str,
        "SamplePayloadUrl": str,
        "AdditionalInferenceSpecifications": List[
            AdditionalInferenceSpecificationDefinitionOutputTypeDef
        ],
        "Tags": List[TagOutputTypeDef],
        "CustomerMetadataProperties": Dict[str, str],
        "DriftCheckBaselines": DriftCheckBaselinesOutputTypeDef,
    },
    total=False,
)

_RequiredCreateAlgorithmInputRequestTypeDef = TypedDict(
    "_RequiredCreateAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
        "TrainingSpecification": TrainingSpecificationTypeDef,
    },
)
_OptionalCreateAlgorithmInputRequestTypeDef = TypedDict(
    "_OptionalCreateAlgorithmInputRequestTypeDef",
    {
        "AlgorithmDescription": str,
        "InferenceSpecification": InferenceSpecificationTypeDef,
        "ValidationSpecification": AlgorithmValidationSpecificationTypeDef,
        "CertifyForMarketplace": bool,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateAlgorithmInputRequestTypeDef(
    _RequiredCreateAlgorithmInputRequestTypeDef, _OptionalCreateAlgorithmInputRequestTypeDef
):
    pass


CreateModelPackageInputRequestTypeDef = TypedDict(
    "CreateModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageDescription": str,
        "InferenceSpecification": InferenceSpecificationTypeDef,
        "ValidationSpecification": ModelPackageValidationSpecificationTypeDef,
        "SourceAlgorithmSpecification": SourceAlgorithmSpecificationTypeDef,
        "CertifyForMarketplace": bool,
        "Tags": Sequence[TagTypeDef],
        "ModelApprovalStatus": ModelApprovalStatusType,
        "MetadataProperties": MetadataPropertiesTypeDef,
        "ModelMetrics": ModelMetricsTypeDef,
        "ClientToken": str,
        "CustomerMetadataProperties": Mapping[str, str],
        "DriftCheckBaselines": DriftCheckBaselinesTypeDef,
        "Domain": str,
        "Task": str,
        "SamplePayloadUrl": str,
        "AdditionalInferenceSpecifications": Sequence[
            AdditionalInferenceSpecificationDefinitionTypeDef
        ],
    },
    total=False,
)

ModelDashboardModelTypeDef = TypedDict(
    "ModelDashboardModelTypeDef",
    {
        "Model": ModelTypeDef,
        "Endpoints": List[ModelDashboardEndpointTypeDef],
        "LastBatchTransformJob": TransformJobTypeDef,
        "MonitoringSchedules": List[ModelDashboardMonitoringScheduleTypeDef],
        "ModelCard": ModelDashboardModelCardTypeDef,
    },
    total=False,
)

_RequiredEndpointTypeDef = TypedDict(
    "_RequiredEndpointTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "EndpointStatus": EndpointStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalEndpointTypeDef = TypedDict(
    "_OptionalEndpointTypeDef",
    {
        "ProductionVariants": List[ProductionVariantSummaryTypeDef],
        "DataCaptureConfig": DataCaptureConfigSummaryTypeDef,
        "FailureReason": str,
        "MonitoringSchedules": List[MonitoringScheduleTypeDef],
        "Tags": List[TagOutputTypeDef],
        "ShadowProductionVariants": List[ProductionVariantSummaryTypeDef],
    },
    total=False,
)


class EndpointTypeDef(_RequiredEndpointTypeDef, _OptionalEndpointTypeDef):
    pass


SearchRecordTypeDef = TypedDict(
    "SearchRecordTypeDef",
    {
        "TrainingJob": TrainingJobTypeDef,
        "Experiment": ExperimentTypeDef,
        "Trial": TrialTypeDef,
        "TrialComponent": TrialComponentTypeDef,
        "Endpoint": EndpointTypeDef,
        "ModelPackage": ModelPackageTypeDef,
        "ModelPackageGroup": ModelPackageGroupTypeDef,
        "Pipeline": PipelineTypeDef,
        "PipelineExecution": PipelineExecutionTypeDef,
        "FeatureGroup": FeatureGroupTypeDef,
        "Project": ProjectTypeDef,
        "FeatureMetadata": FeatureMetadataTypeDef,
        "HyperParameterTuningJob": HyperParameterTuningJobSearchEntityTypeDef,
        "Model": ModelDashboardModelTypeDef,
        "ModelCard": ModelCardTypeDef,
    },
    total=False,
)

SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef",
    {
        "Results": List[SearchRecordTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
