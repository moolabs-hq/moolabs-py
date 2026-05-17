# ShadowRunListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shadow_run_id** | **str** |  | 
**tenant_id** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**row_count** | **int** |  | 
**attributed_rows** | **int** |  | 
**coverage_pct** | **float** |  | 
**created_at** | **str** |  | 

## Example

```python
from moolabs.models.shadow_run_list_item import ShadowRunListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShadowRunListItem from a JSON string
shadow_run_list_item_instance = ShadowRunListItem.from_json(json)
# print the JSON string representation of the object
print(ShadowRunListItem.to_json())

# convert the object into a dict
shadow_run_list_item_dict = shadow_run_list_item_instance.to_dict()
# create an instance of ShadowRunListItem from a dict
shadow_run_list_item_from_dict = ShadowRunListItem.from_dict(shadow_run_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


