# coding: utf-8

# flake8: noqa
"""
    Residential Electrification Model API

    An API for REM, the Residential Electrification Model.         The other Rewiring America APIs and methodology for REM are [here](https://api.rewiringamerica.org/).

    The version of the OpenAPI document: 0.1.0
    Contact: datascience@rewiringamerica.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from rem.models.building_features import BuildingFeatures
from rem.models.building_profile import BuildingProfile
from rem.models.fuel_rate import FuelRate
from rem.models.fuel_savings import FuelSavings
from rem.models.http_validation_error import HTTPValidationError
from rem.models.heating_fuel_input import HeatingFuelInput
from rem.models.heating_fuel_output import HeatingFuelOutput
from rem.models.impact_metric import ImpactMetric
from rem.models.metric_statistics import MetricStatistics
from rem.models.quantity import Quantity
from rem.models.rem_profile_request import RemProfileRequest
from rem.models.result_fuel_type import ResultFuelType
from rem.models.savings import Savings
from rem.models.supported_upgrade import SupportedUpgrade
from rem.models.validation_error import ValidationError
from rem.models.validation_error_loc_inner import ValidationErrorLocInner