# UpdateWalletSettingsRequest

Request to update wallet settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_wallet_id** | **str** | Parent wallet ID. Set to null to detach from hierarchy. | [optional] 
**local_hard_cap_micros** | **int** | Local hard cap (micros). Set to null to remove override. | [optional] 
**policy** | [**WalletPolicy**](WalletPolicy.md) | Wallet policy (SOFT_BORROW, HARD_BUDGET, NOTIFY_ONLY) | [optional] 
**audit_note** | **str** | Audit note for this change | [optional] 

## Example

```python
from moolabs.models.update_wallet_settings_request import UpdateWalletSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWalletSettingsRequest from a JSON string
update_wallet_settings_request_instance = UpdateWalletSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWalletSettingsRequest.to_json())

# convert the object into a dict
update_wallet_settings_request_dict = update_wallet_settings_request_instance.to_dict()
# create an instance of UpdateWalletSettingsRequest from a dict
update_wallet_settings_request_from_dict = UpdateWalletSettingsRequest.from_dict(update_wallet_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


