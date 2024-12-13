# coding: utf-8

"""
    Residential Electrification Model API

    An API for REM, the Residential Electrification Model.         The other Rewiring America APIs and methodology for REM are [here](https://api.rewiringamerica.org/).

    The version of the OpenAPI document: 0.1.0
    Contact: datascience@rewiringamerica.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from rem.models.building_features import BuildingFeatures

class TestBuildingFeatures(unittest.TestCase):
    """BuildingFeatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuildingFeatures:
        """Test BuildingFeatures
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuildingFeatures`
        """
        model = BuildingFeatures()
        if include_optional:
            return BuildingFeatures(
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
                    ]
            )
        else:
            return BuildingFeatures(
        )
        """

    def testBuildingFeatures(self):
        """Test BuildingFeatures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
