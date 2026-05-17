# DeriveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant UUID | 
**feature_key** | **str** |  | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 

## Example

```python
from moolabs.models.derive_request import DeriveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveRequest from a JSON string
derive_request_instance = DeriveRequest.from_json(json)
# print the JSON string representation of the object
print(DeriveRequest.to_json())

# convert the object into a dict
derive_request_dict = derive_request_instance.to_dict()
# create an instance of DeriveRequest from a dict
derive_request_from_dict = DeriveRequest.from_dict(derive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


