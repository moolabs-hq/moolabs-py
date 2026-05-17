# OverdraftSettingsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_policy** | **str** |  | 
**local_hard_cap_micros** | **int** |  | [optional] 
**grace_period_seconds** | **int** |  | [optional] 
**max_spend_rate_per_hour_micros** | **int** |  | [optional] 

## Example

```python
from moolabs.models.overdraft_settings_payload import OverdraftSettingsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OverdraftSettingsPayload from a JSON string
overdraft_settings_payload_instance = OverdraftSettingsPayload.from_json(json)
# print the JSON string representation of the object
print(OverdraftSettingsPayload.to_json())

# convert the object into a dict
overdraft_settings_payload_dict = overdraft_settings_payload_instance.to_dict()
# create an instance of OverdraftSettingsPayload from a dict
overdraft_settings_payload_from_dict = OverdraftSettingsPayload.from_dict(overdraft_settings_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


