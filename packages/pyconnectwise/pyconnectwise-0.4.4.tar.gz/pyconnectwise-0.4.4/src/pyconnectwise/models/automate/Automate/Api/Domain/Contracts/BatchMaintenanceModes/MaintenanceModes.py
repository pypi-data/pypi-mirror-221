
from __future__ import annotations
from datetime import datetime
from enum import Enum
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class EntityType(Enum):
    SYSTEM = 'System'
    COMPUTER = 'Computer'
    SITE = 'Site'
    COMPANY = 'Company'
    PROBE = 'Probe'
    NETWORK_DEVICE = 'NetworkDevice'
    TICKET = 'Ticket'
    GROUP = 'Group'
    MOBILE_DEVICE = 'MobileDevice'
    VENDOR = 'Vendor'
    VENDOR_PRODUCT = 'VendorProduct'
    POSSIBILITY = 'Possibility'
    OPPORTUNITY = 'Opportunity'
    CONTACT = 'Contact'
    USER = 'User'
    SCRIPT = 'Script'
    PLUGIN = 'Plugin'
    SERVICE = 'Service'
    SERVICE_BUNDLE = 'ServiceBundle'
    SEARCH = 'Search'
    SEARCH_FOLDER = 'SearchFolder'
    DATAVIEW = 'Dataview'
    DATAVIEW_FOLDER = 'DataviewFolder'
    USER_FOLDER = 'UserFolder'
    USER_CLASS = 'UserClass'
    SCRIPT_FOLDER = 'ScriptFolder'
    REMOTE_MONITOR_TEMPLATE = 'RemoteMonitorTemplate'
    EXTRA_FIELD = 'ExtraField'

class MaintenanceModeQueueBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    entity_type: (EntityType | None) = Field(default=None, alias='EntityType')
    entity_ids: (list[int] | None) = Field(default=None, alias='EntityIds')
    start_date: (datetime | None) = Field(default=None, alias='StartDate')
    duration_in_minutes: (int | None) = Field(default=None, alias='DurationInMinutes')
    mode: (str | None) = Field(default=None, alias='Mode')
    comments: (str | None) = Field(default=None, alias='Comments')
