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
import json
from enum import Enum
from typing_extensions import Self


class HeatingFuelInput(str, Enum):
    """
    Heating fuels supported by the API.  Note that we do not currently support \"Other Fuel\" or \"None\".
    """

    """
    allowed enum values
    """
    ELECTRICITY = 'electricity'
    FUEL_OIL = 'fuel_oil'
    NATURAL_GAS = 'natural_gas'
    PROPANE = 'propane'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HeatingFuelInput from a JSON string"""
        return cls(json.loads(json_str))


