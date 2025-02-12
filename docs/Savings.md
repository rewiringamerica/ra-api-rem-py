# Savings

Represents the impacts of an upgrade and the rates and emissions factors used to compute these impacts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fuel_results** | [**Dict[str, FuelSavings]**](FuelSavings.md) | A list of results, one for each fuel type. | 
**rates** | **Dict[str, List[FuelRate]]** | A list of rates used to compute the cost of consuming each fuel. | 
**emissions_factors** | [**Dict[str, Quantity]**](Quantity.md) | A list of conversion factors used to compute the emissions from each fuel. | 

## Example

```python
from rewiringamerica_rem.models.savings import Savings

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


