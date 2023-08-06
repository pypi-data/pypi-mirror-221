"""
Type annotations for iotsecuretunneling service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.type_defs import CloseTunnelRequestRequestTypeDef

    data: CloseTunnelRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import ClientModeType, ConnectionStatusType, TunnelStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CloseTunnelRequestRequestTypeDef",
    "ConnectionStateTypeDef",
    "DescribeTunnelRequestRequestTypeDef",
    "DestinationConfigOutputTypeDef",
    "DestinationConfigTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "ListTunnelsRequestRequestTypeDef",
    "TunnelSummaryTypeDef",
    "TagTypeDef",
    "TimeoutConfigTypeDef",
    "OpenTunnelResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RotateTunnelAccessTokenResponseTypeDef",
    "TimeoutConfigOutputTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "RotateTunnelAccessTokenRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTunnelsResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "OpenTunnelRequestRequestTypeDef",
    "TunnelTypeDef",
    "DescribeTunnelResponseTypeDef",
)

_RequiredCloseTunnelRequestRequestTypeDef = TypedDict(
    "_RequiredCloseTunnelRequestRequestTypeDef",
    {
        "tunnelId": str,
    },
)
_OptionalCloseTunnelRequestRequestTypeDef = TypedDict(
    "_OptionalCloseTunnelRequestRequestTypeDef",
    {
        "delete": bool,
    },
    total=False,
)

class CloseTunnelRequestRequestTypeDef(
    _RequiredCloseTunnelRequestRequestTypeDef, _OptionalCloseTunnelRequestRequestTypeDef
):
    pass

ConnectionStateTypeDef = TypedDict(
    "ConnectionStateTypeDef",
    {
        "status": ConnectionStatusType,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

DescribeTunnelRequestRequestTypeDef = TypedDict(
    "DescribeTunnelRequestRequestTypeDef",
    {
        "tunnelId": str,
    },
)

_RequiredDestinationConfigOutputTypeDef = TypedDict(
    "_RequiredDestinationConfigOutputTypeDef",
    {
        "services": List[str],
    },
)
_OptionalDestinationConfigOutputTypeDef = TypedDict(
    "_OptionalDestinationConfigOutputTypeDef",
    {
        "thingName": str,
    },
    total=False,
)

class DestinationConfigOutputTypeDef(
    _RequiredDestinationConfigOutputTypeDef, _OptionalDestinationConfigOutputTypeDef
):
    pass

_RequiredDestinationConfigTypeDef = TypedDict(
    "_RequiredDestinationConfigTypeDef",
    {
        "services": Sequence[str],
    },
)
_OptionalDestinationConfigTypeDef = TypedDict(
    "_OptionalDestinationConfigTypeDef",
    {
        "thingName": str,
    },
    total=False,
)

class DestinationConfigTypeDef(
    _RequiredDestinationConfigTypeDef, _OptionalDestinationConfigTypeDef
):
    pass

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "key": str,
        "value": str,
    },
)

ListTunnelsRequestRequestTypeDef = TypedDict(
    "ListTunnelsRequestRequestTypeDef",
    {
        "thingName": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

TunnelSummaryTypeDef = TypedDict(
    "TunnelSummaryTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": TunnelStatusType,
        "description": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef",
    {
        "maxLifetimeTimeoutMinutes": int,
    },
    total=False,
)

OpenTunnelResponseTypeDef = TypedDict(
    "OpenTunnelResponseTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "sourceAccessToken": str,
        "destinationAccessToken": str,
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

RotateTunnelAccessTokenResponseTypeDef = TypedDict(
    "RotateTunnelAccessTokenResponseTypeDef",
    {
        "tunnelArn": str,
        "sourceAccessToken": str,
        "destinationAccessToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TimeoutConfigOutputTypeDef = TypedDict(
    "TimeoutConfigOutputTypeDef",
    {
        "maxLifetimeTimeoutMinutes": int,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredRotateTunnelAccessTokenRequestRequestTypeDef = TypedDict(
    "_RequiredRotateTunnelAccessTokenRequestRequestTypeDef",
    {
        "tunnelId": str,
        "clientMode": ClientModeType,
    },
)
_OptionalRotateTunnelAccessTokenRequestRequestTypeDef = TypedDict(
    "_OptionalRotateTunnelAccessTokenRequestRequestTypeDef",
    {
        "destinationConfig": DestinationConfigTypeDef,
    },
    total=False,
)

class RotateTunnelAccessTokenRequestRequestTypeDef(
    _RequiredRotateTunnelAccessTokenRequestRequestTypeDef,
    _OptionalRotateTunnelAccessTokenRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTunnelsResponseTypeDef = TypedDict(
    "ListTunnelsResponseTypeDef",
    {
        "tunnelSummaries": List[TunnelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)

OpenTunnelRequestRequestTypeDef = TypedDict(
    "OpenTunnelRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
        "destinationConfig": DestinationConfigTypeDef,
        "timeoutConfig": TimeoutConfigTypeDef,
    },
    total=False,
)

TunnelTypeDef = TypedDict(
    "TunnelTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": TunnelStatusType,
        "sourceConnectionState": ConnectionStateTypeDef,
        "destinationConnectionState": ConnectionStateTypeDef,
        "description": str,
        "destinationConfig": DestinationConfigOutputTypeDef,
        "timeoutConfig": TimeoutConfigOutputTypeDef,
        "tags": List[TagOutputTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

DescribeTunnelResponseTypeDef = TypedDict(
    "DescribeTunnelResponseTypeDef",
    {
        "tunnel": TunnelTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
