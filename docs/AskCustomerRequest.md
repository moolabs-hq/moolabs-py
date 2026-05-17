# AskCustomerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing_field** | **str** |  | 
**context** | **str** |  | [optional] 

## Example

```python
from moolabs.models.ask_customer_request import AskCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AskCustomerRequest from a JSON string
ask_customer_request_instance = AskCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(AskCustomerRequest.to_json())

# convert the object into a dict
ask_customer_request_dict = ask_customer_request_instance.to_dict()
# create an instance of AskCustomerRequest from a dict
ask_customer_request_from_dict = AskCustomerRequest.from_dict(ask_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


