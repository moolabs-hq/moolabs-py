# DisputeSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**as_of** | **datetime** |  | 
**total_disputes** | **int** |  | 
**open_disputes** | **int** |  | 
**total_disputed_micros** | **int** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']
**resolved_valid** | **int** |  | 
**resolved_invalid** | **int** |  | 
**avg_resolution_days** | **float** |  | [optional] 

## Example

```python
from moolabs.models.dispute_summary_response import DisputeSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeSummaryResponse from a JSON string
dispute_summary_response_instance = DisputeSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(DisputeSummaryResponse.to_json())

# convert the object into a dict
dispute_summary_response_dict = dispute_summary_response_instance.to_dict()
# create an instance of DisputeSummaryResponse from a dict
dispute_summary_response_from_dict = DisputeSummaryResponse.from_dict(dispute_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


