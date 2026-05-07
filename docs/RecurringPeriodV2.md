# RecurringPeriodV2

Recurring period with an interval and an anchor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**RecurringPeriodInterval**](RecurringPeriodInterval.md) | The unit of time for the interval. Heuristically maps ISO duraitons to enum values or returns the ISO duration. | 
**anchor** | **datetime** | A date-time anchor to base the recurring period on. | 

## Example

```python
from moolabs.models.recurring_period_v2 import RecurringPeriodV2

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringPeriodV2 from a JSON string
recurring_period_v2_instance = RecurringPeriodV2.from_json(json)
# print the JSON string representation of the object
print(RecurringPeriodV2.to_json())

# convert the object into a dict
recurring_period_v2_dict = recurring_period_v2_instance.to_dict()
# create an instance of RecurringPeriodV2 from a dict
recurring_period_v2_from_dict = RecurringPeriodV2.from_dict(recurring_period_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


