# FlagDisputedRequest

POST /cases/{id}/invoices/{inv_id}/flag-disputed — Phase 1 placeholder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disputed_amount_micros** | **int** |  | 
**description** | **str** |  | 
**dispute_type** | **str** | Dispute type for classification | [optional] [default to 'admin']

## Example

```python
from moolabs.models.flag_disputed_request import FlagDisputedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlagDisputedRequest from a JSON string
flag_disputed_request_instance = FlagDisputedRequest.from_json(json)
# print the JSON string representation of the object
print(FlagDisputedRequest.to_json())

# convert the object into a dict
flag_disputed_request_dict = flag_disputed_request_instance.to_dict()
# create an instance of FlagDisputedRequest from a dict
flag_disputed_request_from_dict = FlagDisputedRequest.from_dict(flag_disputed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


