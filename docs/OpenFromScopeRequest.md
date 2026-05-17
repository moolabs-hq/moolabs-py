# OpenFromScopeRequest

POST /cases/open-from-scope — idempotent case creation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**customer_id** | **str** |  | 
**billing_account_id** | **str** |  | [optional] 
**bill_to_entity_id** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'USD']
**invoice_ids** | **List[str]** | Invoice IDs to attach | [optional] 

## Example

```python
from moolabs.models.open_from_scope_request import OpenFromScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenFromScopeRequest from a JSON string
open_from_scope_request_instance = OpenFromScopeRequest.from_json(json)
# print the JSON string representation of the object
print(OpenFromScopeRequest.to_json())

# convert the object into a dict
open_from_scope_request_dict = open_from_scope_request_instance.to_dict()
# create an instance of OpenFromScopeRequest from a dict
open_from_scope_request_from_dict = OpenFromScopeRequest.from_dict(open_from_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


