# TestSendResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**recipient_email** | **str** |  | 
**version_id** | **str** |  | 

## Example

```python
from moolabs.models.test_send_response import TestSendResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestSendResponse from a JSON string
test_send_response_instance = TestSendResponse.from_json(json)
# print the JSON string representation of the object
print(TestSendResponse.to_json())

# convert the object into a dict
test_send_response_dict = test_send_response_instance.to_dict()
# create an instance of TestSendResponse from a dict
test_send_response_from_dict = TestSendResponse.from_dict(test_send_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


