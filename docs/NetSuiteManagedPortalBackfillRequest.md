# NetSuiteManagedPortalBackfillRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] [default to True]
**include_false** | **bool** |  | [optional] [default to False]

## Example

```python
from moolabs.models.net_suite_managed_portal_backfill_request import NetSuiteManagedPortalBackfillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetSuiteManagedPortalBackfillRequest from a JSON string
net_suite_managed_portal_backfill_request_instance = NetSuiteManagedPortalBackfillRequest.from_json(json)
# print the JSON string representation of the object
print(NetSuiteManagedPortalBackfillRequest.to_json())

# convert the object into a dict
net_suite_managed_portal_backfill_request_dict = net_suite_managed_portal_backfill_request_instance.to_dict()
# create an instance of NetSuiteManagedPortalBackfillRequest from a dict
net_suite_managed_portal_backfill_request_from_dict = NetSuiteManagedPortalBackfillRequest.from_dict(net_suite_managed_portal_backfill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


