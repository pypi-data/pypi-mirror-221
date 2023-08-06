"""
Type annotations for sagemaker-geospatial service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_geospatial/type_defs/)

Usage::

    ```python
    from mypy_boto3_sagemaker_geospatial.type_defs import MultiPolygonGeometryInputOutputTypeDef

    data: MultiPolygonGeometryInputOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AlgorithmNameGeoMosaicType,
    AlgorithmNameResamplingType,
    ComparisonOperatorType,
    DataCollectionTypeType,
    EarthObservationJobErrorTypeType,
    EarthObservationJobExportStatusType,
    EarthObservationJobStatusType,
    ExportErrorTypeType,
    GroupByType,
    OutputTypeType,
    PredefinedResolutionType,
    SortOrderType,
    TargetOptionsType,
    TemporalStatisticsType,
    VectorEnrichmentJobErrorTypeType,
    VectorEnrichmentJobExportErrorTypeType,
    VectorEnrichmentJobExportStatusType,
    VectorEnrichmentJobStatusType,
    VectorEnrichmentJobTypeType,
    ZonalStatisticsType,
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
    "MultiPolygonGeometryInputOutputTypeDef",
    "PolygonGeometryInputOutputTypeDef",
    "MultiPolygonGeometryInputTypeDef",
    "PolygonGeometryInputTypeDef",
    "AssetValueTypeDef",
    "CloudRemovalConfigInputOutputTypeDef",
    "CloudRemovalConfigInputTypeDef",
    "OperationOutputTypeDef",
    "OperationTypeDef",
    "DeleteEarthObservationJobInputRequestTypeDef",
    "DeleteVectorEnrichmentJobInputRequestTypeDef",
    "EarthObservationJobErrorDetailsTypeDef",
    "EoCloudCoverInputOutputTypeDef",
    "EoCloudCoverInputTypeDef",
    "ResponseMetadataTypeDef",
    "ExportErrorDetailsOutputTypeDef",
    "ExportS3DataInputOutputTypeDef",
    "ExportS3DataInputTypeDef",
    "VectorEnrichmentJobS3DataOutputTypeDef",
    "VectorEnrichmentJobS3DataTypeDef",
    "FilterTypeDef",
    "GeoMosaicConfigInputOutputTypeDef",
    "GeoMosaicConfigInputTypeDef",
    "GeometryTypeDef",
    "GetEarthObservationJobInputRequestTypeDef",
    "OutputBandTypeDef",
    "GetRasterDataCollectionInputRequestTypeDef",
    "GetTileInputRequestTypeDef",
    "GetVectorEnrichmentJobInputRequestTypeDef",
    "VectorEnrichmentJobErrorDetailsTypeDef",
    "VectorEnrichmentJobExportErrorDetailsTypeDef",
    "PropertiesTypeDef",
    "TemporalStatisticsConfigInputOutputTypeDef",
    "ZonalStatisticsConfigInputOutputTypeDef",
    "TemporalStatisticsConfigInputTypeDef",
    "ZonalStatisticsConfigInputTypeDef",
    "LandsatCloudCoverLandInputOutputTypeDef",
    "LandsatCloudCoverLandInputTypeDef",
    "PaginatorConfigTypeDef",
    "ListEarthObservationJobInputRequestTypeDef",
    "ListEarthObservationJobOutputConfigTypeDef",
    "ListRasterDataCollectionsInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVectorEnrichmentJobInputRequestTypeDef",
    "ListVectorEnrichmentJobOutputConfigTypeDef",
    "MapMatchingConfigOutputTypeDef",
    "MapMatchingConfigTypeDef",
    "UserDefinedOutputTypeDef",
    "UserDefinedTypeDef",
    "PlatformInputOutputTypeDef",
    "PlatformInputTypeDef",
    "ViewOffNadirInputOutputTypeDef",
    "ViewSunAzimuthInputOutputTypeDef",
    "ViewSunElevationInputOutputTypeDef",
    "ViewOffNadirInputTypeDef",
    "ViewSunAzimuthInputTypeDef",
    "ViewSunElevationInputTypeDef",
    "TimeRangeFilterInputTypeDef",
    "TimeRangeFilterOutputTypeDef",
    "ReverseGeocodingConfigOutputTypeDef",
    "ReverseGeocodingConfigTypeDef",
    "StopEarthObservationJobInputRequestTypeDef",
    "StopVectorEnrichmentJobInputRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AreaOfInterestGeometryOutputTypeDef",
    "AreaOfInterestGeometryTypeDef",
    "CustomIndicesInputOutputTypeDef",
    "CustomIndicesInputTypeDef",
    "GetTileOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ExportErrorDetailsTypeDef",
    "OutputConfigInputOutputTypeDef",
    "OutputConfigInputTypeDef",
    "ExportVectorEnrichmentJobOutputConfigOutputTypeDef",
    "VectorEnrichmentJobDataSourceConfigInputOutputTypeDef",
    "ExportVectorEnrichmentJobOutputConfigTypeDef",
    "VectorEnrichmentJobDataSourceConfigInputTypeDef",
    "GetRasterDataCollectionOutputTypeDef",
    "RasterDataCollectionMetadataTypeDef",
    "ItemSourceTypeDef",
    "ListEarthObservationJobInputListEarthObservationJobsPaginateTypeDef",
    "ListRasterDataCollectionsInputListRasterDataCollectionsPaginateTypeDef",
    "ListVectorEnrichmentJobInputListVectorEnrichmentJobsPaginateTypeDef",
    "ListEarthObservationJobOutputTypeDef",
    "ListVectorEnrichmentJobOutputTypeDef",
    "OutputResolutionResamplingInputOutputTypeDef",
    "OutputResolutionStackInputOutputTypeDef",
    "OutputResolutionResamplingInputTypeDef",
    "OutputResolutionStackInputTypeDef",
    "PropertyOutputTypeDef",
    "PropertyTypeDef",
    "VectorEnrichmentJobConfigOutputTypeDef",
    "VectorEnrichmentJobConfigTypeDef",
    "AreaOfInterestOutputTypeDef",
    "AreaOfInterestTypeDef",
    "BandMathConfigInputOutputTypeDef",
    "BandMathConfigInputTypeDef",
    "ExportEarthObservationJobOutputTypeDef",
    "ExportEarthObservationJobInputRequestTypeDef",
    "ExportVectorEnrichmentJobOutputTypeDef",
    "VectorEnrichmentJobInputConfigOutputTypeDef",
    "ExportVectorEnrichmentJobInputRequestTypeDef",
    "VectorEnrichmentJobInputConfigTypeDef",
    "ListRasterDataCollectionsOutputTypeDef",
    "SearchRasterDataCollectionOutputTypeDef",
    "ResamplingConfigInputOutputTypeDef",
    "StackConfigInputOutputTypeDef",
    "ResamplingConfigInputTypeDef",
    "StackConfigInputTypeDef",
    "PropertyFilterOutputTypeDef",
    "PropertyFilterTypeDef",
    "GetVectorEnrichmentJobOutputTypeDef",
    "StartVectorEnrichmentJobOutputTypeDef",
    "StartVectorEnrichmentJobInputRequestTypeDef",
    "JobConfigInputOutputTypeDef",
    "JobConfigInputTypeDef",
    "PropertyFiltersOutputTypeDef",
    "PropertyFiltersTypeDef",
    "RasterDataCollectionQueryOutputTypeDef",
    "RasterDataCollectionQueryInputTypeDef",
    "RasterDataCollectionQueryWithBandFilterInputTypeDef",
    "InputConfigOutputTypeDef",
    "InputConfigInputTypeDef",
    "SearchRasterDataCollectionInputRequestTypeDef",
    "GetEarthObservationJobOutputTypeDef",
    "StartEarthObservationJobOutputTypeDef",
    "StartEarthObservationJobInputRequestTypeDef",
)

MultiPolygonGeometryInputOutputTypeDef = TypedDict(
    "MultiPolygonGeometryInputOutputTypeDef",
    {
        "Coordinates": List[List[List[List[float]]]],
    },
)

PolygonGeometryInputOutputTypeDef = TypedDict(
    "PolygonGeometryInputOutputTypeDef",
    {
        "Coordinates": List[List[List[float]]],
    },
)

MultiPolygonGeometryInputTypeDef = TypedDict(
    "MultiPolygonGeometryInputTypeDef",
    {
        "Coordinates": Sequence[Sequence[Sequence[Sequence[float]]]],
    },
)

PolygonGeometryInputTypeDef = TypedDict(
    "PolygonGeometryInputTypeDef",
    {
        "Coordinates": Sequence[Sequence[Sequence[float]]],
    },
)

AssetValueTypeDef = TypedDict(
    "AssetValueTypeDef",
    {
        "Href": str,
    },
    total=False,
)

CloudRemovalConfigInputOutputTypeDef = TypedDict(
    "CloudRemovalConfigInputOutputTypeDef",
    {
        "AlgorithmName": Literal["INTERPOLATION"],
        "InterpolationValue": str,
        "TargetBands": List[str],
    },
    total=False,
)

CloudRemovalConfigInputTypeDef = TypedDict(
    "CloudRemovalConfigInputTypeDef",
    {
        "AlgorithmName": Literal["INTERPOLATION"],
        "InterpolationValue": str,
        "TargetBands": Sequence[str],
    },
    total=False,
)

_RequiredOperationOutputTypeDef = TypedDict(
    "_RequiredOperationOutputTypeDef",
    {
        "Equation": str,
        "Name": str,
    },
)
_OptionalOperationOutputTypeDef = TypedDict(
    "_OptionalOperationOutputTypeDef",
    {
        "OutputType": OutputTypeType,
    },
    total=False,
)


class OperationOutputTypeDef(_RequiredOperationOutputTypeDef, _OptionalOperationOutputTypeDef):
    pass


_RequiredOperationTypeDef = TypedDict(
    "_RequiredOperationTypeDef",
    {
        "Equation": str,
        "Name": str,
    },
)
_OptionalOperationTypeDef = TypedDict(
    "_OptionalOperationTypeDef",
    {
        "OutputType": OutputTypeType,
    },
    total=False,
)


class OperationTypeDef(_RequiredOperationTypeDef, _OptionalOperationTypeDef):
    pass


DeleteEarthObservationJobInputRequestTypeDef = TypedDict(
    "DeleteEarthObservationJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "DeleteVectorEnrichmentJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

EarthObservationJobErrorDetailsTypeDef = TypedDict(
    "EarthObservationJobErrorDetailsTypeDef",
    {
        "Message": str,
        "Type": EarthObservationJobErrorTypeType,
    },
    total=False,
)

EoCloudCoverInputOutputTypeDef = TypedDict(
    "EoCloudCoverInputOutputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

EoCloudCoverInputTypeDef = TypedDict(
    "EoCloudCoverInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
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

ExportErrorDetailsOutputTypeDef = TypedDict(
    "ExportErrorDetailsOutputTypeDef",
    {
        "Message": str,
        "Type": ExportErrorTypeType,
    },
    total=False,
)

_RequiredExportS3DataInputOutputTypeDef = TypedDict(
    "_RequiredExportS3DataInputOutputTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalExportS3DataInputOutputTypeDef = TypedDict(
    "_OptionalExportS3DataInputOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class ExportS3DataInputOutputTypeDef(
    _RequiredExportS3DataInputOutputTypeDef, _OptionalExportS3DataInputOutputTypeDef
):
    pass


_RequiredExportS3DataInputTypeDef = TypedDict(
    "_RequiredExportS3DataInputTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalExportS3DataInputTypeDef = TypedDict(
    "_OptionalExportS3DataInputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class ExportS3DataInputTypeDef(
    _RequiredExportS3DataInputTypeDef, _OptionalExportS3DataInputTypeDef
):
    pass


_RequiredVectorEnrichmentJobS3DataOutputTypeDef = TypedDict(
    "_RequiredVectorEnrichmentJobS3DataOutputTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalVectorEnrichmentJobS3DataOutputTypeDef = TypedDict(
    "_OptionalVectorEnrichmentJobS3DataOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class VectorEnrichmentJobS3DataOutputTypeDef(
    _RequiredVectorEnrichmentJobS3DataOutputTypeDef, _OptionalVectorEnrichmentJobS3DataOutputTypeDef
):
    pass


_RequiredVectorEnrichmentJobS3DataTypeDef = TypedDict(
    "_RequiredVectorEnrichmentJobS3DataTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalVectorEnrichmentJobS3DataTypeDef = TypedDict(
    "_OptionalVectorEnrichmentJobS3DataTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class VectorEnrichmentJobS3DataTypeDef(
    _RequiredVectorEnrichmentJobS3DataTypeDef, _OptionalVectorEnrichmentJobS3DataTypeDef
):
    pass


_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "Maximum": float,
        "Minimum": float,
    },
    total=False,
)


class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass


GeoMosaicConfigInputOutputTypeDef = TypedDict(
    "GeoMosaicConfigInputOutputTypeDef",
    {
        "AlgorithmName": AlgorithmNameGeoMosaicType,
        "TargetBands": List[str],
    },
    total=False,
)

GeoMosaicConfigInputTypeDef = TypedDict(
    "GeoMosaicConfigInputTypeDef",
    {
        "AlgorithmName": AlgorithmNameGeoMosaicType,
        "TargetBands": Sequence[str],
    },
    total=False,
)

GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {
        "Coordinates": List[List[List[float]]],
        "Type": str,
    },
)

GetEarthObservationJobInputRequestTypeDef = TypedDict(
    "GetEarthObservationJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

OutputBandTypeDef = TypedDict(
    "OutputBandTypeDef",
    {
        "BandName": str,
        "OutputDataType": OutputTypeType,
    },
)

GetRasterDataCollectionInputRequestTypeDef = TypedDict(
    "GetRasterDataCollectionInputRequestTypeDef",
    {
        "Arn": str,
    },
)

_RequiredGetTileInputRequestTypeDef = TypedDict(
    "_RequiredGetTileInputRequestTypeDef",
    {
        "Arn": str,
        "ImageAssets": Sequence[str],
        "Target": TargetOptionsType,
        "x": int,
        "y": int,
        "z": int,
    },
)
_OptionalGetTileInputRequestTypeDef = TypedDict(
    "_OptionalGetTileInputRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "ImageMask": bool,
        "OutputDataType": OutputTypeType,
        "OutputFormat": str,
        "PropertyFilters": str,
        "TimeRangeFilter": str,
    },
    total=False,
)


class GetTileInputRequestTypeDef(
    _RequiredGetTileInputRequestTypeDef, _OptionalGetTileInputRequestTypeDef
):
    pass


GetVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "GetVectorEnrichmentJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

VectorEnrichmentJobErrorDetailsTypeDef = TypedDict(
    "VectorEnrichmentJobErrorDetailsTypeDef",
    {
        "ErrorMessage": str,
        "ErrorType": VectorEnrichmentJobErrorTypeType,
    },
    total=False,
)

VectorEnrichmentJobExportErrorDetailsTypeDef = TypedDict(
    "VectorEnrichmentJobExportErrorDetailsTypeDef",
    {
        "Message": str,
        "Type": VectorEnrichmentJobExportErrorTypeType,
    },
    total=False,
)

PropertiesTypeDef = TypedDict(
    "PropertiesTypeDef",
    {
        "EoCloudCover": float,
        "LandsatCloudCoverLand": float,
        "Platform": str,
        "ViewOffNadir": float,
        "ViewSunAzimuth": float,
        "ViewSunElevation": float,
    },
    total=False,
)

_RequiredTemporalStatisticsConfigInputOutputTypeDef = TypedDict(
    "_RequiredTemporalStatisticsConfigInputOutputTypeDef",
    {
        "Statistics": List[TemporalStatisticsType],
    },
)
_OptionalTemporalStatisticsConfigInputOutputTypeDef = TypedDict(
    "_OptionalTemporalStatisticsConfigInputOutputTypeDef",
    {
        "GroupBy": GroupByType,
        "TargetBands": List[str],
    },
    total=False,
)


class TemporalStatisticsConfigInputOutputTypeDef(
    _RequiredTemporalStatisticsConfigInputOutputTypeDef,
    _OptionalTemporalStatisticsConfigInputOutputTypeDef,
):
    pass


_RequiredZonalStatisticsConfigInputOutputTypeDef = TypedDict(
    "_RequiredZonalStatisticsConfigInputOutputTypeDef",
    {
        "Statistics": List[ZonalStatisticsType],
        "ZoneS3Path": str,
    },
)
_OptionalZonalStatisticsConfigInputOutputTypeDef = TypedDict(
    "_OptionalZonalStatisticsConfigInputOutputTypeDef",
    {
        "TargetBands": List[str],
        "ZoneS3PathKmsKeyId": str,
    },
    total=False,
)


class ZonalStatisticsConfigInputOutputTypeDef(
    _RequiredZonalStatisticsConfigInputOutputTypeDef,
    _OptionalZonalStatisticsConfigInputOutputTypeDef,
):
    pass


_RequiredTemporalStatisticsConfigInputTypeDef = TypedDict(
    "_RequiredTemporalStatisticsConfigInputTypeDef",
    {
        "Statistics": Sequence[TemporalStatisticsType],
    },
)
_OptionalTemporalStatisticsConfigInputTypeDef = TypedDict(
    "_OptionalTemporalStatisticsConfigInputTypeDef",
    {
        "GroupBy": GroupByType,
        "TargetBands": Sequence[str],
    },
    total=False,
)


class TemporalStatisticsConfigInputTypeDef(
    _RequiredTemporalStatisticsConfigInputTypeDef, _OptionalTemporalStatisticsConfigInputTypeDef
):
    pass


_RequiredZonalStatisticsConfigInputTypeDef = TypedDict(
    "_RequiredZonalStatisticsConfigInputTypeDef",
    {
        "Statistics": Sequence[ZonalStatisticsType],
        "ZoneS3Path": str,
    },
)
_OptionalZonalStatisticsConfigInputTypeDef = TypedDict(
    "_OptionalZonalStatisticsConfigInputTypeDef",
    {
        "TargetBands": Sequence[str],
        "ZoneS3PathKmsKeyId": str,
    },
    total=False,
)


class ZonalStatisticsConfigInputTypeDef(
    _RequiredZonalStatisticsConfigInputTypeDef, _OptionalZonalStatisticsConfigInputTypeDef
):
    pass


LandsatCloudCoverLandInputOutputTypeDef = TypedDict(
    "LandsatCloudCoverLandInputOutputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

LandsatCloudCoverLandInputTypeDef = TypedDict(
    "LandsatCloudCoverLandInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
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

ListEarthObservationJobInputRequestTypeDef = TypedDict(
    "ListEarthObservationJobInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": str,
        "SortOrder": SortOrderType,
        "StatusEquals": EarthObservationJobStatusType,
    },
    total=False,
)

_RequiredListEarthObservationJobOutputConfigTypeDef = TypedDict(
    "_RequiredListEarthObservationJobOutputConfigTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "Name": str,
        "OperationType": str,
        "Status": EarthObservationJobStatusType,
    },
)
_OptionalListEarthObservationJobOutputConfigTypeDef = TypedDict(
    "_OptionalListEarthObservationJobOutputConfigTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListEarthObservationJobOutputConfigTypeDef(
    _RequiredListEarthObservationJobOutputConfigTypeDef,
    _OptionalListEarthObservationJobOutputConfigTypeDef,
):
    pass


ListRasterDataCollectionsInputRequestTypeDef = TypedDict(
    "ListRasterDataCollectionsInputRequestTypeDef",
    {
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

ListVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "ListVectorEnrichmentJobInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": str,
        "SortOrder": SortOrderType,
        "StatusEquals": str,
    },
    total=False,
)

_RequiredListVectorEnrichmentJobOutputConfigTypeDef = TypedDict(
    "_RequiredListVectorEnrichmentJobOutputConfigTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "Name": str,
        "Status": VectorEnrichmentJobStatusType,
        "Type": VectorEnrichmentJobTypeType,
    },
)
_OptionalListVectorEnrichmentJobOutputConfigTypeDef = TypedDict(
    "_OptionalListVectorEnrichmentJobOutputConfigTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListVectorEnrichmentJobOutputConfigTypeDef(
    _RequiredListVectorEnrichmentJobOutputConfigTypeDef,
    _OptionalListVectorEnrichmentJobOutputConfigTypeDef,
):
    pass


MapMatchingConfigOutputTypeDef = TypedDict(
    "MapMatchingConfigOutputTypeDef",
    {
        "IdAttributeName": str,
        "TimestampAttributeName": str,
        "XAttributeName": str,
        "YAttributeName": str,
    },
)

MapMatchingConfigTypeDef = TypedDict(
    "MapMatchingConfigTypeDef",
    {
        "IdAttributeName": str,
        "TimestampAttributeName": str,
        "XAttributeName": str,
        "YAttributeName": str,
    },
)

UserDefinedOutputTypeDef = TypedDict(
    "UserDefinedOutputTypeDef",
    {
        "Unit": Literal["METERS"],
        "Value": float,
    },
)

UserDefinedTypeDef = TypedDict(
    "UserDefinedTypeDef",
    {
        "Unit": Literal["METERS"],
        "Value": float,
    },
)

_RequiredPlatformInputOutputTypeDef = TypedDict(
    "_RequiredPlatformInputOutputTypeDef",
    {
        "Value": str,
    },
)
_OptionalPlatformInputOutputTypeDef = TypedDict(
    "_OptionalPlatformInputOutputTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
    },
    total=False,
)


class PlatformInputOutputTypeDef(
    _RequiredPlatformInputOutputTypeDef, _OptionalPlatformInputOutputTypeDef
):
    pass


_RequiredPlatformInputTypeDef = TypedDict(
    "_RequiredPlatformInputTypeDef",
    {
        "Value": str,
    },
)
_OptionalPlatformInputTypeDef = TypedDict(
    "_OptionalPlatformInputTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
    },
    total=False,
)


class PlatformInputTypeDef(_RequiredPlatformInputTypeDef, _OptionalPlatformInputTypeDef):
    pass


ViewOffNadirInputOutputTypeDef = TypedDict(
    "ViewOffNadirInputOutputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

ViewSunAzimuthInputOutputTypeDef = TypedDict(
    "ViewSunAzimuthInputOutputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

ViewSunElevationInputOutputTypeDef = TypedDict(
    "ViewSunElevationInputOutputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

ViewOffNadirInputTypeDef = TypedDict(
    "ViewOffNadirInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

ViewSunAzimuthInputTypeDef = TypedDict(
    "ViewSunAzimuthInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

ViewSunElevationInputTypeDef = TypedDict(
    "ViewSunElevationInputTypeDef",
    {
        "LowerBound": float,
        "UpperBound": float,
    },
)

TimeRangeFilterInputTypeDef = TypedDict(
    "TimeRangeFilterInputTypeDef",
    {
        "EndTime": Union[datetime, str],
        "StartTime": Union[datetime, str],
    },
)

TimeRangeFilterOutputTypeDef = TypedDict(
    "TimeRangeFilterOutputTypeDef",
    {
        "EndTime": datetime,
        "StartTime": datetime,
    },
)

ReverseGeocodingConfigOutputTypeDef = TypedDict(
    "ReverseGeocodingConfigOutputTypeDef",
    {
        "XAttributeName": str,
        "YAttributeName": str,
    },
)

ReverseGeocodingConfigTypeDef = TypedDict(
    "ReverseGeocodingConfigTypeDef",
    {
        "XAttributeName": str,
        "YAttributeName": str,
    },
)

StopEarthObservationJobInputRequestTypeDef = TypedDict(
    "StopEarthObservationJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

StopVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "StopVectorEnrichmentJobInputRequestTypeDef",
    {
        "Arn": str,
    },
)

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

AreaOfInterestGeometryOutputTypeDef = TypedDict(
    "AreaOfInterestGeometryOutputTypeDef",
    {
        "MultiPolygonGeometry": MultiPolygonGeometryInputOutputTypeDef,
        "PolygonGeometry": PolygonGeometryInputOutputTypeDef,
    },
    total=False,
)

AreaOfInterestGeometryTypeDef = TypedDict(
    "AreaOfInterestGeometryTypeDef",
    {
        "MultiPolygonGeometry": MultiPolygonGeometryInputTypeDef,
        "PolygonGeometry": PolygonGeometryInputTypeDef,
    },
    total=False,
)

CustomIndicesInputOutputTypeDef = TypedDict(
    "CustomIndicesInputOutputTypeDef",
    {
        "Operations": List[OperationOutputTypeDef],
    },
    total=False,
)

CustomIndicesInputTypeDef = TypedDict(
    "CustomIndicesInputTypeDef",
    {
        "Operations": Sequence[OperationTypeDef],
    },
    total=False,
)

GetTileOutputTypeDef = TypedDict(
    "GetTileOutputTypeDef",
    {
        "BinaryFile": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ExportErrorDetailsTypeDef = TypedDict(
    "ExportErrorDetailsTypeDef",
    {
        "ExportResults": ExportErrorDetailsOutputTypeDef,
        "ExportSourceImages": ExportErrorDetailsOutputTypeDef,
    },
    total=False,
)

OutputConfigInputOutputTypeDef = TypedDict(
    "OutputConfigInputOutputTypeDef",
    {
        "S3Data": ExportS3DataInputOutputTypeDef,
    },
)

OutputConfigInputTypeDef = TypedDict(
    "OutputConfigInputTypeDef",
    {
        "S3Data": ExportS3DataInputTypeDef,
    },
)

ExportVectorEnrichmentJobOutputConfigOutputTypeDef = TypedDict(
    "ExportVectorEnrichmentJobOutputConfigOutputTypeDef",
    {
        "S3Data": VectorEnrichmentJobS3DataOutputTypeDef,
    },
)

VectorEnrichmentJobDataSourceConfigInputOutputTypeDef = TypedDict(
    "VectorEnrichmentJobDataSourceConfigInputOutputTypeDef",
    {
        "S3Data": VectorEnrichmentJobS3DataOutputTypeDef,
    },
    total=False,
)

ExportVectorEnrichmentJobOutputConfigTypeDef = TypedDict(
    "ExportVectorEnrichmentJobOutputConfigTypeDef",
    {
        "S3Data": VectorEnrichmentJobS3DataTypeDef,
    },
)

VectorEnrichmentJobDataSourceConfigInputTypeDef = TypedDict(
    "VectorEnrichmentJobDataSourceConfigInputTypeDef",
    {
        "S3Data": VectorEnrichmentJobS3DataTypeDef,
    },
    total=False,
)

GetRasterDataCollectionOutputTypeDef = TypedDict(
    "GetRasterDataCollectionOutputTypeDef",
    {
        "Arn": str,
        "Description": str,
        "DescriptionPageUrl": str,
        "ImageSourceBands": List[str],
        "Name": str,
        "SupportedFilters": List[FilterTypeDef],
        "Tags": Dict[str, str],
        "Type": DataCollectionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredRasterDataCollectionMetadataTypeDef = TypedDict(
    "_RequiredRasterDataCollectionMetadataTypeDef",
    {
        "Arn": str,
        "Description": str,
        "Name": str,
        "SupportedFilters": List[FilterTypeDef],
        "Type": DataCollectionTypeType,
    },
)
_OptionalRasterDataCollectionMetadataTypeDef = TypedDict(
    "_OptionalRasterDataCollectionMetadataTypeDef",
    {
        "DescriptionPageUrl": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class RasterDataCollectionMetadataTypeDef(
    _RequiredRasterDataCollectionMetadataTypeDef, _OptionalRasterDataCollectionMetadataTypeDef
):
    pass


_RequiredItemSourceTypeDef = TypedDict(
    "_RequiredItemSourceTypeDef",
    {
        "DateTime": datetime,
        "Geometry": GeometryTypeDef,
        "Id": str,
    },
)
_OptionalItemSourceTypeDef = TypedDict(
    "_OptionalItemSourceTypeDef",
    {
        "Assets": Dict[str, AssetValueTypeDef],
        "Properties": PropertiesTypeDef,
    },
    total=False,
)


class ItemSourceTypeDef(_RequiredItemSourceTypeDef, _OptionalItemSourceTypeDef):
    pass


ListEarthObservationJobInputListEarthObservationJobsPaginateTypeDef = TypedDict(
    "ListEarthObservationJobInputListEarthObservationJobsPaginateTypeDef",
    {
        "SortBy": str,
        "SortOrder": SortOrderType,
        "StatusEquals": EarthObservationJobStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListRasterDataCollectionsInputListRasterDataCollectionsPaginateTypeDef = TypedDict(
    "ListRasterDataCollectionsInputListRasterDataCollectionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListVectorEnrichmentJobInputListVectorEnrichmentJobsPaginateTypeDef = TypedDict(
    "ListVectorEnrichmentJobInputListVectorEnrichmentJobsPaginateTypeDef",
    {
        "SortBy": str,
        "SortOrder": SortOrderType,
        "StatusEquals": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListEarthObservationJobOutputTypeDef = TypedDict(
    "ListEarthObservationJobOutputTypeDef",
    {
        "EarthObservationJobSummaries": List[ListEarthObservationJobOutputConfigTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListVectorEnrichmentJobOutputTypeDef = TypedDict(
    "ListVectorEnrichmentJobOutputTypeDef",
    {
        "NextToken": str,
        "VectorEnrichmentJobSummaries": List[ListVectorEnrichmentJobOutputConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

OutputResolutionResamplingInputOutputTypeDef = TypedDict(
    "OutputResolutionResamplingInputOutputTypeDef",
    {
        "UserDefined": UserDefinedOutputTypeDef,
    },
)

OutputResolutionStackInputOutputTypeDef = TypedDict(
    "OutputResolutionStackInputOutputTypeDef",
    {
        "Predefined": PredefinedResolutionType,
        "UserDefined": UserDefinedOutputTypeDef,
    },
    total=False,
)

OutputResolutionResamplingInputTypeDef = TypedDict(
    "OutputResolutionResamplingInputTypeDef",
    {
        "UserDefined": UserDefinedTypeDef,
    },
)

OutputResolutionStackInputTypeDef = TypedDict(
    "OutputResolutionStackInputTypeDef",
    {
        "Predefined": PredefinedResolutionType,
        "UserDefined": UserDefinedTypeDef,
    },
    total=False,
)

PropertyOutputTypeDef = TypedDict(
    "PropertyOutputTypeDef",
    {
        "EoCloudCover": EoCloudCoverInputOutputTypeDef,
        "LandsatCloudCoverLand": LandsatCloudCoverLandInputOutputTypeDef,
        "Platform": PlatformInputOutputTypeDef,
        "ViewOffNadir": ViewOffNadirInputOutputTypeDef,
        "ViewSunAzimuth": ViewSunAzimuthInputOutputTypeDef,
        "ViewSunElevation": ViewSunElevationInputOutputTypeDef,
    },
    total=False,
)

PropertyTypeDef = TypedDict(
    "PropertyTypeDef",
    {
        "EoCloudCover": EoCloudCoverInputTypeDef,
        "LandsatCloudCoverLand": LandsatCloudCoverLandInputTypeDef,
        "Platform": PlatformInputTypeDef,
        "ViewOffNadir": ViewOffNadirInputTypeDef,
        "ViewSunAzimuth": ViewSunAzimuthInputTypeDef,
        "ViewSunElevation": ViewSunElevationInputTypeDef,
    },
    total=False,
)

VectorEnrichmentJobConfigOutputTypeDef = TypedDict(
    "VectorEnrichmentJobConfigOutputTypeDef",
    {
        "MapMatchingConfig": MapMatchingConfigOutputTypeDef,
        "ReverseGeocodingConfig": ReverseGeocodingConfigOutputTypeDef,
    },
    total=False,
)

VectorEnrichmentJobConfigTypeDef = TypedDict(
    "VectorEnrichmentJobConfigTypeDef",
    {
        "MapMatchingConfig": MapMatchingConfigTypeDef,
        "ReverseGeocodingConfig": ReverseGeocodingConfigTypeDef,
    },
    total=False,
)

AreaOfInterestOutputTypeDef = TypedDict(
    "AreaOfInterestOutputTypeDef",
    {
        "AreaOfInterestGeometry": AreaOfInterestGeometryOutputTypeDef,
    },
    total=False,
)

AreaOfInterestTypeDef = TypedDict(
    "AreaOfInterestTypeDef",
    {
        "AreaOfInterestGeometry": AreaOfInterestGeometryTypeDef,
    },
    total=False,
)

BandMathConfigInputOutputTypeDef = TypedDict(
    "BandMathConfigInputOutputTypeDef",
    {
        "CustomIndices": CustomIndicesInputOutputTypeDef,
        "PredefinedIndices": List[str],
    },
    total=False,
)

BandMathConfigInputTypeDef = TypedDict(
    "BandMathConfigInputTypeDef",
    {
        "CustomIndices": CustomIndicesInputTypeDef,
        "PredefinedIndices": Sequence[str],
    },
    total=False,
)

ExportEarthObservationJobOutputTypeDef = TypedDict(
    "ExportEarthObservationJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "ExecutionRoleArn": str,
        "ExportSourceImages": bool,
        "ExportStatus": EarthObservationJobExportStatusType,
        "OutputConfig": OutputConfigInputOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredExportEarthObservationJobInputRequestTypeDef = TypedDict(
    "_RequiredExportEarthObservationJobInputRequestTypeDef",
    {
        "Arn": str,
        "ExecutionRoleArn": str,
        "OutputConfig": OutputConfigInputTypeDef,
    },
)
_OptionalExportEarthObservationJobInputRequestTypeDef = TypedDict(
    "_OptionalExportEarthObservationJobInputRequestTypeDef",
    {
        "ClientToken": str,
        "ExportSourceImages": bool,
    },
    total=False,
)


class ExportEarthObservationJobInputRequestTypeDef(
    _RequiredExportEarthObservationJobInputRequestTypeDef,
    _OptionalExportEarthObservationJobInputRequestTypeDef,
):
    pass


ExportVectorEnrichmentJobOutputTypeDef = TypedDict(
    "ExportVectorEnrichmentJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "ExecutionRoleArn": str,
        "ExportStatus": VectorEnrichmentJobExportStatusType,
        "OutputConfig": ExportVectorEnrichmentJobOutputConfigOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

VectorEnrichmentJobInputConfigOutputTypeDef = TypedDict(
    "VectorEnrichmentJobInputConfigOutputTypeDef",
    {
        "DataSourceConfig": VectorEnrichmentJobDataSourceConfigInputOutputTypeDef,
        "DocumentType": Literal["CSV"],
    },
)

_RequiredExportVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "_RequiredExportVectorEnrichmentJobInputRequestTypeDef",
    {
        "Arn": str,
        "ExecutionRoleArn": str,
        "OutputConfig": ExportVectorEnrichmentJobOutputConfigTypeDef,
    },
)
_OptionalExportVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "_OptionalExportVectorEnrichmentJobInputRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class ExportVectorEnrichmentJobInputRequestTypeDef(
    _RequiredExportVectorEnrichmentJobInputRequestTypeDef,
    _OptionalExportVectorEnrichmentJobInputRequestTypeDef,
):
    pass


VectorEnrichmentJobInputConfigTypeDef = TypedDict(
    "VectorEnrichmentJobInputConfigTypeDef",
    {
        "DataSourceConfig": VectorEnrichmentJobDataSourceConfigInputTypeDef,
        "DocumentType": Literal["CSV"],
    },
)

ListRasterDataCollectionsOutputTypeDef = TypedDict(
    "ListRasterDataCollectionsOutputTypeDef",
    {
        "NextToken": str,
        "RasterDataCollectionSummaries": List[RasterDataCollectionMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SearchRasterDataCollectionOutputTypeDef = TypedDict(
    "SearchRasterDataCollectionOutputTypeDef",
    {
        "ApproximateResultCount": int,
        "Items": List[ItemSourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredResamplingConfigInputOutputTypeDef = TypedDict(
    "_RequiredResamplingConfigInputOutputTypeDef",
    {
        "OutputResolution": OutputResolutionResamplingInputOutputTypeDef,
    },
)
_OptionalResamplingConfigInputOutputTypeDef = TypedDict(
    "_OptionalResamplingConfigInputOutputTypeDef",
    {
        "AlgorithmName": AlgorithmNameResamplingType,
        "TargetBands": List[str],
    },
    total=False,
)


class ResamplingConfigInputOutputTypeDef(
    _RequiredResamplingConfigInputOutputTypeDef, _OptionalResamplingConfigInputOutputTypeDef
):
    pass


StackConfigInputOutputTypeDef = TypedDict(
    "StackConfigInputOutputTypeDef",
    {
        "OutputResolution": OutputResolutionStackInputOutputTypeDef,
        "TargetBands": List[str],
    },
    total=False,
)

_RequiredResamplingConfigInputTypeDef = TypedDict(
    "_RequiredResamplingConfigInputTypeDef",
    {
        "OutputResolution": OutputResolutionResamplingInputTypeDef,
    },
)
_OptionalResamplingConfigInputTypeDef = TypedDict(
    "_OptionalResamplingConfigInputTypeDef",
    {
        "AlgorithmName": AlgorithmNameResamplingType,
        "TargetBands": Sequence[str],
    },
    total=False,
)


class ResamplingConfigInputTypeDef(
    _RequiredResamplingConfigInputTypeDef, _OptionalResamplingConfigInputTypeDef
):
    pass


StackConfigInputTypeDef = TypedDict(
    "StackConfigInputTypeDef",
    {
        "OutputResolution": OutputResolutionStackInputTypeDef,
        "TargetBands": Sequence[str],
    },
    total=False,
)

PropertyFilterOutputTypeDef = TypedDict(
    "PropertyFilterOutputTypeDef",
    {
        "Property": PropertyOutputTypeDef,
    },
)

PropertyFilterTypeDef = TypedDict(
    "PropertyFilterTypeDef",
    {
        "Property": PropertyTypeDef,
    },
)

GetVectorEnrichmentJobOutputTypeDef = TypedDict(
    "GetVectorEnrichmentJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "ErrorDetails": VectorEnrichmentJobErrorDetailsTypeDef,
        "ExecutionRoleArn": str,
        "ExportErrorDetails": VectorEnrichmentJobExportErrorDetailsTypeDef,
        "ExportStatus": VectorEnrichmentJobExportStatusType,
        "InputConfig": VectorEnrichmentJobInputConfigOutputTypeDef,
        "JobConfig": VectorEnrichmentJobConfigOutputTypeDef,
        "KmsKeyId": str,
        "Name": str,
        "Status": VectorEnrichmentJobStatusType,
        "Tags": Dict[str, str],
        "Type": VectorEnrichmentJobTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartVectorEnrichmentJobOutputTypeDef = TypedDict(
    "StartVectorEnrichmentJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "ExecutionRoleArn": str,
        "InputConfig": VectorEnrichmentJobInputConfigOutputTypeDef,
        "JobConfig": VectorEnrichmentJobConfigOutputTypeDef,
        "KmsKeyId": str,
        "Name": str,
        "Status": VectorEnrichmentJobStatusType,
        "Tags": Dict[str, str],
        "Type": VectorEnrichmentJobTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredStartVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "_RequiredStartVectorEnrichmentJobInputRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "InputConfig": VectorEnrichmentJobInputConfigTypeDef,
        "JobConfig": VectorEnrichmentJobConfigTypeDef,
        "Name": str,
    },
)
_OptionalStartVectorEnrichmentJobInputRequestTypeDef = TypedDict(
    "_OptionalStartVectorEnrichmentJobInputRequestTypeDef",
    {
        "ClientToken": str,
        "KmsKeyId": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class StartVectorEnrichmentJobInputRequestTypeDef(
    _RequiredStartVectorEnrichmentJobInputRequestTypeDef,
    _OptionalStartVectorEnrichmentJobInputRequestTypeDef,
):
    pass


JobConfigInputOutputTypeDef = TypedDict(
    "JobConfigInputOutputTypeDef",
    {
        "BandMathConfig": BandMathConfigInputOutputTypeDef,
        "CloudMaskingConfig": Dict[str, Any],
        "CloudRemovalConfig": CloudRemovalConfigInputOutputTypeDef,
        "GeoMosaicConfig": GeoMosaicConfigInputOutputTypeDef,
        "LandCoverSegmentationConfig": Dict[str, Any],
        "ResamplingConfig": ResamplingConfigInputOutputTypeDef,
        "StackConfig": StackConfigInputOutputTypeDef,
        "TemporalStatisticsConfig": TemporalStatisticsConfigInputOutputTypeDef,
        "ZonalStatisticsConfig": ZonalStatisticsConfigInputOutputTypeDef,
    },
    total=False,
)

JobConfigInputTypeDef = TypedDict(
    "JobConfigInputTypeDef",
    {
        "BandMathConfig": BandMathConfigInputTypeDef,
        "CloudMaskingConfig": Mapping[str, Any],
        "CloudRemovalConfig": CloudRemovalConfigInputTypeDef,
        "GeoMosaicConfig": GeoMosaicConfigInputTypeDef,
        "LandCoverSegmentationConfig": Mapping[str, Any],
        "ResamplingConfig": ResamplingConfigInputTypeDef,
        "StackConfig": StackConfigInputTypeDef,
        "TemporalStatisticsConfig": TemporalStatisticsConfigInputTypeDef,
        "ZonalStatisticsConfig": ZonalStatisticsConfigInputTypeDef,
    },
    total=False,
)

PropertyFiltersOutputTypeDef = TypedDict(
    "PropertyFiltersOutputTypeDef",
    {
        "LogicalOperator": Literal["AND"],
        "Properties": List[PropertyFilterOutputTypeDef],
    },
    total=False,
)

PropertyFiltersTypeDef = TypedDict(
    "PropertyFiltersTypeDef",
    {
        "LogicalOperator": Literal["AND"],
        "Properties": Sequence[PropertyFilterTypeDef],
    },
    total=False,
)

_RequiredRasterDataCollectionQueryOutputTypeDef = TypedDict(
    "_RequiredRasterDataCollectionQueryOutputTypeDef",
    {
        "RasterDataCollectionArn": str,
        "RasterDataCollectionName": str,
        "TimeRangeFilter": TimeRangeFilterOutputTypeDef,
    },
)
_OptionalRasterDataCollectionQueryOutputTypeDef = TypedDict(
    "_OptionalRasterDataCollectionQueryOutputTypeDef",
    {
        "AreaOfInterest": AreaOfInterestOutputTypeDef,
        "PropertyFilters": PropertyFiltersOutputTypeDef,
    },
    total=False,
)


class RasterDataCollectionQueryOutputTypeDef(
    _RequiredRasterDataCollectionQueryOutputTypeDef, _OptionalRasterDataCollectionQueryOutputTypeDef
):
    pass


_RequiredRasterDataCollectionQueryInputTypeDef = TypedDict(
    "_RequiredRasterDataCollectionQueryInputTypeDef",
    {
        "RasterDataCollectionArn": str,
        "TimeRangeFilter": TimeRangeFilterInputTypeDef,
    },
)
_OptionalRasterDataCollectionQueryInputTypeDef = TypedDict(
    "_OptionalRasterDataCollectionQueryInputTypeDef",
    {
        "AreaOfInterest": AreaOfInterestTypeDef,
        "PropertyFilters": PropertyFiltersTypeDef,
    },
    total=False,
)


class RasterDataCollectionQueryInputTypeDef(
    _RequiredRasterDataCollectionQueryInputTypeDef, _OptionalRasterDataCollectionQueryInputTypeDef
):
    pass


_RequiredRasterDataCollectionQueryWithBandFilterInputTypeDef = TypedDict(
    "_RequiredRasterDataCollectionQueryWithBandFilterInputTypeDef",
    {
        "TimeRangeFilter": TimeRangeFilterInputTypeDef,
    },
)
_OptionalRasterDataCollectionQueryWithBandFilterInputTypeDef = TypedDict(
    "_OptionalRasterDataCollectionQueryWithBandFilterInputTypeDef",
    {
        "AreaOfInterest": AreaOfInterestTypeDef,
        "BandFilter": Sequence[str],
        "PropertyFilters": PropertyFiltersTypeDef,
    },
    total=False,
)


class RasterDataCollectionQueryWithBandFilterInputTypeDef(
    _RequiredRasterDataCollectionQueryWithBandFilterInputTypeDef,
    _OptionalRasterDataCollectionQueryWithBandFilterInputTypeDef,
):
    pass


InputConfigOutputTypeDef = TypedDict(
    "InputConfigOutputTypeDef",
    {
        "PreviousEarthObservationJobArn": str,
        "RasterDataCollectionQuery": RasterDataCollectionQueryOutputTypeDef,
    },
    total=False,
)

InputConfigInputTypeDef = TypedDict(
    "InputConfigInputTypeDef",
    {
        "PreviousEarthObservationJobArn": str,
        "RasterDataCollectionQuery": RasterDataCollectionQueryInputTypeDef,
    },
    total=False,
)

_RequiredSearchRasterDataCollectionInputRequestTypeDef = TypedDict(
    "_RequiredSearchRasterDataCollectionInputRequestTypeDef",
    {
        "Arn": str,
        "RasterDataCollectionQuery": RasterDataCollectionQueryWithBandFilterInputTypeDef,
    },
)
_OptionalSearchRasterDataCollectionInputRequestTypeDef = TypedDict(
    "_OptionalSearchRasterDataCollectionInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class SearchRasterDataCollectionInputRequestTypeDef(
    _RequiredSearchRasterDataCollectionInputRequestTypeDef,
    _OptionalSearchRasterDataCollectionInputRequestTypeDef,
):
    pass


GetEarthObservationJobOutputTypeDef = TypedDict(
    "GetEarthObservationJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "ErrorDetails": EarthObservationJobErrorDetailsTypeDef,
        "ExecutionRoleArn": str,
        "ExportErrorDetails": ExportErrorDetailsTypeDef,
        "ExportStatus": EarthObservationJobExportStatusType,
        "InputConfig": InputConfigOutputTypeDef,
        "JobConfig": JobConfigInputOutputTypeDef,
        "KmsKeyId": str,
        "Name": str,
        "OutputBands": List[OutputBandTypeDef],
        "Status": EarthObservationJobStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartEarthObservationJobOutputTypeDef = TypedDict(
    "StartEarthObservationJobOutputTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "DurationInSeconds": int,
        "ExecutionRoleArn": str,
        "InputConfig": InputConfigOutputTypeDef,
        "JobConfig": JobConfigInputOutputTypeDef,
        "KmsKeyId": str,
        "Name": str,
        "Status": EarthObservationJobStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredStartEarthObservationJobInputRequestTypeDef = TypedDict(
    "_RequiredStartEarthObservationJobInputRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "InputConfig": InputConfigInputTypeDef,
        "JobConfig": JobConfigInputTypeDef,
        "Name": str,
    },
)
_OptionalStartEarthObservationJobInputRequestTypeDef = TypedDict(
    "_OptionalStartEarthObservationJobInputRequestTypeDef",
    {
        "ClientToken": str,
        "KmsKeyId": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)


class StartEarthObservationJobInputRequestTypeDef(
    _RequiredStartEarthObservationJobInputRequestTypeDef,
    _OptionalStartEarthObservationJobInputRequestTypeDef,
):
    pass
