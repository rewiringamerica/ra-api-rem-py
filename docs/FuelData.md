# FuelData

A class to represent fuel data.  Attributes ----------     fuel_type (str): The type of fuel. Values can be \"electricity\", \"natural_gas\", \"propane\", \"fuel_oil\", or \"net\".     value (float): The numerical value of what the metric is.     units (str): The measurement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fuel_type** | **str** |  | 
**value** | **float** |  | [optional] [default to 0.0]
**units** | **str** |  | 

## Example

```python
from ra_rem.models.fuel_data import FuelData

# TODO update the JSON string below
json = "{}"
# create an instance of FuelData from a JSON string
fuel_data_instance = FuelData.from_json(json)
# print the JSON string representation of the object
print(FuelData.to_json())

# convert the object into a dict
fuel_data_dict = fuel_data_instance.to_dict()
# create an instance of FuelData from a dict
fuel_data_from_dict = FuelData.from_dict(fuel_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


