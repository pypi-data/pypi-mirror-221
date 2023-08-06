"""
Type annotations for databrew service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/type_defs/)

Usage::

    ```python
    from mypy_boto3_databrew.type_defs import AllowedStatisticsOutputTypeDef

    data: AllowedStatisticsOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AnalyticsModeType,
    CompressionFormatType,
    EncryptionModeType,
    InputFormatType,
    JobRunStateType,
    JobTypeType,
    LogSubscriptionType,
    OrderType,
    OutputFormatType,
    ParameterTypeType,
    SampleModeType,
    SampleTypeType,
    SessionStatusType,
    SourceType,
    ThresholdTypeType,
    ThresholdUnitType,
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
    "AllowedStatisticsOutputTypeDef",
    "AllowedStatisticsTypeDef",
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ColumnSelectorOutputTypeDef",
    "ColumnSelectorTypeDef",
    "ConditionExpressionOutputTypeDef",
    "ConditionExpressionTypeDef",
    "CreateDatasetResponseTypeDef",
    "JobSampleTypeDef",
    "S3LocationTypeDef",
    "ValidationConfigurationTypeDef",
    "CreateProfileJobResponseTypeDef",
    "SampleTypeDef",
    "CreateProjectResponseTypeDef",
    "RecipeReferenceTypeDef",
    "CreateRecipeJobResponseTypeDef",
    "CreateRecipeResponseTypeDef",
    "CreateRulesetResponseTypeDef",
    "CreateScheduleRequestRequestTypeDef",
    "CreateScheduleResponseTypeDef",
    "CsvOptionsOutputTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsOutputTypeDef",
    "CsvOutputOptionsTypeDef",
    "S3LocationOutputTypeDef",
    "DatetimeOptionsOutputTypeDef",
    "FilterExpressionOutputTypeDef",
    "DatetimeOptionsTypeDef",
    "FilterExpressionTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteRecipeVersionRequestRequestTypeDef",
    "DeleteRecipeVersionResponseTypeDef",
    "DeleteRulesetRequestRequestTypeDef",
    "DeleteRulesetResponseTypeDef",
    "DeleteScheduleRequestRequestTypeDef",
    "DeleteScheduleResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "JobSampleOutputTypeDef",
    "RecipeReferenceOutputTypeDef",
    "ValidationConfigurationOutputTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "SampleOutputTypeDef",
    "DescribeRecipeRequestRequestTypeDef",
    "DescribeRulesetRequestRequestTypeDef",
    "DescribeScheduleRequestRequestTypeDef",
    "DescribeScheduleResponseTypeDef",
    "ExcelOptionsOutputTypeDef",
    "ExcelOptionsTypeDef",
    "FilesLimitOutputTypeDef",
    "FilesLimitTypeDef",
    "JsonOptionsOutputTypeDef",
    "JsonOptionsTypeDef",
    "MetadataOutputTypeDef",
    "MetadataTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef",
    "ListRecipeVersionsRequestRequestTypeDef",
    "ListRecipesRequestListRecipesPaginateTypeDef",
    "ListRecipesRequestRequestTypeDef",
    "ListRulesetsRequestListRulesetsPaginateTypeDef",
    "ListRulesetsRequestRequestTypeDef",
    "RulesetItemTypeDef",
    "ListSchedulesRequestListSchedulesPaginateTypeDef",
    "ListSchedulesRequestRequestTypeDef",
    "ScheduleTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublishRecipeRequestRequestTypeDef",
    "PublishRecipeResponseTypeDef",
    "RecipeActionOutputTypeDef",
    "RecipeActionTypeDef",
    "ResponseMetadataTypeDef",
    "ThresholdOutputTypeDef",
    "ThresholdTypeDef",
    "ViewFrameTypeDef",
    "SendProjectSessionActionResponseTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StartProjectSessionRequestRequestTypeDef",
    "StartProjectSessionResponseTypeDef",
    "StatisticOverrideOutputTypeDef",
    "StatisticOverrideTypeDef",
    "StopJobRunRequestRequestTypeDef",
    "StopJobRunResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateProfileJobResponseTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateRecipeJobResponseTypeDef",
    "UpdateRecipeResponseTypeDef",
    "UpdateRulesetResponseTypeDef",
    "UpdateScheduleRequestRequestTypeDef",
    "UpdateScheduleResponseTypeDef",
    "EntityDetectorConfigurationOutputTypeDef",
    "EntityDetectorConfigurationTypeDef",
    "BatchDeleteRecipeVersionResponseTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatabaseTableOutputOptionsTypeDef",
    "S3TableOutputOptionsTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "OutputFormatOptionsOutputTypeDef",
    "OutputFormatOptionsTypeDef",
    "DataCatalogInputDefinitionOutputTypeDef",
    "DatabaseInputDefinitionOutputTypeDef",
    "DatabaseTableOutputOptionsOutputTypeDef",
    "S3TableOutputOptionsOutputTypeDef",
    "DatasetParameterOutputTypeDef",
    "DatasetParameterTypeDef",
    "DescribeProjectResponseTypeDef",
    "ProjectTypeDef",
    "FormatOptionsOutputTypeDef",
    "FormatOptionsTypeDef",
    "ListRulesetsResponseTypeDef",
    "ListSchedulesResponseTypeDef",
    "RecipeStepOutputTypeDef",
    "RecipeStepTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "StatisticsConfigurationOutputTypeDef",
    "StatisticsConfigurationTypeDef",
    "InputTypeDef",
    "DatabaseOutputTypeDef",
    "DataCatalogOutputTypeDef",
    "OutputTypeDef",
    "InputOutputTypeDef",
    "PathOptionsOutputTypeDef",
    "PathOptionsTypeDef",
    "ListProjectsResponseTypeDef",
    "DescribeRecipeResponseTypeDef",
    "RecipeTypeDef",
    "CreateRecipeRequestRequestTypeDef",
    "SendProjectSessionActionRequestRequestTypeDef",
    "UpdateRecipeRequestRequestTypeDef",
    "DescribeRulesetResponseTypeDef",
    "CreateRulesetRequestRequestTypeDef",
    "UpdateRulesetRequestRequestTypeDef",
    "ColumnStatisticsConfigurationOutputTypeDef",
    "ColumnStatisticsConfigurationTypeDef",
    "CreateRecipeJobRequestRequestTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "UpdateRecipeJobRequestRequestTypeDef",
    "DatasetTypeDef",
    "DescribeDatasetResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "ListRecipeVersionsResponseTypeDef",
    "ListRecipesResponseTypeDef",
    "ProfileConfigurationOutputTypeDef",
    "ProfileConfigurationTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "CreateProfileJobRequestRequestTypeDef",
    "UpdateProfileJobRequestRequestTypeDef",
)

AllowedStatisticsOutputTypeDef = TypedDict(
    "AllowedStatisticsOutputTypeDef",
    {
        "Statistics": List[str],
    },
)

AllowedStatisticsTypeDef = TypedDict(
    "AllowedStatisticsTypeDef",
    {
        "Statistics": Sequence[str],
    },
)

BatchDeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersions": Sequence[str],
    },
)

RecipeVersionErrorDetailTypeDef = TypedDict(
    "RecipeVersionErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "RecipeVersion": str,
    },
    total=False,
)

ColumnSelectorOutputTypeDef = TypedDict(
    "ColumnSelectorOutputTypeDef",
    {
        "Regex": str,
        "Name": str,
    },
    total=False,
)

ColumnSelectorTypeDef = TypedDict(
    "ColumnSelectorTypeDef",
    {
        "Regex": str,
        "Name": str,
    },
    total=False,
)

_RequiredConditionExpressionOutputTypeDef = TypedDict(
    "_RequiredConditionExpressionOutputTypeDef",
    {
        "Condition": str,
        "TargetColumn": str,
    },
)
_OptionalConditionExpressionOutputTypeDef = TypedDict(
    "_OptionalConditionExpressionOutputTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class ConditionExpressionOutputTypeDef(
    _RequiredConditionExpressionOutputTypeDef, _OptionalConditionExpressionOutputTypeDef
):
    pass


_RequiredConditionExpressionTypeDef = TypedDict(
    "_RequiredConditionExpressionTypeDef",
    {
        "Condition": str,
        "TargetColumn": str,
    },
)
_OptionalConditionExpressionTypeDef = TypedDict(
    "_OptionalConditionExpressionTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class ConditionExpressionTypeDef(
    _RequiredConditionExpressionTypeDef, _OptionalConditionExpressionTypeDef
):
    pass


CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobSampleTypeDef = TypedDict(
    "JobSampleTypeDef",
    {
        "Mode": SampleModeType,
        "Size": int,
    },
    total=False,
)

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Key": str,
        "BucketOwner": str,
    },
    total=False,
)


class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass


_RequiredValidationConfigurationTypeDef = TypedDict(
    "_RequiredValidationConfigurationTypeDef",
    {
        "RulesetArn": str,
    },
)
_OptionalValidationConfigurationTypeDef = TypedDict(
    "_OptionalValidationConfigurationTypeDef",
    {
        "ValidationMode": Literal["CHECK_ALL"],
    },
    total=False,
)


class ValidationConfigurationTypeDef(
    _RequiredValidationConfigurationTypeDef, _OptionalValidationConfigurationTypeDef
):
    pass


CreateProfileJobResponseTypeDef = TypedDict(
    "CreateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSampleTypeDef = TypedDict(
    "_RequiredSampleTypeDef",
    {
        "Type": SampleTypeType,
    },
)
_OptionalSampleTypeDef = TypedDict(
    "_OptionalSampleTypeDef",
    {
        "Size": int,
    },
    total=False,
)


class SampleTypeDef(_RequiredSampleTypeDef, _OptionalSampleTypeDef):
    pass


CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecipeReferenceTypeDef = TypedDict(
    "_RequiredRecipeReferenceTypeDef",
    {
        "Name": str,
    },
)
_OptionalRecipeReferenceTypeDef = TypedDict(
    "_OptionalRecipeReferenceTypeDef",
    {
        "RecipeVersion": str,
    },
    total=False,
)


class RecipeReferenceTypeDef(_RequiredRecipeReferenceTypeDef, _OptionalRecipeReferenceTypeDef):
    pass


CreateRecipeJobResponseTypeDef = TypedDict(
    "CreateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecipeResponseTypeDef = TypedDict(
    "CreateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRulesetResponseTypeDef = TypedDict(
    "CreateRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
    },
)
_OptionalCreateScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateScheduleRequestRequestTypeDef",
    {
        "JobNames": Sequence[str],
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateScheduleRequestRequestTypeDef(
    _RequiredCreateScheduleRequestRequestTypeDef, _OptionalCreateScheduleRequestRequestTypeDef
):
    pass


CreateScheduleResponseTypeDef = TypedDict(
    "CreateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvOptionsOutputTypeDef = TypedDict(
    "CsvOptionsOutputTypeDef",
    {
        "Delimiter": str,
        "HeaderRow": bool,
    },
    total=False,
)

CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": str,
        "HeaderRow": bool,
    },
    total=False,
)

CsvOutputOptionsOutputTypeDef = TypedDict(
    "CsvOutputOptionsOutputTypeDef",
    {
        "Delimiter": str,
    },
    total=False,
)

CsvOutputOptionsTypeDef = TypedDict(
    "CsvOutputOptionsTypeDef",
    {
        "Delimiter": str,
    },
    total=False,
)

_RequiredS3LocationOutputTypeDef = TypedDict(
    "_RequiredS3LocationOutputTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalS3LocationOutputTypeDef = TypedDict(
    "_OptionalS3LocationOutputTypeDef",
    {
        "Key": str,
        "BucketOwner": str,
    },
    total=False,
)


class S3LocationOutputTypeDef(_RequiredS3LocationOutputTypeDef, _OptionalS3LocationOutputTypeDef):
    pass


_RequiredDatetimeOptionsOutputTypeDef = TypedDict(
    "_RequiredDatetimeOptionsOutputTypeDef",
    {
        "Format": str,
    },
)
_OptionalDatetimeOptionsOutputTypeDef = TypedDict(
    "_OptionalDatetimeOptionsOutputTypeDef",
    {
        "TimezoneOffset": str,
        "LocaleCode": str,
    },
    total=False,
)


class DatetimeOptionsOutputTypeDef(
    _RequiredDatetimeOptionsOutputTypeDef, _OptionalDatetimeOptionsOutputTypeDef
):
    pass


FilterExpressionOutputTypeDef = TypedDict(
    "FilterExpressionOutputTypeDef",
    {
        "Expression": str,
        "ValuesMap": Dict[str, str],
    },
)

_RequiredDatetimeOptionsTypeDef = TypedDict(
    "_RequiredDatetimeOptionsTypeDef",
    {
        "Format": str,
    },
)
_OptionalDatetimeOptionsTypeDef = TypedDict(
    "_OptionalDatetimeOptionsTypeDef",
    {
        "TimezoneOffset": str,
        "LocaleCode": str,
    },
    total=False,
)


class DatetimeOptionsTypeDef(_RequiredDatetimeOptionsTypeDef, _OptionalDatetimeOptionsTypeDef):
    pass


FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "Expression": str,
        "ValuesMap": Mapping[str, str],
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteJobResponseTypeDef = TypedDict(
    "DeleteJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "DeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
    },
)

DeleteRecipeVersionResponseTypeDef = TypedDict(
    "DeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRulesetRequestRequestTypeDef = TypedDict(
    "DeleteRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteRulesetResponseTypeDef = TypedDict(
    "DeleteRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteScheduleRequestRequestTypeDef = TypedDict(
    "DeleteScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteScheduleResponseTypeDef = TypedDict(
    "DeleteScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)

JobSampleOutputTypeDef = TypedDict(
    "JobSampleOutputTypeDef",
    {
        "Mode": SampleModeType,
        "Size": int,
    },
    total=False,
)

_RequiredRecipeReferenceOutputTypeDef = TypedDict(
    "_RequiredRecipeReferenceOutputTypeDef",
    {
        "Name": str,
    },
)
_OptionalRecipeReferenceOutputTypeDef = TypedDict(
    "_OptionalRecipeReferenceOutputTypeDef",
    {
        "RecipeVersion": str,
    },
    total=False,
)


class RecipeReferenceOutputTypeDef(
    _RequiredRecipeReferenceOutputTypeDef, _OptionalRecipeReferenceOutputTypeDef
):
    pass


_RequiredValidationConfigurationOutputTypeDef = TypedDict(
    "_RequiredValidationConfigurationOutputTypeDef",
    {
        "RulesetArn": str,
    },
)
_OptionalValidationConfigurationOutputTypeDef = TypedDict(
    "_OptionalValidationConfigurationOutputTypeDef",
    {
        "ValidationMode": Literal["CHECK_ALL"],
    },
    total=False,
)


class ValidationConfigurationOutputTypeDef(
    _RequiredValidationConfigurationOutputTypeDef, _OptionalValidationConfigurationOutputTypeDef
):
    pass


DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredSampleOutputTypeDef = TypedDict(
    "_RequiredSampleOutputTypeDef",
    {
        "Type": SampleTypeType,
    },
)
_OptionalSampleOutputTypeDef = TypedDict(
    "_OptionalSampleOutputTypeDef",
    {
        "Size": int,
    },
    total=False,
)


class SampleOutputTypeDef(_RequiredSampleOutputTypeDef, _OptionalSampleOutputTypeDef):
    pass


_RequiredDescribeRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRecipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRecipeRequestRequestTypeDef",
    {
        "RecipeVersion": str,
    },
    total=False,
)


class DescribeRecipeRequestRequestTypeDef(
    _RequiredDescribeRecipeRequestRequestTypeDef, _OptionalDescribeRecipeRequestRequestTypeDef
):
    pass


DescribeRulesetRequestRequestTypeDef = TypedDict(
    "DescribeRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeScheduleRequestRequestTypeDef = TypedDict(
    "DescribeScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeScheduleResponseTypeDef = TypedDict(
    "DescribeScheduleResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExcelOptionsOutputTypeDef = TypedDict(
    "ExcelOptionsOutputTypeDef",
    {
        "SheetNames": List[str],
        "SheetIndexes": List[int],
        "HeaderRow": bool,
    },
    total=False,
)

ExcelOptionsTypeDef = TypedDict(
    "ExcelOptionsTypeDef",
    {
        "SheetNames": Sequence[str],
        "SheetIndexes": Sequence[int],
        "HeaderRow": bool,
    },
    total=False,
)

_RequiredFilesLimitOutputTypeDef = TypedDict(
    "_RequiredFilesLimitOutputTypeDef",
    {
        "MaxFiles": int,
    },
)
_OptionalFilesLimitOutputTypeDef = TypedDict(
    "_OptionalFilesLimitOutputTypeDef",
    {
        "OrderedBy": Literal["LAST_MODIFIED_DATE"],
        "Order": OrderType,
    },
    total=False,
)


class FilesLimitOutputTypeDef(_RequiredFilesLimitOutputTypeDef, _OptionalFilesLimitOutputTypeDef):
    pass


_RequiredFilesLimitTypeDef = TypedDict(
    "_RequiredFilesLimitTypeDef",
    {
        "MaxFiles": int,
    },
)
_OptionalFilesLimitTypeDef = TypedDict(
    "_OptionalFilesLimitTypeDef",
    {
        "OrderedBy": Literal["LAST_MODIFIED_DATE"],
        "Order": OrderType,
    },
    total=False,
)


class FilesLimitTypeDef(_RequiredFilesLimitTypeDef, _OptionalFilesLimitTypeDef):
    pass


JsonOptionsOutputTypeDef = TypedDict(
    "JsonOptionsOutputTypeDef",
    {
        "MultiLine": bool,
    },
    total=False,
)

JsonOptionsTypeDef = TypedDict(
    "JsonOptionsTypeDef",
    {
        "MultiLine": bool,
    },
    total=False,
)

MetadataOutputTypeDef = TypedDict(
    "MetadataOutputTypeDef",
    {
        "SourceArn": str,
    },
    total=False,
)

MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "SourceArn": str,
    },
    total=False,
)

ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "_RequiredListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "Name": str,
    },
)
_OptionalListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "_OptionalListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListJobRunsRequestListJobRunsPaginateTypeDef(
    _RequiredListJobRunsRequestListJobRunsPaginateTypeDef,
    _OptionalListJobRunsRequestListJobRunsPaginateTypeDef,
):
    pass


_RequiredListJobRunsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobRunsRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListJobRunsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobRunsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListJobRunsRequestRequestTypeDef(
    _RequiredListJobRunsRequestRequestTypeDef, _OptionalListJobRunsRequestRequestTypeDef
):
    pass


ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "DatasetName": str,
        "ProjectName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "DatasetName": str,
        "MaxResults": int,
        "NextToken": str,
        "ProjectName": str,
    },
    total=False,
)

ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef = TypedDict(
    "_RequiredListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef",
    {
        "Name": str,
    },
)
_OptionalListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef = TypedDict(
    "_OptionalListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef(
    _RequiredListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef,
    _OptionalListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef,
):
    pass


_RequiredListRecipeVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListRecipeVersionsRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListRecipeVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListRecipeVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListRecipeVersionsRequestRequestTypeDef(
    _RequiredListRecipeVersionsRequestRequestTypeDef,
    _OptionalListRecipeVersionsRequestRequestTypeDef,
):
    pass


ListRecipesRequestListRecipesPaginateTypeDef = TypedDict(
    "ListRecipesRequestListRecipesPaginateTypeDef",
    {
        "RecipeVersion": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "RecipeVersion": str,
    },
    total=False,
)

ListRulesetsRequestListRulesetsPaginateTypeDef = TypedDict(
    "ListRulesetsRequestListRulesetsPaginateTypeDef",
    {
        "TargetArn": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListRulesetsRequestRequestTypeDef = TypedDict(
    "ListRulesetsRequestRequestTypeDef",
    {
        "TargetArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredRulesetItemTypeDef = TypedDict(
    "_RequiredRulesetItemTypeDef",
    {
        "Name": str,
        "TargetArn": str,
    },
)
_OptionalRulesetItemTypeDef = TypedDict(
    "_OptionalRulesetItemTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "Description": str,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "RuleCount": int,
        "Tags": Dict[str, str],
    },
    total=False,
)


class RulesetItemTypeDef(_RequiredRulesetItemTypeDef, _OptionalRulesetItemTypeDef):
    pass


ListSchedulesRequestListSchedulesPaginateTypeDef = TypedDict(
    "ListSchedulesRequestListSchedulesPaginateTypeDef",
    {
        "JobName": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSchedulesRequestRequestTypeDef = TypedDict(
    "ListSchedulesRequestRequestTypeDef",
    {
        "JobName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredScheduleTypeDef = TypedDict(
    "_RequiredScheduleTypeDef",
    {
        "Name": str,
    },
)
_OptionalScheduleTypeDef = TypedDict(
    "_OptionalScheduleTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ScheduleTypeDef(_RequiredScheduleTypeDef, _OptionalScheduleTypeDef):
    pass


ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
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

_RequiredPublishRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredPublishRecipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalPublishRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalPublishRecipeRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class PublishRecipeRequestRequestTypeDef(
    _RequiredPublishRecipeRequestRequestTypeDef, _OptionalPublishRecipeRequestRequestTypeDef
):
    pass


PublishRecipeResponseTypeDef = TypedDict(
    "PublishRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecipeActionOutputTypeDef = TypedDict(
    "_RequiredRecipeActionOutputTypeDef",
    {
        "Operation": str,
    },
)
_OptionalRecipeActionOutputTypeDef = TypedDict(
    "_OptionalRecipeActionOutputTypeDef",
    {
        "Parameters": Dict[str, str],
    },
    total=False,
)


class RecipeActionOutputTypeDef(
    _RequiredRecipeActionOutputTypeDef, _OptionalRecipeActionOutputTypeDef
):
    pass


_RequiredRecipeActionTypeDef = TypedDict(
    "_RequiredRecipeActionTypeDef",
    {
        "Operation": str,
    },
)
_OptionalRecipeActionTypeDef = TypedDict(
    "_OptionalRecipeActionTypeDef",
    {
        "Parameters": Mapping[str, str],
    },
    total=False,
)


class RecipeActionTypeDef(_RequiredRecipeActionTypeDef, _OptionalRecipeActionTypeDef):
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

_RequiredThresholdOutputTypeDef = TypedDict(
    "_RequiredThresholdOutputTypeDef",
    {
        "Value": float,
    },
)
_OptionalThresholdOutputTypeDef = TypedDict(
    "_OptionalThresholdOutputTypeDef",
    {
        "Type": ThresholdTypeType,
        "Unit": ThresholdUnitType,
    },
    total=False,
)


class ThresholdOutputTypeDef(_RequiredThresholdOutputTypeDef, _OptionalThresholdOutputTypeDef):
    pass


_RequiredThresholdTypeDef = TypedDict(
    "_RequiredThresholdTypeDef",
    {
        "Value": float,
    },
)
_OptionalThresholdTypeDef = TypedDict(
    "_OptionalThresholdTypeDef",
    {
        "Type": ThresholdTypeType,
        "Unit": ThresholdUnitType,
    },
    total=False,
)


class ThresholdTypeDef(_RequiredThresholdTypeDef, _OptionalThresholdTypeDef):
    pass


_RequiredViewFrameTypeDef = TypedDict(
    "_RequiredViewFrameTypeDef",
    {
        "StartColumnIndex": int,
    },
)
_OptionalViewFrameTypeDef = TypedDict(
    "_OptionalViewFrameTypeDef",
    {
        "ColumnRange": int,
        "HiddenColumns": Sequence[str],
        "StartRowIndex": int,
        "RowRange": int,
        "Analytics": AnalyticsModeType,
    },
    total=False,
)


class ViewFrameTypeDef(_RequiredViewFrameTypeDef, _OptionalViewFrameTypeDef):
    pass


SendProjectSessionActionResponseTypeDef = TypedDict(
    "SendProjectSessionActionResponseTypeDef",
    {
        "Result": str,
        "Name": str,
        "ActionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartProjectSessionRequestRequestTypeDef = TypedDict(
    "_RequiredStartProjectSessionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalStartProjectSessionRequestRequestTypeDef = TypedDict(
    "_OptionalStartProjectSessionRequestRequestTypeDef",
    {
        "AssumeControl": bool,
    },
    total=False,
)


class StartProjectSessionRequestRequestTypeDef(
    _RequiredStartProjectSessionRequestRequestTypeDef,
    _OptionalStartProjectSessionRequestRequestTypeDef,
):
    pass


StartProjectSessionResponseTypeDef = TypedDict(
    "StartProjectSessionResponseTypeDef",
    {
        "Name": str,
        "ClientSessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatisticOverrideOutputTypeDef = TypedDict(
    "StatisticOverrideOutputTypeDef",
    {
        "Statistic": str,
        "Parameters": Dict[str, str],
    },
)

StatisticOverrideTypeDef = TypedDict(
    "StatisticOverrideTypeDef",
    {
        "Statistic": str,
        "Parameters": Mapping[str, str],
    },
)

StopJobRunRequestRequestTypeDef = TypedDict(
    "StopJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

StopJobRunResponseTypeDef = TypedDict(
    "StopJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProfileJobResponseTypeDef = TypedDict(
    "UpdateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "LastModifiedDate": datetime,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecipeJobResponseTypeDef = TypedDict(
    "UpdateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecipeResponseTypeDef = TypedDict(
    "UpdateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRulesetResponseTypeDef = TypedDict(
    "UpdateRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
    },
)
_OptionalUpdateScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduleRequestRequestTypeDef",
    {
        "JobNames": Sequence[str],
    },
    total=False,
)


class UpdateScheduleRequestRequestTypeDef(
    _RequiredUpdateScheduleRequestRequestTypeDef, _OptionalUpdateScheduleRequestRequestTypeDef
):
    pass


UpdateScheduleResponseTypeDef = TypedDict(
    "UpdateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEntityDetectorConfigurationOutputTypeDef = TypedDict(
    "_RequiredEntityDetectorConfigurationOutputTypeDef",
    {
        "EntityTypes": List[str],
    },
)
_OptionalEntityDetectorConfigurationOutputTypeDef = TypedDict(
    "_OptionalEntityDetectorConfigurationOutputTypeDef",
    {
        "AllowedStatistics": List[AllowedStatisticsOutputTypeDef],
    },
    total=False,
)


class EntityDetectorConfigurationOutputTypeDef(
    _RequiredEntityDetectorConfigurationOutputTypeDef,
    _OptionalEntityDetectorConfigurationOutputTypeDef,
):
    pass


_RequiredEntityDetectorConfigurationTypeDef = TypedDict(
    "_RequiredEntityDetectorConfigurationTypeDef",
    {
        "EntityTypes": Sequence[str],
    },
)
_OptionalEntityDetectorConfigurationTypeDef = TypedDict(
    "_OptionalEntityDetectorConfigurationTypeDef",
    {
        "AllowedStatistics": Sequence[AllowedStatisticsTypeDef],
    },
    total=False,
)


class EntityDetectorConfigurationTypeDef(
    _RequiredEntityDetectorConfigurationTypeDef, _OptionalEntityDetectorConfigurationTypeDef
):
    pass


BatchDeleteRecipeVersionResponseTypeDef = TypedDict(
    "BatchDeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "Errors": List[RecipeVersionErrorDetailTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDataCatalogInputDefinitionTypeDef = TypedDict(
    "_RequiredDataCatalogInputDefinitionTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalDataCatalogInputDefinitionTypeDef = TypedDict(
    "_OptionalDataCatalogInputDefinitionTypeDef",
    {
        "CatalogId": str,
        "TempDirectory": S3LocationTypeDef,
    },
    total=False,
)


class DataCatalogInputDefinitionTypeDef(
    _RequiredDataCatalogInputDefinitionTypeDef, _OptionalDataCatalogInputDefinitionTypeDef
):
    pass


_RequiredDatabaseInputDefinitionTypeDef = TypedDict(
    "_RequiredDatabaseInputDefinitionTypeDef",
    {
        "GlueConnectionName": str,
    },
)
_OptionalDatabaseInputDefinitionTypeDef = TypedDict(
    "_OptionalDatabaseInputDefinitionTypeDef",
    {
        "DatabaseTableName": str,
        "TempDirectory": S3LocationTypeDef,
        "QueryString": str,
    },
    total=False,
)


class DatabaseInputDefinitionTypeDef(
    _RequiredDatabaseInputDefinitionTypeDef, _OptionalDatabaseInputDefinitionTypeDef
):
    pass


_RequiredDatabaseTableOutputOptionsTypeDef = TypedDict(
    "_RequiredDatabaseTableOutputOptionsTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDatabaseTableOutputOptionsTypeDef = TypedDict(
    "_OptionalDatabaseTableOutputOptionsTypeDef",
    {
        "TempDirectory": S3LocationTypeDef,
    },
    total=False,
)


class DatabaseTableOutputOptionsTypeDef(
    _RequiredDatabaseTableOutputOptionsTypeDef, _OptionalDatabaseTableOutputOptionsTypeDef
):
    pass


S3TableOutputOptionsTypeDef = TypedDict(
    "S3TableOutputOptionsTypeDef",
    {
        "Location": S3LocationTypeDef,
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "RecipeName": str,
        "RoleArn": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "Sample": SampleTypeDef,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass


_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Name": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "Sample": SampleTypeDef,
    },
    total=False,
)


class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass


OutputFormatOptionsOutputTypeDef = TypedDict(
    "OutputFormatOptionsOutputTypeDef",
    {
        "Csv": CsvOutputOptionsOutputTypeDef,
    },
    total=False,
)

OutputFormatOptionsTypeDef = TypedDict(
    "OutputFormatOptionsTypeDef",
    {
        "Csv": CsvOutputOptionsTypeDef,
    },
    total=False,
)

_RequiredDataCatalogInputDefinitionOutputTypeDef = TypedDict(
    "_RequiredDataCatalogInputDefinitionOutputTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalDataCatalogInputDefinitionOutputTypeDef = TypedDict(
    "_OptionalDataCatalogInputDefinitionOutputTypeDef",
    {
        "CatalogId": str,
        "TempDirectory": S3LocationOutputTypeDef,
    },
    total=False,
)


class DataCatalogInputDefinitionOutputTypeDef(
    _RequiredDataCatalogInputDefinitionOutputTypeDef,
    _OptionalDataCatalogInputDefinitionOutputTypeDef,
):
    pass


_RequiredDatabaseInputDefinitionOutputTypeDef = TypedDict(
    "_RequiredDatabaseInputDefinitionOutputTypeDef",
    {
        "GlueConnectionName": str,
    },
)
_OptionalDatabaseInputDefinitionOutputTypeDef = TypedDict(
    "_OptionalDatabaseInputDefinitionOutputTypeDef",
    {
        "DatabaseTableName": str,
        "TempDirectory": S3LocationOutputTypeDef,
        "QueryString": str,
    },
    total=False,
)


class DatabaseInputDefinitionOutputTypeDef(
    _RequiredDatabaseInputDefinitionOutputTypeDef, _OptionalDatabaseInputDefinitionOutputTypeDef
):
    pass


_RequiredDatabaseTableOutputOptionsOutputTypeDef = TypedDict(
    "_RequiredDatabaseTableOutputOptionsOutputTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDatabaseTableOutputOptionsOutputTypeDef = TypedDict(
    "_OptionalDatabaseTableOutputOptionsOutputTypeDef",
    {
        "TempDirectory": S3LocationOutputTypeDef,
    },
    total=False,
)


class DatabaseTableOutputOptionsOutputTypeDef(
    _RequiredDatabaseTableOutputOptionsOutputTypeDef,
    _OptionalDatabaseTableOutputOptionsOutputTypeDef,
):
    pass


S3TableOutputOptionsOutputTypeDef = TypedDict(
    "S3TableOutputOptionsOutputTypeDef",
    {
        "Location": S3LocationOutputTypeDef,
    },
)

_RequiredDatasetParameterOutputTypeDef = TypedDict(
    "_RequiredDatasetParameterOutputTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
    },
)
_OptionalDatasetParameterOutputTypeDef = TypedDict(
    "_OptionalDatasetParameterOutputTypeDef",
    {
        "DatetimeOptions": DatetimeOptionsOutputTypeDef,
        "CreateColumn": bool,
        "Filter": FilterExpressionOutputTypeDef,
    },
    total=False,
)


class DatasetParameterOutputTypeDef(
    _RequiredDatasetParameterOutputTypeDef, _OptionalDatasetParameterOutputTypeDef
):
    pass


_RequiredDatasetParameterTypeDef = TypedDict(
    "_RequiredDatasetParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
    },
)
_OptionalDatasetParameterTypeDef = TypedDict(
    "_OptionalDatasetParameterTypeDef",
    {
        "DatetimeOptions": DatetimeOptionsTypeDef,
        "CreateColumn": bool,
        "Filter": FilterExpressionTypeDef,
    },
    total=False,
)


class DatasetParameterTypeDef(_RequiredDatasetParameterTypeDef, _OptionalDatasetParameterTypeDef):
    pass


DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Name": str,
        "RecipeName": str,
        "ResourceArn": str,
        "Sample": SampleOutputTypeDef,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "SessionStatus": SessionStatusType,
        "OpenedBy": str,
        "OpenDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredProjectTypeDef = TypedDict(
    "_RequiredProjectTypeDef",
    {
        "Name": str,
        "RecipeName": str,
    },
)
_OptionalProjectTypeDef = TypedDict(
    "_OptionalProjectTypeDef",
    {
        "AccountId": str,
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "ResourceArn": str,
        "Sample": SampleOutputTypeDef,
        "Tags": Dict[str, str],
        "RoleArn": str,
        "OpenedBy": str,
        "OpenDate": datetime,
    },
    total=False,
)


class ProjectTypeDef(_RequiredProjectTypeDef, _OptionalProjectTypeDef):
    pass


FormatOptionsOutputTypeDef = TypedDict(
    "FormatOptionsOutputTypeDef",
    {
        "Json": JsonOptionsOutputTypeDef,
        "Excel": ExcelOptionsOutputTypeDef,
        "Csv": CsvOptionsOutputTypeDef,
    },
    total=False,
)

FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "Json": JsonOptionsTypeDef,
        "Excel": ExcelOptionsTypeDef,
        "Csv": CsvOptionsTypeDef,
    },
    total=False,
)

ListRulesetsResponseTypeDef = TypedDict(
    "ListRulesetsResponseTypeDef",
    {
        "Rulesets": List[RulesetItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchedulesResponseTypeDef = TypedDict(
    "ListSchedulesResponseTypeDef",
    {
        "Schedules": List[ScheduleTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecipeStepOutputTypeDef = TypedDict(
    "_RequiredRecipeStepOutputTypeDef",
    {
        "Action": RecipeActionOutputTypeDef,
    },
)
_OptionalRecipeStepOutputTypeDef = TypedDict(
    "_OptionalRecipeStepOutputTypeDef",
    {
        "ConditionExpressions": List[ConditionExpressionOutputTypeDef],
    },
    total=False,
)


class RecipeStepOutputTypeDef(_RequiredRecipeStepOutputTypeDef, _OptionalRecipeStepOutputTypeDef):
    pass


_RequiredRecipeStepTypeDef = TypedDict(
    "_RequiredRecipeStepTypeDef",
    {
        "Action": RecipeActionTypeDef,
    },
)
_OptionalRecipeStepTypeDef = TypedDict(
    "_OptionalRecipeStepTypeDef",
    {
        "ConditionExpressions": Sequence[ConditionExpressionTypeDef],
    },
    total=False,
)


class RecipeStepTypeDef(_RequiredRecipeStepTypeDef, _OptionalRecipeStepTypeDef):
    pass


_RequiredRuleOutputTypeDef = TypedDict(
    "_RequiredRuleOutputTypeDef",
    {
        "Name": str,
        "CheckExpression": str,
    },
)
_OptionalRuleOutputTypeDef = TypedDict(
    "_OptionalRuleOutputTypeDef",
    {
        "Disabled": bool,
        "SubstitutionMap": Dict[str, str],
        "Threshold": ThresholdOutputTypeDef,
        "ColumnSelectors": List[ColumnSelectorOutputTypeDef],
    },
    total=False,
)


class RuleOutputTypeDef(_RequiredRuleOutputTypeDef, _OptionalRuleOutputTypeDef):
    pass


_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Name": str,
        "CheckExpression": str,
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Disabled": bool,
        "SubstitutionMap": Mapping[str, str],
        "Threshold": ThresholdTypeDef,
        "ColumnSelectors": Sequence[ColumnSelectorTypeDef],
    },
    total=False,
)


class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass


StatisticsConfigurationOutputTypeDef = TypedDict(
    "StatisticsConfigurationOutputTypeDef",
    {
        "IncludedStatistics": List[str],
        "Overrides": List[StatisticOverrideOutputTypeDef],
    },
    total=False,
)

StatisticsConfigurationTypeDef = TypedDict(
    "StatisticsConfigurationTypeDef",
    {
        "IncludedStatistics": Sequence[str],
        "Overrides": Sequence[StatisticOverrideTypeDef],
    },
    total=False,
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "S3InputDefinition": S3LocationTypeDef,
        "DataCatalogInputDefinition": DataCatalogInputDefinitionTypeDef,
        "DatabaseInputDefinition": DatabaseInputDefinitionTypeDef,
        "Metadata": MetadataTypeDef,
    },
    total=False,
)

_RequiredDatabaseOutputTypeDef = TypedDict(
    "_RequiredDatabaseOutputTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseOptions": DatabaseTableOutputOptionsTypeDef,
    },
)
_OptionalDatabaseOutputTypeDef = TypedDict(
    "_OptionalDatabaseOutputTypeDef",
    {
        "DatabaseOutputMode": Literal["NEW_TABLE"],
    },
    total=False,
)


class DatabaseOutputTypeDef(_RequiredDatabaseOutputTypeDef, _OptionalDatabaseOutputTypeDef):
    pass


_RequiredDataCatalogOutputTypeDef = TypedDict(
    "_RequiredDataCatalogOutputTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalDataCatalogOutputTypeDef = TypedDict(
    "_OptionalDataCatalogOutputTypeDef",
    {
        "CatalogId": str,
        "S3Options": S3TableOutputOptionsTypeDef,
        "DatabaseOptions": DatabaseTableOutputOptionsTypeDef,
        "Overwrite": bool,
    },
    total=False,
)


class DataCatalogOutputTypeDef(
    _RequiredDataCatalogOutputTypeDef, _OptionalDataCatalogOutputTypeDef
):
    pass


_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "Location": S3LocationTypeDef,
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "CompressionFormat": CompressionFormatType,
        "Format": OutputFormatType,
        "PartitionColumns": Sequence[str],
        "Overwrite": bool,
        "FormatOptions": OutputFormatOptionsTypeDef,
        "MaxOutputFiles": int,
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass


InputOutputTypeDef = TypedDict(
    "InputOutputTypeDef",
    {
        "S3InputDefinition": S3LocationOutputTypeDef,
        "DataCatalogInputDefinition": DataCatalogInputDefinitionOutputTypeDef,
        "DatabaseInputDefinition": DatabaseInputDefinitionOutputTypeDef,
        "Metadata": MetadataOutputTypeDef,
    },
    total=False,
)

PathOptionsOutputTypeDef = TypedDict(
    "PathOptionsOutputTypeDef",
    {
        "LastModifiedDateCondition": FilterExpressionOutputTypeDef,
        "FilesLimit": FilesLimitOutputTypeDef,
        "Parameters": Dict[str, DatasetParameterOutputTypeDef],
    },
    total=False,
)

PathOptionsTypeDef = TypedDict(
    "PathOptionsTypeDef",
    {
        "LastModifiedDateCondition": FilterExpressionTypeDef,
        "FilesLimit": FilesLimitTypeDef,
        "Parameters": Mapping[str, DatasetParameterTypeDef],
    },
    total=False,
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "Projects": List[ProjectTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecipeResponseTypeDef = TypedDict(
    "DescribeRecipeResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "Name": str,
        "Steps": List[RecipeStepOutputTypeDef],
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "RecipeVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecipeTypeDef = TypedDict(
    "_RequiredRecipeTypeDef",
    {
        "Name": str,
    },
)
_OptionalRecipeTypeDef = TypedDict(
    "_OptionalRecipeTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "ResourceArn": str,
        "Steps": List[RecipeStepOutputTypeDef],
        "Tags": Dict[str, str],
        "RecipeVersion": str,
    },
    total=False,
)


class RecipeTypeDef(_RequiredRecipeTypeDef, _OptionalRecipeTypeDef):
    pass


_RequiredCreateRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Steps": Sequence[RecipeStepTypeDef],
    },
)
_OptionalCreateRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRecipeRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateRecipeRequestRequestTypeDef(
    _RequiredCreateRecipeRequestRequestTypeDef, _OptionalCreateRecipeRequestRequestTypeDef
):
    pass


_RequiredSendProjectSessionActionRequestRequestTypeDef = TypedDict(
    "_RequiredSendProjectSessionActionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalSendProjectSessionActionRequestRequestTypeDef = TypedDict(
    "_OptionalSendProjectSessionActionRequestRequestTypeDef",
    {
        "Preview": bool,
        "RecipeStep": RecipeStepTypeDef,
        "StepIndex": int,
        "ClientSessionId": str,
        "ViewFrame": ViewFrameTypeDef,
    },
    total=False,
)


class SendProjectSessionActionRequestRequestTypeDef(
    _RequiredSendProjectSessionActionRequestRequestTypeDef,
    _OptionalSendProjectSessionActionRequestRequestTypeDef,
):
    pass


_RequiredUpdateRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRecipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRecipeRequestRequestTypeDef",
    {
        "Description": str,
        "Steps": Sequence[RecipeStepTypeDef],
    },
    total=False,
)


class UpdateRecipeRequestRequestTypeDef(
    _RequiredUpdateRecipeRequestRequestTypeDef, _OptionalUpdateRecipeRequestRequestTypeDef
):
    pass


DescribeRulesetResponseTypeDef = TypedDict(
    "DescribeRulesetResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "TargetArn": str,
        "Rules": List[RuleOutputTypeDef],
        "CreateDate": datetime,
        "CreatedBy": str,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRulesetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "TargetArn": str,
        "Rules": Sequence[RuleTypeDef],
    },
)
_OptionalCreateRulesetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRulesetRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateRulesetRequestRequestTypeDef(
    _RequiredCreateRulesetRequestRequestTypeDef, _OptionalCreateRulesetRequestRequestTypeDef
):
    pass


_RequiredUpdateRulesetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "Rules": Sequence[RuleTypeDef],
    },
)
_OptionalUpdateRulesetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRulesetRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateRulesetRequestRequestTypeDef(
    _RequiredUpdateRulesetRequestRequestTypeDef, _OptionalUpdateRulesetRequestRequestTypeDef
):
    pass


_RequiredColumnStatisticsConfigurationOutputTypeDef = TypedDict(
    "_RequiredColumnStatisticsConfigurationOutputTypeDef",
    {
        "Statistics": StatisticsConfigurationOutputTypeDef,
    },
)
_OptionalColumnStatisticsConfigurationOutputTypeDef = TypedDict(
    "_OptionalColumnStatisticsConfigurationOutputTypeDef",
    {
        "Selectors": List[ColumnSelectorOutputTypeDef],
    },
    total=False,
)


class ColumnStatisticsConfigurationOutputTypeDef(
    _RequiredColumnStatisticsConfigurationOutputTypeDef,
    _OptionalColumnStatisticsConfigurationOutputTypeDef,
):
    pass


_RequiredColumnStatisticsConfigurationTypeDef = TypedDict(
    "_RequiredColumnStatisticsConfigurationTypeDef",
    {
        "Statistics": StatisticsConfigurationTypeDef,
    },
)
_OptionalColumnStatisticsConfigurationTypeDef = TypedDict(
    "_OptionalColumnStatisticsConfigurationTypeDef",
    {
        "Selectors": Sequence[ColumnSelectorTypeDef],
    },
    total=False,
)


class ColumnStatisticsConfigurationTypeDef(
    _RequiredColumnStatisticsConfigurationTypeDef, _OptionalColumnStatisticsConfigurationTypeDef
):
    pass


_RequiredCreateRecipeJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalCreateRecipeJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRecipeJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": Sequence[OutputTypeDef],
        "DataCatalogOutputs": Sequence[DataCatalogOutputTypeDef],
        "DatabaseOutputs": Sequence[DatabaseOutputTypeDef],
        "ProjectName": str,
        "RecipeReference": RecipeReferenceTypeDef,
        "Tags": Mapping[str, str],
        "Timeout": int,
    },
    total=False,
)


class CreateRecipeJobRequestRequestTypeDef(
    _RequiredCreateRecipeJobRequestRequestTypeDef, _OptionalCreateRecipeJobRequestRequestTypeDef
):
    pass


JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List[OutputTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "RecipeReference": RecipeReferenceOutputTypeDef,
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": JobSampleOutputTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationOutputTypeDef],
    },
    total=False,
)

_RequiredJobTypeDef = TypedDict(
    "_RequiredJobTypeDef",
    {
        "Name": str,
    },
)
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List[OutputTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "ProjectName": str,
        "RecipeReference": RecipeReferenceOutputTypeDef,
        "ResourceArn": str,
        "RoleArn": str,
        "Timeout": int,
        "Tags": Dict[str, str],
        "JobSample": JobSampleOutputTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationOutputTypeDef],
    },
    total=False,
)


class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass


_RequiredUpdateRecipeJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalUpdateRecipeJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRecipeJobRequestRequestTypeDef",
    {
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": Sequence[OutputTypeDef],
        "DataCatalogOutputs": Sequence[DataCatalogOutputTypeDef],
        "DatabaseOutputs": Sequence[DatabaseOutputTypeDef],
        "Timeout": int,
    },
    total=False,
)


class UpdateRecipeJobRequestRequestTypeDef(
    _RequiredUpdateRecipeJobRequestRequestTypeDef, _OptionalUpdateRecipeJobRequestRequestTypeDef
):
    pass


_RequiredDatasetTypeDef = TypedDict(
    "_RequiredDatasetTypeDef",
    {
        "Name": str,
        "Input": InputOutputTypeDef,
    },
)
_OptionalDatasetTypeDef = TypedDict(
    "_OptionalDatasetTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "Format": InputFormatType,
        "FormatOptions": FormatOptionsOutputTypeDef,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": PathOptionsOutputTypeDef,
        "Tags": Dict[str, str],
        "ResourceArn": str,
    },
    total=False,
)


class DatasetTypeDef(_RequiredDatasetTypeDef, _OptionalDatasetTypeDef):
    pass


DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "Name": str,
        "Format": InputFormatType,
        "FormatOptions": FormatOptionsOutputTypeDef,
        "Input": InputOutputTypeDef,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": PathOptionsOutputTypeDef,
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "Format": InputFormatType,
        "FormatOptions": FormatOptionsTypeDef,
        "PathOptions": PathOptionsTypeDef,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass


_RequiredUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
    },
)
_OptionalUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestRequestTypeDef",
    {
        "Format": InputFormatType,
        "FormatOptions": FormatOptionsTypeDef,
        "PathOptions": PathOptionsTypeDef,
    },
    total=False,
)


class UpdateDatasetRequestRequestTypeDef(
    _RequiredUpdateDatasetRequestRequestTypeDef, _OptionalUpdateDatasetRequestRequestTypeDef
):
    pass


ListRecipeVersionsResponseTypeDef = TypedDict(
    "ListRecipeVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Recipes": List[RecipeTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {
        "Recipes": List[RecipeTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProfileConfigurationOutputTypeDef = TypedDict(
    "ProfileConfigurationOutputTypeDef",
    {
        "DatasetStatisticsConfiguration": StatisticsConfigurationOutputTypeDef,
        "ProfileColumns": List[ColumnSelectorOutputTypeDef],
        "ColumnStatisticsConfigurations": List[ColumnStatisticsConfigurationOutputTypeDef],
        "EntityDetectorConfiguration": EntityDetectorConfigurationOutputTypeDef,
    },
    total=False,
)

ProfileConfigurationTypeDef = TypedDict(
    "ProfileConfigurationTypeDef",
    {
        "DatasetStatisticsConfiguration": StatisticsConfigurationTypeDef,
        "ProfileColumns": Sequence[ColumnSelectorTypeDef],
        "ColumnStatisticsConfigurations": Sequence[ColumnStatisticsConfigurationTypeDef],
        "EntityDetectorConfiguration": EntityDetectorConfigurationTypeDef,
    },
    total=False,
)

ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "JobRuns": List[JobRunTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List[DatasetTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobResponseTypeDef = TypedDict(
    "DescribeJobResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Name": str,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List[OutputTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "ProjectName": str,
        "ProfileConfiguration": ProfileConfigurationOutputTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationOutputTypeDef],
        "RecipeReference": RecipeReferenceOutputTypeDef,
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": JobSampleOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "ProfileConfiguration": ProfileConfigurationOutputTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationOutputTypeDef],
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List[OutputTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "RecipeReference": RecipeReferenceOutputTypeDef,
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": JobSampleOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfileJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "OutputLocation": S3LocationTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateProfileJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfileJobRequestRequestTypeDef",
    {
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Configuration": ProfileConfigurationTypeDef,
        "ValidationConfigurations": Sequence[ValidationConfigurationTypeDef],
        "Tags": Mapping[str, str],
        "Timeout": int,
        "JobSample": JobSampleTypeDef,
    },
    total=False,
)


class CreateProfileJobRequestRequestTypeDef(
    _RequiredCreateProfileJobRequestRequestTypeDef, _OptionalCreateProfileJobRequestRequestTypeDef
):
    pass


_RequiredUpdateProfileJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileJobRequestRequestTypeDef",
    {
        "Name": str,
        "OutputLocation": S3LocationTypeDef,
        "RoleArn": str,
    },
)
_OptionalUpdateProfileJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileJobRequestRequestTypeDef",
    {
        "Configuration": ProfileConfigurationTypeDef,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "ValidationConfigurations": Sequence[ValidationConfigurationTypeDef],
        "Timeout": int,
        "JobSample": JobSampleTypeDef,
    },
    total=False,
)


class UpdateProfileJobRequestRequestTypeDef(
    _RequiredUpdateProfileJobRequestRequestTypeDef, _OptionalUpdateProfileJobRequestRequestTypeDef
):
    pass
