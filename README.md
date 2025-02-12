# rewiringamerica-rem
An API for REM, the Residential Electrification Model.

Rewiring America's other APIs can be found [at our main API site](https://api.rewiringamerica.org/).

Example code demonstrating how to use the APIs can be found in the [api_demos](https://github.com/rewiringamerica/api_demos) Github repo.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.4.2
- Package version: 0.4.2
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://www.rewiringamerica.org/](https://www.rewiringamerica.org/)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

You can install using:

```sh
pip install rewiringamerica_rem
```

Then import the package:
```python
import rewiringamerica_rem
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rewiringamerica_rem
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

[Sign up for an API key](https://homes.rewiringamerica.org/api/developer-login) and follow the [installation procedure](#installation--usage).
Then, run the following:

```python

import rewiringamerica_rem
from rewiringamerica_rem.rest import ApiException
from pprint import pprint
import os


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
        print("The response of get_home_profile:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling get_home_profile: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.rewiringamerica.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BuildingProfilerApi* | [**get_home_profile**](docs/BuildingProfilerApi.md#get_home_profile) | **GET** /api/v1/building_profiler/home | Get home profile
*ResidentialElectrificationModelApi* | [**get_by_address**](docs/ResidentialElectrificationModelApi.md#get_by_address) | **GET** /api/v1/rem/address | Get by address
*ResidentialElectrificationModelApi* | [**get_by_profile**](docs/ResidentialElectrificationModelApi.md#get_by_profile) | **POST** /api/v1/rem/profile | Get by profile
*ResidentialElectrificationModelApi* | [**get_impl_version**](docs/ResidentialElectrificationModelApi.md#get_impl_version) | **GET** /api/v1/rem/server_version | Get implementation version


## Documentation For Models

 - [BuildingFeatures](docs/BuildingFeatures.md)
 - [BuildingProfile](docs/BuildingProfile.md)
 - [FuelRate](docs/FuelRate.md)
 - [FuelSavings](docs/FuelSavings.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HeatingFuel](docs/HeatingFuel.md)
 - [ImpactMetric](docs/ImpactMetric.md)
 - [MetricStatistics](docs/MetricStatistics.md)
 - [Quantity](docs/Quantity.md)
 - [RemProfileRequest](docs/RemProfileRequest.md)
 - [ResultFuelType](docs/ResultFuelType.md)
 - [Savings](docs/Savings.md)
 - [SupportedUpgrade](docs/SupportedUpgrade.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Sign up for an API key [here](https://homes.rewiringamerica.org/api/developer-login).

Authentication schemes defined for the API:
<a id="auth"></a>
### auth

- **Type**: Bearer authentication


## Author

datascience@rewiringamerica.org


