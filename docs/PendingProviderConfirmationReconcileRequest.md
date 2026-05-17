# PendingProviderConfirmationReconcileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_records** | **int** |  | [optional] [default to 100]

## Example

```python
from moolabs.models.pending_provider_confirmation_reconcile_request import PendingProviderConfirmationReconcileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PendingProviderConfirmationReconcileRequest from a JSON string
pending_provider_confirmation_reconcile_request_instance = PendingProviderConfirmationReconcileRequest.from_json(json)
# print the JSON string representation of the object
print(PendingProviderConfirmationReconcileRequest.to_json())

# convert the object into a dict
pending_provider_confirmation_reconcile_request_dict = pending_provider_confirmation_reconcile_request_instance.to_dict()
# create an instance of PendingProviderConfirmationReconcileRequest from a dict
pending_provider_confirmation_reconcile_request_from_dict = PendingProviderConfirmationReconcileRequest.from_dict(pending_provider_confirmation_reconcile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


