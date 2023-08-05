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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class CreateProjectRequest(BaseModel):
    project_name: StrictStr = Field(..., alias="projectName", description="The name of the first project.")
    original_project_version_id: Optional[StrictInt] = Field(None, alias="originalProjectVersionId", description="The ID of the version that was used to restore this project.")
    __properties = ["projectName", "originalProjectVersionId"]

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
    def from_json(cls, json_str: str) -> CreateProjectRequest:
        """Create an instance of CreateProjectRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateProjectRequest:
        """Create an instance of CreateProjectRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateProjectRequest.construct(**obj)

        _obj = CreateProjectRequest.construct(**{
            "project_name": obj.get("projectName"),
            "original_project_version_id": obj.get("originalProjectVersionId")
        })
        return _obj

