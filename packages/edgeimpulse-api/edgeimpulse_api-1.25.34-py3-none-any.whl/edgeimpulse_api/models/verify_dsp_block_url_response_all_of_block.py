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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class VerifyDspBlockUrlResponseAllOfBlock(BaseModel):
    title: StrictStr = ...
    author: StrictStr = ...
    description: StrictStr = ...
    name: StrictStr = ...
    latest_implementation_version: StrictInt = Field(..., alias="latestImplementationVersion")
    __properties = ["title", "author", "description", "name", "latestImplementationVersion"]

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
    def from_json(cls, json_str: str) -> VerifyDspBlockUrlResponseAllOfBlock:
        """Create an instance of VerifyDspBlockUrlResponseAllOfBlock from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyDspBlockUrlResponseAllOfBlock:
        """Create an instance of VerifyDspBlockUrlResponseAllOfBlock from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return VerifyDspBlockUrlResponseAllOfBlock.construct(**obj)

        _obj = VerifyDspBlockUrlResponseAllOfBlock.construct(**{
            "title": obj.get("title"),
            "author": obj.get("author"),
            "description": obj.get("description"),
            "name": obj.get("name"),
            "latest_implementation_version": obj.get("latestImplementationVersion")
        })
        return _obj

