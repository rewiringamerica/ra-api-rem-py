import ra_rem
from ra_rem.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ra_rem.Configuration(
    host="YOUR_URL_HERE"
)

# Enter a context with an instance of the API client
with ra_rem.ApiClient(configuration) as api_client:
    api_client.default_headers['Authorization'] = 'Bearer YOUR_API_KEY_HERE'
    # Create instances of the API classes
    bp_api = ra_rem.BuildingProfilerApi(api_client)
    rem_api = ra_rem.ResidentialElectrificationModelApi(api_client)
    address = 'YOUR_ADDRESS_HERE' # str | The location of a home.

    try:
        # Get Home Profile
        api_response = bp_api.building_profiler_get_home_profile(address)
        print("The response of BuildingProfilerApi->building_profiler_get_home_profile:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildingProfilerApi->building_profiler_get_home_profile: %s\n" % e)

    try:
        # Get Savings by address
        upgrade = ra_rem.ValidUpgrade.BASIC_ENCLOSURE
        heating_fuel = ra_rem.HeatingFuel.ELECTRICITY
        api_response = rem_api.rem_get_by_address(upgrade, address, heating_fuel)
        print("The response of ResidentialElectrificationModelApi->rem_get_by_address:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResidentialElectrificationModelApi->rem_get_by_address: %s\n" % e)