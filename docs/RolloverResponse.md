# RolloverResponse

Response from period-close rollover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** |  | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**grants_processed** | **int** |  | 
**rollover_amount_micros** | **int** |  | 
**rollover_grants_created** | **List[str]** |  | 

## Example

```python
from moolabs.models.rollover_response import RolloverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RolloverResponse from a JSON string
rollover_response_instance = RolloverResponse.from_json(json)
# print the JSON string representation of the object
print(RolloverResponse.to_json())

# convert the object into a dict
rollover_response_dict = rollover_response_instance.to_dict()
# create an instance of RolloverResponse from a dict
rollover_response_from_dict = RolloverResponse.from_dict(rollover_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


