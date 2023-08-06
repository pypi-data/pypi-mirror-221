"""
Type annotations for pinpoint-email service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/type_defs/)

Usage::

    ```python
    from mypy_boto3_pinpoint_email.type_defs import BlacklistEntryTypeDef

    data: BlacklistEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMxFailureType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DimensionValueSourceType,
    DkimStatusType,
    EventTypeType,
    IdentityTypeType,
    MailFromDomainStatusType,
    TlsPolicyType,
    WarmupStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BlacklistEntryTypeDef",
    "ContentTypeDef",
    "CloudWatchDimensionConfigurationOutputTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "DeliveryOptionsTypeDef",
    "ReputationOptionsTypeDef",
    "SendingOptionsTypeDef",
    "TagTypeDef",
    "TrackingOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "DkimAttributesTypeDef",
    "DomainIspPlacementTypeDef",
    "VolumeStatisticsTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    "DeleteEmailIdentityRequestRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsOutputTypeDef",
    "DestinationTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "InboxPlacementTrackingOptionOutputTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "RawMessageTypeDef",
    "TemplateTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "PinpointDestinationTypeDef",
    "SnsDestinationTypeDef",
    "KinesisFirehoseDestinationOutputTypeDef",
    "PinpointDestinationOutputTypeDef",
    "SnsDestinationOutputTypeDef",
    "SendQuotaTypeDef",
    "GetBlacklistReportsRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "GetConfigurationSetRequestRequestTypeDef",
    "ReputationOptionsOutputTypeDef",
    "SendingOptionsOutputTypeDef",
    "TagOutputTypeDef",
    "TrackingOptionsOutputTypeDef",
    "GetDedicatedIpRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetDedicatedIpsRequestRequestTypeDef",
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    "PlacementStatisticsTypeDef",
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    "GetDomainStatisticsReportRequestRequestTypeDef",
    "GetEmailIdentityRequestRequestTypeDef",
    "MailFromAttributesTypeDef",
    "IdentityInfoTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    "ListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    "ListEmailIdentitiesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MessageTagTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutAccountSendingAttributesRequestRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BodyTypeDef",
    "CloudWatchDestinationOutputTypeDef",
    "CloudWatchDestinationTypeDef",
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    "CreateEmailIdentityRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "SendEmailResponseTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "DailyVolumeTypeDef",
    "OverallVolumeTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "DomainDeliverabilityTrackingOptionOutputTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "GetAccountResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef",
    "ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef",
    "ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef",
    "ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef",
    "ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef",
    "IspPlacementTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "MessageTypeDef",
    "EventDestinationTypeDef",
    "EventDestinationDefinitionTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "EmailContentTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "CreateDeliverabilityTestReportRequestRequestTypeDef",
    "SendEmailRequestRequestTypeDef",
)

BlacklistEntryTypeDef = TypedDict(
    "BlacklistEntryTypeDef",
    {
        "RblName": str,
        "ListingTime": datetime,
        "Description": str,
    },
    total=False,
)

_RequiredContentTypeDef = TypedDict(
    "_RequiredContentTypeDef",
    {
        "Data": str,
    },
)
_OptionalContentTypeDef = TypedDict(
    "_OptionalContentTypeDef",
    {
        "Charset": str,
    },
    total=False,
)

class ContentTypeDef(_RequiredContentTypeDef, _OptionalContentTypeDef):
    pass

CloudWatchDimensionConfigurationOutputTypeDef = TypedDict(
    "CloudWatchDimensionConfigurationOutputTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": DimensionValueSourceType,
        "DefaultDimensionValue": str,
    },
)

CloudWatchDimensionConfigurationTypeDef = TypedDict(
    "CloudWatchDimensionConfigurationTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": DimensionValueSourceType,
        "DefaultDimensionValue": str,
    },
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
        "SendingPoolName": str,
    },
    total=False,
)

ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "ReputationMetricsEnabled": bool,
        "LastFreshStart": Union[datetime, str],
    },
    total=False,
)

SendingOptionsTypeDef = TypedDict(
    "SendingOptionsTypeDef",
    {
        "SendingEnabled": bool,
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

TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": str,
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

DkimAttributesTypeDef = TypedDict(
    "DkimAttributesTypeDef",
    {
        "SigningEnabled": bool,
        "Status": DkimStatusType,
        "Tokens": List[str],
    },
    total=False,
)

DomainIspPlacementTypeDef = TypedDict(
    "DomainIspPlacementTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)

VolumeStatisticsTypeDef = TypedDict(
    "VolumeStatisticsTypeDef",
    {
        "InboxRawCount": int,
        "SpamRawCount": int,
        "ProjectedInbox": int,
        "ProjectedSpam": int,
    },
    total=False,
)

_RequiredDedicatedIpTypeDef = TypedDict(
    "_RequiredDedicatedIpTypeDef",
    {
        "Ip": str,
        "WarmupStatus": WarmupStatusType,
        "WarmupPercentage": int,
    },
)
_OptionalDedicatedIpTypeDef = TypedDict(
    "_OptionalDedicatedIpTypeDef",
    {
        "PoolName": str,
    },
    total=False,
)

class DedicatedIpTypeDef(_RequiredDedicatedIpTypeDef, _OptionalDedicatedIpTypeDef):
    pass

DeleteConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)

DeleteEmailIdentityRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

DeliverabilityTestReportTypeDef = TypedDict(
    "DeliverabilityTestReportTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": DeliverabilityTestStatusType,
    },
    total=False,
)

DeliveryOptionsOutputTypeDef = TypedDict(
    "DeliveryOptionsOutputTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
        "SendingPoolName": str,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "ToAddresses": Sequence[str],
        "CcAddresses": Sequence[str],
        "BccAddresses": Sequence[str],
    },
    total=False,
)

DomainDeliverabilityCampaignTypeDef = TypedDict(
    "DomainDeliverabilityCampaignTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)

InboxPlacementTrackingOptionOutputTypeDef = TypedDict(
    "InboxPlacementTrackingOptionOutputTypeDef",
    {
        "Global": bool,
        "TrackedIsps": List[str],
    },
    total=False,
)

InboxPlacementTrackingOptionTypeDef = TypedDict(
    "InboxPlacementTrackingOptionTypeDef",
    {
        "Global": bool,
        "TrackedIsps": Sequence[str],
    },
    total=False,
)

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[str, bytes, IO[Any], StreamingBody],
    },
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "TemplateArn": str,
        "TemplateData": str,
    },
    total=False,
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)

PinpointDestinationTypeDef = TypedDict(
    "PinpointDestinationTypeDef",
    {
        "ApplicationArn": str,
    },
    total=False,
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
)

KinesisFirehoseDestinationOutputTypeDef = TypedDict(
    "KinesisFirehoseDestinationOutputTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)

PinpointDestinationOutputTypeDef = TypedDict(
    "PinpointDestinationOutputTypeDef",
    {
        "ApplicationArn": str,
    },
    total=False,
)

SnsDestinationOutputTypeDef = TypedDict(
    "SnsDestinationOutputTypeDef",
    {
        "TopicArn": str,
    },
)

SendQuotaTypeDef = TypedDict(
    "SendQuotaTypeDef",
    {
        "Max24HourSend": float,
        "MaxSendRate": float,
        "SentLast24Hours": float,
    },
    total=False,
)

GetBlacklistReportsRequestRequestTypeDef = TypedDict(
    "GetBlacklistReportsRequestRequestTypeDef",
    {
        "BlacklistItemNames": Sequence[str],
    },
)

GetConfigurationSetEventDestinationsRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

ReputationOptionsOutputTypeDef = TypedDict(
    "ReputationOptionsOutputTypeDef",
    {
        "ReputationMetricsEnabled": bool,
        "LastFreshStart": datetime,
    },
    total=False,
)

SendingOptionsOutputTypeDef = TypedDict(
    "SendingOptionsOutputTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TrackingOptionsOutputTypeDef = TypedDict(
    "TrackingOptionsOutputTypeDef",
    {
        "CustomRedirectDomain": str,
    },
)

GetDedicatedIpRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpRequestRequestTypeDef",
    {
        "Ip": str,
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

GetDedicatedIpsRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpsRequestRequestTypeDef",
    {
        "PoolName": str,
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

GetDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    {
        "ReportId": str,
    },
)

PlacementStatisticsTypeDef = TypedDict(
    "PlacementStatisticsTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)

GetDomainDeliverabilityCampaignRequestRequestTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    {
        "CampaignId": str,
    },
)

GetDomainStatisticsReportRequestRequestTypeDef = TypedDict(
    "GetDomainStatisticsReportRequestRequestTypeDef",
    {
        "Domain": str,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
    },
)

GetEmailIdentityRequestRequestTypeDef = TypedDict(
    "GetEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

MailFromAttributesTypeDef = TypedDict(
    "MailFromAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": MailFromDomainStatusType,
        "BehaviorOnMxFailure": BehaviorOnMxFailureType,
    },
)

IdentityInfoTypeDef = TypedDict(
    "IdentityInfoTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "IdentityName": str,
        "SendingEnabled": bool,
    },
    total=False,
)

ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListDedicatedIpPoolsRequestRequestTypeDef = TypedDict(
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListDeliverabilityTestReportsRequestRequestTypeDef = TypedDict(
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

_RequiredListDomainDeliverabilityCampaignsRequestRequestTypeDef = TypedDict(
    "_RequiredListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    {
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "SubscribedDomain": str,
    },
)
_OptionalListDomainDeliverabilityCampaignsRequestRequestTypeDef = TypedDict(
    "_OptionalListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

class ListDomainDeliverabilityCampaignsRequestRequestTypeDef(
    _RequiredListDomainDeliverabilityCampaignsRequestRequestTypeDef,
    _OptionalListDomainDeliverabilityCampaignsRequestRequestTypeDef,
):
    pass

ListEmailIdentitiesRequestRequestTypeDef = TypedDict(
    "ListEmailIdentitiesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

MessageTagTypeDef = TypedDict(
    "MessageTagTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "AutoWarmupEnabled": bool,
    },
    total=False,
)

PutAccountSendingAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSendingAttributesRequestRequestTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)

_RequiredPutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
        "SendingPoolName": str,
    },
    total=False,
)

class PutConfigurationSetDeliveryOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetDeliveryOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetDeliveryOptionsRequestRequestTypeDef,
):
    pass

_RequiredPutConfigurationSetReputationOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetReputationOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetReputationOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetReputationOptionsRequestRequestTypeDef",
    {
        "ReputationMetricsEnabled": bool,
    },
    total=False,
)

class PutConfigurationSetReputationOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetReputationOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetReputationOptionsRequestRequestTypeDef,
):
    pass

_RequiredPutConfigurationSetSendingOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetSendingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetSendingOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetSendingOptionsRequestRequestTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)

class PutConfigurationSetSendingOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetSendingOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetSendingOptionsRequestRequestTypeDef,
):
    pass

_RequiredPutConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "CustomRedirectDomain": str,
    },
    total=False,
)

class PutConfigurationSetTrackingOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetTrackingOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetTrackingOptionsRequestRequestTypeDef,
):
    pass

PutDedicatedIpInPoolRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    {
        "Ip": str,
        "DestinationPoolName": str,
    },
)

PutDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "Ip": str,
        "WarmupPercentage": int,
    },
)

_RequiredPutEmailIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityDkimAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityDkimAttributesRequestRequestTypeDef",
    {
        "SigningEnabled": bool,
    },
    total=False,
)

class PutEmailIdentityDkimAttributesRequestRequestTypeDef(
    _RequiredPutEmailIdentityDkimAttributesRequestRequestTypeDef,
    _OptionalPutEmailIdentityDkimAttributesRequestRequestTypeDef,
):
    pass

_RequiredPutEmailIdentityFeedbackAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityFeedbackAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    {
        "EmailForwardingEnabled": bool,
    },
    total=False,
)

class PutEmailIdentityFeedbackAttributesRequestRequestTypeDef(
    _RequiredPutEmailIdentityFeedbackAttributesRequestRequestTypeDef,
    _OptionalPutEmailIdentityFeedbackAttributesRequestRequestTypeDef,
):
    pass

_RequiredPutEmailIdentityMailFromAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityMailFromAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    {
        "MailFromDomain": str,
        "BehaviorOnMxFailure": BehaviorOnMxFailureType,
    },
    total=False,
)

class PutEmailIdentityMailFromAttributesRequestRequestTypeDef(
    _RequiredPutEmailIdentityMailFromAttributesRequestRequestTypeDef,
    _OptionalPutEmailIdentityMailFromAttributesRequestRequestTypeDef,
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": ContentTypeDef,
        "Html": ContentTypeDef,
    },
    total=False,
)

CloudWatchDestinationOutputTypeDef = TypedDict(
    "CloudWatchDestinationOutputTypeDef",
    {
        "DimensionConfigurations": List[CloudWatchDimensionConfigurationOutputTypeDef],
    },
)

CloudWatchDestinationTypeDef = TypedDict(
    "CloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": Sequence[CloudWatchDimensionConfigurationTypeDef],
    },
)

_RequiredCreateDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)
_OptionalCreateDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDedicatedIpPoolRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateDedicatedIpPoolRequestRequestTypeDef(
    _RequiredCreateDedicatedIpPoolRequestRequestTypeDef,
    _OptionalCreateDedicatedIpPoolRequestRequestTypeDef,
):
    pass

_RequiredCreateEmailIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalCreateEmailIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEmailIdentityRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateEmailIdentityRequestRequestTypeDef(
    _RequiredCreateEmailIdentityRequestRequestTypeDef,
    _OptionalCreateEmailIdentityRequestRequestTypeDef,
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredCreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalCreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationSetRequestRequestTypeDef",
    {
        "TrackingOptions": TrackingOptionsTypeDef,
        "DeliveryOptions": DeliveryOptionsTypeDef,
        "ReputationOptions": ReputationOptionsTypeDef,
        "SendingOptions": SendingOptionsTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateConfigurationSetRequestRequestTypeDef(
    _RequiredCreateConfigurationSetRequestRequestTypeDef,
    _OptionalCreateConfigurationSetRequestRequestTypeDef,
):
    pass

CreateDeliverabilityTestReportResponseTypeDef = TypedDict(
    "CreateDeliverabilityTestReportResponseTypeDef",
    {
        "ReportId": str,
        "DeliverabilityTestStatus": DeliverabilityTestStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetBlacklistReportsResponseTypeDef = TypedDict(
    "GetBlacklistReportsResponseTypeDef",
    {
        "BlacklistReport": Dict[str, List[BlacklistEntryTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDedicatedIpPoolsResponseTypeDef = TypedDict(
    "ListDedicatedIpPoolsResponseTypeDef",
    {
        "DedicatedIpPools": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SendEmailResponseTypeDef = TypedDict(
    "SendEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateEmailIdentityResponseTypeDef = TypedDict(
    "CreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": DkimAttributesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DailyVolumeTypeDef = TypedDict(
    "DailyVolumeTypeDef",
    {
        "StartDate": datetime,
        "VolumeStatistics": VolumeStatisticsTypeDef,
        "DomainIspPlacements": List[DomainIspPlacementTypeDef],
    },
    total=False,
)

OverallVolumeTypeDef = TypedDict(
    "OverallVolumeTypeDef",
    {
        "VolumeStatistics": VolumeStatisticsTypeDef,
        "ReadRatePercent": float,
        "DomainIspPlacements": List[DomainIspPlacementTypeDef],
    },
    total=False,
)

GetDedicatedIpResponseTypeDef = TypedDict(
    "GetDedicatedIpResponseTypeDef",
    {
        "DedicatedIp": DedicatedIpTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDedicatedIpsResponseTypeDef = TypedDict(
    "GetDedicatedIpsResponseTypeDef",
    {
        "DedicatedIps": List[DedicatedIpTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "ListDeliverabilityTestReportsResponseTypeDef",
    {
        "DeliverabilityTestReports": List[DeliverabilityTestReportTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDomainDeliverabilityCampaignResponseTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    {
        "DomainDeliverabilityCampaign": DomainDeliverabilityCampaignTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    {
        "DomainDeliverabilityCampaigns": List[DomainDeliverabilityCampaignTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DomainDeliverabilityTrackingOptionOutputTypeDef = TypedDict(
    "DomainDeliverabilityTrackingOptionOutputTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": InboxPlacementTrackingOptionOutputTypeDef,
    },
    total=False,
)

DomainDeliverabilityTrackingOptionTypeDef = TypedDict(
    "DomainDeliverabilityTrackingOptionTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": Union[datetime, str],
        "InboxPlacementTrackingOption": InboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)

GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "SendQuota": SendQuotaTypeDef,
        "SendingEnabled": bool,
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetConfigurationSetResponseTypeDef = TypedDict(
    "GetConfigurationSetResponseTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": TrackingOptionsOutputTypeDef,
        "DeliveryOptions": DeliveryOptionsOutputTypeDef,
        "ReputationOptions": ReputationOptionsOutputTypeDef,
        "SendingOptions": SendingOptionsOutputTypeDef,
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef = TypedDict(
    "GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef",
    {
        "PoolName": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef = TypedDict(
    "ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef = TypedDict(
    "ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef = TypedDict(
    "ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef = TypedDict(
    "ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

IspPlacementTypeDef = TypedDict(
    "IspPlacementTypeDef",
    {
        "IspName": str,
        "PlacementStatistics": PlacementStatisticsTypeDef,
    },
    total=False,
)

GetEmailIdentityResponseTypeDef = TypedDict(
    "GetEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": DkimAttributesTypeDef,
        "MailFromAttributes": MailFromAttributesTypeDef,
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListEmailIdentitiesResponseTypeDef = TypedDict(
    "ListEmailIdentitiesResponseTypeDef",
    {
        "EmailIdentities": List[IdentityInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Subject": ContentTypeDef,
        "Body": BodyTypeDef,
    },
)

_RequiredEventDestinationTypeDef = TypedDict(
    "_RequiredEventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": List[EventTypeType],
    },
)
_OptionalEventDestinationTypeDef = TypedDict(
    "_OptionalEventDestinationTypeDef",
    {
        "Enabled": bool,
        "KinesisFirehoseDestination": KinesisFirehoseDestinationOutputTypeDef,
        "CloudWatchDestination": CloudWatchDestinationOutputTypeDef,
        "SnsDestination": SnsDestinationOutputTypeDef,
        "PinpointDestination": PinpointDestinationOutputTypeDef,
    },
    total=False,
)

class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, _OptionalEventDestinationTypeDef):
    pass

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": Sequence[EventTypeType],
        "KinesisFirehoseDestination": KinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": CloudWatchDestinationTypeDef,
        "SnsDestination": SnsDestinationTypeDef,
        "PinpointDestination": PinpointDestinationTypeDef,
    },
    total=False,
)

GetDomainStatisticsReportResponseTypeDef = TypedDict(
    "GetDomainStatisticsReportResponseTypeDef",
    {
        "OverallVolume": OverallVolumeTypeDef,
        "DailyVolumes": List[DailyVolumeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": DeliverabilityDashboardAccountStatusType,
        "ActiveSubscribedDomains": List[DomainDeliverabilityTrackingOptionOutputTypeDef],
        "PendingExpirationSubscribedDomains": List[DomainDeliverabilityTrackingOptionOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredPutDeliverabilityDashboardOptionRequestRequestTypeDef = TypedDict(
    "_RequiredPutDeliverabilityDashboardOptionRequestRequestTypeDef",
    {
        "DashboardEnabled": bool,
    },
)
_OptionalPutDeliverabilityDashboardOptionRequestRequestTypeDef = TypedDict(
    "_OptionalPutDeliverabilityDashboardOptionRequestRequestTypeDef",
    {
        "SubscribedDomains": Sequence[DomainDeliverabilityTrackingOptionTypeDef],
    },
    total=False,
)

class PutDeliverabilityDashboardOptionRequestRequestTypeDef(
    _RequiredPutDeliverabilityDashboardOptionRequestRequestTypeDef,
    _OptionalPutDeliverabilityDashboardOptionRequestRequestTypeDef,
):
    pass

GetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "GetDeliverabilityTestReportResponseTypeDef",
    {
        "DeliverabilityTestReport": DeliverabilityTestReportTypeDef,
        "OverallPlacement": PlacementStatisticsTypeDef,
        "IspPlacements": List[IspPlacementTypeDef],
        "Message": str,
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "Simple": MessageTypeDef,
        "Raw": RawMessageTypeDef,
        "Template": TemplateTypeDef,
    },
    total=False,
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List[EventDestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": EventDestinationDefinitionTypeDef,
    },
)

UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": EventDestinationDefinitionTypeDef,
    },
)

_RequiredCreateDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeliverabilityTestReportRequestRequestTypeDef",
    {
        "FromEmailAddress": str,
        "Content": EmailContentTypeDef,
    },
)
_OptionalCreateDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeliverabilityTestReportRequestRequestTypeDef",
    {
        "ReportName": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateDeliverabilityTestReportRequestRequestTypeDef(
    _RequiredCreateDeliverabilityTestReportRequestRequestTypeDef,
    _OptionalCreateDeliverabilityTestReportRequestRequestTypeDef,
):
    pass

_RequiredSendEmailRequestRequestTypeDef = TypedDict(
    "_RequiredSendEmailRequestRequestTypeDef",
    {
        "Destination": DestinationTypeDef,
        "Content": EmailContentTypeDef,
    },
)
_OptionalSendEmailRequestRequestTypeDef = TypedDict(
    "_OptionalSendEmailRequestRequestTypeDef",
    {
        "FromEmailAddress": str,
        "ReplyToAddresses": Sequence[str],
        "FeedbackForwardingEmailAddress": str,
        "EmailTags": Sequence[MessageTagTypeDef],
        "ConfigurationSetName": str,
    },
    total=False,
)

class SendEmailRequestRequestTypeDef(
    _RequiredSendEmailRequestRequestTypeDef, _OptionalSendEmailRequestRequestTypeDef
):
    pass
