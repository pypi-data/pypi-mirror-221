"""
Type annotations for wisdom service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/type_defs/)

Usage::

    ```python
    from mypy_boto3_wisdom.type_defs import AppIntegrationsConfigurationOutputTypeDef

    data: AppIntegrationsConfigurationOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AssistantStatusType,
    ContentStatusType,
    KnowledgeBaseStatusType,
    KnowledgeBaseTypeType,
    RecommendationSourceTypeType,
    RelevanceLevelType,
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
    "AppIntegrationsConfigurationOutputTypeDef",
    "AppIntegrationsConfigurationTypeDef",
    "AssistantAssociationInputDataTypeDef",
    "KnowledgeBaseAssociationDataTypeDef",
    "AssistantIntegrationConfigurationTypeDef",
    "ServerSideEncryptionConfigurationOutputTypeDef",
    "ContentDataTypeDef",
    "ContentReferenceTypeDef",
    "ContentSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "CreateContentRequestRequestTypeDef",
    "RenderingConfigurationTypeDef",
    "CreateSessionRequestRequestTypeDef",
    "DeleteAssistantAssociationRequestRequestTypeDef",
    "DeleteAssistantRequestRequestTypeDef",
    "DeleteContentRequestRequestTypeDef",
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    "HighlightTypeDef",
    "FilterTypeDef",
    "GetAssistantAssociationRequestRequestTypeDef",
    "GetAssistantRequestRequestTypeDef",
    "GetContentRequestRequestTypeDef",
    "GetContentSummaryRequestRequestTypeDef",
    "GetKnowledgeBaseRequestRequestTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetSessionRequestRequestTypeDef",
    "RenderingConfigurationOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssistantAssociationsRequestRequestTypeDef",
    "ListAssistantsRequestRequestTypeDef",
    "ListContentsRequestRequestTypeDef",
    "ListKnowledgeBasesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NotifyRecommendationsReceivedErrorTypeDef",
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    "QueryAssistantRequestRequestTypeDef",
    "QueryRecommendationTriggerDataTypeDef",
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "SessionSummaryTypeDef",
    "SessionIntegrationConfigurationTypeDef",
    "StartContentUploadRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContentRequestRequestTypeDef",
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "CreateAssistantAssociationRequestRequestTypeDef",
    "AssistantAssociationOutputDataTypeDef",
    "AssistantDataTypeDef",
    "AssistantSummaryTypeDef",
    "CreateContentResponseTypeDef",
    "GetContentResponseTypeDef",
    "GetContentSummaryResponseTypeDef",
    "ListContentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SearchContentResponseTypeDef",
    "StartContentUploadResponseTypeDef",
    "UpdateContentResponseTypeDef",
    "CreateAssistantRequestRequestTypeDef",
    "DocumentTextTypeDef",
    "SearchExpressionTypeDef",
    "ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef",
    "ListAssistantsRequestListAssistantsPaginateTypeDef",
    "ListContentsRequestListContentsPaginateTypeDef",
    "ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef",
    "QueryAssistantRequestQueryAssistantPaginateTypeDef",
    "NotifyRecommendationsReceivedResponseTypeDef",
    "RecommendationTriggerDataTypeDef",
    "SearchSessionsResponseTypeDef",
    "SessionDataTypeDef",
    "KnowledgeBaseDataTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "CreateKnowledgeBaseRequestRequestTypeDef",
    "AssistantAssociationDataTypeDef",
    "AssistantAssociationSummaryTypeDef",
    "CreateAssistantResponseTypeDef",
    "GetAssistantResponseTypeDef",
    "ListAssistantsResponseTypeDef",
    "DocumentTypeDef",
    "SearchContentRequestRequestTypeDef",
    "SearchContentRequestSearchContentPaginateTypeDef",
    "SearchSessionsRequestRequestTypeDef",
    "SearchSessionsRequestSearchSessionsPaginateTypeDef",
    "RecommendationTriggerTypeDef",
    "CreateSessionResponseTypeDef",
    "GetSessionResponseTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "CreateAssistantAssociationResponseTypeDef",
    "GetAssistantAssociationResponseTypeDef",
    "ListAssistantAssociationsResponseTypeDef",
    "RecommendationDataTypeDef",
    "ResultDataTypeDef",
    "GetRecommendationsResponseTypeDef",
    "QueryAssistantResponseTypeDef",
)

AppIntegrationsConfigurationOutputTypeDef = TypedDict(
    "AppIntegrationsConfigurationOutputTypeDef",
    {
        "appIntegrationArn": str,
        "objectFields": List[str],
    },
)

_RequiredAppIntegrationsConfigurationTypeDef = TypedDict(
    "_RequiredAppIntegrationsConfigurationTypeDef",
    {
        "appIntegrationArn": str,
    },
)
_OptionalAppIntegrationsConfigurationTypeDef = TypedDict(
    "_OptionalAppIntegrationsConfigurationTypeDef",
    {
        "objectFields": Sequence[str],
    },
    total=False,
)


class AppIntegrationsConfigurationTypeDef(
    _RequiredAppIntegrationsConfigurationTypeDef, _OptionalAppIntegrationsConfigurationTypeDef
):
    pass


AssistantAssociationInputDataTypeDef = TypedDict(
    "AssistantAssociationInputDataTypeDef",
    {
        "knowledgeBaseId": str,
    },
    total=False,
)

KnowledgeBaseAssociationDataTypeDef = TypedDict(
    "KnowledgeBaseAssociationDataTypeDef",
    {
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
    },
)

AssistantIntegrationConfigurationTypeDef = TypedDict(
    "AssistantIntegrationConfigurationTypeDef",
    {
        "topicIntegrationArn": str,
    },
)

ServerSideEncryptionConfigurationOutputTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationOutputTypeDef",
    {
        "kmsKeyId": str,
    },
)

ContentDataTypeDef = TypedDict(
    "ContentDataTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "contentType": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "linkOutUri": str,
        "metadata": Dict[str, str],
        "name": str,
        "revisionId": str,
        "status": ContentStatusType,
        "tags": Dict[str, str],
        "title": str,
        "url": str,
        "urlExpiry": datetime,
    },
)

ContentReferenceTypeDef = TypedDict(
    "ContentReferenceTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
    },
)

ContentSummaryTypeDef = TypedDict(
    "ContentSummaryTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "contentType": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "metadata": Dict[str, str],
        "name": str,
        "revisionId": str,
        "status": ContentStatusType,
        "tags": Dict[str, str],
        "title": str,
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

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

_RequiredCreateContentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContentRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "uploadId": str,
    },
)
_OptionalCreateContentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContentRequestRequestTypeDef",
    {
        "clientToken": str,
        "metadata": Mapping[str, str],
        "overrideLinkOutUri": str,
        "tags": Mapping[str, str],
        "title": str,
    },
    total=False,
)


class CreateContentRequestRequestTypeDef(
    _RequiredCreateContentRequestRequestTypeDef, _OptionalCreateContentRequestRequestTypeDef
):
    pass


RenderingConfigurationTypeDef = TypedDict(
    "RenderingConfigurationTypeDef",
    {
        "templateUri": str,
    },
    total=False,
)

_RequiredCreateSessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "name": str,
    },
)
_OptionalCreateSessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSessionRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateSessionRequestRequestTypeDef(
    _RequiredCreateSessionRequestRequestTypeDef, _OptionalCreateSessionRequestRequestTypeDef
):
    pass


DeleteAssistantAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssistantAssociationRequestRequestTypeDef",
    {
        "assistantAssociationId": str,
        "assistantId": str,
    },
)

DeleteAssistantRequestRequestTypeDef = TypedDict(
    "DeleteAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)

DeleteContentRequestRequestTypeDef = TypedDict(
    "DeleteContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

DeleteKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

HighlightTypeDef = TypedDict(
    "HighlightTypeDef",
    {
        "beginOffsetInclusive": int,
        "endOffsetExclusive": int,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "field": Literal["NAME"],
        "operator": Literal["EQUALS"],
        "value": str,
    },
)

GetAssistantAssociationRequestRequestTypeDef = TypedDict(
    "GetAssistantAssociationRequestRequestTypeDef",
    {
        "assistantAssociationId": str,
        "assistantId": str,
    },
)

GetAssistantRequestRequestTypeDef = TypedDict(
    "GetAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)

GetContentRequestRequestTypeDef = TypedDict(
    "GetContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

GetContentSummaryRequestRequestTypeDef = TypedDict(
    "GetContentSummaryRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

GetKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "GetKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

_RequiredGetRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetRecommendationsRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
    },
)
_OptionalGetRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetRecommendationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "waitTimeSeconds": int,
    },
    total=False,
)


class GetRecommendationsRequestRequestTypeDef(
    _RequiredGetRecommendationsRequestRequestTypeDef,
    _OptionalGetRecommendationsRequestRequestTypeDef,
):
    pass


GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
    },
)

RenderingConfigurationOutputTypeDef = TypedDict(
    "RenderingConfigurationOutputTypeDef",
    {
        "templateUri": str,
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

_RequiredListAssistantAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssistantAssociationsRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)
_OptionalListAssistantAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssistantAssociationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListAssistantAssociationsRequestRequestTypeDef(
    _RequiredListAssistantAssociationsRequestRequestTypeDef,
    _OptionalListAssistantAssociationsRequestRequestTypeDef,
):
    pass


ListAssistantsRequestRequestTypeDef = TypedDict(
    "ListAssistantsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListContentsRequestRequestTypeDef = TypedDict(
    "_RequiredListContentsRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
_OptionalListContentsRequestRequestTypeDef = TypedDict(
    "_OptionalListContentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListContentsRequestRequestTypeDef(
    _RequiredListContentsRequestRequestTypeDef, _OptionalListContentsRequestRequestTypeDef
):
    pass


ListKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "ListKnowledgeBasesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

NotifyRecommendationsReceivedErrorTypeDef = TypedDict(
    "NotifyRecommendationsReceivedErrorTypeDef",
    {
        "message": str,
        "recommendationId": str,
    },
)

NotifyRecommendationsReceivedRequestRequestTypeDef = TypedDict(
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    {
        "assistantId": str,
        "recommendationIds": Sequence[str],
        "sessionId": str,
    },
)

_RequiredQueryAssistantRequestRequestTypeDef = TypedDict(
    "_RequiredQueryAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
        "queryText": str,
    },
)
_OptionalQueryAssistantRequestRequestTypeDef = TypedDict(
    "_OptionalQueryAssistantRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class QueryAssistantRequestRequestTypeDef(
    _RequiredQueryAssistantRequestRequestTypeDef, _OptionalQueryAssistantRequestRequestTypeDef
):
    pass


QueryRecommendationTriggerDataTypeDef = TypedDict(
    "QueryRecommendationTriggerDataTypeDef",
    {
        "text": str,
    },
)

RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

SessionSummaryTypeDef = TypedDict(
    "SessionSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "sessionArn": str,
        "sessionId": str,
    },
)

SessionIntegrationConfigurationTypeDef = TypedDict(
    "SessionIntegrationConfigurationTypeDef",
    {
        "topicIntegrationArn": str,
    },
)

StartContentUploadRequestRequestTypeDef = TypedDict(
    "StartContentUploadRequestRequestTypeDef",
    {
        "contentType": str,
        "knowledgeBaseId": str,
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

_RequiredUpdateContentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)
_OptionalUpdateContentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContentRequestRequestTypeDef",
    {
        "metadata": Mapping[str, str],
        "overrideLinkOutUri": str,
        "removeOverrideLinkOutUri": bool,
        "revisionId": str,
        "title": str,
        "uploadId": str,
    },
    total=False,
)


class UpdateContentRequestRequestTypeDef(
    _RequiredUpdateContentRequestRequestTypeDef, _OptionalUpdateContentRequestRequestTypeDef
):
    pass


UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "templateUri": str,
    },
)

SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "appIntegrations": AppIntegrationsConfigurationOutputTypeDef,
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "appIntegrations": AppIntegrationsConfigurationTypeDef,
    },
    total=False,
)

_RequiredCreateAssistantAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssistantAssociationRequestRequestTypeDef",
    {
        "assistantId": str,
        "association": AssistantAssociationInputDataTypeDef,
        "associationType": Literal["KNOWLEDGE_BASE"],
    },
)
_OptionalCreateAssistantAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssistantAssociationRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateAssistantAssociationRequestRequestTypeDef(
    _RequiredCreateAssistantAssociationRequestRequestTypeDef,
    _OptionalCreateAssistantAssociationRequestRequestTypeDef,
):
    pass


AssistantAssociationOutputDataTypeDef = TypedDict(
    "AssistantAssociationOutputDataTypeDef",
    {
        "knowledgeBaseAssociation": KnowledgeBaseAssociationDataTypeDef,
    },
)

AssistantDataTypeDef = TypedDict(
    "AssistantDataTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "description": str,
        "integrationConfiguration": AssistantIntegrationConfigurationTypeDef,
        "name": str,
        "serverSideEncryptionConfiguration": ServerSideEncryptionConfigurationOutputTypeDef,
        "status": AssistantStatusType,
        "tags": Dict[str, str],
        "type": Literal["AGENT"],
    },
)

AssistantSummaryTypeDef = TypedDict(
    "AssistantSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "description": str,
        "integrationConfiguration": AssistantIntegrationConfigurationTypeDef,
        "name": str,
        "serverSideEncryptionConfiguration": ServerSideEncryptionConfigurationOutputTypeDef,
        "status": AssistantStatusType,
        "tags": Dict[str, str],
        "type": Literal["AGENT"],
    },
)

CreateContentResponseTypeDef = TypedDict(
    "CreateContentResponseTypeDef",
    {
        "content": ContentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetContentResponseTypeDef = TypedDict(
    "GetContentResponseTypeDef",
    {
        "content": ContentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetContentSummaryResponseTypeDef = TypedDict(
    "GetContentSummaryResponseTypeDef",
    {
        "contentSummary": ContentSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListContentsResponseTypeDef = TypedDict(
    "ListContentsResponseTypeDef",
    {
        "contentSummaries": List[ContentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SearchContentResponseTypeDef = TypedDict(
    "SearchContentResponseTypeDef",
    {
        "contentSummaries": List[ContentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartContentUploadResponseTypeDef = TypedDict(
    "StartContentUploadResponseTypeDef",
    {
        "headersToInclude": Dict[str, str],
        "uploadId": str,
        "url": str,
        "urlExpiry": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateContentResponseTypeDef = TypedDict(
    "UpdateContentResponseTypeDef",
    {
        "content": ContentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateAssistantRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssistantRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["AGENT"],
    },
)
_OptionalCreateAssistantRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssistantRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "serverSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateAssistantRequestRequestTypeDef(
    _RequiredCreateAssistantRequestRequestTypeDef, _OptionalCreateAssistantRequestRequestTypeDef
):
    pass


DocumentTextTypeDef = TypedDict(
    "DocumentTextTypeDef",
    {
        "highlights": List[HighlightTypeDef],
        "text": str,
    },
)

SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
    },
)

_RequiredListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef = TypedDict(
    "_RequiredListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef",
    {
        "assistantId": str,
    },
)
_OptionalListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef = TypedDict(
    "_OptionalListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef(
    _RequiredListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef,
    _OptionalListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef,
):
    pass


ListAssistantsRequestListAssistantsPaginateTypeDef = TypedDict(
    "ListAssistantsRequestListAssistantsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListContentsRequestListContentsPaginateTypeDef = TypedDict(
    "_RequiredListContentsRequestListContentsPaginateTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
_OptionalListContentsRequestListContentsPaginateTypeDef = TypedDict(
    "_OptionalListContentsRequestListContentsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListContentsRequestListContentsPaginateTypeDef(
    _RequiredListContentsRequestListContentsPaginateTypeDef,
    _OptionalListContentsRequestListContentsPaginateTypeDef,
):
    pass


ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef = TypedDict(
    "ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredQueryAssistantRequestQueryAssistantPaginateTypeDef = TypedDict(
    "_RequiredQueryAssistantRequestQueryAssistantPaginateTypeDef",
    {
        "assistantId": str,
        "queryText": str,
    },
)
_OptionalQueryAssistantRequestQueryAssistantPaginateTypeDef = TypedDict(
    "_OptionalQueryAssistantRequestQueryAssistantPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class QueryAssistantRequestQueryAssistantPaginateTypeDef(
    _RequiredQueryAssistantRequestQueryAssistantPaginateTypeDef,
    _OptionalQueryAssistantRequestQueryAssistantPaginateTypeDef,
):
    pass


NotifyRecommendationsReceivedResponseTypeDef = TypedDict(
    "NotifyRecommendationsReceivedResponseTypeDef",
    {
        "errors": List[NotifyRecommendationsReceivedErrorTypeDef],
        "recommendationIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RecommendationTriggerDataTypeDef = TypedDict(
    "RecommendationTriggerDataTypeDef",
    {
        "query": QueryRecommendationTriggerDataTypeDef,
    },
)

SearchSessionsResponseTypeDef = TypedDict(
    "SearchSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessionSummaries": List[SessionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SessionDataTypeDef = TypedDict(
    "SessionDataTypeDef",
    {
        "description": str,
        "integrationConfiguration": SessionIntegrationConfigurationTypeDef,
        "name": str,
        "sessionArn": str,
        "sessionId": str,
        "tags": Dict[str, str],
    },
)

KnowledgeBaseDataTypeDef = TypedDict(
    "KnowledgeBaseDataTypeDef",
    {
        "description": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "lastContentModificationTime": datetime,
        "name": str,
        "renderingConfiguration": RenderingConfigurationOutputTypeDef,
        "serverSideEncryptionConfiguration": ServerSideEncryptionConfigurationOutputTypeDef,
        "sourceConfiguration": SourceConfigurationOutputTypeDef,
        "status": KnowledgeBaseStatusType,
        "tags": Dict[str, str],
    },
)

KnowledgeBaseSummaryTypeDef = TypedDict(
    "KnowledgeBaseSummaryTypeDef",
    {
        "description": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "renderingConfiguration": RenderingConfigurationOutputTypeDef,
        "serverSideEncryptionConfiguration": ServerSideEncryptionConfigurationOutputTypeDef,
        "sourceConfiguration": SourceConfigurationOutputTypeDef,
        "status": KnowledgeBaseStatusType,
        "tags": Dict[str, str],
    },
)

_RequiredCreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
    },
)
_OptionalCreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKnowledgeBaseRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "renderingConfiguration": RenderingConfigurationTypeDef,
        "serverSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
        "sourceConfiguration": SourceConfigurationTypeDef,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateKnowledgeBaseRequestRequestTypeDef(
    _RequiredCreateKnowledgeBaseRequestRequestTypeDef,
    _OptionalCreateKnowledgeBaseRequestRequestTypeDef,
):
    pass


AssistantAssociationDataTypeDef = TypedDict(
    "AssistantAssociationDataTypeDef",
    {
        "assistantArn": str,
        "assistantAssociationArn": str,
        "assistantAssociationId": str,
        "assistantId": str,
        "associationData": AssistantAssociationOutputDataTypeDef,
        "associationType": Literal["KNOWLEDGE_BASE"],
        "tags": Dict[str, str],
    },
)

AssistantAssociationSummaryTypeDef = TypedDict(
    "AssistantAssociationSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantAssociationArn": str,
        "assistantAssociationId": str,
        "assistantId": str,
        "associationData": AssistantAssociationOutputDataTypeDef,
        "associationType": Literal["KNOWLEDGE_BASE"],
        "tags": Dict[str, str],
    },
)

CreateAssistantResponseTypeDef = TypedDict(
    "CreateAssistantResponseTypeDef",
    {
        "assistant": AssistantDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAssistantResponseTypeDef = TypedDict(
    "GetAssistantResponseTypeDef",
    {
        "assistant": AssistantDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAssistantsResponseTypeDef = TypedDict(
    "ListAssistantsResponseTypeDef",
    {
        "assistantSummaries": List[AssistantSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "contentReference": ContentReferenceTypeDef,
        "excerpt": DocumentTextTypeDef,
        "title": DocumentTextTypeDef,
    },
)

_RequiredSearchContentRequestRequestTypeDef = TypedDict(
    "_RequiredSearchContentRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": SearchExpressionTypeDef,
    },
)
_OptionalSearchContentRequestRequestTypeDef = TypedDict(
    "_OptionalSearchContentRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class SearchContentRequestRequestTypeDef(
    _RequiredSearchContentRequestRequestTypeDef, _OptionalSearchContentRequestRequestTypeDef
):
    pass


_RequiredSearchContentRequestSearchContentPaginateTypeDef = TypedDict(
    "_RequiredSearchContentRequestSearchContentPaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": SearchExpressionTypeDef,
    },
)
_OptionalSearchContentRequestSearchContentPaginateTypeDef = TypedDict(
    "_OptionalSearchContentRequestSearchContentPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SearchContentRequestSearchContentPaginateTypeDef(
    _RequiredSearchContentRequestSearchContentPaginateTypeDef,
    _OptionalSearchContentRequestSearchContentPaginateTypeDef,
):
    pass


_RequiredSearchSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchSessionsRequestRequestTypeDef",
    {
        "assistantId": str,
        "searchExpression": SearchExpressionTypeDef,
    },
)
_OptionalSearchSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchSessionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class SearchSessionsRequestRequestTypeDef(
    _RequiredSearchSessionsRequestRequestTypeDef, _OptionalSearchSessionsRequestRequestTypeDef
):
    pass


_RequiredSearchSessionsRequestSearchSessionsPaginateTypeDef = TypedDict(
    "_RequiredSearchSessionsRequestSearchSessionsPaginateTypeDef",
    {
        "assistantId": str,
        "searchExpression": SearchExpressionTypeDef,
    },
)
_OptionalSearchSessionsRequestSearchSessionsPaginateTypeDef = TypedDict(
    "_OptionalSearchSessionsRequestSearchSessionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SearchSessionsRequestSearchSessionsPaginateTypeDef(
    _RequiredSearchSessionsRequestSearchSessionsPaginateTypeDef,
    _OptionalSearchSessionsRequestSearchSessionsPaginateTypeDef,
):
    pass


RecommendationTriggerTypeDef = TypedDict(
    "RecommendationTriggerTypeDef",
    {
        "data": RecommendationTriggerDataTypeDef,
        "id": str,
        "recommendationIds": List[str],
        "source": RecommendationSourceTypeType,
        "type": Literal["QUERY"],
    },
)

CreateSessionResponseTypeDef = TypedDict(
    "CreateSessionResponseTypeDef",
    {
        "session": SessionDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "session": SessionDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateKnowledgeBaseResponseTypeDef = TypedDict(
    "CreateKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetKnowledgeBaseResponseTypeDef = TypedDict(
    "GetKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateKnowledgeBaseTemplateUriResponseTypeDef = TypedDict(
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListKnowledgeBasesResponseTypeDef = TypedDict(
    "ListKnowledgeBasesResponseTypeDef",
    {
        "knowledgeBaseSummaries": List[KnowledgeBaseSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAssistantAssociationResponseTypeDef = TypedDict(
    "CreateAssistantAssociationResponseTypeDef",
    {
        "assistantAssociation": AssistantAssociationDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAssistantAssociationResponseTypeDef = TypedDict(
    "GetAssistantAssociationResponseTypeDef",
    {
        "assistantAssociation": AssistantAssociationDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAssistantAssociationsResponseTypeDef = TypedDict(
    "ListAssistantAssociationsResponseTypeDef",
    {
        "assistantAssociationSummaries": List[AssistantAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RecommendationDataTypeDef = TypedDict(
    "RecommendationDataTypeDef",
    {
        "document": DocumentTypeDef,
        "recommendationId": str,
        "relevanceLevel": RelevanceLevelType,
        "relevanceScore": float,
        "type": Literal["KNOWLEDGE_CONTENT"],
    },
)

ResultDataTypeDef = TypedDict(
    "ResultDataTypeDef",
    {
        "document": DocumentTypeDef,
        "relevanceScore": float,
        "resultId": str,
    },
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "recommendations": List[RecommendationDataTypeDef],
        "triggers": List[RecommendationTriggerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

QueryAssistantResponseTypeDef = TypedDict(
    "QueryAssistantResponseTypeDef",
    {
        "nextToken": str,
        "results": List[ResultDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
