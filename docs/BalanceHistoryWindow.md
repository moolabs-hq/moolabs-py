# BalanceHistoryWindow

The balance history window.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**Period**](Period.md) |  | 
**usage** | **float** | The total usage of the feature in the period. | [readonly] 
**balance_at_start** | **float** | The entitlement balance at the start of the period. | [readonly] 

## Example

```python
from moolabs.models.balance_history_window import BalanceHistoryWindow

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryWindow from a JSON string
balance_history_window_instance = BalanceHistoryWindow.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryWindow.to_json())

# convert the object into a dict
balance_history_window_dict = balance_history_window_instance.to_dict()
# create an instance of BalanceHistoryWindow from a dict
balance_history_window_from_dict = BalanceHistoryWindow.from_dict(balance_history_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


