# coding: utf-8

"""
    Residential Electrification Model API

    An API for REM, the Residential Electrification Model.

    The version of the OpenAPI document: 1.0.6
    Contact: datascience@rewiringamerica.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BuildingFeatures(BaseModel):
    """
    A class representing the set of possible building characteristics.  All values default to None, indicating that the given characteristic is unknown for the represented residence. If a characteristic has the string value of \"None\" it indicates that the characteristic, like Air Conditioning or a Pool, is not present at the represented residence.
    """ # noqa: E501
    geometry_floor_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The square footage of the residence.")
    geometry_stories: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of stories in the residence.")
    bedrooms: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of bedrooms contained in the residence.")
    bathrooms: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of bathrooms contained in the residence.")
    vintage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The year in which the residence was built.")
    geometry_attic_type: Optional[List[StrictStr]] = Field(default=None, description="The type of attic.")
    hvac_cooling_type: Optional[List[StrictStr]] = Field(default=None, description="The type of cooling system present in the residence.")
    hvac_heating_type: Optional[List[StrictStr]] = Field(default=None, description="The type of ductwork used for heating in the residence.")
    hvac_heating_type_and_fuel: Optional[List[StrictStr]] = Field(default=None, description="The heating appliance type and fuel in the residence.")
    geometry_garage: Optional[List[StrictStr]] = Field(default=None, description="The size of the garage as measured in the number of cars that can be placed within the garage.")
    misc_pool: Optional[List[StrictStr]] = Field(default=None, description="A string indicating the presence of a pool at the residence.")
    misc_hot_tub_spa: Optional[List[StrictStr]] = Field(default=None, description="The fuel type used to heat a hot tub if one is present at the residence.")
    misc_well_pump: Optional[List[StrictStr]] = Field(default=None, description="The efficiency of a well pump if one is located at the residence.")
    misc_pool_heater: Optional[List[StrictStr]] = Field(default=None, description="The presence and fuel type of a pool heater.")
    geometry_wall_type: Optional[List[StrictStr]] = Field(default=None, description="The material of the exterior walls on the residence.")
    geometry_wall_exterior_finish: Optional[List[StrictStr]] = Field(default=None, description="The finish and color of exterior walls on the residence.")
    roof_material: Optional[List[StrictStr]] = Field(default=None, description="The material of the roof on the residence")
    geometry_building_type_acs: Optional[List[StrictStr]] = Field(default=None, description="The American Community Survey building type of the residence.")
    geometry_building_number_units_sfa: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of units in a single-family attached building.")
    geometry_building_number_units_mf: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of units in a multifamily building.")
    heating_fuel: Optional[List[StrictStr]] = Field(default=None, description="The primary fuel used for heating the residence.")
    __properties: ClassVar[List[str]] = ["geometry_floor_area", "geometry_stories", "bedrooms", "bathrooms", "vintage", "geometry_attic_type", "hvac_cooling_type", "hvac_heating_type", "hvac_heating_type_and_fuel", "geometry_garage", "misc_pool", "misc_hot_tub_spa", "misc_well_pump", "misc_pool_heater", "geometry_wall_type", "geometry_wall_exterior_finish", "roof_material", "geometry_building_type_acs", "geometry_building_number_units_sfa", "geometry_building_number_units_mf", "heating_fuel"]

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
        """Create an instance of BuildingFeatures from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BuildingFeatures from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "geometry_floor_area": obj.get("geometry_floor_area"),
            "geometry_stories": obj.get("geometry_stories"),
            "bedrooms": obj.get("bedrooms"),
            "bathrooms": obj.get("bathrooms"),
            "vintage": obj.get("vintage"),
            "geometry_attic_type": obj.get("geometry_attic_type"),
            "hvac_cooling_type": obj.get("hvac_cooling_type"),
            "hvac_heating_type": obj.get("hvac_heating_type"),
            "hvac_heating_type_and_fuel": obj.get("hvac_heating_type_and_fuel"),
            "geometry_garage": obj.get("geometry_garage"),
            "misc_pool": obj.get("misc_pool"),
            "misc_hot_tub_spa": obj.get("misc_hot_tub_spa"),
            "misc_well_pump": obj.get("misc_well_pump"),
            "misc_pool_heater": obj.get("misc_pool_heater"),
            "geometry_wall_type": obj.get("geometry_wall_type"),
            "geometry_wall_exterior_finish": obj.get("geometry_wall_exterior_finish"),
            "roof_material": obj.get("roof_material"),
            "geometry_building_type_acs": obj.get("geometry_building_type_acs"),
            "geometry_building_number_units_sfa": obj.get("geometry_building_number_units_sfa"),
            "geometry_building_number_units_mf": obj.get("geometry_building_number_units_mf"),
            "heating_fuel": obj.get("heating_fuel")
        })
        return _obj


