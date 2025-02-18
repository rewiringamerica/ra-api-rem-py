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
from rewiringamerica_rem.models.building_profile import BuildingProfile
from rewiringamerica_rem.models.heating_fuel import HeatingFuel
from rewiringamerica_rem.models.supported_upgrade import SupportedUpgrade
from typing import Optional, Set
from typing_extensions import Self

class RemProfileRequest(BaseModel):
    """
    A class representing the request body used to retrieve a building's profile.
    """ # noqa: E501
    upgrade: SupportedUpgrade = Field(description="The upgrade whose effects we want to analyze.")
    heating_fuel: HeatingFuel = Field(description="The heating fuel used in the home before the upgrade.")
    building_profile: BuildingProfile = Field(description="The known geographic features and building characteristics for a given residence.")
    __properties: ClassVar[List[str]] = ["upgrade", "heating_fuel", "building_profile"]

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
        """Create an instance of RemProfileRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of building_profile
        if self.building_profile:
            _dict['building_profile'] = self.building_profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RemProfileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "upgrade": obj.get("upgrade"),
            "heating_fuel": obj.get("heating_fuel"),
            "building_profile": BuildingProfile.from_dict(obj["building_profile"]) if obj.get("building_profile") is not None else None
        })
        return _obj


