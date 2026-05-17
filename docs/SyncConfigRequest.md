# SyncConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** |  | 
**schedule** | **str** |  | [optional] [default to '0 6 * * *']

## Example

```python
from moolabs.models.sync_config_request import SyncConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncConfigRequest from a JSON string
sync_config_request_instance = SyncConfigRequest.from_json(json)
# print the JSON string representation of the object
print(SyncConfigRequest.to_json())

# convert the object into a dict
sync_config_request_dict = sync_config_request_instance.to_dict()
# create an instance of SyncConfigRequest from a dict
sync_config_request_from_dict = SyncConfigRequest.from_dict(sync_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


