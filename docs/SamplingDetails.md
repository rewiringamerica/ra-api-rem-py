# SamplingDetails

Details on the samples used in the model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_samples** | **int** | The number of samples used to compute the statistics. | 
**num_excluded_samples** | **int** | The number of samples that matched the building profile but for which the chosen upgradewas not applicable, and were therefore excluded when computing the statistics. | 

## Example

```python
from rewiringamerica_rem.models.sampling_details import SamplingDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SamplingDetails from a JSON string
sampling_details_instance = SamplingDetails.from_json(json)
# print the JSON string representation of the object
print(SamplingDetails.to_json())

# convert the object into a dict
sampling_details_dict = sampling_details_instance.to_dict()
# create an instance of SamplingDetails from a dict
sampling_details_from_dict = SamplingDetails.from_dict(sampling_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


