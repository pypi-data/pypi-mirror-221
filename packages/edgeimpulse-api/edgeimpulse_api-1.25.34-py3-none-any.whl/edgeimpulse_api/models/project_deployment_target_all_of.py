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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class ProjectDeploymentTargetAllOf(BaseModel):
    recommended_for_project: StrictBool = Field(..., alias="recommendedForProject", description="Whether this deployment target is recommended for the project based on connected devices.")
    disabled_for_project: StrictBool = Field(..., alias="disabledForProject", description="Whether this deployment target is disabled for the project based on various attributes of the project.")
    reason_target_disabled: Optional[StrictStr] = Field(None, alias="reasonTargetDisabled", description="If the deployment target is disabled for the project, this gives the reason why.")
    __properties = ["recommendedForProject", "disabledForProject", "reasonTargetDisabled"]

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
    def from_json(cls, json_str: str) -> ProjectDeploymentTargetAllOf:
        """Create an instance of ProjectDeploymentTargetAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectDeploymentTargetAllOf:
        """Create an instance of ProjectDeploymentTargetAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProjectDeploymentTargetAllOf.construct(**obj)

        _obj = ProjectDeploymentTargetAllOf.construct(**{
            "recommended_for_project": obj.get("recommendedForProject"),
            "disabled_for_project": obj.get("disabledForProject"),
            "reason_target_disabled": obj.get("reasonTargetDisabled")
        })
        return _obj

