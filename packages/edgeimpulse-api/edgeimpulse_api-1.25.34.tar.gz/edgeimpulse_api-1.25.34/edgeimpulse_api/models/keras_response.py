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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator
from edgeimpulse_api.models.akida_edge_learning_config import AkidaEdgeLearningConfig
from edgeimpulse_api.models.augmentation_policy_image_enum import AugmentationPolicyImageEnum
from edgeimpulse_api.models.augmentation_policy_spectrogram import AugmentationPolicySpectrogram
from edgeimpulse_api.models.dependency_data import DependencyData
from edgeimpulse_api.models.keras_model_type_enum import KerasModelTypeEnum
from edgeimpulse_api.models.keras_visual_layer import KerasVisualLayer
from edgeimpulse_api.models.learn_block_type import LearnBlockType
from edgeimpulse_api.models.transfer_learning_model import TransferLearningModel

class KerasResponse(BaseModel):
    success: StrictBool = Field(..., description="Whether the operation succeeded")
    error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
    dependencies: DependencyData = ...
    trained: StrictBool = Field(..., description="Whether the block is trained")
    name: StrictStr = ...
    type: Optional[LearnBlockType] = None
    script: StrictStr = Field(..., description="The Keras script. This script might be empty if the mode is visual.")
    minimum_confidence_rating: float = Field(..., alias="minimumConfidenceRating", description="Minimum confidence rating required for the neural network. Scores below this confidence are tagged as uncertain.")
    selected_model_type: KerasModelTypeEnum = Field(..., alias="selectedModelType")
    mode: StrictStr = Field(..., description="The mode (visual or expert) to use for editing this network.")
    visual_layers: List[KerasVisualLayer] = Field(..., alias="visualLayers", description="The visual layers (if in visual mode) for the neural network. This will be an empty array when in expert mode.")
    training_cycles: StrictInt = Field(..., alias="trainingCycles", description="Number of training cycles. If in expert mode this will be 0.")
    learning_rate: float = Field(..., alias="learningRate", description="Learning rate (between 0 and 1). If in expert mode this will be 0.")
    shape: StrictStr = Field(..., description="Python-formatted tuple of input axes")
    train_test_split: Optional[float] = Field(None, alias="trainTestSplit", description="Train/test split (between 0 and 1)")
    auto_class_weights: Optional[StrictBool] = Field(None, alias="autoClassWeights", description="Whether to automatically balance class weights, use this for skewed datasets.")
    find_learning_rate: Optional[StrictBool] = Field(None, alias="findLearningRate", description="Automatically select the optimal learning rate for your data set.")
    augmentation_policy_image: AugmentationPolicyImageEnum = Field(..., alias="augmentationPolicyImage")
    augmentation_policy_spectrogram: Optional[AugmentationPolicySpectrogram] = Field(None, alias="augmentationPolicySpectrogram")
    transfer_learning_models: List[TransferLearningModel] = Field(..., alias="transferLearningModels")
    profile_int8: StrictBool = Field(..., alias="profileInt8", description="Whether to profile the i8 model (might take a very long time)")
    skip_embeddings_and_memory: StrictBool = Field(..., alias="skipEmbeddingsAndMemory", description="If set, skips creating embeddings and measuring memory (used in tests)")
    akida_edge_learning_config: Optional[AkidaEdgeLearningConfig] = Field(None, alias="akidaEdgeLearningConfig")
    custom_validation_metadata_key: Optional[StrictStr] = Field(None, alias="customValidationMetadataKey", description="This metadata key is used to prevent group data leakage between train and validation datasets.")
    show_advanced_training_settings: StrictBool = Field(..., alias="showAdvancedTrainingSettings", description="Whether the 'Advanced training settings' UI element should be expanded.")
    custom_parameters: Optional[Dict[str, StrictStr]] = Field(None, alias="customParameters", description="Training parameters, this list depends on the list of parameters that the model exposes.")
    __properties = ["success", "error", "dependencies", "trained", "name", "type", "script", "minimumConfidenceRating", "selectedModelType", "mode", "visualLayers", "trainingCycles", "learningRate", "shape", "trainTestSplit", "autoClassWeights", "findLearningRate", "augmentationPolicyImage", "augmentationPolicySpectrogram", "transferLearningModels", "profileInt8", "skipEmbeddingsAndMemory", "akidaEdgeLearningConfig", "customValidationMetadataKey", "showAdvancedTrainingSettings", "customParameters"]

    @validator('mode')
    def mode_validate_enum(cls, v):
        if v not in ('visual', 'expert'):
            raise ValueError("must validate the enum values ('visual', 'expert')")
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
    def from_json(cls, json_str: str) -> KerasResponse:
        """Create an instance of KerasResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of dependencies
        if self.dependencies:
            _dict['dependencies'] = self.dependencies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in visual_layers (list)
        _items = []
        if self.visual_layers:
            for _item in self.visual_layers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['visualLayers'] = _items
        # override the default output from pydantic by calling `to_dict()` of augmentation_policy_spectrogram
        if self.augmentation_policy_spectrogram:
            _dict['augmentationPolicySpectrogram'] = self.augmentation_policy_spectrogram.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in transfer_learning_models (list)
        _items = []
        if self.transfer_learning_models:
            for _item in self.transfer_learning_models:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transferLearningModels'] = _items
        # override the default output from pydantic by calling `to_dict()` of akida_edge_learning_config
        if self.akida_edge_learning_config:
            _dict['akidaEdgeLearningConfig'] = self.akida_edge_learning_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> KerasResponse:
        """Create an instance of KerasResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return KerasResponse.construct(**obj)

        _obj = KerasResponse.construct(**{
            "success": obj.get("success"),
            "error": obj.get("error"),
            "dependencies": DependencyData.from_dict(obj.get("dependencies")) if obj.get("dependencies") is not None else None,
            "trained": obj.get("trained"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "script": obj.get("script"),
            "minimum_confidence_rating": obj.get("minimumConfidenceRating"),
            "selected_model_type": obj.get("selectedModelType"),
            "mode": obj.get("mode"),
            "visual_layers": [KerasVisualLayer.from_dict(_item) for _item in obj.get("visualLayers")] if obj.get("visualLayers") is not None else None,
            "training_cycles": obj.get("trainingCycles"),
            "learning_rate": obj.get("learningRate"),
            "shape": obj.get("shape"),
            "train_test_split": obj.get("trainTestSplit"),
            "auto_class_weights": obj.get("autoClassWeights"),
            "find_learning_rate": obj.get("findLearningRate"),
            "augmentation_policy_image": obj.get("augmentationPolicyImage"),
            "augmentation_policy_spectrogram": AugmentationPolicySpectrogram.from_dict(obj.get("augmentationPolicySpectrogram")) if obj.get("augmentationPolicySpectrogram") is not None else None,
            "transfer_learning_models": [TransferLearningModel.from_dict(_item) for _item in obj.get("transferLearningModels")] if obj.get("transferLearningModels") is not None else None,
            "profile_int8": obj.get("profileInt8"),
            "skip_embeddings_and_memory": obj.get("skipEmbeddingsAndMemory"),
            "akida_edge_learning_config": AkidaEdgeLearningConfig.from_dict(obj.get("akidaEdgeLearningConfig")) if obj.get("akidaEdgeLearningConfig") is not None else None,
            "custom_validation_metadata_key": obj.get("customValidationMetadataKey"),
            "show_advanced_training_settings": obj.get("showAdvancedTrainingSettings"),
            "custom_parameters": obj.get("customParameters")
        })
        return _obj

