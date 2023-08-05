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
from edgeimpulse_api.models.start_performance_calibration_request import StartPerformanceCalibrationRequest

class GetPerformanceCalibrationStatusResponse(BaseModel):
    success: StrictBool = Field(..., description="Whether the operation succeeded")
    error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
    available: StrictBool = ...
    unsupported_project_error: Optional[StrictStr] = Field(None, alias="unsupportedProjectError", description="If the current project is unsupported by performance calibration, this field explains the reason why. Otherwise, it is undefined.")
    options: Optional[StartPerformanceCalibrationRequest] = None
    __properties = ["success", "error", "available", "unsupportedProjectError", "options"]

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
    def from_json(cls, json_str: str) -> GetPerformanceCalibrationStatusResponse:
        """Create an instance of GetPerformanceCalibrationStatusResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetPerformanceCalibrationStatusResponse:
        """Create an instance of GetPerformanceCalibrationStatusResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetPerformanceCalibrationStatusResponse.construct(**obj)

        _obj = GetPerformanceCalibrationStatusResponse.construct(**{
            "success": obj.get("success"),
            "error": obj.get("error"),
            "available": obj.get("available"),
            "unsupported_project_error": obj.get("unsupportedProjectError"),
            "options": StartPerformanceCalibrationRequest.from_dict(obj.get("options")) if obj.get("options") is not None else None
        })
        return _obj

