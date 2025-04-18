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

from rewiringamerica_rem.models.metric_statistics import MetricStatistics

class TestMetricStatistics(unittest.TestCase):
    """MetricStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricStatistics:
        """Test MetricStatistics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricStatistics`
        """
        model = MetricStatistics()
        if include_optional:
            return MetricStatistics(
                mean = rewiringamerica_rem.models.quantity.Quantity(
                    value = 1.337, 
                    unit = '', ),
                median = rewiringamerica_rem.models.quantity.Quantity(
                    value = 1.337, 
                    unit = '', ),
                percentile_20 = rewiringamerica_rem.models.quantity.Quantity(
                    value = 1.337, 
                    unit = '', ),
                percentile_80 = rewiringamerica_rem.models.quantity.Quantity(
                    value = 1.337, 
                    unit = '', )
            )
        else:
            return MetricStatistics(
                mean = rewiringamerica_rem.models.quantity.Quantity(
                    value = 1.337, 
                    unit = '', ),
                median = rewiringamerica_rem.models.quantity.Quantity(
                    value = 1.337, 
                    unit = '', ),
                percentile_20 = rewiringamerica_rem.models.quantity.Quantity(
                    value = 1.337, 
                    unit = '', ),
                percentile_80 = rewiringamerica_rem.models.quantity.Quantity(
                    value = 1.337, 
                    unit = '', ),
        )
        """

    def testMetricStatistics(self):
        """Test MetricStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
