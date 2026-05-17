# BatchWalletStateRequestItem

Single wallet state request item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Credit pool identifier | 
**wallet_id** | **str** | Wallet identifier | 

## Example

```python
from moolabs.models.batch_wallet_state_request_item import BatchWalletStateRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWalletStateRequestItem from a JSON string
batch_wallet_state_request_item_instance = BatchWalletStateRequestItem.from_json(json)
# print the JSON string representation of the object
print(BatchWalletStateRequestItem.to_json())

# convert the object into a dict
batch_wallet_state_request_item_dict = batch_wallet_state_request_item_instance.to_dict()
# create an instance of BatchWalletStateRequestItem from a dict
batch_wallet_state_request_item_from_dict = BatchWalletStateRequestItem.from_dict(batch_wallet_state_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


