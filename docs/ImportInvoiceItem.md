# ImportInvoiceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** |  | 
**invoice_id** | **str** |  | 
**invoice_number** | **str** |  | [optional] 
**amount_micros** | **int** |  | 
**paid_micros** | **int** |  | [optional] [default to 0]
**disputed_micros** | **int** |  | [optional] [default to 0]
**credited_micros** | **int** |  | [optional] [default to 0]
**written_off_micros** | **int** |  | [optional] [default to 0]
**currency_code** | **str** |  | [optional] [default to 'USD']
**due_date** | **date** |  | 
**issue_date** | **date** |  | [optional] 
**aging_bucket** | **str** |  | [optional] [default to 'current']
**invoice_type** | **str** |  | [optional] [default to 'usage']

## Example

```python
from moolabs.models.import_invoice_item import ImportInvoiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImportInvoiceItem from a JSON string
import_invoice_item_instance = ImportInvoiceItem.from_json(json)
# print the JSON string representation of the object
print(ImportInvoiceItem.to_json())

# convert the object into a dict
import_invoice_item_dict = import_invoice_item_instance.to_dict()
# create an instance of ImportInvoiceItem from a dict
import_invoice_item_from_dict = ImportInvoiceItem.from_dict(import_invoice_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


