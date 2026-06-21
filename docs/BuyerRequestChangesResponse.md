# BuyerRequestChangesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**redline_id** | **str** |  | 
**quote_id** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from moolabs.models.buyer_request_changes_response import BuyerRequestChangesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerRequestChangesResponse from a JSON string
buyer_request_changes_response_instance = BuyerRequestChangesResponse.from_json(json)
# print the JSON string representation of the object
print(BuyerRequestChangesResponse.to_json())

# convert the object into a dict
buyer_request_changes_response_dict = buyer_request_changes_response_instance.to_dict()
# create an instance of BuyerRequestChangesResponse from a dict
buyer_request_changes_response_from_dict = BuyerRequestChangesResponse.from_dict(buyer_request_changes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


