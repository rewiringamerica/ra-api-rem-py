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

from rewiringamerica_rem.models.fuel_rate import FuelRate

class TestFuelRate(unittest.TestCase):
    """FuelRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FuelRate:
        """Test FuelRate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FuelRate`
        """
        model = FuelRate()
        if include_optional:
            return FuelRate(
                value = 1.337,
                unit = '',
                rate_type = 'volumetric'
            )
        else:
            return FuelRate(
                unit = '',
        )
        """

    def testFuelRate(self):
        """Test FuelRate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
