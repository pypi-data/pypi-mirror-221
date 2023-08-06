"""
Type annotations for cloudsearch service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudsearch.type_defs import OptionStatusTypeDef

    data: OptionStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AlgorithmicStemmingType,
    AnalysisSchemeLanguageType,
    IndexFieldTypeType,
    OptionStateType,
    PartitionInstanceTypeType,
    SuggesterFuzzyMatchingType,
    TLSSecurityPolicyType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "OptionStatusTypeDef",
    "AnalysisOptionsOutputTypeDef",
    "AnalysisOptionsTypeDef",
    "BuildSuggestersRequestRequestTypeDef",
    "BuildSuggestersResponseTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "DateArrayOptionsOutputTypeDef",
    "DateArrayOptionsTypeDef",
    "DateOptionsOutputTypeDef",
    "DateOptionsTypeDef",
    "ExpressionTypeDef",
    "DeleteAnalysisSchemeRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteExpressionRequestRequestTypeDef",
    "DeleteIndexFieldRequestRequestTypeDef",
    "DeleteSuggesterRequestRequestTypeDef",
    "DescribeAnalysisSchemesRequestRequestTypeDef",
    "DescribeAvailabilityOptionsRequestRequestTypeDef",
    "DescribeDomainEndpointOptionsRequestRequestTypeDef",
    "DescribeDomainsRequestRequestTypeDef",
    "DescribeExpressionsRequestRequestTypeDef",
    "DescribeIndexFieldsRequestRequestTypeDef",
    "DescribeScalingParametersRequestRequestTypeDef",
    "DescribeServiceAccessPoliciesRequestRequestTypeDef",
    "DescribeSuggestersRequestRequestTypeDef",
    "DocumentSuggesterOptionsOutputTypeDef",
    "DocumentSuggesterOptionsTypeDef",
    "DomainEndpointOptionsOutputTypeDef",
    "DomainEndpointOptionsTypeDef",
    "LimitsTypeDef",
    "ServiceEndpointTypeDef",
    "DoubleArrayOptionsOutputTypeDef",
    "DoubleArrayOptionsTypeDef",
    "DoubleOptionsOutputTypeDef",
    "DoubleOptionsTypeDef",
    "ExpressionOutputTypeDef",
    "IndexDocumentsRequestRequestTypeDef",
    "IndexDocumentsResponseTypeDef",
    "IntArrayOptionsOutputTypeDef",
    "IntOptionsOutputTypeDef",
    "LatLonOptionsOutputTypeDef",
    "LiteralArrayOptionsOutputTypeDef",
    "LiteralOptionsOutputTypeDef",
    "TextArrayOptionsOutputTypeDef",
    "TextOptionsOutputTypeDef",
    "IntArrayOptionsTypeDef",
    "IntOptionsTypeDef",
    "LatLonOptionsTypeDef",
    "LiteralArrayOptionsTypeDef",
    "LiteralOptionsTypeDef",
    "TextArrayOptionsTypeDef",
    "TextOptionsTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingParametersOutputTypeDef",
    "ScalingParametersTypeDef",
    "UpdateAvailabilityOptionsRequestRequestTypeDef",
    "UpdateServiceAccessPoliciesRequestRequestTypeDef",
    "AccessPoliciesStatusTypeDef",
    "AvailabilityOptionsStatusTypeDef",
    "AnalysisSchemeOutputTypeDef",
    "AnalysisSchemeTypeDef",
    "DefineExpressionRequestRequestTypeDef",
    "SuggesterOutputTypeDef",
    "SuggesterTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "UpdateDomainEndpointOptionsRequestRequestTypeDef",
    "DomainStatusTypeDef",
    "ExpressionStatusTypeDef",
    "IndexFieldOutputTypeDef",
    "IndexFieldTypeDef",
    "ScalingParametersStatusTypeDef",
    "UpdateScalingParametersRequestRequestTypeDef",
    "DescribeServiceAccessPoliciesResponseTypeDef",
    "UpdateServiceAccessPoliciesResponseTypeDef",
    "DescribeAvailabilityOptionsResponseTypeDef",
    "UpdateAvailabilityOptionsResponseTypeDef",
    "AnalysisSchemeStatusTypeDef",
    "DefineAnalysisSchemeRequestRequestTypeDef",
    "SuggesterStatusTypeDef",
    "DefineSuggesterRequestRequestTypeDef",
    "DescribeDomainEndpointOptionsResponseTypeDef",
    "UpdateDomainEndpointOptionsResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DefineExpressionResponseTypeDef",
    "DeleteExpressionResponseTypeDef",
    "DescribeExpressionsResponseTypeDef",
    "IndexFieldStatusTypeDef",
    "DefineIndexFieldRequestRequestTypeDef",
    "DescribeScalingParametersResponseTypeDef",
    "UpdateScalingParametersResponseTypeDef",
    "DefineAnalysisSchemeResponseTypeDef",
    "DeleteAnalysisSchemeResponseTypeDef",
    "DescribeAnalysisSchemesResponseTypeDef",
    "DefineSuggesterResponseTypeDef",
    "DeleteSuggesterResponseTypeDef",
    "DescribeSuggestersResponseTypeDef",
    "DefineIndexFieldResponseTypeDef",
    "DeleteIndexFieldResponseTypeDef",
    "DescribeIndexFieldsResponseTypeDef",
)

_RequiredOptionStatusTypeDef = TypedDict(
    "_RequiredOptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": OptionStateType,
    },
)
_OptionalOptionStatusTypeDef = TypedDict(
    "_OptionalOptionStatusTypeDef",
    {
        "UpdateVersion": int,
        "PendingDeletion": bool,
    },
    total=False,
)

class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, _OptionalOptionStatusTypeDef):
    pass

AnalysisOptionsOutputTypeDef = TypedDict(
    "AnalysisOptionsOutputTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": AlgorithmicStemmingType,
    },
    total=False,
)

AnalysisOptionsTypeDef = TypedDict(
    "AnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": AlgorithmicStemmingType,
    },
    total=False,
)

BuildSuggestersRequestRequestTypeDef = TypedDict(
    "BuildSuggestersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

BuildSuggestersResponseTypeDef = TypedDict(
    "BuildSuggestersResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DateArrayOptionsOutputTypeDef = TypedDict(
    "DateArrayOptionsOutputTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DateArrayOptionsTypeDef = TypedDict(
    "DateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DateOptionsOutputTypeDef = TypedDict(
    "DateOptionsOutputTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

DateOptionsTypeDef = TypedDict(
    "DateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "ExpressionName": str,
        "ExpressionValue": str,
    },
)

DeleteAnalysisSchemeRequestRequestTypeDef = TypedDict(
    "DeleteAnalysisSchemeRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisSchemeName": str,
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteExpressionRequestRequestTypeDef = TypedDict(
    "DeleteExpressionRequestRequestTypeDef",
    {
        "DomainName": str,
        "ExpressionName": str,
    },
)

DeleteIndexFieldRequestRequestTypeDef = TypedDict(
    "DeleteIndexFieldRequestRequestTypeDef",
    {
        "DomainName": str,
        "IndexFieldName": str,
    },
)

DeleteSuggesterRequestRequestTypeDef = TypedDict(
    "DeleteSuggesterRequestRequestTypeDef",
    {
        "DomainName": str,
        "SuggesterName": str,
    },
)

_RequiredDescribeAnalysisSchemesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAnalysisSchemesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeAnalysisSchemesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAnalysisSchemesRequestRequestTypeDef",
    {
        "AnalysisSchemeNames": Sequence[str],
        "Deployed": bool,
    },
    total=False,
)

class DescribeAnalysisSchemesRequestRequestTypeDef(
    _RequiredDescribeAnalysisSchemesRequestRequestTypeDef,
    _OptionalDescribeAnalysisSchemesRequestRequestTypeDef,
):
    pass

_RequiredDescribeAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAvailabilityOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAvailabilityOptionsRequestRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)

class DescribeAvailabilityOptionsRequestRequestTypeDef(
    _RequiredDescribeAvailabilityOptionsRequestRequestTypeDef,
    _OptionalDescribeAvailabilityOptionsRequestRequestTypeDef,
):
    pass

_RequiredDescribeDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainEndpointOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainEndpointOptionsRequestRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)

class DescribeDomainEndpointOptionsRequestRequestTypeDef(
    _RequiredDescribeDomainEndpointOptionsRequestRequestTypeDef,
    _OptionalDescribeDomainEndpointOptionsRequestRequestTypeDef,
):
    pass

DescribeDomainsRequestRequestTypeDef = TypedDict(
    "DescribeDomainsRequestRequestTypeDef",
    {
        "DomainNames": Sequence[str],
    },
    total=False,
)

_RequiredDescribeExpressionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeExpressionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeExpressionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeExpressionsRequestRequestTypeDef",
    {
        "ExpressionNames": Sequence[str],
        "Deployed": bool,
    },
    total=False,
)

class DescribeExpressionsRequestRequestTypeDef(
    _RequiredDescribeExpressionsRequestRequestTypeDef,
    _OptionalDescribeExpressionsRequestRequestTypeDef,
):
    pass

_RequiredDescribeIndexFieldsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeIndexFieldsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeIndexFieldsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeIndexFieldsRequestRequestTypeDef",
    {
        "FieldNames": Sequence[str],
        "Deployed": bool,
    },
    total=False,
)

class DescribeIndexFieldsRequestRequestTypeDef(
    _RequiredDescribeIndexFieldsRequestRequestTypeDef,
    _OptionalDescribeIndexFieldsRequestRequestTypeDef,
):
    pass

DescribeScalingParametersRequestRequestTypeDef = TypedDict(
    "DescribeScalingParametersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

_RequiredDescribeServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeServiceAccessPoliciesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeServiceAccessPoliciesRequestRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)

class DescribeServiceAccessPoliciesRequestRequestTypeDef(
    _RequiredDescribeServiceAccessPoliciesRequestRequestTypeDef,
    _OptionalDescribeServiceAccessPoliciesRequestRequestTypeDef,
):
    pass

_RequiredDescribeSuggestersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSuggestersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeSuggestersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSuggestersRequestRequestTypeDef",
    {
        "SuggesterNames": Sequence[str],
        "Deployed": bool,
    },
    total=False,
)

class DescribeSuggestersRequestRequestTypeDef(
    _RequiredDescribeSuggestersRequestRequestTypeDef,
    _OptionalDescribeSuggestersRequestRequestTypeDef,
):
    pass

_RequiredDocumentSuggesterOptionsOutputTypeDef = TypedDict(
    "_RequiredDocumentSuggesterOptionsOutputTypeDef",
    {
        "SourceField": str,
    },
)
_OptionalDocumentSuggesterOptionsOutputTypeDef = TypedDict(
    "_OptionalDocumentSuggesterOptionsOutputTypeDef",
    {
        "FuzzyMatching": SuggesterFuzzyMatchingType,
        "SortExpression": str,
    },
    total=False,
)

class DocumentSuggesterOptionsOutputTypeDef(
    _RequiredDocumentSuggesterOptionsOutputTypeDef, _OptionalDocumentSuggesterOptionsOutputTypeDef
):
    pass

_RequiredDocumentSuggesterOptionsTypeDef = TypedDict(
    "_RequiredDocumentSuggesterOptionsTypeDef",
    {
        "SourceField": str,
    },
)
_OptionalDocumentSuggesterOptionsTypeDef = TypedDict(
    "_OptionalDocumentSuggesterOptionsTypeDef",
    {
        "FuzzyMatching": SuggesterFuzzyMatchingType,
        "SortExpression": str,
    },
    total=False,
)

class DocumentSuggesterOptionsTypeDef(
    _RequiredDocumentSuggesterOptionsTypeDef, _OptionalDocumentSuggesterOptionsTypeDef
):
    pass

DomainEndpointOptionsOutputTypeDef = TypedDict(
    "DomainEndpointOptionsOutputTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": TLSSecurityPolicyType,
    },
    total=False,
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": TLSSecurityPolicyType,
    },
    total=False,
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "MaximumReplicationCount": int,
        "MaximumPartitionCount": int,
    },
)

ServiceEndpointTypeDef = TypedDict(
    "ServiceEndpointTypeDef",
    {
        "Endpoint": str,
    },
    total=False,
)

DoubleArrayOptionsOutputTypeDef = TypedDict(
    "DoubleArrayOptionsOutputTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DoubleArrayOptionsTypeDef = TypedDict(
    "DoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DoubleOptionsOutputTypeDef = TypedDict(
    "DoubleOptionsOutputTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

DoubleOptionsTypeDef = TypedDict(
    "DoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ExpressionOutputTypeDef = TypedDict(
    "ExpressionOutputTypeDef",
    {
        "ExpressionName": str,
        "ExpressionValue": str,
    },
)

IndexDocumentsRequestRequestTypeDef = TypedDict(
    "IndexDocumentsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

IndexDocumentsResponseTypeDef = TypedDict(
    "IndexDocumentsResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntArrayOptionsOutputTypeDef = TypedDict(
    "IntArrayOptionsOutputTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

IntOptionsOutputTypeDef = TypedDict(
    "IntOptionsOutputTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LatLonOptionsOutputTypeDef = TypedDict(
    "LatLonOptionsOutputTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LiteralArrayOptionsOutputTypeDef = TypedDict(
    "LiteralArrayOptionsOutputTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

LiteralOptionsOutputTypeDef = TypedDict(
    "LiteralOptionsOutputTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

TextArrayOptionsOutputTypeDef = TypedDict(
    "TextArrayOptionsOutputTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

TextOptionsOutputTypeDef = TypedDict(
    "TextOptionsOutputTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

IntArrayOptionsTypeDef = TypedDict(
    "IntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

IntOptionsTypeDef = TypedDict(
    "IntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LatLonOptionsTypeDef = TypedDict(
    "LatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LiteralArrayOptionsTypeDef = TypedDict(
    "LiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

LiteralOptionsTypeDef = TypedDict(
    "LiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

TextArrayOptionsTypeDef = TypedDict(
    "TextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

TextOptionsTypeDef = TypedDict(
    "TextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "DomainNames": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ScalingParametersOutputTypeDef = TypedDict(
    "ScalingParametersOutputTypeDef",
    {
        "DesiredInstanceType": PartitionInstanceTypeType,
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)

ScalingParametersTypeDef = TypedDict(
    "ScalingParametersTypeDef",
    {
        "DesiredInstanceType": PartitionInstanceTypeType,
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)

UpdateAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "UpdateAvailabilityOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "MultiAZ": bool,
    },
)

UpdateServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccessPolicies": str,
    },
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef",
    {
        "Options": str,
        "Status": OptionStatusTypeDef,
    },
)

AvailabilityOptionsStatusTypeDef = TypedDict(
    "AvailabilityOptionsStatusTypeDef",
    {
        "Options": bool,
        "Status": OptionStatusTypeDef,
    },
)

_RequiredAnalysisSchemeOutputTypeDef = TypedDict(
    "_RequiredAnalysisSchemeOutputTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": AnalysisSchemeLanguageType,
    },
)
_OptionalAnalysisSchemeOutputTypeDef = TypedDict(
    "_OptionalAnalysisSchemeOutputTypeDef",
    {
        "AnalysisOptions": AnalysisOptionsOutputTypeDef,
    },
    total=False,
)

class AnalysisSchemeOutputTypeDef(
    _RequiredAnalysisSchemeOutputTypeDef, _OptionalAnalysisSchemeOutputTypeDef
):
    pass

_RequiredAnalysisSchemeTypeDef = TypedDict(
    "_RequiredAnalysisSchemeTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": AnalysisSchemeLanguageType,
    },
)
_OptionalAnalysisSchemeTypeDef = TypedDict(
    "_OptionalAnalysisSchemeTypeDef",
    {
        "AnalysisOptions": AnalysisOptionsTypeDef,
    },
    total=False,
)

class AnalysisSchemeTypeDef(_RequiredAnalysisSchemeTypeDef, _OptionalAnalysisSchemeTypeDef):
    pass

DefineExpressionRequestRequestTypeDef = TypedDict(
    "DefineExpressionRequestRequestTypeDef",
    {
        "DomainName": str,
        "Expression": ExpressionTypeDef,
    },
)

SuggesterOutputTypeDef = TypedDict(
    "SuggesterOutputTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": DocumentSuggesterOptionsOutputTypeDef,
    },
)

SuggesterTypeDef = TypedDict(
    "SuggesterTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": DocumentSuggesterOptionsTypeDef,
    },
)

DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {
        "Options": DomainEndpointOptionsOutputTypeDef,
        "Status": OptionStatusTypeDef,
    },
)

UpdateDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "DomainEndpointOptions": DomainEndpointOptionsTypeDef,
    },
)

_RequiredDomainStatusTypeDef = TypedDict(
    "_RequiredDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "RequiresIndexDocuments": bool,
    },
)
_OptionalDomainStatusTypeDef = TypedDict(
    "_OptionalDomainStatusTypeDef",
    {
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": ServiceEndpointTypeDef,
        "SearchService": ServiceEndpointTypeDef,
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": LimitsTypeDef,
    },
    total=False,
)

class DomainStatusTypeDef(_RequiredDomainStatusTypeDef, _OptionalDomainStatusTypeDef):
    pass

ExpressionStatusTypeDef = TypedDict(
    "ExpressionStatusTypeDef",
    {
        "Options": ExpressionOutputTypeDef,
        "Status": OptionStatusTypeDef,
    },
)

_RequiredIndexFieldOutputTypeDef = TypedDict(
    "_RequiredIndexFieldOutputTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": IndexFieldTypeType,
    },
)
_OptionalIndexFieldOutputTypeDef = TypedDict(
    "_OptionalIndexFieldOutputTypeDef",
    {
        "IntOptions": IntOptionsOutputTypeDef,
        "DoubleOptions": DoubleOptionsOutputTypeDef,
        "LiteralOptions": LiteralOptionsOutputTypeDef,
        "TextOptions": TextOptionsOutputTypeDef,
        "DateOptions": DateOptionsOutputTypeDef,
        "LatLonOptions": LatLonOptionsOutputTypeDef,
        "IntArrayOptions": IntArrayOptionsOutputTypeDef,
        "DoubleArrayOptions": DoubleArrayOptionsOutputTypeDef,
        "LiteralArrayOptions": LiteralArrayOptionsOutputTypeDef,
        "TextArrayOptions": TextArrayOptionsOutputTypeDef,
        "DateArrayOptions": DateArrayOptionsOutputTypeDef,
    },
    total=False,
)

class IndexFieldOutputTypeDef(_RequiredIndexFieldOutputTypeDef, _OptionalIndexFieldOutputTypeDef):
    pass

_RequiredIndexFieldTypeDef = TypedDict(
    "_RequiredIndexFieldTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": IndexFieldTypeType,
    },
)
_OptionalIndexFieldTypeDef = TypedDict(
    "_OptionalIndexFieldTypeDef",
    {
        "IntOptions": IntOptionsTypeDef,
        "DoubleOptions": DoubleOptionsTypeDef,
        "LiteralOptions": LiteralOptionsTypeDef,
        "TextOptions": TextOptionsTypeDef,
        "DateOptions": DateOptionsTypeDef,
        "LatLonOptions": LatLonOptionsTypeDef,
        "IntArrayOptions": IntArrayOptionsTypeDef,
        "DoubleArrayOptions": DoubleArrayOptionsTypeDef,
        "LiteralArrayOptions": LiteralArrayOptionsTypeDef,
        "TextArrayOptions": TextArrayOptionsTypeDef,
        "DateArrayOptions": DateArrayOptionsTypeDef,
    },
    total=False,
)

class IndexFieldTypeDef(_RequiredIndexFieldTypeDef, _OptionalIndexFieldTypeDef):
    pass

ScalingParametersStatusTypeDef = TypedDict(
    "ScalingParametersStatusTypeDef",
    {
        "Options": ScalingParametersOutputTypeDef,
        "Status": OptionStatusTypeDef,
    },
)

UpdateScalingParametersRequestRequestTypeDef = TypedDict(
    "UpdateScalingParametersRequestRequestTypeDef",
    {
        "DomainName": str,
        "ScalingParameters": ScalingParametersTypeDef,
    },
)

DescribeServiceAccessPoliciesResponseTypeDef = TypedDict(
    "DescribeServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": AccessPoliciesStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceAccessPoliciesResponseTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": AccessPoliciesStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityOptionsResponseTypeDef = TypedDict(
    "DescribeAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": AvailabilityOptionsStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAvailabilityOptionsResponseTypeDef = TypedDict(
    "UpdateAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": AvailabilityOptionsStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnalysisSchemeStatusTypeDef = TypedDict(
    "AnalysisSchemeStatusTypeDef",
    {
        "Options": AnalysisSchemeOutputTypeDef,
        "Status": OptionStatusTypeDef,
    },
)

DefineAnalysisSchemeRequestRequestTypeDef = TypedDict(
    "DefineAnalysisSchemeRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisScheme": AnalysisSchemeTypeDef,
    },
)

SuggesterStatusTypeDef = TypedDict(
    "SuggesterStatusTypeDef",
    {
        "Options": SuggesterOutputTypeDef,
        "Status": OptionStatusTypeDef,
    },
)

DefineSuggesterRequestRequestTypeDef = TypedDict(
    "DefineSuggesterRequestRequestTypeDef",
    {
        "DomainName": str,
        "Suggester": SuggesterTypeDef,
    },
)

DescribeDomainEndpointOptionsResponseTypeDef = TypedDict(
    "DescribeDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": DomainEndpointOptionsStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainEndpointOptionsResponseTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": DomainEndpointOptionsStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainStatus": DomainStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "DomainStatus": DomainStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainsResponseTypeDef = TypedDict(
    "DescribeDomainsResponseTypeDef",
    {
        "DomainStatusList": List[DomainStatusTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineExpressionResponseTypeDef = TypedDict(
    "DefineExpressionResponseTypeDef",
    {
        "Expression": ExpressionStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExpressionResponseTypeDef = TypedDict(
    "DeleteExpressionResponseTypeDef",
    {
        "Expression": ExpressionStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExpressionsResponseTypeDef = TypedDict(
    "DescribeExpressionsResponseTypeDef",
    {
        "Expressions": List[ExpressionStatusTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexFieldStatusTypeDef = TypedDict(
    "IndexFieldStatusTypeDef",
    {
        "Options": IndexFieldOutputTypeDef,
        "Status": OptionStatusTypeDef,
    },
)

DefineIndexFieldRequestRequestTypeDef = TypedDict(
    "DefineIndexFieldRequestRequestTypeDef",
    {
        "DomainName": str,
        "IndexField": IndexFieldTypeDef,
    },
)

DescribeScalingParametersResponseTypeDef = TypedDict(
    "DescribeScalingParametersResponseTypeDef",
    {
        "ScalingParameters": ScalingParametersStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateScalingParametersResponseTypeDef = TypedDict(
    "UpdateScalingParametersResponseTypeDef",
    {
        "ScalingParameters": ScalingParametersStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineAnalysisSchemeResponseTypeDef = TypedDict(
    "DefineAnalysisSchemeResponseTypeDef",
    {
        "AnalysisScheme": AnalysisSchemeStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAnalysisSchemeResponseTypeDef = TypedDict(
    "DeleteAnalysisSchemeResponseTypeDef",
    {
        "AnalysisScheme": AnalysisSchemeStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisSchemesResponseTypeDef = TypedDict(
    "DescribeAnalysisSchemesResponseTypeDef",
    {
        "AnalysisSchemes": List[AnalysisSchemeStatusTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineSuggesterResponseTypeDef = TypedDict(
    "DefineSuggesterResponseTypeDef",
    {
        "Suggester": SuggesterStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSuggesterResponseTypeDef = TypedDict(
    "DeleteSuggesterResponseTypeDef",
    {
        "Suggester": SuggesterStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSuggestersResponseTypeDef = TypedDict(
    "DescribeSuggestersResponseTypeDef",
    {
        "Suggesters": List[SuggesterStatusTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineIndexFieldResponseTypeDef = TypedDict(
    "DefineIndexFieldResponseTypeDef",
    {
        "IndexField": IndexFieldStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIndexFieldResponseTypeDef = TypedDict(
    "DeleteIndexFieldResponseTypeDef",
    {
        "IndexField": IndexFieldStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIndexFieldsResponseTypeDef = TypedDict(
    "DescribeIndexFieldsResponseTypeDef",
    {
        "IndexFields": List[IndexFieldStatusTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
