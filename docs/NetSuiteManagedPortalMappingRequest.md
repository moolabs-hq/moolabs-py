# NetSuiteManagedPortalMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_field_id** | **str** |  | 
**source_field_label** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] [default to True]
**change_reason** | **str** |  | 
**preview_only** | **bool** |  | [optional] [default to False]
**preview_audit_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.net_suite_managed_portal_mapping_request import NetSuiteManagedPortalMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetSuiteManagedPortalMappingRequest from a JSON string
net_suite_managed_portal_mapping_request_instance = NetSuiteManagedPortalMappingRequest.from_json(json)
# print the JSON string representation of the object
print(NetSuiteManagedPortalMappingRequest.to_json())

# convert the object into a dict
net_suite_managed_portal_mapping_request_dict = net_suite_managed_portal_mapping_request_instance.to_dict()
# create an instance of NetSuiteManagedPortalMappingRequest from a dict
net_suite_managed_portal_mapping_request_from_dict = NetSuiteManagedPortalMappingRequest.from_dict(net_suite_managed_portal_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


