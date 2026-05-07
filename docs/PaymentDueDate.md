# PaymentDueDate

PaymentDueDate contains an amount that should be paid by the given date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_at** | **datetime** | When the payment is due. | [readonly] 
**notes** | **str** | Other details to take into account for the due date. | [optional] [readonly] 
**amount** | **str** | How much needs to be paid by the date. | [readonly] 
**percent** | **float** | Percentage of the total that should be paid by the date. | [optional] [readonly] 
**currency** | **str** | If different from the parent document&#39;s base currency. | [optional] [readonly] 

## Example

```python
from moolabs.models.payment_due_date import PaymentDueDate

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDueDate from a JSON string
payment_due_date_instance = PaymentDueDate.from_json(json)
# print the JSON string representation of the object
print(PaymentDueDate.to_json())

# convert the object into a dict
payment_due_date_dict = payment_due_date_instance.to_dict()
# create an instance of PaymentDueDate from a dict
payment_due_date_from_dict = PaymentDueDate.from_dict(payment_due_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


