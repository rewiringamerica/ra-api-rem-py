# AddressComponentRequest

A class representing the request body to retrieve a building profile by address components.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_address** | **str** | The full mailing address of the home. | 
**street_number** | **str** | The street number in the home&#39;s mailing address. | 
**street_name** | **str** | The all-caps street name in the home&#39;s mailing address including directions that may occur             before or after the name and the abbreviate street type like ST or BLVD | 
**city** | **str** | The all-caps city in the home&#39;s mailing address. | 
**state_abbr** | **str** | The two-letter state abbreviation of the state in the home&#39;s mailing address. | 
**zip** | **str** | The five digit zip code in the home&#39;s mailing address. | 
**latitude** | **float** | The geocoded latitude of the home&#39;s location, specified to at least             5 significant digits after the decimal. | 
**longitude** | **float** | The geocoded longitude of the home&#39;s location, specified to at least             5 significant digits after the decimal. | 

## Example

```python
from rewiringamerica_rem.models.address_component_request import AddressComponentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressComponentRequest from a JSON string
address_component_request_instance = AddressComponentRequest.from_json(json)
# print the JSON string representation of the object
print(AddressComponentRequest.to_json())

# convert the object into a dict
address_component_request_dict = address_component_request_instance.to_dict()
# create an instance of AddressComponentRequest from a dict
address_component_request_from_dict = AddressComponentRequest.from_dict(address_component_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


