# CaseInvoiceCreate

Invoice payload accepted during case creation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** |  | 
**invoice_number** | **str** |  | [optional] 
**amount_micros** | **int** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']
**base_currency_code** | **str** |  | [optional] 
**exchange_rate** | [**ExchangeRate**](ExchangeRate.md) |  | [optional] 
**amount_base_micros** | **int** |  | [optional] 
**paid_base_micros** | **int** |  | [optional] 
**disputed_base_micros** | **int** |  | [optional] 
**credited_base_micros** | **int** |  | [optional] 
**written_off_base_micros** | **int** |  | [optional] 
**due_date** | **date** |  | 
**issue_date** | **date** |  | [optional] 
**paid_micros** | **int** |  | [optional] [default to 0]
**disputed_micros** | **int** |  | [optional] [default to 0]
**credited_micros** | **int** |  | [optional] [default to 0]
**written_off_micros** | **int** |  | [optional] [default to 0]
**invoice_type** | **str** |  | [optional] [default to 'usage']

## Example

```python
from moolabs.models.case_invoice_create import CaseInvoiceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CaseInvoiceCreate from a JSON string
case_invoice_create_instance = CaseInvoiceCreate.from_json(json)
# print the JSON string representation of the object
print(CaseInvoiceCreate.to_json())

# convert the object into a dict
case_invoice_create_dict = case_invoice_create_instance.to_dict()
# create an instance of CaseInvoiceCreate from a dict
case_invoice_create_from_dict = CaseInvoiceCreate.from_dict(case_invoice_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


