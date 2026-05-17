# SyncInvoicesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.sync_invoices_request import SyncInvoicesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncInvoicesRequest from a JSON string
sync_invoices_request_instance = SyncInvoicesRequest.from_json(json)
# print the JSON string representation of the object
print(SyncInvoicesRequest.to_json())

# convert the object into a dict
sync_invoices_request_dict = sync_invoices_request_instance.to_dict()
# create an instance of SyncInvoicesRequest from a dict
sync_invoices_request_from_dict = SyncInvoicesRequest.from_dict(sync_invoices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


