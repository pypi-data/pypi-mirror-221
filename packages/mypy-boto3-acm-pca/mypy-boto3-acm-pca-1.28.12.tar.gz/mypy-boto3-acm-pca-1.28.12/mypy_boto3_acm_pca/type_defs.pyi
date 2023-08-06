"""
Type annotations for acm-pca service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/type_defs/)

Usage::

    ```python
    from mypy_boto3_acm_pca.type_defs import CustomAttributeOutputTypeDef

    data: CustomAttributeOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AccessMethodTypeType,
    ActionTypeType,
    AuditReportResponseFormatType,
    AuditReportStatusType,
    CertificateAuthorityStatusType,
    CertificateAuthorityTypeType,
    CertificateAuthorityUsageModeType,
    ExtendedKeyUsageTypeType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyStorageSecurityStandardType,
    ResourceOwnerType,
    RevocationReasonType,
    S3ObjectAclType,
    SigningAlgorithmType,
    ValidityPeriodTypeType,
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
    "CustomAttributeOutputTypeDef",
    "CustomAttributeTypeDef",
    "AccessMethodOutputTypeDef",
    "AccessMethodTypeDef",
    "CreateCertificateAuthorityAuditReportRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "CreatePermissionRequestRequestTypeDef",
    "CrlConfigurationOutputTypeDef",
    "CrlConfigurationTypeDef",
    "KeyUsageOutputTypeDef",
    "KeyUsageTypeDef",
    "CustomExtensionTypeDef",
    "DeleteCertificateAuthorityRequestRequestTypeDef",
    "DeletePermissionRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestRequestTypeDef",
    "DescribeCertificateAuthorityRequestRequestTypeDef",
    "EdiPartyNameOutputTypeDef",
    "EdiPartyNameTypeDef",
    "ExtendedKeyUsageTypeDef",
    "OtherNameOutputTypeDef",
    "OtherNameTypeDef",
    "GetCertificateAuthorityCertificateRequestRequestTypeDef",
    "GetCertificateAuthorityCsrRequestRequestTypeDef",
    "GetCertificateRequestRequestTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "ImportCertificateAuthorityCertificateRequestRequestTypeDef",
    "ValidityTypeDef",
    "PaginatorConfigTypeDef",
    "ListCertificateAuthoritiesRequestRequestTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "PermissionTypeDef",
    "ListTagsRequestRequestTypeDef",
    "TagOutputTypeDef",
    "OcspConfigurationOutputTypeDef",
    "OcspConfigurationTypeDef",
    "QualifierTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "RestoreCertificateAuthorityRequestRequestTypeDef",
    "RevokeCertificateRequestRequestTypeDef",
    "ASN1SubjectOutputTypeDef",
    "ASN1SubjectTypeDef",
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    "CreateCertificateAuthorityResponseTypeDef",
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCertificateAuthorityCertificateResponseTypeDef",
    "GetCertificateAuthorityCsrResponseTypeDef",
    "GetCertificateResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "IssueCertificateResponseTypeDef",
    "TagCertificateAuthorityRequestRequestTypeDef",
    "UntagCertificateAuthorityRequestRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef",
    "GetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef",
    "GetCertificateRequestCertificateIssuedWaitTypeDef",
    "ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateTypeDef",
    "ListPermissionsRequestListPermissionsPaginateTypeDef",
    "ListTagsRequestListTagsPaginateTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListTagsResponseTypeDef",
    "RevocationConfigurationOutputTypeDef",
    "RevocationConfigurationTypeDef",
    "PolicyQualifierInfoTypeDef",
    "GeneralNameOutputTypeDef",
    "GeneralNameTypeDef",
    "UpdateCertificateAuthorityRequestRequestTypeDef",
    "PolicyInformationTypeDef",
    "AccessDescriptionOutputTypeDef",
    "AccessDescriptionTypeDef",
    "ExtensionsTypeDef",
    "CsrExtensionsOutputTypeDef",
    "CsrExtensionsTypeDef",
    "ApiPassthroughTypeDef",
    "CertificateAuthorityConfigurationOutputTypeDef",
    "CertificateAuthorityConfigurationTypeDef",
    "IssueCertificateRequestRequestTypeDef",
    "CertificateAuthorityTypeDef",
    "CreateCertificateAuthorityRequestRequestTypeDef",
    "DescribeCertificateAuthorityResponseTypeDef",
    "ListCertificateAuthoritiesResponseTypeDef",
)

CustomAttributeOutputTypeDef = TypedDict(
    "CustomAttributeOutputTypeDef",
    {
        "ObjectIdentifier": str,
        "Value": str,
    },
)

CustomAttributeTypeDef = TypedDict(
    "CustomAttributeTypeDef",
    {
        "ObjectIdentifier": str,
        "Value": str,
    },
)

AccessMethodOutputTypeDef = TypedDict(
    "AccessMethodOutputTypeDef",
    {
        "CustomObjectIdentifier": str,
        "AccessMethodType": AccessMethodTypeType,
    },
    total=False,
)

AccessMethodTypeDef = TypedDict(
    "AccessMethodTypeDef",
    {
        "CustomObjectIdentifier": str,
        "AccessMethodType": AccessMethodTypeType,
    },
    total=False,
)

CreateCertificateAuthorityAuditReportRequestRequestTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "S3BucketName": str,
        "AuditReportResponseFormat": AuditReportResponseFormatType,
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

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

_RequiredCreatePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
        "Actions": Sequence[ActionTypeType],
    },
)
_OptionalCreatePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionRequestRequestTypeDef",
    {
        "SourceAccount": str,
    },
    total=False,
)

class CreatePermissionRequestRequestTypeDef(
    _RequiredCreatePermissionRequestRequestTypeDef, _OptionalCreatePermissionRequestRequestTypeDef
):
    pass

_RequiredCrlConfigurationOutputTypeDef = TypedDict(
    "_RequiredCrlConfigurationOutputTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCrlConfigurationOutputTypeDef = TypedDict(
    "_OptionalCrlConfigurationOutputTypeDef",
    {
        "ExpirationInDays": int,
        "CustomCname": str,
        "S3BucketName": str,
        "S3ObjectAcl": S3ObjectAclType,
    },
    total=False,
)

class CrlConfigurationOutputTypeDef(
    _RequiredCrlConfigurationOutputTypeDef, _OptionalCrlConfigurationOutputTypeDef
):
    pass

_RequiredCrlConfigurationTypeDef = TypedDict(
    "_RequiredCrlConfigurationTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCrlConfigurationTypeDef = TypedDict(
    "_OptionalCrlConfigurationTypeDef",
    {
        "ExpirationInDays": int,
        "CustomCname": str,
        "S3BucketName": str,
        "S3ObjectAcl": S3ObjectAclType,
    },
    total=False,
)

class CrlConfigurationTypeDef(_RequiredCrlConfigurationTypeDef, _OptionalCrlConfigurationTypeDef):
    pass

KeyUsageOutputTypeDef = TypedDict(
    "KeyUsageOutputTypeDef",
    {
        "DigitalSignature": bool,
        "NonRepudiation": bool,
        "KeyEncipherment": bool,
        "DataEncipherment": bool,
        "KeyAgreement": bool,
        "KeyCertSign": bool,
        "CRLSign": bool,
        "EncipherOnly": bool,
        "DecipherOnly": bool,
    },
    total=False,
)

KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "DigitalSignature": bool,
        "NonRepudiation": bool,
        "KeyEncipherment": bool,
        "DataEncipherment": bool,
        "KeyAgreement": bool,
        "KeyCertSign": bool,
        "CRLSign": bool,
        "EncipherOnly": bool,
        "DecipherOnly": bool,
    },
    total=False,
)

_RequiredCustomExtensionTypeDef = TypedDict(
    "_RequiredCustomExtensionTypeDef",
    {
        "ObjectIdentifier": str,
        "Value": str,
    },
)
_OptionalCustomExtensionTypeDef = TypedDict(
    "_OptionalCustomExtensionTypeDef",
    {
        "Critical": bool,
    },
    total=False,
)

class CustomExtensionTypeDef(_RequiredCustomExtensionTypeDef, _OptionalCustomExtensionTypeDef):
    pass

_RequiredDeleteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalDeleteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCertificateAuthorityRequestRequestTypeDef",
    {
        "PermanentDeletionTimeInDays": int,
    },
    total=False,
)

class DeleteCertificateAuthorityRequestRequestTypeDef(
    _RequiredDeleteCertificateAuthorityRequestRequestTypeDef,
    _OptionalDeleteCertificateAuthorityRequestRequestTypeDef,
):
    pass

_RequiredDeletePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePermissionRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
    },
)
_OptionalDeletePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePermissionRequestRequestTypeDef",
    {
        "SourceAccount": str,
    },
    total=False,
)

class DeletePermissionRequestRequestTypeDef(
    _RequiredDeletePermissionRequestRequestTypeDef, _OptionalDeletePermissionRequestRequestTypeDef
):
    pass

DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

DescribeCertificateAuthorityAuditReportRequestRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "AuditReportId": str,
    },
)

DescribeCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

_RequiredEdiPartyNameOutputTypeDef = TypedDict(
    "_RequiredEdiPartyNameOutputTypeDef",
    {
        "PartyName": str,
    },
)
_OptionalEdiPartyNameOutputTypeDef = TypedDict(
    "_OptionalEdiPartyNameOutputTypeDef",
    {
        "NameAssigner": str,
    },
    total=False,
)

class EdiPartyNameOutputTypeDef(
    _RequiredEdiPartyNameOutputTypeDef, _OptionalEdiPartyNameOutputTypeDef
):
    pass

_RequiredEdiPartyNameTypeDef = TypedDict(
    "_RequiredEdiPartyNameTypeDef",
    {
        "PartyName": str,
    },
)
_OptionalEdiPartyNameTypeDef = TypedDict(
    "_OptionalEdiPartyNameTypeDef",
    {
        "NameAssigner": str,
    },
    total=False,
)

class EdiPartyNameTypeDef(_RequiredEdiPartyNameTypeDef, _OptionalEdiPartyNameTypeDef):
    pass

ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "ExtendedKeyUsageType": ExtendedKeyUsageTypeType,
        "ExtendedKeyUsageObjectIdentifier": str,
    },
    total=False,
)

OtherNameOutputTypeDef = TypedDict(
    "OtherNameOutputTypeDef",
    {
        "TypeId": str,
        "Value": str,
    },
)

OtherNameTypeDef = TypedDict(
    "OtherNameTypeDef",
    {
        "TypeId": str,
        "Value": str,
    },
)

GetCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

GetCertificateAuthorityCsrRequestRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCsrRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

GetCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateArn": str,
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

_RequiredImportCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredImportCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Certificate": Union[str, bytes, IO[Any], StreamingBody],
    },
)
_OptionalImportCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalImportCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateChain": Union[str, bytes, IO[Any], StreamingBody],
    },
    total=False,
)

class ImportCertificateAuthorityCertificateRequestRequestTypeDef(
    _RequiredImportCertificateAuthorityCertificateRequestRequestTypeDef,
    _OptionalImportCertificateAuthorityCertificateRequestRequestTypeDef,
):
    pass

ValidityTypeDef = TypedDict(
    "ValidityTypeDef",
    {
        "Value": int,
        "Type": ValidityPeriodTypeType,
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

ListCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "ListCertificateAuthoritiesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResourceOwner": ResourceOwnerType,
    },
    total=False,
)

_RequiredListPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionsRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalListPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPermissionsRequestRequestTypeDef(
    _RequiredListPermissionsRequestRequestTypeDef, _OptionalListPermissionsRequestRequestTypeDef
):
    pass

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": datetime,
        "Principal": str,
        "SourceAccount": str,
        "Actions": List[ActionTypeType],
        "Policy": str,
    },
    total=False,
)

_RequiredListTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalListTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsRequestRequestTypeDef(
    _RequiredListTagsRequestRequestTypeDef, _OptionalListTagsRequestRequestTypeDef
):
    pass

_RequiredTagOutputTypeDef = TypedDict(
    "_RequiredTagOutputTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagOutputTypeDef = TypedDict(
    "_OptionalTagOutputTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagOutputTypeDef(_RequiredTagOutputTypeDef, _OptionalTagOutputTypeDef):
    pass

_RequiredOcspConfigurationOutputTypeDef = TypedDict(
    "_RequiredOcspConfigurationOutputTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalOcspConfigurationOutputTypeDef = TypedDict(
    "_OptionalOcspConfigurationOutputTypeDef",
    {
        "OcspCustomCname": str,
    },
    total=False,
)

class OcspConfigurationOutputTypeDef(
    _RequiredOcspConfigurationOutputTypeDef, _OptionalOcspConfigurationOutputTypeDef
):
    pass

_RequiredOcspConfigurationTypeDef = TypedDict(
    "_RequiredOcspConfigurationTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalOcspConfigurationTypeDef = TypedDict(
    "_OptionalOcspConfigurationTypeDef",
    {
        "OcspCustomCname": str,
    },
    total=False,
)

class OcspConfigurationTypeDef(
    _RequiredOcspConfigurationTypeDef, _OptionalOcspConfigurationTypeDef
):
    pass

QualifierTypeDef = TypedDict(
    "QualifierTypeDef",
    {
        "CpsUri": str,
    },
)

PutPolicyRequestRequestTypeDef = TypedDict(
    "PutPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

RestoreCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "RestoreCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

RevokeCertificateRequestRequestTypeDef = TypedDict(
    "RevokeCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateSerial": str,
        "RevocationReason": RevocationReasonType,
    },
)

ASN1SubjectOutputTypeDef = TypedDict(
    "ASN1SubjectOutputTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
        "CustomAttributes": List[CustomAttributeOutputTypeDef],
    },
    total=False,
)

ASN1SubjectTypeDef = TypedDict(
    "ASN1SubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
        "CustomAttributes": Sequence[CustomAttributeTypeDef],
    },
    total=False,
)

CreateCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportId": str,
        "S3Key": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthorityArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportStatus": AuditReportStatusType,
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetCertificateAuthorityCertificateResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetCertificateAuthorityCsrResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCsrResponseTypeDef",
    {
        "Csr": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

IssueCertificateResponseTypeDef = TypedDict(
    "IssueCertificateResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "TagCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

UntagCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "UntagCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredDescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef = TypedDict(
    "_RequiredDescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef",
    {
        "CertificateAuthorityArn": str,
        "AuditReportId": str,
    },
)
_OptionalDescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef = TypedDict(
    "_OptionalDescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef(
    _RequiredDescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef,
    _OptionalDescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef,
):
    pass

_RequiredGetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef = TypedDict(
    "_RequiredGetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalGetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef = TypedDict(
    "_OptionalGetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class GetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef(
    _RequiredGetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef,
    _OptionalGetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef,
):
    pass

_RequiredGetCertificateRequestCertificateIssuedWaitTypeDef = TypedDict(
    "_RequiredGetCertificateRequestCertificateIssuedWaitTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateArn": str,
    },
)
_OptionalGetCertificateRequestCertificateIssuedWaitTypeDef = TypedDict(
    "_OptionalGetCertificateRequestCertificateIssuedWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class GetCertificateRequestCertificateIssuedWaitTypeDef(
    _RequiredGetCertificateRequestCertificateIssuedWaitTypeDef,
    _OptionalGetCertificateRequestCertificateIssuedWaitTypeDef,
):
    pass

ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateTypeDef = TypedDict(
    "ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateTypeDef",
    {
        "ResourceOwner": ResourceOwnerType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListPermissionsRequestListPermissionsPaginateTypeDef = TypedDict(
    "_RequiredListPermissionsRequestListPermissionsPaginateTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalListPermissionsRequestListPermissionsPaginateTypeDef = TypedDict(
    "_OptionalListPermissionsRequestListPermissionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListPermissionsRequestListPermissionsPaginateTypeDef(
    _RequiredListPermissionsRequestListPermissionsPaginateTypeDef,
    _OptionalListPermissionsRequestListPermissionsPaginateTypeDef,
):
    pass

_RequiredListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "_RequiredListTagsRequestListTagsPaginateTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "_OptionalListTagsRequestListTagsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListTagsRequestListTagsPaginateTypeDef(
    _RequiredListTagsRequestListTagsPaginateTypeDef, _OptionalListTagsRequestListTagsPaginateTypeDef
):
    pass

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "Permissions": List[PermissionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RevocationConfigurationOutputTypeDef = TypedDict(
    "RevocationConfigurationOutputTypeDef",
    {
        "CrlConfiguration": CrlConfigurationOutputTypeDef,
        "OcspConfiguration": OcspConfigurationOutputTypeDef,
    },
    total=False,
)

RevocationConfigurationTypeDef = TypedDict(
    "RevocationConfigurationTypeDef",
    {
        "CrlConfiguration": CrlConfigurationTypeDef,
        "OcspConfiguration": OcspConfigurationTypeDef,
    },
    total=False,
)

PolicyQualifierInfoTypeDef = TypedDict(
    "PolicyQualifierInfoTypeDef",
    {
        "PolicyQualifierId": Literal["CPS"],
        "Qualifier": QualifierTypeDef,
    },
)

GeneralNameOutputTypeDef = TypedDict(
    "GeneralNameOutputTypeDef",
    {
        "OtherName": OtherNameOutputTypeDef,
        "Rfc822Name": str,
        "DnsName": str,
        "DirectoryName": ASN1SubjectOutputTypeDef,
        "EdiPartyName": EdiPartyNameOutputTypeDef,
        "UniformResourceIdentifier": str,
        "IpAddress": str,
        "RegisteredId": str,
    },
    total=False,
)

GeneralNameTypeDef = TypedDict(
    "GeneralNameTypeDef",
    {
        "OtherName": OtherNameTypeDef,
        "Rfc822Name": str,
        "DnsName": str,
        "DirectoryName": ASN1SubjectTypeDef,
        "EdiPartyName": EdiPartyNameTypeDef,
        "UniformResourceIdentifier": str,
        "IpAddress": str,
        "RegisteredId": str,
    },
    total=False,
)

_RequiredUpdateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalUpdateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCertificateAuthorityRequestRequestTypeDef",
    {
        "RevocationConfiguration": RevocationConfigurationTypeDef,
        "Status": CertificateAuthorityStatusType,
    },
    total=False,
)

class UpdateCertificateAuthorityRequestRequestTypeDef(
    _RequiredUpdateCertificateAuthorityRequestRequestTypeDef,
    _OptionalUpdateCertificateAuthorityRequestRequestTypeDef,
):
    pass

_RequiredPolicyInformationTypeDef = TypedDict(
    "_RequiredPolicyInformationTypeDef",
    {
        "CertPolicyId": str,
    },
)
_OptionalPolicyInformationTypeDef = TypedDict(
    "_OptionalPolicyInformationTypeDef",
    {
        "PolicyQualifiers": Sequence[PolicyQualifierInfoTypeDef],
    },
    total=False,
)

class PolicyInformationTypeDef(
    _RequiredPolicyInformationTypeDef, _OptionalPolicyInformationTypeDef
):
    pass

AccessDescriptionOutputTypeDef = TypedDict(
    "AccessDescriptionOutputTypeDef",
    {
        "AccessMethod": AccessMethodOutputTypeDef,
        "AccessLocation": GeneralNameOutputTypeDef,
    },
)

AccessDescriptionTypeDef = TypedDict(
    "AccessDescriptionTypeDef",
    {
        "AccessMethod": AccessMethodTypeDef,
        "AccessLocation": GeneralNameTypeDef,
    },
)

ExtensionsTypeDef = TypedDict(
    "ExtensionsTypeDef",
    {
        "CertificatePolicies": Sequence[PolicyInformationTypeDef],
        "ExtendedKeyUsage": Sequence[ExtendedKeyUsageTypeDef],
        "KeyUsage": KeyUsageTypeDef,
        "SubjectAlternativeNames": Sequence[GeneralNameTypeDef],
        "CustomExtensions": Sequence[CustomExtensionTypeDef],
    },
    total=False,
)

CsrExtensionsOutputTypeDef = TypedDict(
    "CsrExtensionsOutputTypeDef",
    {
        "KeyUsage": KeyUsageOutputTypeDef,
        "SubjectInformationAccess": List[AccessDescriptionOutputTypeDef],
    },
    total=False,
)

CsrExtensionsTypeDef = TypedDict(
    "CsrExtensionsTypeDef",
    {
        "KeyUsage": KeyUsageTypeDef,
        "SubjectInformationAccess": Sequence[AccessDescriptionTypeDef],
    },
    total=False,
)

ApiPassthroughTypeDef = TypedDict(
    "ApiPassthroughTypeDef",
    {
        "Extensions": ExtensionsTypeDef,
        "Subject": ASN1SubjectTypeDef,
    },
    total=False,
)

_RequiredCertificateAuthorityConfigurationOutputTypeDef = TypedDict(
    "_RequiredCertificateAuthorityConfigurationOutputTypeDef",
    {
        "KeyAlgorithm": KeyAlgorithmType,
        "SigningAlgorithm": SigningAlgorithmType,
        "Subject": ASN1SubjectOutputTypeDef,
    },
)
_OptionalCertificateAuthorityConfigurationOutputTypeDef = TypedDict(
    "_OptionalCertificateAuthorityConfigurationOutputTypeDef",
    {
        "CsrExtensions": CsrExtensionsOutputTypeDef,
    },
    total=False,
)

class CertificateAuthorityConfigurationOutputTypeDef(
    _RequiredCertificateAuthorityConfigurationOutputTypeDef,
    _OptionalCertificateAuthorityConfigurationOutputTypeDef,
):
    pass

_RequiredCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_RequiredCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": KeyAlgorithmType,
        "SigningAlgorithm": SigningAlgorithmType,
        "Subject": ASN1SubjectTypeDef,
    },
)
_OptionalCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_OptionalCertificateAuthorityConfigurationTypeDef",
    {
        "CsrExtensions": CsrExtensionsTypeDef,
    },
    total=False,
)

class CertificateAuthorityConfigurationTypeDef(
    _RequiredCertificateAuthorityConfigurationTypeDef,
    _OptionalCertificateAuthorityConfigurationTypeDef,
):
    pass

_RequiredIssueCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredIssueCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Csr": Union[str, bytes, IO[Any], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmType,
        "Validity": ValidityTypeDef,
    },
)
_OptionalIssueCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalIssueCertificateRequestRequestTypeDef",
    {
        "ApiPassthrough": ApiPassthroughTypeDef,
        "TemplateArn": str,
        "ValidityNotBefore": ValidityTypeDef,
        "IdempotencyToken": str,
    },
    total=False,
)

class IssueCertificateRequestRequestTypeDef(
    _RequiredIssueCertificateRequestRequestTypeDef, _OptionalIssueCertificateRequestRequestTypeDef
):
    pass

CertificateAuthorityTypeDef = TypedDict(
    "CertificateAuthorityTypeDef",
    {
        "Arn": str,
        "OwnerAccount": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": CertificateAuthorityTypeType,
        "Serial": str,
        "Status": CertificateAuthorityStatusType,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": FailureReasonType,
        "CertificateAuthorityConfiguration": CertificateAuthorityConfigurationOutputTypeDef,
        "RevocationConfiguration": RevocationConfigurationOutputTypeDef,
        "RestorableUntil": datetime,
        "KeyStorageSecurityStandard": KeyStorageSecurityStandardType,
        "UsageMode": CertificateAuthorityUsageModeType,
    },
    total=False,
)

_RequiredCreateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityConfiguration": CertificateAuthorityConfigurationTypeDef,
        "CertificateAuthorityType": CertificateAuthorityTypeType,
    },
)
_OptionalCreateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCertificateAuthorityRequestRequestTypeDef",
    {
        "RevocationConfiguration": RevocationConfigurationTypeDef,
        "IdempotencyToken": str,
        "KeyStorageSecurityStandard": KeyStorageSecurityStandardType,
        "Tags": Sequence[TagTypeDef],
        "UsageMode": CertificateAuthorityUsageModeType,
    },
    total=False,
)

class CreateCertificateAuthorityRequestRequestTypeDef(
    _RequiredCreateCertificateAuthorityRequestRequestTypeDef,
    _OptionalCreateCertificateAuthorityRequestRequestTypeDef,
):
    pass

DescribeCertificateAuthorityResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthority": CertificateAuthorityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListCertificateAuthoritiesResponseTypeDef",
    {
        "CertificateAuthorities": List[CertificateAuthorityTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
