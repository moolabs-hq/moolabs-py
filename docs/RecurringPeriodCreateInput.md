# RecurringPeriodCreateInput

Recurring period with an interval and an anchor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**RecurringPeriodInterval**](RecurringPeriodInterval.md) | The unit of time for the interval. | 
**anchor** | **datetime** | A date-time anchor to base the recurring period on. | [optional] 

## Example

```python
from moolabs.models.recurring_period_create_input import RecurringPeriodCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringPeriodCreateInput from a JSON string
recurring_period_create_input_instance = RecurringPeriodCreateInput.from_json(json)
# print the JSON string representation of the object
print(RecurringPeriodCreateInput.to_json())

# convert the object into a dict
recurring_period_create_input_dict = recurring_period_create_input_instance.to_dict()
# create an instance of RecurringPeriodCreateInput from a dict
recurring_period_create_input_from_dict = RecurringPeriodCreateInput.from_dict(recurring_period_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


