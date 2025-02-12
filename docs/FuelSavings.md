# FuelSavings

A class to represent baseline, upgrade and savings data for a particular fuel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**ImpactMetric**](ImpactMetric.md) | The estimates under the baseline scenario. | 
**upgrade** | [**ImpactMetric**](ImpactMetric.md) | The estimates under the upgrade scenario if passed. | [optional] 
**delta** | [**ImpactMetric**](ImpactMetric.md) | The savings estimates (difference between baseline and upgrade) under the upgrade scenario if passed. | [optional] 

## Example

```python
from rewiringamerica_rem.models.fuel_savings import FuelSavings

# TODO update the JSON string below
json = "{}"
# create an instance of FuelSavings from a JSON string
fuel_savings_instance = FuelSavings.from_json(json)
# print the JSON string representation of the object
print(FuelSavings.to_json())

# convert the object into a dict
fuel_savings_dict = fuel_savings_instance.to_dict()
# create an instance of FuelSavings from a dict
fuel_savings_from_dict = FuelSavings.from_dict(fuel_savings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


