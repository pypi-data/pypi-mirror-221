# coding: utf-8

"""
    Edge Impulse API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from edgeimpulse_api.models.data_campaign_link import DataCampaignLink
from edgeimpulse_api.models.data_campaign_query import DataCampaignQuery

class DataCampaign(BaseModel):
    id: StrictInt = ...
    data_campaign_dashboard_id: StrictInt = Field(..., alias="dataCampaignDashboardId")
    created: datetime = ...
    name: StrictStr = ...
    description: StrictStr = ...
    coordinator_uids: List[StrictInt] = Field(..., alias="coordinatorUids", description="List of user IDs that coordinate this campaign")
    logo: Optional[StrictStr] = None
    queries: List[DataCampaignQuery] = ...
    links: List[DataCampaignLink] = ...
    datasets: List[StrictStr] = ...
    pipeline_ids: List[StrictInt] = Field(..., alias="pipelineIds")
    project_ids: List[StrictInt] = Field(..., alias="projectIds")
    __properties = ["id", "dataCampaignDashboardId", "created", "name", "description", "coordinatorUids", "logo", "queries", "links", "datasets", "pipelineIds", "projectIds"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = False

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DataCampaign:
        """Create an instance of DataCampaign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in queries (list)
        _items = []
        if self.queries:
            for _item in self.queries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['queries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataCampaign:
        """Create an instance of DataCampaign from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DataCampaign.construct(**obj)

        _obj = DataCampaign.construct(**{
            "id": obj.get("id"),
            "data_campaign_dashboard_id": obj.get("dataCampaignDashboardId"),
            "created": obj.get("created"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "coordinator_uids": obj.get("coordinatorUids"),
            "logo": obj.get("logo"),
            "queries": [DataCampaignQuery.from_dict(_item) for _item in obj.get("queries")] if obj.get("queries") is not None else None,
            "links": [DataCampaignLink.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "datasets": obj.get("datasets"),
            "pipeline_ids": obj.get("pipelineIds"),
            "project_ids": obj.get("projectIds")
        })
        return _obj

