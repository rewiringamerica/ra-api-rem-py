# coding: utf-8

"""
    Residential Electrification Model API

    An API for REM, the Residential Electrification Model.

    The version of the OpenAPI document: 1.3.0
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
from rewiringamerica_rem.models.fuel_rate import FuelRate
from rewiringamerica_rem.models.fuel_savings import FuelSavings
from rewiringamerica_rem.models.quantity import Quantity
from rewiringamerica_rem.models.sampling_details import SamplingDetails
from typing import Optional, Set
from typing_extensions import Self

class Savings(BaseModel):
    """
    Represents the impacts of an upgrade and additional details on how these were computed.  Additional details include the rates, emissions factors and number of samples used to compute the impacts.
    """ # noqa: E501
    fuel_results: Dict[str, FuelSavings] = Field(description="A dictionary of results, one for each fuel type.")
    rates: Dict[str, List[FuelRate]] = Field(description="A dictionary of rates used to compute the cost of consuming each fuel.")
    emissions_factors: Dict[str, Quantity] = Field(description="A dictionary of conversion factors used to compute the emissions from each fuel.")
    sampling_details: SamplingDetails = Field(description="A dictionary describing the number of samples used in the model.")
    __properties: ClassVar[List[str]] = ["fuel_results", "rates", "emissions_factors", "sampling_details"]

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
        """Create an instance of Savings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in fuel_results (dict)
        _field_dict = {}
        if self.fuel_results:
            for _key_fuel_results in self.fuel_results:
                if self.fuel_results[_key_fuel_results]:
                    _field_dict[_key_fuel_results] = self.fuel_results[_key_fuel_results].to_dict()
            _dict['fuel_results'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in rates (dict of array)
        _field_dict_of_array = {}
        if self.rates:
            for _key_rates in self.rates:
                if self.rates[_key_rates] is not None:
                    _field_dict_of_array[_key_rates] = [
                        _item.to_dict() for _item in self.rates[_key_rates]
                    ]
            _dict['rates'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each value in emissions_factors (dict)
        _field_dict = {}
        if self.emissions_factors:
            for _key_emissions_factors in self.emissions_factors:
                if self.emissions_factors[_key_emissions_factors]:
                    _field_dict[_key_emissions_factors] = self.emissions_factors[_key_emissions_factors].to_dict()
            _dict['emissions_factors'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of sampling_details
        if self.sampling_details:
            _dict['sampling_details'] = self.sampling_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Savings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fuel_results": dict(
                (_k, FuelSavings.from_dict(_v))
                for _k, _v in obj["fuel_results"].items()
            )
            if obj.get("fuel_results") is not None
            else None,
            "rates": dict(
                (_k,
                        [FuelRate.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("rates", {}).items()
            ),
            "emissions_factors": dict(
                (_k, Quantity.from_dict(_v))
                for _k, _v in obj["emissions_factors"].items()
            )
            if obj.get("emissions_factors") is not None
            else None,
            "sampling_details": SamplingDetails.from_dict(obj["sampling_details"]) if obj.get("sampling_details") is not None else None
        })
        return _obj


