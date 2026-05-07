# UpdateWalletSettingsRequest

Request to update wallet settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_wallet_id** | **str** |  | [optional] 
**local_hard_cap_micros** | **int** |  | [optional] 
**policy** | [**WalletPolicy**](WalletPolicy.md) |  | [optional] 
**audit_note** | **str** |  | [optional] 

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


