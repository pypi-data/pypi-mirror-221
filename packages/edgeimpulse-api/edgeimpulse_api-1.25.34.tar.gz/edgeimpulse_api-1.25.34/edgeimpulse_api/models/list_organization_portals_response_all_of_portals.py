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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class ListOrganizationPortalsResponseAllOfPortals(BaseModel):
    id: StrictInt = ...
    name: StrictStr = ...
    description: Optional[StrictStr] = None
    url: StrictStr = ...
    bucket_name: StrictStr = Field(..., alias="bucketName")
    bucket_path: StrictStr = Field(..., alias="bucketPath")
    bucket_url: StrictStr = Field(..., alias="bucketUrl")
    created: datetime = ...
    __properties = ["id", "name", "description", "url", "bucketName", "bucketPath", "bucketUrl", "created"]

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
    def from_json(cls, json_str: str) -> ListOrganizationPortalsResponseAllOfPortals:
        """Create an instance of ListOrganizationPortalsResponseAllOfPortals from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListOrganizationPortalsResponseAllOfPortals:
        """Create an instance of ListOrganizationPortalsResponseAllOfPortals from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ListOrganizationPortalsResponseAllOfPortals.construct(**obj)

        _obj = ListOrganizationPortalsResponseAllOfPortals.construct(**{
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "bucket_name": obj.get("bucketName"),
            "bucket_path": obj.get("bucketPath"),
            "bucket_url": obj.get("bucketUrl"),
            "created": obj.get("created")
        })
        return _obj

