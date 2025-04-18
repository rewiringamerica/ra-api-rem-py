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
import json
from enum import Enum
from typing_extensions import Self


class SupportedUpgrade(str, Enum):
    """
    Upgrades accepted by the REM API.
    """

    """
    allowed enum values
    """
    BASELINE = 'baseline'
    WEATHERIZATION__INSULATION_AIR_DUCT_SEALING = 'weatherization__insulation_air_duct_sealing'
    HVAC__HEAT_PUMP_SEER15_HSPF9 = 'hvac__heat_pump_seer15_hspf9'
    HVAC__HEAT_PUMP_SEER24_HSPF13 = 'hvac__heat_pump_seer24_hspf13'
    WATER_HEATER__HEAT_PUMP_UEF3_DOT_35 = 'water_heater__heat_pump_uef3.35'
    COMBINATION__ALL_ELECTRIC__HVAC_SEER24_HSPF13__WEATHERIZATION = 'combination__all_electric__hvac_seer24_hspf13__weatherization'
    HVAC__HEAT_PUMP_SEER18_HSPF10 = 'hvac__heat_pump_seer18_hspf10'
    COMBINATION__HVAC_SEER18_HSPF10__WEATHERIZATION = 'combination__hvac_seer18_hspf10__weatherization'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SupportedUpgrade from a JSON string"""
        return cls(json.loads(json_str))


