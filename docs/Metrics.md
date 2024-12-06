# Metrics

A class to represent metrics data.  Attributes ----------     samples (Dict[int, List[FuelData]]): A dictionary of sample IDs and their associated data for         energy, emissions, and cost.     mean (List[FuelData]): Mean data for energy, emissions, and cost.     median (List[FuelData]): Median data for energy, emissions, and cost.     percentile_20 (List[FuelData]): 20th percentile data for energy, emissions, and cost.     percentile_80 (List[FuelData]): 80th percentile data for energy, emissions, and cost.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mean** | [**List[FuelData]**](FuelData.md) |  | 
**median** | [**List[FuelData]**](FuelData.md) |  | 
**percentile_20** | [**List[FuelData]**](FuelData.md) |  | 
**percentile_80** | [**List[FuelData]**](FuelData.md) |  | 

## Example

```python
from ra_rem.models.metrics import Metrics

# TODO update the JSON string below
json = "{}"
# create an instance of Metrics from a JSON string
metrics_instance = Metrics.from_json(json)
# print the JSON string representation of the object
print(Metrics.to_json())

# convert the object into a dict
metrics_dict = metrics_instance.to_dict()
# create an instance of Metrics from a dict
metrics_from_dict = Metrics.from_dict(metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


