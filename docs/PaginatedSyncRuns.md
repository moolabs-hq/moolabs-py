# PaginatedSyncRuns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SyncRunItem]**](SyncRunItem.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from moolabs.models.paginated_sync_runs import PaginatedSyncRuns

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSyncRuns from a JSON string
paginated_sync_runs_instance = PaginatedSyncRuns.from_json(json)
# print the JSON string representation of the object
print(PaginatedSyncRuns.to_json())

# convert the object into a dict
paginated_sync_runs_dict = paginated_sync_runs_instance.to_dict()
# create an instance of PaginatedSyncRuns from a dict
paginated_sync_runs_from_dict = PaginatedSyncRuns.from_dict(paginated_sync_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


