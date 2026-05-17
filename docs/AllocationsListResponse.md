# AllocationsListResponse

GET /payments/{id}/allocations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PaymentAllocationResponse]**](PaymentAllocationResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from moolabs.models.allocations_list_response import AllocationsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationsListResponse from a JSON string
allocations_list_response_instance = AllocationsListResponse.from_json(json)
# print the JSON string representation of the object
print(AllocationsListResponse.to_json())

# convert the object into a dict
allocations_list_response_dict = allocations_list_response_instance.to_dict()
# create an instance of AllocationsListResponse from a dict
allocations_list_response_from_dict = AllocationsListResponse.from_dict(allocations_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


