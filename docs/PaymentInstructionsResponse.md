# PaymentInstructionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **bool** |  | 
**payment_instructions_text** | **str** |  | [optional] 
**payment_instructions_hash** | **str** |  | 
**updated_by_actor_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from moolabs.models.payment_instructions_response import PaymentInstructionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstructionsResponse from a JSON string
payment_instructions_response_instance = PaymentInstructionsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentInstructionsResponse.to_json())

# convert the object into a dict
payment_instructions_response_dict = payment_instructions_response_instance.to_dict()
# create an instance of PaymentInstructionsResponse from a dict
payment_instructions_response_from_dict = PaymentInstructionsResponse.from_dict(payment_instructions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


