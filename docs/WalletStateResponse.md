# WalletStateResponse

Wallet state response (matches get_wallet_state return format).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** |  | 
**pool_id** | **str** |  | 
**balance_micros** | **int** |  | 
**balance_decimal** | **float** |  | 
**effective_available_micros** | **int** |  | [optional] 
**state** | **str** |  | 
**as_of** | **str** |  | 
**consistency** | **str** |  | 
**last_projected_at** | **str** |  | [optional] 
**projected_from_recorded_cut** | **str** |  | [optional] 

## Example

```python
from moolabs.models.wallet_state_response import WalletStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletStateResponse from a JSON string
wallet_state_response_instance = WalletStateResponse.from_json(json)
# print the JSON string representation of the object
print(WalletStateResponse.to_json())

# convert the object into a dict
wallet_state_response_dict = wallet_state_response_instance.to_dict()
# create an instance of WalletStateResponse from a dict
wallet_state_response_from_dict = WalletStateResponse.from_dict(wallet_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


