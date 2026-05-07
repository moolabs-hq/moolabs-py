# AllocateCreditsRequest

Request to allocate credits from source to target wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_wallet_id** | **str** |  | 
**target_wallet_id** | **str** |  | 
**amount_micros** | **int** | Amount in micros to transfer | 
**subject_id** | **str** | Subject performing the allocation (for audit) | 
**reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.allocate_credits_request import AllocateCreditsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AllocateCreditsRequest from a JSON string
allocate_credits_request_instance = AllocateCreditsRequest.from_json(json)
# print the JSON string representation of the object
print(AllocateCreditsRequest.to_json())

# convert the object into a dict
allocate_credits_request_dict = allocate_credits_request_instance.to_dict()
# create an instance of AllocateCreditsRequest from a dict
allocate_credits_request_from_dict = AllocateCreditsRequest.from_dict(allocate_credits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


