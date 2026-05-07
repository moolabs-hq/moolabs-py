# AutoTopupActivityItem

Single auto-topup activity item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**rule_id** | **str** |  | [optional] 
**wallet_id** | **str** |  | 
**triggered_at** | **datetime** |  | 
**triggered_balance_micros** | **int** |  | [optional] 
**topup_amount_micros** | **int** |  | 
**status** | **str** |  | 
**reference_id** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from moolabs.models.auto_topup_activity_item import AutoTopupActivityItem

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTopupActivityItem from a JSON string
auto_topup_activity_item_instance = AutoTopupActivityItem.from_json(json)
# print the JSON string representation of the object
print(AutoTopupActivityItem.to_json())

# convert the object into a dict
auto_topup_activity_item_dict = auto_topup_activity_item_instance.to_dict()
# create an instance of AutoTopupActivityItem from a dict
auto_topup_activity_item_from_dict = AutoTopupActivityItem.from_dict(auto_topup_activity_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


