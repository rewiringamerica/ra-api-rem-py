# FuelRate

Represents a `Quantity` with the addition of a rate type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The numerical value. | [optional] [default to 0.0]
**unit** | **str** | The unit. | 
**rate_type** | **str** | The type of rate. Values can be &#39;fixed&#39; or &#39;volumetric&#39;. | [optional] [default to 'volumetric']

## Example

```python
from rewiringamerica_rem.models.fuel_rate import FuelRate

# TODO update the JSON string below
json = "{}"
# create an instance of FuelRate from a JSON string
fuel_rate_instance = FuelRate.from_json(json)
# print the JSON string representation of the object
print(FuelRate.to_json())

# convert the object into a dict
fuel_rate_dict = fuel_rate_instance.to_dict()
# create an instance of FuelRate from a dict
fuel_rate_from_dict = FuelRate.from_dict(fuel_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


