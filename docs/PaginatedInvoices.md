# PaginatedInvoices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[InvoiceItem]**](InvoiceItem.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from moolabs.models.paginated_invoices import PaginatedInvoices

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInvoices from a JSON string
paginated_invoices_instance = PaginatedInvoices.from_json(json)
# print the JSON string representation of the object
print(PaginatedInvoices.to_json())

# convert the object into a dict
paginated_invoices_dict = paginated_invoices_instance.to_dict()
# create an instance of PaginatedInvoices from a dict
paginated_invoices_from_dict = PaginatedInvoices.from_dict(paginated_invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


