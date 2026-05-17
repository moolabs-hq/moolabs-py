# SyncConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | 
**cloud_provider** | **str** |  | 
**schedule** | **str** |  | 

## Example

```python
from moolabs.models.sync_config_response import SyncConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncConfigResponse from a JSON string
sync_config_response_instance = SyncConfigResponse.from_json(json)
# print the JSON string representation of the object
print(SyncConfigResponse.to_json())

# convert the object into a dict
sync_config_response_dict = sync_config_response_instance.to_dict()
# create an instance of SyncConfigResponse from a dict
sync_config_response_from_dict = SyncConfigResponse.from_dict(sync_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


