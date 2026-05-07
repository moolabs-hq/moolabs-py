# PaymentTermInstant

PaymentTermInstant defines the terms for payment on receipt of invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of terms to be applied. | 
**detail** | **str** | Text detail of the chosen payment terms. | [optional] [readonly] 
**notes** | **str** | Description of the conditions for payment. | [optional] [readonly] 

## Example

```python
from moolabs.models.payment_term_instant import PaymentTermInstant

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTermInstant from a JSON string
payment_term_instant_instance = PaymentTermInstant.from_json(json)
# print the JSON string representation of the object
print(PaymentTermInstant.to_json())

# convert the object into a dict
payment_term_instant_dict = payment_term_instant_instance.to_dict()
# create an instance of PaymentTermInstant from a dict
payment_term_instant_from_dict = PaymentTermInstant.from_dict(payment_term_instant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


