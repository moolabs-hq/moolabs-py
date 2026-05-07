# ValueRecognitionResponse

Response from value recognition processing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_entry_id** | **str** |  | 
**burn_allocations_processed** | **int** |  | 
**total_usd_micros** | **int** |  | 
**postings_created** | **List[str]** |  | 

## Example

```python
from moolabs.models.value_recognition_response import ValueRecognitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValueRecognitionResponse from a JSON string
value_recognition_response_instance = ValueRecognitionResponse.from_json(json)
# print the JSON string representation of the object
print(ValueRecognitionResponse.to_json())

# convert the object into a dict
value_recognition_response_dict = value_recognition_response_instance.to_dict()
# create an instance of ValueRecognitionResponse from a dict
value_recognition_response_from_dict = ValueRecognitionResponse.from_dict(value_recognition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


