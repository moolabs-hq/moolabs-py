# ProcessValueRecognitionRequest

Request to process burn allocations for value recognition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**journal_entry_id** | **str** | Journal entry ID to process | 
**effective_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.process_value_recognition_request import ProcessValueRecognitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessValueRecognitionRequest from a JSON string
process_value_recognition_request_instance = ProcessValueRecognitionRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessValueRecognitionRequest.to_json())

# convert the object into a dict
process_value_recognition_request_dict = process_value_recognition_request_instance.to_dict()
# create an instance of ProcessValueRecognitionRequest from a dict
process_value_recognition_request_from_dict = ProcessValueRecognitionRequest.from_dict(process_value_recognition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


