"""
Type annotations for entityresolution service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/type_defs/)

Usage::

    ```python
    from mypy_boto3_entityresolution.type_defs import IncrementalRunConfigTypeDef

    data: IncrementalRunConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AttributeMatchingModelType,
    JobStatusType,
    ResolutionTypeType,
    SchemaAttributeTypeType,
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
    "IncrementalRunConfigTypeDef",
    "InputSourceTypeDef",
    "IncrementalRunConfigOutputTypeDef",
    "InputSourceOutputTypeDef",
    "SchemaInputAttributeTypeDef",
    "SchemaInputAttributeOutputTypeDef",
    "DeleteMatchingWorkflowInputRequestTypeDef",
    "DeleteMatchingWorkflowOutputTypeDef",
    "DeleteSchemaMappingInputRequestTypeDef",
    "DeleteSchemaMappingOutputTypeDef",
    "ErrorDetailsTypeDef",
    "GetMatchIdInputRequestTypeDef",
    "GetMatchIdOutputTypeDef",
    "GetMatchingJobInputRequestTypeDef",
    "JobMetricsTypeDef",
    "GetMatchingWorkflowInputRequestTypeDef",
    "GetSchemaMappingInputRequestTypeDef",
    "JobSummaryTypeDef",
    "ListMatchingJobsInputListMatchingJobsPaginateTypeDef",
    "ListMatchingJobsInputRequestTypeDef",
    "ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef",
    "ListMatchingWorkflowsInputRequestTypeDef",
    "MatchingWorkflowSummaryTypeDef",
    "ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef",
    "ListSchemaMappingsInputRequestTypeDef",
    "SchemaMappingSummaryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "OutputAttributeOutputTypeDef",
    "OutputAttributeTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "StartMatchingJobInputRequestTypeDef",
    "StartMatchingJobOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "CreateSchemaMappingInputRequestTypeDef",
    "CreateSchemaMappingOutputTypeDef",
    "GetSchemaMappingOutputTypeDef",
    "GetMatchingJobOutputTypeDef",
    "ListMatchingJobsOutputTypeDef",
    "ListMatchingWorkflowsOutputTypeDef",
    "ListSchemaMappingsOutputTypeDef",
    "OutputSourceOutputTypeDef",
    "OutputSourceTypeDef",
    "RuleBasedPropertiesOutputTypeDef",
    "RuleBasedPropertiesTypeDef",
    "ResolutionTechniquesOutputTypeDef",
    "ResolutionTechniquesTypeDef",
    "CreateMatchingWorkflowOutputTypeDef",
    "GetMatchingWorkflowOutputTypeDef",
    "UpdateMatchingWorkflowOutputTypeDef",
    "CreateMatchingWorkflowInputRequestTypeDef",
    "UpdateMatchingWorkflowInputRequestTypeDef",
)

IncrementalRunConfigTypeDef = TypedDict(
    "IncrementalRunConfigTypeDef",
    {
        "incrementalRunType": Literal["IMMEDIATE"],
    },
    total=False,
)

_RequiredInputSourceTypeDef = TypedDict(
    "_RequiredInputSourceTypeDef",
    {
        "inputSourceARN": str,
        "schemaName": str,
    },
)
_OptionalInputSourceTypeDef = TypedDict(
    "_OptionalInputSourceTypeDef",
    {
        "applyNormalization": bool,
    },
    total=False,
)


class InputSourceTypeDef(_RequiredInputSourceTypeDef, _OptionalInputSourceTypeDef):
    pass


IncrementalRunConfigOutputTypeDef = TypedDict(
    "IncrementalRunConfigOutputTypeDef",
    {
        "incrementalRunType": Literal["IMMEDIATE"],
    },
    total=False,
)

_RequiredInputSourceOutputTypeDef = TypedDict(
    "_RequiredInputSourceOutputTypeDef",
    {
        "inputSourceARN": str,
        "schemaName": str,
    },
)
_OptionalInputSourceOutputTypeDef = TypedDict(
    "_OptionalInputSourceOutputTypeDef",
    {
        "applyNormalization": bool,
    },
    total=False,
)


class InputSourceOutputTypeDef(
    _RequiredInputSourceOutputTypeDef, _OptionalInputSourceOutputTypeDef
):
    pass


_RequiredSchemaInputAttributeTypeDef = TypedDict(
    "_RequiredSchemaInputAttributeTypeDef",
    {
        "fieldName": str,
        "type": SchemaAttributeTypeType,
    },
)
_OptionalSchemaInputAttributeTypeDef = TypedDict(
    "_OptionalSchemaInputAttributeTypeDef",
    {
        "groupName": str,
        "matchKey": str,
    },
    total=False,
)


class SchemaInputAttributeTypeDef(
    _RequiredSchemaInputAttributeTypeDef, _OptionalSchemaInputAttributeTypeDef
):
    pass


_RequiredSchemaInputAttributeOutputTypeDef = TypedDict(
    "_RequiredSchemaInputAttributeOutputTypeDef",
    {
        "fieldName": str,
        "type": SchemaAttributeTypeType,
    },
)
_OptionalSchemaInputAttributeOutputTypeDef = TypedDict(
    "_OptionalSchemaInputAttributeOutputTypeDef",
    {
        "groupName": str,
        "matchKey": str,
    },
    total=False,
)


class SchemaInputAttributeOutputTypeDef(
    _RequiredSchemaInputAttributeOutputTypeDef, _OptionalSchemaInputAttributeOutputTypeDef
):
    pass


DeleteMatchingWorkflowInputRequestTypeDef = TypedDict(
    "DeleteMatchingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

DeleteMatchingWorkflowOutputTypeDef = TypedDict(
    "DeleteMatchingWorkflowOutputTypeDef",
    {
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSchemaMappingInputRequestTypeDef = TypedDict(
    "DeleteSchemaMappingInputRequestTypeDef",
    {
        "schemaName": str,
    },
)

DeleteSchemaMappingOutputTypeDef = TypedDict(
    "DeleteSchemaMappingOutputTypeDef",
    {
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "errorMessage": str,
    },
    total=False,
)

GetMatchIdInputRequestTypeDef = TypedDict(
    "GetMatchIdInputRequestTypeDef",
    {
        "record": Mapping[str, str],
        "workflowName": str,
    },
)

GetMatchIdOutputTypeDef = TypedDict(
    "GetMatchIdOutputTypeDef",
    {
        "matchId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMatchingJobInputRequestTypeDef = TypedDict(
    "GetMatchingJobInputRequestTypeDef",
    {
        "jobId": str,
        "workflowName": str,
    },
)

JobMetricsTypeDef = TypedDict(
    "JobMetricsTypeDef",
    {
        "inputRecords": int,
        "matchIDs": int,
        "recordsNotProcessed": int,
        "totalRecordsProcessed": int,
    },
    total=False,
)

GetMatchingWorkflowInputRequestTypeDef = TypedDict(
    "GetMatchingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

GetSchemaMappingInputRequestTypeDef = TypedDict(
    "GetSchemaMappingInputRequestTypeDef",
    {
        "schemaName": str,
    },
)

_RequiredJobSummaryTypeDef = TypedDict(
    "_RequiredJobSummaryTypeDef",
    {
        "jobId": str,
        "startTime": datetime,
        "status": JobStatusType,
    },
)
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "endTime": datetime,
    },
    total=False,
)


class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass


_RequiredListMatchingJobsInputListMatchingJobsPaginateTypeDef = TypedDict(
    "_RequiredListMatchingJobsInputListMatchingJobsPaginateTypeDef",
    {
        "workflowName": str,
    },
)
_OptionalListMatchingJobsInputListMatchingJobsPaginateTypeDef = TypedDict(
    "_OptionalListMatchingJobsInputListMatchingJobsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListMatchingJobsInputListMatchingJobsPaginateTypeDef(
    _RequiredListMatchingJobsInputListMatchingJobsPaginateTypeDef,
    _OptionalListMatchingJobsInputListMatchingJobsPaginateTypeDef,
):
    pass


_RequiredListMatchingJobsInputRequestTypeDef = TypedDict(
    "_RequiredListMatchingJobsInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
_OptionalListMatchingJobsInputRequestTypeDef = TypedDict(
    "_OptionalListMatchingJobsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListMatchingJobsInputRequestTypeDef(
    _RequiredListMatchingJobsInputRequestTypeDef, _OptionalListMatchingJobsInputRequestTypeDef
):
    pass


ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef = TypedDict(
    "ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListMatchingWorkflowsInputRequestTypeDef = TypedDict(
    "ListMatchingWorkflowsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

MatchingWorkflowSummaryTypeDef = TypedDict(
    "MatchingWorkflowSummaryTypeDef",
    {
        "createdAt": datetime,
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
    },
)

ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef = TypedDict(
    "ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSchemaMappingsInputRequestTypeDef = TypedDict(
    "ListSchemaMappingsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

SchemaMappingSummaryTypeDef = TypedDict(
    "SchemaMappingSummaryTypeDef",
    {
        "createdAt": datetime,
        "schemaArn": str,
        "schemaName": str,
        "updatedAt": datetime,
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOutputAttributeOutputTypeDef = TypedDict(
    "_RequiredOutputAttributeOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalOutputAttributeOutputTypeDef = TypedDict(
    "_OptionalOutputAttributeOutputTypeDef",
    {
        "hashed": bool,
    },
    total=False,
)


class OutputAttributeOutputTypeDef(
    _RequiredOutputAttributeOutputTypeDef, _OptionalOutputAttributeOutputTypeDef
):
    pass


_RequiredOutputAttributeTypeDef = TypedDict(
    "_RequiredOutputAttributeTypeDef",
    {
        "name": str,
    },
)
_OptionalOutputAttributeTypeDef = TypedDict(
    "_OptionalOutputAttributeTypeDef",
    {
        "hashed": bool,
    },
    total=False,
)


class OutputAttributeTypeDef(_RequiredOutputAttributeTypeDef, _OptionalOutputAttributeTypeDef):
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

RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "matchingKeys": List[str],
        "ruleName": str,
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "matchingKeys": Sequence[str],
        "ruleName": str,
    },
)

StartMatchingJobInputRequestTypeDef = TypedDict(
    "StartMatchingJobInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

StartMatchingJobOutputTypeDef = TypedDict(
    "StartMatchingJobOutputTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredCreateSchemaMappingInputRequestTypeDef = TypedDict(
    "_RequiredCreateSchemaMappingInputRequestTypeDef",
    {
        "schemaName": str,
    },
)
_OptionalCreateSchemaMappingInputRequestTypeDef = TypedDict(
    "_OptionalCreateSchemaMappingInputRequestTypeDef",
    {
        "description": str,
        "mappedInputFields": Sequence[SchemaInputAttributeTypeDef],
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateSchemaMappingInputRequestTypeDef(
    _RequiredCreateSchemaMappingInputRequestTypeDef, _OptionalCreateSchemaMappingInputRequestTypeDef
):
    pass


CreateSchemaMappingOutputTypeDef = TypedDict(
    "CreateSchemaMappingOutputTypeDef",
    {
        "description": str,
        "mappedInputFields": List[SchemaInputAttributeOutputTypeDef],
        "schemaArn": str,
        "schemaName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaMappingOutputTypeDef = TypedDict(
    "GetSchemaMappingOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "mappedInputFields": List[SchemaInputAttributeOutputTypeDef],
        "schemaArn": str,
        "schemaName": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMatchingJobOutputTypeDef = TypedDict(
    "GetMatchingJobOutputTypeDef",
    {
        "endTime": datetime,
        "errorDetails": ErrorDetailsTypeDef,
        "jobId": str,
        "metrics": JobMetricsTypeDef,
        "startTime": datetime,
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMatchingJobsOutputTypeDef = TypedDict(
    "ListMatchingJobsOutputTypeDef",
    {
        "jobs": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMatchingWorkflowsOutputTypeDef = TypedDict(
    "ListMatchingWorkflowsOutputTypeDef",
    {
        "nextToken": str,
        "workflowSummaries": List[MatchingWorkflowSummaryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemaMappingsOutputTypeDef = TypedDict(
    "ListSchemaMappingsOutputTypeDef",
    {
        "nextToken": str,
        "schemaList": List[SchemaMappingSummaryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOutputSourceOutputTypeDef = TypedDict(
    "_RequiredOutputSourceOutputTypeDef",
    {
        "output": List[OutputAttributeOutputTypeDef],
        "outputS3Path": str,
    },
)
_OptionalOutputSourceOutputTypeDef = TypedDict(
    "_OptionalOutputSourceOutputTypeDef",
    {
        "KMSArn": str,
        "applyNormalization": bool,
    },
    total=False,
)


class OutputSourceOutputTypeDef(
    _RequiredOutputSourceOutputTypeDef, _OptionalOutputSourceOutputTypeDef
):
    pass


_RequiredOutputSourceTypeDef = TypedDict(
    "_RequiredOutputSourceTypeDef",
    {
        "output": Sequence[OutputAttributeTypeDef],
        "outputS3Path": str,
    },
)
_OptionalOutputSourceTypeDef = TypedDict(
    "_OptionalOutputSourceTypeDef",
    {
        "KMSArn": str,
        "applyNormalization": bool,
    },
    total=False,
)


class OutputSourceTypeDef(_RequiredOutputSourceTypeDef, _OptionalOutputSourceTypeDef):
    pass


RuleBasedPropertiesOutputTypeDef = TypedDict(
    "RuleBasedPropertiesOutputTypeDef",
    {
        "attributeMatchingModel": AttributeMatchingModelType,
        "rules": List[RuleOutputTypeDef],
    },
)

RuleBasedPropertiesTypeDef = TypedDict(
    "RuleBasedPropertiesTypeDef",
    {
        "attributeMatchingModel": AttributeMatchingModelType,
        "rules": Sequence[RuleTypeDef],
    },
)

ResolutionTechniquesOutputTypeDef = TypedDict(
    "ResolutionTechniquesOutputTypeDef",
    {
        "resolutionType": ResolutionTypeType,
        "ruleBasedProperties": RuleBasedPropertiesOutputTypeDef,
    },
    total=False,
)

ResolutionTechniquesTypeDef = TypedDict(
    "ResolutionTechniquesTypeDef",
    {
        "resolutionType": ResolutionTypeType,
        "ruleBasedProperties": RuleBasedPropertiesTypeDef,
    },
    total=False,
)

CreateMatchingWorkflowOutputTypeDef = TypedDict(
    "CreateMatchingWorkflowOutputTypeDef",
    {
        "description": str,
        "incrementalRunConfig": IncrementalRunConfigOutputTypeDef,
        "inputSourceConfig": List[InputSourceOutputTypeDef],
        "outputSourceConfig": List[OutputSourceOutputTypeDef],
        "resolutionTechniques": ResolutionTechniquesOutputTypeDef,
        "roleArn": str,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMatchingWorkflowOutputTypeDef = TypedDict(
    "GetMatchingWorkflowOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "incrementalRunConfig": IncrementalRunConfigOutputTypeDef,
        "inputSourceConfig": List[InputSourceOutputTypeDef],
        "outputSourceConfig": List[OutputSourceOutputTypeDef],
        "resolutionTechniques": ResolutionTechniquesOutputTypeDef,
        "roleArn": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMatchingWorkflowOutputTypeDef = TypedDict(
    "UpdateMatchingWorkflowOutputTypeDef",
    {
        "description": str,
        "incrementalRunConfig": IncrementalRunConfigOutputTypeDef,
        "inputSourceConfig": List[InputSourceOutputTypeDef],
        "outputSourceConfig": List[OutputSourceOutputTypeDef],
        "resolutionTechniques": ResolutionTechniquesOutputTypeDef,
        "roleArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "_RequiredCreateMatchingWorkflowInputRequestTypeDef",
    {
        "inputSourceConfig": Sequence[InputSourceTypeDef],
        "outputSourceConfig": Sequence[OutputSourceTypeDef],
        "resolutionTechniques": ResolutionTechniquesTypeDef,
        "roleArn": str,
        "workflowName": str,
    },
)
_OptionalCreateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "_OptionalCreateMatchingWorkflowInputRequestTypeDef",
    {
        "description": str,
        "incrementalRunConfig": IncrementalRunConfigTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateMatchingWorkflowInputRequestTypeDef(
    _RequiredCreateMatchingWorkflowInputRequestTypeDef,
    _OptionalCreateMatchingWorkflowInputRequestTypeDef,
):
    pass


_RequiredUpdateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMatchingWorkflowInputRequestTypeDef",
    {
        "inputSourceConfig": Sequence[InputSourceTypeDef],
        "outputSourceConfig": Sequence[OutputSourceTypeDef],
        "resolutionTechniques": ResolutionTechniquesTypeDef,
        "roleArn": str,
        "workflowName": str,
    },
)
_OptionalUpdateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMatchingWorkflowInputRequestTypeDef",
    {
        "description": str,
        "incrementalRunConfig": IncrementalRunConfigTypeDef,
    },
    total=False,
)


class UpdateMatchingWorkflowInputRequestTypeDef(
    _RequiredUpdateMatchingWorkflowInputRequestTypeDef,
    _OptionalUpdateMatchingWorkflowInputRequestTypeDef,
):
    pass
