"""
Type annotations for groundstation service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/type_defs/)

Usage::

    ```python
    from mypy_boto3_groundstation.type_defs import ComponentVersionTypeDef

    data: ComponentVersionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AgentStatusType,
    AngleUnitsType,
    AuditResultsType,
    BandwidthUnitsType,
    CapabilityHealthReasonType,
    CapabilityHealthType,
    ConfigCapabilityTypeType,
    ContactStatusType,
    CriticalityType,
    EndpointStatusType,
    EphemerisInvalidReasonType,
    EphemerisSourceType,
    EphemerisStatusType,
    FrequencyUnitsType,
    PolarizationType,
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
    "ComponentVersionTypeDef",
    "AggregateStatusTypeDef",
    "AntennaDemodDecodeDetailsTypeDef",
    "DecodeConfigOutputTypeDef",
    "DemodulationConfigOutputTypeDef",
    "DecodeConfigTypeDef",
    "DemodulationConfigTypeDef",
    "EirpOutputTypeDef",
    "EirpTypeDef",
    "CancelContactRequestRequestTypeDef",
    "ComponentStatusDataTypeDef",
    "S3RecordingDetailsTypeDef",
    "ConfigIdResponseTypeDef",
    "ConfigListItemTypeDef",
    "DataflowEndpointConfigOutputTypeDef",
    "S3RecordingConfigOutputTypeDef",
    "TrackingConfigOutputTypeDef",
    "UplinkEchoConfigOutputTypeDef",
    "DataflowEndpointConfigTypeDef",
    "S3RecordingConfigTypeDef",
    "TrackingConfigTypeDef",
    "UplinkEchoConfigTypeDef",
    "SocketAddressOutputTypeDef",
    "SocketAddressTypeDef",
    "ElevationTypeDef",
    "ContactIdResponseTypeDef",
    "KmsKeyTypeDef",
    "DataflowEndpointGroupIdResponseTypeDef",
    "DataflowEndpointListItemTypeDef",
    "DeleteConfigRequestRequestTypeDef",
    "DeleteDataflowEndpointGroupRequestRequestTypeDef",
    "DeleteEphemerisRequestRequestTypeDef",
    "DeleteMissionProfileRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeContactRequestRequestTypeDef",
    "DescribeEphemerisRequestRequestTypeDef",
    "DiscoveryDataTypeDef",
    "SecurityDetailsOutputTypeDef",
    "SecurityDetailsTypeDef",
    "S3ObjectOutputTypeDef",
    "EphemerisIdResponseTypeDef",
    "EphemerisMetaDataTypeDef",
    "FrequencyBandwidthOutputTypeDef",
    "FrequencyBandwidthTypeDef",
    "FrequencyOutputTypeDef",
    "FrequencyTypeDef",
    "GetAgentConfigurationRequestRequestTypeDef",
    "GetAgentConfigurationResponseTypeDef",
    "GetConfigRequestRequestTypeDef",
    "GetDataflowEndpointGroupRequestRequestTypeDef",
    "GetMinuteUsageRequestRequestTypeDef",
    "GetMinuteUsageResponseTypeDef",
    "GetMissionProfileRequestRequestTypeDef",
    "KmsKeyOutputTypeDef",
    "GetSatelliteRequestRequestTypeDef",
    "GroundStationDataTypeDef",
    "IntegerRangeOutputTypeDef",
    "IntegerRangeTypeDef",
    "ListConfigsRequestListConfigsPaginateTypeDef",
    "ListConfigsRequestRequestTypeDef",
    "ListContactsRequestListContactsPaginateTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef",
    "ListDataflowEndpointGroupsRequestRequestTypeDef",
    "ListEphemeridesRequestListEphemeridesPaginateTypeDef",
    "ListEphemeridesRequestRequestTypeDef",
    "ListGroundStationsRequestListGroundStationsPaginateTypeDef",
    "ListGroundStationsRequestRequestTypeDef",
    "ListMissionProfilesRequestListMissionProfilesPaginateTypeDef",
    "ListMissionProfilesRequestRequestTypeDef",
    "MissionProfileListItemTypeDef",
    "ListSatellitesRequestListSatellitesPaginateTypeDef",
    "ListSatellitesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MissionProfileIdResponseTypeDef",
    "S3ObjectTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterAgentResponseTypeDef",
    "ReserveContactRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TimeRangeTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentStatusResponseTypeDef",
    "UpdateEphemerisRequestRequestTypeDef",
    "AgentDetailsTypeDef",
    "UpdateAgentStatusRequestRequestTypeDef",
    "ListConfigsResponseTypeDef",
    "ConnectionDetailsOutputTypeDef",
    "DataflowEndpointOutputTypeDef",
    "ConnectionDetailsTypeDef",
    "DataflowEndpointTypeDef",
    "ContactDataTypeDef",
    "CreateMissionProfileRequestRequestTypeDef",
    "UpdateMissionProfileRequestRequestTypeDef",
    "ListDataflowEndpointGroupsResponseTypeDef",
    "DescribeContactRequestContactScheduledWaitTypeDef",
    "EphemerisDescriptionTypeDef",
    "EphemerisItemTypeDef",
    "GetSatelliteResponseTypeDef",
    "SatelliteListItemTypeDef",
    "SpectrumConfigOutputTypeDef",
    "UplinkSpectrumConfigOutputTypeDef",
    "SpectrumConfigTypeDef",
    "UplinkSpectrumConfigTypeDef",
    "GetMissionProfileResponseTypeDef",
    "ListGroundStationsResponseTypeDef",
    "RangedSocketAddressOutputTypeDef",
    "RangedSocketAddressTypeDef",
    "ListMissionProfilesResponseTypeDef",
    "OEMEphemerisTypeDef",
    "TLEDataTypeDef",
    "RegisterAgentRequestRequestTypeDef",
    "ListContactsResponseTypeDef",
    "EphemerisTypeDescriptionTypeDef",
    "ListEphemeridesResponseTypeDef",
    "ListSatellitesResponseTypeDef",
    "AntennaDownlinkConfigOutputTypeDef",
    "AntennaDownlinkDemodDecodeConfigOutputTypeDef",
    "AntennaUplinkConfigOutputTypeDef",
    "AntennaDownlinkConfigTypeDef",
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    "AntennaUplinkConfigTypeDef",
    "RangedConnectionDetailsOutputTypeDef",
    "RangedConnectionDetailsTypeDef",
    "TLEEphemerisTypeDef",
    "DescribeEphemerisResponseTypeDef",
    "ConfigTypeDataOutputTypeDef",
    "ConfigTypeDataTypeDef",
    "AwsGroundStationAgentEndpointOutputTypeDef",
    "AwsGroundStationAgentEndpointTypeDef",
    "EphemerisDataTypeDef",
    "GetConfigResponseTypeDef",
    "CreateConfigRequestRequestTypeDef",
    "UpdateConfigRequestRequestTypeDef",
    "EndpointDetailsOutputTypeDef",
    "EndpointDetailsTypeDef",
    "CreateEphemerisRequestRequestTypeDef",
    "ConfigDetailsTypeDef",
    "GetDataflowEndpointGroupResponseTypeDef",
    "CreateDataflowEndpointGroupRequestRequestTypeDef",
    "DestinationTypeDef",
    "SourceTypeDef",
    "DataflowDetailTypeDef",
    "DescribeContactResponseTypeDef",
)

ComponentVersionTypeDef = TypedDict(
    "ComponentVersionTypeDef",
    {
        "componentType": str,
        "versions": Sequence[str],
    },
)

_RequiredAggregateStatusTypeDef = TypedDict(
    "_RequiredAggregateStatusTypeDef",
    {
        "status": AgentStatusType,
    },
)
_OptionalAggregateStatusTypeDef = TypedDict(
    "_OptionalAggregateStatusTypeDef",
    {
        "signatureMap": Mapping[str, bool],
    },
    total=False,
)

class AggregateStatusTypeDef(_RequiredAggregateStatusTypeDef, _OptionalAggregateStatusTypeDef):
    pass

AntennaDemodDecodeDetailsTypeDef = TypedDict(
    "AntennaDemodDecodeDetailsTypeDef",
    {
        "outputNode": str,
    },
    total=False,
)

DecodeConfigOutputTypeDef = TypedDict(
    "DecodeConfigOutputTypeDef",
    {
        "unvalidatedJSON": str,
    },
)

DemodulationConfigOutputTypeDef = TypedDict(
    "DemodulationConfigOutputTypeDef",
    {
        "unvalidatedJSON": str,
    },
)

DecodeConfigTypeDef = TypedDict(
    "DecodeConfigTypeDef",
    {
        "unvalidatedJSON": str,
    },
)

DemodulationConfigTypeDef = TypedDict(
    "DemodulationConfigTypeDef",
    {
        "unvalidatedJSON": str,
    },
)

EirpOutputTypeDef = TypedDict(
    "EirpOutputTypeDef",
    {
        "units": Literal["dBW"],
        "value": float,
    },
)

EirpTypeDef = TypedDict(
    "EirpTypeDef",
    {
        "units": Literal["dBW"],
        "value": float,
    },
)

CancelContactRequestRequestTypeDef = TypedDict(
    "CancelContactRequestRequestTypeDef",
    {
        "contactId": str,
    },
)

_RequiredComponentStatusDataTypeDef = TypedDict(
    "_RequiredComponentStatusDataTypeDef",
    {
        "capabilityArn": str,
        "componentType": str,
        "dataflowId": str,
        "status": AgentStatusType,
    },
)
_OptionalComponentStatusDataTypeDef = TypedDict(
    "_OptionalComponentStatusDataTypeDef",
    {
        "bytesReceived": int,
        "bytesSent": int,
        "packetsDropped": int,
    },
    total=False,
)

class ComponentStatusDataTypeDef(
    _RequiredComponentStatusDataTypeDef, _OptionalComponentStatusDataTypeDef
):
    pass

S3RecordingDetailsTypeDef = TypedDict(
    "S3RecordingDetailsTypeDef",
    {
        "bucketArn": str,
        "keyTemplate": str,
    },
    total=False,
)

ConfigIdResponseTypeDef = TypedDict(
    "ConfigIdResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigListItemTypeDef = TypedDict(
    "ConfigListItemTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
    },
    total=False,
)

_RequiredDataflowEndpointConfigOutputTypeDef = TypedDict(
    "_RequiredDataflowEndpointConfigOutputTypeDef",
    {
        "dataflowEndpointName": str,
    },
)
_OptionalDataflowEndpointConfigOutputTypeDef = TypedDict(
    "_OptionalDataflowEndpointConfigOutputTypeDef",
    {
        "dataflowEndpointRegion": str,
    },
    total=False,
)

class DataflowEndpointConfigOutputTypeDef(
    _RequiredDataflowEndpointConfigOutputTypeDef, _OptionalDataflowEndpointConfigOutputTypeDef
):
    pass

_RequiredS3RecordingConfigOutputTypeDef = TypedDict(
    "_RequiredS3RecordingConfigOutputTypeDef",
    {
        "bucketArn": str,
        "roleArn": str,
    },
)
_OptionalS3RecordingConfigOutputTypeDef = TypedDict(
    "_OptionalS3RecordingConfigOutputTypeDef",
    {
        "prefix": str,
    },
    total=False,
)

class S3RecordingConfigOutputTypeDef(
    _RequiredS3RecordingConfigOutputTypeDef, _OptionalS3RecordingConfigOutputTypeDef
):
    pass

TrackingConfigOutputTypeDef = TypedDict(
    "TrackingConfigOutputTypeDef",
    {
        "autotrack": CriticalityType,
    },
)

UplinkEchoConfigOutputTypeDef = TypedDict(
    "UplinkEchoConfigOutputTypeDef",
    {
        "antennaUplinkConfigArn": str,
        "enabled": bool,
    },
)

_RequiredDataflowEndpointConfigTypeDef = TypedDict(
    "_RequiredDataflowEndpointConfigTypeDef",
    {
        "dataflowEndpointName": str,
    },
)
_OptionalDataflowEndpointConfigTypeDef = TypedDict(
    "_OptionalDataflowEndpointConfigTypeDef",
    {
        "dataflowEndpointRegion": str,
    },
    total=False,
)

class DataflowEndpointConfigTypeDef(
    _RequiredDataflowEndpointConfigTypeDef, _OptionalDataflowEndpointConfigTypeDef
):
    pass

_RequiredS3RecordingConfigTypeDef = TypedDict(
    "_RequiredS3RecordingConfigTypeDef",
    {
        "bucketArn": str,
        "roleArn": str,
    },
)
_OptionalS3RecordingConfigTypeDef = TypedDict(
    "_OptionalS3RecordingConfigTypeDef",
    {
        "prefix": str,
    },
    total=False,
)

class S3RecordingConfigTypeDef(
    _RequiredS3RecordingConfigTypeDef, _OptionalS3RecordingConfigTypeDef
):
    pass

TrackingConfigTypeDef = TypedDict(
    "TrackingConfigTypeDef",
    {
        "autotrack": CriticalityType,
    },
)

UplinkEchoConfigTypeDef = TypedDict(
    "UplinkEchoConfigTypeDef",
    {
        "antennaUplinkConfigArn": str,
        "enabled": bool,
    },
)

SocketAddressOutputTypeDef = TypedDict(
    "SocketAddressOutputTypeDef",
    {
        "name": str,
        "port": int,
    },
)

SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef",
    {
        "name": str,
        "port": int,
    },
)

ElevationTypeDef = TypedDict(
    "ElevationTypeDef",
    {
        "unit": AngleUnitsType,
        "value": float,
    },
)

ContactIdResponseTypeDef = TypedDict(
    "ContactIdResponseTypeDef",
    {
        "contactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KmsKeyTypeDef = TypedDict(
    "KmsKeyTypeDef",
    {
        "kmsAliasArn": str,
        "kmsKeyArn": str,
    },
    total=False,
)

DataflowEndpointGroupIdResponseTypeDef = TypedDict(
    "DataflowEndpointGroupIdResponseTypeDef",
    {
        "dataflowEndpointGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataflowEndpointListItemTypeDef = TypedDict(
    "DataflowEndpointListItemTypeDef",
    {
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
    },
    total=False,
)

DeleteConfigRequestRequestTypeDef = TypedDict(
    "DeleteConfigRequestRequestTypeDef",
    {
        "configId": str,
        "configType": ConfigCapabilityTypeType,
    },
)

DeleteDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "DeleteDataflowEndpointGroupRequestRequestTypeDef",
    {
        "dataflowEndpointGroupId": str,
    },
)

DeleteEphemerisRequestRequestTypeDef = TypedDict(
    "DeleteEphemerisRequestRequestTypeDef",
    {
        "ephemerisId": str,
    },
)

DeleteMissionProfileRequestRequestTypeDef = TypedDict(
    "DeleteMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
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

DescribeContactRequestRequestTypeDef = TypedDict(
    "DescribeContactRequestRequestTypeDef",
    {
        "contactId": str,
    },
)

DescribeEphemerisRequestRequestTypeDef = TypedDict(
    "DescribeEphemerisRequestRequestTypeDef",
    {
        "ephemerisId": str,
    },
)

DiscoveryDataTypeDef = TypedDict(
    "DiscoveryDataTypeDef",
    {
        "capabilityArns": Sequence[str],
        "privateIpAddresses": Sequence[str],
        "publicIpAddresses": Sequence[str],
    },
)

SecurityDetailsOutputTypeDef = TypedDict(
    "SecurityDetailsOutputTypeDef",
    {
        "roleArn": str,
        "securityGroupIds": List[str],
        "subnetIds": List[str],
    },
)

SecurityDetailsTypeDef = TypedDict(
    "SecurityDetailsTypeDef",
    {
        "roleArn": str,
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
    },
)

S3ObjectOutputTypeDef = TypedDict(
    "S3ObjectOutputTypeDef",
    {
        "bucket": str,
        "key": str,
        "version": str,
    },
    total=False,
)

EphemerisIdResponseTypeDef = TypedDict(
    "EphemerisIdResponseTypeDef",
    {
        "ephemerisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEphemerisMetaDataTypeDef = TypedDict(
    "_RequiredEphemerisMetaDataTypeDef",
    {
        "source": EphemerisSourceType,
    },
)
_OptionalEphemerisMetaDataTypeDef = TypedDict(
    "_OptionalEphemerisMetaDataTypeDef",
    {
        "ephemerisId": str,
        "epoch": datetime,
        "name": str,
    },
    total=False,
)

class EphemerisMetaDataTypeDef(
    _RequiredEphemerisMetaDataTypeDef, _OptionalEphemerisMetaDataTypeDef
):
    pass

FrequencyBandwidthOutputTypeDef = TypedDict(
    "FrequencyBandwidthOutputTypeDef",
    {
        "units": BandwidthUnitsType,
        "value": float,
    },
)

FrequencyBandwidthTypeDef = TypedDict(
    "FrequencyBandwidthTypeDef",
    {
        "units": BandwidthUnitsType,
        "value": float,
    },
)

FrequencyOutputTypeDef = TypedDict(
    "FrequencyOutputTypeDef",
    {
        "units": FrequencyUnitsType,
        "value": float,
    },
)

FrequencyTypeDef = TypedDict(
    "FrequencyTypeDef",
    {
        "units": FrequencyUnitsType,
        "value": float,
    },
)

GetAgentConfigurationRequestRequestTypeDef = TypedDict(
    "GetAgentConfigurationRequestRequestTypeDef",
    {
        "agentId": str,
    },
)

GetAgentConfigurationResponseTypeDef = TypedDict(
    "GetAgentConfigurationResponseTypeDef",
    {
        "agentId": str,
        "taskingDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigRequestRequestTypeDef = TypedDict(
    "GetConfigRequestRequestTypeDef",
    {
        "configId": str,
        "configType": ConfigCapabilityTypeType,
    },
)

GetDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "GetDataflowEndpointGroupRequestRequestTypeDef",
    {
        "dataflowEndpointGroupId": str,
    },
)

GetMinuteUsageRequestRequestTypeDef = TypedDict(
    "GetMinuteUsageRequestRequestTypeDef",
    {
        "month": int,
        "year": int,
    },
)

GetMinuteUsageResponseTypeDef = TypedDict(
    "GetMinuteUsageResponseTypeDef",
    {
        "estimatedMinutesRemaining": int,
        "isReservedMinutesCustomer": bool,
        "totalReservedMinuteAllocation": int,
        "totalScheduledMinutes": int,
        "upcomingMinutesScheduled": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMissionProfileRequestRequestTypeDef = TypedDict(
    "GetMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
    },
)

KmsKeyOutputTypeDef = TypedDict(
    "KmsKeyOutputTypeDef",
    {
        "kmsAliasArn": str,
        "kmsKeyArn": str,
    },
    total=False,
)

GetSatelliteRequestRequestTypeDef = TypedDict(
    "GetSatelliteRequestRequestTypeDef",
    {
        "satelliteId": str,
    },
)

GroundStationDataTypeDef = TypedDict(
    "GroundStationDataTypeDef",
    {
        "groundStationId": str,
        "groundStationName": str,
        "region": str,
    },
    total=False,
)

IntegerRangeOutputTypeDef = TypedDict(
    "IntegerRangeOutputTypeDef",
    {
        "maximum": int,
        "minimum": int,
    },
)

IntegerRangeTypeDef = TypedDict(
    "IntegerRangeTypeDef",
    {
        "maximum": int,
        "minimum": int,
    },
)

ListConfigsRequestListConfigsPaginateTypeDef = TypedDict(
    "ListConfigsRequestListConfigsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListConfigsRequestRequestTypeDef = TypedDict(
    "ListConfigsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListContactsRequestListContactsPaginateTypeDef = TypedDict(
    "_RequiredListContactsRequestListContactsPaginateTypeDef",
    {
        "endTime": Union[datetime, str],
        "startTime": Union[datetime, str],
        "statusList": Sequence[ContactStatusType],
    },
)
_OptionalListContactsRequestListContactsPaginateTypeDef = TypedDict(
    "_OptionalListContactsRequestListContactsPaginateTypeDef",
    {
        "groundStation": str,
        "missionProfileArn": str,
        "satelliteArn": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListContactsRequestListContactsPaginateTypeDef(
    _RequiredListContactsRequestListContactsPaginateTypeDef,
    _OptionalListContactsRequestListContactsPaginateTypeDef,
):
    pass

_RequiredListContactsRequestRequestTypeDef = TypedDict(
    "_RequiredListContactsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "startTime": Union[datetime, str],
        "statusList": Sequence[ContactStatusType],
    },
)
_OptionalListContactsRequestRequestTypeDef = TypedDict(
    "_OptionalListContactsRequestRequestTypeDef",
    {
        "groundStation": str,
        "maxResults": int,
        "missionProfileArn": str,
        "nextToken": str,
        "satelliteArn": str,
    },
    total=False,
)

class ListContactsRequestRequestTypeDef(
    _RequiredListContactsRequestRequestTypeDef, _OptionalListContactsRequestRequestTypeDef
):
    pass

ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef = TypedDict(
    "ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDataflowEndpointGroupsRequestRequestTypeDef = TypedDict(
    "ListDataflowEndpointGroupsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListEphemeridesRequestListEphemeridesPaginateTypeDef = TypedDict(
    "_RequiredListEphemeridesRequestListEphemeridesPaginateTypeDef",
    {
        "endTime": Union[datetime, str],
        "satelliteId": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalListEphemeridesRequestListEphemeridesPaginateTypeDef = TypedDict(
    "_OptionalListEphemeridesRequestListEphemeridesPaginateTypeDef",
    {
        "statusList": Sequence[EphemerisStatusType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListEphemeridesRequestListEphemeridesPaginateTypeDef(
    _RequiredListEphemeridesRequestListEphemeridesPaginateTypeDef,
    _OptionalListEphemeridesRequestListEphemeridesPaginateTypeDef,
):
    pass

_RequiredListEphemeridesRequestRequestTypeDef = TypedDict(
    "_RequiredListEphemeridesRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "satelliteId": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalListEphemeridesRequestRequestTypeDef = TypedDict(
    "_OptionalListEphemeridesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "statusList": Sequence[EphemerisStatusType],
    },
    total=False,
)

class ListEphemeridesRequestRequestTypeDef(
    _RequiredListEphemeridesRequestRequestTypeDef, _OptionalListEphemeridesRequestRequestTypeDef
):
    pass

ListGroundStationsRequestListGroundStationsPaginateTypeDef = TypedDict(
    "ListGroundStationsRequestListGroundStationsPaginateTypeDef",
    {
        "satelliteId": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListGroundStationsRequestRequestTypeDef = TypedDict(
    "ListGroundStationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "satelliteId": str,
    },
    total=False,
)

ListMissionProfilesRequestListMissionProfilesPaginateTypeDef = TypedDict(
    "ListMissionProfilesRequestListMissionProfilesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListMissionProfilesRequestRequestTypeDef = TypedDict(
    "ListMissionProfilesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

MissionProfileListItemTypeDef = TypedDict(
    "MissionProfileListItemTypeDef",
    {
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
    },
    total=False,
)

ListSatellitesRequestListSatellitesPaginateTypeDef = TypedDict(
    "ListSatellitesRequestListSatellitesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListSatellitesRequestRequestTypeDef = TypedDict(
    "ListSatellitesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

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

MissionProfileIdResponseTypeDef = TypedDict(
    "MissionProfileIdResponseTypeDef",
    {
        "missionProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucket": str,
        "key": str,
        "version": str,
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

RegisterAgentResponseTypeDef = TypedDict(
    "RegisterAgentResponseTypeDef",
    {
        "agentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReserveContactRequestRequestTypeDef = TypedDict(
    "_RequiredReserveContactRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "groundStation": str,
        "missionProfileArn": str,
        "satelliteArn": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalReserveContactRequestRequestTypeDef = TypedDict(
    "_OptionalReserveContactRequestRequestTypeDef",
    {
        "tags": Mapping[str, str],
    },
    total=False,
)

class ReserveContactRequestRequestTypeDef(
    _RequiredReserveContactRequestRequestTypeDef, _OptionalReserveContactRequestRequestTypeDef
):
    pass

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

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "endTime": Union[datetime, str],
        "startTime": Union[datetime, str],
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

UpdateAgentStatusResponseTypeDef = TypedDict(
    "UpdateAgentStatusResponseTypeDef",
    {
        "agentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEphemerisRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEphemerisRequestRequestTypeDef",
    {
        "enabled": bool,
        "ephemerisId": str,
    },
)
_OptionalUpdateEphemerisRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEphemerisRequestRequestTypeDef",
    {
        "name": str,
        "priority": int,
    },
    total=False,
)

class UpdateEphemerisRequestRequestTypeDef(
    _RequiredUpdateEphemerisRequestRequestTypeDef, _OptionalUpdateEphemerisRequestRequestTypeDef
):
    pass

_RequiredAgentDetailsTypeDef = TypedDict(
    "_RequiredAgentDetailsTypeDef",
    {
        "agentVersion": str,
        "componentVersions": Sequence[ComponentVersionTypeDef],
        "instanceId": str,
        "instanceType": str,
    },
)
_OptionalAgentDetailsTypeDef = TypedDict(
    "_OptionalAgentDetailsTypeDef",
    {
        "agentCpuCores": Sequence[int],
        "reservedCpuCores": Sequence[int],
    },
    total=False,
)

class AgentDetailsTypeDef(_RequiredAgentDetailsTypeDef, _OptionalAgentDetailsTypeDef):
    pass

UpdateAgentStatusRequestRequestTypeDef = TypedDict(
    "UpdateAgentStatusRequestRequestTypeDef",
    {
        "agentId": str,
        "aggregateStatus": AggregateStatusTypeDef,
        "componentStatuses": Sequence[ComponentStatusDataTypeDef],
        "taskId": str,
    },
)

ListConfigsResponseTypeDef = TypedDict(
    "ListConfigsResponseTypeDef",
    {
        "configList": List[ConfigListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConnectionDetailsOutputTypeDef = TypedDict(
    "_RequiredConnectionDetailsOutputTypeDef",
    {
        "socketAddress": SocketAddressOutputTypeDef,
    },
)
_OptionalConnectionDetailsOutputTypeDef = TypedDict(
    "_OptionalConnectionDetailsOutputTypeDef",
    {
        "mtu": int,
    },
    total=False,
)

class ConnectionDetailsOutputTypeDef(
    _RequiredConnectionDetailsOutputTypeDef, _OptionalConnectionDetailsOutputTypeDef
):
    pass

DataflowEndpointOutputTypeDef = TypedDict(
    "DataflowEndpointOutputTypeDef",
    {
        "address": SocketAddressOutputTypeDef,
        "mtu": int,
        "name": str,
        "status": EndpointStatusType,
    },
    total=False,
)

_RequiredConnectionDetailsTypeDef = TypedDict(
    "_RequiredConnectionDetailsTypeDef",
    {
        "socketAddress": SocketAddressTypeDef,
    },
)
_OptionalConnectionDetailsTypeDef = TypedDict(
    "_OptionalConnectionDetailsTypeDef",
    {
        "mtu": int,
    },
    total=False,
)

class ConnectionDetailsTypeDef(
    _RequiredConnectionDetailsTypeDef, _OptionalConnectionDetailsTypeDef
):
    pass

DataflowEndpointTypeDef = TypedDict(
    "DataflowEndpointTypeDef",
    {
        "address": SocketAddressTypeDef,
        "mtu": int,
        "name": str,
        "status": EndpointStatusType,
    },
    total=False,
)

ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatusType,
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateMissionProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMissionProfileRequestRequestTypeDef",
    {
        "dataflowEdges": Sequence[Sequence[str]],
        "minimumViableContactDurationSeconds": int,
        "name": str,
        "trackingConfigArn": str,
    },
)
_OptionalCreateMissionProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMissionProfileRequestRequestTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "streamsKmsKey": KmsKeyTypeDef,
        "streamsKmsRole": str,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateMissionProfileRequestRequestTypeDef(
    _RequiredCreateMissionProfileRequestRequestTypeDef,
    _OptionalCreateMissionProfileRequestRequestTypeDef,
):
    pass

_RequiredUpdateMissionProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
    },
)
_OptionalUpdateMissionProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMissionProfileRequestRequestTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": Sequence[Sequence[str]],
        "minimumViableContactDurationSeconds": int,
        "name": str,
        "streamsKmsKey": KmsKeyTypeDef,
        "streamsKmsRole": str,
        "trackingConfigArn": str,
    },
    total=False,
)

class UpdateMissionProfileRequestRequestTypeDef(
    _RequiredUpdateMissionProfileRequestRequestTypeDef,
    _OptionalUpdateMissionProfileRequestRequestTypeDef,
):
    pass

ListDataflowEndpointGroupsResponseTypeDef = TypedDict(
    "ListDataflowEndpointGroupsResponseTypeDef",
    {
        "dataflowEndpointGroupList": List[DataflowEndpointListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeContactRequestContactScheduledWaitTypeDef = TypedDict(
    "_RequiredDescribeContactRequestContactScheduledWaitTypeDef",
    {
        "contactId": str,
    },
)
_OptionalDescribeContactRequestContactScheduledWaitTypeDef = TypedDict(
    "_OptionalDescribeContactRequestContactScheduledWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

class DescribeContactRequestContactScheduledWaitTypeDef(
    _RequiredDescribeContactRequestContactScheduledWaitTypeDef,
    _OptionalDescribeContactRequestContactScheduledWaitTypeDef,
):
    pass

EphemerisDescriptionTypeDef = TypedDict(
    "EphemerisDescriptionTypeDef",
    {
        "ephemerisData": str,
        "sourceS3Object": S3ObjectOutputTypeDef,
    },
    total=False,
)

EphemerisItemTypeDef = TypedDict(
    "EphemerisItemTypeDef",
    {
        "creationTime": datetime,
        "enabled": bool,
        "ephemerisId": str,
        "name": str,
        "priority": int,
        "sourceS3Object": S3ObjectOutputTypeDef,
        "status": EphemerisStatusType,
    },
    total=False,
)

GetSatelliteResponseTypeDef = TypedDict(
    "GetSatelliteResponseTypeDef",
    {
        "currentEphemeris": EphemerisMetaDataTypeDef,
        "groundStations": List[str],
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SatelliteListItemTypeDef = TypedDict(
    "SatelliteListItemTypeDef",
    {
        "currentEphemeris": EphemerisMetaDataTypeDef,
        "groundStations": List[str],
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
    },
    total=False,
)

_RequiredSpectrumConfigOutputTypeDef = TypedDict(
    "_RequiredSpectrumConfigOutputTypeDef",
    {
        "bandwidth": FrequencyBandwidthOutputTypeDef,
        "centerFrequency": FrequencyOutputTypeDef,
    },
)
_OptionalSpectrumConfigOutputTypeDef = TypedDict(
    "_OptionalSpectrumConfigOutputTypeDef",
    {
        "polarization": PolarizationType,
    },
    total=False,
)

class SpectrumConfigOutputTypeDef(
    _RequiredSpectrumConfigOutputTypeDef, _OptionalSpectrumConfigOutputTypeDef
):
    pass

_RequiredUplinkSpectrumConfigOutputTypeDef = TypedDict(
    "_RequiredUplinkSpectrumConfigOutputTypeDef",
    {
        "centerFrequency": FrequencyOutputTypeDef,
    },
)
_OptionalUplinkSpectrumConfigOutputTypeDef = TypedDict(
    "_OptionalUplinkSpectrumConfigOutputTypeDef",
    {
        "polarization": PolarizationType,
    },
    total=False,
)

class UplinkSpectrumConfigOutputTypeDef(
    _RequiredUplinkSpectrumConfigOutputTypeDef, _OptionalUplinkSpectrumConfigOutputTypeDef
):
    pass

_RequiredSpectrumConfigTypeDef = TypedDict(
    "_RequiredSpectrumConfigTypeDef",
    {
        "bandwidth": FrequencyBandwidthTypeDef,
        "centerFrequency": FrequencyTypeDef,
    },
)
_OptionalSpectrumConfigTypeDef = TypedDict(
    "_OptionalSpectrumConfigTypeDef",
    {
        "polarization": PolarizationType,
    },
    total=False,
)

class SpectrumConfigTypeDef(_RequiredSpectrumConfigTypeDef, _OptionalSpectrumConfigTypeDef):
    pass

_RequiredUplinkSpectrumConfigTypeDef = TypedDict(
    "_RequiredUplinkSpectrumConfigTypeDef",
    {
        "centerFrequency": FrequencyTypeDef,
    },
)
_OptionalUplinkSpectrumConfigTypeDef = TypedDict(
    "_OptionalUplinkSpectrumConfigTypeDef",
    {
        "polarization": PolarizationType,
    },
    total=False,
)

class UplinkSpectrumConfigTypeDef(
    _RequiredUplinkSpectrumConfigTypeDef, _OptionalUplinkSpectrumConfigTypeDef
):
    pass

GetMissionProfileResponseTypeDef = TypedDict(
    "GetMissionProfileResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
        "streamsKmsKey": KmsKeyOutputTypeDef,
        "streamsKmsRole": str,
        "tags": Dict[str, str],
        "trackingConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroundStationsResponseTypeDef = TypedDict(
    "ListGroundStationsResponseTypeDef",
    {
        "groundStationList": List[GroundStationDataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangedSocketAddressOutputTypeDef = TypedDict(
    "RangedSocketAddressOutputTypeDef",
    {
        "name": str,
        "portRange": IntegerRangeOutputTypeDef,
    },
)

RangedSocketAddressTypeDef = TypedDict(
    "RangedSocketAddressTypeDef",
    {
        "name": str,
        "portRange": IntegerRangeTypeDef,
    },
)

ListMissionProfilesResponseTypeDef = TypedDict(
    "ListMissionProfilesResponseTypeDef",
    {
        "missionProfileList": List[MissionProfileListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OEMEphemerisTypeDef = TypedDict(
    "OEMEphemerisTypeDef",
    {
        "oemData": str,
        "s3Object": S3ObjectTypeDef,
    },
    total=False,
)

TLEDataTypeDef = TypedDict(
    "TLEDataTypeDef",
    {
        "tleLine1": str,
        "tleLine2": str,
        "validTimeRange": TimeRangeTypeDef,
    },
)

RegisterAgentRequestRequestTypeDef = TypedDict(
    "RegisterAgentRequestRequestTypeDef",
    {
        "agentDetails": AgentDetailsTypeDef,
        "discoveryData": DiscoveryDataTypeDef,
    },
)

ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {
        "contactList": List[ContactDataTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EphemerisTypeDescriptionTypeDef = TypedDict(
    "EphemerisTypeDescriptionTypeDef",
    {
        "oem": EphemerisDescriptionTypeDef,
        "tle": EphemerisDescriptionTypeDef,
    },
    total=False,
)

ListEphemeridesResponseTypeDef = TypedDict(
    "ListEphemeridesResponseTypeDef",
    {
        "ephemerides": List[EphemerisItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSatellitesResponseTypeDef = TypedDict(
    "ListSatellitesResponseTypeDef",
    {
        "nextToken": str,
        "satellites": List[SatelliteListItemTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AntennaDownlinkConfigOutputTypeDef = TypedDict(
    "AntennaDownlinkConfigOutputTypeDef",
    {
        "spectrumConfig": SpectrumConfigOutputTypeDef,
    },
)

AntennaDownlinkDemodDecodeConfigOutputTypeDef = TypedDict(
    "AntennaDownlinkDemodDecodeConfigOutputTypeDef",
    {
        "decodeConfig": DecodeConfigOutputTypeDef,
        "demodulationConfig": DemodulationConfigOutputTypeDef,
        "spectrumConfig": SpectrumConfigOutputTypeDef,
    },
)

_RequiredAntennaUplinkConfigOutputTypeDef = TypedDict(
    "_RequiredAntennaUplinkConfigOutputTypeDef",
    {
        "spectrumConfig": UplinkSpectrumConfigOutputTypeDef,
        "targetEirp": EirpOutputTypeDef,
    },
)
_OptionalAntennaUplinkConfigOutputTypeDef = TypedDict(
    "_OptionalAntennaUplinkConfigOutputTypeDef",
    {
        "transmitDisabled": bool,
    },
    total=False,
)

class AntennaUplinkConfigOutputTypeDef(
    _RequiredAntennaUplinkConfigOutputTypeDef, _OptionalAntennaUplinkConfigOutputTypeDef
):
    pass

AntennaDownlinkConfigTypeDef = TypedDict(
    "AntennaDownlinkConfigTypeDef",
    {
        "spectrumConfig": SpectrumConfigTypeDef,
    },
)

AntennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": DecodeConfigTypeDef,
        "demodulationConfig": DemodulationConfigTypeDef,
        "spectrumConfig": SpectrumConfigTypeDef,
    },
)

_RequiredAntennaUplinkConfigTypeDef = TypedDict(
    "_RequiredAntennaUplinkConfigTypeDef",
    {
        "spectrumConfig": UplinkSpectrumConfigTypeDef,
        "targetEirp": EirpTypeDef,
    },
)
_OptionalAntennaUplinkConfigTypeDef = TypedDict(
    "_OptionalAntennaUplinkConfigTypeDef",
    {
        "transmitDisabled": bool,
    },
    total=False,
)

class AntennaUplinkConfigTypeDef(
    _RequiredAntennaUplinkConfigTypeDef, _OptionalAntennaUplinkConfigTypeDef
):
    pass

_RequiredRangedConnectionDetailsOutputTypeDef = TypedDict(
    "_RequiredRangedConnectionDetailsOutputTypeDef",
    {
        "socketAddress": RangedSocketAddressOutputTypeDef,
    },
)
_OptionalRangedConnectionDetailsOutputTypeDef = TypedDict(
    "_OptionalRangedConnectionDetailsOutputTypeDef",
    {
        "mtu": int,
    },
    total=False,
)

class RangedConnectionDetailsOutputTypeDef(
    _RequiredRangedConnectionDetailsOutputTypeDef, _OptionalRangedConnectionDetailsOutputTypeDef
):
    pass

_RequiredRangedConnectionDetailsTypeDef = TypedDict(
    "_RequiredRangedConnectionDetailsTypeDef",
    {
        "socketAddress": RangedSocketAddressTypeDef,
    },
)
_OptionalRangedConnectionDetailsTypeDef = TypedDict(
    "_OptionalRangedConnectionDetailsTypeDef",
    {
        "mtu": int,
    },
    total=False,
)

class RangedConnectionDetailsTypeDef(
    _RequiredRangedConnectionDetailsTypeDef, _OptionalRangedConnectionDetailsTypeDef
):
    pass

TLEEphemerisTypeDef = TypedDict(
    "TLEEphemerisTypeDef",
    {
        "s3Object": S3ObjectTypeDef,
        "tleData": Sequence[TLEDataTypeDef],
    },
    total=False,
)

DescribeEphemerisResponseTypeDef = TypedDict(
    "DescribeEphemerisResponseTypeDef",
    {
        "creationTime": datetime,
        "enabled": bool,
        "ephemerisId": str,
        "invalidReason": EphemerisInvalidReasonType,
        "name": str,
        "priority": int,
        "satelliteId": str,
        "status": EphemerisStatusType,
        "suppliedData": EphemerisTypeDescriptionTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigTypeDataOutputTypeDef = TypedDict(
    "ConfigTypeDataOutputTypeDef",
    {
        "antennaDownlinkConfig": AntennaDownlinkConfigOutputTypeDef,
        "antennaDownlinkDemodDecodeConfig": AntennaDownlinkDemodDecodeConfigOutputTypeDef,
        "antennaUplinkConfig": AntennaUplinkConfigOutputTypeDef,
        "dataflowEndpointConfig": DataflowEndpointConfigOutputTypeDef,
        "s3RecordingConfig": S3RecordingConfigOutputTypeDef,
        "trackingConfig": TrackingConfigOutputTypeDef,
        "uplinkEchoConfig": UplinkEchoConfigOutputTypeDef,
    },
    total=False,
)

ConfigTypeDataTypeDef = TypedDict(
    "ConfigTypeDataTypeDef",
    {
        "antennaDownlinkConfig": AntennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": AntennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": AntennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": DataflowEndpointConfigTypeDef,
        "s3RecordingConfig": S3RecordingConfigTypeDef,
        "trackingConfig": TrackingConfigTypeDef,
        "uplinkEchoConfig": UplinkEchoConfigTypeDef,
    },
    total=False,
)

_RequiredAwsGroundStationAgentEndpointOutputTypeDef = TypedDict(
    "_RequiredAwsGroundStationAgentEndpointOutputTypeDef",
    {
        "egressAddress": ConnectionDetailsOutputTypeDef,
        "ingressAddress": RangedConnectionDetailsOutputTypeDef,
        "name": str,
    },
)
_OptionalAwsGroundStationAgentEndpointOutputTypeDef = TypedDict(
    "_OptionalAwsGroundStationAgentEndpointOutputTypeDef",
    {
        "agentStatus": AgentStatusType,
        "auditResults": AuditResultsType,
    },
    total=False,
)

class AwsGroundStationAgentEndpointOutputTypeDef(
    _RequiredAwsGroundStationAgentEndpointOutputTypeDef,
    _OptionalAwsGroundStationAgentEndpointOutputTypeDef,
):
    pass

_RequiredAwsGroundStationAgentEndpointTypeDef = TypedDict(
    "_RequiredAwsGroundStationAgentEndpointTypeDef",
    {
        "egressAddress": ConnectionDetailsTypeDef,
        "ingressAddress": RangedConnectionDetailsTypeDef,
        "name": str,
    },
)
_OptionalAwsGroundStationAgentEndpointTypeDef = TypedDict(
    "_OptionalAwsGroundStationAgentEndpointTypeDef",
    {
        "agentStatus": AgentStatusType,
        "auditResults": AuditResultsType,
    },
    total=False,
)

class AwsGroundStationAgentEndpointTypeDef(
    _RequiredAwsGroundStationAgentEndpointTypeDef, _OptionalAwsGroundStationAgentEndpointTypeDef
):
    pass

EphemerisDataTypeDef = TypedDict(
    "EphemerisDataTypeDef",
    {
        "oem": OEMEphemerisTypeDef,
        "tle": TLEEphemerisTypeDef,
    },
    total=False,
)

GetConfigResponseTypeDef = TypedDict(
    "GetConfigResponseTypeDef",
    {
        "configArn": str,
        "configData": ConfigTypeDataOutputTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigRequestRequestTypeDef",
    {
        "configData": ConfigTypeDataTypeDef,
        "name": str,
    },
)
_OptionalCreateConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigRequestRequestTypeDef",
    {
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateConfigRequestRequestTypeDef(
    _RequiredCreateConfigRequestRequestTypeDef, _OptionalCreateConfigRequestRequestTypeDef
):
    pass

UpdateConfigRequestRequestTypeDef = TypedDict(
    "UpdateConfigRequestRequestTypeDef",
    {
        "configData": ConfigTypeDataTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
    },
)

EndpointDetailsOutputTypeDef = TypedDict(
    "EndpointDetailsOutputTypeDef",
    {
        "awsGroundStationAgentEndpoint": AwsGroundStationAgentEndpointOutputTypeDef,
        "endpoint": DataflowEndpointOutputTypeDef,
        "healthReasons": List[CapabilityHealthReasonType],
        "healthStatus": CapabilityHealthType,
        "securityDetails": SecurityDetailsOutputTypeDef,
    },
    total=False,
)

EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "awsGroundStationAgentEndpoint": AwsGroundStationAgentEndpointTypeDef,
        "endpoint": DataflowEndpointTypeDef,
        "healthReasons": Sequence[CapabilityHealthReasonType],
        "healthStatus": CapabilityHealthType,
        "securityDetails": SecurityDetailsTypeDef,
    },
    total=False,
)

_RequiredCreateEphemerisRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEphemerisRequestRequestTypeDef",
    {
        "name": str,
        "satelliteId": str,
    },
)
_OptionalCreateEphemerisRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEphemerisRequestRequestTypeDef",
    {
        "enabled": bool,
        "ephemeris": EphemerisDataTypeDef,
        "expirationTime": Union[datetime, str],
        "kmsKeyArn": str,
        "priority": int,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateEphemerisRequestRequestTypeDef(
    _RequiredCreateEphemerisRequestRequestTypeDef, _OptionalCreateEphemerisRequestRequestTypeDef
):
    pass

ConfigDetailsTypeDef = TypedDict(
    "ConfigDetailsTypeDef",
    {
        "antennaDemodDecodeDetails": AntennaDemodDecodeDetailsTypeDef,
        "endpointDetails": EndpointDetailsOutputTypeDef,
        "s3RecordingDetails": S3RecordingDetailsTypeDef,
    },
    total=False,
)

GetDataflowEndpointGroupResponseTypeDef = TypedDict(
    "GetDataflowEndpointGroupResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
        "endpointsDetails": List[EndpointDetailsOutputTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataflowEndpointGroupRequestRequestTypeDef",
    {
        "endpointDetails": Sequence[EndpointDetailsTypeDef],
    },
)
_OptionalCreateDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataflowEndpointGroupRequestRequestTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateDataflowEndpointGroupRequestRequestTypeDef(
    _RequiredCreateDataflowEndpointGroupRequestRequestTypeDef,
    _OptionalCreateDataflowEndpointGroupRequestRequestTypeDef,
):
    pass

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "configDetails": ConfigDetailsTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "dataflowDestinationRegion": str,
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "configDetails": ConfigDetailsTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "dataflowSourceRegion": str,
    },
    total=False,
)

DataflowDetailTypeDef = TypedDict(
    "DataflowDetailTypeDef",
    {
        "destination": DestinationTypeDef,
        "errorMessage": str,
        "source": SourceTypeDef,
    },
    total=False,
)

DescribeContactResponseTypeDef = TypedDict(
    "DescribeContactResponseTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatusType,
        "dataflowList": List[DataflowDetailTypeDef],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
