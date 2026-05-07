# RecurringPeriod

Recurring period with an interval and an anchor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**RecurringPeriodInterval**](RecurringPeriodInterval.md) | The unit of time for the interval. Heuristically maps ISO duraitons to enum values or returns the ISO duration. | 
**anchor** | **datetime** | A date-time anchor to base the recurring period on. | 
**interval_iso** | **str** | The unit of time for the interval in ISO8601 format. | 

## Example

```python
from moolabs.models.recurring_period import RecurringPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringPeriod from a JSON string
recurring_period_instance = RecurringPeriod.from_json(json)
# print the JSON string representation of the object
print(RecurringPeriod.to_json())

# convert the object into a dict
recurring_period_dict = recurring_period_instance.to_dict()
# create an instance of RecurringPeriod from a dict
recurring_period_from_dict = RecurringPeriod.from_dict(recurring_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


