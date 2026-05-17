# ReplayDeadLetterRequest

Request body to replay one ingest dead-letter event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Optional tenant override | [optional] 
**pool_id** | **str** | Optional pool override | [optional] 

## Example

```python
from moolabs.models.replay_dead_letter_request import ReplayDeadLetterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayDeadLetterRequest from a JSON string
replay_dead_letter_request_instance = ReplayDeadLetterRequest.from_json(json)
# print the JSON string representation of the object
print(ReplayDeadLetterRequest.to_json())

# convert the object into a dict
replay_dead_letter_request_dict = replay_dead_letter_request_instance.to_dict()
# create an instance of ReplayDeadLetterRequest from a dict
replay_dead_letter_request_from_dict = ReplayDeadLetterRequest.from_dict(replay_dead_letter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


