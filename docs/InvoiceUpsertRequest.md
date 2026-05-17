# InvoiceUpsertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**netsuite_invoice_id** | **str** |  | 
**moometer_invoice_id** | **str** |  | 
**netsuite_customer_id** | **str** |  | 
**moometer_customer_id** | **str** |  | 
**invoice_number** | **str** |  | 
**invoice_date** | **date** |  | 
**due_date** | **date** |  | 
**currency_code** | **str** |  | 
**amount_micros** | **int** |  | 
**paid_micros** | **int** |  | [optional] [default to 0]
**open_micros** | **int** |  | 
**status** | **str** |  | [optional] [default to 'open']
**source_updated_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.invoice_upsert_request import InvoiceUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceUpsertRequest from a JSON string
invoice_upsert_request_instance = InvoiceUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(InvoiceUpsertRequest.to_json())

# convert the object into a dict
invoice_upsert_request_dict = invoice_upsert_request_instance.to_dict()
# create an instance of InvoiceUpsertRequest from a dict
invoice_upsert_request_from_dict = InvoiceUpsertRequest.from_dict(invoice_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


