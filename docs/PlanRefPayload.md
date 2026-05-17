# PlanRefPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from moolabs.models.plan_ref_payload import PlanRefPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlanRefPayload from a JSON string
plan_ref_payload_instance = PlanRefPayload.from_json(json)
# print the JSON string representation of the object
print(PlanRefPayload.to_json())

# convert the object into a dict
plan_ref_payload_dict = plan_ref_payload_instance.to_dict()
# create an instance of PlanRefPayload from a dict
plan_ref_payload_from_dict = PlanRefPayload.from_dict(plan_ref_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


