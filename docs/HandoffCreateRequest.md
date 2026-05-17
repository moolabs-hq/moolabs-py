# HandoffCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handoff_type** | **str** |  | 
**partner_name** | **str** |  | 
**commission_bps** | **int** |  | [optional] 

## Example

```python
from moolabs.models.handoff_create_request import HandoffCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HandoffCreateRequest from a JSON string
handoff_create_request_instance = HandoffCreateRequest.from_json(json)
# print the JSON string representation of the object
print(HandoffCreateRequest.to_json())

# convert the object into a dict
handoff_create_request_dict = handoff_create_request_instance.to_dict()
# create an instance of HandoffCreateRequest from a dict
handoff_create_request_from_dict = HandoffCreateRequest.from_dict(handoff_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


