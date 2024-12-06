# Impact

A class to represent impact data based on upgrade.  Attributes ----------     energy (Metrics): The data for energy usage per fuel type.     emissions (Metrics): The data for emissions per fuel type.     cost (Metrics): The data for cost per fuel type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy** | [**Metrics**](Metrics.md) |  | 
**emissions** | [**Metrics**](Metrics.md) |  | 
**cost** | [**Metrics**](Metrics.md) |  | 

## Example

```python
from ra_rem.models.impact import Impact

# TODO update the JSON string below
json = "{}"
# create an instance of Impact from a JSON string
impact_instance = Impact.from_json(json)
# print the JSON string representation of the object
print(Impact.to_json())

# convert the object into a dict
impact_dict = impact_instance.to_dict()
# create an instance of Impact from a dict
impact_from_dict = Impact.from_dict(impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


