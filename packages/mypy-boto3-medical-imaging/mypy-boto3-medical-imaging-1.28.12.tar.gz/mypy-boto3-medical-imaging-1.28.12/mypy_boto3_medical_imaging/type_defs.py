"""
Type annotations for medical-imaging service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/type_defs/)

Usage::

    ```python
    from mypy_boto3_medical_imaging.type_defs import CopyDestinationImageSetPropertiesTypeDef

    data: CopyDestinationImageSetPropertiesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    DatastoreStatusType,
    ImageSetStateType,
    ImageSetWorkflowStatusType,
    JobStatusType,
    OperatorType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CopyDestinationImageSetPropertiesTypeDef",
    "CopyDestinationImageSetTypeDef",
    "CopySourceImageSetInformationTypeDef",
    "CopySourceImageSetPropertiesTypeDef",
    "CreateDatastoreRequestRequestTypeDef",
    "CreateDatastoreResponseTypeDef",
    "DICOMImportJobPropertiesTypeDef",
    "DICOMImportJobSummaryTypeDef",
    "DICOMStudyDateAndTimeTypeDef",
    "DICOMTagsTypeDef",
    "DICOMUpdatesTypeDef",
    "DatastorePropertiesTypeDef",
    "DatastoreSummaryTypeDef",
    "DeleteDatastoreRequestRequestTypeDef",
    "DeleteDatastoreResponseTypeDef",
    "DeleteImageSetRequestRequestTypeDef",
    "DeleteImageSetResponseTypeDef",
    "GetDICOMImportJobRequestRequestTypeDef",
    "GetDatastoreRequestRequestTypeDef",
    "ImageFrameInformationTypeDef",
    "GetImageFrameResponseTypeDef",
    "GetImageSetMetadataRequestRequestTypeDef",
    "GetImageSetMetadataResponseTypeDef",
    "GetImageSetRequestRequestTypeDef",
    "GetImageSetResponseTypeDef",
    "ImageSetPropertiesTypeDef",
    "ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef",
    "ListDICOMImportJobsRequestRequestTypeDef",
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    "ListDatastoresRequestRequestTypeDef",
    "ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef",
    "ListImageSetVersionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartDICOMImportJobRequestRequestTypeDef",
    "StartDICOMImportJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateImageSetMetadataResponseTypeDef",
    "CopyImageSetInformationTypeDef",
    "CopyImageSetResponseTypeDef",
    "GetDICOMImportJobResponseTypeDef",
    "ListDICOMImportJobsResponseTypeDef",
    "SearchByAttributeValueTypeDef",
    "ImageSetsMetadataSummaryTypeDef",
    "MetadataUpdatesTypeDef",
    "GetDatastoreResponseTypeDef",
    "ListDatastoresResponseTypeDef",
    "GetImageFrameRequestRequestTypeDef",
    "ListImageSetVersionsResponseTypeDef",
    "CopyImageSetRequestRequestTypeDef",
    "SearchFilterTypeDef",
    "SearchImageSetsResponseTypeDef",
    "UpdateImageSetMetadataRequestRequestTypeDef",
    "SearchCriteriaTypeDef",
    "SearchImageSetsRequestRequestTypeDef",
    "SearchImageSetsRequestSearchImageSetsPaginateTypeDef",
)

_RequiredCopyDestinationImageSetPropertiesTypeDef = TypedDict(
    "_RequiredCopyDestinationImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
    },
)
_OptionalCopyDestinationImageSetPropertiesTypeDef = TypedDict(
    "_OptionalCopyDestinationImageSetPropertiesTypeDef",
    {
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "imageSetArn": str,
    },
    total=False,
)


class CopyDestinationImageSetPropertiesTypeDef(
    _RequiredCopyDestinationImageSetPropertiesTypeDef,
    _OptionalCopyDestinationImageSetPropertiesTypeDef,
):
    pass


CopyDestinationImageSetTypeDef = TypedDict(
    "CopyDestinationImageSetTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
    },
)

CopySourceImageSetInformationTypeDef = TypedDict(
    "CopySourceImageSetInformationTypeDef",
    {
        "latestVersionId": str,
    },
)

_RequiredCopySourceImageSetPropertiesTypeDef = TypedDict(
    "_RequiredCopySourceImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
    },
)
_OptionalCopySourceImageSetPropertiesTypeDef = TypedDict(
    "_OptionalCopySourceImageSetPropertiesTypeDef",
    {
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "imageSetArn": str,
    },
    total=False,
)


class CopySourceImageSetPropertiesTypeDef(
    _RequiredCopySourceImageSetPropertiesTypeDef, _OptionalCopySourceImageSetPropertiesTypeDef
):
    pass


_RequiredCreateDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatastoreRequestRequestTypeDef",
    {
        "clientToken": str,
    },
)
_OptionalCreateDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
        "tags": Mapping[str, str],
        "kmsKeyArn": str,
    },
    total=False,
)


class CreateDatastoreRequestRequestTypeDef(
    _RequiredCreateDatastoreRequestRequestTypeDef, _OptionalCreateDatastoreRequestRequestTypeDef
):
    pass


CreateDatastoreResponseTypeDef = TypedDict(
    "CreateDatastoreResponseTypeDef",
    {
        "datastoreId": str,
        "datastoreStatus": DatastoreStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDICOMImportJobPropertiesTypeDef = TypedDict(
    "_RequiredDICOMImportJobPropertiesTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "datastoreId": str,
        "dataAccessRoleArn": str,
        "inputS3Uri": str,
        "outputS3Uri": str,
    },
)
_OptionalDICOMImportJobPropertiesTypeDef = TypedDict(
    "_OptionalDICOMImportJobPropertiesTypeDef",
    {
        "endedAt": datetime,
        "submittedAt": datetime,
        "message": str,
    },
    total=False,
)


class DICOMImportJobPropertiesTypeDef(
    _RequiredDICOMImportJobPropertiesTypeDef, _OptionalDICOMImportJobPropertiesTypeDef
):
    pass


_RequiredDICOMImportJobSummaryTypeDef = TypedDict(
    "_RequiredDICOMImportJobSummaryTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "datastoreId": str,
    },
)
_OptionalDICOMImportJobSummaryTypeDef = TypedDict(
    "_OptionalDICOMImportJobSummaryTypeDef",
    {
        "dataAccessRoleArn": str,
        "endedAt": datetime,
        "submittedAt": datetime,
        "message": str,
    },
    total=False,
)


class DICOMImportJobSummaryTypeDef(
    _RequiredDICOMImportJobSummaryTypeDef, _OptionalDICOMImportJobSummaryTypeDef
):
    pass


_RequiredDICOMStudyDateAndTimeTypeDef = TypedDict(
    "_RequiredDICOMStudyDateAndTimeTypeDef",
    {
        "DICOMStudyDate": str,
    },
)
_OptionalDICOMStudyDateAndTimeTypeDef = TypedDict(
    "_OptionalDICOMStudyDateAndTimeTypeDef",
    {
        "DICOMStudyTime": str,
    },
    total=False,
)


class DICOMStudyDateAndTimeTypeDef(
    _RequiredDICOMStudyDateAndTimeTypeDef, _OptionalDICOMStudyDateAndTimeTypeDef
):
    pass


DICOMTagsTypeDef = TypedDict(
    "DICOMTagsTypeDef",
    {
        "DICOMPatientId": str,
        "DICOMPatientName": str,
        "DICOMPatientBirthDate": str,
        "DICOMPatientSex": str,
        "DICOMStudyInstanceUID": str,
        "DICOMStudyId": str,
        "DICOMStudyDescription": str,
        "DICOMNumberOfStudyRelatedSeries": int,
        "DICOMNumberOfStudyRelatedInstances": int,
        "DICOMAccessionNumber": str,
        "DICOMStudyDate": str,
        "DICOMStudyTime": str,
    },
    total=False,
)

DICOMUpdatesTypeDef = TypedDict(
    "DICOMUpdatesTypeDef",
    {
        "removableAttributes": Union[str, bytes, IO[Any], StreamingBody],
        "updatableAttributes": Union[str, bytes, IO[Any], StreamingBody],
    },
    total=False,
)

_RequiredDatastorePropertiesTypeDef = TypedDict(
    "_RequiredDatastorePropertiesTypeDef",
    {
        "datastoreId": str,
        "datastoreName": str,
        "datastoreStatus": DatastoreStatusType,
    },
)
_OptionalDatastorePropertiesTypeDef = TypedDict(
    "_OptionalDatastorePropertiesTypeDef",
    {
        "kmsKeyArn": str,
        "datastoreArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)


class DatastorePropertiesTypeDef(
    _RequiredDatastorePropertiesTypeDef, _OptionalDatastorePropertiesTypeDef
):
    pass


_RequiredDatastoreSummaryTypeDef = TypedDict(
    "_RequiredDatastoreSummaryTypeDef",
    {
        "datastoreId": str,
        "datastoreName": str,
        "datastoreStatus": DatastoreStatusType,
    },
)
_OptionalDatastoreSummaryTypeDef = TypedDict(
    "_OptionalDatastoreSummaryTypeDef",
    {
        "datastoreArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)


class DatastoreSummaryTypeDef(_RequiredDatastoreSummaryTypeDef, _OptionalDatastoreSummaryTypeDef):
    pass


DeleteDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteDatastoreRequestRequestTypeDef",
    {
        "datastoreId": str,
    },
)

DeleteDatastoreResponseTypeDef = TypedDict(
    "DeleteDatastoreResponseTypeDef",
    {
        "datastoreId": str,
        "datastoreStatus": DatastoreStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageSetRequestRequestTypeDef = TypedDict(
    "DeleteImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
    },
)

DeleteImageSetResponseTypeDef = TypedDict(
    "DeleteImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDICOMImportJobRequestRequestTypeDef = TypedDict(
    "GetDICOMImportJobRequestRequestTypeDef",
    {
        "datastoreId": str,
        "jobId": str,
    },
)

GetDatastoreRequestRequestTypeDef = TypedDict(
    "GetDatastoreRequestRequestTypeDef",
    {
        "datastoreId": str,
    },
)

ImageFrameInformationTypeDef = TypedDict(
    "ImageFrameInformationTypeDef",
    {
        "imageFrameId": str,
    },
)

GetImageFrameResponseTypeDef = TypedDict(
    "GetImageFrameResponseTypeDef",
    {
        "imageFrameBlob": StreamingBody,
        "contentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetImageSetMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredGetImageSetMetadataRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
    },
)
_OptionalGetImageSetMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalGetImageSetMetadataRequestRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)


class GetImageSetMetadataRequestRequestTypeDef(
    _RequiredGetImageSetMetadataRequestRequestTypeDef,
    _OptionalGetImageSetMetadataRequestRequestTypeDef,
):
    pass


GetImageSetMetadataResponseTypeDef = TypedDict(
    "GetImageSetMetadataResponseTypeDef",
    {
        "imageSetMetadataBlob": StreamingBody,
        "contentType": str,
        "contentEncoding": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetImageSetRequestRequestTypeDef = TypedDict(
    "_RequiredGetImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
    },
)
_OptionalGetImageSetRequestRequestTypeDef = TypedDict(
    "_OptionalGetImageSetRequestRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)


class GetImageSetRequestRequestTypeDef(
    _RequiredGetImageSetRequestRequestTypeDef, _OptionalGetImageSetRequestRequestTypeDef
):
    pass


GetImageSetResponseTypeDef = TypedDict(
    "GetImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "versionId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "deletedAt": datetime,
        "message": str,
        "imageSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImageSetPropertiesTypeDef = TypedDict(
    "_RequiredImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "versionId": str,
        "imageSetState": ImageSetStateType,
    },
)
_OptionalImageSetPropertiesTypeDef = TypedDict(
    "_OptionalImageSetPropertiesTypeDef",
    {
        "ImageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "deletedAt": datetime,
        "message": str,
    },
    total=False,
)


class ImageSetPropertiesTypeDef(
    _RequiredImageSetPropertiesTypeDef, _OptionalImageSetPropertiesTypeDef
):
    pass


_RequiredListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef = TypedDict(
    "_RequiredListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef",
    {
        "datastoreId": str,
    },
)
_OptionalListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef = TypedDict(
    "_OptionalListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef",
    {
        "jobStatus": JobStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef(
    _RequiredListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef,
    _OptionalListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef,
):
    pass


_RequiredListDICOMImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListDICOMImportJobsRequestRequestTypeDef",
    {
        "datastoreId": str,
    },
)
_OptionalListDICOMImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListDICOMImportJobsRequestRequestTypeDef",
    {
        "jobStatus": JobStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListDICOMImportJobsRequestRequestTypeDef(
    _RequiredListDICOMImportJobsRequestRequestTypeDef,
    _OptionalListDICOMImportJobsRequestRequestTypeDef,
):
    pass


ListDatastoresRequestListDatastoresPaginateTypeDef = TypedDict(
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    {
        "datastoreStatus": DatastoreStatusType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDatastoresRequestRequestTypeDef = TypedDict(
    "ListDatastoresRequestRequestTypeDef",
    {
        "datastoreStatus": DatastoreStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef = TypedDict(
    "_RequiredListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
    },
)
_OptionalListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef = TypedDict(
    "_OptionalListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef(
    _RequiredListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef,
    _OptionalListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef,
):
    pass


_RequiredListImageSetVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListImageSetVersionsRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
    },
)
_OptionalListImageSetVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListImageSetVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListImageSetVersionsRequestRequestTypeDef(
    _RequiredListImageSetVersionsRequestRequestTypeDef,
    _OptionalListImageSetVersionsRequestRequestTypeDef,
):
    pass


ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
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

_RequiredStartDICOMImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartDICOMImportJobRequestRequestTypeDef",
    {
        "dataAccessRoleArn": str,
        "clientToken": str,
        "datastoreId": str,
        "inputS3Uri": str,
        "outputS3Uri": str,
    },
)
_OptionalStartDICOMImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartDICOMImportJobRequestRequestTypeDef",
    {
        "jobName": str,
    },
    total=False,
)


class StartDICOMImportJobRequestRequestTypeDef(
    _RequiredStartDICOMImportJobRequestRequestTypeDef,
    _OptionalStartDICOMImportJobRequestRequestTypeDef,
):
    pass


StartDICOMImportJobResponseTypeDef = TypedDict(
    "StartDICOMImportJobResponseTypeDef",
    {
        "datastoreId": str,
        "jobId": str,
        "jobStatus": JobStatusType,
        "submittedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateImageSetMetadataResponseTypeDef = TypedDict(
    "UpdateImageSetMetadataResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "latestVersionId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyImageSetInformationTypeDef = TypedDict(
    "_RequiredCopyImageSetInformationTypeDef",
    {
        "sourceImageSet": CopySourceImageSetInformationTypeDef,
    },
)
_OptionalCopyImageSetInformationTypeDef = TypedDict(
    "_OptionalCopyImageSetInformationTypeDef",
    {
        "destinationImageSet": CopyDestinationImageSetTypeDef,
    },
    total=False,
)


class CopyImageSetInformationTypeDef(
    _RequiredCopyImageSetInformationTypeDef, _OptionalCopyImageSetInformationTypeDef
):
    pass


CopyImageSetResponseTypeDef = TypedDict(
    "CopyImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "sourceImageSetProperties": CopySourceImageSetPropertiesTypeDef,
        "destinationImageSetProperties": CopyDestinationImageSetPropertiesTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDICOMImportJobResponseTypeDef = TypedDict(
    "GetDICOMImportJobResponseTypeDef",
    {
        "jobProperties": DICOMImportJobPropertiesTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDICOMImportJobsResponseTypeDef = TypedDict(
    "ListDICOMImportJobsResponseTypeDef",
    {
        "jobSummaries": List[DICOMImportJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchByAttributeValueTypeDef = TypedDict(
    "SearchByAttributeValueTypeDef",
    {
        "DICOMPatientId": str,
        "DICOMAccessionNumber": str,
        "DICOMStudyId": str,
        "DICOMStudyInstanceUID": str,
        "createdAt": Union[datetime, str],
        "DICOMStudyDateAndTime": DICOMStudyDateAndTimeTypeDef,
    },
    total=False,
)

_RequiredImageSetsMetadataSummaryTypeDef = TypedDict(
    "_RequiredImageSetsMetadataSummaryTypeDef",
    {
        "imageSetId": str,
    },
)
_OptionalImageSetsMetadataSummaryTypeDef = TypedDict(
    "_OptionalImageSetsMetadataSummaryTypeDef",
    {
        "version": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "DICOMTags": DICOMTagsTypeDef,
    },
    total=False,
)


class ImageSetsMetadataSummaryTypeDef(
    _RequiredImageSetsMetadataSummaryTypeDef, _OptionalImageSetsMetadataSummaryTypeDef
):
    pass


MetadataUpdatesTypeDef = TypedDict(
    "MetadataUpdatesTypeDef",
    {
        "DICOMUpdates": DICOMUpdatesTypeDef,
    },
    total=False,
)

GetDatastoreResponseTypeDef = TypedDict(
    "GetDatastoreResponseTypeDef",
    {
        "datastoreProperties": DatastorePropertiesTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List[DatastoreSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageFrameRequestRequestTypeDef = TypedDict(
    "GetImageFrameRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "imageFrameInformation": ImageFrameInformationTypeDef,
    },
)

ListImageSetVersionsResponseTypeDef = TypedDict(
    "ListImageSetVersionsResponseTypeDef",
    {
        "imageSetPropertiesList": List[ImageSetPropertiesTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyImageSetRequestRequestTypeDef = TypedDict(
    "CopyImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "sourceImageSetId": str,
        "copyImageSetInformation": CopyImageSetInformationTypeDef,
    },
)

SearchFilterTypeDef = TypedDict(
    "SearchFilterTypeDef",
    {
        "values": Sequence[SearchByAttributeValueTypeDef],
        "operator": OperatorType,
    },
)

SearchImageSetsResponseTypeDef = TypedDict(
    "SearchImageSetsResponseTypeDef",
    {
        "imageSetsMetadataSummaries": List[ImageSetsMetadataSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateImageSetMetadataRequestRequestTypeDef = TypedDict(
    "UpdateImageSetMetadataRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "latestVersionId": str,
        "updateImageSetMetadataUpdates": MetadataUpdatesTypeDef,
    },
)

SearchCriteriaTypeDef = TypedDict(
    "SearchCriteriaTypeDef",
    {
        "filters": Sequence[SearchFilterTypeDef],
    },
    total=False,
)

_RequiredSearchImageSetsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchImageSetsRequestRequestTypeDef",
    {
        "datastoreId": str,
    },
)
_OptionalSearchImageSetsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchImageSetsRequestRequestTypeDef",
    {
        "searchCriteria": SearchCriteriaTypeDef,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class SearchImageSetsRequestRequestTypeDef(
    _RequiredSearchImageSetsRequestRequestTypeDef, _OptionalSearchImageSetsRequestRequestTypeDef
):
    pass


_RequiredSearchImageSetsRequestSearchImageSetsPaginateTypeDef = TypedDict(
    "_RequiredSearchImageSetsRequestSearchImageSetsPaginateTypeDef",
    {
        "datastoreId": str,
    },
)
_OptionalSearchImageSetsRequestSearchImageSetsPaginateTypeDef = TypedDict(
    "_OptionalSearchImageSetsRequestSearchImageSetsPaginateTypeDef",
    {
        "searchCriteria": SearchCriteriaTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchImageSetsRequestSearchImageSetsPaginateTypeDef(
    _RequiredSearchImageSetsRequestSearchImageSetsPaginateTypeDef,
    _OptionalSearchImageSetsRequestSearchImageSetsPaginateTypeDef,
):
    pass
