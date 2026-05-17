# DisputeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispute_type** | **str** |  | [optional] 
**classification_status** | **str** |  | [optional] 
**accounting_class** | **str** |  | [optional] 
**accounting_reason_code** | **str** |  | [optional] 
**external_dispute_id** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**resolution_deadline** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from moolabs.models.dispute_update_request import DisputeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeUpdateRequest from a JSON string
dispute_update_request_instance = DisputeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DisputeUpdateRequest.to_json())

# convert the object into a dict
dispute_update_request_dict = dispute_update_request_instance.to_dict()
# create an instance of DisputeUpdateRequest from a dict
dispute_update_request_from_dict = DisputeUpdateRequest.from_dict(dispute_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


