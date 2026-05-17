# RevenueRecognitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**reporting_currency** | **str** |  | [optional] 

## Example

```python
from moolabs.models.revenue_recognition_request import RevenueRecognitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueRecognitionRequest from a JSON string
revenue_recognition_request_instance = RevenueRecognitionRequest.from_json(json)
# print the JSON string representation of the object
print(RevenueRecognitionRequest.to_json())

# convert the object into a dict
revenue_recognition_request_dict = revenue_recognition_request_instance.to_dict()
# create an instance of RevenueRecognitionRequest from a dict
revenue_recognition_request_from_dict = RevenueRecognitionRequest.from_dict(revenue_recognition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


