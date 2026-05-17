# OverviewResponse

Aggregate overview for the OverviewPage UI.  The UI's `OverviewPage.tsx` reads multiple field aliases via `numberValue` / `stringValue` helpers, so we emit snake_case names matching the primary aliases the UI looks for (total_spend, requests, reconciled_percent, observation_status). Empty data is returned as zeros + null reconciliation so the four KPI cards render gracefully on a fresh tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**total_spend** | **float** |  | 
**requests** | **int** |  | 
**reconciled_percent** | **float** |  | 
**observation_status** | **str** |  | 
**ingest_health** | [**IngestHealth**](IngestHealth.md) |  | 

## Example

```python
from moolabs.models.overview_response import OverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewResponse from a JSON string
overview_response_instance = OverviewResponse.from_json(json)
# print the JSON string representation of the object
print(OverviewResponse.to_json())

# convert the object into a dict
overview_response_dict = overview_response_instance.to_dict()
# create an instance of OverviewResponse from a dict
overview_response_from_dict = OverviewResponse.from_dict(overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


