"""
Type annotations for apprunner service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/type_defs/)

Usage::

    ```python
    from mypy_boto3_apprunner.type_defs import AssociateCustomDomainRequestRequestTypeDef

    data: AssociateCustomDomainRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AutoScalingConfigurationStatusType,
    CertificateValidationRecordStatusType,
    ConfigurationSourceType,
    ConnectionStatusType,
    CustomDomainAssociationStatusType,
    EgressTypeType,
    HealthCheckProtocolType,
    ImageRepositoryTypeType,
    ObservabilityConfigurationStatusType,
    OperationStatusType,
    OperationTypeType,
    RuntimeType,
    ServiceStatusType,
    VpcConnectorStatusType,
    VpcIngressConnectionStatusType,
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
    "AssociateCustomDomainRequestRequestTypeDef",
    "VpcDNSTargetTypeDef",
    "AuthenticationConfigurationOutputTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AutoScalingConfigurationSummaryTypeDef",
    "AutoScalingConfigurationTypeDef",
    "CertificateValidationRecordTypeDef",
    "CodeConfigurationValuesOutputTypeDef",
    "CodeConfigurationValuesTypeDef",
    "SourceCodeVersionOutputTypeDef",
    "SourceCodeVersionTypeDef",
    "ConnectionSummaryTypeDef",
    "ConnectionTypeDef",
    "TagTypeDef",
    "TraceConfigurationTypeDef",
    "EncryptionConfigurationTypeDef",
    "HealthCheckConfigurationTypeDef",
    "InstanceConfigurationTypeDef",
    "ServiceObservabilityConfigurationTypeDef",
    "VpcConnectorTypeDef",
    "IngressVpcConfigurationTypeDef",
    "DeleteAutoScalingConfigurationRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteObservabilityConfigurationRequestRequestTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteVpcConnectorRequestRequestTypeDef",
    "DeleteVpcIngressConnectionRequestRequestTypeDef",
    "DescribeAutoScalingConfigurationRequestRequestTypeDef",
    "DescribeCustomDomainsRequestRequestTypeDef",
    "DescribeObservabilityConfigurationRequestRequestTypeDef",
    "DescribeServiceRequestRequestTypeDef",
    "DescribeVpcConnectorRequestRequestTypeDef",
    "DescribeVpcIngressConnectionRequestRequestTypeDef",
    "DisassociateCustomDomainRequestRequestTypeDef",
    "EgressConfigurationOutputTypeDef",
    "EgressConfigurationTypeDef",
    "EncryptionConfigurationOutputTypeDef",
    "HealthCheckConfigurationOutputTypeDef",
    "ImageConfigurationOutputTypeDef",
    "ImageConfigurationTypeDef",
    "IngressConfigurationOutputTypeDef",
    "IngressConfigurationTypeDef",
    "IngressVpcConfigurationOutputTypeDef",
    "InstanceConfigurationOutputTypeDef",
    "ListAutoScalingConfigurationsRequestRequestTypeDef",
    "ListConnectionsRequestRequestTypeDef",
    "ListObservabilityConfigurationsRequestRequestTypeDef",
    "ObservabilityConfigurationSummaryTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "OperationSummaryTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ServiceSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "ListVpcConnectorsRequestRequestTypeDef",
    "ListVpcIngressConnectionsFilterTypeDef",
    "VpcIngressConnectionSummaryTypeDef",
    "TraceConfigurationOutputTypeDef",
    "PauseServiceRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeServiceRequestRequestTypeDef",
    "ServiceObservabilityConfigurationOutputTypeDef",
    "StartDeploymentRequestRequestTypeDef",
    "StartDeploymentResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ListAutoScalingConfigurationsResponseTypeDef",
    "CreateAutoScalingConfigurationResponseTypeDef",
    "DeleteAutoScalingConfigurationResponseTypeDef",
    "DescribeAutoScalingConfigurationResponseTypeDef",
    "CustomDomainTypeDef",
    "CodeConfigurationOutputTypeDef",
    "CodeConfigurationTypeDef",
    "ListConnectionsResponseTypeDef",
    "CreateConnectionResponseTypeDef",
    "DeleteConnectionResponseTypeDef",
    "CreateAutoScalingConfigurationRequestRequestTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateVpcConnectorRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateObservabilityConfigurationRequestRequestTypeDef",
    "CreateVpcConnectorResponseTypeDef",
    "DeleteVpcConnectorResponseTypeDef",
    "DescribeVpcConnectorResponseTypeDef",
    "ListVpcConnectorsResponseTypeDef",
    "CreateVpcIngressConnectionRequestRequestTypeDef",
    "UpdateVpcIngressConnectionRequestRequestTypeDef",
    "ImageRepositoryOutputTypeDef",
    "ImageRepositoryTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "VpcIngressConnectionTypeDef",
    "ListObservabilityConfigurationsResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVpcIngressConnectionsRequestRequestTypeDef",
    "ListVpcIngressConnectionsResponseTypeDef",
    "ObservabilityConfigurationTypeDef",
    "AssociateCustomDomainResponseTypeDef",
    "DescribeCustomDomainsResponseTypeDef",
    "DisassociateCustomDomainResponseTypeDef",
    "CodeRepositoryOutputTypeDef",
    "CodeRepositoryTypeDef",
    "CreateVpcIngressConnectionResponseTypeDef",
    "DeleteVpcIngressConnectionResponseTypeDef",
    "DescribeVpcIngressConnectionResponseTypeDef",
    "UpdateVpcIngressConnectionResponseTypeDef",
    "CreateObservabilityConfigurationResponseTypeDef",
    "DeleteObservabilityConfigurationResponseTypeDef",
    "DescribeObservabilityConfigurationResponseTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "ServiceTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteServiceResponseTypeDef",
    "DescribeServiceResponseTypeDef",
    "PauseServiceResponseTypeDef",
    "ResumeServiceResponseTypeDef",
    "UpdateServiceResponseTypeDef",
)

_RequiredAssociateCustomDomainRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateCustomDomainRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
    },
)
_OptionalAssociateCustomDomainRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateCustomDomainRequestRequestTypeDef",
    {
        "EnableWWWSubdomain": bool,
    },
    total=False,
)

class AssociateCustomDomainRequestRequestTypeDef(
    _RequiredAssociateCustomDomainRequestRequestTypeDef,
    _OptionalAssociateCustomDomainRequestRequestTypeDef,
):
    pass

VpcDNSTargetTypeDef = TypedDict(
    "VpcDNSTargetTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "VpcId": str,
        "DomainName": str,
    },
    total=False,
)

AuthenticationConfigurationOutputTypeDef = TypedDict(
    "AuthenticationConfigurationOutputTypeDef",
    {
        "ConnectionArn": str,
        "AccessRoleArn": str,
    },
    total=False,
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "ConnectionArn": str,
        "AccessRoleArn": str,
    },
    total=False,
)

AutoScalingConfigurationSummaryTypeDef = TypedDict(
    "AutoScalingConfigurationSummaryTypeDef",
    {
        "AutoScalingConfigurationArn": str,
        "AutoScalingConfigurationName": str,
        "AutoScalingConfigurationRevision": int,
    },
    total=False,
)

AutoScalingConfigurationTypeDef = TypedDict(
    "AutoScalingConfigurationTypeDef",
    {
        "AutoScalingConfigurationArn": str,
        "AutoScalingConfigurationName": str,
        "AutoScalingConfigurationRevision": int,
        "Latest": bool,
        "Status": AutoScalingConfigurationStatusType,
        "MaxConcurrency": int,
        "MinSize": int,
        "MaxSize": int,
        "CreatedAt": datetime,
        "DeletedAt": datetime,
    },
    total=False,
)

CertificateValidationRecordTypeDef = TypedDict(
    "CertificateValidationRecordTypeDef",
    {
        "Name": str,
        "Type": str,
        "Value": str,
        "Status": CertificateValidationRecordStatusType,
    },
    total=False,
)

_RequiredCodeConfigurationValuesOutputTypeDef = TypedDict(
    "_RequiredCodeConfigurationValuesOutputTypeDef",
    {
        "Runtime": RuntimeType,
    },
)
_OptionalCodeConfigurationValuesOutputTypeDef = TypedDict(
    "_OptionalCodeConfigurationValuesOutputTypeDef",
    {
        "BuildCommand": str,
        "StartCommand": str,
        "Port": str,
        "RuntimeEnvironmentVariables": Dict[str, str],
        "RuntimeEnvironmentSecrets": Dict[str, str],
    },
    total=False,
)

class CodeConfigurationValuesOutputTypeDef(
    _RequiredCodeConfigurationValuesOutputTypeDef, _OptionalCodeConfigurationValuesOutputTypeDef
):
    pass

_RequiredCodeConfigurationValuesTypeDef = TypedDict(
    "_RequiredCodeConfigurationValuesTypeDef",
    {
        "Runtime": RuntimeType,
    },
)
_OptionalCodeConfigurationValuesTypeDef = TypedDict(
    "_OptionalCodeConfigurationValuesTypeDef",
    {
        "BuildCommand": str,
        "StartCommand": str,
        "Port": str,
        "RuntimeEnvironmentVariables": Mapping[str, str],
        "RuntimeEnvironmentSecrets": Mapping[str, str],
    },
    total=False,
)

class CodeConfigurationValuesTypeDef(
    _RequiredCodeConfigurationValuesTypeDef, _OptionalCodeConfigurationValuesTypeDef
):
    pass

SourceCodeVersionOutputTypeDef = TypedDict(
    "SourceCodeVersionOutputTypeDef",
    {
        "Type": Literal["BRANCH"],
        "Value": str,
    },
)

SourceCodeVersionTypeDef = TypedDict(
    "SourceCodeVersionTypeDef",
    {
        "Type": Literal["BRANCH"],
        "Value": str,
    },
)

ConnectionSummaryTypeDef = TypedDict(
    "ConnectionSummaryTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": Literal["GITHUB"],
        "Status": ConnectionStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": Literal["GITHUB"],
        "Status": ConnectionStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TraceConfigurationTypeDef = TypedDict(
    "TraceConfigurationTypeDef",
    {
        "Vendor": Literal["AWSXRAY"],
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
)

HealthCheckConfigurationTypeDef = TypedDict(
    "HealthCheckConfigurationTypeDef",
    {
        "Protocol": HealthCheckProtocolType,
        "Path": str,
        "Interval": int,
        "Timeout": int,
        "HealthyThreshold": int,
        "UnhealthyThreshold": int,
    },
    total=False,
)

InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "Cpu": str,
        "Memory": str,
        "InstanceRoleArn": str,
    },
    total=False,
)

_RequiredServiceObservabilityConfigurationTypeDef = TypedDict(
    "_RequiredServiceObservabilityConfigurationTypeDef",
    {
        "ObservabilityEnabled": bool,
    },
)
_OptionalServiceObservabilityConfigurationTypeDef = TypedDict(
    "_OptionalServiceObservabilityConfigurationTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
    total=False,
)

class ServiceObservabilityConfigurationTypeDef(
    _RequiredServiceObservabilityConfigurationTypeDef,
    _OptionalServiceObservabilityConfigurationTypeDef,
):
    pass

VpcConnectorTypeDef = TypedDict(
    "VpcConnectorTypeDef",
    {
        "VpcConnectorName": str,
        "VpcConnectorArn": str,
        "VpcConnectorRevision": int,
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "Status": VpcConnectorStatusType,
        "CreatedAt": datetime,
        "DeletedAt": datetime,
    },
    total=False,
)

IngressVpcConfigurationTypeDef = TypedDict(
    "IngressVpcConfigurationTypeDef",
    {
        "VpcId": str,
        "VpcEndpointId": str,
    },
    total=False,
)

DeleteAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)

DeleteObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

DeleteVpcConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorArn": str,
    },
)

DeleteVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
    },
)

DescribeAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)

_RequiredDescribeCustomDomainsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeCustomDomainsRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalDescribeCustomDomainsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeCustomDomainsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeCustomDomainsRequestRequestTypeDef(
    _RequiredDescribeCustomDomainsRequestRequestTypeDef,
    _OptionalDescribeCustomDomainsRequestRequestTypeDef,
):
    pass

DescribeObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
)

DescribeServiceRequestRequestTypeDef = TypedDict(
    "DescribeServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

DescribeVpcConnectorRequestRequestTypeDef = TypedDict(
    "DescribeVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorArn": str,
    },
)

DescribeVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "DescribeVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
    },
)

DisassociateCustomDomainRequestRequestTypeDef = TypedDict(
    "DisassociateCustomDomainRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
    },
)

EgressConfigurationOutputTypeDef = TypedDict(
    "EgressConfigurationOutputTypeDef",
    {
        "EgressType": EgressTypeType,
        "VpcConnectorArn": str,
    },
    total=False,
)

EgressConfigurationTypeDef = TypedDict(
    "EgressConfigurationTypeDef",
    {
        "EgressType": EgressTypeType,
        "VpcConnectorArn": str,
    },
    total=False,
)

EncryptionConfigurationOutputTypeDef = TypedDict(
    "EncryptionConfigurationOutputTypeDef",
    {
        "KmsKey": str,
    },
)

HealthCheckConfigurationOutputTypeDef = TypedDict(
    "HealthCheckConfigurationOutputTypeDef",
    {
        "Protocol": HealthCheckProtocolType,
        "Path": str,
        "Interval": int,
        "Timeout": int,
        "HealthyThreshold": int,
        "UnhealthyThreshold": int,
    },
    total=False,
)

ImageConfigurationOutputTypeDef = TypedDict(
    "ImageConfigurationOutputTypeDef",
    {
        "RuntimeEnvironmentVariables": Dict[str, str],
        "StartCommand": str,
        "Port": str,
        "RuntimeEnvironmentSecrets": Dict[str, str],
    },
    total=False,
)

ImageConfigurationTypeDef = TypedDict(
    "ImageConfigurationTypeDef",
    {
        "RuntimeEnvironmentVariables": Mapping[str, str],
        "StartCommand": str,
        "Port": str,
        "RuntimeEnvironmentSecrets": Mapping[str, str],
    },
    total=False,
)

IngressConfigurationOutputTypeDef = TypedDict(
    "IngressConfigurationOutputTypeDef",
    {
        "IsPubliclyAccessible": bool,
    },
    total=False,
)

IngressConfigurationTypeDef = TypedDict(
    "IngressConfigurationTypeDef",
    {
        "IsPubliclyAccessible": bool,
    },
    total=False,
)

IngressVpcConfigurationOutputTypeDef = TypedDict(
    "IngressVpcConfigurationOutputTypeDef",
    {
        "VpcId": str,
        "VpcEndpointId": str,
    },
    total=False,
)

InstanceConfigurationOutputTypeDef = TypedDict(
    "InstanceConfigurationOutputTypeDef",
    {
        "Cpu": str,
        "Memory": str,
        "InstanceRoleArn": str,
    },
    total=False,
)

ListAutoScalingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListAutoScalingConfigurationsRequestRequestTypeDef",
    {
        "AutoScalingConfigurationName": str,
        "LatestOnly": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectionsRequestRequestTypeDef = TypedDict(
    "ListConnectionsRequestRequestTypeDef",
    {
        "ConnectionName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListObservabilityConfigurationsRequestRequestTypeDef = TypedDict(
    "ListObservabilityConfigurationsRequestRequestTypeDef",
    {
        "ObservabilityConfigurationName": str,
        "LatestOnly": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ObservabilityConfigurationSummaryTypeDef = TypedDict(
    "ObservabilityConfigurationSummaryTypeDef",
    {
        "ObservabilityConfigurationArn": str,
        "ObservabilityConfigurationName": str,
        "ObservabilityConfigurationRevision": int,
    },
    total=False,
)

_RequiredListOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListOperationsRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalListOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListOperationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListOperationsRequestRequestTypeDef(
    _RequiredListOperationsRequestRequestTypeDef, _OptionalListOperationsRequestRequestTypeDef
):
    pass

OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": str,
        "Type": OperationTypeType,
        "Status": OperationStatusType,
        "TargetArn": str,
        "StartedAt": datetime,
        "EndedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceArn": str,
        "ServiceUrl": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": ServiceStatusType,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

ListVpcConnectorsRequestRequestTypeDef = TypedDict(
    "ListVpcConnectorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListVpcIngressConnectionsFilterTypeDef = TypedDict(
    "ListVpcIngressConnectionsFilterTypeDef",
    {
        "ServiceArn": str,
        "VpcEndpointId": str,
    },
    total=False,
)

VpcIngressConnectionSummaryTypeDef = TypedDict(
    "VpcIngressConnectionSummaryTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "ServiceArn": str,
    },
    total=False,
)

TraceConfigurationOutputTypeDef = TypedDict(
    "TraceConfigurationOutputTypeDef",
    {
        "Vendor": Literal["AWSXRAY"],
    },
)

PauseServiceRequestRequestTypeDef = TypedDict(
    "PauseServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
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

ResumeServiceRequestRequestTypeDef = TypedDict(
    "ResumeServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

_RequiredServiceObservabilityConfigurationOutputTypeDef = TypedDict(
    "_RequiredServiceObservabilityConfigurationOutputTypeDef",
    {
        "ObservabilityEnabled": bool,
    },
)
_OptionalServiceObservabilityConfigurationOutputTypeDef = TypedDict(
    "_OptionalServiceObservabilityConfigurationOutputTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
    total=False,
)

class ServiceObservabilityConfigurationOutputTypeDef(
    _RequiredServiceObservabilityConfigurationOutputTypeDef,
    _OptionalServiceObservabilityConfigurationOutputTypeDef,
):
    pass

StartDeploymentRequestRequestTypeDef = TypedDict(
    "StartDeploymentRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

StartDeploymentResponseTypeDef = TypedDict(
    "StartDeploymentResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

ListAutoScalingConfigurationsResponseTypeDef = TypedDict(
    "ListAutoScalingConfigurationsResponseTypeDef",
    {
        "AutoScalingConfigurationSummaryList": List[AutoScalingConfigurationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAutoScalingConfigurationResponseTypeDef = TypedDict(
    "CreateAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomDomainTypeDef = TypedDict(
    "_RequiredCustomDomainTypeDef",
    {
        "DomainName": str,
        "EnableWWWSubdomain": bool,
        "Status": CustomDomainAssociationStatusType,
    },
)
_OptionalCustomDomainTypeDef = TypedDict(
    "_OptionalCustomDomainTypeDef",
    {
        "CertificateValidationRecords": List[CertificateValidationRecordTypeDef],
    },
    total=False,
)

class CustomDomainTypeDef(_RequiredCustomDomainTypeDef, _OptionalCustomDomainTypeDef):
    pass

_RequiredCodeConfigurationOutputTypeDef = TypedDict(
    "_RequiredCodeConfigurationOutputTypeDef",
    {
        "ConfigurationSource": ConfigurationSourceType,
    },
)
_OptionalCodeConfigurationOutputTypeDef = TypedDict(
    "_OptionalCodeConfigurationOutputTypeDef",
    {
        "CodeConfigurationValues": CodeConfigurationValuesOutputTypeDef,
    },
    total=False,
)

class CodeConfigurationOutputTypeDef(
    _RequiredCodeConfigurationOutputTypeDef, _OptionalCodeConfigurationOutputTypeDef
):
    pass

_RequiredCodeConfigurationTypeDef = TypedDict(
    "_RequiredCodeConfigurationTypeDef",
    {
        "ConfigurationSource": ConfigurationSourceType,
    },
)
_OptionalCodeConfigurationTypeDef = TypedDict(
    "_OptionalCodeConfigurationTypeDef",
    {
        "CodeConfigurationValues": CodeConfigurationValuesTypeDef,
    },
    total=False,
)

class CodeConfigurationTypeDef(
    _RequiredCodeConfigurationTypeDef, _OptionalCodeConfigurationTypeDef
):
    pass

ListConnectionsResponseTypeDef = TypedDict(
    "ListConnectionsResponseTypeDef",
    {
        "ConnectionSummaryList": List[ConnectionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationName": str,
    },
)
_OptionalCreateAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAutoScalingConfigurationRequestRequestTypeDef",
    {
        "MaxConcurrency": int,
        "MinSize": int,
        "MaxSize": int,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateAutoScalingConfigurationRequestRequestTypeDef(
    _RequiredCreateAutoScalingConfigurationRequestRequestTypeDef,
    _OptionalCreateAutoScalingConfigurationRequestRequestTypeDef,
):
    pass

_RequiredCreateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestRequestTypeDef",
    {
        "ConnectionName": str,
        "ProviderType": Literal["GITHUB"],
    },
)
_OptionalCreateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateConnectionRequestRequestTypeDef(
    _RequiredCreateConnectionRequestRequestTypeDef, _OptionalCreateConnectionRequestRequestTypeDef
):
    pass

_RequiredCreateVpcConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorName": str,
        "Subnets": Sequence[str],
    },
)
_OptionalCreateVpcConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcConnectorRequestRequestTypeDef",
    {
        "SecurityGroups": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateVpcConnectorRequestRequestTypeDef(
    _RequiredCreateVpcConnectorRequestRequestTypeDef,
    _OptionalCreateVpcConnectorRequestRequestTypeDef,
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredCreateObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationName": str,
    },
)
_OptionalCreateObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateObservabilityConfigurationRequestRequestTypeDef",
    {
        "TraceConfiguration": TraceConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateObservabilityConfigurationRequestRequestTypeDef(
    _RequiredCreateObservabilityConfigurationRequestRequestTypeDef,
    _OptionalCreateObservabilityConfigurationRequestRequestTypeDef,
):
    pass

CreateVpcConnectorResponseTypeDef = TypedDict(
    "CreateVpcConnectorResponseTypeDef",
    {
        "VpcConnector": VpcConnectorTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcConnectorResponseTypeDef = TypedDict(
    "DeleteVpcConnectorResponseTypeDef",
    {
        "VpcConnector": VpcConnectorTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcConnectorResponseTypeDef = TypedDict(
    "DescribeVpcConnectorResponseTypeDef",
    {
        "VpcConnector": VpcConnectorTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVpcConnectorsResponseTypeDef = TypedDict(
    "ListVpcConnectorsResponseTypeDef",
    {
        "VpcConnectors": List[VpcConnectorTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcIngressConnectionRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "VpcIngressConnectionName": str,
        "IngressVpcConfiguration": IngressVpcConfigurationTypeDef,
    },
)
_OptionalCreateVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcIngressConnectionRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateVpcIngressConnectionRequestRequestTypeDef(
    _RequiredCreateVpcIngressConnectionRequestRequestTypeDef,
    _OptionalCreateVpcIngressConnectionRequestRequestTypeDef,
):
    pass

UpdateVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "UpdateVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "IngressVpcConfiguration": IngressVpcConfigurationTypeDef,
    },
)

_RequiredImageRepositoryOutputTypeDef = TypedDict(
    "_RequiredImageRepositoryOutputTypeDef",
    {
        "ImageIdentifier": str,
        "ImageRepositoryType": ImageRepositoryTypeType,
    },
)
_OptionalImageRepositoryOutputTypeDef = TypedDict(
    "_OptionalImageRepositoryOutputTypeDef",
    {
        "ImageConfiguration": ImageConfigurationOutputTypeDef,
    },
    total=False,
)

class ImageRepositoryOutputTypeDef(
    _RequiredImageRepositoryOutputTypeDef, _OptionalImageRepositoryOutputTypeDef
):
    pass

_RequiredImageRepositoryTypeDef = TypedDict(
    "_RequiredImageRepositoryTypeDef",
    {
        "ImageIdentifier": str,
        "ImageRepositoryType": ImageRepositoryTypeType,
    },
)
_OptionalImageRepositoryTypeDef = TypedDict(
    "_OptionalImageRepositoryTypeDef",
    {
        "ImageConfiguration": ImageConfigurationTypeDef,
    },
    total=False,
)

class ImageRepositoryTypeDef(_RequiredImageRepositoryTypeDef, _OptionalImageRepositoryTypeDef):
    pass

NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "EgressConfiguration": EgressConfigurationOutputTypeDef,
        "IngressConfiguration": IngressConfigurationOutputTypeDef,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "EgressConfiguration": EgressConfigurationTypeDef,
        "IngressConfiguration": IngressConfigurationTypeDef,
    },
    total=False,
)

VpcIngressConnectionTypeDef = TypedDict(
    "VpcIngressConnectionTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "VpcIngressConnectionName": str,
        "ServiceArn": str,
        "Status": VpcIngressConnectionStatusType,
        "AccountId": str,
        "DomainName": str,
        "IngressVpcConfiguration": IngressVpcConfigurationOutputTypeDef,
        "CreatedAt": datetime,
        "DeletedAt": datetime,
    },
    total=False,
)

ListObservabilityConfigurationsResponseTypeDef = TypedDict(
    "ListObservabilityConfigurationsResponseTypeDef",
    {
        "ObservabilityConfigurationSummaryList": List[ObservabilityConfigurationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "OperationSummaryList": List[OperationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "ServiceSummaryList": List[ServiceSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVpcIngressConnectionsRequestRequestTypeDef = TypedDict(
    "ListVpcIngressConnectionsRequestRequestTypeDef",
    {
        "Filter": ListVpcIngressConnectionsFilterTypeDef,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListVpcIngressConnectionsResponseTypeDef = TypedDict(
    "ListVpcIngressConnectionsResponseTypeDef",
    {
        "VpcIngressConnectionSummaryList": List[VpcIngressConnectionSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObservabilityConfigurationTypeDef = TypedDict(
    "ObservabilityConfigurationTypeDef",
    {
        "ObservabilityConfigurationArn": str,
        "ObservabilityConfigurationName": str,
        "TraceConfiguration": TraceConfigurationOutputTypeDef,
        "ObservabilityConfigurationRevision": int,
        "Latest": bool,
        "Status": ObservabilityConfigurationStatusType,
        "CreatedAt": datetime,
        "DeletedAt": datetime,
    },
    total=False,
)

AssociateCustomDomainResponseTypeDef = TypedDict(
    "AssociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": CustomDomainTypeDef,
        "VpcDNSTargets": List[VpcDNSTargetTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomDomainsResponseTypeDef = TypedDict(
    "DescribeCustomDomainsResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomains": List[CustomDomainTypeDef],
        "VpcDNSTargets": List[VpcDNSTargetTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateCustomDomainResponseTypeDef = TypedDict(
    "DisassociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": CustomDomainTypeDef,
        "VpcDNSTargets": List[VpcDNSTargetTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCodeRepositoryOutputTypeDef = TypedDict(
    "_RequiredCodeRepositoryOutputTypeDef",
    {
        "RepositoryUrl": str,
        "SourceCodeVersion": SourceCodeVersionOutputTypeDef,
    },
)
_OptionalCodeRepositoryOutputTypeDef = TypedDict(
    "_OptionalCodeRepositoryOutputTypeDef",
    {
        "CodeConfiguration": CodeConfigurationOutputTypeDef,
    },
    total=False,
)

class CodeRepositoryOutputTypeDef(
    _RequiredCodeRepositoryOutputTypeDef, _OptionalCodeRepositoryOutputTypeDef
):
    pass

_RequiredCodeRepositoryTypeDef = TypedDict(
    "_RequiredCodeRepositoryTypeDef",
    {
        "RepositoryUrl": str,
        "SourceCodeVersion": SourceCodeVersionTypeDef,
    },
)
_OptionalCodeRepositoryTypeDef = TypedDict(
    "_OptionalCodeRepositoryTypeDef",
    {
        "CodeConfiguration": CodeConfigurationTypeDef,
    },
    total=False,
)

class CodeRepositoryTypeDef(_RequiredCodeRepositoryTypeDef, _OptionalCodeRepositoryTypeDef):
    pass

CreateVpcIngressConnectionResponseTypeDef = TypedDict(
    "CreateVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": VpcIngressConnectionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcIngressConnectionResponseTypeDef = TypedDict(
    "DeleteVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": VpcIngressConnectionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcIngressConnectionResponseTypeDef = TypedDict(
    "DescribeVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": VpcIngressConnectionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVpcIngressConnectionResponseTypeDef = TypedDict(
    "UpdateVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": VpcIngressConnectionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateObservabilityConfigurationResponseTypeDef = TypedDict(
    "CreateObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": ObservabilityConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObservabilityConfigurationResponseTypeDef = TypedDict(
    "DeleteObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": ObservabilityConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeObservabilityConfigurationResponseTypeDef = TypedDict(
    "DescribeObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": ObservabilityConfigurationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "CodeRepository": CodeRepositoryOutputTypeDef,
        "ImageRepository": ImageRepositoryOutputTypeDef,
        "AutoDeploymentsEnabled": bool,
        "AuthenticationConfiguration": AuthenticationConfigurationOutputTypeDef,
    },
    total=False,
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "CodeRepository": CodeRepositoryTypeDef,
        "ImageRepository": ImageRepositoryTypeDef,
        "AutoDeploymentsEnabled": bool,
        "AuthenticationConfiguration": AuthenticationConfigurationTypeDef,
    },
    total=False,
)

_RequiredServiceTypeDef = TypedDict(
    "_RequiredServiceTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceArn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": ServiceStatusType,
        "SourceConfiguration": SourceConfigurationOutputTypeDef,
        "InstanceConfiguration": InstanceConfigurationOutputTypeDef,
        "AutoScalingConfigurationSummary": AutoScalingConfigurationSummaryTypeDef,
        "NetworkConfiguration": NetworkConfigurationOutputTypeDef,
    },
)
_OptionalServiceTypeDef = TypedDict(
    "_OptionalServiceTypeDef",
    {
        "ServiceUrl": str,
        "DeletedAt": datetime,
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
        "HealthCheckConfiguration": HealthCheckConfigurationOutputTypeDef,
        "ObservabilityConfiguration": ServiceObservabilityConfigurationOutputTypeDef,
    },
    total=False,
)

class ServiceTypeDef(_RequiredServiceTypeDef, _OptionalServiceTypeDef):
    pass

_RequiredCreateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestRequestTypeDef",
    {
        "ServiceName": str,
        "SourceConfiguration": SourceConfigurationTypeDef,
    },
)
_OptionalCreateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestRequestTypeDef",
    {
        "InstanceConfiguration": InstanceConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "HealthCheckConfiguration": HealthCheckConfigurationTypeDef,
        "AutoScalingConfigurationArn": str,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "ObservabilityConfiguration": ServiceObservabilityConfigurationTypeDef,
    },
    total=False,
)

class CreateServiceRequestRequestTypeDef(
    _RequiredCreateServiceRequestRequestTypeDef, _OptionalCreateServiceRequestRequestTypeDef
):
    pass

_RequiredUpdateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
_OptionalUpdateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceRequestRequestTypeDef",
    {
        "SourceConfiguration": SourceConfigurationTypeDef,
        "InstanceConfiguration": InstanceConfigurationTypeDef,
        "AutoScalingConfigurationArn": str,
        "HealthCheckConfiguration": HealthCheckConfigurationTypeDef,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "ObservabilityConfiguration": ServiceObservabilityConfigurationTypeDef,
    },
    total=False,
)

class UpdateServiceRequestRequestTypeDef(
    _RequiredUpdateServiceRequestRequestTypeDef, _OptionalUpdateServiceRequestRequestTypeDef
):
    pass

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceResponseTypeDef = TypedDict(
    "DescribeServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PauseServiceResponseTypeDef = TypedDict(
    "PauseServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResumeServiceResponseTypeDef = TypedDict(
    "ResumeServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
