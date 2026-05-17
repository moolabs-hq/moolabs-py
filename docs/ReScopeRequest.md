# ReScopeRequest

POST /cases/{id}/re-scope — add/remove invoices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_invoice_ids** | **List[str]** |  | [optional] 
**remove_invoice_ids** | **List[str]** |  | [optional] 

## Example

```python
from moolabs.models.re_scope_request import ReScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReScopeRequest from a JSON string
re_scope_request_instance = ReScopeRequest.from_json(json)
# print the JSON string representation of the object
print(ReScopeRequest.to_json())

# convert the object into a dict
re_scope_request_dict = re_scope_request_instance.to_dict()
# create an instance of ReScopeRequest from a dict
re_scope_request_from_dict = ReScopeRequest.from_dict(re_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


