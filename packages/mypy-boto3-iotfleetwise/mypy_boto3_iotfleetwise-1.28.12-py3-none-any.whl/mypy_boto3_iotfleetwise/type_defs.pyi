"""
Type annotations for iotfleetwise service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotfleetwise.type_defs import ActuatorOutputTypeDef

    data: ActuatorOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    CampaignStatusType,
    CompressionType,
    DataFormatType,
    DiagnosticsModeType,
    LogTypeType,
    ManifestStatusType,
    NetworkInterfaceTypeType,
    NodeDataTypeType,
    RegistrationStatusType,
    SignalDecoderTypeType,
    SpoolingModeType,
    StorageCompressionFormatType,
    TriggerModeType,
    UpdateCampaignActionType,
    UpdateModeType,
    VehicleAssociationBehaviorType,
    VehicleStateType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActuatorOutputTypeDef",
    "ActuatorTypeDef",
    "AssociateVehicleFleetRequestRequestTypeDef",
    "AttributeOutputTypeDef",
    "AttributeTypeDef",
    "CreateVehicleErrorTypeDef",
    "CreateVehicleResponseItemTypeDef",
    "UpdateVehicleRequestItemTypeDef",
    "UpdateVehicleErrorTypeDef",
    "UpdateVehicleResponseItemTypeDef",
    "BranchOutputTypeDef",
    "BranchTypeDef",
    "CampaignSummaryTypeDef",
    "CanDbcDefinitionTypeDef",
    "CanInterfaceOutputTypeDef",
    "CanInterfaceTypeDef",
    "CanSignalOutputTypeDef",
    "CanSignalTypeDef",
    "CloudWatchLogDeliveryOptionsOutputTypeDef",
    "CloudWatchLogDeliveryOptionsTypeDef",
    "ConditionBasedCollectionSchemeOutputTypeDef",
    "TimeBasedCollectionSchemeOutputTypeDef",
    "ConditionBasedCollectionSchemeTypeDef",
    "TimeBasedCollectionSchemeTypeDef",
    "SignalInformationTypeDef",
    "TagTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDecoderManifestResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateModelManifestResponseTypeDef",
    "CreateSignalCatalogResponseTypeDef",
    "CreateVehicleResponseTypeDef",
    "S3ConfigOutputTypeDef",
    "TimestreamConfigOutputTypeDef",
    "S3ConfigTypeDef",
    "TimestreamConfigTypeDef",
    "DecoderManifestSummaryTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteDecoderManifestRequestRequestTypeDef",
    "DeleteDecoderManifestResponseTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteFleetResponseTypeDef",
    "DeleteModelManifestRequestRequestTypeDef",
    "DeleteModelManifestResponseTypeDef",
    "DeleteSignalCatalogRequestRequestTypeDef",
    "DeleteSignalCatalogResponseTypeDef",
    "DeleteVehicleRequestRequestTypeDef",
    "DeleteVehicleResponseTypeDef",
    "DisassociateVehicleFleetRequestRequestTypeDef",
    "FleetSummaryTypeDef",
    "FormattedVssTypeDef",
    "GetCampaignRequestRequestTypeDef",
    "SignalInformationOutputTypeDef",
    "GetDecoderManifestRequestRequestTypeDef",
    "GetDecoderManifestResponseTypeDef",
    "GetFleetRequestRequestTypeDef",
    "GetFleetResponseTypeDef",
    "GetModelManifestRequestRequestTypeDef",
    "GetModelManifestResponseTypeDef",
    "IamRegistrationResponseTypeDef",
    "TimestreamRegistrationResponseTypeDef",
    "GetSignalCatalogRequestRequestTypeDef",
    "NodeCountsTypeDef",
    "GetVehicleRequestRequestTypeDef",
    "GetVehicleResponseTypeDef",
    "GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef",
    "GetVehicleStatusRequestRequestTypeDef",
    "VehicleStatusTypeDef",
    "IamResourcesOutputTypeDef",
    "IamResourcesTypeDef",
    "ImportDecoderManifestResponseTypeDef",
    "ImportSignalCatalogResponseTypeDef",
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    "ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef",
    "ListDecoderManifestSignalsRequestRequestTypeDef",
    "ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef",
    "ListDecoderManifestsRequestRequestTypeDef",
    "ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef",
    "ListFleetsForVehicleRequestRequestTypeDef",
    "ListFleetsForVehicleResponseTypeDef",
    "ListFleetsRequestListFleetsPaginateTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef",
    "ListModelManifestNodesRequestRequestTypeDef",
    "ListModelManifestsRequestListModelManifestsPaginateTypeDef",
    "ListModelManifestsRequestRequestTypeDef",
    "ModelManifestSummaryTypeDef",
    "ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef",
    "ListSignalCatalogNodesRequestRequestTypeDef",
    "ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef",
    "ListSignalCatalogsRequestRequestTypeDef",
    "SignalCatalogSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagOutputTypeDef",
    "ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef",
    "ListVehiclesInFleetRequestRequestTypeDef",
    "ListVehiclesInFleetResponseTypeDef",
    "ListVehiclesRequestListVehiclesPaginateTypeDef",
    "ListVehiclesRequestRequestTypeDef",
    "VehicleSummaryTypeDef",
    "ObdInterfaceOutputTypeDef",
    "ObdInterfaceTypeDef",
    "SensorOutputTypeDef",
    "SensorTypeDef",
    "ObdSignalOutputTypeDef",
    "ObdSignalTypeDef",
    "PaginatorConfigTypeDef",
    "TimestreamResourcesTypeDef",
    "TimestreamResourcesOutputTypeDef",
    "ResponseMetadataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateDecoderManifestResponseTypeDef",
    "UpdateFleetRequestRequestTypeDef",
    "UpdateFleetResponseTypeDef",
    "UpdateModelManifestRequestRequestTypeDef",
    "UpdateModelManifestResponseTypeDef",
    "UpdateSignalCatalogResponseTypeDef",
    "UpdateVehicleRequestRequestTypeDef",
    "UpdateVehicleResponseTypeDef",
    "BatchCreateVehicleResponseTypeDef",
    "BatchUpdateVehicleRequestRequestTypeDef",
    "BatchUpdateVehicleResponseTypeDef",
    "ListCampaignsResponseTypeDef",
    "NetworkFileDefinitionTypeDef",
    "GetLoggingOptionsResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "CollectionSchemeOutputTypeDef",
    "CollectionSchemeTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateModelManifestRequestRequestTypeDef",
    "CreateVehicleRequestItemTypeDef",
    "CreateVehicleRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DataDestinationConfigOutputTypeDef",
    "DataDestinationConfigTypeDef",
    "ListDecoderManifestsResponseTypeDef",
    "ListFleetsResponseTypeDef",
    "ImportSignalCatalogRequestRequestTypeDef",
    "GetRegisterAccountStatusResponseTypeDef",
    "GetSignalCatalogResponseTypeDef",
    "GetVehicleStatusResponseTypeDef",
    "ListModelManifestsResponseTypeDef",
    "ListSignalCatalogsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVehiclesResponseTypeDef",
    "NetworkInterfaceOutputTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeOutputTypeDef",
    "NodeTypeDef",
    "SignalDecoderOutputTypeDef",
    "SignalDecoderTypeDef",
    "RegisterAccountRequestRequestTypeDef",
    "RegisterAccountResponseTypeDef",
    "ImportDecoderManifestRequestRequestTypeDef",
    "BatchCreateVehicleRequestRequestTypeDef",
    "GetCampaignResponseTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    "ListModelManifestNodesResponseTypeDef",
    "ListSignalCatalogNodesResponseTypeDef",
    "CreateSignalCatalogRequestRequestTypeDef",
    "UpdateSignalCatalogRequestRequestTypeDef",
    "ListDecoderManifestSignalsResponseTypeDef",
    "CreateDecoderManifestRequestRequestTypeDef",
    "UpdateDecoderManifestRequestRequestTypeDef",
)

_RequiredActuatorOutputTypeDef = TypedDict(
    "_RequiredActuatorOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalActuatorOutputTypeDef = TypedDict(
    "_OptionalActuatorOutputTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": List[str],
        "min": float,
        "max": float,
        "assignedValue": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class ActuatorOutputTypeDef(_RequiredActuatorOutputTypeDef, _OptionalActuatorOutputTypeDef):
    pass

_RequiredActuatorTypeDef = TypedDict(
    "_RequiredActuatorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalActuatorTypeDef = TypedDict(
    "_OptionalActuatorTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": Sequence[str],
        "min": float,
        "max": float,
        "assignedValue": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class ActuatorTypeDef(_RequiredActuatorTypeDef, _OptionalActuatorTypeDef):
    pass

AssociateVehicleFleetRequestRequestTypeDef = TypedDict(
    "AssociateVehicleFleetRequestRequestTypeDef",
    {
        "vehicleName": str,
        "fleetId": str,
    },
)

_RequiredAttributeOutputTypeDef = TypedDict(
    "_RequiredAttributeOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalAttributeOutputTypeDef = TypedDict(
    "_OptionalAttributeOutputTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": List[str],
        "min": float,
        "max": float,
        "assignedValue": str,
        "defaultValue": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class AttributeOutputTypeDef(_RequiredAttributeOutputTypeDef, _OptionalAttributeOutputTypeDef):
    pass

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": Sequence[str],
        "min": float,
        "max": float,
        "assignedValue": str,
        "defaultValue": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

CreateVehicleErrorTypeDef = TypedDict(
    "CreateVehicleErrorTypeDef",
    {
        "vehicleName": str,
        "code": str,
        "message": str,
    },
    total=False,
)

CreateVehicleResponseItemTypeDef = TypedDict(
    "CreateVehicleResponseItemTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "thingArn": str,
    },
    total=False,
)

_RequiredUpdateVehicleRequestItemTypeDef = TypedDict(
    "_RequiredUpdateVehicleRequestItemTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalUpdateVehicleRequestItemTypeDef = TypedDict(
    "_OptionalUpdateVehicleRequestItemTypeDef",
    {
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Mapping[str, str],
        "attributeUpdateMode": UpdateModeType,
    },
    total=False,
)

class UpdateVehicleRequestItemTypeDef(
    _RequiredUpdateVehicleRequestItemTypeDef, _OptionalUpdateVehicleRequestItemTypeDef
):
    pass

UpdateVehicleErrorTypeDef = TypedDict(
    "UpdateVehicleErrorTypeDef",
    {
        "vehicleName": str,
        "code": int,
        "message": str,
    },
    total=False,
)

UpdateVehicleResponseItemTypeDef = TypedDict(
    "UpdateVehicleResponseItemTypeDef",
    {
        "vehicleName": str,
        "arn": str,
    },
    total=False,
)

_RequiredBranchOutputTypeDef = TypedDict(
    "_RequiredBranchOutputTypeDef",
    {
        "fullyQualifiedName": str,
    },
)
_OptionalBranchOutputTypeDef = TypedDict(
    "_OptionalBranchOutputTypeDef",
    {
        "description": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class BranchOutputTypeDef(_RequiredBranchOutputTypeDef, _OptionalBranchOutputTypeDef):
    pass

_RequiredBranchTypeDef = TypedDict(
    "_RequiredBranchTypeDef",
    {
        "fullyQualifiedName": str,
    },
)
_OptionalBranchTypeDef = TypedDict(
    "_OptionalBranchTypeDef",
    {
        "description": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class BranchTypeDef(_RequiredBranchTypeDef, _OptionalBranchTypeDef):
    pass

_RequiredCampaignSummaryTypeDef = TypedDict(
    "_RequiredCampaignSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalCampaignSummaryTypeDef = TypedDict(
    "_OptionalCampaignSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "status": CampaignStatusType,
    },
    total=False,
)

class CampaignSummaryTypeDef(_RequiredCampaignSummaryTypeDef, _OptionalCampaignSummaryTypeDef):
    pass

_RequiredCanDbcDefinitionTypeDef = TypedDict(
    "_RequiredCanDbcDefinitionTypeDef",
    {
        "networkInterface": str,
        "canDbcFiles": Sequence[Union[str, bytes, IO[Any], StreamingBody]],
    },
)
_OptionalCanDbcDefinitionTypeDef = TypedDict(
    "_OptionalCanDbcDefinitionTypeDef",
    {
        "signalsMap": Mapping[str, str],
    },
    total=False,
)

class CanDbcDefinitionTypeDef(_RequiredCanDbcDefinitionTypeDef, _OptionalCanDbcDefinitionTypeDef):
    pass

_RequiredCanInterfaceOutputTypeDef = TypedDict(
    "_RequiredCanInterfaceOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalCanInterfaceOutputTypeDef = TypedDict(
    "_OptionalCanInterfaceOutputTypeDef",
    {
        "protocolName": str,
        "protocolVersion": str,
    },
    total=False,
)

class CanInterfaceOutputTypeDef(
    _RequiredCanInterfaceOutputTypeDef, _OptionalCanInterfaceOutputTypeDef
):
    pass

_RequiredCanInterfaceTypeDef = TypedDict(
    "_RequiredCanInterfaceTypeDef",
    {
        "name": str,
    },
)
_OptionalCanInterfaceTypeDef = TypedDict(
    "_OptionalCanInterfaceTypeDef",
    {
        "protocolName": str,
        "protocolVersion": str,
    },
    total=False,
)

class CanInterfaceTypeDef(_RequiredCanInterfaceTypeDef, _OptionalCanInterfaceTypeDef):
    pass

_RequiredCanSignalOutputTypeDef = TypedDict(
    "_RequiredCanSignalOutputTypeDef",
    {
        "messageId": int,
        "isBigEndian": bool,
        "isSigned": bool,
        "startBit": int,
        "offset": float,
        "factor": float,
        "length": int,
    },
)
_OptionalCanSignalOutputTypeDef = TypedDict(
    "_OptionalCanSignalOutputTypeDef",
    {
        "name": str,
    },
    total=False,
)

class CanSignalOutputTypeDef(_RequiredCanSignalOutputTypeDef, _OptionalCanSignalOutputTypeDef):
    pass

_RequiredCanSignalTypeDef = TypedDict(
    "_RequiredCanSignalTypeDef",
    {
        "messageId": int,
        "isBigEndian": bool,
        "isSigned": bool,
        "startBit": int,
        "offset": float,
        "factor": float,
        "length": int,
    },
)
_OptionalCanSignalTypeDef = TypedDict(
    "_OptionalCanSignalTypeDef",
    {
        "name": str,
    },
    total=False,
)

class CanSignalTypeDef(_RequiredCanSignalTypeDef, _OptionalCanSignalTypeDef):
    pass

_RequiredCloudWatchLogDeliveryOptionsOutputTypeDef = TypedDict(
    "_RequiredCloudWatchLogDeliveryOptionsOutputTypeDef",
    {
        "logType": LogTypeType,
    },
)
_OptionalCloudWatchLogDeliveryOptionsOutputTypeDef = TypedDict(
    "_OptionalCloudWatchLogDeliveryOptionsOutputTypeDef",
    {
        "logGroupName": str,
    },
    total=False,
)

class CloudWatchLogDeliveryOptionsOutputTypeDef(
    _RequiredCloudWatchLogDeliveryOptionsOutputTypeDef,
    _OptionalCloudWatchLogDeliveryOptionsOutputTypeDef,
):
    pass

_RequiredCloudWatchLogDeliveryOptionsTypeDef = TypedDict(
    "_RequiredCloudWatchLogDeliveryOptionsTypeDef",
    {
        "logType": LogTypeType,
    },
)
_OptionalCloudWatchLogDeliveryOptionsTypeDef = TypedDict(
    "_OptionalCloudWatchLogDeliveryOptionsTypeDef",
    {
        "logGroupName": str,
    },
    total=False,
)

class CloudWatchLogDeliveryOptionsTypeDef(
    _RequiredCloudWatchLogDeliveryOptionsTypeDef, _OptionalCloudWatchLogDeliveryOptionsTypeDef
):
    pass

_RequiredConditionBasedCollectionSchemeOutputTypeDef = TypedDict(
    "_RequiredConditionBasedCollectionSchemeOutputTypeDef",
    {
        "expression": str,
    },
)
_OptionalConditionBasedCollectionSchemeOutputTypeDef = TypedDict(
    "_OptionalConditionBasedCollectionSchemeOutputTypeDef",
    {
        "minimumTriggerIntervalMs": int,
        "triggerMode": TriggerModeType,
        "conditionLanguageVersion": int,
    },
    total=False,
)

class ConditionBasedCollectionSchemeOutputTypeDef(
    _RequiredConditionBasedCollectionSchemeOutputTypeDef,
    _OptionalConditionBasedCollectionSchemeOutputTypeDef,
):
    pass

TimeBasedCollectionSchemeOutputTypeDef = TypedDict(
    "TimeBasedCollectionSchemeOutputTypeDef",
    {
        "periodMs": int,
    },
)

_RequiredConditionBasedCollectionSchemeTypeDef = TypedDict(
    "_RequiredConditionBasedCollectionSchemeTypeDef",
    {
        "expression": str,
    },
)
_OptionalConditionBasedCollectionSchemeTypeDef = TypedDict(
    "_OptionalConditionBasedCollectionSchemeTypeDef",
    {
        "minimumTriggerIntervalMs": int,
        "triggerMode": TriggerModeType,
        "conditionLanguageVersion": int,
    },
    total=False,
)

class ConditionBasedCollectionSchemeTypeDef(
    _RequiredConditionBasedCollectionSchemeTypeDef, _OptionalConditionBasedCollectionSchemeTypeDef
):
    pass

TimeBasedCollectionSchemeTypeDef = TypedDict(
    "TimeBasedCollectionSchemeTypeDef",
    {
        "periodMs": int,
    },
)

_RequiredSignalInformationTypeDef = TypedDict(
    "_RequiredSignalInformationTypeDef",
    {
        "name": str,
    },
)
_OptionalSignalInformationTypeDef = TypedDict(
    "_OptionalSignalInformationTypeDef",
    {
        "maxSampleCount": int,
        "minimumSamplingIntervalMs": int,
    },
    total=False,
)

class SignalInformationTypeDef(
    _RequiredSignalInformationTypeDef, _OptionalSignalInformationTypeDef
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDecoderManifestResponseTypeDef = TypedDict(
    "CreateDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelManifestResponseTypeDef = TypedDict(
    "CreateModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSignalCatalogResponseTypeDef = TypedDict(
    "CreateSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVehicleResponseTypeDef = TypedDict(
    "CreateVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "thingArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredS3ConfigOutputTypeDef = TypedDict(
    "_RequiredS3ConfigOutputTypeDef",
    {
        "bucketArn": str,
    },
)
_OptionalS3ConfigOutputTypeDef = TypedDict(
    "_OptionalS3ConfigOutputTypeDef",
    {
        "dataFormat": DataFormatType,
        "storageCompressionFormat": StorageCompressionFormatType,
        "prefix": str,
    },
    total=False,
)

class S3ConfigOutputTypeDef(_RequiredS3ConfigOutputTypeDef, _OptionalS3ConfigOutputTypeDef):
    pass

TimestreamConfigOutputTypeDef = TypedDict(
    "TimestreamConfigOutputTypeDef",
    {
        "timestreamTableArn": str,
        "executionRoleArn": str,
    },
)

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "bucketArn": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "dataFormat": DataFormatType,
        "storageCompressionFormat": StorageCompressionFormatType,
        "prefix": str,
    },
    total=False,
)

class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass

TimestreamConfigTypeDef = TypedDict(
    "TimestreamConfigTypeDef",
    {
        "timestreamTableArn": str,
        "executionRoleArn": str,
    },
)

_RequiredDecoderManifestSummaryTypeDef = TypedDict(
    "_RequiredDecoderManifestSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalDecoderManifestSummaryTypeDef = TypedDict(
    "_OptionalDecoderManifestSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "modelManifestArn": str,
        "description": str,
        "status": ManifestStatusType,
    },
    total=False,
)

class DecoderManifestSummaryTypeDef(
    _RequiredDecoderManifestSummaryTypeDef, _OptionalDecoderManifestSummaryTypeDef
):
    pass

DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteCampaignResponseTypeDef = TypedDict(
    "DeleteCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDecoderManifestRequestRequestTypeDef = TypedDict(
    "DeleteDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteDecoderManifestResponseTypeDef = TypedDict(
    "DeleteDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)

DeleteFleetResponseTypeDef = TypedDict(
    "DeleteFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteModelManifestRequestRequestTypeDef = TypedDict(
    "DeleteModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteModelManifestResponseTypeDef = TypedDict(
    "DeleteModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSignalCatalogRequestRequestTypeDef = TypedDict(
    "DeleteSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteSignalCatalogResponseTypeDef = TypedDict(
    "DeleteSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVehicleRequestRequestTypeDef = TypedDict(
    "DeleteVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)

DeleteVehicleResponseTypeDef = TypedDict(
    "DeleteVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateVehicleFleetRequestRequestTypeDef = TypedDict(
    "DisassociateVehicleFleetRequestRequestTypeDef",
    {
        "vehicleName": str,
        "fleetId": str,
    },
)

_RequiredFleetSummaryTypeDef = TypedDict(
    "_RequiredFleetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
    },
)
_OptionalFleetSummaryTypeDef = TypedDict(
    "_OptionalFleetSummaryTypeDef",
    {
        "description": str,
        "lastModificationTime": datetime,
    },
    total=False,
)

class FleetSummaryTypeDef(_RequiredFleetSummaryTypeDef, _OptionalFleetSummaryTypeDef):
    pass

FormattedVssTypeDef = TypedDict(
    "FormattedVssTypeDef",
    {
        "vssJson": str,
    },
    total=False,
)

GetCampaignRequestRequestTypeDef = TypedDict(
    "GetCampaignRequestRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredSignalInformationOutputTypeDef = TypedDict(
    "_RequiredSignalInformationOutputTypeDef",
    {
        "name": str,
    },
)
_OptionalSignalInformationOutputTypeDef = TypedDict(
    "_OptionalSignalInformationOutputTypeDef",
    {
        "maxSampleCount": int,
        "minimumSamplingIntervalMs": int,
    },
    total=False,
)

class SignalInformationOutputTypeDef(
    _RequiredSignalInformationOutputTypeDef, _OptionalSignalInformationOutputTypeDef
):
    pass

GetDecoderManifestRequestRequestTypeDef = TypedDict(
    "GetDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetDecoderManifestResponseTypeDef = TypedDict(
    "GetDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "modelManifestArn": str,
        "status": ManifestStatusType,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFleetRequestRequestTypeDef = TypedDict(
    "GetFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)

GetFleetResponseTypeDef = TypedDict(
    "GetFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelManifestRequestRequestTypeDef = TypedDict(
    "GetModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetModelManifestResponseTypeDef = TypedDict(
    "GetModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "status": ManifestStatusType,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIamRegistrationResponseTypeDef = TypedDict(
    "_RequiredIamRegistrationResponseTypeDef",
    {
        "roleArn": str,
        "registrationStatus": RegistrationStatusType,
    },
)
_OptionalIamRegistrationResponseTypeDef = TypedDict(
    "_OptionalIamRegistrationResponseTypeDef",
    {
        "errorMessage": str,
    },
    total=False,
)

class IamRegistrationResponseTypeDef(
    _RequiredIamRegistrationResponseTypeDef, _OptionalIamRegistrationResponseTypeDef
):
    pass

_RequiredTimestreamRegistrationResponseTypeDef = TypedDict(
    "_RequiredTimestreamRegistrationResponseTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
        "registrationStatus": RegistrationStatusType,
    },
)
_OptionalTimestreamRegistrationResponseTypeDef = TypedDict(
    "_OptionalTimestreamRegistrationResponseTypeDef",
    {
        "timestreamDatabaseArn": str,
        "timestreamTableArn": str,
        "errorMessage": str,
    },
    total=False,
)

class TimestreamRegistrationResponseTypeDef(
    _RequiredTimestreamRegistrationResponseTypeDef, _OptionalTimestreamRegistrationResponseTypeDef
):
    pass

GetSignalCatalogRequestRequestTypeDef = TypedDict(
    "GetSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)

NodeCountsTypeDef = TypedDict(
    "NodeCountsTypeDef",
    {
        "totalNodes": int,
        "totalBranches": int,
        "totalSensors": int,
        "totalAttributes": int,
        "totalActuators": int,
    },
    total=False,
)

GetVehicleRequestRequestTypeDef = TypedDict(
    "GetVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)

GetVehicleResponseTypeDef = TypedDict(
    "GetVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Dict[str, str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef = TypedDict(
    "_RequiredGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef = TypedDict(
    "_OptionalGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef(
    _RequiredGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef,
    _OptionalGetVehicleStatusRequestGetVehicleStatusPaginateTypeDef,
):
    pass

_RequiredGetVehicleStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetVehicleStatusRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalGetVehicleStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetVehicleStatusRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetVehicleStatusRequestRequestTypeDef(
    _RequiredGetVehicleStatusRequestRequestTypeDef, _OptionalGetVehicleStatusRequestRequestTypeDef
):
    pass

VehicleStatusTypeDef = TypedDict(
    "VehicleStatusTypeDef",
    {
        "campaignName": str,
        "vehicleName": str,
        "status": VehicleStateType,
    },
    total=False,
)

IamResourcesOutputTypeDef = TypedDict(
    "IamResourcesOutputTypeDef",
    {
        "roleArn": str,
    },
)

IamResourcesTypeDef = TypedDict(
    "IamResourcesTypeDef",
    {
        "roleArn": str,
    },
)

ImportDecoderManifestResponseTypeDef = TypedDict(
    "ImportDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSignalCatalogResponseTypeDef = TypedDict(
    "ImportSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCampaignsRequestListCampaignsPaginateTypeDef = TypedDict(
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    {
        "status": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "status": str,
    },
    total=False,
)

_RequiredListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef = TypedDict(
    "_RequiredListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef = TypedDict(
    "_OptionalListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef(
    _RequiredListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef,
    _OptionalListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef,
):
    pass

_RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "_RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "_OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDecoderManifestNetworkInterfacesRequestRequestTypeDef(
    _RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef,
    _OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef,
):
    pass

_RequiredListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef = TypedDict(
    "_RequiredListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef = TypedDict(
    "_OptionalListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef(
    _RequiredListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef,
    _OptionalListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef,
):
    pass

_RequiredListDecoderManifestSignalsRequestRequestTypeDef = TypedDict(
    "_RequiredListDecoderManifestSignalsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestSignalsRequestRequestTypeDef = TypedDict(
    "_OptionalListDecoderManifestSignalsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDecoderManifestSignalsRequestRequestTypeDef(
    _RequiredListDecoderManifestSignalsRequestRequestTypeDef,
    _OptionalListDecoderManifestSignalsRequestRequestTypeDef,
):
    pass

ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef = TypedDict(
    "ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef",
    {
        "modelManifestArn": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDecoderManifestsRequestRequestTypeDef = TypedDict(
    "ListDecoderManifestsRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef = TypedDict(
    "_RequiredListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef = TypedDict(
    "_OptionalListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef(
    _RequiredListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef,
    _OptionalListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef,
):
    pass

_RequiredListFleetsForVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredListFleetsForVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalListFleetsForVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalListFleetsForVehicleRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListFleetsForVehicleRequestRequestTypeDef(
    _RequiredListFleetsForVehicleRequestRequestTypeDef,
    _OptionalListFleetsForVehicleRequestRequestTypeDef,
):
    pass

ListFleetsForVehicleResponseTypeDef = TypedDict(
    "ListFleetsForVehicleResponseTypeDef",
    {
        "fleets": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsRequestListFleetsPaginateTypeDef = TypedDict(
    "ListFleetsRequestListFleetsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef = TypedDict(
    "_RequiredListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef = TypedDict(
    "_OptionalListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef(
    _RequiredListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef,
    _OptionalListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef,
):
    pass

_RequiredListModelManifestNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListModelManifestNodesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListModelManifestNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListModelManifestNodesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListModelManifestNodesRequestRequestTypeDef(
    _RequiredListModelManifestNodesRequestRequestTypeDef,
    _OptionalListModelManifestNodesRequestRequestTypeDef,
):
    pass

ListModelManifestsRequestListModelManifestsPaginateTypeDef = TypedDict(
    "ListModelManifestsRequestListModelManifestsPaginateTypeDef",
    {
        "signalCatalogArn": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListModelManifestsRequestRequestTypeDef = TypedDict(
    "ListModelManifestsRequestRequestTypeDef",
    {
        "signalCatalogArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredModelManifestSummaryTypeDef = TypedDict(
    "_RequiredModelManifestSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalModelManifestSummaryTypeDef = TypedDict(
    "_OptionalModelManifestSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "signalCatalogArn": str,
        "description": str,
        "status": ManifestStatusType,
    },
    total=False,
)

class ModelManifestSummaryTypeDef(
    _RequiredModelManifestSummaryTypeDef, _OptionalModelManifestSummaryTypeDef
):
    pass

_RequiredListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef = TypedDict(
    "_RequiredListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef",
    {
        "name": str,
    },
)
_OptionalListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef = TypedDict(
    "_OptionalListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef(
    _RequiredListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef,
    _OptionalListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef,
):
    pass

_RequiredListSignalCatalogNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListSignalCatalogNodesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListSignalCatalogNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListSignalCatalogNodesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListSignalCatalogNodesRequestRequestTypeDef(
    _RequiredListSignalCatalogNodesRequestRequestTypeDef,
    _OptionalListSignalCatalogNodesRequestRequestTypeDef,
):
    pass

ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef = TypedDict(
    "ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSignalCatalogsRequestRequestTypeDef = TypedDict(
    "ListSignalCatalogsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

SignalCatalogSummaryTypeDef = TypedDict(
    "SignalCatalogSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
    total=False,
)

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

_RequiredListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef = TypedDict(
    "_RequiredListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef",
    {
        "fleetId": str,
    },
)
_OptionalListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef = TypedDict(
    "_OptionalListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef(
    _RequiredListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef,
    _OptionalListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef,
):
    pass

_RequiredListVehiclesInFleetRequestRequestTypeDef = TypedDict(
    "_RequiredListVehiclesInFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)
_OptionalListVehiclesInFleetRequestRequestTypeDef = TypedDict(
    "_OptionalListVehiclesInFleetRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListVehiclesInFleetRequestRequestTypeDef(
    _RequiredListVehiclesInFleetRequestRequestTypeDef,
    _OptionalListVehiclesInFleetRequestRequestTypeDef,
):
    pass

ListVehiclesInFleetResponseTypeDef = TypedDict(
    "ListVehiclesInFleetResponseTypeDef",
    {
        "vehicles": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVehiclesRequestListVehiclesPaginateTypeDef = TypedDict(
    "ListVehiclesRequestListVehiclesPaginateTypeDef",
    {
        "modelManifestArn": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListVehiclesRequestRequestTypeDef = TypedDict(
    "ListVehiclesRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

VehicleSummaryTypeDef = TypedDict(
    "VehicleSummaryTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)

_RequiredObdInterfaceOutputTypeDef = TypedDict(
    "_RequiredObdInterfaceOutputTypeDef",
    {
        "name": str,
        "requestMessageId": int,
    },
)
_OptionalObdInterfaceOutputTypeDef = TypedDict(
    "_OptionalObdInterfaceOutputTypeDef",
    {
        "obdStandard": str,
        "pidRequestIntervalSeconds": int,
        "dtcRequestIntervalSeconds": int,
        "useExtendedIds": bool,
        "hasTransmissionEcu": bool,
    },
    total=False,
)

class ObdInterfaceOutputTypeDef(
    _RequiredObdInterfaceOutputTypeDef, _OptionalObdInterfaceOutputTypeDef
):
    pass

_RequiredObdInterfaceTypeDef = TypedDict(
    "_RequiredObdInterfaceTypeDef",
    {
        "name": str,
        "requestMessageId": int,
    },
)
_OptionalObdInterfaceTypeDef = TypedDict(
    "_OptionalObdInterfaceTypeDef",
    {
        "obdStandard": str,
        "pidRequestIntervalSeconds": int,
        "dtcRequestIntervalSeconds": int,
        "useExtendedIds": bool,
        "hasTransmissionEcu": bool,
    },
    total=False,
)

class ObdInterfaceTypeDef(_RequiredObdInterfaceTypeDef, _OptionalObdInterfaceTypeDef):
    pass

_RequiredSensorOutputTypeDef = TypedDict(
    "_RequiredSensorOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalSensorOutputTypeDef = TypedDict(
    "_OptionalSensorOutputTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": List[str],
        "min": float,
        "max": float,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class SensorOutputTypeDef(_RequiredSensorOutputTypeDef, _OptionalSensorOutputTypeDef):
    pass

_RequiredSensorTypeDef = TypedDict(
    "_RequiredSensorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalSensorTypeDef = TypedDict(
    "_OptionalSensorTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": Sequence[str],
        "min": float,
        "max": float,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class SensorTypeDef(_RequiredSensorTypeDef, _OptionalSensorTypeDef):
    pass

_RequiredObdSignalOutputTypeDef = TypedDict(
    "_RequiredObdSignalOutputTypeDef",
    {
        "pidResponseLength": int,
        "serviceMode": int,
        "pid": int,
        "scaling": float,
        "offset": float,
        "startByte": int,
        "byteLength": int,
    },
)
_OptionalObdSignalOutputTypeDef = TypedDict(
    "_OptionalObdSignalOutputTypeDef",
    {
        "bitRightShift": int,
        "bitMaskLength": int,
    },
    total=False,
)

class ObdSignalOutputTypeDef(_RequiredObdSignalOutputTypeDef, _OptionalObdSignalOutputTypeDef):
    pass

_RequiredObdSignalTypeDef = TypedDict(
    "_RequiredObdSignalTypeDef",
    {
        "pidResponseLength": int,
        "serviceMode": int,
        "pid": int,
        "scaling": float,
        "offset": float,
        "startByte": int,
        "byteLength": int,
    },
)
_OptionalObdSignalTypeDef = TypedDict(
    "_OptionalObdSignalTypeDef",
    {
        "bitRightShift": int,
        "bitMaskLength": int,
    },
    total=False,
)

class ObdSignalTypeDef(_RequiredObdSignalTypeDef, _OptionalObdSignalTypeDef):
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

TimestreamResourcesTypeDef = TypedDict(
    "TimestreamResourcesTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
    },
)

TimestreamResourcesOutputTypeDef = TypedDict(
    "TimestreamResourcesOutputTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "action": UpdateCampaignActionType,
    },
)
_OptionalUpdateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCampaignRequestRequestTypeDef",
    {
        "description": str,
        "dataExtraDimensions": Sequence[str],
    },
    total=False,
)

class UpdateCampaignRequestRequestTypeDef(
    _RequiredUpdateCampaignRequestRequestTypeDef, _OptionalUpdateCampaignRequestRequestTypeDef
):
    pass

UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": CampaignStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDecoderManifestResponseTypeDef = TypedDict(
    "UpdateDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)
_OptionalUpdateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateFleetRequestRequestTypeDef(
    _RequiredUpdateFleetRequestRequestTypeDef, _OptionalUpdateFleetRequestRequestTypeDef
):
    pass

UpdateFleetResponseTypeDef = TypedDict(
    "UpdateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateModelManifestRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateModelManifestRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelManifestRequestRequestTypeDef",
    {
        "description": str,
        "nodesToAdd": Sequence[str],
        "nodesToRemove": Sequence[str],
        "status": ManifestStatusType,
    },
    total=False,
)

class UpdateModelManifestRequestRequestTypeDef(
    _RequiredUpdateModelManifestRequestRequestTypeDef,
    _OptionalUpdateModelManifestRequestRequestTypeDef,
):
    pass

UpdateModelManifestResponseTypeDef = TypedDict(
    "UpdateModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSignalCatalogResponseTypeDef = TypedDict(
    "UpdateSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalUpdateVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVehicleRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Mapping[str, str],
        "attributeUpdateMode": UpdateModeType,
    },
    total=False,
)

class UpdateVehicleRequestRequestTypeDef(
    _RequiredUpdateVehicleRequestRequestTypeDef, _OptionalUpdateVehicleRequestRequestTypeDef
):
    pass

UpdateVehicleResponseTypeDef = TypedDict(
    "UpdateVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateVehicleResponseTypeDef = TypedDict(
    "BatchCreateVehicleResponseTypeDef",
    {
        "vehicles": List[CreateVehicleResponseItemTypeDef],
        "errors": List[CreateVehicleErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateVehicleRequestRequestTypeDef = TypedDict(
    "BatchUpdateVehicleRequestRequestTypeDef",
    {
        "vehicles": Sequence[UpdateVehicleRequestItemTypeDef],
    },
)

BatchUpdateVehicleResponseTypeDef = TypedDict(
    "BatchUpdateVehicleResponseTypeDef",
    {
        "vehicles": List[UpdateVehicleResponseItemTypeDef],
        "errors": List[UpdateVehicleErrorTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "campaignSummaries": List[CampaignSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkFileDefinitionTypeDef = TypedDict(
    "NetworkFileDefinitionTypeDef",
    {
        "canDbc": CanDbcDefinitionTypeDef,
    },
    total=False,
)

GetLoggingOptionsResponseTypeDef = TypedDict(
    "GetLoggingOptionsResponseTypeDef",
    {
        "cloudWatchLogDelivery": CloudWatchLogDeliveryOptionsOutputTypeDef,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "cloudWatchLogDelivery": CloudWatchLogDeliveryOptionsTypeDef,
    },
)

CollectionSchemeOutputTypeDef = TypedDict(
    "CollectionSchemeOutputTypeDef",
    {
        "timeBasedCollectionScheme": TimeBasedCollectionSchemeOutputTypeDef,
        "conditionBasedCollectionScheme": ConditionBasedCollectionSchemeOutputTypeDef,
    },
    total=False,
)

CollectionSchemeTypeDef = TypedDict(
    "CollectionSchemeTypeDef",
    {
        "timeBasedCollectionScheme": TimeBasedCollectionSchemeTypeDef,
        "conditionBasedCollectionScheme": ConditionBasedCollectionSchemeTypeDef,
    },
    total=False,
)

_RequiredCreateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestRequestTypeDef",
    {
        "fleetId": str,
        "signalCatalogArn": str,
    },
)
_OptionalCreateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateFleetRequestRequestTypeDef(
    _RequiredCreateFleetRequestRequestTypeDef, _OptionalCreateFleetRequestRequestTypeDef
):
    pass

_RequiredCreateModelManifestRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelManifestRequestRequestTypeDef",
    {
        "name": str,
        "nodes": Sequence[str],
        "signalCatalogArn": str,
    },
)
_OptionalCreateModelManifestRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelManifestRequestRequestTypeDef",
    {
        "description": str,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateModelManifestRequestRequestTypeDef(
    _RequiredCreateModelManifestRequestRequestTypeDef,
    _OptionalCreateModelManifestRequestRequestTypeDef,
):
    pass

_RequiredCreateVehicleRequestItemTypeDef = TypedDict(
    "_RequiredCreateVehicleRequestItemTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
    },
)
_OptionalCreateVehicleRequestItemTypeDef = TypedDict(
    "_OptionalCreateVehicleRequestItemTypeDef",
    {
        "attributes": Mapping[str, str],
        "associationBehavior": VehicleAssociationBehaviorType,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateVehicleRequestItemTypeDef(
    _RequiredCreateVehicleRequestItemTypeDef, _OptionalCreateVehicleRequestItemTypeDef
):
    pass

_RequiredCreateVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
    },
)
_OptionalCreateVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVehicleRequestRequestTypeDef",
    {
        "attributes": Mapping[str, str],
        "associationBehavior": VehicleAssociationBehaviorType,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateVehicleRequestRequestTypeDef(
    _RequiredCreateVehicleRequestRequestTypeDef, _OptionalCreateVehicleRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

DataDestinationConfigOutputTypeDef = TypedDict(
    "DataDestinationConfigOutputTypeDef",
    {
        "s3Config": S3ConfigOutputTypeDef,
        "timestreamConfig": TimestreamConfigOutputTypeDef,
    },
    total=False,
)

DataDestinationConfigTypeDef = TypedDict(
    "DataDestinationConfigTypeDef",
    {
        "s3Config": S3ConfigTypeDef,
        "timestreamConfig": TimestreamConfigTypeDef,
    },
    total=False,
)

ListDecoderManifestsResponseTypeDef = TypedDict(
    "ListDecoderManifestsResponseTypeDef",
    {
        "summaries": List[DecoderManifestSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleetSummaries": List[FleetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredImportSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalImportSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalImportSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "vss": FormattedVssTypeDef,
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class ImportSignalCatalogRequestRequestTypeDef(
    _RequiredImportSignalCatalogRequestRequestTypeDef,
    _OptionalImportSignalCatalogRequestRequestTypeDef,
):
    pass

GetRegisterAccountStatusResponseTypeDef = TypedDict(
    "GetRegisterAccountStatusResponseTypeDef",
    {
        "customerAccountId": str,
        "accountStatus": RegistrationStatusType,
        "timestreamRegistrationResponse": TimestreamRegistrationResponseTypeDef,
        "iamRegistrationResponse": IamRegistrationResponseTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSignalCatalogResponseTypeDef = TypedDict(
    "GetSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "nodeCounts": NodeCountsTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVehicleStatusResponseTypeDef = TypedDict(
    "GetVehicleStatusResponseTypeDef",
    {
        "campaigns": List[VehicleStatusTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelManifestsResponseTypeDef = TypedDict(
    "ListModelManifestsResponseTypeDef",
    {
        "summaries": List[ModelManifestSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSignalCatalogsResponseTypeDef = TypedDict(
    "ListSignalCatalogsResponseTypeDef",
    {
        "summaries": List[SignalCatalogSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVehiclesResponseTypeDef = TypedDict(
    "ListVehiclesResponseTypeDef",
    {
        "vehicleSummaries": List[VehicleSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNetworkInterfaceOutputTypeDef = TypedDict(
    "_RequiredNetworkInterfaceOutputTypeDef",
    {
        "interfaceId": str,
        "type": NetworkInterfaceTypeType,
    },
)
_OptionalNetworkInterfaceOutputTypeDef = TypedDict(
    "_OptionalNetworkInterfaceOutputTypeDef",
    {
        "canInterface": CanInterfaceOutputTypeDef,
        "obdInterface": ObdInterfaceOutputTypeDef,
    },
    total=False,
)

class NetworkInterfaceOutputTypeDef(
    _RequiredNetworkInterfaceOutputTypeDef, _OptionalNetworkInterfaceOutputTypeDef
):
    pass

_RequiredNetworkInterfaceTypeDef = TypedDict(
    "_RequiredNetworkInterfaceTypeDef",
    {
        "interfaceId": str,
        "type": NetworkInterfaceTypeType,
    },
)
_OptionalNetworkInterfaceTypeDef = TypedDict(
    "_OptionalNetworkInterfaceTypeDef",
    {
        "canInterface": CanInterfaceTypeDef,
        "obdInterface": ObdInterfaceTypeDef,
    },
    total=False,
)

class NetworkInterfaceTypeDef(_RequiredNetworkInterfaceTypeDef, _OptionalNetworkInterfaceTypeDef):
    pass

NodeOutputTypeDef = TypedDict(
    "NodeOutputTypeDef",
    {
        "branch": BranchOutputTypeDef,
        "sensor": SensorOutputTypeDef,
        "actuator": ActuatorOutputTypeDef,
        "attribute": AttributeOutputTypeDef,
    },
    total=False,
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "branch": BranchTypeDef,
        "sensor": SensorTypeDef,
        "actuator": ActuatorTypeDef,
        "attribute": AttributeTypeDef,
    },
    total=False,
)

_RequiredSignalDecoderOutputTypeDef = TypedDict(
    "_RequiredSignalDecoderOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
    },
)
_OptionalSignalDecoderOutputTypeDef = TypedDict(
    "_OptionalSignalDecoderOutputTypeDef",
    {
        "canSignal": CanSignalOutputTypeDef,
        "obdSignal": ObdSignalOutputTypeDef,
    },
    total=False,
)

class SignalDecoderOutputTypeDef(
    _RequiredSignalDecoderOutputTypeDef, _OptionalSignalDecoderOutputTypeDef
):
    pass

_RequiredSignalDecoderTypeDef = TypedDict(
    "_RequiredSignalDecoderTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
    },
)
_OptionalSignalDecoderTypeDef = TypedDict(
    "_OptionalSignalDecoderTypeDef",
    {
        "canSignal": CanSignalTypeDef,
        "obdSignal": ObdSignalTypeDef,
    },
    total=False,
)

class SignalDecoderTypeDef(_RequiredSignalDecoderTypeDef, _OptionalSignalDecoderTypeDef):
    pass

RegisterAccountRequestRequestTypeDef = TypedDict(
    "RegisterAccountRequestRequestTypeDef",
    {
        "timestreamResources": TimestreamResourcesTypeDef,
        "iamResources": IamResourcesTypeDef,
    },
    total=False,
)

RegisterAccountResponseTypeDef = TypedDict(
    "RegisterAccountResponseTypeDef",
    {
        "registerAccountStatus": RegistrationStatusType,
        "timestreamResources": TimestreamResourcesOutputTypeDef,
        "iamResources": IamResourcesOutputTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportDecoderManifestRequestRequestTypeDef = TypedDict(
    "ImportDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "networkFileDefinitions": Sequence[NetworkFileDefinitionTypeDef],
    },
)

BatchCreateVehicleRequestRequestTypeDef = TypedDict(
    "BatchCreateVehicleRequestRequestTypeDef",
    {
        "vehicles": Sequence[CreateVehicleRequestItemTypeDef],
    },
)

GetCampaignResponseTypeDef = TypedDict(
    "GetCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "status": CampaignStatusType,
        "startTime": datetime,
        "expiryTime": datetime,
        "postTriggerCollectionDuration": int,
        "diagnosticsMode": DiagnosticsModeType,
        "spoolingMode": SpoolingModeType,
        "compression": CompressionType,
        "priority": int,
        "signalsToCollect": List[SignalInformationOutputTypeDef],
        "collectionScheme": CollectionSchemeOutputTypeDef,
        "dataExtraDimensions": List[str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "dataDestinationConfigs": List[DataDestinationConfigOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "collectionScheme": CollectionSchemeTypeDef,
    },
)
_OptionalCreateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCampaignRequestRequestTypeDef",
    {
        "description": str,
        "startTime": Union[datetime, str],
        "expiryTime": Union[datetime, str],
        "postTriggerCollectionDuration": int,
        "diagnosticsMode": DiagnosticsModeType,
        "spoolingMode": SpoolingModeType,
        "compression": CompressionType,
        "priority": int,
        "signalsToCollect": Sequence[SignalInformationTypeDef],
        "dataExtraDimensions": Sequence[str],
        "tags": Sequence[TagTypeDef],
        "dataDestinationConfigs": Sequence[DataDestinationConfigTypeDef],
    },
    total=False,
)

class CreateCampaignRequestRequestTypeDef(
    _RequiredCreateCampaignRequestRequestTypeDef, _OptionalCreateCampaignRequestRequestTypeDef
):
    pass

ListDecoderManifestNetworkInterfacesResponseTypeDef = TypedDict(
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    {
        "networkInterfaces": List[NetworkInterfaceOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelManifestNodesResponseTypeDef = TypedDict(
    "ListModelManifestNodesResponseTypeDef",
    {
        "nodes": List[NodeOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSignalCatalogNodesResponseTypeDef = TypedDict(
    "ListSignalCatalogNodesResponseTypeDef",
    {
        "nodes": List[NodeOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "nodes": Sequence[NodeTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateSignalCatalogRequestRequestTypeDef(
    _RequiredCreateSignalCatalogRequestRequestTypeDef,
    _OptionalCreateSignalCatalogRequestRequestTypeDef,
):
    pass

_RequiredUpdateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "nodesToAdd": Sequence[NodeTypeDef],
        "nodesToUpdate": Sequence[NodeTypeDef],
        "nodesToRemove": Sequence[str],
    },
    total=False,
)

class UpdateSignalCatalogRequestRequestTypeDef(
    _RequiredUpdateSignalCatalogRequestRequestTypeDef,
    _OptionalUpdateSignalCatalogRequestRequestTypeDef,
):
    pass

ListDecoderManifestSignalsResponseTypeDef = TypedDict(
    "ListDecoderManifestSignalsResponseTypeDef",
    {
        "signalDecoders": List[SignalDecoderOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "modelManifestArn": str,
    },
)
_OptionalCreateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDecoderManifestRequestRequestTypeDef",
    {
        "description": str,
        "signalDecoders": Sequence[SignalDecoderTypeDef],
        "networkInterfaces": Sequence[NetworkInterfaceTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateDecoderManifestRequestRequestTypeDef(
    _RequiredCreateDecoderManifestRequestRequestTypeDef,
    _OptionalCreateDecoderManifestRequestRequestTypeDef,
):
    pass

_RequiredUpdateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDecoderManifestRequestRequestTypeDef",
    {
        "description": str,
        "signalDecodersToAdd": Sequence[SignalDecoderTypeDef],
        "signalDecodersToUpdate": Sequence[SignalDecoderTypeDef],
        "signalDecodersToRemove": Sequence[str],
        "networkInterfacesToAdd": Sequence[NetworkInterfaceTypeDef],
        "networkInterfacesToUpdate": Sequence[NetworkInterfaceTypeDef],
        "networkInterfacesToRemove": Sequence[str],
        "status": ManifestStatusType,
    },
    total=False,
)

class UpdateDecoderManifestRequestRequestTypeDef(
    _RequiredUpdateDecoderManifestRequestRequestTypeDef,
    _OptionalUpdateDecoderManifestRequestRequestTypeDef,
):
    pass
