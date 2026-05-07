# VoidGrantRequest

Request to void a grant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**void_reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.void_grant_request import VoidGrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoidGrantRequest from a JSON string
void_grant_request_instance = VoidGrantRequest.from_json(json)
# print the JSON string representation of the object
print(VoidGrantRequest.to_json())

# convert the object into a dict
void_grant_request_dict = void_grant_request_instance.to_dict()
# create an instance of VoidGrantRequest from a dict
void_grant_request_from_dict = VoidGrantRequest.from_dict(void_grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


