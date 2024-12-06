# ra_rem.BuildingProfilerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**building_profiler_get_home_profile**](BuildingProfilerApi.md#building_profiler_get_home_profile) | **GET** /api/v1/building_profiler/home | Get Home Profile


# **building_profiler_get_home_profile**
> BuildingProfile building_profiler_get_home_profile(address)

Get Home Profile

Geocode an address and match against ATTOM data to find building features for a given residence.  This implementation takes in an address as a required query parameter and returns geographic characteristics and building features about the home if the input address is valid.  Parameters ----------     address: (str) The full address string for a location including street number and name, city, state,         and zip code.  Returns -------     BuildingProfile: JSON containing geographic information like county or state and building features like         square footage or vintage for the residence located at the given address.

### Example


```python
import ra_rem
from ra_rem.models.building_profile import BuildingProfile
from ra_rem.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ra_rem.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ra_rem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ra_rem.BuildingProfilerApi(api_client)
    address = 'address_example' # str | The location of a home.

    try:
        # Get Home Profile
        api_response = api_instance.building_profiler_get_home_profile(address)
        print("The response of BuildingProfilerApi->building_profiler_get_home_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingProfilerApi->building_profiler_get_home_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The location of a home. | 

### Return type

[**BuildingProfile**](BuildingProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

