# DashboardOverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aging** | [**AgingReportResponse**](AgingReportResponse.md) |  | 
**dso** | [**DSOResponse**](DSOResponse.md) |  | 
**cei** | [**CEIResponse**](CEIResponse.md) |  | 
**dispute_summary** | [**DisputeSummaryResponse**](DisputeSummaryResponse.md) |  | 
**ptp_summary** | [**PTPSummaryResponse**](PTPSummaryResponse.md) |  | 

## Example

```python
from moolabs.models.dashboard_overview_response import DashboardOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardOverviewResponse from a JSON string
dashboard_overview_response_instance = DashboardOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardOverviewResponse.to_json())

# convert the object into a dict
dashboard_overview_response_dict = dashboard_overview_response_instance.to_dict()
# create an instance of DashboardOverviewResponse from a dict
dashboard_overview_response_from_dict = DashboardOverviewResponse.from_dict(dashboard_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


