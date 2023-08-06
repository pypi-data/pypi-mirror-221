"""
Type annotations for network-firewall service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/type_defs/)

Usage::

    ```python
    from mypy_boto3_network_firewall.type_defs import AddressOutputTypeDef

    data: AddressOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AttachmentStatusType,
    ConfigurationSyncStateType,
    EncryptionTypeType,
    FirewallStatusValueType,
    GeneratedRulesTypeType,
    IPAddressTypeType,
    LogDestinationTypeType,
    LogTypeType,
    PerObjectSyncStatusType,
    ResourceManagedStatusType,
    ResourceManagedTypeType,
    ResourceStatusType,
    RuleGroupTypeType,
    RuleOrderType,
    StatefulActionType,
    StatefulRuleDirectionType,
    StatefulRuleProtocolType,
    StreamExceptionPolicyType,
    TargetTypeType,
    TCPFlagType,
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
    "AddressOutputTypeDef",
    "AddressTypeDef",
    "AssociateFirewallPolicyRequestRequestTypeDef",
    "AssociateFirewallPolicyResponseTypeDef",
    "SubnetMappingTypeDef",
    "SubnetMappingOutputTypeDef",
    "AttachmentTypeDef",
    "IPSetMetadataTypeDef",
    "EncryptionConfigurationTypeDef",
    "TagTypeDef",
    "SourceMetadataTypeDef",
    "DeleteFirewallPolicyRequestRequestTypeDef",
    "DeleteFirewallRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteTLSInspectionConfigurationRequestRequestTypeDef",
    "DescribeFirewallPolicyRequestRequestTypeDef",
    "DescribeFirewallRequestRequestTypeDef",
    "DescribeLoggingConfigurationRequestRequestTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeRuleGroupMetadataRequestRequestTypeDef",
    "StatefulRuleOptionsOutputTypeDef",
    "DescribeRuleGroupRequestRequestTypeDef",
    "DescribeTLSInspectionConfigurationRequestRequestTypeDef",
    "DimensionOutputTypeDef",
    "DimensionTypeDef",
    "DisassociateSubnetsRequestRequestTypeDef",
    "EncryptionConfigurationOutputTypeDef",
    "FirewallMetadataTypeDef",
    "FirewallPolicyMetadataTypeDef",
    "StatefulEngineOptionsOutputTypeDef",
    "StatelessRuleGroupReferenceOutputTypeDef",
    "TagOutputTypeDef",
    "StatefulEngineOptionsTypeDef",
    "StatelessRuleGroupReferenceTypeDef",
    "HeaderOutputTypeDef",
    "HeaderTypeDef",
    "IPSetOutputTypeDef",
    "IPSetReferenceOutputTypeDef",
    "IPSetReferenceTypeDef",
    "IPSetTypeDef",
    "ListFirewallPoliciesRequestListFirewallPoliciesPaginateTypeDef",
    "ListFirewallPoliciesRequestRequestTypeDef",
    "ListFirewallsRequestListFirewallsPaginateTypeDef",
    "ListFirewallsRequestRequestTypeDef",
    "ListRuleGroupsRequestListRuleGroupsPaginateTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "RuleGroupMetadataTypeDef",
    "ListTLSInspectionConfigurationsRequestListTLSInspectionConfigurationsPaginateTypeDef",
    "ListTLSInspectionConfigurationsRequestRequestTypeDef",
    "TLSInspectionConfigurationMetadataTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "LogDestinationConfigOutputTypeDef",
    "LogDestinationConfigTypeDef",
    "PortRangeOutputTypeDef",
    "TCPFlagFieldOutputTypeDef",
    "PortRangeTypeDef",
    "TCPFlagFieldTypeDef",
    "PaginatorConfigTypeDef",
    "PerObjectStatusTypeDef",
    "PortSetOutputTypeDef",
    "PortSetTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SourceMetadataOutputTypeDef",
    "StatefulRuleOptionsTypeDef",
    "RuleOptionOutputTypeDef",
    "RuleOptionTypeDef",
    "RulesSourceListOutputTypeDef",
    "RulesSourceListTypeDef",
    "ServerCertificateOutputTypeDef",
    "ServerCertificateTypeDef",
    "StatefulRuleGroupOverrideOutputTypeDef",
    "StatefulRuleGroupOverrideTypeDef",
    "TlsCertificateDataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFirewallDeleteProtectionRequestRequestTypeDef",
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    "UpdateFirewallDescriptionRequestRequestTypeDef",
    "UpdateFirewallDescriptionResponseTypeDef",
    "UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef",
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    "UpdateSubnetChangeProtectionRequestRequestTypeDef",
    "UpdateSubnetChangeProtectionResponseTypeDef",
    "AssociateSubnetsRequestRequestTypeDef",
    "AssociateSubnetsResponseTypeDef",
    "DisassociateSubnetsResponseTypeDef",
    "CIDRSummaryTypeDef",
    "UpdateFirewallEncryptionConfigurationRequestRequestTypeDef",
    "CreateFirewallRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DescribeRuleGroupMetadataResponseTypeDef",
    "PublishMetricActionOutputTypeDef",
    "PublishMetricActionTypeDef",
    "UpdateFirewallEncryptionConfigurationResponseTypeDef",
    "ListFirewallsResponseTypeDef",
    "ListFirewallPoliciesResponseTypeDef",
    "FirewallPolicyResponseTypeDef",
    "FirewallTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PolicyVariablesOutputTypeDef",
    "ReferenceSetsOutputTypeDef",
    "ReferenceSetsTypeDef",
    "PolicyVariablesTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTLSInspectionConfigurationsResponseTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "ServerCertificateScopeOutputTypeDef",
    "MatchAttributesOutputTypeDef",
    "ServerCertificateScopeTypeDef",
    "MatchAttributesTypeDef",
    "SyncStateTypeDef",
    "RuleVariablesOutputTypeDef",
    "RuleVariablesTypeDef",
    "RuleGroupResponseTypeDef",
    "StatefulRuleOutputTypeDef",
    "StatefulRuleTypeDef",
    "StatefulRuleGroupReferenceOutputTypeDef",
    "StatefulRuleGroupReferenceTypeDef",
    "TLSInspectionConfigurationResponseTypeDef",
    "CapacityUsageSummaryTypeDef",
    "ActionDefinitionOutputTypeDef",
    "ActionDefinitionTypeDef",
    "CreateFirewallPolicyResponseTypeDef",
    "DeleteFirewallPolicyResponseTypeDef",
    "UpdateFirewallPolicyResponseTypeDef",
    "DescribeLoggingConfigurationResponseTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    "ServerCertificateConfigurationOutputTypeDef",
    "RuleDefinitionOutputTypeDef",
    "ServerCertificateConfigurationTypeDef",
    "RuleDefinitionTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "CreateTLSInspectionConfigurationResponseTypeDef",
    "DeleteTLSInspectionConfigurationResponseTypeDef",
    "UpdateTLSInspectionConfigurationResponseTypeDef",
    "FirewallStatusTypeDef",
    "CustomActionOutputTypeDef",
    "CustomActionTypeDef",
    "TLSInspectionConfigurationOutputTypeDef",
    "StatelessRuleOutputTypeDef",
    "TLSInspectionConfigurationTypeDef",
    "StatelessRuleTypeDef",
    "CreateFirewallResponseTypeDef",
    "DeleteFirewallResponseTypeDef",
    "DescribeFirewallResponseTypeDef",
    "FirewallPolicyOutputTypeDef",
    "FirewallPolicyTypeDef",
    "DescribeTLSInspectionConfigurationResponseTypeDef",
    "StatelessRulesAndCustomActionsOutputTypeDef",
    "CreateTLSInspectionConfigurationRequestRequestTypeDef",
    "UpdateTLSInspectionConfigurationRequestRequestTypeDef",
    "StatelessRulesAndCustomActionsTypeDef",
    "DescribeFirewallPolicyResponseTypeDef",
    "CreateFirewallPolicyRequestRequestTypeDef",
    "UpdateFirewallPolicyRequestRequestTypeDef",
    "RulesSourceOutputTypeDef",
    "RulesSourceTypeDef",
    "RuleGroupOutputTypeDef",
    "RuleGroupTypeDef",
    "DescribeRuleGroupResponseTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
)

AddressOutputTypeDef = TypedDict(
    "AddressOutputTypeDef",
    {
        "AddressDefinition": str,
    },
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressDefinition": str,
    },
)

_RequiredAssociateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyArn": str,
    },
)
_OptionalAssociateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateFirewallPolicyRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class AssociateFirewallPolicyRequestRequestTypeDef(
    _RequiredAssociateFirewallPolicyRequestRequestTypeDef,
    _OptionalAssociateFirewallPolicyRequestRequestTypeDef,
):
    pass


AssociateFirewallPolicyResponseTypeDef = TypedDict(
    "AssociateFirewallPolicyResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSubnetMappingTypeDef = TypedDict(
    "_RequiredSubnetMappingTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalSubnetMappingTypeDef = TypedDict(
    "_OptionalSubnetMappingTypeDef",
    {
        "IPAddressType": IPAddressTypeType,
    },
    total=False,
)


class SubnetMappingTypeDef(_RequiredSubnetMappingTypeDef, _OptionalSubnetMappingTypeDef):
    pass


_RequiredSubnetMappingOutputTypeDef = TypedDict(
    "_RequiredSubnetMappingOutputTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalSubnetMappingOutputTypeDef = TypedDict(
    "_OptionalSubnetMappingOutputTypeDef",
    {
        "IPAddressType": IPAddressTypeType,
    },
    total=False,
)


class SubnetMappingOutputTypeDef(
    _RequiredSubnetMappingOutputTypeDef, _OptionalSubnetMappingOutputTypeDef
):
    pass


AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "SubnetId": str,
        "EndpointId": str,
        "Status": AttachmentStatusType,
        "StatusMessage": str,
    },
    total=False,
)

IPSetMetadataTypeDef = TypedDict(
    "IPSetMetadataTypeDef",
    {
        "ResolvedCIDRCount": int,
    },
    total=False,
)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "Type": EncryptionTypeType,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "KeyId": str,
    },
    total=False,
)


class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SourceMetadataTypeDef = TypedDict(
    "SourceMetadataTypeDef",
    {
        "SourceArn": str,
        "SourceUpdateToken": str,
    },
    total=False,
)

DeleteFirewallPolicyRequestRequestTypeDef = TypedDict(
    "DeleteFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
    },
    total=False,
)

DeleteFirewallRequestRequestTypeDef = TypedDict(
    "DeleteFirewallRequestRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "RuleGroupArn": str,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

DeleteTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfigurationArn": str,
        "TLSInspectionConfigurationName": str,
    },
    total=False,
)

DescribeFirewallPolicyRequestRequestTypeDef = TypedDict(
    "DescribeFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
    },
    total=False,
)

DescribeFirewallRequestRequestTypeDef = TypedDict(
    "DescribeFirewallRequestRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

DescribeLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLoggingConfigurationRequestRequestTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)

DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupMetadataRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupMetadataRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "RuleGroupArn": str,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

StatefulRuleOptionsOutputTypeDef = TypedDict(
    "StatefulRuleOptionsOutputTypeDef",
    {
        "RuleOrder": RuleOrderType,
    },
    total=False,
)

DescribeRuleGroupRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "RuleGroupArn": str,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

DescribeTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfigurationArn": str,
        "TLSInspectionConfigurationName": str,
    },
    total=False,
)

DimensionOutputTypeDef = TypedDict(
    "DimensionOutputTypeDef",
    {
        "Value": str,
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Value": str,
    },
)

_RequiredDisassociateSubnetsRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateSubnetsRequestRequestTypeDef",
    {
        "SubnetIds": Sequence[str],
    },
)
_OptionalDisassociateSubnetsRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateSubnetsRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class DisassociateSubnetsRequestRequestTypeDef(
    _RequiredDisassociateSubnetsRequestRequestTypeDef,
    _OptionalDisassociateSubnetsRequestRequestTypeDef,
):
    pass


_RequiredEncryptionConfigurationOutputTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationOutputTypeDef",
    {
        "Type": EncryptionTypeType,
    },
)
_OptionalEncryptionConfigurationOutputTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationOutputTypeDef",
    {
        "KeyId": str,
    },
    total=False,
)


class EncryptionConfigurationOutputTypeDef(
    _RequiredEncryptionConfigurationOutputTypeDef, _OptionalEncryptionConfigurationOutputTypeDef
):
    pass


FirewallMetadataTypeDef = TypedDict(
    "FirewallMetadataTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
    },
    total=False,
)

FirewallPolicyMetadataTypeDef = TypedDict(
    "FirewallPolicyMetadataTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

StatefulEngineOptionsOutputTypeDef = TypedDict(
    "StatefulEngineOptionsOutputTypeDef",
    {
        "RuleOrder": RuleOrderType,
        "StreamExceptionPolicy": StreamExceptionPolicyType,
    },
    total=False,
)

StatelessRuleGroupReferenceOutputTypeDef = TypedDict(
    "StatelessRuleGroupReferenceOutputTypeDef",
    {
        "ResourceArn": str,
        "Priority": int,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

StatefulEngineOptionsTypeDef = TypedDict(
    "StatefulEngineOptionsTypeDef",
    {
        "RuleOrder": RuleOrderType,
        "StreamExceptionPolicy": StreamExceptionPolicyType,
    },
    total=False,
)

StatelessRuleGroupReferenceTypeDef = TypedDict(
    "StatelessRuleGroupReferenceTypeDef",
    {
        "ResourceArn": str,
        "Priority": int,
    },
)

HeaderOutputTypeDef = TypedDict(
    "HeaderOutputTypeDef",
    {
        "Protocol": StatefulRuleProtocolType,
        "Source": str,
        "SourcePort": str,
        "Direction": StatefulRuleDirectionType,
        "Destination": str,
        "DestinationPort": str,
    },
)

HeaderTypeDef = TypedDict(
    "HeaderTypeDef",
    {
        "Protocol": StatefulRuleProtocolType,
        "Source": str,
        "SourcePort": str,
        "Direction": StatefulRuleDirectionType,
        "Destination": str,
        "DestinationPort": str,
    },
)

IPSetOutputTypeDef = TypedDict(
    "IPSetOutputTypeDef",
    {
        "Definition": List[str],
    },
)

IPSetReferenceOutputTypeDef = TypedDict(
    "IPSetReferenceOutputTypeDef",
    {
        "ReferenceArn": str,
    },
    total=False,
)

IPSetReferenceTypeDef = TypedDict(
    "IPSetReferenceTypeDef",
    {
        "ReferenceArn": str,
    },
    total=False,
)

IPSetTypeDef = TypedDict(
    "IPSetTypeDef",
    {
        "Definition": Sequence[str],
    },
)

ListFirewallPoliciesRequestListFirewallPoliciesPaginateTypeDef = TypedDict(
    "ListFirewallPoliciesRequestListFirewallPoliciesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListFirewallPoliciesRequestRequestTypeDef = TypedDict(
    "ListFirewallPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFirewallsRequestListFirewallsPaginateTypeDef = TypedDict(
    "ListFirewallsRequestListFirewallsPaginateTypeDef",
    {
        "VpcIds": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListFirewallsRequestRequestTypeDef = TypedDict(
    "ListFirewallsRequestRequestTypeDef",
    {
        "NextToken": str,
        "VpcIds": Sequence[str],
        "MaxResults": int,
    },
    total=False,
)

ListRuleGroupsRequestListRuleGroupsPaginateTypeDef = TypedDict(
    "ListRuleGroupsRequestListRuleGroupsPaginateTypeDef",
    {
        "Scope": ResourceManagedStatusType,
        "ManagedType": ResourceManagedTypeType,
        "Type": RuleGroupTypeType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Scope": ResourceManagedStatusType,
        "ManagedType": ResourceManagedTypeType,
        "Type": RuleGroupTypeType,
    },
    total=False,
)

RuleGroupMetadataTypeDef = TypedDict(
    "RuleGroupMetadataTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

ListTLSInspectionConfigurationsRequestListTLSInspectionConfigurationsPaginateTypeDef = TypedDict(
    "ListTLSInspectionConfigurationsRequestListTLSInspectionConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTLSInspectionConfigurationsRequestRequestTypeDef = TypedDict(
    "ListTLSInspectionConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

TLSInspectionConfigurationMetadataTypeDef = TypedDict(
    "TLSInspectionConfigurationMetadataTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(
    _RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
    _OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
):
    pass


_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass


LogDestinationConfigOutputTypeDef = TypedDict(
    "LogDestinationConfigOutputTypeDef",
    {
        "LogType": LogTypeType,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": Dict[str, str],
    },
)

LogDestinationConfigTypeDef = TypedDict(
    "LogDestinationConfigTypeDef",
    {
        "LogType": LogTypeType,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": Mapping[str, str],
    },
)

PortRangeOutputTypeDef = TypedDict(
    "PortRangeOutputTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
)

_RequiredTCPFlagFieldOutputTypeDef = TypedDict(
    "_RequiredTCPFlagFieldOutputTypeDef",
    {
        "Flags": List[TCPFlagType],
    },
)
_OptionalTCPFlagFieldOutputTypeDef = TypedDict(
    "_OptionalTCPFlagFieldOutputTypeDef",
    {
        "Masks": List[TCPFlagType],
    },
    total=False,
)


class TCPFlagFieldOutputTypeDef(
    _RequiredTCPFlagFieldOutputTypeDef, _OptionalTCPFlagFieldOutputTypeDef
):
    pass


PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
)

_RequiredTCPFlagFieldTypeDef = TypedDict(
    "_RequiredTCPFlagFieldTypeDef",
    {
        "Flags": Sequence[TCPFlagType],
    },
)
_OptionalTCPFlagFieldTypeDef = TypedDict(
    "_OptionalTCPFlagFieldTypeDef",
    {
        "Masks": Sequence[TCPFlagType],
    },
    total=False,
)


class TCPFlagFieldTypeDef(_RequiredTCPFlagFieldTypeDef, _OptionalTCPFlagFieldTypeDef):
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

PerObjectStatusTypeDef = TypedDict(
    "PerObjectStatusTypeDef",
    {
        "SyncStatus": PerObjectSyncStatusType,
        "UpdateToken": str,
    },
    total=False,
)

PortSetOutputTypeDef = TypedDict(
    "PortSetOutputTypeDef",
    {
        "Definition": List[str],
    },
    total=False,
)

PortSetTypeDef = TypedDict(
    "PortSetTypeDef",
    {
        "Definition": Sequence[str],
    },
    total=False,
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
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

SourceMetadataOutputTypeDef = TypedDict(
    "SourceMetadataOutputTypeDef",
    {
        "SourceArn": str,
        "SourceUpdateToken": str,
    },
    total=False,
)

StatefulRuleOptionsTypeDef = TypedDict(
    "StatefulRuleOptionsTypeDef",
    {
        "RuleOrder": RuleOrderType,
    },
    total=False,
)

_RequiredRuleOptionOutputTypeDef = TypedDict(
    "_RequiredRuleOptionOutputTypeDef",
    {
        "Keyword": str,
    },
)
_OptionalRuleOptionOutputTypeDef = TypedDict(
    "_OptionalRuleOptionOutputTypeDef",
    {
        "Settings": List[str],
    },
    total=False,
)


class RuleOptionOutputTypeDef(_RequiredRuleOptionOutputTypeDef, _OptionalRuleOptionOutputTypeDef):
    pass


_RequiredRuleOptionTypeDef = TypedDict(
    "_RequiredRuleOptionTypeDef",
    {
        "Keyword": str,
    },
)
_OptionalRuleOptionTypeDef = TypedDict(
    "_OptionalRuleOptionTypeDef",
    {
        "Settings": Sequence[str],
    },
    total=False,
)


class RuleOptionTypeDef(_RequiredRuleOptionTypeDef, _OptionalRuleOptionTypeDef):
    pass


RulesSourceListOutputTypeDef = TypedDict(
    "RulesSourceListOutputTypeDef",
    {
        "Targets": List[str],
        "TargetTypes": List[TargetTypeType],
        "GeneratedRulesType": GeneratedRulesTypeType,
    },
)

RulesSourceListTypeDef = TypedDict(
    "RulesSourceListTypeDef",
    {
        "Targets": Sequence[str],
        "TargetTypes": Sequence[TargetTypeType],
        "GeneratedRulesType": GeneratedRulesTypeType,
    },
)

ServerCertificateOutputTypeDef = TypedDict(
    "ServerCertificateOutputTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

ServerCertificateTypeDef = TypedDict(
    "ServerCertificateTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

StatefulRuleGroupOverrideOutputTypeDef = TypedDict(
    "StatefulRuleGroupOverrideOutputTypeDef",
    {
        "Action": Literal["DROP_TO_ALERT"],
    },
    total=False,
)

StatefulRuleGroupOverrideTypeDef = TypedDict(
    "StatefulRuleGroupOverrideTypeDef",
    {
        "Action": Literal["DROP_TO_ALERT"],
    },
    total=False,
)

TlsCertificateDataTypeDef = TypedDict(
    "TlsCertificateDataTypeDef",
    {
        "CertificateArn": str,
        "CertificateSerial": str,
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateFirewallDeleteProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallDeleteProtectionRequestRequestTypeDef",
    {
        "DeleteProtection": bool,
    },
)
_OptionalUpdateFirewallDeleteProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallDeleteProtectionRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class UpdateFirewallDeleteProtectionRequestRequestTypeDef(
    _RequiredUpdateFirewallDeleteProtectionRequestRequestTypeDef,
    _OptionalUpdateFirewallDeleteProtectionRequestRequestTypeDef,
):
    pass


UpdateFirewallDeleteProtectionResponseTypeDef = TypedDict(
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "DeleteProtection": bool,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateFirewallDescriptionRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "Description": str,
    },
    total=False,
)

UpdateFirewallDescriptionResponseTypeDef = TypedDict(
    "UpdateFirewallDescriptionResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "Description": str,
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef",
    {
        "FirewallPolicyChangeProtection": bool,
    },
)
_OptionalUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef(
    _RequiredUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef,
    _OptionalUpdateFirewallPolicyChangeProtectionRequestRequestTypeDef,
):
    pass


UpdateFirewallPolicyChangeProtectionResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "FirewallPolicyChangeProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSubnetChangeProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSubnetChangeProtectionRequestRequestTypeDef",
    {
        "SubnetChangeProtection": bool,
    },
)
_OptionalUpdateSubnetChangeProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSubnetChangeProtectionRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class UpdateSubnetChangeProtectionRequestRequestTypeDef(
    _RequiredUpdateSubnetChangeProtectionRequestRequestTypeDef,
    _OptionalUpdateSubnetChangeProtectionRequestRequestTypeDef,
):
    pass


UpdateSubnetChangeProtectionResponseTypeDef = TypedDict(
    "UpdateSubnetChangeProtectionResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetChangeProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateSubnetsRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateSubnetsRequestRequestTypeDef",
    {
        "SubnetMappings": Sequence[SubnetMappingTypeDef],
    },
)
_OptionalAssociateSubnetsRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateSubnetsRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
    },
    total=False,
)


class AssociateSubnetsRequestRequestTypeDef(
    _RequiredAssociateSubnetsRequestRequestTypeDef, _OptionalAssociateSubnetsRequestRequestTypeDef
):
    pass


AssociateSubnetsResponseTypeDef = TypedDict(
    "AssociateSubnetsResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List[SubnetMappingOutputTypeDef],
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateSubnetsResponseTypeDef = TypedDict(
    "DisassociateSubnetsResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "SubnetMappings": List[SubnetMappingOutputTypeDef],
        "UpdateToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CIDRSummaryTypeDef = TypedDict(
    "CIDRSummaryTypeDef",
    {
        "AvailableCIDRCount": int,
        "UtilizedCIDRCount": int,
        "IPSetReferences": Dict[str, IPSetMetadataTypeDef],
    },
    total=False,
)

UpdateFirewallEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateFirewallEncryptionConfigurationRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallArn": str,
        "FirewallName": str,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
    },
    total=False,
)

_RequiredCreateFirewallRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallRequestRequestTypeDef",
    {
        "FirewallName": str,
        "FirewallPolicyArn": str,
        "VpcId": str,
        "SubnetMappings": Sequence[SubnetMappingTypeDef],
    },
)
_OptionalCreateFirewallRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallRequestRequestTypeDef",
    {
        "DeleteProtection": bool,
        "SubnetChangeProtection": bool,
        "FirewallPolicyChangeProtection": bool,
        "Description": str,
        "Tags": Sequence[TagTypeDef],
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
    },
    total=False,
)


class CreateFirewallRequestRequestTypeDef(
    _RequiredCreateFirewallRequestRequestTypeDef, _OptionalCreateFirewallRequestRequestTypeDef
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

DescribeRuleGroupMetadataResponseTypeDef = TypedDict(
    "DescribeRuleGroupMetadataResponseTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "Description": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
        "StatefulRuleOptions": StatefulRuleOptionsOutputTypeDef,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PublishMetricActionOutputTypeDef = TypedDict(
    "PublishMetricActionOutputTypeDef",
    {
        "Dimensions": List[DimensionOutputTypeDef],
    },
)

PublishMetricActionTypeDef = TypedDict(
    "PublishMetricActionTypeDef",
    {
        "Dimensions": Sequence[DimensionTypeDef],
    },
)

UpdateFirewallEncryptionConfigurationResponseTypeDef = TypedDict(
    "UpdateFirewallEncryptionConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "UpdateToken": str,
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallsResponseTypeDef = TypedDict(
    "ListFirewallsResponseTypeDef",
    {
        "NextToken": str,
        "Firewalls": List[FirewallMetadataTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFirewallPoliciesResponseTypeDef = TypedDict(
    "ListFirewallPoliciesResponseTypeDef",
    {
        "NextToken": str,
        "FirewallPolicies": List[FirewallPolicyMetadataTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFirewallPolicyResponseTypeDef = TypedDict(
    "_RequiredFirewallPolicyResponseTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicyArn": str,
        "FirewallPolicyId": str,
    },
)
_OptionalFirewallPolicyResponseTypeDef = TypedDict(
    "_OptionalFirewallPolicyResponseTypeDef",
    {
        "Description": str,
        "FirewallPolicyStatus": ResourceStatusType,
        "Tags": List[TagOutputTypeDef],
        "ConsumedStatelessRuleCapacity": int,
        "ConsumedStatefulRuleCapacity": int,
        "NumberOfAssociations": int,
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class FirewallPolicyResponseTypeDef(
    _RequiredFirewallPolicyResponseTypeDef, _OptionalFirewallPolicyResponseTypeDef
):
    pass


_RequiredFirewallTypeDef = TypedDict(
    "_RequiredFirewallTypeDef",
    {
        "FirewallPolicyArn": str,
        "VpcId": str,
        "SubnetMappings": List[SubnetMappingOutputTypeDef],
        "FirewallId": str,
    },
)
_OptionalFirewallTypeDef = TypedDict(
    "_OptionalFirewallTypeDef",
    {
        "FirewallName": str,
        "FirewallArn": str,
        "DeleteProtection": bool,
        "SubnetChangeProtection": bool,
        "FirewallPolicyChangeProtection": bool,
        "Description": str,
        "Tags": List[TagOutputTypeDef],
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
    },
    total=False,
)


class FirewallTypeDef(_RequiredFirewallTypeDef, _OptionalFirewallTypeDef):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextToken": str,
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PolicyVariablesOutputTypeDef = TypedDict(
    "PolicyVariablesOutputTypeDef",
    {
        "RuleVariables": Dict[str, IPSetOutputTypeDef],
    },
    total=False,
)

ReferenceSetsOutputTypeDef = TypedDict(
    "ReferenceSetsOutputTypeDef",
    {
        "IPSetReferences": Dict[str, IPSetReferenceOutputTypeDef],
    },
    total=False,
)

ReferenceSetsTypeDef = TypedDict(
    "ReferenceSetsTypeDef",
    {
        "IPSetReferences": Mapping[str, IPSetReferenceTypeDef],
    },
    total=False,
)

PolicyVariablesTypeDef = TypedDict(
    "PolicyVariablesTypeDef",
    {
        "RuleVariables": Mapping[str, IPSetTypeDef],
    },
    total=False,
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextToken": str,
        "RuleGroups": List[RuleGroupMetadataTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTLSInspectionConfigurationsResponseTypeDef = TypedDict(
    "ListTLSInspectionConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "TLSInspectionConfigurations": List[TLSInspectionConfigurationMetadataTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationOutputTypeDef = TypedDict(
    "LoggingConfigurationOutputTypeDef",
    {
        "LogDestinationConfigs": List[LogDestinationConfigOutputTypeDef],
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "LogDestinationConfigs": Sequence[LogDestinationConfigTypeDef],
    },
)

ServerCertificateScopeOutputTypeDef = TypedDict(
    "ServerCertificateScopeOutputTypeDef",
    {
        "Sources": List[AddressOutputTypeDef],
        "Destinations": List[AddressOutputTypeDef],
        "SourcePorts": List[PortRangeOutputTypeDef],
        "DestinationPorts": List[PortRangeOutputTypeDef],
        "Protocols": List[int],
    },
    total=False,
)

MatchAttributesOutputTypeDef = TypedDict(
    "MatchAttributesOutputTypeDef",
    {
        "Sources": List[AddressOutputTypeDef],
        "Destinations": List[AddressOutputTypeDef],
        "SourcePorts": List[PortRangeOutputTypeDef],
        "DestinationPorts": List[PortRangeOutputTypeDef],
        "Protocols": List[int],
        "TCPFlags": List[TCPFlagFieldOutputTypeDef],
    },
    total=False,
)

ServerCertificateScopeTypeDef = TypedDict(
    "ServerCertificateScopeTypeDef",
    {
        "Sources": Sequence[AddressTypeDef],
        "Destinations": Sequence[AddressTypeDef],
        "SourcePorts": Sequence[PortRangeTypeDef],
        "DestinationPorts": Sequence[PortRangeTypeDef],
        "Protocols": Sequence[int],
    },
    total=False,
)

MatchAttributesTypeDef = TypedDict(
    "MatchAttributesTypeDef",
    {
        "Sources": Sequence[AddressTypeDef],
        "Destinations": Sequence[AddressTypeDef],
        "SourcePorts": Sequence[PortRangeTypeDef],
        "DestinationPorts": Sequence[PortRangeTypeDef],
        "Protocols": Sequence[int],
        "TCPFlags": Sequence[TCPFlagFieldTypeDef],
    },
    total=False,
)

SyncStateTypeDef = TypedDict(
    "SyncStateTypeDef",
    {
        "Attachment": AttachmentTypeDef,
        "Config": Dict[str, PerObjectStatusTypeDef],
    },
    total=False,
)

RuleVariablesOutputTypeDef = TypedDict(
    "RuleVariablesOutputTypeDef",
    {
        "IPSets": Dict[str, IPSetOutputTypeDef],
        "PortSets": Dict[str, PortSetOutputTypeDef],
    },
    total=False,
)

RuleVariablesTypeDef = TypedDict(
    "RuleVariablesTypeDef",
    {
        "IPSets": Mapping[str, IPSetTypeDef],
        "PortSets": Mapping[str, PortSetTypeDef],
    },
    total=False,
)

_RequiredRuleGroupResponseTypeDef = TypedDict(
    "_RequiredRuleGroupResponseTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "RuleGroupId": str,
    },
)
_OptionalRuleGroupResponseTypeDef = TypedDict(
    "_OptionalRuleGroupResponseTypeDef",
    {
        "Description": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
        "RuleGroupStatus": ResourceStatusType,
        "Tags": List[TagOutputTypeDef],
        "ConsumedCapacity": int,
        "NumberOfAssociations": int,
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
        "SourceMetadata": SourceMetadataOutputTypeDef,
        "SnsTopic": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class RuleGroupResponseTypeDef(
    _RequiredRuleGroupResponseTypeDef, _OptionalRuleGroupResponseTypeDef
):
    pass


StatefulRuleOutputTypeDef = TypedDict(
    "StatefulRuleOutputTypeDef",
    {
        "Action": StatefulActionType,
        "Header": HeaderOutputTypeDef,
        "RuleOptions": List[RuleOptionOutputTypeDef],
    },
)

StatefulRuleTypeDef = TypedDict(
    "StatefulRuleTypeDef",
    {
        "Action": StatefulActionType,
        "Header": HeaderTypeDef,
        "RuleOptions": Sequence[RuleOptionTypeDef],
    },
)

_RequiredStatefulRuleGroupReferenceOutputTypeDef = TypedDict(
    "_RequiredStatefulRuleGroupReferenceOutputTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalStatefulRuleGroupReferenceOutputTypeDef = TypedDict(
    "_OptionalStatefulRuleGroupReferenceOutputTypeDef",
    {
        "Priority": int,
        "Override": StatefulRuleGroupOverrideOutputTypeDef,
    },
    total=False,
)


class StatefulRuleGroupReferenceOutputTypeDef(
    _RequiredStatefulRuleGroupReferenceOutputTypeDef,
    _OptionalStatefulRuleGroupReferenceOutputTypeDef,
):
    pass


_RequiredStatefulRuleGroupReferenceTypeDef = TypedDict(
    "_RequiredStatefulRuleGroupReferenceTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalStatefulRuleGroupReferenceTypeDef = TypedDict(
    "_OptionalStatefulRuleGroupReferenceTypeDef",
    {
        "Priority": int,
        "Override": StatefulRuleGroupOverrideTypeDef,
    },
    total=False,
)


class StatefulRuleGroupReferenceTypeDef(
    _RequiredStatefulRuleGroupReferenceTypeDef, _OptionalStatefulRuleGroupReferenceTypeDef
):
    pass


_RequiredTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "_RequiredTLSInspectionConfigurationResponseTypeDef",
    {
        "TLSInspectionConfigurationArn": str,
        "TLSInspectionConfigurationName": str,
        "TLSInspectionConfigurationId": str,
    },
)
_OptionalTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "_OptionalTLSInspectionConfigurationResponseTypeDef",
    {
        "TLSInspectionConfigurationStatus": ResourceStatusType,
        "Description": str,
        "Tags": List[TagOutputTypeDef],
        "LastModifiedTime": datetime,
        "NumberOfAssociations": int,
        "EncryptionConfiguration": EncryptionConfigurationOutputTypeDef,
        "Certificates": List[TlsCertificateDataTypeDef],
    },
    total=False,
)


class TLSInspectionConfigurationResponseTypeDef(
    _RequiredTLSInspectionConfigurationResponseTypeDef,
    _OptionalTLSInspectionConfigurationResponseTypeDef,
):
    pass


CapacityUsageSummaryTypeDef = TypedDict(
    "CapacityUsageSummaryTypeDef",
    {
        "CIDRs": CIDRSummaryTypeDef,
    },
    total=False,
)

ActionDefinitionOutputTypeDef = TypedDict(
    "ActionDefinitionOutputTypeDef",
    {
        "PublishMetricAction": PublishMetricActionOutputTypeDef,
    },
    total=False,
)

ActionDefinitionTypeDef = TypedDict(
    "ActionDefinitionTypeDef",
    {
        "PublishMetricAction": PublishMetricActionTypeDef,
    },
    total=False,
)

CreateFirewallPolicyResponseTypeDef = TypedDict(
    "CreateFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": FirewallPolicyResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallPolicyResponseTypeDef = TypedDict(
    "DeleteFirewallPolicyResponseTypeDef",
    {
        "FirewallPolicyResponse": FirewallPolicyResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFirewallPolicyResponseTypeDef = TypedDict(
    "UpdateFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": FirewallPolicyResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingConfigurationResponseTypeDef = TypedDict(
    "DescribeLoggingConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "LoggingConfiguration": LoggingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "LoggingConfiguration": LoggingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "FirewallArn": str,
        "FirewallName": str,
        "LoggingConfiguration": LoggingConfigurationTypeDef,
    },
    total=False,
)

ServerCertificateConfigurationOutputTypeDef = TypedDict(
    "ServerCertificateConfigurationOutputTypeDef",
    {
        "ServerCertificates": List[ServerCertificateOutputTypeDef],
        "Scopes": List[ServerCertificateScopeOutputTypeDef],
    },
    total=False,
)

RuleDefinitionOutputTypeDef = TypedDict(
    "RuleDefinitionOutputTypeDef",
    {
        "MatchAttributes": MatchAttributesOutputTypeDef,
        "Actions": List[str],
    },
)

ServerCertificateConfigurationTypeDef = TypedDict(
    "ServerCertificateConfigurationTypeDef",
    {
        "ServerCertificates": Sequence[ServerCertificateTypeDef],
        "Scopes": Sequence[ServerCertificateScopeTypeDef],
    },
    total=False,
)

RuleDefinitionTypeDef = TypedDict(
    "RuleDefinitionTypeDef",
    {
        "MatchAttributes": MatchAttributesTypeDef,
        "Actions": Sequence[str],
    },
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupResponse": RuleGroupResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleGroupResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseTypeDef",
    {
        "RuleGroupResponse": RuleGroupResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroupResponse": RuleGroupResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "CreateTLSInspectionConfigurationResponseTypeDef",
    {
        "UpdateToken": str,
        "TLSInspectionConfigurationResponse": TLSInspectionConfigurationResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "DeleteTLSInspectionConfigurationResponseTypeDef",
    {
        "TLSInspectionConfigurationResponse": TLSInspectionConfigurationResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "UpdateTLSInspectionConfigurationResponseTypeDef",
    {
        "UpdateToken": str,
        "TLSInspectionConfigurationResponse": TLSInspectionConfigurationResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFirewallStatusTypeDef = TypedDict(
    "_RequiredFirewallStatusTypeDef",
    {
        "Status": FirewallStatusValueType,
        "ConfigurationSyncStateSummary": ConfigurationSyncStateType,
    },
)
_OptionalFirewallStatusTypeDef = TypedDict(
    "_OptionalFirewallStatusTypeDef",
    {
        "SyncStates": Dict[str, SyncStateTypeDef],
        "CapacityUsageSummary": CapacityUsageSummaryTypeDef,
    },
    total=False,
)


class FirewallStatusTypeDef(_RequiredFirewallStatusTypeDef, _OptionalFirewallStatusTypeDef):
    pass


CustomActionOutputTypeDef = TypedDict(
    "CustomActionOutputTypeDef",
    {
        "ActionName": str,
        "ActionDefinition": ActionDefinitionOutputTypeDef,
    },
)

CustomActionTypeDef = TypedDict(
    "CustomActionTypeDef",
    {
        "ActionName": str,
        "ActionDefinition": ActionDefinitionTypeDef,
    },
)

TLSInspectionConfigurationOutputTypeDef = TypedDict(
    "TLSInspectionConfigurationOutputTypeDef",
    {
        "ServerCertificateConfigurations": List[ServerCertificateConfigurationOutputTypeDef],
    },
    total=False,
)

StatelessRuleOutputTypeDef = TypedDict(
    "StatelessRuleOutputTypeDef",
    {
        "RuleDefinition": RuleDefinitionOutputTypeDef,
        "Priority": int,
    },
)

TLSInspectionConfigurationTypeDef = TypedDict(
    "TLSInspectionConfigurationTypeDef",
    {
        "ServerCertificateConfigurations": Sequence[ServerCertificateConfigurationTypeDef],
    },
    total=False,
)

StatelessRuleTypeDef = TypedDict(
    "StatelessRuleTypeDef",
    {
        "RuleDefinition": RuleDefinitionTypeDef,
        "Priority": int,
    },
)

CreateFirewallResponseTypeDef = TypedDict(
    "CreateFirewallResponseTypeDef",
    {
        "Firewall": FirewallTypeDef,
        "FirewallStatus": FirewallStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFirewallResponseTypeDef = TypedDict(
    "DeleteFirewallResponseTypeDef",
    {
        "Firewall": FirewallTypeDef,
        "FirewallStatus": FirewallStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFirewallResponseTypeDef = TypedDict(
    "DescribeFirewallResponseTypeDef",
    {
        "UpdateToken": str,
        "Firewall": FirewallTypeDef,
        "FirewallStatus": FirewallStatusTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFirewallPolicyOutputTypeDef = TypedDict(
    "_RequiredFirewallPolicyOutputTypeDef",
    {
        "StatelessDefaultActions": List[str],
        "StatelessFragmentDefaultActions": List[str],
    },
)
_OptionalFirewallPolicyOutputTypeDef = TypedDict(
    "_OptionalFirewallPolicyOutputTypeDef",
    {
        "StatelessRuleGroupReferences": List[StatelessRuleGroupReferenceOutputTypeDef],
        "StatelessCustomActions": List[CustomActionOutputTypeDef],
        "StatefulRuleGroupReferences": List[StatefulRuleGroupReferenceOutputTypeDef],
        "StatefulDefaultActions": List[str],
        "StatefulEngineOptions": StatefulEngineOptionsOutputTypeDef,
        "TLSInspectionConfigurationArn": str,
        "PolicyVariables": PolicyVariablesOutputTypeDef,
    },
    total=False,
)


class FirewallPolicyOutputTypeDef(
    _RequiredFirewallPolicyOutputTypeDef, _OptionalFirewallPolicyOutputTypeDef
):
    pass


_RequiredFirewallPolicyTypeDef = TypedDict(
    "_RequiredFirewallPolicyTypeDef",
    {
        "StatelessDefaultActions": Sequence[str],
        "StatelessFragmentDefaultActions": Sequence[str],
    },
)
_OptionalFirewallPolicyTypeDef = TypedDict(
    "_OptionalFirewallPolicyTypeDef",
    {
        "StatelessRuleGroupReferences": Sequence[StatelessRuleGroupReferenceTypeDef],
        "StatelessCustomActions": Sequence[CustomActionTypeDef],
        "StatefulRuleGroupReferences": Sequence[StatefulRuleGroupReferenceTypeDef],
        "StatefulDefaultActions": Sequence[str],
        "StatefulEngineOptions": StatefulEngineOptionsTypeDef,
        "TLSInspectionConfigurationArn": str,
        "PolicyVariables": PolicyVariablesTypeDef,
    },
    total=False,
)


class FirewallPolicyTypeDef(_RequiredFirewallPolicyTypeDef, _OptionalFirewallPolicyTypeDef):
    pass


DescribeTLSInspectionConfigurationResponseTypeDef = TypedDict(
    "DescribeTLSInspectionConfigurationResponseTypeDef",
    {
        "UpdateToken": str,
        "TLSInspectionConfiguration": TLSInspectionConfigurationOutputTypeDef,
        "TLSInspectionConfigurationResponse": TLSInspectionConfigurationResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStatelessRulesAndCustomActionsOutputTypeDef = TypedDict(
    "_RequiredStatelessRulesAndCustomActionsOutputTypeDef",
    {
        "StatelessRules": List[StatelessRuleOutputTypeDef],
    },
)
_OptionalStatelessRulesAndCustomActionsOutputTypeDef = TypedDict(
    "_OptionalStatelessRulesAndCustomActionsOutputTypeDef",
    {
        "CustomActions": List[CustomActionOutputTypeDef],
    },
    total=False,
)


class StatelessRulesAndCustomActionsOutputTypeDef(
    _RequiredStatelessRulesAndCustomActionsOutputTypeDef,
    _OptionalStatelessRulesAndCustomActionsOutputTypeDef,
):
    pass


_RequiredCreateTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfigurationName": str,
        "TLSInspectionConfiguration": TLSInspectionConfigurationTypeDef,
    },
)
_OptionalCreateTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Sequence[TagTypeDef],
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
    },
    total=False,
)


class CreateTLSInspectionConfigurationRequestRequestTypeDef(
    _RequiredCreateTLSInspectionConfigurationRequestRequestTypeDef,
    _OptionalCreateTLSInspectionConfigurationRequestRequestTypeDef,
):
    pass


_RequiredUpdateTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfiguration": TLSInspectionConfigurationTypeDef,
        "UpdateToken": str,
    },
)
_OptionalUpdateTLSInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTLSInspectionConfigurationRequestRequestTypeDef",
    {
        "TLSInspectionConfigurationArn": str,
        "TLSInspectionConfigurationName": str,
        "Description": str,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
    },
    total=False,
)


class UpdateTLSInspectionConfigurationRequestRequestTypeDef(
    _RequiredUpdateTLSInspectionConfigurationRequestRequestTypeDef,
    _OptionalUpdateTLSInspectionConfigurationRequestRequestTypeDef,
):
    pass


_RequiredStatelessRulesAndCustomActionsTypeDef = TypedDict(
    "_RequiredStatelessRulesAndCustomActionsTypeDef",
    {
        "StatelessRules": Sequence[StatelessRuleTypeDef],
    },
)
_OptionalStatelessRulesAndCustomActionsTypeDef = TypedDict(
    "_OptionalStatelessRulesAndCustomActionsTypeDef",
    {
        "CustomActions": Sequence[CustomActionTypeDef],
    },
    total=False,
)


class StatelessRulesAndCustomActionsTypeDef(
    _RequiredStatelessRulesAndCustomActionsTypeDef, _OptionalStatelessRulesAndCustomActionsTypeDef
):
    pass


DescribeFirewallPolicyResponseTypeDef = TypedDict(
    "DescribeFirewallPolicyResponseTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicyResponse": FirewallPolicyResponseTypeDef,
        "FirewallPolicy": FirewallPolicyOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyName": str,
        "FirewallPolicy": FirewallPolicyTypeDef,
    },
)
_OptionalCreateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFirewallPolicyRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Sequence[TagTypeDef],
        "DryRun": bool,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
    },
    total=False,
)


class CreateFirewallPolicyRequestRequestTypeDef(
    _RequiredCreateFirewallPolicyRequestRequestTypeDef,
    _OptionalCreateFirewallPolicyRequestRequestTypeDef,
):
    pass


_RequiredUpdateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFirewallPolicyRequestRequestTypeDef",
    {
        "UpdateToken": str,
        "FirewallPolicy": FirewallPolicyTypeDef,
    },
)
_OptionalUpdateFirewallPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFirewallPolicyRequestRequestTypeDef",
    {
        "FirewallPolicyArn": str,
        "FirewallPolicyName": str,
        "Description": str,
        "DryRun": bool,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
    },
    total=False,
)


class UpdateFirewallPolicyRequestRequestTypeDef(
    _RequiredUpdateFirewallPolicyRequestRequestTypeDef,
    _OptionalUpdateFirewallPolicyRequestRequestTypeDef,
):
    pass


RulesSourceOutputTypeDef = TypedDict(
    "RulesSourceOutputTypeDef",
    {
        "RulesString": str,
        "RulesSourceList": RulesSourceListOutputTypeDef,
        "StatefulRules": List[StatefulRuleOutputTypeDef],
        "StatelessRulesAndCustomActions": StatelessRulesAndCustomActionsOutputTypeDef,
    },
    total=False,
)

RulesSourceTypeDef = TypedDict(
    "RulesSourceTypeDef",
    {
        "RulesString": str,
        "RulesSourceList": RulesSourceListTypeDef,
        "StatefulRules": Sequence[StatefulRuleTypeDef],
        "StatelessRulesAndCustomActions": StatelessRulesAndCustomActionsTypeDef,
    },
    total=False,
)

_RequiredRuleGroupOutputTypeDef = TypedDict(
    "_RequiredRuleGroupOutputTypeDef",
    {
        "RulesSource": RulesSourceOutputTypeDef,
    },
)
_OptionalRuleGroupOutputTypeDef = TypedDict(
    "_OptionalRuleGroupOutputTypeDef",
    {
        "RuleVariables": RuleVariablesOutputTypeDef,
        "ReferenceSets": ReferenceSetsOutputTypeDef,
        "StatefulRuleOptions": StatefulRuleOptionsOutputTypeDef,
    },
    total=False,
)


class RuleGroupOutputTypeDef(_RequiredRuleGroupOutputTypeDef, _OptionalRuleGroupOutputTypeDef):
    pass


_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef",
    {
        "RulesSource": RulesSourceTypeDef,
    },
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef",
    {
        "RuleVariables": RuleVariablesTypeDef,
        "ReferenceSets": ReferenceSetsTypeDef,
        "StatefulRuleOptions": StatefulRuleOptionsTypeDef,
    },
    total=False,
)


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass


DescribeRuleGroupResponseTypeDef = TypedDict(
    "DescribeRuleGroupResponseTypeDef",
    {
        "UpdateToken": str,
        "RuleGroup": RuleGroupOutputTypeDef,
        "RuleGroupResponse": RuleGroupResponseTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupName": str,
        "Type": RuleGroupTypeType,
        "Capacity": int,
    },
)
_OptionalCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroup": RuleGroupTypeDef,
        "Rules": str,
        "Description": str,
        "Tags": Sequence[TagTypeDef],
        "DryRun": bool,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "SourceMetadata": SourceMetadataTypeDef,
    },
    total=False,
)


class CreateRuleGroupRequestRequestTypeDef(
    _RequiredCreateRuleGroupRequestRequestTypeDef, _OptionalCreateRuleGroupRequestRequestTypeDef
):
    pass


_RequiredUpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleGroupRequestRequestTypeDef",
    {
        "UpdateToken": str,
    },
)
_OptionalUpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupName": str,
        "RuleGroup": RuleGroupTypeDef,
        "Rules": str,
        "Type": RuleGroupTypeType,
        "Description": str,
        "DryRun": bool,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "SourceMetadata": SourceMetadataTypeDef,
    },
    total=False,
)


class UpdateRuleGroupRequestRequestTypeDef(
    _RequiredUpdateRuleGroupRequestRequestTypeDef, _OptionalUpdateRuleGroupRequestRequestTypeDef
):
    pass
