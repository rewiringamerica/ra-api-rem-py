# rewiringamerica_rem.BuildingProfilerApi

All URIs are relative to *https://api.rewiringamerica.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_home_profile_by_address**](BuildingProfilerApi.md#get_home_profile_by_address) | **GET** /api/v1/building-profile/address | Get home profile by address
[**get_home_profile_by_address_components**](BuildingProfilerApi.md#get_home_profile_by_address_components) | **POST** /api/v1/building-profile/address-components | Get home profile by address components


# **get_home_profile_by_address**
> BuildingProfile get_home_profile_by_address(address)

Get home profile by address

Geocode an address and match against ATTOM data to find building features for a given residence.

### Example

* Bearer Authentication (auth):

```python
import rewiringamerica_rem
from rewiringamerica_rem.models.building_profile import BuildingProfile
from rewiringamerica_rem.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: auth
configuration = rewiringamerica_rem.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rewiringamerica_rem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rewiringamerica_rem.BuildingProfilerApi(api_client)
    address = 'address_example' # str | The full address for a location including street number and name, city, state, and zip code.

    try:
        # Get home profile by address
        api_response = api_instance.get_home_profile_by_address(address)
        print("The response of BuildingProfilerApi->get_home_profile_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingProfilerApi->get_home_profile_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The full address for a location including street number and name, city, state, and zip code. | 

### Return type

[**BuildingProfile**](BuildingProfile.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_home_profile_by_address_components**
> BuildingProfile get_home_profile_by_address_components(address_component_request)

Get home profile by address components

Geocode an address and match against ATTOM data to find building features for a given residence.

### Example

* Bearer Authentication (auth):

```python
import rewiringamerica_rem
from rewiringamerica_rem.models.address_component_request import AddressComponentRequest
from rewiringamerica_rem.models.building_profile import BuildingProfile
from rewiringamerica_rem.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: auth
configuration = rewiringamerica_rem.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rewiringamerica_rem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rewiringamerica_rem.BuildingProfilerApi(api_client)
    address_component_request = rewiringamerica_rem.AddressComponentRequest() # AddressComponentRequest | 

    try:
        # Get home profile by address components
        api_response = api_instance.get_home_profile_by_address_components(address_component_request)
        print("The response of BuildingProfilerApi->get_home_profile_by_address_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingProfilerApi->get_home_profile_by_address_components: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_component_request** | [**AddressComponentRequest**](AddressComponentRequest.md)|  | 

### Return type

[**BuildingProfile**](BuildingProfile.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

