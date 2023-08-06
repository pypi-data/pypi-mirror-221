"""
Type annotations for appsync service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/type_defs/)

Usage::

    ```python
    from mypy_boto3_appsync.type_defs import CognitoUserPoolConfigOutputTypeDef

    data: CognitoUserPoolConfigOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ApiCacheStatusType,
    ApiCacheTypeType,
    ApiCachingBehaviorType,
    AssociationStatusType,
    AuthenticationTypeType,
    ConflictDetectionTypeType,
    ConflictHandlerTypeType,
    DataSourceTypeType,
    DefaultActionType,
    FieldLogLevelType,
    GraphQLApiTypeType,
    GraphQLApiVisibilityType,
    MergeTypeType,
    OutputTypeType,
    OwnershipType,
    ResolverKindType,
    SchemaStatusType,
    SourceApiAssociationStatusType,
    TypeDefinitionFormatType,
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
    "CognitoUserPoolConfigOutputTypeDef",
    "LambdaAuthorizerConfigOutputTypeDef",
    "OpenIDConnectConfigOutputTypeDef",
    "CognitoUserPoolConfigTypeDef",
    "LambdaAuthorizerConfigTypeDef",
    "OpenIDConnectConfigTypeDef",
    "ApiAssociationTypeDef",
    "ApiCacheTypeDef",
    "ApiKeyTypeDef",
    "AppSyncRuntimeOutputTypeDef",
    "AppSyncRuntimeTypeDef",
    "AssociateApiRequestRequestTypeDef",
    "SourceApiAssociationConfigTypeDef",
    "AwsIamConfigOutputTypeDef",
    "AwsIamConfigTypeDef",
    "CachingConfigOutputTypeDef",
    "CachingConfigTypeDef",
    "CodeErrorLocationTypeDef",
    "CreateApiCacheRequestRequestTypeDef",
    "CreateApiKeyRequestRequestTypeDef",
    "ElasticsearchDataSourceConfigTypeDef",
    "EventBridgeDataSourceConfigTypeDef",
    "LambdaDataSourceConfigTypeDef",
    "OpenSearchServiceDataSourceConfigTypeDef",
    "CreateDomainNameRequestRequestTypeDef",
    "DomainNameConfigTypeDef",
    "LogConfigTypeDef",
    "UserPoolConfigTypeDef",
    "PipelineConfigTypeDef",
    "CreateTypeRequestRequestTypeDef",
    "TypeTypeDef",
    "ElasticsearchDataSourceConfigOutputTypeDef",
    "EventBridgeDataSourceConfigOutputTypeDef",
    "LambdaDataSourceConfigOutputTypeDef",
    "OpenSearchServiceDataSourceConfigOutputTypeDef",
    "DeleteApiCacheRequestRequestTypeDef",
    "DeleteApiKeyRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDomainNameRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteGraphqlApiRequestRequestTypeDef",
    "DeleteResolverRequestRequestTypeDef",
    "DeleteTypeRequestRequestTypeDef",
    "DeltaSyncConfigOutputTypeDef",
    "DeltaSyncConfigTypeDef",
    "DisassociateApiRequestRequestTypeDef",
    "DisassociateMergedGraphqlApiRequestRequestTypeDef",
    "DisassociateMergedGraphqlApiResponseTypeDef",
    "DisassociateSourceGraphqlApiRequestRequestTypeDef",
    "DisassociateSourceGraphqlApiResponseTypeDef",
    "ErrorDetailTypeDef",
    "EvaluateMappingTemplateRequestRequestTypeDef",
    "FlushApiCacheRequestRequestTypeDef",
    "GetApiAssociationRequestRequestTypeDef",
    "GetApiCacheRequestRequestTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetDomainNameRequestRequestTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetGraphqlApiRequestRequestTypeDef",
    "GetIntrospectionSchemaRequestRequestTypeDef",
    "GetIntrospectionSchemaResponseTypeDef",
    "GetResolverRequestRequestTypeDef",
    "GetSchemaCreationStatusRequestRequestTypeDef",
    "GetSchemaCreationStatusResponseTypeDef",
    "GetSourceApiAssociationRequestRequestTypeDef",
    "GetTypeRequestRequestTypeDef",
    "LogConfigOutputTypeDef",
    "UserPoolConfigOutputTypeDef",
    "LambdaConflictHandlerConfigOutputTypeDef",
    "LambdaConflictHandlerConfigTypeDef",
    "ListApiKeysRequestListApiKeysPaginateTypeDef",
    "ListApiKeysRequestRequestTypeDef",
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDomainNamesRequestRequestTypeDef",
    "ListFunctionsRequestListFunctionsPaginateTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListGraphqlApisRequestListGraphqlApisPaginateTypeDef",
    "ListGraphqlApisRequestRequestTypeDef",
    "ListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef",
    "ListResolversByFunctionRequestRequestTypeDef",
    "ListResolversRequestListResolversPaginateTypeDef",
    "ListResolversRequestRequestTypeDef",
    "ListSourceApiAssociationsRequestRequestTypeDef",
    "SourceApiAssociationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypesByAssociationRequestRequestTypeDef",
    "ListTypesRequestListTypesPaginateTypeDef",
    "ListTypesRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineConfigOutputTypeDef",
    "RdsHttpEndpointConfigOutputTypeDef",
    "RdsHttpEndpointConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SourceApiAssociationConfigOutputTypeDef",
    "StartSchemaCreationRequestRequestTypeDef",
    "StartSchemaCreationResponseTypeDef",
    "StartSchemaMergeRequestRequestTypeDef",
    "StartSchemaMergeResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiCacheRequestRequestTypeDef",
    "UpdateApiKeyRequestRequestTypeDef",
    "UpdateDomainNameRequestRequestTypeDef",
    "UpdateTypeRequestRequestTypeDef",
    "AdditionalAuthenticationProviderOutputTypeDef",
    "AdditionalAuthenticationProviderTypeDef",
    "AssociateApiResponseTypeDef",
    "GetApiAssociationResponseTypeDef",
    "CreateApiCacheResponseTypeDef",
    "GetApiCacheResponseTypeDef",
    "UpdateApiCacheResponseTypeDef",
    "CreateApiKeyResponseTypeDef",
    "ListApiKeysResponseTypeDef",
    "UpdateApiKeyResponseTypeDef",
    "EvaluateCodeRequestRequestTypeDef",
    "AssociateMergedGraphqlApiRequestRequestTypeDef",
    "AssociateSourceGraphqlApiRequestRequestTypeDef",
    "UpdateSourceApiAssociationRequestRequestTypeDef",
    "AuthorizationConfigOutputTypeDef",
    "AuthorizationConfigTypeDef",
    "CodeErrorTypeDef",
    "CreateDomainNameResponseTypeDef",
    "GetDomainNameResponseTypeDef",
    "ListDomainNamesResponseTypeDef",
    "UpdateDomainNameResponseTypeDef",
    "CreateTypeResponseTypeDef",
    "GetTypeResponseTypeDef",
    "ListTypesByAssociationResponseTypeDef",
    "ListTypesResponseTypeDef",
    "UpdateTypeResponseTypeDef",
    "DynamodbDataSourceConfigOutputTypeDef",
    "DynamodbDataSourceConfigTypeDef",
    "EvaluateMappingTemplateResponseTypeDef",
    "SyncConfigOutputTypeDef",
    "SyncConfigTypeDef",
    "ListSourceApiAssociationsResponseTypeDef",
    "RelationalDatabaseDataSourceConfigOutputTypeDef",
    "RelationalDatabaseDataSourceConfigTypeDef",
    "SourceApiAssociationTypeDef",
    "GraphqlApiTypeDef",
    "CreateGraphqlApiRequestRequestTypeDef",
    "UpdateGraphqlApiRequestRequestTypeDef",
    "HttpDataSourceConfigOutputTypeDef",
    "HttpDataSourceConfigTypeDef",
    "EvaluateCodeErrorDetailTypeDef",
    "FunctionConfigurationTypeDef",
    "ResolverTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "CreateResolverRequestRequestTypeDef",
    "UpdateFunctionRequestRequestTypeDef",
    "UpdateResolverRequestRequestTypeDef",
    "AssociateMergedGraphqlApiResponseTypeDef",
    "AssociateSourceGraphqlApiResponseTypeDef",
    "GetSourceApiAssociationResponseTypeDef",
    "UpdateSourceApiAssociationResponseTypeDef",
    "CreateGraphqlApiResponseTypeDef",
    "GetGraphqlApiResponseTypeDef",
    "ListGraphqlApisResponseTypeDef",
    "UpdateGraphqlApiResponseTypeDef",
    "DataSourceTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "EvaluateCodeResponseTypeDef",
    "CreateFunctionResponseTypeDef",
    "GetFunctionResponseTypeDef",
    "ListFunctionsResponseTypeDef",
    "UpdateFunctionResponseTypeDef",
    "CreateResolverResponseTypeDef",
    "GetResolverResponseTypeDef",
    "ListResolversByFunctionResponseTypeDef",
    "ListResolversResponseTypeDef",
    "UpdateResolverResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "GetDataSourceResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "UpdateDataSourceResponseTypeDef",
)

_RequiredCognitoUserPoolConfigOutputTypeDef = TypedDict(
    "_RequiredCognitoUserPoolConfigOutputTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
    },
)
_OptionalCognitoUserPoolConfigOutputTypeDef = TypedDict(
    "_OptionalCognitoUserPoolConfigOutputTypeDef",
    {
        "appIdClientRegex": str,
    },
    total=False,
)

class CognitoUserPoolConfigOutputTypeDef(
    _RequiredCognitoUserPoolConfigOutputTypeDef, _OptionalCognitoUserPoolConfigOutputTypeDef
):
    pass

_RequiredLambdaAuthorizerConfigOutputTypeDef = TypedDict(
    "_RequiredLambdaAuthorizerConfigOutputTypeDef",
    {
        "authorizerUri": str,
    },
)
_OptionalLambdaAuthorizerConfigOutputTypeDef = TypedDict(
    "_OptionalLambdaAuthorizerConfigOutputTypeDef",
    {
        "authorizerResultTtlInSeconds": int,
        "identityValidationExpression": str,
    },
    total=False,
)

class LambdaAuthorizerConfigOutputTypeDef(
    _RequiredLambdaAuthorizerConfigOutputTypeDef, _OptionalLambdaAuthorizerConfigOutputTypeDef
):
    pass

_RequiredOpenIDConnectConfigOutputTypeDef = TypedDict(
    "_RequiredOpenIDConnectConfigOutputTypeDef",
    {
        "issuer": str,
    },
)
_OptionalOpenIDConnectConfigOutputTypeDef = TypedDict(
    "_OptionalOpenIDConnectConfigOutputTypeDef",
    {
        "clientId": str,
        "iatTTL": int,
        "authTTL": int,
    },
    total=False,
)

class OpenIDConnectConfigOutputTypeDef(
    _RequiredOpenIDConnectConfigOutputTypeDef, _OptionalOpenIDConnectConfigOutputTypeDef
):
    pass

_RequiredCognitoUserPoolConfigTypeDef = TypedDict(
    "_RequiredCognitoUserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
    },
)
_OptionalCognitoUserPoolConfigTypeDef = TypedDict(
    "_OptionalCognitoUserPoolConfigTypeDef",
    {
        "appIdClientRegex": str,
    },
    total=False,
)

class CognitoUserPoolConfigTypeDef(
    _RequiredCognitoUserPoolConfigTypeDef, _OptionalCognitoUserPoolConfigTypeDef
):
    pass

_RequiredLambdaAuthorizerConfigTypeDef = TypedDict(
    "_RequiredLambdaAuthorizerConfigTypeDef",
    {
        "authorizerUri": str,
    },
)
_OptionalLambdaAuthorizerConfigTypeDef = TypedDict(
    "_OptionalLambdaAuthorizerConfigTypeDef",
    {
        "authorizerResultTtlInSeconds": int,
        "identityValidationExpression": str,
    },
    total=False,
)

class LambdaAuthorizerConfigTypeDef(
    _RequiredLambdaAuthorizerConfigTypeDef, _OptionalLambdaAuthorizerConfigTypeDef
):
    pass

_RequiredOpenIDConnectConfigTypeDef = TypedDict(
    "_RequiredOpenIDConnectConfigTypeDef",
    {
        "issuer": str,
    },
)
_OptionalOpenIDConnectConfigTypeDef = TypedDict(
    "_OptionalOpenIDConnectConfigTypeDef",
    {
        "clientId": str,
        "iatTTL": int,
        "authTTL": int,
    },
    total=False,
)

class OpenIDConnectConfigTypeDef(
    _RequiredOpenIDConnectConfigTypeDef, _OptionalOpenIDConnectConfigTypeDef
):
    pass

ApiAssociationTypeDef = TypedDict(
    "ApiAssociationTypeDef",
    {
        "domainName": str,
        "apiId": str,
        "associationStatus": AssociationStatusType,
        "deploymentDetail": str,
    },
    total=False,
)

ApiCacheTypeDef = TypedDict(
    "ApiCacheTypeDef",
    {
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
        "type": ApiCacheTypeType,
        "status": ApiCacheStatusType,
    },
    total=False,
)

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": str,
        "description": str,
        "expires": int,
        "deletes": int,
    },
    total=False,
)

AppSyncRuntimeOutputTypeDef = TypedDict(
    "AppSyncRuntimeOutputTypeDef",
    {
        "name": Literal["APPSYNC_JS"],
        "runtimeVersion": str,
    },
)

AppSyncRuntimeTypeDef = TypedDict(
    "AppSyncRuntimeTypeDef",
    {
        "name": Literal["APPSYNC_JS"],
        "runtimeVersion": str,
    },
)

AssociateApiRequestRequestTypeDef = TypedDict(
    "AssociateApiRequestRequestTypeDef",
    {
        "domainName": str,
        "apiId": str,
    },
)

SourceApiAssociationConfigTypeDef = TypedDict(
    "SourceApiAssociationConfigTypeDef",
    {
        "mergeType": MergeTypeType,
    },
    total=False,
)

AwsIamConfigOutputTypeDef = TypedDict(
    "AwsIamConfigOutputTypeDef",
    {
        "signingRegion": str,
        "signingServiceName": str,
    },
    total=False,
)

AwsIamConfigTypeDef = TypedDict(
    "AwsIamConfigTypeDef",
    {
        "signingRegion": str,
        "signingServiceName": str,
    },
    total=False,
)

_RequiredCachingConfigOutputTypeDef = TypedDict(
    "_RequiredCachingConfigOutputTypeDef",
    {
        "ttl": int,
    },
)
_OptionalCachingConfigOutputTypeDef = TypedDict(
    "_OptionalCachingConfigOutputTypeDef",
    {
        "cachingKeys": List[str],
    },
    total=False,
)

class CachingConfigOutputTypeDef(
    _RequiredCachingConfigOutputTypeDef, _OptionalCachingConfigOutputTypeDef
):
    pass

_RequiredCachingConfigTypeDef = TypedDict(
    "_RequiredCachingConfigTypeDef",
    {
        "ttl": int,
    },
)
_OptionalCachingConfigTypeDef = TypedDict(
    "_OptionalCachingConfigTypeDef",
    {
        "cachingKeys": Sequence[str],
    },
    total=False,
)

class CachingConfigTypeDef(_RequiredCachingConfigTypeDef, _OptionalCachingConfigTypeDef):
    pass

CodeErrorLocationTypeDef = TypedDict(
    "CodeErrorLocationTypeDef",
    {
        "line": int,
        "column": int,
        "span": int,
    },
    total=False,
)

_RequiredCreateApiCacheRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
    },
)
_OptionalCreateApiCacheRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApiCacheRequestRequestTypeDef",
    {
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
    },
    total=False,
)

class CreateApiCacheRequestRequestTypeDef(
    _RequiredCreateApiCacheRequestRequestTypeDef, _OptionalCreateApiCacheRequestRequestTypeDef
):
    pass

_RequiredCreateApiKeyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalCreateApiKeyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApiKeyRequestRequestTypeDef",
    {
        "description": str,
        "expires": int,
    },
    total=False,
)

class CreateApiKeyRequestRequestTypeDef(
    _RequiredCreateApiKeyRequestRequestTypeDef, _OptionalCreateApiKeyRequestRequestTypeDef
):
    pass

ElasticsearchDataSourceConfigTypeDef = TypedDict(
    "ElasticsearchDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
    },
)

EventBridgeDataSourceConfigTypeDef = TypedDict(
    "EventBridgeDataSourceConfigTypeDef",
    {
        "eventBusArn": str,
    },
)

LambdaDataSourceConfigTypeDef = TypedDict(
    "LambdaDataSourceConfigTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

OpenSearchServiceDataSourceConfigTypeDef = TypedDict(
    "OpenSearchServiceDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
    },
)

_RequiredCreateDomainNameRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
        "certificateArn": str,
    },
)
_OptionalCreateDomainNameRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainNameRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateDomainNameRequestRequestTypeDef(
    _RequiredCreateDomainNameRequestRequestTypeDef, _OptionalCreateDomainNameRequestRequestTypeDef
):
    pass

DomainNameConfigTypeDef = TypedDict(
    "DomainNameConfigTypeDef",
    {
        "domainName": str,
        "description": str,
        "certificateArn": str,
        "appsyncDomainName": str,
        "hostedZoneId": str,
    },
    total=False,
)

_RequiredLogConfigTypeDef = TypedDict(
    "_RequiredLogConfigTypeDef",
    {
        "fieldLogLevel": FieldLogLevelType,
        "cloudWatchLogsRoleArn": str,
    },
)
_OptionalLogConfigTypeDef = TypedDict(
    "_OptionalLogConfigTypeDef",
    {
        "excludeVerboseContent": bool,
    },
    total=False,
)

class LogConfigTypeDef(_RequiredLogConfigTypeDef, _OptionalLogConfigTypeDef):
    pass

_RequiredUserPoolConfigTypeDef = TypedDict(
    "_RequiredUserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": DefaultActionType,
    },
)
_OptionalUserPoolConfigTypeDef = TypedDict(
    "_OptionalUserPoolConfigTypeDef",
    {
        "appIdClientRegex": str,
    },
    total=False,
)

class UserPoolConfigTypeDef(_RequiredUserPoolConfigTypeDef, _OptionalUserPoolConfigTypeDef):
    pass

PipelineConfigTypeDef = TypedDict(
    "PipelineConfigTypeDef",
    {
        "functions": Sequence[str],
    },
    total=False,
)

CreateTypeRequestRequestTypeDef = TypedDict(
    "CreateTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "definition": str,
        "format": TypeDefinitionFormatType,
    },
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": TypeDefinitionFormatType,
    },
    total=False,
)

ElasticsearchDataSourceConfigOutputTypeDef = TypedDict(
    "ElasticsearchDataSourceConfigOutputTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
    },
)

EventBridgeDataSourceConfigOutputTypeDef = TypedDict(
    "EventBridgeDataSourceConfigOutputTypeDef",
    {
        "eventBusArn": str,
    },
)

LambdaDataSourceConfigOutputTypeDef = TypedDict(
    "LambdaDataSourceConfigOutputTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

OpenSearchServiceDataSourceConfigOutputTypeDef = TypedDict(
    "OpenSearchServiceDataSourceConfigOutputTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
    },
)

DeleteApiCacheRequestRequestTypeDef = TypedDict(
    "DeleteApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

DeleteApiKeyRequestRequestTypeDef = TypedDict(
    "DeleteApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
        "id": str,
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)

DeleteDomainNameRequestRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

DeleteFunctionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)

DeleteGraphqlApiRequestRequestTypeDef = TypedDict(
    "DeleteGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

DeleteResolverRequestRequestTypeDef = TypedDict(
    "DeleteResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)

DeleteTypeRequestRequestTypeDef = TypedDict(
    "DeleteTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
    },
)

DeltaSyncConfigOutputTypeDef = TypedDict(
    "DeltaSyncConfigOutputTypeDef",
    {
        "baseTableTTL": int,
        "deltaSyncTableName": str,
        "deltaSyncTableTTL": int,
    },
    total=False,
)

DeltaSyncConfigTypeDef = TypedDict(
    "DeltaSyncConfigTypeDef",
    {
        "baseTableTTL": int,
        "deltaSyncTableName": str,
        "deltaSyncTableTTL": int,
    },
    total=False,
)

DisassociateApiRequestRequestTypeDef = TypedDict(
    "DisassociateApiRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

DisassociateMergedGraphqlApiRequestRequestTypeDef = TypedDict(
    "DisassociateMergedGraphqlApiRequestRequestTypeDef",
    {
        "sourceApiIdentifier": str,
        "associationId": str,
    },
)

DisassociateMergedGraphqlApiResponseTypeDef = TypedDict(
    "DisassociateMergedGraphqlApiResponseTypeDef",
    {
        "sourceApiAssociationStatus": SourceApiAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateSourceGraphqlApiRequestRequestTypeDef = TypedDict(
    "DisassociateSourceGraphqlApiRequestRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "associationId": str,
    },
)

DisassociateSourceGraphqlApiResponseTypeDef = TypedDict(
    "DisassociateSourceGraphqlApiResponseTypeDef",
    {
        "sourceApiAssociationStatus": SourceApiAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "message": str,
    },
    total=False,
)

EvaluateMappingTemplateRequestRequestTypeDef = TypedDict(
    "EvaluateMappingTemplateRequestRequestTypeDef",
    {
        "template": str,
        "context": str,
    },
)

FlushApiCacheRequestRequestTypeDef = TypedDict(
    "FlushApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetApiAssociationRequestRequestTypeDef = TypedDict(
    "GetApiAssociationRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetApiCacheRequestRequestTypeDef = TypedDict(
    "GetApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)

GetDomainNameRequestRequestTypeDef = TypedDict(
    "GetDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetFunctionRequestRequestTypeDef = TypedDict(
    "GetFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)

GetGraphqlApiRequestRequestTypeDef = TypedDict(
    "GetGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

_RequiredGetIntrospectionSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredGetIntrospectionSchemaRequestRequestTypeDef",
    {
        "apiId": str,
        "format": OutputTypeType,
    },
)
_OptionalGetIntrospectionSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalGetIntrospectionSchemaRequestRequestTypeDef",
    {
        "includeDirectives": bool,
    },
    total=False,
)

class GetIntrospectionSchemaRequestRequestTypeDef(
    _RequiredGetIntrospectionSchemaRequestRequestTypeDef,
    _OptionalGetIntrospectionSchemaRequestRequestTypeDef,
):
    pass

GetIntrospectionSchemaResponseTypeDef = TypedDict(
    "GetIntrospectionSchemaResponseTypeDef",
    {
        "schema": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRequestRequestTypeDef = TypedDict(
    "GetResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)

GetSchemaCreationStatusRequestRequestTypeDef = TypedDict(
    "GetSchemaCreationStatusRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetSchemaCreationStatusResponseTypeDef = TypedDict(
    "GetSchemaCreationStatusResponseTypeDef",
    {
        "status": SchemaStatusType,
        "details": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSourceApiAssociationRequestRequestTypeDef = TypedDict(
    "GetSourceApiAssociationRequestRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "associationId": str,
    },
)

GetTypeRequestRequestTypeDef = TypedDict(
    "GetTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
    },
)

_RequiredLogConfigOutputTypeDef = TypedDict(
    "_RequiredLogConfigOutputTypeDef",
    {
        "fieldLogLevel": FieldLogLevelType,
        "cloudWatchLogsRoleArn": str,
    },
)
_OptionalLogConfigOutputTypeDef = TypedDict(
    "_OptionalLogConfigOutputTypeDef",
    {
        "excludeVerboseContent": bool,
    },
    total=False,
)

class LogConfigOutputTypeDef(_RequiredLogConfigOutputTypeDef, _OptionalLogConfigOutputTypeDef):
    pass

_RequiredUserPoolConfigOutputTypeDef = TypedDict(
    "_RequiredUserPoolConfigOutputTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": DefaultActionType,
    },
)
_OptionalUserPoolConfigOutputTypeDef = TypedDict(
    "_OptionalUserPoolConfigOutputTypeDef",
    {
        "appIdClientRegex": str,
    },
    total=False,
)

class UserPoolConfigOutputTypeDef(
    _RequiredUserPoolConfigOutputTypeDef, _OptionalUserPoolConfigOutputTypeDef
):
    pass

LambdaConflictHandlerConfigOutputTypeDef = TypedDict(
    "LambdaConflictHandlerConfigOutputTypeDef",
    {
        "lambdaConflictHandlerArn": str,
    },
    total=False,
)

LambdaConflictHandlerConfigTypeDef = TypedDict(
    "LambdaConflictHandlerConfigTypeDef",
    {
        "lambdaConflictHandlerArn": str,
    },
    total=False,
)

_RequiredListApiKeysRequestListApiKeysPaginateTypeDef = TypedDict(
    "_RequiredListApiKeysRequestListApiKeysPaginateTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListApiKeysRequestListApiKeysPaginateTypeDef = TypedDict(
    "_OptionalListApiKeysRequestListApiKeysPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListApiKeysRequestListApiKeysPaginateTypeDef(
    _RequiredListApiKeysRequestListApiKeysPaginateTypeDef,
    _OptionalListApiKeysRequestListApiKeysPaginateTypeDef,
):
    pass

_RequiredListApiKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListApiKeysRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListApiKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListApiKeysRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListApiKeysRequestRequestTypeDef(
    _RequiredListApiKeysRequestRequestTypeDef, _OptionalListApiKeysRequestRequestTypeDef
):
    pass

_RequiredListDataSourcesRequestListDataSourcesPaginateTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestListDataSourcesPaginateTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListDataSourcesRequestListDataSourcesPaginateTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestListDataSourcesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(
    _RequiredListDataSourcesRequestListDataSourcesPaginateTypeDef,
    _OptionalListDataSourcesRequestListDataSourcesPaginateTypeDef,
):
    pass

_RequiredListDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDataSourcesRequestRequestTypeDef(
    _RequiredListDataSourcesRequestRequestTypeDef, _OptionalListDataSourcesRequestRequestTypeDef
):
    pass

ListDomainNamesRequestRequestTypeDef = TypedDict(
    "ListDomainNamesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListFunctionsRequestListFunctionsPaginateTypeDef = TypedDict(
    "_RequiredListFunctionsRequestListFunctionsPaginateTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListFunctionsRequestListFunctionsPaginateTypeDef = TypedDict(
    "_OptionalListFunctionsRequestListFunctionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListFunctionsRequestListFunctionsPaginateTypeDef(
    _RequiredListFunctionsRequestListFunctionsPaginateTypeDef,
    _OptionalListFunctionsRequestListFunctionsPaginateTypeDef,
):
    pass

_RequiredListFunctionsRequestRequestTypeDef = TypedDict(
    "_RequiredListFunctionsRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListFunctionsRequestRequestTypeDef = TypedDict(
    "_OptionalListFunctionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListFunctionsRequestRequestTypeDef(
    _RequiredListFunctionsRequestRequestTypeDef, _OptionalListFunctionsRequestRequestTypeDef
):
    pass

ListGraphqlApisRequestListGraphqlApisPaginateTypeDef = TypedDict(
    "ListGraphqlApisRequestListGraphqlApisPaginateTypeDef",
    {
        "apiType": GraphQLApiTypeType,
        "owner": OwnershipType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListGraphqlApisRequestRequestTypeDef = TypedDict(
    "ListGraphqlApisRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "apiType": GraphQLApiTypeType,
        "owner": OwnershipType,
    },
    total=False,
)

_RequiredListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef = TypedDict(
    "_RequiredListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)
_OptionalListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef = TypedDict(
    "_OptionalListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef(
    _RequiredListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef,
    _OptionalListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef,
):
    pass

_RequiredListResolversByFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredListResolversByFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)
_OptionalListResolversByFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalListResolversByFunctionRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListResolversByFunctionRequestRequestTypeDef(
    _RequiredListResolversByFunctionRequestRequestTypeDef,
    _OptionalListResolversByFunctionRequestRequestTypeDef,
):
    pass

_RequiredListResolversRequestListResolversPaginateTypeDef = TypedDict(
    "_RequiredListResolversRequestListResolversPaginateTypeDef",
    {
        "apiId": str,
        "typeName": str,
    },
)
_OptionalListResolversRequestListResolversPaginateTypeDef = TypedDict(
    "_OptionalListResolversRequestListResolversPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListResolversRequestListResolversPaginateTypeDef(
    _RequiredListResolversRequestListResolversPaginateTypeDef,
    _OptionalListResolversRequestListResolversPaginateTypeDef,
):
    pass

_RequiredListResolversRequestRequestTypeDef = TypedDict(
    "_RequiredListResolversRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
    },
)
_OptionalListResolversRequestRequestTypeDef = TypedDict(
    "_OptionalListResolversRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListResolversRequestRequestTypeDef(
    _RequiredListResolversRequestRequestTypeDef, _OptionalListResolversRequestRequestTypeDef
):
    pass

_RequiredListSourceApiAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListSourceApiAssociationsRequestRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListSourceApiAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListSourceApiAssociationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListSourceApiAssociationsRequestRequestTypeDef(
    _RequiredListSourceApiAssociationsRequestRequestTypeDef,
    _OptionalListSourceApiAssociationsRequestRequestTypeDef,
):
    pass

SourceApiAssociationSummaryTypeDef = TypedDict(
    "SourceApiAssociationSummaryTypeDef",
    {
        "associationId": str,
        "associationArn": str,
        "sourceApiId": str,
        "sourceApiArn": str,
        "mergedApiId": str,
        "mergedApiArn": str,
        "description": str,
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTypesByAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredListTypesByAssociationRequestRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "associationId": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalListTypesByAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalListTypesByAssociationRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTypesByAssociationRequestRequestTypeDef(
    _RequiredListTypesByAssociationRequestRequestTypeDef,
    _OptionalListTypesByAssociationRequestRequestTypeDef,
):
    pass

_RequiredListTypesRequestListTypesPaginateTypeDef = TypedDict(
    "_RequiredListTypesRequestListTypesPaginateTypeDef",
    {
        "apiId": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalListTypesRequestListTypesPaginateTypeDef = TypedDict(
    "_OptionalListTypesRequestListTypesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListTypesRequestListTypesPaginateTypeDef(
    _RequiredListTypesRequestListTypesPaginateTypeDef,
    _OptionalListTypesRequestListTypesPaginateTypeDef,
):
    pass

_RequiredListTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListTypesRequestRequestTypeDef",
    {
        "apiId": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalListTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListTypesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTypesRequestRequestTypeDef(
    _RequiredListTypesRequestRequestTypeDef, _OptionalListTypesRequestRequestTypeDef
):
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

PipelineConfigOutputTypeDef = TypedDict(
    "PipelineConfigOutputTypeDef",
    {
        "functions": List[str],
    },
    total=False,
)

RdsHttpEndpointConfigOutputTypeDef = TypedDict(
    "RdsHttpEndpointConfigOutputTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

RdsHttpEndpointConfigTypeDef = TypedDict(
    "RdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
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

SourceApiAssociationConfigOutputTypeDef = TypedDict(
    "SourceApiAssociationConfigOutputTypeDef",
    {
        "mergeType": MergeTypeType,
    },
    total=False,
)

StartSchemaCreationRequestRequestTypeDef = TypedDict(
    "StartSchemaCreationRequestRequestTypeDef",
    {
        "apiId": str,
        "definition": Union[str, bytes, IO[Any], StreamingBody],
    },
)

StartSchemaCreationResponseTypeDef = TypedDict(
    "StartSchemaCreationResponseTypeDef",
    {
        "status": SchemaStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSchemaMergeRequestRequestTypeDef = TypedDict(
    "StartSchemaMergeRequestRequestTypeDef",
    {
        "associationId": str,
        "mergedApiIdentifier": str,
    },
)

StartSchemaMergeResponseTypeDef = TypedDict(
    "StartSchemaMergeResponseTypeDef",
    {
        "sourceApiAssociationStatus": SourceApiAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

UpdateApiCacheRequestRequestTypeDef = TypedDict(
    "UpdateApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
    },
)

_RequiredUpdateApiKeyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
        "id": str,
    },
)
_OptionalUpdateApiKeyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApiKeyRequestRequestTypeDef",
    {
        "description": str,
        "expires": int,
    },
    total=False,
)

class UpdateApiKeyRequestRequestTypeDef(
    _RequiredUpdateApiKeyRequestRequestTypeDef, _OptionalUpdateApiKeyRequestRequestTypeDef
):
    pass

_RequiredUpdateDomainNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalUpdateDomainNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainNameRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateDomainNameRequestRequestTypeDef(
    _RequiredUpdateDomainNameRequestRequestTypeDef, _OptionalUpdateDomainNameRequestRequestTypeDef
):
    pass

_RequiredUpdateTypeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalUpdateTypeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTypeRequestRequestTypeDef",
    {
        "definition": str,
    },
    total=False,
)

class UpdateTypeRequestRequestTypeDef(
    _RequiredUpdateTypeRequestRequestTypeDef, _OptionalUpdateTypeRequestRequestTypeDef
):
    pass

AdditionalAuthenticationProviderOutputTypeDef = TypedDict(
    "AdditionalAuthenticationProviderOutputTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "openIDConnectConfig": OpenIDConnectConfigOutputTypeDef,
        "userPoolConfig": CognitoUserPoolConfigOutputTypeDef,
        "lambdaAuthorizerConfig": LambdaAuthorizerConfigOutputTypeDef,
    },
    total=False,
)

AdditionalAuthenticationProviderTypeDef = TypedDict(
    "AdditionalAuthenticationProviderTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "openIDConnectConfig": OpenIDConnectConfigTypeDef,
        "userPoolConfig": CognitoUserPoolConfigTypeDef,
        "lambdaAuthorizerConfig": LambdaAuthorizerConfigTypeDef,
    },
    total=False,
)

AssociateApiResponseTypeDef = TypedDict(
    "AssociateApiResponseTypeDef",
    {
        "apiAssociation": ApiAssociationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApiAssociationResponseTypeDef = TypedDict(
    "GetApiAssociationResponseTypeDef",
    {
        "apiAssociation": ApiAssociationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApiCacheResponseTypeDef = TypedDict(
    "CreateApiCacheResponseTypeDef",
    {
        "apiCache": ApiCacheTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApiCacheResponseTypeDef = TypedDict(
    "GetApiCacheResponseTypeDef",
    {
        "apiCache": ApiCacheTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApiCacheResponseTypeDef = TypedDict(
    "UpdateApiCacheResponseTypeDef",
    {
        "apiCache": ApiCacheTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApiKeyResponseTypeDef = TypedDict(
    "CreateApiKeyResponseTypeDef",
    {
        "apiKey": ApiKeyTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApiKeysResponseTypeDef = TypedDict(
    "ListApiKeysResponseTypeDef",
    {
        "apiKeys": List[ApiKeyTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApiKeyResponseTypeDef = TypedDict(
    "UpdateApiKeyResponseTypeDef",
    {
        "apiKey": ApiKeyTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEvaluateCodeRequestRequestTypeDef = TypedDict(
    "_RequiredEvaluateCodeRequestRequestTypeDef",
    {
        "runtime": AppSyncRuntimeTypeDef,
        "code": str,
        "context": str,
    },
)
_OptionalEvaluateCodeRequestRequestTypeDef = TypedDict(
    "_OptionalEvaluateCodeRequestRequestTypeDef",
    {
        "function": str,
    },
    total=False,
)

class EvaluateCodeRequestRequestTypeDef(
    _RequiredEvaluateCodeRequestRequestTypeDef, _OptionalEvaluateCodeRequestRequestTypeDef
):
    pass

_RequiredAssociateMergedGraphqlApiRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateMergedGraphqlApiRequestRequestTypeDef",
    {
        "sourceApiIdentifier": str,
        "mergedApiIdentifier": str,
    },
)
_OptionalAssociateMergedGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateMergedGraphqlApiRequestRequestTypeDef",
    {
        "description": str,
        "sourceApiAssociationConfig": SourceApiAssociationConfigTypeDef,
    },
    total=False,
)

class AssociateMergedGraphqlApiRequestRequestTypeDef(
    _RequiredAssociateMergedGraphqlApiRequestRequestTypeDef,
    _OptionalAssociateMergedGraphqlApiRequestRequestTypeDef,
):
    pass

_RequiredAssociateSourceGraphqlApiRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateSourceGraphqlApiRequestRequestTypeDef",
    {
        "mergedApiIdentifier": str,
        "sourceApiIdentifier": str,
    },
)
_OptionalAssociateSourceGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateSourceGraphqlApiRequestRequestTypeDef",
    {
        "description": str,
        "sourceApiAssociationConfig": SourceApiAssociationConfigTypeDef,
    },
    total=False,
)

class AssociateSourceGraphqlApiRequestRequestTypeDef(
    _RequiredAssociateSourceGraphqlApiRequestRequestTypeDef,
    _OptionalAssociateSourceGraphqlApiRequestRequestTypeDef,
):
    pass

_RequiredUpdateSourceApiAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSourceApiAssociationRequestRequestTypeDef",
    {
        "associationId": str,
        "mergedApiIdentifier": str,
    },
)
_OptionalUpdateSourceApiAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSourceApiAssociationRequestRequestTypeDef",
    {
        "description": str,
        "sourceApiAssociationConfig": SourceApiAssociationConfigTypeDef,
    },
    total=False,
)

class UpdateSourceApiAssociationRequestRequestTypeDef(
    _RequiredUpdateSourceApiAssociationRequestRequestTypeDef,
    _OptionalUpdateSourceApiAssociationRequestRequestTypeDef,
):
    pass

_RequiredAuthorizationConfigOutputTypeDef = TypedDict(
    "_RequiredAuthorizationConfigOutputTypeDef",
    {
        "authorizationType": Literal["AWS_IAM"],
    },
)
_OptionalAuthorizationConfigOutputTypeDef = TypedDict(
    "_OptionalAuthorizationConfigOutputTypeDef",
    {
        "awsIamConfig": AwsIamConfigOutputTypeDef,
    },
    total=False,
)

class AuthorizationConfigOutputTypeDef(
    _RequiredAuthorizationConfigOutputTypeDef, _OptionalAuthorizationConfigOutputTypeDef
):
    pass

_RequiredAuthorizationConfigTypeDef = TypedDict(
    "_RequiredAuthorizationConfigTypeDef",
    {
        "authorizationType": Literal["AWS_IAM"],
    },
)
_OptionalAuthorizationConfigTypeDef = TypedDict(
    "_OptionalAuthorizationConfigTypeDef",
    {
        "awsIamConfig": AwsIamConfigTypeDef,
    },
    total=False,
)

class AuthorizationConfigTypeDef(
    _RequiredAuthorizationConfigTypeDef, _OptionalAuthorizationConfigTypeDef
):
    pass

CodeErrorTypeDef = TypedDict(
    "CodeErrorTypeDef",
    {
        "errorType": str,
        "value": str,
        "location": CodeErrorLocationTypeDef,
    },
    total=False,
)

CreateDomainNameResponseTypeDef = TypedDict(
    "CreateDomainNameResponseTypeDef",
    {
        "domainNameConfig": DomainNameConfigTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainNameResponseTypeDef = TypedDict(
    "GetDomainNameResponseTypeDef",
    {
        "domainNameConfig": DomainNameConfigTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "domainNameConfigs": List[DomainNameConfigTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainNameResponseTypeDef = TypedDict(
    "UpdateDomainNameResponseTypeDef",
    {
        "domainNameConfig": DomainNameConfigTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTypeResponseTypeDef = TypedDict(
    "CreateTypeResponseTypeDef",
    {
        "type": TypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTypeResponseTypeDef = TypedDict(
    "GetTypeResponseTypeDef",
    {
        "type": TypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypesByAssociationResponseTypeDef = TypedDict(
    "ListTypesByAssociationResponseTypeDef",
    {
        "types": List[TypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypesResponseTypeDef = TypedDict(
    "ListTypesResponseTypeDef",
    {
        "types": List[TypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTypeResponseTypeDef = TypedDict(
    "UpdateTypeResponseTypeDef",
    {
        "type": TypeTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDynamodbDataSourceConfigOutputTypeDef = TypedDict(
    "_RequiredDynamodbDataSourceConfigOutputTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
    },
)
_OptionalDynamodbDataSourceConfigOutputTypeDef = TypedDict(
    "_OptionalDynamodbDataSourceConfigOutputTypeDef",
    {
        "useCallerCredentials": bool,
        "deltaSyncConfig": DeltaSyncConfigOutputTypeDef,
        "versioned": bool,
    },
    total=False,
)

class DynamodbDataSourceConfigOutputTypeDef(
    _RequiredDynamodbDataSourceConfigOutputTypeDef, _OptionalDynamodbDataSourceConfigOutputTypeDef
):
    pass

_RequiredDynamodbDataSourceConfigTypeDef = TypedDict(
    "_RequiredDynamodbDataSourceConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
    },
)
_OptionalDynamodbDataSourceConfigTypeDef = TypedDict(
    "_OptionalDynamodbDataSourceConfigTypeDef",
    {
        "useCallerCredentials": bool,
        "deltaSyncConfig": DeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)

class DynamodbDataSourceConfigTypeDef(
    _RequiredDynamodbDataSourceConfigTypeDef, _OptionalDynamodbDataSourceConfigTypeDef
):
    pass

EvaluateMappingTemplateResponseTypeDef = TypedDict(
    "EvaluateMappingTemplateResponseTypeDef",
    {
        "evaluationResult": str,
        "error": ErrorDetailTypeDef,
        "logs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SyncConfigOutputTypeDef = TypedDict(
    "SyncConfigOutputTypeDef",
    {
        "conflictHandler": ConflictHandlerTypeType,
        "conflictDetection": ConflictDetectionTypeType,
        "lambdaConflictHandlerConfig": LambdaConflictHandlerConfigOutputTypeDef,
    },
    total=False,
)

SyncConfigTypeDef = TypedDict(
    "SyncConfigTypeDef",
    {
        "conflictHandler": ConflictHandlerTypeType,
        "conflictDetection": ConflictDetectionTypeType,
        "lambdaConflictHandlerConfig": LambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ListSourceApiAssociationsResponseTypeDef = TypedDict(
    "ListSourceApiAssociationsResponseTypeDef",
    {
        "sourceApiAssociationSummaries": List[SourceApiAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelationalDatabaseDataSourceConfigOutputTypeDef = TypedDict(
    "RelationalDatabaseDataSourceConfigOutputTypeDef",
    {
        "relationalDatabaseSourceType": Literal["RDS_HTTP_ENDPOINT"],
        "rdsHttpEndpointConfig": RdsHttpEndpointConfigOutputTypeDef,
    },
    total=False,
)

RelationalDatabaseDataSourceConfigTypeDef = TypedDict(
    "RelationalDatabaseDataSourceConfigTypeDef",
    {
        "relationalDatabaseSourceType": Literal["RDS_HTTP_ENDPOINT"],
        "rdsHttpEndpointConfig": RdsHttpEndpointConfigTypeDef,
    },
    total=False,
)

SourceApiAssociationTypeDef = TypedDict(
    "SourceApiAssociationTypeDef",
    {
        "associationId": str,
        "associationArn": str,
        "sourceApiId": str,
        "sourceApiArn": str,
        "mergedApiArn": str,
        "mergedApiId": str,
        "description": str,
        "sourceApiAssociationConfig": SourceApiAssociationConfigOutputTypeDef,
        "sourceApiAssociationStatus": SourceApiAssociationStatusType,
        "sourceApiAssociationStatusDetail": str,
        "lastSuccessfulMergeDate": datetime,
    },
    total=False,
)

GraphqlApiTypeDef = TypedDict(
    "GraphqlApiTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": AuthenticationTypeType,
        "logConfig": LogConfigOutputTypeDef,
        "userPoolConfig": UserPoolConfigOutputTypeDef,
        "openIDConnectConfig": OpenIDConnectConfigOutputTypeDef,
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List[AdditionalAuthenticationProviderOutputTypeDef],
        "xrayEnabled": bool,
        "wafWebAclArn": str,
        "lambdaAuthorizerConfig": LambdaAuthorizerConfigOutputTypeDef,
        "dns": Dict[str, str],
        "visibility": GraphQLApiVisibilityType,
        "apiType": GraphQLApiTypeType,
        "mergedApiExecutionRoleArn": str,
        "owner": str,
        "ownerContact": str,
    },
    total=False,
)

_RequiredCreateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGraphqlApiRequestRequestTypeDef",
    {
        "name": str,
        "authenticationType": AuthenticationTypeType,
    },
)
_OptionalCreateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGraphqlApiRequestRequestTypeDef",
    {
        "logConfig": LogConfigTypeDef,
        "userPoolConfig": UserPoolConfigTypeDef,
        "openIDConnectConfig": OpenIDConnectConfigTypeDef,
        "tags": Mapping[str, str],
        "additionalAuthenticationProviders": Sequence[AdditionalAuthenticationProviderTypeDef],
        "xrayEnabled": bool,
        "lambdaAuthorizerConfig": LambdaAuthorizerConfigTypeDef,
        "visibility": GraphQLApiVisibilityType,
        "apiType": GraphQLApiTypeType,
        "mergedApiExecutionRoleArn": str,
        "ownerContact": str,
    },
    total=False,
)

class CreateGraphqlApiRequestRequestTypeDef(
    _RequiredCreateGraphqlApiRequestRequestTypeDef, _OptionalCreateGraphqlApiRequestRequestTypeDef
):
    pass

_RequiredUpdateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)
_OptionalUpdateGraphqlApiRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGraphqlApiRequestRequestTypeDef",
    {
        "logConfig": LogConfigTypeDef,
        "authenticationType": AuthenticationTypeType,
        "userPoolConfig": UserPoolConfigTypeDef,
        "openIDConnectConfig": OpenIDConnectConfigTypeDef,
        "additionalAuthenticationProviders": Sequence[AdditionalAuthenticationProviderTypeDef],
        "xrayEnabled": bool,
        "lambdaAuthorizerConfig": LambdaAuthorizerConfigTypeDef,
        "mergedApiExecutionRoleArn": str,
        "ownerContact": str,
    },
    total=False,
)

class UpdateGraphqlApiRequestRequestTypeDef(
    _RequiredUpdateGraphqlApiRequestRequestTypeDef, _OptionalUpdateGraphqlApiRequestRequestTypeDef
):
    pass

HttpDataSourceConfigOutputTypeDef = TypedDict(
    "HttpDataSourceConfigOutputTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": AuthorizationConfigOutputTypeDef,
    },
    total=False,
)

HttpDataSourceConfigTypeDef = TypedDict(
    "HttpDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": AuthorizationConfigTypeDef,
    },
    total=False,
)

EvaluateCodeErrorDetailTypeDef = TypedDict(
    "EvaluateCodeErrorDetailTypeDef",
    {
        "message": str,
        "codeErrors": List[CodeErrorTypeDef],
    },
    total=False,
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
        "syncConfig": SyncConfigOutputTypeDef,
        "maxBatchSize": int,
        "runtime": AppSyncRuntimeOutputTypeDef,
        "code": str,
    },
    total=False,
)

ResolverTypeDef = TypedDict(
    "ResolverTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": PipelineConfigOutputTypeDef,
        "syncConfig": SyncConfigOutputTypeDef,
        "cachingConfig": CachingConfigOutputTypeDef,
        "maxBatchSize": int,
        "runtime": AppSyncRuntimeOutputTypeDef,
        "code": str,
    },
    total=False,
)

_RequiredCreateFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "dataSourceName": str,
    },
)
_OptionalCreateFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionRequestRequestTypeDef",
    {
        "description": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
        "syncConfig": SyncConfigTypeDef,
        "maxBatchSize": int,
        "runtime": AppSyncRuntimeTypeDef,
        "code": str,
    },
    total=False,
)

class CreateFunctionRequestRequestTypeDef(
    _RequiredCreateFunctionRequestRequestTypeDef, _OptionalCreateFunctionRequestRequestTypeDef
):
    pass

_RequiredCreateResolverRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)
_OptionalCreateResolverRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResolverRequestRequestTypeDef",
    {
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": PipelineConfigTypeDef,
        "syncConfig": SyncConfigTypeDef,
        "cachingConfig": CachingConfigTypeDef,
        "maxBatchSize": int,
        "runtime": AppSyncRuntimeTypeDef,
        "code": str,
    },
    total=False,
)

class CreateResolverRequestRequestTypeDef(
    _RequiredCreateResolverRequestRequestTypeDef, _OptionalCreateResolverRequestRequestTypeDef
):
    pass

_RequiredUpdateFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "functionId": str,
        "dataSourceName": str,
    },
)
_OptionalUpdateFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionRequestRequestTypeDef",
    {
        "description": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
        "syncConfig": SyncConfigTypeDef,
        "maxBatchSize": int,
        "runtime": AppSyncRuntimeTypeDef,
        "code": str,
    },
    total=False,
)

class UpdateFunctionRequestRequestTypeDef(
    _RequiredUpdateFunctionRequestRequestTypeDef, _OptionalUpdateFunctionRequestRequestTypeDef
):
    pass

_RequiredUpdateResolverRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)
_OptionalUpdateResolverRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResolverRequestRequestTypeDef",
    {
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": PipelineConfigTypeDef,
        "syncConfig": SyncConfigTypeDef,
        "cachingConfig": CachingConfigTypeDef,
        "maxBatchSize": int,
        "runtime": AppSyncRuntimeTypeDef,
        "code": str,
    },
    total=False,
)

class UpdateResolverRequestRequestTypeDef(
    _RequiredUpdateResolverRequestRequestTypeDef, _OptionalUpdateResolverRequestRequestTypeDef
):
    pass

AssociateMergedGraphqlApiResponseTypeDef = TypedDict(
    "AssociateMergedGraphqlApiResponseTypeDef",
    {
        "sourceApiAssociation": SourceApiAssociationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateSourceGraphqlApiResponseTypeDef = TypedDict(
    "AssociateSourceGraphqlApiResponseTypeDef",
    {
        "sourceApiAssociation": SourceApiAssociationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSourceApiAssociationResponseTypeDef = TypedDict(
    "GetSourceApiAssociationResponseTypeDef",
    {
        "sourceApiAssociation": SourceApiAssociationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSourceApiAssociationResponseTypeDef = TypedDict(
    "UpdateSourceApiAssociationResponseTypeDef",
    {
        "sourceApiAssociation": SourceApiAssociationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGraphqlApiResponseTypeDef = TypedDict(
    "CreateGraphqlApiResponseTypeDef",
    {
        "graphqlApi": GraphqlApiTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGraphqlApiResponseTypeDef = TypedDict(
    "GetGraphqlApiResponseTypeDef",
    {
        "graphqlApi": GraphqlApiTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGraphqlApisResponseTypeDef = TypedDict(
    "ListGraphqlApisResponseTypeDef",
    {
        "graphqlApis": List[GraphqlApiTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGraphqlApiResponseTypeDef = TypedDict(
    "UpdateGraphqlApiResponseTypeDef",
    {
        "graphqlApi": GraphqlApiTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": DataSourceTypeType,
        "serviceRoleArn": str,
        "dynamodbConfig": DynamodbDataSourceConfigOutputTypeDef,
        "lambdaConfig": LambdaDataSourceConfigOutputTypeDef,
        "elasticsearchConfig": ElasticsearchDataSourceConfigOutputTypeDef,
        "openSearchServiceConfig": OpenSearchServiceDataSourceConfigOutputTypeDef,
        "httpConfig": HttpDataSourceConfigOutputTypeDef,
        "relationalDatabaseConfig": RelationalDatabaseDataSourceConfigOutputTypeDef,
        "eventBridgeConfig": EventBridgeDataSourceConfigOutputTypeDef,
    },
    total=False,
)

_RequiredCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestRequestTypeDef",
    {
        "description": str,
        "serviceRoleArn": str,
        "dynamodbConfig": DynamodbDataSourceConfigTypeDef,
        "lambdaConfig": LambdaDataSourceConfigTypeDef,
        "elasticsearchConfig": ElasticsearchDataSourceConfigTypeDef,
        "openSearchServiceConfig": OpenSearchServiceDataSourceConfigTypeDef,
        "httpConfig": HttpDataSourceConfigTypeDef,
        "relationalDatabaseConfig": RelationalDatabaseDataSourceConfigTypeDef,
        "eventBridgeConfig": EventBridgeDataSourceConfigTypeDef,
    },
    total=False,
)

class CreateDataSourceRequestRequestTypeDef(
    _RequiredCreateDataSourceRequestRequestTypeDef, _OptionalCreateDataSourceRequestRequestTypeDef
):
    pass

_RequiredUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "description": str,
        "serviceRoleArn": str,
        "dynamodbConfig": DynamodbDataSourceConfigTypeDef,
        "lambdaConfig": LambdaDataSourceConfigTypeDef,
        "elasticsearchConfig": ElasticsearchDataSourceConfigTypeDef,
        "openSearchServiceConfig": OpenSearchServiceDataSourceConfigTypeDef,
        "httpConfig": HttpDataSourceConfigTypeDef,
        "relationalDatabaseConfig": RelationalDatabaseDataSourceConfigTypeDef,
        "eventBridgeConfig": EventBridgeDataSourceConfigTypeDef,
    },
    total=False,
)

class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass

EvaluateCodeResponseTypeDef = TypedDict(
    "EvaluateCodeResponseTypeDef",
    {
        "evaluationResult": str,
        "error": EvaluateCodeErrorDetailTypeDef,
        "logs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFunctionResponseTypeDef = TypedDict(
    "CreateFunctionResponseTypeDef",
    {
        "functionConfiguration": FunctionConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionResponseTypeDef = TypedDict(
    "GetFunctionResponseTypeDef",
    {
        "functionConfiguration": FunctionConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsResponseTypeDef = TypedDict(
    "ListFunctionsResponseTypeDef",
    {
        "functions": List[FunctionConfigurationTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFunctionResponseTypeDef = TypedDict(
    "UpdateFunctionResponseTypeDef",
    {
        "functionConfiguration": FunctionConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResolverResponseTypeDef = TypedDict(
    "CreateResolverResponseTypeDef",
    {
        "resolver": ResolverTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverResponseTypeDef = TypedDict(
    "GetResolverResponseTypeDef",
    {
        "resolver": ResolverTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolversByFunctionResponseTypeDef = TypedDict(
    "ListResolversByFunctionResponseTypeDef",
    {
        "resolvers": List[ResolverTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolversResponseTypeDef = TypedDict(
    "ListResolversResponseTypeDef",
    {
        "resolvers": List[ResolverTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResolverResponseTypeDef = TypedDict(
    "UpdateResolverResponseTypeDef",
    {
        "resolver": ResolverTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "dataSource": DataSourceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "dataSource": DataSourceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "dataSources": List[DataSourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "dataSource": DataSourceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
