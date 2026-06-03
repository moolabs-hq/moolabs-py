# PaymentInstructionsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_instructions_text** | **str** |  | 
**change_reason** | **str** |  | 

## Example

```python
from moolabs.models.payment_instructions_update_request import PaymentInstructionsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstructionsUpdateRequest from a JSON string
payment_instructions_update_request_instance = PaymentInstructionsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentInstructionsUpdateRequest.to_json())

# convert the object into a dict
payment_instructions_update_request_dict = payment_instructions_update_request_instance.to_dict()
# create an instance of PaymentInstructionsUpdateRequest from a dict
payment_instructions_update_request_from_dict = PaymentInstructionsUpdateRequest.from_dict(payment_instructions_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


