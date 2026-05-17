# BillingImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**provider** | **str** |  | 
**billing_period_start** | **date** |  | 
**billing_period_end** | **date** |  | 
**total_cost** | **float** |  | 
**currency** | **str** |  | 
**import_source** | **str** |  | 
**imported_at** | **datetime** |  | 

## Example

```python
from moolabs.models.billing_import_response import BillingImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingImportResponse from a JSON string
billing_import_response_instance = BillingImportResponse.from_json(json)
# print the JSON string representation of the object
print(BillingImportResponse.to_json())

# convert the object into a dict
billing_import_response_dict = billing_import_response_instance.to_dict()
# create an instance of BillingImportResponse from a dict
billing_import_response_from_dict = BillingImportResponse.from_dict(billing_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


