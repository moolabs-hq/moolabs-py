# TriggerResponse

Response from trigger check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triggered** | **bool** |  | 
**reason** | **str** |  | [optional] 
**rule_id** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**topup_amount_micros** | **int** |  | [optional] 
**payment_method_ref** | **str** |  | [optional] 
**invoice_mode** | **str** |  | [optional] 
**outbox_event_id** | **str** |  | [optional] 
**cooldown_until** | **datetime** |  | [optional] 
**wallet_state** | **str** |  | [optional] 
**available_balance_micros** | **int** |  | [optional] 

## Example

```python
from moolabs.models.trigger_response import TriggerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerResponse from a JSON string
trigger_response_instance = TriggerResponse.from_json(json)
# print the JSON string representation of the object
print(TriggerResponse.to_json())

# convert the object into a dict
trigger_response_dict = trigger_response_instance.to_dict()
# create an instance of TriggerResponse from a dict
trigger_response_from_dict = TriggerResponse.from_dict(trigger_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


