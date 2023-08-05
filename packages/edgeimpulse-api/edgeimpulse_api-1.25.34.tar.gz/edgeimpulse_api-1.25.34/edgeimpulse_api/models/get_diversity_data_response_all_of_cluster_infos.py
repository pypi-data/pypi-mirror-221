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
from pydantic import BaseModel, Field, StrictInt
from edgeimpulse_api.models.sample import Sample

class GetDiversityDataResponseAllOfClusterInfos(BaseModel):
    idx: StrictInt = Field(..., description="Unique index of the cluster")
    indexes: List[StrictInt] = Field(..., description="Indexes of all windows contained in the cluster (for debugging)")
    windows: List[List[StrictInt]] = Field(..., description="The sample ID of every window in the cluster")
    samples: Optional[List[Sample]] = Field(None, description="Details of every sample in the cluster")
    vendi_score: float = Field(..., alias="vendiScore", description="Raw vendi score")
    vendi_ratio: float = Field(..., alias="vendiRatio", description="Vendi score expressed as ratio from 0 to 1")
    count: StrictInt = Field(..., description="The number if windows in the cluster")
    distance: float = Field(..., description="The distance of the cluster from the origin")
    left_idx: Optional[StrictInt] = Field(..., alias="leftIdx", description="The cluster id on the left branch of the dendrogram")
    right_idx: Optional[StrictInt] = Field(..., alias="rightIdx", description="The cluster id on the right branch of the dendrogram")
    __properties = ["idx", "indexes", "windows", "samples", "vendiScore", "vendiRatio", "count", "distance", "leftIdx", "rightIdx"]

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
    def from_json(cls, json_str: str) -> GetDiversityDataResponseAllOfClusterInfos:
        """Create an instance of GetDiversityDataResponseAllOfClusterInfos from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in samples (list)
        _items = []
        if self.samples:
            for _item in self.samples:
                if _item:
                    _items.append(_item.to_dict())
            _dict['samples'] = _items
        # set to None if left_idx (nullable) is None
        if self.left_idx is None:
            _dict['leftIdx'] = None

        # set to None if right_idx (nullable) is None
        if self.right_idx is None:
            _dict['rightIdx'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetDiversityDataResponseAllOfClusterInfos:
        """Create an instance of GetDiversityDataResponseAllOfClusterInfos from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetDiversityDataResponseAllOfClusterInfos.construct(**obj)

        _obj = GetDiversityDataResponseAllOfClusterInfos.construct(**{
            "idx": obj.get("idx"),
            "indexes": obj.get("indexes"),
            "windows": obj.get("windows"),
            "samples": [Sample.from_dict(_item) for _item in obj.get("samples")] if obj.get("samples") is not None else None,
            "vendi_score": obj.get("vendiScore"),
            "vendi_ratio": obj.get("vendiRatio"),
            "count": obj.get("count"),
            "distance": obj.get("distance"),
            "left_idx": obj.get("leftIdx"),
            "right_idx": obj.get("rightIdx")
        })
        return _obj

