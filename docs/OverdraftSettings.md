# OverdraftSettings

Wallet-scoped overdraft / spend policy for this subscription contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_policy** | **str** |  | 
**local_hard_cap_micros** | **int** |  | [optional] 
**grace_period_seconds** | **int** |  | [optional] 
**max_spend_rate_per_hour_micros** | **int** |  | [optional] 

## Example

```python
from moolabs.models.overdraft_settings import OverdraftSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OverdraftSettings from a JSON string
overdraft_settings_instance = OverdraftSettings.from_json(json)
# print the JSON string representation of the object
print(OverdraftSettings.to_json())

# convert the object into a dict
overdraft_settings_dict = overdraft_settings_instance.to_dict()
# create an instance of OverdraftSettings from a dict
overdraft_settings_from_dict = OverdraftSettings.from_dict(overdraft_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


