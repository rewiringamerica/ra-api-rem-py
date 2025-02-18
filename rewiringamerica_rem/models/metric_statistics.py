# coding: utf-8

"""
    Residential Electrification Model API

    An API for REM, the Residential Electrification Model.

    The version of the OpenAPI document: 0.4.6
    Contact: datascience@rewiringamerica.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from rewiringamerica_rem.models.quantity import Quantity
from typing import Optional, Set
from typing_extensions import Self

class MetricStatistics(BaseModel):
    """
    Represents a statistic associated with a particular fuel and type of impact.  These statistics are computed are over the set of sample homes in the Monte Carlo simulation.
    """ # noqa: E501
    mean: Quantity = Field(description="The mean statistic.")
    median: Quantity = Field(description="The median statistic.")
    percentile_20: Quantity = Field(description="The 20th percentile statistic.")
    percentile_80: Quantity = Field(description="The 80th percentile statistic.")
    __properties: ClassVar[List[str]] = ["mean", "median", "percentile_20", "percentile_80"]

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
        """Create an instance of MetricStatistics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of mean
        if self.mean:
            _dict['mean'] = self.mean.to_dict()
        # override the default output from pydantic by calling `to_dict()` of median
        if self.median:
            _dict['median'] = self.median.to_dict()
        # override the default output from pydantic by calling `to_dict()` of percentile_20
        if self.percentile_20:
            _dict['percentile_20'] = self.percentile_20.to_dict()
        # override the default output from pydantic by calling `to_dict()` of percentile_80
        if self.percentile_80:
            _dict['percentile_80'] = self.percentile_80.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetricStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mean": Quantity.from_dict(obj["mean"]) if obj.get("mean") is not None else None,
            "median": Quantity.from_dict(obj["median"]) if obj.get("median") is not None else None,
            "percentile_20": Quantity.from_dict(obj["percentile_20"]) if obj.get("percentile_20") is not None else None,
            "percentile_80": Quantity.from_dict(obj["percentile_80"]) if obj.get("percentile_80") is not None else None
        })
        return _obj


