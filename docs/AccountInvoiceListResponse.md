# AccountInvoiceListResponse

GET /accounts/{account_id}/invoices — all invoices for an account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CaseInvoiceResponse]**](CaseInvoiceResponse.md) |  | 

## Example

```python
from moolabs.models.account_invoice_list_response import AccountInvoiceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInvoiceListResponse from a JSON string
account_invoice_list_response_instance = AccountInvoiceListResponse.from_json(json)
# print the JSON string representation of the object
print(AccountInvoiceListResponse.to_json())

# convert the object into a dict
account_invoice_list_response_dict = account_invoice_list_response_instance.to_dict()
# create an instance of AccountInvoiceListResponse from a dict
account_invoice_list_response_from_dict = AccountInvoiceListResponse.from_dict(account_invoice_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


