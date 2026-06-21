# CostEventSummaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_event_ids** | **List[str]** |  | 

## Example

```python
from moolabs.models.cost_event_summary_request import CostEventSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CostEventSummaryRequest from a JSON string
cost_event_summary_request_instance = CostEventSummaryRequest.from_json(json)
# print the JSON string representation of the object
print(CostEventSummaryRequest.to_json())

# convert the object into a dict
cost_event_summary_request_dict = cost_event_summary_request_instance.to_dict()
# create an instance of CostEventSummaryRequest from a dict
cost_event_summary_request_from_dict = CostEventSummaryRequest.from_dict(cost_event_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


