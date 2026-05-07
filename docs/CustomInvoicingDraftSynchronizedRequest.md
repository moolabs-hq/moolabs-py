# CustomInvoicingDraftSynchronizedRequest

Information to finalize the draft details of an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoicing** | [**CustomInvoicingSyncResult**](CustomInvoicingSyncResult.md) | The result of the synchronization. | [optional] 

## Example

```python
from moolabs.models.custom_invoicing_draft_synchronized_request import CustomInvoicingDraftSynchronizedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingDraftSynchronizedRequest from a JSON string
custom_invoicing_draft_synchronized_request_instance = CustomInvoicingDraftSynchronizedRequest.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingDraftSynchronizedRequest.to_json())

# convert the object into a dict
custom_invoicing_draft_synchronized_request_dict = custom_invoicing_draft_synchronized_request_instance.to_dict()
# create an instance of CustomInvoicingDraftSynchronizedRequest from a dict
custom_invoicing_draft_synchronized_request_from_dict = CustomInvoicingDraftSynchronizedRequest.from_dict(custom_invoicing_draft_synchronized_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


