# NetSuiteManagedPortalBackfillRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**max_jobs** | **int** |  | [optional] [default to 1]

## Example

```python
from moolabs.models.net_suite_managed_portal_backfill_run_request import NetSuiteManagedPortalBackfillRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetSuiteManagedPortalBackfillRunRequest from a JSON string
net_suite_managed_portal_backfill_run_request_instance = NetSuiteManagedPortalBackfillRunRequest.from_json(json)
# print the JSON string representation of the object
print(NetSuiteManagedPortalBackfillRunRequest.to_json())

# convert the object into a dict
net_suite_managed_portal_backfill_run_request_dict = net_suite_managed_portal_backfill_run_request_instance.to_dict()
# create an instance of NetSuiteManagedPortalBackfillRunRequest from a dict
net_suite_managed_portal_backfill_run_request_from_dict = NetSuiteManagedPortalBackfillRunRequest.from_dict(net_suite_managed_portal_backfill_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


