# BillingDiscounts

A discount by type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | [**BillingDiscountPercentage**](BillingDiscountPercentage.md) | The percentage discount. | [optional] 
**usage** | [**BillingDiscountUsage**](BillingDiscountUsage.md) | The usage discount. | [optional] 

## Example

```python
from moolabs.models.billing_discounts import BillingDiscounts

# TODO update the JSON string below
json = "{}"
# create an instance of BillingDiscounts from a JSON string
billing_discounts_instance = BillingDiscounts.from_json(json)
# print the JSON string representation of the object
print(BillingDiscounts.to_json())

# convert the object into a dict
billing_discounts_dict = billing_discounts_instance.to_dict()
# create an instance of BillingDiscounts from a dict
billing_discounts_from_dict = BillingDiscounts.from_dict(billing_discounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


