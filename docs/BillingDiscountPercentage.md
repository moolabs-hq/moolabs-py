# BillingDiscountPercentage

A percentage discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **float** | The percentage of the discount. | 
**correlation_id** | **str** | Correlation ID for the discount.  This is used to link discounts across different invoices (progressive billing use case).  If not provided, the invoicing engine will auto-generate one. When editing an invoice line, please make sure to keep the same correlation ID of the discount or in progressive billing setups the discount amounts might be incorrect. | [optional] 

## Example

```python
from moolabs.models.billing_discount_percentage import BillingDiscountPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of BillingDiscountPercentage from a JSON string
billing_discount_percentage_instance = BillingDiscountPercentage.from_json(json)
# print the JSON string representation of the object
print(BillingDiscountPercentage.to_json())

# convert the object into a dict
billing_discount_percentage_dict = billing_discount_percentage_instance.to_dict()
# create an instance of BillingDiscountPercentage from a dict
billing_discount_percentage_from_dict = BillingDiscountPercentage.from_dict(billing_discount_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


