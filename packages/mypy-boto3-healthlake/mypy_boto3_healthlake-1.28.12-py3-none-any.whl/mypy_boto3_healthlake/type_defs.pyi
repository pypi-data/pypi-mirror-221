"""
Type annotations for healthlake service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/type_defs/)

Usage::

    ```python
    from mypy_boto3_healthlake.type_defs import IdentityProviderConfigurationTypeDef

    data: IdentityProviderConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import AuthorizationStrategyType, CmkTypeType, DatastoreStatusType, JobStatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "IdentityProviderConfigurationTypeDef",
    "PreloadDataConfigTypeDef",
    "TagTypeDef",
    "CreateFHIRDatastoreResponseTypeDef",
    "DatastoreFilterTypeDef",
    "IdentityProviderConfigurationOutputTypeDef",
    "PreloadDataConfigOutputTypeDef",
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    "DeleteFHIRDatastoreResponseTypeDef",
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    "DescribeFHIRExportJobRequestRequestTypeDef",
    "DescribeFHIRImportJobRequestRequestTypeDef",
    "InputDataConfigOutputTypeDef",
    "InputDataConfigTypeDef",
    "KmsEncryptionConfigOutputTypeDef",
    "KmsEncryptionConfigTypeDef",
    "ListFHIRExportJobsRequestRequestTypeDef",
    "ListFHIRImportJobsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "S3ConfigurationOutputTypeDef",
    "S3ConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "StartFHIRExportJobResponseTypeDef",
    "StartFHIRImportJobResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListFHIRDatastoresRequestRequestTypeDef",
    "SseConfigurationOutputTypeDef",
    "SseConfigurationTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutputDataConfigOutputTypeDef",
    "OutputDataConfigTypeDef",
    "DatastorePropertiesTypeDef",
    "CreateFHIRDatastoreRequestRequestTypeDef",
    "ExportJobPropertiesTypeDef",
    "ImportJobPropertiesTypeDef",
    "StartFHIRExportJobRequestRequestTypeDef",
    "StartFHIRImportJobRequestRequestTypeDef",
    "DescribeFHIRDatastoreResponseTypeDef",
    "ListFHIRDatastoresResponseTypeDef",
    "DescribeFHIRExportJobResponseTypeDef",
    "ListFHIRExportJobsResponseTypeDef",
    "DescribeFHIRImportJobResponseTypeDef",
    "ListFHIRImportJobsResponseTypeDef",
)

_RequiredIdentityProviderConfigurationTypeDef = TypedDict(
    "_RequiredIdentityProviderConfigurationTypeDef",
    {
        "AuthorizationStrategy": AuthorizationStrategyType,
    },
)
_OptionalIdentityProviderConfigurationTypeDef = TypedDict(
    "_OptionalIdentityProviderConfigurationTypeDef",
    {
        "FineGrainedAuthorizationEnabled": bool,
        "Metadata": str,
        "IdpLambdaArn": str,
    },
    total=False,
)

class IdentityProviderConfigurationTypeDef(
    _RequiredIdentityProviderConfigurationTypeDef, _OptionalIdentityProviderConfigurationTypeDef
):
    pass

PreloadDataConfigTypeDef = TypedDict(
    "PreloadDataConfigTypeDef",
    {
        "PreloadDataType": Literal["SYNTHEA"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateFHIRDatastoreResponseTypeDef = TypedDict(
    "CreateFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatastoreFilterTypeDef = TypedDict(
    "DatastoreFilterTypeDef",
    {
        "DatastoreName": str,
        "DatastoreStatus": DatastoreStatusType,
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
    },
    total=False,
)

_RequiredIdentityProviderConfigurationOutputTypeDef = TypedDict(
    "_RequiredIdentityProviderConfigurationOutputTypeDef",
    {
        "AuthorizationStrategy": AuthorizationStrategyType,
    },
)
_OptionalIdentityProviderConfigurationOutputTypeDef = TypedDict(
    "_OptionalIdentityProviderConfigurationOutputTypeDef",
    {
        "FineGrainedAuthorizationEnabled": bool,
        "Metadata": str,
        "IdpLambdaArn": str,
    },
    total=False,
)

class IdentityProviderConfigurationOutputTypeDef(
    _RequiredIdentityProviderConfigurationOutputTypeDef,
    _OptionalIdentityProviderConfigurationOutputTypeDef,
):
    pass

PreloadDataConfigOutputTypeDef = TypedDict(
    "PreloadDataConfigOutputTypeDef",
    {
        "PreloadDataType": Literal["SYNTHEA"],
    },
)

DeleteFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
)

DeleteFHIRDatastoreResponseTypeDef = TypedDict(
    "DeleteFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
)

DescribeFHIRExportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRExportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRImportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRImportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

InputDataConfigOutputTypeDef = TypedDict(
    "InputDataConfigOutputTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

_RequiredKmsEncryptionConfigOutputTypeDef = TypedDict(
    "_RequiredKmsEncryptionConfigOutputTypeDef",
    {
        "CmkType": CmkTypeType,
    },
)
_OptionalKmsEncryptionConfigOutputTypeDef = TypedDict(
    "_OptionalKmsEncryptionConfigOutputTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class KmsEncryptionConfigOutputTypeDef(
    _RequiredKmsEncryptionConfigOutputTypeDef, _OptionalKmsEncryptionConfigOutputTypeDef
):
    pass

_RequiredKmsEncryptionConfigTypeDef = TypedDict(
    "_RequiredKmsEncryptionConfigTypeDef",
    {
        "CmkType": CmkTypeType,
    },
)
_OptionalKmsEncryptionConfigTypeDef = TypedDict(
    "_OptionalKmsEncryptionConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class KmsEncryptionConfigTypeDef(
    _RequiredKmsEncryptionConfigTypeDef, _OptionalKmsEncryptionConfigTypeDef
):
    pass

_RequiredListFHIRExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListFHIRExportJobsRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
)
_OptionalListFHIRExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListFHIRExportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmittedBefore": Union[datetime, str],
        "SubmittedAfter": Union[datetime, str],
    },
    total=False,
)

class ListFHIRExportJobsRequestRequestTypeDef(
    _RequiredListFHIRExportJobsRequestRequestTypeDef,
    _OptionalListFHIRExportJobsRequestRequestTypeDef,
):
    pass

_RequiredListFHIRImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListFHIRImportJobsRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
)
_OptionalListFHIRImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListFHIRImportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmittedBefore": Union[datetime, str],
        "SubmittedAfter": Union[datetime, str],
    },
    total=False,
)

class ListFHIRImportJobsRequestRequestTypeDef(
    _RequiredListFHIRImportJobsRequestRequestTypeDef,
    _OptionalListFHIRImportJobsRequestRequestTypeDef,
):
    pass

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

S3ConfigurationOutputTypeDef = TypedDict(
    "S3ConfigurationOutputTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": str,
    },
)

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": str,
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

StartFHIRExportJobResponseTypeDef = TypedDict(
    "StartFHIRExportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartFHIRImportJobResponseTypeDef = TypedDict(
    "StartFHIRImportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

ListFHIRDatastoresRequestRequestTypeDef = TypedDict(
    "ListFHIRDatastoresRequestRequestTypeDef",
    {
        "Filter": DatastoreFilterTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

SseConfigurationOutputTypeDef = TypedDict(
    "SseConfigurationOutputTypeDef",
    {
        "KmsEncryptionConfig": KmsEncryptionConfigOutputTypeDef,
    },
)

SseConfigurationTypeDef = TypedDict(
    "SseConfigurationTypeDef",
    {
        "KmsEncryptionConfig": KmsEncryptionConfigTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigOutputTypeDef = TypedDict(
    "OutputDataConfigOutputTypeDef",
    {
        "S3Configuration": S3ConfigurationOutputTypeDef,
    },
    total=False,
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Configuration": S3ConfigurationTypeDef,
    },
    total=False,
)

_RequiredDatastorePropertiesTypeDef = TypedDict(
    "_RequiredDatastorePropertiesTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreTypeVersion": Literal["R4"],
        "DatastoreEndpoint": str,
    },
)
_OptionalDatastorePropertiesTypeDef = TypedDict(
    "_OptionalDatastorePropertiesTypeDef",
    {
        "DatastoreName": str,
        "CreatedAt": datetime,
        "SseConfiguration": SseConfigurationOutputTypeDef,
        "PreloadDataConfig": PreloadDataConfigOutputTypeDef,
        "IdentityProviderConfiguration": IdentityProviderConfigurationOutputTypeDef,
    },
    total=False,
)

class DatastorePropertiesTypeDef(
    _RequiredDatastorePropertiesTypeDef, _OptionalDatastorePropertiesTypeDef
):
    pass

_RequiredCreateFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreTypeVersion": Literal["R4"],
    },
)
_OptionalCreateFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreName": str,
        "SseConfiguration": SseConfigurationTypeDef,
        "PreloadDataConfig": PreloadDataConfigTypeDef,
        "ClientToken": str,
        "Tags": Sequence[TagTypeDef],
        "IdentityProviderConfiguration": IdentityProviderConfigurationTypeDef,
    },
    total=False,
)

class CreateFHIRDatastoreRequestRequestTypeDef(
    _RequiredCreateFHIRDatastoreRequestRequestTypeDef,
    _OptionalCreateFHIRDatastoreRequestRequestTypeDef,
):
    pass

_RequiredExportJobPropertiesTypeDef = TypedDict(
    "_RequiredExportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "OutputDataConfig": OutputDataConfigOutputTypeDef,
    },
)
_OptionalExportJobPropertiesTypeDef = TypedDict(
    "_OptionalExportJobPropertiesTypeDef",
    {
        "JobName": str,
        "EndTime": datetime,
        "DataAccessRoleArn": str,
        "Message": str,
    },
    total=False,
)

class ExportJobPropertiesTypeDef(
    _RequiredExportJobPropertiesTypeDef, _OptionalExportJobPropertiesTypeDef
):
    pass

_RequiredImportJobPropertiesTypeDef = TypedDict(
    "_RequiredImportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "InputDataConfig": InputDataConfigOutputTypeDef,
    },
)
_OptionalImportJobPropertiesTypeDef = TypedDict(
    "_OptionalImportJobPropertiesTypeDef",
    {
        "JobName": str,
        "EndTime": datetime,
        "JobOutputDataConfig": OutputDataConfigOutputTypeDef,
        "DataAccessRoleArn": str,
        "Message": str,
    },
    total=False,
)

class ImportJobPropertiesTypeDef(
    _RequiredImportJobPropertiesTypeDef, _OptionalImportJobPropertiesTypeDef
):
    pass

_RequiredStartFHIRExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartFHIRExportJobRequestRequestTypeDef",
    {
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
    },
)
_OptionalStartFHIRExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartFHIRExportJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
    total=False,
)

class StartFHIRExportJobRequestRequestTypeDef(
    _RequiredStartFHIRExportJobRequestRequestTypeDef,
    _OptionalStartFHIRExportJobRequestRequestTypeDef,
):
    pass

_RequiredStartFHIRImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartFHIRImportJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "JobOutputDataConfig": OutputDataConfigTypeDef,
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
    },
)
_OptionalStartFHIRImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartFHIRImportJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
    total=False,
)

class StartFHIRImportJobRequestRequestTypeDef(
    _RequiredStartFHIRImportJobRequestRequestTypeDef,
    _OptionalStartFHIRImportJobRequestRequestTypeDef,
):
    pass

DescribeFHIRDatastoreResponseTypeDef = TypedDict(
    "DescribeFHIRDatastoreResponseTypeDef",
    {
        "DatastoreProperties": DatastorePropertiesTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFHIRDatastoresResponseTypeDef = TypedDict(
    "ListFHIRDatastoresResponseTypeDef",
    {
        "DatastorePropertiesList": List[DatastorePropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRExportJobResponseTypeDef = TypedDict(
    "DescribeFHIRExportJobResponseTypeDef",
    {
        "ExportJobProperties": ExportJobPropertiesTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFHIRExportJobsResponseTypeDef = TypedDict(
    "ListFHIRExportJobsResponseTypeDef",
    {
        "ExportJobPropertiesList": List[ExportJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRImportJobResponseTypeDef = TypedDict(
    "DescribeFHIRImportJobResponseTypeDef",
    {
        "ImportJobProperties": ImportJobPropertiesTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFHIRImportJobsResponseTypeDef = TypedDict(
    "ListFHIRImportJobsResponseTypeDef",
    {
        "ImportJobPropertiesList": List[ImportJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
