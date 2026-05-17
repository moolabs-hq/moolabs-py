# SyncRunItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**status** | **str** |  | 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**error_summary** | **Dict[str, object]** |  | [optional] 
**row_counts** | **Dict[str, object]** |  | [optional] 
**is_bootstrap** | **bool** |  | 

## Example

```python
from moolabs.models.sync_run_item import SyncRunItem

# TODO update the JSON string below
json = "{}"
# create an instance of SyncRunItem from a JSON string
sync_run_item_instance = SyncRunItem.from_json(json)
# print the JSON string representation of the object
print(SyncRunItem.to_json())

# convert the object into a dict
sync_run_item_dict = sync_run_item_instance.to_dict()
# create an instance of SyncRunItem from a dict
sync_run_item_from_dict = SyncRunItem.from_dict(sync_run_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


