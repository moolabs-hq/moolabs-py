# AskCustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steering_event_id** | **str** |  | 
**child_task_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from moolabs.models.ask_customer_response import AskCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AskCustomerResponse from a JSON string
ask_customer_response_instance = AskCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(AskCustomerResponse.to_json())

# convert the object into a dict
ask_customer_response_dict = ask_customer_response_instance.to_dict()
# create an instance of AskCustomerResponse from a dict
ask_customer_response_from_dict = AskCustomerResponse.from_dict(ask_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


