# BuyerRejectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.buyer_reject_request import BuyerRejectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerRejectRequest from a JSON string
buyer_reject_request_instance = BuyerRejectRequest.from_json(json)
# print the JSON string representation of the object
print(BuyerRejectRequest.to_json())

# convert the object into a dict
buyer_reject_request_dict = buyer_reject_request_instance.to_dict()
# create an instance of BuyerRejectRequest from a dict
buyer_reject_request_from_dict = BuyerRejectRequest.from_dict(buyer_reject_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


