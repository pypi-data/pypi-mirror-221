"""
Type annotations for sms service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/type_defs/)

Usage::

    ```python
    from mypy_boto3_sms.type_defs import LaunchDetailsTypeDef

    data: LaunchDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AppLaunchConfigurationStatusType,
    AppLaunchStatusType,
    AppReplicationConfigurationStatusType,
    AppReplicationStatusType,
    AppStatusType,
    ConnectorCapabilityType,
    ConnectorStatusType,
    LicenseTypeType,
    OutputFormatType,
    ReplicationJobStateType,
    ReplicationRunStateType,
    ReplicationRunTypeType,
    ScriptTypeType,
    ServerCatalogStatusType,
    ValidationStatusType,
    VmManagerTypeType,
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
    "LaunchDetailsTypeDef",
    "ConnectorTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "TagOutputTypeDef",
    "CreateReplicationJobRequestRequestTypeDef",
    "DeleteAppLaunchConfigurationRequestRequestTypeDef",
    "DeleteAppReplicationConfigurationRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppValidationConfigurationRequestRequestTypeDef",
    "DeleteReplicationJobRequestRequestTypeDef",
    "DisassociateConnectorRequestRequestTypeDef",
    "GenerateChangeSetRequestRequestTypeDef",
    "S3LocationOutputTypeDef",
    "GenerateTemplateRequestRequestTypeDef",
    "GetAppLaunchConfigurationRequestRequestTypeDef",
    "GetAppReplicationConfigurationRequestRequestTypeDef",
    "GetAppRequestRequestTypeDef",
    "GetAppValidationConfigurationRequestRequestTypeDef",
    "GetAppValidationOutputRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetConnectorsRequestRequestTypeDef",
    "GetReplicationJobsRequestRequestTypeDef",
    "GetReplicationRunsRequestRequestTypeDef",
    "VmServerAddressTypeDef",
    "ImportAppCatalogRequestRequestTypeDef",
    "LaunchAppRequestRequestTypeDef",
    "ListAppsRequestRequestTypeDef",
    "NotificationContextTypeDef",
    "ReplicationRunStageDetailsTypeDef",
    "S3LocationTypeDef",
    "ServerReplicationParametersOutputTypeDef",
    "ServerReplicationParametersTypeDef",
    "StartAppReplicationRequestRequestTypeDef",
    "StartOnDemandAppReplicationRequestRequestTypeDef",
    "StartOnDemandReplicationRunRequestRequestTypeDef",
    "StopAppReplicationRequestRequestTypeDef",
    "TerminateAppRequestRequestTypeDef",
    "UpdateReplicationJobRequestRequestTypeDef",
    "VmServerAddressOutputTypeDef",
    "AppSummaryTypeDef",
    "CreateReplicationJobResponseTypeDef",
    "GetConnectorsResponseTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "GenerateChangeSetResponseTypeDef",
    "GenerateTemplateResponseTypeDef",
    "SSMOutputTypeDef",
    "SourceOutputTypeDef",
    "UserDataOutputTypeDef",
    "GetConnectorsRequestGetConnectorsPaginateTypeDef",
    "GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef",
    "GetReplicationRunsRequestGetReplicationRunsPaginateTypeDef",
    "ListAppsRequestListAppsPaginateTypeDef",
    "GetServersRequestGetServersPaginateTypeDef",
    "GetServersRequestRequestTypeDef",
    "VmServerTypeDef",
    "NotifyAppValidationOutputRequestRequestTypeDef",
    "ReplicationRunTypeDef",
    "SourceTypeDef",
    "UserDataTypeDef",
    "VmServerOutputTypeDef",
    "ListAppsResponseTypeDef",
    "AppValidationOutputTypeDef",
    "SSMValidationParametersOutputTypeDef",
    "UserDataValidationParametersOutputTypeDef",
    "ServerTypeDef",
    "SSMValidationParametersTypeDef",
    "UserDataValidationParametersTypeDef",
    "ReplicationJobTypeDef",
    "ServerOutputTypeDef",
    "AppValidationConfigurationOutputTypeDef",
    "ServerGroupTypeDef",
    "ServerLaunchConfigurationTypeDef",
    "ServerReplicationConfigurationTypeDef",
    "AppValidationConfigurationTypeDef",
    "ServerValidationConfigurationTypeDef",
    "GetReplicationJobsResponseTypeDef",
    "GetReplicationRunsResponseTypeDef",
    "GetServersResponseTypeDef",
    "ServerGroupOutputTypeDef",
    "ServerLaunchConfigurationOutputTypeDef",
    "ServerReplicationConfigurationOutputTypeDef",
    "ServerValidationConfigurationOutputTypeDef",
    "ServerValidationOutputTypeDef",
    "CreateAppRequestRequestTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "ServerGroupLaunchConfigurationTypeDef",
    "ServerGroupReplicationConfigurationTypeDef",
    "ServerGroupValidationConfigurationTypeDef",
    "CreateAppResponseTypeDef",
    "GetAppResponseTypeDef",
    "UpdateAppResponseTypeDef",
    "ServerGroupLaunchConfigurationOutputTypeDef",
    "ServerGroupReplicationConfigurationOutputTypeDef",
    "ServerGroupValidationConfigurationOutputTypeDef",
    "ValidationOutputTypeDef",
    "PutAppLaunchConfigurationRequestRequestTypeDef",
    "PutAppReplicationConfigurationRequestRequestTypeDef",
    "PutAppValidationConfigurationRequestRequestTypeDef",
    "GetAppLaunchConfigurationResponseTypeDef",
    "GetAppReplicationConfigurationResponseTypeDef",
    "GetAppValidationConfigurationResponseTypeDef",
    "GetAppValidationOutputResponseTypeDef",
)

LaunchDetailsTypeDef = TypedDict(
    "LaunchDetailsTypeDef",
    {
        "latestLaunchTime": datetime,
        "stackName": str,
        "stackId": str,
    },
    total=False,
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": ConnectorStatusType,
        "capabilityList": List[ConnectorCapabilityType],
        "vmManagerName": str,
        "vmManagerType": VmManagerTypeType,
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
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

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredCreateReplicationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationJobRequestRequestTypeDef",
    {
        "serverId": str,
        "seedReplicationTime": Union[datetime, str],
    },
)
_OptionalCreateReplicationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationJobRequestRequestTypeDef",
    {
        "frequency": int,
        "runOnce": bool,
        "licenseType": LicenseTypeType,
        "roleName": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

class CreateReplicationJobRequestRequestTypeDef(
    _RequiredCreateReplicationJobRequestRequestTypeDef,
    _OptionalCreateReplicationJobRequestRequestTypeDef,
):
    pass

DeleteAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

DeleteAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "appId": str,
        "forceStopAppReplication": bool,
        "forceTerminateApp": bool,
    },
    total=False,
)

DeleteAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)

DeleteReplicationJobRequestRequestTypeDef = TypedDict(
    "DeleteReplicationJobRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)

DisassociateConnectorRequestRequestTypeDef = TypedDict(
    "DisassociateConnectorRequestRequestTypeDef",
    {
        "connectorId": str,
    },
)

GenerateChangeSetRequestRequestTypeDef = TypedDict(
    "GenerateChangeSetRequestRequestTypeDef",
    {
        "appId": str,
        "changesetFormat": OutputFormatType,
    },
    total=False,
)

S3LocationOutputTypeDef = TypedDict(
    "S3LocationOutputTypeDef",
    {
        "bucket": str,
        "key": str,
    },
    total=False,
)

GenerateTemplateRequestRequestTypeDef = TypedDict(
    "GenerateTemplateRequestRequestTypeDef",
    {
        "appId": str,
        "templateFormat": OutputFormatType,
    },
    total=False,
)

GetAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppRequestRequestTypeDef = TypedDict(
    "GetAppRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppValidationOutputRequestRequestTypeDef = TypedDict(
    "GetAppValidationOutputRequestRequestTypeDef",
    {
        "appId": str,
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

GetConnectorsRequestRequestTypeDef = TypedDict(
    "GetConnectorsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetReplicationJobsRequestRequestTypeDef = TypedDict(
    "GetReplicationJobsRequestRequestTypeDef",
    {
        "replicationJobId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredGetReplicationRunsRequestRequestTypeDef = TypedDict(
    "_RequiredGetReplicationRunsRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalGetReplicationRunsRequestRequestTypeDef = TypedDict(
    "_OptionalGetReplicationRunsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetReplicationRunsRequestRequestTypeDef(
    _RequiredGetReplicationRunsRequestRequestTypeDef,
    _OptionalGetReplicationRunsRequestRequestTypeDef,
):
    pass

VmServerAddressTypeDef = TypedDict(
    "VmServerAddressTypeDef",
    {
        "vmManagerId": str,
        "vmId": str,
    },
    total=False,
)

ImportAppCatalogRequestRequestTypeDef = TypedDict(
    "ImportAppCatalogRequestRequestTypeDef",
    {
        "roleName": str,
    },
    total=False,
)

LaunchAppRequestRequestTypeDef = TypedDict(
    "LaunchAppRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "appIds": Sequence[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

NotificationContextTypeDef = TypedDict(
    "NotificationContextTypeDef",
    {
        "validationId": str,
        "status": ValidationStatusType,
        "statusMessage": str,
    },
    total=False,
)

ReplicationRunStageDetailsTypeDef = TypedDict(
    "ReplicationRunStageDetailsTypeDef",
    {
        "stage": str,
        "stageProgress": str,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
    total=False,
)

ServerReplicationParametersOutputTypeDef = TypedDict(
    "ServerReplicationParametersOutputTypeDef",
    {
        "seedTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "licenseType": LicenseTypeType,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

ServerReplicationParametersTypeDef = TypedDict(
    "ServerReplicationParametersTypeDef",
    {
        "seedTime": Union[datetime, str],
        "frequency": int,
        "runOnce": bool,
        "licenseType": LicenseTypeType,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

StartAppReplicationRequestRequestTypeDef = TypedDict(
    "StartAppReplicationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

_RequiredStartOnDemandAppReplicationRequestRequestTypeDef = TypedDict(
    "_RequiredStartOnDemandAppReplicationRequestRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalStartOnDemandAppReplicationRequestRequestTypeDef = TypedDict(
    "_OptionalStartOnDemandAppReplicationRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class StartOnDemandAppReplicationRequestRequestTypeDef(
    _RequiredStartOnDemandAppReplicationRequestRequestTypeDef,
    _OptionalStartOnDemandAppReplicationRequestRequestTypeDef,
):
    pass

_RequiredStartOnDemandReplicationRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartOnDemandReplicationRunRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalStartOnDemandReplicationRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartOnDemandReplicationRunRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class StartOnDemandReplicationRunRequestRequestTypeDef(
    _RequiredStartOnDemandReplicationRunRequestRequestTypeDef,
    _OptionalStartOnDemandReplicationRunRequestRequestTypeDef,
):
    pass

StopAppReplicationRequestRequestTypeDef = TypedDict(
    "StopAppReplicationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

TerminateAppRequestRequestTypeDef = TypedDict(
    "TerminateAppRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

_RequiredUpdateReplicationJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationJobRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalUpdateReplicationJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationJobRequestRequestTypeDef",
    {
        "frequency": int,
        "nextReplicationRunStartTime": Union[datetime, str],
        "licenseType": LicenseTypeType,
        "roleName": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

class UpdateReplicationJobRequestRequestTypeDef(
    _RequiredUpdateReplicationJobRequestRequestTypeDef,
    _OptionalUpdateReplicationJobRequestRequestTypeDef,
):
    pass

VmServerAddressOutputTypeDef = TypedDict(
    "VmServerAddressOutputTypeDef",
    {
        "vmManagerId": str,
        "vmId": str,
    },
    total=False,
)

AppSummaryTypeDef = TypedDict(
    "AppSummaryTypeDef",
    {
        "appId": str,
        "importedAppId": str,
        "name": str,
        "description": str,
        "status": AppStatusType,
        "statusMessage": str,
        "replicationConfigurationStatus": AppReplicationConfigurationStatusType,
        "replicationStatus": AppReplicationStatusType,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchConfigurationStatus": AppLaunchConfigurationStatusType,
        "launchStatus": AppLaunchStatusType,
        "launchStatusMessage": str,
        "launchDetails": LaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)

CreateReplicationJobResponseTypeDef = TypedDict(
    "CreateReplicationJobResponseTypeDef",
    {
        "replicationJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetConnectorsResponseTypeDef = TypedDict(
    "GetConnectorsResponseTypeDef",
    {
        "connectorList": List[ConnectorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "StartOnDemandReplicationRunResponseTypeDef",
    {
        "replicationRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GenerateChangeSetResponseTypeDef = TypedDict(
    "GenerateChangeSetResponseTypeDef",
    {
        "s3Location": S3LocationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GenerateTemplateResponseTypeDef = TypedDict(
    "GenerateTemplateResponseTypeDef",
    {
        "s3Location": S3LocationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SSMOutputTypeDef = TypedDict(
    "SSMOutputTypeDef",
    {
        "s3Location": S3LocationOutputTypeDef,
    },
    total=False,
)

SourceOutputTypeDef = TypedDict(
    "SourceOutputTypeDef",
    {
        "s3Location": S3LocationOutputTypeDef,
    },
    total=False,
)

UserDataOutputTypeDef = TypedDict(
    "UserDataOutputTypeDef",
    {
        "s3Location": S3LocationOutputTypeDef,
    },
    total=False,
)

GetConnectorsRequestGetConnectorsPaginateTypeDef = TypedDict(
    "GetConnectorsRequestGetConnectorsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef = TypedDict(
    "GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef",
    {
        "replicationJobId": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredGetReplicationRunsRequestGetReplicationRunsPaginateTypeDef = TypedDict(
    "_RequiredGetReplicationRunsRequestGetReplicationRunsPaginateTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalGetReplicationRunsRequestGetReplicationRunsPaginateTypeDef = TypedDict(
    "_OptionalGetReplicationRunsRequestGetReplicationRunsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class GetReplicationRunsRequestGetReplicationRunsPaginateTypeDef(
    _RequiredGetReplicationRunsRequestGetReplicationRunsPaginateTypeDef,
    _OptionalGetReplicationRunsRequestGetReplicationRunsPaginateTypeDef,
):
    pass

ListAppsRequestListAppsPaginateTypeDef = TypedDict(
    "ListAppsRequestListAppsPaginateTypeDef",
    {
        "appIds": Sequence[str],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetServersRequestGetServersPaginateTypeDef = TypedDict(
    "GetServersRequestGetServersPaginateTypeDef",
    {
        "vmServerAddressList": Sequence[VmServerAddressTypeDef],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

GetServersRequestRequestTypeDef = TypedDict(
    "GetServersRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "vmServerAddressList": Sequence[VmServerAddressTypeDef],
    },
    total=False,
)

VmServerTypeDef = TypedDict(
    "VmServerTypeDef",
    {
        "vmServerAddress": VmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": VmManagerTypeType,
        "vmPath": str,
    },
    total=False,
)

_RequiredNotifyAppValidationOutputRequestRequestTypeDef = TypedDict(
    "_RequiredNotifyAppValidationOutputRequestRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalNotifyAppValidationOutputRequestRequestTypeDef = TypedDict(
    "_OptionalNotifyAppValidationOutputRequestRequestTypeDef",
    {
        "notificationContext": NotificationContextTypeDef,
    },
    total=False,
)

class NotifyAppValidationOutputRequestRequestTypeDef(
    _RequiredNotifyAppValidationOutputRequestRequestTypeDef,
    _OptionalNotifyAppValidationOutputRequestRequestTypeDef,
):
    pass

ReplicationRunTypeDef = TypedDict(
    "ReplicationRunTypeDef",
    {
        "replicationRunId": str,
        "state": ReplicationRunStateType,
        "type": ReplicationRunTypeType,
        "stageDetails": ReplicationRunStageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Location": S3LocationTypeDef,
    },
    total=False,
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "s3Location": S3LocationTypeDef,
    },
    total=False,
)

VmServerOutputTypeDef = TypedDict(
    "VmServerOutputTypeDef",
    {
        "vmServerAddress": VmServerAddressOutputTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": VmManagerTypeType,
        "vmPath": str,
    },
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "apps": List[AppSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AppValidationOutputTypeDef = TypedDict(
    "AppValidationOutputTypeDef",
    {
        "ssmOutput": SSMOutputTypeDef,
    },
    total=False,
)

SSMValidationParametersOutputTypeDef = TypedDict(
    "SSMValidationParametersOutputTypeDef",
    {
        "source": SourceOutputTypeDef,
        "instanceId": str,
        "scriptType": ScriptTypeType,
        "command": str,
        "executionTimeoutSeconds": int,
        "outputS3BucketName": str,
    },
    total=False,
)

UserDataValidationParametersOutputTypeDef = TypedDict(
    "UserDataValidationParametersOutputTypeDef",
    {
        "source": SourceOutputTypeDef,
        "scriptType": ScriptTypeType,
    },
    total=False,
)

ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "serverId": str,
        "serverType": Literal["VIRTUAL_MACHINE"],
        "vmServer": VmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

SSMValidationParametersTypeDef = TypedDict(
    "SSMValidationParametersTypeDef",
    {
        "source": SourceTypeDef,
        "instanceId": str,
        "scriptType": ScriptTypeType,
        "command": str,
        "executionTimeoutSeconds": int,
        "outputS3BucketName": str,
    },
    total=False,
)

UserDataValidationParametersTypeDef = TypedDict(
    "UserDataValidationParametersTypeDef",
    {
        "source": SourceTypeDef,
        "scriptType": ScriptTypeType,
    },
    total=False,
)

ReplicationJobTypeDef = TypedDict(
    "ReplicationJobTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": Literal["VIRTUAL_MACHINE"],
        "vmServer": VmServerOutputTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": LicenseTypeType,
        "roleName": str,
        "latestAmiId": str,
        "state": ReplicationJobStateType,
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[ReplicationRunTypeDef],
    },
    total=False,
)

ServerOutputTypeDef = TypedDict(
    "ServerOutputTypeDef",
    {
        "serverId": str,
        "serverType": Literal["VIRTUAL_MACHINE"],
        "vmServer": VmServerOutputTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

AppValidationConfigurationOutputTypeDef = TypedDict(
    "AppValidationConfigurationOutputTypeDef",
    {
        "validationId": str,
        "name": str,
        "appValidationStrategy": Literal["SSM"],
        "ssmValidationParameters": SSMValidationParametersOutputTypeDef,
    },
    total=False,
)

ServerGroupTypeDef = TypedDict(
    "ServerGroupTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": Sequence[ServerTypeDef],
    },
    total=False,
)

ServerLaunchConfigurationTypeDef = TypedDict(
    "ServerLaunchConfigurationTypeDef",
    {
        "server": ServerTypeDef,
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": UserDataTypeDef,
        "instanceType": str,
        "associatePublicIpAddress": bool,
        "iamInstanceProfileName": str,
        "configureScript": S3LocationTypeDef,
        "configureScriptType": ScriptTypeType,
    },
    total=False,
)

ServerReplicationConfigurationTypeDef = TypedDict(
    "ServerReplicationConfigurationTypeDef",
    {
        "server": ServerTypeDef,
        "serverReplicationParameters": ServerReplicationParametersTypeDef,
    },
    total=False,
)

AppValidationConfigurationTypeDef = TypedDict(
    "AppValidationConfigurationTypeDef",
    {
        "validationId": str,
        "name": str,
        "appValidationStrategy": Literal["SSM"],
        "ssmValidationParameters": SSMValidationParametersTypeDef,
    },
    total=False,
)

ServerValidationConfigurationTypeDef = TypedDict(
    "ServerValidationConfigurationTypeDef",
    {
        "server": ServerTypeDef,
        "validationId": str,
        "name": str,
        "serverValidationStrategy": Literal["USERDATA"],
        "userDataValidationParameters": UserDataValidationParametersTypeDef,
    },
    total=False,
)

GetReplicationJobsResponseTypeDef = TypedDict(
    "GetReplicationJobsResponseTypeDef",
    {
        "replicationJobList": List[ReplicationJobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetReplicationRunsResponseTypeDef = TypedDict(
    "GetReplicationRunsResponseTypeDef",
    {
        "replicationJob": ReplicationJobTypeDef,
        "replicationRunList": List[ReplicationRunTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetServersResponseTypeDef = TypedDict(
    "GetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": ServerCatalogStatusType,
        "serverList": List[ServerOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ServerGroupOutputTypeDef = TypedDict(
    "ServerGroupOutputTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ServerOutputTypeDef],
    },
    total=False,
)

ServerLaunchConfigurationOutputTypeDef = TypedDict(
    "ServerLaunchConfigurationOutputTypeDef",
    {
        "server": ServerOutputTypeDef,
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": UserDataOutputTypeDef,
        "instanceType": str,
        "associatePublicIpAddress": bool,
        "iamInstanceProfileName": str,
        "configureScript": S3LocationOutputTypeDef,
        "configureScriptType": ScriptTypeType,
    },
    total=False,
)

ServerReplicationConfigurationOutputTypeDef = TypedDict(
    "ServerReplicationConfigurationOutputTypeDef",
    {
        "server": ServerOutputTypeDef,
        "serverReplicationParameters": ServerReplicationParametersOutputTypeDef,
    },
    total=False,
)

ServerValidationConfigurationOutputTypeDef = TypedDict(
    "ServerValidationConfigurationOutputTypeDef",
    {
        "server": ServerOutputTypeDef,
        "validationId": str,
        "name": str,
        "serverValidationStrategy": Literal["USERDATA"],
        "userDataValidationParameters": UserDataValidationParametersOutputTypeDef,
    },
    total=False,
)

ServerValidationOutputTypeDef = TypedDict(
    "ServerValidationOutputTypeDef",
    {
        "server": ServerOutputTypeDef,
    },
    total=False,
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "roleName": str,
        "clientToken": str,
        "serverGroups": Sequence[ServerGroupTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

UpdateAppRequestRequestTypeDef = TypedDict(
    "UpdateAppRequestRequestTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "roleName": str,
        "serverGroups": Sequence[ServerGroupTypeDef],
        "tags": Sequence[TagTypeDef],
    },
    total=False,
)

ServerGroupLaunchConfigurationTypeDef = TypedDict(
    "ServerGroupLaunchConfigurationTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": Sequence[ServerLaunchConfigurationTypeDef],
    },
    total=False,
)

ServerGroupReplicationConfigurationTypeDef = TypedDict(
    "ServerGroupReplicationConfigurationTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": Sequence[ServerReplicationConfigurationTypeDef],
    },
    total=False,
)

ServerGroupValidationConfigurationTypeDef = TypedDict(
    "ServerGroupValidationConfigurationTypeDef",
    {
        "serverGroupId": str,
        "serverValidationConfigurations": Sequence[ServerValidationConfigurationTypeDef],
    },
    total=False,
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "appSummary": AppSummaryTypeDef,
        "serverGroups": List[ServerGroupOutputTypeDef],
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "appSummary": AppSummaryTypeDef,
        "serverGroups": List[ServerGroupOutputTypeDef],
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "appSummary": AppSummaryTypeDef,
        "serverGroups": List[ServerGroupOutputTypeDef],
        "tags": List[TagOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ServerGroupLaunchConfigurationOutputTypeDef = TypedDict(
    "ServerGroupLaunchConfigurationOutputTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List[ServerLaunchConfigurationOutputTypeDef],
    },
    total=False,
)

ServerGroupReplicationConfigurationOutputTypeDef = TypedDict(
    "ServerGroupReplicationConfigurationOutputTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List[ServerReplicationConfigurationOutputTypeDef],
    },
    total=False,
)

ServerGroupValidationConfigurationOutputTypeDef = TypedDict(
    "ServerGroupValidationConfigurationOutputTypeDef",
    {
        "serverGroupId": str,
        "serverValidationConfigurations": List[ServerValidationConfigurationOutputTypeDef],
    },
    total=False,
)

ValidationOutputTypeDef = TypedDict(
    "ValidationOutputTypeDef",
    {
        "validationId": str,
        "name": str,
        "status": ValidationStatusType,
        "statusMessage": str,
        "latestValidationTime": datetime,
        "appValidationOutput": AppValidationOutputTypeDef,
        "serverValidationOutput": ServerValidationOutputTypeDef,
    },
    total=False,
)

PutAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": Sequence[ServerGroupLaunchConfigurationTypeDef],
    },
    total=False,
)

PutAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
        "serverGroupReplicationConfigurations": Sequence[
            ServerGroupReplicationConfigurationTypeDef
        ],
    },
    total=False,
)

_RequiredPutAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalPutAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutAppValidationConfigurationRequestRequestTypeDef",
    {
        "appValidationConfigurations": Sequence[AppValidationConfigurationTypeDef],
        "serverGroupValidationConfigurations": Sequence[ServerGroupValidationConfigurationTypeDef],
    },
    total=False,
)

class PutAppValidationConfigurationRequestRequestTypeDef(
    _RequiredPutAppValidationConfigurationRequestRequestTypeDef,
    _OptionalPutAppValidationConfigurationRequestRequestTypeDef,
):
    pass

GetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "GetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List[ServerGroupLaunchConfigurationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "GetAppReplicationConfigurationResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List[
            ServerGroupReplicationConfigurationOutputTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAppValidationConfigurationResponseTypeDef = TypedDict(
    "GetAppValidationConfigurationResponseTypeDef",
    {
        "appValidationConfigurations": List[AppValidationConfigurationOutputTypeDef],
        "serverGroupValidationConfigurations": List[
            ServerGroupValidationConfigurationOutputTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAppValidationOutputResponseTypeDef = TypedDict(
    "GetAppValidationOutputResponseTypeDef",
    {
        "validationOutputList": List[ValidationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
