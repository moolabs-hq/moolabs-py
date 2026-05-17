# CreateValueRecognitionRequest

Request to create a VALUE_RECOGNITION journal entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**wallet_id** | **str** | Wallet identifier | 
**subject_id** | **str** | Subject identifier | 
**usd_amount_micros** | **int** | USD amount in micros | 
**effective_at** | **datetime** | Effective timestamp | 
**usage_event_id** | **str** | Usage event ID | [optional] 

## Example

```python
from moolabs.models.create_value_recognition_request import CreateValueRecognitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateValueRecognitionRequest from a JSON string
create_value_recognition_request_instance = CreateValueRecognitionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateValueRecognitionRequest.to_json())

# convert the object into a dict
create_value_recognition_request_dict = create_value_recognition_request_instance.to_dict()
# create an instance of CreateValueRecognitionRequest from a dict
create_value_recognition_request_from_dict = CreateValueRecognitionRequest.from_dict(create_value_recognition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


