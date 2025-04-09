# coding: utf-8

"""
    Residential Electrification Model API

    An API for REM, the Residential Electrification Model.

    The version of the OpenAPI document: 1.3.0
    Contact: datascience@rewiringamerica.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from rewiringamerica_rem.models.rem_profile_request import RemProfileRequest

class TestRemProfileRequest(unittest.TestCase):
    """RemProfileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemProfileRequest:
        """Test RemProfileRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemProfileRequest`
        """
        model = RemProfileRequest()
        if include_optional:
            return RemProfileRequest(
                upgrade = hvac__heat_pump_seer18_hspf10,
                heating_fuel = natural_gas,
                water_heater_fuel = 'electricity',
                building_profile = rewiringamerica_rem.models.building_profile.BuildingProfile(
                    county = 'G1700310', 
                    puma = 'G17003159', 
                    ashrae_iecc_climate_zone_2004 = '4A', 
                    weather_file_city = 'Chicago Midway Ap', 
                    state = 'IL', 
                    building_features = {geometry_floor_area=1000, heating_fuel=[Natural Gas]}, )
            )
        else:
            return RemProfileRequest(
                upgrade = hvac__heat_pump_seer18_hspf10,
                heating_fuel = natural_gas,
                building_profile = rewiringamerica_rem.models.building_profile.BuildingProfile(
                    county = 'G1700310', 
                    puma = 'G17003159', 
                    ashrae_iecc_climate_zone_2004 = '4A', 
                    weather_file_city = 'Chicago Midway Ap', 
                    state = 'IL', 
                    building_features = {geometry_floor_area=1000, heating_fuel=[Natural Gas]}, ),
        )
        """

    def testRemProfileRequest(self):
        """Test RemProfileRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
