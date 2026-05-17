# UpdateWalletThresholdsRequest

Request to update wallet thresholds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_soft_threshold_micros** | **int** | Local soft threshold (micros). Set to null to remove override. | [optional] 
**local_hard_cap_micros** | **int** | Local hard cap (micros). Set to null to remove override. | [optional] 
**audit_note** | **str** | Audit note for this change | [optional] 

## Example

```python
from moolabs.models.update_wallet_thresholds_request import UpdateWalletThresholdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWalletThresholdsRequest from a JSON string
update_wallet_thresholds_request_instance = UpdateWalletThresholdsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWalletThresholdsRequest.to_json())

# convert the object into a dict
update_wallet_thresholds_request_dict = update_wallet_thresholds_request_instance.to_dict()
# create an instance of UpdateWalletThresholdsRequest from a dict
update_wallet_thresholds_request_from_dict = UpdateWalletThresholdsRequest.from_dict(update_wallet_thresholds_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


