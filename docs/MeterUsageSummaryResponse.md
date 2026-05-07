# MeterUsageSummaryResponse

Response for the multi-meter usage summary endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MeterUsageSummaryItem]**](MeterUsageSummaryItem.md) |  | 

## Example

```python
from moolabs.models.meter_usage_summary_response import MeterUsageSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeterUsageSummaryResponse from a JSON string
meter_usage_summary_response_instance = MeterUsageSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(MeterUsageSummaryResponse.to_json())

# convert the object into a dict
meter_usage_summary_response_dict = meter_usage_summary_response_instance.to_dict()
# create an instance of MeterUsageSummaryResponse from a dict
meter_usage_summary_response_from_dict = MeterUsageSummaryResponse.from_dict(meter_usage_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


