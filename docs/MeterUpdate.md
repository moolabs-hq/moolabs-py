# MeterUpdate

A meter update model.  Only the properties that can be updated are included. For example, the slug and aggregation cannot be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. Defaults to the slug if not specified. | [optional] 
**group_by** | **Dict[str, str]** | Named JSONPath expressions to extract the group by values from the event data.  Keys must be unique and consist only alphanumeric and underscore characters. | [optional] 

## Example

```python
from moolabs.models.meter_update import MeterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MeterUpdate from a JSON string
meter_update_instance = MeterUpdate.from_json(json)
# print the JSON string representation of the object
print(MeterUpdate.to_json())

# convert the object into a dict
meter_update_dict = meter_update_instance.to_dict()
# create an instance of MeterUpdate from a dict
meter_update_from_dict = MeterUpdate.from_dict(meter_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


