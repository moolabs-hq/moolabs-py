# TestSendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** |  | 
**mode** | **str** |  | [optional] 
**case_id** | **str** |  | [optional] 
**recipient_email** | **str** |  | 

## Example

```python
from moolabs.models.test_send_request import TestSendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestSendRequest from a JSON string
test_send_request_instance = TestSendRequest.from_json(json)
# print the JSON string representation of the object
print(TestSendRequest.to_json())

# convert the object into a dict
test_send_request_dict = test_send_request_instance.to_dict()
# create an instance of TestSendRequest from a dict
test_send_request_from_dict = TestSendRequest.from_dict(test_send_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


