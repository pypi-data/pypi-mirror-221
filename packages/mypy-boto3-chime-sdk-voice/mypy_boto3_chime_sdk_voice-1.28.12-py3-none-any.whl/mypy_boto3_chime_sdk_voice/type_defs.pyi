"""
Type annotations for chime-sdk-voice service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_voice.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AlexaSkillStatusType,
    CallingNameStatusType,
    CallLegTypeType,
    CapabilityType,
    ErrorCodeType,
    GeoMatchLevelType,
    NotificationTargetType,
    NumberSelectionBehaviorType,
    OrderedPhoneNumberStatusType,
    OriginationRouteProtocolType,
    PhoneNumberAssociationNameType,
    PhoneNumberOrderStatusType,
    PhoneNumberOrderTypeType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    SipRuleTriggerTypeType,
    VoiceConnectorAwsRegionType,
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
    "AddressTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    "PhoneNumberErrorTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "CallDetailsTypeDef",
    "CandidateAddressTypeDef",
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    "GeoMatchParamsTypeDef",
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "TagTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "CreateVoiceProfileRequestRequestTypeDef",
    "VoiceProfileTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationOutputTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DeletePhoneNumberRequestRequestTypeDef",
    "DeleteProxySessionRequestRequestTypeDef",
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    "DeleteSipRuleRequestRequestTypeDef",
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    "DeleteVoiceConnectorRequestRequestTypeDef",
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    "DeleteVoiceProfileDomainRequestRequestTypeDef",
    "DeleteVoiceProfileRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GeoMatchParamsOutputTypeDef",
    "VoiceConnectorSettingsOutputTypeDef",
    "GetPhoneNumberOrderRequestRequestTypeDef",
    "GetPhoneNumberRequestRequestTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "GetProxySessionRequestRequestTypeDef",
    "GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    "SipMediaApplicationAlexaSkillConfigurationOutputTypeDef",
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "SipMediaApplicationLoggingConfigurationOutputTypeDef",
    "GetSipMediaApplicationRequestRequestTypeDef",
    "GetSipRuleRequestRequestTypeDef",
    "GetSpeakerSearchTaskRequestRequestTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    "ProxyTypeDef",
    "GetVoiceConnectorRequestRequestTypeDef",
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    "TerminationHealthTypeDef",
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    "TerminationOutputTypeDef",
    "GetVoiceProfileDomainRequestRequestTypeDef",
    "GetVoiceProfileRequestRequestTypeDef",
    "GetVoiceToneAnalysisTaskRequestRequestTypeDef",
    "ListAvailableVoiceConnectorRegionsResponseTypeDef",
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListProxySessionsRequestRequestTypeDef",
    "ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef",
    "ListSipMediaApplicationsRequestRequestTypeDef",
    "ListSipRulesRequestListSipRulesPaginateTypeDef",
    "ListSipRulesRequestRequestTypeDef",
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    "PhoneNumberCountryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ListVoiceConnectorsRequestRequestTypeDef",
    "ListVoiceProfileDomainsRequestRequestTypeDef",
    "VoiceProfileDomainSummaryTypeDef",
    "ListVoiceProfilesRequestRequestTypeDef",
    "VoiceProfileSummaryTypeDef",
    "LoggingConfigurationTypeDef",
    "MediaInsightsConfigurationOutputTypeDef",
    "MediaInsightsConfigurationTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteOutputTypeDef",
    "OriginationRouteTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "SipMediaApplicationAlexaSkillConfigurationTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "PutVoiceConnectorProxyRequestRequestTypeDef",
    "TerminationTypeDef",
    "ResponseMetadataTypeDef",
    "RestorePhoneNumberRequestRequestTypeDef",
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "ServerSideEncryptionConfigurationOutputTypeDef",
    "SipMediaApplicationEndpointOutputTypeDef",
    "SipRuleTargetApplicationOutputTypeDef",
    "SpeakerSearchResultTypeDef",
    "StartSpeakerSearchTaskRequestRequestTypeDef",
    "StartVoiceToneAnalysisTaskRequestRequestTypeDef",
    "StopSpeakerSearchTaskRequestRequestTypeDef",
    "StopVoiceToneAnalysisTaskRequestRequestTypeDef",
    "StreamingNotificationTargetOutputTypeDef",
    "StreamingNotificationTargetTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    "UpdateProxySessionRequestRequestTypeDef",
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    "UpdateVoiceConnectorRequestRequestTypeDef",
    "UpdateVoiceProfileDomainRequestRequestTypeDef",
    "UpdateVoiceProfileRequestRequestTypeDef",
    "ValidateE911AddressRequestRequestTypeDef",
    "VoiceConnectorItemOutputTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    "VoiceToneAnalysisTaskTypeDef",
    "ValidateE911AddressResponseTypeDef",
    "CreateProxySessionRequestRequestTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "UpdateSipMediaApplicationCallResponseTypeDef",
    "UpdateSipMediaApplicationRequestRequestTypeDef",
    "CreateSipMediaApplicationRequestRequestTypeDef",
    "CreateVoiceConnectorRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateSipRuleRequestRequestTypeDef",
    "UpdateSipRuleRequestRequestTypeDef",
    "CreateVoiceConnectorGroupRequestRequestTypeDef",
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    "CreateVoiceConnectorResponseTypeDef",
    "GetVoiceConnectorResponseTypeDef",
    "ListVoiceConnectorsResponseTypeDef",
    "UpdateVoiceConnectorResponseTypeDef",
    "CreateVoiceProfileDomainRequestRequestTypeDef",
    "CreateVoiceProfileResponseTypeDef",
    "GetVoiceProfileResponseTypeDef",
    "UpdateVoiceProfileResponseTypeDef",
    "PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "EmergencyCallingConfigurationOutputTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    "PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorProxyResponseTypeDef",
    "PutVoiceConnectorProxyResponseTypeDef",
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    "GetVoiceConnectorTerminationResponseTypeDef",
    "PutVoiceConnectorTerminationResponseTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVoiceProfileDomainsResponseTypeDef",
    "ListVoiceProfilesResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "PhoneNumberOrderTypeDef",
    "OriginationOutputTypeDef",
    "OriginationTypeDef",
    "ProxySessionTypeDef",
    "PhoneNumberTypeDef",
    "PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    "PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    "VoiceProfileDomainTypeDef",
    "SipMediaApplicationTypeDef",
    "SipRuleTypeDef",
    "SpeakerSearchDetailsTypeDef",
    "StreamingConfigurationOutputTypeDef",
    "StreamingConfigurationTypeDef",
    "UpdateGlobalSettingsRequestRequestTypeDef",
    "VoiceConnectorGroupTypeDef",
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    "StartVoiceToneAnalysisTaskResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "GetVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    "CreateProxySessionResponseTypeDef",
    "GetProxySessionResponseTypeDef",
    "ListProxySessionsResponseTypeDef",
    "UpdateProxySessionResponseTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "CreateVoiceProfileDomainResponseTypeDef",
    "GetVoiceProfileDomainResponseTypeDef",
    "UpdateVoiceProfileDomainResponseTypeDef",
    "CreateSipMediaApplicationResponseTypeDef",
    "GetSipMediaApplicationResponseTypeDef",
    "ListSipMediaApplicationsResponseTypeDef",
    "UpdateSipMediaApplicationResponseTypeDef",
    "CreateSipRuleResponseTypeDef",
    "GetSipRuleResponseTypeDef",
    "ListSipRulesResponseTypeDef",
    "UpdateSipRuleResponseTypeDef",
    "SpeakerSearchTaskTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "CreateVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorGroupResponseTypeDef",
    "ListVoiceConnectorGroupsResponseTypeDef",
    "UpdateVoiceConnectorGroupResponseTypeDef",
    "GetSpeakerSearchTaskResponseTypeDef",
    "StartSpeakerSearchTaskResponseTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "streetName": str,
        "streetSuffix": str,
        "postDirectional": str,
        "preDirectional": str,
        "streetNumber": str,
        "city": str,
        "state": str,
        "postalCode": str,
        "postalCodePlus4": str,
        "country": str,
    },
    total=False,
)

_RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": Sequence[str],
    },
)
_OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    {
        "ForceAssociate": bool,
    },
    total=False,
)

class AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef(
    _RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef,
    _OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef,
):
    pass

PhoneNumberErrorTypeDef = TypedDict(
    "PhoneNumberErrorTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": Sequence[str],
    },
)
_OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    {
        "ForceAssociate": bool,
    },
    total=False,
)

class AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef(
    _RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef,
    _OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef,
):
    pass

BatchDeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberIds": Sequence[str],
    },
)

_RequiredUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestItemTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestItemTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "CallingName": str,
    },
    total=False,
)

class UpdatePhoneNumberRequestItemTypeDef(
    _RequiredUpdatePhoneNumberRequestItemTypeDef, _OptionalUpdatePhoneNumberRequestItemTypeDef
):
    pass

CallDetailsTypeDef = TypedDict(
    "CallDetailsTypeDef",
    {
        "VoiceConnectorId": str,
        "TransactionId": str,
        "IsCaller": bool,
    },
    total=False,
)

CandidateAddressTypeDef = TypedDict(
    "CandidateAddressTypeDef",
    {
        "streetInfo": str,
        "streetNumber": str,
        "city": str,
        "state": str,
        "postalCode": str,
        "postalCodePlus4": str,
        "country": str,
    },
    total=False,
)

CreatePhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "E164PhoneNumbers": Sequence[str],
    },
)

GeoMatchParamsTypeDef = TypedDict(
    "GeoMatchParamsTypeDef",
    {
        "Country": str,
        "AreaCode": str,
    },
)

_RequiredCreateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "SipMediaApplicationId": str,
    },
)
_OptionalCreateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "SipHeaders": Mapping[str, str],
        "ArgumentsMap": Mapping[str, str],
    },
    total=False,
)

class CreateSipMediaApplicationCallRequestRequestTypeDef(
    _RequiredCreateSipMediaApplicationCallRequestRequestTypeDef,
    _OptionalCreateSipMediaApplicationCallRequestRequestTypeDef,
):
    pass

SipMediaApplicationCallTypeDef = TypedDict(
    "SipMediaApplicationCallTypeDef",
    {
        "TransactionId": str,
    },
    total=False,
)

SipMediaApplicationEndpointTypeDef = TypedDict(
    "SipMediaApplicationEndpointTypeDef",
    {
        "LambdaArn": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SipRuleTargetApplicationTypeDef = TypedDict(
    "SipRuleTargetApplicationTypeDef",
    {
        "SipMediaApplicationId": str,
        "Priority": int,
        "AwsRegion": str,
    },
    total=False,
)

VoiceConnectorItemTypeDef = TypedDict(
    "VoiceConnectorItemTypeDef",
    {
        "VoiceConnectorId": str,
        "Priority": int,
    },
)

VoiceConnectorTypeDef = TypedDict(
    "VoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": VoiceConnectorAwsRegionType,
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "VoiceConnectorArn": str,
    },
    total=False,
)

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyArn": str,
    },
)

CreateVoiceProfileRequestRequestTypeDef = TypedDict(
    "CreateVoiceProfileRequestRequestTypeDef",
    {
        "SpeakerSearchTaskId": str,
    },
)

VoiceProfileTypeDef = TypedDict(
    "VoiceProfileTypeDef",
    {
        "VoiceProfileId": str,
        "VoiceProfileArn": str,
        "VoiceProfileDomainId": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
    },
    total=False,
)

CredentialTypeDef = TypedDict(
    "CredentialTypeDef",
    {
        "Username": str,
        "Password": str,
    },
    total=False,
)

_RequiredDNISEmergencyCallingConfigurationOutputTypeDef = TypedDict(
    "_RequiredDNISEmergencyCallingConfigurationOutputTypeDef",
    {
        "EmergencyPhoneNumber": str,
        "CallingCountry": str,
    },
)
_OptionalDNISEmergencyCallingConfigurationOutputTypeDef = TypedDict(
    "_OptionalDNISEmergencyCallingConfigurationOutputTypeDef",
    {
        "TestPhoneNumber": str,
    },
    total=False,
)

class DNISEmergencyCallingConfigurationOutputTypeDef(
    _RequiredDNISEmergencyCallingConfigurationOutputTypeDef,
    _OptionalDNISEmergencyCallingConfigurationOutputTypeDef,
):
    pass

_RequiredDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_RequiredDNISEmergencyCallingConfigurationTypeDef",
    {
        "EmergencyPhoneNumber": str,
        "CallingCountry": str,
    },
)
_OptionalDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_OptionalDNISEmergencyCallingConfigurationTypeDef",
    {
        "TestPhoneNumber": str,
    },
    total=False,
)

class DNISEmergencyCallingConfigurationTypeDef(
    _RequiredDNISEmergencyCallingConfigurationTypeDef,
    _OptionalDNISEmergencyCallingConfigurationTypeDef,
):
    pass

DeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "DeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

DeleteProxySessionRequestRequestTypeDef = TypedDict(
    "DeleteProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

DeleteSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

DeleteSipRuleRequestRequestTypeDef = TypedDict(
    "DeleteSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

DeleteVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Usernames": Sequence[str],
    },
)

DeleteVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "DeleteVoiceProfileDomainRequestRequestTypeDef",
    {
        "VoiceProfileDomainId": str,
    },
)

DeleteVoiceProfileRequestRequestTypeDef = TypedDict(
    "DeleteVoiceProfileRequestRequestTypeDef",
    {
        "VoiceProfileId": str,
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": Sequence[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": Sequence[str],
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GeoMatchParamsOutputTypeDef = TypedDict(
    "GeoMatchParamsOutputTypeDef",
    {
        "Country": str,
        "AreaCode": str,
    },
)

VoiceConnectorSettingsOutputTypeDef = TypedDict(
    "VoiceConnectorSettingsOutputTypeDef",
    {
        "CdrBucket": str,
    },
    total=False,
)

GetPhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberOrderRequestRequestTypeDef",
    {
        "PhoneNumberOrderId": str,
    },
)

GetPhoneNumberRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

GetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "GetPhoneNumberSettingsResponseTypeDef",
    {
        "CallingName": str,
        "CallingNameUpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProxySessionRequestRequestTypeDef = TypedDict(
    "GetProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

SipMediaApplicationAlexaSkillConfigurationOutputTypeDef = TypedDict(
    "SipMediaApplicationAlexaSkillConfigurationOutputTypeDef",
    {
        "AlexaSkillStatus": AlexaSkillStatusType,
        "AlexaSkillIds": List[str],
    },
)

GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

SipMediaApplicationLoggingConfigurationOutputTypeDef = TypedDict(
    "SipMediaApplicationLoggingConfigurationOutputTypeDef",
    {
        "EnableSipMediaApplicationMessageLogs": bool,
    },
    total=False,
)

GetSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipRuleRequestRequestTypeDef = TypedDict(
    "GetSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

GetSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "GetSpeakerSearchTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "SpeakerSearchTaskId": str,
    },
)

GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

LoggingConfigurationOutputTypeDef = TypedDict(
    "LoggingConfigurationOutputTypeDef",
    {
        "EnableSIPLogs": bool,
        "EnableMediaMetricLogs": bool,
    },
    total=False,
)

GetVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

ProxyTypeDef = TypedDict(
    "ProxyTypeDef",
    {
        "DefaultSessionExpiryMinutes": int,
        "Disabled": bool,
        "FallBackPhoneNumber": str,
        "PhoneNumberCountries": List[str],
    },
    total=False,
)

GetVoiceConnectorRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationHealthRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

TerminationHealthTypeDef = TypedDict(
    "TerminationHealthTypeDef",
    {
        "Timestamp": datetime,
        "Source": str,
    },
    total=False,
)

GetVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

TerminationOutputTypeDef = TypedDict(
    "TerminationOutputTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)

GetVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "GetVoiceProfileDomainRequestRequestTypeDef",
    {
        "VoiceProfileDomainId": str,
    },
)

GetVoiceProfileRequestRequestTypeDef = TypedDict(
    "GetVoiceProfileRequestRequestTypeDef",
    {
        "VoiceProfileId": str,
    },
)

GetVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "GetVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "VoiceToneAnalysisTaskId": str,
        "IsCaller": bool,
    },
)

ListAvailableVoiceConnectorRegionsResponseTypeDef = TypedDict(
    "ListAvailableVoiceConnectorRegionsResponseTypeDef",
    {
        "VoiceConnectorRegions": List[VoiceConnectorAwsRegionType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumberOrdersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumbersRequestRequestTypeDef",
    {
        "Status": str,
        "ProductType": PhoneNumberProductTypeType,
        "FilterName": PhoneNumberAssociationNameType,
        "FilterValue": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListProxySessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListProxySessionsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
_OptionalListProxySessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListProxySessionsRequestRequestTypeDef",
    {
        "Status": ProxySessionStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListProxySessionsRequestRequestTypeDef(
    _RequiredListProxySessionsRequestRequestTypeDef, _OptionalListProxySessionsRequestRequestTypeDef
):
    pass

ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef = TypedDict(
    "ListSipMediaApplicationsRequestListSipMediaApplicationsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSipMediaApplicationsRequestRequestTypeDef = TypedDict(
    "ListSipMediaApplicationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSipRulesRequestListSipRulesPaginateTypeDef = TypedDict(
    "ListSipRulesRequestListSipRulesPaginateTypeDef",
    {
        "SipMediaApplicationId": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSipRulesRequestRequestTypeDef = TypedDict(
    "ListSipRulesRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSupportedPhoneNumberCountriesRequestRequestTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
    },
)

PhoneNumberCountryTypeDef = TypedDict(
    "PhoneNumberCountryTypeDef",
    {
        "CountryCode": str,
        "SupportedPhoneNumberTypes": List[PhoneNumberTypeType],
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

ListVoiceConnectorGroupsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

ListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {
        "Usernames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListVoiceProfileDomainsRequestRequestTypeDef = TypedDict(
    "ListVoiceProfileDomainsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

VoiceProfileDomainSummaryTypeDef = TypedDict(
    "VoiceProfileDomainSummaryTypeDef",
    {
        "VoiceProfileDomainId": str,
        "VoiceProfileDomainArn": str,
        "Name": str,
        "Description": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredListVoiceProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListVoiceProfilesRequestRequestTypeDef",
    {
        "VoiceProfileDomainId": str,
    },
)
_OptionalListVoiceProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListVoiceProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListVoiceProfilesRequestRequestTypeDef(
    _RequiredListVoiceProfilesRequestRequestTypeDef, _OptionalListVoiceProfilesRequestRequestTypeDef
):
    pass

VoiceProfileSummaryTypeDef = TypedDict(
    "VoiceProfileSummaryTypeDef",
    {
        "VoiceProfileId": str,
        "VoiceProfileArn": str,
        "VoiceProfileDomainId": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "EnableSIPLogs": bool,
        "EnableMediaMetricLogs": bool,
    },
    total=False,
)

MediaInsightsConfigurationOutputTypeDef = TypedDict(
    "MediaInsightsConfigurationOutputTypeDef",
    {
        "Disabled": bool,
        "ConfigurationArn": str,
    },
    total=False,
)

MediaInsightsConfigurationTypeDef = TypedDict(
    "MediaInsightsConfigurationTypeDef",
    {
        "Disabled": bool,
        "ConfigurationArn": str,
    },
    total=False,
)

OrderedPhoneNumberTypeDef = TypedDict(
    "OrderedPhoneNumberTypeDef",
    {
        "E164PhoneNumber": str,
        "Status": OrderedPhoneNumberStatusType,
    },
    total=False,
)

OriginationRouteOutputTypeDef = TypedDict(
    "OriginationRouteOutputTypeDef",
    {
        "Host": str,
        "Port": int,
        "Protocol": OriginationRouteProtocolType,
        "Priority": int,
        "Weight": int,
    },
    total=False,
)

OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {
        "Host": str,
        "Port": int,
        "Protocol": OriginationRouteProtocolType,
        "Priority": int,
        "Weight": int,
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

ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "PhoneNumber": str,
        "ProxyPhoneNumber": str,
    },
    total=False,
)

PhoneNumberAssociationTypeDef = TypedDict(
    "PhoneNumberAssociationTypeDef",
    {
        "Value": str,
        "Name": PhoneNumberAssociationNameType,
        "AssociatedTimestamp": datetime,
    },
    total=False,
)

PhoneNumberCapabilitiesTypeDef = TypedDict(
    "PhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)

SipMediaApplicationAlexaSkillConfigurationTypeDef = TypedDict(
    "SipMediaApplicationAlexaSkillConfigurationTypeDef",
    {
        "AlexaSkillStatus": AlexaSkillStatusType,
        "AlexaSkillIds": Sequence[str],
    },
)

SipMediaApplicationLoggingConfigurationTypeDef = TypedDict(
    "SipMediaApplicationLoggingConfigurationTypeDef",
    {
        "EnableSipMediaApplicationMessageLogs": bool,
    },
    total=False,
)

_RequiredPutVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "_RequiredPutVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "DefaultSessionExpiryMinutes": int,
        "PhoneNumberPoolCountries": Sequence[str],
    },
)
_OptionalPutVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "_OptionalPutVoiceConnectorProxyRequestRequestTypeDef",
    {
        "FallBackPhoneNumber": str,
        "Disabled": bool,
    },
    total=False,
)

class PutVoiceConnectorProxyRequestRequestTypeDef(
    _RequiredPutVoiceConnectorProxyRequestRequestTypeDef,
    _OptionalPutVoiceConnectorProxyRequestRequestTypeDef,
):
    pass

TerminationTypeDef = TypedDict(
    "TerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": Sequence[str],
        "CidrAllowedList": Sequence[str],
        "Disabled": bool,
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

RestorePhoneNumberRequestRequestTypeDef = TypedDict(
    "RestorePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

SearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "AreaCode": str,
        "City": str,
        "Country": str,
        "State": str,
        "TollFreePrefix": str,
        "PhoneNumberType": PhoneNumberTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

SearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseTypeDef",
    {
        "E164PhoneNumbers": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServerSideEncryptionConfigurationOutputTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationOutputTypeDef",
    {
        "KmsKeyArn": str,
    },
)

SipMediaApplicationEndpointOutputTypeDef = TypedDict(
    "SipMediaApplicationEndpointOutputTypeDef",
    {
        "LambdaArn": str,
    },
    total=False,
)

SipRuleTargetApplicationOutputTypeDef = TypedDict(
    "SipRuleTargetApplicationOutputTypeDef",
    {
        "SipMediaApplicationId": str,
        "Priority": int,
        "AwsRegion": str,
    },
    total=False,
)

SpeakerSearchResultTypeDef = TypedDict(
    "SpeakerSearchResultTypeDef",
    {
        "ConfidenceScore": float,
        "VoiceProfileId": str,
    },
    total=False,
)

_RequiredStartSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartSpeakerSearchTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "TransactionId": str,
        "VoiceProfileDomainId": str,
    },
)
_OptionalStartSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartSpeakerSearchTaskRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "CallLeg": CallLegTypeType,
    },
    total=False,
)

class StartSpeakerSearchTaskRequestRequestTypeDef(
    _RequiredStartSpeakerSearchTaskRequestRequestTypeDef,
    _OptionalStartSpeakerSearchTaskRequestRequestTypeDef,
):
    pass

_RequiredStartVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "TransactionId": str,
        "LanguageCode": Literal["en-US"],
    },
)
_OptionalStartVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class StartVoiceToneAnalysisTaskRequestRequestTypeDef(
    _RequiredStartVoiceToneAnalysisTaskRequestRequestTypeDef,
    _OptionalStartVoiceToneAnalysisTaskRequestRequestTypeDef,
):
    pass

StopSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "StopSpeakerSearchTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "SpeakerSearchTaskId": str,
    },
)

StopVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "StopVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "VoiceToneAnalysisTaskId": str,
    },
)

StreamingNotificationTargetOutputTypeDef = TypedDict(
    "StreamingNotificationTargetOutputTypeDef",
    {
        "NotificationTarget": NotificationTargetType,
    },
    total=False,
)

StreamingNotificationTargetTypeDef = TypedDict(
    "StreamingNotificationTargetTypeDef",
    {
        "NotificationTarget": NotificationTargetType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

VoiceConnectorSettingsTypeDef = TypedDict(
    "VoiceConnectorSettingsTypeDef",
    {
        "CdrBucket": str,
    },
    total=False,
)

_RequiredUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "CallingName": str,
    },
    total=False,
)

class UpdatePhoneNumberRequestRequestTypeDef(
    _RequiredUpdatePhoneNumberRequestRequestTypeDef, _OptionalUpdatePhoneNumberRequestRequestTypeDef
):
    pass

UpdatePhoneNumberSettingsRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    {
        "CallingName": str,
    },
)

_RequiredUpdateProxySessionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Capabilities": Sequence[CapabilityType],
    },
)
_OptionalUpdateProxySessionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProxySessionRequestRequestTypeDef",
    {
        "ExpiryMinutes": int,
    },
    total=False,
)

class UpdateProxySessionRequestRequestTypeDef(
    _RequiredUpdateProxySessionRequestRequestTypeDef,
    _OptionalUpdateProxySessionRequestRequestTypeDef,
):
    pass

UpdateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "TransactionId": str,
        "Arguments": Mapping[str, str],
    },
)

UpdateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Name": str,
        "RequireEncryption": bool,
    },
)

_RequiredUpdateVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVoiceProfileDomainRequestRequestTypeDef",
    {
        "VoiceProfileDomainId": str,
    },
)
_OptionalUpdateVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVoiceProfileDomainRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateVoiceProfileDomainRequestRequestTypeDef(
    _RequiredUpdateVoiceProfileDomainRequestRequestTypeDef,
    _OptionalUpdateVoiceProfileDomainRequestRequestTypeDef,
):
    pass

UpdateVoiceProfileRequestRequestTypeDef = TypedDict(
    "UpdateVoiceProfileRequestRequestTypeDef",
    {
        "VoiceProfileId": str,
        "SpeakerSearchTaskId": str,
    },
)

ValidateE911AddressRequestRequestTypeDef = TypedDict(
    "ValidateE911AddressRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "StreetNumber": str,
        "StreetInfo": str,
        "City": str,
        "State": str,
        "Country": str,
        "PostalCode": str,
    },
)

VoiceConnectorItemOutputTypeDef = TypedDict(
    "VoiceConnectorItemOutputTypeDef",
    {
        "VoiceConnectorId": str,
        "Priority": int,
    },
)

AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "BatchDeletePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "BatchUpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List[PhoneNumberErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    {
        "UpdatePhoneNumberRequestItems": Sequence[UpdatePhoneNumberRequestItemTypeDef],
    },
)

VoiceToneAnalysisTaskTypeDef = TypedDict(
    "VoiceToneAnalysisTaskTypeDef",
    {
        "VoiceToneAnalysisTaskId": str,
        "VoiceToneAnalysisTaskStatus": str,
        "CallDetails": CallDetailsTypeDef,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "StartedTimestamp": datetime,
        "StatusMessage": str,
    },
    total=False,
)

ValidateE911AddressResponseTypeDef = TypedDict(
    "ValidateE911AddressResponseTypeDef",
    {
        "ValidationResult": int,
        "AddressExternalId": str,
        "Address": AddressTypeDef,
        "CandidateAddressList": List[CandidateAddressTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProxySessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ParticipantPhoneNumbers": Sequence[str],
        "Capabilities": Sequence[CapabilityType],
    },
)
_OptionalCreateProxySessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProxySessionRequestRequestTypeDef",
    {
        "Name": str,
        "ExpiryMinutes": int,
        "NumberSelectionBehavior": NumberSelectionBehaviorType,
        "GeoMatchLevel": GeoMatchLevelType,
        "GeoMatchParams": GeoMatchParamsTypeDef,
    },
    total=False,
)

class CreateProxySessionRequestRequestTypeDef(
    _RequiredCreateProxySessionRequestRequestTypeDef,
    _OptionalCreateProxySessionRequestRequestTypeDef,
):
    pass

CreateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": SipMediaApplicationCallTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": SipMediaApplicationCallTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalUpdateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSipMediaApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Endpoints": Sequence[SipMediaApplicationEndpointTypeDef],
    },
    total=False,
)

class UpdateSipMediaApplicationRequestRequestTypeDef(
    _RequiredUpdateSipMediaApplicationRequestRequestTypeDef,
    _OptionalUpdateSipMediaApplicationRequestRequestTypeDef,
):
    pass

_RequiredCreateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSipMediaApplicationRequestRequestTypeDef",
    {
        "AwsRegion": str,
        "Name": str,
        "Endpoints": Sequence[SipMediaApplicationEndpointTypeDef],
    },
)
_OptionalCreateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSipMediaApplicationRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateSipMediaApplicationRequestRequestTypeDef(
    _RequiredCreateSipMediaApplicationRequestRequestTypeDef,
    _OptionalCreateSipMediaApplicationRequestRequestTypeDef,
):
    pass

_RequiredCreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceConnectorRequestRequestTypeDef",
    {
        "Name": str,
        "RequireEncryption": bool,
    },
)
_OptionalCreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceConnectorRequestRequestTypeDef",
    {
        "AwsRegion": VoiceConnectorAwsRegionType,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateVoiceConnectorRequestRequestTypeDef(
    _RequiredCreateVoiceConnectorRequestRequestTypeDef,
    _OptionalCreateVoiceConnectorRequestRequestTypeDef,
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredCreateSipRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSipRuleRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
    },
)
_OptionalCreateSipRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSipRuleRequestRequestTypeDef",
    {
        "Disabled": bool,
        "TargetApplications": Sequence[SipRuleTargetApplicationTypeDef],
    },
    total=False,
)

class CreateSipRuleRequestRequestTypeDef(
    _RequiredCreateSipRuleRequestRequestTypeDef, _OptionalCreateSipRuleRequestRequestTypeDef
):
    pass

_RequiredUpdateSipRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
    },
)
_OptionalUpdateSipRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSipRuleRequestRequestTypeDef",
    {
        "Disabled": bool,
        "TargetApplications": Sequence[SipRuleTargetApplicationTypeDef],
    },
    total=False,
)

class UpdateSipRuleRequestRequestTypeDef(
    _RequiredUpdateSipRuleRequestRequestTypeDef, _OptionalUpdateSipRuleRequestRequestTypeDef
):
    pass

_RequiredCreateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorItems": Sequence[VoiceConnectorItemTypeDef],
    },
    total=False,
)

class CreateVoiceConnectorGroupRequestRequestTypeDef(
    _RequiredCreateVoiceConnectorGroupRequestRequestTypeDef,
    _OptionalCreateVoiceConnectorGroupRequestRequestTypeDef,
):
    pass

UpdateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": Sequence[VoiceConnectorItemTypeDef],
    },
)

CreateVoiceConnectorResponseTypeDef = TypedDict(
    "CreateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": VoiceConnectorTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorResponseTypeDef = TypedDict(
    "GetVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": VoiceConnectorTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorsResponseTypeDef = TypedDict(
    "ListVoiceConnectorsResponseTypeDef",
    {
        "VoiceConnectors": List[VoiceConnectorTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceConnectorResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": VoiceConnectorTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceProfileDomainRequestRequestTypeDef",
    {
        "Name": str,
        "ServerSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
    },
)
_OptionalCreateVoiceProfileDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceProfileDomainRequestRequestTypeDef",
    {
        "Description": str,
        "ClientRequestToken": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateVoiceProfileDomainRequestRequestTypeDef(
    _RequiredCreateVoiceProfileDomainRequestRequestTypeDef,
    _OptionalCreateVoiceProfileDomainRequestRequestTypeDef,
):
    pass

CreateVoiceProfileResponseTypeDef = TypedDict(
    "CreateVoiceProfileResponseTypeDef",
    {
        "VoiceProfile": VoiceProfileTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceProfileResponseTypeDef = TypedDict(
    "GetVoiceProfileResponseTypeDef",
    {
        "VoiceProfile": VoiceProfileTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceProfileResponseTypeDef = TypedDict(
    "UpdateVoiceProfileResponseTypeDef",
    {
        "VoiceProfile": VoiceProfileTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
_OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "Credentials": Sequence[CredentialTypeDef],
    },
    total=False,
)

class PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef(
    _RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef,
    _OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef,
):
    pass

EmergencyCallingConfigurationOutputTypeDef = TypedDict(
    "EmergencyCallingConfigurationOutputTypeDef",
    {
        "DNIS": List[DNISEmergencyCallingConfigurationOutputTypeDef],
    },
    total=False,
)

EmergencyCallingConfigurationTypeDef = TypedDict(
    "EmergencyCallingConfigurationTypeDef",
    {
        "DNIS": Sequence[DNISEmergencyCallingConfigurationTypeDef],
    },
    total=False,
)

GetGlobalSettingsResponseTypeDef = TypedDict(
    "GetGlobalSettingsResponseTypeDef",
    {
        "VoiceConnector": VoiceConnectorSettingsOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    {
        "SipMediaApplicationAlexaSkillConfiguration": (
            SipMediaApplicationAlexaSkillConfigurationOutputTypeDef
        ),
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    {
        "SipMediaApplicationAlexaSkillConfiguration": (
            SipMediaApplicationAlexaSkillConfigurationOutputTypeDef
        ),
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": (
            SipMediaApplicationLoggingConfigurationOutputTypeDef
        ),
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": (
            SipMediaApplicationLoggingConfigurationOutputTypeDef
        ),
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": LoggingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorProxyResponseTypeDef = TypedDict(
    "GetVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": ProxyTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorProxyResponseTypeDef = TypedDict(
    "PutVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": ProxyTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    {
        "TerminationHealth": TerminationHealthTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": TerminationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "PutVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": TerminationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSupportedPhoneNumberCountriesResponseTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    {
        "PhoneNumberCountries": List[PhoneNumberCountryTypeDef],
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

ListVoiceProfileDomainsResponseTypeDef = TypedDict(
    "ListVoiceProfileDomainsResponseTypeDef",
    {
        "VoiceProfileDomains": List[VoiceProfileDomainSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceProfilesResponseTypeDef = TypedDict(
    "ListVoiceProfilesResponseTypeDef",
    {
        "VoiceProfiles": List[VoiceProfileSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "LoggingConfiguration": LoggingConfigurationTypeDef,
    },
)

PhoneNumberOrderTypeDef = TypedDict(
    "PhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": PhoneNumberProductTypeType,
        "Status": PhoneNumberOrderStatusType,
        "OrderType": PhoneNumberOrderTypeType,
        "OrderedPhoneNumbers": List[OrderedPhoneNumberTypeDef],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

OriginationOutputTypeDef = TypedDict(
    "OriginationOutputTypeDef",
    {
        "Routes": List[OriginationRouteOutputTypeDef],
        "Disabled": bool,
    },
    total=False,
)

OriginationTypeDef = TypedDict(
    "OriginationTypeDef",
    {
        "Routes": Sequence[OriginationRouteTypeDef],
        "Disabled": bool,
    },
    total=False,
)

ProxySessionTypeDef = TypedDict(
    "ProxySessionTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Name": str,
        "Status": ProxySessionStatusType,
        "ExpiryMinutes": int,
        "Capabilities": List[CapabilityType],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "EndedTimestamp": datetime,
        "Participants": List[ParticipantTypeDef],
        "NumberSelectionBehavior": NumberSelectionBehaviorType,
        "GeoMatchLevel": GeoMatchLevelType,
        "GeoMatchParams": GeoMatchParamsOutputTypeDef,
    },
    total=False,
)

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Country": str,
        "Type": PhoneNumberTypeType,
        "ProductType": PhoneNumberProductTypeType,
        "Status": PhoneNumberStatusType,
        "Capabilities": PhoneNumberCapabilitiesTypeDef,
        "Associations": List[PhoneNumberAssociationTypeDef],
        "CallingName": str,
        "CallingNameStatus": CallingNameStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
        "OrderId": str,
    },
    total=False,
)

_RequiredPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationAlexaSkillConfiguration": (
            SipMediaApplicationAlexaSkillConfigurationTypeDef
        ),
    },
    total=False,
)

class PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef(
    _RequiredPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef,
    _OptionalPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef,
):
    pass

_RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": SipMediaApplicationLoggingConfigurationTypeDef,
    },
    total=False,
)

class PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(
    _RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef,
    _OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef,
):
    pass

PutVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Termination": TerminationTypeDef,
    },
)

VoiceProfileDomainTypeDef = TypedDict(
    "VoiceProfileDomainTypeDef",
    {
        "VoiceProfileDomainId": str,
        "VoiceProfileDomainArn": str,
        "Name": str,
        "Description": str,
        "ServerSideEncryptionConfiguration": ServerSideEncryptionConfigurationOutputTypeDef,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

SipMediaApplicationTypeDef = TypedDict(
    "SipMediaApplicationTypeDef",
    {
        "SipMediaApplicationId": str,
        "AwsRegion": str,
        "Name": str,
        "Endpoints": List[SipMediaApplicationEndpointOutputTypeDef],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "SipMediaApplicationArn": str,
    },
    total=False,
)

SipRuleTypeDef = TypedDict(
    "SipRuleTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
        "Disabled": bool,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "TargetApplications": List[SipRuleTargetApplicationOutputTypeDef],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

SpeakerSearchDetailsTypeDef = TypedDict(
    "SpeakerSearchDetailsTypeDef",
    {
        "Results": List[SpeakerSearchResultTypeDef],
        "VoiceprintGenerationStatus": str,
    },
    total=False,
)

_RequiredStreamingConfigurationOutputTypeDef = TypedDict(
    "_RequiredStreamingConfigurationOutputTypeDef",
    {
        "DataRetentionInHours": int,
        "Disabled": bool,
    },
)
_OptionalStreamingConfigurationOutputTypeDef = TypedDict(
    "_OptionalStreamingConfigurationOutputTypeDef",
    {
        "StreamingNotificationTargets": List[StreamingNotificationTargetOutputTypeDef],
        "MediaInsightsConfiguration": MediaInsightsConfigurationOutputTypeDef,
    },
    total=False,
)

class StreamingConfigurationOutputTypeDef(
    _RequiredStreamingConfigurationOutputTypeDef, _OptionalStreamingConfigurationOutputTypeDef
):
    pass

_RequiredStreamingConfigurationTypeDef = TypedDict(
    "_RequiredStreamingConfigurationTypeDef",
    {
        "DataRetentionInHours": int,
        "Disabled": bool,
    },
)
_OptionalStreamingConfigurationTypeDef = TypedDict(
    "_OptionalStreamingConfigurationTypeDef",
    {
        "StreamingNotificationTargets": Sequence[StreamingNotificationTargetTypeDef],
        "MediaInsightsConfiguration": MediaInsightsConfigurationTypeDef,
    },
    total=False,
)

class StreamingConfigurationTypeDef(
    _RequiredStreamingConfigurationTypeDef, _OptionalStreamingConfigurationTypeDef
):
    pass

UpdateGlobalSettingsRequestRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsRequestRequestTypeDef",
    {
        "VoiceConnector": VoiceConnectorSettingsTypeDef,
    },
    total=False,
)

VoiceConnectorGroupTypeDef = TypedDict(
    "VoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List[VoiceConnectorItemOutputTypeDef],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "VoiceConnectorGroupArn": str,
    },
    total=False,
)

GetVoiceToneAnalysisTaskResponseTypeDef = TypedDict(
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    {
        "VoiceToneAnalysisTask": VoiceToneAnalysisTaskTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartVoiceToneAnalysisTaskResponseTypeDef = TypedDict(
    "StartVoiceToneAnalysisTaskResponseTypeDef",
    {
        "VoiceToneAnalysisTask": VoiceToneAnalysisTaskTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": EmergencyCallingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": EmergencyCallingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "EmergencyCallingConfiguration": EmergencyCallingConfigurationTypeDef,
    },
)

CreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "CreatePhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": PhoneNumberOrderTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberOrderResponseTypeDef = TypedDict(
    "GetPhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": PhoneNumberOrderTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "ListPhoneNumberOrdersResponseTypeDef",
    {
        "PhoneNumberOrders": List[PhoneNumberOrderTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "GetVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": OriginationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "PutVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": OriginationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Origination": OriginationTypeDef,
    },
)

CreateProxySessionResponseTypeDef = TypedDict(
    "CreateProxySessionResponseTypeDef",
    {
        "ProxySession": ProxySessionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProxySessionResponseTypeDef = TypedDict(
    "GetProxySessionResponseTypeDef",
    {
        "ProxySession": ProxySessionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProxySessionsResponseTypeDef = TypedDict(
    "ListProxySessionsResponseTypeDef",
    {
        "ProxySessions": List[ProxySessionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProxySessionResponseTypeDef = TypedDict(
    "UpdateProxySessionResponseTypeDef",
    {
        "ProxySession": ProxySessionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberResponseTypeDef = TypedDict(
    "GetPhoneNumberResponseTypeDef",
    {
        "PhoneNumber": PhoneNumberTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumbers": List[PhoneNumberTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestorePhoneNumberResponseTypeDef = TypedDict(
    "RestorePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": PhoneNumberTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePhoneNumberResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": PhoneNumberTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVoiceProfileDomainResponseTypeDef = TypedDict(
    "CreateVoiceProfileDomainResponseTypeDef",
    {
        "VoiceProfileDomain": VoiceProfileDomainTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceProfileDomainResponseTypeDef = TypedDict(
    "GetVoiceProfileDomainResponseTypeDef",
    {
        "VoiceProfileDomain": VoiceProfileDomainTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceProfileDomainResponseTypeDef = TypedDict(
    "UpdateVoiceProfileDomainResponseTypeDef",
    {
        "VoiceProfileDomain": VoiceProfileDomainTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipMediaApplicationResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": SipMediaApplicationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": SipMediaApplicationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipMediaApplicationsResponseTypeDef = TypedDict(
    "ListSipMediaApplicationsResponseTypeDef",
    {
        "SipMediaApplications": List[SipMediaApplicationTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipMediaApplicationResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": SipMediaApplicationTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipRuleResponseTypeDef = TypedDict(
    "CreateSipRuleResponseTypeDef",
    {
        "SipRule": SipRuleTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipRuleResponseTypeDef = TypedDict(
    "GetSipRuleResponseTypeDef",
    {
        "SipRule": SipRuleTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipRulesResponseTypeDef = TypedDict(
    "ListSipRulesResponseTypeDef",
    {
        "SipRules": List[SipRuleTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipRuleResponseTypeDef = TypedDict(
    "UpdateSipRuleResponseTypeDef",
    {
        "SipRule": SipRuleTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SpeakerSearchTaskTypeDef = TypedDict(
    "SpeakerSearchTaskTypeDef",
    {
        "SpeakerSearchTaskId": str,
        "SpeakerSearchTaskStatus": str,
        "CallDetails": CallDetailsTypeDef,
        "SpeakerSearchDetails": SpeakerSearchDetailsTypeDef,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "StartedTimestamp": datetime,
        "StatusMessage": str,
    },
    total=False,
)

GetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": StreamingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": StreamingConfigurationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "StreamingConfiguration": StreamingConfigurationTypeDef,
    },
)

CreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "CreateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": VoiceConnectorGroupTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "GetVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": VoiceConnectorGroupTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "ListVoiceConnectorGroupsResponseTypeDef",
    {
        "VoiceConnectorGroups": List[VoiceConnectorGroupTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": VoiceConnectorGroupTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSpeakerSearchTaskResponseTypeDef = TypedDict(
    "GetSpeakerSearchTaskResponseTypeDef",
    {
        "SpeakerSearchTask": SpeakerSearchTaskTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSpeakerSearchTaskResponseTypeDef = TypedDict(
    "StartSpeakerSearchTaskResponseTypeDef",
    {
        "SpeakerSearchTask": SpeakerSearchTaskTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
