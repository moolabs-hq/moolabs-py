# CostEventSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CostEventSummaryItem]**](CostEventSummaryItem.md) |  | 

## Example

```python
from moolabs.models.cost_event_summary_response import CostEventSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CostEventSummaryResponse from a JSON string
cost_event_summary_response_instance = CostEventSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(CostEventSummaryResponse.to_json())

# convert the object into a dict
cost_event_summary_response_dict = cost_event_summary_response_instance.to_dict()
# create an instance of CostEventSummaryResponse from a dict
cost_event_summary_response_from_dict = CostEventSummaryResponse.from_dict(cost_event_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


