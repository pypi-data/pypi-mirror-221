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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class ListApiKeysResponseAllOfApiKeys(BaseModel):
    id: StrictInt = ...
    api_key: StrictStr = Field(..., alias="apiKey")
    is_development_key: StrictBool = Field(..., alias="isDevelopmentKey")
    name: StrictStr = ...
    created: datetime = ...
    role: StrictStr = ...
    __properties = ["id", "apiKey", "isDevelopmentKey", "name", "created", "role"]

    @validator('role')
    def role_validate_enum(cls, v):
        if v not in ('admin', 'readonly', 'ingestiononly'):
            raise ValueError("must validate the enum values ('admin', 'readonly', 'ingestiononly')")
        return v

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
    def from_json(cls, json_str: str) -> ListApiKeysResponseAllOfApiKeys:
        """Create an instance of ListApiKeysResponseAllOfApiKeys from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListApiKeysResponseAllOfApiKeys:
        """Create an instance of ListApiKeysResponseAllOfApiKeys from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ListApiKeysResponseAllOfApiKeys.construct(**obj)

        _obj = ListApiKeysResponseAllOfApiKeys.construct(**{
            "id": obj.get("id"),
            "api_key": obj.get("apiKey"),
            "is_development_key": obj.get("isDevelopmentKey"),
            "name": obj.get("name"),
            "created": obj.get("created"),
            "role": obj.get("role")
        })
        return _obj

