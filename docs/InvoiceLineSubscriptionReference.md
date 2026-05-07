# InvoiceLineSubscriptionReference

InvoiceLineSubscriptionReference contains the references to the subscription that this line is related to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**IDResource**](IDResource.md) | The subscription. | [readonly] 
**phase** | [**IDResource**](IDResource.md) | The phase of the subscription. | [readonly] 
**item** | [**IDResource**](IDResource.md) | The item this line is related to. | [readonly] 
**billing_period** | [**Period**](Period.md) | The billing period of the subscription. In case the subscription item&#39;s billing period is different from the subscription&#39;s billing period, this field will contain the billing period of the subscription itself.  For example, in case of: - A monthly billed subscription anchored to 2025-01-01 - A subscription item billed daily  An example line would have the period of 2025-01-02 to 2025-01-03 as the item is billed daily, but the subscription&#39;s billing period will be 2025-01-01 to 2025-01-31. | [readonly] 

## Example

```python
from moolabs.models.invoice_line_subscription_reference import InvoiceLineSubscriptionReference

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineSubscriptionReference from a JSON string
invoice_line_subscription_reference_instance = InvoiceLineSubscriptionReference.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineSubscriptionReference.to_json())

# convert the object into a dict
invoice_line_subscription_reference_dict = invoice_line_subscription_reference_instance.to_dict()
# create an instance of InvoiceLineSubscriptionReference from a dict
invoice_line_subscription_reference_from_dict = InvoiceLineSubscriptionReference.from_dict(invoice_line_subscription_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


