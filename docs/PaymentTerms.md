# PaymentTerms

PaymentTerms defines the terms for payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of terms to be applied. | 
**detail** | **str** | Text detail of the chosen payment terms. | [optional] [readonly] 
**notes** | **str** | Description of the conditions for payment. | [optional] [readonly] 
**due_at** | [**List[PaymentDueDate]**](PaymentDueDate.md) | When the payment is due. | 

## Example

```python
from moolabs.models.payment_terms import PaymentTerms

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTerms from a JSON string
payment_terms_instance = PaymentTerms.from_json(json)
# print the JSON string representation of the object
print(PaymentTerms.to_json())

# convert the object into a dict
payment_terms_dict = payment_terms_instance.to_dict()
# create an instance of PaymentTerms from a dict
payment_terms_from_dict = PaymentTerms.from_dict(payment_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


