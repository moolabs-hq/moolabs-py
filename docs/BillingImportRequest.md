# BillingImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**period_start** | **date** |  | 
**period_end** | **date** |  | 
**total_cost** | [**TotalCost**](TotalCost.md) |  | 
**currency** | **str** |  | [optional] [default to 'USD']
**line_items** | **List[Dict[str, object]]** |  | [optional] 
**raw_invoice_ref** | **str** |  | [optional] 

## Example

```python
from moolabs.models.billing_import_request import BillingImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingImportRequest from a JSON string
billing_import_request_instance = BillingImportRequest.from_json(json)
# print the JSON string representation of the object
print(BillingImportRequest.to_json())

# convert the object into a dict
billing_import_request_dict = billing_import_request_instance.to_dict()
# create an instance of BillingImportRequest from a dict
billing_import_request_from_dict = BillingImportRequest.from_dict(billing_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


