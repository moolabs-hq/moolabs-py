# PaymentAllocationResponse

Single allocation within a payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**payment_id** | **str** |  | 
**invoice_id** | **str** |  | 
**applied_amount_micros** | **int** |  | 
**invoice_currency_code** | **str** |  | 
**settlement_currency_code** | **str** |  | 
**application_source** | **str** |  | [optional] 
**external_application_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from moolabs.models.payment_allocation_response import PaymentAllocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAllocationResponse from a JSON string
payment_allocation_response_instance = PaymentAllocationResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentAllocationResponse.to_json())

# convert the object into a dict
payment_allocation_response_dict = payment_allocation_response_instance.to_dict()
# create an instance of PaymentAllocationResponse from a dict
payment_allocation_response_from_dict = PaymentAllocationResponse.from_dict(payment_allocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


