"""
Type annotations for appflow service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/type_defs/)

Usage::

    ```python
    from mypy_boto3_appflow.type_defs import AggregationConfigOutputTypeDef

    data: AggregationConfigOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AggregationTypeType,
    AuthenticationTypeType,
    ConnectionModeType,
    ConnectorTypeType,
    DatadogConnectorOperatorType,
    DataPullModeType,
    DataTransferApiTypeType,
    DynatraceConnectorOperatorType,
    ExecutionStatusType,
    FileTypeType,
    FlowStatusType,
    GoogleAnalyticsConnectorOperatorType,
    InforNexusConnectorOperatorType,
    MarketoConnectorOperatorType,
    OAuth2CustomPropTypeType,
    OAuth2GrantTypeType,
    OperatorPropertiesKeysType,
    OperatorsType,
    OperatorType,
    PardotConnectorOperatorType,
    PathPrefixType,
    PrefixFormatType,
    PrefixTypeType,
    PrivateConnectionProvisioningFailureCauseType,
    PrivateConnectionProvisioningStatusType,
    S3ConnectorOperatorType,
    S3InputFileTypeType,
    SalesforceConnectorOperatorType,
    SalesforceDataTransferApiType,
    SAPODataConnectorOperatorType,
    ScheduleFrequencyTypeType,
    ServiceNowConnectorOperatorType,
    SingularConnectorOperatorType,
    SlackConnectorOperatorType,
    SupportedDataTransferTypeType,
    TaskTypeType,
    TrendmicroConnectorOperatorType,
    TriggerTypeType,
    VeevaConnectorOperatorType,
    WriteOperationTypeType,
    ZendeskConnectorOperatorType,
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
    "AggregationConfigOutputTypeDef",
    "AggregationConfigTypeDef",
    "AmplitudeConnectorProfileCredentialsTypeDef",
    "AmplitudeSourcePropertiesOutputTypeDef",
    "AmplitudeSourcePropertiesTypeDef",
    "ApiKeyCredentialsTypeDef",
    "AuthParameterTypeDef",
    "BasicAuthCredentialsTypeDef",
    "CancelFlowExecutionsRequestRequestTypeDef",
    "CancelFlowExecutionsResponseTypeDef",
    "ConnectorRuntimeSettingTypeDef",
    "DataTransferApiOutputTypeDef",
    "ConnectorDetailTypeDef",
    "DestinationFieldPropertiesTypeDef",
    "SourceFieldPropertiesTypeDef",
    "ConnectorEntityTypeDef",
    "GoogleAnalyticsMetadataTypeDef",
    "HoneycodeMetadataTypeDef",
    "SalesforceMetadataTypeDef",
    "SlackMetadataTypeDef",
    "SnowflakeMetadataTypeDef",
    "ZendeskMetadataTypeDef",
    "ConnectorOAuthRequestTypeDef",
    "ConnectorOperatorOutputTypeDef",
    "ConnectorOperatorTypeDef",
    "DatadogConnectorProfileCredentialsTypeDef",
    "DynatraceConnectorProfileCredentialsTypeDef",
    "InforNexusConnectorProfileCredentialsTypeDef",
    "RedshiftConnectorProfileCredentialsTypeDef",
    "ServiceNowConnectorProfileCredentialsTypeDef",
    "SingularConnectorProfileCredentialsTypeDef",
    "SnowflakeConnectorProfileCredentialsTypeDef",
    "TrendmicroConnectorProfileCredentialsTypeDef",
    "VeevaConnectorProfileCredentialsTypeDef",
    "DatadogConnectorProfilePropertiesOutputTypeDef",
    "DynatraceConnectorProfilePropertiesOutputTypeDef",
    "InforNexusConnectorProfilePropertiesOutputTypeDef",
    "MarketoConnectorProfilePropertiesOutputTypeDef",
    "PardotConnectorProfilePropertiesOutputTypeDef",
    "RedshiftConnectorProfilePropertiesOutputTypeDef",
    "SalesforceConnectorProfilePropertiesOutputTypeDef",
    "ServiceNowConnectorProfilePropertiesOutputTypeDef",
    "SlackConnectorProfilePropertiesOutputTypeDef",
    "SnowflakeConnectorProfilePropertiesOutputTypeDef",
    "VeevaConnectorProfilePropertiesOutputTypeDef",
    "ZendeskConnectorProfilePropertiesOutputTypeDef",
    "DatadogConnectorProfilePropertiesTypeDef",
    "DynatraceConnectorProfilePropertiesTypeDef",
    "InforNexusConnectorProfilePropertiesTypeDef",
    "MarketoConnectorProfilePropertiesTypeDef",
    "PardotConnectorProfilePropertiesTypeDef",
    "RedshiftConnectorProfilePropertiesTypeDef",
    "SalesforceConnectorProfilePropertiesTypeDef",
    "ServiceNowConnectorProfilePropertiesTypeDef",
    "SlackConnectorProfilePropertiesTypeDef",
    "SnowflakeConnectorProfilePropertiesTypeDef",
    "VeevaConnectorProfilePropertiesTypeDef",
    "ZendeskConnectorProfilePropertiesTypeDef",
    "PrivateConnectionProvisioningStateTypeDef",
    "LambdaConnectorProvisioningConfigOutputTypeDef",
    "LambdaConnectorProvisioningConfigTypeDef",
    "CreateConnectorProfileResponseTypeDef",
    "CreateFlowResponseTypeDef",
    "CustomAuthCredentialsTypeDef",
    "ErrorHandlingConfigOutputTypeDef",
    "ErrorHandlingConfigTypeDef",
    "OAuth2PropertiesOutputTypeDef",
    "OAuth2PropertiesTypeDef",
    "DataTransferApiTypeDef",
    "CustomerProfilesDestinationPropertiesOutputTypeDef",
    "CustomerProfilesDestinationPropertiesTypeDef",
    "DatadogSourcePropertiesOutputTypeDef",
    "DatadogSourcePropertiesTypeDef",
    "DeleteConnectorProfileRequestRequestTypeDef",
    "DeleteFlowRequestRequestTypeDef",
    "DescribeConnectorEntityRequestRequestTypeDef",
    "DescribeConnectorProfilesRequestRequestTypeDef",
    "DescribeConnectorRequestRequestTypeDef",
    "DescribeConnectorsRequestRequestTypeDef",
    "DescribeFlowExecutionRecordsRequestRequestTypeDef",
    "DescribeFlowRequestRequestTypeDef",
    "ExecutionDetailsTypeDef",
    "DynatraceSourcePropertiesOutputTypeDef",
    "DynatraceSourcePropertiesTypeDef",
    "ErrorInfoTypeDef",
    "RangeTypeDef",
    "GlueDataCatalogConfigOutputTypeDef",
    "GlueDataCatalogConfigTypeDef",
    "GoogleAnalyticsSourcePropertiesOutputTypeDef",
    "GoogleAnalyticsSourcePropertiesTypeDef",
    "IncrementalPullConfigOutputTypeDef",
    "IncrementalPullConfigTypeDef",
    "InforNexusSourcePropertiesOutputTypeDef",
    "InforNexusSourcePropertiesTypeDef",
    "ListConnectorEntitiesRequestRequestTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MarketoSourcePropertiesOutputTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "RegistrationOutputTypeDef",
    "OAuth2CustomParameterTypeDef",
    "OAuthPropertiesOutputTypeDef",
    "OAuthPropertiesTypeDef",
    "PardotSourcePropertiesOutputTypeDef",
    "PardotSourcePropertiesTypeDef",
    "PrefixConfigOutputTypeDef",
    "PrefixConfigTypeDef",
    "RegisterConnectorResponseTypeDef",
    "ResetConnectorMetadataCacheRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3InputFormatConfigOutputTypeDef",
    "S3InputFormatConfigTypeDef",
    "SuccessResponseHandlingConfigOutputTypeDef",
    "SuccessResponseHandlingConfigTypeDef",
    "SAPODataSourcePropertiesOutputTypeDef",
    "SAPODataSourcePropertiesTypeDef",
    "SalesforceSourcePropertiesOutputTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesOutputTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "ServiceNowSourcePropertiesOutputTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SingularSourcePropertiesOutputTypeDef",
    "SingularSourcePropertiesTypeDef",
    "SlackSourcePropertiesOutputTypeDef",
    "SlackSourcePropertiesTypeDef",
    "TrendmicroSourcePropertiesOutputTypeDef",
    "VeevaSourcePropertiesOutputTypeDef",
    "ZendeskSourcePropertiesOutputTypeDef",
    "TrendmicroSourcePropertiesTypeDef",
    "VeevaSourcePropertiesTypeDef",
    "ZendeskSourcePropertiesTypeDef",
    "StartFlowRequestRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowRequestRequestTypeDef",
    "StopFlowResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnregisterConnectorRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectorProfileResponseTypeDef",
    "UpdateConnectorRegistrationResponseTypeDef",
    "UpdateFlowResponseTypeDef",
    "CustomAuthConfigTypeDef",
    "CustomConnectorSourcePropertiesOutputTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListConnectorEntitiesResponseTypeDef",
    "ConnectorMetadataTypeDef",
    "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
    "HoneycodeConnectorProfileCredentialsTypeDef",
    "MarketoConnectorProfileCredentialsTypeDef",
    "OAuth2CredentialsTypeDef",
    "OAuthCredentialsTypeDef",
    "PardotConnectorProfileCredentialsTypeDef",
    "SalesforceConnectorProfileCredentialsTypeDef",
    "SlackConnectorProfileCredentialsTypeDef",
    "ZendeskConnectorProfileCredentialsTypeDef",
    "TaskOutputTypeDef",
    "TaskTypeDef",
    "ConnectorProvisioningConfigOutputTypeDef",
    "ConnectorProvisioningConfigTypeDef",
    "CustomConnectorDestinationPropertiesOutputTypeDef",
    "EventBridgeDestinationPropertiesOutputTypeDef",
    "HoneycodeDestinationPropertiesOutputTypeDef",
    "MarketoDestinationPropertiesOutputTypeDef",
    "RedshiftDestinationPropertiesOutputTypeDef",
    "SalesforceDestinationPropertiesOutputTypeDef",
    "SnowflakeDestinationPropertiesOutputTypeDef",
    "ZendeskDestinationPropertiesOutputTypeDef",
    "CustomConnectorDestinationPropertiesTypeDef",
    "EventBridgeDestinationPropertiesTypeDef",
    "HoneycodeDestinationPropertiesTypeDef",
    "MarketoDestinationPropertiesTypeDef",
    "RedshiftDestinationPropertiesTypeDef",
    "SalesforceDestinationPropertiesTypeDef",
    "SnowflakeDestinationPropertiesTypeDef",
    "ZendeskDestinationPropertiesTypeDef",
    "CustomConnectorProfilePropertiesOutputTypeDef",
    "CustomConnectorProfilePropertiesTypeDef",
    "CustomConnectorSourcePropertiesTypeDef",
    "FlowDefinitionTypeDef",
    "ExecutionResultTypeDef",
    "FieldTypeDetailsTypeDef",
    "MetadataCatalogConfigOutputTypeDef",
    "MetadataCatalogConfigTypeDef",
    "MetadataCatalogDetailTypeDef",
    "OAuth2DefaultsTypeDef",
    "SAPODataConnectorProfilePropertiesOutputTypeDef",
    "SAPODataConnectorProfilePropertiesTypeDef",
    "S3OutputFormatConfigOutputTypeDef",
    "UpsolverS3OutputFormatConfigOutputTypeDef",
    "S3OutputFormatConfigTypeDef",
    "UpsolverS3OutputFormatConfigTypeDef",
    "S3SourcePropertiesOutputTypeDef",
    "S3SourcePropertiesTypeDef",
    "SAPODataDestinationPropertiesOutputTypeDef",
    "SAPODataDestinationPropertiesTypeDef",
    "TriggerPropertiesOutputTypeDef",
    "TriggerPropertiesTypeDef",
    "CustomConnectorProfileCredentialsTypeDef",
    "SAPODataConnectorProfileCredentialsTypeDef",
    "RegisterConnectorRequestRequestTypeDef",
    "UpdateConnectorRegistrationRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "SupportedFieldTypeDetailsTypeDef",
    "ExecutionRecordTypeDef",
    "AuthenticationConfigTypeDef",
    "ConnectorProfilePropertiesOutputTypeDef",
    "ConnectorProfilePropertiesTypeDef",
    "S3DestinationPropertiesOutputTypeDef",
    "UpsolverDestinationPropertiesOutputTypeDef",
    "S3DestinationPropertiesTypeDef",
    "UpsolverDestinationPropertiesTypeDef",
    "SourceConnectorPropertiesOutputTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "TriggerConfigOutputTypeDef",
    "TriggerConfigTypeDef",
    "ConnectorProfileCredentialsTypeDef",
    "ConnectorEntityFieldTypeDef",
    "DescribeFlowExecutionRecordsResponseTypeDef",
    "ConnectorConfigurationTypeDef",
    "ConnectorProfileTypeDef",
    "DestinationConnectorPropertiesOutputTypeDef",
    "DestinationConnectorPropertiesTypeDef",
    "SourceFlowConfigOutputTypeDef",
    "SourceFlowConfigTypeDef",
    "ConnectorProfileConfigTypeDef",
    "DescribeConnectorEntityResponseTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeConnectorsResponseTypeDef",
    "DescribeConnectorProfilesResponseTypeDef",
    "DestinationFlowConfigOutputTypeDef",
    "DestinationFlowConfigTypeDef",
    "CreateConnectorProfileRequestRequestTypeDef",
    "UpdateConnectorProfileRequestRequestTypeDef",
    "DescribeFlowResponseTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "UpdateFlowRequestRequestTypeDef",
)

AggregationConfigOutputTypeDef = TypedDict(
    "AggregationConfigOutputTypeDef",
    {
        "aggregationType": AggregationTypeType,
        "targetFileSize": int,
    },
    total=False,
)

AggregationConfigTypeDef = TypedDict(
    "AggregationConfigTypeDef",
    {
        "aggregationType": AggregationTypeType,
        "targetFileSize": int,
    },
    total=False,
)

AmplitudeConnectorProfileCredentialsTypeDef = TypedDict(
    "AmplitudeConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
        "secretKey": str,
    },
)

AmplitudeSourcePropertiesOutputTypeDef = TypedDict(
    "AmplitudeSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

AmplitudeSourcePropertiesTypeDef = TypedDict(
    "AmplitudeSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

_RequiredApiKeyCredentialsTypeDef = TypedDict(
    "_RequiredApiKeyCredentialsTypeDef",
    {
        "apiKey": str,
    },
)
_OptionalApiKeyCredentialsTypeDef = TypedDict(
    "_OptionalApiKeyCredentialsTypeDef",
    {
        "apiSecretKey": str,
    },
    total=False,
)

class ApiKeyCredentialsTypeDef(
    _RequiredApiKeyCredentialsTypeDef, _OptionalApiKeyCredentialsTypeDef
):
    pass

AuthParameterTypeDef = TypedDict(
    "AuthParameterTypeDef",
    {
        "key": str,
        "isRequired": bool,
        "label": str,
        "description": str,
        "isSensitiveField": bool,
        "connectorSuppliedValues": List[str],
    },
    total=False,
)

BasicAuthCredentialsTypeDef = TypedDict(
    "BasicAuthCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

_RequiredCancelFlowExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredCancelFlowExecutionsRequestRequestTypeDef",
    {
        "flowName": str,
    },
)
_OptionalCancelFlowExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalCancelFlowExecutionsRequestRequestTypeDef",
    {
        "executionIds": Sequence[str],
    },
    total=False,
)

class CancelFlowExecutionsRequestRequestTypeDef(
    _RequiredCancelFlowExecutionsRequestRequestTypeDef,
    _OptionalCancelFlowExecutionsRequestRequestTypeDef,
):
    pass

CancelFlowExecutionsResponseTypeDef = TypedDict(
    "CancelFlowExecutionsResponseTypeDef",
    {
        "invalidExecutions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectorRuntimeSettingTypeDef = TypedDict(
    "ConnectorRuntimeSettingTypeDef",
    {
        "key": str,
        "dataType": str,
        "isRequired": bool,
        "label": str,
        "description": str,
        "scope": str,
        "connectorSuppliedValueOptions": List[str],
    },
    total=False,
)

DataTransferApiOutputTypeDef = TypedDict(
    "DataTransferApiOutputTypeDef",
    {
        "Name": str,
        "Type": DataTransferApiTypeType,
    },
    total=False,
)

ConnectorDetailTypeDef = TypedDict(
    "ConnectorDetailTypeDef",
    {
        "connectorDescription": str,
        "connectorName": str,
        "connectorOwner": str,
        "connectorVersion": str,
        "applicationType": str,
        "connectorType": ConnectorTypeType,
        "connectorLabel": str,
        "registeredAt": datetime,
        "registeredBy": str,
        "connectorProvisioningType": Literal["LAMBDA"],
        "connectorModes": List[str],
        "supportedDataTransferTypes": List[SupportedDataTransferTypeType],
    },
    total=False,
)

DestinationFieldPropertiesTypeDef = TypedDict(
    "DestinationFieldPropertiesTypeDef",
    {
        "isCreatable": bool,
        "isNullable": bool,
        "isUpsertable": bool,
        "isUpdatable": bool,
        "isDefaultedOnCreate": bool,
        "supportedWriteOperations": List[WriteOperationTypeType],
    },
    total=False,
)

SourceFieldPropertiesTypeDef = TypedDict(
    "SourceFieldPropertiesTypeDef",
    {
        "isRetrievable": bool,
        "isQueryable": bool,
        "isTimestampFieldForIncrementalQueries": bool,
    },
    total=False,
)

_RequiredConnectorEntityTypeDef = TypedDict(
    "_RequiredConnectorEntityTypeDef",
    {
        "name": str,
    },
)
_OptionalConnectorEntityTypeDef = TypedDict(
    "_OptionalConnectorEntityTypeDef",
    {
        "label": str,
        "hasNestedEntities": bool,
    },
    total=False,
)

class ConnectorEntityTypeDef(_RequiredConnectorEntityTypeDef, _OptionalConnectorEntityTypeDef):
    pass

GoogleAnalyticsMetadataTypeDef = TypedDict(
    "GoogleAnalyticsMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

HoneycodeMetadataTypeDef = TypedDict(
    "HoneycodeMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

SalesforceMetadataTypeDef = TypedDict(
    "SalesforceMetadataTypeDef",
    {
        "oAuthScopes": List[str],
        "dataTransferApis": List[SalesforceDataTransferApiType],
        "oauth2GrantTypesSupported": List[OAuth2GrantTypeType],
    },
    total=False,
)

SlackMetadataTypeDef = TypedDict(
    "SlackMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

SnowflakeMetadataTypeDef = TypedDict(
    "SnowflakeMetadataTypeDef",
    {
        "supportedRegions": List[str],
    },
    total=False,
)

ZendeskMetadataTypeDef = TypedDict(
    "ZendeskMetadataTypeDef",
    {
        "oAuthScopes": List[str],
    },
    total=False,
)

ConnectorOAuthRequestTypeDef = TypedDict(
    "ConnectorOAuthRequestTypeDef",
    {
        "authCode": str,
        "redirectUri": str,
    },
    total=False,
)

ConnectorOperatorOutputTypeDef = TypedDict(
    "ConnectorOperatorOutputTypeDef",
    {
        "Amplitude": Literal["BETWEEN"],
        "Datadog": DatadogConnectorOperatorType,
        "Dynatrace": DynatraceConnectorOperatorType,
        "GoogleAnalytics": GoogleAnalyticsConnectorOperatorType,
        "InforNexus": InforNexusConnectorOperatorType,
        "Marketo": MarketoConnectorOperatorType,
        "S3": S3ConnectorOperatorType,
        "Salesforce": SalesforceConnectorOperatorType,
        "ServiceNow": ServiceNowConnectorOperatorType,
        "Singular": SingularConnectorOperatorType,
        "Slack": SlackConnectorOperatorType,
        "Trendmicro": TrendmicroConnectorOperatorType,
        "Veeva": VeevaConnectorOperatorType,
        "Zendesk": ZendeskConnectorOperatorType,
        "SAPOData": SAPODataConnectorOperatorType,
        "CustomConnector": OperatorType,
        "Pardot": PardotConnectorOperatorType,
    },
    total=False,
)

ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Amplitude": Literal["BETWEEN"],
        "Datadog": DatadogConnectorOperatorType,
        "Dynatrace": DynatraceConnectorOperatorType,
        "GoogleAnalytics": GoogleAnalyticsConnectorOperatorType,
        "InforNexus": InforNexusConnectorOperatorType,
        "Marketo": MarketoConnectorOperatorType,
        "S3": S3ConnectorOperatorType,
        "Salesforce": SalesforceConnectorOperatorType,
        "ServiceNow": ServiceNowConnectorOperatorType,
        "Singular": SingularConnectorOperatorType,
        "Slack": SlackConnectorOperatorType,
        "Trendmicro": TrendmicroConnectorOperatorType,
        "Veeva": VeevaConnectorOperatorType,
        "Zendesk": ZendeskConnectorOperatorType,
        "SAPOData": SAPODataConnectorOperatorType,
        "CustomConnector": OperatorType,
        "Pardot": PardotConnectorOperatorType,
    },
    total=False,
)

DatadogConnectorProfileCredentialsTypeDef = TypedDict(
    "DatadogConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
        "applicationKey": str,
    },
)

DynatraceConnectorProfileCredentialsTypeDef = TypedDict(
    "DynatraceConnectorProfileCredentialsTypeDef",
    {
        "apiToken": str,
    },
)

InforNexusConnectorProfileCredentialsTypeDef = TypedDict(
    "InforNexusConnectorProfileCredentialsTypeDef",
    {
        "accessKeyId": str,
        "userId": str,
        "secretAccessKey": str,
        "datakey": str,
    },
)

RedshiftConnectorProfileCredentialsTypeDef = TypedDict(
    "RedshiftConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
    total=False,
)

ServiceNowConnectorProfileCredentialsTypeDef = TypedDict(
    "ServiceNowConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

SingularConnectorProfileCredentialsTypeDef = TypedDict(
    "SingularConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
    },
)

SnowflakeConnectorProfileCredentialsTypeDef = TypedDict(
    "SnowflakeConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

TrendmicroConnectorProfileCredentialsTypeDef = TypedDict(
    "TrendmicroConnectorProfileCredentialsTypeDef",
    {
        "apiSecretKey": str,
    },
)

VeevaConnectorProfileCredentialsTypeDef = TypedDict(
    "VeevaConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

DatadogConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "DatadogConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
    },
)

DynatraceConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "DynatraceConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
    },
)

InforNexusConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "InforNexusConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
    },
)

MarketoConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "MarketoConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
    },
)

PardotConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "PardotConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
        "isSandboxEnvironment": bool,
        "businessUnitId": str,
    },
    total=False,
)

_RequiredRedshiftConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "_RequiredRedshiftConnectorProfilePropertiesOutputTypeDef",
    {
        "bucketName": str,
        "roleArn": str,
    },
)
_OptionalRedshiftConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "_OptionalRedshiftConnectorProfilePropertiesOutputTypeDef",
    {
        "databaseUrl": str,
        "bucketPrefix": str,
        "dataApiRoleArn": str,
        "isRedshiftServerless": bool,
        "clusterIdentifier": str,
        "workgroupName": str,
        "databaseName": str,
    },
    total=False,
)

class RedshiftConnectorProfilePropertiesOutputTypeDef(
    _RequiredRedshiftConnectorProfilePropertiesOutputTypeDef,
    _OptionalRedshiftConnectorProfilePropertiesOutputTypeDef,
):
    pass

SalesforceConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "SalesforceConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
        "isSandboxEnvironment": bool,
        "usePrivateLinkForMetadataAndAuthorization": bool,
    },
    total=False,
)

ServiceNowConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "ServiceNowConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
    },
)

SlackConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "SlackConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
    },
)

_RequiredSnowflakeConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "_RequiredSnowflakeConnectorProfilePropertiesOutputTypeDef",
    {
        "warehouse": str,
        "stage": str,
        "bucketName": str,
    },
)
_OptionalSnowflakeConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "_OptionalSnowflakeConnectorProfilePropertiesOutputTypeDef",
    {
        "bucketPrefix": str,
        "privateLinkServiceName": str,
        "accountName": str,
        "region": str,
    },
    total=False,
)

class SnowflakeConnectorProfilePropertiesOutputTypeDef(
    _RequiredSnowflakeConnectorProfilePropertiesOutputTypeDef,
    _OptionalSnowflakeConnectorProfilePropertiesOutputTypeDef,
):
    pass

VeevaConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "VeevaConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
    },
)

ZendeskConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "ZendeskConnectorProfilePropertiesOutputTypeDef",
    {
        "instanceUrl": str,
    },
)

DatadogConnectorProfilePropertiesTypeDef = TypedDict(
    "DatadogConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

DynatraceConnectorProfilePropertiesTypeDef = TypedDict(
    "DynatraceConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

InforNexusConnectorProfilePropertiesTypeDef = TypedDict(
    "InforNexusConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

MarketoConnectorProfilePropertiesTypeDef = TypedDict(
    "MarketoConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

PardotConnectorProfilePropertiesTypeDef = TypedDict(
    "PardotConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
        "isSandboxEnvironment": bool,
        "businessUnitId": str,
    },
    total=False,
)

_RequiredRedshiftConnectorProfilePropertiesTypeDef = TypedDict(
    "_RequiredRedshiftConnectorProfilePropertiesTypeDef",
    {
        "bucketName": str,
        "roleArn": str,
    },
)
_OptionalRedshiftConnectorProfilePropertiesTypeDef = TypedDict(
    "_OptionalRedshiftConnectorProfilePropertiesTypeDef",
    {
        "databaseUrl": str,
        "bucketPrefix": str,
        "dataApiRoleArn": str,
        "isRedshiftServerless": bool,
        "clusterIdentifier": str,
        "workgroupName": str,
        "databaseName": str,
    },
    total=False,
)

class RedshiftConnectorProfilePropertiesTypeDef(
    _RequiredRedshiftConnectorProfilePropertiesTypeDef,
    _OptionalRedshiftConnectorProfilePropertiesTypeDef,
):
    pass

SalesforceConnectorProfilePropertiesTypeDef = TypedDict(
    "SalesforceConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
        "isSandboxEnvironment": bool,
        "usePrivateLinkForMetadataAndAuthorization": bool,
    },
    total=False,
)

ServiceNowConnectorProfilePropertiesTypeDef = TypedDict(
    "ServiceNowConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

SlackConnectorProfilePropertiesTypeDef = TypedDict(
    "SlackConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

_RequiredSnowflakeConnectorProfilePropertiesTypeDef = TypedDict(
    "_RequiredSnowflakeConnectorProfilePropertiesTypeDef",
    {
        "warehouse": str,
        "stage": str,
        "bucketName": str,
    },
)
_OptionalSnowflakeConnectorProfilePropertiesTypeDef = TypedDict(
    "_OptionalSnowflakeConnectorProfilePropertiesTypeDef",
    {
        "bucketPrefix": str,
        "privateLinkServiceName": str,
        "accountName": str,
        "region": str,
    },
    total=False,
)

class SnowflakeConnectorProfilePropertiesTypeDef(
    _RequiredSnowflakeConnectorProfilePropertiesTypeDef,
    _OptionalSnowflakeConnectorProfilePropertiesTypeDef,
):
    pass

VeevaConnectorProfilePropertiesTypeDef = TypedDict(
    "VeevaConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

ZendeskConnectorProfilePropertiesTypeDef = TypedDict(
    "ZendeskConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

PrivateConnectionProvisioningStateTypeDef = TypedDict(
    "PrivateConnectionProvisioningStateTypeDef",
    {
        "status": PrivateConnectionProvisioningStatusType,
        "failureMessage": str,
        "failureCause": PrivateConnectionProvisioningFailureCauseType,
    },
    total=False,
)

LambdaConnectorProvisioningConfigOutputTypeDef = TypedDict(
    "LambdaConnectorProvisioningConfigOutputTypeDef",
    {
        "lambdaArn": str,
    },
)

LambdaConnectorProvisioningConfigTypeDef = TypedDict(
    "LambdaConnectorProvisioningConfigTypeDef",
    {
        "lambdaArn": str,
    },
)

CreateConnectorProfileResponseTypeDef = TypedDict(
    "CreateConnectorProfileResponseTypeDef",
    {
        "connectorProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomAuthCredentialsTypeDef = TypedDict(
    "_RequiredCustomAuthCredentialsTypeDef",
    {
        "customAuthenticationType": str,
    },
)
_OptionalCustomAuthCredentialsTypeDef = TypedDict(
    "_OptionalCustomAuthCredentialsTypeDef",
    {
        "credentialsMap": Mapping[str, str],
    },
    total=False,
)

class CustomAuthCredentialsTypeDef(
    _RequiredCustomAuthCredentialsTypeDef, _OptionalCustomAuthCredentialsTypeDef
):
    pass

ErrorHandlingConfigOutputTypeDef = TypedDict(
    "ErrorHandlingConfigOutputTypeDef",
    {
        "failOnFirstDestinationError": bool,
        "bucketPrefix": str,
        "bucketName": str,
    },
    total=False,
)

ErrorHandlingConfigTypeDef = TypedDict(
    "ErrorHandlingConfigTypeDef",
    {
        "failOnFirstDestinationError": bool,
        "bucketPrefix": str,
        "bucketName": str,
    },
    total=False,
)

_RequiredOAuth2PropertiesOutputTypeDef = TypedDict(
    "_RequiredOAuth2PropertiesOutputTypeDef",
    {
        "tokenUrl": str,
        "oAuth2GrantType": OAuth2GrantTypeType,
    },
)
_OptionalOAuth2PropertiesOutputTypeDef = TypedDict(
    "_OptionalOAuth2PropertiesOutputTypeDef",
    {
        "tokenUrlCustomProperties": Dict[str, str],
    },
    total=False,
)

class OAuth2PropertiesOutputTypeDef(
    _RequiredOAuth2PropertiesOutputTypeDef, _OptionalOAuth2PropertiesOutputTypeDef
):
    pass

_RequiredOAuth2PropertiesTypeDef = TypedDict(
    "_RequiredOAuth2PropertiesTypeDef",
    {
        "tokenUrl": str,
        "oAuth2GrantType": OAuth2GrantTypeType,
    },
)
_OptionalOAuth2PropertiesTypeDef = TypedDict(
    "_OptionalOAuth2PropertiesTypeDef",
    {
        "tokenUrlCustomProperties": Mapping[str, str],
    },
    total=False,
)

class OAuth2PropertiesTypeDef(_RequiredOAuth2PropertiesTypeDef, _OptionalOAuth2PropertiesTypeDef):
    pass

DataTransferApiTypeDef = TypedDict(
    "DataTransferApiTypeDef",
    {
        "Name": str,
        "Type": DataTransferApiTypeType,
    },
    total=False,
)

_RequiredCustomerProfilesDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredCustomerProfilesDestinationPropertiesOutputTypeDef",
    {
        "domainName": str,
    },
)
_OptionalCustomerProfilesDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalCustomerProfilesDestinationPropertiesOutputTypeDef",
    {
        "objectTypeName": str,
    },
    total=False,
)

class CustomerProfilesDestinationPropertiesOutputTypeDef(
    _RequiredCustomerProfilesDestinationPropertiesOutputTypeDef,
    _OptionalCustomerProfilesDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredCustomerProfilesDestinationPropertiesTypeDef = TypedDict(
    "_RequiredCustomerProfilesDestinationPropertiesTypeDef",
    {
        "domainName": str,
    },
)
_OptionalCustomerProfilesDestinationPropertiesTypeDef = TypedDict(
    "_OptionalCustomerProfilesDestinationPropertiesTypeDef",
    {
        "objectTypeName": str,
    },
    total=False,
)

class CustomerProfilesDestinationPropertiesTypeDef(
    _RequiredCustomerProfilesDestinationPropertiesTypeDef,
    _OptionalCustomerProfilesDestinationPropertiesTypeDef,
):
    pass

DatadogSourcePropertiesOutputTypeDef = TypedDict(
    "DatadogSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

DatadogSourcePropertiesTypeDef = TypedDict(
    "DatadogSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

_RequiredDeleteConnectorProfileRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
    },
)
_OptionalDeleteConnectorProfileRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteConnectorProfileRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)

class DeleteConnectorProfileRequestRequestTypeDef(
    _RequiredDeleteConnectorProfileRequestRequestTypeDef,
    _OptionalDeleteConnectorProfileRequestRequestTypeDef,
):
    pass

_RequiredDeleteFlowRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)
_OptionalDeleteFlowRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFlowRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)

class DeleteFlowRequestRequestTypeDef(
    _RequiredDeleteFlowRequestRequestTypeDef, _OptionalDeleteFlowRequestRequestTypeDef
):
    pass

_RequiredDescribeConnectorEntityRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectorEntityRequestRequestTypeDef",
    {
        "connectorEntityName": str,
    },
)
_OptionalDescribeConnectorEntityRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectorEntityRequestRequestTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "connectorProfileName": str,
        "apiVersion": str,
    },
    total=False,
)

class DescribeConnectorEntityRequestRequestTypeDef(
    _RequiredDescribeConnectorEntityRequestRequestTypeDef,
    _OptionalDescribeConnectorEntityRequestRequestTypeDef,
):
    pass

DescribeConnectorProfilesRequestRequestTypeDef = TypedDict(
    "DescribeConnectorProfilesRequestRequestTypeDef",
    {
        "connectorProfileNames": Sequence[str],
        "connectorType": ConnectorTypeType,
        "connectorLabel": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredDescribeConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectorRequestRequestTypeDef",
    {
        "connectorType": ConnectorTypeType,
    },
)
_OptionalDescribeConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectorRequestRequestTypeDef",
    {
        "connectorLabel": str,
    },
    total=False,
)

class DescribeConnectorRequestRequestTypeDef(
    _RequiredDescribeConnectorRequestRequestTypeDef, _OptionalDescribeConnectorRequestRequestTypeDef
):
    pass

DescribeConnectorsRequestRequestTypeDef = TypedDict(
    "DescribeConnectorsRequestRequestTypeDef",
    {
        "connectorTypes": Sequence[ConnectorTypeType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredDescribeFlowExecutionRecordsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFlowExecutionRecordsRequestRequestTypeDef",
    {
        "flowName": str,
    },
)
_OptionalDescribeFlowExecutionRecordsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFlowExecutionRecordsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class DescribeFlowExecutionRecordsRequestRequestTypeDef(
    _RequiredDescribeFlowExecutionRecordsRequestRequestTypeDef,
    _OptionalDescribeFlowExecutionRecordsRequestRequestTypeDef,
):
    pass

DescribeFlowRequestRequestTypeDef = TypedDict(
    "DescribeFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "mostRecentExecutionMessage": str,
        "mostRecentExecutionTime": datetime,
        "mostRecentExecutionStatus": ExecutionStatusType,
    },
    total=False,
)

DynatraceSourcePropertiesOutputTypeDef = TypedDict(
    "DynatraceSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

DynatraceSourcePropertiesTypeDef = TypedDict(
    "DynatraceSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "putFailuresCount": int,
        "executionMessage": str,
    },
    total=False,
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "maximum": float,
        "minimum": float,
    },
    total=False,
)

GlueDataCatalogConfigOutputTypeDef = TypedDict(
    "GlueDataCatalogConfigOutputTypeDef",
    {
        "roleArn": str,
        "databaseName": str,
        "tablePrefix": str,
    },
)

GlueDataCatalogConfigTypeDef = TypedDict(
    "GlueDataCatalogConfigTypeDef",
    {
        "roleArn": str,
        "databaseName": str,
        "tablePrefix": str,
    },
)

GoogleAnalyticsSourcePropertiesOutputTypeDef = TypedDict(
    "GoogleAnalyticsSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

GoogleAnalyticsSourcePropertiesTypeDef = TypedDict(
    "GoogleAnalyticsSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

IncrementalPullConfigOutputTypeDef = TypedDict(
    "IncrementalPullConfigOutputTypeDef",
    {
        "datetimeTypeFieldName": str,
    },
    total=False,
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "datetimeTypeFieldName": str,
    },
    total=False,
)

InforNexusSourcePropertiesOutputTypeDef = TypedDict(
    "InforNexusSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

InforNexusSourcePropertiesTypeDef = TypedDict(
    "InforNexusSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ListConnectorEntitiesRequestRequestTypeDef = TypedDict(
    "ListConnectorEntitiesRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "entitiesPath": str,
        "apiVersion": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListFlowsRequestRequestTypeDef = TypedDict(
    "ListFlowsRequestRequestTypeDef",
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

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MarketoSourcePropertiesOutputTypeDef = TypedDict(
    "MarketoSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

RegistrationOutputTypeDef = TypedDict(
    "RegistrationOutputTypeDef",
    {
        "message": str,
        "result": str,
        "status": ExecutionStatusType,
    },
    total=False,
)

OAuth2CustomParameterTypeDef = TypedDict(
    "OAuth2CustomParameterTypeDef",
    {
        "key": str,
        "isRequired": bool,
        "label": str,
        "description": str,
        "isSensitiveField": bool,
        "connectorSuppliedValues": List[str],
        "type": OAuth2CustomPropTypeType,
    },
    total=False,
)

OAuthPropertiesOutputTypeDef = TypedDict(
    "OAuthPropertiesOutputTypeDef",
    {
        "tokenUrl": str,
        "authCodeUrl": str,
        "oAuthScopes": List[str],
    },
)

OAuthPropertiesTypeDef = TypedDict(
    "OAuthPropertiesTypeDef",
    {
        "tokenUrl": str,
        "authCodeUrl": str,
        "oAuthScopes": Sequence[str],
    },
)

PardotSourcePropertiesOutputTypeDef = TypedDict(
    "PardotSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

PardotSourcePropertiesTypeDef = TypedDict(
    "PardotSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

PrefixConfigOutputTypeDef = TypedDict(
    "PrefixConfigOutputTypeDef",
    {
        "prefixType": PrefixTypeType,
        "prefixFormat": PrefixFormatType,
        "pathPrefixHierarchy": List[PathPrefixType],
    },
    total=False,
)

PrefixConfigTypeDef = TypedDict(
    "PrefixConfigTypeDef",
    {
        "prefixType": PrefixTypeType,
        "prefixFormat": PrefixFormatType,
        "pathPrefixHierarchy": Sequence[PathPrefixType],
    },
    total=False,
)

RegisterConnectorResponseTypeDef = TypedDict(
    "RegisterConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetConnectorMetadataCacheRequestRequestTypeDef = TypedDict(
    "ResetConnectorMetadataCacheRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "connectorEntityName": str,
        "entitiesPath": str,
        "apiVersion": str,
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

S3InputFormatConfigOutputTypeDef = TypedDict(
    "S3InputFormatConfigOutputTypeDef",
    {
        "s3InputFileType": S3InputFileTypeType,
    },
    total=False,
)

S3InputFormatConfigTypeDef = TypedDict(
    "S3InputFormatConfigTypeDef",
    {
        "s3InputFileType": S3InputFileTypeType,
    },
    total=False,
)

SuccessResponseHandlingConfigOutputTypeDef = TypedDict(
    "SuccessResponseHandlingConfigOutputTypeDef",
    {
        "bucketPrefix": str,
        "bucketName": str,
    },
    total=False,
)

SuccessResponseHandlingConfigTypeDef = TypedDict(
    "SuccessResponseHandlingConfigTypeDef",
    {
        "bucketPrefix": str,
        "bucketName": str,
    },
    total=False,
)

SAPODataSourcePropertiesOutputTypeDef = TypedDict(
    "SAPODataSourcePropertiesOutputTypeDef",
    {
        "objectPath": str,
    },
    total=False,
)

SAPODataSourcePropertiesTypeDef = TypedDict(
    "SAPODataSourcePropertiesTypeDef",
    {
        "objectPath": str,
    },
    total=False,
)

_RequiredSalesforceSourcePropertiesOutputTypeDef = TypedDict(
    "_RequiredSalesforceSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)
_OptionalSalesforceSourcePropertiesOutputTypeDef = TypedDict(
    "_OptionalSalesforceSourcePropertiesOutputTypeDef",
    {
        "enableDynamicFieldUpdate": bool,
        "includeDeletedRecords": bool,
        "dataTransferApi": SalesforceDataTransferApiType,
    },
    total=False,
)

class SalesforceSourcePropertiesOutputTypeDef(
    _RequiredSalesforceSourcePropertiesOutputTypeDef,
    _OptionalSalesforceSourcePropertiesOutputTypeDef,
):
    pass

_RequiredSalesforceSourcePropertiesTypeDef = TypedDict(
    "_RequiredSalesforceSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalSalesforceSourcePropertiesTypeDef = TypedDict(
    "_OptionalSalesforceSourcePropertiesTypeDef",
    {
        "enableDynamicFieldUpdate": bool,
        "includeDeletedRecords": bool,
        "dataTransferApi": SalesforceDataTransferApiType,
    },
    total=False,
)

class SalesforceSourcePropertiesTypeDef(
    _RequiredSalesforceSourcePropertiesTypeDef, _OptionalSalesforceSourcePropertiesTypeDef
):
    pass

_RequiredScheduledTriggerPropertiesOutputTypeDef = TypedDict(
    "_RequiredScheduledTriggerPropertiesOutputTypeDef",
    {
        "scheduleExpression": str,
    },
)
_OptionalScheduledTriggerPropertiesOutputTypeDef = TypedDict(
    "_OptionalScheduledTriggerPropertiesOutputTypeDef",
    {
        "dataPullMode": DataPullModeType,
        "scheduleStartTime": datetime,
        "scheduleEndTime": datetime,
        "timezone": str,
        "scheduleOffset": int,
        "firstExecutionFrom": datetime,
        "flowErrorDeactivationThreshold": int,
    },
    total=False,
)

class ScheduledTriggerPropertiesOutputTypeDef(
    _RequiredScheduledTriggerPropertiesOutputTypeDef,
    _OptionalScheduledTriggerPropertiesOutputTypeDef,
):
    pass

_RequiredScheduledTriggerPropertiesTypeDef = TypedDict(
    "_RequiredScheduledTriggerPropertiesTypeDef",
    {
        "scheduleExpression": str,
    },
)
_OptionalScheduledTriggerPropertiesTypeDef = TypedDict(
    "_OptionalScheduledTriggerPropertiesTypeDef",
    {
        "dataPullMode": DataPullModeType,
        "scheduleStartTime": Union[datetime, str],
        "scheduleEndTime": Union[datetime, str],
        "timezone": str,
        "scheduleOffset": int,
        "firstExecutionFrom": Union[datetime, str],
        "flowErrorDeactivationThreshold": int,
    },
    total=False,
)

class ScheduledTriggerPropertiesTypeDef(
    _RequiredScheduledTriggerPropertiesTypeDef, _OptionalScheduledTriggerPropertiesTypeDef
):
    pass

ServiceNowSourcePropertiesOutputTypeDef = TypedDict(
    "ServiceNowSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SingularSourcePropertiesOutputTypeDef = TypedDict(
    "SingularSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

SingularSourcePropertiesTypeDef = TypedDict(
    "SingularSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SlackSourcePropertiesOutputTypeDef = TypedDict(
    "SlackSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

SlackSourcePropertiesTypeDef = TypedDict(
    "SlackSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

TrendmicroSourcePropertiesOutputTypeDef = TypedDict(
    "TrendmicroSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

_RequiredVeevaSourcePropertiesOutputTypeDef = TypedDict(
    "_RequiredVeevaSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)
_OptionalVeevaSourcePropertiesOutputTypeDef = TypedDict(
    "_OptionalVeevaSourcePropertiesOutputTypeDef",
    {
        "documentType": str,
        "includeSourceFiles": bool,
        "includeRenditions": bool,
        "includeAllVersions": bool,
    },
    total=False,
)

class VeevaSourcePropertiesOutputTypeDef(
    _RequiredVeevaSourcePropertiesOutputTypeDef, _OptionalVeevaSourcePropertiesOutputTypeDef
):
    pass

ZendeskSourcePropertiesOutputTypeDef = TypedDict(
    "ZendeskSourcePropertiesOutputTypeDef",
    {
        "object": str,
    },
)

TrendmicroSourcePropertiesTypeDef = TypedDict(
    "TrendmicroSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

_RequiredVeevaSourcePropertiesTypeDef = TypedDict(
    "_RequiredVeevaSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalVeevaSourcePropertiesTypeDef = TypedDict(
    "_OptionalVeevaSourcePropertiesTypeDef",
    {
        "documentType": str,
        "includeSourceFiles": bool,
        "includeRenditions": bool,
        "includeAllVersions": bool,
    },
    total=False,
)

class VeevaSourcePropertiesTypeDef(
    _RequiredVeevaSourcePropertiesTypeDef, _OptionalVeevaSourcePropertiesTypeDef
):
    pass

ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

_RequiredStartFlowRequestRequestTypeDef = TypedDict(
    "_RequiredStartFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)
_OptionalStartFlowRequestRequestTypeDef = TypedDict(
    "_OptionalStartFlowRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartFlowRequestRequestTypeDef(
    _RequiredStartFlowRequestRequestTypeDef, _OptionalStartFlowRequestRequestTypeDef
):
    pass

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "executionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFlowRequestRequestTypeDef = TypedDict(
    "StopFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
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

_RequiredUnregisterConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredUnregisterConnectorRequestRequestTypeDef",
    {
        "connectorLabel": str,
    },
)
_OptionalUnregisterConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalUnregisterConnectorRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)

class UnregisterConnectorRequestRequestTypeDef(
    _RequiredUnregisterConnectorRequestRequestTypeDef,
    _OptionalUnregisterConnectorRequestRequestTypeDef,
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateConnectorProfileResponseTypeDef = TypedDict(
    "UpdateConnectorProfileResponseTypeDef",
    {
        "connectorProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectorRegistrationResponseTypeDef = TypedDict(
    "UpdateConnectorRegistrationResponseTypeDef",
    {
        "connectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "flowStatus": FlowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomAuthConfigTypeDef = TypedDict(
    "CustomAuthConfigTypeDef",
    {
        "customAuthenticationType": str,
        "authParameters": List[AuthParameterTypeDef],
    },
    total=False,
)

_RequiredCustomConnectorSourcePropertiesOutputTypeDef = TypedDict(
    "_RequiredCustomConnectorSourcePropertiesOutputTypeDef",
    {
        "entityName": str,
    },
)
_OptionalCustomConnectorSourcePropertiesOutputTypeDef = TypedDict(
    "_OptionalCustomConnectorSourcePropertiesOutputTypeDef",
    {
        "customProperties": Dict[str, str],
        "dataTransferApi": DataTransferApiOutputTypeDef,
    },
    total=False,
)

class CustomConnectorSourcePropertiesOutputTypeDef(
    _RequiredCustomConnectorSourcePropertiesOutputTypeDef,
    _OptionalCustomConnectorSourcePropertiesOutputTypeDef,
):
    pass

ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "connectors": List[ConnectorDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectorEntitiesResponseTypeDef = TypedDict(
    "ListConnectorEntitiesResponseTypeDef",
    {
        "connectorEntityMap": Dict[str, List[ConnectorEntityTypeDef]],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectorMetadataTypeDef = TypedDict(
    "ConnectorMetadataTypeDef",
    {
        "Amplitude": Dict[str, Any],
        "Datadog": Dict[str, Any],
        "Dynatrace": Dict[str, Any],
        "GoogleAnalytics": GoogleAnalyticsMetadataTypeDef,
        "InforNexus": Dict[str, Any],
        "Marketo": Dict[str, Any],
        "Redshift": Dict[str, Any],
        "S3": Dict[str, Any],
        "Salesforce": SalesforceMetadataTypeDef,
        "ServiceNow": Dict[str, Any],
        "Singular": Dict[str, Any],
        "Slack": SlackMetadataTypeDef,
        "Snowflake": SnowflakeMetadataTypeDef,
        "Trendmicro": Dict[str, Any],
        "Veeva": Dict[str, Any],
        "Zendesk": ZendeskMetadataTypeDef,
        "EventBridge": Dict[str, Any],
        "Upsolver": Dict[str, Any],
        "CustomerProfiles": Dict[str, Any],
        "Honeycode": HoneycodeMetadataTypeDef,
        "SAPOData": Dict[str, Any],
        "Pardot": Dict[str, Any],
    },
    total=False,
)

_RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
    },
    total=False,
)

class GoogleAnalyticsConnectorProfileCredentialsTypeDef(
    _RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef,
    _OptionalGoogleAnalyticsConnectorProfileCredentialsTypeDef,
):
    pass

HoneycodeConnectorProfileCredentialsTypeDef = TypedDict(
    "HoneycodeConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
    },
    total=False,
)

_RequiredMarketoConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredMarketoConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalMarketoConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalMarketoConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
    },
    total=False,
)

class MarketoConnectorProfileCredentialsTypeDef(
    _RequiredMarketoConnectorProfileCredentialsTypeDef,
    _OptionalMarketoConnectorProfileCredentialsTypeDef,
):
    pass

OAuth2CredentialsTypeDef = TypedDict(
    "OAuth2CredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
    },
    total=False,
)

_RequiredOAuthCredentialsTypeDef = TypedDict(
    "_RequiredOAuthCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalOAuthCredentialsTypeDef = TypedDict(
    "_OptionalOAuthCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
    },
    total=False,
)

class OAuthCredentialsTypeDef(_RequiredOAuthCredentialsTypeDef, _OptionalOAuthCredentialsTypeDef):
    pass

PardotConnectorProfileCredentialsTypeDef = TypedDict(
    "PardotConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
        "clientCredentialsArn": str,
    },
    total=False,
)

SalesforceConnectorProfileCredentialsTypeDef = TypedDict(
    "SalesforceConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "refreshToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
        "clientCredentialsArn": str,
        "oAuth2GrantType": OAuth2GrantTypeType,
        "jwtToken": str,
    },
    total=False,
)

_RequiredSlackConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredSlackConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalSlackConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalSlackConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
    },
    total=False,
)

class SlackConnectorProfileCredentialsTypeDef(
    _RequiredSlackConnectorProfileCredentialsTypeDef,
    _OptionalSlackConnectorProfileCredentialsTypeDef,
):
    pass

_RequiredZendeskConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredZendeskConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
    },
)
_OptionalZendeskConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalZendeskConnectorProfileCredentialsTypeDef",
    {
        "accessToken": str,
        "oAuthRequest": ConnectorOAuthRequestTypeDef,
    },
    total=False,
)

class ZendeskConnectorProfileCredentialsTypeDef(
    _RequiredZendeskConnectorProfileCredentialsTypeDef,
    _OptionalZendeskConnectorProfileCredentialsTypeDef,
):
    pass

_RequiredTaskOutputTypeDef = TypedDict(
    "_RequiredTaskOutputTypeDef",
    {
        "sourceFields": List[str],
        "taskType": TaskTypeType,
    },
)
_OptionalTaskOutputTypeDef = TypedDict(
    "_OptionalTaskOutputTypeDef",
    {
        "connectorOperator": ConnectorOperatorOutputTypeDef,
        "destinationField": str,
        "taskProperties": Dict[OperatorPropertiesKeysType, str],
    },
    total=False,
)

class TaskOutputTypeDef(_RequiredTaskOutputTypeDef, _OptionalTaskOutputTypeDef):
    pass

_RequiredTaskTypeDef = TypedDict(
    "_RequiredTaskTypeDef",
    {
        "sourceFields": Sequence[str],
        "taskType": TaskTypeType,
    },
)
_OptionalTaskTypeDef = TypedDict(
    "_OptionalTaskTypeDef",
    {
        "connectorOperator": ConnectorOperatorTypeDef,
        "destinationField": str,
        "taskProperties": Mapping[OperatorPropertiesKeysType, str],
    },
    total=False,
)

class TaskTypeDef(_RequiredTaskTypeDef, _OptionalTaskTypeDef):
    pass

ConnectorProvisioningConfigOutputTypeDef = TypedDict(
    "ConnectorProvisioningConfigOutputTypeDef",
    {
        "lambda": LambdaConnectorProvisioningConfigOutputTypeDef,
    },
    total=False,
)

ConnectorProvisioningConfigTypeDef = TypedDict(
    "ConnectorProvisioningConfigTypeDef",
    {
        "lambda": LambdaConnectorProvisioningConfigTypeDef,
    },
    total=False,
)

_RequiredCustomConnectorDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredCustomConnectorDestinationPropertiesOutputTypeDef",
    {
        "entityName": str,
    },
)
_OptionalCustomConnectorDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalCustomConnectorDestinationPropertiesOutputTypeDef",
    {
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
        "writeOperationType": WriteOperationTypeType,
        "idFieldNames": List[str],
        "customProperties": Dict[str, str],
    },
    total=False,
)

class CustomConnectorDestinationPropertiesOutputTypeDef(
    _RequiredCustomConnectorDestinationPropertiesOutputTypeDef,
    _OptionalCustomConnectorDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredEventBridgeDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredEventBridgeDestinationPropertiesOutputTypeDef",
    {
        "object": str,
    },
)
_OptionalEventBridgeDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalEventBridgeDestinationPropertiesOutputTypeDef",
    {
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
    },
    total=False,
)

class EventBridgeDestinationPropertiesOutputTypeDef(
    _RequiredEventBridgeDestinationPropertiesOutputTypeDef,
    _OptionalEventBridgeDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredHoneycodeDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredHoneycodeDestinationPropertiesOutputTypeDef",
    {
        "object": str,
    },
)
_OptionalHoneycodeDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalHoneycodeDestinationPropertiesOutputTypeDef",
    {
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
    },
    total=False,
)

class HoneycodeDestinationPropertiesOutputTypeDef(
    _RequiredHoneycodeDestinationPropertiesOutputTypeDef,
    _OptionalHoneycodeDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredMarketoDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredMarketoDestinationPropertiesOutputTypeDef",
    {
        "object": str,
    },
)
_OptionalMarketoDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalMarketoDestinationPropertiesOutputTypeDef",
    {
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
    },
    total=False,
)

class MarketoDestinationPropertiesOutputTypeDef(
    _RequiredMarketoDestinationPropertiesOutputTypeDef,
    _OptionalMarketoDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredRedshiftDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredRedshiftDestinationPropertiesOutputTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
    },
)
_OptionalRedshiftDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalRedshiftDestinationPropertiesOutputTypeDef",
    {
        "bucketPrefix": str,
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
    },
    total=False,
)

class RedshiftDestinationPropertiesOutputTypeDef(
    _RequiredRedshiftDestinationPropertiesOutputTypeDef,
    _OptionalRedshiftDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredSalesforceDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredSalesforceDestinationPropertiesOutputTypeDef",
    {
        "object": str,
    },
)
_OptionalSalesforceDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalSalesforceDestinationPropertiesOutputTypeDef",
    {
        "idFieldNames": List[str],
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
        "writeOperationType": WriteOperationTypeType,
        "dataTransferApi": SalesforceDataTransferApiType,
    },
    total=False,
)

class SalesforceDestinationPropertiesOutputTypeDef(
    _RequiredSalesforceDestinationPropertiesOutputTypeDef,
    _OptionalSalesforceDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredSnowflakeDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredSnowflakeDestinationPropertiesOutputTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
    },
)
_OptionalSnowflakeDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalSnowflakeDestinationPropertiesOutputTypeDef",
    {
        "bucketPrefix": str,
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
    },
    total=False,
)

class SnowflakeDestinationPropertiesOutputTypeDef(
    _RequiredSnowflakeDestinationPropertiesOutputTypeDef,
    _OptionalSnowflakeDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredZendeskDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredZendeskDestinationPropertiesOutputTypeDef",
    {
        "object": str,
    },
)
_OptionalZendeskDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalZendeskDestinationPropertiesOutputTypeDef",
    {
        "idFieldNames": List[str],
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
        "writeOperationType": WriteOperationTypeType,
    },
    total=False,
)

class ZendeskDestinationPropertiesOutputTypeDef(
    _RequiredZendeskDestinationPropertiesOutputTypeDef,
    _OptionalZendeskDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredCustomConnectorDestinationPropertiesTypeDef = TypedDict(
    "_RequiredCustomConnectorDestinationPropertiesTypeDef",
    {
        "entityName": str,
    },
)
_OptionalCustomConnectorDestinationPropertiesTypeDef = TypedDict(
    "_OptionalCustomConnectorDestinationPropertiesTypeDef",
    {
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
        "writeOperationType": WriteOperationTypeType,
        "idFieldNames": Sequence[str],
        "customProperties": Mapping[str, str],
    },
    total=False,
)

class CustomConnectorDestinationPropertiesTypeDef(
    _RequiredCustomConnectorDestinationPropertiesTypeDef,
    _OptionalCustomConnectorDestinationPropertiesTypeDef,
):
    pass

_RequiredEventBridgeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredEventBridgeDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalEventBridgeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalEventBridgeDestinationPropertiesTypeDef",
    {
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
    },
    total=False,
)

class EventBridgeDestinationPropertiesTypeDef(
    _RequiredEventBridgeDestinationPropertiesTypeDef,
    _OptionalEventBridgeDestinationPropertiesTypeDef,
):
    pass

_RequiredHoneycodeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredHoneycodeDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalHoneycodeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalHoneycodeDestinationPropertiesTypeDef",
    {
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
    },
    total=False,
)

class HoneycodeDestinationPropertiesTypeDef(
    _RequiredHoneycodeDestinationPropertiesTypeDef, _OptionalHoneycodeDestinationPropertiesTypeDef
):
    pass

_RequiredMarketoDestinationPropertiesTypeDef = TypedDict(
    "_RequiredMarketoDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalMarketoDestinationPropertiesTypeDef = TypedDict(
    "_OptionalMarketoDestinationPropertiesTypeDef",
    {
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
    },
    total=False,
)

class MarketoDestinationPropertiesTypeDef(
    _RequiredMarketoDestinationPropertiesTypeDef, _OptionalMarketoDestinationPropertiesTypeDef
):
    pass

_RequiredRedshiftDestinationPropertiesTypeDef = TypedDict(
    "_RequiredRedshiftDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
    },
)
_OptionalRedshiftDestinationPropertiesTypeDef = TypedDict(
    "_OptionalRedshiftDestinationPropertiesTypeDef",
    {
        "bucketPrefix": str,
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
    },
    total=False,
)

class RedshiftDestinationPropertiesTypeDef(
    _RequiredRedshiftDestinationPropertiesTypeDef, _OptionalRedshiftDestinationPropertiesTypeDef
):
    pass

_RequiredSalesforceDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSalesforceDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalSalesforceDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSalesforceDestinationPropertiesTypeDef",
    {
        "idFieldNames": Sequence[str],
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
        "writeOperationType": WriteOperationTypeType,
        "dataTransferApi": SalesforceDataTransferApiType,
    },
    total=False,
)

class SalesforceDestinationPropertiesTypeDef(
    _RequiredSalesforceDestinationPropertiesTypeDef, _OptionalSalesforceDestinationPropertiesTypeDef
):
    pass

_RequiredSnowflakeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSnowflakeDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
    },
)
_OptionalSnowflakeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSnowflakeDestinationPropertiesTypeDef",
    {
        "bucketPrefix": str,
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
    },
    total=False,
)

class SnowflakeDestinationPropertiesTypeDef(
    _RequiredSnowflakeDestinationPropertiesTypeDef, _OptionalSnowflakeDestinationPropertiesTypeDef
):
    pass

_RequiredZendeskDestinationPropertiesTypeDef = TypedDict(
    "_RequiredZendeskDestinationPropertiesTypeDef",
    {
        "object": str,
    },
)
_OptionalZendeskDestinationPropertiesTypeDef = TypedDict(
    "_OptionalZendeskDestinationPropertiesTypeDef",
    {
        "idFieldNames": Sequence[str],
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
        "writeOperationType": WriteOperationTypeType,
    },
    total=False,
)

class ZendeskDestinationPropertiesTypeDef(
    _RequiredZendeskDestinationPropertiesTypeDef, _OptionalZendeskDestinationPropertiesTypeDef
):
    pass

CustomConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "CustomConnectorProfilePropertiesOutputTypeDef",
    {
        "profileProperties": Dict[str, str],
        "oAuth2Properties": OAuth2PropertiesOutputTypeDef,
    },
    total=False,
)

CustomConnectorProfilePropertiesTypeDef = TypedDict(
    "CustomConnectorProfilePropertiesTypeDef",
    {
        "profileProperties": Mapping[str, str],
        "oAuth2Properties": OAuth2PropertiesTypeDef,
    },
    total=False,
)

_RequiredCustomConnectorSourcePropertiesTypeDef = TypedDict(
    "_RequiredCustomConnectorSourcePropertiesTypeDef",
    {
        "entityName": str,
    },
)
_OptionalCustomConnectorSourcePropertiesTypeDef = TypedDict(
    "_OptionalCustomConnectorSourcePropertiesTypeDef",
    {
        "customProperties": Mapping[str, str],
        "dataTransferApi": DataTransferApiTypeDef,
    },
    total=False,
)

class CustomConnectorSourcePropertiesTypeDef(
    _RequiredCustomConnectorSourcePropertiesTypeDef, _OptionalCustomConnectorSourcePropertiesTypeDef
):
    pass

FlowDefinitionTypeDef = TypedDict(
    "FlowDefinitionTypeDef",
    {
        "flowArn": str,
        "description": str,
        "flowName": str,
        "flowStatus": FlowStatusType,
        "sourceConnectorType": ConnectorTypeType,
        "sourceConnectorLabel": str,
        "destinationConnectorType": ConnectorTypeType,
        "destinationConnectorLabel": str,
        "triggerType": TriggerTypeType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
        "lastRunExecutionDetails": ExecutionDetailsTypeDef,
    },
    total=False,
)

ExecutionResultTypeDef = TypedDict(
    "ExecutionResultTypeDef",
    {
        "errorInfo": ErrorInfoTypeDef,
        "bytesProcessed": int,
        "bytesWritten": int,
        "recordsProcessed": int,
    },
    total=False,
)

_RequiredFieldTypeDetailsTypeDef = TypedDict(
    "_RequiredFieldTypeDetailsTypeDef",
    {
        "fieldType": str,
        "filterOperators": List[OperatorType],
    },
)
_OptionalFieldTypeDetailsTypeDef = TypedDict(
    "_OptionalFieldTypeDetailsTypeDef",
    {
        "supportedValues": List[str],
        "valueRegexPattern": str,
        "supportedDateFormat": str,
        "fieldValueRange": RangeTypeDef,
        "fieldLengthRange": RangeTypeDef,
    },
    total=False,
)

class FieldTypeDetailsTypeDef(_RequiredFieldTypeDetailsTypeDef, _OptionalFieldTypeDetailsTypeDef):
    pass

MetadataCatalogConfigOutputTypeDef = TypedDict(
    "MetadataCatalogConfigOutputTypeDef",
    {
        "glueDataCatalog": GlueDataCatalogConfigOutputTypeDef,
    },
    total=False,
)

MetadataCatalogConfigTypeDef = TypedDict(
    "MetadataCatalogConfigTypeDef",
    {
        "glueDataCatalog": GlueDataCatalogConfigTypeDef,
    },
    total=False,
)

MetadataCatalogDetailTypeDef = TypedDict(
    "MetadataCatalogDetailTypeDef",
    {
        "catalogType": Literal["GLUE"],
        "tableName": str,
        "tableRegistrationOutput": RegistrationOutputTypeDef,
        "partitionRegistrationOutput": RegistrationOutputTypeDef,
    },
    total=False,
)

OAuth2DefaultsTypeDef = TypedDict(
    "OAuth2DefaultsTypeDef",
    {
        "oauthScopes": List[str],
        "tokenUrls": List[str],
        "authCodeUrls": List[str],
        "oauth2GrantTypesSupported": List[OAuth2GrantTypeType],
        "oauth2CustomProperties": List[OAuth2CustomParameterTypeDef],
    },
    total=False,
)

_RequiredSAPODataConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "_RequiredSAPODataConnectorProfilePropertiesOutputTypeDef",
    {
        "applicationHostUrl": str,
        "applicationServicePath": str,
        "portNumber": int,
        "clientNumber": str,
    },
)
_OptionalSAPODataConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "_OptionalSAPODataConnectorProfilePropertiesOutputTypeDef",
    {
        "logonLanguage": str,
        "privateLinkServiceName": str,
        "oAuthProperties": OAuthPropertiesOutputTypeDef,
        "disableSSO": bool,
    },
    total=False,
)

class SAPODataConnectorProfilePropertiesOutputTypeDef(
    _RequiredSAPODataConnectorProfilePropertiesOutputTypeDef,
    _OptionalSAPODataConnectorProfilePropertiesOutputTypeDef,
):
    pass

_RequiredSAPODataConnectorProfilePropertiesTypeDef = TypedDict(
    "_RequiredSAPODataConnectorProfilePropertiesTypeDef",
    {
        "applicationHostUrl": str,
        "applicationServicePath": str,
        "portNumber": int,
        "clientNumber": str,
    },
)
_OptionalSAPODataConnectorProfilePropertiesTypeDef = TypedDict(
    "_OptionalSAPODataConnectorProfilePropertiesTypeDef",
    {
        "logonLanguage": str,
        "privateLinkServiceName": str,
        "oAuthProperties": OAuthPropertiesTypeDef,
        "disableSSO": bool,
    },
    total=False,
)

class SAPODataConnectorProfilePropertiesTypeDef(
    _RequiredSAPODataConnectorProfilePropertiesTypeDef,
    _OptionalSAPODataConnectorProfilePropertiesTypeDef,
):
    pass

S3OutputFormatConfigOutputTypeDef = TypedDict(
    "S3OutputFormatConfigOutputTypeDef",
    {
        "fileType": FileTypeType,
        "prefixConfig": PrefixConfigOutputTypeDef,
        "aggregationConfig": AggregationConfigOutputTypeDef,
        "preserveSourceDataTyping": bool,
    },
    total=False,
)

_RequiredUpsolverS3OutputFormatConfigOutputTypeDef = TypedDict(
    "_RequiredUpsolverS3OutputFormatConfigOutputTypeDef",
    {
        "prefixConfig": PrefixConfigOutputTypeDef,
    },
)
_OptionalUpsolverS3OutputFormatConfigOutputTypeDef = TypedDict(
    "_OptionalUpsolverS3OutputFormatConfigOutputTypeDef",
    {
        "fileType": FileTypeType,
        "aggregationConfig": AggregationConfigOutputTypeDef,
    },
    total=False,
)

class UpsolverS3OutputFormatConfigOutputTypeDef(
    _RequiredUpsolverS3OutputFormatConfigOutputTypeDef,
    _OptionalUpsolverS3OutputFormatConfigOutputTypeDef,
):
    pass

S3OutputFormatConfigTypeDef = TypedDict(
    "S3OutputFormatConfigTypeDef",
    {
        "fileType": FileTypeType,
        "prefixConfig": PrefixConfigTypeDef,
        "aggregationConfig": AggregationConfigTypeDef,
        "preserveSourceDataTyping": bool,
    },
    total=False,
)

_RequiredUpsolverS3OutputFormatConfigTypeDef = TypedDict(
    "_RequiredUpsolverS3OutputFormatConfigTypeDef",
    {
        "prefixConfig": PrefixConfigTypeDef,
    },
)
_OptionalUpsolverS3OutputFormatConfigTypeDef = TypedDict(
    "_OptionalUpsolverS3OutputFormatConfigTypeDef",
    {
        "fileType": FileTypeType,
        "aggregationConfig": AggregationConfigTypeDef,
    },
    total=False,
)

class UpsolverS3OutputFormatConfigTypeDef(
    _RequiredUpsolverS3OutputFormatConfigTypeDef, _OptionalUpsolverS3OutputFormatConfigTypeDef
):
    pass

_RequiredS3SourcePropertiesOutputTypeDef = TypedDict(
    "_RequiredS3SourcePropertiesOutputTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3SourcePropertiesOutputTypeDef = TypedDict(
    "_OptionalS3SourcePropertiesOutputTypeDef",
    {
        "bucketPrefix": str,
        "s3InputFormatConfig": S3InputFormatConfigOutputTypeDef,
    },
    total=False,
)

class S3SourcePropertiesOutputTypeDef(
    _RequiredS3SourcePropertiesOutputTypeDef, _OptionalS3SourcePropertiesOutputTypeDef
):
    pass

_RequiredS3SourcePropertiesTypeDef = TypedDict(
    "_RequiredS3SourcePropertiesTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3SourcePropertiesTypeDef = TypedDict(
    "_OptionalS3SourcePropertiesTypeDef",
    {
        "bucketPrefix": str,
        "s3InputFormatConfig": S3InputFormatConfigTypeDef,
    },
    total=False,
)

class S3SourcePropertiesTypeDef(
    _RequiredS3SourcePropertiesTypeDef, _OptionalS3SourcePropertiesTypeDef
):
    pass

_RequiredSAPODataDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredSAPODataDestinationPropertiesOutputTypeDef",
    {
        "objectPath": str,
    },
)
_OptionalSAPODataDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalSAPODataDestinationPropertiesOutputTypeDef",
    {
        "successResponseHandlingConfig": SuccessResponseHandlingConfigOutputTypeDef,
        "idFieldNames": List[str],
        "errorHandlingConfig": ErrorHandlingConfigOutputTypeDef,
        "writeOperationType": WriteOperationTypeType,
    },
    total=False,
)

class SAPODataDestinationPropertiesOutputTypeDef(
    _RequiredSAPODataDestinationPropertiesOutputTypeDef,
    _OptionalSAPODataDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredSAPODataDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSAPODataDestinationPropertiesTypeDef",
    {
        "objectPath": str,
    },
)
_OptionalSAPODataDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSAPODataDestinationPropertiesTypeDef",
    {
        "successResponseHandlingConfig": SuccessResponseHandlingConfigTypeDef,
        "idFieldNames": Sequence[str],
        "errorHandlingConfig": ErrorHandlingConfigTypeDef,
        "writeOperationType": WriteOperationTypeType,
    },
    total=False,
)

class SAPODataDestinationPropertiesTypeDef(
    _RequiredSAPODataDestinationPropertiesTypeDef, _OptionalSAPODataDestinationPropertiesTypeDef
):
    pass

TriggerPropertiesOutputTypeDef = TypedDict(
    "TriggerPropertiesOutputTypeDef",
    {
        "Scheduled": ScheduledTriggerPropertiesOutputTypeDef,
    },
    total=False,
)

TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": ScheduledTriggerPropertiesTypeDef,
    },
    total=False,
)

_RequiredCustomConnectorProfileCredentialsTypeDef = TypedDict(
    "_RequiredCustomConnectorProfileCredentialsTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
    },
)
_OptionalCustomConnectorProfileCredentialsTypeDef = TypedDict(
    "_OptionalCustomConnectorProfileCredentialsTypeDef",
    {
        "basic": BasicAuthCredentialsTypeDef,
        "oauth2": OAuth2CredentialsTypeDef,
        "apiKey": ApiKeyCredentialsTypeDef,
        "custom": CustomAuthCredentialsTypeDef,
    },
    total=False,
)

class CustomConnectorProfileCredentialsTypeDef(
    _RequiredCustomConnectorProfileCredentialsTypeDef,
    _OptionalCustomConnectorProfileCredentialsTypeDef,
):
    pass

SAPODataConnectorProfileCredentialsTypeDef = TypedDict(
    "SAPODataConnectorProfileCredentialsTypeDef",
    {
        "basicAuthCredentials": BasicAuthCredentialsTypeDef,
        "oAuthCredentials": OAuthCredentialsTypeDef,
    },
    total=False,
)

RegisterConnectorRequestRequestTypeDef = TypedDict(
    "RegisterConnectorRequestRequestTypeDef",
    {
        "connectorLabel": str,
        "description": str,
        "connectorProvisioningType": Literal["LAMBDA"],
        "connectorProvisioningConfig": ConnectorProvisioningConfigTypeDef,
        "clientToken": str,
    },
    total=False,
)

_RequiredUpdateConnectorRegistrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectorRegistrationRequestRequestTypeDef",
    {
        "connectorLabel": str,
    },
)
_OptionalUpdateConnectorRegistrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectorRegistrationRequestRequestTypeDef",
    {
        "description": str,
        "connectorProvisioningConfig": ConnectorProvisioningConfigTypeDef,
        "clientToken": str,
    },
    total=False,
)

class UpdateConnectorRegistrationRequestRequestTypeDef(
    _RequiredUpdateConnectorRegistrationRequestRequestTypeDef,
    _OptionalUpdateConnectorRegistrationRequestRequestTypeDef,
):
    pass

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "flows": List[FlowDefinitionTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SupportedFieldTypeDetailsTypeDef = TypedDict(
    "SupportedFieldTypeDetailsTypeDef",
    {
        "v1": FieldTypeDetailsTypeDef,
    },
)

ExecutionRecordTypeDef = TypedDict(
    "ExecutionRecordTypeDef",
    {
        "executionId": str,
        "executionStatus": ExecutionStatusType,
        "executionResult": ExecutionResultTypeDef,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "dataPullStartTime": datetime,
        "dataPullEndTime": datetime,
        "metadataCatalogDetails": List[MetadataCatalogDetailTypeDef],
    },
    total=False,
)

AuthenticationConfigTypeDef = TypedDict(
    "AuthenticationConfigTypeDef",
    {
        "isBasicAuthSupported": bool,
        "isApiKeyAuthSupported": bool,
        "isOAuth2Supported": bool,
        "isCustomAuthSupported": bool,
        "oAuth2Defaults": OAuth2DefaultsTypeDef,
        "customAuthConfigs": List[CustomAuthConfigTypeDef],
    },
    total=False,
)

ConnectorProfilePropertiesOutputTypeDef = TypedDict(
    "ConnectorProfilePropertiesOutputTypeDef",
    {
        "Amplitude": Dict[str, Any],
        "Datadog": DatadogConnectorProfilePropertiesOutputTypeDef,
        "Dynatrace": DynatraceConnectorProfilePropertiesOutputTypeDef,
        "GoogleAnalytics": Dict[str, Any],
        "Honeycode": Dict[str, Any],
        "InforNexus": InforNexusConnectorProfilePropertiesOutputTypeDef,
        "Marketo": MarketoConnectorProfilePropertiesOutputTypeDef,
        "Redshift": RedshiftConnectorProfilePropertiesOutputTypeDef,
        "Salesforce": SalesforceConnectorProfilePropertiesOutputTypeDef,
        "ServiceNow": ServiceNowConnectorProfilePropertiesOutputTypeDef,
        "Singular": Dict[str, Any],
        "Slack": SlackConnectorProfilePropertiesOutputTypeDef,
        "Snowflake": SnowflakeConnectorProfilePropertiesOutputTypeDef,
        "Trendmicro": Dict[str, Any],
        "Veeva": VeevaConnectorProfilePropertiesOutputTypeDef,
        "Zendesk": ZendeskConnectorProfilePropertiesOutputTypeDef,
        "SAPOData": SAPODataConnectorProfilePropertiesOutputTypeDef,
        "CustomConnector": CustomConnectorProfilePropertiesOutputTypeDef,
        "Pardot": PardotConnectorProfilePropertiesOutputTypeDef,
    },
    total=False,
)

ConnectorProfilePropertiesTypeDef = TypedDict(
    "ConnectorProfilePropertiesTypeDef",
    {
        "Amplitude": Mapping[str, Any],
        "Datadog": DatadogConnectorProfilePropertiesTypeDef,
        "Dynatrace": DynatraceConnectorProfilePropertiesTypeDef,
        "GoogleAnalytics": Mapping[str, Any],
        "Honeycode": Mapping[str, Any],
        "InforNexus": InforNexusConnectorProfilePropertiesTypeDef,
        "Marketo": MarketoConnectorProfilePropertiesTypeDef,
        "Redshift": RedshiftConnectorProfilePropertiesTypeDef,
        "Salesforce": SalesforceConnectorProfilePropertiesTypeDef,
        "ServiceNow": ServiceNowConnectorProfilePropertiesTypeDef,
        "Singular": Mapping[str, Any],
        "Slack": SlackConnectorProfilePropertiesTypeDef,
        "Snowflake": SnowflakeConnectorProfilePropertiesTypeDef,
        "Trendmicro": Mapping[str, Any],
        "Veeva": VeevaConnectorProfilePropertiesTypeDef,
        "Zendesk": ZendeskConnectorProfilePropertiesTypeDef,
        "SAPOData": SAPODataConnectorProfilePropertiesTypeDef,
        "CustomConnector": CustomConnectorProfilePropertiesTypeDef,
        "Pardot": PardotConnectorProfilePropertiesTypeDef,
    },
    total=False,
)

_RequiredS3DestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredS3DestinationPropertiesOutputTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3DestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalS3DestinationPropertiesOutputTypeDef",
    {
        "bucketPrefix": str,
        "s3OutputFormatConfig": S3OutputFormatConfigOutputTypeDef,
    },
    total=False,
)

class S3DestinationPropertiesOutputTypeDef(
    _RequiredS3DestinationPropertiesOutputTypeDef, _OptionalS3DestinationPropertiesOutputTypeDef
):
    pass

_RequiredUpsolverDestinationPropertiesOutputTypeDef = TypedDict(
    "_RequiredUpsolverDestinationPropertiesOutputTypeDef",
    {
        "bucketName": str,
        "s3OutputFormatConfig": UpsolverS3OutputFormatConfigOutputTypeDef,
    },
)
_OptionalUpsolverDestinationPropertiesOutputTypeDef = TypedDict(
    "_OptionalUpsolverDestinationPropertiesOutputTypeDef",
    {
        "bucketPrefix": str,
    },
    total=False,
)

class UpsolverDestinationPropertiesOutputTypeDef(
    _RequiredUpsolverDestinationPropertiesOutputTypeDef,
    _OptionalUpsolverDestinationPropertiesOutputTypeDef,
):
    pass

_RequiredS3DestinationPropertiesTypeDef = TypedDict(
    "_RequiredS3DestinationPropertiesTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3DestinationPropertiesTypeDef = TypedDict(
    "_OptionalS3DestinationPropertiesTypeDef",
    {
        "bucketPrefix": str,
        "s3OutputFormatConfig": S3OutputFormatConfigTypeDef,
    },
    total=False,
)

class S3DestinationPropertiesTypeDef(
    _RequiredS3DestinationPropertiesTypeDef, _OptionalS3DestinationPropertiesTypeDef
):
    pass

_RequiredUpsolverDestinationPropertiesTypeDef = TypedDict(
    "_RequiredUpsolverDestinationPropertiesTypeDef",
    {
        "bucketName": str,
        "s3OutputFormatConfig": UpsolverS3OutputFormatConfigTypeDef,
    },
)
_OptionalUpsolverDestinationPropertiesTypeDef = TypedDict(
    "_OptionalUpsolverDestinationPropertiesTypeDef",
    {
        "bucketPrefix": str,
    },
    total=False,
)

class UpsolverDestinationPropertiesTypeDef(
    _RequiredUpsolverDestinationPropertiesTypeDef, _OptionalUpsolverDestinationPropertiesTypeDef
):
    pass

SourceConnectorPropertiesOutputTypeDef = TypedDict(
    "SourceConnectorPropertiesOutputTypeDef",
    {
        "Amplitude": AmplitudeSourcePropertiesOutputTypeDef,
        "Datadog": DatadogSourcePropertiesOutputTypeDef,
        "Dynatrace": DynatraceSourcePropertiesOutputTypeDef,
        "GoogleAnalytics": GoogleAnalyticsSourcePropertiesOutputTypeDef,
        "InforNexus": InforNexusSourcePropertiesOutputTypeDef,
        "Marketo": MarketoSourcePropertiesOutputTypeDef,
        "S3": S3SourcePropertiesOutputTypeDef,
        "Salesforce": SalesforceSourcePropertiesOutputTypeDef,
        "ServiceNow": ServiceNowSourcePropertiesOutputTypeDef,
        "Singular": SingularSourcePropertiesOutputTypeDef,
        "Slack": SlackSourcePropertiesOutputTypeDef,
        "Trendmicro": TrendmicroSourcePropertiesOutputTypeDef,
        "Veeva": VeevaSourcePropertiesOutputTypeDef,
        "Zendesk": ZendeskSourcePropertiesOutputTypeDef,
        "SAPOData": SAPODataSourcePropertiesOutputTypeDef,
        "CustomConnector": CustomConnectorSourcePropertiesOutputTypeDef,
        "Pardot": PardotSourcePropertiesOutputTypeDef,
    },
    total=False,
)

SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Amplitude": AmplitudeSourcePropertiesTypeDef,
        "Datadog": DatadogSourcePropertiesTypeDef,
        "Dynatrace": DynatraceSourcePropertiesTypeDef,
        "GoogleAnalytics": GoogleAnalyticsSourcePropertiesTypeDef,
        "InforNexus": InforNexusSourcePropertiesTypeDef,
        "Marketo": MarketoSourcePropertiesTypeDef,
        "S3": S3SourcePropertiesTypeDef,
        "Salesforce": SalesforceSourcePropertiesTypeDef,
        "ServiceNow": ServiceNowSourcePropertiesTypeDef,
        "Singular": SingularSourcePropertiesTypeDef,
        "Slack": SlackSourcePropertiesTypeDef,
        "Trendmicro": TrendmicroSourcePropertiesTypeDef,
        "Veeva": VeevaSourcePropertiesTypeDef,
        "Zendesk": ZendeskSourcePropertiesTypeDef,
        "SAPOData": SAPODataSourcePropertiesTypeDef,
        "CustomConnector": CustomConnectorSourcePropertiesTypeDef,
        "Pardot": PardotSourcePropertiesTypeDef,
    },
    total=False,
)

_RequiredTriggerConfigOutputTypeDef = TypedDict(
    "_RequiredTriggerConfigOutputTypeDef",
    {
        "triggerType": TriggerTypeType,
    },
)
_OptionalTriggerConfigOutputTypeDef = TypedDict(
    "_OptionalTriggerConfigOutputTypeDef",
    {
        "triggerProperties": TriggerPropertiesOutputTypeDef,
    },
    total=False,
)

class TriggerConfigOutputTypeDef(
    _RequiredTriggerConfigOutputTypeDef, _OptionalTriggerConfigOutputTypeDef
):
    pass

_RequiredTriggerConfigTypeDef = TypedDict(
    "_RequiredTriggerConfigTypeDef",
    {
        "triggerType": TriggerTypeType,
    },
)
_OptionalTriggerConfigTypeDef = TypedDict(
    "_OptionalTriggerConfigTypeDef",
    {
        "triggerProperties": TriggerPropertiesTypeDef,
    },
    total=False,
)

class TriggerConfigTypeDef(_RequiredTriggerConfigTypeDef, _OptionalTriggerConfigTypeDef):
    pass

ConnectorProfileCredentialsTypeDef = TypedDict(
    "ConnectorProfileCredentialsTypeDef",
    {
        "Amplitude": AmplitudeConnectorProfileCredentialsTypeDef,
        "Datadog": DatadogConnectorProfileCredentialsTypeDef,
        "Dynatrace": DynatraceConnectorProfileCredentialsTypeDef,
        "GoogleAnalytics": GoogleAnalyticsConnectorProfileCredentialsTypeDef,
        "Honeycode": HoneycodeConnectorProfileCredentialsTypeDef,
        "InforNexus": InforNexusConnectorProfileCredentialsTypeDef,
        "Marketo": MarketoConnectorProfileCredentialsTypeDef,
        "Redshift": RedshiftConnectorProfileCredentialsTypeDef,
        "Salesforce": SalesforceConnectorProfileCredentialsTypeDef,
        "ServiceNow": ServiceNowConnectorProfileCredentialsTypeDef,
        "Singular": SingularConnectorProfileCredentialsTypeDef,
        "Slack": SlackConnectorProfileCredentialsTypeDef,
        "Snowflake": SnowflakeConnectorProfileCredentialsTypeDef,
        "Trendmicro": TrendmicroConnectorProfileCredentialsTypeDef,
        "Veeva": VeevaConnectorProfileCredentialsTypeDef,
        "Zendesk": ZendeskConnectorProfileCredentialsTypeDef,
        "SAPOData": SAPODataConnectorProfileCredentialsTypeDef,
        "CustomConnector": CustomConnectorProfileCredentialsTypeDef,
        "Pardot": PardotConnectorProfileCredentialsTypeDef,
    },
    total=False,
)

_RequiredConnectorEntityFieldTypeDef = TypedDict(
    "_RequiredConnectorEntityFieldTypeDef",
    {
        "identifier": str,
    },
)
_OptionalConnectorEntityFieldTypeDef = TypedDict(
    "_OptionalConnectorEntityFieldTypeDef",
    {
        "parentIdentifier": str,
        "label": str,
        "isPrimaryKey": bool,
        "defaultValue": str,
        "isDeprecated": bool,
        "supportedFieldTypeDetails": SupportedFieldTypeDetailsTypeDef,
        "description": str,
        "sourceProperties": SourceFieldPropertiesTypeDef,
        "destinationProperties": DestinationFieldPropertiesTypeDef,
        "customProperties": Dict[str, str],
    },
    total=False,
)

class ConnectorEntityFieldTypeDef(
    _RequiredConnectorEntityFieldTypeDef, _OptionalConnectorEntityFieldTypeDef
):
    pass

DescribeFlowExecutionRecordsResponseTypeDef = TypedDict(
    "DescribeFlowExecutionRecordsResponseTypeDef",
    {
        "flowExecutions": List[ExecutionRecordTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectorConfigurationTypeDef = TypedDict(
    "ConnectorConfigurationTypeDef",
    {
        "canUseAsSource": bool,
        "canUseAsDestination": bool,
        "supportedDestinationConnectors": List[ConnectorTypeType],
        "supportedSchedulingFrequencies": List[ScheduleFrequencyTypeType],
        "isPrivateLinkEnabled": bool,
        "isPrivateLinkEndpointUrlRequired": bool,
        "supportedTriggerTypes": List[TriggerTypeType],
        "connectorMetadata": ConnectorMetadataTypeDef,
        "connectorType": ConnectorTypeType,
        "connectorLabel": str,
        "connectorDescription": str,
        "connectorOwner": str,
        "connectorName": str,
        "connectorVersion": str,
        "connectorArn": str,
        "connectorModes": List[str],
        "authenticationConfig": AuthenticationConfigTypeDef,
        "connectorRuntimeSettings": List[ConnectorRuntimeSettingTypeDef],
        "supportedApiVersions": List[str],
        "supportedOperators": List[OperatorsType],
        "supportedWriteOperations": List[WriteOperationTypeType],
        "connectorProvisioningType": Literal["LAMBDA"],
        "connectorProvisioningConfig": ConnectorProvisioningConfigOutputTypeDef,
        "logoURL": str,
        "registeredAt": datetime,
        "registeredBy": str,
        "supportedDataTransferTypes": List[SupportedDataTransferTypeType],
        "supportedDataTransferApis": List[DataTransferApiOutputTypeDef],
    },
    total=False,
)

ConnectorProfileTypeDef = TypedDict(
    "ConnectorProfileTypeDef",
    {
        "connectorProfileArn": str,
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "connectorLabel": str,
        "connectionMode": ConnectionModeType,
        "credentialsArn": str,
        "connectorProfileProperties": ConnectorProfilePropertiesOutputTypeDef,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "privateConnectionProvisioningState": PrivateConnectionProvisioningStateTypeDef,
    },
    total=False,
)

DestinationConnectorPropertiesOutputTypeDef = TypedDict(
    "DestinationConnectorPropertiesOutputTypeDef",
    {
        "Redshift": RedshiftDestinationPropertiesOutputTypeDef,
        "S3": S3DestinationPropertiesOutputTypeDef,
        "Salesforce": SalesforceDestinationPropertiesOutputTypeDef,
        "Snowflake": SnowflakeDestinationPropertiesOutputTypeDef,
        "EventBridge": EventBridgeDestinationPropertiesOutputTypeDef,
        "LookoutMetrics": Dict[str, Any],
        "Upsolver": UpsolverDestinationPropertiesOutputTypeDef,
        "Honeycode": HoneycodeDestinationPropertiesOutputTypeDef,
        "CustomerProfiles": CustomerProfilesDestinationPropertiesOutputTypeDef,
        "Zendesk": ZendeskDestinationPropertiesOutputTypeDef,
        "Marketo": MarketoDestinationPropertiesOutputTypeDef,
        "CustomConnector": CustomConnectorDestinationPropertiesOutputTypeDef,
        "SAPOData": SAPODataDestinationPropertiesOutputTypeDef,
    },
    total=False,
)

DestinationConnectorPropertiesTypeDef = TypedDict(
    "DestinationConnectorPropertiesTypeDef",
    {
        "Redshift": RedshiftDestinationPropertiesTypeDef,
        "S3": S3DestinationPropertiesTypeDef,
        "Salesforce": SalesforceDestinationPropertiesTypeDef,
        "Snowflake": SnowflakeDestinationPropertiesTypeDef,
        "EventBridge": EventBridgeDestinationPropertiesTypeDef,
        "LookoutMetrics": Mapping[str, Any],
        "Upsolver": UpsolverDestinationPropertiesTypeDef,
        "Honeycode": HoneycodeDestinationPropertiesTypeDef,
        "CustomerProfiles": CustomerProfilesDestinationPropertiesTypeDef,
        "Zendesk": ZendeskDestinationPropertiesTypeDef,
        "Marketo": MarketoDestinationPropertiesTypeDef,
        "CustomConnector": CustomConnectorDestinationPropertiesTypeDef,
        "SAPOData": SAPODataDestinationPropertiesTypeDef,
    },
    total=False,
)

_RequiredSourceFlowConfigOutputTypeDef = TypedDict(
    "_RequiredSourceFlowConfigOutputTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "sourceConnectorProperties": SourceConnectorPropertiesOutputTypeDef,
    },
)
_OptionalSourceFlowConfigOutputTypeDef = TypedDict(
    "_OptionalSourceFlowConfigOutputTypeDef",
    {
        "apiVersion": str,
        "connectorProfileName": str,
        "incrementalPullConfig": IncrementalPullConfigOutputTypeDef,
    },
    total=False,
)

class SourceFlowConfigOutputTypeDef(
    _RequiredSourceFlowConfigOutputTypeDef, _OptionalSourceFlowConfigOutputTypeDef
):
    pass

_RequiredSourceFlowConfigTypeDef = TypedDict(
    "_RequiredSourceFlowConfigTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "sourceConnectorProperties": SourceConnectorPropertiesTypeDef,
    },
)
_OptionalSourceFlowConfigTypeDef = TypedDict(
    "_OptionalSourceFlowConfigTypeDef",
    {
        "apiVersion": str,
        "connectorProfileName": str,
        "incrementalPullConfig": IncrementalPullConfigTypeDef,
    },
    total=False,
)

class SourceFlowConfigTypeDef(_RequiredSourceFlowConfigTypeDef, _OptionalSourceFlowConfigTypeDef):
    pass

_RequiredConnectorProfileConfigTypeDef = TypedDict(
    "_RequiredConnectorProfileConfigTypeDef",
    {
        "connectorProfileProperties": ConnectorProfilePropertiesTypeDef,
    },
)
_OptionalConnectorProfileConfigTypeDef = TypedDict(
    "_OptionalConnectorProfileConfigTypeDef",
    {
        "connectorProfileCredentials": ConnectorProfileCredentialsTypeDef,
    },
    total=False,
)

class ConnectorProfileConfigTypeDef(
    _RequiredConnectorProfileConfigTypeDef, _OptionalConnectorProfileConfigTypeDef
):
    pass

DescribeConnectorEntityResponseTypeDef = TypedDict(
    "DescribeConnectorEntityResponseTypeDef",
    {
        "connectorEntityFields": List[ConnectorEntityFieldTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "connectorConfiguration": ConnectorConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorsResponseTypeDef = TypedDict(
    "DescribeConnectorsResponseTypeDef",
    {
        "connectorConfigurations": Dict[ConnectorTypeType, ConnectorConfigurationTypeDef],
        "connectors": List[ConnectorDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorProfilesResponseTypeDef = TypedDict(
    "DescribeConnectorProfilesResponseTypeDef",
    {
        "connectorProfileDetails": List[ConnectorProfileTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDestinationFlowConfigOutputTypeDef = TypedDict(
    "_RequiredDestinationFlowConfigOutputTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "destinationConnectorProperties": DestinationConnectorPropertiesOutputTypeDef,
    },
)
_OptionalDestinationFlowConfigOutputTypeDef = TypedDict(
    "_OptionalDestinationFlowConfigOutputTypeDef",
    {
        "apiVersion": str,
        "connectorProfileName": str,
    },
    total=False,
)

class DestinationFlowConfigOutputTypeDef(
    _RequiredDestinationFlowConfigOutputTypeDef, _OptionalDestinationFlowConfigOutputTypeDef
):
    pass

_RequiredDestinationFlowConfigTypeDef = TypedDict(
    "_RequiredDestinationFlowConfigTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "destinationConnectorProperties": DestinationConnectorPropertiesTypeDef,
    },
)
_OptionalDestinationFlowConfigTypeDef = TypedDict(
    "_OptionalDestinationFlowConfigTypeDef",
    {
        "apiVersion": str,
        "connectorProfileName": str,
    },
    total=False,
)

class DestinationFlowConfigTypeDef(
    _RequiredDestinationFlowConfigTypeDef, _OptionalDestinationFlowConfigTypeDef
):
    pass

_RequiredCreateConnectorProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "connectionMode": ConnectionModeType,
        "connectorProfileConfig": ConnectorProfileConfigTypeDef,
    },
)
_OptionalCreateConnectorProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectorProfileRequestRequestTypeDef",
    {
        "kmsArn": str,
        "connectorLabel": str,
        "clientToken": str,
    },
    total=False,
)

class CreateConnectorProfileRequestRequestTypeDef(
    _RequiredCreateConnectorProfileRequestRequestTypeDef,
    _OptionalCreateConnectorProfileRequestRequestTypeDef,
):
    pass

_RequiredUpdateConnectorProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectionMode": ConnectionModeType,
        "connectorProfileConfig": ConnectorProfileConfigTypeDef,
    },
)
_OptionalUpdateConnectorProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectorProfileRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateConnectorProfileRequestRequestTypeDef(
    _RequiredUpdateConnectorProfileRequestRequestTypeDef,
    _OptionalUpdateConnectorProfileRequestRequestTypeDef,
):
    pass

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "flowArn": str,
        "description": str,
        "flowName": str,
        "kmsArn": str,
        "flowStatus": FlowStatusType,
        "flowStatusMessage": str,
        "sourceFlowConfig": SourceFlowConfigOutputTypeDef,
        "destinationFlowConfigList": List[DestinationFlowConfigOutputTypeDef],
        "lastRunExecutionDetails": ExecutionDetailsTypeDef,
        "triggerConfig": TriggerConfigOutputTypeDef,
        "tasks": List[TaskOutputTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
        "metadataCatalogConfig": MetadataCatalogConfigOutputTypeDef,
        "lastRunMetadataCatalogDetails": List[MetadataCatalogDetailTypeDef],
        "schemaVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": TriggerConfigTypeDef,
        "sourceFlowConfig": SourceFlowConfigTypeDef,
        "destinationFlowConfigList": Sequence[DestinationFlowConfigTypeDef],
        "tasks": Sequence[TaskTypeDef],
    },
)
_OptionalCreateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFlowRequestRequestTypeDef",
    {
        "description": str,
        "kmsArn": str,
        "tags": Mapping[str, str],
        "metadataCatalogConfig": MetadataCatalogConfigTypeDef,
        "clientToken": str,
    },
    total=False,
)

class CreateFlowRequestRequestTypeDef(
    _RequiredCreateFlowRequestRequestTypeDef, _OptionalCreateFlowRequestRequestTypeDef
):
    pass

_RequiredUpdateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": TriggerConfigTypeDef,
        "sourceFlowConfig": SourceFlowConfigTypeDef,
        "destinationFlowConfigList": Sequence[DestinationFlowConfigTypeDef],
        "tasks": Sequence[TaskTypeDef],
    },
)
_OptionalUpdateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowRequestRequestTypeDef",
    {
        "description": str,
        "metadataCatalogConfig": MetadataCatalogConfigTypeDef,
        "clientToken": str,
    },
    total=False,
)

class UpdateFlowRequestRequestTypeDef(
    _RequiredUpdateFlowRequestRequestTypeDef, _OptionalUpdateFlowRequestRequestTypeDef
):
    pass
