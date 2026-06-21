# BuyerRequestedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_terms_days** | **int** |  | [optional] 
**term_months** | **int** |  | [optional] 

## Example

```python
from moolabs.models.buyer_requested_changes import BuyerRequestedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerRequestedChanges from a JSON string
buyer_requested_changes_instance = BuyerRequestedChanges.from_json(json)
# print the JSON string representation of the object
print(BuyerRequestedChanges.to_json())

# convert the object into a dict
buyer_requested_changes_dict = buyer_requested_changes_instance.to_dict()
# create an instance of BuyerRequestedChanges from a dict
buyer_requested_changes_from_dict = BuyerRequestedChanges.from_dict(buyer_requested_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


