# FuelDataRates

A class to represent fuel data for rates.  Attributes ----------     fuel_type (str): The type of fuel. Values can be \"electricity\", \"natural_gas\", \"propane\", \"fuel_oil\", or \"net\".     rate_type (str): The type of rate. Values can be \"fixed\" or \"volumetric\".     value (float): The numerical value of what the metric is.     units (str): The measurement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fuel_type** | **str** |  | 
**value** | **float** |  | [optional] [default to 0.0]
**units** | **str** |  | 
**rate_type** | **str** |  | [optional] [default to 'volumetric']

## Example

```python
from ra_rem.models.fuel_data_rates import FuelDataRates

# TODO update the JSON string below
json = "{}"
# create an instance of FuelDataRates from a JSON string
fuel_data_rates_instance = FuelDataRates.from_json(json)
# print the JSON string representation of the object
print(FuelDataRates.to_json())

# convert the object into a dict
fuel_data_rates_dict = fuel_data_rates_instance.to_dict()
# create an instance of FuelDataRates from a dict
fuel_data_rates_from_dict = FuelDataRates.from_dict(fuel_data_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


