"""
Type annotations for snowball service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snowball/type_defs/)

Usage::

    ```python
    from mypy_boto3_snowball.type_defs import AddressOutputTypeDef

    data: AddressOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AddressTypeType,
    ClusterStateType,
    DeviceServiceNameType,
    ImpactLevelType,
    JobStateType,
    JobTypeType,
    LongTermPricingTypeType,
    RemoteManagementType,
    ServiceNameType,
    ShipmentStateType,
    ShippingLabelStatusType,
    ShippingOptionType,
    SnowballCapacityType,
    SnowballTypeType,
    TransferOptionType,
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
    "CancelClusterRequestRequestTypeDef",
    "CancelJobRequestRequestTypeDef",
    "ClusterListEntryTypeDef",
    "NotificationOutputTypeDef",
    "CompatibleImageTypeDef",
    "ResponseMetadataTypeDef",
    "NotificationTypeDef",
    "JobListEntryTypeDef",
    "PickupDetailsTypeDef",
    "CreateLongTermPricingRequestRequestTypeDef",
    "CreateReturnShippingLabelRequestRequestTypeDef",
    "DataTransferTypeDef",
    "ServiceVersionOutputTypeDef",
    "ServiceVersionTypeDef",
    "DescribeAddressRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAddressesRequestRequestTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeReturnShippingLabelRequestRequestTypeDef",
    "EKSOnDeviceServiceConfigurationOutputTypeDef",
    "EKSOnDeviceServiceConfigurationTypeDef",
    "Ec2AmiResourceOutputTypeDef",
    "Ec2AmiResourceTypeDef",
    "EventTriggerDefinitionOutputTypeDef",
    "EventTriggerDefinitionTypeDef",
    "GetJobManifestRequestRequestTypeDef",
    "GetJobUnlockCodeRequestRequestTypeDef",
    "GetSoftwareUpdatesRequestRequestTypeDef",
    "INDTaxDocumentsOutputTypeDef",
    "INDTaxDocumentsTypeDef",
    "JobLogsTypeDef",
    "PickupDetailsOutputTypeDef",
    "KeyRangeOutputTypeDef",
    "KeyRangeTypeDef",
    "ListClusterJobsRequestRequestTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListCompatibleImagesRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListLongTermPricingRequestRequestTypeDef",
    "LongTermPricingListEntryTypeDef",
    "ListPickupLocationsRequestRequestTypeDef",
    "NFSOnDeviceServiceConfigurationOutputTypeDef",
    "NFSOnDeviceServiceConfigurationTypeDef",
    "S3OnDeviceServiceConfigurationOutputTypeDef",
    "TGWOnDeviceServiceConfigurationOutputTypeDef",
    "S3OnDeviceServiceConfigurationTypeDef",
    "TGWOnDeviceServiceConfigurationTypeDef",
    "TargetOnDeviceServiceOutputTypeDef",
    "TargetOnDeviceServiceTypeDef",
    "ShipmentTypeDef",
    "WirelessConnectionOutputTypeDef",
    "WirelessConnectionTypeDef",
    "UpdateJobShipmentStateRequestRequestTypeDef",
    "UpdateLongTermPricingRequestRequestTypeDef",
    "CreateAddressRequestRequestTypeDef",
    "CreateAddressResultTypeDef",
    "CreateJobResultTypeDef",
    "CreateLongTermPricingResultTypeDef",
    "CreateReturnShippingLabelResultTypeDef",
    "DescribeAddressResultTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeReturnShippingLabelResultTypeDef",
    "GetJobManifestResultTypeDef",
    "GetJobUnlockCodeResultTypeDef",
    "GetSnowballUsageResultTypeDef",
    "GetSoftwareUpdatesResultTypeDef",
    "ListClustersResultTypeDef",
    "ListCompatibleImagesResultTypeDef",
    "ListPickupLocationsResultTypeDef",
    "CreateClusterResultTypeDef",
    "ListClusterJobsResultTypeDef",
    "ListJobsResultTypeDef",
    "DependentServiceOutputTypeDef",
    "DependentServiceTypeDef",
    "DescribeAddressesRequestDescribeAddressesPaginateTypeDef",
    "ListClusterJobsRequestListClusterJobsPaginateTypeDef",
    "ListClustersRequestListClustersPaginateTypeDef",
    "ListCompatibleImagesRequestListCompatibleImagesPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListLongTermPricingRequestListLongTermPricingPaginateTypeDef",
    "LambdaResourceOutputTypeDef",
    "LambdaResourceTypeDef",
    "TaxDocumentsOutputTypeDef",
    "TaxDocumentsTypeDef",
    "ListLongTermPricingResultTypeDef",
    "OnDeviceServiceConfigurationOutputTypeDef",
    "OnDeviceServiceConfigurationTypeDef",
    "S3ResourceOutputTypeDef",
    "S3ResourceTypeDef",
    "ShippingDetailsTypeDef",
    "SnowconeDeviceConfigurationOutputTypeDef",
    "SnowconeDeviceConfigurationTypeDef",
    "ListServiceVersionsResultTypeDef",
    "ListServiceVersionsRequestRequestTypeDef",
    "JobResourceOutputTypeDef",
    "JobResourceTypeDef",
    "DeviceConfigurationOutputTypeDef",
    "DeviceConfigurationTypeDef",
    "ClusterMetadataTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "JobMetadataTypeDef",
    "CreateJobRequestRequestTypeDef",
    "DescribeClusterResultTypeDef",
    "DescribeJobResultTypeDef",
)

AddressOutputTypeDef = TypedDict(
    "AddressOutputTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
        "Type": AddressTypeType,
    },
    total=False,
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
        "Type": AddressTypeType,
    },
    total=False,
)

CancelClusterRequestRequestTypeDef = TypedDict(
    "CancelClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

ClusterListEntryTypeDef = TypedDict(
    "ClusterListEntryTypeDef",
    {
        "ClusterId": str,
        "ClusterState": ClusterStateType,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

NotificationOutputTypeDef = TypedDict(
    "NotificationOutputTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[JobStateType],
        "NotifyAll": bool,
        "DevicePickupSnsTopicARN": str,
    },
    total=False,
)

CompatibleImageTypeDef = TypedDict(
    "CompatibleImageTypeDef",
    {
        "AmiId": str,
        "Name": str,
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

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": Sequence[JobStateType],
        "NotifyAll": bool,
        "DevicePickupSnsTopicARN": str,
    },
    total=False,
)

JobListEntryTypeDef = TypedDict(
    "JobListEntryTypeDef",
    {
        "JobId": str,
        "JobState": JobStateType,
        "IsMaster": bool,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

PickupDetailsTypeDef = TypedDict(
    "PickupDetailsTypeDef",
    {
        "Name": str,
        "PhoneNumber": str,
        "Email": str,
        "IdentificationNumber": str,
        "IdentificationExpirationDate": Union[datetime, str],
        "IdentificationIssuingOrg": str,
        "DevicePickupId": str,
    },
    total=False,
)

_RequiredCreateLongTermPricingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLongTermPricingRequestRequestTypeDef",
    {
        "LongTermPricingType": LongTermPricingTypeType,
        "SnowballType": SnowballTypeType,
    },
)
_OptionalCreateLongTermPricingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLongTermPricingRequestRequestTypeDef",
    {
        "IsLongTermPricingAutoRenew": bool,
    },
    total=False,
)

class CreateLongTermPricingRequestRequestTypeDef(
    _RequiredCreateLongTermPricingRequestRequestTypeDef,
    _OptionalCreateLongTermPricingRequestRequestTypeDef,
):
    pass

_RequiredCreateReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReturnShippingLabelRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalCreateReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReturnShippingLabelRequestRequestTypeDef",
    {
        "ShippingOption": ShippingOptionType,
    },
    total=False,
)

class CreateReturnShippingLabelRequestRequestTypeDef(
    _RequiredCreateReturnShippingLabelRequestRequestTypeDef,
    _OptionalCreateReturnShippingLabelRequestRequestTypeDef,
):
    pass

DataTransferTypeDef = TypedDict(
    "DataTransferTypeDef",
    {
        "BytesTransferred": int,
        "ObjectsTransferred": int,
        "TotalBytes": int,
        "TotalObjects": int,
    },
    total=False,
)

ServiceVersionOutputTypeDef = TypedDict(
    "ServiceVersionOutputTypeDef",
    {
        "Version": str,
    },
    total=False,
)

ServiceVersionTypeDef = TypedDict(
    "ServiceVersionTypeDef",
    {
        "Version": str,
    },
    total=False,
)

DescribeAddressRequestRequestTypeDef = TypedDict(
    "DescribeAddressRequestRequestTypeDef",
    {
        "AddressId": str,
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

DescribeAddressesRequestRequestTypeDef = TypedDict(
    "DescribeAddressesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeReturnShippingLabelRequestRequestTypeDef = TypedDict(
    "DescribeReturnShippingLabelRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

EKSOnDeviceServiceConfigurationOutputTypeDef = TypedDict(
    "EKSOnDeviceServiceConfigurationOutputTypeDef",
    {
        "KubernetesVersion": str,
        "EKSAnywhereVersion": str,
    },
    total=False,
)

EKSOnDeviceServiceConfigurationTypeDef = TypedDict(
    "EKSOnDeviceServiceConfigurationTypeDef",
    {
        "KubernetesVersion": str,
        "EKSAnywhereVersion": str,
    },
    total=False,
)

_RequiredEc2AmiResourceOutputTypeDef = TypedDict(
    "_RequiredEc2AmiResourceOutputTypeDef",
    {
        "AmiId": str,
    },
)
_OptionalEc2AmiResourceOutputTypeDef = TypedDict(
    "_OptionalEc2AmiResourceOutputTypeDef",
    {
        "SnowballAmiId": str,
    },
    total=False,
)

class Ec2AmiResourceOutputTypeDef(
    _RequiredEc2AmiResourceOutputTypeDef, _OptionalEc2AmiResourceOutputTypeDef
):
    pass

_RequiredEc2AmiResourceTypeDef = TypedDict(
    "_RequiredEc2AmiResourceTypeDef",
    {
        "AmiId": str,
    },
)
_OptionalEc2AmiResourceTypeDef = TypedDict(
    "_OptionalEc2AmiResourceTypeDef",
    {
        "SnowballAmiId": str,
    },
    total=False,
)

class Ec2AmiResourceTypeDef(_RequiredEc2AmiResourceTypeDef, _OptionalEc2AmiResourceTypeDef):
    pass

EventTriggerDefinitionOutputTypeDef = TypedDict(
    "EventTriggerDefinitionOutputTypeDef",
    {
        "EventResourceARN": str,
    },
    total=False,
)

EventTriggerDefinitionTypeDef = TypedDict(
    "EventTriggerDefinitionTypeDef",
    {
        "EventResourceARN": str,
    },
    total=False,
)

GetJobManifestRequestRequestTypeDef = TypedDict(
    "GetJobManifestRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobUnlockCodeRequestRequestTypeDef = TypedDict(
    "GetJobUnlockCodeRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetSoftwareUpdatesRequestRequestTypeDef = TypedDict(
    "GetSoftwareUpdatesRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

INDTaxDocumentsOutputTypeDef = TypedDict(
    "INDTaxDocumentsOutputTypeDef",
    {
        "GSTIN": str,
    },
    total=False,
)

INDTaxDocumentsTypeDef = TypedDict(
    "INDTaxDocumentsTypeDef",
    {
        "GSTIN": str,
    },
    total=False,
)

JobLogsTypeDef = TypedDict(
    "JobLogsTypeDef",
    {
        "JobCompletionReportURI": str,
        "JobSuccessLogURI": str,
        "JobFailureLogURI": str,
    },
    total=False,
)

PickupDetailsOutputTypeDef = TypedDict(
    "PickupDetailsOutputTypeDef",
    {
        "Name": str,
        "PhoneNumber": str,
        "Email": str,
        "IdentificationNumber": str,
        "IdentificationExpirationDate": datetime,
        "IdentificationIssuingOrg": str,
        "DevicePickupId": str,
    },
    total=False,
)

KeyRangeOutputTypeDef = TypedDict(
    "KeyRangeOutputTypeDef",
    {
        "BeginMarker": str,
        "EndMarker": str,
    },
    total=False,
)

KeyRangeTypeDef = TypedDict(
    "KeyRangeTypeDef",
    {
        "BeginMarker": str,
        "EndMarker": str,
    },
    total=False,
)

_RequiredListClusterJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListClusterJobsRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListClusterJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListClusterJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListClusterJobsRequestRequestTypeDef(
    _RequiredListClusterJobsRequestRequestTypeDef, _OptionalListClusterJobsRequestRequestTypeDef
):
    pass

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCompatibleImagesRequestRequestTypeDef = TypedDict(
    "ListCompatibleImagesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLongTermPricingRequestRequestTypeDef = TypedDict(
    "ListLongTermPricingRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

LongTermPricingListEntryTypeDef = TypedDict(
    "LongTermPricingListEntryTypeDef",
    {
        "LongTermPricingId": str,
        "LongTermPricingEndDate": datetime,
        "LongTermPricingStartDate": datetime,
        "LongTermPricingType": LongTermPricingTypeType,
        "CurrentActiveJob": str,
        "ReplacementJob": str,
        "IsLongTermPricingAutoRenew": bool,
        "LongTermPricingStatus": str,
        "SnowballType": SnowballTypeType,
        "JobIds": List[str],
    },
    total=False,
)

ListPickupLocationsRequestRequestTypeDef = TypedDict(
    "ListPickupLocationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

NFSOnDeviceServiceConfigurationOutputTypeDef = TypedDict(
    "NFSOnDeviceServiceConfigurationOutputTypeDef",
    {
        "StorageLimit": int,
        "StorageUnit": Literal["TB"],
    },
    total=False,
)

NFSOnDeviceServiceConfigurationTypeDef = TypedDict(
    "NFSOnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": int,
        "StorageUnit": Literal["TB"],
    },
    total=False,
)

S3OnDeviceServiceConfigurationOutputTypeDef = TypedDict(
    "S3OnDeviceServiceConfigurationOutputTypeDef",
    {
        "StorageLimit": float,
        "StorageUnit": Literal["TB"],
        "ServiceSize": int,
        "FaultTolerance": int,
    },
    total=False,
)

TGWOnDeviceServiceConfigurationOutputTypeDef = TypedDict(
    "TGWOnDeviceServiceConfigurationOutputTypeDef",
    {
        "StorageLimit": int,
        "StorageUnit": Literal["TB"],
    },
    total=False,
)

S3OnDeviceServiceConfigurationTypeDef = TypedDict(
    "S3OnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": float,
        "StorageUnit": Literal["TB"],
        "ServiceSize": int,
        "FaultTolerance": int,
    },
    total=False,
)

TGWOnDeviceServiceConfigurationTypeDef = TypedDict(
    "TGWOnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": int,
        "StorageUnit": Literal["TB"],
    },
    total=False,
)

TargetOnDeviceServiceOutputTypeDef = TypedDict(
    "TargetOnDeviceServiceOutputTypeDef",
    {
        "ServiceName": DeviceServiceNameType,
        "TransferOption": TransferOptionType,
    },
    total=False,
)

TargetOnDeviceServiceTypeDef = TypedDict(
    "TargetOnDeviceServiceTypeDef",
    {
        "ServiceName": DeviceServiceNameType,
        "TransferOption": TransferOptionType,
    },
    total=False,
)

ShipmentTypeDef = TypedDict(
    "ShipmentTypeDef",
    {
        "Status": str,
        "TrackingNumber": str,
    },
    total=False,
)

WirelessConnectionOutputTypeDef = TypedDict(
    "WirelessConnectionOutputTypeDef",
    {
        "IsWifiEnabled": bool,
    },
    total=False,
)

WirelessConnectionTypeDef = TypedDict(
    "WirelessConnectionTypeDef",
    {
        "IsWifiEnabled": bool,
    },
    total=False,
)

UpdateJobShipmentStateRequestRequestTypeDef = TypedDict(
    "UpdateJobShipmentStateRequestRequestTypeDef",
    {
        "JobId": str,
        "ShipmentState": ShipmentStateType,
    },
)

_RequiredUpdateLongTermPricingRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLongTermPricingRequestRequestTypeDef",
    {
        "LongTermPricingId": str,
    },
)
_OptionalUpdateLongTermPricingRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLongTermPricingRequestRequestTypeDef",
    {
        "ReplacementJob": str,
        "IsLongTermPricingAutoRenew": bool,
    },
    total=False,
)

class UpdateLongTermPricingRequestRequestTypeDef(
    _RequiredUpdateLongTermPricingRequestRequestTypeDef,
    _OptionalUpdateLongTermPricingRequestRequestTypeDef,
):
    pass

CreateAddressRequestRequestTypeDef = TypedDict(
    "CreateAddressRequestRequestTypeDef",
    {
        "Address": AddressTypeDef,
    },
)

CreateAddressResultTypeDef = TypedDict(
    "CreateAddressResultTypeDef",
    {
        "AddressId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateLongTermPricingResultTypeDef = TypedDict(
    "CreateLongTermPricingResultTypeDef",
    {
        "LongTermPricingId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateReturnShippingLabelResultTypeDef = TypedDict(
    "CreateReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAddressResultTypeDef = TypedDict(
    "DescribeAddressResultTypeDef",
    {
        "Address": AddressOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {
        "Addresses": List[AddressOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeReturnShippingLabelResultTypeDef = TypedDict(
    "DescribeReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ExpirationDate": datetime,
        "ReturnShippingLabelURI": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetJobManifestResultTypeDef = TypedDict(
    "GetJobManifestResultTypeDef",
    {
        "ManifestURI": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetJobUnlockCodeResultTypeDef = TypedDict(
    "GetJobUnlockCodeResultTypeDef",
    {
        "UnlockCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSnowballUsageResultTypeDef = TypedDict(
    "GetSnowballUsageResultTypeDef",
    {
        "SnowballLimit": int,
        "SnowballsInUse": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSoftwareUpdatesResultTypeDef = TypedDict(
    "GetSoftwareUpdatesResultTypeDef",
    {
        "UpdatesURI": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListClustersResultTypeDef = TypedDict(
    "ListClustersResultTypeDef",
    {
        "ClusterListEntries": List[ClusterListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCompatibleImagesResultTypeDef = TypedDict(
    "ListCompatibleImagesResultTypeDef",
    {
        "CompatibleImages": List[CompatibleImageTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPickupLocationsResultTypeDef = TypedDict(
    "ListPickupLocationsResultTypeDef",
    {
        "Addresses": List[AddressOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef",
    {
        "ClusterId": str,
        "JobListEntries": List[JobListEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListClusterJobsResultTypeDef = TypedDict(
    "ListClusterJobsResultTypeDef",
    {
        "JobListEntries": List[JobListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "JobListEntries": List[JobListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DependentServiceOutputTypeDef = TypedDict(
    "DependentServiceOutputTypeDef",
    {
        "ServiceName": ServiceNameType,
        "ServiceVersion": ServiceVersionOutputTypeDef,
    },
    total=False,
)

DependentServiceTypeDef = TypedDict(
    "DependentServiceTypeDef",
    {
        "ServiceName": ServiceNameType,
        "ServiceVersion": ServiceVersionTypeDef,
    },
    total=False,
)

DescribeAddressesRequestDescribeAddressesPaginateTypeDef = TypedDict(
    "DescribeAddressesRequestDescribeAddressesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListClusterJobsRequestListClusterJobsPaginateTypeDef = TypedDict(
    "_RequiredListClusterJobsRequestListClusterJobsPaginateTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListClusterJobsRequestListClusterJobsPaginateTypeDef = TypedDict(
    "_OptionalListClusterJobsRequestListClusterJobsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListClusterJobsRequestListClusterJobsPaginateTypeDef(
    _RequiredListClusterJobsRequestListClusterJobsPaginateTypeDef,
    _OptionalListClusterJobsRequestListClusterJobsPaginateTypeDef,
):
    pass

ListClustersRequestListClustersPaginateTypeDef = TypedDict(
    "ListClustersRequestListClustersPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListCompatibleImagesRequestListCompatibleImagesPaginateTypeDef = TypedDict(
    "ListCompatibleImagesRequestListCompatibleImagesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListLongTermPricingRequestListLongTermPricingPaginateTypeDef = TypedDict(
    "ListLongTermPricingRequestListLongTermPricingPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

LambdaResourceOutputTypeDef = TypedDict(
    "LambdaResourceOutputTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[EventTriggerDefinitionOutputTypeDef],
    },
    total=False,
)

LambdaResourceTypeDef = TypedDict(
    "LambdaResourceTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": Sequence[EventTriggerDefinitionTypeDef],
    },
    total=False,
)

TaxDocumentsOutputTypeDef = TypedDict(
    "TaxDocumentsOutputTypeDef",
    {
        "IND": INDTaxDocumentsOutputTypeDef,
    },
    total=False,
)

TaxDocumentsTypeDef = TypedDict(
    "TaxDocumentsTypeDef",
    {
        "IND": INDTaxDocumentsTypeDef,
    },
    total=False,
)

ListLongTermPricingResultTypeDef = TypedDict(
    "ListLongTermPricingResultTypeDef",
    {
        "LongTermPricingEntries": List[LongTermPricingListEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

OnDeviceServiceConfigurationOutputTypeDef = TypedDict(
    "OnDeviceServiceConfigurationOutputTypeDef",
    {
        "NFSOnDeviceService": NFSOnDeviceServiceConfigurationOutputTypeDef,
        "TGWOnDeviceService": TGWOnDeviceServiceConfigurationOutputTypeDef,
        "EKSOnDeviceService": EKSOnDeviceServiceConfigurationOutputTypeDef,
        "S3OnDeviceService": S3OnDeviceServiceConfigurationOutputTypeDef,
    },
    total=False,
)

OnDeviceServiceConfigurationTypeDef = TypedDict(
    "OnDeviceServiceConfigurationTypeDef",
    {
        "NFSOnDeviceService": NFSOnDeviceServiceConfigurationTypeDef,
        "TGWOnDeviceService": TGWOnDeviceServiceConfigurationTypeDef,
        "EKSOnDeviceService": EKSOnDeviceServiceConfigurationTypeDef,
        "S3OnDeviceService": S3OnDeviceServiceConfigurationTypeDef,
    },
    total=False,
)

S3ResourceOutputTypeDef = TypedDict(
    "S3ResourceOutputTypeDef",
    {
        "BucketArn": str,
        "KeyRange": KeyRangeOutputTypeDef,
        "TargetOnDeviceServices": List[TargetOnDeviceServiceOutputTypeDef],
    },
    total=False,
)

S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef",
    {
        "BucketArn": str,
        "KeyRange": KeyRangeTypeDef,
        "TargetOnDeviceServices": Sequence[TargetOnDeviceServiceTypeDef],
    },
    total=False,
)

ShippingDetailsTypeDef = TypedDict(
    "ShippingDetailsTypeDef",
    {
        "ShippingOption": ShippingOptionType,
        "InboundShipment": ShipmentTypeDef,
        "OutboundShipment": ShipmentTypeDef,
    },
    total=False,
)

SnowconeDeviceConfigurationOutputTypeDef = TypedDict(
    "SnowconeDeviceConfigurationOutputTypeDef",
    {
        "WirelessConnection": WirelessConnectionOutputTypeDef,
    },
    total=False,
)

SnowconeDeviceConfigurationTypeDef = TypedDict(
    "SnowconeDeviceConfigurationTypeDef",
    {
        "WirelessConnection": WirelessConnectionTypeDef,
    },
    total=False,
)

ListServiceVersionsResultTypeDef = TypedDict(
    "ListServiceVersionsResultTypeDef",
    {
        "ServiceVersions": List[ServiceVersionOutputTypeDef],
        "ServiceName": ServiceNameType,
        "DependentServices": List[DependentServiceOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListServiceVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListServiceVersionsRequestRequestTypeDef",
    {
        "ServiceName": ServiceNameType,
    },
)
_OptionalListServiceVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListServiceVersionsRequestRequestTypeDef",
    {
        "DependentServices": Sequence[DependentServiceTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListServiceVersionsRequestRequestTypeDef(
    _RequiredListServiceVersionsRequestRequestTypeDef,
    _OptionalListServiceVersionsRequestRequestTypeDef,
):
    pass

JobResourceOutputTypeDef = TypedDict(
    "JobResourceOutputTypeDef",
    {
        "S3Resources": List[S3ResourceOutputTypeDef],
        "LambdaResources": List[LambdaResourceOutputTypeDef],
        "Ec2AmiResources": List[Ec2AmiResourceOutputTypeDef],
    },
    total=False,
)

JobResourceTypeDef = TypedDict(
    "JobResourceTypeDef",
    {
        "S3Resources": Sequence[S3ResourceTypeDef],
        "LambdaResources": Sequence[LambdaResourceTypeDef],
        "Ec2AmiResources": Sequence[Ec2AmiResourceTypeDef],
    },
    total=False,
)

DeviceConfigurationOutputTypeDef = TypedDict(
    "DeviceConfigurationOutputTypeDef",
    {
        "SnowconeDeviceConfiguration": SnowconeDeviceConfigurationOutputTypeDef,
    },
    total=False,
)

DeviceConfigurationTypeDef = TypedDict(
    "DeviceConfigurationTypeDef",
    {
        "SnowconeDeviceConfiguration": SnowconeDeviceConfigurationTypeDef,
    },
    total=False,
)

ClusterMetadataTypeDef = TypedDict(
    "ClusterMetadataTypeDef",
    {
        "ClusterId": str,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "ClusterState": ClusterStateType,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Resources": JobResourceOutputTypeDef,
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Notification": NotificationOutputTypeDef,
        "ForwardingAddressId": str,
        "TaxDocuments": TaxDocumentsOutputTypeDef,
        "OnDeviceServiceConfiguration": OnDeviceServiceConfigurationOutputTypeDef,
    },
    total=False,
)

_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "JobType": JobTypeType,
        "AddressId": str,
        "SnowballType": SnowballTypeType,
        "ShippingOption": ShippingOptionType,
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "Resources": JobResourceTypeDef,
        "OnDeviceServiceConfiguration": OnDeviceServiceConfigurationTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "Notification": NotificationTypeDef,
        "ForwardingAddressId": str,
        "TaxDocuments": TaxDocumentsTypeDef,
        "RemoteManagement": RemoteManagementType,
        "InitialClusterSize": int,
        "ForceCreateJobs": bool,
        "LongTermPricingIds": Sequence[str],
        "SnowballCapacityPreference": SnowballCapacityType,
    },
    total=False,
)

class CreateClusterRequestRequestTypeDef(
    _RequiredCreateClusterRequestRequestTypeDef, _OptionalCreateClusterRequestRequestTypeDef
):
    pass

_RequiredUpdateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalUpdateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterRequestRequestTypeDef",
    {
        "RoleARN": str,
        "Description": str,
        "Resources": JobResourceTypeDef,
        "OnDeviceServiceConfiguration": OnDeviceServiceConfigurationTypeDef,
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Notification": NotificationTypeDef,
        "ForwardingAddressId": str,
    },
    total=False,
)

class UpdateClusterRequestRequestTypeDef(
    _RequiredUpdateClusterRequestRequestTypeDef, _OptionalUpdateClusterRequestRequestTypeDef
):
    pass

_RequiredUpdateJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalUpdateJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobRequestRequestTypeDef",
    {
        "RoleARN": str,
        "Notification": NotificationTypeDef,
        "Resources": JobResourceTypeDef,
        "OnDeviceServiceConfiguration": OnDeviceServiceConfigurationTypeDef,
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Description": str,
        "SnowballCapacityPreference": SnowballCapacityType,
        "ForwardingAddressId": str,
        "PickupDetails": PickupDetailsTypeDef,
    },
    total=False,
)

class UpdateJobRequestRequestTypeDef(
    _RequiredUpdateJobRequestRequestTypeDef, _OptionalUpdateJobRequestRequestTypeDef
):
    pass

JobMetadataTypeDef = TypedDict(
    "JobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": JobStateType,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Resources": JobResourceOutputTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": ShippingDetailsTypeDef,
        "SnowballCapacityPreference": SnowballCapacityType,
        "Notification": NotificationOutputTypeDef,
        "DataTransferProgress": DataTransferTypeDef,
        "JobLogInfo": JobLogsTypeDef,
        "ClusterId": str,
        "ForwardingAddressId": str,
        "TaxDocuments": TaxDocumentsOutputTypeDef,
        "DeviceConfiguration": DeviceConfigurationOutputTypeDef,
        "RemoteManagement": RemoteManagementType,
        "LongTermPricingId": str,
        "OnDeviceServiceConfiguration": OnDeviceServiceConfigurationOutputTypeDef,
        "ImpactLevel": ImpactLevelType,
        "PickupDetails": PickupDetailsOutputTypeDef,
        "SnowballId": str,
    },
    total=False,
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Resources": JobResourceTypeDef,
        "OnDeviceServiceConfiguration": OnDeviceServiceConfigurationTypeDef,
        "Description": str,
        "AddressId": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "SnowballCapacityPreference": SnowballCapacityType,
        "ShippingOption": ShippingOptionType,
        "Notification": NotificationTypeDef,
        "ClusterId": str,
        "SnowballType": SnowballTypeType,
        "ForwardingAddressId": str,
        "TaxDocuments": TaxDocumentsTypeDef,
        "DeviceConfiguration": DeviceConfigurationTypeDef,
        "RemoteManagement": RemoteManagementType,
        "LongTermPricingId": str,
        "ImpactLevel": ImpactLevelType,
        "PickupDetails": PickupDetailsTypeDef,
    },
    total=False,
)

DescribeClusterResultTypeDef = TypedDict(
    "DescribeClusterResultTypeDef",
    {
        "ClusterMetadata": ClusterMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "JobMetadata": JobMetadataTypeDef,
        "SubJobMetadata": List[JobMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
