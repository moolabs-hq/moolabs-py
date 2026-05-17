# BatchWalletStateResponse

Batch wallet state response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | [**List[WalletStateResponse]**](WalletStateResponse.md) | List of wallet states | 
**errors** | **List[Dict[str, object]]** | List of errors for wallets that failed | [optional] 

## Example

```python
from moolabs.models.batch_wallet_state_response import BatchWalletStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWalletStateResponse from a JSON string
batch_wallet_state_response_instance = BatchWalletStateResponse.from_json(json)
# print the JSON string representation of the object
print(BatchWalletStateResponse.to_json())

# convert the object into a dict
batch_wallet_state_response_dict = batch_wallet_state_response_instance.to_dict()
# create an instance of BatchWalletStateResponse from a dict
batch_wallet_state_response_from_dict = BatchWalletStateResponse.from_dict(batch_wallet_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


