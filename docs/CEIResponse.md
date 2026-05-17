# CEIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**as_of** | **datetime** |  | 
**cei_percentage** | **float** |  | 
**beginning_receivables_micros** | **int** |  | 
**ending_receivables_micros** | **int** |  | 
**credit_sales_micros** | **int** |  | 
**cash_receipts_micros** | **int** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']

## Example

```python
from moolabs.models.cei_response import CEIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CEIResponse from a JSON string
cei_response_instance = CEIResponse.from_json(json)
# print the JSON string representation of the object
print(CEIResponse.to_json())

# convert the object into a dict
cei_response_dict = cei_response_instance.to_dict()
# create an instance of CEIResponse from a dict
cei_response_from_dict = CEIResponse.from_dict(cei_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


