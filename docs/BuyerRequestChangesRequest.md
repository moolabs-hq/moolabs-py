# BuyerRequestChangesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | 
**requested_changes** | [**BuyerRequestedChanges**](BuyerRequestedChanges.md) |  | [optional] 

## Example

```python
from moolabs.models.buyer_request_changes_request import BuyerRequestChangesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerRequestChangesRequest from a JSON string
buyer_request_changes_request_instance = BuyerRequestChangesRequest.from_json(json)
# print the JSON string representation of the object
print(BuyerRequestChangesRequest.to_json())

# convert the object into a dict
buyer_request_changes_request_dict = buyer_request_changes_request_instance.to_dict()
# create an instance of BuyerRequestChangesRequest from a dict
buyer_request_changes_request_from_dict = BuyerRequestChangesRequest.from_dict(buyer_request_changes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


