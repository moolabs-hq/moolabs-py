# WindowedBalanceHistory

The windowed balance history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**windowed_history** | [**List[BalanceHistoryWindow]**](BalanceHistoryWindow.md) | The windowed balance history. - It only returns rows for windows where there was usage. - The windows are inclusive at their start and exclusive at their end. - The last window may be smaller than the window size and is inclusive at both ends. | 
**burndown_history** | [**List[GrantBurnDownHistorySegment]**](GrantBurnDownHistorySegment.md) | Grant burndown history. | 

## Example

```python
from moolabs.models.windowed_balance_history import WindowedBalanceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of WindowedBalanceHistory from a JSON string
windowed_balance_history_instance = WindowedBalanceHistory.from_json(json)
# print the JSON string representation of the object
print(WindowedBalanceHistory.to_json())

# convert the object into a dict
windowed_balance_history_dict = windowed_balance_history_instance.to_dict()
# create an instance of WindowedBalanceHistory from a dict
windowed_balance_history_from_dict = WindowedBalanceHistory.from_dict(windowed_balance_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


