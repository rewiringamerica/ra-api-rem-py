# rewiringamerica_rem.ResidentialElectrificationModelApi

All URIs are relative to *https://api.rewiringamerica.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_address**](ResidentialElectrificationModelApi.md#get_by_address) | **GET** /api/v1/rem/address | Get by address
[**get_by_profile**](ResidentialElectrificationModelApi.md#get_by_profile) | **POST** /api/v1/rem/profile | Get by profile
[**get_impl_version**](ResidentialElectrificationModelApi.md#get_impl_version) | **GET** /api/v1/rem/server_version | Get implementation version


# **get_by_address**
> Savings get_by_address(upgrade, address, heating_fuel)

Get by address

Predict a user's annual savings using the Residential Electrification Model. This API makes predictions of the energy, emissions, and energy bill changes for an existing home based on the upgrade type, the address of the home being upgraded, and the current heating fuel.  Using the provided address, we first query a large database of home properties that Rewiring America has assembled, which contains data such as home age, size, construction material, and much more. We don't know all of the properties needed to get a good estimate of energy consumption, so we perform a [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation over a sample homes chosen from a [conditional probability distribution](https://github.com/NREL/resstock/tree/develop/project_national/housing_characteristics) based the properties that we do know. We then estimate the energy consumption for each sample building by running inference using a Machine Learning based surrogate model, trained on [EnergyPlus](https://energyplus.net/) simulations.  The response JSON is a dictionary with three components: - `fuel_results`: This is a dictionary of the main results from the model, one for each fuel type: `electricity`, `fuel_oil`, `natural_gas`, `propane`, `total` (for the total of all the others). - `rates`: A summary of the rates used to calculate the annual cost in dollars for each fuel. These vary from region to region based local fuel costs. - `emissions_factors`: A summary of the local emissions factors used to calculate annual emissions. Electricity emissions vary from region to region based on how electricity is generated.  Within the `fuel_results` subsection for each of the fuel types, there are three components:   - `baseline`: the annual usage of the fuel before the upgrade across all end uses  (e.g., heating, cooling, water heating, drying, cooking).   - `upgrade`: the annual usage of the fuel after the upgrade across all end uses.   - `delta`: the change in usage of the fuel across all end uses.  Inside those three, there are parallel structures with statistics for the `energy` consumption for each fuel, as well as the `emissions` and `cost` incurred by the consumption of each fuel. The electricity emissions factors are [long run marginal emissions rates assuming a 95% decarbonized grid by 2050](https://www.nrel.gov/analysis/cambium.html).  The emissions and costs are computed with the `rates` and `emissions_factors` data mentioned above, where the costs reflect the annual costs from both volumetric charges and fixed charges. Note that the fixed charges are based on the presence of the given fuel in the baseline scenario, and not assumed to change in the upgrade scenario.  All of the statistics are for a full typical weather year. The units for each of the statistics are also provided and are as appropriate for the fuel, emissions, or cost.  If `baseline` is specified as the upgrade in the request, `fuel_results` will exclude `upgrade` and `delta` since baseline represents the home's current state without any upgrades.  **A note on statistics**: For each value we provide statistics for, we provide a mean, a median, and the 20th and 80th percentile values over all the set of sample homes in the Monte Carlo simulation. It is important to note that the statistics are taken over the distribution of the values they represent. This means, for example, that the median electricity usage before the upgrade, the median electricity usage after the upgrade, and the median change of electricity usage might all be from the same modeled home. So adding the median change to the median usage before the upgrade might not produce the number reported as the median usage after the upgrade.  Note that because we are modeling whole home energy consumption over a set of building samples, and the building set contains homes with a variety of fuels for the non-heating appliances, you may see consumption of fuels other than the passed heating fuel, particularly for the mean.  **Demonstrations**  There are two sample Python notebooks that demonstrate the API in action. - [REM Demo.ipynb](https://github.com/rewiringamerica/api_demos/blob/main/notebooks/REM%20Demo.ipynb) illustrates basic API calls. - [All About REM Statistics.ipynb](https://github.com/rewiringamerica/api_demos/blob/main/notebooks/All%20About%20REM%20Statistics.ipynb) digs into details on the statistics that the API returns and how they relate to one another in various circumstances.  There are also examples showing how to integrate the REM API into a web site. See the full list [here](https://github.com/rewiringamerica/api_demos?tab=readme-ov-file#api_demos).

### Example

* Bearer Authentication (auth):

```python
import rewiringamerica_rem
from rewiringamerica_rem.models.heating_fuel import HeatingFuel
from rewiringamerica_rem.models.savings import Savings
from rewiringamerica_rem.models.supported_upgrade import SupportedUpgrade
from rewiringamerica_rem.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: auth
configuration = rewiringamerica_rem.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rewiringamerica_rem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rewiringamerica_rem.ResidentialElectrificationModelApi(api_client)
    upgrade = rewiringamerica_rem.SupportedUpgrade() # SupportedUpgrade | The upgrade whose effects we want to analyze. Supported values are as follows: - `baseline`: Baseline building with no upgrades applied. - `combination__all_electric__hvac_seer24_hspf13__weatherization`: A whole-home upgrade including a high efficiency air source heat pump for the home’s HVAC system, basic weatherization, a heat pump water heater, a heat pump dryer, and an induction stove. HVAC heat pump is SEER 24, HSPF 13 for ducted systems; SEER 29.3, HSPF 14 for ductless systems, heat pump water heater is UEF 3.35-3.45, and heat pump dryer is Combined Energy Factor (CEF) 5.2. Additional details can be found in measure package 9 (on page 9) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf).  - `combination__hvac_seer18_hspf10__weatherization`: A medium-efficiency heat pump upgrade for the home's HVAC system, plus a basic weatherization upgrade. The heat pump is SEER 18, HSPF 10 for ducted systems; SEER 18, HSPF 10.5 for ductless systems. The nominal capacity is sized equal to the larger of heating/cooling design loads, and the heating and cooling are modeled without setpoint setbacks. The basic weatherization component of this upgrade includes attic floor insulation, air sealing, duct sealing, and drill-and-fill insulation. Attic floor insulation levels are upgraded for compliance with IECC-Residential 2021 and range from R-30 to R-60 depending on climate zone. Attic floor insulation only applies to dwelling units with vented attics. Air sealing is performed to reduce ACH50 by 30%, duct sealing is performed to reduce duct leakage to 10%, and a drill-and-fill insulation level of R-13 is applied to uninsulated wood stud walls. Additional details can be found in measure package 1 (on page 4) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf). - `hvac__heat_pump_seer15_hspf9`: A relatively-low efficiency air source heat pump upgrade for the home’s HVAC system. Heat pump is SEER 15, HSPF 9 for both ducted and ductless systems.Additional details can be found in measure package 3 (on page 5) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf). - `hvac__heat_pump_seer18_hspf10`: A medium-efficiency heat pump upgrade for the home's HVAC system. SEER 18, HSPF 10 for ducted systems; SEER 18, HSPF 10.5 for ductless systems. The nominal capacity is sized equal to the larger of heating/cooling design loads, and the heating and cooling are modeled without setpoint setbacks.  - `hvac__heat_pump_seer24_hspf13`: A high efficiency air source heat pump upgrade for the home’s HVAC system. Heat pump is SEER 24, HSPF 13 for ducted systems; SEER 29.3, HSPF 14 for ductless systems. Additional details can be found in measure package 4 (on page 6) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf).  - `weatherization__insulation_air_duct_sealing`: A basic weatherization upgrade for the home. Measures include attic floor insulation, air sealing, duct sealing, and drill-and-fill insulation. Attic floor insulation levels are upgraded for compliance with IECC-Residential 2021 and range from R-30 to R-60 depending on climate zone. Attic floor insulation only applies to dwelling units with vented attics. Air sealing is performed to reduce ACH50 by 30%, duct sealing is performed to reduce duct leakage to 10%, and a drill-and-fill insulation level of R-13 is applied to uninsulated wood stud walls. Additional details can be found in measure package 1 (on page 4) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf).
    address = 'address_example' # str | The full address for a location including street number and name, city, state, and zip code.
    heating_fuel = rewiringamerica_rem.HeatingFuel() # HeatingFuel | The heating fuel used in the home before the upgrade. Supported values are as follows: - `electricity`: the home is currently heated with electric heating, such as   electric resistance heating or a heat pump. - `natural_gas`: The home is currently heated with natural gas. - `fuel_oil`: The home is currently heated with fuel oil. - `propane`:  The home is currently heated with propane. 

    try:
        # Get by address
        api_response = api_instance.get_by_address(upgrade, address, heating_fuel)
        print("The response of ResidentialElectrificationModelApi->get_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentialElectrificationModelApi->get_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade** | [**SupportedUpgrade**](SupportedUpgrade.md)| The upgrade whose effects we want to analyze. Supported values are as follows: - &#x60;baseline&#x60;: Baseline building with no upgrades applied. - &#x60;combination__all_electric__hvac_seer24_hspf13__weatherization&#x60;: A whole-home upgrade including a high efficiency air source heat pump for the home’s HVAC system, basic weatherization, a heat pump water heater, a heat pump dryer, and an induction stove. HVAC heat pump is SEER 24, HSPF 13 for ducted systems; SEER 29.3, HSPF 14 for ductless systems, heat pump water heater is UEF 3.35-3.45, and heat pump dryer is Combined Energy Factor (CEF) 5.2. Additional details can be found in measure package 9 (on page 9) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf).  - &#x60;combination__hvac_seer18_hspf10__weatherization&#x60;: A medium-efficiency heat pump upgrade for the home&#39;s HVAC system, plus a basic weatherization upgrade. The heat pump is SEER 18, HSPF 10 for ducted systems; SEER 18, HSPF 10.5 for ductless systems. The nominal capacity is sized equal to the larger of heating/cooling design loads, and the heating and cooling are modeled without setpoint setbacks. The basic weatherization component of this upgrade includes attic floor insulation, air sealing, duct sealing, and drill-and-fill insulation. Attic floor insulation levels are upgraded for compliance with IECC-Residential 2021 and range from R-30 to R-60 depending on climate zone. Attic floor insulation only applies to dwelling units with vented attics. Air sealing is performed to reduce ACH50 by 30%, duct sealing is performed to reduce duct leakage to 10%, and a drill-and-fill insulation level of R-13 is applied to uninsulated wood stud walls. Additional details can be found in measure package 1 (on page 4) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf). - &#x60;hvac__heat_pump_seer15_hspf9&#x60;: A relatively-low efficiency air source heat pump upgrade for the home’s HVAC system. Heat pump is SEER 15, HSPF 9 for both ducted and ductless systems.Additional details can be found in measure package 3 (on page 5) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf). - &#x60;hvac__heat_pump_seer18_hspf10&#x60;: A medium-efficiency heat pump upgrade for the home&#39;s HVAC system. SEER 18, HSPF 10 for ducted systems; SEER 18, HSPF 10.5 for ductless systems. The nominal capacity is sized equal to the larger of heating/cooling design loads, and the heating and cooling are modeled without setpoint setbacks.  - &#x60;hvac__heat_pump_seer24_hspf13&#x60;: A high efficiency air source heat pump upgrade for the home’s HVAC system. Heat pump is SEER 24, HSPF 13 for ducted systems; SEER 29.3, HSPF 14 for ductless systems. Additional details can be found in measure package 4 (on page 6) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf).  - &#x60;weatherization__insulation_air_duct_sealing&#x60;: A basic weatherization upgrade for the home. Measures include attic floor insulation, air sealing, duct sealing, and drill-and-fill insulation. Attic floor insulation levels are upgraded for compliance with IECC-Residential 2021 and range from R-30 to R-60 depending on climate zone. Attic floor insulation only applies to dwelling units with vented attics. Air sealing is performed to reduce ACH50 by 30%, duct sealing is performed to reduce duct leakage to 10%, and a drill-and-fill insulation level of R-13 is applied to uninsulated wood stud walls. Additional details can be found in measure package 1 (on page 4) of [this document](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf). | 
 **address** | **str**| The full address for a location including street number and name, city, state, and zip code. | 
 **heating_fuel** | [**HeatingFuel**](HeatingFuel.md)| The heating fuel used in the home before the upgrade. Supported values are as follows: - &#x60;electricity&#x60;: the home is currently heated with electric heating, such as   electric resistance heating or a heat pump. - &#x60;natural_gas&#x60;: The home is currently heated with natural gas. - &#x60;fuel_oil&#x60;: The home is currently heated with fuel oil. - &#x60;propane&#x60;:  The home is currently heated with propane.  | 

### Return type

[**Savings**](Savings.md)

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

# **get_by_profile**
> Savings get_by_profile(rem_profile_request)

Get by profile

Predict a user's annual savings using Residential Electrification Model, using a Building Profile and an Upgrade.

### Example

* Bearer Authentication (auth):

```python
import rewiringamerica_rem
from rewiringamerica_rem.models.rem_profile_request import RemProfileRequest
from rewiringamerica_rem.models.savings import Savings
from rewiringamerica_rem.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: auth
configuration = rewiringamerica_rem.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rewiringamerica_rem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rewiringamerica_rem.ResidentialElectrificationModelApi(api_client)
    rem_profile_request = rewiringamerica_rem.RemProfileRequest() # RemProfileRequest | 

    try:
        # Get by profile
        api_response = api_instance.get_by_profile(rem_profile_request)
        print("The response of ResidentialElectrificationModelApi->get_by_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentialElectrificationModelApi->get_by_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rem_profile_request** | [**RemProfileRequest**](RemProfileRequest.md)|  | 

### Return type

[**Savings**](Savings.md)

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

# **get_impl_version**
> str get_impl_version()

Get implementation version

Return the back end version of the code that is deployed.  This is not the version of the API, but rather of the code that implements it. This is mainly to track code deployments. The same API version is typically supported by a series of deployments each of which improves upon earlier ones in some way, such as fixing bugs or improving performance.

### Example

* Bearer Authentication (auth):

```python
import rewiringamerica_rem
from rewiringamerica_rem.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: auth
configuration = rewiringamerica_rem.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rewiringamerica_rem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rewiringamerica_rem.ResidentialElectrificationModelApi(api_client)

    try:
        # Get implementation version
        api_response = api_instance.get_impl_version()
        print("The response of ResidentialElectrificationModelApi->get_impl_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResidentialElectrificationModelApi->get_impl_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

