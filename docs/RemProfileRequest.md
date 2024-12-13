# RemProfileRequest

A class representing the request body used to retrieve a building's profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upgrade** | [**SupportedUpgrade**](SupportedUpgrade.md) | Building Upgrade | 
**heating_fuel** | [**HeatingFuelInput**](HeatingFuelInput.md) | Heating Fuel | 
**building_profile** | [**BuildingProfile**](BuildingProfile.md) | Building Profile | 

## Example

```python
from rewiringamerica_rem.models.rem_profile_request import RemProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemProfileRequest from a JSON string
rem_profile_request_instance = RemProfileRequest.from_json(json)
# print the JSON string representation of the object
print(RemProfileRequest.to_json())

# convert the object into a dict
rem_profile_request_dict = rem_profile_request_instance.to_dict()
# create an instance of RemProfileRequest from a dict
rem_profile_request_from_dict = RemProfileRequest.from_dict(rem_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


