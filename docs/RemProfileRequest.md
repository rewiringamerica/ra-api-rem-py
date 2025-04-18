# RemProfileRequest

A class representing the request body used to retrieve a building's profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upgrade** | [**SupportedUpgrade**](SupportedUpgrade.md) | The upgrade whose effects we want to analyze. | 
**heating_fuel** | [**HeatingFuel**](HeatingFuel.md) | The heating fuel used in the home before the upgrade. | 
**water_heater_fuel** | [**WaterHeaterFuel**](WaterHeaterFuel.md) |  | [optional] 
**building_profile** | [**BuildingProfile**](BuildingProfile.md) | The known geographic features and building characteristics for a given residence. | 

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


