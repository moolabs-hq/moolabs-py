# NetSuiteManagedPortalMappingDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_reason** | **str** |  | 
**preview_only** | **bool** |  | [optional] [default to False]
**preview_audit_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.net_suite_managed_portal_mapping_delete_request import NetSuiteManagedPortalMappingDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetSuiteManagedPortalMappingDeleteRequest from a JSON string
net_suite_managed_portal_mapping_delete_request_instance = NetSuiteManagedPortalMappingDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NetSuiteManagedPortalMappingDeleteRequest.to_json())

# convert the object into a dict
net_suite_managed_portal_mapping_delete_request_dict = net_suite_managed_portal_mapping_delete_request_instance.to_dict()
# create an instance of NetSuiteManagedPortalMappingDeleteRequest from a dict
net_suite_managed_portal_mapping_delete_request_from_dict = NetSuiteManagedPortalMappingDeleteRequest.from_dict(net_suite_managed_portal_mapping_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


