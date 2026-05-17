# CaseInvoiceResponse

Embedded invoice within a case response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**case_id** | **str** |  | 
**invoice_id** | **str** |  | 
**invoice_number** | **str** |  | [optional] 
**amount_micros** | **int** |  | 
**paid_micros** | **int** |  | 
**disputed_micros** | **int** |  | 
**credited_micros** | **int** |  | 
**written_off_micros** | **int** |  | 
**collectible_micros** | **int** |  | [optional] 
**currency_code** | **str** |  | 
**base_currency_code** | **str** |  | 
**fx_rate_snapshot** | **str** |  | [optional] 
**amount_base_micros** | **int** |  | 
**paid_base_micros** | **int** |  | 
**disputed_base_micros** | **int** |  | 
**credited_base_micros** | **int** |  | 
**written_off_base_micros** | **int** |  | 
**collectible_base_micros** | **int** |  | [optional] 
**due_date** | **date** |  | 
**issue_date** | **date** |  | [optional] 
**predicted_pay_date** | **date** |  | [optional] 
**invoice_status** | **str** |  | [optional] [default to 'payment_pending']
**aging_bucket** | **str** |  | 
**invoice_type** | **str** |  | 
**voided_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.case_invoice_response import CaseInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseInvoiceResponse from a JSON string
case_invoice_response_instance = CaseInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(CaseInvoiceResponse.to_json())

# convert the object into a dict
case_invoice_response_dict = case_invoice_response_instance.to_dict()
# create an instance of CaseInvoiceResponse from a dict
case_invoice_response_from_dict = CaseInvoiceResponse.from_dict(case_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


