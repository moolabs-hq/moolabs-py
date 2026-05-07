# BillingDiscountUsage

A usage discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** | The quantity of the usage discount.  Must be positive. | 
**correlation_id** | **str** | Correlation ID for the discount.  This is used to link discounts across different invoices (progressive billing use case).  If not provided, the invoicing engine will auto-generate one. When editing an invoice line, please make sure to keep the same correlation ID of the discount or in progressive billing setups the discount amounts might be incorrect. | [optional] 

## Example

```python
from moolabs.models.billing_discount_usage import BillingDiscountUsage

# TODO update the JSON string below
json = "{}"
# create an instance of BillingDiscountUsage from a JSON string
billing_discount_usage_instance = BillingDiscountUsage.from_json(json)
# print the JSON string representation of the object
print(BillingDiscountUsage.to_json())

# convert the object into a dict
billing_discount_usage_dict = billing_discount_usage_instance.to_dict()
# create an instance of BillingDiscountUsage from a dict
billing_discount_usage_from_dict = BillingDiscountUsage.from_dict(billing_discount_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


