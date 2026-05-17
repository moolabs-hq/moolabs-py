# CaseCreate

POST /cases — create a collection case.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**customer_id** | **str** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']
**base_currency_code** | **str** |  | [optional] 
**risk_tier** | **str** | low, medium, high, critical | [optional] [default to 'medium']
**assigned_human** | **str** |  | [optional] 
**case_owner_team** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**invoices** | [**List[CaseInvoiceCreate]**](CaseInvoiceCreate.md) |  | [optional] 

## Example

```python
from moolabs.models.case_create import CaseCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCreate from a JSON string
case_create_instance = CaseCreate.from_json(json)
# print the JSON string representation of the object
print(CaseCreate.to_json())

# convert the object into a dict
case_create_dict = case_create_instance.to_dict()
# create an instance of CaseCreate from a dict
case_create_from_dict = CaseCreate.from_dict(case_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


