# AgingReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**as_of** | **datetime** |  | 
**total_outstanding_micros** | **int** |  | 
**total_cases** | **int** |  | 
**buckets** | [**List[AgingBucketDetail]**](AgingBucketDetail.md) |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']

## Example

```python
from moolabs.models.aging_report_response import AgingReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgingReportResponse from a JSON string
aging_report_response_instance = AgingReportResponse.from_json(json)
# print the JSON string representation of the object
print(AgingReportResponse.to_json())

# convert the object into a dict
aging_report_response_dict = aging_report_response_instance.to_dict()
# create an instance of AgingReportResponse from a dict
aging_report_response_from_dict = AgingReportResponse.from_dict(aging_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


