# coding: utf-8

"""
    Residential Electrification Model API

    An API for REM, the Residential Electrification Model.         The other Rewiring America APIs and methodology for REM are [here](https://api.rewiringamerica.org/).

    The version of the OpenAPI document: 0.1.0
    Contact: datascience@rewiringamerica.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from rewiringamerica_rem.models.impact_metric import ImpactMetric
from typing import Optional, Set
from typing_extensions import Self

class FuelSavings(BaseModel):
    """
    A class to represent savings data for a particular fuel.  Attributes ----------     baseline (FuelMetrics): The data if no upgrade is passed into the surrogate model.     upgrade (FuelMetrics): The data if an upgrade is passed into the surrogate model.     delta (FuelMetrics): The deltas if an upgrade is passed into the surrogate model.
    """ # noqa: E501
    baseline: ImpactMetric
    upgrade: ImpactMetric
    delta: ImpactMetric
    __properties: ClassVar[List[str]] = ["baseline", "upgrade", "delta"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FuelSavings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of baseline
        if self.baseline:
            _dict['baseline'] = self.baseline.to_dict()
        # override the default output from pydantic by calling `to_dict()` of upgrade
        if self.upgrade:
            _dict['upgrade'] = self.upgrade.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delta
        if self.delta:
            _dict['delta'] = self.delta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FuelSavings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "baseline": ImpactMetric.from_dict(obj["baseline"]) if obj.get("baseline") is not None else None,
            "upgrade": ImpactMetric.from_dict(obj["upgrade"]) if obj.get("upgrade") is not None else None,
            "delta": ImpactMetric.from_dict(obj["delta"]) if obj.get("delta") is not None else None
        })
        return _obj


