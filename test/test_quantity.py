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

from rewiringamerica_rem.models.quantity import Quantity

class TestQuantity(unittest.TestCase):
    """Quantity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Quantity:
        """Test Quantity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Quantity`
        """
        model = Quantity()
        if include_optional:
            return Quantity(
                value = 1.337,
                units = ''
            )
        else:
            return Quantity(
                units = '',
        )
        """

    def testQuantity(self):
        """Test Quantity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
