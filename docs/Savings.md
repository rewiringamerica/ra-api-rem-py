# Savings

A class to represent savings data.  Attributes ----------     baseline (Impact): The data if no upgrade is passed into the surrogate model.     upgrade (Impact): The data if an upgrade is passed into the surrogate model.     delta (Impact): The deltas if an upgrade is passed into the surrogate model.     rates (List[FuelData]): The cost/fuel unit rates for each fuel type.     emissions_factors (List[FuelData]): The kgCO2e/fuel unit rates for each fuel type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**Impact**](Impact.md) |  | 
**upgrade** | [**Impact**](Impact.md) |  | 
**delta** | [**Impact**](Impact.md) |  | 
**rates** | [**List[FuelDataRates]**](FuelDataRates.md) |  | 
**emissions_factors** | [**List[FuelData]**](FuelData.md) |  | 

## Example

```python
from ra_rem.models.savings import Savings

# TODO update the JSON string below
json = "{}"
# create an instance of Savings from a JSON string
savings_instance = Savings.from_json(json)
# print the JSON string representation of the object
print(Savings.to_json())

# convert the object into a dict
savings_dict = savings_instance.to_dict()
# create an instance of Savings from a dict
savings_from_dict = Savings.from_dict(savings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


