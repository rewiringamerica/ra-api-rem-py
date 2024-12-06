# coding: utf-8

"""
    Dohyo

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class HeatingFuel(str, Enum):
    """
    Heating fuels supported by the API.  Note that we do not currently support \"Other Fuel\" or \"None\".
    """

    """
    allowed enum values
    """
    ELECTRICITY = 'Electricity'
    FUEL_OIL = 'Fuel Oil'
    NATURAL_GAS = 'Natural Gas'
    PROPANE = 'Propane'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HeatingFuel from a JSON string"""
        return cls(json.loads(json_str))

