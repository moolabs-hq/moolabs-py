# ImportInvoicesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoices** | [**List[ImportInvoiceItem]**](ImportInvoiceItem.md) |  | 

## Example

```python
from moolabs.models.import_invoices_request import ImportInvoicesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportInvoicesRequest from a JSON string
import_invoices_request_instance = ImportInvoicesRequest.from_json(json)
# print the JSON string representation of the object
print(ImportInvoicesRequest.to_json())

# convert the object into a dict
import_invoices_request_dict = import_invoices_request_instance.to_dict()
# create an instance of ImportInvoicesRequest from a dict
import_invoices_request_from_dict = ImportInvoicesRequest.from_dict(import_invoices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


