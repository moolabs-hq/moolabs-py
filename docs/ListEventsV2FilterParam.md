# ListEventsV2FilterParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**FilterString**](FilterString.md) |  | [optional] 
**source** | [**FilterString**](FilterString.md) |  | [optional] 
**subject** | [**FilterString**](FilterString.md) |  | [optional] 
**customer_id** | [**FilterIDExact**](FilterIDExact.md) |  | [optional] 
**type** | [**FilterString**](FilterString.md) |  | [optional] 
**time** | [**FilterTime**](FilterTime.md) |  | [optional] 
**ingested_at** | [**FilterTime**](FilterTime.md) |  | [optional] 

## Example

```python
from moolabs.models.list_events_v2_filter_param import ListEventsV2FilterParam

# TODO update the JSON string below
json = "{}"
# create an instance of ListEventsV2FilterParam from a JSON string
list_events_v2_filter_param_instance = ListEventsV2FilterParam.from_json(json)
# print the JSON string representation of the object
print(ListEventsV2FilterParam.to_json())

# convert the object into a dict
list_events_v2_filter_param_dict = list_events_v2_filter_param_instance.to_dict()
# create an instance of ListEventsV2FilterParam from a dict
list_events_v2_filter_param_from_dict = ListEventsV2FilterParam.from_dict(list_events_v2_filter_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


