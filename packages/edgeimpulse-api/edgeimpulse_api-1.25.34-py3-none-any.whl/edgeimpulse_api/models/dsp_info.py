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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from edgeimpulse_api.models.dsp_info_features import DSPInfoFeatures
from edgeimpulse_api.models.dsp_info_performance import DSPInfoPerformance

class DSPInfo(BaseModel):
    id: StrictInt = ...
    name: StrictStr = ...
    window_length: StrictInt = Field(..., alias="windowLength")
    type: StrictStr = ...
    classes: List[StrictStr] = ...
    features: DSPInfoFeatures = ...
    expected_window_count: StrictInt = Field(..., alias="expectedWindowCount", description="Expected number of windows that would be generated")
    input_axes: List[StrictStr] = Field(..., alias="inputAxes", description="Axes that this block depends on.")
    performance: Optional[DSPInfoPerformance] = None
    can_calculate_feature_importance: StrictBool = Field(..., alias="canCalculateFeatureImportance")
    calculate_feature_importance: StrictBool = Field(..., alias="calculateFeatureImportance")
    has_auto_tune: Optional[StrictBool] = Field(None, alias="hasAutoTune", description="Whether this type of DSP block supports autotuning.")
    minimum_version_for_autotune: Optional[float] = Field(None, alias="minimumVersionForAutotune", description="For DSP blocks that support autotuning, this value specifies the minimum block implementation version for which autotuning is supported.")
    has_autotuner_results: Optional[StrictBool] = Field(None, alias="hasAutotunerResults", description="Whether autotune results exist for this DSP block.")
    __properties = ["id", "name", "windowLength", "type", "classes", "features", "expectedWindowCount", "inputAxes", "performance", "canCalculateFeatureImportance", "calculateFeatureImportance", "hasAutoTune", "minimumVersionForAutotune", "hasAutotunerResults"]

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
    def from_json(cls, json_str: str) -> DSPInfo:
        """Create an instance of DSPInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of performance
        if self.performance:
            _dict['performance'] = self.performance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DSPInfo:
        """Create an instance of DSPInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DSPInfo.construct(**obj)

        _obj = DSPInfo.construct(**{
            "id": obj.get("id"),
            "name": obj.get("name"),
            "window_length": obj.get("windowLength"),
            "type": obj.get("type"),
            "classes": obj.get("classes"),
            "features": DSPInfoFeatures.from_dict(obj.get("features")) if obj.get("features") is not None else None,
            "expected_window_count": obj.get("expectedWindowCount"),
            "input_axes": obj.get("inputAxes"),
            "performance": DSPInfoPerformance.from_dict(obj.get("performance")) if obj.get("performance") is not None else None,
            "can_calculate_feature_importance": obj.get("canCalculateFeatureImportance"),
            "calculate_feature_importance": obj.get("calculateFeatureImportance"),
            "has_auto_tune": obj.get("hasAutoTune"),
            "minimum_version_for_autotune": obj.get("minimumVersionForAutotune"),
            "has_autotuner_results": obj.get("hasAutotunerResults")
        })
        return _obj

