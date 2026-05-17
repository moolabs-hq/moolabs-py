# RolloverRequest

Request to process period-close rollover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**subscription_id** | **str** | Subscription identifier | 
**period_end** | **datetime** | Period end timestamp (defaults to now) | [optional] 
**grace_window_seconds** | **int** | Grace window in seconds | [optional] [default to 3600]

## Example

```python
from moolabs.models.rollover_request import RolloverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RolloverRequest from a JSON string
rollover_request_instance = RolloverRequest.from_json(json)
# print the JSON string representation of the object
print(RolloverRequest.to_json())

# convert the object into a dict
rollover_request_dict = rollover_request_instance.to_dict()
# create an instance of RolloverRequest from a dict
rollover_request_from_dict = RolloverRequest.from_dict(rollover_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


