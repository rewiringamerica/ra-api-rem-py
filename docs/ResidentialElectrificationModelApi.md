# ra_rem.ResidentialElectrificationModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rem_get_by_address**](ResidentialElectrificationModelApi.md#rem_get_by_address) | **GET** /api/v1/rem/address | Get By Address
[**rem_get_by_profile**](ResidentialElectrificationModelApi.md#rem_get_by_profile) | **POST** /api/v1/rem/profile | Get By Profile


# **rem_get_by_address**
> Savings rem_get_by_address(upgrade, address, heating_fuel=heating_fuel)

Get By Address

Predict a user's savings using the Residential Electrification Model using an upgrade and address.  This implementation takes in an address as a required query parameter. However, it is currently not used in any way. The JSON response includes hardcoded values.  Parameters ----------     address: The location of a user.  Returns -------     Savings: JSON containing prediction output from Dohyo.

### Example


```python
import ra_rem
from ra_rem.models.heating_fuel import HeatingFuel
from ra_rem.models.savings import Savings
from ra_rem.models.valid_upgrade import ValidUpgrade
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
    api_instance = ra_rem.ResidentialElectrificationModelApi(api_client)
    upgrade = ra_rem.ValidUpgrade() # ValidUpgrade | Building upgrade.
    address = 'address_example' # str | The location of a user.
    heating_fuel = ra_rem.HeatingFuel() # HeatingFuel | The heating fuel of a residence. (optional)

    try:
        # Get By Address
        api_response = api_instance.rem_get_by_address(upgrade, address, heating_fuel=heating_fuel)
        print("The response of ResidentialElectrificationModelApi->rem_get_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentialElectrificationModelApi->rem_get_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade** | [**ValidUpgrade**](.md)| Building upgrade. | 
 **address** | **str**| The location of a user. | 
 **heating_fuel** | [**HeatingFuel**](.md)| The heating fuel of a residence. | [optional] 

### Return type

[**Savings**](Savings.md)

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

# **rem_get_by_profile**
> Savings rem_get_by_profile(rem_profile_request)

Get By Profile

Predict a user's savings using Residential Electrification Model using a Building Profile and an Upgrade.  This implementation takes in a dictionary of required inputs for the request body. However, it is currently not used in any way. The JSON response includes hardcoded values.  Parameters ----------     rem_profile_req (RemProfileRequest): An object containing all of the necessary inputs for Dohyo:         Upgrade, County, PUMA, Climate Zone, ResStock weather file location, state abbreviation, and         building features.  Returns -------     Savings: JSON containing prediction output from Dohyo.

### Example


```python
import ra_rem
from ra_rem.models.rem_profile_request import RemProfileRequest
from ra_rem.models.savings import Savings
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
    api_instance = ra_rem.ResidentialElectrificationModelApi(api_client)
    rem_profile_request = ra_rem.RemProfileRequest() # RemProfileRequest | 

    try:
        # Get By Profile
        api_response = api_instance.rem_get_by_profile(rem_profile_request)
        print("The response of ResidentialElectrificationModelApi->rem_get_by_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentialElectrificationModelApi->rem_get_by_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rem_profile_request** | [**RemProfileRequest**](RemProfileRequest.md)|  | 

### Return type

[**Savings**](Savings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

