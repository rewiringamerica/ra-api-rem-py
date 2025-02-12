# rewiringamerica_rem.BuildingProfilerApi

All URIs are relative to *https://api.rewiringamerica.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_home_profile**](BuildingProfilerApi.md#get_home_profile) | **GET** /api/v1/building_profiler/home | Get home profile


# **get_home_profile**
> BuildingProfile get_home_profile(address)

Get home profile

Geocode an address and match against ATTOM data to find building features for a given residence.  This implementation takes in an address as a required query parameter and returns geographic characteristics and building features about the home if the input address is valid.  Parameters ---------- address     The full address string for a location including street number and name, city, state, and zip code. request     The raw incoming request object.  Returns ------- BuildingProfile     An object containing geographic information like county or state and building features like     square footage or vintage for the residence located at the given address.  Raises ------ HTTPException     If external APIs throw errors, the address is unparsable or missing information, or the address is outside of     the contiguous US.

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
        # Get home profile
        api_response = api_instance.get_home_profile(address)
        print("The response of BuildingProfilerApi->get_home_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingProfilerApi->get_home_profile: %s\n" % e)
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

