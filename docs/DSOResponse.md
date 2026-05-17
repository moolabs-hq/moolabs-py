# DSOResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**as_of** | **datetime** |  | 
**dso_days** | **float** |  | 
**total_outstanding_micros** | **int** |  | 
**total_revenue_micros** | **int** |  | 
**period_days** | **int** |  | [optional] [default to 90]
**currency_code** | **str** |  | [optional] [default to 'USD']

## Example

```python
from moolabs.models.dso_response import DSOResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DSOResponse from a JSON string
dso_response_instance = DSOResponse.from_json(json)
# print the JSON string representation of the object
print(DSOResponse.to_json())

# convert the object into a dict
dso_response_dict = dso_response_instance.to_dict()
# create an instance of DSOResponse from a dict
dso_response_from_dict = DSOResponse.from_dict(dso_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


