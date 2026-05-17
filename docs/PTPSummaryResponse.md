# PTPSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**as_of** | **datetime** |  | 
**open_count** | **int** |  | 
**open_amount_micros** | **int** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']
**due_within_7_days** | **int** |  | 
**overdue_count** | **int** |  | 
**broken_count** | **int** |  | 
**fulfilled_count** | **int** |  | 

## Example

```python
from moolabs.models.ptp_summary_response import PTPSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PTPSummaryResponse from a JSON string
ptp_summary_response_instance = PTPSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(PTPSummaryResponse.to_json())

# convert the object into a dict
ptp_summary_response_dict = ptp_summary_response_instance.to_dict()
# create an instance of PTPSummaryResponse from a dict
ptp_summary_response_from_dict = PTPSummaryResponse.from_dict(ptp_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


