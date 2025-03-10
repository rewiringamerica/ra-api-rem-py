# coding: utf-8

"""
    Residential Electrification Model API

    An API for REM, the Residential Electrification Model.

    The version of the OpenAPI document: 1.0.6
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
                building_profile = rewiringamerica_rem.models.building_profile.BuildingProfile(
                    county = 'G1700310', 
                    puma = 'G17003159', 
                    ashrae_iecc_climate_zone_2004 = '4A', 
                    weather_file_city = 'Chicago Midway Ap', 
                    state = 'IL', 
                    building_features = rewiringamerica_rem.models.building_features.BuildingFeatures(
                        geometry_floor_area = 1.337, 
                        geometry_stories = 1.337, 
                        bedrooms = 1.337, 
                        bathrooms = 1.337, 
                        vintage = 1.337, 
                        geometry_attic_type = [
                            ''
                            ], 
                        hvac_cooling_type = [
                            ''
                            ], 
                        hvac_heating_type = [
                            ''
                            ], 
                        hvac_heating_type_and_fuel = [
                            ''
                            ], 
                        geometry_garage = [
                            ''
                            ], 
                        misc_pool = [
                            ''
                            ], 
                        misc_hot_tub_spa = [
                            ''
                            ], 
                        misc_well_pump = [
                            ''
                            ], 
                        misc_pool_heater = [
                            ''
                            ], 
                        geometry_wall_type = [
                            ''
                            ], 
                        geometry_wall_exterior_finish = [
                            ''
                            ], 
                        roof_material = [
                            ''
                            ], 
                        geometry_building_type_acs = [
                            ''
                            ], 
                        geometry_building_number_units_sfa = 1.337, 
                        geometry_building_number_units_mf = 1.337, 
                        heating_fuel = [
                            ''
                            ], ), )
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
                    building_features = rewiringamerica_rem.models.building_features.BuildingFeatures(
                        geometry_floor_area = 1.337, 
                        geometry_stories = 1.337, 
                        bedrooms = 1.337, 
                        bathrooms = 1.337, 
                        vintage = 1.337, 
                        geometry_attic_type = [
                            ''
                            ], 
                        hvac_cooling_type = [
                            ''
                            ], 
                        hvac_heating_type = [
                            ''
                            ], 
                        hvac_heating_type_and_fuel = [
                            ''
                            ], 
                        geometry_garage = [
                            ''
                            ], 
                        misc_pool = [
                            ''
                            ], 
                        misc_hot_tub_spa = [
                            ''
                            ], 
                        misc_well_pump = [
                            ''
                            ], 
                        misc_pool_heater = [
                            ''
                            ], 
                        geometry_wall_type = [
                            ''
                            ], 
                        geometry_wall_exterior_finish = [
                            ''
                            ], 
                        roof_material = [
                            ''
                            ], 
                        geometry_building_type_acs = [
                            ''
                            ], 
                        geometry_building_number_units_sfa = 1.337, 
                        geometry_building_number_units_mf = 1.337, 
                        heating_fuel = [
                            ''
                            ], ), ),
        )
        """

    def testRemProfileRequest(self):
        """Test RemProfileRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
