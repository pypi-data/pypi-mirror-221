"""
Type annotations for codeguru-reviewer service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/type_defs/)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.type_defs import KMSKeyDetailsTypeDef

    data: KMSKeyDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AnalysisTypeType,
    ConfigFileStateType,
    EncryptionOptionType,
    JobStateType,
    ProviderTypeType,
    ReactionType,
    RecommendationCategoryType,
    RepositoryAssociationStateType,
    SeverityType,
    TypeType,
    VendorNameType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "KMSKeyDetailsTypeDef",
    "BranchDiffSourceCodeTypeOutputTypeDef",
    "BranchDiffSourceCodeTypeTypeDef",
    "CodeArtifactsOutputTypeDef",
    "CodeArtifactsTypeDef",
    "CodeCommitRepositoryTypeDef",
    "MetricsSummaryTypeDef",
    "MetricsTypeDef",
    "CommitDiffSourceCodeTypeOutputTypeDef",
    "CommitDiffSourceCodeTypeTypeDef",
    "WaiterConfigTypeDef",
    "DescribeCodeReviewRequestRequestTypeDef",
    "DescribeRecommendationFeedbackRequestRequestTypeDef",
    "RecommendationFeedbackTypeDef",
    "DescribeRepositoryAssociationRequestRequestTypeDef",
    "DisassociateRepositoryRequestRequestTypeDef",
    "EventInfoOutputTypeDef",
    "EventInfoTypeDef",
    "KMSKeyDetailsOutputTypeDef",
    "ListCodeReviewsRequestRequestTypeDef",
    "ListRecommendationFeedbackRequestRequestTypeDef",
    "RecommendationFeedbackSummaryTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateTypeDef",
    "ListRepositoryAssociationsRequestRequestTypeDef",
    "RepositoryAssociationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecommendationFeedbackRequestRequestTypeDef",
    "RuleMetadataTypeDef",
    "RepositoryHeadSourceCodeTypeTypeDef",
    "RepositoryHeadSourceCodeTypeOutputTypeDef",
    "S3RepositoryTypeDef",
    "ThirdPartySourceRepositoryTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "S3RepositoryDetailsOutputTypeDef",
    "S3RepositoryDetailsTypeDef",
    "DescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef",
    "DescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef",
    "DescribeRecommendationFeedbackResponseTypeDef",
    "RequestMetadataOutputTypeDef",
    "RequestMetadataTypeDef",
    "ListRecommendationFeedbackResponseTypeDef",
    "ListRepositoryAssociationsResponseTypeDef",
    "RecommendationSummaryTypeDef",
    "RepositoryTypeDef",
    "RepositoryAssociationTypeDef",
    "S3BucketRepositoryOutputTypeDef",
    "S3BucketRepositoryTypeDef",
    "ListRecommendationsResponseTypeDef",
    "AssociateRepositoryRequestRequestTypeDef",
    "AssociateRepositoryResponseTypeDef",
    "DescribeRepositoryAssociationResponseTypeDef",
    "DisassociateRepositoryResponseTypeDef",
    "SourceCodeTypeOutputTypeDef",
    "SourceCodeTypeTypeDef",
    "CodeReviewSummaryTypeDef",
    "CodeReviewTypeDef",
    "RepositoryAnalysisTypeDef",
    "ListCodeReviewsResponseTypeDef",
    "CreateCodeReviewResponseTypeDef",
    "DescribeCodeReviewResponseTypeDef",
    "CodeReviewTypeTypeDef",
    "CreateCodeReviewRequestRequestTypeDef",
)

KMSKeyDetailsTypeDef = TypedDict(
    "KMSKeyDetailsTypeDef",
    {
        "KMSKeyId": str,
        "EncryptionOption": EncryptionOptionType,
    },
    total=False,
)

BranchDiffSourceCodeTypeOutputTypeDef = TypedDict(
    "BranchDiffSourceCodeTypeOutputTypeDef",
    {
        "SourceBranchName": str,
        "DestinationBranchName": str,
    },
)

BranchDiffSourceCodeTypeTypeDef = TypedDict(
    "BranchDiffSourceCodeTypeTypeDef",
    {
        "SourceBranchName": str,
        "DestinationBranchName": str,
    },
)

_RequiredCodeArtifactsOutputTypeDef = TypedDict(
    "_RequiredCodeArtifactsOutputTypeDef",
    {
        "SourceCodeArtifactsObjectKey": str,
    },
)
_OptionalCodeArtifactsOutputTypeDef = TypedDict(
    "_OptionalCodeArtifactsOutputTypeDef",
    {
        "BuildArtifactsObjectKey": str,
    },
    total=False,
)

class CodeArtifactsOutputTypeDef(
    _RequiredCodeArtifactsOutputTypeDef, _OptionalCodeArtifactsOutputTypeDef
):
    pass

_RequiredCodeArtifactsTypeDef = TypedDict(
    "_RequiredCodeArtifactsTypeDef",
    {
        "SourceCodeArtifactsObjectKey": str,
    },
)
_OptionalCodeArtifactsTypeDef = TypedDict(
    "_OptionalCodeArtifactsTypeDef",
    {
        "BuildArtifactsObjectKey": str,
    },
    total=False,
)

class CodeArtifactsTypeDef(_RequiredCodeArtifactsTypeDef, _OptionalCodeArtifactsTypeDef):
    pass

CodeCommitRepositoryTypeDef = TypedDict(
    "CodeCommitRepositoryTypeDef",
    {
        "Name": str,
    },
)

MetricsSummaryTypeDef = TypedDict(
    "MetricsSummaryTypeDef",
    {
        "MeteredLinesOfCodeCount": int,
        "SuppressedLinesOfCodeCount": int,
        "FindingsCount": int,
    },
    total=False,
)

MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "MeteredLinesOfCodeCount": int,
        "SuppressedLinesOfCodeCount": int,
        "FindingsCount": int,
    },
    total=False,
)

CommitDiffSourceCodeTypeOutputTypeDef = TypedDict(
    "CommitDiffSourceCodeTypeOutputTypeDef",
    {
        "SourceCommit": str,
        "DestinationCommit": str,
        "MergeBaseCommit": str,
    },
    total=False,
)

CommitDiffSourceCodeTypeTypeDef = TypedDict(
    "CommitDiffSourceCodeTypeTypeDef",
    {
        "SourceCommit": str,
        "DestinationCommit": str,
        "MergeBaseCommit": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

DescribeCodeReviewRequestRequestTypeDef = TypedDict(
    "DescribeCodeReviewRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
    },
)

_RequiredDescribeRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
    },
)
_OptionalDescribeRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRecommendationFeedbackRequestRequestTypeDef",
    {
        "UserId": str,
    },
    total=False,
)

class DescribeRecommendationFeedbackRequestRequestTypeDef(
    _RequiredDescribeRecommendationFeedbackRequestRequestTypeDef,
    _OptionalDescribeRecommendationFeedbackRequestRequestTypeDef,
):
    pass

RecommendationFeedbackTypeDef = TypedDict(
    "RecommendationFeedbackTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "Reactions": List[ReactionType],
        "UserId": str,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
    },
    total=False,
)

DescribeRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "DescribeRepositoryAssociationRequestRequestTypeDef",
    {
        "AssociationArn": str,
    },
)

DisassociateRepositoryRequestRequestTypeDef = TypedDict(
    "DisassociateRepositoryRequestRequestTypeDef",
    {
        "AssociationArn": str,
    },
)

EventInfoOutputTypeDef = TypedDict(
    "EventInfoOutputTypeDef",
    {
        "Name": str,
        "State": str,
    },
    total=False,
)

EventInfoTypeDef = TypedDict(
    "EventInfoTypeDef",
    {
        "Name": str,
        "State": str,
    },
    total=False,
)

KMSKeyDetailsOutputTypeDef = TypedDict(
    "KMSKeyDetailsOutputTypeDef",
    {
        "KMSKeyId": str,
        "EncryptionOption": EncryptionOptionType,
    },
    total=False,
)

_RequiredListCodeReviewsRequestRequestTypeDef = TypedDict(
    "_RequiredListCodeReviewsRequestRequestTypeDef",
    {
        "Type": TypeType,
    },
)
_OptionalListCodeReviewsRequestRequestTypeDef = TypedDict(
    "_OptionalListCodeReviewsRequestRequestTypeDef",
    {
        "ProviderTypes": Sequence[ProviderTypeType],
        "States": Sequence[JobStateType],
        "RepositoryNames": Sequence[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCodeReviewsRequestRequestTypeDef(
    _RequiredListCodeReviewsRequestRequestTypeDef, _OptionalListCodeReviewsRequestRequestTypeDef
):
    pass

_RequiredListRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredListRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
    },
)
_OptionalListRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalListRecommendationFeedbackRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "UserIds": Sequence[str],
        "RecommendationIds": Sequence[str],
    },
    total=False,
)

class ListRecommendationFeedbackRequestRequestTypeDef(
    _RequiredListRecommendationFeedbackRequestRequestTypeDef,
    _OptionalListRecommendationFeedbackRequestRequestTypeDef,
):
    pass

RecommendationFeedbackSummaryTypeDef = TypedDict(
    "RecommendationFeedbackSummaryTypeDef",
    {
        "RecommendationId": str,
        "Reactions": List[ReactionType],
        "UserId": str,
    },
    total=False,
)

_RequiredListRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredListRecommendationsRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
    },
)
_OptionalListRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalListRecommendationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRecommendationsRequestRequestTypeDef(
    _RequiredListRecommendationsRequestRequestTypeDef,
    _OptionalListRecommendationsRequestRequestTypeDef,
):
    pass

ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateTypeDef = TypedDict(
    "ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateTypeDef",
    {
        "ProviderTypes": Sequence[ProviderTypeType],
        "States": Sequence[RepositoryAssociationStateType],
        "Names": Sequence[str],
        "Owners": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListRepositoryAssociationsRequestRequestTypeDef = TypedDict(
    "ListRepositoryAssociationsRequestRequestTypeDef",
    {
        "ProviderTypes": Sequence[ProviderTypeType],
        "States": Sequence[RepositoryAssociationStateType],
        "Names": Sequence[str],
        "Owners": Sequence[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

RepositoryAssociationSummaryTypeDef = TypedDict(
    "RepositoryAssociationSummaryTypeDef",
    {
        "AssociationArn": str,
        "ConnectionArn": str,
        "LastUpdatedTimeStamp": datetime,
        "AssociationId": str,
        "Name": str,
        "Owner": str,
        "ProviderType": ProviderTypeType,
        "State": RepositoryAssociationStateType,
    },
    total=False,
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

PutRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "PutRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "Reactions": Sequence[ReactionType],
    },
)

RuleMetadataTypeDef = TypedDict(
    "RuleMetadataTypeDef",
    {
        "RuleId": str,
        "RuleName": str,
        "ShortDescription": str,
        "LongDescription": str,
        "RuleTags": List[str],
    },
    total=False,
)

RepositoryHeadSourceCodeTypeTypeDef = TypedDict(
    "RepositoryHeadSourceCodeTypeTypeDef",
    {
        "BranchName": str,
    },
)

RepositoryHeadSourceCodeTypeOutputTypeDef = TypedDict(
    "RepositoryHeadSourceCodeTypeOutputTypeDef",
    {
        "BranchName": str,
    },
)

S3RepositoryTypeDef = TypedDict(
    "S3RepositoryTypeDef",
    {
        "Name": str,
        "BucketName": str,
    },
)

ThirdPartySourceRepositoryTypeDef = TypedDict(
    "ThirdPartySourceRepositoryTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "Owner": str,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "TagKeys": Sequence[str],
    },
)

S3RepositoryDetailsOutputTypeDef = TypedDict(
    "S3RepositoryDetailsOutputTypeDef",
    {
        "BucketName": str,
        "CodeArtifacts": CodeArtifactsOutputTypeDef,
    },
    total=False,
)

S3RepositoryDetailsTypeDef = TypedDict(
    "S3RepositoryDetailsTypeDef",
    {
        "BucketName": str,
        "CodeArtifacts": CodeArtifactsTypeDef,
    },
    total=False,
)

_RequiredDescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef = TypedDict(
    "_RequiredDescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef",
    {
        "CodeReviewArn": str,
    },
)
_OptionalDescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef = TypedDict(
    "_OptionalDescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef(
    _RequiredDescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef,
    _OptionalDescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef,
):
    pass

_RequiredDescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef = TypedDict(
    "_RequiredDescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef",
    {
        "AssociationArn": str,
    },
)
_OptionalDescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef = TypedDict(
    "_OptionalDescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef(
    _RequiredDescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef,
    _OptionalDescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef,
):
    pass

DescribeRecommendationFeedbackResponseTypeDef = TypedDict(
    "DescribeRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedback": RecommendationFeedbackTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestMetadataOutputTypeDef = TypedDict(
    "RequestMetadataOutputTypeDef",
    {
        "RequestId": str,
        "Requester": str,
        "EventInfo": EventInfoOutputTypeDef,
        "VendorName": VendorNameType,
    },
    total=False,
)

RequestMetadataTypeDef = TypedDict(
    "RequestMetadataTypeDef",
    {
        "RequestId": str,
        "Requester": str,
        "EventInfo": EventInfoTypeDef,
        "VendorName": VendorNameType,
    },
    total=False,
)

ListRecommendationFeedbackResponseTypeDef = TypedDict(
    "ListRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedbackSummaries": List[RecommendationFeedbackSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List[RepositoryAssociationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "FilePath": str,
        "RecommendationId": str,
        "StartLine": int,
        "EndLine": int,
        "Description": str,
        "RecommendationCategory": RecommendationCategoryType,
        "RuleMetadata": RuleMetadataTypeDef,
        "Severity": SeverityType,
    },
    total=False,
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "CodeCommit": CodeCommitRepositoryTypeDef,
        "Bitbucket": ThirdPartySourceRepositoryTypeDef,
        "GitHubEnterpriseServer": ThirdPartySourceRepositoryTypeDef,
        "S3Bucket": S3RepositoryTypeDef,
    },
    total=False,
)

RepositoryAssociationTypeDef = TypedDict(
    "RepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "AssociationArn": str,
        "ConnectionArn": str,
        "Name": str,
        "Owner": str,
        "ProviderType": ProviderTypeType,
        "State": RepositoryAssociationStateType,
        "StateReason": str,
        "LastUpdatedTimeStamp": datetime,
        "CreatedTimeStamp": datetime,
        "KMSKeyDetails": KMSKeyDetailsOutputTypeDef,
        "S3RepositoryDetails": S3RepositoryDetailsOutputTypeDef,
    },
    total=False,
)

_RequiredS3BucketRepositoryOutputTypeDef = TypedDict(
    "_RequiredS3BucketRepositoryOutputTypeDef",
    {
        "Name": str,
    },
)
_OptionalS3BucketRepositoryOutputTypeDef = TypedDict(
    "_OptionalS3BucketRepositoryOutputTypeDef",
    {
        "Details": S3RepositoryDetailsOutputTypeDef,
    },
    total=False,
)

class S3BucketRepositoryOutputTypeDef(
    _RequiredS3BucketRepositoryOutputTypeDef, _OptionalS3BucketRepositoryOutputTypeDef
):
    pass

_RequiredS3BucketRepositoryTypeDef = TypedDict(
    "_RequiredS3BucketRepositoryTypeDef",
    {
        "Name": str,
    },
)
_OptionalS3BucketRepositoryTypeDef = TypedDict(
    "_OptionalS3BucketRepositoryTypeDef",
    {
        "Details": S3RepositoryDetailsTypeDef,
    },
    total=False,
)

class S3BucketRepositoryTypeDef(
    _RequiredS3BucketRepositoryTypeDef, _OptionalS3BucketRepositoryTypeDef
):
    pass

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "RecommendationSummaries": List[RecommendationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateRepositoryRequestRequestTypeDef",
    {
        "Repository": RepositoryTypeDef,
    },
)
_OptionalAssociateRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateRepositoryRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": Mapping[str, str],
        "KMSKeyDetails": KMSKeyDetailsTypeDef,
    },
    total=False,
)

class AssociateRepositoryRequestRequestTypeDef(
    _RequiredAssociateRepositoryRequestRequestTypeDef,
    _OptionalAssociateRepositoryRequestRequestTypeDef,
):
    pass

AssociateRepositoryResponseTypeDef = TypedDict(
    "AssociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": RepositoryAssociationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoryAssociationResponseTypeDef = TypedDict(
    "DescribeRepositoryAssociationResponseTypeDef",
    {
        "RepositoryAssociation": RepositoryAssociationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateRepositoryResponseTypeDef = TypedDict(
    "DisassociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": RepositoryAssociationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceCodeTypeOutputTypeDef = TypedDict(
    "SourceCodeTypeOutputTypeDef",
    {
        "CommitDiff": CommitDiffSourceCodeTypeOutputTypeDef,
        "RepositoryHead": RepositoryHeadSourceCodeTypeOutputTypeDef,
        "BranchDiff": BranchDiffSourceCodeTypeOutputTypeDef,
        "S3BucketRepository": S3BucketRepositoryOutputTypeDef,
        "RequestMetadata": RequestMetadataOutputTypeDef,
    },
    total=False,
)

SourceCodeTypeTypeDef = TypedDict(
    "SourceCodeTypeTypeDef",
    {
        "CommitDiff": CommitDiffSourceCodeTypeTypeDef,
        "RepositoryHead": RepositoryHeadSourceCodeTypeTypeDef,
        "BranchDiff": BranchDiffSourceCodeTypeTypeDef,
        "S3BucketRepository": S3BucketRepositoryTypeDef,
        "RequestMetadata": RequestMetadataTypeDef,
    },
    total=False,
)

CodeReviewSummaryTypeDef = TypedDict(
    "CodeReviewSummaryTypeDef",
    {
        "Name": str,
        "CodeReviewArn": str,
        "RepositoryName": str,
        "Owner": str,
        "ProviderType": ProviderTypeType,
        "State": JobStateType,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
        "Type": TypeType,
        "PullRequestId": str,
        "MetricsSummary": MetricsSummaryTypeDef,
        "SourceCodeType": SourceCodeTypeOutputTypeDef,
    },
    total=False,
)

CodeReviewTypeDef = TypedDict(
    "CodeReviewTypeDef",
    {
        "Name": str,
        "CodeReviewArn": str,
        "RepositoryName": str,
        "Owner": str,
        "ProviderType": ProviderTypeType,
        "State": JobStateType,
        "StateReason": str,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
        "Type": TypeType,
        "PullRequestId": str,
        "SourceCodeType": SourceCodeTypeOutputTypeDef,
        "AssociationArn": str,
        "Metrics": MetricsTypeDef,
        "AnalysisTypes": List[AnalysisTypeType],
        "ConfigFileState": ConfigFileStateType,
    },
    total=False,
)

RepositoryAnalysisTypeDef = TypedDict(
    "RepositoryAnalysisTypeDef",
    {
        "RepositoryHead": RepositoryHeadSourceCodeTypeTypeDef,
        "SourceCodeType": SourceCodeTypeTypeDef,
    },
    total=False,
)

ListCodeReviewsResponseTypeDef = TypedDict(
    "ListCodeReviewsResponseTypeDef",
    {
        "CodeReviewSummaries": List[CodeReviewSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCodeReviewResponseTypeDef = TypedDict(
    "CreateCodeReviewResponseTypeDef",
    {
        "CodeReview": CodeReviewTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCodeReviewResponseTypeDef = TypedDict(
    "DescribeCodeReviewResponseTypeDef",
    {
        "CodeReview": CodeReviewTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCodeReviewTypeTypeDef = TypedDict(
    "_RequiredCodeReviewTypeTypeDef",
    {
        "RepositoryAnalysis": RepositoryAnalysisTypeDef,
    },
)
_OptionalCodeReviewTypeTypeDef = TypedDict(
    "_OptionalCodeReviewTypeTypeDef",
    {
        "AnalysisTypes": Sequence[AnalysisTypeType],
    },
    total=False,
)

class CodeReviewTypeTypeDef(_RequiredCodeReviewTypeTypeDef, _OptionalCodeReviewTypeTypeDef):
    pass

_RequiredCreateCodeReviewRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCodeReviewRequestRequestTypeDef",
    {
        "Name": str,
        "RepositoryAssociationArn": str,
        "Type": CodeReviewTypeTypeDef,
    },
)
_OptionalCreateCodeReviewRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCodeReviewRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateCodeReviewRequestRequestTypeDef(
    _RequiredCreateCodeReviewRequestRequestTypeDef, _OptionalCreateCodeReviewRequestRequestTypeDef
):
    pass
