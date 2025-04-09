# Savings

Represents the impacts of an upgrade and additional details on how these were computed.  Additional details include the rates, emissions factors and number of samples used to compute the impacts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fuel_results** | [**Dict[str, FuelSavings]**](FuelSavings.md) | A dictionary of results, one for each fuel type. | 
**rates** | **Dict[str, List[FuelRate]]** | A dictionary of rates used to compute the cost of consuming each fuel. | 
**emissions_factors** | [**Dict[str, Quantity]**](Quantity.md) | A dictionary of conversion factors used to compute the emissions from each fuel. | 
**sampling_details** | [**SamplingDetails**](SamplingDetails.md) | A dictionary describing the number of samples used in the model. | 

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


