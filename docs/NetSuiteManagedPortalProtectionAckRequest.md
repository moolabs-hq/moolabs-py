# NetSuiteManagedPortalProtectionAckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**exit_protection_mode** | **bool** |  | [optional] [default to True]

## Example

```python
from moolabs.models.net_suite_managed_portal_protection_ack_request import NetSuiteManagedPortalProtectionAckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetSuiteManagedPortalProtectionAckRequest from a JSON string
net_suite_managed_portal_protection_ack_request_instance = NetSuiteManagedPortalProtectionAckRequest.from_json(json)
# print the JSON string representation of the object
print(NetSuiteManagedPortalProtectionAckRequest.to_json())

# convert the object into a dict
net_suite_managed_portal_protection_ack_request_dict = net_suite_managed_portal_protection_ack_request_instance.to_dict()
# create an instance of NetSuiteManagedPortalProtectionAckRequest from a dict
net_suite_managed_portal_protection_ack_request_from_dict = NetSuiteManagedPortalProtectionAckRequest.from_dict(net_suite_managed_portal_protection_ack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


