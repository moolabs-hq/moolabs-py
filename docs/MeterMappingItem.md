# MeterMappingItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meter_slug** | **str** |  | 
**feature_key** | **str** |  | 
**effective_from** | **str** |  | 
**effective_to** | **str** |  | 
**is_active** | **bool** |  | 

## Example

```python
from moolabs.models.meter_mapping_item import MeterMappingItem

# TODO update the JSON string below
json = "{}"
# create an instance of MeterMappingItem from a JSON string
meter_mapping_item_instance = MeterMappingItem.from_json(json)
# print the JSON string representation of the object
print(MeterMappingItem.to_json())

# convert the object into a dict
meter_mapping_item_dict = meter_mapping_item_instance.to_dict()
# create an instance of MeterMappingItem from a dict
meter_mapping_item_from_dict = MeterMappingItem.from_dict(meter_mapping_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


