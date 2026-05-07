# PaymentTermDueDate

PaymentTermDueDate defines the terms for payment on a specific date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of terms to be applied. | 
**detail** | **str** | Text detail of the chosen payment terms. | [optional] [readonly] 
**notes** | **str** | Description of the conditions for payment. | [optional] [readonly] 
**due_at** | [**List[PaymentDueDate]**](PaymentDueDate.md) | When the payment is due. | 

## Example

```python
from moolabs.models.payment_term_due_date import PaymentTermDueDate

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTermDueDate from a JSON string
payment_term_due_date_instance = PaymentTermDueDate.from_json(json)
# print the JSON string representation of the object
print(PaymentTermDueDate.to_json())

# convert the object into a dict
payment_term_due_date_dict = payment_term_due_date_instance.to_dict()
# create an instance of PaymentTermDueDate from a dict
payment_term_due_date_from_dict = PaymentTermDueDate.from_dict(payment_term_due_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


