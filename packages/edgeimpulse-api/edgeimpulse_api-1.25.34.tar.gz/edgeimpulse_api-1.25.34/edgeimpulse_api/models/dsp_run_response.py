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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from edgeimpulse_api.models.dsp_run_graph import DspRunGraph
from edgeimpulse_api.models.dsp_run_response_all_of_performance import DspRunResponseAllOfPerformance

class DspRunResponse(BaseModel):
    success: StrictBool = Field(..., description="Whether the operation succeeded")
    error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
    features: List[float] = Field(..., description="Array of processed features. Laid out according to the names in 'labels'")
    graphs: List[DspRunGraph] = Field(..., description="Graphs to plot to give an insight in how the DSP process ran")
    labels: Optional[List[StrictStr]] = Field(None, description="Labels of the feature axes")
    performance: Optional[DspRunResponseAllOfPerformance] = None
    __properties = ["success", "error", "features", "graphs", "labels", "performance"]

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
    def from_json(cls, json_str: str) -> DspRunResponse:
        """Create an instance of DspRunResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in graphs (list)
        _items = []
        if self.graphs:
            for _item in self.graphs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['graphs'] = _items
        # override the default output from pydantic by calling `to_dict()` of performance
        if self.performance:
            _dict['performance'] = self.performance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DspRunResponse:
        """Create an instance of DspRunResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DspRunResponse.construct(**obj)

        _obj = DspRunResponse.construct(**{
            "success": obj.get("success"),
            "error": obj.get("error"),
            "features": obj.get("features"),
            "graphs": [DspRunGraph.from_dict(_item) for _item in obj.get("graphs")] if obj.get("graphs") is not None else None,
            "labels": obj.get("labels"),
            "performance": DspRunResponseAllOfPerformance.from_dict(obj.get("performance")) if obj.get("performance") is not None else None
        })
        return _obj

