# BuildingFeatures

A class representing the set of possible building characteristics.  All values default to None, indicating that the given characteristic is unknown for the represented residence. If a characteristic has the string value of \"None\" it indicates that the characteristic, like Air Conditioning or a Pool, is not present at the represented residence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry_floor_area** | **float** | The square footage of the residence. | [optional] 
**geometry_stories** | **float** | The number of stories in the residence. | [optional] 
**bedrooms** | **float** | The number of bedrooms contained in the residence. | [optional] 
**bathrooms** | **float** | The number of bathrooms contained in the residence. | [optional] 
**vintage** | **float** | The year in which the residence was built. | [optional] 
**geometry_attic_type** | **List[str]** | The type of attic. | [optional] 
**hvac_cooling_type** | **List[str]** | The type of cooling system present in the residence. | [optional] 
**hvac_heating_type** | **List[str]** | The type of ductwork used for heating in the residence. | [optional] 
**hvac_heating_type_and_fuel** | **List[str]** | The heating appliance type and fuel in the residence. | [optional] 
**geometry_garage** | **List[str]** | The size of the garage as measured in the number of cars that can be placed within the garage. | [optional] 
**misc_pool** | **List[str]** | A string indicating the presence of a pool at the residence. | [optional] 
**misc_hot_tub_spa** | **List[str]** | The fuel type used to heat a hot tub if one is present at the residence. | [optional] 
**misc_well_pump** | **List[str]** | The efficiency of a well pump if one is located at the residence. | [optional] 
**misc_pool_heater** | **List[str]** | The presence and fuel type of a pool heater. | [optional] 
**geometry_wall_type** | **List[str]** | The material of the exterior walls on the residence. | [optional] 
**geometry_wall_exterior_finish** | **List[str]** | The finish and color of exterior walls on the residence. | [optional] 
**roof_material** | **List[str]** | The material of the roof on the residence | [optional] 
**geometry_building_type_acs** | **List[str]** | The American Community Survey building type of the residence. | [optional] 
**geometry_building_number_units_sfa** | **float** | The number of units in a single-family attached building. | [optional] 
**geometry_building_number_units_mf** | **float** | The number of units in a multifamily building. | [optional] 
**heating_fuel** | **List[str]** | The primary fuel used for heating the residence. | [optional] 
**water_heater_fuel** | **List[str]** | The fuel used by the water heater in the residence. | [optional] 

## Example

```python
from rewiringamerica_rem.models.building_features import BuildingFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingFeatures from a JSON string
building_features_instance = BuildingFeatures.from_json(json)
# print the JSON string representation of the object
print(BuildingFeatures.to_json())

# convert the object into a dict
building_features_dict = building_features_instance.to_dict()
# create an instance of BuildingFeatures from a dict
building_features_from_dict = BuildingFeatures.from_dict(building_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


