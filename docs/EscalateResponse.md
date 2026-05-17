# EscalateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steering_event_id** | **str** |  | 
**escalation_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from moolabs.models.escalate_response import EscalateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EscalateResponse from a JSON string
escalate_response_instance = EscalateResponse.from_json(json)
# print the JSON string representation of the object
print(EscalateResponse.to_json())

# convert the object into a dict
escalate_response_dict = escalate_response_instance.to_dict()
# create an instance of EscalateResponse from a dict
escalate_response_from_dict = EscalateResponse.from_dict(escalate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


