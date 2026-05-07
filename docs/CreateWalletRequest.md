# CreateWalletRequest

Request to create a wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Credit pool identifier | 
**owner_type** | [**WalletOwnerType**](WalletOwnerType.md) | Owner type (ORG, TEAM, USER, etc.) | 
**owner_id** | **str** | Owner identifier | 
**parent_wallet_id** | **str** |  | [optional] 
**depth** | **int** | Hierarchy depth (0-3) | [optional] [default to 0]
**policy** | [**WalletPolicy**](WalletPolicy.md) | Wallet policy | [optional] 
**local_hard_cap_micros** | **int** |  | [optional] 
**local_soft_threshold_micros** | **int** |  | [optional] 

## Example

```python
from moolabs.models.create_wallet_request import CreateWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletRequest from a JSON string
create_wallet_request_instance = CreateWalletRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWalletRequest.to_json())

# convert the object into a dict
create_wallet_request_dict = create_wallet_request_instance.to_dict()
# create an instance of CreateWalletRequest from a dict
create_wallet_request_from_dict = CreateWalletRequest.from_dict(create_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


