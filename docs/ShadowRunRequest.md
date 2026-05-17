# ShadowRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant UUID | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 

## Example

```python
from moolabs.models.shadow_run_request import ShadowRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShadowRunRequest from a JSON string
shadow_run_request_instance = ShadowRunRequest.from_json(json)
# print the JSON string representation of the object
print(ShadowRunRequest.to_json())

# convert the object into a dict
shadow_run_request_dict = shadow_run_request_instance.to_dict()
# create an instance of ShadowRunRequest from a dict
shadow_run_request_from_dict = ShadowRunRequest.from_dict(shadow_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


