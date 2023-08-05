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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt
from edgeimpulse_api.models.job_state import JobState

class JobDetailsAllOf(BaseModel):
    children_ids: Optional[List[StrictInt]] = Field(None, alias="childrenIds", description="List of jobs children isd triggered by this job")
    states: List[JobState] = Field(..., description="List of states the job went through")
    spec: Optional[Dict[str, Any]] = Field(None, description="Job specification (Kubernetes specification or other underlying engine)")
    __properties = ["childrenIds", "states", "spec"]

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
    def from_json(cls, json_str: str) -> JobDetailsAllOf:
        """Create an instance of JobDetailsAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in states (list)
        _items = []
        if self.states:
            for _item in self.states:
                if _item:
                    _items.append(_item.to_dict())
            _dict['states'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobDetailsAllOf:
        """Create an instance of JobDetailsAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return JobDetailsAllOf.construct(**obj)

        _obj = JobDetailsAllOf.construct(**{
            "children_ids": obj.get("childrenIds"),
            "states": [JobState.from_dict(_item) for _item in obj.get("states")] if obj.get("states") is not None else None,
            "spec": obj.get("spec")
        })
        return _obj

