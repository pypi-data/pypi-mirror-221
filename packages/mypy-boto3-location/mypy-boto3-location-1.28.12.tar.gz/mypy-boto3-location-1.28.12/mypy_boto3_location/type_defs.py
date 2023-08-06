"""
Type annotations for location service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/type_defs/)

Usage::

    ```python
    from mypy_boto3_location.type_defs import ApiKeyFilterTypeDef

    data: ApiKeyFilterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    BatchItemErrorCodeType,
    DimensionUnitType,
    DistanceUnitType,
    IntendedUseType,
    PositionFilteringType,
    PricingPlanType,
    RouteMatrixErrorCodeType,
    StatusType,
    TravelModeType,
    VehicleWeightUnitType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApiKeyFilterTypeDef",
    "ApiKeyRestrictionsOutputTypeDef",
    "ApiKeyRestrictionsTypeDef",
    "AssociateTrackerConsumerRequestRequestTypeDef",
    "BatchItemErrorTypeDef",
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    "BatchDeleteGeofenceRequestRequestTypeDef",
    "BatchGetDevicePositionRequestRequestTypeDef",
    "BatchPutGeofenceSuccessTypeDef",
    "CalculateRouteCarModeOptionsTypeDef",
    "CalculateRouteMatrixSummaryTypeDef",
    "CalculateRouteSummaryTypeDef",
    "TruckDimensionsTypeDef",
    "TruckWeightTypeDef",
    "CircleOutputTypeDef",
    "CircleTypeDef",
    "CreateGeofenceCollectionRequestRequestTypeDef",
    "CreateGeofenceCollectionResponseTypeDef",
    "CreateKeyResponseTypeDef",
    "MapConfigurationTypeDef",
    "CreateMapResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "CreatePlaceIndexResponseTypeDef",
    "CreateRouteCalculatorRequestRequestTypeDef",
    "CreateRouteCalculatorResponseTypeDef",
    "CreateTrackerRequestRequestTypeDef",
    "CreateTrackerResponseTypeDef",
    "DataSourceConfigurationOutputTypeDef",
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    "DeleteKeyRequestRequestTypeDef",
    "DeleteMapRequestRequestTypeDef",
    "DeletePlaceIndexRequestRequestTypeDef",
    "DeleteRouteCalculatorRequestRequestTypeDef",
    "DeleteTrackerRequestRequestTypeDef",
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    "DescribeGeofenceCollectionResponseTypeDef",
    "DescribeKeyRequestRequestTypeDef",
    "DescribeMapRequestRequestTypeDef",
    "MapConfigurationOutputTypeDef",
    "DescribePlaceIndexRequestRequestTypeDef",
    "DescribeRouteCalculatorRequestRequestTypeDef",
    "DescribeRouteCalculatorResponseTypeDef",
    "DescribeTrackerRequestRequestTypeDef",
    "DescribeTrackerResponseTypeDef",
    "PositionalAccuracyOutputTypeDef",
    "PositionalAccuracyTypeDef",
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    "GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef",
    "GetDevicePositionHistoryRequestRequestTypeDef",
    "GetDevicePositionRequestRequestTypeDef",
    "GetGeofenceRequestRequestTypeDef",
    "GetMapGlyphsRequestRequestTypeDef",
    "GetMapGlyphsResponseTypeDef",
    "GetMapSpritesRequestRequestTypeDef",
    "GetMapSpritesResponseTypeDef",
    "GetMapStyleDescriptorRequestRequestTypeDef",
    "GetMapStyleDescriptorResponseTypeDef",
    "GetMapTileRequestRequestTypeDef",
    "GetMapTileResponseTypeDef",
    "GetPlaceRequestRequestTypeDef",
    "LegGeometryTypeDef",
    "StepTypeDef",
    "ListDevicePositionsRequestListDevicePositionsPaginateTypeDef",
    "ListDevicePositionsRequestRequestTypeDef",
    "ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef",
    "ListGeofenceCollectionsRequestRequestTypeDef",
    "ListGeofenceCollectionsResponseEntryTypeDef",
    "ListGeofencesRequestListGeofencesPaginateTypeDef",
    "ListGeofencesRequestRequestTypeDef",
    "ListMapsRequestListMapsPaginateTypeDef",
    "ListMapsRequestRequestTypeDef",
    "ListMapsResponseEntryTypeDef",
    "ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef",
    "ListPlaceIndexesRequestRequestTypeDef",
    "ListPlaceIndexesResponseEntryTypeDef",
    "ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef",
    "ListRouteCalculatorsRequestRequestTypeDef",
    "ListRouteCalculatorsResponseEntryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef",
    "ListTrackerConsumersRequestRequestTypeDef",
    "ListTrackerConsumersResponseTypeDef",
    "ListTrackersRequestListTrackersPaginateTypeDef",
    "ListTrackersRequestRequestTypeDef",
    "ListTrackersResponseEntryTypeDef",
    "MapConfigurationUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "PlaceGeometryTypeDef",
    "TimeZoneTypeDef",
    "PutGeofenceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RouteMatrixEntryErrorTypeDef",
    "SearchForSuggestionsResultTypeDef",
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    "SearchPlaceIndexForSuggestionsSummaryTypeDef",
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    "UpdateGeofenceCollectionResponseTypeDef",
    "UpdateKeyResponseTypeDef",
    "UpdateMapResponseTypeDef",
    "UpdatePlaceIndexResponseTypeDef",
    "UpdateRouteCalculatorRequestRequestTypeDef",
    "UpdateRouteCalculatorResponseTypeDef",
    "UpdateTrackerRequestRequestTypeDef",
    "UpdateTrackerResponseTypeDef",
    "ListKeysRequestListKeysPaginateTypeDef",
    "ListKeysRequestRequestTypeDef",
    "DescribeKeyResponseTypeDef",
    "ListKeysResponseEntryTypeDef",
    "CreateKeyRequestRequestTypeDef",
    "UpdateKeyRequestRequestTypeDef",
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    "BatchDeleteGeofenceErrorTypeDef",
    "BatchEvaluateGeofencesErrorTypeDef",
    "BatchGetDevicePositionErrorTypeDef",
    "BatchPutGeofenceErrorTypeDef",
    "BatchUpdateDevicePositionErrorTypeDef",
    "CalculateRouteTruckModeOptionsTypeDef",
    "GeofenceGeometryOutputTypeDef",
    "GeofenceGeometryTypeDef",
    "CreateMapRequestRequestTypeDef",
    "CreatePlaceIndexRequestRequestTypeDef",
    "UpdatePlaceIndexRequestRequestTypeDef",
    "DescribePlaceIndexResponseTypeDef",
    "DescribeMapResponseTypeDef",
    "DevicePositionTypeDef",
    "GetDevicePositionResponseTypeDef",
    "ListDevicePositionsResponseEntryTypeDef",
    "DevicePositionUpdateTypeDef",
    "LegTypeDef",
    "ListGeofenceCollectionsResponseTypeDef",
    "ListMapsResponseTypeDef",
    "ListPlaceIndexesResponseTypeDef",
    "ListRouteCalculatorsResponseTypeDef",
    "ListTrackersResponseTypeDef",
    "UpdateMapRequestRequestTypeDef",
    "PlaceTypeDef",
    "RouteMatrixEntryTypeDef",
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    "ListKeysResponseTypeDef",
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    "BatchDeleteGeofenceResponseTypeDef",
    "BatchEvaluateGeofencesResponseTypeDef",
    "BatchPutGeofenceResponseTypeDef",
    "BatchUpdateDevicePositionResponseTypeDef",
    "CalculateRouteMatrixRequestRequestTypeDef",
    "CalculateRouteRequestRequestTypeDef",
    "GetGeofenceResponseTypeDef",
    "ListGeofenceResponseEntryTypeDef",
    "BatchPutGeofenceRequestEntryTypeDef",
    "PutGeofenceRequestRequestTypeDef",
    "BatchGetDevicePositionResponseTypeDef",
    "GetDevicePositionHistoryResponseTypeDef",
    "ListDevicePositionsResponseTypeDef",
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    "CalculateRouteResponseTypeDef",
    "GetPlaceResponseTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForTextResultTypeDef",
    "CalculateRouteMatrixResponseTypeDef",
    "ListGeofencesResponseTypeDef",
    "BatchPutGeofenceRequestRequestTypeDef",
    "SearchPlaceIndexForPositionResponseTypeDef",
    "SearchPlaceIndexForTextResponseTypeDef",
)

ApiKeyFilterTypeDef = TypedDict(
    "ApiKeyFilterTypeDef",
    {
        "KeyStatus": StatusType,
    },
    total=False,
)

_RequiredApiKeyRestrictionsOutputTypeDef = TypedDict(
    "_RequiredApiKeyRestrictionsOutputTypeDef",
    {
        "AllowActions": List[str],
        "AllowResources": List[str],
    },
)
_OptionalApiKeyRestrictionsOutputTypeDef = TypedDict(
    "_OptionalApiKeyRestrictionsOutputTypeDef",
    {
        "AllowReferers": List[str],
    },
    total=False,
)


class ApiKeyRestrictionsOutputTypeDef(
    _RequiredApiKeyRestrictionsOutputTypeDef, _OptionalApiKeyRestrictionsOutputTypeDef
):
    pass


_RequiredApiKeyRestrictionsTypeDef = TypedDict(
    "_RequiredApiKeyRestrictionsTypeDef",
    {
        "AllowActions": Sequence[str],
        "AllowResources": Sequence[str],
    },
)
_OptionalApiKeyRestrictionsTypeDef = TypedDict(
    "_OptionalApiKeyRestrictionsTypeDef",
    {
        "AllowReferers": Sequence[str],
    },
    total=False,
)


class ApiKeyRestrictionsTypeDef(
    _RequiredApiKeyRestrictionsTypeDef, _OptionalApiKeyRestrictionsTypeDef
):
    pass


AssociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "AssociateTrackerConsumerRequestRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
    },
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Code": BatchItemErrorCodeType,
        "Message": str,
    },
    total=False,
)

BatchDeleteDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "TrackerName": str,
    },
)

BatchDeleteGeofenceRequestRequestTypeDef = TypedDict(
    "BatchDeleteGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceIds": Sequence[str],
    },
)

BatchGetDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchGetDevicePositionRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "TrackerName": str,
    },
)

BatchPutGeofenceSuccessTypeDef = TypedDict(
    "BatchPutGeofenceSuccessTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
    },
)

CalculateRouteCarModeOptionsTypeDef = TypedDict(
    "CalculateRouteCarModeOptionsTypeDef",
    {
        "AvoidFerries": bool,
        "AvoidTolls": bool,
    },
    total=False,
)

CalculateRouteMatrixSummaryTypeDef = TypedDict(
    "CalculateRouteMatrixSummaryTypeDef",
    {
        "DataSource": str,
        "DistanceUnit": DistanceUnitType,
        "ErrorCount": int,
        "RouteCount": int,
    },
)

CalculateRouteSummaryTypeDef = TypedDict(
    "CalculateRouteSummaryTypeDef",
    {
        "DataSource": str,
        "Distance": float,
        "DistanceUnit": DistanceUnitType,
        "DurationSeconds": float,
        "RouteBBox": List[float],
    },
)

TruckDimensionsTypeDef = TypedDict(
    "TruckDimensionsTypeDef",
    {
        "Height": float,
        "Length": float,
        "Unit": DimensionUnitType,
        "Width": float,
    },
    total=False,
)

TruckWeightTypeDef = TypedDict(
    "TruckWeightTypeDef",
    {
        "Total": float,
        "Unit": VehicleWeightUnitType,
    },
    total=False,
)

CircleOutputTypeDef = TypedDict(
    "CircleOutputTypeDef",
    {
        "Center": List[float],
        "Radius": float,
    },
)

CircleTypeDef = TypedDict(
    "CircleTypeDef",
    {
        "Center": Sequence[float],
        "Radius": float,
    },
)

_RequiredCreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalCreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGeofenceCollectionRequestRequestTypeDef",
    {
        "Description": str,
        "KmsKeyId": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateGeofenceCollectionRequestRequestTypeDef(
    _RequiredCreateGeofenceCollectionRequestRequestTypeDef,
    _OptionalCreateGeofenceCollectionRequestRequestTypeDef,
):
    pass


CreateGeofenceCollectionResponseTypeDef = TypedDict(
    "CreateGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef",
    {
        "CreateTime": datetime,
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMapConfigurationTypeDef = TypedDict(
    "_RequiredMapConfigurationTypeDef",
    {
        "Style": str,
    },
)
_OptionalMapConfigurationTypeDef = TypedDict(
    "_OptionalMapConfigurationTypeDef",
    {
        "PoliticalView": str,
    },
    total=False,
)


class MapConfigurationTypeDef(_RequiredMapConfigurationTypeDef, _OptionalMapConfigurationTypeDef):
    pass


CreateMapResponseTypeDef = TypedDict(
    "CreateMapResponseTypeDef",
    {
        "CreateTime": datetime,
        "MapArn": str,
        "MapName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "IntendedUse": IntendedUseType,
    },
    total=False,
)

CreatePlaceIndexResponseTypeDef = TypedDict(
    "CreatePlaceIndexResponseTypeDef",
    {
        "CreateTime": datetime,
        "IndexArn": str,
        "IndexName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DataSource": str,
    },
)
_OptionalCreateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRouteCalculatorRequestRequestTypeDef",
    {
        "Description": str,
        "PricingPlan": PricingPlanType,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateRouteCalculatorRequestRequestTypeDef(
    _RequiredCreateRouteCalculatorRequestRequestTypeDef,
    _OptionalCreateRouteCalculatorRequestRequestTypeDef,
):
    pass


CreateRouteCalculatorResponseTypeDef = TypedDict(
    "CreateRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrackerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalCreateTrackerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrackerRequestRequestTypeDef",
    {
        "Description": str,
        "EventBridgeEnabled": bool,
        "KmsKeyId": str,
        "PositionFiltering": PositionFilteringType,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateTrackerRequestRequestTypeDef(
    _RequiredCreateTrackerRequestRequestTypeDef, _OptionalCreateTrackerRequestRequestTypeDef
):
    pass


CreateTrackerResponseTypeDef = TypedDict(
    "CreateTrackerResponseTypeDef",
    {
        "CreateTime": datetime,
        "TrackerArn": str,
        "TrackerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceConfigurationOutputTypeDef = TypedDict(
    "DataSourceConfigurationOutputTypeDef",
    {
        "IntendedUse": IntendedUseType,
    },
    total=False,
)

DeleteGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)

DeleteKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)

DeleteMapRequestRequestTypeDef = TypedDict(
    "DeleteMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)

DeletePlaceIndexRequestRequestTypeDef = TypedDict(
    "DeletePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)

DeleteRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DeleteRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)

DeleteTrackerRequestRequestTypeDef = TypedDict(
    "DeleteTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)

DescribeGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)

DescribeGeofenceCollectionResponseTypeDef = TypedDict(
    "DescribeGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "KmsKeyId": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyRequestRequestTypeDef = TypedDict(
    "DescribeKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)

DescribeMapRequestRequestTypeDef = TypedDict(
    "DescribeMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)

_RequiredMapConfigurationOutputTypeDef = TypedDict(
    "_RequiredMapConfigurationOutputTypeDef",
    {
        "Style": str,
    },
)
_OptionalMapConfigurationOutputTypeDef = TypedDict(
    "_OptionalMapConfigurationOutputTypeDef",
    {
        "PoliticalView": str,
    },
    total=False,
)


class MapConfigurationOutputTypeDef(
    _RequiredMapConfigurationOutputTypeDef, _OptionalMapConfigurationOutputTypeDef
):
    pass


DescribePlaceIndexRequestRequestTypeDef = TypedDict(
    "DescribePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)

DescribeRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DescribeRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)

DescribeRouteCalculatorResponseTypeDef = TypedDict(
    "DescribeRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrackerRequestRequestTypeDef = TypedDict(
    "DescribeTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)

DescribeTrackerResponseTypeDef = TypedDict(
    "DescribeTrackerResponseTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "EventBridgeEnabled": bool,
        "KmsKeyId": str,
        "PositionFiltering": PositionFilteringType,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PositionalAccuracyOutputTypeDef = TypedDict(
    "PositionalAccuracyOutputTypeDef",
    {
        "Horizontal": float,
    },
)

PositionalAccuracyTypeDef = TypedDict(
    "PositionalAccuracyTypeDef",
    {
        "Horizontal": float,
    },
)

DisassociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
    },
)

_RequiredGetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef = TypedDict(
    "_RequiredGetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
    },
)
_OptionalGetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef = TypedDict(
    "_OptionalGetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef",
    {
        "EndTimeExclusive": Union[datetime, str],
        "StartTimeInclusive": Union[datetime, str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef(
    _RequiredGetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef,
    _OptionalGetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef,
):
    pass


_RequiredGetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetDevicePositionHistoryRequestRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
    },
)
_OptionalGetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetDevicePositionHistoryRequestRequestTypeDef",
    {
        "EndTimeExclusive": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "StartTimeInclusive": Union[datetime, str],
    },
    total=False,
)


class GetDevicePositionHistoryRequestRequestTypeDef(
    _RequiredGetDevicePositionHistoryRequestRequestTypeDef,
    _OptionalGetDevicePositionHistoryRequestRequestTypeDef,
):
    pass


GetDevicePositionRequestRequestTypeDef = TypedDict(
    "GetDevicePositionRequestRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
    },
)

GetGeofenceRequestRequestTypeDef = TypedDict(
    "GetGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
    },
)

_RequiredGetMapGlyphsRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapGlyphsRequestRequestTypeDef",
    {
        "FontStack": str,
        "FontUnicodeRange": str,
        "MapName": str,
    },
)
_OptionalGetMapGlyphsRequestRequestTypeDef = TypedDict(
    "_OptionalGetMapGlyphsRequestRequestTypeDef",
    {
        "Key": str,
    },
    total=False,
)


class GetMapGlyphsRequestRequestTypeDef(
    _RequiredGetMapGlyphsRequestRequestTypeDef, _OptionalGetMapGlyphsRequestRequestTypeDef
):
    pass


GetMapGlyphsResponseTypeDef = TypedDict(
    "GetMapGlyphsResponseTypeDef",
    {
        "Blob": StreamingBody,
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapSpritesRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapSpritesRequestRequestTypeDef",
    {
        "FileName": str,
        "MapName": str,
    },
)
_OptionalGetMapSpritesRequestRequestTypeDef = TypedDict(
    "_OptionalGetMapSpritesRequestRequestTypeDef",
    {
        "Key": str,
    },
    total=False,
)


class GetMapSpritesRequestRequestTypeDef(
    _RequiredGetMapSpritesRequestRequestTypeDef, _OptionalGetMapSpritesRequestRequestTypeDef
):
    pass


GetMapSpritesResponseTypeDef = TypedDict(
    "GetMapSpritesResponseTypeDef",
    {
        "Blob": StreamingBody,
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapStyleDescriptorRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapStyleDescriptorRequestRequestTypeDef",
    {
        "MapName": str,
    },
)
_OptionalGetMapStyleDescriptorRequestRequestTypeDef = TypedDict(
    "_OptionalGetMapStyleDescriptorRequestRequestTypeDef",
    {
        "Key": str,
    },
    total=False,
)


class GetMapStyleDescriptorRequestRequestTypeDef(
    _RequiredGetMapStyleDescriptorRequestRequestTypeDef,
    _OptionalGetMapStyleDescriptorRequestRequestTypeDef,
):
    pass


GetMapStyleDescriptorResponseTypeDef = TypedDict(
    "GetMapStyleDescriptorResponseTypeDef",
    {
        "Blob": StreamingBody,
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMapTileRequestRequestTypeDef = TypedDict(
    "_RequiredGetMapTileRequestRequestTypeDef",
    {
        "MapName": str,
        "X": str,
        "Y": str,
        "Z": str,
    },
)
_OptionalGetMapTileRequestRequestTypeDef = TypedDict(
    "_OptionalGetMapTileRequestRequestTypeDef",
    {
        "Key": str,
    },
    total=False,
)


class GetMapTileRequestRequestTypeDef(
    _RequiredGetMapTileRequestRequestTypeDef, _OptionalGetMapTileRequestRequestTypeDef
):
    pass


GetMapTileResponseTypeDef = TypedDict(
    "GetMapTileResponseTypeDef",
    {
        "Blob": StreamingBody,
        "CacheControl": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPlaceRequestRequestTypeDef = TypedDict(
    "_RequiredGetPlaceRequestRequestTypeDef",
    {
        "IndexName": str,
        "PlaceId": str,
    },
)
_OptionalGetPlaceRequestRequestTypeDef = TypedDict(
    "_OptionalGetPlaceRequestRequestTypeDef",
    {
        "Key": str,
        "Language": str,
    },
    total=False,
)


class GetPlaceRequestRequestTypeDef(
    _RequiredGetPlaceRequestRequestTypeDef, _OptionalGetPlaceRequestRequestTypeDef
):
    pass


LegGeometryTypeDef = TypedDict(
    "LegGeometryTypeDef",
    {
        "LineString": List[List[float]],
    },
    total=False,
)

_RequiredStepTypeDef = TypedDict(
    "_RequiredStepTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
    },
)
_OptionalStepTypeDef = TypedDict(
    "_OptionalStepTypeDef",
    {
        "GeometryOffset": int,
    },
    total=False,
)


class StepTypeDef(_RequiredStepTypeDef, _OptionalStepTypeDef):
    pass


_RequiredListDevicePositionsRequestListDevicePositionsPaginateTypeDef = TypedDict(
    "_RequiredListDevicePositionsRequestListDevicePositionsPaginateTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalListDevicePositionsRequestListDevicePositionsPaginateTypeDef = TypedDict(
    "_OptionalListDevicePositionsRequestListDevicePositionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListDevicePositionsRequestListDevicePositionsPaginateTypeDef(
    _RequiredListDevicePositionsRequestListDevicePositionsPaginateTypeDef,
    _OptionalListDevicePositionsRequestListDevicePositionsPaginateTypeDef,
):
    pass


_RequiredListDevicePositionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDevicePositionsRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalListDevicePositionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDevicePositionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDevicePositionsRequestRequestTypeDef(
    _RequiredListDevicePositionsRequestRequestTypeDef,
    _OptionalListDevicePositionsRequestRequestTypeDef,
):
    pass


ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListGeofenceCollectionsRequestRequestTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "_RequiredListGeofenceCollectionsResponseEntryTypeDef",
    {
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "UpdateTime": datetime,
    },
)
_OptionalListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "_OptionalListGeofenceCollectionsResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
    },
    total=False,
)


class ListGeofenceCollectionsResponseEntryTypeDef(
    _RequiredListGeofenceCollectionsResponseEntryTypeDef,
    _OptionalListGeofenceCollectionsResponseEntryTypeDef,
):
    pass


_RequiredListGeofencesRequestListGeofencesPaginateTypeDef = TypedDict(
    "_RequiredListGeofencesRequestListGeofencesPaginateTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalListGeofencesRequestListGeofencesPaginateTypeDef = TypedDict(
    "_OptionalListGeofencesRequestListGeofencesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListGeofencesRequestListGeofencesPaginateTypeDef(
    _RequiredListGeofencesRequestListGeofencesPaginateTypeDef,
    _OptionalListGeofencesRequestListGeofencesPaginateTypeDef,
):
    pass


_RequiredListGeofencesRequestRequestTypeDef = TypedDict(
    "_RequiredListGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalListGeofencesRequestRequestTypeDef = TypedDict(
    "_OptionalListGeofencesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListGeofencesRequestRequestTypeDef(
    _RequiredListGeofencesRequestRequestTypeDef, _OptionalListGeofencesRequestRequestTypeDef
):
    pass


ListMapsRequestListMapsPaginateTypeDef = TypedDict(
    "ListMapsRequestListMapsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListMapsRequestRequestTypeDef = TypedDict(
    "ListMapsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListMapsResponseEntryTypeDef = TypedDict(
    "_RequiredListMapsResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapName": str,
        "UpdateTime": datetime,
    },
)
_OptionalListMapsResponseEntryTypeDef = TypedDict(
    "_OptionalListMapsResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
    },
    total=False,
)


class ListMapsResponseEntryTypeDef(
    _RequiredListMapsResponseEntryTypeDef, _OptionalListMapsResponseEntryTypeDef
):
    pass


ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef = TypedDict(
    "ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListPlaceIndexesRequestRequestTypeDef = TypedDict(
    "ListPlaceIndexesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "_RequiredListPlaceIndexesResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "IndexName": str,
        "UpdateTime": datetime,
    },
)
_OptionalListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "_OptionalListPlaceIndexesResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
    },
    total=False,
)


class ListPlaceIndexesResponseEntryTypeDef(
    _RequiredListPlaceIndexesResponseEntryTypeDef, _OptionalListPlaceIndexesResponseEntryTypeDef
):
    pass


ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef = TypedDict(
    "ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListRouteCalculatorsRequestRequestTypeDef = TypedDict(
    "ListRouteCalculatorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "_RequiredListRouteCalculatorsResponseEntryTypeDef",
    {
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "UpdateTime": datetime,
    },
)
_OptionalListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "_OptionalListRouteCalculatorsResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
    },
    total=False,
)


class ListRouteCalculatorsResponseEntryTypeDef(
    _RequiredListRouteCalculatorsResponseEntryTypeDef,
    _OptionalListRouteCalculatorsResponseEntryTypeDef,
):
    pass


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

_RequiredListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef = TypedDict(
    "_RequiredListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef = TypedDict(
    "_OptionalListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef(
    _RequiredListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef,
    _OptionalListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef,
):
    pass


_RequiredListTrackerConsumersRequestRequestTypeDef = TypedDict(
    "_RequiredListTrackerConsumersRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalListTrackerConsumersRequestRequestTypeDef = TypedDict(
    "_OptionalListTrackerConsumersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListTrackerConsumersRequestRequestTypeDef(
    _RequiredListTrackerConsumersRequestRequestTypeDef,
    _OptionalListTrackerConsumersRequestRequestTypeDef,
):
    pass


ListTrackerConsumersResponseTypeDef = TypedDict(
    "ListTrackerConsumersResponseTypeDef",
    {
        "ConsumerArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrackersRequestListTrackersPaginateTypeDef = TypedDict(
    "ListTrackersRequestListTrackersPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListTrackersRequestRequestTypeDef = TypedDict(
    "ListTrackersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListTrackersResponseEntryTypeDef = TypedDict(
    "_RequiredListTrackersResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "TrackerName": str,
        "UpdateTime": datetime,
    },
)
_OptionalListTrackersResponseEntryTypeDef = TypedDict(
    "_OptionalListTrackersResponseEntryTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
    },
    total=False,
)


class ListTrackersResponseEntryTypeDef(
    _RequiredListTrackersResponseEntryTypeDef, _OptionalListTrackersResponseEntryTypeDef
):
    pass


MapConfigurationUpdateTypeDef = TypedDict(
    "MapConfigurationUpdateTypeDef",
    {
        "PoliticalView": str,
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

PlaceGeometryTypeDef = TypedDict(
    "PlaceGeometryTypeDef",
    {
        "Point": List[float],
    },
    total=False,
)

_RequiredTimeZoneTypeDef = TypedDict(
    "_RequiredTimeZoneTypeDef",
    {
        "Name": str,
    },
)
_OptionalTimeZoneTypeDef = TypedDict(
    "_OptionalTimeZoneTypeDef",
    {
        "Offset": int,
    },
    total=False,
)


class TimeZoneTypeDef(_RequiredTimeZoneTypeDef, _OptionalTimeZoneTypeDef):
    pass


PutGeofenceResponseTypeDef = TypedDict(
    "PutGeofenceResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
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

_RequiredRouteMatrixEntryErrorTypeDef = TypedDict(
    "_RequiredRouteMatrixEntryErrorTypeDef",
    {
        "Code": RouteMatrixErrorCodeType,
    },
)
_OptionalRouteMatrixEntryErrorTypeDef = TypedDict(
    "_OptionalRouteMatrixEntryErrorTypeDef",
    {
        "Message": str,
    },
    total=False,
)


class RouteMatrixEntryErrorTypeDef(
    _RequiredRouteMatrixEntryErrorTypeDef, _OptionalRouteMatrixEntryErrorTypeDef
):
    pass


_RequiredSearchForSuggestionsResultTypeDef = TypedDict(
    "_RequiredSearchForSuggestionsResultTypeDef",
    {
        "Text": str,
    },
)
_OptionalSearchForSuggestionsResultTypeDef = TypedDict(
    "_OptionalSearchForSuggestionsResultTypeDef",
    {
        "Categories": List[str],
        "PlaceId": str,
        "SupplementalCategories": List[str],
    },
    total=False,
)


class SearchForSuggestionsResultTypeDef(
    _RequiredSearchForSuggestionsResultTypeDef, _OptionalSearchForSuggestionsResultTypeDef
):
    pass


_RequiredSearchPlaceIndexForPositionRequestRequestTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForPositionRequestRequestTypeDef",
    {
        "IndexName": str,
        "Position": Sequence[float],
    },
)
_OptionalSearchPlaceIndexForPositionRequestRequestTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForPositionRequestRequestTypeDef",
    {
        "Key": str,
        "Language": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchPlaceIndexForPositionRequestRequestTypeDef(
    _RequiredSearchPlaceIndexForPositionRequestRequestTypeDef,
    _OptionalSearchPlaceIndexForPositionRequestRequestTypeDef,
):
    pass


_RequiredSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForPositionSummaryTypeDef",
    {
        "DataSource": str,
        "Position": List[float],
    },
)
_OptionalSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForPositionSummaryTypeDef",
    {
        "Language": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchPlaceIndexForPositionSummaryTypeDef(
    _RequiredSearchPlaceIndexForPositionSummaryTypeDef,
    _OptionalSearchPlaceIndexForPositionSummaryTypeDef,
):
    pass


_RequiredSearchPlaceIndexForSuggestionsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForSuggestionsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    {
        "BiasPosition": Sequence[float],
        "FilterBBox": Sequence[float],
        "FilterCategories": Sequence[str],
        "FilterCountries": Sequence[str],
        "Key": str,
        "Language": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchPlaceIndexForSuggestionsRequestRequestTypeDef(
    _RequiredSearchPlaceIndexForSuggestionsRequestRequestTypeDef,
    _OptionalSearchPlaceIndexForSuggestionsRequestRequestTypeDef,
):
    pass


_RequiredSearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCategories": List[str],
        "FilterCountries": List[str],
        "Language": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchPlaceIndexForSuggestionsSummaryTypeDef(
    _RequiredSearchPlaceIndexForSuggestionsSummaryTypeDef,
    _OptionalSearchPlaceIndexForSuggestionsSummaryTypeDef,
):
    pass


_RequiredSearchPlaceIndexForTextRequestRequestTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForTextRequestRequestTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForTextRequestRequestTypeDef",
    {
        "BiasPosition": Sequence[float],
        "FilterBBox": Sequence[float],
        "FilterCategories": Sequence[str],
        "FilterCountries": Sequence[str],
        "Key": str,
        "Language": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchPlaceIndexForTextRequestRequestTypeDef(
    _RequiredSearchPlaceIndexForTextRequestRequestTypeDef,
    _OptionalSearchPlaceIndexForTextRequestRequestTypeDef,
):
    pass


_RequiredSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForTextSummaryTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCategories": List[str],
        "FilterCountries": List[str],
        "Language": str,
        "MaxResults": int,
        "ResultBBox": List[float],
    },
    total=False,
)


class SearchPlaceIndexForTextSummaryTypeDef(
    _RequiredSearchPlaceIndexForTextSummaryTypeDef, _OptionalSearchPlaceIndexForTextSummaryTypeDef
):
    pass


TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalUpdateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGeofenceCollectionRequestRequestTypeDef",
    {
        "Description": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
    },
    total=False,
)


class UpdateGeofenceCollectionRequestRequestTypeDef(
    _RequiredUpdateGeofenceCollectionRequestRequestTypeDef,
    _OptionalUpdateGeofenceCollectionRequestRequestTypeDef,
):
    pass


UpdateGeofenceCollectionResponseTypeDef = TypedDict(
    "UpdateGeofenceCollectionResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateKeyResponseTypeDef = TypedDict(
    "UpdateKeyResponseTypeDef",
    {
        "KeyArn": str,
        "KeyName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMapResponseTypeDef = TypedDict(
    "UpdateMapResponseTypeDef",
    {
        "MapArn": str,
        "MapName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePlaceIndexResponseTypeDef = TypedDict(
    "UpdatePlaceIndexResponseTypeDef",
    {
        "IndexArn": str,
        "IndexName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)
_OptionalUpdateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRouteCalculatorRequestRequestTypeDef",
    {
        "Description": str,
        "PricingPlan": PricingPlanType,
    },
    total=False,
)


class UpdateRouteCalculatorRequestRequestTypeDef(
    _RequiredUpdateRouteCalculatorRequestRequestTypeDef,
    _OptionalUpdateRouteCalculatorRequestRequestTypeDef,
):
    pass


UpdateRouteCalculatorResponseTypeDef = TypedDict(
    "UpdateRouteCalculatorResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrackerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalUpdateTrackerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrackerRequestRequestTypeDef",
    {
        "Description": str,
        "EventBridgeEnabled": bool,
        "PositionFiltering": PositionFilteringType,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
    },
    total=False,
)


class UpdateTrackerRequestRequestTypeDef(
    _RequiredUpdateTrackerRequestRequestTypeDef, _OptionalUpdateTrackerRequestRequestTypeDef
):
    pass


UpdateTrackerResponseTypeDef = TypedDict(
    "UpdateTrackerResponseTypeDef",
    {
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeysRequestListKeysPaginateTypeDef = TypedDict(
    "ListKeysRequestListKeysPaginateTypeDef",
    {
        "Filter": ApiKeyFilterTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListKeysRequestRequestTypeDef = TypedDict(
    "ListKeysRequestRequestTypeDef",
    {
        "Filter": ApiKeyFilterTypeDef,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "ExpireTime": datetime,
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsOutputTypeDef,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKeysResponseEntryTypeDef = TypedDict(
    "_RequiredListKeysResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "ExpireTime": datetime,
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsOutputTypeDef,
        "UpdateTime": datetime,
    },
)
_OptionalListKeysResponseEntryTypeDef = TypedDict(
    "_OptionalListKeysResponseEntryTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class ListKeysResponseEntryTypeDef(
    _RequiredListKeysResponseEntryTypeDef, _OptionalListKeysResponseEntryTypeDef
):
    pass


_RequiredCreateKeyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKeyRequestRequestTypeDef",
    {
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsTypeDef,
    },
)
_OptionalCreateKeyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKeyRequestRequestTypeDef",
    {
        "Description": str,
        "ExpireTime": Union[datetime, str],
        "NoExpiry": bool,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateKeyRequestRequestTypeDef(
    _RequiredCreateKeyRequestRequestTypeDef, _OptionalCreateKeyRequestRequestTypeDef
):
    pass


_RequiredUpdateKeyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)
_OptionalUpdateKeyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKeyRequestRequestTypeDef",
    {
        "Description": str,
        "ExpireTime": Union[datetime, str],
        "ForceUpdate": bool,
        "NoExpiry": bool,
        "Restrictions": ApiKeyRestrictionsTypeDef,
    },
    total=False,
)


class UpdateKeyRequestRequestTypeDef(
    _RequiredUpdateKeyRequestRequestTypeDef, _OptionalUpdateKeyRequestRequestTypeDef
):
    pass


BatchDeleteDevicePositionHistoryErrorTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
    },
)

BatchDeleteGeofenceErrorTypeDef = TypedDict(
    "BatchDeleteGeofenceErrorTypeDef",
    {
        "Error": BatchItemErrorTypeDef,
        "GeofenceId": str,
    },
)

BatchEvaluateGeofencesErrorTypeDef = TypedDict(
    "BatchEvaluateGeofencesErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
        "SampleTime": datetime,
    },
)

BatchGetDevicePositionErrorTypeDef = TypedDict(
    "BatchGetDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
    },
)

BatchPutGeofenceErrorTypeDef = TypedDict(
    "BatchPutGeofenceErrorTypeDef",
    {
        "Error": BatchItemErrorTypeDef,
        "GeofenceId": str,
    },
)

BatchUpdateDevicePositionErrorTypeDef = TypedDict(
    "BatchUpdateDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
        "SampleTime": datetime,
    },
)

CalculateRouteTruckModeOptionsTypeDef = TypedDict(
    "CalculateRouteTruckModeOptionsTypeDef",
    {
        "AvoidFerries": bool,
        "AvoidTolls": bool,
        "Dimensions": TruckDimensionsTypeDef,
        "Weight": TruckWeightTypeDef,
    },
    total=False,
)

GeofenceGeometryOutputTypeDef = TypedDict(
    "GeofenceGeometryOutputTypeDef",
    {
        "Circle": CircleOutputTypeDef,
        "Polygon": List[List[List[float]]],
    },
    total=False,
)

GeofenceGeometryTypeDef = TypedDict(
    "GeofenceGeometryTypeDef",
    {
        "Circle": CircleTypeDef,
        "Polygon": Sequence[Sequence[Sequence[float]]],
    },
    total=False,
)

_RequiredCreateMapRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMapRequestRequestTypeDef",
    {
        "Configuration": MapConfigurationTypeDef,
        "MapName": str,
    },
)
_OptionalCreateMapRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMapRequestRequestTypeDef",
    {
        "Description": str,
        "PricingPlan": PricingPlanType,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreateMapRequestRequestTypeDef(
    _RequiredCreateMapRequestRequestTypeDef, _OptionalCreateMapRequestRequestTypeDef
):
    pass


_RequiredCreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePlaceIndexRequestRequestTypeDef",
    {
        "DataSource": str,
        "IndexName": str,
    },
)
_OptionalCreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePlaceIndexRequestRequestTypeDef",
    {
        "DataSourceConfiguration": DataSourceConfigurationTypeDef,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class CreatePlaceIndexRequestRequestTypeDef(
    _RequiredCreatePlaceIndexRequestRequestTypeDef, _OptionalCreatePlaceIndexRequestRequestTypeDef
):
    pass


_RequiredUpdatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalUpdatePlaceIndexRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePlaceIndexRequestRequestTypeDef",
    {
        "DataSourceConfiguration": DataSourceConfigurationTypeDef,
        "Description": str,
        "PricingPlan": PricingPlanType,
    },
    total=False,
)


class UpdatePlaceIndexRequestRequestTypeDef(
    _RequiredUpdatePlaceIndexRequestRequestTypeDef, _OptionalUpdatePlaceIndexRequestRequestTypeDef
):
    pass


DescribePlaceIndexResponseTypeDef = TypedDict(
    "DescribePlaceIndexResponseTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "DataSourceConfiguration": DataSourceConfigurationOutputTypeDef,
        "Description": str,
        "IndexArn": str,
        "IndexName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMapResponseTypeDef = TypedDict(
    "DescribeMapResponseTypeDef",
    {
        "Configuration": MapConfigurationOutputTypeDef,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapArn": str,
        "MapName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDevicePositionTypeDef = TypedDict(
    "_RequiredDevicePositionTypeDef",
    {
        "Position": List[float],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
    },
)
_OptionalDevicePositionTypeDef = TypedDict(
    "_OptionalDevicePositionTypeDef",
    {
        "Accuracy": PositionalAccuracyOutputTypeDef,
        "DeviceId": str,
        "PositionProperties": Dict[str, str],
    },
    total=False,
)


class DevicePositionTypeDef(_RequiredDevicePositionTypeDef, _OptionalDevicePositionTypeDef):
    pass


GetDevicePositionResponseTypeDef = TypedDict(
    "GetDevicePositionResponseTypeDef",
    {
        "Accuracy": PositionalAccuracyOutputTypeDef,
        "DeviceId": str,
        "Position": List[float],
        "PositionProperties": Dict[str, str],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDevicePositionsResponseEntryTypeDef = TypedDict(
    "_RequiredListDevicePositionsResponseEntryTypeDef",
    {
        "DeviceId": str,
        "Position": List[float],
        "SampleTime": datetime,
    },
)
_OptionalListDevicePositionsResponseEntryTypeDef = TypedDict(
    "_OptionalListDevicePositionsResponseEntryTypeDef",
    {
        "Accuracy": PositionalAccuracyOutputTypeDef,
        "PositionProperties": Dict[str, str],
    },
    total=False,
)


class ListDevicePositionsResponseEntryTypeDef(
    _RequiredListDevicePositionsResponseEntryTypeDef,
    _OptionalListDevicePositionsResponseEntryTypeDef,
):
    pass


_RequiredDevicePositionUpdateTypeDef = TypedDict(
    "_RequiredDevicePositionUpdateTypeDef",
    {
        "DeviceId": str,
        "Position": Sequence[float],
        "SampleTime": Union[datetime, str],
    },
)
_OptionalDevicePositionUpdateTypeDef = TypedDict(
    "_OptionalDevicePositionUpdateTypeDef",
    {
        "Accuracy": PositionalAccuracyTypeDef,
        "PositionProperties": Mapping[str, str],
    },
    total=False,
)


class DevicePositionUpdateTypeDef(
    _RequiredDevicePositionUpdateTypeDef, _OptionalDevicePositionUpdateTypeDef
):
    pass


_RequiredLegTypeDef = TypedDict(
    "_RequiredLegTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
        "Steps": List[StepTypeDef],
    },
)
_OptionalLegTypeDef = TypedDict(
    "_OptionalLegTypeDef",
    {
        "Geometry": LegGeometryTypeDef,
    },
    total=False,
)


class LegTypeDef(_RequiredLegTypeDef, _OptionalLegTypeDef):
    pass


ListGeofenceCollectionsResponseTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseTypeDef",
    {
        "Entries": List[ListGeofenceCollectionsResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMapsResponseTypeDef = TypedDict(
    "ListMapsResponseTypeDef",
    {
        "Entries": List[ListMapsResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaceIndexesResponseTypeDef = TypedDict(
    "ListPlaceIndexesResponseTypeDef",
    {
        "Entries": List[ListPlaceIndexesResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRouteCalculatorsResponseTypeDef = TypedDict(
    "ListRouteCalculatorsResponseTypeDef",
    {
        "Entries": List[ListRouteCalculatorsResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrackersResponseTypeDef = TypedDict(
    "ListTrackersResponseTypeDef",
    {
        "Entries": List[ListTrackersResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMapRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)
_OptionalUpdateMapRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMapRequestRequestTypeDef",
    {
        "ConfigurationUpdate": MapConfigurationUpdateTypeDef,
        "Description": str,
        "PricingPlan": PricingPlanType,
    },
    total=False,
)


class UpdateMapRequestRequestTypeDef(
    _RequiredUpdateMapRequestRequestTypeDef, _OptionalUpdateMapRequestRequestTypeDef
):
    pass


_RequiredPlaceTypeDef = TypedDict(
    "_RequiredPlaceTypeDef",
    {
        "Geometry": PlaceGeometryTypeDef,
    },
)
_OptionalPlaceTypeDef = TypedDict(
    "_OptionalPlaceTypeDef",
    {
        "AddressNumber": str,
        "Categories": List[str],
        "Country": str,
        "Interpolated": bool,
        "Label": str,
        "Municipality": str,
        "Neighborhood": str,
        "PostalCode": str,
        "Region": str,
        "Street": str,
        "SubRegion": str,
        "SupplementalCategories": List[str],
        "TimeZone": TimeZoneTypeDef,
        "UnitNumber": str,
        "UnitType": str,
    },
    total=False,
)


class PlaceTypeDef(_RequiredPlaceTypeDef, _OptionalPlaceTypeDef):
    pass


RouteMatrixEntryTypeDef = TypedDict(
    "RouteMatrixEntryTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "Error": RouteMatrixEntryErrorTypeDef,
    },
    total=False,
)

SearchPlaceIndexForSuggestionsResponseTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    {
        "Results": List[SearchForSuggestionsResultTypeDef],
        "Summary": SearchPlaceIndexForSuggestionsSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "Entries": List[ListKeysResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteDevicePositionHistoryResponseTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    {
        "Errors": List[BatchDeleteDevicePositionHistoryErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteGeofenceResponseTypeDef = TypedDict(
    "BatchDeleteGeofenceResponseTypeDef",
    {
        "Errors": List[BatchDeleteGeofenceErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEvaluateGeofencesResponseTypeDef = TypedDict(
    "BatchEvaluateGeofencesResponseTypeDef",
    {
        "Errors": List[BatchEvaluateGeofencesErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutGeofenceResponseTypeDef = TypedDict(
    "BatchPutGeofenceResponseTypeDef",
    {
        "Errors": List[BatchPutGeofenceErrorTypeDef],
        "Successes": List[BatchPutGeofenceSuccessTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateDevicePositionResponseTypeDef = TypedDict(
    "BatchUpdateDevicePositionResponseTypeDef",
    {
        "Errors": List[BatchUpdateDevicePositionErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCalculateRouteMatrixRequestRequestTypeDef = TypedDict(
    "_RequiredCalculateRouteMatrixRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePositions": Sequence[Sequence[float]],
        "DestinationPositions": Sequence[Sequence[float]],
    },
)
_OptionalCalculateRouteMatrixRequestRequestTypeDef = TypedDict(
    "_OptionalCalculateRouteMatrixRequestRequestTypeDef",
    {
        "CarModeOptions": CalculateRouteCarModeOptionsTypeDef,
        "DepartNow": bool,
        "DepartureTime": Union[datetime, str],
        "DistanceUnit": DistanceUnitType,
        "Key": str,
        "TravelMode": TravelModeType,
        "TruckModeOptions": CalculateRouteTruckModeOptionsTypeDef,
    },
    total=False,
)


class CalculateRouteMatrixRequestRequestTypeDef(
    _RequiredCalculateRouteMatrixRequestRequestTypeDef,
    _OptionalCalculateRouteMatrixRequestRequestTypeDef,
):
    pass


_RequiredCalculateRouteRequestRequestTypeDef = TypedDict(
    "_RequiredCalculateRouteRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePosition": Sequence[float],
        "DestinationPosition": Sequence[float],
    },
)
_OptionalCalculateRouteRequestRequestTypeDef = TypedDict(
    "_OptionalCalculateRouteRequestRequestTypeDef",
    {
        "CarModeOptions": CalculateRouteCarModeOptionsTypeDef,
        "DepartNow": bool,
        "DepartureTime": Union[datetime, str],
        "DistanceUnit": DistanceUnitType,
        "IncludeLegGeometry": bool,
        "Key": str,
        "TravelMode": TravelModeType,
        "TruckModeOptions": CalculateRouteTruckModeOptionsTypeDef,
        "WaypointPositions": Sequence[Sequence[float]],
    },
    total=False,
)


class CalculateRouteRequestRequestTypeDef(
    _RequiredCalculateRouteRequestRequestTypeDef, _OptionalCalculateRouteRequestRequestTypeDef
):
    pass


GetGeofenceResponseTypeDef = TypedDict(
    "GetGeofenceResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "GeofenceProperties": Dict[str, str],
        "Geometry": GeofenceGeometryOutputTypeDef,
        "Status": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGeofenceResponseEntryTypeDef = TypedDict(
    "_RequiredListGeofenceResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": GeofenceGeometryOutputTypeDef,
        "Status": str,
        "UpdateTime": datetime,
    },
)
_OptionalListGeofenceResponseEntryTypeDef = TypedDict(
    "_OptionalListGeofenceResponseEntryTypeDef",
    {
        "GeofenceProperties": Dict[str, str],
    },
    total=False,
)


class ListGeofenceResponseEntryTypeDef(
    _RequiredListGeofenceResponseEntryTypeDef, _OptionalListGeofenceResponseEntryTypeDef
):
    pass


_RequiredBatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "_RequiredBatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": GeofenceGeometryTypeDef,
    },
)
_OptionalBatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "_OptionalBatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceProperties": Mapping[str, str],
    },
    total=False,
)


class BatchPutGeofenceRequestEntryTypeDef(
    _RequiredBatchPutGeofenceRequestEntryTypeDef, _OptionalBatchPutGeofenceRequestEntryTypeDef
):
    pass


_RequiredPutGeofenceRequestRequestTypeDef = TypedDict(
    "_RequiredPutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
        "Geometry": GeofenceGeometryTypeDef,
    },
)
_OptionalPutGeofenceRequestRequestTypeDef = TypedDict(
    "_OptionalPutGeofenceRequestRequestTypeDef",
    {
        "GeofenceProperties": Mapping[str, str],
    },
    total=False,
)


class PutGeofenceRequestRequestTypeDef(
    _RequiredPutGeofenceRequestRequestTypeDef, _OptionalPutGeofenceRequestRequestTypeDef
):
    pass


BatchGetDevicePositionResponseTypeDef = TypedDict(
    "BatchGetDevicePositionResponseTypeDef",
    {
        "DevicePositions": List[DevicePositionTypeDef],
        "Errors": List[BatchGetDevicePositionErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicePositionHistoryResponseTypeDef = TypedDict(
    "GetDevicePositionHistoryResponseTypeDef",
    {
        "DevicePositions": List[DevicePositionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicePositionsResponseTypeDef = TypedDict(
    "ListDevicePositionsResponseTypeDef",
    {
        "Entries": List[ListDevicePositionsResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEvaluateGeofencesRequestRequestTypeDef = TypedDict(
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
        "DevicePositionUpdates": Sequence[DevicePositionUpdateTypeDef],
    },
)

BatchUpdateDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Updates": Sequence[DevicePositionUpdateTypeDef],
    },
)

CalculateRouteResponseTypeDef = TypedDict(
    "CalculateRouteResponseTypeDef",
    {
        "Legs": List[LegTypeDef],
        "Summary": CalculateRouteSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlaceResponseTypeDef = TypedDict(
    "GetPlaceResponseTypeDef",
    {
        "Place": PlaceTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchForPositionResultTypeDef = TypedDict(
    "_RequiredSearchForPositionResultTypeDef",
    {
        "Distance": float,
        "Place": PlaceTypeDef,
    },
)
_OptionalSearchForPositionResultTypeDef = TypedDict(
    "_OptionalSearchForPositionResultTypeDef",
    {
        "PlaceId": str,
    },
    total=False,
)


class SearchForPositionResultTypeDef(
    _RequiredSearchForPositionResultTypeDef, _OptionalSearchForPositionResultTypeDef
):
    pass


_RequiredSearchForTextResultTypeDef = TypedDict(
    "_RequiredSearchForTextResultTypeDef",
    {
        "Place": PlaceTypeDef,
    },
)
_OptionalSearchForTextResultTypeDef = TypedDict(
    "_OptionalSearchForTextResultTypeDef",
    {
        "Distance": float,
        "PlaceId": str,
        "Relevance": float,
    },
    total=False,
)


class SearchForTextResultTypeDef(
    _RequiredSearchForTextResultTypeDef, _OptionalSearchForTextResultTypeDef
):
    pass


CalculateRouteMatrixResponseTypeDef = TypedDict(
    "CalculateRouteMatrixResponseTypeDef",
    {
        "RouteMatrix": List[List[RouteMatrixEntryTypeDef]],
        "SnappedDeparturePositions": List[List[float]],
        "SnappedDestinationPositions": List[List[float]],
        "Summary": CalculateRouteMatrixSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeofencesResponseTypeDef = TypedDict(
    "ListGeofencesResponseTypeDef",
    {
        "Entries": List[ListGeofenceResponseEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutGeofenceRequestRequestTypeDef = TypedDict(
    "BatchPutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Entries": Sequence[BatchPutGeofenceRequestEntryTypeDef],
    },
)

SearchPlaceIndexForPositionResponseTypeDef = TypedDict(
    "SearchPlaceIndexForPositionResponseTypeDef",
    {
        "Results": List[SearchForPositionResultTypeDef],
        "Summary": SearchPlaceIndexForPositionSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchPlaceIndexForTextResponseTypeDef = TypedDict(
    "SearchPlaceIndexForTextResponseTypeDef",
    {
        "Results": List[SearchForTextResultTypeDef],
        "Summary": SearchPlaceIndexForTextSummaryTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
