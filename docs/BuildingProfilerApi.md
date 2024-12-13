# rewiringamerica_rem.BuildingProfilerApi

All URIs are relative to *https://api.rewiringamerica.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_home_profile**](BuildingProfilerApi.md#get_home_profile) | **GET** /api/v1/building_profiler/home | Get Home Profile


# **get_home_profile**
> BuildingProfile get_home_profile(address)

Get Home Profile

Geocode an address and match against ATTOM data to find building features for a given residence.  This implementation takes in an address as a required query parameter and returns geographic characteristics and building features about the home if the input address is valid.

### Example

* Bearer Authentication (auth):

```python
import rewiringamerica_rem
from rewiringamerica_rem.models.building_profile import BuildingProfile
from rewiringamerica_rem.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rewiringamerica.org
# See configuration.py for a list of all supported configuration parameters.
configuration = rewiringamerica_rem.Configuration(
    host = "https://api.rewiringamerica.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: auth
configuration = rewiringamerica_rem.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rewiringamerica_rem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rewiringamerica_rem.BuildingProfilerApi(api_client)
    address = 'address_example' # str | The location of a home.

    try:
        # Get Home Profile
        api_response = api_instance.get_home_profile(address)
        print("The response of BuildingProfilerApi->get_home_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildingProfilerApi->get_home_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The full address string for a location including street number and name, city, state,         and zip code. | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

