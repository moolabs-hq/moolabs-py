# BillingInvoiceCustomerExtendedDetails

BillingInvoiceCustomerExtendedDetails is a collection of fields that are used to extend the billing party details for invoices.  These fields contain the OpenMeter specific details for the customer, that are not strictly required for the invoice itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the party (if available) | [optional] [readonly] 
**key** | **str** | An optional unique key of the party (if available) | [optional] 
**name** | **str** | Legal name or representation of the organization. | [optional] 
**tax_id** | [**BillingPartyTaxIdentity**](BillingPartyTaxIdentity.md) | The entity&#39;s legal ID code used for tax purposes. They may have other numbers, but we&#39;re only interested in those valid for tax purposes. | [optional] 
**addresses** | [**List[Address]**](Address.md) | Regular post addresses for where information should be sent if needed. | [optional] 
**usage_attribution** | [**CustomerUsageAttribution**](CustomerUsageAttribution.md) | Mapping to attribute metered usage to the customer | 

## Example

```python
from moolabs.models.billing_invoice_customer_extended_details import BillingInvoiceCustomerExtendedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInvoiceCustomerExtendedDetails from a JSON string
billing_invoice_customer_extended_details_instance = BillingInvoiceCustomerExtendedDetails.from_json(json)
# print the JSON string representation of the object
print(BillingInvoiceCustomerExtendedDetails.to_json())

# convert the object into a dict
billing_invoice_customer_extended_details_dict = billing_invoice_customer_extended_details_instance.to_dict()
# create an instance of BillingInvoiceCustomerExtendedDetails from a dict
billing_invoice_customer_extended_details_from_dict = BillingInvoiceCustomerExtendedDetails.from_dict(billing_invoice_customer_extended_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


