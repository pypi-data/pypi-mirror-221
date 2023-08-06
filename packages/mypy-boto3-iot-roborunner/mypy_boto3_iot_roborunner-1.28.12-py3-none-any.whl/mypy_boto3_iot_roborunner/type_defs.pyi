"""
Type annotations for iot-roborunner service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/type_defs/)

Usage::

    ```python
    from mypy_boto3_iot_roborunner.type_defs import CartesianCoordinatesOutputTypeDef

    data: CartesianCoordinatesOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import DestinationStateType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CartesianCoordinatesOutputTypeDef",
    "CartesianCoordinatesTypeDef",
    "CreateDestinationRequestRequestTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateSiteRequestRequestTypeDef",
    "CreateSiteResponseTypeDef",
    "CreateWorkerFleetRequestRequestTypeDef",
    "CreateWorkerFleetResponseTypeDef",
    "OrientationTypeDef",
    "VendorPropertiesTypeDef",
    "CreateWorkerResponseTypeDef",
    "DeleteDestinationRequestRequestTypeDef",
    "DeleteSiteRequestRequestTypeDef",
    "DeleteWorkerFleetRequestRequestTypeDef",
    "DeleteWorkerRequestRequestTypeDef",
    "DestinationTypeDef",
    "GetDestinationRequestRequestTypeDef",
    "GetDestinationResponseTypeDef",
    "GetSiteRequestRequestTypeDef",
    "GetSiteResponseTypeDef",
    "GetWorkerFleetRequestRequestTypeDef",
    "GetWorkerFleetResponseTypeDef",
    "GetWorkerRequestRequestTypeDef",
    "OrientationOutputTypeDef",
    "VendorPropertiesOutputTypeDef",
    "ListDestinationsRequestListDestinationsPaginateTypeDef",
    "ListDestinationsRequestRequestTypeDef",
    "ListSitesRequestListSitesPaginateTypeDef",
    "ListSitesRequestRequestTypeDef",
    "SiteTypeDef",
    "ListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef",
    "ListWorkerFleetsRequestRequestTypeDef",
    "WorkerFleetTypeDef",
    "ListWorkersRequestListWorkersPaginateTypeDef",
    "ListWorkersRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateDestinationRequestRequestTypeDef",
    "UpdateDestinationResponseTypeDef",
    "UpdateSiteRequestRequestTypeDef",
    "UpdateSiteResponseTypeDef",
    "UpdateWorkerFleetRequestRequestTypeDef",
    "UpdateWorkerFleetResponseTypeDef",
    "PositionCoordinatesOutputTypeDef",
    "PositionCoordinatesTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListSitesResponseTypeDef",
    "ListWorkerFleetsResponseTypeDef",
    "GetWorkerResponseTypeDef",
    "UpdateWorkerResponseTypeDef",
    "WorkerTypeDef",
    "CreateWorkerRequestRequestTypeDef",
    "UpdateWorkerRequestRequestTypeDef",
    "ListWorkersResponseTypeDef",
)

_RequiredCartesianCoordinatesOutputTypeDef = TypedDict(
    "_RequiredCartesianCoordinatesOutputTypeDef",
    {
        "x": float,
        "y": float,
    },
)
_OptionalCartesianCoordinatesOutputTypeDef = TypedDict(
    "_OptionalCartesianCoordinatesOutputTypeDef",
    {
        "z": float,
    },
    total=False,
)

class CartesianCoordinatesOutputTypeDef(
    _RequiredCartesianCoordinatesOutputTypeDef, _OptionalCartesianCoordinatesOutputTypeDef
):
    pass

_RequiredCartesianCoordinatesTypeDef = TypedDict(
    "_RequiredCartesianCoordinatesTypeDef",
    {
        "x": float,
        "y": float,
    },
)
_OptionalCartesianCoordinatesTypeDef = TypedDict(
    "_OptionalCartesianCoordinatesTypeDef",
    {
        "z": float,
    },
    total=False,
)

class CartesianCoordinatesTypeDef(
    _RequiredCartesianCoordinatesTypeDef, _OptionalCartesianCoordinatesTypeDef
):
    pass

_RequiredCreateDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDestinationRequestRequestTypeDef",
    {
        "name": str,
        "site": str,
    },
)
_OptionalCreateDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDestinationRequestRequestTypeDef",
    {
        "clientToken": str,
        "state": DestinationStateType,
        "additionalFixedProperties": str,
    },
    total=False,
)

class CreateDestinationRequestRequestTypeDef(
    _RequiredCreateDestinationRequestRequestTypeDef, _OptionalCreateDestinationRequestRequestTypeDef
):
    pass

CreateDestinationResponseTypeDef = TypedDict(
    "CreateDestinationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "state": DestinationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSiteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSiteRequestRequestTypeDef",
    {
        "name": str,
        "countryCode": str,
    },
)
_OptionalCreateSiteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSiteRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class CreateSiteRequestRequestTypeDef(
    _RequiredCreateSiteRequestRequestTypeDef, _OptionalCreateSiteRequestRequestTypeDef
):
    pass

CreateSiteResponseTypeDef = TypedDict(
    "CreateSiteResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkerFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkerFleetRequestRequestTypeDef",
    {
        "name": str,
        "site": str,
    },
)
_OptionalCreateWorkerFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkerFleetRequestRequestTypeDef",
    {
        "clientToken": str,
        "additionalFixedProperties": str,
    },
    total=False,
)

class CreateWorkerFleetRequestRequestTypeDef(
    _RequiredCreateWorkerFleetRequestRequestTypeDef, _OptionalCreateWorkerFleetRequestRequestTypeDef
):
    pass

CreateWorkerFleetResponseTypeDef = TypedDict(
    "CreateWorkerFleetResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrientationTypeDef = TypedDict(
    "OrientationTypeDef",
    {
        "degrees": float,
    },
    total=False,
)

_RequiredVendorPropertiesTypeDef = TypedDict(
    "_RequiredVendorPropertiesTypeDef",
    {
        "vendorWorkerId": str,
    },
)
_OptionalVendorPropertiesTypeDef = TypedDict(
    "_OptionalVendorPropertiesTypeDef",
    {
        "vendorWorkerIpAddress": str,
        "vendorAdditionalTransientProperties": str,
        "vendorAdditionalFixedProperties": str,
    },
    total=False,
)

class VendorPropertiesTypeDef(_RequiredVendorPropertiesTypeDef, _OptionalVendorPropertiesTypeDef):
    pass

CreateWorkerResponseTypeDef = TypedDict(
    "CreateWorkerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "site": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDestinationRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteSiteRequestRequestTypeDef = TypedDict(
    "DeleteSiteRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteWorkerFleetRequestRequestTypeDef = TypedDict(
    "DeleteWorkerFleetRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteWorkerRequestRequestTypeDef = TypedDict(
    "DeleteWorkerRequestRequestTypeDef",
    {
        "id": str,
    },
)

_RequiredDestinationTypeDef = TypedDict(
    "_RequiredDestinationTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "state": DestinationStateType,
    },
)
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "additionalFixedProperties": str,
    },
    total=False,
)

class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass

GetDestinationRequestRequestTypeDef = TypedDict(
    "GetDestinationRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetDestinationResponseTypeDef = TypedDict(
    "GetDestinationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "state": DestinationStateType,
        "additionalFixedProperties": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSiteRequestRequestTypeDef = TypedDict(
    "GetSiteRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetSiteResponseTypeDef = TypedDict(
    "GetSiteResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "countryCode": str,
        "description": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkerFleetRequestRequestTypeDef = TypedDict(
    "GetWorkerFleetRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetWorkerFleetResponseTypeDef = TypedDict(
    "GetWorkerFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "additionalFixedProperties": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkerRequestRequestTypeDef = TypedDict(
    "GetWorkerRequestRequestTypeDef",
    {
        "id": str,
    },
)

OrientationOutputTypeDef = TypedDict(
    "OrientationOutputTypeDef",
    {
        "degrees": float,
    },
    total=False,
)

_RequiredVendorPropertiesOutputTypeDef = TypedDict(
    "_RequiredVendorPropertiesOutputTypeDef",
    {
        "vendorWorkerId": str,
    },
)
_OptionalVendorPropertiesOutputTypeDef = TypedDict(
    "_OptionalVendorPropertiesOutputTypeDef",
    {
        "vendorWorkerIpAddress": str,
        "vendorAdditionalTransientProperties": str,
        "vendorAdditionalFixedProperties": str,
    },
    total=False,
)

class VendorPropertiesOutputTypeDef(
    _RequiredVendorPropertiesOutputTypeDef, _OptionalVendorPropertiesOutputTypeDef
):
    pass

_RequiredListDestinationsRequestListDestinationsPaginateTypeDef = TypedDict(
    "_RequiredListDestinationsRequestListDestinationsPaginateTypeDef",
    {
        "site": str,
    },
)
_OptionalListDestinationsRequestListDestinationsPaginateTypeDef = TypedDict(
    "_OptionalListDestinationsRequestListDestinationsPaginateTypeDef",
    {
        "state": DestinationStateType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListDestinationsRequestListDestinationsPaginateTypeDef(
    _RequiredListDestinationsRequestListDestinationsPaginateTypeDef,
    _OptionalListDestinationsRequestListDestinationsPaginateTypeDef,
):
    pass

_RequiredListDestinationsRequestRequestTypeDef = TypedDict(
    "_RequiredListDestinationsRequestRequestTypeDef",
    {
        "site": str,
    },
)
_OptionalListDestinationsRequestRequestTypeDef = TypedDict(
    "_OptionalListDestinationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "state": DestinationStateType,
    },
    total=False,
)

class ListDestinationsRequestRequestTypeDef(
    _RequiredListDestinationsRequestRequestTypeDef, _OptionalListDestinationsRequestRequestTypeDef
):
    pass

ListSitesRequestListSitesPaginateTypeDef = TypedDict(
    "ListSitesRequestListSitesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSitesRequestRequestTypeDef = TypedDict(
    "ListSitesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "arn": str,
        "name": str,
        "countryCode": str,
        "createdAt": datetime,
    },
)

_RequiredListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef = TypedDict(
    "_RequiredListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef",
    {
        "site": str,
    },
)
_OptionalListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef = TypedDict(
    "_OptionalListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef(
    _RequiredListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef,
    _OptionalListWorkerFleetsRequestListWorkerFleetsPaginateTypeDef,
):
    pass

_RequiredListWorkerFleetsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkerFleetsRequestRequestTypeDef",
    {
        "site": str,
    },
)
_OptionalListWorkerFleetsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkerFleetsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListWorkerFleetsRequestRequestTypeDef(
    _RequiredListWorkerFleetsRequestRequestTypeDef, _OptionalListWorkerFleetsRequestRequestTypeDef
):
    pass

_RequiredWorkerFleetTypeDef = TypedDict(
    "_RequiredWorkerFleetTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalWorkerFleetTypeDef = TypedDict(
    "_OptionalWorkerFleetTypeDef",
    {
        "additionalFixedProperties": str,
    },
    total=False,
)

class WorkerFleetTypeDef(_RequiredWorkerFleetTypeDef, _OptionalWorkerFleetTypeDef):
    pass

_RequiredListWorkersRequestListWorkersPaginateTypeDef = TypedDict(
    "_RequiredListWorkersRequestListWorkersPaginateTypeDef",
    {
        "site": str,
    },
)
_OptionalListWorkersRequestListWorkersPaginateTypeDef = TypedDict(
    "_OptionalListWorkersRequestListWorkersPaginateTypeDef",
    {
        "fleet": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListWorkersRequestListWorkersPaginateTypeDef(
    _RequiredListWorkersRequestListWorkersPaginateTypeDef,
    _OptionalListWorkersRequestListWorkersPaginateTypeDef,
):
    pass

_RequiredListWorkersRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkersRequestRequestTypeDef",
    {
        "site": str,
    },
)
_OptionalListWorkersRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "fleet": str,
    },
    total=False,
)

class ListWorkersRequestRequestTypeDef(
    _RequiredListWorkersRequestRequestTypeDef, _OptionalListWorkersRequestRequestTypeDef
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

_RequiredUpdateDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDestinationRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDestinationRequestRequestTypeDef",
    {
        "name": str,
        "state": DestinationStateType,
        "additionalFixedProperties": str,
    },
    total=False,
)

class UpdateDestinationRequestRequestTypeDef(
    _RequiredUpdateDestinationRequestRequestTypeDef, _OptionalUpdateDestinationRequestRequestTypeDef
):
    pass

UpdateDestinationResponseTypeDef = TypedDict(
    "UpdateDestinationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "state": DestinationStateType,
        "additionalFixedProperties": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSiteRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSiteRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateSiteRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSiteRequestRequestTypeDef",
    {
        "name": str,
        "countryCode": str,
        "description": str,
    },
    total=False,
)

class UpdateSiteRequestRequestTypeDef(
    _RequiredUpdateSiteRequestRequestTypeDef, _OptionalUpdateSiteRequestRequestTypeDef
):
    pass

UpdateSiteResponseTypeDef = TypedDict(
    "UpdateSiteResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "countryCode": str,
        "description": str,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkerFleetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkerFleetRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateWorkerFleetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkerFleetRequestRequestTypeDef",
    {
        "name": str,
        "additionalFixedProperties": str,
    },
    total=False,
)

class UpdateWorkerFleetRequestRequestTypeDef(
    _RequiredUpdateWorkerFleetRequestRequestTypeDef, _OptionalUpdateWorkerFleetRequestRequestTypeDef
):
    pass

UpdateWorkerFleetResponseTypeDef = TypedDict(
    "UpdateWorkerFleetResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "additionalFixedProperties": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PositionCoordinatesOutputTypeDef = TypedDict(
    "PositionCoordinatesOutputTypeDef",
    {
        "cartesianCoordinates": CartesianCoordinatesOutputTypeDef,
    },
    total=False,
)

PositionCoordinatesTypeDef = TypedDict(
    "PositionCoordinatesTypeDef",
    {
        "cartesianCoordinates": CartesianCoordinatesTypeDef,
    },
    total=False,
)

ListDestinationsResponseTypeDef = TypedDict(
    "ListDestinationsResponseTypeDef",
    {
        "nextToken": str,
        "destinations": List[DestinationTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSitesResponseTypeDef = TypedDict(
    "ListSitesResponseTypeDef",
    {
        "nextToken": str,
        "sites": List[SiteTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkerFleetsResponseTypeDef = TypedDict(
    "ListWorkerFleetsResponseTypeDef",
    {
        "nextToken": str,
        "workerFleets": List[WorkerFleetTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkerResponseTypeDef = TypedDict(
    "GetWorkerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "fleet": str,
        "site": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "name": str,
        "additionalTransientProperties": str,
        "additionalFixedProperties": str,
        "vendorProperties": VendorPropertiesOutputTypeDef,
        "position": PositionCoordinatesOutputTypeDef,
        "orientation": OrientationOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkerResponseTypeDef = TypedDict(
    "UpdateWorkerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "fleet": str,
        "updatedAt": datetime,
        "name": str,
        "additionalTransientProperties": str,
        "additionalFixedProperties": str,
        "orientation": OrientationOutputTypeDef,
        "vendorProperties": VendorPropertiesOutputTypeDef,
        "position": PositionCoordinatesOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredWorkerTypeDef = TypedDict(
    "_RequiredWorkerTypeDef",
    {
        "arn": str,
        "id": str,
        "fleet": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "name": str,
        "site": str,
    },
)
_OptionalWorkerTypeDef = TypedDict(
    "_OptionalWorkerTypeDef",
    {
        "additionalTransientProperties": str,
        "additionalFixedProperties": str,
        "vendorProperties": VendorPropertiesOutputTypeDef,
        "position": PositionCoordinatesOutputTypeDef,
        "orientation": OrientationOutputTypeDef,
    },
    total=False,
)

class WorkerTypeDef(_RequiredWorkerTypeDef, _OptionalWorkerTypeDef):
    pass

_RequiredCreateWorkerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkerRequestRequestTypeDef",
    {
        "name": str,
        "fleet": str,
    },
)
_OptionalCreateWorkerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkerRequestRequestTypeDef",
    {
        "clientToken": str,
        "additionalTransientProperties": str,
        "additionalFixedProperties": str,
        "vendorProperties": VendorPropertiesTypeDef,
        "position": PositionCoordinatesTypeDef,
        "orientation": OrientationTypeDef,
    },
    total=False,
)

class CreateWorkerRequestRequestTypeDef(
    _RequiredCreateWorkerRequestRequestTypeDef, _OptionalCreateWorkerRequestRequestTypeDef
):
    pass

_RequiredUpdateWorkerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkerRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateWorkerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkerRequestRequestTypeDef",
    {
        "name": str,
        "additionalTransientProperties": str,
        "additionalFixedProperties": str,
        "vendorProperties": VendorPropertiesTypeDef,
        "position": PositionCoordinatesTypeDef,
        "orientation": OrientationTypeDef,
    },
    total=False,
)

class UpdateWorkerRequestRequestTypeDef(
    _RequiredUpdateWorkerRequestRequestTypeDef, _OptionalUpdateWorkerRequestRequestTypeDef
):
    pass

ListWorkersResponseTypeDef = TypedDict(
    "ListWorkersResponseTypeDef",
    {
        "nextToken": str,
        "workers": List[WorkerTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
