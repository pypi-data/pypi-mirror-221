"""
Type annotations for iot1click-devices service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/type_defs/)

Usage::

    ```python
    from mypy_boto3_iot1click_devices.type_defs import ClaimDevicesByClaimCodeRequestRequestTypeDef

    data: ClaimDevicesByClaimCodeRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClaimDevicesByClaimCodeRequestRequestTypeDef",
    "ClaimDevicesByClaimCodeResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DeviceDescriptionTypeDef",
    "DeviceTypeDef",
    "DeviceMethodOutputTypeDef",
    "DeviceMethodTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FinalizeDeviceClaimRequestRequestTypeDef",
    "FinalizeDeviceClaimResponseTypeDef",
    "GetDeviceMethodsRequestRequestTypeDef",
    "InitiateDeviceClaimRequestRequestTypeDef",
    "InitiateDeviceClaimResponseTypeDef",
    "InvokeDeviceMethodResponseTypeDef",
    "ListDeviceEventsRequestListDeviceEventsPaginateTypeDef",
    "ListDeviceEventsRequestRequestTypeDef",
    "ListDevicesRequestListDevicesPaginateTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnclaimDeviceRequestRequestTypeDef",
    "UnclaimDeviceResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceStateRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "DeviceEventTypeDef",
    "GetDeviceMethodsResponseTypeDef",
    "InvokeDeviceMethodRequestRequestTypeDef",
    "ListDeviceEventsResponseTypeDef",
)

ClaimDevicesByClaimCodeRequestRequestTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeRequestRequestTypeDef",
    {
        "ClaimCode": str,
    },
)

ClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeResponseTypeDef",
    {
        "ClaimCode": str,
        "Total": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

DeviceDescriptionTypeDef = TypedDict(
    "DeviceDescriptionTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Attributes": Dict[str, Any],
        "DeviceId": str,
        "Type": str,
    },
    total=False,
)

DeviceMethodOutputTypeDef = TypedDict(
    "DeviceMethodOutputTypeDef",
    {
        "DeviceType": str,
        "MethodName": str,
    },
    total=False,
)

DeviceMethodTypeDef = TypedDict(
    "DeviceMethodTypeDef",
    {
        "DeviceType": str,
        "MethodName": str,
    },
    total=False,
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFinalizeDeviceClaimRequestRequestTypeDef = TypedDict(
    "_RequiredFinalizeDeviceClaimRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalFinalizeDeviceClaimRequestRequestTypeDef = TypedDict(
    "_OptionalFinalizeDeviceClaimRequestRequestTypeDef",
    {
        "Tags": Mapping[str, str],
    },
    total=False,
)


class FinalizeDeviceClaimRequestRequestTypeDef(
    _RequiredFinalizeDeviceClaimRequestRequestTypeDef,
    _OptionalFinalizeDeviceClaimRequestRequestTypeDef,
):
    pass


FinalizeDeviceClaimResponseTypeDef = TypedDict(
    "FinalizeDeviceClaimResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceMethodsRequestRequestTypeDef = TypedDict(
    "GetDeviceMethodsRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

InitiateDeviceClaimRequestRequestTypeDef = TypedDict(
    "InitiateDeviceClaimRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

InitiateDeviceClaimResponseTypeDef = TypedDict(
    "InitiateDeviceClaimResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvokeDeviceMethodResponseTypeDef = TypedDict(
    "InvokeDeviceMethodResponseTypeDef",
    {
        "DeviceMethodResponse": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeviceEventsRequestListDeviceEventsPaginateTypeDef = TypedDict(
    "_RequiredListDeviceEventsRequestListDeviceEventsPaginateTypeDef",
    {
        "DeviceId": str,
        "FromTimeStamp": Union[datetime, str],
        "ToTimeStamp": Union[datetime, str],
    },
)
_OptionalListDeviceEventsRequestListDeviceEventsPaginateTypeDef = TypedDict(
    "_OptionalListDeviceEventsRequestListDeviceEventsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListDeviceEventsRequestListDeviceEventsPaginateTypeDef(
    _RequiredListDeviceEventsRequestListDeviceEventsPaginateTypeDef,
    _OptionalListDeviceEventsRequestListDeviceEventsPaginateTypeDef,
):
    pass


_RequiredListDeviceEventsRequestRequestTypeDef = TypedDict(
    "_RequiredListDeviceEventsRequestRequestTypeDef",
    {
        "DeviceId": str,
        "FromTimeStamp": Union[datetime, str],
        "ToTimeStamp": Union[datetime, str],
    },
)
_OptionalListDeviceEventsRequestRequestTypeDef = TypedDict(
    "_OptionalListDeviceEventsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDeviceEventsRequestRequestTypeDef(
    _RequiredListDeviceEventsRequestRequestTypeDef, _OptionalListDeviceEventsRequestRequestTypeDef
):
    pass


ListDevicesRequestListDevicesPaginateTypeDef = TypedDict(
    "ListDevicesRequestListDevicesPaginateTypeDef",
    {
        "DeviceType": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "DeviceType": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UnclaimDeviceRequestRequestTypeDef = TypedDict(
    "UnclaimDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

UnclaimDeviceResponseTypeDef = TypedDict(
    "UnclaimDeviceResponseTypeDef",
    {
        "State": str,
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

_RequiredUpdateDeviceStateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceStateRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalUpdateDeviceStateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceStateRequestRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)


class UpdateDeviceStateRequestRequestTypeDef(
    _RequiredUpdateDeviceStateRequestRequestTypeDef, _OptionalUpdateDeviceStateRequestRequestTypeDef
):
    pass


DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "DeviceDescription": DeviceDescriptionTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List[DeviceDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {
        "Device": DeviceTypeDef,
        "StdEvent": str,
    },
    total=False,
)

GetDeviceMethodsResponseTypeDef = TypedDict(
    "GetDeviceMethodsResponseTypeDef",
    {
        "DeviceMethods": List[DeviceMethodOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInvokeDeviceMethodRequestRequestTypeDef = TypedDict(
    "_RequiredInvokeDeviceMethodRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalInvokeDeviceMethodRequestRequestTypeDef = TypedDict(
    "_OptionalInvokeDeviceMethodRequestRequestTypeDef",
    {
        "DeviceMethod": DeviceMethodTypeDef,
        "DeviceMethodParameters": str,
    },
    total=False,
)


class InvokeDeviceMethodRequestRequestTypeDef(
    _RequiredInvokeDeviceMethodRequestRequestTypeDef,
    _OptionalInvokeDeviceMethodRequestRequestTypeDef,
):
    pass


ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {
        "Events": List[DeviceEventTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
