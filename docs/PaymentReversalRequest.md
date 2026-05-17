# PaymentReversalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reversal_type** | **str** | chargeback, nsf, ach_return, refund, correction | [optional] [default to 'correction']
**reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.payment_reversal_request import PaymentReversalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReversalRequest from a JSON string
payment_reversal_request_instance = PaymentReversalRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentReversalRequest.to_json())

# convert the object into a dict
payment_reversal_request_dict = payment_reversal_request_instance.to_dict()
# create an instance of PaymentReversalRequest from a dict
payment_reversal_request_from_dict = PaymentReversalRequest.from_dict(payment_reversal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


