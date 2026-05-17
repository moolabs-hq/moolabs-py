# BatchWalletStateRequest

Request to get states for multiple wallets in a single call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallets** | [**List[BatchWalletStateRequestItem]**](BatchWalletStateRequestItem.md) | List of wallet identifiers | 
**effective_as_of** | **datetime** | Effective as-of timestamp (business time) for time travel | [optional] 
**recorded_as_of** | **datetime** | Recorded as-of timestamp (system time) for time travel | [optional] 
**consistent_view** | **bool** | Use strong consistency for reads | [optional] [default to False]
**consistency** | **str** | Consistency level: &#39;eventual&#39; or &#39;STRONG&#39; | [optional] [default to 'eventual']

## Example

```python
from moolabs.models.batch_wallet_state_request import BatchWalletStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWalletStateRequest from a JSON string
batch_wallet_state_request_instance = BatchWalletStateRequest.from_json(json)
# print the JSON string representation of the object
print(BatchWalletStateRequest.to_json())

# convert the object into a dict
batch_wallet_state_request_dict = batch_wallet_state_request_instance.to_dict()
# create an instance of BatchWalletStateRequest from a dict
batch_wallet_state_request_from_dict = BatchWalletStateRequest.from_dict(batch_wallet_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


